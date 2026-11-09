#!/usr/bin/env python3
"""Per-run read behaviour from exports: which containers each run opened, which queries it ran (for placing corrections)."""
import json, sys, re, collections, os
def events(path):
    raw = open(path).read()
    try:
        d = json.loads(raw); return d if isinstance(d, list) else d.get("events") or d.get("messages") or [d]
    except Exception:
        return [json.loads(l) for l in raw.splitlines() if l.strip().startswith("{")]
def calls(path):
    out, res = [], {}
    for e in events(path):
        if not isinstance(e, dict): continue
        m = e.get("message") or {}
        for c in m.get("content") or [] if isinstance(m.get("content"), list) else []:
            if not isinstance(c, dict): continue
            if c.get("type") == "tool_use": out.append([c["id"], c["name"].split("__")[-1], c.get("input", {}), ""])
            if c.get("type") == "tool_result":
                t = c.get("content")
                res[c.get("tool_use_id")] = json.dumps(t, ensure_ascii=False) if not isinstance(t, str) else t
    for o in out: o[3] = res.get(o[0], "")
    return out
if __name__ == "__main__":
  runs = {a.split("=", 1)[0]: calls(a.split("=", 1)[1]) for a in sys.argv[1:]}
  names = collections.Counter()
  for lab, cs in runs.items():
      for c in cs: names[c[1]] += 1
  print("tool names over all runs:", dict(names.most_common(60)))
  for lab, cs in runs.items():
      print(f"\n===== {lab} ({len(cs)} calls)")
      for _, n, i, r in cs:
          if n.startswith(("gmail", "github")) or (n.startswith("slack") and n not in ("slack_send_message",)) or n in ("linear_search_issues", "linear_get_issue") or n.startswith(("trello", "gdrive_search", "gdocs")):
              print(f"  {n} {json.dumps(i, ensure_ascii=False)[:150]}  -> {len(r)} chars")
