src=open('/tmp/claude-1000/-home-sumit-Downloads-OC-OC/64ffea75-2ed7-4766-a065-99d4d43b34de/scratchpad/r3/sim7.py').read().split("T=('T',0)")[0]
T=('T',0);C=('C',0);P=lambda n:('P',n)
b={'547':(T,'excl'),'553':(T,'excl'),'487':(C,'keepN'),'537':(P(46),'keepN')}
L2={**b,'444':(T,'flip'),'X436':(T,'incN'),'531':(T,'flip'),'509':(P(39),'flip'),'459':(P(38),'flip')}
variants={
 'base (hidden status 5, DM list per ticket 3/1, comments 3/1)':src,
 'flat: every status 3, DM list 1, comment 1':src.replace("r+=[('st'+t,5,x),('dl'+t,3,x),('mv'+t,1,x),('cm'+t,3,x)]","r+=[('st'+t,3,x),('dl'+t,1,x),('mv'+t,1,x),('cm'+t,1,x)]").replace("elif kind=='incN': r+=[('st'+t,5,x),('dl'+t,3,x),('mv'+t,1,x),('cm'+t,3,x)]","elif kind=='incN': r+=[('st'+t,3,x),('dl'+t,1,x),('mv'+t,1,x),('cm'+t,1,x)]"),
 'no per-ticket DM list rows (one DM list row 3)':src.replace("r+=[('st'+t,5,x),('dl'+t,3,x),('mv'+t,1,x),('cm'+t,3,x)]","r+=[('st'+t,5,x),('mv'+t,1,x),('cm'+t,3,x)]").replace("elif kind=='incN': r+=[('st'+t,5,x),('dl'+t,3,x),('mv'+t,1,x),('cm'+t,3,x)]","elif kind=='incN': r+=[('st'+t,5,x),('mv'+t,1,x),('cm'+t,3,x)]").replace("r+=[('st'+t,3,True),('dl'+t,1,True),('mv'+t,1,True),('cm'+t,1,True)]","r+=[('st'+t,3,True),('mv'+t,1,True),('cm'+t,1,True)]").replace("r+=[('dmcount',3,allok)","r+=[('dmlist',3,allok),('dmcount',3,allok)"),
 '+10 extra always-pass rows (weight 3)':src.replace("('cols',1,True)]","('cols',1,True)]+[('extra%d'%i,3,True) for i in range(10)]"),
}
for name,code in variants.items():
    g={}; exec(code,g); print(name); g['evaluate']('  ROUND3',L2,n=3000); g['evaluate']('  CURRENT',b,n=1500)
