#!/usr/bin/env python3
"""Pre-scenario SKETCH builder (storyline A: ZM3D playable content brief, Julia Lawson).

Writes sketch_surface.json, sketch_budget.json and the copies difficulty_budget.py needs under
sketch_budget_basis/. These are NOT 01_Gradable_Surface.json / 01_Difficulty_Budget.json: /create-scenario
re-derives both from real records. Member ids (B1.., F1..) are placeholders for cohort members, not record ids.
Row shape follows the rubric the portal accepts: at most five control samples per group plus volume rows, and a
direct row per member that a deciding record singles out (learnings 75, 77, 81).
"""
import json, shutil
from pathlib import Path
HERE = Path(__file__).resolve().parent
slots = []
def add(sid, weight, cls, role, mechs, note):
    slots.append({"id": sid, "weight": weight, "class": cls, "role": role, "mechanisms": mechs, "note": note})

# ---- exception members (each singled out by its own deciding record) --------------------------------------------
for i in range(1, 11):   # BUILD: 10 shortlist items not in the beta build
    add(f"B{i}_call", 5, "direct", "exception", ["BUILD"], "pool call for an item the shortlist marks in build")
    add(f"B{i}_handoff", 5, "direct", "exception", ["BUILD"], "hand-off state for the same item")
for i in range(1, 11):   # ARTFIX: 10 items whose art sign-off was withdrawn elsewhere
    add(f"F{i}_call", 5, "direct", "exception", ["ARTFIX"], "pool call for an item whose art ticket reads final")
    add(f"F{i}_handoff", 5, "direct", "exception", ["ARTFIX"], "hand-off state for the same item")
for i in range(1, 8):    # ABIL: 7 items whose shipped effect differs from the ticket text
    add(f"Q{i}_pairing", 5, "direct", "exception", ["ABIL"], "item-versus-enemy effect in the reference level")
    add(f"Q{i}_line", 3, "direct", "exception", ["ABIL"], "design line (effect as shipped)")
for i in range(1, 9):    # ALIAS: 8 items the vendor names by its own labels
    add(f"N{i}_handoff", 5, "direct", "exception", ["ALIAS"], "hand-off state decided by the vendor's note")
    add(f"N{i}_ticket", 3, "write_content", "exception", ["ALIAS"], "owed-asset ticket exists / does not exist")
for i in range(1, 9):    # LATE: 8 in-scope items that are not on the shortlist tab
    add(f"L{i}_call", 5, "direct", "exception", ["LATE"], "pool call for an item outside the shortlist")
    add(f"L{i}_handoff", 5, "direct", "exception", ["LATE"], "hand-off state for the same item")
    add(f"L{i}_line", 3, "direct", "exception", ["LATE"], "design line")
add("S1_call", 5, "direct", "exception", ["SWAP"], "default-set call for the item swapped out")
add("S2_call", 5, "direct", "exception", ["SWAP"], "default-set call for the item swapped in")
add("S_reflevel", 5, "write_content", "core", ["SWAP"], "reference-level item list in the brief")
add("S_vendor_note", 3, "write_content", "core", ["SWAP"], "default set as stated to the vendor")
for i in range(1, 4):    # AUDIO: 3 sound cues that may not go to an outside vendor as they stand
    add(f"U{i}_call", 5, "direct", "exception", ["AUDIO"], "sound cue in or out of the pack")
    add(f"U{i}_handoff", 5, "direct", "exception", ["AUDIO"], "hand-off state for the same cue")
add("U_section", 5, "write_content", "core", ["AUDIO"], "sound section of the brief")
# ---- controls: at most five samples per group, plus volume rows --------------------------------------------------
for i in range(1, 6):
    add(f"C{i}_call", 5, "direct", "sample", [], "pool call, plain member")
    add(f"C{i}_handoff", 5, "direct", "sample", [], "hand-off state, plain member")
for i in range(1, 4):
    add(f"C{i}_line", 3, "direct", "sample", [], "design line, plain member")
for i in range(1, 4):
    add(f"UC{i}_call", 5, "direct", "sample", [], "non-item asset (UI, background, sound) in the pack, plain member")
    add(f"UC{i}_line", 3, "direct", "sample", [], "non-item asset line, plain member")
add("V_pool_count", 5, "aggregate", "volume", ["BUILD", "ARTFIX", "LATE"], "number of items in the editable pool")
add("V_owed_count", 5, "aggregate", "volume", ["ALIAS", "ARTFIX", "FMT"], "number of assets still owed")
add("V_sound_count", 3, "aggregate", "volume", ["AUDIO"], "number of sound cues in the pack")
# ---- core sections, writes, delivery -----------------------------------------------------------------------------
add("K_mechanic_limit", 5, "write_content", "core", ["FMT"], "extra-mechanic limit the vendor set, applied to the brief")
add("K_3d_format", 3, "write_content", "core", ["FMT"], "export format owed for 3D assets")
add("K_scenario", 3, "write_content", "core", [], "chosen scenario")
add("K_winfail", 3, "write_content", "core", [], "win and fail conditions")
add("K_editables", 3, "write_content", "core", [], "what the vendor makes editable")
add("K_start_date", 3, "write_content", "core", [], "vendor start date and hand-off date")
add("W_tickets_exact", 5, "write_content", "core", ["ALIAS", "ARTFIX"], "owed-asset tickets created for exactly the owed assets")
add("W_reply_counts", 3, "write_content", "core", [], "reply to the requester carries the counts")
add("W_vendor_msg", 3, "write_content", "core", [], "note to the vendor with link and outstanding list")
for sid, note in (("D_doc", "brief doc in the persona's Drive"), ("D_sheet", "hand-off sheet in the persona's Drive"),
                  ("D_reply", "reply in the requester's thread"), ("D_vendor", "post in the vendor channel"),
                  ("D_share", "brief shared with the people the ask names")):
    add(sid, 1, "delivery", "core", [], note)

surface = {"_note": "PRE-SCENARIO SKETCH surface (storyline A). Not 01_Gradable_Surface.json; member ids are placeholders.",
           "revision": "sketch0", "slots": slots}
total = sum(s["weight"] for s in slots)
def rows(mech, own_only=True):
    return [{"id": s["id"], "weight": s["weight"]} for s in slots
            if mech in s["mechanisms"] and (not own_only or s["mechanisms"] == [mech])]
def unit(uid, role, cause, key, carrier, svc, action, decider, rate, basis, mech):
    return {"id": uid, "role": role, "cause": cause, "cause_key": key, "carrier": carrier,
            "habit": {"service": svc, "action": action},
            "decider": {"service": decider[0], "record_id": decider[1], "container": decider[2], "injected": decider[3]},
            "find_rate": rate, "find_rate_basis": basis, "rows": rows(mech), "mechanism": mech}
units = [
    unit("A1", "anchor", "items the shortlist marks in build were taken out of the beta build", "build_content",
         "non_set_ticket", "linear", "list_comments", ("linear", "NEW-beta-memory-ticket-comment", "linear:NEW-beta-memory-ticket", True),
         [0.05, 0.20], "carrier_find_rates.json non_set_ticket 6/33 (0.18)", "BUILD"),
    unit("A2", "anchor", "art sign-off withdrawn for one item family by the art lead", "art_signoff",
         "dm_with_non_owner", "slack", "read_dm", ("slack", "NEW-art-lead-dm", "slack:NEW-dm-julia-claire", True),
         [0.05, 0.20], "carrier_find_rates.json dm_with_non_owner 6/46 (0.13)", "ARTFIX"),
    unit("C1", "variance", "shipped effect changed in a pull request review", "", "inline_pr_review_comment",
         "github", "get_pull_request_review_comments", ("github", "NEW-match3d-pr-review-comment", "github:match3d#NEW", True),
         [0.35, 0.60], "carrier_find_rates.json inline_pr_review_comment 21/51 (0.41); PR linked from one member only", "ABIL"),
    unit("C2", "variance", "vendor's acceptance note uses its own labels", "", "alias",
         "slack", "search", ("slack", "NEW-vendor-acceptance-note", "slack:C08H78VJG80/NEW-root", True),
         [0.40, 0.65], "carrier_find_rates.json alias 15/28 (0.54)", "ALIAS"),
    unit("C3", "variance", "default set changed in a reply under another post", "", "reply_under_unrelated_parent",
         "slack", "read_thread", ("slack", "NEW-art-channel-reply", "slack:C08R8CHB0QL/NEW-unrelated-root", True),
         [0.40, 0.65], "carrier_find_rates.json reply_under_unrelated_parent 16/26 when the reply names the item", "SWAP"),
    unit("C4", "variance", "in-scope items that are not on the shortlist tab", "", "outside_obvious_filter",
         "gsheets", "get_values", ("gsheets", "NEW-level-list-sheet", "file:NEW-level-list-sheet", True),
         [0.40, 0.65], "carrier_find_rates.json outside_obvious_filter 12/21 (0.57)", "LATE"),
    unit("C5", "variance", "sound-cue clearance posted in a channel nothing names", "", "root_post_in_unnamed_channel",
         "slack", "read_channel", ("slack", "NEW-zombie-sfx-root", "slack:C09A7PDFYCV/NEW-root", True),
         [0.40, 0.65], "carrier_find_rates.json root_post_in_unnamed_channel 8/13 (0.62)", "AUDIO"),
    {"id": "R1", "role": "realism", "cause": "vendor rules from the March 2025 round (base, same channel, older page)",
     "carrier": "unpointed_old_base_record", "mechanism": "FMT"},
]
budget = {"schema": "difficulty-budget-v1", "design_id": "SKETCH0", "revision": "sketch0", "mode": "hard",
          "weight_basis": "surface", "total_weight": total, "undesigned_loss": [0.02, 0.05], "units": units}
(HERE / "sketch_surface.json").write_text(json.dumps(surface, indent=1) + "\n")
(HERE / "sketch_budget.json").write_text(json.dumps(budget, indent=1) + "\n")
basis = HERE / "sketch_budget_basis"
(basis / "Working_Files").mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE.parent.parent / "00_Assigments.md", basis / "00_Assigments.md")
(basis / "Working_Files" / "01_Gradable_Surface.json").write_text(json.dumps(surface, indent=1) + "\n")
(basis / "Working_Files" / "01_Difficulty_Budget.json").write_text(json.dumps(budget, indent=1) + "\n")
(basis / "README.md").write_text("Sketch only. A copy of the assignment plus the sketch surface and budget, so that\n"
    "`difficulty_budget.py check --task-dir` can resolve its weight basis. Not a task folder; not read by any stage gate.\n")
share = lambda m: sum(r["weight"] for r in rows(m)) / total
print("slots", len(slots), "total weight", total)
for u in units:
    if u["role"] != "realism":
        print(f"  {u['id']} {u['mechanism']:7} rows {len(u['rows']):2}  own weight {sum(r['weight'] for r in u['rows']):3}  share {share(u['mechanism']):.3f}")
