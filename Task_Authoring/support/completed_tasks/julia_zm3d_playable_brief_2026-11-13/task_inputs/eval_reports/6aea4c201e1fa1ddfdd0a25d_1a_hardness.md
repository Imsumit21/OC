## HARDNESS REPORT (Opus observed)

Scope: chat review, attempt workspace; mode OPUS_OBSERVED; review date 2026-11-11; spec `Evals/1A_Hardness_Eval.md` (model-aware-v3); universe Oct 1, 2025 (synth-cut), `Evals/references/universes/synthcut/universe_manifest.json` (sha256 da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a).
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

### Reviewed inputs and provenance

| Input | Path | SHA-256 |
|---|---|---|
| Prompt | Evals/task_inputs/04_Prompt.txt | db5743eabc4434d8486f8b8feab67a44d51791d84b9edfd9c1b1511c95969ff1 |
| Assignment (platform record) | Evals/task_inputs/00_Task_Assigned_Inputs.md | 470b5576a2929e2fe1c75459001d6bcfdb259cc412214edaf88d9ecab7a37d7e |
| Injection SQL (overlay, not executed) | Evals/task_inputs/01_Universe_Inject.sql | 3a76797fbde16ffa560e3bc54794965464db8f8ef38dc1019f8b11df3ceaeddb |
| Opus run (raw bytes, uploaded `trajectory-run-1.json`) | Evals/task_inputs/opus/trajectory.json | 5b6f86829075e16892d59102cba8db21102cc190e9ef3cd8a48d07a0fb942ac7 |
| Reference files | none used by the prompt | N/A |

Run identity: all 309 assistant events carry `model: claude-opus-5-5`; init `model: claude-opus-5-5`, Claude Code 2.1.322, session e936e530-3944-4fec-9299-e7462bf05722, permission mode bypassPermissions. Final deliverable result at export index 833 (`terminal_reason: completed`); later results (840, 846) only acknowledge background timers.

Task/source match: the run's first call searches Slack for "playable" on 2025-09-30 and reads the injected Frederick DM (D05SD5QLG94, ts 1759256494.852159), the injected hand-off notes doc (f_8c1d0bca1d1d5fde4c5008), Brian's injected pack list and DES-313 children. The #zombie-art bow thread parent shows `reply_count: 2`, which is the SQL `UPDATE` at line 61, so the overlay was live in this run.

Unhinted status: the export has no initial user-prompt event (stream starts with the assistant). The run's behaviour fits the bare three-sentence prompt (it finds the DM by searching), and it misses three seeded traps, which is not consistent with hint use. It was supplied by the contributor as an unhinted run. This is recorded as an evidence limit, not a material confound.

Authority: `prompt-incorporation-v1`; evidence contract `stage-evidence-v1`; reused evidence: line-level answer key facts from `Evals/task_inputs/reports/1_prompt.md` re-verified directly against the SQL and base records in this review (NEW verification of every deciding record cited below).

### Requirement map (incorporation chain: prompt → Frederick DM → hand-off notes → design page)

| # | Requirement | Expected | Observed (export index) | Outcome |
|---|---|---|---|---|
| R1 | Find and follow Frederick's message and notes | DM D05SD5QLG94; notes doc; pack list | Read at 9, 49, 53 | MET |
| R2 | Brief: scenario and purpose | Scenario 1, filter out players who won't like the core game | Brief §1 (521) | MET |
| R3 | Brief: 8 board items + extras | Grenade, Couch, Plushie Chick, Shuriken, Cute Axe, Gift Box, Cactus Plant, **Bow** (Robert's Sep 26 swap for Dynamite) | Brief §4 lists **Dynamite**, not Bow (521) | MATERIAL_FAIL (cause C3) |
| R4 | Brief: 4 zombies + 1 animation | Party Girl, Plumber, Magician, Football Player; walk | Brief §5 | MET |
| R5 | Brief: win/lose + tray slots | Win when all zombies eliminated; lose at zero HP; full tray not a loss; 7 slots | Brief §3 (decoy prototype rule avoided) | MET |
| R6 | Brief: sound use + music start | Only our own sounds; music only after first click | Brief §7 | MET |
| R7 | Brief: start date | Nov 3 | Brief §2 | MET |
| R8 | Hand-off sheet: 96 rows, 7 columns, Line/Category/Ticket as on list | 96 rows | 96 rows, correct columns (528) | MET |
| R9 | Board set column | Default = R3's eight; Bow Default, Dynamite Extra | Dynamite Default, Bow Extra (2 cells) | MATERIAL_FAIL (cause C3, knock-on) |
| R10 | Delivered lines | 8 (Couch, Couch and Pillow, Grenade, Plushie Bunny, Plushie Chick, Cannon, Background, Zombie characters) | Same 8 | MET |
| R11 | Brian's Thursday saves (12: Alarm Clock, Record Player, Retro TV, DES-361..369 kitchen) | Owed, Brian: ASCII ("text kind") FBX, PlayableX takes Binary only | All 12 **Ready** | MATERIAL_FAIL (cause C1) |
| R12 | Instruments zip (8: DES-379..386) | Owed, Brian: zip cut off on upload, not in folder any other way | All 8 **Ready** | MATERIAL_FAIL (cause C2) |
| R13 | Bathroom files (12: DES-348..359) | Owed, Claire (UV redo, Sep 29 Turkish DM) | Owed, Claire | MET |
| R14 | Colour versions (Cactus Plant, Chainsaw, Cone) | Owed, Claire | Owed, Claire | MET |
| R15 | Not yet sent / still Brian's / 2D / fonts (14 lines) | Owed with Claire/Brian/Martin | Owed, correct owners | MET |
| R16 | Sounds | Rocket, Explosion, Background music Owed with Calvin; Matching/Success/Failure Ready | Same (Calvin's sources sheet read, 433) | MET |
| R17 | Owed tickets → Todo + comment; Delivered/Ready untouched | 52 moves + 52 comments | 32 moves + 32 comments, all on correct Owed tickets, all succeeded; 20 Owed tickets (C1+C2) untouched | MATERIAL_FAIL (knock-on of C1, C2) |
| R18 | Counts per state in Frederick's DM | Delivered 8 / Ready 36 / Owed 52 | 8 / **56** / **32** (560) | MATERIAL_FAIL (knock-on of C1, C2) |
| R19 | Share both files view-only: kickoff hold attendees + PlayableX intake | Frederick, Brian, Robert, intake@playablex.ai (reader) | Exactly these 8 shares, all succeeded (534-548) | MET |
| R20 | Post both links in the PlayableX channel | C08H78VJG80 post with both links | Posted (568) | MET (content reflects wrong sheet) |
| R21 | Files in Julia's Drive as Doc + Sheet | Native Doc and Sheet | Created by Julia (519, 521) | MET |

Output capability: creation, sharing, ticket writes and Slack posts are SUPPORTED and were all executed successfully; no capability-caused miss.

### Grouped failures and independent causes

- **C1: Marcus's ASCII note never found.** Deciding record: injected Slack message a5ee6e90923eeab380e6730f674240d2 in #zombie-match3d (C0880U9751A, 2025-09-26 17:08 UTC, SQL line 55): "the models you saved out of unity on thursday are the text kind ... the ones from <Claire> are ok". With PlayableX's base-data format note ("Binary, not ASCII", seen 31 times in the run and even written into the brief §8), and the notes' Ready rule ("exported in a format they take") plus "if someone who knows the file ... has said something since, that counts", these 12 lines are Owed with Brian. Julia is a member of C0880U9751A (channels.json). The run never read that channel's history and no search matched (string "text kind" and ts 1758906517 appear 0 times in the export). Affects 12 sheet rows, 12 ticket moves and comments, both counts.
- **C2: Brian's outgoing-folder doc never opened.** Deciding record: injected Drive doc f_faf4d7c167d14a1127dcc3 "Outgoing folder - what's in it" (shared with Julia as reader, modified 2025-09-30, SQL lines 12/17): "the zip with Friday's music instruments got cut off on upload ... those eight aren't in the folder any other way". Brian's ticket notes for DES-379..386 say "Zipped with the other instruments, in the outgoing folder", pointing to it. The run's only Drive searches were "playable", "Domino playable", "audio", "Universal Sound", "sound"; the doc id appears 0 times. Affects 8 rows, 8 ticket writes, counts.
- **C3: Robert's board swap thread never opened.** Deciding record: injected reply 1d55b38831d7517fe403e4f2a906a897 in #zombie-art (C08R8CHB0QL, 2025-09-26 21:41 UTC, SQL line 56): "Let's have it in the 8 in place of the last one on my list" (Dynamite → Bow), under Julia's own "Can we have arrow to go with the bow?" thread. The run saw that parent with `reply_count: 2` at index 349 but never called `slack_read_thread` on it, and its Robert search was limited to after 2025-09-29. Frederick's DM makes Robert's later changes binding. Affects brief §4 and two Board set cells.

Three independent causes: different items, different deciding records in three different places (a Slack channel, a Drive doc, a Slack thread). Any one could be missed without the others.

### Narrow miss

Narrow miss: NO. Independent causes: 3 (C1, C2, C3). Failed share: about 35% of the weighted core answer. It rests on about 22 core items: the 96 line states grouped by deciding record (10 groups), the 8 brief elements, the Board set column, the ticket writes, the counts reply, shares, the channel post and the final response, with the counts and Owed ticket writes weighted as central. 20 of 96 lines wrong (21%), 20 of 52 ticket writes missing (38%), the counts wrong in both the DM and the final response, and 1 of 8 brief elements wrong. Difficulty mode: Hard, loss 30%. With three causes the narrow-miss rule does not apply.

### Failure-pattern risk

Failure-pattern risk: NO. Largest trap share: about 18%.

| Trap (deciding record) | Share if missed | This run |
|---|---|---|
| T1 ASCII Thursday saves (Marcus, #zombie-match3d Sep 26) | ~17% | Wrong |
| T2 Bathroom UV redo (Claire DM D05HMBQUC8Z Sep 29, Turkish) | ~17% | Right |
| T3 Instruments zip cut off (outgoing-folder doc Sep 30) | ~12% | Wrong |
| T4 Board swap Dynamite → Bow (Robert, #zombie-art thread Sep 26) | ~6% | Wrong |
| T5 New colour versions (Robert, #zombie-design Sep 29) | ~5% | Right |
| T6 Library/bought-pack sounds (Calvin's sources sheet) | ~4% | Right |
| T7 Loss condition: full tray is not a loss (ZM3D GDD vs prototype doc) | ~4% | Right |

The difficulty is spread over seven traps in different places, and this run split them 3 wrong / 4 right, which is the kind of variation the baseline's pattern check needs.

### Tool calls

Tool calls: 253 (189 by the main agent, 64 by one general-purpose sub-agent; both count). Task type: long-horizon; minimum 100 on average; 90% threshold 90. Not under 90% of the minimum.

### Correct work and usability

The run handled the hard parts it found well. It read Claire's Turkish DM and applied the art-change rule to all 12 bathroom lines, caught Robert's colour versions (including that one Default board item is now Owed), and traced both non-original sounds to Calvin's sources sheet. It avoided the prototype loss-rule decoy, used the GDD's current rule and the 7-slot tray, and found the PlayableX music-after-first-click rule. It shared both files with exactly the kickoff attendees plus intake, and moved and commented only true Owed tickets. Usable as-is: the brief apart from §4, 76 of 96 sheet rows, all 32 ticket writes, the shares and the channel post. Needing correction: 20 sheet rows, 20 ticket moves and comments, the counts in the DM and final response, brief §4, and two Board set cells.

### Task / environment defects

None found that affect the run. All three missed records are in the overlay, dated before the clock and visible to Julia (channel membership, doc share, public channel thread). The tools needed (slack_conversations_history / slack_read_thread, gdrive_search / gdocs_get_document_text) were available and used elsewhere in the run.

### Unassessed scope

None material. The exact rendered Doc/Sheet were not re-fetched by the run. The successful create, values_update and batch_update payloads establish their content.

### Score rationale

**4 (Hard, NON-FAIL).** Three independent retrieval failures leave Frederick's central "where the pack actually stands" answer wrong by 20 lines (Ready overstated 56 vs 36, Owed understated 32 vs 52). They also leave 20 Owed tickets untouched, tell PlayableX that 20 unusable files are ready, and give the wrong eighth board item in the brief. Correcting that means changes across the sheet, the tickets, both messages and the brief, which is beyond the bounded correction a 3 describes. It is not a 5: delivery was complete and correctly addressed, and most of the brief, about 80% of the sheet rows and every ticket write it made are correct and usable. The run also beat four of the seven traps, so the central result needs substantial correction but is not invalidated.

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
Next action: Proceed with dependent authoring (/oe, /rubric); retain the C1/C2/C3 failure evidence (ASCII note, outgoing-folder doc, board-swap thread) and keep each trap on its own rubric rows.
Evidence limits: One run only; no average-score or repeatability claim. The export omits the initial user-prompt event, so prompt identity and unhinted status rest on the saved prompt, the run's behaviour and the contributor's submission.
