#!/usr/bin/env python3
"""Writes sketch_manifest.json and sketch_surface.json for the pre-scenario checks only.
Not the /create-scenario manifest or surface. NEW- ids are planned seeds; every other id is a real normal-universe
record. Wording describes design intent; it is not prompt, Oracle Event or criterion text."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
CANVAS = "CE156FDFB428"; BUGS = "C05V5FNLB9V"; BUILDS = "C05433XK267"; DM = "D05S1S2AB5M"; VDM = "D06ULGYJHJS"
def v(service, rid, container, seeded, at):
    return {"service": service, "id": rid, "container": container, "seeded": seeded, "at": at}
man = {
 "_note": "PRE-SCENARIO SKETCH for hardness_v2_check.py only (recommended storyline A: Domino Delights bug carry-over into Linear). NEW- ids are planned seeds with declared containers; all others are real records. Design intent, not prompt, Oracle Event or criterion text.",
 "effective_profile": "extreme", "horizon": "Long Horizon",
 "anchors": [
  {"id": "AN1", "locator": f"slack:{DM}/NEW-arthur-carry-over-dm", "prompt_reference": "Arthur's DM from Thursday"},
  {"id": "AN2", "locator": "linear:ENG-2401", "prompt_reference": "the UI Changes master ticket"},
 ],
 "ask_fragments": [
  {"id": "F1", "seeded_ids": ["NEW-arthur-carry-over-dm"], "delegated_by_record": "NEW-arthur-carry-over-dm", "requirement_ids": ["R1","R2","R3","R5","R7","R8"]},
  {"id": "F2", "seeded_ids": ["NEW-carry-over-rule-doc"], "delegated_by_record": "NEW-arthur-carry-over-dm", "requirement_ids": ["R2","R3","R4","R5"]},
  {"id": "F3", "seeded_ids": ["NEW-note-rule-trello-comment"], "delegated_by_record": "NEW-arthur-carry-over-dm", "requirement_ids": ["R6"]},
 ],
 "traps": [
  {"id": "T_GONE", "family": "house_rule", "mechanism": "A15", "services": ["slack","gdocs","github"], "requirement": "R2",
   "expected_wrong_reading": "the unticked lives lines are still broken, so each gets a ticket or goes on an open lives ticket",
   "resolver": "the economy change replaced lives with tickets and every Android submission since December is cut from the line that carries it, so a bug in the lives counter no longer exists for players",
   "version_records": [v("slack","1763548856.943389",f"slack:{CANVAS}/1763548856.943389",False,"2025-11-19T10:40:56Z"),
                       v("gdocs","f_948768f5a462e7037d17c9","file:f_948768f5a462e7037d17c9",False,"2025-12-12T21:47:11Z")]},
  {"id": "T_LINE", "family": "done_gap", "mechanism": "A24", "services": ["slack","github"], "requirement": "R2",
   "expected_wrong_reading": "the tile dozer window bug is fixed: Marcus said he fixed it and did a PR",
   "resolver": "GameOfDominoes#1913 is still open and was never merged, so no build has it"},
  {"id": "T_BACK", "family": "superseding", "mechanism": "A11", "services": ["slack"], "requirement": "R2",
   "expected_wrong_reading": "a ticked canvas line is fixed",
   "resolver": "Vincent's later 1:1 note to Owen, worded by the screen's nickname, says that line came back on the Android build",
   "version_records": [v("slack","NEW-ticked-line-root",f"slack:{CANVAS}/NEW-ticked-line-root",False,"2025-11-19T10:44:00Z"),
                       v("slack","NEW-vincent-last-note",f"slack:{VDM}/NEW-vincent-last-note",True,"2025-11-22T16:00:00Z")]},
  {"id": "T_ELSE", "family": "completion_elsewhere", "mechanism": "A25", "services": ["slack","github"], "requirement": "R2",
   "expected_wrong_reading": "the flickering thread ends with testing a fix now, so it is still open and needs a ticket",
   "resolver": "the #builds change list shows the EndLevelPopup flickering fix in a submission build",
   "version_records": [v("slack","1764659550.713509",f"slack:{BUGS}/1764659550.713509",False,"2025-12-02T17:15:00Z"),
                       v("slack","1764977839.069349",f"slack:{BUILDS}/1764977839.069349",False,"2025-12-05T23:37:19Z")]},
  {"id": "T_ALIAS", "family": "scope_alias", "mechanism": "A7", "services": ["slack","linear"], "requirement": "R3",
   "expected_wrong_reading": "no ticket carries the canvas wording, so a new one is needed",
   "resolver": "an existing open ticket under other words covers the line, tied by a dated note on that ticket"},
  {"id": "T_FILT", "family": "exact_predicate", "mechanism": "A17", "services": ["slack","linear"], "requirement": "R1",
   "expected_wrong_reading": "the canvas is the whole list",
   "resolver": "Arthur's scope brings in bugs raised after the canvas stopped, such as the mega tile bug Owen himself confirmed"},
  {"id": "T_FOLLOW", "family": "house_rule", "mechanism": "A15", "services": ["trello","linear"], "requirement": "R6",
   "expected_wrong_reading": "setting the state is all a moved ticket needs",
   "resolver": "a standing rule in a card comment says every ticket moved to Done needs a note naming the build"},
  {"id": "T_TREE", "family": "done_gap", "mechanism": "A24", "services": ["gslides","linear","github"], "requirement": "R5",
   "expected_wrong_reading": "the sprint wrap deck says the UI work is finished and the child sits in Validation, so it is Done",
   "resolver": "for a child picked after the census, no merged work carries that screen; seven open children have no linked PR, and Season Pass is not proven (a Season Pass text fix is in #builds)",
   "version_records": [v("gslides","NEW-sprint-wrap-deck","file:NEW-sprint-wrap-deck",True,"2025-11-24T18:00:00Z"),
                       v("github","harmonygames-Games/GameOfDominoes#1907","github:harmonygames-Games/GameOfDominoes#1907",False,"2025-11-19T00:00:00Z")]},
 ],
 "mechanism_portfolio": [
  {"id": "GONE", "mechanism": "A15", "nodes": ["T_GONE"], "requirement": "R2", "natural_reading": "an unticked line is still broken"},
  {"id": "LINE", "mechanism": "A24", "nodes": ["T_LINE"], "requirement": "R2", "natural_reading": "fixed and did a PR means it shipped"},
  {"id": "BACK", "mechanism": "A11", "nodes": ["T_BACK"], "requirement": "R2", "natural_reading": "a tick means fixed"},
  {"id": "ELSE", "mechanism": "A25", "nodes": ["T_ELSE"], "requirement": "R2", "natural_reading": "a thread left open is still open"},
  {"id": "ALIAS", "mechanism": "A7", "nodes": ["T_ALIAS"], "requirement": "R3", "natural_reading": "no matching title means a new ticket"},
  {"id": "FILT", "mechanism": "A17", "nodes": ["T_FILT"], "requirement": "R1", "natural_reading": "the canvas is the list"},
  {"id": "FOLLOW", "mechanism": "A15", "nodes": ["T_FOLLOW"], "requirement": "R6", "natural_reading": "the state change is enough"},
  {"id": "TREE", "mechanism": "A24", "nodes": ["T_TREE"], "requirement": "R5", "natural_reading": "Validation plus the wrap deck means done"},
 ],
}
S = lambda i, w, c, m, n: {"id": i, "weight": w, "class": c, "mechanisms": m, "note": n}
slots = [
 S("V1_new_ticket_count",5,"aggregate",["GONE","LINE","BACK","ELSE","ALIAS","FILT"],"new tickets filed (rule x canvas x builds x tickets)"),
 S("V2_still_broken_count",5,"aggregate",["GONE","LINE","BACK","ELSE","FILT"],"bugs still broken for players"),
 S("V3_tree_done_count",5,"aggregate",["LINE","TREE"],"tree children that end Done"),
 S("G1_lives_loss_line",5,"direct",["GONE"],"call on the lives-after-a-loss line"),
 S("G2_lives_twice_line",5,"direct",["GONE"],"call on the losing-twice line"),
 S("G3_gone_reason",3,"write_content",["GONE"],"reason names the ticket economy"),
 S("L1_window_carried",5,"write_content",["LINE"],"tile dozer window carried as still broken"),
 S("L2_window_points_to_open_pr",3,"write_content",["LINE"],"ticket names the unmerged PR"),
 S("B1_ticked_line_carried",5,"direct",["BACK"],"ticked line carried after the later note"),
 S("B2_ticked_line_master",3,"write_content",["BACK"],"its ticket sits under the right master"),
 S("E1_flicker_closed",5,"direct",["ELSE"],"flicker closed, no ticket"),
 S("E2_flicker_cites_fix",3,"write_content",["ELSE"],"row cites the build change"),
 S("A1_apple_signin_reused",5,"write_content",["ALIAS"],"reuses the existing sign-in ticket"),
 S("A2_android_signin_reused",5,"write_content",["ALIAS"],"reuses the existing splash ticket"),
 S("F1_mega_tile_row",5,"direct",["FILT"],"mega tile bug present"),
 S("F2_bottom_bar_row",3,"direct",["FILT"],"Android bottom bar bug present"),
 S("O1_moved_tickets_noted",5,"aggregate",["FOLLOW"],"moved tickets carry the note"),
 S("O2_sample_note",3,"write_content",["FOLLOW"],"sample note names the build"),
 S("T1_unmerged_child_stays",5,"direct",["TREE"],"child with no merged work stays open (member chosen after census)"),
 S("T2_second_child_stays",3,"direct",["TREE"],"second child stays open"),
 S("K1_ticked_sample_1",3,"direct",[],"control: ticked line closed"),
 S("K2_ticked_sample_2",3,"direct",[],"control: ticked line closed"),
 S("K3_unticked_sample",3,"direct",[],"control: unticked line carried"),
 S("K4_new_ticket_team_label",3,"write_content",[],"new tickets sit on ENG with the bug label"),
 S("K5_master_sample_1",3,"write_content",[],"control: core screen under Core master"),
 S("K6_master_sample_2",3,"write_content",[],"control: event screen under Live-Ops master"),
 S("K7_child_done_1",3,"write_content",[],"control: merged child moved to Done"),
 S("K8_child_done_2",3,"write_content",[],"control: merged child moved to Done"),
 S("K9_child_done_3",3,"write_content",[],"control: merged child moved to Done"),
 S("K10_zm_canvas_out",3,"direct",[],"control: other game's canvas left out"),
 S("K11_sheet_row_volume",3,"aggregate",[],"sheet carries every bug in scope"),
 S("K12_sheet_in_drive",1,"delivery",[],"sheet in Owen's Drive"),
 S("K13_sheet_shared",1,"delivery",[],"shared with the Monday invite"),
 S("K14_reply_in_dm",1,"delivery",[],"reply in Arthur's DM"),
]
json.dump(man, open(os.path.join(HERE,"sketch_manifest.json"),"w"), indent=1)
json.dump({"_note":"PRE-SCENARIO SKETCH surface for hardness_v2_check.py and policy_model.py; not 01_Gradable_Surface.json. Fact slots only, no criterion text. Weights follow kind of work: 1 lookup, 3 interpretation or limited reconciliation, 5 multi-source reconciliation.","slots":slots}, open(os.path.join(HERE,"sketch_surface.json"),"w"), indent=1)
print(len(slots), sum(s["weight"] for s in slots), sum(s["weight"] for s in slots if s["mechanisms"]))
