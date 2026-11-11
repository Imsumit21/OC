# Deep recheck P1 (second sample): Unique Ground Truth and Clarity

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Checked: 6 prompt sentences, 6 required outcomes, 31 decision-sweep candidates.

**Result: 6 open forks (DR1 to DR6).** One of them, DR4, meets the both-fair test. The Held set, Hold until, the Collect & Win window start and all 10 push send-or-hold calls each came out settled by RECORD. The open forks sit in one Still to do item, the cells of the held beat, Brian's moved date, a window-boundary figure, one "what is missing" cell, and the spend line in the deck.

## Findings

`DR# | pass | checklist section | quoted prompt sentence | record path, id and quoted value | Eval dimension | proposed score or severity`

DR1 | P1 | §2 which items are in the set | "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me." | linear ZOM-465 cmt_zom465_2 (Marcus, 2025-09-30 18:05Z): "The Collect & Win event icon animation is still to do on my side"; linear ZOM-565 cmt_zom565_2 (Brian, 16:12Z): "the same P1/P2 polish from my list. Endless runs fine without them, so they can follow and do not have to land before the beta"; #zm-animations C09ATAJ220H 09-12 11:41 (Brian): "*P1/P2 – Endless mode remaining VFX*" linked to ZOM-465 | Unique Ground Truth | 2 unless the main session accepts the closest quote below as a kill

DR2 | P1 | §2 what gets written | "If a beat ends up held, leave a note on its ticket so the owner picks it up." | brief: "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date."; Frederick's message: "which windows it runs in, if anything is held and until when"; Calendar columns "First window (UTC)", "Windows (UTC)", "Weeks running" | Unique Ground Truth / Clarity | 2 if any row grades those three cells on the held beat; no effect if none does

DR3 | P1 | §2 which number or date | "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me." | brief: "A committed date that misses the lock moves earlier and its owner is told in a reply on the mail where they committed to it."; Brian's Sep 22 mail: "The config handoff we agreed with Product is for Wed Oct 29"; Season Pass spec: "locked 24h before each season opens" | Unique Ground Truth | 2 if a row locks one date; passes if every instant before Oct 31 00:00 UTC is accepted

DR4 | P1 | §2 edge values | "the four buy weeks that start Monday the 6th" | brief: "Season Pass seasons open on the 1st at 00:00 UTC."; brief: "The calendar covers Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC"; match3d-backend config/runtime.exs: "Wednesday midnight (end of Tuesday)" | Unique Ground Truth | BOTH_FAIR_FIGURE; the rubric must accept either

DR5 | P1 | §2 what gets written | "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me." | Push Notifications Zombie Match, PNs Beta row 13: "Check the login calendar — fresh rewards are here!"; brief: "names the game as Zombie Match 3D and events by their ZM3D names"; brief: "the daily gift (the Login Calendar row on the push sheet)" | Unique Ground Truth | 3; the hold call is unchanged, only the "What is missing" text differs

DR6 | P1 | §2 which source wins | "send Frederick the recommendation he asked for" | ZM3D beta UA plan, el_5e83a1f4c092: "Small scale at first, scaled up week by week if the cohorts hold."; el_c07b2e9d3148: "Once the stores approve we start buying users at small scale and hold the spend there until the pivot call." | Unique Ground Truth | 2 if the recommendation is graded on the spend path; no effect otherwise

## Fork list

- F1 (DR1): Collect & Win Still to do | Reading A: lists the event icon animation, owner Marcus | Reading B: leaves it out as polish that can follow | Basis: SCOPE_GAP. The closest quote is the brief's "not polish nobody flagged", which excludes unflagged polish but does not say flagged polish is needed. Marcus said "still to do", not "needed before it runs", and only the owner speaks to this gap. His note sits on the ticket Brian's list labels P1/P2 and Brian released two hours earlier. Brian's release names Endless VFX, so it is a neighbouring scope. | Missing: a dated record from someone other than Marcus saying the C&W icon animation must land before the beta, or that it can follow.
- F2 (DR2): Weekly Leaderboard First window, Windows, Weeks running | Reading A: scheduled Monday 00:00 UTC windows are shown (Oct 6, 13, 20, 27), status Held | Reading B: none, because it runs in no window until the fix is confirmed | Basis: SILENCE. The brief covers only the hold end date. | Missing: a brief line saying what a held beat shows in its window cells.
- F3 (DR3): Brian's moved date, in the Season Pass Still to do cell and the mail reply | Reading A: states the lock itself, before Fri Oct 31 00:00 UTC | Reading B: names a date, Thu Oct 30, or back to Wed Oct 29, the date "we agreed with Product" | Basis: SILENCE. "moves earlier" gives no target. Thu Oct 30 is on no record, so this misses the both-fair test. | Missing: a sentence fixing the target, or a rubric accepting any instant before the lock.
- F4 (DR4): window boundary figures | Both fair: Season Pass first window Oct 1 00:00 UTC (real open) or Oct 6 00:00 UTC (clipped to the span); end instants Tue 23:59 or Wed 00:00 for Collect & Win, and the same pattern for season ends. BOTH_FAIR_FIGURE; the rubric must accept either. The reading that Nov 1 is the first window is killed by the #472 review comment: "the Season Pass premium strip is still set to the October range".
- F5 (DR5): Login Calendar push, What is missing | Reading A: Not Ready and WIP | Reading B: also the event name, because the copy says "login calendar" and Linear says "daily gift" | Basis: SILENCE on the player-facing name. The records use "daily gift", "Daily Login" and "Login Calendar". | Missing: a record stating the ZM3D name of this event.
- F6 (DR6): spend path in the recommendation's trade-offs | Reading A: small scale held until the pivot call | Reading B: scaled up week by week if cohorts hold | Basis: SILENCE. Same author and same date in one deck, and nothing ranks the two. | Missing: one line in the deck or in Frederick's message picking the path.

## Decision sweep: candidates checked and settled

| # | Cell | Reading A | Reading B | Quote that kills B | Label |
|---|---|---|---|---|---|
| 1 | Held: Weekly Leaderboard | Held | Not held: Douglas cmt_zom429_1 "so not blocking" and the brief's restart carve-out | Vincent, #zombie-match3d 09-30 20:50: "I killed the app and reopened it twice, played a few levels, and my week is still last week one. Same on the second device." | RECORD |
| 2 | Hold until | Until the fix is confirmed on prod | A date, such as the Oct 8 release | Brief: "say that instead of guessing a date" | RECORD |
| 3 | Hold owner and ticket | Douglas, ZOM-429 | Oliver (Sep 22 "Issue 1" revert) or Calvin (Aug 29 "let me check") | ZOM-429 assignee field: douglas; title "Leaderboard next session doesn't start without killing the app" | RECORD |
| 4 | Leagues as a separate beat | One beat with Weekly Leaderboard | Two rows, leagues not held | ZOM-544: "Weekly contest of leaderboard, the score, the league itself" | RECORD |
| 5 | Held: Endless (freeze) | Not held | Held on Leonard's 09-21 S23 report or Robert's 09-10 hard freeze | Leonard, thread reply 09-29: "Could not get it to freeze, so I am leaving this one."; Robert 09-24: "Once Leonard's friend restarted, his log just continued to the next level" | RECORD |
| 6 | Held: Endless weekly via ZOM-429 | Not held | Same fault reaches the Endless weekly reset | Brief: "an unverified one does not" | RECORD |
| 7 | Held: Plague Race, Endless refresh | Not held | Aug 25/29 refresh failures, Sep 7 "Killing the app doesn't solve the issue" | #live-incidents 08-29: "endless and plague race is working now"; #zombie-bugs 09-07 Douglas: "Solved, try again please" | RECORD |
| 8 | Held: quest rollover (ZOM-534 still open) | Not held, nothing to land | Open ticket means a gap | Leonard, the reporter: "That was my report, it is good on prod now." | RECORD |
| 9 | Held: quests (ZOM-557 counter) | Not held | The quest cannot complete | Brief: "Wrong counters, a reset that needs a restart" (ticket Done 09-30) | RECORD |
| 10 | Held: daily gift (ZOM-556) | Not held | Skip bug holds it | Vincent: "claiming works and nothing is lost" | RECORD |
| 11 | Daily gift Still to do (frame) | Nothing | Frame until stores approve | UA plan: "starting once the stores approve the Sep 30 builds"; #builds: iOS Submission #50, Android Submission #135 after #471 merged; PR #471 summary "updated Daily Gift sprite configuration" | RECORD |
| 12 | Held: Collect & Win | Late start, not held | Held on DEV | Brief: "A beat whose server windows are waiting on that release starts late, it is not held." | RECORD |
| 13 | C&W first window | Fri Oct 10 00:00 UTC, 10 windows | Wed Oct 8 window, joined after the release | Brief: "the first window that opens after its server windows are live on prod"; the Oct 8 release runs 15:00-16:00 UTC, so either instant gives Oct 10 | RECORD |
| 14 | C&W Still to do: vials | In, Claire | Out as cosmetic | Arthur on #468: "The final vial models are missing, Claire has those on her list." | RECORD |
| 15 | C&W Still to do: title and info text | Out | In (open PR #477) | Brian, ZOM-566: "the header title and the info screen text do not have to land before the beta" | RECORD |
| 16 | C&W Still to do: token travel | Out | In (ZOM-526 open) | Calvin: "Collect and Win tokens go through the queue manager now (#472)." | RECORD |
| 17 | C&W Still to do: reward tables | Out | In: Brian in #zm-collect-win 09-26: "Could you update them?" No reply. Julia is not a member of this public channel; visibility unverified. | Confluence Live-Ops Calendar: "Reward tables are re-imported from Google Sheets hourly in production"; runtime.exs job import_win_and_collect_rewards | RECORD |
| 18 | Still to do: lightSweep box | Out | In: Vincent 09-30 "we should squeeze in the fix" | Vincent, same thread: "so it rides the next build and nothing has to land for the beta" | RECORD |
| 19 | Endless Still to do: VFX, desert theme | Out | In | ZOM-565 Brian (quoted in DR1); Robert 09-30: "Endless runs with what it has now and nothing waits on new themes." | RECORD |
| 20 | Endless Still to do: remove force play | Out | In: Robert 09-17 "We are going to remove the force play", no confirmation found | Brief: "flagged since this brief" (Sep 24) | RECORD |
| 21 | Season Pass Held or Still to do: premium buy, untested end flow | Not held | Oliver 09-12 "We need to test the premium buy on a prod build" | Brief: "an unverified one does not" and "flagged since this brief" | RECORD |
| 22 | Season Pass: commits after the submission builds (93f45ebbfc, 0ff577550e) | Out | In: "Fix end popup" is not in the Sep 30 builds | Brief: "Nothing else goes in"; no person flagged it | RECORD |
| 23 | Season Pass lock | Oct 31 00:00 UTC; Brian's 10:00 Istanbul (07:00 UTC) misses by 7 hours | Spec's "freeze the day before" means any time Oct 31, so no miss | Spec: "locked 24h before each season opens"; brief: "read in server time (UTC)" | RECORD |
| 24 | Which mail gets the reply | Sep 26 mail | Sep 22 mail | Brian, Sep 26: "drop the Oct 29 one" and "reply on this mail" | RECORD |
| 25 | Halloween one-off | Off | On, per Robert's Sep 18 approval | Robert's DM 09-30: "pulling my ok. Take it off the beta calendar"; spec: "Owner: Robert (Product)." | RECORD |
| 26 | Endless in or out | In | Out as permanent, like Zombie Lane | Frederick's reason: "a permanent track with no window or reset to plan"; Confluence: "resets daily at 00:00 UTC and weekly on Monday 00:00 UTC" | RECORD |
| 27 | Change-request hold rule | No hold from it | CodeRabbit "Actionable comments" count as blockers | github reviews: 0 CHANGES_REQUESTED after #303 (2025-07-16); the C&W PRs show COMMENTED or APPROVED | RECORD |
| 28 | Push set | 10 rows of Push Notifications Zombie Match | The same-named tab in the Domino sheet | Sheet title; Frederick: "just those four" matches rows 3, 9, 11, 12 | RECORD |
| 29 | Push calls | Send rows 4 and 6; hold the other 8 | Rows 5, 7 sent (Ready and LIVE); rows 4, 6 held (no name) | Row copy "Puzzles vs Zombies"; Frederick: "Copy that does not name the game at all is fine to go out" | RECORD |
| 30 | Push segment | Sheet value | UK and US | Frederick: "plan the PNs Beta tab as it stands" | RECORD |
| 31 | Beat set: Trello "Oct 21" list, pop-up offers, Teams; quests content | Out | Added as beats, or more quests in Still to do | Brief: "an event window, a reset or a start push"; Leonard's Trello comment: "The weekly rollover does not wait on them" | RECORD |

## Channels and message counts

Window 2025-08-15 to the clock, SQL rows overlaid. Julia's membership comes from `channels.json`: 147 channels, 35 with messages in the window.

| Channel | Messages | How read |
|---|---|---|
| #zombie-bugs C08R27X0EAH | 1,178 | in full, by me |
| #zombie-match3d C0880U9751A | 582 | in full, by me |
| #zombie-ops C08R6BF4ENN | 28 | in full, by me |
| Frederick DM D05SD5QLG94 | 24 | in full, by me |
| #zombie-design C090N54TG79 | 963 | in full, by a delegated reader |
| Robert DM D05GU6L0XFH | 908 | in full, by a delegated reader |
| #zombie-art C08R8CHB0QL | 329 | in full, by a delegated reader |
| #zm-animations C09ATAJ220H | 223 | in full, by a delegated reader |
| 25 other files: Julia's DMs, group DMs, company-internal, live-incidents, analytics, zombie-sfx, zombie_marketing, playablex, random, zombie-social, game-design | about 1,600 lines | in full, by a delegated reader |
| #builds C05433XK267 | 1,558 | CI bot only; scripted scan from Sep 24 (309 messages), not read line by line |
| #engineering-bots C050WGU41HR | 36 | 6 human lines read; 30 bot rows not read |

Public channels Julia is not a member of (visibility unverified, Evals/ENVIRONMENT.md: "Unknown visibility remains unverified."):

| Channel | Messages | How read |
|---|---|---|
| #zm-collect-win C09EVVCFHKR | 102 | all lines |
| Collect&Win issues canvas C3DD99314033 | 81 | all lines |
| Season Pass Issues canvas CA2DFEA73CBC | 188 | from Sep 12 only |
| Bug Checklist canvas CF4EDAF93359 | 128 | from Sep 18 only |
| #live-ops-site-hook-up C09BQ2ZTJ2D | 58 | from Sep 10 only |
| #zombie-prs C093LEZGF6J | 911 | not read; it mirrors GitHub, which I read directly |

Also read: PNs Beta tab, Confluence Live-Ops Calendar, Season Pass Spec, GDD and Release Checklist (Live-Ops Event Engine in part), open ZOM tickets, all human PR review comments since Aug 1, the CDK schedules, Trello ZM ROADMAP. Julia's mail since Aug 15 holds no ZM3D content beyond the SQL rows (one Slack notification with an empty body).

## Limits

- Delegated readers' negative results are theirs. I reopened only the records quoted above.
- Slack canvases and file bodies have no readable content, so the issue lists exist only as the comment rows above.

## Passed to P2, no effect on any cell

- Trello list 6851a674975da1fe76e70d93 is named "BETA: Oct 10" in the base, while every action through Sep 30, including the SQL comment, says "BETA: Sep 30".

Platform defects: none
