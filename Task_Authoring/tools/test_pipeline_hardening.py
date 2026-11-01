"""Regression tests for the pipeline hardening: atomic caches, report-pair publication, volume floors.

Run from Task_Authoring/tools with:  python3 -B -m unittest test_pipeline_hardening -v
"""
from __future__ import annotations

import errno
import json
import os
import stat
import tempfile
import threading
import unittest
from pathlib import Path
from unittest import mock

import base_check
import hardness_gate
import persona_view
import redteam_review


def mode(path: Path) -> int:
    return stat.S_IMODE(path.stat().st_mode)


class AtomicCacheTests(unittest.TestCase):
    def test_new_cache_is_written_and_0644(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "cache.json"
            base_check._atomic_json(path, {"a": 1})
            self.assertEqual(json.loads(path.read_text()), {"a": 1})
            self.assertEqual(mode(path), 0o644)

    def test_existing_mode_is_preserved(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "cache.json"
            path.write_text("{}")
            path.chmod(0o600)
            base_check._atomic_json(path, {"a": 2})
            self.assertEqual(mode(path), 0o600)
            persona_view._atomic_json(path, {"b": 3})
            self.assertEqual(mode(path), 0o600)

    def test_corrupt_cache_is_rebuilt(self):
        with tempfile.TemporaryDirectory() as td:
            old, base_check.CACHE = base_check.CACHE, Path(td)
            try:
                (base_check.CACHE / "base_x.json").write_text('{"a": [1')
                self.assertEqual(base_check._cached("x", lambda: {"ok": True}), {"ok": True})
                self.assertEqual(json.loads((base_check.CACHE / "base_x.json").read_text()), {"ok": True})
            finally:
                base_check.CACHE = old

    def test_concurrent_writers_never_expose_partial_json(self):
        blob = "x" * 100_000
        errors: list[str] = []
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "cache.json"
            stop = threading.Event()

            def writer():
                for i in range(50):
                    base_check._atomic_json(path, {"data": blob, "n": i})

            def reader():
                while not stop.is_set():
                    try:
                        if json.loads(path.read_text()).get("data") != blob:
                            errors.append("partial payload")
                    except FileNotFoundError:
                        pass
                    except Exception as error:  # noqa: BLE001 - recorded, asserted empty
                        errors.append(repr(error))

            rd = threading.Thread(target=reader)
            rd.start()
            ws = [threading.Thread(target=writer) for _ in range(4)]
            for t in ws:
                t.start()
            for t in ws:
                t.join()
            stop.set()
            rd.join()
        self.assertEqual(errors, [])


class PairWriteTests(unittest.TestCase):
    def test_pair_is_written_with_default_modes(self):
        with tempfile.TemporaryDirectory() as td:
            out, second = Path(td) / "r.md", Path(td) / "r.second.md"
            redteam_review.write_pair(out, second, "first\n", "second\n")
            self.assertEqual((out.read_text(), second.read_text()), ("first\n", "second\n"))
            self.assertEqual((mode(out), mode(second)), (0o644, 0o644))

    def test_read_only_primary_is_restored_when_second_replace_fails(self):
        with tempfile.TemporaryDirectory() as td:
            out, second = Path(td) / "r.md", Path(td) / "r.second.md"
            out.write_text("OLD\n")
            out.chmod(0o444)
            second.write_text("OLD2\n")
            real_replace = os.replace

            def flaky(src, dst):
                if Path(dst) == second:
                    raise OSError(errno.EIO, "injected failure")
                return real_replace(src, dst)

            with mock.patch("os.replace", side_effect=flaky):
                with self.assertRaises(OSError):
                    redteam_review.write_pair(out, second, "NEW\n", "NEW2\n")
            self.assertEqual(out.read_text(), "OLD\n")
            self.assertEqual(mode(out), 0o444)
            self.assertEqual(second.read_text(), "OLD2\n")
            self.assertEqual(sorted(p.name for p in Path(td).iterdir() if p.name.endswith((".tmp", ".bak"))), [])

    def test_failed_staging_leaves_no_temp_and_publishes_nothing(self):
        with tempfile.TemporaryDirectory() as td:
            out, second = Path(td) / "r.md", Path(td) / "r.second.md"
            real_fdopen = os.fdopen

            class Boom:
                def __init__(self, handle):
                    self.handle = handle

                def __enter__(self):
                    return self

                def __exit__(self, *exc):
                    self.handle.close()

                def write(self, _data):
                    raise OSError(28, "No space left on device")

            with mock.patch("os.fdopen", side_effect=lambda fd, m: Boom(real_fdopen(fd, m))):
                with self.assertRaises(OSError):
                    redteam_review.write_pair(out, second, "x", "y")
            self.assertFalse(out.exists() or second.exists())
            self.assertEqual(sorted(p.name for p in Path(td).iterdir() if p.name.endswith((".tmp", ".bak"))), [])

    def test_symlink_target_is_refused(self):
        with tempfile.TemporaryDirectory() as td:
            out, second = Path(td) / "r.md", Path(td) / "r.second.md"
            out.symlink_to(Path(td) / "missing.md")
            with self.assertRaises(ValueError):
                redteam_review.write_pair(out, second, "x", "y")
            self.assertTrue(out.is_symlink())
            self.assertFalse(second.exists())

    def test_symlinked_lock_path_is_ignored(self):
        # The lock is the output directory's own inode, so a stray .lock pathname is not consulted.
        with tempfile.TemporaryDirectory() as td:
            out, second = Path(td) / "r.md", Path(td) / "r.second.md"
            elsewhere = Path(td) / "elsewhere"
            elsewhere.write_text("x")
            (Path(td) / ".r.md.lock").symlink_to(elsewhere)
            redteam_review.write_pair(out, second, "x", "y")
            self.assertEqual((out.read_text(), second.read_text()), ("x", "y"))

    def test_directory_target_is_refused_before_publication(self):
        with tempfile.TemporaryDirectory() as td:
            out, block = Path(td) / "r.md", Path(td) / "r.second.md"
            block.mkdir()
            with self.assertRaises(ValueError):
                redteam_review.write_pair(out, block, "x", "y")
            self.assertFalse(out.exists())

    def test_metadata_error_does_not_widen_permissions(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "cache.json"
            path.write_text("{}")
            path.chmod(0o600)
            real_stat = Path.stat
            calls = {"n": 0}

            def flaky(self, *args, **kwargs):
                if self == path and calls["n"] == 0:
                    calls["n"] += 1
                    raise OSError(errno.EIO, "input/output error")
                return real_stat(self, *args, **kwargs)

            with mock.patch.object(Path, "stat", flaky):
                with self.assertRaises(OSError):
                    base_check._atomic_json(path, {"a": 1})
            self.assertEqual(path.read_text(), "{}")
            self.assertEqual(mode(path), 0o600)

    def test_concurrent_writers_never_leave_a_mixed_pair(self):
        with tempfile.TemporaryDirectory() as td:
            out, second = Path(td) / "r.md", Path(td) / "r.second.md"
            mixed = []
            for _ in range(20):
                barrier = threading.Barrier(2)

                def writer(tag, barrier=barrier):
                    barrier.wait()
                    redteam_review.write_pair(out, second, f"{tag}-primary\n", f"{tag}-secondary\n")

                threads = [threading.Thread(target=writer, args=(tag,)) for tag in ("A", "B")]
                for t in threads:
                    t.start()
                for t in threads:
                    t.join()
                a, b = out.read_text(), second.read_text()
                if a.split("-primary")[0] != b.split("-secondary")[0]:
                    mixed.append((a.strip(), b.strip()))
            self.assertEqual(mixed, [])


class VolumeExceptionTests(unittest.TestCase):
    VALID = {"reason": "requester-approved reduction", "requester_confirmation": "requester, 2026-11-01",
             "call_budget_floor": 150, "per_record_floor": 30}

    def manifest(self, **overrides):
        man = {"effective_profile": "extreme", "horizon": "Long Horizon", "volume_exception": dict(self.VALID)}
        man["volume_exception"].update(overrides)
        return man

    def test_valid_exception_replaces_only_the_two_minima(self):
        thresholds, floors = hardness_gate.effective_thresholds(self.manifest(), "extreme")
        self.assertEqual(floors, {"budget": 150, "per_record_calls": 30})
        for key, value in hardness_gate.PROFILES["extreme"].items():
            if key not in ("budget", "per_record_calls"):
                self.assertEqual(thresholds[key], value)
        self.assertEqual(hardness_gate.PROFILES["extreme"]["budget"], 500)
        self.assertEqual(hardness_gate.PROFILES["extreme"]["per_record_calls"], 300)

    def test_boundaries_are_accepted(self):
        for key, value in (("call_budget_floor", 100), ("call_budget_floor", 500),
                           ("per_record_floor", 0), ("per_record_floor", 300)):
            thresholds, floors = hardness_gate.effective_thresholds(self.manifest(**{key: value}), "extreme")
            self.assertIsNotNone(floors, (key, value))
            self.assertEqual(thresholds["budget" if key == "call_budget_floor" else "per_record_calls"], value)

    def test_malformed_values_fail_closed(self):
        malformed = [None, "yes", [], {},
                     {"reason": "", "requester_confirmation": "c", "call_budget_floor": 150, "per_record_floor": 30},
                     {"reason": "r", "requester_confirmation": "c", "call_budget_floor": True, "per_record_floor": 30},
                     {"reason": "r", "requester_confirmation": "c", "call_budget_floor": 150.0, "per_record_floor": 30},
                     {"reason": "r", "requester_confirmation": "c", "call_budget_floor": "150", "per_record_floor": 30},
                     {"reason": "r", "requester_confirmation": "c", "call_budget_floor": 99, "per_record_floor": 30},
                     {"reason": "r", "requester_confirmation": "c", "call_budget_floor": 501, "per_record_floor": 30},
                     {"reason": "r", "requester_confirmation": "c", "call_budget_floor": 150, "per_record_floor": -1},
                     {"reason": "r", "requester_confirmation": "c", "call_budget_floor": 150, "per_record_floor": 301},
                     {"reason": "r", "requester_confirmation": "c", "call_budget_floor": 150, "per_record_floor": 30,
                      "per_record_flor": -1}]
        for bad in malformed:
            floors, problems = hardness_gate.volume_exception({"volume_exception": bad}, "extreme")
            self.assertIsNone(floors, bad)
            self.assertTrue(problems, bad)
            thresholds, applied = hardness_gate.effective_thresholds({"effective_profile": "extreme",
                                                                      "volume_exception": bad}, "extreme")
            self.assertIsNone(applied, bad)
            self.assertEqual(thresholds, dict(hardness_gate.PROFILES["extreme"]), bad)

    def test_non_extreme_profile_rejects_the_key(self):
        floors, problems = hardness_gate.volume_exception(self.manifest(), "normal")
        self.assertIsNone(floors)
        self.assertTrue(problems)


if __name__ == "__main__":
    unittest.main()
