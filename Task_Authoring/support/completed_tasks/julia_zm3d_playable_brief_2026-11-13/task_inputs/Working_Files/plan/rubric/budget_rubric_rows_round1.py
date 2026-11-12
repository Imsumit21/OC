#!/usr/bin/env python3
"""Re-map `rubric_rows` in Working_Files/01_Difficulty_Budget.json to the row numbers of the repaired rubric
(/rubric round 1; plan/rubric/fix_round1_map.json). Same rule as budget_rubric_rows.py: per budget unit, the rows that
fail when the unit's deciding record is missed, read from the plan row's "Decided by" trap ids. Both rows of a split
comment keep the ids of the row they come from (no comment is written when the record is missed); deleted rows drop
out; the four added rows (Plushie Chick Delivered, Cannon's empty Board set, the two ordering rows) sit under no unit."""
import json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
meta = json.loads((HERE / "fix_round1_map.json").read_text())
UNIT_OF = {"T1": "C1", "T2": "A2", "T3": "A1", "T7": "A1", "T4": "C2", "T5": "C3", "T15": "C3"}
m = {}
for r in meta:
    if not r["new"]:
        continue
    for t in re.findall(r"\bT\d+\b", r["decided"]):
        if t in UNIT_OF:
            m.setdefault(UNIT_OF[t], set()).add(int(r["new"][1:]))
bp = WF / "01_Difficulty_Budget.json"
b = json.loads(bp.read_text())
b["rubric_rows"] = {u: [f"R{n}" for n in sorted(v)] for u, v in sorted(m.items())}
bp.write_text(json.dumps(b, indent=2, ensure_ascii=False) + "\n")
for u, v in b["rubric_rows"].items():
    print(u, len(v), "rows:", " ".join(v))
