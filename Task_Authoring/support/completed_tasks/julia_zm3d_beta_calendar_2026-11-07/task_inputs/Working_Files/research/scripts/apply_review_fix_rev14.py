#!/usr/bin/env python3
"""Revision 14: the two items from the last cold P1 on revision 13 (sha 1f2175a2...). P2e cold: 0 fail-level, 0 low-impact. Eval 0 PASS. Brief wording only.
No graded value changes. Pure text transform, asserted anchors.

  1. Config locks: "you tell its owner" replaces the passive "its owner is told", so the reply to Brian is plainly Julia's job (every P1 called the passive the thinnest kill).
  2. Span: says which Endless cadence goes in the Windows cell.

Usage: apply_review_fix_rev14.py <in.sql> <out.sql>
"""
import hashlib
import json
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest() == "1f2175a297fd390960f22c3767f790fc980a881023affa6ece970745fb40289b", "unexpected input revision"


def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, f"anchor count {n} != {count}: {old[:100]!r}"
    s = s.replace(old, new)


rep("moves to any time before it and its owner is told in a reply on the mail where they committed to it.",
    "moves to any time before it and you tell its owner in a reply on the mail where they committed to it.")
rep("each opening 00:00 UTC.\nScope\n", "each opening 00:00 UTC. Endless goes down as its weekly windows, with the daily reset noted.\nScope\n")

k = s.index("'ZM3D beta live-ops calendar - working rules\nFrederick")
e = s.index("', '[{\"start\":0", k)
body = s[k + 1:e].replace("''", "'")
m = re.compile(r"'(\[\{\"start\":0.*?\}\])'").search(s, e)
runs = json.loads(m.group(1))
HEADS = ["ZM3D beta live-ops calendar - working rules", "Span and time base", "Scope", "When a beat starts", "Held or not", "One-offs", "Still to do", "Push copy", "Config locks"]
for r, h in zip(runs, HEADS):
    i = 0 if h == HEADS[0] else body.index("\n" + h + "\n") + 1
    r["start"], r["end"] = i, i + len(h)
s = s[:m.start(1)] + json.dumps(runs, separators=(",", ":")) + s[m.end(1):]

open(dst, "w", encoding="utf-8").write(s)
print("written", dst, hashlib.sha256(s.encode()).hexdigest(), len(s.encode()), "bytes")
