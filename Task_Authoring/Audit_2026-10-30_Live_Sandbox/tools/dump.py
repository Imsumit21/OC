import json, sbq
Q1=json.load(open("Q1_tables_columns.json"))
COLS={}
for s,t,pos,col,dt,udt,nul,dflt,ml in Q1["rows"]:
    COLS.setdefault((s,t),[]).append(col)
def cols(s,t): return COLS.get((s,t),[])
def dump(label,sql,n=20,w=320,t=240):
    d=sbq.q(sql,timeout=t)
    print(f"--- {label} ---")
    if "error" in d: print("   ERR",str(d["error"])[:170]); print(); return
    print("   COLS:",d["columns"])
    for row in d["rows"][:n]: print("   ",json.dumps(row,default=str)[:w])
    print(f"   ({len(d['rows'])} rows)"); print()
