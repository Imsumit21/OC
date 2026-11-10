"""Tests for task_metrics.py. Run: cd Task_Authoring/tools && python3.12 -B -m unittest test_task_metrics"""
from __future__ import annotations

import contextlib
import io
import json
import unittest
from pathlib import Path

import selftest_sandbox
import task_metrics as tm
from task_context import ContextError

HERE = Path(__file__).resolve().parent
ARCHIVE = HERE.parent / "support" / "completed_tasks"
AT = "2026-11-01T10:00:00Z"


def tree(folder) -> list:
    return sorted((str(p.relative_to(folder)), p.stat().st_size, p.stat().st_mtime_ns) for p in Path(folder).rglob("*"))


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = selftest_sandbox.scratch_tmp("test_task_metrics_")
        self.root = Path(self._tmp.name)
        self.task = self.root / "task_inputsT"
        (self.task / "Working_Files").mkdir(parents=True)

    def tearDown(self):
        self._tmp.cleanup()

    def log(self):
        return json.loads(tm.metrics_path(self.task).read_text())

    def run_main(self, argv):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            code = tm.main(argv)
        return code, out.getvalue()


class AppendOnly(Base):
    def test_each_record_keeps_every_earlier_entry_unchanged(self):
        self.assertEqual(tm.metrics_path(self.task), self.task / "Working_Files" / tm.METRICS_FILE)
        kept = []
        for kind, fields in (("sql_revision", {"note": "rev1"}), ("precheck", {}), ("baseline", {}),
                             ("platform_round", {"eval": "prompt", "verdict": "FAIL"}),
                             ("stage_start", {"stage": "rubric"}), ("stage_end", {"stage": "rubric"})):
            entry = tm.record_event(self.task, kind, at=AT, **fields)
            events = self.log()["events"]
            self.assertEqual(events[:-1], kept, "an earlier entry was rewritten")
            self.assertEqual(events[-1], entry)
            kept = events
        self.assertEqual([e["n"] for e in kept], [1, 2, 3, 4, 5, 6])
        self.assertEqual(self.log()["schema"], tm.SCHEMA)

    def test_values_are_normalised(self):
        entry = tm.record_event(self.task, "platform_round", eval="/Prompt", verdict="nonfail", at="2026-11-03")
        self.assertEqual((entry["eval"], entry["verdict"], entry["at"]), ("prompt", "NON-FAIL", "2026-11-03T00:00:00Z"))
        entry = tm.record_event(self.task, "stage_start", stage=" Injection ", at="2026-11-03T05:00:00+05:00")
        self.assertEqual((entry["stage"], entry["at"]), ("injection", "2026-11-03T00:00:00Z"))

    def test_bad_events_refused_and_nothing_written(self):
        tm.record_event(self.task, "precheck", at=AT)
        before = tm.metrics_path(self.task).read_bytes()
        bad = (lambda: tm.record_event(self.task, "release"),
               lambda: tm.record_event(self.task, "platform_round", eval="prompt"),
               lambda: tm.record_event(self.task, "platform_round", verdict="PASS"),
               lambda: tm.record_event(self.task, "platform_round", eval="golden", verdict="PASS"),
               lambda: tm.record_event(self.task, "stage_start"),
               lambda: tm.record_event(self.task, "stage_end"),
               lambda: tm.record_event(self.task, "fit_verdict"),
               lambda: tm.record_event(self.task, "local_check"),
               lambda: tm.record_event(self.task, "precheck", at="yesterday"),
               lambda: tm.record_event(self.task, "precheck", n=7),
               lambda: tm.record_event(self.root / "missing", "precheck"))
        for number, call in enumerate(bad, 1):
            with self.subTest(case=number), self.assertRaises(tm.MetricsError):
                call()
        self.assertEqual(tm.metrics_path(self.task).read_bytes(), before)

    def test_a_tampered_log_is_refused(self):
        for _ in range(3):
            tm.record_event(self.task, "sql_revision", at=AT)
        doc = self.log()
        cases = {"an entry removed": dict(doc, events=[doc["events"][0], doc["events"][2]]),
                 "a bad time": dict(doc, events=doc["events"][:2] + [dict(doc["events"][2], at="today")]),
                 "an unknown eval": dict(doc, events=doc["events"] + [{"n": 4, "event": "platform_round", "at": AT,
                                                                        "eval": "golden", "verdict": "PASS"}]),
                 "another schema": dict(doc, schema="other")}
        for name, broken in cases.items():
            with self.subTest(case=name):
                tm.metrics_path(self.task).write_text(json.dumps(broken))
                before = tm.metrics_path(self.task).read_bytes()
                with self.assertRaises(tm.MetricsError):
                    tm.record_event(self.task, "precheck", at=AT)
                self.assertEqual(tm.metrics_path(self.task).read_bytes(), before)
                code, out = self.run_main(["summary", "--task-dir", str(self.task)])
                self.assertEqual(code, 1)
                self.assertTrue(out.startswith("TASK METRICS (summary): FAIL\n[FAIL] metrics.log: "), out)
                result = tm.evaluate(self.task)                  # in-process callers get an object, not a raise
                self.assertEqual((result["verdict"], result["checks"][0]["id"]), ("FAIL", "metrics.log"))

    def test_writes_into_evals_are_refused(self):
        with self.assertRaises(ContextError):
            tm._atomic_write(tm.WS / "Evals" / "never_written_by_test_task_metrics.json", b"{}", "a test probe")
        self.assertFalse((tm.WS / "Evals" / "never_written_by_test_task_metrics.json").exists())


class Targets(Base):
    def test_targets_are_the_plan_numbers(self):
        self.assertEqual(tm.TARGETS, {"sql_revisions": 2, "prechecks": 1, "baselines": 1, "rounds_per_platform_eval": 2})

    def fill(self, sql=2, pre=1, base=1, rounds=2):
        for _ in range(sql):
            tm.record_event(self.task, "sql_revision", at=AT)
        for _ in range(pre):
            tm.record_event(self.task, "precheck", at=AT)
        for _ in range(base):
            tm.record_event(self.task, "baseline", at=AT)
        for name in tm.EVALS:
            for _ in range(rounds):
                tm.record_event(self.task, "platform_round", eval=name, verdict="PASS", at=AT)

    def test_exactly_at_the_targets_is_within(self):
        self.fill()
        result = tm.evaluate(self.task)
        self.assertEqual(result["header"], "TASK METRICS: WITHIN TARGET")
        self.assertEqual(result["verdict"], "PASS")
        self.assertEqual(result["summary"]["over_target"], [])
        self.assertTrue(all(c["status"] in ("PASS", "SKIP") for c in result["checks"]), result["checks"])
        self.assertIn(f"Working_Files/{tm.METRICS_FILE}", result["bound_to"])

    def test_one_over_each_target_is_over(self):
        self.fill(sql=3, pre=2, base=2, rounds=3)
        result = tm.evaluate(self.task)
        self.assertEqual(result["header"], "TASK METRICS: OVER TARGET")
        self.assertEqual(result["verdict"], "WARN")
        self.assertEqual(result["summary"]["over_target"],
                         ["sql_revisions", "prechecks", "baselines"] + ["rounds." + n for n in tm.EVALS])
        statuses = {c["id"]: c["status"] for c in result["checks"]}
        for key in ("metrics.sql_revisions", "metrics.prechecks", "metrics.baselines", "metrics.rounds.rubric"):
            self.assertEqual(statuses[key], "WARN")
        code, out = self.run_main(["summary", "--task-dir", str(self.task), "--json"])
        self.assertEqual(code, 0)                       # over target is a measurement, not a tool failure
        doc = json.loads(out)
        self.assertEqual((doc["tool"], doc["version"], doc["verdict"]), ("task_metrics", 1, "WARN"))

    def test_empty_task_is_within_and_reading_writes_nothing(self):
        before = tree(self.task)
        self.assertTrue(tm.summarise(self.task)["within_target"])
        self.assertEqual(tm.evaluate(self.task)["header"], "TASK METRICS: WITHIN TARGET")
        self.assertEqual(tree(self.task), before)

    def test_stage_time_pairs_and_fit(self):
        tm.record_event(self.task, "stage_start", stage="injection", at="2026-11-01T10:00:00Z")
        tm.record_event(self.task, "stage_end", stage="injection", at="2026-11-01T13:30:00Z")
        tm.record_event(self.task, "stage_end", stage="oe", at=AT)
        tm.record_event(self.task, "stage_start", stage="rubric", at=AT)
        tm.record_event(self.task, "platform_round", eval="prompt", verdict="PASS", local_verdict="PASS", at=AT)
        tm.record_event(self.task, "platform_round", eval="rubric", verdict="FAIL", local_verdict="CLEAN", at=AT)
        tm.record_event(self.task, "fit_verdict", verdict="WARN", at=AT)
        tm.record_event(self.task, "fit_verdict", verdict="fit", at=AT)
        s = tm.summarise(self.task)
        self.assertEqual(s["stage_seconds"], {"injection": 12600})
        self.assertEqual(s["open_stages"], {"rubric": AT})
        self.assertTrue(any("without a start" in n for n in s["stage_notes"]))
        self.assertEqual([p["agree"] for p in s["verdict_pairs"]], [True, False])
        self.assertEqual((s["fit_verdict"]["verdict"], s["fit_verdict"]["recorded"]), ("FIT", 2))
        text = tm.render(tm.evaluate(self.task))
        self.assertIn("injection 3h 30m", text)
        self.assertIn("2 local-versus-platform pairs, 1 agree", text)


class CommandLine(Base):
    def test_record_and_summary(self):
        code, out = self.run_main(["record", "--task-dir", str(self.task), "--event", "platform_round", "--eval",
                                   "oe", "--verdict", "pass", "--at", AT, "--json"])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out)["verdict"], "PASS")
        code, out = self.run_main(["record", "--task-dir", str(self.task), "--event", "stage_end"])
        self.assertEqual(code, 1)
        self.assertTrue(out.startswith("TASK METRICS (record): FAIL"))
        code, out = self.run_main(["summary", "--task-dir", str(self.task)])
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("TASK METRICS: WITHIN TARGET"))
        for line in out.splitlines()[1:]:
            self.assertRegex(line, r"^\[(PASS|FAIL|WARN|SKIP)\] metrics\.")
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as stop:
            tm.main(["record", "--event", "precheck"])
        self.assertEqual(stop.exception.code, 2)


class Backfill(Base):
    def archive(self, name="arch_2026-11-01"):
        arch = self.root / "archives" / name
        ti = arch / "task_inputs"
        for rev, sql in (("rev1", "a"), ("rev2", "b"), ("rev3", "c")):
            (ti / "Working_Files" / "run_forensics" / rev).mkdir(parents=True)
            (ti / "Working_Files" / "run_forensics" / rev / tm.SQL_NAME).write_text(sql)
        (ti / "Working_Files" / "run_forensics" / "rev2" / "precheck.node_verdicts.json").write_text("{}")
        (ti / "Working_Files" / "run_forensics" / "rev3" / "baseline").mkdir()
        (ti / tm.SQL_NAME).write_text("c")
        (ti / "06_PreCheck_Trajectory").mkdir()
        (ti / "06_PreCheck_Trajectory" / "trajectory.json").write_text("{}")
        (ti / "07_Baseline_Trajectories").mkdir()
        (ti / "07_Baseline_Trajectories" / "trajectory-run-1.json").write_text("{}")
        reports = arch / "eval_reports"
        reports.mkdir()
        own, other = "a" * 24, "b" * 24
        for name_, verdict in ((f"{own}_1_prompt.md", "FAIL"), (f"{own}_1_prompt-2.md", "PASS"),
                               (f"{own}_3_rubric.md", "PASS"), (f"{other}_3_rubric.md", "FAIL")):
            (reports / name_).write_text(f"## REPORT {name_}\n\n### FINAL VERDICT: {verdict}\n")
        (reports / f"{own}_1_prompt (copy).md").write_bytes((reports / f"{own}_1_prompt.md").read_bytes())
        return arch

    def test_backfill_counts_and_writes_nothing(self):
        arch = self.archive()
        before = tree(arch)
        result = tm.backfill(arch)
        s = result["summary"]
        self.assertEqual((s["sql_revisions"], s["prechecks"], s["baselines"]), (3, 1, 1))
        self.assertEqual(s["rounds"]["prompt"], {"count": 2, "verdicts": ["FAIL", "PASS"]})
        self.assertEqual(s["rounds"]["rubric"], {"count": 1, "verdicts": ["PASS"]})
        self.assertEqual(s["over_target"], ["sql_revisions"])
        self.assertIn("carry platform id " + "b" * 24, s["basis"]["rounds"])
        self.assertIn("identical to a report already counted", s["basis"]["rounds"])
        self.assertEqual(tree(arch), before)

    def test_backfill_all_does_not_count_an_empty_archive_as_within(self):
        self.archive()
        bare = self.root / "archives" / "bare_2026-10-01" / "task_inputs"
        bare.mkdir(parents=True)
        (bare / tm.SQL_NAME).write_text("x")
        table = tm.backfill_all(self.root / "archives")
        self.assertEqual([t["archive"] for t in table["tasks"]], ["arch_2026-11-01", "bare_2026-10-01"])
        self.assertEqual([c["status"] for c in table["checks"]], ["WARN", "SKIP"])
        self.assertEqual(table["header"],
                         "TASK METRICS (backfill-all): 0 of 2 archived tasks within target; 1 store too little to tell")
        text = tm.render_table(table)
        self.assertIn("unknown (not stored)", text)
        self.assertIn("tasks over each target: sql_revisions 1", text)

    @unittest.skipUnless((ARCHIVE / "robert_seed_bets_2026-11-11").is_dir(), "the archived tasks are not present")
    def test_real_archive_reads_only(self):
        arch = ARCHIVE / "robert_seed_bets_2026-11-11"
        before = tree(arch)
        s = tm.backfill(arch)["summary"]
        self.assertEqual(s["sql_revisions"], 7)                      # README: SQL rev7
        self.assertEqual(s["rounds"]["rubric"]["count"], 5)          # the Leonard report in the folder is left out
        self.assertIn("6aed9d01a1cb8067d8ac7dee", s["basis"]["rounds"])
        self.assertEqual(tree(arch), before)


if __name__ == "__main__":
    unittest.main()
