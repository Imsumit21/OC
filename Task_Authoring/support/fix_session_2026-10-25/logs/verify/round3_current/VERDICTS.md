# Final verification of the P1 tree (2026-10-27 05:5x): 8 tiers, all on this exact tree

Tree: the working tree after the session's last edit (`tools/surface_grader.py` tracker key-regex fallback and
`tools/gradable_surface.py` selector type guards). Bundles rebuilt from this tree by
`build_verify_diffs.py` + `build_verify_bundles.py` (diffs exit 0; every CHANGED file matched a hash-verified
post-move baseline). Freeze of the starting tree: `FREEZE.sha256`.

| Bundle | Tier | Verdict | Verified by | Review |
|---|---|---|---|---|
| code_g1 | code | **FAIL** | openai/gpt-6.1-sol#max | A multi-line tracker group can lose members ("- K-01\n- K-02" after a stated count); `_krx` fallback and the other round-7 findings are fixed, this one is new. |
| code_h1 | code | **FAIL** | openai/gpt-6.1-sol#max | node_verdicts is the unchanged pre-session file: control-explained items remain `slip` and can be emitted as LANDED verdicts into the priors; slots-only channels bypass subtraction. |
| code_f1 | code | **FAIL** | openai/gpt-6.1-sol#max | hardness_forecast unchanged: a run-unit posterior can feed a member-latent channel; other round-2 forecast findings stand. |
| code_misc | code | **FAIL** | openai/gpt-6.1-sol#max | Mutually contradictory with code_g1's acceptance of the same selectors on one point (a truncated finding); the task-1 surface (30/30) and the real gradeable dry run are accepted. |
| redteam_grading | redteam | **FAIL** | openai/gpt-6.1-sol#max | Surviving: multi-line tracker groups lose members (same case as code_g1). |
| redteam_attribution | redteam | **FAIL** | openai/gpt-6.1-sol#max | Control filtering is applied to the go-rule summary but not to classification, rule verdicts or ledger proposals; a control's class cascade can survive. |
| redteam_forecast | redteam | **FAIL** | openai/gpt-6.1-sol#max | Run-unit records used as per-member rates; top-25 slot reporting; M6 sampler boundaries; invalid Beta overrides accepted. |
| methodology | methodology | **FAIL** (fallback: anthropic hold timeout) | openai/gpt-6.1-sol#max | Advisory conversion and figures now supported; one SE statement and some implementation guarantees remain stronger than the code; the 13-assertion protocol gate is still incomplete. |

**P1 is NOT closed.** Every FAIL above is a real finding on the final tree; none is a credentials/hold UNKNOWN.
Round-3 history: the first three rounds of `code_g1` (5 + 5 + 3 findings) and two of `code_misc` (8 + 5) were fixed
in `surface_grader.py`/`gradable_surface.py` before this final run; the surviving findings are listed per bundle.

## Local acceptance on this same tree (all PASS)
- suite 14/14, shared-cache fingerprint 0 differences, linked folders unchanged (`logs/p1_suite_round14.log`).
- E2E 14/14 (`logs/e2e/e2e_round21.log`).
- falsify_g1 PASS (`logs/g1/falsify_g1.round15.txt`), falsify_h1 PASS (`logs/h1/falsify_h1.round15.txt`).
- rev13 reproduction 0 differences in both views (`logs/g1/rev13_c10_round20.txt`,
  `logs/g1/rev13_c10_solver_round20.txt`); rev14 failed sets exactly of record (`logs/g1/rev14_grades_round20.txt`).
- c05: 0 item differences, exactly the 2 documented landed-key seed differences (`logs/h1/round15/c05.log`).
- V1 acceptance PASS; priors unchanged (A17 Beta(2.5705,2.8544), A15 Beta(2.1429,3.1714)/Beta(2.7143,2.6),
  A7 Beta(1.4524,2.2381)); `references/mechanism_priors.json` untouched.
- Task 1 `surface.gradeable`: PASS, 30/30 (`logs/task1_surface_gradeable.md`).
- Frozen rev13/rev14 SHA256SUMS verified before and after every run.

## What this means for P1
The surface-grader and surface.gradeable rows (G1 + SG) are substantially hardened and locally green, but they have
not reached an independent PASS: one tracker-group decoding defect survives. The attribution (H1), forecast (F1/M6)
and F1-protocol rows are unchanged from the start of this session and remain FAIL. P1 requires current PASS verdicts
from code, redteam and methodology; it does not have them.
