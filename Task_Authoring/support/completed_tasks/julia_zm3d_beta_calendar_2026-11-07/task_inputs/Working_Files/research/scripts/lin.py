import json,sys
d=json.load(open('raw/linear_issues.json'))
idx={x['identifier']:x for x in d}
for k in sys.argv[1:]:
    x=idx.get(k)
    if not x: print(k,'MISSING'); continue
    print('%s | %s | %s | created %s | done %s | labels %s'%(x['identifier'],x['state_id'],x['title'],x['created_at'][:10],(x.get('completed_at') or '')[:10],','.join(x.get('labels') or [])))
    print('    assignee',x.get('assignee_id'),'| team',x.get('team_id'),'| prio',x.get('priority'),'| proj',x.get('project_id'))
    desc=(x.get('description') or '').replace('\n',' ')
    print('    DESC:',desc[:700])
