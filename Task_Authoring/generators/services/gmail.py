"""Gmail emitter: spec records -> ordered operations (one email = one row per mailbox copy, plus thread rows).

Record kinds and fields (strict: unknown fields fail; required fields have no defaults):
  gmail.message   required  from to at body
                  optional  subject cc parent labels message_id date_offset
                  from      one entry, "name <address>" or a bare address: an authored literal, or the base form of a
                            known address {"origin":"base","construction":"reference","base":{"service":"gmail",
                            "collection":"addresses","record":"<address>","field":"/form"}}
                  to, cc    authored literal lists of entries (cc defaults to none)
                  at        the send time, exactly YYYY-MM-DDTHH:MM:SSZ (UTC)
                  subject   required for a new thread; a reply defaults to "Re: " + the parent's subject
                  body      the text (CRLF line breaks are written; author it with plain line breaks); quoting the
                            parent, if wanted, is part of the authored text
                  parent    the message this one replies to: {"origin":"authored","construction":"reference",
                            "ref":"<key of another gmail.message>"} or a base reference to the parent's id: base{service
                            gmail, collection messages, record "<mailbox>/<RFC Message-ID>", field "/id"}
                  labels    authored literal {"<mailbox>": [label ids]} replacing the default labels of those copies
                  message_id  authored literal "<local@domain>"; default derived (gmail.message.rfc_id)
                  date_offset authored literal "+HHMM" / "-HHMM" for the Date header (default +0000)
  gmail.haystack  fields: to, optional cc; rows: [{from, at, subject, text, sha256}] -> gmail.message records
                  <key>.001, ... (services/haystack.py): from an authored literal, text a pinned texts/ file.

Other records name a message by `ref: "<key>"` (its RFC Message-ID) or by the locator spec:<key>/message_id; a base
message is base:gmail:messages/<mailbox>/<RFC Message-ID>/<field>.

Copies (gmail.copies): every participant (from, to, cc) whose address is a mailbox in base (users.json) gets one copy:
the sender's labelled SENT, each recipient's INBOX (a sender who is also a recipient: one copy, SENT and INBOX). An
address with no mailbox in base gets no copy (external people, and staff whose mailbox is not exported).

Derived columns (conventions/conventions.json; each records its function and convention in the provenance):
  RFC Message-ID   "<CA" + 49 characters of urlsafe-base64 sha512("<sender>|<epoch>") + "@mail.gmail.com>"
                                                                                      gmail.message.rfc_id
  id               "<mailbox>/<RFC Message-ID>"                                       gmail.message.id
  thread_id        "<mailbox>/<n>": the parent's thread in that mailbox when the mailbox holds the parent, else a
                   new thread n = (first message's internal_date << 20) | 20 bits of sha256("<mailbox>|<RFC id>")
                                                                                      gmail.thread.id, gmail.reply
  label_ids_json   SENT / INBOX, CATEGORY_PERSONAL / SENT, INBOX, IMPORTANT unless authored   gmail.labels
  date, internal_date  at as YYYY-MM-DDTHH:MM:SSZ and epoch milliseconds              gmail.date
  snippet          the body with runs of white space made one space, first 140 characters    gmail.snippet
  from_email, from_name, to_json, cc_json   the entries as written; a known address must use a display name base uses
                   for it                                                             gmail.address.form
  in_reply_to, references, subject (reply)  parent's RFC id; parent's references + its id; "Re: " + parent subject
                                                                                      gmail.reply
  headers_json     X-GM-THRID, X-Gmail-Labels, Delivered-To (recipient copies), MIME-Version, Date, References,
                   In-Reply-To, Message-ID, Subject, From, To, Cc, Content-Type        gmail.headers
  size_estimate    UTF-8 bytes of the header block, a blank line and the body          gmail.size_estimate
  body_text CRLF; body_html, mbox_from NULL; bcc_json, reply_to_json, attachments_meta_json '[]'; history_id not
  written                                                                             gmail.body.crlf, gmail.message.shape
  thread rows      INSERT gmail_threads (id, user_email, snippet = its newest message's snippet, history_id NULL) per
                   new thread; UPDATE gmail_threads SET snippet for a base thread whose newest message is now injected
                                                                                      gmail.snippet

Refused here, with the record key (the independent checks are validate/gmail.py G1-G12): a time that is not exact
UTC; an entry that does not parse, a harmonygames.co address base never shows, a known address with a display name
base never uses for it; no recipient; a message without any copy; two messages with one RFC id, or an id base holds;
a parent that is not earlier, not found, or a base parent with no copy in any mailbox; an unknown label, a sender copy
without SENT or a recipient copy with SENT or without INBOX/ARCHIVED; labels for a mailbox that gets no copy; a new
thread id base holds.

Statement order (a thread before its messages, a parent before its replies): thread inserts by id; message inserts by
(internal_date, RFC id, mailbox); thread snippet updates by id.
"""
from __future__ import annotations

import base64
import datetime as dt
import email.utils
import hashlib
import re

from ..core.gmail_index import address_form, parse_entries
from ..core.ops import INSERT, UPDATE, Op
from ..core.sqlvalue import json_text
from ..core.values import SpecError
from . import haystack

SERVICE = "gmail"
VERSION = "gmail/1.0"

KINDS = {
    "gmail.message": {"required": {"from", "to", "at", "body"},
                      "optional": {"subject", "cc", "parent", "labels", "message_id", "date_offset"}},
}
HAYSTACKS = {"gmail.haystack": "gmail.message"}

CONVENTIONS = {
    "sql.literal_policy": (),
    "sql.json_text": (),
    "gmail.message.id": (),
    "gmail.message.rfc_id": (),
    "gmail.thread.id": (),
    "gmail.copies": (),
    "gmail.labels": (),
    "gmail.date": (),
    "gmail.snippet": (),
    "gmail.address.form": (),
    "gmail.reply": (),
    "gmail.headers": (),
    "gmail.size_estimate": (),
    "gmail.body.crlf": (),
    "gmail.message.shape": (),
}

AT_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
AT_TEXT = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$")
OFFSET = re.compile(r"^[+-](?:0[0-9]|1[0-4])[0-5][0-9]$")
RFC_ID = re.compile(r"^<[^<>\s@]+@[^<>\s@]+>$")
RFC_LOCAL = 49
RFC_DOMAIN = "mail.gmail.com"
SNIPPET_CHARS = 140
DEFAULT_OFFSET = "+0000"
THREAD_LOW_BITS = 20
SENT, INBOX, ARCHIVED = "SENT", "INBOX", "ARCHIVED"
DEFAULT_LABELS = {"sender": [SENT], "recipient": [INBOX, "CATEGORY_PERSONAL"], "self": [SENT, INBOX, "IMPORTANT"]}
CONTENT_TYPE = 'text/plain; charset="UTF-8"'
HEADER_ORDER = ("X-GM-THRID", "X-Gmail-Labels", "Delivered-To", "MIME-Version", "Date", "References", "In-Reply-To",
                "Message-ID", "Subject", "From", "To", "Cc", "Content-Type")
MESSAGE_COLUMNS = ("id", "thread_id", "user_email", "label_ids_json", "snippet", "internal_date", "date",
                   "size_estimate", "subject", "from_email", "from_name", "to_json", "cc_json", "bcc_json",
                   "reply_to_json", "body_text", "body_html", "headers_json", "in_reply_to", "references", "mbox_from",
                   "attachments_meta_json")
THREAD_COLUMNS = ("id", "user_email", "snippet", "history_id")
INTERNAL_DOMAIN = "harmonygames.co"
_WS = re.compile(r"\s+")
_RE_PREFIX = re.compile(r"^\s*re\s*:\s*", re.I)


# ---------------------------------------------------------------- derived values (also used by the tests)

def epoch_of(at, where: str) -> int:
    try:
        if not AT_TEXT.match(at):
            raise ValueError(at)
        when = dt.datetime.strptime(at, AT_FORMAT).replace(tzinfo=dt.timezone.utc)
    except (TypeError, ValueError):
        raise SpecError(where, f"time {at!r} is not YYYY-MM-DDTHH:MM:SSZ") from None
    return int(when.timestamp())


def rfc_id_for(sender: str, epoch: int) -> str:
    """gmail.rfc_id/1: a Gmail-shaped Message-ID fixed by (sender address, second)."""
    digest = hashlib.sha512(f"{sender.lower()}|{epoch}".encode("utf-8")).digest()
    local = "CA" + base64.urlsafe_b64encode(digest).decode("ascii").rstrip("=")[:RFC_LOCAL]
    return f"<{local}@{RFC_DOMAIN}>"


def thread_number(first_ms: int, mailbox: str, rfc: str) -> int:
    """gmail.thread_number/1: the first message's internal_date in the high bits, 20 bits from (mailbox, RFC id)."""
    low = int(hashlib.sha256(f"{mailbox.lower()}|{rfc}".encode("utf-8")).hexdigest()[:8], 16) & ((1 << THREAD_LOW_BITS) - 1)
    return (first_ms << THREAD_LOW_BITS) | low


def snippet_of(body: str) -> str:
    """gmail.snippet/1"""
    return _WS.sub(" ", body).strip()[:SNIPPET_CHARS].rstrip()


def crlf(text: str) -> str:
    """gmail.crlf/1: every line break written CRLF."""
    return text.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "\r\n")


def date_header(epoch: int, offset: str) -> str:
    sign = 1 if offset[0] == "+" else -1
    delta = dt.timedelta(hours=int(offset[1:3]), minutes=int(offset[3:5])) * sign
    local = dt.datetime.fromtimestamp(epoch, dt.timezone(delta))
    return email.utils.format_datetime(local)


def reply_subject(parent_subject: str) -> str:
    """'Re: ' + the parent's subject without its own Re: prefixes."""
    subject = parent_subject or ""
    while _RE_PREFIX.match(subject):
        subject = _RE_PREFIX.sub("", subject, count=1)
    return "Re: " + subject


def label_token(label_id: str, labels: dict) -> str:
    """The X-Gmail-Labels word for a label id: its labels.json name, 'Category <name>' for a category whose name lacks
    the word (the base header writes CATEGORY_PERSONAL as 'Category Personal')."""
    name = (labels.get(label_id) or {}).get("name") or label_id
    if label_id.startswith("CATEGORY_") and not name.lower().startswith("category"):
        return f"Category {name}"
    return name


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
        return {"from": haystack.literal(row["from"]), "at": haystack.literal(row["at"]),
                "subject": haystack.literal(row["subject"]), "body": haystack.text_file(row["text"], row["sha256"])}
    return haystack.expand(where, rec, kind=HAYSTACKS[rec["kind"]], shared_required={"to"},
                           shared_optional={"cc"}, row_required={"from", "at", "subject", "text", "sha256"},
                           row_optional=set(), build=build)


# ---------------------------------------------------------------- entries

def _entry(text, where: str, index) -> tuple[str, str, str]:
    """(display name, address, entry as written) of one From/To/Cc entry, refused unless base-consistent."""
    if not isinstance(text, str) or not text.strip():
        raise SpecError(where, "an address entry is a non-empty text: 'name <address>' or a bare address")
    found = parse_entries(text)
    if len(found) != 1:
        raise SpecError(where, f"{text!r} is not one address entry")
    name, addr = found[0]
    known = index.address(addr)
    if known is None:
        if addr.lower().endswith("@" + INTERNAL_DOMAIN):
            raise SpecError(where, f"{addr} is a {INTERNAL_DOMAIN} address no base message shows; check the spelling")
        return name, addr, address_form(name, addr)
    if addr != known["address"]:
        raise SpecError(where, f"base writes this address {known['address']!r}, not {addr!r}")
    if name not in known["names"]:
        shown = [n or "(bare address)" for n in known["names"][:4]]
        raise SpecError(where, f"base never names {addr} {name or '(bare address)'!r}; it uses {shown} (the "
                               f"base form is {known['form']!r})")
    return name, addr, address_form(name, addr)


def _entries(value, where: str, index) -> list[tuple[str, str, str]]:
    if not isinstance(value, list):
        raise SpecError(where, "must be a list of address entries")
    out = [_entry(v, f"{where}[{n}]", index) for n, v in enumerate(value)]
    seen = set()
    for _, addr, _ in out:
        if addr.lower() in seen:
            raise SpecError(where, f"{addr} is listed twice")
        seen.add(addr.lower())
    return out


def _base_time(msg: dict) -> int | None:
    """Epoch seconds of a base export message (date_parsed, else date as ISO or RFC 2822)."""
    for value in (msg.get("date_parsed"), msg.get("date")):
        if not value:
            continue
        try:
            if re.match(r"^\d{4}-\d{2}-\d{2}T", value):
                return int(dt.datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp())
            return int(email.utils.parsedate_to_datetime(value).timestamp())
        except (TypeError, ValueError):
            continue
    return None


# ---------------------------------------------------------------- expand

def expand(records: list, resolver, base) -> list[Op]:
    """records: spec records of this service ({key, kind, fields}); resolver(record, field) -> (value, provenance)."""
    index = base.index(SERVICE)
    users = base.records(SERVICE, "users")
    labels = base.records(SERVICE, "labels")
    mailboxes = {addr.lower(): addr for addr in users}

    # ---- every record: participants, time, RFC id (registered so other records can name it)
    items, by_rfc = [], {}
    for rec in records:
        k = rec["key"]
        sender_text, p_from = resolver(rec, "from")
        sender = _entry(sender_text, f"{k}.from", index)
        to_value, p_to = resolver(rec, "to")
        to = _entries(to_value, f"{k}.to", index)
        cc, p_cc = [], _default([], "gmail.message.shape")
        if "cc" in rec["fields"]:
            cc_value, p_cc = resolver(rec, "cc")
            cc = _entries(cc_value, f"{k}.cc", index)
        if not to:
            raise SpecError(f"{k}.to", "a message needs at least one To entry")
        both = {a.lower() for _, a, _ in to} & {a.lower() for _, a, _ in cc}
        if both:
            raise SpecError(f"{k}.cc", f"{sorted(both)} also in To")
        at, p_at = resolver(rec, "at")
        epoch = epoch_of(at, f"{k}.at")
        if "message_id" in rec["fields"]:
            rfc, p_rfc = resolver(rec, "message_id")
            if not isinstance(rfc, str) or not RFC_ID.match(rfc):
                raise SpecError(f"{k}.message_id", f"{rfc!r} is not an RFC Message-ID '<local@domain>'")
        else:
            rfc = rfc_id_for(sender[1], epoch)
            p_rfc = _derived("gmail.rfc_id/1", "gmail.message.rfc_id", ["from", "at"])
        if index.copies.get(rfc):
            raise SpecError(f"{k}.at", f"Message-ID {rfc} is already in base ({index.copies[rfc][0][0]}); move the "
                                       "message by a second or author message_id")
        other = by_rfc.get(rfc)
        if other is not None:
            raise SpecError(f"{k}.at", f"{other['key']} and {k} get the same Message-ID {rfc} (same sender, same "
                                       "second); move one by a second")
        resolver.derive(rec, "id", rfc, p_rfc)
        if "message_id" not in rec["fields"]:
            resolver.derive(rec, "message_id", rfc, p_rfc)
        offset = DEFAULT_OFFSET
        p_offset = _default(offset, "gmail.date")
        if "date_offset" in rec["fields"]:
            offset, p_offset = resolver(rec, "date_offset")
            if not isinstance(offset, str) or not OFFSET.match(offset):
                raise SpecError(f"{k}.date_offset", f"{offset!r} is not +HHMM / -HHMM")
        body, p_body = resolver(rec, "body")
        if not isinstance(body, str) or not body.strip():
            raise SpecError(f"{k}.body", "must be non-empty text")
        item = {"rec": rec, "key": k, "rfc": rfc, "epoch": epoch, "ms": epoch * 1000, "at": at, "offset": offset,
                "sender": sender, "to": to, "cc": cc, "body": crlf(body),
                "prov": {"from": p_from, "to": p_to, "cc": p_cc, "at": p_at, "rfc": p_rfc, "offset": p_offset,
                         "body": p_body}}
        by_rfc[rfc] = item
        items.append(item)

    # ---- parents, subjects, references (in time order so a spec parent is done before its replies)
    for item in sorted(items, key=lambda i: (i["ms"], i["rfc"])):
        rec, k = item["rec"], item["key"]
        item["parent"] = None
        if "parent" in rec["fields"]:
            pid, p_parent = resolver(rec, "parent")
            item["prov"]["parent"] = p_parent
            item["parent"] = _parent(item, pid, p_parent, by_rfc, index)
        parent = item["parent"]
        if "subject" in rec["fields"]:
            subject, p_subject = resolver(rec, "subject")
            if not isinstance(subject, str):
                raise SpecError(f"{k}.subject", "must be text")
        elif parent is not None:
            subject = reply_subject(parent["subject"])
            p_subject = _derived("gmail.reply_subject/1", "gmail.reply", ["parent subject"])
        else:
            raise SpecError(f"{k}.subject", "a new thread needs a subject")
        item["subject"], item["prov"]["subject"] = subject, p_subject
        if parent is not None:
            item["in_reply_to"] = parent["rfc"]
            item["references"] = " ".join((parent["references"] or "").split() + [parent["rfc"]])
        else:
            item["in_reply_to"] = item["references"] = ""

    # ---- copies: one per participant mailbox; thread and labels per copy
    for item in items:
        rec, k = item["rec"], item["key"]
        sender_box = mailboxes.get(item["sender"][1].lower())
        recipients = [mailboxes[a.lower()] for _, a, _ in item["to"] + item["cc"] if a.lower() in mailboxes]
        boxes = ([sender_box] if sender_box else []) + [b for b in recipients if b != sender_box]
        if not boxes:
            raise SpecError(f"{k}.to", "no participant has a mailbox in base, so the message would be in no mailbox")
        overrides, p_labels = {}, None
        if "labels" in rec["fields"]:
            overrides, p_labels = resolver(rec, "labels")
            if not isinstance(overrides, dict):
                raise SpecError(f"{k}.labels", "must be an object {mailbox: [label ids]}")
            stray = sorted(set(overrides) - set(boxes))
            if stray:
                raise SpecError(f"{k}.labels", f"{stray} get no copy of this message (copies: {boxes})")
        copies = []
        for box in boxes:
            role = ("self" if box in recipients else "sender") if box == sender_box else "recipient"
            if box in overrides:
                ids = overrides[box]
                p_lab = p_labels
            else:
                ids = list(DEFAULT_LABELS[role])
                p_lab = _derived("gmail.default_labels/1", "gmail.labels", ["copy role"])
            _check_labels(f"{k}.labels.{box}", ids, role, labels)
            copies.append({"box": box, "role": role, "labels": ids, "p_labels": p_lab})
        item["copies"] = copies

    # ---- threads: the parent's thread in a mailbox that holds the parent, else a new one
    spec_threads: dict[str, list] = {}           # thread id -> spec copies in it
    for item in sorted(items, key=lambda i: (i["ms"], i["rfc"])):
        parent = item["parent"]
        for copy in item["copies"]:
            tid = None
            if parent is not None:
                held = parent["spec"]["threads"] if parent["spec"] is not None else parent["threads"]
                tid = held.get(copy["box"])
            if tid is None:
                tid = f"{copy['box']}/{thread_number(item['ms'], copy['box'], item['rfc'])}"
                if tid in index.threads:
                    raise SpecError(f"{item['key']}.at", f"new thread {tid} is already in base; move the message by "
                                                         "a second")
                copy["new_thread"] = True
                copy["p_thread"] = _derived("gmail.thread_number/1", "gmail.thread.id", ["internal_date", "mailbox",
                                                                                         "Message-ID"])
            else:
                copy["new_thread"] = False
                copy["p_thread"] = _derived("gmail.reply_thread/1", "gmail.reply", ["parent's thread in this mailbox"])
            copy["thread"] = tid
            spec_threads.setdefault(tid, []).append((item, copy))
        item["threads"] = {c["box"]: c["thread"] for c in item["copies"]}

    # ---- operations
    thread_ops, message_ops, update_ops = [], [], []
    p_snip = _derived("gmail.thread_snippet/1", "gmail.snippet", ["newest message of the thread in this mailbox"])
    for tid in sorted(spec_threads):
        members = spec_threads[tid]
        newest_item, newest_copy = max(members, key=lambda ic: (ic[0]["ms"], ic[0]["rfc"]))
        if tid in index.threads:
            thread = index.thread(tid)
            base_times = [t for t in (_base_time(m) for m in thread.get("messages") or ()) if t is not None]
            if base_times and max(base_times) >= newest_item["epoch"]:
                continue                             # a base message stays the newest: the snippet does not change
            update_ops.append(Op("gmail.gmail_threads", UPDATE, (("snippet", snippet_of(newest_item["body"])),),
                                 where=(("id", tid),), record=None, prov=(("snippet", p_snip),)))
        else:
            opener, opening = next((i, c) for i, c in members if c["new_thread"])
            values = {"id": tid, "user_email": opening["box"], "snippet": snippet_of(newest_item["body"]),
                      "history_id": None}
            prov = {"id": opening["p_thread"],
                    "user_email": _derived("gmail.copy_mailbox/1", "gmail.copies", ["participants", "users.json"]),
                    "snippet": p_snip, "history_id": _default(None, "gmail.message.shape")}
            thread_ops.append(Op("gmail.gmail_threads", INSERT, tuple((c, values[c]) for c in THREAD_COLUMNS),
                                 record=opener["key"], prov=tuple((c, prov[c]) for c in THREAD_COLUMNS)))
    for item in sorted(items, key=lambda i: (i["ms"], i["rfc"])):
        for copy in sorted(item["copies"], key=lambda c: c["box"].lower()):
            row, prov = _row(item, copy, labels)
            message_ops.append(Op("gmail.gmail_messages", INSERT, tuple((c, row[c]) for c in MESSAGE_COLUMNS),
                                  record=item["key"], prov=tuple((c, prov[c]) for c in MESSAGE_COLUMNS)))
    return thread_ops + message_ops + sorted(update_ops, key=lambda op: op.where)


def _check_labels(where: str, ids, role: str, labels: dict) -> None:
    if not isinstance(ids, list) or not ids or not all(isinstance(x, str) for x in ids):
        raise SpecError(where, "must be a non-empty list of label ids")
    unknown = [x for x in ids if x not in labels]
    if unknown:
        raise SpecError(where, f"labels {unknown} are not in the pinned labels.json")
    if len(set(ids)) != len(ids):
        raise SpecError(where, "a label is listed twice")
    if role in ("sender", "self") and SENT not in ids:
        raise SpecError(where, "the sender's copy is labelled SENT (base: 2,468 of 2,495 own copies)")
    if role == "recipient" and SENT in ids:
        raise SpecError(where, "a recipient's copy is not labelled SENT")
    if role in ("recipient", "self") and not ({INBOX, ARCHIVED} & set(ids)):
        raise SpecError(where, "a received copy is in INBOX or ARCHIVED")


def _parent(item: dict, pid, p_parent: dict, by_rfc: dict, index) -> dict:
    """{"rfc", "subject", "references", "threads": {mailbox: thread id}} of the message a reply answers; refused
    unless it exists and is earlier."""
    k = item["key"]
    where = f"{k}.parent"
    spec = by_rfc.get(pid) if isinstance(pid, str) else None
    if spec is not None:
        if spec is item:
            raise SpecError(where, "a message cannot answer itself")
        if not spec["ms"] < item["ms"]:
            raise SpecError(where, f"parent {spec['key']} ({spec['at']}) is not earlier than the reply ({item['at']})")
        return {"rfc": spec["rfc"], "subject": spec["subject"], "references": spec["references"],
                "threads": None, "spec": spec}
    cited = p_parent.get("base") if p_parent.get("origin") == "base" else None
    if not cited or (cited.get("service"), cited.get("collection"), cited.get("field")) != (SERVICE, "messages", "/id"):
        raise SpecError(where, "a parent is ref: <key of a spec gmail.message> or a base reference to gmail "
                               "messages/<mailbox>/<RFC Message-ID> field /id")
    rfc = str(pid).partition("/")[2]
    copies = index.copies.get(rfc) or []
    if not copies:
        raise SpecError(where, f"base message {pid} not found")
    threads, first = {}, None
    for box, tid in copies:
        thread = index.thread(tid)
        msg = next((m for m in thread.get("messages") or () if m.get("id") == f"{box}/{rfc}"), None)
        if msg is None:
            continue
        threads.setdefault(box, tid)
        first = first or msg
    if first is None:
        raise SpecError(where, f"base message {pid} not found")
    when = _base_time(first)
    if when is None or not when < item["epoch"]:
        raise SpecError(where, f"base message {pid} is not earlier than the reply ({item['at']})")
    return {"rfc": rfc, "subject": first.get("subject") or "", "references": first.get("references") or "",
            "threads": threads, "spec": None}


def _row(item: dict, copy: dict, labels: dict) -> tuple[dict, dict]:
    shape = "gmail.message.shape"
    box, tid = copy["box"], copy["thread"]
    sender_name, sender_addr, sender_form = item["sender"]
    to_forms = [form for _, _, form in item["to"]]
    cc_forms = [form for _, _, form in item["cc"]]
    headers = {
        "X-GM-THRID": tid.partition("/")[2],
        "X-Gmail-Labels": ",".join(label_token(x, labels) for x in copy["labels"]),
        "Delivered-To": box if copy["role"] == "recipient" else None,
        "MIME-Version": "1.0",
        "Date": date_header(item["epoch"], item["offset"]),
        "References": item["references"] or None,
        "In-Reply-To": item["in_reply_to"] or None,
        "Message-ID": item["rfc"],
        "Subject": item["subject"],
        "From": sender_form,
        "To": ", ".join(to_forms),
        "Cc": ", ".join(cc_forms) or None,
        "Content-Type": CONTENT_TYPE,
    }
    header_list = [{"name": n, "value": headers[n]} for n in HEADER_ORDER if headers[n] is not None]
    block = "".join(f"{h['name']}: {h['value']}\r\n" for h in header_list)
    row = {
        "id": f"{box}/{item['rfc']}", "thread_id": tid, "user_email": box,
        "label_ids_json": json_text(copy["labels"]), "snippet": snippet_of(item["body"]),
        "internal_date": item["ms"], "date": item["at"],
        "size_estimate": len((block + "\r\n" + item["body"]).encode("utf-8")),
        "subject": item["subject"], "from_email": sender_addr, "from_name": sender_name or None,
        "to_json": json_text(to_forms), "cc_json": json_text(cc_forms), "bcc_json": "[]", "reply_to_json": "[]",
        "body_text": item["body"], "body_html": None, "headers_json": json_text(header_list),
        "in_reply_to": item["in_reply_to"], "references": item["references"], "mbox_from": None,
        "attachments_meta_json": "[]",
    }
    p = item["prov"]
    copy_of = _derived("gmail.copy_mailbox/1", "gmail.copies", ["participants", "users.json"])
    prov = {
        "id": _derived("gmail.message_id/1", "gmail.message.id", ["mailbox", "Message-ID"]),
        "thread_id": copy["p_thread"], "user_email": copy_of, "label_ids_json": copy["p_labels"],
        "snippet": _derived("gmail.snippet/1", "gmail.snippet", ["body"]),
        "internal_date": _derived("gmail.internal_date/1", "gmail.date", ["at"]),
        "date": p["at"], "size_estimate": _derived("gmail.size_estimate/1", "gmail.size_estimate",
                                                   ["headers", "body"]),
        "subject": p["subject"], "from_email": p["from"], "from_name": p["from"], "to_json": p["to"],
        "cc_json": p["cc"], "bcc_json": _default("[]", shape), "reply_to_json": _default("[]", shape),
        "body_text": dict(p["body"], transform=_derived("gmail.crlf/1", "gmail.body.crlf")),
        "body_html": _default(None, shape),
        "headers_json": _derived("gmail.headers/1", "gmail.headers", ["thread", "labels", "columns"]),
        "in_reply_to": p.get("parent") or _default("", "gmail.reply"),
        "references": _derived("gmail.references/1", "gmail.reply", ["parent references", "parent id"])
        if item["references"] else _default("", "gmail.reply"),
        "mbox_from": _default(None, shape), "attachments_meta_json": _default("[]", shape),
    }
    return row, prov


def key_of(op: Op) -> tuple:
    if op.op == UPDATE:
        return tuple(v for _, v in op.where)
    return (op.col("id"),)
