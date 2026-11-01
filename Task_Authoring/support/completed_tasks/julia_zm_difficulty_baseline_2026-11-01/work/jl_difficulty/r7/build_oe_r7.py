"""Round 7: writes task_inputs/08_Oracle_Events.md from the current SQL (b64bc2f2c6dc) and r7/truth7.py.
Every quoted text is read from the SQL row, so it cannot drift. Run from Task_Authoring-2.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sqlrows import load, load_all  # noqa: E402
import truth7 as T  # noqa: E402

SQL = 'task_inputs/01_Universe_Inject.sql'
R = load(SQL)
ALL = load_all(SQL)
one = lambda x: ' '.join(str(x).replace('\\n', ' ').split())
txt = lambda i: one(R[i]['text'])
M = json.load(open(os.path.join(HERE, '..', 'minted_ids.json')))
N = M['LIN_NOTES']
note = lambda k: one(N[k]['text'])
CARD = one(R['68daca5871dba40417a00383']['desc'])
CMT = one(json.loads(R['68dbfa4362a051efb5e0ae45']['data_json'])['text'])
docs = {r['document_id']: r for r in ALL if r['table'] == 'gdocs.docs_documents'}
DOC_NOTES = one(docs['f_f494073fc667097c3c2c6b'].get('body_text') or docs['f_f494073fc667097c3c2c6b'].get('content'))
DOC_AGENDA = one(docs['f_9ec79682ff351aa466364a'].get('body_text') or docs['f_9ec79682ff351aa466364a'].get('content'))
M1 = one(R['julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>']['body_text'])
M2 = one(R['julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>']['body_text'])
DECK = ' '.join(one(r['text']) for r in ALL if r['table'] == 'gslides.slides_page_elements')
RC265 = one(R['harmonygames-Games/match3d#265#rc_7']['body'])
RC271 = one(R['harmonygames-Games/match3d#271#rc_1']['body'])
C401 = one(R['harmonygames-Games/match3d#401#c_2']['body'])
P = json.load(open(os.path.join(HERE, '..', 'planned_text.json')))
LIVE_TAB = "; ".join(f"{r[0]}: speed {r[1]}, damage {r[2]}, hp {r[3]}" for r in P['SHEET_KNOBS_TABS']['Live'][1:])
EO, NS = ', '.join(T.EO), ', '.join(T.NS)

E = []
ev = lambda a, x: E.append((a, x))

# ---------------------------------------------------------------- discovery
ev("Read Julia's DM with Leonard, newest messages before the clock (Slack: open the direct message with Leonard and read its history)",
   f"Leonard, Tue Sep 30 2025 19:48 UTC (12:48 PM PT): \"{txt('6f77386571537f0bd88c959bdc216f94')}\" The message has 1 reply in its thread. "
   f"The message just before it in the DM, Julia's own message of Mon Sep 29 2025 21:38 UTC, \"{txt('914b21ab6448fac2e4b4f8d164bea41a')}\", also has 1 reply in its thread.")
ev("Open the thread under Leonard's Sep 30 ask (Slack: replies to the ask's message in the DM)",
   f"Leonard, Tue Sep 30 2025 20:07 UTC: \"{txt('33c941fae57ba8d1e23bc1dff9ce3e2c')}\" So ZOM-30, 49, 50, 161, 262 and 275 stay off the register, "
   "the reply to Leonard must list the Not shipped and Editor only keys, and the comments on the Editor only and Not shipped tickets name iOS 0.3.49 and Android 0.3.133.")
ev("Open the thread under Julia's Sep 29 question in the same DM (Slack: replies to that message)",
   f"Leonard, Tue Sep 30 2025 21:16 UTC, the latest instruction before the clock: \"{txt('5f6ed4d5ae1a0a04b616af6d6d2dda43')}\" So ZOM-162, 163, 201 and 250 "
   "also stay off the register and get no ticket comment, and Brian gets comment access, not edit.")
ev("Find the rules card the ask names on the ZM roadmap board (Trello: search \"Difficulty baseline\", open the card on the ZM roadmap board)",
   f"Card \"Difficulty baseline (Julia)\", created Mon Sep 29 2025 18:05 UTC, description last edited Tue Sep 30 2025 14:04 UTC: \"{CARD}\" "
   "The card shows 1 comment, a checklist with 2 items and 1 attachment. Trap: the \"Difficulty baseline\" card on the Domino Delights board "
   "(created Jun 2 2025) is for another game and does not apply.")
ev("Read the comment on the rules card (Trello: the card's comment actions)",
   f"Leonard, Tue Sep 30 2025 15:41 UTC: \"{CMT}\" So titles with \"attack power\" written out join the scope (ZOM-246, 250, 263, "
   "277, 315); ZOM-271, whose title says only \"ATK POWER\", does not.")
ev("Read the card's checklist (Trello: the card's checklists)",
   "Checklist \"Before Monday\", added Tue Sep 30 2025 16:20 UTC, items: \"rule 6 change: the Editor only and Not shipped tickets get a comment "
   "too, saying the change isn't in the store builds\" and \"rule 7 change: Brian gets edit as well, he'll fix rows during the session\". The "
   "first item stands; the second is taken back by Leonard's later DM reply of Sep 30 21:16 UTC (OE 3), so Brian comments.")
ev("Open the card's attachment, Leonard's \"notes for monday\" doc (Trello: the card's attachments, then read the Google Doc it links)",
   f"Doc \"notes for monday\", created Tue Sep 30 2025 15:47 UTC by Leonard, shared with Julia: \"{DOC_NOTES}\" So ZOM-258 stays "
   "off, Arthur gets view access, and the reply names which ticket replaced which. These three things are Leonard's own list, separate from the columns Robert asks for.")
ev("Find the group chat the card's rule 2 names, Julia's group DM with Robert and Leonard, and read its history before the clock (Slack: list Julia's group DMs, open the one with Robert and Leonard)",
   f"Leonard, Tue Sep 30 2025 10:01 UTC: \"{txt('cec246a6e43158f200fe144f0dd7039c')}\" The message has 1 reply in its thread.")
ev("Open the thread under Leonard's question in the group chat (Slack: replies to that message)",
   f"Robert, Tue Sep 30 2025 10:51 UTC: \"{txt('abe096ff0b5d7216efbc889e91d6d13a')}\" So the Tickets tab carries three more columns after status: "
   "the Linear assignee, the day the ticket was marked done in Pacific time (blank when it never got done), and the Linear priority.")
ev("Read Blake's store builds mail in Julia's mailbox (Gmail: search \"store builds\", open the thread \"store builds for monday\")",
   f"Arthur Blake to Leonard, Julia, Robert and Brian, Tue Sep 30 2025 09:12 UTC, the only message in its thread: \"{M1}\" So the store builds "
   "are iOS 0.3.49 and Android 0.3.133, cut from main on Sep 26.")
ev("Find Blake's reply to that mail, which rule 3 and rule 6 name; it sits in its own thread (Gmail: search mail from arthur.blake@harmonygames.co, open \"editor stuff and ZOM-199, before Monday\")",
   f"Arthur Blake to the same four, Tue Sep 30 2025 13:26 UTC: \"{M2}\" So level editor, Editor-folder and debug-menu changes are Editor only, "
   "and ZOM-199's text is wrong (rule 6 comment): the build checks cpm > 90 when the 10th game ends.")
ev("Read the session agenda the card's rule 2 points to (Drive search \"ZM difficulty tuning\", read the Google Doc)",
   f"Doc \"ZM difficulty tuning - Oct 6\", created Mon Sep 29 2025 18:31 UTC: \"{DOC_AGENDA}\" So the register is one "
   "spreadsheet with two tabs, Tickets and Rules in force.")
ev("Read Monday's tuning invite on Julia's calendar (Calendar: search \"ZM difficulty tuning\")",
   "Event \"ZM difficulty tuning\", organizer Leonard, starts Mon Oct 6 2025 17:00 UTC (a future meeting). Attendees: "
   "leonard.hayes@harmonygames.co, julia.lawson@harmonygames.co, robert@harmonygames.co, arthur.blake@harmonygames.co, "
   "brian.foster@harmonygames.co. So the shares go to Robert, Leonard, Arthur and Brian.")
ev("Find the ZM Difficulty folder (Drive: search \"ZM Difficulty\")",
   "Folder \"ZM Difficulty\", created Jun 13 2025; Julia can write to it. It holds her \"ZM monster enrage\" spreadsheet.")
ev("Read the Live tab of Julia's monster enrage sheet (Sheets: spreadsheet \"ZM monster enrage\", tab Live)",
   f"Columns monster (VarC prefab), enrage speed, enrage damage, enrage hp. Rows: {LIVE_TAB}. The \"Next pass\" tab is Leonard's proposal "
   "(0.3 / 0.8 by level band), not what is live.")
ev("Read Blake's note on Robert's tiers deck in #zombie-design (Slack: search \"blunder part\")",
   f"Blake, Wed Sep 3 2025 15:22 UTC: \"{txt('6995ba10acf2888f04f033b8bbeb5629')}\" So enrage is per monster, speed and damage only, no hp.")
ev("Read ZOM-42, the tier spec (Linear: search \"Dynamic Difficulty\" in team ZOM, open ZOM-42)",
   "ZOM-42 \"Dynamic Difficulty\", Done. Starting tier: \"1st 10 level avg CPM > 90 (top 20%) moves to tier 1, rest stays in tier 0\". "
   "Promotion: \"Tier -2 is an exception. You promote instantly after 1 win if you're in tier -2\"; \"we evaluate UP TO THE MOST RECENT 10 "
   "attempts\"; \"We promote if if win rate is 80% or higher\". Demotion: \"Lose 4 in a row, you're demoted\"; \"we demote someone when their "
   "win rate for up to the last 10 games is 50% or lower\"; \"every time a promotion/demotion happens, the record is reset and we start at 0 games played\".")
ev("Read the starting-tier code in the match3d repo (GitHub: file contents of Assets/Scripts/DynamicDifficulty/TierManager.cs and Assets/Scripts/Player/WinHistory.cs)",
   "TierManager.cs: \"var totalGames = WinHistory.GetTotalGames(); if (totalGames == 10)\" applies the initial bucketing, which sets tier 1 "
   "\"when cpm > 90.0f\" and tier 0 otherwise. WinHistory.cs: \"GetTotalGames() { return GetTotalWins() + GetTotalLosses(); }\". So a new "
   "player gets the starting tier when their 10th game ends, wins and losses both counting (not at level 10), and 90 exactly stays on tier 0. "
   "Rule 5 says the build governs this timing.")
ev("Read Robert's dynamic difficulty deck that rule 5 names (Drive search \"dynamic difficulty\", read the Slides deck \"ZM dynamic difficulty - how tiers work\")",
   f"Deck text: \"{DECK}\" Out of date in the deck: \"90 or more\", because Blake's reply (OE 11) says the build checks "
   "cpm > 90, so 90 exactly stays on tier 0; \"first 10 levels\", because the build (OE 18) sets the tier when the player's 10th game ends, "
   "wins and losses both counting; and the blunder line, because Blake's #zombie-design note (OE 16) says enrage adds speed and damage only, "
   "hp doesn't change, and the values are per monster. For promotion and demotion, rule 5 says to write them the way ZOM-42 words them (OE 17).")
TM = ("ZOM-23, ZOM-30, ZOM-42, ZOM-45, ZOM-49, ZOM-50, ZOM-161, ZOM-162, ZOM-163, ZOM-173, ZOM-199, ZOM-200, ZOM-201, ZOM-202, ZOM-246, "
      "ZOM-250, ZOM-254, ZOM-258, ZOM-262, ZOM-263, ZOM-274, ZOM-275, ZOM-277, ZOM-280, ZOM-282, ZOM-288, ZOM-293, ZOM-295, ZOM-303, ZOM-312, ZOM-315")
ev("List every team ZOM issue created up to Aug 31 2025 and match titles against rule 1's words plus \"attack power\" (Linear: list issues of team ZOM, paging to the end)",
   f"31 title matches that are not in the Duplicate state: {TM}. ZOM-203 and ZOM-276 also match but are Duplicates (out). ZOM-271 "
   "(\"ATK POWER\") does not match. States as found: Done for all except ZOM-202 In Progress, ZOM-280 Canceled, ZOM-293 Todo.")
ev("Read the comments on every ZOM issue created up to Aug 31 to find Blake's \"tiers:\" notes and each title match's closing note (Linear: comments, one issue at a time)",
   f"\"tiers:\" notes by Blake on ZOM-221 \"{note('ZOM-221')}\", ZOM-281 \"{note('ZOM-281')}\" (assigned to someone else), "
   f"ZOM-300 \"{note('ZOM-300')}\", ZOM-305 \"{note('ZOM-305')}\", ZOM-378 \"{note('ZOM-378')}\". These 5 join the "
   f"scope. Closing notes that decide status: ZOM-45 \"{note('ZOM-45')}\"; ZOM-173 \"{note('ZOM-173')}\"; ZOM-277 \"{note('ZOM-277')}\"; "
   f"ZOM-315 \"{note('ZOM-315')}\"; ZOM-282 \"{note('ZOM-282')}\"; ZOM-202 \"{note('ZOM-202')}\"; ZOM-280 \"{note('ZOM-280')}\"; "
   f"ZOM-293 \"{note('ZOM-293')}\"; ZOM-312 \"{note('ZOM-312')}\"; ZOM-295 \"{note('ZOM-295')}\". The other title "
   "matches' closing notes say the change works on the dev build, or name the PR it merged with (ZOM-303 match3d#244); "
   "no other comment on a ZOM issue starts with \"tiers:\".")
ev("Check every title match's PR for a \"not tiers\" review, since rule 1 drops a title match Blake marked \"not tiers\" on its PR. Only four title matches have a PR in the match3d repo, and their closing notes (OE 21) name them: 243 (ZOM-173), 244 (ZOM-303), 265 (ZOM-312) and 271 (ZOM-295) (GitHub: reviews and the inline review comments on each PR)",
   f"Two have one. PR 265: Blake's review of Thu Jul 3 2025 17:50 UTC has an empty body, and its inline comment on Assets/Scripts/LevelEditor/UI/LevelSettings.cs says \"{RC265}\" "
   f"PR 271: Blake's review of Fri Jul 4 2025 01:05 UTC is an approval with an empty body, and its inline comment on Assets/Scripts/Monster/MonsterSpawner.cs says \"{RC271}\" "
   "PR 243 has no reviews and PR 244 has only the automated review bot's reviews (\"Actionable comments posted\"). So ZOM-312 and ZOM-295 stay "
   "off the register, and ZOM-173 and ZOM-303 stay on.")
ev("Read the comment on pull request 401 in the match3d repo, which splits ZOM-282's enrage values (GitHub: comments on PR 401)",
   f"Blake, Mon Aug 25 2025 17:02 UTC: \"{C401}\" A PR that splits numbers is not a replacement (rule 4), so ZOM-282 "
   "stays Live and nothing is Replaced by PR 401.")
ev("Read ZOM-303 for whether the level drops after a demotion (Linear: open ZOM-303)",
   "ZOM-303 \"Dynamic Difficult Design Oversight Fix\", Done, closing note \"merged with match3d#244\": \"Solution: when a player is demoted, "
   "we also need to demote the level difficulty for the level\". So yes, the level drops a tier after a demotion.")
lf = "; ".join(f"{r['id']} assignee {r['assignee']}, completed {r['completed_at'] or 'never'}, priority {r['priority']} ({r['priority_label']})" for r in T.ROWS)
ev("Read the assignee, completion time and priority of each register ticket for Robert's columns (Linear: open each issue, or read the fields from the team's issue list)",
   f"{lf}. In Pacific time ZOM-200 was marked done on 2025-06-12 and ZOM-274 and ZOM-282 on 2025-06-20 (Linear shows 01:17 UTC the next day); "
   "every other done day is the same in Pacific time and UTC. ZOM-202, ZOM-280 and ZOM-293 were never marked done.")
# ---------------------------------------------------------------- analysis
rl = "; ".join(f"{r['id']} ({r['state']}) {r['status']}" + (f", replaced by {r['replaced_by']}" if r['replaced_by'] else "") for r in T.ROWS)
ev("Work out the register from rules 1 to 4 as amended (OE 2 to 11, 20 to 25), no tool",
   f"23 rows: {rl}. Counts: 15 Live, 4 Editor only ({EO}), 3 Not shipped ({NS}), 1 Replaced (ZOM-254 by ZOM-282). "
   "Off the register: ZOM-30, 49, 50, 161, 262, 275 (OE 2); ZOM-162, 163, 201, 250 (OE 3); ZOM-258 (OE 7); ZOM-312 and ZOM-295 (OE 22); ZOM-203 and "
   "ZOM-276 (Duplicates). Why each row that is not Live: ZOM-173 Editor only (the set count in the level objects panel, level editor, OE 21); "
   "ZOM-200 Editor only (a debug menu, stripped from store builds per OE 11); ZOM-277 and ZOM-315 Editor only (the editor's stats panel, "
   "nothing changes in the game, OE 21); ZOM-202 Not shipped (nothing merged); ZOM-280 Not shipped (Canceled); ZOM-293 Not shipped (still "
   "open); ZOM-254 Replaced (ZOM-282's note says it replaces it). Every other row is Live: runtime changes merged before the Sep 26 cut (OE 10).")
# ---------------------------------------------------------------- writes
ev("Create the register spreadsheet with a Tickets tab (Sheets: create spreadsheet)",
   "A new Google Sheet owned by Julia with a tab named Tickets (any title).")
rows_out = "; ".join(f"{r['id']} | {r['title']} | {r['state']} | {r['status']} | {r['assignee']} | {r['done_pt'] or '(blank)'} | {r['priority']} ({r['priority_label']})"
                     + (f" | {r['replaced_by']}" if r['replaced_by'] else "") for r in T.ROWS)
ev("Write the 23 ticket rows into the Tickets tab (Sheets: update values on the Tickets tab)",
   "Header ticket, title, Linear state (as found), status, assignee, done day (Pacific), priority, replaced by; then the 23 rows of OE 26 with their "
   f"Linear titles and Robert's columns: {rows_out}. The UTC day (2025-06-13, 2025-06-21, 2025-06-21) for ZOM-200, ZOM-274 and ZOM-282 is also accepted.")
ev("Add a second tab named Rules in force (Sheets: batch update, add sheet)",
   "The spreadsheet now has two tabs, Tickets and Rules in force.")
ev("Write the rules into the Rules in force tab (Sheets: update values on the Rules in force tab)",
   "Starting tier: when a new player's 10th game ends (wins and losses both count), average CPM above 90 goes to tier 1, everyone else stays "
   "on tier 0 (90 exactly stays on 0). Promotion: win rate of 80% or more over up to the most recent 10 attempts; on tier -2 one win promotes. "
   "Demotion: 4 losses in a row, or a win rate of 50% or lower over up to the last 10 games; the record resets after every promotion or "
   f"demotion. Level drop after a demotion: yes (ZOM-303). Enrage, per monster, speed and damage, no hp, copied from the Live tab: {LIVE_TAB}.")
ev("Move the spreadsheet into the ZM Difficulty folder (Drive: move file into the folder found in OE 14)",
   "The register's parent is the ZM Difficulty folder.")
ev("Share the register with Robert as editor (Drive: share file, robert@harmonygames.co, role writer)",
   "robert@harmonygames.co has edit access.")
ev("Share the register with Brian as commenter (Drive: share file, brian.foster@harmonygames.co, role commenter)",
   "brian.foster@harmonygames.co has comment access (not edit, per OE 3).")
ev("Share the register with Leonard as commenter (Drive: share file, leonard.hayes@harmonygames.co, role commenter)",
   "leonard.hayes@harmonygames.co has comment access.")
ev("Share the register with Arthur as viewer (Drive: share file, arthur.blake@harmonygames.co, role reader)",
   "arthur.blake@harmonygames.co has view access (per OE 7).")
ev("Comment on ZOM-199 with what the build does (Linear: create comment on ZOM-199)",
   "A new comment on ZOM-199 saying the build's starting-tier check is CPM > 90, not >= 90, so 90 exactly stays on tier 0, and that it runs when a player's 10th game ends.")
ev("Comment on ZOM-254 naming what replaced it (Linear: create comment on ZOM-254)",
   "A new comment on ZOM-254 saying it was replaced by ZOM-282.")
for k in T.EO + T.NS:
    st = 'Editor only' if k in T.EO else 'Not shipped'
    ev(f"Comment on {k} ({st}) under the checklist's rule 6 change (Linear: create comment on {k})",
       f"A new comment on {k} saying the change isn't in the store builds and naming the builds checked, iOS 0.3.49 and Android 0.3.133 (OE 2).")
ev("Reply to Leonard in the DM with what he asked for (Slack: send a message in the DM with Leonard, in the ask's thread or in the DM)",
   "A message from Julia saying the register is in the ZM Difficulty folder; 23 tickets made the list: 15 Live, 4 Editor only, 3 Not shipped, "
   f"1 Replaced; Not shipped keys {NS}; Editor only keys {EO}; ZOM-254 was replaced by ZOM-282; a new player gets the "
   "starting tier when their 10th game ends, wins and losses both counting (not at level 10).")

out = [f"OE {i}  {a}\n        Expected: {x}\n" for i, (a, x) in enumerate(E, 1)]
body = "\n".join(out)
assert '—' not in body and '\r' not in body, 'em dash or CR'
open('task_inputs/08_Oracle_Events.md', 'w').write(body)
print('wrote', len(E), 'events', len(body), 'chars')
