"""Tests for carrier_backfill.py.

Run: cd Task_Authoring/tools && python3.12 -B -m unittest test_carrier_backfill
"""
from __future__ import annotations

import base64
import contextlib
import io
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import carrier_backfill as cb  # noqa: E402
import selftest_sandbox  # noqa: E402


def _quiet(fn, *args):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = fn(*args)
    return code, out.getvalue(), err.getvalue()


class TextHelpers(unittest.TestCase):
    def test_norm_text_resolves_literal_escapes_and_quotes(self):
        sql_form = 'He said \\"go\\",\\r\\n then’s it'       # as a SQL string or a JSON dump prints it
        shown = "He said \"go\",\r\n then's it"                   # as a tool result shows it
        self.assertEqual(cb.norm_text(sql_form), cb.norm_text(shown))
        self.assertEqual(cb.norm_text("it\\u2019s  A&amp;B"), "its a&b")

    def test_ts_forms_cover_the_float_form(self):
        self.assertEqual(cb.ts_forms("1700000500.250000"), ["1700000500.250000", "1700000500.25"])
        self.assertEqual(cb.ts_forms("1771027942.000000"), ["1771027942.000000", "1771027942.0"])
        self.assertEqual(cb.ts_forms("1770971846.479179"), ["1770971846.479179"])
        self.assertEqual(cb.ts_forms("ENG-2462"), ["ENG-2462"])

    def test_text_windows_start_after_the_snippet_zone(self):
        text = " ".join("word%03d" % i for i in range(60))
        deep, head = cb.text_windows(text, "")
        self.assertEqual(head, text[:cb.WINDOW])
        self.assertTrue(deep)
        self.assertTrue(all(text.index(w) >= cb.HEAD_CHARS for w in deep))
        self.assertLessEqual(len(deep), cb.MAX_WINDOWS)

    def test_text_windows_short_and_tiny_text(self):
        short = "a short record of about fifty characters in all."
        self.assertEqual(cb.text_windows(short, ""), ([short], None))          # the whole text is the needle
        self.assertEqual(cb.text_windows("too short", ""), ([], None))
        mid = "x" * 30 + " the tail of a record a little over one hundred characters long, which a snippet cuts off"
        deep, head = cb.text_windows(mid, "")
        self.assertEqual(deep, [mid[-cb.WINDOW:]])
        self.assertEqual(head, mid[:cb.WINDOW])

    def test_text_windows_skip_text_another_row_also_holds(self):
        text = " ".join("word%03d" % i for i in range(60))
        deep, _ = cb.text_windows(text, text[100:300])
        self.assertTrue(deep)
        self.assertTrue(all(w not in text[100:300] for w in deep))

    def test_scalars_decode_base64_bodies_and_keep_numbers(self):
        body = "The second wire did not settle, the bank returned it on the 4th."
        data = {"payload": {"body": {"data": base64.urlsafe_b64encode(body.encode()).decode().rstrip("=")}},
                "ts": 1700000500.25, "ok": True, "n": None, "id": "a" * 32}
        got = cb.scalars(data, [])
        self.assertIn(body, got)
        self.assertIn("1700000500.25", got)
        self.assertNotIn("True", got)
        self.assertEqual(len([g for g in got if g == "a" * 32]), 1)     # a hex id is not mistaken for base64 text

    def test_scalars_decode_a_body_inside_a_file_read_back(self):
        body = "The second wire did not settle, the bank returned it on the 4th because the account number was wrong."
        b64 = base64.urlsafe_b64encode(body.encode()).decode().rstrip("=")
        dump = '     1\t{"result": "{\\"messages\\": [{\\"payload\\": {\\"body\\": {\\"data\\": \\"' + b64 + '\\"}}}]}"}' \
               + " padding" * 30
        self.assertIn(body, cb.scalars(dump, []))
        self.assertEqual(cb.scalars("/home/agent/.claude/projects/-app/" + "x/" * 120, []).__len__(), 1)


class ObjectRoute(unittest.TestCase):
    def test_gmail_message_needs_a_body(self):
        mid = "me@x.co/<m2@mail.x.co>"
        minimal = {"id": mid, "threadId": "me@x.co/18", "snippet": "Hi both"}
        metadata = {"id": mid, "payload": {"headers": [{"name": "Subject", "value": "x"}]}}
        full = {"id": mid, "payload": {"parts": [{"body": {"data": "aGVsbG8gd29ybGQ"}}]}}
        self.assertFalse(cb.object_shown({"messages": [minimal]}, [mid]))
        self.assertFalse(cb.object_shown(metadata, [mid]))
        self.assertTrue(cb.object_shown({"messages": [full]}, [mid]))

    def test_gmail_thread_id_matches_a_thread_with_bodies(self):
        tid = "me@x.co/18000000000000001"
        thread = {"id": tid, "snippet": "Hi", "messages": [{"id": "me@x.co/<a@b>", "threadId": tid,
                                                             "payload": {"body": {"data": "aGVsbG8"}}}]}
        self.assertTrue(cb.object_shown(thread, [tid]))
        self.assertFalse(cb.object_shown({"threads": [{"id": tid, "snippet": "Hi", "messageCount": 2}]}, [tid]))

    def test_slack_ts_as_float_and_latest_reply_is_not_the_message(self):
        rid = "C0AAAAAAA1/1700000500.250000"
        self.assertTrue(cb.object_shown({"messages": [{"ts": 1700000500.25, "text": "the reply"}]}, [rid]))
        self.assertFalse(cb.object_shown({"messages": [{"ts": 1700000000.0001, "text": "the root",
                                                        "latest_reply": "1700000500.250000"}]}, [rid]))


class UnitsFile(unittest.TestCase):
    POLICY = {"budget": {"carriers_that_miss": ["dm_with_non_owner"], "carriers_without_loss": ["decoy"]}}

    def _doc(self):
        unit = {"task": "t", "revision": "rev1", "run_set": "baseline", "unit": "CORR", "mechanism_family": "A11",
                "decider": {"service": "slack", "record_id": "C0AAAAAAA1/1700000500.250000", "container": "",
                            "injected": True},
                "carrier": "dm_with_non_owner", "habit": {"service": "slack", "action": "dm_history"},
                "rows": ["R1"], "evidence": ["sql:1"], "confidence": "high", "note": ""}
        return {"schema": cb.SCHEMA_UNITS, "units": [unit], "skipped": [],
                "run_sets": [{"task": "t", "revision": "rev1", "run_set": "baseline", "sql": "01_Universe_Inject.sql",
                              "trajectories": ["07_Baseline_Trajectories/trajectory-run-1.json"]}]}

    def _status(self, doc):
        checks = cb.validate_units(doc, self.POLICY)
        return checks[0]["status"], checks[0]["detail"]

    def test_good_file_passes(self):
        self.assertEqual(self._status(self._doc())[0], "PASS")

    def test_other_carrier_needs_text(self):
        doc = self._doc()
        doc["units"][0]["carrier"] = "other:root_post_unswept_channel"
        self.assertEqual(self._status(doc)[0], "PASS")
        doc["units"][0]["carrier"] = "other:"
        self.assertEqual(self._status(doc)[0], "FAIL")

    def test_planted_bad_fields_fail(self):
        for mutate, word in (
                (lambda d: d["units"][0].update(carrier="hidden"), "not in first_pass_policy"),
                (lambda d: d["units"][0].update(run_set="rehearsal"), "not precheck or baseline"),
                (lambda d: d["units"][0].update(confidence="sure"), "confidence"),
                (lambda d: d["units"][0].update(evidence=[]), "evidence is empty"),
                (lambda d: d["units"][0].pop("habit"), "missing"),
                (lambda d: d["units"][0]["decider"].pop("injected"), "decider needs"),
                (lambda d: d["units"][0].update(rows="R1"), "rows must be a list"),
                (lambda d: d["units"].append(dict(d["units"][0])), "listed twice"),
                (lambda d: d["run_sets"].clear(), "no run_sets entry"),
                (lambda d: d["skipped"].append({"task": "t"}), "needs task and reason"),
                (lambda d: d.update(schema="v0"), "schema is")):
            doc = self._doc()
            mutate(doc)
            status, detail = self._status(doc)
            self.assertEqual(status, "FAIL", detail)
            self.assertIn(word, detail)


class SyntheticArchive(unittest.TestCase):
    """End to end on the self-test fixture: detection, binding, rows, aggregates, CLI."""

    @classmethod
    def setUpClass(cls):
        cls._tmp = selftest_sandbox.scratch_tmp("carrier_backfill_test_")
        cls.fx = cb._fixture(Path(cls._tmp.name))
        cls.res = cb.evaluate(cls.fx["units_path"], cls.fx["root"], policy_path=cls.fx["policy"])
        cls.units = {(u["unit"], u["run_set"]): u for u in cls.res["rates"]["units"]}

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def _runs(self, unit, run_set="baseline"):
        return {r["run"]: r for r in self.units[(unit, run_set)]["runs"]}

    def test_contract_object(self):
        self.assertEqual(self.res["tool"], "carrier_backfill")
        self.assertEqual(self.res["verdict"], "WARN")
        self.assertTrue(all(len(v) == 64 for v in self.res["bound_to"].values()))
        self.assertTrue(all(set(c) == {"id", "status", "detail"} for c in self.res["checks"]))
        self.assertEqual(self.res["rates"]["schema"], cb.SCHEMA_RATES)

    def test_opened_by_thread_fetch_with_step_and_container(self):
        r = self._runs("CORR")["run-1"]
        self.assertEqual((r["opened"], r["how"], r["step"], r["tool"], r["container_step"]),
                         (True, "text", 2, "slack_read_thread", 2))

    def test_reply_ts_on_the_parent_is_only_a_snippet(self):
        r = self._runs("CORR")["run-2"]
        self.assertFalse(r["opened"])
        self.assertTrue(r["snippet_only"])

    def test_spilled_container_read_is_not_opened(self):
        r = self._runs("CORR")["run-3"]
        self.assertFalse(r["opened"])
        self.assertTrue(r["container_spilled"])

    def test_subagent_shell_print_counts(self):
        r = self._runs("CORR")["run-4"]
        self.assertEqual((r["opened"], r["context"], r["tool"]), (True, "subagent", "Bash"))

    def test_mail_body_search_hit_spill_and_write_echo(self):
        runs = self._runs("RET")
        self.assertEqual((runs["run-1"]["opened"], runs["run-1"]["tool"]), (True, "gmail_get_thread"))
        self.assertEqual((runs["run-2"]["opened"], runs["run-2"]["snippet_only"]), (False, True))
        self.assertEqual((runs["run-3"]["opened"], runs["run-3"]["how"]), (True, "direct_get_spilled"))
        self.assertFalse(runs["run-4"]["opened"])       # the text is only in the run's own send call

    def test_rows_and_cross_counts(self):
        c = self.res["rates"]["carriers"]["reply_under_unrelated_parent"]
        self.assertEqual((c["runs"], c["opened"], c["rows_graded_runs"], c["rows_right"]), (4, 2, 4, 2))
        self.assertEqual(c["cross"], {"opened_rows_right": 2, "opened_rows_wrong": 0, "missed_rows_right": 0,
                                      "missed_rows_wrong": 2})
        self.assertEqual(c["plan_list"], "carriers_that_miss")
        self.assertEqual(c["by_run_set"], {"baseline": {"runs": 4, "opened": 2}})

    def test_unbound_precheck_is_left_out_and_warned(self):
        pre = self.units[("CORR", "precheck")]
        self.assertEqual(pre["runs"][0]["binding"], "INSUFFICIENT")
        self.assertFalse(pre["runs"][0]["counted"])
        self.assertFalse(pre["in_aggregate"])
        status = {c["id"]: c["status"] for c in self.res["checks"]}
        self.assertEqual(status["runs.binding"], "WARN")

    def test_habits_and_coverage(self):
        rates = self.res["rates"]
        self.assertEqual(rates["habits"]["slack/thread_replies"]["runs"], 4)
        self.assertEqual(rates["coverage"]["archives_covered"], 1)
        self.assertEqual(rates["coverage"]["skipped"], 1)
        self.assertEqual(rates["coverage"]["unit_runs_counted"], 12)

    def test_low_confidence_units_stay_out_of_the_aggregates(self):
        doc = json.loads(json.dumps(self.fx["doc"]))
        doc["units"][0]["confidence"] = "low"
        path = Path(self._tmp.name) / "units_low.json"
        path.write_text(json.dumps(doc), encoding="utf-8")
        res = cb.evaluate(path, self.fx["root"], policy_path=self.fx["policy"])
        self.assertNotIn("reply_under_unrelated_parent", res["rates"]["carriers"])
        low = [u for u in res["rates"]["units"] if u["confidence"] == "low"]
        self.assertEqual(len(low), 1)
        self.assertEqual(low[0]["totals"]["opened"], 2)          # still measured and listed
        self.assertEqual(res["rates"]["coverage"]["units_low_confidence"], 1)

    def test_two_carriers_of_one_unit_share_the_rows(self):
        doc = json.loads(json.dumps(self.fx["doc"]))
        second = self.fx["unit"]("CORR", "me@x.co/<m2@mail.x.co>", "gmail", "email_reply_via_get_thread",
                                 "get_thread", ["R1", "R2"])
        doc["units"].append(second)
        path = Path(self._tmp.name) / "units_two.json"
        path.write_text(json.dumps(doc), encoding="utf-8")
        res = cb.evaluate(path, self.fx["root"], policy_path=self.fx["policy"])
        mail = [u for u in res["rates"]["units"] if u["unit"] == "CORR" and u["decider"]["service"] == "gmail"][0]
        run3 = [r for r in mail["runs"] if r["run"] == "run-3"][0]
        self.assertTrue(run3["opened"])
        slack = [u for u in res["rates"]["units"] if u["unit"] == "CORR" and u["run_set"] == "baseline"
                 and u["decider"]["service"] == "slack"][0]
        run3s = [r for r in slack["runs"] if r["run"] == "run-3"][0]
        self.assertFalse(run3s["opened"])
        self.assertTrue(run3s["unit_opened"])                    # the other carrier settled it in that run

    def test_blind_rows_raise_the_cross_warning(self):
        doc = json.loads(json.dumps(self.fx["doc"]))
        doc["units"][2]["rows"] = ["R1"]            # FILT is never opened, R1 passes in runs 1 and 4
        path = Path(self._tmp.name) / "units_cross.json"
        path.write_text(json.dumps(doc), encoding="utf-8")
        res = cb.evaluate(path, self.fx["root"], policy_path=self.fx["policy"])
        cross = [c for c in res["checks"] if c["id"] == "units.cross"][0]
        self.assertEqual(cross["status"], "WARN")
        self.assertIn("FILT", cross["detail"])

    def test_deterministic(self):
        again = cb.evaluate(self.fx["units_path"], self.fx["root"], policy_path=self.fx["policy"])
        self.assertEqual(json.dumps(self.res, sort_keys=True), json.dumps(again, sort_keys=True))

    def test_cli_compute_write_show(self):
        out = Path(self._tmp.name) / "rates_cli.json"
        code, text, _ = _quiet(cb.main, ["compute", "--units", str(self.fx["units_path"]), "--tasks-root",
                                         str(self.fx["root"]), "--out", str(out), "--detail"])
        self.assertEqual(code, 0)
        self.assertTrue(text.startswith("CARRIER BACKFILL (1 of 1 archives): WARN"), text[:80])
        self.assertIn("[PASS] units.deciders:", text)
        self.assertIn("demo_task rev2 baseline CORR", text)
        self.assertTrue(out.is_file())
        first = out.read_bytes()
        _quiet(cb.main, ["compute", "--units", str(self.fx["units_path"]), "--tasks-root", str(self.fx["root"]),
                         "--out", str(out)])
        self.assertEqual(first, out.read_bytes())                # same bytes on a second write
        code, text, _ = _quiet(cb.main, ["show", "--rates", str(out)])
        self.assertEqual(code, 0)
        self.assertIn("reply_under_unrelated_parent", text)
        self.assertIn("2/4 (0.50)", text)                        # a rate is printed with its counts
        code, text, _ = _quiet(cb.main, ["show", "--rates", str(out), "--carrier", "email_reply_via_get_thread"])
        self.assertEqual(code, 0)
        self.assertIn("demo_task rev2 baseline RET: opened 2/4", text)
        code, _, err = _quiet(cb.main, ["show", "--rates", str(out), "--carrier", "nope"])
        self.assertEqual(code, 2)
        self.assertIn("no data for carrier", err)
        code, text, _ = _quiet(cb.main, ["compute", "--units", str(self.fx["units_path"]), "--tasks-root",
                                         str(self.fx["root"]), "--json"])
        self.assertEqual(code, 0)
        self.assertEqual(set(json.loads(text)) >= {"tool", "version", "verdict", "bound_to", "checks", "rates"}, True)

    def test_cli_usage_errors(self):
        self.assertEqual(_quiet(cb.main, [])[0], 2)
        self.assertEqual(_quiet(cb.main, ["show", "--rates", str(Path(self._tmp.name) / "missing.json")])[0], 2)
        self.assertEqual(_quiet(cb.main, ["compute", "--task", "demo_task", "--write"])[0], 2)
        self.assertEqual(_quiet(cb.main, ["compute", "--units", str(Path(self._tmp.name) / "missing.json")])[0], 2)

    def test_failing_units_file_exits_1_and_writes_nothing(self):
        doc = json.loads(json.dumps(self.fx["doc"]))
        doc["units"][0]["decider"]["record_id"] = "C0AAAAAAA1/1700000777.000000"
        path = Path(self._tmp.name) / "units_bad.json"
        path.write_text(json.dumps(doc), encoding="utf-8")
        out = Path(self._tmp.name) / "rates_bad.json"
        code, text, _ = _quiet(cb.main, ["compute", "--units", str(path), "--tasks-root", str(self.fx["root"]),
                                         "--out", str(out)])
        self.assertEqual(code, 1)
        self.assertIn("[FAIL] units.deciders:", text)
        self.assertFalse(out.exists())


class SelfTest(unittest.TestCase):
    def test_self_test_passes(self):
        code, text, _ = _quiet(cb.main, ["--self-test"])
        self.assertEqual(code, 0)
        self.assertTrue(text.startswith("self-test: ok"))


class StoredFiles(unittest.TestCase):
    """The curated units file and the computed table as they are on disk (no trajectory is read here)."""

    def test_units_file_is_valid(self):
        if not cb.UNITS_PATH.is_file():
            self.skipTest("references/carrier_backfill_units.json is not written yet")
        doc = cb.load_units()
        checks = cb.validate_units(doc, cb.load_policy())
        self.assertEqual([c for c in checks if c["status"] == "FAIL"], [])
        for u in doc["units"]:
            self.assertTrue(all(isinstance(e, str) and e.strip() for e in u["evidence"]), u["unit"])
        # Archived task folders are not all committed (a fresh clone may lack the newest ones): name them, don't fail.
        missing = sorted({u["task"] for u in doc["units"] if not (cb.TASKS_ROOT / u["task"] / "task_inputs").is_dir()})
        if missing:
            self.skipTest("archived task folders not in this copy: " + ", ".join(missing))

    def test_rates_file_matches_the_units_file(self):
        if not (cb.UNITS_PATH.is_file() and cb.RATES_PATH.is_file()):
            self.skipTest("the stored table is not written yet")
        rates = cb.load_rates()
        self.assertEqual(rates["schema"], cb.SCHEMA_RATES)
        self.assertEqual(rates["source"]["units_sha256"], cb.sha256_file(cb.UNITS_PATH),
                         "carrier_find_rates.json is stale: run `carrier_backfill.py compute --write`")
        doc = cb.load_units()
        self.assertEqual(len(rates["units"]), len(doc["units"]))
        for name, c in rates["carriers"].items():
            self.assertLessEqual(c["opened"], c["runs"], name)
            self.assertEqual(c["runs"], sum(u["runs"] for u in c["unit_rates"]), name)
            self.assertEqual(c["opened"], sum(u["opened"] for u in c["unit_rates"]), name)
            self.assertEqual(sum(c["cross"].values()), c["rows_graded_runs"], name)
        self.assertIsNotNone(cb.carrier_rate(sorted(rates["carriers"])[0], rates))


if __name__ == "__main__":
    unittest.main()
