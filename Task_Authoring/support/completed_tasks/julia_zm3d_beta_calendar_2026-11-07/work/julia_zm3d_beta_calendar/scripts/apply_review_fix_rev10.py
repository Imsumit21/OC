#!/usr/bin/env python3
"""Revision 10: the pre-review attack on revision 9 (sha 892f7edd...). Six agents read the post-brief window in full and tested 200+ candidates.
No graded value changes. Pure text transform, asserted anchors.

  1. Still to do rule: the flag clause had a second parse ("not done since this brief") with no kill, "that beat" could bind to "a held
     beat", and "as not done" let polish in. "anything flagged since this brief as still needed for it" closes all three.
  2. "A window the release instant pre-empts does not count." removed: "pre-empts" reads backwards and, without its old "so", the sentence
     is a riddle. "the first window that opens after" gives Fri Oct 10 by itself.
  3. Push copy: "the English copy on that row", so the sheet row, not the client string, is what is judged.
  4. Endless core-game VFX and the refill timer: the one record that met every limb of the rule. Three audits flagged it independently.
     Brian, who set the P1/P2 list, closes it on ZOM-565. It does not say the work stopped (ZOM-567 opens for it on Oct 1).
  5. Martin's Endless themes (Sep 29, Sep 30): Robert's reply in the desert thread. It does not say they are out of the beta.
  6. Shader thread: closed by Vincent, who raised it, not by the fixer's own word (Oliver's reply goes).
  7. Trello note: "weekly rollover", so "which weeks it runs" has a record for the quest rollover.

Usage: apply_review_fix_rev10.py <in.sql> <out.sql>
"""
import calendar
import hashlib
import json
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest() == sys.argv[3], "unexpected input revision"


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


def slack_reply(channel, iso, micro, user, text, parent_id, parent_ts):
    assert micro % 10 == 9
    ts = f"{epoch(iso)}.{micro:06d}"
    mid = hashlib.sha256(f"{channel}|{ts}".encode()).hexdigest()[:32]
    return ts, (f"{SLACK_COLS}VALUES ('{mid}', '{ts}', '{channel}', 'message', '{user}', '{text}', '{parent_id}', '{parent_ts}', 0, 0, NULL, false, NULL, "
                f"'[]', '[]', '[]', '{iso[:-1]}.{micro:06d}Z', '{{}}');\n")


# 1, 2, 3: brief
rep("a held beat''s fix, and what has been flagged for that beat as not done since this brief (prod deploy, config or player-facing art).",
    "its fix if it is held, and anything flagged since this brief as still needed for it (prod deploy, config or player-facing art).")
rep(" A window the release instant pre-empts does not count.", "")
rep("and its English copy names the game as Zombie Match 3D", "and the English copy on that row names the game as Zombie Match 3D")

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

# 4: ZOM-565
T565 = "2025-09-30T16:12:27Z"
old = "UPDATE linear.linear_issues SET updated_at = '2025-09-29T14:34:12Z' WHERE id = 'ZOM-565';"
rep(old, f"{LINEAR_COLS}VALUES ('cmt_zom565_2', 'ZOM-565', 'usr_fc22d5941b2aeb5c', NULL, 'Marcus, the endless VFX inside the core game and the refill timer are the same "
    f"P1/P2 polish from my list. Endless runs fine without them, so they can follow and do not have to land before the beta.', false, '{T565}', '{T565}', 2);\n"
    f"UPDATE linear.linear_issues SET updated_at = '{T565}' WHERE id = 'ZOM-565';")

# 5: themes, and 6: shader
ART, DESERT_ID, DESERT_TS = "C08R8CHB0QL", "a3e78e820b9f880ef4e3d941562110df", "1759159849.386619"
ts_t, row_t = slack_reply(ART, "2025-09-30T16:41:08Z", 275139, "EMPLOYEE_0016_SLACK_ID",
                          "Both look good, the desert and the port. Keep them as options, Endless runs with what it has now and nothing waits on new themes.", DESERT_ID, DESERT_TS)
BUGS, SHADE_ID, SHADE_TS = "C08R27X0EAH", "d0dd5d3ad4658add1f79802e2aa60e48", "1759249488.495439"
ts_s, row_s = slack_reply(BUGS, "2025-09-30T21:46:15Z", 482369, "EMPLOYEE_0012_SLACK_ID",
                          "Oliver pushed the lightSweep fix. It only changes how the box looks, the box opens the same with or without it, so it rides the next build and nothing has to land for the beta.",
                          SHADE_ID, SHADE_TS)
a = s.index("INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, metadata_json) VALUES ('" +
            hashlib.sha256(b"C08R27X0EAH|1759267492.604719").hexdigest()[:32])
b0 = f"UPDATE slack.slack_messages SET reply_count = 5, latest_reply = '1759267492.604719' WHERE id = '{SHADE_ID}';\n"
b = s.index(b0) + len(b0)
s = (s[:a] + row_s + "\n" + f"UPDATE slack.slack_messages SET reply_count = 5, latest_reply = '{ts_s}' WHERE id = '{SHADE_ID}';\n\n"
     + row_t + "\n" + f"UPDATE slack.slack_messages SET reply_count = 4, reply_users_count = 4, latest_reply = '{ts_t}' WHERE id = '{DESERT_ID}';\n" + s[b:])

# 7: Trello
rep("The rollover does not wait on them, the current quests keep running either way.", "The weekly rollover does not wait on them, the current quests keep running either way.")


# 8: coherence attack on revision 9
#    S23: Leonard cancelled BrowserStack on Aug 7, so "remote device list" had no base support; the runbook Julia can read says "a cloud device farm".
#    The reply also moves out of his VC call. Row, parent update and ts change together.
OLD_TS, NEW_TS = "1759182097.318279", "1759187861.318279"
old_id = hashlib.sha256(f"C08R27X0EAH|{OLD_TS}".encode()).hexdigest()[:32]
new_id = hashlib.sha256(f"C08R27X0EAH|{NEW_TS}".encode()).hexdigest()[:32]
rep(old_id, new_id)
rep(OLD_TS, NEW_TS, 2)
rep("2025-09-29T21:41:37.318279Z", "2025-09-29T23:17:41.318279Z")
rep("Ran this again on an S23 Ultra from the remote device list, live Android build,", "Ran this again on an S23 Ultra in the cloud device farm, live Android build,")
#    ZOM-566: Brian said "Analytics and name changes first" 63 minutes earlier, so the note must not rank the text after analytics.
rep("Owen, analytics first. The header title and the info screen text can follow with it. The event runs fine with the current text, so they do not have to land before the beta.",
    "Owen, analytics and the name changes are first on the list, but none of it is a blocker. The event runs fine with the current text, so the header title and the info screen text do not have to land before the beta.")
#    ZOM-534: clear of his live DM. ZOM-563: name the update, so it cannot be read as the backend release.
rep("2025-09-30T01:22:46Z", "2025-09-30T01:09:52Z", 3)
rep("Checked on prod after the update: teams''", "Checked on prod after Douglas''s teams update: teams''")

rep("-- Linear per-issue comments (21 cohort issues) + Trello quests-card comment", "-- Linear per-issue comments + Trello quests-card comment")

open(dst, "w", encoding="utf-8").write(s)
print("written", dst, hashlib.sha256(s.encode()).hexdigest(), len(s.encode()), "bytes | ts", ts_t, ts_s)
