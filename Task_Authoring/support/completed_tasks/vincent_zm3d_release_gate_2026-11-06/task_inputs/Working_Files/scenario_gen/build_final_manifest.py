#!/usr/bin/env python3
"""Final hardness manifest for /create-injection: the draft's ids unchanged plus what only the SQL settles.

Run from the workspace root after build_design.py and build_sql.py:
    python3 -B Task_Authoring/task_inputs/Working_Files/scenario_gen/build_final_manifest.py
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
IDS = json.loads((HERE / "ids.json").read_text())
SOLVER = WF / "solver" / "solver.py"
PREFLIGHT = WF / "01c_Preflight_Report.json"


def digest(p: Path):
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None


m = json.loads((WF / "01_Hardness_Manifest.draft.json").read_text())

# Seeded Slack messages are cited by their SQL row id (sha256(channel|ts)[:32]); base Slack stays as channel/ts.
LEDGER = json.loads((HERE / "records.json").read_text())
SEEDED_SLACK = {r["id"] for r in LEDGER if r["table"] == "slack.slack_messages"}


def sid(ref):
    if isinstance(ref, str) and ref in SEEDED_SLACK:
        ch, ts = ref.split("/")
        return hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]
    return ref


for sec in ("ask_fragments", "traps", "authorities"):
    for it in m.get(sec, []):
        for f in ("seeded_ids", "decoy_seeded_ids"):
            if f in it:
                it[f] = [sid(x) for x in it[f]]
        for v in it.get("version_records", []):
            if v.get("seeded") and "id" in v:
                v["id"] = sid(v["id"])
        if "locator" in it:
            it["locator"] = sid(it["locator"])
for s in m["cohort"]["evidence_surfaces"]:
    s["seeded_ids"] = [sid(x) for x in s.get("seeded_ids", [])]
for c in m.get("chains", []):
    for h in c["hops"]:
        h["record"] = sid(h["record"])
for a in m.get("anchors", []):
    a["seeded_ids"] = [sid(x) for x in a.get("seeded_ids", [])]

m["facts"] = [
    {"key": "store release ticket", "value": "ZOM-570", "kind": "id", "must_appear_in": [IDS["slack_announce"]]},
    {"key": "go/no-go", "value": "2025-10-03", "kind": "date"},
    {"key": "coins before the update", "value": "18,400", "kind": "count", "home_ids": [IDS["update_log"]]},
]

m["hazard_acknowledgements"] = [
    {"hazard_id": "L03", "resolution": "excluded", "requirement": "R5",
     "why_safe": "ZOM-292 and ZOM-387 (open while match3d#267 / #319 merged) are register rows only; both are NO CALL "
                 "under Leonard's rules (tooling / analytics) whatever shipped. The SQL neither modifies nor cites them."},
    {"hazard_id": "L06", "resolution": "excluded", "requirement": "R5",
     "why_safe": "ZOM-16, ZOM-293, ZOM-317, ZOM-453 and ZOM-458 are called on their own state and report; the SQL adds "
                 "a re-check note to ZOM-458 only (its own symptom on #135 / #50) and changes no parent or state field."},
    {"hazard_id": "R01", "resolution": "excluded",
     "why_safe": "no seeded text cites a Linear key that does not exist; every key in seeded text is a base or seeded "
                 "issue (base_check Check A)."},
    {"hazard_id": "R07", "resolution": "excluded",
     "why_safe": "the only seeded GitHub records are on match3d-backend, which is outside the INT-01 mirror list, so no "
                 "#zombie-prs copy is owed."},
]

m["integration_exceptions"] = [
    {"record_id": "harmonygames-Games/match3d-backend#36",
     "reason": "no linear[bot] comment: none of the base match3d-backend PRs (#30-#35) carries one"},
]

m["design_delta"] = [
    {"id": "K9", "change": "delegation_quote verbatim from ZOM-570: 'post the candidates in #zombie-bugs'",
     "reason": "quote settled by the SQL text"},
    {"id": "K10", "change": "delegation_quote verbatim from ZOM-570: 'push notes go in the comments here'",
     "reason": "the comment is posted after the ticket, so the ticket names the comments generically"},
]

m["solver"] = {"path": "Working_Files/solver/solver.py", "digest": digest(SOLVER)}
# no `preflight` field: the preflight report binds this manifest's sha256, so the manifest cannot carry the report's
m["gradable_surface"] = {"path": "01_Gradable_Surface.json", "digest": digest(WF / "01_Gradable_Surface.json")}

(WF / "01_Hardness_Manifest.json").write_text(json.dumps(m, indent=1, ensure_ascii=False) + "\n")
print("final manifest written;", len(m["facts"]), "facts; solver", (m["solver"]["digest"] or "missing")[:12],
      "; preflight", (m.get("preflight") or {}).get("digest", "missing")[:12])
