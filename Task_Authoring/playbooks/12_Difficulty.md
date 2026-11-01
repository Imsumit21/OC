# 12 — Baseline Difficulty & Failure Patterns (Playbook) — HarmonyGames · V3

> Command: `/create-difficulty` · Writes: `task_inputs/Working_Files/12_Difficulty_Stats.txt` (+ `task_inputs/Working_Files/12_difficulty_input.json`) · Paired eval: none (QC-scored as the Trajectory dimensions; rules `Evals/references/rules/scoring.json`) · Platform: screens 59–61 (`references/Taxonomy_V2_Step_Map.md`) · Gate: **`tools/stage_gate.py difficulty` (blocking)** · Read first: `setup/GEN_EXECUTION.md`

## Purpose

Reproduce the platform's Baseline Difficulty Statistics (screen 60) from the six baseline
rollouts and the single verifier, apply the assigned V3 mode and unchanged local checks,
and — when a gate fails — say where the fix belongs. V3 supersedes conflicting V2
average/full-pass thresholds (`references/Docs/11_V3_Changes.md`). The platform computes
the screen numbers itself; this report shows *why* they come out as they do and adds the
gates the screen does not show (SD band, valid-rubric view, counted tool calls) before you
confirm screen 61.

## Inputs / Output

Inputs (all required unless marked; stop and name what is missing)
- `task_inputs/10_Baseline_Verifier_Results.md`, `07_Baseline_Trajectories/`, `09_Rubrics.json` (same version the verifier graded).
- `task_inputs/00_Assigments.md` and its normalized task context — assigned mode, horizon,
  role, freeze (`freeze_utc`, the seed bound) and universe (`key`, `clock_utc`, shutdown rules).
  Never infer a mode or switch it to pass a cap. Per universe: normal applies the Feb 11, 2026
  shutdown and departed-person rules; synth-cut has neither, Victor Barnes departed April 2025,
  and nothing after 2025-09-30 23:59:59 PT exists.
- `task_inputs/03_Error_Async_Config.txt` — friction to verify.
- `task_inputs/11_AF_Justification.md` — its hand-off line (invalid rubrics, judge
  corrections). If all-fails exist and 11 does not, run `/create-allfail` first.
- The numbers on platform screen 60, if the human pastes them (optional; compared in self-review).

Output
- `task_inputs/Working_Files/12_difficulty_input.json` — written by the parser (format in `tools/difficulty_stats.py`).
- `task_inputs/Working_Files/12_Difficulty_Stats.txt` — the calculator output unchanged, plus the notes below.

## The gates (V3 overrides; other existing checks retained)

| Gate | Pass condition | Source · failure mode |
|---|---|---|
| Rollout slots / errors | Exactly six slots, including errored exports; ≤ 2 errored **and** ≥ 4 completed | V3 six-run batch; inherited Error Rate · Too Many Erroneous Runs (Fail) |
| pass@1 (operational pass@k) | Fewer than five rollouts pass every fair rubric; five or six full passes fails | V3 explicitly states the five-of-six rule. Do not substitute ≤50% or derive different math from the “67%” label |
| Avg weighted pass rate | Easy **<90%**, Medium **<85%**, Hard **<70%**; equality fails | Assigned V3 mode; corrected fair rows first · Avg Pass Rate Too High (Fail) |
| Model provenance | Every baseline slot has recorded Opus 5.5 model evidence; mixed/wrong/unknown models block | V3 requires Opus 5.5 for the pre-check and all six baselines; pre-check is validated separately by the stage gate |
| Per-rollout spread | population SD of per-rollout weighted pass rates in 0.1–0.3, edges inclusive | Retained local Evals check; V3 does not restate it · < 0.1 deterministic, > 0.3 ambiguous rubrics (Fail) |
| Failure patterns | ≥ 2 patterns; same pattern unless results differ on ≥ 2 rubrics; largest ≤ 50% of failing rollouts (exactly 50% passes) | QC, screen 59 Rule 2 · Too Few Signatures / Signature Over-Concentrated (Fail) |
| Horizon | counted calls of the golden run if any rollout scored 100%, else the completed-rollout average; Normal 50–100, Long 100–500+ | QC Task Type & Horizon · Wrong Horizon (Fail, under) · Borderline Horizon (Non-fail, over) |

Rubric-shape readings that are **not** difficulty failures:
- **Narrow NON-FAIL bands.** A rubric landing NON-FAIL 3 on `hg-strict-overrides-v1` (Minor on 5–10% of rows, 10% or fewer weights one level off, exactly one missing ordering check, off-pattern agent-centric titles on 10% or fewer rows) is still a valid rubric; report it and never change criteria to move a number.
- **Both-fair figures.** A `BOTH_FAIR_FIGURE` fork the saved prompt report records is intended. Runs splitting between X and Y are not an ambiguous rubric; do not collapse the fork, narrow a row to one value, or treat the split as a failure-pattern defect.

Readings the rules leave open — the calculator applies the strictest and prints the other:
- **Pattern grouping.** "Same pattern" is pairwise; grouping can be transitive (single-linkage,
  verdict) or a set of rollouts all within one rubric of each other (pairwise reading, shown).
  If they disagree the verdict says so; screen 60 is the record.
- **Errored-run denominators.** Preserve existing handling: average scores, SD and fallback
  horizon use completed rollouts only; errors are never scored zero. The full-pass gate
  uses the explicit count out of six slots. Report both counts. V3 does not restate a new
  scoring treatment for errors; flag any disagreement with the platform rather than guessing.
- **SD.** Population SD of weighted rates (verdict); sample and unweighted SD are shown and a
  band-edge note appears when either reads the other way.
- **Several golden runs.** Any golden run under the tier fails the horizon.

## Hard gates

1. **Measure, never estimate.** Build the matrix with the parser (`/create-allfail` Step 1 — same
   command, adding `--invalid <ids>` and `--judge-correction run-k:Rn` from 11's hand-off line),
   supplying `--task-dir Task_Authoring/task_inputs`. `--task-type` is optional; when supplied
   it must match the assignment. Then run
   `python3 Task_Authoring/tools/difficulty_stats.py Task_Authoring/task_inputs/Working_Files/12_difficulty_input.json --task-dir Task_Authoring/task_inputs`.
   The build stops on empty or template verifier output (not errored runs), unbound rows, header
   mismatches, a graded run with an empty trajectory, or truncated JSON — stop with it.
   Paste the output unchanged; disagree beside it, never edit numbers. The matrix records
   assignment/policy/context hashes; changed or missing hashes require rebuilding. Each run
   records actual trajectory model IDs and their source. An empty errored export needs
   independent platform model evidence recorded as `models` plus `model_source`; a filename
   does not prove the model. `--legacy-v2` exists only for archival regression checks.
2. **Two views, never silent.** The platform view keeps every rubric and the raw verifier
   results (what screen 60 shows). The valid view drops rubrics 11 judged INVALID and applies
   documented judge corrections (QC: "pass all valid rubrics"; `scoring.json`: "score only valid
   rubrics"). For V3, the **corrected fair view determines the verdict**; the raw platform
   view stays visible as audit evidence. Corrections need 11's trajectory evidence. Fix
   unfair rows/expected values and re-run the verifier before submission; a local correction
   is an audit aid, not a replacement for a current verifier export.
3. **Count real tool calls.** Counted = MCP service calls (main thread and sub-agents) minus
   blocked calls (error results), exact repeats and `set_acting_user` (`scoring.json`
   "Complexity Threshold Layers"; `long_horizon.md`). Raw and harness (Bash, Agent, Read, Task*)
   counts are shown beside it. ACL-denied reads return "not found" and are not detected:
   check by hand when a run hammers inaccessible records, and subtract them. Padding — many
   near-identical searches, re-opening the same record — is reported as a failure mode of its own.
4. **Friction actually fired.** If `03_` configured errors or waits, confirm from the trajectories
   that the errored tool was called and failed and that submit → check → get appeared. If not,
   the friction added nothing and recovery criteria are ungradeable — flag it.
5. **Fairness before difficulty.** Check failed rows against the requested work and actual
   source records, correct unfair rows and wrong expected values, and re-grade. Only then
   compare the corrected mean with the assigned cap. If it reaches the cap, make the
   universe harder. Do not add/strengthen rows to depress scores or delete a valid check
   merely because its expected value needs correction.

## Diagnosis and routing

The score-shape rows from `/create-hardening` B3b are merged into this table (plan §2, §9: content move). The universe
fixes in the Route column are designed in `/create-scenario --revise` from the MODE B forensics.

| Symptom | Likely cause | Route |
|---|---|---|
| Too Easy / average too high (uniform success, corrected avg ≥ assigned cap) | Evidence sits in one obvious place; rules stated where Opus reads first; the prompt names the artifact; a mechanical cohort; no rarely-opened evidence; no conclusion-sounding message to stop at; correction met before the claim it overturns | `/create-hardening` (MODE B forensics), then `/create-scenario --revise`: move rules to hidden authorities with decoys, add A13/A14/A15/A17 chains, never just add volume; prompt-side defects go to the human |
| Material failures in most runs, corrected average ≥ assigned cap | Mechanism-dependent weight is too small (≈ 26 % in `Hardness_Mastery.md` §11, NF2) | `/create-scenario --revise`: add independent chains whose facts the deliverable must carry; never re-weight to hit the gate (geometry U and L_max in the preflight show the room) |
| Gate fails only in the corrected fair view | Unfair rows were inflating difficulty | Fix the criteria and re-run the verifier; then deepen the universe if the assigned cap is reached |
| Raw average low, clean (corrected) average high | All-fail rows from unincorporated rules, unauthorized criteria or verifier errors | Not hardness — route the defects (`/create-allfail`, `/create-rubric-writing check`); rebuild the difficulty on incorporated mechanisms (`Hardness_Mastery.md` §11, recert task: 48.7 % raw, ≈ 80 % clean) |
| One pattern dominates (bimodal: some runs near 0, some near 100) | A single choke point carries the difficulty — usually one hidden authority (A12) gating most requirements | Add an independent difficulty source: split governance across 2–4 authorities in different rarely-searched services, or a chain landing on different rows (`Hardness_Mastery.md` §0) |
| Over-concentrated only by single-linkage chaining | Rollouts differ by one rubric step by step | Report both readings; read screen 60; treat as at risk |
| SD < 0.1 | Uniform success, or one universal blind spot everyone misses the same way | Uniform success → `/create-hardening` then `/create-scenario --revise`; uniform failure on the same rows → check those rows in 11 first, then make chains partially solvable with a different root cause each |
| Short runs (< 100 calls) on a cohort task | No cohort mandate reached the agent, or a bulk shortcut exists | Make the cohort rule an incorporated requirement; remove the shortcut (`Ask_Carriers.md` §3) |
| Many calls, high score | Volume without judgment (the 0.984 / 816-call case) | Add per-record house rules, boundary records, derived figures |
| Too Easy and every trap settled on its first read (Hardness v2) | A correction sits where the agent already is: the superseded record's container, an anchor's thread or file, or the record that delegates to it; or a bulk call carries the answer | `hardness_v2_check` SAME_PLACE names the traps; `/create-scenario --revise`: move each correction to a later reply on another item, a page comment, a review or another service (`Hardness_Mastery.md` §13.4) |
| Too Easy with no "done" in doubt | Every source agrees on status; nothing claims done while a piece is missing | `/create-scenario --revise`: add a done source with the missing piece in another service (A24) or a completion note somewhere else (A25); `hardness_v2_check` DONE_CHECK |
| Heavy rows (weight 5) pass 6/6 | Those are the parts Opus 5.5 finds easy (v2 Part 8) | Don't add more of that kind of row or work; change what decides them (a v2 move), never add rows, items, steps or prompt rules |
| Latching early (narration "I have enough") | The decoy is the first plausible source | Keep — this is the lever; make sure the real authority is findable by its name |
| SD > 0.3 | Near-0 and near-100 runs | One gating discovery or an ambiguous row — check row ambiguity, then split the gating discovery |
| Wrong Horizon | Scenario too narrow for the tier | Deepen the universe; never pad with blocked or repeated calls |
| Borderline Horizon | Scenario larger than the tier | Non-fail; note it. Narrow only if that honestly simplifies |
| 3+ errored / < 4 completed | Platform or friction problem | Re-run; check friction against the first trajectory |

After any prompt or universe change the baseline is re-run in full (re-inject the SQL first)
and every downstream step re-checked; after a criterion change, the verifier is re-run and
11 and 12 are redone (scores bind to the exact rubric version).

**What this stage owns** (plan §2, §4.6): B0 file mapping (each trajectory ↔ verifier `Run #N` by content, never by file
order: `tools/trajectory_ledger.py` binds every export to its revision and `difficulty_stats.build` maps the files), B2
friction and horizon (`trajectory_ledger.py` counts through `difficulty_stats.count_tool_calls`), the routing above
(B3b) and the corrected numbers. On a gate failure after fairness corrections the next step is `/create-hardening`
MODE B (baseline), whose output `/create-scenario --revise` consumes. The pre-registered forecast (its ledger id is in
`01c_Preflight_Report`) is compared here with the corrected gates of record: save `difficulty_stats.py <input> --json`
output, write the forecast's yes/no predictions (for example "the baseline fails a difficulty gate", confidence
1 − P(all gates) per reported scenario) with their sha256s, and score them with `hardness_forecast.py score --append`,
which records the outcomes in the ledger. It stays advisory and UNCALIBRATED until plan §10 Phase 2.

## Report format

```
Task type: <normal | long-horizon>   Difficulty mode: <assigned easy | medium | hard>   Completed: <n>/6   Errored: <ids + reason>   Invalid rubrics: <ids>   Judge corrections: <run:R>
Clock: <universe.clock_line from 00_Task_Context.json, verbatim>   Seed bound: <freeze_utc>
<calculator markdown output, unchanged>
Readings: <pattern / pass@1 / SD / golden notes from the verdicts, or none>
Tool-call notes: <raw vs counted per rollout; ACL-denied or padded calls found by hand>
Friction check: <fired / not configured / did not fire — evidence>
Screen 60 comparison: <platform numbers vs platform view — match / mismatch + cause | not supplied>
Diagnosis: <for each failing gate: view, cause, route>
Screen 61: confirm only if every gate passes in the corrected fair view and corrected rows have been re-graded.

## Self-review
<below; ends with the stage_gate output>
```

## Self-review (GEN_EXECUTION §6a, this stage)

1. **Re-read as the eval.** Read V3's mode caps, explicit five-of-six rule and fairness-first
   order before walking unchanged QC rows (Error Rate, pass@1, Average Weighted Rubric Pass
   Rate, Failure Signature Concentration, Task Type & Horizon in
   `references/Docs/QC_Spec_Doc_Latest.csv`), `scoring.json` "Agent Failure Rate" / "Error Rate" /
   "Complexity Threshold Layers" and screen 59 against the output, gate by gate.
2. **Recompute every gate number independently** from the matrix, without the calculator:
   completed/errored count; pass@1 as a count and a percentage; the average weighted rate from
   the weights (Σ passed weight ÷ Σ weight per run, then the mean); the SD by formula; a
   rollout × rollout table of differing-rubric counts to group patterns by hand; the horizon
   basis. Any difference from the calculator is a defect to explain before handoff.
3. **Counter-reading per gate.** For each PASS, the reading that would fail it (sample SD,
   single-linkage chain, an incorrect full-pass count, raw tool calls, a run that should be errored, an
   invalid rubric 11 missed). For each FAIL, the reading that would pass it (pairwise grouping,
   a judge error, a valid-view-only failure caused by a rubric the human can fix). Resolve with
   evidence; name what stays open.
4. **Re-verify inputs, not notes.** Spot-check one trajectory's counted calls by hand; confirm the
   `--invalid` / `--judge-correction` lists match 11 verbatim; confirm the rubric version,
   all six models, assigned mode and current assignment/policy hashes.
5. **Stage gate.** `python3 Task_Authoring/tools/stage_gate.py difficulty Task_Authoring/task_inputs --paste` re-runs the calculator and requires the current gate-table lines and all-fail line pasted unchanged, every report line, and `Invalid rubrics` = 11's `--invalid` = the `"valid": false` rubrics in the input JSON. Address model provenance alongside the existing six gate counter-readings.
6. **Record** each gate's final verdict per view, its evidence, counter-readings and their
   resolution. Never edit a number, never soften a FAIL, never invent one.

## Deliver

Handoff is blocked until `stage_gate.py difficulty` prints PASS. Deliver both views,
the blocking gates, routing and self-review. Confirm screen 61 only when every gate
passes in the corrected fair view and the verifier reflects the corrected rubric.
Distinguish V3 cap/full-pass failures from retained local SD/pattern/horizon checks.
Eval Portal submissions and review screenshots are handled by the user.
