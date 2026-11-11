# R_B Spine Facts — ZM3D live-ops calendar (synth-cut, clock 2025-10-01 00:00 PT)

Universe: synth-cut · Clock 2025-10-01 00:00 PT (07:00Z) · Seed bound 2025-10-01T00:00:00Z
Persona: Julia Lawson (Slack EMPLOYEE_0005_SLACK_ID)
In-scope beats: Plague Race, Collect & Win (= Win & Collect), Season Pass, Endless Monster Mode (daily+weekly), weekly leagues/leaderboard, Zombie Lane / Trophy Path, quests rollover, daily login/daily gift calendar.
Out of scope: Boss Arena / Infinite Boss, Axe Arena.

## 1. Live-ops fault threads, Sep 15 00:00Z – Sep 30 23:59Z

Scope note: window = 1757894400 – 1759276799 (Sep 15 00:00Z – Sep 30 23:59:59Z). Channels scanned: #zombie-bugs (C08R27X0EAH), #zombie-match3d (C0880U9751A), #zombie-design (C090N54TG79), #zombie-ops (C08R6BF4ENN), #zombie-art (C08R8CHB0QL), #company-internal (C05KNDCHAAG), #builds (C05433XK267). #builds was scanned and excluded from the table: all 1,000+ messages in the window are Jenkins bot posts (`subtype=bot_message`, `reply_count=0`, empty `text`, content in `attachments[].fields[].value`); it produces no fault threads, but its job-name suffixes (`/winAndCollect`, `/auth`, tag-range commit lists) are used in §5. #zombie-ops has exactly 1 message in the window (Sep 15 04:32, "To test SP: Android: 1869 iOS: 1602", no replies) and no fault threads.

24 roots matched (fault/behaviour of an in-scope beat). "KW in last" = does the deciding last reply contain any of plague|collect|win|season pass|pass|endless|leaderboard|league|quest|daily|login|zombie lane|trophy.

| # | channel | root ts (UTC) | author | beat | rc | first line of root | LAST reply (ts · author · text ≤160) | KW in last | resolution at end | ZOM id |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | #zombie-bugs | 2025-09-15 12:31 · 1757939514.864549 | Vincent Parker | multi: season pass + quests + leaderboards + endless | 11 | "Hey guys, here is the list of issues that will be part of submission today." | 2025-09-15 14:51 · Martin Walsh · "<@…0032> <@…0012> Needs to be like this: image.png image.png" | no | unclear — 10 issue replies, final one is a boss-arena sprite alignment note | none |
| 2 | #zombie-bugs | 2025-09-16 04:51 · 1757998292.212529 | Leonard Hayes | quests | 0 | "Playing submission candidate. Quest animation is annoying indeed <@…0006> -when done think a fix is landing? It feels sluggish" | — (no replies) | — | open question, never answered in-thread | none |
| 3 | #zombie-bugs | 2025-09-16 05:02 · 1757998921.355209 | Leonard Hayes | endless | 0 | "Endless mode stuttered really badly for me as soon as I opened it <@…0016>" | — | — | no reply in this root (parallel root #5 continues it) | none |
| 4 | #zombie-bugs | 2025-09-16 05:12 · 1757999557.589779 | Leonard Hayes | quests | 3 | "Quest animation is also a blocker. It really degraded the experience" | 2025-09-16 06:36 · Calvin Price · "I sent a PR, is not merged yet" | no | PR sent, merge state never confirmed here | none |
| 5 | #zombie-bugs | 2025-09-16 05:22 · 1758000132.434419 | Leonard Hayes | season pass | 0 | "Carnage streak freeze has no timer on the pre-level dialogue. Remove it from season pass or fix pre-level dialogue and add a countdown timer" | — | — | never answered | none |
| 6 | #zombie-bugs | 2025-09-16 05:19 · 1757999990.759409 | Leonard Hayes | season pass (+ trophy path reference) | 1 | "There is no claim sfx for season pass. It sho dil be the same as the trophy road one" | 2025-09-16 05:58 · Oliver Brooks · "will add first thing in the morning" | no | promised, never confirmed fixed | none |
| 7 | #zombie-bugs | 2025-09-16 05:44 · 1758001464.936119 | Leonard Hayes | season pass | 0 | "Season pass is looking pretty good. Animations on the main screen are a bit slow especially season pass chainsaw really takes it time to fly into its icon" | — | — | not a break, still open as polish | none |
| 8 | #zombie-bugs | 2025-09-16 14:13 · 1758031982.956109 | Vincent Parker | season pass + zombie lane + quests + endless | 6 | "Remaining Issues Based on latest builds" | 2025-09-16 14:27 · Vincent Parker · "• Boss arena reward screen shows x2 label which should be removed…" | no | 6 sub-bugs posted, no fix confirmation at all | none |
| 9 | #zombie-bugs | 2025-09-17 17:28 · 1758130096.275899 | Leonard Hayes | daily login | 4 | "I noticed a potential bug that's beneficial to players - daily login doesn' rest if you miss a day - is that intentional?" | 2025-09-17 18:03 · Brian Foster · "Yes it's a bug <@…0012>. The progress bar doesn't reset, but the daily rewards should reset" | **yes** (daily) | confirmed bug, no fix in thread | none |
| 10 | #zombie-bugs | 2025-09-17 21:45 · 1758145553.265559 | Leonard Hayes | endless | 8 | "I let endless level to run for 5 mins+ and my phone is burning right now…" | 2025-09-17 23:36 · Robert · "If top is disabled.. why.." | no | still broken / unexplained | none |
| 11 | #zombie-bugs | 2025-09-21 02:08 · 1758420497.482989 | Leonard Hayes | endless | 0 | "Bug endless mode. Tried to use <item> the screen froze. Samsung galaxy s23 ultra - production build" | — | — | no reply at all | none |
| 12 | #zombie-bugs | 2025-09-22 13:00 · 1758546048.524829 | Vincent Parker | weekly leaderboard | 0 | "After fixes for the crashlytics issues, I cannot participate in leaderboard. Killing the app doesn't help." | — | — | continues in root #13 | none (has Firebase crashlytics link + 1 file) |
| 13 | #zombie-bugs | 2025-09-22 13:01 · 1758546119.789009 | Oliver Brooks | weekly leaderboard | 4 | "on it now" | 2025-09-22 14:19 · Vincent Parker · "yep, it's working fine right now" | no | **fixed** (revert, verified) | none |
| 14 | #zombie-bugs | 2025-09-22 22:40 · 1758580854.440599 | Robert | quests | 0 | "Match boss buster items needs to be removed from quest" | — | — | no reply | none |
| 15 | #zombie-bugs | 2025-09-26 16:20 · 1758903616.346579 | Vincent Parker | zombie lane | 6 | "After I skipped the zombie lane tutorial, ı got the exception and skipping couldn't claim the ice cream." | 2025-09-26 20:04 · Vincent Parker · "Can you trigger an ios build" | no | fix sent + Android build 1977 tested OK; iOS build unverified at thread end | none |
| 16 | #zombie-bugs | 2025-09-26 16:49 · 1758905363.341129 | Arthur Blake | season pass (addressables/memory) + endless load time | 25 | "The iOS memory seems like a guess. Will LiveOps to addressables do the trick you think?" | 2025-09-26 20:45 · Oliver Brooks · "maybe it'll do the spell we need" | no | open — plan agreed, no result | none |
| 17 | #zombie-bugs | 2025-09-30 16:24 · 1759249488.495439 | Vincent Parker | season-pass gold parts / lightsweep shader (beat inferred, not stated) | 4 | "i think we should squeeze in the fix for that issue if it's an easy fix. annoying and players can see that for 10 times in a day…" | 2025-09-30 17:42 · Vincent Parker · "<@…0004> ı think [PERSON_NAME_0022] will handle the problem. It might be about the shader" | no | open — owner named, no fix | none |
| 18 | #zombie-match3d | 2025-09-16 22:39 · 1758062348.988239 | Robert | endless (analytics instrumentation) | 14 | "<@…0038> Did you implement the endless instrumentation? … I also didn't see a sheet for it." | 2025-09-16 23:43 · Leonard Hayes · "I remember I intended to do different things with different tables - let me check and get back to you" | no | open — never answered with a result | none (spun off ZOM-549 in the arena thread, see §1b) |
| 19 | #zombie-match3d | 2025-09-17 17:39 · 1758130794.208109 | EMPLOYEE_0032 (Blake) | endless (perf/heating) | 12 | "please test #1643 ios. it has disabled zombies visuals. please focus on performance on some heavy modes, and heating ofc" | 2025-09-17 19:58 · Vincent Parker · "As a new note, after killing the app the temperature returned to normal pretty quickly compared to prior" | no | still hot in endless — unresolved | none |
| 20 | #zombie-design | 2025-09-17 04:07 · 1758082051.562129 | Leonard Hayes | endless | 3 | "she hated the endless mode and thought it was super stressful - she didn't even complain her first attempt, tried to quit, couldn't find how to do it…" | 2025-09-17 04:26 · Leonard Hayes · "let's do this by the next relesae" | no | deferred to next release | none |
| 21 | #zombie-design | 2025-09-19 14:28 · 1758292083.627299 | Brian Foster | Collect & Win | 0 | "We tested Collect & Win with <@…0012> using the latest commit build… we don't think it will reach a shippable level by the end of today" | — | — | **not shippable** at Sep 19; no follow-up in-thread | none |
| 22 | #zombie-design | 2025-09-22 23:23 · 1758583438.427779 | Robert | plague race / trophy path / endless (playtest notes) | 0 | "• Hard crash x1 • Phone heat up had to stop playing x1 • Audio glitch x1…" | — | — | field notes; "No confusion with how the modes worked (Plague race, trophy path, endless)" | none |
| 23 | #zombie-design | 2025-09-29 19:16 · 1759173389.051889 | Vincent Parker | plague race + quests | 0 | "The only casual live ops implemented is plague race. Quests can be more all around." | — | — | positional statement, not a fault | none |
| 24 | #zombie-design | 2025-09-29 20:16 · 1759176983.189479 | Robert | leaderboards/quests + plague race (status ledger) | 1 | "I think we should think about what 0.3.22 had and what we're keeping." | 2025-09-29 20:39 · Leonard Hayes · "That's a pretty good summary and pov. I agree with you" | no | agreement, no action | none |

§1b — cross-reference: the only ZOM ids minted inside the window come from root #18's sibling thread and from boss-arena/core-bug threads (all outside the in-scope beat set): ZOM-546 refill algorithm (Sep 15 18:39, in #zombie-match3d 1757961539), ZOM-547 boss-arena balance, ZOM-548 boss-arena events, ZOM-549 left_level/endless_left analytics (Sep 17 02:32, reply in 1758063146), ZOM-553 boss-arena refill/nuke, ZOM-530 effects panels (#zombie-design 1757951755), ZOM-487, ZOM-434, ZOM-435, ZOM-383 status-change posts, ZOM-498/536 in a #builds job name (1759161699, branch `Samuel/ZOM-498-536`).

### §1 counts

- Roots matching the beat-fault screen in the window: **24**.
- Roots **with at least one reply**: **14** (#1 11, #4 3, #6 1, #8 6, #9 4, #10 8, #13 4, #15 6, #16 25, #17 4, #18 14, #19 12, #20 3, #24 1); **10** have rc=0.
- Threads whose **deciding last reply carries no beat keyword** (search-unsweepable from the tail): **13 of 14** — only #9 (daily login) ends on a keyword. Counted strictly: 13.
- Threads containing **no Linear (ZOM-nnn) id in root or any reply**: **24 of 24** (100%). Zero in-scope beat thread in this window is linked to Linear from Slack.
- Threads whose **root itself carries no beat keyword** (only discoverable by reading past the root): #13 ("on it now"), #17 (no beat word), #18 root does say "endless", #19 root says "heavy modes" only. Root-level count: **2** (#13, #19) plus #17 ambiguous.

## 2. Fault root messages with replies, Sep 1 – Sep 14

Window = 1756684800 – 1757894399. Same channels; 21 roots matched a beat, 13 had replies. Fault/behaviour rows only:

| channel | root ts (UTC) | beat | rc | resolution at end |
|---|---|---|---|---|
| #zombie-match3d | 2025-09-03 22:07 · 1756937239.183879 | endless (level rotation config) | 17 | resolved by design: "they need to pass month day then instead of 1-3" |
| #zombie-bugs | 2025-09-03 22:07 · 1756937250.627979 | endless (sound bugs) | 1 | ticketed → **ZOM-515** "Fix sound bugs in endless mode" (created in-thread) |
| #zombie-bugs | 2025-09-03 22:09 · 1756937350.361639 | endless (refill 39 vs 40) | 3 | diagnosed "-1 per refill, so 39, 38, 37, 36…" — no fix confirmed |
| #zombie-bugs | 2025-09-03 22:21 · 1756938116.988359 | endless (enrage loss on refill) | 1 | ticketed → **ZOM-517** high priority |
| #zombie-bugs | 2025-09-07 00:07 · 1757203643.996789 | endless (prod freeze, "killing app doesn't solve") | 10 | unclear; thread drifts to difficulty tuning ("a bit too easy") |
| #zombie-bugs | 2025-09-07 18:25 · 1757269507.661569 | zombie lane + item locks | 9 | root cause "prod servers read the old reward sheet" — no fix confirmed |
| #zombie-bugs | 2025-09-08 00:03 · 1757289825.998289 | quests (points don't reset until restart) | 1 | ticketed → **ZOM-534** urgent |
| #zombie-bugs | 2025-09-10 01:21 · 1757467270.178829 | endless (hard freeze 3rd clear) | 4 | ping only, no fix |
| #zombie-bugs | 2025-09-10 03:09 · 1757473760.256049 | trophy path (item granted from path) | 12 | mitigation: "I will remove it from the reward sheet until it's resolved" |
| #zombie-design | 2025-09-10 04:35 · 1757478958.104989 | plague race (payout too generous) | 2 | **fixed by decision**: cut in half, "sounds good" |
| #zombie-bugs | 2025-09-11 04:43 · 1757565808.329509 | endless (quit via settings keeps ticket) | 5 | **won't fix**: "Let's keep it as is" |
| #zombie-ops | 2025-09-12 03:13 · 1757646802.623469 | season pass (premium buy test builds) | 4 | test build requested, "generating a new build now" |
| #zombie-design | 2025-09-09 19:55 · 1757447742.666159 | season pass + Collect&Win (QA status) | 2 | "still waiting for a Collect&Win test"; "some bugs get fixed in one build while breaking in another" |

Section-2 note: unlike Sep 15–30, the **early-Sep threads do carry Linear ids** — ZOM-515, ZOM-517, ZOM-534 are minted inside the thread by the Linear bot (`SLACK_BOT_0007`/None user, message text "[PERSON_NAME_0055] created a … issue ZOM-nnn …"). So the "Slack thread ⇒ Linear id" trail exists for early September and stops around Sep 15.

## 3. The 12 open Linear issues

Source: `spine_open_issues_nonba.json` (12) joined to `linear.json` issues + users. Note: `linear.json.comments` is empty (0 rows), so issue history must come from Slack/GitHub, not Linear comments.

| id | state | assignee (name from linear users) | created | updated | description first 200 chars |
|---|---|---|---|---|---|
| ZOM-344 | Todo | Marcus Bennett (marcus.bennett@harmonygames.co) | 2025-07-03T12:28:16Z | 2025-07-03T12:28:16Z (never touched) | "![image.png](…) We need this boxes in UI to have a little animation closed and opened. WE can use the existing animations that we use for endless mode chest and the progress bar." [labels VFX, Improvement, Hot Fix - Global Launch] |
| ZOM-429 | Backlog | Douglas (douglas@harmonygames.co) | 2025-07-22T15:14:49Z | 2025-09-22T14:51:23Z | "When the weekly leaderboard is ended, it doesn't start the new one or let me claim my rewards. It can only proceed to next leaderboard if the app is killed and when I can claim my rewards if any" [Bug] |
| ZOM-432 | Todo | Calvin Price | 2025-07-23T09:48:01Z | 2025-07-23T09:48:01Z (never touched) | "![image.png](…)" — body is one screenshot, nothing else [Improvement] |
| ZOM-465 | In Progress | Marcus Bennett | 2025-08-11T14:48:37Z | 2025-09-23T14:16:25Z | "* ~~Multiplier VFX at the end of level~~ You have already done the animation Marcus… ## Event Animations * ~~Idle Icon Animation~~ For all event…" [VFX] |
| ZOM-471 | Todo | Samuel Turner | 2025-08-13T18:01:16Z | 2025-08-13T18:01:16Z (never touched) | "'@…0054 said: > @Samuel When player not In a Plague Race, the Icon should have red dot on it." [Improvement, Hot Fix - Global Launch] |
| ZOM-504 | Backlog | EMPLOYEE_0032 (Blake; Linear name unresolved) | 2025-08-25T12:54:47Z | 2025-09-15T15:10:41Z | "Sometimes, objects in endless mode can stay visually after thrown. I couldn't notice anything particularly but it happens in every attempt. [endless-mode-train.mp4]" [Bug] |
| ZOM-517 | Backlog | EMPLOYEE_0032 (Blake) | 2025-09-03T22:22:22Z | 2025-09-03T22:22:22Z (never touched) | "'@…0054 said: > @…0120 Monster will lose enrage in endless mode if they are already enraged and walking on the board and an item refill happens" [Bug] |
| ZOM-534 | In Progress | Douglas | 2025-09-08T00:34:41Z | 2025-09-15T15:10:32Z | "'@Leonard said: > My quest points didn't reset after I completed the day while still being online. They only got reset after I kill the app and restarted it @douglas @…0022 - this is…" [Bug] |
| ZOM-552 | In Progress | Oliver Brooks | 2025-09-17T19:54:58Z | 2025-09-18T18:50:36Z | "We need to add these event logs from the sheets to track users' data in the Season Pass / Season_pass_left: (link) Season_pass_redeem: (link)" [Analytics] |
| ZOM-556 | Todo | Calvin Price | 2025-09-22T14:44:06Z | 2025-09-22T14:44:06Z (never touched) | "![image.png](…) If I didn't log in for a day, the bottom part should reset to day 1. However, it doesn't reset right now." [Bug] |
| ZOM-565 | Todo | Calvin Price | 2025-09-25T13:46:04Z | 2025-09-25T13:46:04Z (never touched) | "So i had to add some vfx to the starting screen of the Endless Horde. First of all the bar as you can see its an image it's not an actual bar that can help me at all…" [VFX, VFX Integration] |
| ZOM-566 | Todo | Owen Baker | 2025-09-30T16:26:02Z | 2025-09-30T16:26:02Z (never touched) | "Analytic logs for collect&win * (link) * (link)" [no labels] |

### 3b. Slack mentions of each id or exact title (cached channel-months Jul/Aug/Sep; 43 files = 22 channels — note `zombie-prs` C093LEZGF6J, `zombie-social` C097K9BHE31, `zombie-sfx` C09A7PDFYCV are **not** in the cached set except zombie-prs Sep which I pulled, and it contains no ZOM-344…566 text)

| id | Slack hit? | where (channel · ts · author) |
|---|---|---|
| ZOM-344 | **none** | — |
| ZOM-429 | **none** | — (but #zombie-bugs 1758546048 / 1758546119 Sep 22 is clearly this bug in prose, with no id) |
| ZOM-432 | **none** | — |
| ZOM-465 | **none** | — |
| ZOM-471 | yes | #zombie-match3d · 1755108077.288629 (2025-08-13 15:21Z) · Linear bot post "created a high priority issue ZOM-471 …" inside thread root 1755108052.016359 (12 replies) |
| ZOM-504 | **none** | — |
| ZOM-517 | yes | #zombie-bugs · 1756938142.754179 (2025-09-03 22:22Z) · Linear bot, rc=0, inside thread 1756938116.988359 |
| ZOM-534 | yes | #zombie-bugs · 1757291682.062479 (2025-09-08 00:34Z) · Linear bot, rc=0, inside thread 1757289825.998289 |
| ZOM-552 | **none** | — |
| ZOM-556 | **none** | — |
| ZOM-565 | **none** | — |
| ZOM-566 | **none** | — |

### 3c. Linear-bot post in #zombie-match3d (C0880U9751A) containing the title, and whether it has replies

| id | bot post in #zombie-match3d? | replies |
|---|---|---|
| ZOM-471 | **yes** — 2025-08-13 15:21Z, ts 1755108077.288629, attachment/field text "[PERSON_NAME_0055] created a high priority issue ZOM-471 Add red dot icon for players not in Plague Race" | post itself rc=0, but it sits in the 12-reply thread under Samuel's 1755108052.016359, where the team **kills the idea**: "i think it's annoying, it already has start button" (1755109202), "yeah, we don't need it! cancel the ticket lol" (1755109968), "I don't think we should do it" (1755116903) — yet Linear still shows **Todo** |
| all other 11 | **no** | — |

So: **1 of 12** open issues has a Linear-bot post in #zombie-match3d, and that one is the one the team decided to cancel; **0 of 12** have Linear comments (linear.json.comments empty); **3 of 12** are nameable from any cached Slack message at all.

## 4. The 22 merged live-ops PRs

Source: `spine_merged_liveops_prs_nonba.json` + `github.json` (pull_requests / reviews / review_comments / pull_request_comments / users). CodeRabbit = `PERSON_6026_GITHUB_USERNAME` (display "PERSON_6026_NAME"). Author names via github users + Slack-name join on `EMPLOYEE_nnnn_GITHUB_USERNAME`.

| pr | title | author | merged_at | reviewers (name · state · submitted) | inline comments human/CR | conv comments human/CR | beat(s) from title+branch | title alone identifies beat? | latest activity |
|---|---|---|---|---|---|---|---|---|---|
| #353 | Fixed UI for endless mode | Blake (EMPLOYEE_0032) | 2025-08-02T20:12:29Z | Arthur Blake · APPROVED · 2025-08-02T20:09:52Z | 0 / 0 | 0 / 1 | endless (`/endless-ui-fix`) | **yes** | 2025-08-02T20:09:52Z |
| #356 | Item Updates and Endless Zombie Swap and redo both levels | Robert | 2025-08-03T03:39:22Z | none | 0 / 0 | 0 / 0 | endless + shared items (`/GamePolish0801`) | partly ("Endless" in title, but "Item Updates" dominates) | none |
| #357 | Changed endless bar settings | Blake | 2025-08-05T16:01:19Z | Arthur Blake · APPROVED · 2025-08-05T15:01:02Z | 0 / 0 | 0 / 1 | endless | **yes** | 2025-08-05T15:01:02Z |
| #360 | Endless Level 3, card item color changes | Robert | 2025-08-06T01:03:15Z | none | 0 / 0 | 0 / 1 | endless + shared: items | partly | 2025-08-06T00:04:37Z |
| #364 | New endless level added to rotation | Blake | 2025-08-06T13:40:56Z | Arthur Blake · APPROVED · 2025-08-06T13:40:51Z | 0 / 0 | 0 / 1 | endless | **yes** | 2025-08-06T13:40:51Z |
| #370 | Collect&Win Items | Claire Morgan | 2025-08-13T16:12:18Z | none | 0 / 0 | 0 / 1 | Collect & Win (`ClaireNewObjects_03`) | **yes** | 2025-08-08T13:22:13Z (stale; merged 5 days later) |
| #384 | Endless mode performance issues | Blake | 2025-08-19T13:35:35Z | CodeRabbit · COMMENTED · 2025-08-18T14:02:18Z | 0 / 1 | 0 / 1 | endless (`/perf-fix`) | **yes** | 2025-08-18T14:02:19Z |
| #394 | [PERSON_NAME_0029]/icon management system | Calvin Price | 2025-08-21T17:47:34Z | CodeRabbit COMMENTED 2025-08-20T14:58:06Z; Arthur Blake APPROVED 2025-08-21T17:47:29Z | 0 / 7 | 0 / 1 | shared: icons | **no** (branch name is a person) | 2025-08-21T17:47:29Z |
| #396 | …icon management system | Calvin Price | 2025-08-22T13:39:18Z | none | 0 / 0 | 0 / 1 | shared: icons | **no** | 2025-08-22T13:39:07Z |
| #397 | …icon management system | Calvin Price | 2025-08-22T15:10:54Z | none | 0 / 0 | 0 / 1 | shared: icons | **no** | 2025-08-22T15:10:55Z |
| #400 | …icon management system | Calvin Price | 2025-08-26T00:41:27Z | Arthur Blake · APPROVED · 2025-08-26T00:41:20Z | 0 / 0 | 0 / 1 | shared: icons | **no** | 2025-08-26T00:41:20Z |
| #403 | …icon management system | Calvin Price | 2025-08-26T18:51:03Z | CodeRabbit COMMENTED 2025-08-26T16:00:16Z; Arthur Blake APPROVED 2025-08-26T18:50:58Z | 0 / 2 | 0 / 1 | shared: icons | **no** | 2025-08-26T18:50:58Z |
| #420 | Update EndlessModeBar.cs | Blake | 2025-09-08T15:26:59Z | none | 0 / 0 | 0 / 1 | endless (`/endless-mode-fixes`) | **yes** (file name) | 2025-09-08T15:27:01Z |
| #438 | Feature/season pass | Oliver Brooks | 2025-09-15T23:09:34Z | CodeRabbit COMMENTED ×3 (22:42:53Z, 22:44:05Z, 23:08:36Z) — **no human review at all** | 0 / 73 | 0 / 1 | season pass (`feature/season-pass`) | **yes** | 2025-09-15T23:08:36Z |
| #454 | Marcus/animated icons | Marcus Bennett | 2025-09-19T17:50:52Z | Calvin Price · APPROVED · 2025-09-19T17:50:45Z | 0 / 0 | 0 / 1 | shared: icons | **no** | 2025-09-19T17:50:45Z |
| #456 | [PERSON_NAME_0029]/animated icons | Calvin Price | 2025-09-24T14:30:39Z | CR COMMENTED ×2 (09-22 16:04:21Z, 17:58:01Z); Oliver Brooks APPROVED 2025-09-23T23:31:02Z | 0 / 3 | 0 / 1 | shared: icons | **no** | 2025-09-23T23:31:02Z |
| #459 | [PERSON_NAME_0029]/queue manager | Calvin Price | 2025-09-24T23:06:25Z | CR COMMENTED ×3 (09-23 23:40:50Z, 09-24 18:10:23Z, 22:36:13Z) — no human review | 0 / 6 | 0 / 1 | shared: queue manager | **no** | 2025-09-24T22:36:13Z |
| #465 | [PERSON_NAME_0029]/queue manager | Calvin Price | 2025-09-25T22:15:51Z | CR COMMENTED ×2 (18:43:41Z, 21:43:05Z) — no human review | 0 / 5 | 0 / 1 | shared: queue manager | **no** | 2025-09-25T21:43:06Z |
| #468 | Collect And Win | Owen Baker | 2025-09-29T16:13:50Z | CR COMMENTED ×2 (09-26 20:29:29Z, 21:54:00Z) — no human review | 0 / 37 | 0 / 1 | Collect & Win (`/winAndCollect`) | **yes** | 2025-09-26T21:54:00Z |
| #470 | Collect And Win minor bugs fixes | Owen Baker | 2025-09-30T15:51:15Z | 8 CR COMMENTED + 2 by Owen Baker (self) 09-30 02:43:00Z / 02:50:56Z; Arthur Blake APPROVED 2025-09-30T15:51:06Z | **2 / 7** | 0 / 1 | Collect & Win (`/winAndCollectMinorBugs`) | **yes** | 2025-09-30T15:51:06Z |
| #472 | Implement Win&Collect into Queue Manager | Calvin Price | 2025-09-30T15:53:04Z | Arthur Blake · APPROVED · 2025-09-30T15:52:58Z | 0 / 0 | 0 / 1 | Collect & Win + queue manager (`/ImplementQueueManager`) | **yes** | 2025-09-30T15:52:58Z |
| #475 | [PERSON_NAME_0029]/animated icons | Calvin Price | 2025-09-30T16:09:15Z | Arthur Blake · APPROVED · 2025-09-30T16:09:09Z | 0 / 0 | 0 / 1 | shared: icons | **no** | 2025-09-30T16:09:09Z |

### §4 findings

- **Human inline review comments across all 22 PRs: 2, both on #470, both by the PR author himself (Owen Baker).** CodeRabbit inline comments: 147. So "a human reviewed the code" is false for 21 of 22 PRs.
- **Human conversation comments: 0 of 22.** Every "conv=1" row is CodeRabbit's auto `## Walkthrough` summary (`<!-- This is an auto-generated comment: summarize by coderabbit.ai -->`).
- Human review events are almost all single-click APPROVEs by **Arthur Blake** (9) / **Calvin Price** (1) / **Oliver Brooks** (2). Season Pass (#438, 259 files) and queue manager (#459, #465) merged with **zero human review**.
- The 5 icon-management PRs (#394/396/397/400/403) and 3 animated-icon PRs (#454/456/475) are the same beat ("shared: icons") re-merged repeatedly — a title-only reader cannot tell which one delivered what, and **none of the 22 titles names a live-ops beat except through the branch name**.
- Titles that identify no beat at all: #394, #396, #397, #400, #403, #454, #456, #459, #465, #475 (**10 of 22**) — all "shared: icons / queue manager".

## 5. Base records that already state a live-ops item is DONE/FIXED/LIVE elsewhere

All quotes verbatim. "Ticket" column = where the item formally lives.

| # | item (ticket) | record that says it's done / decided | quote | what it proves |
|---|---|---|---|---|
| A | **ZOM-432** Daily gift artwork needs to have the frame (Todo, untouched since 2025-07-23) | #builds, **Match3D Android Submission #135**, ts `1759263189.219529` = 2025-09-30 20:13Z, "Changes:" list | "- Fixing UI Elements on Daily Gift [Samuel Turner]" | The frame work shipped in the Sep 30 submission candidate while the ticket is still Todo. Same run also carries "- Fixing UI Elements on Plague Race [Samuel Turner]" and "- Fixing UI Elements on Zombie Lane [Samuel Turner]" |
| A2 | ZOM-432 (supporting) | GitHub commit `f0bb8b4822ef97a3ec2ca1e7bd5353f389d2f931`, authored 2025-09-27T03:43:14Z by Samuel Turner, **in PR #471** | message: "Fixing UI Elements on Daily Gift"; PR #471 (`Samuel/zom 498 536`, merged 2025-09-30T15:52:24Z) body: "Added new sprite assets (e.g., tornado popup, blue bar) and **updated Daily Gift sprite configuration**" | commit → PR → build chain, all predate the calendar and none of them touch ZOM-432 |
| B | **ZOM-565** Endless Horde Start Screen Vfx (Todo, created 2025-09-25T13:46:04Z) | GitHub commit `f7e971b02d24206455637099b571115e35a0dab1`, authored **2025-09-25T13:25:12Z** by `marcus` | "Endless Mode start screen VFX" | Work landed **21 minutes before the ticket was even filed**; commit has **no PR mapping** (`pull_request_commits` has no row) → direct commit, invisible to any PR-title search. Also #builds `1759248192.214539` (2025-09-30 16:03Z) build #2023 contains it. |
| C | **ZOM-566** Collect&Win Analytics (Todo, created 2025-09-30T16:26:02Z) | PR **#477 "Collect And Win Analytics and title change"**, head `[PERSON_NAME_0067]/collectAndWinAnalytics`, **open / not merged**; commit `31ee4178bdd316ea9a43e030baf83c793fcf3ed5` authored 2025-09-30T22:23:02Z | commit: "Added analytics events to collect and win"; PR body: "App emits and tracks Collect & Win start and reward-claimed events" | Not "done" but **in flight** — a run that marks this "nothing exists" is wrong; the honest state is "implemented in an unmerged PR" |
| D | **ZOM-471** Add red dot icon for players not in Plague Race (Todo, untouched since 2025-08-13) | #zombie-match3d thread root `1755108052.016359` (2025-08-13 15:xxZ, Samuel Turner), 12 replies; Linear-bot post `1755108077.288629` sits inside it | "i think it's annoying, it already has start button" (1755109202) · "yeah, we don't need it! cancel the ticket lol" (1755109968) · "I don't think we should do it" (1755116903) · counter-argument "So annoyance does get people to join" (1755113199) | The team **decided to cancel** in Slack; Linear still says Todo. Any planning answer that schedules a "red dot for Plague Race" is repeating cancelled work. |
| E | **ZOM-429** Leaderboard next session doesn't start without killing the app (Backlog, updated 2025-09-22T14:51:23Z) | #zombie-bugs `1758546119.789009` (2025-09-22 13:01Z, Oliver Brooks, rc=4), last reply 14:19Z Vincent Parker | "yep, it's working fine right now" (after Oliver: "can you test again? I reverted the changes") | QA closed the loop **in Slack only**; Linear untouched since that same day, still Backlog |
| E2 | ZOM-429 (correction elsewhere) | #builds Submission #123 (ts `1758396905.879569`, 2025-09-20 19:31Z) then Submission #129 (ts `1758854356.576719`, 2025-09-26 02:39Z) | #123: "- Adding safety checks for when leaderboards cant find the players user. Fix Leaderboards not using variant level to check unlock …"; #129: "- **Revert** \"Adding safety checks for when leaderboards cant find the players user…\"" | The fix was shipped and then reverted — a run that only sees #123 will claim it's fixed; only #129 corrects that |
| F | **ZOM-552** Season Pass Analytics (In Progress) | #builds Submission **#123** (2025-09-20 19:31Z, Failure) and build texts 2025-09-18 20:05Z `1758225951.590669` / 2025-09-19 09:28Z `1758274114.222559` | "- Sending SeasonPass_Redeem info to analytics [PERSON_NAME_0022]" · "- Sending SeasonPass premium purchase and event left info to analytics [PERSON_NAME_0022]" | Partially implemented in release notes while the ticket says In Progress — "not started" would be wrong |
| G | **Season-pass claim SFX** (no ticket) — #zombie-bugs thread `1757999990.759409` (2025-09-16 05:19Z, Leonard), last reply 05:58Z "will add first thing in the morning" | #builds Submission **#122** (ts `1758111759.933039` = 2025-09-17 12:22Z) | "- Adding on season pass the same sound use for quests claim [PERSON_NAME_0022]" | The thread visually ends "promised, not confirmed"; the actual fix is in the next day's release notes — the thread is NOT the end of the story |
| H | **Quests rollover / ZOM-534** Quest points not resetting until app restart (In Progress) | #builds Submission #36 (iOS, ts `1757550527.308879`, 2025-09-11 00:28Z) and #130 (ts `1758853965.523629`, 2025-09-26) | #36: "- Using remaining-time endpoint to sync quests end with client [PERSON_NAME_0022]"; #130: "- Fixing tutorial still playing when it shouldnt; fixing quests chests being setted when backend info didnt came [PERSON_NAME_0022]" | Rollover-related code changed twice after the ticket; whether ZOM-534's exact symptom is fixed is **not stated anywhere** — honest verdict "unclear" |
| I | **Collect & Win "completed"** (no ticket) — #company-internal `1758558302.777379` (2025-09-22 16:25Z, Julia Lawson) | Julia's own status update | "• [PERSON_NAME_0067] and Douglas **feature completed Win and Collect**, and will potentially give us a test today. But they anticipate some edge cases so this test isn't a final product test." | A completion claim by the persona's own team, 7 days before PR #468 merged (2025-09-29) and 8 before #470 (2025-09-30) — "completed" ≠ shipped |
| J | **ZOM-344** Quest UI box animation (Todo, never touched) | — none found | searched: all `github.json` commits (11,226) for quest/box-animation messages, every merged PR title/body, all 60 #builds "Changes:" lists Aug–Sep, #zombie-art and #zombie-design quest posts | Genuinely **still undone** — this is the control case that keeps the trap set honest |
| K | **Axe Arena / Boss Arena off-calendar corroboration** — #company-internal `1758558164.541689` (2025-09-22 16:22Z, Brian Foster) | "We've decided to **postpone Axe Arena** for the beta release. We'll be focusing on tech issues and bugs" | Confirms the exclusion of Axe Arena from the Oct 6 – Nov 2 calendar, and it is dated before the seed bound |

Section-5 caveat: the phrase "Commits between the two tags" does **not** occur in any cached #builds message; the equivalent artefact is the `Changes:` bullet list attached to each `Match3D Android/iOS Submission - #n` success/failure post (60 such posts in Aug–Sep). Searching for the literal phrase finds nothing, which is itself a search-dead-end worth knowing.

## 6. Summary — per-thread call count and best trap candidates

### 6a. Honest call count for §1

A correct run must open, at minimum:

- **24 root reads** (Sep 15–30, six human channels) to establish which roots are in-scope beat faults. Roots #2, #3, #5, #7, #11, #12, #14, #21, #22, #23 have `reply_count = 0` → 1 call each, no thread read needed (10 calls).
- **14 thread reads** for the 14 roots with replies, because the deciding information is in the tail: #1, #4, #6, #8, #9, #10, #13, #15, #16, #17, #18, #19, #20, #24.
- Two of those (#12 → #13, and #18 → the ZOM-549 spin-off in a different thread) only make sense if you also read a **sibling** root: +2 calls.
- #builds: the beat-relevant evidence is only in the 60 `Submission` posts (of 1,133 messages in Sep), so 1 broad query + 1 filter pass, or 60 posts if read one-by-one. Count it as **1–2 calls** with the right query, 60 without.

**Total honest §1 surface: 24 + 14 + 2 + 2 ≈ 42 reads (range 40–102 depending on whether #builds is filtered or brute-forced).** Additional cost per thread: writing it up.

The expensive part is not the count, it is that **13 of the 14 threads end on a reply with no beat keyword** and **24 of 24 contain no ZOM id**, so keyword search over replies returns the wrong thread or nothing; only reading the tail of each thread answers "fixed / still broken / unclear".

### 6b. Best 3–5 "done elsewhere / corrected elsewhere" traps

1. **ZOM-432 — Daily gift frame (strongest).** Ticket Todo, never updated, body is a single screenshot with no text. The work shipped twice: commit `f0bb8b48` "Fixing UI Elements on Daily Gift" (Sep 27) → PR #471 → Android Submission #135 "Changes:" line (Sep 30 20:13Z). Discovery requires joining Linear → GitHub commit text → #builds release notes; no id appears in any of the three.
2. **ZOM-565 — Endless Horde Start Screen Vfx.** Ticket Todo, filed 2025-09-25T13:46:04Z; commit `f7e971b0` "Endless Mode start screen VFX" is authored 13:25:12Z the same day and belongs to **no PR**, so a PR-title-only sweep misses it entirely. Cleanest demonstration that "open ≠ not done".
3. **ZOM-471 — Red dot for Plague Race.** Todo forever, but the 12-reply #zombie-match3d thread (Aug 13) explicitly kills it ("cancel the ticket lol", "I don't think we should do it"). A planner who schedules it is contradicting a recorded decision; the correct answer is "cancelled in Slack, stale in Linear".
4. **ZOM-429 — Weekly leaderboard restart.** Two-way trap: Slack QA says "working fine right now" (Sep 22 14:19Z) and Linear still says Backlog; meanwhile #123 shipped "safety checks for when leaderboards cant find the players user" and #129 **reverted** it. The only defensible status is "reverted fix, still open".
5. **Season-pass claim SFX thread (#zombie-bugs 1757999990).** Thread ends on "will add first thing in the morning" — reads as unfinished; the fix is in Submission #122 the next day ("Adding on season pass the same sound use for quests claim"). Best example of a Slack thread whose tail is *not* the outcome, which is exactly the failure mode §1 is built to test.

Runner-up (avoid as primary, weaker evidence): ZOM-566 Collect&Win Analytics — an open PR (#477) rather than a merge, so it relies on the solver understanding "open PR" ≠ done.
