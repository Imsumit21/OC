# Vincent: ZM store candidates QA gate (archived 2026-11-06)

Persona Vincent Parker (Game Systems Engineer) · Long Horizon · Engineering / Engineering Ops / Analysis and synthesis · difficulty mode easy (cap < 90%) · universe date Oct 1, 2025 (synth-cut, clock 2025-10-01 00:00 PT) · platform attempt 6ae9909f7b5249d3148f3707 (id from the eval reports).

Prompt (4 sentences): run the QA gate on Arthur's ZM store candidates (Android Submission #135, iOS Submission #50), put the register in a new tab of the release gate sheet, add the blockers to the release ticket's description, file a new ZM ticket for anything the QA regression runbook's checks turn up that nobody filed, and reply in Arthur's #zombie-bugs thread with the QA call before Friday's go/no-go.

## Final state

| Slot | State |
|---|---|
| `01_Universe_Inject.sql` | rev 18; /injection PASS (9 rounds; rounds 2 and 3 FAIL, the rest PASS) |
| `04_Prompt.txt` | /prompt PASS 5 on the 7th round (6 FAIL rounds, all Unique Ground Truth or Cross-Service Coherence 2) |
| /hardness | FAIL, then NON-FAIL (Opus observed) |
| `08_Oracle_Events.md` | 35 events; /oe PASS 5 in the report saved as `_2_oe.md`; the two other saved copies are PASS 5 and NON-FAIL 3 |
| `09_Rubrics.json` | 67 rows, weight 227; platform /rubric FAIL 1 twice (70 rows, then 67 rows with one Major on R66); both run-2 fixes applied (R1 evidence, R66 thread guard); independent local DELTA re-run (GPT-6.1 Sol lead + R1-R7) PASS 5 on sha b55e4891f421; platform re-run result not recorded here |
| `10_Baseline_Verifier_Results.md` | 6/6 completed, 0 full passes, weighted 77.5 / 77.5 / 75.3 / 73.1 / 88.5 / 77.5 = **78.3%** average (easy cap < 90% PASS); across-run population SD 0.049 FAILS the 0.1-0.3 spread band (low observed spread) |
| `11_AF_Justification.md` | 3 all-fails, all VALID: R5 (ZOM-293 BLOCKER), R40 (exactly 18 existing blockers on ZOM-570), R41 (ZOM-293 on ZOM-570); allfail gate FAIL only on the upstream `chain.rubric-check` (25 PASS, 1 FAIL, 1 WARN) |
| `05_Human_Time.md` | 18.75 h (worksheet gate PASS) |

## Key answers

133 register rows (112 open in scope + 20 moved to Done after the Android #127 cut 2025-09-22 12:30:43 UTC + the new ticket); 19 blockers (DES-313, ZOM-293, 435, 449, 458, 473, 483, 535, 546, 554, 559, 560, 562, 567, 569, 573, 576, 578 and the new iOS N-1 update save-reset ticket); QA call NO-GO in Arthur's thread C08R27X0EAH/1759263900.484190. Every Opus run called ZOM-293 NO CALL (its symptom lives only in Vincent's Jul 3 comment) and most missed ZOM-458 / 473 / 535 (Brian's Turkish DMs) or ZOM-562 (the playtest vendor's mail).

## Why it took so many iterations, and what to change in the pipeline

1. **Unique Ground Truth took 6 /prompt rounds.** Every round found one more register cell that two of Leonard's rules could decide (ZOM-564, ZOM-477 / ZOM-558, the n/a vs in candidate build status, Done-but-still-failing tickets) or one injected record that contradicted base data (Arthur's #36 comment vs the backend start script, Brian's "1.3.24" vs the App Store version). Fix in the pipeline: before the first /prompt, run a mechanical **decision sweep** over every register row (rule, deciding record, competing rule) and a **base-data contradiction scan** on every injected record that names a version, build or deploy. The rev-17 sweep found the last fork in one pass; it should run at rev 1.
2. **The local rubric eval is older than the platform's.** Our `Evals` release (manifest c5b89f4c…) has no `scope_tail` lint and no "bare count guard only with a real decoy" rule; the platform's (81446b85…) has both. Three local review rounds predicted 5/5 and the platform still failed it twice. Fix: sync the Evals package before each /rubric round, and add `scope_tail` (a required write joined to "only" / "no other") to `hg_rubric_lint.py`.
3. **Incorporation scope must be carried into the rubric review.** The platform /prompt report recorded "How we gate is incorporated" and "the QA Regression Runbook's checks are incorporated only for the new-ticket ask". Local GPT reviewers that did not see it called the tab-name row unauthorized and demanded five runbook sign-off rows; the platform then required the tab name and rejected the runbook rows. Fix: `/create-rubric-writing` should copy the prompt report's incorporation chain into the plan, and local /rubric runs should receive the platform reports as run-1 context (DELTA emulation matched the platform; blind FULL runs did not).
4. **Rubric structure rules the platform enforced:** no "only" / "no other" tails (use one bare count guard per write kind, only where a real decoy exists: the Sep 22 tab, a new top-level post); count rows count pre-existing tickets only so they don't cascade with "exactly one new issue"; a guard on a thread counts threads, not messages; delete rows that cannot fail on the task clock (a deadline two days after the clock); put every accepted surface (title, description, comment) in the title, not only in the evidence; never reconstruct a literal (the Trello URL is the anonymized host the tool returns; grade a path fragment like `/c/pTbZYXdb`); five samples per group, direct rulings protected.
5. **Weights flip-flopped** between reviewers (ZOM-563 rows 5 → 3 locally, back to 5 on the platform). The platform's rule: tracing the deciding record across services is 5, a direct mapping once another row's ruling is known is 1. Write that into the weight guidance.
6. **Builder paste errors are real.** The platform copy had R20 at weight 5 against 3 locally; only a field-by-field diff of the builder export caught it (229 vs 227). Add a tool: `diff_builder_export.py <export.json> 09_Rubrics.json` that reports any field mismatch.
7. **Baseline files landed in the wrong slot.** The graded baseline was saved at the top of `task_inputs/` while `07_Baseline_Trajectories/` still held an older set; `difficulty_stats --build` bound happily to the wrong set. Matching each verifier run's new tab id to the export fixed it. Fix: `difficulty_stats --build` should check content binding (ids the verifier quotes must occur in the bound trajectory) and refuse a mismatch.
8. **Stage-gate chains block on a structural finding.** `diversity.authority_share` fails by construction when one rules doc defines the population (here and on the Robert, Douglas, Julia and Frederick tasks), so rubric-writing never PASSes and every downstream gate (rubric-check, allfail) fails `chain.*`. Fix: a recorded human acceptance of a structural finding should satisfy the chain.
9. **The shortcut probe is slow and noisy.** 60 min cold, 58 HITs, nearly all generic words (BLOCKER, FIXED, level 3) in old records. Fix: weight acceptance values by distinctiveness or drop vocabulary that the How we gate tab itself defines.
10. **Independent reviewers run out of steps on collection-wide checks** (the 132 population, 19-blocker completeness, absence of an existing ticket) and are often denied the shell. Split such checks into their own pass with a read-only parse helper; a DeepSeek worker with Python re-derived every per-run all-fail fact in one pass.
11. **Difficulty: low spread.** All six runs failed the same three rows; across-run population SD 0.049. With friction off, spread comes only from independent traps that runs miss at different rates (Brian's Turkish DM, the vendor mail). Plan at least two such independent traps per easy task.

## Layout

`task_inputs/` the slot as last worked (Working_Files holds the rubric builders under `rubric/`, the solver, forensics, and the superseded 22:17 baseline under `run_forensics/baseline_superseded_2025-11-05_2217/`); `eval_reports/` every platform report (injection ×9, prompt ×7, hardness ×2, oe ×3, rubric ×2); `work/` local analysis scripts (platform fix applier with old-value asserts, all-fail extractor, quote checker, Snowflake shortcut check). Scripts may hard-code `/Users/sumitkumar/...` or `/tmp/rubricwork` paths.
