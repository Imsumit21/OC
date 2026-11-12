#!/usr/bin/env python3
"""Add `rubric_rows` to Working_Files/01_Difficulty_Budget.json: per budget unit, the R<n> rows of 09_Rubrics.json
(R<n> = plan P<n>) that fail when the unit's deciding record is missed. A row's plan "Decided by" trap ids name the
mechanism: T1 EXPORT (C1, Marcus's post) · T2 ARTHOLD (A2, Robert's note) · T3 REVISED and T7 ZIP (A1, Brian's log) ·
T4 AUDIO (C2, Calvin's sheet) · T5/T15 PICKS (C3, Robert's reply). The DM counts carry every trap id: a miss of any
deciding record moves a line between states, so each count row fails with each unit."""
import json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
rows = json.loads((HERE / "rows.json").read_text())
UNIT_OF = {"T1": "C1", "T2": "A2", "T3": "A1", "T7": "A1", "T4": "C2", "T5": "C3", "T15": "C3"}
m = {}
for r in rows:
    for t in re.findall(r"\bT\d+\b", r["decided"]):
        if t in UNIT_OF:
            m.setdefault(UNIT_OF[t], set()).add(int(r["P"][1:]))
bp = WF / "01_Difficulty_Budget.json"
b = json.loads(bp.read_text())
b["rubric_rows"] = {u: [f"R{n}" for n in sorted(v)] for u, v in sorted(m.items())}
bp.write_text(json.dumps(b, indent=2, ensure_ascii=False) + "\n")
for u, v in b["rubric_rows"].items():
    print(u, len(v), "rows:", " ".join(v))
