import json, sys
sys.path.insert(0, '.')
from hgread import read_many, hg
S='/private/tmp/claude-501/-Users-sumit-Source-OC/03f412d7-1226-4687-96da-a0d4194c9430/scratchpad'
items=[]
for p in range(24,50): items.append(('slack','messages/D05UDNHAPL2/2025-08.json',f'/{p}'))
for f,ps in [('messages/D07GJJBFHA5/2025-08.json',[766]),('messages/D07GJJBFHA5/2025-09.json',[143]),
             ('messages/C07C2866011/2025-08.json',[494,495]),('messages/C08R8CHB0QL/2025-08.json',[219]),('messages/C08R8CHB0QL/2025-09.json',[128]),
             ('messages/C0880U9751A/2025-08.json',[172,173]),('messages/C0880U9751A/2025-09.json',[402]),
             ('messages/C06DJBJL798/2025-08.json',[7,9]),('messages/D04UGG61DUM/2025-08.json',[253,298,303,312,316,318,321,331]),('channels.json',[139])]:
    for p in ps: items.append(('slack',f,f'/{p}'))
r=read_many(items)
json.dump({f'{k[1]}#{k[2]}':v for k,v in r.items()},open(S+'/pull3.json','w'),ensure_ascii=False,indent=0)
for k,v in r.items():
    if k[1].startswith('channels'):
        print(k, {a:(b if not isinstance(b,(list,dict)) else f'<{len(b)}>') for a,b in v.items()}, 'EMPLOYEE_0009_SLACK_ID' in v['members'])
        continue
    fs=[f.get('name') for f in (v.get('files') or [])]
    print(k[1].split('messages/')[1],k[2],v.get('ts'),v.get('user'),v.get('thread_ts'),repr(v.get('text'))[:420],fs)
