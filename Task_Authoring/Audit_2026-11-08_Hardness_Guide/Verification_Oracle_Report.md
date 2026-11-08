# Follow-up independent verification oracle

Clock: infrastructure audit; no task evaluation clock applies. Saved task intake remains Oct 1, 2025 (synth-cut). No active task, completed-task evidence, universe export or evaluator policy was changed by this reviewer.

Final verdict: **PASS for the tested local implementation scope, with no unresolved blocking findings.** This supersedes the earlier oracle's coverage claim where the follow-up exposed missed production interactions. It is not a certification of an active task, deployment, real six-run baseline, or complete new V3 end-to-end authoring workflow.

Reviewer: `/root/oracle`, independent of all production authors. I changed only `tests/test_independent_readiness_oracle.py` and this report in this follow-up.

## Why another review was necessary

The prior oracle tested important components, but its positive traversal used synthetic stage records and did not adequately challenge the production import path, future-stage identity dependencies, final coverage mapping or separate Mode B matrix. Those omissions allowed false PASS cases to remain. The user's request to verify everything prompted fresh specialist findings and this second independent review. The earlier report remains a historical record; its PASS must not be read as evidence those untested interactions were correct.

Expected outcomes still come from the reviewed plan, screenshot guides and applicable authoring policy: no premature final-rubric dependency; no generic review masquerading as executed gates; final outcomes remain independently graded; raw and corrected matrices retain their actual identities and work weights; changed referenced evidence invalidates dependent readiness; explicit task identity confines reads and writes.

## Follow-up findings and verified resolutions

| Area | Finding / resolution | Independent verification |
|---|---|---|
| Pre-check identity | A pre-check's bundle must not depend on later OE/rubric creation. Normalized pasted gate text must not change submitted input identity. Actual reference bytes must matter. | Independently authored test passes with later OE/rubric addition and pasted gate text, then detects reference addition/content change. Production `mode_b_review` no-future-rubric integration case also executed. |
| Production attestation | Generic imported records were insufficiently distinguished from full executed gate records. Follow-up added producer, mandatory execution checks, required artifact existence, and executed-gate guard. I additionally found that the CLI still accepted caller-supplied producer metadata; the coordinator reserved that field. | Public `stage_evidence.py --record` with forged full-gate producer now rejects. Integration checks reject unexecuted contexts and missing artifacts. Direct Python calls used in fixtures remain trusted internal APIs, not cryptographic tamper protection. |
| Referenced evidence freshness | Readiness must bind actual Mode B requests, their sources/proofs and reference-file paths/content. | Integration proof mutation rejects; source inspection verifies Mode B request/source hashes plus replay. Reference-routing digest test independently executed. Existing independent baseline-addition/upstream-stability test still passes. |
| Evaluator compatibility | A generic rationale or stale proof cannot turn a release mismatch into compatible. | Independently authored positive substantive comparison, generic rationale rejection and changed proof rejection all pass. No authority/chronology inferred merely from differing hashes. |
| Final paired outcomes | Two provisional slots do not suffice when both map to one final criterion. | Independently authored valid separate final mapping passes; collapsing the pair onto one final row rejects. Specialist suite's exclusive coverage and final lookup weight tests also independently executed. |
| Production Mode B | A correct bundle does not authorize an independently edited matrix's weights/spec/mode. | Independently authored production request builds from actual verifier/exports/current rubric, passes, then rejects matrix weight and V2 downgrade. Specialist positive correction/mode mismatch tests independently executed. |
| Repair proposals | Unknown outcomes, unmeasured scope changes, missing change kind and an unbounded string such as `none` cannot satisfy a concrete repair. | Independently authored and executed valid concrete repair, unknown outcome, missing measured difference, unbounded rerun string, missing change-kind, volume-only difficulty rejection and legitimate fairness addition acceptance. |
| Forensic command boundaries | Explicit `LABEL=PATH`, defaults and output paths must not cross task boundaries. | Independently authored actual CLI test rejects foreign input/output and accepts same-task output. Separately executed six isolation tests with eight additional forensic-tool subcases, including symlink/default discovery. |

All follow-up findings are implementation defects or missing controls, not changes to evaluator policy. The no-injection handoff contract remains applicable only where injection is optional; mandatory-injection authoring floors were not waived.

## Commands actually executed by this oracle

| Command | Result |
|---|---|
| `python3 -B -m unittest discover -s Task_Authoring/tests -p test_independent_readiness_oracle.py -v` | **25 passed**, final rerun 0.418 s. Includes actual four-process shared ledger test and all earlier guide-derived pattern/binding/fairness regressions. |
| `python3 -B -m unittest discover -s Task_Authoring/tests -p test_readiness_integration.py -v` | **13 passed**, 2.156 s. Includes producer/artifact guards, reference routing, production precheck and post-baseline association. |
| `python3 -B -m unittest discover -s Task_Authoring/tests -p test_verify_isolation.py -v` | **6 passed**, 0.828 s; eight additional tool boundary subcases in one test. |
| `python3 -B -m unittest discover -s Task_Authoring/tools -p test_verify_design.py -v` | **9 passed**, 0.113 s. |
| `python3 -B -m unittest discover -s Task_Authoring/tools -p test_verify_identity.py -v` | **6 passed**, 0.074 s. |

The 25-test oracle suite was authored independently and does not import implementation-authored fixtures. The other suites are supporting regression evidence; their passing results alone did not determine this verdict. The oracle inspected their assertions and production paths, added its own negative/positive cases, reported the import-producer bypass, and reran after repair. The broad full-discovery and stage-gate sandbox runs are coordinator-owned and must be reported separately rather than attributed to this reviewer.

## Scope and limitations

- Synthetic full-gate record fixtures exercise readiness state transitions; they do not prove every semantic/base-data gate on a newly authored real V3 task. No complete active-task pilot occurred.
- No SQL was executed, no environment was deployed, no external tool readability was fabricated, and no paid model run was launched. Platform provenance requires real evidence later.
- Semantic authority, meaningful causal independence, task scope and deployment interpretation still require substantive review. Exact hashes and structural checks cannot prove those judgments true.
- Files and internal Python APIs are locally trusted; these controls prevent ordinary supported-command mistakes and false certification, not a malicious actor rewriting the pipeline or its records.
- Concurrent writes were exercised on the local POSIX filesystem. Direct evaluator-store concurrency and cross-host/network filesystem locking were not validated.
- The implementation preserves the existing failure-pattern logic; the oracle's guide-derived cases still pass. Any claimed improvement in paid-run cost or task difficulty remains an empirical follow-up.

No production code was changed by this oracle. Further production changes require affected-case reruns before reusing this verdict.

Additional standalone oracle_kit sandbox failure was reproduced by the coordinator against original HEAD code and classified as a pre-existing missing external fixture assignment, not a production regression. The self-test now creates its own disposable explicit V3 assignment. I inspected the patch and independently executed `python3 -B Task_Authoring/tools/oracle_kit.py --self-test`: PASS, including actual guarded hg.py base-record reads (found value PASS; wrong and absent values FAIL). No assertion was skipped or weakened. There are no unresolved local blocking findings.
