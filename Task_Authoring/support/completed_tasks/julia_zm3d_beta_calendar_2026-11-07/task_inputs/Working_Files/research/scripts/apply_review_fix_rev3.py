#!/usr/bin/env python3
"""Revision 3 repair for the /prompt-2 FAIL (Cross-Service Coherence, SC-15).

Pure text transform of 01_Universe_Inject.sql with asserted anchor counts:
  1. ZOM-521 (VFX master ticket): the description UPDATE unticks the two checklist items whose
     child tickets are still In Progress in the base (ZOM-526 tokens, ZOM-528 claimed cards).
  2. ZOM-526: one later dated line from the ticket's creator that names the Season Pass part,
     says why the master tick was removed and that it does not have to land before the buy or
     the November season. The issue's updated_at follows the newest comment.
Nothing else changes. Usage: apply_review_fix_rev3.py <in.sql> <out.sql>
"""
import hashlib, sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest() == "3afbf7cbbdb7611dad909cfc7244829642e03e136b66c5c555fe77d28570dd63", "unexpected input revision"

def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, f"anchor count {n} != {count}: {old[:80]!r}"
    s = s.replace(old, new)

# --- 2. ZOM-526: later line + updated_at follows it
NEW_TS = "2025-09-26T15:40:00Z"
BODY = ("Unticked this one on the master ticket, it was marked done too early. The Season Pass part I mentioned above "
        "is polish on an effect that already ships: Season Pass runs without it, so it does not have to land before "
        "the beta buy or the November season.")
assert "'" not in BODY
rep("UPDATE linear.linear_issues SET updated_at = '2025-09-24T17:30:00Z' WHERE id = 'ZOM-526';",
    "INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) "
    f"VALUES ('cmt_zom526_2', 'ZOM-526', 'usr_fc22d5941b2aeb5c', NULL, '{BODY}', false, '{NEW_TS}', '{NEW_TS}', 2);\n"
    f"UPDATE linear.linear_issues SET updated_at = '{NEW_TS}' WHERE id = 'ZOM-526';")

# --- 1. ZOM-521: checklist matches the child tickets (base description, two ticks removed)
BASE_DESC = ("This is the master ticket for VFX polish\n\n- [X] End-game Level Animations\n- [X] End-game → Main Menu animations\n"
             "- [X] Live-ops icons appearing on the screen and animations on these icons\n- [X] Tokens traveling to live-ops\n"
             "- [X] Rewards in the claim scene traveling to their destinations\n- [X]   Claimed Cards traveling to inventory Section")
NEW_DESC = BASE_DESC.replace("- [X] Tokens traveling to live-ops", "- [ ] Tokens traveling to live-ops") \
                    .replace("- [X]   Claimed Cards traveling to inventory Section", "- [ ]   Claimed Cards traveling to inventory Section")
assert NEW_DESC != BASE_DESC and NEW_DESC.count("[ ]") == 2 and NEW_DESC.count("[X]") == 4 and "'" not in NEW_DESC
rep("UPDATE linear.linear_issues SET updated_at = '2025-09-26T17:25:00Z' WHERE id = 'ZOM-521';",
    f"UPDATE linear.linear_issues SET description = '{NEW_DESC}', updated_at = '2025-09-26T17:25:00Z' WHERE id = 'ZOM-521';")

open(dst, "w", encoding="utf-8").write(s)
print("written", dst, hashlib.sha256(s.encode()).hexdigest(), len(s.encode()), "bytes")
