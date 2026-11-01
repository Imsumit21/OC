exec(open('/tmp/claude-1000/-home-sumit-Downloads-OC-OC/64ffea75-2ed7-4766-a065-99d4d43b34de/scratchpad/r3/sim7.py').read().split("T=('T',0)")[0])
T=('T',0);C=('C',0);P=lambda n:('P',n)
b={'547':(T,'excl'),'553':(T,'excl'),'487':(C,'keepN'),'537':(P(46),'keepN')}
evaluate('L1 T444,X436(N) P509,459',{**b,'444':(T,'flip'),'X436':(T,'incN'),'509':(P(39),'flip'),'459':(P(38),'flip')})
evaluate('L2 T444,X436(N),531 P509,459',{**b,'444':(T,'flip'),'X436':(T,'incN'),'531':(T,'flip'),'509':(P(39),'flip'),'459':(P(38),'flip')})
evaluate('L3 T444,X436(N),531 P509',{**b,'444':(T,'flip'),'X436':(T,'incN'),'531':(T,'flip'),'509':(P(39),'flip')})
evaluate('L4 T444,X436,X2(N) P509,459',{**b,'444':(T,'flip'),'X436':(T,'incN'),'X2':(T,'incN'),'509':(P(39),'flip'),'459':(P(38),'flip')})
