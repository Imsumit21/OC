import sys, json
sys.path.insert(0, ".")
import traj_lib as T
for r in T.RUNS:
    ev, calls = T.load(r)
    for c in calls:
        if c["name"].startswith("trello_"):
            print(r, c["seq"], c["name"], json.dumps(c["input"]), "=>", len(c["out"] or ""), "ERR" if c["err"] else "")
ev, calls = T.load("B1")
c = calls[12]; print("\n=== B1#12 trello_search"); print(T.text(c["out"]))
ev, calls = T.load("B3")
c = calls[17]; print("\n=== B3#17 trello_search cards"); print(T.text(c["out"]))
c = calls[22]; print("\n=== B3#22 trello_get_comments"); print(T.text(c["out"]))
ev, calls = T.load("B4")
for s in (24, 27):
    c = calls[s]; print(f"\n=== B4#{s} trello_get_card err={c['err']}"); print(json.dumps(c["input"])); print(T.text(c["out"]))
ev, calls = T.load("B6")
for s in (25, 27):
    c = calls[s]; print(f"\n=== B6#{s} err={c['err']}"); print(T.text(c["out"]))
