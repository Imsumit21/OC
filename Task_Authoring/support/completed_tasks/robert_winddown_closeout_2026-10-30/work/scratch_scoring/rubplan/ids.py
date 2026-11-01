import sys, re; sys.argv=['x']; sys.path.insert(0,'/home/sumit/Downloads/OC/OC/Task_Authoring-2/tools')
import stage_gate as sg
from pathlib import Path
doc=sg.Doc(Path('plan_draft.md'),'plan')
led=sg.Doc(Path('/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/Working_Files/08_OE_Writing_Ledger.md'),'led')
lf={}
for i,c,t in sg.rows_in(led, r"^B\b"):
    m=re.match(r"\s*(F\d+)", c[0] if c else "")
    if m: lf[m.group(1)]=" ".join(c)
A=sg.rows_in(doc,r"coverage matrix")
cited={f for _,c,t in A for f in sg.RX_FID.findall(t.cell(c,t.col(r"values")))}
need=sorted({x for f in cited if f in lf for _,x in sg.scoped_ids(lf[f])})
print(sorted(cited, key=lambda x:int(x[1:])), file=sys.stderr)
print("\n".join(need))
