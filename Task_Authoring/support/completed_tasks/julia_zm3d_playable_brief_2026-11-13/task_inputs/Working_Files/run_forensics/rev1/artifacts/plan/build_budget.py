#!/usr/bin/env python3
"""Build Working_Files/01_Difficulty_Budget.json (scenario S5c, design D2). Basis: the rubric skeleton when asked, else the surface.
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
UNITS = [
    ("A1", "anchor", "EXPORT", "twelve lines saved out of the Unity project are in a format the vendor refuses", "export_format", "de_named_root_record", ("slack", "read_channel"),
     ("slack", S["a1_post"]["id"], f"slack:{M.MATCH3D_CH}", True), [0.05, 0.20],
     "carrier_find_rates.json de_named_root_record 4/21 (0.19): a root post in #zombie-match3d that names no line, no ticket and none of the ask's words", ["A1", "W1"]),
    ("A2", "anchor", "ARTHOLD", "the artist is redoing one category's art and says so only to Julia", "art_in_progress", "dm_with_non_owner", ("slack", "read_dm"),
     ("slack", S["a2_dm"]["id"], f"slack:{M.DM_CLAIRE}", True), [0.05, 0.20],
     "carrier_find_rates.json dm_with_non_owner 6/46 (0.13): a DM from the artist, who owns neither the list nor the notes; here also in Turkish", ["A2", "W2"]),
    ("C1", "variance", "REVISED", "three models changed later on the day their files were handed over (base)", "", "outside_obvious_filter", ("github", "get_pull_request_comments"),
     ("github", M.BASE["pr462"], "github:match3d#462", False), [0.35, 0.60],
     "carrier_find_rates.json outside_obvious_filter 12/21 (0.57): the pull request's body is empty and its comment names the models; the same change is in a base #zombie-art thread", []),
    ("C2", "variance", "AUDIO", "which sound cues are ours to pass on is in a sheet nothing links", "", "second_carrier_by_rule_owner", ("gsheets", "values_get"),
     ("gsheets", S["c2_sheet"]["id"], f"file:{S['c2_sheet']['id']}", True), [0.35, 0.65],
     "carrier_find_rates.json second_carrier_by_rule_owner 3/6 (0.50), one unit: a second record by the person who keeps the cues", []),
    ("C3", "variance", "PICKS", "Robert's later reply under another post changes one pick, naming no item", "", "reply_under_unrelated_parent", ("slack", "read_thread"),
     ("slack", S["c3_reply"]["id"], f"slack:{M.BASE['art_bow_root']}", True), [0.40, 0.65],
     "carrier_find_rates.json reply_under_unrelated_parent 15/30 (0.50); the reply names no item, so only opening Julia's bow thread returns it", []),
    ("C4", "variance", "ZIP", "one zip of eight files will not unpack, noted in the packer's own log of the folder", "", "second_carrier_by_rule_owner", ("gdocs", "get_document_text"),
     ("gdocs", S["c4_log"]["id"], f"file:{S['c4_log']['id']}", True), [0.35, 0.65],
     "carrier_find_rates.json second_carrier_by_rule_owner 3/6 (0.50): a second record by the owner of the pack list, found by looking for the outgoing folder the notes speak of", []),
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
budget = {"schema": "difficulty-budget-v1", "design_id": "D2", "revision": "D2-design", "mode": "hard", "weight_basis": basis,
          "total_weight": total, "undesigned_loss": [0.02, 0.05], "units": units}
(WF / "01_Difficulty_Budget.json").write_text(json.dumps(budget, indent=1) + "\n")
print("basis", basis, "total", total)
for u in units:
    if u["role"] != "realism":
        w = sum(r["weight"] for r in u["rows"]); print(f"  {u['id']} {u['mechanism']:8} rows {len(u['rows']):3} weight {w:4} share {w/total:.3f}")
