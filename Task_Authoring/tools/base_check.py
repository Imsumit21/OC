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
    * Slack <@user> / <#channel> mentions, Gmail in_reply_to (same mailbox), Trello
      checklist → card → board and check item → checklist, card/item members, idShort
      unique per board, Linear state names, Drive/Docs/Sheets/Slides owner and share
      entries @harmonygames.co are real people
  Check C — dates, relationships and coherence (QC Cross-service Coherence categories)
    * replies follow their parents (Slack ts, Linear/GitHub/Confluence comments after
      their issue/PR/page, Gmail replies after the message they answer, Trello actions
      after the card exists); Slack posts are not older than their channel
    * calendar events end after they start; Slack created_at agrees with ts
    * a reply added to an existing Slack thread is paired with an UPDATE of the parent's
      reply_count / latest_reply, and every parent's counters equal its replies
    * GCal: every attendee/organizer with a calendar holds a copy (same ical_uid); copies
      agree on time, status and title
    * Docs/Sheets/Slides owner + sharing mirror their drive_files row
    * Linear lifecycle after UPDATEs (sql_lint.linear_lifecycle); issue updated_at is not
      older than its comments; Linear ids and github.com/…/pull/N links cited in any text resolve
    * GitHub: every PR comment has its 'commented' timeline event; PR updated_at covers
      seeded activity
    * Trello badges (comments, checkItems, checkItemsChecked) and dateLastActivity follow
      the comments / check items the SQL adds
    * Confluence versions continue 1..N contiguously, page.version = newest, and
      ri:content-title links resolve
  Warnings: posts into archived channels, comments dated after their issue closed (QC
  appendix "Closed with later activity" — disposition each), Linear state not used by
  that team.
  Integrity layer (references/universe_kb):
    * Hazard touch — the SQL updates, or seeds records referencing, an id listed in
      coherence_hazards.json: warning; FAIL when the SQL itself modifies a record of a
      state_lifecycle or cross_service_referential hazard. An acknowledgement never downgrades
      that FAIL by itself (harness red team A, R1 #4): the only escape is the manifest's
      hazard_acknowledgements entry with `resolution: repaired`, and only when the hazard
      predicate re-evaluated on the post-SQL state shows the inconsistency gone (supported:
      Linear L01-L07; any other hazard type FAILs as unverifiable). `excluded` and
      `dated_claim` never apply to a record the SQL modifies
    * Integration companions (integrations.json): INT-01 a seeded PR open / merge / comment /
      review inside a mirrored repo's window needs its GitHub-app Slack copy threaded under the
      PR's 'opened' message; INT-03 a seeded PR naming a Linear key (in linear[bot]'s active
      repo window) needs the linear[bot] comment; INT-11 a seeded meeting with attendees needs
      invitation mails. Severity from the base rate: FAIL at >= 95% (n >= 20), warning at >= 50%.
      The manifest's integration_exceptions [{record_id, reason}] waives a record (e.g. no_notify)
    * Voice realism (activity.json): a seeded message whose author has no authored activity
      within ±60 days is a warning; one dated after the author's departure signal (status
      quiet_since_*, after last_authored_activity) is a FAIL

It reads the exports directly (read-only) and caches small indexes in
`Task_Authoring/support/local_search/cache/`. Nothing under Evals/, claude/ or HarmonyGames_* is
written. Like `/injection`, it is static: it does not prove the SQL deploys.

Usage:
  python3 Task_Authoring/tools/base_check.py <injection.sql> [--manifest 01_Hardness_Manifest.json] [--json]
  python3 Task_Authoring/tools/base_check.py --self-test
Exit 0 = PASS, 1 = FAIL, 2 = usage error.
"""
from __future__ import annotations

import datetime as dt
import email.utils
import glob
import hashlib
import html
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
        from runtime_context import ensure_active
        ensure_active(globals(), require_source=True)
        self._c = {}
        self._context_hash = globals().get("TASK_CONTEXT", {}).get("context_hash")

    def _get(self, key, build):
        from runtime_context import ensure_active
        ensure_active(globals(), require_source=True)
        current = globals().get("TASK_CONTEXT", {}).get("context_hash")
        if self._context_hash != current:
            self._c.clear()
            self._context_hash = current
        if key not in self._c:
            self._c[key] = build()
        return self._c[key]

    # slack
    def slack(self):
        def build():
            ch = _load(OTHER / "slack" / "channels.json")
            us = _load(OTHER / "slack" / "users.json")
            return {"channels": {c["id"]: c.get("members") or [] for c in ch}, "users": [u["id"] for u in us],
                    "created": {c["id"]: float(c.get("created") or 0) for c in ch},
                    "archived": [c["id"] for c in ch if c.get("is_archived")],
                    "emails": [str(u.get("email") or "").lower() for u in us if u.get("email")]}
        return self._get("slack", lambda: _cached("slack_v2", build))

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
                    "attachments": [a["id"] for a in d.get("attachments") or []],
                    "rec": {i["id"]: {k: i.get(k) for k in ("state_id", "team_id", "created_at", "started_at",
                                                            "completed_at", "canceled_at", "updated_at")}
                            for i in d["issues"]},
                    "team_states": {t["id"]: sorted({i["state_id"] for i in d["issues"] if i["team_id"] == t["id"]})
                                    for t in d["teams"]},
                    "emails": [str(u.get("email") or "").lower() for u in d["users"]]}
        return self._get("linear", lambda: _cached("linear_v2", build))

    def linear_tree(self):
        """{issue id: [state_id, completed_at, parent_id]} — the post-SQL hazard predicates (resolution: repaired)."""
        def build():
            d = _load(OTHER / "linear" / "data.json")
            return {i["id"]: [i.get("state_id"), i.get("completed_at"), i.get("parent_id")] for i in d["issues"]}
        return self._get("linear_tree", lambda: _cached("linear_tree_v1", build))

    def github(self):
        def build():
            d = _load(GITHUB)
            return {"users": [u["login"] for u in d["users"]], "repos": [r["id"] for r in d["repositories"]],
                    "prs": {p["id"]: p.get("created_at") for p in d["pull_requests"]},
                    "pr_comments": [c["id"] for c in d["pull_request_comments"]],
                    "review_comments": [c["id"] for c in d["review_comments"]],
                    "reviews": [c["id"] for c in d["reviews"]],
                    "timeline": [c["id"] for c in d["timeline_events"]],
                    "commits": [c["sha"] for c in d["commits"]],
                    "pr_updated": {p["id"]: p.get("updated_at") for p in d["pull_requests"]}}
        return self._get("github", lambda: _cached("github_v2", build))

    def gmail(self):
        def build():
            idx = {}
            for f in glob.glob(str(GMAIL / "threads" / "*.json")):
                try:
                    d = _load(Path(f))
                except ValueError:
                    continue
                # persona_view reads the 4th field (thread file name) from this same index
                idx[d["id"]] = [d.get("user_email"), [m.get("id") for m in d.get("messages", [])],
                                [m.get("date") for m in d.get("messages", [])], os.path.basename(f)]
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
            uids = defaultdict(list)
            for e in d["events"]:
                uids[e.get("ical_uid")].append(e["calendar_id"])
            return {"calendars": [c["calendar_id"] for c in d["calendars"]],
                    "events": [f"{e['calendar_id']}|{e['event_id']}" for e in d["events"]],
                    "uids": uids}
        return self._get("gcal", lambda: _cached("gcal_v2", build))

    def trello(self):
        def build():
            d = _load(OTHER / "trello" / "data.json")
            return {"boards": [b["id"] for b in d["boards"]], "lists": {l["id"]: l["idBoard"] for l in d["lists"]},
                    "cards": {c["id"]: c["idBoard"] for c in d["cards"]}, "members": [m["id"] for m in d["members"]],
                    "actions": [a["id"] for a in d["actions"]], "labels": [x["id"] for x in d["labels"]],
                    "checklists": [x["id"] for x in d["checklists"]], "check_items": [x["id"] for x in d["check_items"]],
                    "checklist_card": {x["id"]: x["idCard"] for x in d["checklists"]},
                    "badges": {c["id"]: [(c.get("badges") or {}).get(k) for k in ("comments", "checkItems", "checkItemsChecked")]
                               for c in d["cards"]},
                    "idshort": [f"{c['idBoard']}|{c.get('idShort')}" for c in d["cards"]]}
        return self._get("trello", lambda: _cached("trello_v2", build))

    def confluence(self):
        def build():
            d = _load(OTHER / "confluence" / "confluence_working.json")
            return {"users": [u["id"] for u in d["users"]], "spaces": [s["id"] for s in d["spaces"]],
                    "pages": {p["id"]: p.get("created_at") for p in d["pages"]},
                    "comments": [c["id"] for c in d["comments"]],
                    "versions": [f"{v['page_id']}|{v['number']}" for v in d["page_versions"]],
                    "titles": [p["title"] for p in d["pages"]],
                    "page_version": {p["id"]: p.get("version") for p in d["pages"]}}
        return self._get("confluence", lambda: _cached("confluence_v2", build))

    def drive(self):
        def build():
            d = _load(OTHER / "gdrive" / "data.json")
            return {"files": {f["id"]: f.get("mime_type") for f in d["drive_files"]},
                    "users": [u.get("email") for u in d.get("drive_users", [])],
                    "meta": {f["id"]: [str(f.get("owner_email") or "").lower(),
                                       sorted(str(x).lower() for x in (f.get("shared_with_emails") or []))]
                             for f in d["drive_files"]}}
        return self._get("drive", lambda: _cached("drive_v2", build))

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
            return {"ids": [c["contact_id"] for c in d["contacts"]],
                    "emails": [str(c.get("email") or "").lower() for c in d["contacts"] if c.get("email")]}
        return self._get("contacts", lambda: _cached("contacts_v2", build))

    def people(self) -> set:
        """Every identity the base knows by email (Drive users, mailboxes, Slack/Linear users, contacts)."""
        def build():
            ppl = {str(e).lower() for e in self.drive()["users"] if e}
            ppl |= {str(v[0]).lower() for v in self.gmail().values()}
            ppl |= set(self.slack()["emails"]) | set(self.linear()["emails"]) | set(self.contacts()["emails"])
            return ppl
        return self._get("people", build)

    def mailboxes(self) -> set:
        return self._get("mailboxes", lambda: {str(v[0]).lower() for v in self.gmail().values() if v and v[0]})

    def gh_mirror(self) -> dict:
        """GitHub-app Slack mirror index: 'opened' parents per PR (repo#N -> [channel, ts]), streamed one
        month file at a time from the two mirror channels."""
        def build():
            opened = {}
            for ch in sorted(set(MIRROR_CHANNELS.values())):
                for f in sorted(glob.glob(str(OTHER / "slack" / "messages" / ch / "*.json"))):
                    for m in _load(Path(f)):
                        kind, pr = mirror_kind(m.get("attachments"))
                        if kind == "opened" and pr and not (m.get("thread_ts") and m.get("thread_ts") != m.get("ts")):
                            opened.setdefault(pr, [ch, m.get("ts")])
            return {"opened": opened}
        return self._get("gh_mirror", lambda: _cached("gh_mirror_v1", build))

    def gh_integrations(self) -> dict:
        """linear[bot] windows and keyed-PR rates per repo; non-User GitHub logins (bots/apps)."""
        def build():
            d = _load(GITHUB)
            keys = sorted({t.split("_", 1)[1] for t in self.linear()["teams"]})
            rx = re.compile(r"\b(" + "|".join(keys) + r")-\d{1,5}\b")
            bots = sorted(u["login"] for u in d["users"] if u.get("type") != "User")
            win, botprs = {}, set()
            for c in d["pull_request_comments"]:
                if c.get("author_login") == LINEAR_BOT:
                    repo, t = c["pr_id"].split("#")[0], str(c.get("created_at") or "")
                    w = win.setdefault(repo, [t, t])
                    w[0], w[1] = min(w[0], t), max(w[1], t)
                    botprs.add(c["pr_id"])
            keyed = {}
            for p in d["pull_requests"]:
                repo = p["id"].split("#")[0]
                w = win.get(repo)
                if w and rx.search(f"{p.get('title') or ''} {p.get('head_ref') or ''}") and w[0][:10] <= str(p.get("created_at"))[:10] <= w[1][:10]:
                    k = keyed.setdefault(repo, [0, 0])
                    k[0] += 1
                    k[1] += p["id"] in botprs
            del d
            return {"bots": bots, "linear_bot_window": win, "keyed_in_window": keyed}
        return self._get("gh_int", lambda: _cached("gh_integrations_v1", build))


# ---------------------------------------------------------------- checks

def _t(v):
    if v is None:
        return None
    if re.fullmatch(r"\d{10}(\.\d+)?", str(v)):
        return dt.datetime.fromtimestamp(float(v), dt.timezone.utc)
    t = parse_time(str(v))
    if t is None and re.match(r"[A-Z][a-z]{2}, ", str(v)):  # RFC 2822 dates in the Gmail index
        try:
            t = email.utils.parsedate_to_datetime(str(v)).astimezone(dt.timezone.utc)
        except (TypeError, ValueError):
            t = None
    return t


def _json_list(v):
    try:
        x = json.loads(v) if isinstance(v, str) else v
        return x if isinstance(x, list) else []
    except ValueError:
        return []


def check(sql: str, base: Base | None = None, manifest: dict | None = None) -> dict:
    """Checks A + C. `manifest` (optional, the hardness manifest) supplies `integration_exceptions`
    (declared no-companion records) and `hazard_acknowledgements` ({hazard_id, resolution, why_safe}; only
    `resolution: repaired` with a verified post-SQL predicate clears a hazard the SQL modifies)."""
    base = base or Base()
    stmts = parse_sql(sql)
    A, C, notes = [], [], []

    def fa(s, msg):
        A.append({"line": s["line"], "table": s["table"], "msg": msg})

    def fc(s, msg):
        C.append({"line": s["line"], "table": s["table"], "msg": msg})

    warnings = []

    def fw(s, msg):
        warnings.append({"line": s["line"], "table": s["table"], "msg": msg})

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
            born = base.slack()["created"].get(ch)
            if born and _t(ts) and _t(ts).timestamp() < born - 1:
                fc(s, f"message ts {ts} ({_t(ts):%Y-%m-%d}) predates channel {ch}'s creation "
                      f"({dt.datetime.fromtimestamp(born, dt.timezone.utc):%Y-%m-%d}) — Temporal")
            if ch in base.slack()["archived"]:
                fw(s, f"posts into archived channel {ch} — State/Lifecycle unless the post predates the archive")
            for mention in re.findall(r"<@([A-Z0-9_]+)(?:\|[^>]*)?>", str(r.get("text") or "")):
                if mention not in base.slack()["users"] and mention not in new_slack_users:
                    fa(s, f"text mentions <@{mention}>, which is not a Slack user")
            for cm in re.findall(r"<#(C[A-Z0-9]+)", str(r.get("text") or "")):
                if cm not in base.slack()["channels"] and cm not in new_channels:
                    fa(s, f"text links channel <#{cm}>, which does not exist")
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
            irt = (r.get("in_reply_to") or "").strip()
            if irt:
                pool = {str(k).split("/", 1)[-1]: v for k, v in new_gmail_msgs.items()
                        if str(k).startswith(f"{ue}/")}
                if tid in base.gmail():
                    pool.update({str(k).split("/", 1)[-1]: v for k, v in zip(base.gmail()[tid][1], base.gmail()[tid][2])})
                key = irt.split("/", 1)[-1] if not irt.startswith("<") else irt
                if key not in pool:
                    fa(s, f"in_reply_to {irt} does not resolve to a message in mailbox {ue} (base thread or SQL)")
                elif _t(r.get("date")) and _t(pool[key]) and _t(r.get("date")) < _t(pool[key]):
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

    cross_checks(stmts, ins, base, fa, fc, fw)

    # Integrity layer (universe_kb): pre-existing hazards the SQL touches, integration companions
    # (GitHub app → Slack mirror, linear[bot], calendar invitations) and voice realism.
    manifest = manifest or {}
    exceptions = {str(e.get("record_id")): str(e.get("reason") or "") for e in manifest.get("integration_exceptions", [])
                  if isinstance(e, dict) and e.get("record_id")}
    acks = {str(a.get("hazard_id")): a for a in manifest.get("hazard_acknowledgements", []) or []
            if isinstance(a, dict) and a.get("hazard_id")}
    hazards = hazard_touch(stmts, ins, base, fc, fw, acks)
    integration_companions(stmts, ins, base, fc, fw, exceptions, notes)
    voice_realism(stmts, ins, base, fc, fw)

    return {"check_A": A, "check_C": C, "warnings": warnings, "notes": sorted(set(notes)),
            "hazards_touched": hazards,
            "verdict": "PASS" if not A and not C else "FAIL",
            "stats": {"statements": len(stmts), "inserts": sum(1 for s in stmts if s["op"] == "insert"),
                      "updates": sum(1 for s in stmts if s["op"] == "update")}}


TEXT_COLS = ("text", "body", "body_text", "description", "desc", "title", "name", "summary", "snippet",
             "message", "data_json", "subject")
INTERNAL = "@harmonygames.co"


def _rows(ins, table):
    return [(x, x["row"]) for x in ins.get(table, [])]


def _updates(stmts, table):
    return [x for x in stmts if x["op"] == "update" and x["table"] == table]


def cross_checks(stmts, ins, base, fa, fc, fw) -> None:
    """Cross-record rules (each measured at ~100% in the base export; rates in the messages)."""
    # ---- Slack thread counters on parents the SQL inserts or updates
    replies = defaultdict(list)  # (channel, parent_ts) -> [(ts, user)]
    for x, r in _rows(ins, "slack.slack_messages"):
        ch, ts = r.get("channel_id"), r.get("ts")
        p = r.get("thread_ts_legacy") or r.get("thread_parent_id")
        if not p or p == ts or p == r.get("id"):
            continue
        if not re.fullmatch(r"\d{10}\.\d+", str(p)):
            p = next((k for k, v in base_msgs_or_new(base, ch, {ch: {y["row"].get("ts"): y["row"].get("id")
                      for y in ins.get("slack.slack_messages", []) if y["row"].get("channel_id") == ch}}).items() if v == p), p)
        replies[(ch, p)].append((ts, r.get("user_id")))
    for x, r in _rows(ins, "slack.slack_messages"):
        reps = replies.get((r.get("channel_id"), r.get("ts")))
        if not reps:
            if r.get("reply_count") not in (None, "0") and not (r.get("thread_ts_legacy") or r.get("thread_parent_id")):
                fc(x, f"parent {r.get('id')} declares reply_count {r.get('reply_count')} but the SQL inserts no replies to it")
            continue
        exp = (len(reps), max(t for t, _ in reps), len({u for _, u in reps}))
        got = (r.get("reply_count"), r.get("latest_reply"), r.get("reply_users_count"))
        if str(got[0]) != str(exp[0]) or (got[1] and got[1] != exp[1]) or (got[2] is not None and str(got[2]) != str(exp[2])):
            fc(x, f"thread counters reply_count/latest_reply/reply_users_count = {got} but its SQL replies give {exp} "
                  "(base: 16,797/16,799 parents match their replies)")
    for x in _updates(stmts, "slack.slack_messages"):
        pid, rc = x["where"].get("id"), x["set"].get("reply_count")
        if rc is None:
            continue
        for (ch, pts), reps in replies.items():
            pool = base.slack_messages(ch) if ch in base.slack()["channels"] else {}
            if pts in pool and pool[pts].get("id") == pid:
                exp = int(pool[pts].get("reply_count") or 0) + len(reps)
                if str(rc) != str(exp):
                    fc(x, f"UPDATE sets reply_count {rc} on {pid}; base {pool[pts].get('reply_count') or 0} + {len(reps)} new replies = {exp}")
                lr = x["set"].get("latest_reply")
                newest = max([t for t, _ in reps] + [t for t, m in pool.items() if m.get("thread_ts") == pts and t != pts],
                             key=float)
                if lr and lr != newest:
                    fc(x, f"UPDATE sets latest_reply {lr}; the newest reply (base or SQL) is {newest}")

    # ---- Google Calendar: one copy per attendee/organizer calendar, copies agree
    cals = set(base.gcal()["calendars"]) | {r.get("calendar_id") for _, r in _rows(ins, "gcal.gcal_calendars")}
    sql_uids = defaultdict(dict)
    for x, r in _rows(ins, "gcal.gcal_events"):
        sql_uids[r.get("ical_uid")][str(r.get("calendar_id")).lower()] = r
    for uid, copies in sql_uids.items():
        if not uid:
            continue
        first = next(iter(copies.values()))
        for cal, r in copies.items():
            for k in ("start_ts", "end_ts", "status", "summary"):
                if _t(r.get(k)) != _t(first.get(k)) if k.endswith("_ts") else r.get(k) != first.get(k):
                    fc(next(x for x, rr in _rows(ins, "gcal.gcal_events") if rr is r),
                       f"copies of event {uid} disagree on {k} ({first.get('calendar_id')} vs {cal})")
                    break
        people = set()
        for r in copies.values():
            try:
                people |= {str(a.get("email", "")).lower() for a in json.loads(r.get("attendees_json") or "[]") if isinstance(a, dict)}
            except ValueError:
                pass
            if r.get("organizer_email"):
                people.add(str(r["organizer_email"]).lower())
        have = set(copies) | {str(c).lower() for c in base.gcal()["uids"].get(uid, [])}
        for who in sorted(people - have):
            if who in {str(c).lower() for c in cals}:
                fc(next(x for x, rr in _rows(ins, "gcal.gcal_events") if rr is first),
                   f"event {uid}: {who} is an attendee/organizer with a calendar but has no copy of the event "
                   "(base: 102,026/102,026 attendee copies and 9,186/9,186 organizer copies exist)")

    # ---- Drive family: real people in owner/share fields; Docs/Sheets/Slides mirror their drive_files row
    sql_drive = {r.get("id"): r for _, r in _rows(ins, "gdrive.drive_files")}
    ppl = base.people()

    def share_list(v):
        try:
            return sorted(str(e).lower() for e in (json.loads(v) if v else []) or [])
        except (ValueError, TypeError):
            return []
    for t in ("gdrive.drive_files", "gdocs.docs_documents", "gsheets.sheets_spreadsheets", "gslides.slides_presentations"):
        for x, r in _rows(ins, t):
            named = [str(r.get("owner_email") or "").lower()] + share_list(r.get("shared_with_emails_json")) + share_list(r.get("owners_json"))
            for e in named:
                if e.endswith(INTERNAL) and e not in ppl:
                    fa(x, f"owner/share entry {e} is not a known HarmonyGames identity (Drive users, mailboxes, Slack/Linear users, contacts)")
            fid = r.get("drive_file_id")
            if t == "gdrive.drive_files" or not fid:
                continue
            if fid in sql_drive:
                d_owner, d_share = str(sql_drive[fid].get("owner_email") or "").lower(), share_list(sql_drive[fid].get("shared_with_emails_json"))
            elif fid in base.drive()["meta"]:
                d_owner, d_share = base.drive()["meta"][fid]
            else:
                continue
            if (str(r.get("owner_email") or "").lower(), share_list(r.get("shared_with_emails_json"))) != (d_owner, d_share):
                fc(x, f"{fid}: owner/sharing differ from its drive_files row (base: Docs/Sheets/Slides mirror Drive sharing, 633/633 docs)")

    # ---- Linear: lifecycle after UPDATEs, updated_at bumped by comments, comments on closed issues, references
    from sql_lint import linear_lifecycle
    L = base.linear()
    eff = {iid: dict(rec) for iid, rec in L["rec"].items()}
    for x, r in _rows(ins, "linear.linear_issues"):
        eff[r.get("id")] = dict(r)
        st = r.get("state_id")
        known = {s_ for v in L["team_states"].values() for s_ in v}
        if st and st not in known:
            fa(x, f"state_id {st!r} is not a workflow state used anywhere in the base ({sorted(known)})")
        elif st and r.get("team_id") in L["team_states"] and st not in L["team_states"][r["team_id"]]:
            fw(x, f"state_id {st!r} is not used by {r['team_id']} in the base (used: {L['team_states'][r['team_id']]})")
    for x in _updates(stmts, "linear.linear_issues"):
        iid = x["where"].get("id")
        if iid in eff:
            eff[iid].update({k: v for k, v in x["set"].items()})
            if set(x["set"]) & {"state_id", "started_at", "completed_at", "canceled_at", "updated_at", "created_at"}:
                for msg in linear_lifecycle(eff[iid]):
                    fc(x, f"{iid} after this UPDATE: State/Lifecycle — {msg}")
    late = []
    for x, r in _rows(ins, "linear.linear_comments"):
        iss = eff.get(r.get("issue_id"))
        ct = _t(r.get("created_at"))
        if not iss or not ct:
            continue
        up = _t(iss.get("updated_at"))
        if up and ct > up:
            fc(x, f"comment {r.get('id')} ({ct:%Y-%m-%d}) is newer than issue {r.get('issue_id')} updated_at "
                  f"{iss.get('updated_at')} — UPDATE the issue's updated_at (a comment updates the issue; GitHub base 884/884)")
        closed = _t(iss.get("completed_at")) or _t(iss.get("canceled_at"))
        if closed and ct > closed:
            late.append((x, f"{r.get('issue_id')}({iss.get('state_id')})"))
    if late:
        fw(late[0][0], f"{len(late)} comment(s) dated after their issue closed: {', '.join(sorted({i for _, i in late})[:8])}"
                       f"{' …' if len(late) > 8 else ''} — the QC appendix fails 'ticket Closed with later activity' when the "
                       "activity contradicts the status (work resumed, a fix still pending, a promise to change state); "
                       "neutral notes are fine — disposition each in the dossier")
    keys = sorted({t.split("_", 1)[1] for t in L["teams"]})
    known_ids = set(L["identifiers"]) | {r.get("identifier") or r.get("id") for _, r in _rows(ins, "linear.linear_issues")}
    rx = re.compile(r"\b(" + "|".join(keys) + r")-(\d{1,5})\b")
    known_prs = set(base.github()["prs"]) | {r.get("id") for _, r in _rows(ins, "github.github_pull_requests")}
    for tbl, rows in ins.items():
        for x in rows:
            blob = " ".join(str(x["row"].get(c) or "") for c in TEXT_COLS)
            for k, n in sorted(set(rx.findall(blob))):
                if f"{k}-{n}" not in known_ids:
                    fc(x, f"text references Linear {k}-{n}, which exists neither in the base nor in the SQL "
                          "(Cross-service Referential: dangling reference)")
            for repo, n in sorted(set(re.findall(r"github\.com/([\w.-]+/[\w.-]+)/pull/(\d+)", blob + " " + str(x["row"].get("attachments_json") or "")))):
                if f"{repo}#{n}" not in known_prs:
                    fc(x, f"text links PR {repo}#{n}, which does not exist in GitHub (base or SQL) — Cross-service Referential")

    # ---- GitHub: every PR comment has its 'commented' timeline event; PR updated_at covers new activity
    G = base.github()
    tl = {(r.get("pr_id"), str(_t(r.get("created_at")))) for _, r in _rows(ins, "github.github_timeline_events")
          if r.get("event") == "commented"}
    pr_upd = dict(G["pr_updated"])
    pr_upd.update({r.get("id"): r.get("updated_at") for _, r in _rows(ins, "github.github_pull_requests")})
    for x in _updates(stmts, "github.github_pull_requests"):
        if x["set"].get("updated_at"):
            pr_upd[x["where"].get("id")] = x["set"]["updated_at"]
    for t in ("github.github_pr_comments", "github.github_reviews", "github.github_review_comments", "github.github_timeline_events"):
        for x, r in _rows(ins, t):
            when = _t(r.get("created_at") or r.get("submitted_at"))
            up = _t(pr_upd.get(r.get("pr_id")))
            if when and up and when > up:
                fc(x, f"{r.get('id')} ({when:%Y-%m-%d}) is newer than PR {r.get('pr_id')} updated_at {pr_upd.get(r.get('pr_id'))} "
                      "— UPDATE the PR's updated_at (base: 884/884 PRs updated at or after their comments)")
            if t == "github.github_pr_comments" and (r.get("pr_id"), str(when)) not in tl:
                fc(x, f"{r.get('id')} has no matching 'commented' timeline event (same pr_id and created_at) — base pairs 884/884")

    # ---- Trello: checklists/items resolve; badges and activity follow comments and check items
    T = base.trello()
    sql_cards = {r.get("id"): r for _, r in _rows(ins, "trello.trello_cards")}
    sql_lists_card = {r.get("id"): r.get("idCard") for _, r in _rows(ins, "trello.trello_checklists")}
    for x, r in _rows(ins, "trello.trello_checklists"):
        card = r.get("idCard")
        board = (sql_cards.get(card) or {}).get("idBoard") or T["cards"].get(card)
        if board is None:
            fa(x, f"checklist {r.get('id')} points to card {card}, which does not exist")
        elif r.get("idBoard") and r["idBoard"] != board:
            fa(x, f"checklist {r.get('id')} names board {r['idBoard']} but card {card} is on {board}")
    items = defaultdict(lambda: [0, 0])
    for x, r in _rows(ins, "trello.trello_check_items"):
        cl = r.get("idChecklist")
        card = sql_lists_card.get(cl) or T["checklist_card"].get(cl)
        if card is None:
            fa(x, f"check item {r.get('id')} points to checklist {cl}, which does not exist")
            continue
        items[card][0] += 1
        items[card][1] += r.get("state") == "complete"
        if r.get("idMember") and r["idMember"] not in T["members"]:
            fa(x, f"check item {r.get('id')} assigns member {r['idMember']}, who does not exist")
    comments = defaultdict(list)
    for x, r in _rows(ins, "trello.trello_actions"):
        if r.get("type") == "commentCard" and r.get("idCard"):
            comments[r["idCard"]].append(r.get("date"))
    shorts = set(T["idshort"])
    for x, r in _rows(ins, "trello.trello_cards"):
        for m in share_list(r.get("idMembers_json")):
            if m not in {str(v).lower() for v in T["members"]}:
                fa(x, f"card {r.get('id')} lists member {m}, who does not exist")
        key = f"{r.get('idBoard')}|{r.get('idShort')}"
        if r.get("idShort") is not None and key in shorts:
            fa(x, f"card idShort {r.get('idShort')} is already used on board {r.get('idBoard')}")
        shorts.add(key)
        try:
            b = json.loads(r.get("badges_json") or "{}") or {}
        except ValueError:
            b = {}
        exp = {"comments": len(comments.get(r.get("id"), [])), "checkItems": items[r.get("id")][0],
               "checkItemsChecked": items[r.get("id")][1]}
        got = {k: b.get(k, 0 if not b else None) for k in exp}
        if got != exp:
            fc(x, f"card {r.get('id')} badges {got} disagree with its SQL comments/check items {exp} (base: 803/803 cards match)")
    upd_cards = {x["where"].get("id"): x for x in _updates(stmts, "trello.trello_cards")}
    for card, dates in comments.items():
        if card in sql_cards or card not in T["badges"]:
            continue
        u = upd_cards.get(card)
        exp = int(T["badges"][card][0] or 0) + len(dates)
        if not u or "badges_json" not in u["set"]:
            fc(next(x for x, r in _rows(ins, "trello.trello_actions") if r.get("idCard") == card),
               f"{len(dates)} new comment(s) on base card {card} without an UPDATE of its badges_json (comments → {exp}) and dateLastActivity")
            continue
        try:
            got = (json.loads(u["set"]["badges_json"] or "{}") or {}).get("comments")
        except ValueError:
            got = None
        if got != exp:
            fc(u, f"badges comments {got} on {card}; base {T['badges'][card][0] or 0} + {len(dates)} new = {exp}")
        dla = _t(u["set"].get('dateLastActivity'))
        if dla and any(_t(d) and _t(d) > dla for d in dates):
            fc(u, f"dateLastActivity {u['set'].get('dateLastActivity')} is older than a comment it should cover")

    # ---- Confluence: contiguous versions; page.version = newest; page links resolve
    Cf = base.confluence()
    page_upd = {x["where"].get("id"): x for x in _updates(stmts, "confluence.confluence_pages")}
    new_versions = defaultdict(list)
    for x, r in _rows(ins, "confluence.confluence_page_versions"):
        new_versions[r.get("page_id")].append((x, r.get("number")))
    sql_pages = {r.get("id"): r for _, r in _rows(ins, "confluence.confluence_pages")}
    for pg, vs in new_versions.items():
        start = int(Cf["page_version"].get(pg) or 0) if pg not in sql_pages else 0
        nums = sorted(int(n) for _, n in vs if n is not None)
        if nums != list(range(start + 1, start + 1 + len(nums))):
            fc(vs[0][0], f"page {pg} versions {nums} do not continue the base history 1..{start} contiguously")
        want = nums[-1] if nums else None
        have = (page_upd.get(pg) or {}).get("set", {}).get("version") if pg not in sql_pages else sql_pages[pg].get("version")
        if want and str(have) != str(want):
            fc(vs[0][0], f"page {pg}: newest version is {want} but the page row says version {have} — UPDATE the page with it")
    titles = set(Cf["titles"]) | {r.get("title") for r in sql_pages.values()}
    for t in ("confluence.confluence_pages", "confluence.confluence_page_versions", "confluence.confluence_comments"):
        for x, r in _rows(ins, t):
            for title in re.findall(r'ri:content-title="([^"]+)"', str(r.get("body") or "")):
                if html.unescape(title) not in titles:
                    fc(x, f"page link ri:content-title=\"{title}\" does not resolve to any page title")
    for x in _updates(stmts, "confluence.confluence_pages"):
        for title in re.findall(r'ri:content-title="([^"]+)"', str(x["set"].get("body") or "")):
            if html.unescape(title) not in titles:
                fc(x, f"page link ri:content-title=\"{title}\" does not resolve to any page title")


# ---------------------------------------------------------------- integrity layer (references/universe_kb)

KB = BUNDLE / "references" / "universe_kb"
ORG = "harmonygames-Games"
MIRROR_CHANNELS = {"GameOfDominoes": "C050WGU41HR", "game-of-dominoes-backend": "C050WGU41HR", "match3d": "C093LEZGF6J"}
LINEAR_BOT = "PERSON_6028_GITHUB_USERNAME"      # integrations.json INT-03 (author_login of linear[bot] comments)
HAZARD_FAIL_CATEGORIES = ("state_lifecycle", "cross_service_referential")
# Meetings (distinct ical_uid with non-organizer attendees) that have an 'Invitation:'/'Updated invitation:' mail
# with the same summary in some mailbox, and attendee mailboxes holding one (kb_gmail calendar_mails x gcal
# data.json, measured 2026-10-04). Below 95% -> a missing invitation is a warning, never a FAIL.
INVITE_RATE, INVITE_BOX_RATE = (836, 941), (2298, 2974)
_KB = {}


def kb(name: str):
    """A universe_kb JSON file (read once per process)."""
    from runtime_context import ensure_active
    ensure_active(globals(), require_source=True)
    if name not in _KB:
        from runtime_context import validate_kb
        _KB[name] = validate_kb(json.loads((KB / f"{name}.json").read_text()), globals())
    return _KB[name]


def mirror_kind(att):
    """(kind, 'harmonygames-Games/<repo>#N') of a GitHub-app Slack mirror message, from its attachments."""
    if isinstance(att, str):
        try:
            att = json.loads(att)
        except ValueError:
            return None, None
    if not isinstance(att, list) or not att or not isinstance(att[0], dict):
        return None, None
    a = att[0]
    head = f"{a.get('pretext') or ''} {a.get('fallback') or ''}".lower()
    blob = " ".join(str(a.get(k) or "") for k in ("fallback", "pretext", "title", "footer"))
    if "-games/" not in blob.lower() and "github" not in blob.lower():
        return None, None
    for needle, kind in (("pull request opened", "opened"), ("pull request merged", "merged"), ("pull request closed", "closed"),
                         ("ready for review", "ready"), ("review approved", "approved"), ("changes requested", "changes"),
                         ("review comment", "review_comment"), ("comment", "comment"), ("pushed", "push"), ("new commit", "push")):
        if needle in head:
            break
    else:
        return None, None
    m = re.search(r"-Games/([\w.-]+?)\]", blob) or re.search(r"-Games/([\w.-]+?)/pull/", blob) or re.search(r"-Games/([\w.-]+?)[|>]", blob)
    n = re.search(r"/pull/(\d+)", f"{a.get('title') or ''} {a.get('pretext') or ''}") or \
        re.search(r"#(\d+)", f"{a.get('title') or ''} {a.get('fallback') or ''}")
    return kind, (f"{ORG}/{m.group(1)}#{n.group(1)}" if m and n else None)


_HZ_RX = [re.compile(p) for p in (
    r"harmonygames-Games/[\w.-]+#\d+(?:#(?:c|ev|rev|rc)_\d+)?",
    r"(?<![A-Za-z0-9])(?:ENG|ZOM|ART|DES|EPI)-\d{1,5}(?![0-9])",
    r"(?<![A-Za-z0-9])evt_[0-9a-f]{22}(?![0-9a-f])",
    r"(?<![A-Za-z0-9])[fd]_[0-9a-f]{22}(?![0-9a-f])",
    r"(?<![0-9a-f])[0-9a-f]{32}@hg4",
    r"(?<![0-9A-Za-z_])[0-9a-f]{24}(?![0-9a-f])",
    r"(?<![A-Za-z0-9_])page_[a-z0-9_]+",
    r"(?<![A-Za-z0-9_])(?:EMPLOYEE|PERSON|SVC)_\d{4}_GITHUB_USERNAME")]
_SLACK_REF = re.compile(r"(?<![A-Za-z0-9])([CDG][A-Z0-9]{8,12})[/:](\d{10}\.\d{6})")
_GMAIL_FILE = re.compile(r"@harmonygames\.co_(\d{15,20})\.json")


def id_tokens(text) -> set:
    """Record ids cited in a string, normalised the way coherence_hazards.json examples are matched."""
    s = str(text or "")
    out = set()
    for rx in _HZ_RX:
        out |= set(rx.findall(s))
    out |= {f"{c}/{t}" for c, t in _SLACK_REF.findall(s)}
    out |= {f"gmail_thread:{t}" for t in _GMAIL_FILE.findall(s)}
    return out


def hazard_index():
    """token -> {hazard ids}; hazard id -> meta; slack message id (sha) -> 'C/ts' for hazard Slack examples."""
    if "hz_index" in _KB:
        return _KB["hz_index"]
    idx, meta, sha = defaultdict(set), {}, {}
    for cat, hz in kb("coherence_hazards")["categories"].items():
        for h in hz:
            meta[h["id"]] = {"category": h.get("category") or cat, "title": h.get("title"), "service": h.get("service"),
                             "count": h.get("count")}
            for ex in h.get("examples") or []:
                for tok in id_tokens(ex):
                    if tok.endswith("_GITHUB_USERNAME") and meta[h["id"]]["category"] == "identifier_format":
                        continue  # I08-style login tokenisation is a universe-wide convention, not a record defect
                    idx[tok].add(h["id"])
                    if re.fullmatch(r"[CDG][A-Z0-9]+/\d+\.\d+", tok):
                        c, t = tok.split("/")
                        sha[hashlib.sha256(f"{c}|{t}".encode()).hexdigest()[:32]] = tok
    _KB["hz_index"] = (idx, meta, sha)
    return _KB["hz_index"]


REF_COLS = ("issue_id", "parent_id", "pr_id", "idCard", "page_id", "drive_file_id", "ical_uid", "thread_parent_id",
            "in_reply_to_id", "author_login", "actor_login", "spreadsheet_id", "presentation_id", "document_id")


def touched_ids(stmts) -> tuple:
    """(modified, referenced): token -> [statements]. Modified = UPDATE/DELETE targets; referenced = foreign keys
    of seeded rows, base threads they join, and ids cited in seeded text."""
    _, _, sha = hazard_index()
    mod, ref = defaultdict(list), defaultdict(list)
    for s in stmts:
        if s["op"] in ("update", "delete"):
            for v in s["where"].values():
                for tok in id_tokens(v) | ({sha[v]} if v in sha else set()):
                    mod[tok].append(s)
                if s["table"].startswith("gmail.") and "/" in str(v):
                    mod[f"gmail_thread:{str(v).rsplit('/', 1)[-1]}"].append(s)
            for v in s["set"].values():
                for tok in id_tokens(v):
                    ref[tok].append(s)
            continue
        r = s["row"]
        for c in REF_COLS:
            v = r.get(c)
            if v:
                for tok in id_tokens(v) | ({sha[v]} if v in sha else set()):
                    ref[tok].append(s)
        if s["table"] == "slack.slack_messages" and r.get("thread_ts_legacy") and r.get("thread_ts_legacy") != r.get("ts"):
            ref[f"{r.get('channel_id')}/{r.get('thread_ts_legacy')}"].append(s)
        if s["table"].startswith("gmail.") and r.get("thread_id") and "/" in str(r.get("thread_id")):
            ref[f"gmail_thread:{str(r['thread_id']).rsplit('/', 1)[-1]}"].append(s)
        for c in TEXT_COLS + ("attachments_json", "body_text", "grid_json", "notes", "table_json"):
            for tok in id_tokens(r.get(c)):
                ref[tok].append(s)
    return mod, ref


LIN_OPEN_EXCLUDED = {"Done", "Canceled", "Duplicate"}
# Hazard predicates re-evaluable on the post-SQL state (resolution: repaired). token = a Linear issue key.
REPAIRABLE = {"L01": "issue state is 'PR' although a referencing PR merged",
              "L02": "issue state is 'Canceled' although a referencing PR merged",
              "L03": "issue state is Todo/Backlog although a referencing PR merged",
              "L04": "issue state is 'Done' although every referencing PR is unmerged",
              "L05": "completed_at set while the state is not Done",
              "L06": "parent Done while a child is open",
              "L07": "issue state is 'PR' (awaiting merge)"}
_LIN_KEY = re.compile(r"^(?:ENG|ZOM|ART|DES|EPI)-\d{1,5}$")


def linear_post_state(stmts, base) -> dict:
    """Linear issues after the SQL: base {id: [state_id, completed_at, parent_id]} + INSERT rows + UPDATE sets."""
    st = {k: list(v) for k, v in base.linear_tree().items()}
    for s in stmts:
        if s["table"] != "linear.linear_issues":
            continue
        if s["op"] == "insert":
            r = s["row"]
            st[str(r.get("id"))] = [r.get("state_id"), r.get("completed_at"), r.get("parent_id")]
        elif s["op"] == "update" and s["where"].get("id") in st:
            cur = st[s["where"]["id"]]
            for k, i in (("state_id", 0), ("completed_at", 1), ("parent_id", 2)):
                if k in s["set"]:
                    cur[i] = s["set"][k]
    return st


def _present(hid: str, key: str, st: dict, children: dict):
    """True / False = the hazard predicate holds / no longer holds for `key` on the post-SQL state."""
    state, completed, parent = st[key]
    if hid in ("L01", "L07"):
        return state == "PR"
    if hid == "L02":
        return state == "Canceled"
    if hid == "L03":
        return state in ("Todo", "Backlog")
    if hid == "L04":
        return state == "Done"
    if hid == "L05":
        return completed not in (None, "", "None", "NULL") and state != "Done"
    if hid == "L06":
        kids = children.get(key, [])
        if kids:   # the token is the Done parent
            return state == "Done" and any(st[k][0] not in LIN_OPEN_EXCLUDED for k in kids)
        return state not in LIN_OPEN_EXCLUDED and parent in st and st[parent][0] == "Done"
    return None


def repair_status(hid: str, tokens, stmts, base) -> tuple:
    """('repaired' | 'present' | 'unverifiable', detail): the hazard predicate re-evaluated on the post-SQL state."""
    if hid not in REPAIRABLE:
        return "unverifiable", (f"no post-SQL predicate for hazard type {hid} (supported: {', '.join(sorted(REPAIRABLE))})")
    keys = sorted({t for t in tokens if _LIN_KEY.match(str(t))})
    st = linear_post_state(stmts, base)
    keys = [k for k in keys if k in st]
    if not keys:
        return "unverifiable", f"no Linear issue among the touched tokens {sorted(tokens)[:4]} to evaluate {hid} on"
    children = defaultdict(list)
    for k, v in st.items():
        if v[2]:
            children[v[2]].append(k)
    still = [k for k in keys if _present(hid, k, st, children)]
    if still:
        return "present", f"{REPAIRABLE[hid]} still holds after the SQL for {still[:4]} (state {[st[k][0] for k in still[:4]]})"
    return "repaired", f"{REPAIRABLE[hid]} no longer holds after the SQL for {keys[:4]} (state {[st[k][0] for k in keys[:4]]})"


def hazard_touch(stmts, ins, base, fc, fw, acks: dict) -> list:
    """Pre-existing inconsistencies (coherence_hazards.json) the SQL updates or seeds references to."""
    idx, meta, _ = hazard_index()
    mod, ref = touched_ids(stmts)
    hits = {}
    for mode, pool in (("modified", mod), ("referenced", ref)):
        for tok, ss in pool.items():
            for hid in idx.get(tok, ()):
                h = hits.setdefault(hid, {"hazard_id": hid, **meta[hid], "tokens": set(), "modified": set(), "lines": set(), "stmt": ss[0]})
                h["tokens"].add(tok)
                h["lines"] |= {s["line"] for s in ss}
                if mode == "modified":
                    h["modified"].add(tok)
                    h["stmt"] = ss[0]
    out = []
    for hid, h in sorted(hits.items()):
        how = (f"UPDATE/DELETE of {sorted(h['modified'])[:4]}" if h["modified"] else f"seeded references to {sorted(h['tokens'])[:4]}")
        msg = (f"Hazard touch {hid} ({h['category']}: {h['title']}) — {how}. The task now contains a pre-existing "
               "inconsistency (Cross-Service Coherence fails on presence): keep it out or make the reconciliation the explicit job")
        ack = acks.get(hid) or {}
        res = str(ack.get("resolution") or "").strip().lower()
        repair = None
        if res == "repaired":
            repair, why = repair_status(hid, h["tokens"], stmts, base)
        if h["category"] in HAZARD_FAIL_CATEGORIES and h["modified"]:
            if res == "repaired" and repair == "repaired":
                fw(h["stmt"], msg + f" — resolution: repaired, verified on the post-SQL state: {why}")
            elif res == "repaired":
                fc(h["stmt"], msg + f" — resolution: repaired is not established ({repair}): {why}")
            elif res in ("excluded", "dated_claim"):
                fc(h["stmt"], msg + f" — resolution: {res} never applies to a record the SQL modifies (excluded = the record is "
                   "left untouched; dated_claim = a text claim only); repair it verifiably or drop the change")
            else:
                fc(h["stmt"], msg + " — the SQL itself modifies a State/Lifecycle or Referential hazard record; an acknowledgement "
                   "alone never changes the verdict: repair it (hazard_acknowledgements resolution: repaired, verified on the "
                   "post-SQL state) or drop the change")
        else:
            fw(h["stmt"], msg)
        out.append({"hazard_id": hid, "category": h["category"], "title": h["title"], "tokens": sorted(h["tokens"]),
                    "modified": sorted(h["modified"]), "lines": sorted(h["lines"]), "repair": repair})
    return out


def _sev(rate, n):
    """Severity of a missing companion from its base rate: FAIL at ≥ 95% (n ≥ 20), warning at ≥ 50%, else none."""
    if rate is None:
        return "warn"
    if rate >= 0.95 and n >= 20:
        return "error"
    return "warn" if rate >= 0.5 else None


def integration_companions(stmts, ins, base, fc, fw, exceptions: dict, notes: list) -> None:
    """integrations.json INT-01 (GitHub app → Slack mirror), INT-03 (linear[bot]) and INT-11 (calendar invitations)."""
    ints = {i["id"]: i for i in kb("integrations")["integrations"]}
    i01 = ints["INT-01"]
    windows = {repo: (_t(a), _t(b)) for repo, (a, b) in (i01.get("window") or {}).items()}
    per_repo, rates = i01["base_rates"]["per_repo"], i01["base_rates"]["comment_and_review_copy_rates"]

    def emit(sev, stmt, msg):
        (fc if sev == "error" else fw)(stmt, msg)

    def excepted(*ids):
        hit = [i for i in ids if i and str(i) in exceptions]
        if hit:
            notes.append(f"integration exception declared for {hit[0]}: {exceptions[str(hit[0])][:100]}")
        return bool(hit)

    gh_rows = any(ins.get(t) for t in ("github.github_pull_requests", "github.github_pr_comments", "github.github_reviews",
                                       "github.github_review_comments")) or any(
        s["op"] == "update" and s["table"] == "github.github_pull_requests" for s in stmts)
    sql_mirrors, sql_opened = defaultdict(list), {}
    for x in ins.get("slack.slack_messages", []):
        r = x["row"]
        kind, pr = mirror_kind(r.get("attachments_json"))
        if not kind or not pr:
            continue
        parent = r.get("thread_ts_legacy") if r.get("thread_ts_legacy") != r.get("ts") else None
        if kind == "opened" and not parent:
            sql_opened[pr] = (r.get("channel_id"), r.get("ts"))
        sql_mirrors[pr].append({"kind": kind, "x": x, "parent": parent, "ts": r.get("ts"), "ch": r.get("channel_id"), "used": False})

    # ---- INT-01: every seeded PR event inside a mirror window needs its Slack copy, threaded under 'opened'
    need = []
    if gh_rows or sql_mirrors:
        bots = set(base.gh_integrations()["bots"])
        opened_base = base.gh_mirror()["opened"]

        def short(pr):
            return str(pr).split("#")[0].split("/")[-1]

        def in_window(pr, when):
            w = windows.get(short(pr))
            return bool(w and when and w[0] <= when <= w[1])

        for x in ins.get("github.github_pull_requests", []):
            r, pr = x["row"], x["row"].get("id")
            pr_rates = per_repo.get(short(pr)) or {}
            if in_window(pr, _t(r.get("created_at"))):
                n = pr_rates.get("prs_in_window") or 0
                need.append((x, pr, pr, {"opened"}, (pr_rates.get("prs_with_opened_mirror") or 0) / n if n else None, n,
                             "PR opened", _t(r.get("created_at"))))
            if r.get("merged_at") and in_window(pr, _t(r.get("merged_at"))):
                n = pr_rates.get("merged_in_window") or 0
                need.append((x, pr, pr, {"merged"}, (pr_rates.get("merged_with_merged_mirror") or 0) / n if n else None, n,
                             "PR merge", _t(r.get("merged_at"))))
        for x in stmts:
            if x["op"] == "update" and x["table"] == "github.github_pull_requests" and x["set"].get("merged_at"):
                pr = x["where"].get("id")
                if pr and in_window(pr, _t(x["set"]["merged_at"])):
                    pr_rates = per_repo.get(short(pr)) or {}
                    n = pr_rates.get("merged_in_window") or 0
                    need.append((x, pr, pr, {"merged"}, (pr_rates.get("merged_with_merged_mirror") or 0) / n if n else None,
                                 n, "PR merge", _t(x["set"]["merged_at"])))
        for t, label in (("github.github_pr_comments", "PR comment"), ("github.github_review_comments", "review comment")):
            for x in ins.get(t, []):
                r = x["row"]
                pr, when = r.get("pr_id"), _t(r.get("created_at"))
                if in_window(pr, when):
                    v = rates.get(f"{short(pr)}/{'bot' if r.get('author_login') in bots else 'human'}") or {}
                    need.append((x, r.get("id"), pr, {"comment", "review_comment"}, v.get("rate"), v.get("github_records", 0),
                                 label, when))
        for x in ins.get("github.github_reviews", []):
            r = x["row"]
            pr, when, state = r.get("pr_id"), _t(r.get("submitted_at") or r.get("created_at")), str(r.get("state") or "").upper()
            kinds = {"APPROVED": {"approved"}, "CHANGES_REQUESTED": {"changes"}, "COMMENTED": {"review_comment", "comment"}}.get(state)
            if kinds and in_window(pr, when):
                v = rates.get(f"{short(pr)}/review_{state}") or {}
                need.append((x, r.get("id"), pr, kinds, v.get("rate"), v.get("github_records", 0), f"{state} review", when))

        for x, rid, pr, kinds, rate, n, label, when in sorted(need, key=lambda z: (str(z[7]), z[0]["line"])):
            if excepted(rid, pr):
                continue
            ch = MIRROR_CHANNELS.get(short(pr))
            cand = [m for m in sql_mirrors.get(pr, []) if m["kind"] in kinds and not m["used"] and m["ch"] == ch]
            if cand:
                m = cand[0]
                m["used"] = True
                if "opened" not in kinds:
                    parent = (sql_opened.get(pr) or (None, None))[1] or (opened_base.get(pr) or [None, None])[1]
                    if parent is None:
                        fc(m["x"], f"Slack mirror of {label} {rid} has no 'Pull request opened' parent for {pr} in {ch} "
                                   "(base or SQL) to thread under — base: 100% of comment/review/merge mirrors are threaded under it")
                    elif m["parent"] != parent:
                        fc(m["x"], f"Slack mirror of {label} {rid} is not threaded under {pr}'s 'opened' message {ch}/{parent} "
                                   f"(thread_ts {m['parent']}) — base: 100% threaded")
                continue
            sev = _sev(rate, n)
            if sev is None:
                continue
            pct = f"{rate:.0%} of {n}" if rate is not None else "rate unmeasured"
            emit(sev, x, f"{label} {rid} on {pr} ({when:%Y-%m-%d}, inside {short(pr)}'s GitHub-app mirror window) has no Slack "
                         f"mirror copy in {ch} threaded under the PR's 'opened' message (INT-01 base copy rate {pct}) — add it, "
                         "or declare integration_exceptions [{record_id, reason}]")

        for pr, ms in sql_mirrors.items():
            w = windows.get(short(pr))
            for m in ms:
                t = _t(m["ts"])
                if m["kind"] != "push" and t and not (w and w[0] <= t <= w[1]):
                    fw(m["x"], f"GitHub-app mirror message for {pr} dated {t:%Y-%m-%d} lies outside {short(pr)}'s mirror window "
                               f"({'never mirrored' if not w else f'{w[0]:%Y-%m-%d}..{w[1]:%Y-%m-%d}'}) — the base has no mirrors there (INT-01)")

    # ---- INT-03: a seeded PR naming a Linear key carries the linear[bot] comment (where the bot was active)
    if ins.get("github.github_pull_requests"):
        gi = base.gh_integrations()
        keys = sorted({t.split("_", 1)[1] for t in base.linear()["teams"]})
        rx = re.compile(r"\b(" + "|".join(keys) + r")-\d{1,5}\b")
        by_pr = defaultdict(list)
        for x in ins.get("github.github_pr_comments", []):
            by_pr[x["row"].get("pr_id")].append(x["row"])
        for x in ins["github.github_pull_requests"]:
            r, pr = x["row"], x["row"].get("id")
            m = rx.search(f"{r.get('title') or ''} {r.get('head_ref') or ''}")
            repo = str(pr).split("#")[0]
            w = gi["linear_bot_window"].get(repo)
            created = str(r.get("created_at") or "")[:10]
            if not m or not w or not (w[0][:10] <= created <= w[1][:10]) or excepted(pr):
                continue
            if any(c.get("author_login") == LINEAR_BOT or "linear.app/" in str(c.get("body") or "") for c in by_pr.get(pr, [])):
                continue
            n, k = gi["keyed_in_window"].get(repo, [0, 0])
            rate = k / n if n else None
            emit(_sev(rate, n) or "warn", x,
                 f"PR {pr} names Linear {m.group(0)} (created {created}, inside linear[bot]'s active window for {repo.split('/')[-1]} "
                 f"{w[0][:10]}..{w[1][:10]}) but has no linear[bot] comment ({LINEAR_BOT}, body linking linear.app/…/issue/{m.group(0)}) "
                 f"with its 'commented' timeline event (actor SVC_0323) — INT-03 base: {k}/{n} keyed PRs in that window carry it; "
                 "add it or declare integration_exceptions")

    # ---- INT-11: a seeded meeting with attendees has invitation mails (or a declared no_notify exception)
    if ins.get("gcal.gcal_events"):
        mailboxes = base.mailboxes() | {str(x["row"].get("user_email") or "").lower() for x in ins.get("gmail.gmail_threads", [])}
        subjects = defaultdict(list)
        for x in ins.get("gmail.gmail_messages", []):
            subjects[str(x["row"].get("user_email") or "").lower()].append(str(x["row"].get("subject") or ""))
        meetings = defaultdict(list)
        for x in ins["gcal.gcal_events"]:
            meetings[x["row"].get("ical_uid") or x["row"].get("event_id")].append(x)
        for uid, xs in meetings.items():
            r0 = xs[0]["row"]
            summary = str(r0.get("summary") or "").strip()
            att, org = set(), str(r0.get("organizer_email") or "").lower()
            for x in xs:
                for a in _json_list(x["row"].get("attendees_json")):
                    if isinstance(a, dict) and a.get("email"):
                        if a.get("organizer"):
                            org = str(a["email"]).lower()
                        else:
                            att.add(str(a["email"]).lower())
            att.discard(org)
            if not att or not summary or excepted(uid, *[x["row"].get("event_id") for x in xs]):
                continue
            inv = re.compile(r"^\s*(?:updated\s+)?invitation(?:\s+with\s+note)?:\s*" + re.escape(summary), re.I)
            boxes = (att | {org}) & mailboxes
            if not any(inv.match(sj) for b in boxes for sj in subjects.get(b, [])):
                fw(xs[0], f"meeting {uid} '{summary[:60]}' has {len(att)} attendee(s) but no invitation mail ('Invitation: {summary[:40]} @ …') "
                          f"in any attendee mailbox — INT-11 base: {INVITE_RATE[0]}/{INVITE_RATE[1]} meetings with attendees have one "
                          f"({INVITE_BOX_RATE[0]}/{INVITE_BOX_RATE[1]} attendee mailboxes); add the copies or declare "
                          "integration_exceptions [{record_id, reason: 'no_notify: …'}]")


class Activity:
    """activity.json + entities.json joins (exact email only) for 'who could plausibly author this, then'."""

    def __init__(self):
        a = kb("activity")
        self.people = a["people"]
        self.by_slack = {p["slack_id"]: e for e, p in self.people.items() if p.get("slack_id")}
        self.by_linear, self.by_github, self.by_conf, self.names = {}, {}, {}, {}
        for ent in kb("entities")["entities"]:
            if ent.get("kind") != "person" or not ent.get("emails"):
                continue
            em = str(ent["emails"][0]).lower()
            if em not in self.people:
                continue
            if ent.get("canonical_name"):
                self.names[em] = ent["canonical_name"]
            ids = ent.get("identities") or {}
            self.by_linear.update({i["id"]: em for i in ids.get("linear", []) if i.get("join") == "exact_email"})
            self.by_github.update({i["login"]: em for i in ids.get("github", []) if i.get("join") == "exact_email"})
            self.by_conf.update({i["id"]: em for i in ids.get("confluence", []) if i.get("join") == "exact_email"})
        self.months = {e: {m for m, n in (p.get("monthly_authored_total") or {}).items() if n} for e, p in self.people.items()}

    def name(self, email):
        p = self.people.get(email) or {}
        return self.names.get(email) or p.get("name") or email

    def judge(self, email: str, t) -> tuple | None:
        """('error'|'warn', reason) if `email` is implausible as an author at time t, else None."""
        p = self.people.get(email)
        if not p or t is None:
            return None
        st = str(p.get("status_at_clock") or "")
        last = (p.get("departure_signals") or {}).get("last_authored_activity")
        if st.startswith("quiet_since") and last and t.date() > dt.date.fromisoformat(last):
            return ("error", f"{t:%Y-%m-%d} is after {self.name(email)}'s departure signal "
                             f"(last authored activity {last}, status {st}; activity.json)")
        lo, hi = t - dt.timedelta(days=60), min(t + dt.timedelta(days=60), CLOCK)
        months, cur = set(), dt.date(lo.year, lo.month, 1)
        while cur <= hi.date():
            months.add(f"{cur:%Y-%m}")
            cur = dt.date(cur.year + (cur.month == 12), cur.month % 12 + 1, 1)
        if not (months & self.months.get(email, set())):
            return ("warn", f"{self.name(email)} has no authored activity within ±60 days of {t:%Y-%m-%d} "
                            f"(status {st or 'unknown'}; activity.json monthly_authored_total) — implausible voice")
        return None


def _activity() -> Activity:
    if "activity_obj" not in _KB:
        _KB["activity_obj"] = Activity()
    return _KB["activity_obj"]


def authored_rows(ins):
    """(statement, author email, time, record id) for every seeded human-authored message-like row."""
    act = _activity()
    seen_mail = set()
    for x in ins.get("slack.slack_messages", []):
        r = x["row"]
        if r.get("bot_id") or str(r.get("subtype") or "") == "bot_message":
            continue
        e = act.by_slack.get(r.get("user_id"))
        if e:
            yield x, e, _t(r.get("ts")) or _t(r.get("created_at")), r.get("id")
    for x in ins.get("gmail.gmail_messages", []):
        r = x["row"]
        m = re.search(r"[\w.+-]+@harmonygames\.co", str(r.get("from_email") or ""))
        rfc = str(r.get("id") or "").split("/", 1)[-1]
        if m and rfc not in seen_mail:
            seen_mail.add(rfc)
            yield x, m.group(0).lower(), _t(r.get("date")), r.get("id")
    for t, col, pool, when in (("linear.linear_comments", "author_id", act.by_linear, "created_at"),
                               ("linear.linear_issues", "creator_id", act.by_linear, "created_at"),
                               ("github.github_pr_comments", "author_login", act.by_github, "created_at"),
                               ("github.github_review_comments", "author_login", act.by_github, "created_at"),
                               ("github.github_reviews", "author_login", act.by_github, "submitted_at"),
                               ("confluence.confluence_comments", "author_id", act.by_conf, "created_at"),
                               ("confluence.confluence_page_versions", "author_id", act.by_conf, "created_at"),
                               ("confluence.confluence_pages", "author_id", act.by_conf, "created_at")):
        for x in ins.get(t, []):
            e = pool.get(x["row"].get(col))
            if e:
                yield x, e, _t(x["row"].get(when)), x["row"].get("id") or x["row"].get("identifier")


def voice_realism(stmts, ins, base, fc, fw) -> None:
    """A seeded message by someone inactive at that time (activity.json): warning; after their departure: FAIL."""
    act = _activity()
    agg = {}
    for x, email, t, rid in authored_rows(ins):
        v = act.judge(email, t)
        if v:
            key = (email, x["table"], v[0])
            a = agg.setdefault(key, {"x": x, "reason": v[1], "ids": []})
            a["ids"].append(rid)
    for (email, table, sev), a in sorted(agg.items(), key=lambda kv: kv[1]["x"]["line"]):
        n = len(a["ids"])
        msg = (f"Voice realism: seeded message by {act.name(email)} — {a['reason']}"
               + (f" — {n} rows in {table} (e.g. {', '.join(map(str, a['ids'][:3]))})" if n > 1 else f" — {a['ids'][0]}"))
        (fc if sev == "error" else fw)(a["x"], msg)


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

    # cross-record rules (anchors are real base records; see support/examples/calibration/injection/mutation_matrix.py)
    ch, ol, br = "C09R0KXFX71", "oliver.brooks@harmonygames.co", "brian.foster@harmonygames.co"
    old_ts = "1736694000.000100"  # 2025-01-12, before #engineering was created (2025-11-07)
    uid = "0f1e2d3c4b5a69788796a5b4c3d2e1f0@hg4"
    att = json.dumps([{"email": ol, "self": True}, {"email": br, "organizer": True}])
    sql2 = f"""-- Are you planning to inject? Yes
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, created_at) VALUES ('{hashlib.sha256(f"{ch}|{old_ts}".encode()).hexdigest()[:32]}', '{old_ts}', '{ch}', 'message', 'EMPLOYEE_0003_SLACK_ID', 'ping <@UNOBODY000> re ENG-2989, https://github.com/harmonygames-Games/Combo-Fighters/pull/99999 and https://github.com/harmonygames-Games/Combo-Fighters/pull/1', '2025-01-12T15:00:00Z');
INSERT INTO gcal.gcal_events (event_id, calendar_id, start_ts, end_ts, organizer_email, attendees_json, ical_uid) VALUES ('evt_0a1b2c3d4e5f60718293a4', '{ol}', '2026-01-14T17:00:00Z', '2026-01-14T17:30:00Z', '{br}', '{att}', '{uid}');
INSERT INTO linear.linear_comments (id, issue_id, author_id, body, created_at) VALUES ('cmt_selftest2', 'ENG-2022', 'usr_bdf01b53c6a92c5e', 'x', '2026-01-13T09:00:00Z');
UPDATE linear.linear_issues SET state_id = 'Done' WHERE id = 'ENG-2022';
INSERT INTO github.github_pr_comments (id, pr_id, author_login, body, created_at) VALUES ('harmonygames-Games/Combo-Fighters#1#c_900', 'harmonygames-Games/Combo-Fighters#1', 'EMPLOYEE_0003_GITHUB_USERNAME', 'x', '2026-02-01T10:00:00Z');
INSERT INTO trello.trello_actions (id, type, date, "idMemberCreator", "idBoard", "idCard", data_json) VALUES ('698b7230a1b2c3d4e5f6a7c2', 'commentCard', '2026-02-10T18:00:00Z', '12c4a9dcd2d37a25a8d3b557', '65eb4ec525346c8070ca638f', '6644fb2675ff166176503a1a', '{{"text":"x"}}');
INSERT INTO confluence.confluence_page_versions (id, page_id, number, title, body, created_at) VALUES ('ver_selftest', 'page_eng_home', 4, 'Engineering Home', '<ri:page ri:content-title="No Such Page"/>', '2026-01-13T11:00:00Z');
INSERT INTO gdrive.drive_files (id, name, mime_type, owner_email, shared_with_emails_json) VALUES ('f_0a1b2c3d4e5f60718293a4', 'x', 'application/vnd.google-apps.spreadsheet', '{ol}', '["nobody.here@harmonygames.co"]');
INSERT INTO gsheets.sheets_spreadsheets (spreadsheet_id, title, owner_email, shared_with_emails_json, drive_file_id) VALUES ('f_0a1b2c3d4e5f60718293a4', 'x', '{ol}', '[]', 'f_0a1b2c3d4e5f60718293a4');
"""
    r = check(sql2, b)
    msgs = " | ".join(f["msg"] for f in r["check_A"] + r["check_C"])
    for needle in ("predates channel", "not a Slack user", "ENG-2989, which exists neither", "has no copy of the event",
                   "newer than issue ENG-2022", "ENG-2022 after this UPDATE", "no matching 'commented' timeline event",
                   "newer than PR", "without an UPDATE of its badges_json", "do not continue the base history",
                   "does not resolve to any page title", "not a known HarmonyGames identity", "owner/sharing differ",
                   "Combo-Fighters#99999, which does not exist"):
        assert needle in msgs, (needle, msgs)
    assert "Combo-Fighters#1," not in msgs, "existing PR link flagged"
    assert any("dated after their issue closed" in w["msg"] for w in r["warnings"]) is False  # ENG-2022 was open in the base

    # integrity layer: hazard touch, integration companions, voice realism
    _self_test_integrity(b)
    print("self-test: ok")


def _self_test_integrity(b: Base) -> None:
    def sid(ch, ts):
        return hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]

    def msgs(res, key):
        return " | ".join(f["msg"] for f in res[key])

    # hazard touch: UPDATE of an L07 record (state 'PR') = FAIL; a text citation of an L01 record = warning
    ch, ol_u = "C09R0KXFX71", "EMPLOYEE_0003_SLACK_ID"
    ts = "1768231200.000100"
    sql = f"""-- Are you planning to inject? Yes
UPDATE linear.linear_issues SET updated_at = '2026-01-10T00:00:00Z' WHERE id = 'ENG-2414';
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, created_at) VALUES ('{sid(ch, ts)}', '{ts}', '{ch}', 'message', '{ol_u}', 'is ENG-2425 really done?', '2026-01-12T15:20:00Z');
"""
    r = check(sql, b)
    assert "Hazard touch L07" in msgs(r, "check_C"), msgs(r, "check_C")
    assert "Hazard touch L01" in msgs(r, "warnings") and "Hazard touch L01" not in msgs(r, "check_C")
    assert {h["hazard_id"] for h in r["hazards_touched"]} >= {"L07", "L01"}
    # an acknowledgement alone never downgrades the FAIL (red team A, R1 #4)
    r = check(sql, b, {"hazard_acknowledgements": [{"hazard_id": "L07", "why_safe": "the task's job is to reconcile it"}]})
    assert "Hazard touch L07" in msgs(r, "check_C") and "acknowledgement alone" in msgs(r, "check_C"), msgs(r, "check_C")
    r = check(sql, b, {"hazard_acknowledgements": [{"hazard_id": "L07", "resolution": "dated_claim", "why_safe": "x"}]})
    assert "never applies to a record the SQL modifies" in msgs(r, "check_C"), msgs(r, "check_C")
    # resolution: repaired is re-evaluated on the post-SQL state: still 'PR' -> FAIL; moved to Done -> warning only
    rep_ack = {"hazard_acknowledgements": [{"hazard_id": "L07", "resolution": "repaired", "why_safe": "x"}]}
    r = check(sql, b, rep_ack)
    assert "resolution: repaired is not established (present)" in msgs(r, "check_C"), msgs(r, "check_C")
    # (every touched token counts: the same SQL also cites ENG-2425, another L07 record still in 'PR')
    assert "ENG-2425" in msgs(r, "check_C")
    fixed = ("-- Are you planning to inject? Yes\nUPDATE linear.linear_issues SET state_id = 'Done', completed_at = "
             "'2026-01-10T00:00:00Z', updated_at = '2026-01-10T00:00:00Z' WHERE id = 'ENG-2414';\n")
    r = check(fixed, b, rep_ack)
    assert "Hazard touch L07" not in msgs(r, "check_C") and "verified on the post-SQL state" in msgs(r, "warnings"), msgs(r, "check_C")
    assert [h["repair"] for h in r["hazards_touched"] if h["hazard_id"] == "L07"] == ["repaired"]
    # a hazard type without a post-SQL predicate cannot be repaired verifiably -> FAIL as unverifiable
    assert repair_status("L11", {"641f7190800a4c4ac7031494"}, parse_sql(sql), b)[0] == "unverifiable"

    # INT-01: an APPROVED review inside the GameOfDominoes mirror window needs its threaded Slack copy (98.7% -> FAIL)
    prs = b.github()["prs"]
    opened = b.gh_mirror()["opened"]
    pr = max((p for p in opened if p.startswith(f"{ORG}/GameOfDominoes#") and p in prs
              and "2025-01-01" <= str(prs[p])[:10] <= "2025-10-01"), key=lambda p: int(p.rsplit("#", 1)[1]))
    mch, parent = opened[pr]
    when = (_t(prs[pr]) + dt.timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    rev = (f"INSERT INTO github.github_reviews (id, pr_id, author_login, state, body, submitted_at) VALUES "
           f"('{pr}#rev_900', '{pr}', 'EMPLOYEE_0025_GITHUB_USERNAME', 'APPROVED', '', '{when}');\n")
    mts = f"{_t(when).timestamp():.0f}.000200"
    num = pr.rsplit("#", 1)[1]

    def mirror(thread):
        att = json.dumps([{"fallback": f"[{ORG}/GameOfDominoes] Review approved by arthur.blake",
                           "pretext": "Review approved by <https://github.com/arthur.blake|arthur.blake>",
                           "title": f"Review on #{num} x"}]).replace("'", "''")
        return (f"INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_ts_legacy, attachments_json, bot_id, created_at) "
                f"VALUES ('{sid(mch, mts)}', '{mts}', '{mch}', 'message', 'SLACK_BOT_0004_SLACK_ID', '', '{thread}', '{att}', 'B0GITHUB', '{when}');\n")
    r = check("-- Are you planning to inject? Yes\n" + rev, b)
    assert "APPROVED review" in msgs(r, "check_C") and "no Slack mirror copy" in msgs(r, "check_C"), msgs(r, "check_C")
    r = check("-- Are you planning to inject? Yes\n" + rev + mirror("1600000000.000100"), b)
    assert "not threaded under" in msgs(r, "check_C"), msgs(r, "check_C")
    r = check("-- Are you planning to inject? Yes\n" + rev + mirror(parent), b)
    assert "no Slack mirror copy" not in msgs(r, "check_C") + msgs(r, "warnings") and "not threaded" not in msgs(r, "check_C")
    r = check("-- Are you planning to inject? Yes\n" + rev, b, {"integration_exceptions": [{"record_id": f"{pr}#rev_900", "reason": "x"}]})
    assert "no Slack mirror copy" not in msgs(r, "check_C") and any("integration exception" in n for n in r["notes"])

    # INT-03: a seeded GameOfDominoes PR naming an ENG key inside linear[bot]'s window needs the bot comment
    prsql = ("INSERT INTO github.github_pull_requests (id, repo_id, number, title, state, author_login, head_ref, created_at, updated_at) "
             f"VALUES ('{ORG}/GameOfDominoes#9901', '{ORG}/GameOfDominoes', 9901, 'ENG-2300 fix rewind', 'open', "
             "'EMPLOYEE_0025_GITHUB_USERNAME', 'fix/rewind', '2025-06-02T10:00:00Z', '2025-06-02T10:00:00Z');\n")
    r = check("-- Are you planning to inject? Yes\n" + prsql, b)
    assert "linear[bot]" in msgs(r, "check_C") + msgs(r, "warnings"), msgs(r, "check_C")

    # INT-11: a meeting with attendees and no invitation mail = warning; a no_notify exception waives it
    att = json.dumps([{"email": "brian.foster@harmonygames.co", "organizer": True},
                      {"email": "oliver.brooks@harmonygames.co", "self": True}])
    ev = ("INSERT INTO gcal.gcal_events (event_id, calendar_id, summary, start_ts, end_ts, organizer_email, attendees_json, ical_uid) VALUES "
          f"('evt_0a1b2c3d4e5f60718293a4', 'oliver.brooks@harmonygames.co', 'Handoff sync', '2026-01-14T17:00:00Z', '2026-01-14T17:30:00Z', "
          f"'brian.foster@harmonygames.co', '{att}', '0f1e2d3c4b5a69788796a5b4c3d2e1f0@hg4');\n")
    r = check("-- Are you planning to inject? Yes\n" + ev, b)
    assert "no invitation mail" in msgs(r, "warnings")
    r = check("-- Are you planning to inject? Yes\n" + ev, b,
              {"integration_exceptions": [{"record_id": "0f1e2d3c4b5a69788796a5b4c3d2e1f0@hg4", "reason": "no_notify: added by phone"}]})
    assert "no invitation mail" not in msgs(r, "warnings")

    # voice realism: Felix (quiet since 2024-08) posting in 2026 = FAIL; Leonard posting in 2022 = warning
    t1, t2 = "1768231300.000100", "1655000000.000100"
    sql = f"""-- Are you planning to inject? Yes
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, created_at) VALUES ('{sid(ch, t1)}', '{t1}', '{ch}', 'message', 'EMPLOYEE_0029_SLACK_ID', 'hi', '2026-01-12T15:21:40Z');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, created_at) VALUES ('{sid(ch, t2)}', '{t2}', '{ch}', 'message', 'EMPLOYEE_0038_SLACK_ID', 'hi', '2022-06-12T02:13:20Z');
"""
    r = check(sql, b)
    assert "departure signal" in msgs(r, "check_C") and "Felix Young" in msgs(r, "check_C"), msgs(r, "check_C")
    assert "no authored activity within ±60 days" in msgs(r, "warnings"), msgs(r, "warnings")


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        _self_test()
        return 0
    manifest = None
    if "--manifest" in argv:
        i = argv.index("--manifest")
        manifest = json.loads(Path(argv[i + 1]).read_text())
        argv = argv[:i] + argv[i + 2:]
    paths = [a for a in argv if not a.startswith("--")]
    if len(paths) != 1:
        print(__doc__, file=sys.stderr)
        return 2
    r = check(Path(paths[0]).read_text(), manifest=manifest)
    print(json.dumps(r, indent=2) if "--json" in argv else to_text(r))
    return 0 if r["verdict"] == "PASS" else 1


if __name__ == "__main__":
    from runtime_context import guarded_entry
    guarded_entry(globals(), require_source=True)
    raise SystemExit(main(sys.argv[1:]))
