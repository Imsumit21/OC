# Brief SA2: attribution and priors fixes (node_verdicts, hardness_ledger)

Repository: /Users/sumitkumar/Source/Outlier/OC, bundle Task_Authoring/. You own exactly these files:
- Task_Authoring/tools/node_verdicts.py
- Task_Authoring/tools/hardness_ledger.py
Do not edit any other file (not oracle_kit.py, not the E2E driver, not the fixtures). If another file needs a change,
report it instead of making it.

Read first: Task_Authoring/support/fix_session_2026-10-25/logs/verify/design_round2.md (rows H1-1..H1-9 and the
shared interfaces) and logs/verify/round1/code_h1.md plus redteam_attribution.md. Also read the three explore audits'
summary in NOTES.md and the current self-tests, because every behaviour you change needs a planted case.

## Goal

Implement H1-1..H1-9 exactly as the design states:
- H1-1 seeded_landings: supersession-resolved current records, keyed (revision, run, node); a superseding non-LANDED
  record removes the landing.
- H1-2 priors: observation records contribute counts.runs trials, not landed+not_landed; same-(task, revision, family)
  observations collapse to one trial set with landed = max(landed), not_landed = runs - landed; if a group's records
  declare run ids that are not disjoint, refuse the merge with a clear error rather than double counting
  (counts.confounded is neither landing nor trial). A17 must stay Beta(2.5705, 2.8544); A15 changes from
  Beta(1.9825, 3.4538) to about Beta(2.14, 3.17) — confirm exactly.
- H1-3: --seed-ledger without --reference is an error; rho must be finite and in [0, 1] (validate in priors and at
  the CLI with a clear message).
- H1-4: unknown deciding models are carried (unknown_decisions) and own() requires zero.
- H1-5: decider bounds briefs by the key's own last write (trajectory_ledger.table() will provide
  meta["key_events"] = {key: event}; SA1 is implementing it in parallel). Code defensively: if the key is absent from
  key_events, fall back to max(table_events) as today. Do not edit trajectory_ledger.py.
- H1-6: control/channel own-change is computed from truth vs degrade across the declared columns; every own field must
  be present in the written row; a missing own field is unobserved (not held/failed).
- H1-7: channel accounting separates observed / failed / held / unobserved; unobserved members never enter the held
  denominator; a wholly unobserved channel proposes nothing; slots-only channels get a deciding event/model from the
  failed slots' decided_by; HELD members get provenance.
- H1-8: the go rule subtracts control-explained (key, field) evidence from a channel's evidence before counting it.
- H1-9: a class difference is attributed to rule r only when abl[r][k] reproduces the written class AND leaves every
  other written column of k equal to the written row; else cascade. (This keeps SP-039 pending; the naive version
  would land it. Do not implement the unconditional version.)

## Constraints

- Python 3 stdlib only. Never execute SQL. Never edit Task_Authoring/task_inputs/ or the shared ledger
  (support/hardness_ledger/ledger.jsonl); never run git. Run every self-test ONLY as
  python3 -B Task_Authoring/tools/selftest_sandbox.py -- <tool>.py --self-test
  (from the workspace root); never run --self-test directly.
- Keep the docstrings in step with the behaviour.
- Every fix gets a planted case; extend the self-tests. Keep the summary lines accurate.

## Acceptance tests you must run and report

1. python3 -B Task_Authoring/tools/selftest_sandbox.py -- node_verdicts.py --self-test
2. python3 -B Task_Authoring/tools/selftest_sandbox.py -- hardness_ledger.py --self-test
3. The rev13 attribution re-run (read-only on the frozen copies; write the outputs under
   Task_Authoring/support/fix_session_2026-10-25/logs/h1/round2/):
   same command as Task_Authoring/support/fix_session_2026-10-25/scripts/final_evidence.sh's "H1 rev13 c05" block.
   Expected: 0 item differences (reference comparison still reports exactly the 2 landed-key differences: run-4
   validation seed extra keys and run-3 snapshot_labels), the same verdicts/landed keys as
   logs/h1/rev13_node_verdicts.final.json apart from what H1-9 legitimately changes (expect no change on rev13).
4. Priors: regenerate nothing in the shared ledger; print (read-only)
   python3 -B Task_Authoring/tools/hardness_ledger.py priors --model claude-opus-4-8 --family A17
   and --family A15, and report the exact Beta before/after your change. A17 must be Beta(2.5705, 2.8544); A15 must
   become the collapsed value.

## Report format (<= 60 lines)

- Files changed, finding ids implemented.
- Planted cases added (name + the failure it guards).
- Command outputs for acceptance 1-4 (the key lines).
- Any deviation, any cross-file need, any place where the audit and the design disagree.
- Labels [O]/[I].
