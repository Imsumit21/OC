# Injection review C2: factual-consistency half of Check C

- Review version: injection-static-v2
- SQL: Task_Authoring/task_inputsK/01_Universe_Inject.sql, sha256 0c1cf21627d5d9fb6303127c005cbaab216522c5ba1bf25a1e04573a44d24dad (hash confirmed; 137 INSERT, 8 UPDATE, BEGIN, COMMIT = 147 statements)
- Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
- Scope: factual claims in injected text only. Timestamps and lifecycle fields, Checks A and B, voice, realism, difficulty and decoy counts are out of scope.

## Result for this half: PASS

No claim is CONTRADICTED after resolving identity, effective time, scope and source authority. No grader-facing text and no padding record.
This PASS has limits: 27 claims need repo blobs and are UNVERIFIABLE, and 5 notes below need a reader's decision. N1 is the only one that touches injected text in a way a literal grader could fail.

Counts (table rows; each Table B row counts its two parts separately): 150 claims. SUPPORTED 111, CONTRADICTED 0, UNSUPPORTED 12, UNVERIFIABLE 27.

## Evidence key

| Key | Source |
|---|---|
| SHEET | gsheets data.json /sheets_spreadsheets/220/sheets/1/grid (tab "PNs Beta") |
| SHEET0 | same spreadsheet /sheets/0/grid (tab "PNs") |
| H248 | github data.json /review_comments/605 (#248 rc_16 diff_hunk, NotificationManager.cs). SQL L81 hunk equals its first 250 lines exactly (compared line by line) |
| K248 | github /review_comments/609 (#248 rc_4, ZombieConstants: FirstTurorialFinished = 20, LeaderboardsUnlockLevel = 22, PlagueRaceUnlockLevel = 25) |
| T263 | github /review_comments/652 (#263 rc_4, NotificationToggleButton.cs) |
| PR248 | github /pull_requests/2128 (author EMPLOYEE_0004, merged_by EMPLOYEE_0025, merged 2025-06-26T21:23:32Z) |
| LO | confluence /pages/27 (page_liveops_calendar, updated 2025-09-29) |
| SP | confluence /pages/20 (ZM3D Season Pass spec) |
| EXEC | slack messages/C07C2866011/2025-09.json (#executives) |
| ZM | slack messages/C0880U9751A/<month>.json (#zombie-match3d) |
| BUGS | slack messages/C08R27X0EAH/<month>.json (#zombie-bugs) |
| BE | slack messages/C08R6BF4ENN/<month>.json (backend API posts) |
| TR | trello data.json (board 6851a6569f3bf818760632ab) |
| D199, D563, D4, D279 | gdocs data.json /docs_documents/N (Plague Race; Infinite HP Boss GDD; Zombie Lane; Collect&Win v1.0) |

## Table A: facts checkable against the base or other injected records

| # | Claim | SQL line | Verdict | Evidence |
|---|---|---|---|---|
| A1 | The sheet has two status columns | L15 | SUPPORTED | SHEET row 0: "Status" and "Status (NA, WIP, LIVE)" |
| A2 | ZM ROADMAP has a BETA list | L15 | SUPPORTED | TR /lists/42, id 6851a674975da1fe76e70d93. Doc gives no date, so SC-13 is avoided |
| A3 | Vincent has a QA note defining "seen" | L15 | SUPPORTED | Injected L59, L63 |
| A4 | The permission ask is Robert's call | L15 | SUPPORTED | EXEC /944 Arthur asks Leonard and Robert for desired behaviour; ZM 2025-09 /300 Robert set the timing; injected L34 |
| A5 | Client strings are hard-coded | L15 | SUPPORTED | H248; github /review_comments/613 "notification strings are hardcoded" |
| A6 | A settings toggle exists, separate from the ask | L15 | SUPPORTED | T263; Linear ZOM-314 /issues/3370 |
| A7 | DES-314 is the string-ticket parent | L15 | SUPPORTED | Injected L96 |
| A8 | Android 0.3.127 was a store build on Sep 24 | L20, L168, L172, L176, L184, L190 | SUPPORTED | EXEC /908 "0.3.127 on AnDroid (we just published it)"; EXEC /1020 "that's the latest" |
| A9 | iOS 0.3.40 was a store build on Sep 24 | L20, L168, L172, L176, L190 | SUPPORTED | slack messages/D06477JGUKT/2025-09.json /183 "iOS I just released", /186 "0.3.40" (Sep 23); ZM 2025-09 /407 |
| A10 | The six checked rows are the six Ready rows | L20 | SUPPORTED | SHEET: 6 rows with Status = Ready, same six messages |
| A11 | Plague Race iOS cell reads "iPhone", no version | L20 | SUPPORTED | Injected L184, later explained by L41 |
| A12 | Deck says 6 Ready on the PN sheet | L29 | SUPPORTED | SHEET count = 6 |
| A13 | The readiness deck says 6 | L32 | SUPPORTED | Injected L29 (see N2 on who can read it) |
| A14 | Our own ask runs after level 20 | L34 | SUPPORTED | EXEC /943, /952; BUGS 2025-07 /1237; ZM 2025-09 /300; commit /commits/7579 |
| A15 | Robert is not pushing it further | L34 | SUPPORTED | Reverses ZM 2025-09 /300 "punt this even further". A dated later decision |
| A16 | Leonard said PNs matter for retention | L34 | SUPPORTED | EXEC /968 "not having any PN will hurt retention imo" |
| A17 | Unity shows a popup at launch on iOS | L34 | SUPPORTED | EXEC /943, /952 "Unity itself is triggering this one" |
| A18 | That popup alone switches nothing on | L36 | SUPPORTED | H248: OnApplicationFocus writes only the PlayerPrefs string; NotificationsEnabled changes in Enable/Disable. June code; current client is a blob |
| A19 | NotificationManager schedules only after our ask, both platforms | L36 | SUPPORTED | Scoped to popup versus ask: H248 `if (!NotificationsEnabled ...) return`. Literal "only" is over-broad, see N1 |
| A20 | A "taken over" push exists | L38 | SUPPORTED | H248 WeeklyReminderTitle; SHEET |
| A21 | Thread goes from 3 to 4 replies, 3 to 4 repliers | L39 | SUPPORTED | messages/C08R8CHB0QL/2025-09.json /255 rc 3, repliers 0005, 0009, 0033; Leonard is new |
| A22 | Vincent passed the race on iPhone earlier | L41 | SUPPORTED | Injected L184, L20 (correction by a later dated record) |
| A23 | Android is fine for the race | L41 | SUPPORTED | Injected L184, L20 |
| A24 | DM parent gets 1 reply, 1 replier | L42 | SUPPORTED | messages/D06UFE81RF0/2025-09.json /24 rc 0 |
| A25 | PN sheet says six are Ready | L44 | SUPPORTED | SHEET |
| A26 | A PNs Beta tab exists | L44, L96 | SUPPORTED | gsheets /sheets_spreadsheets/220/sheets/1 title "PNs Beta" |
| A27 | Warehouse has D1 and D7 for the Sep 15 cohort week, iOS and Android | L44 | SUPPORTED | snowflake /tables/10/rows/236 android D1 37.86 D7 10.68; /237 ios D1 31.65 D7 9.28 |
| A28 | Leonard made tickets for the sheet rows under DES-314 | L44, L96 | SUPPORTED | 13 of 14 rows have a child; the 14th (Win & Collect) is DES-313, and L44 itself covers existing tickets under another name, see N5 |
| A29 | People added asks under DES-314 | L44 | SUPPORTED | Injected DES-328 to DES-346 |
| A30 | "our push notifications card" exists | L44, L47, L50 | SUPPORTED | TR /cards/705, idShort 7, ADparqb9, list Jun 30th |
| A31 | Money is about to go behind beta | L44 | SUPPORTED | EXEC /1153 to /1160; ZM 2025-09 /125 |
| A32 | Card was dueComplete true before Sep 24 | L47, L48 | SUPPORTED | TR /cards/705; action 6862c0874151cf6318d91742 |
| A33 | Actor PERSON_6094 is Leonard | L47, L50, L53 | SUPPORTED | TR /members: Leonard Hayes |
| A34 | Card has no checklist yet | L50, L51 | SUPPORTED | TR /cards/705 badges checkItems 0 |
| A35 | Comment counts become 2 and 1 | L51, L54 | SUPPORTED | Base badges comments 1 (/cards/705) and 0 (/cards/802) |
| A36 | Fix TECH ISSUES is card 79 on the BETA list, named "BETA: Sep 30" in actions | L53 | SUPPORTED | TR /cards/802; action 68d1eb90bef538c7c5c559bc; SC-13 |
| A37 | Beta build was not yet out on Sep 29 | L53 | SUPPORTED | LO "not yet live"; messages/C05KNDCHAAG/2025-09.json /21 target Sep 30 |
| A38 | Linear Design has a Backlog state | L53 | SUPPORTED | Linear team_DES issues: 3 in Backlog |
| A39 | Phone message checks sheet exists | L59 | SUPPORTED | Injected L12, L18, L20 |
| A40 | Mail sits in Samuel's PR #248 thread; he authored it | L65 | SUPPORTED | gmail threads/samuel@harmonygames.co_1836006988541924555.json subject matches; PR248 author EMPLOYEE_0004 = Samuel |
| A41 | Weekly batch counts from the day they last left | L65, L81 | SUPPORTED | H248: serverToday in ScheduleDominoNotifications, called on focus loss |
| A42 | It is not tied to the rollover | L65, L81 | SUPPORTED | H248 `referenceDate.AddDays(i * 7)` |
| A43 | "Fine to merge" fits what Arthur did | L65, L81 | SUPPORTED | github /reviews/1942 APPROVED 21:23:25Z; PR248 merged by Arthur 21:23:32Z, after the 20:58:14Z comment |
| A44 | Comment path and hunk are real | L81 | SUPPORTED | H248, identical over 250 lines |
| A45 | 10am El Salvador is 16:00Z, and that is Samuel's invite zone | L69, L76 | SUPPORTED | Samuel's base invites use "Central Standard Time - El Salvador" (6 sampled; bounded search) |
| A46 | The weekly one repeats for four weeks | L73 | SUPPORTED | H248 `BatchScheduleWeeklyNotifications(..., 4, serverToday)` |
| A47 | Day 14 is already covered | L73 | SUPPORTED | H248: i = 2 gives day 14 |
| A48 | Event is cancelled on both calendars | L76, L78 | SUPPORTED | Injected L73 |
| A49 | Next free DES number is 313; counter ends at 346 | L94, L297 | SUPPORTED | Linear team_DES max DES-312 (247 issues, full scan); DES-346 is the top new number |
| A50 | Three Collect & Win windows a week | L94 | SUPPORTED | LO "three staggered windows (Mon-Tue, Wed-Thu, Fri-Sun)"; D279 |
| A51 | Collect & Win is the sheet's Win & Collect | L94 | SUPPORTED | LO "Same feature as Win & Collect ... under a different name"; TR /cards/708 |
| A52 | Team Design holds these tickets | L96 | SUPPORTED | Linear team_DES name Design |
| A53 | DES-315 fields match the sheet | L98 | SUPPORTED | SHEET, script match of detail, When, headline |
| A54 | DES-316 fields match the sheet | L100 | SUPPORTED | SHEET |
| A55 | DES-317 fields match the sheet | L102 | SUPPORTED | SHEET |
| A56 | DES-318 fields match the sheet | L104 | SUPPORTED | SHEET |
| A57 | DES-319 fields match the sheet | L106 | SUPPORTED | SHEET |
| A58 | DES-320 fields match the sheet | L108 | SUPPORTED | SHEET |
| A59 | DES-321 fields match the sheet | L110 | SUPPORTED | SHEET |
| A60 | DES-322 fields match the sheet | L112 | SUPPORTED | SHEET |
| A61 | DES-323 fields match the sheet | L114 | SUPPORTED | SHEET |
| A62 | DES-324 fields match the sheet | L116 | SUPPORTED | SHEET |
| A63 | DES-325 fields match the sheet | L118 | SUPPORTED | SHEET |
| A64 | DES-326 fields match the sheet | L120 | SUPPORTED | SHEET |
| A65 | DES-327 fields match the sheet | L122 | SUPPORTED | SHEET |
| A66 | The six Ready messages were built in match3d #248 | L98 to L108 | SUPPORTED | H248 schedules all six; PR248 |
| A67 | Quests are already in production | L110 | SUPPORTED | TR /cards/702 complete; BUGS 2025-07 /653; SHEET LIVE |
| A68 | Daily login is already in the game | L112 | SUPPORTED | TR /cards/704; ZM 2025-08 /64 |
| A69 | Endless uses limited entries | L124, L220 | SUPPORTED | BE 2025-07 /132 used_entries max 3; ZM 2025-09 /18 daily_max_entries 3 |
| A70 | The Endless week closes | L126 | SUPPORTED | LO "weekly reset Monday 00:00 UTC" |
| A71 | Boss Arena has a weekly board | L128, L130 | SUPPORTED | BE 2025-09 /0 /api/boss-arena/weekly; D563 |
| A72 | ZOM-542 concerns Boss Arena | L128, L295 | SUPPORTED | Linear /issues/3617 |
| A73 | Season Pass has a season end | L132 | SUPPORTED | SP monthly reset on the 1st |
| A74 | Free and premium tracks exist | L134, L240 | SUPPORTED | SP |
| A75 | A race has an end | L136, L138 | SUPPORTED | D199 timer, Default State shows time left |
| A76 | Zombie Lane rewards can sit unclaimed | L140 | SUPPORTED | LO; D4; Linear ZOM-385 /issues/3448 |
| A77 | Achievements carry claimable rewards | L142 | SUPPORTED | TR /cards/702; slack messages/C05H8KVNU67/2025-06.json /109 |
| A78 | A daily gift chest exists, separate from the calendar | L144 | SUPPORTED | ZM 2025-07 /912; BUGS 2025-07 /1422; Linear ZOM-556 /issues/3632 |
| A79 | DES-322 is the calendar refresh | L144 | SUPPORTED | Injected L112 |
| A80 | The shop already gives free coins | L146 | SUPPORTED | ZM 2025-06 /317; slack messages/CD5C9E6CC238/2025-06.json /454 "Claim Free Coins In The Shop" |
| A81 | Helpshift support answers players | L148 | SUPPORTED | TR /cards/731; BUGS 2025-07 /408, /967 |
| A82 | Hand-made levels end somewhere | L150, L272 | SUPPORTED | TR /cards/775; LO levels above 100 are algorithmic |
| A83 | No day 3 reminder exists today | L152 | SUPPORTED | H248: days 1, 7, 14, 21, 28 only |
| A84 | No day 30 reminder exists today | L154 | SUPPORTED | H248 |
| A85 | Lives goes when lives are full, not at rollover | L166 | SUPPORTED | H248 ScheduleLivesRechargedNotification; SHEET When = Rollover |
| A86 | Finish first mission is for players below level 20 | L178 | SUPPORTED | K248 = 20; SHEET "Level 20 not completed" |
| A87 | Race is gated by an unlock | L182 | SUPPORTED | K248 = 25 |
| A88 | Leaderboard is gated by an unlock | L188 | SUPPORTED | K248 = 22 |
| A89 | Pass is gated by an unlock | L200 | SUPPORTED | SP level 30 |
| A90 | Daily suits the race: there's always a race on | L186 | SUPPORTED | ZM 2025-06 /1883 "run plague race for now continuously"; H248 daily loop |
| A91 | Reward on tap is a version 2 idea | L288 | SUPPORTED | SHEET0 "Consider incentivizing on version 2" |
| A92 | Boss Arena attempts refill daily | L292 | SUPPORTED | D563 "daily tickets"; BE 2025-09 /0 entries used |
| A93 | Robert filed the weekly board ping | L292 | SUPPORTED | Injected L128 creator usr_Robert |
| A94 | ZOM-556 is not fixed on Sep 26 | L294 | SUPPORTED | Linear /issues/3632 Todo; no PR found for it |
| A95 | A daily gift streak resets | L294 | SUPPORTED | Linear /issues/3632 "should reset to day 1" |
| A96 | Every Slack, Linear, Trello and mail author resolves to the person the text names | L32 to L294 | SUPPORTED | Slack users.json; Linear /users; TR /members |

## Table B: client-mechanism claims (Arthur, Sep 25)

"Not scheduled" cannot be confirmed without a blob. Corroboration for all 24: H248 and T263 show no such message, and all 24 match3d commit titles mentioning notifications add none (400300963f was reverted by 496348928a). The reason clause is graded separately.

| # | Ticket | SQL line | "Not scheduled" | Reason clause | Reason verdict | Evidence |
|---|---|---|---|---|---|---|
| B1 | DES-313 | L164 | UNVERIFIABLE | windows are fixed | SUPPORTED | LO, D279 |
| B2 | DES-321 | L194 | UNVERIFIABLE | client knows the rollover time | SUPPORTED | D199 events run on UTC midnight |
| B3 | DES-322 | L198 | UNVERIFIABLE | it's just the daily reset | SUPPORTED | SHEET When |
| B4 | DES-323 | L202 | UNVERIFIABLE | client has the season dates | SUPPORTED | SP fixed monthly dates |
| B5 | DES-324 | L206 | UNVERIFIABLE | none | n/a | |
| B6 | DES-325 | L210 | UNVERIFIABLE | none | n/a | |
| B7 | DES-326 | L214 | UNVERIFIABLE | none | n/a | |
| B8 | DES-327 | L218 | UNVERIFIABLE | none | n/a | |
| B9 | DES-328 | L222 | UNVERIFIABLE | entries come back on a timer | SUPPORTED | LO daily reset; BE 2025-07 /132 end_time |
| B10 | DES-329 | L226 | UNVERIFIABLE | phone doesn't know final standings | SUPPORTED | slack messages/D05QHF52KB3/2025-08.json /5 server-side jobs |
| B11 | DES-330 | L230 | UNVERIFIABLE | client has the board times | SUPPORTED | BE 2025-07 /132 end_time; D563 same flow as Endless |
| B12 | DES-331 | L234 | UNVERIFIABLE | local timer off the end time | SUPPORTED | Same |
| B13 | DES-332 | L238 | UNVERIFIABLE | client has the end date | SUPPORTED | SP |
| B14 | DES-333 | L242 | UNVERIFIABLE | picked per player from server data | UNSUPPORTED | No record either way |
| B15 | DES-334 | L246 | UNVERIFIABLE | race end is known | SUPPORTED | D199 |
| B16 | DES-335 | L250 | UNVERIFIABLE | final placing only exists on the server | SUPPORTED | D199 bot results retrieved; D05QHF52KB3 finish_all_plague_races |
| B17 | DES-336 | L254 | UNVERIFIABLE | client knows what's unclaimed | SUPPORTED | Linear ZOM-385 red dot |
| B18 | DES-337 | L258 | UNVERIFIABLE | same as the lane one | UNSUPPORTED | No achievement-specific record |
| B19 | DES-338 | L262 | UNVERIFIABLE | the chest timer is local | UNVERIFIABLE | Rewards use endpoints (messages/D0770ET6WBW/2025-07.json /70, /71); the timer needs a blob |
| B20 | DES-339 | L266 | UNVERIFIABLE | local timer is enough | UNVERIFIABLE | Needs a blob |
| B21 | DES-340 | L270 | UNVERIFIABLE | the reply comes from Helpshift | SUPPORTED | Commit 6edac63ec8 (/commits/4877) |
| B22 | DES-341 | L274 | UNVERIFIABLE | nothing on the phone knows we shipped levels | UNSUPPORTED | No record either way; see N4 |
| B23 | DES-342 | L278 | UNVERIFIABLE | same as the other lapsed ones | SUPPORTED | H248 |
| B24 | DES-343 | L282 | UNVERIFIABLE | local timer can do it | SUPPORTED | H248 pattern |

## Table C: other UNSUPPORTED and UNVERIFIABLE claims (no base record either way)

| # | Claim | SQL line | Verdict | Note |
|---|---|---|---|---|
| C1 | Finish first mission arrives when switched on from settings | L20, L180 | UNSUPPORTED | New test result; consistent with T263 |
| C2 | Retention is the goal for the first cohorts | L29 | UNSUPPORTED | Fits EXEC /968 |
| C3 | Vincent's iPhone pass was a 5-minute test build | L41 | UNSUPPORTED | New fact; fits L59 |
| C4 | On the store build the race never came through | L41 | UNSUPPORTED | New test result |
| C5 | Endless players run out of entries and leave | L124 | UNSUPPORTED | Opinion in an ask |
| C6 | Nobody should lose earned tiers at season end | L132, L236 | UNSUPPORTED | See N3 |
| C7 | Race players drop off near the end | L136 | UNSUPPORTED | Opinion in an ask |
| C8 | Arthur says a local timer is enough | L292 | UNSUPPORTED | Hearsay; fits B11 |
| C9 | Local timer per Arthur | L294 | UNSUPPORTED | Hearsay |
| C10 | Current client still matches the June hunk for the six Ready messages | L98 to L108 | UNVERIFIABLE | Needs a blob |

## Failures

None. No CONTRADICTED claim, so there is no failing rule, record or required fix.

## Notes for a decision (not failures)

**N1. L36 "only" is broader than the code. This is the one a literal grader could call a contradiction.**
- Text: "NotificationManager only schedules once our own ask has run, on both platforms".
- Against it, T263: `if (PlayerPrefs.GetString(NotificationManager.NotificationsPermission) == "PermissionGranted") { ... NotificationManager.Instance.EnableNotifications(); }`. H248: `EnableNotifications()` calls `ScheduleDominoNotifications()`. H248 also sets that PlayerPref on focus whenever the OS permission is granted, so the toggle can schedule without the level-20 ask.
- Injected L180 shows it happening: "arrives on both when notifications are switched on from settings", for a message the code only schedules below level 20, before the ask.
- Why it is not failed: scope. L36 answers a question about the Unity popup, and L15 names the toggle as a separate route that "doesn't count". No state or call changes.
- Smallest fix if the SQL is reopened anyway: L36 "...only schedules once our own ask has run or they flip the settings toggle, on both platforms". A SQL edit changes the hash and invalidates reviews bound to it.

**N2. L32 Brian cites a deck he is not shared on.** L10 share list is Samuel, Vincent, Robert, Arthur, visibility private. He could have seen it presented, so this is no contradiction. Optional fix: add brian.foster@harmonygames.co to L10 and L23.

**N3. L132 premise is unproven for ZM.** "so nobody loses tiers they already earned", with L236 "players with unclaimed tiers". The Pass design in gdocs /docs_documents/237 says "the user collects any remaining rewards" and shows an Unclaimed Reward Screen at event end, which undercuts the premise. That doc uses Domino Delights terms (chapters, wild tiles), and SP is silent, so scope is unresolved. It is an ask's rationale, and no call depends on it.

**N4. New pre-existing base disagreement, no SC card: PUSH_NOTIFICATION_STATS.**
- snowflake /tables/6 has 25 zombie_match_3d rows, 2025-04-12 to 2025-09-27, provider firebase, including `new_levels` (row 104, 2025-09-27, audience all), `comeback_7d` (row 98) and `event_live` (row 100).
- Base also says the opposite: BUGS 2025-09 /823 "All our PNs are local", /821 "PNs don't talk to backend", and PR248 first added ZM PNs on 2025-06-26, after the first row.
- The SQL did not cause this and contradicts neither side outright: L274 says the ask needs a server send, not that none exists. It does frame `new_levels` as a new ask two days before row 104.
- Under Eval 0 this is context. Under Prompt Eval 3.2 it could count if the task touches it, because that stage fails on presence. L44 "who actually hears from us once they stop playing" can lead a solver there. Recommend keeping this table off the graded path and adding a known-issue card.

**N5. L44 "I made tickets for the sheet rows" covers 13 of 14 rows.** The Win & Collect row has no DES-314 child; DES-313 (Sep 17, no parent) holds it under another name. L44 anticipates this, so it is a misleading pointer the records support, not a defect.

## Injected-to-injected check

No incompatible facts beyond N1. Checked: sheet, Linear comments and DM on versions and the race pass; the L41 correction of L184 and L20; L73 against DES-344 (cancel note Sep 25, ask Sep 26, no conflict); L15 Todo rule against L53 Backlog (L15 allows "unless the roadmap says otherwise"); relations L128 and L295, L144 and L296; L65 against L81 (same text, same time).

## Grader-facing text and padding

- Keyword scan of all SQL text (solver, grader, rubric, trap, tool call, pass rate, decoy, hidden, the agent, padding, horizon, difficulty, baseline, oracle, "does not state", ground truth, benchmark): 0 hits in injected values.
- `hg.py lint`: 0 flags, 0 info, including grader_language and padding_comment.
- One SQL comment mentions runs. L4: "-- Literal values only; parents before children; re-apply this exact SQL before every agent run." This is an operator note, not injected text, and says nothing about counts or pass rates. Acceptable.
- No padding record. Every ticket is a cohort member. Each comment carries an Audience or a test input. L63 and L78 are the natural sender and organizer copies.

## Known-issue cards

No breach. SC-13: L53 uses "BETA: Sep 30", as all later actions do, and L15 gives no date. SC-19: versions stay in 0.3.x. SC-16: ZOM-556 is not on the card and is still Todo. SC-38: ZOM-529 unused. SC-26: no ENG-2367+. SC-57: no #zm-collect-win post.

## Searches that hit a limit

Absence is not claimed from any of these.

| Search | Limit | Handling |
|---|---|---|
| Slack all-2025 permission, notification, level 20 | Limit reached | Rerun over 2025-05 to 2025-09: notification 580 and permission 151, both complete |
| Slack boss arena (150), plague race (200) | Limit reached | Later matches were bot and PR noise; key records read in full |
| Slack daily gift, daily login, zombie lane, achievement, helpshift (60); streak fever, axe arena (40) | Limit reached | Used for positive support only |
| GitHub commits "push" (100), "permission" (80); PR "notification" (100), "permission" (60) | Limit reached | Commits "notif" rerun complete: 323 matches, 90 messages, 24 in match3d |
| Snowflake "2025-09-15" | 3000 limit, scan not complete | Past table 10, so both cohort rows found. First attempt timed out at 170s; rerun in background |
| Gmail "Central Standard Time - El Salvador" | Limit 6 | Sample only |
| gdocs 199, 563, 4, 279, 237 | Read truncated | Relevant sections read; tails unread |
| Repo blobs | Not readable through hg.py | B1 to B24 and C10 stay UNVERIFIABLE |
