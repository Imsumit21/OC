# Score-5 Study: what task shape earns /hardness 5 (evidence only, 2026-11-07)

Tags: **[R]** stated in the record. **[C]** my count from stored files. **[I]** my inference, not in the record.
Scope: 11 stored report files = 10 unique (Robert's Audit-Report copy is byte-identical). `hardness_calibration.md` and `opus_failure_patterns.md` are marked retired; used as history only. `deep_recheck.md` and `long_horizon.md` are silent on bands. The distinct-failure guidance is not in the repo; quotes come from the memory copy.

## Q1. Any recorded 5 or central-result failure?
**No evaluator has given a 5 anywhere in the record.** [R] Stored scores: 2, 2, 2, 3, 3, 3, 3, 3, 4, 4. Scores cited but not stored: Julia SQL rev 30 = 4, Frederick card = 2 then 3, Vincent = 3, three pre-checks = 1. The V1 blind reads in Mastery §11 also stop at 4.
- The rule, Eval 1A §5 [R]: 5 = "Genuine model failures invalidate the central result/delivery or defeat much of the core task." Also "A single root cause may invalidate the central result and justify 5", and "missing a required write can invalidate the task when that delivery is its central purpose".
- Only predicted 5 [R, author, not evaluator]: Douglas 01a §3, "Predicted band after round 3: 4 for the median run, 5 for a run with no habit", because that run "misses seven register verdicts and seven Todo writes". Runs 3 and 6 did exactly that [C]. No stored /hardness report covers the final SQL (reports are on f5a42cee and c1edeb44; final is 2131bbef), so this was never tested.
- Closest descriptions of collapse, none with a /hardness score [R]:
  - A1, ML-selected Combo Fighters (Mastery §0): "both consequential findings inverted"; Opus "found the data, computed it correctly, and then deferred to the most confident-sounding summary". Best 18/31. The model is not established.
  - Art-canon, 44.1 %: the retired record says the 3-4 band's "substantial core work remains correct" "sits awkwardly against 44.1%", and flags it as an open question.
  - SB-T2, avg 0.21: 5/6 "latched onto a Confluence decoy"; scores 2, 4, 3, 2, 54, 2 of 54. Cited as a QC failure, not a success.
- v2 guide low scorer. "31 % Drive cleanup" and "the exceptions task" are one task (trap 5 and worked example 4). [R] "Opus did the bulk Drive cleanup perfectly but missed every exception"; "All 22 failing rows came from those exceptions". Three carve-outs sat in older mail and a cancelled-meeting note; the 44-file list and ordinary moves passed 6/6.
  - Why so many rows failed [I]: weight sat on exception rows, so 31 % measures rubric placement, not how much work was wrong. The guide gives no /hardness score, and the study is on Enterprise Atlas tasks, not HarmonyGames.
  - Likely evaluator view [I]: 4. "Did the bulk perfectly" is the phrase evaluators use to refuse 5. It could reach 5 only if the exceptions were the purpose of the cleanup. Rubric % does not map to band: 60 % read 4 and 81 % read 4 (§11); Julia's 4 and 3 sat on tasks averaging 83.8 %.

## Q2. Every stored hardness report
| Report (calls) | Root causes | Outputs affected | Share wrong | Headline wrong? | Still correct | Band | Evaluator's reason |
|---|---|---|---|---|---|---|---|
| Julia r1 (741) | 0 material | 1 cell | 1 phrase | No | all else | 2 | "one wording choice in one cell" |
| Julia r2 (222) | 0 material | 1 cell | 1 phrase | No | 12 of 13 groups | 2 | same; "matches the written rule text" |
| Julia r3 (836) | 0 material | final reply line | none in artifacts | No | all artifacts | 2 | "changes no artifact" |
| Julia r4 (836) | 1 unread thread reply | register, DM, final | 6/34 rows (18 %) | Yes: 34 vs 28, Live 22 vs 16, 11 keys missing | 28 rows, rules tab, shares, 13 comments | 3 | "bounded and mechanical" |
| Julia r5 (968) | 1 (both thread replies) | register, share, Linear, DM, final | 10/34 rows (29 %), 1/4 shares, 4 forbidden comments | Yes: 34; 22/8 vs 24; 16/4; keys missing | 24 rows, rules tab, 3 shares, 9 comments | 4 | "the correction runs across the whole result" |
| Julia r6 (908) | 1 (stopped the subagent that found it) | register, DM, final | 1/24 missing | Yes: 23/15 vs 24/16 | 23 rows, all writes | 3 | "one register row and one DM message" |
| Julia r7 (1,084) | 1 (unread inline comment) | register, DM, final | 1 extra in 24 | Yes: 24/16 vs 23/15 | 23 rows, all writes | 3 | same |
| Douglas rev 7 (157) | 1 unread email | register, DM, final | 2/18 rows; 16/16 statuses right | Yes: 10 vs 8 | all statuses, 8 moves, folder, share | 3 | "one root cause, and the correction is bounded" |
| Douglas rev 10 (155) | 3 retrieval misses | register, DM, Linear, final | 4/18 rows, 2/10 moves | Yes: 10/8 vs 6/10 | 14/16 statuses, 8 moves, folder, share | 4 | "materially wrong but not defeated" |
| Robert (209) | 2 (unpaged Slack; GitHub unopened) | reply, 1 row, 1 issue | 1/28 rows, 1/45 issues, 1 of 2 clashes | Partly: totals right, "Everything else lines up" wrong | 27 rows, totals, 44/45 | 3 | "bounded fix" |

Patterns [C/I]: a wrong headline alone buys only 3 (r4, r6, r7). Root-cause count does not set the band: Julia r5 has one cause and scores 4, Robert has two and scores 3. The step from 3 to 4 tracks how many kinds of output need fixing and whether writes must be undone. r4 and r5 are the same miss; r5 added wrong writes. Highest share wrong at a stored 4 is 29 %.

## Q3. Evaluator language, "the central result", and deliverable shape
| Band language | Phrases used [R] |
|---|---|
| 3 | "bounded correction", "bounded and mechanical", "Nothing else needs to change", "No write needs undoing" |
| 4 | "substantial correction across the result", "the correction runs across the whole result", "Every delivery channel the prompt asks for carries a wrong result" |
| Refusing 5 | "the central result is not invalidated"; "materially wrong but not defeated"; "substantial core work remains correct and usable"; "28 of 34 rows are exactly right"; "24 of 34 rows are exactly right"; "the central result and delivery aren't invalidated" |

No report states what a 5 would need; refusals only list what survived. Five reports give no why-not-5 (r6, r7 stop at why-not-4; r1-r3 stop at why-not-3).

The central result is never formally defined, and no prompt names one [R]. The evaluator infers it:
- Julia: "the central deliverable" = the register plus its filing and sharing. Prompt: "build the register the way he set it up".
- Douglas: "the central answer" = on-prod count, "The headline number Arthur asked for". Prompt: "reply to Arthur in the DM with what he asked for".
- Robert: "the central reply" = two totals plus clashes. Prompt: "reply to him in his thread with the two monthly totals and anything that clashes".

Shape effect: all 10 stored reports are multi-part registers, so the record cannot measure one-decision tasks directly. What it shows [R]: Douglas rev 10 called the answer wrong by 4, then refused 5 by counting statuses, moves, rule logic, folder and share. [I] A register turns each row and side deliverable into a surviving part. The evaluator's four recurring cushions are: other rows right; hard rule logic applied correctly; folder/share right; an independent tab or reply section right.

## Q4. Task-shape hypotheses (all rankings are [I])
| Shape | Evidence for 5 | Evidence against | Read |
|---|---|---|---|
| (a) One decision, thin evidence | 1A: single cause may justify 5; A1 "inverted" findings | Vincent's sprint order: Opus "delivered the order in the wrong sequence", yet /hardness 3 (report not stored, reason unknown). Highest UGT risk | Plausible, unproven, one counterexample |
| (b) Many independent rows | None: all stored reports, ceiling 4 | Independent rows are the cushion; v2 says volume "passed 6/6" | Worst for 5 |
| (c) Wrong first conclusion corrupts later outputs | Julia r5: one cause reached every output and scored 4; 1A counts consequences, only forbids inflating failure counts | Collides with the gateway warning (Q5) | Strongest lever |
| (d) List the requester acts on at once | r5 moved to 4 through writes to undo; Robert's false all-clear was consequential; Douglas's go/no-go; 1A: "A simple repair after the fact does not erase a consequential error" | Alone it still bounds: a wrong list with few items scored 3 | Raises stakes, needs (c) |

Record's best fit [I]: **(c) feeding (d), with few independent parts**. The natural reading should give the opposite of the truth for most of a small verdict set, and each verdict should drive a write or an immediate action. Nearest real case is the final Douglas [C]: truth is 2 on prod, 15 not. Runs 3 and 6 told Arthur 10 on prod (8 of 10 wrong), had 7/17 statuses wrong, and missed 7/15 Todo moves and comments.

Even that may stay at 4 [I]: 10/17 statuses, 8 moves, folder and share survive, which is the cushion Douglas rev 10 cited. To reach 5, the surviving parts must be few or themselves depend on the conclusion. Side tabs and independent deliverables reduce the chance of 5.

Gate value [R]: "Supported scores 3-5 clear this gate", and a /hardness pass "only allows continuation". A 5 gives no gate benefit over a 3. A design aimed at a solid 4 with a tail to 5 buys the same clearance.

## Q5. Limits: where pushing for 5 turns unfair
- **/prompt 2.7 [R]:** fails on a trap hint or riddle ("I have a nagging feeling the thing that actually bites us is not on anybody's list"), hidden destinations, "Unrealistic employee behavior", "Difficulty from precision, not complexity", and calls added to inflate work. [I] Stacked reversals of one answer risk the unrealistic-behaviour row if people flip without a business reason.
- **UGT 2.1 [R]:** FAIL when two supported readings give materially incompatible outcomes; "A leading or more-likely interpretation alone does not resolve it". The ruling-out passage must be persona-visible. BOTH_FAIR_FIGURE needs the same decision and writes, so it cannot rescue a one-decision task. Guide 06: "Never add ambiguity to make it 'harder.'" [I] Shape (a) sits closest to this line: thin evidence and unique truth pull in opposite directions.
- **Gateway warning [R, memory copy]:** "One early miss (a gateway doc) blocks many criteria together"; "Missing trap 1 must not block the others. If a gateway is unavoidable, make it findable and put the difficulty after it." Mastery's bimodality trap says the same (SB-T2). 1A allows a single cause to earn 5, but the pattern gate punishes it. Shape (c) must therefore be several independent routes to the same wrong conclusion, not one door.
- **Where /hardness would rule a miss a defect or reasonable reading [R]:**
  - "A reasonable answer to an ambiguous request is not a proven model error."
  - Unincorporated rules are excluded (`prompt-incorporation-v1`). SB-T1 fell from 48.7 % raw to about 80 % clean; its 9 all-fail rows rested on a handbook the prompt never named.
  - Missing capability, inaccessible data, platform outage and truncated exports are excluded. A truncated export leaves no score.
  - Runtime subagent failures are not counted, though the parent's choices after them are (r6, r7).
  - Wording that follows the sources stays minor: "Treating it as consequential would inflate severity" (r1).
  - /hardness flagged ENG-2158 as a key defect where the run's CLOSE was right (learnings §58).
  - Evaluators test the strongest counter-reading (Douglas email, Robert `/190`).
- **Fragile lever [I]:** Douglas and Julia lean on the `slack_read_thread` user-ID error. Douglas rev 10 kept it as an Agent error because "a retry was trivial", and noted the band held without it. A 5 should not rest on a tool quirk.
- **Row inflation [R]:** v2 calls "dozens of rows grading the same downstream effect of one miss" fake difficulty. It affects the average, not the /hardness band, which groups root causes.

## Q6. Six-run gates versus central failure: how Douglas did it
Douglas [R]: 51.9 / 71.0 / 44.6 / 51.9 / 73.6 / 44.6, average 56.3 %, pass@1 0/6, SD 0.117 (sample 0.129, unweighted 0.100), 4 patterns, largest 33 %, 17 all-fail rows all VALID.

| Layer [C] | Rows | Weight | Failed in | Carrier |
|---|---|---|---|---|
| Wall | 17 (incl. "2 on prod", "exactly 15") | 83 of 314 | all 6 | Inline comments on #38, #39, #46 (no run read them) |
| Tier 2 | 14 | 68 | runs 1, 3, 4, 6 | Arthur's single "Two things" reply-all: 547/553 off plus imports on 444, 531, 436 |
| Tier 3 | 5 (R17, R47 also failed run 2) | 23 | runs 3, 6 | Arthur's Confluence reply on 487 |

How this satisfies the gates [C/I]:
- The wall sets the average and caps the best run at 73.6 %, without affecting SD or patterns (an all-fail row "is in every pattern and doesn't separate runs").
- Two independent carriers on different surfaces create the spread: told-on-prod counts of 5, 9 and 10 against a truth of 2.
- So the headline failed 6/6 while the depth of failure varied. Central failure and spread are compatible when the headline sits behind a wall and the breadth sits behind independent carriers.
- Douglas was thin, though: unweighted SD sits on the 0.100 edge, runs 1/4 and 3/6 are identical pairs, and tier 2 is itself a one-email gateway.

Contrast [R]: Julia averaged 83.8 % with SD 0.099 and no all-fail rows, "one dominant scope choke point". Robert 85.7 %, SD 0.034. Frederick card 78.3 %, SD 0.054. Frederick handover 80.8 %, SD 0.161 (bimodal). The README shows handover as accepted; the rest as submitted. Acceptance of low-SD tasks is not recorded.

Tensions that remain [I]:
- /hardness grades one run, so a 5 needs a deep-failure draw. In Douglas 2 of 6 runs reached the deepest tier; that is a small sample, not a rate.
- Valid all-fail rows must each be justified, and Douglas's 17 share one root cause. The guidance also says a wall "doesn't count for this band", so patterns must come from the other layers.
- If every run collapses equally, SD falls below 0.1. If some escape fully, the bimodal SB-T2 shape risks SD above 0.3 and a dominant pattern.
- Workable target: wall on the headline, 2-3 independent carriers for breadth, and no run able to clear all of them.

## Bottom line
The record cannot prove a task earns 5, because none has. It supports a shape, not a recipe: a small verdict set, most verdicts inverted by evidence found through independent routes, each verdict driving a write, and few parts that survive independently.
