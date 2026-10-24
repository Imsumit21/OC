"""Compare blind predictions with exported QC card verdicts/flags. Usage: python3 score.py before|after"""
import json,sys,os,collections
CAL=os.path.dirname(os.path.abspath(__file__))+'/'
ROOT=os.path.abspath(CAL+'../../../../..')+'/'
cases={c['card_index']:c for c in json.load(open(ROOT+'Evals/references/rules/rubric_qc_cases.json'))['cases']}
DIM={'Rubric criteria quality':'overall_quality','Rubric phrasing':'agent_centric','Process-rubric':'process','All-fail':'all_fail'}
def actual(c):
    out={}
    for f in c['flags']:
        dim=next(v for k,v in DIM.items() if f['qc_criterion'].startswith(k))
        st='FAIL' if f['verdict']=='FAIL' else 'NON-FAIL'
        if out.get(dim)!='FAIL': out[dim]=st
    return out
p=sys.argv[1]; d=CAL+'pred_'+p+'/'
rows=[];vc=collections.Counter();fl=collections.Counter();oq=collections.Counter();extra=collections.Counter()
for fn in sorted(os.listdir(d)):
    k=int(fn[5:7]); pr=json.load(open(d+fn)); c=cases[k]; a=actual(c)
    av='FAIL' if c['exported_card_verdict']=='FAIL' else 'NON-FAIL'
    pv={'FAIL-RISK':'FAIL','NON-FAIL-RISK':'NON-FAIL','CLEAN':'PASS'}[pr['readiness']]
    vc[(av,pv)]+=1
    dims={k2:v for k2,v in pr['dimensions'].items() if v in('FAIL','NON-FAIL')}
    for dim,st in a.items():
        if dim=='all_fail': fl['all_fail_not_evaluable']+=1; continue
        fl['actual']+=1
        if dims.get(dim)==st: fl['exact']+=1
        elif dim in dims: fl['dim_only']+=1
        else: fl['missed']+=1
    for dim,st in dims.items():
        if dim not in a: extra[(dim,st)]+=1
    oq[(a.get('overall_quality','none'),pr['dimensions'].get('overall_quality'))]+=1
    t=pr['tally']; rows.append((k,av,pv,a,dims,t['rows_major'],t['rows_moderate'],t['rows_minor'],t['missing_outcomes'],pr['n_criteria']))
n=len(rows); agree=sum(v for (x,y),v in vc.items() if x==y)
print(f'{p}: cards {n}  verdict agreement {agree}/{n}');print(' verdict matrix (actual,pred):',dict(vc))
print(' flag-level:',dict(fl));print(' overall-quality (actual,pred):',dict(oq));print(' extra predicted flags:',dict(extra))
for r in rows: print('  card %02d act=%s pred=%s act_flags=%s pred_dims=%s maj/mod/min/miss=%d/%d/%d/%d of %d'%r)
