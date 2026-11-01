#!/usr/bin/env python3
"""persona_view.py - read the HarmonyGames base exactly as one persona sees it.

Deterministic, read-only, stdlib only (Python 3.9). Run from the workspace root:

  python3 Task_Authoring/tools/persona_view.py reach <persona> [--top N] [--json]
  python3 Task_Authoring/tools/persona_view.py can-see <persona> <service> <id> [--calendar CAL] [--json]
  python3 Task_Authoring/tools/persona_view.py who-can-see <service> <id> [--calendar CAL] [--json]
  python3 Task_Authoring/tools/persona_view.py search <persona> <service> "<query>" [--limit N] [--no-hidden] [--json]
  python3 Task_Authoring/tools/persona_view.py check-sql <persona> <sql_file> [--load-bearing ids.txt] [--allow-unverified] [--json]
  python3 Task_Authoring/tools/persona_view.py personas [--json]
  python3 Task_Authoring/tools/persona_view.py --self-test

<persona> = persona_key, exact roster email, or exact roster name (case-insensitive), from
Task_Authoring/references/persona_roster_v2.json (19). The 17 entries that are also in
Evals/references/persona/roster.json are usable in tasks; `thomas` and `tim_steudler` are
supported but flagged NOT USABLE IN TASKS (not in the Evals roster).

Services: scoped = gmail, slack, gcal, gdrive, gdocs, gsheets, gslides.
          unscoped = contacts, github, trello, linear, snowflake, confluence.

VISIBILITY RULES IMPLEMENTED (authority: Evals/references/persona/acl.md)
----------------------------------------------------------------------
Verdicts are YES / NO / UNVERIFIED. Where the rules below are silent the verdict is
UNVERIFIED with a reason, never YES.

Gmail   A thread or message is visible iff its mailbox `user_email` equals the persona's
        exact roster email (each mailbox holds its own copy, with its own
        `<mailbox>/<id>` thread and message ids). A persona whose email is not a mailbox in
        gmail/users.json (28 on normal, 27 on synth-cut; only Tim Steudler is such a
        persona) sees no Gmail.
        The 6 tokenized mailboxes (EMPLOYEE_0011/0020/0032_EMAIL, SVC_0009/0019/0293_EMAIL)
        never equal a roster email, so they are NO for every persona; their owners are
        unknown (see entity.py).
Slack   A channel (public, private, IM or MPIM) is visible iff the persona's Slack user id
        (users.json, joined on exact email) is in the channel's `members`. Messages,
        thread replies and files (files.json `channel_id`) inherit the channel verdict.
        Non-member + private/IM/MPIM -> NO. Non-member + public channel -> UNVERIFIED
        (whether non-members can read public channels is not established).
GCal    Fields checked: calendars[*].{calendar_id, owner_email, shared_with_emails} and
        events[*].{event_id, calendar_id, ical_uid, attendees[*].email}. Every base
        calendar is private, calendar_id == owner_email, shared_with_emails is empty;
        event ids are globally unique; every attendee who owns a calendar holds a copy
        of the event (same ical_uid) on that calendar (0 exceptions in the base).
        Rule: an event copy is visible iff
          (a) its calendar's owner_email == persona (YES, owner), or
          (b) persona is in that calendar's shared_with_emails (YES, shared), or
          (c) persona is in that copy's attendees AND holds its own copy (same ical_uid)
              on a calendar it owns (YES, attendee; the evidence names the own copy).
        Attendee without an own copy -> UNVERIFIED (reading another calendar's copy by
        id is not established). Otherwise NO.
Drive   A Drive file/folder is visible iff owner_email == persona or persona is in
family  shared_with_emails. Otherwise visibility `domain` or `anyone` -> UNVERIFIED, else NO.
        Sharing is not inherited from folders. Files owned by `Resource: ...` with empty
        sharing and private visibility are visible to no persona. GDocs, GSheets and GSlides
        use the Drive record with the same `f_` id (verified: sharing identical for 633
        docs, 398 sheets, 164 decks). Asking GDocs/GSheets/GSlides for an id whose Drive
        mime type is not that native type -> UNVERIFIED (that service cannot open it).
Unscoped  Contacts, GitHub, Trello, Linear, Snowflake, Confluence: always YES (existence is
        not checked).

UNVERIFIED CASES (complete list)
  U1 Slack public channel, persona not a member (also its messages, replies and files).
  U2 Drive-family file with visibility domain/anyone that the persona neither owns nor is
     shared on.
  U3 GCal copy listing the persona as attendee when the persona holds no own copy.
  U4 Id not found in the base (it may be injected: use check-sql).
  U5 GDocs/GSheets/GSlides asked for a Drive id of another mime type.
  U6 check-sql rows the rules do not cover: slack_users, slack_drafts,
     slack_scheduled_messages, slack_emojis, slack_meta, gcal_acl_rules,
     gcal_calendar_list, drive_users, gmail_labels / gmail_label_user_counters without a
     user_email, and native Docs/Sheets/Slides rows with no Drive record in base or SQL.
  U7 Slack file whose message has no channel, or a message whose channel is unknown.

check-sql judges every seeded row (INSERT, and UPDATE targets) in a scoped service against
the final state after the whole SQL (members_json, shared_with_emails_json, calendar
sharing and ownership UPDATEs are applied). With --load-bearing, exit 1 if any listed row
is NO, or UNVERIFIED unless --allow-unverified. Ids in the list that match no SQL row are
judged against the base. Without --load-bearing it only reports (exit 0).

Caches: small derived indexes in Task_Authoring/support/local_search/cache/pv_*.json, rebuilt when
their source files change. The existing base_gmail_index.json is reused read-only. Nothing
under Evals/, claude/ or HarmonyGames_* is written.
Exit: 0 ok, 1 check-sql load-bearing failure / self-test failure, 2 usage error.
"""
from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import glob
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # base_check / sql_lint live beside this file
BUNDLE = HERE.parent
WS = BUNDLE.parent
from task_context import v2_export_root  # noqa: E402
OTHER = v2_export_root("Other_Services", WS) / "Services_Data"
GMAIL = v2_export_root("Gmail", WS) / "Services_Data" / "gmail"
GITHUB = v2_export_root("GitHub", WS) / "Services_Data" / "github" / "data.json"
CACHE = BUNDLE / "support" / "local_search" / "cache"
ROSTER_V1 = WS / "Evals" / "references" / "persona" / "roster.json"
ROSTER_V2 = BUNDLE / "references" / "persona_roster_v2.json"
GMAIL_INDEX = CACHE / "base_gmail_index.json"
SLACK_MSGS = OTHER / "slack" / "messages"
CLOCK = dt.datetime(2026, 2, 14, tzinfo=dt.timezone.utc)
# Data horizon (universe.clock_utc): what exists in the base data and the persona can see. Equals CLOCK on
# the normal universe, 7 h later on synth-cut. Reach/recency/activity windows read DATA_CLOCK; seeded-record
# checks stay on CLOCK. runtime_context._apply overwrites both per task.
DATA_CLOCK = CLOCK
METADATA_ONLY = "metadata only — content not served (Evals/references/persona/acl.md, 2026-10-17)"
CACHE_VERSION = 4

SCOPED = ("gmail", "slack", "gcal", "gdrive", "gdocs", "gsheets", "gslides")
UNSCOPED = ("contacts", "github", "trello", "linear", "snowflake", "confluence")
DRIVE_FAMILY = ("gdrive", "gdocs", "gsheets", "gslides")
NATIVE_MIME = {"gdocs": "application/vnd.google-apps.document",
               "gsheets": "application/vnd.google-apps.spreadsheet",
               "gslides": "application/vnd.google-apps.presentation"}
NOT_USABLE = {"thomas", "tim_steudler"}
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+|\b[A-Z]+_\d{4}_EMAIL(?:_PLUS_ALIAS_\d+)?\b|\[EMAIL_\d+\]")


# ---------------------------------------------------------------- small helpers

def _load(p: Path):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def _load_trim(p: Path, keep: set):
    """json.load that keeps only `keep` keys in every object (cuts peak memory on big exports)."""
    with open(p, encoding="utf-8") as fh:
        return json.load(fh, object_hook=lambda d: {k: v for k, v in d.items() if k in keep})


def iter_records(p: Path, fields: set, collections: set | None = None):
    """Stream (collection, record) pairs from an indent-2 pretty-printed export of the form
    {"coll": [ {...}, ... ], ...}, keeping only `fields`. Constant memory; nested list/object
    values are parsed only when their key is wanted. Falls back to json.load for other layouts."""
    with open(p, encoding="utf-8") as fh:
        head = fh.readline() + fh.readline()
    if not re.match(r'\{\n  "[^"]+": \[\n?$', head):
        d = _load_trim(p, set(fields) | set(collections or ()) | {k for k in (collections or ())})
        for coll, recs in d.items():
            if (collections is None or coll in collections) and isinstance(recs, list):
                for r in recs:
                    yield coll, r
        return
    coll, rec, key, buf, closer = None, None, None, None, None
    with open(p, encoding="utf-8") as fh:
        for line in fh:
            if key is not None:  # inside a multi-line list/object value at indent 6
                buf.append(line)
                if line.startswith(closer):
                    if key in fields:
                        rec[key] = json.loads("".join(buf).rstrip().rstrip(","))
                    key = buf = None
                continue
            if line.startswith('  "') and not line.startswith('   '):
                coll = line.strip()[1:].split('"', 1)[0]
                continue
            if line.startswith("    {") and not line.startswith("     "):
                rec = {} if (collections is None or coll in collections) else None
                continue
            if line.startswith("    }") and not line.startswith("     "):
                if rec is not None:
                    yield coll, rec
                rec = None
                continue
            if rec is None or not line.startswith('      "'):
                continue
            k, _, val = line.strip().partition('": ')
            k, val = k[1:], val.rstrip(",")
            if val in ("[", "{"):
                key, buf, closer = k, [val], "      " + ("]" if val == "[" else "}")
            elif k in fields:
                rec[k] = json.loads(val)


def ts_date(ts) -> str | None:
    try:
        return dt.datetime.fromtimestamp(float(ts), dt.timezone.utc).strftime("%Y-%m-%d")
    except (TypeError, ValueError):
        return None


def parse_dt(v) -> dt.datetime | None:
    """ISO-8601 or RFC-2822 -> aware UTC datetime."""
    if not v:
        return None
    s = str(v).strip()
    try:
        d = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
        return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)
    except ValueError:
        pass
    try:
        d = email.utils.parsedate_to_datetime(s)
        return d.astimezone(dt.timezone.utc) if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)
    except (TypeError, ValueError, IndexError):
        return None


def days_before_clock(iso: str | None) -> int | None:
    d = parse_dt(iso)
    return None if d is None else (DATA_CLOCK - d).days


def _metadata_only(v: dict) -> dict:
    """Attachment/file verdicts: ACL metadata is served, bytes are not."""
    v["reason"] = f"{v['reason']}; {METADATA_ONLY}"
    return v


def _fingerprint(paths) -> list:
    out = []
    for p in paths:
        p = Path(p)
        if p.is_dir():
            n = size = 0
            mt = 0.0
            for root, _dirs, files in os.walk(p):
                for f in files:
                    st = os.stat(os.path.join(root, f))
                    n, size, mt = n + 1, size + st.st_size, max(mt, st.st_mtime)
            out.append([str(p.relative_to(WS)), n, size, int(mt)])
        else:
            st = p.stat()
            out.append([str(p.relative_to(WS)), st.st_size, int(st.st_mtime)])
    return out


def _atomic_json(path: Path, payload) -> None:
    """Write JSON atomically: concurrent builders never see a partial cache file.

    The published inode keeps the destination's previous mode (a plain overwrite did), or 0644 for a new
    cache file; mkstemp's 0600 must not leak into a shared cache directory. Assumes the cache directory is
    written only by the invoking user's cooperating processes: the check-then-use mode read and the
    post-close chmod are not hardened against a concurrent hostile writer."""
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        mode = path.stat().st_mode & 0o777
    except FileNotFoundError:
        mode = 0o644
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w") as fh:
            json.dump(payload, fh)
        os.chmod(tmp, mode)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def cached(name: str, sources, build):
    """pv_<name>.json under the cache dir; rebuilt when a source's size/mtime changes."""
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"pv_{name}.json"
    fp = _fingerprint(sources)
    if path.exists():
        try:
            d = _load(path)
            if d.get("_meta", {}).get("sources") == fp and d["_meta"].get("version") == CACHE_VERSION:
                return d["data"]
        except (ValueError, KeyError):
            pass
    data = build()
    _atomic_json(path, {"_meta": {"version": CACHE_VERSION, "sources": fp,
                                  "built_utc": dt.datetime.now(dt.timezone.utc).isoformat()},
                        "data": data})
    return data


def V(verdict: str, reason: str, **evidence) -> dict:
    return {"verdict": verdict, "reason": reason, "evidence": evidence}


# ---------------------------------------------------------------- personas

def personas() -> list:
    v1 = _load(ROSTER_V1)
    v2 = _load(ROSTER_V2)["personas"]
    v1_by_key = {p["persona_key"]: p for p in v1}
    out = []
    for p in v2:
        d = dict(p)
        d["usable_in_tasks"] = p["persona_key"] in v1_by_key and p["persona_key"] not in NOT_USABLE
        d["roster_source"] = "Evals roster.json + roster_v2" if p["persona_key"] in v1_by_key else "persona_roster_v2.json only"
        out.append(d)
    for k, p in v1_by_key.items():  # never drop an Evals persona
        if k not in {x["persona_key"] for x in v2}:
            d = dict(p, usable_in_tasks=True, roster_source="Evals roster.json only")
            out.append(d)
    return out


def resolve_persona(q: str) -> dict:
    qq = q.strip().casefold()
    for p in personas():
        if qq in (p["persona_key"].casefold(), p["email"].casefold(), p["name"].casefold()):
            return p
    raise SystemExit(f"error: unknown persona {q!r}. Use a persona_key, exact roster email or exact name:\n  "
                     + "\n  ".join(f"{p['persona_key']:16} {p['email']:34} {p['name']}" for p in personas()))


# ---------------------------------------------------------------- base indexes

class Universe:
    """Lazy, read-only indexes over the base exports (one large export in memory at a time)."""

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

    def drop(self, *keys):
        for k in keys:
            self._c.pop(k, None)

    # ---- slack
    def slack(self) -> dict:
        def build():
            users = _load(OTHER / "slack" / "users.json")
            chans = _load(OTHER / "slack" / "channels.json")
            ch = {}
            for c in chans:
                kind = "im" if c.get("is_im") else "mpim" if c.get("is_mpim") else "private" if c.get("is_private") else "public"
                ch[c["id"]] = {"name": c.get("name"), "kind": kind, "archived": bool(c.get("is_archived")),
                               "members": c.get("members") or [], "n": 0, "replies": 0, "first": None, "last": None}
            ust = {}
            orphan_dirs = []
            for d in sorted(os.listdir(SLACK_MSGS)):
                if not (SLACK_MSGS / d).is_dir():
                    continue
                if d not in ch:
                    orphan_dirs.append(d)
                    ch[d] = {"name": None, "kind": "unknown", "archived": False, "members": [], "n": 0,
                             "replies": 0, "first": None, "last": None}
                c = ch[d]
                for f in sorted(os.listdir(SLACK_MSGS / d)):
                    for m in _load(SLACK_MSGS / d / f):
                        try:
                            ts = float(m.get("ts"))
                        except (TypeError, ValueError):
                            continue
                        c["n"] += 1
                        tt = m.get("thread_ts")
                        if tt and tt != m.get("ts"):
                            c["replies"] += 1
                        c["first"] = ts if c["first"] is None else min(c["first"], ts)
                        c["last"] = ts if c["last"] is None else max(c["last"], ts)
                        u = m.get("user")
                        if u:
                            s = ust.setdefault(u, [0, ts, ts])
                            s[0] += 1
                            s[1], s[2] = min(s[1], ts), max(s[2], ts)
            return {"users": {u["id"]: {k: u.get(k) for k in ("name", "real_name", "email", "is_bot", "deleted")}
                              for u in users},
                    "channels": ch, "user_stats": ust, "orphan_dirs": orphan_dirs}
        return self._get("slack", lambda: cached("slack", [OTHER / "slack" / "users.json",
                                                           OTHER / "slack" / "channels.json", SLACK_MSGS], build))

    def slack_uid(self, email: str) -> str | None:
        e = email.casefold()
        hits = [uid for uid, u in self.slack()["users"].items() if str(u.get("email") or "").casefold() == e]
        return hits[0] if len(hits) == 1 else None

    def slack_files(self) -> dict:
        def build():
            return {f["id"]: [f.get("channel_id"), f.get("message_ts"), f.get("title") or f.get("name"), f.get("user")]
                    for f in _load(OTHER / "slack" / "files.json")}
        return self._get("slack_files", lambda: cached("slack_files", [OTHER / "slack" / "files.json"], build))

    def slack_find(self, channel: str, ts: str) -> dict | None:
        d = SLACK_MSGS / channel
        if not d.is_dir():
            return None
        for f in sorted(os.listdir(d)):
            for m in _load(d / f):
                if m.get("ts") == ts:
                    return {"ts": ts, "id": m.get("id"), "user": m.get("user"), "thread_ts": m.get("thread_ts"),
                            "is_reply": bool(m.get("thread_ts") and m.get("thread_ts") != ts),
                            "date": ts_date(ts), "shard": f"messages/{channel}/{f}"}
        return None

    def slack_find_ids(self, ids) -> dict:
        """message id (sha256[:32]) -> (channel, ts); one streaming pass over all shards."""
        want, out = set(ids), {}
        if not want:
            return out
        for d in sorted(os.listdir(SLACK_MSGS)):
            if not (SLACK_MSGS / d).is_dir():
                continue
            for f in sorted(os.listdir(SLACK_MSGS / d)):
                raw = (SLACK_MSGS / d / f).read_text(encoding="utf-8")
                if not any(i in raw for i in want):
                    continue
                for m in json.loads(raw):
                    if m.get("id") in want:
                        out[m["id"]] = (d, m.get("ts"))
            if len(out) == len(want):
                break
        return out

    # ---- gmail
    def gmail_mailboxes(self) -> list:
        return [u["emailAddress"] for u in _load(GMAIL / "users.json")]

    def gmail(self) -> dict:
        """Compact per-thread index derived from base_gmail_index.json (reused, never written)."""
        def build():
            if not GMAIL_INDEX.is_file():
                from base_check import Base
                Base().gmail()
            idx = _load(GMAIL_INDEX)
            threads, boxes = {}, {}
            for tid, (mb, mids, dates, f) in idx.items():
                ds = sorted(x for x in (parse_dt(d) for d in dates) if x)
                first = ds[0].isoformat()[:19] + "Z" if ds else None
                last = ds[-1].isoformat()[:19] + "Z" if ds else None
                threads[tid] = [mb, len(mids), first, last, f]
                b = boxes.setdefault(mb, {"threads": 0, "messages": 0, "first": None, "last": None, "months": {}})
                b["threads"] += 1
                b["messages"] += len(mids)
                if first:
                    b["first"] = min(b["first"] or first, first)
                    b["last"] = max(b["last"] or last, last)
                    b["months"][last[:7]] = b["months"].get(last[:7], 0) + 1
            return {"threads": threads, "mailboxes": boxes}

        def load():
            # The base index is a fingerprinted source of this cache, so it must exist before cached()
            # stats it (a fresh per-universe context starts with an empty cache folder).
            if not GMAIL_INDEX.is_file():
                from base_check import Base
                Base().gmail()
            return cached("gmail", [GMAIL_INDEX, GMAIL / "users.json"], build)
        return self._get("gmail", load)

    def gmail_message_thread(self, mid: str) -> str | None:
        """Message id -> thread id via the full base index (loaded transiently)."""
        idx = _load(GMAIL_INDEX)
        try:
            for tid, entry in idx.items():
                if mid in entry[1]:
                    return tid
            return None
        finally:
            del idx

    def gmail_stats(self, mailbox: str) -> dict:
        """Top correspondents per mailbox (reads that mailbox's thread files once, cached)."""
        path = CACHE / "pv_gmail_correspondents.json"
        store = _load(path) if path.exists() else {}
        if store.get("_version") == CACHE_VERSION and mailbox in store:
            return store[mailbox]
        cnt, n_files = Counter(), 0
        for tid, (mb, _n, _f, _l, f) in self.gmail()["threads"].items():
            if mb != mailbox:
                continue
            n_files += 1
            try:
                d = _load(GMAIL / "threads" / f)
            except (OSError, ValueError):
                continue
            for m in d.get("messages", []):
                seen = set()
                for fld in ("from", "to", "cc"):
                    for a in EMAIL_RE.findall(str(m.get(fld) or "")):
                        a = a.lower() if "@" in a else a
                        if a != mailbox.lower() and a not in seen:
                            seen.add(a)
                            cnt[a] += 1
        res = {"files_read": n_files, "top": cnt.most_common(15)}
        if store.get("_version") != CACHE_VERSION:
            store = {"_version": CACHE_VERSION}
        store[mailbox] = res
        _atomic_json(path, store)
        return res

    # ---- gcal
    def gcal(self) -> dict:
        def build():
            keep = {"calendar_id", "owner_email", "shared_with_emails", "summary", "visibility", "event_id",
                    "ical_uid", "start", "status", "attendees", "organizer_email"}
            cals, ev = {}, {}
            for coll, e in iter_records(OTHER / "gcal" / "data.json", keep):
                if coll == "calendars":
                    cals[e["calendar_id"]] = {"owner": e.get("owner_email"), "shared": e.get("shared_with_emails") or [],
                                              "summary": e.get("summary"), "visibility": e.get("visibility")}
                elif coll == "events":
                    ev[e["event_id"]] = [e["calendar_id"], e.get("ical_uid"), e.get("summary"),
                                         (e.get("start") or {}).get("dateTime") or (e.get("start") or {}).get("date"),
                                         e.get("status"), [a.get("email") for a in e.get("attendees") or []],
                                         e.get("organizer_email")]
            return {"calendars": cals, "events": ev}
        g = self._get("gcal", lambda: cached("gcal", [OTHER / "gcal" / "data.json"], build))
        if "by_uid" not in g:
            by = defaultdict(list)
            for eid, e in g["events"].items():
                by[e[1]].append(eid)
            g["by_uid"] = dict(by)
        return g

    # ---- drive family
    def drive(self) -> dict:
        def build():
            keep = {"id", "name", "mime_type", "owner_email", "shared_with_emails", "visibility", "modified_time"}
            return {f["id"]: [f.get("name"), f.get("mime_type"), f.get("owner_email"), f.get("shared_with_emails") or [],
                              f.get("visibility"), f.get("modified_time")]
                    for _c, f in iter_records(OTHER / "gdrive" / "data.json", keep, {"drive_files"})}
        return self._get("drive", lambda: cached("drive", [OTHER / "gdrive" / "data.json"], build))


# ---------------------------------------------------------------- visibility core

def _persona_mailbox(u: Universe, p: dict) -> str | None:
    e = p["email"]
    return e if e in u.gmail_mailboxes() else None


def can_see(u: Universe, p: dict, service: str, oid: str, calendar: str | None = None) -> dict:
    service = service.lower()
    if service in UNSCOPED:
        return V("YES", f"{service} is unscoped: every persona reads it (acl.md access matrix); existence not checked",
                 rule="unscoped")
    if service == "slack":
        return _see_slack(u, p, oid)
    if service == "gmail":
        return _see_gmail(u, p, oid)
    if service == "gcal":
        return _see_gcal(u, p, oid, calendar)
    if service in DRIVE_FAMILY:
        return _see_drive(u, p, service, oid)
    raise SystemExit(f"error: unknown service {service!r}; scoped: {', '.join(SCOPED)}; unscoped: {', '.join(UNSCOPED)}")


def _channel_verdict(u: Universe, p: dict, cid: str, extra_members=None) -> dict:
    s = u.slack()
    uid = u.slack_uid(p["email"])
    c = s["channels"].get(cid)
    if c is None and extra_members is None:
        return V("UNVERIFIED", f"channel {cid} not in base (U4; if injected, use check-sql)", channel=cid)
    members = extra_members if extra_members is not None else c["members"]
    kind = c["kind"] if c else "unknown"
    name = (c or {}).get("name")
    ev = {"channel": cid, "name": name, "kind": kind, "members": len(members), "persona_slack_id": uid}
    if uid is None:
        return V("NO", "persona has no Slack user (no exact-email match in slack/users.json)", **ev)
    if uid in members:
        return V("YES", f"persona {uid} is in members of {kind} {name or cid}", **ev)
    if kind == "public":
        return V("UNVERIFIED", f"public channel #{name}: persona {uid} is not a member; non-member reads not established (U1)", **ev)
    return V("NO", f"{kind} conversation {name or cid}: persona {uid} is not a member", **ev)


def _see_slack(u: Universe, p: dict, oid: str) -> dict:
    oid = oid.strip()
    if re.fullmatch(r"F[A-Z0-9]+", oid):
        f = u.slack_files().get(oid)
        if f is None:
            return _metadata_only(V("UNVERIFIED", f"file {oid} not in slack/files.json (U4)", file=oid))
        if not f[0]:
            return _metadata_only(V("UNVERIFIED", f"file {oid} has no channel_id (U7)", file=oid))
        r = _channel_verdict(u, p, f[0])
        r["reason"] = f"file inherits channel: {r['reason']}"
        r["evidence"].update(file=oid, message_ts=f[1])
        return _metadata_only(r)
    if re.fullmatch(r"[0-9a-f]{32}", oid):
        hit = u.slack_find_ids([oid]).get(oid)
        if not hit:
            return V("UNVERIFIED", f"message id {oid} not in base (U4)", message_id=oid)
        oid = f"{hit[0]}/{hit[1]}"
    cid, _, ts = oid.partition("/")
    r = _channel_verdict(u, p, cid)
    if ts:
        m = u.slack_find(cid, ts)
        if m is None:
            if r["verdict"] == "YES" or cid in u.slack()["channels"]:
                return V("UNVERIFIED", f"ts {ts} not found in channel {cid} shards (U4); channel verdict {r['verdict']}",
                         **r["evidence"])
            return r
        r["reason"] = ("thread reply inherits channel: " if m["is_reply"] else "message inherits channel: ") + r["reason"]
        r["evidence"].update(message=m)
    return r


def _see_gmail(u: Universe, p: dict, oid: str) -> dict:
    g = u.gmail()
    mine = _persona_mailbox(u, p)
    tid = oid if oid in g["threads"] else None
    msg_id = None
    if tid is None and "/" in oid:
        tid = u.gmail_message_thread(oid)
        msg_id = oid if tid else None
    if tid is None and "/" not in oid:  # bare thread number: list every mailbox copy
        copies = [t for t in g["threads"] if t.endswith("/" + oid)]
        if copies:
            own = [t for t in copies if g["threads"][t][0] == mine]
            if own:
                return V("YES", f"a copy of thread {oid} is in the persona's mailbox", thread=own[0], copies=copies)
            return V("NO", f"thread {oid} exists only in other mailboxes" + ("" if mine else "; persona has no Gmail mailbox"),
                     copies=copies, persona_mailbox=mine)
    if tid is None:
        return V("UNVERIFIED", f"{oid} is neither a base thread id nor a base message id (U4)", id=oid)
    mb, nmsg, first, last, f = g["threads"][tid]
    ev = {"thread": tid, "message": msg_id, "mailbox": mb, "messages_in_thread": nmsg, "last": last,
          "file": f"threads/{f}", "persona_mailbox": mine}
    if mine is None:
        return V("NO", f"persona {p['email']} has no Gmail mailbox (not in gmail/users.json); thread is in {mb}", **ev)
    if mb == mine:
        return V("YES", f"thread is in the persona's own mailbox {mb}", **ev)
    note = " (tokenized mailbox, owner unknown)" if "@" not in mb else ""
    return V("NO", f"thread is in mailbox {mb}{note}, not the persona's mailbox {mine}", **ev)


def _see_gcal(u: Universe, p: dict, oid: str, calendar: str | None) -> dict:
    g = u.gcal()
    e = g["events"].get(oid)
    if e is None:
        return V("UNVERIFIED", f"event {oid} not in gcal/data.json (U4)", event=oid)
    cal, uid, summary, start, status, attendees, organizer = e
    if calendar and calendar != cal:
        return V("UNVERIFIED", f"event {oid} is on calendar {cal}, not {calendar} (U4)", event=oid, calendar=cal)
    return _event_verdict(p["email"], oid, cal, uid, attendees, g["calendars"], g["by_uid"], g["events"],
                          start=start, summary=summary, status=status)


def _event_verdict(pe: str, eid, cal, uid, attendees, calendars, by_uid, events, extra_copies=(), start=None, **ev) -> dict:
    """extra_copies: (event_id, calendar_id, start) of SQL-inserted copies."""
    c = calendars.get(cal) or {}
    ev.update(event=eid, calendar=cal, ical_uid=uid, calendar_owner=c.get("owner"), start=start)
    if c.get("owner") == pe or (not c and cal == pe):
        return V("YES", f"event is on the persona's own calendar {cal}", **ev)
    if pe in (c.get("shared") or []):
        return V("YES", f"calendar {cal} is shared with the persona", **ev)
    if pe in (attendees or []):
        own = [(x, events[x][3]) for x in by_uid.get(uid, []) if (calendars.get(events[x][0]) or {}).get("owner") == pe]
        own += [(x, xs) for x, xcal, xs in extra_copies if xcal == pe]
        same = [x for x, xs in own if not start or not xs or parse_dt(xs) == parse_dt(start)]
        if same:
            return V("YES", f"persona is an attendee and holds its own copy {same[0]} (same ical_uid and start) on {pe}",
                     own_copy=same[0], **ev)
        if own:
            return V("YES", f"persona is an attendee and holds a copy of the same series {own[0][0]} (same ical_uid, "
                     "different start) on its calendar", own_copy=own[0][0], **ev)
        return V("UNVERIFIED", "persona is listed as attendee but holds no own copy of this event (U3)", **ev)
    if not c:
        return V("UNVERIFIED", f"calendar {cal} not in base (U4)", **ev)
    return V("NO", f"calendar {cal} is owned by {c.get('owner')}, not shared with the persona, persona not an attendee", **ev)


def drive_verdict(pe: str, fid: str, rec: list | None, service: str = "gdrive") -> dict:
    if rec is None:
        return V("UNVERIFIED", f"{fid} not in gdrive/data.json (U4; if injected, use check-sql)", file=fid)
    name, mime, owner, shared, vis, modified = rec
    ev = {"file": fid, "name": name, "mime": mime, "owner": owner, "shared_with": len(shared or []),
          "visibility": vis, "modified": modified}
    if service in NATIVE_MIME and mime != NATIVE_MIME[service]:
        inner = drive_verdict(pe, fid, rec)
        return V("UNVERIFIED", f"{fid} is {mime}, not a {service} file; {service} cannot open it (U5). Drive verdict: "
                 f"{inner['verdict']} ({inner['reason']})", **ev)
    if owner == pe:
        return V("YES", "persona owns the file", **ev)
    if pe in (shared or []):
        return V("YES", "file is shared with the persona (shared_with_emails)", **ev)
    if vis in ("domain", "anyone"):
        return V("UNVERIFIED", f"visibility={vis}; persona is neither owner nor shared; whether {vis} grants access is "
                 "not established (U2)", **ev)
    if str(owner).startswith("Resource:") and not shared:
        return V("NO", f"owned by '{owner}' with empty sharing and {vis} visibility: visible to no persona", **ev)
    return V("NO", f"owned by {owner}; persona not in shared_with_emails ({len(shared or [])} entries); visibility={vis}", **ev)


def _see_drive(u: Universe, p: dict, service: str, oid: str) -> dict:
    return drive_verdict(p["email"], oid, u.drive().get(oid), service)


def who_can_see(u: Universe, service: str, oid: str, calendar: str | None = None) -> dict:
    out = {"service": service, "id": oid, "YES": [], "NO": [], "UNVERIFIED": [], "detail": {}}
    for p in personas():
        r = can_see(u, p, service, oid, calendar)
        tag = p["persona_key"] + ("" if p["usable_in_tasks"] else " (not usable in tasks)")
        out[r["verdict"]].append(tag)
        out["detail"][p["persona_key"]] = {"verdict": r["verdict"], "reason": r["reason"]}
    return out


# ---------------------------------------------------------------- reach

def reach(u: Universe, p: dict, top: int = 10, correspondents: bool = True) -> dict:
    pe = p["email"]
    res = {"persona": {k: p[k] for k in ("persona_key", "name", "email", "role", "department", "usable_in_tasks")},
           "clock": DATA_CLOCK.isoformat(), "services": {}}

    # slack
    s = u.slack()
    uid = u.slack_uid(pe)
    mine = [(cid, c) for cid, c in s["channels"].items() if uid and uid in c["members"]]
    pub_not_member = [cid for cid, c in s["channels"].items() if c["kind"] == "public" and not (uid and uid in c["members"])]
    by_kind = Counter(c["kind"] for _, c in mine)
    mine.sort(key=lambda x: (-x[1]["n"], x[0]))
    last_in = max((c["last"] for _, c in mine if c["last"]), default=None)
    ust = s["user_stats"].get(uid) if uid else None
    res["services"]["slack"] = {
        "slack_user_id": uid, "channels_visible": len(mine), "by_kind": dict(by_kind),
        "messages_visible": sum(c["n"] for _, c in mine),
        "public_channels_not_member_UNVERIFIED": len(pub_not_member),
        "persona_messages_posted": ust[0] if ust else 0,
        "persona_last_post": ts_date(ust[2]) if ust else None,
        "last_activity_in_visible_channels": ts_date(last_in),
        "top_channels": [{"id": cid, "name": c["name"], "kind": c["kind"], "archived": c["archived"],
                          "members": len(c["members"]), "messages": c["n"], "replies": c["replies"],
                          "first": ts_date(c["first"]), "last": ts_date(c["last"])} for cid, c in mine[:top]]}

    # gmail
    mb = _persona_mailbox(u, p)
    if mb:
        b = u.gmail()["mailboxes"].get(mb, {})
        gm = {"mailbox": mb, "threads": b.get("threads", 0), "messages": b.get("messages", 0),
              "first": b.get("first"), "last": b.get("last"),
              "threads_by_last_month_recent": dict(sorted(b.get("months", {}).items())[-6:])}
        if correspondents:
            st = u.gmail_stats(mb)
            gm["top_correspondents"] = st["top"][:top]
        res["services"]["gmail"] = gm
    else:
        res["services"]["gmail"] = {"mailbox": None, "note": f"{pe} is not one of the {len(u.gmail_mailboxes())} mailboxes "
                                    "in gmail/users.json: the persona sees no Gmail"}

    # gcal
    g = u.gcal()
    own = [c for c, x in g["calendars"].items() if x["owner"] == pe]
    shared = [c for c, x in g["calendars"].items() if pe in (x["shared"] or []) and x["owner"] != pe]
    evs = [(eid, e) for eid, e in g["events"].items() if e[0] in own or e[0] in shared]
    months = Counter((e[3] or "")[:7] for _, e in evs)
    past = [e[3] for _, e in evs if e[3] and parse_dt(e[3]) and parse_dt(e[3]) <= DATA_CLOCK]
    fut = [e[3] for _, e in evs if e[3] and parse_dt(e[3]) and parse_dt(e[3]) > DATA_CLOCK]
    res["services"]["gcal"] = {"calendars_owned": own, "calendars_shared_with": shared, "events_visible": len(evs),
                               "distinct_ical_uids": len({e[1] for _, e in evs}),
                               "cancelled": sum(1 for _, e in evs if e[4] == "cancelled"),
                               "events_by_month": dict(sorted(months.items())),
                               "last_event_start_before_clock": max(past, default=None),
                               "next_event_after_clock": min(fut, default=None)}

    # drive family
    d = u.drive()
    owned, sharedw, unver = Counter(), Counter(), Counter()
    sharers, last_mod = Counter(), None
    native = Counter()
    for fid, (name, mime, owner, sh, vis, mod) in d.items():
        short = "folder" if mime == "application/vnd.google-apps.folder" else mime
        if owner == pe:
            owned[short] += 1
        elif pe in sh:
            sharedw[short] += 1
            sharers[owner] += 1
        elif vis in ("domain", "anyone"):
            unver[short] += 1
            continue
        else:
            continue
        if mime in NATIVE_MIME.values():
            native[mime.rsplit(".", 1)[-1]] += 1
        if mod and (last_mod is None or mod > last_mod):
            last_mod = mod
    res["services"]["drive"] = {"owned_total": sum(owned.values()), "owned_by_mime": dict(owned.most_common()),
                                "shared_with_total": sum(sharedw.values()), "shared_by_mime": dict(sharedw.most_common()),
                                "shared_by_owner": dict(sharers.most_common(top)),
                                "UNVERIFIED_domain_or_anyone_total": sum(unver.values()),
                                "UNVERIFIED_by_mime": dict(unver.most_common()),
                                "native_visible": {"gdocs": native["document"], "gsheets": native["spreadsheet"],
                                                   "gslides": native["presentation"]},
                                "last_modified_visible": last_mod}
    res["services"]["unscoped"] = {"services": list(UNSCOPED), "note": "always visible to every persona"}
    res["last_activity"] = {
        "slack_persona_post": res["services"]["slack"]["persona_last_post"],
        "slack_visible_channels": res["services"]["slack"]["last_activity_in_visible_channels"],
        "gmail": (res["services"]["gmail"].get("last") or "")[:10] or None,
        "gcal_last_event_before_clock": (res["services"]["gcal"]["last_event_start_before_clock"] or "")[:10] or None,
        "drive_last_modified_visible": (last_mod or "")[:10] or None}
    res["last_activity_days_before_clock"] = {k: days_before_clock(v) for k, v in res["last_activity"].items()}
    return res


# ---------------------------------------------------------------- search

def _ascii_safe(q: str) -> bool:
    return q.isascii() and '"' not in q and "\\" not in q


def _match_slack(m: dict, q: str) -> str | None:
    texts = [m.get("text") or ""]
    for a in m.get("attachments") or []:
        texts += [str(a.get(k) or "") for k in ("pretext", "title", "text", "fallback")]
    for f in m.get("files") or []:
        if isinstance(f, dict):
            texts += [str(f.get("title") or ""), str(f.get("name") or "")]
    for t in texts:
        i = t.casefold().find(q)
        if i >= 0:
            return t[max(0, i - 60): i + len(q) + 80].replace("\n", " ")
    return None


def search(u: Universe, p: dict, service: str, query: str, limit: int = 20, hidden: bool = True) -> dict:
    q = query.casefold()
    out = {"persona": p["persona_key"], "service": service, "query": query, "visible": [], "visible_total": 0,
           "hidden_by_acl": 0, "hidden_containers": 0, "unverified": 0, "unverified_containers": 0, "scope": ""}
    if service in UNSCOPED:
        cmd = [sys.executable, str(HERE / "hg.py"), "search", "search", service, query, "--limit", str(limit)]
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(WS))
        try:
            data = json.loads(r.stdout)
        except ValueError:
            data = {"raw": r.stdout[-2000:], "stderr": r.stderr[-2000:]}
        out.update(scope="hg.py search (unscoped: no ACL filter)", visible=data.get("matches", data),
                   visible_total=len(data.get("matches", [])), scan_complete=data.get("scan_complete"))
        return out
    hid_c, unv_c = set(), set()

    if service == "slack":
        s = u.slack()
        uid = u.slack_uid(p["email"])
        prefilter = _ascii_safe(q)
        out["scope"] = "Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)"
        for d in sorted(os.listdir(SLACK_MSGS)):
            if not (SLACK_MSGS / d).is_dir():
                continue
            c = s["channels"].get(d, {"members": [], "kind": "unknown", "name": None})
            vis = "YES" if uid and uid in c["members"] else ("UNVERIFIED" if c["kind"] == "public" else "NO")
            if vis == "NO" and not hidden:
                continue
            for f in sorted(os.listdir(SLACK_MSGS / d)):
                raw = (SLACK_MSGS / d / f).read_text(encoding="utf-8")
                if prefilter and q not in raw.casefold():
                    continue
                for m in json.loads(raw):
                    snip = _match_slack(m, q)
                    if snip is None:
                        continue
                    if vis == "YES":
                        out["visible_total"] += 1
                        if len(out["visible"]) < limit:
                            out["visible"].append({"id": f"{d}/{m.get('ts')}", "channel": c.get("name"),
                                                   "kind": c["kind"], "date": ts_date(m.get("ts")), "user": m.get("user"),
                                                   "reply": bool(m.get("thread_ts") and m.get("thread_ts") != m.get("ts")),
                                                   "snippet": snip})
                    elif vis == "UNVERIFIED":
                        out["unverified"] += 1
                        unv_c.add(d)
                    else:
                        out["hidden_by_acl"] += 1
                        hid_c.add(d)

    elif service == "gmail":
        mine = _persona_mailbox(u, p)
        prefilter = _ascii_safe(q)
        out["scope"] = "Gmail subject, body, from, to, cc, attachment filenames (thread files)"
        threads = u.gmail()["threads"]
        order = sorted(threads.items(), key=lambda kv: (kv[1][0] != mine, kv[0]))
        for tid, (mb, _n, _f, last, f) in order:
            if mb != mine and not hidden:
                break
            try:
                raw = (GMAIL / "threads" / f).read_text(encoding="utf-8")
            except OSError:
                continue
            if prefilter and q not in raw.casefold():
                continue
            d = json.loads(raw)
            snip = None
            for m in d.get("messages", []):
                fields = [m.get("subject"), m.get("body"), m.get("from"), m.get("to"), m.get("cc")]
                fields += [a.get("filename") for a in m.get("attachments") or [] if isinstance(a, dict)]
                for t in fields:
                    t = str(t or "")
                    i = t.casefold().find(q)
                    if i >= 0:
                        snip = (m.get("subject"), t[max(0, i - 60): i + len(q) + 80].replace("\r", " ").replace("\n", " "))
                        break
                if snip:
                    break
            if not snip:
                continue
            if mb == mine:
                out["visible_total"] += 1
                if len(out["visible"]) < limit:
                    out["visible"].append({"id": tid, "last": last, "subject": snip[0], "snippet": snip[1]})
            else:
                out["hidden_by_acl"] += 1
                hid_c.add(mb)

    elif service == "gcal":
        g = u.gcal()
        out["scope"] = "GCal event summary (base events carry no description/location)"
        seen = {}
        for eid, e in sorted(g["events"].items()):
            if q not in str(e[2] or "").casefold():
                continue
            r = _event_verdict(p["email"], eid, e[0], e[1], e[5], g["calendars"], g["by_uid"], g["events"], start=e[3])
            key = (e[1], e[3])
            prev = seen.get(key)
            if r["verdict"] == "YES" and r["evidence"].get("own_copy"):  # show the persona's own copy
                eid = r["evidence"]["own_copy"]
                e = g["events"][eid]
            if prev is None or (prev[0] != "YES" and r["verdict"] == "YES"):
                seen[key] = (r["verdict"], eid, e)
        for key, (verdict, eid, e) in sorted(seen.items(), key=lambda kv: str(kv[1][2][3])):
            if verdict == "YES":
                out["visible_total"] += 1
                if len(out["visible"]) < limit:
                    out["visible"].append({"id": eid, "calendar": e[0], "start": e[3], "summary": e[2], "status": e[4]})
            elif verdict == "UNVERIFIED":
                out["unverified"] += 1
                unv_c.add(e[0])
            else:
                out["hidden_by_acl"] += 1
                hid_c.add(e[0])
        out["note"] = "counted per meeting instance (ical_uid + start), visible if any copy is visible"

    elif service in DRIVE_FAMILY:
        d = u.drive()
        hits = {}  # fid -> snippet
        if service == "gdrive":
            out["scope"] = "Drive file/folder names (on-disk file content is not searched)"
            for fid, rec in d.items():
                if q in str(rec[0] or "").casefold():
                    hits[fid] = rec[0]
        elif service == "gdocs":
            out["scope"] = "GDocs title + body_text"
            for x in _load(OTHER / "gdocs" / "data.json")["docs_documents"]:
                for t in (x.get("title"), x.get("body_text")):
                    t = str(t or "")
                    i = t.casefold().find(q)
                    if i >= 0:
                        hits[x["document_id"]] = t[max(0, i - 60): i + len(q) + 80].replace("\n", " ")
                        break
        elif service == "gslides":
            out["scope"] = "GSlides title + page element text"
            for x in _load(OTHER / "gslides" / "data.json")["slides_presentations"]:
                texts = [x.get("title")] + [el.get("text") for pg in x.get("pages") or [] for el in pg.get("elements") or []]
                for t in texts:
                    t = str(t or "")
                    i = t.casefold().find(q)
                    if i >= 0:
                        hits[x["presentation_id"]] = t[max(0, i - 60): i + len(q) + 80].replace("\n", " ")
                        break
        else:  # gsheets: stream the 397 MB export line by line
            out["scope"] = "GSheets spreadsheet title, tab titles, cell strings (streamed)"
            cur = None
            with open(OTHER / "gsheets" / "data.json", encoding="utf-8") as fh:
                for line in fh:
                    if line.startswith('      "drive_file_id": '):
                        cur = json.loads(line.split(":", 1)[1].strip().rstrip(","))
                        continue
                    if cur is None or cur in hits or q not in line.casefold():
                        continue
                    val = line.strip().rstrip(",")
                    if val.startswith('"title": ') or val.startswith('"spreadsheet_id"'):
                        val = val.split(":", 1)[1].strip()
                    try:
                        t = json.loads(val)
                    except ValueError:
                        continue
                    if isinstance(t, str) and q in t.casefold():
                        i = t.casefold().find(q)
                        hits[cur] = t[max(0, i - 60): i + len(q) + 80].replace("\n", " ")
        for fid in sorted(hits):
            r = drive_verdict(p["email"], fid, d.get(fid), service if service != "gdrive" else "gdrive")
            if r["verdict"] == "YES":
                out["visible_total"] += 1
                if len(out["visible"]) < limit:
                    rec = d.get(fid) or [None] * 6
                    out["visible"].append({"id": fid, "name": rec[0], "mime": rec[1], "why": r["reason"],
                                           "snippet": hits[fid]})
            elif r["verdict"] == "UNVERIFIED":
                out["unverified"] += 1
                unv_c.add(fid)
            else:
                out["hidden_by_acl"] += 1
                hid_c.add(fid)
    else:
        raise SystemExit(f"error: unknown service {service!r}")
    out["hidden_containers"], out["unverified_containers"] = len(hid_c), len(unv_c)
    if not hidden and service in ("slack", "gmail"):
        out["hidden_by_acl"] = None
        out["note"] = "--no-hidden: containers outside the persona's view were not scanned"
    return out


# ---------------------------------------------------------------- check-sql

def _jl(v) -> list:
    try:
        x = json.loads(v) if isinstance(v, str) else v
        return [str(i) for i in x] if isinstance(x, list) else []
    except ValueError:
        return []


def _ev_start(r: dict):
    if r.get("start_ts"):
        return r["start_ts"]
    try:
        j = json.loads(r.get("start_json") or "{}")
        return j.get("dateTime") or j.get("date")
    except (ValueError, AttributeError):
        return None


def check_sql(u: Universe, p: dict, sql: str, load_bearing: set | None = None, allow_unverified: bool = False) -> dict:
    from base_check import parse_sql  # reuse the shared SQL grammar (sql_lint underneath)
    pe = p["email"]
    stmts = parse_sql(sql)
    lb = set(load_bearing or ())

    # ---- final SQL-side state for containers
    chan = {}          # channel id -> members (INSERT then UPDATEs)
    chan_kind = {}
    drive = {}         # file id -> [name, mime, owner, shared, vis, modified] (overlay on base)
    cals = {}          # calendar id -> {"owner", "shared"}
    sql_events = []    # (event_id, calendar_id, ical_uid)
    gm_threads, gm_msgs = {}, {}
    slack_ids = {}     # slack message id -> (channel, ts) for SQL-inserted messages
    native_rows = defaultdict(dict)  # file id -> {table: (owner, shared, vis)}
    base_drive = u.drive()

    def drive_rec(fid):
        if fid not in drive:
            b = base_drive.get(fid)
            drive[fid] = list(b) if b else None
        return drive[fid]

    for s in stmts:
        t, op = s["table"], s["op"]
        if op == "insert":
            r = s["row"]
            if t == "slack.slack_channels":
                chan[r.get("id")] = _jl(r.get("members_json"))
                kind = ("im" if str(r.get("is_im")).lower() == "true" else "mpim" if str(r.get("is_mpim")).lower() == "true"
                        else "private" if str(r.get("is_private")).lower() == "true" else "public")
                chan_kind[r.get("id")] = (kind, r.get("name"))
            elif t == "slack.slack_messages":
                slack_ids[r.get("id")] = (r.get("channel_id"), r.get("ts"))
            elif t == "gdrive.drive_files":
                drive[r.get("id")] = [r.get("name"), r.get("mime_type"), r.get("owner_email"),
                                      _jl(r.get("shared_with_emails_json")), r.get("visibility"), r.get("modified_time")]
            elif t == "gcal.gcal_calendars":
                cals[r.get("calendar_id")] = {"owner": r.get("owner_email"), "shared": _jl(r.get("shared_with_emails_json")),
                                              "summary": r.get("summary")}
            elif t == "gcal.gcal_events":
                sql_events.append((r.get("event_id"), r.get("calendar_id"), r.get("ical_uid"), _ev_start(r)))
            elif t == "gmail.gmail_threads":
                gm_threads[r.get("id")] = r.get("user_email")
            elif t == "gmail.gmail_messages":
                gm_msgs[r.get("id")] = r.get("user_email")
            if t in ("gdocs.docs_documents", "gsheets.sheets_spreadsheets", "gslides.slides_presentations"):
                fid = r.get("document_id") or r.get("spreadsheet_id") or r.get("presentation_id")
                native_rows[fid][t] = (r.get("owner_email"), sorted(_jl(r.get("shared_with_emails_json"))), r.get("visibility"))
        elif op == "update":
            w, st = s["where"], s["set"]
            if t == "slack.slack_channels" and "members_json" in st and w.get("id"):
                chan[w["id"]] = _jl(st["members_json"])
            elif t == "gdrive.drive_files" and w.get("id"):
                rec = drive_rec(w["id"])
                if rec is not None:
                    if "owner_email" in st:
                        rec[2] = st["owner_email"]
                    if "shared_with_emails_json" in st:
                        rec[3] = _jl(st["shared_with_emails_json"])
                    if "visibility" in st:
                        rec[4] = st["visibility"]
            elif t == "gcal.gcal_calendars" and w.get("calendar_id"):
                base_c = u.gcal()["calendars"].get(w["calendar_id"], {})
                c = cals.setdefault(w["calendar_id"], {"owner": base_c.get("owner"), "shared": list(base_c.get("shared") or [])})
                if "owner_email" in st:
                    c["owner"] = st["owner_email"]
                if "shared_with_emails_json" in st:
                    c["shared"] = _jl(st["shared_with_emails_json"])

    g = u.gcal()
    all_cals = dict(g["calendars"])
    all_cals.update(cals)
    uid_copies = defaultdict(list)
    for eid, cal, uid, st in sql_events:
        uid_copies[uid].append((eid, cal, st))

    # slack UPDATE targets by message id that are not inserted by the SQL: one shard pass
    need = [s["where"].get("id") for s in stmts if s["op"] == "update" and s["table"] == "slack.slack_messages"
            and s["where"].get("id") and s["where"]["id"] not in slack_ids]
    found = u.slack_find_ids([x for x in need if x])

    def chan_v(cid):
        if cid in chan:
            r = _channel_verdict(u, p, cid, extra_members=chan[cid])
            if cid not in u.slack()["channels"] and cid in chan_kind:
                kind, name = chan_kind[cid]
                r["evidence"].update(kind=kind, name=name)
                if r["verdict"] == "NO" and kind == "public":
                    r = V("UNVERIFIED", f"SQL-created public channel {name}: persona not a member (U1)", **r["evidence"])
            r["evidence"]["members_from_sql"] = True
            return r
        return _channel_verdict(u, p, cid)

    def drive_v(fid, service="gdrive"):
        rec = drive_rec(fid)
        if rec is None:
            return V("UNVERIFIED", f"no Drive record for {fid} in base or SQL (U6)", file=fid)
        r = drive_verdict(pe, fid, rec, service)
        nat = native_rows.get(fid)
        if nat:
            for tbl, (own, sh, vis) in nat.items():
                if (own, sh, vis) != (rec[2], sorted(rec[3] or []), rec[4]):
                    r["evidence"]["native_sharing_mismatch"] = f"{tbl} owner/sharing/visibility differ from the Drive record"
        return r

    rows = []
    unscoped_rows = Counter()
    for s in stmts:
        t, op = s["table"], s["op"]
        svc = t.split(".", 1)[0]
        if svc in UNSCOPED:
            unscoped_rows[t] += 1
            continue
        if svc not in SCOPED or op == "delete":
            if op == "delete":
                rows.append({"line": s["line"], "table": t, "op": op, "keys": list(s["where"].values()),
                             "verdict": "INFO", "reason": "DELETE: not a seeded row"})
            continue
        r = s.get("row") or {}
        w = s.get("where") or {}
        keys, v = [], None
        if t == "slack.slack_messages":
            mid = r.get("id") or w.get("id")
            cid, ts = (r.get("channel_id"), r.get("ts")) if op == "insert" else (slack_ids.get(mid) or found.get(mid) or (None, None))
            keys = [x for x in (mid, f"{cid}/{ts}" if cid else None) if x]
            v = chan_v(cid) if cid else V("UNVERIFIED", f"message {mid} not found in SQL or base (U7)")
        elif t == "slack.slack_channels":
            cid = r.get("id") or w.get("id")
            keys = [cid]
            v = chan_v(cid)
        elif t == "slack.slack_files":
            fid, cid = r.get("id") or w.get("id"), r.get("channel_id")
            if not cid and fid:
                cid = (u.slack_files().get(fid) or [None])[0]
            keys = [fid]
            v = _metadata_only(chan_v(cid)) if cid else _metadata_only(V("UNVERIFIED", f"file {fid} has no channel (U7)"))
        elif t.startswith("slack."):
            keys = [x for x in (r.get("id"), w.get("id")) if x]
            who = r.get("user_id")
            v = V("UNVERIFIED", f"{t}: not covered by the stated Slack rules (U6)"
                  + (f"; row user_id={who}, persona={u.slack_uid(pe)}" if who else ""))
        elif t in ("gmail.gmail_messages", "gmail.gmail_threads"):
            oid = r.get("id") or w.get("id")
            mb = r.get("user_email") or gm_msgs.get(oid) or gm_threads.get(oid) or (oid.split("/", 1)[0] if oid and "/" in oid else None)
            keys = [x for x in (oid, r.get("thread_id")) if x]
            mine = _persona_mailbox(u, p)
            if mb == pe:
                v = V("YES", f"row user_email is the persona ({pe})" + ("" if mine else
                      "; NOTE persona has no base mailbox (gmail_users row needed?)"), user_email=mb)
            else:
                v = V("NO", f"row is in mailbox {mb}, not the persona's ({pe})", user_email=mb)
        elif t == "gmail.gmail_attachments":
            mid = r.get("message_id")
            mb = gm_msgs.get(mid) or (mid.split("/", 1)[0] if mid and "/" in mid else None)
            keys = [x for x in (r.get("id"), mid) if x]
            v = _metadata_only(V("YES", "attachment's message is in the persona's mailbox", user_email=mb) if mb == pe else
                               V("NO", f"attachment's message is in mailbox {mb}", user_email=mb) if mb else
                               V("UNVERIFIED", "attachment's message mailbox unknown (U6)"))
        elif t == "gmail.gmail_users":
            e = r.get("email_address") or w.get("email_address")
            keys = [e]
            v = V("YES", "the persona's own mailbox profile") if e == pe else V("NO", f"mailbox profile of {e}")
        elif t.startswith("gmail."):
            e = r.get("user_email") or w.get("user_email")
            keys = [x for x in (r.get("id"), w.get("id")) if x]
            v = (V("YES", "row user_email is the persona") if e == pe else V("NO", f"row user_email={e}") if e
                 else V("UNVERIFIED", f"{t} row without user_email (U6)"))
        elif t == "gcal.gcal_events":
            eid = r.get("event_id") or w.get("event_id")
            keys = [eid]
            if op == "insert":
                try:
                    att = [a.get("email") for a in json.loads(r.get("attendees_json") or "[]") or [] if isinstance(a, dict)]
                except ValueError:
                    att = []
                cal, uid, st = r.get("calendar_id"), r.get("ical_uid"), _ev_start(r)
            else:
                be = g["events"].get(eid)
                cal, uid, att, st = (be[0], be[1], be[5], be[3]) if be else (w.get("calendar_id"), None, [], None)
            v = _event_verdict(pe, eid, cal, uid, att, all_cals, g["by_uid"], g["events"],
                               extra_copies=uid_copies.get(uid, []), start=st)
        elif t == "gcal.gcal_calendars":
            cid = r.get("calendar_id") or w.get("calendar_id")
            keys = [cid]
            c = all_cals.get(cid) or {}
            v = (V("YES", "persona owns the calendar") if c.get("owner") == pe else
                 V("YES", "calendar shared with the persona") if pe in (c.get("shared") or []) else
                 V("NO", f"calendar owned by {c.get('owner')}"))
        elif t.startswith("gcal."):
            keys = [x for x in (r.get("calendar_id"), r.get("rule_id"), w.get("calendar_id")) if x]
            v = V("UNVERIFIED", f"{t}: not covered by the stated GCal rules (U6)")
        elif t == "gdrive.drive_files":
            fid = r.get("id") or w.get("id")
            keys = [fid]
            v = drive_v(fid)
        elif t.startswith("gdrive."):
            fid = r.get("spreadsheet_id") or r.get("file_id")
            keys = [x for x in (fid, r.get("id"), w.get("id")) if x]
            v = drive_v(fid) if fid else V("UNVERIFIED", f"{t}: not covered by the stated Drive rules (U6)")
        elif svc in ("gdocs", "gsheets", "gslides"):
            fid = (r.get("document_id") or r.get("spreadsheet_id") or r.get("presentation_id") or r.get("drive_file_id")
                   or w.get("document_id") or w.get("spreadsheet_id") or w.get("presentation_id"))
            keys = [x for x in (fid, r.get("object_id"), r.get("page_object_id")) if x]
            if r.get("sheet_id") is not None and fid:
                keys.append(f"{fid}#{r.get('sheet_id')}")
            v = drive_v(fid, svc) if fid else V("UNVERIFIED", f"{t} row without a file id (U6)")
        else:
            v = V("UNVERIFIED", f"{t}: unknown scoped table (U6)")
        is_lb = any(k in lb for k in keys)
        rows.append({"line": s["line"], "table": t, "op": op, "keys": keys, "load_bearing": is_lb,
                     "verdict": v["verdict"], "reason": v["reason"]})

    matched = {k for row in rows for k in row.get("keys", [])}
    base_lb = []
    for k in sorted(lb - matched):
        svc = ("gdrive" if re.match(r"[fd]_[0-9a-f]{22}$", k) else "gcal" if k.startswith("evt_") else
               "slack" if re.match(r"[CDG][A-Z0-9]+(/\d+\.\d+)?$|F[A-Z0-9]+$", k) else
               "gmail" if "/" in k and ("@" in k or "_EMAIL" in k) else None)
        if svc is None:
            base_lb.append({"id": k, "verdict": "UNVERIFIED", "reason": "load-bearing id matches no SQL row and its service "
                            "cannot be inferred (U4)"})
        else:
            r = can_see(u, p, svc, k)
            base_lb.append({"id": k, "service": svc, "verdict": r["verdict"], "reason": "base record: " + r["reason"]})
    summary = Counter(row["verdict"] for row in rows)
    by_table = defaultdict(Counter)
    for row in rows:
        by_table[row["table"]][row["verdict"]] += 1
    bad = {"NO"} if allow_unverified else {"NO", "UNVERIFIED"}
    fails = [row for row in rows if row.get("load_bearing") and row["verdict"] in bad]
    fails += [x for x in base_lb if x["verdict"] in bad]
    return {"persona": p["persona_key"], "persona_email": pe, "usable_in_tasks": p["usable_in_tasks"], "rows": rows,
            "load_bearing_base_ids": base_lb, "summary": dict(summary),
            "by_table": {k: dict(v) for k, v in sorted(by_table.items())},
            "unscoped_rows_visible": dict(unscoped_rows), "load_bearing_given": bool(lb),
            "load_bearing_failures": len(fails),
            "verdict": ("REPORT-ONLY" if not lb else "FAIL" if fails else "PASS")}


# ---------------------------------------------------------------- text rendering

def _txt_verdict(r: dict) -> str:
    ev = ", ".join(f"{k}={v}" for k, v in r["evidence"].items() if v not in (None, "", [], {}) and k != "message")
    msg = r["evidence"].get("message")
    if msg:
        ev += f", message=[ts {msg['ts']} {msg['date']} user {msg['user']}{' reply' if msg['is_reply'] else ''}]"
    return f"{r['verdict']}\n  reason:   {r['reason']}\n  evidence: {ev}"


def _txt_reach(r: dict) -> str:
    P = r["persona"]
    L = [f"REACH  {P['name']} <{P['email']}>  {P['role']} / {P['department']}"
         + ("" if P["usable_in_tasks"] else "   ** NOT USABLE IN TASKS (not in Evals roster) **"),
         f"clock {r['clock'][:10]}"]
    s = r["services"]["slack"]
    L.append(f"\nSLACK  user={s['slack_user_id']}  visible channels={s['channels_visible']} {s['by_kind']}  "
             f"messages={s['messages_visible']}  public-not-member (UNVERIFIED)={s['public_channels_not_member_UNVERIFIED']}")
    L.append(f"  persona posts={s['persona_messages_posted']} last post={s['persona_last_post']}  "
             f"last activity in visible channels={s['last_activity_in_visible_channels']}")
    for c in s["top_channels"]:
        L.append(f"  {c['id']:14} {str(c['name'])[:38]:38} {c['kind']:7} mem={c['members']:<3} msgs={c['messages']:<6} "
                 f"{c['first']}..{c['last']}{' archived' if c['archived'] else ''}")
    gm = r["services"]["gmail"]
    if gm.get("mailbox"):
        L.append(f"\nGMAIL  mailbox={gm['mailbox']} threads={gm['threads']} messages={gm['messages']} "
                 f"range={str(gm['first'])[:10]}..{str(gm['last'])[:10]}")
        L.append(f"  threads by last-message month (recent): {gm['threads_by_last_month_recent']}")
        if gm.get("top_correspondents"):
            L.append("  top correspondents: " + ", ".join(f"{a} ({n})" for a, n in gm["top_correspondents"]))
    else:
        L.append(f"\nGMAIL  none - {gm['note']}")
    gc = r["services"]["gcal"]
    L.append(f"\nGCAL  own={gc['calendars_owned']} shared={gc['calendars_shared_with']} events={gc['events_visible']} "
             f"(distinct ical_uid {gc['distinct_ical_uids']}, cancelled {gc['cancelled']})")
    L.append(f"  last event before clock={gc['last_event_start_before_clock']}  next after clock={gc['next_event_after_clock']}")
    L.append("  by month: " + " ".join(f"{k}:{v}" for k, v in gc["events_by_month"].items()))
    d = r["services"]["drive"]
    L.append(f"\nDRIVE  owned={d['owned_total']} {d['owned_by_mime']}")
    L.append(f"  shared-with={d['shared_with_total']} {d['shared_by_mime']}")
    L.append(f"  shared by owner: {d['shared_by_owner']}")
    L.append(f"  native visible: {d['native_visible']}  last modified visible={d['last_modified_visible']}")
    L.append(f"  UNVERIFIED (domain/anyone, not owned/shared)={d['UNVERIFIED_domain_or_anyone_total']} {d['UNVERIFIED_by_mime']}")
    L.append(f"\nUNSCOPED (always visible): {', '.join(UNSCOPED)}")
    L.append("\nLAST ACTIVITY (days before clock): " + ", ".join(
        f"{k}={v} ({r['last_activity_days_before_clock'][k]}d)" if v else f"{k}=none" for k, v in r["last_activity"].items()))
    return "\n".join(L)


def _txt_search(r: dict) -> str:
    L = [f"SEARCH {r['service']} {r['query']!r} as {r['persona']}  scope: {r['scope']}",
         f"visible hits={r['visible_total']} (showing {len(r['visible'])})  hidden by ACL={r['hidden_by_acl']} "
         f"in {r['hidden_containers']} containers  UNVERIFIED={r['unverified']} in {r['unverified_containers']} containers"]
    for h in r["visible"]:
        L.append("  " + json.dumps(h, ensure_ascii=False)[:300])
    if r.get("note"):
        L.append(f"note: {r['note']}")
    return "\n".join(L)


def _txt_check(r: dict) -> str:
    L = [f"CHECK-SQL as {r['persona']} <{r['persona_email']}>" + ("" if r["usable_in_tasks"] else "  ** NOT USABLE IN TASKS **")]
    for row in r["rows"]:
        lb = " LB" if row.get("load_bearing") else ""
        L.append(f"[{row['verdict']}{lb}] L{row['line']} {row['table']} {row['op']} {', '.join(map(str, row['keys']))[:90]} "
                 f"- {row['reason']}")
    for x in r["load_bearing_base_ids"]:
        L.append(f"[{x['verdict']} LB] base {x.get('service', '?')} {x['id']} - {x['reason']}")
    L.append(f"\nsummary: {r['summary']}  unscoped rows (always visible): {sum(r['unscoped_rows_visible'].values())}")
    for t, c in r["by_table"].items():
        L.append(f"  {t}: {c}")
    L.append(f"verdict: {r['verdict']}" + (f" ({r['load_bearing_failures']} load-bearing rows not visible)"
                                          if r["load_bearing_given"] else " (no --load-bearing list: report only)"))
    return "\n".join(L)


# ---------------------------------------------------------------- self-test

def _self_test() -> int:
    u = Universe()
    ok = [0]

    def check(cond, msg):
        if not cond:
            raise AssertionError(msg)
        ok[0] += 1
        print(f"  ok  {msg}")

    P = {p["persona_key"]: p for p in personas()}
    check(len(P) == 19 and sum(p["usable_in_tasks"] for p in P.values()) == 17, "19 personas, 17 usable in tasks")
    check(not P["thomas"]["usable_in_tasks"] and not P["tim_steudler"]["usable_in_tasks"], "thomas + tim_steudler flagged not usable")
    v1 = {p["persona_key"]: p for p in _load(ROSTER_V1)}
    check(all({k: P[key][k] for k in ("name", "email", "role", "department")} == {k: v1[key][k] for k in
              ("name", "email", "role", "department")} for key in v1), "roster_v2 copies the 17 Evals entries exactly")
    check(resolve_persona("Arthur Blake")["email"] == "arthur.blake@harmonygames.co", "persona resolves by exact name")

    # slack
    ab = P["arthur_blake"]
    r = can_see(u, ab, "slack", "C080X4GTZ0E")
    check(r["verdict"] == "YES" and r["evidence"]["name"] == "live-incidents", "Arthur Blake is a member of C080X4GTZ0E (#live-incidents)")
    s = u.slack()
    tim_uid = u.slack_uid(P["tim_steudler"]["email"])
    check(tim_uid == "UBF5AB53C96" and not any(tim_uid in c["members"] for c in s["channels"].values()),
          "Tim Steudler (UBF5AB53C96) has no Slack channels")
    check(can_see(u, P["tim_steudler"], "slack", "C080X4GTZ0E")["verdict"] == "UNVERIFIED",
          "public channel, non-member -> UNVERIFIED")
    check(can_see(u, P["julia_lawson"], "slack", "C017C8D7AD41")["verdict"] == "NO", "MPIM non-member -> NO")
    check(can_see(u, P["calvin_price"], "slack", "C017C8D7AD41")["verdict"] == "YES", "MPIM member -> YES")
    r = can_see(u, ab, "slack", "C017C8D7AD41/1731890278.557969")
    check(r["verdict"] == "YES" and r["evidence"]["message"]["id"] == "9d4d8ed8acddc1f4b3953e29e6a56823",
          "message inherits channel verdict (C017C8D7AD41/1731890278.557969)")
    check(can_see(u, P["julia_lawson"], "slack", "F080TSWCCVD")["verdict"] == "NO", "Slack file inherits its channel (NO)")
    reach_t = reach(u, P["tim_steudler"], correspondents=False)
    check(reach_t["services"]["slack"]["channels_visible"] == 0, "reach: Tim sees 0 Slack channels")

    # gmail
    boxes = u.gmail_mailboxes()
    check(P["marcus_bennett"]["email"] in boxes and "marcus@harmonygames.co" not in boxes,
          "Marcus Bennett's mailbox is marcus.bennett@harmonygames.co (marcus@ is not a mailbox)")
    g = u.gmail()["threads"]
    ab_tid = "arthur.blake@harmonygames.co/1826526974265913874"
    check(ab_tid in g, f"base thread {ab_tid} exists")
    check(can_see(u, ab, "gmail", ab_tid)["verdict"] == "YES", "Arthur sees his own mailbox thread")
    check(can_see(u, P["leonard_hayes"], "gmail", ab_tid)["verdict"] == "NO", "Leonard cannot see Arthur's copy")
    mtid = next(t for t, e in g.items() if e[0] == P["marcus_bennett"]["email"])
    check(can_see(u, P["marcus_bennett"], "gmail", mtid)["verdict"] == "YES",
          "Marcus Bennett sees a thread in his own mailbox")
    check(can_see(u, ab, "gmail", mtid)["verdict"] == "NO", "Arthur cannot read a thread only in Marcus's mailbox")
    ttid = next(t for t, e in g.items() if e[0] == "EMPLOYEE_0011_EMAIL")
    check(who_can_see(u, "gmail", ttid)["YES"] == [], "tokenized mailbox thread visible to no persona")

    # gcal
    r = can_see(u, P["martin_walsh"], "gcal", "evt_00009bfb80dabb15aa5bb5")
    check(r["verdict"] == "YES" and "own calendar" in r["reason"], "GCal owner sees event on own calendar")
    r = can_see(u, P["robert"], "gcal", "evt_00009bfb80dabb15aa5bb5")
    check(r["verdict"] == "YES" and r["evidence"].get("own_copy"), "GCal attendee with own copy -> YES via own copy")
    check(can_see(u, P["simon_walker"], "gcal", "evt_00009bfb80dabb15aa5bb5")["verdict"] == "NO", "GCal non-attendee -> NO")
    check(all(c["owner"] == cid and not c["shared"] for cid, c in u.gcal()["calendars"].items()),
          "every base calendar: calendar_id == owner_email, no sharing")

    # drive
    w = who_can_see(u, "gdrive", "f_002139fb73222ed7c9d478")
    d = u.drive()["f_002139fb73222ed7c9d478"]
    check(str(d[2]).startswith("Resource:") and not d[3] and d[4] == "private" and w["YES"] == [] and w["UNVERIFIED"] == [],
          "Resource:-owned unshared file f_002139fb73222ed7c9d478 is visible to no one")
    check(can_see(u, P["tim_steudler"], "gdrive", "f_00da0af9039fdf198986af")["verdict"] == "UNVERIFIED",
          "domain-visibility file, not shared -> UNVERIFIED")
    check(can_see(u, P["simon_walker"], "gdrive", "f_12b4105f4b64c3ad374a9f")["verdict"] == "YES", "shared_with -> YES")
    doc = next(fid for fid, x in u.drive().items() if x[1] == NATIVE_MIME["gdocs"] and "arthur.blake@harmonygames.co" in x[3])
    check(can_see(u, ab, "gdocs", doc)["verdict"] == "YES", "GDocs uses the Drive record")
    check(can_see(u, ab, "gsheets", doc)["verdict"] == "UNVERIFIED", "GSheets on a Doc id -> UNVERIFIED (U5)")

    # unscoped
    for svc in UNSCOPED:
        check(can_see(u, P["tim_steudler"], svc, "anything")["verdict"] == "YES", f"can-see on unscoped {svc} is YES")

    # check-sql (synthetic SQL, base records verified above)
    sql = """
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text) VALUES ('a', '1770900000.000001', 'C080X4GTZ0E', 'message', 'EMPLOYEE_0025_SLACK_ID', 'x');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text) VALUES ('b', '1770900000.000002', 'C017C8D7AD41', 'message', 'EMPLOYEE_0025_SLACK_ID', 'x');
UPDATE slack.slack_channels SET members_json = '["EMPLOYEE_0005_SLACK_ID","EMPLOYEE_0006_SLACK_ID","EMPLOYEE_0016_SLACK_ID","EMPLOYEE_0025_SLACK_ID","EMPLOYEE_0038_SLACK_ID"]', num_members = 5 WHERE id = 'C017C8D7AD41';
INSERT INTO gmail.gmail_threads (id, user_email) VALUES ('julia.lawson@harmonygames.co/1', 'julia.lawson@harmonygames.co');
INSERT INTO gmail.gmail_messages (id, thread_id, user_email) VALUES ('julia.lawson@harmonygames.co/<m1>', 'julia.lawson@harmonygames.co/1', 'julia.lawson@harmonygames.co');
INSERT INTO gmail.gmail_messages (id, thread_id, user_email) VALUES ('robert@harmonygames.co/<m1>', 'robert@harmonygames.co/1', 'robert@harmonygames.co');
INSERT INTO gdrive.drive_files (id, name, mime_type, owner_email, shared_with_emails_json, visibility) VALUES ('f_aaaaaaaaaaaaaaaaaaaaaa', 'Doc', 'application/vnd.google-apps.document', 'robert@harmonygames.co', '[]', 'private');
UPDATE gdrive.drive_files SET shared_with_emails_json = '["julia.lawson@harmonygames.co"]' WHERE id = 'f_aaaaaaaaaaaaaaaaaaaaaa';
INSERT INTO gdocs.docs_documents (document_id, title, owner_email, shared_with_emails_json, visibility, drive_file_id) VALUES ('f_aaaaaaaaaaaaaaaaaaaaaa', 'Doc', 'robert@harmonygames.co', '["julia.lawson@harmonygames.co"]', 'private', 'f_aaaaaaaaaaaaaaaaaaaaaa');
INSERT INTO gdrive.drive_files (id, name, mime_type, owner_email, shared_with_emails_json, visibility) VALUES ('f_bbbbbbbbbbbbbbbbbbbbbb', 'Hidden', 'text/plain', 'robert@harmonygames.co', '[]', 'private');
INSERT INTO gcal.gcal_events (event_id, calendar_id, ical_uid, attendees_json) VALUES ('evt_x1', 'julia.lawson@harmonygames.co', 'u1@hg4', '[{"email":"julia.lawson@harmonygames.co","self":true}]');
INSERT INTO gcal.gcal_events (event_id, calendar_id, ical_uid, attendees_json) VALUES ('evt_x2', 'robert@harmonygames.co', 'u2@hg4', '[{"email":"robert@harmonygames.co","self":true}]');
INSERT INTO linear.linear_comments (id, issue_id, author_id, body) VALUES ('c1', 'ENG-1', 'usr_x', 'y');
"""
    res = check_sql(u, P["julia_lawson"], sql, load_bearing={"a", "b", "f_aaaaaaaaaaaaaaaaaaaaaa", "evt_x1"})
    by = {tuple(r["keys"])[0]: r["verdict"] for r in res["rows"]}
    check(by["a"] == "YES", "check-sql: Julia is a member of #live-incidents -> YES")
    check(by["b"] == "YES", "check-sql: members_json UPDATE adds Julia to the MPIM -> YES")
    check(by["julia.lawson@harmonygames.co/<m1>"] == "YES" and by["robert@harmonygames.co/<m1>"] == "NO",
          "check-sql: Gmail rows judged by user_email")
    check(by["f_aaaaaaaaaaaaaaaaaaaaaa"] == "YES" and by["f_bbbbbbbbbbbbbbbbbbbbbb"] == "NO",
          "check-sql: Drive sharing UPDATE applied; GDocs row inherits")
    check(by["evt_x1"] == "YES" and by["evt_x2"] == "NO", "check-sql: GCal rows on persona calendar only")
    check(res["verdict"] == "PASS" and res["unscoped_rows_visible"] == {"linear.linear_comments": 1},
          "check-sql: load-bearing rows all visible -> PASS; unscoped rows counted")
    res2 = check_sql(u, P["julia_lawson"], sql, load_bearing={"f_bbbbbbbbbbbbbbbbbbbbbb"})
    check(res2["verdict"] == "FAIL", "check-sql: invisible load-bearing row -> FAIL")
    res3 = check_sql(u, P["julia_lawson"], sql, load_bearing={ab_tid})
    check(res3["verdict"] == "FAIL" and res3["load_bearing_base_ids"][0]["verdict"] == "NO",
          "check-sql: load-bearing base id outside the persona's mailbox -> FAIL")
    print(f"self-test: ok ({ok[0]} assertions)")
    return 0


# ---------------------------------------------------------------- CLI

def main(argv: list) -> int:
    if "--self-test" in argv:
        try:
            return _self_test()
        except AssertionError as e:
            print(f"self-test: FAIL - {e}")
            return 1
    ap = argparse.ArgumentParser(prog="persona_view.py", description="Persona-scoped view of the HarmonyGames base.")
    sub = ap.add_subparsers(dest="cmd")
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--json", action="store_true")
    sp = sub.add_parser("personas", parents=[common])
    sp = sub.add_parser("reach", parents=[common])
    sp.add_argument("persona")
    sp.add_argument("--top", type=int, default=10)
    sp.add_argument("--no-correspondents", action="store_true", help="skip reading mailbox files for correspondents")
    sp = sub.add_parser("can-see", parents=[common])
    sp.add_argument("persona")
    sp.add_argument("service")
    sp.add_argument("id")
    sp.add_argument("--calendar")
    sp = sub.add_parser("who-can-see", parents=[common])
    sp.add_argument("service")
    sp.add_argument("id")
    sp.add_argument("--calendar")
    sp = sub.add_parser("search", parents=[common])
    sp.add_argument("persona")
    sp.add_argument("service")
    sp.add_argument("query")
    sp.add_argument("--limit", type=int, default=20)
    sp.add_argument("--no-hidden", action="store_true", help="skip scanning containers the persona cannot see")
    sp = sub.add_parser("check-sql", parents=[common])
    sp.add_argument("persona")
    sp.add_argument("sql_file")
    sp.add_argument("--load-bearing")
    sp.add_argument("--allow-unverified", action="store_true")
    a = ap.parse_args(argv)
    if not a.cmd:
        print(__doc__, file=sys.stderr)
        return 2
    if a.cmd == "personas":
        ps = personas()
        print(json.dumps(ps, indent=2) if a.json else "\n".join(
            f"{p['persona_key']:16} {p['email']:34} {p['name']:16} {p['role']}"
            + ("" if p["usable_in_tasks"] else "  ** NOT USABLE IN TASKS **") for p in ps))
        return 0
    u = Universe()
    if a.cmd == "reach":
        r = reach(u, resolve_persona(a.persona), a.top, not a.no_correspondents)
        print(json.dumps(r, indent=2) if a.json else _txt_reach(r))
        return 0
    if a.cmd == "can-see":
        p = resolve_persona(a.persona)
        r = can_see(u, p, a.service, a.id, a.calendar)
        r = {"persona": p["persona_key"], "usable_in_tasks": p["usable_in_tasks"], "service": a.service, "id": a.id, **r}
        print(json.dumps(r, indent=2) if a.json else f"{p['persona_key']} {a.service} {a.id}: " + _txt_verdict(r))
        return 0
    if a.cmd == "who-can-see":
        r = who_can_see(u, a.service, a.id, a.calendar)
        if a.json:
            print(json.dumps(r, indent=2))
        else:
            print(f"WHO-CAN-SEE {a.service} {a.id}")
            for k in ("YES", "NO", "UNVERIFIED"):
                print(f"  {k:10} ({len(r[k])}): {', '.join(r[k]) or '-'}")
            for key, v in r["detail"].items():
                print(f"  {key:16} {v['verdict']:10} {v['reason']}")
        return 0
    if a.cmd == "search":
        r = search(u, resolve_persona(a.persona), a.service.lower(), a.query, a.limit, not a.no_hidden)
        print(json.dumps(r, indent=2, ensure_ascii=False) if a.json else _txt_search(r))
        return 0
    if a.cmd == "check-sql":
        lb = None
        if a.load_bearing:
            lb = {ln.strip() for ln in Path(a.load_bearing).read_text().splitlines()
                  if ln.strip() and not ln.strip().startswith("#")}
        r = check_sql(u, resolve_persona(a.persona), Path(a.sql_file).read_text(), lb, a.allow_unverified)
        print(json.dumps(r, indent=2) if a.json else _txt_check(r))
        return 1 if r["verdict"] == "FAIL" else 0
    return 2


if __name__ == "__main__":
    from runtime_context import guarded_entry
    guarded_entry(globals(), require_source="personas" not in sys.argv[1:])
    raise SystemExit(main(sys.argv[1:]))
