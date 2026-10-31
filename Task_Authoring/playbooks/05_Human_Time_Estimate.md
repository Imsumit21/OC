# 06 — Human Time Estimate (Playbook) — HarmonyGames · Spec V2

> Command: `/create-humantime` · Writes: `task_inputs/Working_Files/05_Human_Time_Worksheet.md` · Paired eval: none. There is no QC Spec V2 row for it. It is a **required** field (the task cannot be submitted without it) and a checklist item in `10_Long Horizon Guidelines - V2.md` §10 and Common Errors & Pre-QC ("justified sub-task by sub-task and the arithmetic adds up") · Gate: **`tools/stage_gate.py humantime` (blocking)** · Read first: `setup/GEN_EXECUTION.md`

## Purpose

Build a worksheet for the Human Time Estimate screen (`references/Taxonomy_V2_Step_Map.md` Screen 25, right after the
prompt): how long a person takes to do the task by hand, with no tools, no AI and no search.
The work is broken into sub-tasks whose measured volumes and minutes add up to the number
entered (`10_Long Horizon Guidelines - V2.md` §5).

| Field | Rule (taxonomy `step-TextCollection-97f4edcbe80f`) |
|---|---|
| `human_time_estimate_hours` | Required · 0–1000 · step **0.25** (max 2 decimals) |
| `human_time_estimate_reasoning` | Required · **50–2,000 characters** · **pasting blocked** (step map) and copying blocked (`Taxonomy.json` `disable_copying`). The field asks for sub-tasks with the time for each and, "if you injected a forced error, the time a human would spend on the workaround path" |

The human types the reasoning. The worksheet supplies facts and arithmetic (sub-tasks,
measured volumes, rates, minutes). It contains no paragraph written to be retyped.

First pass: after `04_Prompt.txt`. Refresh: once `08_Oracle_Events.md` exists, and again
after the baseline if the solution path or the count basis moved.

## Inputs / Output

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`
and read `Working_Files/00_Task_Context.json` (GEN_EXECUTION § 0). Use all eight
assignment fields, the assigned freeze (`freeze_utc`, the seed bound) and the context's
`universe` block and registered KB source.
The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is missing — there is no default. Check each relied-on fact at
the assigned freeze; shared KB summaries are leads, not a separate dataset gate
(`source.kb_status`: `reference-only` means leads only; `unavailable` means no KB — ground every fact in records).
V3 changed-topic rules take
precedence over the older V2 reference documents in `references/Docs/`; local authorship and hardness-profile
exceptions remain as recorded in GEN_EXECUTION § 2 and § 3a.

Inputs
- `task_inputs/04_Prompt.txt` (required: the estimate is for the work this prompt asks for).
- `task_inputs/00_Assigments.md` (required: tier and persona).
- `01_Grounding_Dossier.md`, `01_Hardness_Manifest.json` (traps → dead ends), `04_Prompt_Writing_Brief.md`, `03_Error_Async_Config.txt`, `02_Reference_Files_Manifest.md`.
- Refresh: `08_Oracle_Events.md`, `08_OE_Writing_Ledger.md`, then `07_Baseline_Trajectories/` and `12_Difficulty_Stats.txt` (count basis).
- The universe, only the selected one, through `tools/hg.py search`, for volumes.

Output
- `task_inputs/Working_Files/05_Human_Time_Worksheet.md`: hours, the sub-task table, the tier check and a self-review.

## Hard gates

1. **Manual effort only, and the same work.** The person scrolls channels, opens records one by one and computes by hand. Count only the work the prompt requires the agent to do. Do not count learning the universe from scratch.
2. **Volumes are measured from the persona's view.** Each sub-task names what is read, computed or written, with its real size from `hg.py` (messages in the window, rows, tickets, PRs, cards, documents, pages). Search is evaluator-wide, so filter the scoped services (Gmail, Slack, Calendar, Drive family) to what the persona can see. Never take a volume from memory or the dossier. Every count comes from the selected universe (`Evals/references/universes/<key>/`); the two archives differ (Gmail 91,379 vs 83,727 files, Slack 5,357 vs 4,844 messages), so a figure from the other universe is wrong (A-02). Windows use Pacific dates and `universe.persona_today` (Sat Feb 14, 2026 / Wed Oct 1, 2025), not the QC form's February 28 (A-04/A-30). (Per-persona Slack membership in `references/Ask_Carriers.md` runs from 0 to 293 of the 985 channels.)
3. **Rates are stated and anchored.** The only official calibration is the ten-hour Long-Horizon worked example (`10_Long Horizon Guidelines - V2.md` §4):

   | Work | Anchor |
   |---|---|
   | Skim a channel across a window | ~12,100 messages ≈ 4 h (≈ 3,000/h) |
   | Read one decisive thread past its apparent conclusion | ≈ 20 min |
   | Pull day-level metrics by hand | ≈ 2 h |
   | Find a handful of PRs and confirm what each contains | ≈ 40 min |
   | Write the record, then raise the tickets | ≈ 1 h 45 |

   For per-record work the worked example gives no anchor. Use the V1 estimates that reached QC review (the V1 QC few-shot examples and V1 HarmonyGames tasks):

   | Work | V1 evidence |
   |---|---|
   | Check one cohort record across 2–3 surfaces | ≈ 8–15 min (28 tickets × Linear/GitHub ≈ 4 h; 79 tickets × Linear/GitHub ≈ 20 h) |
   | Triage a listing by title, date or repo | ≈ 450 items/h (≈ 1,600 PRs filtered ≈ 3.5 h) |
   | Classify a reply or file in a sweep | ≈ 2 min each (1,540 replies ≈ 12 h) |
   | One tailored write (comment, ticket, message) | ≈ 5–10 min (79 comments + 13 state changes + 3 messages ≈ 9.5 h) |

   If you use a slower rate (foreign-language DMs, legal clauses, dense sheets), state the rate and the reason.
4. **Dead ends, workaround and re-reading are explicit** (`10_Long Horizon Guidelines - V2.md` §5):
   - one line, or a named part of a line, per designed trap the person would hit: the lookalike channel or title, the wrong month, the decoy record (from the manifest's traps);
   - the alternate path for every forced error in `03_Error_Async_Config.txt`;
   - revisiting findings that a later record overturns.

   An estimate written from the solution path ("finding X's DM", as if the person already knew where it was) undercounts.
5. **Writes are counted per write.** List each required send, create, update or comment, with its count.
6. **The arithmetic adds up.** Sub-task minutes sum exactly to the hours figure. Hours sit on a 0.25 step. The total stated in the reasoning equals the number entered (no "≈ 1 hour" over a 65-minute sum).
7. **Tier cross-check: measure honestly against V3.** Normal is under about 8 hours; Long-Horizon is about 12–24 hours; Super-Long is paused. Re-measure any mismatch and report the scope/tier risk without stretching or trimming the estimate. Older calibration examples below are historical, not replacement V3 effort bands:
   - a Normal estimate at or above about 8 h;
   - a Long-Horizon estimate outside about 12–24 h.

   V1 evidence:
   - The QC examples sit inside the triggers: 5 h at ~64 calls (Normal-sized) and 24 h at ~338 calls (Long).
   - The V1 Long-Horizon worksheet ran 10.5 h.
   - V1 Task1 was assigned **Normal** and estimated at 37 h. Its six baselines then averaged 437 calls, Borderline Horizon. The trigger would have caught that before any run.

   On a trigger, re-measure the volumes. If they hold, keep the number and report the tier risk upstream: an over-scoped Normal task heads for Borderline Horizon (non-fail, score capped at 3); a thin Long-Horizon task either has unmeasured scope or will land under the tier. Never stretch or trim hours to fit the tier.
8. **Legible to the platform linters.** V1 ran these on this field. They are unverified for V2, but they share the V2 step id `step-TextCollection-97f4edcbe80f`:
   - **Reasonableness (an LLM linter).** It sees only the prompt, the hours, the reasoning and the injection SQL. It flags an estimate roughly 3× above or below a defensible one, and any blank, zero or placeholder value.
   - **Banned phrases**, e.g. "OpenAI", "Scale AI", "Remotasks", "knowledge cutoff".
   - **Web plagiarism.**

   So the reasoning must make the scope visible from the prompt's side: name the volumes and the traps, not internal IDs alone. It must also be the human's own wording.
9. **Fits the field.** The condensed breakdown (one short line per sub-task: what, volume, minutes) is 50–2,000 characters, roughly 4–10 lines. Count the characters.

## Procedure (checklist)

- [ ] List the investigation and write work the prompt requires (dossier, manifest traps; OEs on refresh).
- [ ] Measure every volume with `tools/hg.py search`, persona-filtered for scoped services. Record the query or locator.
- [ ] Assign minutes from the anchor rates. Add the dead-end, workaround, re-reading and write lines.
- [ ] Sum, round to 0.25 h, run the tier check, count characters.
- [ ] Write the worksheet, then run the Self-review.

## Worksheet format

```
Pass: first | post-OE refresh | post-baseline refresh        Tier: <Normal | Long-Horizon>
Universe: <normal | synth-cut> · Clock: <universe.clock_line>
Hours: <n.nn>

| Sub-task | Kind (read / dead end / workaround / re-read / write) | Volume (measured, persona view) | Rate | Minutes |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
| Total | | | | <sum> = <n.nn> h |

Tier check: <in band | trigger: … → re-measured: … → reported risk: …>
Baseline count basis (post-baseline only): <golden run N calls | average N> vs tier
Condensed breakdown length: <chars> characters (field accepts 50–2,000)
Sources measured: <hg.py queries / locators>
```

## Self-review (GEN_EXECUTION §6a, record in the worksheet)

1. **Walk the checks in order.** Read `10_Long Horizon Guidelines - V2.md` §5 and §10, the Pre-QC "Difficulty and submission" list and the field text above. Check them in that order against the worksheet, not from memory.
2. **Counter-readings.**
   - "Inflated": each line has a measured volume and an anchor rate, or a stated reason for a slower rate.
   - "Solution-path estimate": every manifest trap and forced error has a dead-end or workaround line.
   - "Evaluator-wide volume": the scoped-service counts are persona-filtered.
   - "Tier mismatch": decide whether the scope or the tier is wrong. Report it; do not tune the number.
   - "Linter reading": judged from the prompt and the SQL alone, as the V1 reasonableness linter did, does the stated scope justify the hours within 3×? If not, the volumes are missing from the reasoning.
3. **Re-verify** every volume through `hg.py`. A figure carried over from the dossier or an earlier pass is a lead, not evidence.
4. **Recompute** the sum and the character count after any change.
5. **Record** each check's result, each counter-reading and how it was resolved, and anything left unresolved (gate minimum: the five counter-readings above, each with evidence).
6. **Stage gate.** `python3 Task_Authoring/tools/stage_gate.py humantime Task_Authoring/task_inputs --paste`: it re-adds the minutes against the hours, checks the 0.25 step, the 50–2,000 character line, a measured volume per row, dead-end/workaround/write lines, the sources line, and that the worksheet is newer than the prompt (and than the OEs or baseline on a refresh).

## Deliver

Handoff is blocked until `stage_gate.py humantime` prints PASS; its output sits in the Self-review.
Report the hours, the sub-task table, the tier check and the pass (first or refresh).
Remind the human that the field is required and blocks both pasting and copying.
