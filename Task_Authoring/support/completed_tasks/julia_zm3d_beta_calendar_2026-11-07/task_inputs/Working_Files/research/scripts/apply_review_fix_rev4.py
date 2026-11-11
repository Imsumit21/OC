#!/usr/bin/env python3
"""Revision 4 repair: Cross-Service Coherence items an independent /prompt run found on revision 3.

Pure text transform of 01_Universe_Inject.sql (revision 3, sha 837d4f5d...) with asserted anchors.
The answer key does not change; only where three notes live, six ticket states, one Slack
placement, one mail's threading and the bot-mirror shape.

  A. Notes on long-merged PRs (closed records with later activity) move to live records:
       #370 rc_1  (vial sprites, Claire)      -> inline review note on #468, before its merge
       #438 rc_74 (premium strip, Oliver)     -> conversation note on #473, 35 min after its merge
       #454 c_4   (C&W icon animation, Marcus)-> second comment on the open ticket ZOM-465
  B. Linear tickets whose own notes report the work finished are closed at that point (Done,
     completed_at = updated_at); the two with work under way move to In Progress with a started_at.
  C. Robert's Halloween retraction becomes a top-level DM message (it sat under an unrelated parent).
  D. Brian's correction becomes a mail of its own (no Re:, no In-Reply-To) with a snippet cut from
     its body, and says where to answer it.
  E. Review timeline events follow the base shape ('reviewed', no actor, no time, commit in data);
     bot mirrors follow the base shape (subtype null, people's GitHub handles, ids in base order).

  F. Brief: Plague Race joins the beats planned without window dates (its cadence differs between
     the synthetic analytics table and the backend schedule), the one-off rule is reworded, and
     the lock rule says where the owner is told.
  G. Frederick's ask separates the calendar (sheet + ticket link) from the recommendation (DM) and
     says what the recommendation is about.
  H. The release event is 'opaque' like every base calendar event.

Usage: apply_review_fix_rev4.py <in.sql> <out.sql>
"""
import hashlib
import json
import re
import sys
from datetime import datetime, timezone

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest() == "837d4f5dedbdedb0febe279f64b5df61f0debdf29e93ef779a4ddd5ff754d76b", "unexpected input revision"

PR = "harmonygames-Games/match3d#"
PRS = "C093LEZGF6J"  # #zombie-prs
ARTHUR = "EMPLOYEE_0025_GITHUB_USERNAME"


def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, f"anchor count {n} != {count}: {old[:90]!r}"
    s = s.replace(old, new)


def line_with(marker):
    hits = [ln for ln in s.split("\n") if marker in ln]
    assert len(hits) == 1, f"{len(hits)} lines contain {marker!r}"
    return hits[0]


def drop(marker):
    ln = line_with(marker)
    rep(ln + "\n", "")


def q(text):
    return text.replace("'", "''")


def slack_ts(iso):
    e = int(datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())
    frac = f"{e % 1000000:06d}"
    return e, f"{e}.{frac}", iso[:-1] + f".{frac}Z"


def mirror(pr_no, pr_title, anchor, handle, body, iso, parent_id, parent_ts):
    e, ts, created = slack_ts(iso)
    mid = hashlib.sha256(f"{PRS}|{ts}".encode()).hexdigest()[:32]
    att = [{"color": "24292f", "fallback": f"[harmonygames-Games/match3d] Comment on #{pr_no}",
            "footer": "<https://github.com/harmonygames-Games/match3d|harmonygames-Games/match3d>",
            "footer_icon": "https://slack.github.com/static/img/favicon-neutral.png", "id": 1, "mrkdwn_in": ["text"],
            "pretext": f"<https://github.com/harmonygames-Games/match3d/pull/{pr_no}#{anchor}|Comment> on pull request by <https://github.com/{handle}|{handle}>",
            "text": body, "title": f"<https://github.com/harmonygames-Games/match3d/pull/{pr_no}|#{pr_no} {pr_title}>", "ts": e}]
    att_json = json.dumps(att, ensure_ascii=False, separators=(",", ":"))
    return ("INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, "
            "reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, metadata_json) "
            f"VALUES ('{mid}', '{ts}', '{PRS}', 'message', 'SLACK_BOT_0004_SLACK_ID', '', '{parent_id}', '{parent_ts}', 0, 0, NULL, false, NULL, "
            f"'[]', '[]', '{q(att_json)}', '{created}', '{{}}');"), ts


# ---------------------------------------------------------------- A1. vial sprites: #370 -> #468 (before merge)
VIAL = ("The final vial sprites are still missing for the Collect & Win set — Claire has those on her list. "
        "Everything else on the art side of this PR is settled from my side.")
VIAL_AT = "2025-09-29T15:36:41Z"           # #468 opened 2025-09-26T20:16:25Z, merged 2025-09-29T16:13:50Z
drop(f"VALUES ('{PR}370#rc_1'")
drop(f"VALUES ('{PR}370#ev_5'")
drop(f"WHERE id = '{PR}370';")
drop("VALUES ('408dca285b06b469679d08666344cc11'")
drop("WHERE id = 'd648cbe9f00776a76405345c855ea190';")
m468, _ = mirror(468, "Collect And Win", "discussion_r2388843617", "arthur.blake", VIAL, VIAL_AT,
                 "4b7c41278397b56b36e9b2f8a820c454", "1758917788.864169")
rep(line_with(f"VALUES ('{PR}370#rev_1'"),
    "INSERT INTO github.github_reviews (id, pr_id, author_login, state, body, submitted_at, commit_id, seq) "
    f"VALUES ('{PR}468#rev_3', '{PR}468', '{ARTHUR}', 'COMMENTED', '', '{VIAL_AT}', NULL, 3);\n"
    "INSERT INTO github.github_review_comments (id, pr_id, author_login, body, path, diff_hunk, line, position, commit_id, in_reply_to_id, "
    "created_at, pull_request_review_id, side, start_line, start_side, subject_type, seq) "
    f"VALUES ('{PR}468#rc_38', '{PR}468', '{ARTHUR}', '{q(VIAL)}', 'Assets/Sprites/CollectAndWin/icn - poison - red.png.meta', '', "
    f"NULL, NULL, NULL, NULL, '{VIAL_AT}', '{PR}468#rev_3', NULL, NULL, NULL, NULL, 38);\n"
    "INSERT INTO github.github_timeline_events (id, pr_id, event, actor_login, created_at, data_json) "
    f"VALUES ('{PR}468#ev_6', '{PR}468', 'reviewed', '', NULL, '{{\"commit_id\": \"648e2c7b9c1d9e263f4b43a45e135ba9fa6002fd\"}}');")
# the thread's newest reply stays the base merge post (2025-09-29T16:13:53Z); only the count moves 41 -> 42
MIRROR_468 = m468 + "\n\nUPDATE slack.slack_messages SET reply_count = 42, latest_reply = '1759162433.383449' WHERE id = '4b7c41278397b56b36e9b2f8a820c454';"

# ---------------------------------------------------------------- A2. premium strip: #438 -> #473 (35 min after merge)
STRIP = ("The Season Pass premium strip needs to move to the November range rather than the current one — "
         "Oliver is taking the date change.")
STRIP_AT = "2025-09-30T16:16:33Z"          # #473 merged 2025-09-30T15:41:20Z
drop(f"VALUES ('{PR}438#rc_74'")
drop(f"VALUES ('{PR}438#ev_9'")
drop(f"WHERE id = '{PR}438';")
drop("VALUES ('cc8ce0e4827971e4bee1fc5c5ea980d5'")
drop("WHERE id = '2f138acf24c126ea5e1fd20ec4fecc1e';")
m473, ts473 = mirror(473, "Addressables/sp", "issuecomment-3352918642", "arthur.blake", STRIP, STRIP_AT,
                     "d05a2f8a3c4ada2d6b91c809e04222dc", "1759246868.802449")
rep(line_with(f"VALUES ('{PR}438#rev_4'"),
    "INSERT INTO github.github_pr_comments (id, pr_id, author_login, body, created_at, updated_at) "
    f"VALUES ('{PR}473#c_2', '{PR}473', '{ARTHUR}', '{q(STRIP)}', '{STRIP_AT}', '{STRIP_AT}');\n\n"
    "INSERT INTO github.github_timeline_events (id, pr_id, event, actor_login, created_at, data_json) "
    f"VALUES ('{PR}473#ev_5', '{PR}473', 'commented', '{ARTHUR}', '{STRIP_AT}', '{{}}');\n\n"
    f"UPDATE github.github_pull_requests SET updated_at = '{STRIP_AT}' WHERE id = '{PR}473';")
MIRROR_473 = m473 + f"\n\nUPDATE slack.slack_messages SET reply_count = 3, latest_reply = '{ts473}' WHERE id = 'd05a2f8a3c4ada2d6b91c809e04222dc';"

# ---------------------------------------------------------------- A3. C&W icon animation: #454 -> ZOM-465 follow-up
ICON = ("Collect & Win came in after my note above, so its event icon is not animated yet. "
        "The Collect & Win event icon animation is still to do on my side, the other event icons are finished.")
ICON_AT = "2025-09-30T18:05:00Z"
drop(f"VALUES ('{PR}454#c_4'")
drop(f"VALUES ('{PR}454#ev_6'")
drop(f"WHERE id = '{PR}454';")
drop("VALUES ('8a9a746604dc5435b6d3cd79d3f19b8d'")
drop("WHERE id = 'ef41446756d5e1929f95817baacb1e7b';")
rep("UPDATE linear.linear_issues SET updated_at = '2025-09-26T18:10:00Z' WHERE id = 'ZOM-465';",
    "INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) "
    f"VALUES ('cmt_zom465_2', 'ZOM-465', 'usr_c77c50cc15c5342d', NULL, '{q(ICON)}', false, '{ICON_AT}', '{ICON_AT}', 2);\n"
    f"UPDATE linear.linear_issues SET updated_at = '{ICON_AT}' WHERE id = 'ZOM-465';")

# ---------------------------------------------------------------- E. remaining mirrors and the #470 review event: base shape
old470 = line_with("VALUES ('c778c9b9d8fff77f59c93ce8d7902953'")
new470 = old470.replace("false, 'bot_message', '[]'", "false, NULL, '[]'") \
               .replace(f"<https://github.com/{ARTHUR}|{ARTHUR}>", "<https://github.com/arthur.blake|arthur.blake>")
assert new470.count("arthur.blake") == 2 and "bot_message" not in new470
rep(old470, new470)
old471 = line_with("VALUES ('a0c2677988d2041ff14477598ee60261'")
new471 = old471.replace("false, 'bot_message', '[]'", "false, NULL, '[]'") \
               .replace("<https://github.com/EMPLOYEE_0004_GITHUB_USERNAME|EMPLOYEE_0004_GITHUB_USERNAME>", "<https://github.com/samuel.turner|samuel.turner>") \
               .replace("issuecomment-3349327810", "issuecomment-3353762954")
assert new471.count("samuel.turner") == 2 and "bot_message" not in new471 and "3353762954" in new471
rep(old471, new471)
# the two new mirrors go where the dropped ones stood: after the #470 mirror's parent UPDATE
rep("UPDATE slack.slack_messages SET reply_count = 17, latest_reply = '1759248252.248252' WHERE id = 'c2b9c90355cf8c2c4326ab19d3a24f79';",
    "UPDATE slack.slack_messages SET reply_count = 17, latest_reply = '1759248252.248252' WHERE id = 'c2b9c90355cf8c2c4326ab19d3a24f79';\n\n"
    + MIRROR_468 + "\n\n" + MIRROR_473)
rep(f"VALUES ('{PR}470#ev_9', '{PR}470', 'commented', '{ARTHUR}', '2025-09-30T16:04:12Z', '{{}}');",
    f"VALUES ('{PR}470#ev_9', '{PR}470', 'reviewed', '', NULL, '{{\"commit_id\": \"4935e9483a95d78b3a58d18794bacd97816787e8\"}}');")

# ---------------------------------------------------------------- B. ticket states follow the tickets' own notes
def done(issue, old_updated, t):
    # base ZOM pattern: every Done ticket has completed_at, and updated_at = completed_at on 401 of 427
    assert t >= old_updated
    rep(f"UPDATE linear.linear_issues SET updated_at = '{old_updated}' WHERE id = '{issue}';",
        f"UPDATE linear.linear_issues SET state_id = 'Done', completed_at = '{t}', updated_at = '{t}' WHERE id = '{issue}';")


def in_progress(issue, old_updated, started):
    assert started <= old_updated
    rep(f"UPDATE linear.linear_issues SET updated_at = '{old_updated}' WHERE id = '{issue}';",
        f"UPDATE linear.linear_issues SET state_id = 'In Progress', started_at = '{started}', updated_at = '{old_updated}' WHERE id = '{issue}';")


done("ZOM-565", "2025-09-29T16:05:00Z", "2025-09-29T17:10:00Z")   # "is in ... can close" (commit f7e971b0, Sep 25); closed an hour after the note
done("ZOM-471", "2025-09-17T16:45:00Z", "2025-09-17T16:45:00Z")   # "ready and wired", by its assignee
done("ZOM-344", "2025-09-16T16:20:00Z", "2025-09-16T16:20:00Z")   # "art side is signed off on my end", by its assignee
done("ZOM-542", "2025-09-22T18:40:00Z", "2025-09-22T18:40:00Z")   # "layouts are in ... regression pass looks clean", by its assignee
done("ZOM-432", "2025-09-24T16:10:00Z", "2025-09-30T21:20:00Z")   # closed after the #471 note (21:07:26Z) says the frame went out; the Sep 24 note stays as the older word
in_progress("ZOM-566", "2025-09-30T19:40:00Z", "2025-09-30T17:20:00Z")   # "first events are landing in the pipeline"
ln387 = line_with("VALUES ('cmt_zom387_1'")
rep(ln387, ln387 + "\nUPDATE linear.linear_issues SET state_id = 'In Progress', started_at = '2025-07-25T13:20:00Z', "
                   "time_in_status_minutes = NULL WHERE id = 'ZOM-387';")

# ---------------------------------------------------------------- C. Robert's retraction: top-level DM message
old_r = line_with("VALUES ('58d06bd55ea4129eaadb726291967d5a'")
new_r = old_r.replace(", 'c54310280ca0915181508d6e9b964926', '1759248350.473459', 0, 0, NULL, false,", ", NULL, NULL, 0, 0, NULL, false,")
assert new_r != old_r
rep(old_r, new_r)
drop("WHERE id = 'c54310280ca0915181508d6e9b964926';")

# ---------------------------------------------------------------- D. Brian's correction: its own mail, snippet from the body, where to answer
OLD_SUBJ = "Re: ZM3D Season Pass November config handoff"
NEW_SUBJ = "ZM3D Season Pass November config handoff: new date"
rep("The November season still opens on Sat Nov 1.\n\nBrian'",
    "The November season still opens on Sat Nov 1. If the new date is a problem on your side, reply on this mail.\n\nBrian'", 3)
m = re.search(r"'(Julia,\n\nCorrection to my Sep 22 mail.*?\n\nBrian)'", s, re.S)
body = m.group(1)
base_snip = "Julia, Handing over the November Season Pass config, Frederick in copy so we all have it in one place. The November season opens on Sat Nov 1. The config handoff we agreed wit"
snippet = " ".join(body.split())[:len(base_snip)]          # same cut as the Sep 22 mail (first 175 characters of the collapsed body)
assert "'" not in snippet and len(snippet) == 175
rep("'Julia, Correction to my Sep 22 mail: the November Season Pass config handoff moves from Wed Oct 29 to Fri Oct 31, 10:00 Istanbul time. "
    "Same contents, same owner, I just need the'", f"'{snippet}'", 6)
rep(f"'2025-09-26T07:40:00+00:00', 4085, '{OLD_SUBJ}'", f"'2025-09-26T07:40:00+00:00', 3966, '{NEW_SUBJ}'", 3)
rep('{"name":"In-Reply-To","value":"<CAH4q9Zb2fK7xQe1M8sPnL3vT6wR0yDc@mail.gmail.com>"},'
    '{"name":"References","value":"<CAH4q9Zb2fK7xQe1M8sPnL3vT6wR0yDc@mail.gmail.com>"},', "", 3)
rep(f'{{"name":"Subject","value":"{OLD_SUBJ}"}}', f'{{"name":"Subject","value":"{NEW_SUBJ}"}}', 3)
rep(", NULL, '<CAH4q9Zb2fK7xQe1M8sPnL3vT6wR0yDc@mail.gmail.com>', '<CAH4q9Zb2fK7xQe1M8sPnL3vT6wR0yDc@mail.gmail.com>', '1844835127305531392@xxx",
    ", NULL, NULL, NULL, '1844835127305531392@xxx", 3)
assert OLD_SUBJ not in s

# ---------------------------------------------------------------- F. brief
HEADINGS = ["Span and time base", "Scope", "When a beat starts", "Held or not", "One-offs", "Still to do", "Push copy", "Config locks"]
md = re.search(r"(VALUES \('f_7c3e91a4d2b85f60e1a9c4', 'ZM3D beta live-ops calendar - working rules', 'frederick\.stone@harmonygames\.co', "
               r"'\[\"julia\.lawson@harmonygames\.co\"\]', 'private', ')((?:[^']|'')*)(', ')(\[[^']*\])(')", s, re.S)
assert md, "brief row not found"
doc = md.group(2)
assert "''" not in doc


def brep(old, new):
    global doc
    assert doc.count(old) == 1, old
    doc = doc.replace(old, new)


brep("For the quest rollover and the daily gift (the Login Calendar row on the push sheet) put down",
     "For the quest rollover, the daily gift (the Login Calendar row on the push sheet) and Plague Race put down")
brep("One-offs may overlap a recurring beat slots. A one-off may take a recurring beat slot only with Product latest dated approval,",
     "One-offs may overlap recurring beat slots. A one-off may take a recurring beat slot only with the latest dated approval from Product,")
brep("A committed date that misses the lock moves earlier and its owner is told.",
     "A committed date that misses the lock moves earlier and its owner is told in a reply on the mail where they committed to it.")
assert "'" not in doc
runs, pos = [], 0
for n, ln in enumerate(doc.split("\n")):
    if n == 0:
        runs.append({"start": 0, "end": len(ln), "named_style": "TITLE", "list_id": None, "list_nesting": 0})
    elif ln in HEADINGS:
        runs.append({"start": pos, "end": pos + len(ln), "named_style": "HEADING_2", "list_id": None, "list_nesting": 0})
    pos += len(ln) + 1
assert len(runs) == 9 and [doc[r["start"]:r["end"]] for r in runs[1:]] == HEADINGS
s = s[:md.start(2)] + doc + md.group(3) + json.dumps(runs, separators=(",", ":")) + s[md.end(4):]
print("brief:", len(doc), "chars; runs", [(r["start"], r["end"]) for r in runs])

# ---------------------------------------------------------------- G. Frederick's ask
rep("what still has to land before it runs and who owns that, and your recommendation with the trade-offs. Put it in the calendar sheet in your "
    "ZM Live Ops folder, link it on the calendar ticket, and send me the recommendation back here. The working rules for it are in my brief, shared with you.",
    "what still has to land before it runs and who owns that. Put it in the calendar sheet in your ZM Live Ops folder and link it on the calendar ticket. "
    "Then send me your recommendation back here, with the trade-offs, on what we run and what we hold in those weeks. "
    "The working rules for the calendar are in my brief, shared with you.")

# ---------------------------------------------------------------- H. release event like the base events
rep("'transparent'", "'opaque'", 4)

# ---------------------------------------------------------------- tidy and write
while "\n\n\n" in s:
    s = s.replace("\n\n\n", "\n\n")
for gone in ("#370#", "#438#", "#454#", "bot_message", "EMPLOYEE_0025_GITHUB_USERNAME|", "In-Reply-To"):
    assert gone not in s, gone
open(dst, "w", encoding="utf-8").write(s)
print("written", dst, hashlib.sha256(s.encode()).hexdigest(), len(s.encode()), "bytes")
print("snippet:", snippet)
