# Prompt Brief — julia-zm3d-beta-liveops-calendar · prep
> Built 2026-11-05 from 00_Task_Context.json, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 01_Scenario_Design.md, 01_Hardness_Manifest.json, solver/truth.json · Persona view verified: see §5a (PROMPT_persona_entity.md)
> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human.
> Revised 2026-11-06 for revision 2 (after the 2026-11-05 `/prompt` FAIL): SQL sha256 `3afbf7cbbdb7`, prompt sha256 `2a23afd87c4c`. The pinned state is now seven beats and ten push rows; the changes and their records are in the dossier §11 (Revision 2).
> Revision 3 (2026-11-06, after the second `/prompt` FAIL, on Cross-Service Coherence alone): the SQL is now sha256 `837d4f5dedbd`, 112 statements (78 INSERT, 34 UPDATE). Three Linear statements differ, on two tickets: a new, later note on `ZOM-526` with that issue's `updated_at`, and the `ZOM-521` description with two checklist items unticked (known-issue card SC-15, repaired; dossier §11, Revision 3). The prompt (sha256 `2a23afd87c4c`), the pinned state and the acceptance in this brief are unchanged.
> Revision 4 (2026-11-06, after an independent `/prompt` run on revision 3: Cross-Service Coherence 2, Clarity 3): the SQL is now sha256 `c955d6ca2bca`, 106 statements (75 INSERT, 31 UPDATE). The prompt (sha256 `2a23afd87c4c`) and every pinned value are unchanged. What moved is where three notes live (vial sprites `#468#rc_38`, premium strip `#473#c_2`, Collect & Win icon `cmt_zom465_2`), five ticket states (Done) and two (In Progress), the retraction's placement (a top-level DM message), the correction mail's threading, and three sentences of the brief plus the ask's wording; the rows below that name those records are corrected in place (dossier §11, Revision 4). The brief now says the config owner is told "in a reply on the mail where they committed to it", so the channel for telling Brian is no longer open.
> Revision 5 (2026-11-06, after an independent `/prompt` run on revision 4 and a claim-by-claim audit of every injected record): the SQL is now sha256 `3c035f2af029`, 96 statements (70 INSERT, 26 UPDATE). The prompt (sha256 `2a23afd87c4c`) is unchanged. Two pinned values change, by design: the Quests still-to-do is empty (the quest note, now Leonard's on the open quests card, says the current set carries the first week) and the Collect & Win vial item reads "the final vial models (Claire)". Daily Login's empty still-to-do now rests on one record, Samuel's closing note on ZOM-432 (`cmt_zom432_2`); nothing is seeded on #471. The five Slack messages people wrote and Brian's two mails have new ids, and this file cites the new ones. Three tickets revision 4 had closed are open again (ZOM-565, ZOM-471, ZOM-542) and ZOM-387 is exactly as base has it. Trello decides no graded value any more; the tenth weight-carrying service is Confluence (the 24 h lock on the Season Pass spec page). Details: dossier §11, Revision 5.
> Revisions 6 and 7 (2026-11-06, after independent rounds on revisions 5 and 6): the SQL is now sha256 `091722f6a281`, 98 statements (72 INSERT, 26 UPDATE). The prompt (sha256 `2a23afd87c4c`) and every pinned value are unchanged. The quest note now says more quests get added with the Mon Oct 13 rollover if they are ready and nothing in the beta waits on them, which settles the one fork the round on revision 5 failed Unique Ground Truth on. ZOM-526 has a third note and ZOM-521 a second one; neither decides a value. ZOM-387 is out of the cohort since revision 6, so the cohort is 41 and the call budget 193. Details: dossier §11, Revision 6 and Revision 7.
> Revision 8 (2026-11-06, after a fresh blind `/prompt` round on revision 7): the SQL is now sha256 `0e8c8ad83f3b`, 96 statements (71 INSERT, 25 UPDATE). The prompt (sha256 `2a23afd87c4c`) and every pinned value are unchanged; one evidence id moves. The premium-strip note is now an inline note under Arthur's approval of #472, before that merge (`#472#rc_1`; it was `#473#c_2`). The brief adds "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date." The quest note now says the rollover does not wait on the new quests. The per-PR conversation surface no longer counts, so the call budget is 154. Details: dossier §11, Revision 8.
> Revision 9 (2026-11-06, after the platform's third `/prompt` failure on Unique Ground Truth and Clarity): the SQL is now sha256 `892f7edda809`, 104 statements (76 INSERT, 28 UPDATE). The prompt (sha256 `2a23afd87c4c`) and every pinned value are unchanged. The brief's rules are closed: an established failure holds a beat and an unverified one does not, and still to do is a held beat's fix plus what has been flagged for that beat as not done since the brief (prod deploy, config or player-facing art), nothing else. The Collect & Win cadence moved to "Span and time base", Push copy lost "only" twice, and Robert's withdrawal now says "the themed prop set I okayed in Martin's thread". New records on ZOM-534, ZOM-566, ZOM-563 and in #zombie-bugs decide no value. Details: dossier §11, Revision 9.
> Revision 10 (2026-11-06, after a pre-review attack on revision 9): the SQL is now sha256 `ffbac4586fb9`, 107 statements (78 INSERT, 29 UPDATE). The prompt (sha256 `2a23afd87c4c`) is unchanged. Two pinned values change by design: Weekly Leagues' fix and Collect & Win's server windows name Douglas, and Quests and Daily Login read All four weeks under Weeks running. The still-to-do rule now reads "its fix if it is held, and anything flagged since this brief as still needed for it (prod deploy, config or player-facing art)", the "pre-empts" sentence is gone, and Push copy judges "the English copy on that row". New and re-worded records decide no value. Details: dossier §11, Revision 10.
> Revision 11 (2026-11-06, after the formal blind round on revision 10): the SQL is now sha256 `1348d287ac4a`, 110 statements (80 INSERT, 30 UPDATE). The prompt (sha256 `2a23afd87c4c`) is unchanged and so is every pinned value. One evidence id is added: `cmt_zom465_3` (Brian: the Collect & Win icon has to land). The brief gains the clip sentence, "closing 23:59 UTC on its last day", the held-row sentence, "Login Calendar on the push sheet, same beat" and "moves to any time before it". Details: dossier §11, Revision 11.
> Revision 12 (2026-11-06, after the verification round on revision 11): the SQL is now sha256 `b5ccbfa577fc`, 111 statements (81 INSERT, 30 UPDATE). The prompt (sha256 `2a23afd87c4c`) is unchanged. Three empty, ungraded cells are filled by design: Weekly Leagues' First window (Mon Oct 6 00:00 UTC) and Weeks running (All four weeks), and Season Pass's First window (Mon Oct 6 00:00 UTC). No other value and no evidence id moves. The brief states the 23:59 UTC close for every window and adds "windows and weeks", the shop sentence, "(Login Calendar and Weekly Rankings are fine)" and "what its row is missing". Details: dossier §11, Revision 12.
> Revision 13 (2026-11-06, after the cold reviewers' last items on revision 12): the SQL is now sha256 `1f2175a297fd`, 111 statements (81 INSERT, 30 UPDATE). The prompt (sha256 `2a23afd87c4c`) is unchanged, and so is every pinned value and evidence id. The brief now says "the rotating shop" and "with which of those its row is missing", and Arthur's vial note and Brian's ZOM-465 note say "before the event runs". Details: dossier §11, Revision 13.
> Revision 14 (2026-11-06, after the last cold P1 on revision 13): the SQL is now sha256 `edae63f3e838`, 111 statements (81 INSERT, 30 UPDATE). The prompt (sha256 `2a23afd87c4c`) is unchanged, and so is every pinned value and evidence id. The brief now says "you tell its owner in a reply on the mail where they committed to it" and "Endless goes down as its weekly windows, with the daily reset noted." Details: dossier §11, Revision 14.

Universe synth-cut (`hg4-synth-sep30cut`); Clock 2025-10-01 00:00 PT (07:00 UTC); seed bound `2025-10-01T00:00:00Z`;
`context_hash 4bbc727fd48ac35a16b4afeda5430937563f2ce969970841bb4f3f97b6a38a39`. Tier Long Horizon (extreme profile;
`call_budget` 154 in the revision-8 manifest (193 in revisions 6 and 7, 194 in revision 5, 192 in revision 4; 200 in revisions 2 and 3: the revision-1 figure of 208, plus the thread-open call, minus nine
reads that existed only for Zombie Lane); floor 130). This brief carries no prompt wording; it prepares the facts and
the acceptance.

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Product (→ `task_categories.md`: Product & Design) | Product decisions on a live-ops + push calendar: which beats run, what is held, what must still land. |
| Persona | Julia Lawson · `julia.lawson@harmonygames.co` · Product Manager, Product | She owns the ZM3D beta live-ops + push calendar; posts in 147 visible channels (last 2025-09-30); scoped reads are hers (her DMs, her mailbox, her ZM Live Ops Drive folder, her calendar copies). Remit: a PM coordinating the beta launch. |
| Competency | Marketing and GTM | A bought-user beta's engagement/retention beats (events, Season Pass, daily login, leagues) and its push-notification plan are GTM/retention work; the deliverable is the launch's live-ops schedule + push calendar + a recommendation. |
| Task skill | Planning and decision support | Build a four-week schedule from scattered readiness signals, decide run/hold per beat and send/hold per push, and recommend with tradeoffs — an authored plan, not a chat answer. |
| Task type | Long Horizon (extreme) | Weight across slack, gmail, gcal, gdocs, gsheets, gslides, github, linear and confluence (trello is injected and carries no weight since revision 5). Measured volume: a 41-member live-ops cohort since revision 6 (18 open ZOM issues + 23 decision-bearing PRs; 39-PR GitHub read surface; 42 / 19 / 23 / 39 in revision 5; 39 / 16 / 23 / 39 in revision 4, which had closed five tickets; 44 / 21 / 23 / 39 in revisions 2 and 3; 47 / 22 / 25 / 41 before Zombie Lane left the calendar), 2 handoff mails, 1 release event, 1 brief, 1 UA deck, 1 push sheet, 1 ask with 1 thread reply. `call_budget` 192 ≥ 130 floor. |

Remit argument: Frederick (GM / calendar owner) hands the beta calendar to Julia (her DM, §5). She owns the calendar
sheet and the ZM Live Ops folder (§5a). The seven beats and the push plan are the product surface a PM schedules; the
readiness signals live across engineering (PR reviews, Linear), QA (Slack), live-ops (Trello, mails) and the
calendar/release (GCal).

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Records the persona cannot see |
|---|---|---|---|
| The ZM3D closed beta opens Mon Oct 6 for four buy weeks and the live-ops + push calendar for those weeks is not built yet; Frederick asked Julia to put it together and send back a recommendation. | Julia (owns the calendar) | Frederick's DM ask `slack:D05SD5QLG94/1759263617.418209` (A1) and his thread reply under it `slack:D05SD5QLG94/1759263878.305129`; her empty calendar sheet `f_e4a17c90b3d25f6a8c1d73` (A2) in the `d_5f2c8e1b7a94d03c6e2b58` folder | the five `#zombie-prs` bot mirrors (public channel she is not a member of — §1.E dossier; non-load-bearing; PR evidence reads through unscoped GitHub) |

Third person, symptom only: the calendar is unbuilt and due before the beta opens. No line says which beats are held,
which pushes wait, or why — those are discovered.

## 3 · Investigation → action

Questions to resolve (no answers in the prompt; since revision 2 the prompt no longer lists these per-row fields
either, they are in Frederick's message):
- Which beats belong on the calendar (seven, from the brief's scope and Frederick's follow-up), and for each: does it
  run, in which windows, is anything held and until when, what still has to land before it runs and who owns that.
- Which push rows belong in the plan (ten, from Frederick's follow-up), and for each: does it go out or is it held,
  and if held, what is missing.
- The overall recommendation and the tradeoffs.

Writes those answers feed:
- Fill the Calendar tab (keyed by beat) and the Pushes tab (keyed by push) of Julia's live-ops calendar sheet.
- Reply to Frederick in his DM thread with the recommendation and tradeoffs.
- Link the finished sheet on the calendar ticket (ZOM-78).
- Note the weekly-leagues hold on its ticket (ZOM-429); it is the only held beat, so the only ticket note.
- Reply to Brian on his slip mail that the November config has to land before the lock (the brief: you tell the owner of a
  committed date that misses the lock).

Each write depends on the investigation: the sheet cells, the hold note and the recommendation are all the output of
reconciling the readiness signals; none can be written without the reads.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents | Destination | Recipients | Catalog write | Fed by |
|---|---|---|---|---|---|
| Calendar tab | one row per beat (7): the windows it runs, whether held and until when, the push that goes with it, what still has to land + owner; no Zombie Lane, Halloween one-off, Boss Arena or Axe Arena row | Julia's calendar sheet `f_e4a17c90b3d25f6a8c1d73`, Calendar tab (A2) | — (own sheet) | gsheets values update | §5 beats |
| Pushes tab | one row per push (10): send or hold, and if held what is missing; the four rows Frederick left off are not listed | same sheet `f_e4a17c90b3d25f6a8c1d73`, Pushes tab | — | gsheets values update | §5 pushes |
| Recommendation reply | the recommendation with tradeoffs | Frederick's DM thread `slack:D05SD5QLG94/1759263617.418209` (A1) | Frederick Stone `frederick.stone@harmonygames.co` | slack message | all |
| Calendar-ticket link | the sheet linked on the existing calendar ticket | Linear `ZOM-78` (`cmt_zom78_1` says "use this ticket, link the sheet here") | — | linear comment | the sheet |
| Leagues hold note | the weekly-leagues hold recorded on its ticket; a hold note goes only on a held beat's ticket, and Weekly Leagues is the only held beat | Linear `ZOM-429` | — | linear comment | Weekly Leagues row |
| Reply to Brian | the November Season Pass config has to land before the lock, so his Fri Oct 31 10:00 Istanbul date moves to any time before the lock | Brian's slip mail `julia.lawson@harmonygames.co/1844311412966040123` | Brian Foster `brian.foster@harmonygames.co` | gmail reply | Season Pass row |

Alternatives a careful run could defend (each settled, or added to §4b): a reply by mail vs the DM (settled — Frederick
asked in his DM, so the reply returns there); a new calendar ticket vs ZOM-78 (settled — the ask names the existing
ticket, §5); a hold note on a Collect & Win or Season Pass ticket (settled — the note is for a held beat, and neither
is held, §4b); how Brian is told (a reply on his own slip mail is the canonical write; the platform review treated the
channel as a minor same-recipient point). Two alternatives that revision 1 accepted either way are closed by records
in revision 2 and are no longer open: a Zombie Lane row or iOS still-to-do (Zombie Lane is off the calendar,
`D05SD5QLG94/1759263878.305129`), and a conditional hold for Collect & Win (the brief `f_7c3e91a4d2b85f60e1a9c4` now
says a beat whose server windows are waiting on the release starts late and is not held).

### 4b · Canonical outcome (all fair outcomes)

Revision-2 values, each from its settling record (dossier §7 and §11 Revision 2). The revision-1 values came from
`solver/truth.json` (independently re-verified, `research/GOLDEN_verify.md`); the solver truth is being revised to
these seven beats and ten push rows. 08 and 09 reuse this table.
Status synonyms accepted set `{Runs, Run, Live, Running, Go}` / `{Held, Hold, On hold}`; Send set `{Send, Sent, Go, Yes}`.

| Deliverable | Field | Fixed value (or accepted set · source) | Delegated by | Allowed equivalence class | Material / representational |
|---|---|---|---|---|---|
| Plague Race | Status | Runs · `cmt_zom543_1` (queue-panel gap is not a play blocker) | — | Runs-set | material |
| Plague Race | Weeks running | All four weeks · `D05GU6L0XFH/1759270241.638119` (one-off dropped) | — | "all four weeks" / "weeks 1-4" / "4 weeks" | material |
| Collect & Win | Status | Runs, as a late start · `#470#rc_10` + brief `f_7c3e91a4d2b85f60e1a9c4` ("A beat whose server windows are waiting on that release starts late, it is not held.") | — | Runs-set only (a late-start note is fine); Held, or a conditional hold until Oct 10, is no longer accepted | material |
| Collect & Win | First window (UTC) | Fri Oct 10 00:00 UTC · `#470#rc_10` + `evt_9a4c2e7f1b3d58e06c7a2f` + brief cadence | — | "Fri Oct 10 00:00 UTC" / "2025-10-10 00:00 UTC" / "Oct 10 00:00 UTC" / "Thu Oct 9 17:00 PDT" | material |
| Collect & Win | Still to do (owner) | the final vial models (Claire) `#468#rc_38` + event-icon animation (Marcus) `cmt_zom465_2`, `cmt_zom465_3` + windows live on prod with the Oct 8 backend release (Douglas) | owners named in records | each item present, any order; owner names accepted | material (items) · representational (order) |
| Season Pass | Status | Runs · `cmt_zom552_1` (analytics, not a hold); the October season is already running on prod (`#470#rc_10`) and the November season opens Sat Nov 1 00:00 UTC; the brief's clip sentence holds them to Mon Oct 6 00:00 UTC and Sun Nov 2 23:59 UTC | — | Runs-set; an October season that does not count, or a first window on Nov 1 only, is not accepted | material |
| Season Pass | First window (UTC) | Mon Oct 6 00:00 UTC · brief clip sentence + `#470#rc_10` (the October season opened Oct 1 and is running) | — | "Mon Oct 6 00:00 UTC" / "2025-10-06 00:00 UTC" / "Sun Oct 5 17:00 PDT" | not graded (no slot reads this cell) |
| Season Pass | Still to do (owner) | premium strip → November (Oliver) `#472#rc_1` + November config before Oct 31 00:00 UTC (`page_season_pass_spec` 24h + `julia.lawson@harmonygames.co/1844311412966040123`; Brian's Oct 31 10:00 Istanbul ~7h late, so the date moves to any time before the lock and Brian is told) | owners named | both items present; "Oct 31 00:00 UTC" / "2025-10-31 00:00 UTC" / "before the lock" | material |
| Endless Monster Mode | Status | Runs · `cmt_zom504_1` | — | Runs-set | material |
| Endless Monster Mode | Still to do (owner) | empty · `cmt_zom565_1` (polish its owner says is not needed for the beta; analytics is not a hold) | — | empty, or a harmless VFX/analytics note | representational |
| Weekly Leagues | Status | Held · `C0880U9751A/1759265412.481909` (established prod failure even after a restart); the only held beat; no fix has a date, and since revision 8 the brief says such a hold runs until the fix is confirmed on prod | — | Held-set | material |
| Weekly Leagues | First window (UTC) | Mon Oct 6 00:00 UTC, on a row marked held · brief `f_7c3e91a4d2b85f60e1a9c4` (held-row sentence) | — | "Mon Oct 6 00:00 UTC" / "2025-10-06 00:00 UTC" / "Sun Oct 5 17:00 PDT" | not graded (no slot reads this cell) |
| Weekly Leagues | Weeks running | All four weeks, on a row marked held · brief `f_7c3e91a4d2b85f60e1a9c4` (held-row sentence) | — | "all four weeks" / "weeks 1-4" / "every week" | not graded (no slot reads this cell) |
| Weekly Leagues | Still to do (owner) | the weekly-reset fix so a new week starts on prod (Douglas) · `C0880U9751A/1759265412.481909` | owner named | the reset-fix item present | material |
| Quests | Status | Runs · `cmt_zom534_1` | — | Runs-set | material |
| Quests | Still to do (owner) | empty since revision 5 · `68dac8204f1e9a3b7c2d5e61` (Leonard's note on the open quests card: more quests and the reward balance go in with the Mon Oct 13 rollover if they are ready and the weekly rollover does not wait on them, so nothing has to land before the beat runs) | — | empty; a line that mentions the Oct 13 set is not graded either way | not graded (no slot reads this cell) |
| Quests | Weeks running | All four weeks · `68dac8204f1e9a3b7c2d5e61` (the weekly rollover; the current quests keep running either way) | — | "all four weeks" / "weeks 1-4" / "every week" | not graded (no slot reads this cell) |
| Daily Login | Status | Runs · `cmt_zom556_1` | — | Runs-set | material |
| Daily Login | Still to do (owner) | empty · `cmt_zom432_2` (Samuel's closing note on ZOM-432, which is Done: the frame went out with PR #471 and is in both submission builds, iOS 50 and Android 135; nothing left) | — | empty, or a harmless note that it is ready; a frame still-to-do (store approval, Android only) is not accepted | material (no frame still-to-do) · representational (empty vs a ready note) |
| Daily Login | Weeks running | All four weeks · base push sheet `f_a325dd4af80afc5994d5dc` (the row's Daily/Monthly Rollover) | — | "all four weeks" / "weeks 1-4" / "every week" | not graded (no slot reads this cell) |
| 1-day lapse | Send or hold | Held · `f_a325dd4af80afc5994d5dc` (Ready+LIVE but old-title body copy) | — | Held-set | material |
| 1-day lapse | What is missing | old-title copy fix — the English copy still names the old game title · `f_a325dd4af80afc5994d5dc` | owner | names the old-title / rename copy fix | material |
| D0-1 FTUE | Send or hold | Held · `f_a325dd4af80afc5994d5dc` (old-title body copy) | — | Held-set | material |
| D0-1 FTUE | What is missing | old-title copy fix · `f_a325dd4af80afc5994d5dc` | owner | names the old-title / rename copy fix | material |
| Plague Race start | Send or hold | Held · `f_a325dd4af80afc5994d5dc` (row Ready, Status (NA, WIP, LIVE) col = WIP) | — | Held-set | material |
| Plague Race start | What is missing | the row is not LIVE: its Status (NA, WIP, LIVE) column reads WIP · `f_a325dd4af80afc5994d5dc` | — | names the WIP / not-LIVE status; a criterion must not require a statement about client wiring (base `NotificationManager.cs` already schedules it locally) | material |
| Weekly Leaderboard reset | Send or hold | Held · `f_a325dd4af80afc5994d5dc` (row Ready, Status (NA, WIP, LIVE) col = WIP) | — | Held-set | material |
| Weekly Leaderboard reset | What is missing | the row is not LIVE: WIP · `f_a325dd4af80afc5994d5dc` | — | names the WIP / not-LIVE status; no wiring claim required | material |
| Quests rollover push | Send or hold · what is missing | Held: the row is Not Ready · `f_a325dd4af80afc5994d5dc` | — | Held-set; names Not Ready | material |
| Win & Collect event start | Send or hold · what is missing | Held: Not Ready, WIP, and the copy uses the Domino Delights event name instead of Collect & Win · `f_a325dd4af80afc5994d5dc` | — | Held-set; names at least one of Not Ready / WIP / the wrong event name | material |
| Login Calendar update | Send or hold · what is missing | Held: Not Ready, WIP · `f_a325dd4af80afc5994d5dc` (the daily gift's push row, brief `f_7c3e91a4d2b85f60e1a9c4`) | — | Held-set; names Not Ready / WIP | material |
| Season Pass activation | Send or hold · what is missing | Held: Not Ready, WIP · `f_a325dd4af80afc5994d5dc` | — | Held-set; names Not Ready / WIP | material |
| Lives recharged | Send or hold | Send · `f_a325dd4af80afc5994d5dc` (Ready+LIVE; copy names no game, which Frederick's follow-up `D05SD5QLG94/1759263878.305129` allows) | — | Send-set | material |
| 7-day lapse | Send or hold | Send · `f_a325dd4af80afc5994d5dc` (Ready+LIVE; copy names no game, allowed by the same follow-up) | — | Send-set | material |
| Reply to Brian | content | the November config has to land before the Oct 31 00:00 UTC lock, so his Fri Oct 31 10:00 Istanbul date moves to any time before the lock · `julia.lawson@harmonygames.co/1844311412966040123` + `page_season_pass_spec` | brief: "you tell its owner in a reply on the mail where they committed to it" | any wording that tells Brian the date has to move before the lock, in a reply on his slip mail (the brief fixes the channel since revision 4) | material (Brian told, earlier date) · representational (wording) |
| Hold note | which ticket | `ZOM-429` only · `C0880U9751A/1759265412.481909` (Weekly Leagues is the only held beat) | — | one hold note, on `ZOM-429`; a hold note on a Collect & Win or Season Pass ticket is not accepted | material |
| Recommendation reply | content | a recommendation reflecting the held/run/send-hold decisions, with tradeoffs · `slack:D05SD5QLG94/1759263617.418209` | delegated (the persona's call) | any coherent recommendation consistent with the calendar | representational |

**Push-plan scope (settled in revision 2; no longer an acceptance boundary).** Frederick's thread reply under his ask
(`D05SD5QLG94/1759263878.305129`, 2025-09-30T20:24:38Z) fixes the row set:
"plan the PNs Beta tab as it stands, one line per row, local notifications included", then
"Leave off the four rows for things that are not in the beta" (Hourly Coins, Nathan's Treasure Hunt, Streak Fever and
Axe Arena, "just those four"). So the plan has **ten required rows**, all ten above: the six that were required in
revision 1 plus the Quests rollover push, Win & Collect event start, Login Calendar update and Season Pass activation
(all four Held). The **four named rows are excluded** and must not be listed at all, not even as held. The same reply
settles the copy edge: "Copy that does not name the game at all is fine to go out, the naming rule is only about wrong names."
so Lives recharged and 7-day lapse are Send. A plan with only the six Ready rows, a plan with only the Push
Notification rows, or a plan with all 14 rows is no longer accepted. The Calendar tab's "Push" and "Hold until (UTC)"
columns may still be filled per beat or left to the Pushes tab; both are accepted (representational). The rubric (09)
must encode this: grade all ten send/hold decisions, and treat any of the four excluded rows appearing in the plan as
wrong. Base support for the four exclusions: Brian's #company-internal post `C05KNDCHAAG/1758558164.541689` postpones
Axe Arena for the beta; Confluence `page_liveops_calendar` lists Streak Fever, Nathan's Treasure Hunt and Axe Arena as
Domino Delights events; Hourly Coins has no ZM3D record.

## 5 · Discovery map

Facts the agent must find (never named in the prompt by default). Each is persona-readable (§5a) or unscoped. "Met
first / overturned by" captures the dynamic-change traps.

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| C&W first window | Fri Oct 10 00:00 UTC, a late start (Runs, not held) | `#470#rc_10` + `evt_9a4c2e7f1b3d58e06c7a2f` + brief cadence and late-start sentence | github (unscoped) · gcal (YES §5a) · gdocs (YES) | merged PRs / Julia's "feature completed" note → Arthur's DEV-only review + Oct 8 release | latches on "merged = live"; stops at the merge; or reads the late start as a hold | No |
| Ask follow-up: push-plan rows, no-game copy, Zombie Lane off | ten PNs Beta rows (Hourly Coins, Nathan's Treasure Hunt, Streak Fever, Axe Arena left off); copy that names no game may go out; Zombie Lane is not a beat | `D05SD5QLG94/1759263878.305129` | slack (YES §5a) | the ask root (shows `reply_count` 1) and the brief → the thread reply under the ask | family A14, replies never opened: DM history returns parents only, so a run that reads only the root never sees it | No (the prompt points to Frederick's message, never to a reply or a thread) |
| SP October season | already running on prod, so it counts; the November season opens Sat Nov 1 00:00 UTC | `#470#rc_10` + `evt_9a4c2e7f1b3d58e06c7a2f` | github (unscoped) · gcal (YES §5a) | the release event read as covering every live-ops window → Arthur's note that the Plague Race, leagues, Endless and Season Pass schedules already run on prod | applies the C&W deploy wait to every beat | No |
| Plague Race weeks | all four weeks | `D05GU6L0XFH/1759270241.638119` | slack (YES §5a) | Robert's #zombie-art approval → his later DM withdrawal | rarely searches a reply to a dispute; since revision 9 a 'Halloween' search returns only the approval | No |
| Weekly Leagues held | Held (prod failure after restart) | `C0880U9751A/1759265412.481909` | slack (YES §5a) | ZOM-429 "restart gets players in" / Sep 22 "working fine" → Vincent's Sep 30 prod re-test | stops at the earlier "working fine" | No |
| SP config lock | before Oct 31 00:00 UTC | `page_season_pass_spec` (24h) + `…/1844311412966040123` (slip) + Nov 1 open | confluence (unscoped) · gmail (YES §5a) | Brian's Wed Oct 29 handoff → his Fri Oct 31 10:00 Istanbul slip (7h late) | secondhand mail over the base spec; timezone slip | No |
| SP premium strip | → November range (Oliver) | `#472#rc_1` | github (unscoped) | — (per-PR inline note on #472) | prefers chat over per-PR reads | No |
| C&W vial models | still to do (Claire) | `#468#rc_38` | github (unscoped) | — (per-PR inline review note on #468) | prefers chat over per-PR reads | No |
| C&W event icon | still to do (Marcus) | `cmt_zom465_2`, `cmt_zom465_3` and the `#456` enumeration | linear + github (unscoped) | ZOM-465 "idle icons done" → `cmt_zom465_2` and `cmt_zom465_3` on the same ticket + `#456` omits C&W | stops at the struck line or at the first note | No |
| Quests still-to-do | none: the weekly rollover does not wait on the new quests (ungraded since revision 5) | trello `68dac8204f1e9a3b7c2d5e61` | trello (unscoped) | the open quests card and the push row's 'Revisit once new quests roll out' | reads the Oct 13 set as work the beat waits for | No |
| Daily Login done | nothing left (frame in both submission builds, iOS 50 and Android 135) | `cmt_zom432_2` on the Done ticket ZOM-432 (base #builds `C05433XK267/1759259749.259909`, `C05433XK267/1759263189.219529` agree) | linear (unscoped) · slack (#builds member) | Calvin's Sep 24 note on the same ticket (`cmt_zom432_1`) → Samuel's closing note | takes the older note over the ticket's closure and its last note; or treats store approval as a still-to-do | No |
| Pushes (10 rows) | 2 send / 8 held | base push sheet `f_a325dd4af80afc5994d5dc` tab PNs Beta; the row set from `D05SD5QLG94/1759263878.305129` | gsheets (YES §5a) · slack (YES §5a) | Ready read as sendable → the second status column (WIP, not LIVE) + the old-title body copy; its own pick of rows → Frederick's follow-up | reads "Ready" as "send"; misses the second status column; plans 6, 9 or 14 rows | No |
| The working rules | deploy/scope/hold/copy/lock rules | brief `f_7c3e91a4d2b85f60e1a9c4` | gdocs (YES §5a) | — (the rulebook the ask points to) | — | Named only as "the working rules" (A1 delegates to it) |

## 5a · Search-as-persona proof

Full evidence in `Working_Files/research/PROMPT_persona_entity.md` Section A. All 13 scoped facts are reachable for
julia_lawson. Eleven are rows of the proposed overlay (`search` reads only the base export, so it returns 0 for them —
U4); their proof is `check-sql --load-bearing` YES **plus** a text match of the natural query on the row. Two (#5, #12)
are base records a `search` returns directly. Row 13, added in revision 2, is the thread reply under the ask: it is
reached by opening the thread of row 1 (the root shows `reply_count` 1), not by a keyword, and the revision-2
`check-sql` re-run returns YES for it. Unscoped services (github, linear, trello, confluence) are always
readable per `Evals/references/persona/acl.md` — no persona search needed.

| # | Fact | Service | Natural query (found) | Found? | Note |
|---|---|---|---|---|---|
| 1 | Frederick's ask (DM `D05SD5QLG94`) | slack | `live-ops and push calendar` / `push calendar` | YES (overlay; check-sql YES, im member) | `beta calendar`, `live-ops calendar` MISS |
| 2 | Robert approval (`C08R8CHB0QL`) | slack | `Halloween one-off` | YES (public #zombie-art member) | exact phrase |
| 3 | Robert withdrawal (`D05GU6L0XFH`) | slack | `pulling my ok` / `beta calendar` (since revision 9 not `Halloween one-off`: it says "the themed prop set I okayed in Martin's thread") | YES (im member) | DM history with Robert also returns it |
| 4 | Vincent prod re-test (`C0880U9751A`) | slack | `weekly leaderboard` | YES (private #zombie-match3d member) | 55 base hits; decisive row is the private re-test |
| 5 | zombie-bugs iOS thread (`C08R27X0EAH`) | slack | `ios build` | YES (base; #zombie-bugs member) | `zombie lane ios` = 0 hits; context only since revision 2 (Zombie Lane is off the calendar, so this thread decides no row) |
| 6 | Brian SP handoff (`…/1843954828968533812`) | gmail | `Season Pass November config` | YES (Julia's mailbox) | Brian/Frederick copies NO (correct) |
| 7 | Brian slip (`…/1844311412966040123`) | gmail | `Season Pass config` / `Oct 31` | YES (Julia's mailbox; not opened yet, and it carries no UNREAD label since revision 5) | the final truth; supersedes Oct 29 |
| 8 | Oct 8 release (`evt_5c1e83a7…`) | gcal | `backend release` | YES (Julia's own copy) | one meeting, 3 copies; cite Julia's |
| 9 | the brief (`f_7c3e91a4…`) | gdocs | `working rules` / `beta live-ops` | YES (shared) | `beta brief`, `live-ops rules` MISS — title is "ZM3D beta live-ops calendar - working rules" |
| 10 | UA deck (`f_2b9d4e7a…`) | gslides | `UA plan` / `buy weeks` | YES (shared) | — |
| 11 | Julia's calendar sheet (`f_e4a17c90…`) | gsheets | `Live-Ops Calendar` | YES (owner) | `ZM Live Ops` is the FOLDER (`d_5f2c8e1b…`), sheet title "ZM3D Beta Live-Ops Calendar" |
| 12 | base push sheet (`f_a325dd4a…`) | gsheets | `PNs` / `Push Notifications Zombie Match` | YES (base, shared) | decoy `f_351b98df…` = "Push Notifications Domino Adventure" |
| 13 | Frederick's follow-up reply (DM `D05SD5QLG94`, thread under the ask of row 1) | slack | open the thread of the ask (row 1 shows `reply_count` 1); the text also matches `PNs Beta tab` / `Zombie Lane off the calendar` | YES (overlay; check-sql YES on the revision-2 SQL, im member) | added in revision 2; no search output is pasted for it below (overlay rows return 0 base hits, U4); a run that reads only the DM root misses it |

`check-sql --load-bearing` verdict (the twelve revision-1 rows + no-leak): `verdict: PASS (0 load-bearing rows not visible)`.
Row 13 is YES in the revision-2 report-only re-run (30 YES, the same 8 other-mailbox copies and 10 mirror rows). The ten
`#zombie-prs` mirror rows are the only UNVERIFIED (U1, non-member) — non-load-bearing by design; PR evidence routes
through GitHub (unscoped). Verbatim `persona_view.py search` outputs (all run as julia_lawson; revision-1 paste, left
as it was):

```
SEARCH slack 'live-ops and push calendar' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers   [overlay row; check-sql YES, im D05SD5QLG94 member]
SEARCH slack 'beta calendar' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers   [so the prompt must not promise the words "beta calendar"]
SEARCH slack 'Halloween one-off' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers   [overlay; check-sql YES, public zombie-art member]
SEARCH slack 'pulling my ok' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers   [overlay; check-sql YES, im D05GU6L0XFH member]
SEARCH slack 'weekly leaderboard' as julia_lawson  scope: Slack message text (all shards)
visible hits=55 (showing 2)  hidden by ACL=61 in 25 containers  UNVERIFIED=8 in 3 containers   [decisive private #zombie-match3d re-test row: check-sql YES]
SEARCH slack 'ios build' as julia_lawson  scope: Slack message text (all shards)
visible hits=135 (showing 2)  hidden by ACL=132 in 34 containers  UNVERIFIED=16 in 3 containers   [in-channel #zombie-bugs, base, member]
SEARCH gmail 'Season Pass November config' as julia_lawson  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers   [overlay; check-sql YES in Julia's mailbox]
SEARCH gcal 'backend release' as julia_lawson  scope: GCal event summary
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers   [overlay; Julia's own copy evt_5c1e83a7d94b02f6c8e31a YES]
SEARCH gdocs 'working rules' as julia_lawson  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers   [overlay; shared; 'beta brief' MISSES]
SEARCH gslides 'UA plan' as julia_lawson  scope: GSlides title + page element text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers   [overlay; shared]
SEARCH gsheets 'Live-Ops Calendar' as julia_lawson  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers   [overlay; owner; 'ZM Live Ops' is the folder]
SEARCH gsheets 'PNs' as julia_lawson  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=2 (showing 2)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers   [correct "Push Notifications Zombie Match"; decoy "Push Notifications Domino Adventure"]
```
(Overlay rows return 0 base hits by design — U4; their proof is `check-sql` YES + a text match, see the table above. Full evidence: `research/PROMPT_persona_entity.md`.)

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger the prompt must carry | Incorporating source (locator · readable · unique · instructions-not-answer) | Inferable? |
|---|---|---|---|---|
| Build the beat calendar (7 rows) | the ask + its thread reply + brief | deliverable: the calendar in her sheet, plus a pointer to Frederick's message for what he wants in it | A1 ask → the brief `f_7c3e91a4` (readable; one search; states the rules, not the answers); the thread reply `D05SD5QLG94/1759263878.305129` keeps Zombie Lane off | the ask makes it explicit |
| Build the push plan (10 rows) | the ask + its thread reply + brief + push sheet | deliverable: named together with the calendar (the live-ops and push calendar), plus the pointer to Frederick's message; no per-push field list in the prompt | A1 thread: the reply `D05SD5QLG94/1759263878.305129` (readable; reached by opening the ask's thread; states which rows to plan, not their send/hold answers) + the base push sheet (readable) | explicit for the plan; the row set is a gotcha → triggered by pointing to his message |
| Apply the deploy / scope / hold / copy / lock rules | brief | constraint: a pointer to the brief as his working rules | brief (readable; unique; instructions) | gotcha → triggered by naming the brief as the rulebook |
| Reply with the recommendation + tradeoffs | the ask | deliverable + recipient (Frederick); the trade-offs come from the ask, the prompt only points to the recommendation he asked for | A1 (the ask asks for it back) | explicit |
| Link the sheet on the calendar ticket | the ask + `cmt_zom78_1` | recipient/destination: the calendar ticket | the ask names it; `cmt_zom78_1` says "use this ticket, link the sheet here" | explicit |
| Note the leagues hold on its ticket | the prompt's own condition + ZOM-429 | constraint carried by the prompt itself since revision 2: a beat that ends up held gets a note on its ticket (revision 1 conditioned it on a beat that could not run yet, which the review found ambiguous) | which beat is held: the brief's hold rule + Vincent's re-test `C0880U9751A/1759265412.481909`; its ticket: `ZOM-429`, the only open ZOM weekly-leaderboard ticket | explicit in the prompt; the brief has no ticket-note rule of its own |
| Tell Brian the config date has to move before the lock | brief rule + Brian's slip mail | constraint via the brief (the pointer to his working rules) | brief `f_7c3e91a4`: "A committed date that misses the lock moves to any time before it and you tell its owner in a reply on the mail where they committed to it." (readable; unique; an instruction, not the answer) | gotcha → triggered by naming the brief as the rulebook |
| Check readiness before scheduling | implicit | — | — | inferable (a PM checks before scheduling) |

Anchor-name table (noun phrases ≤ 6 words; `;`-separated synonyms; gate-checked):

| Anchor | May be named |
|---|---|
| A1 Frederick's ask | Frederick's beta calendar ask; the beta live-ops and push calendar; Frederick's message |
| A2 the calendar sheet | my beta live-ops calendar sheet; the Live-Ops Calendar sheet |
| the brief | the working rules |
| ZOM-78 | the calendar ticket |
| ZOM-429 | the weekly leagues ticket; the held beat's ticket |

Findability note (from §5a): the agent finds the brief by "working rules" (not "beta brief"); the sheet by "Live-Ops
Calendar" ("ZM Live Ops" is the folder); the ask by "live-ops and push calendar" ("beta calendar" alone misses). The
draft should lean on these phrasings so a natural search resolves each anchor. The follow-up is found from the ask,
not by a phrase: the ask's root shows one reply, and the prompt must not say so. The prompt may refer to ZOM-429 only
as the held beat's ticket, never as the leagues ticket (that would give the hold away).

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
|---|---|---|---|
| Beta buy weeks | Mon Oct 6 – Sun Nov 2 2025 | brief `f_7c3e91a4d2b85f60e1a9c4` + ask `D05SD5QLG94/1759263617.418209` | the window (plan) |
| Backend release | Wed Oct 8 15:00–16:00 UTC (18:00 Istanbul) | `evt_9a4c2e7f1b3d58e06c7a2f` | future plan event |
| C&W first window | Fri Oct 10 00:00 UTC | computed from `#470#rc_10` + `evt_9a4c2e7f1b3d58e06c7a2f` | **never in the prompt** |
| More quests | Mon Oct 13 2025 rollover, if they are ready (the weekly rollover does not wait on them) | trello `68dac8204f1e9a3b7c2d5e61` | future plan; decides no graded value since revision 5 |
| SP config lock | Oct 31 00:00 UTC | `page_season_pass_spec` + `julia.lawson@harmonygames.co/1844311412966040123` + Nov 1 open | **never in the prompt** |
| November season opens | Sat Nov 1 00:00 UTC (the October season is already running on prod) | `page_season_pass_spec` + `#470#rc_10` | future plan |
| Frederick's ask and its follow-up | Tue Sep 30 2025, 20:20:00 and 20:24:38 UTC (13:20 and 13:24 PDT) | `D05SD5QLG94/1759263617.418209`, `D05SD5QLG94/1759263878.305129` | past fact; the day before the clock |
| Submission builds with the daily-gift frame | Tue Sep 30 2025: iOS #50 19:15 UTC, Android #135 20:13 UTC | `C05433XK267/1759259749.259909`, `C05433XK267/1759263189.219529` | past fact |
| Clock (today) | Wed Oct 1 2025 (07:00 UTC) | `00_Task_Context.json:/universe/persona_today` | — |

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
|---|---|---|---|---|
| Ambiguity | Yes | partial | which records decide each beat/push (the answer's location) | vague about where the answer lives, never about what is asked; destinations (her sheet, the calendar ticket, a held beat's ticket, Frederick) named because Julia knows them; what is asked is settled by Frederick's message and its reply, not left open |
| Dynamic change | Yes | **Load-bearing** | the four supersessions: Robert approve→withdraw; ZOM-429 "fine"→Vincent prod re-test; Brian handoff→slip; ZOM-465 "icons done"→`cmt_zom465_2`, `cmt_zom465_3` | the prompt gives a reason to build from current readiness but names neither the first summary nor the correction |
| Multi-source | Yes | **Load-bearing** | 9 services carry weight; facts scattered and reconciled | no deciding source named as an exact artifact; only the destinations, Frederick's message and his brief (as the working rules) are pointed to |
| Async | No | — | — | no forced wait (Friction: none) |
| Error recovery | No | — | — | no forced error (Friction: none) |
| Access control | No | — | the `#zombie-prs` mirrors are non-member but non-load-bearing | no requirement asks the agent to read a restriction it never saw |

At least one of Ambiguity / Dynamic Change / Multi-Source is load-bearing: **Dynamic Change and Multi-Source both are**.

## 9 · Must not appear in the prompt

- **Tool / parameter / MCP names**: any function name (slack_*, gmail_*, gsheets_*, github_*, linear_*, gcal_*, trello_*, gdocs_*, gslides_*), any server name, "the X tool".
- **Internal / opaque IDs**: `D05SD5QLG94…`, `C08R8CHB0QL…`, `D05GU6L0XFH…`, `C0880U9751A…`, `C08R27X0EAH`, `f_7c3e91a4…`, `f_2b9d4e7a…`, `f_e4a17c90…`, `f_a325dd4…`, `d_5f2c8e1b…`, `evt_9a4c…`, `#470/#468/#472/#471` and, from earlier revisions, `#370/#438/#454/#473` (+ `#rc_`/`#c_`), `cmt_zom*`, `68dac820…`, every 32-hex slack id, `page_season_pass_spec`.
- **Outcomes / findings** (discovered): any "Runs"/"Send"/"Hold until", which beat is held (the prompt may use the word held only as the condition for the ticket note, never with a beat's name), "Fri Oct 10", "Oct 31 00:00 UTC", "all four weeks", "WIP" or any wiring claim, "Puzzles vs Zombies"/old title, "vial models" (or "vial sprites"), "premium strip", "event icon", "Mon Oct 13", "frame shipped", "late start", "iOS 50", "submission 135".
- **Scope findings added in revision 2** (they live in Frederick's follow-up, not in the prompt): "Hourly Coins", "Treasure Hunt", "Streak Fever", "Axe Arena", "Zombie Lane", "local notification", the count of beats (seven) or push rows (ten), and the name of any single beat or push row.
- **Root causes / deciding records**: why any beat is held or runs; the withdrawal, the prod re-test, the slip, the per-PR review notes, the backend-release date, the 24h lock rule; that Frederick's message has a follow-up reply at all, and the word "thread" or "reply" for it.
- **Injected friction / async / reference files**: none to mention (Friction: none; no reference files).
- **Format scaffolding**: markdown, numbered steps, per-deliverable content lists, a service list, a call count, the number of beats or pushes, and the per-row field list of Frederick's ask (the platform review failed revision 1 on restating it).

## 10 · Entity traps

Full `entity.py collisions` + `resolve` output in `Working_Files/research/PROMPT_persona_entity.md` Section B. Verbatim
collisions (abridged):

```
SHARED_FIRST_NAMES: claire, marcus (Bennett/Lee/trello mononym), martin, thomas
SHARED_LAST_NAMES: baker (Owen/Thomas), bennett (Marcus/Oscar), brooks (Oliver/Lauren), lawson (Julia/Peter), price (Calvin/Nathan)
SEVERAL_IDS_IN_ONE_SERVICE: Calvin Price -> 2 github logins PERSON_0003 + PERSON_2137
INTEGRITY FLAGS: usr_Victor Barnes (id_with_space); github PERSON_2314 joined by email but shows name 'Ryan' (entity is Frederick Stone)
```

| Correct entity (exact) | Lookalike(s) | How they differ | Locator |
|---|---|---|---|
| Julia Lawson `julia.lawson@harmonygames.co` · slack EMPLOYEE_0005_SLACK_ID | Peter Lawson `peter.lawson@`; gmail alias `jlawson@` | same surname, different person | resolve "Julia Lawson" |
| Frederick Stone `frederick.stone@harmonygames.co` · slack EMPLOYEE_0008_SLACK_ID | **GitHub PERSON_2314 renders "Ryan" — IS Frederick** | display name lies (email join) | resolve "Frederick Stone" → name-mismatch FLAG |
| Robert `robert@harmonygames.co` · slack EMPLOYEE_0016_SLACK_ID | none exact; **no surname** | mononym; highest-volume Slack author | resolve "Robert" |
| Vincent Parker `vincent.parker@harmonygames.co` · slack EMPLOYEE_0012_SLACK_ID | git `43593629+vincent.parker` | same person, committer form | resolve "Vincent Parker" |
| Arthur Blake `arthur.blake@harmonygames.co` · slack EMPLOYEE_0025_SLACK_ID | branch mononym "Blake" | surname, not a separate person | resolve "Arthur Blake" |
| Marcus Bennett `marcus.bennett@harmonygames.co` · github PERSON_0396 | Marcus Lee `marcus.lee@`; Trello mononym `Marcus`; Oscar Bennett | two Marcuses + an unresolved Trello mononym | resolve "Marcus Bennett" → UNRESOLVED |
| Samuel Turner `samuel.turner@harmonygames.co` · github EMPLOYEE_0004 | confluence id `user_STAFF_18` (not EMPLOYEE_0004) | linkability trap | resolve "Samuel Turner" |
| Brian Foster `brian.foster@harmonygames.co` · trello d1cd0fef645a6c978ae1f068 | alias `brian@` | no second Brian | resolve "Brian Foster" |
| Douglas `douglas@harmonygames.co` · slack EMPLOYEE_0031 | none; **no surname**; owns the release calendar | mononym; gcal organizer of evt_9a4c… | resolve "Douglas" |
| Calvin Price `calvin.price@harmonygames.co` | **two github logins** PERSON_0003 + PERSON_2137; Nathan Price | one human, two logins → double-count risk | resolve "Calvin Price" |
| Oliver Brooks `oliver.brooks@harmonygames.co` | Lauren Brooks `lauren@` | same surname | resolve "Oliver Brooks" |
| Owen Baker `owen.baker@harmonygames.co` | Thomas Baker `thomas.baker@`; Thomas `thomas@` | `thomas@` ≠ `thomas.baker@`; shared surname | resolve "Owen Baker" |

**Traps the prompt must avoid**: (1) GitHub "Ryan" = Frederick Stone — never "Ryan". (2) duplicate first names (Marcus ×3,
Claire, Martin, Thomas) + shared surnames (Baker, Bennett, Brooks, Lawson, Price) → full name + id. (3) Calvin's two
GitHub logins. (4) mononyms (Robert, Douglas, Thomas) — never expand. (5) **ZOM-429 ≠ ENG-429** (521 collides across
series) — always the full `ZOM-###` key, never "ticket 429". (6) two "PNs" sheets — correct "Push Notifications Zombie
Match", decoy "...Domino Adventure". (7) `#zombie-prs` not reachable for Julia. (8) per-mailbox Gmail copies — cite
Julia's thread ids. (9) one Oct 8 release meeting (3 copies, shared ical_uid) — use Julia's copy. Since none of these
record ids / display names may appear in the prompt (§9), the prompt simply names people by full name and tickets by
their `ZOM-###` key, and the agent resolves the rest.

## 11 · Pre-submit checklist

- [ ] Ordinary request in Julia's voice; no riddle, trap hint, answer-key clause, staged error, audit-form wording or if-chain.
- [ ] No outcome, root cause or deciding record named (§9).
- [ ] Destinations named (her sheet, Frederick, the calendar ticket, a held beat's ticket; never the leagues ticket by name); what he wants pointed to as Frederick's message and the rules as his working rules in the brief.
- [ ] Symptom only (§2); no "why".
- [ ] No tool / parameter / server name; no internal id; no markdown / numbered steps / counts.
- [ ] Every premise holds at the Oct 1 2025 clock; no actor inactive, nothing first appearing after 2025-09-30 23:59:59 PT.
- [ ] At least one write that depends on the investigation (the sheet, the reply, the links).
- [ ] The beats and push rows are not counted, listed or described field by field; the prompt points to Frederick's message and brief instead (review issue 3), so the scope stays discovered.
- [ ] The ticket note is conditioned on a held beat only, and nothing says that Frederick's message has a reply.

## 12 · Blockers and routed defects

- None expected: every scoped deciding fact is targeted for a YES in §5a (pending the evidence worker); unscoped facts
  are always readable. If §5a returns any NO, route it to `/create-injection` and record it here.
- Platform `/injection` must be re-run on the current SQL (SHA `edae63f3e838`, revision 14) — the platform PASS on
  record is for the revision-2 SQL (`3afbf7cbbdb7`) and is stale. Platform `/prompt` FAILED on revision 1 on 2026-11-05 (Unique Ground
  Truth 2, Clarity 2, Contrived 2) and again on revision 2 (Cross-Service Coherence 2 alone, known-issue card SC-15,
  which revision 3 repairs); an independent run on revision 3 then failed Cross-Service Coherence on further items and
  gave Clarity 3, which revision 4 repairs; an independent round on revision 4 found further base contradictions, which revision 5 repairs; independent rounds on revisions 5 and 6 left one fork and two advisories, which revisions 6 and 7 repair; a blind round on revision 7 raised further items, which revision 8 repairs; the platform's third failure, on revision 8, is repaired in revision 9, a pre-review attack on revision 9 in revision 10, the formal blind round on revision 10 in revision 11, the verification round on revision 11 in revision 12, the cold reviewers' last items in revision 13, and the last cold P1 in revision 14; it is re-run after `/injection`, as a pair, on prompt `2a23afd87c4c`, then
  `/hardness`.
- The local stage gates cannot be re-pasted on this machine yet (the tools from the authoring machine are not synced;
  `hardness_gate` here does not know `volume_exception.rows_floor`), so the gate block in §13 is the revision-1 record.
- The blockers revisions 4 and 5 left are gone: the cohort is 41, the SQL does not touch `ZOM-387`, and since revision 6
  the ticket is out of the cohort, so `base_check` passes without the manifest and `hazard_scope` passes with no
  acknowledgement. What still stops the injection gate on this machine is the tool gap above and the stale pastes.

## 13 · Self-review

- **Evidence pointers**: every row of §2, §4, §4b, §5, §7 and §10 carries a record id, email or pointer (checked).
- **Anchor names**: all §6 entries are noun phrases ≤ 6 words, no verb / imperative / second-person; aligned with the
  manifest `anchors[].prompt_reference` (A1, A2) and the dossier §7 table.
- **Reach**: §5a shows all 13 scoped load-bearing facts YES for julia_lawson (`check-sql verdict: PASS` for the twelve
  revision-1 rows; the follow-up reply is YES in the revision-2 re-run); the only
  UNVERIFIED rows are the non-load-bearing `#zombie-prs` mirrors (PR evidence routes through unscoped GitHub).
- **Must-not-appear (§9)**: covers every outcome (which beat is held, Runs/Send, Oct 10, Oct 31, four weeks, WIP, old
  title, each still-to-do), the revision-2 scope findings (the four excluded push rows, Zombie Lane, local
  notifications, the counts), every deciding record and id including the existence of the follow-up reply, every root
  cause, and all format scaffolding including the ask's per-row field list.
- **Levers**: Dynamic Change and Multi-Source are both load-bearing (≥ 1 required) — the four supersessions and nine
  weighted services.
- **Deliverable shape is grader-decodable**: two keyed sheet tabs (Calendar by beat, Pushes by push), a Slack DM message
  to Frederick, two Linear comments (ZOM-78 link, ZOM-429 hold note) and a mail reply to Brian — not prose only.
- **Fair outcomes**: §4b lists every accepted reading (Status/Send synonym sets, date formats, the delegated
  recommendation, the Calendar tab's Push / Hold-until columns filled or left to the Pushes tab); 08 and 09 reuse it.
  The two items revision 1 accepted either way (a Zombie Lane iOS note; a conditional hold for Collect & Win) and the
  optional push rows are closed by dated records in revision 2 (`D05SD5QLG94/1759263878.305129`,
  `f_7c3e91a4d2b85f60e1a9c4`), in the data and not by an answer-key clause in the prompt.
- **Symptom-not-cause**: §2 states only the visible symptom; every root cause sits in §5 flagged "never in the prompt".
  The name-swap test holds — the scenario rests on real records (§5/§5a), not on names.

Counter-readings a careful draft/run could defend, and how this brief settles each (one per QC concern):
- **Clarity** — one could **argue** the recommendation should go by email, not the DM; but Frederick asked in his DM `D05SD5QLG94/1759263617.418209`, so the reply **would** return there (settled; §4b material field).
- **Fair readings / accepted outcomes** — one could **argue** Collect & Win is held until Oct 10 rather than Runs; revision 1 accepted both, but the brief `f_7c3e91a4d2b85f60e1a9c4` now says a beat whose server windows are waiting on the release starts late and is not held, so only Runs with the Fri Oct 10 first window **would** pass (§4b, `#470#rc_10`).
- **Fair readings / push-plan rows** — one could **argue** the push plan is only the Push Notification rows, or all 14 rows of the tab, or only the six Ready rows; Frederick's thread reply `D05SD5QLG94/1759263878.305129` names the set (the tab as it stands, local notifications included, four named rows left off), so only the ten-row plan **would** pass and no reading is left for the rubric to choose between.
- **Fair readings / change-request hold** — one could **argue** Arthur's premium-strip note holds Season Pass under the brief's change-request clause; since revision 8 the note is an inline comment inside Arthur's APPROVED review of #472 (`#472#rc_1`; a plain conversation comment on #473 in revisions 4 to 7, and as the review `#438#rev_4` its state was COMMENTED), base has no CHANGES_REQUESTED in the Aug–Sep cohort, and the platform review rejected this fork itself (P1-DR13), so a criterion that **would** fail a Runs status for Season Pass is wrong. It stays a residual risk, not an accepted alternative.
- **Incorporation** — one could **argue** the 24h lock lives in the brief; it does not — the base `page_season_pass_spec` carries the 24h, the brief only points to "before its lock", so a criterion citing the brief for the offset **would** be ungrounded (fixed in §4b/§7).
- **Truthfulness** — one could **argue** the beta is already live; false — the clock is Oct 1 and the beta opens Oct 6 (`evt_9a4c2e7f1b3d58e06c7a2f` is a future plan event), so no premise **would** contradict the clock.
- **Feasibility / ACL** — one could **argue** the PR review notes require the `#zombie-prs` channel (non-member for Julia); they do not — the per-PR GitHub reads are unscoped and carry the same text (`#470#rc_10`), so no ACL-blocked read **would** be needed.
- **Contrived register** — one could **argue** the prompt should enumerate the beats, the push rows or the per-row fields; the platform review failed revision 1 on exactly that (enumerated deliverable specs, issue 3), and it **would** script the method and leak the scope, so they stay in Frederick's message `D05SD5QLG94/1759263617.418209` and the brief doc `f_7c3e91a4d2b85f60e1a9c4`, and the prompt names only the destinations and points to those two.
- **Ambiguity (destination)** — one could **argue** the hold note's ticket is ambiguous now that the prompt only speaks of a held beat's ticket; it is not — Weekly Leagues is the only held beat and `ZOM-429` is the only open ZOM weekly-leaderboard ticket, and the calendar link goes on `ZOM-78`, which `cmt_zom78_1` designates, so only *where each answer lives* **would** be discovered.
- **Ambiguity (ticket-note scope)** — one could **argue** Collect & Win and Season Pass also need ticket notes because they cannot run at the clock or still wait on config; the prompt conditions the note on a held beat and the brief `f_7c3e91a4d2b85f60e1a9c4` says a beat waiting on the release is not held, so a note on `ZOM-566` or `ZOM-552` **would** be a wrong write.
- **Unresolved**: the platform `/injection` must be re-run on SQL `edae63f3` (revision 14) and `/prompt` on prompt `2a23afd8`; the
  stage gates are to be re-pasted after the tool sync (§12); the landing rate of the follow-up reply is unknown (family
  A14, but an anchor-thread reply is `first_read` for the local `hardness_v2_check`); difficulty is UNCALIBRATED and
  borderline (settled by the six Opus baselines). No blocking defect in the brief itself at this stage.

```
STAGE GATE prompt-writing: PASS — Task_Authoring/task_inputsS · 04_Prompt_Writing_Brief.md#d7b9eabc6471 · 00_Assigments.md#4844ae9f5ae7 · 01_Grounding_Dossier.md#2ed958107b88 · 01_Universe_Inject.sql#4c6328ab2e86 · 03_Error_Async_Config.txt#ca4def2fa591 · __context__#7b0cc66ffd45 · __assignment__#e8b8269803d5 · __policy__#dc4ab5df3cdd · __gate_policy__#9b78441396d8 · __review__#461162429327 · blocking 0 · warnings 0 · checks 24
[PASS] assignment.v3_context: Julia Lawson / Product Manager; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#4c6328ab2e86, 01_Hardness_Manifest.json#cb64fe02fe26, 01_Grounding_Dossier.md#2ed958107b88, solver/solver.py#8c25e08e10c3, 01c_Dispositions.json#777cf02e465b, 01c_Preflight_Report.json#d01a61396e73, 00_Assigments.md#4844ae9f5ae7, 01_Scenario_Design.md#d3905efac6f9, 01_Hardness_Manifest.draft.json#a69a0e4fe2ed, 01_Gradable_Surface.json#f17918c8dfc4, __context__#7b0cc66ffd45, __assignment__#e8b8269803d5, __policy__#dc4ab5df3cdd, __gate_policy__#9b78441396d8, __review__#16d4d727890d)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#ca4def2fa591, 00_Assigments.md#4844ae9f5ae7, 01_Grounding_Dossier.md#2ed958107b88, 01_Universe_Inject.sql#4c6328ab2e86, __context__#7b0cc66ffd45, __assignment__#e8b8269803d5, __policy__#dc4ab5df3cdd, __gate_policy__#9b78441396d8, __review__#16d4d727890d)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 1/1 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 33/33 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 12/12 items carry a source pointer (min 100%)
[PASS] evidence.dates: 7/7 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 12/12 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 12 facts proven findable by persona_view search as julia_lawson
[PASS] reach.brief: 13 scoped load-bearing ids YES for julia_lawson
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.accepted_outcomes: V3 accepts multiple fair outcomes; see v3.fair_outcomes_review
[PASS] boundary.anchor_naming: 5 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 7 evidenced counter-readings (of 7 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.fair_outcomes_review: current accepted outcomes and considered alternatives recorded; multiple fair outcomes are allowed
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

