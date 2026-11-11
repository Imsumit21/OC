#!/usr/bin/env python3
"""Fresh hg.py reads of the base records the OE ledger cites. Writes plan/oe_base.json."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); WS = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
ENV = {**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputs"}
sys.path.insert(0, HERE)
import reports as RP
def hg(*a):
    p = subprocess.run(["python3", "Task_Authoring/tools/hg.py", "search", *a], cwd=WS, env=ENV, capture_output=True, text=True, timeout=900)
    return json.loads(p.stdout)
def rec(svc, needle, key=None, limit=40):
    d = hg("search", svc, needle, "--limit", str(limit))
    for m in d["matches"]:
        if key is None or m["pointer"].endswith("/" + key):
            g = hg("get", svc, "--file", m["service_file"], "--pointer", m["parent_pointer"])
            return {"file": m["file"], "service_file": m["service_file"], "pointer": m["parent_pointer"], "rec": json.loads(g["text"])}
    return None
out = {"slack": {}, "linear": {}, "github": {}}
keys = dict(RP.MAIN_BUILDS); keys.update(RP.BRANCH_BUILDS); keys["Android Submission #135"] = "C05433XK267/1759263189.219529"
extra = {"v_ok": "D06UPGF5PQV/1758820544.160399", "c_tested": "D06UPGF5PQV/1758817744.353289", "subm_root": "C08R27X0EAH/1757939514.864549", "endless_root": "C08R27X0EAH/1757467270.178829",
         "julia": "D05HYDTG5TJ/1756838837.147599", "park_a": "D06UPGF5PQV/1758806199.381319", "park_b": "D0770ET6WBW/1758808795.588519", "skip": "C08R27X0EAH/1758903616.346579", "iconvfx": "D06UPGF5PQV/1758721951.996909"}
for name, k in list(keys.items()) + list(extra.items()):
    r = rec("slack", k.split("/")[1], "ts")
    assert r and r["rec"].get("ts") == k.split("/")[1], (name, k)
    r["name"] = name; out["slack"][k] = r
for t in ("ZOM-543", "ZOM-556", "ZOM-560"):
    out["linear"][t] = rec("linear", t, "identifier") or rec("linear", t, "id")
for n in (465, 472, 473, 475):
    out["github"][str(n)] = rec("github", f"harmonygames-Games/match3d#{n}", "id")
json.dump(out, open(os.path.join(HERE, "oe_base.json"), "w"), indent=1)
for k, v in out["slack"].items(): print(v["name"], k, v["service_file"], v["pointer"], json.dumps(v["rec"])[:150])
for k, v in out["linear"].items(): print(k, v and (v["service_file"], v["pointer"], list(v["rec"].keys())[:30]))
for k, v in out["github"].items(): print(k, v and (v["pointer"], v["rec"]["merged_at"]))
