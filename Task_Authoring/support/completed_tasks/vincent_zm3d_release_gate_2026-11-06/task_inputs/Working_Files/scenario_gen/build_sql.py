#!/usr/bin/env python3
"""Generator for 01_Universe_Inject.sql (Vincent Parker, ZM3D store release gate). Never executes SQL.

Run from the workspace root:  python3 -B Task_Authoring/task_inputs/Working_Files/scenario_gen/build_sql.py
Writes Task_Authoring/task_inputs/01_Universe_Inject.sql and scenario_gen/records.json (the record ledger the dossier,
the final manifest and the solver read).
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TASK = HERE.parents[1]
WF = TASK / "Working_Files"
IDS = json.loads((HERE / "ids.json").read_text())
MINTED = json.loads((WF / "research/tmp_ids/minted.json").read_text())
ZOM = {m["record"]["identifier"]: m["record"] for m in json.loads((WF / "research/zom.json").read_text())["checks"]["zom"]["matches"]}

VINCENT, ARTHUR, LEONARD, BRIAN, DOUGLAS, OLIVER, ROBERT = (
    "vincent.parker@harmonygames.co", "arthur.blake@harmonygames.co", "leonard.hayes@harmonygames.co",
    "brian.foster@harmonygames.co", "douglas@harmonygames.co", "oliver.brooks@harmonygames.co", "robert@harmonygames.co")
NAME = {VINCENT: "Vincent Parker", ARTHUR: "Arthur Blake", LEONARD: "Leonard Hayes", BRIAN: "Brian Foster",
        DOUGLAS: "Douglas", OLIVER: "Oliver Brooks", ROBERT: "Robert"}
LUSR = {VINCENT: "usr_65c76e0b87aa7e9b", ARTHUR: "usr_cc3e90160f490686", LEONARD: "usr_63fffeb4fab5233e",
        BRIAN: "usr_fc22d5941b2aeb5c", DOUGLAS: "usr_cd7849ec043ab3da", OLIVER: "usr_bdf01b53c6a92c5e",
        "samuel.turner@harmonygames.co": "usr_caafeec2804b3a67"}
SAMUEL = "samuel.turner@harmonygames.co"
SLK = {VINCENT: "EMPLOYEE_0012_SLACK_ID", ARTHUR: "EMPLOYEE_0025_SLACK_ID", LEONARD: "EMPLOYEE_0038_SLACK_ID",
       BRIAN: "EMPLOYEE_0026_SLACK_ID", DOUGLAS: "EMPLOYEE_0031_SLACK_ID"}
GH = {ARTHUR: "EMPLOYEE_0025_GITHUB_USERNAME", DOUGLAS: "PERSON_5760_GITHUB_USERNAME"}
TRELLO = {ARTHUR: "2162c1ba310341bf318f48b7", LEONARD: "PERSON_6094_TRELLO_USER_ID"}
VENDOR_EMAIL, VENDOR_NAME = "PERSON_9701_EMAIL", "PERSON_9701_NAME"

OUT: list[str] = []
LEDGER: list[dict] = []


def q(v) -> str:
    if v is None:
        return "NULL"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return repr(v)
    return "'" + str(v).replace("'", "''") + "'"


def j(v) -> str:
    return q(json.dumps(v, ensure_ascii=False, separators=(",", ":")))


def ins(table: str, row: dict, ledger: dict | None = None) -> None:
    cols = ", ".join(f'"{c}"' if (c != c.lower() or c in ("references", "index", "desc")) else c for c in row)
    OUT.append(f"INSERT INTO {table} ({cols}) VALUES ({', '.join(row.values())});")
    if ledger:
        LEDGER.append({"table": table, **ledger})


def upd(table: str, sets: dict, where: str, ledger: dict | None = None) -> None:
    s = ", ".join(f'{(chr(34) + c + chr(34)) if c != c.lower() else c} = {v}' for c, v in sets.items())
    OUT.append(f"UPDATE {table} SET {s} WHERE {where};")
    if ledger:
        LEDGER.append({"table": table, "op": "update", **ledger})


def ep(iso: str) -> int:
    return int(dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp())


def sha(s: str, n: int) -> str:
    return hashlib.sha256(s.encode()).hexdigest()[:n]


# ====================================================================== Linear
def issue(key, team, title, desc, creator, assignee, state, created, priority, labels, completed=None, updated=None,
          role="", element=""):
    num = int(key.split("-")[1])
    ins("linear.linear_issues", {
        "id": q(key), "project_id": "NULL", "team_id": q(team), "parent_id": "NULL",
        "assignee_id": q(LUSR.get(assignee)) if assignee else "NULL", "creator_id": q(LUSR[creator]),
        "state_id": q(state), "cycle_id": "NULL", "identifier": q(key), "number": str(num), "title": q(title),
        "description": q(desc), "priority": str(priority), "estimate": "NULL", "due_date": "NULL", "started_at": "NULL",
        "completed_at": q(completed), "canceled_at": "NULL", "archived_at": "NULL", "time_in_status_minutes": "NULL",
        "labels_json": j(labels), "links_json": "'[]'", "relations_json": "'[]'", "state_history_json": "'[]'",
        "is_archived": "false", "created_at": q(created), "updated_at": q(updated or completed or created)},
        {"id": key, "service": "linear", "container": f"linear:{key}", "role": role, "element": element,
         "at": created, "author": creator})


COMMENT_TIMES: dict[str, str] = {}


def comment(cid, key, author, body, at, role="", element=""):
    ins("linear.linear_comments", {
        "id": q(cid), "issue_id": q(key), "author_id": q(LUSR[author]), "parent_id": "NULL", "body": q(body),
        "is_edited": "false", "created_at": q(at), "updated_at": q(at)},
        {"id": cid, "service": "linear", "container": f"linear:{key}", "role": role, "element": element, "at": at,
         "author": author})
    COMMENT_TIMES[key] = max(COMMENT_TIMES.get(key, ""), at)


NEW_ISSUES = [
    ("ZOM-567", "team_ZOM", "Zombie Lane chests claimed on prod don't land in the inventory",
     "Since this morning Zombie Lane chests on prod show the reward popup but nothing lands in the inventory. "
     "Checked on two accounts (Android #133 and iOS #49 against prod): bones and cards are both missing after the "
     "popup closes. The claim call returns ok in the client log, so probably server side.",
     VINCENT, DOUGLAS, "Done", "2025-09-30T16:40:00Z", 1, ["Bug"], "2025-09-30T19:00:00Z", None,
     "claim met first", "T2 / CH-R4 done ticket"),
    ("ZOM-568", "team_ZOM", "Settings language list jumps back to the top while scrolling",
     "Settings > Language: the list jumps back to the top after every scroll on Android #133. You can still pick a "
     "language, it just takes a few tries.",
     VINCENT, OLIVER, "Todo", "2025-09-30T16:55:00Z", 3, ["Bug"], None, None, "cohort member", "neutral control"),
    ("ZOM-569", "team_ZOM", "Season Pass opens twice from the join popup and leaves an empty screen",
     "Opening the Season Pass from the join popup opens a second Season Pass main screen on top of the first one. "
     "Closing the top one leaves an empty dark screen with no buttons and the only way out is killing the app. "
     "Android #133 and iOS #49.",
     VINCENT, OLIVER, "Done", "2025-09-30T17:10:00Z", 1, ["Bug"], "2025-09-30T18:05:00Z", None,
     "claim met first", "T1 done ticket (closed before both candidate jobs started)"),
    ("ZOM-570", "team_ZOM", "ZM store push - Android Submission #135 / iOS Submission #50",
     "Store push for ZM.\n\nCandidates: Android Submission #135 and iOS Submission #50, both started from main today. "
     "We decide at the go/no-go on Friday, invite coming.\n\nVincent - QA gate as usual: Leonard's "
     "submission rules and my note on how we cut submissions both apply, the docs are shared with you. Blockers go on this ticket by key, "
     "the existing ticket if there is one (I'm putting the reuse rule on the tech-issues card). I'll post the candidates in #zombie-bugs.\n\n"
     "Other push notes go in the comments here.",
     ARTHUR, VINCENT, "In Progress", "2025-09-30T20:20:00Z", 1, [], None, None, "hub / write target", "A1"),
    ("ZOM-571", "team_ZOM", "Gem pack price shows $0.00 for a second when the shop opens",
     "Opening the shop on iOS #50 shows $0.00 on every gem pack for about a second before the real prices load. "
     "Buying after the prices load works.", VINCENT, OLIVER, "Todo", "2025-09-30T20:40:00Z", 3, ["Bug"], None, None,
     "cohort member", "Sep 30 QA pass"),
    ("ZOM-572", "team_ZOM", "Win streak freezer counter shows 2 after using the last one",
     "Used my last win streak freezer on Android #135, the counter on the pre-level screen still says 2. Starting the "
     "next level shows none left, so it's only the label.", VINCENT, OLIVER, "Todo", "2025-09-30T20:55:00Z", 3,
     ["Bug"], None, None, "cohort member", "Sep 30 QA pass"),
    ("ZOM-573", "team_ZOM", "Collect&Win: claiming the 5th chest crashes the app",
     "Android #135 on a Pixel 6: claiming the 5th chest in Collect&Win closes the app straight to the home screen. "
     "Happened 3 times out of 3, the chest is claimable again after relaunch.", BRIAN, OLIVER, "Todo",
     "2025-09-30T21:05:00Z", 1, ["Bug"], None, None, "cohort member", "Sep 30 QA pass"),
    ("ZOM-574", "team_ZOM", "Zombie Lane info popup text is cut off in German",
     "The Zombie Lane info popup cuts the last line of the German text on iOS #50 (iPhone SE). Other languages fit.",
     VINCENT, OLIVER, "Todo", "2025-09-30T21:15:00Z", 4, ["Bug"], None, None, "cohort member", "Sep 30 QA pass"),
    ("ZOM-575", "team_ZOM", "Add a haptics toggle to settings",
     "Players asked for a way to turn haptics off. Add a toggle under Settings > Sound.", VINCENT, None, "Backlog",
     "2025-09-30T21:25:00Z", 0, ["Improvement"], None, None, "cohort member", "Sep 30 QA pass"),
    ("ZOM-576", "team_ZOM", "Season Pass premium tier claim drops the booster bundle",
     "Tier 12 premium reward on iOS #50 (sandbox purchase) is a booster bundle plus gems: claiming shows both reward "
     "animations but only the gems land and the tier is marked claimed, so the boosters are gone.", BRIAN, OLIVER, "Todo",
     "2025-09-30T21:40:00Z", 2, ["Bug"], None, None, "cohort member", "Sep 30 QA pass"),
    ("ZOM-577", "team_ZOM", "level_fail event is missing the booster_used param",
     "level_fail fires without booster_used on #135, so we can't see if boosters were used before a fail.",
     VINCENT, None, "Todo", "2025-09-30T21:50:00Z", 3, ["Analytics"], None, None, "cohort member", "Sep 30 QA pass"),
    ("ZOM-578", "team_ZOM", "Tutorial stuck at step 3 on a fresh install",
     "Fresh install of Android #135: at tutorial step 3 the hand points at the booster but tapping it does nothing. "
     "Can't get past it, killed the app twice and it comes back to the same step.", LEONARD, None, "Todo",
     "2025-09-30T22:15:00Z", 1, [], None, None, "filter member", "T6 unlabeled"),
    ("ZOM-579", "team_ZOM", "Boss arena hit VFX plays behind the board on iPad",
     "On iPad (iOS #50) the boss hit VFX renders behind the board, so you only see it at the edges. Damage numbers "
     "are fine.", VINCENT, None, "Todo", "2025-09-30T22:30:00Z", 4, ["VFX"], None, None, "cohort member",
     "Sep 30 QA pass"),
    ("ZOM-580", "team_ZOM", "Daily gift popup shows twice after the midnight reset",
     "After the daily reset the daily gift popup opens, I claim it, and it opens again empty right after. Android "
     "#135.", BRIAN, None, "Todo", "2025-09-30T22:50:00Z", 3, ["Bug"], None, None, "cohort member",
     "Sep 30 QA pass"),
    ("ART-793", "team_ART", "ZM3D - boss arena background flickers on iPhone 12",
     "The boss arena backdrop flickers between the day and the night texture every few seconds on iPhone 12 "
     "(iOS #49). Gameplay is fine, it's just distracting.", VINCENT, None, "Todo", "2025-09-29T15:00:00Z", 3,
     ["Bug"], None, None, "filter member", "T6 other team"),
    ("DES-313", "team_DES", "ZM level 214 can't be completed",
     "Level 214 asks for 3 jars but only 2 jars ever spawn, so the goal can't be reached and the level can't be "
     "finished. Tried 4 times on Android #133. Looks like the level data, not the code.", VINCENT, None, "Todo",
     "2025-09-29T15:20:00Z", 2, [], None, None, "filter member", "T6 other team"),
]

SETTLE = [  # (comment id, ticket, author, ISO time, body)
    ("cmt_zom237_1", "ZOM-237", VINCENT, "2025-09-29T09:05:00Z",
     "Tested on Android Submission #133 / iOS #49: opened a 10-card pack from the shop. On the second card the red NEW "
     "banner was already visible when the card flipped and then replayed its pop-in; the banner SFX fired on the 4th "
     "and 7th cards where no banner was shown. No effect on claiming the cards."),
    ("cmt_zom348_1", "ZOM-348", VINCENT, "2025-09-29T09:50:00Z",
     "Tested on Android Submission #133 / iOS #49: the 1000-coin common pack showed no discount ribbon, the 80-bone "
     "pack showed none either, and the catapult offer showed -25% against a 100-gem list price. Tapping buy opened "
     "the store sheet with the price that was shown and the purchase went through."),
    ("cmt_zom438_1", "ZOM-438", VINCENT, "2025-09-29T10:20:00Z",
     "Ran C_0120 five times on Android #133 / iOS #49. Monster count at level end was 12, 13, 11, 14, 12; the missing "
     "zombies never appeared, but the level still completed normally every run."),
    ("cmt_zom443_1", "ZOM-443", VINCENT, "2025-09-29T10:45:00Z",
     "On a win-streak bonus level (#133 / #49) the removed items came from the same three columns on four streaks in "
     "a row, while an off-streak level removed a mixed set. Play continued normally."),
    ("cmt_zom449_1", "ZOM-449", BRIAN, "2025-09-29T09:15:00Z",
     "Android Submission #133 on a low-end Android device: cold start into level 3, the tutorial highlight drew over "
     "the loading screen before the board appeared and the device stopped responding to taps for about 40 seconds; "
     "force-quit and relaunch got past it. MF11 microwave and MF12 controller still render with missing surfaces."),
    ("cmt_zom468_1", "ZOM-468", BRIAN, "2025-09-29T09:40:00Z",
     "Android Submission #133, same low-end device: boss buster rendered with half its body missing; opening a "
     "3-card pack showed two empty card slots until the pack was closed and reopened. Gameplay and claims were fine."),
    ("cmt_zom481_1", "ZOM-481", VINCENT, "2025-09-29T11:30:00Z",
     "At 120 CPM on #133 / #49 the health bar stayed about a second after the death animation, then disappeared. "
     "Nothing else was affected, the board cleared and the level finished."),
    ("cmt_zom504_1", "ZOM-504", VINCENT, "2025-09-29T11:55:00Z",
     "Endless horde on #133 / #49: a matched item stayed drawn on its old cell for two refills before disappearing; "
     "the cell still accepted matches and no input was lost."),
    ("cmt_zom505_1", "ZOM-505", VINCENT, "2025-09-29T12:40:00Z",
     "Android Submission #133: failed level 19 three times on purpose. Each retry reopened the tutorial panel over the "
     "pre-level screen; after tapping through all four steps the level started and could be played and finished. "
     "Same on a second install, never a case where the level couldn't start."),
    ("cmt_zom534_1", "ZOM-534", VINCENT, "2025-09-29T13:10:00Z",
     "#133 / #49 against prod: completed the daily quest and stayed in the quest panel; the points stayed at 5/5 and "
     "the chest stayed locked until the app was force-quit and reopened, then it reset. No quest rewards were lost."),
    ("cmt_zom554_1", "ZOM-554", VINCENT, "2025-09-29T13:35:00Z",
     "Android Submission #133: quit level 41 with the tornado booster mid-spin. On the next level the objects hung "
     "above their cells and drifted; matches didn't register on the floating pieces and the level couldn't be played "
     "until I force-quit and relaunched. Same on iOS #49."),
    ("cmt_zom556_1", "ZOM-556", VINCENT, "2025-09-29T14:05:00Z",
     "#133 / #49: claimed day 3, then skipped a day. On the next launch the panel still highlighted day 4 instead of "
     "going back to day 1, and claiming it moved the streak on instead of restarting it."),
    ("cmt_zom559_1", "ZOM-559", BRIAN, "2025-09-29T15:20:00Z",
     "Android Submission #133 on a Samsung S22: home out mid-level, come back, then finish the level. SFX were silent "
     "for the rest of the level and the victory screen froze with the reward panel half drawn for about 20 seconds; "
     "only a force-quit got me out, the level reward was there after relaunch."),
    ("cmt_zom564_1", "ZOM-564", BRIAN, "2025-09-30T21:20:00Z",
     "Checked on iOS #50 and Android #135: finished the tutorial, went back into level 6, no free label on the boosters and the "
     "inventory count stayed the same when I didn't use one. Used one and it took one, as it should."),
]


RECHECK = [  # Sep 30 evening re-checks of open bugs on the candidates (comment id, ticket, author, ISO, body)
    ("cmt_zom237_2", "ZOM-237", VINCENT, "2025-09-30T20:30:00Z",
     "#135 / #50: the NEW banner still replays on the second card and the SFX still fires on the wrong cards. Claims fine."),
    ("cmt_zom348_2", "ZOM-348", VINCENT, "2025-09-30T20:36:00Z",
     "Same on #135: catapult offer still shows -25% against the 100-gem list price, the other ribbons are still missing. "
     "Purchase goes through at the shown price."),
    ("cmt_zom427_1", "ZOM-427", VINCENT, "2025-09-30T20:42:00Z",
     "Android #135: launcher icon is still zoomed in, the zombie's head is cut off at the edges."),
    ("cmt_zom429_1", "ZOM-429", VINCENT, "2025-09-30T20:48:00Z",
     "Couldn't reproduce on #135 or #50: let the weekly leaderboard end with the app open, the new one started and the "
     "rewards were claimable without killing the app, 3 tries on each."),
    ("cmt_zom438_2", "ZOM-438", VINCENT, "2025-09-30T20:54:00Z",
     "#135: C_0120 still ends with 11-13 zombies, level completes."),
    ("cmt_zom443_2", "ZOM-443", VINCENT, "2025-09-30T21:00:00Z",
     "#135: same column pattern on streak bonus levels, no effect on play."),
    ("cmt_zom458_1", "ZOM-458", VINCENT, "2025-09-30T21:06:00Z",
     "Still there on #135 / #50: quit an algo level without passing and the home screen plays the level-pass animation, "
     "same as Brian found on #133 / #49."),
    ("cmt_zom504_2", "ZOM-504", VINCENT, "2025-09-30T21:12:00Z",
     "#50: matched item still lingers on its old cell for a refill in endless horde, the cell still works."),
    ("cmt_zom505_2", "ZOM-505", VINCENT, "2025-09-30T21:18:00Z",
     "#135: tutorial panel still reopens on every level 19 retry, level is playable after tapping through."),
    ("cmt_zom517_1", "ZOM-517", VINCENT, "2025-09-30T21:24:00Z",
     "Can't reproduce on #135 or #50 any more: the monster kept its enrage through 6 refills in endless, 4 runs on each."),
    ("cmt_zom520_1", "ZOM-520", VINCENT, "2025-09-30T21:30:00Z",
     "#135, level 21: the first loss still doesn't reset the win streak, the counter stays at 3."),
    ("cmt_zom534_2", "ZOM-534", VINCENT, "2025-09-30T21:36:00Z",
     "Against prod with #135: quest points still stuck at 5/5 until a restart, rewards fine."),
    ("cmt_zom535_1", "ZOM-535", VINCENT, "2025-09-30T21:42:00Z",
     "#135: fast matching still sends items at a zombie that just died, same as Brian found on #133."),
    ("cmt_zom546_1", "ZOM-546", VINCENT, "2025-09-30T21:48:00Z",
     "#135 / #50 endless: the board drains again after about 8 refills, down to 5 items with no match possible, the run "
     "can't go on."),
    ("cmt_zom554_2", "ZOM-554", VINCENT, "2025-09-30T21:54:00Z",
     "#50: quitting mid tornado still leaves the next level's objects floating, had to force-quit again."),
    ("cmt_zom556_2", "ZOM-556", VINCENT, "2025-09-30T22:00:00Z",
     "#135: a skipped day still doesn't reset the daily gift."),
    ("cmt_zom560_1", "ZOM-560", VINCENT, "2025-09-30T22:06:00Z",
     "#135 sandbox account: bought the abandoned pack, coins and boosters came in, the win streak freezer time still "
     "didn't."),
    ("cmt_zom481_2", "ZOM-481", VINCENT, "2025-09-30T22:10:00Z",
     "#135: the health bar still hangs around for a second after the death animation. Level finishes."),
    ("cmt_zom483_1", "ZOM-483", VINCENT, "2025-09-30T22:14:00Z",
     "#135 fresh install: killed the app with 50 min of the new-install infinite lives left, after relaunch the banner "
     "says 30 min and it counts down from there. The 20 min are gone."),
    ("cmt_zom562_1", "ZOM-562", VINCENT, "2025-09-30T22:18:00Z",
     "#135: still happens, saw single items after 2 of 8 refills in the boss arena."),
    ("cmt_zom568_1", "ZOM-568", VINCENT, "2025-09-30T22:30:00Z",
     "#135: the language list still jumps back to the top while scrolling."),
    ("cmt_art793_1", "ART-793", VINCENT, "2025-09-30T22:34:00Z",
     "#50 on the iPhone 12: the backdrop still flickers in the boss arena."),
    ("cmt_des313_1", "DES-313", VINCENT, "2025-09-30T22:38:00Z",
     "#135: level 214 still only spawns 2 jars, can't finish it."),
    ("cmt_zom449_2", "ZOM-449", BRIAN, "2025-09-30T22:20:00Z",
     "Android #135 on the same low-end device: cold start into level 3 froze again, taps did nothing until I "
     "force-quit."),
    ("cmt_zom468_2", "ZOM-468", BRIAN, "2025-09-30T22:26:00Z",
     "#135 low-end: boss buster still half missing, pack slots fine this time after one reopen."),
]


GATE22 = [  # Sep 22 gate notes on Android #127 / iOS #40 (the previous gate; before each ticket's completion)
    ("cmt_zom546_0", "ZOM-546", VINCENT, "2025-09-22T13:10:00Z",
     "#127: the refill still drains the board in endless after a few refills, same as before."),
    ("cmt_zom520_0", "ZOM-520", VINCENT, "2025-09-22T13:20:00Z",
     "#127, level 21: the first loss still doesn't reset the win streak."),
    ("cmt_zom473_0", "ZOM-473", VINCENT, "2025-09-22T13:30:00Z",
     "#127: the endless end screen can still be tapped away before the x2."),
    ("cmt_zom429_0", "ZOM-429", VINCENT, "2025-09-22T13:40:00Z",
     "#40: weekly leaderboard ended with the app open, the new one didn't start until I killed the app."),
    ("cmt_zom534_0", "ZOM-534", VINCENT, "2025-09-22T13:55:00Z",
     "Prod with the #127 client: quest points still don't reset until a restart."),
    ("cmt_zom535_0", "ZOM-535", VINCENT, "2025-09-22T14:10:00Z",
     "#127: fast matching still sends items at a zombie that just died."),
    ("cmt_zom517_0", "ZOM-517", VINCENT, "2025-09-22T14:25:00Z",
     "#127 endless: the monster still drops its enrage during the item refill."),
    ("cmt_zom503_0", "ZOM-503", VINCENT, "2025-09-22T14:40:00Z",
     "#127: giving lives in teams updates right away now, no tab change needed."),
    ("cmt_zom559_0", "ZOM-559", VINCENT, "2025-09-22T16:30:00Z",
     "Tried on #127 on a Pixel 6: homed out and back three times, sound and the victory screen were fine. Can't "
     "reproduce here, need a Samsung."),
]

LEAD_NOTES = [  # Leonard's calls on tickets his Sep 23 rules could read two ways (dated, before any completion)
    ("cmt_zom558_1", "ZOM-558", LEONARD, "2025-09-23T09:40:00Z",
     "This one is a bug, not one of the UI asks my rules call no call: the levels rule shows an icon where it should "
     "say \"Level:\". Gate it like any other bug."),
    ("cmt_zom477_1", "ZOM-477", LEONARD, "2025-09-24T09:20:00Z",
     "Still want the poison kill cam sped up, it\u2019s a bad experience. But it\u2019s the kill cam doing what we built it to do, "
     "so this is a tuning ask for after the push, not a bug. No call for the store gates."),
]

FIX_NOTES = [  # developer notes before each ticket's completion (fix provenance)
    ("cmt_zom557_1", "ZOM-557", OLIVER, "2025-09-22T18:40:00Z",
     "pushed the fix for the ConsecutiveLogins json mapping, it was always reading 0"),
    ("cmt_zom555_1", "ZOM-555", OLIVER, "2025-09-23T19:00:00Z",
     "switched it to the fade out when no cards are given, like Vincent asked"),
    ("cmt_zom536_1", "ZOM-536", SAMUEL, "2025-09-30T12:35:00Z",
     "updated the trampoline icon and the model, it's in #471 with the home screen fixes"),
    ("cmt_zom498_1", "ZOM-498", SAMUEL, "2025-09-30T12:36:00Z",
     "home screen fixes from the figma list are in #471"),
]

REPORTER_NOTES = [  # a reporter's own follow-up saying what goes wrong (dated long before the gate)
    ("cmt_zom293_1", "ZOM-293", VINCENT, "2025-07-03T17:42:00Z",
     "what goes wrong here: lost 4 in a row on level 63, it demoted me 1 -> 0 and reloaded into the tier 0 version (the "
     "tier drop itself works). but the glue + trampoline I'd picked for that retry were taken from my stock when the "
     "level started, and after the reload for the tier change neither was on the board. both gone, 600 coins worth. "
     "happened again on my next demotion"),
]

DEV_NOTES = [
    ("cmt_zom567_1", "ZOM-567", DOUGLAS, "2025-09-30T18:55:00Z",
     "it was the grant job on the backend, fix is in match3d-backend #36, merged"),
    ("cmt_zom569_1", "ZOM-569", OLIVER, "2025-09-30T18:02:00Z",
     "fixed on my branch, the join popup only opens one SP screen now"),
    ("cmt_zom570_1", "ZOM-570", LEONARD, "2025-09-30T20:52:00Z",
     "sign-off as a reply on Arthur's candidate thread in #zombie-bugs please, not a new post, so it stays on the "
     "candidate post"),
]


def linear():
    OUT.append("-- linear: Sep 29-30 tickets, the store release ticket and QA notes")
    for (key, team, title, desc, creator, assignee, state, created, prio, labels, completed, updated, role,
         element) in NEW_ISSUES:
        last = max([c[3] for c in DEV_NOTES + SETTLE + RECHECK + GATE22 + FIX_NOTES + LEAD_NOTES + REPORTER_NOTES if c[1] == key] + [completed or created])
        issue(key, team, title, desc, creator, assignee, state, created, prio, labels, completed, last, role, element)
    for cid, key, author, at, body in DEV_NOTES:
        comment(cid, key, author, body, at, "evidence" if key != "ZOM-570" else "amendment",
                {"ZOM-567": "T2", "ZOM-569": "T1", "ZOM-570": "K10"}[key])
    for cid, key, author, at, body in SETTLE:
        role = {"ZOM-559": "overturning", "ZOM-564": "overturning"}.get(key, "settling note")
        comment(cid, key, author, body, at, role, {"ZOM-559": "T12", "ZOM-564": "T15"}.get(key, "cohort"))
    for cid, key, author, at, body in RECHECK:
        comment(cid, key, author, body, at, "QA re-check on the candidates", "cohort (R3/R5)")
    for cid, key, author, at, body in GATE22:
        comment(cid, key, author, body, at, "older QA result (Sep 22 gate)", "cohort (R3) / T12")
    for cid, key, author, at, body in FIX_NOTES:
        comment(cid, key, author, body, at, "fix provenance", "cohort (R2)")
    new_keys = {x[0] for x in NEW_ISSUES}
    for cid, key, author, at, body in LEAD_NOTES:
        comment(cid, key, author, body, at, "settling note (lead)", "cohort (R5)")
    for cid, key, author, at, body in REPORTER_NOTES:
        comment(cid, key, author, body, at, "overturning", "T17 what goes wrong (outside the obvious filter)")
    for key in sorted({c[1] for c in SETTLE + RECHECK + GATE22 + FIX_NOTES + LEAD_NOTES + REPORTER_NOTES} - new_keys):
        base = ZOM[key]["updated_at"]
        if COMMENT_TIMES[key] > base:
            upd("linear.linear_issues", {"updated_at": q(COMMENT_TIMES[key])}, f"id = {q(key)}",
                {"id": key, "service": "linear", "container": f"linear:{key}", "role": "companion",
                 "element": "updated_at follows the new comment", "at": COMMENT_TIMES[key]})


# ====================================================================== Slack
def slack_id(ch, ts):
    return hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]


def slack_ts(ref):
    return ref.split("/")[1]


def created_at(ts):
    s, us = ts.split(".")
    return dt.datetime.fromtimestamp(int(s), dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S") + f".{us}Z"


def smsg(ref, user, text, parent=None, replies=None, role="", element=""):
    ch, ts = ref.split("/")
    row = {"id": q(slack_id(ch, ts)), "ts": q(ts), "channel_id": q(ch), "type": "'message'", "user_id": q(user),
           "text": q(text), "thread_parent_id": "NULL", "thread_ts_legacy": "NULL", "reply_count": "0",
           "reply_users_count": "0", "latest_reply": "NULL", "is_activity_message": "false", "subtype": "NULL",
           "reactions_json": "'[]'", "files_json": "'[]'", "attachments_json": "'[]'", "created_at": q(created_at(ts)),
           "metadata_json": "'{}'"}
    if parent:
        pch, pts = parent.split("/")
        row["thread_parent_id"] = q(slack_id(pch, pts))
        row["thread_ts_legacy"] = q(pts)
    if replies:
        row["thread_ts_legacy"] = q(ts)
        row["reply_count"] = str(len(replies))
        row["reply_users_count"] = str(len({u for u, _ in replies}))
        row["latest_reply"] = q(max(t for _, t in replies))
    ins("slack.slack_messages", row, {"id": ref, "service": "slack", "container": f"slack:{ch}", "role": role,
                                       "element": element, "at": created_at(ts)[:19] + "Z",
                                       "author": next(k for k, v in SLK.items() if v == user)})


def slack():
    OUT.append("-- slack: candidate thread in #zombie-bugs, re-test notes and DMs")
    ann, green = IDS["slack_announce"], IDS["slack_green"]
    smsg(IDS["slack_pass133"], SLK[VINCENT],
         "re-tested on Android #133 / iOS #49: trophy path claim spam is ok now (ZOM-435), consecutive login quest ok "
         "too (ZOM-557) :white_check_mark:", role="claim met first", element="T3 older pass")
    smsg(IDS["slack_gate22"], SLK[VINCENT],
         "gate for #127 / #40 done, Bug tickets only this time. tab is in my release sheet", role="claim met first",
         element="T6 / T12 older gate")
    smsg(ann, SLK[ARTHUR],
         "ZM store candidates are up: Android Submission #135 and iOS Submission #50, both from main. "
         "<@EMPLOYEE_0012_SLACK_ID> QA gate before friday's go/no-go please, details on ZOM-570",
         replies=[(SLK[BRIAN], slack_ts(green))], role="destination", element="K9")
    smsg(green, SLK[BRIAN], "regression matrix green on #135 and #50 from my side :+1:", parent=ann,
         role="claim met first", element="T4 / T10 green summary")
    smsg(IDS["slack_dm_brian"], SLK[BRIAN],
         "abi endless bitiş ekranı iOS #50'de hala geçilebiliyor. run bittiğinde hızlı match yapıyordum, x2'den önce "
         "tıklayıp geçtim, coinler x2 olmadan geldi, run'ın coinlerinin yarısı gitti. ZOM-473", role="overturning", element="T3b re-test")
    smsg(IDS["slack_fixes"], SLK[VINCENT],
         "checked the fixes since the sep 22 gate on #135 / #50: ZOM-503 giving lives ok, ZOM-506 zombie lane text ok, "
         "ZOM-557 consecutive login ok, ZOM-561 low-end black surfaces ok, ZOM-434 no flying items after backgrounding "
         "during load, ZOM-558 weekly board says Level: now. rest tomorrow", role="evidence",
         element="controls (R3)")
    smsg(IDS["slack_dm_doc"], SLK[BRIAN], "update path satırlarını da bitirdim, bi dokümana yazdım seninle paylaştım",
         role="connecting", element="T4 pointer to the test log")
    smsg(IDS["slack_dm_brian29"], SLK[BRIAN],
         "abi bugün #133 ve #49'da iki tane buldum, ikisi de göründüğünden kötü\n"
         "ZOM-458: kazanmadan algo leveldan çıktım, dönüşte level change animasyonu oynadı ama olay animasyonda kalmıyor. "
         "level geçilmiş sayılmış, o levelın chesti claimed görünüyor, envantere hiçbir şey gelmedi. uygulamayı kapatıp "
         "açtım yine aynı, chest geri gelmiyor, level de ilerlemiş kalmış\n"
         "ZOM-535: 120 cpm'de match yapınca itemlar ölmüş zombieye gidiyor ya, boss arenada nuke de aynı şekilde ölmüş "
         "zombieye gitti, bossa sıfır hasar, nuke de boşa gitti, süre bitti. 3 denemede de boss arenayı bitiremedim, hep "
         "aynı yerde kalıyor", role="overturning", element="T16 how bad it is (older DM)")
    smsg(IDS["slack_dm_doug36"], SLK[DOUGLAS], "fyi #36 is rolled out to prod too, the container is up. that's the code side",
         role="claim met first", element="T2 done source (code rolled out)")


# ====================================================================== Gmail
def thread_id(iso, seed):
    return str((ep(iso) * 1000 << 20) + int(sha(seed, 6), 16) % 900000 + 1000)


def rfc_date(iso):
    return dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).strftime("%a, %d %b %Y %H:%M:%S +0000")


def mail(key, thrid, msgid, iso, frm, frm_name, to, cc, subject, body, labels, role="", element=""):
    tid = f"{VINCENT}/{thrid}"
    snippet = " ".join(body.split())[:140]
    ins("gmail.gmail_threads", {"id": q(tid), "user_email": q(VINCENT), "snippet": q(snippet), "history_id": "NULL"},
        {"id": tid, "service": "gmail", "container": f"gmail:{tid}", "role": role, "element": element, "at": iso,
         "author": frm})
    headers = [{"name": "X-GM-THRID", "value": thrid}, {"name": "Delivered-To", "value": VINCENT},
               {"name": "From", "value": f"{frm_name} <{frm}>"}, {"name": "To", "value": ", ".join(to)}]
    if cc:
        headers.append({"name": "Cc", "value": ", ".join(cc)})
    headers += [{"name": "Subject", "value": subject}, {"name": "Date", "value": rfc_date(iso)},
                {"name": "Message-ID", "value": msgid}]
    mid = f"{VINCENT}/{msgid}"
    ins("gmail.gmail_messages", {
        "id": q(mid), "thread_id": q(tid), "user_email": q(VINCENT), "label_ids_json": j(labels), "snippet": q(snippet),
        "history_id": "NULL", "internal_date": str(ep(iso) * 1000), "date": q(iso.replace("Z", "+00:00")),
        "size_estimate": str(len(body.encode()) + 900), "subject": q(subject), "from_email": q(frm),
        "from_name": q(frm_name), "to_json": j(to), "cc_json": j(cc), "bcc_json": "'[]'", "reply_to_json": "'[]'",
        "body_text": q(body), "body_html": "NULL", "headers_json": j(headers), "payload_json": "NULL",
        "in_reply_to": "NULL", "references": "NULL", "mbox_from": "NULL", "date_parsed_source": "NULL",
        "attachments_meta_json": "'[]'"},
        {"id": mid, "service": "gmail", "container": f"gmail:{tid}", "role": role, "element": element, "at": iso,
         "author": frm})
    return tid


def invite_copy(mailbox, iso, guests, body):
    thrid = thread_id(iso, "gmail|thread|gonogo-invite|" + mailbox)
    msgid = "<calendar-" + sha("gonogo-invite-uuid", 8) + "-" + sha("gonogo-invite-uuid2", 4) + "-4" + \
        sha("gonogo-invite-uuid3", 3) + "-8" + sha("gonogo-invite-uuid4", 3) + "-" + sha("gonogo-invite-uuid5", 12) + \
        "@google.com>"
    tid, mid = f"{mailbox}/{thrid}", f"{mailbox}/{msgid}"
    subject = "Invitation: ZM store push - go/no-go @ Fri Oct 3, 2025 9am - 9:30am (PDT) (" + mailbox + ")"
    snippet = " ".join(body.split())[:140]
    ins("gmail.gmail_threads", {"id": q(tid), "user_email": q(mailbox), "snippet": q(snippet), "history_id": "NULL"},
        {"id": tid, "service": "gmail", "container": f"gmail:{tid}", "role": "companion (INT-11)",
         "element": "K7 invite copy", "at": iso, "author": ARTHUR})
    headers = [{"name": "X-GM-THRID", "value": thrid}, {"name": "Delivered-To", "value": mailbox},
               {"name": "From", "value": f"{NAME[ARTHUR]} <{ARTHUR}>"},
               {"name": "To", "value": ", ".join(g for g in guests if g != ARTHUR)},
               {"name": "Subject", "value": subject}, {"name": "Date", "value": rfc_date(iso)},
               {"name": "Message-ID", "value": msgid}]
    ins("gmail.gmail_messages", {
        "id": q(mid), "thread_id": q(tid), "user_email": q(mailbox), "label_ids_json": j(["INBOX", "CATEGORY_PERSONAL"]),
        "snippet": q(snippet), "history_id": "NULL", "internal_date": str(ep(iso) * 1000),
        "date": q(iso.replace("Z", "+00:00")), "size_estimate": str(len(body.encode()) + 900), "subject": q(subject),
        "from_email": q(ARTHUR), "from_name": q(NAME[ARTHUR]), "to_json": j([g for g in guests if g != ARTHUR]),
        "cc_json": "'[]'", "bcc_json": "'[]'", "reply_to_json": "'[]'", "body_text": q(body), "body_html": "NULL",
        "headers_json": j(headers), "payload_json": "NULL", "in_reply_to": "NULL", "references": "NULL",
        "mbox_from": "NULL", "date_parsed_source": "NULL", "attachments_meta_json": "'[]'"},
        {"id": mid, "service": "gmail", "container": f"gmail:{tid}", "role": "companion (INT-11)",
         "element": "K7 invite copy", "at": iso, "author": ARTHUR})


GM = {m["key"]: m for m in MINTED["gmail"]}
H1_DECOY_AT = "2025-09-02T15:40:00Z"

MAILS = {
    "vendor": ("vendor_notes", "2025-09-30T22:40:00Z", VENDOR_EMAIL, [VINCENT], [],
               "Session notes - Sep 30 (Puzzles vs Zombies, TestFlight 50)",
               "Hi Vincent,\n\nNotes from today's two sessions on Puzzles vs Zombies (still the name on our test plan), "
               "TestFlight build 50 (iPhone 14 on "
               "iOS 18.6 and iPhone SE on iOS 17.5), 6 players, about 45 minutes each.\n\n1. Boss fight: for 3 of the 6 "
               "players, after the refill two or three single items dropped in with no matching items anywhere on the "
               "board. Nothing could clear them, the board never emptied and the boss timer ran out. Each of them lost "
               "a life and had to start the fight again.\n2. Zombie Lane: two players asked what the cards are for. Not "
               "a bug, just feedback.\n\nBest,\n" + VENDOR_NAME + "\nCobalt Playtesting",
               ["INBOX", "UNREAD", "CATEGORY_PERSONAL"], "evidence (alias)", "T5"),
}


def gmail():
    OUT.append("-- gmail: the playtest vendor's session notes (Vincent's copy)")
    tids = {}
    for k, (mk, iso, frm, to, cc, subj, body, labels, role, element) in MAILS.items():
        m = GM[mk]
        thrid = m["thread_id_num"] if iso == m["date"] else thread_id(iso, "gmail|thread|" + mk + "|" + iso)
        name = VENDOR_NAME if frm == VENDOR_EMAIL else NAME[frm]
        tids[k] = mail(k, thrid, m["message_id"], iso, frm, name, to, cc, subj, body, labels, role, element)
    # INT-11 companion of the seeded go/no-go event (Arthur's invite, Vincent's copy)
    iso = "2025-09-30T20:22:00Z"
    guests = [ARTHUR, LEONARD, VINCENT, BRIAN, ROBERT]
    body = ("ZM store push - go/no-go\nFriday Oct 3, 2025 9am - 9:30am (PDT)\n\nJoin with Google Meet\n"
            "https://meet.google.com/zmq-tbvx-kpr\n\nGo/no-go for the ZM store push (ZOM-570).\n\nOrganizer\n"
            f"{ARTHUR}\n\nGuests\n{ARTHUR} - organizer\n" + "\n".join(g for g in guests if g != ARTHUR))
    tids["invite"] = mail("invite", thread_id(iso, "gmail|thread|gonogo-invite"),
                          "<calendar-" + sha("gonogo-invite-uuid", 8) + "-" + sha("gonogo-invite-uuid2", 4) + "-4"
                          + sha("gonogo-invite-uuid3", 3) + "-8" + sha("gonogo-invite-uuid4", 3) + "-"
                          + sha("gonogo-invite-uuid5", 12) + "@google.com>", iso, ARTHUR, NAME[ARTHUR],
                          [g for g in guests if g != ARTHUR], [],
                          "Invitation: ZM store push - go/no-go @ Fri Oct 3, 2025 9am - 9:30am (PDT) (" + VINCENT + ")",
                          body, ["INBOX", "CATEGORY_PERSONAL"], "companion (INT-11)", "K7 invite")
    for who in (LEONARD, BRIAN, ROBERT):
        invite_copy(who, iso, guests, body)
    return tids


RULE_DOCS = [  # (ids key, owner, title, ISO created, parents, shared with, body, role, element)
    ("doc_h2", LEONARD, "ZM submission rules", "2025-09-23T09:10:00Z", "d_63fffeb4fab5233ed5bb73",
     [VINCENT, ARTHUR, BRIAN],
     "ZM submission rules\nLeonard, Sep 23\n\nAfter the orange juice one on Sunday I want the gate tighter, "
     "not just the Bug view in Linear.\n\nScope: every ZM ticket that's still open (any "
     "state but Done, Canceled or Duplicate), whatever team or label (ART or DES tickets with ZM in the title count too), plus everything that moved to Done after the "
     "last gate's builds were cut (Android #127 / iOS #40 on Sep 22). Release tickets, ZOM-359 and ZOM-475 stay out, that work is separate. From the next gate "
     "on, tickets filed while the gate is running get a row too, including the ones you file yourself.\n\n"
     "A ticket counts as fixed when Vincent or Brian saw it working on the candidate builds, or on prod if the fix is "
     "server side. A Done ticket for a bug nobody has re-checked yet also counts as fixed if its fix is actually in the candidate "
     "builds (or live on prod), noted as not re-checked. Done in Linear or a dev saying fixed isn't enough by itself, and "
     "if the latest check on the candidates still shows the bug, call it on how bad it is whatever the ticket says.\n\nBlocker = crash, freeze, player stuck or can't finish a level (like the orange "
     "juice one), lost progress / coins / lives (infinite-lives time included) / boosters / inventory items, or a purchase "
     "that doesn't deliver. Any other bug a player can see is a known issue, even if it doesn't change play, visual and "
     "sound glitches included. Art/VFX requests, requests for design, balance or tuning changes, analytics, tools, backend endpoints and new "
     "features aren't bugs, no call. The same goes for a ticket that only asks for new or updated art, animation, VFX, "
     "text style or UI layout (replacing an outdated model or icon with its new version included), even with a Bug label and even once it's "
     "Done, and for a ticket that doesn't say what goes wrong.\n\nBlockers go on the release ticket. If in doubt ask "
     "me before the go/no-go, not after.", "authority", "H2"),
    ("doc_h1", ARTHUR, "How ZM submission builds are cut", "2025-09-24T14:20:00Z", "d_cc3e90160f490686039986",
     [VINCENT, LEONARD],
     "How ZM submission builds are cut\nArthur, Sep 24\n\nSo nobody has to guess when gating:\n\n- Since the hotfix "
     "train ended on Sep 3, every store submission (the Match3D Android Submission and Match 3D iOS Submission jobs) is "
     "cut straight from main. The auth branch submission jobs are sign-in test builds, not store candidates.\n- A "
     "submission has exactly what was on main when its job started (the Started line in #builds) and nothing that "
     "landed after, even if the build finishes an hour later. Don't "
     "go by the Changes block either: the iOS posts only ever print the newest change, Android prints the whole list.\n- Backend is separate: match3d-backend changes reach "
     "players only when Douglas deploys the backend to prod, by hand (see the CI/CD page, CI stops at the build). "
     "Merged is not live.", "authority", "H1"),
    ("doc_h1_decoy", ARTHUR, "1.3.24 hotfix submissions", "2025-09-02T15:40:00Z", "d_cc3e90160f490686039986",
     [VINCENT],
     "1.3.24 hotfix submissions\nArthur, Sep 2\n\nThe 1.3.24 hotfix submissions this week are cut from "
     "release/1.3.24_HotFix, not main. Anything on main only goes in if we cherry-pick it onto the branch, so check "
     "the branch log before signing off on a hotfix build.", "decoy (older version)", "H1 decoy / T8"),
    ("doc_h2_decoy", LEONARD, "ZM beta drops - what blocks", "2025-07-27T17:00:00Z", "d_63fffeb4fab5233ed5bb73",
     [VINCENT, BRIAN],
     "ZM beta drops - what blocks\nLeonard, Jul 27\n\nFor the TestFlight beta drops (not store builds): only crashes "
     "and progress wipes block a drop. Everything else goes in as a known issue and we ship the beta anyway, testers "
     "expect rough edges.", "decoy (other lot)", "H2 decoy / T11"),
]


def rule_docs():
    OUT.append("-- drive / docs: Leonard's and Arthur's process docs (Jul 27, Sep 2, Sep 23, Sep 24), shared with Vincent")
    for key, owner, title, iso, parent, shared, body, role, element in RULE_DOCS:
        fid, ts = IDS[key], iso
        roles = {owner: "owner", **{s: "reader" for s in shared}}
        ins("gdrive.drive_files", {
            "id": q(fid), "name": q(title + ".docx"), "mime_type": "'application/vnd.google-apps.document'",
            "parents_json": j([parent]), "owner_email": q(owner), "shared_with_emails_json": j(shared),
            "shared_roles_json": j(roles), "visibility_role": "NULL", "visibility": "'private'",
            "owners_json": j([owner]), "modified_time": q(ts), "created_time": q(ts), "size": "NULL", "trashed": "false",
            "starred": "false", "content_path": "NULL", "web_view_link": "NULL", "icon_link": "NULL",
            "description": "NULL", "drive_id": "NULL", "content_text": "NULL"},
            {"id": fid, "service": "gdrive", "container": f"file:{fid}", "role": role + " (sharing)", "element": element,
             "at": iso, "author": owner})
        ins("gdocs.docs_documents", {
            "document_id": q(fid), "title": q(title), "owner_email": q(owner), "shared_with_emails_json": j(shared),
            "visibility": "'private'", "body_text": q(body),
            "style_runs_json": j([{"start": 0, "end": len(title), "named_style": "TITLE", "list_id": None,
                                   "list_nesting": 0}]),
            "revision_id": q(sha("rev|" + key, 12)), "drive_file_id": q(fid), "created_time": q(ts),
            "modified_time": q(ts)},
            {"id": fid, "service": "gdocs", "container": f"file:{fid}", "role": role, "element": element, "at": iso,
             "author": owner})


# ====================================================================== GCal
def gcal():
    OUT.append("-- gcal: go/no-go for the store push (one copy per attendee calendar)")
    g = MINTED["gcal"]
    start, end, created = "2025-10-03T16:00:00Z", "2025-10-03T16:30:00Z", "2025-09-30T20:22:00Z"
    people = [ARTHUR, LEONARD, VINCENT, BRIAN, ROBERT]
    for c in g["copies"]:
        cal = c["calendar_id"]
        att = []
        for p in people:
            a = {"email": p, "organizer": p == ARTHUR, "responseStatus": "accepted" if p == ARTHUR else "needsAction"}
            if p == cal:
                a["self"] = True
            att.append(a)
        ins("gcal.gcal_events", {
            "event_id": q(c["event_id"]), "calendar_id": q(cal), "summary": q("ZM store push - go/no-go"),
            "description": q("Go/no-go for the ZM store push (ZOM-570)."), "location": "NULL", "start_ts": q(start),
            "end_ts": q(end), "start_json": j({"dateTime": "2025-10-03T16:00:00Z"}),
            "end_json": j({"dateTime": "2025-10-03T16:30:00Z"}), "organizer_email": q(ARTHUR),
            "creator_email": q(ARTHUR), "attendees_json": j(att), "status": "'confirmed'", "visibility": "NULL",
            "transparency": "'opaque'", "rrule_json": "'[]'", "recurring_event_id": "NULL",
            "original_start_json": "NULL", "sequence": "0", "created": q(created), "updated": q(created),
            "hangout_link": q("https://meet.google.com/zmq-tbvx-kpr"), "ical_uid": q(g["ical_uid"]),
            "extras_json": "NULL"},
            {"id": c["event_id"], "service": "gcal", "container": f"gcal:{g['ical_uid']}",
             "role": "deadline" if cal == VINCENT else "companion copy", "element": "K7", "at": "2025-09-30T20:22:00Z",
             "author": ARTHUR})


# ====================================================================== Drive / Sheets / Docs
GATE_HOW = [["How we gate (ZM store submissions) - from the next gate on, updated Sep 23 after Leonard's rules"],
            ["One tab per gate, named after the candidate builds. One row per ticket."],
            [""],
            ["Columns", "ticket", "title", "build status", "QA result", "call", "evidence"],
            ["call", "BLOCKER", "KNOWN ISSUE", "FIXED", "NO CALL"],
            ["build status", "in candidate", "not in candidate", "server - live", "server - not live", "n/a"],
            ["build status means (a server-side fix always takes a server value)",
             "a bug QA re-tested on the candidates and saw working or couldn't reproduce, or a Done bug whose fix was on main at the job's Started line, even if the re-test still shows the bug (if nothing shows when the fix landed, go by when the ticket was closed)",
             "a Done bug whose fix landed after the Started line",
             "a server-side fix that's fully on prod, including any migration or data it needs",
             "a server-side fix with any part not on prod yet, even if its code is deployed",
             "everything else: open bugs that still show up or nobody re-tested, no-call tickets"],
            ["evidence", "id or link of the record that decides the row"]]
GATE_SEP22_ROWS = [("ZOM-546", "n/a", "repro on #127", "BLOCKER", "ZOM-546"),
                   ("ZOM-559", "n/a", "not reproduced on #127 (Pixel)", "KNOWN ISSUE", "ZOM-559"),
                   ("ZOM-534", "n/a", "seen on prod", "KNOWN ISSUE", "ZOM-534"),
                   ("ZOM-520", "n/a", "repro on #127", "KNOWN ISSUE", "ZOM-520"),
                   ("ZOM-535", "n/a", "repro on #127", "KNOWN ISSUE", "ZOM-535"),
                   ("ZOM-517", "n/a", "repro on #127", "KNOWN ISSUE", "ZOM-517"),
                   ("ZOM-429", "n/a", "repro on #40", "KNOWN ISSUE", "ZOM-429"),
                   ("ZOM-503", "in candidate", "pass on #127", "FIXED", "match3d#422")]
GATE_SEP22 = [["ticket", "title", "build status", "QA result", "call", "evidence"]] + [
    [k, ZOM[k]["title"], b, r, c, ev] for k, b, r, c, ev in GATE_SEP22_ROWS]

MATRIX = [["Area", "Fresh install - iOS #50 (iPhone 13)", "Fresh install - Android #135 (Pixel 6)", "Update from N-1",
           "Update from N-2", "Notes"],
          ["Splash / asset load", "Pass", "Pass", "", "", "throttled 3G + cleared cache"],
          ["Save / progression", "Pass", "Pass", "", "", ""],
          ["Lives & scheduler", "Pass", "Pass", "", "", "clock moved +3h, lives refilled"],
          ["Quests populate / reset", "Pass", "Pass", "", "", ""],
          ["Purchase / restore", "Pass", "Pass", "", "", "sandbox, grants checked client side"]]

UPDATE_LOG_BODY = (
    "Update-path run - iOS #50 / Android #135\n"
    "Brian Foster, Sep 30 2025 (after the fresh-install pass)\n\n"
    "Update rows from the QA regression runbook. Fresh-install rows are in my regression matrix sheet.\n\n"
    "Device | OS | Installed from store | Updated to | Result | Notes\n"
    "iPhone 13 | iOS 18.6 | N-1 | iOS Submission #50 | FAIL | After the update the save "
    "came back at level 1 with 500 coins; the account was on level 212 with 18,400 coins before. Relaunching didn't "
    "bring it back.\n"
    "iPhone 13 | iOS 18.6 | N-2 | iOS Submission #50 | Pass | Level, coins and unlocks "
    "kept.\n"
    "Pixel 6 | Android 14 | N-1 | Android Submission #135 | Pass | Level, coins and "
    "unlocks kept.\n"
    "Pixel 6 | Android 14 | N-2 | Android Submission #135 | Pass | Level, coins and "
    "unlocks kept.\n\n"
    "Repro for the iOS row: install the N-1 build from the App Store, play past level 200, install TestFlight 50 over it, "
    "launch.")


def drive():
    OUT.append("-- drive / sheets / docs: Vincent's release sheet, Brian's regression matrix and update-path test log")
    sheet, log = IDS["gate_sheet"], IDS["update_log"]
    ins("gdrive.drive_files", {
        "id": q(sheet), "name": q("ZM3D Release Gate.xlsx"), "mime_type": "'application/vnd.google-apps.spreadsheet'",
        "parents_json": j(["d_65c76e0b87aa7e9b84d1df"]), "owner_email": q(VINCENT), "shared_with_emails_json": "'[]'",
        "shared_roles_json": j({VINCENT: "owner"}), "visibility_role": "NULL", "visibility": "'private'",
        "owners_json": j([VINCENT]), "modified_time": q("2025-09-23T10:05:00Z"),
        "created_time": q("2025-09-22T17:05:00Z"), "size": "NULL", "trashed": "false", "starred": "false",
        "content_path": "NULL", "web_view_link": "NULL", "icon_link": "NULL", "description": "NULL", "drive_id": "NULL",
        "content_text": "NULL"},
        {"id": sheet, "service": "gdrive", "container": f"file:{sheet}", "role": "write target", "element": "A3",
         "at": "2025-09-22T17:05:00Z", "author": VINCENT})
    ins("gsheets.sheets_spreadsheets", {
        "spreadsheet_id": q(sheet), "title": q("ZM3D Release Gate"), "owner_email": q(VINCENT),
        "shared_with_emails_json": "'[]'", "visibility": "'private'", "drive_file_id": q(sheet),
        "created_time": q("2025-09-22T17:05:00Z"), "modified_time": q("2025-09-23T10:05:00Z")},
        {"id": sheet, "service": "gsheets", "container": f"file:{sheet}", "role": "write target / format",
         "element": "A3 / K6", "at": "2025-09-22T17:05:00Z", "author": VINCENT})
    for idx, (title, grid) in enumerate([("How we gate", GATE_HOW), ("Sep 22 - Android #127 / iOS #40", GATE_SEP22)]):
        ins("gsheets.sheets_sheets", {
            "spreadsheet_id": q(sheet), "sheet_id": str(idx), "title": q(title), "index": str(idx),
            "row_count": str(max(len(grid), 20)), "column_count": str(max(len(r) for r in grid)), "grid_json": j(grid)},
            {"id": f"{sheet}#{idx}", "service": "gsheets", "container": f"file:{sheet}",
             "role": "format" if idx == 0 else "decoy (older version)", "element": "K6" if idx == 0 else "T12 / T6",
             "at": "2025-09-22T17:05:00Z", "author": VINCENT})
    mx = IDS["matrix_sheet"]
    ins("gdrive.drive_files", {
        "id": q(mx), "name": q("Regression matrix - Android #135 / iOS #50.xlsx"),
        "mime_type": "'application/vnd.google-apps.spreadsheet'", "parents_json": j(["d_fc22d5941b2aeb5c03ad32"]),
        "owner_email": q(BRIAN), "shared_with_emails_json": j([VINCENT]),
        "shared_roles_json": j({BRIAN: "owner", VINCENT: "reader"}), "visibility_role": "NULL",
        "visibility": "'private'", "owners_json": j([BRIAN]), "modified_time": q("2025-09-30T21:05:00Z"),
        "created_time": q("2025-09-30T20:35:00Z"), "size": "NULL", "trashed": "false", "starred": "false",
        "content_path": "NULL", "web_view_link": "NULL", "icon_link": "NULL", "description": "NULL", "drive_id": "NULL",
        "content_text": "NULL"},
        {"id": mx, "service": "gdrive", "container": f"file:{mx}", "role": "evidence (sharing)", "element": "T4 / T10",
         "at": "2025-09-30T20:35:00Z", "author": BRIAN})
    ins("gsheets.sheets_spreadsheets", {
        "spreadsheet_id": q(mx), "title": q("Regression matrix - Android #135 / iOS #50"), "owner_email": q(BRIAN),
        "shared_with_emails_json": j([VINCENT]), "visibility": "'private'", "drive_file_id": q(mx),
        "created_time": q("2025-09-30T20:35:00Z"), "modified_time": q("2025-09-30T21:05:00Z")},
        {"id": mx, "service": "gsheets", "container": f"file:{mx}", "role": "evidence", "element": "T4 / T10",
         "at": "2025-09-30T20:35:00Z", "author": BRIAN})
    ins("gsheets.sheets_sheets", {
        "spreadsheet_id": q(mx), "sheet_id": "0", "title": q("Matrix"), "index": "0", "row_count": "20",
        "column_count": "6", "grid_json": j(MATRIX)},
        {"id": f"{mx}#0", "service": "gsheets", "container": f"file:{mx}", "role": "evidence (fresh rows only)",
         "element": "T4 / T10", "at": "2025-09-30T20:35:00Z", "author": BRIAN})
    ins("gdrive.drive_files", {
        "id": q(log), "name": q("Update-path run - iOS #50 / Android #135.docx"),
        "mime_type": "'application/vnd.google-apps.document'", "parents_json": j(["d_fc22d5941b2aeb5c03ad32"]),
        "owner_email": q(BRIAN), "shared_with_emails_json": j([VINCENT]),
        "shared_roles_json": j({BRIAN: "owner", VINCENT: "reader"}), "visibility_role": "NULL",
        "visibility": "'private'", "owners_json": j([BRIAN]), "modified_time": q("2025-09-30T22:35:00Z"),
        "created_time": q("2025-09-30T22:05:00Z"), "size": "NULL", "trashed": "false", "starred": "false",
        "content_path": "NULL", "web_view_link": "NULL", "icon_link": "NULL", "description": "NULL", "drive_id": "NULL",
        "content_text": "NULL"},
        {"id": log, "service": "gdrive", "container": f"file:{log}", "role": "evidence (sharing)", "element": "T4",
         "at": "2025-09-30T22:05:00Z", "author": BRIAN})
    title_end = UPDATE_LOG_BODY.index("\n")
    ins("gdocs.docs_documents", {
        "document_id": q(log), "title": q("Update-path run - iOS #50 / Android #135"), "owner_email": q(BRIAN),
        "shared_with_emails_json": j([VINCENT]), "visibility": "'private'", "body_text": q(UPDATE_LOG_BODY),
        "style_runs_json": j([{"start": 0, "end": title_end, "named_style": "TITLE", "list_id": None, "list_nesting": 0}]),
        "revision_id": q(sha("update-log-rev", 12)), "drive_file_id": q(log),
        "created_time": q("2025-09-30T22:05:00Z"), "modified_time": q("2025-09-30T22:35:00Z")},
        {"id": log, "service": "gdocs", "container": f"file:{log}", "role": "overturning evidence", "element": "T4 / CH3",
         "at": "2025-09-30T22:05:00Z", "author": BRIAN})


# ====================================================================== Trello
CARD = "68d1eb90bef538c7c5c5599d"


def trello():
    OUT.append("-- trello: comments on the ZM ROADMAP 'Fix TECH ISSUES' card")
    acts = {a["who"]: a for a in MINTED["trello_actions"]}
    texts = {
        "arthur": ("store push: anything that blocks goes on ZOM-570 under the ticket that already exists, no duplicate "
                   "tickets. only open a new one if nobody filed it yet", ARTHUR, "reuse rule", "K8"),
        "leonard": ("trophy path on android #135: tapped claim twice fast and got stuck on the path again, only killing "
                    "the app got me out. same as ZOM-435", LEONARD, "overturning", "T3 re-test"),
    }
    for who in ("arthur", "leonard"):
        a = acts[who]
        text, person, role, element = texts[who]
        data = {"board": {"id": "6851a6569f3bf818760632ab", "name": "ZM ROADMAP", "shortLink": "HSqnngwQ"},
                "card": {"id": CARD, "idShort": 79, "name": "Fix TECH ISSUES", "shortLink": "pTbZYXdb"},
                "idCard": CARD, "list": {"id": "6851a674975da1fe76e70d93", "name": "BETA: Sep 30"}, "text": text,
                "textData": {"emoji": {}}}
        ins("trello.trello_actions", {
            "id": q(a["action_id"]), "type": "'commentCard'", "date": q(a["date"]), "idMemberCreator": q(TRELLO[person]),
            "idBoard": "'6851a6569f3bf818760632ab'", "idCard": q(CARD), "data_json": j(data)},
            {"id": a["action_id"], "service": "trello", "container": f"trello:{CARD}", "role": role, "element": element,
             "at": a["date"], "author": person})
    badges = {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0,
              "checkItemsChecked": 0, "checkItemsEarliestDue": None, "comments": 2, "description": False, "due": None,
              "dueComplete": False, "externalSource": None, "fogbugz": "", "lastUpdatedByAi": False, "location": False,
              "maliciousAttachments": 0, "start": None, "votes": 0}
    upd("trello.trello_cards", {"badges_json": j(badges), "dateLastActivity": q(acts["leonard"]["date"])},
        f"id = {q(CARD)}", {"id": CARD, "service": "trello", "container": f"trello:{CARD}", "role": "companion",
                            "element": "badges + dateLastActivity follow the comments", "at": acts["leonard"]["date"]})
    upd("trello.trello_boards", {"dateLastActivity": q(acts["leonard"]["date"])}, "id = '6851a6569f3bf818760632ab'",
        {"id": "6851a6569f3bf818760632ab", "service": "trello", "container": "trello:6851a6569f3bf818760632ab",
         "role": "companion", "element": "board dateLastActivity follows the newest action", "at": acts["leonard"]["date"]})


# ====================================================================== Contacts
def contacts():
    OUT.append("-- contacts: the playtest vendor's QA lead")
    cid = MINTED["contacts"][0]["contact_id"]
    ins("contacts.contacts", {
        "contact_id": q(cid), "first_name": q(VENDOR_NAME), "last_name": "''", "is_user": "false",
        "gender": "'Unknown'", "status": "'Unknown'", "job": q("QA Lead, Cobalt Playtesting (ZM3D playtests)"),
        "description": "NULL", "email": q(VENDOR_EMAIL), "created_at": q("2025-08-18T10:00:00Z"),
        "updated_at": q("2025-08-18T10:00:00Z")},
        {"id": cid, "service": "contacts", "container": f"contacts:{cid}", "role": "identity (alias)", "element": "T5",
         "at": "2025-08-18T10:00:00Z", "author": VINCENT})


# ====================================================================== GitHub
PR = "harmonygames-Games/match3d-backend#36"


def github():
    OUT.append("-- github: match3d-backend#36 (Zombie Lane chest grant), Arthur's approval and the merge")
    head = sha("match3d-backend#36 head", 40)
    ins("github.github_commits", {
        "sha": q(head), "repo_id": "'harmonygames-Games/match3d-backend'",
        "message": q("Fix Zombie Lane chest grant after the daily reset"), "authored_date": "'2025-09-30T18:24:00Z'",
        "committed_date": "NULL", "author_login": q(GH[DOUGLAS]), "author_name": "'PERSON_5760_NAME'",
        "author_email": "'PERSON_5760_EMAIL'", "committer_login": q(GH[DOUGLAS]), "committer_name": "'PERSON_5760_NAME'",
        "committer_email": "'PERSON_5760_EMAIL'", "parent_shas_json": "'[]'"},
        {"id": head, "service": "github", "container": f"github:{PR}", "role": "companion",
         "element": "head commit of harmonygames-Games/match3d-backend#36", "at": "2025-09-30T18:24:00Z", "author": DOUGLAS})
    ins("github.github_pull_requests", {
        "id": q(PR), "repo_id": "'harmonygames-Games/match3d-backend'", "number": "36",
        "title": q("Fix Zombie Lane chest grant after the daily reset"), "state": "'closed'", "merged": "true",
        "draft": "false", "locked": "false", "author_login": q(GH[DOUGLAS]),
        "merged_by_login": q(GH[DOUGLAS]),
        "body": q("Chest claims were acknowledged but the grant job skipped them when the claim landed after the daily "
                  "reset. ZOM-567"),
        "base_ref": "'main'", "head_ref": "'zombie-lane-chest-grant'",
        "base_sha": "'a0e4a218082ccfd2d20486fed1dba5772183e0d4'", "head_sha": q(head),
        "merge_commit_sha": "NULL", "additions": "34", "deletions": "9", "changed_files": "3", "labels_json": "NULL",
        "assignee_logins_json": "NULL", "requested_reviewer_logins_json": "NULL", "created_at": "'2025-09-30T18:30:00Z'",
        "updated_at": "'2025-09-30T22:40:00Z'", "merged_at": "'2025-09-30T18:50:00Z'",
        "closed_at": "'2025-09-30T18:50:00Z'", "html_url": "NULL"},
        {"id": PR, "service": "github", "container": f"github:{PR}", "role": "claim met first", "element": "T2",
         "at": "2025-09-30T18:30:00Z", "author": DOUGLAS})
    ins("github.github_pull_request_commits", {"id": q(f"{PR}#c_0"), "pr_id": q(PR), "commit_sha": q(head), "position": "0"},
        {"id": f"{PR}#c_0", "service": "github", "container": f"github:{PR}", "role": "companion",
         "element": "commit list of #36", "at": "2025-09-30T18:30:00Z", "author": DOUGLAS})
    ins("github.github_reviews", {
        "id": q(IDS["review36"]), "pr_id": q(PR), "author_login": q(GH[ARTHUR]), "state": "'APPROVED'",
        "body": "''", "submitted_at": "'2025-09-30T18:42:00Z'", "commit_id": "NULL", "seq": "1"},
        {"id": IDS["review36"], "service": "github", "container": f"github:{PR}", "role": "claim met first",
         "element": "T2 approval", "at": "2025-09-30T18:42:00Z", "author": ARTHUR})
    ins("github.github_reviews", {
        "id": q(IDS["review36_post"]), "pr_id": q(PR), "author_login": q(GH[ARTHUR]), "state": "'COMMENTED'",
        "body": "''", "submitted_at": "'2025-09-30T22:40:00Z'", "commit_id": q(head), "seq": "2"},
        {"id": IDS["review36_post"], "service": "github", "container": f"github:{PR}", "role": "companion",
         "element": "review container of the inline comment", "at": "2025-09-30T22:40:00Z", "author": ARTHUR})
    ins("github.github_review_comments", {
        "id": q(IDS["review36_inline"]), "pr_id": q(PR), "author_login": q(GH[ARTHUR]),
        "body": q("checked prod after Douglas rolled this out: claimed a chest on my prod account and nothing landed. the "
                  "migration only creates the empty zombie_lane_chest_rows table, the rows the grant reads come from this "
                  "load, which runs by hand per environment and hasn't been run on prod. so the new grant path does nothing "
                  "on prod yet. I'm holding the prod load until after the store push"),
        "path": "'priv/repo/data/load_zombie_lane_chest_rows.exs'",
        "diff_hunk": q("@@ -0,0 +1,14 @@\n+# Loads the chest rows the Zombie Lane grant reads. Run by hand per environment:\n"
                       "+#   bin/zombies_game eval 'Code.eval_file(\"priv/repo/data/load_zombie_lane_chest_rows.exs\")'"),
        "line": "2", "position": "NULL", "commit_id": q(head), "in_reply_to_id": "NULL",
        "created_at": "'2025-09-30T22:35:00Z'", "seq": "1"},
        {"id": IDS["review36_inline"], "service": "github", "container": f"github:{PR}", "role": "overturning",
         "element": "T2 missing piece (chest rows not loaded on prod)", "at": "2025-09-30T22:35:00Z", "author": ARTHUR})
    GH["coderabbit"] = "SVC_0321_GITHUB_USERNAME"
    events = [("review_requested", DOUGLAS, "2025-09-30T18:30:00Z",
               {"requested_reviewer": {"github_id": "EMPLOYEE_0025_GITHUB_ID", "login": GH[ARTHUR],
                                       "node_id": "EMPLOYEE_0025_GITHUB_NODE_ID", "type": "User"}}),
              ("commented", "coderabbit", "2025-09-30T18:30:06Z", {}),
              ("reviewed", ARTHUR, "2025-09-30T18:42:00Z", {"state": "approved"}),
              ("merged", DOUGLAS, "2025-09-30T18:50:00Z", {}),
              ("closed", DOUGLAS, "2025-09-30T18:50:00Z", {}),
              ("reviewed", ARTHUR, "2025-09-30T22:40:00Z", {"state": "commented"})]
    for n, (ev, who, at, data) in enumerate(events, 1):
        eid = f"{PR}#ev_{n}"
        ins("github.github_timeline_events", {"id": q(eid), "pr_id": q(PR), "event": q(ev), "actor_login": q(GH[who]),
                                              "created_at": q(at), "data_json": j(data)},
            {"id": eid, "service": "github", "container": f"github:{PR}", "role": "companion",
             "element": f"timeline {ev}", "at": at, "author": who})
    upd("github.github_repositories", {"updated_at": "'2025-09-30T18:50:00Z'", "pushed_at": "'2025-09-30T18:50:00Z'"},
        "id = 'harmonygames-Games/match3d-backend'",
        {"id": "harmonygames-Games/match3d-backend", "service": "github", "container": "github:harmonygames-Games/match3d-backend",
         "role": "companion", "element": "repo push stamp follows the harmonygames-Games/match3d-backend#36 merge", "at": "2025-09-30T18:50:00Z"})


def main():
    head = ["-- Are you planning to inject? Yes", "",
            "-- HarmonyGames injection - Vincent Parker (vincent.parker@harmonygames.co), Game Systems Engineer - "
            "Long Horizon - synth-cut, freeze 2025-10-01T00:00:00Z",
            "-- Services: linear, slack, gmail, gcal, gdrive, gsheets, gdocs, trello, contacts, github",
            "-- Literal values only; parents before children.", ""]
    linear(); OUT.append("")
    slack(); OUT.append("")
    gmail(); OUT.append("")
    gcal(); OUT.append("")
    rule_docs(); OUT.append("")
    drive(); OUT.append("")
    trello(); OUT.append("")
    contacts(); OUT.append("")
    github()
    sql = "\n".join(head + OUT) + "\n"
    (TASK / "01_Universe_Inject.sql").write_text(sql)
    (HERE / "records.json").write_text(json.dumps(LEDGER, indent=1, ensure_ascii=False) + "\n")
    n_ins = sum(1 for s in OUT if s.startswith("INSERT")); n_upd = sum(1 for s in OUT if s.startswith("UPDATE"))
    print(f"SQL written: {n_ins} inserts, {n_upd} updates, {len(LEDGER)} ledger rows")


if __name__ == "__main__":
    main()
