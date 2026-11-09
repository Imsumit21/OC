import json,glob,os,re
T='/home/sumit/Desktop/OC/Task_Authoring/task_inputsK'
FILES={f'run-{i}':glob.glob(f'{T}/07_Baseline_Trajectories/trajectory-run-{i} *.json')[0] for i in range(1,7)}
FILES['precheck']=f'{T}/Run1_trajectory.json'
def load(path):
    ev=json.load(open(path))
    calls=[];byid={}
    for n,e in enumerate(ev):
        if not isinstance(e,dict): continue
        m=e.get('message') or {}
        c=m.get('content')
        if not isinstance(c,list): continue
        for b in c:
            if not isinstance(b,dict): continue
            if b.get('type')=='tool_use':
                name=b.get('name','')
                short=name.split('__')[-1]
                rec={'n':n,'id':b.get('id'),'tool':short,'input':b.get('input') or {},'result':None,'err':None}
                calls.append(rec);byid[rec['id']]=rec
            elif b.get('type')=='tool_result':
                r=byid.get(b.get('tool_use_id'))
                if r is not None:
                    cc=b.get('content')
                    if isinstance(cc,list):
                        cc='\n'.join(x.get('text','') if isinstance(x,dict) else str(x) for x in cc)
                    r['result']=cc; r['err']=b.get('is_error')
    final=[e for e in ev if isinstance(e,dict) and e.get('type')=='result']
    return calls,(final[-1].get('result') if final else None),ev
