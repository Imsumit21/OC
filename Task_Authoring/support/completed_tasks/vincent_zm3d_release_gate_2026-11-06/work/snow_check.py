import json,re,sys
d=json.load(open(sys.argv[1]))
tabs=d['tables']
for i in (1,2,26,31,33):
    t=tabs[i]; print(i, t.get('name') or t.get('table') or [k for k in t if k!='rows'], len(t.get('rows',[])))
rx133=re.compile(r'(?<![A-Za-z0-9])133(?![A-Za-z0-9])'); rx135=re.compile(r'(?<![A-Za-z0-9])135(?![A-Za-z0-9])')
recs=[l.strip() for l in open(sys.argv[2])]
both=one=0; ex=[]
for r in recs:
    m=re.match(r'snowflake.json/tables/(\d+)/rows/(\d+)',r)
    row=tabs[int(m.group(1))]['rows'][int(m.group(2))]
    s=json.dumps(row)
    a,b=bool(rx133.search(s)),bool(rx135.search(s))
    if a and b: both+=1; ex.append((r,s[:300]))
    elif a or b: one+=1
print('records holding both 133 and 135:',both,' holding one:',one)
for e in ex[:5]: print(e)
