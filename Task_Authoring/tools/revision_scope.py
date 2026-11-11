#!/usr/bin/env python3
"""revision_scope.py - what a SQL revision changed, and what has to be redone because of it (plan WS4.6, WS6.3-4).

A revision after a failed pre-check should be one relocation: one unit's deciding record moves to another carrier.
Nothing else is added. This tool compares two injection files as text (the SQL is never executed) and answers:

  diff --previous A.sql --current B.sql [--json]
      Records added, removed and changed, by service, table and record id. For each record it lists the neighbours:
      the same thread or parent, the same container, copies, and records whose text or foreign keys name it.
      A statement the parser cannot read is listed, not skipped. The summary gives the shape (no_change,
      companion_only, one_record, two_records, wider) and fits_one_relocation: one content record, or two that form
      one move (a source and a destination, not two added or two removed), with every statement read. Copies of one
      mail, one Drive file's rows (drive_files, the Docs/Sheets/Slides rows, every slide element) count as one record.
  scope --task-dir T --previous A.sql [--json]
      The record ids a scoped coherence sweep must re-read, and the dossier sections, files and tool checks this
      revision must redo (from playbooks/01_Universe_Injection.md and 01a_Hardening.md), as a checklist. Sections the
      revision does not touch are listed as not needed.
  relocation --task-dir T --previous A.sql [--unit U] [--previous-prompt P] [--previous-budget B] [--json]
      Check `revision.relocation`. Reads Working_Files/01_Difficulty_Budget.json. PASS when every added, removed or
      changed record is one unit's decider or an immediate companion of it (thread row, parent counters, mailbox
      copies, timeline event). WARN with the list otherwise: records that belong to no unit, more than one unit
      moved, prompt sentences added.
  --self-test

A record is one row of one table: all statements that touch it are merged, so reformatting the SQL, reordering
statements or folding an UPDATE into its INSERT is not a change. Record ids use the forms the other tools use:
Slack `C.../ts`, Gmail `mailbox/id`, `ENG-123`, `repo#12#c_3`, Drive `f_...`, `evt_...`.

Limits. Neighbours are found among the injected records; base records are only named (thread parent, issue, card).
A move is recognised by text similarity (MOVE_TEXT_RATIO), so a fully reworded move is reported as one record
removed and one added. Without a budget file the relocation check can only report the shape of the change.

Exit code: 0 PASS or WARN, 1 FAIL, 2 usage error. Stdlib only. Writes nothing.
"""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
WS = BUNDLE.parent
sys.path.insert(0, str(HERE))

TOOL = "revision_scope"
VERSION = 1
SQL_NAME = "01_Universe_Inject.sql"
PROMPT_NAME = "04_Prompt.txt"
BUDGET_NAME = "01_Difficulty_Budget.json"
MANIFEST_NAME = "01_Hardness_Manifest.json"
BUDGET_SCHEMA = "difficulty-budget-v1"

# Thresholds chosen here (not in references/first_pass_policy.json; listed in the hand-over report).
MOVE_TEXT_RATIO = 0.5       # removed text vs added text: at or above this the pair is reported as one move
RELOCATION_MAX_CONTENT = 2  # a relocation touches at most a source and a destination
NEIGHBOUR_PRINT_LIMIT = 12  # ids printed per relation in text output (the JSON holds all of them)

TRANSACTION_WORDS = {"begin", "commit", "start", "end", "set", "rollback"}
# Rows that exist only because another record does.
STRUCTURAL_TABLES = {"gmail.gmail_threads", "github.github_timeline_events", "gmail.gmail_label_user_counters"}
# Counter and bump columns the service recipes say to update when a child record is added (playbook 01, S4).
COMPANION_FIELDS = {"reply_count", "reply_users_count", "latest_reply", "thread_ts_legacy", "updated_at", "updated",
                    "modified_time", "datelastactivity", "badges_json", "snippet", "history_id", "size_estimate",
                    "num_members", "issue_counter", "version", "revision_id", "time_in_status_minutes"}
FK_COLS = ("thread_parent_id", "issue_id", "parent_id", "pr_id", "idCard", "idChecklist", "idBoard", "idList",
           "page_id", "drive_file_id", "in_reply_to_id", "spreadsheet_id", "presentation_id", "document_id",
           "page_object_id", "project_id", "thread_id", "pull_request_review_id", "space_id")
AUTHOR_COLS = ("user_id", "author_id", "author_login", "actor_login", "from_email", "idMemberCreator",
               "organizer_email", "creator_email", "creator_id", "owner_email", "lead_id")
DATE_COLS = ("date", "created_at", "submitted_at", "created", "created_time", "start_ts", "modified_time",
             "updated_at", "dateLastActivity")
TEXT_COLS = ("title", "name", "subject", "summary", "text", "body", "body_text", "description", "desc", "notes",
             "content_text", "first_name", "last_name", "job", "location", "message")
JSON_TEXT_COLS = ("grid_json", "table_json", "data_json", "attachments_json")
DRIVE_TABLES = {"gdrive.drive_files": "id", "gdocs.docs_documents": "document_id",
                "gsheets.sheets_spreadsheets": "spreadsheet_id", "gsheets.sheets_sheets": "spreadsheet_id",
                "gdrive.drive_sheets": "spreadsheet_id", "gslides.slides_presentations": "presentation_id",
                "gslides.slides_pages": "presentation_id", "gslides.slides_page_elements": "presentation_id"}
# Carriers the playbook treats as supporting detail until verified (hard gate 7): table -> columns.
SOFT_CARRIERS = {"gcal.gcal_events": ("description",), "gslides.slides_pages": ("notes",),
                 "contacts.contacts": ("description",), "gdrive.drive_files": ("content_text",)}
MIRROR_SERVICES = {"github": "INT-01 GitHub app copy in the Slack bot channel; INT-03 linear[bot] comment",
                   "gcal": "INT-11 invitation mails"}
SERVICE_RECIPES = {
    "slack": "id = sha256('<channel>|<ts>')[:32]; a thread reply needs the parent's reply_count, reply_users_count "
             "and latest_reply updated; membership changes update members_json and num_members together",
    "gmail": "one gmail_threads row and one message row per mailbox copy; the persona holds a copy in INBOX or SENT; "
             "a reply carries in_reply_to, references and a later date; internal_date equals date",
    "gcal": "one event row per attendee calendar with a shared ical_uid; decide whether invitation mails are seeded",
    "gdrive": "the same f_ id and identical sharing in drive_files and the Docs/Sheets/Slides row; bump modified_time "
              "on both rows",
    "github": "continue the per-PR suffixes; every PR comment needs its 'commented' timeline event; bump the PR's "
              "updated_at; a mirrored repo needs the Slack bot copy",
    "linear": "a comment is dated after the issue's created_at; bump the issue's updated_at to the newest comment; "
              "lifecycle stamps follow the state; a comment after the issue closed needs a disposition",
    "trello": "a comment is a commentCard action with the full data_json shape; update badges_json and "
              "dateLastActivity on the card and the board",
    "confluence": "UPDATE the page and INSERT version N+1; versions stay contiguous",
    "snowflake": "keep mirrored tables in step; update table comments that quote counts",
    "contacts": "keep the record sparse like the base; last_name is NOT NULL",
}
for _alias in ("gdocs", "gsheets", "gslides"):
    SERVICE_RECIPES[_alias] = SERVICE_RECIPES["gdrive"]


class UsageError(Exception):
    """A missing or unreadable input: exit code 2."""


# ---------------------------------------------------------------- small helpers

def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _read(path, what: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise UsageError(f"cannot read {what} {path}: {exc}") from exc


def _rel(path) -> str:
    """A stable name for a file: relative to the workspace when it is inside it."""
    p = Path(path).resolve()
    try:
        return p.relative_to(WS.resolve()).as_posix()
    except ValueError:
        return p.as_posix()


def _parsers():
    """The SQL tokenisers of sql_lint.py and the statement parser of base_check.py (imported on first use)."""
    import base_check
    import sql_lint
    return sql_lint, base_check


def _slot(task_dir, name) -> Path:
    from stage_gate import slot_path
    return slot_path(task_dir, name)


def _norm_text(text) -> str:
    return " ".join(str(text or "").split()).casefold()


def _json_value(raw):
    if raw in (None, ""):
        return None
    try:
        return json.loads(raw)
    except (TypeError, ValueError):
        return None


def _first(mapping: dict, names):
    low = {k.lower(): v for k, v in mapping.items()}
    for name in names:
        value = low.get(name.lower())
        if value not in (None, ""):
            return value
    return None


_ESCAPE_RX = re.compile(r"\\([nrt\\'])")
_ESCAPES = {"n": "\n", "r": "", "t": "\t", "\\": "\\", "'": "'"}


def unescape(text: str) -> str:
    """Backslash escapes of an E'...' SQL string as the characters they stand for (the parser keeps them raw)."""
    return _ESCAPE_RX.sub(lambda m: _ESCAPES[m.group(1)], str(text))


def _slack_iso(ts) -> str | None:
    try:
        return dt.datetime.fromtimestamp(float(ts), tz=dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except (TypeError, ValueError, OverflowError, OSError):
        return None


def json_text(column: str, raw) -> str:
    """Readable text of a JSON column that carries content (sheet cells, Trello comment, Slack attachment)."""
    data = _json_value(raw)
    if data is None:
        return str(raw or "")
    if column in ("grid_json", "table_json") and isinstance(data, list):
        rows = []
        for row in data:
            if isinstance(row, list):
                rows.append(" | ".join("" if c is None else str(c.get("text", c) if isinstance(c, dict) else c)
                                       for c in row))
            else:
                rows.append(json.dumps(row, ensure_ascii=False, sort_keys=True))
        return "\n".join(rows)
    if column == "data_json" and isinstance(data, dict):
        parts = [str(data[k]) for k in ("text", "desc", "name") if isinstance(data.get(k), str) and data[k]]
        for key in ("card", "list", "listBefore", "listAfter", "checklist", "checkItem", "old"):
            sub = data.get(key)
            if isinstance(sub, dict):
                label = ", ".join(f"{k}={sub[k]}" for k in ("name", "idShort", "state", "desc", "closed", "due")
                                  if sub.get(k) not in (None, ""))
                if label:
                    parts.append(f"{key}: {label}")
        return "\n".join(parts)
    if column == "attachments_json" and isinstance(data, list):
        parts = []
        for att in data:
            if isinstance(att, dict):
                parts += [str(att[k]) for k in ("pretext", "title", "text", "fallback")
                          if isinstance(att.get(k), str) and att[k]]
        return "\n".join(parts)
    return json.dumps(data, ensure_ascii=False, sort_keys=True)


# ---------------------------------------------------------------- statements -> records

def parse_statements(sql: str) -> tuple:
    """(statements, unparsed). Each statement is a base_check.parse_sql dict with the file's line number.
    `unparsed` lists every statement the parser returned nothing for (or fewer rows than VALUES tuples)."""
    sql_lint, base_check = _parsers()
    statements, unparsed = [], []
    for line, stmt in sql_lint.split_statements(sql):
        words = stmt.split(None, 1)
        if not words or words[0].lower().rstrip(";") in TRANSACTION_WORDS:
            continue
        rows = base_check.parse_sql(stmt + ";")
        expected = 1
        m = re.match(r"insert\s+into\s+[^()]+\(([^)]*)\)\s*values\s*(.*)$", stmt, re.I | re.S)
        if m:
            body = re.split(r"\bon\s+conflict\b", m.group(2), flags=re.I)[0]
            expected = max(1, len(sql_lint.tuples_after_values(body)))
        if len(rows) < expected:
            unparsed.append({"line": line, "head": " ".join(stmt.split())[:100],
                             "sha256": sha256_text(" ".join(stmt.split()))})
        for row in rows:
            row["line"] = line
            statements.append(row)
    return statements, unparsed


def _pk_columns(table: str, available) -> tuple:
    sql_lint, _ = _parsers()
    names = {str(a).lower(): a for a in available}
    pk = sql_lint.PRIMARY_KEYS.get(table)
    if pk and all(c.lower() in names for c in pk):
        return tuple(names[c.lower()] for c in pk)
    return (names["id"],) if "id" in names else ()


def _record_id(table: str, values: dict) -> str | None:
    cols = _pk_columns(table, values)
    if not cols or any(values.get(c) in (None, "") for c in cols):
        return None
    return "/".join(str(values[c]) for c in cols)


def load_records(sql: str) -> dict:
    """{"records": {key: record}, "unparsed": [...], "statements": n}. key = "<table>:<record id>".

    A record merges every statement on one row: `fields` is the final value of each column the SQL writes."""
    statements, unparsed = parse_statements(sql)
    # Slack: an UPDATE names the 32-hex row id; map it back to channel/ts where the SQL shows it.
    sha_to_slack = {}
    for s in statements:
        if s["table"] == "slack.slack_messages" and s["op"] == "insert":
            row = s["row"]
            if row.get("channel_id") and row.get("ts"):
                if row.get("id"):
                    sha_to_slack[row["id"]] = f"{row['channel_id']}/{row['ts']}"
                parent, parent_ts = row.get("thread_parent_id"), row.get("thread_ts_legacy")
                if parent and parent_ts and parent_ts != row["ts"]:
                    sha_to_slack.setdefault(parent, f"{row['channel_id']}/{parent_ts}")
    records = {}
    for s in statements:
        table, op = s["table"], s["op"]
        values = s["row"] if op == "insert" else s["where"]
        aliases = []
        if table == "slack.slack_messages":
            raw = values.get("id")
            if op == "insert" and values.get("channel_id") and values.get("ts"):
                rid = f"{values['channel_id']}/{values['ts']}"
            else:
                rid = sha_to_slack.get(raw) or raw
            if raw and raw != rid:
                aliases.append(raw)
        else:
            rid = _record_id(table, values)
        if rid is None:
            rid = "?" + sha256_text(json.dumps([op, values], sort_keys=True, ensure_ascii=False))[:16]
        key = f"{table}:{rid}"
        rec = records.setdefault(key, {"key": key, "id": rid, "table": table, "service": table.split(".")[0],
                                       "ops": [], "lines": [], "fields": {}, "aliases": [], "deleted": False})
        if op not in rec["ops"]:
            rec["ops"].append(op)
        rec["lines"].append(s["line"])
        for alias in aliases:
            if alias not in rec["aliases"]:
                rec["aliases"].append(alias)
        if op == "insert":
            rec["fields"].update(s["row"])
        elif op == "update":
            rec["fields"].update(s["set"])
        else:
            rec["deleted"] = True
    for rec in records.values():
        _derive(rec, sha_to_slack)
    _link_children(records)
    return {"records": records, "unparsed": unparsed, "statements": len(statements)}


def _derive(rec: dict, sha_to_slack: dict) -> None:
    """Container, thread, parent, author, date, text, references and the fingerprint of one record."""
    _, base_check = _parsers()
    f, table, rid = rec["fields"], rec["table"], rec["id"]
    container = thread = parent = copy = None
    if table == "slack.slack_messages":
        channel = f.get("channel_id") or (rid.split("/")[0] if "/" in rid else None)
        container = channel
        thread_ts = f.get("thread_ts_legacy")
        own_ts = f.get("ts") or (rid.split("/")[1] if "/" in rid else None)
        if channel and thread_ts and thread_ts != own_ts:
            thread = parent = f"{channel}/{thread_ts}"
        else:
            thread = rid
    elif table == "gmail.gmail_messages":
        container = f.get("user_email") or rid.split("/")[0]
        thread = f.get("thread_id")
        copy = "gmail:" + (rid.split("/", 1)[1] if "/" in rid else rid)
        if f.get("in_reply_to"):
            parent = f"{container}/{f['in_reply_to']}"
    elif table == "gmail.gmail_threads":
        container = f.get("user_email") or rid.split("/")[0]
        thread = rid
    elif table == "linear.linear_comments":
        container = thread = f.get("issue_id")
        parent = f.get("parent_id") or f.get("issue_id")
    elif table == "linear.linear_issues":
        container = f.get("project_id") or f.get("team_id")      # unknown for an UPDATE of a base issue
        thread = rid
        parent = f.get("parent_id")
    elif table.startswith("github.") and (f.get("pr_id") or "#" in rid):
        pr = f.get("pr_id") or "#".join(rid.split("#")[:2])
        if table == "github.github_pull_requests":
            container, thread = rid.split("#")[0], rid
        else:
            container = thread = pr
            parent = f.get("in_reply_to_id") or pr
    elif table == "trello.trello_actions":
        container = thread = parent = _first(f, ("idCard",))
    elif table == "trello.trello_cards":
        container = _first(f, ("idList", "idBoard"))
        thread = rid
    elif table == "trello.trello_checklists":
        container = thread = parent = _first(f, ("idCard",))
    elif table == "trello.trello_check_items":
        container = thread = parent = _first(f, ("idChecklist",))
    elif table == "gcal.gcal_events":
        container = f.get("calendar_id")
        thread = f.get("ical_uid") or rid
        if f.get("ical_uid"):
            copy = "gcal:" + f["ical_uid"]
    elif table in DRIVE_TABLES:
        file_id = f.get(DRIVE_TABLES[table]) or rid.split("/")[0]
        thread = file_id
        copy = "file:" + str(file_id)
        if table == "gdrive.drive_files":
            parents = _json_value(f.get("parents_json"))
            container = parents[0] if isinstance(parents, list) and parents else None
        else:
            container = file_id
    elif table.startswith("confluence."):
        container = _first(f, ("page_id", "space_id", "space_key")) or table.split(".")[1]
        thread = _first(f, ("page_id",)) or rid
        parent = _first(f, ("parent_id", "page_id"))
    else:
        container = table.split(".")[1]
    author = _first(f, AUTHOR_COLS)
    date = _slack_iso(f.get("ts")) if table == "slack.slack_messages" and f.get("ts") else _first(f, DATE_COLS)
    parts = [unescape(f[c]) for c in f if c.lower() in TEXT_COLS and f[c] not in (None, "")]
    parts += [unescape(json_text(c, f[c])) for c in f if c in JSON_TEXT_COLS and f[c] not in (None, "", "[]", "{}")]
    text = "\n".join(p for p in parts if p)
    own = {rid, *rec["aliases"]}
    refs = set()
    for col in f:
        value = f[col]
        if value in (None, ""):
            continue
        if col in FK_COLS:
            refs.add(sha_to_slack.get(value, str(value)))
        if col.lower() in TEXT_COLS or col in JSON_TEXT_COLS or col in ("links_json", "relations_json"):
            refs |= base_check.id_tokens(value)
    if table == "gmail.gmail_messages" and parent:
        refs.add(parent)
    for extra in (thread, parent):
        if extra:
            refs.add(str(extra))
    structural = table in STRUCTURAL_TABLES
    update_only = rec["ops"] == ["update"]
    rec.update({
        "container": container, "thread": thread, "parent": parent, "author": author, "date": date, "text": text,
        "copy": copy, "refs": sorted(r for r in refs if r not in own),
        "logical": copy or rec["key"],
        "structural": structural,
        "companion_only": structural or (update_only and bool(f) and
                                         all(c.lower() in COMPANION_FIELDS for c in f)),
        # the final state of the row, not the statements that reach it: an UPDATE folded into its INSERT is no change
        "fingerprint": sha256_text(json.dumps({"inserted": "insert" in rec["ops"], "deleted": rec["deleted"],
                                               "fields": {k: f[k] for k in sorted(f)}},
                                              sort_keys=True, ensure_ascii=False)),
    })


def _link_children(records: dict) -> None:
    """Trello check items hang off a checklist; when the checklist is in the SQL, thread them to its card."""
    lists = {r["id"]: r for r in records.values() if r["table"] == "trello.trello_checklists"}
    for rec in records.values():
        if rec["table"] == "trello.trello_check_items" and rec["parent"] in lists and lists[rec["parent"]]["thread"]:
            rec["thread"] = lists[rec["parent"]]["thread"]
            rec["container"] = rec["parent"]


def id_index(records: dict) -> dict:
    """record id or alias -> [record keys] (a Drive file id names both its drive_files row and its Docs row)."""
    index = {}
    for key in sorted(records):
        rec = records[key]
        for rid in (rec["id"], *rec["aliases"]):
            index.setdefault(rid, []).append(key)
    return index


def record_summary(rec: dict) -> dict:
    return {"id": rec["id"], "table": rec["table"], "service": rec["service"], "ops": list(rec["ops"]),
            "container": rec["container"], "thread": rec["thread"], "author": rec["author"], "date": rec["date"],
            "aliases": list(rec["aliases"]), "line": min(rec["lines"]) if rec["lines"] else None,
            "text": " ".join(rec["text"].split())[:160]}


# ---------------------------------------------------------------- neighbours

def neighbours(target: dict, records: dict, index: dict | None = None) -> dict:
    """Records in `records` related to `target`, by relation, and the related ids the SQL does not hold (base).

    copy       the same message or file in another mailbox, calendar or table
    thread     the same thread, the parent, or a child
    container  the same channel, mailbox, issue, PR, card, calendar or file
    reference  its text or a foreign key names the target, or the target names it
    base       thread, parent and referenced ids with no record in the SQL"""
    index = index if index is not None else id_index(records)
    own = {target["id"], *target["aliases"]}
    out = {"copy": set(), "thread": set(), "container": set(), "reference": set()}
    for key, rec in records.items():
        if key == target["key"]:
            continue
        ids = {rec["id"], *rec["aliases"]}
        if target.get("copy") and rec.get("copy") == target["copy"]:
            out["copy"].add(key)
        elif (target["thread"] and rec["thread"] == target["thread"]) or (rec["parent"] and rec["parent"] in own) \
                or (target["parent"] and target["parent"] in ids):
            out["thread"].add(key)
        elif own & set(rec["refs"]) or ids & set(target["refs"]):
            out["reference"].add(key)
        elif target["container"] and rec["service"] == target["service"] and rec["container"] == target["container"]:
            out["container"].add(key)
    base = set()
    for rid in (target["thread"], target["parent"], *target["refs"]):
        if rid and rid not in index and rid not in own:
            base.add(str(rid))
    result = {rel: sorted(keys) for rel, keys in out.items()}
    result["base"] = sorted(base)
    return result


# ---------------------------------------------------------------- diff

def _changed_fields(before: dict, after: dict) -> list:
    keys = set(before["fields"]) | set(after["fields"])
    return sorted(k for k in keys if before["fields"].get(k) != after["fields"].get(k))


def _kind(state: str, rec: dict, fields: list) -> str:
    """content: the record's words or state changed. companion: only counters, bumps or a structural row."""
    if rec["structural"]:
        return "companion"
    if state == "changed":
        return "companion" if fields and all(f.lower() in COMPANION_FIELDS for f in fields) else "content"
    return "companion" if rec["companion_only"] else "content"


def diff_records(previous: dict, current: dict) -> dict:
    """Compare two load_records() results. Returns entries (one per changed record) and a summary."""
    prev, cur = previous["records"], current["records"]
    cur_index = id_index(cur)
    entries = []
    for key in sorted(set(prev) | set(cur)):
        before, after = prev.get(key), cur.get(key)
        if before and after and before["fingerprint"] == after["fingerprint"]:
            continue
        state = "changed" if before and after else ("added" if after else "removed")
        rec = after or before
        fields = _changed_fields(before, after) if state == "changed" else sorted(rec["fields"])
        entry = {"state": state, "kind": _kind(state, rec, fields), "key": key, **record_summary(rec),
                 "changed_fields": fields if state == "changed" else [], "logical": rec["logical"],
                 "neighbours": neighbours(rec, cur, cur_index)}
        if state == "changed":
            entry["previous_text"] = " ".join(before["text"].split())[:160]
        entries.append(entry)
    prev_un = {u["sha256"]: u for u in previous["unparsed"]}
    cur_un = {u["sha256"]: u for u in current["unparsed"]}
    unparsed = [{"state": "added", **cur_un[h]} for h in sorted(set(cur_un) - set(prev_un))] + \
               [{"state": "removed", **prev_un[h]} for h in sorted(set(prev_un) - set(cur_un))]
    logical = {}
    for e in entries:
        group = logical.setdefault(e["logical"], {"logical": e["logical"], "kind": "companion", "states": set(),
                                                  "keys": [], "ids": set(), "service": e["service"]})
        group["keys"].append(e["key"])
        group["states"].add(e["state"])
        group["ids"].update([e["id"], *e["aliases"]])
        if e["kind"] == "content":
            group["kind"] = "content"
    groups = []
    for name in sorted(logical):
        g = logical[name]
        groups.append({"logical": name, "kind": g["kind"], "states": sorted(g["states"]), "keys": g["keys"],
                       "ids": sorted(g["ids"]), "service": g["service"]})
    content = [g for g in groups if g["kind"] == "content"]
    moves = _moves(entries, prev, cur)
    n = len(content)
    # one source and one destination: two new records, or two dropped ones, are not a move
    content_states = sorted("+".join(g["states"]) for g in content)
    one_move = n == 1 or (n == 2 and content_states not in (["added", "added"], ["removed", "removed"]))
    if not entries and not unparsed:
        shape = "no_change"
    elif n == 0:
        shape = "companion_only"
    elif n == 1:
        shape = "one_record"
    elif n == 2:
        shape = "two_records"
    else:
        shape = "wider"
    summary = {
        "added": sum(1 for e in entries if e["state"] == "added"),
        "removed": sum(1 for e in entries if e["state"] == "removed"),
        "changed": sum(1 for e in entries if e["state"] == "changed"),
        "content_records": n, "companion_records": len(groups) - n,
        "services": sorted({e["service"] for e in entries}),
        "content_services": sorted({g["service"] for g in content}),
        "shape": shape, "content_states": content_states,
        "fits_one_relocation": 1 <= n <= RELOCATION_MAX_CONTENT and one_move and not unparsed,
        "moves": moves, "unparsed_changed": len(unparsed),
        "statements": {"previous": previous["statements"], "current": current["statements"]},
    }
    return {"entries": entries, "groups": groups, "unparsed": unparsed, "summary": summary}


def _moves(entries: list, prev: dict, cur: dict) -> list:
    """Removed content record -> added content record with similar text: the record was moved, not rewritten."""
    removed = [e for e in entries if e["state"] == "removed" and e["kind"] == "content" and prev[e["key"]]["text"]]
    added = [e for e in entries if e["state"] == "added" and e["kind"] == "content" and cur[e["key"]]["text"]]
    pairs = []
    for r in removed:
        a_text = _norm_text(prev[r["key"]]["text"])
        best = None
        for a in added:
            ratio = difflib.SequenceMatcher(None, a_text, _norm_text(cur[a["key"]]["text"]), autojunk=False).ratio()
            if ratio >= MOVE_TEXT_RATIO and (best is None or ratio > best[0]):
                best = (ratio, a)
        if best:
            pairs.append({"from": r["id"], "from_key": r["key"], "to": best[1]["id"], "to_key": best[1]["key"],
                          "ratio": round(best[0], 3),
                          "same_container": r["container"] == best[1]["container"] and r["service"] == best[1]["service"]})
    return pairs


def diff_files(previous_path, current_path) -> dict:
    previous = load_records(_read(previous_path, "the previous SQL"))
    current = load_records(_read(current_path, "the current SQL"))
    result = diff_records(previous, current)
    result["_previous"], result["_current"] = previous, current
    result["bound_to"] = {_rel(previous_path): sha256_file(previous_path), _rel(current_path): sha256_file(current_path)}
    return result


# ---------------------------------------------------------------- scope: re-read list and checklist

def reread_ids(diff: dict) -> dict:
    """What a scoped coherence sweep reads again: changed records, their neighbours, and the base ids they hang on."""
    cur = diff["_current"]["records"]
    changed, removed, neighbour, base = {}, {}, {}, set()
    for e in diff["entries"]:
        target = removed if e["state"] == "removed" else changed
        target[e["key"]] = {"id": e["id"], "table": e["table"], "state": e["state"], "kind": e["kind"]}
        for relation in ("copy", "thread", "reference", "container"):
            for key in e["neighbours"][relation]:
                slot = neighbour.setdefault(key, {"id": cur[key]["id"], "table": cur[key]["table"], "because": []})
                note = f"{relation} of {e['id']}"
                if note not in slot["because"]:
                    slot["because"].append(note)
        base.update(e["neighbours"]["base"])
    for key in changed:
        neighbour.pop(key, None)
    known = {v["id"] for v in changed.values()} | {v["id"] for v in neighbour.values()}
    return {"changed": [changed[k] for k in sorted(changed)], "removed": [removed[k] for k in sorted(removed)],
            "neighbours": [neighbour[k] for k in sorted(neighbour)], "base": sorted(base - known)}


def scope_ids(diff: dict) -> set:
    """Every id (and alias) of a changed record or a neighbour: the scope of a revision coherence sweep."""
    cur = diff["_current"]["records"]
    keys = set()
    for e in diff["entries"]:
        keys.add(e["key"])
        for relation in ("copy", "thread", "reference", "container"):
            keys.update(e["neighbours"][relation])
    ids = set()
    for key in keys:
        rec = cur.get(key) or diff["_previous"]["records"].get(key)
        if rec:
            ids.update([rec["id"], *rec["aliases"]])
    for e in diff["entries"]:
        ids.update(e["neighbours"]["base"])
    return ids


def _manifest(task_dir):
    for name in (MANIFEST_NAME, "01_Hardness_Manifest.draft.json"):
        path = _slot(task_dir, name)
        if path.is_file():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                return None, path
            return (data if isinstance(data, dict) else None), path
    return None, None


def build_checklist(diff: dict, task_dir=None) -> list:
    """The sections, files and tool checks this revision must redo. Each item: id, kind, title, source, redo, why.

    The mapping follows playbooks/01_Universe_Injection.md (S1-S7, hard gates) and 01a_Hardening.md gate 7
    ("Every SQL change re-passes 01")."""
    prev, cur = diff["_previous"]["records"], diff["_current"]["records"]
    entries = diff["entries"]
    content = [e for e in entries if e["kind"] == "content"]
    live = [e for e in content if e["state"] != "removed"]
    added_inserts = [e for e in entries if e["state"] == "added" and "insert" in e["ops"]]
    ids_of = lambda items: ", ".join(sorted({e["id"] for e in items})[:8]) + (" ..." if len({e["id"] for e in items}) > 8 else "")  # noqa: E731
    prev_tables = {r["table"] for r in prev.values()}
    new_tables = sorted({e["table"] for e in entries if e["state"] != "removed"} - prev_tables)
    prev_authors = {r["author"] for r in prev.values() if r["author"]}
    new_speakers = sorted({cur[e["key"]]["author"] for e in live if cur[e["key"]]["author"]} - prev_authors)
    services = sorted({e["service"] for e in entries})
    soft = [e for e in live if any(c in (e["changed_fields"] or cur[e["key"]]["fields"])
                                   for c in SOFT_CARRIERS.get(e["table"], ()))]
    branchy = [e for e in live if re.search(r"\brelease/[\w.-]+|\b[a-z]+_fix_\d+\b", cur[e["key"]]["text"])]
    touched = set()
    for e in entries:
        touched.update([e["id"], *e["aliases"]])
    manifest, manifest_path = _manifest(task_dir) if task_dir else (None, None)
    fact_keys, manifest_hits, anchor_hits = [], [], []
    if manifest:
        for fact in manifest.get("facts") or []:
            homes = set(fact.get("home_ids") or []) | set(fact.get("must_appear_in") or [])
            if homes & touched:
                fact_keys.append(str(fact.get("key")))
        blob = json.dumps(manifest, ensure_ascii=False)
        manifest_hits = sorted(t for t in touched if t and t in blob)
        for anchor in manifest.get("anchors") or []:
            if {anchor.get("locator"), *(anchor.get("seeded_ids") or [])} & touched:
                anchor_hits.append(str(anchor.get("id")))
    task = _rel(task_dir) if task_dir else "<task_dir>"
    P1, P1A = "01_Universe_Injection.md", "01a_Hardening.md"
    items = []

    def add(item_id, kind, title, source, redo, why):
        items.append({"id": item_id, "kind": kind, "title": title, "source": source, "redo": bool(redo), "why": why})

    add("dossier.1A", "dossier", "1.A Structural: a block for each table written for the first time", f"{P1} S1",
        new_tables, ", ".join(new_tables) if new_tables else "no new table")
    add("dossier.1B", "dossier", "1.B Entity: each person, channel, ticket, PR, doc and figure the changed records name "
        "(value in every service: AGREE or DISAGREE)", f"{P1} S1", content, ids_of(content) or "no text changed")
    add("dossier.1C", "dossier", "1.C Voice and realism: a status line and samples for each speaker new to the SQL; "
        "check the changed text against its author's samples", f"{P1} S1", live,
        ("new speakers: " + ", ".join(new_speakers)) if new_speakers else
        ("no new speaker; changed text by existing speakers" if live else "no text added or changed"))
    add("dossier.1D", "dossier", "1.D Keyword: hit count or NEW TERM for each search term the changed text adds or drops",
        f"{P1} S1", content, ids_of(content) or "no text changed")
    add("dossier.1E", "dossier", "1.E Persona reach: persona_view.py check-sql with the changed load-bearing ids",
        f"{P1} S1, hard gate 8", live, ids_of(live) or "no record added or changed")
    add("dossier.1F", "dossier", "1.F Collision: lookup of each newly minted id (scan_complete:true, 0 hits)",
        f"{P1} S1", added_inserts, ids_of(added_inserts) or "no new id")
    add("dossier.S2", "dossier", "S2 Record ledger: one row per record added, removed or changed", f"{P1} S2",
        entries, f"{len(entries)} records")
    add("dossier.S3", "dossier", "S3 Findability, discovery order and hidden-authority proof for each added or moved "
        "record (likely query, competing base hits, chain position)", f"{P1} S3, hard gate 10", content,
        ids_of(content) or "no content record changed")
    for svc in services:
        add(f"dossier.S4.{svc}", "dossier", f"S4 {svc} recipe: {SERVICE_RECIPES.get(svc, 'follow the service recipe')}",
            f"{P1} S4, hard gate 9", True, ids_of([e for e in entries if e["service"] == svc]))
    mirrors = [s for s in services if s in MIRROR_SERVICES]
    add("dossier.integrations", "dossier", "Integrations and companions table: one decision per changed record whose "
        "service has a mirror" + ("".join(f" ({s}: {MIRROR_SERVICES[s]})" for s in mirrors)), f"{P1} S4 Companions",
        mirrors, ", ".join(mirrors) if mirrors else "no changed record in a mirrored service (github, gcal)")
    add("dossier.census", "dossier", "Touched-data census and coherence hazards: add the neighbours of the changed "
        "records and match them against coherence_hazards.json", f"{P1} S7.3", content,
        "neighbours and base ids are listed above" if content else "no content record changed")
    add("dossier.counter_readings", "dossier", "Counter-readings per coherence category, for the changed records and "
        "their neighbours only", f"{P1} S7.4", content, ids_of(content) or "no content record changed")
    add("dossier.disagreements", "dossier", "Intended disagreements: update the entry if a changed record is one side "
        "of a designed disagreement", f"{P1} S6", content, ids_of(content) or "no content record changed")
    add("dossier.fact_sheet", "dossier", "Fact sheet: facts whose home rows changed, and the fact_check.py output",
        f"{P1} S6, hard gate 12", fact_keys or (content and not manifest),
        ("facts: " + ", ".join(fact_keys)) if fact_keys else
        ("no manifest found: check the facts by hand" if not manifest else "no fact has a home row among the changed records"))
    add("dossier.facts_human", "dossier", "Facts for the human: the rows of the changed records (locator, fact, reach "
        "path, role)", f"{P1} S6; {P1A} gate 7", entries, f"{len(entries)} records")
    add("dossier.prompt_brief", "dossier", "Constraints for the prompt brief: anchor names", f"{P1} S6", anchor_hits,
        ("anchors: " + ", ".join(anchor_hits)) if anchor_hits else "no anchor record changed")
    add("dossier.followups", "dossier", "Platform follow-ups: the changed text sits in a carrier whose rendering is "
        "not verified (GCal description, Slides notes, Contacts description, Drive content_text)",
        f"{P1} S6, hard gate 7", soft, ids_of(soft) or "no unverified carrier among the changed records")
    add("dossier.self_review", "dossier", "Self-review: paste the final tool outputs again (they are bound to the new "
        "bytes)", f"{P1} S7.1", entries, "every SQL change re-passes 01")
    add("file.manifest", "file", "01_Hardness_Manifest.json: seeded_ids, home_ids, version_records and chain hops "
        "that name a changed id; one design_delta entry", f"{P1} S5", manifest_hits or (entries and not manifest),
        ("ids named in the manifest: " + ", ".join(manifest_hits[:8])) if manifest_hits else
        ("no manifest found" if not manifest else "the manifest names none of the changed ids"))
    add("file.budget", "file", "01_Difficulty_Budget.json: the moved unit's decider (record_id, container), carrier, "
        "habit and find_rate; the revision label. design_id stays", "contract: difficulty budget file", content,
        "a decider moved" if content else "no content record changed")
    add("file.solver", "file", f"solver: oracle_kit.py check --task-dir {task} --previous-sql <previous SQL> "
        "--previous-truth <its truth.json>, then recompute solver/truth.json", f"{P1} S4b, hard gate 15", entries,
        "the solver must reproduce the previous truth on the previous SQL")
    add("file.dispositions", "file", "01c_Dispositions.json: mutation and liveness dispositions of the node whose "
        "records changed", f"{P1} S5b, S5c, hard gate 16", content,
        ids_of(content) or "no content record changed")
    add("file.revision_copy", "file", "Store the revision: copy 01_Universe_Inject.sql and 01d_Coherence_Sweep.json to "
        "Working_Files/run_forensics/<rev>/ and never edit the copies", f"{P1} S5e", entries, "every revision is stored")
    tools = [
        ("tool.sql_lint", f"sql_lint.py {task}/{SQL_NAME}", f"{P1} S5", entries, "whole file, cheap"),
        ("tool.base_check", f"base_check.py {task}/{SQL_NAME}", f"{P1} S5", entries, "whole file, cheap"),
        ("tool.hg_lint", f"hg.py lint --task-dir {task}", f"{P1} S5", entries, "whole file, cheap"),
        ("tool.fact_check", f"fact_check.py {task}/{SQL_NAME} --manifest <manifest> --no-leak", f"{P1} S5", entries,
         "a moved value must not leak outside its home rows"),
        ("tool.persona_view", "persona_view.py check-sql <persona> <sql> --load-bearing <changed ids>", f"{P1} S5",
         live, ids_of(live) or "no record added or changed"),
        ("tool.base_claims", f"base_claims.py {task}/{SQL_NAME} --task-dir {task}", f"{P1} S5", branchy,
         ids_of(branchy) or "no changed text names a branch"),
        ("tool.hardness_gate", "hardness_gate.py <manifest> <sql>", f"{P1} S5, {P1A} gate 7", entries,
         "seeded ids must still resolve"),
        ("tool.mutation", f"difficulty_mutation.py mutate --task-dir {task} (then geometry)", f"{P1} S5b", content,
         "the moved node's intervention reads its records" if content else "no content record changed"),
        ("tool.liveness", f"trap_liveness.py --task-dir {task}", f"{P1} S5c", content,
         "flags of the moved node" if content else "no content record changed"),
        ("tool.preflight", f"hardness_forecast.py forecast ... then preflight_report.py --task-dir {task}",
         f"{P1} S5e, {P1A} gate 7", entries, "the preflight report is bound to the SQL by sha256"),
        ("tool.coherence_sweep", f"coherence_sweep.py brief --task-dir {task} --previous <previous SQL>, then check",
         "plan WS4.6", entries, "scoped to the records listed above"),
        ("tool.relocation", f"revision_scope.py relocation --task-dir {task} --previous <previous SQL>", "plan WS6.3",
         entries, "one unit, one move"),
        ("tool.stage_gate", f"stage_gate.py injection {task} --paste", f"{P1} hard gate 13", entries,
         "blocking before hand-off"),
        ("platform.injection_prompt", "platform /injection, then /prompt on the new SQL", f"{P1A} gate 7", entries,
         "every SQL revision re-opens both"),
    ]
    for item_id, title, source, redo, why in tools:
        add(item_id, "tool", title, source, redo, why)
    return items


# ---------------------------------------------------------------- relocation

def load_budget(path) -> dict | None:
    path = Path(path)
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise UsageError(f"cannot read the difficulty budget {path}: {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("units"), list):
        raise UsageError(f"{path} is not a difficulty budget ({BUDGET_SCHEMA}): no units list")
    return data


def _decider_ids(budget: dict | None) -> dict:
    out = {}
    for unit in (budget or {}).get("units") or []:
        decider = unit.get("decider") if isinstance(unit, dict) else None
        if isinstance(decider, dict) and decider.get("record_id") and unit.get("id"):
            out[str(unit["id"])] = str(decider["record_id"])
    return out


def split_sentences(text: str) -> list:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", text or "") if s.strip()]


def relocation_check(diff: dict, budget: dict | None, previous_budget: dict | None = None, unit: str | None = None,
                     previous_prompt: str | None = None, current_prompt: str | None = None) -> dict:
    """One relocation of one unit's decider, nothing else. Returns {"status", "detail", "lines", ...}."""
    groups, entries = diff["groups"], diff["entries"]
    summary = diff["summary"]
    by_key = {e["key"]: e for e in entries}
    all_records = dict(diff["_previous"]["records"])
    all_records.update(diff["_current"]["records"])
    lines, problems = [], []
    added_sentences = []
    if previous_prompt is not None and current_prompt is not None:
        before = {_norm_text(s) for s in split_sentences(previous_prompt)}
        added_sentences = [s for s in split_sentences(current_prompt) if _norm_text(s) not in before]
        if added_sentences:
            problems.append(f"{len(added_sentences)} prompt sentence(s) added or reworded")
            lines += [f"prompt sentence added: {s}" for s in added_sentences]
    if not entries and not diff["unparsed"]:
        detail = "the two SQL files hold the same records: nothing was relocated"
        if problems:
            detail += "; " + "; ".join(problems)
        return {"status": "WARN", "detail": detail, "lines": lines, "units": [], "unattributed": [],
                "attribution": {}, "added_sentences": added_sentences}
    if diff["unparsed"]:
        problems.append(f"{len(diff['unparsed'])} changed statement(s) the parser could not read")
        lines += [f"unparsed statement {u['state']} at line {u['line']}: {u['head']}" for u in diff["unparsed"]]
    if budget is None:
        shape = (f"{summary['content_records']} content record(s) and {summary['companion_records']} companion "
                 f"record(s) changed (shape: {summary['shape']})")
        lines += [f"{g['kind']:9} {'+'.join(g['states']):8} {g['ids'][0]}" for g in groups]
        return {"status": "WARN", "detail": f"no {BUDGET_NAME}: the change cannot be tied to a unit; {shape}"
                + ("; " + "; ".join(problems) if problems else ""), "lines": lines, "units": [],
                "unattributed": [g["ids"][0] for g in groups], "attribution": {}, "added_sentences": added_sentences}
    current_ids, previous_ids = _decider_ids(budget), _decider_ids(previous_budget)
    attribution = {}                     # logical -> (unit, role)
    for g in groups:
        for uid in sorted(set(current_ids) | set(previous_ids)):
            if {current_ids.get(uid), previous_ids.get(uid)} & set(g["ids"]):
                attribution[g["logical"]] = (uid, "decider")
                break
    # A unit whose decider is among the added or changed records: its old home is the removed (or edited)
    # content record with the most similar text, when no previous budget names it.
    moved_units = {uid for name, (uid, _) in attribution.items()}
    for move in summary["moves"]:
        src, dst = by_key[move["from_key"]]["logical"], by_key[move["to_key"]]["logical"]
        if dst in attribution and src not in attribution and attribution[dst][0] not in previous_ids:
            attribution[src] = (attribution[dst][0], "decider (old home, matched by text)")
    # Companions: counters, bumps and structural rows next to a record already tied to a unit.
    progress = True
    while progress:
        progress = False
        for g in groups:
            if g["logical"] in attribution or g["kind"] != "companion":
                continue
            for key in g["keys"]:
                rec = all_records[key]
                near = neighbours(rec, all_records)
                linked = set(near["copy"]) | set(near["thread"]) | set(near["reference"])
                for other in sorted(linked):
                    owner = attribution.get(all_records[other]["logical"]) if other in by_key else None
                    if owner:
                        attribution[g["logical"]] = (owner[0], "companion")
                        progress = True
                        break
                if g["logical"] in attribution:
                    break
    unattributed = [g for g in groups if g["logical"] not in attribution]
    units = sorted({uid for uid, role in attribution.values() if role.startswith("decider")})
    for g in groups:
        owner = attribution.get(g["logical"])
        label = f"{owner[0]} {owner[1]}" if owner else "no unit"
        lines.append(f"{g['kind']:9} {'+'.join(g['states']):8} {g['ids'][0]}  -> {label}")
    if unattributed:
        problems.insert(0, f"{len(unattributed)} record(s) belong to no unit: "
                        + ", ".join(g["ids"][0] for g in unattributed[:6]) + (" ..." if len(unattributed) > 6 else ""))
    if len(units) > 1:
        problems.insert(0, f"{len(units)} units moved ({', '.join(units)})")
    if not units:
        problems.insert(0, "no unit's decider is among the changed records")
    if unit and units and units != [unit]:
        problems.insert(0, f"--unit {unit} was asked for, the change touches {', '.join(units)}")
    if unit and unit not in current_ids and unit not in previous_ids:
        problems.insert(0, f"unit {unit} is not in the budget")
    if problems:
        return {"status": "WARN", "detail": "not one relocation: " + "; ".join(problems), "lines": lines,
                "units": units, "unattributed": [g["ids"][0] for g in unattributed],
                "attribution": {k: list(v) for k, v in attribution.items()}, "added_sentences": added_sentences}
    companions = sum(1 for _, role in attribution.values() if role == "companion")
    detail = (f"one relocation of unit {units[0]}: {len(groups) - companions} decider record(s) and {companions} "
              f"companion record(s) changed, nothing else")
    if previous_prompt is None:
        detail += " (prompt not compared: pass --previous-prompt)"
    return {"status": "PASS", "detail": detail, "lines": lines, "units": units, "unattributed": [],
            "attribution": {k: list(v) for k, v in attribution.items()}, "added_sentences": added_sentences}


# ---------------------------------------------------------------- results and output

def _verdict(checks: list) -> str:
    statuses = {c["status"] for c in checks}
    return "FAIL" if "FAIL" in statuses else ("WARN" if "WARN" in statuses else "PASS")


def _result(command: str, bound_to: dict, checks: list, **extra) -> dict:
    out = {"tool": TOOL, "version": VERSION, "verdict": _verdict(checks), "bound_to": dict(sorted(bound_to.items())),
           "checks": checks, "command": command}
    out.update(extra)
    return out


def _public_entries(diff: dict) -> list:
    return [{k: v for k, v in e.items() if k != "logical"} for e in diff["entries"]]


def diff_result(previous_path, current_path) -> dict:
    diff = diff_files(previous_path, current_path)
    s = diff["summary"]
    checks = [{"id": "revision.diff", "status": "PASS",
               "detail": f"{s['added']} added, {s['removed']} removed, {s['changed']} changed records: "
                         f"{s['content_records']} content and {s['companion_records']} companion, "
                         f"in {', '.join(s['services']) or 'no service'} (shape: {s['shape']})"}]
    total_unparsed = len(diff["_previous"]["unparsed"]) + len(diff["_current"]["unparsed"])
    checks.append({"id": "revision.parse", "status": "WARN" if total_unparsed else "PASS",
                   "detail": (f"{total_unparsed} statement(s) could not be read as INSERT, UPDATE or DELETE; they are "
                              f"compared as raw text only ({s['unparsed_changed']} differ)") if total_unparsed
                   else "every statement was read"})
    return _result("diff", diff["bound_to"], checks, summary=s, records=_public_entries(diff),
                   unparsed=diff["unparsed"], _diff=diff)


def scope_result(task_dir, previous_path) -> dict:
    current_path = _slot(task_dir, SQL_NAME)
    if not current_path.is_file():
        raise UsageError(f"no {SQL_NAME} in {task_dir}")
    diff = diff_files(previous_path, current_path)
    reread = reread_ids(diff)
    checklist = build_checklist(diff, task_dir)
    redo = [i for i in checklist if i["redo"]]
    s = diff["summary"]
    n_read = len(reread["changed"]) + len(reread["neighbours"]) + len(reread["base"])
    status = "WARN" if diff["unparsed"] else "PASS"
    checks = [{"id": "revision.scope", "status": status,
               "detail": f"{s['content_records']} content record(s) changed in "
                         f"{', '.join(s['content_services']) or 'no service'}; {n_read} record(s) to re-read; "
                         f"{len(redo)} item(s) to redo, {len(checklist) - len(redo)} not needed"
                         + (f"; {len(diff['unparsed'])} changed statement(s) could not be read" if diff["unparsed"] else "")}]
    return _result("scope", diff["bound_to"], checks, summary=s, reread=reread, checklist=checklist, _diff=diff)


def evaluate(task_dir, previous_sql, unit=None, previous_prompt=None, previous_budget=None) -> dict:
    """The relocation check for the gate. Side-effect free. Raises UsageError on a missing input."""
    task_dir = Path(task_dir)
    current_path = _slot(task_dir, SQL_NAME)
    if not current_path.is_file():
        raise UsageError(f"no {SQL_NAME} in {task_dir}")
    diff = diff_files(previous_sql, current_path)
    bound = dict(diff["bound_to"])
    budget_path = _slot(task_dir, BUDGET_NAME)
    budget = load_budget(budget_path)
    if budget is not None:
        bound[_rel(budget_path)] = sha256_file(budget_path)
    prior = load_budget(previous_budget) if previous_budget else None
    if previous_budget and prior is None:
        raise UsageError(f"no previous budget at {previous_budget}")
    if prior is not None:
        bound[_rel(previous_budget)] = sha256_file(previous_budget)
    prev_prompt = cur_prompt = None
    if previous_prompt:
        prev_prompt = _read(previous_prompt, "the previous prompt")
        prompt_path = _slot(task_dir, PROMPT_NAME)
        cur_prompt = _read(prompt_path, "the current prompt")
        bound[_rel(previous_prompt)] = sha256_file(previous_prompt)
        bound[_rel(prompt_path)] = sha256_file(prompt_path)
    outcome = relocation_check(diff, budget, prior, unit, prev_prompt, cur_prompt)
    checks = [{"id": "revision.relocation", "status": outcome["status"], "detail": outcome["detail"]}]
    return _result("relocation", bound, checks, summary=diff["summary"], relocation=outcome, _diff=diff)


def _ids_line(keys: list, records: dict) -> str:
    ids = [records[k]["id"] for k in keys]
    shown = ", ".join(ids[:NEIGHBOUR_PRINT_LIMIT])
    return shown + (f" (+{len(ids) - NEIGHBOUR_PRINT_LIMIT} more)" if len(ids) > NEIGHBOUR_PRINT_LIMIT else "")


def to_text(result: dict) -> str:
    out = [f"REVISION SCOPE ({result['command']}): {result['verdict']}"]
    out += [f"[{c['status']}] {c['id']}: {c['detail']}" for c in result["checks"]]
    diff = result.get("_diff")
    if result["command"] == "diff" and diff:
        cur = diff["_current"]["records"]
        for e in diff["entries"]:
            tail = f" fields: {', '.join(e['changed_fields'])}" if e["changed_fields"] else ""
            out.append(f"  {e['state']:8} {e['kind']:9} {e['table']}  {e['id']}{tail}")
            if e["text"]:
                out.append(f"           text: {e['text']}")
            for relation in ("copy", "thread", "reference", "container"):
                if e["neighbours"][relation]:
                    out.append(f"           {relation}: {_ids_line(e['neighbours'][relation], cur)}")
            if e["neighbours"]["base"]:
                base = e["neighbours"]["base"]
                out.append("           base: " + ", ".join(base[:NEIGHBOUR_PRINT_LIMIT])
                           + (f" (+{len(base) - NEIGHBOUR_PRINT_LIMIT} more)" if len(base) > NEIGHBOUR_PRINT_LIMIT else ""))
        for move in diff["summary"]["moves"]:
            out.append(f"  move     {move['from']} -> {move['to']} (text similarity {move['ratio']}"
                       + (", same container" if move["same_container"] else "") + ")")
        for u in diff["unparsed"]:
            out.append(f"  unparsed {u['state']} line {u['line']}: {u['head']}")
    if result["command"] == "scope":
        reread = result["reread"]
        out.append("Re-read for the scoped coherence sweep")
        out += [f"  changed    {r['id']}  ({r['table']}, {r['state']}, {r['kind']})" for r in reread["changed"]]
        out += [f"  removed    {r['id']}  ({r['table']}): check that nothing still points at it" for r in reread["removed"]]
        out += [f"  neighbour  {r['id']}  ({r['table']}; {'; '.join(r['because'][:3])})" for r in reread["neighbours"]]
        out += [f"  base       {rid}" for rid in reread["base"]]
        out.append("Redo")
        out += [f"  - [ ] {i['title']} ({i['source']}) - {i['why']}" for i in result["checklist"] if i["redo"]]
        out.append("Not needed for this revision")
        out += [f"  - [skip] {i['title']} ({i['source']}) - {i['why']}" for i in result["checklist"] if not i["redo"]]
    if result["command"] == "relocation":
        out += ["  " + line for line in result["relocation"]["lines"]]
    return "\n".join(out)


def _strip_private(result: dict) -> dict:
    return {k: v for k, v in result.items() if not k.startswith("_")}


# ---------------------------------------------------------------- self-test

def _fixture_sql(dm_text: str | None, mail_text: str | None, extra: str = "") -> str:
    """A small injection: a Slack thread parent with a reply, a Linear issue with a comment, and the deciding
    record either as a DM (dm_text) or as an email (mail_text)."""
    parts = ["-- Are you planning to inject? Yes", "BEGIN;",
             "INSERT INTO slack.slack_messages (id, channel_id, ts, user_id, text, thread_ts_legacy, thread_parent_id, "
             "reply_count) VALUES ('" + hashlib.sha256(b"C0123ABCD|1700000000.000100").hexdigest()[:32] + "', "
             "'C0123ABCD', '1700000000.000100', 'U_ARTHUR', 'Release notes for the beta, see ENG-900', "
             "'1700000000.000100', NULL, 1);",
             "INSERT INTO slack.slack_messages (id, channel_id, ts, user_id, text, thread_ts_legacy, thread_parent_id, "
             "reply_count) VALUES ('" + hashlib.sha256(b"C0123ABCD|1700000300.000200").hexdigest()[:32] + "', "
             "'C0123ABCD', '1700000300.000200', 'U_BRIAN', 'thanks, noted', '1700000000.000100', '"
             + hashlib.sha256(b"C0123ABCD|1700000000.000100").hexdigest()[:32] + "', 0);",
             "INSERT INTO linear.linear_comments (id, issue_id, author_id, body, created_at) VALUES "
             "('comment_a1', 'ENG-900', 'usr_1', 'Shop icons are done; it''s the last one', '2026-02-10T10:00:00Z');",
             "UPDATE linear.linear_issues SET updated_at = '2026-02-10T10:00:00Z' WHERE id = 'ENG-900';"]
    if dm_text is not None:
        parts.append("INSERT INTO slack.slack_messages (id, channel_id, ts, user_id, text, thread_ts_legacy, "
                     "thread_parent_id, reply_count) VALUES ('"
                     + hashlib.sha256(b"D0BRIAN01|1700009000.000300").hexdigest()[:32]
                     + "', 'D0BRIAN01', '1700009000.000300', 'U_BRIAN', '" + dm_text.replace("'", "''")
                     + "', NULL, NULL, 0);")
    if mail_text is not None:
        parts += ["INSERT INTO gmail.gmail_threads (id, user_email, snippet) VALUES "
                  "('owen@hg.co/1849333980856689601', 'owen@hg.co', 'tavern');",
                  "INSERT INTO gmail.gmail_messages (id, thread_id, user_email, from_email, subject, body_text, date) "
                  "VALUES ('owen@hg.co/<m1@mail>', 'owen@hg.co/1849333980856689601', 'owen@hg.co', 'vincent@hg.co', "
                  "'tavern', '" + mail_text.replace("'", "''") + "', '2026-02-11T09:00:00Z');"]
    parts += [extra, "COMMIT;"]
    return "\n".join(p for p in parts if p) + "\n"


def _self_test() -> int:
    from selftest_sandbox import scratch_tmp
    line = "The Tavern popup is still broken on Android, do not close ENG-900 yet"
    with scratch_tmp("revision_scope_") as tmp:
        root = Path(tmp)
        task = root / "task"
        (task / "Working_Files").mkdir(parents=True)
        prev = root / "rev1.sql"
        prev.write_text(_fixture_sql(line, None), encoding="utf-8")
        cur = task / SQL_NAME
        cur.write_text(_fixture_sql(None, line + "."), encoding="utf-8")
        budget = {"schema": BUDGET_SCHEMA, "design_id": "D1", "revision": "rev2", "mode": "medium",
                  "weight_basis": "surface", "total_weight": 10,
                  "units": [{"id": "U1", "role": "anchor", "cause": "the correction is an email", "carrier":
                             "off_service_record", "habit": {"service": "gmail", "action": "get_thread"},
                             "decider": {"service": "gmail", "record_id": "owen@hg.co/<m1@mail>",
                                         "container": "owen@hg.co", "injected": True},
                             "find_rate": [0.0, 0.15], "rows": [{"id": "X1", "weight": 5}]},
                            {"id": "U2", "role": "variance", "cause": "a comment", "carrier": "non_set_ticket",
                             "habit": {"service": "linear", "action": "list_comments"},
                             "decider": {"service": "linear", "record_id": "comment_a1", "container": "ENG-900",
                                         "injected": True}, "find_rate": [0.4, 0.6], "rows": [{"id": "X2", "weight": 5}]}]}
        (task / "Working_Files" / BUDGET_NAME).write_text(json.dumps(budget), encoding="utf-8")

        # diff: one DM removed, one mail + its thread row added, and the move is recognised
        d = diff_result(prev, cur)
        s = d["summary"]
        assert (s["added"], s["removed"], s["changed"]) == (2, 1, 0), s
        assert s["content_records"] == 2 and s["companion_records"] == 1 and s["shape"] == "two_records", s
        assert s["moves"] and s["moves"][0]["from"] == "D0BRIAN01/1700009000.000300", s["moves"]
        assert d["verdict"] == "PASS" and d["checks"][0]["id"] == "revision.diff"
        # reformatting the SQL is not a change
        same = load_records(_fixture_sql(line, None).replace("VALUES", "\n  VALUES").replace(";\n", ";\n\n-- note\n"))
        assert not diff_records(load_records(prev.read_text()), same)["entries"]
        # ... and neither is folding an UPDATE into the INSERT it follows
        split = ("INSERT INTO linear.linear_issues (id, title) VALUES ('ENG-1', 'a');\n"
                 "UPDATE linear.linear_issues SET title = 'b' WHERE id = 'ENG-1';\n")
        folded = "INSERT INTO linear.linear_issues (id, title) VALUES ('ENG-1', 'b');\n"
        folded_diff = diff_records(load_records(split), load_records(folded))
        assert not folded_diff["entries"], folded_diff["entries"]
        # neighbours: the reply's thread holds its parent; the comment hangs on a base issue
        recs = load_records(cur.read_text())["records"]
        reply = recs["slack.slack_messages:C0123ABCD/1700000300.000200"]
        near = neighbours(reply, recs)
        assert "slack.slack_messages:C0123ABCD/1700000000.000100" in near["thread"], near
        comment = recs["linear.linear_comments:comment_a1"]
        assert "linear.linear_issues:ENG-900" in neighbours(comment, recs)["thread"]
        mail = recs["gmail.gmail_messages:owen@hg.co/<m1@mail>"]
        assert "gmail.gmail_threads:owen@hg.co/1849333980856689601" in neighbours(mail, recs)["thread"]
        # the root post names ENG-900 in its text: a reference neighbour of the issue update
        issue = recs["linear.linear_issues:ENG-900"]
        assert "slack.slack_messages:C0123ABCD/1700000000.000100" in neighbours(issue, recs)["reference"]

        # relocation: PASS for one unit's decider and its thread row
        r = evaluate(task, prev)
        assert r["verdict"] == "PASS" and r["relocation"]["units"] == ["U1"], r["checks"]
        assert evaluate(task, prev, unit="U2")["verdict"] == "WARN"
        # planted bad: an extra row that belongs to no unit
        cur.write_text(_fixture_sql(None, line + ".", extra=
                                    "INSERT INTO linear.linear_comments (id, issue_id, author_id, body, created_at) "
                                    "VALUES ('comment_b2', 'ENG-900', 'usr_2', 'one more decoy note', "
                                    "'2026-02-11T10:00:00Z');"), encoding="utf-8")
        r = evaluate(task, prev)
        assert r["verdict"] == "WARN" and "comment_b2" in r["checks"][0]["detail"], r["checks"]
        # planted bad: two units moved
        cur.write_text(_fixture_sql(None, line + ".").replace("it''s the last one", "it''s the last one, I think"),
                       encoding="utf-8")
        r = evaluate(task, prev)
        assert r["verdict"] == "WARN" and "2 units moved" in r["checks"][0]["detail"], r["checks"]
        # planted bad: a prompt sentence added
        cur.write_text(_fixture_sql(None, line + "."), encoding="utf-8")
        old_prompt = root / "old_prompt.txt"
        old_prompt.write_text("Can you sort the bug list? Reply to Arthur when done.", encoding="utf-8")
        (task / PROMPT_NAME).write_text("Can you sort the bug list? Check my mail too. Reply to Arthur when done.",
                                        encoding="utf-8")
        r = evaluate(task, prev, previous_prompt=old_prompt)
        assert r["verdict"] == "WARN" and r["relocation"]["added_sentences"] == ["Check my mail too."], r["checks"]
        (task / PROMPT_NAME).write_text(old_prompt.read_text(), encoding="utf-8")
        assert evaluate(task, prev, previous_prompt=old_prompt)["verdict"] == "PASS"
        # no budget: WARN with the shape
        (task / "Working_Files" / BUDGET_NAME).unlink()
        r = evaluate(task, prev)
        assert r["verdict"] == "WARN" and BUDGET_NAME in r["checks"][0]["detail"]

        # scope: the re-read list and the checklist
        sc = scope_result(task, prev)
        ids = {x["id"] for x in sc["reread"]["changed"]}
        assert "owen@hg.co/<m1@mail>" in ids and sc["reread"]["removed"][0]["id"] == "D0BRIAN01/1700009000.000300"
        redo = {i["id"] for i in sc["checklist"] if i["redo"]}
        skip = {i["id"] for i in sc["checklist"] if not i["redo"]}
        assert {"dossier.1A", "dossier.1E", "dossier.1F", "dossier.S4.gmail", "tool.sql_lint",
                "tool.coherence_sweep"} <= redo, redo          # 1.A: the mail tables are new in this revision
        assert {"dossier.integrations", "dossier.prompt_brief", "dossier.followups", "tool.base_claims"} <= skip, skip
        text = to_text(sc)
        assert text.startswith("REVISION SCOPE (scope): PASS") and "- [ ]" in text and "- [skip]" in text
        # an unparsed statement is reported, never dropped
        odd = load_records("INSERT INTO slack.slack_messages SELECT * FROM x;\n")
        assert len(odd["unparsed"]) == 1 and not odd["records"]
        json.dumps(_strip_private(sc))
        json.dumps(_strip_private(d))
    print("self-test: ok (diff added/removed/changed, reformatting ignored, neighbours by thread/parent/reference, "
          "move detection, relocation PASS and four planted WARN cases, scope re-read list and checklist, "
          "unparsed statement)")
    return 0


# ---------------------------------------------------------------- command line

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in argv:
        return _self_test()
    ap = argparse.ArgumentParser(prog="revision_scope.py", description="what a SQL revision changed (see docstring)")
    sub = ap.add_subparsers(dest="command")
    p = sub.add_parser("diff", help="records added, removed and changed between two injection files")
    p.add_argument("--previous", required=True)
    p.add_argument("--current", required=True)
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("scope", help="what to re-read and what to redo for this revision")
    p.add_argument("--task-dir", required=True)
    p.add_argument("--previous", required=True)
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("relocation", help="check that the revision is one relocation of one unit")
    p.add_argument("--task-dir", required=True)
    p.add_argument("--previous", required=True)
    p.add_argument("--unit")
    p.add_argument("--previous-prompt")
    p.add_argument("--previous-budget")
    p.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    if not args.command:
        ap.error("a command is required: diff, scope or relocation (or --self-test)")
    try:
        if args.command == "diff":
            result = diff_result(args.previous, args.current)
        elif args.command == "scope":
            result = scope_result(args.task_dir, args.previous)
        else:
            result = evaluate(args.task_dir, args.previous, unit=args.unit, previous_prompt=args.previous_prompt,
                              previous_budget=args.previous_budget)
    except UsageError as exc:
        print(f"revision_scope: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(_strip_private(result), indent=2, sort_keys=True, ensure_ascii=False) if args.json
          else to_text(result))
    return 1 if result["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
