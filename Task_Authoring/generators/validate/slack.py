"""Slack: load base channels as DB-shaped rows, and invariants S1-S11 for a proposed overlay.

Independent of the emitter: nothing here imports generators/services, tools/sql_lint.py or tools/base_check.py. The
rules are re-implemented from their written sources and from the base export itself:
- Task_Authoring/references/universe_schema_live.json and universe_constraints_live.json (slack_messages: PRIMARY KEY
  id, UNIQUE (channel_id, ts), thread_parent_id REFERENCES slack_messages(id))
- Evals/0_Injection_Quality_Eval.md Check A (references, ids) and Check C (replies follow parents, event times at or
  before the clock)
- the platform's /injection reports on accepted SQL (support/completed_tasks/owen_dd_bug_carryover_2026-11-09/
  eval_reports/0_injection_FAIL_r3.md C1: a join needs the user not to be a member; 0_injection_PASS_r7.md)
- the base export: id = sha256("<channel>|<ts>")[:32] on every normalized row; a thread's first post carries
  thread_ts = its own ts and reply_count / reply_users_count / latest_reply equal to its reply rows; replies carry
  0 / 0 / null; no reply to a reply; every channel_join names its own user and that user is in the channel's members.

The export keeps the API shape (user, channel, thread_ts, reactions, files, attachments, members); load_base maps it
onto the live column names. Columns the export does not hold (thread_parent_id, created_at, metadata_json, edited_*,
bot_id, client_msg_id, permalink) are None on base rows. About 13% of base messages are raw Slack API rows without an
id: they are kept (they count as replies and posts) under the key ("noid:<channel>:<ts>",) with id None.

Rules (FAIL blocks publication, WARN is recorded):
  S1  row shape of an inserted message: ts, id contract, type, created_at = ts, JSON columns, non-empty content
  S2  channel and user exist
  S3  (channel_id, ts) is unique
  S4  a reply: parent exists in the same channel, is earlier, is not itself a reply; thread_ts_legacy = parent ts;
      the reply's own counters are 0 / 0 / NULL
  S5  thread counters of every touched parent equal its replies; a post without replies has none (WARN: a first
      post of a thread whose thread_ts_legacy is not its own ts)
  S6  the author is a member of the channel at that time (member list and join/leave rows)
  S7  membership rows: wording, join/leave alternate, first join listed in members, no posts while outside
  S8  no event time at or after the freeze
  S9  a post is not older than its channel (WARN: a post into an archived channel)
  S10 <@user> and <#channel> mentions resolve
  S11 a channel update keeps num_members = len(members_json) and only lists Slack users
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
from pathlib import Path

from generators.validate.invariants import FAIL, WARN, Finding
from generators.validate.overlay import Overlay

MESSAGES = "slack.slack_messages"
CHANNELS = "slack.slack_channels"
USERS = "slack.slack_users"
MANIFEST = "source_manifest.json"

_TS = re.compile(r"^([0-9]{10})\.([0-9]{6})$")
_ISO = re.compile(r"^(\d{4})-(\d{2})-(\d{2})[T ](\d{2}):(\d{2}):(\d{2})(?:\.(\d{1,6}))?(Z|[+-]\d{2}(?::?\d{2})?)?$",
                  re.ASCII)
_CHANNEL_ID = re.compile(r"^[A-Z0-9]{8,14}$")
_MENTION_USER = re.compile(r"<@([A-Z0-9_]+)(?:\|[^>]*)?>")
_MENTION_CHANNEL = re.compile(r"<#([A-Z0-9]+)(?:\|[^>]*)?>")
_JOIN, _LEAVE = "channel_join", "channel_leave"
_EPOCH = dt.datetime(1970, 1, 1, tzinfo=dt.timezone.utc)


class SlackBaseError(Exception):
    """The Slack export is not the pinned one, or a file of it cannot be used."""


# --------------------------------------------------------------------------- loading

def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _json_text(value) -> str:
    return json.dumps(value, ensure_ascii=False)


def channels_of(ops) -> set[str]:
    """Channel ids an op list names (inserted messages' channel_id, channel update keys)."""
    out = set()
    for op in ops:
        if op.table == MESSAGES and op.op == "insert":
            out.add(dict(op.cols).get("channel_id"))
        elif op.table == CHANNELS:
            out.add(dict(op.where).get("id") or dict(op.cols).get("id"))
    return {c for c in out if isinstance(c, str) and _CHANNEL_ID.match(c)}


def _message_row(item: dict) -> tuple[tuple, dict]:
    ts, channel, mid = item.get("ts"), item.get("channel"), item.get("id")
    row = {
        "id": mid, "ts": ts, "channel_id": channel, "type": item.get("type"), "user_id": item.get("user"),
        "text": item.get("text"), "thread_parent_id": None, "thread_ts_legacy": item.get("thread_ts"),
        "reply_count": item.get("reply_count") or 0, "reply_users_count": item.get("reply_users_count") or 0,
        "latest_reply": item.get("latest_reply"), "is_activity_message": bool(item.get("is_activity_message")),
        "subtype": item.get("subtype"), "reactions_json": _json_text(item.get("reactions") or []),
        "files_json": _json_text(item.get("files") or []),
        "attachments_json": _json_text(item.get("attachments") or []), "created_at": None, "edited_ts": None,
        "edited_user": None, "bot_id": item.get("bot_id"), "client_msg_id": item.get("client_msg_id"),
        "permalink": None, "metadata_json": None,
    }
    key = (mid,) if isinstance(mid, str) and mid else (f"noid:{channel}:{ts}",)
    return key, row


def load_base(slack_dir: Path, manifest_sha256: str, channels) -> dict[str, dict[tuple, dict]]:
    """Channels, users and every message of the named channels as DB-shaped rows keyed by primary key.

    `manifest_sha256` is the spec's pin of <slack_dir>/source_manifest.json; every file read must equal its entry
    there. A mismatch, an unlisted file or a channel that is not in the export raises SlackBaseError."""
    root = Path(slack_dir)
    raw = (root / MANIFEST).read_bytes()
    if _sha(raw) != manifest_sha256:
        raise SlackBaseError(f"{root / MANIFEST}: sha256 {_sha(raw)} is not the pinned {manifest_sha256}")
    listed = {f["path"]: f.get("sha256") for f in json.loads(raw.decode("utf-8")).get("files", [])
              if isinstance(f, dict) and isinstance(f.get("path"), str)}

    def read(rel: str):
        if rel not in listed:
            raise SlackBaseError(f"{rel} is not listed in {MANIFEST}")
        data = (root / rel).read_bytes()
        if _sha(data) != listed[rel]:
            raise SlackBaseError(f"{rel}: sha256 {_sha(data)} differs from {MANIFEST} ({listed[rel]})")
        return json.loads(data.decode("utf-8"))

    base: dict[str, dict[tuple, dict]] = {CHANNELS: {}, USERS: {}, MESSAGES: {}}
    for item in read("channels.json"):
        created = item.get("created")
        base[CHANNELS][(item["id"],)] = {
            "id": item["id"], "name": item.get("name"), "is_channel": bool(item.get("is_channel")),
            "is_private": bool(item.get("is_private")), "is_im": bool(item.get("is_im")),
            "is_mpim": bool(item.get("is_mpim")), "is_archived": bool(item.get("is_archived")),
            "is_general": bool(item.get("is_general")), "num_members": item.get("num_members"),
            "topic": item.get("topic"), "purpose": item.get("purpose"),
            "created_ts": float(created) if created not in (None, "") else 0.0,
            "creator_id": item.get("creator"), "members_json": _json_text(item.get("members") or []),
        }
    for item in read("users.json"):
        base[USERS][(item["id"],)] = dict(item)
    for channel in sorted(c for c in channels if isinstance(c, str)):
        if (channel,) not in base[CHANNELS]:
            continue                                # S2 reports the unknown channel
        prefix = f"messages/{channel}/"
        for rel in sorted(p for p in listed if p.startswith(prefix)):
            for item in read(rel):
                if isinstance(item, dict) and _TS.match(str(item.get("ts") or "")):
                    key, row = _message_row(item)
                    base[MESSAGES][key] = row
    return base


# --------------------------------------------------------------------------- helpers

def _finding(rule: str, severity: str, table: str, key: tuple, message: str) -> Finding:
    return Finding(rule=rule, severity=severity, table=table, key=key, message=message)


def _ts_key(ts) -> tuple | None:
    m = _TS.match(ts) if isinstance(ts, str) else None
    return (int(m.group(1)), int(m.group(2))) if m else None


def _ts_instant(ts) -> dt.datetime | None:
    key = _ts_key(ts)
    return _EPOCH + dt.timedelta(seconds=key[0], microseconds=key[1]) if key else None


def _iso_instant(value) -> dt.datetime | None:
    m = _ISO.match(value) if isinstance(value, str) else None
    if not m:
        return None
    y, mo, d, h, mi, s, frac, tz = m.groups()
    try:
        when = dt.datetime(int(y), int(mo), int(d), int(h), int(mi), int(s), int((frac or "0").ljust(6, "0")),
                           tzinfo=dt.timezone.utc)
    except ValueError:
        return None
    if tz and tz != "Z":
        sign = 1 if tz[0] == "+" else -1
        digits = tz[1:].replace(":", "")
        when -= sign * dt.timedelta(hours=int(digits[:2]), minutes=int(digits[2:] or 0))
    return when


def _kind(channel: dict) -> str:
    if channel.get("is_im"):
        return "im"
    if channel.get("is_mpim"):
        return "mpim"
    if str(channel.get("name") or "").startswith("FC:"):
        return "canvas"
    return "private" if channel.get("is_private") else "public"


def _members(channel: dict | None) -> list:
    try:
        value = json.loads((channel or {}).get("members_json") or "[]")
    except (TypeError, ValueError):
        return []
    return value if isinstance(value, list) else []


class _State:
    """Per-channel indexes over the post-overlay messages."""

    def __init__(self, overlay: Overlay, base: dict):
        self.overlay, self.base = overlay, base
        self.messages = overlay.state.get(MESSAGES) or {}
        self.channels = overlay.state.get(CHANNELS) or {}
        self.users = overlay.state.get(USERS) or {}
        self.by_channel: dict[str, list] = {}
        for key, row in self.messages.items():
            self.by_channel.setdefault(row.get("channel_id"), []).append((key, row))
        self._events: dict[tuple, list] = {}
        self._replies: dict[tuple, list] = {}

    def inserted(self) -> list:
        keys = self.overlay.inserted.get(MESSAGES, ())
        return [(k, self.messages[k]) for k in keys if k in self.messages]

    def events(self, channel: str, user: str) -> list:
        """Sorted (ts key, 'join' | 'leave', message key) of one user's membership rows in one channel."""
        ck = (channel, user)
        if ck not in self._events:
            out = []
            for key, row in self.by_channel.get(channel, ()):
                if row.get("user_id") == user and row.get("subtype") in (_JOIN, _LEAVE) and _ts_key(row.get("ts")):
                    out.append((_ts_key(row["ts"]), "join" if row["subtype"] == _JOIN else "leave", key))
            self._events[ck] = sorted(out, key=lambda e: e[0])
        return self._events[ck]

    def replies(self, channel: str, parent_ts: str) -> list:
        ck = (channel, parent_ts)
        if ck not in self._replies:
            self._replies[ck] = [row for _, row in self.by_channel.get(channel, ())
                                 if row.get("thread_ts_legacy") == parent_ts and row.get("ts") != parent_ts]
        return self._replies[ck]

    def at(self, channel: str, ts: str) -> list:
        return [(key, row) for key, row in self.by_channel.get(channel, ()) if row.get("ts") == ts]

    def member_at(self, channel: str, user: str, when: tuple) -> bool:
        events = self.events(channel, user)
        before = [kind for key, kind, _ in events if key < when]
        if before:
            return before[-1] == "join"
        after = [kind for key, kind, _ in events if key > when]
        if after:
            return after[0] == "leave"
        return user in _members(self.channels.get((channel,)))


# --------------------------------------------------------------------------- rules

def _rule_s1(st: _State) -> list[Finding]:
    out = []
    for key, row in st.inserted():
        ts, channel = row.get("ts"), row.get("channel_id")
        if _ts_key(ts) is None:
            out.append(_finding("S1", FAIL, MESSAGES, key, f"ts {ts!r} is not <10 digits>.<6 digits>"))
        elif isinstance(channel, str):
            expected = _sha(f"{channel}|{ts}".encode("utf-8"))[:32]
            if row.get("id") != expected:
                out.append(_finding("S1", FAIL, MESSAGES, key,
                                    f"id {row.get('id')!r} is not sha256('{channel}|{ts}')[:32] = {expected}"))
        if row.get("type") != "message":
            out.append(_finding("S1", FAIL, MESSAGES, key, f"type {row.get('type')!r}, expected 'message'"))
        created, instant = _iso_instant(row.get("created_at")), _ts_instant(ts)
        if created is None:
            out.append(_finding("S1", FAIL, MESSAGES, key,
                                f"created_at {row.get('created_at')!r} is not a usable timestamp"))
        elif instant is not None and abs((created - instant).total_seconds()) >= 1:
            out.append(_finding("S1", FAIL, MESSAGES, key,
                                f"created_at {row.get('created_at')!r} is not the time of ts {ts}"))
        shapes = {}
        for col, kind in (("reactions_json", list), ("files_json", list), ("attachments_json", list),
                          ("metadata_json", dict)):
            try:
                shapes[col] = json.loads(row.get(col))
            except (TypeError, ValueError):
                shapes[col] = None
            if not isinstance(shapes[col], kind):
                out.append(_finding("S1", FAIL, MESSAGES, key,
                                    f"{col} {row.get(col)!r} is not a JSON {'array' if kind is list else 'object'}"))
        if not isinstance(row.get("text"), str):
            out.append(_finding("S1", FAIL, MESSAGES, key, "text is not a string"))
        elif not row["text"] and not shapes.get("attachments_json") and not shapes.get("files_json"):
            out.append(_finding("S1", FAIL, MESSAGES, key, "empty text with no attachments or files"))
        if row.get("is_activity_message") is not False:
            out.append(_finding("S1", WARN, MESSAGES, key,
                                f"is_activity_message={row.get('is_activity_message')!r} (false on every base row)"))
    return out


def _rule_s2(st: _State) -> list[Finding]:
    out = []
    for key, row in st.inserted():
        if (row.get("channel_id"),) not in st.channels:
            out.append(_finding("S2", FAIL, MESSAGES, key, f"channel {row.get('channel_id')!r} does not exist"))
        if (row.get("user_id"),) not in st.users:
            out.append(_finding("S2", FAIL, MESSAGES, key, f"user {row.get('user_id')!r} is not a Slack user"))
    return out


def _rule_s3(st: _State) -> list[Finding]:
    out = []
    for key, row in st.inserted():
        same = [k for k, _ in st.at(row.get("channel_id"), row.get("ts")) if k != key]
        if same:
            out.append(_finding("S3", FAIL, MESSAGES, key,
                                f"(channel_id, ts) = ({row.get('channel_id')}, {row.get('ts')}) is also row {same[0]}"))
    return out


def _parent_of(st: _State, row: dict):
    pid = row.get("thread_parent_id")
    return st.messages.get((pid,)) if pid is not None else None


def _rule_s4(st: _State) -> list[Finding]:
    out = []
    for key, row in st.inserted():
        pid, legacy, ts = row.get("thread_parent_id"), row.get("thread_ts_legacy"), row.get("ts")
        if pid is None:
            if legacy is not None and legacy != ts:
                out.append(_finding("S4", FAIL, MESSAGES, key,
                                    f"thread_ts_legacy {legacy!r} names another post but thread_parent_id is NULL"))
            continue
        parent = _parent_of(st, row)
        if parent is None:
            out.append(_finding("S4", FAIL, MESSAGES, key, f"thread_parent_id {pid!r} is not an existing message"))
            continue
        if parent.get("channel_id") != row.get("channel_id"):
            out.append(_finding("S4", FAIL, MESSAGES, key,
                                f"parent {pid} is in channel {parent.get('channel_id')}, the reply in "
                                f"{row.get('channel_id')}"))
        if legacy != parent.get("ts"):
            out.append(_finding("S4", FAIL, MESSAGES, key,
                                f"thread_ts_legacy {legacy!r} is not the parent's ts {parent.get('ts')!r}"))
        mine, theirs = _ts_key(ts), _ts_key(parent.get("ts"))
        if mine is not None and theirs is not None and not theirs < mine:
            out.append(_finding("S4", FAIL, MESSAGES, key,
                                f"reply ts {ts} is not after its parent's ts {parent.get('ts')}"))
        if parent.get("thread_parent_id") is not None or parent.get("thread_ts_legacy") not in (None, parent.get("ts")):
            out.append(_finding("S4", FAIL, MESSAGES, key,
                                f"parent {pid} is itself a reply (the base has no reply to a reply)"))
        if parent.get("subtype") in (_JOIN, _LEAVE):
            out.append(_finding("S4", FAIL, MESSAGES, key, f"parent {pid} is a {parent['subtype']} row"))
        if (row.get("reply_count"), row.get("reply_users_count"), row.get("latest_reply")) != (0, 0, None):
            out.append(_finding("S4", FAIL, MESSAGES, key,
                                "a reply carries reply_count 0, reply_users_count 0 and latest_reply NULL, not "
                                f"{row.get('reply_count')!r} / {row.get('reply_users_count')!r} / "
                                f"{row.get('latest_reply')!r}"))
    return out


def _rule_s5(st: _State) -> list[Finding]:
    out = []
    parents: dict[tuple, dict] = {}
    for key, row in st.inserted():
        parent = _parent_of(st, row)
        if parent is not None:
            parents[(row.get("thread_parent_id"),)] = parent
        elif row.get("thread_parent_id") is None:
            parents[key] = row
    for key in st.overlay.updated.get(MESSAGES, ()):
        if key in st.messages:
            parents[key] = st.messages[key]
    for key, row in sorted(parents.items(), key=lambda kv: str(kv[0])):
        if row.get("thread_parent_id") is not None:
            continue                                # an updated reply: S4 covers inserted ones
        replies = st.replies(row.get("channel_id"), row.get("ts"))
        got = (row.get("reply_count"), row.get("reply_users_count"), row.get("latest_reply"))
        if not replies:
            if got != (0, 0, None) or row.get("thread_ts_legacy") not in (None, row.get("ts")):
                out.append(_finding("S5", FAIL, MESSAGES, key,
                                    f"no replies, but reply_count / reply_users_count / latest_reply = {got} and "
                                    f"thread_ts_legacy = {row.get('thread_ts_legacy')!r}"))
            elif row.get("thread_ts_legacy") is not None and st.overlay.kind(MESSAGES, key) == "insert":
                out.append(_finding("S5", FAIL, MESSAGES, key,
                                    "a new post without replies has thread_ts_legacy NULL, not its own ts"))
            continue
        keys = [k for k in (_ts_key(r.get("ts")) for r in replies) if k is not None]
        newest = max(replies, key=lambda r: _ts_key(r.get("ts")) or (0, 0)).get("ts") if keys else None
        want = (len(replies), len({r.get("user_id") for r in replies}), newest)
        if got != want:
            out.append(_finding("S5", FAIL, MESSAGES, key,
                                f"reply_count / reply_users_count / latest_reply = {got}, but its {len(replies)} "
                                f"replies give {want}"))
        if row.get("thread_ts_legacy") != row.get("ts"):
            # WARN, not FAIL: every base thread carries it and so do 13 new first posts in accepted SQL, but three
            # accepted first posts (julia_zm_difficulty_baseline: cec246a6, 6f773865, 914b21ab) were inserted with
            # thread_ts_legacy NULL and passed /injection.
            out.append(_finding("S5", WARN, MESSAGES, key,
                                f"a thread's first post carries thread_ts_legacy = its own ts {row.get('ts')}, not "
                                f"{row.get('thread_ts_legacy')!r}"))
    return out


def _rule_s6(st: _State) -> list[Finding]:
    out = []
    for key, row in st.inserted():
        if row.get("subtype") in (_JOIN, _LEAVE):
            continue
        channel, user, when = row.get("channel_id"), row.get("user_id"), _ts_key(row.get("ts"))
        if (channel,) not in st.channels or user is None or when is None:
            continue
        if not st.member_at(channel, user, when):
            out.append(_finding("S6", FAIL, MESSAGES, key,
                                f"author {user} is not a member of {_kind(st.channels[(channel,)])} channel "
                                f"{channel} at {row.get('ts')} (member list and join/leave rows)"))
    return out


def _rule_s7(st: _State) -> list[Finding]:
    out = []
    base_channels = st.base.get(CHANNELS) or {}
    for key, row in st.inserted():
        subtype = row.get("subtype")
        if subtype not in (_JOIN, _LEAVE):
            continue
        channel, user, when = row.get("channel_id"), row.get("user_id"), _ts_key(row.get("ts"))
        ch = st.channels.get((channel,))
        if ch is None or user is None or when is None:
            continue
        kind = _kind(ch)
        if subtype == _JOIN:
            place = "conversation" if kind == "mpim" else "channel"
            text = f"<@{user}> has joined the {place}"
        else:
            text = f"<@{user}> has left the channel"
        if row.get("text") != text:
            out.append(_finding("S7", FAIL if kind != "canvas" else WARN, MESSAGES, key,
                                f"text {row.get('text')!r}, the base wording in a {kind} channel is {text!r}"))
        if kind in ("im", "canvas") or (kind == "mpim" and subtype == _LEAVE):
            out.append(_finding("S7", WARN, MESSAGES, key,
                                f"a {subtype} row in a {kind} channel: the base has none"))
        if (row.get("thread_parent_id"), row.get("thread_ts_legacy"), row.get("reply_count")) != (None, None, 0):
            out.append(_finding("S7", FAIL, MESSAGES, key, "a membership row is not part of a thread"))
        events = st.events(channel, user)
        n = next((i for i, e in enumerate(events) if e[2] == key), None)
        if n is None:
            continue
        prev = events[n - 1] if n else None
        nxt = events[n + 1] if n + 1 < len(events) else None
        me = "join" if subtype == _JOIN else "leave"
        posts = [(_ts_key(r.get("ts")), k) for k, r in st.by_channel.get(channel, ())
                 if r.get("user_id") == user and r.get("subtype") not in (_JOIN, _LEAVE) and _ts_key(r.get("ts"))]
        listed_before = user in _members(base_channels.get((channel,)))
        listed_after = user in _members(ch)
        if nxt is not None and nxt[1] == me:
            out.append(_finding("S7", FAIL, MESSAGES, key,
                                f"{user} has another {me} in {channel} right after this one"))
        if me == "join":
            if prev is not None and prev[1] != "leave":
                out.append(_finding("S7", FAIL, MESSAGES, key,
                                    f"{user} joins {channel} without an earlier leave (already joined)"))
            elif prev is None:
                if listed_before or any(t < when for t, _ in posts):
                    out.append(_finding("S7", FAIL, MESSAGES, key,
                                        f"{user} joins {channel} but is already there (listed member or earlier "
                                        "posts) and never left: a join needs the user not to be a member"))
                else:
                    out.append(_finding("S7", WARN, MESSAGES, key,
                                        f"first-time join of {user} to {channel}: no accepted injection has one; "
                                        "confirm the access in the first pre-check"))
                    if not listed_after:
                        out.append(_finding("S7", FAIL, MESSAGES, key,
                                            f"{user} joins {channel} for the first time but the channel's "
                                            "members_json does not list them (every base joiner is listed)"))
        else:
            if prev is not None and prev[1] != "join":
                out.append(_finding("S7", FAIL, MESSAGES, key, f"{user} leaves {channel} twice without a join"))
            elif prev is None and not listed_before and not any(t < when for t, _ in posts):
                out.append(_finding("S7", FAIL, MESSAGES, key, f"{user} leaves {channel} but was never in it"))
            stray = [k for t, k in posts if t > when and (nxt is None or t < nxt[0])]
            if stray:
                out.append(_finding("S7", FAIL, MESSAGES, key,
                                    f"{user} has {len(stray)} post(s) in {channel} after this leave and before "
                                    "the next join"))
    return out


def _rule_s8(st: _State, freeze_utc: str) -> list[Finding]:
    out = []
    freeze = _iso_instant(freeze_utc)
    if freeze is None:
        return [_finding("S8", FAIL, MESSAGES, (), f"freeze {freeze_utc!r} is not a usable timestamp")]
    for key in st.overlay.touched(MESSAGES):
        row = st.messages.get(key)
        if row is None:
            continue
        stamps = [("ts", _ts_instant(row.get("ts"))), ("latest_reply", _ts_instant(row.get("latest_reply"))),
                  ("thread_ts_legacy", _ts_instant(row.get("thread_ts_legacy"))),
                  ("edited_ts", _ts_instant(row.get("edited_ts"))), ("created_at", _iso_instant(row.get("created_at")))]
        for col, when in stamps:
            if when is not None and not when < freeze:
                out.append(_finding("S8", FAIL, MESSAGES, key,
                                    f"{col} {row.get(col)!r} is not before the freeze {freeze_utc!r}"))
    return out


def _rule_s9(st: _State) -> list[Finding]:
    out = []
    for key, row in st.inserted():
        ch = st.channels.get((row.get("channel_id"),))
        when = _ts_key(row.get("ts"))
        if ch is None or when is None:
            continue
        born = ch.get("created_ts") or 0
        if born and when[0] < born - 1:
            out.append(_finding("S9", FAIL, MESSAGES, key,
                                f"ts {row.get('ts')} is before channel {ch.get('id')} was created ({born:.0f})"))
        if ch.get("is_archived"):
            out.append(_finding("S9", WARN, MESSAGES, key, f"posts into archived channel {ch.get('id')}"))
    return out


def _rule_s10(st: _State) -> list[Finding]:
    out = []
    for key, row in st.inserted():
        text = row.get("text") if isinstance(row.get("text"), str) else ""
        for user in _MENTION_USER.findall(text):
            if (user,) not in st.users:
                out.append(_finding("S10", FAIL, MESSAGES, key, f"text mentions <@{user}>, not a Slack user"))
        for channel in _MENTION_CHANNEL.findall(text):
            if (channel,) not in st.channels:
                out.append(_finding("S10", FAIL, MESSAGES, key, f"text links <#{channel}>, not a channel"))
    return out


def _rule_s11(st: _State) -> list[Finding]:
    out = []
    base_channels = st.base.get(CHANNELS) or {}
    for key in st.overlay.touched(CHANNELS):
        ch = st.channels.get(key)
        if ch is None:
            continue
        try:
            members = json.loads(ch.get("members_json"))
        except (TypeError, ValueError):
            members = None
        if not isinstance(members, list) or not all(isinstance(m, str) for m in members):
            out.append(_finding("S11", FAIL, CHANNELS, key, "members_json is not a JSON array of user ids"))
            continue
        if ch.get("num_members") != len(members):
            out.append(_finding("S11", FAIL, CHANNELS, key,
                                f"num_members {ch.get('num_members')!r} != {len(members)} entries in members_json"))
        if len(set(members)) != len(members):
            out.append(_finding("S11", FAIL, CHANNELS, key, "members_json lists a user twice"))
        for user in members:
            if (user,) not in st.users:
                out.append(_finding("S11", FAIL, CHANNELS, key, f"members_json lists {user!r}, not a Slack user"))
        before = _members(base_channels.get(key))
        gone = [m for m in before if m not in members]
        if gone:
            out.append(_finding("S11", WARN, CHANNELS, key,
                                f"members_json drops {gone[:3]} (the base keeps users who left in members)"))
        for user in [m for m in members if m not in before]:
            joined = any(kind == "join" for _, kind, _ in st.events(key[0], user))
            if not joined:
                out.append(_finding("S11", WARN, CHANNELS, key,
                                    f"{user} is added to members_json without a channel_join row"))
    return out


# --------------------------------------------------------------------------- entry point

def check_slack(overlay: Overlay, base: dict, *, freeze_utc: str) -> list[Finding]:
    """Run S1-S11 on the rows `overlay` inserted or updated; `base` is load_base()'s result for the same channels."""
    st = _State(overlay, base)
    findings: list[Finding] = []
    findings += _rule_s1(st)
    findings += _rule_s2(st)
    findings += _rule_s3(st)
    findings += _rule_s4(st)
    findings += _rule_s5(st)
    findings += _rule_s6(st)
    findings += _rule_s7(st)
    findings += _rule_s8(st, freeze_utc)
    findings += _rule_s9(st)
    findings += _rule_s10(st)
    findings += _rule_s11(st)
    return sorted(findings, key=lambda f: (f.rule, f.table, str(f.key), f.message))
