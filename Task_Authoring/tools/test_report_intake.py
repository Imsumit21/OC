"""Tests for report_intake.py. Run: cd Task_Authoring/tools && python3.12 -B -m unittest test_report_intake

Every test works in its own scratch folder with its own copy of the register. The real
references/platform_rule_delta.json is checked byte for byte (and by mtime) before and after the whole class.
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import shutil
import unittest
from pathlib import Path
from unittest import mock

import release_drift
import report_intake as ri
import selftest_sandbox
import task_metrics

HERE = Path(__file__).resolve().parent
ARCHIVE = HERE.parent / "support" / "completed_tasks"
OWN, OTHER = "6aeed82596dcfe103f9f74d9", "6aed9d01a1cb8067d8ac7dee"


def sha(path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def tree(folder) -> list:
    """Every entry under a folder with its size and mtime: equal before and after means nothing was written."""
    return sorted((str(p.relative_to(folder)), p.stat().st_size, p.stat().st_mtime_ns) for p in Path(folder).rglob("*"))


def real_register_state():
    path = release_drift.REGISTER
    return (path.read_bytes(), path.stat().st_mtime_ns) if path.is_file() else None


class Base(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.real_register = real_register_state()

    @classmethod
    def tearDownClass(cls):
        assert real_register_state() == cls.real_register, "the real references/platform_rule_delta.json changed"

    def setUp(self):
        self._tmp = selftest_sandbox.scratch_tmp("test_report_intake_")
        self.root = Path(self._tmp.name)
        self.fx = ri.make_fixture(self.root)
        self.task, self.kw, self.register = self.fx["task"], self.fx["kw"], self.fx["register"]
        self.inbox = self.root / "inbox"

    def tearDown(self):
        self._tmp.cleanup()

    def report(self, name, title="PROMPT EVALUATION REPORT", verdict="FAIL", task_id=OWN, folder=None, **kw):
        return ri.make_report(folder or self.inbox, name, title, verdict, task_id, **kw)

    def prompt_report(self, name=f"{OWN}_1_prompt.md", verdict="FAIL", folder=None, **kw):
        kw.setdefault("hashes", [(ri.PROMPT, sha(self.task / ri.PROMPT))])
        return self.report(name, verdict=verdict, folder=folder, **kw)

    def intake(self, report, **extra):
        return ri.intake(self.task, report, **dict(self.kw, **extra))

    def status(self, result, check_id):
        return next(c["status"] for c in result["checks"] if c["id"] == check_id)

    def detail(self, result, check_id):
        return next(c["detail"] for c in result["checks"] if c["id"] == check_id)


class Refusals(Base):
    def test_foreign_id_refused_with_nothing_written(self):
        self.assertTrue(self.intake(self.prompt_report())["accepted"])
        before, register = tree(self.task), self.register.read_bytes()
        stray = self.report(f"{OTHER}_2_oe.md", "OE EVALUATION REPORT", "PASS", OTHER)
        result = self.intake(stray)
        self.assertFalse(result["accepted"])
        self.assertEqual(result["verdict"], "FAIL")
        detail = self.detail(result, "bind.task_id")
        for word in (OWN, OTHER, self.task.name, "not filed"):
            self.assertIn(word, detail)
        self.assertEqual(tree(self.task), before)
        self.assertEqual(self.register.read_bytes(), register)
        self.assertNotIn("drift", result)

    def test_foreign_persona_refused_even_as_first_report(self):
        before, register = tree(self.task), self.register.read_bytes()
        foreign = self.report(f"{OTHER}_3_rubric.md", "RUBRIC EVALUATION REPORT", "FAIL", OTHER,
                              persona="Leonard Hayes")
        result = self.intake(foreign, rebind=True)            # --rebind never overrides the persona check
        self.assertFalse(result["accepted"])
        self.assertEqual(self.status(result, "bind.persona"), "FAIL")
        self.assertEqual(tree(self.task), before)
        self.assertFalse((self.task / ri.REPORTS_DIR).exists())
        self.assertIsNone(ri.load_binding(self.task))
        self.assertFalse(task_metrics.metrics_path(self.task).exists())
        self.assertEqual(self.register.read_bytes(), register)

    def test_hashes_of_another_task_folder_refused(self):
        other = self.fx["bundle"] / "task_inputsB"
        (other / "Working_Files").mkdir(parents=True)
        (other / ri.PROMPT).write_text("Another task's prompt.\n")
        wrong = self.prompt_report(hashes=[(ri.PROMPT, sha(other / ri.PROMPT))])
        before = tree(self.task)
        result = self.intake(wrong)
        self.assertFalse(result["accepted"])
        self.assertEqual(result["ran_on"][ri.PROMPT]["ran_on"], "other_task")
        self.assertIn("task_inputsB", self.detail(result, "bind.hashes"))
        self.assertEqual(tree(self.task), before)

    def test_local_review_output_refused(self):
        local = self.prompt_report(extra="local rehearsal, release LOCALFP000000")
        result = self.intake(local)
        self.assertFalse(result["accepted"])
        self.assertEqual(self.status(result, "report.platform"), "FAIL")
        self.assertFalse((self.task / ri.REPORTS_DIR).exists())

    def test_name_id_and_printed_id_disagree(self):
        result = self.intake(self.prompt_report(name=f"{OWN}_1_prompt.md", task_id=OTHER))
        self.assertFalse(result["accepted"])
        self.assertEqual(self.status(result, "report.id"), "FAIL")

    def test_eval_given_against_the_file(self):
        result = self.intake(self.prompt_report(), eval_kind="rubric")
        self.assertFalse(result["accepted"])
        self.assertEqual(self.status(result, "report.eval"), "FAIL")

    def test_unreadable_metrics_log_refuses_before_any_write(self):
        log = task_metrics.metrics_path(self.task)
        log.write_text("not json")
        before = tree(self.task)
        with self.assertRaises(task_metrics.MetricsError):
            self.intake(self.prompt_report())
        self.assertEqual(tree(self.task), before)
        self.assertFalse((self.task / ri.REPORTS_DIR).exists())

    def test_dry_run_writes_nothing(self):
        before = tree(self.task)
        result = self.intake(self.prompt_report(), dry_run=True)
        self.assertTrue(result["accepted"])
        self.assertEqual(self.status(result, "file.copy"), "SKIP")
        self.assertEqual(tree(self.task), before)

    def test_first_bind_without_hash_proof_warns(self):
        bare = self.report(f"{OWN}_1a_hardness.md", "HARDNESS EVALUATION REPORT", "FAIL", persona=None)
        result = self.intake(bare)
        self.assertTrue(result["accepted"])
        self.assertEqual(self.status(result, "bind.task_id"), "WARN")
        self.assertEqual(result["verdict"], "WARN")
        proven = self.intake(self.prompt_report())
        self.assertEqual(self.status(proven, "bind.task_id"), "PASS")


class Filing(Base):
    def test_same_bytes_twice_is_a_no_op(self):
        first = self.prompt_report()
        result = self.intake(first)
        self.assertTrue(result["accepted"])
        self.assertEqual((self.task / ri.REPORTS_DIR / first.name).read_bytes(), first.read_bytes())
        before, register = tree(self.task), self.register.read_bytes()
        renamed = self.inbox / "again" / f"{OWN}_1_prompt (1).md"
        renamed.parent.mkdir(parents=True)
        renamed.write_bytes(first.read_bytes())
        for same in (first, renamed):
            again = self.intake(same)
            self.assertTrue(again["accepted"])
            self.assertEqual(again["filed_as"], f"{ri.REPORTS_DIR}/{first.name}")
            self.assertEqual(again["round"], 1)
            self.assertIn("already counted", self.detail(again, "metrics.platform_round"))
        self.assertEqual(tree(self.task), before)
        self.assertEqual(self.register.read_bytes(), register)
        self.assertEqual(task_metrics.summarise(self.task)["rounds"]["prompt"]["count"], 1)

    def test_different_bytes_same_name_get_dup_suffix(self):
        name = f"{OWN}_1_prompt.md"
        reports = [self.prompt_report(name=name, verdict=v, folder=self.inbox / str(i))
                   for i, v in enumerate(("FAIL", "NON-FAIL", "PASS"))]
        filed = [self.intake(r) for r in reports]
        self.assertEqual([r["filed_as"] for r in filed],
                         [f"{ri.REPORTS_DIR}/{name}", f"{ri.REPORTS_DIR}/{OWN}_1_prompt-dup1.md",
                          f"{ri.REPORTS_DIR}/{OWN}_1_prompt-dup2.md"])
        self.assertEqual([r["round"] for r in filed], [1, 2, 3])
        for report, result in zip(reports, filed):
            self.assertEqual((self.task / result["filed_as"]).read_bytes(), report.read_bytes())
        summary = task_metrics.summarise(self.task)
        self.assertEqual(summary["rounds"]["prompt"], {"count": 3, "verdicts": ["FAIL", "NON-FAIL", "PASS"]})
        self.assertEqual(summary["over_target"], ["rounds.prompt"])

    def test_binding_and_list(self):
        self.intake(self.prompt_report())
        self.intake(self.report(f"{OWN}_3_rubric.md", "RUBRIC EVALUATION REPORT", "PASS"))
        binding = json.loads((self.task / "Working_Files" / ri.BIND_FILE).read_text())
        self.assertEqual(binding["schema"], ri.BIND_SCHEMA)
        self.assertEqual(binding["platform_task_id"], OWN)
        (self.task / ri.REPORTS_DIR / f"{OWN}_0_injection.md").write_text("# /injection\n### FINAL VERDICT: PASS\n")
        listing = ri.list_reports(self.task)
        self.assertEqual([(r["eval"], r["round"]) for r in listing["reports"]], [("prompt", 1), ("rubric", 1)])
        self.assertEqual([u["name"] for u in listing["untracked"]], [f"{OWN}_0_injection.md"])
        self.assertEqual(listing["verdict"], "WARN")

    def test_rebind_records_history(self):
        self.intake(self.prompt_report())
        stray = self.report(f"{OTHER}_2_oe.md", "OE EVALUATION REPORT", "PASS", OTHER)
        result = self.intake(stray, rebind=True)
        self.assertTrue(result["accepted"])
        binding = ri.load_binding(self.task)
        self.assertEqual(binding["platform_task_id"], OTHER)
        self.assertEqual(binding["history"], [{"platform_task_id": OWN, "replaced_by": OTHER, "report": stray.name}])


class Register(Base):
    def test_register_updated_only_through_release_drift_and_only_the_test_copy(self):
        report = self.prompt_report(extra="Applies `ugt-fork-v9` here.\nEval release SHA-256: " + "a" * 64)
        writes = []
        real_write = ri._atomic_write

        def spy(path, data, what):
            writes.append(Path(path).resolve())
            return real_write(path, data, what)

        with mock.patch.object(ri, "_atomic_write", side_effect=spy), \
                mock.patch.object(release_drift, "save_register", wraps=release_drift.save_register) as saved:
            result = self.intake(report)
        self.assertTrue(result["accepted"])
        self.assertEqual(saved.call_count, 1)
        self.assertEqual(Path(saved.call_args[0][0]).resolve(), self.register.resolve())
        self.assertNotIn(self.register.resolve(), writes)                 # report_intake never writes it itself
        self.assertNotIn(release_drift.REGISTER.resolve(), writes)
        reg = json.loads(self.register.read_text())
        self.assertEqual(reg["names"]["ugt-fork-v9"]["status"], "unreviewed")
        self.assertTrue(any(r["fingerprint"] == "a" * 64 for r in reg["releases"]))
        self.assertEqual(self.status(result, "drift.new"), "WARN")
        self.assertIn(ri.REVIEW_LINE, ri.render(result))
        self.assertEqual(result["drift"]["register"], str(self.register))

    def test_known_report_is_not_recorded_twice(self):
        report = self.prompt_report(extra="Eval release SHA-256: " + "b" * 64)
        self.intake(report)
        with mock.patch.object(release_drift, "save_register", wraps=release_drift.save_register) as saved:
            again = self.intake(report)
        self.assertEqual(saved.call_count, 0)
        self.assertTrue(again["drift"]["already_recorded"])

    def test_release_drift_error_is_a_warning_not_a_crash(self):
        self.register.write_text(json.dumps({"schema": "something-else"}))
        result = self.intake(self.prompt_report())
        self.assertTrue(result["accepted"])
        self.assertEqual(self.status(result, "drift.record"), "WARN")


class Snapshots(Base):
    def write_check(self, text):
        (self.task / "Working_Files" / "04_Prompt_Check.md").write_text(text)

    def test_snapshot_numbering(self):
        self.write_check(f"prompt {sha(self.task / ri.PROMPT)[:12]}\n- Predicted /prompt band: PASS\n")
        first = ri.snapshot(self.task, "prompt-check", at="2026-11-11")
        self.assertTrue(first["created"])
        self.assertEqual(first["snapshot"]["n"], 1)
        self.assertFalse(ri.snapshot(self.task, "prompt-check")["created"])       # unchanged: nothing written
        (self.task / ri.PROMPT).write_text("Build the sheet for Leonard, v2.\n")
        self.write_check(f"prompt {sha(self.task / ri.PROMPT)[:12]}\n- Predicted /prompt band: NON-FAIL\n")
        second = ri.snapshot(self.task, "prompt-check", at="2026-11-11")
        self.assertEqual(second["snapshot"]["n"], 2)
        folder = self.task / "Working_Files" / ri.HISTORY_DIR / "prompt-check"
        (folder / "7_stray.md").write_text("left by hand\n")                    # a number already used by a file
        self.write_check(f"prompt {sha(self.task / ri.PROMPT)[:12]}\n- Predicted /prompt band: FAIL\n")
        third = ri.snapshot(self.task, "prompt-check", at="2026-11-11")
        self.assertEqual(third["snapshot"]["n"], 8)
        self.assertEqual((folder / "7_stray.md").read_text(), "left by hand\n")
        names = sorted(p.name for p in folder.iterdir())
        digest = sha(self.task / ri.PROMPT)[:12]
        self.assertIn(f"8_{digest}.md", names)
        self.assertIn(f"8_{digest}.json", names)
        self.assertEqual([s["n"] for s in ri.snapshots(self.task, "prompt-check")], [1, 2, 8])
        self.assertEqual([s["prediction"]["verdict"] for s in ri.snapshots(self.task, "prompt-check")],
                         ["PASS", "NON-FAIL", "FAIL"])
        self.assertEqual(task_metrics.summarise(self.task)["local_checks"]["prompt-check"]["count"], 3)

    def test_snapshot_missing_inputs_fails_and_writes_nothing(self):
        before = tree(self.task)
        result = ri.snapshot(self.task, "oe-check")
        self.assertEqual(result["verdict"], "FAIL")
        self.assertEqual(tree(self.task), before)

    def test_pairing_uses_the_platform_hash_forms(self):
        # The platform hashes the prompt with one final newline and the SQL without its header lines.
        (self.task / ri.PROMPT).write_bytes(b"Build the sheet for Leonard.")
        sql = b"-- header 1\n-- header 2\n-- header 3\nBEGIN;\nINSERT INTO t VALUES (1);\nCOMMIT;\n"
        (self.task / ri.SQL).write_bytes(sql)
        platform_prompt = hashlib.sha256(b"Build the sheet for Leonard.\n").hexdigest()
        platform_sql = hashlib.sha256(b"\n".join(sql.split(b"\n")[3:])).hexdigest()
        self.write_check("- Predicted /prompt band: NON-FAIL\n")
        ri.snapshot(self.task, "prompt-check", at="2026-11-11")
        report = self.prompt_report(verdict="NON-FAIL", hashes=[(ri.PROMPT, platform_prompt[:8] + "…"),
                                                                (ri.SQL, platform_sql[:8] + "…")])
        result = self.intake(report)
        self.assertEqual(result["ran_on"][ri.PROMPT]["form"], "with one final newline")
        self.assertEqual(result["ran_on"][ri.SQL]["form"], "without its first 3 lines")
        self.assertEqual(self.status(result, "bind.hashes"), "PASS")
        self.assertEqual(result["pair"]["local_verdict"], "NON-FAIL")
        self.assertTrue(result["pair"]["agree"])
        pairs = task_metrics.summarise(self.task)["verdict_pairs"]
        self.assertEqual([(p["local"], p["platform"], p["agree"]) for p in pairs], [("NON-FAIL", "NON-FAIL", True)])

    def test_check_on_another_sql_revision_is_not_paired(self):
        self.write_check("- Predicted /prompt band: PASS\n")
        ri.snapshot(self.task, "prompt-check", at="2026-11-11")
        older = self.task / "Working_Files" / ri.FORENSICS_DIR / "rev1" / ri.SQL
        report = self.prompt_report(hashes=[(ri.PROMPT, sha(self.task / ri.PROMPT)), (ri.SQL, sha(older))])
        result = self.intake(report)
        self.assertEqual(result["ran_on"][ri.SQL]["ran_on"], "earlier")
        self.assertEqual(self.status(result, "pair.local"), "SKIP")


class CommandLine(Base):
    def run_main(self, argv):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            code = ri.main(argv)
        return code, out.getvalue()

    def common(self):
        return ["--tasks-root", str(self.fx["bundle"]), "--register", str(self.register), "--repo",
                str(self.fx["repo"]), "--today", "2026-11-11", "--at", "2026-11-11T00:00:00Z"]

    def test_exit_codes_and_header(self):
        good = self.prompt_report()
        code, out = self.run_main(["intake", str(good), "--task-dir", str(self.task)] + self.common())
        self.assertEqual(code, 0)
        self.assertRegex(out.splitlines()[0], r"^REPORT INTAKE \(prompt\): (PASS|WARN)$")
        stray = self.report(f"{OTHER}_2_oe.md", "OE EVALUATION REPORT", "PASS", OTHER)
        code, out = self.run_main(["intake", str(stray), "--task-dir", str(self.task), "--json"] + self.common())
        self.assertEqual(code, 1)
        doc = json.loads(out)
        self.assertEqual((doc["tool"], doc["version"], doc["verdict"]), ("report_intake", 1, "FAIL"))
        for check in doc["checks"]:
            self.assertIn(check["status"], ("PASS", "FAIL", "WARN", "SKIP"))
        code, out = self.run_main(["list", "--task-dir", str(self.task)])
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("REPORT INTAKE (list): PASS"))
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as stop:
            ri.main(["intake", str(good)])
        self.assertEqual(stop.exception.code, 2)


@unittest.skipUnless((ARCHIVE / "robert_seed_bets_2026-11-11" / "eval_reports").is_dir()
                     and (ARCHIVE / "leonard_stockholder_closeout_2026-11-10" / "eval_reports").is_dir(),
                     "the archived backtest tasks are not present")
class ArchivedReports(unittest.TestCase):
    """The Leonard rubric report that was saved into S2's folder is refused there; S2's own report is taken in.
    Only the assignment is copied; the archive is read, never written."""

    def setUp(self):
        self._tmp = selftest_sandbox.scratch_tmp("test_report_intake_archive_")
        self.root = Path(self._tmp.name)
        self.register = self.root / "register.json"
        shutil.copy2(release_drift.REGISTER, self.register)
        self.real_register = real_register_state()

    def tearDown(self):
        self._tmp.cleanup()
        self.assertEqual(real_register_state(), self.real_register)

    def test_seed_bets_refuses_the_leonard_report(self):
        archive = ARCHIVE / "robert_seed_bets_2026-11-11"
        task = self.root / "task_inputsSEED"
        (task / "Working_Files").mkdir(parents=True)
        shutil.copy2(archive / "task_inputs" / "00_Assigments.md", task / "00_Assigments.md")
        before = tree(archive)
        kw = {"tasks_root": self.root, "register": self.register, "today": "2026-11-11",
              "at": "2026-11-11T00:00:00Z"}
        own = ri.intake(task, archive / "eval_reports" / f"{OWN}_0_injection.md", **kw)
        self.assertTrue(own["accepted"], own["checks"])
        foreign = ri.intake(task, archive / "eval_reports" / f"{OTHER}_3_rubric.md", **kw)
        self.assertFalse(foreign["accepted"])
        self.assertEqual({c["id"] for c in foreign["checks"] if c["status"] == "FAIL"},
                         {"bind.task_id", "bind.persona"})
        self.assertEqual(sorted(p.name for p in (task / ri.REPORTS_DIR).iterdir()), [f"{OWN}_0_injection.md"])
        self.assertEqual(tree(archive), before)


if __name__ == "__main__":
    unittest.main()
