# Follow-up verification

Date: 2026-11-08.
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), saved universe selection.
Scope: infrastructure code, supported local commands and isolated regression fixtures.

The user's follow-up “verify everything” prompted a fresh multi-agent review.
The previous passing suites did not cover several production interactions. This
review reproduced those defects, corrected them and added regressions; the
earlier approval must be read together with this follow-up.

## Additional findings and repairs

| Finding | Repair and verification |
|---|---|
| Precheck hardening required a future final rubric | Separate precheck bundle projection excludes future OE/rubric; production Mode B review passes before those files exist and remains current when they are added. |
| Generated gate text changed bundle identity | Text uses the existing normalized digest; certificate-only edits leave bundle identity stable. |
| Generic/imported reviews could certify incomplete gates | Readiness requires explicit full-gate producer provenance, required execution checks and actual required artifacts. The public generic-import CLI cannot claim producer metadata. |
| Attestation output boundary and lock/index handling were incomplete | Enforce authoring output boundaries, reject symlink locks and malformed/path-traversing index IDs. |
| Mode B request/support files could change without staling evidence | Bind request, matrix, verifier/receipt and trajectory files; rerun bounded Mode B evidence checks when assessing current records. |
| Reference manifest did not bind attachment bytes/routing | Reference-file stage includes directory content; directory hashes include relative paths. |
| Compatibility review could cite nonexistent proof | Require substantive reason and current task-local hash-checked compatibility evidence. |
| Two distinct surface outcomes could collapse into one final criterion | Require independently covering final criteria for each selected pair. |
| Final rubric could inflate a lookup slot's weight | Check final mapped work-kind weights rather than only the design surface weights. |
| Mode B matrix could alter weights, mode or spec despite matching bundle | Reconstruct baseline rows from current reviewed rubric/export sources and bind assignment context. Prechecks retain their provisional path. |
| Repair proposals accepted unknown outcomes or unbounded rerun prose | Require known outcome IDs, explicit change kind, measurable/described scope differences and a bounded list of valid rerun stages; fairness/missing-data repairs remain allowed. |
| Forensic CLI paths crossed task boundaries | Validate parsed `LABEL=PATH`, explicit/default-discovered inputs, symlinks and output boundaries across nine forensic CLIs. Preserve explicit ownerless archival diagnostics. |

Affected production files beyond the initial implementation include
`oracle_kit.py`, `gradable_surface.py`, `trap_liveness.py`,
`difficulty_mutation.py`, `hardness_forecast.py`, `preflight_report.py`,
`node_verdicts.py`, and `surface_grader.py`, plus the existing evidence/readiness,
trajectory, design and Mode B modules. New adversarial suites are
`test_verify_identity.py`, `test_verify_design.py`, and
`tests/test_verify_isolation.py`. Integration/oracle tests and the operating guide
were extended. No active task or evaluator policy was changed.

## Verification method and scope

Three specialists independently audited identity/freshness, design/grading and
isolation before implementing assigned fixes. The separate oracle reviewed the
fixes without authoring production code and added its own production-path probes.
See `Verification_Oracle_Report.md` for its detailed findings and verdict.

An AST comparison against original HEAD confirmed `difficulty_stats.py` functions
`group_patterns`, `_gates` and `compute` are unchanged. Thus the transitive
failure-pattern algorithm and numerical scoring gates were not rewritten.

The local positive traversal models completed stage records and separately checks
their prerequisites; it is not proof that an entire new real V3 task passes every
semantic review. The full stage-gate calibration suite exercises its existing
complete legacy fixtures. No deployment, SQL execution, paid run or active-task
pilot occurred. Real platform evidence and empirical rerun/time measurements
remain pending, as in the original plan.

## Final executed results

| Check | Result |
|---|---|
| `python3 -B -m unittest discover -s Task_Authoring/tests` | 154 tests passed |
| `python3 -B -m unittest discover -s Task_Authoring/tools -p 'test_*.py'` | 184 tests, OK; one unavailable live-task/revision fixture skipped |
| `stage_gate.py --self-test` | 138 cases passed in isolated sandbox |
| `selftest_sandbox.py --self-test` | 10 cases passed |
| Independent oracle suite | 25 tests passed |
| Additional verification suites | identity 6, design 9, isolation 6 (including eight CLI subcases), integration 13 passed |
| Affected tool self-tests | trajectory_ledger, gradable_surface, trap_liveness, difficulty_mutation, preflight_report, node_verdicts, hardness_forecast, surface_grader and oracle_kit passed |
| AST comparison against original HEAD | group_patterns, _gates and compute unchanged |
| `git diff --check` | Passed |

The discovery totals include the focused suites; these are not additive counts
of independent checks. The independent oracle authored no production changes.

The additional standalone `oracle_kit.py --self-test` initially failed because
its hardcoded external season-pass fixture lacked an assignment. Isolated
original-HEAD versions of oracle_kit, runtime_context, task_context and hg
reproduced the identical failure. Its self-test now creates an explicit
disposable V3 assignment; real guarded `hg.py` reads still check correct value
PASS, wrong value FAIL and absent record FAIL. No assertion was relaxed and no
live task was repaired to make the test pass.

All identified local blockers were corrected and affected checks rerun. Actual
platform deployment/baseline evidence, a complete live V3 pilot and empirical
measurements remain unverified; they are not substituted with these test results.
