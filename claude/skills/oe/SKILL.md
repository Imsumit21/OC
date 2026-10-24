---
name: oe
description: "Evaluate supplied Oracle Events / MVP path for complete task discovery, dependencies and actions, and accurate tools, parameters, expected data and a feasible supplied path. Use /oe or /oe audit; this replaces golden-answer evaluation."
model: claude-opus-5-5
effort: xhigh
---

# Evaluate Oracle Events

Follow `Evals/INPUTS.md`: save supplied OEs under `oe` (one complete original
upload can use `source:oe`), list saved inputs and read their actual contents.
Required: OEs, exact prompt, assignment/persona and applicable prompt references.
Resolve optional injection SQL using saved SQL or an explicit no-injection
decision; ask for missing inputs together and save partial submissions first.
Do not convert a golden answer into OEs or request a golden, rubric or model run.

Read `Evals/EXECUTION.md`, `Evals/2_Oracle_Events_Eval.md` in full, ENVIRONMENT,
UNIVERSE_MAP and SEARCH once per current version. Use `hg_reference.py guide oe`
and `Evals/references/rules/oracle_events.md` for scoring and record mechanics.

1. Derive the critical path from prompt/incorporated instructions and sources.
   Review all supplied steps and any missing discovery, dependencies or writes.
   OEs describe Action, Information, Tool/Service, Parameters and Expected Data;
   they do not describe what the final response should say. Those five are
   content, not labelled fields: plain sentences are fully valid, and naming the
   service or record in words ("the release channel in Slack") needs no function
   name or raw ID. Judge content, not writing style; readability is advice only
   and never changes a score. Separately, check Format & Standardization (Eval
   2.7): no details/Expected line, arrow chain, several actions in one OE, JSON,
   or no number/service. Record each in `format_review`; any one is NON-FAIL 3,
   never FAIL. Write recommended fixes sentence-first: goal, where to look, then
   an "Expected:" line with the actual values and any trap.
2. Verify each existing step against primary universe data and the actual tool
   catalog: correct service, operation, names/IDs, parameters, expected data,
   timing and feasible dependency chain. Inspect relevant attachments and
   preserve unresolved evidence. Do not execute SQL or workplace writes.
   Build the internal `path_review`: validate tool contracts, source values,
   upstream/downstream bindings and dependency order with `hg_oe_review.py`.
   Verify data/persona access, capability, preconditions and actual completion.
   A broken OE does not prove the task impossible. `/prompt` owns task design
   and overall feasibility; only a supported task-wide blocker merits a separate
   prompt follow-up diagnostic. Never change its score/report or rerun it here.
   Use matching read-only runtime evidence only when needed and available;
   unresolved evidence stays unresolved. Static evidence can suffice.
   Apply relevant examples from `Evals/references/rules/oracle_events_qc_examples.md`:
   material search defaults, full requested scope/joins, actual write completion,
   offered branches, action ownership, ID namespaces and time/state consistency.
   Historical QC flags are examples to investigate, not current source evidence.
3. Map verification Outcome first. Contact lookup can be proved by the correctly
   addressed sent email; do not add Process merely because an OE is a read.
   Use only Outcome and Process as rubric category names; do not introduce
   numbered subtypes. A reference path does not prohibit other task-valid paths. No rubric authoring
   or rubric PASS prerequisite is introduced.
4. Start a bound record with `hg_oe_review.py start`, complete its source-linked
   step, coverage and path checks (format 2 / oracle-events-v2) and save
   `oe-review`. Save `oe` with `hg_write_output.py` only after the deep recheck
   in step 5. Following the Oracle Events guideline, a missing
   critical step or a wrong existing step FAILs (2); minor, non-action and
   final-response defects are NON-FAIL 3; a clean set is PASS 5. The overall
   result is the minimum of completeness and accuracy. Read Eval 2's Local
   Overrides and `Evals/Docs/Original_Conference_Guidelines_-_Oracle_Events.pdf`.
   Missing reviewer evidence is unscored provisional NON-FAIL, not inaccuracy.
   Include the computed Path feasibility, Task solvability and Prompt follow-up
   diagnostics; these are not a third QC score.
5. **Deep recheck.** Run Eval 2 Phase 5 with
   `Evals/references/rules/deep_recheck.md`. Skip the passes only when the review
   stopped as PARTIAL or BLOCKED for missing inputs; the report's
   `## Deep Recheck` section then says why.
   - Start passes O1 (Accuracy), O2 (Completeness) and O3 (Open-instruction
     inventory) at the same time with the subagent tool, one fresh subagent per
     pass, on this skill's model. Do not give O3 `08_Oracle_Events.md` or any
     OE text.
     Give each only the saved input paths under `Evals/task_inputs/` (never
     `reports/`), the workspace path, `Evals/SEARCH.md`, `Evals/references/persona/`,
     `common_errors.md` and `deep_recheck.md`, and its pass ID. Tell it to check
     only its pass's topic on every oracle event, return findings in the deep recheck
     finding format, never execute SQL, and never open `Evals/task_inputs/reports/`.
     Do not pass it the OE record, your findings, your scores or your verdict. If a
     pass crashes, times out or returns no usable result, start a fresh subagent
     for that pass and repeat until it returns one.
   - Open every record each finding cites. Mark it CONFIRMED or REJECTED with a
     reason; the pass's word is not evidence. A different valid route is not a
     missing step. Match each O3 item to the OE that reads both sides and makes
     the fix; a confirmed item with no OE is `MISSING` and is never optional.
   - Put confirmed findings into the record: a wrong field is that step's
     `INACCURATE` (or `MINOR` when harmless), a missing step is a `coverage`
     entry `MISSING`, a non-action or final-response event goes to its segment,
     a shape defect goes to `format_review`. Save `oe-review` again.
   - Check every OE under Recommended Fixes (deep_recheck.md main-session step
     5): each value, branch, window and label quoted from a record, every
     covered item named. Replace one you cannot verify with a plain description.
   - Save the report. It ends with `## Deep Recheck` with the O3 inventory; its
     last part is the report's only verdict block, matching the recomputed record.
6. Return the saved report and suggested corrections; preserve supplied OEs.
   This command evaluates only. It does not rewrite OEs or produce a final answer.

Report: `Evals/task_inputs/reports/2_oe.md`.
Internal record: `Evals/task_inputs/reports/drafts/oe_review_record.json`.
The record verifies hashes, coverage declarations and scoring consistency;
semantic correctness and source relevance still require evidence review.
