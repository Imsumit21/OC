import sys,re
W='/home/sumit/Downloads/OC/OC/Task_Authoring-2/support/task_work/fs_ua_trueup'; sys.path.insert(0,W)
import ids as I, model as M
P='/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/Working_Files/01_Grounding_Dossier.md'
t=open(P).read().split('\n'); n=0
for k,acct,period,saved in I.UNITY_PERIODS:
    fid=I.UNITY_STMT[k]; rows=M.statement_rows(k)
    tot=M.cents(sum(r[4] for r in rows))
    f=M.cents(sum(r[4] for r in rows if M.unity_bucket(r[3],r[0])=='Fundraising')); ru=M.cents(tot-f)
    for i,l in enumerate(t):
        if l.startswith(f'| {fid} | seeded | Unity statement'):
            l2=re.sub(r'total \$[\d,]+\.\d\d( \(Fundraising \$[\d,]+\.\d\d, Real UA \$[\d,]+\.\d\d\))?',
                      lambda m: f'total ${tot:,.2f}'+(f' (Fundraising ${f:,.2f}, Real UA ${ru:,.2f})' if m.group(1) else ''),l)
            if l2!=l: t[i]=l2; n+=1
s='\n'.join(t)
s=s.replace('| Unity statement total Calm Play Sep 15-21 | 1,456.04 |','| Unity statement total Calm Play Sep 15-21 | 1,316.00 |').replace('| Unity statement total Calm Play Jul 8-14 | 858.30 |','| Unity statement total Calm Play Jul 8-14 | 175.18 |')
s=s.replace("Ground truth unchanged: Real UA $111,387.92, Fundraising $3,485.20 (the T23 receipts are excluded).",
 "Revision 2 (after /prompt rev 14): doc says 'Node used to run'; the Calm Play and HG Unity statements follow every dated base pause and restart in #executives (model.py UNITY_CAMPAIGNS comments); the Aug 31 Meta receipt covers Jul 18 - Aug 4; the Jul 28 - Aug 3 decoy receipt. Ground truth now: Real UA $95,795.25, Fundraising $3,485.20 (T23 receipts excluded), gap list unchanged (17).")
open(P,'w').write(s); print('rows updated',n)
