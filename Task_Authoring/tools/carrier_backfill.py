#!/usr/bin/env python3
"""carrier_backfill.py - how often each carrier's deciding record was opened, measured on the archived runs.

Plan RC1 says a designed miss works or leaks because of its carrier (where the deciding record sits and how it is
reached), not because of its mechanism family. This tool builds the table behind that claim (plan WS2 item 4 and
WS7 item 4): per designed unit and per run, was the deciding record opened, and did the run get the unit's rubric
rows right. `difficulty_budget.py` and `path_exposure.py` read the result.

Input   references/carrier_backfill_units.json (schema carrier-backfill-units-v1): curated by hand, one entry per
        designed unit per task revision that was run, with the deciding record, the carrier label and the evidence.
Output  references/carrier_find_rates.json (schema carrier-find-rates-v1): the per-unit, per-run records and one
        aggregate per carrier and per retrieval habit, always with the raw counts.

How "opened" is decided (one rule for every service):
  opened        a tool result shows the record's own text: a 40-character window that starts after the first 100
                characters of the record (the whole text when it is shorter), or the unit's own `needles`. Gmail
                bodies are base64 in the export and are decoded first. A thread fetch, a channel listing, a search
                or a shell command that prints the text all count: the text was in front of the model.
                Also opened: a read call that names the record's own id and whose result was too large and went to
                a file (how = direct_get_spilled), since the model asked for exactly that record.
                A base record without `needles` is opened when a result holds an object with its id and a content
                field (how = object); a Slack result always prints the whole message.
  snippet_only  only the record's id, or only its first 40 characters, was seen (a search hit, a thread list, a
                `format: minimal` fetch). Not counted as opened; reported beside it.
  container     the first read call whose arguments name the record's container (thread, channel, ticket, file).
                A container read that spilled to a file and never showed the text is NOT counted as opened.
Results of write calls are ignored (they echo what the model wrote). Subagent calls count like main-agent calls.

Usage (from the workspace root):
  python3.12 -B Task_Authoring/tools/carrier_backfill.py compute [--units FILE] [--tasks-root DIR] [--task NAME ...]
        [--write] [--out FILE] [--detail] [--json]
  python3.12 -B Task_Authoring/tools/carrier_backfill.py show [--carrier NAME] [--rates FILE] [--json]
  python3.12 -B Task_Authoring/tools/carrier_backfill.py --self-test
Exit 0 = PASS or WARN, 1 = FAIL, 2 = usage error. Read-only on the archives; never executes SQL.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
import os
import re
import statistics
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
WS = BUNDLE.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

TOOL = "carrier_backfill"
VERSION = 1
SCHEMA_UNITS = "carrier-backfill-units-v1"
SCHEMA_RATES = "carrier-find-rates-v1"
UNITS_PATH = BUNDLE / "references" / "carrier_backfill_units.json"
RATES_PATH = BUNDLE / "references" / "carrier_find_rates.json"
POLICY_PATH = BUNDLE / "references" / "first_pass_policy.json"
TASKS_ROOT = BUNDLE / "support" / "completed_tasks"

# Module constants (not in first_pass_policy.json; listed in the hand-over report).
HEAD_CHARS = 100        # a search hit or thread list prints at most this much of a record (the Gmail snippet length)
WINDOW = 40             # needle length; the same window trajectory_ledger and node_verdicts use
MAX_WINDOWS = 6         # text windows taken per SQL row
MIN_NEEDLE = 16         # shorter text is not used as a needle (too easy to match by accident)
SMALL_SAMPLE_RUNS = 12  # a carrier with fewer counted runs gets a small-sample warning
AGGREGATE_CONFIDENCE = ("high", "medium")   # low-confidence units stay in the unit list, out of the aggregates

RUN_SETS = ("precheck", "baseline")
CONFIDENCE = ("high", "medium", "low")
UNIT_FIELDS = ("task", "revision", "run_set", "unit", "mechanism_family", "decider", "carrier", "habit", "rows",
               "evidence", "confidence", "note")
ID_COLS = ("id", "identifier", "event_id", "document_id", "spreadsheet_id", "presentation_id", "object_id",
           "contact_id", "sha")
TEXT_COLS = ("text", "body", "body_text", "description", "desc", "content", "snippet", "summary", "title", "name",
             "subject", "notes", "data_json", "grid_json")
CONTENT_KEYS = ("text", "body", "body_text", "description", "desc", "content", "plain_text", "markdown")
OBJECT_ID_KEYS = ("id", "ts", "identifier", "message_id", "threadId", "documentId", "spreadsheetId",
                  "presentationId", "key")
HARNESS_WRITES = ("Write", "Edit", "MultiEdit", "NotebookEdit")
RX_SLACK_ID = re.compile(r"^([CDG][A-Z0-9]{6,})/(\d{9,}\.\d+)$")
RX_B64 = re.compile(r"^[A-Za-z0-9_\-+/]{24,}={0,2}$")
RX_B64_RUN = re.compile(r"[A-Za-z0-9_\-+/]{64,}={0,2}")   # a body inside a longer string (a spilled file read back)
RX_U = re.compile(r"\\u([0-9a-fA-F]{4})")
DROP = {ord(c): None for c in "\"'`\\‘’“”"}

# Carrier label against what the SQL row is. A mismatch is a warning: the label is a judgement, the row is a fact.
STRUCTURE_RULES = {
    "reply_under_unrelated_parent": ("is_reply", "the record is not a thread or mail reply in the SQL"),
    "de_named_correction_reply": ("is_reply", "the record is not a thread or mail reply in the SQL"),
    "dm_with_non_owner": ("is_dm", "the record is not in a Slack DM channel (id starting with D)"),
    "email_reply_via_get_thread": ("is_mail_reply", "the record is not a later message of a Gmail thread"),
    "non_set_ticket": ("is_ticket", "the record is not a Linear, Trello or GitHub ticket row or a comment on one"),
    "second_tab": ("is_later_tab", "the record is not a sheet tab after the first"),
    "checklist": ("is_checklist", "the record is not a Trello checklist row"),
}


# ------------------------------------------------------------------ small helpers

def _tl():
    import trajectory_ledger
    return trajectory_ledger


def _parse_sql(text: str) -> list:
    from base_check import parse_sql
    return parse_sql(text)


def norm_text(value) -> str:
    """One normal form for record text, ids and tool results: lower case, single spaces, no quotes or backslashes.

    Literal escapes (\\n, \\r, \\t, \\u2019) appear both in SQL strings and in JSON printed by a shell command, so
    they are resolved before the backslashes go."""
    s = RX_U.sub(lambda m: chr(int(m.group(1), 16)), str(value))
    s = s.replace("\\r", " ").replace("\\n", " ").replace("\\t", " ")
    s = html.unescape(s).translate(DROP)
    return re.sub(r"\s+", " ", s).strip().casefold()


def _b64_text(s: str):
    """The text of a base64 or base64url string (a Gmail body), or None when it is not readable text."""
    if not RX_B64.match(s):
        return None
    try:
        text = base64.urlsafe_b64decode(s + "=" * (-len(s) % 4)).decode("utf-8")
    except (ValueError, UnicodeDecodeError):
        return None
    if not text:
        return None
    printable = sum(1 for ch in text if ch.isprintable() or ch in "\r\n\t")
    return text if printable / len(text) > 0.95 else None


def scalars(value, out: list) -> list:
    """Every string (plus its base64 text) and number of a tool result. Numbers matter: a Slack ts is a float."""
    if isinstance(value, str):
        out.append(value)
        decoded = _b64_text(value)
        if decoded:
            out.append(decoded)
        elif len(value) > 200:
            for m in RX_B64_RUN.finditer(value):
                inner = _b64_text(m.group(0))
                if inner:
                    out.append(inner)
    elif isinstance(value, bool) or value is None:
        pass
    elif isinstance(value, (int, float)):
        out.append(repr(value))
    elif isinstance(value, dict):
        for x in value.values():
            scalars(x, out)
    elif isinstance(value, list):
        for x in value:
            scalars(x, out)
    return out


def ts_forms(ts: str) -> list:
    """A Slack ts as the export prints it: the string, and the float form that drops trailing zeros."""
    out = [ts]
    if re.match(r"^\d+\.\d+$", ts):
        short = ts.rstrip("0")
        short = short + "0" if short.endswith(".") else short
        if short not in out:
            out.append(short)
    return out


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _rel(path: Path) -> str:
    try:
        return str(Path(path).resolve().relative_to(WS.resolve()))
    except ValueError:
        return str(path)


def _rate(k: int, n: int):
    return round(k / n, 3) if n else None


def _check(cid: str, status: str, detail: str) -> dict:
    return {"id": cid, "status": status, "detail": detail}


def load_policy(path: Path | None = None) -> dict:
    return json.loads(Path(path or POLICY_PATH).read_text(encoding="utf-8"))


def carrier_lists(policy: dict) -> dict:
    budget = policy.get("budget") or {}
    out = {}
    for name in budget.get("carriers_that_miss") or []:
        out[name] = "carriers_that_miss"
    for name in budget.get("carriers_without_loss") or []:
        out[name] = "carriers_without_loss"
    return out


# ------------------------------------------------------------------ the injected SQL as records

class SqlIndex:
    """The rows of one injection SQL, keyed by every id a unit may name, with their normalised text."""

    def __init__(self, sql_text: str):
        tl = _tl()
        self.rows = []
        for n, x in enumerate(_parse_sql(sql_text)):
            if x["op"] == "insert":
                row, where = x["row"], {}
            elif x["op"] == "update":
                row, where = dict(x.get("set") or {}), x.get("where") or {}
            else:
                continue
            keys = {str(row[k]) for k in ID_COLS if isinstance(row.get(k), str) and row[k]}
            keys.update(str(v) for v in where.values() if v)
            table = x["table"]
            if table == "slack.slack_messages" and row.get("channel_id") and row.get("ts"):
                keys.add(f"{row['channel_id']}/{row['ts']}")
            if table == "gsheets.sheets_sheets" and (row.get("spreadsheet_id") or where.get("spreadsheet_id")):
                sid = row.get("spreadsheet_id") or where.get("spreadsheet_id")
                keys.add(str(sid))
                for k in ("title", "sheet_id"):
                    if row.get(k) not in (None, ""):
                        keys.add(f"{sid}#{row[k]}")
            if table in ("gslides.slides_page_elements", "gslides.slides_pages") and row.get("presentation_id"):
                keys.add(str(row["presentation_id"]))
            texts = []
            for col in TEXT_COLS:
                v = row.get(col)
                if not isinstance(v, str) or not v:
                    continue
                if col.endswith("_json"):
                    try:
                        v = " ".join(tl.strings(json.loads(v)))
                    except ValueError:
                        pass
                texts.append(norm_text(v))
            self.rows.append({"n": n, "op": x["op"], "table": table, "row": row, "where": where, "keys": keys,
                              "text": max(texts, key=len) if texts else "", "all": " ".join(texts)})

    def find(self, record_id: str) -> list:
        return [r for r in self.rows if record_id in r["keys"]]

    def thread_messages(self, thread_id: str) -> list:
        return [r for r in self.rows if r["table"] == "gmail.gmail_messages" and r["op"] == "insert"
                and r["row"].get("thread_id") == thread_id]

    def other_text(self, rows: list) -> str:
        """The text of every other row. A row with the same text as the record is a copy of it (the same mail in
        another mailbox), not another record, and is left out."""
        mine = {r["n"] for r in rows}
        same = {r["text"] for r in rows if r["text"]}
        return " \n ".join(r["all"] for r in self.rows if r["n"] not in mine and r["all"] and r["text"] not in same)


def text_windows(text: str, avoid: str) -> tuple:
    """(deep windows, head window) of one normalised record text; deep windows occur nowhere in `avoid`."""
    n = len(text)
    if n < MIN_NEEDLE:
        return [], None
    if n <= WINDOW + 20:
        return ([text] if text not in avoid else []), None
    head = text[:WINDOW]
    if n < HEAD_CHARS + WINDOW:
        starts = [n - WINDOW]
    else:
        span = n - WINDOW - HEAD_CHARS
        k = max(1, min(MAX_WINDOWS, span // WINDOW + 1))
        starts = [HEAD_CHARS + (span * i) // max(1, k - 1) for i in range(k)] if k > 1 else [n - WINDOW]
    deep = []
    for s in starts:
        w = text[s:s + WINDOW]
        if len(w) == WINDOW and w not in avoid and w not in deep:
            deep.append(w)
    if not deep:   # every evenly spaced window is shared with another row: step through the rest of the text
        for s in range(min(HEAD_CHARS, n - WINDOW), n - WINDOW + 1, 10):
            w = text[s:s + WINDOW]
            if w not in avoid:
                deep.append(w)
                break
    return deep, head


def record_facts(index: SqlIndex, rows: list) -> dict:
    """What the SQL says the record is: the facts the carrier label is checked against."""
    main = max(rows, key=lambda r: len(r["text"]))
    row, table = main["row"], main["table"]
    facts = {"table": table, "op": main["op"], "rows": len(rows), "text_chars": len(main["text"])}
    if table == "slack.slack_messages":
        channel = str(row.get("channel_id") or "")
        parent = row.get("thread_parent_id")
        facts.update({"is_reply": bool(parent), "is_dm": channel.startswith("D"), "channel": channel or None,
                      "thread_root_ts": row.get("thread_ts_legacy") if parent else None,
                      "parent_injected": bool(parent and index.find(str(parent)))})
    elif table == "gmail.gmail_messages":
        thread = row.get("thread_id")
        siblings = index.thread_messages(thread) if thread else []
        first = min(siblings, key=lambda r: str(r["row"].get("internal_date") or "")) if siblings else None
        reply = bool(row.get("in_reply_to")) or bool(first and first["n"] != main["n"])
        facts.update({"is_reply": reply, "is_mail_reply": reply, "thread": thread,
                      "thread_messages_injected": len(siblings),
                      "mailbox": str(row.get("user_email") or str(row.get("id") or "").split("/")[0]) or None})
    elif table == "linear.linear_comments":
        facts.update({"is_ticket": True, "is_reply": bool(row.get("parent_id")), "issue": row.get("issue_id")})
    elif table in ("linear.linear_issues", "trello.trello_cards", "trello.trello_actions"):
        facts.update({"is_ticket": True})
    elif table.startswith("github."):
        facts.update({"is_ticket": True, "is_reply": bool(row.get("in_reply_to_id"))})
    elif table == "gsheets.sheets_sheets":
        try:
            later = int(str(row.get("index") or "0")) > 0
        except ValueError:
            later = False
        facts.update({"is_later_tab": later, "tab": row.get("title")})
    elif table in ("trello.trello_check_items", "trello.trello_checklists"):
        facts.update({"is_checklist": True})
    elif table == "confluence.confluence_comments":
        facts.update({"is_reply": bool(row.get("parent_id")), "page": row.get("page_id")})
    return facts


def build_needles(decider: dict, index: SqlIndex | None) -> tuple:
    """(needles, facts, problems) for one deciding record.

    needles: {"deep": text needles, "head": first-40-character needles, "ids": record ids, "containers": container
    ids, "raw_ids": ids as written, "basis": "sql text" | "unit needles" | "sql text + unit needles" | "object"}.
    An injected record must resolve to a row of the revision's SQL; a problem here is a FAIL for the unit."""
    problems, facts = [], {}
    rid = str(decider.get("record_id") or "")
    service = str(decider.get("service") or "").lower()
    deep, head, raw_ids, containers = [], [], [rid] if rid else [], []
    curated = [norm_text(n) for n in decider.get("needles") or [] if str(n).strip()]
    for n in curated:
        if len(n) < MIN_NEEDLE:
            problems.append(f"needle {n!r} is shorter than {MIN_NEEDLE} characters")
    basis = "object"
    if decider.get("injected"):
        if index is None:
            problems.append("the run set's SQL could not be read, so the injected record cannot be resolved")
            rows = []
        else:
            rows = index.find(rid)
        if index is not None and not rows:
            problems.append(f"record_id {rid!r} is not a row of the revision's SQL")
        elif rows:
            if all(r["table"] == "gmail.gmail_threads" for r in rows):
                ids = [m["row"].get("id") for m in index.thread_messages(rid)]
                problems.append(f"record_id {rid!r} is a Gmail thread; name the message, one of {ids}")
            facts = record_facts(index, rows)
            avoid = index.other_text(rows)
            for r in rows:
                d, h = text_windows(r["text"], avoid)
                deep += [w for w in d if w not in deep]
                if h and h not in head:
                    head.append(h)
                raw_ids += [k for k in sorted(r["keys"]) if len(k) >= 8 and k not in raw_ids]
            own = " ".join(r["all"] for r in rows)
            for n in curated:
                if n not in own:
                    problems.append(f"needle {n!r} is not in the record's text in the SQL")
                elif n in avoid:
                    problems.append(f"needle {n!r} also occurs in another row of the SQL (pick a unique phrase)")
            main = max(rows, key=lambda r: len(r["text"]))
            if facts.get("thread_root_ts"):
                containers.append(str(facts["thread_root_ts"]))
            for key in ("thread", "issue", "page"):
                if facts.get(key):
                    containers.append(str(facts[key]))
            if main["table"] == "slack.slack_messages" and not facts.get("is_reply") and facts.get("channel"):
                containers.append(str(facts["channel"]))
            basis = "sql text + unit needles" if curated and deep else "unit needles" if curated else \
                "sql text" if deep else "object"
    elif curated:
        basis = "unit needles"
    elif service == "gmail" and re.match(r"^[^/]+/\d+$", rid) and "reply" in str(decider.get("_carrier") or ""):
        problems.append(f"record_id {rid!r} is a Gmail thread id, which any message of the thread satisfies; "
                        "name the reply's message id or give a needle from the reply")
    deep += [n for n in curated if n not in deep and len(n) >= MIN_NEEDLE]
    container = str(decider.get("container") or "")
    if container:
        m = RX_SLACK_ID.match(container)
        containers.append(m.group(2) if m else container)
    ids = []
    for i in raw_ids:
        m = RX_SLACK_ID.match(i)
        forms = ts_forms(m.group(2)) if m else ts_forms(i) if re.match(r"^\d{9,}\.\d+$", i) else [i]
        ids += [norm_text(f) for f in forms if norm_text(f) not in ids and len(f) >= 8]
    if service == "slack":
        for r in (index.find(rid) if index is not None and decider.get("injected") else []):
            ts = r["row"].get("ts")
            ids += [norm_text(f) for f in ts_forms(str(ts)) if ts and norm_text(f) not in ids]
    conts = []
    for c in containers:
        for f in ts_forms(c):
            if norm_text(f) not in conts and norm_text(f) not in ids:
                conts.append(norm_text(f))
    return ({"deep": deep, "head": head, "ids": ids, "containers": conts, "raw_ids": raw_ids, "basis": basis,
             "service": service}, facts, problems)


# ------------------------------------------------------------------ one trajectory

class RunView:
    """The tool calls of one export in order, each with the normalised text its result showed."""

    def __init__(self, path: Path):
        tl = _tl()
        self.path = Path(path)
        self.run = tl.load(self.path)
        ordered = sorted(self.run.calls, key=lambda c: c["event"] if c["event"] is not None else 10 ** 9)
        self.calls = []
        for step, c in enumerate(ordered, 1):
            r = self.run.results.get(c["id"])
            raw = " ".join(scalars(r["data"], [])) if r else ""
            tool = tl.short(c["name"])
            self.calls.append({
                "step": step, "event": c["event"], "tool": tool, "context": c["context"], "id": c["id"],
                "args": norm_text(" ".join(scalars(c["input"], []))), "text": norm_text(raw),
                "spilled": bool(tl.RX_SPILL.search(raw)), "has_result": r is not None,
                "write": tl.is_write(c["name"]) or tool in HARNESS_WRITES})

    def data(self, call: dict):
        r = self.run.results.get(call["id"])
        return r["data"] if r else None


def _same_id(value, raw_ids: list) -> bool:
    if isinstance(value, bool) or value is None:
        return False
    s = repr(value) if isinstance(value, float) else str(value)
    for rid in raw_ids:
        m = RX_SLACK_ID.match(rid)
        forms = ts_forms(m.group(2)) if m else ts_forms(rid)
        if s in forms or s.casefold() == rid.casefold():
            return True
    return False


def _has_content(obj: dict) -> bool:
    for k in CONTENT_KEYS:
        if isinstance(obj.get(k), str) and obj[k].strip():
            return True
    payload = obj.get("payload")
    if isinstance(payload, dict):   # a Gmail message fetched with its body (format full), not minimal or metadata
        stack = [payload]
        while stack:
            p = stack.pop()
            body = p.get("body") if isinstance(p, dict) else None
            if isinstance(body, dict) and body.get("data"):
                return True
            stack += [x for x in (p.get("parts") or []) if isinstance(x, dict)] if isinstance(p, dict) else []
    messages = obj.get("messages")   # a Gmail thread fetched with its messages' bodies
    return isinstance(messages, list) and any(isinstance(m, dict) and _has_content(m) for m in messages)


def object_shown(data, raw_ids: list) -> bool:
    """True when a result holds an object that carries one of the ids and a content field (the record itself)."""
    stack = [data]
    while stack:
        v = stack.pop()
        if isinstance(v, dict):
            if any(_same_id(v.get(k), raw_ids) for k in OBJECT_ID_KEYS) and _has_content(v):
                return True
            stack += list(v.values())
        elif isinstance(v, list):
            stack += v
    return False


def detect(view: RunView, nd: dict) -> dict:
    """Was the record opened in this run, at which call, and what weaker signs were seen before."""
    out = {"opened": False, "how": None, "step": None, "event": None, "tool": None, "context": None,
           "snippet_only": False, "snippet_step": None, "snippet_tool": None,
           "container_step": None, "container_spilled": False}
    for c in view.calls:
        if c["write"]:
            continue
        text, how = c["text"], None
        if out["container_step"] is None and any(k in c["args"] for k in nd["containers"]):
            out.update({"container_step": c["step"], "container_spilled": c["spilled"]})
        if text and any(n in text for n in nd["deep"]):
            how = "text"
        elif c["spilled"] and nd["ids"] and any(i in c["args"] for i in nd["ids"]):
            how = "direct_get_spilled"
        elif not nd["deep"] and c["has_result"] and any(i in text for i in nd["ids"]) \
                and object_shown(view.data(c), nd["raw_ids"]):
            how = "object"
        if how:
            out.update({"opened": True, "how": how, "step": c["step"], "event": c["event"], "tool": c["tool"],
                        "context": c["context"]})
            break
        if out["snippet_step"] is None and ((text and (any(n in text for n in nd["head"])
                                                       or any(i in text for i in nd["ids"])))
                                            or any(i in c["args"] for i in nd["ids"])):
            out.update({"snippet_step": c["step"], "snippet_tool": c["tool"]})
    out["snippet_only"] = bool(out["snippet_step"]) and not out["opened"]
    return out


# ------------------------------------------------------------------ run sets: files, binding, rubric results

def _task_inputs(tasks_root: Path, task: str) -> Path:
    return Path(tasks_root) / task / "task_inputs"


def _sql_label(task_inputs: Path, sql_path: Path) -> str:
    try:
        rel = sql_path.resolve().relative_to((task_inputs / "Working_Files" / "run_forensics").resolve())
        return rel.parts[0]
    except ValueError:
        return "root"


def revision_candidates(task_inputs: Path) -> list:
    """[(label, sql text)]: every revision the archive stores, plus the task's own SQL as `root`."""
    tl = _tl()
    out = [(rev, p.read_text(encoding="utf-8", errors="replace")) for rev, p in tl.stored_revisions(task_inputs)]
    root = task_inputs / "01_Universe_Inject.sql"
    if root.is_file():
        out.append(("root", root.read_text(encoding="utf-8", errors="replace")))
    return out


def bind_run(view: RunView, candidates: list, label: str, accept: str | None) -> dict:
    """Is this export a run of the declared revision? Content decides; `accept` is the reason to count a run that
    content cannot tell apart from another stored revision (never one that content binds elsewhere)."""
    tl = _tl()
    b = tl.binding(view.run, candidates) if candidates else {"verdict": "UNBOUND", "bound_to": None}
    verdict, bound = b["verdict"], b.get("bound_to") or []
    if verdict == "BOUND" and label in bound:
        return {"verdict": "BOUND", "counted": True, "note": f"bound to {label} by content"}
    if verdict == "BOUND":
        return {"verdict": "BOUND_ELSEWHERE", "counted": False,
                "note": f"content binds this run to {'/'.join(bound)}, not {label}"}
    if accept:
        return {"verdict": verdict, "counted": True, "note": f"declared ({verdict.lower()} by content): {accept}"}
    return {"verdict": verdict, "counted": False,
            "note": f"{verdict.lower()} by content and the run set gives no binding_accept reason"}


def rubric_results(task_inputs: Path) -> tuple:
    """({trajectory file name: {rubric id: passed}}, rubric ids, how runs were matched to files) for the baseline."""
    di = task_inputs / "Working_Files" / "12_difficulty_input.json"
    if di.is_file():
        data = json.loads(di.read_text(encoding="utf-8"))
        ids = [r.get("id") for r in data.get("rubrics") or []]
        out = {}
        for ro in data.get("rollouts") or []:
            if ro.get("file") and isinstance(ro.get("results"), dict) and ro.get("status", "completed") == "completed":
                out[ro["file"]] = {k: bool(v) for k, v in ro["results"].items()}
        if out:
            return out, ids, "file named per run in 12_difficulty_input.json"
    verifier, rubrics = task_inputs / "10_Baseline_Verifier_Results.md", task_inputs / "09_Rubrics.json"
    if verifier.is_file() and rubrics.is_file() and verifier.stat().st_size:
        import difficulty_stats as ds
        try:
            rows, _ = ds.parse_rubrics(rubrics)
            runs = ds.parse_verifier(verifier)
        except SystemExit:
            return {}, [], "verifier results or rubric file could not be parsed"
        by_title = {ds.norm_title(r["title"]): r["id"] for r in rows}
        out = {}
        files = {ds._run_number(p): p.name for p in sorted((task_inputs / "07_Baseline_Trajectories").glob("*.json"))}
        for n, graded in runs.items():
            if n not in files:
                continue
            res = {}
            for g in graded:
                rid = by_title.get(ds.norm_title(g["title"]))
                if rid:
                    res[rid] = bool(g["passed"])
            out[files[n]] = res
        return out, [r["id"] for r in rows], ("10_Baseline_Verifier_Results.md, Run #N taken as trajectory file "
                                              "number N (not bound by content)")
    return {}, [], "no rubric results stored"


# ------------------------------------------------------------------ units file

def load_units(path: Path | None = None) -> dict:
    return json.loads(Path(path or UNITS_PATH).read_text(encoding="utf-8"))


def unit_key(u: dict) -> str:
    return f"{u.get('task')}|{u.get('revision')}|{u.get('run_set')}|{u.get('unit')}|" \
           f"{(u.get('decider') or {}).get('record_id')}"


def validate_units(doc: dict, policy: dict) -> list:
    """Schema checks on the curated file. Returns checks; any FAIL means nothing is computed."""
    checks, bad = [], []
    if doc.get("schema") != SCHEMA_UNITS:
        return [_check("units.schema", "FAIL", f"schema is {doc.get('schema')!r}, expected {SCHEMA_UNITS}; "
                       "fix the file header")]
    known = carrier_lists(policy)
    sets = {(s.get("task"), s.get("revision"), s.get("run_set")) for s in doc.get("run_sets") or []}
    seen = set()
    for i, u in enumerate(doc.get("units") or []):
        where = f"units[{i}] {u.get('task')}/{u.get('revision')}/{u.get('unit')}"
        missing = [f for f in UNIT_FIELDS if f not in u]
        if missing:
            bad.append(f"{where}: missing {missing}")
            continue
        d, h = u["decider"] or {}, u["habit"] or {}
        if u["run_set"] not in RUN_SETS:
            bad.append(f"{where}: run_set {u['run_set']!r} is not precheck or baseline")
        if (u["task"], u["revision"], u["run_set"]) not in sets:
            bad.append(f"{where}: no run_sets entry for this task, revision and run_set")
        if any(k not in d for k in ("service", "record_id", "container", "injected")) or not d.get("record_id"):
            bad.append(f"{where}: decider needs service, record_id, container and injected")
        if not h.get("service") or not h.get("action"):
            bad.append(f"{where}: habit needs service and action")
        carrier = str(u["carrier"])
        if carrier not in known and not (carrier.startswith("other:") and carrier[6:].strip()):
            bad.append(f"{where}: carrier {carrier!r} is not in first_pass_policy.json; use a listed name or other:<text>")
        if u["confidence"] not in CONFIDENCE:
            bad.append(f"{where}: confidence {u['confidence']!r} is not high, medium or low")
        if not isinstance(u["rows"], list):
            bad.append(f"{where}: rows must be a list of rubric ids (may be empty)")
        if not u["evidence"]:
            bad.append(f"{where}: evidence is empty; cite the file and line or JSON pointer")
        if unit_key(u) in seen:
            bad.append(f"{where}: the same unit and record is listed twice")
        seen.add(unit_key(u))
    for i, s in enumerate(doc.get("run_sets") or []):
        if not s.get("sql") or not s.get("trajectories"):
            bad.append(f"run_sets[{i}] {s.get('task')}/{s.get('revision')}/{s.get('run_set')}: needs sql and trajectories")
    for i, s in enumerate(doc.get("skipped") or []):
        if not s.get("task") or not s.get("reason"):
            bad.append(f"skipped[{i}]: needs task and reason")
    if bad:
        checks.append(_check("units.schema", "FAIL", f"{len(bad)} problem(s): " + "; ".join(bad[:8])
                             + (" ..." if len(bad) > 8 else "")))
    else:
        checks.append(_check("units.schema", "PASS", f"{len(doc.get('units') or [])} unit(s), "
                             f"{len(doc.get('run_sets') or [])} run set(s), {len(doc.get('skipped') or [])} skipped"))
    return checks


# ------------------------------------------------------------------ compute

def _aggregate(records: list, key_of, lists: dict | None = None) -> dict:
    """Counts per key over counted runs of high- and medium-confidence units. Rates never appear without counts."""
    groups = {}
    for rec in records:
        counted = [r for r in rec["runs"] if r["counted"]]
        if rec["confidence"] not in AGGREGATE_CONFIDENCE or not counted:
            continue
        g = groups.setdefault(key_of(rec), {"tasks": set(), "units": set(), "runs": 0, "opened": 0, "snippet_only": 0,
                                            "rows_graded_runs": 0, "rows_right": 0, "by_run_set": {},
                                            "cross": {"opened_rows_right": 0, "opened_rows_wrong": 0,
                                                      "missed_rows_right": 0, "missed_rows_wrong": 0},
                                            "unit_rates": []})
        g["tasks"].add(rec["task"])
        g["units"].add((rec["task"], rec["unit"], rec["decider"]["record_id"]))
        g["unit_rates"].append({"task": rec["task"], "revision": rec["revision"], "run_set": rec["run_set"],
                                "unit": rec["unit"], "opened": sum(r["opened"] for r in counted),
                                "runs": len(counted)})
        rs = g["by_run_set"].setdefault(rec["run_set"], {"runs": 0, "opened": 0})
        for r in counted:
            g["runs"] += 1
            rs["runs"] += 1
            g["opened"] += int(r["opened"])
            rs["opened"] += int(r["opened"])
            g["snippet_only"] += int(r["snippet_only"])
            if r["rows_right"] is not None:
                g["rows_graded_runs"] += 1
                g["rows_right"] += int(r["rows_right"])
                g["cross"][("opened" if r["unit_opened"] else "missed")
                           + ("_rows_right" if r["rows_right"] else "_rows_wrong")] += 1
    out = {}
    for name in sorted(groups):
        g = groups[name]
        rates = sorted(u["opened"] / u["runs"] for u in g["unit_rates"])
        entry = {"tasks": len(g["tasks"]), "units": len(g["units"]), "runs": g["runs"], "opened": g["opened"],
                 "opened_rate": _rate(g["opened"], g["runs"]), "snippet_only": g["snippet_only"],
                 "rows_graded_runs": g["rows_graded_runs"], "rows_right": g["rows_right"],
                 "rows_right_rate": _rate(g["rows_right"], g["rows_graded_runs"]), "cross": g["cross"],
                 "by_run_set": {k: g["by_run_set"][k] for k in sorted(g["by_run_set"])},
                 "unit_rate_min": round(rates[0], 3) if rates else None,
                 "unit_rate_median": round(statistics.median(rates), 3) if rates else None,
                 "unit_rate_max": round(rates[-1], 3) if rates else None,
                 "unit_rates": sorted(g["unit_rates"], key=lambda u: (u["task"], u["revision"], u["run_set"], u["unit"]))}
        if lists is not None:
            entry["plan_list"] = lists.get(name, "other")
        out[name] = entry
    return out


def evaluate(units_path=None, tasks_root=None, only_tasks=None, policy_path=None) -> dict:
    """Read the curated units and the archived runs and return the result object (no file is written).

    The object has the contract keys (tool, version, verdict, bound_to, checks) plus `rates`, the content of
    carrier_find_rates.json."""
    units_path = Path(units_path or UNITS_PATH)
    tasks_root = Path(tasks_root or TASKS_ROOT)
    policy_file = Path(policy_path or POLICY_PATH)
    policy = load_policy(policy_file)
    lists = carrier_lists(policy)
    doc = load_units(units_path)
    bound = {_rel(units_path): sha256_file(units_path), _rel(policy_file): sha256_file(policy_file)}
    checks = validate_units(doc, policy)
    result = {"tool": TOOL, "version": VERSION, "verdict": "FAIL", "bound_to": bound, "checks": checks, "rates": None}
    if any(c["status"] == "FAIL" for c in checks):
        return result

    units = [u for u in doc["units"] if not only_tasks or u["task"] in only_tasks]
    run_sets = {(s["task"], s["revision"], s["run_set"]): s for s in doc["run_sets"]}
    by_task = {}
    for u in units:
        by_task.setdefault(u["task"], []).append(u)

    records, file_problems, decider_problems, structure_warn, weak_needles = [], [], [], [], []
    binding_out, row_warn, no_results, never_seen = [], [], [], []
    runs_seen = set()
    for task in sorted(by_task):
        ti = _task_inputs(tasks_root, task)
        candidates = revision_candidates(ti) if ti.is_dir() else []
        views, bindings, indexes = {}, {}, {}
        results, rubric_ids, mapping = rubric_results(ti) if ti.is_dir() else ({}, [], "task folder missing")
        for u in sorted(by_task[task], key=unit_key):
            decl = run_sets[(u["task"], u["revision"], u["run_set"])]
            sql_path = ti / decl["sql"]
            if decl["sql"] not in indexes:
                indexes[decl["sql"]] = SqlIndex(sql_path.read_text(encoding="utf-8", errors="replace")) \
                    if sql_path.is_file() else None
                if indexes[decl["sql"]] is None:
                    file_problems.append(f"{task}: SQL {decl['sql']} is missing")
                else:
                    bound[_rel(sql_path)] = sha256_file(sql_path)
            nd, facts, problems = build_needles(dict(u["decider"], _carrier=u["carrier"]), indexes[decl["sql"]])
            if problems:
                decider_problems += [f"{task}/{u['revision']}/{u['unit']}: {p}" for p in problems]
            rule = STRUCTURE_RULES.get(u["carrier"])
            if rule and facts and not facts.get(rule[0]):
                structure_warn.append(f"{task}/{u['revision']}/{u['unit']}: carrier {u['carrier']} but {rule[1]}")
            if not nd["deep"]:
                weak_needles.append(f"{task}/{u['revision']}/{u['unit']}")
            label = _sql_label(ti, sql_path)
            runs = []
            for rel in decl["trajectories"]:
                path = ti / rel
                if not path.is_file():
                    file_problems.append(f"{task}: trajectory {rel} is missing")
                    continue
                if rel not in views:
                    views[rel] = RunView(path)
                    bindings[rel] = (sha256_file(path), {})
                sha, cache = bindings[rel]
                bkey = (label, decl.get("binding_accept"))
                if bkey not in cache:
                    cache[bkey] = bind_run(views[rel], candidates, label, decl.get("binding_accept"))
                b = cache[bkey]
                d = detect(views[rel], nd)
                graded = results.get(path.name) if u["run_set"] == "baseline" else None
                row_ids = [r for r in u["rows"] if graded is not None and r in graded]
                passed = sum(1 for r in row_ids if graded[r])
                tl = _tl()
                n = tl.ds._run_number(path) if u["run_set"] == "baseline" else None
                runs.append({"run": f"run-{n}" if n is not None else Path(rel).stem, "file": rel, "sha256": sha,
                             "binding": b["verdict"], "binding_note": b["note"], "counted": b["counted"],
                             "opened": d["opened"], "how": d["how"], "step": d["step"], "event": d["event"],
                             "tool": d["tool"], "context": d["context"], "snippet_only": d["snippet_only"],
                             "snippet_step": d["snippet_step"], "snippet_tool": d["snippet_tool"],
                             "container_step": d["container_step"], "container_spilled": d["container_spilled"],
                             "rows_passed": passed if row_ids else None, "rows_total": len(row_ids) if row_ids else None,
                             "rows_right": (passed == len(row_ids)) if row_ids else None, "unit_opened": d["opened"]})
                runs_seen.add((task, rel))
                if not b["counted"]:
                    binding_out.append(f"{task}/{rel} ({b['note']})")
            if u["rows"] and u["run_set"] == "baseline":
                unknown = [r for r in u["rows"] if rubric_ids and r not in rubric_ids]
                if unknown:
                    row_warn.append(f"{task}/{u['revision']}/{u['unit']}: rows {unknown} are not rubric ids of this task")
                if not results:
                    no_results.append(f"{task} ({mapping})")
            if not u["decider"].get("injected") and nd["deep"] and runs and not any(r["opened"] for r in runs):
                never_seen.append(f"{task}/{u['revision']}/{u['unit']}")
            counted = [r for r in runs if r["counted"]]
            graded_runs = [r for r in counted if r["rows_right"] is not None]
            records.append({
                "task": task, "revision": u["revision"], "run_set": u["run_set"], "unit": u["unit"],
                "mechanism_family": u["mechanism_family"], "carrier": u["carrier"],
                "habit": {"service": str(u["habit"]["service"]).lower(), "action": str(u["habit"]["action"])},
                "decider": {k: u["decider"].get(k) for k in ("service", "record_id", "container", "injected")},
                "rows": list(u["rows"]), "confidence": u["confidence"],
                "in_aggregate": u["confidence"] in AGGREGATE_CONFIDENCE and bool(counted),
                "decider_facts": facts, "needles": {"basis": nd["basis"], "text": len(nd["deep"]), "ids": len(nd["ids"])},
                "results_mapping": mapping if u["run_set"] == "baseline" and u["rows"] else None,
                "runs": runs,
                "totals": {"runs": len(counted), "opened": sum(r["opened"] for r in counted),
                           "snippet_only": sum(r["snippet_only"] for r in counted),
                           "rows_graded_runs": len(graded_runs), "rows_right": sum(r["rows_right"] for r in graded_runs)}})
        # a unit with two carriers (the same unit id on two records): the rows are right when either was opened
        groups = {}
        for rec in records:
            if rec["task"] == task:
                groups.setdefault((rec["revision"], rec["run_set"], rec["unit"]), []).append(rec)
        for recs in groups.values():
            if len(recs) > 1:
                for rel in {r["file"] for rec in recs for r in rec["runs"]}:
                    any_open = any(r["opened"] for rec in recs for r in rec["runs"] if r["file"] == rel)
                    for rec in recs:
                        for r in rec["runs"]:
                            if r["file"] == rel:
                                r["unit_opened"] = any_open

    carriers = _aggregate(records, lambda r: r["carrier"], lists)
    habits = _aggregate(records, lambda r: f"{r['habit']['service']}/{r['habit']['action']}")
    archives = sorted(p.name for p in tasks_root.iterdir() if (p / "task_inputs").is_dir()) if tasks_root.is_dir() else []
    covered = sorted({r["task"] for r in records if r["totals"]["runs"]})
    coverage = {"archives_total": len(archives), "archives_covered": len(covered), "archives": covered,
                "archives_not_covered": [a for a in archives if a not in covered],
                "units": len(records), "units_in_aggregate": sum(1 for r in records if r["in_aggregate"]),
                "units_low_confidence": sum(1 for r in records if r["confidence"] not in AGGREGATE_CONFIDENCE),
                "skipped": len(doc.get("skipped") or []), "trajectories_read": len(runs_seen),
                "unit_runs_counted": sum(r["totals"]["runs"] for r in records)}

    def add(cid, items, bad_status, good, bad):
        if items:
            uniq = sorted(set(items))
            checks.append(_check(cid, bad_status, f"{len(uniq)}: {bad} " + "; ".join(uniq[:6])
                                 + (" ..." if len(uniq) > 6 else "")))
        else:
            checks.append(_check(cid, "PASS", good))

    add("units.files", file_problems, "FAIL", "every declared SQL and trajectory file exists",
        "missing file(s); fix the run_sets entry.")
    add("units.deciders", decider_problems, "FAIL", "every injected deciding record resolves to a row of its SQL",
        "deciding record(s) do not resolve; fix record_id or needles.")
    add("units.structure", structure_warn, "WARN", "carrier labels agree with what the SQL rows are",
        "label(s) disagree with the SQL row; re-check the carrier.")
    add("units.needles", weak_needles, "WARN", "every unit has a text needle",
        "unit(s) have no text needle and are judged on a result object with the record id;")
    add("units.base_needles", never_seen, "WARN", "every base-record needle was seen in at least one run",
        "base-record needle(s) were never seen in any run, so the needle text itself is unverified by the runs:")
    add("runs.binding", binding_out, "WARN", "every run is bound to its declared revision",
        "run(s) left out of the counts:")
    add("rows.ids", row_warn, "WARN", "every row id is a rubric id of its task", "unit(s) name unknown rows;")
    add("rows.results", no_results, "WARN", "rubric results exist for every baseline unit with rows",
        "task(s) have rows but no stored rubric results, so rows-right is empty:")
    cross = []
    for rec in records:
        graded = [r for r in rec["runs"] if r["counted"] and r["rows_right"] is not None]
        blind = sum(1 for r in graded if not r["unit_opened"] and r["rows_right"])
        if blind >= 2:
            cross.append(f"{rec['task']}/{rec['revision']}/{rec['unit']}: rows right in {blind} of {len(graded)} runs "
                         "that never opened the record")
    add("units.cross", cross, "WARN", "no unit had its rows right in two or more runs that never opened its record",
        "unit(s) where the record does not decide the rows as labelled (another record settles them, or the read "
        "is not visible in the export); re-check the decider or move the unit to skipped:")
    small = [f"{n} ({c['opened']}/{c['runs']} runs, {c['units']} unit(s), {c['tasks']} task(s))"
             for n, c in carriers.items() if c["runs"] < SMALL_SAMPLE_RUNS]
    add("rates.small_samples", small, "WARN", f"every carrier has at least {SMALL_SAMPLE_RUNS} counted runs",
        f"carrier(s) under {SMALL_SAMPLE_RUNS} counted runs; read the counts, not the rate:")
    missing = [n for n in sorted(lists) if n not in carriers]
    add("rates.coverage", missing, "WARN", "every carrier named in the policy has data",
        "policy carrier(s) have no unit in the backfill:")
    disagree = []
    for n, c in carriers.items():
        if not c["runs"]:
            continue
        wrong = c["rows_graded_runs"] - c["rows_right"]
        rows = f" (rows wrong in {wrong} of {c['rows_graded_runs']} graded runs)" if c["rows_graded_runs"] else ""
        if c.get("plan_list") == "carriers_without_loss" and c["opened"] < c["runs"]:
            disagree.append(f"{n}: listed as producing no loss, but not opened in {c['runs'] - c['opened']} of "
                            f"{c['runs']} runs{rows}")
        if c.get("plan_list") == "carriers_that_miss" and 2 * c["opened"] > c["runs"]:
            disagree.append(f"{n}: listed as producing misses, but opened in {c['opened']} of {c['runs']} runs{rows}")
    add("rates.plan_lists", disagree, "WARN", "the measured rates agree with the plan's RC1 lists",
        "carrier(s) disagree with the plan's RC1 lists:")

    result["rates"] = {
        "schema": SCHEMA_RATES, "tool": TOOL, "version": VERSION,
        "source": {"units": _rel(units_path), "units_sha256": bound[_rel(units_path)],
                   "policy": _rel(policy_file), "tasks_root": _rel(tasks_root)},
        "method": {
            "opened": "a tool result shows the record's own text (a 40-character window after its first 100 "
                      "characters, the whole text when shorter, or the unit's needles; Gmail bodies decoded from "
                      "base64), or a read call names the record's id and its result spilled to a file, or, for a "
                      "record without a text needle, a result holds an object with its id and a content field",
            "snippet_only": "only the id or the first 40 characters were seen; not counted as opened",
            "not_counted_as_opened": "a container read whose result spilled to a file and never showed the text",
            "rows_right": "every rubric row of the unit passed in that run (baseline runs with stored results only)",
            "cross": "rows right or wrong against whether any record of the unit was opened in that run",
            "aggregates": f"counted runs of units with confidence in {list(AGGREGATE_CONFIDENCE)}; a run counts "
                          "when content binds it to the declared revision or the run set gives a binding_accept reason",
            "constants": {"HEAD_CHARS": HEAD_CHARS, "WINDOW": WINDOW, "MAX_WINDOWS": MAX_WINDOWS,
                          "MIN_NEEDLE": MIN_NEEDLE, "SMALL_SAMPLE_RUNS": SMALL_SAMPLE_RUNS}},
        "coverage": coverage, "carriers": carriers, "habits": habits,
        "units": sorted(records, key=lambda r: (r["task"], r["revision"], r["run_set"], r["unit"],
                                                str(r["decider"]["record_id"]))),
        "skipped": doc.get("skipped") or []}
    statuses = {c["status"] for c in checks}
    result["verdict"] = "FAIL" if "FAIL" in statuses else "WARN" if "WARN" in statuses else "PASS"
    result["bound_to"] = {k: bound[k] for k in sorted(bound)}
    return result


# ------------------------------------------------------------------ reading the table (for other tools)

def load_rates(path=None) -> dict:
    """The stored table, or raise FileNotFoundError: run `compute --write` first."""
    return json.loads(Path(path or RATES_PATH).read_text(encoding="utf-8"))


def carrier_rate(name: str, rates: dict | None = None):
    """The aggregate of one carrier ({runs, opened, opened_rate, ...}) or None when the table has no data for it."""
    return ((rates or load_rates()).get("carriers") or {}).get(name)


def habit_rate(service: str, action: str, rates: dict | None = None):
    return ((rates or load_rates()).get("habits") or {}).get(f"{str(service).lower()}/{action}")


# ------------------------------------------------------------------ output

def write_rates(rates: dict, out_path=None) -> Path:
    from task_context import refuse_read_only
    out = Path(out_path or RATES_PATH)
    refuse_read_only(out, "the carrier find-rate table")
    out.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=out.name + ".", dir=str(out.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(json.dumps(rates, indent=1, sort_keys=True, ensure_ascii=False) + "\n")
        os.replace(tmp, out)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)
    return out


def _frac(k, n) -> str:
    return f"{k}/{n}" + (f" ({k / n:.2f})" if n else "")


def table_lines(rates: dict, carrier: str | None = None, key: str = "carriers") -> list:
    """The aggregate table as text. Counts first; a rate is only ever printed beside its counts."""
    rows = rates.get(key) or {}
    names = [n for n in rows if carrier in (None, n)]
    head = f"{'habit' if key == 'habits' else 'carrier':<34} {'plan list':<10} {'tasks':>5} {'units':>5} " \
           f"{'opened/runs':>16} {'snippet':>7} {'rows right/graded':>18} {'baseline':>12} {'precheck':>10}"
    out = [head, "-" * len(head)]
    order = {"carriers_that_miss": 0, "carriers_without_loss": 1, "other": 2}
    for n in sorted(names, key=lambda n: (order.get(rows[n].get("plan_list", "other"), 2), n)):
        c = rows[n]
        plan = {"carriers_that_miss": "miss", "carriers_without_loss": "no loss"}.get(c.get("plan_list"), "-")
        b, p = c["by_run_set"].get("baseline", {}), c["by_run_set"].get("precheck", {})
        out.append(f"{n[:34]:<34} {plan:<10} {c['tasks']:>5} {c['units']:>5} {_frac(c['opened'], c['runs']):>16} "
                   f"{c['snippet_only']:>7} {_frac(c['rows_right'], c['rows_graded_runs']):>18} "
                   f"{(str(b.get('opened', 0)) + '/' + str(b.get('runs', 0))):>12} "
                   f"{(str(p.get('opened', 0)) + '/' + str(p.get('runs', 0))):>10}")
    if carrier is not None and names:
        c = rows[names[0]]
        x = c["cross"]
        out.append("")
        out.append(f"rows against opened (baseline runs with results): opened and right {x['opened_rows_right']}, "
                   f"opened and wrong {x['opened_rows_wrong']}, not opened and right {x['missed_rows_right']}, "
                   f"not opened and wrong {x['missed_rows_wrong']}")
        out.append("units:")
        for u in c["unit_rates"]:
            out.append(f"  {u['task']} {u['revision']} {u['run_set']} {u['unit']}: opened {u['opened']}/{u['runs']}")
    return out


def unit_lines(rates: dict) -> list:
    """One line per unit record: Y opened (with the step), s snippet only, n not seen, x run not counted."""
    out = []
    for u in rates.get("units") or []:
        marks = []
        for r in u["runs"]:
            mark = "x" if not r["counted"] else f"Y@{r['step']}" if r["opened"] else "s" if r["snippet_only"] else "n"
            if r["rows_right"] is not None:
                mark += "+" if r["rows_right"] else "-"
            marks.append(mark)
        t = u["totals"]
        rows = f" rows right {t['rows_right']}/{t['rows_graded_runs']}" if t["rows_graded_runs"] else ""
        out.append(f"  {u['task']} {u['revision']} {u['run_set']} {u['unit']} [{u['carrier']}; {u['confidence']}; "
                   f"{u['needles']['basis']}]: opened {t['opened']}/{t['runs']} ({' '.join(marks)}){rows}")
    return out


def render(result: dict, qualifier: str, detail: bool = False) -> str:
    lines = [f"CARRIER BACKFILL ({qualifier}): {result['verdict']}"]
    lines += [f"[{c['status']}] {c['id']}: {c['detail']}" for c in result["checks"]]
    rates = result.get("rates")
    if rates and detail:
        lines += ["", "units (Y@step opened, s snippet only, n not seen, x not counted; + rows right, - rows wrong):"]
        lines += unit_lines(rates)
    if rates:
        cov = rates["coverage"]
        lines += ["", f"coverage: {cov['archives_covered']} of {cov['archives_total']} archives, {cov['units']} unit "
                      f"record(s) ({cov['units_in_aggregate']} in the aggregates, {cov['units_low_confidence']} low "
                      f"confidence), {cov['skipped']} skipped, {cov['trajectories_read']} trajectories, "
                      f"{cov['unit_runs_counted']} unit-run observation(s)", ""]
        lines += table_lines(rates)
        lines += ["", "per habit (service/action):"] + table_lines(rates, key="habits")
    return "\n".join(lines)


# ------------------------------------------------------------------ self-test

def _fixture_events(calls: list) -> list:
    """A minimal stream-json export: one assistant tool_use and one user tool_result per call."""
    events = [{"type": "system", "subtype": "init", "model": "claude-opus-5-5", "claude_code_version": "0"}]
    for i, (name, args, result, parent) in enumerate(calls):
        cid = f"toolu_{i:03d}"
        events.append({"type": "assistant", "parent_tool_use_id": parent,
                       "message": {"model": "claude-opus-5-5",
                                   "content": [{"type": "tool_use", "id": cid, "name": name, "input": args}]}})
        events.append({"type": "user", "parent_tool_use_id": parent,
                       "message": {"content": [{"type": "tool_result", "tool_use_id": cid,
                                                "content": result if isinstance(result, str) else json.dumps(result)}]}})
    events.append({"type": "result", "subtype": "success", "is_error": False, "result": "done"})
    return events


def _fixture(tmp: Path) -> dict:
    """A synthetic archive (one task, two SQL revisions, four baseline runs, one pre-check) and its units file."""
    reply = ("thanks for the list. one change before you send anything: the waiver for the Pro plan vendor was "
             "pulled on Friday, Maren confirmed it by phone, so treat that one as still owed and leave the other "
             "nine exactly as they are in the tracker for now")
    mail = ("Hi both, following up on the transfer question from last week. The second wire did not settle: the "
            "bank returned it on the 4th because the account number was wrong, so only the first wire counts toward "
            "the total. I will resend once the details are fixed. Regards")
    root_text = "lunch order for thursday, add yourself to the sheet before noon please, thanks all"
    cols = ("id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count")

    def slack(i, ts, ch, text, parent, root_ts, n):
        par = f"'{parent}'" if parent else "NULL"
        rts = f"'{root_ts}'" if root_ts else "NULL"
        return (f"INSERT INTO slack.slack_messages ({cols})\nVALUES ('{i}', '{ts}', '{ch}', 'message', 'U1', "
                f"'{text}', {par}, {rts}, {n});\n")

    def sql(rev2: bool) -> str:
        s = slack("a" * 32, "1700000000.000100", "C0AAAAAAA1", root_text, None, "1700000000.000100", 1)
        s += slack("b" * 32, "1700000500.250000", "C0AAAAAAA1", reply, "a" * 32, "1700000000.000100", 0)
        s += ("INSERT INTO gmail.gmail_threads (id, user_email, snippet)\nVALUES ('me@x.co/18000000000000001', "
              "'me@x.co', 'Hi both, following up');\n")
        s += ("INSERT INTO gmail.gmail_messages (id, thread_id, user_email, snippet, body_text, in_reply_to, "
              "internal_date)\nVALUES ('me@x.co/<m2@mail.x.co>', 'me@x.co/18000000000000001', 'me@x.co', "
              f"'Hi both, following up on the transfer question', '{mail}', '<m1@mail.x.co>', '1700000900000');\n")
        s += ("INSERT INTO linear.linear_comments (id, issue_id, body)\nVALUES ('comment_0001aaaa', 'ENG-9', "
              "'not a bug as filed, but the fix for the crash on resume rides on this ticket, keep it in the gate');\n")
        if rev2:
            s += slack("c" * 32, "1700009999.000001", "D0BBBBBBB2", "rev2 only: a direct message that tells the "
                       "two revisions apart for the binding check in the self test fixture", None, None, 0)
        return s

    b64 = base64.urlsafe_b64encode(mail.encode()).decode().rstrip("=")
    thread_full = {"ok": True, "messages": [
        {"ts": 1700000000.0001, "text": root_text, "reply_count": 1},
        {"ts": 1700000500.25, "text": reply}]}
    search_hit = {"messages": [{"id": "me@x.co/<m2@mail.x.co>", "threadId": "me@x.co/18000000000000001"}]}
    listing = {"threads": [{"id": "me@x.co/18000000000000001", "snippet": "Hi both, following up on the transfer question"}]}
    full_mail = {"id": "me@x.co/<m2@mail.x.co>", "payload": {"body": {"size": len(mail), "data": b64}}}
    spill = ("Error: result (90,000 characters) exceeds maximum allowed tokens. Output has been saved to "
             "/home/agent/tool-results/x.txt.")
    marker = {"ok": True, "messages": [{"ts": 1700009999.000001, "text": "rev2 only: a direct message that tells "
              "the two revisions apart for the binding check in the self test fixture"}]}
    runs = {
        # opens the reply through a thread fetch (float ts), the mail through get_thread (base64 body)
        1: [("mcp__hg__slack_read_channel", {"channel_id": "C0AAAAAAA1"}, {"ok": True, "messages": [thread_full["messages"][0]]}, None),
            ("mcp__hg__slack_read_thread", {"channel_id": "C0AAAAAAA1", "message_ts": "1700000000.000100"}, thread_full, None),
            ("mcp__hg__gmail_get_thread", {"thread_id": "me@x.co/18000000000000001"}, {"messages": [full_mail]}, None),
            ("mcp__hg__slack_read_channel", {"channel_id": "D0BBBBBBB2"}, marker, None)],
        # sees the root only (latest_reply shows the reply's ts), a search hit and a thread list: snippets only
        2: [("mcp__hg__slack_read_channel", {"channel_id": "C0AAAAAAA1"},
             {"ok": True, "messages": [{"ts": 1700000000.0001, "text": root_text, "latest_reply": "1700000500.250000"}]}, None),
            ("mcp__hg__gmail_search_messages", {"query": "wire"}, search_hit, None),
            ("mcp__hg__gmail_list_threads", {"query": "wire"}, listing, None),
            ("mcp__hg__slack_read_channel", {"channel_id": "D0BBBBBBB2"}, marker, None)],
        # the thread fetch spills to a file and the text is never printed; the mail is fetched by id and spills
        3: [("mcp__hg__slack_read_thread", {"channel_id": "C0AAAAAAA1", "message_ts": "1700000000.000100"}, spill, None),
            ("mcp__hg__gmail_get_message", {"message_id": "me@x.co/<m2@mail.x.co>"}, spill, None),
            ("mcp__hg__slack_read_channel", {"channel_id": "D0BBBBBBB2"}, marker, None)],
        # a subagent prints the reply from a spilled file with a shell command; the write echo must not count
        4: [("mcp__hg__slack_read_thread", {"channel_id": "C0AAAAAAA1", "message_ts": "1700000000.000100"}, spill, None),
            ("Agent", {"description": "read", "prompt": "read the file"}, "launched", None),
            ("Bash", {"command": "python3 dump.py"}, '{"text": "' + reply.replace(",", "\\u002c") + '"}', "toolu_001"),
            ("mcp__hg__gmail_send_message", {"to": "a@x.co", "body": mail}, {"id": "sent", "body": mail}, None),
            ("mcp__hg__slack_read_channel", {"channel_id": "D0BBBBBBB2"}, marker, None)],
    }
    root = Path(tmp) / "archives"
    ti = root / "demo_task" / "task_inputs"
    for rev, flag in (("rev1", False), ("rev2", True)):
        d = ti / "Working_Files" / "run_forensics" / rev
        d.mkdir(parents=True)
        (d / "01_Universe_Inject.sql").write_text(sql(flag), encoding="utf-8")
    (ti / "01_Universe_Inject.sql").write_text(sql(True), encoding="utf-8")
    (ti / "07_Baseline_Trajectories").mkdir()
    (ti / "06_PreCheck_Trajectory").mkdir()
    names = []
    for n, calls in runs.items():
        name = f"07_Baseline_Trajectories/trajectory-run-{n}.json"
        (ti / name).write_text(json.dumps(_fixture_events(calls)), encoding="utf-8")
        names.append(name)
    # a pre-check that never saw the rev2 marker: content cannot bind it, and no reason is given
    (ti / "06_PreCheck_Trajectory" / "trajectory.json").write_text(json.dumps(_fixture_events(runs[1][:3])),
                                                                   encoding="utf-8")
    (ti / "Working_Files" / "12_difficulty_input.json").write_text(json.dumps({
        "rubrics": [{"id": "R1"}, {"id": "R2"}, {"id": "R3"}],
        "rollouts": [{"id": f"run-{n}", "status": "completed", "file": f"trajectory-run-{n}.json",
                      "results": {"R1": n in (1, 4), "R2": n in (1, 4), "R3": n == 1}} for n in runs]}),
        encoding="utf-8")
    policy = Path(tmp) / "policy.json"
    policy.write_text(json.dumps({"budget": {
        "carriers_that_miss": ["reply_under_unrelated_parent", "email_reply_via_get_thread", "non_set_ticket",
                               "dm_with_non_owner"],
        "carriers_without_loss": ["decoy"]}}), encoding="utf-8")

    def unit(name, rec, service, carrier, action, rows, run_set="baseline", **extra):
        d = {"service": service, "record_id": rec, "container": extra.pop("container", ""), "injected": True}
        d.update(extra)
        return {"task": "demo_task", "revision": "rev2", "run_set": run_set, "unit": name,
                "mechanism_family": "A11", "decider": d, "carrier": carrier,
                "habit": {"service": service, "action": action}, "rows": rows, "evidence": ["fixture"],
                "confidence": "high", "note": ""}

    doc = {"schema": SCHEMA_UNITS, "run_sets": [
        {"task": "demo_task", "revision": "rev2", "run_set": "baseline", "trajectories": names,
         "sql": "Working_Files/run_forensics/rev2/01_Universe_Inject.sql"},
        {"task": "demo_task", "revision": "rev2", "run_set": "precheck",
         "trajectories": ["06_PreCheck_Trajectory/trajectory.json"],
         "sql": "Working_Files/run_forensics/rev2/01_Universe_Inject.sql"}],
        "units": [
            unit("CORR", "C0AAAAAAA1/1700000500.250000", "slack", "reply_under_unrelated_parent", "thread_replies",
                 ["R1", "R2"]),
            unit("RET", "me@x.co/<m2@mail.x.co>", "gmail", "email_reply_via_get_thread", "get_thread", ["R3"]),
            unit("FILT", "comment_0001aaaa", "linear", "non_set_ticket", "list_comments", []),
            unit("CORR", "C0AAAAAAA1/1700000500.250000", "slack", "reply_under_unrelated_parent", "thread_replies",
                 [], run_set="precheck")],
        "skipped": [{"task": "demo_task", "unit": "ALIAS", "reason": "no single deciding record"}]}
    units_path = Path(tmp) / "units.json"
    units_path.write_text(json.dumps(doc), encoding="utf-8")
    return {"root": root, "units_path": units_path, "policy": policy, "doc": doc, "unit": unit, "reply": reply}


def _self_test() -> None:
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("carrier_backfill_selftest_") as tmp:
        fx = _fixture(Path(tmp))
        root, units_path, policy, doc, unit, reply = (fx[k] for k in ("root", "units_path", "policy", "doc", "unit",
                                                                     "reply"))
        res = evaluate(units_path, root, policy_path=policy)
        by = {(r["unit"], r["run_set"]): r for r in res["rates"]["units"]}
        corr = {r["run"]: r for r in by[("CORR", "baseline")]["runs"]}
        assert corr["run-1"]["opened"] and corr["run-1"]["how"] == "text" and corr["run-1"]["step"] == 2, corr["run-1"]
        assert corr["run-1"]["tool"] == "slack_read_thread" and corr["run-1"]["container_step"] == 2
        assert not corr["run-2"]["opened"] and corr["run-2"]["snippet_only"], corr["run-2"]   # latest_reply ts only
        assert not corr["run-3"]["opened"] and corr["run-3"]["container_spilled"], corr["run-3"]
        assert corr["run-4"]["opened"] and corr["run-4"]["context"] == "subagent" and corr["run-4"]["tool"] == "Bash"
        ret = {r["run"]: r for r in by[("RET", "baseline")]["runs"]}
        assert ret["run-1"]["opened"] and ret["run-1"]["tool"] == "gmail_get_thread", ret["run-1"]   # base64 body
        assert not ret["run-2"]["opened"] and ret["run-2"]["snippet_only"], ret["run-2"]           # id + snippet
        assert ret["run-3"]["opened"] and ret["run-3"]["how"] == "direct_get_spilled", ret["run-3"]
        assert not ret["run-4"]["opened"], ret["run-4"]                                            # write echo
        assert by[("FILT", "baseline")]["totals"] == {"runs": 4, "opened": 0, "snippet_only": 0, "rows_graded_runs": 0,
                                                       "rows_right": 0}
        assert by[("CORR", "baseline")]["totals"] == {"runs": 4, "opened": 2, "snippet_only": 1, "rows_graded_runs": 4,
                                                       "rows_right": 2}
        pre = by[("CORR", "precheck")]
        assert pre["runs"][0]["binding"] == "INSUFFICIENT" and not pre["runs"][0]["counted"] and not pre["in_aggregate"]
        car = res["rates"]["carriers"]
        c = car["reply_under_unrelated_parent"]
        assert (c["runs"], c["opened"], c["units"], c["tasks"]) == (4, 2, 1, 1), c
        assert c["cross"] == {"opened_rows_right": 2, "opened_rows_wrong": 0, "missed_rows_right": 0,
                              "missed_rows_wrong": 2}, c["cross"]
        assert car["email_reply_via_get_thread"]["opened"] == 2 and car["email_reply_via_get_thread"]["rows_right"] == 1
        assert res["rates"]["habits"]["slack/thread_replies"]["runs"] == 4
        status = {x["id"]: x["status"] for x in res["checks"]}
        assert status["units.schema"] == "PASS" and status["units.deciders"] == "PASS", status
        assert status["runs.binding"] == "WARN" and status["rates.small_samples"] == "WARN", status
        assert status["rates.coverage"] == "WARN" and res["verdict"] == "WARN", status    # decoy, dm: no data
        assert res["rates"]["coverage"]["archives_covered"] == 1 and res["rates"]["coverage"]["skipped"] == 1
        # deterministic: the same inputs give the same bytes
        again = evaluate(units_path, root, policy_path=policy)
        assert json.dumps(res, sort_keys=True) == json.dumps(again, sort_keys=True)
        # the binding_accept reason counts the pre-check; a run bound to another revision never counts
        doc2 = json.loads(json.dumps(doc))
        doc2["run_sets"][1]["binding_accept"] = "the only pre-check stored; the hardening report names rev2"
        doc2["run_sets"][0]["sql"] = "Working_Files/run_forensics/rev1/01_Universe_Inject.sql"
        doc2["run_sets"][0]["binding_accept"] = "wrongly declared on purpose"
        for u in doc2["units"]:
            if u["run_set"] == "baseline":
                u["revision"] = "rev1"
        doc2["run_sets"][0]["revision"] = "rev1"
        units_path.write_text(json.dumps(doc2), encoding="utf-8")
        res2 = evaluate(units_path, root, policy_path=policy)
        by2 = {(r["unit"], r["run_set"]): r for r in res2["rates"]["units"]}
        assert by2[("CORR", "precheck")]["totals"]["runs"] == 1 and by2[("CORR", "precheck")]["totals"]["opened"] == 1
        assert all(r["binding"] == "BOUND_ELSEWHERE" and not r["counted"] for r in by2[("CORR", "baseline")]["runs"])
        # planted-bad units: unknown carrier, a record that is not in the SQL, a label the row contradicts,
        # a needle that is not in the record, a Gmail thread id in place of a message
        bad = json.loads(json.dumps(doc))
        bad["units"][0]["carrier"] = "hidden_somewhere"
        units_path.write_text(json.dumps(bad), encoding="utf-8")
        res3 = evaluate(units_path, root, policy_path=policy)
        assert res3["verdict"] == "FAIL" and res3["rates"] is None and "hidden_somewhere" in res3["checks"][0]["detail"]
        bad = json.loads(json.dumps(doc))
        bad["units"][0]["decider"]["record_id"] = "C0AAAAAAA1/1700000777.000000"
        bad["units"][1]["decider"]["needles"] = ["a sentence that is not in the mail at all"]
        bad["units"][2]["carrier"] = "dm_with_non_owner"
        bad["units"].append(unit("THREAD", "me@x.co/18000000000000001", "gmail", "other:thread id", "get_thread", []))
        units_path.write_text(json.dumps(bad), encoding="utf-8")
        res4 = evaluate(units_path, root, policy_path=policy)
        st4 = {x["id"]: x for x in res4["checks"]}
        assert res4["verdict"] == "FAIL" and st4["units.deciders"]["status"] == "FAIL", st4
        assert "not a row" in st4["units.deciders"]["detail"] and "is a Gmail thread" in st4["units.deciders"]["detail"]
        assert "not in the record" in st4["units.deciders"]["detail"]
        assert st4["units.structure"]["status"] == "WARN" and "dm_with_non_owner" in st4["units.structure"]["detail"]
        # write and show
        units_path.write_text(json.dumps(doc), encoding="utf-8")
        out = write_rates(evaluate(units_path, root, policy_path=policy)["rates"], Path(tmp) / "rates.json")
        stored = load_rates(out)
        assert stored["schema"] == SCHEMA_RATES and carrier_rate("reply_under_unrelated_parent", stored)["opened"] == 2
        assert habit_rate("gmail", "get_thread", stored)["runs"] == 4 and carrier_rate("decoy", stored) is None
        text = "\n".join(table_lines(stored, "reply_under_unrelated_parent"))
        assert "2/4 (0.50)" in text and "not opened and wrong 2" in text, text
    # text helpers
    assert norm_text('He said \\"go\\",\\n then’s it') == norm_text("He said go, then's it")
    assert ts_forms("1700000500.250000") == ["1700000500.250000", "1700000500.25"]
    assert ts_forms("1771027942.000000") == ["1771027942.000000", "1771027942.0"]
    deep, head = text_windows(norm_text(reply), "")
    assert head == norm_text(reply)[:WINDOW] and deep and all(norm_text(reply).index(w) >= HEAD_CHARS for w in deep)
    assert text_windows("short text only", "") == ([], None)
    print("self-test: ok (opened by thread fetch, base64 mail body, shell print in a subagent, spilled direct get; "
          "snippet-only by id, list snippet and latest_reply; spilled container not counted; write echo ignored; "
          "rows and cross counts; binding accept and bound-elsewhere; planted-bad carrier, record id, needle, "
          "thread id and label; write, show and determinism)")


# ------------------------------------------------------------------ CLI

def main(argv: list) -> int:
    ap = argparse.ArgumentParser(prog="carrier_backfill.py", description="Carrier find rates from the archived runs.")
    ap.add_argument("--self-test", action="store_true", help="run the built-in checks on a synthetic archive")
    sub = ap.add_subparsers(dest="cmd")
    c = sub.add_parser("compute", help="read the units and the archived runs; print or write the table")
    c.add_argument("--units", help="curated units file (default references/carrier_backfill_units.json)")
    c.add_argument("--tasks-root", help="folder of archived tasks (default support/completed_tasks)")
    c.add_argument("--task", action="append", help="only this archive (repeatable); do not combine with --write")
    c.add_argument("--write", action="store_true", help="write references/carrier_find_rates.json")
    c.add_argument("--out", help="write to this file instead (implies --write)")
    c.add_argument("--detail", action="store_true", help="also print one line per unit with its runs")
    c.add_argument("--json", action="store_true")
    s = sub.add_parser("show", help="print the stored aggregate table")
    s.add_argument("--carrier", help="one carrier, with its units and the rows-against-opened counts")
    s.add_argument("--rates", help="table file (default references/carrier_find_rates.json)")
    s.add_argument("--json", action="store_true")
    try:
        args = ap.parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code not in (0, None) else 0
    if args.self_test:
        _self_test()
        return 0
    if args.cmd == "show":
        path = Path(args.rates) if args.rates else RATES_PATH
        if not path.is_file():
            print(f"carrier_backfill: {path} does not exist; run `compute --write` first", file=sys.stderr)
            return 2
        rates = load_rates(path)
        if args.carrier and args.carrier not in (rates.get("carriers") or {}):
            print(f"carrier_backfill: no data for carrier {args.carrier!r}; known: "
                  f"{', '.join(sorted(rates.get('carriers') or {}))}", file=sys.stderr)
            return 2
        if args.json:
            print(json.dumps(rates["carriers"][args.carrier] if args.carrier else
                             {"carriers": rates["carriers"], "habits": rates["habits"], "coverage": rates["coverage"]},
                             indent=1, sort_keys=True, ensure_ascii=False))
            return 0
        cov = rates["coverage"]
        print(f"CARRIER FIND RATES ({cov['archives_covered']} of {cov['archives_total']} archives, "
              f"{cov['units_in_aggregate']} units, {cov['unit_runs_counted']} unit-run observations)")
        print("\n".join(table_lines(rates, args.carrier)))
        if not args.carrier:
            print("\nper habit (service/action):")
            print("\n".join(table_lines(rates, key="habits")))
        return 0
    if args.cmd == "compute":
        if args.task and (args.write or args.out):
            print("carrier_backfill: --task gives a partial table; it cannot be written", file=sys.stderr)
            return 2
        try:
            result = evaluate(args.units, args.tasks_root, set(args.task) if args.task else None)
        except (OSError, ValueError) as exc:
            print(f"carrier_backfill: {exc}", file=sys.stderr)
            return 2
        if (args.write or args.out) and result["rates"] is not None and result["verdict"] != "FAIL":
            try:
                out = write_rates(result["rates"], args.out)
            except Exception as exc:   # ContextError from task_context, or an OS error
                print(f"carrier_backfill: {exc}", file=sys.stderr)
                return 2
            result["written"] = _rel(out)
        if args.json:
            print(json.dumps(result, indent=1, sort_keys=True, ensure_ascii=False))
        else:
            cov = (result.get("rates") or {}).get("coverage") or {}
            print(render(result, f"{cov.get('archives_covered', 0)} of {cov.get('archives_total', 0)} archives",
                         args.detail))
            if result.get("written"):
                print(f"\nwrote {result['written']}")
        return 1 if result["verdict"] == "FAIL" else 0
    ap.print_usage(sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
