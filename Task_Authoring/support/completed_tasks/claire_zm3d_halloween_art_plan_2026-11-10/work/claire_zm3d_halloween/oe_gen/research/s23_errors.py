import sys, json, re, collections
sys.path.insert(0, ".")
import traj_lib as T
print("=== is_error true / spills / short error-like outputs")
for r in T.RUNS:
    ev, calls = T.load(r)
    for c in calls:
        t = T.text(c["out"]) or ""
        d = T.unwrap(c["out"])
        flag = None
        if c["err"]: flag = "IS_ERROR"
        elif t.startswith("Error: result ("): flag = "SPILL"
        elif c["name"] in ("Bash","Read") and re.search(r"command not found|Traceback|No such file|Error|error:", t[:3000]): flag = "BASH?"
        elif isinstance(d, dict) and d.get("not_found"): flag = "NOT_FOUND"
        elif len(t) < 400 and re.search(r'"error"|\berror\b|invalid|not found|denied|forbidden', t, re.I): flag = "SHORT"
        if flag:
            inp = json.dumps(c["input"], ensure_ascii=False)
            print(f"[{flag}] {r}#{c['seq']} {c['name']} IN={inp[:230]}\n     OUT={t[:430]!r}")
print("\n=== empty results")
for r in T.RUNS:
    ev, calls = T.load(r)
    for c in calls:
        d = T.unwrap(c["out"])
        if isinstance(d, dict):
            for k in ("files","issues","channels","messages","items","comments","cards"):
                if k in d and d[k] == [] and c["name"] not in ("linear_list_comments",):
                    print(r, c["seq"], c["name"], json.dumps(c["input"])[:140], "empty", k)
print("\n=== list_comments empties")
for r in T.RUNS:
    ev, calls = T.load(r)
    e = [c["input"].get("issueId") for c in calls if c["name"]=="linear_list_comments" and T.unwrap(c["out"]) and T.unwrap(c["out"]).get("comments")==[]]
    print(r, e)
print("\n=== B3 ART-813 retry?")
ev, calls = T.load("B3")
print([ (c["seq"], c["err"]) for c in calls if c["name"]=="linear_create_comment" and c["input"].get("issueId")=="ART-813"])
print("\n=== B4 Agent events")
ev, calls = T.load("B4")
sub = collections.Counter(e.get("parent_tool_use_id") for e in ev if isinstance(e, dict) and e.get("parent_tool_use_id"))
print("events with parent_tool_use_id", sub)
for c in calls:
    if c["name"] == "Agent":
        print(c["seq"], json.dumps(c["input"], ensure_ascii=False)[:500]); print("OUT", T.text(c["out"]))
print("tool_progress", [json.dumps(e)[:200] for e in ev if e.get("type")=="tool_progress"][:2])
