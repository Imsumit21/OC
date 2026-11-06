#!/usr/bin/env python3
"""Read a full record/subtree through Task_Authoring/tools/hg.py get (paged), print parsed JSON to stdout."""
import json, os, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), *[".."] * 4))
def hg_get(service, file, pointer=None):
    out, off = [], 0
    while True:
        cmd = [sys.executable, os.path.join(ROOT, "Task_Authoring/tools/hg.py"), "search", "get", service, "--file", file,
               "--offset", str(off), "--max-chars", "4000000", "--compact"]
        if pointer: cmd += ["--pointer", pointer]
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT,
                           env={**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputs"})
        d = json.loads(r.stdout)
        if "text" not in d: raise SystemExit(r.stdout[:2000] + r.stderr[-2000:])
        out.append(d["text"])
        if not d.get("truncated"): break
        off = d["next_offset"]
    return json.loads("".join(out))
if __name__ == "__main__":
    svc, f = sys.argv[1], sys.argv[2]
    p = sys.argv[3] if len(sys.argv) > 3 else None
    json.dump(hg_get(svc, f, p), sys.stdout)
