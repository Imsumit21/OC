#!/usr/bin/env python3
"""Write Working_Files/01_Hardness_Manifest.json: the scenario's draft manifest (every id kept) plus what only the SQL
settles - the fact sheet (`facts`, per-record facts with `home_ids`), hazard acknowledgements, integration exceptions,
the solver / gradable surface / preflight bindings and an empty design_delta. Re-run after any SQL, solver or
preflight change (the digests bind them).

    python3 -B Task_Authoring/task_inputsN2/Working_Files/injection_gen/build_final_manifest.py
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
SG = WF / "scenario_gen"
DRAFT = json.loads((WF / "01_Hardness_Manifest.draft.json").read_text())
FINAL = json.loads((SG / "roster_final.json").read_text())
I = json.loads((SG / "ids.json").read_text())["ids"]
SQL = (TASK / "01_Universe_Inject.sql").read_text()


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


ADS = [r for r in FINAL["surfaces"] if r.get("ticket")]


def comment_ids_with(value: str) -> list:
    out = []
    for r in ADS:
        n = r["ticket"][4:]
        for i, body in ((1, r.get("comment_1")), (2, r.get("comment_2"))):
            if body and re.search(r"(?<![0-9A-Za-z])" + re.escape(value) + r"(?![0-9])", body):
                out.append(f"cmt_art{n}_{i}")
    return out


PLAN_C = I["gmail_fred_plan"]["msg"]
DOC, DECK, SHEET = I["doc_release"], I["deck_seasonal"]["presentation"], I["sheet_live"]

FACTS = [
    {"key": "Halloween ad hand-off", "aliases": ["needs to be with me by"], "value": "2025-10-15", "kind": "date",
     "must_appear_in": [PLAN_C]},
    {"key": "Android US phone hand-off", "aliases": ["has to be with me by"], "value": "2025-10-10", "kind": "date",
     "must_appear_in": [I["slack_fred_review_reply"]["row_id"]]},
    {"key": "Merge cut", "value": "2025-10-16", "kind": "date", "must_appear_in": [DOC]},
    {"key": "Android US tablet campaign ends", "value": "2025-10-12", "kind": "date", "must_appear_in": [PLAN_C]},
    {"key": "zombie swap build", "aliases": ["the zombie swap with the new background"], "value": "Android #1452", "kind": "id",
     "must_appear_in": [DECK]},
    {"key": "Halloween review", "aliases": ["ZM3D Halloween review"], "value": "2025-10-02", "kind": "date"},
    {"key": "vendor company", "value": "KayKit", "kind": "name"},
]
# per-record capture facts: each build that decides a call lives only in the ticket comments that carry it
for build, why in (("Android #1427", "the Jul 28 capture of the cheer fastcouch and boris cuts (before the swap)"),
                   ("Android #1450", "the portrait end card's render build (two builds before the swap)"),
                   ("Android #1896", "the Sep 16 re-capture"), ("Android #1935", "the Sep 22 re-capture"),
                   ("Android #1966", "the Sep 24 re-capture"), ("Android #1630", "the Aug 13 capture of the marcus.bennett cuts")):
    homes = comment_ids_with(build)
    if build == "Android #1935":          # rev3: Marcus's #zm-animations note carries this build too
        homes = homes + [I["slack_marcus_recapture"]["row_id"]]
    assert homes, build
    FACTS.append({"key": f"capture build {build}", "value": build, "kind": "id", "home_ids": homes, "note": why})

HAZARDS = [
    {"hazard_id": "L05", "resolution": "dated_claim", "requirement": "R1",
     "why_safe": "ART-774 (store screenshot spec, Done 2025-04-15) is read only for its dated Mar-Apr spec list (trap T5); the SQL never modifies or cites it, and the live sets come from the sheet's Store tab"},
    {"hazard_id": "R04", "resolution": "excluded", "requirement": "R10",
     "why_safe": "no seeded Slack message links a Drive file; the sheet, calendar doc and deck are named by title only"},
    {"hazard_id": "R07", "resolution": "excluded", "requirement": "R3",
     "why_safe": "no GitHub PR or review is seeded, so no #zombie-prs mirror is owed; the only repo read is the icon build settings"},
    {"hazard_id": "R08", "resolution": "excluded", "requirement": "R10",
     "why_safe": "the Halloween review event is seeded without invitation mails (integration_exceptions no_notify), so no invite mail can disagree with it"},
]
INTEGRATION_EXCEPTIONS = [
    {"record_id": I["gcal_review"]["ical_uid"],
     "reason": "no_notify: Leonard put the review on the team's calendars at 22:10Z right after his 22:05Z ask, which itself announces 'before thursday's review'; he sent no invitation mail (INT-11 is optional per event; base: 105 of 941 meetings with attendees have none)"},
]


# rev3 (/create-hardening MODE B report, section 10; /create-scenario --revise section 14): what changed against rev2
DESIGN_DELTA = [
    {"id": "R_ALREADY_MADE", "change": "rebuilt as R_TEST_TURNED_DOWN (A24)", "reason": "LEAKED on one keyword search (run-1 event 217); the DM and the two files stay as the done source and Robert's review in another channel is the missing piece"},
    {"id": "R_PACK_ALIAS", "change": "purged as a rule; T7 kept as a plain distractor, CH5 removed", "reason": "FALSE: no graded row, the run turned the bundle down in one line (run-1 event 299)"},
    {"id": "CH5", "change": "removed with R_PACK_ALIAS", "reason": "no graded fact depends on the alias"},
    {"id": "T9", "change": "rebuilt: the re-capture note left the three tickets for Marcus's #zm-animations note; now R_RECAPTURE_NOTE", "reason": "same_container on linear:ART-795 (hardness_v2_check SAME_PLACE)"},
    {"id": "T3", "change": "family completion_elsewhere to done_gap", "reason": "Marcus's test no longer counts as finished work; Reuse becomes Halloween version"},
    {"id": "CH4", "change": "root cause A25 to A24, new hop to Robert's review", "reason": "follows T3"},
    {"id": "R5", "change": "Android US phone hand-off Fri Oct 10 added", "reason": "move 1, R_REVIEW_WINDOW"},
    {"id": "R8", "change": "Julia Lawson takes the ad statics", "reason": "move 4, R_STATICS_COVER"},
]


SLACK_ROW = {I[k]["locator"]: I[k]["row_id"] for k in ("slack_ask", "slack_robert_pointer", "slack_martin_export", "slack_leonard_store_reply",
                                                       "slack_dm_root", "slack_dm_marcus_reply", "slack_robert_icon_reply",
                                                       "slack_fred_review_reply", "slack_marcus_recapture", "slack_marcus_test",
                                                       "slack_robert_test_reply", "slack_marcus_test_reply", "slack_martin_leave",
                                                       "slack_leonard_leave_reply")}


def slack_rows(x):
    """Seeded Slack records are cited by their SQL row id (sha256(channel|ts)[:32]) once the SQL exists; containers keep
    'slack:C/ts' and base Slack pointers stay channel/ts locators."""
    if isinstance(x, dict):
        return {k: (v if k == "container" else slack_rows(v)) for k, v in x.items()}
    if isinstance(x, list):
        return [slack_rows(v) for v in x]
    return SLACK_ROW.get(x, x) if isinstance(x, str) else x


def main() -> None:
    m = slack_rows(dict(DRAFT))
    m["facts"] = FACTS
    m["hazard_acknowledgements"] = HAZARDS
    m["integration_exceptions"] = INTEGRATION_EXCEPTIONS
    m["design_delta"] = DESIGN_DELTA
    solver = WF / "solver" / "solver.py"
    if solver.exists():
        m["solver"] = {"path": "Working_Files/solver/solver.py", "digest": sha(solver)}
    m["gradable_surface"] = {"path": "01_Gradable_Surface.json", "digest": sha(WF / "01_Gradable_Surface.json")}
    # the preflight report binds this manifest by sha256 (stage_gate structure.preflight), so the manifest never
    # carries the report's digest back (that would be a freshness cycle)
    (WF / "01_Hardness_Manifest.json").write_text(json.dumps(m, indent=1, ensure_ascii=False) + "\n")
    print("final manifest:", len(FACTS), "facts;", sum(len(f.get("home_ids", [])) for f in FACTS), "home rows;",
          "solver bound" if "solver" in m else "no solver yet")


if __name__ == "__main__":
    main()
