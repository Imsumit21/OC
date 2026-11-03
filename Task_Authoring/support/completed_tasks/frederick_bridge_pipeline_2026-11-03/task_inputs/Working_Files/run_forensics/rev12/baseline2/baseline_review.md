# Rev12 baseline batch 2 review (6 Opus 5.5 runs, same SQL 69db98aed17f and prompt b5ea6f0ff28c)

This batch replaces batch 1 (../baseline/, failed patterns at 80%). Graded by hand against solver/truth.json (sha 2ce0c48e71ff3bc2), then tools/difficulty_stats.py on a draft matrix that follows downstream_notes.md, with model evidence from the trajectories (trajectory_provenance). The real rubric and verifier remain of record.
Files: runs/trajectory-run-1..6.json (shas 6106cac2, ad54535a, 73fbae4d, 43647b1a, 74d58205, a8204373). Every run: Opus 5.5, result success/completed, 0 write errors. Run 1 has 2 autocompact synthetic notices and finished.

## Per-run results
| Run | Calls | SciPlay | Paul | Build access (4 cells) | Anton | Draft score |
|---|---|---|---|---|---|---|
| r1 | 164 | In talks (miss) | In talks $50K (miss) | iOS only (right) | $25K | 66.7% |
| r2 | 165 | Keep warm (right) | miss | iOS and Android (miss) | $25K | 59.5% |
| r3 | 145 | miss | off (right) | right | $25K | 79.8% |
| r4 | 152 | miss | right | miss | $25K | 56.0% |
| r5 | 118 | right | miss | miss | $25K | 59.5% |
| r6 | 149 | right | right | right | $25K | 100% (golden run) |

Everything else right in all six: sheet name, folder and share with Leonard; 4 checklists on the card; NCsoft comment on the Anel card; no Dentsu or Makers card; reply-all on Leonard's thread; per-group counts consistent with each run's own groups. Runs 1 and 5 state a wrong grand total in the reply (27); there is no total row in the draft rubric, and none should be added (Leonard asks for counts per group).

## Gates (difficulty_stats.py, draft matrix)
- Errored runs 0/6: PASS. pass@1 1/6: PASS. Average 70.2% (< 85% cap, < 80% target): PASS.
- SD 0.154 (sample 0.169, unweighted 0.119): PASS.
- Failure patterns: 4 patterns, largest 40% of 5 failing (r2 and r5); pairwise reading 40%: PASS.
- Horizon: golden run r6, 149 calls: PASS. Models: all 6 claude-opus-5-5: PASS.
- Blocking gates: none.

## Robustness of the verdict to rubric shape
- Patterns stay PASS if build access is one row instead of four (r3 and r4 then join: largest 2 of 5 = 40%).
- SD falls as always-passed weight is added: it reaches 0.1 at a total weight of about 129 (draft total 84). Keep the rubric lean: total weight under about 120, trap rows at weight 5 and per-entity rows separate.
- Average stays far under 85% for any fair weighting.

## Trap catch rates, rev12 (pre-check + 12 baselines)
- SciPlay: 6 of 13. Paul: 6 of 13. Build access: 9 of 13. Anton: 11 of 13.
- Batch 1 showed SciPlay and Paul missed together; batch 2 shows them independent. Batch-to-batch variance is large.
