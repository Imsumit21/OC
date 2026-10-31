# Final pre-implementation review

Review date: 2026-10-30. Repository: `/Users/macbookpro/Downloads/OC`. This is an addendum to the October 28 audit, not a rewrite of its historical snapshots. Three focused reviewers rechecked recommendations, evidence/provenance, and implementation sequencing; the primary reviewer inspected the current code and exact Reviewer B paths. Only this new report was written. No pipeline change, task repair, test/gate execution, paid evaluation, SQL execution, email, commit or push was performed.

## Verdict

**READY TO START BOUNDED IMPROVEMENTS.** The forensic audit is complete enough to support implementation. Another broad audit is unlikely to improve the next decision. Begin with the ordered work packages below, preserving their policy prerequisites and acceptance checks.

This is a readiness judgment, not implementation authorization, Portal acceptance or certification of current tasks. It does not endorse applying every recommendation at once. Changes to clocks, scoring bands, assigned difficulty, authorship policy or historical grades require their own explicit contract decision; the audit does not silently select those policies.

No critical factual correction changes the audit's count or main diagnosis. Several implementation clarifications below prevent overbroad fixes. The outstanding evidence gaps do not block isolated parser/status/predicate improvements; they do block claiming remote equivalence, authenticated old runs, or final release.

## Current evidence and repository state

The October 28 evidence was compared with current bytes without rerunning the audit scripts, which would overwrite historical outputs:

| Current read-only check | Result | Historical reference |
|---|---|---|
| Main delivered audit files | All 17 match their full recorded hashes | `evidence/delivery_manifest.json` |
| Imported original reports | All 84 primary report hashes match; all 91 alias paths and final-verdict lines match | `evidence/report_manifest.json` |
| Named artifact versions | All 446 match | `evidence/artifact_version_manifest.json` |
| Current rule/tool/provenance sources | All 130 match | `evidence/source_rule_manifest.json` |
| Canonical-slot existence/hash observations | All 88 match | `evidence/canonical_slot_snapshot.json` |
| Known imported-report naming/location census | 89 current primary paths, matching the 89 baseline primary paths; no added/missing path in that bounded census | Standard attempt-prefixed reports, preserved Portal/eval directories and the two initial nonstandard Reviewer B names; two nested copies checked separately via aliases |
| Previously inspected ZIP archives | All 13 full archive hashes match; no archive was rewritten or extracted | `scratch/independent_inventory_scope.json` |

The current sorted-concatenation SHA-256 of `Task_Authoring/tools/*.py` remains `4459b8bdd4decccf64864a4fa2e52c9906544d40ade65c7bf4e12550b3d35991`. Thus the October 28 static code findings still describe the inspected implementation. The working tree remains dirty, including `.gitignore` and search-cache entries; those edits were preserved. Git's latest displayed commit is `931fdfb`, dated October 24. Neither Git status nor the selected manifests establish the history of every untracked file.

These checks establish unchanged **inventoried evidence**, not an exhaustive census of new arbitrary report names, changed universe data or later mailbox activity. No mailbox search was repeated. The historical count remains **three attributable sent-task FAILs**—Reviewer A, Reviewer B and Reviewer C—with Reviewer D's different-scenario return unbound. The preserved corpus remains **84 distinct report byte streams: 37 FAIL, 34 PASS, 13 NON-FAIL**, including **zero OE FAILs**. Historical metrics must remain dated, not advertised as a new October 30 all-channel count. Sources: `evidence/MAILBOX_PROVENANCE.md:7`, `evidence/task_matrix.json`, and `expert_reviews/INDEPENDENT_COUNT.md`.

No applicable `AGENTS.md` was found in the repository or inspected ancestors. `.agents/skills/create-*` still resolve to the repository's `Task_Authoring/skills/` sources; evaluator skill links resolve to `claude/skills/`. This review inspected guidance and code; it did not invoke an authoring skill or infer historical invocation from a filename.

## Reviewer B canonical rubric: current observation

At **2026-10-30T21:17:31.238171Z**, the exact path

`/Users/macbookpro/Downloads/OC/Task_Authoring/task_inputs_TASK_B/09_Rubrics.json`

returned **FileNotFoundError / errno 2 (ENOENT)** for both `lstat` and direct read. Its exact parent exists as a normal directory (`drwxr-xr-x`) and is not a symlink. Listing only that directory confirmed that the canonical filename is absent while `Audit-Report`, `Working_Files` and the other task slots remain present. This is a missing directory entry, not a permission failure or a dangling target symlink.

The intact candidate at `Audit-Report/iteration_30_rubric_alias_repair/candidate/09_Rubrics.external_review.r30.v5.json` is a regular, non-symlink file: **36,928 bytes, 45 criteria, weight 149**, SHA-256 `34d1d4f11d0182d7f4cf61f3b751b5f04beae354e8bab6b78662334af6df5042`.

The earlier canonical-slot snapshot records absence at **2026-10-28T23:23:05.216471Z**. The historical iteration31 copy receipt records a successful fill at **2026-10-28T17:32:54.259398Z**. Both observations are preserved. The audit does not establish what happened between them, who changed the path, or whether it was manually moved afterward. No restoration was attempted. The candidate's later local PASS is not an external PASS, and the latest preserved external FAIL concerns prior rubric bytes. Sources: `evidence/canonical_slot_snapshot.json`; Reviewer B `Audit-Report/iteration_31_canonical_rubric_fill/copy_verification.json:2`; `RUBRICS.md`.

This missing canonical file is a task-promotion issue, not a reason to block isolated improvements to the pipeline. A later task-repair action must be separately scoped and must not silently occur as part of a test or migration.

## Clarifications to apply when implementing the recommendations

These addenda take precedence over an expansive reading of the existing recommendations. The original reports and snapshots remain unchanged.

1. **Enforce selected-policy blocking outcomes, not every finding or every NON-FAIL.** `RECOMMENDATIONS.md:21` correctly asks for readiness reconciliation, but this must preserve a scored COMPLETE NON-FAIL 3/4, distinguish unscored PARTIAL/BLOCKED, and retain independently demonstrated FAIL/PARTIAL. Existing report contracts make these distinctions (`Evals/tools/hg_report_contract.py:90`). The authoring rubric playbook explicitly permits a scored NON-FAIL to proceed when its local gate passes with no validity defect (`Task_Authoring/playbooks/09_Rubric_Writing.md:288`). Existing `rubric_validity()` is a stricter local binary control, not proof that all external NON-FAILs are invalid (`Task_Authoring/tools/stage_gate.py:1642`).

2. **Keep diagnostic causes separate from the operational difficulty-pattern algorithm.** The phrase “one root failure pattern” in `RECOMMENDATIONS.md:62` should be implemented as **one causal mechanism with three affected outputs**. Existing failure-pattern grouping uses failed-rubric sets and single linkage (`Task_Authoring/tools/difficulty_stats.py:205`; `setup/GEN_EXECUTION.md:180`). Do not replace that algorithm with causal grouping or retrospectively change scores under this recommendation.

3. **Extend existing duplicate checks.** Unique nonempty rollout IDs and duplicate filename-derived run slots are already checked (`difficulty_stats.py:140`, `:644`). New provenance work concerns the same underlying session/trace being copied under different valid names and the binding of actual runtime inputs. It is not a request to add duplicate-ID checks as if none existed.

4. **Scope positive controls to their original stage, bytes and policy/context.** A passing historical fixture should preserve its recorded stage outcome under that contract. It must not automatically clear canonical promotion, a different clock or full release. Reviewer B's passing OE is the concrete example of a separate clock/context held from adoption (`OE.md:68`). Likewise, an individual preserved-state criterion may legitimately pass when the agent is idle; the **rubric suite's mandatory-write rows** must reject an idle submission. Do not require each valid exclusion criterion to grade unrelated writes.

5. **Do not substitute a broad new architecture for the first bounded fixes.** Typed result reconciliation and frozen output examples can be added before a comprehensive claim/dependency schema. The source-code gaps below are inspectable, but no crafted full bundle was run to demonstrate a live bypass. Controlled regression fixtures should establish the exact behavior before implementation expands.

6. **Retain normalized certificate hashing alongside raw delivery identity.** Replacing `file_digest()` globally with raw bytes would make a document stale when its own certificate is pasted. Existing normalization is intentional (`stage_gate.py:352`). Add raw SHA-256/length for delivered artifacts separately, version any new certificate format, and keep stage-specific sidecar projections (`v3_artifact_checks.py:19`) to avoid freshness cycles.

## Ordered work packages

The order below makes the next change reviewable and keeps policy decisions separate from maintenance. Acceptance checks are proposed future tests, not tests executed during this review. Use isolated fixtures and temporary roots; existing `Task_Authoring/tests/test_v3_stage_gate.py:20` creates a test directory inside the real search cache, so test isolation needs to be explicit before broad regression execution.

### WP0 — Freeze the acceptance matrix and regression controls

**Scope:** choose and name the intended local profile for each changed behavior, retain the literal assignment/source/clock and declared local exceptions, and encode the stage/status cases as small fixtures. Preserve a separate remote-profile UNKNOWN/mismatch state. No new evaluation or policy rewrite is required merely to build this matrix.

**Acceptance:** cover COMPLETE PASS; allowed COMPLETE scored NON-FAIL; unscored PARTIAL/BLOCKED; proved FAIL/PARTIAL; an active blocking finding despite CLEAN prose; a resolved historical finding; missing/invalid metadata; and policy/clock mismatch. An October 00:45Z source cannot be pre-freeze under both 00:00Z and 07:00Z contexts. A 27-row rubric with one Major follows the named profile rather than an unlabelled global rule. Old authoring bands (`playbooks/09_Rubric_Writing.md:205`) and current local evaluator bands (`Evals/3_Rubrics_Eval.md:36`) must not be silently merged.

**Exit condition:** the intended outcomes are explicit enough to test. If the desired scoring/clock contract is unresolved, defer that behavioral branch while allowing unrelated maintenance to proceed. Do not edit read-only `Evals/`, `claude/` or base exports to force alignment.

### WP1 — Fix the narrow documented model-label incompatibility

**Scope:** the Opus 5.5 matcher at `difficulty_stats.py:165` rejects the documented `[1m]` suffix variant. Correct that narrow compatibility issue independently of broader model extraction or scoring changes. Preserve all raw trajectories.

**Acceptance:** accept the documented variant and existing supported spellings/date suffixes; continue to reject wrong, missing and mixed models. Extend the relevant existing tests (`Task_Authoring/tools/test_difficulty_v3.py:81`, `tests/test_v3_stage_gate.py:261`). Demonstrate that parser maintenance changes provenance classification only where warranted; it must not invent task/input/reset provenance or a Portal result.

### WP2 — Reconcile declared results with stage readiness

**Scope:** implement a pure, versioned result aggregator under WP0's selected profile; integrate it with the existing checks rather than replacing them. Current prompt-check validates status-label presence (`stage_gate.py:2190`), OE-ledger recognizes READY or BLOCKED structurally (`:2259`), and OE-check accepts prediction/tally syntax without itself requiring zero blocking findings (`:2298`). Release separately requires supported OE solvability and zero blockers (`:1825`). Rubric-check already has selected binary validity protections, but not comprehensive dimension/readiness reconciliation (`:2360`).

**Acceptance:** a genuinely blocking applicable finding prevents a current handoff PASS despite contradictory CLEAN prose; a permitted complete NON-FAIL can proceed; unresolved evidence is not silently upgraded or recoded as an external FAIL; a historical resolved issue does not block a new clean result. Use actual parsed findings/dimension fields, not unscoped substring matches across historical appendices. Missing or malformed current results cannot produce clearance.

Also add a **latest-result supersession fixture**. `chain()` and release select the last PASS block rather than the latest result of any verdict (`stage_gate.py:981`, `:1796`). Test an older digest-current PASS followed by a newer applicable FAIL/PARTIAL and define authoritative revocation semantics before changing selection logic. This is a static lifecycle concern, not a demonstrated live bypass. Preserve earlier blocks as history.

### WP3 — Add a versioned handoff/promotion inspector

**Scope:** report canonical task ID separately from attempt ID, preparation scope separately from Portal/difficulty/release state, exact raw artifact identity separately from normalized certificates, and canonical/reviewed/candidate roles separately. Recheck existence and hash at packaging. A first implementation can be a read-only inspector; a new identity service or automatic migration is unnecessary.

**Acceptance:** Reviewer D's different scenario remains UNBOUND; Julia does not inherit the old default folder's task ID; a four-gate package remains valid preparation without claiming Portal approval; a historical promotion receipt does not prove current existence; Reviewer B's absent canonical rubric is reported without copying the candidate automatically. Exact duplicate report bytes do not increase report-execution or task counts. Missing historical metadata remains UNKNOWN/INFERRED/HISTORICAL with provenance.

### WP4 — Add predicate examples and source-change regression checks

**Scope:** start with the failures already supported by source evidence. Preserve valid/invalid output examples for rubric R27/R29, Reviewer A's annual-payment wording and hold/write alternatives, and Reviewer B's production/installation/dev/history distinctions. Verify that title and weight repairs actually change the required fields. Track affected requirements, OEs, rubric facts and matching-run applicability incrementally.

**Acceptance:** reject the established wrong outputs and accept fair paraphrases/alternative routes under the original contract; keep status accuracy and entry counting independent; the full rubric suite rejects omitted mandatory writes without forcing every exclusion row to reject inactivity. A source edit reopens affected semantic checks; unaffected facts can remain reusable. Reviewer B's installed-versus-serving changes are genuine source-rule regressions, while Douglas's later report explicitly says it discovered an already-present missed defect (`completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_1_prompt (1).md:315`). Do not rewrite that history as edit-caused introduction.

Do not turn multiple fair outcomes into a new unique-answer requirement, add rubric demands to depress scores, or treat an evaluator's previously suggested phrase as sufficient repair proof. Preserve the documented evaluator advice reversal and the tested counterexamples.

### WP5 — Strengthen run binding before baseline promotion or release claims

**Scope:** supplement existing model/completion/slot checks with exact run/session identity, input/context hashes, environment/reset/configuration and batch-slot receipts. Keep this separate from WP1's label matcher. Current precheck/runtime checks do not authenticate the exact opening inputs (`stage_gate.py:1730`; `difficulty_stats.py:644`).

**Acceptance:** detect one session copied under different run filenames, changed SQL paired with an old trace, absent opening prompt, ambiguous batch/reset information, and genuinely distinct bound runs. Preserve the existing duplicate-ID and duplicate-slot checks. Do not fabricate receipts during backfill or block unrelated authoring merely because the remote platform cannot provide historical metadata. Candidate evidence can be retained without promotion; unresolved runtime binding cannot support a new authenticated difficulty/release claim.

### WP6 — Plan migration and one controlled local canary

**Scope:** make certificate/version migration explicit, then exercise the changed paths on isolated copies. Any direct Python tool change currently changes `__gate_policy__`, potentially staling all saved certificates (`stage_gate.py:482`). New stage-specific evidence must join only the relevant `review_digest()` projection (`v3_artifact_checks.py:19`).

**Acceptance:** preview affected certificates and required revalidation; old PASS blocks remain unchanged historical evidence; no mass re-stamping or invented backfill occurs. A pasted new certificate must not stale itself. Rubric-only edits require affected regrading; SQL/source-rule edits invalidate relevant run applicability; OE edits update affected human-time/review dependencies. Existing source rereads, ACL/temporal evidence, exact spans, static reruns, fail-closed errors, upstream digests, binary validity and final release checks remain effective.

Only after targeted tests pass should a separately scoped local canary exercise the integrated path. Preserve the audit's original failed and successful artifacts as fixtures, not writable test workspaces. A local canary is not a Portal PASS. Paid runs, external reviews, messages, original task restoration and final submission remain outside this review authorization.

## Remaining uncertainty and completion

Reviewer D's canonical assignment remains unbound; original remote policy/clock/source preimages and some runtime input/reset envelopes remain unavailable. Some conclusions concern inspectable static gaps, not demonstrated end-to-end bypasses. These limitations are already stated in the audit and do not justify another full forensic loop before a small, well-tested improvement.

The prior independent review's five corrections remain applied: Reviewer B's FAIL score is 1; physical copies are counted separately; local evaluator policy is not presented as authenticated deployed Portal policy; Douglas's older missed defect is not called a newly introduced regression; mailbox citations stay within their source. No new count or stage-verdict correction was required.

**The audit is finished; the next useful work is scoped implementation with the acceptance checks above.** The only new deliverable from this pass is this review. No action was denied, no mutation outcome is uncertain, and no implementation was performed.
