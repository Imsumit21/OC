#!/usr/bin/env python3
"""Generate Task_Authoring/task_inputsN2/01_Universe_Inject.sql for the ZM3D Halloween art plan task.

Inputs (all in Working_Files/scenario_gen/): roster_final.json (the 62 serving surfaces + 4 archived creatives, every
ticket / comment / time), planned_texts.json (verbatim texts of every seeded record), ids.json (minted,
collision-checked ids). Reads the universe only for a few base constants (Trello list positions). Never executes SQL.

    python3 -B Task_Authoring/task_inputsN2/Working_Files/injection_gen/gen_sql.py
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
ROOT = TASK.parents[1]
SG = WF / "scenario_gen"
FINAL = json.loads((SG / "roster_final.json").read_text())
R = FINAL["surfaces"]
ARCH = FINAL["archived"]
T = json.loads((SG / "planned_texts.json").read_text())
IDS = json.loads((SG / "ids.json").read_text())
I, TS = IDS["ids"], IDS["timestamps"]
UNI = ROOT / "Universe_SynthCut" / "SynthCut_HarmonyGames_Other_Services" / "Services_Data"

SLACK_ID = {"claire": "EMPLOYEE_0009_SLACK_ID", "leonard": "EMPLOYEE_0038_SLACK_ID", "robert": "EMPLOYEE_0016_SLACK_ID",
            "martin": "EMPLOYEE_0033_SLACK_ID", "marcus": "EMPLOYEE_0002_SLACK_ID"}
LINEAR = {"frederick.stone": "usr_175c0d7bc72ed244", "marcus.bennett": "usr_c77c50cc15c5342d",
          "martin.walsh": "usr_51f5f16d46e8cf55", "claire.morgan": "usr_7fe31e7ec8199618"}
EMAIL = {k: f"{k}@harmonygames.co" for k in ("claire.morgan", "leonard.hayes", "frederick.stone", "martin.walsh",
                                              "marcus.bennett", "arthur.blake")}
EMAIL["robert"] = "robert@harmonygames.co"
DRIVE_ROOT = {"leonard.hayes": "d_63fffeb4fab5233ed5bb73", "frederick.stone": "d_175c0d7bc72ed244b944cb",
              "arthur.blake": "d_cc3e90160f490686039986", "robert": "d_9f7ba94f7526d54d8482ba"}
TRELLO_BOARD, TRELLO_LIST = "6851a6569f3bf818760632ab", I["trello_list_oct21"]
TRELLO_MEMBER = {"leonard.hayes": "PERSON_6094_TRELLO_USER_ID", "frederick.stone": "4b4a68fc0fec0b254e4f9d8e"}
FREEZE = "2025-10-01T00:00:00Z"

OUT: list[str] = []
COUNT = Counter()


def h(label: str, n: int) -> str:
    return hashlib.sha256(f"n2-claire-zm3d-halloween-art-plan|inj|{label}".encode()).hexdigest()[:n]


def lit(v) -> str:
    if v is None:
        return "NULL"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    return "'" + str(v).replace("'", "''") + "'"


def js(v) -> str:
    return lit(json.dumps(v, ensure_ascii=False, separators=(",", ":")))


def insert(table: str, row: dict) -> None:
    cols = ", ".join(f'"{c}"' if c in QUOTE else c for c in row)
    OUT.append(f"INSERT INTO {table} ({cols}) VALUES ({', '.join(lit(v) if not isinstance(v, RawJSON) else v.sql for v in row.values())});")
    COUNT[("insert", table.split(".")[0])] += 1


def update(table: str, sets: dict, where: dict) -> None:
    s = ", ".join(f'{(chr(34) + c + chr(34)) if c in QUOTE else c} = {lit(v) if not isinstance(v, RawJSON) else v.sql}' for c, v in sets.items())
    w = " AND ".join(f"{c} = {lit(v)}" for c, v in where.items())
    OUT.append(f"UPDATE {table} SET {s} WHERE {w};")
    COUNT[("update", table.split(".")[0])] += 1


class RawJSON:
    def __init__(self, v):
        self.sql = js(v)


QUOTE = {"references", "index", "idBoard", "idList", "desc", "dueComplete", "idMembers_json", "idLabels_json", "idShort",
         "shortLink", "shortUrl", "dateLastActivity", "idAttachmentCover", "idMemberCreator", "idCard"}


def dt(iso: str) -> datetime:
    return datetime.fromisoformat(iso.replace("Z", "+00:00"))


def z(d: datetime) -> str:
    return d.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def rfc(iso: str) -> str:
    """RFC 2822 in Pacific daylight time, as Frederick's base mails carry it."""
    d = dt(iso) - timedelta(hours=7)
    return d.strftime("%a, %-d %b %Y %H:%M:%S -0700")


def assert_seed(iso: str, what: str) -> str:
    assert iso <= FREEZE, f"{what} {iso} after the seed bound"
    return iso


def comment(text: str) -> None:
    OUT.append(f"-- {text}")


# ------------------------------------------------------------------ helpers over the roster
MONTH = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def md(iso_date: str) -> str:
    y, m, d = iso_date[:10].split("-")
    return f"{MONTH[int(m) - 1]} {int(d)}" + ("" if y == "2025" else f", {y}")


def aspect(key: str) -> str:
    k = key.lower()
    for a in ("16:9", "4:5", "1:1", "9:16"):
        if a in k:
            return a
    if "landscape" in k:
        return "16:9"
    if "1080x1350" in k:
        return "4:5"
    if "android 1080" in k:
        return "1:1"
    return "9:16"


KIND = {"video": "video", "static": "static", "end_card": "end card"}


def fmt(r: dict) -> str:
    return f"{aspect(r['key'])} {KIND[r['kind']]}"


def maker_name(r: dict) -> str:
    m = (r.get("maker") or "").split("@")[0]
    return {"marcus.bennett": "Marcus Bennett", "julia.lawson": "Julia Lawson", "martin.walsh": "Martin Walsh",
            "frederick.stone": "Frederick Stone", "leonard.hayes": "Leonard Hayes"}.get(m, "Marcus Bennett")


ADS = [r for r in R if r.get("ticket")]
ON_SHEET_ADS = [r for r in ADS if r["on_sheet"]]
STORE = [r for r in R if r["kind"] in ("icon", "store_set")]


# ================================================================== header
def header() -> list[str]:
    ins = sum(v for (op, _), v in COUNT.items() if op == "insert")
    upd = sum(v for (op, _), v in COUNT.items() if op == "update")
    svcs = sorted({s for (_, s) in COUNT})
    return ["-- Are you planning to inject? Yes", "",
            "-- HarmonyGames injection - Claire Morgan (claire.morgan@harmonygames.co), Art Lead - Long Horizon - synth-cut, freeze 2025-10-01T00:00:00Z",
            f"-- Services: {', '.join(svcs)} - {ins} INSERT, {upd} UPDATE",
            "-- Literal values only; parents before children; re-apply before every agent run.", ""]


# ================================================================== slack
def slack_row(loc: dict, user: str, text: str, parent: dict | None = None, replies: list | None = None) -> dict:
    ch, ts = loc["channel"], loc["ts"]
    sec, micro = ts.split(".")
    created = datetime.fromtimestamp(int(sec), timezone.utc).strftime("%Y-%m-%dT%H:%M:%S") + f".{micro}Z"
    assert_seed(created[:19] + "Z", f"slack {ch}/{ts}")
    row = {"id": hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32], "ts": ts, "channel_id": ch, "type": "message",
           "user_id": user, "text": text, "thread_parent_id": None, "thread_ts_legacy": None, "reply_count": 0,
           "reply_users_count": 0, "latest_reply": None, "is_activity_message": False, "subtype": None,
           "reactions_json": "[]", "files_json": "[]", "attachments_json": "[]", "created_at": created, "metadata_json": "{}"}
    assert row["id"] == loc["row_id"], (row["id"], loc["row_id"])
    if parent:
        row["thread_parent_id"] = hashlib.sha256(f"{parent['channel']}|{parent['ts']}".encode()).hexdigest()[:32]
        row["thread_ts_legacy"] = parent["ts"]
    if replies:
        row["thread_ts_legacy"] = ts
        row["reply_count"] = len(replies)
        row["reply_users_count"] = len({u for u, _ in replies})
        row["latest_reply"] = max(t for _, t in replies)
    return row


def gen_slack() -> None:
    comment("slack: Robert's deck pointer and Martin's export note in #zombie-art, Claire's DM to Marcus and his thread reply, Leonard's Halloween ask in #zombie_marketing")
    insert("slack.slack_messages", slack_row(I["slack_robert_pointer"], SLACK_ID["robert"], T["slack_robert_pointer"]["text"]))
    root, reply = I["slack_dm_root"], I["slack_dm_marcus_reply"]
    insert("slack.slack_messages", slack_row(root, SLACK_ID["claire"], T["slack_dm_root"]["text"],
                                             replies=[(SLACK_ID["marcus"], reply["ts"])]))
    insert("slack.slack_messages", slack_row(reply, SLACK_ID["marcus"], T["slack_dm_marcus_reply"]["text"], parent=root))
    insert("slack.slack_messages", slack_row(I["slack_martin_export"], SLACK_ID["martin"], T["slack_martin_export"]["text"]))
    insert("slack.slack_messages", slack_row(I["slack_ask"], SLACK_ID["leonard"], T["slack_ask"]["text"]))
    comment("slack: Robert's Sep 17 thread reply under Martin's base Halloween icon concept, and the parent's reply counters")
    icon_parent = {"channel": "C08R8CHB0QL", "ts": "1758121809.236839"}
    reply = I["slack_robert_icon_reply"]
    insert("slack.slack_messages", slack_row(reply, SLACK_ID["robert"], T["slack_robert_icon_reply"]["text"], parent=icon_parent))
    update("slack.slack_messages", {"thread_ts_legacy": icon_parent["ts"], "reply_count": 1, "reply_users_count": 1,
                                    "latest_reply": reply["ts"]},
           {"id": hashlib.sha256(f"{icon_parent['channel']}|{icon_parent['ts']}".encode()).hexdigest()[:32]})


# ================================================================== linear
def gen_linear() -> None:
    comment("linear: the UA creative library on the ART team (Frederick's catalogue tickets, Sep 8 - Sep 25) and their capture, re-capture and upload notes")
    tickets = sorted([("serving", r) for r in ADS] + [("archived", a) for a in ARCH], key=lambda x: int(x[1]["ticket"][4:]))
    for kind, r in tickets:
        n = int(r["ticket"][4:])
        created = assert_seed(r["ticket_created"], r["ticket"])
        if kind == "archived":
            f = f"{r['format']} video"
            paused = f"{r['paused_on']}T17:00:00Z"
            row = issue_row(r["ticket"], n, f"{r['key']} ({f})",
                            f"UA creative library: {r['key']} ({f}). Paused on {md(r['paused_on'])}, see the Archive tab.",
                            created, paused, state="Canceled", canceled_at=paused)
            insert("linear.linear_issues", row)
            continue
        if r["key"] == "marcus portrait UA end card":
            desc = T["art_ticket_description_patterns"]["end_card_off_sheet"]
        elif not r["on_sheet"] and r["kind"] == "static":
            desc = T["art_ticket_description_patterns"]["static_off_sheet"].format(creative=r["key"])
        else:
            notes = "Capture notes in the comments." if r["kind"] == "static" else "Capture and master notes in the comments."
            desc = f"UA creative library: {r['key']} ({fmt(r)}). Made by {maker_name(r)}. {notes}"
        comments = [(f"cmt_art{n}_1", r["comment_1_by"], r["comment_1"], r["comment_1_at"])]
        if r.get("comment_2"):
            comments.append((f"cmt_art{n}_2", r["comment_2_by"], r["comment_2"], r["comment_2_at"]))
        updated = max([created] + [c[3] for c in comments])
        insert("linear.linear_issues", issue_row(r["ticket"], n, f"{r['key']} ({fmt(r)})", desc, created, updated))
        for cid, by, body, at in comments:
            assert_seed(at, cid)
            assert at > created, (cid, at, created)
            insert("linear.linear_comments", {"id": cid, "issue_id": r["ticket"], "author_id": LINEAR[by], "parent_id": None,
                                              "body": body, "is_edited": False, "created_at": at, "updated_at": at,
                                              "sequence": None})


def issue_row(iid, n, title, desc, created, updated, state="Todo", canceled_at=None) -> dict:
    return {"id": iid, "uuid": None, "project_id": None, "team_id": "team_ART", "parent_id": None, "assignee_id": None,
            "creator_id": LINEAR["frederick.stone"], "state_id": state, "cycle_id": None, "identifier": iid, "number": n,
            "title": title, "description": desc, "priority": 0, "estimate": None, "due_date": None, "started_at": None,
            "completed_at": None, "canceled_at": canceled_at, "archived_at": None, "time_in_status_minutes": None,
            "labels_json": "[]", "links_json": "[]", "relations_json": "[]", "state_history_json": "[]",
            "is_archived": False, "created_at": created, "updated_at": updated}


# ================================================================== drive / docs / sheets / slides
def share(emails, role="reader") -> tuple[str, str]:
    return (json.dumps(emails, separators=(",", ":")),
            json.dumps([{"email": e, "role": role} for e in emails], separators=(",", ":")))


def drive_row(fid, name, mime, parent, owner, shared, role, created, modified) -> dict:
    sw, sr = share(shared, role)
    return {"id": fid, "name": name, "mime_type": mime, "parents_json": json.dumps([parent]), "owner_email": owner,
            "shared_with_emails_json": sw, "shared_roles_json": sr, "visibility_role": None, "visibility": "private",
            "owners_json": json.dumps([owner]), "modified_time": assert_seed(modified, fid),
            "created_time": assert_seed(created, fid), "size": None, "trashed": False, "starred": False,
            "content_path": None, "web_view_link": None, "icon_link": None, "description": None, "drive_id": None,
            "content_text": None}


TEAM_HALLOWEEN = [EMAIL["claire.morgan"], EMAIL["frederick.stone"], EMAIL["martin.walsh"], EMAIL["marcus.bennett"], EMAIL["robert"]]
STORE_NAMES = ([f"ZM3D_Halloween_iPhone65_{i:02d}_1242x2688.png" for i in range(1, 6)]
               + [f"ZM3D_Halloween_GooglePlay_phone_{i:02d}_1080x1920.png" for i in range(1, 7)])
UA_NAMES = ["cheer_fastcouch_halloween_9x16.mp4", "cheer_fastcouch_halloween_16x9.mp4"]


def gen_drive() -> None:
    F = I["folder_halloween"]
    t_folder = "2025-09-29T09:15:00Z"
    comment("drive: Leonard's ZM3D Halloween 2025 folder (Store, UA masters), Martin's Halloween store export, Marcus's two Halloween cuts")
    insert("gdrive.drive_files", drive_row(F["root"], "ZM3D Halloween 2025", "application/vnd.google-apps.folder",
                                           DRIVE_ROOT["leonard.hayes"], EMAIL["leonard.hayes"], TEAM_HALLOWEEN, "writer",
                                           t_folder, "2025-09-30T15:12:40Z"))
    insert("gdrive.drive_files", drive_row(F["store"], "Store", "application/vnd.google-apps.folder", F["root"],
                                           EMAIL["leonard.hayes"], TEAM_HALLOWEEN, "writer", "2025-09-29T09:16:00Z",
                                           "2025-09-30T15:12:40Z"))
    insert("gdrive.drive_files", drive_row(F["ua"], "UA masters", "application/vnd.google-apps.folder", F["root"],
                                           EMAIL["leonard.hayes"], TEAM_HALLOWEEN, "writer", "2025-09-29T09:16:30Z",
                                           "2025-09-29T17:05:20Z"))
    others_m = [EMAIL["leonard.hayes"], EMAIL["claire.morgan"], EMAIL["frederick.stone"], EMAIL["marcus.bennett"], EMAIL["robert"]]
    for i, (fid, name) in enumerate(zip(I["files_store"], STORE_NAMES)):
        t = f"2025-09-30T15:12:{i * 3 + 4:02d}Z"
        row = drive_row(fid, name, "image/png", F["store"], EMAIL["martin.walsh"], others_m, "writer", t, t)
        row["size"] = 1_850_000 + int(h(fid, 5), 16) % 900_000
        insert("gdrive.drive_files", row)
    others_c = [EMAIL["leonard.hayes"], EMAIL["claire.morgan"], EMAIL["frederick.stone"], EMAIL["martin.walsh"], EMAIL["robert"]]
    for i, (fid, name) in enumerate(zip(I["files_ua"], UA_NAMES)):
        t = f"2025-09-29T17:05:{i * 9 + 6:02d}Z"
        row = drive_row(fid, name, "video/mp4", F["ua"], EMAIL["marcus.bennett"], others_c, "writer", t, t)
        row["size"] = 24_000_000 + int(h(fid, 6), 16) % 9_000_000
        insert("gdrive.drive_files", row)


def gen_sheet() -> None:
    sid, t = I["sheet_live"], T["sheet_live"]
    created, modified = "2025-09-08T15:40:00Z", "2025-09-29T18:00:00Z"
    shared = [EMAIL["leonard.hayes"], EMAIL["claire.morgan"], EMAIL["martin.walsh"], EMAIL["marcus.bennett"], EMAIL["robert"]]
    comment("sheets: Frederick's ZM3D live creatives (Read me, Store, Unity, Archive)")
    insert("gdrive.drive_files", drive_row(sid, t["title"], "application/vnd.google-apps.spreadsheet", DRIVE_ROOT["frederick.stone"],
                                           EMAIL["frederick.stone"], shared, "reader", created, modified))
    insert("gsheets.sheets_spreadsheets", {"spreadsheet_id": sid, "title": t["title"], "owner_email": EMAIL["frederick.stone"],
                                           "shared_with_emails_json": json.dumps(shared, separators=(",", ":")),
                                           "visibility": "private", "drive_file_id": sid, "created_time": created,
                                           "modified_time": modified})
    stores = {"app icon": "App Store, Google Play", 'iPhone 6.5" set': "App Store", 'iPad 12.9" set': "App Store",
              "Google Play phone set": "Google Play"}
    tabs = [("Read me", [[t["tabs"]["Read me"]]]),
            ("Store", [["Surface", "Stores", "Live since", "ART ticket"]]
             + [[r["key"], stores[r["key"]], md(r["live_since"]), ""] for r in STORE]),
            ("Unity", [["Creative", "Format", "Live since", "ART ticket"]]      # campaigns live only in the ticket comments
             + [[r["key"], fmt(r), md(r["live_since"]), r["ticket"]] for r in ON_SHEET_ADS]),
            ("Archive", [["Creative", "Format", "Paused on", "ART ticket"]]
             + [[a["key"], f"{a['format']} video", md(a["paused_on"]), a["ticket"]] for a in ARCH])]
    for i, (title, grid) in enumerate(tabs):
        width = max(len(x) for x in grid)
        grid = [x + [""] * (width - len(x)) for x in grid]
        insert("gsheets.sheets_sheets", {"spreadsheet_id": sid, "sheet_id": i, "title": title, "index": i,
                                         "row_count": 1000, "column_count": width, "grid_json": json.dumps(grid, ensure_ascii=False)})


def gen_doc() -> None:
    did, t = I["doc_release"], T["doc_release"]
    created, modified = "2025-09-24T16:20:00Z", "2025-09-30T22:40:00Z"
    shared = [EMAIL["leonard.hayes"], EMAIL["frederick.stone"], EMAIL["robert"], EMAIL["claire.morgan"],
              EMAIL["martin.walsh"], EMAIL["marcus.bennett"]]
    body = t["text"]
    first = body.split("\n", 1)[0]
    comment("docs: Arthur's ZM3D release calendar - Q4")
    insert("gdrive.drive_files", drive_row(did, t["title"], "application/vnd.google-apps.document", DRIVE_ROOT["arthur.blake"],
                                           EMAIL["arthur.blake"], shared, "reader", created, modified))
    insert("gdocs.docs_documents", {"document_id": did, "title": t["title"], "owner_email": EMAIL["arthur.blake"],
                                    "shared_with_emails_json": json.dumps(shared, separators=(",", ":")), "visibility": "private",
                                    "body_text": body,
                                    "style_runs_json": json.dumps([{"start": 0, "end": len(first), "named_style": "TITLE",
                                                                    "list_id": None, "list_nesting": 0}]),
                                    "revision_id": h("doc_rev", 10), "drive_file_id": did, "created_time": created,
                                    "modified_time": modified, "text_style_runs_json": "[]"})


def gen_deck() -> None:
    d, t = I["deck_seasonal"], T["deck_seasonal"]
    pid, at = d["presentation"], "2025-09-25T16:10:00Z"
    shared = [EMAIL["claire.morgan"], EMAIL["martin.walsh"], EMAIL["marcus.bennett"], EMAIL["leonard.hayes"], EMAIL["frederick.stone"]]
    comment("slides: Robert's Seasonal art direction - Q4 2025")
    insert("gdrive.drive_files", drive_row(pid, t["title"], "application/vnd.google-apps.presentation", DRIVE_ROOT["robert"],
                                           EMAIL["robert"], shared, "reader", at, at))
    insert("gslides.slides_presentations", {"presentation_id": pid, "title": t["title"], "owner_email": EMAIL["robert"],
                                            "shared_with_emails_json": json.dumps(shared, separators=(",", ":")),
                                            "visibility": "private", "drive_file_id": pid, "revision_id": h("deck_rev", 10),
                                            "created_time": at, "modified_time": at})
    for i, (slide, text) in enumerate(zip(d["slides"], t["slides"])):
        insert("gslides.slides_pages", {"presentation_id": pid, "object_id": slide, "index": i, "layout": "BLANK", "notes": None})
        title, _, body = text.partition("\n")
        for j, (txt, y, hgt) in enumerate([(title, 0, 1000000), (body, 1000000, 4143500)]):
            insert("gslides.slides_page_elements", {"presentation_id": pid, "page_object_id": slide,
                                                    "object_id": d["elements"][i * 2 + j], "kind": "TEXT_BOX", "text": txt,
                                                    "placeholder_type": None, "x_emu": 0, "y_emu": y, "width_emu": 9144000,
                                                    "height_emu": hgt, "table_json": None, "ordinal": None})


# ================================================================== gmail
def gmail_message(mailbox, thread, rfc_id, labels, at, subject, from_email, from_name, to, body, gm_labels) -> dict:
    ms = int(dt(at).timestamp() * 1000)
    thrid = thread.split("/", 1)[1]
    hdrs = [{"name": "X-GM-THRID", "value": thrid}, {"name": "X-Gmail-Labels", "value": gm_labels},
            {"name": "MIME-Version", "value": "1.0"}, {"name": "Date", "value": rfc(at)},
            {"name": "Message-ID", "value": rfc_id}, {"name": "Subject", "value": subject},
            {"name": "From", "value": f"{from_name} <{from_email}>"},
            {"name": "To", "value": ", ".join(to)}]
    if "SENT" not in labels:
        hdrs.insert(2, {"name": "Delivered-To", "value": mailbox})
    snippet = re.sub(r"\s+", " ", body).strip()[:140]
    return {"id": f"{mailbox}/{rfc_id}", "thread_id": thread, "user_email": mailbox,
            "label_ids_json": json.dumps(labels), "snippet": snippet, "history_id": None, "internal_date": ms,
            "date": assert_seed(at, rfc_id), "size_estimate": 3800 + len(body.encode()), "subject": subject,
            "from_email": from_email, "from_name": from_name, "to_json": json.dumps([x.split("<")[-1].rstrip(">") for x in to]),
            "cc_json": "[]", "bcc_json": "[]", "reply_to_json": "[]", "body_text": body, "body_html": None,
            "headers_json": json.dumps(hdrs, ensure_ascii=False), "payload_json": None, "in_reply_to": None,
            "references": None, "mbox_from": None, "date_parsed_source": None, "attachments_meta_json": "[]"}


def gen_gmail() -> None:
    to = [f"leonard hayes <{EMAIL['leonard.hayes']}>", f"claire morgan <{EMAIL['claire.morgan']}>",
          f"marcus bennett <{EMAIL['marcus.bennett']}>", f"martin walsh <{EMAIL['martin.walsh']}>"]
    comment("gmail: Frederick's October UA plan (draft, Sep 12) and its changes mail (Sep 30), one copy per participant mailbox; the vendor's props quote to Claire")
    for key in ("gmail_fred_draft", "gmail_fred_plan"):
        t, ids = T[key], I[key]
        rfc_id = ids["msg"].split("/", 1)[1]
        at = TS[key]
        for mailbox, thread in ids["copies"].items():
            sent = mailbox == EMAIL["frederick.stone"]
            labels = ["SENT"] if sent else ["INBOX", "CATEGORY_PERSONAL"]
            gm = "Sent,Opened" if sent else "Inbox,Opened,Category Personal"
            msg = gmail_message(mailbox, thread, rfc_id, labels, at, t["subject"], EMAIL["frederick.stone"], "frederick stone",
                                to, t["body"], gm)
            insert("gmail.gmail_threads", {"id": thread, "user_email": mailbox, "snippet": msg["snippet"], "history_id": None})
            insert("gmail.gmail_messages", msg)
    q, ids = T["gmail_vendor_quote"], I["gmail_vendor_quote"]
    at = TS["gmail_vendor_quote"]
    msg = gmail_message(EMAIL["claire.morgan"], ids["thread"], ids["msg"].split("/", 1)[1], ["INBOX", "CATEGORY_PERSONAL"], at,
                        q["subject"], ids["sender"], "PERSON_6311_NAME", [EMAIL["claire.morgan"]], q["body"],
                        "Inbox,Opened,Category Personal")
    insert("gmail.gmail_threads", {"id": ids["thread"], "user_email": EMAIL["claire.morgan"], "snippet": msg["snippet"], "history_id": None})
    insert("gmail.gmail_messages", msg)


# ================================================================== gcal
MEET = "https://meet.google.com/" + "-".join("".join(chr(97 + int(c, 16) % 26) for c in h(f"meet{i}", n))
                                            for i, n in ((0, 3), (1, 4), (2, 3))) + "?hs=224"

def gen_gcal() -> None:
    g, t = I["gcal_review"], dict(T["gcal_review"])
    t["start"], t["end"] = TS["gcal_review_start"], "2025-10-02T16:30:00Z"
    attendees = list(g["evt_by_calendar"])
    comment("gcal: Leonard's ZM3D Halloween review, Thu Oct 2 (one copy per attendee calendar)")
    for cal, evt in g["evt_by_calendar"].items():
        att = [{"email": a, "organizer": a == EMAIL["leonard.hayes"], "responseStatus": "accepted" if a == EMAIL["leonard.hayes"] else "needsAction",
                **({"self": True} if a == cal else {})} for a in attendees]
        insert("gcal.gcal_events", {"event_id": evt, "calendar_id": cal, "summary": t["summary"], "description": t["description"],
                                    "location": None, "start_ts": t["start"], "end_ts": t["end"],
                                    "start_json": json.dumps({"dateTime": t["start"]}), "end_json": json.dumps({"dateTime": t["end"]}),
                                    "organizer_email": EMAIL["leonard.hayes"], "creator_email": EMAIL["leonard.hayes"],
                                    "attendees_json": json.dumps(att, separators=(",", ":")), "status": "confirmed", "visibility": None,
                                    "transparency": "opaque", "rrule_json": "[]", "recurring_event_id": None,
                                    "original_start_json": None, "sequence": 0, "created": assert_seed("2025-09-30T22:10:00Z", evt),
                                    "updated": "2025-09-30T22:10:00Z",
                                    "hangout_link": MEET,
                                    "ical_uid": g["ical_uid"], "extras_json": None})


# ================================================================== trello
def gen_trello() -> None:
    tc, tm = T["trello_card"], T["trello_comment"]
    cid, cact, mid = I["trello_card"], I["trello_card_create_action"], I["trello_comment"]
    data = json.loads((UNI / "trello" / "data.json").read_text())
    pos = max([c.get("pos") or 0 for c in data["cards"] if c.get("idList") == TRELLO_LIST] + [0]) + 16384
    short = "".join(c for c in h("trello_short", 40) if c.isalnum())[:8]
    short = short[:2].upper() + short[2:5] + short[5:].upper()
    slug = re.sub(r"[^a-z0-9]+", "-", tc["name"].lower()).strip("-")
    idshort = I["trello_id_short"]
    board = {"id": TRELLO_BOARD, "name": "ZM ROADMAP", "shortLink": "HSqnngwQ"}
    card = {"id": cid, "idShort": idshort, "name": tc["name"], "shortLink": short}
    lst = {"id": TRELLO_LIST, "name": "Oct 21"}
    badges = {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0,
              "checkItemsChecked": 0, "checkItemsEarliestDue": None, "comments": 1, "description": True, "due": None,
              "dueComplete": False, "externalSource": None, "fogbugz": "", "lastUpdatedByAi": False, "location": False,
              "maliciousAttachments": 0, "start": None, "votes": 0}
    created, commented = "2025-09-30T22:00:00Z", "2025-09-30T23:20:00Z"
    for tid, at in ((cid, created), (cact, created), (mid, commented)):
        assert int(tid[:8], 16) == int(dt(at).timestamp()), (tid, at)
    comment("trello: Leonard's Halloween push card on the ZM ROADMAP and Frederick's comment on it")
    insert("trello.trello_cards", {"id": cid, "name": tc["name"], "idBoard": TRELLO_BOARD, "idList": TRELLO_LIST,
                                   "desc": tc["desc"], "pos": pos, "closed": False, "due": None, "dueComplete": False,
                                   "idMembers_json": "[]", "idLabels_json": "[]", "idShort": idshort, "shortLink": None,
                                   "shortUrl": None, "url": f"https://PERSON_6092_TRELLO_USERNAME.com/c/{short}/{idshort}-{slug}",
                                   "dateLastActivity": commented, "cover_json": None, "badges_json": json.dumps(badges, separators=(",", ":")),
                                   "start": None, "idAttachmentCover": None})
    insert("trello.trello_actions", {"id": cact, "type": "createCard", "date": created, "idMemberCreator": TRELLO_MEMBER["leonard.hayes"],
                                     "idBoard": TRELLO_BOARD, "idCard": cid,
                                     "data_json": json.dumps({"board": board, "card": card, "list": lst}, separators=(",", ":"))})
    insert("trello.trello_actions", {"id": mid, "type": "commentCard", "date": commented, "idMemberCreator": TRELLO_MEMBER["frederick.stone"],
                                     "idBoard": TRELLO_BOARD, "idCard": cid,
                                     "data_json": json.dumps({"board": board, "card": card, "idCard": cid, "list": lst, "text": tm["text"],
                                                              "textData": {"emoji": {}}}, ensure_ascii=False, separators=(",", ":"))})
    update("trello.trello_boards", {"dateLastActivity": commented}, {"id": TRELLO_BOARD})


# ================================================================== contacts
def gen_contacts() -> None:
    comment("contacts: the props vendor who wrote to Claire")
    insert("contacts.contacts", {"contact_id": I["contact_vendor"], "first_name": "PERSON_6311", "last_name": "", "is_user": False,
                                 "gender": "Unknown", "status": "Unknown", "job": "Founder, KayKit", "description": None,
                                 "email": "PERSON_6311_EMAIL", "created_at": "2025-09-24T14:05:00Z", "updated_at": "2025-09-24T14:05:00Z"})


def main() -> None:
    gen_slack()
    gen_linear()
    gen_drive()
    gen_sheet()
    gen_doc()
    gen_deck()
    gen_gmail()
    gen_gcal()
    gen_trello()
    gen_contacts()
    sql = "\n".join(header() + OUT) + "\n"
    (TASK / "01_Universe_Inject.sql").write_text(sql)
    ins = {s: v for (op, s), v in COUNT.items() if op == "insert"}
    print("wrote 01_Universe_Inject.sql:", sum(ins.values()), "INSERT", ins, "| UPDATE",
          sum(v for (op, _), v in COUNT.items() if op == "update"))


if __name__ == "__main__":
    main()
