## HARDNESS REPORT (Opus observed)

Scope: chat review, attempt workspace; mode OPUS_OBSERVED; review date 2026-11-11; spec `Evals/1A_Hardness_Eval.md` (model-aware-v3); universe Oct 1, 2025 (synth-cut), `Evals/references/universes/synthcut/universe_manifest.json`.
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

### Reviewed inputs and provenance

| Input | Path | SHA-256 |
|---|---|---|
| Prompt | Evals/task_inputs/04_Prompt.txt | db5743eabc4434d8486f8b8feab67a44d51791d84b9edfd9c1b1511c95969ff1 |
| Assignment (platform record) | Evals/task_inputs/00_Task_Assigned_Inputs.md | 470b5576a2929e2fe1c75459001d6bcfdb259cc412214edaf88d9ecab7a37d7e |
| Injection SQL, current saved version (revision 6) | Evals/task_inputs/01_Universe_Inject.sql | c037dd89736e83e0ca136aaa14985b8e2b7524f74a56b423a7480bb3cc421197 |
| Opus run (raw bytes, uploaded `trajectory-run-1 (4).json`, saved as opus revision 8) | Evals/task_inputs/opus/trajectory.json | c57e71e21d1351d19b8dfa72075dd71f39bdac58a0fa706567f4506cc9cec589 |
| Reference files | none used by the prompt | N/A |

Run identity: all 249 assistant events, the init event and the result's `modelUsage` carry `claude-opus-5-5`; session 349c5918-1822-4142-ac18-b5d92d3dd516, permission mode bypassPermissions, `terminal_reason: completed`, 216 turns, no sub-agents. Model: CONFIRMED Opus.

Unhinted status: the export has no initial user-prompt event (the stream starts with the assistant). The run's behavior fits the bare prompt: it finds Frederick's DM by searching (index 2-9) and there is no hint text in the export. Recorded as an evidence limit, not a confound.

Source version: the run matches the **current** saved SQL. The current-only wording appears in its tool results: DES-334 "Their message today about that zip is the zombie package, not the chick." (index 82) and DES-409 "Waiting on the .ttf files from Martin." The earlier-only wording ("Need the .ttf files") appears 0 times. The confound in the previous report (an older injection) is resolved.

### Requirement map (authority_contract: prompt-incorporation-v1)

Chain: prompt ("do everything he's asking for") → Frederick's DM D05SD5QLG94 ("My hand-off notes say what goes in the brief, what counts as ready, what to do with the tickets and who gets the files") → hand-off notes f_8c1d0bca1d1d5fde4c5008 (rules on brief contents, states, "if someone who knows the file or the art has said something since, that counts", the art-change rule, the sound rule, tickets and sharing) → design page (Confluence ZM3D GDD). All of these are incorporated, and no unincorporated rule is used below.

| # | Requirement | Expected | Observed (export index) | Outcome |
|---|---|---|---|---|
| R1 | Find the DM, notes, pack list and tickets | D05SD5QLG94; f_8c1d0bca1d1d5fde4c5008; f_956e60ec7f2f7977d98934; DES-313 children | 9, 20, 24, 37, comments on all 96 tickets (41-237) | MET |
| R2 | Brief: scenario and purpose | Scenario 1, filter out players who won't like the core game | Brief §2 (445) | MET |
| R3 | Brief: 8 board items plus extras | Grenade, Couch, Plushie Chick, Shuriken, Cute Axe, Gift Box, Cactus Plant, **Bow** (Robert's Sep 26 swap) | Exactly these; "Bow replaced Dynamite"; extras stated (445) | MET |
| R4 | Brief: 4 zombies, 1 animation | Party Girl, Plumber, Magician, Football Player; walk | Same (445) | MET |
| R5 | Brief: win/lose, tray slots | Win = all zombies eliminated; lose only when HP runs out; 7 slots, full tray not a loss | Same (445) | MET |
| R6 | Brief: sound use, music start | Own files only; music after first tap | Same, rocket/explosion withheld (445) | MET |
| R7 | Brief: start date | Nov 3 | Nov 3 (445) | MET |
| R8 | Sheet: 96 rows, 7 columns, Line/Category/Ticket as listed | 96 rows | 96 rows, correct headers (442) | MET |
| R9 | Board set column | 8 Default incl. Bow; 76 Extra; 12 blank | Exactly this (442) | MET |
| R10 | 8 Delivered | Couch, Couch and Pillow, Grenade, Plushie Bunny, Plushie Chick, Cannon, Background, Zombie characters | Same (442) | MET |
| R11 | Brian's 12 Thursday saves (Alarm Clock, Record Player, Retro TV, DES-361..369) | Owed, Brian: Marcus, #zombie-match3d C0880U9751A, msg a5ee6e90923eeab380e6730f674240d2 (SQL line 55): "the models you got out of unity on thursday are the text kind … youll need to redo them"; PlayableX takes Binary FBX only | All 12 **Ready** (442). The run never read C0880U9751A; its "ASCII" search (260) returned only the PlayableX format message; "text kind" appears 0 times in the export | MATERIAL_FAIL (C1) |
| R12 | 12 bathroom lines DES-348..359 | Owed, Claire: Robert's DM D05GU6L0XFH, msg 8a1b1c6d448eecb7ccc81f796c95d5ce (SQL line 59): "the bathroom files she gave <@Brian> on Friday are the old version too" | All 12 **Ready** (442). The run never opened D05GU6L0XFH (it saw only an unrelated Robert message there in a search result, index 9/277); "bathroom files she gave" appears 0 times | MATERIAL_FAIL (C2) |
| R13 | 8 instruments DES-379..386 | Owed, Brian: outgoing-folder doc f_faf4d7c167d14a1127dcc3 (SQL line 17): zip "got cut off on upload … those eight aren't in the folder any other way" | All 8 **Ready** (442). The doc was never opened (its id appears 0 times); Drive searches were only "hand-off", "playable", "sound" and "brief" | MATERIAL_FAIL (C3) |
| R14 | Cactus Plant, Chainsaw, Cone | **Ready**: same doc, "Claire sent the three recoloured models again … they replace Thursday's" | **Owed**, Claire, "re-export" based on PR #462 and Robert's Sep 29 note (442, 496-504) | MATERIAL_FAIL (C3, same unread record) |
| R15 | 6 not yet sent / 5 still Brian's / Item visuals, UI / Fonts | Owed with Claire / Brian / Brian / Martin | Same, correct owners and descriptions (442) | MET |
| R16 | Sounds | Rocket, Explosion (library/bought pack), Background music Owed (Calvin); Matching, Success, Failure Ready | Same (370, 442) | MET |
| R17 | Owed tickets → Todo + comment; Delivered/Ready untouched | 49 moves + 49 comments | 20 moves + 20 comments, all succeeded (470-548). 17 correct; 32 Owed tickets untouched (C1, C2, C3); 3 Ready tickets wrongly moved (DES-323, DES-336, DES-389, C3) | MATERIAL_FAIL (knock-on of C1-C3) |
| R18 | Counts in Frederick's DM | Delivered 8 / Ready 39 / Owed 49 | 8 / **68** / **20** (551) | MATERIAL_FAIL (knock-on of C1-C3) |
| R19 | Share both files view-only | Frederick, Brian, Robert (kickoff hold), intake@playablex.ai (Contacts) | Exactly these 8 reader shares (453-467) | MET |
| R20 | Post both links in the PlayableX channel | C08H78VJG80 | Posted with both links (553); its "20 lines are still owed" is wrong (knock-on) | MET (delivery); content knock-on counted under R18 |
| R21 | Files in Julia's Drive as a Doc and a Sheet | Native Doc and Sheet | Created (433, 445) | MET |

Agent visibility of the deciding records (checked independently): Julia (EMPLOYEE_0005) is a member of C0880U9751A #zombie-match3d (`slack/channels.json` /108) and of DM D05GU6L0XFH (/450). The outgoing-folder doc is shared with julia.lawson@harmonygames.co as reader (SQL line 12). The notes define Ready as "sitting in the outgoing folder", and every Brian note says "In the outgoing folder", so a Drive search for "outgoing" finds the doc. None of the three misses is a task or environment defect.

### Grouped failures and independent causes

- **C1: Marcus's "text kind" note never found.** 12 Thursday saves marked Ready instead of Owed with Brian; 12 tickets not moved; counts off by 12. Deciding record: a5ee6e90… in #zombie-match3d.
- **C2: Robert's bathroom-UV DM never read.** 12 bathroom lines marked Ready instead of Owed with Claire; 12 tickets not moved; counts off by 12. Deciding record: 8a1b1c6d… in D05GU6L0XFH.
- **C3: Brian's outgoing-folder doc never opened.** 8 instruments marked Ready instead of Owed with Brian (8 tickets not moved). The same doc's Sep 30 re-send entry was also missed, so Cactus Plant, Chainsaw and Cone went to Owed instead of Ready (3 tickets wrongly moved to Todo with wrong comments). This is one cause: one unread record.

The three causes rest on different records in different services or channels, so a run could make any one without the others. Total: 35 of 96 sheet rows in the wrong state, 35 of the 52 ticket decisions wrong, Ready and Owed counts wrong, and the channel post's "still owed" figure wrong.

### Narrow miss

Narrow miss: NO. 3 independent causes (C1, C2, C3). Failed share about 40% of the weighted core answer: 35/96 rows (about 13% of the weight), 35/52 ticket decisions (about 13%), 2 of 3 counts (about 7%), the still-owed list in the post and DM (about 5%). The brief (about 25%) and the deliveries are correct. The share rests on 96 line states, 52 ticket decisions, 3 counts and 7 brief elements. Difficulty mode: Hard, loss 30%.

### Failure-pattern risk

Failure-pattern risk: NO. Traps and this run's outcome:
- ASCII Thursday saves (Marcus): about 13%, wrong
- Bathroom old version (Robert DM): about 13%, wrong
- Outgoing doc: instruments zip and recoloured re-send: about 12%, wrong
- Board swap Bow for Dynamite: about 5%, right
- Sound licensing (rocket/explosion): about 4%, right
- Loss rule and 7-slot tray: about 3%, right
- Chick/duck delivered (DES-334): about 1%, right

Largest share about 13%, under 30%. The run split right and wrong across traps.

### Tool calls

Tool calls: 215 (215 by the main agent, 0 by sub-agents; both count). Task type: long-horizon; minimum 100 on average; 90% threshold 90. Not under 90% of the minimum.

### Correct work and usability

The brief is fully correct and usable: Scenario 1 and its purpose, the 8 items with Bow, the extras, the 4 zombies and walk, the win/lose rule with the 7-slot tray, the sound rule with music after the first tap, Nov 3 and the formats. The Board set column is fully correct, and so are the Delivered set, the sound rows, the 2D/fonts rows, the 11 not-yet-sent/Brian lines and their owners. Shares go to exactly the right four recipients, view-only, and both links are posted in the PlayableX channel. All 20 ticket writes succeeded. The run also caught the Bow swap, which the previous run missed.

### Task / environment defects

None found. The only errored call was a benign search syntax error (index 4). Every deciding record is in the run's environment version and visible to Julia.

### Unassessed scope

None material.

### Score rationale

Score 4 (Hard). Three independent genuine retrieval failures put 35 of 96 line states in the wrong state. As a result, Frederick got wrong Ready and Owed counts (68/20 instead of 39/49), 32 of 49 Owed tickets were never moved, 3 Ready tickets were wrongly moved, and PlayableX was told 20 lines are owed instead of 49. Fixing this means substantial correction across the sheet, tickets, DM and channel post, so it is not a bounded fix: that rules out 3. It is not 5 because substantial correct work remains usable: the brief, one of the two deliverables, is entirely correct; the sheet's structure, Board set column and 61 of 96 states are right; and every share and post went to the right place. The central result is partly wrong, not invalidated.

### FINAL VERDICT: NON-FAIL
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Assessment version: model-aware-v3
Assessed model: Opus
Assessment mode: OPUS_OBSERVED
Score: 4
Execution status: COMPLETE
Difficulty: Hard
Gate decision: PROCEED
Gate reason: OBSERVED_OPUS_FAILURE
Evaluator model: Opus 5.5 (claude-opus-5-5), session effort
Next action: Proceed with dependent authoring (/oe, /rubric) using Delivered 8 / Ready 39 / Owed 49; retain C1-C3 as observed failure evidence.
Evidence limits: One run only; no average-score or repeatability claim. The export omits the initial user-prompt event.
