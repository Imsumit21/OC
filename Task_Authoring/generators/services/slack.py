"""Slack emitter: spec records -> ordered operations (messages, thread replies, DMs, membership events).

Record kinds and fields (strict: unknown fields fail; required fields have no defaults):
  slack.message            required channel user at text
                           optional parent attachments
                           A post in a base channel: public, private, canvas-comment (FC:), direct message (D...) or
                           group DM (mpdm) - they are all channels. `parent` makes it a thread reply; it is either
                             {"origin":"authored","construction":"reference","ref":"<key of another slack.message>"}  or
                             a base reference to the parent's id:  base{service slack, collection messages,
                             record "<channel id>:<ts>", field "/id"}   (a reply under an existing base post).
                           `text` may be empty only with `attachments` (an authored JSON array, e.g. a bot card).
  slack.channel_join       required channel user at     the user comes back to a channel they left (base or spec leave)
  slack.channel_leave      required channel user at     the user leaves a channel they are in
  slack.channel_first_join required channel user at     the user joins a channel they were never in: the join row plus
                                                        an UPDATE of the channel's members (unverified convention)
  slack.haystack           fields: channel, optional parent; rows: [{user, at, text, sha256}]
                           expands to slack.message records <key>.001, <key>.002, ... (services/haystack.py): user is a
                           base reference to slack users/<id>, at an authored literal, text a pinned texts/ file.

`at` is the post time, exactly YYYY-MM-DDTHH:MM:SSZ (UTC). Other records name a message by `ref: "<key>"` (its id) or
by the locator spec:<key>/ts; a base message is base:slack:messages/<channel>:<ts>/<field>.

Derived (conventions/conventions.json; each derived column records its function and convention in the provenance):
  ts                 <epoch seconds of at>.<5 digits of sha256("<channel>|<epoch>|<user>")>9      slack.message.ts
  id                 sha256("<channel>|<ts>")[:32]                                                slack.message.id
  created_at         the ts instant, YYYY-MM-DDTHH:MM:SS.ffffffZ                                  slack.message.created_at
  type 'message', is_activity_message false, subtype NULL, reactions_json '[]', files_json '[]',
  attachments_json '[]' unless authored, metadata_json '{}'; edited_ts, edited_user, bot_id,
  client_msg_id and permalink are not written                                                     slack.message.shape
  reply              thread_parent_id = the parent's id, thread_ts_legacy = the parent's ts,
                     reply_count 0, reply_users_count 0, latest_reply NULL                        slack.thread_parent_id
  new thread parent  thread_ts_legacy = its own ts, reply_count / reply_users_count / latest_reply
                     from its spec replies; a post without replies: NULL, 0, 0, NULL              slack.thread.counters
  base thread parent UPDATE ... SET thread_ts_legacy = its ts, reply_count = base count + new replies,
                     reply_users_count = distinct repliers (base and new), latest_reply = newest
                     reply (base or new)                                                          slack.thread.counters
  membership row     subtype channel_join / channel_leave, text "<@user> has joined the channel"
                     ("... the conversation" in a group DM) / "<@user> has left the channel"       slack.membership.event
  first join         also UPDATE slack_channels SET num_members, members_json (user appended)     slack.membership.first_join

Refused here, with the record key (the independent checks are validate/slack.py S1-S11): an unknown channel or user;
two posts with the same (channel, ts); a reply whose parent is in another channel, is itself a reply, is a membership
row or is not earlier; a base parent the export gives no id, or whose stored reply_count differs from its reply rows;
an author who is not a member of the channel at that time; a join without an earlier leave, a leave by a non-member,
posts between a leave and the next join; membership rows in a DM or a canvas-comment channel; text ending in a line
break; a <@user> or <#channel> mention that does not exist.

Statement order (no platform meaning inside one transaction; a parent always precedes its replies): first-join
channel updates by channel id; message inserts by (channel id, ts); base-parent updates by (channel id, parent ts).
"""
from __future__ import annotations

import datetime as dt
import hashlib
import re

from ..core.ops import INSERT, UPDATE, Op
from ..core.sqlvalue import json_text
from ..core.values import SpecError
from . import haystack

SERVICE = "slack"
VERSION = "slack/1.0"

_EVENT = {"required": {"channel", "user", "at"}, "optional": set()}
KINDS = {
    "slack.message": {"required": {"channel", "user", "at", "text"}, "optional": {"parent", "attachments"}},
    "slack.channel_join": _EVENT,
    "slack.channel_leave": _EVENT,
    "slack.channel_first_join": _EVENT,
}
HAYSTACKS = {"slack.haystack": "slack.message"}

# convention id -> record kinds that rely on it (empty tuple: every Slack render)
CONVENTIONS = {
    "sql.literal_policy": (),
    "sql.json_text": (),
    "slack.message.id": (),
    "slack.message.ts": (),
    "slack.message.created_at": (),
    "slack.message.shape": (),
    "slack.thread_parent_id": ("slack.message",),
    "slack.thread.counters": ("slack.message",),
    "slack.membership.event": ("slack.channel_join", "slack.channel_leave", "slack.channel_first_join"),
    "slack.membership.first_join": ("slack.channel_first_join",),
}

AT_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
AT_TEXT = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$")     # ASCII digits only
TS_TEXT = re.compile(r"^([0-9]{10})\.([0-9]{6})$")
TS_LAST_DIGIT = "9"
ID_LENGTH = 32
MESSAGE_TYPE = "message"
EMPTY_LIST_JSON = "[]"
EMPTY_OBJECT_JSON = "{}"
JOIN, LEAVE = "channel_join", "channel_leave"
JOIN_TEXT = "<@{user}> has joined the {place}"
LEAVE_TEXT = "<@{user}> has left the channel"
MESSAGE_COLUMNS = ("id", "ts", "channel_id", "type", "user_id", "text", "thread_parent_id", "thread_ts_legacy",
                   "reply_count", "reply_users_count", "latest_reply", "is_activity_message", "subtype",
                   "reactions_json", "files_json", "attachments_json", "created_at", "metadata_json")
PARENT_UPDATE_COLUMNS = ("thread_ts_legacy", "reply_count", "reply_users_count", "latest_reply")
_MENTION_USER = re.compile(r"<@([A-Z0-9_]+)(?:\|[^>]*)?>")
_MENTION_CHANNEL = re.compile(r"<#([A-Z0-9]+)(?:\|[^>]*)?>")
_EVENT_KINDS = {"slack.channel_join": "join", "slack.channel_first_join": "join", "slack.channel_leave": "leave"}
# where a membership row may be written: the channel kinds in which the base, or SQL the platform accepted, has one
_EVENT_PLACES = {"join": ("public", "private", "mpim"), "leave": ("public", "private")}


# ---------------------------------------------------------------- derived values (also used by the tests)

def epoch_of(at, where: str) -> int:
    try:
        if not AT_TEXT.match(at):
            raise ValueError(at)
        when = dt.datetime.strptime(at, AT_FORMAT).replace(tzinfo=dt.timezone.utc)
    except (TypeError, ValueError):
        raise SpecError(where, f"time {at!r} is not YYYY-MM-DDTHH:MM:SSZ") from None
    return int(when.timestamp())


def ts_for(channel: str, epoch: int, user: str) -> str:
    """slack.ts/1: the second the spec gives, plus six decimals fixed by (channel, second, user); the last is 9."""
    digest = hashlib.sha256(f"{channel}|{epoch}|{user}".encode("utf-8")).hexdigest()
    return f"{epoch:010d}.{int(digest[:8], 16) % 100000:05d}{TS_LAST_DIGIT}"


def message_id(channel: str, ts: str) -> str:
    """slack.message_id/1"""
    return hashlib.sha256(f"{channel}|{ts}".encode("utf-8")).hexdigest()[:ID_LENGTH]


def created_at_for(ts: str) -> str:
    """slack.created_at/1: the ts instant as a timestamp with microseconds."""
    m = TS_TEXT.match(ts)
    when = dt.datetime.fromtimestamp(int(m.group(1)), dt.timezone.utc)
    return f"{when:%Y-%m-%dT%H:%M:%S}.{m.group(2)}Z"


def ts_key(ts) -> tuple:
    m = TS_TEXT.match(ts) if isinstance(ts, str) else None
    if not m:
        raise ValueError(f"not a Slack ts: {ts!r}")
    return int(m.group(1)), int(m.group(2))


def channel_kind(row: dict) -> str:
    if row.get("is_im"):
        return "im"
    if row.get("is_mpim"):
        return "mpim"
    if str(row.get("name") or "").startswith("FC:"):
        return "canvas"
    return "private" if row.get("is_private") else "public"


def member_at(events: list, listed: bool, when: tuple) -> bool:
    """Is the user in the channel at `when`? events: the user's (ts key, 'join' | 'leave') rows in that channel, sorted.
    The last row before `when` decides; before any row, the first row after it does (a user is in the channel until
    they leave it, and not in it before they join); with no rows at all, the channel's member list does."""
    before = [kind for key, kind in events if key < when]
    if before:
        return before[-1] == "join"
    after = [kind for key, kind in events if key > when]
    if after:
        return after[0] == "leave"
    return listed


TRANSFORMS = {}


def _derived(fn: str, convention: str, inputs=()) -> dict:
    p = {"origin": "derived", "construction": "transform", "fn": fn, "convention": convention}
    if inputs:
        p["inputs"] = list(inputs)
    return p


def _default(value, convention: str) -> dict:
    return {"origin": "default", "construction": "default", "value": value, "convention": convention}


# ---------------------------------------------------------------- haystack

def expand_haystack(where: str, rec: dict) -> list[dict]:
    def build(row):
        return {"user": haystack.base_ref("slack", "users", row["user"], "/id"),
                "at": haystack.literal(row["at"]),
                "text": haystack.text_file(row["text"], row["sha256"])}
    return haystack.expand(where, rec, kind=HAYSTACKS[rec["kind"]], shared_required={"channel"},
                           shared_optional={"parent"}, row_required={"user", "at", "text", "sha256"},
                           row_optional=set(), build=build)


# ---------------------------------------------------------------- base view

class _Channel:
    """One base channel: its row and, read once when needed, every message of every monthly shard."""

    def __init__(self, base, cid: str, row: dict):
        self.base, self.id, self.row = base, cid, row
        self.kind = channel_kind(row)
        self.members = [m for m in (row.get("members") or []) if isinstance(m, str)]
        self._rows = None
        self._by_ts = None
        self._events: dict[str, list] = {}
        self._posts: dict[str, list] = {}

    def rows(self) -> list:
        if self._rows is None:
            rows = []
            for rel in self.base.paths_under("slack", f"messages/{self.id}/"):
                shard = self.base.file("slack", rel)
                if not isinstance(shard, list):
                    raise SpecError(f"base.slack.{rel}", "a message shard must be a JSON list")
                rows += [m for m in shard if isinstance(m, dict) and TS_TEXT.match(str(m.get("ts") or ""))]
            self._rows = rows
            self._by_ts = {m["ts"]: m for m in rows}
        return self._rows

    def by_ts(self) -> dict:
        self.rows()
        return self._by_ts

    def events(self, user: str) -> list:
        """The user's base join and leave rows here: sorted (ts key, 'join' | 'leave')."""
        if user not in self._events:
            self._events[user] = sorted(
                (ts_key(m["ts"]), "join" if m.get("subtype") == JOIN else "leave") for m in self.rows()
                if m.get("user") == user and m.get("subtype") in (JOIN, LEAVE))
        return self._events[user]

    def posts(self, user: str) -> list:
        """The ts keys of the user's base posts here (membership rows left out), sorted."""
        if user not in self._posts:
            self._posts[user] = sorted(ts_key(m["ts"]) for m in self.rows()
                                       if m.get("user") == user and m.get("subtype") not in (JOIN, LEAVE))
        return self._posts[user]

    def replies(self, parent_ts: str) -> list:
        return [m for m in self.rows() if m.get("thread_ts") == parent_ts and m["ts"] != parent_ts]


def _json_col(value, where: str) -> str:
    if not isinstance(value, list):
        raise SpecError(where, "must be a JSON array")
    try:
        return json_text(value)
    except (TypeError, ValueError) as exc:
        raise SpecError(where, f"cannot serialize as JSON: {exc}") from None


# ---------------------------------------------------------------- expand

def expand(records: list, resolver, base) -> list[Op]:
    """records: spec records of this service ({key, kind, fields}); resolver(record, field) -> (value, provenance)."""
    users = base.records("slack", "users")
    channels = base.records("slack", "channels")
    views: dict[str, _Channel] = {}

    def view(cid: str) -> _Channel:
        if cid not in views:
            views[cid] = _Channel(base, cid, channels[cid])
        return views[cid]

    # ---- every record: channel, user, time -> ts and id (registered so other records can name them)
    items, by_id = [], {}
    for rec in records:
        k = rec["key"]
        cid, p_channel = resolver(rec, "channel")
        if not isinstance(cid, str) or cid not in channels:
            raise SpecError(f"{k}.channel", f"channel {cid!r} is not in the pinned base")
        uid, p_user = resolver(rec, "user")
        if not isinstance(uid, str) or uid not in users:
            raise SpecError(f"{k}.user", f"user {uid!r} is not in the pinned base")
        at, p_at = resolver(rec, "at")
        epoch = epoch_of(at, f"{k}.at")
        ts = ts_for(cid, epoch, uid)
        mid = message_id(cid, ts)
        p_ts = _derived("slack.ts/1", "slack.message.ts", ["at", "channel_id", "user_id"])
        p_id = _derived("slack.message_id/1", "slack.message.id", ["channel_id", "ts"])
        resolver.derive(rec, "ts", ts, dict(p_ts, of=p_at))
        resolver.derive(rec, "id", mid, p_id)
        item = {"rec": rec, "key": k, "kind": rec["kind"], "channel": cid, "user": uid, "ts": ts, "id": mid,
                "when": ts_key(ts), "event": _EVENT_KINDS.get(rec["kind"]), "place": view(cid).kind,
                "prov": {"channel_id": p_channel, "user_id": p_user, "ts": p_ts, "id": p_id}}
        other = by_id.get(mid)
        if other is not None:
            raise SpecError(f"{k}.at", f"{other['key']} and {k} get the same ts {ts} in {cid} (same second, same "
                                       "user, or a collision of the derived decimals); move one by a second")
        if ts in view(cid).by_ts():
            raise SpecError(f"{k}.at", f"{cid} already has a base message at ts {ts}; move this one by a second")
        by_id[mid] = item
        items.append(item)

    # ---- membership rows: the user's history in the channel must alternate join / leave
    timelines: dict[tuple, list] = {}
    for item in items:
        if item["event"]:
            timelines.setdefault((item["channel"], item["user"]), []).append(item)

    def events_of(cid: str, uid: str) -> list:
        """(ts key, 'join' | 'leave', spec item or None) for base and spec rows of one user in one channel."""
        merged = [(key, kind, None) for key, kind in view(cid).events(uid)]
        merged += [(i["when"], i["event"], i) for i in timelines.get((cid, uid), [])]
        return sorted(merged, key=lambda e: e[0])

    first_joins: dict[str, list] = {}
    for (cid, uid), _ in sorted(timelines.items()):
        ch = view(cid)
        merged = events_of(cid, uid)
        listed = uid in ch.members
        posts = ch.posts(uid)
        for n, (when, kind, item) in enumerate(merged):
            if item is None:
                continue
            k = item["key"]
            if ch.kind not in _EVENT_PLACES[kind]:
                why = {"im": "a direct message has no join or leave rows",
                       "canvas": "no base canvas-comment (FC:) channel has join or leave rows; the one accepted "
                                 "injection that wrote them there got a reviewer advisory",
                       "mpim": "no base group DM has a leave row"}[ch.kind]
                raise SpecError(f"{k}.channel", f"{item['kind']} in {ch.kind} channel {cid}: {why}")
            prev = merged[n - 1] if n else None
            nxt = merged[n + 1] if n + 1 < len(merged) else None
            if nxt is not None and nxt[1] == kind:
                raise SpecError(k, f"{uid} has another {kind} in {cid} right after this one (no "
                                   f"{'leave' if kind == 'join' else 'join'} in between)")
            if item["kind"] == "slack.channel_join":
                if prev is None or prev[1] != "leave":
                    raise SpecError(k, f"{uid} has no earlier channel_leave in {cid}: a join needs the user not to "
                                       "be a member (platform /injection FAIL C1 on a join without a leave). A "
                                       "first-time join is kind slack.channel_first_join")
            elif item["kind"] == "slack.channel_first_join":
                if prev is not None or listed or any(p < when for p in posts):
                    raise SpecError(k, f"{uid} is already in {cid} (listed member, earlier join or leave, or earlier "
                                       "posts): a first join needs a user who was never there; after a leave use "
                                       "slack.channel_join")
                first_joins.setdefault(cid, []).append(item)
            else:                                   # leave
                if prev is not None and prev[1] != "join":
                    raise SpecError(k, f"{uid} already left {cid} before this leave")
                if prev is None and not listed and not any(p < when for p in posts):
                    raise SpecError(k, f"{uid} is not in {cid}: nothing to leave")
            if kind == "leave":
                stray = [p for p in posts if p > when and (nxt is None or p < nxt[0])]
                if stray:
                    raise SpecError(k, f"{uid} has {len(stray)} base post(s) in {cid} after this leave and before "
                                       "the next join")

    # ---- messages: author is a member at that time; parents; text
    replies_spec: dict[str, list] = {}          # spec parent id -> its spec replies
    replies_base: dict[tuple, list] = {}        # (channel, base parent ts) -> spec replies
    for item in items:
        rec, k, cid, uid = item["rec"], item["key"], item["channel"], item["user"]
        ch = view(cid)
        if item["event"]:
            continue
        timeline = [(key, kind) for key, kind, _ in events_of(cid, uid)]
        if not member_at(timeline, uid in ch.members, item["when"]):
            raise SpecError(f"{k}.user", f"{uid} is not a member of {ch.kind} channel {cid} at {item['ts']} (member "
                                         "list and join/leave rows, base and spec)")
        text, item["prov"]["text"] = resolver(rec, "text")
        if not isinstance(text, str):
            raise SpecError(f"{k}.text", "must be text")
        if text.endswith(("\n", "\r")):
            raise SpecError(f"{k}.text", "ends with a line break (99% of base messages do not); remove the trailing "
                                         "newline from the text")
        for mention in _MENTION_USER.findall(text):
            if mention not in users:
                raise SpecError(f"{k}.text", f"mentions <@{mention}>, which is not a Slack user in the pinned base")
        for mention in _MENTION_CHANNEL.findall(text):
            if mention not in channels:
                raise SpecError(f"{k}.text", f"links <#{mention}>, which is not a channel in the pinned base")
        item["text"] = text
        if "attachments" in rec["fields"]:
            attachments, item["prov"]["attachments_json"] = resolver(rec, "attachments")
            item["attachments"] = _json_col(attachments, f"{k}.attachments")
        else:
            item["attachments"] = EMPTY_LIST_JSON
            item["prov"]["attachments_json"] = _default(EMPTY_LIST_JSON, "slack.message.shape")
        if not text and item["attachments"] == EMPTY_LIST_JSON:
            raise SpecError(f"{k}.text", "an empty message needs attachments")
        item["parent"] = None
        if "parent" in rec["fields"]:
            pid, p_parent = resolver(rec, "parent")
            item["prov"]["thread_parent_id"] = p_parent
            if pid is not None:
                item["parent"] = _parent(item, pid, p_parent, by_id, view)

    for item in items:
        parent = item.get("parent")
        if parent is None:
            continue
        if parent["spec"] is not None:
            replies_spec.setdefault(parent["id"], []).append(item)
        else:
            replies_base.setdefault((item["channel"], parent["ts"]), []).append(item)
    for item in items:                           # a reply cannot be a parent (0 replies of replies in the base)
        if item.get("parent") is not None and item["id"] in replies_spec:
            raise SpecError(f"{replies_spec[item['id']][0]['key']}.parent",
                            f"{item['key']} is itself a reply; reply to the thread's first post")

    # ---- operations
    channel_ops = []
    for cid in sorted(first_joins):
        ch = view(cid)
        joiners = [i["user"] for i in sorted(first_joins[cid], key=lambda i: i["when"])]
        members = ch.members + joiners
        p = _derived("slack.members_after_join/1", "slack.membership.first_join", ["members", "first joins"])
        channel_ops.append(Op("slack.slack_channels", UPDATE,
                              (("num_members", len(members)), ("members_json", json_text(members))),
                              where=(("id", cid),), record=None, prov=(("num_members", p), ("members_json", p))))

    message_ops = []
    for item in sorted(items, key=lambda i: (i["channel"], i["when"])):
        row, prov = _row(item, replies_spec.get(item["id"], []))
        message_ops.append(Op("slack.slack_messages", INSERT, tuple((c, row[c]) for c in MESSAGE_COLUMNS),
                              record=item["key"], prov=tuple((c, prov[c]) for c in MESSAGE_COLUMNS)))

    parent_ops = []
    for (cid, pts), new in sorted(replies_base.items(), key=lambda kv: (kv[0][0], ts_key(kv[0][1]))):
        ch = view(cid)
        parent = ch.by_ts()[pts]
        old = ch.replies(pts)
        stored = parent.get("reply_count") or 0
        if stored != len(old):
            raise SpecError(f"{new[0]['key']}.parent", f"base parent {cid}:{pts} stores reply_count {stored} but the "
                                                       f"export holds {len(old)} replies to it; pick another parent")
        repliers = {m.get("user") for m in old} | {i["user"] for i in new}
        newest = max([m["ts"] for m in old] + [i["ts"] for i in new], key=ts_key)
        p = _derived("slack.thread_counters/1", "slack.thread.counters", ["base replies", "spec replies"])
        values = {"thread_ts_legacy": pts, "reply_count": stored + len(new), "reply_users_count": len(repliers),
                  "latest_reply": newest}
        parent_ops.append(Op("slack.slack_messages", UPDATE, tuple((c, values[c]) for c in PARENT_UPDATE_COLUMNS),
                             where=(("id", parent["id"]),), record=None,
                             prov=tuple((c, p) for c in PARENT_UPDATE_COLUMNS)))
    return channel_ops + message_ops + parent_ops


def _parent(item: dict, pid, p_parent: dict, by_id: dict, view) -> dict:
    """The parent of a reply: {"id", "ts", "spec": item or None}; refused unless it is an earlier first post of a
    thread (or a post without one) in the same channel."""
    k, cid = item["key"], item["channel"]
    where = f"{k}.parent"
    spec = by_id.get(pid) if isinstance(pid, str) else None
    if spec is not None:
        if spec["event"]:
            raise SpecError(where, f"{spec['key']} is a membership row, not a message")
        if spec["channel"] != cid:
            raise SpecError(where, f"parent {spec['key']} is in {spec['channel']}, the reply in {cid}")
        if not spec["when"] < item["when"]:
            raise SpecError(where, f"parent {spec['key']} ({spec['ts']}) is not earlier than the reply ({item['ts']})")
        return {"id": spec["id"], "ts": spec["ts"], "spec": spec}
    cited = p_parent.get("base") if p_parent.get("origin") == "base" else None
    if not cited or (cited.get("service"), cited.get("collection"), cited.get("field")) != ("slack", "messages", "/id"):
        raise SpecError(where, "a parent is ref: <key of a spec slack.message> or a base reference to slack "
                               "messages/<channel>:<ts> field /id")
    pch, _, pts = cited["record"].partition(":")
    if pch != cid:
        raise SpecError(where, f"parent {cited['record']} is in {pch}, the reply in {cid}")
    row = view(cid).by_ts().get(pts)
    if row is None or row.get("id") != pid:
        raise SpecError(where, f"base message {cited['record']} not found with id {pid!r}")
    if row.get("thread_ts") not in (None, pts):
        raise SpecError(where, f"base message {cited['record']} is itself a reply (to {row.get('thread_ts')}); "
                               "reply to the thread's first post")
    if row.get("subtype") in (JOIN, LEAVE):
        raise SpecError(where, f"base message {cited['record']} is a {row['subtype']} row (no base thread hangs "
                               "under one)")
    if not ts_key(pts) < item["when"]:
        raise SpecError(where, f"parent {cited['record']} is not earlier than the reply ({item['ts']})")
    return {"id": pid, "ts": pts, "spec": None}


def _row(item: dict, replies: list) -> tuple[dict, dict]:
    shape = "slack.message.shape"
    prov = dict(item["prov"])
    row = {"id": item["id"], "ts": item["ts"], "channel_id": item["channel"], "type": MESSAGE_TYPE,
           "user_id": item["user"], "is_activity_message": False, "reactions_json": EMPTY_LIST_JSON,
           "files_json": EMPTY_LIST_JSON, "metadata_json": EMPTY_OBJECT_JSON,
           "created_at": created_at_for(item["ts"])}
    for col in ("type", "is_activity_message", "reactions_json", "files_json", "metadata_json"):
        prov[col] = _derived("slack.message_defaults/1", shape)
    prov["created_at"] = _derived("slack.created_at/1", "slack.message.created_at", ["ts"])
    counters = _derived("slack.thread_counters/1", "slack.thread.counters", ["spec replies"])
    if item["event"]:
        place = "conversation" if item["place"] == "mpim" else "channel"
        row["subtype"] = JOIN if item["event"] == "join" else LEAVE
        row["text"] = (JOIN_TEXT.format(user=item["user"], place=place) if item["event"] == "join"
                       else LEAVE_TEXT.format(user=item["user"]))
        row["attachments_json"] = EMPTY_LIST_JSON
        event = _derived("slack.membership_row/1", "slack.membership.event", ["user_id", "channel kind"])
        prov.update(subtype=event, text=event, attachments_json=_derived("slack.message_defaults/1", shape))
        row.update(thread_parent_id=None, thread_ts_legacy=None, reply_count=0, reply_users_count=0,
                   latest_reply=None)
        for col in ("thread_parent_id", "thread_ts_legacy", "reply_count", "reply_users_count", "latest_reply"):
            prov[col] = event
        return row, prov
    row["subtype"] = None
    prov["subtype"] = _derived("slack.message_defaults/1", shape)
    row["text"] = item["text"]
    row["attachments_json"] = item["attachments"]
    parent = item["parent"]
    if parent is not None:
        reply = _derived("slack.reply/1", "slack.thread_parent_id", ["parent"])
        row.update(thread_parent_id=parent["id"], thread_ts_legacy=parent["ts"], reply_count=0, reply_users_count=0,
                   latest_reply=None)
        for col in ("thread_ts_legacy", "reply_count", "reply_users_count", "latest_reply"):
            prov[col] = reply
    else:
        row["thread_parent_id"] = None
        prov["thread_parent_id"] = prov.get("thread_parent_id") or _default(None, "slack.thread_parent_id")
        if replies:
            row.update(thread_ts_legacy=item["ts"], reply_count=len(replies),
                       reply_users_count=len({r["user"] for r in replies}),
                       latest_reply=max((r["ts"] for r in replies), key=ts_key))
        else:
            row.update(thread_ts_legacy=None, reply_count=0, reply_users_count=0, latest_reply=None)
        for col in ("thread_ts_legacy", "reply_count", "reply_users_count", "latest_reply"):
            prov[col] = counters
    return row, prov


def key_of(op: Op) -> tuple:
    if op.op == UPDATE:
        return tuple(v for _, v in op.where)
    return (op.col("id"),)
