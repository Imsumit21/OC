"""The case comparator must not silently drop a bad, missing or extra judgment."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hg_check_rubric_cases import compare


class CaseComparisonTests(unittest.TestCase):
    def test_complete_review_agrees(self):
        result = compare({"good": "PASS", "bad": "ISSUE"}, [
            dict(id="good", verdict="PASS", reason="Authorized comparison stays atomic."),
            dict(id="bad", verdict="ISSUE", reason="Wrong price passes all rows.")])
        self.assertTrue(result["passed"])
        self.assertEqual(result["matches"], 2)

    def test_false_positive_false_negative_missing_and_extra_cases_fail(self):
        expected = {"good": "PASS", "bad": "ISSUE"}
        for actual in [[], [dict(id="good", verdict="ISSUE", reason="False positive.")],
                       [dict(id="bad", verdict="PASS", reason="Missed gap.")],
                       [dict(id="extra", verdict="PASS", reason="Unknown case.")]]:
            with self.subTest(actual=actual):
                self.assertFalse(compare(expected, actual)["passed"])

    def test_duplicate_judgments_do_not_inflate_match_count(self):
        row = dict(id="good", verdict="PASS", reason="Valid equivalent representation.")
        with self.assertRaises(ValueError):
            compare({"good": "PASS"}, [row, row])


if __name__ == "__main__":
    unittest.main()
