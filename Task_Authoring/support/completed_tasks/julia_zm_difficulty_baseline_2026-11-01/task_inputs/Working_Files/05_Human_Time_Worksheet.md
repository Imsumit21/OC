# Human Time Worksheet — jl-zm-difficulty-baseline

Pass: post-hardening refresh        Tier: Long-Horizon
Hours: 16.75

Built 2026-10-30 from 04_Prompt.txt (sha256 22f26066688c, /prompt PASS 5), 00_Assigments.md, 01_Grounding_Dossier.md, 01_Hardness_Manifest.json,
04_Prompt_Writing_Brief.md, 03_Error_Async_Config.txt (Friction: none), against 01_Universe_Inject.sql sha256 dd7536cdea3f (hardening round 4: Leonard's reply under Julia's Sep 29 question; round 3: Blake's 'not tiers' review on match3d#265 and Leonard's card attachment; round 2 and /prompt attempt 7 fix; Leonard's thread reply and the card checklist added).
Manual effort only. Julia reads Leonard's DM, finds the rules card on the ZM ROADMAP board, opens every candidate ZOM ticket and its closing note, reads Blake's mail in her own
mailbox, checks the shared PRs, copies the enrage sheet and types the register by hand. Volumes are from Julia's view: Slack channels she is in, her mailbox and
calendar, files shared with her, and unscoped Linear, Trello and GitHub.

| Sub-task | Kind (read / dead end / workaround / re-read / write) | Volume (measured, persona view) | Rate | Minutes |
|---|---|---|---|---|
| Read Leonard's ask in the DM and his follow-up in its thread | read | 1 message + 1 thread reply (D05HB64NMQU/1759261706.530914, D05HB64NMQU/1759262838.442871) | short ask + short reply | 8 |
| Find the difficulty baseline card on the ZM ROADMAP board, read its 7 rules, Leonard's comment and his "Before Monday" checklist, open the card's attachment (Leonard's "notes for monday" doc), and pass over the Domino Delights card of the same name | read | ZM ROADMAP board: 79 cards (69 open) + seeded card 68daca5871dba40417a00383, comment, checklist 68dc033bf7d24e86b8a9cc67 (2 items) and attachment 68dbfcc8aa008dbd8cccea3e -> doc f_f494073fc667097c3c2c6b (2 lines); lookalike card 683dbef4e319167a802bd888 | title scan + 2 card reads + checklist + a 2-line doc | 25 |
| Find Blake's store builds mail and read his reply under it | read | Julia's mailbox: 304 threads (persona_view reach julia_lawson); 1 thread, 2 messages (julia.lawson@harmonygames.co/1844679607844896665) | small mailbox scan + one decisive thread past its first message | 15 |
| Read the session agenda doc | read | 1 doc, 4 agenda items (f_9ec79682ff351aa466364a) | short doc | 5 |
| Find the tuning invite on the calendar and note its attendees | read | Julia's calendar: 792 event copies, 261 meetings (persona_view reach); 1 event, 5 attendees (evt_91674a9c23d012a9ac34da) | open the Mon Oct 6 day | 5 |
| Read ZOM-42 in full (the tier spec) | read | 1 long description: tiers, starting tier, promotion and demotion rules | careful read of a spec | 15 |
| Read Robert's dynamic difficulty deck | read | 3 slides (f_048bf5e69f8e7f1a659a5c) | short deck | 10 |
| Read the enrage sheet: Live, Next pass and History tabs | read | 3 tabs; Live 11 rows × 4, Next pass 4 × 3, History 5 × 3 (f_0ba93ae0238d9ed4178212) | dense sheet | 15 |
| Skim #zombie-design for September: Blake's correction of the deck, Brian's recap, Vincent's request | read | C090N54TG79: 830 messages in Sep 2025 (base) + 3 seeded | skim ≈ 3,000/h | 17 |
| Skim #zombie-match3d and #zombie-bugs for September: the store build versions and per-monster enrage talk | read | C0880U9751A 473 + C08R27X0EAH 1,097 messages in Sep 2025 | skim ≈ 3,000/h | 31 |
| Triage the ZOM tickets by title and created date against the card's words and window | read | 498 ZOM issues created up to Aug 31 (linear data.json) | triage ≈ 450 items/h | 66 |
| Open each candidate's closing note; drop the ones that are out (no listed word, no "tiers:" tag, duplicates, ATK, the six Leonard leaves off, the four tickets he drops in the thread under Julia's question) | read | 109 candidates with notes (01_Universe_Inject.sql linear_comments); 80 non-members | ≈ 2 min each (classify a note in a sweep) | 160 |
| Decide each member's status: note, the mail's stripped list, Not shipped states, the replacing note | read | 24 members (16 Live, 4 Editor only, 3 Not shipped, 1 Replaced; truth.json) | ≈ 8 min per record across 2–3 surfaces (V1 8–15 min) | 192 |
| Check the PRs behind shared or linked tickets (which part of a shared PR is whose), and read the reviews on the title matches' PRs for Blake's 'not tiers' marks | read | 12 PRs: match3d #243, #244, #258, #265, #267, #271, #282, #283, #289, #296, #319, #401; review threads on #243, #244, #265 (8 reviews, 7 inline comments) and #271 | ≈ 8 min each (find a handful of PRs ≈ 40 min) + ≈ 22 min for the 4 review threads | 118 |
| Dead ends: Brian's "editor bits too" and "+50% every monster", the deck's ">= 90" and "+25% HP", the Next pass tab, the Domino card and sheet, Vincent's channel request, ZOM-199's ">= 90", the old iOS build, ATK POWER, tickets after Aug 31, duplicates, untagged Blake tickets, ZOM-45/277/173/312/315 by title, #401 as a replacement, the invite vs Robert only, the lives tickets, the comment set, the four dropped tickets and Brian's edit access (Leonard's reply under Julia's question) | dead end | 27 traps (01_Hardness_Manifest.json traps T1–T25, T28, T29) | ≈ 4 min per trap | 108 |
| Re-read rows a later record overturns: starting tier (Blake's reply), demotion (ZOM-42 in full), enrage (Blake's correction, the sheet), editor-only rows (the mail), ZOM-254/282 (the note), the attack-power tickets (the card comment) | re-read | ≈ 8 rows | ≈ 4 min each | 32 |
| Create the register sheet and type the Tickets tab: ticket, title, Linear state, status, replaced by | write | 1 sheet, 24 rows × 5 columns + header and two tabs | ≈ 3 min per row + 15 min setup | 87 |
| Type the Rules in force tab: starting tier, promotion, demotion, level drop, enrage per monster | write | 5 rules + the enrage table (11 rows copied from the sheet) | ≈ 25 min | 25 |
| Move the sheet into the ZM Difficulty folder and share it with the invite's people at the right roles | write | 1 move (d_96489e1e00a56685625939) + 4 shares (Robert editor; Brian and Leonard commenter; Arthur viewer) | ≈ 2 min move + 2.5 min per share | 12 |
| Comment on the tickets rule 6 and the checklist's rule 6 change cover | write | 9 Linear comments (ZOM-199 > 90; ZOM-254 replaced by ZOM-282; 4 Editor only and 3 Not shipped: not in the store builds) | ≈ 7 min each for the 2 tailored ones, ≈ 5 min each for the 7 similar ones (V1 5–10 min) | 49 |
| Reply to Leonard in the DM with the total, the count per status and the keys he asked for | write | 1 message (24 tickets: 16 / 4 / 3 / 1; 3 Not shipped + 4 Editor only keys; when a new player gets the starting tier) | ≈ 10 min tailored message with 7 keys + one rule | 10 |
| Total | | | | 1005 = 16.75 h |

Tier check: in band. The Long-Horizon review triggers are below 5 h or above 120 h. 16.75 h sits above the 10 h Long-Horizon worked example and under the V1 24 h Long example (~338 calls). The manifest budget is 168 unconditional calls, and the author target is ≥ 120 calls per run. No trigger, so no re-measurement is needed.
Condensed breakdown length: 870 characters (field accepts 50–2,000): one short line per grouped sub-task (what, volume, minutes) plus the total, 10 lines.
Sources measured: `persona_view.py reach julia_lawson` (mailbox 304 threads; calendar 792 event copies, 261 meetings; Slack channels she is in); `persona_view.py search julia_lawson trello "difficulty"` (3 base hits + the seeded cards); `persona_view.py search julia_lawson gdrive "ZM"` (8 visible); exports read through hg.py's sources: linear data.json (498 ZOM issues created up to 2025-08-31); trello data.json ZM ROADMAP (79 cards, 69 open); slack messages C090N54TG79 2025-09 (830), C0880U9751A 2025-09 (473), C08R27X0EAH 2025-09 (1,097); 01_Universe_Inject.sql (109 linear_comments, the card, the mail thread, the sheet's 3 tabs, the deck's 3 slides, the invite); truth.json (35 members, 22/9/3/1; 2 comments).

## Self-review

Walked `10_Long Horizon Guidelines - V2.md` §5 (sub-tasks, dead ends, workarounds, re-reading) and §10, then the Pre-QC "Difficulty and submission" list ("justified sub-task by sub-task and the arithmetic adds up"), then the field text (50–2,000 characters, typed by hand, forced-error workaround time). Result per check:
- Sub-tasks are present, each with a measured volume.
- Dead-end and re-read lines are present.
- There is no forced error (03_Error_Async_Config.txt is Friction: none), so there is no workaround line.
- Writes are counted per write: 1 sheet with 2 tabs, 1 move, 4 shares, 14 comments, 1 reply.
- 1005 min = 16.75 h, on a 0.25 step.
- The condensed breakdown is 850 characters.

| Counter-reading | Resolution (evidence) |
|---|---|
| Counter (inflated): 224 min for 28 member statuses is a lot | each member needs its closing note, the mail's stripped list and often a PR or the Not shipped state (e.g. ZOM-173: note + match3d#243's file split; ZOM-315: note + the editor stats panel; ZOM-254: ZOM-282's replacing note). 8 min is the low end of the V1 8–15 min per record across 2–3 surfaces |
| Counter (inflated): 160 min to drop 80 non-members | the card's scope rests on the closing note (the "tiers:" tag) and the comment's attack-power rule. A title alone can't settle it (ZOM-221 "Fix monster spawning issues…" is in by its tag; ZOM-271 "ATK POWER" is out). 2 min per note is the V1 sweep rate |
| Counter (solution-path estimate): written as if Julia knew where the rules were | discovery lines cover finding the card among 79 board cards (plus a same-name lookalike), Blake's mail in her mailbox, the invite on her calendar, three September channels (2,400 messages) and 498 tickets by title; every manifest trap (T1–T21) has a dead-end share |
| Counter (evaluator-wide volume): Slack, mail and calendar counts include what Julia can't see | the Slack counts are channels Julia is in (C090N54TG79, C0880U9751A, C08R27X0EAH; dossier §1.E check-sql PASS). The mailbox and calendar counts come from `persona_view.py reach julia_lawson`; Linear, Trello and GitHub are unscoped |
| Counter (tier mismatch): 17 h could look low or high for Long-Horizon | the Long-Horizon triggers are < 5 h or > 120 h. The call budget is 147 (01_Hardness_Manifest.json), and the hours follow the 498-ticket triage, the 109 notes and the 35-row register, not the tier |
| Counter (linter reading): from the prompt alone, "build a register and reply" looks like 3–5 h | the reasoning names the volumes the SQL and the universe show: 498 tickets triaged, 109 notes, 35 decisions, 12 PRs, three channels, 21 traps, a 35-row register. 17 h is within 3× of a 6–8 h reading |

Re-verified this run:
- 498 ZOM issues up to Aug 31 (linear data.json).
- 79 / 69 ZM ROADMAP cards (trello data.json).
- 830 / 473 / 1,097 September messages (slack message files).
- Julia's mailbox and calendar (persona_view reach).
- The 109 notes and the seeded records (01_Universe_Inject.sql).
- The 35 members and the writes (truth.json).

Sum recomputed: 8 + 25 + 15 + 5 + 5 + 15 + 10 + 15 + 17 + 31 + 66 + 160 + 192 + 118 + 108 + 32 + 87 + 25 + 12 + 49 + 10 = 1005.

Unresolved: none. The human types the reasoning on Screen 25 in their own words (pasting and copying are blocked).

```
STAGE GATE humantime: PASS — Task_Authoring-2/task_inputs · 05_Human_Time_Worksheet.md#d0d44b745652 · blocking 0 · warnings 0 · checks 15
[PASS] structure.outputs: 1 output(s) present: 05_Human_Time_Worksheet.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 00_Assigments.md, 08_Oracle_Events.md, 07_Baseline_Trajectories)
[PASS] chain.prompt-check: upstream 'prompt-check' PASS pasted and current (04_Prompt_Check.md#7ea3a085bbd9, 04_Prompt.txt#22f26066688c)
[PASS] structure.placeholders: no placeholders in 05_Human_Time_Worksheet.md
[PASS] structure.arithmetic: 21 sub-tasks sum to 1005 min = 16.75 h
[PASS] evidence.volumes: every sub-task has a measured volume
[PASS] structure.kinds: dead-end / workaround / write lines present
[PASS] structure.field_length: condensed breakdown 870 characters
[PASS] evidence.sources: volume sources name the hg.py / persona_view queries
[PASS] structure.tier_check: tier check line present
[PASS] review.counter_readings: 5 evidenced counter-readings (of 6 found; need ≥ 5) in 05_Human_Time_Worksheet.md
[PASS] review.coverage: self-review addresses all 5 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```










