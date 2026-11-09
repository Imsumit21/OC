#!/usr/bin/env python3
"""Writes the PRE-SCENARIO sketch manifest and surface for storyline A (Domino Delights publishing-rights model).
Not the /create-scenario draft manifest or 01_Gradable_Surface.json. Ids prefixed NEW- are planned seeds, not yet checked
against the whole universe. Member labels PA..PI stand for publishers to be minted at /create-scenario.
Fact slots only: no prompt, Oracle Event or criterion text."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
MAIL = "gmail:NEW-pub-%s-terms-thread"
traps = [
 dict(id="T_DONE", family="done_gap", mechanism="A24", services=["gmail", "trello", "slack"], requirement="R3",
      expected_wrong_reading="the first advance tranche from PA is earned: PA's partner manager mails that the KPI test cleared and the BD Follow Up card says test passed, so it counts as Q4 cash",
      resolver="the term mail ties that tranche to installs from non-incent traffic; a later #analytics reply by the person who ran the test shows the window was filled from the incent campaign, so one required part never happened",
      version_records=[dict(service="gmail", id="NEW-pub-PA-kpi-cleared", container="gmail:NEW-pub-PA-terms-thread", seeded=True, at="2025-09-26T16:00:00Z"),
                       dict(service="slack", id="NEW-analytics-test-source-reply", container="slack:C069FF9Q57S/NEW-unrelated-analytics-root", seeded=True, at="2025-09-29T18:00:00Z")]),
 dict(id="T_CORR", family="superseding", mechanism="A11", services=["gmail", "gcal"], requirement="R2",
      expected_wrong_reading="PB's advance is the figure in PB's term mail",
      resolver="Leonard's note on the calendar entry for the follow-up call, dated after the mail, records the lower figure PB came back with and says the rest stands",
      version_records=[dict(service="gmail", id="NEW-pub-PB-terms", container="gmail:NEW-pub-PB-terms-thread", seeded=True, at="2025-09-22T15:00:00Z"),
                       dict(service="gcal", id="NEW-pub-PB-followup-event", container="gcal:NEW-pub-PB-followup-event", seeded=True, at="2025-09-29T20:00:00Z")]),
 dict(id="T_ALIAS", family="alias", mechanism="A7", services=["gmail", "contacts", "slack"], requirement="R1",
      expected_wrong_reading="PC's offer is live: its term mail is unanswered and no Slack hit carries PC's trading name",
      resolver="a founder's post says the parent group's person pulled out, naming her and the group; her signature on PC's mail and a Contacts row tie that person and group to PC",
      version_records=[dict(service="gmail", id="NEW-pub-PC-terms", container="gmail:NEW-pub-PC-terms-thread", seeded=True, at="2025-09-18T15:00:00Z"),
                       dict(service="slack", id="NEW-founder-post-parent-group-out", container="slack:C07C2866011/NEW-group-out-root", seeded=True, at="2025-09-28T17:00:00Z")]),
 dict(id="T_FILT1", family="exact_predicate", mechanism="A17", services=["gmail", "slack"], requirement="R1",
      expected_wrong_reading="the population is the outreach tab plus Frederick's own inbox",
      resolver="the rule record brings in any publisher that came to the company about Domino Delights; PH came to Robert and his relay sits in a founders' thread",
      version_records=[]),
 dict(id="T_FILT2", family="exact_predicate", mechanism="A17", services=["linear", "gsheets"], requirement="R1",
      expected_wrong_reading="the population is the outreach tab plus Frederick's own inbox",
      resolver="PI's terms reached Arthur during an SDK question and are recorded in a comment on a Linear ticket about Domino Delights ads",
      version_records=[]),
 dict(id="T_EXC", family="house_rule", mechanism="A15", services=["gdocs", "slack", "gmail"], requirement="R4",
      expected_wrong_reading="PD is the best deal: it has the largest 12-month value and a clean mobile rev share",
      resolver="the founders' Aug 2025 position keeps code, IP and non-mobile distribution rights (base, exec sync and #executives); PD's grant is worded across all digital storefronts, so it fails",
      version_records=[]),
 dict(id="T_INPUT", family="superseding", mechanism="A11", services=["gmail", "trello"], requirement="R5",
      expected_wrong_reading="PE's monthly install commitment is the figure in PE's term mail, and the forecast multiplies that",
      resolver="a later comment on PE's BD Follow Up card gives the lower commitment PE confirmed by phone and says the rest stands",
      version_records=[dict(service="gmail", id="NEW-pub-PE-terms", container="gmail:NEW-pub-PE-terms-thread", seeded=True, at="2025-09-19T15:00:00Z"),
                       dict(service="trello", id="NEW-pub-PE-card-comment", container="trello:NEW-pub-PE-card", seeded=True, at="2025-09-30T16:00:00Z")]),
 dict(id="T_FOLLOW", family="follow_through", mechanism="A15", services=["slack", "gmail", "gsheets"], requirement="R6",
      expected_wrong_reading="a model and a reply finish the job; nothing is owed to publishers who were sent the paid-traffic numbers",
      resolver="Leonard's standing line, in a reply under a root about deck numbers, says anyone quoted paid-traffic numbers gets the organic figures before their terms are relied on; the outreach log shows who",
      version_records=[]),
]
mech = [
 dict(id="DONE", mechanism="A24", nodes=["T_DONE"], requirement="R3", natural_reading="the partner's own 'cleared' mail means the tranche is earned"),
 dict(id="CORR", mechanism="A11", nodes=["T_CORR"], requirement="R2", natural_reading="the term mail holds the current advance"),
 dict(id="ALIAS", mechanism="A7", nodes=["T_ALIAS"], requirement="R1", natural_reading="no hit under the trading name means the offer stands"),
 dict(id="FILT1", mechanism="A17", nodes=["T_FILT1"], requirement="R1", natural_reading="the tab and my inbox are the population"),
 dict(id="FILT2", mechanism="A17", nodes=["T_FILT2"], requirement="R7", natural_reading="deal terms do not live on engineering tickets"),
 dict(id="EXC", mechanism="A15", nodes=["T_EXC"], requirement="R4", natural_reading="the highest value wins"),
 dict(id="INPUT", mechanism="A11", nodes=["T_INPUT"], requirement="R5", natural_reading="the term mail's commitment feeds the forecast"),
 dict(id="FOLLOW", mechanism="A15", nodes=["T_FOLLOW"], requirement="R6", natural_reading="the model and the reply are all that is asked"),
]
manifest = dict(
 _note="PRE-SCENARIO SKETCH for hardness_v2_check.py only (recommended storyline A: Domino Delights publishing-rights model). Not the /create-scenario draft manifest. Ids prefixed NEW- are planned seeds with declared containers; other ids are real synth-cut records Frederick can open (cansee_anchors.txt). Trap wording describes design intent, not prompt, Oracle Event or criterion text.",
 effective_profile="extreme", horizon="Long Horizon",
 anchors=[dict(id="AN1", locator="gmail:NEW-leonard-dd-model-mail", prompt_reference="Leonard's email from yesterday"),
          dict(id="AN2", locator="gsheets:NEW-outreach-log", prompt_reference="my publisher outreach sheet"),
          dict(id="AN3", locator="trello:670015c2ecd45b634d5eec81", prompt_reference="the BD Follow Up list")],
 ask_fragments=[dict(id="F1", seeded_ids=["NEW-leonard-dd-model-mail"], delegated_by_record="NEW-leonard-dd-model-mail", requirement_ids=["R1", "R2", "R3", "R4", "R5"]),
                dict(id="F2", seeded_ids=["NEW-model-ground-rules-doc"], delegated_by_record="NEW-leonard-dd-model-mail", requirement_ids=["R2", "R3", "R5", "R7"]),
                dict(id="F3", seeded_ids=["NEW-deck-numbers-reply"], delegated_by_record="NEW-model-ground-rules-doc", requirement_ids=["R6"])],
 traps=traps, mechanism_portfolio=mech)
json.dump(manifest, open(os.path.join(HERE, "sketch_manifest.json"), "w"), indent=1)

S = []
def slot(id, w, cls, mechs, note): S.append(dict(id=id, weight=w, **{"class": cls}, mechanisms=mechs, note=note))
# v2 lean surface, shaped like the two completed tasks that cleared SD (bridge 40 rows, handover 37 rows):
# sheet groups sampled, exact counts, template-identical high-count writes sampled, a reply that holds counts and a pick, not lists.
slot("K_home", 1, "delivery", [], "model in his folder")
slot("K_native", 1, "delivery", [], "native Google Sheet")
# population
slot("S_total", 5, "aggregate", ["FILT1","FILT2"], "exact publishers on the model")
slot("S_in_PH", 5, "direct", ["FILT1"], "PH on the model (relay x rule)")
slot("S_in_PI", 5, "direct", ["FILT2"], "PI on the model (ticket comment x rule)")
# group placement: <= 5 samples per group
slot("S_out_PC", 5, "direct", ["ALIAS"], "PC withdrawn (mail x contacts x post)")
slot("S_out_PD", 5, "direct", ["EXC"], "PD fails the rights position (mail x sync record)")
slot("S_q_PA", 3, "direct", [], "PA qualifies")
slot("S_q_PF", 3, "direct", [], "PF qualifies")
for i in (1,2,3): slot(f"S_passed_{i}", 3, "direct", [], "publisher that said no")
for i in (1,2,3): slot(f"S_silent_{i}", 3, "direct", [], "publisher that never answered")
# forecast inputs and values, qualifying offers only
slot("A_adv_PB", 5, "direct", ["CORR"], "PB advance (mail x calendar note)")
slot("A_com_PE", 5, "direct", ["INPUT"], "PE monthly commitment (mail x card comment)")
slot("V12_PB", 5, "aggregate", ["CORR"], "PB 12-month value")
slot("V12_PE", 5, "aggregate", ["INPUT"], "PE 12-month value")
slot("V12_PH", 5, "aggregate", ["FILT1"], "PH 12-month value")
slot("V12_PI", 5, "aggregate", ["FILT2"], "PI 12-month value")
slot("V12_PA", 3, "aggregate", [], "PA 12-month value")
slot("V12_PF", 3, "aggregate", [], "PF 12-month value")
slot("VQ_PA", 5, "aggregate", ["DONE"], "PA Q4 cash (term mail x test source)")
slot("VQ_PB", 3, "aggregate", ["CORR"], "PB Q4 cash")
slot("VQ_PF", 3, "aggregate", [], "PF Q4 cash")
slot("V_keep", 3, "aggregate", [], "what the game earns if kept")
# the central result
slot("R_q4_total", 5, "aggregate", ["DONE","CORR"], "Q4 cash across qualifying offers")
slot("R_top", 5, "aggregate", ["EXC","INPUT"], "first pick")
slot("R_second", 5, "aggregate", ["CORR","FILT2"], "second pick")
# board: template-identical writes, sampled
slot("T_chk_q", 5, "aggregate", ["ALIAS","EXC","FILT1","FILT2"], "qualifying checklist holds exactly the right number")
slot("T_chk_p", 3, "aggregate", [], "passed checklist count")
slot("T_chk_s", 3, "aggregate", [], "no-reply checklist count")
slot("T_item_PH", 5, "write_content", ["FILT1"], "PH item on the qualifying checklist")
slot("T_cards", 5, "aggregate", ["ALIAS","EXC"], "exact new follow-up cards")
for i in (1,2,3): slot(f"T_card_{i}", 3, "write_content", [], "follow-up card sample")
# contacts and reminders: template-identical, sampled
slot("C_vol", 3, "aggregate", ["FILT1","FILT2"], "contacts added")
for i in (1,2,3): slot(f"C_{i}", 1, "write_content", [], "contact sample")
slot("M_vol", 3, "aggregate", ["ALIAS","EXC"], "reminders added")
for i in (1,2): slot(f"M_{i}", 1, "write_content", [], "reminder sample")
# follow-through: distinct content, per target
slot("W_count", 5, "aggregate", ["FOLLOW"], "drafts owed under the standing line")
for i in (1,2,3): slot(f"W_{i}", 5, "write_content", ["FOLLOW"], "draft per publisher quoted the paid-traffic numbers (rule x outreach sheet x thread)")
# reply: counts and a pick, never a member list
slot("K_reply", 1, "delivery", [], "reply on his thread")
slot("K_r_q", 5, "write_content", ["ALIAS","EXC","FILT1","FILT2"], "qualifying count in the reply")
slot("K_r_q4", 3, "write_content", ["DONE","CORR"], "Q4 figure in the reply")
slot("K_r_top", 3, "write_content", ["EXC","INPUT"], "first pick in the reply")
for i in ("sheet","checklist","cards","drafts"): slot(f"P_{i}", 1, "delivery", [], "reply after this write kind")
json.dump(dict(_note="PRE-SCENARIO SKETCH surface for hardness_v2_check.py and policy_model.py; not 01_Gradable_Surface.json. Fact slots only, no criterion text. Weights follow kind of work: 1 lookup, 3 interpretation or limited reconciliation, 5 multi-source reconciliation. v2 lean surface: shaped like bridge and handover, the two tasks that cleared SD. High-count writes are template-identical and sampled; the reply carries counts and a pick, not lists.", slots=S),
          open(os.path.join(HERE, "sketch_surface.json"), "w"), indent=1)
tw = sum(s["weight"] for s in S); fl = sum(s["weight"] for s in S if s["mechanisms"])
print("slots", len(S), "weight", tw, "flippable", fl, f"{fl/tw:.1%}")
