#!/usr/bin/env python3
"""Builds the /create-scenario draft manifest and gradable surface for the Frederick bridge-pipeline task.
Design only (no prompt, OE or criterion text). Seeded ids are minted here and carried unchanged into /create-injection."""
import json
from datetime import datetime, timezone
from pathlib import Path

WF = Path(__file__).resolve().parents[1]
CTX = json.loads((WF / "00_Task_Context.json").read_text())


def thrid(iso: str, k: int = 0) -> str:
    """Gmail X-GM-THRID style id: ms timestamp << 20 (+ k), as the base thread ids are."""
    ms = int(datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp() * 1000)
    return str((ms << 20) + k)


FRED = "frederick.stone@harmonygames.co"
# ---------------------------------------------------------------- minted seeded ids (planned; collision-checked at S2)
HUB_AT = "2025-09-30T21:05:00Z"
G_HUB = f"{FRED}/{thrid(HUB_AT, 11)}"                    # Leonard's ask (anchor + hub)
G_ANTON = f"{FRED}/{thrid('2025-09-24T16:10:00Z', 23)}"   # Anton trims to $25K (INPUT)
G_DS_ANTON = f"{FRED}/{thrid('2025-09-26T19:02:00Z', 31)}"  # signing service: completed (Anton)
G_DS_PAUL = f"{FRED}/{thrid('2025-09-29T15:00:00Z', 37)}"   # signing service: reminder, awaiting signature (Paul)
G_HIRO = f"{FRED}/{thrid('2025-09-26T09:40:00Z', 41)}"    # Edith Vane (Hiro) pass, no firm name in body
G_DENTSU = f"{FRED}/{thrid('2025-09-26T17:20:00Z', 47)}"  # Leonard: invites out to all three (DONE2 'done' source)
G_BRIGHT = f"{FRED}/{thrid('2025-09-25T22:30:00Z', 53)}"  # Leonard follow-up to Ilse Marrow after the call
G_ROBERT_ASK = f"{FRED}/{thrid('2025-09-29T18:20:00Z', 59)}"  # Robert: just email the board (withdrawn by the hub)
S_EXEC_ANGELS = "C07C2866011/1758303600.418207"           # #executives 2025-09-19T17:40Z Leonard: angels 'are in'
S_BP_ROBERT_ROOT = "C096HFA5Z8W/1759161600.226431"        # #bridge-pitch 2025-09-29T16:00Z Robert: phone notes go in threads
S_BP_SCIPLAY_REPLY = "C096HFA5Z8W/1759184040.552871"      # reply in thread 1757716998.377299, 2025-09-29T22:14Z
S_EXEC_ARTHUR = "C07C2866011/1759168800.117903"           # #executives 2025-09-29T18:00Z Arthur: 'just list who Leonard emailed'
DOC_TEMPLATE = "f_3b9e61c04d7a52e8f1a6c2"                 # Board pre-read - fundraising section (Oct 14) template
DOC_TEMPLATE_OLD = "f_8d2c47a91e05b3f6d7c418"             # July template (decoy, superseded)
DOC_README = "f_c61a0e93b7d24f58a2e917"                   # README - Oct 14 board materials (in the Board folder)
DRIVE_FOLDER = "d_5e8a1c3f9b07d2e64a1b93"                 # Board - Oct 14 2025 folder (owner Frederick)
DECK_DRAFT = "f_a47d0e2c95b18f63e2c0d5"                   # HG BoD Oct 14 2025 (draft) deck
EVT_REVIEW = "evt_9c41e7a2d05b38f6e1a7c4"                 # Mon Oct 6 pre-read review (Leonard + Frederick)
EVT_BRIGHT = "evt_2f86b0d4c9e17a35b64e0d"                 # Thu Sep 25 'Ilse Marrow and Leonard Hayes'
LIN_TESTERS = "ZOM-567"                                    # Arthur: investor testers on ZM internal tracks
TR_KEEPWARM_COMMENT = "68c6b2a4f19e03d7c5a81b2e"          # Leonard comment on Existing Investor Update card
TR_BOARDDECK_COMMENT = "68d81f30a6c94e2b7d05e1f4"         # Leonard comment on Board Deck card (Oct 14 slide)
CT_EDITH = "e3a91c07d5b48f26a0c7e314"                     # Contacts: Edith Vane - Partner, Hiro Capital
CT_ILSE = "b72f0d6e19c3a84e5d21f9a0"                      # Contacts: Ilse Marrow - Principal, Brightwater Games Fund
CT_KARTHIC = "5d0e8b31f7a29c64e1b0d3a8"                   # Contacts: Karthic R - T-Accelerate Capital (PXLite fund)

# base records (verified through the synth-cut export)
B_LIST = "f_48247af79428823c3cac92"; B_LIST_2024 = "f_0b29566cd7932a205d54d2"
B_SCIPLAY = f"{FRED}/1842285743246816270"; B_LVP = f"{FRED}/1842277743427687737"
B_HIRO = f"{FRED}/1842278425320449096"; B_TACC = f"{FRED}/1842283406259093714"
B_BUBBLES = f"{FRED}/1843978997950200606"; B_DENTSU = f"{FRED}/1843473831194478743"
B_HOMA_INV = f"{FRED}/1843169166284025277"; B_HOMA_FU = f"{FRED}/1843552279434086285"
B_BP_TRACKER = "C096HFA5Z8W/1757345124.546449"; B_BP_ROOT_0912 = "C096HFA5Z8W/1757716998.377299"
B_BP_HOMA = "C096HFA5Z8W/1758210489.170809"; B_BP_ARTHUR_PLAY = "C096HFA5Z8W/1758677722.184129"
B_EVT_HOMA = "evt_89381fe5a15b802c5652a9"; B_EVT_SCIPLAY = "evt_25c9ee60d4b6c8f6d39a74"
B_EVT_LVP = "evt_e59dc0a675d0c407b79acf"; B_EVT_DENTSU_A = "evt_3671b9a924ccba550e51fa"
B_EVT_DENTSU_B = "evt_eeca6fc7670fe1acd94440"; B_EVT_BOARD = "evt_bd61f3209523d19fdd6ba2"
B_CARD_KEEPWARM = "68c5a49e8491a9d7faf869d0"; B_CARD_BOARDDECK = "67f446b4b0817af30d2d63f6"
B_CARD_INVUPDATE_OLD = "663ea0fc3f231e879cefd5e8"

REQ = {
    "R1": "register population: one row per firm on the 2025 game investor list (duplicate list rows are one firm) plus "
          "every firm not on the list that we had a call or meeting with since the Sep 3 kickoff (Homa; Brightwater Games "
          "Fund); service, publishing and competitor talks are out; 79 firms; each firm's status and last two-way contact "
          "date; whether a firm had a call is read from the calendar and mail",
    "R2": "status per firm as of end of day Tue Sep 30 Pacific, in the template's buckets (Passed, In talks, Awaiting "
          "reply, Not contacted this round); a pass one of us heard by phone counts once it is written in #bridge-pitch; "
          "a partner's reply counts for the firm the contacts and earlier threads tie them to",
    "R3": "committed and soft-circled amounts per firm and in total: committed means a signed SAFE (the signing service "
          "shows it completed), soft-circled means a written yes with an amount that is not signed yet, at the latest "
          "amount the investor gave; committed total $25,000 (Anton Bernstein), soft-circled $50,000 (Paul Heydon)",
    "R4": "build access for each firm in talks: whether they are testers on the current Zombie Match 3D build on iOS "
          "(TestFlight) and Android (Play internal test track) per the tester tracking ticket; Dentsu iOS only",
    "R5": "register saved as one Google Sheet in Frederick's Board - Oct 14 2025 folder, named for the fundraising "
          "section",
    "R6": "every firm that passed after a pitch call or meeting this round goes on the keep-warm checklist of the "
          "Existing Investor Update card (LVP, SciPlay, Hiro Capital; a16z accepted either way)",
    "R7": "reply on Leonard's ask thread with the numbers the draft deck's fundraising slide needs: firms on the "
          "register, committed total and soft-circled total; to Leonard on his thread, not to the board",
}

SERVICES = {
    "gmail": {"role": "anchor ask (hub) and reply destination; investor threads cc'd to Frederick; signing-service "
                      "notices; Anton's amount change; Edith Vane's pass; Leonard's Dentsu 'invites are out' mail",
              "weight_reason": "the ask, the signing state of each SAFE, the latest angel amount and the Hiro pass live only in mail"},
    "slack": {"role": "#bridge-pitch trackers and Robert's phone-note thread reply (SciPlay pass); #executives angel post",
              "weight_reason": "SciPlay's pass exists only as Robert's thread reply; the convincing 'angels are in' post is here"},
    "gsheets": {"role": "2025 game investor list (population, stale Latest Status); the register write",
                "weight_reason": "the population is the list; the register is the deliverable"},
    "gdocs": {"role": "H1 board pre-read template (status buckets, committed vs soft-circled, build access, as-of); "
                      "July template decoy; Board folder README",
              "weight_reason": "every status, money and access definition lives only in the template"},
    "gcal": {"role": "pitch calls since Sep 3 (Homa, Brightwater, Hiro, SciPlay, LVP...); Oct 6 review event",
             "weight_reason": "off-list firms are found only through calendar calls titled by a person"},
    "contacts": {"role": "partner-to-firm mappings (Edith Vane - Hiro Capital; Ilse Marrow - Brightwater; Karthic - T-Accelerate/PXLite)",
                 "weight_reason": "Hiro's pass and Brightwater's call name only a person; contacts tie them to the firm"},
    "trello": {"role": "H2 keep-warm rule on the Existing Investor Update card (+ checklist write); Board Deck card comment",
               "weight_reason": "the follow-through rule and the slide's number list live only on the cards"},
    "linear": {"role": "ZOM-567 investor tester tracking (Dentsu Play track not added)",
               "weight_reason": "Dentsu's missing Android access exists only in the ticket"},
    "gdrive": {"role": "Board - Oct 14 2025 folder owned by Frederick (register destination)",
               "weight_reason": "the folder is the required destination"},
    "gslides": {"role": "HG BoD Oct 14 2025 (draft) deck: the fundraising slide's notes say what the table needs",
                "weight_reason": "the register's columns (status + last two-way contact date) are named only in the deck notes"},
}

ANCHORS = [{"id": "A1", "service": "gmail", "record": G_HUB, "locator": G_HUB,
            "prompt_reference": "Leonard's board pre-read email", "requirement_ids": ["R7"]}]


def frag(fid, svc, container, locator, seeded, via, dby, quote, reqs, names=(), base=()):
    return {"id": fid, "service": svc, "container": container, "locator": locator, "kind": "requirement",
            "incorporated_via": via, "seeded_ids": list(seeded), "base_pointers": list(base),
            "delegated_by_record": dby, "delegation_quote": quote, "requirement_ids": reqs,
            "names_authorities": [{"id": a, "quote": q} for a, q in names]}


FRAGS = [
    frag("K1", "gmail", G_HUB, G_HUB, [G_HUB], ["A1"], G_HUB,
         "reply here with the numbers the fundraising slide needs", ["R7"]),
    frag("K2", "gmail", G_HUB, G_HUB, [G_HUB], ["A1"], G_HUB,
         "put the sheet in your Board - Oct 14 2025 folder", ["R5"]),
    frag("K3", "gmail", G_HUB, G_HUB, [G_HUB], ["A1"], G_HUB,
         "every firm on the 2025 game investor list, plus anyone we've had a call with since the Sep 3 kickoff who isn't on it",
         ["R1"], names=[("H1", "use the buckets and definitions in the board pre-read template")]),
    frag("K4", "gdocs", DOC_TEMPLATE, DOC_TEMPLATE, [DOC_TEMPLATE], ["A1"], G_HUB,
         "use the buckets and definitions in the board pre-read template", ["R2"]),
    frag("K5", "gdocs", DOC_TEMPLATE, DOC_TEMPLATE, [DOC_TEMPLATE], ["A1"], G_HUB,
         "use the buckets and definitions in the board pre-read template", ["R3"]),
    frag("K6", "gdocs", DOC_TEMPLATE, DOC_TEMPLATE, [DOC_TEMPLATE], ["A1"], G_HUB,
         "use the buckets and definitions in the board pre-read template", ["R4"]),
    frag("K7", "gsheets", B_LIST, B_LIST, [], ["A1"], G_HUB,
         "every firm on the 2025 game investor list", ["R1"], base=[B_LIST]),
    frag("K8", "slack", "C096HFA5Z8W", S_BP_ROBERT_ROOT, [S_BP_ROBERT_ROOT], ["K4"], DOC_TEMPLATE,
         "a pass one of us heard by phone counts once it is written in #bridge-pitch", ["R2"]),
    frag("K9", "trello", B_CARD_KEEPWARM, f"trello:{B_CARD_KEEPWARM}", [TR_KEEPWARM_COMMENT], ["A1"], G_HUB,
         "whatever the Existing Investor Update card says to do for firms that pass, do that too", ["R6"],
         names=[("H2", "whatever the Existing Investor Update card says to do for firms that pass")]),
    frag("K10", "trello", B_CARD_BOARDDECK, f"trello:{B_CARD_BOARDDECK}", [TR_BOARDDECK_COMMENT], ["K1"], G_HUB,
         "the Board Deck card says which numbers the slide takes", ["R7"]),
    frag("K11", "gslides", DECK_DRAFT, DECK_DRAFT, [DECK_DRAFT], ["K10"], TR_BOARDDECK_COMMENT,
         "Slide 9 of the draft deck lists the table's columns", ["R1"]),
    frag("K12", "gcal", EVT_REVIEW, EVT_REVIEW, [EVT_REVIEW], ["A1"], G_HUB,
         "I put Monday's review on your calendar", ["R5"]),
    frag("K13", "gdocs", DOC_README, DOC_README, [DOC_README], ["K2"], G_HUB,
         "the README in that folder says how to name it", ["R5"]),
    frag("K14", "linear", LIN_TESTERS, f"linear:{LIN_TESTERS}", [LIN_TESTERS], ["K6"], DOC_TEMPLATE,
         "build access is whatever Arthur's investor tester ticket in Linear shows", ["R4"]),
]

AUTHS = [
    {"id": "H1", "name": "the board pre-read template (fundraising section)", "home_service": "gdocs",
     "decoy_service": "gdocs", "governs": ["R2", "R3", "R4"], "findable_query": "board pre-read template",
     "seeded_ids": [DOC_TEMPLATE], "base_pointers": [], "decoy_seeded_ids": [DOC_TEMPLATE_OLD], "decoy_base_pointers": [],
     "decoy_scope": {"dimension": "lot", "decoy": "July 2025 board (Q2 lot): committed = a verbal yes from a named investor",
                     "task": "October 14 2025 board (Q3 lot): committed = a signed SAFE"}},
    {"id": "H2", "name": "the keep-warm rule on the Existing Investor Update card", "home_service": "trello",
     "decoy_service": "trello", "governs": ["R6"], "findable_query": "Existing Investor Update",
     "seeded_ids": [TR_KEEPWARM_COMMENT], "base_pointers": [B_CARD_KEEPWARM], "decoy_seeded_ids": [],
     "decoy_base_pointers": [B_CARD_INVUPDATE_OLD],
     "decoy_scope": {"dimension": "issuer", "decoy": "existing investors' quarterly update (Investor Update card, Apr 2025)",
                     "task": "bridge-round prospects that passed after a pitch (Existing Investor Update card)"}},
]

COHORT = {
    "definition": "every firm on the 2025 game investor list (77 unique firms over 80 rows) plus every off-list firm with "
                  "a call or meeting since Sep 3 (Homa, Brightwater Games Fund) = 79",
    "definition_source": [G_HUB, B_LIST],
    "size": 79,
    "evidence_surfaces": [
        {"service": "gmail", "tool": "gmail_search_messages+gmail_get_thread", "per_record_calls": 2.1, "records": 79,
         "requirement": "R2", "decides": "status per firm",
         "why_no_bulk": "gmail_search returns ids only; each firm needs its own query (name, partner) and a thread read for the latest two-way message",
         "short_circuit": "the list's Latest Status stops at 09/11 and Slack trackers stop at Sep 8 - only the firm's own mail gives its state at Sep 30, so no other surface decides the record first"},
        {"service": "slack", "tool": "slack_search_messages+slack_get_thread_replies", "per_record_calls": 1.55, "records": 79,
         "requirement": "R2", "decides": "status per firm",
         "why_no_bulk": "channel history returns roots only; phone notes sit in thread replies under roots about other firms, reachable per firm by search or by opening threads",
         "short_circuit": "a firm whose mail looks active can still have passed by phone (SciPlay); mail cannot rule that out"},
        {"service": "contacts", "tool": "contacts_search_contacts", "per_record_calls": 0.5, "records": 79,
         "requirement": "R1", "decides": "whether a firm had a call",
         "why_no_bulk": "calendar titles and some mails name only a partner; each partner needs a contact lookup to reach the firm",
         "short_circuit": "a partner-titled call or pass cannot be placed on a firm row without the mapping"},
    ],
}


def ver(svc, rid, at, seeded, container=None):
    v = {"service": svc, "id": rid, "seeded": seeded, "at": at}
    if container:
        v["container"] = container
    return v


TRAPS = [
    {"id": "T1", "family": "done_gap", "services": ["slack", "gmail", "gdocs"], "seeded_ids": [S_EXEC_ANGELS, G_DS_PAUL],
     "requirement": "R3", "expected_wrong_reading": "Paul Heydon counted as committed $50,000 because Leonard's #executives post says he 'is in'",
     "resolver": "signing-service reminder: Paul's SAFE still awaiting his signature on Sep 29; the template counts only signed SAFEs",
     "discovery_order": "the #executives post sits in channel history every run reads; the reminder is one notice among many automated mails"},
    {"id": "T2", "family": "done_gap", "services": ["gmail", "linear"], "seeded_ids": [G_DENTSU, LIN_TESTERS],
     "requirement": "R4", "expected_wrong_reading": "Dentsu has iOS and Android because Leonard wrote that invites are out to all three",
     "resolver": "ZOM-567: Dentsu added on TestFlight, not on the Play internal track (Arthur's comment Sep 29)",
     "discovery_order": "the Dentsu mail is in the firm's own correspondence; the ticket is in Linear, rarely opened for fundraising"},
    {"id": "T3", "family": "superseding", "services": ["gmail", "slack"], "seeded_ids": [S_BP_SCIPLAY_REPLY],
     "base_pointers": [B_SCIPLAY], "requirement": "R2",
     "expected_wrong_reading": "SciPlay In talks: the last mail is the investor promising to keep playing and report back",
     "resolver": "Robert's Sep 29 reply under the Sep 12 #bridge-pitch root: SciPlay passed by phone",
     "discovery_order": "the mail thread is found by the firm-name search; the reply is under a root about several firms and is not returned by channel history",
     "version_records": [ver("gmail", B_SCIPLAY, "2025-09-12T21:29:27Z", False, f"gmail:{B_SCIPLAY}"),
                         ver("gmail", B_SCIPLAY, "2025-09-18T03:27:31Z", False, f"gmail:{B_SCIPLAY}"),
                         ver("slack", S_BP_SCIPLAY_REPLY, "2025-09-29T22:14:00Z", True, f"slack:{B_BP_ROOT_0912}")]},
    {"id": "T4", "family": "superseding", "services": ["slack", "gmail"], "seeded_ids": [S_EXEC_ANGELS, G_ANTON],
     "requirement": "R3", "expected_wrong_reading": "Anton Bernstein at $40,000 (the #executives post)",
     "resolver": "Anton's Sep 24 mail trims his check to $25,000; the signing notice of Sep 26 shows it completed",
     "discovery_order": "the post is read first; Anton's mail has no subject tie to the SAFE",
     "version_records": [ver("slack", S_EXEC_ANGELS, "2025-09-19T17:40:00Z", True, "slack:C07C2866011/1758303600.418207"),
                         ver("gmail", G_ANTON, "2025-09-24T16:10:00Z", True, f"gmail:{G_ANTON}")]},
    {"id": "T5", "family": "scope_alias", "services": ["gmail", "contacts", "gsheets", "gcal"], "seeded_ids": [G_HIRO, CT_EDITH],
     "base_pointers": [B_HIRO, B_LIST], "requirement": "R2",
     "expected_wrong_reading": "Hiro Capital 'Awaiting reply' from the list's 'no response as of 09/11'",
     "resolver": "Edith Vane's Sep 26 pass (no firm name; cc the Investment Director from the Sep 3 Hiro thread); Contacts: Partner, Hiro Capital",
     "discovery_order": "a search for 'Hiro' returns only the Sep 3 thread and the list row"},
    {"id": "T6", "family": "exact_predicate", "services": ["gcal", "contacts", "gmail"], "seeded_ids": [EVT_BRIGHT, CT_ILSE, G_BRIGHT],
     "requirement": "R1", "expected_wrong_reading": "register = the list's firms; Brightwater Games Fund missing",
     "resolver": "the ask's population includes anyone with a call since Sep 3; the Sep 25 call is titled 'Ilse Marrow and Leonard Hayes' and Contacts ties her to Brightwater",
     "discovery_order": "the list is the obvious population; the call is one of ~20 person-titled events"},
    {"id": "T7", "family": "near_miss_mention", "services": ["gcal", "gmail", "slack"], "seeded_ids": [],
     "base_pointers": [B_EVT_HOMA, B_HOMA_INV, B_BP_HOMA], "requirement": "R1",
     "expected_wrong_reading": "Homa left out (not on the list; the calendar title names a person)",
     "resolver": "the updated invitation names HOMA; Frederick's own #bridge-pitch note puts Homa on the co-dev investment path",
     "discovery_order": "the list is read first; Homa appears only in an invitation body and a Slack mention"},
    {"id": "T8", "family": "authority", "services": ["trello"], "seeded_ids": [TR_KEEPWARM_COMMENT],
     "base_pointers": [B_CARD_KEEPWARM], "requirement": "R6",
     "expected_wrong_reading": "no keep-warm checklist items (only the sheet and the reply are written)",
     "resolver": "Leonard's comment on the Existing Investor Update card: every firm that passes after a pitch goes on the keep-warm checklist",
     "discovery_order": "the hub names the card only by role; the rule is a comment, not the description"},
    {"id": "T9", "family": "superseding", "services": ["gdocs"], "seeded_ids": [DOC_TEMPLATE_OLD, DOC_TEMPLATE],
     "requirement": "R3", "expected_wrong_reading": "committed = verbal yes (July template)",
     "resolver": "the Oct 14 template: committed = signed SAFE",
     "discovery_order": "both templates answer the same search; the July one has more edits and comments",
     "version_records": [ver("gdocs", DOC_TEMPLATE_OLD, "2025-07-08T18:00:00Z", True, f"file:{DOC_TEMPLATE_OLD}"),
                         ver("gdocs", DOC_TEMPLATE, "2025-09-26T18:00:00Z", True, f"file:{DOC_TEMPLATE}")]},
    {"id": "T10", "family": "superseding", "services": ["gsheets", "gmail"], "seeded_ids": [],
     "base_pointers": [B_LIST, B_TACC], "requirement": "R2",
     "expected_wrong_reading": "T-Accelerate 'First pitch being scheduled' (list Latest Status as of 09/11)",
     "resolver": "the Sep 22 call recap in the T-Accelerate thread: In talks",
     "version_records": [ver("gsheets", B_LIST, "2025-09-15T19:27:01Z", False, f"file:{B_LIST}"),
                         ver("gmail", B_TACC, "2025-09-22T17:40:07Z", False, f"gmail:{B_TACC}")]},
    {"id": "T11", "family": "scope_alias", "services": ["gmail", "contacts", "gsheets"], "seeded_ids": [CT_KARTHIC],
     "base_pointers": [B_BUBBLES, B_LIST], "requirement": "R1",
     "expected_wrong_reading": "PXLite (named in the call notes) added as an extra off-list firm",
     "resolver": "Contacts: Karthic R - T-Accelerate Capital (PXLite fund); one firm, one row"},
    {"id": "D1", "family": "distractor", "distractor_type": "near_duplicate_record", "services": ["gsheets"],
     "base_pointers": [B_LIST_2024], "requirement": "R1",
     "expected_wrong_reading": "2024 internal investor list used as the population",
     "resolver": "the ask names the 2025 list"},
    {"id": "D2", "family": "distractor", "distractor_type": "non_authoritative_instruction", "services": ["slack"],
     "seeded_ids": [S_EXEC_ARTHUR], "requirement": "R1",
     "expected_wrong_reading": "only firms Leonard emailed this month",
     "resolver": "Arthur's aside is not the ask; Leonard's population rule governs"},
    {"id": "D3", "family": "distractor", "distractor_type": "scope_adjacent", "services": ["slack", "gmail"],
     "base_pointers": ["C096HFA5Z8W/1758130464.175719", f"{FRED}/1843000993076735547"], "requirement": "R1",
     "expected_wrong_reading": "Rollic (hypercasual work-for-hire) or Playable Factory added as firms",
     "resolver": "template: service, publishing and competitor talks are out"},
    {"id": "D4", "family": "distractor", "distractor_type": "stale_summary", "services": ["slack"],
     "base_pointers": [B_BP_TRACKER], "requirement": "R2",
     "expected_wrong_reading": "statuses taken from Leonard's Sep 8 tracker post",
     "resolver": "each firm's later mail and notes"},
    {"id": "D5", "family": "distractor", "distractor_type": "withdrawn_ask", "services": ["gmail"],
     "seeded_ids": [G_ROBERT_ASK], "requirement": "R7",
     "expected_wrong_reading": "the pipeline mailed to the whole board",
     "resolver": "Leonard's ask: reply to him on his thread; he folds it into the deck"},
    {"id": "D6", "family": "distractor", "distractor_type": "other_title", "services": ["trello"],
     "base_pointers": [B_CARD_INVUPDATE_OLD], "requirement": "R6",
     "expected_wrong_reading": "keep-warm items added to the April 'Investor Update' card",
     "resolver": "the hub and the comment name the Existing Investor Update card"},
    {"id": "D7", "family": "distractor", "distractor_type": "near_duplicate_record", "services": ["gcal"],
     "base_pointers": [B_EVT_DENTSU_A, B_EVT_DENTSU_B], "requirement": "R4",
     "expected_wrong_reading": "two Dentsu meetings read as two firms or as a held meeting",
     "resolver": "one Oct 1 meeting, future at the clock; Dentsu is In talks on its Sep 23 call"},
]

CHAINS = [
    {"id": "C1", "root_cause": "A24", "ends_in": "R3", "hops": [
        {"service": "slack", "record": S_EXEC_ANGELS, "finding": "Leonard: Paul Heydon is in for $50K, Anton for $40K"},
        {"service": "gdocs", "record": DOC_TEMPLATE, "finding": "committed = signed SAFE; soft-circled = written yes, not signed"},
        {"service": "gmail", "record": G_DS_PAUL, "finding": "Paul's SAFE awaiting signature on Sep 29"}]},
    {"id": "C2", "root_cause": "A14", "ends_in": "R2", "hops": [
        {"service": "gmail", "record": B_SCIPLAY, "finding": "investor: we'll continue to play and let you know"},
        {"service": "gdocs", "record": DOC_TEMPLATE, "finding": "a phone pass counts once written in #bridge-pitch"},
        {"service": "slack", "record": S_BP_SCIPLAY_REPLY, "finding": "Robert: SciPlay passed by phone"}]},
    {"id": "C3", "root_cause": "A7", "ends_in": "R2", "hops": [
        {"service": "gsheets", "record": B_LIST, "finding": "Hiro Capital: no response as of 09/11"},
        {"service": "gmail", "record": G_HIRO, "finding": "Edith Vane declines, cc the Investment Director"},
        {"service": "contacts", "record": CT_EDITH, "finding": "Edith Vane - Partner, Hiro Capital"}]},
    {"id": "C4", "root_cause": "A17", "ends_in": "R1", "hops": [
        {"service": "gcal", "record": EVT_BRIGHT, "finding": "Sep 25 call 'Ilse Marrow and Leonard Hayes'"},
        {"service": "contacts", "record": CT_ILSE, "finding": "Ilse Marrow - Principal, Brightwater Games Fund"},
        {"service": "gmail", "record": G_BRIGHT, "finding": "Leonard's follow-up: deck sent, partner meeting next"}]},
    {"id": "C5", "root_cause": "A15", "ends_in": "R6", "hops": [
        {"service": "gmail", "record": G_HUB, "finding": "hub: do what the Existing Investor Update card says for passes"},
        {"service": "trello", "record": TR_KEEPWARM_COMMENT, "finding": "every firm passing after a pitch goes on keep-warm"},
        {"service": "slack", "record": S_BP_SCIPLAY_REPLY, "finding": "SciPlay's pass (one of the members)"}]},
]


def port(pid, mech, nodes, req, natural, fam, why, decides, controls, over):
    return {"id": pid, "mechanism": mech, "nodes": nodes, "requirement": req, "natural_reading": natural,
            "prior_family": fam, "prior_family_reason": why, "decides": decides, "controls": controls,
            "over_application": over}


PORTFOLIO = [
    port("DONE1", "A24", ["T1", "C1"], "R3", "every angel named as 'in' counts as committed at the posted amount",
         "done_gap", "v2 trap 1: a done-looking post against a missing signature in another service",
         ["M1", "M2", "RP2", "RP3"], ["Anton Bernstein (signed: completed notice)"],
         "over-application moves Anton to soft-circled although his notice says completed"),
    port("INPUT", "A11", ["T4"], "R3", "Anton at $40,000 from the #executives post",
         "superseding", "v2 trap 8: a later message in another service changes an input to a total",
         ["M2", "M3", "RP2"], ["Paul Heydon (no amount change)"],
         "over-application lowers Paul's amount although nothing revised it"),
    port("DONE2", "A24", ["T2"], "R4", "Dentsu has iOS and Android because the mail says invites are out to all",
         "done_gap", "v2 trap 1: 'invites are out' mail against the tester ticket's missing Play track",
         ["AC1"], ["T-Accelerate (both tracks confirmed in the ticket)"],
         "over-application marks T-Accelerate iOS only"),
    port("CORR", "A14", ["T3", "C2"], "R2", "SciPlay In talks from its own mail thread",
         "superseding", "v2 trap 2: correction in a Slack thread reply away from the firm's mail",
         ["ST1", "KW1"], ["London Venture Partners (pass in its own mail)"],
         "over-application reads every 'continue to play' firm as passed"),
    port("ALIAS", "A7", ["T5", "C3"], "R2", "Hiro Capital Awaiting reply from the list row",
         "scope_alias", "v2 trap 6: a partner's reply that names no firm; contacts and the earlier thread map it",
         ["ST2", "KW2"], ["Grishin Robotics (GRx pass already on the list as Rejected)"],
         "over-application maps an unrelated partner reply onto a list firm"),
    port("FILT", "A17", ["T6", "T7", "C4"], "R1", "register = the 2025 list rows only",
         "exact_predicate", "v2 trap 7: two in-scope firms outside the obvious list, found through calendar calls",
         ["V1", "ST3", "ST4"], ["Metaplay, Rollic (out: competitor / service talks)"],
         "over-application adds every company with a call (Metaplay, Rollic) to the register"),
    port("FOLLOW", "A15", ["T8", "C5"], "R6", "no keep-warm checklist items",
         "authority", "v2 trap 3: a follow-through rule in a card comment requires a write per passed firm",
         ["KW1", "KW2"], ["Dentsu (in talks, not added)"],
         "over-application adds every contacted firm, not only pitched passes"),
]
CHANNELS = [
    {"id": "CH-FILT-HOMA", "kind": "member", "rule": "FILT", "degrade": "drop Homa from the register", "members": ["Homa"],
     "latent": "calendar sweep", "family": "exact_predicate"},
    {"id": "CH-FILT-BRIGHT", "kind": "member", "rule": "FILT", "degrade": "drop Brightwater Games Fund", "members": ["Brightwater Games Fund"],
     "latent": "calendar sweep", "family": "exact_predicate"},
    {"id": "CH-SLIP", "kind": "slip", "degrade": "base slip on control rows", "slots": ["ST5", "AC2", "RP1", "DL1"]},
]

BUDGET = [
    ("discovery", "gmail", 8, "read the ask and its thread; Robert's board mail; find the template, README, deck via mail links"),
    ("discovery", "gdocs", 5, "read the Oct 14 template, the July template it supersedes, the folder README"),
    ("discovery", "gslides", 3, "open the draft deck and read slide 9's table columns"),
    ("discovery", "trello", 8, "find and read the Board Deck and Existing Investor Update cards, their comments and checklists"),
    ("discovery", "gdrive", 4, "locate the Board - Oct 14 2025 folder and list it"),
    ("discovery", "gcal", 6, "Monday's review event; list Sep 3-30 events on Frederick's calendar (two pages)"),
    ("enumeration", "gsheets", 4, "read the 2025 investor list (80 rows, several ranges) and check the 2024 lookalike"),
    ("enumeration", "slack", 22, "#bridge-pitch Jul-Sep history (4 pages at 100) and #executives Sep history (about 12 pages), roots only"),
    ("per-record", "gmail", 169, "one search per firm by name (79), a second by partner for the ~40 firms whose list row or mail names one, and a thread read for each of the ~50 firms with hits; search returns ids only, no bulk"),
    ("per-record", "slack", 124, "one search per firm (79) plus about 45 thread opens where a hit is a root that mentions the firm; replies are not in channel history"),
    ("per-record", "contacts", 40, "partner lookups for the list's Partner column, person-titled calls and partner-only replies"),
    ("reconciliation", "gcal", 18, "open each person-titled pitch event since Sep 3 for its description and attendees"),
    ("reconciliation", "gmail", 26, "signing-service notices per angel, Anton's and Paul's mails, Dentsu and Brightwater follow-ups, Hiro decline"),
    ("reconciliation", "linear", 6, "find ZOM-567, read it and its comments for each firm in talks"),
    ("reconciliation", "slack", 29, "open every replied thread in #executives (22) and #bridge-pitch (7) for September: phone notes and corrections live in replies"),
    ("rules", "gdocs", 4, "re-read the template's definitions while classifying edge firms"),
    ("rules", "contacts", 6, "check mapping for Karthic/PXLite and Hiro's Investment Director"),
    ("writes", "gsheets", 6, "create the register, write 79 rows in batches, totals"),
    ("writes", "gdrive", 2, "place the sheet in the Board folder and confirm"),
    ("writes", "trello", 5, "create or reuse the keep-warm checklist and add one item per passed firm"),
    ("writes", "gmail", 1, "reply on Leonard's thread"),
    ("read-back", "gsheets", 3, "read back the written ranges and totals"),
    ("read-back", "trello", 2, "read the checklist back"),
    ("read-back", "gdrive", 1, "confirm the file's parent folder"),
]

WRITES = [
    {"service": "gsheets", "tool": "gsheets_create_spreadsheet+gsheets_values_update", "count": 3,
     "depends_on": ["K3", "K4", "K5", "K6", "K7", "K11", "C1", "C2", "C3", "C4", "T1", "T2", "T3", "T4", "T5", "T6", "T7"],
     "requirements": ["R1", "R2", "R3", "R4"]},
    {"service": "gdrive", "tool": "gdrive_move_file", "count": 1, "depends_on": ["K2", "K13"], "requirements": ["R5"]},
    {"service": "trello", "tool": "trello_create_checklist+trello_create_check_item", "count": 4,
     "depends_on": ["K9", "C5", "T3", "T5", "T8"], "requirements": ["R6"]},
    {"service": "gmail", "tool": "gmail_reply_to_message", "count": 1, "depends_on": ["K1", "K10", "C1", "T1", "T4"],
     "requirements": ["R7"]},
]

HAZ = [
    {"hazard_id": "Q01", "resolution": "dated_claim", "requirement": "R2",
     "why_safe": "Robert's seeded reply under the Sep 12 root changes that root's reply_count/latest_reply; the SQL updates the counters (companion), and the text is an attributed, dated claim"},
]

manifest = {
    "_note": "draft manifest (/create-scenario); /create-injection writes 01_Hardness_Manifest.json keeping every id or listing it in design_delta",
    "persona": "frederick_stone",
    "assignment_context": {k: CTX[k] for k in ("context_hash", "assignment_hash", "policy_hash", "freeze_utc", "difficulty_mode")},
    "horizon": "Long Horizon",
    "effective_profile": "extreme",
    "author_targets": {"min_calls_per_run": 100, "max_avg_weighted_pass": 0.80,
                       "requester_confirmation": "task author in chat on 2026-11-01: 'make sure my task is a long horizon task soo i want over 100 tool calls in each runs and my difficulty is medioum so i want difficulty pass rate under 80%'"},
    "requirements": REQ,
    "services": SERVICES,
    "anchors": ANCHORS,
    "ask_fragments": FRAGS,
    "authorities": AUTHS,
    "cohort": COHORT,
    "chains": CHAINS,
    "traps": TRAPS,
    "mechanism_portfolio": PORTFOLIO,
    "channels": CHANNELS,
    "call_budget": [{"phase": p, "service": s, "calls": c, "reason": r} for p, s, c, r in BUDGET],
    "writes": WRITES,
    "hazard_acknowledgements": HAZ,
    "denied_probes": [],
    "gradable_surface": "01_Gradable_Surface.json",
}

# ---------------------------------------------------------------- gradable surface
DELIV = {
    "register": {"kind": "table", "name_regex": r"(?i).*(fundrais|pipeline|bridge).*", "key_column": "Firm",
                 "key_regex": r".+", "columns": ["Firm", "Status", "Last two-way contact", "Build access",
                                                  "Committed", "Soft-circled"],
                 "class_column": "Status", "comparators": {"Status": "norm", "Build access": "norm"}},
    "reply": {"kind": "json_text", "tool": "gmail_reply_to_message"},
    "keepwarm": {"kind": "json_text", "tool": "trello_create_check_item"},
}


def slot(sid, title, w, wk, why, cls, sel, role="core", group=None, mech=(), fact=None, volume_for=None):
    s = {"id": sid, "title": title, "weight": w, "work_kind": wk, "work_reason": why, "class": cls,
         "selector": sel, "role": role, "mechanisms": list(mech)}
    if group:
        s["group"] = group
    if fact:
        s["fact_id"] = fact
    if volume_for:
        s["volume_for"] = volume_for
    return s


SLOTS = [
    slot("V1", "register size", 3, "limited_reconciliation", "list rows deduplicated plus off-list calls", "delivery",
         ["delivery", "register_keys_exact"], role="volume", mech=["FILT"], volume_for=["status", "access"], fact="register_size"),
    slot("ST1", "SciPlay status", 5, "multi_source_reconciliation", "mail thread vs Robert's Slack thread reply", "direct",
         ["field", "Sciplay", "Status"], role="sample", group="status", mech=["CORR"]),
    slot("ST2", "Hiro Capital status", 5, "multi_source_reconciliation", "list row vs partner-only pass mail vs contacts", "direct",
         ["field", "Hiro Capital", "Status"], role="sample", group="status", mech=["ALIAS"]),
    slot("ST3", "Homa on the register in talks", 5, "multi_source_reconciliation", "calendar + invitation body + Slack note, off the list", "direct",
         ["field", "Homa", "Status"], role="sample", group="status", mech=["FILT"]),
    slot("ST4", "Brightwater on the register in talks", 5, "multi_source_reconciliation", "person-titled call + contacts + mail, off the list", "direct",
         ["field", "Brightwater Games Fund", "Status"], role="sample", group="status", mech=["FILT"]),
    slot("ST5", "London Venture Partners status", 3, "interpretation", "pass read from its own thread under the list's longer name", "direct",
         ["field", "London Venture Partners", "Status"], role="sample", group="status"),
    slot("AC1", "Dentsu build access", 5, "multi_source_reconciliation", "invite mail vs tester ticket", "direct",
         ["field", "Dentsu Ventures", "Build access"], role="sample", group="access", mech=["DONE2"]),
    slot("AC2", "T-Accelerate build access", 3, "interpretation", "read from the tester ticket", "direct",
         ["field", "T-accelerate", "Build access"], role="sample", group="access"),
    slot("M1", "Paul Heydon soft-circled amount", 5, "multi_source_reconciliation", "Slack post vs signing reminder vs template", "direct",
         ["field", "Paul Heydon", "Soft-circled"], mech=["DONE1"]),
    slot("M3", "Anton Bernstein committed amount", 5, "multi_source_reconciliation", "Slack post vs Anton's mail vs completed notice", "direct",
         ["field", "Anton Bernstein", "Committed"], mech=["INPUT"]),
    slot("M2", "committed total on the register", 5, "multi_source_reconciliation", "sum over signed SAFEs at their latest amounts", "write_content",
         ["text", "register", r"[Cc]ommitted.{0,60}25,?000"], mech=["DONE1", "INPUT"], fact="committed_total"),
    slot("RP1", "reply on Leonard's thread", 1, "lookup", "delivery to the named thread", "delivery",
         ["delivery", "email_reply", G_HUB]),
    slot("RP2", "reply states the committed total", 5, "multi_source_reconciliation", "same reconciled total carried into the reply", "write_content",
         ["text", "reply", r"[Cc]ommitted.{0,60}25,?000"], mech=["DONE1", "INPUT"], fact="committed_total"),
    slot("RP3", "reply states the soft-circled total", 3, "calculation", "sum over unsigned written yeses", "write_content",
         ["text", "reply", r"[Ss]oft.?circled.{0,60}50,?000"], mech=["DONE1"], fact="soft_total"),
    slot("DL1", "register in the Board - Oct 14 2025 folder", 1, "lookup", "delivery to the named folder", "delivery",
         ["delivery", "register_parent", DRIVE_FOLDER]),
    slot("KW1", "keep-warm item for SciPlay", 5, "multi_source_reconciliation", "card rule applied to a pass found only in a Slack reply", "write_content",
         ["text", "keepwarm", r"Sci[Pp]lay"], mech=["FOLLOW", "CORR"]),
    slot("KW2", "keep-warm item for Hiro Capital", 5, "multi_source_reconciliation", "card rule applied to a partner-only pass", "write_content",
         ["text", "keepwarm", r"[Hh]iro"], mech=["FOLLOW", "ALIAS"]),
]

def truth_keys():
    import ast
    d = json.loads((WF.parents[2] / "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/gsheets/data.json").read_text())
    sp = next(x for x in d["sheets_spreadsheets"] if x["spreadsheet_id"] == B_LIST)
    sh = ast.literal_eval(sp["sheets"]) if isinstance(sp["sheets"], str) else sp["sheets"]
    seen, keys = set(), []
    for r in sh[0]["grid"][1:]:
        f = (r[1] if len(r) > 1 else "").strip()
        if f and f.lower() not in seen:
            seen.add(f.lower()); keys.append(f)
    assert len(keys) == 77, len(keys)
    return keys + ["Homa", "Brightwater Games Fund"]


surface = {"kind": "GRADABLE_SURFACE", "version": 1, "task": "frederick_bridge_pipeline", "revision": "design-1",
           "truth_keys": truth_keys(),
           "classes": ["Passed", "In talks", "Awaiting reply", "Not contacted this round"],
           "truth_fields": {"class": "Status", "groups": "groups"},
           "deliverables": DELIV, "slots": SLOTS}

(WF / "01_Hardness_Manifest.draft.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")
(WF / "01_Gradable_Surface.json").write_text(json.dumps(surface, indent=1, ensure_ascii=False) + "\n")
tot = sum(s["weight"] for s in SLOTS)
print("manifest + surface written; surface weight", tot, "calls", sum(b[2] for b in BUDGET),
      "per-record", sum(b[2] for b in BUDGET if b[0] == "per-record"))
print("ids:", G_HUB, G_ANTON, G_DS_ANTON, G_DS_PAUL, G_HIRO, G_DENTSU, G_BRIGHT, G_ROBERT_ASK)
