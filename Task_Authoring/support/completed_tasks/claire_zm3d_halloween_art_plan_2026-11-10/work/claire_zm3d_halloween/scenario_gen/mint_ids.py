#!/usr/bin/env python3
"""Mint the planned seeded ids for the ZM3D Halloween art plan task, deterministically (sha256 of a fixed label), and
write scenario_gen/ids.json. Collision checks run separately (scenario_gen/ids_checks.md). Read-only on the universe.
    python3 -B Task_Authoring/task_inputsN2/Working_Files/scenario_gen/mint_ids.py
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SALT = "n2-claire-zm3d-halloween-art-plan"
N_SURFACES = 62


def h(label: str, n: int) -> str:
    return hashlib.sha256(f"{SALT}|{label}".encode()).hexdigest()[:n]


def epoch(iso: str) -> int:
    return int(datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp())


def slack(channel: str, iso: str, label: str) -> dict:
    micro = int(h(label, 8), 16) % 1_000_000
    ts = f"{epoch(iso)}.{micro:06d}"
    return {"locator": f"{channel}/{ts}", "ts": ts, "channel": channel, "at": iso,
            "row_id": hashlib.sha256(f"{channel}|{ts}".encode()).hexdigest()[:32]}


def trello(iso: str, label: str) -> str:
    return f"{epoch(iso):08x}{h(label, 16)}"


def thread(iso: str, label: str) -> str:
    """A Gmail thread id as Gmail mints it: (ms of the first message << 20) | 20 random bits (base: thrid >> 20 is the
    first message's internal date, e.g. 1842730512689457893 -> 2025-09-08T20:52:42Z)."""
    ms = epoch(iso) * 1000 + int(h(label + "|ms", 4), 16) % 900
    return str((ms << 20) | (int(h(label, 6), 16) & 0xFFFFF))


MAILBOXES = ["claire.morgan@harmonygames.co", "frederick.stone@harmonygames.co", "leonard.hayes@harmonygames.co",
             "marcus.bennett@harmonygames.co", "martin.walsh@harmonygames.co"]


TS = {
    "slack_ask": "2025-09-30T22:05:13Z", "slack_martin_export": "2025-09-30T15:20:41Z",
    "slack_leonard_store_reply": "2025-09-30T15:47:26Z",
    "slack_robert_pointer": "2025-09-25T16:30:22Z", "slack_dm_root": "2025-09-26T07:40:09Z",
    "slack_dm_marcus_reply": "2025-09-29T17:20:37Z", "gmail_fred_draft": "2025-09-12T17:40:00Z",
    "gmail_fred_plan": "2025-09-30T23:10:00Z", "gmail_vendor_quote": "2025-09-24T14:00:00Z",
    "gcal_review_updated": "2025-09-30T22:10:00Z", "gcal_review_start": "2025-10-02T16:00:00Z",
    "sheet_live_modified": "2025-09-30T22:30:00Z", "doc_release_modified": "2025-09-30T22:40:00Z",
    "deck_seasonal_modified": "2025-09-25T16:10:00Z", "folder_created": "2025-09-29T09:15:00Z",
    "files_store_created": "2025-09-30T15:12:00Z", "files_ua_created": "2025-09-29T17:05:00Z",
    "art_issues_created": "2025-09-08T16:00:00Z", "trello_card": "2025-09-30T22:00:00Z",
    "trello_comment": "2025-09-30T23:20:00Z",
    "slack_robert_icon_reply": "2025-09-17T16:52:31Z",
    # revision rev3 (hardening): deciding facts moved off the swept path
    "slack_fred_review_reply": "2025-09-30T23:42:18Z", "slack_marcus_recapture": "2025-09-25T18:12:44Z",
    "slack_marcus_test": "2025-09-29T17:31:05Z", "slack_robert_test_reply": "2025-09-30T16:05:37Z",
    "slack_marcus_test_reply": "2025-09-30T16:21:09Z", "slack_martin_leave": "2025-09-30T14:41:26Z",
    "slack_leonard_leave_reply": "2025-09-30T23:31:47Z", "gmail_fred_restart": "2025-09-29T23:48:00Z",
    "trello_logo_comment": "2025-09-26T17:40:00Z",
}
ATTENDEES = ["claire.morgan@harmonygames.co", "leonard.hayes@harmonygames.co", "frederick.stone@harmonygames.co",
             "martin.walsh@harmonygames.co", "marcus.bennett@harmonygames.co", "robert@harmonygames.co",
             "arthur.blake@harmonygames.co"]
CLAIRE = "claire.morgan@harmonygames.co"

ids = {
    "slack_ask": slack("C06DJBJL798", TS["slack_ask"], "ask"),
    "slack_martin_export": slack("C08R8CHB0QL", TS["slack_martin_export"], "export"),
    # revision 04: Leonard's thread reply under Martin's export post settles which store art gets a ticket (/prompt issue 1)
    "slack_leonard_store_reply": slack("C08R8CHB0QL", TS["slack_leonard_store_reply"], "storereply"),
    "slack_robert_pointer": slack("C08R8CHB0QL", TS["slack_robert_pointer"], "pointer"),
    "slack_dm_root": slack("D05V2N6PZNU", TS["slack_dm_root"], "dmroot"),
    "slack_dm_marcus_reply": slack("D05V2N6PZNU", TS["slack_dm_marcus_reply"], "dmreply"),
    # revision 03: Robert's thread reply under Martin's base Sep 17 icon concept C08R8CHB0QL/1758121809.236839
    "slack_robert_icon_reply": slack("C08R8CHB0QL", TS["slack_robert_icon_reply"], "iconreply"),
    # revision rev3: Frederick's reply in the Sep 30 fake-installs thread C0880U9751A/1759211437.306779 (Android review window)
    "slack_fred_review_reply": slack("C0880U9751A", TS["slack_fred_review_reply"], "reviewreply"),
    # revision rev3: Marcus's re-capture note in #zm-animations (the note left the three tickets)
    "slack_marcus_recapture": slack("C09ATAJ220H", TS["slack_marcus_recapture"], "recapnote"),
    # revision rev3: Marcus's test post in #zombie-art and Robert's review in its thread (the test cannot ship)
    "slack_marcus_test": slack("C08R8CHB0QL", TS["slack_marcus_test"], "testpost"),
    "slack_robert_test_reply": slack("C08R8CHB0QL", TS["slack_robert_test_reply"], "testreview"),
    "slack_marcus_test_reply": slack("C08R8CHB0QL", TS["slack_marcus_test_reply"], "testack"),
    # revision rev3: Martin's vacation post in #company-internal with Leonard's reply (Julia takes the ad statics)
    "slack_martin_leave": slack("C05KNDCHAAG", TS["slack_martin_leave"], "leavepost"),
    "slack_leonard_leave_reply": slack("C05KNDCHAAG", TS["slack_leonard_leave_reply"], "leavereply"),
    # Gmail thread ids inside the date-consistent ranges of Claire's mailbox (ids_checks.md); message ids RFC-style
    "gmail_fred_draft": {"thread": f"{CLAIRE}/" + thread(TS["gmail_fred_draft"], f"draft|{CLAIRE}"),
                         "copies": {m: f"{m}/" + thread(TS["gmail_fred_draft"], f"draft|{m}") for m in MAILBOXES},
                         "msg": f"{CLAIRE}/<CANf1Nx{h('draftmsg', 31)}@mail.gmail.com>"},
    "gmail_fred_plan": {"thread": f"{CLAIRE}/" + thread(TS["gmail_fred_plan"], f"plan|{CLAIRE}"),
                        "copies": {m: f"{m}/" + thread(TS["gmail_fred_plan"], f"plan|{m}") for m in MAILBOXES},
                        "msg": f"{CLAIRE}/<CANf1Nx{h('planmsg', 31)}@mail.gmail.com>"},
    # revision rev3: Frederick's Sep 29 restart mail (two landscape cuts left off iOS UK tablet)
    "gmail_fred_restart": {"thread": f"{CLAIRE}/" + thread(TS["gmail_fred_restart"], f"restart|{CLAIRE}"),
                           "copies": {m: f"{m}/" + thread(TS["gmail_fred_restart"], f"restart|{m}") for m in MAILBOXES},
                           "msg": f"{CLAIRE}/<CANf1Nx{h('restartmsg', 31)}@mail.gmail.com>"},
    "gmail_vendor_quote": {"thread": f"{CLAIRE}/" + thread(TS["gmail_vendor_quote"], f"quote|{CLAIRE}"),
                           "msg": f"{CLAIRE}/<CAJ{h('quotemsg', 30)}@mail.gmail.com>",
                           "sender": "PERSON_6311_EMAIL", "sender_name": "[PERSON_NAME_6311]"},
    "gcal_review": {"ical_uid": f"{h('review_uid', 32)}@hg4",
                    "evt_by_calendar": {a: "evt_" + h(f"review_evt|{a}", 22) for a in ATTENDEES}},
    "sheet_live": "f_" + h("sheet_live", 22),
    "doc_release": "f_" + h("doc_release", 22),
    "deck_seasonal": {"presentation": "f_" + h("deck_seasonal", 22),
                      "slides": ["slide_" + h(f"slide{i}", 12) for i in range(4)],
                      "elements": ["el_" + h(f"el{i}", 12) for i in range(8)]},
    "folder_halloween": {"root": "d_" + h("folder_root", 22), "store": "d_" + h("folder_store", 22),
                         "ua": "d_" + h("folder_ua", 22)},
    "files_store": ["f_" + h(f"store_file{i}", 22) for i in range(11)],
    "files_ua": ["f_" + h(f"ua_file{i}", 22) for i in range(2)],
    "files_store_ipad_live": ["f_" + h(f"store_ipad_live{i}", 22) for i in range(5)],
    "art_issues": [f"ART-{793 + i}" for i in range(N_SURFACES)],
    "linear_comments": [f"cmt_art{793 + i}_1" for i in range(N_SURFACES)]
                       + [f"cmt_art{793 + i}_2" for i in range(N_SURFACES)],
    "contact_vendor": h("contact_vendor", 24),
    "trello_card": trello(TS["trello_card"], "card"),
    "trello_card_create_action": trello(TS["trello_card"], "card_create"),
    "trello_comment": trello(TS["trello_comment"], "comment"),
    # revision rev3: Frederick's comment on the base Marketing Video Refresh card (old logo on end card 001 and its cuts)
    "trello_logo_comment": trello(TS["trello_logo_comment"], "logocomment"),
    "trello_id_short": 80,
    "trello_list_oct21": "6851a677e090018224fb8c7f",
}

(HERE / "ids.json").write_text(json.dumps({"ids": ids, "timestamps": TS,
                                           "notes": {"salt": SALT, "slack_row_id": "sha256(channel|ts)[:32]",
                                                     "gmail": "thread id = (first message ms << 20) | 20 random bits, one per mailbox copy; message ids per sender style (Frederick: CANf1Nx...)",
                                                     "linear_comments": "cmt_<issue>_<n> as in the sibling task's accepted SQL",
                                                     "trello": "first 8 hex = unix seconds of the record time"}},
                                          indent=1) + "\n")
print("ids.json written:", len(ids["art_issues"]), "ART issues,", len(ids["linear_comments"]), "comment ids")
