"""Ground-truth cohort for the Julia difficulty register (reads the Linear export; writes cohort.json)."""
import json, re
B = '/home/sumit/Downloads/OC/OC/'
d = json.load(open(B + 'HarmonyGames_Other_Services/Services_Data/linear/data.json'))
users = {u['id']: u['email'] for u in d['users']}
idmap = {i['id']: i['identifier'] for i in d['issues']}
CARD = re.compile(r'\b(difficulty|difficult|tier|tiers|tiering|enrage|enraged|blunder|cpm)\b', re.I)
AMEND = re.compile(r'\battack power\b', re.I)
rows = []
for i in d['issues']:
    if not i['identifier'].startswith('ZOM-'):
        continue
    t = i['title'] or ''
    m_card, m_am = bool(CARD.search(t)), bool(AMEND.search(t))
    if not (m_card or m_am):
        continue
    rows.append(dict(id=i['identifier'], n=i['number'], title=t, state=i['state_id'], created=i['created_at'],
                     completed=i['completed_at'], canceled=i['canceled_at'], updated=i['updated_at'],
                     assignee=users.get(i['assignee_id']), creator=users.get(i['creator_id']),
                     parent=idmap.get(i['parent_id']), by_card=m_card, by_amend=m_am and not m_card,
                     in_window='2025-04-21' <= i['created_at'][:10] <= '2025-08-31'))
rows.sort(key=lambda r: r['n'])
cohort = [r for r in rows if r['in_window'] and r['state'] != 'Duplicate']
json.dump({'all_matches': rows, 'cohort': [r['id'] for r in cohort]}, open(B + 'Task_Authoring-2/support/task_work/jl_difficulty/cohort.json', 'w'), indent=1)
for r in rows:
    flag = 'IN ' if r in cohort else 'out'
    print(flag, r['id'], r['state'][:8], r['created'][:10], 'amend' if r['by_amend'] else 'card ', 'P:' + str(r['parent']), 'U' + r['updated'][:10], '|', r['title'][:70])
print('cohort', len(cohort), 'card-only', sum(1 for r in cohort if r['by_card']), 'amend', sum(1 for r in cohort if r['by_amend']))
