import json, sys
sys.path.insert(0, '.')
from hgread import read_many, hg
S='/private/tmp/claude-501/-Users-sumit-Source-OC/03f412d7-1226-4687-96da-a0d4194c9430/scratchpad'
items=[('linear','data.json','/teams/0')]
for p in (17,18,33,9): items.append(('linear','data.json',f'/users/{p}'))
for p in list(range(578,594)): items.append(('linear','data.json',f'/issues/{p}'))
items.append(('trello','data.json','/boards/4'))
for p in range(39,47): items.append(('trello','data.json',f'/lists/{p}'))
items.append(('trello','data.json','/cards/750'))
for p in [41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63]: items.append(('slack','messages/C08R8CHB0QL/2025-08.json',f'/{p}'))
r=read_many(items)
json.dump({f'{k[0]}:{k[1]}#{k[2]}':v for k,v in r.items()},open(S+'/pull4.json','w'),ensure_ascii=False,indent=0)
for k,v in r.items():
    if k[0]=='linear' and '/issues' in k[2]:
        print(k[2],{a:v.get(a) for a in ('id','identifier','number','title','state_id','team_id','assignee_id','creator_id','created_at','completed_at','canceled_at','is_archived','archived_at','time_in_status_minutes')},(v.get('description') or '')[:120].replace('\n',' '), list(v.keys()) if k[2]=='/issues/590' else '')
    elif k[0]=='linear': print(k[2],json.dumps(v,ensure_ascii=False)[:1500])
    elif k[0]=='trello': print(k[2],json.dumps(v,ensure_ascii=False)[:1800])
    else:
        print(k[2],v.get('ts'),v.get('user'),v.get('thread_ts'),repr(v.get('text'))[:250],[f.get('name') for f in v.get('files') or []])
