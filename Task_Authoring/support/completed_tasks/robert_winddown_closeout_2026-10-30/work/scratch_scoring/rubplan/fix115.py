import json,re,sys
D,W=sys.argv[1],sys.argv[2]
def renum(s,letter):
    for n in range(112,117):
        s=re.sub(rf'\b{letter}{n}\b',f'{letter}{n-1}',s)
    return s
NEWB={'P82':3,'P86':3,'P102':3,'P108':3}
# rows.json
rows=[r for r in json.load(open(f'{D}/rows.json')) if r['P']!='P111']
for r in rows:
    if r['P'] in NEWB: r['band']=NEWB[r['P']]
    r['P']=renum(r['P'],'P')
json.dump(rows,open(f'{D}/rows.json','w'),indent=1,ensure_ascii=False)
# draft.py
s=open(f'{D}/draft.py').read()
s=re.sub(r'    elif P == "P111":\n(?:        .*\n)+?(?=    elif P == "P112")','',s)
s=renum(s,'P').replace('assert len(out) == 116','assert len(out) == 115')
open(f'{D}/draft.py','w').write(s)
# plan
p=open(f'{W}/09_Rubric_Writing_Plan.md').read().split('\n')
out=[]
for l in p:
    if re.match(r'\| P111[ |]',l): continue
    l=l.replace(', P111 |',' |')
    out.append(l)
p='\n'.join(out)
p=p.replace('P83–P111 comments, P112–P116 reply','P83–P110 comments, P111–P115 reply')
p=renum(p,'P')
open(f'{W}/09_Rubric_Writing_Plan.md','w').write(p)
print('rows',len(rows),'P111 left in plan:',p.count('| P111 |'), 'draft P111 branches', s.count('"P111"'))
