import sys, json
sys.path.insert(0, ".")
import traj_lib as T
ev, calls = T.load("B1")
for i, e in enumerate(ev[:8]):
    print(i, e.get("type"), e.get("subtype"), list(e.keys())[:10])
    s = json.dumps(e, ensure_ascii=False)
    print("   ", s[:300])
r = ev[-1]
print("RESULT", {k: (str(v)[:400]) for k, v in r.items() if k not in ("message",)})
