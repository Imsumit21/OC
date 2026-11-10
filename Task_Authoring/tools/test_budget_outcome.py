"""Tests for budget_outcome.py. Run: cd Task_Authoring/tools && python3.12 -B -m unittest test_budget_outcome"""
from __future__ import annotations

import ast
import base64
import contextlib
import io
import json
import unittest
from pathlib import Path
from unittest import mock

import budget_outcome as bo
import selftest_sandbox

HERE = Path(__file__).resolve().parent
WF = "Working_Files"
ANCHOR = "C0123ABCD/1700000000.000100"
MAIL = "robert@hg.co/<CAPBs_a5shT3@mail.gmail.com>"
INJECTED_MAIL_TEXT = ("Robert, one thing for the page: the four thousand that went to JPMorgan in August was a move to "
                      "our own Chase account, not a payment to anyone, so leave it out of every bucket")
SQL_MAIL = ("INSERT INTO gmail.gmail_messages (id, thread_id, user_email, subject, body_text)\nVALUES "
            "('robert@hg.co/<inj0001@mail.gmail.com>', 'robert@hg.co/990001', 'robert@hg.co', 'Chase', '"
            + INJECTED_MAIL_TEXT + "');\n")


def unit(uid, role, record_id, find_rate=None, service="slack", **decider):
    d = dict({"service": service, "record_id": record_id}, **decider)
    out = {"id": uid, "role": role, "decider": d, "mechanism": uid}
    if find_rate is not None:
        out["find_rate"] = find_rate
    return out


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = selftest_sandbox.scratch_tmp("test_budget_outcome_")
        self.td = Path(self._tmp.name) / "task"
        (self.td / WF).mkdir(parents=True)
        (self.td / "06_PreCheck_Trajectory").mkdir()
        self.pre = self.td / "06_PreCheck_Trajectory" / "trajectory.json"
        self.budget(bo._budget())
        (self.td / bo.SQL).write_text(bo._SQL + SQL_MAIL)
        self.policy = bo.load_policy()

    def tearDown(self):
        self._tmp.cleanup()

    def budget(self, doc):
        (self.td / WF / bo.BUDGET).write_text(json.dumps(doc, indent=1) + "\n")

    def units(self, *units, design="D1"):
        self.budget({"schema": "difficulty-budget-v1", "design_id": design, "revision": "rev1", "mode": "easy",
                     "weight_basis": "surface", "total_weight": 40, "units": list(units)})

    def run_calls(self, calls, path=None):
        p = path or self.pre
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(bo._events(calls)) + "\n")
        return p

    def compare(self, calls=None, trajectory=None):
        if calls is not None:
            self.run_calls(calls)
        r = bo.evaluate(self.td, trajectory, self.policy)
        return r, {u["unit"]: u for u in r["units"]}

    def run_main(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = bo.main(list(argv))
        return code, out.getvalue(), err.getvalue()


THREAD_READ = ("mcp__hg__slack_conversations_replies", {"channel_id": "C0123ABCD", "thread_ts": "1700000000.000001"},
               {"ok": True, "messages": [{"ts": 1700000000.000001, "text": "root"},
                                         {"ts": 1700000000.0001, "text": "small correction",
                                          "thread_ts": 1700000000.000001}]})


class CompareTests(Base):
    def test_self_test_passes(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            bo._self_test()
        self.assertIn("self-test: ok", out.getvalue())

    def test_go_when_no_anchor_is_opened(self):
        r, u = self.compare(bo._go_calls())
        self.assertEqual((r["outcome"], r["verdict"]), ("GO", "PASS"))
        self.assertEqual(r["hand_review"], [])
        self.assertEqual(r["opened_anchors"], [])
        self.assertFalse(u["U1"]["opened"])
        self.assertTrue(u["U1"]["consistent"])
        self.assertTrue(u["U3"]["opened"])              # a variance unit is consistent either way
        self.assertTrue(u["U3"]["consistent"])
        self.assertTrue(u["U4"]["consistent"])
        self.assertFalse(u["U4"]["opened"])
        self.assertEqual(set(r) >= {"tool", "version", "verdict", "bound_to", "checks"}, True)
        self.assertTrue(all(len(v) == 64 for v in r["bound_to"].values()))

    def test_no_go_names_the_anchor_and_the_step(self):
        r, u = self.compare(bo._go_calls() + [THREAD_READ])
        self.assertEqual((r["outcome"], r["verdict"]), ("NO-GO", "FAIL"))
        self.assertEqual(r["opened_anchors"], ["U1"])
        self.assertEqual((u["U1"]["first_step"], u["U1"]["how"], u["U1"]["tool"]),
                         (9, "result", "slack_conversations_replies"))
        self.assertEqual(u["U1"]["first_event"], 17)    # 0-based event index of the call in the export
        self.assertFalse(u["U1"]["consistent"])
        self.assertEqual([h["unit"] for h in r["hand_review"]], ["U1"])
        outcome = [c for c in r["checks"] if c["id"] == "precheck.budget_outcome"][0]
        self.assertEqual(outcome["status"], "FAIL")
        self.assertIn("anchor U1", outcome["detail"])
        self.assertIn("step 9", outcome["detail"])
        text = bo.to_text(r)
        self.assertEqual(text.splitlines()[0], "BUDGET OUTCOME: NO-GO")
        self.assertIn("HAND-REVIEW: U1", text)

    def test_what_does_not_count_as_opened(self):
        cases = {
            "pointer": ("mcp__hg__slack_search_public_and_private", {"query": "x"},
                        {"messages": [{"ts": 1700000050.5, "thread_ts": "1700000000.000100"}]}),
            "search query": ("mcp__hg__slack_search_public_and_private", {"query": "1700000000.000100 motmot"},
                             {"messages": []}),
            "write": ("mcp__hg__slack_send_message", {"channel_id": "C0123ABCD", "thread_ts": "1700000000.000100"},
                      {"ok": True, "ts": 1700000000.0001}),
            "mention in text": ("mcp__hg__linear_get_issue", {"id": "ENG-5"},
                                {"id": "ENG-5", "description": "see C0123ABCD/1700000000.000100 for the note"}),
            "agent brief": ("Agent", {"prompt": "open C0123ABCD thread 1700000000.000100"}, "ok"),
        }
        for name, call in cases.items():
            with self.subTest(name=name):
                _, u = self.compare([call])
                self.assertFalse(u["U1"]["opened"], name)

    def test_listings_are_listed_not_opened(self):
        calls = [("mcp__hg__gmail_search_messages", {"query": "x"}, {"messages": [{"id": MAIL, "threadId": "t"}]}),
                 ("mcp__hg__gmail_get_message", {"message_id": "robert@hg.co/<other@mail>", "format": "minimal"},
                  {"id": MAIL}),
                 ("mcp__hg__gdrive_list_recent_files", {}, {"files": [{"id": "f_abcdef123456"}]})]
        _, u = self.compare(calls)
        self.assertFalse(u["U2"]["opened"])
        self.assertEqual(u["U2"]["listed_step"], 1)
        self.assertFalse(u["U4"]["opened"])
        self.assertEqual(u["U4"]["listed_step"], 3)
        _, u = self.compare(calls + [("mcp__hg__gmail_get_messages_batch", {"message_ids": [MAIL]}, bo._SPILL)])
        self.assertTrue(u["U2"]["opened"])              # asked for by id: counts even when the result spilled
        self.assertEqual((u["U2"]["how"], u["U2"]["first_step"]), ("argument", 4))

    def test_slack_ts_forms(self):
        for value in (1700000000.0001, "1700000000.000100", "1700000000.0001"):
            with self.subTest(value=value):
                _, u = self.compare([("mcp__hg__slack_conversations_history", {"channel_id": "C0123ABCD"},
                                      {"messages": [{"ts": value, "text": "x"}]})])
                self.assertTrue(u["U1"]["opened"])
        _, u = self.compare([("Bash", {"command": "cat f"},
                              "https://hg.slack.com/archives/C0123ABCD/p1700000000000100 " + bo._ANCHOR_TEXT)])
        self.assertTrue(u["U1"]["opened"])
        _, u = self.compare([("mcp__hg__slack_conversations_history", {"channel_id": "C0123ABCD"},
                              {"messages": [{"ts": 1700000000.000101, "text": "x"}]})])
        self.assertFalse(u["U1"]["opened"])             # a neighbouring ts is another message

    def test_slack_row_id_is_resolved_through_the_sql(self):
        self.units(unit("A", "anchor", "msg_anchor_0001", [0.0, 0.15], injected=True),
                   unit("B", "anchor", "0123456789abcdef0123456789abcdef", [0.0, 0.15]))
        r, u = self.compare([THREAD_READ])
        self.assertTrue(u["A"]["opened"])
        self.assertEqual(u["A"]["id_form"], "slack")
        self.assertIn("C0123ABCD/1700000000.000100", u["A"]["resolved"])
        self.assertIn("unmatchable", u["B"])
        ids = [c for c in r["checks"] if c["id"] == "precheck.id_forms"]
        self.assertEqual(ids[0]["status"], "WARN")
        self.assertIn("B", ids[0]["detail"])

    def test_gmail_thread_decider(self):
        self.units(unit("T", "anchor", "robert@hg.co/185", [0.0, 0.15], service="gmail"),
                   unit("I", "anchor", "robert@hg.co/990001", [0.0, 0.15], service="gmail", injected=True))
        listed = ("mcp__hg__gmail_search_messages", {"query": "x"},
                  {"messages": [{"id": "robert@hg.co/<m1@mail>", "threadId": "robert@hg.co/185"}]})
        _, u = self.compare([listed])
        self.assertFalse(u["T"]["opened"])
        self.assertEqual(u["T"]["listed_step"], 1)
        full = ("mcp__hg__gmail_get_messages_batch", {"message_ids": ["robert@hg.co/<m1@mail>"], "format": "full"},
                {"messages": [{"id": "robert@hg.co/<m1@mail>", "threadId": "robert@hg.co/185",
                               "payload": {"body": {"data": "aGk="}}}]})
        _, u = self.compare([listed, full])
        self.assertTrue(u["T"]["opened"])               # one of the thread's messages came back in full
        self.assertEqual((u["T"]["first_step"], u["T"]["how"]), (2, "result"))
        _, u = self.compare([("mcp__hg__gmail_get_thread", {"thread_id": "robert@hg.co/185"}, bo._SPILL)])
        self.assertEqual(u["T"]["how"], "argument")
        # an injected thread: the SQL gives its message ids, so a spilled batch by message id still counts
        _, u = self.compare([("mcp__hg__gmail_get_messages_batch",
                              {"message_ids": ["robert@hg.co/<inj0001@mail.gmail.com>"]}, bo._SPILL)])
        self.assertTrue(u["I"]["opened"])
        self.assertEqual(u["I"]["how"], "argument")

    def test_base64_mail_body_is_decoded_for_the_text_window(self):
        self.units(unit("M", "anchor", "robert@hg.co/<inj0001@mail.gmail.com>", [0.0, 0.15], service="gmail",
                        injected=True))
        data = base64.urlsafe_b64encode(INJECTED_MAIL_TEXT.encode()).decode().rstrip("=")
        self.assertIn("own chase account", bo.result_text({"payload": {"body": {"data": data}}}))
        # the body arrives under another id (a forwarded copy): only the decoded text shows it
        _, u = self.compare([("mcp__hg__gmail_get_message", {"message_id": "arthur@hg.co/<fwd@mail>"},
                              {"id": "arthur@hg.co/<fwd@mail>", "payload": {"body": {"data": data}}})])
        self.assertTrue(u["M"]["opened"])
        self.assertEqual(u["M"]["how"], "body")
        self.assertTrue(u["M"]["body_window"])

    def test_github_and_plain_ids(self):
        _, u = self.compare([("mcp__hg__github_list_pull_requests", {"repo": "zm-client"},
                              {"items": [{"number": 12, "title": "fix"}, {"number": 13}]}),
                             ("mcp__hg__github_get_pull_request", {"repo": "other", "pull_number": 12}, {"number": 12})])
        self.assertTrue(u["U5"]["opened"])
        self.assertEqual(u["U5"]["first_step"], 1)
        _, u = self.compare([("mcp__hg__github_get_pull_request", {"repo": "other", "pull_number": 12},
                              {"number": 12, "title": "x"})])
        self.assertFalse(u["U5"]["opened"])             # number 12 of another repo
        _, u = self.compare([("mcp__hg__linear_list_issues", {"project": "P"},
                              {"issues": [{"id": "ENG-770"}, {"id": "ENG-7"}]})])
        self.assertFalse(u["U3"]["opened"])             # ENG-77 is neither ENG-770 nor ENG-7
        _, u = self.compare([("mcp__hg__linear_list_issues", {"project": "P"}, {"issues": [{"identifier": "ENG-77"}]})])
        self.assertTrue(u["U3"]["opened"])

    def test_spilled_container_read_is_reported_not_counted(self):
        spill = ("mcp__hg__slack_conversations_history", {"channel_id": "C0123ABCD"}, bo._SPILL)
        r, u = self.compare([spill])
        self.assertEqual((r["outcome"], r["verdict"]), ("GO", "WARN"))
        self.assertFalse(u["U1"]["opened"])
        self.assertEqual(u["U1"]["spilled_container_reads"], [1])
        self.assertEqual(r["unverified"], ["U1"])
        # the same read named by channel name: the id is learnt from another result of the run
        by_name = ("mcp__hg__slack_read_channel", {"channel_id": "#ops"}, bo._SPILL)
        info = ("mcp__hg__slack_search_public_and_private", {"query": "x"},
                {"messages": [{"ts": 1.0, "channel_info": {"id": "C0123ABCD", "name": "ops"}}]})
        r, u = self.compare([by_name, info])
        self.assertEqual(u["U1"]["spilled_container_reads"], [1])
        # the run then reads the record out of the file through Bash: opened, by its text
        r, u = self.compare([spill, ("Bash", {"command": "python3 x.py"}, "Leonard: " + bo._ANCHOR_TEXT)])
        self.assertEqual(r["outcome"], "NO-GO")
        self.assertEqual((u["U1"]["how"], u["U1"]["first_step"]), ("body", 2))

    def test_expectation_by_role_and_range(self):
        p = self.policy
        self.assertEqual(bo.expectation({"role": "anchor"}, p), "not opened")
        self.assertEqual(bo.expectation({"role": "variance", "find_rate": [0.0, 0.1]}, p), "either")
        self.assertEqual(bo.expectation({"role": "realism"}, p), "not judged")
        self.assertEqual(bo.expectation({"find_rate": [0.0, 0.15]}, p), "not opened")
        self.assertEqual(bo.expectation({"find_rate": [0.85, 1.0]}, p), "opened")
        self.assertEqual(bo.expectation({"find_rate": [0.35, 0.65]}, p), "either")
        self.units(unit("N", None, "ENG-900", [0.9, 1.0], service="linear"))
        r, u = self.compare([("mcp__hg__linear_get_issue", {"id": "ENG-1"}, {"id": "ENG-1"})])
        self.assertFalse(u["N"]["consistent"])          # declared nearly always found, and not opened
        self.assertEqual([h["unit"] for h in r["hand_review"]], ["N"])
        self.assertEqual(r["outcome"], "GO")            # only an opened anchor makes NO-GO

    def test_unit_without_a_decider_fails_loudly(self):
        self.units({"id": "X", "role": "anchor", "decider": {"service": "slack"}})
        r, _ = self.compare([THREAD_READ])
        self.assertEqual(r["verdict"], "FAIL")
        self.assertTrue(any(c["id"] == "precheck.deciders" and "X" in c["detail"] for c in r["checks"]))
        with self.assertRaises(bo.UsageError):         # a budget defect is never logged as a pre-check
            bo.write_outcome(self.td, r)
        self.assertFalse((self.td / WF / bo.LOG).exists())

    def test_no_sql_still_compares_by_id(self):
        (self.td / bo.SQL).unlink()
        r, u = self.compare([THREAD_READ])
        self.assertTrue(u["U1"]["opened"])
        self.assertIsNone(r["sql_sha256"])
        self.assertEqual([c for c in r["checks"] if c["id"] == "precheck.trajectory"][0]["status"], "WARN")


class WriteAndStopRuleTests(Base):
    def test_write_binds_and_logs_once(self):
        self.run_calls(bo._go_calls() + [THREAD_READ])
        code, out, _ = self.run_main("compare", "--task-dir", str(self.td), "--write", "--today", "2026-11-11")
        self.assertEqual(code, 1)
        self.assertEqual(out.splitlines()[0], "BUDGET OUTCOME: NO-GO")
        stored = json.loads((self.td / WF / bo.OUTCOME).read_text())
        self.assertEqual(stored["schema"], "budget-outcome-v1")
        self.assertEqual(stored["bound_to"], {
            f"{WF}/{bo.BUDGET}": bo.sha256_file(self.td / WF / bo.BUDGET),
            bo.SQL: bo.sha256_file(self.td / bo.SQL),
            "06_PreCheck_Trajectory/trajectory.json": bo.sha256_file(self.pre)})
        log = json.loads((self.td / WF / bo.LOG).read_text())
        self.assertEqual(log["entries"], [{
            "design_id": "D1", "budget_revision": "rev1", "sql_sha256": bo.sha256_file(self.td / bo.SQL),
            "trajectory_sha256": bo.sha256_file(self.pre), "verdict": "NO-GO", "opened_anchors": ["U1"],
            "date": "2026-11-11"}])
        code, out, _ = self.run_main("compare", "--task-dir", str(self.td), "--write")
        self.assertEqual(code, 1)
        self.assertIn("nothing appended", out)
        self.assertEqual(len(json.loads((self.td / WF / bo.LOG).read_text())["entries"]), 1)

    def test_compare_without_write_touches_nothing(self):
        self.run_calls(bo._go_calls())
        code, out, _ = self.run_main("compare", "--task-dir", str(self.td), "--json")
        self.assertEqual(code, 0)
        data = json.loads(out)
        self.assertEqual((data["tool"], data["version"], data["outcome"]), ("budget_outcome", 1, "GO"))
        self.assertTrue(all(set(c) == {"id", "status", "detail"} for c in data["checks"]))
        self.assertFalse((self.td / WF / bo.OUTCOME).exists())
        self.assertFalse((self.td / WF / bo.LOG).exists())

    def test_stop_rule_counts_no_go_per_design(self):
        code, out, _ = self.run_main("stop-rule", "--task-dir", str(self.td))
        self.assertEqual(code, 0)
        self.assertIn("[PASS] precheck.stop_rule: 0 NO-GO", out)
        for extra in ([], [("mcp__hg__linear_get_issue", {"id": "ENG-1"}, {"id": "ENG-1"})]):
            self.run_calls(bo._go_calls() + [THREAD_READ] + extra)
            self.run_main("compare", "--task-dir", str(self.td), "--write")
        code, out, _ = self.run_main("stop-rule", "--task-dir", str(self.td))
        self.assertEqual(code, 1)
        self.assertEqual(out.splitlines()[0], "BUDGET OUTCOME (stop-rule): FAIL")
        self.assertIn("STOP: two pre-checks on design D1 missed the budget — return to /create-scenario for a "
                      "redesign, not another patch", out.splitlines())
        code, out, _ = self.run_main("stop-rule", "--task-dir", str(self.td), "--json")
        data = json.loads(out)
        self.assertEqual((code, data["no_go"], data["limit"], data["checks"][0]["id"]), (1, 2, 2, "precheck.stop_rule"))
        # a GO on the same design does not count; a redesign starts again at zero
        self.run_calls(bo._go_calls())
        self.run_main("compare", "--task-dir", str(self.td), "--write")
        self.assertEqual(bo.stop_rule(self.td, self.policy)["no_go"], 2)
        doc = bo._budget()
        doc["design_id"] = "D2"
        self.budget(doc)
        r = bo.stop_rule(self.td, self.policy)
        self.assertEqual((r["verdict"], r["no_go"], r["stop"]), ("PASS", 0, None))

    def test_stop_rule_reads_the_limit_from_the_policy(self):
        self.run_calls(bo._go_calls() + [THREAD_READ])
        bo.write_outcome(self.td, bo.evaluate(self.td, policy=self.policy))
        strict = {"precheck": {"stop_after_no_go": 1}, "budget": {}}
        r = bo.stop_rule(self.td, strict)
        self.assertEqual(r["verdict"], "FAIL")
        self.assertTrue(r["stop"].startswith("STOP: one pre-checks on design D1"))

    def test_write_refuses_a_read_only_root(self):
        target = bo.WS / "Evals" / "x" / bo.OUTCOME
        with mock.patch.object(bo.tempfile, "mkstemp", side_effect=AssertionError("must not write")), \
                mock.patch.object(Path, "mkdir", side_effect=AssertionError("must not create folders")):
            with self.assertRaises(Exception) as caught:
                bo.atomic_write(target, "{}", "the budget outcome")
        self.assertEqual(caught.exception.__class__.__name__, "ContextError")


class BaselineTests(Base):
    def test_share_of_runs_against_the_declared_range(self):
        base = self.td / "07_Baseline_Trajectories"
        for i in range(1, 7):
            calls = [c for c in bo._go_calls() if not (c[0].endswith("linear_get_issue") and i > 3)]
            if i == 1:
                calls.append(THREAD_READ)
            self.run_calls(calls, base / f"trajectory-run-{i} (1).json")
        r, u = self.compare(trajectory=base)
        self.assertEqual((r["mode"], len(r["runs"])), ("baseline", 6))
        self.assertEqual([x["label"] for x in r["runs"]], [f"run-{i}" for i in range(1, 7)])
        self.assertEqual((u["U1"]["opened_runs"], u["U1"]["share"], u["U1"]["position"]), (1, 0.1667, "above"))
        self.assertEqual(u["U1"]["opened_in"], ["run-1"])
        self.assertEqual((u["U2"]["opened_runs"], u["U2"]["position"]), (0, "inside"))
        self.assertEqual((u["U3"]["opened_runs"], u["U3"]["position"]), (3, "inside"))
        self.assertEqual(u["U4"]["position"], "below")
        self.assertEqual(u["U6"]["position"], "not judged")
        self.assertEqual(r["verdict"], "WARN")
        self.assertEqual(len(r["bound_to"]), 8)         # budget, SQL and six runs
        code, out, _ = self.run_main("compare", "--task-dir", str(self.td), "--trajectory", str(base))
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("BUDGET OUTCOME (baseline, 6 runs): WARN"))
        code, _, err = self.run_main("compare", "--task-dir", str(self.td), "--trajectory", str(base), "--write")
        self.assertEqual(code, 2)
        self.assertIn("reported only", err)

    def test_usage_errors(self):
        self.assertEqual(self.run_main("compare", "--task-dir", str(self.td))[0], 2)        # no trajectory yet
        self.assertEqual(self.run_main("compare", "--task-dir", str(self.td / "missing"))[0], 2)
        self.assertEqual(self.run_main("compare")[0], 2)
        self.assertEqual(self.run_main()[0], 2)
        self.run_calls(bo._go_calls())
        self.assertEqual(self.run_main("compare", "--task-dir", str(self.td), "--today", "tomorrow")[0], 2)
        (self.td / WF / bo.BUDGET).unlink()
        code, _, err = self.run_main("compare", "--task-dir", str(self.td))
        self.assertEqual(code, 2)
        self.assertIn(bo.BUDGET, err)


class HygieneTests(unittest.TestCase):
    def test_source_hygiene(self):
        source = (HERE / "budget_outcome.py").read_text()
        ast.parse(source, feature_version=(3, 9))
        self.assertTrue(source.split('"""', 2)[2].lstrip().startswith("from __future__ import annotations"))
        self.assertNotIn("Evals/" + "task_inputs", source)
        self.assertNotIn("datetime.now", source)
        self.assertNotIn("time.time", source)

    def test_real_precheck_trajectory_parses(self):
        path = (bo.BUNDLE / "support" / "completed_tasks" / "robert_seed_bets_2026-11-11" / "task_inputs"
                / "06_PreCheck_Trajectory" / "trajectory.json")
        if not path.is_file():
            self.skipTest("the archived pre-check is not in this copy of the bundle")
        run = bo._load_run("precheck", path)
        views = bo.index_run(run)
        self.assertEqual(len(views), len(run.calls))
        self.assertEqual([v.step for v in views], list(range(1, len(views) + 1)))
        # the Leapblock close-out post (rev6): returned by a Slack search, its ts a JSON number
        forms = bo.id_forms({"record_id": "C05URGU759U/1770971846.479179"})
        m = bo.match_unit(views, forms, [], set())
        self.assertTrue(m["opened"])
        self.assertEqual((m["how"], m["tool"]), ("result", "slack_search_public_and_private"))
        # a founders-channel message the hand review found unread
        m = bo.match_unit(views, bo.id_forms({"record_id": "C04UEQVDVB7/1712901800.684259"}), [], {"c04ueqvdvb7"})
        self.assertFalse(m["opened"])
        self.assertTrue(m["spilled_container_reads"])


if __name__ == "__main__":
    unittest.main()
