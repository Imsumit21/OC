# Plan: make `/create-allfail` produce the baseline all-fail justification file

Written 2026-11-03 for review before implementation. Scope: the `create-allfail` skill, its playbook, the
`allfail` stage gate, the task template and the slot map. No change to `Evals/` (owner's rule), and no change
to any task's criteria.

## 1. Problem

The stage produces one artifact, `11_AF_Justification.md`, an evidence workbook (per-run events, eight tests,
causation, hand-off line). The platform review at screen 58 asks for the opposite shape: one short
justification per all-failing rubric, ready to paste. Today that text is hand-written per task; the
`task_inputs-Suryansh` folder shows the accepted format (title, one intro line, then `## <criterion title>`
followed by a single paragraph).

Meanwhile the platform's saved-input table maps the `all-fail` key to `11_Baseline_AllFail_Justifications.txt`
(`Evals/INPUTS.md:172`; `hg_store_input.py:29`; `hg_source_checks.py:20` lists it in `METADATA_NAMES`), while
`setup/GEN_EXECUTION.md:462` maps that same key to `11_AF_Justification.md`. So the file the platform expects
by name is not the file this pipeline produces.

## 2. Goal

`/create-allfail` writes two files from one analysis:

1. `11_AF_Justification.md`, the evidence workbook, unchanged in role and still the gate's primary artifact.
2. `11_Baseline_AllFail_Justifications.md`, the screen-ready file: header line, one `##` section per VALID
   all-fail rubric with the criterion title verbatim, one paragraph each. It is the text for screen 58 and the
   artifact saved under the platform's `all-fail` key.

## 3. Verified constraints

| # | Fact | Evidence |
|---|---|---|
| C1 | The platform's `all-fail` input is `11_Baseline_AllFail_Justifications.txt`; the workbook name is a local invention | `Evals/INPUTS.md:172`; `support/local_search/tools/hg_store_input.py:29` |
| C2 | The platform treats that file as evaluation metadata, never as a source, so it must exist as an input and is never quoted as evidence | `support/local_search/tools/hg_source_checks.py:20` (`METADATA_NAMES`) |
| C3 | The slot map currently binds `all-fail` to `11_AF_Justification.md` | `setup/GEN_EXECUTION.md:462` |
| C4 | Screen 58 is "Rate All-Fail Rubrics - BASELINE"; the QC rule asks for a 1-2 line justification per row | `references/Taxonomy_V2_Step_Map.md:67`; `Evals/references/rules/all_failing.md` § "What all-failing means" |
| C5 | The gate parses only the workbook: blocks by `## R<n> - VERDICT`, eight test words, one justification sentence cap of two | `tools/stage_gate.py:2969-3026` |
| C6 | `STAGES["allfail"]` has one primary and one output, and the difficulty gate consumes it as an optional upstream | `tools/stage_gate.py:3120-3128` |
| C7 | Any change to `tools/*.py` re-digests `__gate_policy__` and stales every pasted gate block in every task | `setup/GEN_EXECUTION.md` § 6b; `plans/Create_Goal_Skill_Plan_2026-11-01.md` C2 |
| C8 | Self-test fixtures live in `support/examples/calibration/stage_gate/` with 108 `bad` cases and a `good` tree that already contains `11_AF_Justification.md` | `support/examples/calibration/stage_gate/bad/cases.json` |
| C9 | Accepted output shape today: title, one intro line, `## <criterion title>` plus one paragraph, no tables | `Task_Authoring-2/task_inputs-Suryansh/11_Baseline_AllFail_Justifications.md` |

## 4. Decisions to take (recommended first)

| # | Question | Recommendation | Reason |
|---|---|---|---|
| D1 | One justification text or two? | **One text.** The paragraph written in the workbook's `Justification (VALID only)` line is the same paragraph the screen file carries; the file is a render of it. Relax the gate's "at most 2 sentences" to "one paragraph, first sentence at most 220 characters, whole justification at most 1,400". | Two texts drift. The 220-character first sentence keeps the platform's 1-2 line reading available if the field truncates. |
| D2 | Extension | `.md`, and note in the playbook that the platform store saves it as `.txt` under the `all-fail` key. | Markdown headings are the format that was accepted. The store renames on save regardless. |
| D3 | Location | Task root, beside the workbook, as a platform slot. The workbook stays at the root too. | It is pasted at screen 58 and saved under a platform key, so it belongs with the platform slots. |
| D4 | INVALID, JUDGE ERROR or UNRESOLVED all-fails | No `##` section. One line `Not justified: R<n>, R<n> (invalid: <reason>)`, and nothing that could be pasted as a justification. | The skill must never hand a reviewer text for a row the pipeline itself says is defective. |
| D5 | No all-fails | Header plus one line saying no rubric failed every completed rollout. | Mirrors the workbook's `NONE` case and keeps the file present for the input key. |
| D6 | Em dashes | Blocking in this file only. House rule for the artifact the user pastes; apply the same rule to the workbook's justification line so the render matches. | Explicit request from the user; scope it so no other artifact is constrained. |
| D7 | Local file names | Blocking: no `Working_Files`, no `.md/.json/.sql/.py` name, no `SQL L<n>`, no `OE <n>`, same rule as rubric evidence. | The file is read outside the bundle. |

## 5. Changes by file

| File | Change |
|---|---|
| `skills/create-allfail/SKILL.md` | Output lists both files and says which one the platform keys; Deliver reports both paths and the screen text per rubric; the stage-gate sentence names the new checks |
| `playbooks/11_AllFail_Analysis.md` | Purpose (two artifacts, one analysis); Inputs/Output (second file); hard gate 6 rewritten for the paragraph shape and the dash rule; new **Step 9, write the screen file** (render from the justification text, one paragraph per VALID row, title verbatim); Output format gains the screen-file block; Self-review gains checks 8 and 9; Deliver text |
| `tools/stage_gate.py` | `st_allfail` gains the `baseline.*` checks of § 6; `STAGES["allfail"]` gains the second output; a historical-task escape (see § 7, R4) |
| `support/examples/calibration/stage_gate/good/11_Baseline_AllFail_Justifications.md` | New good artifact matching the fixture's all-fail set |
| `support/examples/calibration/stage_gate/bad/cases.json` | 8 new defect cases and 1 control case, each with `plan` naming this document |
| `references/Tasks_Template/11_Baseline_AllFail_Justifications.md` | Empty stub with the header line and a comment |
| `setup/GEN_EXECUTION.md` | § 5 adds the slot row and moves the `all-fail` key to it (the workbook keeps no key); § 6b adds the gate's second output; § 6a adds the screen check to the self-review list |
| `references/Tasks_Template/Working_Files/README.md`, `Task_Authoring/README.md` | Slot tables gain the file |
| `Evals/INPUTS.md` | **Not edited.** Its `.txt` path stays; the playbook notes the store renames on save |

## 6. Gate checks (new, `st_allfail`)

| Id | Rule | Blocking |
|---|---|---|
| `baseline.file` | Present when the workbook lists one or more all-fails, or when it says `NONE` | yes |
| `baseline.header` | First heading is `# Baseline All-Fail Justifications`; an intro line states `<n>/6 completed`, the all-fail count and how many are valid, matching the calculator | yes |
| `baseline.sections` | One `##` section per VALID all-fail; heading byte-equal to a `09_Rubrics.json` title; none for an invalid row; no missing or extra section | yes |
| `baseline.paragraph` | Each section body is exactly one paragraph: no blank line, no list marker, no table pipe, 250 to 1,400 characters, ends with a full stop | yes |
| `baseline.first_sentence` | First sentence at most 220 characters and names the criterion's expected value | yes |
| `baseline.figures` | The per-run numbers cited in the paragraph match the numbers the workbook cites for that row (set equality) | yes |
| `baseline.dashes` | No `U+2014` or `U+2013` anywhere in the file | yes (D6) |
| `baseline.names` | No local path or file name, no `SQL L<n>`, no `OE <n>` | yes (D7) |
| `baseline.one_text` | The paragraph equals the workbook's `Justification (VALID only)` text after whitespace normalisation | warn for one release, then blocking |
| `baseline.not_justified` | A `Not justified:` line names every invalid, judge-error or unresolved all-fail | yes (D4) |

Freshness and digests come free once the file is a declared output: editing it after a pasted block stales the
`allfail` certificate exactly as editing the workbook does today.

## 7. Risks and mitigations

| # | Risk | Mitigation |
|---|---|---|
| R1 | `__gate_policy__` changes, so every pasted gate block in every task goes stale | Expected and unavoidable for a gate change. Do it in one commit; list the affected tasks in the handoff; re-run gates only for tasks still in flight |
| R2 | The platform asks for 1-2 lines; a 400 to 1,000 character paragraph may be longer than the field shows | D1's first-sentence rule keeps a paste-able one-liner; cap the paragraph at 1,400 characters |
| R3 | Over-gating a paste-ready file | Only structure, figures consistency and the two house rules block; wording is never graded |
| R4 | Completed and archived tasks lack the new file, so their `allfail` gates would fail on re-run | Backfill the four completed tasks from their workbooks (Phase 4), and let a task whose `11_AF_Justification.md` predates the new gate pass with a `baseline.file` WARN recorded as historical |
| R5 | Two files drift apart | D1 plus `baseline.one_text`; the workbook stays the single source |
| R6 | Token cost per task | One paragraph per all-fail row, roughly 1.6k characters for four rows; no extra research, since the evidence already sits in the workbook |

## 8. Phases

| Phase | Work | Acceptance test |
|---|---|---|
| 0 | Freeze the format and write the fixture file from the current task's four all-fail rows | The fixture renders identically to `task_inputs2/11_Baseline_AllFail_Justifications.md` |
| 1 | Gate: `baseline.*` checks, second output, 9 fixture cases | `python3 Task_Authoring/tools/stage_gate.py --self-test` green; each new bad case fails on its intended id only |
| 2 | Skill and playbook text (Output, Step 9, hard gate 6, format, self-review) | Read-through against `all_failing.md`; no rule contradicts the 1-2 line guidance without saying why |
| 3 | Template stub, `GEN_EXECUTION` § 5, § 6a, § 6b, both READMEs | `grep` finds no other document still binding `all-fail` to the workbook |
| 4 | Backfill: `task_inputs2` plus the completed tasks under `support/completed_tasks/` | `stage_gate.py allfail <dir>` reports only `baseline.*` PASS or a recorded historical WARN, and no other check regresses |
| 5 | Verify and commit | `verify` tiers `code` and `redteam` both PASS (a gate that decides QA outcomes is treated as high risk); `__gate_policy__` change noted in the commit message |

## 9. What the current task needs afterwards

`task_inputs2/11_Baseline_AllFail_Justifications.md` already exists and matches the target format except for
D1: its paragraphs are longer than the workbook's one-line justifications. Once D1 is implemented, the four
workbook justifications are widened to the paragraph text (or the screen file's paragraphs are trimmed to the
workbook text, whichever the author prefers), and `baseline.one_text` then passes.

## 10. Open questions for the owner

1. D1: one text with a longer justification line, or two texts with a consistency check?
2. `baseline.file`: should a historical task without the file fail, warn, or be exempted by a marker?
3. Should the em-dash rule apply to the workbook's justification line too, or only to the screen file?
4. Is `.md` right, or do you want `.txt` so the local name matches the platform's saved path exactly?
