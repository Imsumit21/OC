---
name: prompt
description: "Audit a HarmonyGames V6 task prompt for assignment fit, grounded asks, persona/tool feasibility, task design and originality. Use for /prompt or a pre-run prompt quality review."
model: claude-opus-5-5
effort: xhigh
---

# Prompt quality

Be a **ruthlessly thorough, evidence-based grader**. Apply the **Ruthless
grading standard** in `Evals/WORKFLOW.md`: actively challenge acceptance,
substantiate findings, and preserve this stage's scope, evidence limits and
scoring rules.

**Task date first.** Before anything else, including other input questions, run
`python3 Evals/tools/hg_store_input.py list` and read `universe_intake`. Unless it
is `SELECTED`, ask only this and wait:
**Which date is this task on: Oct 1, 2025 (synth-cut) or Feb 14, 2026 (normal)?**
Save the answer with `python3 Evals/tools/hg_store_input.py universe "<answer>"`.
Never guess, infer or default the date; it selects the universe folder and clock
for every read (`Evals/INPUTS.md` **Task date — ask first**). A saved date is
reused without asking. Copy `report_line` from `universe_intake` (or
`hg_universe.py show`) into the verdict block as its `Clock:` line.

Before source checks or missing-input questions, follow `Evals/INPUTS.md` and
`WORKFLOW.md`'s **Save and reuse supplied inputs** contract. Run
`python3 Evals/tools/hg_store_input.py list`, then save every newly supplied
task input with that helper, including later follow-ups and uploaded files.
New versions replace the same input key; omitted inputs remain saved. Reload
relevant saved inputs across chats in this task workspace, ask only for what
this stage still needs, and never infer missing values. Do not reuse reports
or run evidence as current without checking the input versions.

Check `injection_intake` in the saved-input list. If SQL or an explicit
no-injection answer is not already supplied/saved, always ask:
**Injection SQL (optional): does this task use any? If yes, paste or attach it; if not, say no injection.**
Save other inputs, then wait for this answer before source-dependent evaluation.
Save “no injection” with `python3 Evals/tools/hg_store_input.py no-injection`;
reuse that choice across stages. A later SQL submission replaces it. See INPUTS.md.

Read `Evals/EXECUTION.md` for shared execution and reference routing. Resolve
this workspace once and use its helper paths. After saving inputs, read the
actual saved files needed by this stage, including optional SQL before base
searches; the input list alone is insufficient. Use `lookup` for complete ID
checks and `search-many` for related text queries under `Evals/SEARCH.md`.
Ordinary searches reuse existing indexes or scan directly; avoid cold index
builds for one-off searches and do not retry a locked cache. Preserve JSON stdout separately from
progress stderr, and keep one tracked background job for a long search.

Use `Evals/references/tools/catalog.json` for tool names and declared
parameters under `ENVIRONMENT.md`'s tool-catalog contract. Use the catalog for declared capabilities, not as proof of runtime behavior
or visibility. Tool exports are not SQL schemas. Apply the local-search limits
in `ENVIRONMENT.md` to unsupported runtime checks.
Use `Evals/references/persona/roster.json` and
`Evals/references/persona/acl.md` for existing identities and ACL rules.
Apply the rules as written under `ENVIRONMENT.md`; do not expand their scope
from the tool catalog or overwrite supplied assignment fields with inferred values.

Apply ENVIRONMENT.md's `service-availability-v1`: Snowflake and Confluence are
live and their reads are unscoped (acl.md, QC Rating Form V12); assess actual
task-specific restrictions from evidence.

Read the applicable WORKFLOW sections routed by `EXECUTION.md`. A bare `/prompt` asks in the chat response for
only the missing CB inputs listed below, then waits for the user to paste or
attach them. Reuse inputs already supplied for this review. Do not ask for a
task folder or run preflight during chat input collection.

Only when the user explicitly chooses a task folder, read its stage inputs and
run `python3 Evals/tools/hg_preflight.py "<task>" --stage prompt --format json`.
Read **all** of `Evals/1_Prompt_Eval.md` and its mandatory references; create
every required TODO before judging the prompt.

Read `Evals/references/README.md` for bundled references. No external guide or sample folder is required. For SQL-related checks, follow `Evals/references/schema/README.md`; the bundled injection schema is an unverified snapshot.

## Inputs

Required CB inputs: exact task prompt and all five assignment fields:
**persona, business function, competency, task skill, and horizon**. Every task
has all five assigned. Reuse the latest saved values; save partial submissions
and ask for any missing or ambiguous fields, then wait before evaluating or
issuing a report/verdict. Never infer assignment values from the SQL or prompt.

Additional inputs: optional injection SQL, applicable error/async configuration
and dynamic context, plus reference files used by the prompt, if any. Read the
supplied inputs verbatim. Read base records from the local service exports; load the catalog,
schema and persona authorities locally. Use QC examples only for calibration
and originality checks. Do not rewrite the prompt while auditing its voice.

Injection SQL is optional. Follow INPUTS.md's question-and-save contract: ask
until SQL or an explicit no-injection answer is supplied/saved, then reuse the
answer. Save partial inputs and wait before source-dependent evaluation;
omission alone is not a no-injection answer or a reason to issue a verdict.

Follow `WORKFLOW.md`'s reference-file contract, including uploaded Word
`.docx` and PowerPoint `.pptx` sources. Distinguish source attachments from
Agent deliverables that the prompt asks to create (for example, `report.html`);
inspect actual content and relevant visuals under that contract. In the input request include:
**Please also attach any reference files used by the prompt, if any.** Reuse
files already supplied for this review. Inspect their actual contents, map
prompt references, and record Agent availability and file versions. A file
available only to the evaluator does not establish an Agent-visible source.

Run `python3 Evals/tools/hg_reference.py guide prompt` for the applicable
shared WORKFLOW sections and original scoring groups together. This satisfies
those reads; do not separately dump WORKFLOW.md or repeat hg_context. Read the
selected numbered Eval in full and its remaining conditional references. Use
`hg_reference.py routes <service> ...` for known files/array pointers and
`hg_records.py --request <checks.json>` for related exact record checks across
collections/fields in one pass. See SEARCH.md for request format and limits.

## Evaluate

**Injection gate first (Eval 1 STEP 0.5).** Run
`python3 Evals/tools/hg_injection_gate.py`. On `STALE` or `NEVER_REVIEWED`, run
Eval 0 (the /injection skill's procedure) on the saved SQL before Phase 1, save
its report and manifest entry, then continue. On `CURRENT`, reuse the recorded
result. Put the state, reviewed hash and Eval 0 verdict in the report's
`### Injection Gate` section.

Read `Evals/references/rules/prompt_qc_examples.md` and apply its relevant
challenges in the existing phases. Historical cases are calibration only;
the prompt-only corpus has no rubric/OE/run inputs and cannot prove task facts.

Apply `Evals/references/rules/prompt_rubric_reliability.md` from the shared
`task-quality-v1` release. Verify it with `hg_eval_release.py snapshot prompt`;
do not run copied historical task-folder helpers. Bind `prompt-source-checks-v2`
checks with `hg_prompt_checks.py start` and complete the format-2 premise and UGT
record while reviewing the existing phases. Separate asserted existing facts
from requested new outputs and hypotheses. Authoring metadata is a source lead,
never proof; absence claims need applicable surface coverage and positive controls.

Before every scored Unique Ground Truth verdict, apply Eval 1 §2.1 and fill
`unique_ground_truth`, including when UGT passes inside an overall FAIL. Test the
strongest plausible alternative, account for every explicit option, and compare
concrete decisions, writes, destinations and contents. Apply the five checks to
each material difference: newer source, authority, source identity, scope and
same material result. A later applicable update for the same issue and scope can
resolve an earlier statement without explicitly announcing replacement; respect
cutoff dates and prompt-specified source priority, and retain unaffected requirements.
A leading reading, the same destination, or resolving only one part of the task
does not prove uniqueness. The one exception is Eval 1 §2.1's both-fair figure
(local override 2026-10-17): only one reported figure differs, both values are
on persona-visible records, none of the five checks settles it, and decision,
writes and destinations are the same. Record it as BOTH_FAIR_FIGURE; every other
fork keeps the rules here. Cite the evidence that actually excludes an alternative
or the authority that authorizes its objective acceptance boundary; a list
of candidate calls does not itself delegate interchangeable final decisions.
Challenge strawman alternatives, irrelevant citations and unsupported delegation.
A localized supported material difference can establish FAIL without completing
every other task output. The schema checks binding and consistency, not semantic
truth; finish the source-based challenge before declaring it complete.

Follow `WORKFLOW.md`'s **Stage ownership and evidence reuse** contract. Never
request or load Oracle Events, rubrics, Agent/baseline runs or verifier results
for prompt interpretation. Decide allowed outcomes from the actual request and
authorized sources under `WORKFLOW.md`; no run-count or convergence prerequisite applies.

Build a requirement ledger covering every direct and authorized-source ask,
including destinations, content, exclusions, and the final answer to the user.
For each requirement record:

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|

Apply `WORKFLOW.md`'s **Output capability and failure attribution** contract to
every requested deliverable: content creation, actual format generation/export
and delivery. Confirmed unsupported paths fail feasibility; unknown support
remains unresolved. Catalog MIME fields and evaluator-local tools do not prove
the task Agent can create a PDF or another requested format.

Execute all structure/persona, depth, feasibility and final-scoring phases.
Keep these distinctions explicit:

- Persona, business function, competency, task skill, and horizon are five
  separate required fields. Record their exact supplied values and sources;
  use the assigned horizon to select applicable design guidance. Never invent
  an assignment or infer a Finance persona.
- Apply `WORKFLOW.md`'s `horizon-tiers-v1`: Normal Horizon is 50–100 tool
  calls and Long Horizon 100–500+, measured at Trajectory - Task Type & Horizon.
  `/prompt` does not estimate or score a call count and requests no trajectory.
- Apply the Local Overrides table at the top of Eval 1 and read `Evals/Docs`
  (QC spec, rating form, Prompt Writing, Overall Task Flow) as the authority.
- Prompt-directed reference files or environment records can carry requirements only
  if they satisfy the
  Eval's incorporation/discoverability rules; merely related text is not an ask.
  Apply `WORKFLOW.md`'s `prompt-incorporation-v1` contract: no unmentioned
  handbook/policy can add grading obligations. Cite the prompt passage that
  incorporates each instruction source; research facts do not import its rules.
  Reassess older requirement ledgers under this contract before reuse.
- A requested new document or issue is not a phantom. An asserted existing
  source needs evidence and a real discovery path.
- Read scope is not write permission. Raw numerical truth is not necessarily
  visible at the precision exposed by the cataloged tools.
- Necessary calls, genuine service use, meaningful writes and friction are
  prompt design requirements; retain the existing thresholds. They do not
  establish observed hardness, which belongs to `/hardness`. Padding and
  arbitrary extra calls cannot satisfy the design gate.
- Authoring targets, assigned horizon tiers, prompt rejection floors, and
  empirical QC floors are different. Read their current definitions; do not
  substitute one for another.
- Apply the fixed universe clock and contextual date-resolution rule. Relative
  wording such as Friday, today or yesterday is allowed when it resolves clearly.
  In persona-written text, today is Saturday, February 14, 2026 and yesterday
  is February 13 on a Feb 14 task; on an Oct 1 task, today is Wednesday,
  October 1, 2025 and yesterday is September 30 (clock 2025-10-01 00:00 PT).
  The February 11, 2026 shutdown premise check applies to Feb 14 tasks only; on
  an Oct 1 task, check premises against what exists by 2025-09-30 23:59:59 PT
  (people who left before then, such as Victor, are still gone).
  Flag only material ambiguity or source/clock contradictions; do not require
  explicit dates merely because the prompt uses relative wording.

A current matching `injection-static-v2` PASS / COMPLETE can supply its static
integrity checks under the reuse contract. Do not repeat the entire SQL audit.
Assess task-required anchors, incorporation, paths, assigned-persona feasibility
and configuration here. Without eligible upstream evidence, inspect needed
source facts directly; do not require an injection report as an extra input.
Report new blocking contradictions and invalidate affected reused checks.

Check naturalness, voice, clarity, truthfulness, feasibility, anti-sample-copying,
investigation plus action, unique/gradable ground truth, and all named hard gates.
Do not pass unverified asks because the request sounds plausible.

## Report

Save the check record first, run the deep recheck below, then save the report
once with
`python3 Evals/tools/hg_write_output.py prompt --source "<completed-report.md>"`.
Follow `WORKFLOW.md`'s deterministic output-writing contract; return the
download path only after the writer succeeds.

Before a scored report or any numerically scored UGT dimension in an otherwise
unscored report, save the format-2 internal record using
`hg_write_output.py prompt-checks --source <record.json>`. Include its prompt,
context and record hashes, and the current Eval version/release hash in the
report. Run `python3 Evals/tools/hg_prompt_checks.py render-ugt` to validate the
saved record and generate its required comparison section (an optional final
record path selects another record). Include that section verbatim exactly once,
visibly outside code fences/comments, and keep every UGT score/verdict consistent
with it. Aggregate FAIL or no-score status does not bypass a scored UGT review.
The writer enforces these bindings and preserves genuine no-score partial reports.
This adds no contributor input.

The report path below is fixed relative to the repository root for this task.
A rerun replaces this stage's report; do not add a task or review-ID subfolder.
Follow `WORKFLOW.md` for shared metadata and preservation of historical folders.

Use the standard verdict block in `Evals/WORKFLOW.md` in the report and chat:
`### FINAL VERDICT: PASS / NON-FAIL / FAIL`, `Execution status`, `Next action`,
and `Evidence limits`. Include a separate `Score` line only when the stage's
numeric score is supported. Preserve existing scoring thresholds. Never leave
an issued verdict blank: required unresolved checks with no demonstrated failure
use NON-FAIL and PARTIAL/BLOCKED, without a numeric score or gate clearance.
A demonstrated failure remains FAIL; PASS requires COMPLETE. The writer
validates the exact block under `WORKFLOW.md` before saving.

Write `Evals/task_inputs/reports/1_prompt.md`, retaining Eval 1's phase tables, scores and
overall PASS at 5, NON-FAIL at 3–4 and FAIL at 1–2 thresholds, with the actual
score on its own `Score:` line. UGT itself permits only PASS 5 or FAIL 1–2;
missing required evidence has no numeric score. Include the
requirement ledger, every source-backed failure and minimum fix, and unresolved
assignment/evidence issues. Do not invent a numeric grade for an unexecuted
check.

## Deep recheck

Before the report is saved, run Eval 1 Phase 5 with
`Evals/references/rules/deep_recheck.md`. Skip the passes only when the review
stopped as PARTIAL or BLOCKED for missing inputs; the report's `## Deep Recheck`
section then says why.

1. Start passes P1–P4 at the same time with the subagent tool, one fresh
   subagent per pass, on this skill's model.
   Give each only the saved input paths under `Evals/task_inputs/` (never
   `reports/`), the workspace path, `Evals/SEARCH.md`, `Evals/references/persona/`,
   `common_errors.md` and `deep_recheck.md`, and its pass ID. Tell it to check
   only its pass's topic on every prompt sentence, return findings in the deep recheck
   finding format, never execute SQL, and never open `Evals/task_inputs/reports/`.
   Do not pass it the check record, your findings, your scores or your verdict. If a
   pass crashes, times out or returns no usable result, start a fresh subagent
   for that pass and repeat until it returns one.
2. Open every record each finding cites. Mark it CONFIRMED or REJECTED with a
   reason; the pass's word is not evidence. Reject a UGT finding only by quoting
   a prompt sentence or persona-visible record that rules out Reading B. A fork
   that meets every Eval 1 §2.1 both-fair figure condition is recorded as
   BOTH_FAIR_FIGURE, not rejected. Record `PLATFORM:` findings without scoring them.
3. Add confirmed findings to the check record: Truthfulness as premise checks,
   UGT in `unique_ground_truth`, anything else in `other_failures`. Rescore and
   save with `prompt-checks`. A confirmed fail-level finding makes the verdict FAIL.
4. Check every proposed rewrite (deep_recheck.md main-session step 5): each
   value, id and label quoted from a record, every covered item named, no new
   lock-in. Replace a rewrite you cannot verify with a plain description.
5. Save the report. It ends with `## Deep Recheck` with the fork list (every
   fork, with the record that settles it, what is missing, or its two both-fair
   values); its last part is
   the report's only verdict block, matching the recomputed record.

Then return the verdict/status, blockers, and report path.

Search helpers under `Evals/SEARCH.md` automatically validate matching bundled
indexes on first use and reuse complete raw-record results across supported
services when their request/source/manifest/helper versions match. No additional
user command is needed. Cache hits supply source evidence only; apply every
current input, SQL, persona/ACL, evidence and grading requirement as written.

For several already located records, use
`python3 Evals/tools/hg_search.py get-many --request <reads.json> --compact`
with SEARCH's request format. Finish required pages and retain each item's
errors; selected reads do not prove collection-wide absence or full history.
Targeted batch queries use verified offsets when efficient; broad queries keep
one shared scan. These routes preserve every required grading check.

For already known source services/schema tables, combine the complete reference
views with `hg_reference.py guide prompt --services <service> ... --tables <table> ...`;
omit unneeded flags and avoid repeating the corresponding standalone reads.
Under SEARCH.md, individual record checks survive display-ID/order changes when
their evidence scope and dependencies match. `lookup` automatically uses a
verified prepared identity index where available, with complete-scan fallback.
These helpers reuse evidence only; complete all current grading checks.
