import sys,re
W='/home/sumit/Downloads/OC/OC/Task_Authoring-2/support/task_work/fs_ua_trueup'; sys.path.insert(0,W)
import ids as I, model as M
P='/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/Working_Files/01_Grounding_Dossier.md'
t=open(P).read()
r=M.register(); rows=r['rows']; tot=r['totals']
a=t.index('### 9.2 Derived ground truth'); b=t.index('\nTotals (net):',a); c=t.index('\n',t.index('Snowflake',b+20))
old=t[a:b]
recs={}
for l in old.split('\n'):
    if l.startswith('| 20'):
        c_=[x.strip() for x in l.strip('|').split('|')]
        recs[tuple(c_[:4])]=c_[8]
def ptr(x):
    if x['network']=='Unity Ads':
        acct='CP' if 'Calm Play' in x['source'] else 'HG'
        return '; '.join(I.UNITY_STMT[k] for k,ac,p,_ in I.UNITY_PERIODS if ac==acct and p[:7]==x['month'])
    return recs.get((x['month'],x['network'],x['title'],x['bucket']),'')
miss=[x for x in rows if not ptr(x)]
assert not miss, miss[:3]
head='### 9.2 Derived ground truth (`model.py register()`, from the records above; for the human\'s Oracle Events and rubric)\n\n| Month | Network | Title | Bucket | Spend (USD) | Credit used (USD) | Net cost (USD) | Source | Records |\n|---|---|---|---|---|---|---|---|---|\n'
body='\n'.join(f"| {x['month']} | {x['network']} | {x['title']} | {x['bucket']} | {x['spend']:,.2f} | {x['credit']:,.2f} | {x['net']:,.2f} | {x['source'].replace('account ending 3125','company account 907669287942378')} | {ptr(x)} |" for x in rows)
newtot=f"\nTotals (net): Fundraising ${tot['Fundraising']:,.2f} · Real UA ${tot['Real UA']:,.2f} · all ${r['grand_total']:,.2f} (Snowflake\n${r['snowflake_total']:,.2f})."
t=t[:a]+head+body+'\n'+newtot+t[c:]
open(P,'w').write(t)
print(len(rows), tot, r['grand_total'])
