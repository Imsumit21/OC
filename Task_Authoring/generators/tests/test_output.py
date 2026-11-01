#!/usr/bin/env python3
"""Tests for generators/core/output.py: idempotent, confined publication.

Run from /Users/sumitkumar/Source/Outlier/OC:
    python3 -B Task_Authoring/generators/tests/run_tests.py -k output -v
"""
import os
import shutil
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve()
TA = HERE.parents[2]                                     # Task_Authoring/
if str(TA) not in sys.path:
    sys.path.insert(0, str(TA))

from generators.core import output                    # noqa: E402
from generators.core.output import Build, Change, PublishError, TaskLock, confine   # noqa: E402

SCRATCH = TA / "support" / "scratch"


def build(task, build_id, files):
    b = Build(task, build_id)
    for rel, data in files.items():
        b.add(rel, data)
    return b


def previous(changes):
    """The build record a caller would keep: {rel_path: sha256} of what it published."""
    return {c.path: c.sha256_new for c in changes if c.sha256_new}


def statuses(changes):
    return {c.path: c.status for c in changes}


class OutputTest(unittest.TestCase):
    def setUp(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        self._dirs = []
        self.task = self.new_task()

    def tearDown(self):
        for d in self._dirs:
            shutil.rmtree(d, ignore_errors=True)

    def new_task(self):
        d = Path(tempfile.mkdtemp(prefix="output_test_", dir=str(SCRATCH)))
        self._dirs.append(d)
        return d

    def mtimes(self, rels):
        return {r: (self.task / r).stat().st_mtime_ns for r in rels}

    def temp_leftovers(self):
        return [p for p in self.task.rglob(".tmp-*")]

    # 1 ----------------------------------------------------------------------------------------------------------
    def test_identical_rebuild_keeps_every_mtime(self):
        files = {"a.sql": b"one\n", "sub/b.json": b'{"b": 2}\n'}
        first = build(self.task, "b1", files).publish()
        self.assertEqual(statuses(first), {"a.sql": "new", "sub/b.json": "new"})
        self.assertEqual((self.task / "a.sql").read_bytes(), b"one\n")
        before = self.mtimes(files)
        time.sleep(0.01)

        b2 = build(self.task, "b2", files)
        planned = b2.plan()
        self.assertEqual(statuses(planned), {"a.sql": "unchanged", "sub/b.json": "unchanged"})
        second = b2.publish()
        self.assertEqual(statuses(second), {"a.sql": "unchanged", "sub/b.json": "unchanged"})
        self.assertEqual({c.sha256_old for c in second}, {c.sha256_new for c in second})
        self.assertEqual(self.mtimes(files), before)
        self.assertEqual(self.temp_leftovers(), [])

    # 2 ----------------------------------------------------------------------------------------------------------
    def test_only_the_changed_file_is_replaced(self):
        files = {"a.txt": b"A", "b.txt": b"B", "c.txt": b"C"}
        build(self.task, "b1", files).publish()
        before = self.mtimes(files)
        time.sleep(0.01)

        b2 = build(self.task, "b2", {"a.txt": b"A", "b.txt": b"B2", "c.txt": b"C"})
        result = b2.publish()
        self.assertEqual(statuses(result), {"a.txt": "unchanged", "b.txt": "changed", "c.txt": "unchanged"})
        after = self.mtimes(files)
        self.assertEqual(after["a.txt"], before["a.txt"])
        self.assertEqual(after["c.txt"], before["c.txt"])
        self.assertNotEqual(after["b.txt"], before["b.txt"])
        self.assertEqual((self.task / "b.txt").read_bytes(), b"B2")

    # 3 ----------------------------------------------------------------------------------------------------------
    def test_compare_and_swap_refuses_an_edit_since_plan(self):
        build(self.task, "b1", {"a.txt": b"A", "b.txt": b"B"}).publish()
        b2 = build(self.task, "b2", {"a.txt": b"A2", "b.txt": b"B2"})
        planned = b2.plan()
        self.assertEqual(statuses(planned), {"a.txt": "changed", "b.txt": "changed"})

        (self.task / "b.txt").write_bytes(b"hand edit")
        with self.assertRaises(PublishError) as caught:
            b2.publish()
        message = str(caught.exception)
        self.assertIn("b.txt", message)
        self.assertIn("a.txt", message)                  # the partial publication is reported
        self.assertEqual((self.task / "a.txt").read_bytes(), b"A2")
        self.assertEqual((self.task / "b.txt").read_bytes(), b"hand edit")

    # 4 ----------------------------------------------------------------------------------------------------------
    def test_interruption_reports_the_unpublished_file_as_changed(self):
        build(self.task, "b1", {"a.txt": b"A", "b.txt": b"B"}).publish()
        b2 = build(self.task, "b2", {"a.txt": b"A2", "b.txt": b"B2"})

        real_replace = os.replace
        calls = []

        def replace(src, dst, *a, **kw):
            calls.append(str(dst))
            if len(calls) == 2:
                raise OSError("simulated interruption")
            return real_replace(src, dst, *a, **kw)

        with mock.patch("os.replace", side_effect=replace):
            with self.assertRaises(PublishError) as caught:
                b2.publish()
        self.assertIn("b.txt", str(caught.exception))
        self.assertIn("a.txt", str(caught.exception))
        self.assertEqual((self.task / "a.txt").read_bytes(), b"A2")
        self.assertEqual((self.task / "b.txt").read_bytes(), b"B")
        self.assertEqual(self.temp_leftovers(), [])

        after = statuses(output.check(self.task, b2.files(), previous=None))
        self.assertEqual(after, {"a.txt": "unchanged", "b.txt": "changed"})

    # 5 ----------------------------------------------------------------------------------------------------------
    def test_prune_removes_only_unchanged_stale_files(self):
        first = previous(build(self.task, "b1", {"a.txt": b"A", "keep.txt": b"K"}).publish())

        b2 = build(self.task, "b2", {"a.txt": b"A"})
        self.assertEqual(statuses(b2.plan(first)), {"a.txt": "unchanged", "keep.txt": "stale"})

        kept = b2.publish(previous=first)
        self.assertEqual(statuses(kept), {"a.txt": "unchanged", "keep.txt": "stale"})
        self.assertTrue((self.task / "keep.txt").exists())

        pruned = b2.publish(prune=True, previous=first)
        self.assertEqual(statuses(pruned), {"a.txt": "unchanged", "keep.txt": "removed"})
        self.assertFalse((self.task / "keep.txt").exists())

        edited = self.new_task()
        first = previous(build(edited, "b1", {"a.txt": b"A", "keep.txt": b"K"}).publish())
        (edited / "keep.txt").write_bytes(b"hand edit")
        b3 = build(edited, "b2", {"a.txt": b"A"})
        result = b3.publish(prune=True, previous=first)
        self.assertEqual(statuses(result), {"a.txt": "unchanged", "keep.txt": "stale"})
        self.assertEqual((edited / "keep.txt").read_bytes(), b"hand edit")

    # 6 ----------------------------------------------------------------------------------------------------------
    def test_confine_refuses_escapes_and_symlinks(self):
        for bad in ("../x.txt", "/etc/passwd", "", "a//b.txt", "a/../../b.txt"):
            with self.assertRaises(PublishError, msg=bad):
                confine(self.task, bad)

        (self.task / "real").mkdir()
        os.symlink(self.task / "real", self.task / "link")
        with self.assertRaises(PublishError):
            confine(self.task, "link/x.txt")

        (self.task / "f.txt").write_bytes(b"x")
        os.symlink(self.task / "f.txt", self.task / "s.txt")
        with self.assertRaises(PublishError):
            confine(self.task, "s.txt")

        nested = confine(self.task, "a/b/c.txt")
        self.assertEqual(nested, self.task.resolve() / "a" / "b" / "c.txt")

        b = Build(self.task, "b1")
        b.add("d/x.txt", b"X")
        elsewhere = self.new_task() / "elsewhere"
        elsewhere.mkdir()
        os.symlink(elsewhere, self.task / "d")
        with self.assertRaises(PublishError):
            b.publish()

        not_a_dir = self.new_task() / "file.txt"
        not_a_dir.write_bytes(b"")
        with self.assertRaises(PublishError):
            Build(not_a_dir, "b1")

    # 7 ----------------------------------------------------------------------------------------------------------
    def test_task_lock_is_exclusive(self):
        lock = TaskLock(self.task)
        self.assertEqual(lock.path, self.task.resolve() / "Working_Files" / "build" / ".lock")
        lock.__enter__()
        try:
            self.assertTrue(lock.path.exists())
            with self.assertRaises(PublishError) as caught:
                TaskLock(self.task).__enter__()
            self.assertEqual(str(caught.exception), "another render holds the lock")
        finally:
            lock.__exit__(None, None, None)
        with TaskLock(self.task):
            pass

    # 8 ----------------------------------------------------------------------------------------------------------
    def test_store_revision_is_immutable(self):
        source = self.task / "01_Universe_Inject.sql"
        source.write_bytes(b"-- rev 5\n")
        rel = "Working_Files/run_forensics/rev5/01_Universe_Inject.sql"

        first = output.store_revision(self.task, "rev5")
        self.assertEqual((first.path, first.status), (rel, "new"))
        self.assertEqual((self.task / rel).read_bytes(), b"-- rev 5\n")

        same = output.store_revision(self.task, "rev5")
        self.assertEqual((same.path, same.status), (rel, "unchanged"))
        self.assertEqual(same.sha256_old, same.sha256_new)

        source.write_bytes(b"-- rev 5, edited\n")
        with self.assertRaises(PublishError):
            output.store_revision(self.task, "rev5")
        self.assertEqual((self.task / rel).read_bytes(), b"-- rev 5\n")

        for bad in ("5", "rev", "rev5-1", "Revision5", "", "../rev5"):
            with self.assertRaises(PublishError, msg=bad):
                output.store_revision(self.task, bad)

    # 9 ----------------------------------------------------------------------------------------------------------
    def test_append_line_appends_and_refuses_stored_revisions(self):
        output.append_line(self.task, "Working_Files/build/log.jsonl", '{"a": 1}')
        output.append_line(self.task, "Working_Files/build/log.jsonl", '{"b": 2}')
        self.assertEqual((self.task / "Working_Files/build/log.jsonl").read_text(), '{"a": 1}\n{"b": 2}\n')
        with self.assertRaises(PublishError):
            output.append_line(self.task, "Working_Files/run_forensics/rev1/log.jsonl", "x")
        with self.assertRaises(ValueError):
            output.append_line(self.task, "Working_Files/build/log.jsonl", "two\nlines")

    def test_append_line_skip_if_last_adds_a_repeated_line_once(self):
        rel = "Working_Files/build/log.jsonl"
        self.assertTrue(output.append_line(self.task, rel, "a", skip_if_last=True))       # a new file
        self.assertFalse(output.append_line(self.task, rel, "a", skip_if_last=True))      # the same line again
        self.assertTrue(output.append_line(self.task, rel, "b", skip_if_last=True))
        self.assertTrue(output.append_line(self.task, rel, "a", skip_if_last=True))       # not the last line now
        self.assertTrue(output.append_line(self.task, rel, "a"))                          # without the flag
        self.assertEqual((self.task / rel).read_text(), "a\nb\na\na\n")


if __name__ == "__main__":
    unittest.main()
