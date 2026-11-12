#!/usr/bin/env python3
"""Build Working_Files/01_Difficulty_Budget.json (scenario S5c, design D3 = rev2). Basis: the rubric skeleton when asked, else the surface.
A unit's rows are the surface slots only its mechanism decides, plus, for the two anchors, one list total and its echo in the
reply (they fail whenever that anchor is missed; no other unit is credited with them)."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import design_model as M
WF = Path(__file__).resolve().parents[1]
surface = json.loads((WF / "01_Gradable_Surface.json").read_text())
skel_path = WF / "01_Rubric_Skeleton.json"
basis = sys.argv[1] if len(sys.argv) > 1 else "surface"
S = M.SEED
REVISED_ROWS = [s["id"] for s in surface["slots"] if s["mechanisms"] == ["REVISED"]]
# D3: find rates are the counts measured in the seven rev1 runs (01a_Hardening_Report.md, hardening_gen/out/reach.json), adjusted
# only where D3 removes a route that run used; each basis names the runs and events.
UNITS = [
    ("A1", "anchor", "ZIP", "the packer's own log of the outgoing folder decides two things: Friday's instruments zip will not unpack, and the three recoloured items were sent again and are fine",
     "folder_log", "second_carrier_by_rule_owner", ("gdocs", "get_document_text"),
     ("gdocs", S["c4_log"]["id"], f"file:{S['c4_log']['id']}", True), [0.10, 0.40],
     "rev1: 0 of 7 runs searched Drive for the outgoing folder by name; 5 of 6 baseline runs listed the log only through a full-text Drive search for 'sound' (run-2 event 406, run-3 333, run-4 307, run-5 384, run-6 419), a route D3 removes ('The .wav exports.'); 3 of 7 searched Slack for 'outgoing' (run-1 event 281, run-4 365, run-5 419)",
     REVISED_ROWS + ["A1", "W1"]),
    ("A2", "anchor", "ARTHOLD", "someone who knows the art says, in his DM with Julia, that one category's art is being redone", "art_in_progress", "dm_with_non_owner", ("slack", "read_dm"),
     ("slack", S["a2_dm"]["id"], f"slack:{M.DM_ROBERT}", True), [0.15, 0.45],
     "rev1: 1 of 7 runs read Julia's DM with Robert from 24 Sep (run-6 event 308); 2 of 7 swept her DMs by date (run-2 event 489, run-4 event 346); a search for Robert's messages with limit 50 reached back only to Mon 29 Sep 10:50 PM PT (run-1 event 276), before which the note sits",
     ["A2", "W2"]),
    ("C1", "variance", "EXPORT", "twelve lines saved out of the Unity project are in a format the vendor refuses", "export_format", "de_named_root_record", ("slack", "read_channel"),
     ("slack", S["a1_post"]["id"], f"slack:{M.MATCH3D_CH}", True), [0.30, 0.57],
     "rev1: 4 of 7 runs found Marcus's post (run-1 event 284 by his messages, run-2 events 424 and 446, run-3 event 304 by 'export', run-6 event 259 by channel history); D3 removes the 'export' route, leaving 3 of 7", []),
    ("C2", "variance", "AUDIO", "which sound cues are ours to pass on is in a sheet nothing links", "", "second_carrier_by_rule_owner", ("gsheets", "values_get"),
     ("gsheets", S["c2_sheet"]["id"], f"file:{S['c2_sheet']['id']}", True), [0.70, 0.95],
     "rev1: 6 of 7 runs found the sheet with one Drive search (five full-text 'sound', the pre-check 'Universal Sound'; e.g. run-3 event 333): measured, not a coin flip; kept as designed (no v2 move was chosen for it)", []),
    ("C3", "variance", "PICKS", "Robert's later reply under another post changes one pick, naming no item", "", "reply_under_unrelated_parent", ("slack", "read_thread"),
     ("slack", S["c3_reply"]["id"], f"slack:{M.BASE['art_bow_root']}", True), [0.30, 0.57],
     "rev1: 3 of 7 runs opened Julia's bow thread (run-1 event 321, run-2 event 345, run-6 event 314); 5 read #zombie-art", []),
]
slots = surface["slots"]
slot_w = {s["id"]: s["weight"] for s in slots}
if basis == "skeleton":
    rows_all = json.loads(skel_path.read_text())["rows"]
    weight = {r["id"]: r["weight"] for r in rows_all}
    row_of = {r["slot"]: r["id"] for r in rows_all if r.get("slot")}
else:
    weight = dict(slot_w); row_of = {s: s for s in slot_w}
total = sum(weight.values())
units = []
for uid, role, mech, cause, key, carrier, habit, dec, rate, basis_txt, extra in UNITS:
    own = [s["id"] for s in slots if s["mechanisms"] == [mech]] + extra
    rows = [row_of[s] for s in own]
    units.append({"id": uid, "role": role, "cause": cause, "cause_key": key, "carrier": carrier,
                  "habit": {"service": habit[0], "action": habit[1]},
                  "decider": {"service": dec[0], "record_id": dec[1], "container": dec[2], "injected": dec[3]},
                  "find_rate": rate, "find_rate_basis": basis_txt, "mechanism": mech,
                  "rows": [{"id": r, "weight": weight[r]} for r in rows]})
units.append({"id": "R1", "role": "realism", "cause": "judgement and visible work: the three start dates, the tray proposal, the March format rule, the zombie pack sent twice, the reference level's three items",
              "carrier": "same_container_supersession", "mechanism": "none"})
budget = {"schema": "difficulty-budget-v1", "design_id": "D3", "revision": "D3-design", "mode": "hard", "weight_basis": basis,
          "total_weight": total, "undesigned_loss": [0.02, 0.05], "units": units}
(WF / "01_Difficulty_Budget.json").write_text(json.dumps(budget, indent=1) + "\n")
print("basis", basis, "total", total)
for u in units:
    if u["role"] != "realism":
        w = sum(r["weight"] for r in u["rows"]); print(f"  {u['id']} {u['mechanism']:8} rows {len(u['rows']):3} weight {w:4} share {w/total:.3f}")
