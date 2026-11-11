import json, sys
sys.path.insert(0, '.')
from hgread import read_many, hg
S='/private/tmp/claude-501/-Users-sumit-Source-OC/03f412d7-1226-4687-96da-a0d4194c9430/scratchpad'
items=[]
for p in range(46,64): items.append(('slack','messages/D05S58U4SAK/2025-08.json',f'/{p}'))
for p in list(range(33,40))+list(range(64,71)): items.append(('slack','messages/D05S58U4SAK/2025-09.json',f'/{p}'))
r=read_many(items,page=60000,batch_size=8)
json.dump({f'{k[1]}#{k[2]}':v for k,v in r.items()},open(S+'/pull6.json','w'),ensure_ascii=False,indent=0)
for k,v in r.items():
    print(k[1].split('messages/')[1],k[2],v.get('ts'),v.get('user'),v.get('thread_ts'),repr(v.get('text'))[:330],[(f.get('id'),f.get('name'),f.get('duration_ms')) for f in v.get('files') or []])
req={'items':[{'id':p.strip('/'),'service':'linear','file':'data.json','pointer':p,'max_chars':80} for p in ('/workflow_states','/states','/workflowStates','/team_states')]}
x=hg('get-many','--request','-','--compact',stdin=json.dumps(req))
print({k:v.get('error') for k,v in x['items'].items()})
