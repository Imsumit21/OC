# Why the task-authoring artifacts keep returning Portal failures

Audit requested on 2026-10-28. This is a forensic report, with recommendations only. No task artifact, create skill, validator, source export or original report was repaired, overwritten or deleted. No Portal run or outreach was performed.

## The task count

**Three distinct sent task IDs have a verified returned external FAIL: Reviewer A, Reviewer B and Reviewer C.** Reviewer D also returned a genuine FAIL, but it grades a different scenario and has not been bound to the task originally sent. Reviewer E has a verified send and no located returned report. Consequently, four FAIL-returning reviewers do not establish four failed sent tasks.

| Canonical sent task | CB | First qualifying returned failure | Included |
|---|---|---|---|
| `TASK_A` | Reviewer A | Prompt FAIL 2 / COMPLETE: unresolved closed-item and installment write sets | Yes |
| `TASK_B` | Reviewer B | Prompt FAIL 2 / COMPLETE: incorporated source ambiguity and coherence | Yes |
| `TASK_C` | Reviewer C | Injection FAIL / COMPLETE: duplicate identity for an existing Transcend partner | Yes |
| `TASK_D` | Reviewer D | Hardness FAIL 1 / COMPLETE on returned screenshot-refresh scenario; original send was PlayableX | Attribution unresolved |
| `TASK_E` | Reviewer E | No returned report found; active loop was cancelled | No established failure |

The parent mailbox audit inspected the qualifying reports in full and verified sends/returns. Exact Gmail links, dates, report filenames and historical-search limits are in [MAILBOX_PROVENANCE.md](evidence/MAILBOX_PROVENANCE.md). An independent filesystem auditor reconciled their report bytes in [INDEPENDENT_COUNT.md](expert_reviews/INDEPENDENT_COUNT.md). Older October 16/17 deliveries were also searched; their existence prevents calling five an all-time sent-task total, but no additional attributable failed return was located. The count is three confirmed tasks across the located histories, with the coverage limits stated explicitly.

## What was reviewed

Six expert reviewers separately examined injection/hardness, prompt, OE, rubrics, pipeline/provenance and independent inventory/adversarial verification. They read the actual create wrappers, playbooks, execution contract, validators, stage gates, preserved reports and relevant artifact/source versions. The mailbox audit was performed separately by the parent thread. Filenames and past assistant summaries were not accepted as proof that a skill ran or that an artifact passed Portal.

The full local corpus contains **84 unique imported report documents across eight report-bearing task groups**: 91 extracted-file occurrences after including exact preservation copies. Thirteen ZIP archives were inspected; their 25 report members add no distinct report bytes. The wider corpus includes Julia's current folder, skipped Oliver, archived Arthur and completed Douglas, even where contributor delivery is not established. These groups are included in causal analysis but excluded from the strict sent-task count.

| Stage | PASS | NON-FAIL | FAIL | Total unique report documents |
|---|---:|---:|---:|---:|
| Injection | 21 | 0 | 4 | 25 |
| Prompt | 6 | 4 | 13 | 23 |
| Hardness | 0 | 6 | 5 | 11 |
| Oracle Events | 4 | 3 | 0 | 7 |
| Rubrics | 3 | 0 | 15 | 18 |
| **Total** | **34** | **13** | **37** | **84** |

These are historical report-document counts, not independent trials, failed-task counts or an estimated failure rate. NON-FAIL remains NON-FAIL. One Douglas OE NON-FAIL is PARTIAL and unscored; one Reviewer A rubric FAIL is PARTIAL with a proved defect. The three initial qualifying CB FAIL returns are COMPLETE. Byte deduplication, final verdict lines, statuses and full input hash mentions are in [report_manifest.json](evidence/report_manifest.json). The [complete verdict history](TASK_VERDICT_HISTORY.md) records every unique report in preserved order.

## The main explanation

**There is no single failure of every create skill. The repeated loops combine a narrower local completion contract, missed semantic defects, hardening regressions, divergent review rules and clocks, and imperfect repair/provenance handling.** Some fixes clearly worked. OE has no preserved external FAIL, and several prompt/rubric chains reached externally recorded PASS. The remaining problems require different remedies; adding more checklist prose alone would not address them.

### 1. Local CLEAN was a preparation milestone

The batch explicitly ended after scenario, injection, prompt-writing and prompt-check local gates. `/injection` and `/prompt` were omitted from that batch by recorded user choice, and human time, precheck, OE and rubrics were out of scope. `Task_Authoring/batch/TASK_RUNBOOK.md:5`, `:49`, `:81`, `:111`; `batch/ORCH_STATE.md:83`; `batch/verify_task.py:8`.

That scope change was authorized. The faulty inference is treating a local CLEAN package as if it carried full external quality or release approval. The package checker reruns four gates and copies the pair; it does not run Portal semantics, observed hardness or the full release gate. A Portal FAIL after that handoff is not evidence that a completed Portal review was bypassed or falsified.

### 2. Several gates certify evidence structure more strongly than evidence meaning

The code genuinely reruns SQL/static checks and binds upstream files and gate policy. Those safeguards are useful and must be retained. However, counter-reading rows, source-pointer-shaped cells and dimension-table presence do not prove that every alternative has been resolved or every title accepts the right output. `Task_Authoring/tools/stage_gate.py:609`, `:618`, `:1930`, `:2360`.

Concrete misses explain the consequence: Reviewer C's initial injection lint reported zero flags while manual review found a duplicate real-world identity; Reviewer A's and Reviewer B's prompt failures concerned two plausible write/classification outcomes from incorporated records. Those are semantic claims, not SQL syntax. The [injection](INJECTION.md) and [prompt](PROMPT.md) reports trace the exact defects and repairs. A stronger gate needs checkable claim/alternative records and relevant independent judgments, rather than treating a populated review table as semantic proof.

### 3. Hardness repairs altered the meaning being evaluated

Reviewer B's injection reports repeatedly PASS, while hardness FAILs led to new production-state/configuration evidence. Prompt ambiguity then reopened even though the prompt wording was effectively unchanged. Douglas goes NON-FAIL→FAIL→PASS when a deeper review discovers an existing lifecycle defect and the sources are then repaired; the report explicitly says the earlier review missed it. Reviewer A initially fixes ambiguity by adding prompt casework, then receives a contrived-prompt FAIL, and later resolves the rules in source records.

The causal unit is the prompt **plus everything it validly incorporates**. A source edit can change the required answer without changing the prompt hash. Structural volume and declared necessary-call budgets also do not prove observed difficulty: the Portal hardness reports include model success on large authored tasks. See [INJECTION.md](INJECTION.md) and [PROMPT.md](PROMPT.md) for the source-level chronology and contrary evidence.

### 4. Rubric policy and authoring predictions are out of sync

The authoring contract/playbook still describe percentage bands under which a small number of Major issues can avoid FAIL. The current evaluator explicitly fails **any Major or Moderate issue**. Compare `Task_Authoring/setup/GEN_EXECUTION.md:159`, `Task_Authoring/playbooks/09_Rubric_Writing.md:205`, and `Evals/3_Rubrics_Eval.md:36`. This is a direct policy mismatch, not a mysterious percentage calculation.

The reports also contain real title-level defects: non-atomic results, title acceptance depending on justification/evidence, unauthorized or uncovered results, negative-only criteria, inconsistent weights and aliases with unstable meaning. Fixing evidence alone cannot repair a title-only acceptance rule. Reviewer B's Brian-ID/weight defect recurred after only the supporting evidence changed. The [rubric report](RUBRICS.md) distinguishes those author-side defects from evaluator advice errors and explains why two heavily revised rows kept introducing new edge cases.

### 5. Some review advice was itself unstable

Reviewer B's latest preserved rubric report explicitly acknowledges that earlier open-alias guidance was the evaluator's error. Its fix list says that previous points closed but new problems arose. This is evidence of imperfect repair advice and semantics changing under reformulation; it does not prove every report is unreliable or that every unchanged artifact was arbitrarily regraded. Reviewer A's PASS→FAIL involves changed rubric bytes, so it must not be described as same-input randomness. See report `(11)` at `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_30_rubric_alias_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (11).md:134` and [RUBRICS.md](RUBRICS.md).

The repair process needs frozen valid/invalid output examples and invariant tests across revisions. Copying a suggested phrase is weaker than demonstrating that it preserves all previously accepted correct answers and rejects all established wrong answers.

### 6. Cross-system clock and artifact identity remain unresolved in places

Local V3 authoring resolves the October freeze to 00:00 UTC; the preserved Portal reports use 00:00 PT, 07:00 UTC. This directly explains minor OE disagreements and why Reviewer B's externally passing OE copy was held separately. It is a genuine authority/configuration mismatch, but the reports do not show that it caused every observed failure. Official/local authorship and hardness policies also deliberately differ; no preserved detector rejection establishes authorship as the cause. [OE.md](OE.md) and [PIPELINE_ROOT_CAUSES.md](PIPELINE_ROOT_CAUSES.md) distinguish proven consequences from possible risks.

Current artifact state must also be checked separately from a past receipt. This audit observes that Reviewer B's canonical `09_Rubrics.json` is currently **absent**, although iteration31's historical receipt records a successful copy of 45 criteria at hash `34d1d4f1…`. The candidate remains preserved. The audit does not establish who removed or moved the canonical file or when; it did not restore it because this request is audit-only. The latest genuine external rubric FAIL grades the prior `ea7292a8…` version, while the later local PASS grades `34d1d4f1…`. Neither transfers automatically to a missing canonical file. Evidence: [canonical_slot_snapshot.json](evidence/canonical_slot_snapshot.json), iteration31 `copy_verification.json:2`, and [RUBRICS.md](RUBRICS.md).

## Current interpretation by task

These are the latest **preserved external** labels for each stage, not a certification of every current byte. Full bindings and local holds are in the stage reports.

| Task group | Injection | Prompt | Hardness | OE | Rubrics | Practical interpretation |
|---|---|---|---|---|---|---|
| Reviewer A | PASS | NON-FAIL 3 | NON-FAIL 3 | PASS 5 | PASS 5 | Several repairs succeeded; local rubric preparation/release evidence is a separate question. |
| Reviewer B | PASS | PASS 5 | NON-FAIL 3 | PASS 5 on separate copy | FAIL 1 | Latest local rubric candidate is later than external FAIL; clock/context and canonical packaging remain separate. |
| Reviewer C | PASS | PASS 5 | FAIL 2 | No report | No report | Current SQL was redesigned after quality PASS; historical PASS cannot certify that new pair. |
| Reviewer D | No report | No report | FAIL 1 on changed scenario | No report | No report | Report attribution and raw trajectory missing; original sent scenario not graded by this evidence. |
| Reviewer E | No report | No report | No report | No report | No report | No established returned failure; cancelled loop remains cancelled. |
| Julia/default | Historical FAIL | No original report | No original report | No report | No report | Current SQL differs and local repair exists; no fresh external PASS located. |
| Oliver/skipped | Historical FAIL after earlier PASS | FAIL | NON-FAIL 4 | PASS 5 | FAIL | Real repeated defects, mixed with older/local sandbox histories; no CB-delivery mapping established. |
| Arthur/archived n | PASS | NON-FAIL 3 | NON-FAIL 4 | No original report | No original report | Prompt fork repaired; locally narrated later checks are not original external verdicts. |
| Douglas/completed | PASS | PASS 5 | NON-FAIL 4 | PASS 5 | PASS 5 | Successful bounded repairs; later source revisions still require exact context checks. |

## Deliverables and next decisions

- [INJECTION.md](INJECTION.md): all injection and hardness histories; identity/prose chronology, SQL consistency, collapse of planned difficulty, repairs and regressions.
- [PROMPT.md](PROMPT.md): incorporated-source forks, prompt casework, unchanged-text regressions, realism/role evidence and exact pair bindings.
- [OE.md](OE.md): all seven original OE reports, clock/source/provenance defects, successful repairs, route/tool argument checks and local-only histories.
- [RUBRICS.md](RUBRICS.md): all 18 original rubric reports, row-level repeated failures, policy divergence, checked-fix contradictions and version bindings.
- [PIPELINE_ROOT_CAUSES.md](PIPELINE_ROOT_CAUSES.md): create invocation evidence, real gate protections, semantic gaps, certificate staleness, run provenance and release boundaries.
- [RECOMMENDATIONS.md](RECOMMENDATIONS.md): prioritized changes and concrete regression cases; none implemented.
- [TASK_VERDICT_HISTORY.md](TASK_VERDICT_HISTORY.md), [task_matrix.json](evidence/task_matrix.json), [report_manifest.json](evidence/report_manifest.json), [artifact_version_manifest.json](evidence/artifact_version_manifest.json): chronology, count decisions, source hashes and 446 named artifact versions.
- [source_rule_manifest.json](evidence/source_rule_manifest.json): 130 current rule/tool/provenance fingerprints; a current snapshot rather than a reconstructed complete historical environment.
- [INDEPENDENT_COUNT.md](expert_reviews/INDEPENDENT_COUNT.md) and [ADVERSARIAL_REVIEW.md](expert_reviews/ADVERSARIAL_REVIEW.md): independent count and final challenge review.

The remaining blockers concern evidence and authority, not permission to perform this audit: Reviewer D's task binding, unavailable historical source/review preimages, incomplete run envelopes, cross-system clock configuration and missing original reports behind some retrospective claims. No blocked outreach was retried. No fix or new evaluation was required to complete the requested reports.
