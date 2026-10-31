# PROMPT QUALITY EVALUATOR - Original Conference (HarmonyGames)

Be a **ruthlessly thorough, evidence-based grader** of prompt quality. Actively
challenge task premises, clarity, feasibility and design against this Eval under
the [Ruthless grading standard](WORKFLOW.md#ruthless-grading-standard).

Follow [INPUTS.md](INPUTS.md)'s optional injection question in every intake.
Ask until SQL or an explicit no-injection answer is supplied/saved; reuse the
answer and wait for unresolved intake before source-dependent evaluation.

Use `python3 Evals/tools/hg_reference.py guide prompt` for the applicable
shared WORKFLOW sections and scoring groups; this replaces duplicate shared
reads, not this Eval or its required evidence. Use the record and schema views
in [SEARCH.md](SEARCH.md) for related checks.

Use [EXECUTION.md](EXECUTION.md) for input-first execution, applicable shared
reference sections and efficient search. Read this Eval in full; every required
phase and evidence check still applies. The guide above already includes the
canonical stage scoring groups; do not load them a second time.

**Fixed report path:** `Evals/task_inputs/reports/1_prompt.md` (relative to the repository
root). Use this path for both chat and task-folder reviews. A rerun replaces
this stage's report; do not add a task or review-ID subfolder. Follow
`WORKFLOW.md` for reporting and shared metadata. Save through
`python3 Evals/tools/hg_write_output.py prompt --source "<completed-report.md>"`
and return the path only after the writer verifies the saved file.


**Tool reference:** Use `Evals/references/tools/catalog.json` under the
`ENVIRONMENT.md` tool-catalog contract; the exports are not SQL schemas or
proof of live service availability.

**Input persistence:** Follow `WORKFLOW.md`'s **Save and reuse supplied inputs**
contract and `INPUTS.md` before requesting inputs or checking source coverage. Save every
newly supplied task input immediately with `Evals/tools/hg_store_input.py`;
new versions replace that input's saved entry. Reload the saved inventory and
reuse relevant inputs without expanding this eval's input scope.

**Environment prerequisite:** Read [ENVIRONMENT.md](ENVIRONMENT.md),
[WORKFLOW.md](WORKFLOW.md), and [UNIVERSE_MAP.md](UNIVERSE_MAP.md). Read base
records from the three sibling HarmonyGames folders extracted from
`hg4-2026-08-31.zip` (2026-09-28 download). Use `Evals/tools/hg_search.py` for bounded local searches
and JSON-pointer reads. Cite file path, record ID or JSON pointer, and value.
Apply the unchanged persona ACL to source metadata; local file access alone
does not establish Agent visibility. SQL is an optional static overlay and is
never executed. Historical trajectories establish what a run actually saw.


## Overview

Review the prompt as a work request: its assignment fit, design requirements,
clarity, factual premises, solvability and authorized outcomes. Cover every ask;
use source verification or current evidence under `WORKFLOW.md`'s **Stage ownership
and evidence reuse** contract. Reuse does not reduce the required coverage.

Apply [Prompt QC examples](references/rules/prompt_qc_examples.md) within the
existing phases: challenge material ambiguity, approval/action ownership,
identity and source conflicts, premises and actual tool effects. Use only the
prompt examples for calibration; historical labels are not current task evidence.
Do not load historical rubric/OE/run artifacts to interpret the current prompt.

A prompt is a natural work request written from a HarmonyGames persona's perspective to an AI agent. Your job is to tear it apart across every QC dimension, verify every single factual claim against the universe data, and confirm that the task is 100% feasible and solvable with the available tools and data.

**CRITICAL PRINCIPLES:**
- Every claim, every entity, every relationship, every implied fact in the prompt MUST be verified against the actual universe data. No assumptions. No shortcuts.
- **Feasibility is king.** If the data doesn't exist in the universe to answer what the prompt asks, the task is broken. You MUST deep-explore the universe data to confirm every ask is answerable. Do not trust summaries - inspect the local records and full source contents.
- **Numeric observability is part of feasibility.** A value existing in raw universe JSON is insufficient when the cataloged tool renders it at lower precision, truncates it, or omits the inputs required to derive it. Exact-value and formatting asks must be reachable through the same tool-visible environment the Agent receives.
- **Pre-run input boundary.** Do not request or load a Oracle Events, rubrics,
  Agent/baseline trajectories or verifier results to decide prompt quality.
  Determine authorized outcomes from the prompt, authorized sources under `WORKFLOW.md`
  and assignment. Later answers, criteria and run outcomes cannot define them.
- **Design versus hardness.** The prompt's necessary-work thresholds are
  design checks. Only `/hardness` assigns Too easy/Easy/Hard/Really hard, directly
  from Opus or through Haiku-to-Opus prediction. A prompt score or call estimate
  does not substitute for that review.
- **Persona ACL feasibility is a STRONG HARD GATE.** Every prompt ask must be feasible under the assigned taxonomy persona's exact key/email binding from `Evals/references/persona/roster.json`, using the read-scope semantics in `Evals/references/persona/acl.md` (derive the scoped-service set live from its Access matrix; do not hardcode it). A single persona-scoped read that the assigned persona cannot reach — with no affirmative-denial outcome and no authorized unscoped alternate — is a **standalone FAIL**. It cannot be waived, offset by other passing dimensions, or excused as a "minor/secondary" ask, and author god-mode visibility never satisfies it.
- When in doubt, dig deeper. Read more files. Search more broadly. The cost of missing a factual error or a feasibility gap is far greater than the cost of spending extra time exploring.
- **The Docs are the authority.** `Evals/Docs/` holds the QC spec, the QC rating form and the project guidelines. Departures are listed in the local-override table below and nowhere else.

---

## Local Overrides (2026-09-26)

These user-approved decisions supersede the Docs where they conflict.

| Topic | Docs say | This Eval applies |
|---|---|---|
| Relative dates | Universe and Tools and Prompt Writing: "write dates absolutely"; relative dates are errors | Relative dates are **allowed**. Only material ambiguity or a temporal contradiction is a defect (Phase 2.8). |
| Clock | QC form text says February 28, 2026 | The task date's clock: **2026-02-14 00:00 UTC** (Universe and Tools) for Feb 14 tasks, **2025-10-01 00:00 PT (07:00 UTC)** for Oct 1 tasks (ENVIRONMENT.md **Task date and universe**). |
| Competency and Task Skill | QC form and Overall Task Flow: Non-Fail only | **Hard FAIL** on a clear mismatch or a missing assigned skill (Phase 1.5). |
| Alignment with Today's Date | QC form: Non-Fail only | A material temporal contradiction can **FAIL** (Phase 2.8). |
| Feasibility | QC form: Non-Fail for an impractical secondary request | **No middle band.** Any explicit ask that cannot be fully fulfilled fails. |
| Explicit Tool Mention | QC form: Non-Fail for naming an MCP server or calling a system a "tool" | **Pass/fail.** Naming a tool, parameter or MCP server, or calling a system a tool, fails (Prompt Writing checklist). |
| Tool-call count | Former prompt gate of more than 15 necessary calls | **Removed** (2026-09-26 update). Call counts belong to Trajectory - Task Type & Horizon (Normal 50–100, Long 100–500+). |
| Cross-service coherence | — | Follows the QC form: any inconsistency in the data the task touches fails, one minor inconsistency is Non-Fail, except that lifecycle and sum mismatches always fail (Phase 3.2). |
| Common errors checklist (2026-10-04) | — | `references/rules/common_errors.md` is adopted: each of two services must change a graded fact (2.4), an unneeded opaque ID or exact timestamp fails (2.7), fiscal periods are tight identifiers (2.3), UGT resolution needs a persona-visible quote (2.1), and the deep recheck in `references/rules/deep_recheck.md` runs before the report is saved (Phase 5). |
| Contrived voice (2026-10-05) | QC form: a somewhat contrived prompt whose situation is still natural is Non-Fail | **Fail.** A spec-like or polished, LLM-sounding draft fails even when the situation itself is real (Phases 1.2 and 2.7). |
| One loose factual slip (2026-10-05) | QC form: exactly one harmless loose descriptor is Non-Fail | **Fail.** One wrong loose descriptor fails Truthfulness (Phase 2.3). |
| Injection gate (2026-10-09) | — | Before Phase 1, `hg_injection_gate.py` checks that the saved SQL is the version /injection last reviewed. A changed or never-reviewed SQL gets Eval 0 run on it first (STEP 0.5). |
| Deep recheck revision (2026-10-09) | — | P1 computes each reading at its edge values and reports every fork once, with the record that settles it or what is missing. P2 scores hidden records and broken derived columns as coherence and applies one date-slip severity rule. A UGT finding is rejected only on a quoted record. Known platform defects (FD-2880, FD-3785, Slack paste artifacts) are tagged, not scored. Proposed rewrites are verified before the report is saved. |
| Personas | Universe and Tools: 19 staff personas | The **17** selectable personas in `Evals/references/persona/roster.json`. |
| Typing (2026-10-17) | Prompt Writing: reads like fast, unproofread typing | Clean typing is not a defect; staged typos, made-up emoji or broken punctuation fail Contrived. |
| Riddles (2026-10-17) | QC form: constraint-laden riddles are not contrived | A riddle or hint aimed at the trap fails Contrived. Naming the symptom is fine. |
| UGT both-fair figure (2026-10-17) | QC form: two correct answers fail even with a leading interpretation | PASS when only one reported figure differs, both values are on persona-visible records, nothing ranks them and the rubric accepts either. All other forks unchanged. |

---

## STEP 0 (HARD GATE - MANDATORY): Create TODO List First

Before ANY evaluation, create a comprehensive TODO list. **Do NOT proceed without this.**


```
TODO:
- [ ] Intake: Load the exact prompt and all five required assignment fields — persona, business function, competency, task skill, and horizon; save supplied details and collect missing/ambiguous values before evaluation
- [ ] STEP 0.5: Injection gate - run `python3 Evals/tools/hg_injection_gate.py`; on STALE or NEVER_REVIEWED run Eval 0 on the saved SQL before Phase 1
- [ ] Phase 0.1: Read Evals/Docs (QC spec, rating form, Prompt Writing, Overall Task Flow, Universe and Tools, Persona ACL Policy) and the relevant Evals/references/tools/catalog.json definitions (13 service catalogs plus the gateway tool)
- [ ] Phase 0.2: DO VERY DEEP EXPLORATION OF UNIVERSE DATA - This is critical for feasibility, truthfulness, and data existence checks later
- [ ] Phase 0.3: Calibrate against the Example Task in Evals/Docs - Understand what a good prompt looks like
- [ ] Phase 1.1: Persona Coherence - Verify supplied assignment, the bundled roster and local records
  - [ ] HARD GATE: Persona ACL Identity & Feasibility - exact assigned roster match and supported access; AMV dropdown does not override identity; no later runner/verifier output required
- [ ] Phase 1.2: Naturalness & Voice - Anti-pattern detection
  - [ ] AI-Text / LLM-Sounding Check - document formatting, enumerated specs, staged errors; scored under Contrived / Unnatural
- [ ] Phase 1.3: Structural Anti-Patterns - Command list, bolt-on, pre-solving, tool mention (including MCP server names and "the X tool")
- [ ] Phase 1.4: Prompt Diversity - Is this meaningfully different from "investigate + post one Slack message"?
- [ ] Phase 1.5: Assignment & Complexity Dimensions
  - [ ] HARD GATE: Assigned Competency — scenario and prompt fall inside the assigned competency
  - [ ] HARD GATE: Assigned Task Skill — the assigned primary skill is clearly present (stacking extras is fine)
  - [ ] HARD GATE: Complexity Dimensions — at least one of Ambiguity / Dynamic Change / Multi-Source is load-bearing; record which
  - [ ] HARD GATE: Data Seeding — operating details live in the environment, not a long recipe prompt
- [ ] Phase 2.1: Unique Ground Truth - Ambiguity analysis
  - [ ] HARD GATE: End-State Divergence - Compare concrete decisions, writes and contents; supported, materially incompatible required outcomes with no resolving authority → FAIL UGT (except a both-fair figure, which passes as BOTH_FAIR_FIGURE)
  - [ ] HARD GATE (T11): UGT Precision Guardrail - Complete and report the two-reading table before every scored UGT verdict, including PASS within an overall FAIL; test the strongest plausible alternative and account for every explicit option
  - [ ] Semantic challenge - Verify that cited passages resolve the actual difference; reject strawman alternatives, irrelevant citations and option lists mislabeled as authorized alternatives
  - [ ] Report contract - Save the structured comparison and include the generated UGT section verbatim; source-authorized alternatives and immaterial wording differences do not fail
  - [ ] Input boundary - Use prompt/source authority; no later rubric, OE or run dependency
- [ ] Phase 2.2: Feasibility - Tool capability + Data existence + Dimensional feasibility verification
  - [ ] Current service availability - apply `service-availability-v1` in ENVIRONMENT.md: Snowflake and Confluence are live; verify the required cataloged operation and data. Neither a service reference nor the older ACL omission is a FAIL or blocker. Assess concrete task-specific restrictions separately.
  - [ ] HARD GATE (T10): Dimensional Feasibility - For every per-X breakdown the prompt asks for, confirm the universe data carries that dimension field; missing field → FAIL Feasibility
  - [ ] HARD GATE: Numeric Observability - For every exact value, precision, rounding, or derived-number ask, verify the required value and inputs survive the cataloged tool path at the requested precision
  - [ ] STRONG HARD GATE: Persona-Scoped Read Feasibility & Ask-Level ACL Violation - Derive the scoped-service set live from the `Evals/references/persona/acl.md` access matrix (do not hardcode); confirm every required scoped-service read is visible to the assigned persona, and flag any prompt ask that directs the persona to read scoped data outside their view (unless affirmative-denial or authorized alternate). Any unreachable required scoped read = standalone FAIL, non-waivable
- [ ] Phase 2.3: Truthfulness - EXHAUSTIVE universe data verification (CRITICAL)
  - [ ] HARD GATE: Phantom Tight-Identifier Search - Verify every tight identifier against local records, SQL and applicable attachments; confirmed missing asserted sources fail, incomplete access remains unverified
  - [ ] HARD GATE: State-Premise Verification - Extract every declarative claim about current state (still no reply, hasn't been merged, rolling window, I own/approve this, business as usual after the Feb 11 shutdown on a Feb 14 task, a departed person still acting, anything that does not exist yet on an Oct 1 task) and verify against universe; contradicted premise = Major FAIL
- [ ] Phase 2.4: Cross-Service Requirement - Service mapping
- [ ] Phase 2.5: Investigation + Action - Read/Write balance
  - [ ] Complexity Hygiene - blocked/denied/repeated calls and set_acting_user environment configuration are not necessary work; no call-count estimate is scored at this stage
- [ ] Phase 2.6: Clarity & Specificity - Interpretation analysis
  - [ ] HARD GATE: Write-Action Divergence - Enumerate write action(s) under each reasonable reading; different write actions (or write vs no-write / act vs defer) → FAIL Clarity (Action Decision Ambiguity)
  - [ ] HARD GATE: Delegation Clarity - Scan for "I'll [verb]" statements; if ambiguous delegation vs self-action → FAIL (Action Decision Ambiguity)
- [ ] Phase 2.7: Contrived vs Natural Difficulty - Pattern analysis
  - [ ] HARD GATE: Spec-Sheet Register Escalation - 2+ register triggers (enumerated deliverable contents, preservation/format rules, prescribed reply format, contents-driven length) escalates the soft over-stacking flag to a Contrived FAIL
  - [ ] Trap hint or riddle, hidden destination the persona would know, audit-form wording, long if-chains - each fails Contrived on its own (2026-10-17)
- [ ] Phase 2.8: Alignment with Today's Date - Resolve explicit or relative references using context and the task's fixed date/time (2026-02-14 00:00 UTC or 2025-10-01 00:00 PT); flag only material ambiguity or contradiction, never relative wording alone
- [ ] Phase 2.9: Sample Similarity / Originality - Compare candidate against explicitly supplied samples; N/A when none are supplied
  - [ ] HARD GATE: Sample-Clone Detection - Fingerprint scenario/persona/entities/asks/services/writes/phrasing vs each sample; a clone or light paraphrase of any single sample = FAIL (non-waivable)
- [ ] Phase 3.1: Data Existence - Per-entity verification in universe files
- [ ] Phase 3.2: Cross-Service Coherence (QC form) - Per-artifact review of the data the task touches; any inconsistency fails, one minor inconsistency is Non-Fail; reuse matching injection checks where eligible
- [ ] Phase 4.1: Final Scoring Table - Per bundled scoring.json dimensions
- [ ] Phase 4.2: Verdict + Issues + Recommendations
- [ ] Phase 5: Deep recheck (references/rules/deep_recheck.md): passes P1–P4 at once, check each finding (a UGT rejection needs a quoted record), rescore, re-save record, check the fix text, then save the report ending in ## Deep Recheck with the fork list
```

**Mark each TODO complete ONLY after thorough verification & completion. Do NOT skip phases.**

---

## Reference Documents (MUST READ BEFORE EVALUATION)

**Read these files FIRST - they define what pass/fail means:**

Read `Evals/Docs/README.md` for the guideline index and `Evals/references/README.md` for the portable reference index. Read each applicable reference below; conditional references do not add user input requirements.

**Reading the Docs.** `Evals/Docs/` holds PDFs and one XLSX. `hg_search.py` reads JSON only and no extractor ships in `Evals/tools/`, so extract the text once with whatever the environment provides (for example `pypdf` and `openpyxl`) and work from that. For the workbook, read only the visible sheets. If a document cannot be extracted, record it as an evidence limit and name the checks it leaves unresolved rather than guessing its contents.

| Document | Path | What to Extract |
|---|---|---|
| **QC Spec (Primary)** | `Evals/Docs/QC_Centralized_Spec_Doc.xlsx` | Visible sheets: Audit Workflow, Examples & Notes, Appendix - Universe Data Queries, Appendix - Universe Inconsistency Examples. |
| **QC Rating Form** | `Evals/Docs/QC_Rating_Form_V12.csv` | Every Prompt and Universe dimension with its fail/non-fail/pass options (subject to the local overrides above). |
| **Prompt Writing** | `Evals/Docs/Original_Conference_Guidelines_-_Prompt_Writing.pdf` | Task shape, difficulty from the environment, context injection, write-it-yourself and AI-text rules, pre-submit checklist. |
| **Overall Task Flow** | `Evals/Docs/Original_Conference_Guidelines_-_Overall_Task_Flow.pdf` | Assignment axes (competency, task skill, horizon), the hard rules and the prompt skeleton. |
| **Universe and Tools** | `Evals/Docs/Original_Conference_Guidelines_-_Universe_and_Tools.pdf` | The company, the thirteen services, scoped reads, the clock. |
| **Persona ACL Policy** | `Evals/Docs/Original_Conference_Guidelines_-_Persona_ACL_Policy.pdf` | Voice, remit and read access for the assigned persona. |
| **Common Errors and Pre-QC** | `Evals/Docs/Original_Conference_Guidelines_-_Common_Errors_and_Pre-QC.pdf` | Frequent prompt failures (entity trap, compounding inaccuracies). |
| **Example Task** | `Evals/Docs/Original_Conference_Guidelines_Example_Task.pdf` | A complete ML-selected Long-Horizon task, for calibration. |
| **Company and storylines** | `<P>_HarmonyGames_Other_Services/metadata/*.resolved.yaml` (`<P>` = `Normal` or `SynthCut`) | Scenario background for the source storylines (76 on Feb 14, 70 on Oct 1). Context only: it cannot override the rules, the roster or the clock, and it is never evidence for a finding. |
| **Persona context** | `Evals/references/persona/roster.json`, plus Contacts, Slack users and Linear users in the service exports | Identity, role, team, relationships and open threads. |
| Scoring definitions | `Evals/references/rules/scoring.json` | Stage dimensions, selectable error labels and thresholds. |
| Scoring interpretation | `Evals/references/rules/scoring_notes.md` | Evidence limits and explicit stage overrides. |
| Persona roster and ACL | `Evals/references/persona/roster.json` and `Evals/references/persona/acl.md` | Exact authorized identities and existing read-access rules. |
| Tool catalog | `Evals/references/tools/catalog.json` | Supplied tools/parameters; apply declared capabilities and record unsupported behavior under `ENVIRONMENT.md`. |
| Injection schema snapshot | `Evals/references/schema/injection.json` and `Evals/references/schema/README.md` | Use only for SQL-related checks; live compatibility is unverified. |
| Long-horizon rules | `Evals/references/rules/long_horizon.md` | Read when the assignment or large audit-table exception applies. |
| Task categories | `Evals/references/rules/task_categories.md` | Six business functions and assignment-fit context. |
| Common errors checklist | `Evals/references/rules/common_errors.md` | The blanks and patterns behind most prompt fails; the Phase 5 deep recheck passes fill them. |
| Deep recheck | `Evals/references/rules/deep_recheck.md` | Phase 5 passes P1–P4, the main-session check, and the `## Deep Recheck` section that ends the report. |

**Catalog coverage:** The supplied exports contain 13 service catalogs plus
the gateway `get_time` tool, including Confluence and Snowflake. Read
`Evals/references/tools/manifest.json` for the full inventory and apply its declared capabilities under the local-search
contract in `ENVIRONMENT.md`. Older service lists do not restrict this inventory.

**Live availability:** `service-availability-v1` in `ENVIRONMENT.md` confirms
Snowflake and Confluence are live, and their reads are unscoped per
`acl.md` (QC Rating Form V12). Do not require a new run to re-prove
availability. A concrete task-specific access conflict remains subject to the
normal evidence rules.

**ACL boundary (read the doc; do NOT hardcode the service set):** `Evals/references/persona/acl.md` is the single, authoritative, and *live* source for which services are persona-scoped for reads. Before evaluating ACL, read that doc's **Access matrix** and derive the sets dynamically: every service its matrix marks **Persona-scoped reads = Yes** is scoped; every service it marks **No** is unscoped. Use whatever the doc currently says — if the doc changes, this eval follows it automatically. Do not rely on any list memorized from a prior version of this eval, and do not reintroduce a hardcoded service list here. (Mechanic note, not a scope claim: if the matrix marks the Google Drive-family scoped, the doc's rule is that GDocs/GSheets/GSlides inherit GDrive's underlying file ACL and that supplying a known object ID does not bypass scoping.) Writes are **always** outside ACL scope: never infer that a write is denied because a related read is scoped, regardless of service.

**Optional calibration:** use only samples explicitly supplied for this review. No external sample folder is required. Use the inline examples and bundled specialist rules to understand the checks.

---

## Inputs for This Task

Injection SQL is optional under `WORKFLOW.md`, and INPUTS.md's intake question
must be answered with SQL or an explicit no-injection choice before evaluation.
Reuse a saved answer; no placeholder file is needed. SQL-read and SQL-seeded
checks below apply only to supplied SQL. Evaluate all remaining source and
coverage requirements against the local records and prompt references.

Apply `WORKFLOW.md`'s **Reference files used by the prompt** contract. Include
applicable files in every grounding and coverage check below. References to
prompt/source/environment requirements in this eval also include validly
incorporated task attachments; those attachments need not be SQL-backed.
Verify Agent availability and cite the actual file contents.

| Input | Canonical file or mapping |
|---|---|
| Exact task prompt | `04_Prompt.txt` |
| Reference files used by the prompt, if any | Uploaded source artifacts (including `.docx` / `.pptx`) or mapped files/links; reuse supplied files and distinguish requested outputs under `WORKFLOW.md`. |
| Required assignment — all five fields | Persona, business function, competency, task skill, and horizon, saved in `Evals/task_inputs/00_Task_Assigned_Inputs.md` or supplied assignment/task notes saved under `WORKFLOW.md` |
| Injection SQL, optional | `01_Universe_Inject.sql` or supplied SQL; omit when unused |
| Error/async configuration, when applicable | `03_Error_Async_Config.txt` |
| Dynamic context, when applicable | `07_Dynamic_Context.md` |

The input table is complete. Later Oracle Events, rubrics and agent/verifier
runs are not prompt inputs, even when older examples mention them.

All five assignment fields are always assigned and required for this review.
Follow `WORKFLOW.md` § "Required prompt assignment": reuse saved values,
save partial submissions, and ask for missing or ambiguous fields before
starting evaluation or issuing a report/verdict. Never infer the assignment
from the prompt or SQL.

**What clears intake.** A saved `00_Task_Assigned_Inputs.md` that states all five
fields explicitly clears intake on its own, in a chat review or a task-folder
review, with no round trip. Record each value and that file as its source. Ask
only when a field is absent, blank, a placeholder, or names a value outside its
allowed set. The same applies to the injection question: saved SQL or a saved
explicit no-injection answer clears it. An unanswered question is an intake
clarification, never a quality finding.

Use the intake rules in `WORKFLOW.md`. Load the roster, ACL rules, schema and
tool catalog locally; read base service records from the local service exports.
They are evaluator references, not additional CB inputs. Model proposed task
state as local base plus the static SQL overlay, not an executed injection.

---

## Universe Data Sources (For Verification)

**Source:** the local service folders in `UNIVERSE_MAP.md`, under
`ENVIRONMENT.md`. Inspect source records and bodies with `SEARCH.md`.
Check persona visibility from the unchanged ACL policy and actual ownership
or membership metadata; search results are not persona-filtered.

| Service | What to verify in the local export |
|---|---|
| Slack | Messages, channels, users and files |
| Linear | Issues, projects, comments, teams, users, memberships and attachments |
| GitHub | Repositories, PRs, issues, commits, comments, reviews, branches, labels, users and repository contents |
| Gmail | Messages, threads, senders, recipients, attachments, users and labels |
| GDrive | Files, folders, users and referenced blobs |
| GDocs | Document content and metadata |
| GSheets | Spreadsheets, tabs and cells |
| GSlides | Presentations and slide content |
| GCal | Calendars, events, attendees, times, locations and recurrence |
| Trello | Boards, cards, lists, actions, members, labels, checklists and attachments |
| Contacts | Contact details and current-user mapping |
| Confluence | Task-relevant spaces, pages, comments, attachments and versions |
| Snowflake | Task-relevant databases, tables, metadata and records through supported read-only paths |

Use `python3 Evals/tools/hg_search.py inventory` for coverage, followed by
targeted `search`, `get` and attachment reads. Missing files or incomplete
searches are evidence limits, not proof that records do not exist.

**Empty-in-base tables:** a table may be a write target or populated by the task's
SQL. Inspect current records and the SQL before declaring a phantom. Proposed
new records are not observed base facts; never apply SQL to run this eval.

---

## STEP 0.5: Injection Gate (2026-10-09)

Run after intake clears and before Phase 0:

```bash
python3 Evals/tools/hg_injection_gate.py
```

| State | Action |
|---|---|
| `NOT_USED` | No overlay. Continue. |
| `ASK` / `NEEDS_ATTENTION` | Follow the intake rules; do not grade yet. |
| `CURRENT` | Reuse the recorded /injection result. |
| `STALE` or `NEVER_REVIEWED` | Run Eval 0 (`0_Injection_Quality_Eval.md`) on the saved SQL now, save its report and manifest entry, then continue. |

Prompts were graded on SQL that /injection never saw (rounds where the SQL
changed after the last /injection run). This step closes that gap.

The gate result goes in the report's `### Injection Gate` section: the state,
the reviewed SQL hash and the Eval 0 verdict. An Eval 0 FAIL does not change a
prompt score by itself. An Eval 0 finding on a record this prompt's answer
depends on is a Cross-Service Coherence finding under Phase 3.2, cited to the
Eval 0 report, only when it changes a value, set, order, recipient or
destination the answer is graded on. Other Eval 0 advisories stay in the
Injection Gate section and do not change a score.

---

## PHASE 0: Reference Document Review + Deep Universe Exploration

**MANDATORY FIRST STEP - Do not skip.**

### 0.1 Read Reference Documents

Pull paths and "what to extract" from the [Reference Documents](#reference-documents-must-read-before-evaluation) table above. Cover them in this priority order:

1. Read the applicable scoring definitions and interpretation notes in the bundled reference table. Use supplied assignment details and local records for current company context.
2. Use supplied assignment details, the bundled roster and current local records for company/persona context. Read `Evals/references/tools/catalog.json` for supplied tools and parameters and check declared capabilities and record unsupported runtime assumptions.
3. **If Long Horizon or Super Long Horizon:** Read `Evals/references/rules/long_horizon.md` in full and apply the assigned tier's necessary-calls guidance, environment-reference, and batch-work rules.

### 0.2 DO VERY VERY DEEP EXPLORATION OF UNIVERSE DATA

First validate eligible existing source ledgers under `WORKFLOW.md`. Source
exploration below applies to new, stale or unsupported claims; record REUSED
for unchanged supported checks while preserving complete ask coverage.

**Inspect the local universe before judging feasibility.** Discover the
services, entities, relationships and relevant source chains. Cover every
mandatory claim and complete task cohort; do not sample away required records.

1. Start with the local service inventory and the declared tool catalog.
2. Inspect the services in the [source table](#universe-data-sources-for-verification),
   prioritizing those the prompt touches. Read full relevant documents, messages,
   attachments and repository contents, and account for pagination.
3. Compare existing records with the static injection SQL. Distinguish records
   proposed by SQL from missing asserted base sources and new requested outputs.
4. Verify names, amounts, dates, account numbers and persona details against
   actual records and supported ACL metadata. Cite each source; report access/export limits.

Read local exports without altering them. Keep supplied historical run state
and SQL-proposed changes distinct from the selected base archive.

### 0.3 Calibrate Against the Example Task

Read `Evals/Docs/Original_Conference_Guidelines_Example_Task.pdf`. Note how a short, informal prompt drives a long task because the operating details live in the environment, and how persona and competency relate (an artist doing defensible GTM work). Use it for calibration only, never as task evidence. Also use this Eval's inline examples for naturalness, grounding and specificity. No sample task folder is required. If the user supplies samples, identify their scope and compare only those artifacts; do not treat them as live facts or policy. With no supplied samples, continue the quality review. Phase 2.9 is not applicable when no comparison samples are supplied; do not claim corpus-wide originality.


---

## PHASE 1: Prompt Structure & Persona Assessment

> **Authoritative scoring source:** The per-phase **Scoring** bands below are an inline convenience summary. The QC rating form in `Evals/Docs/QC_Rating_Form_V12.csv`, as adapted in `Evals/references/rules/scoring.json`, defines every dimension's fail/non-fail/pass band. If an inline band conflicts with them, they win, except where the Local Overrides table above says otherwise.

### 1.1 Persona Coherence Check

**Read `00_Task_Assigned_Inputs.md` and verify the acting identity against the exact
roster in `Evals/references/persona/roster.json`. Use
supplied assignment details and local records for role, relationship, and voice context.**

**Verification Checklist:**

| Check | Question | Finding |
|-------|----------|---------|
| Role Plausibility | Would this person realistically make this request? | Yes/No - [reason] |
| Voice Match | Does the tone and vocabulary fit this persona's role? `roster.json` carries only persona_key, name, email, role and department, so there is no Style line to compare against. Judge against the role only; the persona's own Slack or mail style is not a standard. | Yes/No - [reason] |
| Access Plausibility | Would this persona know about this situation (portfolio/entity access)? | Yes/No - [reason] |
| Responsibility Scope | Does request fall within persona's department/level (prepare/review/approve)? | Yes/No - [reason] |

**IMPORTANT:** Only the exact entries in
`Evals/references/persona/roster.json` may be the acting task
voice. The org chart contains additional storyline identities that are not
selectable personas. Use supplied assignment details and local records for role context for a selected
roster identity; NPCs and non-roster identities appear only as
participants/counterparties. Do not rely on memory or copy a persona format or
identity from a calibration folder.

**Persona identity hard gate:** The assigned acting voice must be one of the
roster's listed taxonomy personas and must match its exact roster entry. The AMV
dropdown is not an identity source and must not replace the assigned taxonomy
persona. Universe Explorer author god-mode is authoring-only. This pre-run
review validates the assigned identity and supported access, not actual future
Runner/verifier execution. Later runs must use that identity, but their outputs
are not prerequisites for `/prompt`.

**Scoring (from bundled scoring.json):**
- FAIL (1-2): Prompt cannot plausibly be written by the assigned persona
- NON-FAIL (3-4): Plausible for assigned persona but fits a different persona better
- PASS (5): Aligns naturally with assigned persona's role, voice, and scope

---

### 1.2 Naturalness & Voice Check

**Verify the prompt reads like a real employee message, not a spec document.**

| Check | Pass/Fail | Evidence |
|-------|-----------|----------|
| First person ("I need...", "Can you...") | | |
| Informal where appropriate | | |
| Real-world feel | | |
| No robotic phrasing | | |
| No technical jargon inconsistent with persona | | |

**Red Flags to Search For:**
- Overly formal/structured for a casual persona
- Reads like a spec document rather than a chat message
- Uses technical jargon inconsistent with the persona's role
- **Excessively long / over-stacked** — many separate asks crammed into one prompt so it reads like a wordy multi-item checklist rather than a focused, natural message. **Soft flag** (note it in Recommended Improvements; suggest tightening to fewer, well-connected asks) — NOT a hard fail on its own. Escalate only if the stacking is actually a **bolt-on** (unrelated asks → Coherence FAIL, see 1.3.2) or makes the prompt **contrived/unnatural** (see 2.7).

#### AI-Text / LLM-Sounding Check

Prompt Writing prohibits LLM-drafted or LLM-polished prompts, and an AI-text detector runs before anything else in the pipeline; an LLM-sounding prompt is the most common rejection. A prompt is a plain natural request: readable, not polished into a document, not roughed up on purpose.

| Red flag | Found? | Quote |
|---|---|---|
| Document formatting: headings, bullets, numbered lists, bold | Yes/No | "..." |
| Polished connective phrasing ("Additionally", "Furthermore", "Please ensure") | Yes/No | "..." |
| Enumerated deliverable specs or preservation rules | Yes/No | "..." |
| Even, symmetric sentence lengths with no natural shortcuts | Yes/No | "..." |
| Staged errors: misspellings, made-up emoji or broken punctuation a person typing normally would not leave | Yes/No | "..." |

Score the result under **Contrived / Unnatural (2.7)**: any red flag fails, including one mild flag on an otherwise real situation. Do not claim to run a detector; report the observable features.

Clean, correctly spelled writing raises no flag (Local Overrides, Typing). A few natural slips are not staged errors; there is no fixed count, so judge whether the errors read as planted. Calibration: #11 (6abc06a6…073708) packs 11 misspellings into about 120 words ("breakdiwn", "wirk", "testd", "chanel", "calndars", "telll") and fails; the same prompt spelled correctly raises no flag.

#### Requirements Incorporated from Reference Files or the Environment

Apply `WORKFLOW.md`'s **Task requirement authority** contract
(`prompt-incorporation-v1`). Only the prompt and instructions it clearly directs
the Agent to follow establish requirements. An unmentioned handbook, onboarding
document or policy adds no grading obligations, even when injected or official.
Sources used for factual research do not automatically become instruction sources.
Record the prompt-to-source passage, scope, availability and version. Do not fail
a prompt for omitting an unincorporated rule. Unresolved incorporation or access
remains an evidence limit; a demonstrated lack of incorporation excludes the rule.

A natural prompt may say to follow a prior request, meeting note, task list, policy, or recommendation instead of repeating its full contents. Treat the referenced record as part of the request only when:

- It is a reference attachment supplied to the Agent with the task, or it exists in the task environment backed by base data or injection SQL. Apply the file-mapping and availability checks in `WORKFLOW.md`.
- The prompt identifies the attachment unambiguously or leads to one uniquely discoverable source through available tools.
- The source clearly states the requirement being attributed to it.
- The source supplies instructions or context rather than a precomputed answer.

Retrieve and inspect the source before scoring clarity, truthfulness, feasibility, or coverage. A file supplied only to the evaluator does not prove Agent access. If a source is demonstrated unavailable to the Agent or multiple files reasonably match the reference, apply the existing feasibility/ambiguity gates. If the evaluator merely lacks the referenced file or availability evidence, request it and record the unresolved check. Do not require the prompt to repeat validly incorporated file or environment content.

---

### 1.3 Structural Anti-Pattern Detection

**Run EACH anti-pattern check independently. Any single failure can FAIL the prompt.**

#### 1.3.1 Command List Detection

**Test:** Does the prompt prescribe a step-by-step procedure?

| Indicator | Found? | Quote |
|-----------|--------|-------|
| Sequential instructions ("First... Then... Finally...") | Yes/No | "..." |
| Numbered steps | Yes/No | "..." |
| Agent told what to do in order | Yes/No | "..." |

**Verdict:** PASS / FAIL

#### 1.3.2 Bolt-On Detection

**Test:** Remove any one sentence. Does the rest still make perfect sense without it?

| Sentence/Clause | Remove it - does rest still make sense? | Bolt-on? |
|-----------------|----------------------------------------|----------|
| "..." | Yes / No | Yes / No |
| "..." | Yes / No | Yes / No |

**If ANY sentence is a bolt-on → FAIL for Coherence**

#### 1.3.3 Pre-Solving Detection

**Test:** Does the prompt tell the agent the answer before investigation?

| Indicator | Found? | Quote |
|-----------|--------|-------|
| Root cause stated | Yes/No | "..." |
| Specific entities identified that should be discovered | Yes/No | "..." |
| Answer counts presupposed ("the employee involved") | Yes/No | "..." |

**Verdict:** PASS / FAIL

#### 1.3.4 Explicit Tool Mention Detection

**Test:** Does the prompt name specific MCP tools unnaturally?

| Indicator | Found? | Quote |
|-----------|--------|-------|
| Tool function names (for example, `slack_send_message` or `linear_create_issue`) | Yes/No | "..." |
| Parameter names (recipient, sender, channel_id, etc.) | Yes/No | "..." |
| MCP server named ("use the Linear MCP server") | Yes/No | "..." |
| A system called a tool ("use the GitHub tool") | Yes/No | "..." |

**Note:** Natural service references are OK ("check my emails", "the Linear ticket"); unnatural exact tool instructions are not ("call `gmail_search_messages`"). Evaluators may use exact tool names. Opaque internal IDs, generated filenames and full agent IDs are scored under Contrived (2.7), not here.

**Verdict:** PASS / FAIL. This dimension is pass/fail (local override): any row above found → FAIL.

---

### 1.4 Prompt Diversity Check

**Prompt diversity is a major quality bar.** Refer to `Evals/references/rules/task_categories.md` for conceptual business-function framing and examples, but validate its write-tool suggestions against `Evals/references/tools/catalog.json`. For the authoritative category list and worked examples, cross-check the task categories defined in `Evals/references/rules/task_categories.md` and the QC spec.

> **Caveat:** the assignment may supply a business-function label that is not verbatim one of the six categories, for example "Engineering" for **Engineering & Live-Ops**. Map it to the closest category in `Evals/references/rules/task_categories.md`, record the mapping, and do not treat the wording difference as a mismatch. Where a supplied label genuinely fits two categories, that is the Non-Fail Business Function Mismatch band.

| Check | Finding |
|-------|---------|
| Does this prompt go beyond "investigate + post one Slack message"? | Yes/No |
| Which task category does it target? | ... |
| Does it use diverse write actions? (not just one `slack_send_message`) | Yes/No - list exact available write tools expected |
| Does the workflow shape differ from typical tasks? (branching, stacking, batch updates, etc.) | Yes/No |

**Not a hard fail** - but if the prompt is yet another "research something, post one generic update," flag it as a diversity concern in your final verdict.

---

### 1.5 Assignment & Complexity Dimensions (HARD GATE)

Bind all five required taxonomy assignment fields before evaluating the prompt.
Use the latest explicit user/task notes or taxonomy values and saved
`00_Task_Assigned_Inputs.md` under `WORKFLOW.md`'s replacement/reuse contract.
Record each exact value and its source; do not infer missing fields.

| Field | Allowed values | Recorded value | Source |
|-------|----------------|----------------|--------|
| Persona | Exact assigned persona, resolved against the authorized roster | | |
| Business function | Taxonomy claim | | |
| Competency | Product Management / Engineering Ops / Marketing and GTM / Corporate Ops / Finance | | |
| Task skill | Retrieval / Analysis and Synthesis / Planning and Decision Support / Authoring / Actions | | |
| Horizon | Exact assigned taxonomy horizon; apply the corresponding design guidance | | |

If any field is missing or ambiguous, return to intake and ask for that field;
wait before evaluating or issuing a verdict. Missing assignment details are not
optional and do not themselves establish a prompt-quality failure. Once supplied,
check assignment alignment. Use the horizon to select applicable design guidance
(including the long-horizon reference when relevant); do not convert an assigned
horizon or call estimate into observed hardness.
Horizon tiers (2026-09-26 update): Normal Horizon is 50–100 tool calls; Long
Horizon is 100–500+. They are measured at Trajectory - Task Type & Horizon from
a 100%-scoring baseline run, or the average of the six baseline runs when none
scored 100%. `/prompt` does not estimate or score a call count; it only uses the
horizon to pick the applicable design guidance.

#### Competency alignment

The scenario and prompt must fall inside the assigned competency's focus and expected outputs (PRDs/roadmap work for Product Management; tickets/PRs/release ops for Engineering Ops; campaigns/GTM for Marketing and GTM; board/legal/HR/vendor for Corporate Ops; models/budgets/forecasts for Finance).

**FAIL** if the task clearly belongs to a different competency than the assigned one. This is a local override: the QC form and Overall Task Flow score a competency mismatch as Non-Fail only. Judge the kind of work, not the persona's job title; a defensible non-obvious match (the Example Task's artist doing GTM work) passes.

#### Task skill

The assigned **primary** skill must be clearly present. Extra stacked skills are encouraged and never a defect.

**FAIL** if the assigned skill is not a real part of the work (for example, an Analysis and Synthesis task that only looks up one value and posts it). This is a local override of the QC form's Non-Fail - Task Skill Weak.

#### Complexity dimensions

Use these as task-design requirements, not a measured model-difficulty score.
A task may use one, two, or all three — **FAIL** only when **none** is load-bearing.

| Dimension | What it requires | Present? | Evidence |
|-----------|------------------|----------|----------|
| **Ambiguity** | Prompt is under-specified on purpose; key details (dates, names, priorities) are planted in the environment. Where the output goes is named when the persona would know it. It is left to the environment only when finding it is the task, and then each place must be findable from a record the persona can see (for example, the message where someone asked). The unhinted prompt + persona-reachable evidence still resolve to one defensible end-state | Yes/No | |
| **Dynamic Change** | A later-discovered source supersedes an earlier one (discovery order, not live mid-run mutation). Name the stale fact, the newer fact, and why a plausible path hits the stale one first | Yes/No | |
| **Multi-Source** | Needed facts split across 3+ systems, with at least one distractor or a resolvable disagreement | Yes/No | |

Ambiguity that cannot be resolved from the environment is still a UGT / Clarity fail — do not treat under-specification as a free pass.

#### Data seeding

Plant operating instructions and missing context in Slack, mail, docs, tickets, or sheets, then keep the user prompt short and natural. Call this **data seeding/injection**, not "SQL injection."

**FAIL** if the prompt is a spec-sheet or long recipe that restates details that already live (or should live) in the environment.

**Scoring:**
- FAIL (1-2): Assigned competency or task skill is mismatched; **or** zero complexity dimensions are load-bearing; **or** the prompt dumps seeded instructions instead of triggering investigation
- PENDING: Required assignment values are supplied, but evidence needed to verify alignment remains unresolved. Missing values must be collected during intake before evaluation.
- PASS (5): All five assignment values are recorded, assignment alignment and applicable horizon guidance are checked, at least one complexity dimension is load-bearing, and the prompt stays a short trigger over seeded context

---

## PHASE 2: Depth Assessment

### 2.1 Unique Ground Truth

Determine whether the prompt and authorized sources under `WORKFLOW.md` establish the
required material outcomes and acceptable alternatives. For a task requiring
one objective answer, reasonable readings must converge on the same material
result. For open-ended work, the request must establish objective acceptance
boundaries rather than one exact wording.

**Before any PASS or FAIL, complete the two-reading precision guardrail and include the table in the report.**

Record the best-supported reading and the strongest plausible alternative.
Name each reading's concrete decision, actions, destinations and required
deliverable contents, with supporting prompt/source passages. For an explicit
option list, account for every option; ruling out one does not resolve a choice
between the remaining options. Apply these five checks to each material difference:

1. **Newer source.** Use the latest applicable source for the same issue and scope.
   A later update can resolve an earlier conflicting statement without explicitly
   announcing replacement. Respect the task's cutoff date and any source priority
   the prompt specifies.
2. **Authority.** When the prompt directs the agent to follow a source, apply its
   instructions to the decisions it governs. Cite the passage that resolves the
   competing reading.
3. **Source identity.** Establish whose words, which message, or which document the
   prompt identifies. A statement from a different source is not automatically
   interchangeable with the named source.
4. **Scope.** A source that settles part of the task does not settle the rest. When
   a later update changes one requirement, retain the unaffected requirements.
5. **Same material result.** Compare the concrete decision, writes, destinations
   and required contents. Wording and equivalent execution paths may differ. The
   same destination alone does not make different contents the same result.

The passage that rules out Reading B must be a prompt sentence or a record the
assigned persona can open under `Evals/references/persona/acl.md`. A record only
another persona can see resolves nothing, and "B is less likely" is not a
resolution. Settle what counts as the event: a deck, a Done ticket or a draft is
not the event unless the prompt says it is. Readings that differ on this are a
material difference until a cited passage settles it.

Accept alternatives actually authorized by the request; do not invent them
from a later Oracle Events or grading criterion. The only exception is a
both-fair figure (below). Listing candidate calls and
asking the agent to choose one does not, by itself, authorize materially
different final calls as interchangeable outcomes. Different writes,
act-versus-defer decisions, or materially different required contents without
a resolving rule are ambiguity.

| Candidate interpretation | Prompt/source authority | Material actions and outputs | Resolved or genuinely ambiguous? |
|---|---|---|---|
| Reading A — best-supported | Exact passage and source | Concrete decision, actions, destination and contents | ... |
| Reading B — strongest plausible alternative | Exact passage and source | Concrete decision, actions, destination and contents | ... |

- **FAIL (1–2):** two supported reasonable readings produce materially incompatible
  required outcomes, and the prompt/authorized sources do not resolve the choice.
  A leading or more-likely interpretation alone does not resolve it (06/09);
  only the prompt, a validly incorporated source, or source identity, scope,
  timing and authority can.
- **PASS (5):** the completed table names the strongest plausible alternative and
  shows that it is ruled out by cited evidence under the five checks or yields
  the same required material result—including the concrete decision, writes and contents, not
  merely the destination. For open-ended work, any remaining differences must
  fall within explicitly authorized alternatives or cited objective acceptance
  boundaries. One coherent procedure, a leading interpretation, or resolving
  only one part of the task is insufficient for PASS.
- **PASS (5): both-fair figure (local override 2026-10-17).** Applies only when
  all five hold: (1) the readings make the same decision, writes, destinations
  and recipients and differ only in one reported figure (amount, count, rate or
  date); (2) each value is stated in a record the assigned persona can open;
  (3) none of the five checks settles it; (4) each reading completes every
  explicit ask; (5) the figure does not change what the agent does next.
  Record it as BOTH_FAIR_FIGURE with both values and citations; the rubric must
  accept either. Every other fork follows the FAIL and PASS rules above unchanged.
  The same fork is not scored again under Clarity (2.6): the writes are the same
  and the two values come from the records, not from the prompt's wording.
  In the record, both readings state the same decision, writes and destinations
  word for word, each reading's contents states its value, and the
  comparison's `figure` holds the kind, a label, the two
  values (leading reading first) each with its record quote (and a derivation
  when the record gives the operands, not the value), a reason for each of the
  five checks, and the reasons for conditions 4 and 5; the generated section
  then prints "Rubric must accept: X or Y". Calibration: #50 (6aa8272b…fea8d),
  where the 2-day completion rate is 32.8% under the #analytics roll-up note
  the thread points to and 28.5% from the ZOM-673 operands, passes as
  BOTH_FAIR_FIGURE. #49's $8.5K (2026-01-22) versus $8K (2026-01-23) does not:
  the newer source settles it. A file-now versus defer fork is not a figure.
- This sub-dimension has no scored NON-FAIL band. Required missing source evidence
  follows `WORKFLOW.md` § "Ruthless grading standard", not an invented ambiguity finding.

Do not consult rubrics, Oracle Events, run convergence or a fixed number of
agent runs. Prompt interpretation comes before those artifacts. Record the
resolved requirements and cited outcome boundaries for downstream reuse.

**Challenge the comparison before saving.** Confirm that Reading B is the
strongest plausible alternative, not an easier-to-dismiss strawman. Read each
cited passage and explain how it supports or resolves the specific difference;
a real but irrelevant citation does not settle it. A list of candidate options
is not evidence that different final calls are authorized. A demonstrated,
unresolved difference in one required outcome is enough to establish FAIL;
proving it does not require completing every other task deliverable.

Include this comparison for every scored UGT verdict, including UGT PASS when
another dimension makes the overall report FAIL. Save the matching
`unique_ground_truth` field in the format-2 `prompt_check_record.json` under
[the prompt report contract](references/rules/prompt_rubric_reliability.md).
Generate its report section with
`python3 Evals/tools/hg_prompt_checks.py render-ugt [record-path]`
(the saved record is the default) and include that section verbatim in the
report. Keep the UGT score and verdict synchronized with the record. Required
missing evidence continues to follow the existing provisional-report rules.

---

### 2.2 Feasibility - DEEP EXPLORATION REQUIRED

**⚠️ THIS IS THE MOST IMPORTANT CHECK. Do NOT rush. Do NOT assume. VERIFY EVERYTHING.**

**Check:** Can the prompt be COMPLETELY fulfilled by an AI agent using available service tools and documented/observed task-Agent runtime capabilities, with the data that ACTUALLY EXISTS in the universe **as the assigned persona**?

**This is NOT just a tool capability check.** You must verify TWO things:

**A. Tool Feasibility** - Do the task Agent's available service tools and documented/observed runtime capabilities support every required action? Read `Evals/references/tools/catalog.json` and apply `WORKFLOW.md`'s **Output capability and failure attribution** contract.

For every requested deliverable, verify content creation, actual format generation/export and the requested save/share/handoff. Record each step's capability evidence and SUPPORTED / UNSUPPORTED / UNVERIFIED status. Confirmed absence of a necessary capability with no valid path is **FAIL (Feasibility)**, including secondary explicit output asks. Incomplete evidence is UNVERIFIED per `WORKFLOW.md` § "Output capability and failure attribution" and is then graded under § "Ruthless grading standard"; absence of a named PDF tool alone is insufficient. Neither a MIME field nor the evaluator's own Python environment proves the task Agent can produce and deliver a PDF. Suggest a supported output or environment correction; do not silently rewrite the task.

| Ask from Prompt | Required Capability | Tool(s) Available? | Feasible? |
|-----------------|--------------------|--------------------|-----------|
| [Ask 1] | [What's needed] | [Tool name] | Yes/No |
| [Ask 2] | [What's needed] | [Tool name] | Yes/No |

**A1. Current service availability** - Apply `service-availability-v1` in
`ENVIRONMENT.md`. Snowflake and Confluence are live and may be used through
supported cataloged operations. References to a wiki, knowledge base, space/page,
analytics warehouse, SQL query or `SCHEMA.TABLE` path are not feasibility defects
by themselves. Check the actual operation, required data and any evidenced
task-specific access restriction. The original ACL omission alone is not a
FAIL, PENDING or HOLD reason; do not require another run or a different service
merely for that omission. A confirmed unsupported operation or inaccessible
required read still fails under the normal feasibility rules; a material
unresolved access conflict remains PENDING.

**B. Data Feasibility** - Does the universe data contain EVERY piece of information needed to answer the prompt? This requires searching local records and inspecting the full relevant sources. Do NOT trust your memory from Phase 0 - go back and verify.

| Information Needed to Solve | Where Should It Exist? | Actually Searched? | Found? | Evidence |
|----------------------------|----------------------|-------------------|--------|----------|
| [Key fact 1] | `gmail/threads/<thread>.json` | Yes/No | Yes/No | "..." |
| [Key fact 2] | `gsheets/data.json` (`sheets_spreadsheets`) | Yes/No | Yes/No | "..." |
| [Key discovery the agent must make] | `slack/messages/<channel>/<YYYY-MM>.json` | Yes/No | Yes/No | "..." |

**Search the local sources thoroughly. Proven absence of a required existing source is a feasibility defect; incomplete access or export coverage is an unverified check. Account for SQL-proposed records and task attachments before declaring absence.**

**C. Dimensional Feasibility (HARD GATE — mandatory when the prompt asks for a breakdown)**

When the prompt asks for a quantitative result **broken down by a dimension** (per-state, per-vendor, per-period, per-entity, per-jurisdiction, per-cost-center, per-employee, etc.), you MUST verify that the universe data **actually carries that dimension** as a field before passing feasibility. If it doesn't, the breakdown is impossible / requires secondary input and the prompt is not solvable as stated.

| Breakdown Requested in Prompt | Dimension Field Required | Table(s) to Check | Field Exists? | Verdict |
|-------------------------------|--------------------------|--------------------|--------------:|---------|
| [e.g., "per project"] | project name field | `linear/data.json` (`projects`), relevant `trello/data.json` files | Yes/No | Feasible / **FAIL** / UNVERIFIED |
| [e.g., "by assignee"] | assignee_id or assignee_name | `linear/data.json` (`issues`) | Yes/No | Feasible / **FAIL** / UNVERIFIED |

**Procedure (mandatory):**
1. Extract every quantitative ask from the prompt that requests a breakdown or per-X split.
2. Identify the dimension (the "by X" or "per X" or "across our X" qualifier).
3. Open the relevant universe data tables and confirm the dimension exists as a queryable field.
4. If the field does not exist → the ask is **impossible as stated** → **FAIL (Feasibility)**. Do NOT wave it through on professional charity or context ("they'd know to look elsewhere") — if the data isn't there, it isn't there.

**Why this is a hard gate:** This exact pattern caused a genuine fail in a prior universe — a prompt needed per-jurisdiction figures, but the relevant data table had no state/jurisdiction field. The eval waved it through and QC caught it.

**D. Numeric Observability (HARD GATE — mandatory for quantitative precision and exact-value asks)**

Raw backing data establishes canonical truth; tool-visible output establishes whether that truth is scoreable by the Agent. A prompt passes only when both layers support the requested result.

| Quantitative Ask | Raw Universe Value / Inputs | Cataloged Tool Path | Tool-Visible Value / Precision | Hidden Derivation Required? | Verdict |
|------------------|-----------------------------|----------------------|--------------------------------|-----------------------------|---------|
| [Exact amount or rate] | [raw value / component fields] | [tool + query/read path] | [returned value / scale] | Yes/No | Feasible / **FAIL** / UNVERIFIED |

**Procedure (mandatory):**
1. Extract every exact amount, percentage, decimal-place instruction, rounding rule, and derived-number ask from the prompt.
2. Verify the canonical value and all calculation inputs in the raw universe.
3. Verify the same fields through the cataloged tool path. Use same-snapshot trajectories when available; otherwise inspect tool schemas, parameters, known rendering behavior, and any representative query evidence. **Catalog limit:** `catalog.json` lists only each tool's `name` and `parameters`; it carries no return schemas and no service field, and the per-service files such as `gmail-tools.json` supply the service split. When no trajectory or schema establishes how a value is rendered, verify the raw value and the derivation, then record the rendering as an explicit evidence limit. Do not fail the gate for missing return schemas, and do not claim a rendering the catalog cannot establish.
4. Record rounding, truncation, coercion, pagination loss, or omitted fields. A raw value in an unserved local file does not make the ask feasible.
5. Separate **display formatting** from **calculation instructions**. “Report to one decimal place” controls presentation; it does not silently authorize a hidden recomputation from other columns.
6. If the requested precision is lost and the prompt supplies no explicit derivation rule or reachable alternate source, mark the ask **FAIL (Feasibility)**.

**E. Persona-Scoped Read Feasibility & Ask-Level ACL Violation (STRONG HARD GATE — standalone FAIL)**

**This gate stands alone.** A single required scoped-service read that the assigned persona cannot reach — with no affirmative-denial outcome and no authorized unscoped alternate — FAILS the prompt on its own, regardless of how strong every other dimension is. It cannot be waived, averaged away, or excused as a minor/secondary ask, and raw-data or Universe Explorer author god-mode existence never satisfies it.

**First, load the scope dynamically:** read the **Access matrix** in `Evals/references/persona/acl.md` and list the services it currently marks persona-scoped for reads. Do NOT hardcode the set from memory or from this eval. Apply the checks below to every service in that doc-derived scoped set. Mechanic note (not a scope claim): if that set includes the Google Drive-family, remember the doc's rule that GDocs/GSheets/GSlides inherit GDrive's file ACL and that supplying a known object ID does **not** bypass scoping.

This gate has two lenses — run BOTH:

**Lens 1 — Required-read feasibility.** For every fact in a persona-scoped service that is required for successful completion, record its source and whether the assigned persona can read it:

| Required Scoped-Service Fact | Service / Record | Scoped per ACL doc? | Assigned-Persona Visibility Basis | Authorized Alternate Source? | Verdict |
|------------------|------------------|--------------|--------------------------------------|------------------------------|---------|
| [fact] | [record] | Yes (which service) / No | mailbox ownership / channel membership or implemented public visibility / calendar ownership-share-invite / Drive ownership-or-share / N/A | [source or none] | Feasible / **FAIL** / UNVERIFIED |

**Lens 2 — Ask-level ACL violation.** Independently, scan every explicit and buried ask in the prompt for any directive that instructs the assigned persona to *read* scoped-service data outside their visibility (e.g., "open the spreadsheet Leonard shared internally," "check Maria's calendar," "pull the doc from the Design drive") when that record is not owned by / shared with / visible to the persona. Such an ask is an **ACL violation → FAIL**, even if the same fact happens to be reachable elsewhere — unless the prompt's intended outcome is an affirmative denial (identify/report/escalate) or an explicitly authorized alternate source.

Rules:
1. Scoped-service evidence visible only to another persona cannot be required for successful completion. Its presence in raw data or Universe Explorer author god-mode does not make the ask feasible.
2. An intentional read-denial task is valid only when successful completion requires an **affirmative compliant outcome**, such as identifying/reporting the denial, escalating it, or finding an authorized alternate source. A prompt that merely requires impossible access still fails.
3. Expected denial followed by an authorized unscoped-source investigation can be feasible. Apply ACL to reads only in the services the ACL doc marks scoped; services it marks unscoped remain readable by any task persona.
4. Writes are **always** outside ACL scope. Never infer write denial for any service, including the Drive-family.
5. `set_acting_user` is environment configuration, not an Agent tool call or prompt ask.

**Feasibility Checklist:**

| Check | Pass/Fail |
|-------|-----------|
| Every ask can be completed with available MCP tools | |
| Every piece of information the agent needs EXISTS in the universe data | |
| The agent can DISCOVER the information (it's retrievable via tool queries) | |
| No impossible requests (human judgment, physical actions) | |
| No conflicting instructions | |
| No requests beyond MCP tool access | |
| **Dimensional feasibility: every per-X breakdown the prompt asks for has a corresponding field in the universe data** | |
| **Numeric observability: every requested exact value or precision is retrievable or explicitly derivable from tool-visible data** | |
| **Persona-scoped feasibility: every required fact in a persona-scoped service (per the `Evals/references/persona/acl.md` access matrix) is visible to the assigned persona, intentionally denied with an affirmative compliant outcome, or available from an authorized unscoped alternate source** | |
| **Ask-level ACL: no prompt ask directs the persona to read scoped-service data outside their visibility (unless the intended outcome is affirmative denial or an authorized alternate)** | |

**Scoring:**
- FAIL (1-2): Contains impossible/impractical requests, conflicting instructions, OR required data does not exist in the universe
- NON-FAIL (3-4): **Not used (local override).** The QC form's [Non-Fail - Prompt Impractical Secondary Request] band does not apply here. If ANY explicit prompt ask cannot be fully fulfilled with available tools and data, it is a FAIL, whether it is the core ask or a secondary one. Only implicit/nice-to-have asks (not explicitly stated in the prompt) may be excused.
- PASS (5): Completely actionable - all tools available, all data exists, and every requested value/precision is discoverable or explicitly derivable through the Agent's tool-visible environment

---

### 2.3 Truthfulness - EXHAUSTIVE Universe Verification

Apply [prompt/rubric evidence reliability](references/rules/prompt_rubric_reliability.md).
Record the exact asserted existence, state and relationship premises with source
checks in the premise record at `Evals/task_inputs/reports/drafts/prompt_check_record.json`,
saved with `python3 Evals/tools/hg_write_output.py prompt-checks --source "<record.json>"`
before the scored report; requested new outputs and hypotheses are
not asserted existing facts. Verify original identity/account fields when a
pseudonymized label conflicts with raw message or source identity data; do not
infer a person from a substituted product name. Review source chronology and
entity ownership before calling a premise false. Dynamic context and difficulty
notes are discovery leads, not factual authority. Complete the bound premise
record before a scored prompt report; retain every existing phase and score.

**⚠️ CRITICAL PHASE - This is where most errors are caught. Do NOT rush.**

**MANDATORY: Verify EVERY factual claim in the prompt against universe data.**

**Major vs Minor classification (06/10) — apply this when you find an error:**
- **Major (1 = FAIL):** errors in **tight identifiers** — channel names, document IDs, vendor/company entity names, account numbers, dollar amounts, dates, fiscal periods, ticket/issue IDs. These are passed literally into tool calls and do not tolerate near-matches. A confirmed phantom identifier for an asserted existing source is always Major. Establish absence with adequate local source coverage, accounting for SQL and task attachments; an unavailable read is not proof of absence.
- **Minor (1+ = FAIL):** errors in **loose descriptors** — person first-name-only references where the universe context disambiguates, role titles, casual entity references. One loose slip fails even when it does not change what has to be done.
- **Escalation:** a Minor error escalates to Major if it actually causes agent failure (e.g., a first name where two people in the universe share it).
- **HARD GATE — phantom tight-identifier search (mandatory before a Truthfulness pass):** Extract **every** tight identifier in the prompt — channel names, document/ticket/issue IDs, vendor & company entity names, account numbers, dollar amounts, dates, fiscal periods — and verify each against local records, SQL and applicable task attachments. A confirmed missing asserted source is phantom = **Major (FAIL)**; incomplete access or pagination leaves the check unverified. Requested new outputs are not phantoms. **Near-match trap:** a partial/substring match is NOT a match — if the prompt names channel 'X' but only 'X-and-Y' exists, 'X' is a phantom (it is passed literally into the tool call and fails). Do **not** assume "that's what they meant." Do not skip this gate.

- **HARD GATE — state-premise verification (mandatory before a Truthfulness pass):** The phantom-grep gate above catches bad *identifiers*; it does NOT catch bad *state premises* — declarative claims about the current state of the world that the universe contradicts. These grep clean (the named entity exists) yet still send the agent down a false path, and they were the latest cohort's hardest Truthfulness misses. Extract **every declarative state premise** in the prompt — anything the persona asserts as currently true — and verify each against the universe. Watch for:
  - persistence claims: "still no reply", "hasn't been merged/closed/paid/answered", "is still open", "nobody has responded yet"
  - existence / absence claims: "there's no ticket for this", "I never got the invoice", "we have no record of X"
  - temporal-window claims: "for the past two weeks", "since Monday nothing has…", "over the last sprint"
  - relationship / ownership state: "I own this", "this is assigned to me", "I'm the approver on it"
  - company and people state: work that assumes HarmonyGames still runs normally after the February 11, 2026 shutdown announcement, or that a person who has left reviews, approves or replies. #43 (6a83fa91…3deb) fails: its premise has Victor, who left in April 2025, holding a current art-canon handoff control. Cite the records that show the shutdown or the departure, not the storyline YAML. The shutdown part applies to Feb 14 tasks only. On an Oct 1 task the company runs normally, so business as usual is not a false premise; a person who left before 2025-10-01 (Victor) still is, and so is anything the prompt treats as existing that only appears after 2025-09-30 23:59:59 PT (for example Combo Fighter or Zombie Match Lite work).

  Any state premise the universe **contradicts** is **Major (FAIL)** — treat it exactly like a phantom identifier, because it breaks the task the same way. A premise that is merely **unverifiable** (no supporting record either way) is a truthfulness risk: flag it and confirm the task is still solvable without it.

**Verification Protocol:**

1. **Extract every named entity** from the prompt (people, companies, events, dates, amounts)
2. **Search the relevant local records** for each entity
3. **Document your findings** with file paths and evidence

| Entity/Fact from Prompt | Search Query | File(s) Searched | Found? | Accurate? | Evidence |
|------------------------|--------------|------------------|--------|-----------|----------|
| [Person name] | Supported contact/mail search | Deployed Contacts/Gmail tool or export URL + record ID | Yes/No/Unverified | Yes/No/Unverified | Field: "..." |
| [Entity / team member / contractor] | Supported contact/Slack search | Deployed Contacts/Slack tool or export URL + record ID | Yes/No/Unverified | Yes/No/Unverified | Field: "..." |
| [Event/situation] | Supported mail/Slack search | Deployed Gmail/Slack tool or export URL + record ID | Yes/No/Unverified | Yes/No/Unverified | Field: "..." |
| [Relationship claim] | Supported identity/relationship lookup | Deployed record + local roster/context reference | Yes/No/Unverified | Yes/No/Unverified | Field: "..." |
| [Dollar amount] | Supported sheet read | Deployed GSheets tool + spreadsheet/tab/cell | Yes/No/Unverified | Yes/No/Unverified | Cell: "..." |

**Deep Verification Checklist:**

- [ ] All person names exist in universe
- [ ] All company names exist in universe
- [ ] All events/situations referenced actually occurred in the data
- [ ] All relationships stated are correct (X manages Y, Z works at W)
- [ ] All dates mentioned align with universe timeline
- [ ] All dollar amounts match universe data
- [ ] No misleading statements that would send agent down wrong path
- [ ] No grammar errors or typos that change meaning or break feasibility or truthfulness (e.g., wrong person name "Samra" vs "Samira", wrong month "March" vs "April", wrong entity "Vectral" vs "Vectoral") - cosmetic typos that don't affect meaning are fine. Staged typos fail Contrived (1.2).

**Scoring:**
- FAIL (1-2): 1+ **major** factual errors (tight-identifier errors — see classification above) OR 1+ **minor** factual errors
- NON-FAIL (3-4): **Not used.** One loose descriptor error fails.
- PASS (5): No factual errors, no misleading statements

---

### 2.4 Cross-Service Requirement

**Check:** Does the prompt require data/actions across multiple MCP services?

**Service Mapping:**

| Service | Why Needed | Read/Write | Evidence from Prompt |
|---------|-----------|------------|---------------------|
| Slack | | Read / Write | "..." |
| Linear | | Read / Write | "..." |
| GitHub | | Read / Write | "..." |
| Gmail | | Read / mailbox-label mutation / outbound mail (send, reply, drafts) | "..." |
| GDrive/GDocs/GSheets/GSlides | | Read / Write | "..." |
| GCal | | Read / Write | "..." |
| Trello | | Read / Write | "..." |
| Contacts | | Read / Write | "..." |
| Confluence | | Check declared capability and available evidence | "..." |
| Snowflake | | Check exported data and declared query capability | "..." |

**Validation:**
```
Services required: [count task-required service domains; exclude gateway clock utilities]
- Minimum 2 distinct services: [PASS/FAIL]
- Ideally 3+ services: [Yes/No]
- Information friction exists (answer not in one place): [Yes/No]
- Each required service changes a graded fact (dropping it changes the answer): [Yes/No per service]
```

Name, for each of the two required services, the graded fact it changes. A
second service that is read but changes no graded fact does not count; the
prompt is then single-service.

**Scoring (no NON-FAIL band):**
- FAIL (1-2): Single service, a second service that changes no graded fact, or answerable without tools / Pre-solved
- PASS (5): Requires genuine cross-service investigation in which each of two services changes a graded fact, plus at least one write action

---

### 2.5 Investigation + Action Verification

**Check:** Does the prompt require BOTH investigation (reading) AND action (writing)?

| Phase | Required? | Evidence from Prompt |
|-------|-----------|---------------------|
| Investigation (searching/reading across services) | Yes/No | "..." |
| Action (post Slack message, create issue, schedule GCal event, etc.) | Yes/No | "..." |
| Investigation feeds the action (can't act without investigating) | Yes/No | "..." |

**Write Actions:** Use `Evals/references/rules/task_categories.md` only for business-function framing. Build the actual write-tool list from the `Evals/references/tools/catalog.json` catalog. In particular, Gmail now has outbound mail (send, reply, drafts) in addition to mailbox/label mutations.

**Scoring:**
- FAIL: Only investigation with NO tool-based write action (unless intentional)
- PASS: Both investigation AND action required, with investigation feeding the action

---

### Call Counts Are Not Scored Here

The former "more than 15 necessary calls" prompt gate is **removed** (2026-09-26 update). Tool-call requirements are handled only at Trajectory - Task Type & Horizon: use the tool-call count from a baseline run that scored 100% on the rubric when one exists, otherwise the average across the six baseline runs; Normal Horizon is 50–100 calls and Long Horizon is 100–500+. The Oracle Events set never enters that count.

`/prompt` still checks the design that makes a task deep: genuine cross-service investigation with information friction (2.4), investigation that feeds meaningful writes (2.5), and a load-bearing complexity dimension (1.5). Do not estimate or score a call count. Padding with blocked, repeated or unnecessary calls is contrived (2.7).

---

### 2.6 Clarity & Specificity

**Check:** Can an expert developer/employee understand what's being asked?

| Question | Answer |
|----------|--------|
| Is user intent clear from the prompt? | Yes/No |
| Are key details present (who, what, when, where)? | Yes/No |
| How many assumptions needed to answer? | [count] |
| Could this be reasonably interpreted multiple ways? | Yes/No |
| If interpreted multiple ways, do the interpretations lead to DIFFERENT write actions (or write vs no-write / act vs defer)? | Yes → FAIL (Action Decision Ambiguity) / No → at most NON-FAIL |

**HARD GATE — Delegation Clarity (mandatory scan):**
Scan the prompt for all first-person action statements: "I'll [verb]", "I need to [verb]", "I want to [verb]", "I'm going to [verb]".

If ANY such statement appears alongside imperatives directed at the agent (e.g., "check my emails" + "I'll post an update to Slack"):
- Determine: is the "I'll" statement intended as user self-action (the persona will do it themselves) or delegation to the agent (the agent should do it)?
- If ambiguous → **FAIL (Action Decision Ambiguity)** — two reasonable readings lead to different write actions (agent posts vs. agent doesn't post).
- "I'll [verb]" ordinarily assigns the action to the user. Resolve the actor from the request; do not consult later criteria to turn user work into an Agent obligation.

**Scoring:**
- FAIL (1-2): **[Major Clarity/Specificity Issues]** not clear what's being asked, extremely difficult to follow, or critical details missing and unassumable; **OR [Action Decision Ambiguity] (06/09)** the prompt is open to 2+ reasonable interpretations that lead to **different write actions** (or write vs. no-write / act vs. defer) and nothing resolves which is intended.
- NON-FAIL (3-4): **[Minor Clarity/Specificity Issues] (narrowed 06/09)** — multiple reasonable interpretations exist but **all lead to the same set of write actions / external side effects**; only wording, framing, channel-of-delivery to the same recipient, or non-action details vary (e.g., 'send a quick note to Daniel' = email vs. Slack DM to the same person; 'the partner' = minor referent ambiguity that doesn't change the action).
- PASS (5): Little to no room for misinterpretation of the specific request.
- **HARD GATE — write-action divergence (mandatory before scoring Clarity):** Enumerate the **write action(s)** the agent would take under each reasonable reading. If two readings produce different write actions — or write vs. no-write / act vs. defer — and nothing in the prompt resolves which is intended → **FAIL (Action Decision Ambiguity)**. Wording-only or channel-to-the-same-recipient differences that converge on the same action are NOT a fail.
- **Distinction from UGT:** UGT compares the required final decisions, writes and contents under the mandatory two-reading check in §2.1; Action Decision Ambiguity asks whether the *write action the agent chooses* diverges. A file-now-vs-defer prompt typically fails BOTH.

---

### 2.7 Contrived vs Natural Difficulty

**Check:** Does difficulty come from natural business complexity or artificial constraints?

**Contrived Indicators (BAD):**

| Indicator | Found? | Quote |
|-----------|--------|-------|
| Exact timestamps demanded | Yes/No | "..." |
| Arbitrary format constraints | Yes/No | "..." |
| Unrealistic employee behavior | Yes/No | "..." |
| Step-by-step commands disguised as prompt | Yes/No | "..." |
| Difficulty from precision, not complexity | Yes/No | "..." |
| Arbitrary checkpoints, repeated reads, or unnecessary writes added to increase calls | Yes/No | "..." |
| Unnatural opaque IDs, generated filenames, full agent IDs or similar references a person would not type (2026-09-26 update) | Yes/No | "..." |
| LLM-sounding text or staged errors from the AI-Text check in 1.2 | Yes/No | "..." |
| Trap hint or riddle: wording that points at the trap without naming it | Yes/No | "..." |
| Hidden destination the persona would know ('wherever that's been asked for', 'the same place the rest of these calls have been going') | Yes/No | "..." |

**Trap hints and hidden destinations (2026-10-17).** A Yes on either row fails
Contrived, like the other rows. A hidden cause is good difficulty only when the
prompt does not hint at it; naming the symptom stays fine (Local Overrides,
Riddles). #31 (6aaae611…2a2b) fails on "I have a nagging feeling the thing that
actually bites us is not on anybody's list" and "at least a couple of the
conclusions people settled on in Slack do not survive contact with the code";
"CPI jumped last week and I don't know which test did it" passes. A destination
may be left to the data only when finding it is the task and a persona-visible
record names each place (1.5 Ambiguity). #42 (6abd857f…8348, "get it on record
wherever that's actually been asked for"), #47 (6abcef4d…025c, "landed in the
same place the rest of these wind down calls have been going") and #44
(6ac674e1…ecbf, "answer him there too", where nothing leads to the PR comment)
fail; "post the summary in #winddown" passes.

**Realistic human requests (2026-09-26 update).** Prompts should read like realistic workplace requests. Exact titles and values are fine when they are naturally human-readable ("the Q1 Launch Plan doc", "$4,180"). An unnatural opaque ID, generated filename, full agent ID, or exact timestamp ("January 15 at 3:47 PM") **fails** Contrived unless the task is about that ID or timestamp.

**HARD GATE — Spec-Sheet Register Escalation (mandatory):** Over-stacking is a *soft* flag under Naturalness (1.2), but the latest cohort shows the ~600-word "spec-sheet register" prompt is the single most common contrived fail (5/12; see `Evals/references/rules/scoring_notes.md`). Escalate the soft flag into a **Contrived FAIL** here when the prompt exhibits the register — a natural scenario delivered in an unnatural voice that reads like a deliverables spec rather than a message. Trigger it when **two or more** of these are present:

| Register trigger | Found? | Quote |
|-----------|--------|-------|
| Enumerates each deliverable's exact contents item-by-item ("the note should contain (a)…(b)…(c)…") | Yes/No | "..." |
| States preservation / format rules for the output ("keep the existing order", "don't change the headers", "use this exact structure") | Yes/No | "..." |
| Prescribes the reply format ("respond with a table with these columns", "give me back exactly these fields") | Yes/No | "..." |
| Length driven by exhaustively listing contents rather than by scenario complexity | Yes/No | "..." |

**Audit forms and if-chains (2026-10-17).** Each of these red flags fails
Contrived on its own; it does not need a second trigger. There is no word list
and no count: judge whether the prompt reads as a person asking for help, and
calibrate on the examples below. A per-case rule belongs in a seeded record,
not in the prompt.

| Red flag | Found? | Quote |
|-----------|--------|-------|
| Reads like an audit or compliance form, not a person asking for help | Yes/No | "..." |
| Long chains of if / but-not / then-also clauses dictating what the Agent does per case | Yes/No | "..." |

#1 (6a7f62da…6b43, "Find the current governing control he meant, reconcile
its evidence, and complete the decision record, remediation, and handoff it
requires") and #43 (6a83fa91…3deb, "apply it to the full in-scope upload-thread
cohort, reconcile the decisions chronologically, classify the outcomes, rank
the outstanding channels and evidence, and complete the review artifacts and
handoff it requires") read as forms and fail. #44 (6ac674e1…ecbf, "If he asked
me somewhere else, not the rules or his posts about them, to shut something off
or hand it over, answer him there too") is an if-chain and fails. "Arthur wants
the merge-review stuff sorted before the next push, can you check what's still
open and close it out?" passes.

**Naturalness reference:** use `Evals/references/rules/long_horizon.md` for natural delegation and moving validly incorporated operating detail into the environment. Judge the actual task's wording and necessary work; no historical task file is required.

**Natural Difficulty Indicators (GOOD):**

| Indicator | Found? | Quote |
|-----------|--------|-------|
| Entity confusion (similar names, overlapping roles) | Yes/No | "..." |
| Information scattered across services | Yes/No | "..." |
| Conflicting data between systems | Yes/No | "..." |
| Hidden root causes the prompt does not hint at | Yes/No | "..." |
| Multiple related issues to connect | Yes/No | "..." |
| Implicit requirements carried by records, not by prompt wording | Yes/No | "..." |

**Scoring:**
- FAIL (1-2): Contrived or unnatural prompt, including a spec-like or polished draft whose situation is real, or an unneeded opaque ID, generated filename, full agent ID or exact timestamp; or staged errors, a trap hint or riddle, a hidden destination the persona would know, audit-form wording or a long if-chain (2026-10-17)
- NON-FAIL (3-4): **Not used.** A limited artificial or LLM-sounding element fails.
- PASS (5): All difficulty comes from natural business complexity, and the prompt reads like a real employee message

**Long Horizon anti-inflation check:** Apply the assigned tier's scale target. Verify that repeated calls answer distinct required questions over a source-defined cohort and that no complete bulk result can replace them. The call count itself is never evidence of quality. Repeatedly opening the same record, splitting one complete response into smaller calls, or adding process choreography only to increase volume is contrived. Use `Evals/references/rules/long_horizon.md` to verify that each record/surface check answers a distinct necessary question and that discovery, creation and verification calls support the deliverable.

---

### 2.8 Alignment with Today's Date Check

The fixed universe date and time is the task date's clock: **2026-02-14 00:00 UTC**
(Universe and Tools) for Feb 14 tasks and **2025-10-01 00:00 PT (2025-10-01 07:00 UTC)**
for Oct 1 tasks. Read the saved date (`hg_universe.py show`); never assume one.
**Relative wording is allowed (local override).** Universe and Tools and Prompt
Writing tell authors to write dates absolutely; this Eval does not fail relative
wording. Expressions such as "Friday", "today", "yesterday", "last week" and
"this morning" do not need to be rewritten as explicit dates.
Evaluate whether the intended reference is clear and consistent with the task
context and source timeline, not whether the prompt uses a particular date format.

**Step 1: Resolve material temporal references.** Use the fixed universe clock for
the task's current "today" or "now". Interpret relative wording inside a historical
message against that message's own date/context. Preserve explicit source timezones;
the universe clock itself is UTC. Record the resolved date or window
in the review when it matters to scope, a deadline, current state or an action.
In persona-written text, 'today' means Saturday, February 14, 2026, the date of
the fixed clock (2026-02-14 00:00 UTC, the current date set in the taxonomy).
'Yesterday' is February 13. On an Oct 1 task, 'today' means Wednesday,
October 1, 2025 (the clock is 2025-10-01 00:00 PT) and 'yesterday' is
Tuesday, September 30, 2025.

| Reference | Review action |
|-----------|---------------|
| "Friday", "yesterday", "last week" | Resolve using the task clock and incorporated source context; accept when the intended event/window is clear. |
| "today", "now", "still open" | Check the requested state at the task clock (2026-02-14 00:00 UTC or 2025-10-01 00:00 PT); historical quotations retain their own temporal context. |
| "this morning", "EOD", "an hour ago" | Resolve the time boundary only to the precision the request needs; use supplied timezone information where necessary. |
| Explicit date or named event | Verify it against the source; explicit wording does not excuse a wrong date or nonexistent asserted event. |

**Step 2: Test material ambiguity.** Consider plausible readings in context.
Do they change the required records, conclusions, deadline or write actions?
If sources resolve the choice, accept it. Harmless imprecision or wording variation
is not a defect. If materially different readings remain genuinely plausible,
report the actual ambiguity under Clarity/Unique Ground Truth with both readings
and their consequences. Do not demand an exact date merely for convenience.

**Step 3: Verify source and clock consistency.** Confirm any asserted event/date
and the data needed to answer the request. An empty search result can be a valid
answer to a request to check a window; it is not automatically a time-alignment
failure. An asserted event that demonstrably did not occur in the identified
window, or a request treating an event after the fixed clock as already past,
can be a real contradiction. Missing evidence or an unstated timezone that is
necessary for a boundary decision remains PENDING, not an invented contradiction.

**Step 4: Check universe-level alignment.** Keep the existing material-coherence
gate: source dates that create contradictory scenario state or make the requested
work impossible can fail before a run. Do not use an export date, the review
date or the existence of older historical records as an automatic failure.

**Scoring:**
- **PASS (5):** Temporal references, explicit or relative, resolve sufficiently
  for the task and are consistent with the fixed clock and relevant sources.
- **FAIL (1–2):** A demonstrated material temporal contradiction or unresolved
  material interpretation conflict changes the required result/action or makes
  the request impossible. Explain the concrete conflict; relative wording alone
  never qualifies. (Local override: the QC form scores Prompt Misaligned with
  Today as Non-Fail only.) Seeded records dated after the clock are scored under
  Cross-Service Coherence (3.2) as a Temporal Field Inconsistency.
- **PENDING:** Evidence needed to decide a material boundary is unavailable.
  Apply WORKFLOW.md's PARTIAL/BLOCKED rule without inventing a numeric score.
  There is no penalty or NON-FAIL band solely for using relative dates or for
  being near a data boundary.


---

### 2.9 Sample Similarity / Originality (STRONG HARD GATE — Anti-Sample-Copying)

**⚠️ SILENT KILLER. This gate stands alone.** A prompt that is a clone or light paraphrase of any provided sample is not original work and **FAILS here on its own**, no matter how strong every other dimension is. It cannot be waived, averaged away, or excused because the individual asks are feasible and truthful.

**Applicability:** compare only sample prompts or injected-thread examples explicitly supplied for this review. No comparison corpus is bundled. If none are supplied, mark Phase 2.9 **N/A — no comparison samples supplied**, continue the other checks, and do not assign an originality score or claim corpus-wide originality. This absence does not make the review PARTIAL or BLOCKED. If samples are supplied, apply the existing hard gate to demonstrated copying from those samples.

**For the candidate and each supplied sample, compare these fingerprint elements:**

| # | Element | How to extract |
|---|---------|----------------|
| 1 | Core scenario / premise | The one-line situation driving the task (e.g., "reconcile the duplicate-payment alert across finance systems") |
| 2 | Persona + scenario pairing | The acting voice AND whether it is paired with the same situation as a sample |
| 3 | Tight entities | Named channels, vendors, docs, tickets/issue IDs, people, account numbers, amounts, dates reused from the sample |
| 4 | Ask set / deliverables | The specific artifacts the agent must produce and where they land |
| 5 | Service + write combination | The exact mix of services touched and the write actions performed |
| 6 | Workflow shape | The investigation→action structure, branching, batching, stacking pattern |
| 7 | Distinctive phrasing | Sentence-level wording, opening line, signature phrases |

**Comparison table (fill for the closest 1–3 samples):**

| Sample (path) | 1 Scenario | 2 Persona+Scenario | 3 Entities | 4 Asks | 5 Svc+Writes | 6 Shape | 7 Phrasing | Elements matched (/7) |
|---------------|-----------|--------------------|-----------|--------|--------------|---------|-----------|-----------------------|
| `<supplied sample path>` | same/diff | same/diff | same/diff | same/diff | same/diff | same/diff | same/diff | X/7 |

**HARD-GATE thresholds — FAIL if ANY is true against ANY single sample:**
- **Verbatim / near-verbatim reuse:** one or more full sentences (or the opening line) copied or only lightly reworded from a sample prompt or its injected thread.
- **Paraphrase clone:** same core scenario (#1) **AND** same tight-entity core (#3) — the same story about the same records, only reworded.
- **≥4 of 7 elements match** a single sample (structural clone, even if some entities were swapped and wording changed).
- **Persona+scenario lift:** the same persona (#2) paired with the same scenario (#1) **and** the same ask set (#4) as a sample.

**Scoring:**
- **FAIL (1–2):** Meets any hard-gate threshold above — the prompt is a clone or light paraphrase of a provided sample. Non-waivable; cannot be offset by strong scores elsewhere.
- **NON-FAIL (3–4):** Meaningful overlap with a sample (2–3 elements) but scenario, entities, and asks are materially different — it reads as its own task that merely shares a category or a service mix. Flag it and recommend further differentiation.
- **PASS (5):** Distinct scenario, entities, asks, and wording. Shares only the *quality patterns* the samples were meant to teach (natural voice, cross-service friction, embedded difficulty), not their *content*.

**Precision guardrail (mandatory before FAILING 2.9 — avoid over-fire):** When samples are supplied, learning their general quality patterns is permitted. Do **NOT** fail a prompt merely because it:
- uses the **same persona** as a sample on a *different* scenario,
- touches the **same service(s)** or targets the same task category,
- follows the **same investigate-then-act shape** with different content, or
- reuses **generic domain vocabulary** any HarmonyGames task would (standard channel names, common tool nouns, the fixed universe date).

Only FAIL when the *content* is duplicated per the thresholds — scenario + entities + asks, or actual wording. When genuinely unsure, downgrade to NON-FAIL and flag it under Recommended Improvements rather than hard-failing.

---

## PHASE 3: Universe Feasibility

### 3.1 Data Existence Verification

All entity/fact existence was verified in Phase 2.2B (Data Feasibility) and Phase 2.3 (Truthfulness). Phase 3.1 adds one additional check: confirm every verified entity is also **programmatically retrievable via MCP tool queries** (not just present in the raw JSON). Cross-check the `Evals/references/tools/catalog.json` catalog.

- [ ] All core facts verified in Phase 2.2B/2.3 are retrievable via available MCP tools
- [ ] No entity exists only in a file the tools can't query

**Scoring:**
- FAIL (1-2): Key facts/entities can't be retrieved via MCP tools
- PASS (5): All core facts exist and are retrievable

---

### 3.2 Cross-Service Coherence (QC form)

**Check the universe data the task touches, visually and per artifact**, within each artifact and across related artifacts and services. This dimension fails on the **presence** of an inconsistency itself, whether or not it would cause an agent failure and whether or not the contributor introduced it. Synthetic data in HarmonyGames: **Snowflake and Confluence**. Note knock-on effects or a larger pattern with evidence. Use `Appendix - Universe Inconsistency Examples` in the QC spec for examples.

| Category | What fails |
|---|---|
| Temporal Field Inconsistency | Date-bearing fields contradict each other or the task clock (2026-02-14 00:00 UTC or 2025-10-01 00:00 PT), including seeded records dated after the clock |
| Semantic / Category Inconsistency | A categorical or descriptive field does not match the underlying work or entity, or names overlap ambiguously. **A naming overlap is only a defect when it misdescribes a record.** An overlap that the task requires the Agent to reconcile is designed friction, and this stage cannot read the Oracle Events to learn the author's intent, so treat a consistent overlap between two correctly named records as intentional and note it rather than failing it. A field that names the wrong entity is still a defect. |
| Cross-service Referential Inconsistency | The same entity or fact differs across services, or a required reference does not resolve |
| Quantitative / Reconciliation Inconsistency | Line items do not sum to totals; aggregates do not match records |
| State / Lifecycle Inconsistency | A status contradicts the record's activity or related records |
| Identifier / Uniqueness / Format Inconsistency | IDs are malformed, null, duplicated or follow mixed schemes within a service |
| Other Universe Inconsistency | Any other internal inconsistency |

**Scoring (QC form):** FAIL (1–2) for any inconsistency above; NON-FAIL (3) for a single low-impact inconsistency that does not affect solvability or storyline coherence (for example a plausibly intentional, consistently applied ID-format variation); PASS (5) when the task-touched data is consistent. A State / Lifecycle inconsistency (a closed ticket with later activity) or a Quantitative one (line items that do not sum to the total) always fails, even when no agent would miss it; neither qualifies for the low-impact NON-FAIL.

The task-state checks below still apply and feed the same dimension.

Read supplied SQL to identify the proposed sources relevant to the prompt.
After confirmed no injection, mark SQL-specific checks N/A and assess the base/reference-file task.

Apply `WORKFLOW.md`'s **Stage ownership and evidence reuse** contract. A matching
`injection-static-v2` PASS / COMPLETE report can satisfy its static integrity
checks. Cite the reused check IDs and validated dependencies; do not repeat the
full ID-collision, SQL-structure or cross-service data audit. If that report is
missing or stale, inspect task-relevant proposed records directly. A complete
standalone injection audit is not a prerequisite for `/prompt`.

This stage still checks what the injection review does not:

- The prompt incorporates any source-based requirements unambiguously.
- Required base/proposed sources and their relationships support the requested
  actions and conclusions, under the assigned persona's applicable access rules.
- Natural task anchors and cataloged paths reach the necessary sources.
- Applicable dynamic-context and error/async configuration align with that path;
  a forced error must not remove the only valid route or mask an intended denial.
- Any newly discovered data contradiction materially affects task solvability
  or a factual premise. Report it and reopen affected reused checks; do not
  suppress a defect because an earlier report passed.
- Task-relevant proposed records are free of duplicate and conflicting data:
  no two injected records share key fields with conflicting values; no injected
  record contradicts established base data (a person active in one service and
  departed in another, conflicting contact details); and new records do not
  predate or conflict with existing activity, milestones or message timestamps.
- Every message the SQL adds to a Slack channel has an author who is a member of
  that channel, and every apostrophe inside a quoted SQL string is doubled
  (`don''t`). Either failure is a demonstrated inconsistency (FAIL). Inspect the
  SQL text only; never execute it.

| Prompt ask / source | Static evidence NEW or REUSED | Prompt-specific discovery/access/configuration evidence | Task coherence |
|---|---|---|---|
| ... | Source/report/check IDs | ... | PASS / FAIL / PENDING / N/A |

A demonstrated inconsistency in task-touched data, or a configuration mismatch
that prevents a valid solution, is **FAIL** (one minor inconsistency is NON-FAIL
as above). A task-relevant inconsistency that cannot be resolved from available
evidence remains PENDING. Records the task never touches and injection-wide
integrity are outside this stage. PASS requires all applicable checks supported;
it does not imply every universe record was re-audited.

---

## PHASE 4: Final Evaluation

### 4.1 Final Scoring Table

**Score each sub-dimension per `Evals/references/rules/scoring.json` definitions.** Every row below resolves to exactly one `scoring.json` entry. Seven of them are short forms of a longer canonical name:

| This table | `scoring.json` |
|---|---|
| Clarity & Specificity | Prompt Clarity and Specificity |
| Contrived / Unnatural | Contrived or Unnatural Prompt |
| Tool Use & Cross-service | Tool Use and Cross-Service Requirement |
| Investigation + Action | Investigation |
| Coherence (Bolt-on) | Coherence |
| Complexity Dimensions & Data Seeding | Complexity Dimensions and Data Seeding |
| Data Exists | Universe Feasibility (Data Exists) |

Each band below is the one its own phase defines; where a Local Override removed a middle band, the band here is binary.

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|-----------|--------------|-------------|---------------|
| Prompt | Unique Ground Truth | 1–2 / 5 (binary; no scored 3–4 band) | Cite the completed two-reading comparison and its resolution |
| Prompt | Feasibility | 1/5 (binary; the middle band is removed by the Local Override in 2.2) | ... |
| Prompt | Persona ACL Reachability | 1/5 (strong hard gate, 2.2E; a single unreachable required scoped read is a standalone FAIL) | ... |
| Prompt | Explicit Tool Mention | 1/5 (binary per the Local Override) | ... |
| Prompt | Clarity & Specificity | 1/3/5 | ... |
| Prompt | Contrived / Unnatural | 1/5 (binary; a spec-like or polished draft fails) | ... |
| Prompt | Alignment with Today's Date | 1/5 or PENDING (2.8 defines no NON-FAIL band) | ... |
| Prompt | Originality / Sample Similarity | 1/3/5 when samples are supplied; otherwise N/A | ... |
| Prompt | Truthfulness | 1/5 (binary; one loose descriptor error fails) | ... |
| Prompt | Tool Use & Cross-service | 1/5 | ... |
| Prompt | Investigation + Action | 1/5 | ... |
| Prompt | Coherence (Bolt-on) | 1/5 | ... |
| Prompt | Persona | 1/3/5 | ... |
| Prompt | Business Function | 3/5 | ... |
| Prompt | Assigned Competency | 1/5 or PENDING | ... |
| Prompt | Assigned Task Skill | 1/5 or PENDING | ... |
| Prompt | Complexity Dimensions & Data Seeding | 1/5 | ... |
| Universe | Data Exists | 1/5 | ... |
| Universe | Cross-Service Coherence | 1/3/5 | QC form categories on task-touched data, plus task-state checks |

**Grading Rules:**
- Exclude properly marked N/A checks from aggregation. In particular, no supplied sample corpus means Phase 2.9 is N/A, not an unsupported PASS or a blocker. Required unverified checks still follow `WORKFLOW.md` § "Ruthless grading standard": a provisional NON-FAIL does not certify a disputed gate, and PASS requires its applicable evidence.
- Grade to the LOWEST dimension across all sub-dimensions
- If ANY sub-dimension meets Fail criteria → the prompt FAILS
- If no fails but ANY sub-dimension is Non-Fail (3-4) → the prompt is NON-FAIL
- ALL applicable scored sub-dimensions must be 5 for the prompt to PASS
- Every scored UGT verdict requires §2.1's completed comparison and matching generated report section, regardless of the overall verdict. A single coherent procedure or leading reading cannot justify UGT PASS.

---

### 4.2 Final Verdict

Apply `WORKFLOW.md` verdict precedence: a demonstrated failure remains FAIL;
required unresolved checks with no demonstrated failure produce NON-FAIL
with PARTIAL/BLOCKED status and no numeric score. PASS requires COMPLETE.

```
## PROMPT EVALUATION REPORT

### Task: [Brief description]
### Assigned Persona: [Name - Role]
### Assigned Business Function: [supplied value]
### Assigned Competency: [supplied value]
### Assigned Task Skill: [supplied value]
### Assigned Horizon: [supplied value]

---

### Injection Gate
- State: [NOT_USED / CURRENT / STALE → rerun / NEVER_REVIEWED → run]
- Reviewed SQL sha256: [...]  Eval 0 verdict: [...]
- Eval 0 findings on records this prompt depends on: [none, or each one and where it is scored]

### Phase 1: Prompt Structure & Persona

**Persona:** [PASS/NON-FAIL/FAIL]
- Justification: [...]

**Assigned Competency:** [PASS/FAIL/PENDING]
- Justification: [...]

**Assigned Task Skill:** [PASS/FAIL/PENDING]
- Justification: [...]

**Complexity Dimensions:** Ambiguity [Y/N] · Dynamic Change [Y/N] · Multi-Source [Y/N] — [PASS/FAIL]
- Data seeding: [PASS/FAIL]
- Justification: [...]

**Naturalness:** [PASS/NON-FAIL/FAIL]
- Justification: [...]

**Anti-Patterns:**
| Pattern | Status |
|---------|--------|
| Command List | PASS/FAIL |
| Bolt-On | PASS/FAIL |
| Pre-Solving | PASS/FAIL |
| Tool Mention | PASS/FAIL |

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** [PASS (5) / FAIL (1–2) / PENDING — no score]

[For a scored UGT verdict, insert the complete section generated by
`python3 Evals/tools/hg_prompt_checks.py render-ugt [record-path]` verbatim.
It must include the two-reading comparison even when UGT passes within an
overall FAIL. Synchronize this verdict and the scoring-table row with the
saved comparison. For missing required evidence, state the missing checks
and next action under the existing provisional-report rules.]

[Findings for every other sub-dimension with scores and evidence]

---

### Phase 3: Universe Feasibility

**Data Existence:**
- Entities verified: [X of Y]
- All retrievable via MCP: [Yes/No]

**Cross-Service Coherence:** [PASS/NON-FAIL/FAIL]
- Inconsistencies in task-touched data: [category - artifacts - evidence, or None]
- Injection SQL considered: [Yes / N/A — user confirmed no injection]
- Static integrity evidence: [REUSED with report/check IDs / direct task-relevant checks / N/A]
- Prompt-specific sources, access and configuration: [supported / issues]

---

### Phase 4: Final Evaluation

**Scoring Table:**
[Include the completed scoring table from 4.1]

---

### Issues Found (if any):

| # | Issue | Severity | Dimension |
|---|-------|----------|-----------|
| 1 | ... | Major/Moderate/Minor | ... |
| 2 | ... | ... | ... |

---

### Recommended Improvements (if any):

1. [Specific, actionable suggestion]
2. [Specific, actionable suggestion]

---

## Deep Recheck

[Phase 5 section, in the format set by references/rules/deep_recheck.md]

### FINAL VERDICT: [PASS / NON-FAIL / FAIL]

Score: [supported integer 1–5; omit this line for provisional NON-FAIL]

Execution status: [COMPLETE / PARTIAL / BLOCKED]

Evaluator model: [e.g. Opus 5.5 (claude-opus-5-5), xhigh effort]

Next action: [specific next step, or None]

Evidence limits: [missing/deferred checks and scope, or None]

**Lowest Dimension:** [Dimension - Score - Reason]

**Summary:** [2-3 sentence justification]
```

The report is saved once, after Phase 5. The verdict block is the last part of
`## Deep Recheck` and is the report's only verdict block; it carries the score
after the recheck.

---

## PHASE 5: Deep Recheck

Save the check record with `hg_write_output.py prompt-checks` first. Do not save
the report yet. Follow [deep_recheck.md](references/rules/deep_recheck.md):

1. Start passes P1–P4 at the same time, each as a fresh subagent that cannot see
   the check record or this session's findings. Each checks one topic on every
   prompt sentence and returns quoted findings. Rerun any pass that does not
   return a usable result until it does.
2. Open every record a finding cites. Mark each finding CONFIRMED or REJECTED
   with a reason. Do not accept a finding on the pass's word. A UGT finding is
   REJECTED only by quoting a prompt sentence or persona-visible record that
   rules out Reading B; otherwise it stays CONFIRMED. A fork that meets every
   both-fair figure condition (§2.1) is recorded as BOTH_FAIR_FIGURE instead. A
   `PLATFORM:` finding is recorded, not scored.
3. Put each confirmed finding into the check record under its existing rule:
   Truthfulness as a premise check, UGT in `unique_ground_truth`, any other
   dimension in `other_failures`. Rescore under Phase 4. A confirmed fail-level
   finding makes the verdict FAIL.
4. Save the record with `prompt-checks` again. Check every rewrite under
   Recommended Improvements as deep_recheck.md step 5 says, then save the
   report. It ends with `## Deep Recheck` (with the fork list), whose last
   part is the only verdict block.

When the review stopped as PARTIAL or BLOCKED for missing inputs, skip the
passes; `## Deep Recheck` says why, then gives the verdict block.

---

## Quick Reference: Common Mistakes to Catch

| Mistake | How to Detect | Severity |
|---------|---------------|----------|
| Phantom entity / tight identifier | Asserted existing entity or tight ID is confirmed absent from local records, SQL and applicable task attachments | Major (Truthfulness) |
| **False state premise** | **A stated claim about current state ("still no reply", "hasn't been merged", "rolling window", "assigned to me") is contradicted by the universe — greps clean but breaks the task. Includes work that assumes normal operations after the Feb 11 shutdown announcement (Feb 14 tasks only), a person who has left reviewing, approving or replying (#43), or, on an Oct 1 task, anything that does not exist yet by 2025-09-30 23:59:59 PT** | **Major (Truthfulness)** |
| Wrong relationships | Verify preparer→reviewer→approver and entity/portfolio mappings against supplied assignment context and local records | Major (Truthfulness) |
| Pre-solved prompt | Root cause stated in prompt | Major (Pre-Solving) |
| Bolt-on asks | Remove sentence test - rest still makes sense | Major (Coherence) |
| Command list | Sequential instructions present | Major (Command List) |
| Single-service task | Only one service needed, or a second service changes no graded fact | Major (Cross-Service) |
| No write action | Only investigation, no action | Major (Investigation+Action) |
| Contrived difficulty | Arbitrary precision requirements | Major (Contrived) |
| **Spec-sheet register** | **~600-word prompt that enumerates each deliverable's contents + preservation rules + reply format (2+ triggers) — natural scenario, unnatural voice** | **Major (Contrived)** |
| Persona mismatch | Request outside persona's scope | Major (Persona) |
| Persona ACL violation | Prompt requires (or directs) reading scoped-service data outside the persona's view — scoped set derived live from the `Evals/references/persona/acl.md` Access matrix; no affirmative-denial or authorized alternate | Major (Feasibility) |
| Ambiguous end-state | Two supported readings require different decisions, writes or contents, and prompt/source authority does not resolve the choice (a both-fair figure under §2.1 passes instead) | Major (Unique Ground Truth) |
| Action decision ambiguity | Two readings → different write actions (or write vs no-write / act vs defer) | Major (Clarity - 06/09) |
| Wrong business function | Category doesn't match the task categories | Non-Fail (Business Function; the QC form has no fail option) |
| **LLM-sounding or spec-like prompt** | **Document formatting, polished connectives, or a deliverable spec — even when the situation is real** | **FAIL (Contrived)** |
| **Staged errors** | **Misspellings, made-up emoji or broken punctuation planted to look human (#11); clean writing is fine** | **FAIL (Contrived, local override)** |
| **Trap hint or riddle** | **Wording that points at the trap without naming it (#31); naming the symptom is fine** | **FAIL (Contrived, local override)** |
| **Hidden destination** | **The persona would know where the output goes but the prompt hides it (#42, #47, #44)** | **FAIL (Contrived)** |
| **Audit form or if-chain** | **Reads like an audit or compliance form (#1, #43), or long if / but-not / then-also chains dictate per-case actions (#44)** | **FAIL (Contrived)** |
| **Opaque IDs / generated filenames / exact timestamps** | **Full agent IDs, hash-like IDs, generated filenames or exact timestamps a person would not type, when not necessary** | **FAIL (Contrived)** |
| **MCP server or "tool" wording** | **"use the Linear MCP server", "use the GitHub tool"** | **FAIL (Explicit Tool Mention, local override)** |
| **Universe inconsistency** | **Task-touched data contradicts itself or the clock (dates, categories, references, totals, states, IDs)** | **FAIL, or Non-Fail for one minor that is not a lifecycle or sum mismatch (Cross-Service Coherence)** |
| **Broken injected message** | **An added Slack message whose author is not in the channel, or an undoubled apostrophe inside a quoted SQL string** | **FAIL (Cross-Service Coherence)** |
| **Wrong competency** | **The scenario belongs to a different competency than the assigned one** | **Major (Assignment — HARD GATE 1.5)** |
| **Missing assigned task skill** | **The assigned task skill is not a real part of the work** | **Major (Assignment — HARD GATE 1.5)** |
| **No complexity dimension** | **Prompt is a fully specified recipe with no env-resolved gap, no discovery-order shift, and no 3+ source split** | **Major (Complexity Dimensions — HARD GATE 1.5)** |
| **Unseeded spec-sheet prompt** | **Prompt restates operating details that live, or should live, in injected Slack/mail/docs/tickets** | **Major (Data Seeding — HARD GATE 1.5)** |
| Lacks diversity | Yet another "investigate + post one Slack message" pattern | Flag (Diversity) |
| **Sample clone / copied prompt** | **Candidate duplicates an explicitly supplied sample — same scenario+entities, ≥4/7 fingerprint elements, persona+scenario+ask lift, or verbatim/near-verbatim sentences** | **Major (Originality — STRONG HARD GATE 2.9)** |
| **Impossible dimensional breakdown** | **Prompt asks for a per-X split (per-state, per-vendor, etc.) but the universe data has no field for that dimension** | **Major (Feasibility)** |
| **UGT false PASS from one coherent reading** | **Challenge the strongest plausible alternative and every explicit option; require actual resolving authority or the same material decision, writes and contents, not only the same destination** | **Check before PASS (UGT)** |
| **UGT over-fire on wording variation** | **Candidate readings differ only in wording or source-authorized alternatives, with no materially incompatible required outcome — apply the two-reading precision guardrail without later rubrics/runs** | **Required before PASS or FAIL (UGT)** |

---

## Evaluation Mindset

- **Be skeptical** — assume claims are wrong until verified against universe data
- **Be objective** — score from `Evals/references/rules/scoring.json` definitions, not personal judgment
- **Be diversity-aware** — flag prompts repeating the "investigate + post one Slack message" pattern (see `Evals/references/rules/task_categories.md`)
- **Be persona-bound** — bind the assigned roster identity and supported read access; actual runner/verifier execution belongs to reviews of those runs
