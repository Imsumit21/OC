---
name: rubric
description: "Evaluate an existing HarmonyGames rubric against the prompt, source evidence and QC rules. Return findings and scores without generating, rewriting or prefilling rubric criteria."
model: claude-opus-5-5
effort: xhigh
---

# Evaluate the supplied rubric

`/rubric` is evaluation-only. `/rubric audit` is an alias. Apply
`rubric-revision-v10` grading under the `rubric-eval-only-v1` workflow.
Use only Outcome and Process as category names in rubrics, reports and coverage
maps. Do not introduce numbered subtypes.
`/rubric create` is retired: explain that this skill evaluates supplied criteria
and request the existing rubric if missing. Never generate a substitute.

Follow `Evals/INPUTS.md`: list saved inputs, save new submissions under their
own keys, then read the actual relevant contents. Required: the existing rubric,
exact prompt, assignment/persona and applicable prompt reference files. Use a
supplied OE as a comparison reference; an OE PASS or OE repair is
not a prerequisite. Verify acceptance-bearing facts against primary sources.
Optional injection SQL needs saved SQL or an explicit no-injection decision.
If unresolved, ask with the other missing inputs: **Injection SQL (optional): does
this task use any? If yes, paste or attach it; if not, say no injection.** Save an
explicit answer with `hg_store_input.py no-injection`. Save partial inputs before
waiting. Requested output files are not missing reference attachments.

Read `Evals/EXECUTION.md` for workspace resolution and `Evals/3_Rubrics_Eval.md`
in full, plus ENVIRONMENT, UNIVERSE_MAP and SEARCH once per current version.
Use `hg_reference.py guide rubric` for the applicable shared rules. Task-folder
preflight is only for explicit task-folder mode; chat intake needs no task directory.
Apply `Evals/references/rules/rubric_sampling.md` when coverage uses sampling. Verifier,
all-failing and batch-result inputs are outside this stage.

## Run flow (rubric-flow-v2)

Follow `Evals/references/rules/rubric_flow_v2.md`. Right after intake, run
`python3 Evals/tools/hg_rubric_ledger.py plan` and use the mode it prints:
- Always run the code checks first: `python3 Evals/tools/hg_rubric_lint.py`.
- `FULL` (run 1): start two extra independent full reviewers (F2, F3) in the
  background, do your own full review including the scope checklist, run R1–R7 at
  Phase 5.5, combine every finding into one list (merge duplicates, do not vote),
  give a fix for every finding and check the fixes once (lint + R1–R7 on the
  candidate rubric), so the contributor gets all feedback at once.
- `DELTA` (run 2): rows that passed last time, and rows that copy a `(checked)` fix
  exactly, are locked and fail only on a provable factual error; anything else on
  them is a note for QM. Review edited, new and previously flagged rows fully,
  check recorded dismissal reasons, and run R1–R7 on those rows only.
- `UNCHANGED`: do not re-review; restate the previous verdict.
After saving the report, run `hg_rubric_ledger.py write` as `rubric_flow_v2.md` says.

## Evaluation

Read `Evals/references/rules/rubric_qc_examples.md` and apply its coverage,
destination, authorization and contradiction challenges in the existing ledger.
Use historical cases as calibration, preserving current sampling, atomicity
exceptions, Outcome-first categories and source-authority boundaries.

Apply `Evals/references/rules/prompt_rubric_reliability.md`. Verify the installed
package with `hg_eval_release.py snapshot rubric` and put its `eval_release`
object in the score record. Use current installed helpers, not historical task
copies. Authoring metadata cannot prove a fact or contradiction. Complete the
conditional absence evidence where applicable; use executable RANGE checks
for explicit acceptance bands. Include release fingerprints in the report.

1. **Bind the actual input.** Save supplied criteria with `hg_store_input.py save rubric`.
   Use `source:rubric` under INPUTS when retaining an original upload. Review the
   actual current array and all its fields; preserve its bytes and row numbering.
   Historical `5_Rubric.json` exports and proposal drafts are not automatically
   current inputs. If explicitly selected by the user, register them as input first.
2. **Establish acceptance.** Build the prompt/source requirement ledger before
   consulting the OE as a reference path. Apply `prompt-incorporation-v1`:
   unmentioned handbooks add no obligations; research facts remain evidence.
   Preserve source versions, persona visibility and actual output capabilities.
   Snowflake and Confluence are live under `service-availability-v1`, with
   unscoped reads (acl.md). Use local files and static SQL; do not
   execute SQL, replay workplace tools or launch model runs.
3. **Evaluate every criterion and the set.** Apply Eval 3's six review checks,
   six static QC dimensions and factual checks. Complete the format-4 scoring
   record in `Evals/references/rules/review_scoring.md`, including the mandatory
   `checks` ledger in `rubric_checks.md` and each row's `fact_review` under
   `rubric_factual_checks.md`. Test valid alternatives, plausible wrong answers,
   missing outcomes, restrictions and overlaps against the actual predicates.
   Preserve QC atomicity exceptions. Cover core/distinct outcomes directly;
   sample only repetitive, comparably important artifact items with controls and
   justified ordinary/edge selections. Complete the conditional sampling ledger;
   never sample the supplied rubric criteria themselves. Exact title
   subjects, affirmative framing, weights and supporting-field consistency remain
   mandatory. Read `Evals/Docs` (QC spec, rating form, Rubric Writing) as the
   authority and apply the Local Overrides table at the top of Eval 3:
   title-only self-containment, Major Overly Specific, Moderate Overly Broad,
   cascading-failure overlap groups, prohibition-only titles failing Negative
   Criteria, Major `non_agent_centric` for artifact-subject or tool-name titles, Category Balance failing only at zero Outcome, at most five spot
   checks per group plus a volume criterion, and the `predicted_all_fail` record
   (two or more rows force FAIL).
   A PASS label cannot override a source-derived factual mismatch.
   Unsupported facts remain unresolved; source selection and semantic judgments
   require evidence. No external model is required.
4. **Report.** Save `rubric-score`. Do not save the Markdown report until the
   deep recheck in step 5 is done; then save it through
   `hg_write_output.py rubric`. Copy the computed QC verdict, score, fractions and
   hashes. Give affected criteria, severity, evidence, practical grading impact
   and suggested fixes. Every suggested rewrite must itself pass this eval's
   rules and must not break any other row. Give a fix for every finding (never
   "no fix"), and check the fixes once before reporting: lint plus R1–R7 on the
   candidate rubric (`rubric_flow_v2.md`, "Fixes"). Mark each `(checked)` or
   `(revised after check)`.
   Report PASS, NON-FAIL or FAIL under the existing thresholds;
   incomplete evidence stays provisional unless an independent defect proves FAIL.
5. **Deep recheck, then stop.** Run Eval 3 Phase 5.5 with
   `Evals/references/rules/deep_recheck.md`. Skip the passes only when the review
   stopped as PARTIAL or BLOCKED for missing inputs; the report's
   `## Deep Recheck` section then says why.
   - Start passes R1–R7 at the same time with the subagent tool, one fresh
     subagent per pass, on this skill's model.
     Give each only the saved input paths under `Evals/task_inputs/` (never
     `reports/`), the workspace path, `Evals/SEARCH.md`, `Evals/references/persona/`,
     `common_errors.md` and `deep_recheck.md`, and its pass ID. Tell it to check
     only its pass's topic on every rubric row, return findings in the deep recheck
     finding format, never execute SQL, and never open `Evals/task_inputs/reports/`.
     Do not pass it the scoring record, your findings, your scores or your verdict. If a
     pass crashes, times out or returns no usable result, start a fresh subagent
     for that pass and repeat until it returns one.
   - Open every record each finding cites. Mark it CONFIRMED or REJECTED with a
     reason; the pass's word is not evidence.
   - Add confirmed findings to the scoring record as `issues`, `weight_reviews`
     changes or `predicted_all_fail` entries, save `rubric-score` again, and let
     the helper recompute the verdict under the existing thresholds and gates.
   - Save the report. It ends with `## Deep Recheck`, whose last part is the
     report's only verdict block, matching the recomputed record.

6. **Save the row ledger** with the checked fixes, exactly as `rubric_flow_v2.md`
   says: write `fixcheck/fix_status.json`, then `hg_rubric_ledger.py write --mode FULL`
   (or `--mode DELTA --keep-checked`). Put `## Fix List` directly under the report header. In FULL mode the report includes `## All Findings`;
   in DELTA mode it includes `## Changes Since Last Run`.

   End after evaluating this supplied version. Do not revise criteria, retry until
   PASS, emit replacement rubric JSON or run another stage to repair its inputs.

## Outputs

- Evaluation report: `Evals/task_inputs/reports/3_rubric.md`.
- Internal evidence/scoring record: `Evals/task_inputs/reports/drafts/rubric_score_record.json`.
- Row ledger for the next run: `Evals/task_inputs/reports/drafts/rubric_ledger.json`.

The scoring record is an audit ledger, not a rubric prefill. The `rubric-draft`,
`rubric-review` and `rubric-json` writer routes are retired. No CREATE record,
iteration loop or Ready for prefill field is part of the current workflow.
Keep suggested repairs separate from the QC grade; no repair is applied by this
skill. Preserve historical exports and supplied inputs. Verify writer receipts
before returning paths. Missing rubric input calls for input collection, not a
fabricated array or completed evaluation.

Use SEARCH's verified caches and `hg_search.py get-many --request <reads.json>
--compact` for already located records. Finish required pages, retain errors and
check source/dependency matches before reuse. Selected reads never prove global
absence. `hg_reference.py guide rubric --services <service> --tables <table>`
can combine the complete relevant reference views without duplicate reads.
