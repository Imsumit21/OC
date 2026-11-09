#!/usr/bin/env python3
"""Spot-decode one realistic correct run per selector kind through tools/surface_grader (decode + grade). Writes nothing but stdout."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'Task_Authoring/tools')); sys.path.insert(0, str(ROOT / 'Task_Authoring/task_inputs/Working_Files/solver'))
import surface_grader as sg
import gradable_surface as gs
import solver as S
W = ROOT / 'Task_Authoring/task_inputs/Working_Files'
surface = gs.load(W / '01_Gradable_Surface.json')
truth = json.load(open(W / 'solver/truth.json'))
rows = {k: v for k, v in truth.items() if v['Status']}
money = (sys.argv[1] if len(sys.argv) > 1 else 'plain') == 'money'
def cell(v, cur=True):
    if v is None: return ''
    return (f"${v:,}" if cur else f"{v:,}") if money else v
header = ['Publisher', 'Status', 'Advance', 'Monthly installs', '12-month value', 'Q4 cash']
grid = [header] + [[k, v['Status'], cell(v['Advance']), cell(v['Monthly installs'], False), cell(v['12-month value']), cell(v['Q4 cash'])] for k, v in rows.items()]
calls = [('gsheets_create_spreadsheet', {'title': 'DD publishing model', 'sheets': ['Publishers', 'Summary']}, {'spreadsheetId': 'S1'}),
         ('gsheets_values_update', {'spreadsheetId': 'S1', 'range': 'Publishers!A1:F27', 'values': grid}),
         ('gsheets_values_update', {'spreadsheetId': 'S1', 'range': 'Summary!A1:B3', 'values': [['Keep value', '$12,723.96'], ['First pick', 'Copperleaf Games'], ['Banked so far', '$0']]}),
         ('gdrive_move_file', {'fileId': 'S1', 'newParentId': S.I['dd_folder']})]
for st in ('Live', 'Withdrawn', 'Out on rights', 'Passed', 'Waiting on us', 'No reply'):
    calls.append(('trello_create_checklist', {'cardId': S.I['dd_card'], 'name': st}, {'id': 'CL' + st}))
    for k, v in rows.items():
        if v['Status'] == st:
            calls.append(('trello_create_check_item', {'checklistId': 'CL' + st, 'name': k}))
for k in sorted(k for k, v in rows.items() if 'card_new' in v['groups']):
    calls.append(('trello_create_card', {'idList': S.B.BD_LIST, 'name': f'F/up with {k}'}))
for c in (S.I['oakline_card'], S.I['sunfold_card']):
    calls.append(('trello_add_comment', {'cardId': c, 'text': 'Status: Live'}))
for k, v in rows.items():
    m = next(x for x in S.B.M if x['key'] == k)
    if 'contact_add' in v['groups']:
        p = m['person']
        calls.append(('contacts_add_new_contact', {'first_name': p[0], 'last_name': p[1], 'job': k, 'email': f"{p[0].lower()}@{m['dom'] or 'x'}"}))
    if 'reminder' in v['groups']:
        calls.append(('gcal_create_event', {'summary': f"{k} response date", 'start': v['Respond by'], 'end': v['Respond by']}))
    if 'organic_note' in v['groups']:
        calls.append(('gmail_create_draft', {'to': [f"{m['person'][0].lower()}@{m['dom']}"], 'subject': f'Domino Delights numbers for {k}', 'body': f"Hi {m['person'][0]}, one number the May one-pager didn't have: on organic traffic we see $0.50 D30 ARPI."}))
    if 'nudge' in v['groups']:
        calls.append(('gmail_create_draft', {'to': [f"partnerships@{m['dom']}"], 'subject': f'Domino Delights for {k}', 'body': f"Hi {k} team, checking whether Domino Delights is of interest."}))
reply = "Copperleaf Games goes first. It brings in $67,200 over 12 months and $32,000 in Q4. We've banked $0 so far."
calls.append(('gmail_reply_to_message', {'message_id': sys.argv[2] if len(sys.argv) > 2 else 'hub-message', 'reply_all': False, 'body': reply}))
if len(sys.argv) > 3 and sys.argv[3] == 'summary_first':
    calls[1], calls[2] = calls[2], calls[1]
if len(sys.argv) > 3 and sys.argv[3] == 'share':
    calls[1], calls[2] = calls[2], calls[1]
    calls.insert(4, ('gdrive_share_file', {'fileId': 'S1', 'email': 'leonard.hayes@harmonygames.co', 'role': 'reader'}))
d = sg.decode(sg._planted_run(calls), surface)
g = sg.grade(surface, truth, d)
res = g.get('slots', g)
items = res.items() if isinstance(res, dict) else [(x.get('id'), x) for x in res]
ok, bad = [], []
for sid, r in items:
    v = r.get('verdict') or r.get('status') or r.get('result') if isinstance(r, dict) else r
    (ok if str(v).upper() in ('PASS', 'TRUE', 'OK') or v is True else bad).append((sid, v))
print('slots', len(ok) + len(bad), 'pass', len(ok), 'calls', len(calls)); print('not pass:', bad)
