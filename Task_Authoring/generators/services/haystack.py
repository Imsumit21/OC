"""Haystack records: a compact spec form for routine traffic around a deciding record.

A haystack record names fields shared by every row once (`fields`, ordinary spec values) and lists the rows in a short
form (`rows`); the loader expands it into one ordinary record per row before anything else looks at the spec:

  {"key": "HS1", "kind": "slack.haystack", "fields": {"channel": <value>},
   "rows": [{"user": "EMPLOYEE_0012_SLACK_ID", "at": "2025-09-26T16:02:00Z", "text": "texts/hs1_01.txt",
             "sha256": "<64 hex>"}, ...]}

becomes records HS1.001, HS1.002, ... of the emitter's target kind. Every field of an expanded record is a full spec
value with its own origin (the emitter says which short key becomes which value: a base reference, an authored literal
or a pinned text file), so provenance, `texts/` pinning and every emitter and validator rule apply to a haystack row
exactly as to a hand-written record. `role`, `manifest` and `note` are copied to every row.
"""
from __future__ import annotations

from ..core.values import SpecError

RECORD_KEYS = {"key", "kind", "role", "manifest", "note", "fields", "rows"}
MAX_ROWS = 999


def base_ref(service: str, collection: str, record, field: str) -> dict:
    return {"origin": "base", "construction": "reference",
            "base": {"service": service, "collection": collection, "record": record, "field": field}}


def literal(value) -> dict:
    return {"origin": "authored", "construction": "literal", "value": value}


def text_file(path, sha256) -> dict:
    return {"origin": "authored", "construction": "literal", "text": path, "sha256": sha256}


def expand(where: str, rec: dict, *, kind: str, shared_required: set, shared_optional: set, row_required: set,
           row_optional: set, build) -> list[dict]:
    """rec: the raw haystack record; build(row) -> {field: raw spec value} for one row. Returns raw records of `kind`."""
    if not isinstance(rec, dict):
        raise SpecError(where, "must be an object")
    unknown, missing = sorted(set(rec) - RECORD_KEYS), sorted({"key", "kind", "fields", "rows"} - set(rec))
    if unknown:
        raise SpecError(where, f"unknown keys {unknown}")
    if missing:
        raise SpecError(where, f"missing keys {missing} (a haystack needs key, kind, fields and rows)")
    key = rec["key"]
    if not isinstance(key, str) or not key:
        raise SpecError(f"{where}.key", "must be a non-empty string")
    shared = rec["fields"]
    if not isinstance(shared, dict):
        raise SpecError(f"{key}.fields", "must be an object")
    stray, lacking = sorted(set(shared) - shared_required - shared_optional), sorted(shared_required - set(shared))
    if stray:
        raise SpecError(f"{key}.fields", f"a {rec['kind']} shares only {sorted(shared_required | shared_optional)}; "
                                         f"not {stray}")
    if lacking:
        raise SpecError(f"{key}.fields", f"shared fields missing for {rec['kind']}: {lacking}")
    rows = rec["rows"]
    if not isinstance(rows, list) or not rows:
        raise SpecError(f"{key}.rows", "must be a non-empty list")
    if len(rows) > MAX_ROWS:
        raise SpecError(f"{key}.rows", f"{len(rows)} rows; one haystack holds at most {MAX_ROWS}")
    out = []
    for n, row in enumerate(rows, 1):
        at = f"{key}.rows[{n - 1}]"
        if not isinstance(row, dict):
            raise SpecError(at, "a row must be an object")
        stray, lacking = sorted(set(row) - row_required - row_optional), sorted(row_required - set(row))
        if stray:
            raise SpecError(at, f"unknown row keys {stray} (a row has {sorted(row_required | row_optional)})")
        if lacking:
            raise SpecError(at, f"row keys missing: {lacking}")
        for name, value in row.items():
            if not isinstance(value, str) or not value:
                raise SpecError(f"{at}.{name}", "must be a non-empty string")
        fields = dict(shared)
        fields.update(build(row))
        item = {"key": f"{key}.{n:03d}", "kind": kind, "fields": fields}
        for extra in ("role", "manifest", "note"):
            if extra in rec:
                item[extra] = rec[extra]
        out.append(item)
    return out
