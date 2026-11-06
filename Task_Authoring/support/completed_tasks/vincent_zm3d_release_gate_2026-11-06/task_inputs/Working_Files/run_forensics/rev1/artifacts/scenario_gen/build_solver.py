#!/usr/bin/env python3
"""Writes Working_Files/solver/solver.py with the base cohort table embedded (titles, labels, states from the base
Linear export, via research/zom.json and research/open_all.json). Run from the workspace root:
    python3 -B Task_Authoring/task_inputs/Working_Files/scenario_gen/build_solver.py
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
KEYS = json.loads((HERE / "scope_keys.json").read_text())
ZOM = {m["record"]["identifier"]: m["record"] for m in json.loads((WF / "research/zom.json").read_text())["checks"]["zom"]["matches"]}
OPEN = {m["record"]["identifier"]: m["record"] for m in json.loads((WF / "research/open_all.json").read_text())["checks"]["o"]["matches"]}
PLAN = {x["id"]: x for x in json.loads((WF / "research/cohort_plan.json").read_text())["open"]}
NEW = {}
for line in (HERE / "build_sql.py").read_text().splitlines():
    pass

BASE = {}
for k in KEYS:
    r = ZOM.get(k) or OPEN.get(k)
    if r:
        BASE[k] = {"title": r["title"], "state": r["state_id"], "labels": r.get("labels") or [],
                   "completed_at": r.get("completed_at")}

# call of every base open ticket under Leonard's rules, from the cohort plan, with the injection-stage settlements
CALL = {k: PLAN[k]["call"] for k in PLAN if k in KEYS}
CALL.update({"ZOM-505": "KNOWN ISSUE", "ZOM-483": "BLOCKER", "ZOM-429": "FIXED", "ZOM-517": "FIXED",
             "ZOM-563": "FIXED", "ZOM-564": "FIXED", "ZOM-562": "BLOCKER", "ZOM-559": "BLOCKER",
             "ZOM-449": "BLOCKER", "ZOM-554": "BLOCKER",
             "ZOM-453": "NO CALL"})
DONE_CALL = {  # tickets moved to Done since the Sep 22 gate (base)
    "ZOM-112": "NO CALL", "ZOM-169": "NO CALL", "ZOM-239": "NO CALL", "ZOM-419": "NO CALL", "ZOM-434": "FIXED",
    "ZOM-435": "BLOCKER", "ZOM-473": "BLOCKER", "ZOM-498": "NO CALL", "ZOM-503": "FIXED", "ZOM-506": "FIXED",
    "ZOM-507": "NO CALL", "ZOM-536": "NO CALL", "ZOM-538": "NO CALL", "ZOM-553": "NO CALL", "ZOM-555": "NO CALL",
    "ZOM-557": "FIXED", "ZOM-558": "FIXED", "ZOM-561": "FIXED"}
SEEDED = {  # key: (title, call, build status)
    "ZOM-567": ("Zombie Lane chests claimed on prod don't land in the inventory", "BLOCKER", "server - not live"),
    "ZOM-568": ("Settings language list jumps back to the top while scrolling", "KNOWN ISSUE", "n/a"),
    "ZOM-569": ("Season Pass opens twice from the join popup and leaves an empty screen", "BLOCKER", "not in candidate"),
    "ZOM-571": ("Gem pack price shows $0.00 for a second when the shop opens", "KNOWN ISSUE", "n/a"),
    "ZOM-572": ("Win streak freezer counter shows 2 after using the last one", "KNOWN ISSUE", "n/a"),
    "ZOM-573": ("Collect&Win: claiming the 5th chest crashes the app", "BLOCKER", "n/a"),
    "ZOM-574": ("Zombie Lane info popup text is cut off in German", "KNOWN ISSUE", "n/a"),
    "ZOM-575": ("Add a haptics toggle to settings", "NO CALL", "n/a"),
    "ZOM-576": ("Season Pass premium reward claimed twice grants only one chest", "BLOCKER", "n/a"),
    "ZOM-577": ("level_fail event is missing the booster_used param", "NO CALL", "n/a"),
    "ZOM-578": ("Tutorial stuck at step 3 on a fresh install", "BLOCKER", "n/a"),
    "ZOM-579": ("Boss arena hit VFX plays behind the board on iPad", "KNOWN ISSUE", "n/a"),
    "ZOM-580": ("Daily gift popup shows twice after the midnight reset", "KNOWN ISSUE", "n/a"),
    "ART-793": ("ZM3D - boss arena background flickers on iPhone 12", "KNOWN ISSUE", "n/a"),
    "DES-313": ("ZM level 214 can't be completed", "BLOCKER", "n/a"),
}
missing = [k for k in KEYS if k not in BASE and k not in SEEDED]
assert not missing, missing
for k in KEYS:
    if k in SEEDED:
        continue
    if k in DONE_CALL:
        continue
    assert k in CALL, k

def _lit_placeholder():
    pass


def lit(v):
    s = json.dumps(v, ensure_ascii=False, indent=0, sort_keys=True)
    assert '"""' not in s
    return 'json.loads(r"""' + s + '""")'


import sys
sys.path.insert(0, str(HERE))
import build_sql  # noqa: E402  (definitions only; main() is guarded)
import re  # noqa: E402
RECHECKED = sorted({c[1] for c in build_sql.RECHECK if c[1] in BASE})
ON133 = sorted({c[1] for c in build_sql.SETTLE if c[1] in BASE and "#133" in c[4]} - set(RECHECKED))
QA_TEXT = {}
for cid, key, author, at, body in sorted(build_sql.SETTLE + build_sql.RECHECK, key=lambda c: c[3]):
    if key not in BASE or key == "ZOM-564":
        continue
    toks = []
    for tok in re.findall(r"#(?:135|133|50|49)\b", body):
        if tok not in toks:
            toks.append(tok)
    verb = "can't reproduce on" if key in ("ZOM-429", "ZOM-517") else "reproduces on"
    QA_TEXT[key] = f"{verb} {' / '.join(toks) or 'the candidates'}" + (" (Samsung S22)" if "Samsung" in body else "")
src = (HERE / "solver_template.py").read_text()
src = src.replace("__RECHECKED__", lit(RECHECKED)).replace("__ON133__", lit(ON133)).replace("__QA_TEXT__", lit(QA_TEXT))
src = src.replace("__KEYS__", lit(KEYS)).replace("__BASE__", lit(BASE))
src = src.replace("__CALL__", lit(CALL)).replace("__DONE_CALL__", lit(DONE_CALL))
src = src.replace("__SEEDED__", lit({k: list(v) for k, v in SEEDED.items()}))
(WF / "solver").mkdir(exist_ok=True)
(WF / "solver" / "solver.py").write_text(src)
print("solver written:", len(KEYS), "keys")
