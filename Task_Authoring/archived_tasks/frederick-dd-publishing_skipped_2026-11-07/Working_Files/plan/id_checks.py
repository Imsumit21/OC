#!/usr/bin/env python3
"""Writes plan/id_checks_sql.json and plan/slack_ids.json from the SQL (each minted id, by its base collection)."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'Task_Authoring/tools'))
from base_check import parse_sql
P = Path(__file__).parent
rows = [x for x in parse_sql((ROOT / 'Task_Authoring/task_inputs/01_Universe_Inject.sql').read_text()) if x['op'] == 'insert']
def vals(t, k): return sorted({str(x['row'][k]) for x in rows if x['table'] == t})
checks = [
    dict(id='drive', service='gdrive', file='data.json', pointer='/drive_files', field='id', values=vals('gdrive.drive_files', 'id')),
    dict(id='gcal', service='gcal', file='data.json', pointer='/events', field='id', values=vals('gcal.gcal_events', 'event_id')),
    dict(id='trello_cards', service='trello', file='data.json', pointer='/cards', field='id', values=vals('trello.trello_cards', 'id')),
    dict(id='trello_actions', service='trello', file='data.json', pointer='/actions', field='id', values=vals('trello.trello_actions', 'id')),
    dict(id='contacts', service='contacts', file='contacts.json', pointer='/contacts', field='id', values=vals('contacts.contacts', 'contact_id')),
    dict(id='linear_comments', service='linear', file='data.json', pointer='/comments', field='id', values=vals('linear.linear_comments', 'id')),
]
json.dump({'checks': checks}, open(P / 'id_checks_sql.json', 'w'), indent=1)
json.dump(vals('slack.slack_messages', 'id'), open(P / 'slack_ids.json', 'w'))
print({c['id']: len(c['values']) for c in checks}, 'slack', len(vals('slack.slack_messages', 'id')))
