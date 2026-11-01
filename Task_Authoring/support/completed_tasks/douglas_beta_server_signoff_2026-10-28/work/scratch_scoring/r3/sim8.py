exec(open('/tmp/claude-1000/-home-sumit-Downloads-OC-OC/64ffea75-2ed7-4766-a065-99d4d43b34de/scratchpad/r3/sim7.py').read().split("T=('T',0)")[0])
T=('T',0);C=('C',0);P=lambda n:('P',n)
base={'547':(T,'excl'),'553':(T,'excl'),'487':(C,'keepN')}
evaluate('G5 T531,444 C435x P336x,509 +537',{**base,'531':(T,'flip'),'444':(T,'flip'),'435':(C,'excl'),'336':(P(40),'excl'),'509':(P(39),'flip'),'537':(P(46),'keepN')})
evaluate('G8 T531,444,510 P336x,509 +537',{**base,'531':(T,'flip'),'444':(T,'flip'),'510':(T,'flip'),'336':(P(40),'excl'),'509':(P(39),'flip'),'537':(P(46),'keepN')})
evaluate('G9 T531,444,510 P336x,509,459 +537',{**base,'531':(T,'flip'),'444':(T,'flip'),'510':(T,'flip'),'336':(P(40),'excl'),'509':(P(39),'flip'),'459':(P(38),'flip'),'537':(P(46),'keepN')})
evaluate('G10 T531,444,510 C435x P336x,509 +537',{**base,'531':(T,'flip'),'444':(T,'flip'),'510':(T,'flip'),'435':(C,'excl'),'336':(P(40),'excl'),'509':(P(39),'flip'),'537':(P(46),'keepN')})
evaluate('G11 T531,444 C435x P336x,509,459 +537',{**base,'531':(T,'flip'),'444':(T,'flip'),'435':(C,'excl'),'336':(P(40),'excl'),'509':(P(39),'flip'),'459':(P(38),'flip'),'537':(P(46),'keepN')})
evaluate('G12 T531,444 C435x P336x,509,459',{**base,'531':(T,'flip'),'444':(T,'flip'),'435':(C,'excl'),'336':(P(40),'excl'),'509':(P(39),'flip'),'459':(P(38),'flip')})
