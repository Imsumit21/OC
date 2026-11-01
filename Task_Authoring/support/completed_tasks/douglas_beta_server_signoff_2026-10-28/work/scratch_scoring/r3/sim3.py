exec(open('/tmp/claude-1000/-home-sumit-Downloads-OC-OC/64ffea75-2ed7-4766-a065-99d4d43b34de/scratchpad/r3/sim2.py').read().split('designs={')[0])
import collections
def summary(design,model):
    tot=0;ok=0;fails=collections.Counter();avgs=[];sds=[]
    for b,runs in B.items():
        samples=[runs] if len(runs)==6 else [list(c) for c in itertools.combinations(runs,6)]
        for s in samples:
            rows=[rubric(design,h,model) for h in s]
            data={'task_type':'long-horizon','rubrics':[{'id':n,'weight':w,'valid':True} for n,w,_ in rows[0]],
                  'rollouts':[{'id':f'run-{i+1}','status':'completed','tool_calls':200,'results':{n:p for n,_,p in r}} for i,r in enumerate(rows)]}
            g=ds.compute(data)['gates']; tot+=1
            bad=[k for k,x in g.items() if not x['verdict'].startswith(('PASS','NON-FAIL'))]
            if not bad: ok+=1
            for k in bad: fails[k]+=1
            sc=[sum(w for _,w,p in r if p)/sum(w for _,w,_ in r) for r in rows]
            avgs.append(st.mean(sc)); sds.append(st.pstdev(sc))
    print('  %-8s pass %d/%d  avg %.2f-%.2f  sd %.3f-%.3f  fails %s'%(model,ok,tot,min(avgs),max(avgs),min(sds),max(sds),dict(fails)))
designs={
 'D_b A,B,C@39':{'A':('T',0),'B':('C',0),'C':('P',39)},
 'E1 A,B,C@38,C2@39':{'A':('T',0),'B':('C',0),'C':('P',38),'C2':('P',39)},
 'E2 A,B,B2,C@38,C2@39':{'A':('T',0),'B':('C',0),'B2':('C',0),'C':('P',38),'C2':('P',39)},
 'E3 A,B,B2,C@39':{'A':('T',0),'B':('C',0),'B2':('C',0),'C':('P',39)},
 'E4 A,B,C@39,537@46':{'A':('T',0),'B':('C',0),'C':('P',39),'D':('P',46)},
}
for name,d in designs.items():
    print('##',name)
    for m in ('compact','verbose'): summary(d,m)
