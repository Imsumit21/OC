#!/usr/bin/env python3
"""Run hg.py search-many for a service/file glob and a list of terms; summarise hits by container.

Usage: smany.py <service> <file_glob> <out_name> term1 term2 ...  [--limit N]
Writes research/raw/<out_name>.json (full hg.py output) and prints counts per term per container.
"""
import json, os, subprocess, sys, collections

ROOT = "/Users/sumitkumar/Source/Outlier/OC"
RAW = os.path.join(ROOT, "Task_Authoring/task_inputsS/Working_Files/research/raw")


def main():
    args = sys.argv[1:]
    limit = 400
    if "--limit" in args:
        i = args.index("--limit"); limit = int(args[i + 1]); del args[i:i + 2]
    service, glob, out = args[0], args[1], args[2]
    terms = args[3:]
    req = {"service": service, "file": glob,
           "queries": [{"id": f"q{i}", "query": t, "limit": limit} for i, t in enumerate(terms)]}
    rp = os.path.join(RAW, f"{out}.request.json")
    json.dump(req, open(rp, "w"))
    env = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputsS")
    r = subprocess.run(["python3", "Task_Authoring/tools/hg.py", "search", "search-many", "--request", rp],
                       cwd=ROOT, env=env, capture_output=True, text=True)
    try:
        d = json.loads(r.stdout)
    except Exception:
        print(r.stdout[:2000]); print(r.stderr[:2000]); sys.exit(1)
    json.dump(d, open(os.path.join(RAW, f"{out}.json"), "w"))
    for i, t in enumerate(terms):
        q = d["queries"][f"q{i}"]
        ms = q.get("matches", [])
        c = collections.Counter()
        for m in ms:
            sf = m.get("service_file", "")
            parts = sf.split("/")
            key = "/".join(parts[:3]) if service == "slack" else sf
            c[key] += 1
        print(f"== {t!r}: {len(ms)} matches complete={q.get('scan_complete')} truncated={q.get('truncated')}")
        for k, v in c.most_common(12):
            print(f"   {v:4d} {k}")


if __name__ == "__main__":
    main()
