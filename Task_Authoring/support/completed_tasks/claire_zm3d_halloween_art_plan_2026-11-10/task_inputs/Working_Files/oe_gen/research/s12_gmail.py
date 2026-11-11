import sys, json, re, collections
sys.path.insert(0, ".")
import traj_lib as T
print("=== all gmail_search/list inputs + result ids")
for r in T.RUNS:
    ev, calls = T.load(r)
    for c in calls:
        if c["name"] in ("gmail_search_messages","gmail_list_messages"):
            d = T.unwrap(c["out"])
            ks = list(d.keys()) if isinstance(d, dict) else type(d)
            n = len(d.get("messages", [])) if isinstance(d, dict) else None
            print(r, c["seq"], c["name"], json.dumps(c["input"]), "keys", ks, "n", n, {k:v for k,v in (d.items() if isinstance(d,dict) else []) if k!="messages"})
ev, calls = T.load("B2")
c = calls[6]; print("\n=== B2#6 full"); print(T.text(c["out"]))
ev, calls = T.load("B1")
print("\n=== B1#11 first 900"); print(T.text(calls[11]["out"])[:900])
print("\n=== B1#18"); print(T.text(calls[18]["out"]))
print("\n=== B1#20 get_thread full"); print(T.text(calls[20]["out"]))
print("\n=== B1#15 get_thread full"); print(T.text(calls[15]["out"]))
