#!/usr/bin/env python3
"""Persona-visible dump of the seeded records (Frederick's view) for a blind fork sweep. No answer key, no ids map
beyond what the records themselves carry. Writes plan/record_dump_members_<rev>.md."""
import json, os, sys, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)); TI = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql
rev = sys.argv[1] if len(sys.argv) > 1 else "rev4"
FRED = "frederick.stone@harmonygames.co"
st = [x for x in parse_sql(open(os.path.join(TI, "01_Universe_Inject.sql")).read()) if x["op"] == "insert"]
T = {}
for x in st:
    T.setdefault(x["table"], []).append(x["row"])
NAMES = {"EMPLOYEE_0038_SLACK_ID": "Leonard Hayes", "EMPLOYEE_0016_SLACK_ID": "Robert", "EMPLOYEE_0008_SLACK_ID": "Frederick Stone"}
out = [f"# Persona-visible record dump (seeded part, {rev}) — Frederick's view\n"]
th = {}
for r in T["gmail.gmail_messages"]:
    if r["user_email"] == FRED:
        th.setdefault(r["thread_id"], []).append(r)
for tid, ms in sorted(th.items(), key=lambda kv: min(m["date"] for m in kv[1])):
    out.append(f"\n## thread {tid}")
    for m in sorted(ms, key=lambda m: m["date"]):
        out.append(f"  [{m['date']}] From {m['from_name']} <{m['from_email']}> To {m['to_json']} Cc {m['cc_json']} | {m['subject']}")
        out.append("    " + (m["body_text"] or "").replace("\\r", "").replace("\\n", "\n").replace("\r", "").replace("\n", "\n    "))
files = {r["id"]: r for r in T.get("gdrive.drive_files", [])}
out.append("\n# Drive / Docs / Slides (owned by or shared with Frederick)")
for r in T.get("gdocs.docs_documents", []):
    f = files.get(r["document_id"], {})
    if f.get("owner_email") == FRED or FRED in (f.get("shared_with_emails_json") or ""):
        out.append(f"\n## doc {r['document_id']} '{r['title']}' (owner {f.get('owner_email')}, folder {f.get('parents_json')}, created {f.get('created_time')})")
        out.append("    " + (r["body_text"] or "").replace("\n", "\n    "))
for r in T.get("gslides.slides_presentations", []):
    out.append(f"\n## slides {r['presentation_id']} '{r.get('title')}'")
    for e in T.get("gslides.slides_page_elements", []):
        if e["presentation_id"] == r["presentation_id"] and e.get("text"):
            out.append("    " + e["text"].replace("\n", " / "))
for r in T.get("gdrive.drive_files", []):
    if r["mime_type"].endswith("folder"):
        out.append(f"\n## folder {r['id']} '{r['name']}' owner {r['owner_email']} shared {r['shared_with_emails_json']}")
for r in T.get("gsheets.sheets_sheets", []):
    out.append(f"\n## sheet {r['spreadsheet_id']} tab '{r.get('title')}'\n    {str(r.get('grid_json'))[:1500]}")
out.append("\n# Slack (#executives C07C2866011 and DM D05S58U4SAK with Leonard)")
for r in sorted(T.get("slack.slack_messages", []), key=lambda r: float(r["ts"])):
    when = dt.datetime.fromtimestamp(float(r["ts"]), dt.UTC).strftime("%Y-%m-%d %H:%M UTC")
    par = f" (thread reply under parent ts {r['thread_ts_legacy']})" if r.get("thread_ts_legacy") else ""
    out.append(f"  [{when}] {r['channel_id']} {NAMES.get(r['user_id'], r['user_id'])}{par}: {r['text']}")
out.append("  base context: D05S58U4SAK ts 1758151772.570449 (Sep 17 23:29 UTC) Leonard Hayes: \"we have no localization though\" (a message in the DM about Google Play featuring); C07C2866011 ts 1758513190.847889 Leonard Hayes: \"Playtestcloud results are in - we are gonna go through the data...\"")
out.append("\n# Trello")
for r in T.get("trello.trello_cards", []):
    g = lambda k: r.get(k) or r.get('"' + k + '"')
    out.append(f"  card '{r['name']}' board {g('idBoard')} list {g('idList')}: {g('desc')}")
for r in T.get("trello.trello_check_items", []):
    out.append(f"    checklist item: {r.get('name')} (state {r.get('state')})")
out.append("\n# Linear")
for r in T.get("linear.linear_issues", []):
    out.append(f"  {r['identifier']} '{r['title']}' state {r.get('state_name') or r.get('state')}: {r['description']}")
for r in T.get("linear.linear_comments", []):
    out.append(f"    comment {r['id']} ({r.get('created_at')}): {r['body']}")
out.append("\n# Calendar (Frederick's copies)")
for r in T.get("gcal.gcal_events", []):
    if r["calendar_id"] == FRED:
        out.append(f"  {r['event_id']} '{r['summary']}' {r['start_json']} organizer {r['organizer_email']} attendees {r['attendees_json']} | description: {r['description']}")
out.append("\n# Contacts (seeded)")
for r in T.get("contacts.contacts", []):
    out.append(f"  {r['contact_id']}: {r.get('first_name')} {r.get('last_name')} · job {r.get('job')} · {r.get('email')}")
open(os.path.join(HERE, f"record_dump_members_{rev}.md"), "w").write("\n".join(out) + "\n")
print("wrote", f"record_dump_members_{rev}.md", len(out), "lines")
