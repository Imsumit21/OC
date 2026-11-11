#!/usr/bin/env python3
"""Revision 9: the platform's third /prompt failure (FAIL 2: UGT and Clarity on ZOM-534, the S23 freeze and #477) on sha 0e8c8ad8...

Root cause: the brief's still-to-do and hold rules were open sets. "an unverified build or platform is a still-to-do" fed no truth value
but pulled in any open bug report, and the still-to-do list put no test on "prod deploy" or "config". A full census found about 90
candidates, so this revision closes the rule and adds records only where the platform asked for one or the rule cannot reach.
No graded value changes. Pure text transform, asserted anchors.

  A. Brief (no item named, no word pointing at a place):
     1. Held or not: "An established failure holds it; an unverified one does not."
     2. Still to do: a closed rule with a tail, and a cutoff at this brief. Passive "has been flagged", so it neither excludes a
        reviewer's flag nor points runs at reviews.
     3. When a beat starts: "which weeks it runs and whether its push goes out" (the sheet asks for both; the old text said "is ready").
     4. "A beat whose server windows are waiting on that release" replaces "only waiting" (Collect & Win also waits on art).
     5. Scope: "Not only the events everyone lists." removed; nothing depends on it.
     6. Difficulty: the Collect & Win cadence moves to "Span and time base".
     7. Difficulty: Push copy drops "only" twice, so Frederick's thread reply decides the no-name rows.
  B. Records the platform asked for:
     8. S23: Leonard's thread reply: a re-run on an S23 Ultra from the remote device list, no freeze. No cause or fix is claimed.
     9. ZOM-534: Leonard, who reported it, confirms on the store build. Douglas's note says "went out in the client builds", and drops
        "backend": the fix is client commit 47c65623e7, so the Oct 8 backend release does not apply.
    10. #477: Brian, who opened ZOM-566, says the header title and info text do not have to land first. Owen's note becomes the second comment.
  C. What the rule cannot reach, or a loose end in injected text:
    11. Sep 30 #zombie-bugs shader thread: Oliver's reply after 25c6c66b6b, which changes lightSweep Box Variant.mat.
    12. ZOM-563: Vincent's check on prod (his base DM of 21:58Z) and the ticket closes.
    13. Trello quest note also covers the card's reward balance.
    14. Brian's Sep 22 mail: the config contents follow the spec ("tiers, rewards, theme"), so no quest table reads as a Quests to-do.
    15. Pushes tab headers match what the task asks for.
  D. Difficulty: 16. Robert's withdrawal drops the search words, keeping the sentence the record is cited for.

Usage: apply_review_fix_rev9.py <in.sql> <out.sql>
"""
import calendar
import hashlib
import json
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest() == "0e8c8ad83f3be435db1f9268f114c916f52293993eb687a55b34005015f9f815", "unexpected input revision"


def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, f"anchor count {n} != {count}: {old[:100]!r}"
    s = s.replace(old, new)


def after(stmt, new):
    """Insert `new` after the statement that ends with `stmt`, keeping the file's blank-line spacing."""
    global s
    assert s.count(stmt) == 1, f"statement anchor {s.count(stmt)}: {stmt[:90]!r}"
    i = s.index(stmt) + len(stmt)
    s = s[:i] + new + s[i:]


def epoch(iso):
    return calendar.timegm((int(iso[0:4]), int(iso[5:7]), int(iso[8:10]), int(iso[11:13]), int(iso[14:16]), int(iso[17:19])))


SLACK_COLS = ("INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, "
              "reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, metadata_json) ")
LINEAR_COLS = "INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) "


def slack_reply(channel, iso, micro, user, text, parent_id, parent_ts):
    assert micro % 10 == 9, "base Slack ts end in 9"
    ts = f"{epoch(iso)}.{micro:06d}"
    mid = hashlib.sha256(f"{channel}|{ts}".encode()).hexdigest()[:32]
    return ts, (f"{SLACK_COLS}VALUES ('{mid}', '{ts}', '{channel}', 'message', '{user}', '{text}', '{parent_id}', '{parent_ts}', 0, 0, NULL, false, NULL, "
                f"'[]', '[]', '[]', '{iso[:-1]}.{micro:06d}Z', '{{}}');\n")


def comment(cid, issue, author, body, iso, seq):
    return f"{LINEAR_COLS}VALUES ('{cid}', '{issue}', '{author}', NULL, '{body}', false, '{iso}', '{iso}', {seq});\n"


# ---- A. brief
rep("An established failure holds it; an unverified build or platform is a still-to-do, not a hold.",
    "An established failure holds it; an unverified one does not.")
rep("For each beat, what still has to land before it runs for bought users (prod deploy, config, player-facing art an owner has flagged) and who owns it. "
    "Not what already shipped, not analytics, not polish nobody flagged.",
    "For each beat, what still has to land before it runs for bought users and who owns it: a held beat''s fix, and what has been flagged for that beat "
    "as not done since this brief (prod deploy, config or player-facing art). Nothing else goes in: not what already shipped, not analytics, not polish nobody flagged.")
rep("put down whether the beat is in and whether its push is ready, not its window dates.",
    "put down whether the beat is in, which weeks it runs and whether its push goes out, not its window dates.")
rep("not when its client PRs merged. Collect & Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC, so a window the release instant pre-empts does not count. "
    "A beat that is only waiting on that release starts late, it is not held.",
    "not when its client PRs merged. A window the release instant pre-empts does not count. "
    "A beat whose server windows are waiting on that release starts late, it is not held.")
rep("A PT/PDT rendering of the same instant is fine, a different instant is not.\nScope\n",
    "A PT/PDT rendering of the same instant is fine, a different instant is not. Collect & Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC.\nScope\n")
rep(" Not only the events everyone lists.", "")
rep("its English copy names the game only as Zombie Match 3D and events only by their ZM3D names.",
    "its English copy names the game as Zombie Match 3D and events by their ZM3D names.")

# heading offsets, recomputed from the new body
k = s.index("'ZM3D beta live-ops calendar - working rules\nFrederick")
e = s.index("', '[{\"start\":0", k)
body = s[k + 1:e].replace("''", "'")
m = re.compile(r"'(\[\{\"start\":0.*?\}\])'").search(s, e)
runs = json.loads(m.group(1))
HEADS = ["ZM3D beta live-ops calendar - working rules", "Span and time base", "Scope", "When a beat starts", "Held or not", "One-offs", "Still to do", "Push copy", "Config locks"]
assert len(runs) == len(HEADS)
for r, h in zip(runs, HEADS):
    i = 0 if h == HEADS[0] else body.index("\n" + h + "\n") + 1
    r["start"], r["end"] = i, i + len(h)
s = s[:m.start(1)] + json.dumps(runs, separators=(",", ":")) + s[m.end(1):]

# ---- B. the records the platform asked for
BUGS = "C08R27X0EAH"
S23_ID, S23_TS = "ede90bc6ec6cb16fd97663f2888f39a2", "1758420497.482989"
ts1, row1 = slack_reply(BUGS, "2025-09-29T21:41:37Z", 318279, "EMPLOYEE_0038_SLACK_ID",
                        "Ran this again on an S23 Ultra from the remote device list, live Android build, a few endless runs with the airstrike. "
                        "Could not get it to freeze, so I am leaving this one.", S23_ID, S23_TS)
SHADE_ID, SHADE_TS = "d0dd5d3ad4658add1f79802e2aa60e48", "1759249488.495439"
ts2, row2 = slack_reply(BUGS, "2025-09-30T21:24:52Z", 604719, "EMPLOYEE_0003_SLACK_ID",
                        "Pushed the fix for the lightSweep on the box. It is only that sweep on the art, it goes out with the next build and nothing waits on it.",
                        SHADE_ID, SHADE_TS)
ANCHOR = "UPDATE slack.slack_messages SET thread_ts_legacy = '1758121809.236839', reply_count = 1, reply_users_count = 1, latest_reply = '1758213623.552919' WHERE id = '9025d428af1f551a20e303c3acbc545b';\n"
after(ANCHOR, "\n" + row1 + "\n"
      f"UPDATE slack.slack_messages SET thread_ts_legacy = '{S23_TS}', reply_count = 1, reply_users_count = 1, latest_reply = '{ts1}' WHERE id = '{S23_ID}';\n\n"
      + row2 + "\n"
      f"UPDATE slack.slack_messages SET reply_count = 5, latest_reply = '{ts2}' WHERE id = '{SHADE_ID}';\n")

# ZOM-534
LEONARD, BRIAN, VINCENT = "usr_63fffeb4fab5233e", "usr_fc22d5941b2aeb5c", "usr_65c76e0b87aa7e9b"
rep("That is on main, so nothing else has to land for the beta. I am keeping this open to watch one backend timing edge case on the day boundary.",
    "That went out in the client builds, so nothing else has to land for the beta. I am keeping this open to watch one timing edge case on the day boundary.")
T534 = "2025-09-30T01:22:46Z"
rep("UPDATE linear.linear_issues SET updated_at = '2025-09-25T16:35:04Z' WHERE id = 'ZOM-534';",
    comment("cmt_zom534_2", "ZOM-534", LEONARD, "Stayed online through the 00:00 UTC reset on the store build tonight. Quest points reset on their own, no restart. "
            "That was my report, it is good on prod now.", T534, 2)
    + f"UPDATE linear.linear_issues SET updated_at = '{T534}' WHERE id = 'ZOM-534';")

# ZOM-566 / #477: Brian comes first in time, so Owen's note becomes the second comment
T566 = "2025-09-30T17:53:19Z"
rep("VALUES ('cmt_zom566_1', 'ZOM-566', 'usr_4e13bd40cc73d0fc', NULL, 'Collect and Win event list is mapped to the sheet (start and redeem). "
    "Wiring both into the analytics manager now, ahead of the beta.', false, '2025-09-30T19:40:47Z', '2025-09-30T19:40:47Z', 1);",
    "VALUES ('cmt_zom566_2', 'ZOM-566', 'usr_4e13bd40cc73d0fc', NULL, 'Collect and Win event list is mapped to the sheet (start and redeem). "
    "Wiring both into the analytics manager now, ahead of the beta.', false, '2025-09-30T19:40:47Z', '2025-09-30T19:40:47Z', 2);")
i = s.index("INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom566_2'")
s = s[:i] + comment("cmt_zom566_1", "ZOM-566", BRIAN, "Owen, analytics first. The header title and the info screen text can follow with it. "
                    "The event runs fine with the current text, so they do not have to land before the beta.", T566, 1) + s[i:]

# ---- C.
T563 = "2025-09-30T22:04:33Z"
j = s.index("UPDATE linear.linear_issues SET state_id = 'In Progress', started_at = '2025-09-30T17:20:13Z', updated_at = '2025-09-30T19:40:47Z' WHERE id = 'ZOM-566';")
j = s.index(";\n", j) + 2
s = s[:j] + "\n" + comment("cmt_zom563_1", "ZOM-563", VINCENT, "Checked on prod after the update: teams'' lives, golden frames and names all work as expected. Closing.", T563, 1) \
    + f"UPDATE linear.linear_issues SET state_id = 'Done', completed_at = '{T563}', updated_at = '{T563}' WHERE id = 'ZOM-563';\n" + s[j:]

rep("More quests get added with the Mon Oct 13 rollover if they are ready.", "More quests and the reward balance go in with the Mon Oct 13 rollover if they are ready.")
rep("reward tiers, the daily and weekly quest tables and the premium track.", "reward tiers, the premium track and the season theme.", 3)
rep('[["Beat","Push name","Send (UTC)","Segment","English copy","Status","Notes"]]', '[["Beat","Push name","Send (UTC or trigger)","Segment","English copy","Send or hold","What is missing"]]')
rep("-- GitHub review/inline/conversation notes + timeline events + PR bumps + INT-01 #zombie-prs mirrors", "-- GitHub review and inline notes + timeline events + INT-01 #zombie-prs mirrors")

# ---- D.
rep("Coming back on the Halloween one-off: pulling my ok.", "Coming back on the themed prop set I okayed in Martin''s thread: pulling my ok.")

open(dst, "w", encoding="utf-8").write(s)
print("written", dst, hashlib.sha256(s.encode()).hexdigest(), len(s.encode()), "bytes | ts", ts1, ts2)
