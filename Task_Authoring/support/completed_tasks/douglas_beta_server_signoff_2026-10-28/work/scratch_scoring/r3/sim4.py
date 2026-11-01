import itertools,statistics as st,sys,collections
sys.path.insert(0,'/home/sumit/Downloads/OC/OC/Task_Authoring-2/tools')
import difficulty_stats as ds
R=lambda a,b:set(range(a,b+1))
B={'B0':[{},{},{},{'T':1},{'T':1},{'C':1},{'T':1,'C':1}],
   'B1':[{'T':1,'P':R(37,48)},{'T':1,'P':R(38,41)},{},{'T':1},{'T':1},{'T':1,'C':1}],
   'B2':[{'T':1,'P':{54}},{},{'P':R(37,41)},{'P':R(37,42)},{},{},{'T':1,'C':1}]}
def found(h,f):
    k,a=f
    return (k in h) if k in('T','C') else a in h.get('P',set())
Y=['459','509','499','531','444','510']; N=['336','392','503','518','550','435','557','256']
def rubric(hidden,excl,h,model):
    # hidden: ticket->habit that flips it Y->N (or keeps N for 487/537 style)
    f={t:found(h,v) for t,v in hidden.items()}
    a=found(h,excl) if excl else True
    tickets=sorted(set(Y+N+list(hidden)))
    r=[]
    if model=='verbose':
        for t in tickets: r.append(('st'+t,3,f.get(t,True)))
        for t in [t for t in tickets if t in N or t in hidden]: r.append(('todo'+t,3,f.get(t,True)))
        r+=[('folder',3,True),('share',3,True),('dmdest',1,True),('leo',1,True),('cols',1,True)]
    else:
        for t in hidden: r+=[('st'+t,3,f[t]),('todo'+t,3,f[t])]
        r+=[('other_status',5,True),('other_todo',3,True),('folder',3,True),('share',3,True),('dmdest',1,True)]
    if excl: r.append(('excl',3,a))
    r+=[('dm_count',5,a and all(f.values())),('dm_list',3,all(f.values()))]
    return r
def summary(name,hidden,excl):
    for model in('compact','verbose'):
        tot=ok=0;fails=collections.Counter();avgs=[];sds=[]
        for b,runs in B.items():
            for s in ([runs] if len(runs)==6 else [list(c) for c in itertools.combinations(runs,6)]):
                rows=[rubric(hidden,excl,h,model) for h in s]
                data={'task_type':'long-horizon','rubrics':[{'id':n,'weight':w,'valid':True} for n,w,_ in rows[0]],
                      'rollouts':[{'id':f'run-{i+1}','status':'completed','tool_calls':200,'results':{n:p for n,_,p in r}} for i,r in enumerate(rows)]}
                g=ds.compute(data)['gates']; tot+=1
                bad=[k for k,x in g.items() if not x['verdict'].startswith(('PASS','NON-FAIL'))]
                ok+= not bad
                for k in bad: fails[k]+=1
                sc=[sum(w for _,w,p in r if p)/sum(w for _,w,_ in r) for r in rows]
                avgs.append(st.mean(sc)); sds.append(st.pstdev(sc))
        print('%-34s %-8s pass %2d/%d avg %.2f-%.2f sd %.3f-%.3f %s'%(name,model,ok,tot,min(avgs),max(avgs),min(sds),max(sds),dict(fails)))
T=('T',0);C=('C',0);P=lambda n:('P',n)
cands={
 'cur: 487C 537P46 +excl':({'487':C,'537':P(46)},T),
 'D_b: 487C 509P39 +excl':({'487':C,'509':P(39)},T),
 'E1: 487C 459P38 509P39 +excl':({'487':C,'459':P(38),'509':P(39)},T),
 'E2: 487C 499C 459P38 509P39 +excl':({'487':C,'499':C,'459':P(38),'509':P(39)},T),
 'E5: 487C 499C 459P38 509P39 531T +excl':({'487':C,'499':C,'459':P(38),'509':P(39),'531':T},T),
 'E6: 487C 459P38 509P39 531T +excl':({'487':C,'459':P(38),'509':P(39),'531':T},T),
 'E7: 487C 499C 509P39 531T +excl':({'487':C,'499':C,'509':P(39),'531':T},T),
 'E8: 487C 509P39 531T +excl':({'487':C,'509':P(39),'531':T},T),
}
for k,(h,e) in cands.items(): summary(k,h,e)
