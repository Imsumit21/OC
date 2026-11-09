# Independent red team
Reviewer: independent pass on 2026-11-04. Universe synth-cut, read through `hg.py` and `persona_view.py`, plus NotificationManager.cs only. Percentages use the 161 weight in design §12.

## Verdict
FAIL as written: 4 blocking findings. All four are seed and record fixes; the storyline survives. Separately, the 80 % bar is at risk (N2): most traps leak one hop past the four sources, and the one that does not leak (FILT) is unreachable.

## Blocking findings
**B1. FILT members cannot be found by any route (Prompt Eval §1.5 Ambiguity, §2.2 discovery).**
- Base `/comments` in linear/data.json is `[]`, and §11 seeds no Slack or mail companion. The catalog has no comment search: `linear_list_comments(issueId!)` only.
- ZOM-542 is "Update home screen and victory score screen for game modes"; ZOM-556 is "When the daily gift is skipped, it doesn't reset to 0." Neither is near the messages. T6 says searches miss them on purpose, and chain C6 has no record linking the hub to ZOM-542.
- The honest route is one comment read per ticket: 553 ZOM tickets, 3,687 in all. §1.5 requires each place be "findable from a record the persona can see".
- Effect: X11, X12, X13, V1 = 16 of 161 (9.9 %) fail in nearly every run for a reason a fair path cannot fix. Expect invalid all-fail rows, and an /oe path that cannot justify the hop.
- Caveat: `linear_show_data` and the `query` scope of `linear_list_issues` are unverified (`[U]`, Ask_Carriers.md). If either exposes comments this becomes a full leak instead.

**B2. "Can reach" is unsettled for Finish first mission, and the design reads it two ways (§2.1).**
- Reading B is supported by seeds and base: `cmt_f4960d3c073493b6bfc6` says it arrives on both once switched on from settings; ZOM-314 (Done) shipped the Notification On/Off button; `RequestNotificationPermission()` opens OS settings.
- The cited resolver `C0880U9751A/1759167600.326578` says only that nothing *asks* before level 20. It never mentions settings, so it does not rule out Go. §2.1: a leading reading alone does not resolve.
- Double standard: Lives recharged has Segmentation "Everyone", and Lapsed 1 and 7 cover all lapsers, so all include players below the ask. They pass because *some* players are reachable; Finish fails although *some* are reachable through settings. No sentence sets that line.
- The ask is also still at startup today: `C0880U9751A/1758216118.113509` (iOS), `C08R27X0EAH/1758291802.756889` (App Store 1.3.38). "Arthur is switching off" is future tense and no record says it landed.
- Flips Go 3 to 4: X5, X6, X6b, T1 = 20 of 161 (12.4 %). Needs a record stating that a player nobody asked does not count as reachable.

**B3. Lapsed 14 days contradicts the code (§3.2).**
- `BatchScheduleWeeklyNotifications(..., 4, serverToday)` runs `referenceDate.AddDays(i * 7)`, so the week-away message fires on days 7, 14, 21 and 28. X17's own reason says "a four-week batch".
- §11 has Arthur note "not in NotificationManager yet" on every unbuilt ticket, including DES-343, and the planned value is "not scheduled in the client". Both are false for day 14. The Call can stay Hold only through a different gap (not seen), so the planned value has no defensible support.

**B4. Two Drop values rest on no record (§2.1; T3 Drop 12, and Canceled vs Backlog).**
- Comeback gift: §10 says a Leonard comment "will state it", but Q has no wording and §11's per-ticket notes cover only Arthur and Vincent. The only support, the older PNs tab comment ("Consider incentivizing on version 2"), sits on a tab T11 rules out as Domino copy. Lapsed messaging is live, so without the comment Hold is the natural reading.
- Pop-up offer live: ZOM-225 (Done Jun 13) is a tiered pop-up offer system "in Zombie Match", and `C08R6BF4ENN` (Jul) places Pop-up Offers on the home icons. Trello's "Pop-up Offers via HE" on Oct 21 may be a different scope, and the rule says "live today". I could not confirm it shipped; `C090N54TG79` (Sep, "adding some pop-up offers") hints it did not. No planned note on DES-346 settles it.

## Non-blocking findings
**N1. Competency is the top remaining risk (check 4).** Defensible, not clearly wrong: retention pushes, headlines, a send plan. But the eval gives "tickets/PRs/release ops" to Engineering Ops, and the job is a release sign-off: rule tests are build, schedule and QA; five of seven plan columns are readiness; about 76 of 85 writes are Linear; Snowflake push stats are excluded; no audience, cadence or opt-in judgement exists. The skeleton is Douglas's ticket sign-off, assigned Engineering Ops (`douglas_beta_server_signoff_2026-10-28`, 00_Assigments.md line 13). A strict reviewer could fail it.

**N2. Trap liveness (check 3).** "Four sources" = hub, rule doc, sheet, every child ticket's comments.

| Trap | Settled by the four? | Leak |
|---|---|---|
| DONE | No | The hub's "Fires as built" column forces the source read, and `AddDays(i * 7)` beside "Weekly Rollover" settles it. The seeded mail `.../1836026670612966074` also sits in Samuel's inbox |
| CORR | No | DES-317's title hands over "week-away"; 0 base hits, so one search lands on the reply |
| DEP | Nearly | Rule says "can reach" and "Robert's call"; Vincent's "from settings" flags it; Robert's post is a root post |
| QA | No | "debug timer" from the QA note: 0 Slack hits Jun-Sep, so a search finds the reply. "(race reminder)" in the title does too. See N4 for a route with no reply |
| ALIAS | Nearly | Hub says "under whatever name"; DES-313 is the only post-May DES ticket outside the parent; a "Collect" search hits |
| FILT | No | No leak: unreachable (B1) |
| BUILT | Yes | See N3 |
| FOLLOW | No | The rule's clause points at the board; `trello_get_board_actions(filter=commentCard)` lists 14 comments, 12 of them old June-July notes |

Only DES-317 and DES-319 carry title parentheticals, a tell. My estimate, not a measurement: with B1 fixed by a pointer, mean landing is near 0.25, against 0.48 in the design. Design §6 gives P(<80) = 0.50 at 0.24, so the bar is a coin flip.

**N3. BUILT's wrong reading defeats itself.** Claiming a line differs from the client needs the client read, and that read shows it is right. A run that never opens GitHub answers No by default, so X15 passes free. X14 and X17 only test the same read as DONE, so one file decides 30 of 161. §6 names this correlation but still rates the two at 0.55 and 0.50.

**N4. Planned QA build numbers clash with base.** `C05433XK267` 2025-09 shows iOS 1593 and Android 1860 as `feature/season-pass` builds from Sep 12 on the Internal and plain Android jobs; store work runs on separate Submission jobs (Android 107-135, iOS 28-50). Under Vincent's own note, Android 1860 is not store-signed either, yet the reply says "Android is fine". It also gives a Hold route without the DM reply, so it weakens QA.

**N5. "A correct run cannot skip a ticket" is false.** The source shows six scheduled and Trello decides scope, so 32 unbuilt comment reads are skippable; only the client/server wording needs them. The §9 lean run falls from 148 to 116, under 130. Real runs will likely read them, but the claim fails.

**N6. Filler (check 5).** The 24 parent asks look generated: 7 of the 8 Drops map one-to-one onto Backlog and Oct 21 cards, and 16 Holds repeat one fact. No one files "PN ask: Lava Event start" for a Backlog event, so a reviewer can read this as cohort padding to reach 40. gcal (a ○ support for BUILT) and gslides (one sentence) exist mostly for service count. §9's 24 Slack and 10 Trello per-feature calls find nothing on about 38 of 40 rows. Comment plus state plus sheet records the same call three times, though the hub asks for it.

**N7. "Name the one thing missing" has no order.** All 22 unbuilt Holds fail both "schedules" and "seen". "Needs a server send" is not a rule test, yet K9 requires the word "server". Finish first mission also has a second gap: `serverToday.AddHours(12)` is noon today, so late leavers get nothing (`fireTime <= DateTime.Now` returns).

**N8. Emoji fork settled only by the grader.** Sheet and client swap emoji on rows 6 and 14 (🎯 vs 🧟‍♀️📈). The string clause is not limited to Go rows, so a strict reader files two more tickets. §10 answers by not grading emoji, which is not a record.

**N9. "Live today" has no single authority.** Confluence has 0 hits for Daily Login, Trophy Path, daily chest and free coin, so those rest on Linear Done plus QA chat, the evidence the §1a audit (SC-16) calls no proof of shipping. They converge on Hold in practice.

**N10. Housekeeping.** §1a omits Robert's `C0880U9751A/1758215775.137159` (Sep 18, "punt this even further down the road"), which the seeded "stays after level 20" quietly reverses. The `Trello comments []` sweep line is wrong: the board has 12 base comments, harmless. §11 gives 37 tickets by several authors one timestamp, and the hub's "I made a ticket per message" conflicts with teammates filing asks. §6 prints 42 slots and 164 weight, stale against §12's 41 and 161.

## Checks that held
Rule sweep (check 1), every sentence applied:

| Message | Result |
|---|---|
| Lives recharged, Lapsed 1 day, Lapsed 7 days | Go holds, subject to the B2 reach line; headlines match the client exactly |
| Plague Race | Hold holds; timing settled by Leonard's ticket comment |
| Weekly Leaderboard reset | Hold holds, one gap |
| Finish first mission | Fork, B2 |
| Win & Collect, Season Pass start, Boss Arena open | Hold holds: BETA list |
| Quests, Login Calendar, Zombie Lane, Trophy Path, Daily chest, Free shop coins, Lapsed 3 days | Hold holds (see N9) |
| Hourly Coins, Axe Arena, Streak Fever, Nathan's Treasure Hunt, Rewarded ad, Lava, PvP, Wild card, Team battle, Bones | Drop holds: not live, not on BETA |
| Comeback gift, Pop-up offer live; Lapsed 14 days | Forks, B4; B3 |

Base coherence (check 2):
- Weekly Leaderboard: code matches the claim. rc_18 at 20:58Z precedes Arthur's approval (21:23:25Z) and the merge (21:23:32Z); ids end at rc_17, and no review row is needed. `page_liveops_calendar` lists Weekly Leaderboards Live on ZM. No record names the reset day, and none is needed.
- Plague Race: Live on the page. Leonard's "always on" fits the "1-day timer" (`C08R27X0EAH`, 2025-07) and the code's daily 00:15 for five days. `C0880U9751A` (2025-06) on 30-minute dev timers grounds the debug timer.
- Level 20: rc_4 gives `FirstTutorialFinished = 20`; PR #292 and `D06KPMDV2JZ/1752162738.497679` agree. Later-dated Robert beats the older points; only reach is open (B2).
- Features exist as described: Quests, Daily Login (ZOM-299, identical to DD), Zombie Lane, Trophy Path, daily chest, shop daily free coin (ZOM-539), Boss Arena ("Infinite HP Boss Mode" on BETA, "Infinite boss arena (#424)" in builds).
- ALIAS base fact confirmed: the page maps Collect & Win to Win & Collect, and the BETA list carries it.
- Seed authors are members of their channels. DES uses Backlog, Canceled, Todo, In Review and Done.

Not confirmed: `linear_show_data`, `linear_list_issues` query scope, whether pop-up offers shipped, and per-variant `LevelVariantManager` values (file not read, by the rules).

## Delta review
Scope: re-read `build_scenario.py` and design §13 only; universe through `hg.py`. Weights use 183, summed from the builder's slots. §11 and Ask_Carriers §6b were not re-read, so two points below are marked unverified.

**1. First-pass blocking findings: all four closed.**
- B1 closed. T6 and C6 add relates-to links from DES-330 to ZOM-542 and DES-338 to ZOM-556, so a fair route exists. `relations` is a real base field (ZOM-225: target ZOM-222, type relates). Unverified: that `linear_list_issues` output shows it. §13 cites Ask_Carriers §6b; prove it in the pre-check, because B1 reopens if it does not.
- B2 closed. Test 5 says "A player only counts once the permission ask has happened, the settings toggle doesn't count", and Q["ask_decision"] says "Nothing asks before that in the beta build". That removes the toggle reading, the startup strand and the double standard: Lives and lapsed rows have players who count, Finish has none.
- B3 closed. Lapsed 14 days (now DES-344) is Drop, naming Lapsed 7 days, through the rule clause and Q["ladder_review"]. C7 says Arthur leaves no note, and it matches `AddDays(i * 7)`.
- B4 closed. Q["gift_note"] settles Comeback gift at test 1; Pop-up offer live is gone from M. Loose end: gift_note appears only at builder lines 210 and 244, with no trap, chain or fragment, and Q names no author (§13 says Leonard).

**2. New rule applied to the twelve messages.**

| Message | Result |
|---|---|
| Lives recharged, Lapsed 1 day | Go, one answer. Players past the ask count; next-day firing passes test 4 |
| Lapsed 7 days | Go, one answer; day 7 is right, string ticket follows |
| Lapsed 14 days | Drop, one answer. A reader who fails it at test 3 still lands here, because Hold is "anything else" |
| Lapsed 30 days, Lapsed 3 days | Hold at test 3, one answer. The batch stops at day 28 and has no day 3 |
| Weekly Leaderboard reset | Hold, stops at test 4, one answer |
| Quests rollover | Hold at test 3 if Arthur's note says local; the sheet's Type says Push. Not in Q, no graded slot |
| Comeback gift | Drop at test 1, one answer |
| Rewarded ad ready | Drop at test 1, one answer: Oct 21 list, `D04UP2L3E3S` "I moved out rewarded ads and axe arena", no live evidence |
| Plague Race | Hold, but the stop point is at risk: N11 |
| Finish first mission | Hold, but the stop point can differ: N12 |

The "already covers it" clause catches nothing else in the 35, and the emoji sentence closes N8.
- N11 Non-blocking. Plague Race reaches test 6 only if test 4 passes (sheet "Event Start", code daily at 00:15). That rests on Leonard's "daily is fine" comment, which has 0 hits in the builder and no mention in §13. If §11 lost it, runs stop at test 4 and X8, X8b, X8c mislabel. Unverified; put it in Q.
- N12 Non-blocking. "Stop at the first failure" makes N7's gap decisive. `serverToday.AddHours(12)` is noon today, so a first session after noon schedules nothing (`fireTime <= DateTime.Now`). A reader can stop at test 4; X6 and X6b (10 of 183) require ask or reach wording. "The hour doesn't matter" favours test 5 but does not cover never firing.
- N13 Non-blocking. K4's quote "I made a ticket per message under" is no longer in Q["hub"], so the delegation check fails at injection. Every other quote matches.
- N14 Non-blocking. X1c, X6c and X8c all require Backlog, so missing the freeze comment now costs 30 of 183 (16.4 %), the largest single choke in the design. Their titles say "leaves Done", which Todo also satisfies.
- N15 Non-blocking. Cohort 42 is 35 messages plus 7 decoys, so the gate's 40 is met only by counting records the rule rules out.

**3. The note.**
- **B5 Blocking: "five messages over 28 days" is not one defensible value.** By `ScheduleDominoNotifications`, five fits only a player past the ask, with full lives, below the leaderboard unlock. Short lives adds 1. The leaderboard unlock adds 4 (about level 22, `C08R27X0EAH` 2025-07; constant not read). The race adds 5 at level 25 (ZOM-413). So a level 25+ player gets 14 or 15, and a player below level 20 gets 0 because `NotificationsEnabled` stays false.
- Hub says "actually hears", and a Hold call removes no code, so the leaderboard and race messages still fire. Even counting Go rows only gives 5 or 6, since Lives recharged is a Go. An exact "up to 15" fails X20's regex, and no record states any value, so it is not a both-fair figure. The population needs sharpening: name the lapsed reminders in the hub, or grade the days 1, 7, 14, 21, 28 ladder instead of a count.
- The D1 and D7 baseline holds. `USER_COHORT_RETENTION` has exactly two rows for 2025-09-15, a Monday, both zombie_match_3d, so the unnamed game is not a fork: Android 103 installs, D1 37.86, D7 10.68; iOS 237, D1 31.65, D7 9.28. D7 is closed. I found no second retention table but did not confirm the full table list. N16 Non-blocking: K16 and K17 are titled D1 and D7 but their regexes check D1 only.

**4. Competency: defensible, up from at risk, still not clearly Marketing and GTM.** The D1 and D7 framing, Audience column, warehouse baseline, team note and asker emails move it toward retention comms. But 66 of 84 writes are Linear, and the note carries only 16 of 183. The most useful change: make the note's graded core the reach gap, stating who hears nothing (below the ask) and who hears what, at weight 5 or more. That is a retention finding, and it also closes B5.

**Verdict: FAIL, narrowly. B1 to B4 are closed; 1 blocking finding is open (B5).**
