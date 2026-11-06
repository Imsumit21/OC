#!/usr/bin/env python3
"""Writes research/tool_out/lb_ids.txt (the load-bearing ids for persona_view check-sql) from records.json."""
import json
from pathlib import Path
WF = Path(__file__).resolve().parents[1]
L = json.loads((WF / "scenario_gen" / "records.json").read_text())
lb = []
for r in L:
    if r["service"] not in ("slack", "gmail", "gdrive", "gcal", "gdocs", "gsheets") or r.get("op") == "update":
        continue
    if r["service"] == "gcal" and not r["id"].startswith("evt_81e6"):
        continue
    if r["service"] == "gmail" and not r["id"].startswith("vincent.parker@"):
        continue
    if r["service"] == "gsheets" and "#" in r["id"]:
        continue
    lb.append(r["id"])
base = ["C05433XK267/1759257934.076209", "C05433XK267/1759257812.041449", "C05433XK267/1759268201.182309",
        "C05433XK267/1759263189.219529", "C05433XK267/1759259749.259909", "C05433XK267/1759267266.044859",
        "C08R27X0EAH/1758485492.586459", "C08R27X0EAH/1758409417.505029", "D079SNE2TL4/1759256193.859279",
        "D079SNE2TL4/1759269524.769369", "C05433XK267/1756826078.213299"]
(WF / "research" / "tool_out" / "lb_ids.txt").write_text("\n".join(sorted(set(lb)) + base) + "\n")
print(len(lb) + len(base), "load-bearing ids")
