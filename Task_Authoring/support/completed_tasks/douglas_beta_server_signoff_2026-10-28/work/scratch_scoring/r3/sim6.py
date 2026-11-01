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
def rubric(Ys,Ns,hidden,excl,h):
    f={t:found(h,v) for t,v in hidden.items()}; a=found(h,excl) if excl else True
    r=[]
    for t in Ys: r.append(('st'+t,3,True))
    for t in Ns: r+=[('st'+t,3,True),('dl'+t,1,True),('mv'+t,1,True),('cm'+t,1,True)]
    for t,x in f.items(): r+=[('st'+t,5,x),('dl'+t,3,x),('mv'+t,1,x),('cm'+t,3,x)]
    if excl: r+=[('ex547',3,a),('ex553',3,a)]
    r+=[('dmcount',3,a and all(f.values())),('folder',3,True),('share',3,True),('leo',1,True),('dm',1,True),('cols',1,True)]
    return r
def summary(name,Ys,Ns,hidden,excl,verbose=False):
    tot=ok=0;fails=collections.Counter();avgs=[];sds=[]
    for b,runs in B.items():
        for s in ([runs] if len(runs)==6 else [list(c) for c in itertools.combinations(runs,6)]):
            rows=[rubric(Ys,Ns,hidden,excl,h) for h in s]
            data={'task_type':'long-horizon','rubrics':[{'id':n,'weight':w,'valid':True} for n,w,_ in rows[0]],
                  'rollouts':[{'id':f'run-{i+1}','status':'completed','tool_calls':200,'results':{n:p for n,_,p in r}} for i,r in enumerate(rows)]}
            g=ds.compute(data)['gates']; tot+=1
            bad=[k for k,x in g.items() if not x['verdict'].startswith(('PASS','NON-FAIL')) and k!='horizon']
            ok+= not bad
            for k in bad: fails[k]+=1
            sc=[sum(w for _,w,p in r if p)/sum(w for _,w,_ in r) for r in rows]
            avgs.append(st.mean(sc)); sds.append(st.pstdev(sc))
    print('%-46s rows %2d pass %2d/%d avg %.2f-%.2f sd %.3f-%.3f %s'%(name,len(rows[0]),ok,tot,min(avgs),max(avgs),min(sds),max(sds),dict(fails)))
T=('T',0);C=('C',0);P=lambda n:('P',n)
Y0=['459','509','499','531','444','510']; N0=['336','392','503','518','550','435','557','256']
def mk(name,hidden,dropN=(),dropY=(),excl=T):
    Ys=[y for y in Y0 if y not in hidden and y not in dropY]; Ns=[n for n in N0 if n not in dropN]
    summary(name,Ys,Ns,hidden,excl)
mk('cur 487C 537P46',{'487':C,'537':P(46)})
mk('F4 531T 444T 487C 499C 459P 509P',{'531':T,'444':T,'487':C,'499':C,'459':P(38),'509':P(39)})
mk('F3 531T 444T 487C 459P 509P',{'531':T,'444':T,'487':C,'459':P(38),'509':P(39)})
mk('F3 drop336,435',{'531':T,'444':T,'487':C,'459':P(38),'509':P(39)},dropN=('336','435'))
mk('F3 drop336,435,518',{'531':T,'444':T,'487':C,'459':P(38),'509':P(39)},dropN=('336','435','518'))
mk('F5 531T 444T 487C 509P',{'531':T,'444':T,'487':C,'509':P(39)})
mk('F6 531T 444T 510T 487C 459P 509P',{'531':T,'444':T,'510':T,'487':C,'459':P(38),'509':P(39)})
mk('F7 531T 444T 487C 499C 509P drop336,435',{'531':T,'444':T,'487':C,'499':C,'509':P(39)},dropN=('336','435'))
