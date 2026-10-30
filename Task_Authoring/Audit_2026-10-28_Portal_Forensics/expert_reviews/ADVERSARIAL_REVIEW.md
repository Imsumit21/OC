# Independent adversarial review

Audit label: 2026-10-28. Review completed after the synthesis and stage reports were assembled. This is a challenge of the audit's evidence handling, consistency and causal claims; it is not a Portal evaluation or a fresh task-quality score.

**Disposition: review complete. No unresolved material internal contradiction was found in the reviewed suite after the corrections below.** Evidence gaps remain explicitly unresolved, particularly Reviewer D's task attribution, historical remote configurations and some run/input bindings. Completion of this review does not close those gaps.

## Scope and independently reproduced results

Reviewed: `README.md`, `INJECTION.md`, `PROMPT.md`, `OE.md`, `RUBRICS.md`, `PIPELINE_ROOT_CAUSES.md`, `RECOMMENDATIONS.md`, `TASK_VERDICT_HISTORY.md`, the mailbox provenance document, report/task manifests, canonical-slot snapshot and this reviewer's independent inventory. The read-only originals, authoring contract and report parser policy supplied the controlling evidence. The stage experts performed the deeper stage-specific source/code analyses; this reviewer did not independently recompute every universe claim made by every report.

| Challenge | Independent result |
|---|---|
| Complete local task scope | 29 top-level assignment roots: 22 current Task_Authoring, three completed, four archived; older batch snapshots also inspected. |
| ZIP-only report discovery | All **702 `.md`/`.txt` members in 13 ZIPs** read. No over-5-MB text member, nested ZIP or ZIP read error. The 25 members carrying actual final verdict headings have 20 distinct hashes; every one already belongs to the known external-report set. No ZIP-only distinct report discovered. |
| Copy versus report denominator | **89 primary report paths + two nested preservation copies = 91 extracted-file occurrences; 84 distinct report byte streams.** ZIP members are additional occurrences, not additional reports. |
| Issued final labels | **37 FAIL, 34 PASS, 13 NON-FAIL**, read from final verdict headings. Findings, filename words, scores, local predictions and templates did not substitute for final labels. |
| Independent manifest reconciliation | The independent 84-hash set and parent's `report_manifest.json` 84-hash set are identical. Every primary path still hashes to its recorded full SHA-256. |
| History accuracy | All **84 history rows**, representing 84 distinct reports, checked against original path, verdict line, SHA-256, execution status and score. Zero mismatches. |
| Task-matrix accuracy | All 84 matrix report entries checked against those same source fields. The three counted groups are exactly Reviewer A, Reviewer B and Reviewer C. Zero mismatches. |
| Rubric preimages | All **18 reviewed JSON digests** in the rubric appendix independently matched the listed retained JSON bytes. Zero mismatches. |
| Missing OE preimage challenge | Douglas D1's unmatched OE digest `3118b9e…` was additionally sought among ZIP text members and not found. The OE report appropriately states the narrower negative result rather than asserting the preimage never existed. |

Supporting evidence: `scratch/independent_inventory_scope.json` records the 29 roots, all 13 archive hashes and supporting-source hashes; `independent_zip_verdict_inventory.json` records ZIP report members; `independent_external_all_copies.json` records extracted paths/hashes; `independent_history_validation.json` and `independent_rubric_binding_validation.json` record the checks. `scratch/independent_final_review_validation.json` records the reviewed-suite hashes and final matrix/count checks.

## Issues found and resolved

| Issue found in draft | Evidence and correction | Final disposition |
|---|---|---|
| Reviewer B's latest rubric score was typed FAIL 2 in the README matrix. | Latest external `(11)` report is FAIL 1 / COMPLETE at `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_30_rubric_alias_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (11).md:180–182`. All six preserved Reviewer B rubric reports are FAIL 1. README matrix now says FAIL 1. | Resolved; labels/count unchanged, score corrected. |
| Injection's physical-copy denominator omitted two nested preservation aliases. | The copies under skipped `Eval_Sandbox/review_history/pre_fix_7ff46e0e/platform_01_injection.md` and `injection_fix_20261024/before/03_Injection.md` match existing hashes `4ac9782d…` and `41a855cd…`. `INJECTION.md:7`, `:63` now distinguish 39 primary paths, two nested copies, 41 extracted occurrences and 36 unique injection/hardness reports. | Resolved; unique corpus and task counts unchanged. |
| A recommendation described the current local rubric rule as an authenticated current Portal profile. | The current repository evaluator is directly inspectable; the deployed historical/remote profile is not fully authenticated. `RECOMMENDATIONS.md:9` now says the current **local** evaluator rule returns FAIL for one Major and requires remote-profile authentication separately. | Resolved; policy-version uncertainty preserved. |
| Douglas's later coherence FAIL was described as introduced by intervening hardening. | The original report explicitly says the defect already existed in revision 4 and the earlier prompt review missed it (`completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_1_prompt (1).md:315`). README, `PROMPT.md:126` and its causal table, and `RECOMMENDATIONS.md:44` now distinguish deeper-review discovery from proven edit-caused regression. | Resolved; source-coherence defect and verdict reversal remain valid, unsupported causal introduction removed. |
| Independent count report cited beyond the mailbox document's final line. | Mailbox document has 44 lines. References were corrected to its actual table and historical-coverage ranges. | Resolved; evidence content unchanged. |

## Counter-hypotheses tested

**“Four reviewers returned FAIL, so four sent tasks failed.”** Rejected. Reviewer D's original is a genuine FAIL, but the report expressly withholds the task ID; returned prompt/SQL hashes and scenario differ materially from the sent pair. The strict result is **three matched sent tasks, plus one genuine but unbound FAIL return**. The audit does not invent a second task for Reviewer D or assign blame for the replacement. Reviewer E's missing return is neither PASS nor FAIL. Earlier October 16/17 sends do not establish additional qualifying returns. Mailbox facts are explicitly attributed to the parent's separate Gmail inspection, not claimed as this reviewer's own mailbox reads.

**“The extra local groups prove more CB failures.”** Rejected. Current Julia, skipped Oliver, archived Arthur and completed Douglas contain additional preserved FAILs, but no located contributor-delivery binding establishes their inclusion. The current `task_inputs` folder contains Julia; old batch …TASK_W was Frederick. Arthur's report distinguishes a task ID from its attempt ID. Neither a reused path nor a 24-character report filename resolves those identity questions.

**“Every later FAIL is an authoring regression.”** Rejected. The corrected Douglas case is a deeper-recheck discovery of an older defect. Reviewer A's rubric PASS→FAIL uses changed JSON bytes; its later PASS is preserved separately. Reviewer B's injection timing finding remains advisory within an overall PASS. Other documented source edits genuinely change the incorporated task contract. The suite now states these cases separately rather than asserting universal same-input randomness or universal edit-caused damage.

**“OE repeatedly failed.”** Rejected. There are four PASS, two scored NON-FAIL 3 and one unscored NON-FAIL/PARTIAL OE reports, with zero FAIL. The Douglas provenance blocker does not become FAIL; the Reviewer A rubric FAIL/PARTIAL remains an issued FAIL because that report identifies an independent defect. None of the three initial CB-count triggers depends on a PARTIAL review.

**“Latest historical PASS certifies current files.”** Rejected. The suite preserves Reviewer B's separate externally passing OE, missing current canonical rubric, and later local rubric candidate; Reviewer C's redesigned SQL differs from historical PASS inputs; completed-folder labels do not certify every current byte. Reviewer A and Reviewer B current prompt/SQL exact matches are positively identified where supported, rather than applying blanket distrust to all history.

**“The create skills were absent, the gates were fake, or no checks existed.”** Rejected. Saved stage activity and genuine mechanical protections exist. The suite distinguishes recorded activity, digest-current certificates, attested semantics and authenticated invocation transcripts. A printed model name or generated filename does not independently prove reviewer independence or a skill invocation. Current tool-policy hashes do not reconstruct all historical Markdown or remote evaluator versions.

**“More structural checks alone solve the observed problems.”** Rejected. Recommendations retain actual digest/upstream/freshness/static/source controls and specify additional semantic counterexamples, field-aware repair closure, stage-scope receipts and run-to-input evidence. The new immutable handoff/run envelope is distinguished from already-existing local digest and model checks. Recommendations do not claim a missing count check where one already exists, silently change the assignment, harden a rubric merely to lower scores, or authorize a new paid run or outreach.

## Limits that remain valid after review

- The count is three confirmed attributable failed sends **across located histories**. It is not an exhaustive all-time census of unknown communications.
- Original reports establish what was reported for their stated inputs. Their presence does not independently authenticate every underlying source fact, reviewer action or remote execution.
- Historical source/evaluator/clock preimages and some runtime input/reset/batch envelopes remain unavailable. Current code inspection cannot settle those historical facts.
- No audit fix, Portal operation, paid run, SQL execution, outreach or original-file edit was performed. No audit action was denied or has an uncertain external mutation outcome.

The count, scores, chronology qualifications, current-versus-reviewed distinctions and recommendations are internally consistent within those stated limits. The remaining uncertainty is evidence uncertainty, not an unreported contradiction that this review treats as resolved.
