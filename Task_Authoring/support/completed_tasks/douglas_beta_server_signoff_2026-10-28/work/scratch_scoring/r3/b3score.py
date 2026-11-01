exec(open('sim7.py').read().split("T=('T',0)")[0])
T=('T',0);C=('C',0);P=lambda n:('P',n)
b={'547':(T,'excl'),'553':(T,'excl'),'487':(C,'keepN'),'537':(P(46),'keepN')}
L2={**b,'444':(T,'flip'),'X436':(T,'incN'),'531':(T,'flip'),'509':(P(39),'flip'),'459':(P(38),'flip')}
H=['547','553','487','537','444','X436','531','509','459']
wrong={1:{'459','509','531','537','444','X436','547','553'},
       2:{'459','509','537'},
       3:{'459','509','531','537','444','487','X436','547','553'},
       4:{'459','509','531','537','444','X436','547','553'},
       5:{'459','509','537'},
       6:{'459','509','531','537','444','487','X436','547','553'}}
import difficulty_stats as ds
def rub(ok):
    global found
    old=found
    globals()['found']=lambda h,f: h['_t'] in ok
    r=[]
    for t in Y0+N0+['487','537','547','553','X436']:
        hab,kind=L2.get(t,(None,None)) if t in L2 else (None,None)
        x=t in ok
        if t in L2:
            if kind in('flip','keepN','incN'): r+=[('st'+t,5,x),('dl'+t,3,x),('mv'+t,1,x),('cm'+t,3,x)]
            elif kind=='excl': r+=[('ex'+t,3,x)]
        elif t in Y0: r.append(('st'+t,3,True))
        elif t in N0: r+=[('st'+t,3,True),('dl'+t,1,True),('mv'+t,1,True),('cm'+t,1,True)]
    r+=[('dmcount',3,all(t in ok for t in H)),('folder',3,True),('share',3,True),('leo',1,True),('dm',1,True),('cols',1,True)]
    globals()['found']=old
    return r
rows=[rub(set(H)-wrong[i]) for i in range(1,7)]
sc=[sum(w for _,w,p in r if p)/sum(w for _,w,_ in r) for r in rows]
data={'task_type':'long-horizon','rubrics':[{'id':n,'weight':w,'valid':True} for n,w,_ in rows[0]],
      'rollouts':[{'id':f'run-{i+1}','status':'completed','tool_calls':200,'results':{n:p for n,_,p in r}} for i,r in enumerate(rows)]}
g=ds.compute(data)['gates']
print('scores',' '.join('%.3f'%x for x in sc),'avg %.3f sd %.3f'%(st.mean(sc),st.pstdev(sc)))
for k,v in g.items(): print(k,v['verdict'],str(v.get('value'))[:150])
def run(rows,label):
    sc=[sum(w for _,w,p in r if p)/sum(w for _,w,_ in r) for r in rows]
    data={'task_type':'long-horizon','rubrics':[{'id':n,'weight':w,'valid':True} for n,w,_ in rows[0]],
      'rollouts':[{'id':f'run-{i+1}','status':'completed','tool_calls':200,'results':{n:p for n,_,p in r}} for i,r in enumerate(rows)]}
    g=ds.compute(data)['gates']
    print('%-28s avg %.3f sd %.3f | %s'%(label,st.mean(sc),st.pstdev(sc),' '.join('%s:%s'%(k[:8],v['verdict'][:4]) for k,v in g.items())))
run(rows,'plan weights')
run([[(n,1,p) for n,_,p in r] for r in rows],'flat weights')
run([r+[('ap%d'%j,3,True) for j in range(10)] for r in rows],'+10 always-pass (w3)')
run([r+[('ap%d'%j,5,True) for j in range(10)] for r in rows],'+10 always-pass (w5)')
run([[(n,3,p) for n,_,p in r if not n.startswith(('dl','mv','cm'))] for r in rows],'status rows only, flat 3')
