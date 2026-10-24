#!/usr/bin/env python3
"""Scratch: parse a task's baseline verifier results (Run #N blocks, tab-separated title/Pass|Fail) + rubric JSON into the
difficulty_stats.py input JSON and a per-criterion pass matrix. Read-only on inputs.

Usage: python3 verifier_matrix.py <task_dir> <task_type> <tool_calls_csv> <out_prefix> <rubric.json> <verifier.txt>
"""
import json, re, sys

task_dir, task_type, calls_csv, out = sys.argv[1:5]
RUB, VER = sys.argv[5], sys.argv[6]  # rubric json, verifier results
raw = open(RUB).read()
try:
    rub = json.loads(raw)
except json.JSONDecodeError:
    print("NOTE: 09_Rubrics.json is not valid JSON; falling back to line-based field extraction")
    rub, cur = [], None
    for line in raw.splitlines():
        m = re.match(r'\s*"(title|category|weight)":\s*(.*?),?\s*$', line)
        if not m:
            continue
        k, v = m.group(1), m.group(2)
        if k == "title":
            cur = {"title": v.strip().strip('"').replace('\\\\"', '"').replace('\\"', '"')}
            rub.append(cur)
        elif k == "category":
            cur["category"] = v.strip().strip('"')
        elif k == "weight":
            cur["weight"] = int(re.sub(r"\D", "", v))
def norm(t):
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    return t.replace('\\\\"', '"').replace('\\"', '"').strip()
titles = [norm(r["title"]) for r in rub]
txt = open(VER).read()
runs = re.split(r"^Run #(\d+)\s*$", txt, flags=re.M)
calls = [int(x) for x in calls_csv.split(",")]
rollouts, matrix = [], {}
for k in range(1, len(runs), 2):
    rid, body = runs[k], runs[k + 1]
    res = {}
    for line in body.splitlines():
        parts = line.split("\t")
        if len(parts) >= 2 and parts[1].strip() in ("Pass", "Fail"):
            t = norm(parts[0])
            if t in titles:
                res[f"C{titles.index(t)+1}"] = parts[1].strip() == "Pass"
            else:
                # fuzzy: prefix match
                hits = [i for i, x in enumerate(titles) if x[:80] == t[:80]]
                if len(hits) == 1:
                    res[f"C{hits[0]+1}"] = parts[1].strip() == "Pass"
                else:
                    print("UNMATCHED", rid, t[:100])
    missing = [f"C{i+1}" for i in range(len(titles)) if f"C{i+1}" not in res]
    if missing:
        print("run", rid, "missing", missing)
    rollouts.append({"id": f"run-{rid}", "status": "completed", "tool_calls": calls[int(rid) - 1], "results": res})
    matrix[rid] = res
data = {"task_type": task_type, "rubrics": [{"id": f"C{i+1}", "weight": r.get("weight", 1)} for i, r in enumerate(rub)], "rollouts": rollouts}
json.dump(data, open(out + "_stats_input.json", "w"), indent=1)
with open(out + "_matrix.md", "w") as f:
    f.write("| C | w | cat | " + " | ".join(f"r{k}" for k in matrix) + " | title |\n|---|---|---|" + "---|" * len(matrix) + "---|\n")
    for i, r in enumerate(rub):
        cid = f"C{i+1}"
        f.write(f"| {cid} | {r.get('weight', 1)} | {r.get('category','')[:3]} | " + " | ".join("P" if matrix[k].get(cid) else ("F" if cid in matrix[k] else "?") for k in matrix) + f" | {r['title'][:150]} |\n")
print("wrote", out)
