#!/usr/bin/env python3
"""Third read batch for the drafted events, through tools/hg.py only. Writes plan/oe_base3.json."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from oe_hg import hg, get, find, many
O = {}
def jl(x):
    try: return json.loads(x)
    except Exception: return None
for k in ("identifier", "title", "state_id"):
    O["boss_" + k] = jl(get("linear", "data.json", "/issues/3558/" + k, 300)["text"])
for z, p in (("ZOM-116", None), ("ZOM-363", None), ("ZOM-314", None), ("ZOM-553", None), ("ZOM-301", None)):
    ms = [m for m in find("linear", z, "data.json", 4).get("matches", []) if m["pointer"].endswith("/id")]
    pp = ms[0]["parent_pointer"]
    O[z] = {"title": jl(get("linear", "data.json", pp + "/title", 300)["text"]), "state": jl(get("linear", "data.json", pp + "/state_id", 80)["text"]), "desc": jl(get("linear", "data.json", pp + "/description", 1500).get("text"))}
r = hg("search", "trello", "commentCard", "--file", "data.json", "--pointer", "/actions", "--key", "type", "--limit", 900)
ptrs = [m["parent_pointer"] for m in r.get("matches", [])]
print("commentCard total", len(ptrs), r.get("scan_complete"))
res = many([(p + "/data/board/id", "trello", "data.json", p + "/data/board/id", 60) for p in ptrs])
O["zm_comments"] = sum(1 for v in res.values() if v and "6851a6569f3bf818760632ab" in v)
ms = find("trello", "6851a769c65dc0017a227bb7", "data.json", 2).get("matches", [])
O["pn_list"] = jl(get("trello", "data.json", "/cards/705/idList", 80)["text"])
O["pn_name"] = jl(get("trello", "data.json", "/cards/705/name", 200)["text"])
json.dump(O, open(os.path.join(HERE, "oe_base3.json"), "w"), indent=0)
print({k: (str(v)[:90]) for k, v in O.items()})
