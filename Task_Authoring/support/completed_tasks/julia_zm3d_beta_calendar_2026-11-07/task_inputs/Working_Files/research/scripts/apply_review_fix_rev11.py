#!/usr/bin/env python3
"""Revision 11: the formal blind round on revision 10 (sha ffbac458...). Three independent P1 passes and the main reviewer converged on one short
list; none reopened the open-set family that failed the platform. No graded value changes. Pure text transform, asserted anchors.

  1. Collect & Win icon: the only cover was its owner's note, and comparable polish was released on ZOM-565. Brian, who owns the list, says it has
     to land (ZOM-465). All three P1 passes and the main review raised this.
  2. A held beat's window cells had no rule: "A held beat keeps its usual windows on its row, marked held."
  3. "login calendar" on the push copy: the brief says it is the same beat, so it is not a wrong name.
  4. Window edges: "Clip anything that starts before or runs past that to those two instants" and "closing 23:59 UTC on its last day".
     Season Pass first window, the November end and the Collect & Win end instants each stop being a both-fair figure.
  5. Moved date: "moves to any time before it" states the acceptance boundary outright.
  6. UA deck: slides 1 and 2 agree with slide 3 (the spend stays small until the pivot call).
  7. Trello note: base shape with no list field (1 base commentCard has it), so it no longer repeats the SC-13 list-name mismatch.
  8. #zm-collect-win: Douglas answers Brian's Sep 26 reward-table request in its thread.
  9. P2b: ZOM-542 moves to Todo; Brian's note explains why the master list keeps its icons tick; Robert's approval drops two terms no record had coined.
 10. Robert's withdrawal ends at "Sorry for the flip.": the rest echoed a brief he cannot see, and nothing needs it.

Usage: apply_review_fix_rev11.py <in.sql> <out.sql>
"""
import calendar
import hashlib
import json
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest() == "ffbac4586fb91842ca16263c2b76987c26623c7ed689e00d33886c63f9331bdc", "unexpected input revision"


def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, f"anchor count {n} != {count}: {old[:100]!r}"
    s = s.replace(old, new)


def epoch(iso):
    return calendar.timegm((int(iso[0:4]), int(iso[5:7]), int(iso[8:10]), int(iso[11:13]), int(iso[14:16]), int(iso[17:19])))


SLACK_COLS = ("INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, "
              "reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, metadata_json) ")
LINEAR_COLS = "INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) "

# brief
rep("the four buy weeks in my UA plan. Every window is stated",
    "the four buy weeks in my UA plan. Clip anything that starts before or runs past that to those two instants. Every window is stated")
rep("Collect & Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC.\nScope\n",
    "Collect & Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC and closing 23:59 UTC on its last day.\nScope\n")
rep("say that instead of guessing a date.\nOne-offs\n", "say that instead of guessing a date. A held beat keeps its usual windows on its row, marked held.\nOne-offs\n")
rep("the daily gift (the Login Calendar row on the push sheet)", "the daily gift (Login Calendar on the push sheet, same beat)")
rep("A committed date that misses the lock moves earlier and its owner is told", "A committed date that misses the lock moves to any time before it and its owner is told")

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

# 1: icon
T465 = "2025-09-30T18:13:41Z"
rep("UPDATE linear.linear_issues SET updated_at = '2025-09-30T18:05:02Z' WHERE id = 'ZOM-465';",
    f"{LINEAR_COLS}VALUES ('cmt_zom465_3', 'ZOM-465', 'usr_fc22d5941b2aeb5c', NULL, 'Marcus, the Collect & Win icon does have to land before the beta, it is the one event icon with no animation. Keep it on this ticket, the master VFX list was written before that event came in.', "
    f"false, '{T465}', '{T465}', 3);\nUPDATE linear.linear_issues SET updated_at = '{T465}' WHERE id = 'ZOM-465';")

# 6: deck
rep("Scaled beta-cohort buy, starting once", "Beta-cohort buy, starting once")
rep("Small scale at first, scaled up week by week if the cohorts hold.", "Small scale at first, any scale-up comes after the pivot call.")

# 7: Trello payload
rep('"idCard":"68c452a03006277f55d9dc96","list":{"id":"6851a674975da1fe76e70d93","name":"BETA: Sep 30"},"text":"More quests', '"text":"More quests')
rep('the current quests keep running either way.","textData":{"emoji":{}}}', 'the current quests keep running either way."}')

# 8: reward tables
ch, parent, pts = "C09EVVCFHKR", "0069f6143e89802993b39e442d3baeb2", "1758899400.476649"
iso, micro = "2025-09-26T16:22:44Z", 713429
ts = f"{epoch(iso)}.{micro:06d}"
mid = hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]
row = (f"{SLACK_COLS}VALUES ('{mid}', '{ts}', '{ch}', 'message', 'EMPLOYEE_0031_SLACK_ID', 'Both tables are updated.', '{parent}', '{pts}', 0, 0, NULL, false, NULL, "
       f"'[]', '[]', '[]', '{iso[:-1]}.{micro:06d}Z', '{{}}');\n\n"
       f"UPDATE slack.slack_messages SET reply_count = 3, reply_users_count = 2, latest_reply = '{ts}' WHERE id = '{parent}';\n\n")
a = "UPDATE slack.slack_messages SET reply_count = 4, reply_users_count = 4, latest_reply = '1759250468.275139' WHERE id = 'a3e78e820b9f880ef4e3d941562110df';\n"
assert s.count(a) == 1
i = s.index(a) + len(a)
s = s[:i] + "\n" + row.rstrip("\n") + "\n" + s[i:]

# 9: Robert
rep("Sorry for the flip, my later word on this one is the one that counts.", "Sorry for the flip.")


# 10: P2b. ZOM-542 was never started, so Regression sat against its note; Todo fits it. Robert's approval used "beta weeks" and "the cut" before any record coined them.
rep("UPDATE linear.linear_issues SET updated_at = '2025-09-22T18:40:21Z' WHERE id = 'ZOM-542';", "UPDATE linear.linear_issues SET state_id = 'Todo', updated_at = '2025-09-22T18:40:21Z' WHERE id = 'ZOM-542';")
rep("approved from my side for one of the beta weeks.", "approved from my side for one week of the beta.")
rep("and I sign the object off if it lands before the cut.", "and I sign the object off if it lands in time.")


# 11: Eval 0 advisories on revision 10.
#     ZOM-563: naming "Douglas's teams update" put a Sep 30 prod update in front of Julia, a route to arguing the Collect & Win windows shipped early. The note needs no update at all.
rep("Checked on prod after Douglas''s teams update: teams''", "Checked on prod: teams''")
#     Premium strip: a date range in code has no trace (sprites are LFS pointers); the note speaks of the art. Mirror text follows the GitHub body.
rep("Separately, the Season Pass premium strip is still set to the October range.", "Separately, the Season Pass premium strip art still shows the October range.", 2)
#     Frederick's reply narrows his brief's naming rule, so it should not call that unstated.
rep("Two things the brief does not spell out.", "Two things on top of the brief.")
#     ZOM-504 and the shader note: exact wording.
rep("Still only shows up with the bot running;", "Re-tested: it only shows up with the bot running;")
rep("so it rides the next build and nothing has to land for the beta.", "so it rides the next store build and nothing has to land for the beta.")

open(dst, "w", encoding="utf-8").write(s)
print("written", dst, hashlib.sha256(s.encode()).hexdigest(), len(s.encode()), "bytes | ts", ts, mid)
