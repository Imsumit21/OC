"""Round 7 hardening: SQL transform (from the round-6 SQL f6afeda7b086).

1. Blake's 'not tiers' mark on PR #271 (ZOM-295), as an inline review comment under an APPROVED review with an
   empty body (his usual shape). Card rule 1 already says a title match Blake marked 'not tiers' in his review on
   its PR stays off, so ZOM-295 leaves the register (24 -> 23 tickets, Live 16 -> 15).
   Companion: the GitHub feed bot posts the comment in C093LEZGF6J under the PR-opened message (reply_count 4 -> 6, approval and comment mirrors).
2. Robert's thread reply asks for the done day in pacific time (ZOM-200 06-12, ZOM-274 06-20, ZOM-282 06-20).
3. Header comment counts.

Usage: harden_r7.py <round-6 sql> <out sql>
"""
import hashlib
import sys

src, out = sys.argv[1], sys.argv[2]
s = open(src).read()


def once(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, (n, count, old[:80])
    s = s.replace(old, new)


PR = 'harmonygames-Games/match3d#271'
REV_ID, RC_ID = PR + '#rev_2', PR + '#rc_1'
REV_AT = '2025-07-04T01:05:22Z'        # Blake was asked to review at 00:36:36Z; merged 13:29:30Z
HEAD = '2f1c9a2251dd59ea40b7a64f09231de80ff466ed'
BODY = ("not tiers: this is a bug fix, enrage was always meant to clear on refill health and push back. "
        "no tier version or enrage number changes here. leave it out when we list tier work")
HUNK = ("@@ -523,4 +524,9 @@ public class MonsterSpawner : SingletonMonoBehaviour<MonsterSpawner>\\n"
        "             AudioManager.Instance.PlayClip(audioClip);\\n"
        "         }\\n"
        "     }\\n"
        "+\\n"
        "+    public void ResetEnrageCounter()")
assert PR + '#rev_2' not in s and RC_ID not in s

GH = ("INSERT INTO github.github_reviews (id, pr_id, author_login, state, body, submitted_at, commit_id, seq)\n"
      f"VALUES ('{REV_ID}', '{PR}', 'EMPLOYEE_0025_GITHUB_USERNAME', 'APPROVED', '', '{REV_AT}', '{HEAD}', 2);\n"
      "INSERT INTO github.github_review_comments (id, pr_id, author_login, body, path, diff_hunk, line, position, "
      "commit_id, in_reply_to_id, created_at, seq, pull_request_review_id, side, subject_type)\n"
      f"VALUES ('{RC_ID}', '{PR}', 'EMPLOYEE_0025_GITHUB_USERNAME', '{BODY}', 'Assets/Scripts/Monster/MonsterSpawner.cs', "
      f"E'{HUNK}', 528, NULL, '{HEAD}', NULL, '{REV_AT}', 1, '{REV_ID}', 'RIGHT', 'line');\n")
anchor = "-- ===================== LINEAR ====================="
assert s.count(anchor) == 1
s = s.replace(anchor, GH + anchor)

# --- GitHub feed companion (same shape as the #265 one)
CH, PARENT_ID, PARENT_TS = 'C093LEZGF6J', '2e34453f3fc13f34986b9d16b76c4119', '1751588271.756019'
TS = '1751591125.638214'                # 01:05:25Z, three seconds after the comment
MID = hashlib.sha256(f'{CH}|{TS}'.encode()).hexdigest()[:32]
assert TS not in s and MID not in s
ATT = ('[{"color": "24292f", "fallback": "[harmonygames-Games/match3d] Comment on #271", '
       '"footer": "<https://github.com/harmonygames-Games/match3d|harmonygames-Games/match3d>", '
       '"footer_icon": "https://slack.github.com/static/img/favicon-neutral.png", "id": 1, "mrkdwn_in": ["text"], '
       '"pretext": "<https://github.com/harmonygames-Games/match3d/pull/271#discussion_r2184401907|Comment> on pull request by '
       '<https://github.com/arthur.blake|arthur.blake>", '
       f'"text": "{BODY}", '
       '"title": "<https://github.com/harmonygames-Games/match3d/pull/271|#271 ZOM-295: Refill health and Push monster back should reset ALL enrage status>", '
       '"ts": 1751591122}]')
TS_A = '1751591124.205377'              # approval mirror, just before the comment mirror
MID_A = hashlib.sha256(f'{CH}|{TS_A}'.encode()).hexdigest()[:32]
assert TS_A not in s and MID_A not in s
ATT_A = ('[{"color": "36a64f", "fallback": "[harmonygames-Games/match3d] Review approved by <https://github.com/arthur.blake|arthur.blake> '
         'on <https://github.com/owen.baker|owen.baker\'\'s> pull request", '
         '"footer": "<https://github.com/harmonygames-Games/match3d|harmonygames-Games/match3d>", '
         '"footer_icon": "https://slack.github.com/static/img/favicon-neutral.png", "id": 1, "mrkdwn_in": ["text"], '
         '"pretext": "Review approved by <https://github.com/arthur.blake|arthur.blake> on <https://github.com/owen.baker|owen.baker\'\'s> pull request", '
         '"title": "Review on #271 ZOM-295: Refill health and Push monster back should reset ALL enrage status", '
         '"title_link": "https://github.com/harmonygames-Games/match3d/pull/271#pullrequestreview-2984501722", "ts": 1751591122}]')
COLS_S = ("INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, "
          "reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, "
          "attachments_json, created_at, metadata_json)\n")
SL_A = (COLS_S + f"VALUES ('{MID_A}', '{TS_A}', '{CH}', 'message', 'SLACK_BOT_0004_SLACK_ID', '', '{PARENT_ID}', '{PARENT_TS}', 0, 0, NULL, "
        f"false, NULL, '[]', '[]', '{ATT_A}', '2025-07-04T01:05:24.205377Z', '{{}}');\n")
SL = SL_A + ("INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, "
      "reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, "
      "attachments_json, created_at, metadata_json)\n"
      f"VALUES ('{MID}', '{TS}', '{CH}', 'message', 'SLACK_BOT_0004_SLACK_ID', '', '{PARENT_ID}', '{PARENT_TS}', 0, 0, NULL, "
      f"false, NULL, '[]', '[]', '{ATT}', '2025-07-04T01:05:25.638214Z', '{{}}');\n"
      f"UPDATE slack.slack_messages SET reply_count = 6 WHERE id = '{PARENT_ID}';\n")
anchor2 = "UPDATE slack.slack_messages SET reply_count = 13 WHERE id = '6a42cb69b452e0c89f36407f56a3d84b';\n"
assert s.count(anchor2) == 1
s = s.replace(anchor2, anchor2 + SL)

# --- 2. Robert: pacific day
once("the day it got marked done (leave it blank if it never got done)",
     "the day it got marked done, pacific time (leave it blank if it never got done)")

# --- 3. header counts
ins = s.count('\nINSERT INTO ')
upd = s.count('\nUPDATE ')
once("Statements: 179 INSERT (one row each), 3 UPDATE.", f"Statements: {ins} INSERT (one row each), {upd} UPDATE.")
assert '\r' not in s and '—' not in BODY
open(out, 'w').write(s)
print('ok', ins, 'INSERT', upd, 'UPDATE', 'slack id', MID)
