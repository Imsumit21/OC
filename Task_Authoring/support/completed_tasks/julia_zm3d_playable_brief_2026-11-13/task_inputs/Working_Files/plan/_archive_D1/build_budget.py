#!/usr/bin/env python3
"""Build Working_Files/01_Difficulty_Budget.json (scenario S5c). Basis: the rubric skeleton when it exists, else the surface."""
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
    ("A1", "anchor", "EXPORT", "twelve lines exported in one go are empty shells", "export_tool", "de_named_root_record", ("slack", "read_channel"),
     ("slack", S["a1_post"]["id"], f"slack:{M.BUGS_CH}", True), [0.05, 0.20],
     "carrier_find_rates.json de_named_root_record 4/21 (0.19): a root post in #zombie-bugs that names no object, no ticket and none of the ask's words", 12),
    ("A2", "anchor", "ARTHOLD", "art sign-off withdrawn for one set by the artist", "art_signoff", "dm_with_non_owner", ("slack", "read_dm"),
     ("slack", S["a2_dm"]["id"], f"slack:{M.DM_CLAIRE}", True), [0.05, 0.20],
     "carrier_find_rates.json dm_with_non_owner 6/46 (0.13): a DM from the artist, who owns neither the list nor the notes", 12),
    ("C1", "variance", "REVISED", "art changed the day after the files went out (base)", "", "outside_obvious_filter", ("github", "get_pull_request_files"),
     ("github", M.BASE["pr462"], "github:match3d#462", False), [0.35, 0.60],
     "carrier_find_rates.json outside_obvious_filter 12/21 (0.57), lowered because the pull request's body is empty; the same change is also in a base #zombie-art thread", 5),
    ("C2", "variance", "AUDIO", "which sound cues are ours is in a sheet nothing links", "", "second_carrier_by_rule_owner", ("gsheets", "values_get"),
     ("gsheets", S["c2_sheet"]["id"], f"file:{S['c2_sheet']['id']}", True), [0.35, 0.65],
     "carrier_find_rates.json second_carrier_by_rule_owner 3/6 (0.50), one unit: a second record by the person who keeps the cues", 2),
    ("C3", "variance", "PICKS", "Robert's later reply under another post changes one pick and adds six lines", "", "reply_under_unrelated_parent", ("slack", "read_thread"),
     ("slack", S["c3_reply"]["id"], f"slack:{M.BASE['art_bow_root']}", True), [0.40, 0.65],
     "carrier_find_rates.json reply_under_unrelated_parent 16/26 when the reply names the item (it names the iron and the bow)", 6),
    ("C4", "variance", "PARENT", "the export failure of one set is noted on the pack ticket itself", "", "reply_under_related_root", ("linear", "list_comments"),
     ("linear", S["c4_comment"]["id"], "linear:ART-793", True), [0.35, 0.60],
     "linear/list_comments habit 13/41 (0.32) and Calvin's task (notes on a ticket outside the per-line reads missed by 5 of 6); raised because the pack ticket is the hub of the set", 8),
]
slots = surface["slots"]
if basis == "skeleton":
    sk = json.loads(skel_path.read_text())
    rows_all = sk["rows"]
    weight = {r["id"]: r["weight"] for r in rows_all}
    by_mech = lambda m: [r["id"] for r in rows_all if r.get("mechanisms") == [m]]
    comment_rows = [r["id"] for r in rows_all if str(r.get("write_target", "")).startswith("linear_create_comment#")]
    create_rows = [r["id"] for r in rows_all if str(r.get("write_target", "")).startswith("linear_create_issue#")]
else:
    weight = {s["id"]: s["weight"] for s in slots}
    by_mech = lambda m: [s["id"] for s in slots if s["mechanisms"] == [m]]
    comment_rows, create_rows = [], []
total = sum(weight.values())
units, used = [], 0
for uid, role, mech, cause, key, carrier, habit, dec, rate, basis_txt, n in UNITS:
    rows = list(by_mech(mech))
    if basis == "skeleton":
        if mech == "PICKS":
            rows += create_rows                      # the four added tickets not named by a slot
        else:
            rows += comment_rows[used:used + n]      # one comment row per Owed ticket this record decides
            used += n
    units.append({"id": uid, "role": role, "cause": cause, "cause_key": key, "carrier": carrier,
                  "habit": {"service": habit[0], "action": habit[1]},
                  "decider": {"service": dec[0], "record_id": dec[1], "container": dec[2], "injected": dec[3]},
                  "find_rate": rate, "find_rate_basis": basis_txt, "mechanism": mech,
                  "rows": [{"id": r, "weight": weight[r]} for r in rows]})
units.append({"id": "R1", "role": "realism", "cause": "judgement and visible work: the three start dates, the tray proposal, the March format rule, the zombie pack sent twice",
              "carrier": "same_container_supersession", "mechanism": "none"})
budget = {"schema": "difficulty-budget-v1", "design_id": "D1", "revision": "D1-design", "mode": "hard", "weight_basis": basis,
          "total_weight": total, "undesigned_loss": [0.02, 0.05], "units": units}
(WF / "01_Difficulty_Budget.json").write_text(json.dumps(budget, indent=1) + "\n")
print("basis", basis, "total", total)
for u in units:
    if u["role"] != "realism":
        w = sum(r["weight"] for r in u["rows"]); print(f"  {u['id']} {u['mechanism']:8} rows {len(u['rows']):3} weight {w:4} share {w/total:.3f}")
