#!/usr/bin/env python3
"""Builds task_inputs/01_Universe_Inject.sql for Robert's LLC take-over plan (normal universe, Feb 14, 2026).

Reads plan/ids.json, plan/wording.json and plan/cohort.json (written by plan/build_scenario.py) plus the
injection-level wording below (per-issue notes and native shapes checked against base records through hg.py).
Never executes SQL. Writes the SQL and plan/sql_ids.json (every row id, for the manifest and dossier).
"""
import base64, datetime as D, email.utils, hashlib, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
I = json.load(open(os.path.join(HERE, "ids.json")))
Q = json.load(open(os.path.join(HERE, "wording.json")))
C = json.load(open(os.path.join(HERE, "cohort.json")))
IDS, BASE, T, ISS = I["IDS"], I["BASE"], I["T"], I["issues"]
SALT = "hg-robert-llc-takeover|"

ROB, LEO, ART = "robert@harmonygames.co", "leonard.hayes@harmonygames.co", "arthur.blake@harmonygames.co"
NAMES = {ROB: "robert", LEO: "leonard hayes", ART: "arthur blake"}
SLACK_U = {ROB: "EMPLOYEE_0016_SLACK_ID", LEO: "EMPLOYEE_0038_SLACK_ID", ART: "EMPLOYEE_0025_SLACK_ID"}
LIN = {LEO: "usr_63fffeb4fab5233e", ROB: "usr_Robert", ART: "usr_cc3e90160f490686"}
ROOT = {ROB: "d_9f7ba94f7526d54d8482ba", LEO: "d_63fffeb4fab5233ed5bb73"}          # base Drive roots (drive_files parents)
BOARD = {"id": "640643a3fd8f3ca308d9318e", "name": "Harmony Games", "shortLink": "f4LGcmuh"}
TODO_LIST = ("640643a3fd8f3ca308d93195", "To Do")
TR_LEO = "PERSON_6094_TRELLO_USER_ID"
JENKINS = "SLACK_BOT_0005_SLACK_ID"
REPO = "harmonygames-Games/GameOfDominoes"
GH_ART = "EMPLOYEE_0025_GITHUB_USERNAME"
DD_BRANCH_GH, DD_BRANCH_JENKINS = "arthur.blake/boombitWithEcon", "Blake/boombitWithEcon"   # base branches/981; #builds 2026-01 /1237
DD_BRANCH_SHA = "71a5f99d55e6e050f9ccd53b6b4e3dc7864187bd"
ROOTS = {  # base thread roots the seeded replies sit under (id, ts) — dm_ra 2026-02, #prototype 2026-02
    "arthur_dm": ("bc4bc3d0e2a0ea6ae92cb2a9712e8f76", "1770056235.480619"),
    "vo_status": ("73ec270a3d07eb8d8488384898be079e", "1770404397.819789"),
    "layer_reply": ("bdb4f7af824ec3819acdf5fc3cc480ea", "1770837702.167889"),   # rev4: Leonard's base layer.ai post, #prototype 2026-02 /575 (reply_count 0)
}


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


# ======================================================================== injection-level wording (native shapes)
W = dict(Q)    # all seeded wording lives in plan/wording.json (plan/build_scenario.py), native shapes checked against base records
JOB_URL = "http://blake.tplinkdns.com:9009/job/DD%20iOS%20Submission/218/display/redirect"

# Issue descriptions (bulk-readable: what the item is, never its status or figure) and the owners' notes (per record).
DESC = {
    "Combo Fighter": "The game: code, art and the App Store listing.",
    "Domino Delights": "The game and its store listings.",
    "Zombie Match": "The game and its store listings.",
    "Domino Delights production account (AWS)": "Domino Delights' production AWS account.",
    "Domino Delights dev account (AWS)": "Domino Delights' dev AWS account.",
    "Zombie Match account (AWS)": "Zombie Match's AWS account (dev and prod in one).",
    "Analytics pipeline account (AWS)": "The analytics pipeline's AWS account (Kinesis, Glue, S3).",
    "Combo Fighter backend and auth stacks (AWS)": "Combo Fighter's backend and auth stacks on AWS.",
    "Build machines": "The Android and Apple build machines.",
    "Metabase": "Dashboards.",
    "dbt": "The models behind the dashboards.",
    "GitHub": "Repos and the team plan.",
    "Singular": "Attribution.",
    "AppsFlyer": "Attribution if Singular cuts us off.",
    "Google Analytics": "Analytics property.",
    "Figma": "Design files.",
    "layer.ai": "Art generation.",
    "Soundly": "Sound library.",
    "Kapwing": "Video editing for the ads.",
    "Cursor": "Code editor seats.",
    "CodeRabbit": "PR reviews.",
    "Unity Pro": "Unity licences.",
    "Zapier": "Automations.",
    "Helpshift": "Player support desk for DD and ZM.",
    "Domino Delights player support": "How Domino Delights players reach us once Helpshift is gone.",
    "Slack": "Workspace.",
    "Google Workspace": "Email and Drive accounts.",
    "Linear": "This workspace.",
    "Deel": "Contractor payments.",
    "Gusto": "Payroll and records.",
    "Intuit": "Accounting.",
    "Carta": "Cap table.",
    "Apple developer account": "The Apple developer account.",
    "Google Play developer account": "The Google Play developer account.",
    "Calm Play LLC": "Calm Play LLC.",
    "Unity Ads balance": "What's left on the Unity Ads account.",
    "Playable vendor": "The playable ad vendor.",
}
# (author, note key in wording.json or literal text, time key in T or a literal ISO time)
NOTES = {
    "Combo Fighter": (LEO, "robert's game. all of it is HG's IP today", "2026-02-13T00:24:00Z"),
    "Domino Delights": (LEO, "boombit's test doesn't change anything, the game is ours. I'll handle it with Sunset", "2026-02-13T00:26:00Z"),
    "Zombie Match": (LEO, "both store listings moved over to HG's accounts in july", "2026-02-13T00:28:00Z"),
    "Domino Delights production account (AWS)": (LEO, "@c_dd_prod", "c_dd_prod"),
    "Domino Delights dev account (AWS)": (ART, "nothing runs on dev anymore, shutting it down", "2026-02-13T00:55:00Z"),
    "Zombie Match account (AWS)": (ART, "@c_zm_account", "c_zm_account"),
    "Analytics pipeline account (AWS)": (ART, "kinesis and glue only ever carried DD and ZM events, CF's go through firebase. shutting it down",
                                         "2026-02-13T01:01:00Z"),
    "Combo Fighter backend and auth stacks (AWS)": (ART, "@c_cf_backend", "c_cf_backend"),
    "Build machines": (ART, "@c_build", "c_build"),
    "Metabase": (LEO, "@c_metabase", "c_metabase"),
    "dbt": (LEO, "same as metabase, the two go together", "2026-02-13T00:53:00Z"),
    "GitHub": (LEO, "we keep it under HG until the data is sold, then the repos transfer", "2026-02-13T00:54:00Z"),
    "Singular": (LEO, "termination letter is the one in #winddown. they deferred our last quarterly payment, still waiting on them",
                 "2026-02-13T00:31:00Z"),
    "AppsFlyer": (LEO, "singular is getting terminated, so CF goes on appsflyer's free tier from March. free up to 15K installs, no cost aggregation or user level data. I'll set CF up on it",
                  "2026-02-13T00:33:00Z"),
    "Google Analytics": (LEO, "stays under HG until the data is extracted, nothing for the LLC to take or pay", "2026-02-13T00:35:00Z"),
    "Figma": (LEO, "@c_figma", "c_figma"),
    "layer.ai": (LEO, Q["c_layer"], "c_layer"),   # rev4 (RB4): the note states only the cancellation (literal text keeps the rev3 comment id)
    "Soundly": (LEO, "robert cancelled it on the 11th", "2026-02-13T00:38:00Z"),
    "Kapwing": (ART, "@c_kapwing", "c_kapwing"),
    "Cursor": (ART, "cancelled the seats on the 12th", "2026-02-13T01:32:00Z"),
    "CodeRabbit": (ART, "cancelled on the 12th", "2026-02-13T01:33:00Z"),
    "Unity Pro": (ART, "termination note to unity goes out from me, leonard's draft from #winddown. CF is fine on unity personal", "2026-02-13T01:36:00Z"),
    "Zapier": (LEO, "cancelled", "2026-02-13T00:39:00Z"),
    "Helpshift": (LEO, "they're cancelling without a hassle. DD and ZM have to be off it before Feb 28th. CF was never on it, its support is the contact on its store listing and that moves with the game", "2026-02-13T00:41:00Z"),
    "Domino Delights player support": (ART, "@c_support", "c_support"),
    "Slack": (LEO, "down to the three of us as paid members, everyone else is a single channel guest. we keep it for the data", "2026-02-13T00:42:00Z"),
    "Google Workspace": (LEO, "archiving the unused accounts after Feb 15", "2026-02-13T00:43:00Z"),
    "Linear": (LEO, "keeping it during the transition", "2026-02-13T00:44:00Z"),
    "Deel": (LEO, "keeping it during the shutdown", "2026-02-13T00:45:00Z"),
    "Gusto": (LEO, "keeping it during the shutdown, we need it for the docs", "2026-02-13T00:46:00Z"),
    "Intuit": (LEO, "keeping it for the next two months", "2026-02-13T00:47:00Z"),
    "Carta": (LEO, "renewal is 8/15 and it's tied to the closed chase account, no rush", "2026-02-13T00:49:00Z"),
    "Apple developer account": (LEO, "HG's account. CF's listing sits in it and moves with the game", "2026-02-13T01:12:00Z"),
    "Google Play developer account": (LEO, "HG's account, one-time fee, nothing monthly", "2026-02-13T01:13:00Z"),
    "Calm Play LLC": (LEO, "@c_calm", "c_calm"),
    "Unity Ads balance": (LEO, "the $100 left on it goes on this week's playable test, then nothing", "2026-02-13T01:15:00Z"),
    "Playable vendor": (LEO, "$3,750 for the first playable, one-off", "2026-02-13T01:16:00Z"),
}
ISSUE_ITEMS = [m for m in C if m["issue"]]
assert set(NOTES) == {m["key"] for m in ISSUE_ITEMS} == set(DESC), set(NOTES) ^ {m["key"] for m in ISSUE_ITEMS}

# ======================================================================== Drive / Docs / Sheets / Slides
DF_COLS = ["id", "name", "mime_type", "parents_json", "owner_email", "shared_with_emails_json", "shared_roles_json",
           "visibility", "owners_json", "modified_time", "created_time", "trashed", "starred"]
DOC, SHEET, SLIDES = ("application/vnd.google-apps.document", "application/vnd.google-apps.spreadsheet",
                      "application/vnd.google-apps.presentation")


def drive(fid, name, mime, owner, shares, created, modified):
    ins("gdrive.drive_files", DF_COLS, [fid, name, mime, js([ROOT[owner]]), owner, js([e for e in shares]),
                                        js([{"email": e, "role": "writer"} for e in shares]), "private", js([owner]),
                                        modified, created, False, False], fid)


def gdoc(fid, text, owner, shares, at):
    title = text.split("\n", 1)[0]
    body = text.rstrip("\n") + "\n"
    drive(fid, title, DOC, owner, shares, at, at)
    tl = len(title) + 1
    runs = [{"start": 0, "end": tl, "named_style": "TITLE", "list_id": None, "list_nesting": 0},
            {"start": tl, "end": len(body), "named_style": "NORMAL_TEXT", "list_id": None, "list_nesting": 0}]
    ins("gdocs.docs_documents", ["document_id", "title", "owner_email", "shared_with_emails_json", "visibility", "body_text",
                                 "style_runs_json", "revision_id", "drive_file_id", "created_time", "modified_time"],
        [fid, title, owner, js(shares), "private", body, js(runs), hx("rev" + fid, 10), fid, at, at], fid)
    return title


FOUNDERS = [ROB, ART]
GR_TITLE = gdoc(IDS["ground_rules"], W["ground_rules"], LEO, FOUNDERS, T["ground_rules"])
NOTES_TITLE = gdoc(IDS["notes_doc"], W["notes_doc"], LEO, FOUNDERS, T["notes_doc"])

ds = IDS["draft_sheet"]
DRAFT_TITLE = "LLC 90 days (draft)"
drive(ds, DRAFT_TITLE, SHEET, LEO, FOUNDERS, T["draft_sheet"], T["draft_sheet"])
ins("gsheets.sheets_spreadsheets", ["spreadsheet_id", "title", "owner_email", "shared_with_emails_json", "visibility",
                                    "drive_file_id", "created_time", "modified_time"],
    [ds, DRAFT_TITLE, LEO, js(FOUNDERS), "private", ds, T["draft_sheet"], T["draft_sheet"]], ds)
grid = [W["draft_header"]] + [list(r) for r in W["draft_rows"]]
ins("gsheets.sheets_sheets", ["spreadsheet_id", "sheet_id", "title", '"index"', "row_count", "column_count", "grid_json"],
    [ds, 0, "Sheet1", 0, 1000, 26, js(grid)], f"{ds}#0")

deck = IDS["cf_deck"]
DECK_TITLE = W["cf_deck"][0]
drive(deck, DECK_TITLE, SLIDES, ROB, [LEO, ART], T["cf_deck"], T["cf_deck"])
ins("gslides.slides_presentations", ["presentation_id", "title", "owner_email", "shared_with_emails_json", "visibility",
                                     "drive_file_id", "revision_id", "created_time", "modified_time"],
    [deck, DECK_TITLE, ROB, js([LEO, ART]), "private", deck, hx("rev" + deck, 10), T["cf_deck"], T["cf_deck"]], deck)
DECK_EL = []
for n, text in enumerate(W["cf_deck"]):
    pid, eid = "slide_" + hx(f"deck-page-{n}", 12), "el_" + hx(f"deck-el-{n}", 12)
    ins("gslides.slides_pages", ["presentation_id", "object_id", '"index"', "layout", "notes"], [deck, pid, n, "BLANK", None], f"{deck}#{pid}")
    ins("gslides.slides_page_elements", ["presentation_id", "page_object_id", "object_id", "kind", "text", "placeholder_type",
                                         "x_emu", "y_emu", "width_emu", "height_emu", "table_json", "ordinal"],
        [deck, pid, eid, "TEXT_BOX", text, None, 0, 0, 9144000, 5143500, None, 0], f"{deck}#{eid}")
    DECK_EL.append(f"{deck}#{eid}")

# ======================================================================== Slack
SL_COLS = ["id", "ts", "channel_id", "type", "user_id", "text", "thread_parent_id", "thread_ts_legacy", "reply_count",
           "reply_users_count", "latest_reply", "is_activity_message", "subtype", "reactions_json", "files_json",
           "attachments_json", "created_at", "metadata_json"]
SLACK = {}


def slack(key, user, text, parent=None, attachments=None):
    channel, ts = IDS[key].split("/")
    mid = slack_id(channel, ts)
    ins("slack.slack_messages", SL_COLS, [mid, ts, channel, "message", user, text, parent[0] if parent else None,
                                          parent[1] if parent else None, 0, 0, None, False, None, "[]", "[]",
                                          js(attachments or []), iso_of(float(ts)), "{}"], IDS[key])
    if parent:
        upd("slack.slack_messages", {"thread_ts_legacy": parent[1], "reply_count": 1, "reply_users_count": 1, "latest_reply": ts},
            "id", parent[0])
    SLACK[key] = {"id": mid, "ts": ts, "channel": channel, "locator": IDS[key]}


def jenkins(text, color):
    return [{"color": color, "fallback": text, "fields": [{"short": False, "title": "", "value": text}], "id": 1,
             "mrkdwn_in": ["fields", "pretext", "text"]}]


slack("builds_start", JENKINS, "", attachments=jenkins(W["builds_start_text"], "2eb886"))
slack("builds_result", JENKINS, "", attachments=jenkins(W["builds_result_text"], "2eb886"))
slack("vo_status", SLACK_U[LEO], W["vo_status"], parent=ROOTS["vo_status"])
slack("layer_reply", SLACK_U[LEO], W["layer_reply"], parent=ROOTS["layer_reply"])   # rev4 (RB4); the helper updates the parent's thread fields
slack("arthur_dm", SLACK_U[ART], W["arthur_dm"], parent=ROOTS["arthur_dm"])
slack("hub", SLACK_U[LEO], W["hub"])

# ======================================================================== Trello (Leonard's card on the founders' board)
TC_COLS = ["id", "name", '"idBoard"', '"idList"', '"desc"', "pos", "closed", "due", '"dueComplete"', '"idMembers_json"',
           '"idLabels_json"', '"idShort"', '"shortLink"', '"shortUrl"', "url", '"dateLastActivity"', "cover_json", "badges_json"]
TA_COLS = ["id", "type", "date", '"idMemberCreator"', '"idBoard"', '"idCard"', "data_json"]
card, card_at, card_name, short = IDS["trello_card"], T["trello_card"], "LLC: what we take from HG", 456   # board's last idShort is 455
sl = base64.b64encode(hashlib.sha256((SALT + card).encode()).digest()).decode().replace("+", "x").replace("/", "Q")[:8]
badges = {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0, "checkItemsChecked": 0,
          "checkItemsEarliestDue": None, "comments": 0, "description": True, "due": None, "dueComplete": False,
          "externalSource": None, "fogbugz": "", "lastUpdatedByAi": False, "location": False, "maliciousAttachments": 0,
          "start": None, "votes": 0}
url = f"https://PERSON_6092_TRELLO_USERNAME.com/c/{sl}/{short}-llc-what-we-take-from-hg"
ins("trello.trello_cards", TC_COLS, [card, card_name, BOARD["id"], TODO_LIST[0], W["trello_desc"], 3.0, False, None, False,
                                     "[]", "[]", short, None, None, url, card_at, None, js(badges)], card)
act = "%08x" % int(ep(card_at)) + hx("llc_card_create", 16)
ins("trello.trello_actions", TA_COLS, [act, "createCard", card_at, TR_LEO, BOARD["id"], card, js(
    {"board": BOARD, "card": {"id": card, "idShort": short, "name": card_name, "shortLink": sl},
     "list": {"id": TODO_LIST[0], "name": TODO_LIST[1]}})], act)

# ======================================================================== Gmail
GM_COLS = ["id", "thread_id", "user_email", "label_ids_json", "snippet", "internal_date", "date", "size_estimate", "subject",
           "from_email", "from_name", "to_json", "cc_json", "bcc_json", "reply_to_json", "body_text", "body_html",
           "headers_json", "in_reply_to", '"references"', "mbox_from", "attachments_meta_json"]
GLOG = {}


def addr(e, names=NAMES):
    return f"{names[e]} <{e}>" if e in names else e


def gmail_id(label):
    return "<CA" + base64.urlsafe_b64encode(hashlib.sha256((SALT + label).encode()).digest()).decode()[:38] + "@mail.gmail.com>"


def thread_id(label, box, at):
    return str(((int(ep(at)) * 1000) << 20) + (int(hx(label + "|" + box, 8), 16) & 0xFFFFF))


def mail(key, sender, to, cc, subject, body, at, raw_id, boxes, from_name=None, to_hdr=None, labels_in=("INBOX", "IMPORTANT", "CATEGORY_PERSONAL"),
         fixed_thread=None, attachments=None):
    dt = D.datetime.fromisoformat(at.replace("Z", "+00:00"))
    ms = int(dt.timestamp() * 1000)
    b = body.replace("\r\n", "\n").replace("\n", "\r\n")
    snippet = " ".join(body.split())[:140]
    fname = from_name or NAMES.get(sender, sender)
    hdrs = [{"name": "Message-ID", "value": raw_id}, {"name": "Date", "value": email.utils.format_datetime(dt)},
            {"name": "Subject", "value": subject}, {"name": "From", "value": f"{fname} <{sender}>"},
            {"name": "To", "value": to_hdr or ", ".join(addr(e) for e in to)}]
    if cc:
        hdrs.append({"name": "Cc", "value": ", ".join(addr(e) for e in cc)})
    GLOG[key] = {}
    for box in boxes:
        tid = f"{box}/" + ((fixed_thread or {}).get(box) or thread_id(key, box, at))
        ins("gmail.gmail_threads", ["id", "user_email", "snippet", "history_id"], [tid, box, snippet, None], tid)
        mid = f"{box}/{raw_id}"
        labels = ["SENT"] if box == sender else list(labels_in)
        ins("gmail.gmail_messages", GM_COLS,
            [mid, tid, box, js(labels), snippet, ms, at, len(b) + 900, subject, sender, fname,
             js([addr(e) for e in to]), js([addr(e) for e in cc]), "[]", "[]", b, None, js(hdrs), None, None, None,
             js(attachments or [])], mid)
        GLOG[key][box] = {"message": mid, "thread": tid}


def robert_thread(key):
    return {ROB: IDS[key].split("/", 1)[1]}


mail("arthur_mail", ART, [ROB, LEO], [], W["arthur_subject"], W["arthur_mail"], T["arthur_mail"], gmail_id("arthur_mail"),
     [ART, ROB, LEO], fixed_thread=robert_thread("arthur_thread"))
mail("split_mail", LEO, [ROB], [ART], W["split_subject"], W["split_mail"], T["split_mail"], gmail_id("split_mail"),
     [LEO, ROB, ART], fixed_thread=robert_thread("split_thread"))
mail("jenkins_mail", ART, [ROB], [LEO], W["jenkins_subject"], W["jenkins_mail"], T["jenkins_mail"], gmail_id("jenkins_mail"),
     [ART, ROB, LEO], fixed_thread=robert_thread("jenkins_thread"))   # rev4 (RB5): CF's stacks at $62 now, second paragraph
asc_ms = int(ep(T["asc_notice"]) * 1000)
ASC_SID = str(int(hx("asc-sid", 6), 16) % 90000 + 30000)
for box in (ROB, ART, LEO):        # App Review mails each team member separately (one message per mailbox, own Message-ID)
    tag = "" if box == ROB else "|" + box
    raw = (f"<{int(hx('asc-a' + tag, 8), 16) % 10**9}.{int(hx('asc-b' + tag, 8), 16) % 10**9}."
           f"{asc_ms + (0 if box == ROB else int(hx('asc-ms' + tag, 3), 16) % 900)}@email.apple.com>")
    greet = {ROB: "[PERSON_NAME_0054]", ART: "Arthur", LEO: "Leonard"}[box]       # base copies greet each recipient
    labels = {ROB: ("INBOX", "CATEGORY_UPDATES", "Label_ad4e31dc09", "Label_aeb79a643f"),   # robert threads/00014520.json
              ART: ("INBOX", "CATEGORY_UPDATES", "UNREAD"),                                   # blake@..._1838693712455374094.json
              LEO: ("ARCHIVED", "CATEGORY_UPDATES", "Label_6e8d84b057")}[box]                 # leonard@..._1838693748302395744.json
    mail("asc_notice" + tag, "SVC_4131_EMAIL", [box], [], W["asc_subject"],
         W["asc_body"].replace("{sid}", ASC_SID).replace("Hello [PERSON_NAME_0054],", f"Hello {greet},"),
         T["asc_notice"], raw, [box], from_name="SVC_4131_NAME", to_hdr=box,
         labels_in=labels,
         fixed_thread=robert_thread("asc_thread") if box == ROB else None)

# ======================================================================== GCal (one copy per attendee calendar) + INT-11 invitations
GC_COLS = ["event_id", "calendar_id", "summary", "description", "location", "start_ts", "end_ts", "start_json", "end_json",
           "organizer_email", "creator_email", "attendees_json", "status", "visibility", "transparency", "rrule_json",
           "recurring_event_id", "original_start_json", "sequence", "created", "updated", "hangout_link", "ical_uid"]
EV_SUMMARY, EV_START = "LLC: decide", T["monday_start"]
EV_END = plus(EV_START, 45 * 60)
ICAL = hx("monday_call_ical", 32) + "@hg4"
MEET = "https://meet.google.com/" + hx("meet1", 3) + "-" + hx("meet2", 4) + "-" + hx("meet3", 3)
ATT = [LEO, ROB, ART]
EVTS = {}
for cal in ATT:
    eid = IDS["monday_evt"] if cal == LEO else "evt_" + hx("monday_call|" + cal, 22)
    att = []
    for e in ATT:
        a = {"email": e, "organizer": e == LEO, "responseStatus": "accepted" if e == LEO else "needsAction"}
        if e == cal:
            a["self"] = True
        att.append(a)
    ins("gcal.gcal_events", GC_COLS, [eid, cal, EV_SUMMARY, W["monday_desc"], None, EV_START, EV_END, js({"dateTime": EV_START}),
                                      js({"dateTime": EV_END}), LEO, LEO, js(att), "confirmed", None, "opaque", "[]", None, None,
                                      0, T["monday_created"], T["monday_created"], MEET, ICAL], eid)
    EVTS[cal] = eid
inv_at = plus(T["monday_created"], 3)
TZ = {ROB: ("Mon Feb 16, 2026 10am - 10:45am (PST)", "Monday Feb 16, 2026 \u22c5 10am \u2013 10:45am\nPacific Time - Los Angeles", "[PERSON_NAME_0055]"),
      ART: ("Mon Feb 16, 2026 1pm - 1:45pm (EST)", "Monday Feb 16, 2026 \u22c5 1pm \u2013 1:45pm\nEastern Time - New York", "Arthur Blake")}
for box in (ROB, ART):          # base invitations render in the recipient's calendar timezone and display name (robert threads/00016854.json; blake@..._1856867715191204796.json)
    when, slot_text, rname = TZ[box]
    u = hx("invite-uuid|" + box, 32)
    raw = f"<calendar-{u[:8]}-{u[8:12]}-{u[12:16]}-{u[16:20]}-{u[20:32]}@google.com>"
    subj = f"Invitation: {EV_SUMMARY} @ {when} ({rname})"
    body = (f"{EV_SUMMARY}\n{slot_text}\n\n{W['monday_desc']}\n\n"
            f"Join with Google Meet\n{MEET}\n\nOrganizer\n{LEO}\n\nGuests\n{LEO} - organizer\n{ROB}\n{ART}\nView all guest info")
    mail("invite|" + box, LEO, [box], [], subj, body, inv_at, raw, [box], to_hdr=box, labels_in=("INBOX", "CATEGORY_PERSONAL"),
         attachments=[{"attachment_id": "att_0001", "content_type": "application/ics", "filename": "invite.ics", "size_bytes": 1982}])

# ======================================================================== GitHub (GameOfDominoes #1917, merged)
pr_id = IDS["pr"]
head_ref, head_ref_pr = "arthur.blake/supportEmail", "Blake/supportEmail"   # branches table vs PR refs (NB-13 form split, as in base)
head_sha, merge_sha = hx("pr1917-head", 40), hx("pr1917-merge", 40)
ins("github.github_pull_requests",
    ["id", "repo_id", "number", "title", "state", "merged", "draft", "locked", "author_login", "merged_by_login", "body",
     "base_ref", "head_ref", "base_sha", "head_sha", "merge_commit_sha", "additions", "deletions", "changed_files",
     "labels_json", "assignee_logins_json", "requested_reviewer_logins_json", "created_at", "updated_at", "merged_at",
     "closed_at", "html_url"],
    [pr_id, REPO, 1917, W["pr_title"], "closed", True, False, False, GH_ART, GH_ART, W["pr_body"], DD_BRANCH_JENKINS, head_ref_pr,
     DD_BRANCH_SHA, head_sha, merge_sha, 64, 211, 9, "[]", "[]", "[]", T["pr_open"], T["pr_merge"], T["pr_merge"], T["pr_merge"], None], pr_id)
ins("github.github_branches", ["id", "repo_id", "name", "head_sha", "protected", "is_default"],
    [f"{REPO}:{head_ref}", REPO, head_ref, head_sha, False, False], f"{REPO}:{head_ref}")
ins("github.github_commits", ["sha", "repo_id", "message", "authored_date", "committed_date", "author_login", "author_name",
                              "author_email", "committer_login", "committer_name", "committer_email", "parent_shas_json"],
    [head_sha, REPO, "Replace Helpshift with support email", plus(T["pr_open"], -1500), plus(T["pr_open"], -1500), GH_ART,
     "arthur blake", "EMPLOYEE_0025_GITHUB_NOREPLY_EMAIL_0001", GH_ART, "arthur blake", "EMPLOYEE_0025_GITHUB_NOREPLY_EMAIL_0001",
     js([DD_BRANCH_SHA])], head_sha)
ins("github.github_commits", ["sha", "repo_id", "message", "authored_date", "committed_date", "author_login", "author_name",
                              "author_email", "committer_login", "committer_name", "committer_email", "parent_shas_json"],
    [merge_sha, REPO, f"Merge pull request #1917 from harmonygames-Games/{head_ref_pr}\n\n{W['pr_title']}", T["pr_merge"], None, GH_ART,
     "arthur blake", "EMPLOYEE_0025_GITHUB_NOREPLY_EMAIL_0001", "", "SVC_0181_NAME", "SVC_0181_EMAIL", "[]"], merge_sha)   # base merge shape: commits/4580
ins("github.github_pull_request_commits", ["id", "pr_id", "commit_sha", "position"], [f"{pr_id}#c_0", pr_id, head_sha, 0], f"{pr_id}#c_0")
for n, ev in ((1, "merged"), (2, "closed")):
    ins("github.github_timeline_events", ["id", "pr_id", "event", "actor_login", "created_at", "data_json"],
        [f"{pr_id}#ev_{n}", pr_id, ev, GH_ART, T["pr_merge"], js({"commit_id": merge_sha} if ev == "merged" else {})], f"{pr_id}#ev_{n}")

# ======================================================================== Linear (project, 37 issues, the owners' notes)
proj = IDS["project"]
ins("linear.linear_projects", ["id", "team_id", "name", "summary", "description", "lead_id", "priority", "state", "start_date",
                               "target_date", "labels_json", "links_json", "is_archived", "created_at", "updated_at"],
    [proj, "team_ENG", "LLC take-over", None, W["project_desc"], LIN[LEO], 0, "started", "2026-02-12", None, "[]", "[]", False,
     T["project"], T["project"]], proj)
# linear_project_teams / linear_project_members are not writable (Injection Schema Guideline 2026-10-22)

LI_COLS = ["id", "project_id", "team_id", "parent_id", "assignee_id", "creator_id", "state_id", "cycle_id", "identifier",
           "number", "title", "description", "priority", "estimate", "due_date", "started_at", "completed_at", "canceled_at",
           "archived_at", "time_in_status_minutes", "labels_json", "links_json", "relations_json", "state_history_json",
           "is_archived", "created_at", "updated_at"]
LC_COLS = ["id", "issue_id", "author_id", "parent_id", "body", "is_edited", "created_at", "updated_at"]
LINROWS = {}
for n, m in enumerate(ISSUE_ITEMS):
    k = m["linear"]
    created = plus(T["issue0"], 20 * n)
    who, body, when = NOTES[m["key"]]
    text = W[body[1:]] if body.startswith("@") else body
    at = T[when] if when in T else when
    cid = IDS[body[1:]] if body.startswith("@") else "comment_" + hx("note|" + m["key"], 32)
    assert created < at < "2026-02-14", (k, created, at)
    ins("linear.linear_issues", LI_COLS,
        [k, proj, "team_ENG", None, None, LIN[LEO], "Backlog", None, k, int(k.split("-")[1]), m["key"], DESC[m["key"]], 0,
         None, None, None, None, None, None, None, "[]", "[]", "[]", "[]", False, created, at], k)
    ins("linear.linear_comments", LC_COLS, [cid, k, LIN[who], None, text, False, at, at], cid)
    LINROWS[m["key"]] = {"issue": k, "comment": cid, "author": who, "at": at, "created": created, "text": text}

# ======================================================================== write
order = ["gdrive", "gdocs", "gsheets", "gslides", "slack", "trello", "gmail", "gcal", "github", "linear"]
n_ins = sum(1 for s in OUT for x in OUT[s] if x.startswith("INSERT"))
n_upd = sum(1 for s in OUT for x in OUT[s] if x.startswith("UPDATE"))
head = ["-- Are you planning to inject? Yes",
        f"-- HarmonyGames injection - persona Robert <{ROB}> (Co-Founder & Creative Director), Long Horizon.",
        f"-- Services: {', '.join(order)}. Statements: {n_ins} INSERT (one row each), {n_upd} UPDATE.",
        "-- Literal values only; parents before children; re-apply this exact SQL before every agent run.", "BEGIN;"]
body = []
for s in order:
    body.append(f"-- ===================== {s.upper()} =====================")
    body += OUT[s]
open(os.path.join(TI, "01_Universe_Inject.sql"), "w").write("\n".join(head + body + ["COMMIT;"]) + "\n")
json.dump({"rows": ROWS, "slack": SLACK, "gmail": GLOG, "gcal": EVTS, "linear": LINROWS, "deck_elements": DECK_EL,
           "trello": {"card": card, "create_action": act, "idShort": short, "shortLink": sl},
           "github": {"pr": pr_id, "head_sha": head_sha, "merge_sha": merge_sha, "head_ref": head_ref},
           "titles": {"ground_rules": GR_TITLE, "notes_doc": NOTES_TITLE, "draft_sheet": DRAFT_TITLE, "deck": DECK_TITLE},
           "wording": W}, open(os.path.join(HERE, "sql_ids.json"), "w"), indent=1)
print(n_ins, n_upd, {k: len(v) for k, v in ROWS.items()})
