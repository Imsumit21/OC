"""Per-service SQL emitters. Each function returns a list of statements; all values come from data.py."""
import json

import data as D


class Raw(str):
    """A SQL expression emitted as is (not quoted)."""


def q(v):
    """SQL literal."""
    if isinstance(v, Raw):
        return str(v)
    if v is None:
        return "NULL"
    if v is True:
        return "true"
    if v is False:
        return "false"
    if isinstance(v, (int, float)):
        return repr(v)
    s = str(v).replace("'", "''")
    if "\n" in s or "\r" in s or "\\" in s:
        s = s.replace("\\", "\\\\").replace("\r", "\\r").replace("\n", "\\n")
        return f"E'{s}'"
    return f"'{s}'"


def j(v):
    return json.dumps(v, ensure_ascii=False)


def ins(table, cols, vals):
    c = ", ".join(f'"{x}"' if (x in ("references", "desc", "index") or any(ch.isupper() for ch in x)) else x for x in cols)
    return f"INSERT INTO {table} ({c})\nVALUES ({', '.join(q(v) for v in vals)});"


def drive_row(fid, name, mime, parent, owner, shares, when_created, when_modified, role="reader"):
    return ins("gdrive.drive_files",
               ["id", "name", "mime_type", "parents_json", "owner_email", "shared_with_emails_json", "shared_roles_json",
                "visibility", "owners_json", "modified_time", "created_time", "trashed", "starred"],
               [fid, name, mime, j([parent]), owner, j(shares), j([{"email": e, "role": role} for e in shares]),
                "private", j([owner]), when_modified, when_created, False, False])


def doc_row(fid, title, owner, shares, body, created, modified, rev=None):
    n = len(title) + 1
    runs = [{"start": 0, "end": n, "named_style": "TITLE", "list_id": None, "list_nesting": 0},
            {"start": n, "end": len(body), "named_style": "NORMAL_TEXT", "list_id": None, "list_nesting": 0}]
    return ins("gdocs.docs_documents",
               ["document_id", "title", "owner_email", "shared_with_emails_json", "visibility", "body_text",
                "style_runs_json", "revision_id", "drive_file_id", "created_time", "modified_time"],
               [fid, title, owner, j(shares), "private", body, j(runs), rev or D.hexid(fid + "rev", 10), fid, created, modified])


GOOGLE_DOC = "application/vnd.google-apps.document"
GOOGLE_SHEET = "application/vnd.google-apps.spreadsheet"
GOOGLE_SLIDES = "application/vnd.google-apps.presentation"

GATE = D.PR["R2_gate_doc"]
LOGN = D.PR["R6_log_note"]
DECK = D.PR["audience_deck"]
GATE_SHARES = [D.JULIA.email, D.ROBERT.email, D.BRIAN.email, D.VINCENT.email]
TEAM_SHARES = [D.LEONARD.email, D.ROBERT.email]
WORKBOOK_CREATED, WORKBOOK_MODIFIED = "2025-09-30T16:21:47Z", "2025-09-30T19:44:12Z"
DECK_CREATED = "2025-09-24T17:02:15Z"
LOG_CREATED = "2025-09-30T16:24:03Z"
KPI_CREATED, KPI_MODIFIED = "2025-09-24T10:48:33Z", "2025-09-24T11:15:08Z"


def emit_gdrive():
    out = [drive_row(GATE["id"], GATE["title"], GOOGLE_DOC, D.LEONARD.root, D.LEONARD.email, GATE_SHARES,
                     "2025-09-24T15:12:40Z", GATE["at"]),
           drive_row(LOGN["id"], D.LOG_NOTE_TITLE, GOOGLE_DOC, LOGN["parent"], D.JULIA.email, TEAM_SHARES,
                     LOG_CREATED, LOGN["at"]),
           drive_row(DECK["id"], DECK["title"], GOOGLE_SLIDES, D.JULIA.root, D.JULIA.email, TEAM_SHARES + [D.BRIAN.email],
                     DECK_CREATED, DECK["at"]),
           drive_row(D.WORKBOOK, D.WORKBOOK_TITLE, GOOGLE_SHEET, D.JULIA.root, D.JULIA.email, TEAM_SHARES,
                     WORKBOOK_CREATED, WORKBOOK_MODIFIED),
           drive_row(D.KPI_SHEET, D.KPI_TITLE, GOOGLE_SHEET, D.VINCENT.root, D.VINCENT.email,
                     [D.JULIA.email, D.ROBERT.email, D.LEONARD.email], KPI_CREATED, KPI_MODIFIED)]
    for v in D.SESSION_VIEWS:
        p = D.PEOPLE[v["observer"]]
        out.append(drive_row(v["notes_doc"], v["title"], GOOGLE_DOC, p.root, p.email, [D.JULIA.email],
                             v["doc_time"], v["doc_time"]))
    return out


def emit_gdocs():
    out = [doc_row(GATE["id"], GATE["title"], D.LEONARD.email, GATE_SHARES, D.GATE_DOC, "2025-09-24T15:12:40Z", GATE["at"],
                   rev="c4e19b7a02"),
           doc_row(LOGN["id"], D.LOG_NOTE_TITLE, D.JULIA.email, TEAM_SHARES, D.LOG_NOTE, LOG_CREATED, LOGN["at"])]
    for v in D.SESSION_VIEWS:
        p = D.PEOPLE[v["observer"]]
        out.append(doc_row(v["notes_doc"], v["title"], p.email, [D.JULIA.email], D.notes_body(v), v["doc_time"], v["doc_time"]))
    return out


def emit_gsheets():
    log = [["ticket", "session date", "form date", "observer", "audience", "stars", "notes doc"]]
    for v in D.SESSION_VIEWS:
        log.append([v["ticket"], v["session_date"], D.FORMS[v["form"]]["form_at"][:10], v["observer"],
                    "RPG" if v["audience"] == "rpg" else "casual", f"{v['rating']:g}", v["title"]])
    register = [["Register: one row per session"], ["ticket", "audience", "stars", "verdict", "reason"]]
    kpi = [["cohort week", "platform", "installs", "d1 %", "d7 %"]]
    for r in D.KPI_ROWS:
        kpi.append([r["cohort_week"], r["platform"], str(r["installs"]), f"{r['d1_ret']:.2f}", f"{r['d7_ret']:.2f}"])
    mean = sum(r["d7_ret"] for r in D.KPI_ROWS) / len(D.KPI_ROWS)
    kpi.append(["D7 mean", "", "", "", f"{mean:.2f}"])
    out = []
    sp = ["spreadsheet_id", "title", "owner_email", "shared_with_emails_json", "visibility", "drive_file_id", "created_time", "modified_time"]
    sh = ["spreadsheet_id", "sheet_id", "title", "index", "row_count", "column_count", "grid_json"]
    out.append(ins("gsheets.sheets_spreadsheets", sp, [D.WORKBOOK, D.WORKBOOK_TITLE, D.JULIA.email, j(TEAM_SHARES), "private",
                                                       D.WORKBOOK, WORKBOOK_CREATED, WORKBOOK_MODIFIED]))
    out.append(ins("gsheets.sheets_sheets", sh, [D.WORKBOOK, 0, "Log", 0, 1000, 26, j(log)]))
    out.append(ins("gsheets.sheets_sheets", sh, [D.WORKBOOK, 1, "Register", 1, 1000, 26, j(register)]))
    shares = [D.JULIA.email, D.ROBERT.email, D.LEONARD.email]
    out.append(ins("gsheets.sheets_spreadsheets", sp, [D.KPI_SHEET, D.KPI_TITLE, D.VINCENT.email, j(shares), "private",
                                                       D.KPI_SHEET, KPI_CREATED, KPI_MODIFIED]))
    out.append(ins("gsheets.sheets_sheets", sh, [D.KPI_SHEET, 0, "KPI", 0, 1000, 26, j(kpi)]))
    return out


def emit_gslides():
    pid = DECK["id"]
    shares = TEAM_SHARES + [D.BRIAN.email]
    out = [ins("gslides.slides_presentations",
               ["presentation_id", "title", "owner_email", "shared_with_emails_json", "visibility", "drive_file_id",
                "revision_id", "created_time", "modified_time"],
               [pid, DECK["title"], D.JULIA.email, j(shares), "private", pid, D.hexid(pid + "rev", 10), DECK_CREATED, DECK["at"]])]
    for i, texts in enumerate(D.DECK_SLIDES):
        page = "slide_" + D.hexid(f"{pid}p{i}", 12)
        out.append(ins("gslides.slides_pages", ["presentation_id", "object_id", "index", "layout", "notes"],
                       [pid, page, i, "BLANK", None]))
        for k, t in enumerate(texts):
            out.append(ins("gslides.slides_page_elements",
                           ["presentation_id", "page_object_id", "object_id", "kind", "text", "placeholder_type", "x_emu",
                            "y_emu", "width_emu", "height_emu", "table_json", "ordinal"],
                           [pid, page, "el_" + D.hexid(f"{pid}e{i}{k}", 12), "TEXT_BOX", t, None, 0, 0, 9144000, 5143500, None, k]))
    return out


def emit_gcal():
    e = D.PR["friday_event"]
    out = []
    for evt, cal in ((D.CLAIRE_EVT, D.CLAIRE.email), (e["id"], D.JULIA.email)):
        att = [{"email": D.CLAIRE.email, "organizer": True, "responseStatus": "accepted"},
               {"email": D.JULIA.email, "organizer": False, "responseStatus": e["julia_response"]}]
        for a in att:
            if a["email"] == cal:
                a["self"] = True
        out.append(ins("gcal.gcal_events",
                       ["event_id", "calendar_id", "summary", "description", "location", "start_ts", "end_ts", "start_json",
                        "end_json", "organizer_email", "creator_email", "attendees_json", "status", "visibility", "transparency",
                        "rrule_json", "recurring_event_id", "original_start_json", "sequence", "created", "updated",
                        "hangout_link", "ical_uid"],
                       [evt, cal, e["summary"], None, None, e["start"], D.EVT_END, j({"dateTime": e["start"]}),
                        j({"dateTime": D.EVT_END}), e["organizer"], e["organizer"], j(att), "confirmed", None, "opaque", "[]",
                        None, None, 0, e["created"], e["created"], None, D.ICAL_UID]))
    return out


def rfc(ts):
    return D.parse(ts).strftime("%a, %d %b %Y %H:%M:%S +0000")


def mail_copy(mailbox, thread, msgid, labels, sender, to, subject, body, at):
    """One mailbox copy; msgid is the bare <...> id. Bodies use CRLF like the base."""
    body = body.replace("\n", "\r\n")
    snip = " ".join(body.split())[:140]
    t = ins("gmail.gmail_threads", ["id", "user_email", "snippet", "history_id"], [thread, mailbox, snip, None])
    hdr = [{"name": "Message-ID", "value": msgid}, {"name": "Date", "value": rfc(at)}, {"name": "Subject", "value": subject},
           {"name": "From", "value": sender.addr}, {"name": "To", "value": ", ".join(p.addr for p in to)}]
    m = ins("gmail.gmail_messages",
            ["id", "thread_id", "user_email", "label_ids_json", "snippet", "internal_date", "date", "size_estimate", "subject",
             "from_email", "from_name", "to_json", "cc_json", "bcc_json", "reply_to_json", "body_text", "body_html", "headers_json",
             "in_reply_to", "references", "mbox_from", "attachments_meta_json"],
            [f"{mailbox}/{msgid}", thread, mailbox, j(labels), snip, D.unix(at) * 1000, at, len(body.encode()), subject, sender.email,
             sender.name, j([p.addr for p in to]), "[]", "[]", "[]", body, None, j(hdr), None, None, None, "[]"])
    return [t, m]


INBOX = ["INBOX", "IMPORTANT", "CATEGORY_PERSONAL"]


def sender_thread(julia_thread, sender):
    n = int(julia_thread.rsplit("/", 1)[1]) + D.jitter(julia_thread + sender.email, 200000, 900000)
    return f"{sender.email}/{n}"


def both_copies(julia_msg, julia_thread, sender, subject, body, at):
    msgid = julia_msg.split("/", 1)[1]
    out = mail_copy(D.JULIA.email, julia_thread, msgid, INBOX, sender, [D.JULIA], subject, body, at)
    out += mail_copy(sender.email, sender_thread(julia_thread, sender), msgid, ["SENT"], sender, [D.JULIA], subject, body, at)
    return out


def form_subject(f):
    return f"ZM friend sessions form - {f['observer']}"


def form_body(key):
    f = D.FORMS[key]
    return D.FORM_MAIL[key].format(day=D.day(f["session_date"]), n=f["n"])


def emit_gmail():
    pf = D.PR["panel_forward"]
    subject = "Fwd: Playtest results for Puzzles vs. Zombies"
    out = mail_copy(D.JULIA.email, pf["thread"], pf["message"].split("/", 1)[1], INBOX, D.LEONARD, [D.JULIA], subject, D.PANEL_BODY, pf["at"])
    # One message, two mailbox copies: base row ids are <mailbox>/<same Message-ID>, so the manifest's leonard_copy suffix is not used.
    out += mail_copy(D.LEONARD.email, sender_thread(pf["thread"], D.LEONARD), pf["message"].split("/", 1)[1], ["SENT"], D.LEONARD,
                     [D.JULIA], subject, D.PANEL_BODY, pf["at"])
    for key, f in sorted(D.FORMS.items(), key=lambda kv: kv[1]["form_at"]):
        if f["carrier"] != "gmail":
            continue
        out += both_copies(f["msg"], f["thread"], D.PEOPLE[f["observer"]], form_subject(f), form_body(key), f["form_at"])
    r = D.PR["resent_form"]
    f = D.FORMS[r["of"]]
    out += both_copies(r["message"], r["thread"], D.PEOPLE[f["observer"]], form_subject(f), D.RESENT_PREFIX + form_body(r["of"]), r["at"])
    k = D.PR["k1_mail"]
    out += both_copies(k["message"], k["thread"], D.CLAIRE, k["subject"], D.K1_BODY, k["at"])
    return out


ISSUE_COLS = ["id", "project_id", "team_id", "parent_id", "assignee_id", "creator_id", "state_id", "cycle_id", "identifier",
              "number", "title", "description", "priority", "estimate", "due_date", "started_at", "completed_at", "canceled_at",
              "archived_at", "time_in_status_minutes", "labels_json", "links_json", "relations_json", "state_history_json",
              "is_archived", "created_at", "updated_at"]
COMMENT_COLS = ["id", "issue_id", "author_id", "parent_id", "body", "is_edited", "created_at", "updated_at", "sequence"]


def emit_linear():
    z = D.PR["zom567"]
    out = [ins("linear.linear_issues", ISSUE_COLS,
               ["ZOM-567", None, D.TEAM, None, D.VINCENT.linear, D.VINCENT.linear, "Done", None, "ZOM-567", 567, D.ZOM567["title"],
                D.ZOM567["description"], 2, None, None, D.ZOM567["started_at"], z["closed_at"], None, None, None, '["Bug"]', "[]",
                "[]", "[]", False, z["created_at"], z["closed_at"]])]
    for v in D.SESSION_VIEWS:
        n = int(v["ticket"][4:])
        out.append(ins("linear.linear_issues", ISSUE_COLS,
                       [v["ticket"], None, D.TEAM, None, D.JULIA.linear, D.JULIA.linear, "Todo", None, v["ticket"], n, D.ticket_title(v),
                        D.ticket_description(v), 3, None, None, None, None, None, None, None, "[]", "[]", "[]", "[]", False,
                        v["created_at"], v["comment_time"]]))
    out.append(ins("linear.linear_comments", COMMENT_COLS,
                   [D.ZOM567["line_id"], "ZOM-567", D.VINCENT.linear, None, D.ZOM567["line"], False, z["owner_line_at"], z["owner_line_at"], 1]))
    for v in D.SESSION_VIEWS:
        out.append(ins("linear.linear_comments", COMMENT_COLS,
                       [v["comment"], v["ticket"], D.JULIA.linear, None, v["device_line"], False, v["comment_time"], v["comment_time"], 1]))
    return out


def emit_github():
    a = D.PR["rc27"]
    rev = ["id", "pr_id", "author_login", "state", "body", "submitted_at", "commit_id", "seq"]
    rc = ["id", "pr_id", "author_login", "body", "path", "diff_hunk", "line", "position", "commit_id", "in_reply_to_id", "created_at", "seq"]
    return [
        ins("github.github_reviews", rev, [D.PR["rev3"], D.PR_ID, D.GH_ARTHUR, "COMMENTED", "", a["at"], None, 3]),
        ins("github.github_review_comments", rc, [a["id"], D.PR_ID, D.GH_ARTHUR, D.RC27_BODY, D.VISION_PATH, D.VISION_HUNK, None, None, None, None, a["at"], 27]),
        # rc_28 (CodeRabbit reply) and rev_4 dropped by review M3.
        f"UPDATE github.github_pull_requests SET updated_at = {q(a['at'])} WHERE id = {q(D.PR_ID)};",
    ]


def emit_trello():
    c = D.PR["trello_card"]
    slug = "80-cards-earlier-waiting-on-the-audience-read"
    badges = {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0, "checkItemsChecked": 0,
              "checkItemsEarliestDue": None, "comments": 0, "description": True, "due": None, "dueComplete": False,
              "externalSource": None, "fogbugz": "", "lastUpdatedByAi": False, "location": False, "maliciousAttachments": 0,
              "start": None, "votes": 0}
    card = ins("trello.trello_cards",
               ["id", "name", "idBoard", "idList", "desc", "pos", "closed", "due", "dueComplete", "idMembers_json", "idLabels_json",
                "idShort", "shortLink", "shortUrl", "url", "dateLastActivity", "cover_json", "badges_json"],
               [c["id"], D.CARD["name"], c["board"], c["list"], D.CARD["desc"], D.CARD["pos"], False, None, False, j([D.TRELLO_JULIA]),
                "[]", c["idShort"], D.CARD["shortLink"], None, f"https://PERSON_6092_TRELLO_USERNAME.com/c/{D.CARD['shortLink']}/{slug}",
                c["at"], None, j(badges)])
    data = {"board": {"id": c["board"], "name": "ZM ROADMAP", "shortLink": D.BOARD_SHORT},
            "card": {"id": c["id"], "idShort": c["idShort"], "name": D.CARD["name"], "shortLink": D.CARD["shortLink"]},
            "list": {"id": c["list"], "name": "Backlog"}}
    act = ins("trello.trello_actions", ["id", "type", "date", "idMemberCreator", "idBoard", "idCard", "data_json"],
              [D.CARD["action_id"], "createCard", c["at"], c["creator"], c["board"], c["id"], j(data)])
    return [card, act]


SLACK_COLS = ["id", "ts", "channel_id", "type", "user_id", "text", "thread_parent_id", "thread_ts_legacy", "reply_count",
              "reply_users_count", "latest_reply", "is_activity_message", "subtype", "reactions_json", "files_json",
              "attachments_json", "created_at", "metadata_json"]


def mirror_attachment(login_link, text, ts, disc):
    return [{"color": "24292f", "fallback": "[harmonygames-Games/match3d] Comment on #476",
             "footer": "<https://github.com/harmonygames-Games/match3d|harmonygames-Games/match3d>",
             "footer_icon": "https://slack.github.com/static/img/favicon-neutral.png", "id": 1, "mrkdwn_in": ["text"],
             "pretext": f"<{D.PR_NUM_URL}#discussion_r{disc}|Comment> on pull request by {login_link}", "text": text,
             "title": f"<{D.PR_NUM_URL}|#476 Vision bot>", "ts": int(float(ts))}]


def slack_parent(ch, root):
    """thread_parent_id for a reply. A raw-shape base root has no id field, so a minted sha id would point at no row:
    take the root's own id by channel and ts instead (rev4 fix, plan/parent_check.py)."""
    if (ch, root) in D.RAW_ROOTS:
        return Raw(f"(SELECT id FROM slack.slack_messages WHERE channel_id = {q(ch)} AND ts = {q(root)})")
    return D.row_id(ch, root)


def emit_slack():
    out = []
    for key, ch, ts, row, who, text, root in D.SLACK_ROWS:
        assert row == D.row_id(ch, ts), key
        parent = slack_parent(ch, root) if root else None
        out.append(ins("slack.slack_messages", SLACK_COLS,
                       [row, ts, ch, "message", who.slack, text, parent, root, 0, 0, None, False, None, "[]", "[]", "[]", D.ts_iso(ts), "{}"]))
    root = D.PR["mirror_rc27"]["root"]
    parent = slack_parent(D.CH_PRS, root)
    for rec, link, text, disc in (
            (D.PR["mirror_rc27"], "<https://github.com/arthur.blake|arthur.blake>", D.RC27_BODY, 2392847113),):
        assert rec["row"] == D.row_id(D.CH_PRS, rec["ts"])
        out.append(ins("slack.slack_messages", SLACK_COLS,
                       [rec["row"], rec["ts"], D.CH_PRS, "message", "SLACK_BOT_0004_SLACK_ID", "", parent, root, 0, 0, None, False, None,
                        "[]", "[]", j(mirror_attachment(link, text, rec["ts"], disc)), D.ts_iso(rec["ts"]), "{}"]))
    for ch, ts, rc, users, latest, set_thread in D.ROOT_UPDATES:
        extra = f", thread_ts_legacy = {q(ts)}" if set_thread else ""
        where = f"channel_id = {q(ch)} AND ts = {q(ts)}" if (ch, ts) in D.RAW_ROOTS else f"id = {q(D.row_id(ch, ts))}"
        out.append(f"UPDATE slack.slack_messages SET reply_count = {rc}, reply_users_count = {users}, latest_reply = {q(latest)}{extra} "
                   f"WHERE {where};")
    return out


# Parent-before-child order: Drive rows before native rows, threads before messages, issues before comments.
SERVICES = [("GDRIVE", emit_gdrive), ("GDOCS", emit_gdocs), ("GSHEETS", emit_gsheets), ("GSLIDES", emit_gslides), ("GCAL", emit_gcal),
            ("GMAIL", emit_gmail), ("LINEAR", emit_linear), ("GITHUB", emit_github), ("TRELLO", emit_trello), ("SLACK", emit_slack)]
