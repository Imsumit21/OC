import json,sys,glob
TD='/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/07_Baseline_Trajectories/'
files=sorted(glob.glob(TD+'*.json'))
for f in files:
    n=f.split('run-')[1][0]
    d=json.load(open(f))
    calls=[];res={};model=set()
    for e in d:
        if e.get('type')=='assistant':
            model.add(e['message'].get('model'))
            for c in e['message'].get('content',[]):
                if c.get('type')=='tool_use': calls.append((c['id'],c['name'].replace('mcp__hg__',''),c['input']))
        if e.get('type')=='user':
            cont=e['message'].get('content')
            if isinstance(cont,list):
                for c in cont:
                    if isinstance(c,dict) and c.get('type')=='tool_result':
                        r=c.get('content'); res[c['tool_use_id']]=r if isinstance(r,str) else json.dumps(r,ensure_ascii=False)
    out=open(f'run{n}.ledger.txt','w')
    out.write(f'run {n} models {model} calls {len(calls)}\n')
    for i,(cid,t,inp) in enumerate(calls,1):
        if t in ('linear_list_comments','linear_create_comment','linear_update_issue'): 
            out.write(f'{i:3} {t} {json.dumps(inp,ensure_ascii=False)[:90]}\n'); continue
        r=(res.get(cid) or '').replace('\n',' ')
        out.write(f'{i:3} {t} {json.dumps(inp,ensure_ascii=False)[:260]}\n      -> {r[:300]}\n')
    print(n,len(calls),model)
