# Human Time Worksheet — stage-gate-fixture

Pass: first        Tier: Long-Horizon
Hours: 10.50

| Sub-task | Kind (read / dead end / workaround / re-read / write) | Volume (measured, persona view) | Rate | Minutes |
|---|---|---|---|---|
| Skim #winddown Feb 2026 | read | 1,240 messages | 3,000/h | 25 |
| Open each ENG defect and its comments | read | 48 tickets | 9 min each | 432 |
| Stale hub count followed first | dead end | 1 thread, 14 replies | 20 min | 20 |
| Check claimed fixes against PRs | re-read | 12 PRs | 6 min each | 72 |
| Build the schedule | write | 1 file, 48 rows | 1 h 05 | 65 |
| Hand-off post | write | 1 message | 16 min | 16 |
| Total | | | | 630 = 10.50 h |

Tier check: in band (Long-Horizon 5–120 h)
Condensed breakdown length: 612 characters (field accepts 50–2,000)
Sources measured: hg.py search slack "#winddown" window 2026-02-01..13 (1,240); hg.py search linear ENG state Bugs (48); persona_view search arthur_blake slack "0.3.309"

## Self-review

| Check | Verdict | Strongest counter-reading | Resolution (evidence) | Unresolved |
|---|---|---|---|---|
| Inflated | PASS | 9 min per ticket is slow | V1 anchor 8–15 min per record (05_Human_Time_Estimate.md gate 3) | none |
| Solution-path | PASS | the stale hub is skipped | dead-end row for C0ADGSZKR3R/1770940000.000100 | none |
| Evaluator-wide | PASS | Slack volume counts hidden channels | persona_view search, persona filtered | none |
| Tier mismatch | PASS | 10.5 h is high for the scope | Long Horizon anchor 10 h (Long Horizon §4) | none |
| Linter reading | PASS | the linter sees only 48 tickets | volumes named in the breakdown (ENG-2280 children) | none |

Unresolved: none.

```
STAGE GATE humantime: PASS — Task_Authoring/support/local_search/cache/stage_gate_selftest/gen · 05_Human_Time_Worksheet.md#c97e6d740a70 · blocking 0 · warnings 0 · checks 16
[PASS] structure.outputs: 1 output(s) present: 05_Human_Time_Worksheet.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 00_Assigments.md, 08_Oracle_Events.md, 07_Baseline_Trajectories)
[PASS] chain.prompt-check: upstream 'prompt-check' PASS pasted and current (04_Prompt_Check.md#768fb7a25f6f, 04_Prompt.txt#19c9b7220c07)
[PASS] structure.placeholders: no placeholders in 05_Human_Time_Worksheet.md
[PASS] structure.arithmetic: 6 sub-tasks sum to 630 min = 10.5 h
[PASS] evidence.volumes: every sub-task has a measured volume
[PASS] structure.kinds: dead-end / workaround / write lines present
[PASS] structure.field_length: condensed breakdown 612 characters
[PASS] evidence.sources: volume sources name the hg.py / persona_view queries
[PASS] structure.tier_check: tier check line present
[PASS] boundary.retypable: no paragraph written to be retyped
[PASS] review.counter_readings: 5 evidenced counter-readings (of 5 found; need ≥ 5) in 05_Human_Time_Worksheet.md
[PASS] review.coverage: self-review addresses all 5 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```





