#!/usr/bin/env python3
"""Read-only overlay scanner for 01_Universe_Inject.sql.

Parses INSERT statements as TEXT (never executes SQL) and reports rows whose
concatenated string values contain every word of a query (word-level AND,
case-insensitive). Also resolves Claire-visibility per service.

Usage:
  python3 overlay_scan.py "<query>" [--all]
  python3 overlay_scan.py --file queries.txt

  --all   list every matching row, including ones not visible to Claire
          (default: all matches are listed but tagged VISIBLE=yes/no)
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "Task_Authoring" / "tools"))
from base_check import parse_sql  # noqa: E402

SQL_PATH = ROOT / "Task_Authoring" / "task_inputsN2" / "01_Universe_Inject.sql"
CLAIRE = "claire.morgan@harmonygames.co"
SLACK_OK = {"C06DJBJL798", "C08R8CHB0QL", "D05V2N6PZNU"}
DRIVE = {"gdrive.drive_files", "gdocs.docs_documents", "gsheets.sheets_spreadsheets",
         "gsheets.sheets_sheets", "gslides.slides_presentations", "gslides.slides_pages",
         "gslides.slides_page_elements"}

ID_KEYS = ["id", "document_id", "spreadsheet_id", "presentation_id", "event_id", "contact_id"]


def load_rows():
    return [r for r in parse_sql(SQL_PATH.read_text(encoding="utf-8")) if r["op"] == "insert"]


def haystack(row):
    return " ".join(v for v in row.values() if isinstance(v, str))


def row_id(table, row):
    for k in ID_KEYS:
        if row.get(k) not in (None, ""):
            return row[k]
    if table.startswith("trello."):
        return row.get("id") or row.get("idCard")
    return "?"


def owner_visible(owner, shared):
    if (owner or "").lower() == CLAIRE:
        return True
    return CLAIRE in (shared or "").lower()


def build_parent_maps(rows):
    """child id -> (owner_email, shared_with_emails_json) for diff services."""
    pres, sheets, drive = {}, {}, {}
    for r in rows:
        t, row = r["table"], r["row"]
        if t == "gslides.slides_presentations":
            pres[row.get("presentation_id")] = (row.get("owner_email"), row.get("shared_with_emails_json"))
        elif t == "gsheets.sheets_spreadsheets":
            sheets[row.get("spreadsheet_id")] = (row.get("owner_email"), row.get("shared_with_emails_json"))
        elif t == "gdrive.drive_files":
            drive[row.get("id")] = (row.get("owner_email"), row.get("shared_with_emails_json"))
    return pres, sheets, drive


def visibility(r, maps):
    t, row = r["table"], r["row"]
    pres, sheets, drive = maps
    if t.startswith("gmail."):
        return row.get("user_email") == CLAIRE, f"user_email={row.get('user_email')}"
    if t.startswith("gcal."):
        return row.get("calendar_id") == CLAIRE, f"calendar_id={row.get('calendar_id')}"
    if t.startswith("slack."):
        ch = row.get("channel_id")
        return ch in SLACK_OK, f"channel_id={ch} ts={row.get('ts')}"
    if t in DRIVE:
        owner, shared = row.get("owner_email"), row.get("shared_with_emails_json")
        src = "row"
        if owner is None and shared is None:
            parent = row.get("presentation_id") or row.get("spreadsheet_id") or row.get("drive_file_id")
            for m in (pres, sheets, drive):
                if parent in m:
                    owner, shared = m[parent]
                    src = f"parent {parent}"
                    break
        return owner_visible(owner, shared), f"owner_email={owner} ({src})"
    return True, "unscoped (not ACL-scoped)"


def run(query, rows, maps, show_all=True):
    words = [w for w in query.lower().split() if w]
    hits = []
    for r in rows:
        hay = haystack(r["row"]).lower()
        if all(w in hay for w in words):
            hits.append(r)
    print(f'### OVERLAY "{query}"  -> {len(hits)} matching INSERT row(s)')
    if not hits:
        print("  (no rows in 01_Universe_Inject.sql match every query word)")
        return
    for r in hits:
        vis, ev = visibility(r, maps)
        rid = row_id(r["table"], r["row"])
        tag = "VISIBLE" if vis else "HIDDEN "
        if r["table"].startswith("slack."):
            rid = f"{r['row'].get('channel_id')}/{r['row'].get('ts')}"
        print(f"  [{tag}] {r['table']}  id={rid}  {ev}")
        if show_all:
            txt = haystack(r["row"]).replace("\n", " ")
            print(f"           text: {txt[:220]}")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    rows = load_rows()
    maps = build_parent_maps(rows)
    if not args:
        print("usage: overlay_scan.py \"<query>\"")
        return 1
    for q in args:
        run(q, rows, maps)
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
