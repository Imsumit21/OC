"""Round-7 answer key: the 23 register rows with Robert's three columns, from truth.json (round 4) and Linear data.json."""
import datetime
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
_T = json.load(open(os.path.join(HERE, '..', 'truth.json')))
_L = json.load(open(os.path.join(ROOT, 'HarmonyGames_Other_Services', 'Services_Data', 'linear', 'data.json')))
_users = {u['id']: u for u in _L['users']}
_iss = {x['identifier']: x for x in _L['issues'] if (x.get('identifier') or '').startswith('ZOM-')}
PRIO = {1: 'Urgent', 2: 'High', 3: 'Medium', 4: 'Low'}
key = lambda k: int(k.split('-')[1])

ROWS = []
for r in _T['rows']:
    if not r['member'] or r['id'] == 'ZOM-295':      # round 7: Blake's 'not tiers' on match3d#271
        continue
    x = _iss[r['id']]
    u = _users[x['assignee_id']]
    c = x.get('completed_at')
    utc = c[:10] if c else ''
    pt = (datetime.datetime.fromisoformat(c.replace('Z', '+00:00')) - datetime.timedelta(hours=7)).date().isoformat() if c else ''
    ROWS.append(dict(id=r['id'], title=x['title'], state=r['state'], status=r['status'], replaced_by=r['replaced_by'],
                     assignee=u['name'], completed_at=c, done_pt=pt, done_utc=utc, priority=x['priority'],
                     priority_label=PRIO[x['priority']]))
ROWS.sort(key=lambda r: key(r['id']))
assert len(ROWS) == 23
by = lambda s: [r['id'] for r in ROWS if r['status'] == s]
LIVE, EO, NS, REP = by('Live'), by('Editor only'), by('Not shipped'), by('Replaced')
assert (len(LIVE), len(EO), len(NS), len(REP)) == (15, 4, 3, 1)
PT_DIFF = [r['id'] for r in ROWS if r['done_pt'] != r['done_utc']]
assert PT_DIFF == ['ZOM-200', 'ZOM-274', 'ZOM-282'], PT_DIFF
OFF = {'ZOM-30': 'F2', 'ZOM-49': 'F2', 'ZOM-50': 'F2', 'ZOM-161': 'F2', 'ZOM-262': 'F2', 'ZOM-275': 'F2',
       'ZOM-162': 'F3', 'ZOM-163': 'F3', 'ZOM-201': 'F3', 'ZOM-250': 'F3', 'ZOM-258': 'F7', 'ZOM-312': 'F16', 'ZOM-295': 'F25'}


def row_text(r):
    done = r['done_pt'] or 'blank (never done)'
    if r['done_pt'] and r['done_pt'] != r['done_utc']:
        done += f" (UTC {r['done_utc']})"
    s = f"{r['id']} {r['state']} {r['status']}"
    if r['replaced_by']:
        s += f" by {r['replaced_by']}"
    return s + f", assignee {r['assignee']}, done {done}, priority {r['priority']} {r['priority_label']}"


if __name__ == '__main__':
    for r in ROWS:
        print(row_text(r))
    print(len(LIVE), LIVE)
