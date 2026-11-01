"""Deterministic id minting for the account-custody scenario (design only; never writes to the base)."""
import hashlib, datetime as D, json
def ts(s): return D.datetime.fromisoformat(s.replace('Z','+00:00')).timestamp()
def h(seed,n): return hashlib.sha256(seed.encode()).hexdigest()[:n]
out={}
slack=[('S_CLAIM','D05S58U4SAK','2025-09-29T23:05:41.318207Z'),('S_HUB','D05S58U4SAK','2025-09-30T22:40:12.507134Z'),('S_DECOY90','C07C2866011','2025-09-15T19:02:33.240719Z'),('S_ARTHUR_SUM','C07C2866011','2025-09-30T21:10:27.118342Z')]
for k,c,t in slack:
    tsv=f"{ts(t):.6f}"; out[k]={'channel':c,'ts':tsv,'id':hashlib.sha256(f"{c}|{tsv}".encode()).hexdigest()[:32],'at':t}
def trello(seed,t): return format(int(ts(t)),'08x')+h('trello'+seed,16)
for k,t in [('T_H1CARD','2025-09-30T20:41:16Z'),('T_ENGCARD','2025-09-30T20:52:03Z'),('T_H1CMT','2025-09-30T21:58:44Z'),('T_H1CREATE','2025-09-30T20:41:16Z'),('T_ENGCREATE','2025-09-30T20:52:03Z')]:
    out[k]={'id':trello(k,t),'at':t}
def f(seed): return 'f_'+h('drive'+seed,22)
plats=['meta','gads_569','gads_449','unity_ads','applovin','adjoe','tiktok','youtube','linkedin','x','instagram','discord','admob','play_console','app_store_connect','singular']
for p in plats: out['SW_'+p]={'id':f('sweep_'+p)}
for k in ['FOLDER_SWEEP','FOLDER_OPS','DOC_CASH','SHEET_MARCH']: out[k]={'id':f(k)}
# gmail ids: 19-digit gmail-style ids increase with time (ms<<20 approx)
def gid(t): return str(int(ts(t)*1000)<<20 | int(h('g'+t,5),16) & 0xFFFFF)
out['G_AMEND']={'at':'2025-09-30T23:21:09Z','gmail_id':gid('2025-09-30T23:21:09Z')}
out['CONF_PAGE']={'id':'page_company_accounts_access','at':'2024-03-12T16:20:00Z'}
print(json.dumps(out,indent=1))
