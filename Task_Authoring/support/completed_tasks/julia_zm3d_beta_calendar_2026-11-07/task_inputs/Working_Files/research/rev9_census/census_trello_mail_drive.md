# Fork census: Trello, Gmail, Google Calendar, Drive family (task_inputsS, revision 8 to 9)

Clock 2025-10-01 07:00 UTC, Universe_SynthCut. Basis labels follow CENSUS_BRIEF.md: RECORD, SCOPE_GAP, SILENCE.
Emoji in sheet and code strings are left out of the quotes. Nothing was executed from the SQL. Nothing outside this file was written (helper scripts sit in rev9/work_tmd/).

Row numbering: "row n" is the platform's numbering of PNs Beta (row n = sheet row n+1, so row 1 = R2 and row 14 = R15).
Reach tags: YES = owner or in shared_with_emails. UNVERIFIED = visibility domain or anyone and Julia is not listed (persona_view.py code U2). Trello, Linear and GitHub are unscoped.

## 0. Bottom line

- Gmail and Google Calendar add no new fork. Julia's mailbox has 2 base messages in the window, neither about a beat, and no base calendar event in the window carries a beat, release or description.
- Trello and Drive add new items. The most serious sit on the push rows, and they are not in the platform's sweep.
- **The biggest finding:** the client on main already sends six of the PNs Beta rows as local notifications, and two of those rows have copy the sheet gets wrong. Rows 4 and 6 are held in Reading A for "Puzzles vs Zombies", but Arthur renamed both strings to "Zombie Match 3D" in the client on Jul 22. Rows 9 and 14 are held as WIP, but the client already schedules them. A run that opens `NotificationManager.cs` (GitHub is unscoped) can argue a different status or a different "what is missing".
- **Second:** Frederick's UA deck says the buy starts "once the stores approve the Sep 30 builds". No record says whether store approval is a still-to-do.
- **Classification caution:** TMD-01 and TMD-02 are judgement calls. The brief's "its row ... its English copy" and the reply's "plan the PNs Beta tab as it stands" may be enough to rule them out. I rank them as forks because the platform has rejected on thinner gaps, and because the settled reading is untrue of the shipped client.

## 1. Unsettled candidates, ranked

| id | beat / row | where it lives (locator, author, date, verbatim quote) | how a reader would use it (cell, alternative value) | basis | what the base truly shows | best minimal settling record |
|---|---|---|---|---|---|---|
| TMD-01 | Push rows 4 (1 day lapsed) and 6 (FTUE) | Sheet f_a325dd4af80afc5994d5dc tab PNs Beta R5 K: "Return to Puzzles vs Zombies now and continue your mission"; R7 K: "[PERSON_NAME_2549] your first mission in Puzzles vs Zombies". Against: match3d main `Assets/Scripts/Notifications/NotificationManager.cs` lines 146 and 158: "Return to Zombie Match 3D now and continue your mission"; "Complete your first mission in Zombie Match 3D". Commit ec377e9fcf, Arthur Blake, 2025-07-22 13:54 UTC, "Update more title references". | Pushes tab Status and Notes. Expected: held, wrong game name. Alternative A: goes out (both rows are Ready and LIVE, and the real copy names the game correctly), so 4 rows go instead of 2. Alternative B: held, but what is missing is only a sheet update. | SCOPE_GAP. The nearest rule is brief "its row is Ready and LIVE and its English copy" and reply "plan the PNs Beta tab as it stands", which read most naturally as the row set. No record says the sheet text, not the client string, is what counts. | Sheet last modified 2025-06-23, before the rename. The client has held the right name for 10 weeks, so the Sep 30 builds carry it. Expected "wrong name" is true of the sheet and false of the shipped copy. The code also maps the anonymized token: [PERSON_NAME_2549] = "Complete". | Slack #zombie-match3d (C0880U9751A, Julia is a member), Leonard Hayes (he circulated the sheet on Jun 17). Earliest 2025-07-22 13:55 UTC, natural Sep 24 to Sep 30, latest 2025-10-01 06:59 UTC. Outcome that keeps Reading A and stays true: the PN sheet is the sign-off copy, the client strings were renamed in July but the sheet was not, and a row is not cleared until the sheet matches. Do not name row numbers. Other option: change the expected answer so rows 4 and 6 go. |
| TMD-02 | Push rows 9 (Plague Race) and 14 (Weekly Leaderboard) | PNs Beta R10 and R15: Status "Ready", "Status (NA, WIP, LIVE)" = "WIP". Against: same file lines 153, 161, 177 and 180: `WeeklyLeaderboardTitle = "Weekly Rankings Reset!"`, `PlagueRaceTitle = "Plague Race Is On!"`, `BatchScheduleWeeklyLeaderboardNotifications(...)`, `BatchSchedulePlagueRace(...)`. In the file since Samuel Turner's commit 5f077e47fc, 2025-06-24, "Added Push Notification". | Pushes Status or Notes, Weekly Leaderboard row, recommendation. Expected: held, WIP. Alternative: already going out from the client, so holding needs a client change (owner Samuel or Arthur). For row 14: players get "Weekly Rankings Reset" while the beat is held. | SILENCE. No record says what WIP means when the client already schedules the row, or whether a hold can take effect in the Sep 30 builds. | Local notification, not server push. Row 14 fires every 7 days from the player's server date for 4 weeks once at the leaderboard unlock level, not at the Monday rollover. Row 9 fires daily at 00:15 server date for 5 days once at level 26. Both are live in code regardless of the sheet. | Same Leonard message as TMD-01, one more clause: anything not LIVE on the sheet is not signed off, even where the client already schedules it. Same dates. Do not claim the client has stopped sending it. |
| TMD-03 | All beats that need the Sep 30 client (Collect & Win first) | Injected deck f_2b9d4e7a1c63f08d5e7b21, Frederick, Sep 23, slide 1: "Scaled beta-cohort buy, starting once the stores approve the Sep 30 builds."; slide 3: "Once the stores approve we start buying users at small scale". #zombie-match3d, Leonard, 2025-09-11 03:31: "submitted to app store, when it's approved we'll start buying users at small scale". Samuel cmt_zom432_2: "both submission builds from today, iOS 50 and Android 135". | Still to do (owner) on each beat, or a global note. Expected: not listed. Alternative: "store approval of the Sep 30 builds (Leonard or Arthur)", since the brief asks what must land "before it runs for bought users" and lists "prod deploy". | SILENCE. Nothing says if approval is a beat still-to-do or who owns it. The prompt fixes the buy start ("start Monday the 6th") but not the approval. | The export cuts at Sep 30, so no approval record exists. Earlier cycles: "0.3.40 is in review on IOS" (Leonard, #executives, Sep 22, not Julia's). | Simplest: reword the two injected slide sentences so they no longer gate on approval. Or Slack #zombie-match3d, Leonard, earliest 2025-09-30 21:08 UTC, latest 2025-10-01 06:59 UTC: both builds are in store review, that is his to chase and not a live-ops item. |
| TMD-04 | Endless | Trello [58] 68c451141c69fb8af1b4568e, list BETA, not dueComplete: "Refill algorithm spawns fewer items over time for both events." Linear ZOM-546, state Todo, assignee Owen. Only cover: injected cmt_zom546_1, Owen, Sep 24: "Refill counts hold level across a long endless run here, the board refills the same amount at the 40th refill as at the second." | Endless Still to do. Expected: nothing. Alternative: "refill bug ZOM-546 (Owen)". Or a build or platform check, since "here" names no build. | SCOPE_GAP. The covering note is the assignee's own claim, it names no build, and the ticket stays Todo. | Commit 163564f4ed "Manual refill logic (#453)", EMPLOYEE_0032, 2025-09-22, is on main, two days before Owen's note. ZOM-516 "refills one item less" is Duplicate. So the outcome "fixed" fits the base. | Linear comment on ZOM-546 by Vincent Parker (usr_65c76e0b87aa7e9b), not Owen, earliest 2025-09-24 19:01 UTC, latest 2025-09-30 23:59 UTC: re-tested on the submission build, refills hold across a long run. Optionally move it to Done. |
| TMD-05 | Endless | Doc f_9956263905ddb43d1500ff (Robert, shared with Julia, mod Aug 14): "Players can play 2 + 1 times per day. The entries resets at midnight GMT. The first 2 entries are FREE, the 3rd one requires an ad watch." Trello [53] "Rewarded Ads": Leonard moved it from BETA: Sep 30 to Oct 21 on 2025-09-23T00:34Z. | Endless Still to do or What players see. Expected: nothing. Alternative: "third entry needs Rewarded Ads, Oct 21 list" or "two entries only until Oct 21". | SILENCE on Endless. The Trello move shows Rewarded Ads left the beta list, but no record says Endless runs without the ad entry. | `EndlessScreen.cs` lines 48 and 83 only ever `adsButton.SetActive(false)`, so the ad entry is not wired. Robert to Brian, D077ALC9VK3, Sep 23 19:48: "We are postponing"; Leonard, D04UP2L3E3S, Sep 23 00:35: "I moved out rewarded ads and axe arena". Julia sees neither. | Trello comment on [53] by Leonard, earliest 2025-09-23T00:35Z, latest 2025-10-01 06:59 UTC: out of the beta, Endless stays on its two free entries, nothing waits on this. |
| TMD-06 | Endless and any beat on Samsung or Android | Trello [58]: "it's still happens for samsung devices, that's why I couldn't repro." (ZOM-535); "if I were to finish a level, I hard freeze at end game victory screen ... Doesn't happen to me, might be again a Samsung issue but I need to see video" (ZOM-559, Todo). Bug Checklist on Android crash: "(Vincent- I think it's fixed but need robert to validate)" (reach UNVERIFIED). | Still to do under brief "an unverified build or platform is a still-to-do". Alternative: "verify Samsung freeze (Oliver)" on Endless or every beat. Same clause as the failed S23 item. | SILENCE. Same shape as the platform's S23 finding. Nothing ties these to a beat or clears them. | ZOM-559 and ZOM-535 are Todo with no comments. ZOM-475 is Todo, and it is SC-8: do not grade it. | Must be written together with the S23 fix. A reply that says only "not reproducible on S23" leaves ZOM-559 open. Add a clause: the home-out freeze is game-wide and tracked on ZOM-559, not an Endless item. See section 3. |
| TMD-07 | Quest rollover | Trello [61] "Add more quests and balance quest rewards - (Leonard/Douglas)", BETA list, not dueComplete. Injected comment 68dac8204f1e9a3b7c2d5e61, Leonard, Sep 29: "More quests get added with the Mon Oct 13 rollover if they are ready. The rollover does not wait on them, the current quests keep running either way." | Quest Still to do. Expected: nothing. Alternative: "balance quest rewards (Leonard/Douglas)". | SCOPE_GAP. The comment covers "more quests" only, not the second half of the card. | Nothing in the base on reward balance. | Edit the injected comment, one clause: reward balance goes in with them. Same author and date. No new row. |
| TMD-08 | Push rows 1, 7, 12, 13 | PNs Beta column D "Push Notification". #zombie-bugs (Julia is a member), Leonard, 2025-09-18 23:52: "All our PNs are local". Not Julia's: Arthur, D06KV30TPL4, Jun 26: "We aren't using Push notifications yet." | Pushes Notes, or a Still to do on Collect & Win, Season Pass or daily gift. Alternative: "no server push pipeline, Send (UTC) cannot follow event start". Expected lists only Not Ready, WIP and naming. | SILENCE. Rows stay held either way, so only the what-is-missing content differs. | The client has no code for these four rows. "Event Start (server time)" cannot be met by timer notifications. | One clause in the TMD-01 message: server-sent pushes are not set up for the beta. True to Leonard and Arthur. |
| TMD-09 | All pushes, go rows 3 and 5 | #zombie-bugs, Robert, 2025-09-18 23:40: "Push notification needs to be pushed back"; 23:51: "There are 3 that quit immediately after seeing Push notification permission prompt". Leonard, Sep 19 14:23: "It's not PNs". | Notes on rows 3 and 5, or the recommendation. Alternative: "permission prompt timing unresolved". | SILENCE in Julia's view. The argument ends with no decision she can see. | #executives Sep 23 (not Julia's): Leonard "I don't think we are on agreement on the desired behavior"; Robert "I just prefer to go with anything that minimizes potential tech issue". No commit on the prompt on main after Sep 5. | Slack #zombie-bugs, Leonard, earliest 2025-09-23 21:02 UTC, latest 2025-09-30: prompt stays as it is for the beta. Weak item, add only if the message is cheap. |
| TMD-10 | Quest rollover | Injected Brian mail Sep 22: "I will have the November season config ready and handed over to you: reward tiers, the daily and weekly quest tables and the premium track." Brief: "Every config a beat needs lands before its lock". | Quest Still to do. Expected: only under Season Pass. Alternative: repeat "November quest tables (Brian), before Oct 31 00:00 UTC" on the quest row. | SILENCE. The Trello "does not wait on them" is about new quests, not this config. | Injected only. | Reword the injected mail (3 copies) to "Season Pass quest tables". Keep the Sep 26 mail. |
| TMD-11 | Endless | Doc f_89c68172f34a475f4ad0a3 "Bug Checklist – v0.3.21 iOS Submission Candidate", Leonard, mod Aug 25, reach UNVERIFIED: "Endless mode: stretched image issue – incorrect aspect ratio."; "after losing, "how to play" screen reappears"; "info button appears twice on first run"; "certain variant ([USERNAME_6108]) is overly difficult"; "Spawn time between monster waves too long". | Endless Still to do: "player-facing art an owner has flagged". Under "P2-ANNOYING PLEASE FIX ASAP". | SILENCE for these five lines (no ticket mark). ZOM-473, 474 and 480 clear the other lines. | Build is superseded: 0.3.40 was in review by Sep 22. ZOM-470 (Aug 25), ZOM-501 and ZOM-485 (Sep 2) and ZOM-433 are Done and may cover them; that is my inference, not a record. | None if domain or anyone reads are out of reach. If in reach, fold into the Trello [58] comment below. |
| TMD-12 | Collect & Win, Season Pass | Doc f_89b6f703a1d10982e129eb "ZM VFX Polish 07.30.2025", Robert, reach UNVERIFIED: "What we don't have but will have soon: Bones (needs recycling system), win&collect potions, axe-arena coins, season pass coins"; "P0 – Collect & Win → may need your help later, but not clear yet". | Still to do: reward animation (Marcus). The doc marks it P0, so it is not "polish nobody flagged". | SCOPE_GAP, weak. Trello [22] Reward Animations was completed Sep 18, and Marcus cmt_zom465_2 names only the icon. Neither names the potions. | Trello [22] done by Leonard. | None needed if out of reach. |
| TMD-13 | Season Pass, Weekly Leaderboard | Bug Checklist, section "PX - TO BE PRIORITIZED", flat lines: "Profile for Leaderboard" / "With slight issues" / "Season Pass" / "Douglas - Calvin Profile bug / polish client sync". | Still to do on either beat. | SILENCE, weak. The doc's list nesting is flat, so what "slight issues" attaches to cannot be read. | Nothing more. | None. |
| TMD-14 | Weekly Leaderboard, Plague Race | Trello [64] "Bot Scoring Improvements [PERSON_NAME_0050]/Douglas", BETA list, open, no description. | Still to do for bot-scored beats (Douglas). | SILENCE, weak. | Backend commit cb29e35 covers boss arena bots only. | One Trello comment on [58] by Leonard (below) could cover it. |
| TMD-15 | All live-ops rewards | Trello [62] "Ability to give different rewards in different liveops ([PERSON_NAME_0050]/Douglas/Client Team)", list Oct 21, a date inside W3. | Still to do or a mid-span change. | SILENCE, weak. | Nothing more. | None. |
| TMD-16 | None named | Trello [79] "Fix TECH ISSUES", BETA list, created Sep 23, empty. | Still to do on any beat, with no owner. | SILENCE, weak. | Leonard, D04UP2L3E3S, Sep 23 00:37 (not Julia's): "Fix tech issues, google/Apple login, win & collect, queue manager + other minor bug fixes." | Same [58] comment. |
| TMD-17 | None named, bought users | Trello [54] Google/Apple Login, open, BETA list. Injected cmt_zom544_1, Vincent: "progress does not restore yet". | Global still-to-do. Not a beat. | SILENCE, weak. | ZOM-544 In Progress. SC-14 covers this card's two complete flags. | Same [58] comment. |
| TMD-18 | Push row 12 | R13 K: "Check the login calendar — fresh rewards are here! Tap in every day this month". The in-game name is Daily Gift (Vision Bot sheet R47: ""Daily Gift" overlay"). | What is missing: wrong event name, in addition to Not Ready and WIP. | SILENCE, weak. The brief itself says "the Login Calendar row". Status is held either way. | Row has no client code. | None. Keep the rubric from requiring or rejecting the extra name note. |
| TMD-19 | Recommendation only | Deck f_ccd36b8c7ef6c6f9f6a38a "Weekly Update Oct 24", shared with Julia, slide 0: "Company Update, Oct 24 2025"; slide 5: "De-prioritize Zombie Match unless metrics are spectacular in the next 2 weeks." | Trade-offs in the DM. | SILENCE. It is dated after the clock. Drive created_time is 2025-08-29. Not in synthcut.md. | Date mismatch inside the base, likely a date-shift artifact. | None. Add to known issues and keep the rubric off it. |

**Bundling option.** One Leonard comment on Trello [58], dated Sep 30 around 16:40Z (he moved the card then), could cover TMD-14, 16, 17 and part of 06: these are game-wide fixes and none of them gates an event's start. Leave ZOM-546 out of that claim, because the card itself ties it to "both events".

## 2. Settled candidates (RECORD), kept so a reviewer can see they were looked at

| id | beat / row | item | settling quote | base agrees? |
|---|---|---|---|---|
| R-01 | Rows 3, 5 | No game name in copy | Reply: "Copy that does not name the game at all is fine to go out, the naming rule is only about wrong names." | Yes. Client strings match the sheet. |
| R-02 | Rows 9, 14 | "Ready" in column B against brief "whether its push is ready" | Brief: "only if its row is Ready and LIVE". | Yes on the sheet. See TMD-02. |
| R-03 | Row 1 | "Revisit once new quests roll out." plus Trello "Mon Oct 13": held until Oct 13? | Brief: "put down whether the beat is in and whether its push is ready, not its window dates." Row is Not Ready. | Yes. Notes text may vary, status does not. |
| R-04 | Rows 2, 8, 10, 11 | Hourly, Nathan, Streak Fever, Axe Arena | Reply: "Leave off the four rows". Trello [73] Hourly Collection moved to Backlog Sep 23. | Yes. |
| R-05 | Tab PN BETA Translated | "River Rush Is On!", different leaderboard copy, Tiledozer row | Brief: "the translated tab is the old Domino set". | Yes. |
| R-06 | Tab PNs, Deep Links (not used) | Domino rows, "Consider incentivizing on version 2" | Reply: "plan the PNs Beta tab". | Yes. |
| R-07 | Endless | No push row | Reply: "plan the PNs Beta tab as it stands". | Yes. |
| R-08 | Axe Arena | Trello [9] in list Oct 21, inside W3 | Reply: "things that are not in the beta". Brian cmt_zom526_2 "once that event is back". | Yes. |
| R-09 | Collect & Win | Trello [63] Queue Manager complete against ZOM-543 In Progress | Trello completed by Leonard 2025-09-30T16:40Z, after Calvin's 16:20; Calvin: "current flow is ... plus Collect and Win". | #472 merged Sep 30. |
| R-10 | Collect & Win, Season Pass | Trello [10], [27] | dueComplete true, Sep 30 and Sep 18. | SC-14 does not cover these cards. |
| R-11 | Quests | Trello [58] "Consecutive login quest not working" | ZOM-557 Done 2025-09-30. | Fix 0a2951f054, Sep 22, on main. |
| R-12 | Weekly Leaderboard | Trello [58] "Weekly star count has the wrong image" (player-facing art) | ZOM-558 Done 2025-09-23. | Yes. |
| R-13 | Plague Race | Slack Aug 4: levels above 100 "don't count toward the race" | ZOM-459 Done 2025-08-25. | Yes. |
| R-14 | Plague Race | Trello [1] "unlocks at level {X}", Julia to specify | ZOM-413 Done; client constant is level 26. | Yes. |
| R-15 | Plague Race, Endless | Trello [22] desc: Plague Race lives animation, Endless rewards VFX | dueComplete Sep 18; ZOM-463 Done. | Yes. |
| R-16 | Endless | Bug Checklist "ending screen sometimes skipped", "Rocket ready button too faded" | ZOM-473 Done Sep 22, ZOM-474 Done Aug 25. | Yes. |
| R-17 | Endless | Doc: "resets at 12:00:01 AM Monday GMT"; daily chest line also says Monday | Confluence F12: "resets daily at 00:00 UTC and weekly on Monday 00:00 UTC" (platform's quote). | One-second difference, no effect. |
| R-18 | Plague Race | LiveOps Event Calendar sheet, River Rush on Mon, Wed, Fri | Brief: no window dates for Plague Race. | Sheet is Feb 2025, Domino names. |
| R-19 | Collect & Win | Same sheet: C&W Mon-Tue, Wed-Thu, Fri-Sun | Matches the brief. | Yes. |
| R-20 | Season Pass | Holiday sheet: 2025-10-29 Republic Day (Turkey column), a clash with Brian's Oct 29 | F15 objective boundary: any date before Oct 31 00:00 UTC. | Rubric must not require Oct 29. |
| R-21 | Season Pass | Reply on the Sep 22 or Sep 26 mail | Sep 26: "Treat Fri Oct 31 as the date I am committing to"; "reply on this mail". | Injected. |
| R-22 | Collect & Win | GCal release 2025-10-08 15:00 UTC, organizer Douglas | Only release event on any calendar. Window Oct 8 pre-empted, first window Oct 10. | Injected; nothing in the base contradicts it. |
| R-23 | All | Stale unchecked items on [14], [4], [5] and others (section 4) | Cards dueComplete; Arthur #470 rc_10 has Endless and leagues on prod. | June estimates, not work items. |
| R-24 | Analytics | Data Dictionary "I don't know what endless mode rewards are"; [66] CPM_history; Eksik Loglar | Brief: "not analytics". | Yes. |
| R-25 | Domino files | DD Global Launch Readiness, GTM - Beta, 10_2_2024 Submission Build Bugs | Domino only. | Yes. |

## 3. Cross-references to the three known platform forks

- **ZOM-534 (main against prod):** nothing in Trello, Gmail or Drive mentions it. GCal injected event says "Prod backend deploy for the beta" but scopes itself to "the server windows that are still on the DEV stack", so a reader cannot use it as a settling record unless it is extended.
- **Leonard's S23 freeze:** no Trello, Gmail, GCal or Drive record mentions it. Two cautions for the fix. The company device list (Harmony Games Devices, reach UNVERIFIED) shows no S23, only S21 Ultra (Robert) and S22 Ultra, so a Vincent re-test "on the S23" may not ring true; Leonard, the reporter, is the safer author. It must also not imply Samsung is clean, because ZOM-559 and ZOM-535 stay open (TMD-06).
- **#477 header title:** no Trello, Gmail or Drive record names it. Trello [10] Win and Collect was marked complete by Leonard at 2025-09-30T16:40Z, which makes a Leonard comment on [10] a natural place for the settling line.

Seen in passing, for the GitHub slice: three commits on main postdate Samuel's "submission builds from today" note: 93f45ebbfc (Season Pass main screen, Sep 30 21:36 UTC), 25c6c66b6b (popups and endless_02, Sep 30 21:20 UTC), 0ff577550e ("Fix end popup", Oct 1 05:44 UTC). Whether they are in iOS 50 and Android 135 is not shown.

## 4. Trello census

Boards: ZM ROADMAP (6851a6569f3bf818760632ab) is the only active ZM3D board: 79 cards, 69 open, 10 closed. Open by list: BETA: Oct 10 18, Jun 30th 9, July 18 9, Backlog 9, Oct 21 8, Jul 24 7, Jun 18th 5, July 30 4. List "BETA: Oct 10" is the SC-13 list. Closed cards were read and none touches an open item.

Other boards: UA/BD list "ZM 3d Technical Launch / Alpha" has 15 open cards (ads, store assets, alpha geos), last activity March 2025, no beat. No description, checklist or comment there names a beat. On DD Product Roadmap and Harmony Games the beat words are Domino-era. The one Sep 2025 hit is "Follow up on ZM investor video and UA creative" (list Done).

Comments: the 12 base ZM ROADMAP comments all date from 2025-06-23 to 2025-07-02; the only later comment is the injected one on [61]. Attachments: one image, on [21].

| card | list | name | dueComplete | beat touched | unchecked |
|---|---|---|---|---|---|
| [10] | BETA: Oct 10 | Win and Collect - [PERSON_NAME_0092]/[PERSON_NAME_0067] | yes | Collect & Win | 0 |
| [22] | BETA: Oct 10 | Reward Animations (VFX) - [PERSON_NAME_0092]/Marcus/[PERSON_NAME_0029] | yes | Plague Race, Endless VFX (R-15) | 0 |
| [26] | BETA: Oct 10 | Infinite HP Boss Mode - ([PERSON_NAME_0054]/[PERSON_NAME_0120]) | yes | Boss Arena (off) | 0 |
| [27] | BETA: Oct 10 | Season Pass - ([PERSON_NAME_0092]/[PERSON_NAME_0022]) | yes | Season Pass | 0 |
| [54] | BETA: Oct 10 | Google/Apple Login ([PERSON_NAME_0050]/[PERSON_NAME_0120]) | no | None (TMD-17) | 0 |
| [55] | BETA: Oct 10 | 300 Levels Manmade - but the goal is have enough content for D7 - [PERSON_NAME | yes | No | 0 |
| [56] | BETA: Oct 10 | Algo Levels V2.1 - [PERSON_NAME_0050] | no | No | 0 |
| [58] | BETA: Oct 10 | Minor Bugs to Fix - [PERSON_NAME_0050] | no | Several (TMD-04, 06; R-11, 12) | 0 |
| [60] | BETA: Oct 10 | Shop Inventory Review and Additions ([PERSON_NAME_0092]/[PERSON_NAME_0054]) | no | No | 0 |
| [61] | BETA: Oct 10 | Add more quests and balance quest rewards - (Leonard/Douglas) | no | Quest rollover (TMD-07) | 0 |
| [63] | BETA: Oct 10 | Queue Manager - [PERSON_NAME_0092]/[PERSON_NAME_0029] | yes | Collect & Win (panel queue) | 0 |
| [64] | BETA: Oct 10 | Bot Scoring Improvements [PERSON_NAME_0050]/Douglas | no | Leaderboard, Plague Race bots (TMD-14) | 0 |
| [65] | BETA: Oct 10 | Pre-level Dialogue Change ([PERSON_NAME_0054]/[PERSON_NAME_0040]/Martin) | no | No | 0 |
| [66] | BETA: Oct 10 | CPM_history (lt_avg, lt_median, last_30, last_20, last_10) Leonard by next rel | no | Analytics only | 0 |
| [67] | BETA: Oct 10 | Adaptive Difficulty Learnings to tier players into different buckets([PERSON_N | no | No | 0 |
| [68] | BETA: Oct 10 | Adjust airstrike balance??? ([PERSON_NAME_0054]/[PERSON_NAME_0040]) | yes | No | 0 |
| [72] | BETA: Oct 10 | Revisit All Boosters ([PERSON_NAME_0054]/[PERSON_NAME_0120]) | no | No | 0 |
| [79] | BETA: Oct 10 | Fix TECH ISSUES | no | None named (TMD-16) | 0 |
| [9] | Oct 21 | Axe Arena (Win streak multiplier scoring) (link) - ([PERSON_NAME_0092]/[PERSON | no | Axe Arena (off, R-08) | 0 |
| [46] | Oct 21 | Server-side inventory (Douglas/[PERSON_NAME_0120]/Blake to provide card_ids) | no | No | 0 |
| [48] | Oct 21 | Conversion System 2.0 (needs Spec [PERSON_NAME_0050] and art from Martin) | no | No | 0 |
| [53] | Oct 21 | Rewarded Ads ([PERSON_NAME_0092]/[PERSON_NAME_0054] to Support) | no | Endless ad entry (TMD-05) | 0 |
| [57] | Oct 21 | Improve Performance on low-end devices - ([PERSON_NAME_0050]/Leonard) | no | Performance (brief: no hold) | 0 |
| [59] | Oct 21 | Pop-up Offers via HE - [PERSON_NAME_0092] | no | No | 0 |
| [62] | Oct 21 | Ability to give different rewards in different liveops ([PERSON_NAME_0050]/Dou | no | All live-ops rewards (TMD-15) | 0 |
| [75] | Oct 21 | Zombie Unlock Videos | no | No | 0 |
| [24] | Backlog | social team battles - [PERSON_NAME_0092] + [PERSON_NAME_0050] + [PERSON_NAME_0 | no | No | 0 |
| [39] | Backlog | Introduce wild cards of each rarity. These can be used as materials to upgrade | no | No | 0 |
| [40] | Backlog | Introduce a mode that rewards bones currency. Bones will be used to buy bone p | no | No | 0 |
| [47] | Backlog | End Game - [PERSON_NAME_0092] | no | No | 0 |
| [73] | Backlog | Hourly Collection | no | Hourly Coins (off) | 0 |
| [74] | Backlog | [USERNAME_0152] | no | No | 0 |
| [76] | Backlog | Lava Event | no | No | 0 |
| [77] | Backlog | PvP Event | no | No | 0 |
| [78] | Backlog | Fake PvE Coop | no | No | 0 |
| [14] | Jul 24 | [Feature] Endless Mode - [PERSON_NAME_0120] | yes | Endless | 2 |
| [23] | Jul 24 | Ask Lives / Lives Bank ([PERSON_NAME_0067]) | yes | No | 0 |
| [25] | Jul 24 | New Monsters with Animation and new Background ([USERNAME_24761]) | yes | No | 0 |
| [28] | Jul 24 | Player profile Individual - [PERSON_NAME_0029] | yes | No | 0 |
| [35] | Jul 24 | [Tools] A/B test tool for levels, FTUE, unlocks, etc. (Blake) | yes | No | 1 |
| [37] | Jul 24 | [Implement] social (Guild, guild admin, chat, life gift) - [PERSON_NAME_0092]  | yes | No | 1 |
| [45] | Jul 24 | Marketing Video Refresh (Marcus/[PERSON_NAME_0036]) | yes | No | 0 |
| [5] | July 18 | [Feature] Trophy Path ([PERSON_NAME_0022]) | yes | Trophy Path = Zombie Lane (off) | 2 |
| [6] | July 18 | [Feature] Daily Login - [PERSON_NAME_0029] + [PERSON_NAME_0092] | yes | Daily gift | 0 |
| [13] | July 18 | Haptics (Leonard/Blake) | yes | No | 0 |
| [29] | July 18 | New FTUE for Items ([PERSON_NAME_0092]/[PERSON_NAME_0022])? | yes | No | 0 |
| [33] | July 18 | NEEDS TICKET [Customer Service] Help Shift Integration [July 4th] - [PERSON_NA | yes | No | 0 |
| [41] | July 18 | Rate us (Samuel) | yes | No | 0 |
| [42] | July 18 | Adding Analytics for Missing Events (Leonard/Blake) | yes | Analytics only | 0 |
| [43] | July 18 | iPad compatibility (Blake/[PERSON_NAME_0050]/Leonard/Samuel) | yes | No | 0 |
| [44] | July 18 | Moving Calm Play SKU into Harmony Games (Leonard/Blake) | yes | No | 0 |
| [49] | July 30 | Icon Management System (Show what live ops unlocks at what level) ([PERSON_NAM | yes | Live-ops icons | 0 |
| [50] | July 30 | Out-of-lives redirect to shop ([PERSON_NAME_0067]) | yes | No | 0 |
| [51] | July 30 | Profiling heat up - Blake | yes | No | 0 |
| [52] | July 30 | Player profile Other Players - [PERSON_NAME_0029] | yes | No | 0 |
| [1] | Jun 18th | [Live ops] Plague Race (AKA Mine Dash) - [PERSON_NAME_0022] (link) | yes | Plague Race (R-14) | 0 |
| [3] | Jun 18th | Level Adjustments | yes | No | 0 |
| [19] | Jun 18th | [USERNAME_14171] v2.0 | yes | No | 0 |
| [31] | Jun 18th | Card upgrade VFX implementation | yes | No | 0 |
| [32] | Jun 18th | Tutorial language update for blunder | yes | No | 0 |
| [2] | Jun 30th | [Bugs] Gameplay Related Bugs - [PERSON_NAME_0120] | yes | No | 0 |
| [4] | Jun 30th | [Feature] Quests and Milestones and Achievements - [PERSON_NAME_0022] | yes | Quests | 2 |
| [7] | Jun 30th | [Feature] Push Notifications - Samuel + Leonard | yes | Pushes | 0 |
| [8] | Jun 30th | [Estimate] social (Guild, guild admin, chat, life gift) - [PERSON_NAME_0092] + | yes | No | 1 |
| [15] | Jun 30th | [Improvement] Equipped Card Item Infusion VFX implementation - [PERSON_NAME_01 | yes | No | 2 |
| [21] | Jun 30th | [Improvement] QoL Features for Level Design Tool (Blake) | yes | No | 1 |
| [30] | Jun 30th | [Estimate] Monster Mechanics 2.0 - [PERSON_NAME_0120] | yes | No | 1 |
| [34] | Jun 30th | [Boost] Implement Time-Based Preload Boost - [PERSON_NAME_0029] | yes | No | 0 |
| [36] | Jun 30th | [Feature] Dynamic Item Removal Based on Win Streak Rewards | yes | No | 0 |

Unchecked items on ZM ROADMAP (13, all on dueComplete cards, all from June):
- [14] Endless: "Backend reads GDD and give their estimates", "Set Priority"
- [4] Quests: "Provide engineering estimate", "Set Priority"
- [5] Trophy Path: "Backend team needs to read GDD", "Set Priority"
- [15] Item Infusion VFX: "Marcus to create VFX", "Engineer to implement"
- [8], [30], [35], [21], [37]: "Provide engineering estimate"

Trello [58] tickets at the clock. Open: ZOM-475 (SC-8), 539, 554, 546, 438, 535, 559, 520, 477, 481, 483, 458, 560. Done: ZOM-557, 558, 498, 536, 561.

## 5. Push sheet: all 14 rows against the client

Sheet last modified 2025-06-23. No notes column beyond F "Details"; columns M to Z and rows 16 to 987 are empty.

| row | sheet | what | B Status | I Status | type (col D) | in client? | client copy against sheet |
|---|---|---|---|---|---|---|---|
| 1 | R2 | Quests rollover | Not Ready | LIVE | Push | No | n/a |
| 2 | R3 | Hourly Coins (off) | Not Ready | LIVE | Local | No | n/a |
| 3 | R4 | Lives recharged | Ready | LIVE | Local | Yes | Same |
| 4 | R5 | 1 day lapsed | Ready | LIVE | Local | Yes | **Client says Zombie Match 3D, sheet says Puzzles vs Zombies** |
| 5 | R6 | 7 days lapsed | Ready | LIVE | Local | Yes | Same |
| 6 | R7 | FTUE | Ready | LIVE | Local | Yes | **Client says Zombie Match 3D, sheet says Puzzles vs Zombies** |
| 7 | R8 | Win & Collect | Not Ready | WIP | Push | No | n/a |
| 8 | R9 | Nathan (off) | Not Ready | WIP | Push | No | n/a |
| 9 | R10 | Plague Race | Ready | WIP | Push | **Yes, as local** | Same text |
| 10 | R11 | Streak Fever (off) | Not Ready | WIP | Push | No | n/a |
| 11 | R12 | Axe Arena (off) | Not Ready | WIP | Push | No | n/a |
| 12 | R13 | Login Calendar | Not Ready | WIP | Push | No | n/a |
| 13 | R14 | Season Pass | Not Ready | WIP | Push | No | n/a |
| 14 | R15 | Weekly Leaderboard | Ready | WIP | Push | **Yes, as local** | Same text, emoji differ |

## 6. Coverage

Scanned in full:
- **Trello:** data.json, all 5 boards, 47 lists, 803 cards, 54 checklists, 161 check items, 76 attachment records, 5,252 actions. ZM ROADMAP read card by card, actions from Aug 15 listed one by one. Other boards by keyword over names, descriptions, checklists and comments, plus every card on the ZM and Beta lists. The injected action is read from the SQL.
- **Gmail:** Julia's whole mailbox, all 253 threads and 304 messages, 2023-07-16 to 2025-09-17. Window Aug 15 to clock: 2 base messages (Aug 22 Slack notice with an empty body; Sep 17 cancelled 1:1), plus the 2 injected Brian mails. All of 2025 read. No Linear notification, POD or standup note, beta plan or QA report exists there. The mailbox was also keyword-scanned for beats and beta (101 hits, nearly all "request" matching "quest").
- **GCal:** data.json, 10,395 events, 7,292 on Julia's calendar or with her as attendee. Sep 1 to Nov 5: 95 rows, 9 distinct events (POD: PROTOTYPE x5, Engineering Focused Weekly Planning x2, a Sep 2 meeting Julia organised, the cancelled 1:1). The export has no description field. A title scan of all calendars, Aug 15 to Nov 30, for beat, release, season, beta and store terms found nothing. The Oct 8 release is injected only.
- **Drive family:** 53,631 Drive records. Reachable set 275: 186 owner or shared (28 owned), 89 more domain or anyone (UNVERIFIED). Text extracted for 254; keyword-counted on 14 beat and beta terms; 81 hit. No folder inheritance adds anything. Injected brief, UA deck and calendar sheet read from the SQL.
- **Read in full:** Push Notifications Zombie Match (all 4 tabs; translated tab English columns plus the first translations), Bug Checklist, LiveOps Event Calendar, Live Ops Planning, Collect & Win Endpoints, Plague Race, ZM VFX Polish, ZM Ideas for Beta, GTM - Beta, Tech Stack, Weekly Update Oct 24, Master GDD, Quests And Achievements, ZM QA Checklist, QA - June 2025, Blocker List, Roadmap New Hires, Eksik Loglar, Feature Owners, Quest System Backend tasks, Debug Wishlist, Leaderboard API, Plague Race API, Vision Bot Test Cases, Event Icon Management, Harmony Games Devices.
- **No tracker found:** no Drive sheet has an open row per beat, and there is no beta checklist or launch plan for ZM3D beyond the Bug Checklist.

Partly read:
- Endless GDD: rules, flagged lines and tail (32 KB, the middle is refill maths).
- Testing and GDD, App Version Tracker, ZM3 bots, TrophyPathSchedule, Data Dictionary, Pitch - Internal, Comparison Table, Haptics, FTUE Steps DEPRECATED, DD Global Launch Readiness: head or beat lines only.
- Large data sheets (Loc files, I2Loc, puzzle_data, StatsWFavorsTarget, IAP Data, ExportedLevelItems, ExportedLevelMonsters): keyword only.

Not scanned:
- 19 PDFs in Julia's reach (most are exports of decks already read as slides) and 2 folders.
- Gmail .ics attachments, Trello image attachments, images inside docs.
- Doc comments: the export has none.
- Linear, GitHub and Slack beyond targeted checks for the items above. Slack term scans, Jul to Sep unless noted: rewarded ads, Plague Race levels, store review (Sep only), push and notification (Jun to Sep). These are not a channel census.
- Confluence, Snowflake, Universe_Normal.
