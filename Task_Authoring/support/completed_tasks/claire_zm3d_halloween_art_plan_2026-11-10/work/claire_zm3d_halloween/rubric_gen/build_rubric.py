#!/usr/bin/env python3
"""Build 09_Rubrics.json, the V3 rubric_rows evidence and rows.json (input to the plan and check builders) for
claire-zm3d-halloween-art-plan, injection rev3. Calls, due dates and makers come from oe_gen/model.py, which re-derives
them from the seeded rows and asserts them against solver/truth.json. Every quoted span is asserted against its record
here. The rubric text carries no em dash, no en dash and no local file reference."""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TI = WF.parent
WS = TI.parents[1]
sys.path.insert(0, str(WF / "oe_gen"))
sys.path.insert(0, str(WS / "Task_Authoring/tools"))
import model as M  # noqa: E402
from base_check import parse_sql  # noqa: E402

SQL = parse_sql((TI / "01_Universe_Inject.sql").read_text())
PROMPT = (TI / "04_Prompt.txt").read_text()
LBL = json.load(open(WF / "oe_gen/events.json"))["label"]
FID = json.load(open(WF / "oe_gen/oe_ledger_ids.json"))["fid"]
REVIEWER = "Claude (model-drafted under GEN_EXECUTION §2; for the human author's review)"


def sql_row(table, **ident):
    rows = [x["row"] for x in SQL if x.get("table") == table and x["op"] == "insert"
            and all(x["row"].get(k) == v for k, v in ident.items())]
    assert len(rows) == 1, (table, ident, len(rows))
    return rows[0]


def path(*hops):
    return [{"service": s, "id": i} for s, i in hops]


def S(service, rid, table, ident, column, rec_col, hops, why, semantics="fact"):
    row = sql_row(table, **ident)
    return {"service": service, "id": rid, "source_file": "01_Universe_Inject.sql", "table": table, "identity": ident,
            "column": column, "source_value": row[column], "evidence_path": path(*hops), "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": semantics, "mutable_state": False, "recorded_at_column": rec_col,
                                  "rationale": f"Seeded {table} row; {rec_col} = {row[rec_col]} (before the freeze)."}}


# ---- records ---------------------------------------------------------------------------------------------------
ASK_ID = "C06DJBJL798/1759269913.882683"
REPLY_ID = "C0880U9751A/1759275738.984915"
LEAVE_ID = "C05KNDCHAAG/1759243286.478812"
LEAVE_OK_ID = "C05KNDCHAAG/1759275107.322377"
NOTE_ID = "C09ATAJ220H/1758823964.738872"
IM_ID = "D05V2N6PZNU/1759166437.080255"
TEST_ID = "C08R8CHB0QL/1759167065.499092"
ROBERT_ID = "C08R8CHB0QL/1759248337.170599"
EXPORT_ID = "C08R8CHB0QL/1759245641.309714"
EXPORT_OK_ID = "C08R8CHB0QL/1759247246.453725"
ICON_NO_ID = "C08R8CHB0QL/1758127951.679146"
MUSIC_ID = "C06DJBJL798/1755114007.441789"
SHEET = "f_02b1968f5e882366fbb883"
DECK = "f_5ebf55ad29e815d46243c8"
CAL = "f_fdd6d2d2f4a4d2f5b908fb"
STORE = "d_74a7c95c28097dd9777e01"
MASTERS = "d_6c2e4339e5d58108799ac8"
EVENT = "evt_d947bf7cd910549b674b1f"
MAIL_CH = "claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>"
MAIL_RS = "claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>"
BOARD = "6851a6569f3bf818760632ab"
VIDEO_CARD = "68768a1501ae552dbee94b8a"
PUSH_CMT = "68dc65a0f2d7fb28743f5860"
PACKS_CMT = "68d6cff0c6568da5d9c8e81f"

msg = lambda ts: sql_row("slack.slack_messages", ts=ts)["text"]
ASK = msg("1759269913.882683")
REPLY = msg("1759275738.984915")
LEAVE = msg("1759243286.478812")
LEAVE_OK = msg("1759275107.322377")
NOTE = msg("1758823964.738872")
IM = msg("1759166437.080255")
ROBERT = msg("1759248337.170599")
EXPORT = msg("1759245641.309714")
EXPORT_OK = msg("1759247246.453725")
ICON_NO = msg("1758127951.679146")
CH = sql_row("gmail.gmail_messages", id=MAIL_CH)["body_text"]
RS = sql_row("gmail.gmail_messages", id=MAIL_RS)["body_text"]
DECK_OLD_T = sql_row("gslides.slides_page_elements", object_id="el_1f12d04ad444")["text"]
DECK_CALLS_T = sql_row("gslides.slides_page_elements", object_id="el_b04e5ccd5706")["text"]
CAL_T = sql_row("gdocs.docs_documents", document_id=CAL)["body_text"]
CARD_T = json.loads(sql_row("trello.trello_actions", id=PUSH_CMT)["data_json"])["text"]
PACKS_T = json.loads(sql_row("trello.trello_actions", id=PACKS_CMT)["data_json"])["text"]
GRID_ME = M.GRID["Read me"]


def q(text, s):
    assert s in text, s
    return s


Q_OLD = q(DECK_OLD_T, "Anything captured or rendered from a build older than Android #1452 / iOS 1232 (the zombie swap with the new background, Jul 29) is redone on the current build first.")
Q_NEW = q(DECK_OLD_T, "If a later capture has replaced it, the newest capture is the one that counts.")
Q_MUSIC = q(DECK_OLD_T, "A video whose master has the music baked in is re-cut first from a master without music")
Q_HV = q(DECK_CALLS_T, "Halloween version: dress it from the current art.")
Q_RF = q(DECK_CALLS_T, "Refresh first: re-capture, re-render or re-cut before any seasonal pass.")
Q_RU = q(DECK_CALLS_T, "Reuse: it already has a seasonal version, use that one.")
Q_SK = q(DECK_CALLS_T, "Skip: no seasonal version this time.")
Q_TAB = q(CH, "The Android US tablet campaign ends Sun Oct 12 and its budget moves to iOS UK, so don't make Halloween versions of anything that only runs there.")
Q_15 = q(CH, "every Halloween ad needs to be with me by Wed Oct 15, not the 17th.")
Q_10 = q(REPLY, "So any new ad going on Android US phone has to be with me by Fri Oct 10, not the 15th.")
Q_UK = q(REPLY, "iOS UK stays on the 15th.")
Q_RS = q(RS, "I left squirrelfail landscape and mrfluffernot landscape off iOS UK tablet this time")
Q_RS2 = q(RS, "Both stay on Android US tablet.")
Q_NOTE = q(NOTE, "re-recorded 3 of the old ua cuts for frederick, same edits, no music: couch alpha 50 on android #1935, barrel marketing2 4:5 on #1896, balloons alpha 50 (1) on #1966")
Q_IM = q(IM, "did the cheer fastcouch one, both 9:16 and 16:9, from the no music masters.")
Q_ROB = q(ROBERT, "We can't ship these, they need doing again from the Sep 16 one")
Q_PACKS = q(PACKS_T, "end card 001 still has the old zombies on the packs")
Q_PACKS2 = q(PACKS_T, "Same on the 16:9, 1:1 and 4:5 cut from it.")
Q_CARD = q(CARD_T, "is still running on iOS UK")
Q_CARD2 = q(CARD_T, "It never made it onto the live creatives sheet, so count it in for Halloween.")
Q_LEAVE = q(LEAVE, "takes the ad statics while I'm out, store art stays with me.")
Q_OK = q(LEAVE_OK, "julia on the ad statics works for me")
Q_SPLIT = q(ASK, "Martin has the icon and the stills, Marcus has video and end cards")
Q_24 = q(ASK, "maybe we swap the icon around the 24th?")
Q_EXP = q(EXPORT, "halloween store screens are exported to the halloween folder")
Q_NOTK = q(EXPORT_OK, "tickets are just for store art that still has to be made")
Q_ICON = q(ICON_NO, "Nice for an event, but not for the app icon")
Q_CUT = q(CAL_T, "Merge cut is Thu Oct 16, 12:00 PT.")
Q_CUT2 = q(CAL_T, "Anything that ships in the build has to be merged by then.")
Q_IOS = q(CAL_T, "new iOS screenshots go up with the Oct 17 submission and are due by the same Oct 16 12:00 PT cut.")
ST = "the Store tab of the live creatives sheet " + SHEET
DECKN = f"Robert's seasonal art direction deck {DECK}"
MAILN = f"Frederick's mail 'October UA plan - changes' {MAIL_CH}"
RSN = f"Frederick's mail 'Unity retention restart' {MAIL_RS}"
ASKN = f"Leonard's message {ASK_ID}"

# ---- prompt spans ----------------------------------------------------------------------------------------------
SP_WORK = "Work out the Halloween call for everything that's live today, the store pages and every ad we're running, and who makes what by when"
SP_DOC = "put it in a plan doc and a tracker in my Drive"
SP_SHARE = "shared with everyone on the review so they can comment"
SP_CMT = "Comment each ad's call and due date on its ART ticket"
SP_ASSIGN = "assign the ones that need new work to whoever's making them"
SP_TICKET = "open ART tickets for any new store art"
SP_REPLY = "reply in Leonard's thread with both links before the review"
for s in (SP_WORK, SP_DOC, SP_SHARE, SP_CMT, SP_ASSIGN, SP_TICKET, SP_REPLY):
    assert s in PROMPT, s

# ---- V3 sources ------------------------------------------------------------------------------------------------
LIN = "The gate's Linear lookup reads base data only, so the seeded ticket is cited through its base ART team; the row itself is the seeded record named in identity."
TRL = "The gate's Trello lookup reads base data only, so the seeded comment is cited through its base board or card; the row itself is the seeded action named in identity."
P_ASK = ("slack", ASK_ID)
s_ask = S("slack", ASK_ID, "slack.slack_messages", {"ts": "1759269913.882683"}, "text", "created_at", [P_ASK],
          "The prompt names Leonard's message in #zombie_marketing.")
s_review = S("gcal", EVENT, "gcal.gcal_events", {"event_id": EVENT}, "attendees_json", "updated", [("gcal", EVENT)],
             "The prompt names Thursday's review; it is on Claire's calendar.")
s_sheet = S("gsheets", SHEET, "gsheets.sheets_spreadsheets", {"spreadsheet_id": SHEET}, "title", "modified_time",
            [P_ASK, ("gsheets", SHEET)], "Leonard's message: 'the live creatives sheet is what's running'.")
s_deck = S("gslides", DECK, "gslides.slides_presentations", {"presentation_id": DECK}, "title", "modified_time",
           [P_ASK, ("gslides", DECK)], "Leonard's message: 'Robert has direction for seasonal art'; a Drive search for seasonal finds the deck.")
s_cal = S("gdocs", CAL, "gdocs.docs_documents", {"document_id": CAL}, "body_text", "modified_time",
          [P_ASK, ("gdocs", CAL)], "Leonard's message: 'Arthur's release calendar has the Q4 dates'.")
s_mail = S("gmail", MAIL_CH, "gmail.gmail_messages", {"id": MAIL_CH}, "body_text", "date", [P_ASK, ("gmail", MAIL_CH)],
           "Leonard's message: 'Frederick is sending his october UA plan tonight'; the mail is in Claire's inbox.")
s_rs = S("gmail", MAIL_RS, "gmail.gmail_messages", {"id": MAIL_RS}, "body_text", "date", [P_ASK, ("gmail", MAIL_RS)],
         "A search for Frederick's mail, which Leonard's message sends the Agent to, returns this mail too.")
s_reply = S("slack", REPLY_ID, "slack.slack_messages", {"ts": "1759275738.984915"}, "text", "created_at",
            [P_ASK, ("gsheets", SHEET), ("slack", REPLY_ID)],
            "The sheet's Read me names the Android US phone campaign; a Slack search for that name finds Frederick's reply.")
s_leave = S("slack", LEAVE_ID, "slack.slack_messages", {"ts": "1759243286.478812"}, "text", "created_at",
            [P_ASK, ("slack", LEAVE_ID)], "Leonard's message names who makes the stills; a Slack search for the ad statics finds Martin's post.")
s_ok = S("slack", LEAVE_OK_ID, "slack.slack_messages", {"ts": "1759275107.322377"}, "text", "created_at",
         [P_ASK, ("slack", LEAVE_ID), ("slack", LEAVE_OK_ID)], "Leonard's reply is in the thread of Martin's post.")
s_note = S("slack", NOTE_ID, "slack.slack_messages", {"ts": "1758823964.738872"}, "text", "created_at",
           [P_ASK, ("gsheets", SHEET), ("slack", NOTE_ID)], "A Slack search for the creative names on the sheet finds Marcus's post.")
s_im = S("slack", IM_ID, "slack.slack_messages", {"ts": "1759166437.080255"}, "text", "created_at",
         [P_ASK, ("gsheets", SHEET), ("slack", IM_ID)], "A Slack search for cheer fastcouch, a creative on the sheet, finds Marcus's reply in Claire's DM.")
s_robert = S("slack", ROBERT_ID, "slack.slack_messages", {"ts": "1759248337.170599"}, "text", "created_at",
             [P_ASK, ("gsheets", SHEET), ("slack", TEST_ID), ("slack", ROBERT_ID)],
             "A Slack search for cheer fastcouch, a creative on the sheet, finds Marcus's test post; Robert's reply is in its thread.")
s_export = S("slack", EXPORT_ID, "slack.slack_messages", {"ts": "1759245641.309714"}, "text", "created_at",
             [P_ASK, ("slack", EXPORT_ID)], "A Slack search for the store screens finds Martin's post.")
s_export_ok = S("slack", EXPORT_OK_ID, "slack.slack_messages", {"ts": "1759247246.453725"}, "text", "created_at",
                [P_ASK, ("slack", EXPORT_ID), ("slack", EXPORT_OK_ID)], "Leonard's reply is in the thread of Martin's post.")
s_icon = S("slack", ICON_NO_ID, "slack.slack_messages", {"ts": "1758127951.679146"}, "text", "created_at",
           [P_ASK, ("slack", ICON_NO_ID)], "A Slack search for the app icon finds Martin's concept; Robert's reply is in its thread.")
s_store = S("gdrive", STORE, "gdrive.drive_files", {"id": STORE}, "name", "modified_time",
            [P_ASK, ("gdrive", STORE)], "Martin's post names the Halloween folder; its Store subfolder is listable in Drive.")
s_packs = S("trello", VIDEO_CARD, "trello.trello_actions", {"id": PACKS_CMT}, "data_json", "date", [P_ASK, ("trello", VIDEO_CARD)],
            "A Trello search for end card 001, a creative on the sheet, finds this comment on the Marketing Video Refresh card. " + TRL)
s_card = S("trello", BOARD, "trello.trello_actions", {"id": PUSH_CMT}, "data_json", "date",
           [P_ASK, ("gsheets", SHEET), ("trello", BOARD)],
           "The sheet's Read me sends the Agent to the Halloween push card on the ZM roadmap; this is its comment. " + TRL)


def s_cm(k):
    c = camp_comment(k)
    return S("linear", "team_ART", "linear.linear_comments", {"id": c["id"]}, "body", "created_at",
             [P_ASK, ("gsheets", SHEET), ("linear", "team_ART")],
             f"The sheet's Read me says the campaigns, capture and master notes are in the ticket comments; {k} is an ART ticket. " + LIN)


def s_first(k):
    c = M.CM[k][0]
    return S("linear", "team_ART", "linear.linear_comments", {"id": c["id"]}, "body", "created_at",
             [P_ASK, ("gsheets", SHEET), ("linear", "team_ART")],
             f"The sheet's Read me says the campaigns, capture and master notes are in the ticket comments; {k} is an ART ticket. " + LIN)


def s_issue(k):
    return S("linear", "team_ART", "linear.linear_issues", {"id": k}, "title", "created_at",
             [P_ASK, ("gsheets", SHEET), ("linear", "team_ART")], f"{k} is on the sheet or in the ART team's ticket list. " + LIN)


# ---- ticket helpers --------------------------------------------------------------------------------------------
RX_CAMP = re.compile(r"Unity(?: Sep \d+)?: [^.(]+?(?: \(checked [^)]*\))?\.")


def camp_comment(k):
    c = None
    for x in M.CM[k]:
        if RX_CAMP.search(x["body"]):
            c = x
    assert c, k
    return c


def bodies(k):
    return "; ".join(f"{x['id']}: '{x['body']}'" for x in M.CM[k])


def camps(k):
    return ", ".join(M.campaigns(k))


def tag_name(k):
    return f"{k} ({M.name(k)})"


oe = lambda *keys: [f"OE {LBL[x]}" for x in keys]
CMTS = {"cmts1": range(793, 805), "cmts2": range(805, 817), "cmts3": range(817, 825), "cmts4": range(825, 836), "cmts5": range(840, 855)}


def oe_read(k):
    n = int(k.split("-")[1])
    return next(f"OE {LBL[g]}" for g, r in CMTS.items() if n in r)


def F(*keys):
    return " ".join(FID[x] for x in keys)


def Ft(k):
    return FID[f"t:{k}"]


R = []


def row(**k):
    for a, b in (("dist", "none"), ("amb", "none"), ("grp", "none"), ("ovl", "none"), ("slots", [])):
        k.setdefault(a, b)
    assert k["w"] in (1, 3, 5)
    R.append(k)


# ================================================================ D1 plan doc
OE_DOC = oe("w_doc")
row(tag="doc_create", t="The Agent creates a Google Doc in Claire's Drive as the Halloween plan doc", w=1, kind="lookup",
    why="the prompt names the deliverable", fact="doc.exists", span=SP_DOC, oe=OE_DOC, fids=F("ask"),
    vals="`plan doc`", verify="A new Google Doc", final="A Google Doc the Agent created as Claire",
    acc=["a Google Doc the Agent creates for the Halloween plan, under any title and in any folder of Claire's Drive"],
    alt="A sheet tab or a Slack post is not a plan doc. Title and folder are the Agent's choice.", srcs=[s_ask],
    just="Lookup: the prompt asks for a plan doc in Claire's Drive.",
    ev=f"Source: {ASKN} ('put it all in a plan doc we can comment on plus a tracker'). Accept: a Google Doc the Agent creates for the Halloween plan, under any title and in any folder of Claire's Drive.",
    dec="R6", valid="A Google Doc titled 'ZM3D Halloween art plan'", idle="No Google Doc is created")

STORE_ROWS = [
    ("icon", "the app icon", "Halloween version", 5, "multi-source", "T13 T16 CH6",
     f"Multi-source: the Store tab lists the app icon, Martin's Sep 17 post offers a Halloween concept, Robert's reply turns it down for the app icon, and the deck's Reuse needs a seasonal version that exists.",
     f"Sources: Martin's concept post C08R8CHB0QL/1758121809.236839, Robert's reply {ICON_NO_ID} ('{Q_ICON}'), {ST} (row 'app icon'), {DECKN} ('{Q_HV}'; '{Q_RU}').", [s_icon, s_sheet],
     "T10 Martin's concept"),
    ("ipad", "the iPad 12.9\" set", "Halloween version", 5, "multi-source", "T1 CH1",
     f"Multi-source: Martin's post says the store screens are exported, {'the Store tab lists the iPad 12.9 set'}, and the Halloween Store folder holds iPhone and Google Play files only.",
     f"Sources: Martin's post {EXPORT_ID} ('{Q_EXP}'), {ST} (row 'iPad 12.9\" set'), Drive folder Store {STORE} (11 PNG files named iPhone65 and GooglePlay_phone, none named iPad), {DECKN} ('{Q_HV}').",
     [s_export, s_sheet, s_store], "T11 Martin's 'exported'"),
    ("iphone", "the iPhone 6.5\" set", "Reuse", 3, "interpretation", "T1 CH1",
     f"Interpretation: Martin's export is in the Halloween Store folder as five iPhone65 files, so this set already has a seasonal version.",
     f"Sources: Martin's post {EXPORT_ID} ('{Q_EXP}'), Drive folder Store {STORE} (five ZM3D_Halloween_iPhone65 PNG files), {DECKN} ('{Q_RU}').",
     [s_export, s_store], "none"),
    ("play", "the Google Play phone set", "Reuse", 3, "interpretation", "T1 CH1",
     f"Interpretation: Martin's export is in the Halloween Store folder as six GooglePlay_phone files, so this set already has a seasonal version.",
     f"Sources: Martin's post {EXPORT_ID} ('{Q_EXP}'), Drive folder Store {STORE} (six ZM3D_Halloween_GooglePlay_phone PNG files), {DECKN} ('{Q_RU}').",
     [s_export, s_store], "none"),
]
for key, nm, call, w, kind, dec, just, src, srcs, dist in STORE_ROWS:
    verb = "gets a Halloween version" if call == "Halloween version" else "is Reuse"
    row(tag=f"doc_{key}_call", t=f"The Agent states in its plan doc that {nm} {verb} (in any wording with that meaning)", w=w, kind=kind, why=just.split(": ", 1)[1], fact=f"{key}.call",
        span=SP_WORK, oe=OE_DOC + oe("d_store"), fids=F("d_store", "store", "export"), vals=f"`{nm.replace('the ', '')}` `{call}`",
        verify=f"The call for {nm} in the plan doc", final="Plan doc body", acc=[f"the plan doc says {nm} {verb}, in any wording with that meaning"],
        alt=f"The word from the deck or any wording with that meaning passes; another call for {nm} fails.", srcs=srcs, just=just,
        ev=f"{src} Accept: the plan doc says {nm} {verb}, in any wording with that meaning.", dec=dec, dist=dist,
        valid=f"A plan doc line '{nm}: {call}'", idle="No plan doc exists")

COUNT_EV = {
    "Refresh first": f"the 31 running tickets whose source predates the swap in {DECKN} ('{Q_OLD}'), ART-809 with the music-baked master in Frederick's thread {MUSIC_ID}, and ART-833, ART-834, ART-835 and ART-848 in Frederick's comment {PACKS_CMT} ('{Q_PACKS}'; '{Q_PACKS2}')",
    "Halloween version": f"ART-795, ART-797 and ART-805 in Marcus's post {NOTE_ID}, ART-808 and ART-816 in Robert's reply {ROBERT_ID} ('{Q_ROB}'), and ART-817, ART-818, ART-819, ART-851, ART-852, ART-853 and ART-854 on current captures under {DECKN} ('{Q_HV}')",
    "Skip": f"ART-806, ART-820, ART-821, ART-822, ART-824, ART-842, ART-844 and ART-849 on Android US tablet alone, ART-811 and ART-813 moved there by {RSN} ('{Q_RS}'), and {MAILN} ('{Q_TAB}')"}
COUNT_ACC = {"Refresh first": "the plan doc gives 36 as the number of ads that are Refresh first, or lists exactly 36 such ads",
             "Halloween version": "the plan doc gives 12 as the number of ads that get a Halloween version, lists exactly 12 such ads, or gives 14 surfaces counting the app icon and the iPad 12.9\" set",
             "Skip": "the plan doc gives 10 as the number of ads that are Skip, or lists exactly 10 such ads"}
for call, n, w_key in (("Refresh first", 36, "d_rf"), ("Halloween version", 12, "d_hv"), ("Skip", 10, "d_skip")):
    say = {"Refresh first": "are Refresh first", "Halloween version": "get a Halloween version", "Skip": "are Skip"}[call]
    extra_t = " (as a total, as a list of the ads, or as 14 surfaces counting the app icon and the iPad 12.9\" set)" if call == "Halloween version" else " (as a total or as a list of the ads)"
    row(tag=f"doc_count_{call.split()[0].lower()}", t=f"The Agent states in its plan doc that {n} ads {say}{extra_t}",
        w=5, kind="multi-source", why=f"the count comes only from every ad's ticket read against the deck, the mails and the other records that change a call",
        fact=f"ads.{call.split()[0].lower()}.count", span=SP_WORK, oe=OE_DOC + oe(w_key), fids=F(w_key), vals=f"`{n}` `{call}`",
        verify=f"The number of {call} ads in the plan doc", final="Plan doc body",
        acc=[COUNT_ACC[call]],
        alt="Any other count fails.",
        srcs=[s_deck, s_mail], just=f"Multi-source: the {n} comes from all 58 ad tickets read against the deck, Frederick's mails and the Slack and Trello records that change single calls.",
        ev=f"Sources: {COUNT_EV[call]}. Accept: {COUNT_ACC[call]}.",
        dec="H3 H4", grp="G0 doc counts", valid=f"A plan doc line '{call}: {n} ads'", idle="No plan doc exists")

row(tag="doc_due10", t="The Agent states in its plan doc that ads on Android US phone are due Oct 10, 2025 (any date form; an earlier October 2025 date also passes; as the rule, or as a list of those ads with that date)", w=5, kind="multi-source",
    why="Frederick's mail says Wed Oct 15 for every ad, and his later Slack reply moves Android US phone to Fri Oct 10", fact="due.android_phone_rule", span=SP_WORK,
    oe=OE_DOC + oe("d_due", "reply"), fids=F("reply", "changes", "d_due"), vals="`Android US phone` `Fri Oct 10`", verify="The Android US phone date in the plan doc", final="Plan doc body",
    acc=["the plan doc gives Oct 10, 2025, or an earlier October 2025 date, as the due date for ads on Android US phone, in any date form, as the rule or as a list of those ads with that date"],
    alt="Oct 15 for these ads fails: Frederick's reply is 32 minutes after his mail and names the campaign. A doc that names the date ad by ad passes.", srcs=[s_reply, s_mail],
    just="Multi-source: Frederick's Sep 30 mail (Gmail) says every Halloween ad is due Wed Oct 15, and his later reply in #zombie-match3d (Slack) moves Android US phone to Fri Oct 10.",
    ev=f"Sources: {MAILN} ('{Q_15}'), Frederick's reply {REPLY_ID} ('{Q_10}'). Route: a Slack search for Android US phone, the campaign the sheet's Read me names, finds the reply. Accept: the plan doc gives Oct 10, 2025, or an earlier October 2025 date, as the due date for ads on Android US phone, in any date form, as the rule or as a list of those ads with that date.",
    dec="T20 CH8", dist="T1 Frederick's Sep 30 mail", valid="A plan doc line 'Android US phone ads: with Frederick by Fri Oct 10'", idle="No plan doc exists")
row(tag="doc_due15", t="The Agent states in its plan doc that every ad with a Halloween version or Refresh first call that is not on Android US phone is due Oct 15, 2025 (any date form; a date from Oct 11 to Oct 14, 2025 also passes; as the rule, or as a list of those ads with that date)", w=3, kind="comparison",
    why="Frederick's mail date holds for the ads his later reply leaves out", fact="due.other_rule", span=SP_WORK, oe=OE_DOC + oe("d_due", "changes"), fids=F("changes", "reply", "d_due"),
    vals="`iOS UK` `Wed Oct 15`", verify="The date for the other working ads in the plan doc", final="Plan doc body",
    acc=["the plan doc gives Oct 15, 2025, or a date from Oct 11 to Oct 14, 2025, as the due date for the ads with a Halloween version or Refresh first call that are not on Android US phone, in any date form, as the rule or as a list of those ads with that date"],
    alt="The draft's Oct 17 fails. A doc that names the date ad by ad passes.", srcs=[s_mail, s_reply],
    just="Comparison: Frederick's reply moves only Android US phone, so his mail's Wed Oct 15 holds for the other working ads ('iOS UK stays on the 15th').",
    ev=f"Sources: {MAILN} ('{Q_15}'), Frederick's reply {REPLY_ID} ('{Q_UK}'). Accept: the plan doc gives Oct 15, 2025, or a date from Oct 11 to Oct 14, 2025, as the due date for the ads with a Halloween version or Refresh first call that are not on Android US phone, in any date form, as the rule or as a list of those ads with that date.",
    dec="T4 CH3", dist="T2 Frederick's Sep 12 draft", valid="A plan doc line 'everything else with Frederick by Wed Oct 15'", idle="No plan doc exists")

for key, nm, dist in (("icon", "the app icon", "T9 Leonard's 'around the 24th'"), ("ipad", "the iPad 12.9\" set", "none")):
    cal_q = Q_CUT2 if key == "icon" else Q_IOS
    pre = (f"Interpretation: the icon ships inside the app, so the calendar's merge cut for the Oct 17 build sets its date, not Leonard's 'around the 24th'." if key == "icon"
           else "Interpretation: new iOS screenshots go up with the Oct 17 submission, so the calendar's merge cut sets the date for this set.")
    srcs = [s_cal, s_ask] if key == "icon" else [s_cal]
    extra = f"{ASKN} ('{Q_24}'), " if key == "icon" else ""
    for where, tagp, grp_oe in (("doc", "doc", OE_DOC), ("tracker", "trk", oe("w_rows"))):
        say = (f"The Agent states in its plan doc that {nm} is due by the Oct 16, 2025 merge cut (any date form; an earlier October 2025 date also passes)" if where == "doc"
               else f"The Agent gives {nm} a due date of Oct 16, 2025 in its tracker (any date form; an earlier October 2025 date also passes)")
        row(tag=f"{tagp}_{key}_due", t=say, w=3, kind="interpretation", why=pre.split(": ", 1)[1], fact=f"{key}.due", span=SP_WORK, oe=grp_oe + oe("calendar", "d_store"),
            fids=F("calendar", "d_store"), vals="`Oct 16` `12:00 PT`", verify=f"The date for {nm} in the {where}", final=("Plan doc body" if where == "doc" else "Tracker row"),
            acc=[f"Oct 16, 2025, or an earlier October 2025 date, for {nm} in the {where}, in any date form"],
            alt="Oct 17 is the submission, after the cut; Oct 24 is Leonard's guess. Both fail. An earlier internal date is fair because the cut is a last date.", srcs=srcs, just=pre,
            ev=f"Sources: {extra}Arthur's release calendar {CAL} ('{Q_CUT}'; '{cal_q}'). Accept: Oct 16, 2025, or an earlier October 2025 date, for {nm} in the {where}, in any date form.",
            dec="T2 T16 CH6", dist=dist, valid=f"'{nm}: by Thu Oct 16 12:00 PT'", idle=f"No {'plan doc' if where == 'doc' else 'tracker'} exists")

row(tag="doc_julia", t="The Agent names Julia Lawson in its plan doc as the maker or owner of the ad statics", w=5, kind="multi-source",
    why="Leonard's ask gives the stills to Martin; Martin's later post and Leonard's reply hand the ad statics to Julia", fact="statics.maker", span=SP_WORK, oe=OE_DOC + oe("leave", "who", "d_maker"),
    fids=F("leave", "leave_ok", "who", "d_maker"), vals="`Julia Lawson` `ad statics`", verify="The maker of the ad statics in the plan doc", final="Plan doc body",
    acc=["the plan doc names Julia Lawson as the maker or owner of the ad statics"], alt="Martin as maker of the ad statics fails: his due dates fall inside his Oct 6-15 vacation and Leonard agreed the hand-off.",
    srcs=[s_ask, s_leave, s_ok], just="Multi-source: Leonard's ask gives the stills to Martin, Martin's #company-internal post tags Julia for the ad statics, and Leonard's later reply agrees.",
    ev=f"Sources: {ASKN} ('{Q_SPLIT}'), Martin's post {LEAVE_ID} ('{Q_LEAVE}'; the tag resolves to Julia Lawson), Leonard's reply {LEAVE_OK_ID} ('{Q_OK}'). Route: a Slack search for the ad statics finds Martin's post. Accept: the plan doc names Julia Lawson as the maker or owner of the ad statics.",
    dec="T21 CH10", dist="T5 Leonard's split", valid="A plan doc line 'Julia Lawson: ad statics'", idle="No plan doc exists")
for mk, part in (("video", "the video ads"), ("endcards", "the end cards")):
    row(tag=f"doc_marcus_{mk}", t=f"The Agent names Marcus Bennett in its plan doc as the maker or owner of {part}", w=1, kind="lookup", why="Leonard's message says it in one line", fact=f"{mk}.maker",
        span=SP_WORK, oe=OE_DOC + oe("ask"), fids=F("ask", "d_maker"), vals="`Marcus Bennett`", verify=f"The maker of {part} in the plan doc", final="Plan doc body",
        acc=[f"the plan doc names Marcus Bennett as the maker or owner of {part}"], alt="Marcus Lee is a different person and fails.", srcs=[s_ask],
        just="Lookup: Leonard's message says Marcus has video and end cards.", ev=f"Source: {ASKN} ('{Q_SPLIT}'). Accept: the plan doc names Marcus Bennett as the maker or owner of {part}.",
        dec="R5", valid=f"A plan doc line 'Marcus: {part}'", idle="No plan doc exists")
row(tag="doc_martin_icon", t="The Agent names Martin Walsh in its plan doc as the maker or owner of the app icon", w=1, kind="lookup", why="Leonard's message says it in one line", fact="icon.maker", span=SP_WORK,
    oe=OE_DOC + oe("ask"), fids=F("ask", "d_store"), vals="`Martin Walsh`", verify="The maker of the app icon in the plan doc", final="Plan doc body",
    acc=["the plan doc names Martin Walsh as the maker or owner of the app icon"], alt="Another maker fails.", srcs=[s_ask], just="Lookup: Leonard's message says Martin has the icon.",
    ev=f"Source: {ASKN} ('{Q_SPLIT}'). Accept: the plan doc names Martin Walsh as the maker or owner of the app icon.", dec="R5", valid="A plan doc line 'Martin: app icon'", idle="No plan doc exists")
row(tag="doc_martin_ipad", t="The Agent names Martin Walsh in its plan doc as the maker or owner of the iPad 12.9\" set (naming him for the store art also passes)", w=3, kind="interpretation", why="Martin keeps the store art through his vacation", fact="ipad.maker", span=SP_WORK,
    oe=OE_DOC + oe("leave", "d_store"), fids=F("leave", "d_store"), vals="`Martin Walsh` `iPad 12.9`", verify="The maker of the iPad set in the plan doc", final="Plan doc body",
    acc=["the plan doc names Martin Walsh as the maker or owner of the iPad 12.9\" set, or names him for the store art"], alt="Julia fails: the hand-off covers the ad statics only.", srcs=[s_leave],
    just="Interpretation: Martin's vacation post hands over the ad statics only and keeps the store art, so the iPad set stays his.",
    ev=f"Source: Martin's post {LEAVE_ID} ('{Q_LEAVE}'). Accept: the plan doc names Martin Walsh as the maker or owner of the iPad 12.9\" set, or names him for the store art.", dec="T21", valid="A plan doc line 'Martin: iPad 12.9 set'", idle="No plan doc exists")

row(tag="doc_icon_build", t="The Agent states in its plan doc that the app icon ships with the Oct 17, 2025 build", w=3, kind="interpretation", why="the icon ships inside the app, so the calendar's Oct 17 build carries it, not Leonard's 'around the 24th' swap",
    fact="icon.route", span=SP_WORK, oe=OE_DOC + oe("calendar", "d_store"), fids=F("calendar", "ask", "d_store"), vals="`Oct 17`", verify="The icon's ship route in the plan doc", final="Plan doc body",
    acc=["the plan doc says the app icon ships with the Oct 17, 2025 build or submission"], alt="A swap around Oct 24 as the route fails: the Oct 17 build is the last that can carry Halloween changes.", srcs=[s_cal, s_ask],
    just="Interpretation: Leonard asks about a swap around the 24th, and Arthur's calendar makes the Oct 17 submission the last build that can carry Halloween changes, so the icon rides that build.",
    ev=f"Sources: {ASKN} ('{Q_24}'), Arthur's release calendar {CAL} ('{q(CAL_T, 'Oct 17 submission: the last build that can carry Halloween changes.')}'). Accept: the plan doc says the app icon ships with the Oct 17, 2025 build or submission.",
    dec="T2 T16 CH6", dist="T9 Leonard's 'around the 24th'", valid="A plan doc line 'the icon rides the Oct 17 build'", idle="No plan doc exists")
# ================================================================ D2 tracker
OE_TR = oe("w_rows")
row(tag="trk_create", t="The Agent creates a tracker in Claire's Drive", w=1, kind="lookup", why="the prompt names the deliverable", fact="tracker.exists", span=SP_DOC,
    oe=oe("w_sheet"), fids=F("ask"), vals="`tracker`", verify="A new spreadsheet", final="A Google spreadsheet the Agent created as Claire",
    acc=["a file the Agent creates in Claire's Drive as the tracker, under any title and in any folder"], alt="The live creatives sheet is Frederick's and is not the tracker. Title and folder are the Agent's choice.", srcs=[s_ask],
    just="Lookup: the prompt asks for a tracker in Claire's Drive.", ev=f"Source: {ASKN} ('put it all in a plan doc we can comment on plus a tracker'). Accept: a file the Agent creates in Claire's Drive as the tracker, under any title and in any folder.",
    dec="R7", valid="A spreadsheet titled 'ZM3D Halloween tracker'", idle="No spreadsheet is created")
row(tag="trk_rows", t="The Agent lists exactly 62 surfaces in its tracker, the 4 store surfaces plus 58 ads (on one tab or several)", w=5, kind="multi-source",
    why="the count needs the Store and Unity tabs, the two ads off the sheet and the Archive tab left out", fact="tracker.keys", span=SP_WORK, oe=OE_TR + oe("readme", "unity", "archive", "library", "card"),
    fids=F("sheet", "unity", "archive", "library", "card"), vals="`58`", verify="Number of ads with a Halloween call in the tracker", final="Tracker ad rows",
    acc=["the tracker lists the 4 store surfaces and 58 ads, 62 in all, on one tab or several"], alt="56 ads (the sheet alone) or an Archive ticket in place of ART-826 or ART-831 fails; a tab that notes paused creatives with no call does not count against the 58.", srcs=[s_sheet, s_card],
    just="Multi-source: 4 Store rows and 56 Unity rows from the sheet, Julia's 4:5 static from Frederick's Trello comment and ART-831 from its own ticket, with the 4 Archive rows left out.",
    ev=f"Sources: live creatives sheet {SHEET} (Store 4, Unity 56, Archive 4), Frederick's comment {PUSH_CMT} on the Halloween push card ('{Q_CARD2}'), ART-831 comment cmt_art831_2 ('Not on the live creatives sheet yet.'). Accept: the tracker lists the 4 store surfaces and 58 ads, 62 in all, on one tab or several.",
    dec="T6 T14 CH7", dist="T8 the sheet as the whole list", valid="A tracker with 62 surface rows under one header", idle="No tracker exists", slots=["V01"])
for call, n in (("Halloween version", 14), ("Skip", 10), ("Refresh first", 36)):
    nm = call
    row(tag=f"trk_count_{call.split()[0].lower()}", t=f"The Agent marks exactly {n} surfaces {nm} in its tracker", w=5, kind="multi-source",
        why="the count comes only from every surface's records", fact=f"tracker.{call.split()[0].lower()}.count", span=SP_WORK, oe=OE_TR + oe("d_hv", "d_rf", "d_skip", "d_store"),
        fids=F("d_hv", "d_rf", "d_skip", "d_store"), vals=f"`{n}` `{call}`", verify=f"Number of {call} rows", final="Tracker call column",
        acc=[f"exactly {n} tracker rows carry the call {nm}"], alt="Any other count fails.", srcs=[s_deck, s_mail],
        just=f"Multi-source: the {n} comes from all 62 surfaces read against the deck, Frederick's mails and the records that change single calls.",
        ev=f"Sources: {COUNT_EV[call]}" + (f", plus the app icon and the iPad 12.9\" set on {ST}" if call == "Halloween version" else "") + f". Accept: exactly {n} tracker rows carry the call {nm}.",
        dec="H3 H4", grp="G1 tracker calls", valid=f"{n} rows marked {call}", idle="No tracker exists")
for key, nm, call, w, kind, dec, just, src, srcs, dist in STORE_ROWS:
    row(tag=f"trk_{key}_call", t=f"The Agent marks {nm} as {call} in its tracker", w=w, kind=kind, why=just.split(": ", 1)[1], fact=f"{key}.call", span=SP_WORK, oe=OE_TR + oe("d_store"),
        fids=F("d_store", "store", "export"), vals=f"`{nm.replace('the ', '')}` `{call}`", verify=f"The call on the {nm} row", final="Tracker row",
        acc=[f"the {nm.replace('the ', '')} row of the tracker carries the call {call}"], alt=f"Another call on this row fails.", srcs=srcs, just=just,
        ev=f"{src} Accept: the {nm.replace('the ', '')} row of the tracker carries the call {call}.", dec=dec, dist=dist, valid=f"A tracker row '{nm.replace('the ', '')} | {call}'", idle="No tracker exists",
        slots={"icon": ["S25"], "ipad": ["S03"], "iphone": ["S24"], "play": []}[key])
for key, nm in (("icon", "the app icon"), ("ipad", "the iPad 12.9\" set")):
    row(tag=f"trk_{key}_owner", t=f"The Agent names Martin Walsh as the maker or owner of {nm} in its tracker", w=(1 if key == "icon" else 3), kind=("lookup" if key == "icon" else "interpretation"),
        why=("Leonard's message says it in one line" if key == "icon" else "Martin keeps the store art through his vacation"), fact=f"{key}.maker", span=SP_WORK, oe=OE_TR + oe("d_store"), fids=F("d_store", "leave"),
        vals="`Martin Walsh`", verify=f"The maker on the {nm} row", final="Tracker row", acc=[f"the {nm.replace('the ', '')} row names Martin Walsh as its maker or owner"], alt="Another maker fails.",
        srcs=[s_ask] if key == "icon" else [s_leave], just=("Lookup: Leonard's message says Martin has the icon." if key == "icon" else "Interpretation: Martin's vacation post hands over the ad statics only and keeps the store art."),
        ev=(f"Source: {ASKN} ('{Q_SPLIT}')." if key == "icon" else f"Source: Martin's post {LEAVE_ID} ('{Q_LEAVE}').") + f" Accept: the {nm.replace('the ', '')} row names Martin Walsh as its maker or owner.",
        dec="R5" if key == "icon" else "T21", valid=f"A tracker row '{nm.replace('the ', '')} | Martin Walsh'", idle="No tracker exists")

# ================================================================ per-ad reasons
RECAP = {"ART-795": "#1935", "ART-805": "#1896", "ART-797": "#1966"}


def call_kind(k):
    """(weight, kind, why, sources, source text, decided by, distractor)"""
    c, nm = M.call(k), M.name(k)
    body = bodies(k)
    if k in RECAP:
        return (5, "multi-source", f"the ticket's April capture is replaced by the re-record on Android {RECAP[k]} in Marcus's Sep 25 post, which the deck's newest-capture line counts",
                [s_note, s_first(k), s_deck], f"{k} comments ({body}), Marcus's post {NOTE_ID} ('{Q_NOTE}'; a Slack search for the creative name finds it), {DECKN} ('{Q_NEW}'; '{Q_HV}')", "T9 CH9", "T3 the April capture note")
    if k in ("ART-808", "ART-816"):
        return (5, "multi-source", "Marcus's DM and the file in UA masters read as done, but Robert's reply turns the test down, and the ticket's Sep 16 re-capture on Android #1896 is current",
                [s_im, s_robert, s_first(k), s_deck], f"{k} comments ({body}), Marcus's DM {IM_ID} ('{Q_IM}'), Drive folder UA masters {MASTERS} (cheer_fastcouch_halloween files), Robert's reply {ROBERT_ID} ('{Q_ROB}'), {DECKN} ('{Q_HV}')", "T3 CH4", "T4 Marcus's DM and the test files")
    if k == "ART-809":
        return (5, "multi-source", "the capture is current, but the ticket points to Frederick's Aug 13 thread, where the master has the music baked in, and the deck re-cuts such a master first",
                [s_first(k), s_deck], f"{k} comment ({body}), Frederick's thread {MUSIC_ID} ('I can't really cut and paste different video segments as the background music is baked in.'), {DECKN} ('{Q_MUSIC}'; '{Q_RF}')", "T8 CH2", "T14 a current capture with no master note")
    if k in M.PACKS:
        return (5, "multi-source", "the ticket's Android #1529 passes the deck's build line, but Frederick's comment on the Marketing Video Refresh card says the render has the old zombies on the packs and needs a re-render",
                [s_packs, s_first(k), s_deck], f"{k} comment ({body}), Frederick's comment {PACKS_CMT} on the Marketing Video Refresh card ('{Q_PACKS}'; '{Q_PACKS2}'; a Trello search for the creative name end card 001 finds it), {DECKN} ('{Q_RF}')", "T23 CH12", "T7 Android #1529 on the ticket")
    if k in M.TRIM:
        return (5, "multi-source", "the ticket keeps iOS UK tablet, but Frederick's Sep 29 mail took this cut off it, so it runs only on Android US tablet, which his Sep 30 mail ends",
                [s_rs, s_mail, s_cm(k)], f"{k} comments ({body}), {RSN} ('{Q_RS}'; '{Q_RS2}'), {MAILN} ('{Q_TAB}'), {DECKN} ('{Q_SK}')", "T22 CH11", "T6 the ticket's campaign note")
    if k == "ART-826":
        return (3, "comparison", "the ticket's Android #852 source is older than the deck's Android #1452",
                [s_card, s_first(k), s_deck], f"{k} comment ({body}), Frederick's comment {PUSH_CMT} on the Halloween push card ('{Q_CARD}'; '{Q_CARD2}'), {DECKN} ('{Q_OLD}'; '{Q_RF}')", "T6 CH7", "T8 the sheet as the whole list")
    if k == "ART-831":
        return (3, "comparison", "the ticket's Android #1450 source is two builds older than the deck's Android #1452", [s_first(k), s_deck],
                f"{k} comments ({body}), {DECKN} ('{Q_OLD}'; '{Q_RF}')", "T6 T17 CH7", "T13 Android #1450 reads as post-swap")
    if c == "Skip":
        return (3, "comparison", f"the ticket's only campaign is Android US tablet, which Frederick's Sep 30 mail ends", [s_cm(k), s_mail],
                f"{k} comments ({body}), {MAILN} ('{Q_TAB}'), {DECKN} ('{Q_SK}')", "H4 T18", "none")
    if c == "Halloween version":
        return (3, "comparison", "the ticket's newest capture is at or after the deck's Android #1452 with a master without music", [s_first(k), s_deck],
                f"{k} comments ({body}), {DECKN} ('{Q_OLD}'; '{Q_HV}')", "H3", "none")
    b = M.source(k)
    what = (f"the ticket's Android #{b} source is older than the deck's Android #1452" if b else "the ticket's capture date is before the deck's Jul 29 swap")
    if k == "ART-840":
        what = "the ticket's Jul 28 capture is before the deck's Jul 29 swap (its Sep 11 opening is an edit, not a capture)"
    return (3, "comparison", what, [s_first(k), s_deck], f"{k} comments ({body}), {DECKN} ('{Q_OLD}'; '{Q_RF}')", "H3 CH2", "T12 the Sep 11 opening" if k == "ART-840" else "none")


# ================================================================ tracker samples
SLOT_CALL = {"ART-793": "S21", "ART-825": "S22", "ART-818": "S23", "ART-808": "S05", "ART-816": "S06", "ART-820": "S08", "ART-823": "S09", "ART-851": "S28", "ART-849": "S29",
             "ART-826": "S10", "ART-831": "S11", "ART-840": "S14", "ART-841": "S15", "ART-809": "S16", "ART-795": "S17", "ART-805": "S18", "ART-797": "S30", "ART-811": "S33",
             "ART-813": "S34", "ART-833": "S35", "ART-834": "S36"}
SLOT_DUE = {"ART-793": "S37"}
SLOT_OWNER = {"ART-825": "S31"}
for k in ("ART-793", "ART-826", "ART-831", "ART-808", "ART-811"):
    c = M.call(k)
    w, kind, why, srcs, src, dec, dist = call_kind(k)
    nm = c
    row(tag=f"trk_call_{k}", t=f"The Agent marks {tag_name(k)} as {nm} in its tracker", w=w, kind=kind, why=why, fact=f"{k}.call", span=SP_WORK, oe=OE_TR + [oe_read(k)], fids=Ft(k) + " " + F("deck"),
        vals=f"`{k}` `{c}`", verify=f"The call on the {M.name(k)} row", final="Tracker row", acc=[f"the {M.name(k)} row of the tracker carries the call {nm}"], alt="Another call on this row fails.", srcs=srcs,
        just=("Multi-source: " if w == 5 else "Comparison: ") + why + ".", ev=f"Sources: {src}. Accept: the {M.name(k)} row of the tracker carries the call {nm}.", dec=dec, dist=dist, grp="G1 tracker calls",
        valid=f"A tracker row '{M.name(k)} | {c}'", idle="No tracker exists")


def due_text(k):
    """(date, accepted earlier dates as they read in a title)"""
    return ("Oct 10, 2025", "an earlier October 2025 final date also passes") if M.due(k) == "Fri Oct 10" else ("Oct 15, 2025", "a final date from Oct 11 to Oct 14, 2025 also passes")


def due_kind(k):
    if M.due(k) == "Fri Oct 10":
        return (5, "multi-source", f"{k}'s comment puts the ad on Android US phone (Linear); Frederick's Sep 30 mail says Wed Oct 15 (Gmail), and his later reply in #zombie-match3d moves Android US phone to Fri Oct 10 (Slack)",
                [s_cm(k), s_mail, s_reply], f"{k} comment {camp_comment(k)['id']} ('{camp_comment(k)['body']}'), {MAILN} ('{Q_15}'), Frederick's reply {REPLY_ID} ('{Q_10}'; a Slack search for the campaign name Android US phone finds it)", "T20 CH8", "T1 Frederick's Sep 30 mail")
    return (3, "comparison", f"{k}'s campaigns ({camps(k)}) read against the Wed Oct 15 date in Frederick's Sep 30 mail", [s_cm(k), s_mail],
            f"{k} comment {camp_comment(k)['id']} ('{camp_comment(k)['body']}'), {MAILN} ('{Q_15}')", "T4 CH3", "T2 Frederick's Sep 12 draft")


for k in ("ART-793", "ART-852", "ART-816", "ART-826"):
    w, kind, why, srcs, src, dec, dist = due_kind(k)
    d, early = due_text(k)
    row(tag=f"trk_due_{k}", t=f"The Agent gives {tag_name(k)} a final due date of {d} in its tracker (any date form; {early})", w=w, kind=kind, why=why, fact=f"{k}.due", span=SP_WORK, oe=OE_TR + oe("d_due"),
        fids=Ft(k) + " " + F("changes", "reply", "d_due"), vals=f"`{k}` `{M.due(k)}`", verify=f"The due date on the {M.name(k)} row", final="Tracker row", acc=[f"{d} as the final due date on the {M.name(k)} row, in any date form; {early}"],
        alt="The other tier's date fails, and so does the draft's Oct 17.", srcs=srcs, just=("Multi-source: " if w == 5 else "Comparison: ") + why + ".", ev=f"Sources: {src}. Accept: {d} as the final due date on the {M.name(k)} row, in any date form; {early}.",
        dec=dec, dist=dist, grp="G2 tracker due dates", valid=f"A tracker row '{M.name(k)} | {M.due(k)}'", idle="No tracker exists", slots=[SLOT_DUE[k]] if k in SLOT_DUE else [])
row(tag="trk_due_count_30", t="The Agent gives exactly 30 ads in its tracker a final due date on or before Oct 10, 2025 (any date form)", w=5, kind="multi-source", why="the count comes from every working ad's campaigns read against Frederick's mail and reply",
    fact="tracker.due30.count", span=SP_WORK, oe=OE_TR + oe("d_due"), fids=F("d_due", "changes", "reply"), vals="`30` `Fri Oct 10`", verify="Ads with a final due date on or before Oct 10", final="Tracker due column",
    acc=["exactly 30 ad rows carry a final due date on or before Oct 10, 2025, in any date form"], alt="Every ad on one date fails; Skip rows carry no date.", srcs=[s_mail, s_reply],
    just="Multi-source: the 30 comes from the 48 working ads' campaigns (Linear) read against Frederick's mail (Gmail) and reply (Slack).",
    ev=f"Sources: the 58 running ART tickets, {MAILN} ('{Q_15}'), Frederick's reply {REPLY_ID} ('{Q_10}'). Accept: exactly 30 ad rows carry a final due date on or before Oct 10, 2025, in any date form.", dec="T20 CH8", grp="G2 tracker due dates", valid="30 ad rows on or before Oct 10", idle="No tracker exists")
row(tag="trk_due_count_18", t="placeholder trk_due_count_18", w=5, kind="multi-source", why="the count comes from every working ad's campaigns read against Frederick's mail and reply",
    fact="tracker.due18.count", span=SP_WORK, oe=OE_TR + oe("d_due"), fids=F("d_due", "changes", "reply"), vals="`18` `Wed Oct 15`", verify="Ads with a final due date from Oct 11 to Oct 15", final="Tracker due column",
    acc=["placeholder"], alt="Every ad on one date fails; Skip rows carry no date.", srcs=[s_mail, s_reply], just="placeholder", ev="placeholder", dec="T4 CH3", grp="G2 tracker due dates", valid="18 ad rows from Oct 11 to Oct 15", idle="No tracker exists")


def maker_kind(k):
    if k in M.JULIA:
        return (5, "multi-source", f"{M.name(k)} is an ad static: Leonard's ask gives the stills to Martin, and Martin's post with Leonard's later reply hands the ad statics to Julia", [s_issue(k), s_leave, s_ok],
                f"{k} title '{M.ISS[k]['title']}', {ASKN} ('{Q_SPLIT}'), Martin's post {LEAVE_ID} ('{Q_LEAVE}'), Leonard's reply {LEAVE_OK_ID} ('{Q_OK}')", "T21 CH10", "T5 Leonard's split")
    if k == "ART-832":
        return (3, "interpretation", "the ticket's description says Made by Martin Walsh, but it is an end card, which Leonard's split gives to Marcus", [s_issue(k), s_ask],
                f"{k} title '{M.ISS[k]['title']}' and description ('Made by Martin Walsh'), {ASKN} ('{Q_SPLIT}')", "T7 R5", "T15 the ticket's 'Made by Martin Walsh'")
    if k == "ART-808":
        return (3, "interpretation", "Marcus's test can't ship, so the ad needs new work from the Sep 16 capture, and it is a video, which Leonard's split gives to Marcus", [s_robert, s_ask],
                f"{k} title '{M.ISS[k]['title']}', Robert's reply {ROBERT_ID} ('{Q_ROB}'), {ASKN} ('{Q_SPLIT}')", "T3 CH4", "T4 Marcus's DM and the test files")
    if k == "ART-831":
        return (3, "interpretation", "the end card's Android #1450 source is older than the swap, so it needs new work, and Leonard's split gives end cards to Marcus", [s_first(k), s_deck, s_ask],
                f"{k} comments ({bodies(k)}), {DECKN} ('{Q_OLD}'), {ASKN} ('{Q_SPLIT}')", "T6 T17", "T13 Android #1450 reads as post-swap")
    if k == "ART-848":
        return (3, "interpretation", "the end card needs new work whichever call it gets, and Leonard's split gives end cards to Marcus", [s_issue(k), s_ask],
                f"{k} title '{M.ISS[k]['title']}', {ASKN} ('{Q_SPLIT}')", "R5", "none")
    return (3, "interpretation", "the ad needs new work and it is a video, which Leonard's split gives to Marcus", [s_issue(k), s_ask], f"{k} title '{M.ISS[k]['title']}', {ASKN} ('{Q_SPLIT}')", "R5", "none")


for k in ("ART-825", "ART-826", "ART-832", "ART-793"):
    who = M.maker(k)
    w, kind, why, srcs, src, dec, dist = maker_kind(k)
    row(tag=f"trk_owner_{k}", t=f"The Agent names {who} as the maker or owner of {tag_name(k)} in its tracker", w=w, kind=kind, why=why, fact=f"{k}.maker", span=SP_WORK, oe=OE_TR + oe("d_maker"), fids=Ft(k) + " " + F("d_maker"),
        vals=f"`{k}` `{who}`", verify=f"The maker on the {M.name(k)} row", final="Tracker row", acc=[f"the {M.name(k)} row names {who} as its maker or owner"], alt="Another maker fails.", srcs=srcs,
        just=("Multi-source: " if w == 5 else "Interpretation: ") + why + ".", ev=f"Sources: {src}. Accept: the {M.name(k)} row names {who} as its maker or owner.", dec=dec, dist=dist, grp="G3 tracker makers",
        valid=f"A tracker row '{M.name(k)} | {who}'", idle="No tracker exists", slots=[SLOT_OWNER[k]] if k in SLOT_OWNER else [])
for who, n, eml in (("Marcus Bennett", 42, "marcus.bennett@harmonygames.co"),):
    row(tag=f"trk_owner_count_{n}", t=f"The Agent names {who} as the maker or owner on exactly {n} ads in its tracker with a Halloween version or Refresh first call", w=5, kind="multi-source",
        why="the count needs every working ad and the hand-off of the ad statics", fact=f"tracker.maker{n}.count", span=SP_WORK, oe=OE_TR + oe("d_maker"), fids=F("d_maker", "leave", "leave_ok"), vals=f"`{n}` `{who}`",
        verify=f"Working ad rows naming {who}", final="Tracker maker column", acc=[f"exactly {n} ad rows with a Halloween version or Refresh first call name {who} as maker or owner; Skip rows are not counted"],
        alt="Skip rows may be blank or name a maker; they are not counted.", srcs=[s_ask, s_leave, s_ok], just=f"Multi-source: the {n} comes from the 48 working ads, Leonard's split and the hand-off of the ad statics to Julia.",
        ev=f"Sources: the 58 running ART tickets, {ASKN} ('{Q_SPLIT}'), Martin's post {LEAVE_ID} ('{Q_LEAVE}'), Leonard's reply {LEAVE_OK_ID} ('{Q_OK}'). Accept: exactly {n} ad rows with a Halloween version or Refresh first call name {who} as maker or owner; Skip rows are not counted.",
        dec="T21 CH10", grp="G3 tracker makers", valid=f"{n} working ad rows naming {who}", idle="No tracker exists")

# ================================================================ D3 shares
PEOPLE = (("Leonard Hayes", "leonard.hayes@harmonygames.co"), ("Frederick Stone", "frederick.stone@harmonygames.co"), ("Martin Walsh", "martin.walsh@harmonygames.co"),
          ("Marcus Bennett", "marcus.bennett@harmonygames.co"), ("Robert", "robert@harmonygames.co"), ("Arthur Blake", "arthur.blake@harmonygames.co"))
for art, key in (("plan doc", "w_doc"), ("tracker", "w_sheet")):
    for who, eml in PEOPLE:
        row(tag=f"share_{key}_{eml.split('@')[0]}", t=f"The Agent shares its {art} with {who} ({eml}) with commenter or writer access", w=1, kind="lookup", why="the address is on the review invite", fact=f"share.{key}.{eml.split('@')[0]}", span=SP_SHARE,
            oe=oe(f"w_share_{key}_{eml}", "review"), fids=F("review"), vals=f"`{eml}`", verify=f"{who}'s access to the {art}", final="Drive permission on the file", acc=[f"a share of the {art} to {eml} as commenter or writer"],
            alt="Reader access fails 'so they can comment'. This row looks only at this person; the two exact-six rows carry the scope.", srcs=[s_review], just=f"Lookup: {who} is on the review invite.",
            ev=f"Source: calendar event 'ZM3D Halloween review' {EVENT} (attendee {eml}). Accept: a share of the {art} to {eml} as commenter or writer.", dec="R8", valid=f"A share to {eml} as commenter", idle=f"No share of the {art} is made")

for art, key in (("plan doc", "w_doc"), ("tracker", "w_sheet")):
    row(tag=f"share_scope_{key}", t=f"The Agent shares its {art} with exactly 6 people, the other attendees of the ZM3D Halloween review", w=1, kind="lookup", why="the set is the attendee list on the review invite", fact=f"share.{key}.scope", span=SP_SHARE,
        oe=[f"OE {LBL['w_share_' + key + '_leonard.hayes@harmonygames.co']}", f"OE {LBL['w_share_' + key + '_arthur.blake@harmonygames.co']}", "OE 2"], fids=F("review"), vals="`6`", verify=f"People the {art} is shared with", final="Drive permissions on the file",
        acc=[f"the {art} is shared with exactly the 6 people on the review invite other than Claire"], alt="Sharing the file with someone off the invite, or with the whole domain, goes past 'everyone on the review'.", srcs=[s_review],
        just="Lookup: the review invite lists Claire and six others.", ev=f"Source: calendar event 'ZM3D Halloween review' {EVENT} (attendees besides Claire: leonard.hayes@harmonygames.co, frederick.stone@harmonygames.co, martin.walsh@harmonygames.co, marcus.bennett@harmonygames.co, robert@harmonygames.co, arthur.blake@harmonygames.co). Accept: the {art} is shared with exactly the 6 people on the review invite other than Claire.",
        dec="R8", valid=f"Six shares of the {art}, one per attendee", idle=f"No share of the {art} is made")

# ================================================================ D4 ticket comments
row(tag="cmt_count", t="The Agent posts its Halloween comments on exactly 58 ART tickets, all of them in ART-793 to ART-835 and ART-840 to ART-854", w=5, kind="multi-source", why="the set comes from the sheet, the ticket list and the Archive tab", fact="comments.scope", span=SP_CMT,
    oe=oe("library", "archive") + [f"OE {LBL['w_c_ART-793']}", f"OE {LBL['w_c_ART-854']}"], fids=F("library", "unity", "archive"), vals="`58`", verify="Number of ART tickets with a new comment", final="New comments on ART tickets",
    acc=["new Halloween comments on exactly the 58 tickets ART-793 to ART-835 and ART-840 to ART-854; a second comment on one of them does not add a ticket"], alt="56 tickets (the sheet alone) or 62 (with the four Archive tickets) fails.", srcs=[s_sheet],
    just="Multi-source: 56 tickets from the Unity tab plus ART-826 and ART-831, which are off the sheet, with ART-836 to ART-839 on the Archive tab left out.",
    ev=f"Sources: live creatives sheet {SHEET} (Unity 56, Archive ART-836 to ART-839), the ART team's ticket list (ART-793 to ART-854), Frederick's comment {PUSH_CMT} ('{Q_CARD2}'), ART-831 comment cmt_art831_2 ('Not on the live creatives sheet yet.'). Accept: new Halloween comments on exactly the 58 tickets ART-793 to ART-835 and ART-840 to ART-854; a second comment on one of them does not add a ticket.",
    dec="T6 T14 CH7", dist="T8 the sheet as the whole list", valid="One new comment on each of the 58 running tickets", idle="No comment is posted")
for k in M.ADS:
    c = M.call(k)
    w, kind, why, srcs, src, dec, dist = call_kind(k)
    nm = c
    fids = Ft(k) + " " + F("deck") + {"Skip": " " + F("changes"), "Refresh first": "", "Halloween version": ""}[c]
    if k in RECAP:
        fids += " " + F("note")
    if k in ("ART-808", "ART-816"):
        fids += " " + F("robert")
    if k in M.PACKS:
        fids += " " + F("packs")
    if k in M.TRIM:
        fids += " " + F("restart")
    if k == "ART-809":
        fids += " " + F("music")
    if k == "ART-826":
        fids += " " + F("card")
    head = "Multi-source" if w == 5 else "Comparison"
    row(tag=f"cmt_call_{k}", t=f"The Agent comments on {tag_name(k)} that its Halloween call is {nm} (in any wording with that meaning)", w=w, kind=kind, why=why, fact=f"{k}.call", span=SP_CMT, oe=[f"OE {LBL['w_c_' + k]}", oe_read(k)], fids=fids, vals=f"`{k}` `{c}`",
        verify=f"The call in the comment on {k}", final=f"New comment on {k}", acc=[f"a comment on {k} that gives the call {nm}, in any wording with that meaning"], alt="Another call fails; a reason in the comment is fine.", srcs=srcs, just=f"{head}: {why}.",
        ev=f"Sources: {src}. Accept: a comment on {k} that gives the call {nm}, in any wording with that meaning.", dec=dec, dist=dist, valid=f"A comment on {k}: '{c}. {'No date.' if c == 'Skip' else 'Due ' + str(M.due(k)) + '.'}'", idle=f"No comment on {k}",
        slots=[SLOT_CALL[k]] if k in SLOT_CALL else [])
    if M.due(k):
        w2, kind2, why2, srcs2, src2, dec2, dist2 = due_kind(k)
        d, early = due_text(k)
        row(tag=f"cmt_due_{k}", t=f"The Agent comments on {tag_name(k)} that its final due date is {d} (any date form; {early})", w=w2, kind=kind2, why=why2, fact=f"{k}.due", span=SP_CMT, oe=[f"OE {LBL['w_c_' + k]}", f"OE {LBL['d_due']}"],
            fids=Ft(k) + " " + F("changes") + (" " + F("reply") if w2 == 5 else ""), vals=f"`{k}` `{M.due(k)}`", verify=f"The due date in the comment on {k}", final=f"New comment on {k}", acc=[f"a comment on {k} giving {d} as the final due date, in any date form; {early}"],
            alt="The other tier's date fails, and so does the draft's Oct 17. Setting the ticket's due-date field as well is fine, but the date must be in the comment.", srcs=srcs2, just=("Multi-source: " if w2 == 5 else "Comparison: ") + why2 + ".",
            ev=f"Sources: {src2}. Accept: a comment on {k} giving {d} as the final due date, in any date form; {early}.", dec=dec2, dist=dist2, valid=f"A comment on {k}: '{c}, due {M.due(k)}'", idle=f"No comment on {k}", slots={"ART-819": ["S38"], "ART-818": ["S39"]}.get(k, []))
for n, d, dec_ in ((30, "Fri Oct 10", "T20 CH8"), (18, "Wed Oct 15", "T4 CH3")):
    row(tag=f"cmt_due_count_{n}", t=f"placeholder cmt_due_count_{n}", w=5, kind="multi-source", why="the count guards a date on a Skip ticket", fact=f"comments.due{n}.count", span=SP_CMT, oe=[f"OE {LBL['w_c_ART-793']}", f"OE {LBL['w_c_ART-854']}", f"OE {LBL['d_due']}"],
        fids=F("d_due", "changes", "reply"), vals=f"`{n}` `{d}`", verify="Tickets whose comment carries a date in that range", final="New comments on ART tickets", acc=["placeholder"], alt="A date on a Skip ticket breaks this count or its sibling.", srcs=[s_mail, s_reply], just="placeholder", ev="placeholder", dec=dec_,
        valid=f"{n} comments with a date in that range", idle="No comment is posted")

# ================================================================ D5 assignments
ASSIGN_OE = [f"OE {LBL['w_a_ART-793']}", f"OE {LBL['w_a_ART-854']}", f"OE {LBL['d_maker']}"]
row(tag="assign_count_48", t="placeholder assign_count_48", w=5, kind="multi-source", why="the set comes only from the full call audit", fact="assign.scope", span=SP_ASSIGN, oe=ASSIGN_OE, fids=F("d_maker", "d_hv", "d_rf", "users"), vals="`48`", verify="Ad tickets the run assigns", final="Assignee writes on the ad tickets",
    acc=["placeholder"], alt="All 58 ads, a Skip ad or a working ad left unassigned fails.", srcs=[s_mail, s_deck], just="placeholder", ev="placeholder", dec="H3 H4", grp="G4 assignments", valid="48 assignee writes on those tickets", idle="No ticket is assigned")
row(tag="assign_julia_6", t="placeholder assign_julia_6", w=5, kind="multi-source", why="the six come from the working statics and the hand-off to Julia", fact="assign.julia", span=SP_ASSIGN, oe=ASSIGN_OE, fids=F("d_maker", "leave", "leave_ok", "users"), vals="`6` `julia.lawson@harmonygames.co`", verify="Tickets assigned to Julia Lawson", final="Assignee writes on the ad tickets",
    acc=["placeholder"], alt="The statics given to Martin or Marcus fail.", srcs=[s_ask, s_leave, s_ok], just="placeholder", ev="placeholder", dec="T21 CH10", grp="G4 assignments", valid="Six assignee writes naming Julia Lawson", idle="No ticket is assigned", slots=["S32"])
row(tag="assign_marcus_42", t="placeholder assign_marcus_42", w=5, kind="multi-source", why="the 42 come from the working ads and Leonard's split", fact="assign.marcus", span=SP_ASSIGN, oe=ASSIGN_OE, fids=F("d_maker", "d_hv", "d_rf", "users"), vals="`42` `marcus.bennett@harmonygames.co`", verify="Tickets assigned to Marcus Bennett", final="Assignee writes on the ad tickets",
    acc=["placeholder"], alt="marcus.lee@harmonygames.co is a different person.", srcs=[s_ask, s_leave, s_ok], just="placeholder", ev="placeholder", dec="H3 H4", grp="G4 assignments", valid="42 assignee writes naming Marcus Bennett", idle="No ticket is assigned")
for k in ["ART-826", "ART-808", "ART-832", "ART-831", "ART-793"]:
    who = M.maker(k)
    eml = "julia.lawson@harmonygames.co" if who == "Julia Lawson" else "marcus.bennett@harmonygames.co"
    w, kind, why, srcs, src, dec, dist = maker_kind(k)
    row(tag=f"assign_{k}", t=f"The Agent assigns {tag_name(k)} to {who} ({eml})", w=w, kind=kind, why=why, fact=f"{k}.maker", span=SP_ASSIGN, oe=[f"OE {LBL['w_a_' + k]}", f"OE {LBL['d_maker']}"], fids=Ft(k) + " " + F("d_maker", "users"),
        vals=f"`{k}` `{eml}`", verify=f"The assignee of {k}", final=f"Assignee on {k}", acc=[f"{k} has {eml} as assignee after the run"], alt="Another assignee fails; marcus.lee@harmonygames.co is a different person.", srcs=srcs,
        just=("Multi-source: " if w == 5 else "Interpretation: ") + why + ".", ev=f"Sources: {src}. Accept: {k} has {eml} as assignee after the run.", dec=dec, dist=dist, grp="G4 assignments",
        valid=f"{k} assigned to {eml}", idle=f"{k} is not assigned", slots=[])

# ================================================================ D6 new tickets
row(tag="tk_icon", t="The Agent opens a new ART ticket for the Halloween app icon (its own ticket, or one ticket naming both the app icon and the iPad 12.9\" set)", w=5, kind="multi-source",
    why="Robert turned Martin's concept down for the icon, so the icon is new store art", fact="icon.ticket", span=SP_TICKET, oe=oe("w_t_icon", "icon"), fids=F("icon_no", "d_store", "users"), vals="`app icon`", verify="A new ART ticket for the icon", final="New issue on team ART",
    acc=["a new ART ticket whose title or description names the Halloween app icon"], alt="Assignee, due date and description are the Agent's choice.", srcs=[s_icon], just="Multi-source: the Store tab lists the app icon, Robert's reply turns Martin's concept down for it, and Leonard's rule sends store art still to be made to a ticket.",
    ev=f"Sources: {ST} (row 'app icon'), Robert's reply {ICON_NO_ID} ('{Q_ICON}'), Leonard's reply {EXPORT_OK_ID} ('{Q_NOTK}'). Accept: a new ART ticket whose title or description names the Halloween app icon.", dec="T13", dist="T10 Martin's concept", valid="A ticket titled 'Halloween app icon'", idle="No ticket is opened", slots=["S26"])
row(tag="tk_ipad", t="The Agent opens a new ART ticket for the Halloween iPad 12.9\" set (its own ticket, or one ticket naming both the app icon and the iPad 12.9\" set)", w=5, kind="multi-source",
    why="Martin's post reads as done, but the Store tab lists the iPad set and the Halloween Store folder holds no iPad file", fact="ipad.ticket", span=SP_TICKET, oe=oe("w_t_ipad", "store"), fids=F("store", "export", "d_store", "users"), vals="`iPad 12.9`", verify="A new ART ticket for the iPad set", final="New issue on team ART",
    acc=["a new ART ticket whose title or description names the Halloween iPad 12.9\" set"], alt="Assignee, due date and description are the Agent's choice.", srcs=[s_export, s_sheet, s_store], just="Multi-source: Martin's post says the store screens are exported, the Store tab lists the iPad 12.9 set, and the Halloween Store folder holds no iPad file.",
    ev=f"Sources: Martin's post {EXPORT_ID} ('{Q_EXP}'), {ST}, Drive folder Store {STORE} (11 PNG files, none named iPad), Leonard's reply {EXPORT_OK_ID} ('{Q_NOTK}'). Accept: a new ART ticket whose title or description names the Halloween iPad 12.9\" set.", dec="T1 CH1", dist="T11 Martin's 'exported'",
    valid="A ticket titled 'Halloween iPad 12.9 screenshots'", idle="No ticket is opened", slots=["S04"])
row(tag="tk_scope", t="The Agent opens its new ART tickets for store art still to be made, with none of them for the iPhone 6.5\" set or the Google Play phone set", w=5, kind="multi-source",
    why="the scope needs the Store tab, the Store folder and Leonard's rule on what is already exported", fact="tickets.scope", span=SP_TICKET, oe=oe("w_t_icon", "w_t_ipad", "export", "store"), fids=F("export_ok", "store", "d_store"), vals="`iPhone 6.5` `Google Play phone`", verify="Store surfaces with a new ticket", final="New issues on team ART",
    acc=["at least one new ART ticket for store art, and none of the new tickets is for the iPhone 6.5\" set or the Google Play phone set"], alt="A ticket for an exported set fails Leonard's rule. An Agent that opens no ticket fails too.", srcs=[s_export_ok, s_store],
    just="Multi-source: of the four store surfaces, Leonard's reply rules out tickets for what is exported, and the Store folder shows which sets are.", ev=f"Sources: Leonard's reply {EXPORT_OK_ID} ('{Q_NOTK}'), {ST}, Drive folder Store {STORE} (five iPhone65 and six GooglePlay_phone files). Accept: at least one new ART ticket for store art, and none of the new tickets is for the iPhone 6.5\" set or the Google Play phone set.",
    dec="T1 CH1", valid="Two tickets, one for the icon and one for the iPad set", idle="No ticket is opened")

# ================================================================ D7 reply
for art, key, slot in (("plan doc", "doc", ["D01"]), ("tracker", "tracker", ["D02"])):
    row(tag=f"reply_{key}", t=f"The Agent replies in Leonard's #zombie_marketing thread (message ts 1759269913.882683) with the link to its {art}", w=1, kind="lookup", why="the prompt names the thread and the link", fact=f"reply.{key}", span=SP_REPLY, oe=oe("w_reply"), fids=F("ask"),
        vals="`1759269913.882683`", verify=f"The {art} link in the thread reply", final="Thread reply under Leonard's message", acc=[f"a reply under {ASK_ID} holding a link to the {art} the Agent made"], alt="A new top-level post is not a reply in the thread. Extra links, including the new tickets, are fine.", srcs=[s_ask],
        just="Lookup: the prompt names the thread and asks for both links; the run happens before the Oct 2 review.", ev=f"Source: {ASKN} in #zombie_marketing. Accept: a reply under {ASK_ID} holding a link to the {art} the Agent made.", dec="R12", valid=f"A thread reply with the {art} URL", idle="No reply is posted", slots=slot)

# ---- /rubric round 1: fix-checked text, copied word for word from the evaluator's candidate -------------------------
# Kept out of the candidate on purpose: its per-ticket cut (A1, A2). Every comment keeps its own call and due-date rows, so
# candidate rows 73 to 75 (comment call counts) add nothing and are left out; rows 76 and 77 stay as the Skip-date guard.
CAND = json.load(open(HERE / "review2/rubric_candidate.json"))
BYT = {r["tag"]: r for r in R}
BYTITLE = {r["t"]: r for r in R}
MAP = {1: "doc_create", 2: "doc_icon_call", 3: "doc_ipad_call", 6: "doc_count_refresh", 7: "doc_count_halloween", 8: "doc_count_skip", 9: "doc_due10", 10: "doc_due15", 11: "doc_icon_due",
       13: "doc_ipad_due", 18: "doc_martin_icon", 19: "doc_martin_ipad", 20: "doc_icon_build", 21: "trk_create", 22: "trk_rows", 25: "trk_count_refresh", 38: "trk_due_ART-852", 39: "trk_due_ART-816",
       42: "trk_due_count_18", 44: "trk_owner_ART-826", 60: "share_scope_w_doc", 61: "share_scope_w_sheet", 62: "cmt_count", 64: "cmt_call_ART-794", 65: "cmt_call_ART-795", 66: "cmt_call_ART-809",
       67: "cmt_call_ART-813", 71: "cmt_call_ART-833", 76: "cmt_due_count_30", 77: "cmt_due_count_18", 78: "assign_count_48", 79: "assign_julia_6", 80: "assign_marcus_42", 86: "tk_icon", 87: "tk_ipad", 88: "tk_scope"}
for i, c in enumerate(CAND, 1):
    if i in (73, 74, 75):
        continue
    r = BYT[MAP[i]] if i in MAP else BYTITLE[c["title"]]
    r.update(t=c["title"], w=c["weight"], just=c["justification"], ev=c["evidence"])
    r["kind"] = c["justification"].split(":", 1)[0].lower()
    r["why"] = c["justification"].split(": ", 1)[1].rstrip(".")
    r["acc"] = [c["evidence"].split("Accept: ", 1)[1].rstrip(".")]
    r["cand"] = i
# first names: Leonard's message and most runs write Marcus, Julia and Martin alone (an accepted form goes in the title)
FIRST = (("Julia Lawson", "Julia"), ("Marcus Bennett", "Marcus"), ("Martin Walsh", "Martin"))
for tag in ("doc_julia", "doc_marcus_video", "doc_marcus_endcards", "doc_martin_icon", "doc_martin_ipad", "trk_icon_owner", "trk_ipad_owner", "trk_owner_ART-825", "trk_owner_ART-826", "trk_owner_ART-832", "trk_owner_ART-793", "trk_owner_count_42"):
    r = BYT[tag]
    for full, first in FIRST:
        new = f"{full} (or {first})"
        r["t"] = r["t"].replace(full, new)
        head, _, tail = r["ev"].partition("Accept: ")
        r["ev"] = head + "Accept: " + tail.replace(full, new)
    r["acc"] = [r["ev"].split("Accept: ", 1)[1].rstrip(".")]
assert not any("placeholder" in (r["t"] + r["just"] + r["ev"]) for r in R)

# ---- /rubric round 2: its 12 changed rows, copied word for word; the candidate keeps this rubric's numbering ------------
CAND2 = json.load(open(HERE / "review3/rubric_candidate.json"))
assert len(CAND2) == len(R)
ROUND2 = []
for i, (r, c) in enumerate(zip(R, CAND2), 1):
    if (r["t"], r["w"], r["just"], r["ev"]) != (c["title"], c["weight"], c["justification"], c["evidence"]):
        ROUND2.append(i)
        r.update(t=c["title"], w=c["weight"], just=c["justification"], ev=c["evidence"])
        r["kind"] = c["justification"].split(":", 1)[0].lower()
        r["why"] = c["justification"].split(": ", 1)[1].rstrip(".")
        r["acc"] = [c["evidence"].split("Accept: ", 1)[1].rstrip(".")]
assert ROUND2 == [42, 47, 170, 171, 172, 173, 174, 175, 176, 177, 178, 181], ROUND2

# ---- /rubric round 3 ---------------------------------------------------------------------------------------------------
# Copied from its candidate: the Accept fixes on the tracker counts and the Marcus count. Not copied, on purpose: rows that pair
# "exactly" with named tickets or people. Every count is now bare and each member has its own row, the form common_errors 7.8
# gives ("closes exactly three of the leftover reviews ... With a row for each review that must close"). Assignments are
# separate writes, so they get one row each, as the comments do (run 2's ruling on A1 and A2).
CAND3 = json.load(open(HERE / "review4/rubric_candidate.json"))


def take(tag, i):
    r, c = BYT[tag], CAND3[i - 1]
    r.update(t=c["title"], w=c["weight"], just=c["justification"], ev=c["evidence"])
    r["acc"] = [c["evidence"].split("Accept: ", 1)[1].rstrip(".")]


for tag, i in (("trk_count_halloween", 23), ("trk_count_skip", 24), ("trk_due_count_30", 41), ("trk_owner_count_42", 46)):
    take(tag, i)
BYT["trk_owner_count_42"]["t"] = CAND3[45]["title"]


def bare(tag, title, just, ev_head, accept, **kw):
    r = BYT[tag]
    r.update(t=title, just=just, ev=f"{ev_head}Accept: {accept}.", acc=[accept], **kw)
    r["kind"] = just.split(":", 1)[0].lower()
    r["why"] = just.split(": ", 1)[1].rstrip(".")


HEAD_C = CAND3[167]["evidence"].split("Accept: ", 1)[0]
HEAD_A = CAND3[168]["evidence"].split("Accept: ", 1)[0]
J48 = "Multi-source: the 48 is the 58 running ads less the 10 Skip ads, which needs every ticket's campaigns read against Frederick's mails."
BYT["cmt_due_count_30"]["tag"] = "cmt_due_count_48"
BYT["cmt_due_count_48"] = BYT["cmt_due_count_30"]
bare("cmt_due_count_48", "The Agent comments a final due date on exactly 48 of the tickets ART-793 to ART-854 (any date form)", J48 + " A final due date on a Skip ticket adds to this count.", HEAD_C,
     "exactly 48 of the tickets ART-793 to ART-854 carry a comment with a final due date, in any date form; a comment on a new store ticket is not counted, and a Skip comment that mentions when a campaign ends gives no due date",
     fact="comments.due.count", vals="`48`", verify="Tickets whose comment carries a final due date", alt="A final due date on a Skip ticket makes 49. Each of the 48 has its own date row, so this row only guards the extra target.")
bare("assign_count_48", "The Agent sets an assignee on exactly 48 of the tickets ART-793 to ART-854", J48, HEAD_A,
     "after the Agent's last assignee write on each ticket, exactly 48 of the tickets ART-793 to ART-854 have an assignee; an assignee on a new store ticket is not counted",
     grp="none", alt="A Skip or Archive ticket assigned makes 49. Each of the 48 has its own assignee row, so this row only guards the extra target.")
for key, art in (("w_doc", "plan doc"), ("w_sheet", "tracker")):
    head = BYT[f"share_scope_{key}"]["ev"].split("Accept: ", 1)[0]
    bare(f"share_scope_{key}", f"The Agent shares its {art} with exactly 6 people (Claire, the owner, is not counted)", BYT[f"share_scope_{key}"]["just"], head,
         f"the {art} is shared with exactly 6 people besides Claire; a domain-wide or anyone-with-the-link share goes past the 6",
         alt="Each of the six has their own share row, so this row only guards an extra share.")
head = BYT["tk_scope"]["ev"].split("Accept: ", 1)[0]
bare("tk_scope", "The Agent opens new ART store-art tickets that cover exactly 2 of the 4 store surfaces (in any number of tickets)", BYT["tk_scope"]["just"], head,
     "the new ART tickets for store art, however many, cover exactly 2 of the 4 store surfaces on the live creatives sheet", vals="`2`",
     alt="A ticket for an exported set makes 3. The icon and the iPad set each have their own ticket row, so this row only guards the extra target.")

KEEP_ASSIGN = {r["tag"]: r for r in R if r["tag"].startswith("assign_ART")}
DROP = {"trk_count_refresh", "trk_due_count_18", "cmt_due_count_18", "assign_julia_6", "assign_marcus_42"}
pos = [r["tag"] for r in R].index("assign_count_48")
n0 = len(R)
for k in M.ADS:
    if M.call(k) == "Skip" or f"assign_{k}" in KEEP_ASSIGN:
        continue
    who = M.maker(k)
    eml = "julia.lawson@harmonygames.co" if who == "Julia Lawson" else "marcus.bennett@harmonygames.co"
    made = re.search(r"Made by ([^.]+)\.", M.ISS[k]["description"]).group(1)
    part = "end card" if M.kind(k).endswith("card") else "video"
    if who == "Julia Lawson":
        w, kind, why, srcs, src, dec, dist = maker_kind(k)
    elif made == "Marcus Bennett":
        w, kind, why, srcs, dec, dist = 1, "lookup", "the ticket says Made by Marcus Bennett and Leonard's line agrees", [s_issue(k), s_ask], "R5", "none"
        src = f"{k} title '{M.ISS[k]['title']}' and description ('Made by Marcus Bennett'), {ASKN} ('{Q_SPLIT}')"
    else:
        w, kind, srcs, dec, dist = 3, "interpretation", [s_issue(k), s_ask], "R5", "none"
        why = f"the ticket says Made by {made}, and it is a {part}, which Leonard's split gives to Marcus"
        src = f"{k} title '{M.ISS[k]['title']}' and description ('Made by {made}'), {ASKN} ('{Q_SPLIT}')"
    head = {"lookup": "Lookup", "interpretation": "Interpretation", "multi-source": "Multi-source"}[kind]
    acc = f"an assignee write on {k} setting {eml}, by address, name or user id"
    row(tag=f"assign_{k}", t=f"The Agent assigns {tag_name(k)} to {who} ({eml})", w=w, kind=kind, why=why, fact=f"{k}.maker", span=SP_ASSIGN, oe=[f"OE {LBL['w_a_' + k]}", f"OE {LBL['d_maker']}"], fids=Ft(k) + " " + F("d_maker", "users"),
        vals=f"`{k}` `{eml}`", verify=f"The assignee of {k}", final=f"Assignee on {k}", acc=[acc], alt="Another assignee fails; marcus.lee@harmonygames.co is a different person.", srcs=srcs, just=f"{head}: {why}.", ev=f"Sources: {src}. Accept: {acc}.",
        dec=dec, dist=dist, valid=f"{k} assigned to {eml}", idle=f"{k} is not assigned", slots=(["S32"] if k == "ART-827" else []))
new = R[n0:]
del R[n0:]
for r in KEEP_ASSIGN.values():
    r["grp"] = "none"
ordered = sorted(new + list(KEEP_ASSIGN.values()), key=lambda r: r["tag"])
R[:] = [r for r in R[:pos + 1] if r["tag"] not in DROP] + ordered + [r for r in R[pos + 1:] if r["tag"] not in DROP and not r["tag"].startswith("assign_ART")]

# ---- /rubric round 4: its 6 changed rows, copied word for word; the candidate keeps this rubric's numbering ---------------
CAND4 = json.load(open(HERE / "review5/rubric_candidate.json"))
assert len(CAND4) == len(R)
ROUND4 = []
for i, (r, c) in enumerate(zip(R, CAND4), 1):
    if (r["t"], r["w"], r["just"], r["ev"]) != (c["title"], c["weight"], c["justification"], c["evidence"]):
        ROUND4.append(i)
        r.update(t=c["title"], w=c["weight"], just=c["justification"], ev=c["evidence"])
        r["kind"] = c["justification"].split(":", 1)[0].lower()
        r["why"] = c["justification"].split(": ", 1)[1].rstrip(".")
        r["acc"] = [c["evidence"].split("Accept: ", 1)[1].rstrip(".")]
assert ROUND4 == [58, 59, 167, 168, 189, 219], ROUND4
BY4 = {r["tag"]: r for r in R}
BY4["assign_ART-816"].update(srcs=[s_issue("ART-816"), s_robert], fids=BY4["assign_ART-816"]["fids"] + " " + F("robert"), dec="T3 CH4")
for tag, what in (("cmt_due_count_48", "A due date on a Skip or Archive ticket"), ("assign_count_48", "An assignee on a Skip or Archive ticket")):
    BY4[tag].update(vals="`14`", alt=f"{what} fails. Naming only what is out of scope keeps required members out of this row, and each of the 48 has its own row.")
BY4["tk_scope"].update(vals="`iPhone 6.5` `Google Play phone`", alt="A ticket for an exported set fails Leonard's rule. The icon and the iPad set each have their own ticket row.")

# ---- /rubric round 5: its one changed row, copied word for word ------------------------------------------------------------
CAND5 = json.load(open(HERE / "review6/rubric_candidate.json"))
assert len(CAND5) == len(R)
ROUND5 = []
for i, (r, c) in enumerate(zip(R, CAND5), 1):
    if (r["t"], r["w"], r["just"], r["ev"]) != (c["title"], c["weight"], c["justification"], c["evidence"]):
        ROUND5.append(i)
        r.update(t=c["title"], w=c["weight"], just=c["justification"], ev=c["evidence"])
        r["kind"] = c["justification"].split(":", 1)[0].lower()
        r["why"] = c["justification"].split(": ", 1)[1].rstrip(".")
        r["acc"] = [c["evidence"].split("Accept: ", 1)[1].rstrip(".")]
assert ROUND5 == [167], ROUND5
CAND6 = json.load(open(HERE / "review7/rubric_candidate.json"))
assert len(CAND6) == len(R)
ROUND6 = []
for i, (r, c) in enumerate(zip(R, CAND6), 1):
    if (r["t"], r["w"], r["just"], r["ev"]) != (c["title"], c["weight"], c["justification"], c["evidence"]):
        ROUND6.append(i)
        r.update(t=c["title"], w=c["weight"], just=c["justification"], ev=c["evidence"])
        r["acc"] = [c["evidence"].split("Accept: ", 1)[1].rstrip(".")]
assert ROUND6 == [60], ROUND6
BY4["cmt_due_count_48"].update(vals="`10`", alt="A due date left standing on a Skip ticket fails. A date on an Archive ticket is the comment scope row's error, not this row's. Each of the 48 has its own row.")

# ---- platform /rubric round 1 (FULL, FAIL 2): its Fix List, every line marked checked, copied word for word ---------------
# The platform's reading replaces the local runs on the guard rows: a bare count is the guard, an exclusion-only row is an
# idle-passes negative, and a share count has no decoy behind it. Supporting text changes only where a new title makes it wrong.
BP = {r["tag"]: r for r in R}


def plat(tag, title=None, weight=None, accept=None, just=None, **kw):
    r = BP[tag]
    if title:
        r["t"] = title
    if weight:
        r["w"] = weight
    if accept:
        r["ev"] = r["ev"].split("Accept: ", 1)[0] + "Accept: " + accept + "."
        r["acc"] = [accept]
    if just:
        r["just"] = just
        r["kind"] = just.split(":", 1)[0].lower()
        r["why"] = just.split(": ", 1)[1].rstrip(".")
    r.update(kw)


plat("doc_due10", weight=5, just="Multi-source: Frederick's Sep 30 mail (Gmail) says Wed Oct 15, his later reply in #zombie-match3d (Slack) moves Android US phone to Fri Oct 10, and each ad's campaigns (Linear) say which ads that reaches.")
BP["doc_due10"]["ev"] = BP["doc_due10"]["ev"].replace("Sources: Frederick's mail", "Sources: the 58 running ART tickets, Frederick's mail", 1)
assert BP["doc_due10"]["ev"].startswith("Sources: the 58 running ART tickets, Frederick's mail")
plat("doc_julia", title="The Agent names Julia Lawson (or Julia) in its plan doc as the maker or owner of the Halloween work on the ad statics",
     accept="the plan doc names Julia Lawson (or Julia) as the maker or owner of the Halloween work on the ad statics")
plat("trk_rows", title="The Agent lists exactly 58 ads with a Halloween call in its tracker (on one tab or several)", accept="the tracker gives a Halloween call to exactly 58 ads, on one tab or several; an ad on several tabs counts once",
     alt="56 ads (the sheet alone) or 60 (with the Archive tab) fails. A count of ads, not of rows.")
for k, nm in (("ART-825", "julia 1:1"), ("ART-826", "julia 4:5")):
    plat(f"trk_owner_{k}", title=f"The Agent names Julia Lawson (or Julia) as the maker or owner of the Halloween work on {k} ({nm}) in its tracker",
         accept=f"the {nm} row names Julia Lawson (or Julia) as the maker or owner of its Halloween work")
plat("cmt_count", title="The Agent posts comments carrying a Halloween call on exactly 58 existing ART tickets", accept="count ART tickets that existed before the run, whichever they are; a second comment on one ticket adds nothing",
     alt="56 (the sheet alone) or 62 (with the Archive tickets) fails. Each ticket's call has its own row.")
plat("assign_count_48", title="The Agent sets an assignee on exactly 48 existing ART tickets", accept="counted whichever tickets they are; a new store ticket isn't counted",
     just="Multi-source: the 48 is the 58 running ads less the 10 Skip ads, which needs every ticket's campaigns read against Frederick's mails.", vals="`48`",
     alt="Assigning all 58 ads, or a Skip or Archive ticket on top of the 48, fails the count. Each of the 48 has its own assignee row.")
plat("tk_ipad", title='The Agent opens a new ART ticket to make the Halloween iPad 12.9" set', accept='a new ART ticket to make the Halloween iPad 12.9" set')
plat("tk_scope", title="The Agent opens new ART tickets for exactly two store surfaces in total (in any number of tickets)", accept="count each surface the new tickets cover once, whichever they are", vals="`2`",
     alt="A ticket for an exported set makes three. One combined ticket, or a set split across several, still counts two.")
for k in ("ART-814", "ART-815", "ART-817", "ART-818", "ART-819", "ART-823", "ART-833", "ART-834", "ART-835", "ART-845", "ART-846", "ART-848"):
    part = "end cards" if M.kind(k).endswith("card") else "video"
    plat(f"assign_{k}", weight=3, just=f"Interpretation: the ticket says Made by Marcus Bennett, but assigning it also needs the check that the ad needs new work, and Leonard's split gives {part} to Marcus.")
for r in R:
    if r["tag"].startswith("share_w_"):
        r["alt"] = "Reader access fails 'so they can comment'. This row looks only at this person; sharing with anyone else as well is allowed."
DELETED = {"trk_owner_count_42", "share_scope_w_doc", "share_scope_w_sheet", "cmt_due_count_48"}
assert DELETED <= set(BP)
R[:] = [r for r in R if r["tag"] not in DELETED]

# ---- checks ----------------------------------------------------------------------------------------------------
BAD = re.compile(r"[—–]|\.sql\b|\.json\b|\.md\b|Working_Files|task_inputs|solver|truth\.|/Users/|SQL L\d+|\bsuch as\b|\be\.g\.|for example", re.I)
for r in R:
    for f in ("t", "just", "ev"):
        m = BAD.search(r[f])
        assert not m, (r["tag"], f, m.group(0), r[f][:160])
    assert r["t"].startswith("The Agent "), r["t"]
tags = [r["tag"] for r in R]
assert len(tags) == len(set(tags))
from collections import Counter
dup = [k for k, v in Counter(r["fact"] for r in R).items() if v >= 3]
assert not dup, dup
titles = Counter(r["t"] for r in R)
assert max(titles.values()) == 1

# ---- outputs ---------------------------------------------------------------------------------------------------
rubric = [{"title": r["t"], "category": r.get("cat", "Outcome"), "weight": r["w"], "justification": r["just"], "evidence": r["ev"]} for r in R]
(TI / "09_Rubrics.json").write_text(json.dumps(rubric, indent=1, ensure_ascii=False) + "\n")


def ahash(p):
    return subprocess.run([sys.executable, str(WS / "Task_Authoring/tools/stage_gate.py"), "--artifact-hash", str(p)], capture_output=True, text=True, cwd=WS).stdout.strip()


ev_path = WF / "00_V3_Authoring_Evidence.json"
ev = json.loads(ev_path.read_text())
ev["rubric_hash"] = ahash(TI / "09_Rubrics.json")
ev["prompt_hash"] = ahash(TI / "04_Prompt.txt")
ev["rubric_rows"] = [{"criterion_id": f"C{i + 1}", "fact_id": r["fact"], "prompt_span": r["span"], "accepted_outcomes": r["acc"], "alternatives_review": r["alt"], "source_records": r["srcs"]} for i, r in enumerate(R)]
ev_path.write_text(json.dumps(ev, indent=1, ensure_ascii=False) + "\n")
json.dump([{k: v for k, v in r.items() if k != "srcs"} for r in R], open(HERE / "rows.json", "w"), indent=1, ensure_ascii=False)
tw = sum(r["w"] for r in R)
print(len(R), "rows; weight", tw, "; bands", {b: sum(1 for r in R if r["w"] == b) for b in (5, 3, 1)}, "; hash", ev["rubric_hash"])
grp = Counter()
for r in R:
    grp[r["tag"].split("_")[0]] += r["w"]
print({k: (v, round(100 * v / tw, 1)) for k, v in grp.items()})
