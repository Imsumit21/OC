#!/usr/bin/env python3
"""Builds the /create-scenario draft manifest and gradable surface for the Frederick Q4 update send-list task (rev7).
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
G_HUB = f"{FRED}/{thrid(HUB_AT, 11)}"                    # Leonard's ask (anchor + hub): Q4 update send list
S_EXEC_SIGNED = "C07C2866011/1758911700.336170"           # rev7 #executives 2025-09-26T18:35Z Leonard: what counts as signed
# rev6: Anton's trim moved from a mail into Leonard's DM with Frederick (D05S58U4SAK)
S_DM_ANTON = "D05S58U4SAK/1758731100.281734"            # DM 2025-09-24T16:25Z Leonard: Anton down to 25, resending the SAFE
S_DM_ANTON_SIGNED = "D05S58U4SAK/1758914100.640218"     # DM 2025-09-26T19:15Z Leonard: Anton signed the 25 one
G_DS_ANTON = f"{FRED}/{thrid('2025-09-26T19:02:00Z', 31)}"  # signing service: completed (Anton)
G_DS_PAUL = f"{FRED}/{thrid('2025-09-29T15:00:00Z', 37)}"   # Leonard's Sep 29 nudge to Paul ("still sitting with you"); rev10: Paul's reply sits in this thread
# rev11: Paul's rev10 "signed it" reply is gone; he backs out by mail to Leonard only. rev12: Leonard tells Frederick in
# their 1:1 DM (the rev11 reply under the angel post was opened by every run)
S_DM_PAUL_OUT = "D05S58U4SAK/1759251900.863415"          # 2025-09-30T17:05Z Leonard (1:1 DM with Frederick): "Paul's out"
# rev12: ZOM-567 logs two more firms in talks (NCsoft, Brightwater); the rev11 T-Accelerate mail replies are removed
LIN_C_NCSOFT, LIN_C_BRIGHT = "lc_4369758f577612cdb63b3457", "lc_5e2ff140afff06e3a78e2fe1"
G_HIRO = f"{FRED}/{thrid('2025-09-26T09:40:00Z', 41)}"    # Edith Vane (Hiro) pass, no firm name in body
G_DENTSU = f"{FRED}/{thrid('2025-09-26T17:20:00Z', 47)}"  # Leonard: invites out to all three (DONE2 'done' source)
G_BRIGHT = f"{FRED}/{thrid('2025-09-25T22:30:00Z', 53)}"  # Leonard follow-up to Ilse Marrow after the call
G_ROBERT_ASK = f"{FRED}/{thrid('2025-09-29T18:20:00Z', 59)}"  # Robert: just email the board (withdrawn by the hub)
S_EXEC_ANGELS = "C07C2866011/1758303600.418207"           # #executives 2025-09-19T17:40Z Leonard: angels 'are in'
# rev6: Robert's SciPlay pass moved from a #bridge-pitch thread into a #executives thread reply (root: Leonard's speedrun post)
B_EXEC_A16Z_ROOT = "C07C2866011/1759196326.309469"        # base #executives 2025-09-30T01:38Z (Sep 29 18:38 PT) Leonard: speedrun, "Not a surprise"
S_EXEC_SCIPLAY_REPLY = "C07C2866011/1759248360.377105"    # reply in that thread, 2025-09-30T16:06Z (Sep 30 9:06am PT)
# rev6: Arthur's Play-track correction in #zombie-match3d, Leonard's reply. rev10: both are replies in the thread under
# Leonard's base Sep 29 post "I just released 0.3.49 on IOS"; the text no longer says tester, TestFlight or ZOM-567
B_ZM_REL_ROOT = "C0880U9751A/1759182908.627389"           # base root 2025-09-29T21:55Z Leonard: "I just released 0.3.49 on IOS"
S_ZM_ARTHUR_PLAY = "C0880U9751A/1759274400.518306"        # 2025-09-30T23:20Z Arthur (thread reply): the Play console group was never attached to the internal track
S_ZM_LEO_REPLY = "C0880U9751A/1759276080.094417"          # 2025-09-30T23:48Z Leonard (thread reply): ping me when it's live
S_EXEC_ARTHUR = "C07C2866011/1759168800.117903"           # #executives 2025-09-29T18:00Z Arthur: 'just list who Leonard emailed'
DOC_TEMPLATE = "f_3b9e61c04d7a52e8f1a6c2"                 # rev7: Q4 investor update - send list (rules doc)
DOC_TEMPLATE_OLD = "f_8d2c47a91e05b3f6d7c418"             # rev7: Q3 investor update - send list (July decoy, superseded)
DOC_README = "f_c61a0e93b7d24f58a2e917"                   # README - Q4 investor update (in the folder)
DRIVE_FOLDER = "d_5e8a1c3f9b07d2e64a1b93"                 # Q4 2025 investor update folder (owner Frederick)
DECK_DRAFT = "f_a47d0e2c95b18f63e2c0d5"                   # Harmony Games Q4 2025 update (draft) deck
EVT_REVIEW = "evt_9c41e7a2d05b38f6e1a7c4"                 # Mon Oct 6 send list review (Leonard + Frederick)
EVT_BRIGHT = "evt_2f86b0d4c9e17a35b64e0d"                 # Thu Sep 25 'Ilse Marrow and Leonard Hayes'
LIN_TESTERS = "ZOM-567"                                    # Arthur: investor testers on ZM internal tracks
TR_KEEPWARM_COMMENT = "68c6b2a4f19e03d7c5a81b2e"          # Leonard comment on Existing Investor Update card
TR_BOARDDECK_COMMENT = "68d81f30a6c94e2b7d05e1f4"         # Leonard comment on Board Deck card (Oct 14 slide)
CT_EDITH = "e3a91c07d5b48f26a0c7e314"                     # Contacts: Edith Vane - Partner, Hiro Capital
CT_ILSE = "b72f0d6e19c3a84e5d21f9a0"                      # Contacts: Ilse Marrow - Principal, Brightwater Games Fund
CT_KARTHIC = "5d0e8b31f7a29c64e1b0d3a8"                   # Contacts: Karthic R - T-Accelerate Capital (PXLite fund)
# rev9 (baseline: 72.7 counted calls, ~82% pass): Leonard's second card comment and the follow-up records
TR_Q4_CMT = "68db03b86054eff7e8e92474"                    # Leonard Sep 29 comment: a checklist per group + follow-up cards
TR_FU_ANEL = "68c99e98737744bd966aed24"                   # Leonard Sep 16 open To Do card: F/up with Anel after the engine deep dive
EVT_MAKERS = "evt_6b2e94d0c17a3f58e9d2b1"                 # Fred's copy: Michael Cheung and Leonard Hayes (Makers Fund), Wed Oct 8 (made Sep 29)

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
    "R1": "send list population: look at every name on the 2025 game investor list (duplicate list rows are one name) "
          "plus every firm not on the list that we had a pitch call or meeting with since the Sep 3 kickoff (Homa; "
          "Brightwater Games Fund); service, publishing-only, RFP and competitor talks are out; 26 people go on the list "
          "(New investor 1, In talks 7, Awaiting reply 14, Keep warm 3); 25 go on the list; email-only passes, firms not contacted and "
          "Paul Heydon (backed out on Sep 30, no call) stay off",
    "R2": "group per entry as of end of day Tue Sep 30 Pacific under the send-list doc's rules: only this round counts, "
          "outreach by someone introducing us counts as ours, a no they told any of us counts (a no sent to Griffin too), "
          "an accelerator decision is not a bridge answer, a pass after a pitch call or meeting is Keep warm; a partner's "
          "reply counts for the firm Contacts ties them to",
    "R3": "new investors and amounts: New investor means a signed SAFE (the DocuSign Completed notice is in, per "
          "Leonard's #executives note); angels who said yes but haven't signed are In talks with the amount they said yes "
          "to; Anton Bernstein New investor 25,000 (his SAFE re-sent and signed at 25 after the $40,000 post); Paul "
          "Heydon is off the list: he backed out on Sep 30 (Leonard's 1:1 DM to Frederick), a no without "
          "a call",
    "R4": "build access for each firm in talks: whether they can get the current internal build on iOS (TestFlight) "
          "and Android (Play internal test track), from Arthur's tester records; T-Accelerate, Dentsu, NCsoft and "
          "Brightwater iOS only (the investor tester list in the Play console was never attached to the internal track: "
          "Arthur's Sep 30 #zombie-match3d post naming everyone on it)",
    "R5": "send list saved as one Google Sheet in Frederick's Q4 2025 investor update folder, named per the folder README",
    "R6": "a checklist per send-list group on the Existing Investor Update card, one item per firm or angel: Keep warm "
          "(Leonard's Sep 13 comment: every firm that passed after a pitch call or meeting this round: LVP, SciPlay, Hiro "
          "Capital; a16z stays In talks, a speedrun decision is not a bridge answer) plus New investor, In talks and "
          "Awaiting reply (his Sep 29 comment); 25 items over 4 checklists",
    "R8": "a follow-up card \"F/up with\" + name in To Do on the Harmony Games board for everyone In talks or Awaiting "
          "reply (18 cards); NCsoft already has Leonard's open To Do card 'F/up with Anel after the engine deep dive' (Anel "
          "Ceman is NCsoft's partner on the 2025 list), so it gets a comment there instead; Dentsu (Wed Oct 1 meeting) and "
          "Makers Fund (Wed Oct 8 call with its partner Michael Cheung) are on Fred's calendar after Sep 30 and get none",
    "R7": "reply on Leonard's ask thread with how many firms and angels are in each group (New investor 0 firms 1 angel, In "
          "talks 7 firms 0 angels, Awaiting reply 14 firms, Keep warm 3 firms); to Leonard on his thread",
}

SERVICES = {
    "gmail": {"role": "anchor ask (hub: Q4 update send list) and reply destination; investor threads cc'd to Frederick; "
                      "signing-service notices; Edith Vane's pass; Leonard's Dentsu 'invites are out' mail",
              "weight_reason": "the ask, the signing state of each SAFE and the Hiro pass live in mail"},
    "slack": {"role": "#bridge-pitch trackers; #executives angel post, Leonard's what-counts-as-signed note and Robert's "
                      "thread reply (SciPlay pass); Leonard's DM with Frederick (Anton's revised amount; Paul backs out); "
                      "Arthur's #zombie-match3d post on the investor tester list's Android access",
              "weight_reason": "SciPlay's pass, Paul's withdrawal, Anton's revised amount and Dentsu's Play gap exist only in "
                               "Slack, each in a different container from the record it corrects"},
    "gsheets": {"role": "2025 game investor list (who to look at, stale Latest Status); the send list write",
                "weight_reason": "the population is the list; the send list is the deliverable"},
    "gdocs": {"role": "H1 Q4 update send-list doc (groups, amounts, build access, as-of); Q3 (July) send-list decoy; "
                      "folder README",
              "weight_reason": "every group, amount and access definition lives only in the send-list doc"},
    "gcal": {"role": "pitch calls since Sep 3 (Homa, Brightwater, Hiro, SciPlay, LVP...); Oct 6 review event; calls already "
                     "booked after Sep 30 (Dentsu Oct 1, Makers Oct 8) that need no follow-up card",
             "weight_reason": "off-list firms are found only through calendar calls titled by a person"},
    "contacts": {"role": "partner-to-firm mappings (Edith Vane - Hiro Capital; Ilse Marrow - Brightwater; Karthic - T-Accelerate/PXLite)",
                 "weight_reason": "Hiro's pass and Brightwater's call name only a person; contacts tie them to the firm"},
    "trello": {"role": "H2 Leonard's two comments on the Existing Investor Update card (checklist per group, follow-up "
                       "cards); his open To Do card for NCsoft's partner; 4 checklists, 25 items, 18 cards and 1 comment written",
               "weight_reason": "the follow-through rules live only in the card comments; every entry needs its own item and "
                                "most need their own card (no bulk write)"},
    "linear": {"role": "ZOM-567 investor tester log (the done source: TestFlight and Play adds logged for T-Accelerate, NCsoft, Brightwater and Dentsu)",
               "weight_reason": "the believable done source for build access; its missing piece is in Slack"},
    "gdrive": {"role": "Q4 2025 investor update folder owned by Frederick (send list destination)",
               "weight_reason": "the folder is the required destination"},
    "gslides": {"role": "Harmony Games Q4 2025 update (draft) deck: what each send-list group gets",
                "weight_reason": "the bridge slide says what each group's paragraph and links are, so the groups matter"},
}

ANCHORS = [{"id": "A1", "service": "gmail", "record": G_HUB, "locator": G_HUB,
            "prompt_reference": "Leonard's Q4 update email", "requirement_ids": ["R7"]}]


def frag(fid, svc, container, locator, seeded, via, dby, quote, reqs, names=(), base=()):
    return {"id": fid, "service": svc, "container": container, "locator": locator, "kind": "requirement",
            "incorporated_via": via, "seeded_ids": list(seeded), "base_pointers": list(base),
            "delegated_by_record": dby, "delegation_quote": quote, "requirement_ids": reqs,
            "names_authorities": [{"id": a, "quote": q} for a, q in names]}


FRAGS = [
    frag("K1", "gmail", G_HUB, G_HUB, [G_HUB], ["A1"], G_HUB,
         "reply here with how many firms and angels are in each group", ["R7"]),
    frag("K2", "gmail", G_HUB, G_HUB, [G_HUB], ["A1"], G_HUB,
         "put it in your Q4 investor update folder", ["R5"]),
    frag("K3", "gmail", G_HUB, G_HUB, [G_HUB], ["A1"], G_HUB,
         "everyone from the bridge round who should get it", ["R1"],
         names=[("H1", "with the groups and details in the Q4 update send list doc")]),
    frag("K4", "gdocs", DOC_TEMPLATE, DOC_TEMPLATE, [DOC_TEMPLATE], ["A1"], G_HUB,
         "with the groups and details in the Q4 update send list doc", ["R2"]),
    frag("K5", "gdocs", DOC_TEMPLATE, DOC_TEMPLATE, [DOC_TEMPLATE], ["A1"], G_HUB,
         "with the groups and details in the Q4 update send list doc", ["R3"]),
    frag("K6", "gdocs", DOC_TEMPLATE, DOC_TEMPLATE, [DOC_TEMPLATE], ["A1"], G_HUB,
         "with the groups and details in the Q4 update send list doc", ["R4"]),
    frag("K7", "gsheets", B_LIST, B_LIST, [], ["K4"], DOC_TEMPLATE,
         "Every name on the 2025 game investor list", ["R1"], base=[B_LIST]),
    frag("K9", "trello", B_CARD_KEEPWARM, f"trello:{B_CARD_KEEPWARM}", [TR_KEEPWARM_COMMENT], ["A1"], G_HUB,
         "do what I put on the Existing Investor Update card in Trello", ["R6"],
         names=[("H2", "what I put on the Existing Investor Update card")]),
    frag("K18", "trello", B_CARD_KEEPWARM, f"trello:{TR_Q4_CMT}", [TR_Q4_CMT], ["A1"], G_HUB,
         "do what I put on the Existing Investor Update card in Trello", ["R6", "R8"]),
    frag("K11", "gslides", DECK_DRAFT, DECK_DRAFT, [DECK_DRAFT], ["A1"], G_HUB,
         "The draft update deck shows what each group gets", ["R1"]),
    frag("K12", "gcal", EVT_REVIEW, EVT_REVIEW, [EVT_REVIEW], ["A1"], G_HUB,
         "I put Monday's review on your calendar", ["R5"]),
    frag("K13", "gdocs", DOC_README, DOC_README, [DOC_README], ["K2"], G_HUB,
         "the README in that folder says how to name it", ["R5"]),
    frag("K14", "linear", LIN_TESTERS, f"linear:{LIN_TESTERS}", [LIN_TESTERS], ["K6"], DOC_TEMPLATE,
         "Arthur tracks the tester adds", ["R4"]),
    frag("K15", "slack", "C0880U9751A", S_ZM_ARTHUR_PLAY, [S_ZM_ARTHUR_PLAY], ["K6"], DOC_TEMPLATE,
         "Arthur tracks the tester adds", ["R4"]),
    frag("K16", "gdrive", DRIVE_FOLDER, DRIVE_FOLDER, [DRIVE_FOLDER], ["A1"], G_HUB,
         "put it in your Q4 investor update folder", ["R5"]),
    frag("K17", "slack", "C07C2866011", S_EXEC_SIGNED, [S_EXEC_SIGNED], ["K5"], DOC_TEMPLATE,
         "see my note in #executives on what counts as signed", ["R3"]),
]

AUTHS = [
    {"id": "H1", "name": "the Q4 update send-list doc", "home_service": "gdocs",
     "decoy_service": "gdocs", "governs": ["R2", "R3", "R4"], "findable_query": "send list",
     "seeded_ids": [DOC_TEMPLATE], "base_pointers": [], "decoy_seeded_ids": [DOC_TEMPLATE_OLD], "decoy_base_pointers": [],
     "decoy_scope": {"dimension": "lot", "decoy": "Q3 (July) investor update: new investor = anyone who said yes with an amount",
                     "task": "Q4 investor update: new investor = a signed SAFE"}},
    {"id": "H2", "name": "Leonard's comments on the Existing Investor Update card", "home_service": "trello",
     "decoy_service": "trello", "governs": ["R6", "R8"], "findable_query": "Existing Investor Update",
     "seeded_ids": [TR_KEEPWARM_COMMENT, TR_Q4_CMT], "base_pointers": [B_CARD_KEEPWARM], "decoy_seeded_ids": [],
     "decoy_base_pointers": [B_CARD_INVUPDATE_OLD],
     "decoy_scope": {"dimension": "issuer", "decoy": "existing investors' quarterly update (Investor Update card, Apr 2025)",
                     "task": "bridge-round prospects that passed after a pitch (Existing Investor Update card)"}},
]

COHORT = {
    "definition": "every firm on the 2025 game investor list (77 unique names over 80 rows) plus every off-list firm with "
                  "a call or meeting since Sep 3 (Homa, Brightwater Games Fund) = 79 looked at; 26 go on the send list",
    "definition_source": [G_HUB, B_LIST],
    "size": 79,
    "evidence_surfaces": [
        {"service": "gmail", "tool": "gmail_search_messages+gmail_get_thread", "per_record_calls": 2.1, "records": 79,
         "requirement": "R2", "decides": "group per entry",
         "why_no_bulk": "gmail_search returns ids only; each firm needs its own query (name, partner) and a thread read for the firm's latest answer",
         "short_circuit": "the list's Latest Status stops at 09/11 and Slack trackers stop at Sep 8 - only the firm's own mail gives its state at Sep 30, so no other surface decides the record first"},
        {"service": "slack", "tool": "slack_search_messages+slack_get_thread_replies", "per_record_calls": 1.55, "records": 79,
         "requirement": "R2", "decides": "group per entry",
         "why_no_bulk": "channel history returns roots only; corrections sit in thread replies under roots about other firms and in DMs, reachable per firm by search",
         "short_circuit": "a firm whose mail looks active can still have passed by phone (SciPlay); mail cannot rule that out"},
        {"service": "contacts", "tool": "contacts_search_contacts", "per_record_calls": 0.5, "records": 79,
         "requirement": "R1", "decides": "every firm not on the list that we had a pitch call or meeting with",
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
    {"id": "T1", "family": "superseding", "services": ["slack", "gmail", "gsheets"], "seeded_ids": [S_EXEC_ANGELS, G_DS_PAUL, S_DM_PAUL_OUT],
     "requirement": "R3", "expected_wrong_reading": "Paul Heydon In talks at $50,000: Leonard's #executives post says he is in, the Bridge angels sheet says in, and Leonard's Sep 29 nudge shows only that the SAFE is still waiting on him",
     "resolver": "Leonard's Sep 30 10:05 AM PT message in his 1:1 DM with Frederick: Paul's out, he can't put money in this year after all. A no for this round with no call or meeting, so Paul stays off the send list (no row, no checklist item, no follow-up card)",
     "discovery_order": "the angel post is returned by the SAFE and DocuSign searches and has no replies; the DM is read only by runs that open the 1:1 conversation (about 6 of 15 Opus runs did) or search Slack for Paul, and the message avoids SAFE, DocuSign, signed, counts and angel; Paul's own mail went to Leonard only",
     "version_records": [ver("slack", S_EXEC_ANGELS, "2025-09-19T17:40:00Z", True, "slack:C07C2866011/1758303600.418207"),
                         ver("gmail", G_DS_PAUL, "2025-09-29T15:00:00Z", True, f"gmail:{G_DS_PAUL}"),
                         ver("slack", S_DM_PAUL_OUT, "2025-09-30T17:05:00Z", True, "slack:D05S58U4SAK")]},
    {"id": "T2", "family": "done_gap", "services": ["gmail", "linear", "slack"],
     "seeded_ids": [G_DENTSU, LIN_TESTERS, LIN_C_NCSOFT, LIN_C_BRIGHT, S_ZM_ARTHUR_PLAY, S_ZM_LEO_REPLY],
     "base_pointers": ["C07C2866011/1758558621.032499"],
     "requirement": "R4", "expected_wrong_reading": "T-Accelerate, Dentsu, NCsoft and Brightwater have iOS and Android: ZOM-567 logs both tracks for each and Leonard wrote that the Dentsu invites are out",
     "resolver": "Arthur's Sep 30 4:20 PM PT post in #zombie-match3d: the investor tester list he made in the Play console never got attached to the internal track, so nobody on it has android yet (Karthic, the 3 Dentsu folks, Anel's two at NCsoft and Ilse from Brightwater), whatever the Linear log says; iOS is fine for all of them. All four iOS only; Arthur attaches it with his Oct 1 push",
     "discovery_order": "the ticket is the record the template points to and reads as done; the correction is a root post in the game channel, which no run reads, found by a Slack search for tester (the template's own word), android, Play or a firm name; it avoids TestFlight and the ticket id",
     "version_records": [ver("gmail", G_DENTSU, "2025-09-26T17:20:00Z", True, f"gmail:{G_DENTSU}"),
                         ver("linear", LIN_TESTERS, "2025-09-30T18:40:00Z", True, f"linear:{LIN_TESTERS}"),
                         ver("slack", S_ZM_ARTHUR_PLAY, "2025-09-30T23:20:00Z", True, "slack:C0880U9751A/1759274400.518306")]},
    {"id": "T3", "family": "superseding", "services": ["gmail", "slack"], "seeded_ids": [S_EXEC_SCIPLAY_REPLY],
     "base_pointers": [B_SCIPLAY, B_EXEC_A16Z_ROOT], "requirement": "R2",
     "expected_wrong_reading": "SciPlay In talks: the last mail is the investor promising to keep playing and report back",
     "resolver": "Robert's Sep 30 reply under Leonard's speedrun post in #executives: SciPlay's contact called him, they are out for this round",
     "discovery_order": "the mail thread is found by the firm-name search; the reply sits under a root about another firm and is not returned by channel history",
     "version_records": [ver("gmail", B_SCIPLAY, "2025-09-18T03:27:31Z", False, f"gmail:{B_SCIPLAY}"),
                         ver("slack", S_EXEC_SCIPLAY_REPLY, "2025-09-30T16:06:00Z", True, f"slack:{B_EXEC_A16Z_ROOT}")]},
    {"id": "T4", "family": "superseding", "services": ["slack", "gsheets"], "seeded_ids": [S_EXEC_ANGELS, "f_6e1d93a0c4b72f85d39a0e", S_DM_ANTON, S_DM_ANTON_SIGNED],
     "requirement": "R3", "expected_wrong_reading": "Anton Bernstein committed at $40,000 (the #executives post and the Bridge angels sheet)",
     "resolver": "Leonard's Sep 24 DM to Frederick: Anton is down to $25,000, the SAFE is re-sent at 25; Sep 26 DM: Anton signed the 25 one (the Completed notice the same day carries no amount)",
     "discovery_order": "the post and the sheet agree and are read first; the DM is a 1:1 conversation no channel read returns",
     "version_records": [ver("slack", S_EXEC_ANGELS, "2025-09-19T17:40:00Z", True, "slack:C07C2866011/1758303600.418207"),
                         ver("gsheets", "f_6e1d93a0c4b72f85d39a0e", "2025-09-20T03:15:00Z", True, "file:f_6e1d93a0c4b72f85d39a0e"),
                         ver("slack", S_DM_ANTON, "2025-09-24T16:25:00Z", True, "slack:D05S58U4SAK/1758731100.281734")]},
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
     "expected_wrong_reading": "no checklists on the card, or only the Keep warm one (only the sheet and the reply are written)",
     "resolver": "Leonard's Sep 13 comment (passes after a pitch go on a Keep warm checklist) and his Sep 29 comment (every other group gets its own checklist, one item per firm or angel)",
     "discovery_order": "the hub names the card only by role; the rule is a comment, not the description"},
    {"id": "T9", "family": "superseding", "services": ["gdocs"], "seeded_ids": [DOC_TEMPLATE_OLD, DOC_TEMPLATE],
     "requirement": "R3", "expected_wrong_reading": "new investor = anyone who said yes with an amount (the Q3 July send list)",
     "resolver": "the Q4 send-list doc: new investor = a signed SAFE",
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
    {"id": "T12", "family": "scope_alias", "services": ["trello", "gsheets"], "seeded_ids": [TR_FU_ANEL, TR_Q4_CMT],
     "base_pointers": [B_LIST], "requirement": "R8",
     "expected_wrong_reading": "a new 'F/up with NCsoft' card next to Leonard's open To Do card for the same firm",
     "resolver": "the open To Do card 'F/up with Anel after the engine deep dive' is NCsoft's: the 2025 list's Partner column "
                 "has Anel Ceman for NCsoft, whose Latest Status is the engine follow-up; Leonard's Sep 29 comment: comment on "
                 "an existing To Do card instead of adding another",
     "discovery_order": "the card names only the partner's first name; a board search for NCsoft returns nothing"},
    {"id": "T13", "family": "exact_predicate", "services": ["gcal", "trello", "gsheets"], "seeded_ids": [EVT_MAKERS, TR_Q4_CMT],
     "base_pointers": [B_EVT_DENTSU_A, B_EVT_DENTSU_B], "requirement": "R8",
     "expected_wrong_reading": "follow-up cards for Dentsu Ventures and Makers Fund",
     "resolver": "Fred's calendar after Sep 30: the Dentsu meeting on Wed Oct 1 and 'Michael Cheung and Leonard Hayes' on Wed "
                 "Oct 8 (booked Sep 29); the 2025 list's Partner column has Michael Cheung for Makers Fund; Leonard's Sep 29 "
                 "comment: anyone with a call or meeting on Fred's calendar after Sep 30 doesn't need a card. Makers stays "
                 "Awaiting reply (no call yet at Sep 30)",
     "discovery_order": "all six rev8 baseline runs listed Fred's calendar Sep 3 - Oct 1 only; the Oct 8 call and its "
                        "invitation name only the partner"},
    {"id": "D1", "family": "distractor", "distractor_type": "near_duplicate_record", "services": ["gsheets"],
     "base_pointers": [B_LIST_2024], "requirement": "R1",
     "expected_wrong_reading": "2024 internal investor list used as the population",
     "resolver": "the ask names the 2025 list"},
    {"id": "D2", "family": "distractor", "distractor_type": "non_authoritative_instruction", "services": ["slack"],
     "seeded_ids": [S_EXEC_ARTHUR], "requirement": "R1",
     "expected_wrong_reading": "the send list = only firms Leonard emailed this month",
     "resolver": "Arthur's aside is not the ask; the send-list doc's rules govern"},
    {"id": "D3", "family": "distractor", "distractor_type": "scope_adjacent", "services": ["slack", "gmail"],
     "base_pointers": ["C096HFA5Z8W/1758130464.175719", f"{FRED}/1843000993076735547"], "requirement": "R1",
     "expected_wrong_reading": "Rollic (hypercasual work-for-hire) or Playable Factory added as firms",
     "resolver": "send-list doc: service, publishing and competitor talks are out"},
    {"id": "D4", "family": "distractor", "distractor_type": "stale_summary", "services": ["slack"],
     "base_pointers": [B_BP_TRACKER], "requirement": "R2",
     "expected_wrong_reading": "statuses taken from Leonard's Sep 8 tracker post",
     "resolver": "each firm's later mail and notes"},
    {"id": "D5", "family": "distractor", "distractor_type": "withdrawn_ask", "services": ["gmail"],
     "seeded_ids": [G_ROBERT_ASK], "requirement": "R7",
     "expected_wrong_reading": "every name on the 2025 list put on the send list (Robert's idea)",
     "resolver": "Leonard's ask: 'Let's not, only the people the doc says'"},
    {"id": "D6", "family": "distractor", "distractor_type": "other_title", "services": ["trello"],
     "base_pointers": [B_CARD_INVUPDATE_OLD], "requirement": "R6",
     "expected_wrong_reading": "keep-warm items added to the April 'Investor Update' card",
     "resolver": "the hub and the comment name the Existing Investor Update card"},
    {"id": "D7", "family": "distractor", "distractor_type": "near_duplicate_record", "services": ["gcal"],
     "base_pointers": [B_EVT_DENTSU_A, B_EVT_DENTSU_B], "requirement": "R4",
     "expected_wrong_reading": "two Dentsu meetings read as two firms or as a held meeting",
     "resolver": "one Oct 1 meeting, future at the clock; Dentsu is In talks on its Sep 23 call and, with the meeting "
                 "booked, needs no follow-up card"},
]

CHAINS = [
    {"id": "C1", "root_cause": "A14", "ends_in": "R3", "hops": [
        {"service": "slack", "record": S_EXEC_ANGELS, "finding": "Leonard: Paul Heydon is in for $50K, Anton for $40K"},
        {"service": "gmail", "record": G_DS_PAUL, "finding": "Leonard's Sep 29 nudge: the SAFE is still sitting with Paul"},
        {"service": "slack", "record": S_DM_PAUL_OUT, "finding": "Leonard, Sep 30, in his 1:1 DM with Frederick: Paul's out, he can't put money in this year"}]},
    {"id": "C2", "root_cause": "A14", "ends_in": "R2", "hops": [
        {"service": "gmail", "record": B_SCIPLAY, "finding": "investor: we'll continue to play and let you know"},
        {"service": "gdocs", "record": DOC_TEMPLATE, "finding": "Keep warm: passed after a pitch call; passed = told us no for this round"},
        {"service": "slack", "record": S_EXEC_SCIPLAY_REPLY, "finding": "Robert: SciPlay's contact called, they are out"}]},
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
        {"service": "slack", "record": S_EXEC_SCIPLAY_REPLY, "finding": "SciPlay's pass (one of the members)"}]},
    {"id": "C6", "root_cause": "A7", "ends_in": "R8", "hops": [
        {"service": "trello", "record": TR_Q4_CMT, "finding": "if one already has a card in To Do, comment there instead"},
        {"service": "trello", "record": TR_FU_ANEL, "finding": "open To Do card: F/up with Anel after the engine deep dive"},
        {"service": "gsheets", "record": B_LIST, "finding": "NCsoft: partner Anel Ceman, engine follow-up planned"}]},
    {"id": "C7", "root_cause": "A17", "ends_in": "R8", "hops": [
        {"service": "trello", "record": TR_Q4_CMT, "finding": "no card for anyone with a call or meeting after Sep 30"},
        {"service": "gcal", "record": EVT_MAKERS, "finding": "Michael Cheung and Leonard Hayes, Wed Oct 8 (Makers Fund's partner)"},
        {"service": "gcal", "record": B_EVT_DENTSU_A, "finding": "Harmony Games & Dentsu, Wed Oct 1"}]},
]


def port(pid, mech, nodes, req, natural, fam, why, decides, controls, over):
    return {"id": pid, "mechanism": mech, "nodes": nodes, "requirement": req, "natural_reading": natural,
            "prior_family": fam, "prior_family_reason": why, "decides": decides, "controls": controls,
            "over_application": over}


PORTFOLIO = [
    port("DONE1", "A14", ["T1", "C1"], "R3", "Paul Heydon In talks at $50,000: he said yes and the SAFE is still waiting on him",
         "superseding", "v2 trap 2: the no sits in the 1:1 DM, away from the angel post that announced the yes, worded without the signing words",
         ["V1", "RP2"], ["Anton Bernstein (said yes and signed: stays New investor)"],
         "over-application drops Anton too although nothing says he backed out"),
    port("INPUT", "A11", ["T4"], "R3", "Anton at $40,000 from the #executives post and the Bridge angels sheet",
         "superseding", "v2 trap 8: a later 1:1 DM, away from the post and the sheet, changes an amount on the list",
         ["M3"], ["GFR Fund (in talks, no amount)"],
         "over-application puts an amount on a firm in talks although no note gave one"),
    port("DONE2", "A24", ["T2"], "R4", "T-Accelerate, Dentsu, NCsoft and Brightwater have iOS and Android because the ticket logs both tracks",
         "done_gap", "v2 trap 1: a tester log that reads as done against Arthur's later post in the game channel that the Play tester list never went live",
         ["AC1", "AC2", "AC3", "AC4"], ["GFR Fund (in talks, never added: none)"],
         "over-application gives GFR Fund iOS access as if it had been added"),
    port("CORR", "A14", ["T3", "C2"], "R2", "SciPlay In talks from its own mail thread",
         "superseding", "v2 trap 2: correction in a #executives thread reply under another firm's post, away from the firm's mail",
         ["ST1", "RP3"], ["London Venture Partners (pass in its own mail)"],
         "over-application reads every 'continue to play' firm as passed"),
    port("ALIAS", "A7", ["T5", "C3"], "R2", "Hiro Capital Awaiting reply from the list row",
         "scope_alias", "v2 trap 6: a partner's reply that names no firm; contacts and the earlier thread map it",
         ["ST2", "RP3"], ["Grishin Robotics (GRx pass already on the list as Rejected)"],
         "over-application maps an unrelated partner reply onto a list firm"),
    port("FILT", "A17", ["T6", "T7", "C4"], "R1", "the send list looks only at the 2025 list rows",
         "exact_predicate", "v2 trap 7: two in-scope firms outside the obvious list, found through calendar calls",
         ["V1", "ST3", "ST4", "RP2"], ["Metaplay, Rollic (out: competitor / service talks)"],
         "over-application adds every company with a call (Metaplay, Rollic) to the send list"),
    port("FOLLOW", "A15", ["T8", "C5"], "R6", "no checklists on the card",
         "authority", "v2 trap 3: a follow-through rule in a card comment requires a write per send-list entry",
         ["CL1"], ["Dentsu (in talks, not added to Keep warm)"],
         "over-application adds every contacted firm to Keep warm, not only pitched passes"),
    port("DUP", "A7", ["T12", "C6"], "R8", "a new F/up card for NCsoft: the open To Do card names only Anel",
         "scope_alias", "v2 trap 6: a record named for a partner's first name; the 2025 list's Partner column maps it",
         ["AN1", "FU1"], ["GFR Fund (in talks, no To Do card: gets its own)"],
         "over-application comments on an unrelated open To Do card instead of making GFR's card"),
    port("BOOKED", "A17", ["T13", "C7"], "R8", "follow-up cards for Dentsu and Makers: the calendar is read only through Sep 30, or the Oct 8 call is not tied to Makers",
         "exact_predicate", "v2 trap 7: the exception population sits outside the date window every run lists, and one member is named by its partner",
         ["FU2"], ["BBQ Capital (awaiting reply, nothing booked: gets a card)"],
         "over-application skips a firm with nothing booked"),
]
CHANNELS = [
    {"id": "CH-FILT-HOMA", "kind": "member", "rule": "FILT", "degrade": "drop Homa from the register", "members": ["Homa"],
     "latent": "calendar sweep", "family": "exact_predicate"},
    {"id": "CH-FILT-BRIGHT", "kind": "member", "rule": "FILT", "degrade": "drop Brightwater Games Fund", "members": ["Brightwater Games Fund"],
     "latent": "calendar sweep", "family": "exact_predicate"},
    {"id": "CH-SLIP", "kind": "slip", "degrade": "base slip on control rows", "slots": ["ST5", "RP1", "DL1"]},
]

BUDGET = [
    ("discovery", "gmail", 8, "read the ask and its thread; Robert's Q4 list mail; find the send-list doc, README, draft deck"),
    ("discovery", "gdocs", 5, "read the Q4 send-list doc, the Q3 (July) send list it supersedes, the folder README"),
    ("discovery", "gslides", 3, "open the draft Q4 update deck and read what each group gets"),
    ("discovery", "trello", 8, "find and read the Existing Investor Update card (and the older Investor Update card), comments and checklists"),
    ("discovery", "gdrive", 4, "locate the Q4 2025 investor update folder and list it"),
    ("discovery", "gcal", 6, "Monday's review event; list Sep 3-30 events on Frederick's calendar (two pages)"),
    ("enumeration", "gsheets", 4, "read the 2025 investor list (80 rows, several ranges) and check the 2024 lookalike"),
    ("enumeration", "slack", 22, "#bridge-pitch Jul-Sep history (4 pages at 100) and #executives Sep history (about 12 pages), roots only"),
    ("per-record", "gmail", 169, "one search per firm by name (79), a second by partner for the ~40 firms whose list row or mail names one, and a thread read for each of the ~50 firms with hits; search returns ids only, no bulk"),
    ("per-record", "slack", 124, "one search per firm and angel (79) plus about 45 thread or DM opens where a hit needs its context; replies and DMs are not in channel history"),
    ("per-record", "contacts", 40, "partner lookups for the list's Partner column, person-titled calls and partner-only replies"),
    ("reconciliation", "gcal", 18, "open each person-titled pitch event since Sep 3 for its description and attendees"),
    ("reconciliation", "gmail", 26, "signing-service notices per angel, Anton's and Paul's mails, Dentsu and Brightwater follow-ups, Hiro decline"),
    ("reconciliation", "linear", 6, "find ZOM-567, read it and its comments for each firm in talks"),
    ("reconciliation", "slack", 4, "check Arthur's and Leonard's later word on the tester adds (search by firm, TestFlight, Play)"),
    ("reconciliation", "slack", 29, "open every replied thread in #executives (22) and #bridge-pitch (7) for September: phone notes and corrections live in replies"),
    ("rules", "gdocs", 4, "re-read the send-list doc's definitions while grouping edge firms"),
    ("rules", "slack", 2, "read Leonard's #executives note on what counts as signed"),
    ("rules", "contacts", 6, "check mapping for Karthic/PXLite and Hiro's Investment Director"),
    ("writes", "gsheets", 6, "create the send list and write its 25 rows"),
    ("writes", "gdrive", 2, "place the sheet in the Q4 update folder and confirm"),
    ("writes", "trello", 48, "4 checklists on the card (one per group) and 25 items (one per firm or angel); 18 follow-up "
                             "cards in To Do; 1 comment on the open Anel card (no batch write exists for items or cards)"),
    ("reconciliation", "trello", 3, "list the To Do cards and map each open one to a firm before adding cards"),
    ("reconciliation", "gcal", 2, "list Fred's calendar after Sep 30 for calls already booked with In talks or Awaiting reply firms"),
    ("writes", "gmail", 1, "reply on Leonard's thread"),
    ("read-back", "gsheets", 3, "read back the written ranges and the group counts"),
    ("read-back", "trello", 2, "read the checklist back"),
    ("read-back", "gdrive", 1, "confirm the file's parent folder"),
]

WRITES = [
    {"service": "gsheets", "tool": "gsheets_create_spreadsheet+gsheets_values_update", "count": 3,
     "depends_on": ["K3", "K4", "K5", "K6", "K7", "K11", "K17", "C1", "C2", "C3", "C4", "T1", "T2", "T3", "T4", "T5", "T6", "T7"],
     "requirements": ["R1", "R2", "R3", "R4"]},
    {"service": "gdrive", "tool": "gdrive_move_file", "count": 1, "depends_on": ["K2", "K13", "K16"], "requirements": ["R5"]},
    {"service": "trello", "tool": "trello_create_checklist+trello_create_check_item", "count": 30,
     "depends_on": ["K9", "K18", "C5", "T3", "T5", "T8"], "requirements": ["R6"]},
    {"service": "trello", "tool": "trello_create_card+trello_add_comment", "count": 20,
     "depends_on": ["K18", "C6", "C7", "T12", "T13", "T3", "T5"], "requirements": ["R8"]},
    {"service": "gmail", "tool": "gmail_reply_to_message", "count": 1, "depends_on": ["K1", "C1", "C4", "T1", "T3", "T5"],
     "requirements": ["R7"]},
]

HAZ = [
    {"hazard_id": "Q01", "resolution": "dated_claim", "requirement": "R2",
     "why_safe": "Robert's seeded reply under Leonard's Sep 29 (PT) speedrun post changes that root's reply_count/latest_reply; the SQL updates the counters (companion), and the text is an attributed, dated claim"},
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
    "register": {"kind": "table", "name_regex": r"(?i).*(send|list|q4|update).*", "key_column": "Firm",
                 "key_regex": r".+", "columns": ["Firm", "Group", "Amount", "Build access"],
                 "class_column": "Group", "comparators": {"Group": "norm", "Build access": "norm"}},
    "reply": {"kind": "json_text", "tool": "gmail_reply_to_message"},
    "checklists": {"kind": "json_text", "tool": "trello_create_check_item"},
    "followups": {"kind": "json_text", "tool": "trello_create_card"},
    # the local grader's trello_card check reads card comments under this name (the catalog tool is trello_add_comment;
    # the rubric grades the platform call)
    "cardcomment": {"kind": "calls", "tool": "trello_add_comment_to_card"},
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


SEND_LIST = ['Anton Bernstein', 'GFR Fund', 'London Venture Partners', 'Initial Capital', 'BITKRAFT Ventures', 'Makers Fund', 'Andreessen Horowitz', 'Dentsu Ventures', 'Hiro Capital', 'Raine Ventures', 'General Catalyst', 'BBQ Capital', 'Treo VC', 'T-accelerate', 'NCsoft', 'Sciplay', 'Superplay', 'Sony Mobile', 'Revo Capital', 'e2vc', 'Triptyq', 'Turkven', 'Harlem Capital', 'Homa', 'Brightwater Games Fund']


SLOTS = [
    slot("V1", "send list membership", 3, "limited_reconciliation", "79 names looked at, 25 kept: email-only passes, uncontacted firms and Paul (backed out) off, off-list calls on", "delivery",
         ["delivery", "register_keys_exact"], role="volume", mech=["FILT", "DONE1"], volume_for=["group", "access"], fact="send_list_size"),
    slot("ST1", "SciPlay group", 5, "multi_source_reconciliation", "mail thread vs Robert's #executives thread reply", "direct",
         ["field", "Sciplay", "Group"], role="sample", group="group", mech=["CORR"]),
    slot("ST2", "Hiro Capital group", 5, "multi_source_reconciliation", "list row vs partner-only pass mail vs contacts", "direct",
         ["field", "Hiro Capital", "Group"], role="sample", group="group", mech=["ALIAS"]),
    slot("ST3", "Homa on the send list in talks", 5, "multi_source_reconciliation", "calendar + invitation body + Slack note, off the list", "direct",
         ["field", "Homa", "Group"], role="sample", group="group", mech=["FILT"]),
    slot("ST4", "Brightwater on the send list in talks", 5, "multi_source_reconciliation", "person-titled call + contacts + mail, off the list", "direct",
         ["field", "Brightwater Games Fund", "Group"], role="sample", group="group", mech=["FILT"]),
    slot("ST5", "London Venture Partners group", 3, "interpretation", "pass after a call read from its own thread", "direct",
         ["field", "London Venture Partners", "Group"], role="sample", group="group"),
    slot("AC1", "Dentsu build access", 5, "multi_source_reconciliation", "invite mail and tester ticket vs Arthur's #zombie-match3d post", "direct",
         ["field", "Dentsu Ventures", "Build access"], role="sample", group="access", mech=["DONE2"]),
    slot("AC2", "T-Accelerate build access", 5, "multi_source_reconciliation", "tester ticket vs Arthur's #zombie-match3d post", "direct",
         ["field", "T-accelerate", "Build access"], role="sample", group="access", mech=["DONE2"]),
    slot("AC3", "NCsoft build access", 5, "multi_source_reconciliation", "tester ticket vs Arthur's #zombie-match3d post (rev12)", "direct",
         ["field", "NCsoft", "Build access"], role="sample", group="access", mech=["DONE2"]),
    slot("AC4", "Brightwater build access", 5, "multi_source_reconciliation", "tester ticket vs Arthur's #zombie-match3d post (rev12)", "direct",
         ["field", "Brightwater Games Fund", "Build access"], role="sample", group="access", mech=["DONE2"]),
    slot("M3", "Anton Bernstein amount", 5, "multi_source_reconciliation", "Slack post and angels sheet vs Leonard's DM vs completed notice", "direct",
         ["field", "Anton Bernstein", "Amount"], mech=["INPUT"]),
    slot("G2", "Anton Bernstein group", 3, "interpretation", "signed: the DocuSign Completed notice is in", "direct",
         ["field", "Anton Bernstein", "Group"]),
    slot("RP1", "reply on Leonard's thread", 1, "lookup", "delivery to the named thread", "delivery",
         ["delivery", "email_reply", G_HUB]),
    slot("RP2", "reply gives the In talks count", 5, "multi_source_reconciliation", "7 firms, 0 angels: off-list calls in, Anton out (signed), Paul out (backed out)", "write_content",
         ["text", "reply", r"[Ii]n [Tt]alks.{0,40}7 firms?.{0,12}0 angels?"], mech=["FILT", "DONE1"], fact="in_talks_count"),
    slot("RP3", "reply gives the Keep warm count", 3, "calculation", "3: LVP, Hiro, SciPlay", "write_content",
         ["text", "reply", r"[Kk]eep [Ww]arm.{0,40}3"], mech=["CORR", "ALIAS"], fact="keep_warm_count"),
    slot("DL1", "send list in the Q4 2025 investor update folder", 1, "lookup", "delivery to the named folder", "delivery",
         ["delivery", "register_parent", DRIVE_FOLDER]),
    slot("CL1", "send checklist item for Homa", 3, "interpretation", "card rule applied to an off-list firm found through its call", "write_content",
         ["text", "checklists", r"H[Oo][Mm][Aa]"], mech=["FOLLOW", "FILT"]),
    slot("FU1", "follow-up card for GFR Fund", 3, "interpretation", "in talks, no open To Do card of its own", "write_content",
         ["text", "followups", r"GFR"], mech=["DUP"]),
    slot("FU2", "follow-up card for BBQ Capital", 3, "interpretation", "awaiting reply, nothing booked after Sep 30", "write_content",
         ["text", "followups", r"BBQ"], mech=["BOOKED"]),
    slot("FU3", "follow-up card for Brightwater Games Fund", 3, "interpretation", "off-list firm in talks gets a card too", "write_content",
         ["text", "followups", r"Brightwater"], mech=["FILT"]),
    slot("AN1", "comment on Leonard's open Anel card for NCsoft", 5, "multi_source_reconciliation",
         "To Do card named for NCsoft's partner vs the 2025 list's Partner column", "delivery",
         ["delivery", "trello_card", TR_FU_ANEL, "up"], mech=["DUP"]),
]
SLOTS[0]["expected_keys"] = SEND_LIST

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


surface = {"kind": "GRADABLE_SURFACE", "version": 1, "task": "frederick_bridge_pipeline", "revision": "design-12",
           "truth_keys": truth_keys(),
           "classes": ["New investor", "In talks", "Awaiting reply", "Keep warm"],
           "truth_fields": {"class": "Group", "groups": "groups"},
           "deliverables": DELIV, "slots": SLOTS}

(WF / "01_Hardness_Manifest.draft.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")
(WF / "01_Gradable_Surface.json").write_text(json.dumps(surface, indent=1, ensure_ascii=False) + "\n")
tot = sum(s["weight"] for s in SLOTS)
print("manifest + surface written; surface weight", tot, "calls", sum(b[2] for b in BUDGET),
      "per-record", sum(b[2] for b in BUDGET if b[0] == "per-record"))
print("ids:", G_HUB, S_DM_ANTON, G_DS_ANTON, G_DS_PAUL, G_HIRO, G_DENTSU, G_BRIGHT, G_ROBERT_ASK)
