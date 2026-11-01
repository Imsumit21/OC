"""Operation records shared by the emitter, the parse-back validators and the overlay.

An Op is one SQL statement in the restricted grammar (validate/grammar.py): an INSERT of one row, or an UPDATE of one
row addressed by every primary-key column. Values are plain Python: None, bool, int, decimal.Decimal or str. JSON
columns (`*_json`) carry their serialized text (core/sqlvalue.json_text), never a Python list or dict, so the intended
value and the parsed value are the same type.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

INSERT, UPDATE = "insert", "update"


@dataclass(frozen=True)
class Op:
    table: str                                         # "schema.table"
    op: str                                            # INSERT | UPDATE
    cols: tuple[tuple[str, object], ...]               # INSERT columns in order, or UPDATE SET pairs in order
    where: tuple[tuple[str, object], ...] = ()         # UPDATE only: every primary-key column = value
    record: str | None = None                          # spec record key, or None for a derived companion
    prov: tuple[tuple[str, dict], ...] = field(default=(), compare=False)   # column -> provenance (not rendered)

    def __post_init__(self):
        if self.op not in (INSERT, UPDATE):
            raise ValueError(f"unknown op {self.op!r}")
        if "." not in self.table:
            raise ValueError(f"table must be schema-qualified: {self.table!r}")
        if self.op == UPDATE and not self.where:
            raise ValueError(f"{self.table}: UPDATE without a key")
        if self.op == INSERT and self.where:
            raise ValueError(f"{self.table}: INSERT with a WHERE")
        names = [c for c, _ in self.cols]
        if len(names) != len(set(names)):
            raise ValueError(f"{self.table}: duplicate column in {names}")
        for c, v in self.cols + self.where:
            check_value(self.table, c, v)

    def col(self, name, default=None):
        for c, v in self.cols:
            if c == name:
                return v
        return default

    def as_dict(self) -> dict:
        """Plain form compared by validate/compare.py: {"table", "op", "cols": {...}, "where": {...}}."""
        return {"table": self.table, "op": self.op, "cols": dict(self.cols), "where": dict(self.where)}


def check_value(table: str, col: str, v) -> None:
    if v is None or isinstance(v, (bool, int, str, Decimal)):
        if isinstance(v, Decimal) and not v.is_finite():
            raise ValueError(f"{table}.{col}: non-finite number {v!r}")
        return
    raise TypeError(f"{table}.{col}: unsupported value type {type(v).__name__} ({v!r}); "
                    "use None, bool, int, Decimal or str (JSON columns as serialized text)")
