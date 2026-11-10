#!/usr/bin/env python3
"""Revision 13: the cold reviewers' last items on revision 12 (sha b5ccbfa5...). P1d, P1f: no open fork. P1c, P2c, P3, P4, Eval 0: clean or advisory.
No graded value changes. Pure text transform, asserted anchors.

  1. Vial note (and its mirror): "first-pass models" did not fit git (Claire revised the model on Aug 14; P2d, the one low-impact item). It no
     longer calls the current models first-pass. "before the event runs" replaces "before the beta" (the Sep 30 builds were already out; Eval 0
     ADV-22), and "Not a blocker for this PR" removes the change-request reading (P1d B1).
  2. Brian's ZOM-465 note: "before the event runs", same reason.
  3. Scope: "the rotating shop", the company's term (P4).
  4. Push copy: "with which of those its row is missing", so a row's Details note is not part of that cell (P1e, the one open item).
  5. Trello payload: the list key is back, the exact shape the platform accepted and 14 base rows have (Eval 0 ADV-18). The platform marked the
     list name not scored.

Usage: apply_review_fix_rev13.py <in.sql> <out.sql>
"""
import hashlib
import json
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest() == "b5ccbfa577fc9f2c8f6eb3098f8d62a16623d799f41d11285de8227f1bed60d3", "unexpected input revision"


def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, f"anchor count {n} != {count}: {old[:100]!r}"
    s = s.replace(old, new)


# 1
TAIL_OLD = "vials that spawn in the levels are still the first-pass models. The final vial models are missing and need to be in before the beta, Claire has those on her list."
TAIL_NEW = "vials that spawn in the levels still need their final models before the event runs. Not a blocker for this PR, Claire has those on her list."
rep(TAIL_OLD, TAIL_NEW, 2)
# 2
rep("the Collect & Win icon does have to land before the beta, it is the one event icon with no animation.",
    "the Collect & Win icon does have to land before the event runs, it is the one event icon with no animation.")
# 3, 4
rep("and the shop rotation is not a beat.", "and the rotating shop is not a beat.")
rep("Anything else is held, with what its row is missing.", "Anything else is held, with which of those its row is missing.")

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

# 5
rep('"idCard":"68c452a03006277f55d9dc96","text":"More quests', '"idCard":"68c452a03006277f55d9dc96","list":{"id":"6851a674975da1fe76e70d93","name":"BETA: Sep 30"},"text":"More quests')

open(dst, "w", encoding="utf-8").write(s)
print("written", dst, hashlib.sha256(s.encode()).hexdigest(), len(s.encode()), "bytes")
