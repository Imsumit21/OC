exec(open('/tmp/claude-1000/-home-sumit-Downloads-OC-OC/64ffea75-2ed7-4766-a065-99d4d43b34de/scratchpad/r3/sim6.py').read().split("T=('T',0)")[0])
import random
random.seed(7)
POOL=[h for runs in B.values() for h in runs]
T=('T',0);C=('C',0);P=lambda n:('P',n)
Y0=['459','509','499','531','444','510']; N0=['336','392','503','518','550','435','557','256']
def gates(Ys,Ns,hidden,excl,s):
    rows=[rubric(Ys,Ns,hidden,excl,h) for h in s]
    data={'task_type':'long-horizon','rubrics':[{'id':n,'weight':w,'valid':True} for n,w,_ in rows[0]],
          'rollouts':[{'id':f'run-{i+1}','status':'completed','tool_calls':200,'results':{n:p for n,_,p in r}} for i,r in enumerate(rows)]}
    return ds.compute(data)['gates']
def boot(name,hidden,dropN=(),excl=T,n=3000):
    Ys=[y for y in Y0 if y not in hidden]; Ns=[x for x in N0 if x not in dropN]
    ok=0;fails=collections.Counter()
    for _ in range(n):
        s=random.choices(POOL,k=6)
        g=gates(Ys,Ns,hidden,excl,s)
        bad=[k for k,x in g.items() if not x['verdict'].startswith(('PASS','NON-FAIL')) and k!='horizon']
        ok+=not bad
        for k in bad: fails[k]+=1
    print('%-48s P(all gates)=%.0f%% fails %s'%(name,100*ok/n,{k:'%.0f%%'%(100*v/n) for k,v in fails.items()}))
H3={'531':T,'444':T,'487':C,'459':P(38),'509':P(39)}
boot('F3',H3)
boot('F3 drop336,435',H3,dropN=('336','435'))
boot('F3 +537P46 drop336,435',{**H3,'537':P(46)},dropN=('336','435'))
boot('F6 (+510T)',{**H3,'510':T})
boot('F6 +537P46',{**H3,'510':T,'537':P(46)})
boot('F6 drop336,435 +537P46',{**H3,'510':T,'537':P(46)},dropN=('336','435'))
boot('F4 (+499C)',{**H3,'499':C})
boot('F4 +537P46',{**H3,'499':C,'537':P(46)})
boot('F4 +537P46 drop336,435',{**H3,'499':C,'537':P(46)},dropN=('336','435'))
