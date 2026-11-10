# Closure audit: Slack census under revision 9

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). SQL sha 892f7edd. Read-only: nothing was edited outside this file and R/work/.

## Verdict

I tried to argue 146 rows onto the calendar. **2 stay OPEN**, both on Endless Still to do. 3 more close only on an owner's claim. **No reading survived on a Held status, a Hold until value, a window start or a push call.**

The cutoff carries a lot of weight: 19 rows are closed by the date alone, and that depends on one reading of a single sentence (Finding 3). A same-length word swap removes that risk.

## Findings, most serious first

### 1. SO-45b: Endless in-level VFX is OPEN

The census marked SO-45 settled through ZOM-565. That comment does not cover this work. Marcus's Sep 25 note passes every limb of the rule: after the brief, names the beat, player-facing art, flagged as not done.

- **For the fork:** Marcus, #zm-animations ts 1758815614.940719, Sep 25: "The vfx added to the endless mode gameplay ... i shall remove it) I also need to add few text animations like for the combo when it changes etc...." ZOM-565 body: "I'm going to start working on the endless mode vfx inside of the core game part."
- **Against it:** cmt_zom565_1, Marcus, Sep 29: "This is the P1/P2 endless polish from the list Brian gave me, the screen already works without it, so it is not needed for the beta." The ticket is "Endless Horde Start Screen Vfx" and the reason given is about "the screen".
- **Why it is not closed:** the waiver is the owner's own claim and covers a neighbouring scope. "polish nobody flagged" does not help, because this polish was flagged.
- **Smallest fix:** one comment on ZOM-565 from Brian (usr_fc22d5941b2aeb5c), who set the priorities and is not the art owner, dated between Sep 29 14:35Z and Sep 30 16:33Z. For example: "Agreed. All the P1/P2 Endless VFX, the start screen and the in-level part, can follow after the beta." Add `UPDATE linear.linear_issues SET updated_at` to match. This also backs SO-45a and X-6.
- **Keep it true to the base:** [N] Marcus, Sep 29: "im going to continue working on this branch for the stuff in the core game", and [N] Brian, Sep 30: "After the boss arena and endless mode...". The work goes on, so the record must not say it stopped.

### 2. SO-22: Endless desert and port themes are OPEN

This one is weak, but the standard does not allow dismissing it on that ground. It is post-brief art that names the beat, and no Julia-readable record waives it.

- **For the fork:** Martin, #zombie-art ts 1759159849.386619, Sep 29: "I'm preparing a *desert theme* for the *Endless Mode*!"; ts 1759249627.370789, Sep 30: "*Port theme* to have more variants to choose for Endless or Main gameplay mode".
- **Against it:** only inference from "to choose", plus Robert's "we are not spending art time on a theme we may not ship at all", which is about the prop set. Whether "preparing" counts as "flagged as not done" is a judgment, not a quote.
- **Smallest fix:** one reply in that thread from Robert, dated Sep 30 16:28Z to 22:09Z, so it follows the port post and comes before his DM. For example: "Nice, but neither of these is for the beta. Endless keeps its current look." Update parent a3e78e820b9f880ef4e3d941562110df: reply_count 4, reply_users_count 4, latest_reply, thread_ts_legacy. The base has reply_count 3, reply_users_count 3.
- **Keep it true to the base:** [N] Martin, Sep 26: "About the Endless Mode I think we are not changing it for now." Keep the word Halloween out, since revision 9 removed it from Robert's DM for difficulty.

### 3. One sentence carries the cutoff, and it has a second parse

"what has been flagged for that beat as not done since this brief" is meant as flagged since the brief. A hostile reader can attach "since this brief" to "not done": flagged at any time, and still not done since the brief. That reading brings back the 19 rows marked †, including Julia's own quest config (U3) and Vincent's prod config (U10).

- **Why I still count these closed:** "has been ... since" binds to the verb, and a flag from before the brief cannot speak about the time after it. But that is an argument about grammar, and deep_recheck says an inference "is not a reason".
- **Smallest fix:** swap the words to "what has been flagged since this brief for that beat as not done (prod deploy, config or player-facing art)". The phrase stays 52 characters, so no style_runs offset moves. The clause appears only in the SQL and in apply_review_fix_rev9.py, and no graded value changes.

### 4. Kills that hold but rest on an owner, or on silence

None of these is OPEN, but a reviewer who presses will land here first.

- **U4, reward box:** the rule kill needs "the box" to stay unattached to a beat. Oliver's "nothing waits on it" is the owner's claim, and "goes out with the next build" concedes the fix has not landed. The word "box" points at several beats, so no single beat is named.
- **SO-03, SO-08, U13:** three fixes on main after iOS 50 and Android 135, the same shape as ZOM-534. No record speaks to them. Only "flagged" and "Nothing else goes in" keep them out. That is enough under the rule, and the census's proposed Oct 1 record would add a Season Pass still-to-do, so do not add it.
- **SO-41:** Leonard's Trello note is an owner's decision. It holds, but it does not reach U3, which rests on the date alone.

### 5. Corrections to the census

- **Robert's Sep 24 restatement is after the brief:** 18:32:34Z against the doc row's 17:40:52Z, by 51m42s. The cutoff does not kill it. Leonard's reply and the kind limb do.
- **SO-05 and SO-14 need no new record.** Confluence page_liveops_calendar (Sep 29, Julia-reachable) already says "QA blockers cleared 26 Sep 2025" and "Same feature as Win & Collect on Domino Delights, under a different name". The census's proposed Vincent record can be dropped.
- **Held readings of Endless and Plague Race have a non-owner kill:** the same page lists both as "Live", so U9 no longer rests on Douglas's "Solved".
- **B17 does close:** #builds Sep 24 18:18Z, "Double the timeouts for Get requests."
- **U2:** "force quit recovered it" is an inference. Robert only says he force quit. The kill does not need it.
- **Not in the census:** six new rows, X-1 to X-5 and X-7, plus X-6 from the Linear slice. All closed. X-2 and X-3 are cutoff-only, so they join Finding 3.

## Kill quotes used in the table

Sources are Julia-reachable. The brief is gdocs f_7c3e91a4d2b85f60e1a9c4, "Frederick, Sep 24", row modified 2025-09-24 17:40:52Z.

| Code | Source | Quote |
|---|---|---|
| K1 | Brief, Still to do | "what has been flagged for that beat as not done since this brief (prod deploy, config or player-facing art). Nothing else goes in: not what already shipped, not analytics, not polish nobody flagged." |
| K2 | Brief, Held or not | "Hold a beat only when players provably cannot enter, score or claim on prod even after a restart. An established failure holds it; an unverified one does not. Wrong counters, a reset that needs a restart, cosmetic, VFX and performance gaps and analytics gaps do not hold a beat" |
| K3 | Brief, Held or not | "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date." |
| K4 | Brief, Push copy | "A push goes out only if its row is Ready and LIVE and its English copy names the game as Zombie Match 3D and events by their ZM3D names. Anything else is held, with what is missing." |
| K5 | Arthur, PR #470 rc_10, Sep 30 15:51Z | "The Plague Race, leagues, Endless and Season Pass schedules are already running on prod." |
| K6 | Confluence page_liveops_calendar, Sep 29 17:00Z | Endless Monster Mode: "Live; also one of the three permanent board modes". Plague Race: "Live; algo bug Aug 2025". |
| K7 | Same page | Collect & Win: "Built for the end-of-September beta submission (QA blockers cleared 26 Sep 2025); not yet live. Same feature as Win & Collect on Domino Delights, under a different name" |
| K8 | Confluence page_season_pass_spec, Sep 30 17:30Z | "Reached production in the week of September 22-29, 2025 - Android 0.3.127 published Sep 22, iOS 0.3.49 released Sep 29 at $6.99" |
| K9 | Leonard, #zombie-bugs, Sep 17 | "overall we are in great shape - no major bugs until level 50+"; "but no other blockers" |

K1 is cited by limb: **date** (dated before the brief), **kind** (not a prod deploy, config or art), **beat** (names no beat), **flag** (nothing flags it as not done), **shipped**.

Fourth column: RECORD is a dated, Julia-reachable, non-owner record. RECORD (rule) is the brief's own words applied to a checkable fact. OWNER and INFERENCE are what they say. "pre" and "post" are against 2025-09-24 17:40:52Z.

Row ids: U, SO and N are the census ids. B1 to B59 are section 4 rows of census_slack_bugs.md. T1 to T16 are its section 3 rows in order, and T17 and T18 its Samsung history. X are new. SO-45 is split into a and b. U6-edge is split from U6.

## Results, ranked

### OPEN: no quote rules it out (2)

| id | Reading B tried | Kill quote and source, or OPEN | Kind of kill, and does it truly rule it out |
|---|---|---|---|
| SO-45b | [Sep 25 15:53Z, post; names "endless mode gameplay"; art, owner's own flag] Endless Still to do: "in-level VFX: combo text animations, remove the purple lightsweep on the rocket (Marcus)". Marcus: "i shall remove it) I also need to add few text animations like for the combo when it changes etc....". ZOM-565 body: "I'm going to start working on the endless mode vfx inside of the core game part." Branch commit 7683df0351, Sep 30: "infiniteBoss and endless mode core gameplay ui vfx wip", not on main. | OPEN. Nearest: cmt_zom565_1, Marcus, Sep 29: "This is the P1/P2 endless polish from the list Brian gave me, the screen already works without it, so it is not needed for the beta." It sits on "Endless Horde Start Screen Vfx" and argues from "the screen", so it does not reach in-level VFX. Brian's Sep 12 list says P1/P2 and nothing about the beta. | OWNER, and a neighbouring scope (SCOPE_GAP). Does not truly rule it out. Passes every limb of the rule, and "polish nobody flagged" does not help because this polish was flagged. |
| SO-22 | [Sep 29 15:30Z and Sep 30 16:27Z, post; names Endless; art] Endless Still to do: "desert or port theme art (Martin)". Martin: "I'm preparing a *desert theme* for the *Endless Mode*!" and "*Port theme* to have more variants to choose for Endless or Main gameplay mode". Julia herself replied "It looks super cute and polished". | OPEN. Nearest: Martin's own "to have more variants to choose" (reads as optional, but says nothing about the beta). Robert's Sep 30 DM "we are not spending art time on a theme we may not ship at all" is about the prop set. K5 covers schedules, not art. | INFERENCE only. Nobody says it can wait. Weak, but no quote rules it out, and the only base record that would ([N] Martin Sep 26, "About the Endless Mode I think we are not changing it for now") is one Julia cannot read. |

### Closed only by an owner's claim (3)

| id | Reading B tried | Kill quote and source, or OPEN | Kind of kill, and does it truly rule it out |
|---|---|---|---|
| SO-45a | [Sep 25 13:46Z, post; names Endless Horde; art] Endless Still to do: ZOM-565 bar hook-up and claim-state glow (Calvin). Ticket is Todo, assignee Calvin. | cmt_zom565_1, Marcus, Sep 29 14:34Z: "the screen already works without it, so it is not needed for the beta." | OWNER (the ticket's author and art owner, not the assignee). Truly rules out the start-screen work, and the platform accepted it as F24. No non-owner backs it. |
| SO-41 | [Sep 12 list; Trello note Sep 29, post; names the rollover; config] Quests Still to do: "more quests and reward balance (Leonard, Douglas)". The Sep 29 note is itself a post-brief flag. | Trello 68dac8204f1e9a3b7c2d5e61, Leonard, Sep 29: "The rollover does not wait on them, the current quests keep running either way." | OWNER, but a decision, not a status claim about a gap: Leonard opened the card and co-owns it. Truly rules it out for added quests and reward balance. It does not reach U3. |
| U6-edge | [Sep 25, post; names quest rollover] Quests Still to do: Douglas's "keeping this open to watch one timing edge case on the day boundary". | cmt_zom534_1, same comment: "so nothing else has to land for the beta." Also K1 kind: watching a timing case is not a deploy, config or art. | OWNER plus RECORD (rule). Holds on the kind limb even if the owner's clause is set aside. |

### Dated after the brief, or needing more than the cutoff: closed by a rule or a record (33)

| id | Reading B tried | Kill quote and source, or OPEN | Kind of kill, and does it truly rule it out |
|---|---|---|---|
| U1 | [Report Sep 21, pre; Robert's restatement Sep 24 18:32:34Z, POST by 51m42s; names endless] Endless Still to do: verify the S23 freeze. Held: friend "froze for good". | Leonard, thread reply fb870fca, Sep 29: "Ran this again on an S23 Ultra from the remote device list, live Android build, a few endless runs with the airstrike. Could not get it to freeze, so I am leaving this one." K1 kind: a check is none of the three. K2: "an unverified one does not". Robert: "Once Leonard's friend restarted, his log just continued to the next level". | RECORD. Truly rules it out. The cutoff does NOT do this work, because Robert's line is after the brief. Leonard is the reporter, not a fix owner. |
| B41 | [Sep 21, pre; Endless] Same report as U1. | See U1. | RECORD. Holds. |
| B44 | [Sep 24 18:32Z, post; Endless] Same event, restated. Passes the date limb. | See U1. It is an account of past logs and flags nothing as not done, and K1 kind applies. | RECORD. Holds. |
| U4 | [Sep 30 16:24Z, post; art; NO beat named] Quests, Daily gift or Endless Still to do: "reward box lightSweep fix (Oliver)". Vincent: "i think we should squeeze in the fix for that issue if it's an easy fix." | K1 beat: none of the six messages names a beat. Oliver, reply 31b154fc, Sep 30 21:24Z: "It is only that sweep on the art, it goes out with the next build and nothing waits on it." | RECORD (rule), with OWNER as the second leg. Holds. "box" does not resolve to a beat: ZOM-565 ("the box", Endless), cmt_zom344_1 ("Quest box"), ZOM-432 ("gift box"), and the material's Jul 4 commit touches RewardScreen.prefab and weeklyContest animators. If a reviewer pins it to a beat, only Oliver's claim is left. |
| B45 | [Sep 30, post; no beat] Same as U4. | See U4. | RECORD (rule) plus OWNER. Holds. |
| U5 | [Sep 16 To Do, pre; ZOM-563 started Sep 30, post; prod deploy] Season Pass Still to do: "premium golden frames and names to prod (Douglas)". | cmt_zom563_1, Vincent, Sep 30 22:04Z: "Checked on prod after the update: teams' lives, golden frames and names all work as expected. Closing." Issue set to Done. | RECORD. Truly rules it out: the tester, not the assignee, and it mirrors his base DM. |
| SO-04 | [Same as U5] ZOM-563 still looks In Progress. | See U5. Post-SQL state is Done. | RECORD. Holds. |
| U6 | [Reports Jul 16 and Sep 8, pre; injected notes post; Quests] Quests Still to do: "ZOM-534 fix to prod". | cmt_zom534_2, Leonard, Sep 30 01:22Z: "Stayed online through the 00:00 UTC reset on the store build tonight. Quest points reset on their own, no restart. That was my report, it is good on prod now." | RECORD. Truly rules it out: the reporter, on prod. Also K2 "a reset that needs a restart" for Held. |
| B2 | [Jul 16, pre; Quests] First report of U6. | See U6. | RECORD. Holds. |
| B25 | [Sep 8, pre; Quests] Second report of U6. | See U6. | RECORD. Holds. |
| U7 | [Aug 29 and Sep 22, pre; Leaderboard; the held-fix limb has NO cutoff] Still-to-do owner is Oliver or Calvin (client crash, reverted 49211bd82f), not Douglas. | Prompt: "leave a note on its ticket so the owner picks it up." ZOM-429 assignee field: Douglas; body: "it doesn't start the new one or let me claim my rewards", the same symptom as Vincent's Sep 30 re-test. | RECORD (ticket field plus prompt). Holds for the owner. Nothing links the crash to the rollover, so the cell should not name a code cause. |
| SO-10 | [Sep 19 and 22, pre; Leaderboard] Hold until or Still to do: "re-land the reverted crash fix (Oliver)". | K3 sets the Hold-until value whichever fix it is. Owner as U7. Vincent, after the revert: "yep, it's working fine right now". | RECORD (rule). Holds for Hold until. The held-fix limb has no date test, so the kill for Still to do is U7's, not the cutoff. |
| U11 | [Sep 25 17:31Z, post; names Endless] Endless Still to do: "reduce objects (Oliver)". No such commit is on main. Read as config. | K1 kind, and Oliver's own words: "different optimizations to reduce heating", "we wanna measure the impact of these actions". Season Pass spec, Sep 30: "Do not touch tray count or Endless refill cadence during an active season". | RECORD (rule plus the author's own description). Holds: a measured performance test. Robert's spec line points against landing it, though refill cadence is not object count. |
| U13a | [Sep 30 21:27Z, post; names endless_02] Endless Still to do: "next client build for the popup fix". Commit 25c6c66b6b is after iOS 50 and Android 135. | K1 flag: #builds says "Ensuring that in level popups are only called in normal levels", a change made, not a flag of something not done. "Nothing else goes in". | RECORD (rule). Holds, though no record speaks to it: the rule turns silence into "out". Same on-main shape as ZOM-534, which failed under the old rule. |
| SO-08 | [Same as U13a] Endless. | See U13a. | RECORD (rule). Holds. |
| U13b | [Sep 30 21:43Z, post; names season pass] Season Pass Still to do: next client build with "Fix season pass main screen instance from join popup". | K1 flag, as U13a. The Vincent lines that do call it unfinished are [N]. | RECORD (rule). Holds, no record speaks to it. |
| U13c | [Oct 1 05:51Z, post, before the clock; "Fix end popup" names no beat in its text] Season Pass Still to do before Nov 1. | K1 flag and K1 beat: the line names no beat, and only the diff (SeasonPassEndedPopup) ties it to Season Pass. | RECORD (rule). Holds. |
| SO-03 | [U13b and U13c together] Season Pass: "next client build (Oliver), before Nov 1". The UA deck buys on "the Sep 30 builds". | See U13b and U13c. Reading the timestamps against iOS 50 and Android 135 is the reader's own inference, not a flag. | RECORD (rule). Holds. |
| U13 | [Parent of U13a to U13c] Fixes on main after the submission builds. | See U13a, U13b, U13c. | RECORD (rule). Holds. |
| SO-20 | [Sep 29 22:01Z, post; names Win&Collect and daily Login] C&W or Daily gift Still to do: queue manager sign-off. Calvin: "let me know if that seems okay". | K1 "not what already shipped": #builds Sep 30 16:01Z, "Merge pull request #472", before Submission #50 at 18:43Z. cmt_zom526_3: "Collect and Win tokens go through the queue manager now (#472)." | RECORD. Holds. A sign-off ask is also none of the kinds. |
| SO-21 | [Sep 30 18:16Z and 22:25Z, post; art; NO beat] Endless Still to do: better enrage effect (Marcus). Robert: "that was a placeholder". | K1 beat: "better "enraged" effects on zombies" names no beat. It follows Robert's Boss Arena thread with "also". | RECORD (rule). Holds, and the "for that beat" limb is what does it. This is real flagged art. |
| SO-26 | [Sep 29 18:52Z, post; NO beat] Still to do or unlock levels: "move up card introduction earlier" (Brian). | K1 beat: FTUE and level order, no beat named. | RECORD (rule). Holds. |
| SO-13 | [Sep 25 17:59Z, post, and Sep 19-22, pre; push] Push call: hold pushes until the permission prompt is fixed. Robert: "it disables the audio". | K4 tests the row and the copy only. Robert: "It could very well be an OS bug that we can't fix." | RECORD (rule). Holds for Send or hold. |
| SO-14 | [Sep 12 to 30; push and C&W] Win & Collect is a live ZM3D name (#472 title, Calvin Sep 29), so the row's what-is-missing drops the naming note. | K7, Confluence page_liveops_calendar, Sep 29: "Same feature as Win & Collect on Domino Delights, under a different name". Brief: "Collect & Win runs Mon-Tue, Wed-Thu and Fri-Sun". | RECORD. Truly rules it out. Upgrades the census's SCOPE_GAP. No new record needed. |
| SO-05 | [Sep 19 and 22, pre; C&W] Still to do: "final product test or shippable sign-off (Brian)". | K7: "Built for the end-of-September beta submission (QA blockers cleared 26 Sep 2025)". K1 date and kind. | RECORD. Truly rules it out. The census asked for a new record, but this one exists and Julia can read it. |
| B59 | [Sep 30, post; Leaderboard] Not held: Douglas's Sep 16 note makes it "a reset that needs a restart". | Vincent b5f2955c: "I killed the app and reopened it twice, played a few levels, and my week is still last week one. Same on the second device." | RECORD. Holds; this is the expected answer. |
| SO-42 | [Sep 17 and 18, pre; Halloween] One-off on the calendar. | Robert, DM, Sep 30: "pulling my ok. Take it off the beta calendar". Brief: "his later word is the one that counts". | RECORD. Holds. |
| SO-43 | [Sep 30 Boss Arena VFX, post] Boss Arena Still to do. | Brief: "Boss Arena is off this calendar until the pivot call." | RECORD (rule). Holds. |
| X-1 | [NEW. Sep 26 16:57Z, post; names season pass] Season Pass or other beats Still to do: move to Addressables. Oliver: "I'll start moving season pass soon", "create linear tasks to move each liveops feature to Addressables". | K1 shipped for Season Pass: #builds Sep 30 15:50Z, "Merge pull request #473 ... addressables/sp", before the cut. K1 kind for the rest (a memory refactor). | RECORD. Holds. |
| X-5 | [NEW. Sep 30 17:30Z, post; names Season Pass] Spec: "No Season Pass purchase has been recorded yet". Strengthens SO-01's Reading B. | K1 flag and kind: a fact about sales, not a flag, and a purchase test is not a kind. | RECORD (rule). Holds. |
| X-7 | [NEW. Sep 26 20:35Z, post; Endless] Still to do: slow Endless level load. Robert: "it takes a good 10 seconds". | K1 kind. Robert: "I don't know if this has any implication on the actual game in a live environment". | RECORD (rule). Holds. |
| T2 | [Sep 21, pre; Endless] The S23 report, same as U1. | See U1. | RECORD. Holds. |
| T14 | [Sep 24 18:32Z, post; Endless] Same as B44. | See U1. | RECORD. Holds. |

### Closed by the date alone (†): these come back if the cutoff parse fails (Finding 3) (19)

| id | Reading B tried | Kill quote and source, or OPEN | Kind of kill, and does it truly rule it out |
|---|---|---|---|
| U3 | [Sep 22 22:40Z and Sep 23 14:21Z, pre, 27h before the doc row; Quests; config; Julia's own message] Quests Still to do: remove boss buster quests, adjust bosses killed. | K1 date. The Trello note covers "More quests and the reward balance", not removals. | RECORD (rule + date). Holds on the date alone † |
| B43 | [Same as U3.] | See U3. | RECORD (rule + date). Holds on the date alone † |
| U10 | [Aug 6, pre; Endless; literally prod config] Vincent: "too op for prod configuration", "It needs to be updated with the params in the thread". ZOM-545 Todo. | K1 date. | RECORD (rule + date). Holds on the date alone †. This is the plainest config row in the census. |
| B52 | [Same as U10.] | See U10. | RECORD (rule + date). Holds on the date alone † |
| U12 | [Sep 3-5, pre; Endless; config] Rotation config. EMPLOYEE_0032: "this is incorrect bc if we add 4 levels or more". | K1 date. No effect while only 3 levels exist. | RECORD (rule + date). Holds on the date alone † |
| B55 | [Same as U12.] | See U12. | RECORD (rule + date). Holds on the date alone † |
| SO-11 | [Sep 10, pre; Plague Race; config] Leonard: "Can we please cut it it in half by tomorrow?" Thread ends with no Julia-readable close. | K1 date. The base close is [N]. | RECORD (rule + date). Holds on the date alone † |
| SO-16 | [Sep 13, pre; Endless; config] Leonard: "first step is to cut coins back to half". | K1 date. | RECORD (rule + date). Holds on the date alone † |
| SO-24 | [Sep 9, pre; daily login chest; art] Marcus: "the chest need to open first and then the rewards come out". | K1 date. | RECORD (rule + date). Holds on the date alone † |
| SO-06 | [Sep 17, pre; Endless] Robert: "We are going to remove the force play"; Leonard: "let's do this by the next relesae". Robert's Sep 24 18:32 "every user is forced to play it" states a fact and flags nothing. | K1 date. Kind is arguable (tutorial flow). | RECORD (rule + date). Holds on the date alone † |
| SO-07 | [Sep 11, pre; Endless] Brian: "I think we need to adjust the Endless Mode tutorial". | K1 date. Kind arguable. | RECORD (rule + date). Holds on the date alone † |
| SO-15 | [Sep 12, pre; several beats] Leonard's beta pipeline list: "Bot scoring improvements", "Add quests and rebalance quest rewards", "Adjust airstrike balance", as owned lines. | K1 date. K8 for Season Pass, K7 for C&W, Trello for quests. Bot scoring has only the date. | RECORD (rule + date). Holds on the date alone † |
| B37 | [Sep 16, pre; Season Pass] Leonard: "Remove it from season pass or fix pre-level dialogue". | K1 date. No Julia-readable record names the fix. | RECORD (rule + date). Holds on the date alone † |
| B5 | [Jul 31, pre; Endless; art] Robert: "Not blocker but strange shadows in Endless Mode levels". | K1 date. K2 cosmetic for Held. | RECORD (rule + date). Holds on the date alone † |
| B7 | [Aug 6, pre; Endless; art] Tutorial above other UI. Vincent: "Doesn't cause any issue but not the ideal." | K1 date. K2 cosmetic. | RECORD (rule + date). Holds on the date alone † |
| B8 | [Aug 6, pre; Endless; art] Robert: unlock message "didn't stay for more than 0.5 seconds". | K1 date. K2 cosmetic. | RECORD (rule + date). Holds on the date alone † |
| B47 | [Jul 23, pre; Endless] Robert: "I've noticed that bosses are double spawning... I guess that bug is back?" Vincent asked for a video; none followed. | K1 date. | RECORD (rule + date). Holds on the date alone † |
| X-2 | [NEW. Sep 7 01:37Z, pre; Endless; config] Chest thresholds: Douglas lists 10, 25, 50; Leonard: "I think we may want to change it." | K1 date. | RECORD (rule + date). Holds on the date alone † |
| X-3 | [NEW. Sep 16, pre; Season Pass; config] To Do: "Rearrange rewards until win streak freezer duration is implemented" (Brian). | K1 date. | RECORD (rule + date). Holds on the date alone † |

### Before the brief, with a second kill (75)

| id | Reading B tried | Kill quote and source, or OPEN | Kind of kill, and does it truly rule it out |
|---|---|---|---|
| U2 | [Sep 10-11 reports and ZOM-559 created Sep 22 14:54Z, never updated, pre; Sep 10 names endless horde, Sep 11 and ZOM-559 say "a level"] Endless Still to do: verify the end-screen freeze on Samsung (Oliver). Held: "frozen for good". | K1 date and kind. Robert's Sep 25 lines (post) cover audio only: "It could very well be an OS bug that we can't fix." Held: K2 "provably"; Leonard is back in Endless Sep 16 and Sep 17; K6 "Live". | RECORD. Holds. Census says force quit "recovered" it. That is inferred, as Robert only says "I had to manual force quit". |
| B27 | [Sep 10, pre; Endless] U2's first report. | See U2. | RECORD. Holds. |
| B28 | [Sep 11, pre; "a level", no beat] U2's second report. | See U2, and K1 beat. | RECORD. Holds. |
| U8 | [Aug 8-9, pre; Plague Race] Still to do: bot behaviour (Douglas). Held: race restarts when complete. | K1 date and kind. Held: Vincent: "If I win 10 levels, I can continue with the next stage". K6: "Live". | RECORD. Holds. |
| B13 | [Same as U8.] | See U8. | RECORD. Holds. |
| U9 | [Aug 8 promise; Sep 7, pre; Endless, Plague] Held: "Killing the app doesn't solve the issue". Still to do: "check the reset jobs after the Oct 8 deploy", from Douglas's "I will check the jobs on prod after every deployment". | Held: K6 (Sep 29): "Live". Leonard Sep 16: "Endless mode stuttered really badly for me as soon as I opened it". Still to do: K1 date and kind. | RECORD. Truly rules it out, and no longer rests on Douglas's own "Solved". |
| B24 | [Sep 7, pre; Endless; survives restart] Same as U9. | See U9. | RECORD. Holds. |
| B1 | [Jul 10-17, pre; Leaderboard] Still to do: rank counting. Vincent: "showing +3 more than the completed levels". | K1 date and kind. K2 "Wrong counters". | RECORD (rule + date). Holds. |
| B3 | [Jul 29, pre; daily chest] Tooltips "all show coins image". | Calvin: "that fixed all tooltips from quest, leaderboard and daily login". | OWNER, plus K1 date. Holds. |
| B4 | [Jul 31, pre; Quests] 4th daily chest. | Leonard, Jul 31: "4th daily chest is fixed". | RECORD. Holds. |
| B6 | [Aug 4, pre; Daily gift] Held: "the panel did not close", "only killing the app solved it" (Vincent's Jul 22 words, quoted into the thread). | cmt_zom556_1, Vincent: "it paid out and moved to the next day ... claiming works and nothing is lost." K2 fails "even after a restart". | RECORD. Holds. |
| B9 | [Aug 6, pre; Endless] Stutter. | K2 "performance gaps". Robert, Aug 19: "the monster stuttering is gone I think". | RECORD (rule + date). Holds. |
| B10 | [Aug 7, pre; Daily gift] Held: date parse error after claiming. | cmt_zom556_1, as B6. K1 date. | RECORD. Holds. |
| B11 | [Aug 7, pre; Endless, Plague] Held: "Endless mode got stuck after the first day". | Vincent, Aug 8: "I can see that the daily is refreshed and played it without an issue." K6. | RECORD. Holds. |
| B12 | [Aug 8, pre; Daily gift] Held: "I didn't see daily login today". | Same line: "I might see it at midnight so not sure". K2 "an unverified one does not". cmt_zom556_1. | RECORD. Holds. |
| B14 | [Aug 13, pre; Plague Race] Red dot. | Leonard: "yeah, we don't need it! cancel the ticket". cmt_zom471_1: "nothing here has to land for the beta." | RECORD. Holds. |
| B15 | [Aug 13-14, pre; Endless] 0.3.21 notes. | ZOM-473 Done. K1 date. | RECORD. Holds. |
| B16 | [Aug 14, pre; Endless] Timer beeps. | ZOM-479 Done. | RECORD. Holds. |
| B17 | [Aug 28 and Sep 22, pre; all live-ops] Still to do: raise Android timeouts (Arthur). | K1 shipped: #builds Sep 24 18:18Z, "Double the timeouts for Get requests. [Arthur Blake]", in later submission builds. K1 date. | RECORD. Holds. Census left this with no closure in the thread. |
| B18 | [Aug 25, pre; Endless, Plague] Held: no refresh on prod. | Row 20's Vincent quote. K6. | RECORD. Holds. |
| B19 | [Aug 29, pre; Leaderboard] Held on other grounds. | Beat is held by b5f2955c; owner as U7. | RECORD. Holds. |
| B20 | [Aug 29, pre; Endless, Plague] Held. | Vincent: "endless and plague race is working now." | RECORD. Holds. Not the owner. |
| B21 | [Sep 3, pre; Endless] Sound bugs. | ZOM-515 Done. | RECORD. Holds. |
| B22 | [Sep 3, pre; Endless] Refill one short. | cmt_zom546_1, Owen (assignee): "Refill counts hold level across a long endless run here". K1 date and kind. | RECORD (rule + date). Holds. |
| B23 | [Sep 3, pre; Endless] Enrage lost on refill. | cmt_zom517_1, Robert (reporter): "could not get one to lose it while walking." | RECORD. Holds. |
| B26 | [Sep 10, pre; no beat] Held: "live ops buttons disappeared" at 112. | Douglas: "probably There was a network error/lag". K2 unverified. K1 date. | RECORD (rule + date). Holds. |
| B29 | [Sep 11, pre; Endless] Quit keeps ticket. | Leonard: "That's cool. No ticket is needed then", "Let's keep it as is". | RECORD. Holds. |
| B30 | [Sep 11, pre; Leaderboard] Wrong star image. | ZOM-558 Done. | RECORD. Holds. |
| B31 | [Sep 15, pre; Quests] Held: "If I left, the quest cannot be claimed." | Same line: "I also need to stay in quest page after claiming it", so claiming works. K2. K9. | RECORD. Holds. Calvin's +1 on Robert's "Things fixed?" is only the owner's word, so the kill rests on the same-line workaround and K9. |
| B32 | [Sep 15, pre; Season Pass, test branch] Still to do: price 9.99 vs 6.99, left events. | K8: "iOS 0.3.49 released Sep 29 at $6.99". K1 date. | RECORD. Holds. |
| B33 | [Sep 15, pre; C&W] "I haven't seen any update or build". | K7. #468 merged Sep 29. | RECORD. Holds. |
| B34 | [Sep 16, pre; Quests] "Quest animation is also a blocker." | K2 cosmetic. K1 date. K9. | RECORD (rule + date). Holds. |
| B35 | [Sep 16, pre; Endless] Stutter on open. | K2 performance. K1 date and kind. | RECORD (rule + date). Holds. |
| B36 | [Sep 16, pre; Season Pass] No claim SFX. | Vincent's list, struck through: "~Add "claim" SFX to season pass~". | RECORD. Holds. |
| B38 | [Sep 16, pre; Season Pass] Premium lives, refill, trampoline set. | K1 date and kind. Oliver: "bugs fixed". K2 "Wrong counters". To Dos: U5, X-3. | RECORD (rule + date). Holds. |
| B39 | [Sep 17, pre; ZOM-556 note Sep 24 15:20Z, same day as the byline but before the doc existed; Daily gift] Still to do: ZOM-556. | K1 kind: a bug fix is none of the three. cmt_zom556_1: "claiming works and nothing is lost". K2 "Wrong counters". | RECORD. Holds. The only row near the Sep 24 line, and the kind limb covers it. |
| B40 | [Sep 17, pre; Endless] Phone burning. | K2 performance. K1 date and kind. | RECORD (rule + date). Holds. |
| B42 | [Sep 22, pre; Leaderboard] "Killing the app doesn't help". | Vincent: "yep, it's working fine right now". Beat is held anyway. | RECORD. Holds. |
| B46 | [Jul 23-24, pre, dev; Endless] Claim button persists. | Vincent: "I will stop testing the event flow before the backend integration then". K6. | RECORD. Holds. |
| B48 | [Jul 24, pre; Quests, Plague] TestFlight 0.3.3. | Leonard: "ok, I played first 25 levels again on 0.3.5 ... all look good." | RECORD. Holds. |
| B49 | [Jul 29-31, pre; Quests] Pack before level 35. | Vincent: "yep fixed". | RECORD. Holds. |
| B50 | [Aug 5, pre; Daily gift] Held: panel cannot close. | K2 "on prod": Frederick says "playing ZM in Unity Editor". | RECORD (rule + date). Holds. |
| B51 | [Aug 6, pre; Plague Race] Algo levels do not count. | K6 note: "(ZOM-459, opened 5 Aug, fixed 25 Aug 2025)". ZOM-459 Done. | RECORD. Holds. |
| B53 | [Aug 7, pre; Plague, Endless] Summary of B11 and B13. | See B11, U8. | RECORD. Holds. |
| B54 | [Aug 18, pre; Endless] De-enrage. | cmt_zom517_1, as B23. | RECORD. Holds. |
| B56 | [Sep 15, pre; Endless] Refill spawns fewer. | cmt_zom546_1, as B22. K1 date and kind. | RECORD (rule + date). Holds. |
| B57 | [Sep 17, pre; Endless] Heat. | K2 performance. K1 date and kind. | RECORD (rule + date). Holds. |
| B58 | [Sep 18, pre; push] Push call: prompt is hurting the funnel. | K4. Leonard, Sep 19: "This is 1.3.38. It's not PNs". | RECORD. Holds. |
| X-4 | [NEW. Sep 18, pre; push] Robert: "Push notification needs to be pushed back". | K4. Leonard: "It's not PNs". Prompt timing is not a row test. | RECORD. Holds. |
| X-6 | [NEW, Linear slice. Undated ticket body, base update Sep 23; Endless; art] ZOM-465 last unstruck item, "Refill Timer ticking animation". Post-SQL updated_at is Sep 30, so it looks fresh. | Same item: "(i've seen that the refil counter it's already animated do we still need to do that?)". K1 date. | OWNER plus RECORD (rule). Holds. The F1 fix would cover it too. |
| SO-01 | [Sep 12 03:13Z, pre; Season Pass] Still to do: "test the premium buy on a prod build". | K1 date and kind: a test is none of the three. K8. | RECORD (rule + date). Holds. |
| SO-02 | [Sep 2 and 5, pre; Season Pass] Still to do: test Pass End and Bonus Bank. | K1 date and kind. | RECORD (rule + date). Holds. |
| SO-09 | [Sep 22, pre; Samsung family; only the airstrike line touches a beat] Still to do: verify Samsung freeze. | K1 date and kind. Leonard's reply (U1). GDD, Sep 30: "mostly Samsung (Aug-Sep 2025, ZOM-475), fixed by removing the glass SFX and VFX." Level 21: K1 beat. | RECORD. Holds. |
| SO-12 | [Sep 5 and 9, pre; Season Pass] Still to do: clear the canvas issues. | K1 date and kind. K8. | RECORD (rule + date). Holds. |
| SO-17 | [Sep 13, pre; Endless] Performance. | K2. K1 date and kind. | RECORD (rule + date). Holds. |
| SO-18 | [Aug 23, pre; Endless, Plague] Held: "I can't play the Endless Zombie mode anymore". | K6. Vincent: "endless and plague race is working now." | RECORD. Holds. |
| SO-19 | [Sep 12, pre; C&W] "may need your help later, but not clear yet". | K1 date and flag. | RECORD (rule + date). Holds. |
| SO-23 | [Sep 4, pre; Season Pass] Badge choice. | Brian: "we can use only :exclamation:for now". K1 date. | RECORD (rule + date). Holds. |
| SO-25 | [Sep 22, pre; no beat] "Beta must be tech stable, no excuses." | K1 date and beat. Robert, Sep 29: "Our live ops are fine". | RECORD (rule + date). Holds. |
| SO-27 | [Sep 12 and 22, pre; naming] Infinite read as Endless. | #builds Sep 12: "Infinite boss arena (#424)". ZOM-487 "Infinite HP Boss Arena". | RECORD. Holds. |
| SO-28 | [Sep 12, pre] Login, ads, offers, 300 levels as beta to-dos. | Brief Scope: "an event window, a reset or a start push". K1 beat. | RECORD (rule + date). Holds. |
| SO-40 | [Sep 12, pre; Axe Arena] On the calendar. | Brian: "We've decided to postpone Axe Arena for the beta release." Frederick's reply lists it as not in the beta. | RECORD. Holds. |
| SO-44 | [Aug 29, pre] Reset failure. | Vincent: "endless and plague race is working now." | RECORD. Holds. |
| SO-46 | [Sep 14, pre; Endless] Home and victory screens. | K1 date. cmt_zom542_1: "so they are not needed for the beta." | RECORD (rule + date), plus OWNER. Holds. |
| SO-47 | [Sep 8, pre; Leaderboard] Profile deploy. | Same message: "P.S. the profile deployment is also done." | RECORD. Holds. |
| SO-48 | [Sep 12 and 24; dates] Span starts Sep 30. | Frederick's DM: "the beta buy we start Mon Oct 6 through Sun Nov 2". | RECORD (rule). Holds. |
| T1 | [Sep 17, pre] "1.3.38 is out!" | K1 flag: nothing to place. | RECORD (rule + date). Holds. |
| T9 | [Sep 22, pre] Vincent's Samsung line, same as SO-09. | See SO-09. | RECORD. Holds. |
| T7 | [Sep 22, pre] Android Submission #127. | K1 flag. | RECORD (rule + date). Holds. |
| T8 | [Sep 22, pre] ZOM-556 to 560 batch has no freeze ticket. | K1 flag and kind. See U1. | RECORD (rule + date). Holds. |
| T10 | [Sep 22, pre; no beat] "froze hard for a user at end of level 21". | K1 date and beat. K2 unverified. | RECORD (rule + date). Holds. |
| T11 | [Sep 23, pre] Arthur: "update the match3d required versions". | K1 date and beat. Window rule uses the backend release only. | RECORD (rule + date). Holds. |
| T12 | [Sep 23, pre] Robert passes QA the friend's user id. | See U1. | RECORD. Holds. |
| T17 | [Aug 14, pre] ZOM-475 glass crash still Todo. | GDD, Sep 30: "fixed by removing the glass SFX and VFX." | RECORD. Holds. |
| T18 | [Apr, pre] ENG-2324 Samsung startup freeze. | Domino Delights, Done May 27 per census. K1 date and beat. | RECORD (rule + date). Holds. |

### Not reachable by Julia (14)

| id | Reading B tried | Kill quote and source, or OPEN | Kind of kill, and does it truly rule it out |
|---|---|---|---|
| T3 | [#executives Sep 21 05:13] | Membership check on channels.json: not visible. | Not a fork: Julia cannot read it, and it is not a Reading B source. |
| T4 | [#executives Sep 21 05:18] | Membership check on channels.json: not visible. | Not a fork: Julia cannot read it, and it is not a Reading B source. |
| T5 | [#executives Sep 22 03:54] | Membership check on channels.json: not visible. | Not a fork: Julia cannot read it, and it is not a Reading B source. |
| T6 | [DM D04UP2L3E3S Sep 22] | Membership check on channels.json: not visible. | Not a fork: Julia cannot read it, and it is not a Reading B source. |
| T13 | [#executives Sep 23] | Membership check on channels.json: not visible. | Not a fork: Julia cannot read it, and it is not a Reading B source. |
| T15 | [DM D04UP2L3E3S Sep 25 (Oliver's half is U11)] | Membership check on channels.json: not visible. | Not a fork: Julia cannot read it, and it is not a Reading B source. |
| T16 | [#executives Sep 28 (Submission #133 in #builds flags nothing)] | Membership check on channels.json: not visible. | Not a fork: Julia cannot read it, and it is not a Reading B source. |
| N-1 | [self-DM D05QQ7YQTND, quests] | Membership check on channels.json: not visible. | Not a fork: Julia cannot read it, and it is not a Reading B source. |
| N-2 | [DM D07GY332589, season reset] | Membership check on channels.json: not visible. | Not a fork: Julia cannot read it, and it is not a Reading B source. |
| N-3 | [#zm-collect-win] | Membership check on channels.json: not visible. | Not a fork: Julia cannot read it, and it is not a Reading B source. |
| N-4 | [Collect&Win canvas] | Membership check on channels.json: not visible. | Not a fork: Julia cannot read it, and it is not a Reading B source. |
| N-5 | [Bug Checklist canvas] | Membership check on channels.json: not visible. | Not a fork: Julia cannot read it, and it is not a Reading B source. |
| N-6 | [#executives and DMs, heat] | Membership check on channels.json: not visible. | Not a fork: Julia cannot read it, and it is not a Reading B source. |
| N-7 | [#executives, confidence] | Membership check on channels.json: not visible. | Not a fork: Julia cannot read it, and it is not a Reading B source. |

## What I scanned

- **Every Julia-visible Slack message from Sep 24 00:00Z to the clock:** 1,130 in the export, plus the injected Slack rows read from the SQL. Membership comes from channels.json.
  - 821 outside #builds were read in order, with each line capped at 240 to 430 characters. A full-text keyword scan of the longer ones found nothing further.
  - #builds (309): raw lines to Sep 26, then Submission jobs and main-branch commit lines that match a beat keyword.
- **All 115 Slack timestamps cited in the two census files**, checked against the raw export. All resolve. Row 7's ts prefix also matches a non-visible DM, and the #zombie-bugs copy is the visible one.
- **Linear:** every ZOM ticket touched since the brief, plus the tickets cited here, with the SQL overlay applied by hand.
- **Trello:** the quest card and its actions, and the comment author.
- **Confluence:** the three post-brief pages that bear on beats (calendar, Season Pass spec, GDD keyword lines).
- **GitHub:** match3d PRs since the brief, human comments, branch commits, and match3d-backend commits since the brief.

## What I did not scan

- Pre-brief Julia-visible messages were not re-read line by line. For those I relied on the census's coverage and read only the cited threads, so "no follow-up" claims before Sep 24 are spot-checked, not proven.
- Slack file bodies and images, including the Sep 30 box image, are not readable. Bot attachments on #builds after Sep 26 were filtered.
- The material's GUID appears in no prefab in the tree, so tying the box to RewardScreen rests on its Jul 4 commit, not on a live reference.
- Gmail, GCal, Sheets, Slides, Snowflake, the rest of Trello, the API reference and Economy pages, and Universe_Normal were not read for this audit.
- The other census files (Linear, GitHub and Confluence, Trello, mail and Drive) are outside this slice, so a clean result here says nothing about them. X-6 is one row of theirs I happened to touch.
- The suggested record wording is untested: no lint, solver or gate was run on it.
