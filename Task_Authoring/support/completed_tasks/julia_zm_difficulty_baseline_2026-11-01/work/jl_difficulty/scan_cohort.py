import json,re,collections,sys
B='/home/sumit/Downloads/OC/OC/'
d=json.load(open(B+'HarmonyGames_Other_Services/Services_Data/linear/data.json'))
g=json.load(open(B+'HarmonyGames_GitHub/Services_Data/github/data.json'))
users={u['id']:u['name'].split('@')[0] for u in d['users']}
repos={r['id']:r['name'] for r in g['repositories']}
kw=re.compile(r'difficult|tier|cpm|\bbot|simulat|level editor|algo level|enrage|rage|blunder|balanc|win ?rate|winrate|attack power',re.I)
c=[i for i in d['issues'] if i['identifier'].startswith('ZOM') and i['created_at']<'2025-10-01' and kw.search(i['title']+' '+(i['description'] or '')[:400])]
ids={i['identifier'] for i in c}
att=collections.defaultdict(list)
for a in d['attachments']:
    if a['issue_identifier'] in ids: att[a['issue_identifier']].append(a['kind']+':'+(a['filename'] or '')[:30])
pr_by=collections.defaultdict(list)
for p in g['pull_requests']:
    txt=(p['title'] or '')+' '+(p['head_ref'] or '')+' '+(p['body'] or '')
    for m in set(re.findall(r'ZOM-?(\d+)',txt,re.I)):
        k='ZOM-'+m
        if k in ids: pr_by[k].append(f"{repos[p['repo_id']]}#{p['number']}({'M'+p['merged_at'][:10] if p['merged_at'] else p['state']})")
out=[]
for i in sorted(c,key=lambda x:x['number']):
    out.append(dict(id=i['identifier'],state=i['state_id'],created=i['created_at'],completed=i['completed_at'],canceled=i['canceled_at'],updated=i['updated_at'],
      assignee=users.get(i['assignee_id']),creator=users.get(i['creator_id']),parent=i['parent_id'],labels=i['labels'],title=i['title'],
      desc=(i['description'] or ''),links=i['links'],relations=i['relations'],att=att.get(i['identifier'],[]),prs=pr_by.get(i['identifier'],[])))
json.dump(out,open(B+'Task_Authoring-2/support/task_work/jl_difficulty/candidates.json','w'),indent=1)
idmap={i['id']:i['identifier'] for i in d['issues']}
for o in out:
    print(o['id'],o['state'][:6],o['created'][:10],(o['completed'] or '')[:10],'U'+o['updated'][:10],(o['assignee'] or '-')[:10],'|',o['title'][:55],'|P:',idmap.get(o['parent'],''),'|rel:',[ (r.get('type'),idmap.get(r.get('related_issue_id'),r.get('related_issue_id'))) for r in (o['relations'] or [])][:3],'|links',len(o['links'] or []),'|att',len(o['att']),'|prs',o['prs'][:4],'|dlen',len(o['desc']))
