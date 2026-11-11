"""Print the matches of an `hg.py records` output. Usage: show.py <out.json> [maxchars]"""
import json
import sys

d = json.load(open(sys.argv[1], encoding="utf8"))
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
print("scan_complete", d.get("scan_complete"))
checks = d["checks"]
items = checks.items() if isinstance(checks, dict) else enumerate(checks)
for k, c in items:
    print("==", k, {a: b for a, b in c.items() if not isinstance(b, (list, dict))})
    for key in ("matches", "records", "found"):
        v = c.get(key)
        if isinstance(v, dict):
            v = [x for vv in v.values() for x in (vv if isinstance(vv, list) else [vv])]
        for m in v or []:
            r = m.get("record", m) if isinstance(m, dict) else m
            print(json.dumps(r, ensure_ascii=False)[:mx])
            print()
