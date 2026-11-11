#!/usr/bin/env python3
"""Tests for path_exposure.py: is each planned miss off the path a run sweeps anyway?

Synthetic SQL and a stub universe only (path_exposure.StubView); no base data is read.

  cd Task_Authoring/tools && python3.12 -B -m unittest test_path_exposure -v
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import re
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import path_exposure as pe  # noqa: E402
import selftest_sandbox  # noqa: E402

SLACK_COLS = "(id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy)"


def slack_row(mid, ts, channel, user, text, root=None):
    parent = "NULL" if root is None else "'p'"
    return (f"INSERT INTO slack.slack_messages {SLACK_COLS} VALUES ('{mid}', '{ts}', '{channel}', 'message', "
            f"'{user}', '{text}', {parent}, '{root or ts}');\n")


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = selftest_sandbox.scratch_tmp("path_exposure_test_")
        self.td = Path(self._tmp.name) / "task"
        self.stub = pe._write_fixture(self.td)
        self.wf = self.td / "Working_Files"

    def tearDown(self):
        self._tmp.cleanup()

    def run_tool(self, **kw):
        kw.setdefault("view", pe.StubView(self.stub))
        return pe.evaluate(self.td, **kw)

    def units(self, **kw):
        return {u["id"]: u for u in self.run_tool(**kw)["units"]}

    def codes(self, unit):
        return sorted({r["code"] for r in unit.get("reasons") or []})

    def edit_json(self, name, change):
        path = self.wf / name
        data = json.loads(path.read_text())
        change(data)
        path.write_text(json.dumps(data, indent=1))

    def add_sql(self, text):
        path = self.td / "01_Universe_Inject.sql"
        path.write_text(path.read_text() + text)

    def add_unit(self, uid, rid, service="slack", role="anchor", injected=True):
        self.edit_json(pe.BUDGET_NAME, lambda b: b["units"].append(
            {"id": uid, "role": role, "habit": {"service": service, "action": "read"},
             "decider": {"service": service, "record_id": rid, "injected": injected}}))


class ReasonCodes(Base):
    def test_keyword_is_a_name_the_task_supplies(self):
        u = self.units()["U_KEYWORD"]
        self.assertEqual(u["verdict"], "EXPOSED")
        kw = next(r for r in u["reasons"] if r["code"] == "keyword")
        self.assertEqual(kw["evidence"]["keyword"], "Brightvale")
        self.assertEqual(kw["evidence"]["source"], "a cohort entity name")
        self.assertEqual(kw["evidence"]["search"], {"results": 1, "newer": 0})     # the search and its result count

    def test_a_cohort_entity_keyword_alone_is_marked_weakest(self):
        self.add_sql(slack_row("m_proj", "1770100800.000100", "C0QUIET0009", "EMPLOYEE_0003_SLACK_ID",
                               "orchid is off the table", "1760000900.000100"))
        self.add_unit("U_PROJECT", "C0QUIET0009/1770100800.000100")
        units = self.units()
        self.assertTrue(units["U_KEYWORD"]["only_entity_keyword"])                # 'Brightvale', a truth key
        self.assertFalse(units["U_PROJECT"]["only_entity_keyword"])               # 'Orchid', a prompt name
        self.assertIn("weakest basis", pe._fmt(units["U_KEYWORD"]))

    def test_de_named_reply_does_not_trip_keyword(self):
        u = self.units()["U_OFF"]
        self.assertEqual((u["verdict"], u["reasons"]), ("OFF-PATH", []))

    def test_prompt_name_counts_and_people_do_not(self):
        self.add_sql(slack_row("m_proj", "1770100800.000100", "C0QUIET0009", "EMPLOYEE_0003_SLACK_ID",
                               "orchid is off the table, Vera said so", "1760000900.000100"))
        self.add_unit("U_PROJECT", "C0QUIET0009/1770100800.000100")
        u = self.units()["U_PROJECT"]
        words = [r["evidence"]["keyword"] for r in u["reasons"] if r["code"] == "keyword"]
        self.assertEqual(words, ["Orchid"])                                      # 'Vera' is a person, not a keyword

    def test_keyword_in_a_record_search_does_not_return_is_a_note(self):
        self.add_sql("INSERT INTO linear.linear_issues (id, identifier, title, description, project_id, team_id, "
                     "created_at) VALUES ('ZZZ-9', 'ZZZ-9', 'Old chore', 'x', 'proj-else', 'team_Z', "
                     "'2026-01-01T00:00:00Z');\n"
                     "INSERT INTO linear.linear_comments (id, issue_id, author_id, body, created_at) VALUES "
                     "('cmt_far', 'ZZZ-9', 'usr_x', 'Brightvale pulled out', '2026-02-03T00:00:00Z');\n")
        self.add_unit("U_FAR", "cmt_far", "linear")
        u = self.units()["U_FAR"]
        self.assertEqual(u["verdict"], "OFF-PATH")                              # a comment on a ticket outside the set
        self.assertTrue(any("not returned by a text search" in n for n in u["notes"]), u["notes"])

    def test_named_container_reply_in_the_anchor_thread(self):
        u = self.units()["U_NAMED"]
        self.assertEqual(self.codes(u), ["named_container"])
        self.assertEqual(u["reasons"][0]["evidence"]["path_record"], "anchor A1")

    def test_named_container_by_words_in_a_rules_document(self):
        self.edit_json(pe.MANIFEST_NAMES[0], lambda m: None)
        sql = self.td / "01_Universe_Inject.sql"
        sql.write_text(sql.read_text().replace("One of the answers came in later.",
                                               "One of the answers came in later. See #sidebar for the rest."))
        self.stub["channels"]["C0QUIET0003"] = {"name": "sidebar", "kind": "public"}
        self.add_sql(slack_row("m_side", "1770100900.000100", "C0QUIET0003", "EMPLOYEE_0003_SLACK_ID",
                               "they dropped out"))
        self.add_unit("U_SIDE", "C0QUIET0003/1770100900.000100")
        units = self.units()
        self.assertIn("named_container", self.codes(units["U_SIDE"]))             # a root post in the named channel
        self.assertEqual(units["U_OFF"]["verdict"], "OFF-PATH")                    # a reply under another parent there

    def test_root_post_in_a_read_channel_only_inside_the_window(self):
        self.assertEqual(self.codes(self.units()["U_ROOT"]), ["root_or_self"])
        self.add_sql(slack_row("m_early", "1767000000.000100", "C0HUBCHAN01", "EMPLOYEE_0003_SLACK_ID",
                               "they are out"))
        self.add_unit("U_EARLY", "C0HUBCHAN01/1767000000.000100")
        u = self.units()["U_EARLY"]
        self.assertEqual(u["verdict"], "OFF-PATH")
        self.assertTrue(any("before the task window opens" in n for n in u["notes"]), u["notes"])

    def test_comment_on_a_cohort_item_and_tab_of_a_listed_sheet(self):
        self.assertEqual(self.codes(self.units()["U_SELF"]), ["root_or_self"])
        self.add_sql("INSERT INTO gsheets.sheets_spreadsheets (spreadsheet_id, title) VALUES ('f_sheet0001', "
                     "'Renewal tracker');\n"
                     "INSERT INTO gsheets.sheets_sheets (spreadsheet_id, sheet_id, title, \"index\", grid_json) VALUES "
                     "('f_sheet0001', 7, 'Later', 1, '[[\"vendor\", \"gone\"]]');\n")
        self.edit_json(pe.MANIFEST_NAMES[0], lambda m: m["ask_fragments"].append(
            {"id": "K9", "service": "gsheets", "container": "f_sheet0001", "locator": "f_sheet0001",
             "seeded_ids": ["f_sheet0001"], "delegated_by_record": "f_rules00001", "delegation_quote": "x"}))
        self.add_unit("U_TAB", "f_sheet0001#7", "gsheets")
        self.assertEqual(self.codes(self.units()["U_TAB"]), ["root_or_self"])

    def test_inline_review_comment_on_a_set_item_is_a_note(self):
        self.add_sql("INSERT INTO github.github_pull_requests (id, repo_id, number, title, body, author_login, "
                     "created_at) VALUES ('org/repo#5', 'org/repo', 5, 'Fix it', 'body', 'dev', "
                     "'2026-02-02T00:00:00Z');\n"
                     "INSERT INTO github.github_review_comments (id, pr_id, author_login, body, created_at) VALUES "
                     "('org/repo#5#rc_1', 'org/repo#5', 'dev', 'this still breaks', '2026-02-03T00:00:00Z');\n")
        self.edit_json(pe.MANIFEST_NAMES[0], lambda m: m["ask_fragments"].append(
            {"id": "K8", "service": "github", "container": "org/repo#5", "locator": "org/repo#5",
             "seeded_ids": ["org/repo#5"], "delegated_by_record": "f_rules00001", "delegation_quote": "x"}))
        self.add_unit("U_INLINE", "org/repo#5#rc_1", "github")
        u = self.units()["U_INLINE"]
        self.assertEqual(u["verdict"], "OFF-PATH")
        self.assertTrue(any("second read inside the item" in n for n in u["notes"]), u["notes"])

    def test_sweep_window_for_a_searched_sender_states_the_rule(self):
        u = self.units()["U_SWEEP"]
        sweep = next(r for r in u["reasons"] if r["code"] == "sweep_window")
        self.assertEqual(sweep["evidence"]["sender"], "Vera Quill")
        self.assertEqual(sweep["evidence"]["why_searched"], "named in the prompt")
        self.assertEqual(sweep["evidence"]["results"], 4)                        # 3 base messages + the record
        self.assertIn(f"at most {pe.SENDER_SWEEP_MAX}", sweep["detail"])

    def test_a_busy_sender_is_not_a_sweep(self):
        self.stub["records"] += [["slack.slack_messages", {"id": f"w{i}", "ts": f"17700{i:05d}.000100",
                                                           "channel_id": "C0BUSY00001",
                                                           "user_id": "EMPLOYEE_0002_SLACK_ID", "text": "chatter"}]
                                 for i in range(pe.SENDER_SWEEP_MAX + 5)]
        u = self.units()["U_SWEEP"]
        self.assertEqual(u["verdict"], "OFF-PATH")
        self.assertTrue(any("too many for a sweep" in n for n in u["notes"]), u["notes"])

    def test_the_requester_is_not_a_searched_sender(self):
        self.add_sql(slack_row("m_boss", "1770101000.000100", "C0QUIET0008", "EMPLOYEE_0001_SLACK_ID",
                               "scrap that one", "1760000800.000100"))
        self.add_unit("U_BOSS", "C0QUIET0008/1770101000.000100")
        u = self.units()["U_BOSS"]
        self.assertEqual(u["verdict"], "OFF-PATH")
        self.assertTrue(any("wrote an anchor" in n for n in u["notes"]), u["notes"])

    def test_pointer_by_link_from_another_injected_record(self):
        u = self.units()["U_POINTER"]
        self.assertEqual(self.codes(u), ["pointer"])
        self.assertEqual(u["reasons"][0]["evidence"]["pointing_record"], "C0OTHER0002/1770100450.000100")

    def test_pointer_by_id_in_the_prompt(self):
        (self.td / "04_Prompt.txt").write_text("Sort out the Orchid renewals; start from "
                                               "C0QUIET0003/1770100600.000100.\n")
        u = self.units()["U_OFF"]
        self.assertEqual(self.codes(u), ["pointer"])
        self.assertEqual(u["reasons"][0]["evidence"]["pointing_record"], "the prompt")

    def test_fairness_pointer_is_a_note_until_it_names_the_container(self):
        u = self.units()["U_FAIR"]
        self.assertEqual(u["verdict"], "OFF-PATH")
        self.assertTrue(any(n.startswith("allowed fairness pointer") for n in u["notes"]), u["notes"])

        def name_it(m):
            m["ask_fragments"][1]["delegation_quote"] = "the late answer is in a thread in the quiet channel"
        self.edit_json(pe.MANIFEST_NAMES[0], name_it)
        u = self.units()["U_FAIR"]
        self.assertEqual(self.codes(u), ["pointer"])
        self.assertIn("declared delegation K2", u["reasons"][0]["detail"])

    def test_an_indefinite_medium_word_names_no_container(self):
        def loose(m):
            m["ask_fragments"][1]["delegation_quote"] = "someone answered in a thread or a channel later"
        self.edit_json(pe.MANIFEST_NAMES[0], loose)
        u = self.units()["U_FAIR"]
        self.assertEqual((u["verdict"], u["reasons"]), ("OFF-PATH", []))       # Samuel rev5: 'on a ticket or a card'
        self.assertTrue(any(n.startswith("allowed fairness pointer") for n in u["notes"]), u["notes"])

    def test_a_copy_of_the_same_message_is_not_a_pointer(self):
        cols = "(id, thread_id, user_email, subject, from_email, body_text, date)"
        for box in ("me@example.com", "odd@example.com"):
            self.add_sql(f"INSERT INTO gmail.gmail_messages {cols} VALUES ('{box}/<copy@x>', '{box}/950', '{box}', "
                         "'Renewal answer for the quiet vendor', 'odd@example.com', 'they declined', "
                         "'2026-01-04T09:00:00Z');\n")
        self.add_unit("U_COPY", "me@example.com/<copy@x>", "gmail")
        self.assertNotIn("pointer", self.codes(self.units()["U_COPY"]))
        self.add_sql(slack_row("m_subj", "1770101100.000100", "C0QUIET0007", "EMPLOYEE_0003_SLACK_ID",
                               "see the mail Renewal answer for the quiet vendor", "1760001000.000100"))
        self.assertIn("pointer", self.codes(self.units()["U_COPY"]))           # a different record naming it still is

    def test_a_record_the_persona_cannot_open_points_nowhere(self):
        self.stub["sql_hidden"] = ["C0OTHER0002/1770100450.000100"]             # the row carrying the thread link
        u = self.units()["U_POINTER"]
        self.assertEqual((u["verdict"], u["reasons"]), ("OFF-PATH", []))

    def test_a_keyword_past_the_first_page_is_a_note(self):
        self.stub["records"] += [["slack.slack_messages", {"id": f"bv{i}", "ts": f"17702{i:05d}.000100",
                                                           "channel_id": "C0BUSY00001",
                                                           "user_id": "EMPLOYEE_0003_SLACK_ID",
                                                           "text": "Brightvale weekly numbers"}]
                                 for i in range(pe.KEYWORD_FIRST_PAGE)]
        u = self.units()["U_KEYWORD"]
        self.assertEqual(u["verdict"], "OFF-PATH")
        self.assertTrue(any("past the first page" in n for n in u["notes"]), u["notes"])

    def test_a_fragment_author_is_not_a_searched_sender(self):
        (self.td / "04_Prompt.txt").write_text("Can you sort out the Orchid renewals the way the ask lays it out?\n")
        res = self.run_tool()
        self.assertEqual(res["searched_senders"], {})                          # Vera wrote fragment K3 only
        u = {x["id"]: x for x in res["units"]}["U_SWEEP"]
        self.assertNotIn("sweep_window", self.codes(u))

    def test_a_big_team_is_not_the_set(self):
        cols = "(id, identifier, title, description, project_id, team_id, created_at)"
        self.add_sql(f"INSERT INTO linear.linear_issues {cols} VALUES ('ZZT-1', 'ZZT-1', 'Vendor intake', "
                     "'intake', NULL, 'team_X', '2026-02-01T00:00:00Z');\n"
                     f"INSERT INTO linear.linear_issues {cols} VALUES ('ZZT-5', 'ZZT-5', 'Old chore', 'x', NULL, "
                     "'team_X', '2026-02-01T00:00:00Z');\n"
                     "INSERT INTO linear.linear_comments (id, issue_id, author_id, body, created_at) VALUES "
                     "('cmt_team', 'ZZT-5', 'usr_x', 'they walked away', '2026-02-03T00:00:00Z');\n")
        self.edit_json(pe.MANIFEST_NAMES[0], lambda m: m["ask_fragments"].append(
            {"id": "K7", "service": "linear", "container": "ZZT-1", "locator": "ZZT-1", "seeded_ids": ["ZZT-1"],
             "delegated_by_record": "f_rules00001", "delegation_quote": "x"}))
        self.add_unit("U_TEAM", "cmt_team", "linear")
        self.assertEqual(self.codes(self.units()["U_TEAM"]), ["root_or_self"])  # a small team is listed whole
        self.stub["records"] += [["linear.linear_issues", {"id": f"ZZT-{100 + i}", "identifier": f"ZZT-{100 + i}",
                                                           "title": "chore", "team_id": "team_X"}]
                                 for i in range(pe.SET_LIST_MAX)]
        units = self.units()
        self.assertEqual(units["U_TEAM"]["verdict"], "OFF-PATH")                # Samuel rev5/rev6 FILT: filtered
        self.assertEqual(self.codes(units["U_SELF"]), ["root_or_self"])          # the small project item still is

    def test_thin_search_in_a_quiet_mailbox(self):
        u = self.units()["U_THIN"]
        thin = [r for r in u["reasons"] if r["code"] == "thin_search"]
        self.assertTrue(thin and all(r["evidence"]["results"] < 10 for r in thin), thin)
        self.assertIn("sweep_window", self.codes(u))

    def test_thin_threshold_comes_from_the_policy(self):
        policy = {"path_exposure": {"thin_search_min_results": 1}, "modes": {"exposure.units": "block"}}
        res = self.run_tool(policy=policy)
        by = {u["id"]: u for u in res["units"]}
        self.assertNotIn("thin_search", self.codes(by["U_KEYWORD"]))
        self.assertEqual((res["thresholds"]["thin_search_min_results"], res["gate_mode"]), (1, "block"))


class Verdicts(Base):
    def test_unverified_when_the_record_cannot_be_read(self):
        units = self.units()
        self.assertEqual(units["U_MISSING"]["verdict"], "UNVERIFIED")
        self.assertIn("no INSERT in the SQL", units["U_MISSING"]["why"])
        self.add_unit("U_NOBASE", "C0NOBASE001/1769000000.000100", injected=False)
        self.add_unit("U_NOID", "")
        self.add_unit("U_WAREHOUSE", "snowflake:ANALYTICS.X.Y", "snowflake", injected=False)
        units = self.units()
        self.assertIn("neither the SQL nor the persona's base data", units["U_NOBASE"]["why"])
        self.assertIn("no decider.record_id", units["U_NOID"]["why"])
        self.assertIn("warehouse rows are not read", units["U_WAREHOUSE"]["why"])
        self.assertEqual({units[k]["verdict"] for k in ("U_NOBASE", "U_NOID", "U_WAREHOUSE")}, {"UNVERIFIED"})

    def test_unverified_when_the_persona_cannot_open_it(self):
        self.stub["sql_hidden"] = ["C0QUIET0003/1770100600.000100"]
        u = self.units()["U_OFF"]
        self.assertEqual(u["verdict"], "UNVERIFIED")
        self.assertIn("persona cannot open", u["why"])

    def test_no_base_data_never_reads_as_off_path(self):
        res = self.run_tool(view=pe.NullView("no context in this test"))
        by = {u["id"]: u for u in res["units"]}
        self.assertEqual(by["U_OFF"]["verdict"], "UNVERIFIED")
        self.assertEqual(by["U_KEYWORD"]["verdict"], "EXPOSED")                   # what the SQL alone shows still counts
        self.assertEqual(by["U_BASE"]["verdict"], "UNVERIFIED")
        status = {c["id"]: c["status"] for c in res["checks"]}
        self.assertEqual(status["exposure.base"], "WARN")

    def test_base_decider_is_read_through_the_view(self):
        u = self.units()["U_BASE"]
        self.assertEqual((u["verdict"], u["record"]["source"]), ("OFF-PATH", "base"))

    def test_check_lines_and_overall_verdict(self):
        res = self.run_tool()
        status = {c["id"]: c["status"] for c in res["checks"]}
        self.assertEqual(res["verdict"], "FAIL")
        self.assertEqual(status["exposure.bound"], "PASS")
        self.assertEqual(status["exposure.units"], "FAIL")
        self.assertEqual(status["exposure.unit.U_KEYWORD"], "FAIL")
        self.assertEqual(status["exposure.unit.U_OFF"], "PASS")
        self.assertEqual(status["exposure.unit.U_MISSING"], "WARN")
        self.assertEqual(status["exposure.unit.U_REAL"], "SKIP")                 # realism units are skipped
        self.assertEqual(set(res) >= {"tool", "version", "verdict", "bound_to", "checks"}, True)
        self.assertEqual((res["tool"], res["version"]), ("path_exposure", 1))
        text = pe.to_text(res).splitlines()
        self.assertRegex(text[0], r"^PATH EXPOSURE \(.+\): FAIL$")
        for line in text[1:]:
            self.assertRegex(line, r"^\[(PASS|FAIL|WARN|SKIP)\] exposure\.[\w.]+: .+")
        rules = next(c["detail"] for c in res["checks"] if c["id"] == "exposure.rules")
        self.assertIn("window = 7 days before the earliest dated anchor", rules)
        self.assertIn("Vera Quill (named in the prompt)", rules)

    def test_warn_when_only_unverified_and_pass_when_all_off_path(self):
        def keep(ids):
            return lambda b: b.__setitem__("units", [u for u in b["units"] if u["id"] in ids])
        self.edit_json(pe.BUDGET_NAME, keep({"U_OFF", "U_FAIR", "U_REAL"}))
        self.assertEqual(self.run_tool()["verdict"], "PASS")
        self.add_unit("U_GONE", "C0NOWHERE01/1770100700.000100")
        res = self.run_tool()
        self.assertEqual(res["verdict"], "WARN")
        self.assertEqual({c["id"]: c["status"] for c in res["checks"]}["exposure.units"], "WARN")
        self.edit_json(pe.BUDGET_NAME, keep({"U_REAL"}))
        self.assertEqual(self.run_tool()["verdict"], "WARN")                      # nothing to check is not a pass


class Sources(Base):
    def test_no_prompt_uses_the_manifest_and_says_so(self):
        (self.td / "04_Prompt.txt").unlink()
        res = self.run_tool()
        src = next(c["detail"] for c in res["checks"] if c["id"] == "exposure.sources")
        self.assertIn("no 04_Prompt.txt yet", src)
        self.assertEqual(res["stage"], "injection")
        self.assertIn("Orchid", res["keywords"])                                 # from the anchor's prompt_reference
        self.assertNotIn("04_Prompt.txt", res["bound_to"])
        self.assertRegex(pe.to_text(res).splitlines()[0], r"^PATH EXPOSURE \(injection stage, \d+ unit\(s\)\): FAIL$")

    def test_draft_manifest_is_read_when_the_final_is_absent(self):
        (self.wf / pe.MANIFEST_NAMES[0]).rename(self.wf / pe.MANIFEST_NAMES[1])
        res = self.run_tool()
        self.assertIn("Working_Files/" + pe.MANIFEST_NAMES[1], res["bound_to"])
        self.assertEqual({u["id"]: u for u in res["units"]}["U_NAMED"]["verdict"], "EXPOSED")

    def test_missing_inputs_fail_the_bound_check(self):
        (self.wf / pe.BUDGET_NAME).unlink()
        res = self.run_tool()
        self.assertEqual(res["verdict"], "FAIL")
        self.assertEqual((res["checks"][0]["id"], res["checks"][0]["status"]), ("exposure.bound", "FAIL"))
        self.assertIn("budget file missing", res["checks"][0]["detail"])
        self.assertEqual(res["units"], [])


class Binding(Base):
    def test_bound_to_hashes_the_files_read(self):
        res = self.run_tool()
        self.assertEqual(sorted(res["bound_to"]), ["01_Universe_Inject.sql", "04_Prompt.txt",
                                                   "Working_Files/01_Difficulty_Budget.json",
                                                   "Working_Files/01_Gradable_Surface.json",
                                                   "Working_Files/01_Hardness_Manifest.json"])
        for rel, digest in res["bound_to"].items():
            self.assertEqual(digest, hashlib.sha256((self.td / rel).read_bytes()).hexdigest(), rel)
        before = res["bound_to"]["01_Universe_Inject.sql"]
        self.add_sql("-- a comment changes the bytes\n")
        self.assertNotEqual(self.run_tool()["bound_to"]["01_Universe_Inject.sql"], before)

    def test_write_stores_the_bound_report(self):
        res = self.run_tool(today="2026-11-11")
        out = pe.write_report(self.td, res)
        self.assertEqual(out, self.wf / pe.OUT_NAME)
        stored = json.loads(out.read_text())
        self.assertEqual(stored["bound_to"], res["bound_to"])
        self.assertEqual((stored["verdict"], stored["today"]), ("FAIL", "2026-11-11"))
        self.assertEqual([p.name for p in self.wf.iterdir() if p.name.startswith(".")], [])   # no temp file left

    def test_deterministic(self):
        a = json.dumps(self.run_tool(), sort_keys=True)
        b = json.dumps(self.run_tool(), sort_keys=True)
        self.assertEqual(a, b)
        self.assertNotRegex(a, r"20\d\d-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+")           # no wall-clock stamp


class Cli(Base):
    def call(self, argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                code = pe.main(argv)
            except SystemExit as exc:
                code = exc.code
        return code, out.getvalue(), err.getvalue()

    def test_usage_errors_exit_2(self):
        self.assertEqual(self.call([])[0], 2)
        self.assertEqual(self.call(["check", "--task-dir", str(self.td / "nope")])[0], 2)
        self.assertEqual(self.call(["check", "--task-dir", str(self.td), "--today", "tomorrow"])[0], 2)
        self.assertEqual(self.call(["backtest", "--units", str(self.td / "nope.json")])[0], 2)

    def test_check_without_a_task_context_still_reports(self):
        # the fixture has no 00_Assigments.md, so no base view can be built: units the SQL alone exposes still fail
        code, out, _err = self.call(["check", "--task-dir", str(self.td), "--json"])
        res = json.loads(out)
        self.assertEqual((code, res["verdict"]), (1, "FAIL"))
        status = {c["id"]: c["status"] for c in res["checks"]}
        self.assertEqual(status["exposure.base"], "WARN")
        self.assertFalse((self.wf / pe.OUT_NAME).exists())                        # no --write, no file


class Pieces(unittest.TestCase):
    def test_person_key_joins_services(self):
        self.assertEqual(pe.person_key("EMPLOYEE_0038_SLACK_ID"), "EMPLOYEE_0038")
        self.assertEqual(pe.person_key("user_EMPLOYEE_0038"), "EMPLOYEE_0038")
        self.assertEqual(pe.person_key('"Bo" <Bo@Example.com>', {"bo@example.com": "EMPLOYEE_0001"}), "EMPLOYEE_0001")
        self.assertIsNone(pe.person_key(None))

    def test_when_reads_the_date_forms_in_the_data(self):
        self.assertEqual(pe._iso(pe._when("1770000000.000100")), "2026-02-02T02:40:00Z")
        self.assertEqual(pe._iso(pe._when("2026-02-02T02:40:00Z")), "2026-02-02T02:40:00Z")
        # the Postgres text form appears in archived SQL (18 rows); it is read, with the offset applied
        self.assertEqual(pe._iso(pe._when("2024-10-03 15:20:00+00")), "2024-10-03T15:20:00Z")
        self.assertEqual(pe._iso(pe._when("2024-10-03 15:20:00+0200")), "2024-10-03T13:20:00Z")
        self.assertIsNone(pe._when("sometime in October"))                          # an unreadable form is not guessed
        self.assertIsNone(pe._when("None"))

    def test_slack_reply_and_root_shapes(self):
        root = pe.normalise("slack.slack_messages", {"id": "a", "ts": "1.1", "channel_id": "C1", "text": "x",
                                                     "thread_ts_legacy": "1.1"})
        reply = pe.normalise("slack.slack_messages", {"id": "b", "ts": "2.2", "channel_id": "C1", "text": "y",
                                                      "thread_ts_legacy": "1.1"})
        self.assertEqual((root["kind"], reply["kind"]), ("slack_root", "slack_reply"))
        self.assertEqual(reply["container"], root["container"])
        self.assertEqual(reply["ids"], ["C1/2.2", "b"])

    def test_no_forbidden_literal(self):
        text = (HERE / "path_exposure.py").read_text() + (HERE / "test_path_exposure.py").read_text()
        self.assertNotIn("Evals/" + "task_inputs", text)
        self.assertIsNone(re.search(r"\bmatch\s+\w+:\s*$", text, re.M))            # Python 3.9 syntax only


if __name__ == "__main__":
    unittest.main()
