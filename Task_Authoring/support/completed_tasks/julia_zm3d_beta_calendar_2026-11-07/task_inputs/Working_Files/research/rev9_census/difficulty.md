# Difficulty review: Julia ZM3D beta calendar, revision 8

Task folder `Task_Authoring/task_inputsS`. Clock Oct 1, 2025 (synth-cut). Medium mode, Long Horizon, 30 slots, weight 102.

## Bottom line

- **Pass rate.** I expect about **79% on the real verifier** (about 75% on the 30 slots alone). My plausible range is 72 to 85. That clears the Medium cap (under 85%) about nine times in ten and your under-80% target about two times in three. Under 70% is unlikely without the changes below, and still unlikely with them.
- **Calls.** I expect a median of about **135 counted calls per run**, ranging from about 95 to 210. The six-run average should clear 100 and probably 130. **Every run at 130+ is unlikely** (about 3 to 5%).
- **Spread is the risk nobody has priced.** Population SD is likely 0.06 to 0.08, under the 0.1 floor.
- **Where the difficulty sits.** It is in five places: the two inline PR notes, the Confluence lock chain, the thread reply under the ask, ZOM-465 and the leagues re-test. About 55 of 102 weight is easy. Four rules that look live are in practice default-right or stated in the brief.
- **Best moves.** Re-arm those four rules with wording changes and one record move (section 3). Together they take the verifier estimate to about 74%. None adds a rule or a graded item, except that the fourth option takes S07 back to weight 5.

**How far to trust this.** No run exists on this task. Every per-slot figure below is my judgement, anchored on read habits measured on other tasks. The simulation behind the averages only combines those judgements (scratch script `/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/rev9/mc.py`). Its intervals show my assumptions, not measured error. The biggest single unknown is how often runs open inline comments: each 10 points there moves the average about 1 point.

## Measured read habits used here

| Carrier | Measured on Opus 5.5 | Source |
|---|---|---|
| Inline PR comments, nothing points there | 4 of 20 runs read them on early PRs; 1 of 20 reached the late PR; in the final batch 1 of 6 runs made any inline call | Douglas `01a_Hardening_Report.md`; my count of its six trajectories |
| Inline PR comments, the rule names the review | #265 read by 5 to 6 of 6 in later batches (0 of 3 in the first); #271 by 5 of 15; #243 and #244 by 10 of 15 | Julia `01a_Hardening_Report.md` |
| Thread reply under a DM ask | Read by 4, 1, 3 and 5 of 6 across four batches (13 of 24) | same |
| Linear comments | Sweeps run wide: 73 to 146 distinct tickets for a 17-row register (Douglas), 244 to 942 (Julia) | my count of the trajectories |
| Judgement and rule application | Every judgement trap resisted in 22 of 22 runs; the only failures were records never opened | Julia report |
| De-named corrections | Missed by 6 of 6, SD 0.016 | Frederick Q4 README |
| Mail with the fact in the newest hit | Met by every run | Julia report |

## 1. Slot by slot

"Opens" is the fewest records a run must open to get the slot right. P is my estimate of a run passing.

**Likely easy: 55 of 102 weight**

| Slot | W | P | Opens | Where | Why |
|---|---|---|---|---|---|
| S04 Quests runs | 5 | .95 | 2 | Central brief, push sheet | The brief names the quest rollover outright, so T3 is not a trap |
| S05 Daily login runs | 5 | .94 | 2 to 3 | Central brief, push sheet, ZOM-556 comment | Same, and "wrong counters" do not hold |
| S02 Plague Race four weeks | 5 | .92 | 0 to 2 | Thread reply, top-level DM | Default-right: a run that never meets the approval still writes four weeks. One "Halloween" or "one-off" search returns approval and withdrawal together |
| S01 C&W Fri Oct 10 | 5 | .87 | 3 | Central brief, calendar event | The brief puts C&W, its cadence and the pre-empted window beside the release rule, so #470's inline note is not needed |
| C01, C02, C04 run | 3 each | .95, .94, .94 | 2 to 4 | Brief, ticket comments | The brief lists exactly what does not hold |
| C05 C&W runs | 3 | .93 | 1 | Central brief | "Starts late, it is not held" |
| P01, P02, P06 old title | 3 each | .95 | 2 | Brief, push sheet | Rule plus a cell every run reads |
| P03, P07 WIP | 3 each | .96 | 2 | Brief, push sheet | Same. Opus reads the second status column |
| P04, P05 no-name copy | 3 each | .85 | 2 to 3 | Brief, sheet, thread reply | Default-right: "names the game only as" does not fail copy that names no game, so about 70% send without the reply |
| W01 DM, W04 ZOM-78 link | 1 each | .98, .96 | 1 | Ask | Named destinations |

**Coin-flip: 37 of 102 weight**

| Slot | W | P | Opens | Where | Why |
|---|---|---|---|---|---|
| W02 reply names the late start | 3 | .81 | 3 | Follows S01 | Carried into the reply when S01 is right |
| S07 login nothing left | 1 | .75 | 0 to 1 | Default empty | Failure is a run writing the login push row into this cell |
| S03 leagues held | 5 | .74 | 3 | Ticket comment, then another channel | Vincent's post is the newest root in #zombie-match3d and says "weekly leaderboard". The prompt's "if a beat ends up held" sends runs looking |
| W05 hold note on ZOM-429 | 3 | .68 | 3 | Follows S03 | Same fact plus a write |
| V01 exactly seven beats | 3 | .64 | 2 | Thread reply | Zombie Lane is off only in the reply; a run may also add a "Halloween off" row |
| W03 reply says Halloween off | 5 | .61 | 3 | Top-level DM, then the reply | Must find it (.82) and choose to say it (.82) |
| S11 C&W icon, Marcus | 5 | .59 | 2 | Ticket comment on another beat's ticket | ZOM-465 is titled "Endless Mode Master VFX Ticket". The Linear sweep usually reaches it |
| V02 ten push rows | 3 | .54 | 1 | Thread reply | Needs the reply, about 55% |
| S10 November config | 5 | .50 | 4 | Mail, then Confluence body | The slip mail is the newest hit, so it is met. The gate is the 24h lock, which only the spec page states |
| W06 reply to Brian | 1 | .49 | 4 | Follows S10 | No lock found, no reply |
| W07 reply moves the date | 3 | .45 | 4 | Follows W06 | Same chain |

**Likely missed: 10 of 102 weight**

| Slot | W | P | Opens | Where | Why |
|---|---|---|---|---|---|
| S08 vials, Claire | 5 | .25 | 3 to 4 | Inline PR comment on #468 | Nothing points at inline comments. Arthur's review body is empty. The note comes after 37 CodeRabbit comments, about 80 KB of bodies and 65 KB of hunks, so it may spill |
| S09 premium strip, Oliver | 5 | .21 | 3 to 4 | Inline PR comment on #472 | The PR title is about the queue manager, and among seeded records only `cmt_zom526_3` names it. The note is alone there, so whoever opens it cannot miss it. Base Slack has no "premium strip" text |

**Expected weight lost, 25.9 of 102:** inline notes 7.7, lock chain 4.7, thread reply 3.4, Halloween 2.4, leagues 2.3, icon 2.1, small slips 3.4.

**Two corrections to the working notes.**

- **T11.** Moving the strip note did not make S09 easier to reach, as dossier §11 expects. Runs called the rev 7 carrier (`github_get_issue_comments`) 17 to 25 times each on Douglas and the rev 8 carrier 0 to 6 times. What rev 8 lost is independence: S08 and S09 now pass or fail together. That helps SD and only hurts pattern concentration.
- **The 154 floor predicts nothing about real runs.** 78 of the 154 are per-PR calls, and real runs make 0 to 9 inline calls. The brief's cohort is also Aug-Sep while the 39 PRs start Jul 1, so at least four are outside it.

## 2. Realistic pass rate and calls

| Scenario | Mean | Under 85% | Under 80% | Under 70% | SD median | SD at or above 0.1 |
|---|---|---|---|---|---|---|
| 30 slots as written | 74.6% | ~100% | 90% | 14% | .083 | 26% |
| Real rubric, about 45 more weight (my model) | **78.6%** | 97% | 67% | 1% | .066 | 7% |

I would state those more loosely than the simulation does: about 90% under 85, about 60% under 80, about 5% under 70.

**Why the verifier lands above the slots.** The sheet has columns the 30 slots do not read (Windows, Hold until, Push, Send, Segment, English copy) and four held push rows with no slot. `/rubric` requires one row per target: Frederick Q4 went from 57 to 102 rows and Robert from 115 to 136. Those rows are mostly easy. S04 and S05 also read as rule applications, which the /rubric weight bands put at 3 rather than 5. That lowers the mean slightly but does not offset the added rows.

| Completed task | Mode | Rows / weight | Average | SD | Counted calls | Writes per run | What set the result |
|---|---|---|---|---|---|---|---|
| Douglas sign-off | Medium | 76 / 314 | 56.3% | .117 | 163 to 238 | ~24 | Hidden notes decided ticket verdicts that fan out to many rows; 17 all-fail |
| Q4 commitments | Easy | 102 / 350 | 71.0% | .016 | 151 to 212 | ~90 | Five de-named records, all missed by every run |
| Bridge pipeline | Medium | 40 / 168 | 77.7% | .106 | 109 to 150 | ~50 | Three independent off-path corrections, 12 revisions |
| Card spend | Medium | 63 / 243 | 78.3% | .054 | 556 to 675 (raw) | ~10 | Two unopened mails |
| Handover | Medium, Normal | 37 / 119 | 80.8% | .161 | 68 to 108 (raw) | ~7 | Hidden authorities, bimodal runs |
| Julia ZM baseline | Medium | 81 / 173 | 83.8% | .099 | 357 to 1209 | ~20 | Same persona and tools; thread and inline carriers only, seven hardening rounds |
| Robert wind-down | Easy | 136 / 500 | 85.7% | .034 | 116 to 143 | ~44 | About 100 rows passed by every run |

This task is shaped most like Bridge: a few independent off-path facts. 24 of 102 weight sits fully off path, close to the 26% mechanism-dependent weight that `12_Difficulty.md` flags as too small to get under a cap. It has no fan-out of the Douglas kind, so 56% is not a fair comparison. The history also leans upward: Julia and Bridge both needed several rounds, and N2's first pre-check read about 97%. I would treat 79% as central and not count on the low side.

**Calls.** Across tasks, reads outside a per-record sweep run about 30 to 100 per run, typically 50. This task has about 10 writes, among the lowest of the Long Horizon comparators, and writes supplied the horizon on Bridge, Q4 and N2. So a run needs about 70 sweep calls to reach 130.

- **What will sweep:** Linear comments (18 cohort tickets, 97 open, and Opus over-reads) and PR reviews (the brief's change-request clause is the only per-PR mandate; Douglas runs made 14 to 23).
- **Estimate:** per run p10 95, median 134, p90 about 210, with about a 12% chance of a subagent sweep adding 60 to 160. The six-run average is about 140.
- **Probabilities:** average at or above 100 about 99%, at or above 130 about 70%, every run at 130+ about 3 to 5%.

The platform gate is met. Your every-run target is not something this design can promise, and I see no clean fix (section 3).

**/hardness.** One typical run misses both inline notes and probably one more chain, which reads as a 3 and sometimes a 4. I put a 1 or 2 at about 20%, from a run that opens both the thread and inline comments.

## 3. Revision 9 and the levers

**What the planned revision does.** If placed and worded well it costs about 0.5 to 1.5 points. No slot penalizes an extra still-to-do, so settling a decoy changes almost no graded cell. It mainly removes residual noise on C01, C02, C04, S04, S05 and S07, which lowers SD a little. If worded badly it costs far more. In the simulation, a still-to-do rule that points runs at reviews lifts the verifier estimate by about 2.5 points (about 3 on the slots), matching what happened on #265.

| Settling item | Put it here | Not here | Why |
|---|---|---|---|
| ZOM-534 fix | A second person's note on ZOM-534 itself | A Vincent post in #zombie-match3d | It would pull quest readers next to his leagues re-test and lift S03. The fix is client commit `47c65623e7` on main since Sep 15, so "in the submission builds" is true |
| Leonard's S23 freeze | Reply under his post `1758420497.482989` in #zombie-bugs | The brief | Neutral for scoring |
| #477 title change | A comment on ZOM-566 | Anything on #477 | #477 is the one open C&W PR. A human note on GitHub teaches runs that PR notes carry still-to-dos, and it leads to inline comments on #468 and #472. It also stays clear of SC-18 |

Wording limits for revision 9:

- No word in the still-to-do or hold rules should point to a place: not review, PR, inline, comment, note, ticket or re-test.
- No settling note should say "the only thing left is X". Any such list hints at vials, icon or strip.
- **Keep "An unresolved change-request review blocker on an in-scope live-ops PR from that cohort does hold it" verbatim.** It is the only per-PR mandate. Losing it costs 15 to 35 real calls and takes surface 2 out of the budget (154 becomes 115, under the 130 floor).

**Ranked levers.** Each re-arms an existing rule. Points are at verifier level, from the 78.6% base.

| Rank | Lever | Record that changes | Effect | Fork check | Risk |
|---|---|---|---|---|---|
| 1 | Take the search words out of Robert's withdrawal, so it sits in a DM runs do not open by default | Slack `669d15f685f158633e56302160957f1e`, first sentence only | −1.8. S02 .92 to .65, W03 .61 to .37. S02 stops being default-right | One themed prop set exists, and Robert's approval coined the phrase. The sentence the platform cites stays verbatim | Low |
| 2 | Make the brief's naming sentence say what the design assumes, so Frederick's reply carries P04 and P05 | Brief `f_7c3e91a4d2b85f60e1a9c4`, Push copy | −1.0. P04, P05 .85 to .60. Thread reply becomes worth 12 weight | Reply stays verbatim, is later and is by the same author | Low |
| 3 | Separate C&W from the release rule in the brief, so which beat waits needs #470 or a real inference | Same brief, two sections | −1.2. S01 .87 to .67, W02 .81 to .67 | `#470#rc_10` names C&W as DEV-only and the others as on prod. Calendar event unchanged | Low to medium |
| 4 | Move the frame completion off its ticket, so the ticket reads wrong by default | ZOM-432, `cmt_zom432_2`, one new Slack post | −0.7, and a new independent failure pattern | Later dated, by the ticket's own assignee | Medium |

All four together: about **73.9%** on the verifier and 68% on the slots. Under 80%: about 95%. Under 70%: about 16%. SD median .077, SD at or above 0.1 about 18%.

**Exact changes**

1. **Withdrawal.** Change "Coming back on the Halloween one-off: pulling my ok." to "Coming back on the themed prop set I okayed in Martin's thread: pulling my ok." Leave the rest untouched, including "Take it off the beta calendar", so a "beta calendar" search, a `from:Robert` search or a DM read still reaches it. That keeps it partial, not a Q4-style 0 of 6. Follow-on: manifest `facts` entry `plague.weeks` (its value text no longer appears in the home record), T2 `discovery_order`, solver anchor, dossier §3. Optional second step only if a pre-check shows this is too easy: delete ", and if he takes that back his later word is the one that counts" from the brief. That clause announces the retraction, but reviewers have cited it, so treat it as its own decision.
2. **Push copy.** Change "names the game only as Zombie Match 3D and events only by their ZM3D names" to "names the game as Zombie Match 3D and events by their ZM3D names". Exactly two rows flip for a run that skips the reply (Lives recharged, 7-day lapse). Follow-on: `style_runs_json` Config locks heading moves 10 characters earlier, and R6 wording.
3. **C&W sentence.** Move "Collect & Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC." to the end of "Span and time base". In "When a beat starts", leave "A window the release instant pre-empts does not count." Keep the calendar event text as it is, so S01 does not hang on the inline read alone. Follow-on: heading offsets. This ties S01 to the same read habit as S08 and S09, which helps SD but concentrates patterns, so check the pattern gate on the first batch.
4. **Frame.** Drop the ZOM-432 Done UPDATE so the ticket returns to base Todo, with `updated_at` following `cmt_zom432_1`. Remove `cmt_zom432_2`. Add a top-level post by Calvin Price in #zm-animations (`C09ATAJ220H`, Julia is a member) after 20:13 UTC on Sep 30, when Android 135 succeeded, keeping "The frame went out with PR #471" and the two build numbers. Follow-on: S07 returns to multi-source at weight 5 (total 106), T10, Linear cohort 18 to 19. Avoid #builds (no human replies in September) and #zombie-match3d (it would sit beside Vincent's post). This reverses part of revision 5, so run the coherence pre-sweep first.

**Considered and rejected**

- **Grading ZOM-534 as a deploy still-to-do:** the fix is client code on main, so "ships with the backend release" would be false.
- **Renaming Vincent's post to "league":** only 5 September messages use that word, and it breaks his voice.
- **Vincent's re-test as a reply under "I just released 0.3.49 on IOS":** it reads as iOS-only and reopens the "unverified platform" clause.
- **Removing the C&W cadence from the brief:** it would then rest on the Domino calendar row and the CDK schedule, whose wording disagrees. That is a fork.
- **Moving the strip note again:** a Confluence comment is near all-fail and a Slack reply makes it easier. Rev 8's shape passed review, and a third move buys little.
- **De-naming more records:** Q4 shows the end state: lower average, no spread.
- **A rule that each still-to-do gets a ticket note, to lift calls:** it adds a rule, about five calls and a fork, since vials, strip and config have no ticket.

**Calls.** There is no clean lever. Bridge reached its horizon through per-entry writes, and this task has no honest equivalent. Take the pre-check count first. If it lands under about 110, revisit. Otherwise accept an average above 130 with a few runs under it.

**Spread.** Options 1 to 3 help most because each adds an independent swing. Avoid rows that every run passes where the rubric allows it, and re-run the SD check after any row change, as the Bridge notes advise.

## 4. Keep untouched

The platform scored these 5 on `6aea4c1e9b621f28dc3a5332_1_prompt-3.md`. Unique Ground Truth and Clarity at 2 are the only open dimensions.

| Scored 5 | What must not change |
|---|---|
| Alignment with date, Contrived, Explicit Tool Mention, Truthfulness | `04_Prompt.txt` byte for byte (reviewed sha `2a23afd8…`): "yesterday", "Monday the 6th", no tool names, all 7 premises |
| Persona, Business Function, Competency, Task Skill | Julia building Frederick's calendar and recommendation as one job |
| Coherence, Investigation + Action | One workflow and the five kinds of write: sheet, ZOM-78 link, ZOM-429 note, reply to Brian, DM reply |
| Tool Use & Cross-service | Each service still changes a graded fact: Slack, Docs, Sheets, Gmail, Calendar, Linear, GitHub, Confluence |
| Feasibility, Persona ACL, Data Exists | Every deciding record stays Julia-readable. No deciding fact only in #zombie-prs or #zm-collect-win. The sheet, folder, deck and native-file row shape stay |
| Cross-Service Coherence | The SC-15 repair (ZOM-521 description, `cmt_zom526_2`, `cmt_zom526_3`, `cmt_zom521_2`). `#470#rc_10` and `#472#rc_1` inside base approvals seconds before merge. Nothing added to merged PRs. Rubric and OE stay off SC-13, SC-18, SC-22, SC-38, SC-62 |
| Complexity & Data Seeding, Originality | Short trigger, the four-week buy window, push plan, and hold and lock rules (dataset gate 0.75, same scenario) |

**Quotes the review's fork table rests on. Keep them findable.**

- Brief: "a window the release instant pre-empts does not count", "A hold with no dated fix runs until the fix is confirmed on prod", "Boss Arena is off this calendar", "its owner is told in a reply on the mail where they committed to it", "Wrong counters", "For the quest rollover, the daily gift", "an event window, a reset or a start push".
- Reply under the ask: "Leave off the four rows", "local notifications included", "Copy that does not name the game at all is fine to go out", "keep Zombie Lane off the calendar".
- Records: Vincent's re-test; Robert's "pulling my ok. Take it off the beta calendar"; spec "locked 24h before each season opens"; Arthur on #468 and #470; Marcus's Sep 30 note; `cmt_zom78_1`; Brian "it does not have to land before the beta"; both "not needed for the beta" comments; Samuel's frame sentence; "claiming works and nothing is lost"; Trello "The rollover does not wait on them".
- Both-fair items must stay accepted: any new config date before Oct 31 00:00 UTC, the October window from Oct 1 or Oct 6, the strip deadline Oct 31 or Nov 1.

**How the options touch this list.** Option 1 keeps Robert's quote. Option 2 leaves the reply verbatim. Option 3 keeps the pre-empted-window clause (capital A only). Option 4 keeps the frame sentence but changes author and service, so it is the one that needs a fresh blind pass on F25.

**Also keep the carriers that already work:** the thread reply under the ask, `#468#rc_38` and `#472#rc_1` inline, ZOM-465's location, Confluence as the only lock source, and the brief's silence on all of them.
