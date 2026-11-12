#!/usr/bin/env python3
"""Print the tool call at an event index and its result (data only; python -I). Usage: event.py <export.json> <ev,ev,...> [chars]"""
import json, sys
path, evs = sys.argv[1], [int(x) for x in sys.argv[2].split(",")]
n = int(sys.argv[3]) if len(sys.argv) > 3 else 1200
ev = json.load(open(path))
def text_of(c):
    if isinstance(c, str): return c
    if isinstance(c, list): return "\n".join(text_of(x.get("text") if isinstance(x, dict) and "text" in x else (x.get("content") if isinstance(x, dict) else x)) for x in c)
    return json.dumps(c, ensure_ascii=False) if c is not None else ""
calls = {}
for i, e in enumerate(ev):
    m = e.get("message") if isinstance(e.get("message"), dict) else e
    c = m.get("content") if isinstance(m, dict) else None
    if not isinstance(c, list): continue
    for b in c:
        if not isinstance(b, dict): continue
        if b.get("type") == "tool_use": calls[b["id"]] = (i, b.get("name"), b.get("input"))
        if b.get("type") == "tool_result" and calls.get(b.get("tool_use_id"), (None,))[0] in evs:
            ci = calls[b["tool_use_id"]]
            print(f"=== call ev {ci[0]} {ci[1].split('__')[-1]} {json.dumps(ci[2], ensure_ascii=False)[:260]} -> result ev {i}")
            print(text_of(b.get("content"))[:n].replace("\\n", " "))
        if b.get("type") == "text" and i in evs: print(f"=== text ev {i}: {b.get('text', '')[:n]}")
