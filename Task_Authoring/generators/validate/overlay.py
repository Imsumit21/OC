"""Load a Linear base export as DB-shaped rows and apply restricted INSERT/UPDATE ops.

The Linear export (`Services_Data/linear/data.json`) keeps the API shape: JSON-valued
fields are Python lists, and `state_history_json` (a NOT NULL live column) is absent.
This module maps that export onto the live column names taken from
references/universe_schema_live.json and applies `core.ops.Op` records to a deep copy,
so validators can inspect the post-state without touching the read-only export.

Independence: nothing here imports tools/sql_lint.py, tools/base_check.py or any
generators/services module; the mapping and overlay rules are re-implemented from the
written sources.
"""
from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path

# --------------------------------------------------------------------------- constants

#: Tables addressed by SQL ops and their primary-key column tuples.
PK = {
    "linear.linear_issues": ("id",),
    "linear.linear_comments": ("id",),
    "linear.linear_projects": ("id",),
    "linear.linear_teams": ("id",),
    "linear.linear_users": ("id",),
}

#: Non-SQL helper table (memberships are only consulted by validators, never emitted).
MEMBERSHIP_TABLE = "linear.team_memberships"
MEMBERSHIP_KEY = ("team_id", "user_id", "id")

#: Columns that exist in the live database but cannot be reconstructed from the export.
#: The overlay stores them as None so a validator can tell "unknown" from "absent".
UNKNOWN_IN_EXPORT = {
    "linear.linear_issues": ("state_history_json",),
}

#: Live column sets from references/universe_schema_live.json, used to give an INSERT of
#: a row into an otherwise empty base table the same shape as a loaded row.
DEFAULT_COLUMNS = {
    "linear.linear_issues": (
        "id", "uuid", "project_id", "team_id", "parent_id", "assignee_id", "creator_id",
        "state_id", "cycle_id", "identifier", "number", "title", "description", "priority",
        "estimate", "due_date", "started_at", "completed_at", "canceled_at", "archived_at",
        "time_in_status_minutes", "labels_json", "links_json", "relations_json",
        "state_history_json", "is_archived", "created_at", "updated_at",
    ),
    "linear.linear_comments": (
        "id", "issue_id", "author_id", "parent_id", "body", "is_edited",
        "created_at", "updated_at", "sequence",
    ),
    "linear.linear_teams": (
        "id", "name", "key", "description", "is_archived", "created_at", "updated_at",
        "issue_counter",
    ),
    "linear.linear_users": (
        "id", "email", "name", "display_name", "avatar_url", "is_active", "is_admin",
        "is_guest", "created_at", "updated_at",
    ),
    "linear.linear_projects": (
        "id", "team_id", "name", "summary", "description", "lead_id", "priority", "state",
        "start_date", "target_date", "uuid", "icon", "color", "started_at", "completed_at",
        "canceled_at", "start_date_resolution", "target_date_resolution", "labels_json",
        "links_json", "is_archived", "created_at", "updated_at",
    ),
    MEMBERSHIP_TABLE: ("id", "team_id", "user_id", "created_at"),
}

#: Export field -> DB column, applied to issues (and to labels on projects).
_JSON_FIELDS = (("labels", "labels_json"), ("links", "links_json"), ("relations", "relations_json"))


def pk_columns(table: str) -> tuple[str, ...]:
    """Primary-key columns for `table` (helper table included)."""
    if table in PK:
        return PK[table]
    if table == MEMBERSHIP_TABLE:
        return MEMBERSHIP_KEY
    return ("id",)


# --------------------------------------------------------------------------- loading

def _json_text(value) -> str:
    return json.dumps(value, ensure_ascii=False)


def _issue_row(item: dict) -> dict:
    row = dict(item)
    for src, dst in _JSON_FIELDS:
        row[dst] = _json_text(row.pop(src, []))
    row["state_history_json"] = None          # unknown in the export (see UNKNOWN_IN_EXPORT)
    return row


def _project_row(item: dict) -> dict:
    row = dict(item)
    if "labels" in row:
        row["labels_json"] = _json_text(row.pop("labels"))
    return row


def load_linear_base(data_json: Path, expected_sha256: str | None = None) -> dict[str, dict[tuple, dict]]:
    """Load one universe's Linear export as DB-shaped rows keyed by primary key.

    `expected_sha256` is the hash of the *file* as recorded in the sibling
    source_manifest.json (files[] entry path "data.json"). A mismatch raises ValueError.
    """
    path = Path(data_json)
    raw = path.read_bytes()
    if expected_sha256 is not None:
        actual = hashlib.sha256(raw).hexdigest()
        if actual.lower() != expected_sha256.lower():
            raise ValueError(f"{path}: sha256 mismatch: expected {expected_sha256}, got {actual}")
    export = json.loads(raw.decode("utf-8"))

    base: dict[str, dict[tuple, dict]] = {
        "linear.linear_issues": {},
        "linear.linear_comments": {},
        "linear.linear_projects": {},
        "linear.linear_teams": {},
        "linear.linear_users": {},
        MEMBERSHIP_TABLE: {},
    }

    for item in export.get("issues") or ():
        row = _issue_row(item)
        base["linear.linear_issues"][(row["id"],)] = row
    for item in export.get("comments") or ():
        base["linear.linear_comments"][(item["id"],)] = dict(item)
    for item in export.get("projects") or ():
        row = _project_row(item)
        base["linear.linear_projects"][(row["id"],)] = row
    for item in export.get("teams") or ():
        base["linear.linear_teams"][(item["id"],)] = dict(item)
    for item in export.get("users") or ():
        base["linear.linear_users"][(item["id"],)] = dict(item)
    for item in export.get("team_memberships") or ():
        key = (item["team_id"], item["user_id"], item["id"])
        base[MEMBERSHIP_TABLE][key] = dict(item)

    return base


# --------------------------------------------------------------------------- overlay

@dataclass
class Overlay:
    """Post-op view of a base plus a record of what each op changed."""

    state: dict[str, dict[tuple, dict]]
    inserted: dict[str, list[tuple]] = field(default_factory=dict)
    updated: dict[str, list[tuple]] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    ops: list = field(default_factory=list)        # applied Op records, in order

    def touched(self, table: str) -> list[tuple]:
        """Keys inserted or updated in `table`, inserted first, deduplicated."""
        seen: set[tuple] = set()
        out: list[tuple] = []
        for key in list(self.inserted.get(table, ())) + list(self.updated.get(table, ())):
            if key not in seen:
                seen.add(key)
                out.append(key)
        return out

    def kind(self, table: str, key: tuple) -> str | None:
        """'insert', 'update' or None for a key in this overlay."""
        if key in set(self.inserted.get(table, ())):
            return "insert"
        if key in set(self.updated.get(table, ())):
            return "update"
        return None


def _insert_row(table: str, cols: tuple[tuple[str, object], ...], state: dict) -> dict:
    template = state.get(table) or {}
    columns: list[str] = list(DEFAULT_COLUMNS.get(table, ()))
    for row in template.values():
        for col in row:
            if col not in columns:
                columns.append(col)
    provided = dict(cols)
    for col in provided:
        if col not in columns:
            columns.append(col)
    row = {col: provided.get(col) for col in columns}
    return row


def apply(base: dict[str, dict[tuple, dict]], ops) -> Overlay:
    """Apply `ops` to a deep copy of `base`; never mutates `base`."""
    state = copy.deepcopy(base)
    overlay = Overlay(state=state)
    for table in state:
        overlay.inserted[table] = []
        overlay.updated[table] = []

    for op in ops:
        overlay.ops.append(op)
        table = op.table
        if table not in state:
            overlay.errors.append(f"{table}: unknown table for {op.op}")
            continue

        if op.op == "insert":
            row = _insert_row(table, op.cols, state)
            key_cols = pk_columns(table)
            if any(col not in row for col in key_cols):
                overlay.errors.append(f"{table}: INSERT is missing primary key columns {key_cols}")
                continue
            key = tuple(row[col] for col in key_cols)
            if key in state[table]:
                overlay.errors.append(f"{table}: INSERT of an existing key {key}")
                continue
            state[table][key] = row
            overlay.inserted[table].append(key)
        elif op.op == "update":
            where = dict(op.where)
            key_cols = pk_columns(table)
            if any(col not in where for col in key_cols):
                overlay.errors.append(f"{table}: UPDATE key is missing columns {key_cols}")
                continue
            key = tuple(where[col] for col in key_cols)
            if key not in state[table]:
                overlay.errors.append(f"{table}: UPDATE of a missing key {key}")
                continue
            row = state[table][key]
            for col, value in op.cols:
                row[col] = value
            overlay.updated[table].append(key)
        else:                                        # Op already rejects this
            overlay.errors.append(f"{table}: unknown op {op.op!r}")

    return overlay
