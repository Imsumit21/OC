"""Classify after-pass disagreements by driver. Re-tallies each card under QC-era severities
(overly_specific->Moderate, overly_broad->Minor, non_agent_centric->Minor, negative not failing)
to separate 'older rules' from residual over-flagging. Not blind (analyst step)."""
import json,os,collections
CAL=os.path.dirname(os.path.abspath(__file__))+'/'
ROOT=os.path.abspath(CAL+'../../../../..')+'/'
cases={c['card_index']:c for c in json.load(open(ROOT+'Evals/references/rules/rubric_qc_cases.json'))['cases']}
RANK={'Major':3,'Moderate':2,'Minor':1}
QC={'overly_specific':'Moderate','overly_broad':'Minor','non_agent_centric':'Minor'}
def band(rows,n,miss):
    mj=sum(1 for v in rows.values() if v==3)+miss; md=sum(1 for v in rows.values() if v>=2)+miss; an=len(rows)+miss
    if mj/n>.10 or md/n>.15 or an/n>.20: return 'FAIL'
    return 'PASS' if md==0 and an/n<.05 else 'NON-FAIL'
cls=collections.Counter(); out=[]
for fn in sorted(os.listdir(CAL+'pred_after')):
    k=int(fn[5:7]); p=json.load(open(CAL+'pred_after/'+fn)); c=cases[k]
    act='FAIL' if c['exported_card_verdict']=='FAIL' else 'NON-FAIL'
    pred={'FAIL-RISK':'FAIL','NON-FAIL-RISK':'NON-FAIL','CLEAN':'PASS'}[p['readiness']]
    if act==pred: continue
    n=p['n_criteria']; miss=p['tally']['missing_outcomes']
    strict={};qc={};types=collections.Counter()
    for f in p['findings']:
        s=f['severity']
        if s not in RANK: continue
        t=f['defect'].split()[0].strip(',;'); types[(t,s)]+=1
        strict[f['c']]=max(strict.get(f['c'],0),RANK[s])
        qs=QC.get(t,s); qc[f['c']]=max(qc.get(f['c'],0),RANK[qs])
    neg=p['dimensions'].get('negative')=='FAIL'; oq=p['dimensions'].get('overall_quality')
    qcband=band(qc,n,miss)
    if oq!='FAIL' and neg: why='negative-override only'
    elif oq=='FAIL' and qcband!='FAIL': why='override severities (overly_specific/broad/agent-centric)'
    elif oq=='FAIL': why='Major/Moderate rate under QC-era severities too (title-only self-containment, atomicity, coverage strictness)'
    else: why='other'
    cls[why]+=1
    out.append((k,act,pred,oq,neg,qcband,dict(types.most_common(4)),why))
for o in out: print(o)
print(dict(cls))
