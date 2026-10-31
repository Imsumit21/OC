#!/usr/bin/env python3
"""fact_check.py — fact consistency inside an injection and against the base universe.

Large injections (300–1,400 rows over 12 services) restate the same facts in many places: a
Slack claim, the mail that amends it, a Linear description, a sheet cell, a slide. This tool
scans every text-bearing value the SQL writes — Slack text + GitHub-app attachments, Gmail
subject/body, Linear titles/descriptions/comments, PR/review bodies, Trello desc/comments,
Confluence bodies, Docs body, Sheets grid cells (one segment per sheet row), Slides element
text/notes, GCal summary/description, Drive names — and reports:

ERRORS (exit 1)
  * declared-fact contradictions — the manifest's fact sheet
      facts: [{key, value, kind: amount|date|count|name|status|id|version,
               aliases?: [...], must_appear_in?: [record ids], forbidden_variants?: [...]}]
    - wherever the key or an alias is mentioned, any value of the fact's kind in the same
      sentence/line must equal the declared value (amount 11,700 = $11.7K; dates compare
      month/day/year and, when both sides carry a timezone, the UTC time); a differing value
      with the declared one absent is a contradiction
    - `name` facts: any near-spelling of the declared name (difflib ratio >= 0.8) that is not
      the name or a declared alias is a contradiction, mention or not
    - `forbidden_variants` must appear nowhere
    - `must_appear_in`: each listed record (SQL row id, Slack "C/ts", Gmail thread, sheet,
      deck …) must state the declared value
    - records named as superseded versions (every traps[].version_records entry except the
      newest) are exempt: they are meant to disagree (reported as notes)
  * --no-leak (always on in hardness_gate's fact_consistency): a fact that declares `home_ids`
    (its per-record carrier rows) may state its value only there, in its `must_appear_in`
    records and in its own `version_records`; the value in any other seeded text row is a
    `fact_leak` error — above all in bulk-readable rows (Slack messages, Linear issue
    descriptions, Sheets cells, Confluence bodies), where one list/search call returns it
    (harness red team A, R2 #2)
  * unresolved ids cited in text (base_check resolvers + the SQL itself): Linear keys,
    github.com/…/pull/N links, short '<repo>#N' refs, Slack permalinks, Drive f_/d_ ids,
    GCal evt_ ids, Confluence page_ ids

WARNINGS (heuristic drift, no fact sheet needed)
  * the same named entity spelled differently across rows (incl. near-misses of roster names)
  * the same subject word carrying different amounts, or a date noun (deadline, cut-off, due …)
    carrying different dates, across rows
  * people named in text who are inactive at the record's timestamp (activity.json: no
    authored activity within ±60 days, or after their departure signal)
  * bare first names that several roster entities share (entities.json collisions, e.g. the
    three Marcuses) — use the full name or a <@mention>

Every finding carries the SQL line, the table and the row id.

Usage:
  python3 Task_Authoring/tools/fact_check.py <injection.sql> [--manifest 01_Hardness_Manifest.json] [--no-leak] [--json]
  python3 Task_Authoring/tools/fact_check.py --self-test
  python3 Task_Authoring/tools/fact_check.py --integrity-matrix [--out DIR]   # catch matrix (fact_check + base_check + gate)
Read-only on the base exports (through base_check's caches). Exit 0 = PASS, 1 = FAIL, 2 = usage.
"""
from __future__ import annotations

import datetime as dt
import difflib
import html
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from base_check import (CLOCK, Base, _activity, _t, kb, parse_sql)  # noqa: E402
try:  # data horizon; older base_check has no DATA_CLOCK
    from base_check import DATA_CLOCK, KBUnavailable  # noqa: E402
except ImportError:  # pragma: no cover
    DATA_CLOCK = CLOCK

    class KBUnavailable(RuntimeError):
        """base_check predates the KB status contract."""

# ---------------------------------------------------------------- text units

TEXT_FIELDS = {
    "slack.slack_messages": ("text", "attachments_json"),
    "gmail.gmail_messages": ("subject", "body_text"),
    "linear.linear_issues": ("title", "description"),
    "linear.linear_comments": ("body",),
    "github.github_pull_requests": ("title", "body"),
    "github.github_pr_comments": ("body",),
    "github.github_reviews": ("body",),
    "github.github_review_comments": ("body",),
    "github.github_commits": ("message",),
    "trello.trello_cards": ("name", "desc"),
    "trello.trello_actions": ("data_json",),
    "trello.trello_checklists": ("name",),
    "trello.trello_check_items": ("name",),
    "confluence.confluence_pages": ("title", "body"),
    "confluence.confluence_page_versions": ("title", "body", "message"),
    "confluence.confluence_comments": ("body",),
    "gdocs.docs_documents": ("title", "body_text"),
    "gsheets.sheets_spreadsheets": ("title",),
    "gsheets.sheets_sheets": ("title", "grid_json"),
    "gslides.slides_presentations": ("title",),
    "gslides.slides_pages": ("notes",),
    "gslides.slides_page_elements": ("text", "table_json"),
    "gcal.gcal_events": ("summary", "description"),
    "gdrive.drive_files": ("name",),
}
ID_COLS = ("id", "event_id", "ical_uid", "document_id", "spreadsheet_id", "presentation_id", "object_id",
           "page_object_id", "drive_file_id", "thread_id", "identifier", "contact_id", "calendar_id")
TIME_COLS = ("created_at", "date", "submitted_at", "updated_at", "created", "modified_time", "created_time", "start_ts")


def _clean(s: str) -> str:
    s = str(s).replace("\\r\\n", "\n").replace("\\n", "\n").replace("\\t", " ").replace("\r", "")
    return s


def _strip_html(s: str) -> str:
    s = re.sub(r"(?i)<br\s*/?>|</(p|li|tr|h\d|div|td|th)>", "\n", s)
    return html.unescape(re.sub(r"<[^>]+>", " ", s))


def _walk_strings(x, out):
    if isinstance(x, str):
        out.append(x)
    elif isinstance(x, dict):
        for v in x.values():
            _walk_strings(v, out)
    elif isinstance(x, list):
        for v in x:
            _walk_strings(v, out)


def _field_text(col: str, v) -> str:
    if v is None or str(v) in ("", "None", "NULL"):
        return ""
    s = str(v)
    if col == "attachments_json":
        try:
            atts = json.loads(s)
        except ValueError:
            return ""
        return "\n".join(" ".join(str(a.get(k) or "") for k in ("pretext", "title", "text"))
                         for a in atts if isinstance(a, dict)) if isinstance(atts, list) else ""
    if col == "data_json":
        try:
            d = json.loads(s)
        except ValueError:
            return ""
        return _clean(d.get("text") or "") if isinstance(d, dict) else ""
    if col == "grid_json":
        try:
            g = json.loads(s)
        except ValueError:
            return _clean(s)
        if isinstance(g, list):
            lines = []
            for row in g:
                if isinstance(row, list):
                    cells = [str(c) for c in row if c not in (None, "")]
                else:
                    cells = []
                    _walk_strings(row, cells)
                lines.append(" | ".join(cells))
            return "\n".join(lines)
        out = []
        _walk_strings(g, out)
        return "\n".join(out)
    if col == "table_json":
        try:
            out = []
            _walk_strings(json.loads(s), out)
            return "\n".join(out)
        except ValueError:
            return ""
    s = _clean(s)
    if col == "body" and "<" in s and ">" in s:
        s = _strip_html(s)
    if col == "body_text":  # drop reply-quote history ("On … wrote:" + "> " lines); forwards stay (they are content)
        s = re.split(r"\n\s*On [^\n]{5,200} wrote:\s*\n", s)[0]
        s = "\n".join(line for line in s.split("\n") if not line.lstrip().startswith(">"))
    return s


SEG_RX = re.compile(r"\n+|(?<=[.!?;])\s+(?=[A-Z0-9•*\-(\"'])|\s+•\s+|\s+-\s+(?=[A-Z])")


def _segments(text: str) -> list:
    out, pos = [], 0
    for m in SEG_RX.finditer(text):
        if m.start() > pos:
            out.append((pos, m.start()))
        pos = m.end()
    if pos < len(text):
        out.append((pos, len(text)))
    return out


def text_units(stmts) -> list:
    units = []
    for s in stmts:
        fields = TEXT_FIELDS.get(s["table"])
        if not fields:
            continue
        if s["op"] == "insert":
            row, ids_src = s["row"], s["row"]
        elif s["op"] == "update":
            row, ids_src = s["set"], s["where"]
        else:
            continue
        parts = [_field_text(c, row.get(c)) for c in fields if c in row]
        text = "\n".join(p for p in parts if p.strip())
        if not text.strip():
            continue
        ids = {str(ids_src.get(c)) for c in ID_COLS if ids_src.get(c) not in (None, "", "None")}
        r = s["row"] if s["op"] == "insert" else {}
        if s["table"] == "slack.slack_messages" and r.get("channel_id") and r.get("ts"):
            ids.add(f"{r['channel_id']}/{r['ts']}")
        if s["table"] == "gmail.gmail_messages" and "/" in str(r.get("id") or ""):
            ids.add("rfc:" + str(r["id"]).split("/", 1)[1])  # the same RFC message in every mailbox copy
        if s["table"] == "gsheets.sheets_sheets" and r.get("spreadsheet_id"):
            ids.add(f"{r['spreadsheet_id']}#{r.get('title')}")
        rid = (r.get("id") or r.get("event_id") or r.get("document_id") or
               (f"{r.get('spreadsheet_id')}#{r.get('title')}" if r.get("spreadsheet_id") and s["table"].endswith("sheets_sheets") else None)
               or r.get("object_id") or r.get("spreadsheet_id") or r.get("presentation_id")
               or next(iter(sorted(ids)), None) or f"line{s['line']}")
        when = None
        for c in TIME_COLS:
            when = _t(r.get(c)) if r.get(c) else None
            if when:
                break
        if when is None and s["table"] == "slack.slack_messages":
            when = _t(r.get("ts"))
        units.append({"line": s["line"], "table": s["table"], "op": s["op"], "rid": str(rid), "ids": ids, "time": when,
                      "text": text, "segs": _segments(text), "row": r})
    return units


def _seg_of(u, pos):
    for a, b in u["segs"]:
        if a <= pos < b:
            return a, b
    return max(0, pos - 120), min(len(u["text"]), pos + 160)


# ---------------------------------------------------------------- value extraction

MULT = {"k": 1e3, "m": 1e6, "mn": 1e6, "million": 1e6, "thousand": 1e3, "bn": 1e9}
AMT_RX = re.compile(
    r"(?<![\w.])(?P<cur>[$€£])\s?(?P<a>\d[\d,]*(?:\.\d+)?)(?:\s?(?:-|–|to)\s?[$€£]?(?P<b>\d[\d,]*(?:\.\d+)?))?"
    r"(?:\s?(?P<suf>[kKmM]n?|million|thousand|bn)\b)?"
    r"|(?<![\w.$€£])(?P<a2>\d[\d,]*(?:\.\d+)?)(?:\s?(?P<suf2>[kKmM]|million|thousand))?\s?(?P<code>USD|EUR|GBP|dollars?)\b")


def amounts(text: str) -> list:
    out = []
    for m in AMT_RX.finditer(text):
        a, b, suf = (m.group("a"), m.group("b"), m.group("suf")) if m.group("cur") else (m.group("a2"), None, m.group("suf2"))
        try:
            mult = MULT.get((suf or "").lower(), 1)
            lo = float(a.replace(",", "")) * mult
            hi = float(b.replace(",", "")) * mult if b else lo
        except ValueError:
            continue
        out.append((m.start(), m.end(), (round(lo, 2), round(hi, 2)), m.group(0).strip()))
    return out


MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "sept": 9, "oct": 10,
          "nov": 11, "dec": 12}
MON = r"(jan|feb|mar|apr|may|jun|jul|aug|sept|sep|oct|nov|dec)(?:[a-z]*)\.?"
DATE_RX = re.compile(
    r"(?P<iso>\b(?P<y>20\d\d)-(?P<m>0[1-9]|1[0-2])-(?P<d>0[1-9]|[12]\d|3[01])(?:[T ](?P<H>\d\d):(?P<M>\d\d)(?::\d\d(?:\.\d+)?)?(?P<z>Z|[+-]\d\d:?\d\d)?)?)"
    r"|(?P<md>\b(?:(?:mon|tue|wed|thu|fri|sat|sun)[a-z]*,?\s+)?" + MON.replace("(jan", "(?P<mon1>jan") +
    r"\s+(?P<d1>[0-3]?\d)(?:st|nd|rd|th)?\b(?:,?\s+(?P<y1>20\d\d))?)"
    r"|(?P<dm>\b(?P<d2>[0-3]?\d)(?:st|nd|rd|th)?\s+" + MON.replace("(jan", "(?P<mon2>jan") + r"(?:,?\s+(?P<y2>20\d\d))?\b)",
    re.I)
TZ = {"pst": -8, "pdt": -7, "pt": -8, "est": -5, "edt": -4, "et": -5, "utc": 0, "gmt": 0, "z": 0, "cet": 1, "cest": 2, "bst": 1}
TIME_RX = re.compile(r"^\s*(?:,|at|@|⋅|·)?\s*(?P<h>[01]?\d)(?::(?P<mi>[0-5]\d))?\s*(?P<ap>am|pm)?(?:\s*[-–]\s*[01]?\d(?::[0-5]\d)?\s*(?:am|pm)?)?"
                     r"\s*\(?(?P<tz>PST|PDT|PT|EST|EDT|ET|UTC|GMT|Z|CET|CEST|BST)?\b", re.I)


def dates(text: str) -> list:
    out = []
    for m in DATE_RX.finditer(text):
        g = m.groupdict()
        if g["iso"]:
            y, mo, d = int(g["y"]), int(g["m"]), int(g["d"])
            utc = None
            if g["H"] and g["z"]:
                off = 0 if g["z"] == "Z" else int(g["z"][:3]) + (1 if g["z"][0] == "+" else -1) * int(g["z"][-2:]) / 60
                base = dt.datetime(y, mo, d, int(g["H"]), int(g["M"])) - dt.timedelta(hours=off)
                utc, (y, mo, d) = base.strftime("%H:%M"), (base.year, base.month, base.day)
            out.append((m.start(), m.end(), (y, mo, d, utc), m.group(0)))
            continue
        mon = (g["mon1"] or g["mon2"] or "").lower()[:4].rstrip(".")
        mo = MONTHS.get(mon if mon == "sept" else mon[:3])
        d = int(g["d1"] or g["d2"])
        y = int(g["y1"] or g["y2"]) if (g["y1"] or g["y2"]) else None
        if not mo or not 1 <= d <= 31:
            continue
        utc = None
        t = TIME_RX.match(text[m.end():m.end() + 40])
        if t and t.group("tz") and (t.group("ap") or t.group("mi")):
            h = int(t.group("h")) % 12 + (12 if (t.group("ap") or "").lower() == "pm" else 0) if t.group("ap") else int(t.group("h"))
            try:
                local = dt.datetime(y or DATA_CLOCK.year, mo, d, h, int(t.group("mi") or 0))
                base = local - dt.timedelta(hours=TZ[t.group("tz").lower()])
                utc, (mo, d) = base.strftime("%H:%M"), (base.month, base.day)
                y = base.year if y else None
            except ValueError:
                pass
        out.append((m.start(), m.end(), (y, mo, d, utc), m.group(0)))
    return out


VER_RX = re.compile(r"(?<![\w.$€£])v?(\d+\.\d+(?:\.\d+){0,2})(?![\w.]*\d)|\bbuild\s+#?(\d+)\b", re.I)


def versions(text: str) -> list:
    taken = [(a, b) for a, b, _, _ in amounts(text)] + [(a, b) for a, b, _, _ in dates(text)]
    out = []
    for m in VER_RX.finditer(text):
        if any(a <= m.start() < b for a, b in taken):
            continue
        out.append((m.start(), m.end(), (m.group(1) or f"build {m.group(2)}").lower(), m.group(0)))
    return out


NUM_WORDS = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
                                         "fifteen sixteen seventeen eighteen nineteen twenty".split())}
NUM = r"(\d[\d,]*|" + "|".join(NUM_WORDS) + r")"


def _num(s: str):
    s = s.lower().replace(",", "")
    return NUM_WORDS.get(s, int(s) if s.isdigit() else None)


def counts(text: str, aliases: list) -> list:
    out = []
    for a in aliases:
        ar = re.escape(a)
        for rx in (re.compile(r"(?<![\w.#-])" + NUM + r"\s+(?:[A-Za-z][\w-]*\s+){0,2}?" + ar + r"\b", re.I),
                   re.compile(r"\b" + ar + r"\s*(?:[:=]|is|are|was|were|of|total(?:s|ling)?|count(?:ed)?|now|at)?\s*" + NUM + r"\b(?![.\-/]\d)", re.I)):
            for m in rx.finditer(text):
                n = _num(m.group(1))
                if n is not None:
                    out.append((m.start(), m.end(), n, m.group(0)))
    return out


def ids_like(text: str, value: str) -> list:
    v = value.strip()
    m = re.fullmatch(r"(.*?)([A-Za-z]+)([-_#])(\d+)", v)
    if re.fullmatch(r"(?:[a-z]+_)?[0-9a-f]{8,}", v):
        pre = re.match(r"[a-z]+_", v)
        rx = (re.escape(pre.group(0)) if pre else "") + "[0-9a-f]{%d}" % (len(v) - (len(pre.group(0)) if pre else 0))
    elif m:
        rx = re.escape(m.group(1) + m.group(2) + m.group(3)) + r"\d+"
    else:
        rx = re.sub(r"\\?\d+", r"\\d+", re.escape(v))
    return [(x.start(), x.end(), x.group(0).lower(), x.group(0))
            for x in re.finditer(r"(?<![\w-])" + rx + r"(?![\w])", text, re.I)]


STATUS_GENERAL = ["in progress", "in review", "in qa", "to do", "todo", "backlog", "done", "canceled", "cancelled", "blocked",
                  "open", "closed", "merged", "shipped", "approved", "rejected", "pending", "live", "paused", "released",
                  "reverted", "fixed", "resolved", "reproduced", "not reproduced", "unverified", "verified", "won't fix",
                  "duplicate", "triage", "accepted", "declined", "on hold", "signed", "draft", "final", "completed", "incomplete"]


def _status_norm(s: str) -> str:
    s = s.lower().strip()
    return {"cancelled": "canceled", "todo": "to do", "wontfix": "won't fix", "complete": "completed"}.get(s, s)


def statuses(text: str, vocab: list) -> list:
    out, taken = [], []
    for w in sorted(set(vocab), key=len, reverse=True):
        for m in re.finditer(r"(?<![\w-])" + re.escape(w) + r"(?![\w-])", text, re.I):
            if any(a <= m.start() < b for a, b in taken):
                continue
            taken.append((m.start(), m.end()))
            out.append((m.start(), m.end(), _status_norm(m.group(0)), m.group(0)))
    return out


def _amount_eq(a, b):
    (alo, ahi), (blo, bhi) = a, b
    if alo == ahi and blo == bhi:
        return abs(alo - blo) < 0.01
    return (blo - 0.01 <= alo <= bhi + 0.01) if alo == ahi else (alo - 0.01 <= blo <= ahi + 0.01)


def _date_eq(a, b):
    ya, ma, da, ta = a
    yb, mb, db, tb = b
    return (ma, da) == (mb, db) and (ya is None or yb is None or ya == yb) and (ta is None or tb is None or ta == tb)


def parse_value(kind: str, value):
    v = str(value)
    if kind == "amount":
        a = amounts(v) or amounts("$" + v.lstrip("$"))
        return a[0][2] if a else None
    if kind == "date":
        d = dates(v)
        return d[0][2] if d else None
    if kind == "count":
        return _num(v.strip())
    if kind == "version":
        x = versions(v) or versions("build " + v if v.isdigit() else v)
        return x[0][2] if x else v.lower().lstrip("v")
    if kind == "status":
        return _status_norm(v)
    return v.strip().lower()


def values_of(kind, text, fact, vocab) -> list:
    if kind == "amount":
        return amounts(text)
    if kind == "date":
        return dates(text)
    if kind == "version":
        return versions(text)
    if kind == "status":
        return statuses(text, vocab)
    if kind == "id":
        return ids_like(text, str(fact["value"]))
    return []


def same(kind, a, b) -> bool:
    if kind == "amount":
        return _amount_eq(a, b)
    if kind == "date":
        return _date_eq(a, b)
    if kind == "version":
        return str(a).lstrip("v") == str(b).lstrip("v")
    return a == b


# ---------------------------------------------------------------- the check

FACT_KINDS = {"amount", "date", "count", "name", "status", "id", "version"}


def superseded_ids(manifest: dict) -> set:
    """Every traps[].version_records entry except the newest is a declared superseded version. The list is
    oldest first (hardness_gate's supersession_chronology proves the order from the records' own timestamps),
    so the newest is the last entry."""
    out = set()
    for t in manifest.get("traps", []) or []:
        vs = [v for v in t.get("version_records", []) or [] if isinstance(v, dict)]
        if len(vs) < 2:
            continue
        for v in vs[:-1]:
            for k in ("id", "base_pointer"):
                if v.get(k):
                    out.add(str(v[k]))
                    if "@" in str(v[k]).split("/", 1)[0] and "/<" in str(v[k]):
                        out.add("rfc:" + str(v[k]).split("/", 1)[1])
    return out


BULK_READABLE = {"slack.slack_messages": "Slack message (channel history / filter search returns it)",
                 "linear.linear_issues": "Linear issue title/description (linear_list_issues returns it)",
                 "gsheets.sheets_sheets": "Sheets cells (one values_batch_get returns them)",
                 "confluence.confluence_pages": "Confluence page body (search / get page returns it)",
                 "confluence.confluence_page_versions": "Confluence version body"}


def _rid_variants(rid: str) -> set:
    rid = str(rid).strip()
    out = {rid}
    m = re.match(r"^([CDG][A-Z0-9]{8,11})(?:\s+ts\s+|[:/])(\d{10}\.\d{6})$", rid)
    if m:
        out.add(f"{m.group(1)}/{m.group(2)}")
    if "@" in rid.split("/", 1)[0] and "/<" in rid:
        out.add("rfc:" + rid.split("/", 1)[1])
    return out


def leaks(units, facts, err, vocab_of) -> None:
    """--no-leak: a fact with home_ids states its value only in its home rows, must_appear_in records and its own
    version_records; anywhere else in seeded text it is a leak (one bulk call may return it)."""
    for f in facts:
        if not f.get("home_ids"):
            continue
        kind = str(f.get("kind") or "name").lower()
        decl = parse_value(kind, f["value"])
        if decl is None:
            continue
        home = set()
        for r in list(f.get("home_ids") or []) + list(f.get("must_appear_in") or []) + list(f.get("version_records") or []):
            home |= _rid_variants(r)
        aliases = [str(a) for a in [f["key"]] + list(f.get("aliases") or []) if str(a).strip()]
        mention = re.compile(r"(?<![\w-])(?:" + "|".join(re.escape(a) for a in sorted(aliases, key=len, reverse=True)) + r")(?![\w])", re.I)
        for u in units:
            if u["ids"] & home or u["rid"] in home:
                continue
            text, hit = u["text"], None
            if kind in ("name", "status", "id"):
                m = re.search(r"(?<![\w-])" + re.escape(str(f["value"])) + r"(?![\w])", text, re.I)
                hit = m.group(0) if m else None
            elif kind == "count":
                for m in mention.finditer(text):
                    a, b = _seg_of(u, m.start())
                    v = [x for x in counts(text[a:b], aliases) if x[2] == decl]
                    if v:
                        hit = v[0][3]
                        break
            else:
                v = [x for x in values_of(kind, text, f, vocab_of(f)) if same(kind, decl, x[2])]
                hit = v[0][3] if v else None
            if hit:
                where = BULK_READABLE.get(u["table"])
                err(u, f"fact '{f['key']}' = {f['value']} has home_ids {sorted(f['home_ids'])[:3]} but this row also states "
                       f"{hit!r}" + (f" — bulk-readable: {where}" if where else "") +
                       " (one call returns the per-record answer; move it to its home row or drop it)")


def check(sql: str, manifest: dict | None = None, base: Base | None = None, no_leak: bool = False) -> dict:
    from runtime_context import ensure_active
    ensure_active(globals(), require_source=True)
    manifest = manifest or {}
    base = base or Base()
    stmts = parse_sql(sql)
    units = text_units(stmts)
    errors, warnings, notes = [], [], []
    old = superseded_ids(manifest)

    def emit(pool, u, rule, msg):
        pool.append({"line": u["line"], "table": u["table"], "row": u["rid"], "rule": rule, "msg": msg})

    def exempt(u):
        return bool(u["ids"] & old)

    # ---- declared facts
    facts = [f for f in manifest.get("facts", []) or [] if isinstance(f, dict) and f.get("key") and "value" in f]
    linear_states = {s_ for v in base.linear()["team_states"].values() for s_ in v}
    for f in facts:
        kind = str(f.get("kind") or "name").lower()
        key, value = str(f["key"]), f["value"]
        aliases = [str(a) for a in [key] + list(f.get("aliases") or []) if str(a).strip()]
        if kind not in FACT_KINDS:
            errors.append({"line": 0, "table": "manifest", "row": key, "rule": "fact_sheet",
                           "msg": f"fact '{key}': kind {kind!r} is not one of {sorted(FACT_KINDS)}"})
            continue
        decl = parse_value(kind, value)
        if decl is None:
            errors.append({"line": 0, "table": "manifest", "row": key, "rule": "fact_sheet",
                           "msg": f"fact '{key}': declared value {value!r} does not parse as kind '{kind}'"})
            continue
        vocab = (sorted(linear_states) if str(value) in linear_states else STATUS_GENERAL) + [str(value)] + \
            [str(x) for x in f.get("forbidden_variants") or []]
        mention = re.compile(r"(?<![\w-])(?:" + "|".join(re.escape(a) for a in sorted(aliases, key=len, reverse=True)) + r")(?![\w])", re.I)
        seen = set()
        for u in units:
            text = u["text"]
            for fv in f.get("forbidden_variants") or []:
                if re.search(r"(?<![\w-])" + re.escape(str(fv)) + r"(?![\w])", text, re.I):
                    if exempt(u):
                        notes.append(f"line {u['line']} {u['rid']}: forbidden variant {fv!r} of '{key}' in a declared superseded version")
                    else:
                        emit(errors, u, "forbidden_variant", f"fact '{key}' = {value}: forbidden variant {fv!r} appears")
            if kind == "name":
                target = str(value)
                okforms = {a.lower() for a in aliases} | {target.lower()}
                n = len(target.split())
                words = list(re.finditer(r"[\w'’&.-]+", text))
                for size in {max(1, n - 1), n, n + 1}:
                    for i in range(0, max(0, len(words) - size + 1)):
                        cand = text[words[i].start():words[i + size - 1].end()].strip(".,;:'’\"")
                        cl = cand.lower()
                        # a correct mention plus a determiner/possessive/neighbouring word is not a misspelling
                        core = re.sub(r"^(the|a|an|our|their|his|her|its|this|that)\s+", "", cl)
                        core = re.sub(r"(['’]s|s)$", "", core)  # possessive or plain plural of a correct name
                        core = re.sub(r"[-_]+", " ", core)      # data-room / data_room = data room
                        # whole-form containment uses the declared name and real aliases only, never the bare key
                        names = {target.lower()} | {str(x).lower() for x in f.get("aliases") or []}
                        if (cl in okforms or core in okforms or (u["rid"], cl) in seen or len(cl) < 4
                                or any(re.search(r"(?<!\w)" + re.escape(o) + r"(?!\w)", cl) for o in names)):
                            continue
                        r = difflib.SequenceMatcher(None, cl, target.lower()).ratio()
                        if r >= 0.8:
                            seen.add((u["rid"], cl))
                            if exempt(u):
                                notes.append(f"line {u['line']} {u['rid']}: '{cand}' (variant of '{target}') in a declared superseded version")
                            else:
                                emit(errors, u, "fact_contradiction",
                                     f"fact '{key}' is the name {target!r}; this row spells it {cand!r} (similarity {r:.2f})")
                continue
            for m in mention.finditer(text):
                a, b = _seg_of(u, m.start())
                seg = text[a:b]
                vals = counts(seg, aliases) if kind == "count" else values_of(kind, seg, f, vocab)
                if kind == "id":
                    vals = [v for v in vals if not mention.fullmatch(v[3])]
                if not vals or any(same(kind, decl, v[2]) for v in vals):
                    continue
                near = min(vals, key=lambda v: abs((a + v[0]) - m.start()))
                k = (u["rid"], near[3].lower())
                if k in seen:
                    continue
                seen.add(k)
                msg = (f"fact '{key}' is declared {value} ({kind}); this row says {near[3]!r} next to '{m.group(0)}': "
                       f"\"{seg.strip()[:140]}\"")
                if exempt(u):
                    notes.append(f"line {u['line']} {u['rid']}: superseded version, expected to differ — {msg}")
                else:
                    emit(errors, u, "fact_contradiction", msg)
        for rid in f.get("must_appear_in") or []:
            hits = [u for u in units if str(rid) in u["ids"] or str(rid) == u["rid"]]
            if not hits:
                warnings.append({"line": 0, "table": "manifest", "row": str(rid), "rule": "must_appear_in",
                                 "msg": f"fact '{key}': must_appear_in record {rid} matches no text-bearing SQL row (base record or typo — not checkable)"})
                continue
            blob = "\n".join(u["text"] for u in hits)
            if kind == "name":
                ok = str(value).lower() in blob.lower()
            elif kind == "count":
                ok = any(v[2] == decl for v in counts(blob, aliases)) or re.search(r"(?<![\d.,])" + re.escape(str(value)) + r"(?![\d.,])", blob) is not None
            elif kind in ("status", "id"):
                ok = re.search(r"(?<![\w-])" + re.escape(str(value)) + r"(?![\w])", blob, re.I) is not None
            else:
                ok = any(same(kind, decl, v[2]) for v in values_of(kind, blob, f, vocab))
            if not ok:
                emit(errors, hits[0], "must_appear_in", f"fact '{key}' = {value} must appear in {rid}, which does not state it")

    # ---- no-leak: per-record facts only in their home rows
    if no_leak:
        def vocab_of(f):
            return (sorted(linear_states) if str(f["value"]) in linear_states else STATUS_GENERAL) + [str(f["value"])]
        leaks(units, facts, lambda u, msg: emit(errors, u, "fact_leak", msg), vocab_of)

    # ---- unresolved ids cited in text
    resolve_ids(units, stmts, base, lambda u, msg: emit(errors, u, "unresolved_id", msg))

    # ---- undeclared drift (warnings)
    live = [u for u in units if not exempt(u)]
    try:
        name_variants(live, lambda u, msg: emit(warnings, u, "entity_spelling", msg))
        people_in_text(live, lambda u, msg: emit(warnings, u, "inactive_person_named", msg),
                       lambda u, msg: emit(warnings, u, "ambiguous_name", msg))
    except KBUnavailable as exc:  # no KB for this universe: skip, loudly
        notes.append(f"person-name heuristics skipped: {exc} — verify against records")
    subject_drift(live, lambda u, msg: emit(warnings, u, "value_drift", msg))

    return {"verdict": "FAIL" if errors else "PASS", "errors": errors, "warnings": warnings, "notes": notes,
            "stats": {"statements": len(stmts), "text_units": len(units), "facts": len(facts),
                      "superseded_records": len(old)}}


# ---------------------------------------------------------------- id resolution (base_check resolvers + SQL)

def resolve_ids(units, stmts, base: Base, err) -> None:
    ins = defaultdict(set)
    for s in stmts:
        if s["op"] == "insert":
            r = s["row"]
            for c in ("id", "identifier", "event_id", "document_id", "spreadsheet_id", "presentation_id"):
                if r.get(c):
                    ins[s["table"]].add(str(r[c]))
            if s["table"] == "slack.slack_messages":
                ins["slack_ts"].add(f"{r.get('channel_id')}/{r.get('ts')}")
    L = base.linear()
    keys = sorted({t.split("_", 1)[1] for t in L["teams"]})
    lin_rx = re.compile(r"\b(" + "|".join(keys) + r")-(\d{1,5})\b")
    known_lin = set(L["identifiers"]) | ins["linear.linear_issues"]
    G = base.github()
    known_pr = set(G["prs"]) | ins["github.github_pull_requests"]
    repos = {r.split("/")[-1]: r for r in G["repos"]}
    short_rx = re.compile(r"(?<![\w/-])(" + "|".join(re.escape(r) for r in sorted(repos, key=len, reverse=True)) + r")#(\d+)\b")
    drive = None
    evts = None
    pages = None
    for u in units:
        text, done = u["text"], set()

        def bad(tok, msg):
            if tok not in done:
                done.add(tok)
                err(u, msg)
        for k, n in lin_rx.findall(text):
            if f"{k}-{n}" not in known_lin:
                bad(f"{k}-{n}", f"text cites Linear {k}-{n}, which exists neither in the base nor in the SQL")
        for repo, n in re.findall(r"github\.com/([\w.-]+/[\w.-]+)/pull/(\d+)", text):
            if f"{repo}#{n}" not in known_pr:
                bad(f"{repo}#{n}", f"text links PR {repo}#{n}, which is in neither the base nor the SQL")
        for repo, n in short_rx.findall(text):
            if f"{repos[repo]}#{n}" not in known_pr:
                bad(f"{repo}#{n}", f"text cites {repo}#{n}, which is in neither the base nor the SQL")
        for ch, sec, frac in re.findall(r"slack\.com/archives/([CDG][A-Z0-9]+)/p(\d{10})(\d{6})", text):
            ts = f"{sec}.{frac}"
            if f"{ch}/{ts}" in ins["slack_ts"]:
                continue
            if ch not in base.slack()["channels"]:
                bad(ch, f"Slack permalink to channel {ch}, which does not exist")
            elif ts not in base.slack_messages(ch):
                bad(f"{ch}/{ts}", f"Slack permalink {ch}/p{sec}{frac} matches no message (base or SQL)")
        for fid in re.findall(r"(?<![\w])([fd]_[0-9a-f]{22})(?![0-9a-f])", text):
            drive = drive if drive is not None else set(base.drive()["files"])
            if fid not in drive and fid not in ins["gdrive.drive_files"]:
                bad(fid, f"text cites Drive id {fid}, which is in neither the base nor the SQL")
        for eid in re.findall(r"(?<![\w])(evt_[0-9a-f]{22})(?![0-9a-f])", text):
            evts = evts if evts is not None else {e.split("|", 1)[1] for e in base.gcal()["events"]}
            if eid not in evts and eid not in ins["gcal.gcal_events"]:
                bad(eid, f"text cites calendar event {eid}, which is in neither the base nor the SQL")
        for pid in re.findall(r"(?<![\w])(page_[a-z0-9_]{3,})", text):
            pages = pages if pages is not None else set(base.confluence()["pages"])
            if pid not in pages and pid not in ins["confluence.confluence_pages"]:
                bad(pid, f"text cites Confluence page {pid}, which is in neither the base nor the SQL")


# ---------------------------------------------------------------- undeclared drift heuristics

LEAD_STOP = {"hi", "hey", "hello", "thanks", "thank", "the", "a", "an", "re", "fwd", "fw", "dear", "subject", "from", "to",
             "date", "cc", "on", "in", "for", "and", "but", "so", "if", "also", "please", "just", "my", "our", "your",
             "this", "that", "we", "i", "it", "per", "via", "with", "lot", "see", "not", "no", "yes", "ok", "when", "what",
             "who", "where", "why", "how", "all", "any", "every", "each", "both", "new", "old", "next", "last"}
CAP_RX = re.compile(r"(?<![\w@./-])([A-Z][A-Za-z0-9'’&-]*[A-Za-z0-9](?:[ \t]+[A-Z][A-Za-z0-9'’&-]*[A-Za-z0-9]){1,3})(?![\w@-])")


def _norm_name(s: str) -> str:
    s = re.sub(r"['’]s\b", "", s.lower())
    words = [w[:-1] if len(w) > 4 and w.endswith("s") and not w.endswith("ss") else w for w in re.findall(r"[a-z0-9]+", s)]
    return " ".join(words)


def _roster_names() -> list:
    names = set()
    for p in kb("activity")["people"].values():
        if p.get("name") and " " in p["name"]:
            names.add(p["name"])
    for e in kb("entities")["entities"]:
        if e.get("kind") == "person" and e.get("canonical_name") and " " in e["canonical_name"]:
            names.add(e["canonical_name"])
    return sorted(names)


def name_variants(units, warn) -> None:
    forms = defaultdict(lambda: defaultdict(list))  # norm -> surface -> [unit]
    for u in units:
        for m in CAP_RX.finditer(u["text"]):
            words = m.group(1).split()
            while words and words[0].lower().strip("'’") in LEAD_STOP:
                words = words[1:]
            if len(words) < 2 or all(w.isupper() and len(w) <= 4 for w in words):
                continue
            surface = " ".join(words)
            forms[_norm_name(surface)][surface].append(u)
    roster = {_norm_name(n): n for n in _roster_names()}
    norms = sorted(forms)
    reported = set()
    for i, a in enumerate(norms):
        sa = a.replace(" ", "")
        if len(sa) < 8:
            continue
        for b in norms[i + 1:]:
            sb = b.replace(" ", "")
            if len(sb) < 8 or sa == sb or re.sub(r"\d", "", sa) == re.sub(r"\d", "", sb):
                continue
            ta, tb = a.split(), b.split()
            if ta[:len(tb)] == tb or tb[:len(ta)] == ta or ta[-len(tb):] == tb or tb[-len(ta):] == ta:
                continue  # 'Harmony Games' vs 'Harmony Games IP': a longer name, not a respelling
            if len(ta) == len(tb) and sum(x != y for x, y in zip(ta, tb)) == 1 and \
                    any(len(x) <= 2 or len(y) <= 2 for x, y in zip(ta, tb) if x != y):
                continue  # 'Lot A' vs 'Lot B', 'Build 3' vs 'Build 4'
            r = difflib.SequenceMatcher(None, sa, sb).ratio()
            if r < 0.9:
                continue
            ua = [x for xs in forms[a].values() for x in xs]
            ub = [x for xs in forms[b].values() for x in xs]
            minority, major, mu, Mu = (a, b, ua, ub) if len(ua) <= len(ub) else (b, a, ub, ua)
            if roster.get(major) is None and roster.get(minority) is not None:
                minority, major, mu, Mu = major, minority, Mu, mu
            key = (minority, major)
            if key in reported:
                continue
            reported.add(key)
            sm, sM = next(iter(forms[minority])), next(iter(forms[major]))
            warn(mu[0], f"entity spelled {sm!r} here ({len(mu)} mention(s)) but {sM!r} in {len(Mu)} mention(s) "
                        f"(e.g. line {Mu[0]['line']}, row {Mu[0]['rid']}) — same entity? pick one spelling")
    for n, surfaces in forms.items():
        if n in roster or len(n.split()) != 2:
            continue
        for rn, real in roster.items():
            r = difflib.SequenceMatcher(None, n, rn).ratio()
            if 0.85 <= r < 1 and n.split()[0][:1] == rn.split()[0][:1]:
                us = [x for xs in surfaces.values() for x in xs]
                warn(us[0], f"{next(iter(surfaces))!r} is a near-miss of the roster name {real!r} ({len(us)} mention(s)) — misspelt person?")
                break


SALIENT_STOP = set("""the a an of to for in on at by from with and or is are was were be been it this that these those its our your
their my his her as about around approx approximately roughly total only just also still now then than per each
up down over under into out off we you they he she i me us them will would can could should may might must not no
yes ok so but if when which who what where why how all any some more most less few new old same other another one
two three four five six seven eight nine ten get got have has had do does did make made pay paid cost costs costing
quoted quote came come comes says said say""".split())
DATE_NOUNS = {"deadline", "cut-off", "cutoff", "due", "launch", "release", "freeze", "shutdown", "close", "closing", "sunset",
              "handoff", "hand-off", "kickoff", "kick-off", "transfer", "signing", "payment", "invoice", "expiry", "expires",
              "renewal", "go-live", "golive", "effective", "termination", "last day", "start", "starts", "ends", "end"}
MONTH_WORDS = {"jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "sept", "oct", "nov", "dec", "january",
               "february", "march", "april", "june", "july", "august", "september", "october", "november", "december",
               "mon", "tue", "wed", "thu", "fri", "sat", "sun", "monday", "tuesday", "wednesday", "thursday", "friday",
               "saturday", "sunday", "today", "tomorrow", "yesterday"}


def _subject_before(seg: str, pos: int):
    words = re.findall(r"[A-Za-z][A-Za-z-]+", seg[max(0, pos - 60):pos])
    for w in reversed(words[-5:]):
        lw = w.lower()
        if len(lw) >= 3 and lw not in SALIENT_STOP and lw not in MONTH_WORDS:
            return lw[:-1] if len(lw) > 4 and lw.endswith("s") and not lw.endswith("ss") else lw
    return None


def _date_noun(seg: str, a: int, b: int):
    window = seg[max(0, a - 50):min(len(seg), b + 30)].lower()
    found = [n for n in DATE_NOUNS if re.search(r"(?<![\w-])" + re.escape(n) + r"(?![\w-])", window)]
    if not found:
        return None
    n = sorted(found, key=len, reverse=True)[0]
    return {"cutoff": "cut-off", "hand-off": "handoff", "kick-off": "kickoff", "golive": "go-live"}.get(n, n)


CONTAINER_COLS = ("issue_id", "pr_id", "idCard", "page_id")
ANCHOR_RX = re.compile(r"\b(?:ENG|ZOM|ART|DES|EPI)-\d{1,5}\b|[\w.-]+#\d+\b|\bevt_[0-9a-f]{22}\b|\b[fd]_[0-9a-f]{22}\b")


def _anchor(u, seg: str):
    """What a value is about: an id cited in the same sentence, else the record's container (the issue a comment
    sits on, the PR, the card, the page), else the first cell of a sheet row; None = the conversation at large."""
    m = ANCHOR_RX.search(seg)
    if m:
        return m.group(0)
    for c in CONTAINER_COLS:
        if u["row"].get(c):
            return str(u["row"][c])
    if u["table"] == "gsheets.sheets_sheets" and " | " in seg:
        return seg.split(" | ", 1)[0].strip().lower()
    return None


def subject_drift(units, warn) -> None:
    groups = defaultdict(lambda: defaultdict(list))  # (kind, subject, anchor) -> norm value -> [(unit, raw)]
    for u in units:
        text = u["text"]
        for a, b in u["segs"]:
            seg = text[a:b]
            anchor = _anchor(u, seg)
            for s, e, norm, raw in amounts(seg):
                subj = _subject_before(seg, s)
                if subj:
                    groups[("amount", subj, anchor)][norm].append((u, raw))
            for s, e, norm, raw in dates(seg):
                noun = _date_noun(seg, s, e)
                if noun:
                    groups[("date", noun, anchor)][(norm[0], norm[1], norm[2])].append((u, raw))
        # meetings: a GCal row's own start and an invitation mail's '@ <when>' are dates of the same meeting
        r = u["row"]
        if u["table"] == "gcal.gcal_events" and r.get("summary") and str(r.get("rrule_json") or "[]") in ("[]", "None", ""):
            start = r.get("start_ts")
            if not start:
                try:
                    start = (json.loads(r.get("start_json") or "{}") or {}).get("dateTime")
                except (ValueError, AttributeError):
                    start = None
            st = _t(start) if start else None
            if st:
                groups[("date", "meeting '" + str(r["summary"]).strip().lower() + "'", None)][(st.year, st.month, st.day)].append(
                    (u, f"{st:%Y-%m-%d %H:%MZ} (event start)"))
        if u["table"] == "gmail.gmail_messages":
            m = re.match(r"\s*(?:updated\s+)?invitation(?:\s+with\s+note)?:\s*(.+?)\s+@\s+(.+)$", str(r.get("subject") or ""), re.I)
            if m:
                d = dates(m.group(2))
                if d:
                    y, mo, dd, _ = d[0][2]
                    groups[("date", "meeting '" + m.group(1).strip().lower() + "'", None)][(y, mo, dd)].append((u, d[0][3] + " (invitation)"))
    for (kind, subj, anchor), vals in sorted(groups.items(), key=lambda kv: (kv[0][0], kv[0][1], str(kv[0][2]))):
        rows = {x[0]["rid"] for v in vals.values() for x in v}
        if len(vals) < 2 or len(rows) < 2:
            continue
        if kind == "date":  # a year-less mention agrees with a dated one on the same day
            merged = defaultdict(list)
            for (y, m, d), xs in vals.items():
                merged[(m, d)].extend(xs)
            if len(merged) < 2:
                continue
            vals = merged
        ordered = sorted(vals.items(), key=lambda kv: -len(kv[1]))
        desc = "; ".join(f"{xs[0][1]!r} (line {xs[0][0]['line']}, row {xs[0][0]['rid']}{', +' + str(len(xs) - 1) if len(xs) > 1 else ''})"
                         for _, xs in ordered[:4])
        u = ordered[-1][1][0][0]
        warn(u, f"'{subj}'{f' ({anchor})' if anchor else ''} carries {len(vals)} different {kind}s across rows: {desc} — supersession (declare it in "
                "traps[].version_records / facts) or drift?")


def people_in_text(units, warn_inactive, warn_ambiguous) -> None:
    act = _activity()
    ent = kb("entities")
    collisions = ent.get("collisions", {}).get("shared_first_names", {})
    full, first = {}, defaultdict(set)
    for email, p in act.people.items():
        for nm in {p.get("name"), act.names.get(email)} - {None}:
            full[nm.lower()] = email
            first[nm.split()[0].lower()].add(email)
    for e in ent["entities"]:
        if e.get("kind") == "person" and e.get("canonical_name"):
            first[e["canonical_name"].split()[0].lower()].add((e.get("emails") or [e["entity_id"]])[0].lower())
    surnames = defaultdict(set)
    for n in collisions:
        for c in collisions[n]:
            parts = c.split("<")[0].split()
            if len(parts) > 1:
                surnames[n].add(parts[1].lower())
    unique_first = {f: next(iter(es)) for f, es in first.items() if len(es) == 1 and f not in collisions and len(f) >= 4}
    rx_full = re.compile(r"(?<![\w@.])(" + "|".join(re.escape(n) for n in sorted(full, key=len, reverse=True)) + r")(?![\w@])", re.I)
    rx_first = re.compile(r"(?<![\w@.<|])(" + "|".join(re.escape(n) for n in sorted(unique_first, key=len, reverse=True)) + r")(?![\w@])", re.I)
    rx_coll = re.compile(r"(?<![\w@.<|])(" + "|".join(re.escape(n) for n in collisions) + r")\b(?:\s+([A-Za-z]+))?", re.I) if collisions else None
    inactive, ambiguous = {}, {}
    for u in units:
        text = re.sub(r"<@[A-Z0-9_]+(?:\|[^>]*)?>|[\w.+-]+@[\w.-]+", " ", u["text"])
        named = set()
        spans = []
        for m in rx_full.finditer(text):
            named.add(full[m.group(1).lower()])
            spans.append((m.start(), m.end()))
        for m in rx_first.finditer(text):
            if not any(a <= m.start() < b for a, b in spans):
                named.add(unique_first[m.group(1).lower()])
        for email in named:
            v = act.judge(email, u["time"]) if u["time"] else None
            if v:
                inactive.setdefault(email, {"u": u, "rows": [], "reason": v[1]})["rows"].append(u)
        if rx_coll:
            for m in rx_coll.finditer(text):
                n = m.group(1).lower()
                nxt = (m.group(2) or "").lower()
                if nxt in surnames.get(n, set()):
                    continue
                ambiguous.setdefault(n, {"u": u, "rows": []})["rows"].append(u)
    for email, a in inactive.items():
        rows = a["rows"]
        warn_inactive(a["u"], f"names {act.name(email)}, inactive at the record's time: {a['reason']}"
                              + (f"; {len(rows)} rows (e.g. lines {', '.join(str(r['line']) for r in rows[:4])})" if len(rows) > 1 else ""))
    for n, a in ambiguous.items():
        rows = a["rows"]
        warn_ambiguous(a["u"], f"bare first name '{n.title()}' matches several roster entities ({'; '.join(collisions[n])}) — "
                               f"use the full name or a <@mention>; {len(rows)} row(s) (e.g. lines {', '.join(str(r['line']) for r in rows[:4])})")


# ---------------------------------------------------------------- output

def to_text(r: dict) -> str:
    lines = [f"FACT CHECK: {r['verdict']} — {r['stats']['text_units']} text-bearing rows, {r['stats']['facts']} declared facts, "
             f"{r['stats']['superseded_records']} declared superseded records"]
    lines.append(f"Errors ({len(r['errors'])}):" if r["errors"] else "Errors: none")
    for f in r["errors"][:80]:
        lines.append(f"  line {f['line']}: {f['table']} {f['row']}: [{f['rule']}] {f['msg']}")
    if len(r["errors"]) > 80:
        lines.append(f"  … {len(r['errors']) - 80} more (use --json)")
    if r["warnings"]:
        lines.append(f"Warnings ({len(r['warnings'])}):")
        for f in r["warnings"][:60]:
            lines.append(f"  line {f['line']}: {f['table']} {f['row']}: [{f['rule']}] {f['msg']}")
        if len(r["warnings"]) > 60:
            lines.append(f"  … {len(r['warnings']) - 60} more (use --json)")
    for n in r["notes"][:30]:
        lines.append(f"  note: {n}")
    return "\n".join(lines)


# ---------------------------------------------------------------- self-test

def _self_test() -> None:
    import hashlib
    ch, ol, br = "C09R0KXFX71", "EMPLOYEE_0003_SLACK_ID", "EMPLOYEE_0026_SLACK_ID"

    def slack(ts, user, text, iso):
        sid = hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]
        return (f"INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, created_at) VALUES "
                f"('{sid}', '{ts}', '{ch}', 'message', '{user}', '{text}', '{iso}');\n"), sid
    s1, id1 = slack("1768231200.000100", br, "Sunset fee is $11.7K, cut-off is Mon Feb 16 9am PST. DD has 13 open bugs on 0.3.309", "2026-01-12T15:20:00Z")
    s2, id2 = slack("1768231300.000100", ol, "heard the Sunset fee is $13-15K and the cut-off moved to Feb 13", "2026-01-12T15:21:40Z")
    s3, id3 = slack("1768231400.000100", ol, "ENG-2439 is Done. DD has 12 open bugs, store build 0.3.308. Sunset Studio confirmed", "2026-01-12T15:23:20Z")
    s4, id4 = slack("1768231500.000100", br, "old note: fee $9,000 (superseded)", "2026-01-12T15:25:00Z")
    s5, id5 = slack("1768231600.000100", br, "see ENG-99999 and f_0000000000000000000000 and ask Felix Young and Marcus", "2026-01-12T15:26:40Z")
    s6, id6 = slack("1768231700.000100", ol, "the deposit is $5,000 for Domino Delights", "2026-01-12T15:28:20Z")
    s7, id7 = slack("1768231800.000100", br, "deposit $5,500 confirmed for Domino Delihgts", "2026-01-12T15:30:00Z")
    sql = "-- Are you planning to inject? Yes\n" + s1 + s2 + s3 + s4 + s5 + s6 + s7
    manifest = {"facts": [
        {"key": "Sunset fee", "value": "$11,700", "kind": "amount", "aliases": ["fee"]},
        {"key": "cut-off", "value": "2026-02-16T17:00:00Z", "kind": "date"},
        {"key": "open bugs", "value": "13", "kind": "count", "aliases": ["open bugs"]},
        {"key": "ENG-2439", "value": "In Review", "kind": "status"},
        {"key": "store build", "value": "0.3.309", "kind": "version", "aliases": ["0.3.30"]},
        {"key": "buyer", "value": "Sunset Studios", "kind": "name", "forbidden_variants": ["Sunset Studio"]},
        {"key": "Sunset fee (first)", "value": "$11,700", "kind": "amount", "must_appear_in": [id1, id6]}],
        "traps": [{"id": "T1", "family": "superseding", "version_records": [
            {"service": "slack", "id": id4, "seeded": True, "at": "2026-01-12T15:25:00Z"},
            {"service": "slack", "id": id1, "seeded": True, "at": "2026-01-12T15:26:00Z"}]}]}
    r = check(sql, manifest)
    errs = [(e["row"], e["rule"], e["msg"]) for e in r["errors"]]
    blob = " | ".join(f"{a} {b} {c}" for a, b, c in errs)

    def has(row, needle):
        return any(e[0] == row and needle in e[2] for e in errs)
    assert has(id2, "$13-15K"), blob                       # amount range contradicts $11.7K
    assert has(id2, "Feb 13"), blob                        # date contradicts Feb 16
    assert not any(e[0] == id1 for e in errs if e[1] == "fact_contradiction"), blob  # $11.7K == $11,700; 9am PST == 17:00Z
    assert has(id3, "12 open bugs"), blob                  # count
    assert has(id3, "Done"), blob                          # status
    assert has(id3, "0.3.308"), blob                       # version
    assert any(e[0] == id3 and e[1] in ("fact_contradiction", "forbidden_variant") and "Sunset Studio" in e[2] for e in errs), blob
    assert not any(e[0] == id4 for e in errs), blob        # declared superseded version is exempt
    assert any("superseded" in n for n in r["notes"])
    assert has(id6, "must appear in"), blob                # must_appear_in
    assert has(id5, "ENG-99999") and has(id5, "f_0000000000000000000000"), blob  # unresolved ids
    w = " | ".join(f"{x['row']} {x['rule']} {x['msg']}" for x in r["warnings"])
    assert "Domino Delihgts" in w and "entity_spelling" in w, w
    assert "'deposit' carries 2 different amounts" in w, w
    assert "Felix Young" in w and "inactive_person_named" in w, w
    assert "'Marcus' matches several roster entities" in w, w
    assert r["verdict"] == "FAIL"
    clean = "-- Are you planning to inject? Yes\n" + slack("1768231200.000100", br, "Sunset fee is $11,700, cut-off Feb 16", "2026-01-12T15:20:00Z")[0]
    r2 = check(clean, {"facts": manifest["facts"][:2]})
    assert r2["verdict"] == "PASS" and not r2["warnings"], to_text(r2)
    # --no-leak: a per-record fact homed in one row must not be stated in another (bulk-readable) row
    s8, id8 = slack("1768231900.000100", ol, "ZOM-616 retest: iOS clean on 0.3.309", "2026-01-12T15:31:40Z")
    s9, id9 = slack("1768232000.000100", br, "fyi ZOM-616 iOS clean on 0.3.309 per oliver", "2026-01-12T15:33:20Z")
    leak_sql = "-- Are you planning to inject? Yes\n" + s8 + s9
    lf = {"facts": [{"key": "ZOM-616 iOS retest", "value": "iOS clean", "kind": "name", "home_ids": [id8]}]}
    r3 = check(leak_sql, lf, no_leak=True)
    assert [e["row"] for e in r3["errors"] if e["rule"] == "fact_leak"] == [id9], to_text(r3)
    assert "bulk-readable" in [e for e in r3["errors"] if e["rule"] == "fact_leak"][0]["msg"]
    assert not [e for e in check(leak_sql, lf)["errors"] if e["rule"] == "fact_leak"]          # off unless --no-leak
    assert not [e for e in check("-- Are you planning to inject? Yes\n" + s8, lf, no_leak=True)["errors"]
                if e["rule"] == "fact_leak"]                                                     # the home row itself
    print("self-test: ok")


# ---------------------------------------------------------------- integrity catch matrix

def integrity_matrix(out_dir: Path | None = None) -> str:
    """Planted-defect catch matrix for fact_check + base_check integrity rules + hardness_gate full-mode checks."""
    import hashlib
    import importlib.util
    import base_check
    import hardness_gate
    here = Path(__file__).resolve().parent
    src = here.parent / "support" / "examples" / "calibration" / "injection" / "mutation_matrix.py"
    spec = importlib.util.spec_from_file_location("mutation_matrix_ro", src)
    mm = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mm)  # import only: CLEAN fixture + helpers; nothing is written
    base = Base()
    CH, OL, BR, OL_U, BR_U = mm.CH, mm.OL, mm.BR, mm.OLIVER_U, mm.BRIAN_U

    def sid(ch, ts):
        return hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]
    P_ID, R_ID = sid(CH, mm.P_TS), sid(CH, mm.R_TS)
    # clean2 = mutation_matrix CLEAN + consistent facts in Slack and Gmail + the meeting's invitation mail
    inv_tid = f"{OL}/1890000000000000002"
    inv = (f"INSERT INTO gmail.gmail_threads (id, user_email, snippet, history_id) VALUES ('{inv_tid}', '{OL}', 'Invitation', NULL);\n"
           f"INSERT INTO gmail.gmail_messages ({mm.GMAIL_COLS}) VALUES ('{OL}/<calendar-0a1b2c3d@google.com>', '{inv_tid}', '{OL}', "
           "'[\"INBOX\"]', 'Handoff sync', 1768233000000, '2026-01-12T15:50:00Z', "
           "'Invitation: Handoff sync @ Wed Jan 14, 2026 9am - 9:30am (PST) (oliver.brooks@harmonygames.co)', "
           f"'{BR}', 'Brian Foster', '[\"{OL}\"]', '[]', '[]', 'Handoff sync', NULL, NULL);\n")
    clean = mm.CLEAN.replace("'can someone own the handoff list? <@",
                             "'can someone own the handoff list? vendor budget is $12,500, due Jan 20. <@") \
                    .replace("'can you own it', 1768233600000", "'can you own it', 1768233600000") \
                    .replace("'Handoff list', '{0}', 'Brian Foster', '[\"{1}\"]', '[]', '[]', 'can you own it'".format(BR, OL),
                             "'Handoff list', '{0}', 'Brian Foster', '[\"{1}\"]', '[]', '[]', 'can you own it? vendor budget is $12,500, due Jan 20'".format(BR, OL))
    clean = clean.replace("INSERT INTO gcal.gcal_events", inv + "INSERT INTO gcal.gcal_events", 1)
    assert "$12,500" in clean and clean.count("$12,500") == 2 and "Invitation: Handoff sync" in clean
    facts = [{"key": "vendor budget", "value": "$12,500", "kind": "amount", "aliases": ["budget"],
              "must_appear_in": [f"{OL}/<handoff-1@harmonygames.co>"]},
             {"key": "handoff due date", "value": "2026-01-20", "kind": "date", "aliases": ["due"]}]
    manifest = {"persona": "oliver_brooks", "facts": facts,
                "ask_fragments": [{"id": "K1", "service": "slack", "seeded_ids": [P_ID]},
                                  {"id": "K2", "service": "gmail", "seeded_ids": [f"{OL}/<handoff-1@harmonygames.co>"]}],
                "traps": [], "authorities": [], "chains": []}

    # an in-window GameOfDominoes PR with an 'opened' mirror, for the INT-01 companion mutation
    prs, opened = base.github()["prs"], base.gh_mirror()["opened"]
    pr = max((p for p in opened if p.startswith("harmonygames-Games/GameOfDominoes#") and p in prs
              and "2025-01-01" <= str(prs[p])[:10] <= "2025-10-01"), key=lambda p: int(p.rsplit("#", 1)[1]))
    mch, parent = opened[pr]
    created, updated = _t(prs[pr]), _t(base.github()["pr_updated"].get(pr)) or _t(prs[pr])
    when = (created + (updated - created) / 2).strftime("%Y-%m-%dT%H:%M:%SZ")
    review = (f"INSERT INTO github.github_reviews (id, pr_id, author_login, state, body, submitted_at) VALUES "
              f"('{pr}#rev_900', '{pr}', 'EMPLOYEE_0025_GITHUB_USERNAME', 'APPROVED', '', '{when}');\n")
    mts = f"{_t(when).timestamp():.0f}.000200"
    att = json.dumps([{"fallback": "[harmonygames-Games/GameOfDominoes] Review approved by arthur.blake",
                       "pretext": "Review approved by <https://github.com/arthur.blake|arthur.blake>",
                       "title": f"Review on #{pr.rsplit('#', 1)[1]} x"}]).replace("'", "''")
    mirror = (f"INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_ts_legacy, attachments_json, bot_id, created_at) "
              f"VALUES ('{sid(mch, mts)}', '{mts}', '{mch}', 'message', 'SLACK_BOT_0004_SLACK_ID', '', '{parent}', '{att}', 'B0GITHUB', '{when}');\n")
    pool = base.slack_messages(mch)
    base_pc = pool.get(parent, {}).get("reply_count") or 0
    newest = max([mts] + [t for t, m in pool.items() if m.get("thread_ts") == parent and t != parent], key=float)
    mirror += f"UPDATE slack.slack_messages SET reply_count = {int(base_pc) + 1}, latest_reply = '{newest}' WHERE id = '{opened_id(base, mch, parent)}';\n"

    def slack_row(ts_iso, user, text):
        t = mm.ts(ts_iso)
        return (f"INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, created_at) VALUES "
                f"('{sid(CH, t)}', '{t}', '{CH}', 'message', '{user}', '{text}', '{ts_iso}');\n")
    def MOVE_TO_BRIAN(q):
        return (q.replace(f"('{OL}/<handoff-1@harmonygames.co>', '{OL}/1890000000000000001', '{OL}'", f"('{BR}/<handoff-1@harmonygames.co>', '{BR}/1890000000000000001', '{BR}'")
                .replace(f"INSERT INTO gmail.gmail_threads (id, user_email, snippet, history_id) VALUES ('{OL}/1890000000000000001', '{OL}'",
                         f"INSERT INTO gmail.gmail_threads (id, user_email, snippet, history_id) VALUES ('{BR}/1890000000000000001', '{BR}'"))
    M = [  # (defect class, name, sql transform, manifest transform, expected tool:rule substring)
        ("fact contradiction", "Slack restates the budget as $15,000", lambda q: q.replace("vendor budget is $12,500, due Jan 20. <@", "vendor budget is $15,000, due Jan 20. <@"), None, "F:fact_contradiction"),
        ("fact contradiction", "Gmail moves the due date to Jan 21", lambda q: q.replace("budget is $12,500, due Jan 20'", "budget is $12,500, due Jan 21'"), None, "F:fact_contradiction"),
        ("fact contradiction", "forbidden variant appears", lambda q: q, lambda m: _set_fact(m, 0, forbidden_variants=["$12.5K"]) or m, None),
        ("fact contradiction", "must_appear_in record lacks the value", lambda q: q.replace("can you own it? vendor budget is $12,500, due Jan 20'", "can you own it?'"), None, "F:must_appear_in"),
        ("fact contradiction", "superseded version disagrees (control: must NOT fire)", lambda q: q.replace("vendor budget is $12,500, due Jan 20. <@", "vendor budget is $15,000, due Jan 20. <@"),
         lambda m: dict(m, traps=[{"id": "T1", "family": "superseding", "version_records": [
             {"service": "slack", "id": P_ID, "seeded": True, "at": "2026-01-12T15:00:00Z"},
             {"service": "gmail", "id": f"{OL}/<handoff-1@harmonygames.co>", "seeded": True, "at": "2026-01-12T16:00:00Z"}]}]), "-"),
        ("undeclared drift", "entity spelled two ways", lambda q: q.replace("'on it'", "'on it, Domino Delights list first'") + slack_row("2026-01-12T16:30:00Z", OL_U, "Domino Delihgts list is done"), None, "Fw:entity_spelling"),
        ("undeclared drift", "same subject, different amounts", lambda q: q + slack_row("2026-01-12T16:30:00Z", OL_U, "deposit is $5,000") + slack_row("2026-01-12T16:40:00Z", BR_U, "deposit $5,500 then"), None, "Fw:value_drift"),
        ("undeclared drift", "text cites a Drive id that exists nowhere", lambda q: q.replace("'on it'", "'on it, see f_9999999999999999999999'"), None, "F:unresolved_id"),
        ("undeclared drift", "names a person inactive at that time", lambda q: q.replace("'on it'", "'on it, will ask Felix Young'"), None, "Fw:inactive_person_named"),
        ("undeclared drift", "bare colliding first name", lambda q: q.replace("'on it'", "'on it, Marcus has the list'"), None, "Fw:ambiguous_name"),
        ("invisible load-bearing record", "load-bearing mail in another mailbox", MOVE_TO_BRIAN,
         lambda m: dict(m, ask_fragments=[m["ask_fragments"][0], {"id": "K2", "service": "gmail", "seeded_ids": [f"{BR}/<handoff-1@harmonygames.co>"]}]), "G:persona_reach"),
        ("hazard touch", "UPDATE of a state/lifecycle hazard record (ENG-2414, L07)", lambda q: q + "UPDATE linear.linear_issues SET updated_at = '2026-01-13T09:00:00Z' WHERE id = 'ENG-2414';\n", None, "B:Hazard touch L07"),
        ("hazard touch", "same, acknowledged with why_safe only (red team A item 2: no downgrade)", lambda q: q + "UPDATE linear.linear_issues SET updated_at = '2026-01-13T09:00:00Z' WHERE id = 'ENG-2414';\n",
         lambda m: dict(m, hazard_acknowledgements=[{"hazard_id": "L07", "why_safe": "reconciling ENG-2414's PR state is requirement R2"}]), "B:acknowledgement alone"),
        ("hazard touch", "same, resolution: repaired but the UPDATE leaves the state 'PR'", lambda q: q + "UPDATE linear.linear_issues SET updated_at = '2026-01-13T09:00:00Z' WHERE id = 'ENG-2414';\n",
         lambda m: dict(m, hazard_acknowledgements=[{"hazard_id": "L07", "resolution": "repaired", "why_safe": "x"}]), "G:hazard_scope"),
        ("hazard touch", "resolution: repaired and the UPDATE moves ENG-2414 to Done (control: gate must pass hazard_scope)",
         lambda q: q + "UPDATE linear.linear_issues SET state_id = 'Done', completed_at = '2026-01-13T09:00:00Z', updated_at = '2026-01-13T09:00:00Z' WHERE id = 'ENG-2414';\n",
         lambda m: dict(m, hazard_acknowledgements=[{"hazard_id": "L07", "resolution": "repaired", "why_safe": "closing ENG-2414 is requirement R2"}]), "-G"),
        ("hazard touch", "text cites a referential/lifecycle hazard record (ENG-2425, L01)", lambda q: q.replace("'on it'", "'on it, like ENG-2425'"), None, "G:hazard_scope"),
        ("fact leak", "per-record fact with home_ids restated in a Slack channel message (red team A item 8)", lambda q: q,
         lambda m: _set_fact(m, 0, home_ids=[f"{OL}/<handoff-1@harmonygames.co>"]) or m, "F:fact_leak"),
        ("fact leak", "same fact, both rows declared as its home (control)", lambda q: q,
         lambda m: _set_fact(m, 0, home_ids=[f"{OL}/<handoff-1@harmonygames.co>", P_ID]) or m, "-"),
        ("invisible load-bearing record", "denied probe (trap-only) without alternate_evidence_ids (red team A item 1)", MOVE_TO_BRIAN,
         lambda m: dict(m, ask_fragments=[m["ask_fragments"][0]], traps=[{"id": "T9", "family": "acl_alternate", "seeded_ids": [f"{BR}/<handoff-1@harmonygames.co>"]}],
                        denied_probes=[{"record": f"{BR}/<handoff-1@harmonygames.co>", "reason": "designed denial"}]), "G:persona_reach"),
        ("invisible load-bearing record", "same denied probe with a YES alternate (control: gate must pass persona_reach)", MOVE_TO_BRIAN,
         lambda m: dict(m, ask_fragments=[m["ask_fragments"][0]], traps=[{"id": "T9", "family": "acl_alternate", "seeded_ids": [f"{BR}/<handoff-1@harmonygames.co>"]}],
                        denied_probes=[{"record": f"{BR}/<handoff-1@harmonygames.co>", "reason": "designed denial",
                                        "alternate_evidence_ids": [P_ID]}]), "-P"),
        ("missing integration companion", "APPROVED review in a mirror window without its Slack copy", lambda q: q + review, None, "B:no Slack mirror copy"),
        ("missing integration companion", "same review with its threaded copy (control)", lambda q: q + review + mirror, None, "-"),
        ("missing integration companion", "meeting with attendees, invitation mail removed", lambda q: q.replace(inv, ""), None, "Bw:no invitation mail"),
        ("missing integration companion", "invitation removed but no_notify declared (control)", lambda q: q.replace(inv, ""),
         lambda m: dict(m, integration_exceptions=[{"record_id": mm.UID, "reason": "no_notify: booked by phone"}]), "-"),
        ("inactive author", "Slack reply by someone who left (Samuel, quiet since 2025-10)", lambda q: q.replace(f"'message', '{OL_U}', 'on it'", "'message', 'EMPLOYEE_0004_SLACK_ID', 'on it'"), None, "B:Voice realism"),
        ("inactive author", "post by someone with no activity within ±60 days", lambda q: q + slack_row("2023-01-10T16:00:00Z", "EMPLOYEE_0026_SLACK_ID", "hello"), None, "Bw:Voice realism"),
    ]

    def run(sql, man):
        f = check(sql, man, base, no_leak=True)
        b = base_check.check(sql, base, man)
        g = {c["check"]: c for c in hardness_gate.integrity_checks(man, sql, base=base, fact_result=f, base_result=b)}
        return {"F": {e["rule"] + " " + e["msg"] for e in f["errors"]},
                "Fw": {w["rule"] + " " + w["msg"] for w in f["warnings"]},
                "B": {x["msg"] for x in b["check_A"] + b["check_C"]},
                "Bw": {x["msg"] for x in b["warnings"]},
                "G": {name for name, c in g.items() if not c["ok"]}}
    c0 = run(clean, manifest)
    lines = ["# Integrity catch matrix — fact_check + base_check (integrity rules) + hardness_gate full-mode checks", "",
             "Clean fixture (mutation_matrix CLEAN + consistent facts + invitation mail): "
             f"fact_check {len(c0['F'])} errors / {len(c0['Fw'])} warnings; base_check {len(c0['B'])} FAIL findings / {len(c0['Bw'])} warnings; "
             f"gate integrity checks failing: {sorted(c0['G']) or 'none'}", ""]
    for k in ("F", "Fw", "B", "Bw"):
        for m in sorted(c0[k]):
            lines.append(f"- clean {k}: {m[:200]}")
    lines += ["", "F = fact_check error · Fw = fact_check warning · B = base_check FAIL · Bw = base_check warning · "
              "G = gate check FAIL. Controls must produce no new finding of the targeted rule.", "",
              "| # | Defect class | Planted defect | fact_check | base_check | gate (persona_reach / fact_consistency / hazard_scope) | Caught | First new finding |",
              "|---|---|---|---|---|---|---|---|"]
    caught = total = ctrl_ok = ctrls = 0
    for i, (cls, name, tq, tm, expect) in enumerate(M, 1):
        sql = tq(clean)
        man = json.loads(json.dumps(manifest))
        if tm:
            man = tm(man)
        if expect is None:  # forbidden variant: plant the variant in the text
            sql = sql.replace("'on it'", "'on it, so $12.5K then'")
            expect = "F:forbidden_variant"
        r = run(sql, man)
        new = {k: sorted(r[k] - c0[k]) for k in ("F", "Fw", "B", "Bw")}
        newg = sorted(r["G"] - c0["G"])
        if expect.startswith("-"):
            ctrls += 1
            if expect == "-G":
                ok = "hazard_scope" not in newg
            elif expect == "-P":
                ok = "persona_reach" not in newg
            else:
                ok = not new["F"] and not any("Hazard" in m or "mirror" in m or "invitation" in m for m in new["B"] + new["Bw"])
            ctrl_ok += ok
            verdict = "control ok" if ok else "CONTROL FIRED"
        else:
            total += 1
            tool, needle = expect.split(":", 1)
            hit = (needle in newg) if tool == "G" else any(needle in m for m in new[tool])
            caught += hit
            verdict = "Y" if hit else "N"
        first = (new["F"] + new["B"] + [f"gate:{g}" for g in newg] + new["Fw"] + new["Bw"] + [""])[0]
        lines.append(f"| {i} | {cls} | {name} | {len(new['F'])}E/{len(new['Fw'])}W | {len(new['B'])}F/{len(new['Bw'])}W | "
                     f"{', '.join(newg) or '-'} | {verdict} | {first[:150].replace('|', '/')} |")
    lines.append(f"\nPlanted defects caught by the targeted rule: {caught}/{total}; controls silent: {ctrl_ok}/{ctrls}")

    # the two sample-task injections, end to end (full gate; only the integrity-layer findings are itemised)
    lines += ["", "## Sample-task injections", ""]
    integrity_rules = ("Hazard touch", "mirror", "linear[bot]", "invitation", "Voice realism")
    for d in ("sample_task_01", "sample_task_02"):
        folder = here.parent / "support" / "examples" / d
        sql = (folder / "01_Universe_Inject.sql").read_text()
        man = json.loads((folder / "01_Hardness_Manifest.json").read_text())
        f = check(sql, man, base, no_leak=True)
        b = base_check.check(sql, base, man)
        g = hardness_gate.evaluate(man, sql)
        lines.append(f"### {d} (persona {man.get('persona')})")
        lines.append(f"- fact_check: {f['verdict']} — {len(f['errors'])} errors, {len(f['warnings'])} warnings, "
                     f"{f['stats']['superseded_records']} declared superseded records")
        for e in f["errors"] + f["warnings"]:
            lines.append(f"  - line {e['line']} [{e['rule']}] {e['msg'][:220]}")
        new_b = [x for x in b["check_A"] + b["check_C"] if any(k in x["msg"] for k in integrity_rules)]
        new_w = [x for x in b["warnings"] if any(k in x["msg"] for k in integrity_rules)]
        lines.append(f"- base_check: {b['verdict']} — integrity-layer FAIL findings {len(new_b)}, integrity-layer warnings {len(new_w)} "
                     f"(all findings: {len(b['check_A']) + len(b['check_C'])} FAIL / {len(b['warnings'])} warnings)")
        for x in new_b:
            lines.append(f"  - FAIL line {x['line']}: {x['msg'][:220]}")
        for x in new_w:
            lines.append(f"  - warn line {x['line']}: {x['msg'][:220]}")
        gi = {c["check"]: c for c in g["checks"]}
        for name in ("base_consistency", "persona_reach", "fact_consistency", "hazard_scope"):
            c = gi[name]
            lines.append(f"- gate {name}: {'ok' if c['ok'] else 'FAIL'} — {c['detail'][:300]}")
        lines.append(f"- gate verdict {g['verdict']}; failing checks: {[c['check'] for c in g['checks'] if not c['ok']]}")
        lines.append("")
    text = "\n".join(lines)
    if out_dir:
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "integrity_matrix.md").write_text(text + "\n")
    return text


def _set_fact(m, i, **kw):
    m["facts"][i].update(kw)


def opened_id(base: Base, ch: str, ts: str) -> str:
    return (base.slack_messages(ch).get(ts) or {}).get("id") or ""


def main(argv: list) -> int:
    if "--self-test" in argv:
        _self_test()
        return 0
    if "--integrity-matrix" in argv:
        out = Path(argv[argv.index("--out") + 1]) if "--out" in argv else None
        print(integrity_matrix(out))
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
    r = check(Path(paths[0]).read_text(), manifest, no_leak="--no-leak" in argv)
    print(json.dumps(r, indent=2, default=str) if "--json" in argv else to_text(r))
    return 0 if r["verdict"] == "PASS" else 1


if __name__ == "__main__":
    from runtime_context import guarded_entry
    guarded_entry(globals(), require_source=True)
    raise SystemExit(main(sys.argv[1:]))
