# Blind fork sweep, rev2 (Calvin Price, Queue Manager epic, clock Wed Oct 1 2025)

Reviewer read only: `04_Prompt.txt`, `01_Universe_Inject.sql` (as data), and the base universe through `hg.py search`. Nothing under `Working_Files/` and not `01_Scenario_Design.md`. No SQL was run.

Not checked: "Julia's point about your tickets" (Brian's note) was not traced to a record; the Collect & Win canvas was not opened (the Bug Checklist canvas exists in Slack `files.json`).

## 0. Instruction chain followed

1. Prompt -> Brian's DM `D0770ET6WBW` msg `446ba456...` (Sep 30 20:40 UTC).
2. That DM -> Brian's note on ZOM-543, `comment_faaa7924...` (Sep 30 20:25): children, scope, the three statuses, ticket handling, Clear/Open, review list, sheet tabs, slide.
3. Note -> Vincent's sheet `f_cb40955893624e1acb8500` (38 rows) and legend doc `f_d3a1aa5976285aac98ffda`.
4. Note -> "Arthur's rule for QA passes" = doc `f_6d0326fa006b136f1bbf82` "ZM builds and QA passes" (main-branch builds only; a pass stands until the bug is seen again on a main build made after the one it passed on; branch is in the #builds post). Decoy: `f_ea7517885d11570b54bf13` (DD hotfix rule).
5. Note -> "agenda of Thursday's review" = Trello card `68daad83bacf52c6ea7e1593`, current desc "Collect & Win, Level-end rewards" (changed Sep 30 17:22; was "Collect & Win, Daily Gift"). Leonard's update mail: "daily gift waits until next week".
6. DM -> "everyone on the review invite" = gcal `evt_342a813cb7765d4a6fce8d`: arthur.blake, brian.foster, calvin.price, julia.lawson, leonard.hayes (organizer), vincent.parker.

## 1. Facts checked in the base

### Build times and branches (#builds `C05433XK267`, UTC)

| Build | Branch | Success |
|---|---|---|
| iOS Internal 1698 | QueueManager (feature) | 09-24 18:07 |
| iOS Internal 1708 / 1716 / 1718 | QueueManager (feature) | 09-24 22:35 / 09-25 15:19 / 09-25 16:25 |
| Android 1974 | main | 09-24 23:13 |
| iOS Internal 1713 | main | 09-25 11:27 |
| iOS Internal 1727 / Android 1984 | main | 09-25 22:21 |
| Android Submission 129 | main | 09-26 02:39 |
| Android 2006 | main | 09-29 15:39 |
| iOS Internal 1745 | main | 09-29 16:19 |
| iOS Internal 1746 | AnimatedIcons (feature) | 09-29 19:24 |
| Android 2010 | main | 09-29 19:26 |
| Android 2013 | main | 09-29 23:34 |
| iOS Internal 1750 | main | 09-30 01:55 |
| iOS Internal 1754 | main | 09-30 16:01 (started 15:56:10) |
| iOS Internal 1757 | main | 09-30 18:43 (started 18:37:53) |
| Android Submission 135 | main | 09-30 20:13 (started 18:45) |
| iOS 1760 / Android 2029 | main | 10-01 05:50 ("Fix end popup", Oliver) |

### PRs (GitHub `harmonygames-Games/match3d`)

| PR | Head | Merged to main | Notes |
|---|---|---|---|
| #465 | QueueManager | 09-25 22:15:51 | body: coin animation after kill; queued tutorials |
| #472 | ImplementQueueManager | 09-30 15:53:04 | Arthur `#472#rc_1` (15:53:40): season pass icon restart is NOT in this diff, the two Collect & Win ones are |
| #473 | addressables/sp (Oliver) | 09-30 15:41:20 | Oliver `#473#c_2` (15:42:10): also has the fix for the pass start popup after every level and the bar filling before the tokens land |
| #475 | AnimatedIcons | 09-30 16:09:15 | Arthur `#475#rc_1` (16:09:50): pack sound stop is not in here |

### "ok, chat" (rows 1, 2, 25)

Vincent DM `D06UPGF5PQV`: Calvin 09-25 16:29 "I think I may have fixed the tutorial stuffs. Match 3D iOS Internal - #1718 already tested"; Vincent 09-25 17:15 "Looks ok to me" / "Boss arena as well". Build 1718 is a QueueManager feature-branch build. Every build Calvin named in that chat (1695-era, 1708, 1716, 1718) is a feature-branch build.

### Later sightings

- Row 9: Vincent, #zombie-bugs thread reply `b156fdcd...` (09-30 21:20), Android Submission 135: "the pass popup came up on top of the gift again. so that one is not gone". Pass was nr on iOS 1745 (09-29). Sub 135 is a main build made after 1745.
- Row 29: EMPLOYEE_0016, #zombie-bugs thread reply `a4082477...` (09-30 21:44), Android Submission 135: home intro replays coming back from endless. Pass was ok on iOS 1750 (09-30 01:55). Sub 135 is later.
- Row 27: EMPLOYEE_0016, #zombie-match3d `ecf80487...` (posted 09-29 22:40), "Android 2006: I could still tap the arena entry button". Pass was nr on iOS 1745 (built 09-29 16:19). Android 2006 was built 09-29 15:39, 40 minutes BEFORE 1745.

### Tickets

- ZOM-543: In Progress, assignee Calvin, creator Brian, no parent.
- ZOM-556 (Todo, daily gift does not reset after a skip) carries Vincent's comment `comment_b3c56083...` tying it to row 11. ZOM-560 (Todo, abandoned pack freezer) carries `comment_9f28b3d8...` tying it to row 20. Neither key is in the sheet.
- ZOM-567..584 are the 18 keyed rows. States: all Todo except ZOM-571, ZOM-576, ZOM-581 (In Validation).
- No other base ZOM ticket (520-566 scanned by title) matches an unkeyed row.

### DMs to Calvin since Sep 26

All of Calvin's DM channels with September files were read from Sep 24. The only bug report from somebody other than Vincent is Marcus, `D05U73FNDDL` `806f4a67...` + `bb5dd875...` (09-30 17:10): pass icon glow stays on after claiming everything, "today's main build", "3 levels in a row", "the animation itself is fine".

## A. My answer

39 reports: 38 sheet rows + Marcus's glow report.

| # | Area | Status | Ticket | Review list | Why |
|---|---|---|---|---|---|
| 1 | Tutorials | Waiting on QA | new (In Validation) | No | ok was in chat on 1718, a feature-branch build; #465 is in main since 09-25, not re-tested on main |
| 2 | Tutorials | Waiting on QA | new (In Validation) | No | same as row 1 |
| 3 | Tutorials | Passed | new (Done) | No | nr on iOS 1745, main |
| 4 | Tutorials | Waiting on a fix | ZOM-567 (Todo) | No | no fix; dev cannot reproduce yet |
| 5 | Level-end rewards | Passed | new (Done) | No | ok on iOS 1745, main, after #465 merged |
| 6 | Level-end rewards | Waiting on a fix | ZOM-568 (Todo) | Yes | no fix |
| 7 | Level-end rewards | Passed | new (Done) | No | nr on iOS 1745, main |
| 8 | Level-end rewards | Waiting on a fix | ZOM-569 (Todo) | Yes | no fix |
| 9 | Daily Gift | Waiting on a fix | new (Todo) | No | nr on 1745, but Vincent saw it again on Android Submission 135, a later main build; no fix known |
| 10 | Daily Gift | Waiting on a fix | ZOM-570 (Todo) | No | no fix; still on 2013 |
| 11 | Daily Gift | Waiting on a fix | ZOM-556 (Todo) | No | existing ticket per Vincent's comment; no fix |
| 12 | Season Pass | Waiting on a fix | ZOM-571 (In Validation -> Todo) | No | Arthur: not in #472, needs its own PR |
| 13 | Season Pass | Waiting on QA | ZOM-572 (Todo -> In Validation) | No | Oliver: fix is in #473, merged 09-30; not re-tested |
| 14 | Season Pass | Waiting on a fix | ZOM-573 (Todo) | No | fix on a branch, no PR |
| 15 | Collect & Win | Waiting on a fix | ZOM-574 (Todo) | Yes | no fix |
| 16 | Endless Mode | Waiting on a fix | ZOM-575 (Todo) | No | no fix |
| 17 | Collect & Win | Passed | new (Done) | No | ok on iOS 1754, main, built after #472 merged |
| 18 | Collect & Win | Waiting on QA | ZOM-576 (In Validation, no change) | Yes | "again" was on Android 2013 (09-29), before #472 merged (09-30 15:53); fix in main untried |
| 19 | Collect & Win | Waiting on a fix | ZOM-577 (Todo) | Yes | fix is local only |
| 20 | Win Streak | Waiting on a fix | ZOM-560 (Todo) | No | existing ticket per Vincent's comment; no fix |
| 21 | Win Streak | Waiting on a fix | ZOM-578 (Todo) | No | dev still checking |
| 22 | Zombie Lane | Passed | new (Done) | No | nr on Android 2006, main |
| 23 | Zombie Lane | Passed | new (Done) | No | ok on Android 2006, main |
| 24 | Zombie Lane | Passed | new (Done) | No | ok on Android 2010, main |
| 25 | Boss Arena | Waiting on QA | new (In Validation) | No | ok in chat on 1718, feature branch; #465 in main, not re-tested |
| 26 | Boss Arena | Passed | new (Done) | No | nr on Android 2006, main |
| 27 | Boss Arena | Passed | new (Done) | No | nr on iOS 1745; the Android 2006 sighting is on a build made before 1745, so the pass stands |
| 28 | Endless Mode | Waiting on a fix | ZOM-579 (Todo) | No | no fix |
| 29 | Endless Mode | Waiting on a fix | new (Todo) | No | ok on 1750, seen again on Android Submission 135, a later main build; no fix known |
| 30 | Endless Mode | Waiting on a fix | ZOM-580 (Todo) | No | no fix |
| 31 | Card packs | Passed | new (Done) | No | ok on iOS 1757, main, after #475 merged |
| 32 | Card packs | Waiting on a fix | ZOM-581 (In Validation -> Todo) | No | Arthur: pack sound stop is not in #475 |
| 33 | Card packs | Passed | new (Done) | No | ok on iOS 1757, main |
| 34 | Card packs | Waiting on a fix | ZOM-582 (Todo) | No | "again" on iOS 1757, built after #475 merged: fix tried, still happens |
| 35 | Tutorials | Passed | new (Done) | No | nr on iOS 1745, main |
| 36 | Level-end rewards | Waiting on a fix | ZOM-583 (Todo) | Yes | no fix |
| 37 | Win Streak | Waiting on a fix | ZOM-584 (Todo) | No | no fix |
| 38 | Season Pass | Waiting on QA | new (In Validation) | No | Oliver: fix is in #473, in main; not re-tested |
| 39 | Season Pass | Waiting on a fix | new (Todo) | No | Marcus DM 09-30, pass icon glow stays on; not a sheet row; no fix |

**Five numbers:** Passed 12, Waiting on QA 6, Waiting on a fix 21, areas clear 1 (Zombie Lane), review list 6 (rows 6, 8, 36, 15, 18, 19).

**Areas tab:** Tutorials Open 3; Level-end rewards Open 3; Daily Gift Open 3; Season Pass Open 5; Collect & Win Open 3; Win Streak Open 3; Zombie Lane Clear 0; Boss Arena Open 1; Endless Mode Open 4; Card packs Open 2. Total open 27.

**Linear:** 10 children under ZOM-543 (team ZOM, no assignee): Zombie Lane Done, the other nine Todo. 20 existing tickets moved under children with a note (ZOM-556, ZOM-560, ZOM-567..584). 19 new sub-issues, no priority, no assignee: 12 Done, 4 In Validation (rows 1, 2, 25, 38), 3 Todo (rows 9, 29, Marcus).

**Existing tickets that change state:** ZOM-571 In Validation -> Todo; ZOM-572 Todo -> In Validation; ZOM-581 In Validation -> Todo. ZOM-576 stays In Validation. The other 16 stay Todo.

**Sheet shared with:** arthur.blake, brian.foster, julia.lawson, leonard.hayes, vincent.parker (all @harmonygames.co). Calvin owns it. Sheet goes in folder `d_36cdb0374c4aad3b8bf741`; slide goes in deck `f_637e63ae6c1b4a7eb016aa`.

**Rows that differ from the sheet's own reading** (sheet alone gives 17 Passed): 1, 2, 25 (ok, chat -> Waiting on QA); 9, 29 (nr/ok -> Waiting on a fix); 12, 32 (fix named -> Waiting on a fix); 13, 38 (no fix named -> Waiting on QA); 18 ("again" -> Waiting on QA); 11, 20 (blank ticket -> ZOM-556, ZOM-560).

## B. Forks

Severity: blocking = I would expect a strict reviewer to say the records do not settle it. Major = records settle it, but a second careful reading is defensible and changes a graded value. Minor = settled, or changes nothing graded.

No fork reached blocking. Four are major.

### F1 (major). Rows 1, 2, 25: "Waiting on QA" or "Waiting on a fix"?

- Reading A (mine): not Passed (branch build), fix #465 is in main, QA has not tried it on main -> Waiting on QA. Arthur's doc backs this: a branch pass "has to be done again once the branch is merged".
- Reading B: Brian's wording is "a fix for it is in main that QA has not tried yet". QA did try this fix (on the branch, and said ok). Read literally, "has not tried" is false, so the row falls to "Waiting on a fix: everything else".
- Records: Brian's note `comment_faaa7924...`; Arthur's doc `f_6d0326fa...`; DM 09-25 17:15; #builds 1718; PR #465 merged 09-25 22:15.
- Effect of B: Waiting on QA 3, Waiting on a fix 24; three new sub-issues Todo instead of In Validation.
- Confidence a strict reviewer calls it settled: about 70%. One clause in Brian's note ("tried on a main build") would close it.

### F2 (major). Row 9: does Vincent's own later sighting reopen it?

- Reading A (mine): Arthur's rule says "whoever saw it"; Sub 135 is a main build after 1745; the sheet was last edited 19:30, the sighting is 21:20, so the sheet is stale on this row. Waiting on a fix.
- Reading B: Brian says "For Vincent that sheet is the list, so don't add things from his chats". The sheet says nr on a main build, so Passed. Vincent himself opens with "one for the next list".
- Records: `b156fdcd...` (#zombie-bugs thread under `90084203...`); sheet row 9; Brian's note; Arthur's doc.
- Effect of B: Passed 13, Waiting on a fix 20; new sub-issue Done instead of Todo. Areas clear and review list do not change (Daily Gift stays Open through rows 10, 11 and is off the agenda).
- Confidence settled: about 65%. "Don't add things" is about adding reports, not about status, but the sentence sits right next to the scope rule and the "next list" phrase pulls the other way.

### F3 (major). Does "Passed" include the "pass stands until" half of Arthur's rule at all?

- Reading A (mine): "a build that counts under Arthur's rule" plus "as it stands today" brings in the whole doc, including re-sightings.
- Reading B: Brian's definition only tests the build ("ok or nr on a build that counts"). A main build counts. Re-sightings are not part of the definition.
- Records: Brian's note; Arthur's doc.
- Effect of B: rows 9 and 29 both Passed (Passed 14, Waiting on a fix 19).
- Confidence settled: about 75%. F2 and F3 share row 9; row 29 depends on F3 alone and is the cleaner test, since the sighting is not Vincent's.

### F4 (major). Row 27: does the Android 2006 sighting reopen the pass?

- Reading A (mine): the rule is "a main build made after the one it passed on". Android 2006 (15:39) was made before iOS 1745 (16:19). Pass stands.
- Reading B: the message was posted 22:40, after 1745 existed, and 2006 looks like a higher number than 1745. A reader who compares message time or build numbers, or who treats Android and iOS separately, reopens it.
- Records: `ecf80487...`; #builds posts for 2006 and 1745.
- Effect of B: Passed 11, Waiting on a fix 22, Boss Arena open reports 2. Areas clear unchanged.
- Confidence settled: about 80%. The rule text is explicit; the gap is only 40 minutes across two job counters.

### F5 (minor). Row 18: "again Android #2013" with Fix #472

Android 2013 was built 09-29 23:34; #472 merged 09-30 15:53. The build cannot contain the fix, so Waiting on QA. A reader who trusts "again" says Waiting on a fix. Settled by timestamps; confidence about 90%. ZOM-576 state does not change under my reading, so only the status, the note and the counts show it.

### F6 (minor). Row 34: "again iOS Internal #1757" with Fix #475

1757 started 18:37, #475 merged 16:09. Fix tried on main, still happens -> Waiting on a fix. Whether #475 really holds this fix does not matter; both paths give the same status. Confidence about 95%.

### F7 (minor). Rows 12 and 32: sheet names a PR, reviewer says it is not in the diff

Arthur's review comments are explicit. Waiting on a fix; ZOM-571 and ZOM-581 go to Todo. A reader who stops at the sheet and Vincent's "I was told" comments keeps In Validation. Settled; confidence about 90%. Both comments are also mirrored in Calvin's Gmail and #zombie-prs.

### F8 (minor). Rows 13 and 38: no fix in the sheet, fix claimed in a PR comment

Oliver's `#473#c_2` names both. "The bar filling before the tokens land" matches row 38 (the only row about tokens); a hurried reader could map it to row 15 or 17 (Collect & Win event bar), but #473 is the Season Pass PR. Nobody contradicts Oliver, and the automated PR summary does not mention either fix. Confidence about 85%.

### F9 (minor). Rows with no fix and nr (3, 7, 22, 26, 27, 35)

Brian says "ok or nr", so nr with no fix is Passed. Settled by the note; confidence about 95%.

### F10 (minor). Which build is "the build is there" for "ok, chat"

Calvin named 1716 and 1718 before Vincent's ok. Both are QueueManager branch builds, as is 1708. Every candidate gives the same result. Row 25's sheet wording ("does not play when another tutorial is queued") differs from the chat ("plays again even if I completed it"); status is unaffected.

### F11 (minor). Review areas

Current Trello desc: Collect & Win, Level-end rewards. Stale sources: Brian's DM of 09-29 (`345e6d1a...`), the first invite mail, the first card edit, all saying Collect & Win and Daily Gift. Leonard's update note only says Daily Gift waits; only the card says Level-end rewards came in. Settled; confidence about 90%.

Design weakness, not a fork: the stale agenda also yields 6 (Collect & Win 3 + Daily Gift 3 under my statuses). The count cannot tell the two agendas apart; only the per-row flags can.

### F12 (minor). Scope: is Marcus's glow a new report or row 12?

Marcus says the animation is fine and only the glow stays; row 12 is the icon animation restarting. New report. "Today's main build" has no number, and "about the home screen after a level" rests on "saw it 3 levels in a row". Confidence about 85%. If merged into row 12: 38 reports, Waiting on a fix 20.

### F13 (minor). Scope: the two EMPLOYEE_0016 sightings

Both are in channels, not DMs, and both match existing rows (27, 29). They are not new reports. Settled.

### F14 (minor). Rows 11 and 20 already have a ticket

Vincent's comments on ZOM-556 and ZOM-560 settle it. His DM `cfee08a8...` ("the ticket keys are in it where I opened one") is loosely at odds: he created both tickets and left both keys out. A reader who trusts the DM makes two duplicate sub-issues (21 new, 18 moved). Confidence about 85%.

### F15 (minor). Rows 31, 33 and ZOM-541 / ZOM-528

These are feature tickets (card pack VFX), not bug reports. I made new sub-issues. Low risk.

### F16 (minor). Unlabelled main commits

Oliver pushed to main 09-30 21:20, 21:36 and 10-01 05:44 ("Fix end popup"). No record ties them to a row. A solver could guess one of them fixes row 9 or 13. I ignored them.

### F17 (minor). Unpinned write details

Share role (reader or writer); "Open reports" as a count or a list; the wording of each note; new ticket keys (depend on creation order, ZOM-585 onward); child priority; whether ZOM-543's own state changes; whether moved tickets keep their assignee and priority (the "no priority, no assignee" rule is stated for new ones only).

## C. Ambiguous, contradictory, or contradicted by the data

1. Brian's "Passed" definition tests the build, while Arthur's doc has a second clause about a pass ceasing to stand. The note does not say whether that clause applies (F3).
2. "Don't add things from his chats" against Vincent's own re-sighting of a sheet row in a channel thread, posted after the sheet's last edit and after Brian's note and DM (F2).
3. "A fix ... in main that QA has not tried yet" does not say "on main". Rows 1, 2, 25 were tried and approved on a branch (F1).
4. "Share it with everyone on the review invite, Leonard too": Leonard is the organizer and already on the invite. Harmless. The mail body hides Julia as a name token; the calendar event and the To header show her address.
5. Brian's DM of 09-29 says the review is Friday and covers Collect & Win and Daily Gift. Both were superseded on 09-30; the DM was never corrected.
6. The sheet's Fix column is hearsay by its own legend ("the PR the dev told me"). It is wrong for rows 12 and 32 and blank for rows 13 and 38, which do have a fix in main.
7. Vincent set ZOM-571, ZOM-576, ZOM-581 to In Validation on the same hearsay. Only ZOM-576 is right, and for a reason he did not know.
8. Vincent's "ticket keys are in it where I opened one" against ZOM-556 and ZOM-560 (F14).
9. The legend says "ok, chat ... the build is there" without naming the build; the chat names several, all on the feature branch.
10. Deck slide 2 and the ZOM-543 description list six things the manager orders (Tutorials, Level-end animations, ...). They are not the ten areas; Brian's note gives the child names.
11. Two "builds and QA passes" docs by Arthur. The DD one says the opposite for hotfixes. "Arthur's rule" in the note does not name the game; the titles do.
12. Rows 1, 2 were found on a feature-branch build (1698) and rows 31-33 on another (1746). The rule only speaks about passes, so this does not affect status.
