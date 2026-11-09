# Blind fork sweep rev2

SQL reviewed: `01_Universe_Inject.sql`, sha256 8766100f768ab9aabf51cf4bf5a5791914fed1639c92d52b538f3dd8b54476c0. All statements read.
Universe: Oct 1 2025 synth-cut. Persona: Samuel Turner.

## 1. Result

| | Count | Rows |
|---|---|---|
| Go | 3 | DES-315, DES-316, DES-317 |
| Hold | 25 | T2: 5. T3: 17. T4: 1. T5: 1. T6: 1 |
| Drop | 7 | T1: 6. Covered by another message: 1 |
| **Rows** | **35** | 14 sheet rows + DES-328..346 (19) + 2 asks in ZOM comments |

Forks: **1 HIGH, 6 MEDIUM, 16 LOW.**

The Go total is firm. Hold and Drop can each move by one, through DES-346 and the ZOM-556 ask. See section 5.

## 2. My call table

Test numbers are the rule doc's. "Backlog" means Backlog and unassigned. Final headline and String change are blank on non-Go rows, as the rule doc says.

### Sheet rows (spreadsheet /sheets_spreadsheets/220, tab PNs Beta)

| # | Message | Ticket | Call | First failed test | Final headline | String change | Audience | State after call | Deciding records |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Quests rollover | DES-321 | Hold | T3 | | | everyone | In Review to Backlog | DES-321 description (quests in production); cmt_7b184259cfbb33052325; cmt_4aa525e0162ec9ef15f6 |
| 2 | Hourly Coins | DES-324 | Drop | T1 | | | everyone | In Review to Canceled | Trello 68d1eb1af2a60631ad39b617 (Hourly Collection, Oct 21 to Backlog); DESIGN_EVENTS has 0 ZM rows among 3,377 hourly_collect rows; cmt_144462e04c0e02c19d02 |
| 3 | Lives recharged | DES-315 | Go | none | Full Ammo Reloaded! 🔫 | No | everyone | Done, stays | cmt_2395189dfd5e7d5c1e88; cmt_51e018b23e18c2f680cd; Beta tab row 1; rc_18 hunk |
| 4 | Lapsed 1 day | DES-316 | Go | none | The Horde Is Growing… 🧟‍♂️ | No | everyone who has stopped | Done, stays | cmt_d6bf99cc8b3e926c2569; cmt_5ab75e0ee96e70745960; Vincent QA note (phone date allowed); rc_18 hunk DailyNotifications |
| 5 | Lapsed 7 days | DES-317 | Go | none | Your Squad Needs You Back | Yes | everyone who has stopped | Done, stays; string ticket added | Slack d2b16907dc8c10fe5052805751097b58; cmt_f64ebdf08bef6b136513; cmt_e4bb9fe925b86f52cf55; rc_18 hunk |
| 6 | Finish first mission | DES-318 | Hold | T4 | | | new players below level 20 | Done to Backlog | Slack 37c5701a1780374401d295e86884f276 and 09aae609aa744fb23288c7dcbac9926c; cmt_886fb8b04e3b6ba66b57; cmt_f4960d3c073493b6bfc6 |
| 7 | Win & Collect event start | DES-313 | Hold | T3 | | | players on the event | In Review to Backlog (Calvin removed) | page_liveops_calendar (same feature, built for beta); card 6851a7abf7876721472dba99; cmt_cb634ee40df2ae6c6022; cmt_7c6c022293a0505fbf85 |
| 8 | Nathan's Treasure Hunt start | DES-325 | Drop | T1 | | | everyone | In Review to Canceled | page_liveops_calendar (Domino Delights one-off); no ZM card |
| 9 | Plague Race | DES-319 | Hold | T6 | | | players past the race unlock | Done to Backlog | Slack 4a5ee02518ff2fbeacaef2fc6d5a9ef9; Vincent QA note; cmt_fd950c410ed25c447c02; cmt_9338bb2c286a6c207792; cmt_10ae5518084785a96cfc |
| 10 | Streak Fever start | DES-326 | Drop | T1 | | | everyone | In Review to Canceled | page_liveops_calendar (Domino Delights); LIVE_EVENT_PERFORMANCE has no ZM rows; no ZM card |
| 11 | Axe Arena start | DES-327 | Drop | T1 | | | everyone | In Review to Canceled | Trello 68d1eb0c134ce36d25dcea3c (BETA to Oct 21, Sep 23) |
| 12 | Login Calendar update | DES-322 | Hold | T3 | | | everyone | In Review to Backlog | DES-322 description; cmt_5acbc1a3f111af34e7ac; cmt_8531c2616065b39e5c26 |
| 13 | Season Pass start or reward | DES-323 | Hold | T3 | | | players past the pass unlock | In Review to Backlog | card 6851ab766fcaf894d0c0048b (BETA list); cmt_181bcd11a979359893fb; cmt_3dabe2da836af3cc9ba8 |
| 14 | Weekly Leaderboard reset | DES-320 | Hold | T5 | | | players past the leaderboard unlock | Done to Backlog | match3d#248#rc_18 and its Gmail copy; cmt_f1b42e3a7c9cfa136439 |

### Asks under DES-314

| # | Message | Ticket | Call | First failed test | Audience | State after call | Deciding records |
|---|---|---|---|---|---|---|---|
| 15 | Endless entries are back | DES-328 | Hold | T3 | players who used all their entries | Backlog | page_liveops_calendar; cmt_c6f09d1660c6a174811f; cmt_55c7d795dc967c39c6a5 |
| 16 | Endless weekly result | DES-329 | Hold | T2 | players who ranked that week | Backlog | cmt_9d5748e1540a9588ceb9; cmt_6e27d2eb839bbc66a95a |
| 17 | Boss Arena is open | DES-330 | Hold | T3 | players past the arena unlock | Backlog | card 6851ab7090e82351a14e7837; ZOM-487; cmt_e4ac33987005778b372e; cmt_c6a61568172ef0ebb990 |
| 18 | Boss Arena last hours | DES-331 | Hold | T3 | players who started the arena | Backlog | cmt_e1c7ebcf5aa9ee4b4a8c; cmt_d9f2d461e083b4a65263 |
| 19 | Season Pass last 48 hours | DES-332 | Hold | T3 | players with unclaimed tiers | Backlog | cmt_44a1117f30fbb476c28c; cmt_e911c52cf054cb3ed19b |
| 20 | Season Pass premium nudge | DES-333 | Hold | T2 | free-track players near a premium reward | Backlog | cmt_ff7c43f0633261872ec7; cmt_2456f47526183e4e1161 |
| 21 | Plague Race last hour | DES-334 | Hold | T3 | players in a race | Backlog | cmt_521d7e03d14d535f1d5b; cmt_abb99f26dc3013206909 |
| 22 | Plague Race result | DES-335 | Hold | T2 | players in a race | Backlog | cmt_fda157bae8336585356a; cmt_83e42df52254cf27fe4d |
| 23 | Zombie Lane reward ready | DES-336 | Hold | T3 | players with a reward to claim | Backlog | page_liveops_calendar; cmt_b55d6a0b35ae5242ffd4; cmt_546a8f6d521e2d00dc28 |
| 24 | Achievement reward waiting | DES-337 | Hold | T3 | players with a reward to claim | Backlog | ZOM-363; cmt_4feec391e19bb4a4a16a; cmt_cd8081a714a205760ce7 |
| 25 | Daily chest ready | DES-338 | Hold | T3 | everyone | Backlog | match3d#317; cmt_32da06fe646ada57c7fa; cmt_b770ad38987fc947c65f |
| 26 | Free shop coins ready | DES-339 | Hold | T3 | everyone | Backlog | ZOM-539 (daily free coin); cmt_aa68a0b0ee32e8e24c58; cmt_e0e37d68814e1eae6002 |
| 27 | Support reply waiting | DES-340 | Hold | T2 | players with an open support thread | Backlog | match3d#277; cmt_31db977b4adf091259da; cmt_a6c862db8697a973afc7 |
| 28 | New levels added | DES-341 | Hold | T2 | players past the hand-made levels | Backlog | cmt_96b8c0e10b3d2b20a982; cmt_904474dee7687823b700 |
| 29 | Lapsed 3 days | DES-342 | Hold | T3 | everyone who has stopped | Backlog | cmt_af799d5941e425ad3e53; cmt_1443f47829522f8bb44e |
| 30 | Lapsed 30 days | DES-343 | Hold | T3 | everyone who has stopped | Backlog | cmt_58672546fb6435495753; cmt_fe5087128f529fdbb69f; rc_18 hunk (weeksToCover 4) |
| 31 | Lapsed 14 days | DES-344 | Drop | none; covered by Lapsed 7 days | everyone who has stopped | Canceled | Gmail `<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com>`; evt_b56d5b19baa0a573da4553; rc_18 hunk; cmt_fd99936084694fa6d973 |
| 32 | Comeback gift on tap | DES-345 | Drop | T1 | everyone who has stopped | Canceled | cmt_13477aa8d1468ae11c9d; cmt_8c95a627941e0b32e091 |
| 33 | Rewarded ad ready | DES-346 | Drop | T1 (see H1) | everyone | Canceled | Trello 68d1eb16ac8c64cf8165101d; page_qa_runbook Ads row; cmt_bd206b061637646ac5cb |

### Asks with no ticket

| # | Message | Ticket | Call | First failed test | Audience | State after call | Deciding records |
|---|---|---|---|---|---|---|---|
| 34 | Boss Arena attempts refilled | new, child of DES-314 | Hold | T3 | players who used their attempts | Backlog | cmt_f1b8a109dfa70cdc4565 on ZOM-542 |
| 35 | Gift streak resets tomorrow | new, child of DES-314 | Hold | T3 | players on a gift streak | Backlog | cmt_2b519285937e7fa79453 on ZOM-556 (see M1, M2) |

### Other writes I would make

- **Hold override:** Trello 68dae8c7d95e24b55b69bf80 on Fix TECH ISSUES sends held work to Backlog, unassigned, which the rule doc allows ("unless the roadmap says otherwise").
- **New tickets:** 3 in team DES under DES-314: rows 34 and 35, plus one string ticket for Lapsed 7 days. Counter is 346, so expect DES-347 to DES-349. The DES-314 description keeps these out of ZOM.
- **Checklist:** on card 6851a769c65dc0017a227bb7, three unticked items (rows 3, 4, 5). Basis: Trello 68d415a716abcb84070a8e2a.
- **Emails, 7 people, 20 asks:**
  - Calvin: DES-313, 338
  - Brian: DES-328, 329, 333, 345, ZOM-542 ask
  - Robert: DES-330, 331, 344, 346
  - Oliver: DES-332
  - Julia: DES-334, 335, 341, ZOM-556 ask
  - Owen: DES-336, 337, 340
  - Martin: DES-339
  - Leonard's own 15 rows get no email (13 sheet rows, DES-342, DES-343).
- **Note facts:**
  - Sep 15 cohort, zombie_match_3d: iOS D1 31.65, D7 9.28 (237 installs). Android D1 37.86, D7 10.68 (103 installs).
  - Hearing from us needs our own ask after level 20. Players who leave earlier hear nothing, unless they used the settings toggle (see M4).
  - Lapsed reminders: day 1, then the weekly line on days 7, 14, 21 and 28. Nothing on day 3 or day 30.

## 3. Forks

### HIGH (1)

**H1. DES-346 Rewarded ad ready: is the feature "live today"?**
- Reading A: Drop T1. The card moved from BETA to Oct 21 on Sep 23 (68d1eb16ac8c64cf8165101d). page_qa_runbook marks Ads as ZM3D "n/a" (Aug 4). Leonard's Sep 12 post (2e176d7fccaddc7a7e57dcdba0d0be08) lists rewarded ad surfaces as work to do. No match3d PR or ZOM ticket adds ads.
- Reading B: Hold. T1 is an OR, and the board only proves "not on the BETA list". ANALYTICS.RAW_TELEMETRY.AD_IMPRESSION_EVENTS has zombie_match_3d rows with ad_format rewarded_video, placement rewarded_continue. In a sample of 48 rows dated Sep 21 to 27, 4 were rewarded. That sample comes from a search capped at 4,000 ZM rows, so it is not a full count.
- Why HIGH: the records lean Drop, but nothing dated after the impressions says rewarded ads are not in the client. The runbook predates them. DES-346 is also the one ask with no feature evidence of its own: Arthur's comment round ended Sep 25 and the ticket was filed Sep 29.
- Limit: this fires only if a solver opens that table, and nothing points there.
- Effect: Hold 26, Drop 6.
- Settle with: one Arthur comment on DES-346, for example "rewarded ads aren't in the client, moved to Oct 21".

### MEDIUM (6)

**M1. ZOM-556 ask: separate from DES-338, or already ticketed?**
- Reading A: separate message, new ticket. Different trigger and audience.
- Reading B: same ticket. ZOM-556 and DES-338 carry a mutual relation, and the DM says not to make a second ticket "under whatever name".
- Brian's ZOM-542 comment says "separate from the weekly board ping". Julia's comment has no such sentence.
- Effect of B: rows 34, Hold 24, one fewer new ticket.
- Settle with: add "separate from the chest ping on DES-338" to cmt_2b519285937e7fa79453.

**M2. ZOM-556 ask: T1 when the feature behind it is broken.**
- Reading A: Daily Gift is live (match3d#317), so T1 passes and the row is Hold T3.
- Reading B: the feature behind it is the streak reset. ZOM-556 says that does not work, the ticket is Todo, and it is not on the BETA bug card (68c451141c69fb8af1b4568e lists 18 ZOM ids, not this one). That is Drop T1.
- I side with A, because a bug in a live feature is still live, but no dated record says so.
- Effect of B: Hold 24, Drop 8.
- Settle with: add ZOM-556 to the BETA bug card, or have Julia's comment say the gift streak is live and only the skip case is broken.

**M3. String ticket: state and assignee.**
- The rule doc says only "a string ticket under DES-314".
- Reading A: Todo, because it is beta work, and the Sep 29 comment only bars non-beta work from Todo.
- Reading B: Backlog, unassigned, as the default.
- Assignee has no record at all.
- Settle with: one sentence in the rule doc, or do not grade state or assignee.

**M4. Note: who "actually hears from us".**
- Reading A: players past our ask at level 20, using T4's language.
- Reading B: those players plus anyone who used the settings toggle. Slack 09aae609aa744fb23288c7dcbac9926c says the client schedules for both, and cmt_f4960d3c073493b6bfc6 shows it arriving. T4 excludes the toggle for the test, not for what really happens.
- Reading C: only players who said yes. The code defaults NotificationsEnabled to false.
- No record defines a number either, so a reader may or may not compute one.
- Settle with: tighten the DM, or grade only "nobody before our level 20 ask, apart from the settings toggle".

**M5. Note and DES-341: LIVE_OPS.EVENTS.PUSH_NOTIFICATION_STATS contradicts "all local".**
- The table has 25 zombie_match_3d rows from Apr 12 to Sep 27, provider firebase. They include comeback_7d to segment lapsed (275 sent Sep 6) and new_levels (278 sent Sep 27).
- Against it: Leonard, b43da6b90f8b2573ee79893932b352b9, "All our PNs are local" (Sep 18). Arthur, D06KV30TPL4 Jun 26, "We aren't using Push Notifications yet". The first send also predates the client code (#248, Jun 26).
- Reading A: ignore the table.
- Reading B: report in the note that lapsed players already get server pushes, and that a new-levels server send already exists.
- No Call flips, because T2 still fails for DES-341. The note's content does change.
- Settle with: a short Slack line that the stats table does not reflect ZM client messages, or do not penalise a caveat.

**M6. Email form.**
- "Email everyone else who asked" fits 7 individual emails or one group email listing each person's asks.
- The recipient set is stable at 7. The send count is not.
- Settle with: "email each of them", or grade per-person coverage only.

### LOW (16)

| ID | Rows | Fork | Why LOW | Settling wording or record |
|---|---|---|---|---|
| L1 | DES-325, 326, 327 | T1 says "live today" but not which game. Streak Fever and Axe Arena are live on Domino Delights. A literal reader gets Hold T3 | "The beta" and the sheet are Zombie Match, and LIVE_EVENT_PERFORMANCE has no ZM rows for them | Rule doc: "live today in Zombie Match" |
| L2 | DES-343 | Weekly batch ends on day 28, so does it cover "a last reminder at 30 days"? | Rule doc says the day matters; Leonard's note names only day 14; Arthur says it is not there | None needed |
| L3 | DES-344 | T3 literally passes (day 14 is scheduled), or fails (no such message). Either way the Drop clause applies, so the "first failed test" cell is unclear | Call is fixed; only that cell varies | Grade "covered by Lapsed 7 days" |
| L4 | DES-320 | The only T5 evidence is Jun 26 (rc_18). Blobs are unreadable, and Vincent's Sep 24 pass could suggest a fix | No PR or commit message after Jul 21 touches it, and the QA pass shows arrival only. This is the one route to Go 4 | Arthur comment on DES-320: "still keyed off last session" |
| L5 | DES-316 | Next server midnight can be under 24 hours after leaving | Rule doc: "the day does" | None needed |
| L6 | Row 7 | "Window opens" vs "event start"; DES-313 sits outside DES-314 and may need re-parenting | Confluence names them the same feature; no record asks for a re-parent | Do not grade parent |
| L7 | DES-324, 339 | Hourly coins vs free shop coins could be one message | ZOM-539 says daily free coin; Hourly Collection is a separate Backlog card | None needed |
| L8 | DES-330, 331, row 34 | "Boss Arena" is not the card name on the BETA list | ZOM-487 is titled "Infinite HP Boss Arena"; match3d#424 matches | None needed |
| L9 | All sheet rows | Audience from the ticket comment or the sheet Segmentation column (Plague Race, DES-313 say "Everyone" on the sheet) | DES-314 puts "who it's for" in a comment | Rule doc: "from the ticket comment" |
| L10 | DES-318, 319, 320 and all Holds | Three edges of the Backlog rule: does a Done ticket "go back"; is a Hold on a beta feature "beta work"; has "until the beta build is out" expired | DM says move to match; second sentence covers all held work; the list now reads BETA: Oct 10 and no record says the build is out. The injected action says "BETA: Sep 30", a cosmetic mismatch | Add the date to the card comment |
| L11 | ZOM-542, ZOM-556 | Does "each ticket" include the ZOM tickets for the comment or the move? | Those are bug tickets; the call belongs on the new child, and a pointer comment does no harm | Neither require nor forbid it |
| L12 | Population | ENG-2311 (Done May 2025) and DD cards are older asks for event pushes | Domino Delights, finished, before the ZM client code; Arthur's Sep 25 comments are newer | None needed |
| L13 | Sheet | Two spreadsheets have a PNs Beta tab (/73 and /220) | Only /220 has the Ready column and the ZM rows | None needed |
| L14 | Checklist | Item text: message name or headline; pre-tick since Vincent already passed them? | Trello comment says Vincent ticks them | Grade the three names only |
| L15 | DES-327, 346 | Sep 12 post puts Axe Arena and rewarded ads in beta scope; the board moved them Sep 23 | Rule doc names the board, and the board is later | None needed |
| L16 | Note | For days 7 to 28, name the line shipping today or the final headline? | The string ticket has not shipped, so both are true | Accept either if the change is stated |

## 4. Rule doc against later records

- Hold to Todo vs Backlog (Sep 26 vs Sep 29): clear winner, by the rule doc's own exception.
- Final headline, permission ask: later records fill in what the rule doc delegates. No conflict.
- Sep 18 "punt further" vs Sep 29 "not pushing it further": Robert's later post wins.
- iOS popup at launch vs ask at level 20 (272c3bf3bb5ac118c783b99cbe629724, 2ffa97bfac3b7e217987e8ce4c5c9837): Arthur's Sep 29 reply settles it.
- The DM says the sheet rows have tickets under DES-314. Win & Collect's does not, but "under whatever name" covers it.
- No disagreement is left without a winner, apart from the warehouse conflicts in H1 and M5.

## 5. How stable the totals are

- **Go 3: firm.** Each passes all six on dated records. The only route to 4 is trusting Vincent's arrival over rc_18 (L4), which I do not consider a fair reading. I found no route to 2.
- **Hold 25: firm to within one.** 24 if M1 or M2 is taken, 26 if H1 is taken.
- **Drop 7: firm to within one.** 6 under H1, 8 under M2.
- **First failed tests** are stable, with the DES-344 cell (L3) the only soft one.
- Rows that look risky but held up: Hourly Coins, Plague Race, Finish first mission, Lapsed 14.
- Fixing H1, M1 and M2 needs three short edits and would lock 3 / 25 / 7.

## 6. Text addressed to a solver or grader

- **Injected rows: none found**, by read-through and by a keyword scan.
- **SQL lines 1 to 4** are authoring comments, not rows: "Are you planning to inject?", "persona Samuel Turner", "Long Horizon", "before every agent run". Strip them if the SQL is ever shown to a solver or grader.
- **Spec-like but in Leonard's voice:** rule doc lines such as "Final headline and String change are only for Go rows". Fine as they stand.
- **Base text, not injected:** page_qa_runbook ("Treat the route's existence as a trap") and page_liveops_calendar ("do not quote a duration"). Neither touches these rows.

## 7. Method and limits

- Base reads went through `hg.py search`. I also read `Evals/SEARCH.md` for request formats. Nothing was run as SQL and nothing else was edited.
- **Repo blobs were not read.** Client code comes from review hunks, so the current state of NotificationManager rests on those plus Arthur's Sep 25 comments.
- **Scratch files.** My first few scratch files went into the shared session scratchpad, not a new directory. I moved them to `blind_sweep.8xSkd0` inside it. Names: parse2.py, parse_issues.py, fetch.py, linear.json, sheet220.json, sheet73.json, err220, err73, trello_all.json. If any of those names already existed there, that file was overwritten and then moved. A listing also showed me other session files by name (ledger.md, delta.md, timeline.md and others). I opened none of them.
- **Off-limits path.** Two oversized tool outputs were auto-saved under `/home/sumit/.claude/.../tool-results/`. I never read those files, and they held only my own GitHub query output. The auto-attached memory index was in my context; I did not open any memory file.
