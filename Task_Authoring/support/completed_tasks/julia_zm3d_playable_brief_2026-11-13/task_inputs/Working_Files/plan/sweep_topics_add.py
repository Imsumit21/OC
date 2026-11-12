#!/usr/bin/env python3
"""Add topic searches to plan/out/sweep_base_topics.json through tools/hg.py (read-only, base data only), in the same
shape as the earlier entries: {count, complete, truncated, hits}. Usage: python3 -B sweep_topics_add.py <svc> "<term>" ...
(pairs). Used for the rev2 facts (Robert's note on the bathroom UVs, Brian's log on the re-sent recoloured models)."""
import json, os, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; TASK = HERE.parents[1]; ROOT = TASK.parents[1]
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=str(TASK))
p = HERE / "out" / "sweep_base_topics.json"; topics = json.loads(p.read_text())
args = sys.argv[1:]; assert args and len(args) % 2 == 0, "give <svc> <term> pairs"
for svc, term in zip(args[::2], args[1::2]):
    r = subprocess.run([sys.executable, "-B", str(TASK.parent / "tools" / "hg.py"), "search", "search", svc, term,
                        "--limit", "500", "--compact"], capture_output=True, text=True, cwd=ROOT, env=ENV)
    d = json.loads(r.stdout)
    hits = d.get("matches", [])
    topics.setdefault(svc, {})[term] = {"count": len(hits), "complete": d.get("scan_complete") is True,
                                         "truncated": bool(d.get("truncated")), "hits": hits}
    print(f"{svc} {term!r}: {len(hits)} hit(s), complete={d.get('scan_complete')}, truncated={d.get('truncated')}")
    for h in hits[:6]:
        print("   ", h.get("file", "")[-60:], h.get("pointer"), "|", (h.get("text") or "")[:140].replace("\n", " "))
p.write_text(json.dumps(topics, indent=1, ensure_ascii=False) + "\n")
