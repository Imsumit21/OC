import json, re, sys
sys.path.insert(0, "/tmp/claude-1000/-home-sumit-Desktop-OC/0eb6fcc3-ed7e-43b1-ab5b-04d624fcaa67/scratchpad/tools")
from af_evidence_lib import FILES, TI
run, pat = sys.argv[1], sys.argv[2]
evs = json.load(open(TI / "07_Baseline_Trajectories" / FILES[run]))
calls = {}
for n, ev in enumerate(evs):
    if isinstance(ev, dict) and ev.get("type") == "assistant":
        for c in (ev.get("message") or {}).get("content") or []:
            if isinstance(c, dict) and c.get("type") == "tool_use":
                calls[c["id"]] = (n, c["name"].replace("mcp__hg__", ""), json.dumps(c["input"])[:160])
for n, ev in enumerate(evs):
    if isinstance(ev, dict) and ev.get("type") == "user":
        for c in (ev.get("message") or {}).get("content") or []:
            if isinstance(c, dict) and c.get("type") == "tool_result":
                t = c.get("content"); t = t if isinstance(t, str) else json.dumps(t)
                for m in re.finditer(pat, t):
                    cn = calls.get(c.get("tool_use_id"))
                    print(f"result event {n} (call event {cn[0]} {cn[1]} {cn[2]})")
                    print("   ...", t[max(0, m.start()-250):m.end()+250].replace("\\n", " ").replace("\n", " "))
                    break
