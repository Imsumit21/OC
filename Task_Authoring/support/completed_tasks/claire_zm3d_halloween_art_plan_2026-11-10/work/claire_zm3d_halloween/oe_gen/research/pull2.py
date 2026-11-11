import json, sys
sys.path.insert(0, '.')
from hgread import read_many, hg
S='/private/tmp/claude-501/-Users-sumit-Source-OC/03f412d7-1226-4687-96da-a0d4194c9430/scratchpad'
items=[]
for p in range(1660,1674): items.append(('slack','messages/C05433XK267/2025-07.json',f'/{p}'))
for p in (0,3,6,7,8,9,13,14,19,20,23,88,90): items.append(('slack','users.json',f'/{p}'))
for p in (25,38,57,108,129,590): items.append(('slack','channels.json',f'/{p}'))
r=read_many(items)
json.dump({f'{k[1]}#{k[2]}':v for k,v in r.items()},open(S+'/pull2.json','w'),ensure_ascii=False,indent=0)
for k,v in r.items():
    if k[1].startswith('messages'):
        a=v.get('attachments') or []
        print(k[2],v.get('ts'),v.get('user'),v.get('subtype'),repr((a[0].get('fallback') if a else v.get('text'))[:400]))
    elif k[1]=='users.json':
        print(k[2],json.dumps(v,ensure_ascii=False))
    else:
        m=v.get('members') or v.get('member_ids') or []
        print(k[2],json.dumps({a:(b if not isinstance(b,(list,dict)) else f'<{type(b).__name__} {len(b)}>') for a,b in v.items()},ensure_ascii=False)[:700])
