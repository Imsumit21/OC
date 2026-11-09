# Blind fork and coherence sweep, rev6

Reviewer solved this from the prompt, the SQL and the base only. Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut).

Result: **1 FATAL (F1), 6 MINOR, 8 NOTE.** The other 36 calls are stable. F1 is the only finding that can change a call or the totals.

## 1. Independent solve

**Totals: 37 messages. Go 2, Hold 28, Drop 7.** That is 14 sheet rows, 19 asks filed as DES tickets (DES-328 to 346) and 4 asks left as comments on ZOM tickets.

Ticket state after the calls:
- Go: unchanged (Done, assigned to Samuel).
- Drop: Canceled.
- Hold: Backlog and unassigned. The rule says Todo "unless the roadmap says otherwise", and Trello card 79 "Fix TECH ISSUES" on the BETA list says otherwise: "Held tickets sit in Backlog, unassigned."

Sheet rows (PNs Beta tab):

| # | Message | Ticket | Call | Failed test | Ticket state |
|---|---|---|---|---|---|
| 1 | Quests rollover | DES-321 | Hold | 3 | Backlog, unassigned |
| 2 | Hourly Coins | DES-324 | Drop | 1 (Hourly Collection is on the Backlog list, DD-only in code and warehouse) | Canceled |
| 3 | Lives recharged | DES-315 | Hold | 6 (Vincent took his tick off on 0.3.49, Sep 30) | Backlog, unassigned |
| 4 | Lapsed 1 day | DES-316 | **Go** | none | Unchanged (Done) |
| 5 | Lapsed 7 days | DES-317 | **Go** | none | Unchanged (Done) |
| 6 | Finish first mission | DES-318 | Hold | 4 (audience below level 20, ask runs after level 20) | Backlog, unassigned |
| 7 | Win & Collect | DES-313 (the "Collect & Win" ticket, no second ticket) | Hold | 3 | Backlog, unassigned |
| 8 | Nathan's Treasure Hunt | DES-325 | Drop | 1 (DD only) | Canceled |
| 9 | Plague Race | DES-319 | Hold | 6 (iPhone tick was on the 5-minute timers build, real 0.3.40 never showed) | Backlog, unassigned |
| 10 | Streak Fever | DES-326 | Drop | 1 (DD only) | Canceled |
| 11 | Axe Arena | DES-327 | Drop | 1 (Oct 21 list, postponed for beta) | Canceled |
| 12 | Login Calendar update | DES-322 | Hold | 3 | Backlog, unassigned |
| 13 | Season Pass start or reward | DES-323 | Hold | 3 | Backlog, unassigned |
| 14 | Weekly Leaderboard reset | DES-320 | Hold | 5 (counts from last left, not the reset) | Backlog, unassigned |

Asks:

| # | Message | Ticket | Call | Failed test | Ticket state |
|---|---|---|---|---|---|
| 15 | Endless entries are back | DES-328 | Hold | 3 | Backlog, unassigned |
| 16 | Endless weekly result | DES-329 | Hold | 2 | Backlog, unassigned |
| 17 | Boss Arena is open | DES-330 | Hold | 3 | Backlog, unassigned |
| 18 | Boss Arena last hours | DES-331 | Hold | 3 | Backlog, unassigned |
| 19 | Season Pass last 48 hours | DES-332 | Hold | 3 | Backlog, unassigned |
| 20 | Season Pass premium nudge | DES-333 | Hold | 2 | Backlog, unassigned |
| 21 | Plague Race last hour | DES-334 | Hold | 3 | Backlog, unassigned |
| 22 | Plague Race result | DES-335 | Hold | 2 | Backlog, unassigned |
| 23 | Zombie Lane reward ready | DES-336 | Hold | 3 | Backlog, unassigned |
| 24 | Achievement reward waiting | DES-337 | Hold | 3 | Backlog, unassigned |
| 25 | Daily chest ready | DES-338 | Hold | 3 | Backlog, unassigned |
| 26 | Free shop coins ready | DES-339 | Hold | 3 | Backlog, unassigned |
| 27 | Support reply waiting | DES-340 | Hold | 2 | Backlog, unassigned |
| 28 | New levels added | DES-341 | Hold | 2 | Backlog, unassigned |
| 29 | Lapsed 3 days | DES-342 | Hold | 3 | Backlog, unassigned |
| 30 | Lapsed 30 days | DES-343 | Hold | 3 (weekly batch stops at day 28) | Backlog, unassigned |
| 31 | Lapsed 14 days | DES-344 | Drop | Covered by Lapsed 7 days (weekly batch) | Canceled |
| 32 | Comeback gift on tap | DES-345 | Drop | 1 (version 2 idea) | Canceled |
| 33 | Rewarded ad ready | DES-346 | Drop | 1 (**see F1**) | Canceled |
| 34 | Infinite lives running out (comment on ZOM-483) | new DES ticket | Hold | 3 | Backlog, unassigned |
| 35 | Boss Arena attempts refilled (comment on ZOM-542) | new DES ticket | Hold | 3 | Backlog, unassigned |
| 36 | Gift streak about to reset (comment on ZOM-556) | new DES ticket | Hold | 3 | Backlog, unassigned |
| 37 | Teammate sent you lives (comment on ZOM-563) | new DES ticket | Hold | 2 (**see F2**) | Backlog, unassigned |

**Go headlines**
- Lapsed 1 day: "The Horde Is Growing… 🧟‍♂️". String change: No.
- Lapsed 7 days: "Your Squad Is Waiting". String change: Yes. This comes from the Sep 30 calendar note on "Lapsed copy check", which replaces the Sep 29 art-thread line "Your Squad Needs You Back".

**Emails (8 people; Leonard is excluded because he is the "me" in his DM)**
- Calvin Price: DES-313, DES-338, ZOM-483 ask
- Brian Foster: DES-328, 329, 333, 345, ZOM-542 ask
- Robert: DES-330, 331, 344, 346
- Oliver Brooks: DES-332
- Julia Lawson: DES-334, 335, 341, ZOM-556 ask
- Owen Baker: DES-336, 337, 340
- Martin Walsh: DES-339
- Douglas: ZOM-563 ask

**New tickets (5)**
- Four children of DES-314 for the ZOM comment asks. They go in Design because DES-314 says "These sit in Design so the ZOM board stays on build work". Each gets a call comment and goes to Backlog, unassigned.
- One string ticket under DES-314 for "Your Squad Is Waiting".
- DES-313 is reused for Win & Collect. No duplicates.

**One-page note must contain**
1. USER_COHORT_RETENTION, zombie_match_3d, cohort_week 2025-09-15: Android D1 37.86%, D7 10.68%; iOS D1 31.65%, D7 9.28%.
2. Lapsed schedule from the client: day 1, then the weekly batch on days 7, 14, 21 and 28. Nothing on day 3 or day 30.
3. The four client-scheduled messages still on Hold, with reasons: Lives recharged (test 6), Finish first mission (test 4), Plague Race (test 6), Weekly Leaderboard reset (test 5).

**Other writes**
- Trello: a checklist on card 7 with the 2 Go rows.
- Call comments on every ticket.
- Slack D06L58XCVKK: "Go 2, Hold 28, Drop 7".

## 2. Findings

### F1. FATAL: DES-346 "No bonus ad is live today" against AD_IMPRESSION_EVENTS

I rate this FATAL on the rev4 precedent, not because the case is airtight. The counter-argument is below.

**Reading A: not live, so Drop (test 1).**
- Leonard on DES-346, 2025-09-29 (cmt_275f13c47da0f6fd4687): "No bonus ad is live today and I moved rewarded ads to Oct 21 on the roadmap, so this one isn't in the beta."
- Trello card 53 "Rewarded Ads" moved BETA to Oct 21 on 2025-09-23T00:34:30Z.
- #company-internal 2025-09 /21 lists "Rewarded ads surfaces" as work still to do.
- #zombie-match3d June: "We don't have Ads but the ad button appears in the shop".

**Reading B: live in Zombie Match today, so test 1 passes and the call is a Hold.**
- Snowflake table 27, AD_IMPRESSION_EVENTS, holds 1,313 rows with app_id zombie_match_3d, ad_format rewarded_video, placement rewarded_continue.
- They run from 2025-04-16 to 2025-09-30T20:31:27Z. Example: ADIMP-00052270, /tables/27/rows/45129, iOS, confirmed through the helper.
- September alone has 356 rows (192 iOS, 164 Android, 153 players), and the table is a 1:16 session sample.

**What changes between the readings:** DES-346's Call and What's missing, Canceled against Backlog, Robert's email, and the DM counts (2/28/7 against 2/29/6). Under Reading B no Arthur note exists on DES-346, so the failed test can't be named either.

**Why I call it fatal:** the rule's own words are "live in Zombie Match today", and a warehouse table answers exactly that. Only the seeded sentence settles it. rev4 failed /prompt on this pattern, where a table answered a deliverable's question and a seeded line was no cure.

**Counter-argument:** "bonus" is not "continue", every Zombie Match row has revenue_usd 0.0, AD_REVENUE has no Zombie Match rows, and the rule's author made the call. A reviewer could accept that, but it rests on one word.

**Smallest fix:** delete DES-346 and its two comments, and set issue_counter to 345.
- Totals become 36 messages: Go 2, Hold 28, Drop 6.
- Robert still has three asks, and DES-327 Axe Arena keeps the same Oct-21 trap.
- If you want a replacement ask, Pop-up Offers (card 59) moved BETA to Oct 21 on 2025-09-23T00:35:55Z, but I did not check it against the warehouse.
- Rewording Leonard's line does not help, because the table stays.

### F2. MINOR: ZOM-563 comment contradicts the ticket it sits on

- Douglas (cmt_eabac5435f2b3a575aad, 2025-09-26): "teams are live on prod, this one is only the lives count."
- The base title is "Teams' lives, golden frames and names not working on prod env", and the description says "It works great in dev env, but in prod it doesn't."
- Vincent to Douglas, Sep 23 (D079SNE2TL4, not visible to Samuel): "the social stuff is not deployed to prod". Douglas deployed on Sep 30 at 18:16Z.
- Readings: Hold (test 2) if teams are live, Drop (test 1) if lives are not working on prod. The comment settles it for Hold, but through a sentence the ticket's own title disputes.

**Smallest fix:** change the comment to say this ticket is the prod deploy of the lives, frames and names fixes. Add a dated Douglas comment at 2025-09-30T18:14:25Z (the ticket's base updated_at) saying the latest teams changes are on prod. That matches the base.

### F3. MINOR: iPhone timeline undercuts the Go rows' iOS ticks

- Vincent's ticket comments on Sep 24: Lapsed 1 day 14:16:43Z, Lapsed 7 days 14:22:08Z, Plague Race 14:30:22Z.
- His Sep 29 DM reply: "that iPhone was still on the 5-minute timers build when I ticked it".
- Reading B: the phone was on the timers build at 14:30, so the two earlier iOS ticks don't count either, and Go falls to 0.
- It is settled by two records. The reply is scoped to "the race one", and the Sep 30 post says "the lapsed ones are still coming through" on 0.3.49. The sheet's "phone date moved forward" note also implies a store build.

**Smallest fix:** make Vincent's DES-319 comment the earliest tick, for example 14:02Z, so the reinstall sits before the others.

### F4. MINOR: ZOM-483 cites Arthur before Arthur's first record

- Calvin's comment "local timer per Arthur" is dated 2025-09-25T16:41:28Z. Arthur's first PN comment is 20:35:48Z the same day.
- Test 2 for all three local-timer ZOM asks rests on hearsay. Arthur never comments on those tickets.

**Smallest fix:** move the comment to Sep 26 and update ZOM-483's updated_at to match.

### F5. MINOR: answer-key and templated wording in the seeded comments

- Three bug tickets carry the same defensive line: "infinite lives themselves are live, this only breaks…", "the gift streak itself is live, this only breaks…", "teams are live on prod, this one is only…". Nobody volunteers that on a bug ticket, and it appears only on rows that pass test 1.
- Similar statements sit on DES-321, DES-322 and DES-339, and none on the Drop rows.
- The asks also repeat one pattern: "separate from the X, this is for players…".
- DES-319 "Daily is fine for this one, there's always a race on." answers nothing visible on the ticket. It reads as a pre-emptive test 5 ruling, although the warehouse's back-to-back 5-day race windows do support it.
- DES-338 "This is the chest itself, not the calendar refresh on DES-322." reads the same way.

**Smallest fix:** vary two of the three "itself is live" lines. Give the DES-319 line an antecedent, such as Vincent noting "it fires every day, not just at the start".

### F6. MINOR: PUSH_NOTIFICATION_STATS still shows Zombie Match Firebase pushes

- Table 6 has 25 Zombie Match rows, provider firebase, through 2025-09-27. Campaigns: new_levels, comeback_7d, daily_reward, event_live, sale_weekend.
- #zombie-bugs Sep 18: "All our PNs are local".
- This table was already the rev4 failure. The DM's "the client schedules" scoping handles the note, and I found no call that moves, because every test is about the client.
- DES-341 stays Hold (test 2) even with a server-sent new_levels campaign in the warehouse, since that is a server send.
- The residual exposure is the DM and prompt opener "what we actually say to players", plus the overlap with DES-341, DES-338 and DES-317.

**Smallest fix:** cut or narrow that opener if you want zero exposure. Otherwise leave it.

### F7. MINOR: Vincent's retraction sits under an unrelated parent

- The reply 4a5ee025… is threaded under Samuel's "could you help me test the build? Android 2007", which is a UI build request.
- "also on the race one I passed" has no antecedent there. It only makes sense if the reader knows it was placed to be hidden. It is persona-visible and clear once read.
- Brian's Sep 26 "just send all the Ready ones" is a similar cold post in #zombie-match3d. That one is harmless.

**Smallest fix:** add one line earlier in that DM about the message checks, or thread it under something related.

### Notes (no action needed)

- **F8.** The DM says "a ticket or a card", but no ZM ROADMAP card carries an ask. An empty result, not a fork.
- **F9.** Leonard's card comment "The beta list goes on this card" collides with the rule's "BETA list of the ZM ROADMAP board". Context separates them.
- **F10.** ZM has a live win-streak mechanic, so Streak Fever could look live. Confluence Live-Ops Event Calendar lists Streak Fever, Nathan's Treasure Hunt and Axe Arena under Domino Delights only, and calls itself the single source of truth. LIVE_EVENT_PERFORMANCE agrees.
- **F11.** ENG-2311 (Apr 2025, Done) and DES-9 (2023) are PN asks on tickets, but they are DD-era. The DM's Zombie Match framing leaves them out of scope.
- **F12.** Arthur's "the chest timer is local" sits next to a backend /api/daily-reward. No call moves, because he is the only source on test 2.
- **F13.** ENG-2363 and similar old tickets match the PN search terms but are not asks.
- **F14.** Injected rename at 2025-09-30T18:26:14Z is later than the board's dateLastActivity of 17:09:07Z.
- **F15.** Small bookkeeping points: rev_7 (20:58Z) predates rev_6 (21:23Z), and Vincent's email exists only in his and Samuel's mailboxes, not Oliver's or Owen's.

### Checked against the base and clean

- Builds: Android 0.3.127 and iOS 0.3.40 are the required versions from Sep 23, and 0.3.49 was released Sep 29 at 21:55Z.
- PR #248: approved and merged 21:23Z, after the injected 20:58Z review.
- Code: leaderboard batch counts from the reference date, four-week lapsed batch, FirstTutorialFinished gate, and NotificationManager enabling only through the ask or the toggle all match the seeded claims. Arthur's Unity-popup reply fits the code.
- Permission ask: level 20 matches PR #327 and the Aug 13 Samuel and Brian DM.
- Trello: card 53, 9 and 73 positions, reopen action on card 7, and the "BETA: Sep 30" name on Sep 29 actions.
- Collect & Win windows and the alias: Confluence.
- Boss Arena daily entries and weekly board: #zombie-ops Sep 1.
- Endless weekly rewards, and Plague Race windows running back to back.
- Calendar: no conflicts on Sep 26 or Sep 30. Gmail thread 1836006988541924555 exists.
- Persona visibility: every deciding record is readable by Samuel.
- D1/D7: USER_COHORT_RETENTION is the only Zombie Match retention source. DAILY_ACTIVE_USERS excludes it by design and DAILY_METRICS_AGG has no retention columns.

## 3. Could not check

- **Repo blobs:** the helper can't read them. I used the match3d NotificationManager.cs text in the shared scratchpad (nm.txt, from a run's github_get_file_contents, 21,075 bytes matching the base listing) plus the PR #248 hunks.
- **Warehouse dumps:** Snowflake aggregates for tables 18, 27, 28 and 35 came from raw dumps in that scratchpad. I confirmed tables 6 and 10 and row 27/45129 through the helper.
- **Not scanned:** RESOURCE_FLOW_EVENTS and VIRTUAL_CURRENCY_LEDGER for hourly grants. DESIGN_EVENTS, a 1:64 sample of the same grant stream, shows zero Zombie Match hourly_collect.
- **Other limits:** no full Gmail sweep, only targeted queries. Several broad Slack terms hit their limit, so those are not proof of absence. I did not read the ZM GDD docs or check Pop-up Offers against the warehouse.
