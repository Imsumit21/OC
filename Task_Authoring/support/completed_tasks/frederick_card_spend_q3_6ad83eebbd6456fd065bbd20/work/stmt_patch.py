import sys,json,re
W='/home/sumit/Downloads/OC/OC/Task_Authoring-2/support/task_work/fs_ua_trueup'
sys.path.insert(0,W)
import ids as I, model as M, texts as X
P='/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/01_Universe_Inject.sql'
L=open(P).read().split('\n')
def j(o): return json.dumps(o,ensure_ascii=False)
changed=[];same=0
for key,acct,period,saved in I.UNITY_PERIODS:
    fid=I.UNITY_STMT[key]; a,b=M.period_bounds(key); rows=M.statement_rows(key)
    tot=M.cents(sum(r[4] for r in rows)); to_date=" (to date)" if key=="2025-09-22..29" else ""
    grid=[["Unity Ads - spend statement"],["Organization",X.UNITY_ACCOUNT_NAME[acct]],["Period",f"{a.isoformat()} to {b.isoformat()}{to_date}"],["Exported",saved[:10]],[],X.UNITY_STMT_HEADER]+[[r[0].isoformat(),r[2],r[3],r[4]] for r in rows]+[[],["Total","","",f"${tot:,.2f}"]]
    new=j(grid).replace("'","''")
    idx=[i for i,l in enumerate(L) if l.startswith(f"VALUES ('{fid}', 0, 'Statement'")]
    assert len(idx)==1,fid
    l=L[idx[0]]; m=re.search(r", '(\[\[.*\]\])'\);$",l); old=m.group(1)
    if old==new: same+=1; continue
    L[idx[0]]=l[:m.start(1)]+new+l[m.end(1):]
    oldtot=re.search(r'\["Total", "", "", "([^"]+)"\]',old).group(1)
    changed.append((key,fid,oldtot,f"${tot:,.2f}"))
open(P,'w').write('\n'.join(L))
print('unchanged',same)
for c in changed: print('changed',c)
