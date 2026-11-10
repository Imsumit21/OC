import sys, json, re, collections
sys.path.insert(0, ".")
import traj_lib as T
c = T.load("B1")[1][10]; d = T.unwrap(c["out"])
for vr in d["valueRanges"]: print(vr["range"], "rows incl header", len(vr["values"]), "header", vr["values"][0][:4])
pc = T.load("PC")[1]
print([ (x["seq"], x["name"]) for x in pc[8:21] ])
b = [x for x in pc if x["name"]=="Bash"][:3]
for x in b: print(x["seq"], json.dumps(x["input"])[:230], "=>", (T.text(x["out"]) or "")[:200].replace("\n"," / "))
hits = collections.Counter()
for r in T.RUNS:
    raw = open(T.RUNS[r], encoding="utf8").read()
    for n in ("trello_get_board_actions","gsheets_get_spreadsheet","inputSchema","input_schema"):
        hits[(r, n)] = raw.count(n)
print({k:v for k,v in hits.items() if v})
ev = T.load("B4")[0]
for e in ev:
    if e.get("type")=="user":
        s = json.dumps(e["message"]["content"])
        i = s.find("trello_get_board_actions")
        if i>=0: print("B4 ctx:", s[max(0,i-200):i+500]); break
print("B5 Read me route:", [ (x["seq"], x["name"]) for x in T.load("B5")[1] if x["name"] in ("gsheets_values_batch_get",)])
print("linear ids in sheet Unity: count", )
