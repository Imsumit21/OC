#!/usr/bin/env python3
"""Writes sketch_manifest.json and sketch_surface.json for the pre-scenario checks only.
Not the /create-scenario manifest or surface. NEW- ids are planned seeds; every other id is a real synth-cut record
read through tools/hg.py on 2026-11-10. Wording describes design intent; it is not prompt, Oracle Event or criterion text."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
BDM = "D0770ET6WBW"; VDM = "D06UPGF5PQV"; ODM = "D05S1S2H55M"; BUILDS = "C05433XK267"; BUGS = "C08R27X0EAH"
def v(service, rid, container, seeded, at):
    return {"service": service, "id": rid, "container": container, "seeded": seeded, "at": at}
man = {
 "_note": "PRE-SCENARIO SKETCH for hardness_v2_check.py only (recommended storyline A: Queue Manager roll-out stock-take, ZOM-543 turned into an epic). NEW- ids are planned seeds with declared containers; all others are real records.",
 "effective_profile": "extreme", "horizon": "Long Horizon",
 "anchors": [
  {"id": "AN1", "locator": f"slack:{BDM}/NEW-brian-epic-ask", "prompt_reference": "Brian's message from yesterday"},
  {"id": "AN2", "locator": "linear:ZOM-543", "prompt_reference": "the Queue Manager ticket"},
 ],
 "ask_fragments": [
  {"id": "F1", "seeded_ids": ["NEW-brian-epic-ask"], "delegated_by_record": "NEW-brian-epic-ask", "requirement_ids": ["R1","R2","R3","R4","R6","R7"]},
  {"id": "F2", "seeded_ids": ["NEW-brian-epic-note-on-ZOM-543"], "delegated_by_record": "NEW-brian-epic-ask", "requirement_ids": ["R2","R3","R5"]},
  {"id": "F3", "seeded_ids": ["NEW-arthur-main-build-rule"], "delegated_by_record": "NEW-brian-epic-note-on-ZOM-543", "requirement_ids": ["R2"]},
 ],
 "traps": [
  {"id": "T_BRANCH", "family": "done_gap", "mechanism": "A24", "services": ["slack","github"], "requirement": "R2",
   "expected_wrong_reading": "QA said it looks ok and Calvin said tested, so the tutorial chain, the coin animation and the boss arena tutorial are cleared",
   "resolver": "the build QA looked at (Match 3D iOS Internal #1718) was cut from the QueueManager branch, the #builds post says so, and main took later merges to the same flow; no QA word exists on a main build",
   "version_records": [v("slack","1758820544",f"slack:{VDM}/1758820544",False,"2025-09-25T17:15:44Z"),
                       v("slack","1758817549.builds-1718",f"slack:{BUILDS}/1758817549",False,"2025-09-25T16:25:49Z"),
                       v("github","harmonygames-Games/match3d#472","github:harmonygames-Games/match3d#472",False,"2025-09-30T15:53:04Z")]},
  {"id": "T_REOPEN", "family": "superseding", "mechanism": "A11", "services": ["slack"], "requirement": "R3",
   "expected_wrong_reading": "the daily gift ordering report was closed out in the QA chat",
   "resolver": "a later reply by Vincent under an unrelated #zombie-bugs post says the same thing happened again on a main build, worded by what the player sees",
   "version_records": [v("slack","NEW-vincent-gift-ok",f"slack:{VDM}/NEW-vincent-gift-ok",True,"2025-09-26T15:00:00Z"),
                       v("slack","NEW-vincent-gift-again",f"slack:{BUGS}/NEW-unrelated-root",True,"2025-09-29T18:00:00Z")]},
  {"id": "T_INLINE", "family": "done_gap", "mechanism": "A24", "services": ["github","linear"], "requirement": "R2",
   "expected_wrong_reading": "the PR merged and its summary lists the flow, so the flow is in the queue",
   "resolver": "an inline review comment by the human reviewer on that merged PR says one hook was left out of the merge on purpose; the review body is silent",
   "version_records": [v("github","harmonygames-Games/match3d#NEW-merged-pr","github:harmonygames-Games/match3d#NEW-merged-pr",True,"2025-09-26T20:00:00Z"),
                       v("github","NEW-inline-review-comment","github:harmonygames-Games/match3d#NEW-merged-pr/inline",True,"2025-09-26T21:00:00Z")]},
  {"id": "T_FILT_TICKET", "family": "exact_predicate", "mechanism": "A17", "services": ["slack","linear"], "requirement": "R3",
   "expected_wrong_reading": "the reports are the ones in the QA sheet, the QA chat and under the epic",
   "resolver": "Brian's scope brings in any report about what shows on the home screen after a level, whoever raised it; the VFX artist sent Calvin one directly, in their own 1:1 chat, and no ticket holds it"},
  {"id": "T_FILT_MAIL", "family": "exact_predicate", "mechanism": "A17", "services": ["gmail"], "requirement": "R3",
   "expected_wrong_reading": "every report is in Slack or Linear",
   "resolver": "one report reached Calvin only by mail and was never ticketed"},
  {"id": "T_ALIAS", "family": "scope_alias", "mechanism": "A7", "services": ["linear","slack"], "requirement": "R4",
   "expected_wrong_reading": "nothing under the epic covers this, so it needs a new sub-issue",
   "resolver": "an open ticket under the feature's other name already covers it; a dated message ties the two names"},
  {"id": "T_DONE_ELSEWHERE", "family": "completion_elsewhere", "mechanism": "A25", "services": ["slack","github"], "requirement": "R4",
   "expected_wrong_reading": "one live-op still has to be hooked into the queue, so it needs a sub-issue",
   "resolver": "the feature owner already hooked it in on his own branch and it merged; he told Calvin so in their own chat, in Spanish",
   "version_records": [v("slack","NEW-brian-still-to-hook",f"slack:{BDM}/NEW-brian-still-to-hook",True,"2025-09-26T16:00:00Z"),
                       v("slack","NEW-owner-hooked-it",f"slack:{ODM}/NEW-owner-hooked-it",True,"2025-09-29T22:00:00Z")]},
  {"id": "T_DATE", "family": "boundary_date", "mechanism": "A9", "services": ["gcal","slack"], "requirement": "R5",
   "expected_wrong_reading": "the publish day in the chat decides what has to land first",
   "resolver": "the publish review on the calendar was moved after that message; two items change sides",
   "version_records": [v("slack","NEW-brian-publish-day",f"slack:{BDM}/NEW-brian-publish-day",True,"2025-09-24T16:00:00Z"),
                       v("gcal","NEW-publish-review-moved","gcal:NEW-publish-review-moved",True,"2025-09-29T17:00:00Z")]},
  {"id": "T_FOLLOW", "family": "house_rule", "mechanism": "A15", "services": ["slack","linear"], "requirement": "R6",
   "expected_wrong_reading": "a new sub-issue only needs a title and the parent",
   "resolver": "Julia's standing note on Calvin's tickets (relayed to him on 2 Sep, slack:D05HYDTG5TJ/1756838837) plus Brian's note on the epic fix what each new ticket of his must carry"},
 ],
 "mechanism_portfolio": [
  {"id": "BRANCH", "mechanism": "A24", "nodes": ["T_BRANCH"], "requirement": "R2", "natural_reading": "QA said ok, so it is cleared"},
  {"id": "REOPEN", "mechanism": "A11", "nodes": ["T_REOPEN"], "requirement": "R3", "natural_reading": "closed in the QA chat means closed"},
  {"id": "INLINE", "mechanism": "A24", "nodes": ["T_INLINE"], "requirement": "R2", "natural_reading": "merged with the flow in the summary means it is in the queue"},
  {"id": "FILT", "mechanism": "A17", "nodes": ["T_FILT_TICKET"], "requirement": "R3", "natural_reading": "the reports are in the QA chat"},
  {"id": "MAIL", "mechanism": "A17", "nodes": ["T_FILT_MAIL"], "requirement": "R3", "natural_reading": "every report is in Slack or Linear"},
  {"id": "ALIAS", "mechanism": "A7", "nodes": ["T_ALIAS"], "requirement": "R4", "natural_reading": "no matching title means a new sub-issue"},
  {"id": "ELSE", "mechanism": "A25", "nodes": ["T_DONE_ELSEWHERE"], "requirement": "R4", "natural_reading": "Brian said it is still to hook, so it is open"},
  {"id": "DATE", "mechanism": "A9", "nodes": ["T_DATE"], "requirement": "R5", "natural_reading": "the day in the chat is the day"},
 ],
}
S = lambda i, w, c, m, n: {"id": i, "weight": w, "class": c, "mechanisms": m, "note": n}
slots = [
 # aggregates (each a number the reply and the doc carry)
 S("V1_flows_cleared_count",5,"aggregate",["BRANCH","REOPEN"],"flows QA has cleared on main"),
 S("V2_open_reports_count",5,"aggregate",["REOPEN","FILT","MAIL"],"reports still open"),
 S("V3_new_subissue_count",5,"aggregate",["ALIAS","ELSE","FILT","MAIL","INLINE"],"new sub-issues created under the epic"),
 # BRANCH: three different flows, one count of what must be re-checked
 S("B1_tutorial_chain_not_cleared",5,"direct",["BRANCH"],"back-to-back tutorials: not cleared on main"),
 S("B2_coin_animation_not_cleared",5,"direct",["BRANCH"],"level-end coin animation: not cleared on main"),
 S("B3_boss_arena_tutorial_not_cleared",5,"direct",["BRANCH"],"boss arena tutorial: not cleared on main"),
 S("B4_recheck_item_names_main_build",5,"write_content",["BRANCH"],"the re-check item points at a build cut from main"),
 S("B5_reply_says_recheck_needed",5,"write_content",["BRANCH"],"the reply to Brian says QA has to look again"),
 # REOPEN
 S("R1_gift_order_open",5,"direct",["REOPEN"],"daily gift ordering report is open"),
 S("R2_gift_order_subissue",5,"write_content",["REOPEN"],"a sub-issue carries it"),
 S("R3_gift_flow_status",3,"direct",["REOPEN"],"daily gift flow not cleared"),
 # INLINE
 S("I1_flow_partly_in_queue",5,"direct",["INLINE"],"the flow is only partly in the queue"),
 S("I2_missing_hook_subissue",5,"write_content",["INLINE"],"a sub-issue for the hook left out"),
 S("I3_names_missing_hook",3,"write_content",["INLINE"],"it names the hook"),
 S("I4_flow_child_left_open",5,"write_content",["INLINE"],"that flow's child issue is left open, not Done"),
 # FILT (ticket outside the filter)
 S("F1_artist_report_in_list",5,"direct",["FILT"],"the report the VFX artist sent Calvin directly is in the list"),
 S("F2_artist_report_subissue",5,"write_content",["FILT"],"a sub-issue carries it"),
 S("F3_artist_report_flow",5,"direct",["FILT"],"the flow it hits is not cleared"),
 # MAIL
 S("M1_mail_report_in_list",5,"direct",["MAIL"],"the mailed report is in the list"),
 S("M2_mail_report_subissue",5,"write_content",["MAIL"],"a sub-issue carries it"),
 S("M3_mail_report_flow",5,"direct",["MAIL"],"the flow it hits is not cleared"),
 # ALIAS
 S("A1_existing_ticket_a_reused",5,"write_content",["ALIAS"],"first existing ticket moved under the epic, not duplicated"),
 S("A2_existing_ticket_b_reused",5,"write_content",["ALIAS"],"second existing ticket moved under the epic, not duplicated"),
 # ELSE
 S("E1_liveop_already_in_queue",5,"direct",["ELSE"],"that live-op is already in the queue"),
 S("E2_names_the_merge",5,"direct",["ELSE"],"the doc names the merge that did it (chat plus GitHub)"),
 S("E4_flow_child_done",5,"write_content",["ELSE"],"that live-op's child issue is Done"),
 S("E3_left_to_hook_count",5,"aggregate",["ELSE","INLINE"],"live-ops still to hook into the queue"),
 # DATE
 S("D1_item_x_before_publish",5,"direct",["DATE"],"item X falls before the publish review"),
 S("D2_item_y_after_publish",5,"direct",["DATE"],"item Y falls after it"),
 S("D3_publish_day_in_reply",3,"write_content",["DATE"],"the reply gives the moved day"),
 # controls (no mechanism): sampled, never per-target
 S("K1_flow_clean_1",3,"direct",[],"control flow status"),
 S("K2_flow_clean_2",3,"direct",[],"control flow status"),
 S("K3_flow_clean_3",3,"direct",[],"control flow status"),
 S("K4_flow_not_in_queue_1",3,"direct",[],"control: flow not in the queue yet"),
 S("K6_report_clean_1",3,"direct",[],"control report status"),
 S("K7_report_clean_2",3,"direct",[],"control report status"),
 S("K9_subissue_plain_1",3,"write_content",[],"control sub-issue"),
 S("K10_subissue_plain_2",3,"write_content",[],"control sub-issue"),
 S("K11_merge_fact_1",1,"direct",[],"control: merge that put a flow in the queue"),
 S("K12_merge_fact_2",1,"direct",[],"control: merge that put a flow in the queue"),
 S("K13_subissue_team_parent",1,"write_content",[],"sub-issues sit on ZOM under the epic"),
 S("K14_doc_volume",3,"aggregate",[],"the doc covers every flow"),
 S("K19_report_note_volume",3,"aggregate",[],"every report has its line in Linear"),
 S("K20_report_note_sample",1,"write_content",[],"sample report line"),
 S("K15_doc_in_drive",1,"delivery",[],"doc in Calvin's Drive"),
 S("K16_reply_in_dm",1,"delivery",[],"reply in Brian's DM"),
 S("K17_order_subissues",1,"delivery",[],"Process: reply after the sub-issues"),
 S("K18_order_doc",1,"delivery",[],"Process: reply after the doc"),
]
json.dump(man, open(os.path.join(HERE,"sketch_manifest.json"),"w"), indent=1)
json.dump({"_note":"PRE-SCENARIO SKETCH surface for hardness_v2_check.py and policy_model.py; not 01_Gradable_Surface.json. Fact slots only, no criterion text. Weights follow kind of work: 1 lookup, 3 interpretation or limited reconciliation, 5 multi-source reconciliation.","slots":slots}, open(os.path.join(HERE,"sketch_surface.json"),"w"), indent=1)
tot=sum(s["weight"] for s in slots); fl=sum(s["weight"] for s in slots if s["mechanisms"])
print(len(slots), tot, fl, f"{fl/tot:.1%}")
import collections
c=collections.Counter()
for s in slots:
    for m in s["mechanisms"]: c[m]+=s["weight"]
print({k: f"{x} ({x/tot:.0%})" for k,x in c.items()})
