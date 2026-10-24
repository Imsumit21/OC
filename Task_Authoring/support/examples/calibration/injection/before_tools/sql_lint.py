#!/usr/bin/env python3
"""Static linter for a HarmonyGames injection SQL file (never executes anything).

Checks every INSERT / UPDATE / DELETE against references/universe_schema_live.json (the
platform DB export from setup/extract_schema.sql Q1) and
the fixed clock, so a long injection fails here instead of in Universe Explorer:

  errors   unknown table · unknown column · INSERT missing a NOT NULL column ·
           value count != column count · forbidden run-time functions (NOW(),
           CURRENT_TIMESTAMP, random(), gen_random_uuid(), uuid_generate_*) ·
           timestamp at/after 2026-02-14T00:00:00Z in a created/sent/updated-type
           column · created_at > updated_at in one row · duplicate primary id within
           one table · line 1 is not the "-- Are you planning to inject? Yes|No" marker
  warnings future timestamp in a due/start/end-type column (allowed for deadlines and
           scheduled events, but confirm) · business message on a weekend (UTC) ·
           Confluence/Snowflake statements (need a pointer from another record) · DELETE use

It also prints coverage stats (statements and rows per schema) that
tools/hardness_gate.py cross-checks against the hardness manifest.

Usage:
  python3 Task_Authoring/tools/sql_lint.py Task_Authoring/task_inputs/01_Universe_Inject.sql [--json]
  python3 Task_Authoring/tools/sql_lint.py --self-test
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

CLOCK = dt.datetime(2026, 2, 14, tzinfo=dt.timezone.utc)
SCHEMA_PATH = Path(__file__).resolve().parent.parent / "references" / "universe_schema_live.json"
# Re-export with setup/extract_schema.sql (Q1 → this file, Q2 → the constraints file) when the platform changes.
LIVE_SCHEMA = SCHEMA_PATH
LIVE_CONSTRAINTS = SCHEMA_PATH.parent / "universe_constraints_live.json"
FORBIDDEN = re.compile(r"\b(now\s*\(|current_timestamp|current_date|localtimestamp|random\s*\(|gen_random_uuid|uuid_generate_v\d|clock_timestamp)", re.I)
PAST_ONLY = re.compile(r"(^|_)(created|updated|sent|date|ts|time|timestamp|internal_date|submitted|merged|closed|completed|canceled|archived|edited|latest_reply|modified|added|posted|received|joined)($|_|at)", re.I)
FUTURE_OK = re.compile(r"(due|start|end|deadline|scheduled|post_at|expires|original_start|effective)", re.I)
MESSAGE_TABLES = {"slack.slack_messages", "gmail.gmail_messages", "linear.linear_comments",
                  "github.github_pr_comments", "github.github_review_comments", "trello.trello_actions",
                  "confluence.confluence_comments"}
ISO = re.compile(r"^(\d{4})-(\d{2})-(\d{2})(?:[T ](\d{2}):(\d{2})(?::(\d{2})(?:\.\d+)?)?)?(Z|[+-]\d{2}:?\d{2})?$")
EPOCH = re.compile(r"^\d{10}(\.\d{1,6})?$")


def load_schema(path: Path = SCHEMA_PATH) -> dict:
    tables = {}
    for t in json.loads(path.read_text()):
        tables[f"{t['table_schema']}.{t['table_name']}"] = {
            c["column"]: {"nullable": c["nullable"] == "YES", "default": c["default"], "type": c["type"],
                          # the export marks computed columns (generated = ALWAYS), e.g. slack_messages.text_fts
                          "generated": c.get("generated") == "ALWAYS" or (c.get("generated") is None and c["column"].endswith("_fts"))}
            for c in t["columns"]
        }
    return tables


# ---------- tokenising ----------

def split_statements(sql: str) -> list[tuple[int, str]]:
    """Split on semicolons outside quotes/comments; return (line_no, statement)."""
    out, buf, i, line, start_line = [], [], 0, 1, 1
    in_s = in_d = False
    while i < len(sql):
        ch = sql[i]
        nxt = sql[i + 1] if i + 1 < len(sql) else ""
        if not in_s and not in_d and ch == "-" and nxt == "-":
            j = sql.find("\n", i)
            j = len(sql) if j == -1 else j
            i = j
            continue
        if not in_s and not in_d and ch == "/" and nxt == "*":
            j = sql.find("*/", i + 2)
            j = len(sql) if j == -1 else j + 2
            line += sql[i:j].count("\n")
            i = j
            continue
        if not in_s and not in_d and ch == "$":
            dq = re.match(r"\$[A-Za-z_]*\$", sql[i:])
            if dq:
                tag = dq.group(0)
                j = sql.find(tag, i + len(tag))
                j = len(sql) if j == -1 else j + len(tag)
                buf.append(sql[i:j])
                line += sql[i:j].count("\n")
                i = j
                continue
        if ch == "\n":
            line += 1
        if ch == "'" and not in_d:
            if in_s and nxt == "'":
                buf.append("''")
                i += 2
                continue
            in_s = not in_s
        elif ch == '"' and not in_s:
            in_d = not in_d
        if ch == ";" and not in_s and not in_d:
            stmt = "".join(buf).strip()
            if stmt:
                out.append((start_line, stmt))
            buf, start_line = [], line
        else:
            if not buf and ch.isspace():
                start_line = line + (1 if ch == "\n" else 0) - (1 if ch == "\n" else 0)
            buf.append(ch)
        i += 1
    tail = "".join(buf).strip()
    if tail:
        out.append((start_line, tail))
    return out


def split_top(s: str, sep: str = ",") -> list[str]:
    parts, depth, buf, in_s, i = [], 0, [], False, 0
    while i < len(s):
        ch = s[i]
        if not in_s and ch == "$":
            dq = re.match(r"\$[A-Za-z_]*\$", s[i:])
            if dq:
                j = s.find(dq.group(0), i + len(dq.group(0)))
                j = len(s) if j == -1 else j + len(dq.group(0))
                buf.append(s[i:j])
                i = j
                continue
        if ch == "'":
            if in_s and i + 1 < len(s) and s[i + 1] == "'":
                buf.append("''")
                i += 2
                continue
            in_s = not in_s
        elif not in_s:
            if ch in "([":
                depth += 1
            elif ch in ")]":
                depth -= 1
            elif ch == sep and depth == 0:
                parts.append("".join(buf).strip())
                buf = []
                i += 1
                continue
        buf.append(ch)
        i += 1
    if "".join(buf).strip():
        parts.append("".join(buf).strip())
    return parts


def tuples_after_values(s: str) -> list[str]:
    tuples, depth, start, in_s, i = [], 0, None, False, 0
    while i < len(s):
        ch = s[i]
        if not in_s and ch == "$":
            dq = re.match(r"\$[A-Za-z_]*\$", s[i:])
            if dq:
                j = s.find(dq.group(0), i + len(dq.group(0)))
                i = len(s) if j == -1 else j + len(dq.group(0))
                continue
        if ch == "'":
            if in_s and i + 1 < len(s) and s[i + 1] == "'":
                i += 2
                continue
            in_s = not in_s
        elif not in_s:
            if ch == "(":
                if depth == 0:
                    start = i + 1
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0 and start is not None:
                    tuples.append(s[start:i])
                    start = None
            elif depth == 0 and s[i:i + 2].lower() == "on" and re.match(r"on\s+conflict", s[i:], re.I):
                break
        i += 1
    return tuples


def literal(v: str) -> str | None:
    v = v.strip()
    v = re.sub(r"::[a-z_ ]+(\[\])?$", "", v, flags=re.I).strip()
    dq = re.fullmatch(r"(\$[A-Za-z_]*\$)(.*)\1", v, re.S)
    if dq:
        return dq.group(2)
    if v[:2] in ("E'", "e'") and v.endswith("'"):
        v = v[1:]
    if len(v) >= 2 and v[0] == "'" and v[-1] == "'":
        return v[1:-1].replace("''", "'")
    if re.fullmatch(r"-?\d+(\.\d+)?", v):
        return v
    return None


def parse_time(raw: str | None) -> dt.datetime | None:
    if raw is None:
        return None
    raw = raw.strip()
    if EPOCH.match(raw):
        return dt.datetime.fromtimestamp(float(raw), tz=dt.timezone.utc)
    m = ISO.match(raw)
    if not m:
        return None
    y, mo, d, h, mi, s, tz = m.groups()
    t = dt.datetime(int(y), int(mo), int(d), int(h or 0), int(mi or 0), int(s or 0))
    if tz and tz != "Z":
        sign = 1 if tz[0] == "+" else -1
        hh, mm = int(tz[1:3]), int(tz[-2:])
        t = t - sign * dt.timedelta(hours=hh, minutes=mm)
    return t.replace(tzinfo=dt.timezone.utc)


# ---------- linting ----------

# Composite primary keys (used until universe_constraints_live.json — Q2 — supplies the declared ones).
PRIMARY_KEYS = {
    "gsheets.sheets_sheets": ("spreadsheet_id", "sheet_id"),
    "gdrive.drive_sheets": ("spreadsheet_id", "sheet_id"),
    "gslides.slides_pages": ("presentation_id", "object_id"),
    "gslides.slides_page_elements": ("presentation_id", "page_object_id", "object_id"),
    "gmail.gmail_label_user_counters": ("label_id", "user_email"),
    "github.github_commits": ("repo_id", "sha"),
    "github.github_commit_map": ("repo_id", "old_sha"),
}


def _live_primary_keys() -> None:
    """Replace the hand-kept composite-key map with declared PRIMARY KEY / UNIQUE constraints (Q2)."""
    if not LIVE_CONSTRAINTS.exists():
        return
    try:
        for c in json.loads(LIVE_CONSTRAINTS.read_text()):
            if c.get("kind") == "PRIMARY KEY" and c.get("columns"):
                PRIMARY_KEYS[f"{c['table_schema']}.{c['table_name']}"] = tuple(c["columns"])
    except (ValueError, KeyError, TypeError):
        pass


_live_primary_keys()


def lint(sql: str, schema: dict) -> dict:
    errors, warnings = [], []
    stats = {"statements": Counter(), "rows": Counter(), "ops": Counter()}
    seen_ids: dict[str, set] = defaultdict(set)
    first = sql.lstrip().splitlines()[0].strip() if sql.strip() else ""
    if not re.fullmatch(r"--\s*Are you planning to inject\?\s*(Yes|No)", first, re.I):
        errors.append({"line": 1, "msg": 'line 1 must be "-- Are you planning to inject? Yes" or "... No"'})

    def err(line, msg):
        errors.append({"line": line, "msg": msg})

    def warn(line, msg):
        warnings.append({"line": line, "msg": msg})

    for line, stmt in split_statements(sql):
        low = stmt.lower()
        if FORBIDDEN.search(re.sub(r"'(?:[^']|'')*'", "''", stmt)):
            err(line, "run-time function (NOW/CURRENT_TIMESTAMP/random/uuid) — use literal values so the SQL reproduces")
        m = re.match(r"insert\s+into\s+([a-z_0-9\"]+)\.([a-z_0-9\"]+)\s*\(([^)]*)\)\s*values\s*(.*)$", stmt, re.I | re.S)
        u = re.match(r"update\s+([a-z_0-9\"]+)\.([a-z_0-9\"]+)\s+set\s+(.*?)\s+where\s+(.*)$", stmt, re.I | re.S)
        d = re.match(r"delete\s+from\s+([a-z_0-9\"]+)\.([a-z_0-9\"]+)\s+where\s+(.*)$", stmt, re.I | re.S)
        if m:
            table = f"{m.group(1).strip(chr(34))}.{m.group(2).strip(chr(34))}".lower()
            cols = [c.strip().strip('"') for c in m.group(3).split(",")]
            stats["ops"]["insert"] += 1
        elif u:
            table = f"{u.group(1).strip(chr(34))}.{u.group(2).strip(chr(34))}".lower()
            stats["ops"]["update"] += 1
        elif d:
            table = f"{d.group(1).strip(chr(34))}.{d.group(2).strip(chr(34))}".lower()
            stats["ops"]["delete"] += 1
            warn(line, f"DELETE on {table} — prove nothing references the row and record it in the dossier")
        elif re.match(r"do\s+\$", low):
            warn(line, "DO block (procedural SQL) is not linted — prefer plain INSERT/UPDATE statements a reviewer can re-apply")
            continue
        else:
            if not low.startswith(("begin", "commit", "set ")):
                err(line, f"unsupported statement shape (use schema-qualified INSERT/UPDATE/DELETE): {stmt[:70]!r}")
            continue
        schema_name = table.split(".")[0]
        stats["statements"][schema_name] += 1
        if schema_name in ("confluence", "snowflake"):
            warn(line, f"{schema_name} statement — unscoped and not advertised to the agent: make sure another record points here"
                 + ("; keep mirrored warehouse tables in step" if schema_name == "snowflake" else ""))
        if table not in schema:
            err(line, f"unknown table {table} (not in {SCHEMA_PATH.name})")
            continue
        cols_def = schema[table]

        if u:
            for assign in split_top(u.group(3)):
                col = assign.split("=", 1)[0].strip().strip('"')
                if col not in cols_def:
                    err(line, f"{table}: unknown column {col}")
                    continue
                if cols_def[col].get("generated"):
                    err(line, f"{table}: UPDATE sets generated column {col} — the database computes it")
                val = literal(assign.split("=", 1)[1]) if "=" in assign else None
                check_time(table, col, val, line, err, warn)
            if not re.search(r"\b(id|event_id|identifier|thread_id|calendar_id|contact_id|spreadsheet_id|document_id|presentation_id)\b\s*=", u.group(4), re.I):
                warn(line, f"{table}: UPDATE predicate is not keyed on an id column")
            stats["rows"][schema_name] += 1
            continue
        if d:
            continue

        for c in cols:
            if c not in cols_def:
                err(line, f"{table}: unknown column {c}")
        missing = [c for c, meta in cols_def.items()
                   if not meta["nullable"] and meta["default"] is None and c not in cols and not meta.get("generated")]
        if missing:
            err(line, f"{table}: INSERT omits NOT NULL column(s) {missing}")
        gen = [c for c in cols if c in cols_def and cols_def[c].get("generated")]
        if gen:
            err(line, f"{table}: INSERT writes generated column(s) {gen} — the database computes them; drop them from the column list")
        for tup in tuples_after_values(m.group(4)):
            vals = split_top(tup)
            stats["rows"][schema_name] += 1
            if len(vals) != len(cols):
                err(line, f"{table}: {len(vals)} values for {len(cols)} columns")
                continue
            row = dict(zip(cols, vals))
            for c, v in row.items():
                lit = literal(v)
                if v.strip().upper() == "NULL" and c in cols_def and not cols_def[c]["nullable"]:
                    err(line, f"{table}: NULL in NOT NULL column {c}")
                check_time(table, c, lit, line, err, warn)
            key_cols = PRIMARY_KEYS.get(table) or next(
                ((k,) for k in ("id", "event_id", "contact_id", "document_id", "spreadsheet_id",
                               "presentation_id", "calendar_id", "sha", "login", "email_address")
                 if k in cols_def), ())
            if key_cols and all(k in row and literal(row[k]) is not None for k in key_cols):
                k = tuple(literal(row[c]) for c in key_cols)
                label = "/".join(key_cols)
                if k in seen_ids[table]:
                    err(line, f"{table}: duplicate {label} {k if len(k) > 1 else k[0]!r} inserted twice")
                seen_ids[table].add(k)
            c_at = parse_time(literal(row.get("created_at", "NULL")) if "created_at" in row else None)
            u_at = parse_time(literal(row.get("updated_at", "NULL")) if "updated_at" in row else None)
            if c_at and u_at and c_at > u_at:
                err(line, f"{table}: created_at {c_at.isoformat()} is after updated_at {u_at.isoformat()}")
    return {"errors": errors, "warnings": warnings,
            "stats": {"statements_by_schema": dict(stats["statements"]), "rows_by_schema": dict(stats["rows"]),
                      "ops": dict(stats["ops"]), "schemas_touched": sorted(stats["statements"]),
                      "total_rows": sum(stats["rows"].values())}}


def check_time(table, col, lit, line, err, warn):
    t = parse_time(lit)
    if t is None:
        return
    if t >= CLOCK:
        if FUTURE_OK.search(col):
            warn(line, f"{table}.{col} = {lit} is on/after the clock — allowed only as a deadline or a not-yet-happened event")
        elif PAST_ONLY.search(col):
            err(line, f"{table}.{col} = {lit} is on/after the clock 2026-02-14T00:00:00Z")
    elif table in MESSAGE_TABLES and PAST_ONLY.search(col) and t.weekday() >= 5 and col in ("ts", "created_at", "date"):
        warn(line, f"{table}.{col} = {lit} falls on a weekend (UTC) — business messages should be on weekdays")


def to_text(result: dict) -> str:
    s = result["stats"]
    lines = [f"schemas touched ({len(s['schemas_touched'])}): {', '.join(s['schemas_touched'])}",
             f"rows by schema: {s['rows_by_schema']}  total rows: {s['total_rows']}  ops: {s['ops']}",
             f"errors: {len(result['errors'])}  warnings: {len(result['warnings'])}"]
    lines += [f"  ERROR line {e['line']}: {e['msg']}" for e in result["errors"]]
    lines += [f"  warn  line {w['line']}: {w['msg']}" for w in result["warnings"]]
    return "\n".join(lines)


def _self_test() -> None:
    schema = load_schema()
    good = """-- Are you planning to inject? Yes
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, reply_count, reply_users_count, is_activity_message, reactions_json, files_json, attachments_json, created_at, metadata_json)
VALUES ('m1', '1770634800.000100', 'C1', 'message', 'U1', 'it''s fine', 0, 0, false, '[]', '[]', '[]', '2026-02-09T11:00:00Z', '{}'),
       ('m2', '1770638400.000100', 'C1', 'message', 'U2', 'ok; noted', 0, 0, false, '[]', '[]', '[]', '2026-02-09T12:00:00Z', '{}');
UPDATE linear.linear_issues SET description = 'x', updated_at = '2026-02-10T10:00:00Z' WHERE id = 'ENG-1';
"""
    r = lint(good, schema)
    assert not r["errors"], r["errors"]
    assert r["stats"]["rows_by_schema"] == {"slack": 2, "linear": 1}, r["stats"]
    bad = """INSERT INTO slack.slack_messages (id, ts, channel_id, type, text, bogus) VALUES ('m1', '1771200000.0', 'C1', 'message', 'x', 1);
INSERT INTO gcal.gcal_events (event_id, calendar_id, start_ts, created) VALUES ('e1', 'c', '2026-02-20T10:00:00Z', NOW());
INSERT INTO nope.t (a) VALUES (1);
INSERT INTO slack.slack_messages (id, ts, channel_id, type, text, reply_count, reply_users_count, is_activity_message, reactions_json, files_json, attachments_json, created_at, metadata_json, text_fts) VALUES ('m9', '1770634800.0009', 'C1', 'message', 'x', 0, 0, false, '[]', '[]', '[]', '2026-02-09T11:00:00Z', '{}', 'x');
"""
    r = lint(bad, schema)
    msgs = " | ".join(e["msg"] for e in r["errors"])
    for needle in ("line 1 must", "unknown column bogus", "omits NOT NULL", "on/after the clock", "run-time function", "unknown table nope.t", "generated column"):
        assert needle in msgs, (needle, msgs)
    assert any("deadline" in w["msg"] for w in r["warnings"])
    print("self-test: ok")


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        _self_test()
        return 0
    paths = [a for a in argv if not a.startswith("--")]
    if len(paths) != 1:
        print(__doc__, file=sys.stderr)
        return 2
    result = lint(Path(paths[0]).read_text(), load_schema())
    print(json.dumps(result, indent=2) if "--json" in argv else to_text(result))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
