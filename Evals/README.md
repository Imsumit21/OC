# HarmonyGames direct-search evals

This bundle reviews tasks using local exported universe records. It needs
Python 3 and local file access, with no `/setup`, deployment or live MCP connection.

**Two-universe update — 2026-10-20 (`dual-universe-v1`):** Every task now names
its date first: **Oct 1, 2025 (synth-cut)** or **Feb 14, 2026 (normal)**. Each
skill asks before anything else and saves the answer with
`tools/hg_store_input.py universe <answer>`; there is no default. The date picks
`Universe_SynthCut/` (`hg4-synth-sep30cut` v16, clock 2025-10-01 00:00 PT) or
`Universe_Normal/` (`hg4-2026-08-31` v37, clock 2026-02-14 00:00 UTC); search,
lint and review tools refuse to read the universe until it is saved, and new
reports carry a matching `Clock:` line. The February 11, 2026 shutdown rules
apply to Feb 14 tasks only; on Oct 1 the company runs normally, people who had
already left (Victor, April 2025) are still gone, and nothing after
2025-09-30 23:59:59 PT exists. See ENVIRONMENT.md **Task date and universe**.

**Task-quality update — 2026-10-18 (`task-quality-v1`):** From the 50-task QC review
(2026-10-17). Prompt: staged typos, trap hints/riddles, hidden destinations,
audit-form prompts and long if-chains fail Contrived; clean writing is fine; a
narrow `BOTH_FAIR_FIGURE` UGT pass when only one reported figure differs and
both values are on persona-visible records (every other fork unchanged).
Rubric: every row needs a `valid_case` it accepts and a `do_nothing_case` it
rejects; Overly Broad is Major; PT/UTC dates accept either day; anonymized
tokens bind literally; rows map to OE steps and OE conflicts are recorded
(format 5). OE: every Expected-line value needs a quote, absence claims need a
search. Injection: run `tools/hg_injection_lint.py` (future-dated records, ID
contracts, unreadable Drive files, duplicate accounts, grader-facing text,
padding comments). Dates are written in PT; on a Feb 14 task "today" is Saturday,
February 14, 2026 and the clock is 2026-02-14 00:00 UTC. See the Local Overrides in Evals 1
and 3. Older records keep their release and need a fresh review.

**Unique Ground Truth update — 2026-09-30 (`prompt-ugt-v1`):** Every scored
UGT verdict now requires a source-bound comparison of concrete outcomes,
including PASS within an overall FAIL. Prompt check records use format 2;
`hg_prompt_checks.py render-ugt` generates the section required by the saver.
Judges must test the strongest plausible alternative and account for every
listed option. One coherent procedure or a shared destination cannot establish
PASS 5. See [Eval 1 §2.1](1_Prompt_Eval.md#21-unique-ground-truth) and the
[record contract](references/rules/prompt_rubric_reliability.md).
Refresh Evals.zip and claude.zip together. Older records retain their original
release and require a fresh review before being issued under this one.

**Service update — 2026-09-23 (`service-availability-v1`):** Snowflake and
Confluence are confirmed live. Tasks may use their cataloged operations; the
older ACL omission alone does not fail or block a review. Actual task-specific
restrictions still apply. See [ENVIRONMENT.md](ENVIRONMENT.md#live-service-availability).
Use the refreshed Evals.zip and claude.zip together and reload the project to
replace stale instructions. Earlier failures based on the retired-service rule
need reassessment; other findings remain independently assessable.

## Installation

ZIP each of the five folders separately, preserving the folder itself. Extract
all five together as siblings in one workspace. Each upload ZIP must be below 5 GB. See [UNIVERSE_MAP.md](UNIVERSE_MAP.md).
Have the agent run `python3 claude/install.py` from that workspace once to
register project-local skills and persistent input instructions. It creates
relative links under `.claude/`, never changes global settings, and refuses
conflicting files. Reload Claude's project if skills are not discovered yet.
The user does not need to run the input or search helpers manually.

## Commands and outputs

| Command | Fixed output path |
|---|---|
| `/injection` | `Evals/task_inputs/reports/0_injection.md` |
| `/prompt` | `Evals/task_inputs/reports/1_prompt.md` |
| `/hardness` | `Evals/task_inputs/reports/1a_hardness.md` |
| `/oe` | `Evals/task_inputs/reports/2_oe.md` |
| `/rubric` | `Evals/task_inputs/reports/3_rubric.md` |

Run each stage through its individual command. Bare commands ask for missing
inputs in chat. Supplied inputs and uploaded references are saved automatically;
a newer version replaces that input only.
Each workspace is one task. Reruns replace the matching report. Files appear
only after the corresponding writer succeeds, not during input collection.
See [INPUTS.md](INPUTS.md) for saving/reuse and [WORKFLOW.md](WORKFLOW.md) for
the exact stage inputs, scoring/report contract and optional SQL handling.

`/rubric` evaluates an existing rubric only; `/rubric audit` is an alias.
It reports scores, evidence and suggested fixes without rewriting criteria or
producing a prefill. `/rubric create` and the former prefill writer routes are
retired. Use the actual rubric, prompt and applicable task/source context.
A supplied OE is a comparison reference; no OE PASS is required.
Under `rubric-revision-v10`, executable factual checks and six static QC dimensions
are unchanged. Local `hg-strict-overrides-v1` (2026-09-26) supersedes the QC
workbook on severity, negative framing, title-only self-containment, cascading
overlap and a predicted all-fail gate; see the table at the top of Eval 3. The workflow is `rubric-eval-only-v1`; verifier/all-failing inputs
remain outside this stage. OE does not require
rubrics. Hardness needs the prompt and one unhinted run JSON (Opus preferred, Haiku
fallback), with optional SQL.
Prompt-reference attachments are supported; `/injection` takes SQL only.
`/prompt` requires the exact prompt plus persona, business function, competency,
task skill, and horizon. Saved values are reused; missing assignment fields are
collected before evaluation starts.
Injection is optional downstream and is never executed by these evals.
`/injection` checks records/IDs, SQL structure and data consistency only. It has
no numeric/difficulty score, style gate or live-search requirement. A static
PASS does not certify deployment compatibility. `/prompt` owns task discovery
and feasibility; `/hardness` owns observed or predicted Opus difficulty. Rerun injection reports
from before `injection-static-v2` before reusing them under the new scope.

## Stage boundaries and reusable facts

`/prompt` checks request quality, design requirements and feasibility without
later OE/rubric/run inputs. `/hardness` uses `model-aware-v3`: assess one
unhinted Opus run directly, or use a Haiku fallback to predict Opus difficulty
through transfer checks. Name the actual run model and assessment mode. Haiku's
failure severity alone cannot establish Opus difficulty; disclose prediction
limits, with no numeric pass-rate forecast. Task/tool defects never establish
model hardness. Scores 1–2 HOLD; supported 3–5 PROCEED, predictively for Haiku.
Insufficient evidence is unscored provisional NON-FAIL with HOLD. The author
supplies the selected run; HOLD never blocks obtaining a needed run. Older Haiku
runs can be reassessed without backfill. A later matching Opus run is preferred
and assessed afresh. Load only the matching eval: [Opus](1A_Hardness_Eval.md)
or [Haiku prediction](1B_Haiku_Prediction_Eval.md). These are two internal paths
of the same `/hardness` command and write the same report.
OE checks the actual critical path; rubric checks the actual criteria.

Stages reuse verified source facts/checks only when the relevant input/source
fingerprints, rules and coverage still match. New claims and changed artifacts
still get their own checks. See [WORKFLOW.md](WORKFLOW.md#stage-ownership-and-evidence-reuse).
This adds no user inputs or download paths; metadata stays in stage reports and
the existing input manifest. Old PASS labels alone cannot establish reuse.

## Search and evidence

Start with [EXECUTION.md](EXECUTION.md), then [ENVIRONMENT.md](ENVIRONMENT.md),
[SEARCH.md](SEARCH.md) and the selected
numbered Eval. `tools/hg_search.py` inventories service files, searches JSON
with bounded output and reads exact JSON pointers without loading whole large
exports into memory. Batch related terms with `search-many` and complete ID checks with `lookup`.
Read several already discovered file/pointer pairs together with `get-many`,
retaining each record's paging, errors and evidence requirements. Targeted
batch searches use verified offsets when efficient; broad batches keep one scan.
Ordinary scoped searches and record reads automatically validate matching
prepared GitHub/GDrive/Linear/Snowflake indexes on first use, then reuse them.
Other sources use existing scan paths. Compact routing and complete raw-record
caching are shared across supported service exports. No extra setup command is
needed; index construction remains optional. Results keep citations, errors and
coverage, and grading requirements remain unchanged.
Use `tools/hg_context.py <stage>` for the canonical scoring groups of one stage.
Search results are not filtered by persona; use the unchanged
ACL policy and actual source metadata to assess Agent visibility.

The latest supplied tool catalog lists 298 declared tools. It describes task
capabilities, not local evaluator commands. Local files cannot certify live
retrieval ranking, write success or runtime ACL enforcement. Required unsupported
checks within the selected stage's scope remain PENDING; missing evidence is
not a quality FAIL. `/injection` lists unavailable live behavior and unverified
schema compatibility as outside-scope limits. The injection SQL schema remains
an unverified snapshot; see `references/schema/README.md`.
The refreshed archive includes populated GCal and GSlides exports.

## Reports

Every stage uses `### FINAL VERDICT:` with PASS, NON-FAIL or FAIL, a separate
numeric Score line only when supported, execution status, evaluator model,
next action and evidence limits. Required unresolved checks without a proven failure use
NON-FAIL with PARTIAL/BLOCKED and no numeric score. Proven failures remain FAIL;
PASS requires COMPLETE. Existing completed scoring bands are unchanged.
NON-FAIL must remain distinct in taxonomy parsing; provisional results do not
clear gates.

The agent saves reports through `hg_write_output.py`, inputs through
`hg_store_input.py`, and uses `hg_preflight.py` only for explicit task-folder
reviews. The source archive and old base folders are not required at runtime.

Individual record checks can reuse unchanged evidence across renamed/reordered
requests. Exact-ID lookups can use verified prepared indexes for GitHub, Linear
and GDrive; other scopes retain the complete scanner. Large Gmail routing lists
use a bounded lossless cache. `hg_reference.py guide` can include the full
requested route/schema views in the same call. Include both
`Evals/references/universes/` (both universes' indexes) when zipping;
exclude disposable runtime caches. See `Evals/SEARCH.md` for scope and freshness
rules. No scoring check or instruction is shortened by these optimizations.

Oracle Events replace golden evaluation under `oracle-events-v2`. Use `/oe`
with `08_Oracle_Events.md` (key `oe`). Following the Oracle Events guideline,
a missing or wrong step FAILs (2); minor, non-action and final-response defects
are NON-FAIL 3; a clean set is PASS 5. The overall result is the minimum of
completeness and accuracy. OEs describe a supported critical path, not final-response prose.
Update both packages, rerun `claude/install.py`, and reload the project. The
installer retires only its managed golden link. Historical golden inputs and
reports are preserved and never converted automatically.

OE path checks (`oracle-events-v2`) now validate tool/parameter contracts, source
values and step-to-step consistency. They assess whether the supplied path can
complete the task with the persona's access and supported capabilities. `/prompt`
retains task design and overall feasibility. A broken OE does not prove the task
impossible. The report separates path feasibility from task solvability, without
adding a QC score or changing prompt/rubric grading. Replace Evals/ and claude/
together and rerun `python3 claude/install.py`; earlier reports stay historical.
