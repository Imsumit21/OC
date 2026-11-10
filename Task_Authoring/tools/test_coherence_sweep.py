"""Tests for coherence_sweep.py; run with: cd Task_Authoring/tools && python3.12 -B -m unittest test_coherence_sweep."""
from __future__ import annotations

import contextlib
import copy
import hashlib
import io
import json
import unittest
from pathlib import Path

import coherence_sweep as cs
import selftest_sandbox

SQL, PROMPT, RECORD = cs.SQL_NAME, cs.PROMPT_NAME, cs.RECORD_NAME
PARENT_ID = "C0123ABCD/1770000000.000100"


def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:32]


def slack_row(channel: str, ts: str, user: str, text: str, thread_ts=None, parent=None, replies=0) -> str:
    return ("INSERT INTO slack.slack_messages (id, channel_id, ts, user_id, text, thread_ts_legacy, thread_parent_id, "
            f"reply_count) VALUES ('{sha(channel + '|' + ts)}', '{channel}', '{ts}', '{user}', "
            f"'{text.replace(chr(39), chr(39) * 2)}', {repr(thread_ts) if thread_ts else 'NULL'}, "
            f"{repr(sha(parent)) if parent else 'NULL'}, {replies});")


def status(result: dict, check_id: str) -> str:
    return next(c["status"] for c in result["checks"] if c["id"] == check_id)


class SweepCase(unittest.TestCase):
    """A fixture task (SQL, prompt, manifest, rubric) with two reviewer briefs and a record that passes `check`."""

    def setUp(self):
        self._tmp = selftest_sandbox.scratch_tmp("test_coherence_sweep_")
        self.root = Path(self._tmp.name)
        fx = cs._fixture_task(self.root)
        self.task, self.work, self.sql, self.prompt = fx["task"], fx["work"], fx["sql"], fx["prompt"]
        self.good = cs._fixture_record(self.task)

    def tearDown(self):
        self._tmp.cleanup()

    def write_record(self, record):
        (self.work / RECORD).write_text(json.dumps(record), encoding="utf-8")

    def run_check(self, change=None, **kw):
        record = copy.deepcopy(self.good)
        if change:
            change(record)
        self.write_record(record)
        return cs.evaluate(self.task, universe="normal", **kw)


# ---------------------------------------------------------------- brief

class BriefIsolation(SweepCase):
    SECRETS = ("SECRET", "decoy", "design note", "expected_wrong_reading", "requirement_ids", "delegation_quote",
               "rubric row", "R1")

    def plant_design_files(self):
        """Design, answers and grading that a cold reviewer must never see."""
        (self.work / "01_Scenario_Design.md").write_text("SECRET design: the decoy is T1", encoding="utf-8")
        (self.task / "08_Oracle_Events.md").write_text("SECRET oracle answer", encoding="utf-8")
        (self.work / "01_Grounding_Dossier.md").write_text("SECRET dossier", encoding="utf-8")
        (self.work / "01_Difficulty_Budget.json").write_text(json.dumps({"units": [{"cause": "SECRET-CAUSE"}]}),
                                                              encoding="utf-8")
        manifest = json.loads((self.work / "01_Hardness_Manifest.json").read_text())
        manifest["facts"].append({"key": "SECRET-FACT-KEY", "value": "SECRET-FACT-VALUE", "kind": "amount"})
        manifest["authorities"] = [{"id": "H1", "name": "SECRET-AUTHORITY", "seeded_ids": [sha(
            "C0123ABCD|1770000000.000100")], "decoy_seeded_ids": ["SECRET-DECOY-ID"]}]
        (self.work / "01_Hardness_Manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    def assert_clean(self, text):
        for secret in self.SECRETS:
            self.assertFalse(secret in text, f"{secret!r} leaked into the brief")

    def test_brief_has_prompt_and_every_record_but_no_design(self):
        self.plant_design_files()
        text = cs.build_brief(self.task, "1")["text"]
        self.assertIn(self.prompt.strip(), text)
        for rid in (PARENT_ID, "C0123ABCD/1770000300.000200", "D0BRIAN01/1770009000.000300", "comment_a1",
                    "ENG-900"):
            self.assertIn(rid, text)
        self.assertIn("still broken on Android", text)
        self.assertIn("U_BRIAN", text)                       # authors
        self.assertIn("2026-02-10T10:00:00Z", text)           # dates
        self.assertIn("## slack", text)
        self.assertIn("### linear container ENG-900", text)
        self.assert_clean(text)

    def test_brief_before_a_prompt_names_the_ask_records_only(self):
        self.plant_design_files()
        (self.task / PROMPT).write_text("", encoding="utf-8")
        text = cs.build_brief(self.task, "1")["text"]
        self.assertIn("no prompt is written yet", text)
        self.assertIn("Arthur's ask", text)
        self.assertIn(PARENT_ID, text)
        self.assert_clean(text)

    def test_revision_brief_marks_changes_and_stays_clean(self):
        self.plant_design_files()
        previous = self.root / "previous.sql"
        previous.write_text(self.sql, encoding="utf-8")
        (self.task / SQL).write_text(self.sql.replace("ok, on it", "ok, on it today"), encoding="utf-8")
        brief = cs.build_brief(self.task, "1", previous)
        self.assertIn("CHANGED in this revision", brief["text"])
        self.assertIn("next to a changed record", brief["text"])
        self.assertIn("Scope: revision (previous SQL sha256 " + hashlib.sha256(self.sql.encode()).hexdigest(),
                      brief["text"])
        self.assert_clean(brief["text"])

    def test_brief_is_deterministic_and_bound_to_the_bytes(self):
        a, b = cs.build_brief(self.task, "1"), cs.build_brief(self.task, "1")
        self.assertEqual(a["text"], b["text"])
        self.assertEqual(a["sha256"], hashlib.sha256(a["text"].encode()).hexdigest())
        self.assertNotEqual(a["sha256"], cs.build_brief(self.task, "2")["sha256"])
        head = cs._brief_header(a["text"])
        self.assertEqual(head["sql"], cs.sha256_file(self.task / SQL))
        self.assertEqual(head["prompt"], cs.sha256_file(self.task / PROMPT))
        self.assertEqual(head["scope"], "full")

    def test_brief_command_writes_only_the_brief(self):
        before = {p for p in self.task.rglob("*")}
        with contextlib.redirect_stdout(io.StringIO()) as out:
            code = cs.main(["brief", "--task-dir", str(self.task), "--reviewer", "7"])
        self.assertEqual(code, 0)
        written = {p for p in self.task.rglob("*")} - before
        self.assertEqual({p for p in written if p.is_file()}, {self.task / cs.REVIEW_DIR / "brief_7.md"})
        self.assertTrue(out.getvalue().startswith("COHERENCE SWEEP (brief): PASS"))

    def test_bad_reviewer_id_is_a_usage_error(self):
        with self.assertRaises(cs.UsageError):
            cs.build_brief(self.task, "../x")


# ---------------------------------------------------------------- candidates

class Candidates(SweepCase):
    def test_quantifiers_in_prompt_and_ask_records(self):
        found = cs.candidates(self.task, "normal")
        prompt = [q for q in found["quantifiers"] if q["where"] == "prompt"]
        self.assertEqual([q["quantifier"] for q in prompt], ["every"])
        self.assertTrue(any(q["where"] == PARENT_ID for q in found["quantifiers"]))

    def test_idioms_and_mail_boilerplate_are_not_populations(self):
        spans = cs.quantifier_spans("Is that at all possible? We all agree. Please reply to all. "
                                    "If you are not the intended recipient, any disclosure is prohibited. "
                                    "Move every open bug.")
        self.assertEqual([s["quantifier"] for s in spans], ["every"])
        self.assertEqual([s["quantifier"] for s in cs.quantifier_spans("An unverified build is a still-to-do.")],
                         ["still-to-do"])

    def test_span_cover(self):
        text = "Move every open bug  into\nLinear."
        start = text.index("every")
        self.assertTrue(cs._span_covers("every open bug into Linear", text, start, start + 5))
        self.assertFalse(cs._span_covers("open bug", text, start, start + 5))

    def test_value_conflicts_each_kind(self):
        found = cs.candidates(self.task, "normal")
        ids = {c["id"] for c in found["conflicts"]}
        self.assertTrue({"X:status:ENG-900", "X:amount:Helpshift", "X:date:due:Helpshift"} <= ids, ids)
        self.assertTrue(any(c["kind"] == "weekday" for c in found["conflicts"]))      # Fri Feb 12, 2026 is a Thursday

    def test_owner_year_and_chronology(self):
        rows = [
            slack_row("C0123ABCD", "1770000900.000100", "U_A", "Heads up: ENG-1234 is assigned to Brian. Kickoff on "
                      "Mar 3, 2025.", "1770000900.000100", None, 1),
            slack_row("C0123ABCD", "1770000100.000200", "U_B", "ok", "1770000900.000100",
                      "C0123ABCD|1770000900.000100"),
            "INSERT INTO linear.linear_issues (id, title, description, created_at) VALUES ('ENG-1234', 'Fix popup', "
            "'The popup is broken.', '2026-02-10T10:00:00Z');",
            "INSERT INTO linear.linear_comments (id, issue_id, author_id, body, created_at) VALUES ('c1', 'ENG-1234', "
            "'usr_1', 'ENG-1234 assigned to Carla. Kickoff on Mar 3, 2026.', '2026-02-09T10:00:00Z');"]
        records = cs.rs.load_records("\n".join(rows))["records"]
        found = {c["id"]: c for c in cs.conflict_candidates(records)}
        self.assertEqual([v["value"] for v in found["X:owner:ENG-1234"]["values"]], ["Brian", "Carla"])
        self.assertIn("X:year:Mar 3", found)
        self.assertIn("X:chronology:C0123ABCD/1770000100.000200", found)       # reply before its parent
        self.assertIn("X:chronology:c1", found)                                 # comment before its issue

    def test_status_words_in_links_verbs_and_finance_terms_are_ignored(self):
        self.assertIsNone(cs._status_class("Open the Carta Help Center at <https://app.carta.com/x?open=1>"))
        self.assertIsNone(cs._status_class("Each outstanding option line by holder"))
        self.assertEqual(cs._status_class("ENG-12 is not fixed yet"), "open")
        self.assertEqual(cs._status_class("ENG-12 is merged"), "done")
        self.assertIsNone(cs._status_class("ENG-12 was merged but is still open"))      # mixed: no single class

    def test_same_service_values_are_not_cross_service_conflicts(self):
        rows = [slack_row("C0123ABCD", "1770000900.000100", "U_A", "ENG-77 is done."),
                slack_row("C0123ABCD", "1770000950.000100", "U_A", "ENG-77 is still open.")]
        records = cs.rs.load_records("\n".join(rows))["records"]
        self.assertNotIn("X:status:ENG-77", {c["id"] for c in cs.conflict_candidates(records)})

    def test_known_issue_cards_strong_weak_manifest_persona(self):
        cards = [{"id": "NB-90", "title": "ENG-4321 checklist", "dont_grade": "", "why": "", "safer": "",
                  "watch": False},
                 {"id": "NB-91", "title": "Tavern Popup and Shop Icons", "dont_grade": "", "why": "", "safer": "",
                  "watch": False},
                 {"id": "NB-92", "title": "ENG-5555 state", "dont_grade": "", "why": "", "safer": "", "watch": False},
                 {"id": "NB-93", "title": "Access", "dont_grade": "", "why": "Owen leaves his channels",
                  "safer": "", "watch": False}]
        for card in cards:
            card["terms"] = cs.card_terms(card)
        records = cs.rs.load_records(slack_row("C0123ABCD", "1770000900.000100", "U_A",
                                               "ENG-4321 is done and the Tavern Popup is back"))["records"]
        touched = {k["card"]: k for k in cs.known_issue_candidates(cards, records, "", {"base": ["ENG-5555"]},
                                                                   "Owen Baker")}
        self.assertEqual(touched["NB-90"]["level"], "strong")
        self.assertEqual(touched["NB-90"]["via"], ["records"])
        self.assertEqual(touched["NB-91"]["level"], "weak")
        self.assertEqual(touched["NB-92"]["via"], ["manifest"])
        self.assertEqual(touched["NB-93"]["via"], ["persona"])
        plain = {k["card"] for k in cs.known_issue_candidates(cards, records, "")}
        self.assertEqual(plain, {"NB-90", "NB-91"})

    def test_real_cards_parse(self):
        self.assertTrue(cs.load_cards("normal"))
        self.assertTrue(cs.load_cards("synthcut"))
        self.assertEqual(cs.load_cards("nowhere"), [])
        found = cs.candidates(self.task, "normal")
        self.assertTrue(any(k["card"] == "NB-14" and k["level"] == "strong" for k in found["known_issues"]))

    def test_fact_terms_skip_design_labels(self):
        found = cs.candidates(self.task, "normal")
        self.assertEqual(found["facts"][0]["terms"], ["Helpshift", "$1,800"])
        files = {"manifest": {"facts": [{"key": "returned wire rule", "value": "Take a notice as paid unless one of us "
                                                                                "has said the money came back"},
                                        {"key": "Leapblock", "value": "407,944"},
                                        {"key": "ENG-2455 bucket", "value": "Marketing", "aliases": ["Lauren"]}]}}
        terms = {f["fact"]: f["terms"] for f in cs.fact_candidates(files)}
        self.assertEqual(terms["returned wire rule"], [])
        self.assertEqual(terms["Leapblock"], ["Leapblock", "407,944"])
        self.assertEqual(terms["ENG-2455 bucket"], ["ENG-2455", "Lauren", "Marketing"])
        requests = cs.base_requests(cs.fact_candidates(files))
        self.assertEqual(sorted(requests), sorted(cs.BASE_SERVICES))
        self.assertIn("search-many", cs.base_commands(self.task, requests)[0])

    def test_sibling_candidates_list_unchecked_family(self):
        record = copy.deepcopy(self.good)
        record["siblings"][0]["families"] = [{"kind": "same_thread", "checked_ids": []}]
        self.write_record(record)
        found = cs.candidates(self.task, "normal")
        self.assertTrue(any(s["kind"] == "same_thread" and "ENG-900" in s["unchecked"] for s in found["siblings"]))

    def test_candidates_result_shape_and_cover(self):
        result = cs.candidates_result(self.task, "normal", "no")
        self.assertEqual(result["verdict"], "WARN")
        self.assertEqual(result["bound_to"][SQL], cs.sha256_file(self.task / SQL))
        self.assertIn("candidates.quantifiers", {c["id"] for c in result["checks"]})
        self.assertEqual(status(result, "candidates.base"), "SKIP")
        self.write_record(self.good)
        covered = cs.candidates_result(self.task, "normal", "no")
        self.assertEqual(status(covered, "candidates.conflicts"), "PASS")
        self.assertEqual(status(covered, "candidates.known_issues"), "PASS")
        text = cs.candidates_text(self.task, covered)
        self.assertTrue(text.startswith("COHERENCE SWEEP (candidates): "))
        self.assertIn("[PASS] candidates.conflicts", text)

    def test_candidates_are_deterministic(self):
        a = json.dumps(cs.candidates_result(self.task, "normal", "no"), sort_keys=True)
        b = json.dumps(cs.candidates_result(self.task, "normal", "no"), sort_keys=True)
        self.assertEqual(a, b)


# ---------------------------------------------------------------- check

class Check(SweepCase):
    def test_complete_record_passes(self):
        result = self.run_check()
        self.assertEqual(result["verdict"], "PASS", cs.to_text(result))
        self.assertTrue(cs.to_text(result).startswith("COHERENCE SWEEP (full): PASS"))
        self.assertIn(RECORD, " ".join(result["bound_to"]))

    def test_no_record_fails(self):
        result = cs.evaluate(self.task, universe="normal")
        self.assertEqual(result["verdict"], "FAIL")
        self.assertEqual(result["scope"], "none")

    def test_missing_sql_is_a_fail_result_not_an_exception(self):
        (self.task / SQL).unlink()
        result = cs.evaluate(self.task)
        self.assertEqual(result["verdict"], "FAIL")
        self.assertEqual(result["checks"][0]["id"], "sweep.bound")
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(cs.main(["check", "--task-dir", str(self.task)]), 2)
            self.assertEqual(cs.main(["check", "--task-dir", str(self.root / "nowhere")]), 2)

    def test_bound(self):
        self.assertEqual(status(self.run_check(lambda d: d["bound_to"].update({SQL: "0" * 64})), "sweep.bound"),
                         "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["bound_to"].update({PROMPT: "0" * 64})), "sweep.bound"),
                         "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d.update({"schema": "v0"})), "sweep.bound"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d.update({"forks": {"F1": 1}})), "sweep.bound"), "FAIL")
        result = self.run_check(lambda d: d.update({"scope": "partial"}))
        self.assertEqual(result["verdict"], "FAIL")
        self.assertEqual(result["scope"], "none")

    def test_a_later_sql_edit_makes_the_record_stale(self):
        self.write_record(self.good)
        (self.task / SQL).write_text(self.sql.replace("ok, on it", "ok, on it today"), encoding="utf-8")
        result = cs.evaluate(self.task, universe="normal")
        self.assertEqual(status(result, "sweep.bound"), "FAIL")
        self.assertEqual(status(result, "sweep.reviewers"), "FAIL")     # the briefs were built from the old bytes

    def test_weird_types_never_raise(self):
        for bad in ({"reviewers": 5}, {"forks": [5, "x"]}, {"siblings": [{"families": 7, "record_ids": 3}]},
                    {"open_sets": [{"span": 5}]}, {"base_consistency": [{"fact": None, "conflicts": 4}]},
                    {"known_issues": "NB-1"}, {"bound_to": []}):
            result = self.run_check(lambda d, bad=bad: d.update(bad))
            self.assertIn(result["verdict"], ("FAIL", "WARN", "PASS"))

    def test_reviewers(self):
        self.assertEqual(status(self.run_check(lambda d: d["reviewers"].pop()), "sweep.reviewers"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["reviewers"][0].update({"brief_sha256": "1" * 64})),
                                "sweep.reviewers"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["reviewers"][0].update({"model": ""})),
                                "sweep.reviewers"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["reviewers"][1].update({"findings": "nope.json"})),
                                "sweep.reviewers"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["reviewers"][1].update({"id": "1"})),
                                "sweep.reviewers"), "FAIL")
        (self.task / cs.REVIEW_DIR / "brief_2.md").unlink()
        self.assertEqual(status(self.run_check(), "sweep.reviewers"), "WARN")       # brief not kept

    def test_brief_from_other_bytes_fails(self):
        other = cs.build_brief(self.task, "1")["text"].replace(cs.sha256_file(self.task / SQL), "a" * 64)
        (self.task / cs.REVIEW_DIR / "brief_1.md").write_text(other, encoding="utf-8")
        result = self.run_check(lambda d: d["reviewers"][0].update(
            {"brief_sha256": hashlib.sha256(other.encode()).hexdigest()}))
        self.assertEqual(status(result, "sweep.reviewers"), "FAIL")

    def test_findings(self):
        self.assertEqual(status(self.run_check(lambda d: d["forks"][0].update({"sources": []})), "sweep.findings"),
                         "FAIL")
        ok = self.run_check(lambda d: (d["forks"][0].update({"sources": []}),
                                       d["dismissed"].append({"source": "1:F1", "reason": "same outcome"})))
        self.assertEqual(status(ok, "sweep.findings"), "PASS")
        no_reason = self.run_check(lambda d: (d["forks"][0].update({"sources": []}),
                                              d["dismissed"].append({"source": "1:F1", "reason": ""})))
        self.assertEqual(status(no_reason, "sweep.findings"), "FAIL")
        (self.task / cs.REVIEW_DIR / "findings_2.json").write_text("{}", encoding="utf-8")
        self.assertEqual(status(self.run_check(), "sweep.findings"), "FAIL")        # no lists

    def test_forks(self):
        def fork(**kw):
            return lambda d: d["forks"][0].update(kw)
        self.assertEqual(status(self.run_check(fork(status="open")), "sweep.forks"), "FAIL")
        self.assertEqual(status(self.run_check(fork(status="open", material=False)), "sweep.forks"), "PASS")
        self.assertEqual(status(self.run_check(fork(status="maybe")), "sweep.forks"), "FAIL")
        self.assertEqual(status(self.run_check(fork(settled={"record_ids": ["comment_gone"], "sql_revision": "r"})),
                                "sweep.forks"), "FAIL")
        self.assertEqual(status(self.run_check(fork(settled={"record_ids": ["comment_a1"]})), "sweep.forks"), "FAIL")
        self.assertEqual(status(self.run_check(fork(reading_b={"reading": "x"})), "sweep.forks"), "FAIL")
        self.assertEqual(status(self.run_check(fork(reason="")), "sweep.forks"), "FAIL")

    def test_both_fair_needs_both_figures(self):
        self.assertEqual(status(self.run_check(lambda d: d["forks"][0].update(
            {"status": "both_fair", "both_fair": {"figure_a": "9"}})), "sweep.forks"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["forks"][0].update(
            {"status": "both_fair", "both_fair": {"figure_a": "9", "figure_b": "10"}})), "sweep.forks"), "FAIL")
        result = self.run_check(lambda d: d["forks"][0].update(
            {"status": "both_fair", "both_fair": {"figure_a": "9", "figure_b": "10", "rubric_accepts_both": True}}))
        self.assertEqual(result["verdict"], "PASS")

    def test_prompt_sentence_warns(self):
        result = self.run_check(lambda d: d["forks"][0].update(
            {"status": "prompt_sentence", "prompt_sentence": {"sentence": "tell him when done", "reason": "r"}}))
        self.assertEqual(status(result, "sweep.forks"), "PASS")
        self.assertEqual(status(result, "sweep.prompt_sentences"), "WARN")
        self.assertEqual(result["verdict"], "WARN")
        missing = self.run_check(lambda d: d["forks"][0].update(
            {"status": "prompt_sentence", "prompt_sentence": {"sentence": "a sentence nobody wrote", "reason": "r"}}))
        self.assertEqual(status(missing, "sweep.forks"), "FAIL")

    def test_open_sets(self):
        self.assertEqual(status(self.run_check(lambda d: d["open_sets"].pop(0)), "sweep.open_sets"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["open_sets"].pop(1)), "sweep.open_sets"), "WARN")
        self.assertEqual(status(self.run_check(lambda d: d["open_sets"][0]["census"].update({"ids": ["gone"]})),
                                "sweep.open_sets"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["open_sets"][0]["census"].update({"count": 5})),
                                "sweep.open_sets"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["open_sets"][0].update(
            {"census": {"count": 0, "ids": [], "base_ids": []}})), "sweep.open_sets"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["open_sets"][0].update({"rule": ""})),
                                "sweep.open_sets"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["open_sets"][0].update({"span": "every closed bug"})),
                                "sweep.open_sets"), "FAIL")
        idiom = self.run_check(lambda d: d["open_sets"].__setitem__(0, {
            "span": "every open bug", "where": "prompt", "not_a_population": "the bugs list is the population "
                                                                          "of another task"}))
        self.assertEqual(status(idiom, "sweep.open_sets"), "PASS")

    def test_siblings(self):
        def defect(**kw):
            return lambda d: d["siblings"][0].update(kw)
        self.assertEqual(status(self.run_check(defect(families=[])), "sweep.siblings"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["siblings"][0]["families"].pop()), "sweep.siblings"),
                         "FAIL")                                        # one family kind not listed
        self.assertEqual(status(self.run_check(lambda d: d["siblings"][0]["families"][0].update(
            {"checked_ids": ["else"]})), "sweep.siblings"), "FAIL")      # the issue update in the thread unchecked
        self.assertEqual(status(self.run_check(lambda d: d["siblings"][0]["families"][0].update(
            {"checked_ids": [], "none": ""})), "sweep.siblings"), "FAIL")
        self.assertEqual(status(self.run_check(defect(status="open")), "sweep.siblings"), "FAIL")
        self.assertEqual(status(self.run_check(defect(fix={})), "sweep.siblings"), "FAIL")
        self.assertEqual(status(self.run_check(defect(fix={"record_ids": ["gone"], "sql_revision": "r"})),
                                "sweep.siblings"), "FAIL")
        self.assertEqual(status(self.run_check(defect(status="not_a_defect")), "sweep.siblings"), "FAIL")
        self.assertEqual(status(self.run_check(defect(status="not_a_defect", reason="designed")), "sweep.siblings"),
                         "PASS")
        self.assertEqual(status(self.run_check(defect(status="known_issue")), "sweep.siblings"), "FAIL")
        self.assertEqual(status(self.run_check(defect(status="known_issue", card="NB-14")), "sweep.siblings"), "PASS")

    def test_base(self):
        self.assertEqual(status(self.run_check(lambda d: d["base_consistency"].clear()), "sweep.base"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["base_consistency"][0].update({"result_count": None})),
                                "sweep.base"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["base_consistency"][0].update(
            {"conflicts": [], "disposition": ""})), "sweep.base"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["base_consistency"][0].update(
            {"conflicts": [{"id": "x", "disposition": ""}]})), "sweep.base"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["base_consistency"][0].update(
            {"result_count": 0, "conflicts": [], "disposition": ""})), "sweep.base"), "PASS")
        manifest = json.loads((self.work / "01_Hardness_Manifest.json").read_text())
        manifest["facts"] = []
        (self.work / "01_Hardness_Manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        self.assertEqual(status(self.run_check(lambda d: d["base_consistency"].clear()), "sweep.base"), "SKIP")

    def test_known_issues(self):
        self.assertEqual(status(self.run_check(lambda d: d["known_issues"].clear()), "sweep.known_issues"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["known_issues"][0].update({"disposition": ""})),
                                "sweep.known_issues"), "FAIL")
        record = copy.deepcopy(self.good)
        record.pop("universe")
        self.write_record(record)
        self.assertEqual(status(cs.evaluate(self.task), "sweep.known_issues"), "WARN")    # universe unknown

    def test_conflicts_warn_only(self):
        result = self.run_check(lambda d: d["conflicts"].clear())
        self.assertEqual(status(result, "sweep.conflicts"), "WARN")
        self.assertEqual(result["verdict"], "WARN")

    def test_evaluate_is_deterministic(self):
        self.write_record(self.good)
        a = json.dumps(cs.evaluate(self.task, universe="normal"), sort_keys=True)
        self.assertEqual(a, json.dumps(cs.evaluate(self.task, universe="normal"), sort_keys=True))

    def test_template_is_a_starting_record(self):
        record = cs.template(self.task, None, "normal")
        self.assertEqual(record["schema"], cs.SCHEMA)
        self.assertEqual(record["bound_to"][SQL], cs.sha256_file(self.task / SQL))
        spans = [(o["where"], o["span"]) for o in record["open_sets"]]
        self.assertEqual(len(spans), len(set(spans)))
        self.write_record(record)
        self.assertEqual(cs.evaluate(self.task, universe="normal")["verdict"], "FAIL")   # empty entries


# ---------------------------------------------------------------- revision scope and the chain

class RevisionChain(SweepCase):
    """rev1 (full sweep) -> rev2 (revision sweep) -> current (revision sweep), each link checked by sha256."""

    def store(self, rev: str, sql: str, record: dict) -> tuple:
        folder = self.work / "run_forensics" / rev
        folder.mkdir(parents=True, exist_ok=True)
        (folder / SQL).write_text(sql, encoding="utf-8")
        (folder / RECORD).write_text(json.dumps(record), encoding="utf-8")
        return folder / SQL, folder / RECORD

    def revision_record(self, previous_sql: Path, previous_record: Path) -> dict:
        record = cs._fixture_record(self.task, previous_sql)
        record.update({"scope": "revision", "previous_sql_sha256": cs.sha256_file(previous_sql),
                       "changed_record_ids": [], "previous_sweep": {
                           "path": previous_record.relative_to(self.task).as_posix(),
                           "sha256": cs.sha256_file(previous_record)}})
        diff = cs.rs.diff_files(previous_sql, self.task / SQL)
        record["changed_record_ids"] = sorted({e["id"] for e in diff["entries"] if e["state"] != "removed"})
        return record

    def setUp(self):
        super().setUp()
        self.rev1_sql, self.rev1_record = self.store("rev1", self.sql, self.good)
        self.sql2 = self.sql.replace("ok, on it", "ok, on it today")
        (self.task / SQL).write_text(self.sql2, encoding="utf-8")
        rev2 = self.revision_record(self.rev1_sql, self.rev1_record)
        self.rev2_sql, self.rev2_record = self.store("rev2", self.sql2, rev2)
        self.sql3 = self.sql2.replace("see the ENG-2403 checklist", "see the ENG-2403 checklist, Brian")
        (self.task / SQL).write_text(self.sql3, encoding="utf-8")
        self.good = self.revision_record(self.rev2_sql, self.rev2_record)

    def test_two_links_back_to_a_full_sweep_pass(self):
        result = self.run_check()
        self.assertEqual(result["verdict"], "PASS", cs.to_text(result))
        self.assertEqual(result["scope"], "revision")
        self.assertEqual(status(result, "sweep.chain"), "PASS")
        self.assertEqual(self.good["changed_record_ids"], ["D0BRIAN01/1770009000.000300"])

    def test_tampered_earlier_link_fails(self):
        data = json.loads(self.rev1_record.read_text())
        data["forks"] = []
        self.rev1_record.write_text(json.dumps(data), encoding="utf-8")       # rev2 recorded the old hash
        self.assertEqual(status(self.run_check(), "sweep.chain"), "FAIL")

    def test_chain_must_end_in_a_full_sweep(self):
        data = json.loads(self.rev1_record.read_text())
        data["scope"] = "revision"
        self.rev1_record.write_text(json.dumps(data), encoding="utf-8")
        rev2 = json.loads(self.rev2_record.read_text())
        rev2["previous_sweep"]["sha256"] = cs.sha256_file(self.rev1_record)
        self.rev2_record.write_text(json.dumps(rev2), encoding="utf-8")
        result = self.run_check(lambda d: d["previous_sweep"].update({"sha256": cs.sha256_file(self.rev2_record)}))
        self.assertEqual(status(result, "sweep.chain"), "FAIL")

    def test_chain_problems(self):
        self.assertEqual(status(self.run_check(lambda d: d.update({"changed_record_ids": []})), "sweep.chain"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["previous_sweep"].update({"sha256": "2" * 64})),
                                "sweep.chain"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d.update({"previous_sql_sha256": "3" * 64})),
                                "sweep.chain"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d.pop("previous_sweep")), "sweep.chain"), "FAIL")
        self.assertEqual(status(self.run_check(lambda d: d["previous_sweep"].update({"path": "../../x.json"})),
                                "sweep.chain"), "FAIL")
        # the previous sweep must be the sweep of the previous SQL
        result = self.run_check(lambda d: d["previous_sweep"].update(
            {"path": self.rev1_record.relative_to(self.task).as_posix(), "sha256": cs.sha256_file(self.rev1_record)}))
        self.assertEqual(status(result, "sweep.chain"), "FAIL")

    def test_previous_sql_is_found_by_hash_or_passed(self):
        self.assertEqual(self.run_check(previous_sql=self.rev2_sql)["verdict"], "PASS")
        self.assertEqual(status(self.run_check(previous_sql=self.rev1_sql), "sweep.chain"), "FAIL")
        self.rev2_sql.unlink()
        self.assertEqual(status(self.run_check(), "sweep.chain"), "FAIL")

    def test_scoped_brief_must_match_the_record_scope(self):
        full = cs.build_brief(self.task, "1")
        (self.task / cs.REVIEW_DIR / "brief_1.md").write_text(full["text"], encoding="utf-8")
        result = self.run_check(lambda d: d["reviewers"][0].update({"brief_sha256": full["sha256"]}))
        self.assertEqual(status(result, "sweep.reviewers"), "FAIL")

    def test_out_of_scope_entries_are_carried_but_must_be_closed(self):
        far = "C0123ABCD/1770000300.000200"          # the reply: not changed and not next to the changed DM
        carried = self.run_check(lambda d: d["siblings"].append(
            {"id": "D2", "defect": "old", "record_ids": [far], "status": "not_a_defect", "reason": "x",
             "families": []}))
        self.assertEqual(status(carried, "sweep.siblings"), "PASS", cs.to_text(carried))
        still_open = self.run_check(lambda d: d["siblings"].append(
            {"id": "D2", "defect": "old", "record_ids": [far], "status": "open", "families": []}))
        self.assertEqual(status(still_open, "sweep.siblings"), "FAIL")
        in_scope = self.run_check(lambda d: d["siblings"].append(
            {"id": "D3", "defect": "new", "record_ids": ["D0BRIAN01/1770009000.000300"], "status": "not_a_defect",
             "reason": "x", "families": []}))
        self.assertEqual(status(in_scope, "sweep.siblings"), "FAIL")           # in scope: needs its families
        fork_open = self.run_check(lambda d: d["forks"].append(
            {"id": "F9", "record_ids": [far], "status": "open", "material": True}))
        self.assertEqual(status(fork_open, "sweep.forks"), "FAIL")

    def test_settling_record_changed_in_the_revision_needs_a_recheck(self):
        dm = "D0BRIAN01/1770009000.000300"
        result = self.run_check(lambda d: d["forks"][0].update(
            {"record_ids": [dm], "settled": {"record_ids": [dm], "sql_revision": "rev3"}}))
        self.assertEqual(status(result, "sweep.forks"), "FAIL")
        result = self.run_check(lambda d: d["forks"][0].update(
            {"record_ids": [dm], "settled": {"record_ids": [dm], "sql_revision": "rev3"},
             "rechecked_sql_sha256": cs.sha256_file(self.task / SQL)}))
        self.assertEqual(status(result, "sweep.forks"), "PASS")

    def test_template_for_a_revision(self):
        record = cs.template(self.task, self.rev2_sql, "normal")
        self.assertEqual(record["scope"], "revision")
        self.assertEqual(record["previous_sql_sha256"], cs.sha256_file(self.rev2_sql))
        self.assertEqual(record["changed_record_ids"], ["D0BRIAN01/1770009000.000300"])


if __name__ == "__main__":
    unittest.main()
