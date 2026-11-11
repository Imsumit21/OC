# Human Time Worksheet — calvin_qm_epic

Pass: first, rebuilt for rev3        Tier: Long-Horizon
Universe: synth-cut · Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Hours: 19.25

Basis:
- The work 04_Prompt.txt asks for (sha256 edefd55c0ff5): set up the Queue Manager epic the way Brian's message of yesterday asks, with the children and report lines in Linear, the stock-take sheet in Calvin's folder shared with the review invite, a slide with the numbers, and the numbers back to Brian in the DM.
- The work is done by hand in Calvin's own accounts: no search, scripts or AI. Calvin's today is Wednesday Oct 1, 2025; windows are Pacific dates. Learning the universe from scratch is not counted.
- Counts come from rev3 (01_Universe_Inject.sql sha256 479b8441f52e; solver/truth.json) and the platform /prompt report on rev3 (Working_Files/platform_reports/prompt_rev2_PASS.md): 39 reports, 10 children, 17 new sub-issues, 22 moves with 8 state changes, 22 notes, 49 sheet rows, 5 shares, 1 slide, 1 message.
- The person does not start out knowing which records decide a call. Finding them is the skim work below, and each designed trap in 01_Hardness_Manifest.json has its own dead-end line, which costs only the extra misleading records. 03_Error_Async_Config.txt is Friction: none, so there is no workaround line.

| Sub-task | Kind (read / dead end / workaround / re-read / write) | Volume (measured, persona view) | Rate | Minutes |
|---|---|---|---|---|
| Read Brian's message and what it points to: the DM, his note on the Queue Manager ticket, Vincent's pass sheet (38 rows) and its legend, Arthur's note on QA passes, the review invite, Calvin's folder and deck | read | 8 records | 5 min each | 40 |
| Skim #builds for Sep 15 to Sep 30, 2025 PT: which branch each build came from | read | 706 messages (C05433XK267) | ≈ 3,000 messages/h | 14 |
| Skim the other ZM conversations for the same window: #zombie-bugs, #zombie-match3d, #zombie-prs and Calvin's DMs with Brian, Vincent and Marcus | read | 1520 messages (#zombie-bugs 448, #zombie-match3d 321, #zombie-prs 449, Brian DM 79, Vincent DM 102, Marcus DM 121) | ≈ 3,000 messages/h | 30 |
| Triage Calvin's September inbox for the review invitations and GitHub review mails | read | 51 threads (49 base in 2025-09 per persona_view reach + 2 seeded invitation threads in calvin.price@harmonygames.co) | ≈ 450 items/h (triage by sender and subject) | 7 |
| Scan the ZOM tickets for ones that already hold a report | read | 571 ZOM tickets (553 base + 20 seeded) | ≈ 450 items/h (triage by title) | 76 |
| List the match3d PRs opened since Sep 15 | read | 46 PRs of 477 | ≈ 450 items/h | 6 |
| Find the review card on the ZM ROADMAP board and read its history | read | 80 cards (idShort 1 to 79 in base + the seeded card 80), 4 actions on the card | ≈ 450 items/h (11 min), plus 6 min for the card and its 4 actions | 17 |
| Confirm what the four PRs the reports lean on contain: summary, merge, reviews, review comments, conversation | read | 4 PRs (#465, #472, #473, #475) | ≈ 40 min (the worked example's 'find a handful of PRs and confirm what each contains') | 40 |
| Per report: the sheet row, its re-test code against the legend, the re-test build's branch in #builds, the fix against the PR, any later word on it, then the status under Brian's note | read | 39 reports (38 sheet rows + 1 from a DM), 15 builds cited | 8 min each (low end of the cohort-record anchor 8–15 min) | 312 |
| Per existing ticket: read the ticket, Vincent's note and any reply, and compare its state with the status | read | 22 tickets (ZOM-567 to ZOM-586, ZOM-556, ZOM-560), 32 notes | 3 min each (one ticket, no second surface) | 66 |
| T_BRANCH three 'ok, chat' rows look passed until the chat names build #1718 and #builds shows it came from a feature branch | dead end | 3 rows, 3 records | 15 min | 15 |
| T_INLINE the season pass icon row looks fixed by a merged PR until the reviewer's comment on it | dead end | 1 row, 3 records | 15 min | 15 |
| T_INLINE_PACK the pack sound row looks fixed by a merged PR until the reviewer's comment on it | dead end | 1 row, 2 records | 10 min | 10 |
| T_REOPEN a passed row comes back in a reply under an unrelated thread, on a newer build | dead end | 1 row, 2 records | 10 min | 10 |
| T_BACK another passed row comes back in a founder's channel post, on the same newer build | dead end | 1 row, 2 records | 10 min | 10 |
| T_ELSE four rows with no fix named turn out to be in another dev's merged PR, by his comment on it | dead end | 4 rows, 2 records | 15 min | 15 |
| T_FILT the sheet looks like the whole list until a teammate's DM adds a report | dead end | 1 DM, 2 messages | 10 min | 10 |
| T_ALIAS_GIFT the day counter row has no ticket in the sheet until Vincent's note on an older ticket | dead end | 1 row, 2 records | 10 min | 10 |
| T_ALIAS_STREAK the freezer row has no ticket in the sheet until Vincent's note on an older ticket | dead end | 1 row, 2 records | 10 min | 10 |
| T_GATE the review reads as Friday with Daily Gift until the changed card and the updated invitation | dead end | 4 records | 15 min | 15 |
| T_PARK the input blocker reads as a report until Brian's line parking it | dead end | 2 messages | 5 min | 5 |
| T_SHARE the sheet reads as for Brian and Vincent until the invite's attendee list | dead end | 1 event, 6 attendees | 5 min | 5 |
| T_FIELDS new sub-issues read as needing a priority and an owner until the note | dead end | 1 note, 1 message | 5 min | 5 |
| T_STATE three tickets' own states read as where the report stands | dead end | 3 tickets | 5 min | 5 |
| D_DDRULE the DD hotfix note read as the rule for passes | dead end | 1 doc | 5 min | 5 |
| D_QMCARD the ticked Queue Manager roadmap card read as the work being done | dead end | 1 card | 5 min | 5 |
| D_SKIP Oliver's skip tutorial exceptions read as reports | dead end | 1 post | 5 min | 5 |
| D_ICONVFX Vincent's chat remark about the pass icon read as another report | dead end | 1 message | 5 min | 5 |
| D_CANVAS the Bug Checklist and Collect & Win canvases opened as part of the list | dead end | 2 canvases | 5 min | 5 |
| D_COINDM Brian's own coin line read as a second report | dead end | 1 message | 5 min | 5 |
| D_432 ZOM-432 read as the daily gift ticket | dead end | 1 ticket | 5 min | 5 |
| D_OLDINVITE the first invitation read as the current one | dead end | 1 mail | 5 min | 5 |
| D_DDQUEUE the DD queue manager tickets read as belonging under the epic | dead end | 1 ticket family (ENG-2069) | 5 min | 5 |
| Redo the calls a later record overturns (rows 1, 2, 25, 9, 29, 12, 32, 13, 38) | re-read | 9 calls | 2 min each | 18 |
| Tally the five numbers and the per-area open counts from the finished list | read | 39 rows, 10 areas, 5 figures | 10 min | 10 |
| Create the area children under the Queue Manager ticket, with the right state | write | 10 tickets | 3 min each, under the 5–10 min tailored-write anchor because the title is the area name | 30 |
| File a sub-issue for every report no ticket holds: copied title, parent, state | write | 17 tickets | 3 min each (title copied, no description) | 51 |
| Move each existing ticket under its child and fix the state where it differs | write | 22 moves, 8 state changes | 1 min each (one or two fields), plus 3 min to check the 8 changed states | 25 |
| Leave the note with the status and why on each existing ticket | write | 22 comments | 5 min each (low end of the tailored-write anchor) | 110 |
| Create the stock-take sheet in the folder: tab Reports with six columns, tab Areas with three | write | 1 sheet, 39 rows × 6 columns + 10 rows × 3 columns | 5 min setup + 2 min per report row + 1 min per area row | 93 |
| Share the sheet with the review's other attendees | write | 5 shares | 1 min each | 5 |
| Add the slide with the five numbers to the deck | write | 1 slide | 10 min | 10 |
| Message Brian in the DM with the five numbers | write | 1 message | 10 min (tailored-write anchor 5–10 min) | 10 |
| Total | | | | 1155 = 19.25 h |

Tier check: in band (Long-Horizon ≈ 12–24 h; 19.25 h). Reads are 618 min, dead ends 185 min, re-reads 18 min, writes 334 min. Sensitivity, not a tuning: reports at 5 min instead of 8 give 17.30 h; notes and tickets at the 5 min anchor instead of 3 give 20.22 h. The planned call budget floor is 180 (01_Hardness_Manifest.json) and the requester's target is over 130 counted calls per run.

Baseline count basis (post-baseline only): n/a (first pass)

Condensed breakdown (one line per sub-task, facts only; the human types the reasoning in their own words):
- Rules: Brian's DM, his note on the ticket, the pass sheet and legend, the QA-pass note, invite, folder, deck (8 records) 40 min
- Slack by hand at 3,000/h: #builds 706 messages 14 min; 3 ZM channels and 3 DMs 1520 messages 30 min
- Inbox 51 threads 7 min; 571 ZM tickets by title 76 min; 46 PRs 6 min; review card among 80 on the board 17 min; what 4 PRs contain 40 min
- 39 reports (38 sheet rows + 1 from a DM), each against legend, build branch, PR and later posts, 8 min each 312 min
- 22 existing tickets with their notes, 3 min each 66 min
- 23 traps and decoys (branch-build passes, reviewer comments on merged PRs, two bugs that came back, a moved review, tickets under other names, another game's rule) 185 min; redo 9 calls 18 min; tally 10 min
- Writes: 10 children 30 min; 17 sub-issues 51 min; 22 moves 25 min; 22 notes 110 min; sheet 39 + 10 rows 93 min; 5 shares 5 min; slide 10 min; DM 10 min
- Total 1,155 min = 19.25 h

Condensed breakdown length: 938 characters (field accepts 50–2,000)

Sources measured:
- hg.py search search slack '.' --file 'messages/CHANNEL/*.json' --key ts, filtered to Sep 15 to Sep 30, 2025 PT, for C05433XK267 (706), C08R27X0EAH (446), C0880U9751A (320), C093LEZGF6J (446), D0770ET6WBW (76), D06UPGF5PQV (100), D05U73FNDDL (119); scan_complete true on each (plan/measure_humantime.py, plan/out/humantime_volumes.json).
- hg.py search search linear 'ZOM-' --key identifier on data.json: 553 ZOM issues.
- hg.py search search github 'match3d#' --key id --pointer /pull_requests with --key created_at: 477 PRs, 46 opened since Sep 15.
- Trello board 6851a6569f3bf818760632ab: idShort runs to 79 in base (checked at injection and by the platform /injection report); the seeded card 68daad83bacf52c6ea7e1593 is 80.
- persona_view.py reach calvin_price: 49 threads in calvin.price@harmonygames.co with a last message in 2025-09; persona_view.py can-see calvin_price slack returned YES for C05433XK267/1758817549.151639, C08R27X0EAH/1758903616.346579, D0770ET6WBW/1758808795.588519 and D06UPGF5PQV/1758817744.353289 in this session.
- 01_Universe_Inject.sql rows (rev3): seeded messages per conversation (C08R27X0EAH 2, C0880U9751A 1, C093LEZGF6J 3, D0770ET6WBW 3, D06UPGF5PQV 2, D05U73FNDDL 2); 18 seeded tickets ZOM-567 to ZOM-584 and 27 Linear notes; 2 of the 10 seeded invitation threads are in Calvin's mailbox.

## Self-review

Checked in order against 10_Long Horizon Guidelines - V2.md §5 and §10, the Pre-QC 'Difficulty and submission' list and the Screen 25 field rules (0.25 step, 50–2,000 characters, pasting and copying blocked). §5: dead ends, re-reading and no universe learning are in; no workaround applies. §10 and Pre-QC ask that the estimate is justified sub-task by sub-task and adds up, which the gate re-adds; their other items are post-baseline.

| Area | Counter-reading | Evidence that resolves it | Verdict |
|---|---|---|---|
| Inflated | The strongest case it fails: 39 per-report checks plus 23 dead-end lines count the same reads twice | The per-report rate is the low end of the 8–15 min anchor for a record checked across the sheet f_cb40955893624e1acb8500, #builds and GitHub. A dead-end line costs only the extra records, such as harmonygames-Games/match3d#472#rc_1 for the season pass icon row. The re-read line covers the 9 overturned calls only. Tickets are at 3 min, under the 5–10 min anchor, because titles are copied | PASS |
| Solution-path estimate | It could be written as if the person already knew where the deciding records sit, such as Robert's post C0880U9751A/1759268652.552719 or Vincent's reply C08R27X0EAH/1759267212.418339 | The skims (706 + 1520 messages), the inbox, the ticket scan, the PR list and the board come first, and every manifest trap and decoy has a dead-end line. Friction: none, so no alternate path applies | PASS |
| Evaluator-wide volume | Search is evaluator-wide, so the counts could include channels or mail Calvin cannot read | Every Slack count is one conversation Calvin is a member of: persona_view.py can-see returned YES for C05433XK267/1758817549.151639, C08R27X0EAH/1758903616.346579 and D0770ET6WBW/1758808795.588519, and check-sql passed for the seeded rows. The inbox count is his own mailbox, calvin.price@harmonygames.co. Linear, GitHub and Trello are unscoped | PASS |
| Tier mismatch | 19.25 h could sit outside the Long-Horizon band, or the scope could be thin for the tier | The band is about 12–24 h and 19.25 h is inside it; both sensitivities above stay inside it too. 68 Linear writes and 39 per-report calls under ZOM-543 carry the hours, not padding | PASS |
| Linter reading | The V1 reasonableness linter sees only the prompt, the hours, the reasoning and the SQL, and an 80-word prompt could make 19.25 h look 3× too high | The reasoning names the volumes: 38 sheet rows, 39 reports, 22 existing tickets, 27 new tickets, 22 notes, 49 sheet rows, and the SQL shows the records behind them (the 38-row grid of f_cb40955893624e1acb8500, ZOM-567 to ZOM-586). 3× either way is 6.4 h to 58 h. No banned phrase appears | PASS |

Re-verified: every volume in the table came from this run's hg.py queries or the SQL, not from the dossier. The sum and the character count are computed by plan/build_humantime.py.

Unresolved: none blocking. Refresh after 08_Oracle_Events.md and after the baseline (count basis).

```
STAGE GATE humantime: PASS — Task_Authoring/task_inputs · 05_Human_Time_Worksheet.md#71e63771b08f · 04_Prompt.txt#7f9ab6c62396 · 00_Assigments.md#a8cc00ce24ff · 08_Oracle_Events.md#be85999b8fe9 · 07_Baseline_Trajectories#d71c0a69afc1 · __context__#7be566a0936c · __assignment__#d644f7ef43f6 · __policy__#dc4ab5df3cdd · __gate_policy__#cc68bf5564ff · __review__#15d71f843716 · blocking 0 · warnings 0 · checks 18
[PASS] assignment.v3_context: Calvin Price / Game Engineer (Unity VFX); hard cap <70%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 05_Human_Time_Worksheet.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 00_Assigments.md, 08_Oracle_Events.md, 07_Baseline_Trajectories)
[PASS] chain.prompt-check: upstream 'prompt-check' PASS pasted and current (04_Prompt_Check.md#59f72e210c96, 04_Prompt.txt#7f9ab6c62396, 04_Prompt_Writing_Brief.md#b42cfa5ecf15, __context__#7be566a0936c, __assignment__#d644f7ef43f6, __policy__#dc4ab5df3cdd, __gate_policy__#cc68bf5564ff, __review__#28576aab3ad0)
[PASS] structure.placeholders: no placeholders in 05_Human_Time_Worksheet.md
[PASS] structure.arithmetic: 43 sub-tasks sum to 1155 min = 19.25 h
[PASS] evidence.volumes: every sub-task has a measured volume
[PASS] structure.kinds: dead-end / workaround / write lines present
[PASS] structure.field_length: condensed breakdown 938 characters
[PASS] evidence.sources: volume sources name the hg.py / persona_view queries
[PASS] structure.tier_check: tier check line present
[PASS] review.counter_readings: 5 evidenced counter-readings (of 5 found; need ≥ 5) in 05_Human_Time_Worksheet.md
[PASS] review.coverage: self-review addresses all 5 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

