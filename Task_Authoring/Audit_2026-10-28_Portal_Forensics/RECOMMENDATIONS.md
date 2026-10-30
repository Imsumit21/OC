# Recommended changes and regression cases

These recommendations are derived from the preserved failures and the code actually inspected. **None are implemented by this audit.** Priority reflects repeated cost and risk of invalid handoff, not a statistical attribution of all 37 historical FAIL reports. Existing digest, upstream, source-context, static rerun, fairness and release checks should be retained.

## P0 — Make the review contract explicit before another repair loop

| Proposed change | Evidence and reason | Acceptance test |
|---|---|---|
| Store a single selected evaluation profile with literal assignment, resolved freeze, source/environment fingerprint, applicable rule versions and known local exceptions. Surface conflicts before downstream drafting. | Local October freeze is 00:00Z; Portal October reports use 07:00Z. Rubric authoring uses older percentage bands while current local evaluator fails any Major/Moderate. `GEN_EXECUTION.md:60`, `:159`; `playbooks/09_Rubric_Writing.md:205`; `Evals/3_Rubrics_Eval.md:36`. [OE.md](OE.md), [RUBRICS.md](RUBRICS.md). | Given otherwise identical bundles with 00:00Z and 07:00Z cutoffs, return explicit context mismatch. A source at 00:45Z cannot silently be pre-freeze in both. A 27-row rubric with one Major must use the selected profile's rule; the current local evaluator rule returns FAIL despite 3.7%. Authenticate the remote profile separately. Do not resolve conflicts by changing assignment or tightening a rubric. |
| Carry completion scope with the package/status. Separate local preparation, external quality, observed hardness, six-run difficulty and full release. | Batch CLEAN intentionally means four gates; `batch/TASK_RUNBOOK.md:5`, `:111`; `batch/verify_task.py:8`. [PIPELINE_ROOT_CAUSES.md](PIPELINE_ROOT_CAUSES.md). | A four-gate package remains a valid preparation package but cannot present an external quality/release PASS. A scored NON-FAIL3 differs from NON-FAIL/PARTIAL with no score. Existing cancelled Reviewer E loop remains cancelled. |
| Bind each returned report to canonical task ID, attempt ID, exact inputs, semantic context and review version; keep a separate unmatched-return state. | Reviewer D returns a different scenario with no confirmed task binding. A reused default folder now contains Julia, not the older TASK_W Frederick assignment. [INDEPENDENT_COUNT.md](expert_reviews/INDEPENDENT_COUNT.md). | Reviewer D's sent/returned pair stays UNBOUND despite same recipient. Julia's FAIL cannot attach to TASK_W by folder alone. Renamed duplicate report bytes do not increase task/report execution counts. |

These changes require an explicit selection of the intended review contract where current sources disagree. The audit does not decide that policy by silently editing clocks, difficulty assignments, authorship rules or Portal documents.

## P0 — Stop treating a well-formed review as semantic clearance

`stage_gate.py` already checks meaningful bindings and mechanical outputs. The specific gap is that several semantic reviews are represented by nonempty tables, pointer-shaped cells or attestations. `stage_gate.py:609`, `:618`, `:2085`, `:2285`, `:2360`; `v3_artifact_checks.py:134`. [PROMPT.md](PROMPT.md), [OE.md](OE.md), [PIPELINE_ROOT_CAUSES.md](PIPELINE_ROOT_CAUSES.md).

Recommended implementation boundary:

1. Make every recorded blocking finding and dimension result machine-readable. Compute readiness from them; do not only check that a readiness label or seven-row dimension table exists. Keep issue severity, overall verdict and execution/solvability status separate.
2. Store each decision as an authorized ask, source versions, applicability time, accepted outcome class, strongest alternative, material difference and evidence excluding or accepting it. The current brief already asks for alternatives; check the relationships and outcome differences rather than adding another “reviewed” checkbox.
3. For deterministic facts, assert exact source selector, extracted value and transformation. For semantic interpretation, require independent review of the frozen candidate and named counterexamples. Machine checks cannot establish every natural-language inference; their output should say which claims remain reviewer judgments.

Required regression cases include:

| Case from this corpus | Expected behavior |
|---|---|
| Zero SQL lint flags but a second identity for the existing Transcend partner | Semantic identity check rejects the distinct-person claim after matching base history; lint success remains recorded honestly. Reviewer C initial report `.../iteration_01/6ad90e9fa38cc384483b1c80_0_injection.md:29`, `:103`. |
| Reviewer A closed item with no live card; one versus three installment holds | Material alternatives must be settled in authorized source rules or both accepted where allowed. A populated alternative table alone cannot establish one write set. [PROMPT.md](PROMPT.md). |
| Reviewer B fix installed/deployed but production switch off | Distinguish installation, current service, dated service, dev state and plans. A source edit must trigger re-evaluation of every dependent status and output. [PROMPT.md](PROMPT.md), [RUBRICS.md](RUBRICS.md). |
| Finding is marked Major while dimension table/readiness says CLEAN | Recomputed selected-profile verdict blocks contradictory clearance. Explanatory prose cannot override a proved defect. |
| OE sign-off cell contains a valid-looking pointer but its claimed record subtype is wrong | Structural pointer check can PASS; fact check must identify the wrong subtype rather than claiming independent reread proof. Reviewer B OE10, [OE.md](OE.md). |

## P1 — Preserve outcome invariants through hardening

Create a dependency map from each edited source fact/rule to prompt requirements, expected writes, OE nodes, rubric facts and run inputs. Existing file digests catch staleness; they do not determine whether the revised facts still yield one authorized outcome. Retain the actual upstream/freshness gates and require semantic recheck where the map changes.

The most valuable regression cases are the observed repair transitions:

- Reviewer A: ambiguous outcomes → explanatory casework added to prompt → contrived prompt FAIL → rules clarified in source records → NON-FAIL. Verify the final source repair resolves the original four forks while the request stays natural.
- Reviewer B: prompt PASS plus injection PASS → production-state hardening → new status and QA-recheck forks → source fallback/scope repairs → prompt PASS. Recheck “no applicable re-check” versus “re-check reports recurrence,” and branch-APK pass versus actual submission-build status.
- Reviewer C: date/reporting-date repair → a second clock interpretation → source clarification → PASS; later full redesign must not inherit that historical PASS.
- Douglas: deeper recheck finds pre-existing fixed-and-verified comments on Todo/Backlog tickets → coherence FAIL → source alignment → PASS. The FAIL report explicitly says the earlier review missed the revision-4 defect (`completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_1_prompt (1).md:315`); introduction by the intervening hardening is not established.
- Julia local review: appended mail-reply correction must update the earlier UGT alternatives that still accept Slack-only delivery. Append-only prose is insufficient when the contract table remains stale.

Source histories and exact report hashes are in [PROMPT.md](PROMPT.md) and [TASK_VERDICT_HISTORY.md](TASK_VERDICT_HISTORY.md). These tests should check the intended outputs and accepted alternatives, not mirror the implementation's wording.

## P1 — Demonstrate difficulty with valid work, not declared volume

The corpus shows SQL integrity success alongside hardness FAIL. Large cohorts, many services and injected decoys do not prove that the critical inference is difficult or that the proposed per-record calls are necessary. Conversely, a 403 on a required destination is an environment failure and must not be counted as model hardness. Reviewer C's Portal report excludes that defect correctly. [INJECTION.md](INJECTION.md).

Recommended checks:

| Proposed test | Expected result |
|---|---|
| Bulk/list surface exposes all facts declared to need one read per record | Recalculate necessary-call budget; do not preserve the larger declared floor by renaming rows. |
| One summary explicitly states all decisive QA verdicts and local build mapping | Identify the short route and explicitness; adding unrelated rows does not repair it. |
| One rule card governs many rows but each row genuinely needs different evidence | Distinguish a shared authority from an answer shortcut; do not mechanically call every central rule invalid. |
| Model meets all core asks while proposed decoy is ignored | Hardness conclusion reflects the observed usable result. It is not repaired by grading an unauthorized ask. |
| Destination is read-only or runtime capability is unverified | Separate environment/capability limitation from model error. |
| One observed failure propagates into three outputs | Record one root failure pattern and three affected outputs, rather than inventing three independent failure mechanisms. |

Measure corrected difficulty only after the rubric is fair and the relevant input/run binding is established. No paid run was needed or performed for this audit.

## P1 — Repair rubric predicates and preserve tested alternatives

The core repair unit is the title's acceptance predicate. Source correctness, atomicity, weight and title-only self-containment must be evaluated together. An evidence-field edit does not change what the judge is instructed to accept. [RUBRICS.md](RUBRICS.md).

For each row, retain a small frozen bank of correct outputs, plausible incorrect outputs and borderline representations. Every revision should show which examples changed verdict and why. Required cases from the repeated rows:

| Rubric behavior | Regression expectation |
|---|---|
| Status row R27: current live claim, Pending heading, dated deployment, installed/prod0, dev-only, future plan, other-change contrast | Accept the source-authorized status semantics; reject actual current production-live misclassification. Do not let broad heading-override or clearing-word logic cancel a correct Pending label or excuse a wrong Live entry. |
| Count row R29: one entry with history/details, alias paraphrase, nested lines, separate listed changes, incidental mention | Count listed change entries under an explicit rule. Keep status accuracy independent so one wrong live claim does not create a cascade across status and count rows. |
| “Any name or paraphrase counts” | The title must still identify the target and define an acceptance rule. Test accepted source paraphrases without making supporting evidence carry the missing identity. The evaluator's acknowledged earlier guidance error must be retained as provenance. |
| Reviewer A annual/yearly/full-year wording versus the superseded $25K bill | Accept fair wording under one substantive value rule; reject the wrong payable amount. Avoid a fragile vocabulary list with a missing valid phrase. |
| Reviewer B Brian Slack identity and one-level weight issue | Assert both title and weight changed when the finding requires them; changing evidence alone is not a completed repair. |
| Wrong recipient/destination/population or omission from required final reply | Each authorized result has a title predicate rejecting the wrong output on the correct artifact. Preserve fair alternative routes. |
| No actions taken at all | Exclusion/preserved-state rows must not make an idle response look successful while mandatory writes are absent. |

Keep earlier passing versions and examples. If a suggested fix later fails on the same established example, identify whether author implementation differed, the test was missing, or evaluator advice was wrong. This is more diagnostic than another unchecked rewrite or a universal claim that Portal is inconsistent.

## P2 — Strengthen runtime and promotion provenance

Current precheck/release checks establish that a completed-looking trajectory exists, but do not authenticate the run against the opening prompt, SQL revision, universe/reset state and batch. The Reviewer B intake retains seven distinct sessions and missing run-envelope information; candidates were correctly held separately. `stage_gate.py:1730`, `:1846`; `difficulty_stats.py:644`. [PIPELINE_ROOT_CAUSES.md](PIPELINE_ROOT_CAUSES.md).

Recommended additions:

1. Preserve a run envelope with canonical task/attempt/session ID, exact prompt/SQL/reference/config/assignment hashes, source/environment revision, reset state, model ID and terminal result. Reject duplicate run IDs and ambiguous slot mapping before treating six files as six independent baselines.
2. Test model extraction against the actual `[1m]` suffix trace variant. Report parser uncertainty without editing raw model labels or relabeling runs to obtain a preferred score.
3. Preserve exact uploaded artifact bytes, report bytes, selected policy context and a promotion receipt. Verify canonical existence/hash again when packaging; a historical copied-and-verified receipt cannot prove a file still exists later.
4. Keep current-canonical, externally reviewed and review-candidate states explicit. Reviewer B's passing OE and current OE differ; latest external rubric FAIL and later local PASS grade different JSON versions. Avoid using any of these as another version's status.
5. Refresh dependent counts, headers, certificates and status indexes after promotion. Several completed/archived OE headers are stale; current count predicates already detect them. Add those as regression examples instead of inventing a missing count-check feature.

## P2 — Version the full effective rule bundle and retain invocation evidence

The current tools digest matches the five named tasks' saved core certificate policy prefix, so current code is relevant to those certificate claims. It does not cover every skill Markdown, playbook, guideline or external evaluator preimage. Older archived/completed runs show different paths, profiles and digest schemes. `PIPELINE_ROOT_CAUSES.md` records this limitation and the actual evidence per task.

Record create skill identity, full source digest, playbook/contract versions, command arguments/task context, reviewer identities and tool outputs for future runs. A file named `04_Prompt_Check.md` should be treated as an artifact, not a recovered invocation trace. Preserve the original logs so the audit can distinguish a missing safeguard from a safeguard that was required but not performed. Never infer intent or rule compliance from filename alone.

## P3 — Calibrate against this corpus without overfitting

Use the demonstrated repaired successes as negative controls: Reviewer A's current exact-pair NON-FAIL, Reviewer B's final prompt PASS, all four OE PASSs and Douglas's repaired rubric PASS. A new check that rejects all those examples would be an overcorrection. Historical skipped ID-naming/cache findings must retain their evaluator version and scope; same version labels can hide changed document hashes.

Maintain report provenance separately from truth adjudication. A Portal report proves what was reported for its bytes; source facts still require source evidence. Track false positives, accepted alternative repairs, advice reversals and pending provenance independently. Prioritize exact observed defects over speculative global restrictions, and do not use this audit to revive cancelled contributor communication.
