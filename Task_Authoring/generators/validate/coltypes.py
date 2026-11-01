"""Column types: would PostgreSQL accept each parsed value for its live column? (independent of the emitter)

Reads references/universe_schema_live.json directly. Per udt:
  int2 / int4 / int8      a Python int (not bool) inside the type's range
  numeric / float4/8      int or finite Decimal
  bool                    bool
  varchar(n) / text       str, at most n characters when the column has a max_length, no NUL
  json / jsonb            str that json.loads accepts without NaN/Infinity
  date                    a real calendar date 'YYYY-MM-DD'
  timestamp / timestamptz a real 'YYYY-MM-DD[ T]HH:MM:SS[.ffffff][Z|±HH[:MM]]'
  anything else           refused (fail closed)
An explicit NULL is accepted only where the column is nullable (a column default applies to an omitted column, never to
a written NULL). An INSERT must write every NOT NULL column without a default, and no statement may write a generated
column.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
from decimal import Decimal
from pathlib import Path

RANGES = {"int2": (-2 ** 15, 2 ** 15 - 1), "int4": (-2 ** 31, 2 ** 31 - 1), "int8": (-2 ** 63, 2 ** 63 - 1)}
_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$", re.ASCII)
_TS = re.compile(r"^\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}(\.\d{1,6})?(Z|[+-]\d{2}(:?\d{2})?)?$", re.ASCII)
_SCHEMAS: dict[tuple, dict] = {}


def load(path: Path) -> dict:
    """The schema as {table: {column: meta}}, cached by file content (a changed file is read again)."""
    raw = Path(path).read_bytes()
    key = (str(Path(path).resolve()), hashlib.sha256(raw).hexdigest())
    if key not in _SCHEMAS:
        out = {}
        for t in json.loads(raw.decode("utf-8")):
            out[f"{t['table_schema']}.{t['table_name']}"] = {c["column"]: c for c in t["columns"]}
        _SCHEMAS[key] = out
    return _SCHEMAS[key]


def problem(col: dict, value) -> str | None:
    udt = col["udt"]
    if value is None:
        return None if col["nullable"] == "YES" else "NULL in a NOT NULL column"
    if udt in RANGES:
        lo, hi = RANGES[udt]
        if isinstance(value, bool) or not isinstance(value, int):
            return f"{udt} needs an integer, got {type(value).__name__} {value!r}"
        return None if lo <= value <= hi else f"{value} is outside the {udt} range [{lo}, {hi}]"
    if udt in ("numeric", "float4", "float8"):
        ok = (isinstance(value, int) and not isinstance(value, bool)) or (isinstance(value, Decimal)
                                                                          and value.is_finite())
        return None if ok else f"{udt} needs a number, got {type(value).__name__} {value!r}"
    if udt == "bool":
        return None if isinstance(value, bool) else f"bool needs true/false, got {value!r}"
    if not isinstance(value, str):
        return f"{udt} needs a string literal, got {type(value).__name__} {value!r}"
    if "\x00" in value:
        return "text holds NUL"
    if not _utf8(value):
        return "text holds a lone surrogate, which UTF-8 (and PostgreSQL) cannot store"
    if udt in ("varchar", "text", "bpchar"):
        n = col.get("max_length")
        return f"{len(value)} characters exceed {udt}({n})" if n and len(value) > n else None
    if udt in ("json", "jsonb"):
        try:                                    # PostgreSQL rejects NaN/Infinity and checks every pair, duplicates too
            doc = json.loads(value, parse_constant=_no_constant, object_pairs_hook=_Pairs)
        except ValueError as exc:
            return f"{udt} value is not JSON: {exc}"
        for s in _strings(doc):
            if not _utf8(s):
                return f"{udt} value holds an unpaired \\u surrogate escape"
            if udt == "jsonb" and "\x00" in s:
                return "jsonb cannot hold \\u0000"
        return None
    if udt == "date":
        try:
            if _DATE.match(value):
                dt.date.fromisoformat(value)
                return None
        except ValueError:
            pass
        return f"date needs a real YYYY-MM-DD, got {value!r}"
    if udt in ("timestamp", "timestamptz"):
        try:
            if _TS.match(value):
                dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
                return None
        except ValueError:
            pass
        return f"{udt} needs a real ISO-8601 timestamp, got {value!r}"
    return f"unsupported column type {udt}"


def _no_constant(name):
    raise ValueError(f"{name} is not valid JSON")


def _utf8(s: str) -> bool:
    try:
        s.encode("utf-8")
        return True
    except UnicodeEncodeError:
        return False


class _Pairs(list):
    """A JSON object kept as all of its (key, value) pairs, so a repeated key cannot hide an earlier value."""


def _strings(value):
    """Every string in a decoded JSON value, keys and the values of repeated keys included."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, _Pairs):
        for k, v in value:
            yield k
            yield from _strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from _strings(v)


def check_ops(ops, schema_path: Path) -> list[str]:
    schema = load(schema_path)
    out = []
    for n, op in enumerate(ops):
        cols = schema.get(op.table)
        if cols is None:
            out.append(f"op {n} {op.table}: table not in the live schema")
            continue
        key = ", ".join(f"{c}={v}" for c, v in op.where) or f"{op.cols[0][0]}={op.cols[0][1]}"
        if op.op == "insert":
            given = {c for c, _ in op.cols}
            out += [f"{op.table} {key}: NOT NULL column {c} has no default and is not written"
                    for c, meta in sorted(cols.items())
                    if c not in given and meta["nullable"] == "NO" and meta.get("default") is None
                    and meta.get("generated", "NEVER") == "NEVER" and meta.get("identity", "NO") == "NO"]
        for c, _ in op.cols:
            if (cols.get(c) or {}).get("generated", "NEVER") not in ("NEVER", None):
                out.append(f"{op.table} {key} {c}: a generated column; PostgreSQL refuses a written value")
        for c, v in tuple(op.cols) + tuple(op.where):
            meta = cols.get(c)
            if meta is None:
                out.append(f"{op.table} {key}: column {c} not in the live schema")
                continue
            p = problem(meta, v)
            if p:
                out.append(f"{op.table} {key} {c}: {p}")
    return out
