#!/usr/bin/env python3
"""Revision 12: the verification round on revision 11 (sha 1348d287...). Eval 0 PASS; P3, P4 clean; the seven P1 and P2 samples converged on these.
No graded value changes. Pure text transform, asserted anchors.

  1. Window closes: stated once for every window, not only Collect & Win (P1a, P1b, P1c, P1d).
  2. Held row: "windows and weeks", so Weeks running is covered too (P1a, P1b, P1c).
  3. Scope: the shop's daily rotation is a reset a player sees and no rule excluded it (fresh P1d).
  4. Push copy: "Login Calendar" and "Weekly Rankings" are not wrong names (all P1 samples, fresh P1d); "what its row is missing"
     keeps a held beat or a note out of that cell.
  5. Vial note: says it is needed before the beta, as the icon note now does (P1a).
  6. Brian's ZOM-465 note: "ticked before that event merged" (base has Collect & Win work from August, so "came in" was loose; Eval 0, sync, P4).
  7. Trello payload: idCard and textData back, as on this board; the list stays out, so SC-13 is not repeated (Eval 0 ADV-18, P2a).
  8. ZOM-563: Douglas's note at his base prod update says it carried only teams and social and that the Collect & Win windows wait for Oct 8.
     This settles a private Sep 29 meeting line and Eval 0 ADV-1 (P2c). Vincent's check becomes the second comment.

Usage: apply_review_fix_rev12.py <in.sql> <out.sql>
"""
import hashlib
import json
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest() == "1348d287ac4a105c41b9f0bf511c6664e306adcc3cf42406688a228fd4b684e7", "unexpected input revision"


def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, f"anchor count {n} != {count}: {old[:100]!r}"
    s = s.replace(old, new)


# 1
rep("Every window is stated in server time (UTC) as a start-end instant.", "Every window is stated in server time (UTC) as a start-end instant, closing 23:59 UTC on its last day.")
rep("each opening 00:00 UTC and closing 23:59 UTC on its last day.\nScope\n", "each opening 00:00 UTC.\nScope\n")
# 2
rep("A held beat keeps its usual windows on its row, marked held.", "A held beat keeps its usual windows and weeks on its row, marked held.")
# 3
rep("Boss Arena is off this calendar until the pivot call.", "Boss Arena is off this calendar until the pivot call, and the shop rotation is not a beat.")
# 4
rep("names the game as Zombie Match 3D and events by their ZM3D names. Anything else is held, with what is missing.",
    "names the game as Zombie Match 3D and events by their ZM3D names (Login Calendar and Weekly Rankings are fine). Anything else is held, with what its row is missing.")

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

# 5: GitHub note and its #zombie-prs mirror
rep("The final vial models are missing, Claire has those on her list.", "The final vial models are missing and need to be in before the beta, Claire has those on her list.", 2)

# 6
rep("Keep it on this ticket, the master VFX list was written before that event came in.", "Keep it on this ticket, the master VFX list was ticked before that event merged.")

# 7
rep('"shortLink":"viBYIjSG"},"text":"More quests', '"shortLink":"viBYIjSG"},"idCard":"68c452a03006277f55d9dc96","text":"More quests')
rep('the current quests keep running either way."}', 'the current quests keep running either way.","textData":{"emoji":{}}}')

# 8
T = "2025-09-30T18:17:05Z"
rep("VALUES ('cmt_zom563_1', 'ZOM-563', 'usr_65c76e0b87aa7e9b', NULL, 'Checked on prod: teams'' lives, golden frames and names all work as expected. Closing.', false, '2025-09-30T22:04:33Z', '2025-09-30T22:04:33Z', 1);",
    f"VALUES ('cmt_zom563_1', 'ZOM-563', 'usr_cd7849ec043ab3da', NULL, 'Prod has the teams and social changes now. That update carried only these, the Collect & Win server windows wait for the Oct 8 release.', false, '{T}', '{T}', 1);\n"
    "INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) "
    "VALUES ('cmt_zom563_2', 'ZOM-563', 'usr_65c76e0b87aa7e9b', NULL, 'Checked on prod: teams'' lives, golden frames and names all work as expected. Closing.', false, '2025-09-30T22:04:33Z', '2025-09-30T22:04:33Z', 2);")

open(dst, "w", encoding="utf-8").write(s)
print("written", dst, hashlib.sha256(s.encode()).hexdigest(), len(s.encode()), "bytes")
