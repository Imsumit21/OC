import re,json,collections,datetime as dt,sys
L=open(sys.argv[1],errors='replace').read().split('\n')
names={}
for i,l in enumerate(L):
    m=re.match(r"VALUES \('(f_[0-9a-f]+)', '(card_\d{4}_\d{4}-\d\d-\d\d)'",l)
    if m: names[m.group(1)]=m.group(2)
rows=[]; sheets=set(); adj=0
for i,l in enumerate(L,1):
    m=re.match(r"VALUES \('(f_[0-9a-f]+)', (\d+), '([^']+)', \d+, \d+, \d+, '(\[\[\"posted_date.*)'\);$",l)
    if m and m.group(1) in names:
        sheets.add(m.group(1)); tab=m.group(3)
        if tab!='Sheet1': adj+=1
        data=json.loads(m.group(4).replace("''","'"))
        for r in data[1:]:
            if len(r)>=9 and r[0] and r[0][:4]=='2025' or (len(r)>=9 and r[0][:4]=='2024'):
                rows.append(dict(zip(data[0],r),line=i,tab=tab,sheet=names[m.group(1)]))
print('sheets',len(sheets),'adj tabs',adj,'rows',len(rows),file=sys.stderr)
json.dump(rows,open('feed_rows.json','w'))
