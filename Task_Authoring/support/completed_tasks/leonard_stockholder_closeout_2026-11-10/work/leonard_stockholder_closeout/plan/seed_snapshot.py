#!/usr/bin/env python3
"""Reader copy of everything the SQL seeds, for cold reviewers (no answer key)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql
L = ["# Seeded records, as the SQL writes them (reader copy; no answer key)", ""]
for x in parse_sql(open(os.path.join(TI, "01_Universe_Inject.sql")).read()):
    if x["op"] != "insert":
        continue
    t, r = x["table"], x["row"]
    if t == "gdocs.docs_documents": L += [f"## Doc {r['document_id']} ({r['created_time']}), owner {r['owner_email']}", r["body_text"], ""]
    elif t == "gdrive.drive_files": L += [f"- Drive {r['mime_type'].split('.')[-1]} {r['id']} '{r['name']}' parent {r['parents_json']} created {r['created_time']}"]
    elif t == "gsheets.sheets_sheets": L += [f"## Sheet {r['spreadsheet_id']} tab {r['title']}", "```", "\n".join(" | ".join(map(str, row)) for row in json.loads(r["grid_json"])), "```", ""]
    elif t == "gslides.slides_page_elements": L += [f"- Slide text ({r['presentation_id']}): {r['text']!r}"]
    elif t == "slack.slack_messages": L += [f"- Slack {r['channel_id']}/{r['ts']} ({r['created_at']}) {r['user_id']}: {r['text']}"]
    elif t == "trello.trello_cards": L += [f"## Trello card {r['id']} '{r['name']}' (To Do, founders' board)", r['"desc"'] if '"desc"' in r else r.get('desc', ''), ""]
    elif t == "trello.trello_actions": L += [f"- Trello action {r['type']} {r['date']}: {json.loads(r['data_json']).get('text', '')}"]
    elif t == "gmail.gmail_messages": L += [f"## Mail {r['id']} ({r['date']}) mailbox {r['user_email']}", f"From {r['from_name']} <{r['from_email']}> to {r['to_json']} cc {r['cc_json']}; subject {r['subject']}; thread {r['thread_id']}", str(r["body_text"]).replace("\r\n", "\n"), ""]
    elif t == "gcal.gcal_events": L += [f"## Calendar {r['event_id']} on {r['calendar_id']}: '{r['summary']}' {r['start_ts']} to {r['end_ts']}, attendees {r['attendees_json']}", ""]
    elif t == "contacts.contacts": L += [f"- Contact: {r['first_name']} {r['last_name']} | {r['job']} | {r['email']}"]
    elif t == "linear.linear_projects": L += [f"## Linear project {r['id']} '{r['name']}' lead {r['lead_id']} team {r['team_id']}, created {r['created_at']}, updated {r['updated_at']}", r["description"], ""]
    elif t == "linear.linear_issues": L += [f"- Linear {r['identifier']} '{r['title']}' state {r['state_id']} created {r['created_at']}"]
    elif t == "linear.linear_comments": L += [f"  - comment on {r['issue_id']} by {r['author_id']} {r['created_at']}: {r['body']}"]
open(os.path.join(WF, "research", "sweeps", "seed_snapshot.md"), "w").write("\n".join(L).replace("\\r\\n", "\n").replace("\\n", "\n") + "\n")
print(len(L))
