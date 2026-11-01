"""The one SQL literal policy of the generators.

Kept identical to the policy that passed platform /injection in task 1 (task_inputs/Working_Files/plan/sql_common.py
q/j/col): standard strings with '' doubling; an E'' string only when the text holds a raw line break, with backslash,
CR and LF escaped; JSON columns as text produced by json.dumps(..., ensure_ascii=False) with default separators.
Characters PostgreSQL text cannot hold (NUL) and other C0 controls except TAB/LF/CR are refused rather than escaped.
"""
from __future__ import annotations

import json
import re
from decimal import Decimal

# Identifiers that must be quoted even when lower case (reserved words seen in the live schema).
RESERVED = {"references", "desc", "primary", "index", "user", "order", "end", "default", "check", "table", "to", "from",
            "group", "limit", "offset"}
_PLAIN_IDENT = re.compile(r"^[a-z_][a-z0-9_]*$")
_BAD_CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


def ident(name: str) -> str:
    if '"' in name:
        raise ValueError(f"identifier with a double quote: {name!r}")
    return name if (_PLAIN_IDENT.match(name) and name not in RESERVED) else f'"{name}"'


def literal(v) -> str:
    if v is None:
        return "NULL"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, Decimal):
        if not v.is_finite():
            raise ValueError(f"non-finite number {v!r}")
        text = format(v, "f")
        return text
    if isinstance(v, float):
        raise TypeError("floats are not allowed; use int or decimal.Decimal for exact numbers")
    if not isinstance(v, str):
        raise TypeError(f"unsupported literal type {type(v).__name__}")
    if _BAD_CONTROL.search(v):
        raise ValueError(f"text holds a control character PostgreSQL text cannot carry safely: {v[:60]!r}")
    s = v.replace("'", "''")
    if "\n" in s or "\r" in s:
        s = s.replace("\\", "\\\\").replace("\r", "\\r").replace("\n", "\\n")
        return "E'" + s + "'"
    return "'" + s + "'"


def json_text(obj) -> str:
    """Serialized JSON for a *_json column (default separators, as task 1)."""
    return json.dumps(obj, ensure_ascii=False)
