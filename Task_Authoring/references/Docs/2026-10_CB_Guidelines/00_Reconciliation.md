# 2026-10 CB guidelines → pipeline reconciliation

The twelve guideline texts in this folder (Oct 19–28, 2026) were checked rule by rule against `skills/`,
`playbooks/`, `setup/`, `references/` and `tools/` on 2026-11-01. Rules not listed here were already
implemented (horizon tiers, Super-Long-Horizon paused, Opus 5.5 baseline, pass@k ≤ 4/6, the four rubric
prohibitions, five OE fields, do-nothing tests, attachment-body rule, title self-containment, conflict rows,
hedge wording, prompt tool/step-list bans).

## Now enforced by a tool

| Rule (guide) | Where |
|---|---|
| Seeded claims about base git branches must agree with base git and `#builds` (06 §data check; `/prompt` 3.2 runs `git branch --contains`) | new `tools/base_claims.py` (B1–B4), blocking in `stage_gate.py injection` (`tool.base_claims`); bad cases in `support/examples/calibration/stage_gate/bad/cases.json` |
| Only the 64 listed tables are writable; never Snowflake; never `public._changelog` (08) | `tools/sql_lint.py` `WRITABLE_TABLES`, errors (was a warning / unchecked) |
| A closed ticket with later activity fails the task (09) | `tools/base_check.py`: a seeded comment after `completed_at`/`canceled_at` is a FAIL (was a warning) |
| Several 100 % runs: the lowest count governs (11) | `tools/difficulty_stats.py`: one governing count for both tier bounds (was `max` for the upper bound) |
| More than 50 % Process rows fails; zero Outcome fails (05, 09) | `tools/stage_gate.py` rubric-check `rubric.category_balance` |
| Normal: stay clear of 100 (11) | `tools/hardness_gate.py` normal `budget_cap` 95 (was 100) |

## Now stated in the playbooks / setup

| Rule (guide) | Where |
|---|---|
| Normal above 100 = NON-FAIL; padding is a failing error; pre-check count is an early warning; margin 60–95 / ≥ 110; tier shares 15 / 85 % (03, 11) | `setup/GEN_EXECUTION.md` §3 table; `playbooks/12_Difficulty.md`; `references/Hardness_Manifest_Spec.md`; task template |
| No filler records, fields, comments or steps for volume (11) | `skills/create-injection`, `skills/create-scenario` Checks |
| Call budget recheck before `/prompt` (11 Part 6) | `playbooks/04_Prompt_Writing.md` (replaces "Do not estimate a call count") |
| ≥ 2 unnecessary Process rows fails (05, 09) | `playbooks/09_Rubric_Writing.md`, `GEN_EXECUTION.md` |
| `/oe` passes or blocks, no NON-FAIL (04) | `GEN_EXECUTION.md`; `playbooks/08_Oracle_Event_Writing.md` (every row fixed before `/oe`) |
| Review repair: change only FAIL/Major rows; settle the item, not a new rule (06 §9) | `GEN_EXECUTION.md` §3 "Review repair" |
| Re-run matrix per changed input (06) | `GEN_EXECUTION.md` §3 "Re-run matrix" |
| Pass screen only; `EVP-` code, attempt ID, one review at a time, `/admin` (12) | `GEN_EXECUTION.md` §3 "Submission proof"; `references/Tasks_Template/00_Assigments.md` |
| 1–2 load-bearing traps, kept only if they fail > 1 run; don't stack information seeking with source evaluation / temporal / deliverable form; multimodal skipped (10) | `references/Hardness_Mastery.md` §13.1 |
| `public._changelog` is where the user confirms the injection landed; "No records found" is expected (08) | `GEN_EXECUTION.md` platform-outputs note |

## Deliberately kept different (stricter or grader-aligned)

| Guide says | Pipeline keeps | Why |
|---|---|---|
| Score cap "at most" 90 / 85 / 70 % (06, 10) | strictly below; equality fails | the safer side of the boundary |
| Rubric issues fail at > 10 % major, > 15 % moderate+, > 20 % any (05, 09) | any Major or Moderate fails; Minor > 10 % fails | Evals `3_Rubrics_Eval.md` bands, stricter; platform floor recorded beside it |
| Weights by difficulty axes exercised (05) | kind of work (Evals override); both readings recorded, disagreements resolved per row | the `/rubric` grader applies the override |
| Exact-set / "exactly N rows" enumeration rows (10) | volume row + ≤ 5 spot checks, no bundled exact-set row | Evals 2.2 override (`/rubric` fails bundled rows) |
| Average of all six when no 100 % run (11) | average of completed rollouts | an errored run has no count; stated in `GEN_EXECUTION.md` |
| Build on 1–2 traps (10) | local ≥ 12 traps / ≥ 7 families floor, with the 1–2 load-bearing traps named | user-retained extreme profile |
| Confluence / Snowflake unclassified, check from persona view (01, 02) | unscoped, confirmed live | `AGENTS.md` / `service-availability-v1`, QC Rating Form V12 `acl.md` |
| Let the portal draft the SQL (08) | SQL authored locally, then pasted | the bundle's gates need the SQL as an input |
