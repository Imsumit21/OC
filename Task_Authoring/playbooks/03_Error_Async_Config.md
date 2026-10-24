# 03 — Error Injection & Async Wait Config (Playbook) — HarmonyGames · Spec V2

> Command: `/create-error-async` (optional step) · Writes: `task_inputs/03_Error_Async_Config.txt` · Paired eval: none of its own. `/prompt` takes the config as an input; `/oe` Phase 3.5 and `/rubric` grade what it implies · Gate: **`tools/stage_gate.py error-async` (blocking)** · Read first: `setup/GEN_EXECUTION.md`

## Purpose

Decide whether the task gets forced tool errors or async (submit → check → get) search
waits. **The default answer is `Friction: none`.** Configure friction only when the
scenario is realistically about an outage or a slow system, and then make it safe: the
task stays solvable, gradable and unambiguous.

Configured friction is **not** a difficulty lever. Use it for realism only:
- **Measured.** In the 131-run corpus every run routed around forced errors and async waits (`references/Hardness_Mastery.md` §0, §9). V1 check (V1 authoring-bundle QC task 1):
  - The config errored Slack search, Gmail search and Linear list at persistent 1.0, and made Drive search async.
  - The errors fired in 6 of 6 rollouts.
  - The agent got the right figures anyway.
  - Every failed row was a format row.
- **Not counted by `/prompt`.** The complexity hard gate counts only Ambiguity, Dynamic Change and Multi-Source (`Evals/1_Prompt_Eval.md` §1.5).
- **Not counted toward the horizon.** Blocked calls and repeated retries add nothing (`Evals/references/rules/long_horizon.md`).
- **Not the fix for a too-deterministic baseline.** When `difficulty_stats.py` or `scoring.json` says "add friction" (per-rollout SD < 0.1), it means *information* friction across services, delivered by `/create-hardening`. It never means this config.

Author this after `/create-injection`: you need the dossier to name the alternate path.

## The screen (`references/Taxonomy_V2_Step_Map.md` Screens 15–16, `step-ServerConfigInject`)

| Field | Values | Notes |
|---|---|---|
| `error_functions` | 0–18 of: `slack_send_message`, `slack_conversations_history`, `slack_search_public_and_private`, `gmail_search_messages`, `gmail_get_message`, `github_get_file_contents`, `github_create_issue`, `github_create_pull_request`, `github_search_code`, `linear_create_issue`, `linear_list_issues`, `trello_create_card`, `gdrive_search`, `gdrive_read_file`, `gsheets_values_get`, `gcal_list_events`, `gdocs_get_document`, `gslides_get_presentation` | Five are **writes**: `slack_send_message`, `github_create_issue`, `github_create_pull_request`, `linear_create_issue` and `trello_create_card` |
| `error_mode` | `transient` (timeout, agent should retry) · `persistent` (server_error, agent must work around) | Blank = persistent |
| `error_rate` | 0.1–1.0, step 0.1 | Blank = 1.0. Any rate below 1.0 is **automatically marked transient** |
| `wait_functions` | 0–6 of: `gmail_submit_search_messages` (disables `gmail_search_messages`), `slack_submit_search` (disables `slack_search_public_and_private`), `gdrive_submit_search` (disables `gdrive_search`), `github_submit_search_code` (disables `github_search_code`), `linear_submit_list_issues` (disables `linear_list_issues`), `trello_submit_search` (disables `trello_search`) | Search only. Fetches stay instant |
| `wait_min_seconds` / `wait_max_seconds` | 5–300, step 5 | Blank = 30 / 35. A max below the min is clamped up. The wait is paid per call, per rollout, on every run |

Screen 15 says the settings apply to "all runs: the baseline agent run and the rubric verifier",
not to the Universe Explorer. The Opus pre-check is an agent run: treat it as covered and confirm
that in its trajectory.

## Inputs / Output

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`
and read `Working_Files/00_Task_Context.json` (GEN_EXECUTION § 0). Use all eight
assignment fields, the assigned freeze and the context's registered universe/KB source.
Both freeze dates use the same local universe data. Check each relied-on fact at
the assigned freeze; shared KB summaries are leads, not a separate dataset gate.
V3 changed-topic rules take
precedence over older Evals/V2 references; local authorship and hardness-profile
exceptions remain as recorded in GEN_EXECUTION § 2 and § 3a.

Inputs
- `00_Assigments.md` (persona → scoped services), `01_Grounding_Dossier.md` + `01_Universe_Inject.sql`, `01_Hardness_Manifest.json`.
- `04_Prompt_Writing_Brief.md` / `04_Prompt.txt` and `02_Reference_Files_Manifest.md` if they exist. Use them to check that discovery is still required.
- `Evals/references/tools/catalog.json` for exact names and the alternate path's tools.

Output
- `task_inputs/03_Error_Async_Config.txt` in the `references/Tasks_Template/03_Error_Async_Config.txt` format, with a Self-review section. With no friction, write `Friction: none` and leave every field empty: delete the template's `[ ]` and `[ a | b ]` choices (the gate treats any left over as an unfilled placeholder), drop the empty tables, and write `pending (pre-baseline)` or the result on each post-baseline line. Supply the file to `/prompt` only when friction is configured.

## Hard gates

1. **Default none; never a hardness or horizon lever.** Write a one-line reason for configuring anything (the realism it adds). "Make it harder" or "add calls" is not a reason.
2. **Exact picker values.** Every function comes from the table above and exists in `catalog.json`. Name the instant tool that each wait disables.
3. **Mode and rate agree.** Use `persistent` with 1.0 to test a workaround or an escalation. Use `transient` with a rate below 1.0 (0.5 is the taxonomy's starting point) to test retries. `persistent` with a rate below 1.0 is contradictory, because the platform marks it transient. At 1.0 a retry never succeeds, so any expectation of a successful retry is unpassable. At a rate below 1.0 the task must still work in a run where every retry also fails.
4. **The alternate path is proven.** For each errored function, name where the same facts live and cite the record (`hg.py` pointer or SQL row). Use the delete-on-paper test: remove every errored function and re-derive the task end to end. The alternate path must be persona-readable, findable without the errored tool, and must not itself be errored or async. If no alternate exists, do not configure the error (`Fail - Prompt Feasibility with Tools`).
5. **The verifier hits the error too.** Never error a function the verifier needs to read required results. Never error a required write unless a natural feasible alternative remains. Record every fair alternate destination in acceptance; multiple fair routes alone do not fail. No feasible alternative is a Feasibility defect.
6. **Async needs real discovery.** The wait only fires when the agent has to search. If the prompt or a reference file names the artifact, the agent fetches it directly and the wait never fires. Record "do not name `<artifact>`" as a constraint for the brief and the reference-file manifest.
6a. **An errored search is not an outage when it has an async twin.** The error picker cannot reach the `*_submit_*` twins, and an unconfigured twin stays live. The twins:
    - `slack_search_public_and_private` → `slack_submit_search`
    - `gmail_search_messages` → `gmail_submit_search_messages`
    - `gdrive_search` → `gdrive_submit_search`
    - `github_search_code` → `github_submit_search_code`
    - `linear_list_issues` → `linear_submit_list_issues`

    In V1 (QC Task1, 6 of 6 rollouts) the agent met the 500 error on `linear_list_issues` and `slack_search_public_and_private`, then finished the same searches through `linear_submit_list_issues` and `slack_submit_search`. The designed alternate path is therefore only one valid route. The OE may show it, but no criterion may require it over the twin. The error still costs 2–9 wasted retries per rollout, and none of them count toward the horizon.
7. **ACL.** Do not error a scoped tool (Gmail, Slack, Calendar, the Drive family) whose denial the task wants reasoned about: an error is indistinguishable from an ACL denial (`4_Persona ACL Policy - V2.md` §8). Prefer GitHub, Linear or Trello functions. Some personas have no Gmail mailbox (`references/Hardness_Mastery.md` §6.7): verify the mailbox before erroring a Gmail function, because without one the Gmail path is already dead and the error adds nothing.
8. **The prompt never announces friction.** "Gmail is down, so…" is a Never in `6_Prompt Writing Guidelines - V2.md` §4.2. Record this as a brief constraint.
9. **Untested values.** Only an error rate of 1.0 and waits of 30/35 s have ever been exercised. Treat any other value as a test of the setting (V1 QC Task1 shipped an untested 20 s minimum wait). Confirm it in the pre-check trajectory: the failure rate is roughly as configured and the delay is as configured. If it is not, report it through the issue form and do not build on it.
10. **Recovery is observable.** The recovery or wait path must be expressible as an explicit, affirmative Oracle Event (`/oe` Phase 3.5) and as an affirmative criterion (Negative Criteria = **Fail**). Record the locator and the expected data for the human. Do not write the event or the criterion.
11. **Proof separates configured friction from natural friction.** Rollouts can fail without any configuration (dropped connections, query errors, invalid search qualifiers), and agents may call `*_submit_*` functions unprompted. The friction fired only if all of these hold:
    - the configured function was called and returned the **configured** error type, at about the configured rate. In V1 the persistent error read `{"status_code": 500, "message": "Internal Server Error"}`. A function the agent never calls proves nothing: V1's errored `gmail_search_messages` was called in 1 of 6 rollouts;
    - a call to the disabled instant tool returns `No such tool available` (V1: `gdrive_search` under an async Drive wait), or is absent;
    - submit → status → result shows the configured delay.

    If it did not fire, every recovery criterion is ungradeable. Remove the friction or those criteria before rating all-fails.
12. **Changing the config later invalidates the downstream work** (`Evals/WORKFLOW.md`): re-run `/prompt`, the pre-check and `/hardness`, the OE and rubric checks, and the baseline.

## What the evals do with it

| Eval / QC | Effect |
|---|---|
| `/prompt` | Takes `03_Error_Async_Config.txt` when configured. Feasibility: "a forced error must not remove the only valid route or mask an intended denial." Friction never satisfies the complexity gate |
| `/oe` | Phase 3.5: every injected error or wait has an explicit recovery or wait event (missing = Incomplete) |
| `/rubric` · QC Negative Criteria | Recovery criteria must be affirmative. A "does not give up" row = **Fail** |
| `/injection`, `/hardness` | Never receive the config. `/hardness` judges the run as it is |
| QC Error Rate | Rollouts that crash on the friction count toward the 3-of-6 errored-run **Fail** |

## Procedure (checklist)

- [ ] Gate 1: decide. If there is no realism reason, write `Friction: none` and go to the Self-review.
- [ ] Choose the functions, the mode/rate pair and the waits (gates 2, 3, 9).
- [ ] Prove the alternate path per errored function, name its async twin if it has one, and run the delete-on-paper test (gates 4, 5, 6a).
- [ ] Check async discovery against the prompt, the brief and the reference files (gate 6), and the persona's scope and mailbox (gate 7).
- [ ] Fill the template: alternate-path table, async-discovery table, "Facts for the human" (locator → expected data, for `/create-oe-writing`), and the post-baseline checks from gate 11.

## Self-review (GEN_EXECUTION §6a, record it in the config file)

1. **Walk the checks in order.** Read `Evals/1_Prompt_Eval.md` §2.2 (Feasibility A/B, persona ACL gate) and its "configuration align with that path" check, then `2_Oracle_Events_Eval.md` §3.5. Walk them against the config.
2. **Counter-readings.**
   - "Friction is load-bearing for difficulty": §9 evidence. If any design note relies on it, strike that note.
   - "The alternate path is a second destination": check UGT. The alternate must yield the same fact or the same write.
   - "The verifier cannot see the write": gate 5.
   - "The wait never fires": search the prompt, the brief and the reference files for the target's name.
   - "Some criterion requires the designed alternate path": the async twin (gate 6a) is an equally valid route. Remove the requirement.
   - "Mode and rate conflict": gate 3.
   - For `Friction: none`: is the scenario explicitly about an outage the prompt mentions? If not, none stands.
3. **Re-verify** each alternate-path record through `hg.py`, under the persona's ACL.
4. **Record** each verdict with its evidence, each counter-reading and how it was resolved, and anything left unresolved, under a `## Self-review` heading (gate minimum: six evidenced counter-readings when friction is configured, two for `none`).

## Deliver

Run `python3 Task_Authoring/tools/stage_gate.py error-async Task_Authoring/task_inputs --paste`; handoff is blocked until it prints `STAGE GATE error-async: PASS`, and `--paste` writes that output into the Self-review of `03_Error_Async_Config.txt` (the next stage's gate refuses an upstream artifact without a current PASS block). The gate checks the picker values, the mode/rate pair, one alternate-path row (with a record pointer) per errored function and one discovery row per wait.

Report the configured functions with mode/rate/wait (or `Friction: none`), the alternate path
for each, the constraints for the brief and the reference files, and the post-baseline checks.
Next: `/create-reference-files` if the scenario needs an attachment, otherwise `/create-prompt-writing`.
