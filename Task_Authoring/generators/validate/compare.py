"""Diff the intended ops against the ops parsed back from the emitted SQL.

Independent of both the emitter and the eval tokenizer: it only looks at Op records (values are None,
bool, int, decimal.Decimal or str). Two comparisons are offered:

  compare_ops       ordered and exact. Same length, same table, same op, the same column names in the
                    same order, and typed-equal values: None only equals None, bool only bool, numbers
                    by Decimal(str(x)), strings exactly. A *_json column whose texts differ but whose
                    json.loads values are equal is reported as kind "json_format" (a formatting diff,
                    not a value diff).

  compare_multiset  for shadow comparisons against SQL written by other code: ops are matched by
                    (table, op, key_of(op)), column order does not matter, *_json columns are compared
                    structurally, and the caller may ignore table/column differences or treat an INSERT
                    column missing on one side as NULL.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation

from generators.core.ops import INSERT, Op

NUMBERS = (int, Decimal)


@dataclass(frozen=True)
class Diff:
    index: int
    kind: str
    table: str
    column: str | None
    intended: object
    parsed: object
    message: str


# ---------------------------------------------------------------- value equality

def _is_number(value) -> bool:
    return isinstance(value, NUMBERS) and not isinstance(value, bool)


def values_equal(a, b) -> bool:
    """Typed equality: None only None, bool only bool, numbers by Decimal(str(x)), strings exactly."""
    if a is None or b is None:
        return a is None and b is None
    if isinstance(a, bool) or isinstance(b, bool):
        return isinstance(a, bool) and isinstance(b, bool) and a == b
    if isinstance(a, str) or isinstance(b, str):
        return isinstance(a, str) and isinstance(b, str) and a == b
    if _is_number(a) and _is_number(b):
        try:
            return Decimal(str(a)) == Decimal(str(b))
        except (InvalidOperation, ValueError):
            return False
    return a == b


def _json_values(a, b):
    """True/False when both are strings holding JSON, else None."""
    if not (isinstance(a, str) and isinstance(b, str)):
        return None
    try:
        return json.loads(a) == json.loads(b)
    except (ValueError, TypeError):
        return None


def _value_diff(column: str, intended, parsed):
    """(kind, message) for two values that already failed values_equal, or None."""
    if values_equal(intended, parsed):
        return None
    if column.endswith("_json"):
        equal = _json_values(intended, parsed)
        if equal:
            return ("json_format",
                    f"{column}: same JSON value, different text ({intended!r} vs {parsed!r})")
        if equal is False:
            return ("value", f"{column}: JSON value differs ({intended!r} vs {parsed!r})")
    return ("value", f"{column}: {intended!r} != {parsed!r}")


def _pair_diffs(index: int, table: str, label: str,
                intended_pairs, parsed_pairs) -> list[Diff]:
    """Ordered, exact pair comparison (INSERT/SET columns and UPDATE WHERE keys)."""
    diffs: list[Diff] = []
    intended_names = [name for name, _ in intended_pairs]
    parsed_names = [name for name, _ in parsed_pairs]
    if intended_names != parsed_names:
        diffs.append(Diff(index, "column", table, None, tuple(intended_names), tuple(parsed_names),
                          f"op {index} {label}: columns differ or are out of order "
                          f"{intended_names} != {parsed_names}"))
    for (name, left), (other, right) in zip(intended_pairs, parsed_pairs):
        if name != other:
            continue                      # already reported above; values are not comparable
        found = _value_diff(name, left, right)
        if found:
            kind, message = found
            diffs.append(Diff(index, kind, table, name, left, right, f"op {index} {label}: {message}"))
    return diffs


# ---------------------------------------------------------------- ordered comparison

def compare_ops(intended: list[Op], parsed: list[Op]) -> list[Diff]:
    """Ordered, exact comparison of the intended ops and the ops parsed back from the SQL."""
    diffs: list[Diff] = []
    if len(intended) != len(parsed):
        diffs.append(Diff(min(len(intended), len(parsed)), "length", "", None, len(intended), len(parsed),
                          f"op count {len(intended)} (intended) != {len(parsed)} (parsed)"))
    for index in range(min(len(intended), len(parsed))):
        left, right = intended[index], parsed[index]
        if left.table != right.table:
            diffs.append(Diff(index, "table", left.table, None, left.table, right.table,
                              f"op {index}: table {left.table!r} != {right.table!r}"))
        if left.op != right.op:
            diffs.append(Diff(index, "op", left.table, None, left.op, right.op,
                              f"op {index}: operation {left.op!r} != {right.op!r}"))
        diffs.extend(_pair_diffs(index, left.table, "cols", left.cols, right.cols))
        diffs.extend(_pair_diffs(index, left.table, "where", left.where, right.where))
    return diffs


# ---------------------------------------------------------------- multiset comparison

def compare_multiset(intended: list[Op], parsed: list[Op], key_of,
                     ignore=(), omitted_as_null: bool = False) -> list[Diff]:
    """Match ops by (table, op, key_of(op)) and compare their columns by name.

    ignore=set(("table", "column")): skip table differences and column-presence differences.
    omitted_as_null: an INSERT column present on one side and absent on the other, where the present
    value is None, counts as equal.
    """
    ignored = set(ignore)
    def key(op: Op):
        table = None if "table" in ignored else op.table
        return (table, op.op, tuple(key_of(op)))

    buckets: dict[tuple, list[Op]] = {}
    for op in parsed:
        buckets.setdefault(key(op), []).append(op)

    diffs: list[Diff] = []
    for index, op in enumerate(intended):
        bucket = buckets.get(key(op))
        if not bucket:
            diffs.append(Diff(index, "missing", op.table, None, op.as_dict(), None,
                              f"op {index}: no parsed op for {key(op)!r}"))
            continue
        other = bucket.pop(0)
        diffs.extend(_multiset_diffs(index, op, other, ignored, omitted_as_null))
    for bucket in buckets.values():
        for op in bucket:
            diffs.append(Diff(len(intended), "extra", op.table, None, None, op.as_dict(),
                              f"unexpected parsed op for {key(op)!r}"))
    return diffs


def _multiset_diffs(index: int, left: Op, right: Op, ignored: set[str],
                    omitted_as_null: bool) -> list[Diff]:
    diffs: list[Diff] = []
    if "table" not in ignored and left.table != right.table:
        diffs.append(Diff(index, "table", left.table, None, left.table, right.table,
                          f"op {index}: table {left.table!r} != {right.table!r}"))
    if left.op != right.op:
        diffs.append(Diff(index, "op", left.table, None, left.op, right.op,
                          f"op {index}: operation {left.op!r} != {right.op!r}"))
    diffs.extend(_multiset_pairs(index, left, left.cols, right.cols, ignored, omitted_as_null))
    diffs.extend(_multiset_pairs(index, left, left.where, right.where, ignored, False))
    return diffs


def _multiset_pairs(index: int, op: Op, intended_pairs, parsed_pairs, ignored: set[str],
                    omitted_as_null: bool) -> list[Diff]:
    diffs: list[Diff] = []
    left = dict(intended_pairs)
    right = dict(parsed_pairs)
    for name in left.keys() - right.keys():
        if omitted_as_null and op.op == INSERT and left[name] is None:
            continue
        if "column" in ignored:
            continue
        diffs.append(Diff(index, "column", op.table, name, left[name], None,
                          f"op {index}: column {name!r} only in the intended op"))
    for name in right.keys() - left.keys():
        if omitted_as_null and op.op == INSERT and right[name] is None:
            continue
        if "column" in ignored:
            continue
        diffs.append(Diff(index, "column", op.table, name, None, right[name],
                          f"op {index}: column {name!r} only in the parsed op"))
    for name in left.keys() & right.keys():
        found = _value_diff(name, left[name], right[name])
        if found:
            kind, message = found
            diffs.append(Diff(index, kind, op.table, name, left[name], right[name],
                              f"op {index}: {message}"))
    return diffs
