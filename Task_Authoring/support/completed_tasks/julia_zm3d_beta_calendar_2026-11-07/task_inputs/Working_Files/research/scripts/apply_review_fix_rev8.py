#!/usr/bin/env python3
"""Revision 8: the findings of the fresh blind /prompt round on revision 7 (sha 091722f6...).

P1 raised two fail-level forks, P2 four low-impact items (two low-impact items fail the dimension) and
Eval 0 two optional wording fixes. No graded value changes; one evidence id does (note 7). Pure text
transform, asserted anchors.

  1. Brief, "Held or not": says how to state a hold when no fix has a date (P1 DR1, P2 DR3). Later
     heading offsets shift by the length of the new sentence.
  2. ZOM-534: says the sync is on main and nothing else has to land for the beta, so the watched
     edge case is not a still-to-do (P1 DR2). Base: 47c65623e7 (Sep 10), on main since Sep 15.
  3. ZOM-521 note: also names ZOM-541, the integration ticket for the same work (Eval 0 F1).
  4. Trello quest note: "The rollover does not wait on them", because PNs Beta row 1 ("Revisit once
     new quests roll out") does wait on them (Eval 0 F2).
  5. ZOM-542: drops "not in the build yet / mockup stage", which sat against the base state Regression
     (P2 DR2). The ticket stays unstarted; the note says it comes after the bug list.
  6. Calendar sheet: web_view_link set in the base form (P2 DR4). 11 of Julia's 12 owned sheets have one.
  7. Premium-strip note moves off merged #473 (35 min after merge, P2 DR1: a closed record with later
     activity always fails) to an inline note under Arthur's base approval of #472, 6 s before merge,
     on the file that plays the Season Pass token. Same shape as #470#rc_10. All #473 rows go.

Usage: apply_review_fix_rev8.py <in.sql> <out.sql>
"""
import hashlib
import json
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest() == "091722f6a28117d59d40742adf1c0bbf379dd756c540a9dc79187b87275cb876", "unexpected input revision"


def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, f"anchor count {n} != {count}: {old[:100]!r}"
    s = s.replace(old, new)


def drop(start):
    """Remove the one statement that starts with `start`, up to its closing ';' at end of line."""
    global s
    assert s.count(start) == 1, f"statement anchor {s.count(start)}: {start[:90]!r}"
    i = s.index(start)
    j = s.index(";\n", i) + 2
    while s[j:j + 1] == "\n":
        j += 1
    s = s[:i] + s[j:]


# 1. brief: undated holds; shift the headings after "Held or not"
NEW = " A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date."
rep("An unresolved change-request review blocker on an in-scope live-ops PR from that cohort does hold it.\nOne-offs\n",
    "An unresolved change-request review blocker on an in-scope live-ops PR from that cohort does hold it." + NEW + "\nOne-offs\n")
for a, b in ((1728, 1736), (1936, 1947), (2165, 2174), (2491, 2503)):
    rep(f'{{"start":{a},"end":{b},"named_style":"HEADING_2"', f'{{"start":{a + len(NEW)},"end":{b + len(NEW)},"named_style":"HEADING_2"')

# 2. ZOM-534
rep("instead of waiting on a restart. Watching one backend timing edge case on the day boundary.",
    "instead of waiting on a restart. That is on main, so nothing else has to land for the beta. "
    "I am keeping this open to watch one backend timing edge case on the day boundary.")

# 3. ZOM-521 note
rep("I am leaving this item and ZOM-528 open until Brian has seen it in a build.",
    "I am leaving this item, ZOM-528 and ZOM-541 open until Brian has seen it in a build.")

# 4. Trello quest note
rep("Nothing in the beta waits on them, the current quests keep running either way.",
    "The rollover does not wait on them, the current quests keep running either way.")

# 5. ZOM-542
rep("Not in the build yet: the home screen and victory score changes for endless and boss arena are still at the mockup stage. "
    "I am on the bug list first, and this is a layout refresh on screens that already work, so it is not needed for the beta.",
    "Picking this up after the bug list. The home screen and victory score changes for endless and boss arena are a layout "
    "refresh on screens that already work, so they are not needed for the beta.")

# 6. calendar sheet link (Google-shaped id, 44 chars, as the base's sheet links)
import base64
gid = "1" + base64.urlsafe_b64encode(hashlib.sha256(b"ZM3D Beta Live-Ops Calendar").digest()).decode().rstrip("=")[:43]
rep("'2025-09-30 06:38:27+00', '2025-09-30 06:35:14+00', NULL, false, false, NULL, NULL, NULL, NULL, NULL, NULL);",
    f"'2025-09-30 06:38:27+00', '2025-09-30 06:35:14+00', NULL, false, false, NULL, 'https://drive.google.com/file/d/{gid}/view', NULL, NULL, NULL, NULL);")

# 7. premium-strip note: #473 rows out, inline note on #472 in
drop("INSERT INTO github.github_pr_comments (id, pr_id, author_login, body, created_at, updated_at) VALUES ('harmonygames-Games/match3d#473#c_2'")
drop("INSERT INTO github.github_timeline_events (id, pr_id, event, actor_login, created_at, data_json) VALUES ('harmonygames-Games/match3d#473#ev_5'")
drop("UPDATE github.github_pull_requests SET updated_at = '2025-09-30T16:16:33Z' WHERE id = 'harmonygames-Games/match3d#473';")
drop("INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, metadata_json) VALUES ('bd1a7d0ac25ccb2ee31db82d61f38607'")
drop("UPDATE slack.slack_messages SET reply_count = 3, latest_reply = '1759248995.720659', attachments_json =")

BODY = ("Fine for this PR. Separately, the Season Pass premium strip is still set to the October range. "
        "It needs the November range before that season opens, Oliver is taking the date change.")
TS = "1759247580.842719"                      # 15:53:00.84Z: 2.8 s after the note, after the base approval mirror
MID = hashlib.sha256(f"C093LEZGF6J|{TS}".encode()).hexdigest()[:32]
DISC = sys.argv[3]                            # discussion id in base order
att = [{"color": "24292f", "fallback": "[harmonygames-Games/match3d] Comment on #472",
        "footer": "<https://github.com/harmonygames-Games/match3d|harmonygames-Games/match3d>",
        "footer_icon": "https://slack.github.com/static/img/favicon-neutral.png", "id": 1, "mrkdwn_in": ["text"],
        "pretext": f"<https://github.com/harmonygames-Games/match3d/pull/472#discussion_r{DISC}|Comment> on pull request by <https://github.com/arthur.blake|arthur.blake>",
        "text": BODY, "title": "<https://github.com/harmonygames-Games/match3d/pull/472|#472 Implement Win&amp;Collect into Queue Manager>",
        "ts": 1759247578}]
ATT = json.dumps(att, separators=(",", ":"))
rc = ("INSERT INTO github.github_review_comments (id, pr_id, author_login, body, path, diff_hunk, line, position, commit_id, in_reply_to_id, created_at, "
      "pull_request_review_id, side, start_line, start_side, subject_type, seq) VALUES ('harmonygames-Games/match3d#472#rc_1', 'harmonygames-Games/match3d#472', "
      f"'EMPLOYEE_0025_GITHUB_USERNAME', '{BODY}', 'Assets/RewardVFXManager.cs', '', NULL, NULL, NULL, NULL, '2025-09-30T15:52:58Z', "
      "'harmonygames-Games/match3d#472#rev_1', NULL, NULL, NULL, NULL, 1);\n\n")
mirror = ("INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, reply_users_count, latest_reply, "
          f"is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, metadata_json) VALUES ('{MID}', '{TS}', 'C093LEZGF6J', 'message', "
          "'SLACK_BOT_0004_SLACK_ID', '', '61f686b8a8b6c164b14aff6b5b1897bf', '1759185399.395419', 0, 0, NULL, false, NULL, '[]', '[]', "
          f"'{ATT}', '2025-09-30T15:53:00.842719Z', '{{}}');\n\n"
          "UPDATE slack.slack_messages SET reply_count = 4, latest_reply = '1759247586.958099' WHERE id = '61f686b8a8b6c164b14aff6b5b1897bf';\n\n")
A = "UPDATE slack.slack_messages SET reply_count = 17, latest_reply = '1759247478.371389' WHERE id = 'c2b9c90355cf8c2c4326ab19d3a24f79';\n"
assert s.count(A) == 1
i = s.index(A) + len(A)
while s[i:i + 1] == "\n":
    i += 1
s = s[:i] + rc + mirror + s[i:]
assert "#473" not in s and "/pull/473" not in s, "a #473 reference is left"

open(dst, "w", encoding="utf-8").write(s)
print("written", dst, hashlib.sha256(s.encode()).hexdigest(), len(s.encode()), "bytes", "| mirror id", MID, "| len NEW", len(NEW), "| gid", gid, len(gid))
