"""Rubric plan rows for calvin_qm_epic (rev3b) after the /rubric round-1 Fix List: loaded from plan/rubric_final.json, which
plan/apply_fixlist.py builds from the reviewed rows (out/rubric_rows.draft1.py, reviewed JSON afbc830d0cbb) and the Fix List in
Working_Files/platform_reports/rubric_r1_FAIL.md. One dict per criterion, in file order."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, "rubric_final.json")))
PN = {r["fact"]: r["p"] for r in R}
assert len(PN) == len(R)
if __name__ == "__main__":
    import collections
    print("rows", len(R), collections.Counter(r["band"] for r in R), "weight", sum(r["band"] for r in R))
