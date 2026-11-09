import json,os,subprocess,sys
WS='/home/sumit/Desktop/OC'
ENV={**os.environ,'TASK_AUTHORING_TASK_DIR':WS+'/Task_Authoring/task_inputsK'}
def hg(*a,timeout=280):
    p=subprocess.run(['python3','Task_Authoring/tools/hg.py','search',*map(str,a)],cwd=WS,capture_output=True,text=True,env=ENV,timeout=timeout)
    try: return json.loads(p.stdout)
    except Exception: return {'_raw':p.stdout[:400],'_err':p.stderr[:400]}
def find(svc,q,file=None,limit=8,**kw):
    a=['search',svc,q,'--limit',limit]
    if file: a+=['--file',file]
    for k,v in kw.items(): a+=['--'+k,v]
    return hg(*a)
def get(svc,file,ptr,maxc=200000):
    return hg('get',svc,'--file',file,'--pointer',ptr,'--max-chars',maxc)

def many(items):
    """items: list of (id,service,file,pointer,maxc); batched at 50."""
    out={}
    for i in range(0,len(items),40):
        req={'items':[{'id':a,'service':b,'file':c,'pointer':d,'max_chars':e} for a,b,c,d,e in items[i:i+40]]}
        fn='/tmp/claude-1000/-home-sumit-Desktop-OC/2eac4773-c48b-419e-a4fd-71940747c48d/scratchpad/oe/req.json'; json.dump(req,open(fn,'w'))
        g=hg('get-many','--request',fn,'--compact')
        its=g.get('items') or g.get('results') or []
        if isinstance(its,dict): its=[dict(v,id=k) for k,v in its.items()]
        for it in its:
            out[it.get('id')]=it.get('text')
        if not (g.get('items') or g.get('results')): print('MANYERR',str(g)[:300])
    return out
