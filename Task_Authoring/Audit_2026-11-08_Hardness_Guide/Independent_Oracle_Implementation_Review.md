# Independent implementation oracle review

Clock: infrastructure audit; no task evaluation clock applies. Saved intake remains Oct 1, 2025 (synth-cut). No task inputs were changed.

Reviewer: separate `/root/oracle` agent, not an author of production changes. The reviewer owns only its regression tests and this report. Review date: 2026-11-08.

Final oracle verdict: PASS for the implemented local scope, with no unresolved blocking findings. The 18 independently authored tests and 9 integration tests passed in the final rerun after the reported fixes. External rollout and empirical limitations remain as listed below; this is not a platform-evidence certification.

## Expected outcomes and authority

Expectations were derived before tests from FINAL_IMPLEMENTATION_PLAN.md, both screenshot guides, Combined_Findings.md, Pipeline_Coverage_Report.md, the V3 policy, and the rubric playbook's scope, atomicity, visibility, sampling and work-kind rules. The guide's advice to raise weights does not override work-kind weights. Its decision/reason pair is valid only when the reason is requested. Its same-thread correction example does not prove independence under actual retrieval. Historical evidence remains readable but is not silently certified. Unknown platform deployment cannot be inferred from local SQL.

The numerical oracle uses the guide's two examples plus zero/one failures, three distinct failures, five failures with a group of three, exactly 50%, and a transitive bridge. Expected PASS/FAIL values are literal guide-derived expectations, not values copied from the implementation. Synthetic binding records represent Vincent-style batches without reading or changing completed-task evidence.

## Findings raised and resolutions

| Finding | Classification | Resolution / verification |
|---|---|---|
| O1: release used a pre-baseline platform validation path, permitting empty or unrelated baseline run identities | New integration defect | Release, difficulty and all-fail now invoke post-baseline validation, derive identities from bound exports and compare the platform receipt's exact set. Validator positive/no-run and negative/wrong-run cases executed. Independently reran production readiness integration: exact six-session set passes; empty post-baseline set rejects. |
| O2: a saved hardness review could retain its JSON hash after its referenced semantic proof changed | New integration defect | Current-stage evidence re-evaluates the review against actual referenced bytes. Independent regression preserves scenario on a new baseline file, then invalidates it after proof-file mutation. Passed. |
| O3: reviewed verifier receipts accepted generic observations shared by all runs | New binding validation defect | Receipt observations must identify the particular export and the particular verifier run section; generic `type`/`Run` text no longer binds. Independent valid reviewed receipt and adversarial generic receipt both tested. Passed. |
| O4a: Mode B accepted a quote anywhere in an export rather than in the cited event | New diagnosis validation defect | Requires a valid zero-based event index and quote in that event. Independent test first reproduced false PASS, then passed after repair. |
| O4b: relabeling an all-fail observation could avoid fairness/readability/grader review | New diagnosis validation defect | All-fail and heavy-all-pass sets are derived from actual matrix; explicit criterion coverage and relevant safety reviews are required regardless of supplied label. Independent label-evasion rejection passed. |
| O5: Mode B production integration trusted request bundle identity without comparing current artifacts | New integration defect | Production hook compares current binding_bundle_hash before consuming request. Source inspected after repair. |
| Intermediate `json` local-variable error in Mode B event validation | New repair regression | Reported immediately; corrected import scope. Independent baseline and correction tests rerun and passed. |
| Filename-only verifier/export association | Pre-existing defect being repaired | New independent tests accept correct exact-content batch despite shuffled filenames, reject changed/superseded export bytes, and reject filenames/context alone. Passed. |
| Final rubric required at rubric-planning stage | Pre-existing stage-order defect being repaired | Planning defers final row evidence; final rubric checking retains that requirement. Independently executed integration check passed. |

## Executed checks

1. `python3 -B -m unittest discover -s Task_Authoring/tests -p test_independent_readiness_oracle.py -v`: 18 independently authored tests passed in the final executed run (0.211 s). The file contains multiple subcases, including actual four-process ledger writes.
2. `python3 -B -m unittest discover -s Task_Authoring/tests -p test_readiness_integration.py -v`: 9 integration tests passed in the final rerun independently executed by the oracle (1.020 s), including actual production post-baseline association. This suite was authored by the coordinator and is supporting evidence, not the source of the oracle's expectations.

The independent test file is `Task_Authoring/tests/test_independent_readiness_oracle.py`. It imports production APIs, not implementation-authored test fixtures. All writes use disposable `Task_Authoring/support/scratch/` directories.

## Acceptance coverage

| Plan area | Evidence |
|---|---|
| Dependency DAG / freshness | Independent ancestor-cycle checks, certificate self-stability, baseline arrival leaves upstream scenario current, referenced proof mutation rejects; integration SQL mutation stales injection but preserves scenario. |
| Stage availability | Independent scenario review passes without SQL/prompt/final rubric/platform artifacts; deferred availability becomes required at injection. Integration local-readiness traversal does not require platform receipt. |
| Fairness / forecasts | Inaccessible required evidence and generic waiver reject; zero advisory forecast does not block otherwise valid design. |
| Binding | Exact-content six-run batch binds despite filenames/order; changed exports and metadata-free filename inference reject; reviewed receipt needs discriminating observations. |
| Evaluator identity | Mismatch in either direction produces review-required, not a newer/authoritative verdict; original policy identity retained. |
| Rubric scope / coverage | Legitimate independent region budget/allocation pair passes; unrequested explanation, duplicated fact, inflated lookup weight and sampling away core output reject. |
| Pattern logic | Eight guide-derived cases, including both screenshots and transitive bridge. Existing algorithm remains the source of grouping, checked against independent expected outcomes. |
| Corrected scoring | Raw matrix preserved, unsubstantiated correction rejected by Mode B, justified correction changes corrected cell only, errors excluded from score denominator. |
| Environment | Missing proof rejects; explicit no-injection receipt accepted; cross-task and changed-state proof reject; run IDs required only after baseline. |
| Concurrency | Four simultaneous process appends survive with no lost records; duplicate idempotence and conflicting identity reject; implementation lock scope inspected to cover reload/validation/commit. |
| Task isolation | Ambiguous four-task default rejects; explicit task works; mixed future artifact owner rejects. |
| Migration / efficiency | Missing legacy attestation is historical/unverified; immutable prior records retained; repeat attestation idempotent; baseline change does not force upstream redesign. |
| Mode B | Exact event support and all-fail diagnosis cannot be bypassed by arbitrary labels; report preserves raw/corrected data. |

## Limits and remaining external work

The integration traversal fixture supplies synthetic successful stage records. It verifies dependency and readiness behavior; it is not a full newly authored V3 task passing every source, lint and semantic gate. Existing full-stage regression fixtures are separate checks reported by the coordinator. No active-task pilot was authorized or performed, and no platform environment, SQL application, tool-readability run or paid baseline was created. Those remain real-world evidence requirements, not locally inferred passes.

The authoring profile's existing mandatory-injection policy is unchanged. Explicit no-injection works in platform-handoff validation where applicable; this review does not certify an injection-free traversal of a profile that requires injection. Direct concurrent writes to the evaluator-owned global input store remain outside authoring scope. Local POSIX locking was exercised; network filesystem or cross-host lock behavior was not.

Semantic source authority, intended scope, meaningful independence and deployment interpretation remain evidence-backed reviewer judgments. Hashes prove identity/freshness, not truth. Neither this oracle nor the implementation establishes a future baseline success probability or reduced paid-run count.

Final rerun scope: executed after the Mode B event/all-fail fixes, current-proof freshness fix, discriminating receipt fix, current Mode B bundle comparison, post-baseline identity association, and decisive-record readability coverage integration. No production edits were made by the oracle.
