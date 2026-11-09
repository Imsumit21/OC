#!/usr/bin/env python3
"""Which seeded records reached each run's tool results (exposure), by a distinctive 40-character slice of each seed's text."""
import json, sys, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from behaviour import calls
seeds = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "plan", "seed_text.json")))
def probes(txt):
    t = re.sub(r"\s+", " ", txt)
    return [t[i:i + 40] for i in (0, len(t) // 3, 2 * len(t) // 3) if len(t) > 50] or [t[:40]]
runs = {}
for a in sys.argv[1:]:
    lab, p = a.split("=", 1)
    blob = re.sub(r"\s+", " ", "\n".join(r for *_, r in calls(p)).replace("\\n", " ").replace('\\"', '"').replace("\\u2019", "’"))
    runs[lab] = blob
print("seed".ljust(14), " ".join(l.rjust(4) for l in runs), " caught/where")
for k, v in seeds.items():
    pr = probes(v["text"])
    row = ["yes" if any(x in runs[l] for x in pr) else "-" for l in runs]
    print(k.ljust(14), " ".join(r.rjust(4) for r in row), f" {sum(r == 'yes' for r in row)}/{len(row)}  {v['service']}:{v['id'][:40]}")
