#!/usr/bin/env python3
"""oe_qualifier_check.py - every qualifier in an Oracle Event's Expected line must be in the record the call reads.

The platform reviewer (/oe, pass O1) opens the record behind each event and checks every value on the `Expected:`
line with its qualifier: a date, a count, a name, a status, an amount, "the only", "latest". The local playbook let
narrative values through as `not_a_claim`. This tool does the mechanical part of that check (plan RC4 item 4, WS5
item 2). It reads `08_Oracle_Events.md`, finds the record(s) each event reads and compares the qualifiers.

What it does
  1. Parse the events: `OE <n>` heading (also `**OE 3**`, `## OE 3`, `OE 3 -`, `Step 3`), the call description and
     the `Expected:` text (also `Expected data:`, `Expected (note):`, "the agent finds"). A block it cannot parse
     is reported under `oe.parse`, never skipped.
  2. Resolve the records of each event. Injected rows come from `01_Universe_Inject.sql`, parsed as text (never
     executed), with UPDATEs applied. A record is matched by an id in the event (ticket, Slack ts, file id, #number),
     by a quoted title, or by a verbatim quote found in the row. Base records are read through `tools/hg.py`
     (`records` for exact ids, `search search-many` + `search get-many` for quotes) under the task's context.
  3. Extract the qualifiers of the Expected text: quoted strings, dates and times, ids and other literals (emails,
     snake_case ids, tickets, Slack ids, SHAs, versions), amounts and figures, counts, states, the author named in
     front of a quote, superlatives ("only", "latest", "first") and absence wording ("no other", "never").
  4. Check each one:
       supported     found in a resolved record (the record id and field are kept)
       contradicted  the record holds a different value for the same field (a message's timestamp, author, reply
                     count, a ticket's state, a file's owner), or the date contradicts itself (weekday, PT vs UTC)
       unsupported   not in the resolved records, and every source in scope was really read or searched
       unverifiable  the record could not be read, or the wording needs a collection-wide read (the line says
                     which read would prove it)

Rules that decide a FAIL (conservative on purpose)
  - A date is compared with a record only when it is bound to it: it introduces the record's quote
    (`Leo, Tue Sep 30 2025 3:05 PM PT, ts 1759269913.882683: "..."`) or a field word names the field ("created",
    "due", "merged" ...) next to a quoted title. Without such a word only a message's own timestamp is compared.
  - Minute rule: a clock time contradicts a record time only when the record holds that time to the minute (an epoch
    ts, or an ISO time that is not exactly 00:00:00 UTC). The minute may be cut (what Slack shows) or rounded. Against
    a day-only value the clock time is dropped: the day contradicts only when it is neither the record's UTC day nor
    its Pacific day (task_context.date_acceptance); if the day agrees, the clock time is unverifiable.
  - A quote is the record's text when it matches after dashes, quote marks and emphasis are made plain (the platform
    passed hyphens written for em dashes); other case is unsupported only against the record the event reads.
  - "all five read "X"" / "both say "X"": fewer places than claimed is unsupported (never contradicted: the base
    search is literal), and only when the event's base export was searched for that quote.

Checks
  oe.parse        every block is an event with an Expected line
  oe.records      every read event resolves to at least one record
  oe.qualifiers   FAIL on any contradicted qualifier, WARN on unsupported or unverifiable ones; one line per finding

Limits (read these before trusting a PASS)
  - It cannot judge meaning. "The fix is in build #2297" passes when #2297 is in the record, even if that build
    failed. Attribution to the wrong subject, a rule applied to too few items and wrong OE cross-references are not
    seen. Most platform NON-FAIL 3 findings are of this kind; run the blind reviewer for them.
  - Base reads are evaluator-wide: a quote found in a mailbox the persona cannot open still counts as found.
  - A write or a reasoning event states values the path produces. Only its dates, ids and reused values are checked.

Usage
  python3.12 -B Task_Authoring/tools/oe_qualifier_check.py check --task-dir T [--oe FILE] [--base MODE] [--json]
  python3.12 -B Task_Authoring/tools/oe_qualifier_check.py backtest [--root DIR] [--base MODE] [--json]
  python3.12 -B Task_Authoring/tools/oe_qualifier_check.py --self-test
--base: auto (default: search when the task's source is ready, else off), off, ids (exact ids only), search (ids and
quotes; skips the Sheets and Snowflake exports), all.
Exit 0 = PASS or WARN, 1 = FAIL, 2 = usage error. Stdlib only. Writes nothing into the task folder.
"""
from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import hashlib
import html
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
WS = BUNDLE.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

TOOL = "oe_qualifier_check"
VERSION = 1
TITLE = "OE QUALIFIER CHECK"
OE_FILE = "08_Oracle_Events.md"
SQL_FILE = "01_Universe_Inject.sql"
POLICY = BUNDLE / "references" / "first_pass_policy.json"

# Thresholds (module constants; none of them is in first_pass_policy.json yet).
MIN_ANCHOR_QUOTE = 12        # a quote shorter than this never selects a record
MIN_BASE_QUOTE = 12          # a quote shorter than this is not searched in the base exports
MIN_BASE_PROBE = 12          # shortest literal run sent to the base text search
MAX_ANCHOR_RECORDS = 4       # a quote found in more records than this is a common phrase, not an anchor
MAX_BASE_QUERIES = 400       # base text probes per run
MAX_BASE_READS = 240         # base records read back per run
BASE_QUERY_LIMIT = 8         # matches kept per base probe
BASE_READ_CHARS = 40000      # characters read per base record (get-many)
BASE_TIMEOUT_S = 1200        # one hg.py call
TEXT_DATE_CAP = 200000       # characters of a record scanned for dates written in its text
LEAD_GAP = 140               # characters between a date or name and the quote it introduces
BASE_HEAVY = ("gsheets", "snowflake")   # exports skipped unless --base all
PARTIAL_SEARCH = {"gmail": "mail bodies break lines inside sentences, so a wrapped quote can be missed",
                  "github": "repository files (code) are not in the searched data.json"}
BASE_FILES = {"slack": "messages/*.json", "linear": "data.json", "github": "data.json", "trello": "data.json",
              "confluence": "confluence_working.json", "gcal": "data.json", "gdrive": "data.json",
              "gdocs": "data.json", "gsheets": "data.json", "gslides": "data.json", "gmail": "threads/*.json",
              "contacts": "contacts.json"}


# ------------------------------------------------------------------ text

_TRANS = {0x2018: "'", 0x2019: "'", 0x201A: "'", 0x201C: '"', 0x201D: '"', 0x00A0: " ", 0x202F: " ", 0x2009: " ",
          0x200B: None, 0x200E: None, 0xFEFF: None}
_DASHES = dict.fromkeys(range(0x2010, 0x2016), "-")
_DASHES[0x2212] = "-"


def norm(value) -> str:
    """Whitespace collapsed, curly quotes straightened. Used for every containment test."""
    return re.sub(r"\s+", " ", str(value).translate(_TRANS)).strip()


def fold(value) -> str:
    """norm() plus case, dash variants, ellipsis and markdown marks removed: a near match, not a match."""
    s = norm(value).casefold().translate(_DASHES).replace("\u2026", "...")
    s = re.sub(r"[*_~`]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def sha256(path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _flatten(value, out, depth=0):
    """Every scalar of a decoded value, depth first, in a stable order."""
    if isinstance(value, dict):
        for key in value:
            _flatten(value[key], out, depth + 1)
    elif isinstance(value, (list, tuple)):
        for item in value:
            _flatten(item, out, depth + 1)
    elif value is not None and not isinstance(value, bool):
        out.append(str(value))


def _decode(value):
    """A JSON column as its decoded value; anything else unchanged."""
    if isinstance(value, str) and value[:1] in "[{" and value[-1:] in "]}":
        try:
            return json.loads(value)
        except ValueError:
            return value
    return value


def _variants(text: str):
    """The stored text plus the text a tool shows: Slack links by their label, HTML without tags."""
    yield text
    shown = text
    if "\\n" in shown or "\\r" in shown or "\\t" in shown:   # escapes kept as text by the SQL (a mail body's \r\n)
        shown = re.sub(r"(?:\\r\\n|\\n|\\r|\\t)+", " ", shown)
    if "<" in text and ">" in text:
        shown = re.sub(r"<(?:https?|mailto):[^|>\s]+\|([^>]+)>", r"\1", shown)
        shown = re.sub(r"[ \t]*<[@!#][A-Za-z0-9_|^-]+>", "", shown)          # a Slack mention a quote may leave out
        if re.search(r"</?[a-zA-Z][^>]*>", shown):
            shown = html.unescape(re.sub(r"</?[a-zA-Z][^>]*>", " ", shown))
    elif "&" in text and re.search(r"&[a-z#0-9]+;", text):
        shown = html.unescape(shown)
    if "*" in shown or "_" in shown or "`" in shown:          # emphasis marks are formatting, not wording
        shown = re.sub(r"(\*\*|__|`)(?=\S)(.+?)(?<=\S)\1", r"\2", shown)
        shown = re.sub(r"(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])", r"\1", shown)
        shown = re.sub(r"(?<![\w_])_(?=\S)([^_\n]+?)(?<=\S)_(?![\w_])", r"\1", shown)
    if shown != text:
        yield shown


# ------------------------------------------------------------------ parsing

RX_HEAD = re.compile(r"^[ \t]*(?:#{1,6}[ \t]*)?(?:\*\*|__)?[ \t]*(?:OE|Oracle[ \t]+Event|Step)[ \t]*#?(\d+)"
                     r"[ \t]*(?:\*\*|__)?[ \t]*[:.)\u2014\u2013-]*[ \t]*(?:\*\*|__)?[ \t]*", re.I)
RX_HEADISH = re.compile(r"^[ \t]*(?:#{1,6}[ \t]*)?(?:\*\*|__)?[ \t]*(?:OE|Oracle[ \t]+Event)\b", re.I)
RX_CUE = re.compile(r"(?:\*\*|__)?\bExpected(?:[ \t]+(?:data|results?|outputs?|values?))?[ \t]*(?:\*\*|__)?[ \t]*"
                    r"(?P<paren>\()?", re.I)
RX_AGENT_FINDS = re.compile(r"\b(?:the[ \t]+)?agent[ \t]+finds\b[ \t]*:?", re.I)

READ_VERBS = frozenset("read find search check list open look confirm query count page get fetch pull view scan "
                       "inspect load locate review see collect gather verify reread run trace follow go browse "
                       "download note".split())
WRITE_VERBS = frozenset("comment move create add assign reply share leave write save set email say send record put "
                        "post make give file update change mark close rename upload edit append delete archive "
                        "invite schedule log attach link tick remove unassign cancel reopen transition build fill "
                        "enter insert paste copy name grant publish draft tell notify answer respond message label "
                        "tag unshare complete finish submit forward".split())
DERIVE_VERBS = frozenset("work apply pick tie total sum settle decide call take derive compute calculate classify "
                         "choose judge tally reconcile map match determine compare sort group rank combine merge "
                         "split filter drop keep exclude rule convert translate".split())
SERVICE_WORDS = (("slack", r"\bslack\b|#[a-z][a-z0-9_-]{2,}|\bDMs?\b"), ("gmail", r"\bgmail\b|\be-?mails?\b|\binbox\b|\bmailbox\b"),
                 ("linear", r"\blinear\b"), ("github", r"\bgithub\b|\bpull requests?\b|\bPRs?\b|\bcommits?\b"),
                 ("trello", r"\btrello\b"), ("confluence", r"\bconfluence\b"),
                 ("gcal", r"\bcalendar\b"), ("gdrive", r"\bdrive\b"), ("gdocs", r"\bdocs?\b"),
                 ("gsheets", r"\bsheets?\b|\bspreadsheet\b"), ("gslides", r"\bslides\b|\bdeck\b|\bpresentation\b"),
                 ("contacts", r"\bcontacts\b"), ("snowflake", r"\bsnowflake\b|\bwarehouse\b"))


def _cue(text: str, start: int = 0):
    """(cue start, expected-text start) of the first Expected cue at or after `start`, or None.

    `Expected (a note with: colons): text` is one cue: the bracket is skipped to its matching close."""
    best = None
    for m in RX_CUE.finditer(text, start):
        pos = m.end()
        if m.group("paren"):
            depth, i = 1, pos
            while i < len(text) and depth:
                depth += {"(": 1, ")": -1}.get(text[i], 0)
                i += 1
            if depth:
                continue
            pos = i
        rest = re.match(r"[ \t]*(?:\*\*|__)?[ \t]*:[ \t]*(?:\*\*|__)?", text[pos:])
        if rest:
            best = (m.start(), pos + rest.end())
            break
    finds = RX_AGENT_FINDS.search(text, start)
    if finds and (best is None or finds.start() < best[0]):
        best = (finds.start(), finds.end())
    return best


def classify(head: str) -> str:
    """read | write | derive | unknown, from the first verb of the call description."""
    words = re.findall(r"[A-Za-z][A-Za-z-]*", head)
    first = words[0].lower().replace("-", "") if words else ""
    nxt = words[1].lower() if len(words) > 1 else ""
    if first == "open" and nxt in ("a", "an", "new", "one"):
        return "write"
    if first == "add" and nxt == "up":
        return "derive"
    if first in ("look", "check", "page") or first in READ_VERBS:
        return "read"
    if first in WRITE_VERBS:
        return "write"
    if first in DERIVE_VERBS:
        return "derive"
    return "unknown"


def services_of(text: str) -> list:
    return [name for name, rx in SERVICE_WORDS if re.search(rx, text, re.I if name != "slack" else 0)
            or (name == "slack" and re.search(r"\bslack\b", text, re.I))]


def parse_events(text: str) -> dict:
    """{'events': [...], 'problems': [...], 'preamble': n}. One event per `OE <n>` heading.

    An event keeps: n, line, head (the call description), expected (text after the cue, or None), kind and services.
    A problem is a block that is not a usable event; the caller reports it, it is never dropped."""
    lines = text.splitlines()
    starts = [(i, RX_HEAD.match(line)) for i, line in enumerate(lines)]
    starts = [(i, m) for i, m in starts if m]
    events, problems = [], []
    first = starts[0][0] if starts else len(lines)
    preamble = sum(1 for line in lines[:first] if line.strip())
    for i, line in enumerate(lines):
        if RX_HEADISH.match(line) and not RX_HEAD.match(line):
            problems.append({"line": i + 1, "what": "a heading that starts like an event but has no number",
                             "text": line.strip()[:80]})
    seen = {}
    for k, (i, m) in enumerate(starts):
        end = starts[k + 1][0] if k + 1 < len(starts) else len(lines)
        number = int(m.group(1))
        body = "\n".join([lines[i][m.end():]] + lines[i + 1:end])
        cue = _cue(body)
        head = (body[:cue[0]] if cue else body).strip()
        expected = body[cue[1]:].strip() if cue else None
        second = _cue(body, cue[1]) if cue else None
        event = {"n": number, "line": i + 1, "head": norm(head), "expected": expected,
                 "kind": classify(head), "services": services_of(head)}
        events.append(event)
        if cue is None:
            problems.append({"line": i + 1, "what": f"OE {number} has no Expected line", "text": norm(head)[:80]})
        elif not expected:
            problems.append({"line": i + 1, "what": f"OE {number} has an empty Expected line", "text": norm(head)[:80]})
        if second:
            problems.append({"line": i + 1, "what": f"OE {number} has more than one Expected cue (all text after "
                                                      "the first is read as one Expected line)", "text": norm(head)[:80]})
        if not head:
            problems.append({"line": i + 1, "what": f"OE {number} has no call description before Expected", "text": ""})
        if number in seen:
            problems.append({"line": i + 1, "what": f"OE {number} appears twice (also line {seen[number]})", "text": ""})
        seen.setdefault(number, i + 1)
    numbers = [e["n"] for e in events]
    if numbers and numbers != sorted(numbers):
        problems.append({"line": events[0]["line"], "what": "event numbers are not in ascending order", "text": ""})
    return {"events": events, "problems": problems, "preamble": preamble}


# ------------------------------------------------------------------ dates

_UTC = dt.timezone.utc
_PT_CACHE = []
MONTHS = {name: i for i, name in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}
DOWS = {name: i for i, name in enumerate("mon tue wed thu fri sat sun".split())}
DOW_NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
_MON = (r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|"
        r"Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)")
_DOW = r"(?:Mon(?:day)?|Tue(?:s(?:day)?)?|Wed(?:nesday)?|Thu(?:r(?:s(?:day)?)?)?|Fri(?:day)?|Sat(?:urday)?|Sun(?:day)?)"
_ZONE = r"(?:PT|PST|PDT|Pacific|UTC|GMT)"
_CLOCK = r"(\d{1,2}):(\d{2})(?::\d{2})?[ \t]*([AaPp]\.?[Mm]\.?)?[ \t]*(" + _ZONE + r"\b)?"
RX_HUMAN = re.compile(r"(?<![A-Za-z])(?:(" + _DOW + r")\.?,?[ \t]+)?(" + _MON + r")\.?[ \t]+(\d{1,2})(?:st|nd|rd|th)?(?![\d:/])"
                      r"(?:,?[ \t]+(20\d{2})(?![\d:]))?(?:,?[ \t]+(?:at[ \t]+)?" + _CLOCK + r")?")
RX_ISO = re.compile(r"(?<![\w-])(20\d{2})-(\d{2})-(\d{2})(?:(?:T|[ \t]+)(\d{2}):(\d{2})(?::\d{2}(?:\.\d+)?)?[ \t]*"
                    r"(Z|" + _ZONE + r"\b)?)?(?![\w-])")
RX_MONTH_YEAR = re.compile(r"(?<![A-Za-z])(" + _MON + r")\.?[ \t]+(20\d{2})(?!\d)")
RX_SLASH = re.compile(r"(?<![\w/.])(\d{1,2})/(\d{1,2})(?:/(\d{2,4}))?(?![\w/])")
RX_TIME_ONLY = re.compile(r"(?<![\d:])" + _CLOCK)
RX_ALT = re.compile(r"[ \t]*\([ \t]*(?:(" + _DOW + r")\.?,?[ \t]+)?(?:(" + _MON + r")\.?[ \t]+(\d{1,2})(?:,?[ \t]+(20\d{2}))?,?[ \t]+)?"
                    + _CLOCK + r"[ \t]*\)")


def pacific():
    if not _PT_CACHE:
        from zoneinfo import ZoneInfo
        _PT_CACHE.append(ZoneInfo("America/Los_Angeles"))
    return _PT_CACHE[0]


def _zone(raw):
    if not raw:
        return None
    return "UTC" if raw.upper() in ("UTC", "GMT", "Z") else "PT"


def _hour(hour, ampm):
    hour = int(hour)
    if ampm:
        pm = ampm.lower().startswith("p")
        hour = hour % 12 + (12 if pm else 0)
    return hour


def _date_qual(text, start, end, **kw) -> dict:
    q = {"kind": "date", "text": text[start:end].strip(), "start": start, "end": end, "y": None, "m": None, "d": None,
         "hh": None, "mi": None, "zone": None, "dow": None, "alt": None}
    q.update(kw)
    return q


def find_dates(text: str, taken=()) -> list:
    """Date and time qualifiers in `text`, left to right. `taken` are spans to leave alone (quotes)."""
    def free(a, b):
        return not any(a < y and x < b for x, y in used)

    used, out = list(taken), []
    for m in RX_ISO.finditer(text):
        if not free(*m.span()):
            continue
        y, mo, d, hh, mi, z = m.groups()
        if not (1 <= int(mo) <= 12 and 1 <= int(d) <= 31):
            continue
        q = _date_qual(text, m.start(), m.end(), y=int(y), m=int(mo), d=int(d))
        if hh is not None and int(hh) < 24 and int(mi) < 60:
            q.update(hh=int(hh), mi=int(mi), zone=_zone(z) or ("UTC" if text[m.start() + 10:m.start() + 11] == "T" else None))
        out.append(q)
        used.append(m.span())
    for m in RX_HUMAN.finditer(text):
        if not free(*m.span()):
            continue
        dow, mon, day, year, hh, mi, ampm, z = m.groups()
        if not 1 <= int(day) <= 31:
            continue
        end = m.end()
        q = _date_qual(text, m.start(), end, y=int(year) if year else None, m=MONTHS[mon[:3].lower()], d=int(day),
                       dow=DOWS[dow[:3].lower()] if dow else None)
        if hh is not None and int(mi) < 60 and _hour(hh, ampm) < 24:
            q.update(hh=_hour(hh, ampm), mi=int(mi), zone=_zone(z))
        alt = RX_ALT.match(text, end)
        if alt and q["hh"] is not None:
            adow, amon, aday, ayear, ahh, ami, aampm, az = alt.groups()
            q["alt"] = {"dow": DOWS[adow[:3].lower()] if adow else None, "m": MONTHS[amon[:3].lower()] if amon else None,
                        "d": int(aday) if aday else None, "y": int(ayear) if ayear else None,
                        "hh": _hour(ahh, aampm), "mi": int(ami), "zone": _zone(az)}
            end = alt.end()
            q.update(end=end, text=text[m.start():end].strip())
        out.append(q)
        used.append((m.start(), end))
    for m in RX_MONTH_YEAR.finditer(text):
        if free(*m.span()):
            out.append(_date_qual(text, m.start(), m.end(), y=int(m.group(2)), m=MONTHS[m.group(1)[:3].lower()]))
            used.append(m.span())
    for m in RX_SLASH.finditer(text):
        mo, d, y = m.groups()
        if free(*m.span()) and 1 <= int(mo) <= 12 and 1 <= int(d) <= 31:
            year = None if y is None else (2000 + int(y) if len(y) == 2 else int(y))
            out.append(_date_qual(text, m.start(), m.end(), y=year, m=int(mo), d=int(d), slash=True))
            used.append(m.span())
    for m in RX_TIME_ONLY.finditer(text):
        hh, mi, ampm, z = m.groups()
        if free(*m.span()) and (ampm or z) and int(mi) < 60 and _hour(hh, ampm) < 24:
            out.append(_date_qual(text, m.start(), m.end(), hh=_hour(hh, ampm), mi=int(mi), zone=_zone(z)))
            used.append(m.span())
    out.sort(key=lambda q: q["start"])
    return out


def _valid(y, m, d) -> bool:
    try:
        dt.date(y, m, d)
        return True
    except ValueError:
        return False


def _instant(y, m, d, hh, mi, zone):
    local = dt.datetime(y, m, d, hh, mi)
    if zone == "PT":
        return local.replace(tzinfo=pacific()).astimezone(_UTC)
    return local.replace(tzinfo=_UTC)


def show_instant(t) -> str:
    local = t.astimezone(pacific())
    return (f"{t.strftime('%Y-%m-%d %H:%M')} UTC ({local.strftime('%a %b')} {local.day} {local.year} "
            f"{local.strftime('%I:%M %p').lstrip('0')} PT)")


def date_self_check(q) -> str | None:
    """Why the date contradicts itself (weekday against the date, PT against UTC), or None."""
    if q["m"] and q["d"] and q["y"] and not _valid(q["y"], q["m"], q["d"]):
        return f"{q['y']}-{q['m']:02d}-{q['d']:02d} is not a calendar date"
    if q["dow"] is not None and q["y"] and q["m"] and q["d"]:
        real = dt.date(q["y"], q["m"], q["d"]).weekday()
        if real != q["dow"]:
            return f"{q['y']}-{q['m']:02d}-{q['d']:02d} is a {DOW_NAMES[real]}, not a {DOW_NAMES[q['dow']]}"
    alt = q.get("alt")
    if alt and q["y"] and q["zone"] and alt["zone"] and alt["zone"] != q["zone"]:
        main = _instant(q["y"], q["m"], q["d"], q["hh"], q["mi"], q["zone"])
        there = main.astimezone(pacific() if alt["zone"] == "PT" else _UTC)
        wrong = (there.hour, there.minute) != (alt["hh"], alt["mi"])
        if alt["m"] and alt["d"] and (there.month, there.day) != (alt["m"], alt["d"]):
            wrong = True
        if alt["dow"] is not None and there.weekday() != alt["dow"]:
            wrong = True
        if wrong:
            return (f"{q['hh']:02d}:{q['mi']:02d} {q['zone']} on {q['y']}-{q['m']:02d}-{q['d']:02d} is "
                    f"{there.strftime('%a %b')} {there.day} {there.strftime('%H:%M')} {alt['zone']}")
    return None


def date_matches(q, when, has_time=True) -> bool:
    """Does the qualifier agree with a record time?

    A dated time must be the record's minute in the zone it names (either zone when it names none); the minute may be
    the record's time cut to the minute (what Slack and Gmail show) or rounded to it. A day accepts the UTC day and the
    Pacific day, as task_context.date_acceptance does. A year is compared only when written."""
    y, m, d = q["y"], q["m"], q["d"]
    if q["hh"] is not None and has_time:
        for zone in ([q["zone"]] if q["zone"] else ["PT", "UTC"]):
            for t in (when, when + dt.timedelta(seconds=30)):
                v = t.astimezone(pacific() if zone == "PT" else _UTC)
                if (v.hour, v.minute) != (q["hh"], q["mi"]):
                    continue
                if m is None or (v.month == m and v.day == d and y in (None, v.year)):
                    return True
        return False
    if m is None:
        return False
    views = [when.astimezone(_UTC), when.astimezone(pacific())] if has_time else [when]
    return any(v.month == m and (d is None or v.day == d) and y in (None, v.year) for v in views)


def minute_precise(when, has_time) -> bool:
    """Is a stored time known to the minute? A day-only value is not, and neither is an exact UTC midnight
    (`2025-09-30T00:00:00Z`), which seeded rows use for a day."""
    return bool(has_time) and (when.hour, when.minute, when.second, when.microsecond) != (0, 0, 0, 0)


def date_conflict(q, when, has_time):
    """Why a record time contradicts the date, or None when they agree or cannot be compared.

    The rule (conservative): a clock time is compared to the minute only when the record's time is known to the
    minute (minute_precise). Against a day-only value the clock time is dropped and the day is compared: it
    contradicts only when neither the UTC day nor the Pacific day of the record is the stated day."""
    if date_matches(q, when, has_time):
        return None
    if q["hh"] is not None and minute_precise(when, has_time):
        zone = q["zone"] or "PT or UTC"
        return f"the record's time is {show_instant(when)}, not {q['hh']:02d}:{q['mi']:02d} {zone}"
    if q["m"] is None:
        return None                                   # a bare clock time against a day: nothing to compare
    day = dict(q, hh=None, mi=None, zone=None)
    if date_matches(day, when, has_time):
        return None                                   # the day agrees; the record does not hold the minute
    shown = show_instant(when) if has_time else when.date().isoformat()
    said = dt.date(2000, q["m"], 1).strftime("%b") + (f" {q['d']}" if q["d"] else "") + (f" {q['y']}" if q["y"] else "")
    return f"the record's day is {shown}, not {said}"


def parse_when(key: str, value):
    """(aware UTC datetime, has_time) for a stored time value, or None."""
    key = key.lower()
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        timey = any(t in key for t in ("ts", "time", "date", "_at", "created", "updated", "start", "end", "due"))
        if timey and 1e9 < value < 2.2e9:
            return dt.datetime.fromtimestamp(float(value), tz=_UTC), True
        if timey and 1e12 < value < 2.2e12:
            return dt.datetime.fromtimestamp(value / 1000.0, tz=_UTC), True
        return None
    if not isinstance(value, str) or not value or len(value) > 40:
        return None
    text = value.strip()
    if re.fullmatch(r"\d{10}(?:\.\d{1,9})?", text) and (key in ("ts", "latest_reply", "thread_ts", "thread_ts_legacy")
                                                         or "ts" in key.split("_") or "date" in key or "time" in key):
        return dt.datetime.fromtimestamp(float(text), tz=_UTC), True
    if re.fullmatch(r"\d{13}", text) and ("date" in key or "time" in key or "ts" in key):
        return dt.datetime.fromtimestamp(int(text) / 1000.0, tz=_UTC), True
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        try:
            day = dt.date.fromisoformat(text)
        except ValueError:
            return None
        return dt.datetime(day.year, day.month, day.day, tzinfo=_UTC), False
    if re.match(r"\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}", text):
        try:
            when = dt.datetime.fromisoformat(text.replace("Z", "+00:00").replace(" ", "T", 1))
        except ValueError:
            return None
        return (when.replace(tzinfo=_UTC) if when.tzinfo is None else when.astimezone(_UTC)), True
    if re.match(r"(?:[A-Z][a-z]{2}, )?\d{1,2} [A-Z][a-z]{2} \d{4} \d{2}:\d{2}", text):
        try:
            when = email.utils.parsedate_to_datetime(text)
        except (TypeError, ValueError):
            return None
        return (when.replace(tzinfo=_UTC) if when.tzinfo is None else when.astimezone(_UTC)), True
    return None


# ------------------------------------------------------------------ records

KEY_COLUMNS = ("id", "identifier", "ts", "event_id", "document_id", "spreadsheet_id", "presentation_id", "sha",
               "contact_id", "shortLink", "ical_uid", "object_id")
TITLE_COLUMNS = ("title", "name", "summary", "subject")
AUTHOR_COLUMNS = ("user_id", "user", "author_id", "author_login", "from_email", "idMemberCreator", "creator_id",
                  "organizer_email", "owner_email", "actor_login", "creator_email")
PRIMARY_TIME = ("ts", "internal_date", "submitted_at", "date", "created_at", "created", "created_time", "start_ts")
ROLE_FIELDS = {"created": ("created_at", "created", "created_time", "ts", "date", "internal_date", "authored_date"),
               "modified": ("updated_at", "updated", "modified_time", "dateLastActivity"),
               "starts": ("start_ts", "start_json", "start", "start_date"),
               "ends": ("end_ts", "end_json", "end"),
               "due": ("due", "due_date", "target_date"),
               "merged": ("merged_at",), "closed": ("closed_at", "completed_at", "canceled_at"),
               "sent": ("internal_date", "date", "ts", "created_at"), "submitted": ("submitted_at",)}
ROLE_WORDS = (("created", r"created|opened|filed|written|authored"),
              ("modified", r"(?:last[ \t]+)?(?:changed|edited|modified|updated)"),
              ("starts", r"starts?|starting|begins?"), ("ends", r"ends?|ending"), ("due", r"due"),
              ("merged", r"merged"), ("closed", r"closed|completed|canceled|cancelled"),
              ("sent", r"sent|posted|received"), ("submitted", r"submitted"))
STATE_COLUMNS = ("state_id", "state", "status")
FAMILY_COLUMNS = ("spreadsheet_id", "document_id", "presentation_id", "drive_file_id", "id")
MESSAGE_TABLES = ("slack_messages", "linear_comments", "github_pr_comments", "github_review_comments",
                  "github_reviews", "trello_actions", "confluence_comments", "gmail_messages", "messages",
                  "comments", "pull_request_comments", "review_comments", "reviews", "actions")


class Record:
    """One record: an injected row (final state after the SQL's UPDATEs) or a base record."""

    def __init__(self, table, fields, source, line=None, where=None, partial=False):
        self.table, self.fields, self.source, self.line, self.where, self.partial = table, fields, source, line, where, partial
        self._text = self._plain = self._folded = self._times = self._dates = self._dashed = None

    @property
    def short(self) -> str:
        return self.table.split(".")[-1]

    @property
    def rid(self) -> str:
        f = self.fields
        if "ts" in f and (f.get("channel_id") or f.get("channel")):
            key = f"{f.get('channel_id') or f.get('channel')}/{f['ts']}"
        else:
            key = next((str(f[c]) for c in ("identifier", "id", "event_id", "document_id", "spreadsheet_id",
                                           "presentation_id", "sha", "contact_id") if f.get(c)), "?")
            if self.short.endswith("pull_requests") and f.get("number") is not None and "#" not in key:
                key += f"#{f['number']}"
        where = f"SQL L{self.line}" if self.source.startswith("sql") else f"base {self.where or ''}".strip()
        return f"{self.short}:{key} ({where}{', UPDATE only' if self.source == 'sql-update' else ''})"

    @property
    def text(self) -> str:
        if self._text is None:
            parts = []
            for value in self.fields.values():
                scalars = []
                _flatten(_decode(value), scalars)
                for s in scalars:
                    for variant in _variants(s):
                        parts.append(norm(variant))
            self._text = "\n".join(p for p in parts if p)
        return self._text

    @property
    def plain(self) -> str:
        """The text with thousands separators dropped, for figures."""
        if self._plain is None:
            self._plain = re.sub(r"(?<=\d),(?=\d{3}\b)", "", self.text)
        return self._plain

    @property
    def folded(self) -> str:
        if self._folded is None:
            self._folded = fold(self.text)
        return self._folded

    @property
    def keys(self) -> list:
        f, out = self.fields, []
        for c in KEY_COLUMNS:
            if f.get(c) not in (None, ""):
                out.append(str(f[c]))
        if f.get("ts") and (f.get("channel_id") or f.get("channel")):
            out.append(f"{f.get('channel_id') or f.get('channel')}/{f['ts']}")
        for c in ("number", "idShort"):
            if f.get(c) not in (None, ""):
                out.append(f"#{f[c]}")
        if self.short == "contacts" and f.get("email"):
            out.append(str(f["email"]))
        return out

    @property
    def times(self) -> list:
        """[(field, UTC datetime, has_time)] for every stored time, JSON columns included."""
        if self._times is None:
            out = []
            for key, value in self.fields.items():
                decoded = _decode(value)
                items = [(key, decoded)]
                if isinstance(decoded, dict):
                    items = [(f"{key}.{k}", v) for k, v in decoded.items()]
                for name, v in items:
                    got = parse_when(name if "." not in name else key + "_date", v)
                    if got:
                        out.append((name, got[0], got[1]))
            oid = str(self.fields.get("id") or "")
            if "trello" in self.table and re.fullmatch(r"[0-9a-f]{24}", oid) and 1.2e9 < int(oid[:8], 16) < 2.2e9:
                out.append(("id (creation time)", dt.datetime.fromtimestamp(int(oid[:8], 16), tz=_UTC), True))
            self._times = out
        return self._times

    @property
    def text_dates(self) -> list:
        if self._dates is None:
            self._dates = find_dates(self.text[:TEXT_DATE_CAP])
        return self._dates

    def primary_time(self):
        for name in PRIMARY_TIME:
            for field, when, has_time in self.times:
                if field == name:
                    return field, when, has_time
        return None

    def message_like(self) -> bool:
        return self.short in MESSAGE_TABLES and self.primary_time() is not None

    def author_tokens(self) -> list:
        return [str(self.fields[c]) for c in AUTHOR_COLUMNS if self.fields.get(c)]

    def state(self):
        """(column, state name), or None. A raw state id (`state_5599a57e…`) is not a name and is never compared."""
        for c in STATE_COLUMNS:
            value = self.fields.get(c)
            if isinstance(value, str) and value and not re.fullmatch(r"(?:state|wfs|st)_[0-9a-f]{6,}", value):
                return c, value
        return None

    def has(self, needle: str) -> bool:
        return needle in self.text


FAMILY_TABLES = ("slides_page_elements", "docs_", "sheets_", "slides_pages")


def family_records(records) -> list:
    """One extra record per injected file whose text is split over several rows (a deck's text boxes, a doc's
    sections): the prose of its rows in SQL order, so a quote that runs across two text boxes is found."""
    groups, order = {}, []
    for rec in records:
        if rec.partial or not any(rec.short.startswith(t) or rec.short == t for t in FAMILY_TABLES):
            continue
        key = next((str(rec.fields[c]) for c in ("presentation_id", "document_id", "spreadsheet_id") if rec.fields.get(c)), None)
        if not key:
            continue
        if key not in groups:
            groups[key] = []
            order.append(key)
        groups[key].append(rec)
    out = []
    for key in order:
        rows = groups[key]
        if len(rows) < 2:
            continue
        prose = []
        for rec in rows:
            for value in rec.fields.values():
                if isinstance(value, str) and len(value) >= 12 and " " in value and not value.lstrip().startswith(("{", "[")):
                    prose.append(value)
        if prose:
            fam = Record(rows[0].table.rsplit(".", 1)[0] + ".file_text", {"id": key, "text": "\n".join(prose)}, "sql",
                         line=rows[0].line)
            out.append(fam)
    return out


class SqlIndex:
    """The injection SQL as records. Parsed as text with base_check.parse_sql; nothing is executed."""

    def __init__(self, sql_text: str):
        from base_check import parse_sql
        self.records, self.updates = [], []
        inserted = {}
        statements = parse_sql(sql_text or "")
        for st in statements:
            if st["op"] == "insert":
                rec = Record(st["table"], dict(st["row"]), "sql", line=st["line"])
                self.records.append(rec)
                for c in ("id", "identifier", "spreadsheet_id", "contact_id", "event_id", "document_id"):
                    if rec.fields.get(c):
                        inserted.setdefault((st["table"], c, str(rec.fields[c])), []).append(rec)
        for st in statements:
            if st["op"] not in ("update", "delete") or not st.get("where"):
                continue
            targets = None
            for col, val in st["where"].items():
                hit = inserted.get((st["table"], col, val)) or inserted.get((st["table"], "id", val), [])
                targets = hit if targets is None else [r for r in targets if r in hit]
            if st["op"] == "delete":                       # a deleted injected row supports nothing
                self.records = [r for r in self.records if r not in (targets or [])]
                continue
            if targets:
                for rec in targets:
                    rec.fields.update(st["set"])
                    rec._text = rec._plain = rec._folded = rec._times = rec._dates = rec._dashed = None
            else:
                fields = dict(st["where"])
                fields.update(st["set"])
                self.records.append(Record(st["table"], fields, "sql-update", line=st["line"], partial=True))
                self.updates.append((st["table"], dict(st["where"]), dict(st["set"])))
        self.families = family_records(self.records)
        self.by_key, self.by_title = {}, {}
        for rec in self.records:
            for key in rec.keys:
                if rec not in self.by_key.setdefault(key, []):
                    self.by_key[key].append(rec)
            for c in TITLE_COLUMNS:
                title = rec.fields.get(c)
                if isinstance(title, str) and len(title) >= 4:
                    self.by_title.setdefault(norm(title), []).append(rec)

    def containing(self, needle: str) -> list:
        return [r for r in self.records if needle in r.text]

    def overlay(self, table_short: str, fields: dict) -> dict:
        """A base record with the SQL's UPDATEs of that row applied (the state the agent reads)."""
        for table, where, sets in self.updates:
            if table.split(".")[-1].endswith(table_short) or table_short.endswith(table.split(".")[-1].split("_", 1)[-1]):
                if all(str(fields.get(c)) == v for c, v in where.items()):
                    fields = dict(fields)
                    fields.update(sets)
        return fields


# ------------------------------------------------------------------ base records (through tools/hg.py)

def _run_hg(task_dir, args: list, request: dict):
    """One hg.py helper call with a JSON request file. Returns (parsed stdout or None, error text or None)."""
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("oe_qualifier_") as tmp:
        path = Path(tmp) / "request.json"
        path.write_text(json.dumps(request, ensure_ascii=False))
        cmd = [sys.executable, "-B", str(HERE / "hg.py"), "--task-dir", str(task_dir)] + args + ["--request", str(path)]
        try:
            run = subprocess.run(cmd, capture_output=True, text=True, timeout=BASE_TIMEOUT_S)
        except (OSError, subprocess.TimeoutExpired) as exc:
            return None, f"tools/hg.py {args[0]}: {exc}"
    try:
        return json.loads(run.stdout), None
    except ValueError:
        return None, f"tools/hg.py {' '.join(args[:2])} exit {run.returncode}: {(run.stderr or run.stdout).strip()[-200:]}"


class BaseReader:
    """Base records for the task's universe, read only through tools/hg.py. `runner` is replaceable in tests."""

    def __init__(self, task_dir, mode: str, sql: SqlIndex, runner=None):
        self.task_dir, self.mode, self.sql = task_dir, mode, sql
        self.runner = runner or _run_hg
        self.calls, self.errors, self.skipped = 0, [], []
        self.by_key, self.cache, self.searched = {}, {}, {}

    def enabled(self) -> bool:
        return self.mode in ("ids", "search", "all")

    def _call(self, args, request):
        """One helper call. Any failure (no base data, a crash in the helper, bad output) becomes an error line, so a
        base read the tool could not make reads as unverifiable, never as a crash."""
        try:
            doc, err = self.runner(self.task_dir, args, request)
        except Exception as exc:                              # the runner is replaceable; never let it stop the check
            return None, f"tools/hg.py {' '.join(args[:2])}: {type(exc).__name__}: {str(exc)[:160]}"
        return doc, err

    def _record(self, service, collection, fields, where) -> Record:
        table = f"{service}.{collection}"
        return Record(table, self.sql.overlay(collection, fields), "base", where=where)

    def lookup(self, wanted: dict) -> None:
        """wanted: {kind: set of values}. Kinds: ticket, slack_ts, channel, pr, sha, drive, gcal."""
        if not self.enabled():
            return
        checks, routes = [], {}

        def add(cid, service, file, pointer, field, values, collection):
            values = sorted(values)
            if values:
                checks.append({"id": cid, "service": service, "file": file, "pointer": pointer, "field": field, "values": values})
                routes[cid] = (service, collection)

        add("ticket", "linear", "data.json", "/issues", "identifier", wanted.get("ticket", ()), "linear_issues")
        add("channel", "slack", "channels.json", "", "name", wanted.get("channel", ()), "slack_channels")
        add("pr", "github", "data.json", "/pull_requests", "number", wanted.get("pr", ()), "github_pull_requests")
        add("sha", "github", "data.json", "/commits", "sha", wanted.get("sha", ()), "github_commits")
        add("drive", "gdrive", "data.json", "/drive_files", "id", wanted.get("drive", ()), "drive_files")
        add("gcal", "gcal", "data.json", "/events", "event_id", wanted.get("gcal", ()), "gcal_events")
        add("usr", "linear", "data.json", "/users", "id", wanted.get("usr", ()), "linear_users")
        add("contact", "contacts", "contacts.json", "/contacts", "email", wanted.get("contact", ()), "contacts")
        months = {}
        for ts in wanted.get("slack_ts", ()):
            when = dt.datetime.fromtimestamp(float(ts), tz=_UTC)
            for shift in (-1, 0, 1):
                months.setdefault((when + dt.timedelta(days=shift)).strftime("%Y-%m"), set()).add(ts)
        for month in sorted(months):
            add(f"ts-{month}", "slack", f"messages/*/{month}.json", "", "ts", months[month], "slack_messages")
        if not checks:
            return
        self.calls += 1
        doc, err = self._call(["records"], {"checks": checks})
        if err or not isinstance(doc, dict) or not isinstance(doc.get("checks"), dict):
            self.errors.append(err or "tools/hg.py records returned no checks")
            return
        for cid, check in doc["checks"].items():
            service, collection = routes.get(cid, ("?", "?"))
            if check.get("scan_complete") is not True:
                self.errors.append(f"base {service} {collection}: scan incomplete ({str(check.get('errors'))[:120]})")
            for match in check.get("matches") or []:
                rec = match.get("record")
                if not isinstance(rec, dict):
                    continue
                where = f"{Path(str(match.get('file', ''))).name}{match.get('pointer', '')}"
                if service == "slack" and collection == "slack_messages":
                    channel = Path(str(match.get("file", ""))).parent.name
                    rec = dict(rec, channel=rec.get("channel") or channel)
                    where = f"{channel}/{where}"
                record = self._record(service, collection, rec, where)
                key = str(match.get("value"))
                self.by_key.setdefault(f"#{key}" if cid == "pr" else key, []).append(record)
                for k in record.keys:
                    if record not in self.by_key.setdefault(k, []):
                        self.by_key[k].append(record)

    def search(self, service: str, probes: dict) -> None:
        """probes: {probe text: full normalised quote}. Fills self.searched[(service, quote)] = [Record]."""
        if self.mode not in ("search", "all") or service not in BASE_FILES:
            return
        if service in BASE_HEAVY and self.mode != "all":
            self.skipped.append(service)
            return
        todo = {p: q for p, q in probes.items() if (service, q) not in self.searched}
        if not todo:
            return
        order = sorted(todo)
        request = {"service": service, "file": BASE_FILES[service],
                   "queries": [{"id": f"q{i}", "query": probe, "limit": BASE_QUERY_LIMIT} for i, probe in enumerate(order)]}
        self.calls += 1
        doc, err = self._call(["search", "search-many", "--compact"], request)
        for probe in order:
            self.searched.setdefault((service, todo[probe]), [])
        if err or not isinstance(doc, dict) or not isinstance(doc.get("queries"), dict):
            self.errors.append(err or f"tools/hg.py search-many {service} returned no queries")
            return
        reads, owners = {}, {}
        for i, probe in enumerate(order):
            for match in (doc["queries"].get(f"q{i}") or {}).get("matches") or []:
                file, pointer = match.get("service_file"), str(match.get("pointer") or "")
                parts, keep = pointer.split("/"), []
                for part in parts:
                    keep.append(part)
                    if part.isdigit():
                        break
                target = (file, "/".join(keep))
                if file and target not in self.cache and len(reads) + len(self.cache) < MAX_BASE_READS:
                    reads[target] = None
                owners.setdefault(target, set()).add(todo[probe])
        targets = sorted(reads)
        for chunk in range(0, len(targets), 12):
            batch = targets[chunk:chunk + 12]
            items = [{"id": f"r{j}", "service": service, "file": f, "pointer": p, "max_chars": BASE_READ_CHARS}
                     for j, (f, p) in enumerate(batch)]
            self.calls += 1
            got, err = self._call(["search", "get-many", "--compact"], {"items": items})
            if not isinstance(got, dict) or not isinstance(got.get("items"), dict):
                self.errors.append(err or f"tools/hg.py get-many {service} returned no items")
                continue
            for j, (f, p) in enumerate(batch):
                item = got["items"].get(f"r{j}") or {}
                text = item.get("text")
                if not isinstance(text, str):
                    continue
                collection = (p.strip("/").split("/")[0] if not p.strip("/").split("/")[0].isdigit() else Path(f).parent.name or Path(f).stem)
                collection = {"issues": "linear_issues", "comments": f"{service}_comments", "cards": "trello_cards",
                              "actions": "trello_actions", "pages": "confluence_pages", "events": "gcal_events",
                              "pull_requests": "github_pull_requests", "commits": "github_commits",
                              "messages": f"{service}_messages"}.get(collection, collection)
                if service == "slack" and f.startswith("messages/"):
                    collection = "slack_messages"
                try:
                    fields = json.loads(text) if not item.get("truncated") else {"text": text}
                except ValueError:
                    fields = {"text": text}
                if not isinstance(fields, dict):
                    fields = {"value": fields}
                if service == "slack" and collection == "slack_messages" and "channel" not in fields:
                    fields["channel"] = Path(f).parent.name
                self.cache[(f, p)] = self._record(service, collection, fields, f"{f}{p}")
                self.cache[(f, p)].partial = bool(item.get("truncated"))
        for target, quotes in owners.items():
            rec = self.cache.get(target)
            if rec is None:
                continue
            for quote in quotes:
                if (quote_in(quote, rec) or quote_dashed(quote, rec)) and rec not in self.searched[(service, quote)]:
                    self.searched[(service, quote)].append(rec)

    def all_records(self) -> list:
        seen, out = set(), []
        for group in list(self.by_key.values()) + [[r] for r in self.cache.values()]:
            for rec in group:
                if id(rec) not in seen:
                    seen.add(id(rec))
                    out.append(rec)
        return out


# ------------------------------------------------------------------ people (author check)

class People:
    """Service ids, emails and names of the universe's people, from the universe KB (entities.json). Optional."""

    def __init__(self, path=None, data=None):
        self.token, self.names, self.first = {}, {}, {}
        if data is None:
            if not path or not Path(path).is_file():
                return
            try:
                data = json.loads(Path(path).read_text())
            except (OSError, ValueError):
                return
        if not isinstance(data, dict):
            return
        for ent in data.get("entities") or []:
            if not isinstance(ent, dict) or ent.get("kind") != "person" or not ent.get("canonical_name"):
                continue
            eid = ent["entity_id"]
            names = {norm(n).casefold() for n in (ent.get("names") or []) + [ent["canonical_name"]] if n}
            self.names[eid] = (ent["canonical_name"], names)
            for value in ent.get("emails") or []:
                self.token[str(value).casefold()] = eid
            for rows in (ent.get("identities") or {}).values():
                for row in rows:
                    for key in ("id", "login", "email", "mailbox", "calendar_id", "username", "account_id", "contact_id"):
                        if isinstance(row.get(key), str) and row[key]:
                            self.token[row[key].casefold()] = eid
        counts = {}
        for eid, (canonical, _) in self.names.items():
            counts.setdefault(canonical.split()[0].casefold(), []).append(eid)
        self.first = {first: ids[0] for first, ids in counts.items() if len(ids) == 1}

    def known(self, name: str) -> bool:
        """Is this (full or first) name the name of a person in the universe?"""
        key = norm(name).casefold()
        return any(key in names or key in {n.split()[0] for n in names} for _, names in self.names.values())

    def matches(self, eid, name: str) -> bool:
        key = norm(name).casefold()
        names = self.names.get(eid, ("", set()))[1]
        return key in names or key in {n.split()[0] for n in names} or key in {n.split()[-1] for n in names}

    def by_token(self, token: str):
        return self.token.get(str(token).casefold())

    def label(self, eid) -> str:
        return self.names.get(eid, ("?",))[0]


# ------------------------------------------------------------------ qualifier extraction

RX_OE_REF = re.compile(r"\bOEs?[ \t]*\d+(?:[ \t]*(?:[-\u2013+,&]|and|to|or|through)[ \t]*(?:OEs?[ \t]*)?\d+)*", re.I)
RX_TICKET = re.compile(r"\b[A-Z][A-Z0-9]{1,9}-\d{1,6}\b")
LITERALS = (("code", re.compile(r"`([^`\n]+)`")),
            ("email", re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")),
            ("id", re.compile(r"(?<![\w.-])[A-Za-z0-9]+(?:_[A-Za-z0-9]+)+(?!\w)")),
            ("ticket", RX_TICKET),
            ("id", re.compile(r"\b(?=[A-Z0-9]*\d)(?=[A-Z0-9]*[A-Z])[A-Z0-9]{9,12}\b")),
            ("sha", re.compile(r"\b(?=[0-9a-f]*\d)(?=[0-9a-f]*[a-f])[0-9a-f]{7,40}\b")),
            ("id", re.compile(r"(?<![\w.])\d{10,}(?:\.\d+)?(?!\w|\.\w)")),
            ("version", re.compile(r"(?<![\w.])\d+\.\d+\.\d+(?:\.\d+)?(?!\w|\.\w)")),
            ("channel", re.compile(r"(?<![\w#])#[a-z][a-z0-9_-]{2,}\b")))
RX_MONEY = re.compile(r"(?:[$\u20ac\u00a3][ \t]?\d(?:[\d,]*\d)?(?:\.\d+)?(?:[ \t]?[kKmM]\b)?)|(?:\b\d(?:[\d,]*\d)?(?:\.\d+)?[ \t]?(?:USD|EUR|GBP|TRY|BGN)\b)")
RX_PERCENT = re.compile(r"\b\d(?:[\d,]*\d)?(?:\.\d+)?[ \t]?%")
RX_HASHNUM = re.compile(r"(?<![\w#])#\d{1,6}\b")
RX_NUMBER = re.compile(r"(?<![\w.,:$#/*-])\d(?:[\d,]*\d)?(?:\.\d+)?(?![\w%:/]|[.,-]\d)")
NUMBER_WORDS = {"no": 0, "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
                "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12}
COUNT_NOUNS = ("rows?|issues?|tickets?|comments?|repl(?:y|ies)|messages?|posts?|lines?|items?|cards?|children|tabs?|"
               "files?|docs?|documents?|events?|attendees?|people|names?|firms?|angels?|accounts?|invoices?|mails?|"
               "e-?mails?|threads?|results?|match(?:es)?|hits?|PRs?|pull requests?|commits?|reviews?|members?|"
               "entries|entry|records?|checklists?|columns?|pages?|slides?|versions?|builds?|creatives?|payments?|"
               "notices?|receipts?|transfers?|holders?|grants?|projects?|sheets?|folders?|contacts?|payees?|"
               "vendors?|subscriptions?|charges?|surfaces?|sub-?issues?|bugs?|labels?|lists?|boards?|channels?|"
               "calls?|meetings?|recipients?|steps?|notes?|wires?|runs?|items?|tests?|levels?|tiers?|sets?|ads?|videos?|stills?|icons?")
RX_COUNT = re.compile(r"(?<![\w.,:$#/-])(?P<num>\d(?:[\d,]*\d)?|" + "|".join(NUMBER_WORDS) + r")[ \t]+(?P<mid>(?:[A-Za-z][\w'-]*[ \t]+){0,2}?)"
                      r"(?P<noun>" + COUNT_NOUNS + r")\b", re.I)
ENUM_BEFORE = re.compile(r"(?:\b(?:rule|test|step|line|lines|row|rows|tier|tiers|level|levels|slide|page|chapter|no|"
                         r"number|item|section|part|version|v|build|submission|round|phase|day|week|q|top|tab|"
                         r"position|of|to|or|and|through|than|under|over|above|below|least|most|about|around|by|"
                         r"cpm|=|>|<|x)[ \t.]*)$", re.I)
STOP_UNITS = frozenset("in with of to on at by for and or from are is were was as that which per each the a an off out "
                       "up down over under more less total plus minus times vs not no so if then than but also all both "
                       "when while after before until since through into onto it its they them this these those "
                       "has have had will would can could may might must should do does did be been being".split())
RX_SUPERLATIVE = re.compile(r"\b(?P<word>only|sole|single|latest|newest|oldest|earliest|most[ \t]+recent|first|last)"
                            r"[ \t]+(?P<mid>(?:[\w'-]+[ \t]+){0,2}?)(?P<noun>messages?|posts?|repl(?:y|ies)|comments?|"
                            r"e-?mails?|mails?|threads?|tickets?|issues?|cards?|docs?|documents?|sheets?|rows?|lines?|"
                            r"entry|entries|versions?|reviews?|commits?|builds?|events?|meetings?|invoices?|charges?|"
                            r"payments?|updates?|edits?|changes?|notes?|instructions?|one|match(?:es)?|results?|hits?|"
                            r"records?|files?|pages?|PRs?|pull requests?|run|deploy|deploys|answer|word|call|holder)\b", re.I)
RX_ABSENCE = re.compile(r"\b(?:none|nothing|nobody|no[ \t]+one|nowhere|never|absent|missing|not[ \t]+found|"
                        r"no[ \t]+(?:other|such|later|further|newer|known|records?|fix(?:es)?|commits?|follow-ups?|"
                        r"repl(?:y|ies)|response|evidence|trace|mention)|do(?:es)?[ \t]+not[ \t]+exist|"
                        r"do(?:es)?n't[ \t]+exist|no[ \t]+longer[ \t]+exists?)\b", re.I)
RX_REPLIES = re.compile(r"\b(?:(?P<num>no|zero|one|two|three|four|five|six|seven|eight|nine|ten|\d+)[ \t]+"
                        r"(?:thread[ \t]+|threaded[ \t]+)?repl(?:y|ies)\b)", re.I)
STATE_WORDS = ("Backlog", "Todo", "In Progress", "In Review", "In Validation", "Validation", "Regression", "Done",
               "Canceled", "Cancelled", "Duplicate", "Bugs", "Triage", "PR")
RX_ALL_STATE = re.compile(r"\b(?i:all|each|every[ \t]+one)(?:[ \t]+\d+)?(?:[ \t]+(?:are|of[ \t]+them|is))?[ \t]+in[ \t]+"
                          r"(?P<state>" + "|".join(STATE_WORDS) + r")\b")
RX_TYPED_EMAIL = re.compile(r"\b(?P<role>owner|owned by|organizer|organiser|organized by)[ \t]+(?:is[ \t]+)?"
                            r"(?P<email>[\w.+-]+@[\w-]+(?:\.[\w-]+)+)", re.I)
RX_LEAD_NAME = re.compile(r"(?:^|[.;:!?][ \t]+|\b(?:by|from)[ \t]+|\b(?:One|Next|Then|First|Second|Last|Its|The)[ \t]+"
                          r"(?:thread[ \t]+)?(?:reply|message|comment|post|answer),?[ \t]+)"
                          r"(?P<name>[A-Z][a-z]+(?:[ \t]+[A-Z][a-z]+)?)(?:'s[ \t]+[a-z][a-z \t-]{0,30})?,?[ \t]*$")


def find_quotes(text: str) -> list:
    """[(start, end, inner)] for "quoted" spans. An inch mark (6.5" set") does not close a quote."""
    out, open_at, n = [], None, len(text)
    for i, ch in enumerate(text):
        if ch not in '"\u201c\u201d':
            continue
        if ch == '"' and i > 0 and text[i - 1].isdigit():
            size = re.search(r"(?<![\d.])\d{1,2}(?:\.\d)?$", text[max(0, i - 5):i])
            nxt = next((j for j in range(i + 1, n) if text[j] in '"\u201c\u201d'), None)
            if size and open_at is not None and nxt is not None and not text[nxt - 1].isspace() and nxt - i < 40 \
                    and not re.match(r"[ \t]*[,.;:)]", text[i + 1:i + 3]):
                continue
            if size and open_at is None and re.match(r"[ \t]+[a-z]", text[i + 1:i + 4]):
                continue
        if open_at is None:
            open_at = i
        else:
            out.append((open_at, i + 1, text[open_at + 1:i]))
            open_at = None
    return out


def quote_segments(inner: str) -> list:
    """A quote cut at its ellipses: each piece must be in the record."""
    pieces = re.split(r"\[\s*(?:\.\.\.|\u2026)\s*\]|\.\.\.+|\u2026", inner)
    return [p for p in (norm(x) for x in pieces) if len(p) >= 3]


def quote_in(quote: str, record: Record) -> bool:
    segments = quote_segments(quote) or [norm(quote)]
    text = record.text
    for seg in segments:
        if seg in text:
            continue
        trimmed = seg.rstrip(".,;:!?")
        if len(trimmed) >= 3 and trimmed in text:
            continue
        return False
    return True


def quote_near(quote: str, record: Record) -> bool:
    segments = [fold(s) for s in (quote_segments(quote) or [quote])]
    return all(s.rstrip(".,;:!?") in record.folded for s in segments if s)


def _dashless(value) -> str:
    """norm() with dashes, ellipses, quote marks and emphasis marks made plain; case is kept."""
    s = norm(value).translate(_DASHES).replace("\u2026", "...").replace("\u2014", "-").replace("\u00f7", "/").replace("\u00d7", "x")
    s = re.sub(r"[*_~`]", "", s)
    return re.sub(r"[ \t]*-[ \t]*", "-", s)


def quote_dashed(quote: str, record: Record) -> bool:
    """The quote is in the record when dashes (hyphen, en and em dash, with or without spaces), quote marks and
    emphasis are made plain. Case must match."""
    segments = [_dashless(s).rstrip(".,;:!?") for s in (quote_segments(quote) or [quote])]
    if not any(segments):
        return False
    if record._dashed is None:
        record._dashed = _dashless(record.text)
    return all(s in record._dashed for s in segments if s)


def quote_services(event: dict, q: dict, by_n: dict) -> list:
    """The base services a quote may come from: the event's own, plus those of an event the text right after the
    quote points to (`"Reached out - no response" (OE 5)`)."""
    services = list(event.get("base_services") or [])
    tail = (event.get("expected") or "")[q["end"]:q["end"] + 60]
    tail = re.split(r"[.;!?][ \t]|\n|\"", tail)[0]
    for ref in RX_OE_REF.finditer(tail):
        for number in re.findall(r"\d+", ref.group(0))[:5]:
            other = by_n.get(int(number))
            for service in (other or {}).get("services", ()):
                if service in BASE_FILES and service not in services:
                    services.append(service)
    return services


def _masked(text: str, spans) -> str:
    chars = list(text)
    for a, b in spans:
        for i in range(a, min(b, len(chars))):
            if chars[i] not in "\n":
                chars[i] = "\x00"
    return "".join(chars)


def extract(expected: str) -> dict:
    """Every qualifier of an Expected text, with spans. Text inside quotes is the record's own wording: only the
    quote itself is a qualifier there."""
    quotes = [{"kind": "quote", "text": inner, "start": a, "end": b} for a, b, inner in find_quotes(expected)]
    taken = [(q["start"], q["end"]) for q in quotes]
    taken += [m.span() for m in RX_OE_REF.finditer(expected)]
    outside = _masked(expected, taken)
    dates = find_dates(outside)
    taken += [(q["start"], q["end"]) for q in dates]
    outside = _masked(expected, taken)

    def free(a, b):
        return not any(a < y and x < b for x, y in taken)

    literals = []
    for kind, rx in LITERALS:
        for m in rx.finditer(outside):
            if free(*m.span()):
                value = m.group(1) if kind == "code" else m.group(0)
                literals.append({"kind": kind, "text": value, "start": m.start(), "end": m.end()})
                taken.append(m.span())
    outside = _masked(expected, taken)
    figures, counts = [], []
    for kind, rx in (("amount", RX_MONEY), ("amount", RX_PERCENT), ("number", RX_HASHNUM)):
        for m in rx.finditer(outside):
            if free(*m.span()):
                figures.append({"kind": kind, "text": m.group(0), "start": m.start(), "end": m.end()})
                taken.append(m.span())
    outside = _masked(expected, taken)
    for m in RX_COUNT.finditer(outside):
        raw = m.group("num").lower()
        if re.search(r"\b(?:per|each|every|a|an|the|of|or|to)[ \t]*$", m.group("mid") or "", re.I):
            continue
        if raw in NUMBER_WORDS and re.match(r"[ \t]+(?:per|each|every|at a time)\b", outside[m.end():m.end() + 14]):
            continue
        if raw == "no" or ENUM_BEFORE.search(outside[max(0, m.start() - 14):m.start()]):
            continue
        value = NUMBER_WORDS[raw] if raw in NUMBER_WORDS else int(raw.replace(",", ""))
        end = m.start() + len(m.group("num"))
        counts.append({"kind": "count", "text": norm(m.group(0)), "start": m.start(), "end": m.end(), "value": value,
                       "noun": m.group("noun").lower(), "num_end": end, "word": raw in NUMBER_WORDS})
        taken.append((m.start(), end))
    outside = _masked(expected, taken)
    for m in RX_NUMBER.finditer(outside):
        raw = m.group(0)
        digits = raw.replace(",", "")
        if not free(*m.span()) or ENUM_BEFORE.search(outside[max(0, m.start() - 14):m.start()]):
            continue
        if re.fullmatch(r"20[12]\d", digits):
            continue
        big = "," in raw or "." in raw or len(digits) >= 4
        unit = re.match(r"[ \t]+([A-Za-z][A-Za-z-]+)", outside[m.end():m.end() + 24])
        if unit and unit.group(1).lower() in STOP_UNITS:
            unit = None
        if not big and (len(digits) < 2 or not unit):
            continue
        figures.append({"kind": "amount" if big else "number", "text": raw + (f" {unit.group(1)}" if unit and not big else ""),
                        "start": m.start(), "end": m.end(), "digits": digits})
    for f in figures:
        f.setdefault("digits", re.sub(r"[^\d.]", "", f["text"].replace(",", "")).strip("."))
    words = _masked(expected, [(q["start"], q["end"]) for q in quotes])
    superlatives = [{"kind": "superlative", "text": norm(m.group(0)), "start": m.start(), "end": m.end(),
                     "word": m.group("word").lower(), "noun": m.group("noun").lower()}
                    for m in RX_SUPERLATIVE.finditer(words)]
    absences = [{"kind": "absence", "text": norm(m.group(0)), "start": m.start(), "end": m.end()}
                for m in RX_ABSENCE.finditer(words)]
    plain = _masked(expected, [(q["start"], q["end"]) for q in quotes] + [(q["start"], q["end"]) for q in dates]
                    + [m.span() for m in RX_OE_REF.finditer(expected)])
    return {"quotes": quotes, "dates": dates, "literals": literals, "figures": figures, "counts": counts,
            "superlatives": superlatives, "absences": absences, "masked": words, "plain": plain}


def sentence_start(masked: str, pos: int) -> int:
    """Start of the sentence that holds `pos` (quotes are masked, so a full stop inside one does not count)."""
    best = 0
    for m in re.finditer(r"[.!?][ \t]+(?=[A-Z\x00(\[])|\n", masked[:pos]):
        best = m.end()
    return best


# ------------------------------------------------------------------ the check

def _figure_in(digits: str, text: str) -> bool:
    if not digits:
        return False
    core = digits[:-3] if re.search(r"\.00$", digits) else digits
    return bool(re.search(r"(?<![\d.:-])" + re.escape(core) + r"(?:\.0+)?(?![\d:-]|\.\d)", text)
                or (core != digits and re.search(r"(?<![\d.:-])" + re.escape(digits) + r"(?!\d)", text)))


class Checker:
    def __init__(self, sql: SqlIndex, base: BaseReader | None, people: People, clock_dates=()):
        self.sql, self.base, self.people = sql, base, people
        self.clock_dates = tuple(clock_dates)
        self.earlier = ""            # Expected text of the events before the current one (values already produced)

    # ---- resolution
    def corpus(self) -> list:
        return self.sql.records + (self.base.all_records() if self.base else [])

    def key_records(self, token: str) -> list:
        return list(self.sql.by_key.get(token, ())) + (list(self.base.by_key.get(token, ())) if self.base else [])

    def quote_records(self, quote: str, services) -> list:
        """Records holding the quote verbatim; when none does, the ones holding it with other dashes or quote marks."""
        for test in (quote_in, quote_dashed):
            hits = [r for r in self.sql.records if test(quote, r)]
            if not hits and self.base:
                for service in services:
                    hits += [r for r in self.base.searched.get((service, norm(quote)), ()) if r not in hits and test(quote, r)]
                hits += [r for r in self.base.all_records() if r not in hits and test(quote, r)]
            if hits:
                return hits
        return [r for r in self.sql.families if quote_in(quote, r) or quote_dashed(quote, r)]

    def resolve(self, event: dict, ex: dict) -> None:
        """event['records'] (ordered, unique) and per-quote anchors."""
        records = []

        def add(found):
            for rec in found:
                if rec not in records:
                    records.append(rec)

        whole = event["head"] + " " + _masked(event["expected"] or "", [(q["start"], q["end"]) for q in ex["quotes"]])
        for token in id_tokens(whole):
            if "@" not in token or "contacts" in event["services"]:      # an address names a record only in Contacts
                add(self.key_records(token))
        for q in ex["quotes"]:
            inner = norm(q["text"])
            titled = self.sql.by_title.get(inner, [])
            q["title"] = bool(titled)
            found = titled or (self.quote_records(q["text"], q.get("services") or event.get("base_services") or event["services"])
                               if len(inner) >= 3 else [])
            q["records"] = found
            q["anchor"] = (len(inner) >= MIN_ANCHOR_QUOTE or bool(titled)) and 0 < len(found) <= MAX_ANCHOR_RECORDS
            if q["anchor"]:
                add(found)
        for m in re.finditer(r'"([^"]{4,120})"', event["head"]):          # a title quoted in the call description
            add(self.sql.by_title.get(norm(m.group(1)), []))
        for rec in list(records):                                         # the rows that make up one file
            for col in FAMILY_COLUMNS:
                value = rec.fields.get(col)
                if value and (col != "id" or rec.short == "drive_files"):
                    add(self.key_records(str(value)))
        event["records"] = records

    # ---- single qualifiers
    def _support(self, records, test):
        for rec in records:
            if test(rec):
                return rec
        return None

    def miss(self, event, services=None, inner=None) -> tuple:
        """('unsupported', scope) when every source in scope was searched (for this quote, when `inner` is given),
        else ('unverifiable', scope)."""
        if not self.base or self.base.mode not in ("search", "all"):
            return "unverifiable", "not in the injection SQL; base records were not searched"
        services = list(event.get("base_services", ()) if services is None else services)
        if self.base.errors:
            return "unverifiable", "not in the injection SQL; the base read failed"
        if not services:
            return "unverifiable", "not in the injection SQL; the event names no base service to search"
        skipped = [s for s in services if s in self.base.skipped or (s in BASE_HEAVY and self.base.mode != "all")]
        if skipped:
            return "unverifiable", f"not in the injection SQL; the base {', '.join(skipped)} export was not searched (--base all)"
        if inner is not None and not all((s, inner) in self.base.searched for s in services):
            return "unverifiable", "not in the injection SQL; the quote could not be sent to the base search (too short or budget)"
        partial = [s for s in services if s in PARTIAL_SEARCH]
        if inner is not None and partial:
            # A literal search miss is not proof there: mail bodies break lines ("I won't be able\nto make it.",
            # frederick_q4_commitments OE 14, PASS 5) and code quotes live in repository files that are not searched
            # (julia_zm_difficulty_baseline OE 18, PASS 5).
            return "unverifiable", (f"not in the injection SQL, and a literal search of the base {', '.join(services)} "
                                    f"export did not find it; " + "; ".join(PARTIAL_SEARCH[s] for s in partial))
        return "unsupported", f"not in the injection SQL or the base {', '.join(services)} export"

    def check_quote(self, event, q, out):
        inner = norm(q["text"])
        if len(inner) < 3:
            return
        if q["records"]:
            rec = q["records"][0]
            out.append(_res(event, q, "supported", rec, "verbatim" + (" (a title)" if q.get("title") else "")))
            return
        if event["kind"] in ("write", "derive"):
            out.append(_res(event, q, "skipped", None, "text the event produces or paraphrases"))
            return
        # The same words with other dashes, quote marks or emphasis: the platform has passed these (five such quotes
        # on a PASS 5 file), so they count as the record's text. Other case is a defect only in this event's record.
        dashed = self._support(self.corpus(), lambda r: quote_dashed(q["text"], r))
        if dashed:
            out.append(_res(event, q, "supported", dashed, "the record's text with other dashes or quote marks"))
            return
        near = self._support(event["records"], lambda r: quote_near(q["text"], r))
        if near and len(inner) >= MIN_ANCHOR_QUOTE:
            out.append(_res(event, q, "unsupported", near, "the record this event reads has this text in other case or "
                            "punctuation; quote it character for character"))
            return
        if len(inner) < MIN_ANCHOR_QUOTE:
            known = near or inner in self.earlier or inner.casefold() in event["head"].casefold() or \
                self._support(self.corpus(), lambda r: inner in r.text)
            out.append(_res(event, q, "supported" if known else "skipped", near, "a short label" if known else "a short label, not searched"))
            return
        result, scope = self.miss(event, q.get("services", event.get("base_services", ())), inner)
        out.append(_res(event, q, result, None, scope,
                        prove=None if result == "unsupported" else "read the record this event opens and compare the quote"))

    def check_date(self, event, q, out, anchors=None, role=None, lead_dates=()):
        """One date. `anchors` are the records of the quote this date introduces (it may then contradict them);
        `role` is the kind of time the text names (created, due ...) for a titled record."""
        problem = date_self_check(q)
        if problem:
            out.append(_res(event, q, "contradicted", None, problem))
            return
        records = event["records"]
        if anchors:
            hit = self._date_in(q, anchors)
            if hit:
                out.append(_res(event, q, "supported", hit[0], hit[1]))
                return
            verdict = self._bound_conflict(q, anchors, role, lead_dates)
            if verdict:
                result, rec, says = verdict
                out.append(_res(event, q, result, rec, says,
                                prove=None if result == "contradicted" else "read the record in the tool and compare the minute"))
                return
        hit = self._date_in(q, records)
        if hit:
            out.append(_res(event, q, "supported", hit[0], hit[1]))
            return
        if any(self._same_day(q, d) for d in self.clock_dates):
            out.append(_res(event, q, "supported", None, "the task clock"))
            return
        hit = self._date_in(q, [r for r in self.corpus() if r not in records])
        if hit:
            out.append(_res(event, q, "supported", hit[0], hit[1] + " (another record the events read)", scope="corpus"))
            return
        if q["text"] in self.earlier or q["text"] in event["head"]:
            out.append(_res(event, q, "supported", None, "stated by an earlier event or the call description"))
            return
        if event["kind"] in ("write", "derive"):
            out.append(_res(event, q, "skipped", None, "a date the event derives"))
            return
        has = "; ".join(f"{r.rid}: " + ", ".join(f"{f} {show_instant(w) if h else w.date().isoformat()}" for f, w, h in r.times[:2])
                        for r in records[:2] if r.times)
        out.append(_res(event, q, "unverifiable", records[0] if records else None,
                        ("no time field or written date of the records resolved for this event matches" + (f" ({has})" if has else ""))
                        if records else "the record this event reads was not resolved",
                        prove="name the record that carries this date (id, ts or a quote) or compare it by hand"))

    def _bound_conflict(self, q, anchors, role, lead_dates):
        """(result, record, says) for a date bound to `anchors` that none of their times or written dates carries, or
        None when nothing can be said.

        The field compared is the one the text names (created, due, merged ...) or, with no such word, a message's
        own timestamp. It is 'contradicted' only when every compared field of every anchor contradicts the date
        (date_conflict: the minute only where the record holds the minute). When a field holds the day only and the
        day agrees, the clock time is 'unverifiable'."""
        if not role and any(d is not q and self._date_in(d, anchors) for d in lead_dates):
            return None                      # another date of the same lead is the record's time
        if role:
            if self._date_in(q, self.corpus()):
                return None                  # a weak binding: any record the events read that carries the date clears it
            pairs = [(r, [t for t in r.times if t[0].split(".")[0] in ROLE_FIELDS[role]]) for r in anchors]
        elif all(r.message_like() for r in anchors):
            pairs = [(r, [r.primary_time()]) for r in anchors]
        else:
            return None
        if not pairs or not all(times for _, times in pairs):
            return None
        rows = [(r, f, w, h, date_conflict(q, w, h)) for r, times in pairs for f, w, h in times]
        if all(row[4] for row in rows):
            rec, field, _, _, why = rows[0]
            return "contradicted", rec, f"{field}: {why}"
        coarse = [row for row in rows if row[4] is None and q["hh"] is not None and not minute_precise(row[2], row[3])]
        if coarse:
            rec, field, when, has_time, _ = coarse[0]
            shown = show_instant(when) if has_time else when.date().isoformat()
            return "unverifiable", rec, f"{field} = {shown} holds the day only; the stated clock time cannot be compared"
        return None

    def _same_day(self, q, day) -> bool:
        return q["m"] == day.month and q["d"] == day.day and (q["y"] in (None, day.year))

    def _date_in(self, q, records):
        for rec in records:
            for field, when, has_time in rec.times:
                if date_matches(q, when, has_time):
                    return rec, f"{field} = {show_instant(when) if has_time else when.date().isoformat()}"
        for rec in records:
            for t in rec.text_dates:
                if q["m"] is None:                                   # a bare time: the same clock time written out
                    if t["hh"] is not None and (t["hh"], t["mi"]) == (q["hh"], q["mi"]):
                        return rec, f"written in the record as \"{t['text']}\""
                    continue
                if t["m"] != q["m"] or (q["y"] and t["y"] and t["y"] != q["y"]):
                    continue
                if q["d"] is not None and t["d"] != q["d"]:
                    continue
                if q["hh"] is not None and t["hh"] is not None and (t["hh"], t["mi"]) != (q["hh"], q["mi"]):
                    continue
                return rec, f"written in the record as \"{t['text']}\"" + (" (day only)" if q["hh"] is not None and t["hh"] is None else "")
        return None

    def check_literal(self, event, q, out):
        value = q["text"][1:] if q["kind"] == "channel" else q["text"]
        rec = self._support(event["records"], lambda r: value in r.text or value in r.keys)
        if rec:
            out.append(_res(event, q, "supported", rec, "in the record"))
            return
        keyed = self.key_records(q["text"]) or self.key_records(value)
        if keyed:
            out.append(_res(event, q, "supported", keyed[0], "a record with this id"))
            return
        rec = self._support(self.corpus(), lambda r: value in r.text)
        if rec:
            out.append(_res(event, q, "supported", rec, "in another record the events read"))
            return
        if q["kind"] in ("email", "id") and self.people.by_token(value):
            out.append(_res(event, q, "supported", None, "a known person's id or address in the universe (not in the resolved records)"))
            return
        if value in self.earlier or value.casefold() in event["head"].casefold():
            out.append(_res(event, q, "supported", None, "stated by an earlier event or the call description"))
            return
        if event["kind"] != "read" and q["kind"] in ("id", "code", "version", "sha"):
            out.append(_res(event, q, "skipped", None, "a value the event produces"))
            return
        before = (event.get("expected") or "")[max(0, q["start"] - 40):q["start"]]
        if re.search(r"\b(?:no|not|never|without|isn't|doesn't|there is no)\b[^.;:\n]{0,25}$", before, re.I):
            out.append(_res(event, q, "supported", None, "the line says it does not exist, and no record read carries it"))
            return
        readable = self._id_readable(q)
        if readable:
            out.append(_res(event, q, "unsupported", None, f"no record carries it: not in the injection SQL{readable}"))
        else:
            out.append(_res(event, q, "unverifiable", None, "not in the injection SQL; base records were not read for it",
                            prove="read the base record that holds this value"))

    def _id_readable(self, q) -> str:
        """Scope text when the base was really asked for this kind of id, else ''."""
        if not self.base or not self.base.enabled() or self.base.errors:
            return ""
        if q["kind"] == "ticket":
            # Only a known Linear team key proves anything: `ES-2` (a stock line) or `INV-12` is not a ticket.
            prefix = q["text"].split("-")[0]
            keys = {str(r.fields.get("identifier") or r.fields.get("id") or "").split("-")[0]
                    for r in self.corpus() if r.short == "linear_issues"}
            return " and not a Linear issue in the base" if prefix in keys else ""
        if q["kind"] == "channel":
            return " and not a Slack channel name in the base"
        if q["kind"] == "id" and re.fullmatch(r"\d{10}\.\d{6}", q["text"]):
            return " and not a Slack message ts in the base"
        return ""

    def check_figure(self, event, q, out):
        digits = q["digits"]
        if q["text"].startswith("#"):
            rec = self._support(event["records"], lambda r: q["text"] in r.keys or _figure_in(digits, r.plain)) or \
                self._support(self.key_records(q["text"]), lambda r: True) or \
                self._support(self.corpus(), lambda r: q["text"] in r.keys or ("#" + digits) in r.text)
        else:
            rec = self._support(event["records"], lambda r: _figure_in(digits, r.plain))
        if rec:
            out.append(_res(event, q, "supported", rec, "in the record"))
            return
        if _figure_in(digits, self.earlier.replace(",", "")) or _figure_in(digits, event["head"].replace(",", "")):
            out.append(_res(event, q, "supported", None, "stated by an earlier event or the call description"))
            return
        rec = self._support(self.corpus(), lambda r: _figure_in(digits, r.plain)) if q["kind"] == "amount" or q["text"].startswith("#") else None
        if rec:
            out.append(_res(event, q, "supported", rec, "in another record the events read", scope="corpus"))
            return
        if event["kind"] in ("write", "derive"):
            out.append(_res(event, q, "skipped", None, "a figure the event derives"))
            return
        result, scope = self.miss(event)
        out.append(_res(event, q, "unverifiable", event["records"][0] if event["records"] else None,
                        "the figure is in no record read" + ("" if result == "unsupported" else f" ({scope})"),
                        prove="if it is computed, recompute it from the rows the event reads and state the calculation; "
                              "if it is quoted, read the record that holds it"))

    def check_count(self, event, q, ex, out):
        expected = event["expected"]
        if "repl" in q["noun"]:
            return                                   # reply counts are bound to their message below
        listed = self._listed(expected, q)
        if listed is not None and listed == q["value"]:
            out.append(_res(event, q, "supported", None, f"the event lists {listed} itself"))
            return
        if _figure_in(str(q["value"]), self.earlier.replace(",", "")) and not q["word"]:
            out.append(_res(event, q, "supported", None, "stated by an earlier event"))
            return
        if event["kind"] != "read":
            out.append(_res(event, q, "skipped", None, "a count the event derives"))
            return
        if q["word"] and q["value"] <= 1 and not re.search(r"\b(?:only|just|exactly)\b", expected[max(0, q["start"] - 12):q["start"]], re.I):
            out.append(_res(event, q, "skipped", None, "\"one\" used as an article"))
            return
        if _figure_in(str(q["value"]), " ".join(r.plain for r in event["records"])) and not q["word"] and q["value"] >= 10:
            out.append(_res(event, q, "supported", event["records"][0], "the number is written in a record read (weak: not recounted)"))
            return
        same = [r for r in event["records"] if _noun_table(q["noun"], r)]
        if same and len(same) == q["value"]:
            out.append(_res(event, q, "supported", same[0], f"{len(same)} such records resolved for this event"))
            return
        detail = f"the event itself lists {listed}" if listed is not None else "a count of a collection"
        out.append(_res(event, q, "unverifiable", None, detail,
                        prove=f"list the {q['noun']} with the call this event names and count them"))

    def _listed(self, expected, q):
        """How many items the Expected text itself lists for this count, or None."""
        tail = expected[q["end"]:]
        tickets = RX_TICKET.findall(_masked(expected, [m.span() for m in RX_OE_REF.finditer(expected)]))
        if re.search(r"issue|ticket|child|bug", q["noun"]) and len(set(tickets)) >= 2:
            return len(set(tickets))
        colon = re.match(r"[^.:;]{0,80}:[ \t]*", tail)
        if colon:
            body = re.split(r"\.[ \t]+(?=[A-Z])|\n", tail[colon.end():])[0]
            parts = [p for p in re.split(r";", body) if p.strip()]
            if len(parts) < 2:
                parts = [p for p in re.split(r",[ \t]+(?![^(]*\))", body) if p.strip()]
            if len(parts) >= 2:
                return len(parts)
        return None

    # ---- bound checks (the ones that can contradict)
    def bound_checks(self, event, ex, out, handled):
        """Checks tied to one record: the time, author and reply count of a quoted message, the dated fields of a
        titled record, ticket states, owner and organizer. These are the checks that can contradict."""
        masked = ex["masked"]
        quotes = ex["quotes"]
        for q in quotes:
            start = max(sentence_start(masked, q["start"]), max([p["end"] for p in quotes if p["end"] <= q["start"]] or [0]))
            lead = masked[start:q["start"]]
            if len(lead) > LEAD_GAP or q.get("title") or len(norm(q["text"])) < MIN_ANCHOR_QUOTE:
                continue
            dates = [d for d in ex["dates"] if start <= d["start"] and d["end"] <= q["start"]]
            stamp = next((d for d in dates if _attributes(masked[d["end"]:q["start"]], d) and id(d) not in handled), None)
            if q.get("anchor"):
                if stamp:
                    role = _role(masked[max(start, stamp["start"] - 28):stamp["start"]])
                    self.check_date(event, stamp, out, anchors=q["records"], role=role, lead_dates=dates)
                    handled.add(id(stamp))
                self._author(event, q, lead, dates, out)
            elif not q["records"] and stamp and event["kind"] in ("read", "unknown"):
                problem = date_self_check(stamp)                      # the quoted record was not read
                out.append(_res(event, stamp, "contradicted" if problem else "unverifiable", None,
                                problem or "the time of a quoted record that was not read",
                                prove=None if problem else "read the quoted record and compare its timestamp"))
                handled.add(id(stamp))
        for q in [t for t in quotes if t.get("title") and t.get("anchor")]:      # dated fields around a quoted title
            lo = max(sentence_start(masked, q["start"]), max([p["end"] for p in quotes if p["end"] <= q["start"]] or [0]))
            hi = min([p["start"] for p in quotes if p["start"] >= q["end"]] + [len(masked)])
            stop = re.search(r"[.!?][ \t]+(?=[A-Z\x00])", masked[q["end"]:hi])
            hi = q["end"] + stop.start() if stop else hi
            for d in ex["dates"]:
                if lo <= d["start"] < hi and id(d) not in handled:
                    role = _role(masked[max(lo, d["start"] - 28):d["start"]])
                    if role:
                        self.check_date(event, d, out, anchors=q["records"], role=role)
                        handled.add(id(d))
        self._replies(event, ex, out)
        if event["kind"] in ("read", "unknown"):
            self._quantified(event, ex, out)
        if event["kind"] == "read":
            self._states(event, ex, out)
            self._typed_emails(event, ex, out)

    def _quantified(self, event, ex, out):
        """`all five read "quote"`, `both say "quote"`: the quote must be in that many records (or that many times in
        them). Never 'contradicted': the search is literal, so a record that words it with another line break is not
        counted. 'unsupported' only when the base export of the event's service was searched for this quote."""
        for q in ex["quotes"]:
            got = quantifier(ex, q)
            if not got:
                continue
            m, want = got
            inner = norm(q["text"])
            qual = {"kind": "count", "text": f"{norm(m.group(0))} \"{inner[:50]}\"", "start": q["start"] - 1, "end": q["start"]}
            recs = [r for r in self.sql.records if quote_in(q["text"], r)]
            from_base = []
            if self.base:
                for service in event.get("base_services", ()):
                    from_base += [r for r in self.base.searched.get((service, inner), ()) if r not in from_base]
                from_base += [r for r in self.base.all_records() if r not in from_base and quote_in(q["text"], r)]
            recs += [r for r in from_base if r not in recs]
            seg = (quote_segments(q["text"]) or [inner])[0].rstrip(".,;:!?")
            found = sum(occurrences(r, seg) for r in recs)
            if found >= want:
                out.append(_res(event, qual, "supported", recs[0], f"the quote is in {found} places in {len(recs)} records"))
                continue
            searched = bool(self.base and self.base.mode in ("search", "all") and not self.base.errors
                            and any((s, inner) in self.base.searched for s in event.get("base_services", ())))
            capped = len(from_base) >= BASE_QUERY_LIMIT or any(r.partial for r in recs) or \
                any(s in PARTIAL_SEARCH for s in event.get("base_services", ()))      # a wrapped body can be missed
            says = (f"the line says {norm(m.group(0))} \"{inner[:60]}\", but the quote is in {found} place(s) in "
                    f"{len(recs)} record(s)" + (f" ({', '.join(r.rid for r in recs[:3])})" if recs else ""))
            if searched and not capped:
                out.append(_res(event, qual, "unsupported", recs[0] if recs else None, says,
                                prove="read every record the line counts and quote what each one says"))
            else:
                out.append(_res(event, qual, "unverifiable", recs[0] if recs else None,
                                says + "; the base export was not searched for it in full",
                                prove="read every record the line counts and quote what each one says"))

    def _author(self, event, q, lead, dates, out):
        """`Name, <time>: "quote"`: the name must be the author of the quoted message."""
        if not self.people.names:
            return
        cut = (dates[0]["start"] - (q["start"] - len(lead))) if dates else len(lead)
        m = RX_LEAD_NAME.search(lead[:cut].replace("\x00", " ").rstrip(": \t"))
        if not m:
            return
        said = norm(m.group("name")).casefold()
        if not self.people.known(said):
            return
        recs = [r for r in q["records"] if r.message_like()]
        if not recs or len(recs) != len(q["records"]):
            return
        authors = [self.people.by_token(r.author_tokens()[0]) if r.author_tokens() else None for r in recs]
        qual = {"kind": "name", "text": m.group("name"), "start": q["start"] - len(lead) + m.start("name"), "end": 0}
        if any(a and self.people.matches(a, said) for a in authors):
            out.append(_res(event, qual, "supported", recs[0], "the record's author"))
        elif all(authors):
            out.append(_res(event, qual, "contradicted", recs[0], f"the author of the quoted record is {self.people.label(authors[0])} "
                            f"({recs[0].author_tokens()[0]})"))

    def _replies(self, event, ex, out):
        """"It has one reply" after a quoted Slack message: the message's reply_count."""
        plain = ex["plain"]
        messages = [(q, q["records"][0]) for q in ex["quotes"] if q.get("anchor") and len(q["records"]) == 1
                    and q["records"][0].short.endswith("messages") and "reply_count" in q["records"][0].fields]
        if event["kind"] != "read":
            return
        for m in RX_REPLIES.finditer(plain):
            before = [(q, r) for q, r in messages if q["end"] <= m.start()]
            after = [(q, r) for q, r in messages if q["start"] >= m.end()]
            start = sentence_start(ex["masked"], m.start())
            sentence = plain[start:m.end() + 40]
            if not before or not re.search(r"\b(?:has|have|had|with|carries|got)\b", plain[start:m.start()], re.I):
                continue
            if re.search(r"\b(?:first|second|other|another|earlier|previous|before|parent|root|each|every|one of)\b", sentence, re.I):
                continue
            if any(q["start"] < m.start() + 160 for q, _ in after) and not re.match(r"[ \t]*(?:It|The message|The post|This|Both|Neither)\b", plain[start:]):
                continue
            both = re.match(r"[ \t]*(?:Both|Neither)\b", plain[start:])
            targets = before if both else before[-1:]
            raw = m.group("num").lower()
            value = NUMBER_WORDS[raw] if raw in NUMBER_WORDS else int(raw)
            qual = {"kind": "count", "text": norm(m.group(0)), "start": m.start(), "end": m.end()}
            for _, rec in targets:
                try:
                    actual = int(rec.fields.get("reply_count") or 0)
                except (TypeError, ValueError):
                    continue
                out.append(_res(event, qual, "supported" if actual == value else "contradicted", rec, f"reply_count = {actual}"))

    def _states(self, event, ex, out):
        """`ENG-12 "title" (Todo)` and "all in Backlog": the ticket's state. A bare `ENG-12 Done` is not checked,
        because events also write the state a later step sets."""
        plain = ex["plain"]
        tickets = [(m.group(0), m.start(), m.end()) for m in RX_TICKET.finditer(plain)]
        states = "|".join(STATE_WORDS)
        for token, a, b in tickets:
            recs = [r for r in self.key_records(token) if r.state() and not r.partial]
            if len(recs) != 1:
                continue
            tail = re.sub(r"^[ \t]*\x00+", " ", plain[b:b + 220], count=1)                  # an optional quoted title
            m = re.match(r"[ \t]*(?:\((" + states + r")\)|,?[ \t]*(?:is[ \t]+in|in[ \t]+state|state|status)[ \t]+(" + states + r")\b)", tail)
            if not m:
                continue
            start = sentence_start(ex["masked"], a)
            if re.search(r"\b(?:so|therefore|thus|hence|goes?|moves?|moved|becomes?|set|mark(?:ed)?|closes?|move)\b", plain[start:a], re.I):
                continue
            said, (field, actual) = m.group(1) or m.group(2), recs[0].state()
            qual = {"kind": "state", "text": f"{token} {said}", "start": a, "end": b}
            same = said.casefold() == actual.casefold() or {said.casefold(), actual.casefold()} == {"canceled", "cancelled"}
            out.append(_res(event, qual, "supported" if same else "contradicted", recs[0], f"{field} = {actual}"))
        for m in RX_ALL_STATE.finditer(plain):
            said = m.group("state")
            names = sorted({t for t, _, _ in tickets})
            if len(names) < 2:
                continue
            wrong, unread = [], 0
            for token in names:
                recs = [r for r in self.key_records(token) if r.state() and not r.partial]
                if len(recs) != 1:
                    unread += 1
                elif recs[0].state()[1].casefold() != said.casefold():
                    wrong.append((token, recs[0]))
            qual = {"kind": "state", "text": norm(m.group(0)), "start": m.start(), "end": m.end()}
            if wrong:
                shown = ", ".join(f"{t} is {r.state()[1]}" for t, r in wrong[:6])
                out.append(_res(event, qual, "contradicted", wrong[0][1], shown))
            elif unread:
                out.append(_res(event, qual, "unverifiable", None, f"{unread} of the {len(names)} listed tickets were not read",
                                prove="read the state of every listed ticket"))
            else:
                out.append(_res(event, qual, "supported", None, f"all {len(names)} listed tickets are {said}"))

    def _typed_emails(self, event, ex, out):
        for m in RX_TYPED_EMAIL.finditer(ex["plain"]):
            column = "owner_email" if m.group("role").lower().startswith("own") else "organizer_email"
            recs = [r for r in event["records"] if r.fields.get(column) and not r.partial]
            if not recs:
                continue
            qual = {"kind": "name", "text": norm(m.group(0)), "start": m.start(), "end": m.end()}
            said = m.group("email").casefold()
            if any(str(r.fields[column]).casefold() == said for r in recs):
                out.append(_res(event, qual, "supported", recs[0], f"{column} matches"))
            elif len({str(r.fields[column]).casefold() for r in recs}) == 1:
                out.append(_res(event, qual, "contradicted", recs[0], f"{column} = {recs[0].fields[column]}"))

    def _head_titles(self, event, out):
        """A record named in the call description must carry that exact name (a hyphen for an en dash misses)."""
        for _, _, inner in find_quotes(event["head"]):
            name = norm(inner)
            if len(name) < 8 or name in self.sql.by_title or any(name in r.text for r in event["records"]):
                continue
            folded = fold(name)
            for rec in self.corpus():
                for col in TITLE_COLUMNS:
                    title = rec.fields.get(col)
                    # other dashes or punctuation miss an exact-name lookup; other case alone does not
                    if isinstance(title, str) and fold(title) == folded and norm(title).casefold() != name.casefold():
                        qual = {"kind": "quote", "text": name, "start": -1, "end": -1}
                        out.append(_res(event, qual, "unsupported", rec, f"the call names \"{name}\"; the record's {col} is \"{norm(title)}\""))
                        break
                else:
                    continue
                break

    # ---- one event
    def check_event(self, event: dict) -> list:
        out = []
        expected = event["expected"]
        if not expected:
            return out
        ex = event["ex"]
        handled = set()
        self.bound_checks(event, ex, out, handled)
        for q in ex["quotes"]:
            self.check_quote(event, q, out)
        for q in ex["dates"]:
            if id(q) not in handled:
                self.check_date(event, q, out)
        for q in ex["literals"]:
            self.check_literal(event, q, out)
        for q in ex["figures"]:
            self.check_figure(event, q, out)
        for q in ex["counts"]:
            self.check_count(event, q, ex, out)
        service = (event.get("base_services") or event["services"] or ["the service the event names"])[0]
        if event["kind"] == "read":
            self._head_titles(event, out)
        if event["kind"] != "write":
            for q in ex["superlatives"]:
                order = q["word"] not in ("only", "sole", "single")
                out.append(_res(event, q, "unverifiable", None, "a claim about the whole set, not one record",
                                prove=(f"read every {q['noun']} of the container in {service} and compare their times" if order
                                       else f"list every {q['noun']} in the scope the event names in {service} and confirm there is one")))
            for q in ex["absences"]:
                out.append(_res(event, q, "unverifiable", None, "absence wording",
                                prove=f"a scope-bound absence search in {service} (query, surfaces, positive control), "
                                      "or the record's own words"))
        return out


def id_tokens(text: str) -> list:
    """Record ids written in an event: tickets, Slack ts and ids, file and event ids, #numbers."""
    found = []
    for rx in (RX_TICKET, re.compile(r"(?<![\w.])\d{10}\.\d{6}(?!\w|\.\w)"), re.compile(r"\b[CDG][A-Z0-9]{8,11}\b"),
               re.compile(r"\b(?:f|d|evt|cmt|comment|page|usr|doc|sheet|pres)_[A-Za-z0-9_]{4,}\b"),
               re.compile(r"\b[0-9a-f]{24}\b|\b[0-9a-f]{32}\b|\b[0-9a-f]{40}\b"), RX_HASHNUM,
               re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b")):
        for m in rx.finditer(text):
            if m.group(0) not in found:
                found.append(m.group(0))
    for m in re.finditer(r"\b(?:PR|pull request)[ \t]+#?(\d{1,6})\b", text, re.I):
        if f"#{m.group(1)}" not in found:
            found.append(f"#{m.group(1)}")
    for m in re.finditer(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", text):
        if m.group(0) not in found:
            found.append(m.group(0))
    return found


RX_QUANT = re.compile(r"\b(?:(?P<all>all|each|every[ \t]+one)(?:[ \t]+of[ \t]+(?:the|them|these|those))?[ \t]+"
                      r"(?P<num>\d{1,2}|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)|(?P<both>both))"
                      r"(?:[ \t]+[\w'-]+){0,4}?[ \t]+(?:read|reads|open|opens|say|says|carry|carries|contain|contains|"
                      r"start|starts|begin|begins|show|shows|end|ends)(?:[ \t]+with)?[ \t]*:?[ \t]*$", re.I)


def quantifier(ex: dict, q: dict):
    """(match, how many) when the words right before a quote say that several records hold it, else None."""
    inner = norm(q["text"])
    if len(inner) < MIN_ANCHOR_QUOTE:
        return None
    masked = ex["masked"]
    start = max(sentence_start(masked, q["start"]), max([p["end"] for p in ex["quotes"] if p["end"] <= q["start"]] or [0]))
    m = RX_QUANT.search(masked[start:q["start"]].replace("\x00", " "))
    if not m:
        return None
    raw = (m.group("num") or "").lower()
    want = 2 if m.group("both") else (NUMBER_WORDS[raw] if raw in NUMBER_WORDS else int(raw))
    return (m, want) if want >= 2 else None


def occurrences(rec: Record, segment: str) -> int:
    """How many messages of a record hold a quote piece: one per message of a thread record (its `messages` list),
    else one for the record. A message is counted once however many of its fields (body, snippet, HTML) repeat it."""
    def holds(value) -> bool:
        scalars = []
        _flatten(_decode(value), scalars)
        return any(segment in norm(v) or segment in _dashless(v) for scalar in scalars for v in _variants(scalar))

    messages = _decode(rec.fields.get("messages"))
    if isinstance(messages, list) and messages:
        return sum(1 for m in messages if holds(m)) or (1 if holds(rec.fields) else 0)
    return 1 if holds(rec.fields) else 0


def _attributes(gap: str, date: dict) -> bool:
    """True when a date introduces the quote after it: `<date>[, short note]: "quote"`, and the date is a
    timestamp (it has a time, a weekday or a year), not a loose day such as "by Mar 1"."""
    stamp = date["hh"] is not None or date["dow"] is not None or date["y"] is not None
    if not stamp or len(gap) > 72 or "\x00" in gap:
        return False
    # The gap may hold an id with dots in it (a Slack ts 1759269913.882683, a version 0.3.49); it may not hold the
    # end of a sentence (a full stop, ! or ? followed by a space).
    return re.fullmatch(r"(?:[^.!?\x00]|[.!?](?=[^\s.!?]))*:[ \t]*", gap) is not None


def _role(before: str):
    text = before.replace("\x00", " ")
    for role, rx in ROLE_WORDS:
        if re.search(r"\b(?:" + rx + r")\b(?:[ \t]+(?:by|on|at)\b[ \t]*(?:[A-Z][\w.'-]*[ \t]*){0,2})?[ \t,]*$", text, re.I):
            return role
    return None


def _noun_table(noun: str, rec: Record) -> bool:
    table = rec.short
    pairs = (("issue", "issues"), ("ticket", "issues"), ("comment", "comments"), ("message", "messages"),
             ("post", "messages"), ("card", "cards"), ("event", "events"), ("commit", "commits"), ("review", "reviews"),
             ("pr", "pull_requests"), ("pull request", "pull_requests"), ("mail", "gmail_messages"), ("page", "pages"))
    return any(noun.startswith(n) and table.endswith(t) for n, t in pairs)


def _res(event, q, result, record, says, prove=None, scope="event") -> dict:
    return {"event": event["n"], "kind": q["kind"], "qualifier": q["text"] if len(q["text"]) <= 120 else q["text"][:117] + "...",
            "pos": q.get("start", 0), "result": result, "record": record.rid if record is not None else None,
            "says": says, "prove": prove, "scope": scope}


# ------------------------------------------------------------------ evaluate

def _context(task_dir):
    """The task context (universe, freeze, KB), or (None, reason) when the folder has no usable V3 assignment."""
    try:
        import task_context
        return task_context.load_context(task_dir), None
    except Exception as exc:                                    # ContextError and unreadable assignment alike
        return None, str(exc).splitlines()[0][:200] if str(exc) else type(exc).__name__


def _policy_mode() -> str:
    try:
        return (json.loads(POLICY.read_text()).get("modes") or {}).get("oe.qualifiers", "warn")
    except (OSError, ValueError):
        return "warn"


def _base_plan(events) -> dict:
    """Ids worth asking the base for, by kind."""
    wanted = {k: set() for k in ("ticket", "slack_ts", "channel", "pr", "sha", "drive", "gcal", "usr", "contact")}
    for ev in events:
        text = ev["head"] + " " + (ev["expected"] or "")
        plain = _masked(text, [(a, b) for a, b, _ in find_quotes(text)] + [m.span() for m in RX_OE_REF.finditer(text)])
        wanted["ticket"].update(RX_TICKET.findall(plain))
        wanted["slack_ts"].update(re.findall(r"(?<![\w.])\d{10}\.\d{6}(?!\w|\.\w)", plain))
        wanted["channel"].update(m[1:] for m in re.findall(r"(?<![\w#])#[a-z][a-z0-9_-]{2,}\b", plain))
        wanted["sha"].update(re.findall(r"\b[0-9a-f]{40}\b", plain))
        wanted["drive"].update(re.findall(r"\b[fd]_[0-9a-f]{6,}\b", plain))
        wanted["gcal"].update(re.findall(r"\bevt_[A-Za-z0-9_]{4,}\b", plain))
        wanted["usr"].update(re.findall(r"\busr_[A-Za-z0-9]{3,}\b", plain))
        if "contacts" in ev["services"]:
            wanted["contact"].update(re.findall(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", plain))
        if "slack" in ev["services"]:                              # a channel named in quotes
            wanted["channel"].update(norm(inner) for _, _, inner in find_quotes(text) if 3 <= len(norm(inner)) <= 80 and "\n" not in inner)
        if re.search(r"\bgithub\b|\bPRs?\b|\bpull requests?\b", text, re.I):
            wanted["pr"].update(int(n) for n in re.findall(r"\b(?:PR|PRs|pull request)[ \t]+#?(\d{1,6})\b", plain, re.I))
            wanted["pr"].update(int(n) for n in re.findall(r"(?<![\w#])#(\d{1,6})\b", plain))
    return wanted


def _probes(quote: str) -> list:
    """Literal runs of a quote to send to the base text search (the search is exact on spacing and dashes).

    The raw quote is cut at ellipses, quote marks, runs of two or more spaces and en or em dashes; each piece keeps its
    own spacing. The first probe is the longest piece. When that piece holds a spaced hyphen (` - `, which a record
    may write as a dash), the longest run without one is sent as well."""
    pieces = re.split(r"\[\s*(?:\.\.\.|\u2026)\s*\]|\.\.\.+|\u2026|['\"\u2018\u2019\u201c\u201d\\]|\s{2,}|\n|[\u2013\u2014]",
                      quote.translate(_TRANS))
    pieces = [p.strip(" \t.,;:") for p in pieces]
    pieces = [p for p in pieces if len(p) >= MIN_BASE_PROBE]
    if not pieces:
        return []
    first = max(pieces, key=len)
    out = [first]
    if re.search(r"[ \t]-[ \t]", first):
        runs = [r.strip() for p in pieces for r in re.split(r"[ \t]+-[ \t]+", p)]
        runs = [r for r in runs if len(r) >= MIN_BASE_PROBE and r != first]
        if runs:
            out.append(max(runs, key=len))
    return out


def evaluate(task_dir, oe=None, base="auto", runner=None, people=None, sql=None) -> dict:
    """Check the task's Oracle Events. Returns the report object; prints nothing and writes nothing in the task.

    oe / sql: other files to check instead of the task's own (an earlier round's bytes).
    base: auto | off | ids | search | all. Base reads go through tools/hg.py in a subprocess (its caches stay in the
    bundle); `runner` replaces that call in tests. `people` replaces the universe KB lookup."""
    task_dir = Path(task_dir)
    from stage_gate import slot_path
    oe_path = Path(oe) if oe else slot_path(task_dir, OE_FILE)
    sql_path = Path(sql) if sql else slot_path(task_dir, SQL_FILE)

    def rel(path):
        try:
            return str(Path(path).resolve().relative_to(task_dir.resolve()))
        except ValueError:
            return str(path)

    bound = {}
    oe_text = None
    if oe_path.is_file():
        oe_text = oe_path.read_text(errors="replace")
        bound[rel(oe_path)] = sha256(oe_path)
    sql_text = ""
    if sql_path.is_file():
        sql_text = sql_path.read_text(errors="replace")
        bound[rel(sql_path)] = sha256(sql_path)
    return check_text(task_dir, oe_text, sql_text, base=base, runner=runner, people=people, bound=bound, oe_name=rel(oe_path))


def check_text(task_dir, oe_text, sql_text, base="auto", runner=None, people=None, bound=None, oe_name=OE_FILE) -> dict:
    """The check on texts already in memory (evaluate() reads the files; the backtest patches them)."""
    task_dir = Path(task_dir)
    checks, findings = [], []
    report = {"tool": TOOL, "version": VERSION, "verdict": "FAIL", "bound_to": dict(bound or {}), "checks": checks,
              "findings": findings, "counts": {}, "by_kind": {}, "events": [],
              "base": {"mode": "off", "calls": 0, "errors": []}, "policy_mode": _policy_mode()}

    def stop(detail):
        checks.append({"id": "oe.parse", "status": "FAIL", "detail": detail})
        checks.append({"id": "oe.records", "status": "SKIP", "detail": "no events to resolve"})
        checks.append({"id": "oe.qualifiers", "status": "SKIP", "detail": "no events to check"})
        return report

    if oe_text is None or not oe_text.strip():
        return stop(f"{oe_name} is missing or empty; write the Oracle Events first")
    parsed = parse_events(oe_text)
    events = parsed["events"]
    if not events:
        return stop(f"no `OE <n>` heading found in {oe_name} ({parsed['preamble']} non-empty lines); number every event")
    problems = parsed["problems"]
    detail = f"{len(events)} events parsed from {oe_name}"
    if parsed["preamble"]:
        detail += f"; {parsed['preamble']} lines before the first event are not checked"
    if problems:
        detail += f"; {len(problems)} not usable: " + "; ".join(f"line {p['line']}: {p['what']}" for p in problems[:8])
    checks.append({"id": "oe.parse", "status": "WARN" if problems else "PASS", "detail": detail})

    try:
        sql = SqlIndex(sql_text)
    except Exception as exc:                                   # unreadable SQL: check against no injected rows
        report["base"]["errors"].append(f"{SQL_FILE} could not be parsed ({type(exc).__name__}); injected rows were not read")
        sql = SqlIndex("")
    context, context_error = _context(task_dir)
    clock_dates = ()
    if context:
        freeze = dt.datetime.fromisoformat(context["freeze_utc"].replace("Z", "+00:00"))
        clock = dt.datetime.fromisoformat((context.get("universe") or {}).get("clock_utc", context["freeze_utc"]).replace("Z", "+00:00"))
        clock_dates = tuple(sorted({freeze.date(), clock.date(), clock.astimezone(pacific()).date()}))
    ready = bool(context and (context.get("source") or {}).get("status") == "ready")
    mode = base if base != "auto" else ("search" if ready else "off")
    if mode != "off" and not ready and runner is None:
        report["base"]["errors"].append("base records were not read: " + (context_error or (context or {}).get("source", {}).get("reason", "no task context")))
        mode = "off"
    reader = BaseReader(task_dir, mode, sql, runner=runner) if mode != "off" else None
    if people is None:
        kb = (context or {}).get("source", {}).get("kb_path") if context else None
        people = People(Path(kb) / "entities.json" if kb else None)

    for ev in events:
        ev["ex"] = extract(ev["expected"] or "")
        ev["base_services"] = []
    last = []
    for ev in events:                                       # an event that names no service reads the one before it
        last = ev["services"] or last
        if ev["kind"] in ("read", "unknown"):
            ev["base_services"] = [s for s in last if s in BASE_FILES]
    by_n = {}
    for ev in events:
        by_n.setdefault(ev["n"], ev)
    for ev in events:
        for q in ev["ex"]["quotes"]:
            q["services"] = quote_services(ev, q, by_n)
    if reader:
        reader.lookup(_base_plan(events))
        budget, by_service = MAX_BASE_QUERIES, {}
        for ev in events:
            for q in ev["ex"]["quotes"] if ev["kind"] in ("read", "unknown") else ():
                inner = norm(q["text"])
                if len(inner) < MIN_BASE_QUOTE or inner in sql.by_title:
                    continue
                if not quantifier(ev["ex"], q) and any(quote_in(q["text"], r) for r in sql.records):
                    continue                     # in the injection SQL; a quote said to be in N records is searched anyway
                probes = _probes(q["text"])
                if not probes or budget <= 0:
                    continue
                for service in q["services"]:
                    if service in BASE_HEAVY and mode != "all":
                        continue
                    for probe in probes:
                        by_service.setdefault(service, {})[probe] = inner
                budget -= len(probes)
        for service in sorted(by_service):
            reader.search(service, by_service[service])
        report["base"].update(mode=mode, calls=reader.calls, errors=report["base"]["errors"] + reader.errors[:8],
                              skipped=sorted(set(reader.skipped)), records=len(reader.all_records()))

    checker = Checker(sql, reader, people, clock_dates)
    unresolved, results = [], []
    for ev in events:
        if ev["expected"]:
            checker.resolve(ev, ev["ex"])
            results += checker.check_event(ev)
            checker.earlier += "\n" + norm(ev["expected"])
        else:
            ev["records"] = []
        if ev["kind"] in ("read", "unknown") and ev["expected"] and not ev["records"]:
            unresolved.append(ev)
        report["events"].append({"n": ev["n"], "kind": ev["kind"], "services": ev["services"],
                                 "records": [r.rid for r in ev["records"][:12]], "record_count": len(ev["records"])})
    reads = [ev for ev in events if ev["kind"] in ("read", "unknown") and ev["expected"]]
    for ev in unresolved:
        hint = "name the record by id, exact title or a verbatim quote"
        if not reader:
            hint += "; base records were not read (--base search)"
        results.append({"event": ev["n"], "kind": "record", "qualifier": ev["head"][:100], "pos": -1, "scope": "event",
                        "result": "unverifiable", "record": None, "says": "no record resolved for this read event",
                        "prove": hint})
    detail = (f"{len(reads) - len(unresolved)} of {len(reads)} read events resolved to a record "
              f"({len(sql.records)} injected rows; base {report['base']['mode']}"
              + (f", {report['base'].get('records', 0)} base records read in {reader.calls} helper calls" if reader else "") + ")")
    others = [ev for ev in events if ev["kind"] in ("write", "derive")]
    if others:
        detail += f"; {len(others)} write or reasoning events are checked for dates, ids and reused values only"
    if unresolved:
        detail += "; not resolved: " + ", ".join(f"OE {ev['n']}" for ev in unresolved[:20]) + (" ..." if len(unresolved) > 20 else "")
    if report["base"]["errors"]:
        detail += "; " + "; ".join(report["base"]["errors"][:2])
    checks.append({"id": "oe.records", "status": "WARN" if unresolved or report["base"]["errors"] else "PASS", "detail": detail})

    tally = {k: 0 for k in ("supported", "contradicted", "unsupported", "unverifiable", "skipped")}
    by_kind = {}
    for r in results:
        tally[r["result"]] += 1
        by_kind.setdefault(r["kind"], {}).setdefault(r["result"], 0)
        by_kind[r["kind"]][r["result"]] += 1
    order = {"contradicted": 0, "unsupported": 1, "unverifiable": 2}
    findings += sorted((r for r in results if r["result"] in order),
                       key=lambda r: (order[r["result"]], r["event"], r["pos"], r["kind"], r["qualifier"]))
    for f in findings:
        f.pop("pos", None)
    checked = sum(tally.values()) - tally["skipped"]
    weak = sum(1 for r in results if r["result"] == "supported" and r.get("scope") == "corpus")
    status = "FAIL" if tally["contradicted"] else ("WARN" if tally["unsupported"] or tally["unverifiable"] else "PASS")
    detail = (f"{checked} qualifiers checked in {len(events)} events: {tally['supported']} supported"
              + (f" ({weak} only in a record of another event)" if weak else "")
              + f", {tally['contradicted']} contradicted, {tally['unsupported']} unsupported, {tally['unverifiable']} unverifiable"
              f"; {tally['skipped']} values the events produce were not checked")
    if tally["contradicted"]:
        detail += "; fix every contradicted value before /oe"
    checks.append({"id": "oe.qualifiers", "status": status, "detail": detail})
    report["counts"] = dict(tally, events=len(events), read=len(reads), unresolved=len(unresolved), checked=checked,
                            supported_elsewhere=weak)
    report["by_kind"] = by_kind
    statuses = [c["status"] for c in checks]
    report["verdict"] = "FAIL" if "FAIL" in statuses else ("WARN" if "WARN" in statuses else "PASS")
    return report


def finding_line(f: dict) -> str:
    status = "FAIL" if f["result"] == "contradicted" else "WARN"
    line = f"[{status}] oe.qualifiers: OE {f['event']} {f['kind']} \"{f['qualifier']}\" {f['result']}"
    if f.get("record"):
        line += f"; record {f['record']}"
    line += f": {f['says']}"
    if f.get("prove"):
        line += f"; to prove it: {f['prove']}"
    return line


def to_text(report: dict, name: str = "", ungrouped: bool = False) -> str:
    """Header, the three checks, then the findings. Contradicted and unsupported findings get a line each.
    Unverifiable ones of the same event, kind and reason share a line unless `ungrouped`."""
    n = report.get("counts", {}).get("events", 0)
    lines = [f"{TITLE} ({name + ', ' if name else ''}{n} events): {report['verdict']}"]
    for c in report["checks"]:
        lines.append(f"[{c['status']}] {c['id']}: {c['detail']}")
    groups, order = {}, []
    for f in report["findings"]:
        if ungrouped or f["result"] != "unverifiable":
            order.append(("one", f))
            continue
        key = (f["event"], f["kind"], f["says"] if f["kind"] not in ("date", "count") else "", f.get("prove") if f["kind"] != "count" else "")
        if key not in groups:
            groups[key] = []
            order.append(("group", key))
        groups[key].append(f)
    for tag, item in order:
        if tag == "one":
            lines.append(finding_line(item))
            continue
        members = groups[item]
        if len(members) == 1:
            lines.append(finding_line(members[0]))
            continue
        shown = "; ".join(f"\"{m['qualifier'][:60]}\"" for m in members[:8]) + (f"; +{len(members) - 8} more" if len(members) > 8 else "")
        first = members[0]
        lines.append(f"[WARN] oe.qualifiers: OE {first['event']} {len(members)} {first['kind']} qualifiers unverifiable ({shown}): "
                     f"{first['says']}" + (f"; to prove it: {first['prove']}" if first.get("prove") else ""))
    return "\n".join(lines)


# ------------------------------------------------------------------ CLI

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in argv:
        return _self_test()
    ap = argparse.ArgumentParser(prog="oe_qualifier_check.py", description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd")
    ck = sub.add_parser("check", help="check one task's Oracle Events")
    ck.add_argument("--task-dir", required=True, type=Path)
    ck.add_argument("--oe", type=Path, default=None, help="another Oracle Events file to check against this task")
    ck.add_argument("--base", choices=("auto", "off", "ids", "search", "all"), default="auto")
    ck.add_argument("--sql", type=Path, default=None, help="another injection SQL (an earlier round's)")
    ck.add_argument("--ungrouped", action="store_true", help="one line per unverifiable qualifier")
    ck.add_argument("--json", action="store_true")
    bt = sub.add_parser("backtest", help="run on the archived tasks and compare with the platform /oe reports")
    bt.add_argument("--root", type=Path, default=BUNDLE / "support" / "completed_tasks")
    bt.add_argument("--base", choices=("auto", "off", "ids", "search", "all"), default="auto")
    bt.add_argument("--only", default=None, help="archive name substring")
    bt.add_argument("--json", action="store_true")
    try:
        args = ap.parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code not in (0, None) else 0
    if args.cmd == "check":
        if not args.task_dir.is_dir():
            print(f"oe_qualifier_check: {args.task_dir} is not a folder", file=sys.stderr)
            return 2
        if args.oe and not args.oe.is_file():
            print(f"oe_qualifier_check: {args.oe} is not a file", file=sys.stderr)
            return 2
        report = evaluate(args.task_dir, oe=args.oe, base=args.base, sql=args.sql)
        name = args.task_dir.resolve().parent.name if args.task_dir.name == "task_inputs" else args.task_dir.resolve().name
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) if args.json
              else to_text(report, name, ungrouped=args.ungrouped))
        return 1 if report["verdict"] == "FAIL" else 0
    if args.cmd == "backtest":
        result = backtest(args.root, base=args.base, only=args.only)
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) if args.json else backtest_text(result))
        return 0
    ap.print_usage(sys.stderr)
    return 2


# ------------------------------------------------------------------ backtest

REPORT_FOLDERS = ("eval_reports", "Audit-Report", "plateform_reports", "platform_reports")
# Platform /oe findings on archived tasks (NON-FAIL 3 and FAIL rounds), one row per finding that concerns a value on
# an Expected line or a name in the call. `run` cases are rebuilt: the round's bytes when the archive has them
# (`oe`), else the final event with the defective wording put back (`old` -> `new`, or `new` appended). A case is a
# hit when the patched run has a finding on that event that names `needle` and the unpatched run does not.
# Rows with run=False are findings about meaning, parameters or cross-references: not reachable by a text check.
PLATFORM_CASES = (
    {"id": "douglas-35", "archive": "douglas_beta_server_signoff_2026-10-28", "round": "NON-FAIL (PARTIAL)", "event": 35, "run": True,
     "finding": "raw Linear state id state_5599a57e03a35620 is in no primary record", "type": "id",
     "old": '"Todo" exists for team ZOM, beside', "new": '"Todo" exists for team ZOM (state id state_5599a57e03a35620, type unstarted), beside',
     "needle": "state_5599a57e03a35620"},
    {"id": "winddown-r1-37", "archive": "robert_winddown_closeout_2026-10-30", "round": "FAIL 2 (minor item)", "event": 38, "run": True,
     "oe": "work/rb_winddown_closeout/v11_task_inputs/08_Oracle_Events.v11.md",
     "finding": "comment dates the last Typecast charge Aug 2025; the record shows Jul 2025", "type": "date in write content",
     "old": "(Leonard cancelled it in Jul 2025; free tier since)", "new": "(last charge Aug 2025)", "needle": "Aug 2025"},
    {"id": "winddown-r1-43", "archive": "robert_winddown_closeout_2026-10-30", "round": "FAIL 2 (minor item)", "event": 44, "run": True,
     "oe": "work/rb_winddown_closeout/v11_task_inputs/08_Oracle_Events.v11.md",
     "finding": "Kling comment invents a \"Sep 2025 trial\"", "type": "invented fact in write content",
     "old": "(dropped after Sep 2025)", "new": "(after the Sep 2025 trial)", "needle": "trial"},
    {"id": "winddown-r1-98", "archive": "robert_winddown_closeout_2026-10-30", "round": "FAIL 2 (minor item)", "event": 99, "run": True,
     "oe": "work/rb_winddown_closeout/v11_task_inputs/08_Oracle_Events.v11.md",
     "finding": "comment says canceled Oct 17; the notice says 10/16/25", "type": "date in write content",
     "old": "(account canceled Oct 16, 2025)", "new": "(account canceled Oct 17, 2025)", "needle": "Oct 17"},
    {"id": "winddown-r1-6", "archive": "robert_winddown_closeout_2026-10-30", "round": "FAIL 2 (minor item)", "event": 6, "run": True,
     "oe": "work/rb_winddown_closeout/v11_task_inputs/08_Oracle_Events.v11.md",
     "finding": "project name typed with a hyphen instead of the record's en dash", "type": "name in the call",
     "old": "open the one named Shutdown, en dash, accounts", "new": 'open the project "Shutdown - accounts"',
     "needle": "Shutdown - accounts"},
    {"id": "winddown-r2-5", "archive": "robert_winddown_closeout_2026-10-30", "round": "NON-FAIL 3", "event": 5, "run": True,
     "oe": "work/rb_winddown_closeout/v11_task_inputs/08_Oracle_Events.v11.md",
     "finding": "quoted doc text starts with a heading the doc does not have", "type": "quote",
     "old": '"Close-out register conventions 1. One row per vendor account.',
     "new": '"Close-out register - how we fill it in 1. One row per vendor account.', "needle": "how we fill it in"},
    {"id": "winddown-r5-21", "archive": "robert_winddown_closeout_2026-10-30", "round": "NON-FAIL 3", "event": 21, "run": True,
     "finding": "both Singular invoices said to be $6,250 a quarter; one is $25,000.00 for the year", "type": "amount bound to the wrong item",
     "old": "With Leonard's ENG-2444 comment", "new": "Quarterly $6,250 invoices on Sep 1 and Dec 1 2025. With Leonard's ENG-2444 comment",
     "needle": "6,250"},
    {"id": "winddown-r5-25", "archive": "robert_winddown_closeout_2026-10-30", "round": "NON-FAIL 3", "event": 25, "run": True,
     "finding": "credits the project description with saying two lines \"are not company accounts\"", "type": "paraphrase of a record",
     "old": None, "new": " The two $30 game-ops lines, which Arthur's project description says are not company accounts to settle here, stay off.",
     "needle": "company accounts"},
    {"id": "winddown-r7-21", "archive": "robert_winddown_closeout_2026-10-30", "round": "NON-FAIL 3", "event": 21, "run": True,
     "finding": "\"Two invoice mails\" but the mailbox holds four", "type": "count of a collection",
     "old": "Robert's mailbox holds four Singular invoice mails:", "new": "Two invoice mails:", "needle": "two invoice mails"},
    {"id": "seedbets-16", "archive": "robert_seed_bets_2026-11-11", "round": "NON-FAIL 3", "event": 16, "run": True,
     "finding": "all five receipts said to read \"Lucas can now pick up the money\"; four read another name", "type": "quote applied to too many records",
     "old": 'the Jun 17 one opens "Lucas can now pick up the money" and the other four open "PERSON_R001 can now pick up the money"',
     "new": 'all five read "Lucas can now pick up the money"', "needle": "lucas can now"},
    {"id": "bridge-r2-7", "archive": "frederick_bridge_pipeline_2026-11-03", "round": "NON-FAIL 3", "event": 7, "run": True,
     "finding": "a Sep 23 quote reads as BITKRAFT not responding; it is about Play Ventures", "type": "quote attributed to the wrong subject",
     "old_re": r'Tue Sep 23 4:55 PM PT, Leonard answering Robert\'s .*?their no\)\.', "new": 'Tue Sep 23: "I just checked, they didn’t respond".',
     "needle": "sep 23"},
    {"id": "bridge-r1-28", "archive": "frederick_bridge_pipeline_2026-11-03", "round": "NON-FAIL 3", "event": 28, "run": True,
     "finding": "48 names described as \"nothing from us since Sep 3\"; two had contact", "type": "absence",
     "old": None, "new": " The 48 other list names have nothing from us since Sep 3.", "needle": "nothing"},
    {"id": "q4-14", "archive": "frederick_q4_commitments_2026-11-05", "round": "NON-FAIL 3", "event": 14, "run": True,
     "finding": "\"Frederick's reply went to Leonard only\"; it is an unsent draft", "type": "state of a record",
     "old_re": r"Frederick's reply to it is an unsent draft addressed to Leonard, labelled \"Opened,Drafts\", so nobody answered Rayking",
     "new": "Frederick's reply went to Leonard only", "needle": "only"},
    {"id": "owen-r1-13", "archive": "owen_dd_bug_carryover_2026-11-09", "round": "FAIL 2 (minor item)", "event": 13, "run": True,
     "finding": "\"under his post\" calls Robert's post Brian's", "type": "author by pronoun",
     "old": "under Robert's post", "new": "under his post", "needle": "his post"},
    {"id": "owen-r2-30", "archive": "owen_dd_bug_carryover_2026-11-09", "round": "NON-FAIL 3", "event": 30, "run": True,
     "finding": "\"the fix is in EconomyChanges build #2297\"; that build failed", "type": "status of a cited record",
     "old_re": r"the fix is on EconomyChanges, listed in build #2297's changes: that build failed, and #2299 on the same branch succeeded on Dec 10, OE 17",
     "new": "the fix is in EconomyChanges build #2297", "needle": "#2297"},
    {"id": "vincent-14", "archive": "vincent_zm3d_release_gate_2026-11-06", "round": "NON-FAIL 3", "event": 14, "run": True,
     "oe": "task_inputs/Working_Files/research/oe/08_Oracle_Events.3ddf0464_before_rev.md",
     "finding": "ZOM-293 listed among bugs that \"still fail\"; nobody re-tested it", "type": "status qualifier",
     "old": None, "new": None, "needle": "zom-293"},
    {"id": "douglas-43", "archive": "douglas_beta_server_signoff_2026-10-28", "round": "NON-FAIL (PARTIAL)", "event": 43, "run": False,
     "finding": "comment names the wrong approval condition", "type": "meaning"},
    {"id": "bridge-r1-8a", "archive": "frederick_bridge_pipeline_2026-11-03", "round": "NON-FAIL 3", "event": 8, "run": False,
     "finding": "\"Raine, Sep 3 2:17 PM PT\" cites a thread that goes to another firm", "type": "wrong record for a name (round text not kept)"},
    {"id": "bridge-r1-8b", "archive": "frederick_bridge_pipeline_2026-11-03", "round": "NON-FAIL 3", "event": 8, "run": False,
     "finding": "Superplay outreach mail goes to Supercell's lead", "type": "wrong record for a name (round text not kept)"},
    {"id": "bridge-r1-6", "archive": "frederick_bridge_pipeline_2026-11-03", "round": "NON-FAIL 3", "event": 6, "run": False,
     "finding": "a list of remaining meetings leaves out the recurring ones", "type": "meaning"},
    {"id": "bridge-r1-7", "archive": "frederick_bridge_pipeline_2026-11-03", "round": "NON-FAIL 3", "event": 7, "run": False,
     "finding": "description of a record's sections is imprecise", "type": "meaning"},
    {"id": "q4-14-window", "archive": "frederick_q4_commitments_2026-11-05", "round": "NON-FAIL 3", "event": 14, "run": False,
     "finding": "unsourced search window", "type": "parameter"},
    {"id": "julia-13", "archive": "julia_zm_difficulty_baseline_2026-11-01", "round": "NON-FAIL 3", "event": 13, "run": False,
     "finding": "Expected line cites the wrong OEs for a reason", "type": "cross-reference"},
    {"id": "julia-19", "archive": "julia_zm_difficulty_baseline_2026-11-01", "round": "NON-FAIL 3", "event": 19, "run": False,
     "finding": "a rule checked on one PR of four", "type": "meaning"},
    {"id": "leonard-r1-17", "archive": "leonard_stockholder_closeout_2026-11-10", "round": "FAIL 2 (minor item)", "event": 17, "run": False,
     "finding": "search limited to Slack, one word and a date range", "type": "parameter"},
    {"id": "leonard-r1-21", "archive": "leonard_stockholder_closeout_2026-11-10", "round": "FAIL 2 (minor item)", "event": 21, "run": False,
     "finding": "vesting term assumed; ES-9 called an advisor grant, the schedule says Board member", "type": "meaning"},
    {"id": "leonard-r2-21", "archive": "leonard_stockholder_closeout_2026-11-10", "round": "NON-FAIL 3", "event": 21, "run": False,
     "finding": "says the consent PDF cannot be opened; it can", "type": "meaning"},
    {"id": "owen-r1-26", "archive": "owen_dd_bug_carryover_2026-11-09", "round": "FAIL 2 (minor item)", "event": 26, "run": False,
     "finding": "two posts rest on a DM that names no build", "type": "meaning"},
    {"id": "owen-r1-8", "archive": "owen_dd_bug_carryover_2026-11-09", "round": "FAIL 2 (minor item)", "event": 8, "run": False,
     "finding": "wrong OE range in a cross-reference", "type": "cross-reference"},
    {"id": "owen-r2-26", "archive": "owen_dd_bug_carryover_2026-11-09", "round": "NON-FAIL 3", "event": 26, "run": False,
     "finding": "state filter (Bugs and Todo) narrower than \"open\"", "type": "parameter"},
    {"id": "seedbets-31", "archive": "robert_seed_bets_2026-11-11", "round": "NON-FAIL 3", "event": 31, "run": False,
     "finding": "two content rules no record supports", "type": "meaning"},
    {"id": "winddown-r1-2", "archive": "robert_winddown_closeout_2026-10-30", "round": "FAIL 2 (minor item)", "event": 2, "run": False,
     "finding": "\"before the newest 100 messages\" misplaces a message", "type": "parameter"},
    {"id": "winddown-r1-99", "archive": "robert_winddown_closeout_2026-10-30", "round": "FAIL 2 (minor item)", "event": 99, "run": False,
     "finding": "unrequested writes listed as required", "type": "meaning"},
    {"id": "winddown-r1-23", "archive": "robert_winddown_closeout_2026-10-30", "round": "FAIL 2 (minor item)", "event": 23, "run": False,
     "finding": "rows do not say where the vendor confirmed", "type": "meaning"},
    {"id": "winddown-r6-21", "archive": "robert_winddown_closeout_2026-10-30", "round": "NON-FAIL 3", "event": 21, "run": False,
     "finding": "values taken from PDF attachments the agent cannot read", "type": "meaning"},
)


def read_oe_report(path) -> dict | None:
    """Verdict, score and reviewed-OE hash of one platform /oe report, or None when it is not one."""
    text = Path(path).read_text(errors="replace")
    verdict = re.search(r"FINAL VERDICT:\s*\**\s*(PASS|NON-FAIL|FAIL)", text)
    if not verdict:
        return None
    score = re.search(r"^Score:\s*\**\s*(\d)", text, re.M)
    sha = re.search(r"Reviewed OE SHA-256:\s*`?([0-9a-f]{64})", text) or re.search(r"Oracle Events[^\n]*?([0-9a-f]{64})", text)
    return {"path": str(path), "verdict": verdict.group(1), "score": int(score.group(1)) if score else None,
            "oe_sha": sha.group(1) if sha else None, "sha": hashlib.sha256(text.encode()).hexdigest()}


def archive_reports(archive: Path) -> list:
    out, seen = [], set()
    for path in sorted(archive.rglob("*.md")):
        if "2_oe" not in path.name or not any(part in REPORT_FOLDERS for part in path.parts):
            continue
        rep = read_oe_report(path)
        if rep and rep["sha"] not in seen:
            seen.add(rep["sha"])
            out.append(rep)
    return out


def _patch(text: str, case: dict):
    """The OE text with the case's defective wording put back into its event, or (None, why)."""
    lines = text.splitlines(keepends=True)
    starts = [i for i, line in enumerate(lines) if RX_HEAD.match(line)]
    block = next(((i, starts[k + 1] if k + 1 < len(starts) else len(lines)) for k, i in enumerate(starts)
                  if int(RX_HEAD.match(lines[i]).group(1)) == case["event"]), None)
    if block is None:
        return None, f"OE {case['event']} not found"
    body = "".join(lines[block[0]:block[1]])
    if case.get("new") is None:
        return text, None
    if case.get("old_re"):
        new_body, n = re.subn(case["old_re"], lambda m: case["new"], body, count=1, flags=re.S)
    elif case.get("old"):
        n = body.count(case["old"])
        new_body = body.replace(case["old"], case["new"], 1)
    else:
        stripped = body.rstrip("\n")
        new_body, n = stripped + case["new"] + body[len(stripped):], 1
    if not n:
        return None, "the wording to replace is not in the event"
    return "".join(lines[:block[0]]) + new_body + "".join(lines[block[1]:]), None


def _new_findings(before: list, after: list) -> list:
    """Findings of `after` that `before` does not have, counted as a multiset: a second "nothing" on the same event
    is new even though the first one was already there."""
    left = {}
    for f in before:
        key = (f["event"], f["kind"], f["qualifier"], f["result"])
        left[key] = left.get(key, 0) + 1
    out = []
    for f in after:
        key = (f["event"], f["kind"], f["qualifier"], f["result"])
        if left.get(key):
            left[key] -= 1
        else:
            out.append(f)
    return out


def _part1_row(archive: str, file: str, status: str, rep: dict) -> dict:
    return {"archive": archive, "file": file, "status": status, "ran": True, "verdict": rep["verdict"],
            "counts": rep["counts"], "base": rep["base"]["mode"], "base_errors": rep["base"]["errors"][:1],
            "contradicted": [f for f in rep["findings"] if f["result"] == "contradicted"],
            "unsupported": [f for f in rep["findings"] if f["result"] == "unsupported"],
            "unverifiable_by_kind": {k: v.get("unverifiable", 0) for k, v in sorted(rep["by_kind"].items()) if v.get("unverifiable")}}


def backtest(root, base="auto", only=None, runner=None) -> dict:
    """Part 1: the final Oracle Events of every archive, against its last /oe verdict. Part 2: PLATFORM_CASES."""
    root = Path(root)
    part1, part2 = [], []
    archives = [d for d in sorted(root.iterdir()) if d.is_dir() and (not only or only in d.name)] if root.is_dir() else []
    for archive in archives:
        task = archive / "task_inputs"
        final = task / OE_FILE
        if not final.is_file() or not final.read_text(errors="replace").strip():
            part1.append({"archive": archive.name, "status": "no Oracle Events file", "ran": False})
            continue
        digest = sha256(final)
        reports = archive_reports(archive)
        bound = [r for r in reports if r["oe_sha"] == digest]
        passed = [r for r in reports if r["verdict"] == "PASS" and r["score"] == 5]
        if any(r in passed for r in bound):
            status = "PASS 5"
        elif bound:
            status = "/".join(sorted({f"{r['verdict']} {r['score']}" for r in bound}))
        elif passed:
            status = "PASS 5 (the report does not name the OE hash)"     # the archive's last /oe report passed
        elif reports:
            status = "final bytes not in a stored report"
        else:
            status = "no /oe report"
        rep = evaluate(task, base=base, runner=runner)
        part1.append(_part1_row(archive.name, OE_FILE, status, rep))
        # An earlier stored copy of the events that a PASS 5 report names, checked with the SQL of its own round.
        seen = {digest}
        for path in sorted(archive.rglob("08_Oracle_Events*.md")):
            other = sha256(path)
            named = [r for r in passed if r["oe_sha"] == other]
            if other in seen or not named:
                continue
            seen.add(other)
            rel_path = str(path.relative_to(archive))
            sql_path = path.parent / SQL_FILE
            if not sql_path.is_file():
                part1.append({"archive": archive.name, "file": rel_path, "status": "PASS 5", "ran": False,
                              "why": "no injection SQL of that round is stored next to it"})
                continue
            rep = evaluate(task, oe=path, sql=sql_path, base=base, runner=runner)
            part1.append(_part1_row(archive.name, rel_path, "PASS 5", rep))
    groups = {}
    for case in PLATFORM_CASES:
        if only and only not in case["archive"]:
            continue
        if not case["run"]:
            part2.append(dict(id=case["id"], archive=case["archive"], round=case["round"], event=case["event"],
                              finding=case["finding"], type=case["type"], outcome="not reachable", detail="not run: " + case["type"]))
            continue
        groups.setdefault((case["archive"], case.get("oe")), []).append(case)
    for (name, oe_rel), cases in sorted(groups.items(), key=lambda kv: (kv[0][0], kv[0][1] or "")):
        archive = root / name
        task = archive / "task_inputs"
        oe_path = archive / oe_rel if oe_rel else task / OE_FILE
        sql_path = oe_path.parent / SQL_FILE if (oe_path.parent / SQL_FILE).is_file() else task / SQL_FILE
        if not oe_path.is_file():
            part2 += [dict(id=c["id"], archive=name, round=c["round"], event=c["event"], finding=c["finding"], type=c["type"],
                           outcome="not rebuilt", detail=f"{oe_rel or OE_FILE} is not in the archive") for c in cases]
            continue
        text = oe_path.read_text(errors="replace")
        sql_text = sql_path.read_text(errors="replace") if sql_path.is_file() else ""
        patched, failed = text, {}
        for case in cases:
            got, why = _patch(patched, case)
            if got is None:
                failed[case["id"]] = why
            else:
                patched = got
        before = check_text(task, text, sql_text, base=base, runner=runner)
        after = check_text(task, patched, sql_text, base=base, runner=runner) if patched != text else before
        new_findings = _new_findings(before["findings"], after["findings"])
        for case in cases:
            row = dict(id=case["id"], archive=name, round=case["round"], event=case["event"], finding=case["finding"],
                       type=case["type"], source="round bytes" if oe_rel and case.get("new") is None else
                       ("rebuilt on " + (Path(oe_rel).name if oe_rel else "the final file")), base=after["base"]["mode"])
            if case["id"] in failed:
                part2.append(dict(row, outcome="not rebuilt", detail=failed[case["id"]]))
                continue
            pool = after["findings"] if case.get("new") is None else \
                new_findings
            hits = [f for f in pool if f["event"] == case["event"]
                    and case["needle"].casefold() in (f["qualifier"] + " " + f["says"]).casefold()]
            if hits:
                best = min(hits, key=lambda f: ("contradicted", "unsupported", "unverifiable").index(f["result"]))
                part2.append(dict(row, outcome="flagged " + best["result"], detail=finding_line(best)[:300]))
            else:
                part2.append(dict(row, outcome="missed", detail="no finding on this event names the defective value"))
    pass5 = [r for r in part1 if r.get("ran") and r.get("status", "").startswith("PASS 5")]
    ran2 = [r for r in part2 if r["outcome"].startswith(("flagged", "missed"))]
    summary = {"archives": len(archives), "files": len(part1), "pass5_final": len(pass5),
               "unverifiable_on_pass5": sum(r["counts"]["unverifiable"] for r in pass5),
               "checked_on_pass5": sum(r["counts"]["checked"] for r in pass5),
               "pass5_with_fail": sum(1 for r in pass5 if r["contradicted"]),
               "fail_findings_on_pass5": sum(len(r["contradicted"]) for r in pass5),
               "unsupported_on_pass5": sum(len(r["unsupported"]) for r in pass5),
               "platform_findings": len(part2), "run": len(ran2),
               "flagged_contradicted": sum(1 for r in part2 if r["outcome"] == "flagged contradicted"),
               "flagged_unsupported": sum(1 for r in part2 if r["outcome"] == "flagged unsupported"),
               "flagged_unverifiable": sum(1 for r in part2 if r["outcome"] == "flagged unverifiable"),
               "missed": sum(1 for r in part2 if r["outcome"] == "missed"),
               "not_reachable": sum(1 for r in part2 if r["outcome"] == "not reachable"),
               "not_rebuilt": sum(1 for r in part2 if r["outcome"] == "not rebuilt")}
    return {"tool": TOOL, "version": VERSION, "root": str(root), "summary": summary, "final_files": part1, "platform_findings": part2}


def backtest_text(result: dict) -> str:
    s = result["summary"]
    lines = [f"OE QUALIFIER BACKTEST ({s['archives']} archives): {s['fail_findings_on_pass5']} FAIL findings on "
             f"{s['pass5_final']} Oracle Events files the platform passed with 5 ({s['unsupported_on_pass5']} unsupported, "
             f"{s['unverifiable_on_pass5']} unverifiable of {s['checked_on_pass5']} checked); "
             f"{s['flagged_contradicted'] + s['flagged_unsupported'] + s['flagged_unverifiable']} of {s['run']} rebuilt platform findings flagged"]
    lines.append("Part 1 - final Oracle Events of each archive (and earlier copies a PASS 5 report names)")
    for r in result["final_files"]:
        name = r["archive"] + ("" if r.get("file", OE_FILE) == OE_FILE else f" [{r['file']}]")
        if not r["ran"]:
            lines.append(f"  {name}: {r['status']}" + (f"; not run: {r['why']}" if r.get("why") else ""))
            continue
        c = r["counts"]
        lines.append(f"  {name}: platform {r['status']}; tool {r['verdict']} (base {r['base']}); {c['supported']} supported, "
                     f"{c['contradicted']} contradicted, {c['unsupported']} unsupported, {c['unverifiable']} unverifiable "
                     f"({', '.join(f'{k} {v}' for k, v in r.get('unverifiable_by_kind', {}).items())}); "
                     f"{c['read'] - c['unresolved']} of {c['read']} read events resolved"
                     + (f"; base: {r['base_errors'][0][:160]}" if r.get("base_errors") else ""))
        for f in r["contradicted"] + r["unsupported"]:
            lines.append("      " + finding_line(f)[:420])
    lines.append("Part 2 - platform /oe findings (NON-FAIL 3 and FAIL rounds)")
    for r in result["platform_findings"]:
        lines.append(f"  {r['id']} (OE {r['event']}, {r['round']}; {r['type']}): {r['finding']} -> {r['outcome']}"
                     + (f" [{r.get('source')}, base {r.get('base')}]" if r.get("source") else ""))
        if r["outcome"].startswith("flagged") or r["outcome"] == "not rebuilt":
            lines.append("      " + r["detail"])
    lines.append(f"Totals: {s['run']} findings run: {s['flagged_contradicted']} flagged contradicted, {s['flagged_unsupported']} unsupported, "
                 f"{s['flagged_unverifiable']} unverifiable, {s['missed']} missed; {s['not_reachable']} not reachable by a text check; "
                 f"{s['not_rebuilt']} not rebuilt")
    return "\n".join(lines)


# ------------------------------------------------------------------ self-test

SELFTEST_SQL = """-- synthetic rows for the self-test (never executed)
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, reply_count, created_at)
VALUES ('m1', '1759269913.882683', 'C0TEST00001', 'message', 'U_LEO', 'please move the three bug tickets to Done before friday''s review', NULL, 0, '2025-09-30T22:05:13Z');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, reply_count, created_at)
VALUES ('m2', '1759270513.000100', 'C0TEST00001', 'message', 'U_LEO', 'and leave ZOM-9 alone — it is not ours', 'm1', 0, '2025-09-30T22:15:13Z');
UPDATE slack.slack_messages SET reply_count = 1 WHERE id = 'm1';
INSERT INTO linear.linear_issues (id, identifier, team_id, state_id, title, description, created_at, updated_at)
VALUES ('ZOM-7', 'ZOM-7', 'team_ZOM', 'Todo', 'Crash on level 12', 'Seen on 0.3.49. Costs $1,250.00 a month.', '2025-09-29T17:15:00Z', '2025-09-29T17:15:00Z');
INSERT INTO linear.linear_issues (id, identifier, team_id, state_id, title, description, created_at, updated_at)
VALUES ('ZOM-8', 'ZOM-8', 'team_ZOM', 'Todo', 'Tier resets', 'After a reload.', '2025-09-29T17:20:00Z', '2025-09-29T17:20:00Z');
UPDATE linear.linear_issues SET state_id = 'In Progress' WHERE id = 'ZOM-8';
INSERT INTO linear.linear_issues (id, identifier, team_id, state_id, title, description, created_at, updated_at)
VALUES ('ZOM-9', 'ZOM-9', 'team_ZOM', 'Todo', 'Old art', 'Not ours.', '2025-09-29T17:25:00Z', '2025-09-29T17:25:00Z');
INSERT INTO gdocs.docs_documents (document_id, title, owner_email, body_text, created_time, modified_time)
VALUES ('f_doc0001', 'Bug review rules', 'leo@example.co', 'Rule 1: a ticket counts once QA has seen it on both builds.', '2025-09-26T16:00:00Z', '2025-09-28T18:30:00Z');
"""
SELFTEST_OE = """OE 1  Read Leo's ask in #bugs in Slack (latest messages)
Expected: Leo, Tue Sep 30 2025 3:05 PM PT (22:05 UTC), message ts 1759269913.882683: "please move the three bug tickets to Done before friday's review". It has one reply.

OE 2  Open the thread under that message (Slack replies)
Expected: Leo, Tue Sep 30 2025 3:15 PM PT: "and leave ZOM-9 alone — it is not ours"

OE 3  List the bug tickets in Linear (team ZOM)
Expected: 3 issues: ZOM-7 "Crash on level 12" (Todo); ZOM-8 "Tier resets" (In Progress); ZOM-9 "Old art" (Todo). ZOM-7 costs $1,250.00 a month and was seen on 0.3.49.

OE 4  Read the rules doc in Docs (search "Bug review rules")
Expected: Doc "Bug review rules", owner leo@example.co, created Fri Sep 26 2025 9:00 AM PT: "a ticket counts once QA has seen it on both builds".

OE 5  Move ZOM-7 to Done (Linear update)
Expected: ZOM-7 is Done.
"""
SELFTEST_PEOPLE = {"entities": [
    {"entity_id": "p:leo", "kind": "person", "canonical_name": "Leo Hart", "names": ["Leo Hart"], "emails": ["leo@example.co"],
     "identities": {"slack": [{"id": "U_LEO"}]}},
    {"entity_id": "p:ann", "kind": "person", "canonical_name": "Ann Vale", "names": ["Ann Vale"], "emails": ["ann@example.co"],
     "identities": {"slack": [{"id": "U_ANN"}]}}]}


def _selftest_run(tmp, oe_text, sql_text=SELFTEST_SQL):
    task = Path(tmp)
    (task / OE_FILE).write_text(oe_text)
    (task / SQL_FILE).write_text(sql_text)
    return evaluate(task, base="off", people=People(data=SELFTEST_PEOPLE))


def _self_test() -> int:
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("oe_qualifier_selftest_") as tmp:
        good = _selftest_run(tmp, SELFTEST_OE)
        assert good["verdict"] == "PASS", to_text(good)
        assert good["counts"]["contradicted"] == 0 and good["counts"]["unsupported"] == 0, to_text(good)
        assert good == _selftest_run(tmp, SELFTEST_OE), "two runs differ"

        def bad(old, new, kind, result, check="oe.qualifiers"):
            assert old in SELFTEST_OE, old
            rep = _selftest_run(tmp, SELFTEST_OE.replace(old, new, 1))
            hits = [f for f in rep["findings"] if f["kind"] == kind and f["result"] == result]
            assert hits, f"{new!r}: expected a {result} {kind}\n{to_text(rep)}"
            status = {c["id"]: c["status"] for c in rep["checks"]}[check]
            assert status == ("FAIL" if result == "contradicted" else "WARN"), (new, status)
            assert (rep["verdict"] == "FAIL") == (result == "contradicted"), to_text(rep)
            return hits[0]

        bad("3:05 PM PT (22:05 UTC)", "3:25 PM PT (22:25 UTC)", "date", "contradicted")          # the message's ts
        bad("Tue Sep 30 2025 3:05", "Wed Sep 30 2025 3:05", "date", "contradicted")               # weekday
        bad("(22:05 UTC)", "(21:05 UTC)", "date", "contradicted")                                 # PT against UTC
        bad("Leo, Tue Sep 30 2025 3:15", "Ann, Tue Sep 30 2025 3:15", "name", "contradicted")      # author
        bad("It has one reply", "It has two replies", "count", "contradicted")                    # reply_count after the UPDATE
        bad('"Tier resets" (In Progress)', '"Tier resets" (Todo)', "state", "contradicted")       # state after the UPDATE
        bad("owner leo@example.co", "owner ann@example.co", "name", "contradicted")               # owner
        bad("created Fri Sep 26 2025 9:00 AM PT", "created Fri Sep 26 2025 9:40 AM PT", "date", "contradicted")
        near = bad("please move the three bug tickets to Done", "Please move the three bug tickets to done", "quote",
                   "unsupported")                                                                  # other case
        assert "character for character" in near["says"], near
        rep = _selftest_run(tmp, SELFTEST_OE.replace("alone — it is not ours", "alone - it is not ours"))
        assert rep["verdict"] == "PASS", to_text(rep)                                              # a dash variant passes
        bad("seen it on both builds", "seen it on every build", "quote", "unverifiable")           # base not read
        bad("$1,250.00", "$1,350.00", "amount", "unverifiable")
        bad("0.3.49.", "0.3.50.", "version", "unverifiable")
        bad("Expected: 3 issues:", "Expected: The only open tickets, 3 issues:", "superlative", "unverifiable")
        rep = _selftest_run(tmp, SELFTEST_OE + "\nOE 6  Read the March invoice in Gmail (search \"invoice\")\nExpected: An invoice for 40 seats.\n")
        assert {c["id"]: c["status"] for c in rep["checks"]}["oe.records"] == "WARN" and rep["counts"]["unresolved"] == 1, to_text(rep)
        rep = _selftest_run(tmp, SELFTEST_OE + "\nOE 7  Read the board\n")
        assert {c["id"]: c["status"] for c in rep["checks"]}["oe.parse"] == "WARN", to_text(rep)
        variants = "## OE 1 - Read the doc in Docs\n**Expected data:** Doc \"Bug review rules\".\n\n**OE 2**: Read it again\nThe agent finds \"a ticket counts once QA has seen it on both builds\".\n"
        rep = _selftest_run(tmp, variants)
        assert rep["counts"]["events"] == 2 and rep["verdict"] == "PASS", to_text(rep)
        rep = _selftest_run(tmp, "")
        assert rep["verdict"] == "FAIL" and rep["checks"][0]["id"] == "oe.parse", rep
    print("self-test: ok (parser variants; date, time zone, weekday, author, reply count, state, owner contradicted; "
          "quote in other case unsupported, dash variant supported; quote, amount, version, superlative unverifiable; unresolved record; "
          "event without Expected; empty file; determinism)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
