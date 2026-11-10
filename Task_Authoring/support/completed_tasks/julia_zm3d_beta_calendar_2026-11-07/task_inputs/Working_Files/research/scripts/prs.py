import json,sys
d=json.load(open('raw/gh_prs.json'))
repo=sys.argv[1]
out=[x for x in d if x['_repo']==repo]
out.sort(key=lambda x:x['number'])
for x in out:
    print('#%s %s | %s | merged=%s %s | %s -> %s'%(x['number'],x['state'],x['title'],x['merged'],(x.get('merged_at') or '')[:10],x['created_at'][:10],x.get('head_ref')))
print('TOTAL',len(out))
