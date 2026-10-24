import json,glob,re,collections
L=json.load(open('HarmonyGames_Other_Services/Services_Data/linear/data.json'))
G=json.load(open('HarmonyGames_GitHub/Services_Data/github/data.json'))
users={u['id']:u.get('name') for u in L['users']}
openst={'Todo','Backlog','Bugs','In Progress','PR','In Review','In Validation','Validation','Regression'}
coh=[i for i in L['issues'] if i['state_id'] in openst and i['team_id'] in ('team_ENG','team_ZOM') and (i['state_id'] in ('Bugs','Regression') or 'Bug' in i['labels'])]
keys={i['identifier'] for i in coh}
pat=re.compile(r'\b((?:ENG|ZOM)[-_ ]?\d{2,4})\b',re.I)
def norm(k): 
    k=k.upper().replace('_','-').replace(' ','-')
    if '-' not in k: k=k[:3]+'-'+k[3:]
    return k
prmap=collections.defaultdict(list)
for p in G['pull_requests']:
    for m in pat.finditer(' '.join([p['title'] or '',p['head_ref'] or '',p['body'] or ''])):
        k=norm(m.group(1))
        if k in keys: prmap[k].append(p['id']+('M' if p['merged'] else ('O' if p['state']=='open' else 'C')))
sl=collections.defaultdict(list)
chs={c['id']:c.get('name') for c in json.load(open('HarmonyGames_Other_Services/Services_Data/slack/channels.json'))}
for f in glob.glob('HarmonyGames_Other_Services/Services_Data/slack/messages/*/*.json'):
    ch=f.split('/')[-2]
    try: d=json.load(open(f))
    except: continue
    for m in d:
        t=m.get('text') or ''
        for mm in pat.finditer(t):
            k=norm(mm.group(1))
            if k in keys: sl[k].append((chs.get(ch,ch),m.get('ts'),'R' if m.get('thread_ts') and m.get('thread_ts')!=m.get('ts') else ('P' if m.get('reply_count') else 'S')))
out=[]
for i in sorted(coh,key=lambda x:(x['team_id'],x['number'])):
    k=i['identifier']
    out.append(dict(key=k,state=i['state_id'],prio=i['priority'],labels=i['labels'],assignee=users.get(i['assignee_id'],i['assignee_id']),created=i['created_at'],updated=i['updated_at'],title=i['title'],desc=(i.get('description') or ''),parent=i.get('parent_id'),rel=i.get('relations'),prs=sorted(set(prmap.get(k,[]))),slack=sl.get(k,[])))
json.dump(out,open('Task_Authoring/support/examples/sample_task_01/work/cohort.json','w'),indent=1)
print(len(out))
for o in out:
    print(o['key'],o['state'],o['prio'],o['labels'][:3],(o['assignee'] or '')[:18],o['created'][:10],'desc',len(o['desc']),'PR',o['prs'][:3],'SL',[(a,b,c) for a,b,c in o['slack'][:3]])
