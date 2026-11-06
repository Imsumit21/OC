# Human Time Worksheet — vincent-zm3d-release-gate

Pass: post-baseline refresh        Tier: Long-Horizon
Universe: synth-cut · Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Hours: 18.75

Built from 04_Prompt.txt (sha256 e775405ef8d5, prompt-check PASS), 00_Assigments.md, 01_Grounding_Dossier.md, 01_Hardness_Manifest.json (18 traps), 03_Error_Async_Config.txt (Friction: none), 08_Oracle_Events.md (35 events) and the graded baseline (07_Baseline_Trajectories, 6/6 completed, average 164 counted calls).
Manual effort only. Vincent reads Arthur's candidates post and the release ticket, opens Leonard's rules and Arthur's build note, works out the in-scope ticket list in Linear by hand, opens every ticket and its comments, chases the decisive re-checks through #builds, Brian's DM (mostly Turkish), #zombie-bugs, Douglas's DM, his mailbox, the Trello card and the backend PR, runs the runbook's update-path check against Brian's files, then types the register, edits ZOM-570, files one ticket and replies in the thread. Volumes are from Vincent's view: channels and DMs he is in, his mailbox, files shared with him, and unscoped Linear, Trello, GitHub and Confluence.

| Sub-task | Kind (read / dead end / workaround / re-read / write) | Volume (measured, persona view) | Rate | Minutes |
|---|---|---|---|---|
| Read Arthur's candidates post, the ZOM-570 description and Leonard's sign-off comment on it | read | 1 post (C08R27X0EAH/1759263900.484190) + 1 ticket description (4 paragraphs) + 1 comment (cmt_zom570_1) | short ask | 10 |
| Read Leonard's ZM submission rules, Arthur's "How ZM submission builds are cut" note, and the gate sheet's How we gate and Sep 22 tabs | read | 2 docs (f_632c44650df44fe252ee59, f_a038a576ca8db6955fae95) + 2 tabs (20 rows and 9 rows, f_0ebfccf33076f9dbf086bc) | careful read of rules and definitions | 25 |
| Skim #builds for the #127 cut, the #135 / #50 Started lines and when the ZOM-569 and ZOM-473 fixes landed | read | C05433XK267: 443 messages Sep 22 to Sep 30 PT | skim ≈ 3,000/h + reading 3 change lists | 20 |
| Triage Linear by team, state and completed date to the in-scope list (open ZM tickets, ZM-titled ART/DES, Done after the cut; ZOM-570, ZOM-359, ZOM-475 out) | read | 553 base ZOM issues + 2 ZM-titled ART/DES + 16 seeded issues = 571 listed; 132 in scope | triage ≈ 450 items/h | 76 |
| Open each in-scope ticket with its comments and give it a call and build status under Leonard's rules | read | 132 tickets; 58 seeded comments (01_Universe_Inject.sql linear_comments; base Linear has none) | ≈ 2 min each (classify in a sweep) | 264 |
| Cross-check the tickets whose call turns on another record: Done but re-tested, server-side fixes, Leonard's per-ticket rulings, comments that name what goes wrong | read | 24 tickets (19 blockers incl. the new one, ZOM-558, ZOM-563, ZOM-429, ZOM-517, ART-793) across Linear, Slack, mail, Trello, GitHub | ≈ 8 min per record across 2–3 surfaces (V1 8–15 min) | 192 |
| Skim Brian's DM for his #133 / #49 and #50 findings | read | D0770ET1HV2: 1,376 messages Sep 22 to Sep 30 + 3 seeded, mostly Turkish | ≈ 2,000/h (slower: foreign-language DM) | 41 |
| Skim #zombie-bugs for Vincent's own re-check posts on the candidates | read | C08R27X0EAH: 198 messages Sep 22 to Sep 30 + 5 seeded | skim ≈ 3,000/h + 2 posts read closely | 10 |
| Read Vincent's DM with Douglas for the prod deploys (ZOM-563, ZOM-567) | read | D079SNE2TL4: 103 messages Sep 22 to Sep 30 + 1 seeded | skim + 3 messages read closely | 10 |
| Find the playtest vendor's session notes in the mailbox | read | Vincent's mailbox: 55 threads in Sep 2025 (persona_view reach) | small mailbox scan + 1 email | 15 |
| Read the Fix TECH ISSUES card on the ZM ROADMAP board: Arthur's reuse rule and Leonard's #135 re-test | read | ZM ROADMAP 79 cards; 1 card, 2 seeded comments | title scan + 1 card | 10 |
| Read the match3d-backend PR #36 reviews for the chest-rows load | read | 1 PR, 2 reviews, 1 inline review comment | 1 decisive thread past its apparent conclusion | 10 |
| Run the runbook's update-path check: the runbook, Brian's matrix and update-path doc, and a Linear search for an existing ticket | read | 1 Confluence page (page_qa_runbook), 1 sheet (6 rows, f_b91db376f65604b8602657), 1 doc (4 rows, f_5e40215b7d4d24b0455412), Linear search ("update", "save", "level 1") | short reads + 1 search | 25 |
| Dead ends: the Sep 22 tab's calls, "regression matrix green", the old hotfix doc, ZOM-424 as the update bug, the Trello to-do card, Douglas's "rolled out", ZOM-569's "fixed on my branch", the #135 "trampoline and glue" change, Wilson's #1974 change and the rest of the manifest traps | dead end | 18 traps (01_Hardness_Manifest.json traps) | ≈ 4 min per trap | 72 |
| Re-read rows a later record overturns: ZOM-559 (Sep 22 tab vs Brian's S22), ZOM-435 and ZOM-473 (Done vs re-tests), ZOM-567 (rolled out vs Arthur's prod check), ZOM-569 (closed vs #2028), ZOM-558 (rule vs Leonard's override), ZOM-293 (description vs comment), ZOM-458 / ZOM-535 (Vincent's note vs Brian's DM) | re-read | 8 rows | ≈ 4 min each | 32 |
| Create the new tab and type the register: ticket, title, build status, QA result, call, evidence | write | 1 tab, 133 rows × 6 columns + header | ≈ 2 min per row + 10 min setup | 276 |
| Add the blocker list to the ZOM-570 description, keeping Arthur's text | write | 1 description edit, 19 keys | ≈ 15 min | 15 |
| File the new ZOM ticket for the iOS N-1 update save reset with device, OS, source build and repro | write | 1 Linear issue (4 fields) | ≈ 10 min tailored ticket (V1 5–10 min) | 10 |
| Reply in Arthur's candidates thread with the QA call | write | 1 thread reply (no-go, 19 blockers) | ≈ 12 min tailored message | 12 |
| Total | | | | 1125 = 18.75 h |

Tier check: in band. Long-Horizon is about 12–24 h; 18.75 h sits inside it. The baseline confirms the scope: 6/6 Opus runs averaged 164 counted tool calls (12_difficulty_input.json; long-horizon tier 100–500+). No trigger, so no re-measurement.
Baseline count basis (post-baseline only): average 164 counted calls (runs 259, 169, 169, 124, 134, 128) vs Long-Horizon 100–500+
Condensed breakdown length: 731 characters (field accepts 50–2,000): 9 grouped lines (read the ask 35, #builds 20, triage 76, ticket sweep 264, cross-checks 288, runbook check 25, dead ends and re-reads 104, register 276, other writes 37) plus the total.
Sources measured: `python3 Task_Authoring/tools/persona_view.py reach vincent_parker` (mailbox 1,258 threads, 55 in Sep 2025; Slack channels he is in incl. C05433XK267, C08R27X0EAH, D0770ET1HV2, D079SNE2TL4); `python3 Task_Authoring/tools/hg.py search search linear "ZOM-293"` (Linear export located: linear/data.json); exports read through hg.py's registered sources: slack messages C05433XK267 / C08R27X0EAH / D0770ET1HV2 / D079SNE2TL4 2025-09.json (443 / 198 / 1,376 / 103 messages Sep 22 to Sep 30), linear data.json (553 ZOM issues, 2 ZM-titled ART/DES, 0 comments), trello data.json (ZM ROADMAP 79 cards), 01_Universe_Inject.sql (16 issues, 58 comments, 2 Trello comments, PR #36 with 2 reviews and 1 review comment), 01_Hardness_Manifest.json (18 traps).

## Self-review

Walked `10_Long Horizon Guidelines - V2.md` §5 (sub-tasks, dead ends, workarounds, re-reading) and §10, the Pre-QC "Difficulty and submission" list ("justified sub-task by sub-task and the arithmetic adds up") and the field text (50–2,000 characters, typed by hand, forced-error workaround time). Every sub-task has a measured volume; dead-end and re-read lines are present; there is no forced error (03_Error_Async_Config.txt: Friction none), so there is no workaround line; writes are counted per write (1 tab of 133 rows, 1 description edit, 1 issue, 1 reply); 1125 min = 18.75 h on a 0.25 step; the condensed breakdown is 731 characters.

| Counter-reading | Resolution (evidence) |
|---|---|
| Counter (inflated): 264 min to sweep 132 tickets plus 192 min of cross-checks double counts | the sweep is the V1 ≈ 2 min classify rate for every ticket (132 in scope, 12_difficulty_input.json population confirmed by the R2 recount); the cross-checks are only the 24 tickets whose call needs another surface (Trello re-test for ZOM-435, Brian's DM for ZOM-458 / 473 / 535, the vendor mail for ZOM-562, PR #36 for ZOM-567, #2028 for ZOM-569, Douglas's DM for ZOM-563), at the low end of V1's 8–15 min |
| Counter (inflated): 276 min to type a register | 133 rows × 6 columns with an evidence id per decisive row; 2 min per row is under the 3 min per 5-column row of the Julia ZM worksheet; the six baseline runs wrote the same 133-row grid (trajectory-run-1.json event 885, run-2 to run-6 alike) |
| Counter (solution-path estimate): written as if Vincent knew which records decide each ticket | discovery lines cover the 571-ticket triage, 443 #builds messages, 1,376 messages of Brian's DM, 198 #zombie-bugs messages, 103 Douglas DM messages and 55 mailbox threads; every one of the 18 manifest traps has a dead-end share, and 8 overturned rows are re-read (traps from 01_Hardness_Manifest.json; volumes via hg.py export reads) |
| Counter (evaluator-wide volume): Slack and mail counts could include what Vincent can't see | the channel counts are channels Vincent is a member of (`persona_view.py reach vincent_parker`: C05433XK267 #builds, C08R27X0EAH #zombie-bugs, D0770ET1HV2, D079SNE2TL4); the mailbox count is his own (1,258 threads, 55 in Sep 2025); Linear, Trello, GitHub and Confluence are unscoped |
| Counter (tier mismatch): 18.75 h could look high or low for Long-Horizon | Long-Horizon is about 12–24 h and the baseline averaged 164 counted calls (100–500+ band); both agree, so the hours follow the 132-ticket register, not the tier (12_difficulty_input.json) |
| Counter (linter reading): from the prompt alone, "run a QA gate and reply" looks like 4–6 h | the reasoning names the volumes the SQL and the universe show: 571 tickets triaged, 132 called, 24 cross-checked across five services, 18 traps, a 133-row register; 18.75 h is within 3× of a 6–8 h reading (04_Prompt.txt, 01_Universe_Inject.sql) |

Re-verified this run: Vincent's reach (`persona_view.py reach vincent_parker`); 443 / 198 / 1,376 / 103 messages Sep 22 to Sep 30 in the four channels (slack message files); 553 ZOM issues and 2 ZM-titled ART/DES (linear data.json); 79 ZM ROADMAP cards (trello data.json); 16 issues, 58 comments, 2 Trello comments and PR #36's 2 reviews and 1 review comment (01_Universe_Inject.sql); 18 traps (01_Hardness_Manifest.json); 132 in scope and 164 average calls (12_difficulty_input.json).

Sum recomputed: 10 + 25 + 20 + 76 + 264 + 192 + 41 + 10 + 10 + 15 + 10 + 10 + 25 + 72 + 32 + 276 + 15 + 10 + 12 = 1125.

Unresolved: none. The human types the reasoning on Screen 25 in their own words (pasting and copying are blocked).

```
STAGE GATE humantime: PASS — Task_Authoring/task_inputs · 05_Human_Time_Worksheet.md#adc8b55ccc2e · 04_Prompt.txt#e775405ef8d5 · 00_Assigments.md#90d69427cab7 · 08_Oracle_Events.md#b4ca728961d2 · 07_Baseline_Trajectories#dfde6e919b67 · __context__#fb209f3058d7 · __assignment__#c2f3888d53bd · __policy__#dc4ab5df3cdd · __gate_policy__#9b78441396d8 · __review__#4c88e8308ed5 · blocking 0 · warnings 0 · checks 17
[PASS] assignment.v3_context: Vincent Parker / Game Systems Engineer; easy cap <90%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 05_Human_Time_Worksheet.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 00_Assigments.md, 08_Oracle_Events.md, 07_Baseline_Trajectories)
[PASS] chain.prompt-check: upstream 'prompt-check' PASS pasted and current (04_Prompt_Check.md#393ef573a3c0, 04_Prompt.txt#e775405ef8d5, 04_Prompt_Writing_Brief.md#25ac59db2409, __context__#fb209f3058d7, __assignment__#c2f3888d53bd, __policy__#dc4ab5df3cdd, __gate_policy__#9b78441396d8, __review__#e9dc2ff73cec)
[PASS] structure.placeholders: no placeholders in 05_Human_Time_Worksheet.md
[PASS] structure.arithmetic: 19 sub-tasks sum to 1125 min = 18.75 h
[PASS] evidence.volumes: every sub-task has a measured volume
[PASS] structure.kinds: dead-end / workaround / write lines present
[PASS] structure.field_length: condensed breakdown 731 characters
[PASS] evidence.sources: volume sources name the hg.py / persona_view queries
[PASS] structure.tier_check: tier check line present
[PASS] review.counter_readings: 6 evidenced counter-readings (of 6 found; need ≥ 5) in 05_Human_Time_Worksheet.md
[PASS] review.coverage: self-review addresses all 5 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```
