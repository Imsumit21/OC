#!/usr/bin/env python3
"""Generator for the scenario-stage artifacts of the Claire Morgan ZM3D Halloween art plan task (design only, no SQL).

Writes Working_Files/01_Hardness_Manifest.draft.json, Working_Files/01_Gradable_Surface.json and
scenario_gen/truth.json from the data below + ids.json (minted, collision-checked ids) + roster_final.json (the 50
serving surfaces, grounded in base records by finalize_roster.py) + planned_texts.json (verbatim planned texts of the
seeded records). Read-only on the universe; run from the workspace root:
    python3 -B Task_Authoring/task_inputsN2/Working_Files/scenario_gen/build_design.py
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
TASK = HERE.parents[1]
WF = TASK / "Working_Files"
CTX = json.loads((WF / "00_Task_Context.json").read_text())
IDS = json.loads((HERE / "ids.json").read_text())["ids"]
FINAL = json.loads((HERE / "roster_final.json").read_text())
ROSTER = FINAL["surfaces"]
ARCHIVED = FINAL["archived"]
TEXT = json.loads((HERE / "planned_texts.json").read_text())


def q(key: str, phrase: str) -> str:
    """A delegation / naming quote: must be an exact substring of the planned text of `key`."""
    blob = json.dumps(TEXT[key], ensure_ascii=False)
    if json.dumps(phrase, ensure_ascii=False)[1:-1] not in blob:
        raise SystemExit(f"quote not in planned text of {key}: {phrase!r}")
    return phrase


def slack_loc(v) -> str:
    return v["locator"] if isinstance(v, dict) else v


# ------------------------------------------------------------------ planned seeded records (ids from ids.json)
ASK = slack_loc(IDS["slack_ask"])                    # A1: Leonard's #zombie_marketing Halloween ask (Sep 30 22:05Z)
POINTER = slack_loc(IDS["slack_robert_pointer"])     # Robert's #zombie-art post naming his deck (Sep 25)
EXPORT = slack_loc(IDS["slack_martin_export"])       # Martin's #zombie-art 'store screens exported' (Sep 30)
DM_ROOT = slack_loc(IDS["slack_dm_root"])            # Claire's DM to Marcus (Sep 26)
DM_REPLY = slack_loc(IDS["slack_dm_marcus_reply"])   # Marcus's thread reply: Halloween cheer fastcouch cuts done (Sep 29)
SHEET = IDS["sheet_live"]                            # H1: Frederick's 'ZM3D live creatives'
DOC = IDS["doc_release"]                             # H2: Arthur's 'ZM3D release calendar — Q4'
DECK = IDS["deck_seasonal"]["presentation"]          # H3: Robert's 'Seasonal art direction — Q4 2025'
MAIL_PLAN = IDS["gmail_fred_plan"]["msg"]            # H4: Frederick's 'October UA plan - changes' (Sep 30)
MAIL_DRAFT = IDS["gmail_fred_draft"]["msg"]          # Frederick's 'October UA plan (draft)' (Sep 12, superseded)
MAIL_PLAN_T = IDS["gmail_fred_plan"]["thread"]
MAIL_DRAFT_T = IDS["gmail_fred_draft"]["thread"]
QUOTE = IDS["gmail_vendor_quote"]["msg"]             # vendor quote for the Halloween Bits bundle (Sep 24)
QUOTE_T = IDS["gmail_vendor_quote"]["thread"]
CONTACT = IDS["contact_vendor"]                      # Contacts: the quote's sender is KayKit's founder
CARD = IDS["trello_card"]                            # Leonard's 'Halloween push' card (ZM ROADMAP)
CARD_CMT = IDS["trello_comment"]                     # Frederick's comment: Julia's 4:5 static is still running
REVIEW_UID = IDS["gcal_review"]["ical_uid"]
REVIEW_EVT = IDS["gcal_review"]["evt_by_calendar"]["claire.morgan@harmonygames.co"]
FOLDER = IDS["folder_halloween"]
STORE_FILES = IDS["files_store"]
UA_FILES = IDS["files_ua"]

# base records (read through tools/hg.py; ids verified in the pre-scenario analysis and the Phase-1 census)
HALLOWEEN_ICON = "C08R8CHB0QL/1758121809.236839"     # Martin, Sep 17: Halloween icon concept (no replies)
PACK_MSG = "C0880U9751A/1738109783.735889"           # Robert, Jan 28: 'we have the Halloween pack'
SWAP_1232 = "C0880U9751A/1753820524.488479"          # Robert, Jul 29: iOS 1232, zombie swap with new background
EXPORT_SEP3 = "C06DJBJL798/1756914854.743319"        # Leonard, Sep 3: export iphone/ipad/gp
SFX_RULE = "C06DJBJL798/1755116786.755519"           # Leonard, Aug 13: record SFX without music
CUT_30S = "C06DJBJL798/1755114007.441789"            # Frederick, Aug 13: 30 s UA cut, music baked in
END_CARD = "C06DJBJL798/1753968186.965269"           # Marcus, Jul 31: portrait UA end card
ART774 = "ART-774"                                   # store screenshot spec (Done 2025-04-15)
PACK_REPO = "harmonygames-Games/match3d:Assets/ThirdParty/3D Characters/KayKit/Packs/Bits/KayKit - Halloween Bits (For Unity)"
PROJSET = "harmonygames-Games/match3d:ProjectSettings/ProjectSettings.asset"
CHECKLIST = "page_release_checklist"                 # Confluence (decoy for H2: no dates)
DD_CAPTURE = "f_b5fb884dc96261846b6c2c"              # 'Video Capture Requests for UA' (Domino Delights; decoy for H1)
DD_HALLOWEEN = "C04V7N09LE7/1726011239.339499"       # Robert's 2024 Domino Delights Halloween icon asks (decoy for H3)
POD_0929 = "claire.morgan@harmonygames.co/1844625524254242367"  # POD notes Sep 29 (endless-mode themes)
BUILD_1450 = "C05433XK267/1753789877.590639"         # #builds: Match3D Android #1450 success, Jul 29 11:51Z (before #1452)
BUILD_1452 = "C05433XK267/1753820674.990309"         # #builds: Match3D Android #1452 success, Jul 29 20:24Z
AD_SPEND = "snowflake:ANALYTICS.MARKETING.AD_SPEND_DAILY"

# ------------------------------------------------------------------ the cohort (50 serving surfaces)
CALLS = ["HALLOWEEN VERSION", "REFRESH FIRST", "REUSE", "SKIP"]
CALL_WORD = {"Halloween version": "HALLOWEEN VERSION", "Refresh first": "REFRESH FIRST", "Reuse": "REUSE",
             "Skip October": "SKIP"}
for r in ROSTER:
    r["call_word"] = CALL_WORD[r["call"]]
KEYS = [r["key"] for r in ROSTER]
BY = {r["key"]: r for r in ROSTER}
COHORT = len(ROSTER)
ADS = [r for r in ROSTER if r.get("ticket")]
N_ADS = len(ADS)
N_ASSIGN = sum(1 for r in ADS if r.get("assign_to"))
N_READ = N_ADS   # campaigns live only in the ticket comments: every ad ticket read decides a call
TICKETS = [r["ticket"] for r in ADS]
LIBRARY = TICKETS + [a["ticket"] for a in ARCHIVED]
CMT1 = {r["ticket"]: f"cmt_art{r['ticket'][4:]}_1" for r in ADS}
CMT2 = {r["ticket"]: f"cmt_art{r['ticket'][4:]}_2" for r in ADS if r.get("comment_2")}
OFF_SHEET = [r["key"] for r in ROSTER if not r["on_sheet"]]


def one(key: str) -> dict:
    if key not in BY:
        raise SystemExit(f"roster has no surface {key!r}")
    return BY[key]


ICON, IPAD, IPHONE, GP = "app icon", 'iPad 12.9" set', 'iPhone 6.5" set', "Google Play phone set"
REUSE_CUTS = ["cheer fastcouch 9:16", "cheer fastcouch 16:9"]
OLD_BUILD = ["boris fastcouch 9:16", "boris alin2 9:16"]
MUSIC = "marcus.bennett 9:16"
RECAP = ["couch alpha 50", "barrel marketing2 4:5", "balloons alpha 50 (1)"]
SKIP_MUSIC = "cheer 30p 16:9"                        # tablet-only and music baked in: Skip beats Refresh first
TWO_TABLETS = "couch alpha 50 16:9"                  # on iOS UK tablet too: not skipped (over-application control)
STATIC_OFF, ENDCARD_OFF = "julia 4:5", "marcus portrait UA end card"
CHEER_45 = "cheer fastcouch 4:5"                     # cut from the Sep 16 re-capture; Marcus's DM covers the 9:16 and 16:9 only
SKIP_STATIC = "julia 1:1 android tablet"             # a still that runs only on Android US tablet: Skip applies to stills too
RECAP_TAB = "balloons alpha 50 (1) 16:9"             # cut from a re-capture, on both tablets: kept, Halloween version
HV_SAMPLE = ["marcus.bennett 4:5", "end card 001"]
RF_SAMPLE = ["couch boss 30", "julia 1:1"]
DUE_AD = "marcus.bennett 1:1"
for k in [ICON, IPAD, IPHONE, GP, MUSIC, SKIP_MUSIC, TWO_TABLETS, STATIC_OFF, ENDCARD_OFF, DUE_AD, CHEER_45, SKIP_STATIC,
          RECAP_TAB] + REUSE_CUTS + OLD_BUILD + RECAP + HV_SAMPLE + RF_SAMPLE:
    one(k)
assert [one(k)["call"] for k in REUSE_CUTS] == ["Reuse", "Reuse"]
assert all(one(k)["call"] == "Refresh first" for k in OLD_BUILD + [MUSIC, STATIC_OFF, ENDCARD_OFF, TWO_TABLETS] + RF_SAMPLE)
assert all(one(k)["call"] == "Halloween version" for k in RECAP + HV_SAMPLE + [ICON, IPAD, DUE_AD, CHEER_45, RECAP_TAB])
assert one(SKIP_STATIC)["call"] == "Skip October"
assert one(SKIP_MUSIC)["call"] == "Skip October" and sorted(OFF_SHEET) == sorted([STATIC_OFF, ENDCARD_OFF])
T_BORIS, T_ALIN = one(OLD_BUILD[0])["ticket"], one(OLD_BUILD[1])["ticket"]
T_MUSIC, T_ENDCARD, T_STATIC = one(MUSIC)["ticket"], one(ENDCARD_OFF)["ticket"], one(STATIC_OFF)["ticket"]
T_RECAP = [one(k)["ticket"] for k in RECAP]
T_CHEER = one(REUSE_CUTS[0])["ticket"]
T_CHEER45 = one(CHEER_45)["ticket"]
N_SHEET_ADS = sum(1 for r in ADS if r["on_sheet"])

# ------------------------------------------------------------------ requirements
REQ = {
    "R1": "Tracker scope: one row per ZM3D marketing surface players see on Sep 30 - the store listing sets, the app icon and every ad creative serving on Unity, statics and end cards included, wherever it is recorded; paused creatives are out",
    "R2": "Halloween call per surface (Halloween version / Refresh first / Reuse / Skip): an ad captured or rendered from a build older than the zombie swap build (Android #1452 / iOS 1232), or with the music baked into its master, is refreshed first unless a later re-capture replaced it",
    "R3": "Ship route for the store and icon pieces: what ships inside the app goes in the Oct 17 store build; iOS screenshots go up with that submission; Google Play listing graphics upload any day",
    "R4": "Art due date for the store and icon pieces, set by the build cut (Thu Oct 16 12:00 PT for anything inside the app and for new iOS screenshots)",
    "R5": "Art due date for the ad pieces, set by the UA flight (every Halloween ad with Frederick by Wed Oct 15)",
    "R6": "Halloween call Skip only for creatives that run on nothing but the Android US tablet campaign, which ends before the flight",
    "R7": "Reuse: Halloween work already made and art the studio already owns (the KayKit Halloween Bits pack) are reused, not re-requested or bought",
    "R8": "Owner per new piece: Martin Walsh for the icon and the stills, Marcus Bennett for video and end cards; each ad that needs new work is assigned to its maker on its ART ticket, Reuse and Skip ads are not",
    "R9": "Follow-through: each ad's Halloween call and due date go on its ART ticket as a comment (Leonard asks for a comment), and new store art gets its own ticket",
    "R10": "Delivery: a plan doc and a tracker Claire owns, shared with the team, and the links posted in Leonard's thread before Thursday's review",
}

SERVICES = {
    "slack": {"role": "the ask and reply thread, Robert's pointer to his deck, Martin's export claim, Marcus's completion note, base art-refresh posts",
              "weight_reason": "Leonard's ask is the anchor, scope, follow-through and reply destination (R1, R9, R10); Marcus's DM thread reply is the only record that the two cheer fastcouch cuts already have Halloween versions (R7); Martin's post is the convincing done claim (R2); base #zombie-match3d and #builds posts date the zombie swap build (R2)"},
    "gsheets": {"role": "H1: the live creatives sheet (cohort definition)",
                "weight_reason": "Frederick's 'ZM3D live creatives' defines what is serving (R1) and links every ad to its ART ticket, whose comments carry its campaigns; its Store tab fixes the live store sets (R2)"},
    "gdocs": {"role": "H2: Arthur's Q4 release calendar",
              "weight_reason": "the only record of the Halloween build cut, the iOS screenshot rule and the Play listing route (R3, R4)"},
    "gslides": {"role": "H3: Robert's seasonal art direction deck",
                "weight_reason": "sets the refresh-first rule by source build and master audio, the newest-capture rule and the call words (R2)"},
    "gmail": {"role": "H4: Frederick's October UA plan and its superseded draft; the vendor quote",
              "weight_reason": "the Sep 30 mail moves the ad due date to Oct 15 and ends the Android US tablet campaign (R5, R6); the vendor quote is the purchase decoy (R7)"},
    "linear": {"role": "the per-creative ART library tickets: campaigns, source build and master audio in comments; follow-through destination",
               "weight_reason": "each ad's campaigns, source build, master audio and any re-capture live only in its ticket comments (R2, R6); the calls go back on the tickets as comments and new store art gets tickets (R9); the off-sheet end card is serving per its ticket (R1)"},
    "gdrive": {"role": "the Halloween delivery folders and ownership of the write targets",
               "weight_reason": "the Store folder shows which Halloween store sets exist (R2: the iPad set is missing); the UA masters folder holds the two finished Halloween cuts (R7); Claire's created doc and sheet are hers to share (R10)"},
    "github": {"role": "what the studio already owns and what ships in the build",
               "weight_reason": "the match3d repo holds the KayKit Halloween Bits pack the quote offers (R7) and the icon settings that ship in the build (R3)"},
    "trello": {"role": "the Halloween push card and Frederick's scope comment",
               "weight_reason": "Frederick's comment on the card the sheet's Read me names is the only record that Julia's 4:5 static is still running although it is not on the sheet (R1)"},
    "contacts": {"role": "vendor identity",
                 "weight_reason": "the quote's sender resolves to KayKit's founder, linking the 'Halloween Bits bundle' to the pack already in the repo (R7)"},
    "gcal": {"role": "the reply deadline",
             "weight_reason": "Thursday's 'ZM3D Halloween review' (Oct 2 16:00Z) is the deadline the ask names (R10)"},
    "confluence": {"role": "decoy for the release dates",
                   "weight_reason": "the release checklist is the convincing but undated source for store submissions; the calendar doc governs (R3)"},
    "snowflake": {"role": "network context",
                  "weight_reason": "AD_SPEND_DAILY shows Unity as the only network with ZM3D rows after Aug 11, consistent with the four Unity campaigns the sheet's Read me names (R1)"},
}

ANCHORS = [
    {"id": "A1", "prompt_reference": "Leonard's Halloween message", "service": "slack", "locator": ASK,
     "seeded_ids": [ASK], "container": f"slack:{ASK}", "requirement_ids": ["R1", "R8", "R10"]},
]


def frag(fid, service, container, kind, via, seeded=None, base=None, by=None, quote=None, reqs=(), names=None):
    f = {"id": fid, "service": service, "container": container, "locator": (seeded or base)[0], "kind": kind,
         "incorporated_via": via, "seeded_ids": list(seeded or []), "base_pointers": list(base or []),
         "delegated_by_record": by, "delegation_quote": quote, "requirement_ids": list(reqs)}
    if names:
        f["names_authorities"] = names
    return f


FRAGMENTS = [
    frag("K1", "gsheets", f"file:{SHEET}", "requirement", ["A1"], seeded=[SHEET], by=ASK,
         quote=q("slack_ask", "the live creatives sheet is what's running"), reqs=["R1"]),
    frag("K2", "gdocs", f"file:{DOC}", "requirement", ["A1"], seeded=[DOC], by=ASK,
         quote=q("slack_ask", "Arthur's release calendar has the Q4 dates"), reqs=["R3", "R4"]),
    frag("K3", "slack", f"slack:{POINTER}", "delegation", ["A1"], seeded=[POINTER], by=ASK,
         quote=q("slack_ask", "Robert has direction for seasonal art"), reqs=["R2"],
         names=[{"id": "H3", "quote": q("slack_robert_pointer", "seasonal art direction for Q4 is in my deck")}]),
    frag("K4", "gslides", f"file:{DECK}", "requirement", ["A1", "K3"], seeded=[DECK], by=POINTER,
         quote=q("slack_robert_pointer", "seasonal art direction for Q4 is in my deck"), reqs=["R2"]),
    frag("K5", "gmail", f"gmail:{MAIL_PLAN_T}", "amendment", ["A1"], seeded=[MAIL_PLAN], by=ASK,
         quote=q("slack_ask", "Frederick is sending his october UA plan tonight"), reqs=["R5", "R6"]),
    frag("K6", "gmail", f"gmail:{MAIL_DRAFT_T}", "requirement", ["A1", "K5"], seeded=[MAIL_DRAFT], by=MAIL_PLAN,
         quote=q("gmail_fred_plan", "the October plan I sent on the 12th"), reqs=["R5"]),
    frag("K7", "trello", f"trello:{CARD}", "requirement", ["A1", "K1"], seeded=[CARD, CARD_CMT], by=SHEET,
         quote=q("sheet_live", "see the Halloween push card on the ZM roadmap"), reqs=["R1"]),
    frag("K8", "gcal", f"gcal:{REVIEW_UID}", "destination", ["A1"], seeded=[REVIEW_EVT], by=ASK,
         quote=q("slack_ask", "before thursday's review"), reqs=["R10"]),
    frag("K9", "slack", f"slack:{ASK}", "recipient", ["A1"], seeded=[ASK], by=ASK,
         quote=q("slack_ask", "Martin has the icon and the stills, Marcus has video and end cards"), reqs=["R8"]),
    frag("K10", "slack", f"slack:{ASK}", "exclusion", ["A1"], seeded=[ASK], by=ASK,
         quote=q("slack_ask", "what we already have"), reqs=["R7"]),
    frag("K11", "linear", f"linear:{TICKETS[0]}", "requirement", ["A1", "K1"], seeded=LIBRARY, by=SHEET,
         quote=q("sheet_live", "capture and master notes are in the ticket comments"), reqs=["R2", "R6", "R9"]),
    frag("K15", "slack", f"slack:{EXPORT}", "requirement", ["A1"], seeded=[EXPORT], by=ASK,
         quote=q("slack_ask", "Martin has the icon and the stills"), reqs=["R2"]),
    frag("K12", "gdrive", f"file:{FOLDER['root']}", "requirement", ["A1", "K15"], seeded=[FOLDER["root"], FOLDER["store"], FOLDER["ua"]],
         by=EXPORT, quote=q("slack_martin_export", "exported to the halloween folder"), reqs=["R7", "R2"]),
    frag("K16", "slack", f"slack:{DM_ROOT}", "requirement", ["A1"], seeded=[DM_ROOT, DM_REPLY], by=ASK,
         quote=q("slack_ask", "Marcus has video and end cards"), reqs=["R7"]),
    frag("K13", "slack", f"slack:{ASK}", "format", ["A1"], seeded=[ASK], by=ASK,
         quote=q("slack_ask", "put it all in a plan doc we can comment on plus a tracker"), reqs=["R10"]),
    frag("K14", "slack", f"slack:{ASK}", "requirement", ["A1"], seeded=[ASK], by=ASK,
         quote=q("slack_ask", "drop a comment on each ad's ART ticket with its call and due date"), reqs=["R9"]),
    frag("K17", "slack", f"slack:{ASK}", "recipient", ["A1"], seeded=[ASK], by=ASK,
         quote=q("slack_ask", "assign the ones that need new work to whoever's making them"), reqs=["R8"]),
]

AUTHORITIES = [
    {"id": "H1", "name": "the live creatives sheet", "home_service": "gsheets", "decoy_service": "gsheets",
     "governs": ["R1"], "findable_query": "live creatives", "seeded_ids": [SHEET],
     "decoy_base_pointers": [DD_CAPTURE],
     "decoy_scope": {"dimension": "game", "decoy": "Domino Delights capture list (Video Capture Requests for UA, 2024)",
                     "task": "Zombie Match 3D creatives serving on Unity, Sep 30 2025"}},
    {"id": "H2", "name": "Arthur's Q4 release calendar", "home_service": "gdocs", "decoy_service": "slack",
     "governs": ["R3", "R4"], "findable_query": "release calendar", "seeded_ids": [DOC],
     "decoy_seeded_ids": [ASK]},
    {"id": "H3", "name": "Robert's seasonal art direction", "home_service": "gslides", "decoy_service": "slack",
     "governs": ["R2"], "findable_query": "seasonal art direction", "seeded_ids": [DECK],
     "decoy_base_pointers": [DD_HALLOWEEN],
     "decoy_scope": {"dimension": "game", "decoy": "Domino Delights 2024 Halloween icons",
                     "task": "Zombie Match 3D Q4 2025 marketing art"}},
    {"id": "H4", "name": "Frederick's October UA plan", "home_service": "gmail", "decoy_service": "gmail",
     "governs": ["R5", "R6"], "findable_query": "October UA plan", "seeded_ids": [MAIL_PLAN],
     "decoy_seeded_ids": [MAIL_DRAFT]},
]


def vrec(service, rid, at, seeded, container=None):
    v = {"service": service, ("id" if seeded else "base_pointer"): rid, "seeded": seeded, "at": at}
    if container:
        v["container"] = container
    return v


COHORT_SPEC = {
    "definition_source": "K1", "key": "surface", "size": COHORT, "members": KEYS,
    "evidence_surfaces": [
        {"service": "linear", "tool": "linear_list_comments", "per_record_calls": 1.0, "records": N_ADS,
         "seeded": True, "seeded_ids": [CMT1[t] for t in TICKETS] + list(CMT2.values()),
         "why_no_bulk": "linear_list_issues and linear_get_issue return titles, states and descriptions but never comments; each ad's campaigns, source build, master audio and any later re-capture are only in its own ticket comments (no bulk comment endpoint)",
         "short_circuit": "the sheet and the ticket descriptions carry no campaign, source build or master (no-leak), so even a Skip (tablet-only) or Reuse call needs the ticket's campaign note; the post date and the sheet's 'live since' mislead both ways (Sep 12 boris cuts captured Jul 28, April cuts re-captured in September), so no run can settle an ad's call without its comments",
         "requirement": "R2", "decides": "Halloween call per surface"},
        {"service": "gdrive", "tool": "gdrive_list_folder", "per_record_calls": 1.0, "records": 3,
         "seeded": True, "seeded_ids": [FOLDER["root"], FOLDER["store"], FOLDER["ua"]],
         "why_no_bulk": "gdrive_search by name returns files without their folder context; which Halloween sets and cuts exist is read per delivery folder (root, Store, UA masters)",
         "short_circuit": "Martin's 'exported' post and Marcus's DM note say what was made; only the folders show the iPad set is absent and the two cuts are there",
         "requirement": "R7", "decides": "Halloween work already made"},
        {"service": "slack", "tool": "slack_read_thread", "per_record_calls": 1.0, "records": 6,
         "seeded": False, "base_pointers": [CUT_30S, END_CARD, SFX_RULE],
         "note": "one read is unconditional: the 30 s cut's ticket sends the master note to Frederick's Aug 13 thread (budget row per-record/slack 1)",
         "why_no_bulk": "a base cut's origin post shows who made it and when, but the feedback in its thread (music baked in, SFX stripped) is only in the replies; channel history never lists replies",
         "short_circuit": "the ticket comment already states the master; the thread only confirms it where a run doubts the comment",
         "requirement": "R2", "decides": "Halloween call per surface", "conditional_on": "runs that confirm a ticket's master note against the cut's origin thread"},
    ],
}

TRAPS = [
    {"id": "T1", "family": "done_gap", "services": ["slack", "gdrive", "gsheets"],
     "seeded_ids": [EXPORT, FOLDER["store"], SHEET], "base_pointers": [EXPORT_SEP3], "requirement": "R2",
     "expected_wrong_reading": "Martin says the Halloween store screens are exported, so every store set has a Halloween version (Reuse)",
     "resolver": "the Halloween Store folder holds the iPhone 6.5-inch and Google Play phone sets only; the iPad 12.9-inch set the Store tab lists (and Leonard's Sep 3 'iphone/ipad/gp' export) has none, so the iPad set is a Halloween version still to make and needs its own ticket",
     "discovery_order": "the claim is in #zombie-art where Claire works; the gap shows only in the Drive folder listing against the Store tab"},
    {"id": "T2", "family": "superseding", "services": ["slack", "gdocs", "github"],
     "seeded_ids": [ASK, DOC], "base_pointers": [PROJSET], "requirement": "R4",
     "expected_wrong_reading": "swap the Halloween icon around the 24th, as Leonard suggests: the icon is due about then",
     "resolver": "Arthur's release calendar: anything inside the app, the app icon included, must be merged by Thu Oct 16 12:00 PT for the Oct 17 submission, the last build that can carry Halloween changes (live from about Oct 22)",
     "discovery_order": "the swap date is in the ask everyone reads first; the cut is in a doc the ask names only by owner",
     "version_records": [vrec("slack", ASK, "2025-09-30T22:05:13Z", True, f"slack:{ASK}"),
                         vrec("gdocs", DOC, "2025-09-30T22:40:00Z", True, f"file:{DOC}")]},
    {"id": "T3", "family": "completion_elsewhere", "services": ["slack", "gdrive", "linear"],
     "seeded_ids": [DM_ROOT, DM_REPLY, FOLDER["ua"], T_CHEER] + UA_FILES, "requirement": "R7",
     "expected_wrong_reading": "every current cut, cheer fastcouch included, still needs a Halloween version from Marcus",
     "resolver": "Marcus's reply in Claire's DM thread (Sep 29): both cheer fastcouch cuts already have Halloween versions made from the September re-capture's no-music masters, in the Halloween folder's UA masters; call Reuse",
     "discovery_order": "the ask and the sheet list cheer fastcouch as a live cut; the completion is a thread reply in a DM, which channel history does not list"},
    {"id": "T4", "family": "superseding", "services": ["gmail", "slack"],
     "seeded_ids": [MAIL_DRAFT, MAIL_PLAN], "requirement": "R5",
     "expected_wrong_reading": "Halloween ad art is due Fri Oct 17 for an Oct 20-31 flight on all four campaigns (the Sep 12 draft)",
     "resolver": "Frederick's Sep 30 mail: the flight moves to Oct 18-31, every Halloween ad is due with him Wed Oct 15, and the Android US tablet campaign ends Oct 12",
     "discovery_order": "a Gmail search for the October UA plan returns the draft and the changes mail as two separate threads; the draft has the fuller plan",
     "version_records": [vrec("gmail", MAIL_DRAFT, "2025-09-12T17:40:00Z", True, f"gmail:{MAIL_DRAFT_T}"),
                         vrec("slack", ASK, "2025-09-30T22:05:13Z", True, f"slack:{ASK}"),
                         vrec("gmail", MAIL_PLAN, "2025-09-30T23:10:00Z", True, f"gmail:{MAIL_PLAN_T}")]},
    {"id": "T5", "family": "superseding", "services": ["linear", "slack", "gsheets"],
     "seeded_ids": [SHEET], "base_pointers": [ART774, EXPORT_SEP3], "requirement": "R1",
     "expected_wrong_reading": "the store surfaces are every size ART-774 lists (iPhone 6.5 and 5.5, three iPad sizes, Play phone and tablet)",
     "resolver": "Leonard's Sep 3 export ask and the sheet's Store tab: the live store sets are iPhone 6.5-inch, iPad 12.9-inch and the Google Play phone set, plus the icon",
     "discovery_order": "ART-774 is the only store spec a ticket search returns; the live sets are on the Store tab",
     "version_records": [vrec("linear", ART774, "2025-03-10T20:16:34Z", False, "linear:ART-774"),
                         vrec("slack", EXPORT_SEP3, "2025-09-03T15:54:14Z", False, f"slack:{EXPORT_SEP3}"),
                         vrec("gsheets", SHEET, "2025-09-29T18:00:00Z", True, f"file:{SHEET}")]},
    {"id": "T6", "family": "exact_predicate", "services": ["gsheets", "trello", "linear"],
     "seeded_ids": [SHEET, CARD_CMT, T_STATIC, T_ENDCARD], "base_pointers": [END_CARD],
     "requirement": "R1",
     "expected_wrong_reading": "the tracker is the sheet's rows: Julia's 4:5 static and Marcus's portrait end card are left out",
     "resolver": "the ask's scope is everything players see and every ad running; Frederick's comment on the Halloween push card says Julia's 4:5 static is still running on iOS UK though it never made the sheet, and the end card's ticket says it plays after every Android US phone video, so both are rows",
     "discovery_order": "the sheet is the first and fullest list; the two extra surfaces show only in a Trello comment and in the ticket library (" + f"{N_ADS} serving tickets against {N_SHEET_ADS} ad rows)"},
    {"id": "T7", "family": "scope_alias", "services": ["gmail", "contacts", "github", "slack"],
     "seeded_ids": [QUOTE, CONTACT], "base_pointers": [PACK_REPO, PACK_MSG], "requirement": "R7",
     "expected_wrong_reading": "buy the Halloween Bits bundle the vendor quoted for the seasonal props",
     "resolver": "the sender is KayKit's founder (Contacts); the KayKit Halloween Bits pack is already in the match3d repo and is what Robert calls 'the Halloween pack', so the plan reuses it",
     "discovery_order": "the quote is in Claire's inbox; the pack's identity needs the contact record and the repo path"},
    {"id": "T8", "family": "authority", "services": ["gslides", "linear", "slack"],
     "seeded_ids": [DECK, POINTER, T_BORIS, T_ALIN, T_MUSIC], "base_pointers": [SWAP_1232, CUT_30S],
     "requirement": "R2",
     "expected_wrong_reading": "every serving cut, including the Sep 12 boris cuts and the Aug 13 30 s cut, can take a Halloween overlay as it is",
     "resolver": "Robert's deck: anything captured or rendered from a build older than Android #1452 / iOS 1232 is redone first and a master with the music baked in is re-exported first; the boris tickets show a Jul 28 capture despite the Sep 12 post and the 30 s cut's ticket says its master has the music baked in",
     "discovery_order": "the post date and the sheet's 'live since' look current; the build is only in the ticket comments and the rule only in the deck"},
    {"id": "T9", "family": "superseding", "services": ["linear"],
     "seeded_ids": [T_RECAP[0], CMT1[T_RECAP[0]], CMT2[T_RECAP[0]]] + T_RECAP[1:], "requirement": "R2",
     "expected_wrong_reading": "couch alpha 50, barrel marketing2 4:5 and balloons alpha 50 (1) were captured in April, so they are refreshed first",
     "resolver": "a later comment on each ticket records a September re-capture on a current build (Android #1935 / #1896 / #1966); the deck counts the newest capture, so each is a Halloween version",
     "version_records": [vrec("linear", CMT1[T_RECAP[0]], one(RECAP[0])["comment_1_at"], True, f"linear:{T_RECAP[0]}"),
                         vrec("linear", CMT2[T_RECAP[0]], one(RECAP[0])["comment_2_at"], True, f"linear:{T_RECAP[0]}")]},
    {"id": "T10", "family": "distractor", "distractor_type": "lookalike_entity", "services": ["gsheets"],
     "base_pointers": [DD_CAPTURE], "requirement": "R1",
     "expected_wrong_reading": "the 'Video Capture Requests for UA' sheet lists the creatives to dress",
     "resolver": "it is the 2024 Domino Delights capture list; ZM3D's serving creatives are on the live creatives sheet"},
    {"id": "T11", "family": "distractor", "distractor_type": "scope_adjacent", "services": ["slack"],
     "base_pointers": [DD_HALLOWEEN], "requirement": "R2",
     "expected_wrong_reading": "Robert's 2024 Halloween icon direction is the seasonal rule set",
     "resolver": "those 2024 asks are for Domino Delights in #god-gameart; the ZM3D rules are in his Q4 2025 deck"},
    {"id": "T12", "family": "distractor", "distractor_type": "keyword_collision", "services": ["gmail"],
     "base_pointers": [POD_0929], "requirement": "R2",
     "expected_wrong_reading": "Martin's cemetery / ice-cave theme from the Sep 29 POD notes is the Halloween look to plan",
     "resolver": "that is an in-game endless-mode theme; the Halloween push is store and ads"},
    {"id": "T13", "family": "distractor", "distractor_type": "already_done", "services": ["slack"],
     "base_pointers": [HALLOWEEN_ICON], "requirement": "R4",
     "expected_wrong_reading": "Martin's Sep 17 Halloween icon concept means the icon is done",
     "resolver": "it is an undecided concept ('for an app icon or an event', no replies); the icon is a Halloween version Martin finishes by the build cut"},
    {"id": "T14", "family": "distractor", "distractor_type": "near_duplicate_record", "services": ["gsheets", "linear"],
     "seeded_ids": [SHEET] + [a["ticket"] for a in ARCHIVED], "requirement": "R1",
     "expected_wrong_reading": "the Archive tab's paused cuts and their library tickets are serving and get rows",
     "resolver": "the Read me: paused or retired creatives move to Archive; their tickets say paused; only the Store and Unity tabs plus the two surfaces the card comment and the end card ticket add are serving"},
    {"id": "T15", "family": "distractor", "distractor_type": "stale_summary", "services": ["confluence"],
     "base_pointers": [CHECKLIST], "requirement": "R3",
     "expected_wrong_reading": "the release checklist governs when Halloween store changes can ship",
     "resolver": "the checklist is the generic pre-submission gate with no dates; the Q4 dates are in Arthur's calendar"},
    {"id": "T16", "family": "distractor", "distractor_type": "non_authoritative_instruction", "services": ["slack"],
     "seeded_ids": [ASK], "requirement": "R4",
     "expected_wrong_reading": "Leonard's 'maybe we swap the icon around the 24th' sets the icon date",
     "resolver": "a suggestion with a question mark; the build cut in Arthur's calendar decides"},
    {"id": "T17", "family": "near_miss_mention", "services": ["linear", "slack", "gslides"],
     "seeded_ids": [T_ENDCARD, CMT1[T_ENDCARD], DECK], "base_pointers": [BUILD_1450, BUILD_1452], "requirement": "R2",
     "expected_wrong_reading": "the portrait end card was rendered from the Jul 29 build with the new background, so it is current art",
     "resolver": "its ticket names Android #1450 (Jul 29 11:51Z, new background only); the deck's threshold is #1452 (the zombie swap, 20:24Z), so the end card is refreshed first"},
    {"id": "T19", "family": "exact_predicate", "services": ["slack", "gdrive", "linear"],
     "seeded_ids": [DM_REPLY, FOLDER["ua"], T_CHEER45], "requirement": "R7",
     "expected_wrong_reading": "Marcus already dressed the cheer fastcouch cut, so every cheer fastcouch export (the 4:5 too) is reused",
     "resolver": "Marcus's reply names both 9:16 and 16:9 and the UA masters folder holds those two files only; the 4:5 cut from the Sep 16 re-capture has no Halloween version, so it is a Halloween version to make",
     "discovery_order": "the DM reply is found as the completion note for 'the cheer fastcouch one'; the 4:5 is a later ticket (Sep 17) on the sheet's Unity tab"},
    {"id": "T18", "family": "exact_predicate", "services": ["gmail", "linear"],
     "seeded_ids": [MAIL_PLAN, one(TWO_TABLETS)["ticket"], one(RECAP_TAB)["ticket"]], "requirement": "R6",
     "expected_wrong_reading": "every 16:9 tablet cut is skipped because the Android US tablet campaign ends",
     "resolver": "Frederick skips only what runs nothing but the Android US tablet campaign; couch alpha 50 16:9, balloons alpha 50 (1) 16:9 and the other cuts that also run on iOS UK tablet stay in, and the rule reaches stills too (julia 1:1 android tablet)"},
]

CHAINS = [
    {"id": "CH1", "root_cause": "A24", "ends_in": "R2", "hops": [
        {"service": "slack", "record": EXPORT, "finding": "Martin: Halloween store screens exported"},
        {"service": "gsheets", "record": SHEET, "finding": "Store tab: iPhone 6.5, iPad 12.9, Play phone sets are live"},
        {"service": "gdrive", "record": FOLDER["store"], "finding": "Halloween Store folder: iPhone and Play files only"}]},
    {"id": "CH2", "root_cause": "A15", "ends_in": "R2", "hops": [
        {"service": "slack", "record": POINTER, "finding": "Robert: seasonal direction is in my deck"},
        {"service": "gslides", "record": DECK, "finding": "redo anything older than Android #1452 / iOS 1232; re-export music-baked masters"},
        {"service": "linear", "record": T_BORIS, "finding": "boris cut captured Jul 28, posted Sep 12"},
        {"service": "slack", "record": SWAP_1232, "finding": "iOS 1232 is the zombie swap with the new background (Jul 29)"}]},
    {"id": "CH3", "root_cause": "A11", "ends_in": "R5", "hops": [
        {"service": "gmail", "record": MAIL_DRAFT, "finding": "draft: flight Oct 20-31, art due Oct 17"},
        {"service": "slack", "record": ASK, "finding": "Frederick is sending his October UA plan tonight"},
        {"service": "gmail", "record": MAIL_PLAN, "finding": "changes: flight Oct 18-31, art due Oct 15, Android US tablet ends Oct 12"}]},
    {"id": "CH4", "root_cause": "A25", "ends_in": "R7", "hops": [
        {"service": "slack", "record": ASK, "finding": "what we already have"},
        {"service": "slack", "record": DM_REPLY, "finding": "Marcus: both cheer fastcouch cuts done from the no-music masters"},
        {"service": "gdrive", "record": FOLDER["ua"], "finding": "the two Halloween masters are in the Halloween folder's UA masters"}]},
    {"id": "CH5", "root_cause": "A7", "ends_in": "R7", "hops": [
        {"service": "gmail", "record": QUOTE, "finding": "quote for the Halloween Bits bundle"},
        {"service": "contacts", "record": CONTACT, "finding": "sender is KayKit's founder"},
        {"service": "github", "record": PACK_REPO, "finding": "KayKit Halloween Bits already in match3d"},
        {"service": "slack", "record": PACK_MSG, "finding": "Robert: we have the Halloween pack"}]},
    {"id": "CH6", "root_cause": "2.6.7", "ends_in": "R4", "hops": [
        {"service": "slack", "record": ASK, "finding": "maybe we swap the icon around the 24th"},
        {"service": "gdocs", "record": DOC, "finding": "anything inside the app merged by Thu Oct 16 12:00 PT"},
        {"service": "github", "record": PROJSET, "finding": "the icon is a build setting"}]},
    {"id": "CH7", "root_cause": "A17", "ends_in": "R1", "hops": [
        {"service": "gsheets", "record": SHEET, "finding": f"the sheet's serving rows ({N_SHEET_ADS} ads + 4 store surfaces)"},
        {"service": "trello", "record": CARD_CMT, "finding": "Julia's 4:5 static is still running on iOS UK"},
        {"service": "linear", "record": T_ENDCARD, "finding": "the portrait end card plays after every Android US phone video"}]},
]

PORTFOLIO = [
    {"id": "R_BUILD_CUT", "mechanism": "2.6.7", "prior_family": "2.6.7",
     "prior_family_reason": "explicit temporal rule with a dependency (the icon ships in the binary); no Opus 5.5 ledger record, so Beta(1,1); julia_zm converted a Pacific date correctly 6/6, so the date itself is easy and the dependency is the trap",
     "nodes": ["T2", "CH6", "T16", "T13"], "requirement": "R4", "natural_reading": "the icon swaps around Oct 24 as Leonard suggests",
     "decides": ["art due date", "ship route"], "source": "release-calendar", "signature": "icon-in-build-cut",
     "controls": [IPHONE, GP], "over_application": "over:every-store-piece-due-oct16"},
    {"id": "R_DONE_EXPORT", "mechanism": "A24", "prior_family": "A24",
     "prior_family_reason": "same mechanism id (a done claim plus the missing piece in another service); no Opus 5.5 record (Beta(1,1)); douglas 4/6 and arthur 3/6 on done gaps",
     "nodes": ["T1", "CH1"], "requirement": "R2", "natural_reading": "'exported' means every store set has its Halloween version",
     "decides": ["Halloween call per surface", "new store art ticket"], "source": "store-folder", "signature": "store-set-missing",
     "controls": [IPHONE, GP], "over_application": "over:every-store-set-missing"},
    {"id": "R_ALREADY_MADE", "mechanism": "A25", "prior_family": "A25",
     "prior_family_reason": "same mechanism id (completion recorded away from the request, in a DM thread reply); no Opus 5.5 record; julia_zm: DM thread replies were missed (slack_read_thread on a DM fails without the channel id)",
     "nodes": ["T3", "CH4", "T19"], "requirement": "R7", "natural_reading": "every current cut needs a Halloween version",
     "decides": ["Halloween call per surface", "Halloween work already made"], "source": "marcus-dm", "signature": "cut-already-dressed",
     "controls": [CHEER_45] + HV_SAMPLE[:1] + RECAP[:1], "over_application": "over:every-current-cut-reused"},
    {"id": "R_FLIGHT_CHANGE", "mechanism": "A11", "prior_family": "A11",
     "prior_family_reason": "v2 trap 2 (a correction in another thread changes a date and a status); no Opus 5.5 record (Beta(1,1))",
     "nodes": ["T4", "CH3", "T18"], "requirement": "R5", "natural_reading": "the Sep 12 draft: ads due Oct 17, all four campaigns",
     "decides": ["art due date", "Halloween call per surface"], "source": "fred-plan-mail", "signature": "flight-moved-up",
     "controls": [TWO_TABLETS, RECAP_TAB], "over_application": "over:every-tablet-cut-skipped"},
    {"id": "R_SCOPE_SERVING", "mechanism": "A17", "prior_family": "A17",
     "prior_family_reason": "same mechanism id (cohort boundary: serving surfaces off the obvious list, paused lookalikes on it); Opus 5.5 Beta(1,2) from one robert-vendor-schedule trial; FE-6a7e 23/30 on a later-added member",
     "nodes": ["T6", "CH7", "T5", "T10", "T14"], "requirement": "R1", "natural_reading": "the sheet's rows are the scope",
     "decides": ["one row per ZM3D marketing surface"], "source": "sheet-scope", "signature": "serving-off-sheet",
     "controls": [a["key"] for a in ARCHIVED[:2]], "over_application": "over:archive-rows-serving"},
    {"id": "R_PACK_ALIAS", "mechanism": "A7", "prior_family": "A7",
     "prior_family_reason": "scope / alias boundary surviving full retrieval; Opus 5.5 Beta(1,2) from one trial; v2 trap 6 (person-to-company link in Contacts)",
     "nodes": ["T7", "CH5"], "requirement": "R7", "natural_reading": "a quoted bundle is a new purchase",
     "decides": ["Halloween work already made"], "source": "vendor-quote", "signature": "pack-already-owned",
     "controls": [], "over_application": None},
    {"id": "R_ART_CURRENT", "mechanism": "A15", "prior_family": "A15",
     "prior_family_reason": "house rule overriding the natural reading, applied per record (V7-T1 5/6 wrong); Opus 5.5 Beta(1,2) from one trial",
     "nodes": ["T8", "CH2", "T9", "T17", "T11", "T12"], "requirement": "R2", "natural_reading": "any serving cut takes a Halloween overlay as it is",
     "decides": ["Halloween call per surface"], "source": "robert-deck", "signature": "refresh-before-seasonal",
     "controls": RECAP[:2] + HV_SAMPLE[:1], "over_application": "over:every-pre-august-post-refreshed"},
]

WRITES = [
    {"service": "gdocs", "tool": "gdocs_create_document", "count": 1, "depends_on": ["K13", "R_BUILD_CUT", "R_PACK_ALIAS", "R_FLIGHT_CHANGE"], "requirements": ["R10", "R3", "R4", "R5", "R7"]},
    {"service": "gdocs", "tool": "gdocs_batch_update", "count": 3, "depends_on": ["R_BUILD_CUT", "R_FLIGHT_CHANGE", "R_PACK_ALIAS"], "requirements": ["R3", "R4", "R5", "R7"]},
    {"service": "gsheets", "tool": "gsheets_create_spreadsheet", "count": 1, "depends_on": ["K13"], "requirements": ["R10"]},
    {"service": "gsheets", "tool": "gsheets_values_update", "count": 2, "depends_on": ["R_ART_CURRENT", "R_SCOPE_SERVING", "R_DONE_EXPORT", "R_ALREADY_MADE", "R_FLIGHT_CHANGE", "R_BUILD_CUT", "K1"], "requirements": ["R1", "R2", "R4", "R5", "R6", "R8"]},
    {"service": "linear", "tool": "linear_create_comment", "count": N_ADS, "depends_on": ["K14", "R_ART_CURRENT", "R_FLIGHT_CHANGE", "R_ALREADY_MADE"], "requirements": ["R9", "R2", "R5"]},
    {"service": "linear", "tool": "linear_update_issue", "count": N_ASSIGN, "depends_on": ["K17", "K9", "R_ALREADY_MADE", "R_FLIGHT_CHANGE"], "requirements": ["R8"]},
    {"service": "linear", "tool": "linear_create_issue", "count": 2, "depends_on": ["K14", "R_DONE_EXPORT", "R_BUILD_CUT"], "requirements": ["R9", "R4"]},
    {"service": "gdrive", "tool": "gdrive_share_file", "count": 2, "depends_on": ["K13", "K8"], "requirements": ["R10"]},
    {"service": "slack", "tool": "slack_send_message", "count": 1, "depends_on": ["K8", "K13"], "requirements": ["R10"]},
]


def B(phase, service, calls, reason, **kw):
    return dict({"phase": phase, "service": service, "calls": calls, "reason": reason}, **kw)


BUDGET = [
    # unconditional: the shortest complete route (red team rev 02: one full-grid sheet read, batched mail, the plan
    # doc created with its body); every per-ticket row is one call per ticket, no bulk endpoint
    B("discovery", "slack", 1, "read Leonard's Halloween ask in #zombie_marketing (scope, owners, follow-through, deadline)"),
    B("discovery", "slack", 1, "page #zombie-art for late September (Robert's pointer to his deck, Martin's export claim)"),
    B("discovery", "gdrive", 3, "locate the live creatives sheet, the release calendar and the seasonal deck by title (no links are posted)"),
    B("discovery", "gmail", 2, "search Claire's mailbox for Frederick's October UA plan and read the Sep 30 changes mail"),
    B("rules", "gsheets", 2, "open the sheet (tab list) and read its Read me, Store, Unity and Archive tabs in one batch (scope, ticket per ad)"),
    B("rules", "gdocs", 1, "read Arthur's Q4 release calendar (build cut, iOS screenshot rule, Play listing route)"),
    B("rules", "gslides", 1, "read Robert's seasonal art direction deck (refresh-first rule, newest capture, call words)"),
    B("rules", "trello", 2, "find the Halloween push card the Read me names and read its comments (Julia's 4:5 static)"),
    B("rules", "github", 1, "check the match3d repo for the KayKit Halloween Bits pack (what the studio already owns)"),
    B("enumeration", "linear", 2, f"list the ART library tickets ({len(LIBRARY)}, two pages) to map each sheet row to its ticket and find the serving tickets the sheet omits"),
    B("enumeration", "gdrive", 3, "list the Halloween folder and its Store and UA masters subfolders (which Halloween versions exist)"),
    B("per-record", "linear", N_ADS, "linear_list_comments per serving ad ticket: campaigns, source build, master audio and any re-capture decide every ad's call (no bulk comment endpoint)"),
    B("per-record", "slack", 1, "read Frederick's Aug 13 thread the 30 s cut's ticket points to for its master (the music is baked in; a reply-only fact)"),
    B("per-record", "linear", N_ADS, "comment each serving ad's Halloween call and due date on its ART ticket (the ask's follow-through; one comment per ticket, no bulk)"),
    B("per-record", "linear", N_ASSIGN, "assign each ad that needs new work (Halloween version or Refresh first) to its maker on its ticket; Reuse and Skip ads stay unassigned (one update per ticket)"),
    B("writes", "linear", 2, "open tickets for the new store art (the Halloween icon and the iPad set)"),
    B("writes", "gdocs", 1, "create the plan doc with its body (calls by surface type, dates, reuse, owners)"),
    B("writes", "gsheets", 2, "create the tracker and write its header and rows"),
    B("writes", "gdrive", 2, "share the plan doc and the tracker with the team (one share call per file)"),
    B("writes", "slack", 1, "post the links in Leonard's thread"),
    # conditional: exploration and confirmation most runs make, counted 0 until a run shows them
    B("discovery", "slack", 2, "read the Claire-Marcus DM and open the thread under Claire's Sep 26 note (Marcus's completion reply)", conditional_on="runs that confirm the two Halloween cuts from the DM, not only from the UA masters folder"),
    B("discovery", "gmail", 2, "read the Sep 12 draft and the vendor quote", conditional_on="runs that open the superseded draft or the quote"),
    B("discovery", "gcal", 1, "read Thursday's ZM3D Halloween review (the deadline the ask names)", conditional_on="runs that open the review event"),
    B("rules", "contacts", 1, "look up the quote's sender (vendor identity)", conditional_on="runs that identify the vendor"),
    B("rules", "github", 1, "check the icon build settings in the match3d repo", conditional_on="runs that confirm the icon ships in the build"),
    B("rules", "slack", 1, "read Robert's Jul 29 iOS 1232 zombie-swap post (the build the deck's rule names)", conditional_on="runs that date the threshold build"),
    B("rules", "confluence", 1, "read the release checklist a search for store submission rules returns (generic gate; no Q4 dates)", conditional_on="runs that search Confluence for the submission rules"),
    B("rules", "snowflake", 1, "check which networks serve ZM3D (AD_SPEND_DAILY channels since Aug)", conditional_on="runs that check the networks behind the campaigns"),
    B("per-record", "gdrive", 2, "open the two Halloween cut files' metadata (what was made, from which master)", conditional_on="runs that open the files"),
    B("per-record", "slack", 5, "read another base cut's origin thread to confirm a ticket's master note", conditional_on="runs that confirm a ticket's master note against the cut's origin thread"),
    B("writes", "linear", 1, "look up the ART team for the new tickets", conditional_on="runs that look up the team first"),
    B("read-back", "gsheets", 1, "read the tracker back", conditional_on="runs that verify the tracker"),
    B("read-back", "linear", 1, "list one ticket's comments back", conditional_on="runs that verify a comment"),
]


def build_manifest() -> dict:
    floor = sum(b["calls"] for b in BUDGET if not b.get("conditional_on"))
    total = sum(b["calls"] for b in BUDGET)
    per = int(sum(s["per_record_calls"] * s["records"] for s in COHORT_SPEC["evidence_surfaces"] if not s.get("conditional_on")))
    return {
        "assignment_context": {k: CTX[k] for k in ("context_hash", "assignment_hash", "policy_hash", "freeze_utc", "difficulty_mode")},
        "persona": "claire_morgan",
        "horizon": "Long Horizon",
        "effective_profile": "extreme",
        "volume_exception": {
            "reason": (f"Planned necessary calls are {total}; {floor} are unconditional (the shortest complete route), of which {2 * N_ADS + N_ASSIGN} are the per-ticket "
                       f"spine ({N_ADS} linear_list_comments reads, {N_ADS} follow-through comments and {N_ASSIGN} maker assignments, one "
                       "per serving ad ticket). The rest are "
                       "rule, discovery and delivery reads: Slack threads are search-sweepable, the sheet is one read per tab and the "
                       "tracker is a few value writes. Reaching 500 / 300 would need padding, a failing error."),
            "requester_confirmation": ("The requester chose D2 on 2026-11-04 in this session (question tool): a call-budget floor of "
                                       "'more then 150', recorded in Working_Files/00_Pre_Scenario_Analysis.md section 10; at "
                                       "/create-injection on 2026-11-04 the requester raised it: 'i want over 180+ tool calls in "
                                       "each runs' (D2', same section)"),
            "call_budget_floor": 181, "per_record_floor": per},
        "requirements": REQ,
        "services": SERVICES,
        "anchors": ANCHORS,
        "ask_fragments": FRAGMENTS,
        "authorities": AUTHORITIES,
        "cohort": COHORT_SPEC,
        "chains": CHAINS,
        "traps": TRAPS,
        "call_budget": BUDGET,
        "writes": WRITES,
        "mechanism_portfolio": PORTFOLIO,
        "gradable_surface": {"path": "01_Gradable_Surface.json"},
    }


# ------------------------------------------------------------------ gradable surface
def slot(sid, title, w, kind, reason, cls, role, sel, fact, mech=None, group=None, by=None, **kw):
    s = {"id": sid, "title": title, "weight": w, "work_kind": kind, "work_reason": reason, "class": cls, "role": role,
         "selector": sel, "fact_id": fact}
    if group:
        s["group"] = group
    if mech:
        s["mechanisms"] = mech
    if by:
        s["singled_out_by"] = by
    s.update(kw)
    return s


MSR = "multi_source_reconciliation"
LR = "limited_reconciliation"
# a due date from Oct 6 up to the deadline (the Oct 1 clock and the Oct 2 review are not due dates)
ORD = r"(?:st|nd|rd|th)?"
DUE_OCT15 = (r"oct(?:ober)?\.? ?(?:1[0-5]|0?[6-9])" + ORD + r"\b|10/(?:1[0-5]|0?[6-9])\b|2025-10-(?:1[0-5]|0[6-9])"
             r"|(?:1[0-5]|0?[6-9])" + ORD + r" (?:of )?oct")
DUE_OCT16 = (r"oct(?:ober)?\.? ?(?:1[0-6]|0?[6-9])" + ORD + r"\b|10/(?:1[0-6]|0?[6-9])\b|2025-10-(?:1[0-6]|0[6-9])"
             r"|(?:1[0-6]|0?[6-9])" + ORD + r" (?:of )?oct")
# the due cell must START with the date (an optional weekday first), so "not Oct 15; due Oct 17" does not pass
DUE_CELL15 = r"^ *(?:(?:mon|tue|wed|thu|fri|sat|sun)[a-z]*,? )?(?:" + DUE_OCT15 + ")"
DUE_CELL16 = r"^ *(?:(?:mon|tue|wed|thu|fri|sat|sun)[a-z]*,? )?(?:" + DUE_OCT16 + ")"
SLOTS = [
    # build cut (icon)
    # done gap (store sets)
    slot("S03", "iPad 12.9-inch store set is a Halloween version still to make", 5, MSR, "Martin's 'exported' claim, the Store tab's live sets and the Halloween Store folder listing must be reconciled", "direct", "exception", ["field", IPAD, "call"], "ipad.call", ["R_DONE_EXPORT"], by="K12"),
    slot("S26", "One new-ticket field (title or a description line) names the Halloween icon", 1, "lookup", "the icon is new store art the ask routes to a ticket", "write_content", "core", ["text", "tickets", r"icon[^\n]*halloween|halloween[^\n]*icon"], "icon.ticket"),
    slot("S04", "One new-ticket field (title or a description line) names the Halloween iPad set", 3, LR, "the iPad gap found above becomes new store art with its own ticket", "write_content", "core", ["text", "tickets", r"ipad[^\n]*halloween|halloween[^\n]*ipad"], "ipad.ticket", ["R_DONE_EXPORT"]),
    # completion elsewhere
    slot("S05", f"{REUSE_CUTS[0]} is reused", 5, MSR, "the sheet's live row and its old first capture note are joined with the September re-capture, Marcus's DM thread reply and the UA masters folder", "direct", "exception", ["field", REUSE_CUTS[0], "call"], "reuse1.call", ["R_ALREADY_MADE"], by="K16"),
    slot("S06", f"{REUSE_CUTS[1]} is reused", 5, MSR, "the same DM reply covers the tablet cut, matched to its own sheet row, ticket and file", "direct", "exception", ["field", REUSE_CUTS[1], "call"], "reuse2.call", ["R_ALREADY_MADE"], by="K16"),
    # flight change
    slot("S08", f"{SKIP_MUSIC} is skipped for October", 5, MSR, "the ticket's campaign note is joined with the mail's Android US tablet end date, which outranks the cut's baked-in music", "direct", "exception", ["field", SKIP_MUSIC, "call"], "skip.call", ["R_FLIGHT_CHANGE"], by="H4"),
    slot("S09", f"{TWO_TABLETS} is kept and refreshed first", 3, "comparison", "its ticket's campaigns (iOS UK tablet as well) are compared with the mail's 'only runs there'", "direct", "exception", ["field", TWO_TABLETS, "call"], "twotab.call", ["R_FLIGHT_CHANGE", "R_ART_CURRENT"], by="H4"),
    slot("S28", f"{CHEER_45} gets a Halloween version (not covered by Marcus's DM)", 5, MSR, "Marcus's reply names the 9:16 and the 16:9, the UA masters folder holds those two only, and the 4:5's own ticket shows a later cut from the Sep 16 re-capture", "direct", "exception", ["field", CHEER_45, "call"], "cheer45.call", ["R_ALREADY_MADE"], by="K16"),
    slot("S29", f"{SKIP_STATIC} is skipped for October", 3, "comparison", "a still's only campaign, from its ticket note, is compared with the mail's Android US tablet end date", "direct", "exception", ["field", SKIP_STATIC, "call"], "skipstatic.call", ["R_FLIGHT_CHANGE"], by="H4"),
    # scope (outside the sheet)
    slot("S10", f"{STATIC_OFF} has a row and is refreshed first", 5, MSR, "a static missing from the sheet is brought in by Frederick's card comment and judged by its ticket's Jun 5 source build under the deck's rule", "direct", "exception", ["field", STATIC_OFF, "call"], "static_off.call", ["R_SCOPE_SERVING", "R_ART_CURRENT"], by="K7"),
    slot("S11", f"{ENDCARD_OFF} has a row and is refreshed first", 5, MSR, "an end card missing from the sheet is shown serving by its own ticket, and its Android #1450 source is compared with the #1452 threshold", "direct", "exception", ["field", ENDCARD_OFF, "call"], "endcard_off.call", ["R_SCOPE_SERVING", "R_ART_CURRENT"], by="K11"),
    slot("V01", "Tracker covers exactly the serving surfaces", 3, LR, "the sheet's Store and Unity rows plus the two off-sheet surfaces, minus the Archive tab", "delivery", "volume", ["delivery", "register_keys_exact"], "tracker.keys", ["R_SCOPE_SERVING"], volume_for=["calls"]),
    # alias
    # art currency
    slot("S14", f"{OLD_BUILD[0]} is refreshed first", 5, MSR, "a Sep 12 post is overturned by its ticket's Jul 28 capture under Robert's rule (iOS 1232 / Android #1452, Jul 29)", "direct", "exception", ["field", OLD_BUILD[0], "call"], "oldbuild1.call", ["R_ART_CURRENT"], by="H3"),
    slot("S15", f"{OLD_BUILD[1]} is refreshed first", 5, MSR, "the cut's capture build from its ticket comment is compared with the deck's threshold build, against its September post", "direct", "exception", ["field", OLD_BUILD[1], "call"], "oldbuild2.call", ["R_ART_CURRENT"], by="H3"),
    slot("S16", f"{MUSIC} is refreshed first (music baked in)", 5, MSR, "the deck's master-audio rule is joined with the cut's ticket comment on a current capture", "direct", "exception", ["field", MUSIC, "call"], "music.call", ["R_ART_CURRENT"], by="H3"),
    slot("S17", f"{RECAP[0]} gets a Halloween version (re-captured)", 5, MSR, "the April capture note is superseded by the ticket's September re-capture under the deck's newest-capture rule", "direct", "exception", ["field", RECAP[0], "call"], "recap1.call", ["R_ART_CURRENT"], by="K11"),
    slot("S18", f"{RECAP[1]} gets a Halloween version (re-captured)", 3, "comparison", "the second comment's build is compared with the threshold", "direct", "exception", ["field", RECAP[1], "call"], "recap2.call", ["R_ART_CURRENT"], by="K11"),
    # follow-through
    # ordinary samples (calls group)
    slot("S21", f"{RF_SAMPLE[0]} is refreshed first", 3, "interpretation", "an April capture read against the deck's threshold", "direct", "sample", ["field", RF_SAMPLE[0], "call"], "rf1.call", group="calls"),
    slot("S22", f"{RF_SAMPLE[1]} is refreshed first", 3, "interpretation", "a June static whose source build predates the swap", "direct", "sample", ["field", RF_SAMPLE[1], "call"], "rf2.call", group="calls"),
    slot("S23", f"{HV_SAMPLE[0]} gets a Halloween version", 3, "interpretation", "a current-build export with an SFX-only master read against the deck's calls", "direct", "sample", ["field", HV_SAMPLE[0], "call"], "hv1.call", group="calls"),
    slot("S24", f"{IPHONE} is reused", 3, "interpretation", "the Halloween iPhone set is in the Store folder", "direct", "sample", ["field", IPHONE, "call"], "iphone.call", group="calls"),
    slot("S25", f"{ICON} gets a Halloween version", 3, "interpretation", "the icon concept is undecided; the icon is a new piece", "direct", "sample", ["field", ICON, "call"], "icon.call", group="calls"),
    # delivery
    slot("D01", "A reply is posted in Leonard's thread", 1, "lookup", "delivery into the named thread is a direct check", "delivery", "core", ["delivery", "slack_thread", ASK.split("/")[1]], "reply.thread"),
    slot("D02", "The tracker's own link (its file id) is in a Slack message, and the tracker is shared", 1, "lookup", "the decoded tracker's identity in the reply is a direct check", "delivery", "core", ["link", "slack"], "tracker.link"),
]


# facts the surface cannot decode deterministically (per-ticket coverage, issue-to-owner mapping, plan text written
# through either Docs path): graded by rubric rows, recorded for /create-rubric-writing (scenario_gen/rubric_only_facts.json)
RUBRIC_ONLY = [
    {"id": "RO1", "fact": f"Every one of the {N_ADS} serving ad tickets gets its own comment with that ad's call (Skip and Reuse included)", "work_kind": LR, "weight": 3, "mechanisms": [], "why_not_surface": "no selector counts comments per issue"},
    {"id": "RO2", "fact": "Each comment on an ad that needs work or is reused carries the Wed Oct 15 hand-off date", "work_kind": LR, "weight": 3, "mechanisms": ["R_FLIGHT_CHANGE"], "why_not_surface": "comment text is concatenated across issues"},
    {"id": "RO3", "fact": f"Exactly the {N_ASSIGN} ads that need new work are assigned to their maker ({sum(1 for r in ADS if r.get('assign_to') == 'Marcus Bennett')} to Marcus, {sum(1 for r in ADS if r.get('assign_to') == 'Martin Walsh')} to Martin); the {sum(1 for r in ADS if r['call'] == 'Reuse')} Reuse and {sum(1 for r in ADS if r['call'] == 'Skip October')} Skip ads stay unassigned", "work_kind": MSR, "weight": 5, "mechanisms": ["R_ALREADY_MADE", "R_FLIGHT_CHANGE"], "why_not_surface": "assignee identity per issue is not decoded"},
    {"id": "RO4", "fact": "The plan reuses the KayKit Halloween Bits pack the studio already owns for the seasonal props", "work_kind": MSR, "weight": 5, "mechanisms": ["R_PACK_ALIAS"], "why_not_surface": "plan text can arrive through gdocs_create_document bodyText or gdocs_batch_update; one deliverable reads one tool"},
    {"id": "RO5", "fact": "The plan does not buy the quoted Halloween Bits bundle", "work_kind": "comparison", "weight": 3, "mechanisms": ["R_PACK_ALIAS"], "why_not_surface": "as RO4"},
    {"id": "RO7", "fact": "The plan doc and the tracker are shared with the review attendees so they can comment, and both links are in Leonard's thread", "work_kind": "lookup", "weight": 1, "mechanisms": [], "why_not_surface": "share_reader binds to the tracker and the reader role; the plan link is not a decoded identity"},
    {"id": "RO8", "fact": "The new Halloween icon ticket is due by the Thu Oct 16 12:00 PT merge cut; the iPad set ticket by the same cut", "work_kind": LR, "weight": 3, "mechanisms": ["R_BUILD_CUT"], "why_not_surface": "ticket text is concatenated across new tickets and a time of day is not decoded"},
    {"id": "RO9", "fact": "In the tracker, the app icon and the iPad and iPhone store sets are due by the Thu Oct 16 12:00 PT merge cut (an earlier internal date is fair); the Google Play set has no fixed date", "work_kind": MSR, "weight": 5, "mechanisms": ["R_BUILD_CUT"], "why_not_surface": "a due window (any date up to the cut) needs a date comparison the field comparators do not have; reason_matches has no solver value"},
    {"id": "RO10", "fact": f"In the tracker, every ad that needs new work or is reused is due with Frederick by Wed Oct 15 (not Fri Oct 17); Skip ads have no due date", "work_kind": MSR, "weight": 5, "mechanisms": ["R_FLIGHT_CHANGE"], "why_not_surface": "as RO9"},
    {"id": "RO6", "fact": "The plan says the Halloween icon ships in the Oct 17 store build (merged by the Oct 16 12:00 PT cut), not as a standalone swap around Oct 24", "work_kind": "interpretation", "weight": 3, "mechanisms": ["R_BUILD_CUT"], "why_not_surface": "as RO4"},
]


def build_surface() -> dict:
    return {
        "kind": "GRADABLE_SURFACE", "version": 1, "task": "claire-zm3d-halloween-art-plan", "revision": "scenario-01",
        "classes": CALLS,
        "truth_fields": {"class": "call", "groups": "groups"},
        "truth_keys": KEYS,
        "deliverables": {
            "tracker": {"kind": "table", "name_regex": "(?:halloween)", "key_column": "surface",
                        "key_regex": "[A-Za-z0-9][A-Za-z0-9 _:.,'\"()/&+-]{1,60}",
                        "columns": ["surface", "call", "owner", "due", "notes"],
                        "class_column": "call", "reason_column": "due",
                        "comparators": {"call": "norm"}, "missing_values": ["", "-", "n/a"]},
            "comments": {"kind": "json_text", "tool": "linear_create_comment"},
            "tickets": {"kind": "json_text", "tool": "linear_create_issue"},
            "slack": {"kind": "json_text", "tool": "slack_send_message"},
        },
        "slots": SLOTS,
    }


def main() -> None:
    m = build_manifest()
    (WF / "01_Hardness_Manifest.draft.json").write_text(json.dumps(m, indent=1, ensure_ascii=False) + "\n")
    (WF / "01_Gradable_Surface.json").write_text(json.dumps(build_surface(), indent=1, ensure_ascii=False) + "\n")
    truth = [{"surface": r["key"], "call": r["call_word"], "owner": r.get("owner"), "due": r.get("due"), "route": r.get("route"),
              "ticket": r.get("ticket"), "kind": r["kind"], "on_sheet": r["on_sheet"], "campaigns": r["campaigns"],
              "source_build": r.get("source_build"), "current_build": r.get("current_build"),
              "audio_master": r.get("audio_master"), "groups": ["calls"]} for r in ROSTER]
    (HERE / "truth.json").write_text(json.dumps(truth, indent=1, ensure_ascii=False) + "\n")
    (HERE / "rubric_only_facts.json").write_text(json.dumps(RUBRIC_ONLY, indent=1, ensure_ascii=False) + "\n")
    floor = sum(b["calls"] for b in BUDGET if not b.get("conditional_on"))
    share = Counter()
    for s in SLOTS:
        for mch in s.get("mechanisms", []):
            share[mch] += s["weight"]
    tw = sum(s["weight"] for s in SLOTS)
    mech_w = sum(s["weight"] for s in SLOTS if s.get("mechanisms"))
    print(f"manifest + surface written; cohort {COHORT} {dict(Counter(r['call_word'] for r in ROSTER))}; ads {N_ADS}; "
          f"budget unconditional {floor} / total {sum(b['calls'] for b in BUDGET)}; slots {len(SLOTS)} weight {tw}; "
          f"mechanism weight {mech_w} ({mech_w / tw:.0%}); weight-5 {sum(1 for s in SLOTS if s['weight'] == 5)}; by rule {dict(share)}")


if __name__ == "__main__":
    main()
