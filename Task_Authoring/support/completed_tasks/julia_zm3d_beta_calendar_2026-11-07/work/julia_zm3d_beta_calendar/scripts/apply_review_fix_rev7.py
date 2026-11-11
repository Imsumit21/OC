#!/usr/bin/env python3
"""Revision 7: two last residuals from the independent reviews of revision 6 (sha f8d905bd...).

Both are wording or record-state items; neither changes a value the answer is graded on.
Pure text transform, asserted anchors.

  1. Trello quest note: "goes in ... if it is ready" and "the current set runs the whole time" only
     fit together if the new quests are additive (card name: "Add more quests"). Eval 0 advisory E1.
     The note now says they are added, and still says nothing in the beta waits on them.
  2. ZOM-521: PR #475 (card pack animation, Calvin Price) merged 2025-09-30T16:09:15Z while the
     master checklist keeps the cards item open and child ZOM-528 stays In Progress (SC-16 pattern,
     Eval 0 advisory D6). A Sep 30 note from Calvin records the merge and why the item stays open.
     No base Slack between the merge and the clock mentions this work.

Drive Doc/Sheet rows stay NULL size/content_path: id_contracts.json says NULL means no bytes, the
Doc and Sheet are served from their gdocs/gsheets rows, and a path with no bytes behind it is the
404 case the contract records.

Usage: apply_review_fix_rev7.py <in.sql> <out.sql>
"""
import hashlib
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest() == "f8d905bdd0c29585b17090b54aeb7837135f9d2462440ba71d81192d0871249c", "unexpected input revision"


def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, f"anchor count {n} != {count}: {old[:100]!r}"
    s = s.replace(old, new)


# 1. quest note
rep("New quest set goes in with the Mon Oct 13 rollover if it is ready. Nothing in the beta waits on it, the current set runs the whole time either way.",
    "More quests get added with the Mon Oct 13 rollover if they are ready. Nothing in the beta waits on them, the current quests keep running either way.")

# 2. ZOM-521 note after #475
T521 = "2025-09-30T16:27:38Z"
rep("Cards VFX is what I am on now.', false, '2025-09-26T17:25:02Z', '2025-09-26T17:25:02Z', 1);\n",
    "Cards VFX is what I am on now.', false, '2025-09-26T17:25:02Z', '2025-09-26T17:25:02Z', 1);\n"
    "INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) "
    "VALUES ('cmt_zom521_2', 'ZOM-521', 'usr_49b9dfa5208d400d', NULL, 'Card pack animation went in with #475. "
    f"I am leaving this item and ZOM-528 open until Brian has seen it in a build.', false, '{T521}', '{T521}', 2);\n")
rep("- [ ]   Claimed Cards traveling to inventory Section', updated_at = '2025-09-26T17:25:02Z' WHERE id = 'ZOM-521';",
    f"- [ ]   Claimed Cards traveling to inventory Section', updated_at = '{T521}' WHERE id = 'ZOM-521';")

open(dst, "w", encoding="utf-8").write(s)
print("written", dst, hashlib.sha256(s.encode()).hexdigest(), len(s.encode()), "bytes")
