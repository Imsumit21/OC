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
STORE_REPLY = slack_loc(IDS["slack_leonard_store_reply"])   # Leonard's thread reply: exported art needs no ticket (Sep 30)
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
# revision rev3 carriers: deciding facts moved off the swept path (hardening report section 10)
FRED_REVIEW = slack_loc(IDS["slack_fred_review_reply"])    # Frederick's reply in the fake-installs thread: Android US phone by Fri Oct 10
INSTALLS_ROOT = "C0880U9751A/1759211437.306779"           # base: Robert, Sep 30, Unity fake installs (Frederick already in the thread)
RECAP_NOTE = slack_loc(IDS["slack_marcus_recapture"])      # Marcus, #zm-animations: three re-captures
TEST_POST = slack_loc(IDS["slack_marcus_test"])            # Marcus, #zombie-art: quick test on cheer fastcouch
TEST_REVIEW = slack_loc(IDS["slack_robert_test_reply"])    # Robert's review: July capture, cannot ship
TEST_ACK = slack_loc(IDS["slack_marcus_test_reply"])       # Marcus: will redo both
LEAVE_POST = slack_loc(IDS["slack_martin_leave"])          # Martin, #company-internal: vacation, Julia takes the ad statics
LEAVE_REPLY = slack_loc(IDS["slack_leonard_leave_reply"])  # Leonard: works for me
MAIL_RESTART = IDS["gmail_fred_restart"]["msg"]            # Frederick, Sep 29: two cuts left off iOS UK tablet
MAIL_RESTART_T = IDS["gmail_fred_restart"]["thread"]
LOGO_CMT = IDS["trello_logo_comment"]                      # Frederick's comment: old zombies on the packs in end card 001 and its cuts
PACKS_OLD = "C08R8CHB0QL/1754310794.907609"                # base: Marcus posts EndCard001.mp4, the packs "have the old zombies on it"
PACKS_NEW = "C08R8CHB0QL/1754316299.381419"                # base: Martin's new packs, about 90 minutes later
LOGO_CARD = "68768a1501ae552dbee94b8a"                     # base: Marketing Video Refresh card, ZM ROADMAP
FOLDER = IDS["folder_halloween"]
STORE_FILES = IDS["files_store"]
UA_FILES = IDS["files_ua"]

# base records (read through tools/hg.py; ids verified in the pre-scenario analysis and the Phase-1 census)
HALLOWEEN_ICON = "C08R8CHB0QL/1758121809.236839"     # Martin, Sep 17: Halloween icon concept (base; revision 03 adds Robert's reply)
ICON_REPLY = slack_loc(IDS["slack_robert_icon_reply"])  # Robert's thread reply: not for the app icon, too busy at icon size
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
HV_SAMPLE = ["marcus.bennett 4:5", "marcus.bennett 1:1"]
LOGO_KEYS = ["end card 001", "end card 16:9 from 001", "end card 1:1 from 001", "end card 4:5 from 001"]
TRIM_KEYS = ["squirrelfail landscape", "mrfluffernot landscape"]
STATIC_KEYS = ["julia 1:1", "julia 9:16"]
ANDROID_DUE = ["couch boss 30", "marcus.bennett 1:1"]       # on Android US phone: Fri Oct 10
IOS_DUE = "marcus.bennett 4:5"                              # iOS UK only: stays Wed Oct 15
RF_SAMPLE = ["couch boss 30", "julia 1:1"]
DUE_AD = "marcus.bennett 1:1"
for k in [ICON, IPAD, IPHONE, GP, MUSIC, SKIP_MUSIC, TWO_TABLETS, STATIC_OFF, ENDCARD_OFF, DUE_AD, CHEER_45, SKIP_STATIC,
          RECAP_TAB] + REUSE_CUTS + OLD_BUILD + RECAP + HV_SAMPLE + RF_SAMPLE:
    one(k)
assert [one(k)["call"] for k in REUSE_CUTS] == ["Halloween version", "Halloween version"]
assert all(one(k)["call"] == "Refresh first" for k in LOGO_KEYS) and all(one(k)["call"] == "Skip October" for k in TRIM_KEYS)
assert all(one(k)["owner"] == "Julia Lawson" for k in STATIC_KEYS)
assert all(one(k)["due"] == "2025-10-10" for k in ANDROID_DUE) and one(IOS_DUE)["due"] == "2025-10-15"
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
    "R2": "Halloween call per surface (Halloween version / Refresh first / Reuse / Skip): an ad captured or rendered from a build older than the zombie swap build (Android #1452 / iOS 1232), or with the music baked into its master, is refreshed first unless a later re-capture replaced it, wherever that re-capture is recorded; a render flagged for re-render is refreshed first too",
    "R3": "Ship route for the store and icon pieces: what ships inside the app goes in the Oct 17 store build; iOS screenshots go up with that submission; Google Play listing graphics upload any day",
    "R4": "Art due date for the store and icon pieces, set by the build cut (Thu Oct 16 12:00 PT for anything inside the app and for new iOS screenshots)",
    "R5": "Art due date for the ad pieces, set by the UA flight and Unity's review: anything going on Android US phone is with Frederick by Fri Oct 10, every other working ad by Wed Oct 15",
    "R6": "Halloween call Skip only for creatives that run on nothing but the Android US tablet campaign, which ends before the flight, on the campaigns they run on today",
    "R7": "Reuse: Halloween work already made and able to ship is reused; a test the art director turned down is not",
    "R8": "Owner per new piece: Martin Walsh for the icon and store art, Julia Lawson for the ad statics (she covers them while Martin is out), Marcus Bennett for video and end cards; each ad that needs new work is assigned to its maker on its ART ticket, Reuse and Skip ads are not",
    "R9": "Follow-through: each ad's Halloween call and due date go on its ART ticket as a comment (Leonard asks for a comment), and new store art gets its own ticket",
    "R10": "Delivery: a plan doc and a tracker Claire owns, shared with the team, and the links posted in Leonard's thread before Thursday's review",
}

SERVICES = {
    "slack": {"role": "the ask and reply thread, Robert's pointer to his deck, Martin's export claim, Marcus's completion note, base art-refresh posts",
              "weight_reason": "Leonard's ask is the anchor, scope, follow-through and reply destination (R1, R9, R10); Marcus's DM reply is the convincing done claim for the cheer fastcouch test and Robert's #zombie-art review overturns it (R7); Martin's post is the convincing done claim for the store (R2); Frederick's fake-installs thread reply sets the Android due date (R5); Marcus's #zm-animations note carries three re-captures (R2); Martin's #company-internal post moves the ad statics to Julia (R8); base #zombie-match3d and #builds posts date the zombie swap build (R2)"},
    "gsheets": {"role": "H1: the live creatives sheet (cohort definition)",
                "weight_reason": "Frederick's 'ZM3D live creatives' defines what is serving (R1) and links every ad to its ART ticket, whose comments carry its campaigns; its Store tab fixes the live store sets (R2)"},
    "gdocs": {"role": "H2: Arthur's Q4 release calendar",
              "weight_reason": "the only record of the Halloween build cut, the iOS screenshot rule and the Play listing route (R3, R4)"},
    "gslides": {"role": "H3: Robert's seasonal art direction deck",
                "weight_reason": "sets the refresh-first rule by source build and master audio, the newest-capture rule and the call words (R2)"},
    "gmail": {"role": "H4: Frederick's October UA plan and its superseded draft; the vendor quote",
              "weight_reason": "the Sep 30 mail moves the ad due date to Oct 15 and ends the Android US tablet campaign (R5, R6); Frederick's Sep 29 restart mail takes two cuts off iOS UK tablet (R6); the vendor quote is a plain distractor"},
    "linear": {"role": "the per-creative ART library tickets: campaigns, source build and master audio in comments; follow-through destination",
               "weight_reason": "each ad's catalogue campaigns, source build and master audio are in its ticket comments (R2, R6); the calls go back on the tickets as comments and new store art gets tickets (R9); the off-sheet end card is serving per its ticket (R1)"},
    "gdrive": {"role": "the Halloween delivery folders and ownership of the write targets",
               "weight_reason": "the Store folder shows which Halloween store sets exist (R2: the iPad set is missing); the UA masters folder holds Marcus's two test cuts, the convincing done source (R7); Claire's created doc and sheet are hers to share (R10)"},
    "github": {"role": "what ships in the build",
               "weight_reason": "the icon settings in the match3d repo ship in the build (R3)"},
    "trello": {"role": "the Halloween push card and Frederick's scope comment; the Marketing Video Refresh card",
               "weight_reason": "Frederick's comment on the card the sheet's Read me names is the only record that Julia's 4:5 static is still running although it is not on the sheet (R1); his comment on the Marketing Video Refresh card flags the old zombies on the packs in end card 001 and its cuts (R2)"},
    "contacts": {"role": "vendor identity",
                 "weight_reason": "the quote's sender resolves to KayKit's founder (context for a plain distractor, no graded row)"},
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
    frag("K18", "slack", f"slack:{STORE_REPLY}", "exclusion", ["A1"], seeded=[STORE_REPLY], by=ASK,
         quote=q("slack_ask", "open tickets for any new store art"), reqs=["R9"]),
    frag("K16", "slack", f"slack:{DM_ROOT}", "requirement", ["A1"], seeded=[DM_ROOT, DM_REPLY], by=ASK,
         quote=q("slack_ask", "Marcus has video and end cards"), reqs=["R7"]),
    frag("K19", "slack", f"slack:{INSTALLS_ROOT}", "amendment", ["A1"], seeded=[FRED_REVIEW], base=[INSTALLS_ROOT], by=ASK,
         quote=q("slack_ask", "who makes what by when"), reqs=["R5"]),
    frag("K20", "slack", f"slack:{RECAP_NOTE}", "requirement", ["A1"], seeded=[RECAP_NOTE], by=ASK,
         quote=q("slack_ask", "what needs work first"), reqs=["R2"]),
    frag("K21", "slack", f"slack:{TEST_POST}", "exclusion", ["A1"], seeded=[TEST_POST, TEST_REVIEW, TEST_ACK], by=ASK,
         quote=q("slack_ask", "what we already have"), reqs=["R7"]),
    frag("K22", "slack", f"slack:{LEAVE_POST}", "recipient", ["A1"], seeded=[LEAVE_POST, LEAVE_REPLY], by=ASK,
         quote=q("slack_ask", "whoever's making them"), reqs=["R8"]),
    frag("K23", "gmail", f"gmail:{MAIL_RESTART_T}", "amendment", ["A1"], seeded=[MAIL_RESTART], by=ASK,
         quote=q("slack_ask", "every ad we're running"), reqs=["R6"]),
    frag("K24", "trello", f"trello:{LOGO_CARD}", "requirement", ["A1"], seeded=[LOGO_CMT], base=[LOGO_CARD], by=ASK,
         quote=q("slack_ask", "go through everything that's live today"), reqs=["R2"]),
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
         "why_no_bulk": "linear_list_issues and linear_get_issue return titles, states and descriptions but never comments; each ad's catalogue campaigns, source build and master audio are only in its own ticket comments (no bulk comment endpoint)",
         "short_circuit": "the sheet and the ticket descriptions carry no campaign, source build or master (no-leak), so even a Skip (tablet-only) or Reuse call needs the ticket's campaign note; the post date and the sheet's 'live since' mislead both ways (Sep 12 boris cuts captured Jul 28, April cuts re-captured in September), so no run can settle an ad's call without its comments",
         "requirement": "R2", "decides": "Halloween call per surface"},
        {"service": "gdrive", "tool": "gdrive_list_folder", "per_record_calls": 1.0, "records": 3,
         "seeded": True, "seeded_ids": [FOLDER["root"], FOLDER["store"], FOLDER["ua"]],
         "why_no_bulk": "gdrive_search by name returns files without their folder context; which Halloween sets and cuts exist is read per delivery folder (root, Store, UA masters)",
         "short_circuit": "Martin's 'exported' post and Marcus's DM note say what was made; only the folders show the iPad set is absent and that the two test cuts exist",
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
    {"id": "T3", "family": "done_gap", "services": ["slack", "gdrive", "linear"],
     "seeded_ids": [DM_ROOT, DM_REPLY, FOLDER["ua"], T_CHEER, TEST_POST, TEST_REVIEW, TEST_ACK] + UA_FILES, "requirement": "R7",
     "expected_wrong_reading": "Marcus's DM reply and the two files in UA masters mean both cheer fastcouch cuts have Halloween versions, so they are reused",
     "resolver": "Robert's review in the #zombie-art thread under Marcus's test post: the test sits on the July capture with the old background and cannot ship, and Marcus will redo both from the Sep 16 capture; each cut is a Halloween version to make and is assigned to Marcus",
     "discovery_order": "the done claim holds the task's own keyword and the two files carry it in their names; the review is in another channel and never says halloween",
     "version_records": [vrec("slack", DM_REPLY, "2025-09-29T17:20:37Z", True, f"slack:{DM_ROOT}"),
                         vrec("slack", TEST_REVIEW, "2025-09-30T16:05:37Z", True, f"slack:{TEST_POST}")]},
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
                         vrec("gsheets", SHEET, "2025-09-30T22:30:00Z", True, f"file:{SHEET}")]},
    {"id": "T6", "family": "exact_predicate", "services": ["gsheets", "trello", "linear"],
     "seeded_ids": [SHEET, CARD_CMT, T_STATIC, T_ENDCARD, CMT2[T_ENDCARD]], "base_pointers": [END_CARD],
     "requirement": "R1",
     "expected_wrong_reading": "the tracker is the sheet's rows: Julia's 4:5 static and Marcus's portrait end card are left out",
     "resolver": "the ask's scope is everything players see and every ad running; Frederick's comment on the Halloween push card says Julia's 4:5 static is still running on iOS UK though it never made the sheet, and the end card's ticket says it plays after every Android US phone video, with Frederick's Sep 29 note on it (still running, not on the sheet yet), so both are rows",
     "discovery_order": "the sheet is the first and fullest list; the two extra surfaces show only in a Trello comment and in the ticket library (" + f"{N_ADS} serving tickets against {N_SHEET_ADS} ad rows)"},
    {"id": "T7", "family": "distractor", "distractor_type": "scope_adjacent", "services": ["gmail", "contacts"],
     "seeded_ids": [QUOTE, CONTACT], "requirement": "R2",
     "expected_wrong_reading": "buy the Halloween Bits bundle the vendor quoted for the seasonal props",
     "resolver": "a sales pitch, not a marketing surface; the plan needs no purchase, and no graded row depends on it (purged as a rule at rev3, kept as a plain distractor)"},
    {"id": "T8", "family": "authority", "services": ["gslides", "linear", "slack"],
     "seeded_ids": [DECK, POINTER, T_BORIS, T_ALIN, T_MUSIC], "base_pointers": [SWAP_1232, CUT_30S],
     "requirement": "R2",
     "expected_wrong_reading": "every serving cut, including the Sep 12 boris cuts and the Aug 13 30 s cut, can take a Halloween overlay as it is",
     "resolver": "Robert's deck: anything captured or rendered from a build older than Android #1452 / iOS 1232 is redone first and a cut whose master has the music baked in is re-cut first from a master without music; the boris tickets show a Jul 28 capture despite the Sep 12 post, and the 30 s cut's ticket points to Frederick's Aug 13 thread, where its music is baked in (Marcus's no-music export in the same thread is the source to re-cut from, not a Halloween-ready cut)",
     "discovery_order": "the post date and the sheet's 'live since' look current; the build is only in the ticket comments and the rule only in the deck"},
    {"id": "T9", "family": "completion_elsewhere", "services": ["linear", "slack"],
     "seeded_ids": [T_RECAP[0], CMT1[T_RECAP[0]], RECAP_NOTE] + T_RECAP[1:], "requirement": "R2",
     "expected_wrong_reading": "couch alpha 50, barrel marketing2 4:5 and balloons alpha 50 (1) were captured in April, so they are refreshed first",
     "resolver": "Marcus's note in #zm-animations records a September re-capture of each on a current build (Android #1935 / #1896 / #1966); the deck counts the newest capture, so each is a Halloween version",
     "discovery_order": "the ticket comment is the source the sheet's Read me names and shows April; the note is in the animation channel and names each cut",
     "version_records": [vrec("linear", CMT1[T_RECAP[0]], one(RECAP[0])["comment_1_at"], True, f"linear:{T_RECAP[0]}"),
                         vrec("slack", RECAP_NOTE, "2025-09-25T18:12:44Z", True, f"slack:{RECAP_NOTE}")]},
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
     "seeded_ids": [ICON_REPLY], "base_pointers": [HALLOWEEN_ICON], "requirement": "R4",
     "expected_wrong_reading": "Martin's Sep 17 Halloween icon concept means the icon is done (Reuse)",
     "resolver": "Robert's reply in that thread turns the concept down for the app icon ('too busy at that size', keep it for an event); the icon is a Halloween version Martin dresses from the current icon by the build cut"},
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
     "resolver": "Marcus's reply names both 9:16 and 16:9 and the UA masters folder holds those two files only; the 4:5 cut from the Sep 16 re-capture was never in the test, so it is a Halloween version to make",
     "discovery_order": "the DM reply is found as the completion note for 'the cheer fastcouch one'; the 4:5 is a later ticket (Sep 17) on the sheet's Unity tab"},
    {"id": "T18", "family": "exact_predicate", "services": ["gmail", "linear"],
     "seeded_ids": [MAIL_PLAN, one(TWO_TABLETS)["ticket"], one(RECAP_TAB)["ticket"]], "requirement": "R6",
     "expected_wrong_reading": "every 16:9 tablet cut is skipped because the Android US tablet campaign ends",
     "resolver": "Frederick skips only what runs nothing but the Android US tablet campaign; couch alpha 50 16:9, balloons alpha 50 (1) 16:9 and the other cuts that also run on iOS UK tablet stay in, and the rule reaches stills too (julia 1:1 android tablet)"},
    {"id": "T20", "family": "effective_date", "services": ["gmail", "slack", "linear"],
     "seeded_ids": [MAIL_PLAN, FRED_REVIEW], "base_pointers": [INSTALLS_ROOT], "requirement": "R5",
     "expected_wrong_reading": "every working ad is due with Frederick on Wed Oct 15, as his Sep 30 mail says",
     "resolver": "Frederick's later reply in the fake-installs thread: Unity manually reviews every new Android creative, so anything going on Android US phone is due Fri Oct 10; iOS UK stays on the 15th",
     "discovery_order": "the mail is the source the ask names and says every ad; the reply is in a #zombie-match3d thread about fake installs",
     "version_records": [vrec("gmail", MAIL_PLAN, "2025-09-30T23:10:00Z", True, f"gmail:{MAIL_PLAN_T}"),
                         vrec("slack", FRED_REVIEW, "2025-09-30T23:42:18Z", True, f"slack:{INSTALLS_ROOT}")]},
    {"id": "T21", "family": "superseding", "services": ["slack", "linear"],
     "seeded_ids": [ASK, LEAVE_POST, LEAVE_REPLY], "requirement": "R8",
     "expected_wrong_reading": "Martin makes the stills, as Leonard's split says, so the julia statics go to Martin",
     "resolver": "Martin's later #company-internal post: he is out Oct 6-15 and Julia takes the ad statics, store art stays with him; Leonard's reply agrees",
     "discovery_order": "the split is in the ask everyone reads first; the change is a vacation post in the leave channel",
     "version_records": [vrec("slack", ASK, "2025-09-30T22:05:13Z", True, f"slack:{ASK}"),
                         vrec("slack", LEAVE_REPLY, "2025-09-30T23:31:47Z", True, f"slack:{LEAVE_POST}")]},
    {"id": "T22", "family": "cross_reference_gap", "services": ["linear", "gmail"],
     "seeded_ids": [one(TRIM_KEYS[0])["ticket"], one(TRIM_KEYS[1])["ticket"], MAIL_RESTART, MAIL_PLAN], "requirement": "R6",
     "expected_wrong_reading": "squirrelfail landscape and mrfluffernot landscape still run on iOS UK tablet, so they are kept and refreshed first",
     "resolver": "Frederick's Sep 29 restart mail left both off iOS UK tablet, so only Android US tablet remains and his Sep 30 rule skips them",
     "discovery_order": "the ticket notes name both tablets (checked Sep 9); the restart mail shares no words with the October plan",
     "version_records": [vrec("linear", CMT1[one(TRIM_KEYS[0])["ticket"]], one(TRIM_KEYS[0])["comment_1_at"], True, f"linear:{one(TRIM_KEYS[0])['ticket']}"),
                         vrec("gmail", MAIL_RESTART, "2025-09-29T23:48:00Z", True, f"gmail:{MAIL_RESTART_T}")]},
    {"id": "T23", "family": "authority", "services": ["linear", "trello", "gslides"],
     "seeded_ids": [one(LOGO_KEYS[0])["ticket"], LOGO_CMT, DECK], "base_pointers": [LOGO_CARD, PACKS_OLD, PACKS_NEW], "requirement": "R2",
     "expected_wrong_reading": "end card 001 and its cuts were rendered from Android #1529, after the swap, so each takes a Halloween version as it is",
     "resolver": "Frederick's comment on the Marketing Video Refresh card: end card 001 and its 16:9, 1:1 and 4:5 cuts still show the old zombies on the packs, which the base thread confirms (Marcus's Aug 4 post of EndCard001.mp4, Martin's new packs after it), so they need a re-render first; the deck's Refresh first covers a re-render",
     "discovery_order": "the build on each ticket passes the deck's rule; the flag is on a different Trello card and never says halloween"},
]

CHAINS = [
    {"id": "CH1", "root_cause": "A24", "ends_in": "R2", "hops": [
        {"service": "slack", "record": EXPORT, "finding": "Martin: Halloween store screens exported"},
        {"service": "gsheets", "record": SHEET, "finding": "Store tab: iPhone 6.5, iPad 12.9, Play phone sets are live"},
        {"service": "gdrive", "record": FOLDER["store"], "finding": "Halloween Store folder: iPhone and Play files only"}]},
    {"id": "CH2", "root_cause": "A15", "ends_in": "R2", "hops": [
        {"service": "slack", "record": POINTER, "finding": "Robert: seasonal direction is in my deck"},
        {"service": "gslides", "record": DECK, "finding": "redo anything older than Android #1452 / iOS 1232; re-cut music-baked masters from a no-music master"},
        {"service": "linear", "record": T_BORIS, "finding": "boris cut captured Jul 28, posted Sep 12"},
        {"service": "slack", "record": SWAP_1232, "finding": "iOS 1232 is the zombie swap with the new background (Jul 29)"}]},
    {"id": "CH3", "root_cause": "A11", "ends_in": "R5", "hops": [
        {"service": "gmail", "record": MAIL_DRAFT, "finding": "draft: flight Oct 20-31, art due Oct 17"},
        {"service": "slack", "record": ASK, "finding": "Frederick is sending his October UA plan tonight"},
        {"service": "gmail", "record": MAIL_PLAN, "finding": "changes: flight Oct 18-31, art due Oct 15, Android US tablet ends Oct 12"}]},
    {"id": "CH4", "root_cause": "A24", "ends_in": "R7", "hops": [
        {"service": "slack", "record": DM_REPLY, "finding": "Marcus: both cheer fastcouch cuts done"},
        {"service": "gdrive", "record": FOLDER["ua"], "finding": "two Halloween files in UA masters"},
        {"service": "slack", "record": TEST_REVIEW, "finding": "Robert: July capture, old background, cannot ship"}]},
    {"id": "CH6", "root_cause": "2.6.7", "ends_in": "R4", "hops": [
        {"service": "slack", "record": ASK, "finding": "maybe we swap the icon around the 24th"},
        {"service": "gdocs", "record": DOC, "finding": "anything inside the app merged by Thu Oct 16 12:00 PT"},
        {"service": "github", "record": PROJSET, "finding": "the icon is a build setting"}]},
    {"id": "CH7", "root_cause": "A17", "ends_in": "R1", "hops": [
        {"service": "gsheets", "record": SHEET, "finding": f"the sheet's serving rows ({N_SHEET_ADS} ads + 4 store surfaces)"},
        {"service": "trello", "record": CARD_CMT, "finding": "Julia's 4:5 static is still running on iOS UK"},
        {"service": "linear", "record": T_ENDCARD, "finding": "the portrait end card plays after every Android US phone video"}]},
    {"id": "CH8", "root_cause": "A14", "ends_in": "R5", "hops": [
        {"service": "gmail", "record": MAIL_PLAN, "finding": "every Halloween ad with Frederick by Wed Oct 15"},
        {"service": "slack", "record": FRED_REVIEW, "finding": "new Android creatives reviewed by hand: Android US phone by Fri Oct 10"},
        {"service": "linear", "record": T_RECAP[0], "finding": "the ticket's campaign note says which ads run on Android US phone"}]},
    {"id": "CH9", "root_cause": "A25", "ends_in": "R2", "hops": [
        {"service": "linear", "record": T_RECAP[0], "finding": "April capture on the ticket"},
        {"service": "gslides", "record": DECK, "finding": "the newest capture is the one that counts"},
        {"service": "slack", "record": RECAP_NOTE, "finding": "Marcus re-recorded it on Android #1935"}]},
    {"id": "CH10", "root_cause": "A18", "ends_in": "R8", "hops": [
        {"service": "slack", "record": ASK, "finding": "Martin has the icon and the stills"},
        {"service": "slack", "record": LEAVE_POST, "finding": "Martin out Oct 6-15, Julia takes the ad statics"},
        {"service": "slack", "record": LEAVE_REPLY, "finding": "Leonard: works for me"},
        {"service": "linear", "record": one(STATIC_KEYS[0])["ticket"], "finding": "the static's ticket is assigned to Julia"}]},
    {"id": "CH11", "root_cause": "A13", "ends_in": "R6", "hops": [
        {"service": "linear", "record": one(TRIM_KEYS[0])["ticket"], "finding": "ticket note: iOS UK tablet and Android US tablet"},
        {"service": "gmail", "record": MAIL_RESTART, "finding": "left off iOS UK tablet at the Sep 29 restart"},
        {"service": "gmail", "record": MAIL_PLAN, "finding": "skip anything that only runs on Android US tablet"}]},
    {"id": "CH12", "root_cause": "A12", "ends_in": "R2", "hops": [
        {"service": "linear", "record": one(LOGO_KEYS[0])["ticket"], "finding": "rendered from Android #1529, after the swap"},
        {"service": "trello", "record": LOGO_CMT, "finding": "end card 001 and its cuts still show the old zombies on the packs"},
        {"service": "gslides", "record": DECK, "finding": "Refresh first: re-capture, re-render or re-cut"}]},
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
    {"id": "R_TEST_TURNED_DOWN", "mechanism": "A24", "prior_family": "A24",
     "prior_family_reason": "v2 trap 1 (a done source plus a missing piece in another service); rebuilt from R_ALREADY_MADE, which leaked on one keyword search (hev_5607371363107ea5); Opus 5.5 prior Beta(1,1) plus that task's one R_DONE_EXPORT non-landing",
     "nodes": ["T3", "CH4", "T19"], "requirement": "R7", "natural_reading": "Marcus's DM and the two files mean the cheer fastcouch cuts are done, so they are reused",
     "decides": ["Halloween call per surface"], "source": "robert-test-review", "signature": "test-turned-down",
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
    {"id": "R_ART_CURRENT", "mechanism": "A15", "prior_family": "A15",
     "prior_family_reason": "house rule overriding the natural reading, applied per record (V7-T1 5/6 wrong); Opus 5.5 Beta(1,2) from one trial",
     "nodes": ["T8", "CH2", "T17", "T11", "T12"], "requirement": "R2", "natural_reading": "any serving cut takes a Halloween overlay as it is",
     "decides": ["Halloween call per surface"], "source": "robert-deck", "signature": "refresh-before-seasonal",
     "controls": RECAP[:2] + HV_SAMPLE[:1], "over_application": "over:every-pre-august-post-refreshed"},
    {"id": "R_REVIEW_WINDOW", "mechanism": "A14", "prior_family": "A14",
     "prior_family_reason": "v2 traps 2 and 4: a dated correction by the same person in a thread reply elsewhere; frederick_bridge: 'a later post in another channel' discriminated; no Opus 5.5 ledger record (Beta(1,1))",
     "nodes": ["T20", "CH8"], "requirement": "R5", "natural_reading": "every working ad is due with Frederick on Wed Oct 15",
     "decides": ["art due date"], "source": "fred-review-reply", "signature": "android-due-earlier",
     "controls": [IOS_DUE, CHEER_45], "over_application": "over:every-ad-due-oct10"},
    {"id": "R_RECAPTURE_NOTE", "mechanism": "A25", "prior_family": "A25",
     "prior_family_reason": "v2 trap 9 (completion note away from the request); replaces T9's same-ticket re-capture, which leaked (hev_cdb4202aec019c58); no Opus 5.5 ledger record (Beta(1,1))",
     "nodes": ["T9", "CH9"], "requirement": "R2", "natural_reading": "the ticket's April capture is the newest, so the cut is refreshed first",
     "decides": ["Halloween call per surface"], "source": "marcus-recapture-note", "signature": "recapture-off-ticket",
     "controls": ["couch alpha 30", "couch boss 30"], "over_application": "over:every-april-cut-recaptured"},
    {"id": "R_STATICS_COVER", "mechanism": "A18", "prior_family": "A18",
     "prior_family_reason": "a needle topical search cannot reach: the post shares no word with the ask's sources; v2 trap 2 changing a write; no Opus 5.5 ledger record (Beta(1,1))",
     "nodes": ["T21", "CH10"], "requirement": "R8", "natural_reading": "Martin has the stills, as Leonard's split says",
     "decides": ["owner"], "source": "martin-leave-post", "signature": "statics-to-julia",
     "controls": [ICON, IPAD], "over_application": "over:every-martin-piece-to-julia"},
    {"id": "R_TABLET_TRIM", "mechanism": "A13", "prior_family": "A13",
     "prior_family_reason": "v2 trap 8 shape: a changed input to a decision, in a mail that shares no words with the plan; no Opus 5.5 ledger record (Beta(1,1))",
     "nodes": ["T22", "CH11"], "requirement": "R6", "natural_reading": "the ticket's campaign note is current, so the cut stays on iOS UK tablet",
     "decides": ["Halloween call per surface"], "source": "fred-restart-mail", "signature": "left-ios-tablet",
     "controls": ["boris alin2 16:9", "couch boss 30 16:9"], "over_application": "over:every-landscape-cut-skipped"},
    {"id": "R_OLD_PACKS", "mechanism": "A12", "prior_family": "A12",
     "prior_family_reason": "v2 trap 5: an exception in another service overrides a rule that looks satisfied; douglas: a page comment bit; no Opus 5.5 ledger record (Beta(1,1))",
     "nodes": ["T23", "CH12"], "requirement": "R2", "natural_reading": "a render from a current build takes a Halloween version as it is",
     "decides": ["Halloween call per surface"], "source": "fred-packs-comment", "signature": "old-packs-rerender",
     "controls": HV_SAMPLE, "over_application": "over:every-august-render-refreshed"},
]

WRITES = [
    {"service": "gdocs", "tool": "gdocs_create_document", "count": 1, "depends_on": ["K13", "R_BUILD_CUT", "R_FLIGHT_CHANGE", "R_REVIEW_WINDOW"], "requirements": ["R10", "R3", "R4", "R5"]},
    {"service": "gdocs", "tool": "gdocs_batch_update", "count": 3, "depends_on": ["R_BUILD_CUT", "R_FLIGHT_CHANGE", "R_REVIEW_WINDOW"], "requirements": ["R3", "R4", "R5"]},
    {"service": "gsheets", "tool": "gsheets_create_spreadsheet", "count": 1, "depends_on": ["K13"], "requirements": ["R10"]},
    {"service": "gsheets", "tool": "gsheets_values_update", "count": 2, "depends_on": ["R_ART_CURRENT", "R_SCOPE_SERVING", "R_DONE_EXPORT", "R_TEST_TURNED_DOWN", "R_FLIGHT_CHANGE", "R_BUILD_CUT", "R_REVIEW_WINDOW", "R_RECAPTURE_NOTE", "R_STATICS_COVER", "R_TABLET_TRIM", "R_OLD_PACKS", "K1"], "requirements": ["R1", "R2", "R4", "R5", "R6", "R8"]},
    {"service": "linear", "tool": "linear_create_comment", "count": N_ADS, "depends_on": ["K14", "R_ART_CURRENT", "R_FLIGHT_CHANGE", "R_TEST_TURNED_DOWN", "R_REVIEW_WINDOW", "R_RECAPTURE_NOTE", "R_TABLET_TRIM", "R_OLD_PACKS"], "requirements": ["R9", "R2", "R5"]},
    {"service": "linear", "tool": "linear_update_issue", "count": N_ASSIGN, "depends_on": ["K17", "K9", "R_TEST_TURNED_DOWN", "R_FLIGHT_CHANGE", "R_STATICS_COVER", "R_TABLET_TRIM"], "requirements": ["R8"]},
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
    B("rules", "slack", 1, "read Frederick's reply in the Sep 30 fake-installs thread (the Android hand-off date)"),
    B("rules", "slack", 1, "read Martin's vacation post and Leonard's reply in #company-internal (who takes the ad statics)"),
    B("rules", "gmail", 1, "read Frederick's Sep 29 restart mail (which cuts left iOS UK tablet)"),
    B("enumeration", "linear", 2, f"list the ART library tickets ({len(LIBRARY)}, two pages) to map each sheet row to its ticket and find the serving tickets the sheet omits"),
    B("enumeration", "gdrive", 3, "list the Halloween folder and its Store and UA masters subfolders (which Halloween versions exist)"),
    B("per-record", "linear", N_ADS, "linear_list_comments per serving ad ticket: campaigns, source build, master audio and any re-capture decide every ad's call (no bulk comment endpoint)"),
    B("per-record", "slack", 1, "read Frederick's Aug 13 thread the 30 s cut's ticket points to for its master (the music is baked in; a reply-only fact)"),
    B("per-record", "slack", 1, "read Marcus's #zm-animations note (three re-captures the tickets do not show)"),
    B("per-record", "slack", 1, "read Robert's review in the thread under Marcus's #zombie-art test post (the cheer fastcouch test cannot ship)"),
    B("per-record", "trello", 1, "read Frederick's comment on the Marketing Video Refresh card (old zombies on the packs in end card 001 and its cuts)"),
    B("per-record", "linear", N_ADS, "comment each serving ad's Halloween call and due date on its ART ticket (the ask's follow-through; one comment per ticket, no bulk)"),
    B("per-record", "linear", N_ASSIGN, "assign each ad that needs new work (Halloween version or Refresh first) to its maker on its ticket; Skip ads stay unassigned (one update per ticket)"),
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
    B("rules", "github", 1, "check the match3d repo for the KayKit pack", conditional_on="runs that check what the vendor offers against the repo"),
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
# rev3: the Android hand-off, up to Fri Oct 10 (an earlier internal date is fair); and the rest, Oct 11-15 only
DUE_OCT10 = (r"oct(?:ober)?\.? ?(?:10|0?[6-9])" + ORD + r"\b|10/(?:10|0?[6-9])\b|2025-10-(?:10|0[6-9])"
             r"|(?:10|0?[6-9])" + ORD + r" (?:of )?oct")
DUE_CELL10 = r"^ *(?:(?:mon|tue|wed|thu|fri|sat|sun)[a-z]*,? )?(?:" + DUE_OCT10 + ")"
DUE_LATE = (r"oct(?:ober)?\.? ?1[1-5]" + ORD + r"\b|10/1[1-5]\b|2025-10-1[1-5]|1[1-5]" + ORD + r" (?:of )?oct")
DUE_CELL_LATE = r"^ *(?:(?:mon|tue|wed|thu|fri|sat|sun)[a-z]*,? )?(?:" + DUE_LATE + ")"
SLOTS = [
    # build cut (icon)
    # done gap (store sets)
    slot("S03", "iPad 12.9-inch store set is a Halloween version still to make", 5, MSR, "Martin's 'exported' claim, the Store tab's live sets and the Halloween Store folder listing must be reconciled", "direct", "exception", ["field", IPAD, "call"], "ipad.call", ["R_DONE_EXPORT"], by="K12"),
    slot("S26", "One new-ticket field (title or a description line) names the Halloween icon", 1, "lookup", "the icon is new store art the ask routes to a ticket", "write_content", "core", ["text", "tickets", r"icon[^\n]*halloween|halloween[^\n]*icon"], "icon.ticket"),
    slot("S04", "One new-ticket field (title or a description line) names the Halloween iPad set", 3, LR, "the iPad gap found above becomes new store art with its own ticket", "write_content", "core", ["text", "tickets", r"ipad[^\n]*halloween|halloween[^\n]*ipad"], "ipad.ticket", ["R_DONE_EXPORT"]),
    # done source with a missing piece
    slot("S05", f"{REUSE_CUTS[0]} gets a Halloween version (Marcus's test was turned down)", 5, MSR, "Marcus's DM and the file in UA masters are overturned by Robert's review in a #zombie-art thread, joined with the ticket's Sep 16 re-capture", "direct", "exception", ["field", REUSE_CUTS[0], "call"], "reuse1.call", ["R_TEST_TURNED_DOWN"], by="K21"),
    slot("S06", f"{REUSE_CUTS[1]} gets a Halloween version (Marcus's test was turned down)", 5, MSR, "the same review covers the tablet cut, matched to its own sheet row, ticket and file", "direct", "exception", ["field", REUSE_CUTS[1], "call"], "reuse2.call", ["R_TEST_TURNED_DOWN"], by="K21"),
    # flight change
    slot("S08", f"{SKIP_MUSIC} is skipped for October", 5, MSR, "the ticket's campaign note is joined with the mail's Android US tablet end date, which outranks the cut's baked-in music", "direct", "exception", ["field", SKIP_MUSIC, "call"], "skip.call", ["R_FLIGHT_CHANGE"], by="H4"),
    slot("S09", f"{TWO_TABLETS} is kept and refreshed first", 3, "comparison", "its ticket's campaigns (iOS UK tablet as well) are compared with the mail's 'only runs there'", "direct", "exception", ["field", TWO_TABLETS, "call"], "twotab.call", ["R_FLIGHT_CHANGE", "R_ART_CURRENT"], by="H4"),
    slot("S28", f"{CHEER_45} gets a Halloween version (not covered by Marcus's DM)", 5, MSR, "Marcus's reply names the 9:16 and the 16:9, the UA masters folder holds those two only, and the 4:5's own ticket shows a later cut from the Sep 16 re-capture", "direct", "exception", ["field", CHEER_45, "call"], "cheer45.call", ["R_TEST_TURNED_DOWN"], by="K16"),
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
    slot("S17", f"{RECAP[0]} gets a Halloween version (re-captured)", 5, MSR, "the ticket's April capture is superseded by Marcus's #zm-animations note under the deck's newest-capture rule", "direct", "exception", ["field", RECAP[0], "call"], "recap1.call", ["R_RECAPTURE_NOTE"], by="K20"),
    slot("S18", f"{RECAP[1]} gets a Halloween version (re-captured)", 5, MSR, "the same note's #1896 is joined with the ticket's April capture and the deck's threshold", "direct", "exception", ["field", RECAP[1], "call"], "recap2.call", ["R_RECAPTURE_NOTE"], by="K20"),
    slot("S30", f"{RECAP[2]} gets a Halloween version (re-captured)", 5, MSR, "the same note's #1966 is joined with the ticket's April capture and the deck's threshold", "direct", "exception", ["field", RECAP[2], "call"], "recap3.call", ["R_RECAPTURE_NOTE"], by="K20"),
    # Android review window
    slot("S37", f"{ANDROID_DUE[0]} is due by Fri Oct 10", 5, MSR, "the ticket's Android US phone campaign is joined with Frederick's thread reply, which overrides his Sep 30 mail", "write_content", "exception", ["reason_matches", ANDROID_DUE[0], DUE_CELL10], "android1.due", ["R_REVIEW_WINDOW"], by="K19"),
    slot("S38", f"{ANDROID_DUE[1]} is due by Fri Oct 10", 5, MSR, "a second ad on Android US phone under the same reply", "write_content", "exception", ["reason_matches", ANDROID_DUE[1], DUE_CELL10], "android2.due", ["R_REVIEW_WINDOW"], by="K19"),
    slot("S39", f"{IOS_DUE} stays on Wed Oct 15", 3, "comparison", "its ticket's iOS UK phone campaign is compared with 'iOS UK stays on the 15th'", "write_content", "exception", ["reason_matches", IOS_DUE, DUE_CELL_LATE], "ios.due", ["R_REVIEW_WINDOW"], by="K19"),
    # statics cover
    slot("S31", f"{STATIC_KEYS[0]} goes to Julia Lawson", 5, MSR, "Leonard's split is overridden by Martin's #company-internal post and Leonard's reply, applied to a still", "direct", "exception", ["field", STATIC_KEYS[0], "owner"], "static1.owner", ["R_STATICS_COVER"], by="K22"),
    slot("S32", f"{STATIC_KEYS[1]} goes to Julia Lawson", 5, MSR, "the same post, applied to a second still", "direct", "exception", ["field", STATIC_KEYS[1], "owner"], "static2.owner", ["R_STATICS_COVER"], by="K22"),
    # tablet trim
    slot("S33", f"{TRIM_KEYS[0]} is skipped for October", 5, MSR, "the ticket's campaign note is corrected by Frederick's restart mail, then his Sep 30 rule applies", "direct", "exception", ["field", TRIM_KEYS[0], "call"], "trim1.call", ["R_TABLET_TRIM"], by="K23"),
    slot("S34", f"{TRIM_KEYS[1]} is skipped for October", 5, MSR, "the same mail, applied to the second landscape cut", "direct", "exception", ["field", TRIM_KEYS[1], "call"], "trim2.call", ["R_TABLET_TRIM"], by="K23"),
    # old zombies on the packs
    slot("S35", f"{LOGO_KEYS[0]} is refreshed first (old zombies on the packs)", 5, MSR, "a build that passes the deck's rule is overridden by Frederick's card comment, under the deck's re-render call", "direct", "exception", ["field", LOGO_KEYS[0], "call"], "logo1.call", ["R_OLD_PACKS"], by="K24"),
    slot("S36", f"{LOGO_KEYS[1]} is refreshed first (old zombies on the packs)", 5, MSR, "the same comment reaches the cut made from it, matched to its own ticket", "direct", "exception", ["field", LOGO_KEYS[1], "call"], "logo2.call", ["R_OLD_PACKS"], by="K24"),
    # follow-through
    # ordinary samples (calls group)
    slot("S21", f"{RF_SAMPLE[0]} is refreshed first", 3, "interpretation", "an April capture read against the deck's threshold", "direct", "sample", ["field", RF_SAMPLE[0], "call"], "rf1.call", group="calls"),
    slot("S22", f"{RF_SAMPLE[1]} is refreshed first", 3, "interpretation", "a June static whose source build predates the swap", "direct", "sample", ["field", RF_SAMPLE[1], "call"], "rf2.call", group="calls"),
    slot("S23", f"{HV_SAMPLE[0]} gets a Halloween version", 3, "interpretation", "a current-build export with an SFX-only master read against the deck's calls", "direct", "sample", ["field", HV_SAMPLE[0], "call"], "hv1.call", group="calls"),
    slot("S24", f"{IPHONE} is reused", 3, "interpretation", "the Halloween iPhone set is in the Store folder", "direct", "sample", ["field", IPHONE, "call"], "iphone.call", group="calls"),
    slot("S25", f"{ICON} gets a Halloween version", 3, "interpretation", "Robert turned the concept down for the icon, so the icon is a new piece", "direct", "sample", ["field", ICON, "call"], "icon.call", group="calls"),
    # delivery
    slot("D01", "A reply is posted in Leonard's thread", 1, "lookup", "delivery into the named thread is a direct check", "delivery", "core", ["delivery", "slack_thread", ASK.split("/")[1]], "reply.thread"),
    slot("D02", "The tracker's own link (its file id) is in a Slack message, and the tracker is shared", 1, "lookup", "the decoded tracker's identity in the reply is a direct check", "delivery", "core", ["link", "slack"], "tracker.link"),
]


# facts the surface cannot decode deterministically (per-ticket coverage, issue-to-owner mapping, plan text written
# through either Docs path): graded by rubric rows, recorded for /create-rubric-writing (scenario_gen/rubric_only_facts.json)
RUBRIC_ONLY = [
    {"id": "RO1", "fact": f"Every one of the {N_ADS} serving ad tickets gets its own comment with that ad's call (Skip included)", "work_kind": LR, "weight": 3, "mechanisms": [], "why_not_surface": "no selector counts comments per issue"},
    {"id": "RO2", "fact": "Each comment on an ad that needs work carries its hand-off date: Fri Oct 10 on Android US phone, Wed Oct 15 otherwise", "work_kind": LR, "weight": 3, "mechanisms": ["R_FLIGHT_CHANGE", "R_REVIEW_WINDOW"], "why_not_surface": "comment text is concatenated across issues"},
    {"id": "RO3", "fact": f"Exactly the {N_ASSIGN} ads that need new work are assigned to their maker ({sum(1 for r in ADS if r.get('assign_to') == 'Marcus Bennett')} to Marcus, {sum(1 for r in ADS if r.get('assign_to') == 'Julia Lawson')} to Julia); the {sum(1 for r in ADS if r['call'] == 'Skip October')} Skip ads stay unassigned", "work_kind": MSR, "weight": 5, "mechanisms": ["R_TEST_TURNED_DOWN", "R_FLIGHT_CHANGE", "R_STATICS_COVER", "R_TABLET_TRIM"], "why_not_surface": "assignee identity per issue is not decoded"},
    {"id": "RO7", "fact": "The plan doc and the tracker are shared with the review attendees so they can comment, and both links are in Leonard's thread", "work_kind": "lookup", "weight": 1, "mechanisms": [], "why_not_surface": "share_reader binds to the tracker and the reader role; the plan link is not a decoded identity"},
    {"id": "RO8", "fact": "The new Halloween icon ticket is due by the Thu Oct 16 12:00 PT merge cut; the iPad set ticket by the same cut", "work_kind": LR, "weight": 3, "mechanisms": ["R_BUILD_CUT"], "why_not_surface": "ticket text is concatenated across new tickets and a time of day is not decoded"},
    {"id": "RO9", "fact": "In the tracker, the app icon and the iPad and iPhone store sets are due by the Thu Oct 16 12:00 PT merge cut (an earlier internal date is fair); the Google Play set has no fixed date", "work_kind": MSR, "weight": 5, "mechanisms": ["R_BUILD_CUT"], "why_not_surface": "a due window (any date up to the cut) needs a date comparison the field comparators do not have"},
    {"id": "RO10", "fact": f"In the tracker, every ad on Android US phone that needs new work is due with Frederick by Fri Oct 10, every other working ad by Wed Oct 15 (not Fri Oct 17); Skip ads have no due date", "work_kind": MSR, "weight": 5, "mechanisms": ["R_FLIGHT_CHANGE", "R_REVIEW_WINDOW"], "why_not_surface": "as RO9"},
    {"id": "RO6", "fact": "The plan says the Halloween icon ships in the Oct 17 store build (merged by the Oct 16 12:00 PT cut), not as a standalone swap around Oct 24", "work_kind": "interpretation", "weight": 3, "mechanisms": ["R_BUILD_CUT"], "why_not_surface": "plan text can arrive through gdocs_create_document bodyText or gdocs_batch_update; one deliverable reads one tool"},
]


def build_surface() -> dict:
    return {
        "kind": "GRADABLE_SURFACE", "version": 1, "task": "claire-zm3d-halloween-art-plan", "revision": "scenario-03",
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
