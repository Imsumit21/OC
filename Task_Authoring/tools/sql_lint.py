#!/usr/bin/env python3
"""Static linter for a HarmonyGames injection SQL file (never executes anything).

Checks every INSERT / UPDATE / DELETE against references/universe_schema_live.json (the
platform DB export from setup/extract_schema.sql Q1) and
the fixed clock, so a long injection fails here instead of in Universe Explorer:

  errors   unknown table · unknown column · INSERT missing a NOT NULL column ·
           value count != column count · forbidden run-time functions (NOW(),
           CURRENT_TIMESTAMP, random(), gen_random_uuid(), uuid_generate_*) ·
           timestamp after the assigned V3 freeze in a created/sent/updated-type
           column · created_at > updated_at in one row · duplicate primary id within
           one table · line 1 is not the "-- Are you planning to inject? Yes|No" marker ·
           malformed JSON in any *_json column (and non-array values in array-shaped ones) ·
           service ID formats (Drive/Docs/Sheets/Slides f_/d_ + 22 hex, GCal evt_ + ical_uid
           32hex@hg4, GitHub <pr_id>#c_/rev_/rc_/ev_<n>, Trello timestamped ObjectIds, Gmail
           <mailbox>/<Message-ID> and RFC in_reply_to, Linear id = identifier = team key + number) ·
           Linear state/lifecycle (Done ⇔ completed_at, Canceled ⇔ canceled_at, started ≤ completed,
           created ≤ stamps ≤ updated) · Gmail copy vs From/To (own copy SENT; else owner a recipient),
           internal_date = date · GCal self:true only on the owner, start/end_json = start/end_ts ·
           Slack num_members = len(members_json) · Drive d_/f_ prefix vs mime type
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


# ---------- row rules (Check B literal JSON + per-row Check C coherence) ----------
# Every rule below holds for 100% (or ≥ 99.9%) of the base export rows it describes; the
# measured base rate is quoted in each message so a reviewer can see why it is a rule.

LIST_JSON = {"members_json", "label_ids_json", "to_json", "cc_json", "bcc_json", "parents_json",
             "shared_with_emails_json", "owners_json", "attendees_json", "idMembers_json", "idLabels_json",
             "reactions_json", "files_json", "attachments_json", "labels_json", "links_json", "relations_json",
             "assignee_logins_json", "requested_reviewer_logins_json", "member_logins_json"}
ID_SHAPES = {  # table -> (column, regex, base evidence)
    "gdrive.drive_files": ("id", r"[fd]_[0-9a-f]{22}", "53,866/53,866 base files are f_/d_ + 22 hex"),
    "gdocs.docs_documents": ("document_id", r"f_[0-9a-f]{22}", "Docs ids equal their drive_files id (f_ + 22 hex)"),
    "gsheets.sheets_spreadsheets": ("spreadsheet_id", r"f_[0-9a-f]{22}", "Sheets ids equal their drive_files id"),
    "gslides.slides_presentations": ("presentation_id", r"f_[0-9a-f]{22}", "Slides ids equal their drive_files id"),
    "gcal.gcal_events": ("event_id", r"evt_[0-9a-f]{22}", "11,233/11,233 base events are evt_ + 22 hex"),
    "trello.trello_cards": ("id", r"[0-9a-f]{24}", "all base Trello ids are 24-hex ObjectIds"),
    "trello.trello_actions": ("id", r"[0-9a-f]{24}", "all base Trello ids are 24-hex ObjectIds"),
    "trello.trello_checklists": ("id", r"[0-9a-f]{24}", "all base Trello ids are 24-hex ObjectIds"),
    "trello.trello_check_items": ("id", r"[0-9a-f]{24}", "all base Trello ids are 24-hex ObjectIds"),
    "trello.trello_lists": ("id", r"[0-9a-f]{24}", "all base Trello ids are 24-hex ObjectIds"),
}
GH_SUFFIX = {"github.github_pr_comments": "c", "github.github_reviews": "rev",
             "github.github_review_comments": "rc", "github.github_timeline_events": "ev"}
LIN_DONE, LIN_CANCEL = {"Done"}, {"Canceled", "Duplicate"}
LIN_UNSTARTED = {"Todo", "Backlog", "Triage"}
LIN_STARTED = {"In Progress", "PR", "In Validation", "Validation", "Regression"}
EMAIL = re.compile(r"[\w.+-]+@[\w.-]+\.\w+|[A-Z0-9_]+_EMAIL")


def emails_in(v) -> list[str]:
    return [e.lower() for e in EMAIL.findall(str(v or ""))]


def linear_lifecycle(r: dict) -> list[str]:
    """State/lifecycle rules for one Linear issue (base: 3,153 Done all with completed_at; 412
    Canceled/Duplicate all with canceled_at; no Todo/Backlog with started/completed/canceled;
    started ≤ completed, created ≤ every lifecycle stamp ≤ updated in 1 of 3,165 exceptions)."""
    out = []
    st = r.get("state_id")
    t = {k: parse_time(r.get(k)) for k in ("created_at", "started_at", "completed_at", "canceled_at", "updated_at")}
    if st in LIN_DONE and not t["completed_at"]:
        out.append(f"state {st} without completed_at (base: every Done issue has completed_at)")
    if t["completed_at"] and st not in LIN_DONE | {"In Review", None}:
        out.append(f"completed_at set but state is {st} (base: completed_at only on Done / In Review)")
    if st in LIN_CANCEL and not t["canceled_at"]:
        out.append(f"state {st} without canceled_at (base: every Canceled/Duplicate issue has canceled_at)")
    if t["canceled_at"] and st not in LIN_CANCEL | {None}:
        out.append(f"canceled_at set but state is {st}")
    if st in LIN_CANCEL and t["completed_at"]:
        out.append(f"state {st} but completed_at is set")
    if st in LIN_UNSTARTED and (t["started_at"] or t["completed_at"] or t["canceled_at"]):
        out.append(f"state {st} but started/completed/canceled stamps are set")
    if t["started_at"] and t["completed_at"] and t["started_at"] > t["completed_at"]:
        out.append("started_at is after completed_at")
    for k in ("started_at", "completed_at", "canceled_at"):
        if t[k] and t["created_at"] and t[k] < t["created_at"]:
            out.append(f"{k} predates created_at")
        if t[k] and t["updated_at"] and t[k] > t["updated_at"]:
            out.append(f"{k} is after updated_at")
    return out


def row_rules(table: str, row: dict, line: int, err, warn, cols_def: dict | None = None) -> None:
    """Literal-value rules for one INSERT row (row = column -> literal or None)."""
    for c, v in row.items():
        if v is None or not (c.endswith("_json")):
            continue
        try:
            parsed = json.loads(v)
        except ValueError as e:
            err(line, f"{table}.{c}: malformed JSON in a JSON column ({e.msg} at char {e.pos})")
            continue
        if c in LIST_JSON and parsed is not None and not isinstance(parsed, list):
            if parsed == {}:
                warn(line, f"{table}.{c}: '{{}}' where the base stores an array — use '[]'")
                continue
            err(line, f"{table}.{c}: must be a JSON array (base shape), got {type(parsed).__name__}")
    if table in ID_SHAPES:
        col, rx, ev = ID_SHAPES[table]
        if row.get(col) and not re.fullmatch(rx, row[col]):
            err(line, f"{table}.{col} {row[col]!r} breaks the service ID format ({ev})")
    if table in GH_SUFFIX and row.get("id") and row.get("pr_id"):
        if not re.fullmatch(re.escape(row["pr_id"]) + rf"#{GH_SUFFIX[table]}_\d+", row["id"]):
            err(line, f"{table}.id {row['id']!r} breaks the GitHub id scheme <pr_id>#{GH_SUFFIX[table]}_<n> (100% of base rows)")
    if table.startswith("trello.") and re.fullmatch(r"[0-9a-f]{24}", row.get("id") or ""):
        born = dt.datetime.fromtimestamp(int(row["id"][:8], 16), dt.timezone.utc)
        when = parse_time(row.get("date"))
        if after_clock(born) or born.year < 2011:
            err(line, f"{table}.id {row['id']} encodes creation {born:%Y-%m-%d} — Trello ids start with the record's Unix "
                      "seconds (100% of base cards/actions/lists/checklists); mint it from the record's own time")
        elif when and abs((when - born).total_seconds()) > 86400:
            warn(line, f"{table}.id {row['id']} encodes {born:%Y-%m-%d}, but date is {when:%Y-%m-%d} — mint the id from the record's time")
    if table == "linear.linear_issues":
        ident, iid = row.get("identifier"), row.get("id")
        if ident and iid and ident != iid:
            err(line, f"linear id {iid} differs from identifier {ident} (base: id = identifier)")
        m = re.fullmatch(r"([A-Z]+)-(\d+)", ident or iid or "")
        if m:
            if row.get("number") is not None and str(row["number"]) != m.group(2):
                err(line, f"linear number {row['number']} does not match identifier {ident or iid}")
            if row.get("team_id") and row["team_id"] != f"team_{m.group(1)}":
                err(line, f"linear team_id {row['team_id']} does not match identifier prefix {m.group(1)}")
        for msg in linear_lifecycle(row):
            err(line, f"{iid}: State/Lifecycle — {msg}")
    if table == "gmail.gmail_messages":
        ue, mid, tid = (row.get("user_email") or "").lower(), row.get("id") or "", row.get("thread_id") or ""
        if mid and not re.fullmatch(r"[^/]+/<[^<>]+@[^<>]+>", mid):
            err(line, f"gmail message id {mid!r} breaks the <mailbox>/<RFC Message-ID> scheme (104,476/104,480 base ids)")
        if tid and not re.fullmatch(r"[^/]+/\d{15,20}", tid):
            err(line, f"gmail thread id {tid!r} breaks the <mailbox>/<numeric thread id> scheme (100% of base threads)")
        for col in ("in_reply_to",):
            v = row.get(col)
            if v and not re.fullmatch(r"<[^<>]+@[^<>]+>", v.strip()):
                err(line, f"gmail {col} {v!r} is not an RFC Message-ID '<…@…>' (base threads link replies by Message-ID)")
        d, idt = parse_time(row.get("date")), row.get("internal_date")
        if d and idt and re.fullmatch(r"\d{12,14}", str(idt)) and abs(int(idt) / 1000 - d.timestamp()) > 1:
            err(line, f"gmail internal_date {idt} disagrees with date {row.get('date')}")
        frm = (emails_in(row.get("from_email")) or [""])[0]
        rcpts = emails_in(row.get("to_json")) + emails_in(row.get("cc_json")) + emails_in(row.get("bcc_json"))
        labels = row.get("label_ids_json") or ""
        if ue and frm == ue and "SENT" not in labels:
            err(line, f"gmail copy in {ue}'s own mailbox is from {ue} but not labelled SENT (base: 100% of own copies are SENT)")
        if ue and frm and frm != ue and ue not in rcpts:
            err(line, f"gmail copy in {ue}'s mailbox: {ue} is neither the sender ({frm}) nor in To/Cc/Bcc — mailbox copy "
                      "disagrees with the headers (name the list alias in To/Cc if it arrived through one)")
    if table == "gcal.gcal_events":
        uid = row.get("ical_uid")
        if uid and not re.fullmatch(r"[0-9a-f]{32}@hg4", uid):
            err(line, f"gcal ical_uid {uid!r} breaks the 32-hex@hg4 scheme (11,233/11,233 base events)")
        try:
            att = json.loads(row.get("attendees_json") or "[]")
        except ValueError:
            att = []
        cal = (row.get("calendar_id") or "").lower()
        if isinstance(att, list) and att:
            selfs = [a.get("email", "").lower() for a in att if isinstance(a, dict) and a.get("self")]
            if cal in [a.get("email", "").lower() for a in att if isinstance(a, dict)] and selfs != [cal]:
                err(line, f"gcal event on {cal}: the owner's attendee entry must be the only one with self:true (11,233/11,233 base)")
        for side in ("start", "end"):
            ts, js = parse_time(row.get(f"{side}_ts")), row.get(f"{side}_json")
            try:
                jt = parse_time((json.loads(js) or {}).get("dateTime")) if js else None
            except (ValueError, AttributeError):
                jt = None
            if ts and jt and ts != jt:
                err(line, f"gcal {side}_ts {row.get(f'{side}_ts')} disagrees with {side}_json dateTime")
    if table == "gdrive.drive_files" and row.get("id") and row.get("mime_type"):
        folder = row["mime_type"] == "application/vnd.google-apps.folder"
        if folder != row["id"].startswith("d_"):
            err(line, f"drive id {row['id']} prefix does not match mime_type {row['mime_type']} (folders d_, files f_)")
    if table == "slack.slack_channels" and row.get("members_json") and row.get("num_members"):
        try:
            if len(json.loads(row["members_json"])) != int(row["num_members"]):
                err(line, f"slack channel {row.get('id')}: num_members {row['num_members']} != len(members_json)")
        except (ValueError, TypeError):
            pass


def lint(sql: str, schema: dict) -> dict:
    from runtime_context import ensure_active
    ensure_active(globals())
    errors, warnings = [], []
    stats = {"statements": Counter(), "rows": Counter(), "ops": Counter()}
    seen_ids: dict[str, set] = defaultdict(set)
    first = sql.lstrip().splitlines()[0].strip() if sql.strip() else ""
    if not re.fullmatch(r"--\s*Are you planning to inject\?\s*(Yes|No)", first, re.I):
        errors.append({"line": 1, "msg": 'line 1 must be "-- Are you planning to inject? Yes" or "... No" '
                                         '(bundle/platform paste convention — not an /injection data finding)'})

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
            warn(line, f"{schema_name} statement — unscoped and rarely opened by agents: make sure another record points here"
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
                if val is not None and col.endswith("_json"):
                    row_rules(table, {col: val}, line, err, warn)
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
            row_rules(table, {c: literal(v) for c, v in row.items()}, line, err, warn)
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


def after_clock(when):
    return when > CLOCK if globals().get("TASK_CONTEXT") else when >= CLOCK


def check_time(table, col, lit, line, err, warn):
    t = parse_time(lit)
    if t is None:
        return
    if after_clock(t):
        if FUTURE_OK.search(col):
            warn(line, f"{table}.{col} = {lit} is on/after the clock — allowed only as a deadline or a not-yet-happened event")
        elif PAST_ONLY.search(col):
            relation = "after the assigned clock" if globals().get("TASK_CONTEXT") else "on/after the clock"
            err(line, f"{table}.{col} = {lit} is {relation} {CLOCK.isoformat()}")
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

    # row rules: each defect fires its rule; the matching valid row stays clean
    ol, br = "oliver.brooks@harmonygames.co", "brian.foster@harmonygames.co"
    att = '[{"email":"%s","self":true},{"email":"%s","organizer":true}]' % (ol, br)
    ok_rows = [
        ("gmail.gmail_messages", {"id": f"{ol}/<a@x.co>", "thread_id": f"{ol}/1890000000000000001", "user_email": ol,
                                  "label_ids_json": '["INBOX"]', "from_email": br, "to_json": f'["{ol}"]',
                                  "date": "2026-01-12T16:00:00Z", "internal_date": "1768233600000", "in_reply_to": "<z@x.co>"}),
        ("gmail.gmail_messages", {"id": f"{ol}/<b@x.co>", "thread_id": f"{ol}/1890000000000000001", "user_email": ol,
                                  "label_ids_json": '["SENT"]', "from_email": ol, "to_json": f'["Brian <{br}>"]'}),
        ("gcal.gcal_events", {"event_id": "evt_0a1b2c3d4e5f60718293a4", "calendar_id": ol, "attendees_json": att,
                              "ical_uid": "0f1e2d3c4b5a69788796a5b4c3d2e1f0@hg4", "start_ts": "2026-01-14T17:00:00Z",
                              "start_json": '{"dateTime":"2026-01-14T17:00:00Z"}'}),
        ("linear.linear_issues", {"id": "ENG-2990", "identifier": "ENG-2990", "number": "2990", "team_id": "team_ENG",
                                  "state_id": "Done", "created_at": "2026-01-01T00:00:00Z", "started_at": "2026-01-02T00:00:00Z",
                                  "completed_at": "2026-01-03T00:00:00Z", "updated_at": "2026-01-03T00:00:00Z", "labels_json": "[]"}),
        ("trello.trello_actions", {"id": "69651a80a1b2c3d4e5f6a7b8", "date": "2026-01-12T16:00:00Z", "data_json": '{"text":"x"}'}),
        ("github.github_pr_comments", {"id": "o/r#1#c_9", "pr_id": "o/r#1"}),
        ("gdrive.drive_files", {"id": "f_0a1b2c3d4e5f60718293a4", "mime_type": "application/vnd.google-apps.document",
                                "shared_with_emails_json": f'["{br}"]'}),
    ]
    bad_rows = [
        ("gmail.gmail_messages", {"user_email": ol, "label_ids_json": '["INBOX"]', "from_email": br, "to_json": '["x@y.co"]'}, "neither the sender"),
        ("gmail.gmail_messages", {"user_email": ol, "label_ids_json": '["INBOX"]', "from_email": ol, "to_json": f'["{br}"]'}, "not labelled SENT"),
        ("gmail.gmail_messages", {"id": f"{ol}/abc", "thread_id": f"{ol}/t1"}, "RFC Message-ID"),
        ("gmail.gmail_messages", {"in_reply_to": f"{ol}/abc"}, "is not an RFC Message-ID"),
        ("gmail.gmail_messages", {"date": "2026-01-12T16:00:00Z", "internal_date": "1768230000000"}, "internal_date"),
        ("gcal.gcal_events", {"ical_uid": "abc@hg4"}, "32-hex@hg4"),
        ("gcal.gcal_events", {"calendar_id": ol, "attendees_json": '[{"email":"%s"},{"email":"%s","self":true}]' % (ol, br)}, "self:true"),
        ("gcal.gcal_events", {"start_ts": "2026-01-14T17:00:00Z", "start_json": '{"dateTime":"2026-01-14T18:00:00Z"}'}, "disagrees with start_json"),
        ("gcal.gcal_events", {"attendees_json": '[{"email": "a"'}, "malformed JSON"),
        ("slack.slack_messages", {"reactions_json": '{"name":"x"}'}, "must be a JSON array"),
        ("linear.linear_issues", {"id": "ENG-1", "identifier": "ENG-1", "state_id": "Done"}, "without completed_at"),
        ("linear.linear_issues", {"id": "ENG-1", "state_id": "Todo", "started_at": "2026-01-02T00:00:00Z"}, "started/completed/canceled"),
        ("linear.linear_issues", {"id": "ENG-1", "state_id": "In Progress", "canceled_at": "2026-01-02T00:00:00Z"}, "canceled_at set"),
        ("linear.linear_issues", {"id": "ENG-1", "started_at": "2026-01-05T00:00:00Z", "completed_at": "2026-01-02T00:00:00Z",
                                  "state_id": "Done"}, "started_at is after completed_at"),
        ("linear.linear_issues", {"id": "iss_x", "identifier": "ENG-5"}, "differs from identifier"),
        ("trello.trello_actions", {"id": "9a1b2c3d4e5f6a7b8c9d0e1f"}, "Trello ids start with"),
        ("github.github_pr_comments", {"id": "o/r#1#c_x", "pr_id": "o/r#1"}, "GitHub id scheme"),
        ("gdrive.drive_files", {"id": "f_0a1b2c3d4e5f60718293a49"}, "service ID format"),
        ("gdrive.drive_files", {"id": "f_0a1b2c3d4e5f60718293a4", "mime_type": "application/vnd.google-apps.folder"}, "prefix does not match"),
        ("slack.slack_channels", {"id": "C1", "members_json": '["U1","U2"]', "num_members": "3"}, "num_members"),
    ]
    for t, row, *_ in ok_rows:
        e, w = [], []
        row_rules(t, row, 1, lambda l, m: e.append(m), lambda l, m: w.append(m))
        assert not e, (t, e)
    for t, row, needle in bad_rows:
        e = []
        row_rules(t, row, 1, lambda l, m: e.append(m), lambda l, m: None)
        assert any(needle in m for m in e), (t, needle, e)
    w = []
    row_rules("slack.slack_messages", {"reactions_json": "{}"}, 1, lambda l, m: None, lambda l, m: w.append(m))
    assert w and "use '[]'" in w[0], w
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
    from runtime_context import guarded_entry
    guarded_entry(globals())
    raise SystemExit(main(sys.argv[1:]))
