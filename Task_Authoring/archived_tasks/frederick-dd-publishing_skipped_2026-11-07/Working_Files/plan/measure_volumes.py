#!/usr/bin/env python3
"""Human-time volumes through tools/hg.py, persona view. Writes plan/humantime_volumes.json."""
import datetime as D, json, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'Task_Authoring/tools'))
from base_check import parse_sql
HG = ['python3', '-B', 'Task_Authoring/tools/hg.py', 'search']
def run(*a):
    r = subprocess.run(HG + list(a), cwd=ROOT, capture_output=True, text=True, timeout=500)
    try:
        return json.loads(r.stdout)
    except ValueError:
        print('hg.py returned no JSON for', a[:4], (r.stderr or r.stdout)[-160:], file=sys.stderr)
        return {}
PT = D.timezone(D.timedelta(hours=-7))
out = {}
d = run('files', 'gmail', 'threads/frederick@harmonygames.co_', '--limit', '6000')
s = int(D.datetime(2025, 4, 1, tzinfo=PT).timestamp() * 1000); e = int(D.datetime(2025, 10, 1, tzinfo=PT).timestamp() * 1000)
ids = [int(m.group(1)) >> 20 for x in d['matches'] if (m := re.search(r'_(\d{15,})\.json', x['path']))]
out['gmail_threads_total'] = len(ids); out['gmail_threads_window'] = sum(s <= t < e for t in ids)
months = ['2025-04', '2025-05', '2025-06', '2025-07', '2025-08', '2025-09']
for ch, name in [('C07C2866011', 'executives'), ('C096HFA5Z8W', 'bridge-pitch'), ('C069FF9Q57S', 'analytics'), ('D05S58U4SAK', 'dm_leonard')]:
    tot = {}
    for mth in months:
        q = run('search', 'slack', '.', '--file', f'messages/{ch}/{mth}.json', '--key', 'ts', '--limit', '20000', '--compact')
        tot[mth] = len(q.get('matches') or [])
    out[name] = tot
c = run('search', 'contacts', '@', '--key', 'email', '--limit', '1000', '--compact'); out['contacts_with_email'] = len(c.get('matches') or [])
c = run('search', 'contacts', '.', '--key', 'contact_id', '--limit', '1000', '--compact'); out['contacts_probe'] = len(c.get('matches') or [])
q = run('search', 'snowflake', 'domino_delights', '--file', 'snowflake.json', '--pointer', '/tables/12/rows', '--limit', '20000', '--compact')
rows = q.get('matches') or []
out['rev_daily_dd_rows_all'] = len(rows)
rows_sql = [x for x in parse_sql((ROOT / 'Task_Authoring/task_inputs/01_Universe_Inject.sql').read_text()) if x['op'] == 'insert']
F = 'frederick.stone@harmonygames.co'
out['seeded'] = {'threads_fred': sum(1 for x in rows_sql if x['table'] == 'gmail.gmail_threads' and x['row']['user_email'] == F),
                 'messages_fred': sum(1 for x in rows_sql if x['table'] == 'gmail.gmail_messages' and x['row']['user_email'] == F),
                 'slack': sum(1 for x in rows_sql if x['table'] == 'slack.slack_messages'), 'docs': sum(1 for x in rows_sql if x['table'] == 'gdocs.docs_documents'),
                 'contacts': sum(1 for x in rows_sql if x['table'] == 'contacts.contacts')}
json.dump(out, open(Path(__file__).parent / 'humantime_volumes.json', 'w'), indent=1)
print(json.dumps(out))
