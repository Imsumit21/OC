"""Tests for eval_scratch.py. Run: cd Task_Authoring/tools && python3.12 -B -m unittest test_eval_scratch

The tests build a fake workspace (a small evaluator that finds its store the way the real one does) under
support/scratch. The real Evals/ is listed with sizes and mtimes before and after the whole class and must not change.
"""
from __future__ import annotations

import contextlib
import io
import json
import unittest
from pathlib import Path
from unittest import mock

import eval_scratch as es
import report_intake as ri
import selftest_sandbox
from task_context import ContextError

REAL_EVALS = es.WS / es.EVALS
CAN_CLONE = es._clone_function() is not None
ASSIGNMENT = ri.ASSIGNMENT_TEXT.format(persona="Robert")         # a full V3 assignment dated February 14, 2026


class Base(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.real_before = es.listing(REAL_EVALS) if REAL_EVALS.is_dir() else None

    @classmethod
    def tearDownClass(cls):
        if cls.real_before is not None:
            changes = es.listing_diff(cls.real_before, es.listing(REAL_EVALS))
            assert not changes, f"the real Evals/ changed during the eval_scratch tests: {changes[:5]}"

    def setUp(self):
        self._tmp = selftest_sandbox.scratch_tmp("test_eval_scratch_")
        self.root = Path(self._tmp.name)
        self.fx = es.make_fixture(self.root / "a")
        self.ws, self.task, self.kw, self.scratch = self.fx["ws"], self.fx["task"], self.fx["kw"], self.fx["scratch"]
        self.fake_evals_before = es.listing(self.ws / es.EVALS)

    def tearDown(self):
        self._tmp.cleanup()

    def by_id(self, result):
        return {c["id"]: c for c in result["checks"]}

    def assert_fake_evals_untouched(self):
        self.assertEqual(es.listing_diff(self.fake_evals_before, es.listing(self.ws / es.EVALS)), [])


class Create(Base):
    def test_symlink_mode_store_is_separate(self):
        made = es.create(self.task, universe_data="symlink", **self.kw)
        root = Path(made["scratch"])
        checks = self.by_id(made)
        self.assertEqual(made["verdict"], "WARN")                    # record reads fail through a symlink
        self.assertEqual(checks["scratch.universe_reads"]["status"], "WARN")
        for key in ("scratch.store_list", "scratch.store_write", "scratch.store_read", "scratch.real_evals"):
            self.assertEqual(checks[key]["status"], "PASS", checks[key])
        store = root / "ws" / es.EVALS / es.STORE
        self.assertEqual((store / es.DATE_FILE).read_text(), "2026-02-14\n")
        self.assertEqual((self.ws / es.EVALS / es.STORE / es.DATE_FILE).read_text(), "2025-10-01\n")
        self.assert_fake_evals_untouched()
        self.assertTrue(root.parent.samefile(self.scratch) and root.name.startswith(es.PREFIX))
        staged = json.loads((store / "inputs.json").read_text())["inputs"]["universe"]["tmp"]
        self.assertTrue(es._inside(staged, root / "tmp"), "a tempfile without a folder left the scratch")

    def test_copy_leaves_out_the_store_and_caches(self):
        root = Path(es.create(self.task, universe_data="symlink", **self.kw)["scratch"])
        copied = root / "ws" / es.EVALS
        self.assertFalse((copied / ".cache").exists())
        self.assertEqual(sorted(p.name for p in (copied / es.STORE).iterdir()), [es.DATE_FILE, "inputs.json"])
        self.assertFalse(any(p.is_symlink() for p in copied.rglob("*")))
        self.assertTrue((copied / "references" / "universes" / "normal" / "universe_manifest.json").is_file())
        self.assertFalse((root / "ws" / "Universe_SynthCut").exists())
        self.assertTrue((root / "ws" / "claude").is_symlink())
        meta = json.loads((root / "scratch.json").read_text())
        self.assertEqual((meta["schema"], meta["universe"]["key"], meta["universe_data"]),
                         (es.SCHEMA, "normal", "symlink"))

    @unittest.skipUnless(CAN_CLONE, "copy-on-write clones need macOS (APFS)")
    def test_clone_mode_reads_records_and_never_writes_the_original(self):
        made = es.create(self.task, universe_data="clone", **self.kw)
        self.assertEqual((made["verdict"], made["universe_data"]), ("PASS", "clone"))
        self.assertEqual(self.by_id(made)["scratch.universe_reads"]["status"], "PASS")
        data = Path(made["workspace"]) / "Universe_Normal" / "contacts" / "contacts.json"
        self.assertFalse(data.is_symlink() or data.parent.parent.is_symlink())
        data.write_text("changed in the scratch\n")
        self.assertIn("Universe_Normal", (self.ws / "Universe_Normal" / "contacts" / "contacts.json").read_text())
        self.assert_fake_evals_untouched()

    def test_without_clone_support_auto_falls_back_and_clone_refuses(self):
        with mock.patch.object(es, "_clone_function", return_value=None):
            with self.assertRaises(es.CloneUnsupported):
                es.create(self.task, universe_data="clone", **self.kw)
            self.assertFalse(list(self.scratch.glob(es.PREFIX + "*")), "a failed create left a scratch")
            auto = es.create(self.task, universe_data="auto", **self.kw)
        self.assertEqual(auto["universe_data"], "symlink")
        self.assertEqual(self.by_id(auto)["scratch.universe_data"]["status"], "WARN")

    def test_a_write_into_the_real_evals_is_caught(self):
        bad = es.make_fixture(self.root / "b", leak=True)
        leaked = es.create(bad["task"], universe_data="symlink", **bad["kw"])
        detail = self.by_id(leaked)["scratch.real_evals"]["detail"]
        self.assertEqual(leaked["verdict"], "FAIL")
        self.assertIn("LEAK", detail)
        self.assertIn("leaked.txt", detail)
        self.assertNotIn("run evaluator tools with", es.render(leaked))

    def test_a_scratch_inside_the_real_evals_is_refused(self):
        with self.assertRaises(ContextError):
            es.create(self.task, source_ws=self.ws, scratch=REAL_EVALS / "scratch_never_made", date="2026-02-14")
        self.assertFalse((REAL_EVALS / "scratch_never_made").exists())


class Dates(Base):
    def test_the_task_date_is_never_guessed(self):
        with self.assertRaises(es.ScratchError) as caught:
            es.create(self.task, source_ws=self.ws, scratch=self.scratch)
        self.assertIn("task date", str(caught.exception))
        with self.assertRaises(es.ScratchError):
            es.create(self.task, source_ws=self.ws, scratch=self.scratch, date="March 3, 2026")
        self.assertFalse(self.scratch.exists() and list(self.scratch.glob(es.PREFIX + "*")))

    def test_the_assignment_date_selects_the_universe(self):
        text = ASSIGNMENT.replace("February 14, 2026 00:00", "October 1, 2025 00:00")
        self.assertNotEqual(text, ASSIGNMENT)
        (self.task / "00_Assigments.md").write_text(text)
        universe = es.task_universe(self.task, source_ws=self.ws)
        self.assertEqual((universe["key"], universe["folder"]), ("synthcut", "Universe_SynthCut"))
        made = es.create(self.task, universe_data="symlink", source_ws=self.ws, scratch=self.scratch)
        store = Path(made["workspace"]) / es.EVALS / es.STORE / es.DATE_FILE
        self.assertEqual(store.read_text(), "2025-10-01\n")
        self.assertTrue((Path(made["workspace"]) / "Universe_SynthCut").exists())

    def test_two_folders_never_share_a_scratch(self):
        other = self.task.parent / "task_inputsB"
        other.mkdir()
        self.assertNotEqual(es.scratch_root(self.task, self.scratch), es.scratch_root(other, self.scratch))
        same_name = self.root / "elsewhere" / self.task.name
        same_name.mkdir(parents=True)
        self.assertNotEqual(es.scratch_root(self.task, self.scratch), es.scratch_root(same_name, self.scratch))


class Lifecycle(Base):
    def test_status_reads_only_and_equals_evaluate(self):
        made = es.create(self.task, universe_data="symlink", **self.kw)
        root = Path(made["scratch"])
        before = es.listing(root)
        shown = es.status(self.task, source_ws=self.ws, scratch=self.scratch)
        self.assertEqual(es.evaluate(self.task, source_ws=self.ws, scratch=self.scratch)["checks"], shown["checks"])
        self.assertEqual(es.listing(root), before)
        self.assertEqual((shown["exists"], shown["saved_inputs"]), (True, ["universe"]))

    def test_recheck_without_rebuild_and_a_changed_evaluator(self):
        es.create(self.task, universe_data="symlink", **self.kw)
        again = es.create(self.task, universe_data="symlink", **self.kw)
        self.assertIn("not rebuilt", self.by_id(again)["scratch.build"]["detail"])
        (self.ws / es.EVALS / "WORKFLOW.md").write_text("workflow v2\n")
        shown = es.status(self.task, source_ws=self.ws, scratch=self.scratch)
        self.assertEqual(self.by_id(shown)["scratch.current"]["status"], "WARN")
        rebuilt = es.create(self.task, universe_data="symlink", force=True, **self.kw)
        self.assertEqual(self.by_id(rebuilt)["scratch.rebuild"]["status"], "PASS")
        self.assertEqual((Path(rebuilt["workspace"]) / es.EVALS / "WORKFLOW.md").read_text(), "workflow v2\n")

    def test_another_universe_needs_force(self):
        es.create(self.task, universe_data="symlink", **self.kw)
        other = es.create(self.task, universe_data="symlink", source_ws=self.ws, scratch=self.scratch,
                          date="2025-10-01")
        self.assertEqual(other["verdict"], "FAIL")
        self.assertIn("--force", self.by_id(other)["scratch.build"]["detail"])

    def test_remove_deletes_the_scratch_only(self):
        root = Path(es.create(self.task, universe_data="symlink", **self.kw)["scratch"])
        listed = es.list_scratches(self.scratch)
        self.assertEqual([r["scratch"] for r in listed["scratches"]], [root.name])
        gone = es.remove(self.task, scratch=self.scratch)
        self.assertEqual(gone["verdict"], "PASS")
        self.assertFalse(root.exists())
        self.assertTrue((self.ws / "claude" / "CLAUDE.md").is_file())
        self.assertTrue((self.ws / "Universe_Normal" / "contacts" / "contacts.json").is_file())
        self.assertEqual(es.remove(self.task, scratch=self.scratch)["checks"][0]["status"], "SKIP")
        with self.assertRaises(es.ScratchError):
            es._remove_tree(self.ws / es.EVALS, self.scratch)
        self.assert_fake_evals_untouched()


class CommandLine(Base):
    def run_main(self, argv):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            code = es.main(argv)
        return code, out.getvalue()

    def test_commands_and_exit_codes(self):
        hidden = ["--source-ws", str(self.ws), "--scratch-root", str(self.scratch)]
        code, out = self.run_main(["create", "--task-dir", str(self.task)] + hidden)
        self.assertEqual(code, 1)                                    # no assignment and no --date: never guessed
        self.assertTrue(out.startswith("EVAL SCRATCH (create): FAIL"))
        code, out = self.run_main(["create", "--task-dir", str(self.task), "--universe-data", "symlink", "--date",
                                   "2026-02-14", "--json"] + hidden)
        self.assertEqual(code, 0)
        doc = json.loads(out)
        self.assertEqual((doc["tool"], doc["version"], doc["verdict"]), ("eval_scratch", 1, "WARN"))
        code, out = self.run_main(["status", "--task-dir", str(self.task)] + hidden)
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("EVAL SCRATCH (status): PASS"))
        code, out = self.run_main(["list", "--scratch-root", str(self.scratch)])
        self.assertEqual(code, 0)
        code, out = self.run_main(["remove", "--task-dir", str(self.task), "--scratch-root", str(self.scratch)])
        self.assertEqual(code, 0)
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as stop:
            es.main(["create"])
        self.assertEqual(stop.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
