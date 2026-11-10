import sys, json, collections
sys.path.insert(0, ".")
import traj_lib as T
# spills per run, and does tool_use_result carry the full body?
for r in T.RUNS:
    ev, calls = T.load(r)
    sp = [c for c in calls if (c["out"] or "").startswith("Error: result (")]
    print(r, "spills", len(sp), collections.Counter(c["name"] for c in sp).most_common())
ev, calls = T.load("B1")
c = calls[27]
for e in ev:
    if e.get("type") == "user":
        for b in e["message"]["content"] if isinstance(e["message"]["content"], list) else []:
            if isinstance(b, dict) and b.get("tool_use_id") == c["id"]:
                t = e.get("tool_use_result")
                print("tool_use_result type", type(t), str(t)[:300], len(str(t)))
