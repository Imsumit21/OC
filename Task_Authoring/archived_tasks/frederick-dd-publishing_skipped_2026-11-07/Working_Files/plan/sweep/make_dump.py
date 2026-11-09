#!/usr/bin/env python3
"""Plain reading of every seeded record for the blind sweeps. Reads the SQL only; no design, truth or answer text."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / 'Task_Authoring/tools'))
from base_check import parse_sql
sql = (ROOT / 'Task_Authoring/task_inputs/01_Universe_Inject.sql').read_text()
items = parse_sql(sql)
def _un(v): return v.replace('\\r', '').replace('\\n', '\n') if isinstance(v, str) else v
for x in items:
    if 'row' in x: x['row'] = {k: _un(v) for k, v in x['row'].items()}
rows = [x for x in items if x['op'] == 'insert']
by = {}
for x in rows: by.setdefault(x['table'], []).append(x['row'])
o = ['# Seeded records (plain reading of the injection SQL)', '']
def J(v):
    try: return json.loads(v)
    except Exception: return v
o.append('## Drive files')
for r in by.get('gdrive.drive_files', []):
    o.append(f"- `{r['id']}` {r['name']} ({r['mime_type'].split('.')[-1]}) owner {r['owner_email']} shared {r['shared_with_emails_json']} parents {r['parents_json']} created {r['created_time']} modified {r['modified_time']}")
o.append('\n## Docs')
for r in by.get('gdocs.docs_documents', []):
    o += [f"### `{r['document_id']}` {r['title']} (owner {r['owner_email']}, {r['created_time']})", '```', r['body_text'], '```']
o.append('\n## Sheets')
for r in by.get('gsheets.sheets_sheets', []):
    o.append(f"### `{r['spreadsheet_id']}` tab {r['title']}")
    for row in J(r['grid_json']): o.append(' | '.join(str(c) for c in row))
o.append('\n## Slides')
for r in by.get('gslides.slides_page_elements', []):
    o.append(f"- `{r['presentation_id']}` {r['placeholder_type']}: {r['text']}")
o.append('\n## Slack')
for r in sorted(by.get('slack.slack_messages', []), key=lambda r: float(r['ts'])):
    o.append(f"- {r['created_at']} channel {r['channel_id']} user {r['user_id']} thread_parent {r['thread_parent_id']} (root ts {r['thread_ts_legacy']}) id {r['id']}\n  > " + r['text'].replace('\n', '\n  > '))
o.append('\n## Trello')
for r in by.get('trello.trello_cards', []):
    o.append(f"- card `{r['id']}` {r['name']} list {r['idList']} members {r['idMembers_json']} desc: {r['desc']!r}")
for r in by.get('trello.trello_actions', []):
    d = J(r['data_json']); o.append(f"- action {r['type']} {r['date']} by {r['idMemberCreator']} on `{r['idCard']}`: {d.get('text', '')}")
o.append('\n## Gmail (Frederick and others, by thread)')
ms = by.get('gmail.gmail_messages', [])
th = {}
for r in ms: th.setdefault(r['thread_id'], []).append(r)
for t, rs in sorted(th.items(), key=lambda kv: min(x['date'] for x in kv[1])):
    o.append(f"### thread {t}")
    for r in sorted(rs, key=lambda x: x['date']):
        o += [f"- {r['date']} labels {r['label_ids_json']} From {r['from_name']} <{r['from_email']}> To {r['to_json']} Cc {r['cc_json']} Subject: {r['subject']}", '  > ' + r['body_text'].replace('\r\n', '\n').replace('\n', '\n  > ')]
o.append('\n## Calendar')
for r in by.get('gcal.gcal_events', []):
    o.append(f"- `{r['event_id']}` cal {r['calendar_id']} {r['summary']} {r['start_ts']}–{r['end_ts']} organizer {r['organizer_email']} attendees {[a['email'] for a in J(r['attendees_json'])]} created {r['created']} updated {r['updated']}\n  description: {r['description']}")
o.append('\n## Linear comments')
for r in by.get('linear.linear_comments', []):
    o.append(f"- `{r['id']}` on {r['issue_id']} by {r['author_id']} {r['created_at']}: {r['body']}")
o.append('\n## Contacts')
for r in by.get('contacts.contacts', []):
    o.append(f"- `{r['contact_id']}` {r['first_name']} {r['last_name']} {r['job']} {r['email']}")
o.append('\n## UPDATE statements')
for x in items:
    if x['op'] != 'insert' and x['table'] != 'gmail.gmail_threads':
        o.append(f"- {x['table']}: {json.dumps({k: v for k, v in x.items() if k not in ('op', 'table', 'line')}, default=str)[:300]}")
(Path(__file__).parent / 'seeded_records.md').write_text('\n'.join(o) + '\n')
print(len(rows), 'rows', sum(len(x) for x in o), 'chars')
