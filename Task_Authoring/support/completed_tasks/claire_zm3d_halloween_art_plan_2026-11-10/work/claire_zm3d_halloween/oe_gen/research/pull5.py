import json, sys, collections
sys.path.insert(0, '.')
from hgread import read_many
S='/private/tmp/claude-501/-Users-sumit-Source-OC/03f412d7-1226-4687-96da-a0d4194c9430/scratchpad'
d=json.load(open(S+'/clev.json'))
ptrs=[m['pointer'].rsplit('/',1)[0] for m in d['matches']['claire.morgan@harmonygames.co']]
r=read_many([('gcal','data.json',p) for p in ptrs],page=12000,batch_size=50)
ev={k[2]:v for k,v in r.items()}
json.dump(ev,open(S+'/clev_full.json','w'),ensure_ascii=False)
print(len(ev))
def st(e):
    s=e.get('start') or {}
    return s.get('dateTime') or s.get('date') or ''
print('latest starts',sorted(st(e) for e in ev.values())[-8:])
print('status',collections.Counter(e.get('status') for e in ev.values()))
rec=[(p,e) for p,e in ev.items() if e.get('rrule')]
print('recurring masters',len(rec))
for p,e in sorted(rec,key=lambda x:st(x[1])):
    print(p,st(e),e.get('summary'),e.get('rrule'),e.get('status'),e.get('recurring_event_id'))
print('---- start >= 2025-09-20')
for p,e in sorted(ev.items(),key=lambda x:st(x[1])):
    if st(e)>='2025-09-20': print(p,st(e),e.get('summary'),e.get('status'),e.get('rrule'),e.get('recurring_event_id'))
print('---- summary contains review/halloween/zm3d/ua/art')
c=collections.Counter(e.get('summary') for e in ev.values())
print([ (k,v) for k,v in c.most_common() if any(w in (k or '').lower() for w in('review','hallow','zm','zombie','seasonal'))])
