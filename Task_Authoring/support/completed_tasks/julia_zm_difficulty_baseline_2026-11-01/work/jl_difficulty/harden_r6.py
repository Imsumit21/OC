"""Round 6 hardening: SQL transform (from the round-5 SQL 7966b1496ad9).

1. A third hidden thread reply, in a different conversation: the Robert / Leonard / Julia group DM CAFC495E4006.
   Leonard asks Robert there (top level) what he wants on Julia's register; Robert answers in a thread reply:
   three extra Tickets-tab columns (Linear assignee, the day it was marked done, Linear priority).
2. Card rule 2 points to that group chat (card desc + the 14:04Z updateCard action).
3. Header comment counts brought up to date (/injection advisory C-1).

Usage: harden_r6.py <round-5 sql> <out sql>
"""
import sys

src, out = sys.argv[1], sys.argv[2]
s = open(src).read()


def once(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, (n, count, old[:80])
    s = s.replace(old, new)


COLS = ("INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, "
        "reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, "
        "attachments_json, created_at, metadata_json)\n")
CH = 'CAFC495E4006'
P_ID, P_TS = 'cec246a6e43158f200fe144f0dd7039c', '1759226461.318204'   # 2025-09-30T10:01:01Z, Leonard
R_ID, R_TS = 'abe096ff0b5d7216efbc889e91d6d13a', '1759229513.774912'   # 2025-09-30T10:51:53Z, Robert
P_TXT = ("robert anything you want on julia''s difficulty list for monday? she''s putting it together from the card")
R_TXT = ("yeah three things after status please. who it''s assigned to in linear, the day it got marked done "
         "(leave it blank if it never got done), and its linear priority. i want to sort by them in the session")
for x in (P_TXT, R_TXT):
    for w in ('register', 'column', 'baseline'):
        assert w not in x.lower(), w
ROWS = (COLS +
        f"VALUES ('{P_ID}', '{P_TS}', '{CH}', 'message', 'EMPLOYEE_0038_SLACK_ID', '{P_TXT}', NULL, NULL, 1, 1, '{R_TS}', "
        "false, NULL, '[]', '[]', '[]', '2025-09-30T10:01:01.318204Z', '{}');\n" +
        COLS +
        f"VALUES ('{R_ID}', '{R_TS}', '{CH}', 'message', 'EMPLOYEE_0016_SLACK_ID', '{R_TXT}', '{P_ID}', '{P_TS}', 0, 0, NULL, "
        "false, NULL, '[]', '[]', '[]', '2025-09-30T10:51:53.774912Z', '{}');\n")
assert P_TS not in s and R_TS not in s and P_ID not in s and R_ID not in s
anchor = COLS + "VALUES ('6f77386571537f0bd88c959bdc216f94'"
assert s.count(anchor) == 1
s = s.replace(anchor, ROWS + anchor)

# --- 2. card rule 2 (desc + updateCard action)
once("Layout as in the session agenda.",
     "Layout as in the session agenda, plus the three things Robert asked for when I asked him in our group chat.", 2)

# --- 3. header counts
ins = s.count('\nINSERT INTO ')
upd = s.count('\nUPDATE ')
once("Statements: 172 INSERT (one row each), 3 UPDATE.", f"Statements: {ins} INSERT (one row each), {upd} UPDATE.")
open(out, 'w').write(s)
print('ok', ins, 'INSERT', upd, 'UPDATE')
