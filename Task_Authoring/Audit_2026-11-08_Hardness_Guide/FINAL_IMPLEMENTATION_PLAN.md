# Final implementation plan: reduce preventable authoring iterations

Status: local implementation complete and independently reviewed; platform pilot and empirical measurements pending. Completion evidence appended below; original acceptance requirements preserved.
Date: 2026-11-08.
Workspace: `/Users/sumit/Source/OC/Task_Authoring`.

## Objective

Reduce avoidable authoring revisions by detecting weak difficulty design, invalid grading, stale evidence, wrong baseline associations and environment problems before expensive runs. Preserve fair tasks, correct failure-pattern counting and parallel task isolation.

Zero iterations is not a promised outcome. Six model runs are variable, and semantic design checks cannot guarantee a score. Measure prevented reruns alongside review overhead and false blocks.

This plan incorporates the independent oracle review. It authorizes no platform deployment, SQL execution, task rewriting or evaluator-policy change merely by existing as a document. Execute changes within the user's authorized scope.

## Mandatory multi-subagent execution instructions

**Use multiple subagents. Do not implement or review this plan alone.**

Use a coordinator plus at least three distinct specialist roles, scheduling them in waves when concurrency limits require it:

1. **Evidence and identity agent:** stage dependencies, evidence schemas, freshness, verifier-to-trajectory binding and evaluator-version provenance.
2. **Design and grading agent:** hardness review, difficulty-channel mapping, scope-safe outcome pairs, fairness and Mode B integration.
3. **Parallel-safety agent:** explicit task selection, shared-write inventory, concurrency control and isolation tests.
4. **Independent oracle agent:** tests the integrated changes against the acceptance cases below. This must be a separate agent from the authors of the changes it reviews.

The coordinator owns scope, interfaces, integration, migration and the final report. With four total active slots, run the coordinator and three specialists first; run the independent oracle in the next wave.

Before editing, assign non-overlapping file ownership. Where specialists need the same file, one designated owner integrates their changes. Do not concurrently edit central files such as `stage_gate.py` or `runtime_context.py`. Share interface proposals before implementation, not only after code is written.

The oracle must derive expected results from the supplied guides and applicable policy, not copy the implementation's outputs as expectations. It must distinguish a real regression, a pre-existing defect, an intentional policy adaptation and an unresolved assumption. Ask it to challenge false PASSes, false blocks, dependency cycles, scope expansion and parallel contamination.

Require an explicit oracle verdict before declaring completion. If implementation changes after that review, rerun the affected oracle checks. Report what was executed versus what was only inspected.

## Non-negotiable invariants

- Keep the existing failure-pattern algorithm: failed-criterion sets, distance zero/one merged transitively, at least two groups, largest group at most 50% of failing completed runs.
- Preserve exactly-six-slot, model-provenance, assigned difficulty-cap, error-handling and corrected-versus-raw scoring rules under the applicable policy.
- Do not inflate weights, add unstated outcomes, duplicate facts or manipulate criteria after observing results merely to improve a band.
- Genuine fairness or grader defects may be corrected with evidence; preserve raw results and their original identity.
- Do not weaken persona visibility, incorporation, source authority or findability to make a task harder.
- Keep advisory, uncalibrated success probabilities advisory. Low confidence is not itself a new mandatory rejection rule.
- Preserve stage ownership: Mode B diagnoses and proposes; scenario revision decides; injection implements universe changes; prompt/OE/rubric stages own their artifacts.
- Keep local construction separate from platform deployment and baseline execution. Never claim a local SQL check proves deployed state.
- Do not alter the user's active task folders to exercise tests. Use isolated fixtures.

## Phase 0 — Freeze interfaces and establish the regression baseline

Owners: coordinator and all specialists, with independent oracle input.

1. Read current repository instructions and inspect current code before relying on line numbers in the audit.
2. Inventory the stage dependency graph, existing certificates, task-context selection, shared writes, policy release identities and baseline associations.
3. Reuse existing evidence/gating structures where possible; do not introduce a competing source of truth.
4. Capture current behavior for known valid fixtures and relevant invalid fixtures. Reproduce the wrong-baseline association with isolated/read-only inputs before changing that logic; prior reproduction is evidence, not a substitute for verifying the current implementation.
5. Agree on evidence schemas, ownership and dependency edges before parallel edits.

Deliverables: dependency diagram, shared-write inventory, interface/schema proposal and a bounded regression suite.

Exit condition: proposed dependencies are acyclic, task selection is explicit where ambiguity exists, and all specialists agree on the interfaces they consume.

## Phase 1 — Stage-specific evidence and reliable identity

Owner: evidence and identity agent.

### Evidence architecture

Create versioned, task-local, revision-bound attestations for each stage. Generate the overall readiness summary from those attestations. **The summary must not become a mutable input required by upstream stages.**

Each attestation should identify:

- Schema version, task identity, revision and stage.
- Relevant input hashes and upstream evidence identities.
- Tool/check version and applicable policy/evaluator identity.
- Check outcomes, evidence references, reviewer and dispositions.
- Evidence availability: required-now, deferred-to-a-named-stage, not-applicable with reason, or unresolved-required.

Use immutable revision records or explicit supersession; preserve history. Persist records atomically. Exclude generated certificate text from content hashing according to existing digest conventions so saving a result does not invalidate itself.

Invalidate only dependent evidence. A baseline update must not invalidate unchanged scenario or injection checks. A SQL change must invalidate the evidence that actually depends on it. A deferred item must become required at its designated stage.

### Verifier-to-trajectory binding

Bind each verifier result to the actual trajectory export using export hash, reliable run/session identifier where available, revision/bundle evidence and discriminating observed writes or outputs.

Filename `Run #N` correspondence and task-context hashes alone are insufficient. Renaming files must not silently reassign grades. Missing identifying evidence produces UNBOUND or REVIEW_REQUIRED, never an inferred match. Permit an evidenced review receipt for export formats without reliable machine identifiers.

Do not demand that every ID mentioned by the verifier appear verbatim in the trajectory: verifiers can observe end-state data not repeated in the export.

### Evaluator compatibility

Record local evaluator release and the release reported by platform evidence. Detect substantive incompatibilities and route them for review. Different hashes do not establish which release is authoritative or newer. Do not edit hash-bound evaluator files to imitate report wording.

Exit condition: identity and freshness tests pass without adding upstream cycles or rejecting valid early-stage work.

## Phase 2 — Difficulty design and grading readiness

Owner: design and grading agent.

### Design evidence

For each selected difficulty mechanism, record:

| Field | Required meaning |
|---|---|
| Initial plausible answer | Concrete source that makes the initial answer believable |
| Deciding evidence | Correction, exception, alias mapping or missing prerequisite |
| Authority and chronology | Why that evidence governs |
| Fair discovery path | How the persona can reach and read it |
| Changed outcome | Actual number, status, inclusion or write affected |
| Independent operation | Which other mechanisms remain solvable if this one is missed |
| Grading coverage | Existing prompt-required outcomes affected, with work-kind weights |

Reuse the manifest, solver and gradable surface; avoid manually duplicating the same facts into several documents.

Preserve the existing requirement for at least three independent loss channels and four for Hard, subject to applicable policy. Do not count routine volume, decoys or multiple labels for one gateway as distinct effective channels.

### Scope-safe outcome pairing

For selected diversity mechanisms, evaluate whether two legitimate, atomic, independently passable outcomes expose the mistake. Both must already follow from the intended business task.

Do not add an explanation the prompt did not request or repeat the same fact in two destinations to satisfy a count. If suitable outcomes do not exist, revise the scenario deliberately or choose another mechanism. Design-time outcomes can be provisional slots; do not require final rubric text before its stage.

Complete required action/write coverage before forecasting difficulty. Distinguish allowed sampling from explicitly requested outcomes according to the applicable rubric policy. Compare the final builder export with the reviewed rubric before verifier execution.

### Stage-aware hardness dispositions

Make the presence and freshness of an applicable hardness review enforceable. Do not blindly run the advisory helper in strict mode everywhere.

- At design: absent SQL or not-yet-materialized containers can be deferred.
- After injection: required load-bearing evidence must resolve.
- At prompt review: check semantic leakage as well as literal resolver overlap.
- Before baseline: confirm actual outcomes and applicable evidence are covered.

A warning needs a repair, an evidence-backed accepted disposition, or a reasoned not-applicable status. Generic “reviewed” text cannot clear a finding. Hard fairness/visibility defects cannot be waived as ordinary advisory warnings.

Semantic review must examine what natural search/list calls return, not only container equality. A correction in another thread may still appear in the same channel search. Declaring `done_gap` does not prove a meaningful missing prerequisite.

Exit condition: valid tasks are not forced to contain every trap family; real unresolved dependencies and grading defects block at the correct stage.

## Phase 3 — Local readiness versus platform baseline readiness

Owners: evidence agent and coordinator.

Local build readiness must be obtainable without network access, executing SQL or deploying an environment.

A separate platform handoff records:

- Selected base universe identity.
- Evidence of fresh deployment from base rather than an accumulated old environment.
- Exact applied SQL identity, or an explicit no-injection state where permitted.
- Application evidence and disclosed intervening manual changes.
- Agent-tool readability of decisive records.
- Environment/run identity associated with the baseline.

Use actual platform evidence or an explicitly reviewed receipt supported by evidence. Do not invent a required vendor receipt format the platform cannot provide. Unknown state remains unknown. Reuse prior readability evidence only when the exact environment state, relevant artifacts and tool assumptions remain valid.

Rebuild/reapply requirements concern the final platform environment; they must not create a local-authoring deadlock. No-injection must not require fake SQL. Do not redeploy automatically without applicable user authorization.

Exit condition: local construction can finish while platform readiness is pending, and no final run is certified against an unverified or mismatched environment.

## Phase 4 — Parallel authoring safety

Owner: parallel-safety agent.

1. Inventory every shared write, including the hardness ledger, evaluation input store, generated reports and caches. Do not assume task-local readiness solves existing shared-state risks.
2. Require unambiguous task identity for production commands in multi-task contexts. Preserve supported single-task and archival diagnostic flows through explicit compatibility rules.
3. Reject disagreement between selected task and supplied artifact paths; do not silently read the default folder.
4. Serialize shared ledger read/check/append as one transaction, or use per-task queues with one serialized merger. Merely locking the final append is insufficient when conflict decisions used stale in-memory state.
5. Preserve idempotence, conflict detection, correction/supersession semantics and read-only consumers.
6. Keep outputs and evidence task-local; use context-aware cache keys and safe output boundaries.

Exit condition: four concurrent isolated tasks preserve outputs and shared records without cross-task reads, lost updates or duplicate conflicting identities.

## Phase 5 — Mode B and repair routing

Owner: design and grading agent, integrated by the coordinator.

Add required structured outputs, generated from bound evidence where possible:

1. Weight-5 criterion matrix across six runs, including raw results and separately justified corrections.
2. Exact failure sets, transitive groups and largest-group share from the existing calculator.
3. Mechanism-level causal diagnosis supported by trajectory events.
4. Repair proposal: original evidence placement, proposed placement/reasoning change, affected outcomes, scope/volume difference, preserved fair discovery path and required reruns.

A single pre-check is provisional; never label it 6/6 or infer a stable failure rate from it.

Route repairs according to the diagnosis:

| Observation | Required response |
|---|---|
| Heavy rows pass in every run | Repair meaningful evidence/reasoning; do not add routine volume |
| One pattern dominates | Examine shared gateways and genuinely independent decisions |
| Differences collapse through one-criterion links | Inspect complete outcome coverage and transitive grouping; do not cosmetically split criteria |
| Every run fails a row | Check fairness, tool readability and grader accuracy first |
| Correction appears naturally on first read | Reassess placement without removing fair discovery links |
| Local and platform reviewers disagree | Inspect policy/release and evidence differences before rewriting the task |

“Do not add volume” blocks using volume alone as a difficulty repair. It must not forbid legitimate missing-data or fairness repairs. Classify the reason for any scope change explicitly.

Exit condition: each proposed repair has a causal reason, an owner and a bounded rerun scope. No stage rewrites another stage's artifact implicitly.

## Independent oracle regression acceptance matrix

The independent oracle must inspect expected outcomes and execute applicable cases against isolated fixtures. Do not create tests that merely assert implementation-specific strings.

| Area | Must pass |
|---|---|
| Dependency graph | No cycle; baseline updates do not invalidate unchanged upstream checks; saving certificate text does not self-invalidate |
| Stage availability | Scenario succeeds without final SQL/prompt/rubric/platform receipt; deferred evidence becomes required later |
| Fairness | Required inaccessible evidence blocks; a generic warning waiver cannot bypass it; fair alternative outcomes remain accepted |
| Forecasts | Uncalibrated probabilities alone do not cause a new hard failure |
| Binding | Correct Vincent-style batch binds; superseded batch rejects or remains UNBOUND; filename shuffle cannot remap; changed export stales receipt |
| Evaluator identity | Release mismatch is surfaced; historical verdicts retain their original policy; no authority inferred solely from hash differences |
| Rubric scope | Unrequested explanation and duplicated facts cannot satisfy paired outcomes; legitimate independently passable outcomes can |
| Coverage | Required writes remain covered; pairing does not alter work-kind weights or bypass sampling/atomicity rules |
| Pattern logic | Both screenshot examples; zero/one-failure cases; three/five failure limits; exact 50%; transitive bridge |
| Corrected scoring | Raw evidence preserved; justified corrections affect the intended view; errors are not silently scored zero |
| Environment | Local completion without deployment; missing platform evidence blocks only the relevant handoff; explicit no-injection works; cross-task receipt reuse rejects |
| Concurrency | Four distinct appends survive; duplicate identity is idempotent; conflicting identity is rejected; locking covers validation and append |
| Task isolation | Task B cannot consume task A/default artifacts silently; mixed context/path inputs reject; valid explicit single-task flow works |
| Migration | Historical tasks remain readable; legacy evidence is marked historical/unverified rather than silently certified; current tasks are not rewritten for migration |
| Efficiency | Repeated unchanged checks reuse valid evidence; changes rerun only dependent work; no repeated platform run demanded without a material reason |

The seven earlier calculator probes are useful fixtures, not a complete regression suite. The independent oracle review of the plan is not an implementation test pass.

## Rollout and review sequence

1. Implement and validate foundations in isolated fixtures: stage attestations, task identity and verifier binding.
2. Integrate design review and Mode B without changing the pattern algorithm.
3. Add platform handoff and concurrency controls with explicit phase boundaries.
4. Have the independent oracle review the integrated result; fix blockers and rerun affected checks.
5. Pilot on one authorized task; retain a clear rollback path for new controls.
6. Expand to four concurrent tasks only after isolation and shared-write tests pass.
7. Keep existing policy checks active throughout. Do not silently grandfather unsupported evidence into PASS or demand costly reruns of historical archives.

## Completion criteria and measurements

Implementation is complete only when:

- All acceptance cases applicable to the implemented scope pass, with unresolved cases disclosed.
- The independent oracle has no unresolved blocking findings.
- Documentation and command routing match actual behavior.
- A valid task can traverse the workflow without circular dependencies or premature platform requirements.
- No active user task, base export or evaluator policy was modified merely for testing.
- The coordinator reports files changed, tests executed, oracle findings resolved and remaining limitations.

Track baseline reruns, late fairness/coverage defects, wrong-evidence incidents, environment-related failures, false blocks, review time and total authoring time. Compare similar tasks and difficulty modes; do not attribute all improvement to the new controls without evidence.

## Supporting audit artifacts

- [Combined findings](Combined_Findings.md)
- [Hardness guide](Hardness_Guide_From_Screenshots.md)
- [Failure-pattern guide](Failure_Pattern_Guide_From_Screenshots.md)
- [Initial pipeline coverage report](Pipeline_Coverage_Report.md)
- [Executed pattern probes](Failure_Pattern_Verification.json)

Reinspect the current implementation before editing. Prior audit references and temporary reproductions may become stale; preserve a maintained fixture for any confirmed defect during implementation.

## Implementation completion evidence — 2026-11-08

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), saved universe selection.
This is infrastructure implementation and isolated-fixture validation, not a task
evaluation or claim about deployed platform state.

The coordinator and three distinct specialists implemented phases 0–5 in waves;
a fourth, independent reviewer authored no production changes. File ownership
was separated, with the coordinator integrating `stage_gate.py`. The original
acceptance matrix above was not relaxed or rewritten.

| Phase | Completion evidence |
|---|---|
| 0: interfaces and baseline | Complete plan/audit reads; original suites 102 and 128 tests passed (one skipped); filename-only wrong-export defect reproduced before repair. Dependency diagram and schemas in `../Guide/Readiness_And_Evidence.md`; shared-write inventory in `Parallel_Safety_Implementation.md`. |
| 1: identity and freshness | Immutable atomic stage records, upstream identities, stage-specific hashes, deferred availability, evaluator compatibility review; strict verifier/export binding and saved-matrix revalidation. New evidence tests plus independent binding/staleness probes pass. |
| 2: design and grading | Stage-specific reviewed source/retrieval evidence, unwaivable access defects, independent outcome pairs, work-kind weights and coverage; prompt semantic review; builder equality before baseline. Valid early design accepted without later artifacts. |
| 3: separate readiness | Local readiness completes without platform evidence. Platform handoff consumes reviewed fresh-base/application/readability proof; post-baseline checks require actual bound run identities. No platform action executed. |
| 4: isolation/concurrency | Explicit task/path selection, task-salted caches, ledger validation+commit lock and atomic publication, entity publication lock; four-process distinct/idempotent/conflicting identity tests pass. |
| 5: Mode B | Bound raw/corrected heavy-row matrix, original transitive grouping, actual-event causal references, observed all-fail safeguards and scope/owner/rerun repair fields. Precheck remains provisional without final rubric/verifier. |

Final executed regression results:

- `python3 -B -m unittest discover -s Task_Authoring/tests`: 137 passed.
- `python3 -B -m unittest discover -s Task_Authoring/tools -p 'test_*.py'`: 169 tests, OK, one live-task check skipped.
- `stage_gate.py --self-test`: 138 cases passed.
- `selftest_sandbox.py --self-test`: 10 cases passed.
- `difficulty_stats.py --self-test`, `trajectory_ledger.py --self-test`, `hardness_ledger.py --self-test`: passed.
- Independent oracle: 18 tests passed; separately reran 9 integration tests, all passed. Verdict: **PASS for implemented local scope; no unresolved blockers**.

Two full-stage forecast controls initially failed against both the original and
changed code because they depended on a missing external ledger record. The
sandbox now seeds a deterministic synthetic forecast through the actual ledger
API; the full 138-case suite passes without changing its acceptance logic.

See [Implementation report](Implementation_Report.md),
[independent oracle findings](Independent_Oracle_Implementation_Review.md), and
[operating guide](../Guide/Readiness_And_Evidence.md) for file lists, exact scope,
resolved findings, schemas and migration.

Remaining plan work is explicitly external or prospective: an authorized live
task pilot, actual deployment/readability/baseline evidence, and empirical tracking
of reruns, late defects, false blocks and time. No active task, completed-task
evidence, universe export or evaluator policy was modified. The local positive
traversal uses synthetic stage records; it does not substitute for a complete V3
task or platform pilot. No-injection receipts work where permitted; existing
mandatory-injection authoring policy remains unchanged. Direct evaluator-store
concurrency and full KB maintenance remain serialized external operations.

## Follow-up verification — user request “verify everything”

The fresh review found missed production interactions despite the initial passing
tests. They were reproduced and fixed without relaxing the acceptance matrix:
precheck stage projection, gate execution provenance and artifact completeness,
Mode B/reference/evaluator-proof freshness, final paired criterion/weight
coverage, matrix-to-current-source validation, typed repair scope/reruns, and
forensic CLI input/output isolation (explicit, default and symlink paths).

Current evidence: [Verification_Report.md](Verification_Report.md) and
[Verification_Oracle_Report.md](Verification_Oracle_Report.md). Final local
discovery results are 154 integration tests passed and 184 tool tests OK with one
live-task fixture skipped. The complete stage sandbox passes 138 cases; the
independent oracle passes 25 cases. Numerical scoring/grouping functions are
AST-identical to original HEAD. An additional pre-existing oracle-kit fixture
failure was reproduced against original code and fixed with a disposable
assignment; its real base-read assertions now pass without a skip.

This follow-up supersedes the initial verification confidence, not the original
requirements. External platform proof, an authorized live-task pilot and empirical
measurements remain pending. No active task, completed evidence, base export or
evaluator policy was modified for this verification.
