exec(open('/tmp/claude-1000/-home-sumit-Downloads-OC-OC/64ffea75-2ed7-4766-a065-99d4d43b34de/scratchpad/r3/sim4.py').read().split('T=(')[0])
T=('T',0);C=('C',0);P=lambda n:('P',n)
cands={
 'F1 excl+531T 487C+499C 459P+509P':({'531':T,'487':C,'499':C,'459':P(38),'509':P(39)},T),
 'F2 excl+531T+444T 487C+499C 509P':({'531':T,'444':T,'487':C,'499':C,'509':P(39)},T),
 'F3 excl+531T+444T 487C 459P+509P':({'531':T,'444':T,'487':C,'459':P(38),'509':P(39)},T),
 'F4 excl+531T+444T 487C+499C 459P+509P':({'531':T,'444':T,'487':C,'499':C,'459':P(38),'509':P(39)},T),
 'F5 excl+531T+444T 487C 509P':({'531':T,'444':T,'487':C,'509':P(39)},T),
}
for k,(h,e) in cands.items(): summary(k,h,e)
