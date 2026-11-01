import itertools,statistics as st,sys
sys.path.insert(0,'/home/sumit/Downloads/OC/OC/Task_Authoring-2/tools')
import difficulty_stats as ds
R=lambda a,b:set(range(a,b+1))
B={'B0':[{},{},{},{'T':1},{'T':1},{'C':1},{'T':1,'C':1}],
   'B1':[{'T':1,'P':R(37,48)},{'T':1,'P':R(38,41)},{},{'T':1},{'T':1},{'T':1,'C':1}],
   'B2':[{'T':1,'P':{54}},{},{'P':R(37,41)},{'P':R(37,42)},{},{},{'T':1,'C':1}]}
def found(h,f):
    k,a=f
    return (k in h) if k in('T','C') else a in h.get('P',set())
def rubric(design,h,model):
    f={k:found(h,v) for k,v in design.items()}
    flips=[k for k in f if k!='A']
    r=[]
    if 'A' in f: r+=[('A_excl',3,f['A']),('A_rowset',3,f['A'])]
    r+=[('dm_count',5,all(f.values())),('dm_list',3,all(f[k] for k in flips))]
    for k in flips: r+=[(k+'_N',3,f[k]),(k+'_todo',3,f[k])]
    if model=='compact':
        r+=[('other_status',5,True),('other_todo',3,True),('folder',3,True),('share',3,True),('dmdest',1,True)]
    else: # verbose: per-ticket always-pass rows
        r+=[('st%d'%i,3,True) for i in range(13)]+[('td%d'%i,3,True) for i in range(7)]+[('folder',3,True),('share',3,True),('dmdest',1,True),('leonard_reply',1,True)]
    return r
def run(design,model):
    res={}
    for b,runs in B.items():
        samples=[runs] if len(runs)==6 else [list(c) for c in itertools.combinations(runs,6)]
        for si,s in enumerate(samples):
            rows=[rubric(design,h,model) for h in s]
            data={'task_type':'long-horizon','rubrics':[{'id':n,'weight':w,'valid':True} for n,w,_ in rows[0]],
                  'rollouts':[{'id':f'run-{i+1}','status':'completed','tool_calls':200,'results':{n:p for n,_,p in r}} for i,r in enumerate(rows)]}
            out=ds.compute(data); g=out['gates']
            v=lambda k:g[k]['verdict'].split(' ')[0]
            res.setdefault(b,[]).append((g['avg_weighted_pass']['value'] if 'avg_weighted_pass' in g else '', v('per_rollout_sd') if 'per_rollout_sd' in g else '', ))
            ok=all(x['verdict'].startswith(('PASS','NON-FAIL')) for x in g.values())
            print('  %s s%d %s | %s'%(b,si,'ALLPASS' if ok else 'FAIL',' ; '.join(f"{k}:{x['value']}={x['verdict'][:22]}" for k,x in g.items() if k not in('errored_runs','horizon'))))
designs={
 'cur  A,B,537@46':{'A':('T',0),'B':('C',0),'D':('P',46)},
 'D_a  A,B,C@39,537@46':{'A':('T',0),'B':('C',0),'C':('P',39),'D':('P',46)},
 'D_b  A,B,C@39':{'A':('T',0),'B':('C',0),'C':('P',39)},
}
for m in ('compact','verbose'):
  for name,d in designs.items():
    print('##',m,name); run(d,m)
