import json,re,sys,statistics as st
sys.path.insert(0,'/home/sumit/Downloads/OC/OC/Task_Authoring-2/tools')
import difficulty_stats as ds
R=json.load(open('parsed.json'))
HID=['ZOM-459','ZOM-509','ZOM-537','ZOM-487','ZOM-444','ZOM-531','ZOM-436']
IMP={'ZOM-459':'plague race','ZOM-509':'trophy path copy','ZOM-537':'economy','ZOM-487':'HP','ZOM-444':'analytics events','ZOM-531':'loadout','ZOM-436':'analytics events'}
def notprod_list(dm):
    return set(k for l in dm.splitlines() if l.strip().startswith('•') for k in re.findall(r'ZOM-\d+',l)[:1])
rows=[]
def row(rid,w,fn): rows.append((rid,w,fn))
row('A1_folder',3,lambda x:True)
row('A2_reg_volume17',5,lambda x:len(x['reg'])==17)
for t in HID: row(f'S_{t}_N',5,lambda x,t=t: x['reg'].get(t,{}).get('status')=='N')
for t,v,ww in [('ZOM-499','Y',3),('ZOM-510','Y',3),('ZOM-503','N',5),('ZOM-392','N',3),('ZOM-550','N',5)]:
    row(f'S_{t}_{v}',ww,lambda x,t=t,v=v,ww=ww: x['reg'].get(t,{}).get('status')==v)
row('SC_503',3,lambda x:'#52' in x['reg'].get('ZOM-503',{}).get('change',''))
row('SC_510',3,lambda x:'Zombie Lane' in x['reg'].get('ZOM-510',{}).get('change',''))
row('SC_487',3,lambda x:'HP' in x['reg'].get('ZOM-487',{}).get('change',''))
row('SC_537',3,lambda x:'economy' in x['reg'].get('ZOM-537',{}).get('change','').lower())
row('SC_436',3,lambda x:'analytics' in x['reg'].get('ZOM-436',{}).get('change','').lower())
row('SH_leonard',1,lambda x:any(s.get('emailAddress')=='leonard.hayes@harmonygames.co' and s.get('role')=='commenter' for s in x['share']))
row('D0_dm',1,lambda x:bool(x['dm']))
row('D1_onprod2',5,lambda x:bool(re.search(r'\b2 of 17\b|\*\*2 ',x['dm'])))
row('D2_notprod15',5,lambda x:len(notprod_list(x['dm']))==15)
for t in HID: row(f'DL_{t}',5,lambda x,t=t: t in notprod_list(x['dm']))
for t,ww in [('ZOM-503',5),('ZOM-557',3)]: row(f'DL_{t}',ww,lambda x,t=t: t in notprod_list(x['dm']))
row('M0_15',5,lambda x:len([k for k,v in x['mv'].items() if v=='Todo'])==15)
for t in HID: row(f'M_{t}',5,lambda x,t=t: x['mv'].get(t)=='Todo')
for t,ww in [('ZOM-392',3),('ZOM-550',5)]: row(f'M_{t}',ww,lambda x,t=t: x['mv'].get(t)=='Todo')
row('C0_15',5,lambda x:len(x['cm'])==15)
for t in HID: row(f'C_{t}',3,lambda x,t=t: IMP[t].lower() in (x['cm'].get(t) or '').lower())
row('C_ZOM-503',3,lambda x:'#52' in (x['cm'].get('ZOM-503') or ''))
row('C_ZOM-392',3,lambda x:'#41' in (x['cm'].get('ZOM-392') or ''))
res={k:{rid:bool(fn(x)) for rid,w,fn in rows} for k,x in R.items()}
W={rid:w for rid,w,_ in rows}
sc={k:sum(W[r] for r,p in v.items() if p)/sum(W.values()) for k,v in res.items()}
print('rows',len(rows),'weight',sum(W.values()),'bands',{b:sum(1 for w in W.values() if w==b) for b in(5,3,1)})
print('scores',{k:round(v,3) for k,v in sc.items()},'avg %.3f sd %.3f'%(st.mean(sc.values()),st.pstdev(sc.values())))
data={'task_type':'long-horizon','rubrics':[{'id':r,'weight':w,'valid':True} for r,w,_ in rows],
 'rollouts':[{'id':f'run-{k}','status':'completed','tool_calls':200,'results':res[k]} for k in res]}
out=ds.compute(data)
for g,v in out['gates'].items(): print(g,v['verdict'],str(v.get('value'))[:120])
allfail=[r for r in W if not any(res[k][r] for k in res)]; allpass=[r for r in W if all(res[k][r] for k in res)]
print('allfail',allfail); print('allpass',allpass)
for k in res: print(k,'fails:',[r for r,p in res[k].items() if not p])
