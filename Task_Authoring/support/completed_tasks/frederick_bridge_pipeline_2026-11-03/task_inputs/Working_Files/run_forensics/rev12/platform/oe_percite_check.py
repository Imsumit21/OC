import json,re,glob,sys
sys.path.insert(0,'Task_Authoring/tools')
from base_check import parse_sql
sql=open('Task_Authoring/task_inputs/01_Universe_Inject.sql').read()
L={}
for x in parse_sql(sql):
    r=x.get('row') or {}
    vals=[]
    for k,v in r.items():
        if isinstance(v,str):
            vals.append(v.replace('\\r\\n','\n').replace('\\n','\n'))
            try:
                j=json.loads(v)
                if isinstance(j,dict) and 'text' in j: vals.append(j['text'])
                if isinstance(j,list): vals+= [json.dumps(j,ensure_ascii=False)]
            except Exception: pass
    L[x['line']]='\n'.join(vals)
# SQL UPDATE grid line 31 raw
L[31]=sql.split('\n')[30].replace("''","'")
def S(*lines): return '\n'.join(L[l] for l in lines)
G='Universe_SynthCut/SynthCut_HarmonyGames_Gmail/Services_Data/gmail/threads/frederick@harmonygames.co_'
def T(*tids):
    out=[]
    for t in tids:
        d=json.load(open(G+t+'.json'))
        for m in d['messages']: out+= [m.get('subject',''), m.get('body','').replace('\r\n','\n'), m.get('to',''), m.get('from','')]
    return '\n'.join(out)
slack={}
for f in glob.glob('Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/messages/*/2025-09.json'):
    ch=f.split('/')[-2]
    for m in json.load(open(f)): slack[(ch,m['ts'])]=m.get('text','')
BP='\n'.join(v for (c,t),v in slack.items() if c=='C096HFA5Z8W')
cal=json.load(open('Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/gcal/data.json'))
CAL='\n'.join((e.get('summary') or '') for e in cal['events'] if e.get('calendar_id')=='frederick.stone@harmonygames.co')
tr=json.load(open('Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json'))
TRC='\n'.join(c['name'] for c in tr['cards'])
GRID=L[31]
SRC={1:S(137),2:S(19,22),3:S(32,37,39,43,45,49,51,55,57,61,63,67,69,73,75,79),4:S(86),5:GRID+'\nGame Investor List - Harmony Games 2025\nGame Investors List 25',
6:CAL+'\n'+S(274,283),7:BP+'\n'+S(88,90,92,94,96),8:T('1842277859335386393','1842278858600251474','1843988506059556678','1842279098258817066','1842285179768836773')+GRID,
9:T('1842278603974731778','1842279175401495849','1842278301421016623')+GRID,10:S(81),11:S(101,103,105),12:S(157,161),13:T('1842285743246816270'),
14:S(98)+slack[('C07C2866011','1759196326.309469')],15:T('1842277743427687737'),16:S(172),17:S(314,283),18:S(208,223),19:T('1843552279434086285'),
20:T('1843547312959065138'),21:T('1842277213140775733','1844748127814183717'),22:T('1832208184829815962'),23:T('1842283406259093714')+CAL,24:S(319),
25:T('1843473831194478743'),26:S(303,306,308,310,312),27:S(107,109),28:S(96),29:S(11,24,13),30:S(24),31:S(11),33:S(111,114)+TRC,34:TRC+S(117),35:CAL+S(291,295)}
oe=open('Task_Authoring/task_inputs/08_Oracle_Events.md').read()
evs=re.split(r'\n(?=OE \d+  )',oe)
bad=0
for ev in evs:
    n=int(re.match(r'OE (\d+)',ev).group(1))
    if n not in SRC: continue
    for line in ev.split('\n'):
        for sp in re.findall(r'"([^"]{3,})"',line):
            if sp in SRC[n]: continue
            bad+=1; print(f'OE {n}: NOT IN CITED RECORD: {sp[:100]}')
print('done; problems:',bad)
