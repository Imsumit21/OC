import json,re,sys
sys.path.insert(0,'../rubplan')
runs=json.load(open('runs.json'))
rows={x['P']:x for x in json.load(open('/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/Working_Files/09_Rubrics.draft_with_plan_ids.json'))}
exec(open('../rubplan/draft.py').read().split("out = []")[0].replace("rows = json.load(open(sys.argv[1]))","rows=[]"))  # get ACC, A
def norm(s): return re.sub(r'[^a-z0-9]','',str(s).lower())
NAMES={norm(n):n for n in ACC}
NAMES.update({'intuitquickbooks':'QuickBooks','quickbooksintuit':'QuickBooks','intuit':'QuickBooks','quickbooksonline':'QuickBooks','googleworkspacegsuite':'Google Workspace','elevenlabssoundline':'ElevenLabs','githubhosting':'GitHub','googlecloudbigquery':'BigQuery','bigquerygooglecloud':'BigQuery'})
def acct(cell):
    c=norm(cell)
    if c in NAMES: return NAMES[c]
    for k,v in NAMES.items():
        if c.startswith(k) or k in c[:len(k)+6]: return v
    return None
def money(x):
    try: return round(float(str(x).replace('$','').replace(',','').strip()),2)
    except: return None
def date(x):
    s=str(x)
    for pat,fmt in [(r'2026-(\d\d)-(\d\d)',None)]:
        m=re.search(pat,s)
        if m: return (int(m.group(1)),int(m.group(2)))
    M={'jan':1,'feb':2,'mar':3,'apr':4,'aug':8,'sep':9}
    m=re.search(r'([A-Za-z]{3})[a-z]* (\d{1,2})',s)
    if m and m.group(1).lower() in M: return (M[m.group(1).lower()],int(m.group(2)))
    m=re.search(r'(\d{1,2})/(\d{1,2})',s)
    if m: return (int(m.group(1)),int(m.group(2)))
    return None
def register(R):
    rows_=[]
    for rng,vals in R['sheet']:
        if vals and len(vals)>3: rows_=vals  # main block
    hdr=[norm(h) for h in rows_[0]]
    def col(*keys):
        for i,h in enumerate(hdr):
            if any(k in h for k in keys): return i
    ci={'acct':0,'act':col('whatwedo','action'),'stat':col('wherestands','status','stands'),'by':col('bywhen','due'),'own':col('owner','whodoes'),'cost':col('monthly','cost'),'note':col('note','source','where')}
    reg={}; extra=[]
    for r in rows_[1:]:
        if not r or not str(r[0]).strip(): continue
        a=acct(r[0])
        g=lambda k: (r[ci[k]] if ci[k] is not None and ci[k]<len(r) else '')
        if a and a not in reg: reg[a]={k:g(k) for k in ci}; reg[a]['raw']=' | '.join(map(str,r))
        else: extra.append(' | '.join(map(str,r)))
    return reg,extra,ci,rows_
ACTW={'Cancel':['cancel'],'Keep':['keep'],'Hold for Sunset':['hold'],"Move to Arthur's LLC":['move','llc']}
res={}
for k,R in runs.items():
    reg,extra,ci,allrows=register(R)
    out={}
    out['P2']=len(reg)==25
    out['P3']='QuickBooks' in reg and not any('intuit' in norm(e)[:12] for e in extra)
    for n,(a,s,b,o,c) in ACC.items():
        r=reg.get(n,{})
        out[('act',n)]=any(w in norm(r.get('act','')) for w in ACTW[a])
        out[('stat',n)]= (s.lower() in norm(r.get('stat',''))) if s else None
        out[('by',n)]= date(r.get('by',''))== (date(b) if b!='—' else None) if b!='—' else None
        out[('own',n)]= o.lower() in str(r.get('own','')).lower()
        out[('cost',n)]= money(r.get('cost')) is not None and abs(money(r.get('cost'))-money(c))<=0.011
        out[('raw',n)]=r.get('raw','MISSING')
    allt=' '.join(' '.join(map(str,x)) for x in allrows)+' '+' '.join(' '.join(' '.join(map(str,rr)) for rr in v) for _,v in R['sheet'] if v)
    out['P66']='6706.49' in allt.replace(',','') ; out['P67']='1249.04' in allt.replace(',','')
    out['shares']=R['shares']; out['states']=R['states']; out['comments']=R['comments']; out['slack']=[s['message'] for s in R['slack']]
    out['extra']=extra
    res[k]=out
import pickle; pickle.dump(res,open("graded.pkl","wb"))
# summary
keys=[k for k in res[next(iter(res))] if isinstance(k,tuple) and k[0]!='raw']+['P2','P3','P66','P67']
for key in keys:
    v=[res[r][key] for r in res]
    if all(x is None for x in v): continue
    print(key, sum(1 for x in v if x), '/', len(v))
