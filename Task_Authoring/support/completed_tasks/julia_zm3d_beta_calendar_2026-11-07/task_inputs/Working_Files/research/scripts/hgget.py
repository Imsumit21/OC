#!/usr/bin/env python3
"""Small wrappers over Task_Authoring/tools/hg.py (search / get with paging) for this task's research.

Import from other scripts:  sys.path.insert(0, <scripts dir>); from hgget import get, search, find_ptr
"""
import json, os, subprocess

ROOT = "/Users/sumitkumar/Source/Outlier/OC"
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputsS")


def _run(args):
    r = subprocess.run(["python3", "Task_Authoring/tools/hg.py", "search"] + args, cwd=ROOT, env=ENV,
                       capture_output=True, text=True)
    return json.loads(r.stdout)


def get(service, file, pointer=None, as_json=True):
    out, off = "", 0
    while True:
        a = ["get", service, "--file", file, "--max-chars", "600000"]
        if pointer:
            a += ["--pointer", pointer]
        if off:
            a += ["--offset", str(off)]
        d = _run(a)
        out += d["text"]
        if not d.get("truncated"):
            break
        off = d["next_offset"]
    return json.loads(out) if as_json else out


def search(service, query, file=None, limit=200, pointer=None):
    a = ["search", service, query, "--limit", str(limit)]
    if file:
        a += ["--file", file]
    if pointer:
        a += ["--pointer", pointer]
    return _run(a)


def find_ptr(service, file, value, depth=2):
    """Return the record pointer (first `depth` path segments) of the first match of value."""
    d = search(service, value, file=file, limit=5)
    for m in d.get("matches", []):
        parts = m["pointer"].split("/")
        return "/".join(parts[: depth + 1])
    return None
