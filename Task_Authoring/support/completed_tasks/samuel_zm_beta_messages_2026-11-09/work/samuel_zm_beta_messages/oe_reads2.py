#!/usr/bin/env python3
"""Second read batch for the OE ledger, through tools/hg.py only. Writes plan/oe_base2.json."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from oe_hg import hg, get, find, many
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "..", "tools")))
from base_check import parse_sql
sql = open(os.path.join(HERE, "..", "..", "01_Universe_Inject.sql")).read()
st = parse_sql(sql)
O = {}
def jl(x):
    try: return json.loads(x)
    except Exception: return None
# population: base issues updated Sep 23 to Sep 30
ptrs = set()
for d in range(23, 31):
    r = hg("search", "linear", f"2025-09-{d}", "--file", "data.json", "--pointer", "/issues", "--key", "updated_at", "--limit", 400)
    assert r.get("scan_complete"), d
    ptrs |= {m["parent_pointer"] for m in r.get("matches", [])}
F = ("identifier", "title", "state_id", "team_id", "updated_at")
res = many([(p + "/" + k, "linear", "data.json", p + "/" + k, 500) for p in ptrs for k in F])
pop = [{"pointer": p, "id": jl(res.get(p + "/identifier")), "title": jl(res.get(p + "/title")), "state": jl(res.get(p + "/state_id")),
        "team": jl(res.get(p + "/team_id")), "updated_at": jl(res.get(p + "/updated_at"))} for p in ptrs]
O["pop_base"] = sorted(pop, key=lambda r: str(r["id"]))
# authors of seeded comments and tickets
ids = sorted({str(x["row"].get(k)) for x in st if x["op"] == "insert" and x.get("table") in ("linear.linear_comments", "linear.linear_issues") for k in ("author_id", "creator_id", "assignee_id") if x["row"].get(k)})
O["users"] = {}
for u in ids:
    r = find("linear", u, "data.json", 3, pointer="/users")
    ms = [m for m in r.get("matches", []) if m["pointer"].endswith("/id")]
    if ms:
        x = jl(get("linear", "data.json", ms[0]["parent_pointer"], 1500)["text"]) or {}
        O["users"][u] = {"pointer": ms[0]["parent_pointer"], "email": x.get("email"), "name": x.get("name")}
    else:
        O["users"][u] = None
# Boss Arena in the base
O["boss"] = {}
for svc, f in (("confluence", "confluence_working.json"), ("linear", "data.json"), ("trello", "data.json")):
    r = find(svc, "Boss Arena", f, 12)
    O["boss"][svc] = [(m["pointer"], str(m["text"])[:200]) for m in r.get("matches", [])]
r = hg("search", "slack", "Boss Arena", "--file", "messages/C0880U9751A/2025-09.json", "--limit", 8)
O["boss"]["slack"] = [(m["pointer"], str(m["text"])[:200]) for m in r.get("matches", [])]
# look-alikes
O["like"] = {}
for z in ("ZOM-366", "ZOM-471", "ZOM-539"):
    ms = [m for m in find("linear", z, "data.json", 4).get("matches", []) if m["pointer"].endswith("/id")]
    x = jl(get("linear", "data.json", ms[0]["parent_pointer"], 3000)["text"]) if ms else None
    O["like"][z] = {"pointer": ms[0]["parent_pointer"] if ms else None, "title": (x or {}).get("title"), "state": (x or {}).get("state_id")}
ms = hg("search", "gsheets", "f_351b98dfb06f61fb8357d0", "--file", "data.json", "--limit", 3).get("matches", [])
if ms:
    base = "/".join(ms[0]["pointer"].split("/")[:3])
    O["twin"] = {"pointer": base, "title": jl(get("gsheets", "data.json", base + "/title", 200)["text"]),
                 "tabs": [jl((get("gsheets", "data.json", f"{base}/sheets/{i}/title", 200) or {}).get("text")) for i in range(3)],
                 "header": jl(get("gsheets", "data.json", base + "/sheets/0/grid/0", 1500).get("text"))}
ms = [m for m in hg("search", "gdocs", "f_ffbe775ff72a994c5d6b7c", "--file", "data.json", "--limit", 3).get("matches", [])]
O["gtm"] = [(m["pointer"], str(m["text"])[:80]) for m in ms]
json.dump(O, open(os.path.join(HERE, "oe_base2.json"), "w"), indent=0)
print({k: (len(v) if hasattr(v, "__len__") else v) for k, v in O.items()})
