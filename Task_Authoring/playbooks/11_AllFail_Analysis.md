# 11 — All-Fail Rubric Analysis (Playbook) — HarmonyGames · Spec V2

> Command: `/create-allfail` · Writes: `task_inputs/11_AF_Justification.md` · Paired eval: none (QC-scored as "Rubrics — All-Failing Rubrics"; rule file `Evals/references/rules/all_failing.md`) · Platform: screens 56–58 (`references/Taxonomy_V2_Step_Map.md`) · Gate: **`tools/stage_gate.py allfail` (blocking)** · Read first: `setup/GEN_EXECUTION.md`

## Purpose

After the single baseline verifier runs, every rubric that failed **all completed
rollouts** is rated on screen 58 ("Failed", justification required) with a 1–2 line
justification confirming a genuine model failure, not a false negative caused by the
criterion, the judge, the data or the environment (`all_failing.md`; `8_Rubric Writing - V2.md` §11).
This step finds those rubrics, classifies each from the trajectories and the universe,
writes justifications for the valid ones, and reports the rest.

An invalid all-fail is a false negative: the task looks harder than it is. Screen 56:
"fix the rubric instead of justifying it". Claude or Codex may author criteria (GEN_EXECUTION §2), so
this step reports each defect and may propose corrected criterion wording. Justifications are
model-authorable.

## Inputs / Output

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`
and read `Working_Files/00_Task_Context.json` (GEN_EXECUTION § 0). Use all eight
assignment fields, the assigned freeze and the context's registered universe/KB source.
The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is missing — there is no default. `freeze_utc` is the seed bound; the eval clock `universe.clock_utc` sits beside it and supplies the `Clock:` line. Check each relied-on fact at
the assigned freeze; shared KB summaries are leads, not a separate dataset gate.
V3 changed-topic rules take
precedence over the older V2 reference documents in `references/Docs/`; local authorship and hardness-profile
exceptions remain as recorded in GEN_EXECUTION § 2 and § 3a.

Inputs (all required unless marked; stop and name what is missing)
- `task_inputs/10_Baseline_Verifier_Results.md` — the platform verifier copy ("Run #N" blocks).
- `task_inputs/07_Baseline_Trajectories/` — the six rollouts.
- `task_inputs/09_Rubrics.json` — the criteria the verifier graded (same version).
- `task_inputs/04_Prompt.txt`, `00_Assigments.md` (persona), `03_Error_Async_Config.txt`,
  `01_Universe_Inject.sql` (or "no injection"), reference files the prompt uses.
- `08_OE_Writing_Ledger.md`, `08_Oracle_Events.md` (optional — leads and a comparison path, never authority).

Output
- `task_inputs/11_AF_Justification.md` — denominator, all-fail list, one
  classified block per all-fail rubric, the tally, and the hand-off line for `/create-difficulty`.
  `NONE` (with the denominator) when no rubric failed every completed rollout — the QC dimension
  is then an automatic 5.

## Step 1 — Parse and bind (mechanical)

Run the parser; it binds every verifier row to `09_Rubrics.json` by title and counts errored runs:

```sh
python3 Task_Authoring/tools/difficulty_stats.py --build \
  --verifier Task_Authoring/task_inputs/10_Baseline_Verifier_Results.md \
  --rubrics Task_Authoring/task_inputs/09_Rubrics.json \
  --trajectories Task_Authoring/task_inputs/07_Baseline_Trajectories \
  --task-type "<horizon from 00_>" --out Task_Authoring/task_inputs/Working_Files/12_difficulty_input.json
python3 Task_Authoring/tools/difficulty_stats.py Task_Authoring/task_inputs/Working_Files/12_difficulty_input.json
```

Rubric ids are `R<n>` = position in `09_Rubrics.json`. The all-fail list is the
calculator's "All-fail rubrics" line. The build **stops** — and so does this step — when:
the verifier file is empty or holds no "Run #N" blocks (the verifier has not run: these are
**not** errored rollouts); a run's "X/Y criteria passed" header disagrees with its rows; a row
does not bind to exactly one criterion (the verifier graded a different rubric version — re-run
the verifier on the current criteria; `coherent_record.md` S1); the verifier graded a run whose
trajectory is empty; a trajectory is truncated JSON. Never bind by guesswork. A warning that
`09_Rubrics.json` is not valid JSON means the builder export is damaged: say so in the output.

## Hard gates

1. **Denominator = completed rollouts.** Errored = empty trajectory file, no final `result`
   event, or an error result; excluded from the all-fail test. If 4 of 6 completed, an all-fail
   failed all 4; a rubric passed by any completed run is not an all-fail. Record excluded runs
   and why. Three or more errored (or fewer than 4 completed) = Error Rate Fail: say so and stop.
   Screen 59 Rule 0 wants all six complete — note any errored run for a re-run.
2. **Read every completed trajectory** for every all-fail — the final response, the write-tool
   arguments and their results — never the verifier's one-liner alone. Repetition never proves
   the Agent wrong; zero task-level passes does not make any all-fail valid.
3. **Validity tests, each answered with evidence** (record pointer, prompt quote, catalog entry):
   - **Authority** — the requirement comes from the prompt or a source the prompt clearly
     incorporates (`prompt-incorporation-v1`, `Evals/WORKFLOW.md`). Quote the incorporating
     passage. An unmentioned handbook, policy or house rule makes the criterion invalid.
     A fact may answer an ask without being quoted in the prompt; it cannot add an obligation.
   - **Grounding** — every ID, name, status, amount, date, count, destination and expected
     conclusion exists in base + injected state (SQL read as text, never executed), before the
     assigned freeze (shared context), in the version in force (corrections, supersessions).
   - **Reachability** — reachable by the assigned persona's scoped view (Gmail, Slack, Calendar,
     Drive family: persona-exact; Explorer-only or another persona's view is not reach;
     GitHub, Linear, Trello, Contacts, Confluence, Snowflake unscoped). Discoverable through the
     catalog tools as the runs actually used them (search coverage, pagination, filters).
     **Deciding record:** its `reachability` must be `PROMPT_LINKED`; a value stated only by a
     Trash/Spam copy, readable only inside an attachment, or unlinked from every prompt noun is an
     `unobservable` rubric defect (Eval 3 §2.4) — INVALID — rubric, never a valid all-fail.
   - **Capability** — for any create/export/deliver ask, classify the path SUPPORTED,
     UNSUPPORTED or UNVERIFIED (WORKFLOW "Output capability and failure attribution"); writes
     need a catalog write tool.
   - **Atomicity / destination** — one independently pass/fail condition, graded at the artifact
     or action the prompt requested. A row whose acceptance presupposes another row's finding
     is conditional: decide whether a run that did the asked action correctly can pass it.
   - **Precision / flexibility** — exact values for IDs, dates, counts and discrete fields;
     "approximately" only for calculated or rounded values; equivalent free text accepted; no
     route, wording, title, count or format the prompt did not ask for (214 MB = 214.0 MB).
     A row that rejects a fair alternative — a `BOTH_FAIR_FIGURE` value the saved prompt report
     records, the other day of a split PT/UTC date, an anonymized source token, or a format/count the
     prompt never states — is `overly_specific` (Major): INVALID — rubric, not a valid all-fail.
   - **Phrasing** — affirmative, Agent-centric, no tool name, title self-contained. Process rows
     pass the three-condition test (`all_failing.md` § Process). A row an idle Agent passes
     (`do_nothing_case` ACCEPT, e.g. "leaves X open" or "as found") fails Negative Criteria:
     INVALID — rubric.
   - **Friction** — a configured forced error actually fired and its recovery path exists; a
     configured async wait was actually taken (submit → check → get) by the runs.
4. **Classify** (the four classes of `all_failing.md`, plus unresolved):

   | Verdict | When | Counts as |
   |---|---|---|
   | VALID | every test passes and each completed run genuinely missed the requirement | justified on screen 58 |
   | INVALID — rubric | a test fails **and the defect causes the failure**: a correct, prompt-compliant run would still fail the row, or the defect explains what the runs did (e.g. they reached a valid alternative the row rejects) | invalid all-fail |
   | INVALID — environment | the required evidence or operation is systematically unreachable or UNSUPPORTED (tool-observability) | invalid all-fail; escalate |
   | JUDGE ERROR | a run's trajectory satisfies the valid criterion but the verifier failed it | not an all-fail; flag for the reviewer; hand to `/create-difficulty` as a judge correction |
   | UNRESOLVED | evidence is missing (UNVERIFIED capability, unreadable record) | not a demonstrated model failure; never justified; blocks handoff until resolved |

   Three rubric-defect classes make an all-fail INVALID — rubric when they cause the failure: `unobservable` (the deciding record is not `PROMPT_LINKED`), `overly_specific` (the row rejects a fair alternative), and a do-nothing negative (the row accepts an idle Agent).
   A defect that does **not** cause the failure (e.g. a non-atomic row whose every part every
   run missed) leaves the all-fail VALID for this dimension (QC: invalid = "a quality issue that
   causes the failure"), but it is still a rubric-quality finding: report it to be
   fixed (screen 56) and do not let the justification depend on it.
5. **Dependent rows get their own verdict.** When several rows fail on one root cause (one
   missed discovery), test each row separately; say which root cause they share. Shared
   cause is not itself a defect; an identical acceptance condition repeated across rows is an
   overlap finding for `/rubric`, not an all-fail invalidity.
6. **Justification shape (VALID only).** One or two sentences that state (a) the exact grounded
   requirement — value and source — and why it is a fair ask of this prompt (incorporating
   passage, reachable to this persona), and (b) the concrete miss shared by the completed runs
   (what they did instead, with the decisive omitted step). Every clause must be checkable in
   the trajectories. Never: "all runs failed" alone, a restatement of the criterion, a hedge
   that concedes a defect (a tool limit, an unreachable record, a requirement the prompt does
   not make — QC treats a justification that reveals the defect as an invalid all-fail), a claim
   no trajectory shows, or advice. An unfactual or irrelevant justification of
   a valid all-fail is a QC Non-fail.
7. **Invalid → report and fix.** Quote the criterion, name the failed test, the evidence,
   whether it is causal, and the consequence (inflates difficulty), and propose the corrected
   criterion. Fix it (Claude, Codex or the human) and re-run the verifier; then re-run this step and `/create-difficulty`.
8. **Never tune.** Never recommend deleting a valid criterion to move the difficulty numbers.

## Output format

```
Completed rollouts: <n>/6 (excluded: <ids + reason> | none)   Rubric binding: <ok | warning text>
Clock: <universe.clock_line>
All-fail rubrics: <ids or NONE>

### R<n> — VALID | INVALID — rubric | INVALID — environment | JUDGE ERROR | UNRESOLVED   (weight <w>)
Criterion: "<quoted>"
Per-run evidence: run-<k>: <what it did — tool + key arguments / quoted response or write> (<file> event <i>) …
Tests: authority … · grounding … · reachability … · capability … · atomicity/destination … · precision/flexibility … · phrasing … · friction …
Causation: <for each failed test: causal yes/no + why>
Shared root cause: <row ids or none>
Justification (VALID only): <1–2 sentences>
Finding (otherwise): <test failed · rule · evidence · consequence>

Summary: valid <n> · invalid <n> (rubric <n>, environment <n>; ≥ 2 = QC Fail, 1 = Non-fail) · judge errors <n> · unresolved <n> · non-causal defects to fix <ids>
Hand-off to /create-difficulty: --invalid <ids | none> --judge-correction <run-k:Rn … | none>

## Self-review
<below; ends with the stage_gate output>
```

## Self-review (GEN_EXECUTION §6a, this stage)

1. **Re-read as the eval.** Walk `all_failing.md` top to bottom, the QC row "Rubrics — All-Failing
   Rubrics" (`references/Docs/QC_Spec_Doc_Latest.csv`) and screens 56/58 against the output.
2. **Recompute the list independently.** From the raw verifier copy (not the calculator), count
   Fail decisions per criterion over the completed runs; the all-fail set is the criteria whose
   count equals the completed count. Compare with the calculator and with every "Run #N" header.
3. **Per VALID all-fail — strongest FAIL reading:** (a) *could a correct run fail this row?* —
   write the best prompt-compliant answer that differs from the row (other route, wording,
   granularity, a defensible alternative entity or conclusion, a count or format not asked
   for) and check the row would accept it; (b) *did the judge err?* — search each completed
   trajectory's final response and write arguments for the row's key value and its paraphrases;
   (c) *is the evidence really reachable?* — re-open the decisive record through
   `tools/hg.py` as the persona would, and the SQL text for injected rows; (d) *did friction
   or the environment block it?* Resolve each with a pointer; any unresolved doubt → UNRESOLVED.
4. **Per INVALID / JUDGE ERROR — strongest false-positive reading:** is the defect really causal
   (would the runs have failed anyway)? Is the "valid alternative" actually valid under the
   prompt? Does the "satisfying" passage meet every part of the criterion?
5. **Re-verify every justification sentence** against a trajectory locator and a source record; a
   value carried from the ledger, OE or verifier text is a lead, not evidence.
6. **Stage gate.** `python3 Task_Authoring/tools/stage_gate.py allfail Task_Authoring/task_inputs --paste` re-runs `difficulty_stats.py` on `12_difficulty_input.json` (write it in Step 1 with `--out`) and compares the all-fail list; checks one block per all-fail with an exact criterion quote, every completed run cited with an event, all eight tests, a 1–2 sentence justification for VALID; and needs one evidenced counter-reading per block plus the recomputation.
7. **Re-run** the calculator after any binding fix; **record** each counter-reading, its
   resolution, and anything left unresolved. Never soften a finding to reach a count of zero
   invalid, never invent one. Criteria and the prompt are quoted; a proposed fix is labelled as such.

## Deliver

Handoff is blocked until `stage_gate.py allfail` prints PASS. The denominator, each verdict, the justifications ready for screen 58, the invalid/unresolved
rows the human must fix (re-run the verifier after), and the hand-off line. Next: `/create-difficulty`.
