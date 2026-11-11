"""difficulty_stats.norm_title: verifier titles bind to 09_Rubrics.json titles despite the verifier copy's formatting.

The input builder refuses to bind a verifier row whose title matches no rubric title ("never bind by guesswork"), so
every formatting difference the platform's verifier copy introduces must normalise away on both sides.
"""
from __future__ import annotations

import glob
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import difficulty_stats as ds  # noqa: E402

ARCHIVES = HERE.parent / "support" / "completed_tasks"


class NormTitle(unittest.TestCase):
    def same(self, verifier, rubric):
        self.assertEqual(ds.norm_title(verifier), ds.norm_title(rubric))

    def test_escaped_brackets(self):
        self.same(r"The Agent emails \[PERSON_NAME_0001\] the list", "The Agent emails [PERSON_NAME_0001] the list")

    def test_html_entities(self):
        self.same("average CPM strictly above 90 (&gt; 90)", "average CPM strictly above 90 (> 90)")
        self.same("Tom &amp; Jerry", "Tom & Jerry")

    def test_bold_markers(self):
        self.same("**The Agent states that enrage is off**", "The Agent states that enrage is off")

    def test_existing_forms_still_hold(self):
        self.same('Says \\"done\\" and links [the doc](https://x.example/doc)', 'Says "done" and links the doc')
        self.same("Robert’s  sheet", "Robert's sheet")

    def test_same_text_on_both_sides_is_unchanged_and_different_text_stays_different(self):
        for title in ("A > B", "x &gt; y", "two ** stars", "[x]"):
            self.same(title, title)
        self.assertNotEqual(ds.norm_title("tier 1 above 90"), ds.norm_title("tier 2 above 90"))


class ArchivedVerifierCopies(unittest.TestCase):
    """Every verifier row of every archived task binds to a rubric title, with no two rubric titles merging."""

    def test_every_archived_verifier_row_binds(self):
        checked = 0
        for ver in sorted(glob.glob(str(ARCHIVES / "*" / "task_inputs" / "10_Baseline_Verifier_Results.md"))):
            task = Path(ver).parent
            try:
                rubrics, _ = ds.parse_rubrics(task / "09_Rubrics.json")
                runs = ds.parse_verifier(Path(ver))
            except (SystemExit, ValueError, OSError):
                continue                      # an archive with an empty template rubric or a damaged copy
            titles = [ds.norm_title(r["title"]) for r in rubrics]
            with self.subTest(task=task.parent.name):
                self.assertEqual(len(titles), len(set(titles)), "two rubric titles normalise to the same text")
                unbound = sorted({row["title"][:80] for rows in runs.values() for row in rows
                                  if ds.norm_title(row["title"]) not in set(titles)})
                self.assertEqual(unbound, [])
            checked += 1
        if not checked:
            self.skipTest("no archived task with a verifier copy in this checkout")


if __name__ == "__main__":
    unittest.main()
