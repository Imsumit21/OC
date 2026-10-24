# Task_Authoring — Shared Execution Contract (V3 assignments · extreme-hardness engine)

Read this file first for every `/create-*` command, then read the playbook the
command wraps. It pins what every command must get right: the write boundary,
the authorship policy, the numbers of record, the hardness targets, and
the slot map.

**Agent invocation and paths.** The same skill sources serve Claude and Codex.
In this contract, skills and guides, `/create-<name>` denotes the Claude command;
in Codex invoke `$create-<name>` with the same arguments, for example
`$create-prompt-writing draft` or `$create-rubric-writing check`. Eval Portal
commands (`/injection`, `/prompt`, `/hardness`, `/oe`, `/rubric`) remain user-run
Portal steps.

Resolve the selected `SKILL.md` through its symlink to
`<bundle>/skills/<name>/SKILL.md`. The bundle's parent is the workspace root.
Run shell commands with that workspace as the working directory. In examples,
`Task_Authoring/` means this actual bundle directory, even if renamed;
`references/`, `playbooks/`, `setup/`, `tools/` and `task_inputs/` without that
prefix are bundle-relative. Use the selected task directory in place of the
default `task_inputs/` paths, as described in § 0.

Authority: `references/Docs/11_V3_Changes.md` supersedes conflicting V2 rules on its
changed topics. For unchanged topics use the V2 taxonomy
(`references/Taxonomy_V2_Step_Map.md`, generated from `Taxonomy.json`),
`references/Docs/QC_Spec_Doc_Latest.csv` and the V2 guidelines. Local Evals are
read-only reference implementations: their older clock, difficulty, unique-answer
and prompt-style overrides do not override V3. Apply the stricter unchanged rule
where sources still differ. § 2 records the explicit local authorship exception;
§ 3a preserves the existing local hardness targets. Eval Portal operation is the
user's responsibility, outside the local pipeline.

## 0 · Assignment context (before any universe access)

Paste the assignment exactly into `task_inputs/00_Assigments.md`, including its
headings, persona `Role:` line and displayed date. The eight fields are business
function, persona, role, competency, task skill, task type, difficulty mode and
universe date. Then run:

```sh
python3 Task_Authoring/tools/task_context.py --task-dir Task_Authoring/task_inputs --write
python3 Task_Authoring/tools/task_context.py --task-dir Task_Authoring/task_inputs --write --require-source
```

The first command normalizes the paste into
`Working_Files/00_Task_Context.json`; the second validates the registered shared
universe source. Both assigned freeze dates use the same local universe data.
Every `/create-*` command uses this
shared context and must pass source validation before grounding or writing a task.
Use `--task-dir <task_dir>` for another task workspace; keep all its artifacts in
that workspace. Each direct tool supports this option; pass it on every independent
shell command, or set `TASK_AUTHORING_TASK_DIR` to that task directory. Stage gates
keep their positional `<task_dir>` argument and propagate the selected context to
their child checks. Running `task_context.py --write` does not change the shell's
environment. Do not silently default missing V3 fields, change the assigned
mode/persona/date or infer a timezone for a displayed time. Source archive metadata
is provenance, not the task's assigned clock; a February archive label does not
make an October assignment unsupported.

The canonical freeze is the assigned date at 00:00 UTC, either
`2025-10-01T00:00:00Z` or `2026-02-14T00:00:00Z`. The original displayed date stays
in the context for traceability. Scope facts, activity, cohorts, timelines and ACL
claims to that freeze. Shared KB/brief summaries are leads: verify each relied-on
fact's record dates. A later event cannot be treated as already completed; a mutable
body edited after the freeze needs a dated version or independent before-freeze
evidence to establish its earlier content. Assignment/context changes invalidate
downstream certificates and require the affected stages to be repeated.

`references/universe_sources.json` maps both assigned dates to the same local
universe manifest and shared KB in shared-universe mode. Use the context's
`source.manifest` and `source.kb_path`. No separate October export or date-specific
KB build/review is required. The assigned freeze constrains task facts, completed
events and seeded timestamps; it does not select a different underlying dataset.
Source manifests and service folders must stay within this workspace because the
bounded helpers use workspace-relative locators. The derived KB stays inside
`Task_Authoring/`; exports remain read-only. Absolute registry paths are supported
within that boundary.

Role plausibility is a failing requirement, independent of competency. Business
function, competency and task-skill mismatches lower quality but do not fail a task
on their own. Authoring still calls for an authored artifact. Record the role
review and rubric evidence in `Working_Files/00_V3_Authoring_Evidence.json`
(§ 6b); its structured attestations support review, not semantic proof.

## 1 · Write boundary (HARD RULE)

- `Evals/`, `claude/`, `HarmonyGames_GitHub/`, `HarmonyGames_Gmail/` and
  `HarmonyGames_Other_Services/` are **read-only**: read, search and quote them;
  never write, edit, move or delete anything in them (owner's standing rule).
  **Never run `git` inside them** either: git freshens pack-file timestamps even on
  commands that look read-only. Read commits and PRs from `github/data.json` or `tools/hg.py`.
  Never execute SQL. Never modify the base exports.
- All work happens inside `Task_Authoring/` — normally `Task_Authoring/task_inputs/`;
  new folders and files inside `Task_Authoring/` are fine (e.g. `support/examples/`).
- **The eval commands are not run from this bundle.** The user runs `/injection`,
  `/prompt`, `/hardness`, `/oe` and `/rubric` in Eval Portal and handles its inputs,
  reviews and proof uploads. Locally, a `/create-*` command prepares the artifacts
  and never imitates Portal operation or writes into `Evals/`.
- Skill registration may create `.claude/skills/create-*` (Claude) and
  `.agents/skills/create-*` (Codex) symlinks at the workspace root through
  `setup/install.py --target claude|codex|both`. These link to the same bundle
  sources; `setup/uninstall.py` removes only this bundle's selected links.
  Registration does not change the read-only data folders or global settings.
- `tools/redteam_review.py` sends design material (never the prompt, OE or criteria
  text) to the reviewer endpoint configured in the environment (`REDTEAM_*`); never
  print, copy or log the key.

## 2 · Authorship policy (preserved local exception)

The official V3 course retains human authorship without LLM drafting or polishing.
This repository deliberately preserves its existing local exception: Claude or Codex may
draft, revise and polish every artifact, including the three course-reserved items.
This is a local automation policy, not a claim of compliance with that course rule.

| Artifact | Platform step | Who may write it |
|---|---|---|
| The prompt (`04_Prompt.txt`) | Write the Prompt | Claude, Codex or the human |
| The Oracle Events (`08_Oracle_Events.md`) | Oracle Events | Claude, Codex or the human |
| The rubric criteria (`09_Rubrics.json`) | Rubric Criteria Builder | Claude, Codex or the human |

The commands for these three work in three modes:

- **Prep** — a prep artifact built by querying the universe:
  `04_Prompt_Writing_Brief.md`, `08_OE_Writing_Ledger.md`, `09_Rubric_Writing_Plan.md`.
- **Draft** (on request) — Claude or Codex writes or revises the artifact itself, grounded in the
  prep artifact and the universe (every value from a record, never from memory).
- **Check** — compares the artifact (whoever wrote it) against its prep artifact and the
  universe, and writes a findings report. A check may propose replacement wording.

Platform mechanics still apply: the platform's AI-text detector screens every prompt,
and the Oracle Events field blocks pasting, so a drafted OE set is typed in. `/prompt`
reports how the prompt reads; a prompt that reads machine-written is a `/prompt` finding
to fix, like any other.

The official human-authorship rule remains recorded in `references/Docs/`, including
V3 § 8 and § 12; this bundle does not enforce it under the preserved local exception.

Everything else may be model-authored: injection SQL and its dossier, error/async
configuration, reference files, the human-time worksheet, all-fail analysis,
difficulty statistics, and hardening forensics.

## 3 · Numbers of record

| Item | Value | Source / note |
|---|---|---|
| Assigned freeze | **2025-10-01T00:00:00Z** or **2026-02-14T00:00:00Z**, from `00_Task_Context.json`; source validation must pass first | V3 § 3. No seeded record or completed event after the freeze; future deadlines are allowed |
| Model | **Opus 5.5** for the pre-check run and the baseline rollouts | Taxonomy steps 33–35; Change Log |
| Horizon tiers | Normal **50–100** tool calls · Long **100–500+** · Super-Long **paused** | QC Spec V2; Evals `horizon-tiers-v1` |
| Tool-call basis | The **golden run** (a baseline rollout scoring 100% on the rubric) if one exists, else the **rollout average**. Blocked/repeated calls add nothing. Under tier = Fail (Wrong Horizon); exceeding the displayed range is allowed by V3. Existing local profile limits remain in § 3a | V3 § 4. Oracle Events never enter this count |
| Full-pass gate | **Five or more of six rollouts passing every criterion fails**; four does not fail this gate alone | V3 § 5 operational pass@k rule; do not substitute the older ≤ 3/6 local gate |
| Avg weighted pass rate | **Easy < 90%; Medium < 85%; Hard < 70%**, assigned mode fixed; equality fails | V3 § 5. Judge only after fairness corrections and regrading (§ 6); old < 75% is superseded |
| Per-rollout spread | Standard deviation of per-rollout pass rates **0.1–0.3** | Evals `scoring.json`: > 0.3 suggests ambiguous rubrics, < 0.1 a deterministic task needing friction |
| Failure patterns | **≥ 2 distinct** patterns among failing rollouts; two rollouts are the same pattern unless they differ on **≥ 2** rubric results; largest pattern **≤ 50%** of failing rollouts | QC Spec V2; Evals `scoring.json`; taxonomy step 59 |
| Errored runs | **≤ 2 of 6** (3+ errored = Fail) | QC Spec V2 "Error Rate" |
| All-fail denominator | Completed (non-errored) rollouts only. ≥ 2 invalid all-fails = Fail; the Evals also fail a rubric with ≥ 2 rows **predicted** to fail every run. **Harness tolerance for predicted all-fail rows is 0** (stricter than `/rubric`): `stage_gate.py rubric-writing` / `rubric-check` block one | QC Spec V2; Evals `hg-strict-overrides-v1`; 09 hard gate 11 |
| Rubric weights | **1 / 3 / 5 by the kind of work**: 1 = direct lookup / literal check from one source · 3 = interpretation, calculation, comparison, limited reconciliation · 5 = multi-source reconciliation, deeper reasoning, cross-modal, tracing | QC Spec V2 "Criteria Weights" (Evals override replaces the Rubric Writing §5 axis count) |
| Rubric set | ≥ 1 Outcome row (zero Outcome = Fail; **no Process ratio**); builder minimum 5 criteria; ≤ 5 spot checks per group plus an output-volume row and direct exception rows (no bundled exact-set row); one fact per row and the same fact in **three or more rows fails**, across deliverables; every fair reading accepted | V3 § 9 supersedes conflicting UGT/duplicate rules; unchanged title-only, agent-centric and affirmative-title local checks still apply |
| Rubric validity | Binary, outside the quality tally: any incorrect, unauthorized, unobservable / impossible, contradictory, missing-coverage or predicted all-fail item blocks handoff; the percentage thresholds below apply to the other issue types | 09 check mode; red team B (2026-10-04) |
| Rubric quality | > 10% major, > 15% moderate-or-worse, or > 20% minor-or-worse issues = Fail | QC Spec V2 |
| Release | `stage_gate.py release` PASS before submit: every stage certificate present and current, one bundle digest (prompt, OEs, rubric JSON, SQL, reference-file bytes, error/async config, manifest, assignment + persona) matching every digest a stage recorded, no PROVISIONAL / UNRESOLVED / UNVERIFIED marker, OE check Task solvability SUPPORTED_BY_OE, difficulty gates clear, `06_PreCheck_Trajectory/trajectory.json` present | § 6b; red team B (2026-10-04) |
| Prompt field | 20–4,000 words; plain prose, no markdown | Taxonomy step 24 |
| Oracle Events field | 300–50,000 characters; pasting blocked | Taxonomy step 45 |
| Human time | Hours 0–1000 (step 0.25); reasoning 50–2,000 characters; pasting and copying blocked | Taxonomy step 25 (Oct 3 taxonomy) |
| Error injection | 18 selectable functions; mode `transient`/`persistent`; rate 0.1–1.0 (1.0 = permanent outage) | Taxonomy step 16 |
| Async wait | 6 selectable `*_submit_*` search functions; 5–300 s (default 30–35). Only 1.0 / 30 / 35 have ever been exercised — verify any other value in the first trajectory | Taxonomy steps 15–16 |
| Eval commands | `/injection` · `/prompt` · `/hardness` · `/oe` · `/rubric`. Verdicts **PASS · NON-FAIL · FAIL** (NON-FAIL with PARTIAL/BLOCKED = unresolved, does not clear a gate; NOT EVALUATED exists only on the platform record). `/oe`: wrong/missing step = FAIL 2, minor or final-response defects = NON-FAIL 3, clean = PASS 5. `/hardness`: score 1–2 = HOLD, 3–5 = PROCEED | Evals README / WORKFLOW; taxonomy steps 28–55 |
| Personas | **17 usable**: the roster in `Evals/references/persona/roster.json`. `thomas` and `tim_steudler` are on the taxonomy's 19-person list (`references/persona_roster_v2.json`) but fail `/prompt`'s identity gate and lack the data to carry a task (`references/Scenario_Atlas.md`) — escalate an assignment that names them | Evals roster; taxonomy |

**Counting conventions** (exactly what `tools/difficulty_stats.py` computes — verified against its code; red team A,
R1 #12). A rollout is *completed* unless its trajectory is empty, has no final `result` event or ends in an error
result (then *errored*); empty verifier output is not an errored run.
- **Full pass** means every rubric passes (the corrected view uses every fair rubric
  after recorded judge corrections). Report the completed-run ratio, but apply V3's
  operational count: five or more full passes out of the six rollouts fails.
- **Errored runs** are counted separately: ≤ 2 errored **and** ≥ 4 completed, else Fail (Too Many Erroneous Runs).
- **Per-run score** = the **weighted** pass rate: passed rubric weight ÷ total rubric weight. The average weighted pass rate
  is the plain mean of the per-run scores over completed rollouts.
- **Spread** = the **population** standard deviation (`statistics.pstdev`) of the per-run weighted scores; the sample SD
  and the unweighted SD are printed beside it and flagged when they read the other way at the band edge.
- **Failure patterns** = **single-linkage** grouping of the failing completed rollouts: two rollouts are linked when their
  failed-rubric sets differ on ≤ 1 rubric, and a pattern is a connected component (union-find; order-independent, no
  tie-breaking needed). The gate verdict uses this grouping (the strictest reading); the **pairwise** reading (largest
  set all within 1 rubric of each other) and every chained merge are printed beside it.
- **Horizon basis** = the tool calls of the golden run(s) (100% rollouts), else the mean over completed rollouts.

## 3a · Hardness targets (what `/create-*` designs for)

**Preserved local design policy.** V3 changes the assigned empirical score caps,
but this repository keeps its existing extreme/normal profiles and all targets
below: Long Horizon → extreme, including the ≥ 500-call floor. Easy does not select
a smaller profile. The Normal profile's 60–100 budget and existing profile exception
remain local design limits, separate from V3's minimum-call horizon check.

The engine is built so a single Opus run cannot pass by stacking easy steps. Every
task is designed in `/create-scenario`, implemented in `/create-injection`, and
checked by `tools/hardness_gate.py` against the SQL itself.

| Target | `effective_profile: extreme` — Long Horizon (default) | `effective_profile: normal` — Normal Horizon |
|---|---|---|
| Services carrying weight / injected | **≥ 10 of 13** / ≥ 10, every injected schema used | ≥ 7 / ≥ 6 |
| Necessary agent calls (design budget; `conditional_on` rows count 0) | **≥ 500** unconditional (plan ~600), ≥ 300 of them per-record, ≥ 10 services, none > 50% outside the per-record phase | **60–100**, ≥ 6 services, none > 40% |
| Cohort spine | ≥ 40 records × ≥ 3 per-record surfaces over ≥ 2 services | ≥ 10 × ≥ 2 |
| Asks spread through the universe | ≥ 12 fragments, ≥ 7 services, ≥ 10 containers | ≥ 7 / ≥ 5 / ≥ 6 |
| Hidden authorities | 2–4 in rarely-searched services, each with a decoy | ≥ 1 |
| Independent forensic chains | ≥ 3, distinct root causes | ≥ 2 |
| Traps | ≥ 12 in ≥ 7 families over ≥ 6 requirements; ≥ 4 supersessions; ≥ 6 distractors | ≥ 8 in ≥ 5 families; ≥ 2 supersessions; ≥ 4 distractors |
| Injected rows (INSERTs; UPDATE companions not counted) | ≥ 120 | ≥ 50 |

**Why these levers** — `references/Hardness_Mastery.md` §0 (measured on 131 Opus runs
and the calibration tasks): volume alone does not lower scores; hidden authorities in
rarely-opened services, authoritative-but-wrong summaries, unread thread replies,
house rules that override the natural reading and boundary records do. Breadth and
volume make the run long; the authorities and chains make it fail; spreading them
over several independent discoveries keeps the failures diverse.

**Horizon fit — one effective profile per task.** A ≥ 500-call design suits a **Long Horizon**
assignment. On a **Normal Horizon** assignment it scores Borderline Horizon (non-fail, task score
capped at 3). `/create-scenario` resolves the profile once and writes it into the manifest as
`effective_profile` (Long Horizon → `extreme`; Normal Horizon → `normal`, or `extreme` only with
`profile_exception: {reason, requester_confirmation}`). `hardness_gate.py` reads it from the manifest
and FAILs a `--profile` that disagrees; `stage_gate.py` scenario, injection and prompt-check read the
same value, so no two stages can validate one task under different thresholds. Long-Horizon volume must also pass
the Evals anti-inflation check (`Evals/references/rules/long_horizon.md`): every
repeated call answers a distinct question about a source-defined cohort that no bulk
result can replace.

## 4 · Universe access

The shared universe is split across the folders in the validated context's
`source.manifest` (the read-only Evals manifest for both assigned dates). Read the
shared data through the Evals search
helpers — never bulk-read a large export — and **always through
`Task_Authoring/tools/hg.py`**: it runs patched copies of `Evals/tools/hg_*.py`
(`Task_Authoring/setup/local_search.py`) whose runtime caches land in
`Task_Authoring/support/local_search/cache/` instead of `Evals/.cache/`. Running
`Evals/tools/hg_*.py` directly writes into `Evals/` and breaks § 1. Same subcommands
and arguments as `Evals/SEARCH.md`; run from the workspace root:

```sh
python3 Task_Authoring/tools/hg.py search inventory
python3 Task_Authoring/tools/hg.py search files <service> [query]
python3 Task_Authoring/tools/hg.py search search <service> "<query>" [--file F --pointer P --limit N]
python3 Task_Authoring/tools/hg.py search get <service> --file <service-relative file> [--pointer P]
python3 Task_Authoring/tools/hg.py search get-many --request <req.json>
python3 Task_Authoring/tools/hg.py search search-many --request <req.json>
python3 Task_Authoring/tools/hg.py search lookup <service> --ids-file F --file GLOB
python3 Task_Authoring/tools/hg.py records --request <checks.json>      # related record checks in one pass
python3 Task_Authoring/tools/hg.py reference routes <service> ...       # known export locations
```

`get` takes the service-relative file name (for example `--file contacts.json`),
not the workspace path printed by `search`. Finish paged results
(`truncated` / `next_offset`). Full syntax: `Evals/SEARCH.md`.

| Need | Authority |
|---|---|
| Tool names, parameters, read/write capability | `Evals/references/tools/catalog.json` (298 tools, 13 services) |
| Persona identity | `Evals/references/persona/roster.json` (17 usable) · `references/persona_roster_v2.json` (taxonomy's 19, exact emails) |
| Read visibility (ACL) | `references/Docs/4_Persona ACL Policy - V2.md`; `Evals/references/persona/acl.md` for mechanics |
| Injection SQL schema | `references/universe_schema_live.json` — **144 tables exported from the platform DB on 2026-10-04** (`setup/extract_schema.sql` Q1; generated columns `slack_messages.text_fts` and `gmail_messages.body_text_fts` must never be written), enforced by `tools/sql_lint.py`. Re-export when the platform changes. `Evals/references/schema/injection.json` is a 58-table snapshot without them — cross-check only |
| Where asks/facts can live, per-item call costs, bulk shortcuts | `references/Ask_Carriers.md` |
| Verified storylines + per-service anchors | `references/Scenario_Atlas.md` |
| Hardness techniques + evidence | `references/Hardness_Mastery.md` |
| Universe narrative | `references/Universe_Brief.md`, `references/Persona_Briefs.md` |
| What one persona can see / find (reach census, can-see, search-as-persona, check-sql on the injection) | `tools/persona_view.py` |
| Who is who across services; shared names and token conflicts | `tools/entity.py` (`resolve`, `collisions`) |
| Timeline, who is active at the clock, known coherence hazards, natural traps, cohorts, integrations/companions, writing and id conventions | `references/universe_kb/` (README first) |
| Fact consistency inside an injection (the manifest's `facts`) | `tools/fact_check.py` |

Search is evaluator-wide and does **not** apply persona ACL. You apply it:
Gmail, Slack, Google Calendar, Drive, Docs, Sheets and Slides are scoped to the
persona (search, list and by-ID reads; a denial reads as "not found"). GitHub,
Linear, Trello, Contacts, **Confluence and Snowflake are unscoped** — Confluence and
Snowflake are confirmed live (`Evals/ENVIRONMENT.md`, `service-availability-v1`) and
may carry weight through their cataloged operations. The current agent system prompt
(taxonomy, Oct 2026) lists all 13 services, Confluence and Snowflake included (the V1-era
prompt listed 11). Agents still open them rarely (Snowflake 46/131 V1 runs), so a task that
depends on them still benefits from a natural pointer (a link, a page or table name).

Two access traps apply everywhere (`references/Scenario_Atlas.md`): Drive-family files
owned by `Resource: -6481757892984311338` with an empty share list are readable by no
persona, and `domain` / `anyone` visibility is unverified — never count it as reach.

## 5 · Slot map — `task_inputs/` (numbered in platform screen order)

Each slot maps to an Evals input key (`Evals/INPUTS.md`, last column), so a file can be
pasted or saved under its key unchanged.

**Layout.** The top of `task_inputs/` holds only the platform slots, exactly as in
`references/Tasks_Template/`: `00_Assigments.md`, `01_Universe_Inject.sql`,
`02_Reference_Files/`, `03_Error_Async_Config.txt`, `04_Prompt.txt`, `05_Human_Time.md`,
`06_PreCheck_Trajectory/`, `07_Baseline_Trajectories/`, `08_Oracle_Events.md`,
`09_Rubrics.json`, `10_Baseline_Verifier_Results.md`, `11_AF_Justification.md` and
`Audit-Report/`. Every other row below (design, dossier, manifests, briefs, ledgers,
checks, stats, gates) is written to `task_inputs/Working_Files/`; `stage_gate.py`
resolves names in both places.

| Slot | Author | Platform step | Produced by | Evals key |
|---|---|---|---|---|
| `00_Assigments.md` | Human (exact paste of all eight V3 fields); `task_context.py` writes `Working_Files/00_Task_Context.json` | Assignment, Persona Selection | `task_context.py --write`; source validation before grounding | `task-details` |
| `01_Scenario_Design.md` + `01_Hardness_Manifest.draft.json` (draft manifest) | Model | — (design) | `/create-scenario` | — |
| `01b_Redteam_Review.md` | Model (optional, local) | — | `tools/redteam_review.py` | — |
| `01_Universe_Inject.sql` + `01_Grounding_Dossier.md` + `01_Hardness_Manifest.json` (final manifest: every draft id kept or listed in `design_delta`) | Model | Injection SQL | `/create-injection` | `injection` |
| `01a_Hardening_Report.md` (+ revision N+1 of the SQL / final manifest / dossier) | Model | — (forensics after a run) | `/create-hardening` | — |
| `02_Reference_Files/` + `02_Reference_Files_Manifest.md` | Model | Upload / Re-upload Reference Files | `/create-reference-files` | `reference:<id>` |
| `03_Error_Async_Config.txt` | Model | Configure Server Behavior | `/create-error-async` | `error-async` |
| `04_Prompt_Writing_Brief.md` | Model (prep) | — | `/create-prompt-writing` | — |
| `04_Prompt.txt` | Claude, Codex or human | Write the Prompt | `/create-prompt-writing draft` (optional) | `prompt` |
| `04_Prompt_Check.md` | Model | — | `/create-prompt-writing check` | — |
| `05_Human_Time_Worksheet.md` | Model worksheet; the human types the field | Human Time Estimate | `/create-humantime` | — |
| `05_Human_Time.md` | **Human** (the typed field) | Human Time Estimate | — | `human-time` |
| `06_PreCheck_Trajectory/trajectory.json` | Platform run | Opus 5.5 Pre-check, Opus Difficulty Check | — (then `/hardness`) | `opus` |
| `07_Baseline_Trajectories/` | Platform | Agent Runner — Baseline | — | `baseline` |
| `08_OE_Writing_Ledger.md` | Model (prep) | — | `/create-oe-writing` | — |
| `08_Oracle_Events.md` | Claude, Codex or human | Oracle Events | `/create-oe-writing draft` (optional) | `oe` |
| `08_OE_Check.md` | Model | — | `/create-oe-writing check` | — |
| `09_Rubric_Writing_Plan.md` | Model (prep) | — | `/create-rubric-writing` | — |
| `09_Rubrics.json` | Claude, Codex or human (builder export) | Rubric Criteria Builder | `/create-rubric-writing draft` (optional) | `rubric` |
| `09_Rubric_Check.md` | Model | — | `/create-rubric-writing check` | — |
| `10_Baseline_Verifier_Results.md` | Platform | Run Verifiers — Baseline | — | `baseline-verifier` |
| `11_AF_Justification.md` | Model | Rate All-Fail Rubrics | `/create-allfail` | `all-fail` |
| `12_Difficulty_Stats.txt` | Model (+ `tools/difficulty_stats.py`) | Difficulty & Failure-Pattern Check | `/create-difficulty` | `difficulty` |
| `13_Release_Gate.txt` | Model (+ `tools/stage_gate.py release`) | — (final check before Submit) | `stage_gate.py release` | — |

**Stage gates per slot** (`tools/stage_gate.py <stage> <task_dir>`, § 6b). The primary artifact (bold) carries
the pasted PASS block; the next stage's gate checks that block is current.

| Stage | Gates the slot(s) | Upstream PASS it requires |
|---|---|---|
| `scenario` | **`01_Scenario_Design.md`**, `01_Hardness_Manifest.draft.json` | — |
| `injection` | SQL, final manifest, **`01_Grounding_Dossier.md`** (inputs: assignment, scenario design, draft manifest — never a later stage's output) | scenario |
| `hardening` | **`01a_Hardening_Report.md`** + digests of the revised SQL and final manifest (its gate re-runs the injection checks: revision N+1) | injection |
| `reference-files` | **`02_Reference_Files_Manifest.md`** + folder | injection |
| `error-async` | **`03_Error_Async_Config.txt`** | injection |
| `prompt-writing` | **`04_Prompt_Writing_Brief.md`** | injection (+ error-async, reference-files if present) |
| `prompt-check` | **`04_Prompt_Check.md`** (+ hash of `04_Prompt.txt`) | prompt-writing |
| `humantime` | **`05_Human_Time_Worksheet.md`** | prompt-check |
| `oe-writing` | **`08_OE_Writing_Ledger.md`** | prompt-check |
| `oe-check` | **`08_OE_Check.md`** (+ `08_Oracle_Events.md` digest) | oe-writing |
| `rubric-writing` | **`09_Rubric_Writing_Plan.md`** | oe-writing, oe-check |
| `rubric-check` | **`09_Rubric_Check.md`** (+ `09_Rubrics.json` digest) | rubric-writing |
| `allfail` | **`11_AF_Justification.md`** | rubric-check |
| `difficulty` | **`12_Difficulty_Stats.txt`** (+ `12_difficulty_input.json`) | allfail (if present) |

The prompt, OE and rubric slots (`04_Prompt.txt`, `08_Oracle_Events.md`, `09_Rubrics.json`) have no gate of their own: the
check reports are gated, and their digests tie each report to the exact text checked.

**Revisions, not cycles.** The stage graph is a DAG: no stage reads a later stage's output. The scenario certifies the
draft manifest; injection writes the final one. Hardening is revision N+1 of the injection: it edits the SQL / final
manifest / dossier, re-runs `stage_gate.py injection --paste`, then `stage_gate.py hardening --paste` (which re-runs the
injection checks on the revised files and records their digests); downstream stages then re-run on the new revision.

Platform outputs (`06_PreCheck_Trajectory/`, `07_Baseline_Trajectories/`,
`10_Baseline_Verifier_Results.md`) are placed here by the user. No command ever
fabricates, estimates or "fills in" a platform output. There is no changelog slot
(the platform's changelog export was retired) and no dynamic-context slot (removed
from the platform).

## 6 · Per-command procedure

1. Read this file, then the command's playbook in full. Playbook gates are hard gates.
   Run `task_context.py --task-dir <task_dir> --write --require-source` before any
   universe lookup; use the shared context's role, freeze, mode and source everywhere.
2. Read the upstream slots the playbook lists. If a required one is missing, stop
   and name it — do not invent it.
3. Ground every fact through § 4. Apply the clock and the persona ACL yourself.
4. Write only the slot(s) the playbook names.
5. Run the bundle's mechanical checks the playbook names (`tools/sql_lint.py` — schema
   and clock, `/injection` Check B; `tools/base_check.py` — consistency with the base
   universe, `/injection` Checks A and C; `tools/hardness_gate.py`, which runs both;
   `tools/difficulty_stats.py`; and the universe tools the playbook names: `tools/persona_view.py`, `tools/entity.py`,
   `tools/fact_check.py`) and report their verdicts verbatim. A FAIL blocks handoff.
   Schema of record: `references/universe_schema_live.json` (exported with
   `setup/extract_schema.sql`).
6. Self-check against the applicable `QC_Spec_Doc_Latest.csv` dimensions and the Evals rules
   for the paired command. A dimension that would score 2 (Fail) blocks handoff — fix
   the artifact (any of them, including the prompt, OEs and criteria).
7. Run the adversarial self-review (§ 6a) and record it.
8. **Stage gate (§ 6b):** `python3 Task_Authoring/tools/stage_gate.py <stage> Task_Authoring/task_inputs --paste`.
   Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; fix the artifact and re-run until it does.
9. Deliver: the output path(s), the stage-gate verdict, the blocking findings if any, and the next step
   (the paired eval command, or the human step that comes next).

## 6a · Adversarial self-review (every command, before handoff)

A verdict or artifact is not done when it is written; it is done when an attempt to fail it
has itself failed. Every `/create-*` command ends with this loop and records it in its output
under **Self-review**:

1. **Re-read as the eval.** Open the paired Eval file (`Evals/0_Injection_Quality_Eval.md`,
   `1_Prompt_Eval.md`, `1A_Hardness_Eval.md`, `2_Oracle_Events_Eval.md`, `3_Rubrics_Eval.md`;
   for all-fail / difficulty: `Evals/references/rules/all_failing.md`, `scoring.json` and the
   QC rows) and walk its checks in order against the output — not from memory.
2. **Strongest counter-reading.** For every PASS-direction judgement, write the best argument
   that it should FAIL (a rejected fair reading, a missing record, a looser/stricter rule, a
   reviewer case in `Evals/references/rules/*_qc_cases.json` / `*_qc_examples.md` that looks
   similar). For every FAIL-direction finding, write the best argument that it is a false
   positive. Resolve each with evidence (record pointer, rule §, case id), not opinion.
3. **Re-verify facts, not notes.** Re-read every load-bearing value from the source record
   through `tools/hg.py`; a value carried over from a ledger, brief or dossier is a lead, not
   evidence.
4. **Mechanical checks again** after any change (`sql_lint`, `base_check`, `hardness_gate`,
   `difficulty_stats`).
5. **Record** the final verdict per check with its evidence, each counter-reading and how it
   was resolved, and anything left unresolved (named, never hidden). Never soften a finding to
   reach PASS; never invent a finding to look thorough.
6. **Prompt, OEs and criteria** may be quoted, judged and rewritten in the self-review.

7. **Gate it.** The self-review ends with the pasted `stage_gate.py` PASS block (§ 6b). The gate counts the
   counter-readings (each must cite evidence: a record id, pointer, rule § or case id) against a stage-specific
   minimum that scales with the artifact, and checks that the self-review names its required items and an
   `Unresolved:` line.

Independent pass (required for scenario — the gate blocks without both files; recommended for injection): `tools/redteam_review.py --mode redteam --dual` — two reviewer models from different families red-team the same model-authored artifacts
(design, dossier, ledger, plans) — not on the prompt, OE or criteria text.

## 6b · Stage gates (`tools/stage_gate.py`, every `/create-*` command)

A stage is handed off when its gate passes, not when its author says it is done. The gate is mechanical,
read-only on inputs, stdlib only; `--self-test` runs 15 good stages (release included), 66 planted defects and 2 re-run contradictions
(`support/examples/calibration/stage_gate/`; the 13 added for harness red team A carry a `redteam` field).

| Family | What blocks |
|---|---|
| structure | missing output or input; an output older than an input (stale); a required heading missing or empty; `<…>` template slots, TODO/TBD, empty table rows, unchecked boxes, unresolved `[ a / b ]` choices |
| evidence | factual rows without a record id or pointer (Slack `C…/ts`, `f_`/`d_`+22 hex, `evt_`, `ENG-n`, `repo#n`, `mailbox/id`, `page_`, `cmt_`, 24-hex, JSON pointer, SQL line, F-id) below the stage's ratio; quoted spans that are not exact substrings of the human file |
| tool | a required tool output not pasted, or a paste the re-run contradicts (`sql_lint`, `base_check`, `fact_check --no-leak`, `hardness_gate` at the manifest's `effective_profile`, `difficulty_stats`, `persona_view` reach / can-see / check-sql) |
| review | fewer evidenced counter-readings than the stage minimum; required items not addressed; no unresolved list |
| reach | a load-bearing scoped record that `persona_view` does not show as YES for the assigned persona; a `DENIAL-INTENDED` / `UNVERIFIED-OK` probe row marked `LB` or without `alternate_evidence_ids` that are all YES |
| anchor naming | scenario, injection, prompt-writing: an anchor-naming entry (an `anchor name` / `may be named` / `noun phrase` table column, an `Anchor An name:` line, the manifest's `anchors[].prompt_reference`) that starts with an imperative verb, contains a second-person request or runs over 6 words (`boundary.anchor_naming`) |
| revision | injection: a draft-manifest id missing from the final manifest without a `design_delta` entry (`structure.design_delta`); a pasted hardness_gate profile other than the manifest's `effective_profile`. hardening: the injection checks re-run on the revised SQL / manifest / dossier (`revision.injection`) |
| kb | scenario/injection without `coherence_hazards` ids for all six categories, `activity.json` status for every seeded speaker, `integrations.json` companions per seeded service, cohorts/trap_catalog/timeline citations, `conventions.json`, `entity.py` output |
| chain | the upstream artifact lacks a pasted `STAGE GATE <stage>: PASS` block, or its digests no longer match the files |
| tier | prompt-check: no `01_Hardness_Manifest.json`; an `effective_profile` that does not fit the assignment's tier (Long Horizon → extreme; Normal → normal, or extreme with `profile_exception.requester_confirmation`) or a manifest `horizon` other than the assignment's; or no current dossier `HARDNESS GATE (<effective_profile>): PASS`; the C12 QC floor stays the `/prompt` prediction |
| provenance | oe-writing: an opaque §B locator (channel/ts, `f_`/`d_`, `evt_`, ticket, mailbox/id, hex id) not traceable to the prompt, an earlier fact's Expected data (topological Depends-on) or a natural `search "<query>"` that reaches it as the persona; a scoped fact with no record id; a defer search without services, population, pagination and governing version (or UNRESOLVED) |
| validity | rubric-writing: any predicted all-fail row (tolerance 0, stricter than `/rubric`'s 2); rubric-check: any `incorrect` / `unauthorized` / `unobservable` / contradiction / `missing_coverage` finding, Coverage gap, unauthorized criterion or predicted all-fail row — binary, whatever the percentage tally |
| diversity | rubric-writing: one unit of discovery (an authority, or one tool response however many F rows it is split into; transitive over Depends-on) deciding > 50% of the weight; sampled populations need volume and direct exception rows, with no bundled exact-set row |
| shortcut | rubric-writing: `tools/shortcut_probe.py` output not pasted, stale (values digest), restricted (k > 3, not all services, no SQL overlay), not matching its re-run, or a HIT / INCOMPLETE line without `SHORTCUT-OK: <service> <record> — <reason>` |
| release | see the release gate below |

Row markers the gate reads: `LB` marks a load-bearing record anywhere in the artifact. `DENIAL-INTENDED: <reason>`
(a designed access denial, NO) and `UNVERIFIED-OK: <reason>` (e.g. a public channel the persona has not joined) mark a
**probe, which is never load-bearing**: the row must not carry `LB` and must list `alternate_evidence_ids: <ids>`, every
one YES for the persona — the alternates carry the dependency; UNVERIFIED never satisfies a required dependency
(red team A, R1 #3). The manifest's counterpart is `denied_probes` (`hardness_gate` `persona_reach`). Digests (`<file>#<12 hex>`) ignore the pasted gate lines, so pasting does not stale
a block but any later edit does. `--rerun lint` skips `base_check`/`hardness_gate`/`fact_check` (and the tier `hardness_gate`, search-origin and
shortcut-probe re-runs) and can only reach PARTIAL (exit 1). The gate only reports; it never edits an artifact. `SHORTCUT-OK: <service> <record> — <reason>` (outside the pasted probe output) accepts a
shortcut-probe hit after review.

**Release gate (final step before submit).** `python3 Task_Authoring/tools/stage_gate.py release Task_Authoring/task_inputs --paste`
writes its certificate to `13_Release_Gate.txt`. It blocks unless:
- every stage's PASS block is present and current (scenario, injection, prompt-writing, prompt-check, humantime,
  oe-writing, oe-check, rubric-writing, rubric-check, difficulty; hardening, reference-files, error-async and allfail
  when their artifact exists), and each certified stage is newer than its inputs;
- one **bundle digest** over `04_Prompt.txt`, `08_Oracle_Events.md`, `09_Rubrics.json`, `01_Universe_Inject.sql`,
  the `02_Reference_Files/` bytes, `03_Error_Async_Config.txt`, `01_Hardness_Manifest.json` and the assignment +
  persona matches every digest a stage certificate recorded for those files, and the prompt, OEs, rubric JSON, SQL and
  manifest are certified by prompt-check, oe-check, rubric-check and injection; the digest is recorded in the release
  block, so any later edit stales it;
- no PROVISIONAL, UNRESOLVED or UNVERIFIED marker (outside pasted tool output; `UNVERIFIED-OK:` dispositions excepted)
  and no open `Unresolved:` line or Unresolved cell remains in any artifact;
- `08_OE_Check.md` reports Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE · Blocking 0;
- the difficulty gates pass (`difficulty_stats.py` re-run has no blocking gate; `Blocking gates: none` pasted);
- the pre-check trajectory `06_PreCheck_Trajectory/trajectory.json` exists.

The release gate is static: it does not replay the task in a sandbox (the platform's baseline rollouts are the replay).

**V3 authoring evidence.** The gates also consume
`Working_Files/00_V3_Authoring_Evidence.json`, bound to the shared `context_hash`.
Its role reviews cover scenario and prompt-check; outcome reviews cover
prompt-writing and prompt-check; rubric rows bind each criterion to its prompt span,
fact, actual source value, reachable evidence path and accepted alternatives. See
`Guide/How_To_Author_A_Task.md` for the schema and artifact-hash command. These
checks verify supplied evidence, source values and bindings; a passing structure
does not prove the reviewer's semantic judgment. Eval Portal screenshots and uploads
are handled entirely by the user and are not collected or gated locally.

**Residual gaps (harness red team A, 2026-10-05 — documented, not implemented).** These findings are not closed by a
mechanical check; the partial answer is named so nobody mistakes a gate PASS for them.
- **Platform revision binding and reference solvability** (R1 #1–2). No platform `task_revision_id` binds Eval reports
  and trajectories to one universe snapshot + tool runtime + configuration, and no reference solution is executed in an
  isolated clone. Partial answer: the release gate's single bundle digest over every local artifact, and the Opus
  pre-check run (`06_PreCheck_Trajectory/trajectory.json`) as the first end-to-end execution.
- **Causal independence of chains** (R1 #11). `root_cause` ids are now a closed enum and distinct means distinct ids,
  but no intervention test neutralises each trap while holding the others fixed; failure patterns are still read from
  rubric vectors.
- **Record-level service necessity by removal** (R1 #8). The orphan check is schema-level; no test removes a service's
  operations to prove a required result becomes unattainable. Partially covered by `surface_requirements` (every
  per-record surface must serve an incorporated requirement's stated output).
- **Touched-scope selector** (R1 #16). "Task-touched data" is still the author's census plus the SQL- and
  manifest-touched records; there is no executable scope selector or instrumentation of the records a validation run
  opens.

## 7 · Handoff to the evals

The user handles Eval Portal. The bundle hands off the exact local artifacts and
the eight-field assignment context; the table below describes the review inputs
for that handoff. It does not authorize this bundle to operate Portal or collect
screenshots/uploads. Supply the SQL or an explicit "no injection" answer where asked.

| Command | Supply |
|---|---|
| `/injection` | `01_Universe_Inject.sql` only (skip the command if the task has no injection) |
| `/prompt` | `04_Prompt.txt` exactly as submitted · all eight assignment fields · SQL or "no injection" · `03_Error_Async_Config.txt` if configured · reference files the prompt uses |
| `/hardness` | `04_Prompt.txt` · SQL or "no injection" · the unhinted Opus 5.5 pre-check trajectory JSON · reference files the prompt uses |
| `/oe` | `08_Oracle_Events.md` · prompt · assignment + persona · SQL or "no injection" · reference files |
| `/rubric` | `09_Rubrics.json` · prompt · assignment + persona · SQL or "no injection" · reference files. A supplied OE is a comparison reference only; no OE PASS is required |

Order: `/injection` + `/prompt` as a pair once the SQL and prompt exist; `/hardness` on
the first Opus run (scores 1–2 = HOLD: return to `/create-hardening`); `/oe` once the
Oracle Events exist; `/rubric` once the criteria exist. The user runs the five
reviews in Eval Portal. A `/hardness` pass permits continuation; final difficulty
still uses corrected six-rollout results against the assigned mode's cap.
