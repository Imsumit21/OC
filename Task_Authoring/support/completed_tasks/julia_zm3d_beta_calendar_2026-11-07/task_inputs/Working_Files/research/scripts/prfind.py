import json,sys
d=json.load(open('raw/gh_prs.json'))
term=sys.argv[1].lower()
repo=sys.argv[2] if len(sys.argv)>2 else None
out=[]
for x in d:
    if repo and x['_repo']!=repo: continue
    if term in (x['title']+' '+(x.get('body') or '')+' '+(x.get('head_ref') or '')).lower(): out.append(x)
out.sort(key=lambda x:x['created_at'])
for x in out:
    print('%s#%s | %s | merged=%s %s | c%s'%(x['_repo'],x['number'],x['title'],x['merged'],(x.get('merged_at') or '')[:10],x['created_at'][:10]))
print('TOTAL',len(out))
