#!/usr/bin/env python3
"""Builds 01_Universe_Inject.sql for Robert: the seed, bet by bet (normal universe, Feb 14, 2026).
Reads plan/ids.json, wording.json, cohort.json (build_scenario.py), plan/notes.json (per-payee notes, each proven against a base
record) and research/minted_ids.json. Shapes follow the robert_llc_takeover SQL that passed /injection. Never executes SQL.
Writes the SQL and plan/sql_ids.json."""
import base64, datetime as D, email.utils, hashlib, json, os, textwrap
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); TI = os.path.dirname(WF)
I = json.load(open(os.path.join(HERE, "ids.json"))); Q = json.load(open(os.path.join(HERE, "wording.json")))
C = json.load(open(os.path.join(HERE, "cohort.json"))); MINT = json.load(open(os.path.join(HERE, "research", "minted_ids.json")))
NOTESF = os.path.join(HERE, "notes.json")
NOTES = json.load(open(NOTESF)) if os.path.exists(NOTESF) else {p[0]: [{"author": a, "text": t} for a, t in p[4]] for p in C}
IDS, BASE, T, ISS = I["IDS"], I["BASE"], I["T"], I["issues"]
SALT = "hg-robert-seed-bets|"
ROB, LEO, ART = "robert@harmonygames.co", "leonard.hayes@harmonygames.co", "arthur.blake@harmonygames.co"
NAMES = {ROB: "robert", LEO: "leonard hayes", ART: "arthur blake"}
SLACK_U = {LEO: "EMPLOYEE_0038_SLACK_ID", "scott": "EMPLOYEE_0024_SLACK_ID"}
LIN = {"leonard": "usr_63fffeb4fab5233e", "arthur": "usr_cc3e90160f490686"}
ROOT = {LEO: "d_63fffeb4fab5233ed5bb73"}
BOARD = {"id": "640643a3fd8f3ca308d9318e", "name": "Harmony Games", "shortLink": "f4LGcmuh"}
TODO_LIST = ("640643a3fd8f3ca308d93195", "To Do"); TR_LEO = "PERSON_6094_TRELLO_USER_ID"
def hx(l, n): return hashlib.sha256((SALT + l).encode()).hexdigest()[:n]
def ep(iso): return D.datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp()
def iso_of(t): return D.datetime.fromtimestamp(t, D.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def plus(iso, s): return iso_of(ep(iso) + s)
def q(v):
    if v is None: return "NULL"
    if isinstance(v, bool): return "true" if v else "false"
    if isinstance(v, (int, float)): return repr(v)
    s = str(v)
    if "\n" in s or "\\" in s or "\r" in s:
        return "E'" + s.replace("\\", "\\\\").replace("'", "''").replace("\r", "\\r").replace("\n", "\\n") + "'"
    return "'" + s.replace("'", "''") + "'"
js = lambda x: json.dumps(x, ensure_ascii=False)
OUT, ROWS = {}, {}
def upd_raw(schema, stmt, key):
    OUT.setdefault(schema, []).append(stmt); ROWS.setdefault(schema + " (UPDATE)", []).append(key)
def ins(table, cols, vals, key):
    OUT.setdefault(table.split(".")[0], []).append(f"INSERT INTO {table} ({', '.join(cols)})\nVALUES ({', '.join(q(v) for v in vals)});")
    ROWS.setdefault(table, []).append(key)
slack_id = lambda c, ts: hashlib.sha256(f"{c}|{ts}".encode()).hexdigest()[:32]
# ---- Drive / Docs / Sheets / Slides
DF = ["id", "name", "mime_type", "parents_json", "owner_email", "shared_with_emails_json", "shared_roles_json", "visibility", "owners_json", "modified_time", "created_time", "trashed", "starred"]
DOC, SHEET, SLIDES = "application/vnd.google-apps.document", "application/vnd.google-apps.spreadsheet", "application/vnd.google-apps.presentation"
SH = [ROB, ART]
def drive(fid, name, mime, created, modified):
    ins("gdrive.drive_files", DF, [fid, name, mime, js([ROOT[LEO]]), LEO, js(SH), js([{"email": e, "role": "writer"} for e in SH]), "private", js([LEO]), modified, created, False, False], fid)
m = IDS["method"]; title = Q["method_title"]; body = Q["method"].rstrip("\n")
drive(m, title, DOC, T["method"], T["method_mod"])
runs, pos = [], 0
for i_, line in enumerate(body.split("\n")):   # base: one run per paragraph, ending before its newline
    if line:
        runs.append({"start": pos, "end": pos + len(line), "named_style": "TITLE" if i_ == 0 else "NORMAL_TEXT", "list_id": None, "list_nesting": 0})
    pos += len(line) + 1
ins("gdocs.docs_documents", ["document_id", "title", "owner_email", "shared_with_emails_json", "visibility", "body_text", "style_runs_json", "revision_id", "drive_file_id", "created_time", "modified_time"],
    [m, title, LEO, js(SH), "private", body, js(runs), MINT["gdocs"]["revision"], m, T["method"], T["method_mod"]], m)
s_ = IDS["sheet"]; drive(s_, Q["sheet_title"], SHEET, T["sheet"], T["sheet"])
ins("gsheets.sheets_spreadsheets", ["spreadsheet_id", "title", "owner_email", "shared_with_emails_json", "visibility", "drive_file_id", "created_time", "modified_time"],
    [s_, Q["sheet_title"], LEO, js(SH), "private", s_, T["sheet"], T["sheet"]], s_)
ins("gsheets.sheets_sheets", ["spreadsheet_id", "sheet_id", "title", '"index"', "row_count", "column_count", "grid_json"], [s_, 0, "Sheet1", 0, 1 + len(Q["sheet_rows"]), len(Q["sheet_header"]), js([Q["sheet_header"]] + [list(r) for r in Q["sheet_rows"]])], f"{s_}#0")
d_ = IDS["deck"]; drive(d_, Q["deck_title"], SLIDES, T["deck"], T["deck"])
ins("gslides.slides_presentations", ["presentation_id", "title", "owner_email", "shared_with_emails_json", "visibility", "drive_file_id", "revision_id", "created_time", "modified_time"],
    [d_, Q["deck_title"], LEO, js(SH), "private", d_, MINT["gslides"]["revision"], T["deck"], T["deck"]], d_)
DECK_EL = []
for n, text in enumerate(Q["deck"]):
    pid = MINT["gslides"]["pages"][n] if n < 3 else "slide_" + hx(f"deck-page-{n}", 12)
    eid = MINT["gslides"]["elements"][n] if n < 3 else "el_" + hx(f"deck-el-{n}", 12)
    ins("gslides.slides_pages", ["presentation_id", "object_id", '"index"', "layout", "notes"], [d_, pid, n, "BLANK", None], f"{d_}#{pid}")
    ins("gslides.slides_page_elements", ["presentation_id", "page_object_id", "object_id", "kind", "text", "placeholder_type", "x_emu", "y_emu", "width_emu", "height_emu", "table_json", "ordinal"],
        [d_, pid, eid, "TEXT_BOX", text, None, 0, 0, 9144000, 5143500, None, 0], f"{d_}#{eid}"); DECK_EL.append(f"{d_}#{eid}")
# ---- Slack: new top-level posts, so no base row is updated
SL = ["id", "ts", "channel_id", "type", "user_id", "text", "thread_parent_id", "thread_ts_legacy", "reply_count", "reply_users_count", "latest_reply", "is_activity_message", "subtype", "reactions_json", "files_json", "attachments_json", "created_at", "metadata_json"]
SLACK = {}
def slack(key, user, text):
    ch, ts = IDS[key].split("/"); mid = slack_id(ch, ts)
    ins("slack.slack_messages", SL, [mid, ts, ch, "message", user, text, None, None, 0, 0, None, False, None, "[]", "[]", "[]", iso_of(float(ts)), "{}"], IDS[key])
    SLACK[key] = {"id": mid, "ts": ts, "channel": ch, "locator": IDS[key]}
slack("ask", SLACK_U[LEO], Q["ask"]); slack("ask2", SLACK_U[LEO], Q["ask2"]); slack("statement", SLACK_U["scott"], Q["statement"]); slack("return_note", SLACK_U[LEO], Q["return_note"])
# ---- Trello
TC = ["id", "name", '"idBoard"', '"idList"', '"desc"', "pos", "closed", "due", '"dueComplete"', '"idMembers_json"', '"idLabels_json"', '"idShort"', '"shortLink"', '"shortUrl"', "url", '"dateLastActivity"', "cover_json", "badges_json"]
TA = ["id", "type", "date", '"idMemberCreator"', '"idBoard"', '"idCard"', "data_json"]
card, short, sl = IDS["trello"], MINT["trello"]["idShort"], MINT["trello"]["slug8"]
badges = {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0, "checkItemsChecked": 0, "checkItemsEarliestDue": None, "comments": 1, "description": True, "due": None, "dueComplete": False, "externalSource": None, "fogbugz": "", "lastUpdatedByAi": False, "location": False, "maliciousAttachments": 0, "start": None, "votes": 0}
url = f"https://PERSON_6092_TRELLO_USERNAME.com/c/{sl}/{short}-angel-note-money-page"
ins("trello.trello_cards", TC, [card, Q["trello_title"], BOARD["id"], TODO_LIST[0], Q["trello_desc"], 3.0, False, None, False, "[]", "[]", short, None, None, url, T["trello_comment"], None, js(badges)], card)
act = card[:22] + hx("create-action", 2)
ins("trello.trello_actions", TA, [act, "createCard", T["trello"], TR_LEO, BOARD["id"], card, js({"board": BOARD, "card": {"id": card, "idShort": short, "name": Q["trello_title"], "shortLink": sl}, "list": {"id": TODO_LIST[0], "name": TODO_LIST[1]}})], act)
cact = "%08x" % int(ep(T["trello_comment"])) + hx("trello_comment", 16)
_cardref = {"id": card, "idShort": short, "name": Q["trello_title"], "shortLink": sl}
ins("trello.trello_actions", TA, [cact, "commentCard", T["trello_comment"], TR_LEO, BOARD["id"], card, js({"board": BOARD, "card": _cardref, "idCard": card, "list": {"id": TODO_LIST[0], "name": TODO_LIST[1]}, "text": Q["trello_comment"], "textData": {"emoji": {}}})], cact)
upd_raw("trello", f"""UPDATE trello.trello_boards SET "dateLastActivity" = {q(T["trello_comment"])} WHERE id = {q(BOARD["id"])};""", BOARD["id"])
# ---- Gmail
GM = ["id", "thread_id", "user_email", "label_ids_json", "snippet", "internal_date", "date", "size_estimate", "subject", "from_email", "from_name", "to_json", "cc_json", "bcc_json", "reply_to_json", "body_text", "body_html", "headers_json", "in_reply_to", '"references"', "mbox_from", "attachments_meta_json"]
GLOG = {}
addr = lambda e: f"{NAMES[e]} <{e}>" if e in NAMES else e
TZ = {ART: D.timezone(D.timedelta(hours=-5)), LEO: D.timezone(D.timedelta(hours=-8))}
LABEL_TEXT = {"INBOX": "Inbox", "IMPORTANT": "Important", "CATEGORY_PERSONAL": "Category Personal", "SENT": "Sent"}
def mail(key, sender, to, subject, body, at, raw, threads, labels_in=("INBOX", "IMPORTANT", "CATEGORY_PERSONAL"), thread_snip=None, reply_to=None, new_threads=True, snip=None, invite=False, extra_labels=None):
    dt = D.datetime.fromisoformat(at.replace("Z", "+00:00")); ms = int(dt.timestamp() * 1000)
    b = body.replace("\r\n", "\n").replace("\n", "\r\n"); snip = snip or " ".join(body.split())[:175]
    stamp = email.utils.format_datetime(dt if invite else dt.astimezone(TZ[sender]))
    GLOG[key] = {}
    for box, tid in threads.items():
        if new_threads:
            ins("gmail.gmail_threads", ["id", "user_email", "snippet", "history_id"], [tid, box, thread_snip or snip, None], tid)
        mid = f"{box}/{raw}"; labels = ["SENT"] if box == sender else list(labels_in) + list((extra_labels or {}).get(box, []))
        hdrs = [{"name": "X-GM-THRID", "value": tid.split("/")[-1]}, {"name": "X-Gmail-Labels", "value": ",".join(LABEL_TEXT[x] for x in labels if x in LABEL_TEXT)}, {"name": "Delivered-To", "value": box}]
        if invite:
            hdrs += [{"name": "Reply-To", "value": addr(sender)}, {"name": "Sender", "value": "Google Calendar <SVC_0842_EMAIL>"}]
        hdrs += [{"name": "Message-ID", "value": raw}, {"name": "Date", "value": stamp}, {"name": "Subject", "value": subject}, {"name": "From", "value": addr(sender)}, {"name": "To", "value": ", ".join(addr(e) for e in to)}]
        if reply_to:
            hdrs += [{"name": "In-Reply-To", "value": reply_to}, {"name": "References", "value": reply_to}]
        ins("gmail.gmail_messages", GM, [mid, tid, box, js(labels), snip, ms, at, len(b) + 900, subject, sender, NAMES[sender], js([addr(e) for e in to]), "[]", "[]", js([addr(sender)] if invite else []), b, None, js(hdrs), reply_to or "", reply_to or "", None, "[]"], mid)
        GLOG[key][box] = {"message": mid, "thread": tid}
am = MINT["gmail"]["arthur_chase"]
A_BODY = textwrap.fill(Q["arthur_mail"], 76, break_long_words=False, break_on_hyphens=False)
mail("arthur_mail", ART, [LEO, ROB], Q["arthur_subject"], A_BODY, T["arthur"], am["raw"], I["gmail_threads"]["arthur"], thread_snip=Q["leonard_reply"])
LEO_RAW = "<CAPBs_a5" + base64.urlsafe_b64encode(hashlib.sha256((SALT + "leonard_reply").encode()).digest()).decode()[:43] + "@mail.gmail.com>"
QUOTED = "On Fri, Feb 13, 2026 at 8:26 AM arthur blake <arthur.blake@harmonygames.co>\nwrote:\n\n" + "\n".join("> " + x for x in A_BODY.split("\n"))
mail("leonard_reply", LEO, [ART, ROB], "Re: " + Q["arthur_subject"], Q["leonard_reply"] + "\n\n" + QUOTED, T["leonard_reply"], LEO_RAW, I["gmail_threads"]["arthur"], reply_to=am["raw"], new_threads=False, snip=Q["leonard_reply"], extra_labels={ART: ["Label_b19fb8d1b3"]})
# ---- GCal (one copy per attendee) + the invitation in Robert's mail
GC = ["event_id", "calendar_id", "summary", "description", "location", "start_ts", "end_ts", "start_json", "end_json", "organizer_email", "creator_email", "attendees_json", "status", "visibility", "transparency", "rrule_json", "recurring_event_id", "original_start_json", "sequence", "created", "updated", "hangout_link", "ical_uid"]
gc = MINT["gcal"]; ATT = [LEO, ROB, ART]; EVTS = {}; gc["events"][ART] = "evt_" + hx("hold|arthur", 22)
for cal in ATT:
    att = []
    for e in sorted(ATT):
        a = {"email": e, "organizer": e == LEO, "responseStatus": "accepted" if e == LEO else "needsAction"}
        if e == cal: a["self"] = True
        att.append(a)
    ins("gcal.gcal_events", GC, [gc["events"][cal], cal, Q["hold_title"], None, None, T["hold_start"], T["hold_end"], js({"dateTime": T["hold_start"]}), js({"dateTime": T["hold_end"]}), LEO, LEO, js(att), "confirmed", None, "opaque", "[]", None, None, 0, T["hold"], T["hold"], gc["meet"], gc["ical"]], gc["events"][cal])
    EVTS[cal] = gc["events"][cal]
WHEN = "Tue Feb 17, 2026 9am - 10:30am (PST)"
def v4(label):
    h = hx(label, 32)
    return f"<calendar-{h[:8]}-{h[8:12]}-4{h[13:16]}-{'89ab'[int(h[16], 16) % 4]}{h[17:20]}-{h[20:32]}@google.com>"
def invite_body(box, when, zone):
    code = gc["meet"].rsplit("/", 1)[-1]
    eid = base64.b64encode(f"{gc['ical'].split('@')[0][:26]} {box}".encode()).decode().rstrip("=")
    tok = base64.b64encode(f"22#{LEO}{hx('tok|' + box, 40)}".encode()).decode().rstrip("=")
    link = f"https://calendar.google.com/calendar/event?action=VIEW&eid={eid}&tok={tok}&ctz=America%2FLos_Angeles&hl=en&es=1"
    pin = str(int(hx("pin", 12), 16))[:9]; pin2 = str(int(hx("pin2", 16), 16))[:13]
    return (f"{Q['hold_title']}\nTuesday Feb 17, 2026 \u22c5 {when}\n{zone}\n\nJoin with Google Meet\n{gc['meet']}?hs=224\n\n\n\t\nJoin by phone\n(US) [PHONE_42254]\nPIN: {pin}\n\n"
            f"More phone numbers\nhttps://tel.meet/{code}?pin={pin2}&hs=0\n\n\nOrganizer\nLeonard Hayes\n{LEO}\n\nGuests\nLeonard Hayes - organizer\n[PERSON_NAME_0055]\nArthur Blake\n"
            f"View all guest info  \n{link}\n\nReply for {box} and view more details  \n{link}\n\n~~//~~\nInvitation from Google Calendar: https://calendar.google.com/calendar/\n\n"
            "You are receiving this email because you are subscribed to calendar  \nnotifications. To stop receiving these emails, go to  \nhttps://calendar.google.com/calendar/r/settings, select this calendar, and  \nchange \"Other notifications\".\n\n"
            "Forwarding this invitation could allow any recipient to send a response to  \nthe organizer, be added to the guest list, invite others regardless of  \ntheir own invitation status, or modify your RSVP.\n\n"
            "Learn more https://support.google.com/calendar/answer/37135#forwarding")
IN_LABELS = ("INBOX", "CATEGORY_PERSONAL"); TH = I["gmail_threads"]["invite"]
mail("invite", LEO, [ROB, ART], f"Invitation: {Q['hold_title']} @ {WHEN} ([PERSON_NAME_0055])", invite_body(ROB, "9am \u2013 10:30am", "Pacific Time - Los Angeles"), T["invite"], v4("invite|robert"), {ROB: TH[ROB]}, labels_in=IN_LABELS, invite=True)
mail("invite_arthur", LEO, [ART, ROB], f"Invitation: {Q['hold_title']} @ Tue Feb 17, 2026 12pm - 1:30pm (EST) (Arthur Blake)", invite_body(ART, "12pm \u2013 1:30pm", "Eastern Time - New York"), T["invite"], v4("invite|arthur"), {ART: TH[ART]}, labels_in=IN_LABELS, invite=True)
# ---- Contacts
ins("contacts.contacts", ["contact_id", "first_name", "last_name", "is_user", "gender", "status", "job", "email"], [IDS["c_brooks"], "Lauren", "Brooks", False, "Unknown", "Unknown", Q["c_brooks_job"], "lauren@harmonygames.co"], IDS["c_brooks"])
# ---- Linear
proj = IDS["project"]
ins("linear.linear_projects", ["id", "team_id", "name", "summary", "description", "lead_id", "priority", "state", "start_date", "target_date", "labels_json", "links_json", "is_archived", "created_at", "updated_at"],
    [proj, "team_ENG", Q["project_name"], None, Q["project_desc"], LIN["leonard"], 0, "started", "2026-02-12", None, "[]", "[]", False, T["project"], T["project"]], proj)
LI = ["id", "project_id", "team_id", "parent_id", "assignee_id", "creator_id", "state_id", "cycle_id", "identifier", "number", "title", "description", "priority", "estimate", "due_date", "started_at", "completed_at", "canceled_at", "archived_at", "time_in_status_minutes", "labels_json", "links_json", "relations_json", "state_history_json", "is_archived", "created_at", "updated_at"]
LC = ["id", "issue_id", "author_id", "parent_id", "body", "is_edited", "created_at", "updated_at"]
LINROWS = {}; n_note = 0; CLOCK = "2026-02-14T00:00:00Z"; gap = 0
NOTE0 = "2026-02-12T23:36:11Z"; LIMIT = T["ask"]
for n, p in enumerate(C):
    key, spell, sfx = p[0], p[1], p[2]; k = ISS[key]; gap += 0 if n == 0 else 4 + int(hx(f"issue-gap|{n}", 2), 16) % 53; created = plus(T["issue0"], gap)
    desc = f"On the SVB notices as {spell}, account ending {sfx}." if "," not in sfx else f"On the SVB notices as {spell}, accounts ending {sfx}."
    notes = NOTES[key]; rows = []
    for j, nt in enumerate(notes):
        at = plus(NOTE0, 83 * n_note + 17 * (j + 1) + (n_note * 7) % 29); n_note += 1
        cid = "comment_" + hashlib.sha256((SALT + f"note|{k}|{j}").encode()).hexdigest()[:32]
        rows.append({"id": cid, "author": nt["author"], "at": at, "text": nt["text"]})
    last = rows[-1]["at"]; assert created < rows[0]["at"] and last < LIMIT, (k, created, last)
    ins("linear.linear_issues", LI, [k, proj, "team_ENG", None, None, LIN["leonard"], "Backlog", None, k, int(k.split("-")[1]), spell, desc, 0, None, None, None, None, None, None, int((ep(CLOCK) - ep(created)) // 60), "[]", "[]", "[]", "[]", False, created, last], k)
    for r in rows:
        ins("linear.linear_comments", LC, [r["id"], k, LIN[r["author"]], None, r["text"], False, r["at"], r["at"]], r["id"])
    LINROWS[key] = {"issue": k, "created": created, "comments": rows}
upd_raw("linear", f"""UPDATE linear.linear_teams SET issue_counter = {max(int(v.split("-")[1]) for v in ISS.values())} WHERE id = 'team_ENG';""", "team_ENG")
# ---- write
order = ["gdrive", "gdocs", "gsheets", "gslides", "slack", "trello", "gmail", "gcal", "contacts", "linear"]
n_ins = sum(1 for s in OUT for x in OUT[s] if x.startswith("INSERT")); n_upd = sum(1 for s in OUT for x in OUT[s] if x.startswith("UPDATE"))
head = ["-- Are you planning to inject? Yes", f"-- HarmonyGames injection - persona Robert <{ROB}> (Co-Founder & Creative Director), Long Horizon.", f"-- Services: {', '.join(order)}. Statements: {n_ins} INSERT (one row each), {n_upd} UPDATE.", "-- Literal values only; parents before children; re-apply this exact SQL before every agent run.", "BEGIN;"]
body = []
for s in order:
    body.append(f"-- ===================== {s.upper()} ====================="); body += OUT[s]
open(os.path.join(TI, "01_Universe_Inject.sql"), "w").write("\n".join(head + body + ["COMMIT;"]) + "\n")
json.dump({"rows": ROWS, "slack": SLACK, "gmail": GLOG, "gcal": EVTS, "linear": LINROWS, "deck_elements": DECK_EL, "trello": {"card": card, "create_action": act, "idShort": short, "shortLink": sl}, "wording": Q}, open(os.path.join(HERE, "sql_ids.json"), "w"), indent=1)
print(n_ins, n_upd, {k: len(v) for k, v in ROWS.items()})
