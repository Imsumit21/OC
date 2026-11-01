import json,collections
from decimal import Decimal as D
r=json.load(open('feed_rows.json'))
BANK=['AMAZON WEB SERVICES','GOOGLE *GSUITE','SLACK T','LINEAR','GITHUB','FIGMA','ATLASSIAN']
def cyc(p):
    y,m,d=map(int,p.split('-'))
    if (y,m)<(2025,6) or (y,m)==(2025,6) and d<=25:
        # closes 25th
        if d<=25: return f'{y}-{m:02d}' if y==2025 else None
        return f'2025-{m+1:02d}' if y==2025 else '2025-01'
    if (y,m)==(2025,6): return '2025-07'
    if (y,m)==(2025,7): return '2025-07' if d<=28 else '2025-08'
    if (y,m)==(2025,8): return '2025-08' if d<=28 else '2025-09'
    if (y,m)==(2025,9): return '2025-09' if d<=28 else '2025-10'
spend=[x for x in r if x['type'] in('purchase','fee','refund')]
# attach fee to vendor above on same sheet
prev={}
for x in r:
    if x['type']=='fee': x['vendor_desc']=prev[(x['sheet'],x['tab'])]
    elif x['type'] in ('purchase','refund'): x['vendor_desc']=x['descriptor']; prev[(x['sheet'],x['tab'])]=x['descriptor']
un=[x for x in spend if not any(x['vendor_desc'].startswith(b) for b in BANK)]
bank=[x for x in spend if any(x['vendor_desc'].startswith(b) for b in BANK)]
tot=collections.defaultdict(D)
for x in un:
    c=cyc(x['posted_date']); x['cycle']=c
    tot[c]+=D(str(x['amount_usd']))
for k in sorted(tot,key=str): print(k, tot[k])
print('Jan-Sep', sum(v for k,v in tot.items() if k and k<='2025-09'))
json.dump(un,open('unmatched.json','w'))
