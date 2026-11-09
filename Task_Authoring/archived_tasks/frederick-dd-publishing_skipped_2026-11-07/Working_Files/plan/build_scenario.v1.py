#!/usr/bin/env python3
"""Scenario builder (design stage) for Frederick Stone · Domino Delights publishing-rights model.

Writes Working_Files/01_Hardness_Manifest.draft.json, Working_Files/01_Gradable_Surface.json and plan/ids.json.
Design only: the seeded texts here are the planned wording /create-injection must use verbatim.
Ids are minted deterministically (sha256 of a label) and collision-checked by plan/check_names.py.
Contains no prompt, Oracle Event or criterion text."""
import hashlib, json, os
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
CTX = json.load(open(os.path.join(WF, "00_Task_Context.json")))
FRED = "frederick.stone@harmonygames.co"
LEO = "leonard.hayes@harmonygames.co"
SALT = "hg-fred-dd-publishing|"


def hx(label, n): return hashlib.sha256((SALT + label).encode()).hexdigest()[:n]
def ts(iso): return int(datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp())
def drive(label, folder=False): return ("d_" if folder else "f_") + hx(label, 22)
def evt(label): return "evt_" + hx(label, 22)
def trello(label, iso): return "%08x" % ts(iso) + hx(label, 16)
def contact(label): return hx(label, 24)
def thread(label, iso): return str(((ts(iso) * 1000) << 20) + (int(hx(label, 8), 16) & 0xFFFFF))
def slack_ts(label, iso): return f"{ts(iso)}.{int(hx(label, 8), 16) % 1000000:06d}"
def gm(tid): return f"{FRED}/{tid}"


# ---------------------------------------------------------------- base anchors (all read through hg.py)
EXEC, BRIDGE, ANALYTICS, DM = "C07C2866011", "C096HFA5Z8W", "C069FF9Q57S", "D05S58U4SAK"
UABD_BOARD, BD_LIST = "66da196af476ab78deaa0cef", "670015c2ecd45b634d5eec81"
BASE = {
    "rights_post": f"{EXEC}/1756140953.197759",      # Leonard, Aug 25: keep code, IP and non-mobile rights
    "rights_agenda": f"{EXEC}/1756251167.453019",    # Leonard, Aug 26: same text as the sync agenda
    "sync_doc": "f_26e1f9a86761e35049192a",          # Executives Biweekly Sync, Aug 28
    "publisher_or_organic": "C08H78VJG80/1756223629.429589",
    "positioned": f"{BRIDGE}/1757542591.718649",
    "numbers_question": f"{DM}/1758735778.095599",   # Sep 24: quote incent numbers?
    "organic_arpi": f"{DM}/1758736747.409459",       # Sep 24: pure organics, $0.50 D30 ARPI
    "tranche": f"{DM}/1758736827.548589",            # Sep 24: new tranche of potential pubs
    "lead": f"{DM}/1758736842.534589",               # Sep 24: a dude looking for games
    "partners_doc": "f_10dfa1b4236a7c35dcb632",      # Publishing Partners (Fred, Sep 24)
    "bizdev_doc": "f_0d17fc08eddaf231cf7f28",        # Biz Dev Notes (Fred)
    "appodeal_fwd": gm("1829687508014442264"),
    "appodeal_thread": gm("1830012626042968381"),
    "rayking_thread": gm("1842348778705877030"),     # Frederick's Sep 4 message is an unsent draft
    "tilting_ack": gm("1842443183462721250"),        # auto-ack of a UA funding request
    "ua_funding_second_title": gm("1823332883409810377"),
    "apple_arcade": f"{EXEC}/1756261199.570279",
    "homa_codev": f"{BRIDGE}/1758210489.170809",
    "ncsoft_question": f"{EXEC}/1757516293.887729",
    "board_followup": gm("1830890312657338682"),     # Apr 30 board note: paid-traffic numbers
    "esg_engagement": gm("1841636073974841484"),     # ESG Law engagement (PERSON_2694 partner)
    "transfer_done": f"{EXEC}/1752726128.862409",
    "banker_root": f"{EXEC}/1757345405.134829",      # Sep 8 root: Arthur's cash reply sits under it
    "seventy_root": f"{EXEC}/1758736960.824899",     # Sep 24 root: Robert's relay sits under it
    "matthew_root": f"{BRIDGE}/1758147530.732569",   # Sep 17 root: Leonard's standing line sits under it
    "fred_root": "d_175c0d7bc72ed244b944cb",
    "board_event": "evt_bd61f3209523d19fdd6ba2",
    "eng2362": "ENG-2362",
}

T = {   # seeded timestamps (UTC), all before the seed bound 2025-10-01T00:00:00Z
    "onepager": "2025-05-05T17:00:00Z",
    "outreach_sheet": "2025-09-24T19:30:00Z",
    "codev_doc": "2025-09-19T17:30:00Z",
    "sunfold_terms": "2025-09-19T15:00:00Z",
    "pb_terms": "2025-09-22T15:00:00Z",
    "arthur_analytics": "2025-09-22T18:40:00Z",
    "eng2362_comment": "2025-09-22T18:32:00Z",
    "moonrail_terms": "2025-09-18T15:00:00Z",
    "standing_line": "2025-09-25T16:20:00Z",
    "oakline_terms": "2025-09-23T15:30:00Z",
    "oakline_paid": "2025-09-26T16:00:00Z",
    "oakline_card_comment": "2025-09-26T17:10:00Z",
    "copperleaf_relay": "2025-09-26T18:05:00Z",
    "kestrel_post": "2025-09-26T20:15:00Z",
    "oakline_card": "2025-09-23T19:00:00Z",
    "sunfold_card": "2025-09-19T19:00:00Z",
    "dd_card": "2025-09-29T16:40:00Z",
    "rule_doc": "2025-09-29T16:00:00Z",
    "esg_note": "2025-09-29T17:30:00Z",
    "arthur_cash": "2025-09-29T17:05:00Z",
    "pb_event": "2025-09-29T18:30:00Z",
    "pb_event_update": "2025-09-29T20:00:00Z",
    "folder": "2025-09-29T20:30:00Z",
    "sunfold_comment": "2025-09-30T16:00:00Z",
    "esg_leonard": "2025-09-30T16:10:00Z",
    "hub": "2025-09-30T23:10:00Z",
}

IDS = {
    "hub_thread": gm(thread("hub", T["hub"])),
    "esg_thread": gm(thread("esg", T["esg_note"])),
    "rule_doc": drive("rule_doc"),
    "codev_doc": drive("codev_doc"),
    "outreach_sheet": drive("outreach_sheet"),
    "onepager_deck": drive("onepager"),
    "dd_folder": drive("dd_folder", folder=True),
    "dd_card": trello("dd_card", T["dd_card"]),
    "oakline_card": trello("oakline_card", T["oakline_card"]),
    "sunfold_card": trello("sunfold_card", T["sunfold_card"]),
    "oakline_card_comment": trello("oakline_card_comment", T["oakline_card_comment"]),
    "sunfold_comment": trello("sunfold_comment", T["sunfold_comment"]),
    "pb_event": evt("pb_event"),
    "monday_event": evt("monday_event"),
    "arthur_cash": f"{EXEC}/{slack_ts('arthur_cash', T['arthur_cash'])}",
    "copperleaf_relay": f"{EXEC}/{slack_ts('copperleaf_relay', T['copperleaf_relay'])}",
    "kestrel_post": f"{EXEC}/{slack_ts('kestrel_post', T['kestrel_post'])}",
    "standing_line": f"{BRIDGE}/{slack_ts('standing_line', T['standing_line'])}",
    "arthur_analytics": f"{ANALYTICS}/{slack_ts('arthur_analytics', T['arthur_analytics'])}",
    "eng2362_comment": "lc_" + hx("eng2362_comment", 24),
    "anika_contact": contact("anika"),
    "lena_contact": contact("lena"),
}

# ---------------------------------------------------------------- planned wording (verbatim at injection)
HUB = ("Fred,\n\na16z didn't happen and the Turkish fund is a no, so I want to get serious about the DD publishing idea from the sync. "
       "On Monday Oct 6 I want the four of us to sit down knowing what each publisher would actually bring in. Can you build the model for that?\n\n"
       "The ground rules doc has how we're doing this, including who counts and how an offer gets valued. "
       "Put the model in your DD publishing folder, laid out the way the doc says.\n\n"
       "Do what's on the DD publishing card on the UA/BD board too.\n\n"
       "Everyone at a publisher who has written to one of us should be in Contacts, with the company in the job title. Skip anyone who's already there.\n\n"
       "That guy from Sep 24 I said I'd chase only wants hypercasual, so leave him out.\n\n"
       "When it's all in, reply here with which offer goes first, what it brings in over 12 months, what it brings in during Q4, "
       "and how much publisher money we've actually banked so far.\n\nLeonard")
RULES = ("DD publishing model: ground rules\nWritten for Monday's talk. Leonard, Sep 29.\n\n"
         "Who's in\nEvery publisher on Fred's outreach sheet, plus any publisher that came to one of the four of us about Domino Delights since Apr 1, 2025, however it reached us. "
         "Co-dev or investment talks about Zombie Match aren't part of this. That covers Homa and NCsoft, and Tilting Point's UA fund form, which was for Zombie Match.\n\n"
         "Status (first that fits, top to bottom)\n"
         "Withdrawn: they gave terms, then took them back.\n"
         "Out on rights: their terms take something we keep. The position we agreed at the August sync still stands.\n"
         "Live: terms in writing from them, whether that's a term sheet, an email, or their note pasted in by one of us.\n"
         "Passed: they said no.\n"
         "Waiting on us: they wrote to us, there are no terms, and we haven't answered.\n"
         "No reply: nothing back from them. An automatic acknowledgement doesn't count.\n\n"
         "Use the latest terms we have from them, wherever they are.\n\n"
         "Valuing a Live offer\nMonthly installs x 12 x $0.50 is the gross. $0.50 is the organic D30 ARPI from my Sep 24 note. It's a planning figure, not a promise.\n"
         "Our share is their rev share times the gross.\n"
         "12-month value is the larger of our share and the total advance, because the advance is recouped out of our share.\n\n"
         "Q4 cash\nAdvance money that lands between Oct 1 and Dec 31, 2025. Assume we sign on Oct 31. If ESG gives us a later date, use theirs. "
         "A payment on net terms lands that many days after signature. Rev share statements don't land in Q4. Banked means it's actually in the SVB account.\n\n"
         "Keep value\nWhat DD earned in Jul, Aug and Sep (ANALYTICS.MONETIZATION.REVENUE_DAILY, total_revenue_usd), averaged, times 12.\n\n"
         "First pick\nThe Live offer with the highest 12-month value.\n\n"
         "Reminders\nOne on Fred's calendar on each Live offer's response date.\n\n"
         "Layout\nA Google Sheet called DD publishing model. Tab Publishers: Publisher, Status, Rev share, Advance, Monthly installs, 12-month value, Q4 cash, Banked. "
         "Figures only for Live offers. Tab Summary: Keep value, First pick.\n\n"
         "Anything I've already said about what goes out to publishers still applies.")
CARD = ("For Monday. One checklist per status on this card, one item per publisher. Every Live, Waiting on us and No reply publisher gets a follow-up card on this list, "
        "named F/up with and the publisher. If they already have a card here, leave a comment with the status on that one instead.")
STANDING = ("On the numbers going out: the May one-pager only had the paid-traffic numbers on it. Anyone who got it and is still Live hears the organic figure from us, "
            "$0.50 D30 ARPI, before we sit down with them. Fred, one short note each as a draft and I'll read them first.")
ARTHUR_CASH = "On cash: that Oakline $10K never hit SVB. Their bank sent it back because the beneficiary name still said Calm Play. They're resending it next week."
RELAY = ("Someone I know at Copperleaf Games saw DD and emailed me out of the blue, pasting it here so it doesn't get lost: "
         "\"We'd do 28% of net to you, a $32,000 advance net 30 from signature, 40,000 installs a month for 12 months, mobile stores only, open to Oct 17. Jonas Weber, Copperleaf, jonas@copperleafgames.com\"")
KESTREL = "Anika called me. Kestrel have frozen every outside signing for the year, so whatever they had on the table with us is off."
ANALYTICS_POST = "A tech lead at a publisher asked me about Singular deep links for DD. Notes are on ENG-2362."
ENG_COMMENT = ("Redwood Arcade's tech lead, Mei Tanaka (mei@redwoodarcade.com), asked about deep links while they look at DD. Her terms for the record: 24% of net to HG, a $25,000 advance net 45 from signature, "
               "40,000 installs a month for 12 months, mobile stores only, open to Oct 31.")
PB_NOTE = ("Agenda: walk through their term sheet, the UA plan for the first two quarters, who runs live ops after the handover, and what they need from us on store listings and analytics access. "
           "Notes: Paola came back on the call. The advance is $40,000 now, not the number in the term sheet. Everything else stands.")
SUNFOLD_NOTE = "Lena rang. Their UA budget got cut, so they can only commit 30,000 installs a month, not the 50,000 in the term sheet. Rest stands."
OAK_PAID = "Confirming our finance team sent the $10,000 first-look payment by wire today, ref OAK-2291. The remaining $20,000 of the advance stays payable net 30 from signature."
OAK_CARD = "Marek says the $10K first-look payment went out today."
ESG_NOTE = "Leonard, we're tied up on an arbitration until Nov 7. The earliest I can turn a licence for Domino Delights for signature is Nov 14."
ESG_LEO = "OK. Fred, that makes Nov 14 our signing date, not Oct 31."
Q = dict(hub=HUB, rules=RULES, card=CARD, standing=STANDING, arthur_cash=ARTHUR_CASH, relay=RELAY, kestrel=KESTREL, analytics=ANALYTICS_POST,
         eng=ENG_COMMENT, pb_note=PB_NOTE, sunfold_note=SUNFOLD_NOTE, oak_paid=OAK_PAID, oak_card=OAK_CARD, esg_note=ESG_NOTE, esg_leo=ESG_LEO)

# ---------------------------------------------------------------- the cohort. value per install $0.50, signing Nov 14 (Oct 31 in the rule doc)
def v12(share, installs, adv): return max(round(share * installs * 12 * 0.5), adv)
M = [
 # key, person, domain, status, tranche, sent, share, installs(true), advance(true), net, respond, notes
 dict(key="Oakline Games", person=("Marek", "Sobol"), dom="oaklinegames.com", status="Live", tranche=2, sent="Intro only", share=.30, inst=20000, adv=30000, q4=30000, banked=0, resp="Oct 24"),
 dict(key="Tallwater Games", person=("Paola", "Duarte"), dom="tallwatergames.com", status="Live", tranche=1, sent="May one-pager", share=.25, inst=30000, adv=40000, q4=40000, banked=0, resp="Oct 17"),
 dict(key="Sunfold Mobile", person=("Lena", "Fischer"), dom="sunfoldmobile.com", status="Live", tranche=2, sent="Intro only", share=.30, inst=30000, adv=20000, q4=20000, banked=0, resp="Oct 31"),
 dict(key="Harbor Lane Games", person=("Diego", "Reyes"), dom="harborlanegames.com", status="Live", tranche=1, sent="May one-pager", share=.20, inst=25000, adv=25000, q4=0, banked=0, resp="Oct 24"),
 dict(key="Wavecrest Play", person=("Sofia", "Lindqvist"), dom="wavecrestplay.com", status="Live", tranche=1, sent="May one-pager", share=.22, inst=15000, adv=15000, q4=0, banked=0, resp="Oct 31"),
 dict(key="Copperleaf Games", person=("Jonas", "Weber"), dom=None, status="Live", tranche=0, sent="not on the sheet", share=.28, inst=40000, adv=32000, q4=32000, banked=0, resp="Oct 17"),
 dict(key="Redwood Arcade", person=("Mei", "Tanaka"), dom=None, status="Live", tranche=0, sent="not on the sheet", share=.24, inst=40000, adv=25000, q4=25000, banked=0, resp="Oct 31"),
 dict(key="Moonrail Studios", person=("Anika", "Rao"), dom="moonrailstudios.com", status="Withdrawn", tranche=1, sent="May one-pager"),
 dict(key="Northglow Publishing", person=("Callum", "Ross"), dom="northglowpublishing.com", status="Out on rights", tranche=2, sent="Intro only"),
 dict(key="Pinegrove Games", person=("Elena", "Petrova"), dom="pinegrovegames.com", status="Out on rights", tranche=2, sent="Intro only"),
 dict(key="Fernhollow Media", person=("Rhys", "Morgan"), dom="fernhollowmedia.com", status="Passed", tranche=1, sent="May one-pager"),
 dict(key="Quietbay Games", person=("Nadia", "Haddad"), dom="quietbaygames.com", status="Passed", tranche=1, sent="May one-pager"),
 dict(key="Slatewood Mobile", person=("Yuki", "Sato"), dom="slatewoodmobile.com", status="Passed", tranche=2, sent="Intro only"),
 dict(key="Ironbridge Interactive", person=("Tessa", "Hale"), dom="ironbridgeinteractive.com", status="Passed", tranche=2, sent="Intro only"),
 dict(key="Tidewell Studios", person=("Omar", "Khalil"), dom="tidewellstudios.com", status="Passed", tranche=3, sent="Organic note"),
 dict(key="Marlin Play", person=("Greta", "Holm"), dom="marlinplay.com", status="Passed", tranche=3, sent="Organic note"),
 dict(key="Appodeal", person=None, dom=None, status="Waiting on us", tranche=0, sent="came to us Apr 17", base=BASE["appodeal_thread"]),
 dict(key="Rayking Game", person=None, dom=None, status="Waiting on us", tranche=0, sent="came to us Sep 4", base=BASE["rayking_thread"]),
 dict(key="Kitebridge Games", person=("Ivo", "Novak"), dom="kitebridgegames.com", status="Waiting on us", tranche=3, sent="Organic note"),
 dict(key="Orchard Lane Games", person=None, dom="orchardlanegames.com", status="No reply", tranche=1, sent="May one-pager"),
 dict(key="Summit Mobile", person=None, dom="summitmobile.io", status="No reply", tranche=1, sent="May one-pager", ack=True),
 dict(key="Silverlake Mobile", person=None, dom="silverlakemobile.com", status="No reply", tranche=2, sent="Intro only"),
 dict(key="Cedarbrook Play", person=None, dom="cedarbrookplay.com", status="No reply", tranche=2, sent="Intro only"),
 dict(key="Foxglove Games", person=None, dom="foxglovegames.com", status="No reply", tranche=3, sent="Organic note"),
 dict(key="Riverstone Interactive", person=None, dom="riverstoneinteractive.com", status="No reply", tranche=3, sent="Organic note"),
 dict(key="Bellwether Arcade", person=None, dom="bellwetherarcade.com", status="No reply", tranche=3, sent="Organic note"),
]
for m in M:
    if m["status"] == "Live":
        m["v12"] = v12(m["share"], m["inst"], m["adv"])
WRONG = {"Oakline Games": dict(q4=20000, banked=10000), "Tallwater Games": dict(adv=60000, v12=60000, q4=60000),
         "Sunfold Mobile": dict(inst=50000, v12=90000), "Harbor Lane Games": dict(q4=25000), "Wavecrest Play": dict(q4=15000)}
TERM_DOCS = {  # term sheets in Drive as stated at the time (superseded values kept on purpose)
 "Oakline Games": "30% of net, $30,000 advance ($10,000 first-look payment on acceptance of this sheet, credited to the advance, the remaining $20,000 net 30 from signature), 20,000 installs a month for 12 months, mobile stores, open to Oct 24",
 "Tallwater Games": "25% of net, $60,000 advance net 30 from signature, 30,000 installs a month for 12 months, mobile stores, open to Oct 17",
 "Sunfold Mobile": "30% of net, $20,000 advance net 45 from signature, 50,000 installs a month for 12 months, mobile stores, open to Oct 31",
 "Harbor Lane Games": "20% of net, $25,000 advance net 60 from signature, 25,000 installs a month for 12 months, mobile stores, open to Oct 24",
 "Wavecrest Play": "22% of net, $15,000 advance net 60 from signature, 15,000 installs a month for 12 months, mobile stores, open to Oct 31",
 "Moonrail Studios": "26% of net, $30,000 advance net 30 from signature, 35,000 installs a month for 12 months, mobile stores, open to Oct 24",
 "Northglow Publishing": "35% of net, $50,000 advance net 30 from signature, 60,000 installs a month for 12 months, exclusive across all digital storefronts and platforms, including PC and web, open to Oct 31",
 "Pinegrove Games": "30% of net, $40,000 advance net 30 from signature, 45,000 installs a month for 12 months, mobile stores, full source code and build pipeline delivered to Pinegrove at signature, open to Oct 24",
}
KEEP_MONTHS = {"2025-07": 2078.33, "2025-08": 721.55, "2025-09": 381.11}   # dd_revenue_months.txt
KEEP_VALUE = round(sum(KEEP_MONTHS.values()) / 3 * 12, 2)
TRUTH = sorted((m for m in M if m["status"] == "Live"), key=lambda m: -m["v12"])
FIRST_PICK = TRUTH[0]["key"]
assert FIRST_PICK == "Copperleaf Games" and TRUTH[1]["key"] == "Redwood Arcade"
COUNTS = {s: sum(1 for m in M if m["status"] == s) for s in ("Live", "Withdrawn", "Out on rights", "Passed", "Waiting on us", "No reply")}
assert sum(COUNTS.values()) == 26 and COUNTS["Live"] == 7

for label, sub, full in [("hub rules", "The ground rules doc has how we're doing this", HUB), ("hub card", "Do what's on the DD publishing card", HUB),
                         ("hub folder", "Put the model in your DD publishing folder", HUB), ("rules scope", "Every publisher on Fred's outreach sheet", RULES),
                         ("rules sync", "The position we agreed at the August sync", RULES), ("rules latest", "Use the latest terms we have from them, wherever they are", RULES),
                         ("rules however", "however it reached us", RULES), ("rules esg", "If ESG gives us a later date, use theirs", RULES),
                         ("rules goes out", "Anything I've already said about what goes out to publishers still applies", RULES),
                         ("rules warehouse", "ANALYTICS.MONETIZATION.REVENUE_DAILY", RULES), ("standing deck", "the May one-pager", STANDING)]:
    assert sub in full, label

# ---------------------------------------------------------------- manifest
requirements = {
 "R1": "the publisher population: every publisher on the outreach sheet plus any publisher that came to the founders about Domino Delights since Apr 1, 2025; one row per publisher",
 "R2": "status per publisher (Withdrawn, Out on rights, Live, Passed, Waiting on us, No reply)",
 "R3": "latest terms per Live offer: rev share, advance, monthly installs",
 "R4": "12-month value per Live offer",
 "R5": "Q4 cash per Live offer and money banked so far",
 "R6": "rights test: whether an offer's terms take something the founders keep",
 "R7": "first pick",
 "R8": "keep value of the game",
 "R9": "board writes: a checklist per status with one item per publisher, and a follow-up card per Live, Waiting on us and No reply publisher, reusing existing cards",
 "R10": "a contact per publisher person who has written to us, skipping existing contacts",
 "R11": "a reminder on each Live offer's response date",
 "R12": "a draft note with the organic figure to each Live publisher that got the May one-pager",
 "R13": "the reply to Leonard: first pick, its 12-month value, its Q4 cash and money banked",
}
services = {
 "gmail": {"role": "Leonard's ask and the report destination; each publisher's thread; ESG's signing date; Oakline's payment confirmation; follow-through drafts", "weight_reason": "the ask, who answered and the signing date live in mail"},
 "gdocs": {"role": "the ground rules doc (H1), its co-dev decoy, ten-odd publisher term sheets, the base exec sync (H2)", "weight_reason": "rules, terms and the rights position"},
 "gsheets": {"role": "Fred's outreach sheet (population, what each got); the model itself", "weight_reason": "the population and the deliverable"},
 "gdrive": {"role": "the DD publishing folder and term-sheet filing", "weight_reason": "the destination Frederick owns"},
 "gslides": {"role": "the May one-pager that carried the paid-traffic numbers", "weight_reason": "who was told what, behind the follow-through"},
 "slack": {"role": "Arthur's cash note, Robert's relay, the Kestrel post, Leonard's standing line, the analytics pointer", "weight_reason": "four deciding records sit in Slack"},
 "gcal": {"role": "Tallwater's follow-up note; Monday's sit-down; reminders", "weight_reason": "a corrected advance and the reminders"},
 "trello": {"role": "the DD publishing card (H3); existing follow-up cards with a comment on Sunfold's commitment; new cards", "weight_reason": "the board ask, a corrected input and the board writes"},
 "contacts": {"role": "who Anika works for; existing and new contacts", "weight_reason": "the alias join and the contact writes"},
 "linear": {"role": "Arthur's comment on ENG-2362 holding Redwood's terms", "weight_reason": "an in-scope offer outside the inbox"},
 "snowflake": {"role": "REVENUE_DAILY for the keep value", "weight_reason": "the only home of the keep value"},
}
anchors = [
 {"id": "A1", "prompt_reference": "Leonard's email from yesterday", "service": "gmail", "locator": IDS["hub_thread"], "record": IDS["hub_thread"], "requirement_ids": ["R10", "R13"]},
 {"id": "A2", "prompt_reference": "the DD publishing card", "service": "trello", "locator": IDS["dd_card"], "record": IDS["dd_card"], "requirement_ids": ["R9"]},
 {"id": "A3", "prompt_reference": "my DD publishing folder", "service": "gdrive", "locator": IDS["dd_folder"], "record": IDS["dd_folder"], "requirement_ids": []},
]
def frag(id, service, container, kind, via, seeded, base, by, quote, reqs, names=None, **k):
    d = dict(id=id, service=service, container=container, locator=container, kind=kind, incorporated_via=via, seeded_ids=seeded, base_pointers=base,
             delegated_by_record=by, delegation_quote=quote, requirement_ids=reqs, names_authorities=names or [])
    d.update(k); return d
H, RD = IDS["hub_thread"], IDS["rule_doc"]
ask_fragments = [
 frag("K1", "gdocs", RD, "delegation", ["A1"], [RD], [], H, "The ground rules doc has how we're doing this", ["R2", "R4", "R5", "R7", "R11"],
      [{"id": "H1", "quote": "The ground rules doc"}]),
 frag("K2", "gsheets", IDS["outreach_sheet"], "requirement", ["A1", "K1"], [IDS["outreach_sheet"]], [], RD, "Every publisher on Fred's outreach sheet", ["R1"]),
 frag("K3", "gdocs", BASE["sync_doc"], "requirement", ["A1", "K1"], [], [BASE["sync_doc"]], RD, "The position we agreed at the August sync", ["R6"],
      [{"id": "H2", "quote": "The position we agreed at the August sync"}]),
 frag("K4", "trello", IDS["dd_card"], "requirement", ["A2"], [IDS["dd_card"]], [], IDS["dd_card"], "One checklist per status on this card", ["R9"], [{"id": "H3", "quote": "One checklist per status on this card"}]),
 frag("K5", "gdrive", IDS["dd_folder"], "destination", ["A1"], [IDS["dd_folder"]], [], H, "Put the model in your DD publishing folder", ["R13"]),
 frag("K6", "gmail", IDS["esg_thread"], "amendment", ["A1", "K1"], [IDS["esg_thread"]], [], RD, "If ESG gives us a later date, use theirs", ["R5"]),
 frag("K7", "gcal", IDS["pb_event"], "amendment", ["A1", "K1"], [IDS["pb_event"]], [], RD, "Use the latest terms we have from them, wherever they are", ["R3"]),
 frag("K8", "trello", IDS["sunfold_card"], "amendment", ["A1", "K1"], [IDS["sunfold_card"], IDS["sunfold_comment"]], [], RD, "Use the latest terms we have from them, wherever they are", ["R3"]),
 frag("K9", "slack", BASE["matthew_root"], "requirement", ["A1", "K1"], [IDS["standing_line"]], [], RD, "Anything I've already said about what goes out to publishers still applies", ["R12"]),
 frag("K10", "gslides", IDS["onepager_deck"], "format", ["A1", "K1", "K9"], [IDS["onepager_deck"]], [], IDS["standing_line"], "the May one-pager", ["R12"]),
 frag("K11", "slack", BASE["seventy_root"], "requirement", ["A1", "K1"], [IDS["copperleaf_relay"]], [], RD, "however it reached us", ["R1", "R3"]),
 frag("K12", "linear", BASE["eng2362"], "requirement", ["A1", "K1"], [IDS["eng2362_comment"]], [], RD, "however it reached us", ["R1", "R3"]),
 frag("K13", "slack", ANALYTICS, "requirement", ["A1", "K1"], [IDS["arthur_analytics"]], [], RD, "however it reached us", ["R1"]),
 frag("K14", "snowflake", "snowflake:ANALYTICS.MONETIZATION.REVENUE_DAILY", "requirement", ["A1", "K1"], [], ["ANALYTICS.MONETIZATION.REVENUE_DAILY"], RD, "ANALYTICS.MONETIZATION.REVENUE_DAILY", ["R8"]),
 frag("K15", "contacts", IDS["anika_contact"], "recipient", ["A1"], [IDS["anika_contact"], IDS["lena_contact"]], [], H, "Everyone at a publisher who has written to one of us should be in Contacts", ["R10"]),
]
authorities = [
 {"id": "H1", "name": "the ground rules doc", "home_service": "gdocs", "decoy_service": "gdocs", "governs": ["R2", "R4", "R5", "R7", "R8", "R11"], "findable_query": "ground rules", "seeded_ids": [RD], "base_pointers": [],
  "decoy_seeded_ids": [IDS["codev_doc"]], "decoy_base_pointers": [], "decoy_scope": {"dimension": "game", "decoy": "co-dev terms for Zombie Match (Sep 19)", "task": "publishing rights for Domino Delights"}},
 {"id": "H2", "name": "the rights position from the August sync", "home_service": "gdocs", "decoy_service": "gmail", "governs": ["R6"], "findable_query": "publishing rights", "seeded_ids": [], "base_pointers": [BASE["sync_doc"]],
  "decoy_seeded_ids": [], "decoy_base_pointers": [BASE["appodeal_fwd"]], "decoy_scope": {"dimension": "issuer", "decoy": "Appodeal's own programme line that it takes no game transfer or IP rights", "task": "what the founders keep"}},
 {"id": "H3", "name": "the DD publishing card", "home_service": "trello", "decoy_service": "trello", "governs": ["R9"], "findable_query": "DD publishing", "seeded_ids": [IDS["dd_card"]], "base_pointers": [],
  "decoy_seeded_ids": [], "decoy_base_pointers": ["trello:/cards/557"], "decoy_scope": {"dimension": "lot", "decoy": "the four Oct 2024 BD Follow Up cards from the first partner round", "task": "the Sep 2025 publisher round"}},
]
cohort = {
 "definition": "every publisher on Fred's outreach sheet plus any publisher that came to the founders about Domino Delights since Apr 1, 2025 (26: 24 on the sheet, 2 outside it)",
 "definition_source": [RD, IDS["outreach_sheet"]], "key": "publisher", "size": 26,
 "evidence_surfaces": [
  {"service": "gmail", "tool": "gmail_search_messages+gmail_get_thread", "per_record_calls": 0.75, "records": 24, "requirement": "R2", "decides": "status per publisher",
   "why_no_bulk": "gmail_search_messages returns ids only; gmail_get_messages_batch reads bodies in bulk, so three quarters of a call per publisher is counted",
   "short_circuit": "only a publisher's own thread shows whether it answered, passed or wrote first; no list records outcomes, and the outreach sheet carries none"},
  {"service": "gdocs", "tool": "gdocs_get_document_text", "per_record_calls": 1.0, "records": 8, "seeded": True, "seeded_ids": [drive("terms:" + k) for k in TERM_DOCS], "requirement": "R3", "decides": "latest terms per Live offer",
   "why_no_bulk": "each term sheet is its own document; no call returns several bodies",
   "short_circuit": "rights, net terms, installs and advance are only in that sheet; the covering mail says terms are attached, not what they are"},
  {"service": "slack", "tool": "slack_search_public_and_private", "per_record_calls": 1.0, "records": 26, "requirement": "R2", "decides": "status per publisher",
   "why_no_bulk": "channel history returns roots only and a generic search misses a record that names a person or a group",
   "short_circuit": "a later founder note can change a publisher's standing, so a thread that looks settled still needs its own search"},
  {"service": "gcal", "tool": "gcal_search_events", "per_record_calls": 1.0, "records": 9, "requirement": "R3", "decides": "latest terms per Live offer",
   "why_no_bulk": "gcal_list_events shows the start of a description only; the rest needs the event itself",
   "short_circuit": "a call note can move a term after the sheet was sent; the sheet can't show that"},
  {"service": "contacts", "tool": "contacts_search_contacts", "per_record_calls": 0.5, "records": 19, "requirement": "R10", "decides": "a contact per publisher person who has written to us",
   "why_no_bulk": "contacts_get_contacts lists everyone in bulk, so half a call per publisher is counted",
   "short_circuit": "Leonard asks to skip anyone already there, so each person has to be checked before each add"},
 ]}
def trap(id, family, svcs, seeded, base, req, wrong, res, **k):
    d = dict(id=id, family=family, services=svcs, seeded_ids=seeded, base_pointers=base, requirement=req, expected_wrong_reading=wrong, resolver=res); d.update(k); return d
def term(k): return drive("terms:" + k)
def thr(k): return gm(thread("member:" + k, "2025-09-01T16:00:00Z"))
traps = [
 trap("T1", "done_gap", ["gmail", "trello", "slack"], [thr("Oakline Games"), IDS["oakline_card_comment"], IDS["arthur_cash"]], [BASE["banker_root"]], "R5",
      "Oakline's $10,000 is banked: Marek confirms the wire and the card says it went out, so Q4 cash is only the remaining $20,000",
      "Arthur's Sep 29 reply: the money never hit SVB, the bank sent it back and Oakline will resend it next week; the rule doc says banked means in the SVB account",
      discovery_order="Marek's mail and the card are met first, in Oakline's own thread and on the board; Arthur's note sits in a reply under an older root about a banker"),
 trap("T2", "superseding", ["gdocs", "gcal"], [term("Tallwater Games"), IDS["pb_event"]], [], "R3",
      "Tallwater's advance is the $60,000 in its term sheet", "Leonard's note on the follow-up call: $40,000 now, everything else stands",
      discovery_order="the term sheet is opened with every other offer; the note sits past the agenda in a calendar description",
      version_records=[{"service": "gdocs", "id": term("Tallwater Games"), "container": "file:" + term("Tallwater Games"), "seeded": True, "at": T["pb_terms"]},
                       {"service": "gcal", "id": IDS["pb_event"], "container": "gcal:" + IDS["pb_event"], "seeded": True, "at": T["pb_event_update"]}]),
 trap("T3", "scope_alias", ["gmail", "contacts", "slack"], [thr("Moonrail Studios"), IDS["anika_contact"], IDS["kestrel_post"]], [], "R2",
      "Moonrail's offer is Live: its term sheet is open and nothing carries the Moonrail name",
      "the post says Anika and Kestrel; her signature and her Contacts row tie both to Moonrail", discovery_order="a name search for Moonrail returns nothing in Slack, so the thread reads as open"),
 trap("T4", "exact_predicate", ["slack", "gsheets"], [IDS["copperleaf_relay"]], [BASE["seventy_root"]], "R1",
      "the population is the outreach sheet and Frederick's inbox", "the rule doc brings in anyone who came to one of the four of us; Robert pasted Copperleaf's note into a thread",
      discovery_order="the sheet is read first and looks complete"),
 trap("T5", "exact_predicate", ["linear", "slack", "gsheets"], [IDS["arthur_analytics"], IDS["eng2362_comment"]], [BASE["eng2362"]], "R1",
      "deal terms don't live on engineering tickets", "Arthur's post points at ENG-2362, whose comment holds Redwood's terms", discovery_order="the sheet is read first; Linear isn't on the mail path"),
 trap("T6", "authority", ["gdocs", "slack"], [term("Northglow Publishing")], [BASE["sync_doc"], BASE["rights_post"]], "R6",
      "Northglow is the best deal: the largest 12-month value and a clean rev share", "the founders keep non-mobile distribution rights; Northglow's grant covers all digital storefronts, including PC and web",
      discovery_order="the term sheet's numbers are met first; the rights position is an old record the rule doc points at by role"),
 trap("T7", "superseding", ["gdocs", "trello"], [term("Sunfold Mobile"), IDS["sunfold_card"], IDS["sunfold_comment"]], [], "R3",
      "Sunfold commits 50,000 installs a month", "Frederick's Sep 30 card comment: 30,000 a month, rest stands",
      discovery_order="the term sheet is opened first; the card is titled by Lena's first name",
      version_records=[{"service": "gdocs", "id": term("Sunfold Mobile"), "container": "file:" + term("Sunfold Mobile"), "seeded": True, "at": T["sunfold_terms"]},
                       {"service": "trello", "id": IDS["sunfold_comment"], "container": "trello:" + IDS["sunfold_card"], "seeded": True, "at": T["sunfold_comment"]}]),
 trap("T8", "synthesis_omission", ["slack", "gsheets", "gslides"], [IDS["standing_line"], IDS["onepager_deck"]], [BASE["matthew_root"]], "R12",
      "the model, the board and the reply finish the job", "Leonard's line under his Sep 17 root: anyone who got the May one-pager and is still Live hears the organic figure, as a draft",
      discovery_order="the rule doc points at it by role only; the reply sits under a root about raising"),
 trap("T9", "effective_date", ["gdocs", "gmail"], [RD, IDS["esg_thread"]], [], "R5",
      "the signing date is Oct 31, so net-60 advances land by Dec 30", "ESG's Sep 29 note and Leonard's Sep 30 reply make it Nov 14, so net-60 money lands Jan 13",
      discovery_order="the rule doc is read first; ESG's thread doesn't name a publisher",
      version_records=[{"service": "gdocs", "id": RD, "container": "file:" + RD, "seeded": True, "at": T["rule_doc"]},
                       {"service": "gmail", "id": IDS["esg_thread"], "container": "gmail:" + IDS["esg_thread"], "seeded": True, "at": T["esg_leonard"]}]),
 trap("T10", "reuse_exclusion", ["trello"], [IDS["oakline_card"], IDS["sunfold_card"]], [], "R9",
      "every Live publisher needs a new card", "two cards already exist under contacts' first names: leave a comment there"),
 trap("T11", "near_miss_mention", ["gmail"], [thr("Summit Mobile")], [], "R2", "Summit answered: there's a message from it", "an automatic acknowledgement doesn't count, so No reply"),
 trap("T12", "tool_surface", ["gmail"], [], [BASE["rayking_thread"]], "R2", "Frederick replied to Rayking, so it isn't waiting on us", "his Sep 4 message is an unsent draft addressed to Leonard, so Rayking is Waiting on us"),
 trap("T13", "superseding", ["gmail", "slack", "gdocs"], [RD], [BASE["board_followup"], BASE["numbers_question"]], "R4",
      "value an install at the paid-traffic numbers ($0.87 ARPDAU, an LTV of $7)", "the rule doc fixes $0.50, the organic D30 ARPI",
      discovery_order="the Sep 24 DM and the April board note are met by a metrics search",
      version_records=[{"service": "gmail", "base_pointer": BASE["board_followup"], "container": "gmail:" + BASE["board_followup"], "seeded": False, "at": "2025-05-01T04:19:37Z"},
                       {"service": "slack", "base_pointer": BASE["numbers_question"], "container": "slack:" + DM + "/1758735778.095599", "seeded": False, "at": "2025-09-24T17:42:58Z"},
                       {"service": "gdocs", "id": RD, "container": "file:" + RD, "seeded": True, "at": T["rule_doc"]}]),
 trap("T14", "authority", ["gdocs"], [term("Pinegrove Games")], [BASE["sync_doc"]], "R6", "Pinegrove is Live: its grant is mobile only", "it takes source code and the build pipeline; the founders keep the code"),
 trap("T15", "distractor", ["slack"], [], [BASE["homa_codev"], BASE["ncsoft_question"]], "R1", "Homa and NCsoft are publishers in talks", "the rule doc leaves co-dev and investment talks about Zombie Match out", distractor_type="other_title"),
 trap("T16", "distractor", ["gmail"], [], [BASE["tilting_ack"]], "R1", "Tilting Point is a publisher we approached", "its UA fund form was for Zombie Match", distractor_type="scope_adjacent"),
 trap("T17", "distractor", ["slack"], [], [BASE["apple_arcade"]], "R1", "Apple Arcade is a dominoes lead", "it isn't on the sheet, and it had already signed someone", distractor_type="keyword_collision"),
 trap("T18", "distractor", ["gdocs"], [], [BASE["partners_doc"]], "R1", "Frederick's Publishing Partners doc is the population", "it's a candidate list; the outreach sheet records who was approached", distractor_type="partial_listing"),
 trap("T19", "distractor", ["gdocs"], [], [BASE["bizdev_doc"]], "R1", "the Biz Dev Notes regional list is the population", "it's an April candidate list with a template", distractor_type="stale_summary"),
 trap("T20", "distractor", ["slack", "gmail"], [], [BASE["lead"]], "R1", "the Sep 24 lead is a publisher to add", "Leonard's mail leaves him out: he only wants hypercasual", distractor_type="withdrawn_ask"),
 trap("T21", "distractor", ["gdocs"], [IDS["codev_doc"]], [], "R4", "the co-dev doc's rules value an offer", "it's about Zombie Match co-dev; the ground rules govern", distractor_type="near_duplicate_record"),
]
mechanism_portfolio = [
 dict(id="DONE", mechanism="A24", prior_family="done_gap", prior_family_reason="v2 trap 1: a paid claim and its missing piece in another service", nodes=["T1", "C1"], requirement="R5",
      natural_reading="Oakline's $10,000 counts as banked", decides=["B_PA", "VQ_PA", "K_r_banked"], controls=["Tallwater Games (no first-look payment, nothing banked)"],
      over_application="over-application marks another offer's advance as unbanked twice", source="slack-reply", signature="Oakline wire SVB returned"),
 dict(id="CORR", mechanism="A11", prior_family="superseding", prior_family_reason="v2 trap 2: a later note in another service changes one number", nodes=["T2", "C2"], requirement="R3",
      natural_reading="the term sheet's advance stands", decides=["A_adv_PB", "V12_PB", "VQ_PB"], controls=["Harbor Lane Games (a call with no change to its terms)"],
      over_application="over-application cuts a control's advance", source="gcal-note", signature="Tallwater advance $40,000"),
 dict(id="ALIAS", mechanism="A7", prior_family="scope_alias", prior_family_reason="v2 trap 6: a person-to-company link in Contacts and a signature", nodes=["T3", "C3"], requirement="R2",
      natural_reading="Moonrail is Live", decides=["S_out_PC", "T_item_PC"], controls=["Wavecrest Play (no founder note about it)"],
      over_application="over-application withdraws a control", source="alias-join", signature="Anika Kestrel Moonrail"),
 dict(id="FILT", mechanism="A17", prior_family="exact_predicate", prior_family_reason="v2 trap 7: in-scope items outside the obvious filter", nodes=["T4", "T5", "C4"], requirement="R1",
      natural_reading="the outreach sheet and the inbox are the population", decides=["S_in_PH", "S_in_PI", "S_total"], controls=["Homa and NCsoft stay out"],
      over_application="over-application adds Homa", source="outside-filter", signature="Copperleaf Redwood outside the sheet"),
 dict(id="EXC", mechanism="A15", prior_family="authority", prior_family_reason="v2 trap 5: a rule in an older record changes the obvious answer", nodes=["T6", "T14", "C5"], requirement="R6",
      natural_reading="value alone decides", decides=["S_out_PD", "S_out_PJ", "R_top"], controls=["Sunfold Mobile (mobile stores only)"],
      over_application="over-application rules a mobile-only offer out", source="sync-record", signature="retain code IP non-mobile"),
 dict(id="INPUT", mechanism="A11", prior_family="superseding", prior_family_reason="v2 trap 8: a changed input to a figure, in a card comment", nodes=["T7", "C6"], requirement="R3",
      natural_reading="the term sheet's commitment feeds the forecast", decides=["A_com_PE", "V12_PE", "R_top"], controls=["Oakline Games (its card comment changes no term)"],
      over_application="over-application cuts a control's installs", source="card-comment", signature="Sunfold 30,000 installs"),
 dict(id="DATE", mechanism="A4", prior_family="effective_date", prior_family_reason="v2 trap 4: a moved date changes which payments land in the window", nodes=["T9", "C7"], requirement="R5",
      natural_reading="signing is Oct 31", decides=["VQ_PF", "VQ_PG"], controls=["Sunfold Mobile (net 45 lands Dec 29 either way)"],
      over_application="over-application pushes a net-45 payment out of Q4", source="esg-thread", signature="Nov 14 signing"),
 dict(id="FOLLOW", mechanism="A15", prior_family="authority", prior_family_reason="v2 trap 3: a write a standing line requires", nodes=["T8", "C8"], requirement="R12",
      natural_reading="no note is owed", decides=["W_count", "W_1", "W_2", "W_3"], controls=["Oakline Games (got Intro only, so no note)"],
      over_application="over-application drafts a note to an Intro-only publisher", source="bridge-reply", signature="May one-pager organic note"),
]
channels = [
 dict(id="CH-DONE", kind="member", rule="DONE", degrade="Oakline's $10,000 treated as banked", members=["Oakline Games"], latent="slack reply read", family="done_gap"),
 dict(id="CH-CORR", kind="member", rule="CORR", degrade="term-sheet advance kept", members=["Tallwater Games"], latent="calendar note read", family="superseding"),
 dict(id="CH-ALIAS", kind="member", rule="ALIAS", degrade="Moonrail kept Live", members=["Moonrail Studios"], latent="alias join", family="scope_alias"),
 dict(id="CH-FILT1", kind="member", rule="FILT", degrade="Copperleaf missing", members=["Copperleaf Games"], latent="relay found", family="exact_predicate"),
 dict(id="CH-FILT2", kind="member", rule="FILT", degrade="Redwood missing", members=["Redwood Arcade"], latent="ticket comment found", family="exact_predicate"),
 dict(id="CH-EXC", kind="member", rule="EXC", degrade="rights position not applied", members=["Northglow Publishing", "Pinegrove Games"], latent="rights record applied", family="authority"),
 dict(id="CH-INPUT", kind="member", rule="INPUT", degrade="term-sheet installs kept", members=["Sunfold Mobile"], latent="card comment read", family="superseding"),
 dict(id="CH-DATE", kind="member", rule="DATE", degrade="Oct 31 signing kept", members=["Harbor Lane Games", "Wavecrest Play"], latent="ESG thread read", family="effective_date"),
 dict(id="CH-FOLLOW", kind="member", rule="FOLLOW", degrade="no drafts", members=["Tallwater Games", "Harbor Lane Games", "Wavecrest Play"], latent="standing line read", family="authority"),
 dict(id="CH-SLIP", kind="slip", degrade="base slip on control rows", slots=["S_live_PA", "S_live_PG", "S_passed_1", "S_silent_1", "V12_PF"]),
]
chains = [
 dict(id="C1", root_cause="A24", ends_in="R5", hops=[dict(service="gmail", record=thr("Oakline Games"), finding="Marek confirms the wire"), dict(service="trello", record=IDS["oakline_card_comment"], finding="the card repeats it"), dict(service="slack", record=IDS["arthur_cash"], finding="it never hit SVB")]),
 dict(id="C2", root_cause="A11", ends_in="R3", hops=[dict(service="gdocs", record=term("Tallwater Games"), finding="$60,000"), dict(service="gcal", record=IDS["pb_event"], finding="$40,000 on the call"), dict(service="gsheets", record="model", finding="advance, value and Q4 cash follow")]),
 dict(id="C3", root_cause="A7", ends_in="R2", hops=[dict(service="gmail", record=thr("Moonrail Studios"), finding="Anika's signature names Kestrel"), dict(service="contacts", record=IDS["anika_contact"], finding="her row says Kestrel Group"), dict(service="slack", record=IDS["kestrel_post"], finding="Kestrel's offer is off")]),
 dict(id="C4", root_cause="A17", ends_in="R1", hops=[dict(service="gdocs", record=RD, finding="anyone who came to the four of us"), dict(service="slack", record=IDS["arthur_analytics"], finding="a publisher's tech lead, notes on ENG-2362"), dict(service="linear", record=IDS["eng2362_comment"], finding="Redwood's terms")]),
 dict(id="C5", root_cause="A15", ends_in="R6", hops=[dict(service="gdocs", record=term("Northglow Publishing"), finding="all digital storefronts"), dict(service="slack", record=BASE["rights_post"], finding="keep code, IP and non-mobile rights"), dict(service="gdocs", record=RD, finding="Out on rights")]),
 dict(id="C6", root_cause="A13", ends_in="R3", hops=[dict(service="gdocs", record=term("Sunfold Mobile"), finding="50,000 a month"), dict(service="trello", record=IDS["sunfold_card"], finding="card titled by Lena's first name"), dict(service="trello", record=IDS["sunfold_comment"], finding="30,000 a month")]),
 dict(id="C7", root_cause="A4", ends_in="R5", hops=[dict(service="gdocs", record=RD, finding="Oct 31, unless ESG says later"), dict(service="gmail", record=IDS["esg_thread"], finding="Nov 14"), dict(service="gdocs", record=term("Harbor Lane Games"), finding="net 60 lands Jan 13")]),
 dict(id="C8", root_cause="A14", ends_in="R12", hops=[dict(service="gdocs", record=RD, finding="what I've said still applies"), dict(service="slack", record=IDS["standing_line"], finding="a note to anyone Live who got the one-pager"), dict(service="gsheets", record=IDS["outreach_sheet"], finding="who got it")]),
]
B = lambda phase, svc, n, why: dict(phase=phase, service=svc, calls=n, reason=why)
call_budget = [
 B("discovery", "gmail", 3, "read Leonard's ask; open the ESG thread; open Oakline's payment mail"),
 B("discovery", "gdocs", 3, "read the ground rules doc and the August sync; reject the co-dev doc"),
 B("discovery", "gsheets", 2, "read the outreach sheet's tabs"),
 B("discovery", "gdrive", 3, "list the DD publishing folder; find term sheets"),
 B("discovery", "slack", 4, "search founder talk on publishing, numbers and rights"),
 B("discovery", "trello", 3, "read the board, the BD Follow Up list and the DD publishing card"),
 B("discovery", "snowflake", 4, "list and describe the table; query three months of revenue"),
 B("enumeration", "gmail", 6, "census threads since Apr 1 by publisher, offer and rights terms"),
 B("enumeration", "slack", 5, "census publisher talk; Slack search has no bulk read of replies"),
 B("enumeration", "gcal", 3, "list calls in the window; read Monday's sit-down"),
 B("enumeration", "linear", 3, "follow the pointer to ENG-2362 and its comments"),
 B("enumeration", "contacts", 2, "list contacts; resolve people named in posts"),
 B("per-record", "gmail", 18, "each publisher's thread (three quarters of a call each, bulk reads discounted)"),
 B("per-record", "gdocs", 8, "each term sheet: terms and rights"),
 B("per-record", "slack", 26, "a search per publisher, since a later founder note can change its standing"),
 B("per-record", "gcal", 9, "a search per Live or Out offer for a call note"),
 B("per-record", "contacts", 10, "a lookup before each add (two already exist)"),
 B("per-record", "trello", 4, "read comments on the existing follow-up cards"),
 B("writes", "gsheets", 5, "create the model, write two tabs, move it into the folder"),
 B("writes", "contacts", 17, "a contact for each publisher person who has written to us, minus two that exist"),
 B("writes", "trello", 32, "six checklists and one item per publisher"),
 B("writes", "trello", 17, "15 new follow-up cards and comments on two existing ones"),
 B("writes", "gcal", 7, "a reminder on each Live offer's response date"),
 B("writes", "gmail", 4, "three follow-through drafts and the reply"),
 B("read-back", "gsheets", 2, "check the model"),
 B("read-back", "trello", 1, "check the card"),
]
TOTAL_BUDGET = sum(r["calls"] for r in call_budget)
writes = [
 dict(service="gsheets", tool="gsheets_create_spreadsheet+gsheets_values_update+gdrive_move_file", count=5, depends_on=["K1", "K2", "K5", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T9"], requirements=["R1", "R2", "R3", "R4", "R5", "R7", "R8"]),
 dict(service="trello", tool="trello_create_checklist+trello_create_check_item", count=32, depends_on=["K4", "C3", "C4", "C5"], requirements=["R9"]),
 dict(service="trello", tool="trello_create_card+trello_add_comment", count=17, depends_on=["K4", "T10", "C3", "C4", "C5"], requirements=["R9"]),
 dict(service="contacts", tool="contacts_add_new_contact", count=17, depends_on=["K15", "C4"], requirements=["R10"]),
 dict(service="gcal", tool="gcal_create_event", count=7, depends_on=["K1", "C3", "C4", "C5"], requirements=["R11"]),
 dict(service="gmail", tool="gmail_create_draft", count=3, depends_on=["K9", "C8"], requirements=["R12"]),
 dict(service="gmail", tool="gmail_reply_to_message", count=1, depends_on=["K1", "C1", "C2", "C4", "C5", "C6"], requirements=["R13"]),
]
CONFIRM = ("task author in chat on 2026-11-06: 'my task is a long horizon task soo i want over 130 tool calls in each runs and also i want difficulty pass rate under 80% and also have to folllow "
           "all other difficulty guidelines soo you can choose from your self which option is best fit for my requirements in this task'")
PER_RECORD = int(sum(s["per_record_calls"] * s["records"] for s in cohort["evidence_surfaces"]))
manifest = dict(
 _note="Draft manifest for /create-injection. Seeded ids are minted here; injection keeps them or records design_delta.",
 persona="frederick_stone",
 assignment_context={k: CTX[k] for k in ("context_hash", "assignment_hash", "policy_hash", "freeze_utc", "difficulty_mode")},
 horizon="Long Horizon", effective_profile="extreme",
 author_targets={"min_calls_per_run": 130, "max_avg_weighted_pass": 0.80, "requester_confirmation": CONFIRM},
 volume_exception={"reason": "26 publishers and 9 sets of terms; mail and calendars are bulk-readable, so honest necessary calls are about 190. Reaching 500 would need padding, which fails on its own",
                   "requester_confirmation": CONFIRM, "call_budget_floor": 180, "per_record_floor": 60},
 cohort_exception={"reason": "no natural 40-record publisher cohort exists; padding it would add always-pass rows that cut the SD", "requester_confirmation": CONFIRM, "cohort_floor": 24},
 requirements=requirements, services=services, anchors=anchors, ask_fragments=ask_fragments, authorities=authorities, cohort=cohort, chains=chains, traps=traps,
 mechanism_portfolio=mechanism_portfolio, channels=channels, call_budget=call_budget, writes=writes,
 hazard_acknowledgements=[
  {"hazard_id": "Q01", "resolution": "dated_claim", "requirement": "R5", "why_safe": "seeded replies under three base roots change reply_count and latest_reply; SQL updates those counters as companions and each text is an attributed, dated claim"},
 ],
 denied_probes=[], gradable_surface="01_Gradable_Surface.json", design_delta=[],
)
json.dump(manifest, open(os.path.join(WF, "01_Hardness_Manifest.draft.json"), "w"), indent=1, ensure_ascii=False)

# ---------------------------------------------------------------- gradable surface
S = []
def slot(id, title, w, kind, reason, cls, sel, role="core", mechs=(), **k):
    d = dict(id=id, title=title, weight=w, work_kind=kind, work_reason=reason, **{"class": cls}, selector=sel, role=role, mechanisms=list(mechs)); d.update(k); S.append(d)
MS, IP, LU = "multi_source_reconciliation", "interpretation", "lookup"
F = lambda key, col: ["field", key, col]
slot("K_home", "model in his folder", 1, LU, "folder named by Leonard", "delivery", ["delivery", "register_parent", IDS["dd_folder"]])
slot("K_reply", "reply on Leonard's thread", 1, LU, "reply on the hub", "delivery", ["delivery", "email_reply", "hub-message"])
slot("S_total", "publishers on the model", 5, MS, "sheet plus records in Slack and Linear, by the rule", "delivery", ["delivery", "register_keys_exact"], role="volume", volume_for=["Live", "Passed", "No reply", "Waiting on us"], mechs=["FILT"], fact_id="population")
slot("S_in_PH", "Copperleaf on the model", 5, MS, "relay in a Slack thread joined to the rule", "direct", F("Copperleaf Games", "Status"), role="sample", group="Live", mechs=["FILT"])
slot("S_in_PI", "Redwood on the model", 5, MS, "Slack pointer, Linear comment and the rule", "direct", F("Redwood Arcade", "Status"), role="sample", group="Live", mechs=["FILT"])
slot("S_live_PA", "Oakline Live", 3, IP, "rule applied to one thread and sheet", "direct", F("Oakline Games", "Status"), role="sample", group="Live")
slot("S_live_PG", "Wavecrest Live", 3, IP, "rule applied to one thread and sheet", "direct", F("Wavecrest Play", "Status"), role="sample", group="Live")
slot("S_out_PC", "Moonrail Withdrawn", 5, MS, "mail signature, Contacts and a founder post joined", "direct", F("Moonrail Studios", "Status"), role="exception", singled_out_by="K11", mechs=["ALIAS"])
slot("S_out_PD", "Northglow Out on rights", 5, MS, "term sheet joined to the August sync", "direct", F("Northglow Publishing", "Status"), role="exception", singled_out_by="H2", mechs=["EXC"])
slot("S_out_PJ", "Pinegrove Out on rights", 5, MS, "term sheet joined to the August sync", "direct", F("Pinegrove Games", "Status"), role="exception", singled_out_by="H2", mechs=["EXC"])
for i, k in enumerate(["Fernhollow Media", "Slatewood Mobile", "Tidewell Studios"], 1):
    slot(f"S_passed_{i}", f"{k} Passed", 3, IP, "rule applied to one thread", "direct", F(k, "Status"), role="sample", group="Passed")
for i, k in enumerate(["Summit Mobile", "Orchard Lane Games", "Bellwether Arcade"], 1):
    slot(f"S_silent_{i}", f"{k} No reply", 3, IP, "rule applied to one thread; Summit's is an automatic acknowledgement", "direct", F(k, "Status"), role="sample", group="No reply")
for i, k in enumerate(["Rayking Game", "Appodeal", "Kitebridge Games"], 1):
    slot(f"S_wait_{i}", f"{k} Waiting on us", 3, IP, "rule applied to one thread", "direct", F(k, "Status"), role="sample", group="Waiting on us")
slot("A_adv_PB", "Tallwater advance", 5, MS, "term sheet against the calendar note", "direct", F("Tallwater Games", "Advance"), mechs=["CORR"])
slot("A_com_PE", "Sunfold monthly installs", 5, MS, "term sheet against the card comment", "direct", F("Sunfold Mobile", "Monthly installs"), mechs=["INPUT"])
slot("A_adv_PH", "Copperleaf advance", 3, IP, "read from a pasted note", "direct", F("Copperleaf Games", "Advance"), mechs=["FILT"])
slot("A_adv_PI", "Redwood advance", 3, IP, "read from a ticket comment", "direct", F("Redwood Arcade", "Advance"), mechs=["FILT"])
slot("A_share_PF", "Harbor Lane rev share", 1, LU, "one term sheet", "direct", F("Harbor Lane Games", "Rev share"))
for k, w, kd, ms, r in [("Tallwater Games", 5, MS, ["CORR"], "formula on a corrected input"), ("Sunfold Mobile", 5, MS, ["INPUT"], "formula on a corrected input"),
                        ("Copperleaf Games", 5, MS, ["FILT"], "formula on terms outside the sheet"), ("Redwood Arcade", 5, MS, ["FILT"], "formula on terms outside the sheet"),
                        ("Oakline Games", 3, "calculation", [], "formula on one term sheet"), ("Harbor Lane Games", 3, "calculation", [], "formula on one term sheet"), ("Wavecrest Play", 3, "calculation", [], "formula on one term sheet")]:
    slot("V12_" + k.split()[0], f"{k} 12-month value", w, kd, r, "aggregate", F(k, "12-month value"), mechs=ms)
for k, w, kd, ms, r in [("Oakline Games", 5, MS, ["DONE"], "mail and card against Arthur's note"), ("Harbor Lane Games", 5, MS, ["DATE"], "net 60 from the moved signing date"), ("Wavecrest Play", 5, MS, ["DATE"], "net 60 from the moved signing date"),
                        ("Tallwater Games", 3, "calculation", ["CORR"], "corrected advance, net 30"), ("Sunfold Mobile", 3, "calculation", [], "net 45 lands either way")]:
    slot("VQ_" + k.split()[0], f"{k} Q4 cash", w, kd, r, "aggregate", F(k, "Q4 cash"), mechs=ms)
slot("B_PA", "Oakline banked", 5, MS, "wire confirmation against Arthur's note", "direct", F("Oakline Games", "Banked"), mechs=["DONE"], fact_id="banked")
slot("V_keep", "keep value", 3, "calculation", "three warehouse months under the rule", "aggregate", ["text", "summary", r".*12,?72[34].*"], fact_id="keep")
slot("R_top", "first pick", 5, "deeper_reasoning", "the ranking after every correction", "aggregate", ["text", "summary", r".*[Cc]opperleaf.*"], mechs=["EXC", "INPUT", "FILT"], fact_id="pick")
slot("T_chk_live", "Live checklist size", 5, MS, "the status work across services, on the board", "aggregate", ["text", "checklists", r".*Live.*"], mechs=["ALIAS", "EXC", "FILT"], fact_id="live_count")
slot("T_chk_passed", "Passed checklist size", 3, "comparison", "count from threads", "aggregate", ["text", "checklists", r".*Passed.*"], fact_id="passed_count")
slot("T_chk_silent", "No reply checklist size", 3, "comparison", "count from threads", "aggregate", ["text", "checklists", r".*No reply.*"], fact_id="silent_count")
slot("T_chk_wait", "Waiting checklist size", 3, "comparison", "count from threads", "aggregate", ["text", "checklists", r".*Waiting.*"], fact_id="wait_count")
slot("T_item_PC", "Moonrail on the Withdrawn checklist", 5, MS, "same join, on the board", "write_content", ["text", "checklist_items", r".*Moonrail.*"], mechs=["ALIAS"], fact_id="moonrail_item")
slot("T_item_PH", "Copperleaf item", 5, MS, "same join, on the board", "write_content", ["text", "checklist_items", r".*Copperleaf.*"], mechs=["FILT"], fact_id="copperleaf_item")
slot("T_item_PI", "Redwood item", 5, MS, "same join, on the board", "write_content", ["text", "checklist_items", r".*Redwood.*"], mechs=["FILT"], fact_id="redwood_item")
slot("T_cards", "new follow-up cards", 3, "comparison", "count after reuse", "aggregate", ["text", "cards", r".*F/up with.*"], mechs=["ALIAS", "EXC", "FILT"], fact_id="card_count")
for i, k in enumerate(["Silverlake Mobile", "Kitebridge Games", "Harbor Lane Games"], 1):
    slot(f"T_card_{i}", f"follow-up card for {k}", 3, IP, "status decides the card", "write_content", ["text", "cards", f".*{k.split()[0]}.*"], fact_id=f"card_{i}")
slot("T_reuse_PE", "comment on Lena's card", 3, IP, "first-name card mapped to Sunfold", "write_content", ["text", "comments", r".*(Live|live).*"], fact_id="reuse_lena")
slot("C_vol", "contacts added", 3, "comparison", "count after skipping two", "aggregate", ["text", "contacts", r".*(Copperleaf|Redwood).*"], mechs=["FILT"], fact_id="contact_count", role="volume", volume_for=["contacts"])
for i, k in enumerate(["Paola", "Diego", "Rhys"], 1):
    slot(f"C_{i}", f"contact for {k}", 1, LU, "one signature", "write_content", ["text", "contacts", f".*{k}.*"], role="sample", group="contacts", fact_id=f"contact_{i}")
slot("M_vol", "reminders added", 3, "comparison", "one per Live offer", "aggregate", ["text", "events", r".*(Copperleaf|Redwood).*"], mechs=["ALIAS", "EXC", "FILT"], fact_id="reminder_count", role="volume", volume_for=["reminders"])
for i, (k, d) in enumerate([("Tallwater", "2025-10-17"), ("Wavecrest", "2025-10-31")], 1):
    slot(f"M_{i}", f"reminder for {k}", 1, LU, "one term sheet's date", "write_content", ["text", "events", f".*{d}.*"], role="sample", group="reminders", fact_id=f"reminder_{i}")
slot("W_count", "drafts owed", 5, MS, "standing line joined to the sheet and to status", "aggregate", ["text", "drafts", r".*0\.50.*"], mechs=["FOLLOW", "ALIAS"], fact_id="draft_count")
for i, k in enumerate(["Tallwater", "Harbor Lane", "Wavecrest"], 1):
    slot(f"W_{i}", f"draft to {k}", 5, MS, "standing line joined to the sheet and to status, per target", "write_content", ["text", "drafts", f".*{k.split()[0]}.*"], mechs=["FOLLOW"], fact_id=f"draft_{i}")
slot("K_r_top", "first pick in the reply", 3, IP, "states the pick", "write_content", ["text", "replies", r".*[Cc]opperleaf.*"], mechs=["EXC", "INPUT", "FILT"], fact_id="pick")
slot("K_r_value", "its 12-month value in the reply", 3, IP, "states the value", "write_content", ["text", "replies", r".*67,?200.*"], mechs=["EXC", "INPUT", "FILT"], fact_id="pick_value")
slot("K_r_q4", "its Q4 cash in the reply", 3, IP, "states the Q4 cash", "write_content", ["text", "replies", r".*32,?000.*"], mechs=["EXC", "INPUT", "FILT"], fact_id="pick_q4")
slot("K_r_banked", "money banked in the reply", 5, MS, "wire confirmation against Arthur's note", "write_content", ["text", "replies", r".*(\$0|nothing|none|no publisher money).*"], mechs=["DONE"], fact_id="banked")
for k in ("sheet", "checklists", "cards", "drafts"):
    slot(f"P_{k}", f"reply after the {k}", 1, LU, "order of the writes", "delivery", ["delivery", "email_reply", "hub-message"], fact_id=f"order_{k}")
surface = dict(kind="GRADABLE_SURFACE", version=1, task="frederick_dd_publishing", revision="design-1", truth_keys=[m["key"] for m in M], classes=list(COUNTS),
               truth_fields={"class": "Status", "groups": "groups"},
               deliverables={"model": {"kind": "table", "name_regex": "(?i).*dd publishing model.*", "key_column": "Publisher", "key_regex": ".+",
                                       "columns": ["Publisher", "Status", "Rev share", "Advance", "Monthly installs", "12-month value", "Q4 cash", "Banked"], "class_column": "Status", "reason_column": "Status",
                                       "comparators": {"Status": "norm"}},
                             "summary": {"kind": "json_text", "tool": "gsheets_values_update"}, "replies": {"kind": "json_text", "tool": "gmail_reply_to_message"}, "drafts": {"kind": "json_text", "tool": "gmail_create_draft"},
                             "events": {"kind": "json_text", "tool": "gcal_create_event"}, "cards": {"kind": "json_text", "tool": "trello_create_card"}, "comments": {"kind": "json_text", "tool": "trello_add_comment"},
                             "checklists": {"kind": "json_text", "tool": "trello_create_checklist"}, "checklist_items": {"kind": "json_text", "tool": "trello_create_check_item"}, "contacts": {"kind": "json_text", "tool": "contacts_add_new_contact"}},
               slots=S)
json.dump(surface, open(os.path.join(WF, "01_Gradable_Surface.json"), "w"), indent=1, ensure_ascii=False)
json.dump(dict(IDS=IDS, BASE=BASE, T=T), open(os.path.join(HERE, "ids.json"), "w"), indent=1)
if __name__ == "__main__":
    tw = sum(s["weight"] for s in S); fl = sum(s["weight"] for s in S if s["mechanisms"])
    print("rows", len(S), "weight", tw, "flippable", fl, f"{fl/tw:.1%}", "budget", TOTAL_BUDGET, "per-record", PER_RECORD, "keep", KEEP_VALUE)
    print({m["key"]: m["v12"] for m in TRUTH}, COUNTS)
