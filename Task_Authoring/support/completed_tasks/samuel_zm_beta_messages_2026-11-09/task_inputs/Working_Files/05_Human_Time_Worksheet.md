# Human Time Worksheet — samuel_zm_beta_messages

Pass: first (rev6)        Tier: Long-Horizon
Universe: synth-cut · Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Hours: 21.5

Basis:
- The work 04_Prompt.txt asks for (sha256 22df2abfec65): carry out Leonard's Sep 30 DM, which covers a call on every PNs Beta row and every filed ask, a sheet, a one-page note, ticket comments and moves, new tickets, a checklist, emails and the counts.
- The work is done by hand in Samuel's own accounts: no search, scripts or AI.
- Counts come from rev6 (01_Universe_Inject.sql 6d162cfd1032, solver/truth.json): 36 messages, Go 2, Hold 28, Drop 6. The person doesn't start out knowing where any of them are.
- Friction: none (03_Error_Async_Config.txt), so there is no workaround line.

| Sub-task | Kind (read / dead end / workaround / re-read / write) | Volume (measured, persona view) | Rate | Minutes |
|---|---|---|---|---|
| Read the request, Leonard's DM and the message rule doc | read | 3 records: prompt 547 chars, DM 1322 chars, rule doc 1,462 chars, 6 ordered tests | careful read, the tests are applied 36 times | 20 |
| Read the PNs Beta tab row by row | read | 14 rows, 11 filled columns | about 1 min per row | 15 |
| Skim September Slack where the game is discussed, for corrections and calls | read | 2,025 messages: #zombie-bugs 1,097, #zombie-match3d 485, #zombie-art 275, Arthur DM 89, Vincent DM 39, #company-internal 39, Leonard DM 1 (Samuel is a member of each; seeded rows included) | ≈ 3,000 messages/h (worked-example skim anchor) | 41 |
| Triage Samuel's mailbox for September | read | 36 threads (31 + 1 base, 4 seeded) | ≈ 450 items/h | 5 |
| Read Vincent's QA note and his Phone message checks log | read | 1 email, 6 logged rows | 2 min for the note, 1 min per row plus the header | 10 |
| Triage Samuel's calendar for September and open the notes | read | 11 events (9 base, 2 seeded) | 30 s per event | 5 |
| List Samuel's Drive to find the rule doc, the deck and the log | read | 135 files (24 owned, 108 shared, 3 seeded) | ≈ 450 items/h | 18 |
| Scan the ZM ROADMAP board for test 1 | read | 79 cards on 8 lists | ≈ 450 items/h | 11 |
| Read PR #248 and its review for what the client schedules | read | 1 PR, 18 review comments, 7 reviews | ≈ 40 min (worked-example PR anchor) | 40 |
| Read the client's NotificationManager.cs for the schedule and the days | read | 1 file, 21,075 bytes, 6 scheduled messages | 30 min (dense C#, slower than a document) | 30 |
| Find the Sep 15 cohort week in the warehouse | read | 1 table, 51 Zombie Match rows, 2 needed | 15 min (find the table, read 2 rows) | 15 |
| Each sheet row: ticket, its comments, roadmap list and the client, then run the tests | read | 14 messages on 14 tickets | 12 min each (V1 anchor 8–15 min per record over 2–3 surfaces) | 168 |
| Each ask under the parent: ticket, comments, roadmap list, then run the tests | read | 18 asks on 18 tickets (64 comments across all DES tickets) | 8 min each (low end of the anchor: fewer surfaces) | 144 |
| Each ask found in a ticket comment: run the tests | read | 4 asks | 8 min each | 32 |
| T1 Weekly Leaderboard reset looks finished (Ready, Done, passed) until the review note and the source show it counts from the last leave | dead end | 1 inline comment, 1 code block | ≈ 20 min (decisive-thread anchor) | 20 |
| T2 Lapsed 7 days: the June line gives way to Leonard's Sep 29 reply, which a later calendar note replaces | dead end | 1 thread under a theme post, 1 event note | 25 min (two records, the second in another service) | 25 |
| T3 Finish first mission looks ready until the trigger is joined to where our own ask runs | dead end | 2 source files, 1 post with its reply | ≈ 20 min | 20 |
| T4 Plague Race reads as passed until Vincent's reply in a DM thread under a build request | dead end | 1 thread reply, checked against the QA note | ≈ 20 min | 20 |
| T16 Lives recharged reads as passed until Vincent's post after iOS 0.3.49 | dead end | 1 channel post, checked against the log | 15 min | 15 |
| T5 The Win & Collect row has no child ticket until the live-ops page maps it to a ticket under another name | dead end | 1 page, 1 ticket | 15 min | 15 |
| T6 Asks outside the parent: triage the ZOM tickets by title, then follow the links from the child tickets and read the comments | dead end | 114 ZOM tickets filed Aug–Sep (59 + 55), 4 opened | 15 min at ≈ 450 items/h, then 5 min per ticket opened | 35 |
| T7 Lapsed 14 days reads as new work until the weekly batch and the cancelled review show it's covered | dead end | 1 ask, 1 cancelled event, 1 mail | 15 min | 15 |
| T8 'Unless the roadmap says otherwise': open the BETA list's cards to find what it says about held tickets | dead end | 19 cards | about 1.5 min per card | 30 |
| T9 Older permission-ask records point elsewhere until Robert's Sep 29 post | dead end | 3 Slack records | 5 min each | 15 |
| T10 The readiness deck says six are Ready | dead end | 1 slide | 5 min | 5 |
| T11 The other tabs of the PN sheet look like part of the list | dead end | 2 tabs: PNs 7 rows, PN BETA Translated 16 rows | 10 min (compare headers and titles, Domino copy) | 10 |
| T12 Brian's 'send all the Ready ones' post | dead end | 1 post | 5 min | 5 |
| T13 ENG-2311 looks like the event messages are built | dead end | 1 ticket on another game | 5 min | 5 |
| T14 Red-dot tickets read like asks | dead end | 2 tickets (ZOM-471, ZOM-539) | 5 min | 5 |
| T15 Rate Us and the permission popup read like messages | dead end | 1 card, 1 ticket | 5 min | 5 |
| Go back over calls that a later record overturned | re-read | 4 findings: Plague Race, Lives recharged, the Lapsed 7 line, the Hold state | about 4 min each | 15 |
| Create the sheet in Samuel's folder and enter one row per message | write | 1 sheet, 36 rows × 7 columns | 5 min setup + 3 min per row | 113 |
| Write the one-page note: D1 and D7 per platform, the lapsed days, the four built Holds with why | write | 1 doc, 3 parts | 45 min | 45 |
| Leave the call as a comment on each ticket | write | 32 comments | 5 min each (low end of the V1 anchor: reuses the sheet's reason) | 160 |
| Move each Hold and Drop ticket to match | write | 30 ticket moves, Holds also unassigned | 2 min each (no text) | 60 |
| New tickets: the four asks with none, and the string ticket | write | 5 tickets | 6 min each | 30 |
| Checklist of the Go messages on the push notifications card | write | 1 checklist, 2 items | 2 min each | 6 |
| Email each person who asked about their asks | write | 8 emails | 7 min each (a join of their asks and calls) | 56 |
| Count the 36 calls and tell Leonard in the DM | write | 1 message, 3 counts | 6 min | 6 |
| Total | | | | 1290 = 21.5 h |

Tier check: in band (Long-Horizon ≈ 12–24 h; 21.5 h). No trigger.
- Re-measured in this run: 2,025 Slack messages, 114 ZOM tickets, 79 cards, 36 messages, 32 tickets.
- The manifest's call budget is 202. The rev5 pre-check made 188 calls (185 counted) on a near-identical job.
- Most of the hours are 36 manual decisions and about 85 per-record writes, which an agent makes in far fewer steps.

Baseline count basis (post-baseline only): n/a (first pass)

Condensed breakdown (one line per sub-task group, facts only; the human types the reasoning in their own words):
- Rules: DM, rule doc, PNs Beta tab, QA note and log 45 min
- Slack skim: 2,025 September messages at 3,000/h 41 min
- Listings: 36 mail threads, 11 events, 135 Drive files, 79 roadmap cards 39 min
- Client: PR #248 with its review, NotificationManager.cs 70 min
- Warehouse: Sep 15 cohort week 15 min
- 36 messages through the six tests, 8 to 12 min each 344 min
- 16 traps: wrong day, replaced headline, reach, two withdrawn passes, other-name ticket, asks outside the list, day 14, Hold rule, older posts, deck, tabs, decoys 245 min
- Re-reading 4 overturned calls 15 min
- Sheet 36 rows and one-page note 158 min
- 32 comments, 30 moves, 5 tickets 250 min
- Checklist, 8 emails, reply to Leonard 68 min
- Total 1,290 min = 21.5 h

Condensed breakdown length: 733 characters (field accepts 50–2,000)

Sources measured: hg.py and persona_view.py, listed here.
- hg.py search search slack '.' --key ts with --file messages/CHANNEL/2025-09.json for C0880U9751A, C08R27X0EAH, C08R8CHB0QL, D06UFE81RF0, D06KV30TPL4 and C05KNDCHAAG; hg.py search files slack D06L58XCVKK shows no September file, so its one message is seeded.
- persona_view.py can-see samuel_turner slack, run for each of those channels and D06L58XCVKK, D06KPMDV2JZ: YES for each; persona_view.py reach samuel_turner --json: mail threads by month, calendar events by month, Drive owned and shared.
- hg.py search search trello 6851a6569f3bf818760632ab --pointer /cards --key idBoard and --pointer /lists; hg.py search search trello 6851a674975da1fe76e70d93 --pointer /cards --key idList.
- hg.py search search linear team_ZOM --pointer /issues --key team_id, joined to created_at 2025-08 and 2025-09.
- hg.py search search github 'harmonygames-Games/match3d#248#rc_' and '#rev_' --key id; hg.py search files github Notifications/NotificationManager.cs.
- hg.py search get gsheets --file data.json --pointer /sheets_spreadsheets/220/sheets/0 and /1; the tab at /2 counted with hg.py search search gsheets --pointer.
- hg.py search search snowflake zombie_match_3d --pointer /tables/10/rows --key game_id, and 2025-09-15 --key cohort_week.
- 01_Universe_Inject.sql rows (rev6), parsed with tools/base_check.parse_sql, never run: 7 Slack messages, 4 Samuel threads, 2 Samuel events, 33 DES issues, 64 DES comments, 4 ZOM comments.
- Raw figures: plan/humantime_measured.json.

## Self-review

Walked against `10_Long Horizon Guidelines - V2.md` §5 and §10, the Pre-QC list in `9_Common Errors & Pre-QC - V2.md` (line 237), and the field rules in the playbook, in that order. §5 asks for dead ends, a workaround if forced, re-reading, and no learning the universe from scratch: covered below. §10 and Pre-QC ask for a sub-task justification whose arithmetic adds up: the script computes the sum, so it can't drift.

| Check | Counter-reading | Evidence | Result |
|---|---|---|---|
| Inflated | the 344 minutes of per-message work double-count the Slack skim and the source read | the skim finds corrections, and the per-message line reads each ticket's own comments (64 DES comments, 01_Universe_Inject.sql) and runs the tests. Asks use the 8-minute low end of the V1 anchor for that reason | holds |
| Inflated | 32 comments at 5 min is high when the reason is already on the sheet | 5 min is the low end of the 5–10 min anchor; the V1 evidence averages about 6 min across 95 writes; the 32 comment targets are the tickets in 01_Universe_Inject.sql | holds |
| Solution-path estimate | the dead ends assume the person knows where the corrections sit | all 16 traps in 01_Hardness_Manifest.json have a line (T1 to T16), and the Slack skim is the unguided path to them; friction is none, so no workaround applies (03_Error_Async_Config.txt) | holds |
| Evaluator-wide volume | Slack, mail, calendar and Drive counts could include what Samuel can't see | persona_view.py can-see returned YES for all eight channels; mail, calendar and Drive come from persona_view.py reach samuel_turner, so the counts are his own view; the 3 seeded Drive files are not in the base, so plan/checksql.txt (persona_view.py check-sql) shows them visible instead | holds |
| Tier mismatch | 21.5 h sits close to the top of 12–24 h, so scope might be over the tier | in band with no trigger; the volumes in plan/humantime_measured.json were measured in this run, and the number was not tuned toward the band | holds |
| Linter reading | from the prompt and SQL alone, 36 messages might not justify the hours | 04_Prompt.txt names a sheet, a note, ticket work and emails, and 01_Universe_Inject.sql shows 33 tickets and 68 comments. With 36 decisions and about 85 writes, 21.5 h is well inside 3× of a defensible figure, and the condensed lines name the volumes | holds |
| Re-verification | volumes could be carried over from an earlier stage | every volume in Sources measured was taken in this run through hg.py or persona_view.py; none comes from the dossier | holds |

Unresolved: first pass, so no Oracle Events or baseline refresh yet. Refresh after 08_Oracle_Events.md exists and again after the baseline. Rates beyond the two anchor tables are judgment, stated per row. Field length and banned phrases are for the human to check when typing.

```
STAGE GATE humantime: PASS — Task_Authoring/task_inputsK · 05_Human_Time_Worksheet.md#c71d05473414 · 04_Prompt.txt#c3f8859dd772 · 00_Assigments.md#55f6d8057880 · 08_Oracle_Events.md#e3b0c44298fc · 07_Baseline_Trajectories#ad7848c1ad99 · __context__#72168f70a409 · __assignment__#3adec6ac02d7 · __policy__#dc4ab5df3cdd · __gate_policy__#115714063000 · __review__#95f1481dfb3c · blocking 0 · warnings 0 · checks 17
[PASS] assignment.v3_context: Samuel Turner / Game Designer; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 05_Human_Time_Worksheet.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 00_Assigments.md, 08_Oracle_Events.md, 07_Baseline_Trajectories)
[PASS] chain.prompt-check: upstream 'prompt-check' PASS pasted and current (04_Prompt_Check.md#1816abba50a8, 04_Prompt.txt#c3f8859dd772, 04_Prompt_Writing_Brief.md#e2bf2822817a, __context__#72168f70a409, __assignment__#3adec6ac02d7, __policy__#dc4ab5df3cdd, __gate_policy__#115714063000, __review__#672901990199)
[PASS] structure.placeholders: no placeholders in 05_Human_Time_Worksheet.md
[PASS] structure.arithmetic: 39 sub-tasks sum to 1290 min = 21.5 h
[PASS] evidence.volumes: every sub-task has a measured volume
[PASS] structure.kinds: dead-end / workaround / write lines present
[PASS] structure.field_length: condensed breakdown 733 characters
[PASS] evidence.sources: volume sources name the hg.py / persona_view queries
[PASS] structure.tier_check: tier check line present
[PASS] review.counter_readings: 7 evidenced counter-readings (of 7 found; need ≥ 5) in 05_Human_Time_Worksheet.md
[PASS] review.coverage: self-review addresses all 5 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```
