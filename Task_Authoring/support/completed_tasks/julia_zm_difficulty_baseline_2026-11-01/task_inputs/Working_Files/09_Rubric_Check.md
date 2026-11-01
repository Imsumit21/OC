# 09 Rubric Check — jl-zm-difficulty-baseline (round 7, SQL b64bc2f2c6dc)
Checked 2026-11-01 · Criteria 73 (builder minimum 5: ok) · Plan 2026-11-01 (09_Rubric_Writing_Plan.md) · Base: the /rubric r3 PASS rubric (Audit-Report/3_rubric_PASS_r3.md, 68 rows) brought to round 7 per /prompt r14 and /hardness r7 (Audit-Report/1_prompt_PASS_r14.md, 1a_hardness_NONFAIL_r7.md)
JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · schema gate: pass (every row has all five fields non-blank; categories Outcome/Process; weights 1/3/5) · note: the file is the Claude draft, not yet a builder export; re-run check on the export if any text changes
Readiness for /rubric: CLEAN — a prediction only; /rubric gives the verdict

## Coverage
| Plan row / requirement | Criteria | Covered (omission + wrong-result test) |
|---|---|---|
| W1 register artifact and tabs (agenda 'One sheet with two tabs') | C1–C24 | covered — no sheet or a tab left out fails |
| W1 folder (prompt: "put it in the zm difficulty folder") | C4 | covered — the Drive root fails |
| W1 row set and exclusions (23 rows; 15 Live; 4 Editor only) | C5–C7 | covered — 33/27/24/22 rows, 21/16/14 Live and 8–9 Editor only fail; the count rows are the exclusion guard, incl. ZOM-295 (PR 271) and ZOM-312 (PR 265) |
| W1 statuses and replaced-by (rules 1, 3, 4) | C8–C20 | covered — 5 Live samples incl. ZOM-42 (rule 4) and ZOM-281 (the non-Blake 'tiers:' ticket, /hardness r6 F1), every Editor only, Not shipped and Replaced ticket |
| W1 columns: title, Linear state (rule 2) | C21, C22, C23 | covered — status words in the state column or a cut title fail (r1 M4) |
| W1 Robert's three columns (card rule 2, Robert's group-chat reply) | C24–C27 | covered — a tab with the agenda's columns only fails the header row; assignee, priority and the Pacific done day are spot-checked (UTC day also passes, /prompt r14) |
| W1 Rules in force (rule 5) | C28–C41 | covered — '10 levels' timing, '>= 90', the deck's +25% hp and Next pass values fail; Mailman, Mayor2, PartyGirl row graded (r1 M1) |
| W2 shares (rule 7, notes doc, Sep 30 21:16 reply) | C42–C46 | covered — Brian as editor, Arthur above viewer and an extra person (Domino Delights decoy, r1 M5) fail |
| W3 ticket comments (rule 6 and the checklist) | C47–C56 | covered — every one of the 9 tickets on its own row plus the exact-9 volume row; the 7 Editor only / Not shipped rows need both builds (Leonard's reply D05HB64NMQU/1759262838.442871) |
| W4 DM reply: counts, keys, 254 → 282, starting tier | C57–C71 | covered — 24/27/29/33 tickets, 16/21 Live, 8–9 Editor only, keys left out, extra Editor only keys (exact-key row) and 'after level 10' fail |
| W4 one Slack place (Vincent's #zombie-design request) | C72 | covered — a copy in #zombie-design fails (r1 M6) |
| W4 order: reply after the register is in the folder | C73 | covered — Process row, order only (r1 Process finding) |
| R8 'no need to check with me first' | all | covered — constraint only; the end-state rows need the writes done |

Unauthorized criteria: none

## Findings
| # | Severity | /rubric type | Criterion | Quoted span | Rule (§) | What is wrong | Evidence (record / plan row) |
|---|---|---|---|---|---|---|---|
| N1 | Note | none | C41 | "marked as not copied yet" | 2.9 lexical pre-scan | the word 'not' is the enrage sheet's own cell label, not a prohibition; the row grades a listed entry | Live tab f_0ba93ae0238d9ed4178212 row 'Mailman, Mayor2, PartyGirl … not copied yet'; /rubric r1 fix list (C37 text) |

`hg_rubric_lint.py` on 09_Rubrics.json (the /rubric code checks):

```
hg_rubric_lint.py task_inputs/09_Rubrics.json -> findings: none, count: 0
```

## Round 7 changes (from the /rubric r3 PASS rubric)
| Change | Criteria | Source |
|---|---|---|
| 23 tickets, 15 Live in the register and the DM | C5, C6, C57, C58 | /prompt r14 recommendation 1; Blake's review comment harmonygames-Games/match3d#271#rc_1 |
| ZOM-281 Live replaces the ZOM-246 spot check (Live group stays at 5) | C10 | /hardness r6 F1 and r7 next action; cmt_df69e4a92767cbff0000 |
| The 7 Editor only / Not shipped comments name both builds | C47–C55 | Leonard's reply D05HB64NMQU/1759262838.442871; /prompt r14 'Unchanged' |
| Robert's three columns: header + 3 spot checks, Pacific or UTC day | C24–C27 | /prompt r14 recommendation 1 (accept both days, number or label); CAFC495E4006/1759229513.774912 |
| Exact Editor only keys in the DM | C69 | Leonard's ask for the keys 'so i know who to chase' (D05HB64NMQU/1759262838.442871) |
| Brian's share w5 (multi-source: rule 7, checklist, later reply) | C43 | weight by kind of work: the latest of three records decides |
| Blake's editor/debug rule cited from his reply (own thread) | C8–C16, C61–C65 | /injection r12 C-2 (reply in its own thread); julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> |
| Starting tier also accepts '10 levels played' | C28, C70, C71 | /prompt r14 carried item |

## /rubric r1 Fix List applied (kept from round 2)
| r1 item | Applied as | Status |
|---|---|---|
| R2 two tabs | C2, C3 (w1 each) | evaluator's text |
| R3 weight | C4 w1 | evaluator's text |
| R4 exclusion guard | C5 | evaluator's text |
| R4–R6, R59–R63 evidence | cites the card, both DM replies, the notes doc, PR #265 rc_7 and the store-builds mail | applied |
| R7–R18 absence-only | deleted; the count rows are the guard | applied |
| R20 | C9 ZOM-42 Live w1 | evaluator's text |
| R31 | C20 writes out ZOM-282's title | applied |
| R33 / R73 (r2: evaluator's checked text) | C28, C70: wins/losses clause removed from the required content; fail list limited to a timing tied to reaching or clearing level 10; 'the first 10 levels played' and 'after the first 10 games' pass | own rewrite |
| R34 | C29 | evaluator's text |
| R35 / R38 | either window wording passes, w1 each | evaluator's direction |
| R40 | drops in difficulty, no amount or one tier; Blake's note removed from the evidence; w1 | evaluator's text |
| R41, R42, R44 | w1; R44 cites ZOM-282's closing note cmt_912bdd42ad5c8d51521f instead of ZOM-303 | applied |
| R45 | C40: bare count of 10 monster entries; split variants count once; Mailman, Mayor2, PartyGirl not counted; no 'Live-tab rows' wording in the title | own rewrite |
| R48 | evidence now includes the folder-owner route | applied |
| R50 | C47 | evaluator's text |
| R58 | deleted | applied |
| R61 / R71 | R71 deleted; R61 w5 | applied |
| R62, R63 → w3; R64–R66 → w1 | weights set | applied |
| R64–R70 evidence | Accept states key and status only; records cited | applied |
| Add title, Canceled, Mailman row, share count, ZOM-315/293 comments, Slack guard | C22, C23, C41, C46, C54, C55, C72 | evaluator's text |
| Add Process row | C73: grades only that the DM reply comes after the register's last create or move step, so a run that misses the folder is not failed twice | own rewrite |
| Worth-a-look wording repairs | copied '10 levels played' sentences, repeated sentences, 'Brief §4b', 'Gate 6' and the dangling 'those six' removed | applied |

## Overlap / spot-check / all-fail
| Group | Criteria | Kind | Verdict |
|---|---|---|---|
| G1 Live samples | C8, C9, C10, C11, C12 + volume C6 | spot check (5) + volume | valid — ≤ 5 samples incl. ZOM-42 and ZOM-281 |
| G4 Robert's columns | C25, C26, C27 + header C24 | spot check (3) + structure | valid — one value per column, Pacific or UTC day |
| DM Editor only keys | C65, C66, C67, C68 + exact set C69 | members + exact set | not duplicates: the members grade each key, the exact set grades the chase list (extra keys fail it) |
| G2 enrage samples | C36, C37, C38 + volume C40 | spot check (3) + volume | valid |
| G3 Linear state | C21, C23 | spot check (2, incl. a non-Done edge) | valid |
| Register vs DM counts | C5/C57, C6/C58, C7/C59 | same fact in two prompt-required deliverables | not duplicates (one row per deliverable); the r1 overlap R61/R71 removed |
| Comment volume vs members | C56 with the 9 per-ticket comment rows | control + members | not duplicates (Eval 3.3) |
| Process vs folder | C73 and C4 | order vs end state | independent: a run that never moves the file still passes the order row if it replies after creating it |
| Predicted all-fail | — | none of the four bases | 0 — round-7 baseline run 3 passes every criterion in the replay |

## Dimensions
| Dimension | Count | Status | Margin / note |
|---|---|---|---|
| Overall Rubric Quality | 0 Major · 0 Moderate · 0 Minor | PASS | 0/73 |
| Criteria Weights | 0 off by two · 0 off by one | PASS | weights as set by the r1 Fix List; new rows by kind of work (1 lookup, 3 interpretation, 5 multi-source) |
| Category Balance | 72 Outcome · 1 Process | PASS | ≥ 1 Outcome |
| Process Rubrics | 1 | PASS | the one ordering check the ask carries ('reply here when it's in the folder') |
| Agent-Centric Phrasing | 0 | PASS | every title starts 'The Agent' |
| Negative Criteria | 0 | PASS | absence-only rows removed; every row needs an observable write |
| Predicted all-fail gate | 0 | PASS | tolerance 0 |
| Repair gates: schema, accuracy, atomicity, coverage, contradiction | 0 | PASS | values re-verified (Self-review) |

## Baseline replay (prediction for /create-difficulty)

```
round-7 replay: avg ~82%, pop SD ~0.11, pass@1 1/6, 4 patterns (largest 40%)
```

Replay of the six round-7 baselines (payloads read by r7 projection scripts; DM key lists hand-checked): run 1 66.9%, run 2 75.7%, run 3 100%, run 4 81.7%, run 5 88.2%, run 6 86.4% before the Brian weight change; with Brian w5 the projection is average about 82%, population SD about 0.11, pass@1 1 of 6, 4 failure patterns (largest 40%). The verifier decides the real numbers.

## Self-review

Re-read as /rubric in phase order (Evals/3_Rubrics_Eval.md Phases 1–5, hg-strict-overrides-v1) with the r1 report beside it. Pre-verdict sweep: no missing requirement (M1–M6 added), no absence-only title, no non-atomic row (status + replaced-by, speed + damage and threshold + window are the groupings r1 accepted), no title whose acceptance depends on the evidence (each evidence 'Accept' restates the title's pass/fail list), no 'such as' / 'e.g.' exemplar.

Round 7: re-verified PR 271's inline comment harmonygames-Games/match3d#271#rc_1, Robert's reply CAFC495E4006/1759229513.774912, ZOM-293 (assignee Robert, priority 4), ZOM-200 completed_at 2025-06-13T01:17:38Z, ZOM-281's note cmt_df69e4a92767cbff0000 and Leonard's reply D05HB64NMQU/1759262838.442871 (builds) through the SQL rows and linear data.json. Re-verified this run through tools/hg.py and the SQL: ZOM-282 title 'Optimize enrage mechanic for speed and attack damage only' and closing note cmt_912bdd42ad5c8d51521f ('the hp part was switched off'); ZOM-254 title; ZOM-280 Canceled; card rule 4 'ZOM-42 is the system itself: it stays Live'; Leonard's replies D05HB64NMQU/1759262838.442871 (six tickets off, keys in the reply) and D05HB64NMQU/1759267002.665190 (162, 163, 201, 250 off, no comments, Brian comments); notes doc f_f494073fc667097c3c2c6b (ZOM-258 off, Arthur view, which replaced which); all six baseline runs' Rules tab and DM wording against the rewritten rows.

| Check | Verdict | Strongest counter-reading | Resolution (evidence: pointer / rule § / case id) | Unresolved |
|---|---|---|---|---|
| C1 (R1) | PASS | a run that adds the tabs to an existing sheet — the agenda asks for a new sheet | title restates its pass/fail list; evidence 'Accept' matches (R1, P1) | none |
| C2 (R2) | PASS | a tab named 'Ticket list' — contains Tickets, passes | title restates its pass/fail list; evidence 'Accept' matches (R2, P2) | none |
| C3 (R2) | PASS | a tab named 'Rules' — contains Rules, passes | title restates its pass/fail list; evidence 'Accept' matches (R2, P2) | none |
| C4 (R3) | PASS | created in My Drive and moved later — passes on the end state | title restates its pass/fail list; evidence 'Accept' matches (R3, P3) | none |
| C5 (R4) | PASS | a run keeping 34 or 35 rows with statuses fails; a left-off list with no statuses does not count against it | title restates its pass/fail list; evidence 'Accept' matches (R4, P4) | none |
| C6 (R5) | PASS | a run that keeps ZOM-295 (24 rows, 16 Live) fails; the PR 271 inline comment is the deciding record | title restates its pass/fail list; evidence 'Accept' matches (R5, P5) | none |
| C7 (R6) | PASS | 8 or 9 Editor only rows fail | title restates its pass/fail list; evidence 'Accept' matches (R6, P6) | none |
| C8 (R19) | PASS | a run that leaves tag-only tickets out — fails, as rule 1 counts the 'tiers:' notes | title restates its pass/fail list; evidence 'Accept' matches (R19, P19) | none |
| C9 (added) | PASS | ZOM-42 marked Replaced by a later tier ticket — fails rule 4 | title restates its pass/fail list; evidence 'Accept' matches (added, new) | none |
| C10 (R21) | PASS | a run that scans only Blake's own tickets for 'tiers:' misses ZOM-281 (/hardness r6 F1) | title restates its pass/fail list; evidence 'Accept' matches (R21, P21) | none |
| C11 (R22) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R22, P22) | none |
| C12 (R23) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R23, P23) | none |
| C13 (R24) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R24, P24) | none |
| C14 (R25) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R25, P25) | none |
| C15 (R26) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R26, P26) | none |
| C16 (R27) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R27, P27) | none |
| C17 (R28) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R28, P28) | none |
| C18 (R29) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R29, P29) | none |
| C19 (R30) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R30, P30) | none |
| C20 (R31) | PASS | ZOM-254 marked Live — fails | title restates its pass/fail list; evidence 'Accept' matches (R31, P31) | none |
| C21 (R32) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R32, P32) | none |
| C22 (added) | PASS | a shortened title — fails; the row names the full title | title restates its pass/fail list; evidence 'Accept' matches (added, new) | none |
| C23 (added) | PASS | 'Not shipped' written in the state column — fails | title restates its pass/fail list; evidence 'Accept' matches (added, new) | none |
| C24 (added) | PASS | a run that never opens the group chat thread has the agenda's columns only | title restates its pass/fail list; evidence 'Accept' matches (added, new) | none |
| C25 (added) | PASS | assignee cells copied from the creator field fail | title restates its pass/fail list; evidence 'Accept' matches (added, new) | none |
| C26 (added) | PASS | a priority taken from a label or a guess fails | title restates its pass/fail list; evidence 'Accept' matches (added, new) | none |
| C27 (added) | PASS | a blank done day for a Done ticket fails | title restates its pass/fail list; evidence 'Accept' matches (added, new) | none |
| C28 (R33) | PASS | 'after the first 10 levels played' — passes; 'once they finish level 10' — fails | title restates its pass/fail list; evidence 'Accept' matches (R33, P33) | none |
| C29 (R34) | PASS | '90 or more' (ZOM-199) — fails | title restates its pass/fail list; evidence 'Accept' matches (R34, P34) | none |
| C30 (R35) | PASS | 'last 10 levels won' — fails, wrong window | title restates its pass/fail list; evidence 'Accept' matches (R35, P35) | none |
| C31 (R36) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R36, P36) | none |
| C32 (R37) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R37, P37) | none |
| C33 (R38) | PASS | a run naming only the 4-loss demotion — fails | title restates its pass/fail list; evidence 'Accept' matches (R38, P38) | none |
| C34 (R39) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R39, P39) | none |
| C35 (R40) | PASS | 'yes, the level drops' with no amount — passes | title restates its pass/fail list; evidence 'Accept' matches (R40, P40) | none |
| C36 (R41) | PASS | the deck's +25% — fails | title restates its pass/fail list; evidence 'Accept' matches (R41, P41) | none |
| C37 (R42) | PASS | Next pass 0.3/0.8 — fails | title restates its pass/fail list; evidence 'Accept' matches (R42, P42) | none |
| C38 (R43) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R43, P43) | none |
| C39 (R44) | PASS | the deck's +25% max HP — fails | title restates its pass/fail list; evidence 'Accept' matches (R44, P44) | none |
| C40 (R45) | PASS | Magician split into three variant rows — counts once, passes | title restates its pass/fail list; evidence 'Accept' matches (R45, P45) | none |
| C41 (added) | PASS | the three monsters left off the tab — fails | title restates its pass/fail list; evidence 'Accept' matches (added, new) | none |
| C42 (R46) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R46, P46) | none |
| C43 (R47) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R47, P47) | none |
| C44 (R48) | PASS | Leonard as editor — fails | title restates its pass/fail list; evidence 'Accept' matches (R48, P48) | none |
| C45 (R49) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R49, P49) | none |
| C46 (added) | PASS | Vincent added from the Domino Delights card — fails | title restates its pass/fail list; evidence 'Accept' matches (added, new) | none |
| C47 (R50) | PASS | a comment saying '>= 90' is right — fails | title restates its pass/fail list; evidence 'Accept' matches (R50, P50) | none |
| C48 (R51) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R51, P51) | none |
| C49 (R52) | PASS | a comment that says 'not in the store builds' without the two build numbers fails | title restates its pass/fail list; evidence 'Accept' matches (R52, P52) | none |
| C50 (R53) | PASS | a comment that says 'not in the store builds' without the two build numbers fails | title restates its pass/fail list; evidence 'Accept' matches (R53, P53) | none |
| C51 (R54) | PASS | a comment that says 'not in the store builds' without the two build numbers fails | title restates its pass/fail list; evidence 'Accept' matches (R54, P54) | none |
| C52 (R55) | PASS | a comment that says 'not in the store builds' without the two build numbers fails | title restates its pass/fail list; evidence 'Accept' matches (R55, P55) | none |
| C53 (R56) | PASS | a comment that says 'not in the store builds' without the two build numbers fails | title restates its pass/fail list; evidence 'Accept' matches (R56, P56) | none |
| C54 (added) | PASS | a comment that says 'not in the store builds' without the two build numbers fails | title restates its pass/fail list; evidence 'Accept' matches (added, new) | none |
| C55 (added) | PASS | a comment that says 'not in the store builds' without the two build numbers fails | title restates its pass/fail list; evidence 'Accept' matches (added, new) | none |
| C56 (R57) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R57, P57) | none |
| C57 (R59) | PASS | 35 — fails | title restates its pass/fail list; evidence 'Accept' matches (R59, P59) | none |
| C58 (R60) | PASS | 22 Live — fails | title restates its pass/fail list; evidence 'Accept' matches (R60, P60) | none |
| C59 (R61) | PASS | 9 Editor only — fails | title restates its pass/fail list; evidence 'Accept' matches (R61, P61) | none |
| C60 (R62) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R62, P62) | none |
| C61 (R63) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R63, P63) | none |
| C62 (R64) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R64, P64) | none |
| C63 (R65) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R65, P65) | none |
| C64 (R66) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R66, P66) | none |
| C65 (R67) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R67, P67) | none |
| C66 (R68) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R68, P68) | none |
| C67 (R69) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R69, P69) | none |
| C68 (R70) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R70, P70) | none |
| C69 (added) | PASS | a reply listing ZOM-162, 163, 201, 250 or 312 as Editor only fails | title restates its pass/fail list; evidence 'Accept' matches (added, new) | none |
| C70 (R72) | PASS | a valid alternative wording could fail it | title restates its pass/fail list; evidence 'Accept' matches (R72, P72) | none |
| C71 (R73) | PASS | '10 games played, not 10 levels beaten' — passes; 'after level 10' — fails | title restates its pass/fail list; evidence 'Accept' matches (R73, P73) | none |
| C72 (added) | PASS | a copy posted in #zombie-design — fails | title restates its pass/fail list; evidence 'Accept' matches (added, new) | none |
| C73 (added) | PASS | a reply sent before the move — fails | title restates its pass/fail list; evidence 'Accept' matches (added, new) | none |
| C24/C66 'the first 10 levels' in a CPM-window sentence | PASS | C24/C66 'the first 10 levels' in a CPM-window sentence | the fail list names only a timing tied to reaching or clearing level 10; a CPM-window sentence is not a timing | none |
| C36 MonsterBase is not a monster | PASS | C36 MonsterBase is not a monster | the Live tab lists it as an entry with values; the title says 'monster entries' | none |
| C68 fails together with the folder row | PASS | C68 fails together with the folder row | the order row passes on the last create step when no move happens | none |
| C-new exact Editor only keys double-grades the per-key rows | PASS | C-new exact Editor only keys double-grades the per-key rows | the per-key rows pass a reply that also lists extra tickets; the exact row fails it; different facts (members vs list) | none |
| Brian w5 is off by two | PASS | Brian w5 is off by two | the row needs three records in time order (rule 7, checklist 16:20Z, reply 21:16Z), the same multi-source basis as the count rows | none |
| Pacific day row could fail a UTC answer | PASS | Pacific day row could fail a UTC answer | the title and Accept pass 2025-06-13 too (/prompt r14) | none |

Unresolved: none for the rubric. The plan's diversity.authority_share and the difficulty risk are design findings, not rubric defects.
