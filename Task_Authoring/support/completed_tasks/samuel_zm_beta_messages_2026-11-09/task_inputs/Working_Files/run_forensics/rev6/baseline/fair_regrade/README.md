# Rev6 baseline fair regrade (2026-11-05)

Advisory proxy. There is no rubric or verifier yet, so none of this is the grading of record.

`surface_grades.json` (one level up) is the raw `surface_grader.py` output: 61.7 %, SD 0.068. It joins on row names, so
rows the runs named "Axe Arena start" or "Lives recharged (Full Ammo Reloaded)" scored as failures.
`fair.py` joins on the Ticket column and checks each item on its own ticket. `sim.py` runs the shapes and the re-run simulation.

| Shape | Rows | Weight | Average | Pop. SD | Patterns |
|---|---|---|---|---|---|
| A sealed surface, fair grading | 57 | 227 | 74.8 % | 0.087 | 4, largest 50 % |
| B one call row per message, rest sampled | 80 | 300 | 80.9 % | 0.066 | 4, largest 50 % |
| C full per-target | 159 | 471 | 80.9 % | 0.047 | 4, largest 50 % |

Shape B and C weights are estimates (trap 5, rule on one item 3, copied value 1).
Shape A per-run: 78.9, 78.9, 56.8, 72.2, 83.3, 78.9. Counted calls: 184, 185, 177, 186, 188, 197.

If the ZOM rows were ruled invalid: average 89.9 / 92.7 / 94.7 %, and run-5 becomes a full pass.
`baseline_models FAIL` and horizon 194 in `sim.py` output are artefacts of that script's minimal input; see `surface_grades.json`
(provenance PASS, horizon 186).
