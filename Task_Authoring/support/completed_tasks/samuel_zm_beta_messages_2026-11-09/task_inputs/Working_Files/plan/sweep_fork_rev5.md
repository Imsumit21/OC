# Fork sweep, rev5 (independent, adversarial)

Task: samuel_zm_beta (task_inputsK). Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut).
Inputs read: 04_Prompt.txt, 01_Universe_Inject.sql (as text), universe through hg.py only.

## Verdict

No FATAL found. Three MINOR findings and one evidence limit that needs closing.

| # | Finding | Severity |
|---|---|---|
| F1 | DES-346 Rewarded ad: warehouse shows ZM rewarded video live, which hits the first prong of "in the beta" | MINOR (highest priority) |
| F2 | PUSH_NOTIFICATION_STATS shows ZM Firebase campaigns, including `new_levels`, against the "needs a server send" rows | MINOR (no content change) |
| F3 | Note, lapsed section: a code comment labels Weekly Rankings a "Lapsed Weekly reminder batch" | MINOR (low) |
| F4 | String ticket has no stated state or assignee | MINOR, only if a rubric grades it |
| L1 | Current `NotificationManager.cs` is unreadable through hg.py, so sections 2 and 3 rest on the PR #248 diff | Evidence limit |

My independent counts: **3 Go, 25 Hold, 7 Drop** (35 rows).

## 1. What the deliverables must contain

- Sheet (Samuel's Drive folder `d_caafeec2804b3a67ce46aa`), one row per message: Message, Ticket, Call, What's missing, Audience, Final headline, String change.
- Note: (a) D1 and D7 for the Sep 15 cohort week, iOS and Android separately; (b) lapsed reminders the client schedules, day by day; (c) anything the client already schedules that is still a Hold, and why.
- Tickets: a call comment on each ticket. Drop to Canceled, Go unchanged, Hold to Backlog and unassigned (rule doc "unless the roadmap says otherwise" plus Leonard's Trello comment, SQL L53).
- New tickets: 2 asks with no ticket (comments on ZOM-542 L294 and ZOM-556 L296) and 1 string ticket under DES-314 for Lapsed 7 days. No new ticket for Win & Collect: DES-313 already covers it.
- Checklist on `[Feature] Push Notifications - Samuel + Leonard`: the 3 Go rows.
- Emails: Calvin, Brian, Robert, Oliver, Julia, Owen, Martin (7). Leonard is excluded as "me".
- DM in D06L58XCVKK: counts.

## 2. The note, line by line

### Section (a): D1 and D7, Sep 15 cohort week. CLEAN

| Platform | Installs | D1 | D7 |
|---|---|---|---|
| Android | 103 | 37.86 | 10.68 |
| iOS | 237 | 31.65 | 9.28 |

- Source: `ANALYTICS.GAME_EVENTS.USER_COHORT_RETENTION` (snowflake.json `/tables/10/rows`), `cohort_week` 2025-09-15, `zombie_match_3d`.
- I recomputed it from `INSTALL_ATTRIBUTION` (`/tables/33`) and `PLAYER_DAILY_PROGRESS` (`/tables/7`): Android 39/103 and 11/103, iOS 75/237 and 22/237. Exact match, so there is no second warehouse answer.
- `domino_delights` has no cohort row from 2025-09-01 on. `DAILY_ACTIVE_USERS` excludes ZM by design.
- Grain is settled by the DM ("iOS and Android separately"), so pooling is not a fork.
- No competing Sep 15 figure surfaced in targeted searches: Docs "Sep 15 cohort" had 0 hits and Confluence had no ZM cohort figure in the hits read. Sheets has 5 numeric hits on 37.86 and 31.65 that I did not open. The Slack "D7" query hit its limit on noise, so Slack is not exhaustive here.
- Aside: the D14 recompute does not match the mart (0.97 vs 5.83, 3.8 vs 7.17). D14 is not asked for. Do not add it to any rubric.

### Section (b): lapsed reminders, day by day

Answer: **day 1** (The Horde Is Growing) and **days 7, 14, 21, 28** (They've Taken Over, four repeats).

- `DailyNotifications`: `serverToday.AddDays(1)`. `BatchScheduleWeeklyNotifications(..., 4, serverToday)`: `referenceDate.AddDays(i * 7)` for i = 1..4 (PR #248 diff, review comments rc_10 and rc_18, SQL L81).
- Leonard's cancel note agrees: "The weekly one repeats for four weeks, so day 14 is already covered." (SQL L73).

Forks tested:
- Server `comeback_7d` winback (`/tables/6`, 5 ZM rows, audience `lapsed`, firebase): excluded by the words "the client schedules". CLEAN.
- Domino or rpg-prototype `NotificationManager.cs`: excluded by the ZM context and "Built in match3d #248". CLEAN.
- PN sheet shows only 1 and 7 days: the DM asks what the client schedules, so code decides. CLEAN.
- Weekly Rankings: see F3.

### Section (c): client-scheduled rows still on Hold

See section 3 below. One defensible answer.

## 3. Rows the client already schedules that are still a Hold

The client schedules six messages (`ScheduleDominoNotifications`, PR #248 diff): Lives recharged, Finish first mission, Lapsed 1, Lapsed 7 (weekly batch), Weekly Leaderboard reset, Plague Race. Go: Lives recharged, Lapsed 1, Lapsed 7. Hold:

| Row | Test failed | Evidence |
|---|---|---|
| DES-318 Finish first mission | 4 | Audience is new players below level 20 (L178). Gate is `GetCurrentLevelNumber() < FirstTutorialFinished`, value 20 (rc_6, review 2007). Our own ask stays after level 20 (Robert, L34). Nobody in the audience counts. |
| DES-320 Weekly Leaderboard reset | 5 | Arthur on PR #248: "it isn't a reset message until it's anchored to the real reset" (L81, Gmail L65). Unlock level 22, so test 4 passes. |
| DES-319 Plague Race | 6 | Vincent: "my iPhone pass was the 5-minute test build, not the store build. on the store build it never came through." (L41). QA note: shortened timers do not count (L59). |

The set has one defensible answer. Forks tested:

- **DES-318 iOS popup. CLEAN, settled explicitly.** Base `zombie-bugs` says the iOS prompt comes at launch (Vincent Sep 19 07:01, Leonard Sep 19 14:23 "Yeah PNs are at the beginning"). If that counted, test 4 would pass and the row could reach Go. Robert (L34) and Arthur's thread reply (L36, "that popup doesn't switch anything on") settle it, with the rule's "our own permission ask". The code agrees: `NotificationsEnabled` defaults false and scheduling returns early unless it is set.
- **DES-319 test 5 vs 6. CLEAN.** The sheet says Event Start; the code fires daily at 00:15 for 5 days. Leonard's "Daily is fine for this one, there's always a race on." (L186) settles it. Warehouse agrees: 20 back-to-back 5-day ZM runs with no gap through Sep 26 (`/tables/18`).
- **DES-344 Lapsed 14 days.** Scheduled under Lapsed 7, but a Drop, so it is outside this section. Rule text settles it.
- **DES-318 "scheduled but partly reachable".** The code schedules it, and Vincent saw it via settings, so test 3 passes and test 4 fails. Stop-at-first-fail settles it.
- **Other builds.** Vincent's check builds Android 0.3.127 and iOS 0.3.40 match the base required versions (`zombie-match3d`, Arthur, Sep 23). Newer builds exist (0.3.133, iOS 0.3.49), but the QA note requires a store build, not the latest. CLEAN.

## 4. Can warehouse data change a call or a What's missing value?

### F1. DES-346 Rewarded ad. MINOR, highest priority

- **Deliverable:** sheet row, ticket comment and state, Robert's email, DM counts.
- **Reading A (Drop, test 1):** not live and not on the BETA list. Counts 3/25/7, ticket to Canceled.
- **Reading B (Hold):** rule says "live in Zombie Match today **or** on the BETA list". The warehouse shows rewarded video live, so test 1 passes. Row becomes Hold, counts 3/26/6, ticket to Backlog. No Arthur comment exists on this ticket, so the failing test is not stated either.
- **Evidence for B:** `RAW_TELEMETRY.AD_IMPRESSION_EVENTS` (`/tables/27/rows`): 1,313 ZM `rewarded_video` rows in a 1:16 sample, 2025-04-16 to 2025-09-30, 356 of them in September across 153 players. Example ADIMP-00001663, placement `rewarded_continue`. match3d also has `Assets/Store/Ads/AppLovinMaxManager.cs`.
- **Evidence for A:** Leonard on DES-346 (L292): "I moved rewarded ads to Oct 21 on the roadmap, they aren't in the beta." Trello log: Rewarded Ads moved BETA: Sep 30 to Oct 21 on 2025-09-23. `MONETIZATION.AD_REVENUE` (`/tables/35`, 55,302 rows) has zero ZM rows and every ZM impression has revenue 0. The `company-internal` plan of Sep 12 lists "Rewarded ads surfaces" as work still to do.
- **Settled?** Yes, by a persona-visible record from the rule's owner on that ticket, using the rule's own term. But his sentence only addresses the roadmap prong; "not live" is inferred. The placement also differs: `rewarded_continue` is not the "watch for a bonus" surface the ask describes. That distinction is my inference.
- **Smallest fix:** make L292 close the first prong for the bonus surface, for example that the bonus ad isn't live and the card moved. Do not claim all rewarded ads are off, because the warehouse would contradict it.

### F2. Firebase campaigns vs the "needs a server send" rows. MINOR, no content change

- **Deliverable:** sheet rows DES-329, 333, 335, 340, 341 and their emails. DES-341 New levels added is the one that matches a campaign key.
- **Reading A:** Hold, test 2. Arthur: "needs a server send, nothing on the phone knows we shipped levels" (L274).
- **Reading B:** a server path exists and `new_levels` is already going out, so the block is not real.
- **Evidence for B:** `LIVE_OPS.EVENTS.PUSH_NOTIFICATION_STATS` (`/tables/6/rows`): 25 ZM rows, provider firebase, 5 each of `new_levels`, `comeback_7d`, `daily_reward`, `event_live`, `sale_weekend`. `new_levels`: PUSH-0000065 (May 10) through PUSH-0000105 (Sep 27, 278 sent).
- **Evidence against B:** Leonard, `zombie-bugs` Sep 18: "PNs don't talk to backend", "All our PNs are local" (Samuel is a member). ZM rows start 2025-04-12, before client push existed (PR #248 merged 2025-06-26). So the table conflicts with both the team and the code.
- **Settled?** Yes, by the literal rule. Test 2 reads "The client can send it without a server." A campaign proves a server sends it, not that the client can. All five rows stay Hold, test 2, under both readings. The Drop clause needs the *client* to cover it, so it does not apply either. Only prose changes.
- **Other campaign names:** `comeback_7d` vs DES-317 and DES-345; `daily_reward` vs DES-322 and DES-338; `event_live` vs the event rows. None changes a call: tests 1 to 3 are about the feature and the client.
- **Smallest fix:** none in the SQL. Keep OE and rubric text to "fails test 2". Never have them assert "we have no server push".

### Other warehouse checks. CLEAN

- **DES-324 Hourly Coins, Drop test 1.** `DESIGN_EVENTS` (`/tables/28`, all 18,654 rows read): `hourly_collect` 3,377 for Domino, 0 for ZM. No Hourly script in match3d. Trello: Hourly Collection moved to Backlog 2025-09-23.
- **DES-325, 326, 327.** `LIVE_EVENT_PERFORMANCE` has no ZM rows for them; no scripts in match3d; Axe Arena moved to Oct 21 on 2025-09-23 and Brian announced the postponement on `company-internal`, Sep 22.
- **Season Pass rows.** ZM run EVT-0527 (Sep 29 to 30) and the BETA list agree that test 1 passes.
- **DES-320 and DES-321.** The warehouse event table has no ZM Weekly Leaderboards or Weekly Quests rows. Absence is weak, though: match3d has `LiveOps/LeaderBoards/*`, DES-321 says Quests are in production, and Samuel's Sep 29 DM mentions both. Test 1 passes.

## 5. Other UGT and coherence checks

### F3. Lapsed section vs Weekly Rankings. MINOR (low)

- **Deliverable:** note section (b).
- **Reading A:** the two LAPSED messages only, days 1, 7, 14, 21, 28.
- **Reading B:** also Weekly Rankings Reset on days 7, 14, 21, 28. The PR #248 diff heads that string `// Lapsed Weekly reminder batch`, and Arthur says it counts from the day they last left.
- **Settled?** By inference: sheet Type `LAPSED` covers only two rows, the tickets are named Lapsed, and the comment is a copy-paste.
- **Smallest fix:** have the rubric grade the day list for the two lapsed messages and not penalise a mention of the leaderboard batch.

### F4. String ticket state. MINOR, only if graded

- **Deliverable:** the string ticket under DES-314.
- **Reading A:** Backlog or Todo. **Reading B:** Leonard's comment bars non-beta work from Todo, but a string change on a Go row is beta work.
- **Settled?** No. No record gives its state or assignee.
- **Smallest fix:** do not grade its state or assignee.

### Clean, one line each

- **Hold state:** L53 "Held work sits in Backlog, unassigned." Beta is not out: the BETA list reads Oct 10, and Leonard says mid October on Sep 25 (a DM Samuel cannot see).
- **Win & Collect ticket:** DES-313 under the name Collect & Win. Test 3.
- **Final headline:** only Lapsed 7 changes (L38, "Your Squad Needs You Back"). Targeted Slack searches found no competing call (Full Ammo, Rankings Reset, First Mission: 0 hits), and Sheets has Full Ammo only on the PN sheet. Docs were not searched for headlines. The client's swapped emoji on Finish first mission and Weekly Rankings do not matter: emoji don't count and both are Hold.
- **Hidden asks:** no other ZM ask found in Linear or the ZM ROADMAP board. Base Linear has no comments. ENG-2311 is a Domino ticket.
- **Card:** the only other push card, "local Push Notification", is on DD Product Roadmap. L50 settles which card.
- **Sheet:** the Domino file also has a PNs Beta tab; the prompt names Zombie Match. Samuel is on the share list.
- **"Me" in the DM:** Leonard, who wrote it. He filed DES-342 and 343, so he is the one excluded.

## 6. My calls, all 35 rows

**Go (3):** DES-315 Lives recharged, DES-316 Lapsed 1 day, DES-317 Lapsed 7 days (headline change, string ticket).

**Hold (25):**
- Test 2: DES-329, 333, 335, 340, 341.
- Test 3: DES-313, 321, 322, 323, 328, 330, 331, 332, 334, 336, 337, 338, 339, 342, 343, plus 2 new tickets (Boss Arena attempts refill, gift streak reset eve).
- Test 4: DES-318. Test 5: DES-320. Test 6: DES-319.

**Drop (7):**
- Test 1: DES-324, 325, 326, 327, 345, 346.
- Covered: DES-344, under Lapsed 7 days.

## 7. Verified vs inferred

**Verified by opening the record:** all warehouse tables cited (rows read in full for `/tables/5, 6, 7, 10, 18, 27, 28, 33, 35`); PNs Beta grid; ZM ROADMAP lists, cards, actions; Linear issues and users; PR #248, #251, #263, #292, #327 records and review text; the Slack messages quoted; Drive folder and sheet share list.

**Inferred:**
- Hourly Coins absent from ZM is based on a 1:64 sample plus file names.
- Script absence is based on file names only.
- The `rewarded_continue` vs bonus-surface distinction.
- That later commits did not change the schedule.

## 8. Evidence limits

- **L1. match3d `Assets/Scripts/Notifications/NotificationManager.cs` (21,075 bytes) cannot be read.** `hg.py search get` fails on non-JSON blobs. Sections (b) and (c) rest on PR #248 hunks, which end at the merge on 2025-06-26, plus Arthur's Sep 25 ticket comments. Commit messages after that concern permissions and the toggle, and there is one revert pair (400300963f, 496348928a). The agent has `github_get_file_contents`, so a reviewer will read the live file. **Before sealing, confirm in the live file** that the six schedule calls, `weeksToCover` 4, and `AddDays(1)` still stand.
- `NotificationPermissionRequester.cs` and `ZombieConstants.cs` were read only through review text.
- `RESOURCE_FLOW_EVENTS` (1.3M rows) and `RAW_EVENTS` could not be scanned: full-file scans and deep offsets timed out. So ZM `rewarded_video` or `hourly_collection` coin flows are unchecked. A hit on `rewarded_video` would strengthen F1 Reading B.
- Gmail searches were complete for the zero-hit terms; "Taken Over" stopped at its match limit after 57,716 of 81,404 files, and the hits read were unrelated.
- Slack searches covered 2025 by month patterns, and some queries hit their match limits.
