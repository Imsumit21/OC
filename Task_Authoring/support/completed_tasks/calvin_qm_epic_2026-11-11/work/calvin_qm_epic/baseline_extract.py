import json,collections,sys
out={}
for n in range(1,7):
    d=json.load(open(f'07_Baseline_Trajectories/trajectory-run-{n}.json'))
    calls=[]
    for e in d:
        if e.get('type')!='assistant': continue
        sub=e.get('parent_tool_use_id') is not None
        for c in e['message'].get('content',[]):
            if c.get('type')=='tool_use': calls.append({'name':c['name'].split('__')[-1],'input':c['input'],'sub':sub})
    out[n]=calls
    cnt=collections.Counter(c['name'] for c in calls)
    writes={k:v for k,v in cnt.items() if any(w in k for w in('create','update','send','move','share','comment','batch'))}
    print(n,'calls',len(calls),'sub',sum(c['sub'] for c in calls),'writes',sum(writes.values()),dict(writes))
    res=[e for e in d if e.get('type')=='result']
    print('   result:',str(res[-1].get('result'))[:300].replace('\n',' ') if res else None)
json.dump(out,open('Working_Files/run_forensics/rev3/baseline/calls.json','w'))
