# Parallel authoring implementation

Clock: infrastructure audit; no task evaluation clock applies. Saved intake remains Oct 1, 2025 (synth-cut); no task inputs were changed.

## Selection and boundaries

`task_context.select_task(task_dir=None, artifact_paths=(), allow_implicit_single=True)` resolves an explicit CLI path, inherited environment, or a single artifact owner. With none, compatibility fallback is allowed only when exactly one `Task_Authoring/task_inputs*/00_Assigments.md` exists. Archives do not participate in automatic selection. Mixed owners, selected-task/path disagreement, future output paths owned by a different task, and symlink aliases across tasks reject before activation. `validate_task_paths` is available for tools that parse arguments themselves.

`runtime_context` applies this to its production entry points and activation. Explicit V2 archival diagnostics and self-tests retain the existing safeguards against treating V3 tasks as legacy. `task_context.py` CLI also selects explicitly. `hg.py` validates its final default-filled arguments and refuses evaluator task input paths before context activation.

Context identity now includes the resolved task directory and a task identity digest. Identical assignments in two folders no longer share context caches. Moving a task changes its current context identity: old evidence remains readable but requires review/rebinding before current certification. This implementation does not rewrite historical evidence or task artifacts.

## Shared-write inventory

| Writer / destination | Isolation or concurrency contract |
|---|---|
| `hardness_ledger.Ledger.append`, shared JSONL ledger | Stable sidecar OS lock covers disk reload, validation, duplicate/conflict/supersession decisions, and atomic durable replacement. Two pre-created stale Ledger objects cannot bypass current conflicts. Readers receive complete snapshots and do not create locks merely by reading. |
| `task_context.py --write`, task `Working_Files/00_Task_Context.json` | Explicit selected task; existing unique temporary file plus atomic replacement. |
| `runtime_context` legacy helper caches | Namespaced by task-bound context hash; previous in-process task objects cleared on switching. |
| `setup/local_search.py`, copied helpers, date index, cache | Task-bound context directory; existing atomic replacement; source identity and selected universe validated. Copies exclude evaluator input/output writers. |
| Stage reports and attestations | Task-local outputs; coordinator integrates selection and evidence validation in `stage_gate.py`. |
| `entity.py build`, per-universe entity KB | Shared maintenance output, separate from task-local reports. A per-target sidecar lock now covers build plus publication; a unique temporary file replaces the old shared `.tmp` path. Reads require matching universe/source metadata. |
| Evals standalone saved inputs and reports | Evaluator-owned shared global store. No changes authorized here. Concurrent direct intake/report writes are not supported by this authoring implementation; use `hg.py` for authoring reads and task-local authoring artifacts. |
| Universe exports and completed archives | Read-only; not used as writable fixtures or migrated. |

The ledger is still append-only in logical history: atomic replacement copies all prior records and adds accepted records. Raw records and superseded corrections remain present. Return values and read-only prior/query behavior are preserved. The lock is held for the entire decision and commit, not merely the final write. Local POSIX filesystem locking is assumed; cross-host network filesystem lock semantics were not tested.

## Executed isolated checks

- `python3 -B -m unittest discover -s Task_Authoring/tests -p test_parallel_safety.py`: 7 tests passed initially. Includes four processes with all Ledger objects instantiated before a barrier, distinct records, duplicate identity, conflicting identity, and supersession; mixed path/symlink/future output rejection and valid explicit/single-task flows.
- `python3 -B -m unittest discover -s Task_Authoring/tools -p test_task_context.py`: 29 tests passed.
- `python3 -B Task_Authoring/tools/hardness_ledger.py --self-test`: passed existing provenance, conflict, supersession and prior-calculation tests.
- Universe seam suite initially exposed two diagnostic-order regressions: evaluator input path rejection occurred after ambiguous task selection. The wrapper now rejects those paths before activation; final rerun result recorded below.

All concurrency fixtures live in disposable isolated folders. No baseline run, injection SQL execution, task rewriting or evaluator-policy mutation occurred.

Final reruns: universe seam suite passed all 33 tests. New isolated suite expanded to 8 tests including atomic entity publication; see final execution result. Entity source-data rebuild was not executed.
