import json,glob
TD='/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/07_Baseline_Trajectories/'
K={'T1':'gusto pulls its invoice','T2':'free plan hides history','T3':"don't archive or delete",'T4':"Metabase isn",'T5':'Trello is part of the bundle',
'T6':'Pond5, Soundly','T7':'Pond5, Soundly','T8':'applovin','T9':'close the card on Feb 20','T10':'Sherwood','T11':'January line','T12':'same account as the quickbooks',
'T13':'lite plan, 3 seats','T14':'data delivery review','T15':'helpshift_export','T16':'6,250','T17':'Leave out people','T18':'docusign','T19':'ipostal',
'T20':'replaces my subscriptions sheet','T21':'combo fighter','T22':'Mar 15','T23':'$150 a month','T24':'1485','T25':'2,348.50'}
out={}
for f in sorted(glob.glob(TD+'*.json')):
    n=int(f.split('run-')[1][0]); d=json.load(open(f)); calls=[];res={}
    for e in d:
        if e.get('type')=='assistant':
            for c in e['message'].get('content',[]):
                if c.get('type')=='tool_use': calls.append(c)
        if e.get('type')=='user' and isinstance(e['message'].get('content'),list):
            for c in e['message']['content']:
                if isinstance(c,dict) and c.get('type')=='tool_result':
                    r=c.get('content'); res[c['tool_use_id']]=r if isinstance(r,str) else json.dumps(r)
    for t,k in K.items():
        hit=next((i for i,c in enumerate(calls,1) if k.lower() in (res.get(c['id']) or '').lower()),None)
        out.setdefault(t,{})[n]=hit
json.dump(out,open('cites.json','w'))
for t in K: print(t,out[t])
