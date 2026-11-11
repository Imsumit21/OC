import sys, json, re, collections
sys.path.insert(0, ".")
import traj_lib as T
def show(run, seq, m=1800, mi=1400):
    ev, calls = T.load(run); c = calls[seq]
    print(f"\n=== {run}#{seq} {c['raw']} err={c['err']}"); print("IN :", json.dumps(c["input"], ensure_ascii=False)[:mi]); print("OUT:", T.text(c["out"])[:m])
def first(run, name, n=1):
    ev, calls = T.load(run)
    return [c["seq"] for c in calls if c["name"] == name][:n]
show("B1", first("B1","gdocs_create_document")[0], 500, 700)
show("B4", first("B4","gdocs_create_document")[0], 900, 300)
show("B1", first("B1","gsheets_create_spreadsheet")[0], 800)
show("B1", first("B1","gsheets_batch_update")[0], 700, 400)
for s in first("B1","gsheets_values_update",3): show("B1", s, 320, 420)
s = first("B1","gdrive_share_file")[0]; show("B1", s, 900)
s = first("B1","linear_create_comment")[0]; show("B1", s, 900, 900)
ev, calls = T.load("B1")
ups = [c for c in calls if c["name"]=="linear_update_issue"]
show("B1", ups[0]["seq"], 1500, 300)
show("B1", 95, 2400, 1000)
show("B1", 96, 900, 300)
show("B1", 226, 2100, 900)
show("B4", 123, 300, 300); show("B4", 125, 300, 300)
show("B2", 99, 400, 500)
show("B1", 105, 800)
