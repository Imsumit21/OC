"""Gmail: load base rows (DB-shaped) for the threads an op list touches, and invariants G1-G12 for a proposed overlay.

Independent of the emitter: nothing here imports generators/services, generators/core/gmail_index.py,
tools/sql_lint.py or tools/base_check.py. The rules come from their written sources and from the base export itself:
- Task_Authoring/references/universe_schema_live.json and universe_constraints_live.json (gmail_messages: PRIMARY KEY
  id, thread_id REFERENCES gmail_threads(id), user_email REFERENCES gmail_users(email_address))
- Evals/0_Injection_Quality_Eval.md Check A (references, ids, history_id NULL or decimal) and Check C (replies follow
  parents, event times before the clock)
- the platform's /injection reviews of accepted SQL: support/completed_tasks/frederick_q4_commitments_2026-11-05/
  eval_reports/0_injection_PASS_r1.md:64 and frederick_bridge_pipeline_2026-11-03/eval_reports/0_injection_PASS_r7.md:38
  (internal_date = date; headers match the columns; snippet = body start; sender copies SENT, recipient copies INBOX;
  a reply's parent in the same thread and earlier; a thread's snippet = its newest message's; copies of one
  Message-ID agree; thread number >> 20 = the first message's internal_date), julia_zm3d_beta_calendar_2026-11-07/
  eval_reports/0_injection_FAIL_r1.md A2/A3 (a reply in another thread; a snippet that is not the body start)
- the base export: id = <mailbox>/<RFC Message-ID>; thread id = <mailbox>/<19 digits>, one number per mailbox; the
  thread number >> 20 within an hour of its first message; display names per address.

The export keeps the API shape (labelIds, from, to, cc, date as ISO or RFC 2822, headers); load_base maps the threads
the statements touch onto the live columns. Columns the export does not hold (snippet, size_estimate, body_html,
history_id) are None on base rows; a base thread's snippet is unknown.

Rules (FAIL blocks publication, WARN is recorded):
  G1  row shape of an inserted message: id and thread_id schemes, internal_date = date, JSON columns, history_id
  G2  mailbox, thread (same mailbox) and labels exist
  G3  an inserted message id or thread id is new (WARN: a new copy of a Message-ID base holds in other mailboxes)
  G4  copies: every participant mailbox (from, to, cc, bcc that is a base mailbox) holds a copy; no copy in a mailbox
      that is not a participant; copies of one Message-ID agree. A Google Calendar invitation (<calendar-...@google.com>)
      is one message per invitee in base, so its To list is not a copy list (3,828 of 7,497 normal invitations).
  G5  labels: the sender's copy is SENT; a recipient's copy is not SENT (WARN: neither INBOX nor ARCHIVED)
  G6  a reply: its parent exists and is earlier; in a mailbox holding the parent, a reply with the parent's subject
      (Re:/Fwd: prefixes aside) is in the parent's thread (base: 8,638 of 8,642; a changed subject may open a thread,
      103 of 996) (WARN: References does not end with In-Reply-To; a subject without Re:)
  G7  no date at or after the freeze (WARN: a new thread's number >> 20 is not within an hour after its first message)
  G8  thread snippets (WARN): a new thread's snippet is its newest message's; an updated base thread's newest message
      is the injected one whose snippet it takes; a base thread whose newest message is now injected gets its snippet
  G9  snippet is the start of the body with white space collapsed
  G10 headers_json agrees with the columns: Message-ID, Date, Subject, From, To, X-GM-THRID (WARN: Cc, In-Reply-To,
      References disagreeing with or missing from the columns; one of Message-ID, Date, Subject, From, To missing)
  G11 address forms: an address written in a spelling base never uses for it (case, token); WARN: a display name base
      never uses for the address, a harmonygames.co address base never shows
  G12 body line breaks (WARN): a bare LF where base writes CRLF

FAIL is kept for what the brief (PLAN.md WS9 3e) requires, what breaks the database, and what the platform failed.
Rules the platform passed in accepted SQL are WARN: G7's thread number (owen_dd_bug_carryover, 3 invitation threads
~10 h late), G8 (frederick_card_spend_q3 kept an older snippet), G10's Cc / In-Reply-To / References
(samuel_zm_beta_messages), G11's display names (39 'Leonard Hayes' rows across tasks).
"""
from __future__ import annotations

import datetime as dt
import email.utils
import hashlib
import json
import os
import re
from pathlib import Path

from generators.validate.invariants import FAIL, WARN, Finding
from generators.validate.overlay import Overlay

MESSAGES = "gmail.gmail_messages"
THREADS = "gmail.gmail_threads"
USERS = "gmail.gmail_users"
LABELS = "gmail.gmail_labels"
MANIFEST = "source_manifest.json"
INTERNAL = "@harmonygames.co"
_RFC = re.compile(r"^<[^<>\s]+@[^<>\s]+>$")
_MID = re.compile(r"^([^/]+)/(<[^<>]+>)$")
_TID = re.compile(r"^([^/]+)/([0-9]{15,20})$")
_ISO = re.compile(r"^(\d{4})-(\d{2})-(\d{2})[T ](\d{2}):(\d{2}):(\d{2})(?:\.(\d{1,6}))?(Z|[+-]\d{2}(?::?\d{2})?)?$",
                  re.ASCII)
_PAIR = re.compile(rb'"(id|user_email|from|to|cc|bcc)":\s*"((?:[^"\\]|\\.)*)"')
_HOUR_MS = 3600 * 1000
_INVITE = "<calendar-"
_PREFIX = re.compile(r"^\s*(re|fwd?|aw)\s*:\s*", re.I)
_SCANS: dict[tuple, tuple] = {}                 # (root, manifest sha) -> (stat signature, facts)


class GmailBaseError(Exception):
    """The Gmail export is not the pinned one, or a file of it cannot be used."""


# --------------------------------------------------------------------------- small helpers

def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _jt(value) -> str:
    return json.dumps(value, ensure_ascii=False)


def _instant(value) -> dt.datetime | None:
    """A UTC instant from ISO-8601 (any offset) or RFC 2822 text."""
    if not isinstance(value, str) or not value.strip():
        return None
    m = _ISO.match(value.strip())
    if m:
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
    try:
        when = email.utils.parsedate_to_datetime(value)
    except (TypeError, ValueError, IndexError):
        return None
    if when is None:
        return None
    return when if when.tzinfo else when.replace(tzinfo=dt.timezone.utc)


def _split(text: str) -> list[str]:
    """Entries of a From/To/Cc string: commas outside quotes and angle brackets separate them."""
    parts, cur, quoted, angle = [], [], False, False
    for ch in text or "":
        if ch == '"' and not angle:
            quoted = not quoted
        elif ch == "<" and not quoted:
            angle = True
        elif ch == ">" and not quoted:
            angle = False
        if ch == "," and not quoted and not angle:
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    parts.append("".join(cur))
    return [p.strip() for p in parts if p.strip()]


def _addresses(text) -> list[tuple[str, str]]:
    """(display name, address) per entry; the address is what stands in <...>, else the whole entry. Anonymised
    exports write tokens such as [EMAIL_0801] or SVC_0325_EMAIL where an address would be, which email.utils drops."""
    out = []
    for part in _split(text if isinstance(text, str) else ""):
        if "<" in part and part.rstrip().endswith(">"):
            addr = part[part.rfind("<") + 1:part.rstrip().rfind(">")].strip()
            name = part[:part.rfind("<")].strip().strip('"').strip()
        else:
            addr, name = part.strip().strip('"'), ""
        if addr:
            out.append((name, addr))
    return out


def _json_list(value) -> list | None:
    try:
        parsed = json.loads(value) if isinstance(value, str) else None
    except ValueError:
        return None
    return parsed if isinstance(parsed, list) else None


def _entries_of(column) -> list[tuple[str, str]]:
    """(name, address) of every entry of a to_json / cc_json / bcc_json column."""
    out = []
    for entry in _json_list(column) or []:
        if isinstance(entry, str):
            out += _addresses(entry)
    return out


def _topic(subject) -> str:
    """A subject without its Re:/Fwd: prefixes, case and outer space."""
    s = str(subject or "")
    while True:
        t = _PREFIX.sub("", s)
        if t == s:
            return s.strip().lower()
        s = t


def _collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


# --------------------------------------------------------------------------- loading

class Facts:
    """What the whole export says, from one pass over every thread file."""

    def __init__(self):
        self.thread_files: dict[str, str] = {}          # thread id -> export file
        self.copies: dict[str, set] = {}                # RFC id -> {(mailbox lower, thread id)}
        self.names: dict[str, set] = {}                 # address lower -> display names ('' = bare)
        self.spellings: dict[str, set] = {}             # address lower -> the address as base writes it
        self.mailboxes: dict[str, str] = {}             # mailbox lower -> as written in users.json
        self.labels: dict[str, str] = {}                # label id -> name


def _scan(root: Path, listed: dict) -> Facts:
    rels = sorted(p for p in listed if p.startswith("threads/"))
    h = hashlib.sha256()
    for rel in rels:
        st = os.stat(root / rel)
        h.update(f"{rel}|{st.st_size}|{st.st_mtime_ns}|{st.st_ino}\n".encode("utf-8"))
    key = (str(root.resolve()), _sha("".join(f"{r}{listed[r]}" for r in rels).encode("utf-8")))
    cached = _SCANS.get(key)
    if cached is not None and cached[0] == h.hexdigest():
        return cached[1]
    facts = Facts()
    raw_entries = set()
    for rel in rels:
        data = (root / rel).read_bytes()
        if _sha(data) != listed[rel]:
            raise GmailBaseError(f"{rel}: sha256 {_sha(data)} differs from {MANIFEST} ({listed[rel]})")
        thread = None
        for name, raw in _PAIR.findall(data):
            if name == b"id":
                value = json.loads(b'"' + raw + b'"')
                if thread is None:
                    thread = value
                    facts.thread_files[thread] = rel
                else:
                    box, _, rfc = value.partition("/")
                    facts.copies.setdefault(rfc, set()).add((box.lower(), thread))
            elif name != b"user_email":
                raw_entries.add(raw)
    for raw in raw_entries:
        for name, addr in _addresses(json.loads(b'"' + raw + b'"')):
            facts.names.setdefault(addr.lower(), set()).add(name)
            facts.spellings.setdefault(addr.lower(), set()).add(addr)
    _SCANS[key] = (h.hexdigest(), facts)
    return facts


def _from_parts(text: str) -> tuple[str | None, str | None]:
    found = _addresses(text)
    if not found:
        return None, (text or None)
    name, addr = found[0]
    return addr, (name or None)


def _entry_list(text: str) -> str:
    return _jt([f"{n} <{a}>" if n else a for n, a in _addresses(text)])


def _message_row(thread: dict, item: dict) -> tuple[tuple, dict]:
    when = _instant(item.get("date_parsed")) or _instant(item.get("date"))
    ms = item.get("internal_date_ms")
    from_email, from_name = _from_parts(item.get("from") or "")
    row = {
        "id": item.get("id"), "thread_id": thread.get("id"), "user_email": thread.get("user_email"),
        "label_ids_json": _jt(item.get("labelIds") or []), "snippet": None, "history_id": None,
        "internal_date": int(ms) if isinstance(ms, (int, str)) and str(ms).isdigit()
        else (int(when.timestamp() * 1000) if when else None),
        "date": when.strftime("%Y-%m-%dT%H:%M:%SZ") if when else None, "size_estimate": None,
        "subject": item.get("subject"), "from_email": from_email, "from_name": from_name,
        "to_json": _entry_list(item.get("to")), "cc_json": _entry_list(item.get("cc")),
        "bcc_json": _entry_list(item.get("bcc")), "reply_to_json": _entry_list(item.get("reply_to")),
        "body_text": item.get("body"), "body_html": None, "headers_json": _jt(item.get("headers") or []),
        "in_reply_to": item.get("in_reply_to") or "", "references": item.get("references") or "",
        "mbox_from": item.get("mbox_from"), "attachments_meta_json": _jt(item.get("attachments") or []),
    }
    return (row["id"],), row


def wanted(ops) -> tuple[set, set]:
    """Thread ids the statements name, and RFC ids they insert, update or answer (their base copies are loaded)."""
    threads, rfcs = set(), set()
    for op in ops:
        cols, where = dict(op.cols), dict(op.where)
        if op.table == MESSAGES and op.op == "insert":
            threads.add(cols.get("thread_id"))
            m = _MID.match(str(cols.get("id") or ""))
            if m:
                rfcs.add(m.group(2))
            irt = str(cols.get("in_reply_to") or "").strip()
            if _RFC.match(irt):
                rfcs.add(irt)
        elif op.table == MESSAGES:
            m = _MID.match(str(where.get("id") or ""))
            if m:
                rfcs.add(m.group(2))
        elif op.table == THREADS:
            threads.add(where.get("id") or cols.get("id"))
    return {t for t in threads if isinstance(t, str)}, rfcs


def load_base(gmail_dir: Path, manifest_sha256: str, ops) -> tuple[dict, Facts]:
    """Users, labels, and the threads the statements touch (and every base thread holding a copy of a Message-ID they
    insert or answer) as DB-shaped rows, with the export-wide Facts. `manifest_sha256` pins <gmail_dir>/
    source_manifest.json; every file read must equal its entry there."""
    root = Path(gmail_dir)
    raw = (root / MANIFEST).read_bytes()
    if _sha(raw) != manifest_sha256:
        raise GmailBaseError(f"{root / MANIFEST}: sha256 {_sha(raw)} is not the pinned {manifest_sha256}")
    listed = {f["path"]: f.get("sha256") for f in json.loads(raw.decode("utf-8")).get("files", [])
              if isinstance(f, dict) and isinstance(f.get("path"), str)}

    def read(rel: str):
        if rel not in listed:
            raise GmailBaseError(f"{rel} is not listed in {MANIFEST}")
        data = (root / rel).read_bytes()
        if _sha(data) != listed[rel]:
            raise GmailBaseError(f"{rel}: sha256 {_sha(data)} differs from {MANIFEST} ({listed[rel]})")
        return json.loads(data.decode("utf-8"))

    facts = _scan(root, listed)
    base: dict[str, dict[tuple, dict]] = {USERS: {}, LABELS: {}, THREADS: {}, MESSAGES: {}}
    for item in read("users.json"):
        addr = item.get("emailAddress")
        base[USERS][(addr,)] = {"email_address": addr, "name": item.get("name"),
                                "messages_total": item.get("messagesTotal"), "threads_total": item.get("threadsTotal"),
                                "history_id": item.get("historyId"), "created_at": None}
        facts.mailboxes[str(addr).lower()] = addr
    for item in read("labels.json"):
        base[LABELS][(item["id"],)] = {"id": item["id"], "name": item.get("name"), "type": item.get("type")}
        facts.labels[item["id"]] = item.get("name")
    threads, rfcs = wanted(ops)
    for rfc in rfcs:
        threads |= {tid for _, tid in facts.copies.get(rfc, ())}
    for tid in sorted(threads):
        rel = facts.thread_files.get(tid)
        if rel is None:
            continue
        thread = read(rel)
        base[THREADS][(tid,)] = {"id": tid, "user_email": thread.get("user_email"), "snippet": None,
                                 "history_id": None}
        for item in thread.get("messages") or ():
            if isinstance(item, dict) and item.get("id"):
                key, row = _message_row(thread, item)
                base[MESSAGES][key] = row
    return base, facts


# --------------------------------------------------------------------------- rules

def _f(rule: str, severity: str, table: str, key: tuple, message: str) -> Finding:
    return Finding(rule=rule, severity=severity, table=table, key=key, message=message)


class _State:
    def __init__(self, overlay: Overlay, base: dict, facts: Facts):
        self.overlay, self.base, self.facts = overlay, base, facts
        self.messages = overlay.state.get(MESSAGES) or {}
        self.threads = overlay.state.get(THREADS) or {}
        self.labels = overlay.state.get(LABELS) or {}
        self.users = overlay.state.get(USERS) or {}
        self.mailboxes = {str(k[0]).lower() for k in self.users}
        self.by_thread: dict[str, list] = {}
        self.by_rfc: dict[str, list] = {}
        for key, row in self.messages.items():
            self.by_thread.setdefault(row.get("thread_id"), []).append(row)
            m = _MID.match(str(row.get("id") or ""))
            if m:
                self.by_rfc.setdefault(m.group(2), []).append(row)
        ins = set(overlay.inserted.get(MESSAGES, ()))
        self.inserted = [(k, self.messages[k]) for k in overlay.inserted.get(MESSAGES, ()) if k in self.messages]
        self.inserted_keys = ins

    def copy_boxes(self, rfc: str) -> set:
        """Mailboxes (lower) holding a copy of an RFC id: post-overlay rows and base copies anywhere."""
        boxes = {str(r.get("user_email") or "").lower() for r in self.by_rfc.get(rfc, ())}
        return boxes | {box for box, _ in self.facts.copies.get(rfc, ())}

    def parent_rows(self, rfc: str, box: str) -> list:
        return [r for r in self.by_rfc.get(rfc, ()) if str(r.get("user_email") or "").lower() == box]


def _participants(row: dict) -> tuple[str, set]:
    sender = (row.get("from_email") or "").lower()
    rcpts = {a.lower() for _, a in _entries_of(row.get("to_json")) + _entries_of(row.get("cc_json"))
             + _entries_of(row.get("bcc_json"))}
    return sender, rcpts


def _rule_g1(st: _State) -> list[Finding]:
    out = []
    for key, row in st.inserted:
        mid, tid, box = str(row.get("id") or ""), str(row.get("thread_id") or ""), row.get("user_email")
        m = _MID.match(mid)
        if not m or m.group(1) != box or not _RFC.match(m.group(2)):
            out.append(_f("G1", FAIL, MESSAGES, key, f"id {mid!r} is not '{box}/<RFC Message-ID>'"))
        t = _TID.match(tid)
        if not t or t.group(1) != box:
            out.append(_f("G1", FAIL, MESSAGES, key, f"thread_id {tid!r} is not '{box}/<number>'"))
        when = _instant(row.get("date"))
        if when is None:
            out.append(_f("G1", FAIL, MESSAGES, key, f"date {row.get('date')!r} is not a usable timestamp"))
        elif row.get("internal_date") is None or int(row["internal_date"]) // 1000 != int(when.timestamp()):
            out.append(_f("G1", FAIL, MESSAGES, key,
                          f"internal_date {row.get('internal_date')!r} is not the date {row.get('date')} in ms"))
        for col in ("label_ids_json", "to_json", "cc_json", "bcc_json", "reply_to_json", "attachments_meta_json"):
            if row.get(col) is not None and _json_list(row.get(col)) is None:
                out.append(_f("G1", FAIL, MESSAGES, key, f"{col} {str(row.get(col))[:60]!r} is not a JSON array"))
        headers = _json_list(row.get("headers_json"))
        if row.get("headers_json") is not None and (headers is None or not all(
                isinstance(h, dict) and set(h) >= {"name", "value"} for h in headers)):
            out.append(_f("G1", FAIL, MESSAGES, key, "headers_json is not a JSON array of {name, value}"))
        hid = row.get("history_id")
        if hid is not None and not re.fullmatch(r"[0-9]+", str(hid)):
            out.append(_f("G1", FAIL, MESSAGES, key, f"history_id {hid!r} is neither NULL nor a decimal string"))
        if not (row.get("body_text") or "").strip() and not row.get("body_html"):
            out.append(_f("G1", WARN, MESSAGES, key, "the message has no body"))
    return out


def _rule_g2(st: _State) -> list[Finding]:
    out = []
    for key, row in st.inserted:
        box = row.get("user_email")
        if (box,) not in st.users:
            out.append(_f("G2", FAIL, MESSAGES, key, f"mailbox {box!r} is not a gmail_users row"))
        thread = st.threads.get((row.get("thread_id"),))
        if thread is None:
            out.append(_f("G2", FAIL, MESSAGES, key, f"thread {row.get('thread_id')!r} does not exist"))
        elif thread.get("user_email") != box:
            out.append(_f("G2", FAIL, MESSAGES, key,
                          f"thread {row.get('thread_id')} belongs to {thread.get('user_email')}, the message to {box}"))
        for label in _json_list(row.get("label_ids_json")) or []:
            if (label,) not in st.labels:
                out.append(_f("G2", FAIL, MESSAGES, key, f"label {label!r} is not in gmail_labels"))
    for key in st.overlay.inserted.get(THREADS, ()):
        row = st.threads.get(key) or {}
        if (row.get("user_email"),) not in st.users:
            out.append(_f("G2", FAIL, THREADS, key, f"mailbox {row.get('user_email')!r} is not a gmail_users row"))
        t = _TID.match(str(row.get("id") or ""))
        if not t or t.group(1) != row.get("user_email"):
            out.append(_f("G2", FAIL, THREADS, key, f"thread id {row.get('id')!r} is not '<mailbox>/<number>'"))
    return out


def _rule_g3(st: _State) -> list[Finding]:
    out = []
    for key, row in st.inserted:
        m = _MID.match(str(row.get("id") or ""))
        if not m:
            continue
        here = {(b, t) for b, t in st.facts.copies.get(m.group(2), ()) if b == str(row.get("user_email")).lower()}
        if here:
            out.append(_f("G3", FAIL, MESSAGES, key, f"{row.get('id')} is already in base (thread {sorted(here)[0][1]})"))
        elif st.facts.copies.get(m.group(2)):
            out.append(_f("G3", WARN, MESSAGES, key,
                          f"Message-ID {m.group(2)} is a base message held in other mailboxes; this adds a copy"))
    for key in st.overlay.inserted.get(THREADS, ()):
        if key[0] in st.facts.thread_files:
            out.append(_f("G3", FAIL, THREADS, key, f"thread {key[0]} is already in base"))
    return out


_COPY_COLUMNS = ("subject", "date", "internal_date", "from_email", "from_name", "to_json", "cc_json", "body_text",
                 "snippet", "in_reply_to", "references")


def _rule_g4(st: _State) -> list[Finding]:
    out = []
    done = set()
    for key, row in st.inserted:
        m = _MID.match(str(row.get("id") or ""))
        if not m or m.group(2) in done:
            continue
        rfc = m.group(2)
        done.add(rfc)
        if rfc.startswith(_INVITE):
            continue
        copies = [r for r in st.by_rfc.get(rfc, ()) if (r.get("id"),) in st.inserted_keys]
        sender, rcpts = _participants(row)
        held = st.copy_boxes(rfc)
        missing = sorted(b for b in ({sender} | rcpts) & st.mailboxes if b not in held)
        if missing:
            out.append(_f("G4", FAIL, MESSAGES, key,
                          f"{rfc}: participant mailbox(es) {missing} hold no copy (sender's Sent copy, each "
                          "recipient's Inbox copy)"))
        for r in copies:
            box = str(r.get("user_email") or "").lower()
            s, rc = _participants(r)
            if box != s and box not in rc:
                out.append(_f("G4", FAIL, MESSAGES, (r.get("id"),),
                              f"copy in {box}, which is neither the sender nor a recipient"))
        for col in _COPY_COLUMNS:
            values = {json.dumps(r.get(col), ensure_ascii=False) for r in copies}
            if len(values) > 1:
                out.append(_f("G4", FAIL, MESSAGES, key, f"{rfc}: the copies disagree on {col}"))
    return out


def _rule_g5(st: _State) -> list[Finding]:
    out = []
    for key, row in st.inserted:
        box = str(row.get("user_email") or "").lower()
        labels = _json_list(row.get("label_ids_json")) or []
        sender, rcpts = _participants(row)
        if box == sender and "SENT" not in labels:
            out.append(_f("G5", FAIL, MESSAGES, key, f"the sender's copy in {box} is not labelled SENT"))
        if box != sender:
            if "SENT" in labels:
                out.append(_f("G5", FAIL, MESSAGES, key, f"a recipient's copy in {box} is labelled SENT"))
            if not ({"INBOX", "ARCHIVED"} & set(labels)):
                out.append(_f("G5", WARN, MESSAGES, key, f"the copy in {box} is in neither INBOX nor ARCHIVED"))
    return out


def _rule_g6(st: _State) -> list[Finding]:
    out = []
    for key, row in st.inserted:
        irt = str(row.get("in_reply_to") or "").strip()
        if not irt:
            continue
        if not _RFC.match(irt):
            out.append(_f("G6", FAIL, MESSAGES, key, f"in_reply_to {irt!r} is not an RFC Message-ID"))
            continue
        box = str(row.get("user_email") or "").lower()
        if not st.copy_boxes(irt):
            out.append(_f("G6", FAIL, MESSAGES, key, f"in_reply_to {irt} is no message in base or in the SQL"))
            continue
        mine = _instant(row.get("date"))
        parents = st.parent_rows(irt, box)
        known = [r for r in st.by_rfc.get(irt, ()) if _instant(r.get("date"))]
        if mine and known and not all(_instant(r.get("date")) < mine for r in known):
            out.append(_f("G6", FAIL, MESSAGES, key, f"the reply ({row.get('date')}) is not later than {irt}"))
        same = [p for p in parents if _topic(p.get("subject")) == _topic(row.get("subject"))]
        if same and all(p.get("thread_id") != row.get("thread_id") for p in same):
            out.append(_f("G6", FAIL, MESSAGES, key,
                          f"{box} holds the parent {irt} in thread {parents[0].get('thread_id')}, the reply in "
                          f"{row.get('thread_id')}"))
        refs = str(row.get("references") or "").split()
        if not refs or refs[-1] != irt:
            out.append(_f("G6", WARN, MESSAGES, key, "References does not end with In-Reply-To"))
        if not re.match(r"^\s*re\s*:", str(row.get("subject") or ""), re.I):
            out.append(_f("G6", WARN, MESSAGES, key, f"a reply's subject {row.get('subject')!r} has no Re:"))
    return out


def _rule_g7(st: _State, freeze_utc: str) -> list[Finding]:
    out = []
    freeze = _instant(freeze_utc)
    if freeze is None:
        return [_f("G7", FAIL, MESSAGES, (), f"freeze {freeze_utc!r} is not a usable timestamp")]
    for key, row in st.inserted:
        when = _instant(row.get("date"))
        if when is not None and not when < freeze:
            out.append(_f("G7", FAIL, MESSAGES, key, f"date {row.get('date')} is not before the freeze {freeze_utc}"))
    for key in st.overlay.inserted.get(THREADS, ()):
        t = _TID.match(str(key[0]))
        stamps = [int(r["internal_date"]) for r in st.by_thread.get(key[0], ()) if r.get("internal_date") is not None]
        if not t or not stamps:
            continue
        born = int(t.group(2)) >> 20
        if not 0 <= born - min(stamps) <= _HOUR_MS:
            out.append(_f("G7", WARN, THREADS, key,
                          f"thread number >> 20 is {born}, not within an hour after its first message "
                          f"({min(stamps)} ms; base: 88,027 of 88,726 normal threads)"))
    return out


def _newest(rows: list) -> dict | None:
    dated = [r for r in rows if _instant(r.get("date"))]
    return max(dated, key=lambda r: (_instant(r.get("date")), str(r.get("id")))) if dated else None


def _rule_g8(st: _State) -> list[Finding]:
    out = []
    inserted_threads = set(st.overlay.inserted.get(THREADS, ()))
    updated = set(st.overlay.updated.get(THREADS, ()))
    touched = {(r.get("thread_id"),) for _, r in st.inserted} | inserted_threads | updated
    for key in sorted(touched, key=str):
        thread = st.threads.get(key)
        if thread is None:
            continue
        newest = _newest(st.by_thread.get(key[0], []))
        if newest is None:
            continue
        newest_injected = (newest.get("id"),) in st.inserted_keys
        if key in inserted_threads or key in updated:
            if not newest_injected:
                out.append(_f("G8", WARN, THREADS, key,
                              f"the thread's snippet is set, but its newest message {newest.get('id')} is a base "
                              "message whose snippet base does not export"))
            elif thread.get("snippet") != newest.get("snippet"):
                out.append(_f("G8", WARN, THREADS, key,
                              f"snippet {str(thread.get('snippet'))[:40]!r} is not its newest message's "
                              f"{str(newest.get('snippet'))[:40]!r}"))
        elif newest_injected:
            out.append(_f("G8", WARN, THREADS, key,
                          f"base thread's newest message is now the injected {newest.get('id')}, but its snippet is "
                          "not updated"))
    return out


def _rule_g9(st: _State) -> list[Finding]:
    out = []
    for key, row in st.inserted:
        snippet = row.get("snippet")
        if snippet is None:
            continue
        body = _collapse(row.get("body_text"))
        if not body.startswith(_collapse(snippet)):
            out.append(_f("G9", FAIL, MESSAGES, key,
                          f"snippet {str(snippet)[:40]!r} is not the start of the body {body[:40]!r}"))
    return out


def _rule_g10(st: _State) -> list[Finding]:
    out = []
    for key, row in st.inserted:
        headers = _json_list(row.get("headers_json"))
        if headers is None:
            continue
        first = {}
        for h in headers:
            if isinstance(h, dict) and h.get("name") not in first:
                first[h.get("name")] = h.get("value")
        m = _MID.match(str(row.get("id") or ""))
        t = _TID.match(str(row.get("thread_id") or ""))
        checks = [
            ("Message-ID", m.group(2) if m else None, lambda v, want: str(v).strip() == want),
            ("Subject", row.get("subject"), lambda v, want: v == want),
            ("Date", row.get("date"), lambda v, want: _instant(v) is not None and _instant(v) == _instant(want)),
            ("From", row.get("from_email"),
             lambda v, want: [a.lower() for _, a in _addresses(v)][:1] == [str(want).lower()]),
            ("To", row.get("to_json"), lambda v, want: [a.lower() for _, a in _addresses(v)]
             == [a.lower() for _, a in _entries_of(want)]),
            ("Cc", row.get("cc_json"), lambda v, want: [a.lower() for _, a in _addresses(v)]
             == [a.lower() for _, a in _entries_of(want)]),
            ("In-Reply-To", row.get("in_reply_to"), lambda v, want: str(v).strip() == str(want or "").strip()),
            ("References", row.get("references"), lambda v, want: str(v).split() == str(want or "").split()),
            ("X-GM-THRID", t.group(2) if t else None, lambda v, want: str(v).strip() == want),
        ]
        for name, want, same in checks:
            if name in first:
                if want is None or not same(first[name], want):
                    severity = WARN if name in ("Cc", "In-Reply-To", "References") else FAIL
                    out.append(_f("G10", severity, MESSAGES, key,
                                  f"header {name} {str(first[name])[:50]!r} disagrees with the columns "
                                  f"({str(want)[:50]!r})"))
            elif name == "Cc" and _entries_of(row.get("cc_json")):
                out.append(_f("G10", WARN, MESSAGES, key, "cc_json lists recipients but there is no Cc header"))
            elif name in ("In-Reply-To", "References") and str(want or "").strip():
                out.append(_f("G10", WARN, MESSAGES, key, f"{name} column is set but the header is missing"))
            elif name in ("Message-ID", "Date", "Subject", "From", "To"):
                out.append(_f("G10", WARN, MESSAGES, key, f"no {name} header"))
    return out


def _rule_g11(st: _State) -> list[Finding]:
    out = []
    for key, row in st.inserted:
        entries = [(row.get("from_name") or "", row.get("from_email") or "")]
        for col in ("to_json", "cc_json", "bcc_json"):
            entries += _entries_of(row.get(col))
        for name, addr in entries:
            if not addr:
                continue
            names = st.facts.names.get(addr.lower())
            spelled = st.facts.spellings.get(addr.lower()) or set()
            if names is not None and addr not in spelled:
                out.append(_f("G11", FAIL, MESSAGES, key, f"{addr!r} is written {sorted(spelled)[:3]} in base"))
            if names is None:
                if addr.lower().endswith(INTERNAL):
                    out.append(_f("G11", WARN, MESSAGES, key, f"{addr} is a harmonygames.co address no base message "
                                                              "shows"))
            elif name not in names:
                shown = sorted(n or "(bare)" for n in names)[:4]
                out.append(_f("G11", WARN, MESSAGES, key, f"base never names {addr} {name or '(bare)'!r} "
                                                          f"(it uses {shown})"))
    return out


def _rule_g12(st: _State) -> list[Finding]:
    out = []
    for key, row in st.inserted:
        body = row.get("body_text") or ""
        if "\n" in body.replace("\r\n", ""):
            out.append(_f("G12", WARN, MESSAGES, key, "body line breaks are bare LF (base bodies use CRLF)"))
    return out


# --------------------------------------------------------------------------- entry point

def check_gmail(overlay: Overlay, base: dict, facts: Facts, *, freeze_utc: str) -> list[Finding]:
    """Run G1-G12 on the rows `overlay` inserted or updated; `base`, `facts` are load_base()'s result."""
    st = _State(overlay, base, facts)
    findings: list[Finding] = []
    findings += _rule_g1(st)
    findings += _rule_g2(st)
    findings += _rule_g3(st)
    findings += _rule_g4(st)
    findings += _rule_g5(st)
    findings += _rule_g6(st)
    findings += _rule_g7(st, freeze_utc)
    findings += _rule_g8(st)
    findings += _rule_g9(st)
    findings += _rule_g10(st)
    findings += _rule_g11(st)
    findings += _rule_g12(st)
    return sorted(findings, key=lambda f: (f.rule, f.table, str(f.key), f.message))
