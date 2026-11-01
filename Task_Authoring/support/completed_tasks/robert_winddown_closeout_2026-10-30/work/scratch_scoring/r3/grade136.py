import json,re,sys,statistics as st
LEN=sys.argv[3] if len(sys.argv)>3 else ''
RUNS=json.load(open(sys.argv[1])); RUB=json.load(open(sys.argv[2]))
ID={'ENG-2438':'Unity','ENG-2439':'Helpshift','ENG-2440':'Soundly','ENG-2441':'Linear','ENG-2442':'Figma','ENG-2443':'Trello','ENG-2444':'Singular','ENG-2446':'Metabase','ENG-2447':'dbt','ENG-2448':'BigQuery','ENG-2449':'QuickBooks','ENG-2450':'Intuit','ENG-2451':'Carta','ENG-2452':'Google Workspace','ENG-2453':'Slack','ENG-2454':'iPostal','ENG-2455':'Gusto','ENG-2456':'Deel','ENG-2457':'Docusign','ENG-2458':'Layer','ENG-2459':'CodeRabbit','ENG-2460':'Cursor','ENG-2461':'Zapier','ENG-2462':'GitHub','ENG-2463':'Kapwing','ENG-2464':'1Password','ENG-2465':'Lucidchart','ENG-2466':'Google Ads'}
DONE={'ENG-2438','ENG-2439','ENG-2440','ENG-2459','ENG-2460','ENG-2461','ENG-2463'}; CANC={'ENG-2450','ENG-2454','ENG-2465','ENG-2466'}
DATE={'Feb 17':r'feb(ruary)?\.? ?17|2026-02-17|02/17|2/17|17 feb|the 17th','Mar 12':r'mar(ch)?\.? ?12|2026-03-12|03/12|3/12|review call','Aug 14':r'aug(ust)?\.? ?14|2026-08-14|08/14|8/14'}
ANYDATE=r'(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.? ?\d{1,2}\b|\b2026-\d\d-\d\d|\b\d{1,2}/\d{1,2}\b|by eod'
def acct(t):
    m=re.search(r'ENG-\d+',t); return ID[m.group(0)] if m else ('ElevenLabs' if 'ElevenLabs' in t else None)
def grid(o):
    rows=[]
    for rng,vals in o['sheet']:
        rows+= [[str(c) for c in r] for r in vals]
    return rows
def find(rows,n):
    k={'QuickBooks':['quickbooks','intuit'],'Google Workspace':['google workspace','workspace'],'1Password':['1password'],'ElevenLabs':['elevenlabs','eleven']}.get(n,[n.lower()])
    for r in rows[1:]:
        if r and any(x in r[0].lower() for x in k): return r
    return None
def st_(o,i): s=(o['states'].get(i) or '').lower(); return {'completed':'done'}.get(s,s)
res={}
for name,o in RUNS.items():
    if name=='trajectory-run-1.json': continue
    G=grid(o); hdr=[h.lower() for h in G[0]] if G else []
    col=lambda key: next((j for j,h in enumerate(hdr) if key in h),None)
    cA,cS,cB,cO,cC=col('what we do'),col('where'),col('by when'),col('owner'),col('cost')
    allsheet=' '.join(' '.join(r) for r in G).replace(',','')
    reply=' '.join(m['message'] for m in o['slack'] if m.get('thread_ts')=='1771003267.448213').lower()
    got=W=0; fails=[]
    for ix,r in enumerate(RUB,1):
        t=r['title']; w=r['weight']; W+=w; n=acct(t); row=find(G,n) if n else None
        cell=lambda c: (row[c].lower() if row and c is not None and c<len(row) else '')
        com=' '.join(o['comments'].get(next((k for k,v in ID.items() if v==n),''),[]) ).lower()
        ok=True
        if 'as the action for' in t:
            a=cell(cA); exp=t.split('records ')[1].split(' (')[0].lower()
            ok={'hold for sunset':'hold' in a,'keep':'keep' in a and 'hold' not in a,'cancel':'cancel' in a,"move to arthur's llc":('move' in a or 'arthur' in a or 'kubllc' in a)}.get(exp,True)
        elif 'records the status' in t:
            s=cell(cS); exp=t.split('status ')[1].split(' (')[0]
            ok={'Closed':'closed' in s or 'confirm' in s,'Requested':'request' in s,'Open':'open' in s}[exp]
        elif 'records no status' in t: ok=cell(cS).strip() in ('','-','—','n/a','none')
        elif 'records no date' in t: ok=cell(cB).strip() in ('','-','—','n/a','none')
        elif 'as the by-when date for' in t:
            dk=next(k for k in DATE if t.split('records ')[1].startswith(k)); ok=bool(re.search(DATE[dk],cell(cB)))
        elif 'as the owner of' in t: ok=t.split('records ')[1].split(' ')[0].lower() in cell(cO)
        elif 'a monthly cost of' in t:
            v=float(re.search(r'of ([\d,]+\.\d\d)',t).group(1).replace(',',''))
            try: ok=abs(float(cell(cC).replace('$','').replace(',',''))-v)<=0.011
            except: ok=False
        elif 'as where' in t:
            nt=' '.join(row).lower() if row else ''
            ok={'Unity':'account manager' in nt or 'executives' in nt,'Cursor':'prototype' in nt or ('cursor' in nt and 'confirm' in nt),'CodeRabbit':'bot' in nt or 'pull' in nt or 'pr ' in nt or '#38' in nt}[n] and ('closed' in cell(cS) or 'confirm' in cell(cS))
        elif 'total monthly cost over every row' in t: ok='6706.49' in allsheet or '=sum' in allsheet.lower()
        elif 'Keep and Hold for Sunset rows of' in t: ok='1249.04' in allsheet or '=sum' in allsheet.lower()
        elif 'one single row' in t or 'exactly 25' in t or 'creates the account' in t or 'shares the' in t: ok=True
        elif t.startswith('The Agent sets Linear issue'):
            i=re.search(r'ENG-\d+',t).group(0); ok=st_(o,i)==('done' if i in DONE else 'canceled')
        elif 'moves exactly 11' in t:
            ok=sum(1 for i in ID if st_(o,i) in ('done','canceled','duplicate'))==11
        elif 'nothing is due by a date' in t: ok=bool(com) and (bool(re.search(r'no date|no deadline|nothing (left|else|more|to do|due)|n/a|no by.when|no hold'+LEN,com)) or not re.search(ANYDATE,com))
        elif 'as the by-when date in its new comment' in t:
            dk=next(k for k in DATE if t.split('gives ')[1].startswith(k)); ok=bool(re.search(DATE[dk],com))
        elif 'adds a new comment on Linear issue' in t:
            if not com: ok=False
            elif 'is cancelled (cancelled' in t: ok=not re.search(r'request|pending|waiting|no reply|nothing back|until .* confirms',com)
            elif 'held for Sunset' in t: ok='hold' in com or 'sunset' in com
            elif 'is kept' in t: ok='keep' in com or 'kept' in com
            elif 'being cancelled' in t: ok='cancel' in com
            elif 'moves to Arthur' in t: ok=('arthur' in com or 'kubllc' in com) and 'hold' not in com
            else: ok=True
        elif 'monthly total over every register row' in t: ok='6,706.49' in reply or '6706.49' in reply
        elif 'monthly total over the Keep and Hold' in t: ok='1,249.04' in reply or '1249.04' in reply
        elif 'as a clash, the #winddown decision to take Slack' in t: ok=bool(re.search(r'clash[^\n]*\n?[^\n]*slack|\*\*slack',reply)) and 'nothing else clashes' not in reply.split('slack')[0][-200:]
        elif 'as a clash, the plan to archive Google' in t: ok='archiv' in reply
        elif 'names exactly two clashes' in t: ok=None
        elif r['category']=='Process': ok=True
        if ok is None: W-=w; continue
        got+=w if ok else 0
        if not ok: fails.append(ix)
    res[name]=(got/W,fails)
for k,(s,f) in res.items(): print(k, round(100*s,1), len(f), f)
v=[s for s,_ in res.values()]; print('avg',round(100*st.mean(v),1),'sd',round(st.pstdev(v),3))
