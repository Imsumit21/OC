# Rev10 baseline review (6 Opus 5.5 runs, SQL c999829d668e, prompt b5ea6f0ff28c)

Graded by hand against solver/truth.json (sha f3dd0b9de6e2d3f8). Scripts: scratchpad extract.py and grade.py.
Note: surface_grade.json (tools/surface_grader.py) reads 36.7%, but it mis-decodes this sheet: it fails Paul and Anton rows in runs that got them right and its group classes are all 0. Don't use its score. Its provenance gates are fine: 6 of 6 completed, Opus 5.5 in every slot, horizon average 133.

## Per-run results

| Run | Calls (grader count) | SciPlay group | Dentsu build | T-Accelerate build | Paul | Anton | Other |
|---|---|---|---|---|---|---|---|
| r1 | 155 | In talks (wrong) | iOS and Android (wrong) | iOS and Android (wrong) | In talks $50K | $25K | none |
| r2 | 150 | In talks (wrong) | wrong | wrong | In talks $50K | **$40K (wrong)** | sheet not shared with Leonard |
| r3 | 123 | In talks (wrong) | wrong | wrong | In talks $50K | $25K | none |
| r4 | 139 | **Keep warm (right)** | wrong | wrong | In talks $50K | $25K | **Treo VC left out** (never opened its Sep 3 #bridge-pitch outreach; row, checklist item and card missing; Awaiting reply 13) |
| r5 | 119 | In talks (wrong) | wrong | wrong | In talks $50K | $25K | none |
| r6 | 114 | In talks (wrong) | wrong | wrong | In talks $50K | $25K | none |

Everything else was right in all six runs: Homa and Brightwater added, every off-list firm excluded, Hiro and LVP Keep warm, a16z In talks, e2vc Awaiting reply, the NCsoft comment instead of a card, no Dentsu or Makers card, the reply on Leonard's thread.

SciPlay In talks also puts SciPlay on the In talks checklist, gives it a follow-up card (20 cards instead of 19) and makes the reply counts In talks 8/1 and Keep warm 2/0.

## Trap catch rates (rev10: pre-check + 6 baseline runs)
- Build access (Arthur's thread reply): caught 0 of 7.
- SciPlay (#executives thread reply): caught 2 of 7 (pre-check, r4).
- Paul ("Done, signed it", no Completed notice): caught 7 of 7. The stated rule settles it.
- Anton ($40K to $25K): caught 6 of 7.
- Treo VC (natural): caught 6 of 7.

## Gates (estimated; the rubric and verifier remain of record)
- pass@1: 0 of 6 full passes. PASS.
- Average weighted pass rate: about 55 to 70% under an atomic rubric with weight 5 on the deciding values (draft weights: r1/r3/r5/r6 about 63%, r2 about 55%, r4 about 66%). Under 80% and under the 85% Medium cap. PASS.
- Horizon: average 133 counted calls, lowest 114. PASS.
- Model provenance: Opus 5.5 in all six slots. PASS.
- **Failure concentration: at risk of FAIL.** r1, r3, r5 and r6 fail exactly the same values (SciPlay plus both build-access cells), so any fair rubric gives them one signature: 4 of 6 failing runs = 67%, over the 50% limit ("Signature Over-Concentrated", Long Horizon Guidelines §6, Common Errors §9).
- **Spread: at risk of FAIL (local check).** With four identical runs the population SD of weighted pass rates is about 0.03 to 0.05, under the 0.1 floor.

## Cause
The difficulty sits on two near-deterministic choke points (build access missed 7 of 7, SciPlay 5 of 7). Most runs miss both, so most runs fail the same way. Paul's trap is caught every time, so it adds no variation. Playbook 12 routes this case ("SD < 0.1, uniform failure on the same rows" and "One pattern dominates") to: make the chains partially solvable, each with a different root cause, and land them on different rows. Re-weighting or deleting rubric rows is not allowed.
