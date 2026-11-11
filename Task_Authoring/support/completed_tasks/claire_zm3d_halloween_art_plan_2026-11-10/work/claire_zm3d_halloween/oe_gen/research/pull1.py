import json, sys
sys.path.insert(0, '.')
from hgread import read_many
S='/private/tmp/claude-501/-Users-sumit-Source-OC/03f412d7-1226-4687-96da-a0d4194c9430/scratchpad'
items=[]
for p in range(21,39): items.append(('slack','messages/C06DJBJL798/2025-08.json',f'/{p}'))
for p in (120,121,122): items.append(('slack','messages/C08R8CHB0QL/2025-09.json',f'/{p}'))
for p in (466,467,468,469,470,471,472): items.append(('slack','messages/C0880U9751A/2025-09.json',f'/{p}'))
items.append(('slack','messages/C05KNDCHAAG/2025-10.json','/0'))
for p in (1671,1672,1673): items.append(('slack','messages/C05433XK267/2025-07.json',f'/{p}'))
for p in (903,904,911): items.append(('slack','messages/C0880U9751A/2025-07.json',f'/{p}'))
items.append(('slack','messages/C0880U9751A/2025-09.json','/286'))
items.append(('slack','messages/C06DJBJL798/2025-09.json','/0'))
for p in (45,64,65): items.append(('slack','messages/C08R8CHB0QL/2025-08.json',f'/{p}'))
r=read_many(items)
json.dump({f'{k[1]}#{k[2]}':v for k,v in r.items()},open(S+'/pull1.json','w'),ensure_ascii=False,indent=0)
for k,v in r.items():
    print(k[1],k[2],v.get('ts'),v.get('user'),v.get('thread_ts'),v.get('reply_count'),len(json.dumps(v)),repr((v.get('text') or '')[:110]))
