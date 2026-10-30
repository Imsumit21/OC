# Authoring a task after the P1 hardening

This guide is the companion to `Guide/How_To_Author_A_Task.md` (which owns the order, gates and loop-backs). It
records **what changed in the tooling** during the P1 hardening, **how each authoring stage is affected**, and the
**steps to re-certify an existing task** (task 1 is used as the worked example). The playbooks and skills remain the
method; this file only covers the deltas an author will actually hit.

Path convention: bare paths (`tools/`, `support/`, `task_inputs/`) are relative to `Task_Authoring/`; a command that
must run from the workspace root spells out `Task_Authoring/…`.

> **Status of the tooling (read first).** The hardening is locally green: the local suite (14/14), the E2E (14/14),
> both falsification suites, the rev13/rev14 reproductions, c05, V1 and the priors all pass on the final tree. It is
> **not independently certified**: the eight verification tiers were run on that tree and 7 of 8 FAIL (only
> `code_misc` PASS). The residual findings are listed in
> `support/fix_session_2026-10-25/logs/verify/round4_current/VERDICTS.md`. Until those are closed, treat the
> attribution and forecast output as **advisory**, and do not present a forecast as calibration or validation.

## 1. The one systemic change: the gate-policy hash

Every stage gate pastes a PASS block into the artifact's Self-review. That block carries the hash of the live
`tools/*.py` (`__gate_policy__`). The P1 edits changed the tools, so the hash moved:

```
pasted in existing artifacts:  e27466d3711e
live after the hardening:      bf8e231eb5d9
```

Consequence: **every pasted stage-gate PASS on every existing task is stale.** `stage_gate.py release` reports it as
`chain.* FAIL … upstream 'scenario' PASS is stale: __gate_policy__ (pasted …, now …)`. A task is not releasable until
each stage is re-run against the current tools and its PASS block re-pasted (`stage_gate.py <stage> <task_dir> --paste`
on PASS). This is expected cost of changing the tools, not a task defect — but it must be paid before the next
platform pre-check.

## 2. What changed, by tool

| Tool | New behaviour an author must satisfy |
|---|---|
| `surface_grader` | Tracker groups decode across same-line lists, `-`/`*`/`+` bullets (space or tab, task-list checkboxes, inline-code keys), bare key lines and Markdown tables (with/without outer pipes, key in any column). A counted first declaration (including zero) is authoritative; re-declarations never merge; a bare `---` is a horizontal rule, not a table; escaped pipes are prose unless the bullet is a list item; a stated count is a bare or parenthesised number ≤ 500, and date/time/year/month-name suffixes are not counts. Unreadable register/tracker content is UNGRADED, never false; average/full-pass gates are decided by bounds, SD/pattern gates by enumerated completions. |
| `gradable_surface` | `gradeable()` really decodes and grades a synthetic fixture for every slot (plus a must-be-False empty control). The CLI `gradeable-report` lists every ungradable slot by id/weight. Every slot must point at a deliverable and selector class the grader reads: table columns, tracker text, `json_text` / `calls` deliveries, `tracker_state`, `slack_thread`/`slack_channel_post`, `register_parent`, `share_reader`, `register_keys_exact`, etc. `truth_fields.groups` must name the list field. |
| `node_verdicts` | Control declarations are part of the contract: a control member written as the over-application gives is OVER-APPLIED (else HELD), with its deciding event/model, and is never a landing. Control-explained `(key, field)` evidence is its own class in the items, the rule verdicts and the ledger proposals; a class-only over-application cannot land. Channels are reported per run (FAILED/HELD/UNOBSERVED), a slots-only channel is judged on the surface, and a missing deciding record is UNKNOWN. Proposal provenance carries the observed record set, covered/observed counts, the deciding event(s) and an explicit fallback flag. `reference_landed` lands only a `None` or `mechanism` reference item; cascade/`mechanism?`/control/slip items are refused and reported as a contract disagreement. Every evaluated run records the observations it dropped and why. |
| `hardness_ledger` | `control` and `channel` records are kept outside the priors (they are F1 evidence, never landings). A control/channel record needs typed provenance (non-negative integer event or covered count, non-empty string model list, or a literal `true` unknown). A LANDED verdict that also landed an unexplained key stays a trial; a control-explained-only landing never does. H2 remains one trial per (task, revision, run, family) with the Kish design effect; rho is validated. |
| `hardness_forecast` | A record's rate unit must match the channel's declared latent (a run-unit posterior cannot silently feed a member-latent channel); a member-bearing channel with no declared latent refuses a run-unit rate. A channel with no eligible record is UNPARAMETERIZED **with its exclusion reasons**, never zero. Beta parameters are finite and inside [0.01, 1e9] (inf/nan/1e400 and the shapes that hang or collapse the sampler are refused). A batch channel whose briefs intersect none of its members refuses to be built. The sampler handles theta 0/1, tiny positive theta, large B and `B > 5000`. Every slot is reported (the top-25 is a presentation extra), and each slot's P(fail) and P(fails all six) are **workload, never a block**. The briefs digest is unambiguous and bound to the briefs object actually simulated; `landing_pairs` keys are escaped. |
| `f1_protocol` (acceptance harness) | Not an authoring stage. It is the F1 engine's acceptance record: 13 manifest ids × 3 seeds × 20,000 baselines, m = 39, Bonferroni z = 3.6558, three mandatory production-path checks, and a summarizer that rebuilds every assertion from sufficient statistics under the current gate. f6 (chain) is ABSENT because no chain channel ships; the replay is advisory with its original criterion recorded FAIL and withdrawn; there is **no calibration claim**. If a task ships a chain channel, f6 must be implemented and the gate re-run. |
| `oracle_kit` | The solver contract now includes `RULES[r].controls` (+ `over_application`) and `CHANNELS`; `contract.controls` is a blocking check. Determinism across processes (different `PYTHONHASHSEED`) and a golden base route (values read through `tools/hg.py records`) are checked. |
| `difficulty_mutation` / `hardness_gate` | Channel degrades and over-application operators are elements of the geometry (U counts them), never whole mechanisms. A non-composable solver gives U UNVERIFIED plus a written `geometry.U` disposition; a missing disposition blocks. |
| `selftest_sandbox` | Every self-test runs in a throwaway workspace and must not write the shared caches. If you add or change a self-test, run it through the sandbox. |
| `difficulty_stats` | One owner of model labels: strip only a bracketed suffix and compare exactly; `mixed_model` and `v3_valid` are separate outcomes; an unrecognised label is UNKNOWN, never valid. |

## 3. Stage-by-stage impact

1. **`/create-scenario`** — the solver/portfolio you design must already declare controls and channels (they are
   graded, not optional). Geometry U counts a channel degrade as a complexity element, so a scale/delegation design
   passes U only through its declared degrades. Each portfolio rule needs a `family` (prior family) and a `source`.
   The surface must be **gradeable at design time**: run `gradable_surface.py gradeable-report` and require 0
   ungradable slots before the SQL exists. `truth_fields.groups` must name the list field.
2. **`/create-injection`** — `contract.controls` is blocking, and every channel needs a rate: ledger records
   (`control`/`channel` kinds) or a disclosed `--channel-rate` with an independent source. A channel that moves no
   register column must declare surface slots or it is UNOBSERVED. `sql_lint`, `base_check`, `hardness_gate` and the
   preflight must all pass, and every mutation result must be dispositioned; a non-composable solver needs its
   geometry U disposition.
3. **`/create-hardening` MODE B** — read the control/channel records, not just the rules. The go rule counts only the
   expected model's own landings and pre-registered channel failures; a control-explained error is never a slip or a
   landing. Any `mechanism?` must be dispositioned (`features.disposed_by`) before a ledger append. The ledger keeps
   control/channel records outside the priors.
4. **`/create-reference-files`** — unchanged mechanically, but every number in an attachment must match the injection
   at the freeze, and an attachment must not pre-solve. A reference file is part of the assessed universe.
5. **`/create-error-async`** — unchanged gates; the alternate path must be proven, async twins accounted for, and the
   configured friction is realism only (never a difficulty lever).
6. **`/create-prompt-writing`** — the prompt must ask for the deliverable in a shape the decoder reads: tracker text
   with group lists/tables, a table/CSV-shaped register, a `json_text` write (tickets/summary/mail), or a Slack/Trello
   post delivered through `json_text`/`calls`. Do not rely on prose the grader cannot decode. Control/channel
   declarations are universe facts, not prompt hints: do not leak them.
7. **`/create-prompt-writing check`** + `/prompt` — unchanged, plus one practical check: dry-run the surface
   (`gradeable-report`) and spot-decode one realistic deliverable per selector class before the pre-check.
8. **`/create-humantime`** — unchanged; refresh it after the Oracle Events and after the baseline. Channel/control
   evidence is not a deliverable and must not inflate the time worksheet.
9. **`/create-oe-writing` then `oe-check`** — the fact ledger must include the control/channel facts and the exact
   deliverable locations. `release.oe_solvability` requires `Path feasibility SUPPORTED`,
   `Task solvability SUPPORTED_BY_OE` and `Blocking 0`, so an OE path that depends on a channel record the agent
   cannot see will block.
10. **`/create-rubric-writing` then `rubric-check`** — §G must cover every slot of the gradable surface (covering row
    id or a reasoned disposition per slot; missing/neither/bare label/gap/stale slot block). A criterion must not
    grade a control-explained field as a landing. An all-fail rubric needs the written all-fail justification; a
    forecast's P(fails all six) is workload, never a block. Weights stay in the V3 bands (1/3/5).
11. **`/create-allfail`** — every rubric that failed all completed baseline rollouts needs its valid/invalid decision
    and a 1–2 line justification; an all-fail rubric without one blocks.
12. **`/create-difficulty`** — six **V3-valid** runs are required (four runs are refused); model labels come from
    `difficulty_stats` (exact comparison; mixed and v3-valid separate). The matrix binds `assignment_hash`,
    `policy_hash` and `context_hash` and is refused after an assignment or policy change, and `--build` stops when a
    verifier row does not bind exactly once to a `09_Rubrics.json` criterion. The **stage certificate** (not the JSON)
    is what digests `12_difficulty_input.json`, `09_Rubrics.json`, `10_Baseline_Verifier_Results.md` and
    `07_Baseline_Trajectories`, so editing any of them after the paste makes the `difficulty` PASS stale — re-run and
    re-paste, do not hand-edit. The forecast
    runs with channels/batches; label it UNCALIBRATED and disclose UNPARAMETERIZED channels. Use the F1 protocol only
    as the engine's acceptance record, never as a per-task calibration.
13. **`release`** — the bundle digest needs the OE-check and rubric-check certifications, the stage inputs must be
    fresh (scenario not older than the assignment), the markers must be closed, and the difficulty gates must be
    clear with a non-empty rubric. Re-run every upstream stage first: the policy hash has changed.

## 4. Re-certifying task 1 — the steps

Task 1 is authored through the prompt/pre-check/baseline/AF but not through rubric, difficulty or release. Its
`09_Rubrics.json` is `[]`, `12_difficulty_input.json` / `12_Difficulty_Stats.txt` are absent, and the `05/08/09`
plan/check artifacts are missing. All pasted gate PASS blocks are stale (policy hash). In order:

1. **Re-run every stage gate and re-paste** (authoring session; it may edit `task_inputs/`), from the workspace root:
   `python3 -B Task_Authoring/tools/stage_gate.py <stage> Task_Authoring/task_inputs --paste` for `scenario,
   injection, hardening, reference-files, error-async, prompt-writing, prompt-check, humantime, oe-writing, oe-check,
   rubric-writing, rubric-check, allfail, difficulty`. `release` last. The last `release` run on the current tree
   reports **19 blocking** checks: 13 stale or missing chain certificates (all stages except `reference-files`),
   `release.bundle_digest`, `release.stage_inputs`, `release.markers`, `release.oe_solvability`,
   `release.difficulty` and `v3.rubric_evidence` — so finish the upstream work below before expecting release to pass.
2. **Write the missing artifacts** (gates read `Working_Files/` first, then a top-level legacy copy):
   `05_Human_Time_Worksheet.md`, `08_OE_Writing_Ledger.md`, `08_OE_Check.md`, `09_Rubric_Writing_Plan.md`,
   `09_Rubric_Check.md`, and a non-empty `09_Rubrics.json` (the current `[]` fails `v3.rubric_evidence`).
3. **Close the three open markers** the release scan actually finds on this tree (`release_markers` scans every
   artifact for `PROVISIONAL`/`UNRESOLVED`/`UNVERIFIED` and for `Unresolved:` lines that are not `none`):
   `01_Scenario_Design.md:L1002` (`Unresolved:` pre-registered posterior / ledger append),
   `01c_Preflight_Report.md:L10` (`Geometry U … UNVERIFIED`, blocking), and `01a_Hardening_Report.md:L211`
   (`Unresolved:` ledger append). Resolve the substance — do not cosmetically rename the line to `none` while the
   item is still open.
4. **Refresh the scenario** so it is not older than `00_Assigments.md` (the current `01_Scenario_Design.md` is newer,
   so this is already satisfied on this tree), and reconcile the surface (30/30 gradeable) with the prompt's
   deliverables.
5. **OE solvability**: run the OE check to `Path feasibility SUPPORTED`, `Task solvability SUPPORTED_BY_OE`,
   `Blocking 0`. `release.oe_solvability` requires exactly those three; `SUPPORTED` on solvability alone is not enough.
6. **Six V3-valid Opus 5.5 runs** for the difficulty stage. The current four baselines are V3-invalid (model mix) and
   cannot be used; the platform runs must be produced first. This is the hard offline boundary.
7. Then `difficulty`, then `release` with the pasted blocks current.

## 5. Rules that now cost the most cycles

- **Do not design a deliverable the decoder cannot read.** Run `gradeable-report` at scenario time, not after the
  baseline. A slot that is ungradable is a design defect, not a grader defect.
- **Declare controls and channels in the solver.** Without them, control evidence is invisible, the go rule
  over-counts, and the forecast has no rate. A channel with no record must be disclosed as UNPARAMETERIZED.
- **Never present a forecast as validation.** It is UNCALIBRATED, the F1 engine's acceptance is a synthetic-fixture
  check, and the pools are in-sample. Say "advisory", not "expected".
- **Re-run the gates after any tool change.** The policy hash makes every pasted block stale; an old PASS is not a
  PASS.
- **Keep the evidence with the tree.** `Task_Authoring/support/fix_session_2026-10-25/logs/verify/round4_current/VERDICTS.md`
  and the acceptance logs are the record; a green self-test is not a certification.
