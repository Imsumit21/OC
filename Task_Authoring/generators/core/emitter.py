"""Operations -> SQL text in the restricted grammar, with early schema checks.

The early checks reuse the gate's own schema loader and row rules (tools/sql_lint.py), so a bad row stops the render
at once with its record key. They are NOT the independent validation: that is validate/parse_back.py (the eval's
tokenizer), validate/compare.py and validate/invariants.py on the published bytes.
"""
from __future__ import annotations

from .context import tools_module
from .ops import INSERT, Op
from .sqlvalue import ident, literal

MARKER = "-- Are you planning to inject? Yes"

_SQL_LINT = None


def sql_lint():
    global _SQL_LINT
    if _SQL_LINT is None:
        _SQL_LINT = tools_module("sql_lint")
    return _SQL_LINT


def load_schema() -> dict:
    return sql_lint().load_schema()


def primary_key(table: str) -> tuple:
    return tuple(sql_lint().PRIMARY_KEYS.get(table, ("id",)))


def _lit_text(v):
    if v is None:
        return None
    if isinstance(v, bool):
        return "true" if v else "false"
    return str(v)


def check_op(op: Op, schema: dict, freeze_utc: str) -> tuple[list[str], list[str]]:
    """Early (errors, warnings) for one operation."""
    sl = sql_lint()
    where = f"{op.table} {dict(op.where) or op.col('id') or op.col('event_id') or ''} [{op.record or 'derived'}]"
    if op.table not in schema:
        return [f"{where}: unknown table"], []
    cols = schema[op.table]
    errs, warns = [], []
    names = [c for c, _ in op.cols] + [c for c, _ in op.where]
    errs += [f"{where}: unknown column {c}" for c in names if c not in cols]
    errs += [f"{where}: generated column {c} is written" for c, _ in op.cols if c in cols and cols[c]["generated"]]
    errs += [f"{where}: NULL in NOT NULL column {c}" for c, v in op.cols
             if v is None and c in cols and not cols[c]["nullable"]]
    if op.op == INSERT:
        given = {c for c, _ in op.cols}
        errs += [f"{where}: NOT NULL column {c} missing" for c, m in cols.items()
                 if not m["nullable"] and m["default"] is None and not m["generated"] and c not in given]
        sl.row_rules(op.table, {c: _lit_text(v) for c, v in op.cols}, 0,
                     lambda line, msg: errs.append(f"{where}: {msg}"),
                     lambda line, msg: warns.append(f"{where}: {msg}"))
    freeze = sl.parse_time(freeze_utc)
    for c, v in op.cols:
        if isinstance(v, str) and sl.PAST_ONLY.search(c) and not sl.FUTURE_OK.search(c):
            t = sl.parse_time(v)
            if t and freeze and t >= freeze:
                errs.append(f"{where}: {c}={v} is on/after the seed bound {freeze_utc}")
    return errs, warns


def to_sql(op: Op) -> str:
    if op.op == INSERT:
        cols = ", ".join(ident(c) for c, _ in op.cols)
        vals = ", ".join(literal(v) for _, v in op.cols)
        return f"INSERT INTO {op.table} ({cols}) VALUES ({vals});"
    sets = ", ".join(f"{ident(c)} = {literal(v)}" for c, v in op.cols)
    keys = " AND ".join(f"{ident(c)} = {literal(v)}" for c, v in op.where)
    return f"UPDATE {op.table} SET {sets} WHERE {keys};"


def render_part(service: str, ops: list[Op]) -> str:
    """One service section: a banner line, then one statement per line (no comments inside the section)."""
    lines = [f"-- ===================== {service.upper()} ====================="]
    lines += [to_sql(op) for op in ops]
    return "\n".join(lines) + "\n"


def render_full(header: list[str], parts: list[str]) -> str:
    """A complete injection file: marker on line 1, header comments, BEGIN, parts, COMMIT."""
    for h in header:
        if not h.startswith("-- ") or "\n" in h:
            raise ValueError(f"header lines must be single '-- ' comment lines: {h!r}")
    body = "".join(parts)
    return "\n".join([MARKER, *header, "BEGIN;"]) + "\n" + body + "COMMIT;\n"
