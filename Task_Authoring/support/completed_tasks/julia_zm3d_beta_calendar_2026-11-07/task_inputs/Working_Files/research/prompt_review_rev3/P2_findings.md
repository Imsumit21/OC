# Deep Recheck — Pass P2 (Services, data and access)

Task: Julia Lawson (Product Manager), ZM3D beta live-ops and push calendar. Universe: Oct 1, 2025 (synth-cut). Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC).
Topics checked: Cross-Service Coherence, Feasibility, Persona access, Data exists, Tool use and cross-service (hidden records, derived columns, open-instruction scope, date-slip severity).

## Coverage

- Prompt: 6 of 6 sentences checked.
- Incorporated sources: Frederick's DM ask (5 sentences) and his thread reply (5), the working-rules brief (26 sentences plus title and byline), the UA plan deck (3 slides), the PNs Beta tab (14 data rows), PN BETA Translated tab (header and 12 rows), Robert's approval and reversal, Vincent's re-test, Brian's two emails, the Oct 8 release event, and every GitHub, Linear and Trello note the SQL adds.
- Injected records checked: 112 of 112 SQL statements (78 INSERT, 34 UPDATE). Each was checked against the base record it sits on: parent Slack messages, Slack reply counts and latest_reply, channel membership, PR state, merge time, review and timeline conventions, Linear state, dates and children, Trello card badges, Gmail threading and mailbox ids, GCal calendars, Drive parents and shares, and Docs style offsets.
- Base records opened for comparison: Confluence `page_liveops_calendar`, `page_season_pass_spec`, `page_live_ops_engine` and `page_zm3d_gdd`; Snowflake `LIVE_OPS.EVENTS.LIVE_EVENT_PERFORMANCE` (529 rows) and `PUSH_NOTIFICATION_STATS` (25 ZM3D rows); match3d-backend `zombies-game-cdk/lib/zombies-game-cdk-stack.ts` and its git log; match3d-quests `lib/quests-stack.ts`; #builds submission posts; the push spreadsheet `f_a325dd4af80afc5994d5dc`.

## Findings (one line each)

| DR# | Pass | Checklist section | Quote | Record | Dimension / issue | Proposed severity |
|---|---|---|---|---|---|---|
| DR1 | P2 | §3 two services / §3.2 State-Lifecycle | "Every beat players can see ... what still has to land before it runs and who owns that" (Frederick DM, incorporated) | github data.json `/pull_requests` match3d#370, #438, #454 (merged Aug 13 / Sep 15 / Sep 19) vs injected rc_1, rc_74, c_4 dated 2025-09-30 | Cross-Service Coherence — State / Lifecycle | Fail-level |
| DR2 | P2 | §3.2 State-Lifecycle | "Not what already shipped" (brief, Still to do) | linear data.json `/issues` ZOM-565, ZOM-471, ZOM-432 (state Todo, started_at null) vs injected comments and the PR #471 c_18 note | Cross-Service Coherence — State / Lifecycle | Fail-level |
| DR3 | P2 | §3.2 Cross-service referential; derived/synthetic Snowflake | "Every beat players can see in those weeks: which windows it runs in" (Frederick DM) | Snowflake `LIVE_EVENT_PERFORMANCE` Plague Race rows (5-day runs) vs CDK `PLAGUE_RACE_SCHEDULE` "0 0 * * *" and #zombie-ops 2025-06-18 "Plague Race: every day at 00:00 AM UTC" | Cross-Service Coherence — Cross-service Referential | Fail-level |
| DR4 | P2 | §3.2 Semantic / Other | "A one-off may take a recurring beat slot only with Product latest dated approval, and if he takes that back his later word is the one that counts." (brief) | SQL L17 Slack `58d06bd55ea4129eaadb726291967d5a` threaded under base `c54310280ca0915181508d6e9b964926` (D05GU6L0XFH/2025-09.json) | Cross-Service Coherence — Semantic / Other | Minor |
| DR5 | P2 | §3.2 Identifier / Format | "Every config a beat needs lands before its lock ... A committed date that misses the lock moves earlier and its owner is told." (brief) | SQL L57–81 Gmail thread `.../1844835127305531392` ("Re:", In-Reply-To the Sep 22 message in thread `.../1844470925517303296`) | Cross-Service Coherence — Identifier / Format | Minor |
| DR6 | P2 | §3.2 Identifier / Format | (supports DR1 records) | SQL L142, L150, L158 timeline `commented` events for reviews vs base `reviewed` convention | Cross-Service Coherence — Identifier / Format | Minor (advisory) |
| DR7 | P2 | §3.2 Confluence vs code | "Every config a beat needs lands before its lock, read in server time (UTC)." (brief) | Confluence `page_liveops_calendar` "hourly ... IMPORT_REWARDS_SCHEDULE defaults to 0 * * * *" vs CDK `IMPORT_REWARDS_SCHEDULE ... "*/5 * * * *"` (known card SC-62) | Cross-Service Coherence — Cross-service Referential | Minor (advisory) |

Note on scoring: under Eval 1 §3.2 only one single low-impact inconsistency qualifies for NON-FAIL. DR4–DR7 are each low-impact, but there are four of them. DR1 and DR2 are State / Lifecycle items, which §3.2 says always fail.

---

## DR1 — Merged PRs get "still missing / needs to move" notes 11–48 days after merge

- **Quote (incorporated source, Frederick DM `8b090dec472117f4598b9ad84318272e`):** "what still has to land before it runs and who owns that". **Brief:** "For each beat, what still has to land before it runs for bought users (prod deploy, config, player-facing art an owner has flagged) and who owns it."
- **Base side:** `Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json` `/pull_requests`:
  - `harmonygames-Games/match3d#370` "Collect&Win Items", `state: closed`, `merged: true`, `merged_at: 2025-08-13T16:12:18Z`, `updated_at: 2025-08-13T16:12:18Z`, 0 reviews.
  - `harmonygames-Games/match3d#438` "Feature/season pass", `merged_at: 2025-09-15T23:09:34Z`, last timeline event `head_ref_deleted` 2025-09-15T23:17:40Z.
  - `harmonygames-Games/match3d#454` "Marcus/animated icons", `merged_at: 2025-09-19T17:50:52Z`.
  - Across every repo in the base export, no review, review comment or PR comment lands more than 0.26 days (about 6 h) after its PR's `merged_at`; none lands more than 1 day after.
- **Injected side:**
  - SQL L146–152: review `#370#rev_1` and review comment `#370#rc_1`, 2025-09-30T19:48:33Z: "The final vial sprites are still missing for the Collect & Win set — Claire has those on her list."
  - SQL L154–160: `#438#rc_74`, 2025-09-30T20:41:17Z: "The Season Pass premium strip needs to move to the November range rather than the current one — Oliver is taking the date change."
  - SQL L162–166: `#454#c_4`, 2025-09-30T18:05:52Z: "The Collect & Win event icon animation is still to do on my side — the other menu icons in this PR are finished."
  - Plus `UPDATE github.github_pull_requests SET updated_at = '2025-09-30…'` on all three merged PRs.
- **Inconsistency:** these are closed (merged) records with later activity that says the PR's own scope is incomplete. That is §3.2's defining State / Lifecycle example ("a closed ticket with later activity"). Each note carries a graded still-to-do and owner (Claire, Oliver, Marcus). The 48-day, 15-day and 11-day gaps fall far outside the base pattern. The injected #470 (13 min after merge) and #471 (5 h 15 m after merge) notes fall inside the base pattern and are not part of this finding.
- **Section / category:** Phase 3.2, State / Lifecycle Inconsistency (Cross-Service Coherence).
- **Severity:** fail-level (§3.2: a State / Lifecycle inconsistency always fails).
- **Fix:** carry these three owner flags on records that are still open: the matching open Linear tickets, or Slack posts in channels Julia belongs to (#zombie-art C08R8CHB0QL, #zombie-match3d C0880U9751A). Alternatively, attach them to PRs merged within hours of the note. Drop the `updated_at` bumps on #370, #438 and #454. If Marcus's C&W icon note moves to a Linear ticket, check it against his 2025-09-26 ZOM-465 comment ("every event icon animates at idle now"). Right now that comment is reconcilable only because C&W PR #468 merged later, on 2025-09-29.

## DR2 — Linear tickets left Todo (never started) while their own notes say the work is in, live or closable

- **Quote (brief, Still to do):** "Not what already shipped, not analytics, not polish nobody flagged."
- **Base side** (`Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json` `/issues`; base Linear has 0 comments):
  - ZOM-565 "Endless Horde Start Screen Vfx": `state_id: Todo`, `started_at: null`, assignee calvin.price.
  - ZOM-471 "Add red dot icon for players not in Plague Race": `state_id: Todo`, `started_at: null`.
  - ZOM-432 "Daily gift artwork needs to have the frame": `state_id: Todo`, `started_at: null`.
- **Injected side:**
  - SQL L203 `cmt_zom565_1` (2025-09-29, Marcus): "The endless start screen vfx is in (commit f7e971b0). Claim button glow and the new bar are both live now, can close." (Commit f7e971b0 exists in `/commits`, authored by Marcus 2025-09-25.)
  - SQL L236 `cmt_zom471_1` (2025-09-17, Samuel): "Red dot asset is ready and wired to the Plague Race state check".
  - SQL L219 `cmt_zom432_1` (2025-09-24, Calvin): "Card back and gift box are done, the frame is the last piece on my side". SQL L168 PR `#471#c_18` (2025-09-30, Samuel): "The daily-gift frame went out with this PR — it is in both submission builds from today, iOS 50 and Android 135, so nothing is left on it and that one can be closed."
  - Weaker cases of the same pattern: ZOM-344 (Todo, "Art side is signed off on my end"), ZOM-566 and ZOM-387 (Todo with in-progress notes), and ZOM-542 (`Regression` with "Regression pass on the mode switch looks clean").
- **Inconsistency:** the status ("Todo", never started) contradicts the record's own activity and a related record. This is the known SC-16 pattern ("Linear tickets still open after work shipped", 11 FAILs). The injection adds new instances, and the answer depends on them: shipped items must be kept out of "still to do".
- **Section / category:** Phase 3.2, State / Lifecycle Inconsistency.
- **Severity:** fail-level (§3.2 "always fails").
- **Fix:** keep the shipped-but-not-closed trap without the contradiction. Move ZOM-565, ZOM-471 and ZOM-432 to an open state that fits finished-but-unclosed work (In Review or In Progress, with a `started_at` on or before the first injected note and no `completed_at`, which avoids SC-32). Or change the notes so they don't claim the work is live.

## DR3 — Plague Race cadence: Snowflake 5-day runs vs prod config and Slack "every day at 00:00 UTC"

- **Quote (Frederick DM):** "Every beat players can see in those weeks: which windows it runs in". **Brief:** "Every window is stated in server time (UTC) as a start-end instant." Arthur's injected #470 note (SQL L140): "The Plague Race, leagues, Endless and Season Pass schedules are already running on prod."
- **Side A, Snowflake (synthetic):** `snowflake.json` `/tables/18` `LIVE_OPS.EVENTS.LIVE_EVENT_PERFORMANCE`. There are 20 ZM3D Plague Race rows, all back-to-back 5-day runs from 2025-06-19. The last two: EVT-0502 `start_date 2025-09-17`, `end_date 2025-09-21`; EVT-0514 `2025-09-22` to `2025-09-26`. The same table records real event windows elsewhere: DD Win & Collect rows are Mon 2-day (52), Wed 2-day (52) and Fri 3-day (51), and Weekly Leaderboards are Mon 7-day (39).
- **Side B, code and Slack:** `github/root/harmonygames-Games/match3d-backend/zombies-game-cdk/lib/zombies-game-cdk-stack.ts` L140–143: "// Plague Race event schedule // PROD: every day at 00:00 AM UTC … PLAGUE_RACE_SCHEDULE: props.production ? "0 0 * * *"". This has been unchanged in git since 2025-06. Slack #zombie-ops `C08R6BF4ENN/2025-06.json /298` (2025-06-18, Julia is a member): "currently `PROD` schedules are: Weekly leagues: every monday at 00:00 AM UTC / Plague Race: every day at 00:00 AM UTC". #zombie-bugs `C08R27X0EAH/2025-08.json /805` (2025-08-29, Vincent): "plague race didn't refresh daily either - it shows yesterday's race with ended text".
- **Inconsistency:** the same fact, Plague Race's prod window, differs across services. From Snowflake, Oct 6–Nov 2 gives 5-day windows (Oct 2–6, Oct 7–11, …, Nov 1–5). From the code and Slack it gives daily 00:00 UTC windows. Confluence `page_liveops_calendar` only says "Recurring" and settles nothing. This is not one of the FD-3785 rollups, so no PLATFORM tag applies.
- **Section / category:** Phase 3.2, Cross-service Referential Inconsistency (synthetic Snowflake in task-touched data). Date-slip rule: it changes a window the answer uses.
- **Severity:** fail-level for Cross-Service Coherence. It also opens a Plague Race window fork for P1/UGT to settle.
- **Fix:** make the Plague Race cadence agree across records, or point the solver at one source. Name in the brief (or a seeded record) where windows are read from (the prod schedule in the backend stack), and make sure no record presents the Snowflake 5-day runs as the prod window. Otherwise grading must accept both readings.

## DR4 — Robert's Halloween reversal is threaded under an unrelated DM message

- **Quote (brief, One-offs):** "A one-off may take a recurring beat slot only with Product latest dated approval, and if he takes that back his later word is the one that counts." (Confluence `page_season_pass_spec`: "Owner: Robert (Product)", so "Product" = Robert is consistent.)
- **Base side:** `slack/messages/D05GU6L0XFH/2025-09.json`, id `c54310280ca0915181508d6e9b964926` (2025-09-30T16:05:50Z, Robert): "How do you think we should make the game catered to more hardcore players? Obviously some level optimization, but aside from that". The conversation continues top-level, through Robert's 2025-10-01T03:32Z message in 2025-10.json.
- **Injected side:** SQL L17, `58d06bd55ea4129eaadb726291967d5a` (2025-09-30T22:10Z, Robert), `thread_parent_id = c54310280ca0915181508d6e9b964926`: "Coming back on the Halloween one-off: pulling my ok. Take it off the beta calendar…". The approval it reverses is in #zombie-art under the Halloween thread `9025d428af1f551a20e303c3acbc545b` ("*Halloween theme* for an app icon or an event"), SQL L15.
- **Inconsistency:** the reply's thread link points at a parent on an unrelated topic. The graded value (Halloween off) is unchanged, and the message is still findable by search.
- **Section / category:** Phase 3.2, Semantic / Other.
- **Severity:** minor (low impact).
- **Fix:** post the reversal as a top-level DM message (thread fields null), or as a second reply in the #zombie-art Halloween thread `9025d428…` (then raise that parent's `reply_count` to 2). Revert the parent `c5431028…` update.

## DR5 — Brian's correction is a "Re:" reply placed in a separate Gmail thread; snippet differs from body

- **Quote (brief, Config locks):** "Every config a beat needs lands before its lock, read in server time (UTC). A committed date that misses the lock moves earlier and its owner is told."
- **Injected side:** SQL L57–81, thread `<mailbox>/1844835127305531392`, subject "Re: ZM3D Season Pass November config handoff", headers `In-Reply-To` / `References` = `<CAH4q9Zb2fK7xQe1M8sPnL3vT6wR0yDc@mail.gmail.com>`. That is the Sep 22 message, which sits in thread `<mailbox>/1844470925517303296` (SQL L24–55). `X-GM-THRID` 1844835127305531392 differs from the parent's 1844470925517303296. The snippet reads "Julia, Correction to my Sep 22 mail: the November Season Pass config handoff moves…", but the body reads "Correction to my Sep 22 mail, Frederick in copy: the November Season Pass config handoff moves…".
- **Base side:** in a 1-in-10 sample of base thread files (8,141 files, 1,313 replies), 877 of 878 replies whose parent was found sit in the parent's thread. The one exception is an "Automatic reply".
- **Inconsistency:** a reply that names its parent sits outside the parent's thread, which breaks the export's threading convention. Reading the Sep 22 thread alone shows only the superseded Oct 29 date. The value is still reachable by search, so the graded value is unchanged.
- **Section / category:** Phase 3.2, Identifier / Uniqueness / Format (plus Other: snippet vs body).
- **Severity:** minor.
- **Fix:** put the Sep 26 message into thread `…/1844470925517303296` in all three mailboxes (X-GM-THRID 1844470925517303296), drop the second `gmail_threads` rows, and make the snippet the first characters of the body.

## DR6 — Injected review timeline events use a type base never uses for reviews

- **Injected side:** SQL L142 `#470#ev_9`, L150 `#370#ev_5` and L158 `#438#ev_9`: `event 'commented'`, `actor_login EMPLOYEE_0025_GITHUB_USERNAME`, each at the second its COMMENTED review was submitted.
- **Base side:** `github/data.json` `/timeline_events` has 2,116 `reviewed` events, all with no actor. 0 `commented` events coincide with a review submission (base `commented` events are issue comments).
- **Category / severity:** Identifier / Format; minor, advisory (the answer never reads it).
- **Fix:** use `event 'reviewed'` with a null actor for the three review events. Keep `commented` for the two PR comments (#454 ev_6, #471 ev_8).

## DR7 — Confluence live-ops calendar vs CDK on reward-import cadence (known SC-62)

- **Side A:** Confluence `page_liveops_calendar` (updated 2025-09-29): "There is no technical content lock. Reward tables are re-imported from Google Sheets hourly in production (IMPORT_REWARDS_SCHEDULE defaults to 0 * * * *)… The 24h season-pass freeze in the Season Pass spec is a process control on top of that".
- **Side B:** `zombies-game-cdk-stack.ts`: "// PROD: every hour … IMPORT_REWARDS_SCHEDULE: props.production ? "*/5 * * * *"".
- **Inconsistency:** a task-touched Confluence page (it supplies the C&W windows, Zombie Lane and the lock rule) disagrees with the code. This is base data, listed as known card SC-62. It doesn't change a graded value, because the lock the answer uses is the spec's "locked 24h before each season opens".
- **Category / severity:** Cross-service Referential; minor, advisory.
- **Fix:** none needed in the task. Keep any graded fact off the import cadence.

---

## Topic lines

- **Two services (§3):** no finding. GCal (release `2025-10-08 15:00:00+00` on Julia's calendar `evt_5c1e83a7d94b02f6c8e31a`) changes C&W's first window: the Wed-Thu window is pre-empted, so the first window is Fri Oct 10 00:00 UTC. Gmail (Brian's revised handoff "Fri Oct 31, 10:00 Istanbul time" = 07:00 UTC) sits against the spec's lock ("locked 24h before each season opens", so Oct 31 00:00 UTC) and changes the config result. Slack (Robert's reversal, Vincent's re-test), Sheets (PNs Beta Ready/LIVE columns), GitHub, Linear, Trello and Confluence each change at least one graded fact too.
- **Hidden record (§3):** no finding. Julia (`EMPLOYEE_0005_SLACK_ID`) is a member of D05SD5QLG94, D05GU6L0XFH, #zombie-art (joined 2025-05-06), #zombie-match3d (joined 2025-01-12), #builds, #zombie-ops and #zombie-bugs, with no `channel_leave`. Every injected Slack author is a member of its channel. Brian's mails exist in Brian's SENT and Julia's and Frederick's INBOX, under base mailbox ids. The release event is on all four attendee calendars. The brief and deck are shared with Julia as reader. The calendar sheet is Julia's own, in Julia's root folder `d_8140f09bf9f1b94cb8ee2d`. The push sheet `f_a325dd4af80afc5994d5dc` is shared with Julia. Julia is not a member of #zombie-prs (C093LEZGF6J), but its five injected bot mirrors duplicate GitHub notes the Agent can read unscoped (`github_get_pull_request_reviews`, `github_get_pull_request_comments`, `github_get_issue_comments`). They are not required, so this is not a hidden-record defect. The private Plague Race design doc `f_5666e4f65022f54fe1d0a0` is not needed.
- **Feasibility / tool use:** no finding. Writes: `gsheets_values_update` / `gsheets_values_append` (Julia owns the sheet), `linear_create_comment` / `linear_update_issue` with `links` (ZOM-78 and ZOM-429 exist), and `slack_send_message` with `thread_ts` in D05SD5QLG94. Reads: `gdocs_get_document_text`, `gdrive_read_sheet_range`, `gmail_search_messages`, `gcal_list_events`, `github_get_file_contents` and the PR review/comment tools, `linear_list_comments`, `trello_get_card_actions`, `confluence_get_page`. Breakdowns: the Calendar tab (Beat … Still to do (owner)) and the Pushes tab (Beat … Notes) each have backing fields. PNs Beta has both "Status" (Ready / Not Ready) and "Status (NA, WIP, LIVE)", plus Headline and Body for the naming rule.
- **Open-instruction scope:** no finding. The open sets are bounded: the PNs Beta plan is 15 rows minus the 4 named exclusions = 11, and the beats are fewer than 15.
- **Persona access (ACL):** no finding. No required read is outside Julia's scope, and no ask directs a read of another person's private data.
- **Data exists:** no finding, apart from the DR3 cadence conflict. C&W "three staggered windows (Mon-Tue, Wed-Thu, Fri-Sun)" (Confluence and CDK `WIN_AND_COLLECT_GROUP_1..3`). Season Pass "reset monthly on the 1st at 00:00 UTC" (spec and CDK `"0 0 1 * *"`). Leagues `"0 0 * * 1"`. Endless daily 00:00 and weekly Monday 00:00. Weekly quest reset `weekDay: 'MON'` (match3d-quests `lib/quests-stack.ts` L426–433), which matches the Trello "Mon Oct 13 rollover". Zombie Lane "Permanent". The translated tab is the Domino Adventures set, as the brief says. Submission builds "iOS Submission - #50" and "Android Submission - #135" were both built Sep 30 in #builds. The brief's change-request hold rule has no Aug–Sep match: the only match3d CHANGES_REQUESTED review is #303 on 2025-07-16, outside the cohort, so it is a valid exclusion.
- **Derived columns (Snowflake):** no finding. `LIVE_EVENT_PERFORMANCE.completion_rate_pct` recomputed as completions / participants × 100: all 21 ZM3D rows match (EVT-0527 Season Pass 20/61 = 32.8). 18 DD rows differ only by x.x5 half-up rounding (EVT-0008 5/16 = 31.25 → 31.3). `PUSH_NOTIFICATION_STATS` has no derived columns. No FD-3785 table is used.
- **Date slips:** no finding. Every weekday and date pair checks out: Mon Oct 6, Sun Oct 12, Mon Oct 13, Sun Oct 19, Mon Oct 20, Sun Oct 26, Mon Oct 27, Sun Nov 2, Wed Oct 29, Fri Oct 31, Sat Nov 1, Wed Oct 8. Istanbul conversions are UTC+3: 18:00–19:00 = 15:00–16:00Z and 10:00 = 07:00Z (Brian's calendar `time_zone: UTC+03:00`). Every injected `updated_at` / `dateLastActivity` / `latest_reply` is later than the base value it replaces. All Slack ts values fall Sep 18–30, before the clock.

## Checked and consistent (no finding)

- ZOM-521 description untick (SQL L246–253) matches its open children ZOM-526 and ZOM-528 (In Progress), and the ticked items' children ZOM-523/524/525/527 are Done. This resolves known card SC-15 rather than adding to it.
- Slack #zombie-prs parents: base reply_count 16/2/78/3/7 → injected 17/3/79/4/8. Each new `latest_reply` is later than the existing last reply, and each thread_ts matches.
- Trello card `6851a724601a61857a1b202f`: comments badge 1 → 2. Card and badge `dueComplete` agree. Creator `d1cd0fef645a6c978ae1f068` = Brian Foster (base uses both hex and token ids).
- Docs `style_runs_json` offsets match all 8 headings and the title in the brief body.
- Injected GitHub review-comment paths exist in match3d (git history ties `Collect&Win Item Potion Medium Blue2.prefab` to "Collect&Win Items" 2025-08-08). All injected GitHub, GCal and Drive ids are free in base.
- PR #471's commits include "Fixing UI Elements on Daily Gift" (2025-09-27), which supports Samuel's frame note. Android #135's change list shows it; iOS #50's list shows only "Bump max level for debug menu" (base change-list gap, advisory).
- Marcus's 2025-09-26 ZOM-465 note vs his 2025-09-30 #454 note reconcile because the C&W feature (PR #468) merged 2025-09-29.
- SC-6 (Node CEO mail from brian.foster@) does not reach Julia: her mailbox has 0 Brian-sent base messages.
- `PUSH_NOTIFICATION_STATS` ZM3D rows are historical weekly campaigns that don't map to the PNs Beta rows, and the brief routes push status through the sheet (advisory only).

Platform defects: none. FD-2880 applies only incidentally: match3d-backend git history runs to 2025-09-29 while `/commits` stops at 2025-08-13, and no finding depends on it.
