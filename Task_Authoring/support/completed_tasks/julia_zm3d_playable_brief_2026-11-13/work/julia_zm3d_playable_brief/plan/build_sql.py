#!/usr/bin/env python3
"""Build task_inputs/01_Universe_Inject.sql for Julia Lawson · ZM3D playable brief (rev2, design D3).
Linear and Slack come from the generator's rendered parts (Working_Files/build/parts, from plan/build_spec.py); this file
writes Drive, Docs, Sheets, Slides, Calendar, Gmail, Trello and Contacts and splices everything together.
Read-only on the base; writes only under the task folder. Never executes SQL.
Row shapes follow base records and the accepted frederick_q4 injection's helpers (task_inputs-uselater/Working_Files/plan)."""
import datetime as D, email.utils, hashlib, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
TI = WF.parent
sys.path.insert(0, str(HERE))
import design_model as M
import planned_texts as TXT

S = M.SEED
JULIA, FRED, BRIAN, ROB, CALVIN, LEO = ("julia.lawson@harmonygames.co", "frederick.stone@harmonygames.co", "brian.foster@harmonygames.co",
                                        "robert@harmonygames.co", "calvin.price@harmonygames.co", "leonard.hayes@harmonygames.co")
NAMES = {JULIA: "Julia Lawson", FRED: "Frederick Stone", BRIAN: "Brian Foster", ROB: "Robert", CALVIN: "Calvin Price"}
ROOT = {JULIA: M.BASE["julia_root"], FRED: "d_175c0d7bc72ed244b944cb", BRIAN: "d_fc22d5941b2aeb5c03ad32", CALVIN: "d_49b9dfa5208d400d9b3937"}
TR_LEO = "PERSON_6094_TRELLO_USER_ID"
BOARD = {"id": "640643a3fd8f3ca308d9318e", "name": "Harmony Games", "shortLink": "f4LGcmuh"}
CARD = {"id": M.BASE["trello_kickoff"], "idShort": 447, "name": "Playable Kickoff", "shortLink": "XIcVS41B"}
LIST = {"id": "640643a3fd8f3ca308d93195", "name": "To Do"}

def h(seed, n): return M.h(seed, n)
def dt(iso): return D.datetime.fromisoformat(iso.replace("Z", "+00:00"))
def q(v):
    if v is None: return "NULL"
    if isinstance(v, bool): return "true" if v else "false"
    if isinstance(v, (int, float)): return repr(v)
    s = str(v)
    if "\n" in s or "\\" in s or "\r" in s:
        return "E'" + s.replace("\\", "\\\\").replace("'", "''").replace("\r", "\\r").replace("\n", "\\n") + "'"
    return "'" + s.replace("'", "''") + "'"
def js(x): return json.dumps(x, ensure_ascii=False)
OUT, ROWS = {}, {}
def ins(table, cols, vals, key):
    OUT.setdefault(table.split(".")[0], []).append(f"INSERT INTO {table} ({', '.join(cols)})\nVALUES ({', '.join(q(v) for v in vals)});")
    ROWS.setdefault(table, []).append(key)
def upd(table, sets, key_col, key):
    OUT.setdefault(table.split(".")[0], []).append(f"UPDATE {table} SET {', '.join(f'{k} = {q(v)}' for k, v in sets.items())} WHERE {key_col} = {q(key)};")
    ROWS.setdefault(table + " (UPDATE)", []).append(key)

# ============================================================ Drive / Docs / Sheets / Slides
DF_COLS = ["id", "name", "mime_type", "parents_json", "owner_email", "shared_with_emails_json", "shared_roles_json", "visibility", "owners_json",
           "modified_time", "created_time", "trashed", "starred"]
DOC_MT, SLIDE_MT, SHEET_MT = ("application/vnd.google-apps.document", "application/vnd.google-apps.presentation", "application/vnd.google-apps.spreadsheet")
def drive(fid, name, mime, owner, shares, created, modified):
    ins("gdrive.drive_files", DF_COLS, [fid, name, mime, js([ROOT[owner]]), owner, js([e for e, _ in shares]),
                                        js([{"email": e, "role": r} for e, r in shares]), "private", js([owner]), modified, created, False, False], fid)
def doc(fid, title, body, owner, shares, created, modified):
    drive(fid, title, DOC_MT, owner, shares, created, modified)
    first = len(body.split("\n", 1)[0])
    runs = [{"start": 0, "end": first + 1, "named_style": "TITLE", "list_id": None, "list_nesting": 0},
            {"start": first + 1, "end": len(body), "named_style": "NORMAL_TEXT", "list_id": None, "list_nesting": 0}]
    ins("gdocs.docs_documents", ["document_id", "title", "owner_email", "shared_with_emails_json", "visibility", "body_text", "style_runs_json", "revision_id",
                                 "drive_file_id", "created_time", "modified_time"],
        [fid, title, owner, js([e for e, _ in shares]), "private", body, js(runs), h("rev" + fid, 10), fid, created, modified], fid)
def sheet(fid, title, grid, tab, owner, shares, created, modified):
    drive(fid, title, SHEET_MT, owner, shares, created, modified)
    ins("gsheets.sheets_spreadsheets", ["spreadsheet_id", "title", "owner_email", "shared_with_emails_json", "visibility", "drive_file_id", "created_time", "modified_time"],
        [fid, title, owner, js([e for e, _ in shares]), "private", fid, created, modified], fid)
    ins("gsheets.sheets_sheets", ["spreadsheet_id", "sheet_id", "title", '"index"', "row_count", "column_count", "grid_json"],
        [fid, 0, tab, 0, 1000, 26, js(grid)], f"{fid}#0")
def deck(fid, title, slides, owner, shares, created, modified):
    drive(fid, title, SLIDE_MT, owner, shares, created, modified)
    ins("gslides.slides_presentations", ["presentation_id", "title", "owner_email", "shared_with_emails_json", "visibility", "drive_file_id", "revision_id",
                                         "created_time", "modified_time"],
        [fid, title, owner, js([e for e, _ in shares]), "private", fid, h("rev" + fid, 10), created, modified], fid)
    for i, (head, body) in enumerate(slides):
        sid = "slide_" + h(fid + "s" + str(i), 12)
        ins("gslides.slides_pages", ["presentation_id", "object_id", '"index"', "layout", "notes"], [fid, sid, i, "TITLE_AND_BODY", None], f"{fid}#{sid}")
        for oid, ph, text, ordn, y, hgt in [("el_" + h(fid + "e" + str(i), 12), "TITLE", head, 0, 457200, 1143000),
                                             ("el_" + h(fid + "b" + str(i), 12), "BODY", body, 1, 1600200, 3200400)]:
            ins("gslides.slides_page_elements", ["presentation_id", "page_object_id", "object_id", "kind", "text", "placeholder_type", "x_emu", "y_emu",
                                                 "width_emu", "height_emu", "table_json", "ordinal"],
                [fid, sid, oid, "SHAPE", text, ph, 457200, y, 8229600, hgt, None, ordn], f"{fid}#{oid}")

NOTES_TITLE = TXT.NOTES.split("\n", 1)[0]
doc(S["notes"]["id"], NOTES_TITLE, TXT.NOTES.rstrip("\n"), FRED, [(JULIA, "reader"), (BRIAN, "reader"), (ROB, "reader")], "2025-09-30T16:25:41Z", "2025-09-30T16:58:19Z")
TRACKER_GRID = [["Line", "Kind", "Category", "Went out", "Ticket"]] + [[l["name"], l["kind"], l["category"], l["went_out"], l["ticket"]] for l in M.LINES if l["on_list"]]
sheet(S["tracker"]["id"], "ZM3D playable - pack list", TRACKER_GRID, "Pack", BRIAN, [(FRED, "reader"), (JULIA, "reader"), (ROB, "reader")],
      "2025-09-25T06:48:27Z", "2025-09-26T17:25:08Z")
sheet(S["c2_sheet"]["id"], TXT.C2_SHEET_TITLE, TXT.C2_SHEET_GRID, "Sources", CALVIN, [(ROB, "writer"), (JULIA, "reader"), (BRIAN, "reader")],
      "2025-09-12T15:42:11Z", "2025-09-26T20:10:36Z")
deck(S["deck"]["id"], TXT.DECK_SLIDES[0][0], TXT.DECK_SLIDES, JULIA, [(BRIAN, "reader")], "2025-09-23T19:31:22Z", "2025-09-23T19:55:47Z")
doc(S["c4_log"]["id"], TXT.C4_LOG_TITLE, TXT.C4_LOG, BRIAN, [(FRED, "reader"), (JULIA, "reader")], "2025-09-25T15:58:14Z", S["c4_log"]["at"])

# ============================================================ Trello: Leonard's comment on his Playable Kickoff card
TA_COLS = ["id", "type", "date", '"idMemberCreator"', '"idBoard"', '"idCard"', "data_json"]
ins("trello.trello_actions", TA_COLS, [S["trello_note"]["id"], "commentCard", S["trello_note"]["at"], TR_LEO, BOARD["id"], CARD["id"],
                                       js({"text": TXT.TRELLO_NOTE, "textData": {"emoji": {}}, "card": CARD, "board": BOARD, "list": LIST})], S["trello_note"]["id"])
BADGES = {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0, "checkItemsChecked": 0, "checkItemsEarliestDue": None,
          "comments": 1, "description": False, "due": None, "dueComplete": False, "externalSource": None, "fogbugz": "", "lastUpdatedByAi": False,
          "location": False, "maliciousAttachments": 0, "start": None, "votes": 0}
upd("trello.trello_cards", {"badges_json": js(BADGES), '"dateLastActivity"': S["trello_note"]["at"]}, "id", CARD["id"])
upd("trello.trello_boards", {'"dateLastActivity"': S["trello_note"]["at"]}, "id", BOARD["id"])

# ============================================================ Calendar: Frederick's kickoff hold, one row per attendee calendar (INT-11)
GC_COLS = ["event_id", "calendar_id", "summary", "description", "location", "start_ts", "end_ts", "start_json", "end_json", "organizer_email", "creator_email",
           "attendees_json", "status", "visibility", "transparency", "rrule_json", "recurring_event_id", "original_start_json", "sequence", "created", "updated",
           "hangout_link", "ical_uid"]
HOLD_START, HOLD_END, HOLD_CREATED = "2025-11-03T17:00:00Z", "2025-11-03T17:30:00Z", "2025-09-30T16:41:17Z"
ATTENDEES = [FRED, JULIA, BRIAN, ROB]
UID = h("uid_hold", 32) + "@hg4"
EVT = {}
for cal in ATTENDEES:
    eid = S["hold"]["id"] if cal == JULIA else "evt_" + h("hold_" + cal, 22)
    att = []
    for e in sorted(ATTENDEES):
        a = {"email": e, "organizer": e == FRED, "responseStatus": "accepted" if e == FRED else "needsAction"}
        if e == cal: a["self"] = True
        att.append(a)
    ins("gcal.gcal_events", GC_COLS, [eid, cal, TXT.HOLD_SUMMARY, None, None, HOLD_START, HOLD_END, js({"dateTime": HOLD_START}), js({"dateTime": HOLD_END}),
                                      FRED, FRED, js(att), "confirmed", None, "opaque", "[]", None, None, 0, HOLD_CREATED, HOLD_CREATED, None, UID], eid)
    EVT[cal] = eid

# ============================================================ Gmail: the invitation mail in each guest's mailbox (INT-11 companions)
GM_COLS = ["id", "thread_id", "user_email", "label_ids_json", "snippet", "internal_date", "date", "size_estimate", "subject", "from_email", "from_name",
           "to_json", "cc_json", "bcc_json", "reply_to_json", "body_text", "body_html", "headers_json", "in_reply_to", '"references"', "mbox_from",
           "attachments_meta_json"]
def thread_num(at, seed): return str((int(dt(at).timestamp() * 1000) << 20) + (int(h(seed, 8), 16) & 0xFFFFF))
INVITES = {}
GUESTS = [JULIA, BRIAN, ROB]
for box in GUESTS:
    key = "inv_hold"
    d0 = dt(HOLD_CREATED); ms = int(d0.timestamp() * 1000)
    mid = f"<calendar-{h(key + box, 8)}-{h(key + box + '1', 4)}-{h(key + box + '2', 4)}-{h(key + box + '3', 4)}-{h(key + box + '4', 12)}@google.com>"
    subject = f"Invitation: {TXT.HOLD_SUMMARY} @ Mon Nov 3, 2025 9am - 9:30am (PST) ({box})"
    body = (f"{TXT.HOLD_SUMMARY}\r\nMonday Nov 3, 2025 \u22c5 9am \u2013 9:30am\r\nPacific Time - Los Angeles\r\n\r\n"
            f"Organizer\r\n{NAMES[FRED]}\r\n{FRED}\r\n\r\nGuests\r\n{NAMES[FRED]} - organizer\r\n" + "\r\n".join(GUESTS) + "\r\n")
    tref = f"{box}/{thread_num(HOLD_CREATED, key + box)}"
    snippet = " ".join(body.split())[:140]
    ins("gmail.gmail_threads", ["id", "user_email", "snippet", "history_id"], [tref, box, snippet, None], tref)
    frm = f"{NAMES[FRED].lower()} <{FRED}>"
    hdrs = [{"name": "Message-ID", "value": mid}, {"name": "Date", "value": email.utils.format_datetime(d0)}, {"name": "Subject", "value": subject},
            {"name": "From", "value": frm}, {"name": "To", "value": ", ".join(GUESTS)}]
    ins("gmail.gmail_messages", GM_COLS, [f"{box}/{mid}", tref, box, js(["INBOX", "CATEGORY_PERSONAL"]), snippet, ms, HOLD_CREATED, len(body) + 3000, subject,
                                          FRED, NAMES[FRED].lower(), js(GUESTS), "[]", "[]", js([frm]), body, None, js(hdrs), None, None, None, "[]"], f"{box}/{mid}")
    INVITES[box] = {"thread": tref, "message": f"{box}/{mid}"}

# ============================================================ Contacts: PlayableX's intake address
CT_COLS = ["contact_id", "first_name", "last_name", "is_user", "gender", "status", "job", "email"]
C = TXT.CONTACT
ins("contacts.contacts", CT_COLS, [S["contact"]["id"], C["first_name"], C["last_name"], False, "Unknown", "Unknown", C["job"], C["email"]], S["contact"]["id"])

# ============================================================ splice the generator parts and write
PARTS = WF / "build" / "parts"
def part(name):
    lines = [l for l in (PARTS / f"{name}.sql").read_text().splitlines() if l.strip() and not l.startswith("--")]
    return lines
gen = {"slack": part("slack"), "linear": part("linear")}
order = ["gdrive", "gdocs", "gsheets", "gslides", "slack", "linear", "trello", "gcal", "gmail", "contacts"]
stmts = {s: (gen[s] if s in gen else OUT.get(s, [])) for s in order}
n_ins = sum(1 for s in order for x in stmts[s] if x.startswith("INSERT"))
n_upd = sum(1 for s in order for x in stmts[s] if x.startswith("UPDATE"))
head = ["-- Are you planning to inject? Yes",
        f"-- HarmonyGames injection - persona Julia Lawson <{JULIA}> (Product Manager), Long Horizon.",
        f"-- Services: {', '.join(order)}. Statements: {n_ins} INSERT (one row each), {n_upd} UPDATE.",
        "-- Literal values only; parents before children; re-apply this exact SQL before every agent run.", "BEGIN;"]
body = []
for s in order:
    body.append(f"-- {s}")
    body += stmts[s]
(TI / "01_Universe_Inject.sql").write_text("\n".join(head + body + ["COMMIT;"]) + "\n")
json.dump({"rows": ROWS, "events": EVT, "invites": INVITES, "ical_uid": UID}, open(HERE / "out" / "sql_ids.json", "w"), indent=1)
print(n_ins, "INSERT", n_upd, "UPDATE", {k: len(v) for k, v in ROWS.items()}, "| generator parts: slack", len(gen["slack"]), "linear", len(gen["linear"]))
