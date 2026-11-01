#!/usr/bin/env python3
"""Advisory cap selection in difficulty_mutation.caps_for (Hardness v2 Part 1).

A V3 assignment always carries its mode, and the authoring gates refuse to infer one
(difficulty_stats, pinned by test_difficulty_v3). The advisory geometry path used to fall
back to Hard silently; Hardness v2 treats a task with no mode as Medium, so the advisory
default is Medium and the fallback is disclosed on stderr.

  python3 -B -m unittest test_difficulty_mutation -v     (from Task_Authoring/tools)
"""
from __future__ import annotations

import contextlib
import io
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import difficulty_mutation as dm  # noqa: E402


class CapsFor(unittest.TestCase):
    def caps(self, context):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            out = dm.caps_for("v3", context)
        return out, err.getvalue()

    def test_missing_mode_defaults_to_medium_with_disclosure(self):
        out, err = self.caps({"spec_version": "V3"})
        self.assertEqual(out["V3"]["mode"], "medium")
        self.assertEqual(out["V3"]["cap"], dm.ds.DIFFICULTY_CAPS["medium"])
        self.assertIn("no difficulty_mode", err)
        self.assertIn("Medium", err)

    def test_no_context_defaults_to_medium(self):
        out, err = self.caps(None)
        self.assertEqual(out["V3"]["mode"], "medium")
        self.assertIn("no difficulty_mode", err)

    def test_explicit_mode_is_kept_without_disclosure(self):
        for mode in ("easy", "medium", "hard"):
            out, err = self.caps({"spec_version": "V3", "difficulty_mode": mode})
            self.assertEqual(out["V3"]["mode"], mode)
            self.assertEqual(out["V3"]["cap"], dm.ds.DIFFICULTY_CAPS[mode])
            self.assertEqual(err, "")


if __name__ == "__main__":
    unittest.main()
