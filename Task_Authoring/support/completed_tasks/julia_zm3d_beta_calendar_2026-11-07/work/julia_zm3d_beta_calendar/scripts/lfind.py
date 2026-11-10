import json,sys,re
d=json.load(open('raw/linear_issues.json'))
term=sys.argv[1].lower()
team=sys.argv[2] if len(sys.argv)>2 else None
out=[]
for x in d:
    if team and x['team_id']!=team: continue
    blob=(x['identifier']+' '+(x.get('title') or '')+' '+(x.get('description') or '')).lower()
    if term in blob: out.append(x)
out.sort(key=lambda x:x['created_at'])
for x in out:
    print('%s | %s | %s | c%s d%s'%(x['identifier'],x['state_id'],x['title'],x['created_at'][:10],(x.get('completed_at') or '')[:10]))
print('TOTAL',len(out))
