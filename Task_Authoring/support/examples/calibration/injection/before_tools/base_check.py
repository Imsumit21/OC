#!/usr/bin/env python3
"""Base-universe consistency check for injection SQL — mirrors `/injection` Checks A and C.

`sql_lint.py` checks the SQL against the schema and the clock (Check B). This tool checks
it against the **base data** in the three read-only HarmonyGames folders, the way
`Evals/0_Injection_Quality_Eval.md` does:

  Check A — records, references and IDs
    * every new primary id is free in the base (no collision) and unique in the SQL
    * every reference resolves to a base record or a record the SQL itself inserts
      (channel, user, thread parent, issue, PR, repo, thread, calendar, board/list/card,
      page/space, Drive parent, drive_file_id …)
    * every UPDATE / DELETE target exists
    * service ID contracts (Slack id = sha256("<channel>|<ts>")[:32]; Gmail ids
      "<mailbox>/<id>" with the row's own user_email)
  Check C — dates and relationships
    * replies follow their parents (Slack ts, Linear/GitHub/Confluence comments after
      their issue/PR/page, Gmail replies after the message they answer, Trello actions
      after the card exists)
    * calendar events end after they start; Slack created_at agrees with ts
    * a reply added to an existing Slack thread is paired with an UPDATE of the parent's
      reply_count / latest_reply

It reads the exports directly (read-only) and caches small indexes in
`Task_Authoring/support/local_search/cache/`. Nothing under Evals/, claude/ or HarmonyGames_* is
written. Like `/injection`, it is static: it does not prove the SQL deploys.

Usage:
  python3 Task_Authoring/tools/base_check.py <injection.sql> [--json]
  python3 Task_Authoring/tools/base_check.py --self-test
Exit 0 = PASS, 1 = FAIL, 2 = usage error.
"""
from __future__ import annotations

import datetime as dt
import glob
import hashlib
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sql_lint import literal, parse_time, split_statements, split_top, tuples_after_values  # noqa: E402

BUNDLE = Path(__file__).resolve().parent.parent
WS = BUNDLE.parent
OTHER = WS / "HarmonyGames_Other_Services" / "Services_Data"
GITHUB = WS / "HarmonyGames_GitHub" / "Services_Data" / "github" / "data.json"
GMAIL = WS / "HarmonyGames_Gmail" / "Services_Data" / "gmail"
CACHE = BUNDLE / "support" / "local_search" / "cache"
CLOCK = dt.datetime(2026, 2, 14, tzinfo=dt.timezone.utc)


# ---------------------------------------------------------------- SQL parsing

def parse_sql(sql: str) -> list[dict]:
    """INSERT rows / UPDATE / DELETE statements as dicts (same grammar sql_lint accepts)."""
    out = []
    for line, stmt in split_statements(sql):
        m = re.match(r"insert\s+into\s+([a-z_0-9\"]+)\.([a-z_0-9\"]+)\s*\(([^)]*)\)\s*values\s*(.*)$", stmt, re.I | re.S)
        u = re.match(r"update\s+([a-z_0-9\"]+)\.([a-z_0-9\"]+)\s+set\s+(.*?)\s+where\s+(.*)$", stmt, re.I | re.S)
        d = re.match(r"delete\s+from\s+([a-z_0-9\"]+)\.([a-z_0-9\"]+)\s+where\s+(.*)$", stmt, re.I | re.S)
        if m:
            table = f"{m.group(1).strip(chr(34))}.{m.group(2).strip(chr(34))}".lower()
            cols = [c.strip().strip('"') for c in m.group(3).split(",")]
            body = re.split(r"\bon\s+conflict\b", m.group(4), flags=re.I)[0]
            for tup in tuples_after_values(body):
                vals = split_top(tup)
                if len(vals) == len(cols):
                    out.append({"line": line, "op": "insert", "table": table,
                                "row": {c: literal(v) for c, v in zip(cols, vals)}})
        elif u or d:
            g = u or d
            table = f"{g.group(1).strip(chr(34))}.{g.group(2).strip(chr(34))}".lower()
            where = (u.group(4) if u else d.group(3))
            keys = {k.lower(): v for k, v in re.findall(r"\"?([a-z_]+)\"?\s*=\s*'((?:[^']|'')*)'", where, re.I)}
            sets = {}
            if u:
                for assign in split_top(u.group(3)):
                    if "=" in assign:
                        col, val = assign.split("=", 1)
                        sets[col.strip().strip('"')] = literal(val)
            out.append({"line": line, "op": "update" if u else "delete", "table": table, "where": keys, "set": sets})
    return out


# ---------------------------------------------------------------- base indexes

def _cached(name: str, build):
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"base_{name}.json"
    if path.exists():
        return json.loads(path.read_text())
    data = build()
    path.write_text(json.dumps(data))
    return data


def _load(p: Path):
    return json.loads(p.read_text())


class Base:
    """Lazy, read-only indexes over the base exports."""

    def __init__(self):
        self._c = {}

    def _get(self, key, build):
        if key not in self._c:
            self._c[key] = build()
        return self._c[key]

    # slack
    def slack(self):
        def build():
            ch = _load(OTHER / "slack" / "channels.json")
            us = _load(OTHER / "slack" / "users.json")
            return {"channels": {c["id"]: c.get("members") or [] for c in ch}, "users": [u["id"] for u in us]}
        return self._get("slack", lambda: _cached("slack", build))

    def slack_messages(self, channel: str) -> dict:
        key = f"slack_msgs:{channel}"

        def build():
            msgs = {}
            for f in sorted(glob.glob(str(OTHER / "slack" / "messages" / channel / "*.json"))):
                for m in _load(Path(f)):
                    msgs[m["ts"]] = {"id": m.get("id"), "thread_ts": m.get("thread_ts"),
                                     "reply_count": m.get("reply_count")}
            return msgs
        return self._get(key, build)

    def linear(self):
        def build():
            d = _load(OTHER / "linear" / "data.json")
            return {"users": [u["id"] for u in d["users"]], "teams": [t["id"] for t in d["teams"]],
                    "projects": [p["id"] for p in d["projects"]],
                    "issues": {i["id"]: i.get("created_at") for i in d["issues"]},
                    "identifiers": [i.get("identifier") for i in d["issues"]],
                    "comments": [c["id"] for c in d.get("comments") or []],
                    "attachments": [a["id"] for a in d.get("attachments") or []]}
        return self._get("linear", lambda: _cached("linear", build))

    def github(self):
        def build():
            d = _load(GITHUB)
            return {"users": [u["login"] for u in d["users"]], "repos": [r["id"] for r in d["repositories"]],
                    "prs": {p["id"]: p.get("created_at") for p in d["pull_requests"]},
                    "pr_comments": [c["id"] for c in d["pull_request_comments"]],
                    "review_comments": [c["id"] for c in d["review_comments"]],
                    "reviews": [c["id"] for c in d["reviews"]],
                    "timeline": [c["id"] for c in d["timeline_events"]],
                    "commits": [c["sha"] for c in d["commits"]]}
        return self._get("github", lambda: _cached("github", build))

    def gmail(self):
        def build():
            idx = {}
            for f in glob.glob(str(GMAIL / "threads" / "*.json")):
                try:
                    d = _load(Path(f))
                except ValueError:
                    continue
                idx[d["id"]] = [d.get("user_email"), [m.get("id") for m in d.get("messages", [])],
                                [m.get("date") for m in d.get("messages", [])]]
            return idx
        return self._get("gmail", lambda: _cached("gmail_index", build))

    def gmail_messages(self) -> dict:
        def build():
            out = {}
            for tid, entry in self.gmail().items():
                for mid, date in zip(entry[1], entry[2]):
                    out[mid] = date
            return out
        return self._get("gmail_msgs", build)

    def gcal(self):
        def build():
            d = _load(OTHER / "gcal" / "data.json")
            return {"calendars": [c["calendar_id"] for c in d["calendars"]],
                    "events": [f"{e['calendar_id']}|{e['event_id']}" for e in d["events"]]}
        return self._get("gcal", lambda: _cached("gcal", build))

    def trello(self):
        def build():
            d = _load(OTHER / "trello" / "data.json")
            return {"boards": [b["id"] for b in d["boards"]], "lists": {l["id"]: l["idBoard"] for l in d["lists"]},
                    "cards": {c["id"]: c["idBoard"] for c in d["cards"]}, "members": [m["id"] for m in d["members"]],
                    "actions": [a["id"] for a in d["actions"]], "labels": [x["id"] for x in d["labels"]],
                    "checklists": [x["id"] for x in d["checklists"]], "check_items": [x["id"] for x in d["check_items"]]}
        return self._get("trello", lambda: _cached("trello", build))

    def confluence(self):
        def build():
            d = _load(OTHER / "confluence" / "confluence_working.json")
            return {"users": [u["id"] for u in d["users"]], "spaces": [s["id"] for s in d["spaces"]],
                    "pages": {p["id"]: p.get("created_at") for p in d["pages"]},
                    "comments": [c["id"] for c in d["comments"]],
                    "versions": [f"{v['page_id']}|{v['number']}" for v in d["page_versions"]]}
        return self._get("confluence", lambda: _cached("confluence", build))

    def drive(self):
        def build():
            d = _load(OTHER / "gdrive" / "data.json")
            return {"files": {f["id"]: f.get("mime_type") for f in d["drive_files"]},
                    "users": [u.get("email") for u in d.get("drive_users", [])]}
        return self._get("drive", lambda: _cached("drive", build))

    def google_native(self):
        def build():
            docs = _load(OTHER / "gdocs" / "data.json")
            slides = _load(OTHER / "gslides" / "data.json")
            return {"docs": [x["document_id"] for x in docs["docs_documents"]],
                    "slides": [x["presentation_id"] for x in slides["slides_presentations"]]}
        return self._get("gnative", lambda: _cached("gnative", build))

    def contacts(self):
        def build():
            d = _load(OTHER / "contacts" / "contacts.json")
            return {"ids": [c["contact_id"] for c in d["contacts"]]}
        return self._get("contacts", lambda: _cached("contacts", build))


# ---------------------------------------------------------------- checks

def _t(v):
    if v is None:
        return None
    if re.fullmatch(r"\d{10}(\.\d+)?", str(v)):
        return dt.datetime.fromtimestamp(float(v), dt.timezone.utc)
    return parse_time(str(v))


def _json_list(v):
    try:
        x = json.loads(v) if isinstance(v, str) else v
        return x if isinstance(x, list) else []
    except ValueError:
        return []


def check(sql: str, base: Base | None = None) -> dict:
    base = base or Base()
    stmts = parse_sql(sql)
    A, C, notes = [], [], []

    def fa(s, msg):
        A.append({"line": s["line"], "table": s["table"], "msg": msg})

    def fc(s, msg):
        C.append({"line": s["line"], "table": s["table"], "msg": msg})

    ins = defaultdict(list)
    for s in stmts:
        if s["op"] == "insert":
            ins[s["table"]].append(s)

    def new(table, col):
        return {s["row"].get(col) for s in ins.get(table, [])}

    # ids the SQL itself creates, for reference resolution
    new_slack_ts = defaultdict(dict)  # channel -> ts -> id
    for s in ins.get("slack.slack_messages", []):
        r = s["row"]
        new_slack_ts[r.get("channel_id")][r.get("ts")] = r.get("id")
    new_channels = new("slack.slack_channels", "id")
    new_slack_users = new("slack.slack_users", "id")
    new_issues = {s["row"].get("id"): s["row"].get("created_at") for s in ins.get("linear.linear_issues", [])}
    new_lin_comments = new("linear.linear_comments", "id")
    new_prs = {s["row"].get("id"): s["row"].get("created_at") for s in ins.get("github.github_pull_requests", [])}
    new_threads = {s["row"].get("id"): s["row"].get("user_email") for s in ins.get("gmail.gmail_threads", [])}
    new_gmail_msgs = {s["row"].get("id"): s["row"].get("date") for s in ins.get("gmail.gmail_messages", [])}
    new_cals = new("gcal.gcal_calendars", "calendar_id")
    new_cards = {s["row"].get("id"): s["row"].get("idBoard") for s in ins.get("trello.trello_cards", [])}
    new_lists = {s["row"].get("id"): s["row"].get("idBoard") for s in ins.get("trello.trello_lists", [])}
    new_pages = {s["row"].get("id"): s["row"].get("created_at") for s in ins.get("confluence.confluence_pages", [])}
    new_drive = {s["row"].get("id") for s in ins.get("gdrive.drive_files", [])}

    seen = defaultdict(set)
    updated_parents = set()
    for s in stmts:
        if s["op"] == "update" and s["table"] == "slack.slack_messages":
            updated_parents.add(s["where"].get("id"))

    for s in stmts:
        t, op = s["table"], s["op"]
        if op in ("update", "delete"):
            w = s["where"]
            exists = None
            if t == "slack.slack_messages" and "id" in w:
                exists = any(w["id"] == m.get("id") for ch in _channels_for_id(base, w["id"], new_slack_ts)
                             for m in base.slack_messages(ch).values()) or any(w["id"] in d.values() for d in new_slack_ts.values())
            elif t == "linear.linear_issues" and "id" in w:
                exists = w["id"] in base.linear()["issues"] or w["id"] in new_issues
            elif t == "github.github_pull_requests" and "id" in w:
                exists = w["id"] in base.github()["prs"] or w["id"] in new_prs
            elif t == "trello.trello_cards" and "id" in w:
                exists = w["id"] in base.trello()["cards"] or w["id"] in new_cards
            elif t == "confluence.confluence_pages" and "id" in w:
                exists = w["id"] in base.confluence()["pages"] or w["id"] in new_pages
            elif t == "gdrive.drive_files" and "id" in w:
                exists = w["id"] in base.drive()["files"] or w["id"] in new_drive
            elif t == "slack.slack_channels" and "id" in w:
                exists = w["id"] in base.slack()["channels"] or w["id"] in new_channels
            elif t == "gmail.gmail_threads" and "id" in w:
                exists = w["id"] in base.gmail() or w["id"] in new_threads
            if exists is False:
                fa(s, f"{op.upper()} target {w} does not exist in the base or the SQL")
            continue

        r = s["row"]
        if t == "slack.slack_messages":
            ch, ts, mid = r.get("channel_id"), r.get("ts"), r.get("id")
            if ch not in base.slack()["channels"] and ch not in new_channels:
                fa(s, f"channel {ch} does not exist")
            else:
                base_msgs = base.slack_messages(ch) if ch in base.slack()["channels"] else {}
                if ts in base_msgs:
                    fa(s, f"(channel, ts) {ch}/{ts} already exists in the base")
            if mid and ch and ts and hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32] != mid:
                fa(s, f"id {mid} breaks the Slack id contract sha256('{ch}|{ts}')[:32]")
            uid = r.get("user_id")
            if uid and uid not in base.slack()["users"] and uid not in new_slack_users:
                fa(s, f"user {uid} does not exist in slack users")
            members = base.slack()["channels"].get(ch) or []
            if uid and members and uid not in members and not r.get("bot_id"):
                fc(s, f"user {uid} posts in {ch} but is not a channel member")
            parent = r.get("thread_ts_legacy") or r.get("thread_parent_id")
            if parent and parent != ts:
                pts = parent
                if not re.fullmatch(r"\d{10}\.\d+", str(parent)):  # parent given by id → find its ts
                    pts = next((k for k, v in base_msgs_or_new(base, ch, new_slack_ts).items() if v == parent), None)
                pool = base_msgs_or_new(base, ch, new_slack_ts)
                if pts not in pool:
                    fa(s, f"thread parent {parent} not found in channel {ch}")
                else:
                    if _t(ts) and _t(pts) and _t(ts) <= _t(pts):
                        fc(s, f"reply ts {ts} is not after its parent {pts}")
                    pid = pool[pts]
                    if pts in (base.slack_messages(ch) if ch in base.slack()["channels"] else {}) and pid not in updated_parents:
                        fc(s, f"reply to base thread {pts} without an UPDATE of the parent's reply_count/latest_reply")
            ca = _t(r.get("created_at"))
            if ca and _t(ts) and abs((ca - _t(ts)).total_seconds()) > 1:
                fc(s, f"created_at {r.get('created_at')} disagrees with ts {ts}")
        elif t == "linear.linear_comments":
            iid = r.get("issue_id")
            created = base.linear()["issues"].get(iid) if iid in base.linear()["issues"] else new_issues.get(iid)
            if iid not in base.linear()["issues"] and iid not in new_issues:
                fa(s, f"issue {iid} does not exist")
            if r.get("author_id") not in base.linear()["users"]:
                fa(s, f"author {r.get('author_id')} is not a linear user")
            if r.get("id") in base.linear()["comments"]:
                fa(s, f"comment id {r.get('id')} collides with the base")
            if r.get("parent_id") and r["parent_id"] not in new_lin_comments and r["parent_id"] not in base.linear()["comments"]:
                fa(s, f"parent comment {r['parent_id']} does not exist")
            if created and _t(r.get("created_at")) and _t(created) and _t(r.get("created_at")) < _t(created):
                fc(s, f"comment {r.get('id')} predates its issue {iid}")
        elif t == "linear.linear_issues":
            L = base.linear()
            if r.get("id") in L["issues"] or r.get("identifier") in L["identifiers"]:
                fa(s, f"issue {r.get('id')} collides with the base")
            for col, pool in (("team_id", L["teams"]), ("assignee_id", L["users"]), ("creator_id", L["users"]),
                              ("project_id", L["projects"])):
                if r.get(col) and r[col] not in pool:
                    fa(s, f"{col} {r[col]} does not exist")
            if r.get("parent_id") and r["parent_id"] not in L["issues"] and r["parent_id"] not in new_issues:
                fa(s, f"parent issue {r['parent_id']} does not exist")
        elif t in ("github.github_pr_comments", "github.github_reviews", "github.github_review_comments",
                   "github.github_timeline_events"):
            G = base.github()
            pr = r.get("pr_id")
            if pr not in G["prs"] and pr not in new_prs:
                fa(s, f"PR {pr} does not exist")
            pool = {"github.github_pr_comments": "pr_comments", "github.github_reviews": "reviews",
                    "github.github_review_comments": "review_comments", "github.github_timeline_events": "timeline"}[t]
            if r.get("id") in G[pool]:
                fa(s, f"id {r.get('id')} collides with the base")
            who = r.get("author_login") or r.get("actor_login")
            if who and who not in G["users"]:
                fa(s, f"login {who} is not a github user")
            when = r.get("created_at") or r.get("submitted_at")
            pc = G["prs"].get(pr) or new_prs.get(pr)
            if when and pc and _t(when) and _t(pc) and _t(when) < _t(pc):
                fc(s, f"{r.get('id')} predates its PR {pr}")
        elif t == "github.github_pull_requests":
            G = base.github()
            if r.get("id") in G["prs"]:
                fa(s, f"PR {r.get('id')} collides with the base")
            if r.get("repo_id") not in G["repos"]:
                fa(s, f"repo {r.get('repo_id')} does not exist")
        elif t == "gmail.gmail_threads":
            tid, ue = r.get("id"), r.get("user_email")
            if tid in base.gmail():
                fa(s, f"thread {tid} collides with the base")
            if tid and ue and not str(tid).startswith(f"{ue}/"):
                fa(s, f"thread id {tid} does not carry its mailbox prefix {ue}/")
        elif t == "gmail.gmail_messages":
            tid, ue, mid = r.get("thread_id"), r.get("user_email"), r.get("id")
            owner = base.gmail()[tid][0] if tid in base.gmail() else new_threads.get(tid)
            if owner is None:
                fa(s, f"thread {tid} does not exist (insert the gmail_threads row first)")
            elif owner != ue:
                fa(s, f"message user_email {ue} differs from its thread's mailbox {owner}")
            if mid in base.gmail_messages():
                fa(s, f"message id {mid} collides with the base")
            if mid and ue and not str(mid).startswith(f"{ue}/"):
                fa(s, f"message id {mid} does not carry its mailbox prefix {ue}/")
            irt = r.get("in_reply_to")
            if irt:
                ref_date = None
                for k, v in list(new_gmail_msgs.items()) + [(k, v) for k, v in base.gmail_messages().items() if irt in str(k)]:
                    if str(k).endswith(str(irt)) or k == irt:
                        ref_date = v
                        break
                if ref_date and _t(r.get("date")) and _t(ref_date) and _t(r.get("date")) < _t(ref_date):
                    fc(s, f"reply {mid} is dated before the message it answers")
        elif t == "gcal.gcal_events":
            cal = r.get("calendar_id")
            if cal not in base.gcal()["calendars"] and cal not in new_cals:
                fa(s, f"calendar {cal} does not exist")
            if f"{cal}|{r.get('event_id')}" in base.gcal()["events"]:
                fa(s, f"event {r.get('event_id')} already exists on {cal}")
            if _t(r.get("start_ts")) and _t(r.get("end_ts")) and _t(r["end_ts"]) <= _t(r["start_ts"]):
                fc(s, f"event {r.get('event_id')} ends before it starts")
        elif t in ("trello.trello_cards", "trello.trello_actions"):
            T = base.trello()
            if r.get("id") in (T["cards"] if t.endswith("cards") else T["actions"]):
                fa(s, f"id {r.get('id')} collides with the base")
            if r.get("idBoard") and r["idBoard"] not in T["boards"]:
                fa(s, f"board {r['idBoard']} does not exist")
            if t.endswith("cards") and r.get("idList"):
                lb = T["lists"].get(r["idList"]) or new_lists.get(r["idList"])
                if lb is None:
                    fa(s, f"list {r['idList']} does not exist")
                elif lb != r.get("idBoard"):
                    fa(s, f"list {r['idList']} belongs to board {lb}, not {r.get('idBoard')}")
            if t.endswith("actions"):
                card = r.get("idCard")
                if card and card not in T["cards"] and card not in new_cards:
                    fa(s, f"card {card} does not exist")
                if r.get("idMemberCreator") and r["idMemberCreator"] not in T["members"]:
                    fa(s, f"member {r['idMemberCreator']} does not exist")
                if card and re.fullmatch(r"[0-9a-f]{24}", card) and _t(r.get("date")):
                    born = dt.datetime.fromtimestamp(int(card[:8], 16), dt.timezone.utc)
                    if _t(r["date"]) < born:
                        fc(s, f"action {r.get('id')} predates card {card} (created {born:%Y-%m-%d})")
        elif t in ("confluence.confluence_pages", "confluence.confluence_comments", "confluence.confluence_page_versions"):
            Cf = base.confluence()
            if t.endswith("pages"):
                if r.get("id") in Cf["pages"]:
                    fa(s, f"page {r.get('id')} collides with the base")
                if r.get("space_id") and r["space_id"] not in Cf["spaces"]:
                    fa(s, f"space {r['space_id']} does not exist")
            else:
                pg = r.get("page_id")
                if pg not in Cf["pages"] and pg not in new_pages:
                    fa(s, f"page {pg} does not exist")
                if t.endswith("comments") and r.get("id") in Cf["comments"]:
                    fa(s, f"comment {r.get('id')} collides with the base")
                if t.endswith("versions") and f"{pg}|{r.get('number')}" in Cf["versions"]:
                    fa(s, f"version {r.get('number')} of {pg} already exists")
                pc = Cf["pages"].get(pg) or new_pages.get(pg)
                if pc and _t(r.get("created_at")) and _t(pc) and _t(r["created_at"]) < _t(pc):
                    fc(s, f"{r.get('id')} predates page {pg}")
            if r.get("author_id") and r["author_id"] not in Cf["users"]:
                fa(s, f"author {r['author_id']} is not a confluence user")
        elif t == "gdrive.drive_files":
            D = base.drive()
            if r.get("id") in D["files"]:
                fa(s, f"file {r.get('id')} collides with the base")
            for p in _json_list(r.get("parents_json")):
                if p not in D["files"] and p not in new_drive:
                    fa(s, f"parent folder {p} does not exist")
        elif t in ("gdocs.docs_documents", "gsheets.sheets_spreadsheets", "gslides.slides_presentations"):
            key = {"gdocs.docs_documents": "document_id", "gsheets.sheets_spreadsheets": "spreadsheet_id",
                   "gslides.slides_presentations": "presentation_id"}[t]
            fid = r.get("drive_file_id")
            if fid and fid not in base.drive()["files"] and fid not in new_drive:
                fa(s, f"drive_file_id {fid} has no drive_files row (base or SQL)")
            if r.get(key) and fid and r[key] != fid:
                fa(s, f"{key} {r[key]} differs from drive_file_id {fid}")
            if t == "gdocs.docs_documents" and r.get(key) in base.google_native()["docs"]:
                fa(s, f"document {r.get(key)} collides with the base")
            if t == "gslides.slides_presentations" and r.get(key) in base.google_native()["slides"]:
                fa(s, f"presentation {r.get(key)} collides with the base")
        elif t == "contacts.contacts":
            if r.get("contact_id") in base.contacts()["ids"]:
                fa(s, f"contact {r.get('contact_id')} collides with the base")
        else:
            notes.append(f"{t}: no base-reference rules (checked by sql_lint only)")

        # duplicate keys inside the SQL itself
        key = next((r.get(k) for k in ("id", "event_id", "contact_id", "document_id", "presentation_id") if r.get(k)), None)
        if key and t not in ("gsheets.sheets_sheets", "gslides.slides_pages", "gslides.slides_page_elements"):
            if key in seen[t]:
                fa(s, f"{t} id {key} inserted twice")
            seen[t].add(key)

    # GitHub → Slack mirror (GitHub app): seeded PR comments/reviews in these repos normally have a
    # Slack copy. Missing copies make GitHub and Slack disagree; the base has a few exceptions, so warn.
    MIRROR = {"harmonygames-Games/GameOfDominoes": "C050WGU41HR",
              "harmonygames-Games/game-of-dominoes-backend": "C050WGU41HR",
              "harmonygames-Games/match3d": "C093LEZGF6J"}
    warnings = []
    slack_att = defaultdict(str)
    for x in ins.get("slack.slack_messages", []):
        slack_att[x["row"].get("channel_id")] += " " + str(x["row"].get("attachments_json") or "") + " " + str(x["row"].get("text") or "")
    for tbl in ("github.github_pr_comments", "github.github_reviews", "github.github_review_comments"):
        for x in ins.get(tbl, []):
            pr = str(x["row"].get("pr_id") or "")
            repo, _, num = pr.partition("#")
            ch = MIRROR.get(repo)
            if ch and f"pull/{num}" not in slack_att.get(ch, ""):
                warnings.append({"line": x["line"], "table": tbl,
                                 "msg": f"{x['row'].get('id')} on {pr} has no Slack mirror copy in {ch} (GitHub app) — add one or justify"})

    return {"check_A": A, "check_C": C, "warnings": warnings, "notes": sorted(set(notes)),
            "verdict": "PASS" if not A and not C else "FAIL",
            "stats": {"statements": len(stmts), "inserts": sum(1 for s in stmts if s["op"] == "insert"),
                      "updates": sum(1 for s in stmts if s["op"] == "update")}}


def _channels_for_id(base, mid, new_slack_ts):
    """Channels worth scanning for a message id (UPDATE targets): channels the SQL touches."""
    return [c for c in new_slack_ts if c in base.slack()["channels"]]


def base_msgs_or_new(base, ch, new_slack_ts) -> dict:
    pool = {}
    if ch in base.slack()["channels"]:
        pool.update({ts: m.get("id") for ts, m in base.slack_messages(ch).items()})
    pool.update(new_slack_ts.get(ch, {}))
    return pool


def to_text(r: dict) -> str:
    lines = [f"BASE CHECK (/injection A + C, static): {r['verdict']}  — "
             f"{r['stats']['inserts']} inserts, {r['stats']['updates']} updates"]
    for name in ("check_A", "check_C"):
        lines.append(f"{'Check A — records, references, IDs' if name == 'check_A' else 'Check C — dates and relationships'}: "
                     f"{'PASS' if not r[name] else f'FAIL ({len(r[name])})'}")
        for f in r[name][:60]:
            lines.append(f"  line {f['line']}: {f['table']}: {f['msg']}")
        if len(r[name]) > 60:
            lines.append(f"  … {len(r[name]) - 60} more (use --json)")
    if r.get("warnings"):
        lines.append(f"Warnings ({len(r['warnings'])}):")
        for f in r["warnings"][:30]:
            lines.append(f"  line {f['line']}: {f['table']}: {f['msg']}")
    for n in r["notes"]:
        lines.append(f"  note: {n}")
    return "\n".join(lines)


def _self_test() -> None:
    real_ch, real_user = "C080X4GTZ0E", None
    b = Base()
    real_user = b.slack()["users"][0]
    base_msgs = b.slack_messages(real_ch)
    parent_ts = sorted(base_msgs)[-1]
    ts = "1770634800.000100"
    good_id = hashlib.sha256(f"{real_ch}|{ts}".encode()).hexdigest()[:32]
    sql = f"""-- Are you planning to inject? Yes
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, created_at) VALUES ('{good_id}', '{ts}', '{real_ch}', 'message', '{real_user}', 'x', '2026-02-09T11:00:00Z');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, created_at) VALUES ('bad', '1770634900.000100', 'CNOPE', 'message', 'UNOPE', 'x', '2026-02-09T11:01:40Z');
INSERT INTO linear.linear_comments (id, issue_id, author_id, body, created_at) VALUES ('cmt_selftest', 'ENG-999999', 'usr_nope', 'x', '2026-02-09T11:00:00Z');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_ts_legacy, created_at) VALUES ('{hashlib.sha256(f"{real_ch}|1600000000.000100".encode()).hexdigest()[:32]}', '1600000000.000100', '{real_ch}', 'message', '{real_user}', 'reply', '{parent_ts}', '2020-09-13T12:26:40Z');
"""
    r = check(sql, b)
    msgs = " | ".join(f["msg"] for f in r["check_A"] + r["check_C"])
    for needle in ("channel CNOPE does not exist", "breaks the Slack id contract", "user UNOPE", "issue ENG-999999 does not exist",
                   "is not a linear user", "is not after its parent", "without an UPDATE of the parent"):
        assert needle in msgs, (needle, msgs)
    assert not any(good_id in f["msg"] for f in r["check_A"]), "valid row flagged"
    print("self-test: ok")


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        _self_test()
        return 0
    paths = [a for a in argv if not a.startswith("--")]
    if len(paths) != 1:
        print(__doc__, file=sys.stderr)
        return 2
    r = check(Path(paths[0]).read_text())
    print(json.dumps(r, indent=2) if "--json" in argv else to_text(r))
    return 0 if r["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
