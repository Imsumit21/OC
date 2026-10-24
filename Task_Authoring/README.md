# Task_Authoring — HarmonyGames task authoring bundle (V3 assignments · extreme-hardness engine)

The authoring half that sits beside the sandbox's evaluation half (`Evals/` +
`claude/`). It designs and builds every part of a task —
above all an **extremely hard, broad, long universe injection** — including the prompt,
Oracle Events and rubric criteria, and checks them before the official evals run.

V3 changed-topic rules in `references/Docs/11_V3_Changes.md` supersede conflicting
V2/taxonomy/Evals text. Unchanged V2 rules still apply. The bundle preserves its
local model-authorship allowance and existing extreme/normal hardness targets;
these are explicit local choices (`setup/GEN_EXECUTION.md` § 2 and § 3a). The user
handles Eval Portal reviews and proof uploads outside this local pipeline.

## The two rules that shape everything

1. **Claude or Codex may author every artifact.** The prompt, the Oracle Events and the rubric
   criteria may be drafted and revised by Claude or Codex as well as by the human. For those three,
   the bundle writes a prep artifact from the universe, a draft on request, and a check.
   The platform still screens prompts with its AI-text detector. Details:
   `setup/GEN_EXECUTION.md` §2. This preserved local exception differs from the official
   V3 human-authorship rule.
2. **Hardness is measured, not claimed.** A task is designed (`/create-scenario`) before
   any SQL is written, declared in a machine-checkable manifest, and verified against
   the SQL by `tools/hardness_gate.py`. The default targets (`GEN_EXECUTION.md` §3a):
   **≥ 10 of 13 services carrying weight, ≥ 500 necessary agent calls (plan ~600), ≥ 120 injected
   rows, asks spread over ≥ 12 fragments in ≥ 7 services and ≥ 10 containers, 2–4 hidden
   authorities with decoys, ≥ 3 independent forensic chains, ≥ 12 traps.** The levers
   come from measured Opus behaviour (`references/Hardness_Mastery.md` §0), not from
   stacking easy steps. The targets remain unchanged for an Easy assignment; the
   assigned empirical cap is a separate measurement.

## Install

From the workspace root that holds `Evals/`, `claude/`, `Task_Authoring/` and the
three `HarmonyGames_*` folders:

```sh
python3 Task_Authoring/setup/install.py --target both --dry-run  # preview Claude + Codex
python3 Task_Authoring/setup/install.py --target both            # register both
python3 Task_Authoring/setup/uninstall.py --target codex         # remove only Codex links
```

`--target claude` registers `.claude/skills/`; `--target codex` registers
`.agents/skills/`; `--target both` registers both. Omitting `--target` keeps the
original Claude-only behavior for install and uninstall. Both scripts support
`--dry-run`, reject redirected registry directories, and preserve unrelated files.
Install checks all selected destinations for conflicts before creating any links.

All 11 skill folders stay in `Task_Authoring/skills/`; both registries contain
relative folder symlinks, for example:

```text
.claude/skills/create-scenario -> ../../Task_Authoring/skills/create-scenario
.agents/skills/create-scenario -> ../../Task_Authoring/skills/create-scenario
```

Launch Codex with this workspace root as its working directory. Invoke
`$create-scenario`, `$create-prompt-writing draft`, or
`$create-rubric-writing check`. The `/create-*` examples throughout this bundle
use Claude's spelling; use `$create-*` in Codex with the same arguments. The
`/injection`, `/prompt`, `/hardness`, `/oe` and `/rubric` reviews remain Eval Portal
steps handled by the user. Authoring with Codex does not change the required
Opus 5.5 pre-check and baseline runs.

The scripts follow the folder they live in, so the bundle folder may carry another name;
the paths below write it as `Task_Authoring/`.

Reload the project if the commands are not discovered. Then start a task:
`cp -R Task_Authoring/references/Tasks_Template/. Task_Authoring/task_inputs/` and
paste the eight-field assignment exactly into `00_Assigments.md`: business function,
persona, role, competency, task skill, task type, difficulty mode and universe date.
The emoji-labelled paste and nested `Role:` line are accepted. Normalize it, then
validate the source before any universe grounding:

```sh
python3 Task_Authoring/tools/task_context.py --task-dir Task_Authoring/task_inputs --write
python3 Task_Authoring/tools/task_context.py --task-dir Task_Authoring/task_inputs --write --require-source
```

Commands share `Working_Files/00_Task_Context.json`; use the same `--task-dir` for
every direct tool command in another task workspace (or set
`TASK_AUTHORING_TASK_DIR` for that shell). Stage gates retain their positional
task directory and propagate it. Normalization does not change shell state.
`references/universe_sources.json` maps both freeze dates to the same local universe
data and shared KB. Archive labels describe source provenance, not the assigned
clock. No separate October export or date-specific KB build is required. Validate
each relied-on fact at the assigned freeze: later events cannot be completed facts,
and mutable content edited later needs a dated version or independent earlier evidence.
The displayed time remains traceable; the V3 freeze is the assigned date at 00:00 UTC.

Role, freeze and mode are enforced separately. Correct the rubric and re-grade
before measuring difficulty: Easy must average <90%, Medium <85%, Hard <70%; equality
fails. Five or more fully passing baseline rollouts fails. Pre-check and baseline runs use Opus 5.5.

## Commands

Platform slots (`01_Universe_Inject.sql`, `02_Reference_Files/`, `03_Error_Async_Config.txt`,
`11_AF_Justification.md`) are written at the top of `task_inputs/`; every other file a command
writes goes to `task_inputs/Working_Files/`.

| Command | Writes | Then |
|---|---|---|
| `/create-scenario` | `01_Scenario_Design.md`, draft `01_Hardness_Manifest.json` (+ optional `01b_Redteam_Review.md`) | `/create-injection` |
| `/create-injection` | `01_Universe_Inject.sql`, `01_Grounding_Dossier.md`, final `01_Hardness_Manifest.json` | `/injection` |
| `/create-hardening` *(advanced)* | `01a_Hardening_Report.md` (+ hardened SQL) | `/injection`; human revises prompt if needed |
| `/create-reference-files` *(optional)* | `02_Reference_Files/`, `02_Reference_Files_Manifest.md` | — |
| `/create-error-async` *(optional)* | `03_Error_Async_Config.txt` | — |
| `/create-prompt-writing` | `04_Prompt_Writing_Brief.md` (+ `04_Prompt.txt` draft on request) | `04_Prompt.txt` (Claude, Codex or human) |
| `/create-prompt-writing check` | `04_Prompt_Check.md` | `/injection` + `/prompt` |
| `/create-humantime` | `05_Human_Time_Worksheet.md` | Opus 5.5 pre-check → `/hardness` |
| `/create-oe-writing` | `08_OE_Writing_Ledger.md` (+ `08_Oracle_Events.md` draft on request) | `08_Oracle_Events.md` (Claude, Codex or human) |
| `/create-oe-writing check` | `08_OE_Check.md` | `/oe` |
| `/create-rubric-writing` | `09_Rubric_Writing_Plan.md` (+ `09_Rubrics.json` draft on request) | `09_Rubrics.json` (Claude, Codex or human) |
| `/create-rubric-writing check` | `09_Rubric_Check.md` | `/rubric` |
| `/create-allfail` | `11_AF_Justification.md` | Rate All-Fail Rubrics screen |
| `/create-difficulty` | `12_Difficulty_Stats.txt` | Difficulty check screen |

Every command is blocked at handoff until `python3 Task_Authoring/tools/stage_gate.py <stage> Task_Authoring/task_inputs --paste` prints PASS (stages: scenario, injection, hardening, reference-files, error-async, prompt-writing, prompt-check, humantime, oe-writing, oe-check, rubric-writing, rubric-check, allfail, difficulty).

Full flow, gates and loop-backs: `Guide/How_To_Author_A_Task.md`. Copy-paste
equivalents of every command: `Guide/Manual_Commands.md`.

## Tools (local, no network unless stated)

| Tool | What it does |
|---|---|
| `tools/task_context.py --task-dir <task_dir> --write [--require-source]` | Parses the exact eight-field paste, resolves persona and canonical freeze, binds assigned mode/cap and the shared universe source before grounding; writes `Working_Files/00_Task_Context.json`. Both freeze dates use the same data |
| `tools/hg.py search` · `records` · `reference` | The Evals search helpers (same commands as `Evals/SEARCH.md`), run from patched copies so their caches land in `support/local_search/cache/` — never in the read-only `Evals/`. Use it for every universe lookup |
| `tools/base_check.py <sql>` | `/injection` Checks A + C against the base data: new ids free, every reference resolves (channel, user, thread parent, issue, PR, mailbox thread, calendar, board/list/card, page, Drive parent), UPDATE targets exist, Slack/Gmail id contracts, replies after parents, events end after start; warns on PR comments missing their Slack mirror copy |
| `setup/extract_schema.sql` | Read-only SELECTs to run in Universe Explorer: tables/columns/types, constraints, indexes, enums, triggers, row counts. Save Q1 as `references/universe_schema_live.json` and the linter uses it |
| `tools/shortcut_probe.py <persona> <values>` | Searches every persona-visible service (plus the SQL overlay) for one record holding ≥ 3 of the task's acceptance values or ≥ 50% of a population's keys — a shallow answer source that collapses the task; required by the rubric-writing gate |
| `tools/stage_gate.py release <task_dir>` | Final gate before submit: every stage PASS current, one bundle digest over prompt/OEs/rubric/SQL/files/config/manifest, no PROVISIONAL/UNRESOLVED/UNVERIFIED left, OE route supported, difficulty passing, pre-check trajectory present → `13_Release_Gate.txt` |
| `tools/sql_lint.py <sql>` | Static lint against the live 144-table platform schema (`references/universe_schema_live.json`) and the clock: unknown tables/columns, missing NOT NULL values, post-clock timestamps, created > updated, duplicate ids, the line-1 inject marker; coverage stats per schema |
| `tools/hardness_gate.py <manifest> <sql>` · `--design` | Checks the hardness manifest against the SQL itself (every cited id must be in the SQL; every injected schema must be used): breadth, volume, cohort, lattice, authorities, chains, traps, writes. Profiles `extreme` (Long Horizon) and `normal` (Normal Horizon, 60–100 calls) |
| `tools/difficulty_stats.py <input.json>` · `--build --verifier … --rubrics … --trajectories …` | Corrected six-run difficulty against the assigned V3 mode cap; five full passes fails; retains errored-run, spread, pattern and golden-run horizon checks. Build binds scores to the shared task context and rejects incomplete/duplicate inputs |
| `tools/redteam_review.py --mode redteam [--dual]` | Independent red team of the design by an external reviewer model (`REDTEAM_MODEL`), plus a second model family (`REDTEAM_SECOND_MODEL`) with `--dual`; endpoint and key come only from `REDTEAM_BASE_URL` / `REDTEAM_API_KEY`; never sends the prompt, OE or criteria; never prints a key |
| `tools/build_taxonomy_map.py <Taxonomy.json>` | Regenerates `references/Taxonomy_V2_Step_Map.md` |
| `tools/persona_view.py reach · can-see · who-can-see · search · check-sql` | The base as one persona sees it (ACL of `Evals/references/persona/acl.md`): reach census, YES/NO/UNVERIFIED per record, search-as-persona with hidden-hit counts, and `check-sql --load-bearing` on the injection's final state |
| `tools/fact_check.py <sql> --manifest <manifest>` | Fact consistency inside an injection: the manifest's declared `facts` hold in every text the SQL writes; unresolved ids cited in text; drift warnings |
| `tools/entity.py resolve · collisions` | One entity per person across every service (`references/universe_kb/entities.json`); shared names, lookalike handles and token conflicts |
| `tools/stage_gate.py <stage> <task_dir> [--paste]` | **Stage gates, blocking.** Per stage: outputs present and fresh, headings filled, no placeholders, evidence pointers per row, tool outputs pasted and re-run, persona reach of load-bearing records, universe-KB use, counter-readings in the self-review, and a current PASS from the upstream stage. Handoff is blocked until PASS; `--paste` writes the block into the Self-review (`setup/GEN_EXECUTION.md` § 6b; fixtures in `support/examples/calibration/stage_gate/`) |

Every tool has `--self-test`.

## Layout

```
Task_Authoring/
├── README.md                 this file
├── Guide/                    How_To_Author_A_Task.md (flow), Manual_Commands.md
├── task_inputs/              the single-task workspace: the platform slots (same layout as references/Tasks_Template)
│   └── Working_Files/        everything the commands generate (design, dossier, manifests, briefs, checks, stats, gates)
├── playbooks/                01 (scenario, injection), 01a, 02, 03, 04, 05, 08, 09, 11, 12 — numbered like the slot they write
├── skills/create-*/          the 11 command wrappers
├── tools/                    hg (search wrapper), sql_lint, base_check, fact_check, hardness_gate, persona_view, entity, stage_gate, difficulty_stats, redteam_review, build_taxonomy_map
├── setup/                    GEN_EXECUTION.md (contract every command reads first), install.py, uninstall.py, local_search.py
├── support/                  internals — not needed to author a task
│   ├── local_search/         patched copies of Evals/tools + their cache (rebuilt on demand by setup/local_search.py)
│   └── examples/             tool self-test fixtures, calibration evidence, two sample runs (sample_task_01/02) — not platform tasks
├── references/
│   ├── Hardness_Mastery.md   the technique library + the evidence behind it (read before designing)
│   ├── Scenario_Atlas.md     17 verified storylines with per-service anchors, persona reach, natural contradictions
│   ├── Ask_Carriers.md       where asks and facts can live in each of the 13 services, call costs, bulk shortcuts, SQL skeletons
│   ├── Hardness_Manifest_Spec.md  the manifest format and gate thresholds
│   ├── Docs/                 official V2 guidelines (1_Changelog … 10_Long Horizon), QC_Spec_Doc_Latest.csv
│   ├── Taxonomy_V2_Step_Map.md  generated from Taxonomy/Taxonomy.json (62 screens + key screen text)
│   ├── Tasks_Template/       empty V2 slot scaffold (copied into task_inputs/)
│   ├── Universe_Brief.md, Persona_Briefs.md, Native_Artifact_Anatomy.md
│   ├── persona_roster_v2.json (taxonomy's 19; 17 usable — see GEN_EXECUTION §3)
│   └── universe_schema_live.json (144-table injection schema, platform export Oct 4 — used by sql_lint)
```

Single sources of truth stay in `Evals/`: the tool catalog
(`Evals/references/tools/catalog.json`), the search helpers (`Evals/tools/`), the
roster (`Evals/references/persona/roster.json`) and the ACL mechanics
(`Evals/references/persona/acl.md`). This bundle never copies them.
`Evals/`, `claude/` and the three `HarmonyGames_*` data folders are **read-only**: all work
happens inside `Task_Authoring/` (GEN_EXECUTION §1). The eval commands run in the
user's Eval Portal workflow, not from here.

## Self-review and calibration (Oct 4 2026)

Every command ends with the adversarial self-review in `setup/GEN_EXECUTION.md` §6a and its stage gate (§6b, `tools/stage_gate.py`):
re-walk the paired Eval, write the strongest counter-reading for every PASS and FAIL and
settle it with evidence, re-verify facts from the source, re-run the tools. Each stage was
calibrated against ground truth (never against in-progress reviews):

| Stage | Ground truth | Before → after |
|---|---|---|
| Prompt check | 25 labelled QC cases | verdict 14 → 21/25 (fully blind subset 4/9 → 9/9); flag+severity 8 → 15/17 |
| Oracle Events check | 39 labelled QC rows | 30 → 33/39 |
| Rubric check | 35 labelled QC cards (blind) | flags 19 → 30/44; false Agent-Centric FAILs 6 → 0; verdict 18/35 both (the Eval is deliberately stricter than the older QC) |
| All-fail + difficulty | V1 task with recorded stats; 53-assert self-test | reproduces the recorded numbers exactly |
| Injection validity | 39 planted defect classes; clean SQL | 11 → 39/39 caught by their own rule; 0 false FAILs |
| Hardness forensics | 4 V1 tasks, blind band prediction | 3/4 → 4/4 |
| Human time · error/async · reference files | taxonomy, QC rows, V1 tasks | gaps closed (tier cross-check, async-twin bypass, one-file-per-reference) |

Scratch and evidence: `support/examples/calibration/`. The labelled cases are pre-Spec-V2 and from
other universes, so they validate the rules, not HarmonyGames facts; a fresh labelled
HarmonyGames set would tighten them further.

## Limits to know

- **Verification ceiling.** The lint and the gate prove structure, breadth, volume and
  that every designed difficulty exists in the SQL. Whether Opus actually fails is only
  proven by platform runs: the Opus pre-check → `/hardness`, then the baseline →
  `/create-difficulty`. `/create-hardening` MODE B closes that loop.
- **Horizon.** The extreme profile is built for Long Horizon. A Normal Horizon
  assignment at ≥ 500 calls scores Borderline Horizon (non-fail, task score capped at 3);
  use `--profile normal` unless the requester confirms otherwise.
- **Red team** needs `REDTEAM_BASE_URL`, `REDTEAM_API_KEY` and `REDTEAM_MODEL` (plus `REDTEAM_SECOND_MODEL` for `--dual`) in the environment and fails cleanly when the endpoint rejects the request (for example an exhausted budget). Transient drops are retried three times.
- **Personas.** 17 usable. `thomas` and `tim_steudler` are on the taxonomy list but fail
  `/prompt`'s identity gate and have too little data.
- **External reviews.** The user operates Eval Portal, including its five review
  pass screens and uploads. The local release gate does not collect those proofs.
