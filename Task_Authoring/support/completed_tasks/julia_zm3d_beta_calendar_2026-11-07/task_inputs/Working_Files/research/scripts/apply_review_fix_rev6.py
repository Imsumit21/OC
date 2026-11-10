#!/usr/bin/env python3
"""Revision 6: the last items from the independent /prompt round on revision 5 (sha 3c035f2a...).

That round scored Cross-Service Coherence clean and every other dimension 5 except Unique Ground
Truth, which failed on one fork: nothing said whether the Oct 13 quest set has to land for the beta.
Pure text transform, asserted anchors.

  1. Trello quest note: says outright that nothing in the beta waits on the new set (settles the fork).
  2. ZOM-544: drops the "Google Play login is waiting on the backend" sentence, which read as the
     brief's "unverified build or platform" case although sign-in is not a beat, and the branch name
     (no such branch can be traced in the repository).
     ZOM-526: a Sep 30 note says what is left after the Collect and Win trigger merged (Axe Arena,
     postponed for the beta), so the ticket's In Progress state matches the merged work.
  3. Brian's Sep 22 mail: drops "from the September handoff" (no such handoff exists in the base).
  4. Drive: the Doc and Sheet rows go back to NULL size / content_path, as in every earlier revision;
     a path with no bytes behind it could fail a download at run time.
  5. Gmail: empty-string reply fields on non-reply mail and the ARCHIVED label on Brian's sent
     copies, as in the base.

Usage: apply_review_fix_rev6.py <in.sql> <out.sql>
"""
import hashlib
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest() == "3c035f2af02934538a1e07d04fe82a2ea2f0a7b8031cff8ca1bd53eb4217bc6f", "unexpected input revision"


def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, f"anchor count {n} != {count}: {old[:100]!r}"
    s = s.replace(old, new)


# 1. quest note
rep("New quest set goes in with the Mon Oct 13 rollover, the current set carries the first week.",
    "New quest set goes in with the Mon Oct 13 rollover if it is ready. Nothing in the beta waits on it, the current set runs the whole time either way.")

# 2. ZOM-544
rep("Apple sign-in works from the settings menu on the auth branch, but progress does not restore yet: "
    "levels, currencies and cards are not synced. Google Play login is still waiting on the backend setup.",
    "Apple sign-in works from the settings menu, but progress does not restore yet: "
    "levels, currencies and cards are not synced.")

# 2b. ZOM-526: after the Collect and Win trigger landed (#468 on Sep 29, queue manager #472 on Sep 30 15:53Z) the ticket is
#     still In Progress in base; the only token travel left is Axe Arena, which Brian postponed for the beta on Sep 22
rep("What is left is the Collect and Win trigger I mentioned above. It is polish on an effect that already ships for Season Pass, "
    "and the event runs without it, so it does not have to land before the beta.",
    "What is left is the Collect and Win trigger I mentioned above and, once that event is back, Axe Arena. "
    "It is polish on an effect that already ships for Season Pass, and the events run without it, so it does not have to land before the beta.")
T526 = "2025-09-30T16:24:19Z"
rep("UPDATE linear.linear_issues SET updated_at = '2025-09-26T15:40:50Z' WHERE id = 'ZOM-526';",
    "INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) "
    "VALUES ('cmt_zom526_3', 'ZOM-526', 'usr_49b9dfa5208d400d', NULL, 'Collect and Win tokens go through the queue manager now (#472). "
    f"Only the Axe Arena travel is left here, and that waits on the event coming back.', false, '{T526}', '{T526}', 3);\n"
    f"UPDATE linear.linear_issues SET updated_at = '{T526}' WHERE id = 'ZOM-526';")

# 3. Brian's Sep 22 mail (three mailbox copies)
rep("Nothing else changes from the September handoff. If anything moves on your side,", "Nothing else changes. If anything moves on your side,", 3)

# 4. Drive rows: no file path without bytes
rep("13872, false, false, 'frederick.stone@harmonygames.co/ZM3D beta live-ops calendar - working rules.docx', NULL, NULL, NULL, NULL, NULL);",
    "NULL, false, false, NULL, NULL, NULL, NULL, NULL, NULL);")
rep("9216, false, false, 'julia.lawson@harmonygames.co/ZM Live Ops/ZM3D Beta Live-Ops Calendar.xlsx', NULL, NULL, NULL, NULL, NULL);",
    "NULL, false, false, NULL, NULL, NULL, NULL, NULL, NULL);")

# 5. Gmail shapes
rep(", NULL, NULL, NULL, '18", ", NULL, '', '', '18", 6)                     # payload_json, in_reply_to, references, mbox_from
rep('\'["SENT","Label_b19fb8d1b3"]\'', '\'["ARCHIVED","SENT","Label_b19fb8d1b3"]\'', 2)
rep('{"name":"X-Gmail-Labels","value":"Sent,Opened"}', '{"name":"X-Gmail-Labels","value":"Archived,Sent,Opened"}', 2)

open(dst, "w", encoding="utf-8").write(s)
print("written", dst, hashlib.sha256(s.encode()).hexdigest(), len(s.encode()), "bytes")
