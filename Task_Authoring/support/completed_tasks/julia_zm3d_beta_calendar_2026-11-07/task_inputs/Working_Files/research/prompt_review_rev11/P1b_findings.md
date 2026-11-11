# Deep recheck P1 (second sample), rerun on the revised SQL

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

SQL: sha256 1348d287ac4a105c41b9f0bf511c6664e306adcc3cf42406688a228fd4b684e7 (hash verified; prompt byte-identical to the last round).

**Result: of the six findings, 3 are settled (DR1, DR3, DR6) and 3 stay open but narrower (DR2, DR4, DR5). The new text added no new fork.** DR4 still meets the both-fair test, so it is not a UGT failure as long as the rubric accepts either value. DR2 is now one cell. DR5 cannot change a push call. The Held set, Hold until, the Collect & Win window start and all 10 push send-or-hold calls stay settled by RECORD.

## DR1 to DR6: status

| DR | Status | What changed | Does a record rule out Reading B? |
|---|---|---|---|
| DR1 C&W icon animation in Still to do | **Settled** (RECORD) | New linear comment cmt_zom465_3, Brian, 2025-09-30 18:13Z: "the Collect & Win icon does have to land before the beta, it is the one event icon with no animation. Keep it on this ticket, the master VFX list was written before that event came in." | Yes. This is a dated non-owner flag, which is what the last round found missing. With the brief's "anything flagged since this brief as still needed for it", leaving it out is no longer defensible. It also answers the P1/P2 reading: "the master VFX list was written before that event came in". Owner stays Marcus. |
| DR2 held beat's window cells | **Still open, narrower** | Brief adds: "A held beat keeps its usual windows on its row, marked held." | First window and Windows: yes, settled (Mon Oct 6 00:00 UTC; Monday windows, marked held). Weeks running: no. That is a separate column, and "none until the fix" still leaves the windows on the row. |
| DR3 Brian's moved date | **Settled** (RECORD) | Brief now: "A committed date that misses the lock moves to any time before it" | Yes. Any instant before Oct 31 00:00 UTC is valid by rule, so Oct 29, Oct 30 and "before the lock" all pass. The rubric must not lock one date. |
| DR4 window boundary figures | **Changed, narrower, still BOTH_FAIR_FIGURE** | Brief adds: "Clip anything that starts before or runs past that to those two instants." and "each opening 00:00 UTC and closing 23:59 UTC on its last day." | Settled: Season Pass first window is Oct 6 00:00 UTC, its last window closes Nov 2 23:59 UTC, and C&W ends are 23:59. Not settled: ends of non-C&W windows inside the span. The 23:59 sentence covers Collect & Win only. |
| DR5 Login Calendar, What is missing | **Still open, narrower** | Brief now: "the daily gift (Login Calendar on the push sheet, same beat)" | Identity: yes, one beat. Name: no. "same beat" does not say the name is right (see F5). The hold call is unchanged. |
| DR6 spend path | **Settled** (RECORD) | UA plan slide 2 now: "Small scale at first, any scale-up comes after the pivot call." Slide 1 no longer says "Scaled". | Yes. Slide 3 agrees: "hold the spend there until the pivot call". Slack agrees: Leonard 09-11 "when it's approved we'll start buying users at small scale". |

## Open findings

`DR# | pass | checklist section | quoted prompt sentence | record path, id and quoted value | Eval dimension | proposed score or severity`

DR2 | P1 | §2 what gets written | "If a beat ends up held, leave a note on its ticket so the owner picks it up." | brief: "A held beat keeps its usual windows on its row, marked held."; Calendar column "Weeks running"; Frederick's message: "which windows it runs in" | Unique Ground Truth | 2 if any row grades Weeks running on the held beat; no effect if none does

DR4 | P1 | §2 edge values | "the four buy weeks that start Monday the 6th" | brief: "each opening 00:00 UTC and closing 23:59 UTC on its last day" (C&W only); brief: "a different instant is not"; Season Pass spec: "production seasons reset monthly on the 1st at 00:00 UTC"; Confluence Live-Ops Calendar: "weekly reset Monday 00:00 UTC" | Unique Ground Truth | BOTH_FAIR_FIGURE; the rubric must accept either

DR5 | P1 | §2 what gets written | "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me." | PNs Beta row 13 copy: "Check the login calendar — fresh rewards are here!"; Domino sheet carries the identical row: "Login Calendar update"; match3d Assets/Scripts/UI/Daily Gift/DailyGiftProgressBar.cs line 180: "Daily Gift"; Confluence: "Same feature as Win & Collect on Domino Delights, under a different name" | Unique Ground Truth | 3; the hold call is unchanged, only the "What is missing" text differs

## Fork list

- F2 (DR2): Weekly Leaderboard, Weeks running | Reading A: W1 to W4, marked held | Reading B: none until the fix is confirmed | Basis: SILENCE on this column. "on its row" leans towards A, but an inference is not a kill. | Missing: the brief sentence also naming the weeks.
- F4 (DR4): end instant of Season Pass October and of the Monday windows (Weekly Leaderboard, Endless weekly) | Both fair: Oct 31 23:59 UTC or Nov 1 00:00 UTC; Sun 23:59 UTC or Mon 00:00 UTC. Same decision, writes and destination, and nothing ranks them. The C&W sentence supports 23:59 only by analogy. BOTH_FAIR_FIGURE; the rubric must accept either.
- F5 (DR5): Login Calendar push, What is missing | Reading A: Not Ready and WIP | Reading B: also the event name | Basis: SCOPE_GAP. "same beat" settles identity, and Reading A's best support is that the brief itself uses the label. But the row and copy are carried over unchanged from the Domino sheet, the game code says "Daily Gift", and "Win & Collect" shows that the same feature under a Domino name is a wrong name. | Missing: a record saying "login calendar" is an acceptable ZM3D name, or that it is not.

Closed since last round: F1, F3, F6.

## New and changed text tested against Slack and the other records

Slack base is unchanged, so the full read from last round stands. For this pass I rebuilt the overlay (12 SQL Slack rows; Julia's channels plus public channels, 49 files), searched it for each new sentence's terms, and tested the sentences against every candidate from last round's read.

| # | New or changed text | Reading B tried | Record tested | Can it change a cell? |
|---|---|---|---|---|
| 1 | ZOM-465 cmt_zom465_3 (Brian) | Icon "has to land" so C&W cannot start Oct 10. The Sep 30 builds (iOS #50, Android #135) do not carry it. | Brief: "cosmetic, VFX and performance gaps and analytics gaps do not hold a beat"; "not when its client PRs merged" | No. Killed. |
| 2 | Same: "the one event icon with no animation" | Axe icon also needs a Still to do line. Marcus 09-22: "I still have the axe icon" | Frederick: "things that are not in the beta"; cmt_zom465_1 "every event icon on the main menu" | No. Killed. |
| 3 | Same: "the master VFX list was written before that event came in" | Brian's 09-12 list already had "*P0 – Collect & Win*", so the sentence is wrong and the release of P1/P2 polish applies | That line continues "may need your help later, but not clear yet", and the later flag is specific to this icon | No. Killed. |
| 4 | Clip sentence | Clip touches a hold or a date outside windows | Brief: it sits under "Span and time base", and "say that instead of guessing a date" | No. Killed. |
| 5 | Held-beat sentence | Another beat is now held. Held rows imply the push sends. | Held set unchanged; row 15 is WIP, so the push holds under the brief | No, apart from F2. |
| 6 | "any time before it" | Lock is any time on Oct 31 | Spec: "locked 24h before each season opens" | No. Killed. |
| 7 | "premium strip art still shows the October range" | Art folds into Brian's handoff ("the premium track and the season theme"), so the owner is Brian, or the lock applies to it | Arthur, same comment: "Oliver is taking the date change"; "before that season opens"; brief lists "prod deploy, config or player-facing art" as separate kinds | No. Killed. No Julia-visible Slack mentions the strip. |
| 8 | Douglas 09-26: "Both tables are updated." | The Sep 19 token-count ask is still open | Dated before the brief: "flagged since this brief" | No. Killed. It also closes sweep row 17 directly. |
| 9 | "rides the next store build" | Next store build means the Sep 30 builds, so the fix needs tracking | Same sentence: "nothing has to land for the beta" | No. Killed. |
| 10 | Robert's DM lost "my later word" | His pull no longer overrides his approval | Brief: "if he takes that back his later word is the one that counts"; DM: "pulling my ok. Take it off the beta calendar" | No. Killed. |
| 11 | "Two things on top of the brief." | The brief's naming rule still fails no-name copy | Thread: "Copy that does not name the game at all is fine to go out" | No. Killed. |
| 12 | "approved ... for one week of the beta", "lands in time" | No live effect once withdrawn | As row 10 | No. Killed. |
| 13 | "Beta-cohort buy" and the UA slide 2 rewrite | Conflicts with a Slack plan to scale | No Slack record plans a scale-up; Leonard 09-22 ties the decision to "clean data from a tech-stable beta" | No. Killed. |
| 14 | ZOM-504, ZOM-542 state, ZOM-563 and Trello wording | Beat or Still to do effect | ZOM-504 "Visual only"; ZOM-542 dated before the brief; Teams has no window; Trello text keeps "The weekly rollover does not wait on them" | No. Killed. |

## Sweep rows whose quote changed (the other 28 of 31 rows rest on unchanged statements and stand)

- Row 17 C&W reward tables: now settled directly by Douglas in thread: "Both tables are updated." Julia is not a member of this public channel (visibility unverified), but no cell depends on it now.
- Row 18 lightSweep: quote is now "so it rides the next store build and nothing has to land for the beta".
- Row 25 Halloween: Robert's line is gone from the DM. The kill now rests on the brief's rule plus his DM (test 10).

## Limits

- No line-by-line Slack reread this round: the Slack base did not change, so only the changed rows and term searches are new. Last round's delegated reads and partial canvas reads stand as stated there.
- review_rev10 was not opened in this pass; tooling was rebuilt under R11/work.

## Passed on, no effect on any cell

- Last round's Trello note is resolved in the SQL: the action no longer names the list.
- Brief style offsets were rechecked: all 9 heading ranges match the new text.
- New Slack row: the parent exists (0069f6143e89802993b39e442d3baeb2), the id is new, Douglas is a channel member, and reply_count goes from 2 to 3.

Platform defects: none
