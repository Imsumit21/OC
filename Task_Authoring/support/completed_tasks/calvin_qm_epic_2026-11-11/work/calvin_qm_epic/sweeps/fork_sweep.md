# Fork sweep (Unique Ground Truth check)

Reviewer: independent, did not write the design. Inputs: `plan/seed_text.json`, `plan/reports.py`, `plan/truth_sketch.json`.
Base read only through `Task_Authoring/tools/hg.py` (synth-cut universe). Slack pointers are `channel /index` in `messages/<channel>/2025-09.json`; GitHub and Linear pointers are in `data.json`.

## Summary

- My row-by-row answers reproduce the stated totals: **13 Passed / 6 Waiting on QA / 21 Waiting on a fix / 1 Clear area (Zombie Lane) / 8 holding**. The arithmetic is right under the intended reading.
- The intended reading is not the only defensible one. I found **5 BLOCKING forks**, 7 moderate ones and several wording points. Three of the blocking ones come from real base records the plan does not account for.
- BLOCKING:
  1. **Row 32**: base PR #475 text and a base commit title say the close button is locked during the animation; only the planned review comment says it is not. Nothing in the rules says which wins.
  2. **"A merged PR covers it" is open-ended.** The ELSE trap (rows 15/16) forces the solver to judge coverage from PR text for rows with a blank Fix cell. The same test gives a fair "Waiting on QA" for **row 19** (PR #472) and **row 4** (PR #465).
  3. **Arthur's rule wording** ("a build cut from main, Internal or Submission") can be read two other ways: one makes rows 1/5/25 Passed, the other makes rows 22/23/24/26 not Passed (0 Clear areas).
  4. **Hub count "how many hold the review"** reads naturally as areas (answer 2), not reports (answer 8).
  5. **Extra in-scope report in base**: Brian's 26 Sep Collect & Win canvas note about the main menu UI is a fair 41st report in a gate area. The same canvas shows rows 15/16 still unticked after Vincent said it was up to date with the merged PR.
- Non-fork contradictions with the base (will fail a coherence check): sheet saved 17:40Z cites build #1757 finished 18:43Z; rows 15/16 "Found on Android #2004" (29 Sep) but the base canvas lists them on 26 Sep; rows 1/2 found-on builds are later than the base chat reports; ZOM-573/ZOM-578 are dated before base ZOM-566 (30 Sep 16:26Z).
- Verified fine: main/branch split of every cited build, PR merge times, #459 merged 24 Sep 23:06Z ("went to main on the 24th"), the input blocker Brian parked (base, D0770ET6WBW /256), no base go/no-go date or build rule that competes, "In Validation" exists as a ZOM state, seed ids `#472#rc_1` / `#475#rc_1` and ZOM-567..586 are free.
- Not checkable from the three inputs: the planned states of ZOM-567..586, and any planned chat lines behind "ok, chat" (the base chat already supplies them, see below).

## Rule-by-item table

Rule sentences: S1 Passed = Vincent's ok/nr on a build that counts under Arthur's rule, unless the raiser later says it is back. S2 Waiting on QA = not passed, a merged PR covers it. S3 Waiting on a fix = everything else, also came back. H = holds if not Passed and area in the invite (v2: Collect & Win, Level-end rewards).
Verdict: OK = one answer; FORK-B = blocking; FORK-M = moderate; W = wording only.

| # | Area | My result | Deciding record(s) | Competing reading | Verdict |
|---|---|---|---|---|---|
| 1 | Tutorials | QA | "ok, chat" = base D06UPGF5PQV /169 (25 Sep 17:15Z "Looks ok to me") after /158 (#1718). #1718 is branch `QueueManager` (C05433XK267 /926). #465 body names the queued-tutorial fix | Rule-wording reading B (Internal counts) gives Passed. Deck "QA passed" is a decoy only | FORK-B (wording, F3) |
| 2 | Tutorials | Passed | ok iOS Internal #1727, main, change list "Merge PR #465" (C05433XK267 /959, 25 Sep 22:21Z) | none. Found-on #1974 (23:13Z) is later than base chat /140 (22:00Z) | OK |
| 3 | Tutorials | Passed | ok #1727 main | #465 body does not name the hand pointer; irrelevant once Passed | OK |
| 4 | Tutorials | Fix | blank fix, blank re-test | #465 body "reducing stuck or repeated tutorials", merged after found-on #1974; #474/#467 tutorial fixes. A solver can call it covered | FORK-M (F2) |
| 5 | Level-end | QA, holds | chat names #1716 (/156) and #1718, both branch `QueueManager` (/922, /926); #465 body "not play coin animation again" | Reading B gives Passed. Brian raised the same bug (D0770ET6WBW /258), a duplicate | FORK-B (F3) |
| 6 | Level-end | Fix, holds | blank | #472 "shortening input-block time" is loose | OK |
| 7 | Level-end | Passed | nr iOS Internal #1745 main (/1058) | Kin of the parked input blocker (chat /120-/121); the exclusion sentence could be stretched to it | W |
| 8 | Level-end | Fix, holds | blank | none | OK |
| 9 | Daily Gift | Fix, no hold | nr #1745 then `reopen` (C08R27X0EAH 21:20Z, Android Submission #135 main, finished 20:13Z /1124) | "don't add things he only said in chat" vs a chat-only reopen: weak. Old gate (v1, `gate_old`) would make it hold | OK |
| 10 | Daily Gift | Fix | blank | #472 "prevents premature progression during reward animations" is Collect & Win specific | OK |
| 11 | Daily Gift | Fix, ticket ZOM-573 | `alias_gift` comment names build 1727 and the same symptom | #471 / Samuel's "Fixing UI Elements on Daily Gift" commits are layout only | OK |
| 12 | Season Pass | Fix | `inline` (#472 review) says tokens are not in it; #472 body silent | Sheet Fix "#472" (legend: the dev said so) and `claim`. Base walkthrough (pull_request_comments/655) shows a new 0.2 s wait before `PlaySeasonPassToken` | FORK-M |
| 13 | Season Pass | Fix | blank | #473 (merged 30 Sep 15:41Z) "Season Pass popups... proper queuing" is loose | OK |
| 14 | Season Pass | Fix | blank | none | OK |
| 15 | Collect & Win | QA, holds | #470 body "After level completion, it first shows placeholder icon and progress..."; `else_dm` | Base canvas C3DD99314033 /69 still unticked while Vincent says the canvas is up to date with the merged PR (C09EVVCFHKR /94-/95, 16:38Z) | FORK-M (F5) |
| 16 | Collect & Win | QA, holds | #470 body "In Boss arena and endless mode, the c&w UI is visible" | Same canvas, /72 unticked. Title mentions Boss Arena/Endless; sheet Area column settles the area | FORK-M (F5) |
| 17 | Collect & Win | Passed | ok iOS Internal #1754 main, "Merge PR #472" (/1107, 16:01Z) | none | OK |
| 18 | Collect & Win | QA, holds | sheet Fix #472; body "waiting for Collect & Win status" | `inline` says "This only waits for the Collect & Win status though": "only" can be read as not covering the panel order | FORK-M |
| 19 | Collect & Win | Fix, holds | blank | #472 body "Prevents premature progression during reward animations", merged after found-on #2013; #470 "grand-prize items now reflect claimed state" | FORK-B (F2) |
| 20 | Win Streak | Fix, ticket ZOM-578 | `alias_streak` comment (Android 1984, chest over rewards) | none | OK |
| 21 | Win Streak | Fix | blank | none | OK |
| 22 | Zombie Lane | Passed | nr Android #2006 main (/1053) | Reading C: "Match3D Android" job is neither Internal nor Submission. Found on iOS, checked on Android (rule silent) | FORK-B (F3) |
| 23 | Zombie Lane | Passed | ok Android #2006 main | Reading C | FORK-B (F3) |
| 24 | Zombie Lane | Passed | ok Android #2010 main (/1069) | Reading C | FORK-B (F3) |
| 25 | Boss Arena | QA | base chat /170 "Boss arena as well" on #1718 branch; #465 body "repeated tutorials" | Reading B gives Passed. Coverage rests on a generic bot line plus the sheet Fix cell | FORK-B (F3) |
| 26 | Boss Arena | Passed | nr Android #2006 main | Reading C | FORK-B (F3) |
| 27 | Boss Arena | Passed | nr #1745 main | Input-blocker kin, as row 7 | W |
| 28 | Endless | Fix | blank | none | OK |
| 29 | Endless | Passed | ok iOS Internal #1750 main (/1084) | none | OK |
| 30 | Endless | Fix | blank | none | OK |
| 31 | Card packs | Passed | ok iOS Internal #1757 main (/1119) | none. Timestamp clash with the sheet (see below) | OK |
| 32 | Card packs | Fix | `inline2` (#475 review) "not covered here" | #475 body "Temporarily disables the close button during transitions"; commit "Fix not allowing multiple tap during card animation" (/1116); walkthrough (pull_request_comments/658) "CloseScreen... disables close button" | FORK-B (F1) |
| 33 | Card packs | Passed | ok #1757 main | none | OK |
| 34 | Card packs | Fix | blank, ZOM-586 | Base ZOM-539 "Implement Red Dot for Cards and Shop" is a feature ticket | OK |
| 35 | Tutorials | Passed | nr #1745 main | none | OK |
| 36 | Level-end | Fix, holds | blank | none | OK |
| 37 | Win Streak | Fix | blank | Base ZOM-560 is a different freezer bug | OK |
| 38 | Season Pass | Fix | blank | Base ZOM-526 "Tokens traveling to live-ops" is a feature ticket | OK |
| 39 | Season Pass | Fix, new sub-issue | `mail` (Robert, 28 Sep) | Area is the solver's call; Season Pass is natural | OK |
| 40 | Card packs | Fix, new sub-issue | `filt_dm` (Marcus, 30 Sep 18:30Z); main builds with #475 exist by then (#1756, Android #2025) | Area could be Level-end rewards (a gate area, holds 9). Base ZOM-528 / ZOM-541 are the cards-to-inventory tickets, both In Progress and assigned to Calvin | FORK-M |

Areas (Clear when all reports Passed):

| Area | Reports | Not passed | Roll-up | Note |
|---|---|---|---|---|
| Tutorials | 1,2,3,4,35 | 2 | Open | |
| Level-end rewards | 5,6,7,8,36 | 4 | Open | gate area |
| Daily Gift | 9,10,11 | 3 | Open | was a gate area in v1 |
| Season Pass | 12,13,14,38,39 | 5 | Open | |
| Collect & Win | 15-19 | 4 | Open | gate area |
| Win Streak | 20,21,37 | 3 | Open | |
| Zombie Lane | 22,23,24 | 0 | Clear | rests entirely on Android main builds (F3) |
| Boss Arena | 25,26,27 | 1 | Open | becomes Clear under reading B |
| Endless Mode | 28,29,30 | 2 | Open | |
| Card packs | 31-34,40 | 3 | Open | |

Recount: Passed 2,3,7,17,22,23,24,26,27,29,31,33,35 = 13. QA 1,5,15,16,18,25 = 6. Fix = 21. Holding 5,6,8,36,15,16,18,19 = 8. Matches the plan.

## Forks found

**F1. Row 32, does #475 cover it? BLOCKING.**
Three base records say the close button is handled: the PR body ("Temporarily disables the close button during transitions to prevent accidental skips", pull_requests/2380), the bot walkthrough (pull_request_comments/658) and the commit title in the build change list (C05433XK267 /1116). The sheet's Fix cell also says #475. Only the planned `inline2` says a single pack can still be closed. The rule sentence "a merged PR covers it" does not say whose word decides. "Waiting on QA" is defensible: the PR claims the fix, so QA re-testing is the natural next step. Row 12 has the same shape but is safer because the #472 body never mentions pass tokens.

**F2. "A merged PR covers it" has no stated test. BLOCKING (structural).**
The legend says a blank Fix cell means only "nobody told me", and rows 15/16 are designed so that the solver must find coverage in PR text. That licenses the same search for every blank-Fix row:
- Row 19 (grand prize popup closable before the reward lands) against #472 "Prevents premature progression during reward animations by waiting for Collect & Win status". Found on #2013 (29 Sep 23:34Z), PR merged 30 Sep 15:53Z. Fair "Waiting on QA"; changes counts to 7 / 20 and the state to In Validation.
- Row 4 (win streak tutorial freezes at level 20) against #465 "reducing stuck or repeated tutorials". Row 25 is accepted as covered by the same generic line.
- Weaker: rows 6, 10, 13 and report 39 against #472 / #473.

**F3. Arthur's rule sentence. BLOCKING (wording, up to 7 rows).**
"For ZM a QA pass only counts on a build cut from main, Internal or Submission."
- Intended: any main build, whichever job.
- Reading B: three things count: main, Internal, Submission. "Match 3D iOS Internal #1718" is an Internal build, so rows 1/5/25 are Passed (16 / 3 / 21, Boss Arena Clear, holding 7). The second sentence about branch builds pushes back, but the build is literally named Internal.
- Reading C: main builds of the Internal or Submission jobs. The Android job is named "Match3D Android" (no "Internal"), so rows 22/23/24/26 do not count (9 Passed, 0 Clear areas).

**F4. Hub count. BLOCKING (wording).**
"how many areas are clear and how many hold the review" parses as areas that hold the review: 2. The note defines "holds" per report: 8. Both are fair answers to a graded count.

**F5. Base Collect & Win canvas. BLOCKING for scope, moderate for rows 15/16.**
Canvas channel C3DD99314033 ("Collect&Win issues", public, Calvin is not a member), items added 26 Sep 14:37Z by Brian and Vincent (C09EVVCFHKR /89):
- /69 and /72 are rows 15 and 16, both unticked. On 30 Sep 16:38Z, after #470 merged, Owen asks "is the canvas up to date with the latest PR merged into main?" and Vincent answers "that one, it is" (/94-/95). An unticked item on an up-to-date list can be read as "still there after the fix", which is Waiting on a fix. The sheet's blank re-test ("not re-tested yet") argues the other way.
- /78 with Brian's reply /80: "In the main menu, the UI also looks quite short compared to the screen." Raised by somebody else, after the 24th, about the home screen, written on a canvas ("wherever they wrote it"). A fair 41st report in Collect & Win: 22 waiting on a fix, 9 holding.
- /98 Vincent: "none of them blockers and doesn't affect the submission", which sits badly beside an invite that says open Collect & Win items hold the go/no-go.

**F6. Other scope candidates since the 24th. Moderate.**
- ZOM-565 "Endless Horde Start Screen Vfx" (Marcus, 25 Sep, assigned to Calvin, issues/3642): "when you get back to the screen after playing the endless mode we want to see the bar moving".
- Marcus in #zm-animations (C09ATAJ220H /161-/171, 29 Sep): cards should fly to the inventory over the main menu. Settled in the thread, but it is the same subject as report 40.
- Brian's DM about the coin animation (D0770ET6WBW /258) duplicates row 5; the rules never say to merge duplicates.

**F7. State mapping. Moderate.**
"If its state does not match" does not say what matches. A ticket In Progress for a Waiting-on-a-fix report can be left alone or moved back to Todo. Depends on the planned states of ZOM-567..586, which are not in the inputs.

**F8. Report 40 area and ticket. Moderate.** See table. "If a ticket already has the report" could pull in ZOM-541 or ZOM-528.

## Base records that offer another answer

| Record | What it says | Effect |
|---|---|---|
| github pull_requests/2380 (#475 body), pull_request_comments/658, slack C05433XK267 /1116 | Close button disabled during the card animation | Row 32 Waiting on QA (F1) |
| github pull_requests/2377 (#472 body), pull_request_comments/655 | Premature progression during reward animations prevented; wait before season pass token | Rows 19, 12 (F2) |
| github pull_requests/2369 (#465 body) | "reducing stuck or repeated tutorials" | Row 4 (F2) |
| slack C3DD99314033 /69 /72 /78 /80; C09EVVCFHKR /89 /94-/98 | Canvas items, unticked, "up to date", "none of them blockers" | Rows 15/16, extra report, hold story (F5) |
| slack C05433XK267 build posts | Job names "Match 3D iOS Internal", "Match3D Android", "Match3D Android Submission", each with the branch | Readings B and C of Arthur's rule (F3) |
| linear issues/3642 (ZOM-565), issues/3616 (ZOM-541), issues/3602 (ZOM-528), issues/3600 (ZOM-526) | Feature tickets on the same subjects | Scope and "existing ticket" (F6, F8) |
| slack D0770ET6WBW /256 | Brian: "the input blocker is not a problem right now" | Supports the plan: the parked item is identifiable |
| slack D06UPGF5PQV /134-/170 | Real QA chat for rows 1, 2, 3, 5, 25 | Supports "ok, chat" on branch builds; contradicts found-on for rows 1 and 2 |

Contradictions that are not forks but should be fixed:
- Sheet `at` 17:40Z, yet rows 31/33 cite iOS Internal #1757, posted 18:43Z (C05433XK267 /1119). #1756 (about 16:15Z, "Merge PR #475", /1115) fits.
- Rows 15/16 "Found on Android #2004" (29 Sep 12:40Z, branch `winAndCollect`); the canvas lists both on 26 Sep 14:37Z.
- Row 1 found on #1710 and row 2 on #1974 (both 24 Sep about 23:12Z); Vincent reported both at 21:36Z-22:00Z that day (chat /134, /140) on pre-merge branch builds.
- ZOM-573 dated 26 Sep and ZOM-578 dated 23 Sep, with comments on 29 Sep, but base ZOM-565 is 25 Sep and ZOM-566 is 30 Sep 16:26Z. Keys 567+ cannot predate that. Sheet keys ZOM-567..572 for bugs from 24-25 Sep have the same problem.
- ZOM-543's base description lists six sub-areas that differ from Brian's ten children (issues/3618). The note overrides it; no fork.

Checked and found nothing competing: Trello ("QA pass", "branch build", "cut from main"), calendar and mail ("go/no-go"), Drive and Sheets ("queue manager", "pass sheet", "QA pass"), Linear for the main report terms (Daily Login, daily gift, home buttons, grand prize, freezer, Collect & Win, season pass, card pack, input block; the "Nathan" scan hit its match limit).
Not swept: the Brian-Vincent Turkish DM (D0770ET1HV2, Calvin is not a member) and Slack outside September 2025.

## Wording problems in the rules

| Phrase | Two readings | Severity |
|---|---|---|
| `rule_comment`: "a build cut from main, Internal or Submission" | see F3 | BLOCKING |
| `hub`: "how many areas are clear and how many hold the review" | areas (2) or reports (8) | BLOCKING |
| `epic_note`: "a merged PR covers it" | PR text, sheet Fix cell, dev's word or reviewer's word; none ranked | BLOCKING (F1, F2) |
| `epic_note`: "anything somebody else on the team raised... about what shows on the home screen after a level" | bugs only, or also layout and VFX requests; "after a level" strict or loose; duplicates of sheet rows | moderate (F5, F6) |
| `epic_note`: "since the queue manager went to main on the 24th" | from the merge (23:06Z) or the whole day; ZOM-564 was filed 16:38Z that day (out of scope either way) | minor |
| `epic_note`: "If its state does not match" | see F7 | moderate |
| `epic_note`: "The input blocker I already parked, leave it out too" | one parked item, or any input-blocking row (7, 19, 27, 32) | minor |
| `epic_note`: "don't add things he only said in chat" | new reports only, or also chat-only status changes such as `reopen` | minor |
| `epic_note`: "an area the review invite lists" | two invites exist; v2 says "now", so v2 | fine |
| `epic_note`: "Open reports" column on tab Areas | a count or a list | minor |
| `inline`: "This only waits for the Collect & Win status though" | limits the PR to row 17, or only excludes the tokens | moderate (row 18) |
| `legend`: "ok, chat means I told the dev ok in our chat, the build is there" | fine for rows 1 and 25; for row 5 the chat names #1716, then #1718, and has no explicit ok for the coin bug. Both are branch builds, so one answer | fine |
| `epic_note`: Passed needs "Vincent's ok or nr" | reports from others can never be Passed; consistent for 39/40 | fine |
