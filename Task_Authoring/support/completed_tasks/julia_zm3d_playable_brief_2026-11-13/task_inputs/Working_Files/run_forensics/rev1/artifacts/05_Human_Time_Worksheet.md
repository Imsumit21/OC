# Human Time Worksheet — julia_zm3d_playable_brief

Pass: first        Tier: Long-Horizon
Universe: synth-cut · Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Hours: 19.00

Basis:
- The work 04_Prompt.txt asks for (sha256 33c721d60945): do everything Frederick's Sep 30 message asks, which covers a brief, a hand-off list with a state for every line of the pack, ticket moves and comments for the lines that are owed, sharing, the count for each state, and the two links.
- The work is done by hand in Julia's own accounts: no search, scripts or AI.
- Counts come from rev1 (01_Universe_Inject.sql 78465cd474f8, solver/truth.json): 96 lines, Delivered 8, Ready 36, Owed 52. The person does not start out knowing where anything is.
- Friction: none (03_Error_Async_Config.txt), so there is no workaround line.

| Sub-task | Kind (read / dead end / workaround / re-read / write) | Volume (measured, persona view) | Rate | Minutes |
|---|---|---|---|---|
| Read the request, Frederick's DM and his hand-off notes | read | 3 records: prompt 246 chars, DM 789 chars, notes 2180 chars with 3 state tests | careful read: the tests are applied to every line | 30 |
| Read Brian's pack list row by row | read | 96 rows, 5 columns | about half a minute per row | 45 |
| Skim Slack where the playable and its assets are discussed | read | 731 messages: the PlayableX channel (all of it) 198, #zombie-design 292, #zombie-art 34, #zombie-match3d 69, #zm-animations 66, DM with Frederick (Sep) 4, DM with Claire 25, DM with Brian 37; 6 seeded (Julia is a member of each) | ≈ 3,000 messages/h (worked-example skim anchor) | 15 |
| Read the vendor's threads past their apparent end: formats and asset list, the pause and the new start, the first playable's sound exchange | read | 3 threads in a channel of 198 messages (119 of them from March and April) | ≈ 20 min each (decisive-thread anchor) | 60 |
| Open each pack ticket, read Brian's note, apply the three tests | read | 97 tickets (the pack ticket and 96 children), 96 notes | 3 min each: one ticket, one short note (below the 8 to 15 min anchor, which is for 2 to 3 surfaces) | 288 |
| List Julia's Drive for the notes, the pack list, the deck and anything else about the pack | read | 191 files (28 owned, 158 shared, 5 seeded) | ≈ 450 items/h | 25 |
| Read Calvin's sound sources sheet and Brian's log of the outgoing folder against the tickets | read | 8 sheet rows, 4 dated log lines | 15 min for both | 15 |
| Find the pull requests since the first zip and confirm what each changed | read | 22 pull requests created 22 to 30 Sep | ≈ 40 min (worked-example PR anchor) | 40 |
| Read the design page and its comments for the tray and the loss rule; the reference-level deck | read | 1 page, 2 comments, 4 slides | 20 min | 20 |
| Find the kickoff hold and its attendees, and the vendor's intake address | read | 1 event with 4 attendees, 1 contact | 10 min | 10 |
| T1 Thursday's exports look ready until a colleague's post is read against the vendor's format rule | dead end | 12 tickets, 1 post, 1 rule message | ≈ 20 min (decisive-thread anchor) | 20 |
| T2 Friday's bathroom files look ready until the artist's message | dead end | 12 tickets, 1 DM message | 15 min | 15 |
| T3 three recoloured models: the note is older than the change | dead end | 3 tickets, 1 pull request with its comment | 15 min on top of the PR search | 15 |
| T7 the zipped instruments: the folder log says the zip will not unpack | dead end | 8 tickets, 1 log line | 10 min | 10 |
| T4 two sounds are not ours to pass on | dead end | 2 tickets, 2 sheet rows | 10 min | 10 |
| T5 the board's eight: the first list against a later reply under another post | dead end | 2 posts, 1 thread of 3 messages | ≈ 20 min (decisive-thread anchor) | 20 |
| T8, T12 stale start dates and the first playable's format rule | dead end | 3 dates, 2 rule messages | 5 min each pair | 10 |
| T9 the six-slot proposal on the design page | dead end | 2 comments | 5 min | 5 |
| T10, T16 the zombie pack 'not exported correctly', the duck and the rocket launcher | dead end | 3 vendor messages, 2 tickets | 5 min each | 15 |
| T11, T17 Leonard's Playable Kickoff card and his Playable Feedback doc | dead end | 1 card, 1 doc | 5 min each | 10 |
| T13, T14, T15 the board on the reference-level deck and earlier board ideas | dead end | 1 slide, 3 messages | 10 min | 10 |
| T18 other objects in the recolour pull requests | dead end | 3 object names checked against 96 lines | 5 min | 5 |
| T19 object tickets with the same titles as pack lines | dead end | 51 tickets under one parent | ≈ 450 items/h, then 3 opened | 10 |
| T6 board set for the lines that are not board items | dead end | 12 lines | 5 min | 5 |
| Go back over the lines each later statement overturns: state, what is owed, who has it | re-read | 39 lines (12 + 12 + 3 + 2 + 8 states, 2 board-set cells) | 2 min each | 78 |
| Type the hand-off list | write | 1 sheet, 96 rows × 7 columns | 1.25 min per row | 120 |
| Write the brief | write | 1 doc, 10 required facts | 60 min | 60 |
| Move each Owed line's ticket to Todo and write its comment | write | 52 state changes, 52 comments | 3 min per ticket (comments repeat within a group) | 156 |
| Share both files | write | 2 files × 4 recipients = 8 shares | 1 min each | 8 |
| Send Frederick the count for each state; post both links in the vendor channel | write | 2 messages | 5 min each | 10 |
| Total |  |  |  | 1140 = 19.00 h |

Tier check: in band (Long-Horizon ≈ 12–24 h; 19.00 h). No trigger.
- Reads 548 min, dead ends 160 min, re-reading 78 min, writes 354 min.
- The manifest's call budget is 261; most of the hours are 96 manual decisions, a 96-row sheet typed by hand and 104 per-ticket writes, which an agent makes in far fewer minutes each.

Condensed breakdown (one line per sub-task group, facts only; the human types the reasoning in their own words):
- Rules and list: the message, the notes, 96 pack-list rows 75 min
- Slack: skim 731 messages at 3,000/h, 3 vendor threads read through 75 min
- 96 tickets, one note each, 3 min each 288 min
- Drive listing 191 files, sound sheet, folder log 40 min
- 22 pull requests, design page, deck, kickoff hold, contact 70 min
- 14 dead ends: notes that look ready, the first board list, stale dates, look-alike tickets and card 160 min
- Re-deciding 39 overturned lines 78 min
- Sheet of 96 rows and the brief 180 min
- 52 ticket moves with comments, 8 shares, 2 messages 174 min
- Total 1,140 min = 19.00 h

Condensed breakdown length: 598 characters (field accepts 50–2,000)

Sources measured: hg.py and persona_view.py, listed here.
- hg.py search search slack '17' --key ts with --file messages/CHANNEL/*.json for C08H78VJG80, C090N54TG79, C08R8CHB0QL, C09ATAJ220H, D05SD5QLG94, D05HMBQUC8Z and D076RBM29JS, and '175' on messages/C0880U9751A/2025-09.json; windows are Pacific days (22 Sep 00:00 PT to 1 Oct 00:00 PT). Scan complete for each.
- persona_view.py can-see julia_lawson slack for those conversations (reach table, YES for each); persona_view.py reach julia_lawson: Drive owned 28, shared 158.
- hg.py search search github '2025-09-' --pointer /pull_requests --key created_at (22 created 22 to 30 Sep); hg.py search search linear ZOM-97 --key parent_id (51).
- 01_Universe_Inject.sql rows (rev1), parsed with tools/base_check.parse_sql, never run: 97 Design-team tickets, 96 notes, 6 Slack messages, 5 Drive files, 1 sheet of 96 rows.
- Raw figures: plan/out/humantime_volumes.json.

## Self-review

Checked in order against `10_Long Horizon Guidelines - V2.md` §5 and §10, the Pre-QC list and the field's own text.

| Area | Counter-reading | Evidence that resolves it | Verdict |
|---|---|---|---|
| Inflated | Three minutes for each of 96 tickets and 156 minutes of ticket writes are padding. | each line has its own ticket and note (DES-314 to DES-409) and every Owed line needs a move and a comment (hand-off notes f_8c1d0bca1d1d5fde4c5008); the per-record rate is below the 8 to 15 min anchor because there is one surface, and the reason is stated on the row | holds |
| Solution-path estimate | The table assumes the person already knows where the six later statements are. | each has a dead-end line (T1, T2, T3, T4, T5, T7) and the places are found by the skim and listing rows: 731 messages, 191 Drive files, 22 pull requests (C0880U9751A/1758906517.912099, f_faf4d7c167d14a1127dcc3) | holds |
| Evaluator-wide volume | The Slack and Drive counts could be universe-wide, not Julia's. | only conversations she is a member of are counted (persona_view can-see YES for C08H78VJG80, C0880U9751A, D05HMBQUC8Z); Drive is her owned and shared files from persona_view reach, plus the seeded files shared with her (f_8c1d0bca1d1d5fde4c5008) | holds |
| Tier mismatch | 19.00 h could sit outside Long-Horizon. | 12 to 24 h is the band; the manifest's call budget is 261 with 96 per-line reads (DES-313); no trigger, nothing tuned | holds |
| Linter reading | From a 46-word prompt and the SQL alone, 19 hours could look more than three times too high. | the SQL shows 97 tickets with 96 notes under DES-313 and a 96-row list (f_956e60ec7f2f7977d98934); the condensed breakdown names those volumes, the 52 ticket writes and the dead ends | holds; the reasoning must name the volumes |

Every volume was measured in this run (sources above); nothing is carried from the dossier. The sum was recomputed by the generator (1140 min) and the character count taken from the condensed lines as printed. Unresolved: none. To refresh after the Oracle Events exist and again after the baseline.

```
STAGE GATE humantime: PASS — Task_Authoring/task_inputs · 05_Human_Time_Worksheet.md#41cf184d7a72 · 04_Prompt.txt#33c721d60945 · 00_Assigments.md#82494197a841 · 08_Oracle_Events.md#e3b0c44298fc · 07_Baseline_Trajectories#ad7848c1ad99 · __context__#3246c54345b9 · __assignment__#70579cebc8fc · __policy__#dc4ab5df3cdd · __gate_policy__#1747d7aa5ab8 · __review__#b62863bc4291 · blocking 0 · warnings 1 · checks 19
[PASS] assignment.v3_context: Julia Lawson / Product Manager; hard cap <70%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 05_Human_Time_Worksheet.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 00_Assigments.md, 08_Oracle_Events.md, 07_Baseline_Trajectories)
[PASS] chain.prompt-check: upstream 'prompt-check' PASS pasted and current (04_Prompt_Check.md#20e6960b5a7d, 04_Prompt.txt#33c721d60945, 04_Prompt_Writing_Brief.md#3d36e5b56261, __context__#3246c54345b9, __assignment__#70579cebc8fc, __policy__#dc4ab5df3cdd, __gate_policy__#1747d7aa5ab8, __review__#3a428aaee74e)
[PASS] structure.placeholders: no placeholders in 05_Human_Time_Worksheet.md
[PASS] structure.arithmetic: 30 sub-tasks sum to 1140 min = 19.0 h
[PASS] evidence.volumes: every sub-task has a measured volume
[PASS] structure.kinds: dead-end / workaround / write lines present
[PASS] structure.field_length: condensed breakdown 598 characters
[PASS] evidence.sources: volume sources name the hg.py / persona_view queries
[PASS] structure.tier_check: tier check line present
[PASS] review.counter_readings: 5 evidenced counter-readings (of 5 found; need ≥ 5) in 05_Human_Time_Worksheet.md
[PASS] review.coverage: self-review addresses all 5 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[WARN] task.folder: the task folder is the bare default `task_inputs`: give each task its own folder (`Task_Authoring/task_inputs<Label>`) and pass it to every command, so two tasks never share one [first-pass check in warn mode: reported, not blocking]
[PASS] handoff.pasted: pasted into the Self-review by --paste
```
