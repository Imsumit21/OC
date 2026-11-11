# Oracle Events blind review, round 1

Scope: `08_Oracle_Events.md` (103 events) against `04_Prompt.txt`, `01_Universe_Inject.sql` (read as text, never executed), the two rule files, `catalog.json`, and base records read only through `hg.py search`.
Clock: 2025-10-01 00:00 PT (07:00 UTC). PT = UTC-7 on all dates involved.

Outcome: the decision in OE 21 is right for all 39 reports, and every write event matches Brian's note. The defects are in the discovery events: one false "newest" label, one unsourced build and count, one search term with no valid source, and four places where an Expected line names only the hit and not the scope that makes OE 21's "new", "passed" and "no other" calls derivable.

Likely score under the rules as written: Accuracy 2 (finding 1 is a label one record breaks), Completeness 2 or 3 depending on whether findings 4 to 6 are read as missing discovery.

## Findings

### CRITICAL

**1. OE 7: "Android Submission #135 is the newest main build."** (also the action text "plus the newest main build")
- Wrong. Four main builds were posted in #builds after #135 (Sep 30 1:13 PM PT) and before the clock:
  - `Match3D Android - #2027 - main`, Tue Sep 30 2:27 PM PT (21:27 UTC), `messages/C05433XK267/2025-09.json` `/1127`
  - `Match 3D iOS Internal - #1758 - main`, 2:27 PM PT (21:27 UTC), `/1128`
  - `Match 3D iOS Internal - #1759 - main`, 2:42 PM PT (21:42 UTC), `/1131`
  - `Match3D Android - #2028 - main`, 2:43 PM PT (21:43 UTC), `/1132` (the last post in the channel)
- An agent that follows "the newest main build" lands on Android #2028, and OE 14's search then has no source.
- The decision does not need "newest". It needs #135 to be a main build posted after #1745, #1750 and #1757, which is true.
- Fix: action "…for every build the sheet names, the build in the chat (OE 6) and Android Submission 135 (named in the ticket notes, OE 12)". Last sentence: "Android Submission #135 is a main build posted after iOS Internal #1745, #1750 and #1757." Move OE 12 before OE 7, or split the #135 read into its own event after OE 12.

### MAJOR

**2. OE 7: "Sixteen posts" / "Thirteen are builds of main" / "Match 3D iOS Internal - #1754 - main".**
- #1754 is named by nothing in OE 3, OE 6 or any earlier event. The sheet names 13 builds (1698, 1713, 1974, 1727, 129, 1984, 1745, 2013, 2006, 1750, 2010, 1746, 1757), the chat names #1718, plus #135: 15 posts, not 16.
- No status depends on #1754.
- "Every build … the chat name" is also broken by Calvin's message of Thu Sep 25 8:48 AM PT, "I think the The coin animation is being fixed on Match 3D iOS Internal - #1716" (`messages/D06UPGF5PQV/2025-09.json` `/156`); #1716 is not listed.
- Fix: drop #1754 and write "Fifteen posts … Twelve are builds of main", or keep it and say why it is read. Narrow "the chat" to "#1718, the build Calvin names just before Vincent's ok (OE 6)".

**3. OE 14: "(search "Submission 135", the build from OE 7)" / "later reports from the newest main build".**
- The term has no valid source in OE 7 once finding 1 is fixed. It is first seen in OE 12, in Samuel's note on ZOM-585 and Owen's on ZOM-586.
- Fix: "Search Slack for other sightings on Android Submission 135, the build Samuel and Owen name in OE 12 (search "Submission 135"), and open the threads of the hits."

**4. OE 11: Expected names only #473.**
- The action lists PRs merged since Sep 26 and reads each one the sheet does not name. Eight such PRs exist (`github/data.json` `/pull_requests/2370`–`2379`):
  - #466 "[PERSON_NAME_0092]/tutorial adjustments", merged Fri Sep 26 8:14 AM PT (15:14 UTC)
  - #467 "adding safety checks", Fri Sep 26 11:58 AM PT (18:58 UTC)
  - #468 "Collect And Win", Mon Sep 29 9:13 AM PT (16:13 UTC)
  - #469 "Unity 6000.2.6f1 + top part tex resoultion decrease", Mon Sep 29 6:50 PM PT (Sep 30 01:50 UTC)
  - #470 "Collect And Win minor bugs fixes", Tue Sep 30 8:51 AM PT (15:51 UTC)
  - #471 "Samuel/zom 498 536", 8:52 AM PT (15:52 UTC)
  - #473 "Addressables/sp", 8:41 AM PT (15:41 UTC)
  - #474 "Skip/fix", 8:48 AM PT (15:48 UTC)
- The Expected line reads as if #473 were the only one. I read the bodies and comments of the other seven: none claims a sheet row. #466, #467 and #474 are tutorial-skip work, which Brian's note keeps off the list.
- Fix: "Eight merged PRs are not on the sheet: #466, #467, #468, #469, #470, #471, #473, #474. Only #473 says anything about the flow list: …" (rest unchanged).

**5. OE 13: "the two open rows with no ticket and no fix in OE 3".**
- Wrong basis. Row 38 also has no ticket, no fix and no re-test (grid row 38: `"Android #1984", "", "", ""`). Rows 9 and 29 become open without ticket or fix after OE 14.
- OE 21 marks 17 reports "new" (1, 2, 3, 5, 7, 9, 22, 23, 25, 26, 27, 29, 31, 33, 35, 38, 39). No event looks for an existing ticket for 15 of them; the note's "If no ticket has it" needs that.
- I read base ZOM-500 to ZOM-566 (`linear/data.json` `/issues/3573`–`3643`). None holds those rows. The nearest titles are ZOM-555 "Zombie Lane Reward Animations" (Done), ZOM-540 "Boss Arena Tutorial" (Done), ZOM-505 "Tutorial repeats at level 19 in V 1736 Android version" and ZOM-564, all different subjects. So the calls are right; the discovery is what is missing.
- Fix: "Search the ZOM tickets in Linear for one that already holds each row with a blank Ticket cell (rows 1, 2, 3, 5, 7, 9, 11, 20, 22, 23, 25, 26, 27, 29, 31, 33, 35, 38) and Marcus's report, by the row's wording, and read the comments of the hits. Expected: ZOM-556 … (row 11). ZOM-560 … (row 20). No ticket holds the other sixteen rows or Marcus's report."

**6. OE 15: only "arena entry button" is searched.**
- OE 21 keeps ten passes (rows 3, 5, 7, 22, 23, 26, 27, 31, 33, 35). "As long as that pass still stands" needs a check for a later sighting of each; the event shows it for row 27 only.
- I searched base Slack (September files, all channels) for each of the other nine rows' wording and read every base message since Sep 26 in #zombie-bugs and #zombie-match3d: no sighting. Base Linear has no comment dated Sep 29 or 30.
- Fix: "Search Slack for other sightings of the ten passed rows, by each row's wording (rows 3, 5, 7, 22, 23, 26, 27, 31, 33, 35). Expected: one hit, for row 27: … so that pass stands. Nothing for the other nine."

### MINOR

**7. OE 14: "Robert's reply under his Sep 10 thread".** The parent is ts 1757467270.178829 = Sep 10 01:21 UTC = Tue Sep 9 2025 6:21 PM PT (`messages/C08R27X0EAH/2025-09.json` `/461`). Every other date in the file is PT first. Fix: "his thread of Tue Sep 9 2025 6:21 PM PT (Sep 10 01:21 UTC)". Vincent's Sep 15 parent is right in both zones (`/651`, 5:31 AM PT).

**8. OE 9, 10, 11: "Arthur Blake" / "Oliver Brooks's comment".** The comment reads return `author_login` `EMPLOYEE_0025_GITHUB_USERNAME` and `EMPLOYEE_0003_GITHUB_USERNAME`, not a name. The name needs a user lookup (`github/data.json` `/users/6` Arthur Blake, `/users/1` Oliver Brooks). Fix: add "(login EMPLOYEE_0025_GITHUB_USERNAME, Arthur Blake in the GitHub user record)", and the same for Oliver.

**9. OE 7: no stated way to find the posts.** Build posts have empty `text`; the title is only in `attachments[0].fallback` (`/1124`). A text search for "#1745" may return nothing. Fix: "Read the #builds history in Slack from Wed Sep 24 to Tue Sep 30 2025 and pick out the post of each build …".

**10. OE 16: Expected names only Marcus.** Calvin's DMs with messages since Sep 26 are five: Marcus (D05U73FNDDL), Brian (D0770ET6WBW), Vincent (D06UPGF5PQV), EMPLOYEE_0021 (D05S1S2H55M) and EMPLOYEE_0032 (D07GJJBK789). The near miss is D05S1S2H55M `/121`, Mon Sep 29 3:14 PM PT, "Se ve un poco mas lento todo": a remark on a clip Calvin sent, not a build sighting, and it is row 17's subject anyway. "No sheet row has it" is correct. Marcus's second message (10:10 AM PT, "saw it 3 levels in a row. its not the vfx, the animation itself is fine, its just the glow") is what ties it to the home screen after a level and is not quoted. Fix: add that quote and "The other DMs since Sep 26 (Brian, Vincent, EMPLOYEE_0021, EMPLOYEE_0032) carry no bug seen in a build."

**11. OE 48: title "Pass icon glow stays on after everything is claimed".** This is the author's wording in quotation marks; no record has it. Marcus wrote "the pass icon glow stays on after i claimed everything". Fix: "A new ZOM issue titled with Marcus's report (the pass icon glow staying on after everything is claimed) …".

**12. OE 94: Ticket column source not stated.** For the 17 new reports the Ticket cell is the key created in OE 32 to OE 48, which OE 21 can only call "new". Fix: "(columns from OE 2, rows from OE 21, ticket keys of the new sub-issues from OE 32 to OE 48)".

**13. OE 93 to OE 95: the second tab.** `gsheets_create_spreadsheet` gives one tab (`initialSheetTitle`). The Areas tab needs `gsheets_batch_update` (addSheet) before the values write, so OE 95 holds two writes. Fix: OE 93 Expected "…its first tab named Reports"; OE 95 "Add the Areas tab to the stock-take sheet and fill it".

**14. OE 4: search term "pass sheets".** OE 3's note says "my pass sheet legend doc". "pass sheets" is the target's title, and "legend" is nowhere in the doc. Fix: "(search "pass sheet", from the note in OE 3)".

**15. OE 12: "Samuel".** The Linear author is samuel.turner@harmonygames.co (`usr_caafeec2804b3a67`, `/users/34`); Owen gets his full name in the same line. Fix: "Samuel Turner".

### Advice only (traps the events do not call out; no score effect)

- OE 5: "QA passes" also returns Arthur's "DD hotfix builds and QA passes", which says the opposite ("a pass on the dev's branch build is enough").
- OE 17: the same search returns the Sep 29 invitation, "Agenda is on the roadmap card: Collect & Win and Daily Gift this time."
- OE 19: Brian's DM of Mon Sep 29 9:41 AM PT, "For the flow review on Friday I want to go through collect&amp;win and daily gift first", is superseded by Leonard's card change.
- OE 12: Owen on ZOM-577, "I have a fix locally, need to test it before I open the PR", is why row 19 is not Waiting on QA.
- OE 2: the note's scope sentences are not quoted ("The skip tutorial exceptions Oliver has in #zombie-bugs and the input blocker I parked are not on the sheet and stay off."); they explain why #466, #467, #474 and Vincent's Sep 26 #zombie-bugs post add no report.

## OE 21, checked report by report

All 39 statuses, tickets and review flags are correct and derivable from OE 2 to OE 19, apart from the "new" and "pass stands" absences in findings 5 and 6.

| Reports | Status | Basis checked |
|---|---|---|
| 1, 2, 25 | Waiting on QA | "ok, chat" is #1718, a `[PERSON_NAME_0029]/QueueManager` build (Sep 25 16:25 UTC); #465 merged to main Sep 25 22:15:51 UTC; no re-test on a main build |
| 3, 7, 27, 35 | Passed | nr on iOS Internal #1745, main. Row 27: Robert's sighting is on Android #2006, posted 15:39 UTC, before #1745 at 16:19 UTC |
| 5 | Passed | ok on #1745, main |
| 22, 23, 26 | Passed | nr / ok / nr on Android #2006, main |
| 31, 33 | Passed | ok on iOS Internal #1757, main |
| 9 | Waiting on a fix | nr on #1745, then Vincent on Submission 135 (Sep 30 21:20 UTC); no fix |
| 29 | Waiting on a fix | ok on #1750, then Robert on Submission 135 (21:44 UTC); no fix |
| 17 | Waiting on a fix | ok on #1757, then Samuel on Submission 135 (21:52 UTC); #472 already tried on a main build |
| 24 | Waiting on a fix | nr on #1757, then Owen on Submission 135 (22:07 UTC); no fix |
| 6 | Waiting on QA | #472 body names the pre-level panel fix; merged 15:53:04 UTC; never re-tested |
| 18 | Waiting on QA | in #472 per Arthur; "again" on Android #2013 (Sep 29 23:34 UTC), before the merge |
| 13, 14, 37, 38 | Waiting on QA | Oliver's comment on #473 (merged 15:41:20 UTC); never re-tested |
| 12, 15 | Waiting on a fix | Arthur: not in the #472 diff |
| 32 | Waiting on a fix | Arthur: not in #475 |
| 34 | Waiting on a fix | "again" on #1757 (18:43 UTC), after #475 merged 16:09:15 UTC |
| 10 | Waiting on a fix | "again" on #2013; no fix |
| 4, 8, 11, 16, 19, 20, 21, 28, 30, 36, 39 | Waiting on a fix | no fix in main, no pass |

- Totals: 10 Passed / 9 Waiting on QA / 20 Waiting on a fix. Correct.
- Areas, open of total: Tutorials 3/5, Level-end rewards 3/5, Daily Gift 3/3, Season Pass 5/5, Collect & Win 4/4, Win Streak 3/3, Zombie Lane 1/3, Boss Arena 1/3, Endless Mode 4/4, Card packs 2/4. Sum 39; 0 Clear. Correct.
- Review list: 6, 8, 36 (Level-end rewards) and 15, 17, 18, 19 (Collect & Win) = 7. Correct.
- Writes: 10 children (all Todo), 17 new sub-issues (10 Done, 5 In Validation, 2 Todo), 22 moves (9 state changes: ZOM-568, 572, 573, 584 to In Validation; ZOM-571, 574, 581, 585 to Todo; ZOM-576 stays In Validation), 22 notes, sheet, 2 tabs, move, 5 shares, slide, DM. All match the note and the DM. None missing or duplicated.

## Events verified as fully correct

OE 1, 2, 3 (all 38 rows character for character), 5, 6, 8, 17, 18, 19, 20, 21, 22–47, 49–92, 96–103.

Correct in every value but carrying a finding above: OE 4 (14), 9 and 10 (8), 11 (4, 8), 12 (15), 13 (5), 14 (3, 7), 15 (6), 16 (10), 48 (11), 93–95 (12, 13). OE 7 has every post title and time right; its defects are findings 1, 2 and 9.

## Other checks

- Every quoted span (123) is in the SQL or the base record cited. Every PT/UTC pair and weekday was recomputed and is right, except finding 7.
- Tool feasibility: every step has a cataloged tool (`github_get_pull_request`, `_comments`, `_reviews`, `github_get_issue_comments`, `github_list_pull_requests`, `linear_list_comments`, `linear_create_issue` / `linear_update_issue` with `parentId` and `state`, `trello_search`, `trello_get_card_actions`, `slack_read_thread`, Slack search, `gsheets_create_spreadsheet`, `gsheets_batch_update`, `gsheets_values_update`, `gdrive_move_file`, `gdrive_share_file`, `gslides_batch_update`).
- Access: Calvin (EMPLOYEE_0006) is a member of #builds, #zombie-bugs, #zombie-match3d and the three DMs; the sheet, both docs, the mail and the calendar event are his or shared with him.
- No event states something the agent refrains from doing, and none describes the final answer. A move that also sets the state is one `linear_update_issue` call.
- Base has no other "flow review" record in Gmail, Calendar or Trello, and no Drive path named "queue manager".

## Limits

- Group DMs (mpim) were not swept for a bug told to Calvin since Sep 26.
- Whether Slack search indexes attachment text (finding 9) is a runtime question.
- Drive full-text collisions for "flow pass" and "QA passes" were checked by file name only; the full scan was too slow to finish.
- My scratch files went into the shared session scratchpad before I moved to a subfolder (`blind_r1/`). `builds.json`, `ts.json`, `rows.json`, `p.py` and `err.txt` there are mine and may have replaced same-named files.
