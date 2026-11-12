#!/usr/bin/env python3
"""Re-read, through tools/hg.py, every base record the Oracle Event path relies on. Read-only on the universe.
Writes oe_gen/out/base_records.json: pointer -> {file, pointer, record}. Run from the workspace root."""
import datetime as D, json, os, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
TASK = HERE.parents[1]
ROOT = TASK.parents[1]
TOOLS = TASK.parent / "tools"
sys.path.insert(0, str(HERE.parent / "plan"))
import design_model as M
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=str(TASK))
def hg(*a):
    p = subprocess.run([sys.executable, "-B", str(TOOLS / "hg.py"), "search", *a, "--compact"], capture_output=True, text=True, cwd=ROOT, env=ENV)
    try: return json.loads(p.stdout)
    except ValueError: return {"error": (p.stderr or p.stdout)[:400]}
def slack(ptr):
    ch, ts = ptr.split("/")
    month = D.datetime.fromtimestamp(float(ts), D.timezone.utc).strftime("%Y-%m")
    f = f"messages/{ch}/{month}.json"
    s = hg("search", "slack", ts, "--key", "ts", "--file", f, "--limit", "3")
    m = [x for x in s.get("matches", []) if x.get("text") == ts]
    if not m: return {"error": "not found", "search": s}
    g = hg("get", "slack", "--file", f, "--pointer", m[0]["parent_pointer"], "--max-chars", "20000")
    return {"file": f, "pointer": m[0]["parent_pointer"], "scan_complete": s.get("scan_complete"), "record": g.get("value", g)}
out = {}
# the 22 Sep #zombie-design thread on what the scenario is for (sweep fork F30, settled: Robert walks the hardcore line back)
EXTRA_SLACK = {"purpose_robert_22sep": "C090N54TG79/1758569655.409719", "purpose_julia_22sep": "C090N54TG79/1758569707.508219",
               "purpose_robert_matter": "C090N54TG79/1758569872.578829"}     # /oe round 1: Robert's walk-back, with robert_remain
for key, ptr in list(M.BASE.items()) + list(EXTRA_SLACK.items()):
    if "/" in ptr and ptr[0] in "CD" and "#" not in ptr:
        out[key] = dict(slack(ptr), id=ptr)
        r = out[key].get("record")
        t = (r.get("text") if isinstance(r, dict) else str(r)) or ""
        print(key, ptr, "|", str(t)[:110].replace("\n", " "), "| ERR" if "error" in out[key] else "")
(HERE / "out" / "base_records.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
