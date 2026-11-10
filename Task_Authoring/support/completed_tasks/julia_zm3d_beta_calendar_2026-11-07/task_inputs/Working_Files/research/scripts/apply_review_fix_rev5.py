#!/usr/bin/env python3
"""Revision 5 repair: every injected claim and record shape made true to the base universe.

Input is revision 4 (sha c955d6ca...). An independent /prompt round, a claim-by-claim audit of all
injected records against the whole base (code and git history on main, DMs the persona cannot see,
notification mails, Trello and Gmail conventions) and a re-audit of the rewritten records found
statements, dates and field shapes the base contradicts. This transform fixes exactly those.
Pure text transform with asserted anchors; it reads two base #zombie-prs cards to rebuild them.

  A. GitHub notes
       #470 rc_10   now part of Arthur's base approval review (15:51:06Z, before the merge)
       #468 rc_38   final vial MODELS (Claire's 3D work), anchored on the file that spawns them
       #473 c_2     says which range the strip is on now; updated_at NULL like every base PR comment
       #471 c_18    removed: the frame note moves to the ticket it closes (ZOM-432)
       mirrors      post 2-3 s after the event, escape '&', ts ends in 9 like every base Slack ts;
                    the #468 and #473 "opened" cards show the new reviewer / comment count
  B. Slack: ts values end in 9 and are not on the whole minute; ids follow from them
  C. Linear comments re-worded, re-timed or removed to match base code, commits and messages;
     ZOM-565, ZOM-471 and ZOM-542 stay open; ZOM-387 is left exactly as base has it;
     timestamps carry seconds
  D. Gmail: per-mailbox thread ids that encode the send time, Brian's Message-ID shape, his +0300
     Date header, Julia's read state with the label her mailbox uses, no Reply-To, sent copies
     without Delivered-To
  E. Drive / Docs / Slides / Sheets / GCal: working-hours timestamps with seconds; size and
     content_path on the Doc and Sheet rows; folder modified with its newest child
  F. Trello: the quest note moves from a card completed on Jun 30 to the open quests card #61,
     written by that card's owner, and no longer reads as something the beat waits for
  G. Deck: the retention-campaign line no longer says they were running on Sep 23

Usage: apply_review_fix_rev5.py <in.sql> <out.sql> <workspace root>
"""
import glob
import hashlib
import json
import re
import sys
from datetime import datetime, timezone

src, dst, root = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest() == "c955d6ca2bca5d1aa0c457e3107a28e8210903a833b3192a54d1e5337adc1cf2", "unexpected input revision"

PR = "harmonygames-Games/match3d#"
PRS = "C093LEZGF6J"
ARTHUR = "EMPLOYEE_0025_GITHUB_USERNAME"


def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, f"anchor count {n} != {count}: {old[:100]!r}"
    s = s.replace(old, new)


def line_with(marker):
    hits = [ln for ln in s.split("\n") if marker in ln]
    assert len(hits) == 1, f"{len(hits)} lines contain {marker!r}"
    return hits[0]


def drop(marker):
    rep(line_with(marker) + "\n", "")


def q(text):
    return text.replace("'", "''")


def epoch(iso):
    return int(datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())


def slack_id(channel, ts):
    return hashlib.sha256(f"{channel}|{ts}".encode()).hexdigest()[:32]


def slack_created(ts):
    e, frac = ts.split(".")
    return datetime.fromtimestamp(int(e), timezone.utc).strftime("%Y-%m-%dT%H:%M:%S") + f".{frac}Z"


assert slack_id("D05SD5QLG94", "1759263600.418207") == "8b090dec472117f4598b9ad84318272e"


def mirror(pr_no, pr_title, anchor, handle, body, iso, parent_id, parent_ts):
    """GitHub-app copy in #zombie-prs: 2-3 s after the event, '&' escaped, attachment ts = event time, ts ending in 9."""
    e = epoch(iso)
    h = int(hashlib.sha256(f"{pr_no}|{anchor}".encode()).hexdigest(), 16)
    e_msg, micro = e + 2 + h % 2, ((h >> 8) % 100000) * 10 + 9
    ts = f"{e_msg}.{micro:06d}"
    att = [{"color": "24292f", "fallback": f"[harmonygames-Games/match3d] Comment on #{pr_no}",
            "footer": "<https://github.com/harmonygames-Games/match3d|harmonygames-Games/match3d>",
            "footer_icon": "https://slack.github.com/static/img/favicon-neutral.png", "id": 1, "mrkdwn_in": ["text"],
            "pretext": f"<https://github.com/harmonygames-Games/match3d/pull/{pr_no}#{anchor}|Comment> on pull request by <https://github.com/{handle}|{handle}>",
            "text": body.replace("&", "&amp;"), "title": f"<https://github.com/harmonygames-Games/match3d/pull/{pr_no}|#{pr_no} {pr_title}>", "ts": e}]
    att_json = json.dumps(att, ensure_ascii=False, separators=(",", ":"))
    return ("INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, "
            "reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, metadata_json) "
            f"VALUES ('{slack_id(PRS, ts)}', '{ts}', '{PRS}', 'message', 'SLACK_BOT_0004_SLACK_ID', '', '{parent_id}', '{parent_ts}', 0, 0, NULL, false, NULL, "
            f"'[]', '[]', '{q(att_json)}', '{slack_created(ts)}', '{{}}');"), ts


# the two base "opened" cards whose derived fields the new notes change
base_prs = json.load(open(glob.glob(f"{root}/Universe_SynthCut/*Other_Services/Services_Data/slack/messages/{PRS}/2025-09.json")[0], encoding="utf-8"))
card = {m["id"]: m["attachments"] for m in base_prs if m.get("id") in ("4b7c41278397b56b36e9b2f8a820c454", "d05a2f8a3c4ada2d6b91c809e04222dc")}


def card_json(parent_id, field, old, new):
    att = json.loads(json.dumps(card[parent_id]))
    hit = [f for f in att[0]["fields"] if f["title"] == field]
    assert len(hit) == 1 and hit[0]["value"] == old, (parent_id, field, hit)
    hit[0]["value"] = new
    return q(json.dumps(att, ensure_ascii=False, separators=(",", ":")))


# ================================================================ A. GitHub notes
# ---- #470: an inline note inside Arthur's base approval (rev_9, 2025-09-30T15:51:06Z; the PR merged at 15:51:15Z)
NOTE470 = ("Server-side windows for Collect & Win are still on the DEV stack only, they reach prod with the next backend release. "
           "The Plague Race, leagues, Endless and Season Pass schedules are already running on prod. The client side in this PR is fine as it is.")
AT470 = "2025-09-30T15:51:06Z"
drop(f"VALUES ('{PR}470#rev_10'")
drop(f"VALUES ('{PR}470#ev_9'")
drop(f"WHERE id = '{PR}470';")
rep(f"'{NOTE470}', 'Assets/Scripts/UI/CollectAndWin/CollectAndWinMainScreenController.cs', '', NULL, NULL, NULL, NULL, '2025-09-30T16:04:12Z', '{PR}470#rev_10',",
    f"'{NOTE470}', 'Assets/Scripts/UI/CollectAndWin/CollectAndWinMainScreenController.cs', '', NULL, NULL, NULL, NULL, '{AT470}', '{PR}470#rev_9',")
m470, ts470 = mirror(470, "Collect And Win minor bugs fixes", "discussion_r2391980467", "arthur.blake", NOTE470, AT470,
                     "c2b9c90355cf8c2c4326ab19d3a24f79", "1759180973.545069")
assert ts470 < "1759247478.371389"      # the thread's newest reply stays the base "merged" post
rep(line_with("VALUES ('c778c9b9d8fff77f59c93ce8d7902953'"), m470)
rep("UPDATE slack.slack_messages SET reply_count = 17, latest_reply = '1759248252.248252' WHERE id = 'c2b9c90355cf8c2c4326ab19d3a24f79';",
    "UPDATE slack.slack_messages SET reply_count = 17, latest_reply = '1759247478.371389' WHERE id = 'c2b9c90355cf8c2c4326ab19d3a24f79';")

# ---- #468: Claire owns the 3D vial objects (Martin owns the UI sprites, which this PR already ships in five colours)
VIAL_AT = "2025-09-29T15:36:41Z"
OLD_VIAL = ("The final vial sprites are still missing for the Collect & Win set \u2014 Claire has those on her list. "
            "Everything else on the art side of this PR is settled from my side.")
NEW_VIAL = ("The Collect & Win vials that spawn in the levels are still the first-pass models. "
            "The final vial models are missing, Claire has those on her list.")
rep(f"'{OLD_VIAL}', 'Assets/Sprites/CollectAndWin/icn - poison - red.png.meta',", f"'{NEW_VIAL}', 'Assets/Match3D/Game/Levels/GameLoader.cs',")
# #468#ev_6 (the review's timeline event) stays: base pairs reviews with one, and it keeps the row count at the agreed floor
m468, _ = mirror(468, "Collect And Win", "discussion_r2388843617", "arthur.blake", NEW_VIAL, VIAL_AT,
                 "4b7c41278397b56b36e9b2f8a820c454", "1758917788.864169")
rep(line_with("discussion_r2388843617"), m468)
rev468 = card_json("4b7c41278397b56b36e9b2f8a820c454", "Reviewers", "<https://github.com/apps/coderabbitai|@coderabbitai[bot]>",
                   "<https://github.com/apps/coderabbitai|@coderabbitai[bot]>, <@EMPLOYEE_0025_SLACK_ID>")
rep("UPDATE slack.slack_messages SET reply_count = 42, latest_reply = '1759162433.383449' WHERE id = '4b7c41278397b56b36e9b2f8a820c454';",
    f"UPDATE slack.slack_messages SET reply_count = 42, latest_reply = '1759162433.383449', attachments_json = '{rev468}' WHERE id = '4b7c41278397b56b36e9b2f8a820c454';")

# ---- #473: which range the strip is on, and by when it has to change
STRIP_AT = "2025-09-30T16:16:33Z"
OLD_STRIP = ("The Season Pass premium strip needs to move to the November range rather than the current one \u2014 "
             "Oliver is taking the date change.")
NEW_STRIP = ("The Season Pass premium strip is still set to the October range. It needs the November range before that season opens, "
             "Oliver is taking the date change.")
rep(f"'{OLD_STRIP}', '{STRIP_AT}', '{STRIP_AT}');", f"'{NEW_STRIP}', '{STRIP_AT}', NULL);")
m473, ts473 = mirror(473, "Addressables/sp", "issuecomment-3352918642", "arthur.blake", NEW_STRIP, STRIP_AT,
                     "d05a2f8a3c4ada2d6b91c809e04222dc", "1759246868.802449")
rep(line_with("issuecomment-3352918642"), m473)
cnt473 = card_json("d05a2f8a3c4ada2d6b91c809e04222dc", "Comments", "1", "2")
rep("UPDATE slack.slack_messages SET reply_count = 3, latest_reply = '1759248993.248993' WHERE id = 'd05a2f8a3c4ada2d6b91c809e04222dc';",
    f"UPDATE slack.slack_messages SET reply_count = 3, latest_reply = '{ts473}', attachments_json = '{cnt473}' WHERE id = 'd05a2f8a3c4ada2d6b91c809e04222dc';")

# ---- #471: nothing injected on it any more (a note 5 h after the merge has no base precedent); see ZOM-432 below
drop(f"VALUES ('{PR}471#c_18'")
drop(f"VALUES ('{PR}471#ev_8'")
drop(f"WHERE id = '{PR}471';")
drop("VALUES ('a0c2677988d2041ff14477598ee60261'")
drop("WHERE id = 'da3fe08c76cb0ac8a9337166c8a51d00';")
assert f"{PR}471" not in s

# ================================================================ B. Slack messages written by people
def retime(old_id, channel, old_ts, new_ts):
    """New ts (ends in 9, off the whole minute where it was on it); id and created_at follow; returns the new id."""
    assert new_ts.endswith("9")
    new_id = slack_id(channel, new_ts)
    rep(f"VALUES ('{old_id}', '{old_ts}', '{channel}',", f"VALUES ('{new_id}', '{new_ts}', '{channel}',")
    rep(f"'{slack_created(old_ts)}', '{{}}');", f"'{slack_created(new_ts)}', '{{}}');")
    return new_id


ASK_OLD, ASK_NEW = "1759263600.418207", "1759263617.418209"          # 20:20:17Z
REPLY_OLD, REPLY_NEW = "1759263878.305127", "1759263878.305129"      # 20:24:38Z
ask_id = retime("8b090dec472117f4598b9ad84318272e", "D05SD5QLG94", ASK_OLD, ASK_NEW)
retime("097c95c6e043ada8294b60f13e1656ba", "D05SD5QLG94", REPLY_OLD, REPLY_NEW)
rep(f", NULL, '{ASK_OLD}', 1, 1, '{REPLY_OLD}', false,", f", NULL, '{ASK_NEW}', 1, 1, '{REPLY_NEW}', false,")             # the ask's own thread fields
rep(f", '8b090dec472117f4598b9ad84318272e', '{ASK_OLD}', 0, 0, NULL, false,", f", '{ask_id}', '{ASK_NEW}', 0, 0, NULL, false,")  # the reply's parent
APPR_OLD, APPR_NEW = "1758213600.552913", "1758213623.552919"        # 16:40:23Z
retime("2e75e232f5e6206273411a8305ac5d01", "C08R8CHB0QL", APPR_OLD, APPR_NEW)
rep(f"UPDATE slack.slack_messages SET reply_count = 1, reply_users_count = 1, latest_reply = '{APPR_OLD}' WHERE id = '9025d428af1f551a20e303c3acbc545b';",
    "UPDATE slack.slack_messages SET thread_ts_legacy = '1758121809.236839', reply_count = 1, reply_users_count = 1, "
    f"latest_reply = '{APPR_NEW}' WHERE id = '9025d428af1f551a20e303c3acbc545b';")       # base parents with replies carry their own thread ts
retime("58d06bd55ea4129eaadb726291967d5a", "D05GU6L0XFH", "1759270200.638114", "1759270241.638119")     # 22:10:41Z
retime("fa3eee2c614b0741aeb240275f86abf7", "C0880U9751A", "1759265412.481907", "1759265412.481909")     # 20:50:12Z

# ================================================================ C. Linear comments
CMT = re.compile(r"VALUES \('(cmt_zom\d+_\d)', '(ZOM-\d+)', '([^']+)', NULL, '((?:[^']|'')*)', false, '([^']+)', '([^']+)', (\d+)\);")


def comment(cid, body=None, at=None):
    global s
    hits = [m for m in CMT.finditer(s) if m.group(1) == cid]
    assert len(hits) == 1, cid
    m = hits[0]
    new_body = q(body) if body is not None else m.group(4)
    new_at = at or m.group(5)
    assert (body is None or new_body != m.group(4)) and (at is None or at != m.group(5)), f"no change for {cid}"
    s = s[:m.start()] + f"VALUES ('{cid}', '{m.group(2)}', '{m.group(3)}', NULL, '{new_body}', false, '{new_at}', '{new_at}', {m.group(7)});" + s[m.end():]


def issue_update(issue, old_set, new_set):
    rep(f"UPDATE linear.linear_issues SET {old_set} WHERE id = '{issue}';", f"UPDATE linear.linear_issues SET {new_set} WHERE id = '{issue}';")


# ZOM-429: the note predates the Sep 19 regression that Vincent reported on Sep 22 ("Killing the app doesn't help");
# base already carries a later updated_at (Sep 22), so no bump
comment("cmt_zom429_1", at="2025-09-16T18:12:00Z")
drop("WHERE id = 'ZOM-429';")

# ZOM-556: the day row not resetting IS the reported bug; claiming works
comment("cmt_zom556_1", "Claimed the daily gift on the submission build after skipping a day, it paid out and moved to the next day. "
                        "So the lower day row still carries on instead of going back to day 1, but claiming works and nothing is lost.")

# ZOM-565: base has the new bar hidden on Marcus's branch for Calvin to hook up (commit at 14:33:08Z, his DM
# "i wrote a comment on the linear task" at 14:34:25Z) and the glow showing on every box; the ticket stays Todo
comment("cmt_zom565_1", "Calvin, I pushed a small change to the endless screen prefab on my branch (Marcus/EndlessMode_Vfx). "
                        "The new bar is still hidden in there for you to hook up, and the glow still shows on every box until it is tied to the Claim state. "
                        "This is the P1/P2 endless polish from the list Brian gave me, the screen already works without it, so it is not needed for the beta.",
        at="2025-09-29T14:34:00Z")
issue_update("ZOM-565", "state_id = 'Done', completed_at = '2025-09-29T17:10:00Z', updated_at = '2025-09-29T17:10:00Z'",
             "updated_at = '2025-09-29T14:34:00Z'")

# ZOM-526: token travel exists for Season Pass (on main since PR #438, Sep 15) and Collect and Win (trigger on its branch until Sep 29)
comment("cmt_zom526_1", "Token-to-live-ops travel is in progress. Season Pass tokens already fly to the icon; "
                        "the Collect and Win trigger is on its branch, waiting for the merge.")
comment("cmt_zom526_2", "Unticked this one on the master ticket, it was marked done too early. What is left is the Collect and Win trigger "
                        "I mentioned above. It is polish on an effect that already ships for Season Pass, and the event runs without it, "
                        "so it does not have to land before the beta.")

# ZOM-552: all three events were in by Sep 19; there are no release notes in base
comment("cmt_zom552_1", "Season pass redeem events are being sent. Left and premium are in from the sheet as well; "
                        "keeping this open until the data is checked against the sheet.")

# ZOM-432: Samuel's frame note sits on the ticket it closes
FRAME_AT = "2025-09-30T21:07:26Z"
FRAME = ("The frame went out with PR #471. It is in both submission builds from today, iOS 50 and Android 135, "
         "so nothing is left here. Closing.")
ln432 = line_with("VALUES ('cmt_zom432_1'")
rep(ln432, ln432 + "\nINSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) "
                   f"VALUES ('cmt_zom432_2', 'ZOM-432', 'usr_caafeec2804b3a67', NULL, '{FRAME}', false, '{FRAME_AT}', '{FRAME_AT}', 2);")
issue_update("ZOM-432", "state_id = 'Done', completed_at = '2025-09-30T21:20:00Z', updated_at = '2025-09-30T21:20:00Z'",
             f"state_id = 'Done', completed_at = '{FRAME_AT}', updated_at = '{FRAME_AT}'")

# ZOM-465: the icons animate when they call for action, not at idle
comment("cmt_zom465_1", "Idle icon animations for the event icons are done and in the animated-icons PRs, "
                        "so every event icon on the main menu has its animation now.")

# ZOM-344: "the hub" is not a term the base uses
comment("cmt_zom344_1", "Quest box open and close animation reuses the endless chest curve and reads well on the quest screen. "
                        "Art side is signed off on my end.")

# ZOM-387: base has this as Arthur's ticket with its PR merged on Jul 19; leave the ticket exactly as base has it
drop("VALUES ('cmt_zom387_1'")
drop("WHERE id = 'ZOM-387';")

# ZOM-442: the event and two of its parameters are in code; three sheet super properties are not sent
comment("cmt_zom442_1", "Trophy reward redeem fires, and its trophy_level and chest_content parameters match the sheet tab.")

# ZOM-471: nothing wired on main; the creating thread in #zombie-match3d has Leonard saying to drop it
comment("cmt_zom471_1", "Not started. In the thread this came from Leonard said we do not need it, and the Plague Race icon already shows "
                        "the Start button when the player is outside a race. Parking it, nothing here has to land for the beta.")
issue_update("ZOM-471", "state_id = 'Done', completed_at = '2025-09-17T16:45:00Z', updated_at = '2025-09-17T16:45:00Z'",
             "updated_at = '2025-09-17T16:45:00Z'")

# ZOM-504: Vincent's own base word is that it only reproduces with the bot
comment("cmt_zom504_1", "Still only shows up with the bot running; in manual play across a long endless session I could not get it. "
                        "When it happens the object clears on the next throw. Visual only, no board state affected.")

# ZOM-517: there is no refill flag in the code; Robert was in another thread at 14:50Z
comment("cmt_zom517_1", "Retested in endless mode. Enraged monsters kept their enrage through item refills, "
                        "could not get one to lose it while walking.", at="2025-09-18T17:40:00Z")
issue_update("ZOM-517", "updated_at = '2025-09-18T14:50:00Z'", "updated_at = '2025-09-18T17:40:00Z'")

# ZOM-521: on Sep 26 neither open item was finished (queue integration merged Sep 30, cards reached a test build Sep 29)
comment("cmt_zom521_1", "Master VFX checklist is down to the last two items: tokens traveling to live-ops and claimed cards traveling "
                        "to inventory. Cards VFX is what I am on now.")

# ZOM-542: the new screens are not on main; the ticket stays in its base state; Julia's own Sep 22 status post has Samuel on the bug list
comment("cmt_zom542_1", "Not in the build yet: the home screen and victory score changes for endless and boss arena are still at the mockup stage. "
                        "I am on the bug list first, and this is a layout refresh on screens that already work, so it is not needed for the beta.")
issue_update("ZOM-542", "state_id = 'Done', completed_at = '2025-09-22T18:40:00Z', updated_at = '2025-09-22T18:40:00Z'",
             "updated_at = '2025-09-22T18:40:00Z'")

# ZOM-544: Vincent's base messages have sign-in in the settings menu since Sep 22 and progress not restoring
comment("cmt_zom544_1", "Apple sign-in works from the settings menu on the auth branch, but progress does not restore yet: "
                        "levels, currencies and cards are not synced. Google Play login is still waiting on the backend setup.")

# ZOM-546: inside Owen's usual hours
comment("cmt_zom546_1", at="2025-09-24T19:00:00Z")
issue_update("ZOM-546", "updated_at = '2025-09-24T14:05:00Z'", "updated_at = '2025-09-24T19:00:00Z'")

# ZOM-549: left_level does not send total_equipped_power on main
comment("cmt_zom549_1", "The new endless_left fields (endless_level, nuke_damage_total, total_equipped_power) are in the payload. "
                        "left_level does not send total_equipped_power yet.")

# ZOM-566: at 19:40Z nothing was committed (first commit 22:23Z, PR #477 opened 22:26Z and is still open)
comment("cmt_zom566_1", "Collect and Win event list is mapped to the sheet (start and redeem). "
                        "Wiring both into the analytics manager now, ahead of the beta.")

# ---- seconds on every whole-minute Linear timestamp (base issue stamps are never on the whole minute as a set)
a = s.index("-- Linear per-issue comments")
b = s.index("INSERT INTO trello.trello_actions")
sec = s[a:b]
FIXED = {"2025-09-29T14:34:00Z": "2025-09-29T14:34:12Z"}      # after the 14:33:08Z commit, before the 14:34:25Z DM that mentions the comment
for stamp in sorted(set(re.findall(r"'(2025-\d\d-\d\dT\d\d:\d\d:00Z)'", sec))):
    new = FIXED.get(stamp) or stamp[:-3] + f"{int(hashlib.sha256(stamp.encode()).hexdigest(), 16) % 58 + 1:02d}Z"
    sec = sec.replace(f"'{stamp}'", f"'{new}'")
assert not re.search(r"'2025-\d\d-\d\dT\d\d:\d\d:00Z'", sec)
s = s[:a] + sec + s[b:]

# ================================================================ D. Gmail
MAILS = {  # old shared thread id -> everything that changes for that mail
    "1844470925517303296": {"old_mid": "<CAH4q9Zb2fK7xQe1M8sPnL3vT6wR0yDc@mail.gmail.com>",
                            "new_mid": "<CAPT--p4sBC8XnaA7qBDMtZkWqJPiXP0MT3deOQGPusOZhHF+vo@mail.gmail.com>",
                            "old_ms": 1758532320000, "new_ms": 1758532361000,
                            "old_date": "2025-09-22T09:12:00+00:00", "new_date": "2025-09-22T09:12:41+00:00",
                            "old_hdr": "Mon, 22 Sep 2025 09:12:00 +0000", "new_hdr": "Mon, 22 Sep 2025 12:12:41 +0300",
                            "old_mbox": "Mon Sep 22 09:12:00 +0000 2025", "new_mbox": "Mon Sep 22 09:12:41 +0000 2025",
                            "low": {"brian.foster": 174017, "julia.lawson": 597812, "frederick.stone": 853474}},
    "1844835127305531392": {"old_mid": "<CAH4q9Zc8uV1nE5kJ2mRtP7aW3xQ9bLs@mail.gmail.com>",
                            "new_mid": "<CAPT--p4a5fY9wd6vr+8JtjFXfffkxQOCEUYsuqSPy9HbQJu3Fs@mail.gmail.com>",
                            "old_ms": 1758872400000, "new_ms": 1758872426000,
                            "old_date": "2025-09-26T07:40:00+00:00", "new_date": "2025-09-26T07:40:26+00:00",
                            "old_hdr": "Fri, 26 Sep 2025 07:40:00 +0000", "new_hdr": "Fri, 26 Sep 2025 10:40:26 +0300",
                            "old_mbox": "Fri Sep 26 07:40:00 +0000 2025", "new_mbox": "Fri Sep 26 07:40:26 +0000 2025",
                            "low": {"brian.foster": 231905, "julia.lawson": 664123, "frederick.stone": 912046}},
}
new_thread_ids = []
for old, mm in MAILS.items():
    assert len(mm["new_mid"]) - len("<@mail.gmail.com>") == 51 and mm["new_mid"].startswith("<CAPT--p4")      # Brian's base Message-ID shape
    for box, low in mm["low"].items():
        new = str((mm["new_ms"] << 20) + low)
        assert int(new) >> 20 == mm["new_ms"]                                   # base: thread id >> 20 is the mail's time in ms
        new_thread_ids.append(new)
        mail = f"{box}@harmonygames.co"
        rep(f"VALUES ('{mail}/{old}', '{mail}',", f"VALUES ('{mail}/{new}', '{mail}',")            # gmail_threads row
        a = s.index(f"VALUES ('{mail}/{mm['old_mid']}'")
        b = s.index("'[]');", a) + len("'[]');")
        row = s[a:b]

        def sub(old_h, new_h, n=1):
            global row
            assert row.count(old_h) == n, (box, old, old_h, row.count(old_h))
            row = row.replace(old_h, new_h)

        sub(old, new, 3)                                                        # thread_id, X-GM-THRID, mbox_from
        sub(mm["old_mid"], mm["new_mid"], 2)                                    # id, Message-ID header
        sub(f", {mm['old_ms']}, '{mm['old_date']}',", f", {mm['new_ms']}, '{mm['new_date']}',")
        sub(f'{{"name":"Date","value":"{mm["old_hdr"]}"}}', f'{{"name":"Date","value":"{mm["new_hdr"]}"}}')
        sub(mm["old_mbox"], mm["new_mbox"])
        sub('{"name":"To","value":"Julia Lawson <julia.lawson@harmonygames.co>"}', '{"name":"To","value":"julia.lawson@harmonygames.co"}')
        sub('{"name":"Cc","value":"Frederick Stone <frederick.stone@harmonygames.co>"}', '{"name":"Cc","value":"frederick.stone@harmonygames.co"}')
        sub('{"name":"Reply-To","value":"Brian Foster <brian.foster@harmonygames.co>"},', '')      # reply_to_json is empty; base internal mail has none
        if box == "brian.foster":       # sent copy: no Delivered-To, filed Sent + Opened like base sent mail
            sub('\'["SENT"]\'', '\'["SENT","Label_b19fb8d1b3"]\'')
            sub('{"name":"X-Gmail-Labels","value":"Sent"}', '{"name":"X-Gmail-Labels","value":"Sent,Opened"}')
            sub('{"name":"Delivered-To","value":"julia.lawson@harmonygames.co"},', '')
        if box == "julia.lawson" and old == "1844470925517303296":      # the Sep 22 mail was opened (her mailbox marks that with this label)
            sub('\'["INBOX","CATEGORY_PERSONAL"]\'', '\'["INBOX","Label_b19fb8d1b3","CATEGORY_PERSONAL"]\'')
            sub('"value":"Inbox,Category Personal"}', '"value":"Inbox,Opened,Category Personal"}')
        if box == "julia.lawson" and old == "1844835127305531392":      # the correction is not opened yet; her mailbox never uses UNREAD
            sub('\'["INBOX","CATEGORY_PERSONAL","UNREAD"]\'', '\'["INBOX","CATEGORY_PERSONAL"]\'')
            sub('"value":"Inbox,Category Personal,Unread"}', '"value":"Inbox,Category Personal"}')
        s = s[:a] + row + s[b:]
    assert old not in s and mm["old_mid"] not in s, old
assert "UNREAD" not in s and "Unread" not in s and "Reply-To" not in s and len(set(new_thread_ids)) == 6

# ================================================================ E. Drive / Docs / Slides / Sheets / GCal
# folder: modified with its newest child (the calendar sheet's creation)
rep("'2025-09-30 06:30:00+00', '2025-08-11 07:20:00+00', NULL, false, false,", "'2025-09-30 06:35:14+00', '2025-08-11 07:20:38+00', NULL, false, false,")
# brief: Frederick's working hours (he has no base activity 07:00-11:59 UTC); Doc rows carry size and content_path in base
rep("'2025-09-24 10:40:00+00', '2025-09-24 10:15:00+00', NULL, false, false, NULL, NULL, NULL, NULL, NULL, NULL);",
    "'2025-09-24 17:40:52+00', '2025-09-24 17:15:22+00', 13872, false, false, "
    "'frederick.stone@harmonygames.co/ZM3D beta live-ops calendar - working rules.docx', NULL, NULL, NULL, NULL, NULL);")
rep("'4c1a7e9b02', 'f_7c3e91a4d2b85f60e1a9c4', '2025-09-24 10:15:00+00', '2025-09-24 10:40:00+00');",
    "'4c1a7e9b02', 'f_7c3e91a4d2b85f60e1a9c4', '2025-09-24 17:15:22+00', '2025-09-24 17:40:52+00');")
# deck
rep("'2025-09-23 16:05:00+00', '2025-09-23 16:05:00+00', NULL, false, false,", "'2025-09-23 16:05:43+00', '2025-09-23 16:05:43+00', NULL, false, false,")
rep("'a9d3f60c48', '2025-09-23T16:05:00Z', '2025-09-23T16:05:00Z');", "'a9d3f60c48', '2025-09-23T16:05:43Z', '2025-09-23T16:05:43Z');")
# calendar sheet: path includes its folder, as every base file path does
rep("'2025-09-30 06:38:00+00', '2025-09-30 06:35:00+00', NULL, false, false, NULL, NULL, NULL, NULL, NULL, NULL);",
    "'2025-09-30 06:38:27+00', '2025-09-30 06:35:14+00', 9216, false, false, "
    "'julia.lawson@harmonygames.co/ZM Live Ops/ZM3D Beta Live-Ops Calendar.xlsx', NULL, NULL, NULL, NULL, NULL);")
rep("'f_e4a17c90b3d25f6a8c1d73', '2025-09-30T06:35:00Z', '2025-09-30T06:38:00Z');", "'f_e4a17c90b3d25f6a8c1d73', '2025-09-30T06:35:14Z', '2025-09-30T06:38:27Z');")
# release event: Douglas's working hours, plain hyphen in the title
rep("'2025-09-24T13:05:00Z', '2025-09-26T11:20:00Z'", "'2025-09-24T16:05:37Z', '2025-09-26T17:20:09Z'", 4)
rep("'ZM3D backend release \u2014 live-ops server windows'", "'ZM3D backend release - live-ops server windows'", 4)

# ================================================================ G. deck: Unity retention budget was at $1 on Sep 23, not "running"
rep("The small retention campaigns already running are a separate budget and are not part of these buys.",
    "The Unity retention campaigns are a separate budget and are not part of these buys.")

# ================================================================ F. Trello: open quests card #61, by its owner
a = s.index("INSERT INTO trello.trello_actions")
b = s.index("WHERE id = '6851a724601a61857a1b202f';", a) + len("WHERE id = '6851a724601a61857a1b202f';")
QUEST = "New quest set goes in with the Mon Oct 13 rollover, the current set carries the first week."
data = {"board": {"id": "6851a6569f3bf818760632ab", "name": "ZM ROADMAP", "shortLink": "HSqnngwQ"},
        "card": {"id": "68c452a03006277f55d9dc96", "idShort": 61, "name": "Add more quests and balance quest rewards - (Leonard/Douglas)", "shortLink": "viBYIjSG"},
        "idCard": "68c452a03006277f55d9dc96",
        "list": {"id": "6851a674975da1fe76e70d93", "name": "BETA: Sep 30"},     # the name every base action on this list carries since Sep 12
        "text": QUEST, "textData": {"emoji": {}}}
badges = {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0, "checkItemsChecked": 0,
          "checkItemsEarliestDue": None, "comments": 1, "description": False, "due": None, "dueComplete": False, "externalSource": None,
          "fogbugz": "", "lastUpdatedByAi": False, "location": False, "maliciousAttachments": 0, "start": None, "votes": 0}
trello = ("INSERT INTO trello.trello_actions (id, type, date, \"idMemberCreator\", \"idBoard\", \"idCard\", data_json) VALUES "
          "('68dac8204f1e9a3b7c2d5e61', 'commentCard', '2025-09-29T17:55:44Z', 'PERSON_6094_TRELLO_USER_ID', '6851a6569f3bf818760632ab', "
          f"'68c452a03006277f55d9dc96', '{q(json.dumps(data, ensure_ascii=False, separators=(',', ':')))}');\n\n"
          "UPDATE trello.trello_cards\n"
          f"   SET badges_json = '{json.dumps(badges, separators=(',', ':'))}',\n"
          "       \"dateLastActivity\" = '2025-09-29T17:55:44Z'\n"
          " WHERE id = '68c452a03006277f55d9dc96';")
s = s[:a] + trello + s[b:]
assert "6851a724601a61857a1b202f" not in s

# ================================================================ tidy and write
rep("-- Linear per-issue comments (22 cohort issues) + Trello quests-card comment", "-- Linear per-issue comments (21 cohort issues) + Trello quests-card comment")
while "\n\n\n" in s:
    s = s.replace("\n\n\n", "\n\n")
body_wo_header = s.split("\n", 3)[3]
for gone in ("cmt_zom387", "ZOM-387", "release notes", "refill flag", "can close.", "#470#rev_10", "#471#", "Reply-To", "beta buy or",
             "8b090dec472117f4598b9ad84318272e", "CAH4q9Z"):
    assert gone not in s, gone
assert "\u2014" not in body_wo_header, "em dash left in a record"
for ts in re.findall(r"VALUES \('[0-9a-f]{32}', '(\d+\.\d+)',", s):
    assert ts.endswith("9"), ts
open(dst, "w", encoding="utf-8").write(s)
print("written", dst, hashlib.sha256(s.encode()).hexdigest(), len(s.encode()), "bytes")
print("ask id", ask_id, "| mirror ts", ts470, ts473, "| thread ids", new_thread_ids)
