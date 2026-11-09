#!/usr/bin/env python3
"""Shared helpers for the Leonard stockholder close-out OE builders (ledger, events, check).

Every value that reaches an Expected line is checked here as an exact substring of its record:
base records are re-read through tools/hg.py (`search get`, decoded text, cached per run in
oe_cache.json next to this file); seeded records come from the parsed injection SQL
(tools/base_check.parse_sql, never executed). A quote that is not a substring stops the build.
"""
import json
import os
import re
import subprocess
import sys
import threading

HERE = os.path.dirname(os.path.abspath(__file__))
PLAN = os.path.dirname(HERE)
WF = os.path.dirname(PLAN)
TI = os.path.dirname(WF)
TA = os.path.dirname(TI)
WS = os.path.dirname(TA)
PY = os.path.expanduser("~/.local/bin/python3.12")
TDREL = "Task_Authoring/task_inputs"
ENV = {**os.environ, "TASK_AUTHORING_TASK_DIR": TDREL}
sys.path.insert(0, os.path.join(TA, "tools"))
from base_check import parse_sql  # noqa: E402

SQL_PATH = os.path.join(TI, "01_Universe_Inject.sql")
SQL = open(SQL_PATH).read()
STMTS = parse_sql(SQL)
CACHE_PATH = os.path.join(HERE, "oe_cache.json")
_cache = json.load(open(CACHE_PATH)) if os.path.exists(CACHE_PATH) else {}


_lock = threading.Lock()


def _save():
    with _lock:
        snap = dict(_cache)
        tmp = CACHE_PATH + ".tmp"
        json.dump(snap, open(tmp, "w"), indent=0, ensure_ascii=False)
        os.replace(tmp, CACHE_PATH)


def run(args, timeout=900):
    return subprocess.run(args, cwd=WS, capture_output=True, text=True, env=ENV, timeout=timeout)


def _leaves(v):
    if isinstance(v, str):
        return [v]
    if isinstance(v, dict):
        return [x for k in v for x in _leaves(v[k])]
    if isinstance(v, list):
        return [x for k in v for x in _leaves(k)]
    return [] if v is None else [str(v)]


def hg_get(service, file, pointer):
    """Decoded text of one base record field, read through tools/hg.py (all pages)."""
    key = f"{service}|{file}|{pointer}"
    if key in _cache:
        return _cache[key]
    parts, offset = [], 0
    while True:
        args = [PY, "-B", "Task_Authoring/tools/hg.py", "search", "get", service, "--file", file, "--pointer", pointer]
        if offset:
            args += ["--offset", str(offset)]
        r = run(args)
        try:
            d = json.loads(r.stdout)
        except ValueError:
            raise SystemExit(f"hg.py get failed for {key}: {r.stderr[-400:]}")
        parts.append(d.get("text") or "")
        if not d.get("truncated"):
            break
        offset = d.get("next_offset")
    raw = "".join(parts)
    enc = d.get("encoding")
    text = raw
    if enc == "rendered-json":
        try:
            v = json.loads(raw)
            text = v if isinstance(v, str) else "\n".join(_leaves(v))
        except ValueError:
            text = raw
    _cache[key] = text
    return text


def sql_rows(table=None, **kw):
    out = []
    for s in STMTS:
        if table and s.get("table") != table:
            continue
        r = s.get("row") or {}
        if all(str(r.get(k)) == str(v) for k, v in kw.items()):
            out.append(s)
    return out


def sql_by_id(rid):
    """The INSERT statement whose id-like column equals rid (first match)."""
    for s in STMTS:
        if s["op"] != "insert":
            continue
        r = s["row"]
        for k in ("id", "identifier", "document_id", "spreadsheet_id", "presentation_id", "event_id", "contact_id"):
            if str(r.get(k)) == rid:
                return s
    raise KeyError(rid)


def norm(s):
    s = (s or "").replace("\\r", "").replace("\\n", "\n").replace("\r", "")
    return s


def sql_text(rid=None, line=None, field=None):
    """Text of a seeded row (all fields joined, or one field), JSON escapes decoded."""
    if line is not None:
        st = next(s for s in STMTS if s.get("line") == line)
    else:
        st = sql_by_id(rid)
    row = st.get("row") or st.get("set") or {}
    if field:
        return norm(str(row.get(field)))
    return "\n".join(norm(str(v)) for v in row.values())


def sql_line(rid):
    return sql_by_id(rid)["line"]


def squash(s):
    return re.sub(r"\s+", " ", s or "").strip()


def assert_quote(text, quote, where):
    if quote in text:
        return True
    if squash(quote) in squash(text):
        return True
    raise AssertionError(f"quote not in record {where}: {quote!r}")


def persona_can_see(service, rid):
    key = f"cansee|{service}|{rid}"
    if key in _cache:
        return _cache[key]
    r = run([PY, "-B", "Task_Authoring/tools/persona_view.py", "can-see", "leonard_hayes", service, rid])
    line = (r.stdout.strip().splitlines() or [""])[0]
    _cache[key] = line
    _save()
    return line
