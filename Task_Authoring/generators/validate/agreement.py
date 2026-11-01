"""Parser agreement: values where the repo's local parser and the eval tokenizer read different text (plan §3.6).

tools/base_check.parse_sql (used by base_check, fact_check, the task solvers and oracle_kit) keeps E'' escapes undecoded
(tools/sql_lint.py literal), while the eval tokenizer and PostgreSQL decode them. Until the shared decoder is fixed
(plan Phase 2), every such value is listed: a local check or solver that reads it sees different text than the run.
The local parser is imported read-only, on purpose: comparing it with the eval tokenizer is this module's job.
"""
from __future__ import annotations

from generators.core.context import tools_module
from generators.core.ops import INSERT


def _text(v):
    return None if v is None else str(v)


def disagreements(text: str, parsed: list) -> list[str]:
    """parsed: parse_back.parse_ops(text) for the same text. Returns one message per differing value."""
    rows = tools_module("base_check").parse_sql(text)
    local = [r for r in rows if r["op"] in ("insert", "update")]
    if len(local) != len(parsed):
        return [f"the local parser reads {len(local)} statements, the eval tokenizer {len(parsed)}"]
    out = []
    for n, (mine, op) in enumerate(zip(local, parsed)):
        if mine["table"] != op.table.lower():
            out.append(f"statement {n}: table {mine['table']} vs {op.table}")
            continue
        key = ", ".join(f"{k}={v}" for k, v in op.where) or f"{op.cols[0][0]}={op.cols[0][1]}"
        values = mine["row"] if op.op == INSERT else mine["set"]
        lowered = {k.lower(): v for k, v in values.items()}
        for col, v in op.cols:
            if isinstance(v, bool):
                continue                  # sql_lint.literal reads unquoted true/false as None; nothing local uses it
            seen = lowered.get(col.lower(), "<absent>")
            if seen != _text(v):
                out.append(f"{op.table} {key} {col}: the run reads {_text(v)!r}, local tools read {seen!r}")
    return out
