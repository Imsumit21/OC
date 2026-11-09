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
# status of each publisher with terms: a rule on one thread is 3; a join across services is 5
for m, w, ms, n in [("PA",3,[],"terms in writing; status"),("PB",3,[],"terms in writing; status"),("PC",5,["ALIAS"],"withdrawn via group person (mail x contacts x slack)"),
                    ("PD",5,["EXC"],"out on rights (mail x exec sync)"),("PE",3,[],"terms in writing; status"),("PF",3,[],"control"),("PG",3,[],"control"),
                    ("PH",5,["FILT1"],"on the sheet at all (slack relay x rule)"),("PI",5,["FILT2"],"on the sheet at all (linear comment x rule)")]:
    slot(f"S_status_{m}", w, "direct", ms, n)
# term values copied from one record are 1, except the ones a later record changes
for m in "ABCDEFG":
    slot(f"S_share_P{m}", 1, "direct", [], "rev share from the term mail")
for m, w, ms in [("PA",1,[]),("PB",5,["CORR"]),("PD",1,[]),("PE",1,[]),("PF",1,[]),("PG",1,[])]:
    slot(f"S_advance_{m}", w, "direct", ms, "advance")
slot("S_commit_PE", 5, "direct", ["INPUT"], "monthly installs (mail x later card comment)")
slot("S_terms_PH", 3, "direct", ["FILT1"], "rev share and advance from the relay")
slot("S_terms_PI", 3, "direct", ["FILT2"], "rev share and advance from the comment")
# derived forecast values
for m, w, ms in [("PA",3,[]),("PB",5,["CORR"]),("PE",5,["INPUT"]),("PF",3,[]),("PG",3,[]),("PH",5,["FILT1"]),("PI",5,["FILT2"])]:
    slot(f"V_12m_{m}", w, "aggregate", ms, "12-month value to the company under the ground rules")
for m, w, ms in [("PA",5,["DONE"]),("PB",3,["CORR"]),("PE",3,[]),("PF",3,[]),("PG",3,[])]:
    slot(f"V_q4_{m}", w, "aggregate", ms, "cash landing in Q4 under the deal's payment terms")
slot("V_keep_baseline", 3, "aggregate", [], "what the game earns if kept (warehouse months under the ground rules)")
# roll-ups
slot("R_count_eligible", 5, "aggregate", ["ALIAS","EXC","FILT1","FILT2"], "offers that qualify")
slot("R_q4_total", 5, "aggregate", ["DONE","CORR"], "Q4 cash across qualifying offers")
slot("R_top_pick", 5, "aggregate", ["EXC","INPUT"], "which deal goes first")
slot("R_runner_up", 5, "aggregate", ["CORR","FILT2"], "second deal")
# routine population: <= 5 samples per group plus a volume row
for i in range(1,6): slot(f"S_passed_{i}", 3, "direct", [], "publisher that said no")
for i in range(1,6): slot(f"S_silent_{i}", 3, "direct", [], "publisher that never answered")
slot("S_passed_volume", 3, "aggregate", [], "number that said no")
slot("S_silent_volume", 3, "aggregate", [], "number that never answered")
# follow-through
slot("W_pack_count", 5, "write_content", ["FOLLOW"], "drafts owed under the standing line")
for m in ("1","2","3"): slot(f"W_pack_{m}", 3, "write_content", ["FOLLOW"], "draft to a publisher quoted paid-traffic numbers, per target")
# other writes
for m in ("PA","PB","PE","PF","PG"): slot(f"W_card_{m}", 3, "write_content", [], "BD Follow Up card for a qualifying offer")
slot("W_card_count", 3, "aggregate", ["ALIAS","EXC"], "cards made")
for i in range(1,6): slot(f"W_contact_{i}", 1, "write_content", [], "contact for a publisher that answered")
slot("W_contact_volume", 3, "aggregate", ["FILT1","FILT2"], "contacts added")
# reply
slot("K_reply_counts", 3, "write_content", ["ALIAS","EXC"], "counts in the reply")
slot("K_reply_pick", 3, "write_content", ["EXC","INPUT"], "what he recommends in the reply")
slot("K_reply_q4", 3, "write_content", ["DONE","CORR"], "Q4 figure in the reply")
slot("K_reply_link", 1, "delivery", [], "link to the sheet")
slot("K_sheet_home", 1, "delivery", [], "sheet in his folder")
slot("K_order", 1, "delivery", [], "reply after the sheet is done")
json.dump(dict(_note="PRE-SCENARIO SKETCH surface for hardness_v2_check.py and policy_model.py; not 01_Gradable_Surface.json. Fact slots only, no criterion text. Weights follow kind of work: 1 lookup, 3 interpretation or limited reconciliation, 5 multi-source reconciliation. Per-target rows are listed up front, because per-target rows lifted the Robert LLC proxy average from about 76 to 83.6 %.", slots=S),
          open(os.path.join(HERE, "sketch_surface.json"), "w"), indent=1)
tw = sum(s["weight"] for s in S); fl = sum(s["weight"] for s in S if s["mechanisms"])
print("slots", len(S), "weight", tw, "flippable", fl, f"{fl/tw:.1%}")
