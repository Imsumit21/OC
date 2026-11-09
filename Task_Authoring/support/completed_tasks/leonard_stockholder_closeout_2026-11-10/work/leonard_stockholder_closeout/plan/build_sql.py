#!/usr/bin/env python3
"""Builds task_inputs/01_Universe_Inject.sql for Leonard's stockholder close-out (normal universe, Feb 14, 2026).

Ids and constants come from plan/build_scenario.py (importing it re-writes the same draft and surface); per-holder comment
facts come from plan/holder_facts.json. Never executes SQL. Writes the SQL and plan/sql_ids.json."""
import base64, contextlib, datetime as D, email.utils, hashlib, io, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import build_scenario as B
SALT = "hg-leonard-closeout|"
LEO, ROB, ART = B.MB, "robert@harmonygames.co", "arthur.blake@harmonygames.co"
NAMES = {LEO: "leonard hayes", ROB: "robert", ART: "arthur blake"}
SLACK_U = {LEO: "EMPLOYEE_0038_SLACK_ID", ROB: "EMPLOYEE_0016_SLACK_ID", ART: "EMPLOYEE_0025_SLACK_ID"}
LIN = {LEO: "usr_63fffeb4fab5233e", ROB: "usr_Robert", ART: "usr_cc3e90160f490686"}
ROOT = "d_63fffeb4fab5233ed5bb73"
BOARD = {"id": "640643a3fd8f3ca308d9318e", "name": "Harmony Games", "shortLink": "f4LGcmuh"}
TODO_LIST = ("640643a3fd8f3ca308d93195", "To Do")
TR_LEO = "PERSON_6094_TRELLO_USER_ID"
KPMG_ID = "<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@LV3PR19MB8524.namprd19.prod.outlook.com>"
ACK_ID = "<CAPBs_a7Tq2LmV9xYcR4KdN8wUe3HsJ6oFbZ1gPiA5tGyQnE0Xw@mail.gmail.com>"
SUNSET_ID = "<mlkq74xd.3f9e2c1a-6b48-4d07-a1e5-8c2f0d7b6a94@we.are.superhuman.com>"
ROBERT_ID = "<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com>"
ROBERT_PARENT = "<CAGkro_Ox2wP8TQrYO9J2+FkfLbZqy_NixtRjOS7wcBeB3pFZtA@mail.gmail.com>"
LABEL_IN = ["INBOX", "IMPORTANT", "Label_b19fb8d1b3", "CATEGORY_PERSONAL"]
LABEL_SENT = ["SENT", "Label_b19fb8d1b3"]

T = {"folder": "2026-02-12T23:20:37Z", "project": "2026-02-12T23:24:12Z", "project_upd": "2026-02-13T18:21:46Z",
     "issue0": "2026-02-12T23:25:03Z", "last0": "2026-02-12T23:34:21Z", "fig0": "2026-02-12T23:43:08Z",
     "notes": "2026-02-13T01:05:41Z", "old": "2026-02-10T17:41:09Z", "sheet": "2026-02-10T18:12:26Z", "deck": "2026-02-10T18:33:52Z",
     "kpmg": "2026-02-13T16:48:33Z", "ack": "2026-02-13T17:12:40Z", "follow": "2026-02-13T17:37:15Z", "sunset": "2026-02-13T18:06:21Z", "sunset_ack": "2026-02-13T18:19:02Z", "robert": "2026-02-12T23:41:12Z",
     "card": "2026-02-12T22:54:08Z", "board": "2026-02-12T22:38:16Z", "card_comment": "2026-02-13T18:14:27Z", "hold_created": "2026-02-13T01:12:18Z",
     "hold_start": "2026-02-17T17:00:00Z", "ext": "2026-02-03T16:20:44Z", "bounce": "2026-02-11T20:13:57Z", "akin": "2026-02-12T22:52:17Z"}


def hx(label, n):
    return hashlib.sha256((SALT + label).encode()).hexdigest()[:n]


def ep(iso):
    return D.datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp()


def iso_of(t):
    return D.datetime.fromtimestamp(t, D.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def plus(iso, sec):
    return iso_of(ep(iso) + sec)


def q(v):
    if v is None:
        return "NULL"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return repr(v)
    s = str(v)
    if "\n" in s or "\\" in s or "\r" in s:
        return "E'" + s.replace("\\", "\\\\").replace("'", "''").replace("\r", "\\r").replace("\n", "\\n") + "'"
    return "'" + s.replace("'", "''") + "'"


def js(x):
    return json.dumps(x, ensure_ascii=False)


OUT, ROWS = {}, {}


def ins(table, cols, vals, key):
    OUT.setdefault(table.split(".")[0], []).append(f"INSERT INTO {table} ({', '.join(cols)})\nVALUES ({', '.join(q(v) for v in vals)});")
    ROWS.setdefault(table, []).append(key)


def upd(table, sets, key_col, key):
    s = ", ".join(f"{c} = {q(v)}" for c, v in sets.items())
    OUT.setdefault(table.split(".")[0], []).append(f"UPDATE {table} SET {s} WHERE {key_col} = {q(key)};")
    ROWS.setdefault(table + " (UPDATE)", []).append(key)


def slack_id(channel, ts):
    return hashlib.sha256(f"{channel}|{ts}".encode()).hexdigest()[:32]


# ======================================================================== seeded wording
NOTES_DOC = """Stockholder close-out notes

These replace my earlier outreach notes.

What needs doing
- the reach-out I promised to the investors, one by one, not one mail to everyone
- where I left things today in #winddown: the angels are what's open from my list, besides the Sunset onboarding
- the investor email on the Task List: take my draft from #winddown and bring it up to date as a letter I can send. the update outline has the sections
- the holder sheet comes first, the notes and everything else run off it. Finish my draft one in the folder rather than starting another. Share it and the letter with Robert
- notes ready for me by Tuesday, as Gmail drafts. I said I'd archive google after the 15th but that waits, we keep it until the data is extracted, so my drafts are safe until I've gone through them. I read and send each note myself
- everything goes in the close-out folder, not the Wind Down one, that one is the vendor and termination papers
- Griffin's partner gets a heads-up as a reply to all on their own Board position mail from Feb 12, asking for their vote as preferred holders on the dissolution. That one can go out once the sheet is done
- when the sheet is ready, reply under my list in #winddown and say who goes first

How each holder gets handled
- Carta is the record, over any date in the letters. If a line's last day has passed, it holds nothing.
- One row per issue on the sheet, and the counts go by rows. At most one note per person. The three of us get no row, only the totals.
- Told means a written message about the closing, sent to them directly and delivered, from one of the three of us (a post in a channel doesn't count); for a fund, its partner.
- Everyone still holding something gets what they are owed: the closing if they have not been told, their last day if they have one. Whoever's last day comes first goes first.
- Each note says what they hold.
- Anything they asked about their holding that we never answered gets answered in their note, if they get one.
- Messages go to the email on each holder's issue.

Labels for the sheet: Nothing, Already told, Closing, Last day, Closing and last day.
"""
OLD_DOC = """Holder outreach notes

Rough plan, before I forget.

- Griffin first, then everyone else
- one email to everyone on the investor list, same note for all of them, BCC like the update
- take the names and numbers from the Nov 2024 owner list
- ask Robert and Arthur to read it before it goes
"""
PROJECT_DESC = ("The holders, as I said in #winddown: one issue per holder on Carta, live or lapsed, the three of us aside. my close-out notes have how each holder "
                "gets handled, and the sheet is what Sunset asked for. I'll pass it to Sunset myself. Send KPMG's confirmation as a reply to all once the sheet is done.\n\n"
                "States once the sheet is done: Canceled where the line holds nothing; otherwise Todo where its own note is waiting for me, "
                "and Done where it isn't. On every issue with no note of its own, Canceled included, say why.")
ORIGIN = [("1770938120.410229", LEO, "Putting the holders in linear, one issue each"),
          ("1770938131.882339", LEO, "We keep it during the transition anyway and the three of us can all see it"),
          ("1770938158.104719", LEO, "They stay in Backlog until the sheet is done")]
AMEND = [("1770949310.220519", LEO, "One thing on the angels: one note to whoever has always handled it for a family covers the rest of the family's lines, which need no note of their own, and that note says what each of them holds"),
         ("1770949322.640149", LEO, "Mark those lines Covered on the sheet in place of a label, and count them that way"),
         ("1770949351.317729", LEO, "<@EMPLOYEE_0025_SLACK_ID> the sheet goes to you as well as Robert, the rest of my notes stands"),
         ("1770949437.902269", ART, "sounds good")]
KPMG_SUBJECT = "GRIFFIN GAMING PARTNERS 2025 Audit Request [SOURCE_ORG_0001], Inc."
KPMG_BODY = """Hello,

KPMG is currently engaged in the audit of GRIFFIN GAMING PARTNERS for the year ended December 31, 2025. The financial statements are covered by the Standard Metrics upload, so there is no need to send those again. For the fund's investment in [SOURCE_ORG_0001], Inc., please confirm the below as of December 31, 2025 and return directly to us via email by replying to all Recipients herein:

1. Shares outstanding by class, showing what each fund holds.
2. Each outstanding option line by holder, and their total, using each effective date as Carta shows it, regardless of when recorded.
3. Shares outstanding plus those options, as one figure.
4. Any financing or other significant event since that date.

We appreciate your response by 2/27/2026. Should you have any questions, please feel free to contact us directly.

Thank you in advance,

[PERSON_NAME_46103] (she/her/[PERSON_NAME_13208])
Audit Associate
KPMG LLP | 55 Second Street | Suite 1400 | San Francisco, CA 94105
PERSON_3088_EMAIL
kpmg.com/us

**********************************************************************
The information in this email is confidential and may be legally privileged. It is intended solely for the addressee. Access to this email by anyone else is unauthorized. If you are not the intended recipient, any disclosure, copying, distribution or any action taken or omitted to be taken in reliance on it, is prohibited and may be unlawful. When addressed to our clients any opinions or advice contained in this email are subject to the terms and conditions expressed in the governing KPMG client engagement letter.
***********************************************************************
"""
ACK_BODY = """Thanks, got it. I'll get this to you before the 27th.

Leonard

On Fri, Feb 13, 2026 at 8:48 AM PERSON_3088_NAME <PERSON_3088_EMAIL> wrote:

""" + "\n".join("> " + l if l else ">" for l in KPMG_BODY.rstrip().split("\n")) + "\n"
FOLLOW_ID = "<LV3PR19MB85246D2E9B14C7A03F5E8D12BC4A7@LV3PR19MB8524.namprd19.prod.outlook.com>"
FOLLOW_BODY = """Thank you Leonard. Two clarifications on our side. For item 2, a line terminated on or before the as-of date counts only what had vested by its termination date. For item 4, we need any new financing and whether the company is winding down.

Thank you,

[PERSON_NAME_46103] (she/her/[PERSON_NAME_13208])
Audit Associate
KPMG LLP | 55 Second Street | Suite 1400 | San Francisco, CA 94105
PERSON_3088_EMAIL
kpmg.com/us
"""
SUNSET_ACK_ID = "<CAPBs_a5Wn3RvK8yZtH2DqL7mJc9XeU4oGfB6sPiN1aTuYkEr0Q@mail.gmail.com>"
SUNSET_SUBJECT = "Sunset: stockholder info for intake"
SUNSET_BODY = """Hi Leonard,

Quick one from legal for the intake. Before they start on the stockholder side they'll need this from you, ideally in one sheet:

- One line per holder of stock or options, with what each holds today (for options, what's vested) and any last day
- Total shares and options outstanding
- A count of holders by what each still needs to hear from you
- Directors in office, and who holds the preferred vote

Formal notices are a separate step that legal will walk you through later, so your own notes to holders don't need to double as notices.

Best,
PERSON_2888_NAME
Head of Partnerships
M: [PHONE_15402]
W: www.sunsethq.com ( http://www.sunsethq.com/ )

Sent via Superhuman ( https://sprh.mn/?vip=PERSON_2888_EMAIL )
"""
ROBERT_SUBJECT = "Re: Funds Transfer Request #450904566 Has Been Scheduled"
ROBERT_BODY = """Hey [PERSON_NAME_0112],

Digging up this old thread because it's the one I had handy. Wanted you to hear this from me: we're closing the company. We ran out of runway and we've had to let the team go. Really appreciate you backing us from the very start.

Thanks
[PERSON_NAME_0054]

On Fri, Aug 11, 2023 at 1:00 PM robert <robert@harmonygames.co> wrote:

> Thanks!!!
"""
CARD_NAME = "Stockholder close-out"
CARD_DESC = "Order: holder sheet, then the notes, then the letter. Nothing goes out until the sheet is done."
CARD_COMMENT = "Sunset wants the same sheet for the intake, so nothing changes on order"
DRAFT_TITLE = "Holder list (draft)"
DRAFT_GRID = [["Holder", "Shares", "Notes"],
              ["GRIFFIN GAMING PARTNERS", "2,746,693", "copied from the Nov 2024 list"],
              ["[PERSON_NAME_0038]", "127,162", "copied from the Nov 2024 list"],
              ["[PERSON_NAME_11362]", "86,470", "copied from the Nov 2024 list"],
              ["[PERSON_NAME_0089] [PERSON_NAME_25152]", "81,383", "copied from the Nov 2024 list"],
              ["TOR Capital Limited", "50,865", "copied from the Nov 2024 list"],
              ["PERSON_3941_NAME [PERSON_NAME_0127]", "31,536", "copied from the Nov 2024 list"],
              ["PERSON_1287_NAME", "31,536", "copied from the Nov 2024 list"],
              ["", "", "the list's percentages leave out the option pool, so they only add to about 94%"]]
DECK_TITLE = "Harmony Games February 26 Update"
DECK = ["Harmony Games February 26 Update\nOutline",
        "What happened\nWhy we are closing",
        "Where things stand\nHolders, per the Nov 2024 owner list\nBoard, process, who is running the close",
        "What it means for you\nDistributions, tax papers, your options",
        "What happens to the games and the IP\nThank you"]
HOLD_SUMMARY = "Holder notes due"

# ======================================================================== Drive / Docs / Sheets / Slides
DF_COLS = ["id", "name", "mime_type", "parents_json", "owner_email", "shared_with_emails_json", "shared_roles_json",
           "visibility", "owners_json", "modified_time", "created_time", "trashed", "starred"]
DOC, SHEET, SLIDES, FOLD = ("application/vnd.google-apps.document", "application/vnd.google-apps.spreadsheet",
                            "application/vnd.google-apps.presentation", "application/vnd.google-apps.folder")


def drive(fid, name, mime, parent, created, modified):
    ins("gdrive.drive_files", DF_COLS, [fid, name, mime, js([parent]), LEO, "[]", "[]", "private", js([LEO]), modified, created, False, False], fid)


def gdoc(fid, text, parent, at, rev):
    title = text.split("\n", 1)[0]
    body = text.rstrip("\n") + "\n"
    drive(fid, title, DOC, parent, at, at)
    tl = len(title) + 1
    runs = [{"start": 0, "end": tl, "named_style": "TITLE", "list_id": None, "list_nesting": 0},
            {"start": tl, "end": len(body), "named_style": "NORMAL_TEXT", "list_id": None, "list_nesting": 0}]
    ins("gdocs.docs_documents", ["document_id", "title", "owner_email", "shared_with_emails_json", "visibility", "body_text",
                                 "style_runs_json", "revision_id", "drive_file_id", "created_time", "modified_time"],
        [fid, title, LEO, "[]", "private", body, js(runs), rev, fid, at, at], fid)
    return title


FOLDER_NAME = "Stockholder close-out"
drive(B.FOLDER, FOLDER_NAME, FOLD, ROOT, T["folder"], T["notes"])
NOTES_TITLE = gdoc(B.DOC_NOTES, NOTES_DOC, B.FOLDER, T["notes"], "3c986c6ce3")
OLD_TITLE = gdoc(B.DOC_OLD, OLD_DOC, ROOT, T["old"], "84bdd1a5ac")

drive(B.SHEET, DRAFT_TITLE, SHEET, B.FOLDER, T["sheet"], T["sheet"])
ins("gsheets.sheets_spreadsheets", ["spreadsheet_id", "title", "owner_email", "shared_with_emails_json", "visibility",
                                    "drive_file_id", "created_time", "modified_time"],
    [B.SHEET, DRAFT_TITLE, LEO, "[]", "private", B.SHEET, T["sheet"], T["sheet"]], B.SHEET)
ins("gsheets.sheets_sheets", ["spreadsheet_id", "sheet_id", "title", '"index"', "row_count", "column_count", "grid_json"],
    [B.SHEET, 0, "Sheet1", 0, 1000, 26, js(DRAFT_GRID)], f"{B.SHEET}#0")

drive(B.DECK, DECK_TITLE, SLIDES, B.FOLDER, T["deck"], T["deck"])
ins("gslides.slides_presentations", ["presentation_id", "title", "owner_email", "shared_with_emails_json", "visibility",
                                     "drive_file_id", "revision_id", "created_time", "modified_time"],
    [B.DECK, DECK_TITLE, LEO, "[]", "private", B.DECK, "0b2616045d", T["deck"], T["deck"]], B.DECK)
PAGES = ["slide_341616bedf43", "slide_659353384faa"] + ["slide_" + hx(f"deck-page-{n}", 12) for n in range(2, len(DECK))]
ELS = ["el_f71854425943", "el_3f1b82e16a82"] + ["el_" + hx(f"deck-el-{n}", 12) for n in range(2, len(DECK))]
for n, text in enumerate(DECK):
    ins("gslides.slides_pages", ["presentation_id", "object_id", '"index"', "layout", "notes"], [B.DECK, PAGES[n], n, "BLANK", None], f"{B.DECK}#{PAGES[n]}")
    ins("gslides.slides_page_elements", ["presentation_id", "page_object_id", "object_id", "kind", "text", "placeholder_type",
                                         "x_emu", "y_emu", "width_emu", "height_emu", "table_json", "ordinal"],
        [B.DECK, PAGES[n], ELS[n], "TEXT_BOX", text, None, 0, 0, 9144000, 5143500, None, 0], f"{B.DECK}#{ELS[n]}")

# ======================================================================== Slack
SL_COLS = ["id", "ts", "channel_id", "type", "user_id", "text", "thread_parent_id", "thread_ts_legacy", "reply_count",
           "reply_users_count", "latest_reply", "is_activity_message", "subtype", "reactions_json", "files_json",
           "attachments_json", "created_at", "metadata_json"]
SLACK = {}
EXEC_FIX = ("1768418331.402719", LEO, "fyi chatgpt has the other seed investors a couple of shares off in these, go by the ledger")
EXEC_PARENT = ("b658ec71107dd059e03ea425728ba3b3", "1768417784.194359")   # base: Leonard's ChatGPT cap-table paste with 305,188 for the other seed investors, #executives 2026-01 /728 (reply_count 0)
mid = slack_id("C07C2866011", EXEC_FIX[0])
ins("slack.slack_messages", SL_COLS, [mid, EXEC_FIX[0], "C07C2866011", "message", SLACK_U[LEO], EXEC_FIX[2], EXEC_PARENT[0], EXEC_PARENT[1], 0, 0, None, False, None,
                                      "[]", "[]", "[]", iso_of(float(EXEC_FIX[0])), "{}"], f"C07C2866011/{EXEC_FIX[0]}")
SLACK[f"C07C2866011/{EXEC_FIX[0]}"] = mid
upd("slack.slack_messages", {"thread_ts_legacy": EXEC_PARENT[1], "reply_count": 1, "reply_users_count": 1, "latest_reply": EXEC_FIX[0]}, "id", EXEC_PARENT[0])
LIST_ID, LIST_TS = "e3e198cc6e3f866a032d34c5f69e39f9", "1770934638.035469"      # base: Leonard's Feb 12 list, #winddown 2026-02 /197 (reply_count 0)
for ts, who, text in ORIGIN:
    mid = slack_id(B.WD, ts)
    ins("slack.slack_messages", SL_COLS, [mid, ts, B.WD, "message", SLACK_U[who], text, None, None, 0, 0, None, False, None, "[]", "[]",
                                          "[]", iso_of(float(ts)), "{}"], f"{B.WD}/{ts}")
    SLACK[f"{B.WD}/{ts}"] = mid
for ts, who, text in AMEND:
    mid = slack_id(B.WD, ts)
    ins("slack.slack_messages", SL_COLS, [mid, ts, B.WD, "message", SLACK_U[who], text, LIST_ID, LIST_TS, 0, 0, None, False, None, "[]", "[]",
                                          "[]", iso_of(float(ts)), "{}"], f"{B.WD}/{ts}")
    SLACK[f"{B.WD}/{ts}"] = mid
upd("slack.slack_messages", {"thread_ts_legacy": LIST_TS, "reply_count": len(AMEND), "reply_users_count": 2, "latest_reply": AMEND[-1][0]}, "id", LIST_ID)

# ======================================================================== Trello
TC_COLS = ["id", "name", '"idBoard"', '"idList"', '"desc"', "pos", "closed", "due", '"dueComplete"', '"idMembers_json"',
           '"idLabels_json"', '"idShort"', '"shortLink"', '"shortUrl"', "url", '"dateLastActivity"', "cover_json", "badges_json"]
TA_COLS = ["id", "type", "date", '"idMemberCreator"', '"idBoard"', '"idCard"', "data_json"]
card, short = B.TRELLO_CARD, 456
sl = base64.b64encode(hashlib.sha256((SALT + card).encode()).digest()).decode().replace("+", "x").replace("/", "Q")[:8]
badges = {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0, "checkItemsChecked": 0,
          "checkItemsEarliestDue": None, "comments": 1, "description": True, "due": None, "dueComplete": False,
          "externalSource": None, "fogbugz": "", "lastUpdatedByAi": False, "location": False, "maliciousAttachments": 0,
          "start": None, "votes": 0}
url = f"https://PERSON_6092_TRELLO_USERNAME.com/c/{sl}/{short}-stockholder-close-out"
ins("trello.trello_cards", TC_COLS, [card, CARD_NAME, BOARD["id"], TODO_LIST[0], CARD_DESC, 3.0, False, None, False,
                                     "[]", "[]", short, None, None, url, T["card_comment"], None, js(badges)], card)
cdata = {"board": BOARD, "card": {"id": card, "idShort": short, "name": CARD_NAME, "shortLink": sl}, "list": {"id": TODO_LIST[0], "name": TODO_LIST[1]}}
act = "%08x" % int(ep(T["card"])) + hx("closeout_card_create", 16)
ins("trello.trello_actions", TA_COLS, [act, "createCard", T["card"], TR_LEO, BOARD["id"], card, js(cdata)], act)
act2 = "%08x" % int(ep(T["card_comment"])) + hx("closeout_card_comment", 16)
upd("trello.trello_boards", {'"dateLastActivity"': T["card_comment"]}, "id", BOARD["id"])
ins("trello.trello_actions", TA_COLS, [act2, "commentCard", T["card_comment"], TR_LEO, BOARD["id"], card, js({**cdata, "text": CARD_COMMENT})], act2)

# ======================================================================== Gmail
GM_COLS = ["id", "thread_id", "user_email", "label_ids_json", "snippet", "internal_date", "date", "size_estimate", "subject",
           "from_email", "from_name", "to_json", "cc_json", "bcc_json", "reply_to_json", "body_text", "body_html",
           "headers_json", "in_reply_to", '"references"', "mbox_from", "attachments_meta_json"]
GLOG = {}


from zoneinfo import ZoneInfo
PT_TZ = ZoneInfo("America/Los_Angeles")
SENDER_TZ = {LEO: PT_TZ, ROB: PT_TZ, ART: PT_TZ, "[EMAIL_0801]": ZoneInfo("America/El_Salvador")}


def message(key, box, thread, raw_id, sender, fname, to, cc, subject, body, at, labels, parent=None, new_thread=True, refs=None):
    dt = D.datetime.fromisoformat(at.replace("Z", "+00:00"))
    b = body.replace("\r\n", "\n").replace("\n", "\r\n")
    snippet = " ".join(body.split())[:140]
    hdr_dt = dt.astimezone(SENDER_TZ[sender]) if sender in SENDER_TZ else dt      # base Gmail sends carry the sender's own offset (Calvin's -0600)
    hdrs = [{"name": "Message-ID", "value": raw_id}, {"name": "Date", "value": email.utils.format_datetime(hdr_dt)}, {"name": "Subject", "value": subject},
            {"name": "From", "value": f"{fname} <{sender}>"}, {"name": "To", "value": ", ".join(to)}]
    if cc:
        hdrs.append({"name": "Cc", "value": ", ".join(cc)})
    if parent:
        hdrs += [{"name": "In-Reply-To", "value": parent}, {"name": "References", "value": refs or parent}]
    if new_thread:
        ins("gmail.gmail_threads", ["id", "user_email", "snippet", "history_id"], [thread, box, snippet, None], thread)
    else:
        upd("gmail.gmail_threads", {"snippet": snippet}, "id", thread)
    mid = f"{box}/{raw_id}"
    ins("gmail.gmail_messages", GM_COLS, [mid, thread, box, js(labels), snippet, int(dt.timestamp() * 1000), at, len(b) + 900, subject, sender, fname,
                                          js(to), js(cc), "[]", "[]", b, None, js(hdrs), parent, refs or parent, None, "[]"], mid)
    GLOG[key] = {"message": mid, "thread": thread}


LEO_ADDR = f"leonard hayes <{LEO}>"
KPMG_CC = ["PERSON_4416_NAME <PERSON_4416_EMAIL>", "PERSON_2322_NAME <PERSON_2322_EMAIL>", "PERSON_2847_EMAIL"]
message("kpmg", LEO, B.TH_KPMG, KPMG_ID, "PERSON_3088_EMAIL", "PERSON_3088_NAME", [LEO], KPMG_CC, KPMG_SUBJECT, KPMG_BODY, T["kpmg"], LABEL_IN)
message("kpmg_ack", LEO, B.TH_KPMG, ACK_ID, LEO, NAMES[LEO], ["PERSON_3088_NAME <PERSON_3088_EMAIL>"], KPMG_CC, "Re: " + KPMG_SUBJECT, ACK_BODY, T["ack"],
        LABEL_SENT, parent=KPMG_ID, new_thread=False)
message("kpmg_follow", LEO, B.TH_KPMG, FOLLOW_ID, "PERSON_3088_EMAIL", "PERSON_3088_NAME", [LEO_ADDR], KPMG_CC, "RE: " + KPMG_SUBJECT, FOLLOW_BODY, T["follow"], LABEL_IN,
        parent=ACK_ID, refs=KPMG_ID + " " + ACK_ID, new_thread=False)
message("sunset", LEO, B.TH_SUNSET, SUNSET_ID, "PERSON_2888_EMAIL", "PERSON_2888_NAME", [LEO_ADDR], [], SUNSET_SUBJECT, SUNSET_BODY, T["sunset"], LABEL_IN)
SUNSET_ACK = ("Thanks. I'll get you the sheet next week.\n\nLeonard\n\nOn Fri, Feb 13, 2026 at 10:06 AM PERSON_2888_NAME <PERSON_2888_EMAIL> wrote:\n\n"
              + "\n".join("> " + l if l else ">" for l in SUNSET_BODY.rstrip().split("\n")) + "\n")
message("sunset_ack", LEO, B.TH_SUNSET, SUNSET_ACK_ID, LEO, NAMES[LEO], ["PERSON_2888_NAME <PERSON_2888_EMAIL>"], [], "Re: " + SUNSET_SUBJECT, SUNSET_ACK, T["sunset_ack"], LABEL_SENT,
        parent=SUNSET_ID, new_thread=False)
BOARD_PARENT = "<CAPBs_a5B01FzMbHrb6FgGYtB1YhcNSecOo6FKJ63ki5rD0Gg6Q@mail.gmail.com>"           # Leonard's Feb 12 22:14:52Z reply (base)
BOARD_REFS = "<BYAPR02MB435880CCF501BE0AE906AFFDC460A@BYAPR02MB4358.namprd02.prod.outlook.com> " + BOARD_PARENT
BOARD_ID = "<CAGkro_Tn7wQ2xLp9VbR4mYc8KsHd3EjUf6ZaNi1oGqX5tBe0Rw@mail.gmail.com>"
BOARD_BODY = """Thanks PERSON_4337_NAME, for everything over the last three years. That leaves Leonard and me on the board to see the close through.

Thanks
[PERSON_NAME_0054]

On Thu, Feb 12, 2026 at 2:14 PM leonard hayes <leonard.hayes@harmonygames.co> wrote:

> Hi PERSON_4337_NAME,
>
> Understood and thank you. This confirms receipt of your resignation from
> the Board of [SOURCE_ORG_0001], effective as of today unless you intended a
> different effective date.
"""
BOARD_TO = ["PERSON_4337_NAME <PERSON_4337_EMAIL>"]
BOARD_CC = [LEO_ADDR, "PERSON_2847_NAME <PERSON_2847_EMAIL>", "arthur blake <arthur.blake@harmonygames.co>"]
for key, box, thread, labels in (("board_leo", LEO, f"{LEO}/1856958794180374704", LABEL_IN), ("board_rob", ROB, f"{ROB}/1856959418563541618", ["SENT"]),
                                 ("board_art", ART, f"{ART}/1856959418725253571", ["INBOX", "IMPORTANT", "CATEGORY_PERSONAL"])):
    message(key, box, thread, BOARD_ID, ROB, NAMES[ROB], BOARD_TO, BOARD_CC, "Re: Board position", BOARD_BODY, T["board"], labels, parent=BOARD_PARENT,
            refs=BOARD_REFS, new_thread=False)
NEB_TO = ["PERSON_3941_NAME <PERSON_3941_EMAIL>"]
ROBERT_REFS = "<1002618385.1717453.1691782739607@jlppacebcwls01.onefiserv.net> <CAE426NoTs38nTRaaAq=2u4nYuWZwpwtjTiJ6KAL+WBERzGLm6Q@mail.gmail.com> " + ROBERT_PARENT
message("robert_leo", LEO, f"{LEO}/{B.M_NEB_THREAD}", ROBERT_ID, ROB, NAMES[ROB], NEB_TO, [LEO_ADDR], ROBERT_SUBJECT, ROBERT_BODY, T["robert"], LABEL_IN,
        parent=ROBERT_PARENT, refs=ROBERT_REFS, new_thread=False)
message("robert_rob", ROB, f"{ROB}/1773963101279916523", ROBERT_ID, ROB, NAMES[ROB], NEB_TO, [LEO_ADDR], ROBERT_SUBJECT, ROBERT_BODY, T["robert"], ["SENT"],
        parent=ROBERT_PARENT, refs=ROBERT_REFS, new_thread=False)

# rev2 BOUNCE: Owen's Feb 11 letter (base, thread 1856860994291529096, 20:13:48Z to PERSON_3140_EMAIL) came back 9 s later. Base Gmail keeps
# every bounce in the original's thread (Robert 1769337688765186323; Leonard 1810030685221873164, 1828131137010192802): research/rev2/census_a_bounce.md
OWEN_LETTER = "<CAPBs_a5HKTOGV3nwn6iyxz8GhwLGRaF_Gs-uii3x7tVQ9eTfQQ@mail.gmail.com>"
TH_OWEN = f"{LEO}/1856860994291529096"
BOUNCE_ID = "<698ce305.050a0220.3b7f1c.9d2e.GMR@mx.google.com>"
BOUNCE_BODY = ("** Address not found **\n\nYour message wasn't delivered to PERSON_3140_EMAIL because the address couldn't be found, or is unable to receive mail.\n\n"
               "Learn more here: https://support.google.com/mail/?p=DisabledUser\n\nThe response was:\n\n"
               "550 5.2.1 The email account that you tried to reach is disabled. Learn more at https://support.google.com/mail/?p=DisabledUser "
               "5b1f17b1804b1-4835a1f7e2csor2210417f8f.11 - gsmtp")
_b = BOUNCE_BODY.replace("\n", "\r\n")
_snip = " ".join(BOUNCE_BODY.split())[:140]
_bh = [{"name": "Message-ID", "value": BOUNCE_ID}, {"name": "Date", "value": "Wed, 11 Feb 2026 12:13:57 -0800 (PST)"},
       {"name": "Subject", "value": "Delivery Status Notification (Failure)"}, {"name": "From", "value": "PERSON_3555_NAME <PERSON_3555_EMAIL>"},
       {"name": "To", "value": LEO}, {"name": "Auto-Submitted", "value": "auto-replied"}, {"name": "In-Reply-To", "value": OWEN_LETTER},
       {"name": "References", "value": OWEN_LETTER}, {"name": "X-Failed-Recipients", "value": "PERSON_3140_EMAIL"}]
upd("gmail.gmail_threads", {"snippet": _snip}, "id", TH_OWEN)
ins("gmail.gmail_messages", GM_COLS, [f"{LEO}/{BOUNCE_ID}", TH_OWEN, LEO, js(["INBOX", "IMPORTANT", "Label_b19fb8d1b3", "CATEGORY_UPDATES"]), _snip,
                                      int(ep(T["bounce"]) * 1000), T["bounce"], len(_b) + 7000, "Delivery Status Notification (Failure)", "PERSON_3555_EMAIL",
                                      "PERSON_3555_NAME", js([LEO]), "[]", "[]", "[]", _b, None, js(_bh), OWEN_LETTER, OWEN_LETTER, None, "[]"], f"{LEO}/{BOUNCE_ID}")
GLOG["bounce"] = {"message": f"{LEO}/{BOUNCE_ID}", "thread": TH_OWEN}

# rev2 EXT: Calvin forwards Carta's holder notice (Jan 23) that moved ES-3's last day from Jan 24 to Feb 20, from the address on his issue, in a new thread
# (research/rev2/census_b_carta.md V2; Carta's body follows his base termination notice, thread 1847333347700620793)
EXT_ID = "<CAJr7mPx2QwF8nVb4LtK9sYd3HcE6uZaR1oGiN5tMeBq0WsXkQz@mail.gmail.com>"
TH_EXT = f"{LEO}/1856121753612004097"
CARTA_FOOTER = """       Learn more about Carta <https://Carta.com>   •   Visit Carta’s
Knowledge Base <https://support.Carta.com>   •   Release Notes
<https://releasenotes.Carta.com/>   •   Equity Education Center
<https://Carta.com/equity/learn/what-is-equity/?utm_campaign=q2_2022_corps_us_core-Carta-equity-101-launch&amp;utm_medium=email&amp;utm_source=product&amp;utm_content=>


  The contents of this e-mail message and any attachments are confidential
and may be legally privileged. If you are not the intended recipient,
notify the sender and delete this message and its attachments, if any. 

  To ensure delivery to your inbox, add SVC_0077_EMAIL
<mailto:SVC_0077_EMAIL>, SVC_5909_EMAIL <mailto:SVC_5909_EMAIL>,
and SVC_4490_EMAIL <mailto:SVC_4490_EMAIL> to your address book. 

  For Carta Support, log in and open the Carta Help Center from the user
menu at the top right of the page. Open Carta Help Center →
<https://app.Carta.com/profiles/update/?help=true> 

  eShares, Inc. DBA Carta, Inc. 
 333 Bush Street, Suite 2300 
 San Francisco, CA 94104 
 [PHONE_14952] <tel:[PHONE_14951]>"""
EXT_SUBJECT = "Fwd: Your option grant at [SOURCE_ORG_0001] Games Inc. has been updated"
EXT_BODY = ("Fyi, this came through from Carta. Thanks for sorting out the extra weeks I asked for.\n\nCalvin\n\n"
            "---------- Forwarded message ---------\nFrom: SVC_0077_NAME <SVC_0077_EMAIL>\nDate: Fri, Jan 23, 2026 at 10:05 AM\n"
            "Subject: Your option grant at [SOURCE_ORG_0001] Games Inc. has been updated\nTo: <[EMAIL_0801]>\n\n"
            "= Your option grant has been updated. =\n\n  [SOURCE_ORG_0001] Games Inc. has extended the post-termination exercise period on your\n"
            "option grant. Current holdings and overview of the changes summarized below: \n\n"
            " Equity awards     ID ES-3   Acceptance status Accepted   Granted 8,138  \n"
            "Vested 4,408   Exercised 0   Grant date Nov. 10, 2023   Termination date\n"
            "Oct. 24, 2025   Last day to exercise Feb. 20, 2026 (previously Jan. 24, 2026)    \n \n  \n" + CARTA_FOOTER)
message("ext", LEO, TH_EXT, EXT_ID, "[EMAIL_0801]", "Calvin Price", [LEO_ADDR], [], EXT_SUBJECT, EXT_BODY, T["ext"], LABEL_IN)

# rev2 (UGT, research/prompt_review_rev2/P1.md DR4): Carta's next-business-day digest after the Nov 17, 2023 one (base 1782897835407336831, which lists
# ES-9 and ES-11 and "7 more items"): the two other advisor holders accept ES-8 and ES-10, so all four advisor grants are Carta lines. No amounts, as in every base digest.
DIGEST_ID = "<170056300100.11.4471902385519067321@notifications-worker-75f77576db-lb9sh>"
TH_DIGEST = f"{LEO}/1783169549554193375"
DIGEST_BODY = ("Activity in [SOURCE_ORG_0001] Games Inc.            \n \n  \n     \n \n  \n    =  Here's what's happening in your accounts.  =\n\n"
               "  Activity for [SOURCE_ORG_0001] Games Inc.      [PERSON_NAME_0089] [PERSON_NAME_25152]\naccepted  option grant ES-8\n"
               "<https://app.Carta.com/options/list/3048065/?open=18258527>     PERSON_1287_NAME\naccepted  option grant ES-10\n"
               "<https://app.Carta.com/options/list/3048065/?open=18258529>      View\n[SOURCE_ORG_0001] Games Inc. on Carta ›\n"
               "<https://app.Carta.com/corporations/3048065/summary/> \n \n \n \n  \n" + CARTA_FOOTER)
message("digest", LEO, TH_DIGEST, DIGEST_ID, "SVC_0077_EMAIL", "SVC_0077_NAME", [LEO], [], "Carta activity for Nov. 20, 2023", DIGEST_BODY, "2023-11-21T10:36:41Z",
        ["INBOX", "IMPORTANT", "Label_b19fb8d1b3", "CATEGORY_UPDATES"])

# rev2 ALIAS: Leonard tells Matthew Collins about the closing at a personal address, under the name he signs with ("best / akin",
# leonard.hayes@harmonygames.co/1847258343060233599); after his Feb 12 22:17Z list and before Robert's 23:41Z angel mail (research/rev2/census_c_alias.md,
# attack_coherence.md N3)
AKIN_ID = "<CAPBs_aLeDrdRoqOb0LrQ1AfGvbpmR-YdoG8A6PGmPay5Sc-ng=@mail.gmail.com>"
TH_AKIN = f"{LEO}/1856961760270377901"
AKIN_BODY = """Hi Akin,

Not the note I hoped to write. Harmony is shutting down: we let the team know yesterday, and Robert and I are handling the wind-down from here.

I'll come back to you once the paperwork side is clear. Thank you for everything, on the board and since.

Leonard
"""
message("akin", LEO, TH_AKIN, AKIN_ID, LEO, NAMES[LEO], ["Husnu Akin <PERSON_8862_EMAIL>"], [], "Harmony", AKIN_BODY, T["akin"], LABEL_SENT)

# The Nov 26, 2024 owner list says its percentages add to 100%, but its 27 lines sum to 94.1% (the pool is not listed): drop that one sentence
for ob in json.load(open(os.path.join(HERE, "owner_list_bodies.json"))):
    old = "diluted ownership\n         (Total ownership percentage adds to 100%)."
    assert old in ob["body"], ob["id"]
    upd("gmail.gmail_messages", {"body_text": ob["body"].replace(old, "diluted ownership", 1)}, "id", ob["id"])

# ======================================================================== GCal (Leonard is the only attendee)
GC_COLS = ["event_id", "calendar_id", "summary", "description", "location", "start_ts", "end_ts", "start_json", "end_json",
           "organizer_email", "creator_email", "attendees_json", "status", "visibility", "transparency", "rrule_json",
           "recurring_event_id", "original_start_json", "sequence", "created", "updated", "hangout_link", "ical_uid"]
end = plus(T["hold_start"], 1800)
ins("gcal.gcal_events", GC_COLS, [B.EVT_HOLD, LEO, HOLD_SUMMARY, None, None, T["hold_start"], end, js({"dateTime": T["hold_start"]}), js({"dateTime": end}),
                                  LEO, LEO, js([{"email": LEO, "organizer": True, "responseStatus": "accepted", "self": True}]), "confirmed", None, "opaque", "[]",
                                  None, None, 0, T["hold_created"], T["hold_created"], None, hx("hold_ical", 32) + "@hg4"], B.EVT_HOLD)

# ======================================================================== Contacts
ins("contacts.contacts", ["contact_id", "first_name", "last_name", "is_user", "gender", "status", "job", "description", "email", "created_at", "updated_at"],
    [hx("contact_bergmann", 24), "PERSON_0693", "", False, "Unknown", "Unknown", "Investor", None, "PERSON_0693_EMAIL", T["folder"], T["folder"]], "contact_bergmann")
upd("contacts.contacts", {"job": "Investor and advisor (left the board May 2025)", "updated_at": "2025-05-02T16:20:11Z"}, "contact_id", "db57e559500151d6b3991b62")
ins("contacts.contacts", ["contact_id", "first_name", "last_name", "is_user", "gender", "status", "job", "description", "email", "created_at", "updated_at"],
    [hx("contact_eren", 24), "PERSON_2275", "", False, "Unknown", "Unknown", "Investor", None, "PERSON_2275_EMAIL", plus(T["folder"], 41), plus(T["folder"], 41)], "contact_eren")

# ======================================================================== Linear
HF_PATH = os.path.join(HERE, "holder_facts.json")
HF = json.load(open(HF_PATH)) if os.path.exists(HF_PATH) else {}
ins("linear.linear_projects", ["id", "team_id", "name", "summary", "description", "lead_id", "priority", "state", "start_date",
                               "target_date", "labels_json", "links_json", "is_archived", "created_at", "updated_at"],
    [B.PROJECT, "team_ENG", "Holder records", None, PROJECT_DESC, LIN[LEO], 0, "started", "2026-02-12", None, "[]", "[]", False, T["project"], T["project_upd"]], B.PROJECT)
LI_COLS = ["id", "project_id", "team_id", "parent_id", "assignee_id", "creator_id", "state_id", "cycle_id", "identifier",
           "number", "title", "description", "priority", "estimate", "due_date", "started_at", "completed_at", "canceled_at",
           "archived_at", "time_in_status_minutes", "labels_json", "links_json", "relations_json", "state_history_json",
           "is_archived", "created_at", "updated_at"]
LC_COLS = ["id", "issue_id", "author_id", "parent_id", "body", "is_edited", "created_at", "updated_at"]
LINROWS = {}


def step(label, lo, hi):
    return lo + int(hx(label, 6), 16) % (hi - lo + 1)


def when(iso):
    d = D.date.fromisoformat(iso)
    return f"{d.strftime('%b')} {d.day}, {d.year}"


def channel(f):
    c = f["last_contact_channel"]
    if c.startswith("group channel, "):
        return c.split(", ", 1)[1]
    if c.startswith("WhatsApp"):
        return "whatsapp"
    return {"mail, Leonard on bcc": "mail", "mail, Leonard on cc": "mail", "mail, bcc": "the investor update, bcc"}.get(c, c)


# Leonard's own (Pacific) date of each last written contact; overrides from research/sweeps/rev1_delta_b.md: the Jan 31 02:26Z group DM
# CE22D7884D8F reaches ES-7 and ES-13 (Jan 30 PT), Calvin's Oct 23 #zombie-bugs post, and three rows whose UTC date differs in PT
LAST_PT = {"ENG-2447": "2025-10-28", "ENG-2438": "2026-01-24", "ENG-2439": "2026-01-24", "ENG-2446": "2025-10-23", "ENG-2454": "2025-10-21",
           "ENG-2456": "2026-01-30", "ENG-2458": "2026-01-30", "ENG-2452": "2025-10-23"}
LASTMAIL = json.load(open(os.path.join(HERE, "last_mail.json")))      # plan/last_mail.py: newest message in Leonard's mailbox before Feb 1 (PT) carrying the issue's address
created, last_at, fig_at = T["issue0"], T["last0"], T["fig0"]
TITLE = {"ENG-2447": "Husnu Matthew Collins", "ENG-2460": "Brian Foster"}
# each holder's email as Leonard has it: the Carta invite lists (leonard.hayes@harmonygames.co/1782034095239486005 [34] and [3], /1789011705438137160 [15], [PERSON_NAME_0051]'s
# own mails), the May 18, 2024 investor update list (/1799418746420547240 [2]), the Feb 11 letters and Robert's Feb 12 reply
EMAIL = {"ENG-2438": "PERSON_4337_EMAIL", "ENG-2439": "PERSON_4337_EMAIL", "ENG-2440": "PERSON_3336_EMAIL", "ENG-2441": "PERSON_3063_EMAIL", "ENG-2442": "PERSON_0693_EMAIL",
         "ENG-2443": "PERSON_2260_EMAIL", "ENG-2444": "patrick@harmonygames.co", "ENG-2445": "PERSON_2275_EMAIL", "ENG-2446": "PERSON_3941_EMAIL", "ENG-2447": "matthew.collins@harmonygames.co",
         "ENG-2448": "PERSON_5275_EMAIL", "ENG-2449": "PERSON_1287_EMAIL", "ENG-2450": "PERSON_2361_EMAIL", "ENG-2451": "PERSON_3641_EMAIL", "ENG-2452": "[EMAIL_0801]",
         "ENG-2453": "PERSON_2360_EMAIL", "ENG-2454": "PERSON_4194_EMAIL", "ENG-2455": "victor.barnes@harmonygames.co", "ENG-2456": "marcus.bennett@harmonygames.co",
         "ENG-2457": "PERSON_3140_EMAIL", "ENG-2458": "PERSON_4363_EMAIL", "ENG-2459": "PERSON_2684_EMAIL", "ENG-2460": "PERSON_4243_EMAIL", "ENG-2461": "cameron@harmonygames.co",
         "ENG-2462": "PERSON_2314_EMAIL", "ENG-2463": "PERSON_1174_EMAIL"}
NOTICE = {}      # TOR's Jun 14, 2023 mail 'For legal notices'; the side letter's Attn line (gdocs /docs_documents/238)    # Carta's SSP-10 name (leonard.hayes@harmonygames.co/1777100628672295991); the letter's addressee
for n, h in enumerate(B.HOLDERS):
    k = h[0]
    f = dict(HF[k])
    f["title_form"] = TITLE.get(k, f["title_form"])
    if n:
        created = plus(created, step(f"issue|{k}", 6, 34))
        last_at = plus(last_at, step(f"last|{k}", 8, 20))
        fig_at = plus(fig_at, step(f"fig|{k}", 26, 70))
    figure = f["owner_list_figure"]
    if k in ("ENG-2438", "ENG-2439"):
        fig_text = f"Nov 2024 owner list: {figure}, both funds on one line"
    elif figure:
        fig_text = f"Nov 2024 owner list: {figure}"
    else:
        fig_text = "Not on the Nov 2024 owner list"
    lm = LASTMAIL[k]["date_pt"]
    last_text = f"Last mail with that address before Feb: {when(lm)}" if lm else "No mail with that address before Feb"
    comments = [(LEO, last_text, last_at), (LEO, fig_text, fig_at)]
    assert last_at < T["robert"], (k, last_at)
    ins("linear.linear_issues", LI_COLS, [k, B.PROJECT, "team_ENG", None, None, LIN[LEO], "Backlog", None, k, int(k.split("-")[1]), f["title_form"], f"Email: {EMAIL[k]}" + NOTICE.get(k, ""), 0,
                                          None, None, None, None, None, None, None, "[]", "[]", "[]", "[]", False, created, fig_at], k)
    ids = []
    for i, (who, body, at) in enumerate(comments):
        cid = "comment_" + hx(f"note|{k}|{i}", 32)
        ins("linear.linear_comments", LC_COLS, [cid, k, LIN[who], None, body, False, at, at], cid)
        ids.append(cid)
    LINROWS[k] = {"title": f["title_form"], "comments": ids, "created": created, "updated": fig_at}

# ======================================================================== write
order = ["gdrive", "gdocs", "gsheets", "gslides", "slack", "trello", "gmail", "gcal", "contacts", "linear"]
n_ins = sum(1 for s in OUT for x in OUT[s] if x.startswith("INSERT"))
n_upd = sum(1 for s in OUT for x in OUT[s] if x.startswith("UPDATE"))
head = ["-- Are you planning to inject? Yes",
        f"-- HarmonyGames injection - persona Leonard Hayes <{LEO}> (Co-founder & Creative Director), Long Horizon.",
        f"-- Services: {', '.join(order)}. Statements: {n_ins} INSERT (one row each), {n_upd} UPDATE.",
        "-- Literal values only; parents before children; re-apply this exact SQL before every agent run.", "BEGIN;"]
body = []
for s in order:
    body.append(f"-- ===================== {s.upper()} =====================")
    body += OUT[s]
open(os.path.join(TI, "01_Universe_Inject.sql"), "w").write("\n".join(head + body + ["COMMIT;"]) + "\n")
json.dump({"rows": ROWS, "slack": SLACK, "gmail": GLOG, "linear": LINROWS, "deck": {"pages": PAGES, "elements": ELS},
           "trello": {"card": card, "create_action": act, "comment_action": act2, "idShort": short, "shortLink": sl},
           "titles": {"notes": NOTES_TITLE, "old": OLD_TITLE, "sheet": DRAFT_TITLE, "deck": DECK_TITLE, "folder": FOLDER_NAME},
           "times": T}, open(os.path.join(HERE, "sql_ids.json"), "w"), indent=1, ensure_ascii=False)
print(n_ins, n_upd, {k: len(v) for k, v in ROWS.items()})
