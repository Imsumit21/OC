# 09 — Rubric Writing: coverage plan (prep) + rubric check (Playbook) — HarmonyGames · Spec V2

> Command: `/create-rubric-writing` (prep) · `/create-rubric-writing draft` (draft) · `/create-rubric-writing check` (check) · Writes: `task_inputs/Working_Files/09_Rubric_Writing_Plan.md` / `task_inputs/Working_Files/09_Rubric_Check.md` · Coverage seed: `task_inputs/Working_Files/01_Gradable_Surface.json` when present · Paired eval: `/rubric` · Gates: **`tools/stage_gate.py rubric-writing` / `rubric-check` (blocking)** · Read first: `setup/GEN_EXECUTION.md`, `plans/Fold_Hardening_Into_Scenario_And_Injection.md` §4.6

> **Claude, Codex or the human writes the rubric criteria.** This stage prepares the facts, drafts the criteria on request, and checks whatever was written — GEN_EXECUTION §2.

## Purpose

Claude or Codex may draft the rubric criteria (GEN_EXECUTION §2); the platform's Criteria Builder
opens empty (prefill is off), so drafted criteria are entered there and exported. The last audit's top defects were incorrect (22%), non-atomic (22%) and
missing coverage (21%), then unauthorized (6%) and overly specific (5%). Rubrics failed
correct answers (44%) more often than they passed wrong ones (29%)
(`Task_Authoring/references/Docs/8_Rubric Writing - V2.md` §10).

Release `task-quality-v1` (`dual-universe-v1`). The verdict block is rubric scoring-record format 5: per row `valid_case`, `do_nothing_case` and source `reachability`, plus one `final_reply_test` and `oe_cross_check` (`Evals/references/rules/review_scoring.md`); the rubric ledger is format 2, so an old ledger forces a FULL review (`rubric_flow_v2.md`).

The plan targets those defects. It lists everything that must be graded, the final
state that proves it, the values a self-contained criterion must name, the category
decision and the weight band. Draft mode (on request) writes the criteria from the plan
into `09_Rubrics.json`. `check` mode lints the builder export, whoever wrote it, against the plan, the twelve-point checklist and every
`/rubric` check, with `/rubric`'s severities.

When `/create-scenario` wrote a gradable surface (`Working_Files/01_Gradable_Surface.json`: the fact slots the
deliverables make gradable), the plan starts from it and accounts for every slot: covered by a row, or dispositioned
with a reason (`surface.coverage`, gate 17).

## Writing the criteria

- Claude or Codex may draft, rewrite or polish criteria (and OEs) — GEN_EXECUTION §2.
- The plan describes what must be verified as rows of noun phrases plus values ("owner notification — recipient = F4"); it may also carry draft criterion text.
- `check` quotes the span, names the rule, states the defect and cites the plan row, and may propose replacement wording, splits, merges or reweights.

## Inputs / Output

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`
and read `Working_Files/00_Task_Context.json` (GEN_EXECUTION § 0). Use all eight
assignment fields, the assigned freeze and the context's registered universe/KB source.
The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is missing — there is no default. Check each relied-on fact at
the assigned freeze; shared KB summaries are leads, not a separate dataset gate.
V3 changed-topic rules take
precedence over the older V2 reference documents in `references/Docs/`; local authorship and hardness-profile
exceptions remain as recorded in GEN_EXECUTION § 2 and § 3a.

Prep inputs (`task_inputs/` = `Task_Authoring/task_inputs/`):
- `04_Prompt.txt` — required.
- `08_Oracle_Events.md` — **required, stop if missing** (the plan uses it as the path reference). `/rubric` itself does not require an `/oe` PASS (it treats a supplied OE as a comparison reference); if `/oe` has not passed, proceed only when `08_OE_Check.md` shows no BLOCKING finding, and mark the plan PROVISIONAL. A PROVISIONAL plan is a working state, never a release state: after `/oe` passes, re-run prep, set `OE status: /oe PASS <date>` and re-gate (`stage_gate.py release` blocks any PROVISIONAL marker and an OE check whose Task solvability is not SUPPORTED_BY_OE).
- `08_OE_Writing_Ledger.md` — required (values, write capability, traps, open risks); if missing, run `/create-oe-writing` first.
- `00_Assigments.md` (persona, tier), `03_Error_Async_Config.txt`, `02_Reference_Files_Manifest.md`, `05_Human_Time_Worksheet.md` if present (set-size sanity).
- `01_Scenario_Design.md` (§10 grading devices: cohort multisets, aggregate invariants, spot-check groups) and `01_Hardness_Manifest.json` (chains → `ends_in`, traps → requirement, authorities → `governs`) if present — they say which requirement each independent difficulty lands on.
- `Working_Files/01_Gradable_Surface.json` if present (`/create-scenario` S6b; `tools/gradable_surface.py`): the fact slots the deliverables make gradable, each with a stable fact ID, a work-kind weight, a role (sample · exception · volume · core), the mechanisms that can flip it and its incorporating span. It is the **coverage seed** (Step 0) and the slot list gate 17 accounts for. `Working_Files/01c_Preflight_Report.json` (`/create-injection` S5e) lists each slot's solver value (`surface.expected`) and the mutants that flip it (`surface.flipped_by`). A slot is a lead, never an authority: it adds no requirement the prompt does not incorporate (gate 3), and a solver value is still re-read from its source record (gate 5).
- Universe: `Task_Authoring/tools/hg.py search` to re-verify values (`get` takes a service-relative `--file`, e.g. `--file contacts.json`). Tools: `Evals/references/tools/catalog.json`.
- Rules: `Evals/3_Rubrics_Eval.md` in full (Phases 1–5 and the `hg-strict-overrides-v1` table — stricter than the Docs and applied by `/rubric`); `Evals/references/rules/qc_rubric_v10.md`, `coherent_record.md`, `rubric_sampling.md`, `rubric_factual_checks.md`; `rubric_qc_examples.md` and `rubric_qc_cases.json` (historical calibration, not policy); Docs in `references/Docs/`: `8_Rubric Writing - V2.md`, `7_Oracle Events V2.md` §8, `10_Long Horizon Guidelines - V2.md` §9, `9_Common Errors & Pre-QC - V2.md` §8, `4_Persona ACL Policy - V2.md` §5 and §9, `QC_Spec_Doc_Latest.csv` (Rubrics rows); `references/Taxonomy_V2_Step_Map.md` step 51 (builder: minimum 5 criteria); `Evals/Docs/Original_Conference_Guidelines_Example_Task.pdf` (the ML-selected example task).
- **V3 overrides conflicting V2/Evals rules on changed topics.** Fair alternatives, source-cited expected values, global fact duplication, Pacific/UTC date acceptance and assigned mode caps follow V3. Preserve unchanged local checks (title-only, affirmative titles, Outcome balance, work-kind weights and binary validity).

Check inputs: the above, plus `09_Rubric_Writing_Plan.md` (required — run prep first)
and `09_Rubrics.json`, the builder JSON export (required — stop if missing).

Output: `task_inputs/Working_Files/09_Rubric_Writing_Plan.md` (prep) or `task_inputs/Working_Files/09_Rubric_Check.md`
(check); draft mode writes `task_inputs/09_Rubrics.json`.

## Hard gates

1. **Prompt and OEs first.** No prompt or no OEs, no plan.
2. **Drafts grounded.** Drafted criteria (draft mode) cite a plan row and re-read every literal value in this run.
3. **Prompt-traced.** Every row quotes a prompt span. An OE result the prompt never asked for is not a row (unstated expectation). A discovery OE maps to the row whose final state proves it.
4. **Outcome first.** Every write OE → a result row, plus one content row per requirement the prompt sets for it. Every fact the user asked to be told → a final-response row. Process only as a candidate, for ordering (rarely source verification) that no Outcome can prove, with the three-condition test recorded per condition. When in doubt, Outcome.
5. **Source-cited values and date alternatives.** Re-read every expected value from its actual source field, with a reachable record path, and match it exactly or document its calculation/rounding. Accept every fair precise/rounded figure and anonymized source token. **Identifiers:** unless the prompt asks for the full form, accept any unambiguous prefix of a hash or id (7 or more characters, matching only that record). A correct Season Pass run wrote 8-character SHA prefixes. **LITERAL claims:** event keys (`quest_completed`), ticket keys, prefixed record IDs, long hex IDs and anonymized tokens each bind as LITERAL, and the evidence names the record holding each expected value; accept every rendering the tools return (prefix, case, repo-qualified, short SHA, token such as `[PERSON_NAME_0854]`). Use the shared assigned freeze. Human-facing dates use Pacific, with UTC alongside when days differ; accept either date unless the prompt explicitly requests one timezone, and never require an exact time for a date-only ask. A date row for an instant whose PT and UTC days differ accepts both (`pt_or_utc_date`, state both); prose dates with month, day and a four-digit year can bind as DATE, yearless prose dates cannot. A length, line, sentence or section count is a format: grade it only when the prompt states the count. Record the actual source value, accepted outcomes, derivation and date acceptance in the V3 sidecar (Guide schema).
6. **One fact per row; global duplicate limit.** Each criterion tests one fact and traces to an exact prompt span. Keep a stable `fact_id` across deliverables and recipients. The same fact in **three or more rows fails** under V3; a repeated figure in document/ticket/reply does not become three independent facts. Remove redundant grading while retaining fair coverage, rather than using recipient/deliverable labels to disguise duplication. Unchanged coherent-record exceptions cannot be used to bundle independently passable facts.
7. **Four prohibitions** (`8_Rubric Writing - V2.md` §6). No unstated expectations. No single conclusion on ambiguous evidence unless a careful human reading reaches the same answer. Grade how a distractor is handled, not its disclosure. No hard-coded titles or phrasings the prompt did not specify. Under the Evals overrides a **prohibition-only or absence-only** acceptance always fails Negative Criteria, and so does any row an idle Agent passes: a row passes only when an Agent that makes no writes and gives no answer fails it. `leaves … as found / as is / unchanged / untouched / open / off` and `keeps … off` fail however worded. Cover an exclusion as a condition on a write the Agent must make (an exact count or scope, e.g. "closes exactly three of the leftover reviews") or as a requirement inside a required artifact, and drop exclusions nobody asked about (`do_nothing_case`, 5.3; Eval 3 §2.9). **Hardness v2** (Part 6, trap 9) asks for a "guard row" on an item correctly left unchanged and "grade that the agent leaves those items alone": here that is the exact count or scope on the required write ("creates vendor charge records for exactly 17 of the 20 receipts", "labels exactly 17 emails"), never a standalone leave-alone row, because the grader fails any row an idle agent passes (`Hardness_Mastery.md` §10; the Agentic Benchmark Checklist, arXiv 2507.02825, asks the same of a do-nothing agent).
8. **Weight by the kind of work** (QC Spec V2 "Criteria Weights", applied by the Evals override): 1 = direct lookup or literal check from one source; 3 = interpretation, calculation, comparison or limited reconciliation; 5 = multi-source reconciliation, deeper reasoning, cross-modal evidence or tracing. Record the kind and its reason per row. Only 1/3/5. Essential-and-easy is still 1. Hardness v2 says "put weight 5 on the trap rows": that holds only because the trap decides 5-band work. If a designed mechanism decides only 1- or 3-band rows, the fix is upstream (move the evidence onto the decision path or change the work in `/create-scenario --revise`; `hardness_v2_check` DECISION_FLIP), never a raised weight. **Wrong inputs to a total** (v2 trap 8): grade the corrected input and the final figure on two separate rows — two rows for one fact is legal under gate 6; three is not.
9. **Passable.** Every write row cites a feasible ledger write. No row depends on evidence outside the persona's view, requires describing a restriction the agent only saw as "not found", expects a successful retry on a rate-1.0 tool, or grades recovery as a non-action. Visibility is proven, not asserted: for every scoped record behind a row's F-IDs, paste the `python3 Task_Authoring/tools/persona_view.py can-see <persona> <service> <id>` YES line (seeded records: the `check-sql --load-bearing` row) under section E ("Visibility proof"). The gate resolves each row's F-IDs in the ledger, re-runs every pasted line, and blocks a mismatch or a missing line. It also re-runs `persona_view` on **every** scoped id behind every cited F-id, pasted or not (`reach.plan_fids`), so leaving an id out of the paste hides nothing.
10. **Every fair outcome.** Reuse brief §4b acceptance for all requested deliverables. A second fair material outcome is allowed when every fair result passes. Do not force a single conclusion when records support alternatives, reject source tokens, or add prompt answer-key clauses merely to eliminate variants. Each row's `accepted_outcomes` and `alternatives_review` in the sidecar record the strongest defensible alternatives. Keep requested destinations/recipients explicit where known, and distinguish actual unauthorized/wrong results from accepted variants. A figure the saved prompt report marks `BOTH_FAIR_FIGURE` ("Rubric must accept: X or Y") is a required alternative: a row grading it accepts either value, or the row is `overly_specific` (Major; `3_Rubrics_Eval.md` Local Overrides, 2026-10-17).
11. **Evals overrides** (`Evals/3_Rubrics_Eval.md`). Self-containment is **title-only** — the values a row lists must all be nameable in the title; the prompt, sibling titles, justification and evidence supply none. No ranking word (`primary`, `main`, `chief`, `principal`, `leading`, `mainly`, `largely`, `generally`, `overall`) that admits what it outranks — record the exclusion as a value. Multi-recipient content is planned per recipient unless one message to everyone is the graded artifact. Rows that would all fail on one agent error because each embeds the same acceptance condition form one cascading-overlap group — note each group (a write row and its own content row never form one). **Predicted all-fail:** mark any row whose values the persona cannot reach, on one of the four Evals bases — `target_data_absent`, `required_tool_absent`, `filter_impossible`, `entity_unreachable`. **One or more blocks handoff (tolerance 0).** The harness is deliberately stricter than `/rubric`, which fails the rubric only at two or more: a row already known to be impossible caps every run's score and makes the task look harder than it is. `stage_gate.py rubric-writing` blocks a non-zero count in §E or any A2 row naming a basis (`validity.predicted_allfail`). Over-specific acceptance is a separate risk (it fails correct runs and becomes an invalid all-fail after the verifier): note it in A2, not as predicted all-fail.
12. **Failure diversity.** Map each independent chain, hidden authority and trap requirement from the manifest to the row(s) it decides. **Unit of discovery:** one authority (a chain, authority or trap id in A2 "Decided by") or one tool response (ledger F-ids that share one locator record count as one unit, however many F rows the response was split into). **Weight share per unit is transitive:** a row counts for every unit in the Depends-on closure of its F-ids (ledger §B "Depends on" and "Locator origin" edges), plus its Decided-by ids. A fact whose locator the prompt itself supplies (origin `prompt`) is handed over, not discovered, and is not a unit. No unit may decide more than half of the total weight (`diversity.authority_share`, computed by the gate from A, A2 and the ledger). Independent chains land on different rows, so failing runs differ on ≥ 2 rubric results (the failure-pattern gate). *Residual:* this is a static proxy; whether failing runs actually differ is measured only by the baseline's failure-pattern gate (empirical ablation is out of scope).
13. **Stage gate.** `tools/stage_gate.py rubric-writing` (prep) and `tools/stage_gate.py rubric-check` (check) PASS; handoff is blocked until they pass.
14. **No shortcut source** (red team B, R1 #5 and 1). Run `python3 Task_Authoring/tools/shortcut_probe.py <persona> Task_Authoring/task_inputs/Working_Files/09_Rubric_Writing_Plan.md` and paste its output under §F. It takes the acceptance values (section A's Values column: backticked literals, or the ledger's Expected data for a bare F-id) and the population key sets (section D). It searches every persona-visible scoped service through `persona_view`, every unscoped service through `hg.py`, and the injection SQL overlay. It reports any single record that holds ≥ k (3) of the values or ≥ 50% of one population's keys: a shallow answer-bearing source that collapses the task. Each reported item stays blocking until a line outside the paste reads `SHORTCUT-OK: <service> <record> — <reason>` (for example, the record is the designed authority the task makes the agent find, or it is visible only after the discovery it would shortcut). The gate checks the values digest, k ≤ 3, all services and the SQL overlay, re-runs the probe (`--rerun all`), and blocks any undispositioned hit. A shortcut is fixed in the universe (`/create-injection`, `/create-hardening`), never by dropping a row.
15. **Populations: volume row + direct exceptions + ≤ 5 samples, no bundled exact set** (R1 #6, revised 2026-10-05). A population the prompt requires (its "every" / "all" / "which ones" set) keeps the Evals spot-check rule: at most 5 sampled items (hard and edge cases plus one ordinary) and **one volume row per sampled output** (the exact count in that cell, list or record set). Every member the prompt or an authority singles out as an exception (a takeover, the one item outside the default rule) gets its own direct row. **Do not write an exact-set or exact-map row**: listing many items in one title is a bundle of independently variable assertions — Not Atomic (Major) — whether the items are separate writes (`3_Rubrics_Eval.md` 2.2) or ids in one cell (Rubric Writing §7: the worst recorded case was "eleven assertions about one artifact"); controls do not waive atomicity (`qc_rubric_v10.md`). In §D write `none — bundle (Rubric Writing §7; Eval 2.2)` in the exact-set column (`structure.exact_set_rows`). A **core requirement** is defined by the prompt, not by an author label: anything the prompt asks for on its own (a deliverable, a told fact, a determination, an explicit exclusion, a named item) is core, is graded directly and is never spot-checked. Only the repetitive per-item members of a population, of comparable importance, may be sampled. Weights follow the agent's work, not the grader's: a volume row whose count only the full audit produces is multi-source work (5), not a "lookup".
16. **Multi-recipient content and title-only findings** (task-1 blind audit, 2026-10-05). Content may be bundled across recipients only when ONE message addressed to everyone is the graded artifact (`3_Rubrics_Eval.md` override "Multi-recipient content"): grade that single message's recipients in one row and its content in the next rows, and do not accept a "completing second send". Every acceptance-bearing finding sits in the title — a diagnosis only in `evidence` is `not_self_contained`. Wrap-up "where it landed" rows name the artifact (the sheet), not a tab, and never embed a count another row grades (a shared embedded condition is a cascade group). If the universe holds a second plausible source for a value (e.g. another warehouse table), name the exact source in the incorporated line or accept both.
17. **Gradable-surface coverage** (`surface.coverage`; plan §4.6). When `Working_Files/01_Gradable_Surface.json` exists, the plan is seeded from it (Step 0), and every slot an incorporated requirement makes gradable is either covered — a row whose title predicate rejects both the omission and a plausible wrong value of the slot's fact on the correct artifact — or dispositioned with a reason in §G. This follows the `missing_coverage` rule: a slot with neither is a coverage gap. Prep records the count in §E (an unticked box fails `stage_gate.py rubric-writing`); check mode lists every slot under `Coverage — gradable surface`, where each `gap` is one `missing_coverage` finding and blocks (`validity.rubric`). The gate check `surface.coverage` (rubric-writing and rubric-check, blocking) reads the slot list and the table:
   - every slot needs a line naming a covering row (P-n in §G, C-n in check mode), or a disposition with its reason: one of the four labels with why, or another reason with its evidence (a record id, row id or gate number);
   - a slot without a line, a line with neither, a `gap`, a bare label and a line for a slot the surface no longer has (stale) all block. The surface never adds a requirement (gate 3), never sets a weight (gate 8: kind of work) and never picks the sampled members (gate 15: hard and edge cases plus one ordinary). The **mechanism share** — the weight on rows that cover a slot a designed mechanism can flip — is reported, not gated, so no row is chosen, dropped or re-weighted for forecast loss.
18. **OE cross-check, both ways** (`oe_cross_check`; `3_Rubrics_Eval.md` 3.1). Every row maps to at least one OE step, whose label is quoted verbatim from the saved OE. An unmapped row is fixed as `ROW_DEFECT` (record its issue) or sent back as `OE_GAP` (the OE missed an authorized step); a row that would fail an Agent doing exactly what the OE says is a conflict settled from the records as `FIX_ROW` (with the row's issue) or `FIX_OE`. An OE edit after this review makes it stale — re-run the cross-check.

## Procedure — prep mode (checklist)

- [ ] Read GEN_EXECUTION, this playbook, `8_Rubric Writing - V2.md` and `7_Oracle Events V2.md` §8. Load inputs; stop per gate 1.
- [ ] Step 0 — Seed from the gradable surface (gate 17; when `01_Gradable_Surface.json` is absent, write `no gradable surface` under §G and start at Step 1). One candidate section A row per slot: stable fact ID = the slot's `fact_id` (else its id); source = its `incorporating_span`, re-quoted from the prompt (a slot whose requirement no prompt span incorporates gets no row; disposition it `not incorporated`); what must be verified = its selector and deliverable; A2 kind and band = its `work_kind` and `work_reason`; spot-check group = its `role` / `group` (the surface's sampled members are candidates; choose per gate 15); Decided by = the trap / chain ids of the `mechanism_portfolio` entries its `mechanisms` name (gate 12 counts trap and chain ids, never rule ids). Step 1 then confirms each seeded row against the OEs and adds what the surface does not hold (final-response rows, friction outcomes).
- [ ] Step 1 — Outcomes. Walk the OEs in order. Write event → result row (target, recipient, location) + one content row per prompt-set requirement. Discovery event → the content or final-response row that carries its result (section B); no separate row unless the prompt asks for that result itself. Each Tell requirement in the ledger → final-response row.
- [ ] Cross-check with the ledger: every requirement R has a row; every OE appears in section B.
- [ ] Step 2 — gaps. List requirements no Outcome row can verify: ordering stated or implied by the prompt (A before B, one step gating another); rarely, source verification where the right answer also sits in a shallow source and no Outcome can be made specific enough.
- [ ] Step 3 — three-condition test per candidate: (1) required by every valid path, or phrasable broadly enough; (2) no stricter Outcome can capture it; (3) a behavioural property, not an execution trace. Record each condition with its reason. Any fail → name the Outcome row to tighten and the value that tightens it.
- [ ] Fill values from the ledger and re-verify each in the universe (`tools/hg.py`, the SQL statement for seeded values) — a ledger value is a lead; record the pointer in the Self-review.
- [ ] Prove visibility for every scoped record behind the rows (gate 9) and paste the `persona_view` lines.
- [ ] Per row mark: title/phrasing specified by the prompt (quote it, or "no — must not hard-code"); distractor present (ledger T-ID → grade handling); ambiguous evidence (ledger risk # → no single conclusion); kind of work with a reason; weight band; the chain / authority / trap that decides it; predicted all-fail risk.
- [ ] Format 5 (§A3): per row a `valid_case` (a prompt-allowed answer the row must ACCEPT, built from what the prompt actually asks — "keep it short" allows any length), a `do_nothing_case` that must REJECT (quote the exact title text of the write an idle Agent never produces), the verbatim OE step ids that reach it, and the deciding source's `reachability` (`PROMPT_LINKED` required); then one whole-set `final_reply_test` (a concise final reply a valid run could give must pass).
- [ ] Failure-diversity check (gate 12): weight share per unit of discovery (authority or tool response), transitive over the ledger's Depends-on edges; no unit above 50%.
- [ ] Spot-check: for repetitive items of equal importance, choose ≤ 5 hard or edge items per group (say why each) plus one volume row with the expected count. Never spot-check a core requirement (gate 15: defined by the prompt span, not by a label); never one row per line of a long output. Each sampled population gets one volume row per output and direct rows on its exceptions, never a bundled exact-set row (gate 15: `none — bundle (Rubric Writing §7; Eval 2.2)` in §D); list its keys as backticked literals in the §D "Item set" cell so the shortcut probe can test them.
- [ ] Duplicate risk across the complete rubric: map every criterion to a stable fact ID; no fact may appear in three or more rows, even across requested deliverables. Record and remove redundant rows before grading.
- [ ] Surface coverage (gate 17): fill §G with one line per surface slot: the row(s) that cover it, or a disposition and its reason — `sampled out` (its spot-check group samples other members, gate 15), `duplicate fact` (graded in other rows, gate 6), `not incorporated` (no prompt span or incorporated authority asks for it, gate 3; report the slot to `/create-scenario`), `unobservable` (outside the persona's reach, gate 9; route it to the universe), or another reason with its evidence. Leave no slot with neither, then tick the §E box and report the mechanism share there (not gated).
- [ ] Final state: copy the canonical outcome reference (brief §4b) into the plan header. Rows grade material fields; delegated or representational fields are phrased broadly or left ungraded (gate 10).
- [ ] Friction: recovery appears as an Outcome on what the alternative source yielded; no row names the failing tool.
- [ ] Shortcut probe (gate 14): put each row's literal acceptance values in its Values cell (backticks), then run `python3 Task_Authoring/tools/shortcut_probe.py <persona> Task_Authoring/task_inputs/Working_Files/09_Rubric_Writing_Plan.md` and paste the output verbatim under §F. Disposition every HIT / INCOMPLETE line with `SHORTCUT-OK: <service> <record> — <reason>` below the paste, or route the shortcut to `/create-injection` / `/create-hardening` and re-run.
- [ ] Fill the summary (section E — tick every box ☑ or mark it ☒ with the reason; an empty ☐ fails the gate), run the Self-review (prep), self-scan for criterion text (gate 2), write the plan.
- [ ] `python3 Task_Authoring/tools/stage_gate.py rubric-writing Task_Authoring/task_inputs --paste` → PASS (every cited F-id's scoped ids visible, predicted all-fail = 0, largest unit of discovery ≤ 50%, population volume/direct-exception rows, current V3 evidence, shortcut probe pasted and dispositioned).

## Plan template

Write exactly these headings and columns.

```text
# 09 Rubric Writing Plan — <task id>
Generated <date> · Clock <assigned freeze from context> · Persona <name> <email> · Assigned role <role> · Tier <…> · Mode <Easy | Medium | Hard> · Human time <h> · OE status: /oe PASS <date> | PROVISIONAL
Canonical outcomes: brief §4b (all fair results and accepted alternatives)

## A · Coverage matrix
| P | Source (exact prompt span · OE n) | Stable fact ID | What must be verified | Final state that proves it | Category (Outcome / Process candidate → C) | Expected/source values and pointers · accepted alternatives · date acceptance · F-IDs |

## A2 · Grading risks and weight
| P | Title/phrasing specified by prompt? | Distractor? (T-ID → grade handling) | Ambiguous evidence? (risk # → no single conclusion) | Kind of work (lookup / interpretation · calculation · comparison / multi-source · tracing) + reason | Band 1/3/5 | Decided by (chain / authority / trap id) | Spot-check group | Global fact duplication / overlap group | Predicted all-fail basis (four Evals bases) · over-specific risk |

## A3 · Format 5 — per-row acceptance cases, OE steps and reachability
| P | valid_case (must ACCEPT · prompt authority) | do_nothing_case (must REJECT · exact title text of the required write) | OE step ids (verbatim OE labels) | Deciding source reachability (PROMPT_LINKED / TRASH / ATTACHMENT_ONLY / UNLINKED) |
Final-reply test (whole set): <a concise final reply a valid run could give> → ACCEPT ☐ (a rejecting row needs its `overly_specific` or `unauthorized` issue)

## B · OE trace
| OE | Kind (write / discovery / friction) | Proved by row(s) | Own row? (reason) |

## C · Process candidates — three-condition test
| P | Requirement (prompt span) | Why no Outcome can prove it | (1) every valid path | (2) no stricter Outcome | (3) behavioural, not trace | Result (Process / tighten P-n with F-n) |

## D · Spot-check groups
| G | Item set (F-IDs, total N; keys as backticked literals) | Sampled items (≤ 5) and why hard/edge | Volume row | Exact-set row (`none — bundle (Rubric Writing §7; Eval 2.2)`) | Core requirement? (must be no) |

## E · Summary
Rows N · Outcome N · Process candidates N — ≥ 1 Outcome ☐ · Process rows ≤ 50 % ☐ · fewer than two Process rows failing the three-condition test ☐ (2026-10 Rubric Writing / Read This Before You Submit: either one is a failing error) · builder minimum 5 ☐ · one volume row per sampled output, no bundled exact-set row ☐ · predicted all-fail rows = 0 ☐ (harness tolerance 0; /rubric fails at ≥ 2)
Failure diversity: largest unit of discovery (authority or tool response, transitive) N% of the weight (≤ 50% ☐) · chains landing on distinct rows ☐
Bands: 5 ×N · 3 ×N · 1 ×N
Format 5 (§A3): rows N/N ☐ · `do_nothing_case` REJECT N/N ☐ · reachability `PROMPT_LINKED` N/N ☐ · final-reply test ACCEPT ☐
Set size: N rows for <h> h (reference: 31 criteria for a ~10-hour task; ~60 signals duplicate grading, ~12 missing coverage)
Coverage: requirements N/N · OEs N/N · writes N/N · told facts N/N · friction N/N
Gradable surface (gate 17): slots N · covered N · dispositioned N (§G) · no slot with neither ☐ (☒ when the task has no surface) · mechanism share N% of the weight (reported, not gated)
Four prohibitions: ☐ unstated expectations ☐ conclusions on ambiguous evidence ☐ grading the distractor ☐ hard-coded titles/phrasings
Blocking: <UGT defects · infeasible writes · unverified visibility>

Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)

## F · Shortcut probe
<tools/shortcut_probe.py output, pasted verbatim in a fence>
SHORTCUT-OK: <service> <record> — <reason>   (one line per HIT / INCOMPLETE line; none when the verdict is CLEAR)

## G · Gradable-surface coverage
| Slot | Stable fact ID | Selector · role / group | Work kind (band) | Mechanisms → Decided by | Covered by (P-n) | Disposition and reason (evidence) |
(one line per slot of 01_Gradable_Surface.json; `no gradable surface` when the task has none)
```

## Procedure — check mode (checklist)

For both prep and check, maintain `Working_Files/00_V3_Authoring_Evidence.json`
using the Guide schema: current context/prompt/rubric hashes, criterion IDs, stable
fact IDs, exact prompt spans, accepted outcomes, alternatives review and actual
source fields. Cite JSON with absolute or workspace-relative paths inside the
selected universe's source (`source.paths`); seeded SQL uses `source_file: "01_Universe_Inject.sql"` with
table/identity/column. Each source needs a useful `evidence_path` and
`reachability_rationale`. A pointer must lead from requested work: unreferenced
comments, Trash and attachments must not hide deciding evidence; seed a usable
link in a record the prompt leads the agent to open. Lower weight or a vague hint
does not repair unreachable evidence. The gate checks supplied fields and path
records; it does not prove the semantic fairness of the author's review.

The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is missing — there is no default. Each source record needs
`temporal_evidence` (Guide schema) naming its actual recorded timestamp and value
semantics. Later deadlines/events can remain future values, but their source record
must already exist at the freeze. A mutable current body needs a freeze-state
review citing dated history or independent earlier records in its evidence path;
an old creation date by itself cannot certify later-edited content.
Immutable directory/contact identifiers may use the Guide's `directory_identity`
exception with `mutable_state: false` and a rationale; it does not establish an
earlier task state or employment/role history.

After the verifier, check every failed row for fairness and source correctness,
correct errors and re-grade the six rollouts before evaluating the assigned mode's
cap. If the corrected task is too easy, harden the universe; do not add or tighten
criteria to reduce the average or delete a valid check just because its key was wrong.

Walk the checks in `/rubric`'s order (`Evals/3_Rubrics_Eval.md` Phases 1–5). For every row
record: requirement → title predicate → valid alternative → plausible near miss → finding.

- [ ] **Intake (schema gate).** Load `09_Rubrics.json` and the plan; stop if either is missing. Edit neither. If the JSON does not parse or is not an array of criteria, report where it breaks, readiness FAIL-RISK (schema-only, `3_Rubrics_Eval.md` 1.2), and stop — the human re-exports from the builder; never repair the file. Record the key map (criterion/title, weight, category, justification, evidence). Every row needs all five non-blank; category `Outcome` or `Process` (letter case is cosmetic — note it); weight an integer 1, 3 or 5. A blank field or invalid value fails the schema gate.
- [ ] Number criteria C1…Cn in file order. The denominator is the authored count; fewer than 5 breaks the builder minimum (taxonomy step 51).
- [ ] **Lint before reading.** Run `python3 Task_Authoring/tools/hg.py rubric-lint Task_Authoring/task_inputs/09_Rubrics.json` (the eval's `hg_rubric_lint.py`) and clear every `disguised_negative`, `format_lock`, `anon_token` and `evidence_no_record` hit; record every `vague_exemplar`, `tool_name`, `prohibition_title` and schema hit with its verdict.
- [ ] **Coverage (hard gate; Eval 1.4, 3.1).** Build the requirement list from the prompt and what it clearly incorporates, then check it against the plan (an unmentioned handbook adds nothing). A requirement is covered only when a title predicate rejects **both** its omission and a plausible wrong result on the **correct artifact**; topic similarity, a heading mention or a justification is not coverage. Check in particular: every write the prompt assigns to the Agent has a result row and its prompt-set content (a content row that requires the write covers both); every fact or verdict the user asked to be told has a final-response row (rows on a post or record do not cover the reply, and vice versa); a determination ask has a row on the verdict itself; both halves of a compound ask; a required exclusion or decoy has a row rejecting the all-inclusive answer; a required population has a volume row per output plus its spot checks and direct exception rows (gate 15) — an exact-set or exact-map row is `non_atomic` (Major), not coverage; cross-deliverable facts keep fair coverage without grading the same fact in three or more rows (gate 6); a draft does not satisfy a send, nor a note a requested status change. Judge final-state rows against the canonical outcome (brief §4b): a row that rejects a representational variant inside the allowed equivalence class is `overly_specific`; a row that accepts an unsupported material value is `overly_broad` or `incorrect`; a fair alternative is accepted. Each missing outcome is one `missing_coverage` entry (numerator only). A write row for an action the prompt leaves to the user ("I'll post it") is `unauthorized`. An OE result the prompt never asked for is an OE defect, not a gap.
- [ ] **Gradable-surface coverage (`surface.coverage`, gate 17; follows `missing_coverage`).** When `01_Gradable_Surface.json` exists, list every slot under `Coverage — gradable surface`. A slot is `covered` only when a criterion's title alone passes the Coverage test above for the slot's fact; otherwise carry over the plan's §G disposition after re-checking its reason, or mark it `gap`. Keep the reason in its own column: the Covered / dispositioned / gap cell is read for gap words. Each gap is one `missing_coverage` finding (Major, numerator only) and blocks through `validity.rubric`, like any coverage gap. Report the mechanism share of the criteria weight below the table: reported, never gated, and never a reason to add, drop, tighten or re-weight a criterion (weights stay by kind of work).
- [ ] **Per-row lint.** Assign each finding its `/rubric` type (severity table below):
  - *Self-containment, title-only (2.1).* Hide everything but the title: every acceptance-bearing ID, value, status, destination, recipient and finding must be there. Flag "that message", "the designated channel", "the right person", "the correct figure", catch-alls that extend a named set of entities, values or routes ("or another account", "relevant vendors", "via email, Slack or similar") — and a catch-all route that admits a wrong completion (a draft for a send) is also `overly_broad`. "(or similar)" / "or equivalent" qualifying a meaning the title states in full ("confirms the lease is closed (or similar)") is a paraphrase allowance (2.10), not a defect. A title that names the topic but not the finding ("mentions the billing status for X") does not name its answer. A supporting field that **widens** acceptance → `not_self_contained`; one that **narrows** it → `overly_specific` if it changes grading, else `harmless_specificity`.
  - *Atomicity (2.2) — decompose every row.* Two or more claims that can pass or fail separately → `non_atomic`, including `at least N`, `any one of`, `X and Y` over independently required items, a filtered list ("A, B and C are done"), and a verdict bundled with its grounding. Apply unchanged exceptions (`coherent_record.md`) only where they still test one fact: attributes of one record (a PR and its own merge date), components of one evidenced tool output, the same content of **one** message sent to several people, a send plus the content that defines it, qualifiers and operands of one metric or comparison, premises of one causal finding. Content "delivered to both X and Y" when separate sends are accepted is `non_atomic` (and a cascade group if repeated). A disjunctive title is `non_atomic` when both branches are required, `overly_broad` when the "or" admits a wrong alternative. An "or" over a complete closed set of valid alternatives (two accepted channels, two accepted spellings) is valid flexibility, not a defect.
  - *Correctness and verifiability (2.3–2.4; `rubric_factual_checks.md`).* Re-read every literal through `hg.py` and the injection SQL (know which layer each value belongs to). `incorrect`: contradicts the records, the SQL or the clock; a literal found nowhere; an impossible derivation or imported qualifier; persona-scope error ("my projects" given an entity total); role overreach; a mandated write that an accessible human decision defers. `unobservable`: the value is not reachable at the required precision through cataloged tools, or only another persona can see the evidence, or passing depends on hidden tool returns. A count needs the complete candidate set; an absence claim needs a positive control. Evidence names the record holding each expected value; event keys, ticket keys, prefixed record IDs, long hex IDs and anonymized tokens bind as LITERAL, accepting every rendering the tools return; evidence that names no record is `evidence_no_record`. Unverifiable without SQL or source → UNRESOLVED, never a guessed defect.
  - *Objectivity and ranking (2.5).* `enough`, `professional`, `thorough`, `appropriate`, `comprehensive`, `sufficient`, `reasonable`, `adequate`, `properly`, `correctly`, `accurately` in place of a concrete target → the row does not name its answer (`not_self_contained`). Ranking words (list in gate 11) → `not_self_contained` (Major) when only a supporting field states the exclusion, else `overly_broad`.
  - *Specificity (2.7; anti-rationalization).* A valid prompt-authorized alternative the row rejects → `overly_specific`: channel or method lock-in where the prompt said "notify/reach out", content chained to a locked channel, a structured value the catalog does not require, a hard-coded title, heading or phrasing, a forced single conclusion on ambiguous evidence. Never excuse it as "the likely route". **Overly-broad test on every row in isolation:** a plausible wrong answer passes → `overly_broad` (**Major**); never argue a sibling row catches it; very unlikely wrong paths are not flagged. Never repair an overly broad row with a count, format or phrasing; name the value. A length, line, sentence or section count is a format: grade it only when the prompt states the count ("keep it short" grades no count; `format_lock`).
  - *Vague exemplar (2.7A).* `such as`, `e.g.`, `for example` in **any** field → `vague_exemplar` once per row (inside a verified immutable name: UNRESOLVED).
  - *What not to grade (2.8).* Unstated expectation or graded distractor → `unauthorized`; same fact graded again elsewhere → `duplicate`.
  - *Agent-centric and negative (2.9).* Subject an artifact or model ("The response states…", "The write-up…") or a catalog tool identifier in the **title** → `non_agent_centric` (Major) and the Agent-Centric dimension fails. "The Agent's report states…" and bare "Reports…" are valid nonstandard forms: dimension NON-FAIL, no tally issue. A tool name only in justification/evidence is a note (Docs say "anywhere"; `/rubric` permits it to locate evidence). Lexical pre-scan of every title: `does not`, `do not`, `must not`, `makes no`, `has no`, `no`, `not`, `never`, `without`, `avoid`, `refrain`, `fail to`. Prohibition-only or absence-only acceptance fails Negative Criteria even when the prompt prohibits the action; a positive second clause does not cure it; a reported negative fact ("reports that PR #438 had no review") is affirmative. **Do-nothing test:** a row passes only when an Agent that makes no writes and gives no answer fails it; `leaves … as found / as is / unchanged / untouched / open / off` and `keeps … off` fail however worded (lint: `disguised_negative`, `prohibition_title`). Cover an exclusion as a condition on a write the Agent must make (an exact count or scope, e.g. "closes exactly three of the leftover reviews") or a requirement inside a required artifact; drop exclusions nobody asked about (`do_nothing_case`).
  - *Category (2.6, 3.2).* A write or observable result labeled Process, or a Process row a stricter Outcome could capture → `category`. Record which of the three conditions each Process row fails.
  - *Clock and dates (V3).* Use the assigned freeze. A seeded record or completed event after it is incorrect; future deadlines/scheduled events may remain future. Display Pacific plus UTC when days differ; without a requested timezone accept both dates, and a split-day date row states both days (`pt_or_utc_date`) — one day only is `overly_specific`. Prose dates with month, day and a four-digit year can bind as DATE; yearless prose dates cannot. A date-only ask never authorizes an exact-time requirement. *Weight:* retain work-kind 1/3/5 for the atomic result.
- [ ] **Set-level (3.3–3.7).** Duplicates: wholly redundant row → `duplicate` per row; overlapping rows and cascading-failure rows → one `OVERLAP_GROUP` per shared condition, counted once after removing members already Major, no intersecting groups. A cascade group needs one embedded acceptance condition (the same recipient pair, the same wrong premise) — rows that merely share a likely root cause (one miscalculated value that each prompt-required deliverable must carry), or that fail only because their own artifact was never created, are not a group. Apply V3's global limit: the same fact in three or more rows fails, including across deliverables. A write row and an independently graded content fact can be distinct; record stable fact IDs rather than inventing IDs per occurrence. Spot checks (`rubric_sampling.md`): repetitive items of equal importance only; > 5 samples in a group → one overlap group; no volume row for a sampled output → `missing_coverage`; an exact set or map over many items → `non_atomic` (Major; Eval 2.2, Rubric Writing §7, controls do not waive atomicity); a sampled core requirement (core = asked for by its own prompt span, gate 15) → `missing_coverage` for the unsampled part; a weak sample choice is a note. Contradictions: rows (and each row's three fields) must be jointly satisfiable; a proven contradiction fails that repair gate — record the source-wrong row as `incorrect`. Mutation test: a complete valid solution (including correct delivery plus a concise reply) must pass every row; change one value, recipient, status or output outside its accepted fair alternatives at a time and name the row that rejects it — an unrejected change is a coverage or broadness finding. For a sampled population, an unsampled per-item error is the documented sampling limit (`rubric_sampling.md`), not a gap; a wholesale error must fail the volume row.
- [ ] **Predicted all-fail (5.1).** From defects already recorded, list rows that would fail every run on a basis of `target_data_absent`, `required_tool_absent`, `filter_impossible` or `entity_unreachable` (includes a successful retry on a rate-1.0 tool and evidence outside the persona's view). **One or more → FAIL** (harness tolerance 0; `/rubric` itself fails at two or more — the harness is stricter on purpose).
- [ ] **Binary validity gate.** Validity defects are not spent from a percentage budget. Any finding of these kinds blocks handoff, whatever the quality tally: `incorrect`, `unauthorized`, `unobservable` (including impossible), a contradiction (recorded on the source-wrong row as `incorrect`), `missing_coverage` (including a Coverage row marked gap), an `Unauthorized criteria:` entry, and any predicted all-fail row. `stage_gate.py rubric-check` exits 1 on any of them (`validity.rubric`). A finding the evidence cannot settle is UNRESOLVED: it does not block this check, and the release gate blocks it. Percentage tallies remain for the other types (`not_self_contained`, `non_atomic`, `overly_specific`, `non_agent_centric`, `overly_broad`, `duplicate`, `category`, `vague_exemplar`, `harmless_specificity`).
- [ ] **Tally and dimensions.** Count each row once at its highest severity; overlap groups once; missing outcomes in the numerator only. Apply the dimension table; give the threshold margin when the set is small (with 11 rows one Major is 9.1%).
- [ ] Run the Self-review (check), then write the report.

Severity — the `/rubric` issue types (`3_Rubrics_Eval.md` taxonomy + `hg-strict-overrides-v1`; `qc_rubric_v10.md`). `/rubric` decides; this is a prediction.

| `/rubric` type | Severity | Covers |
|---|---|---|
| `missing_coverage` | Major, one per missing outcome, numerator only | Uncovered authorized requirement or wrong artifact; missing volume row for a sampled output; sampled core requirement; a gradable-surface slot neither covered nor dispositioned (gate 17) |
| `not_self_contained` | Major | Title alone does not name the answer; catch-all; vague reference; subjective word in place of a target; supporting field widens acceptance; ranking word whose exclusion sits only in a supporting field |
| `non_atomic` | Major | Independent results outside the documented exceptions; `at least N` / any-one; disjunction of required items; multi-recipient content when sends are graded separately |
| `incorrect` | Major | Contradicts records / SQL / clock; fabricated literal; impossible derivation; persona scope; role overreach; deferred mandated write; source-wrong side of a contradiction |
| `unauthorized` | Major | Unstated expectation; user-owned action; graded distractor; unmentioned handbook rule; requires describing a restriction only seen as "not found" (ACL Policy §9 says Moderate — strictest governs) |
| `unobservable` | Major | Precision or evidence the persona's tools cannot reach; hidden tool returns; deciding source not `PROMPT_LINKED` (Trash/Spam, attachment-only or unlinked from the prompt) |
| `non_agent_centric` | Major + Agent-Centric FAIL | Artifact/model subject or tool name in the title |
| `overly_specific` | Major | Rejects a valid prompt-authorized answer (lock-ins, hard-coded title/phrasing, forced conclusion, narrowing supporting field, single day of a split PT/UTC date, unstated format/count, one value of a `BOTH_FAIR_FIGURE` fork) |
| `overly_broad` | Major | A plausible wrong answer passes; ranking word otherwise; "or" admitting a wrong branch. Never repair with a count, format or phrasing; name the value |
| `duplicate` | Moderate | Wholly redundant row (per row); overlap / cascading-failure / > 5-sample group (once per group) |
| `category` | Moderate | Write or observable result labeled Process; Process row an Outcome could capture |
| `vague_exemplar` | Moderate | `such as` / `e.g.` / `for example` in any field, once per row |
| `harmless_specificity` | Minor | Wording preference that rejects no valid answer |
| — (not tallied) | dimension or note | Prohibition-only title (Negative FAIL); nonstandard Agent form (Agent-Centric NON-FAIL); missing Process for a real ordering dependency (Process NON-FAIL); typo the judge still reads correctly; tool name only in a supporting field |

| Dimension (QC Spec V2 + Evals Local Overrides `hg-strict-overrides-v1`) | FAIL (1–2) | NON-FAIL (3–4) | PASS (5) |
|---|---|---|---|
| Overall Rubric Quality | Any Major or Moderate issue; Minor issues on > 10% of rows | Minor issues on 5–10% of rows (NON-FAIL 3) | No Major/Moderate, Minor < 5% |
| Criteria Weights | > 10% of rows one level off, or any row two levels off | 10% or fewer rows one level off and none two levels off (NON-FAIL 4) | All match |
| Category Balance | Zero Outcome rows; more than 50 % Process rows; two or more Process rows failing the three-condition test (2026-10 guides) | — | ≥ 1 Outcome, Process ≤ 50 %, < 2 unnecessary Process rows |
| Process Rubrics | 2+ genuinely missing ordering checks, or any invalid Process row | Exactly 1 genuinely missing ordering check (NON-FAIL 3) | No ordering dependency lacks a check and every Process row is valid |
| Agent-Centric Phrasing | 1+ artifact/model subject or tool name in a title; off-pattern agent-centric titles on > 10% of rows | Off-pattern but agent-centric titles (possessive, bare action) on ≤ 10% of rows (NON-FAIL 3) | The Agent + action in every title |
| Negative Criteria | 1+ prohibition-only / absence-only title, or any row an idle Agent passes (`do_nothing_case` ACCEPT), even with prompt authority | — | Every row rejects an idle Agent and is affirmative |
| Predicted all-fail gate | 1+ rows on the four bases (harness tolerance 0; `/rubric` fails at 2+) | — | 0 |
| Repair gates (no score) | Schema, self-containment, accuracy, atomicity, coverage, duplicates, weights, contradiction, format-5 cases (`valid_case`, `do_nothing_case`, `final_reply_test`, `oe_cross_check`) — a failure is reported; its tally issue carries the score. Schema, accuracy (`incorrect` / `unobservable`), coverage and contradiction are also **validity** defects: they block handoff on their own (binary validity gate) | | |

Readiness: **FAIL-RISK** if any dimension, the schema gate or the binary validity gate fails · **NON-FAIL-RISK** if any is NON-FAIL or a required fact is UNRESOLVED · **CLEAN** if all PASS. The lowest dimension controls `/rubric`'s verdict; any validity defect blocks handoff even when the tally alone would be NON-FAIL.

Calibration (35 historical QC cards, blind, 2026-10-04; `support/examples/calibration/rubric/`): this check caught every QC FAIL, but rated the historical NON-FAIL cards FAIL-RISK, because title-only self-containment, the atomicity rules and the Negative override are stricter than the QC that scored them. That is the intended direction: the check predicts `/rubric`. Do not soften a finding to match older verdicts.

Red-team triage (harness red team B, 2026-10-04; `support/examples/calibration/harness_redteam/B_prompt_oe_rubric.md` + `.second.md`, reviewed under the old names `09_Rubric_Coverage_Plan`, `08_Evidence_Ledger`, `04_Prompt_Brief`). Implemented: predicted all-fail tolerance 0 (gate 11), binary validity gate (check mode), unit of discovery + transitive share (gate 12), shortcut probe (gate 14), exact-set row and the prompt-defined core requirement (gate 15), one fact per prompt-required deliverable (gate 6), one final-state definition (gate 10), visibility re-checked for every cited F-id (gate 9), release gate (GEN_EXECUTION §6b). **Rejected, with the reason:**
- *Keep Process rows for long tasks when the Outcome does not prove the deep path (R2 #6).* This conflicts with the Evals Process rules (`hg-strict-overrides-v1`: a Process row that a stricter Outcome could capture is a `category` defect, and only zero Outcome fails its balance; the 2026-10 guides add > 50 % Process and ≥ 2 unnecessary Process rows as failing errors, so keep Process rows few and each one passing the three-condition test). A shortcut that lets a run reach the right Outcome is closed by design instead: the universe removes it (gate 14's `shortcut_probe`, `/create-hardening`), and the rubric does not grade the trace.
- *Allow negative criteria / typed behavioural prohibitions (R1 #12).* The Evals `hg-strict-overrides-v1` fail every prohibition-only or absence-only acceptance (Negative Criteria FAIL, even with prompt authority). An exclusion is covered as a condition on a write the Agent must make (an exact count or scope) or as a requirement inside a required artifact; a standalone row an idle Agent passes is a `do_nothing_case` ACCEPT and fails Negative Criteria (gate 7, 2.9). Transient violations that the final state cannot show stay ungraded (residual).
- *Full population verification replacing spot checks (R1 #6, the rest).* The Evals mandate at most 5 samples per group plus a volume row (`rubric_sampling.md`). Gate 15 (revised 2026-10-05) grades each population by one volume row per output plus direct rows on its exceptions; a bundled exact-set row would be Not Atomic. Per-item correctness of unsampled members stays ungraded (residual, as `rubric_sampling.md` documents).
- *Correction, not a rejection — exact-set row over separate writes (task-1 Hardened_v2 audit, 2026-10-05).* Gate 15 originally demanded an exact-set row for every sampled population; on a population of separate writes (8 status changes, 15 reassignments) that produced two Not Atomic (Major) rows. Gate 15 now forbids bundled exact-set rows altogether (a second audit pass found the one-cell lists also fall under Rubric Writing §7's "eleven assertions about one artifact"): every population uses volume + direct exception rows + ≤ 5 samples.

## Self-review (GEN_EXECUTION §6a — this stage)

Run before saving either output; record it under **Self-review** in that output. It may quote, judge and rewrite criteria.

Prep mode:
1. **Re-read as `/rubric`.** Walk `3_Rubrics_Eval.md` 1.4 and 3.1 against the plan: every prompt requirement, write, told fact, verdict, exclusion and friction has a row on the correct artifact.
2. **Counter-readings per row.** (a) Could a valid answer fail a criterion that names exactly these values — another channel, route, format, rounding, or a second reasonable conclusion? Resolve with evidence: mark "phrase broadly", add a tolerance, or record the ambiguity risk. (b) Could a wrong answer pass — the all-inclusive answer, the runner-up, the decoy, the stale value? Resolve by listing the excluding value or a separate exclusion row.
3. **Re-verify every value** the plan lists through `tools/hg.py` (and the SQL for injected values): record the command and pointer. A ledger value is a lead, not evidence.
4. **Predicted all-fail re-check.** For each row: the persona can reach the value through a cataloged tool at the stated precision (`persona_view.py can-see` YES for every scoped record, not an assertion), the write exists in the catalog, no rate-1.0 retry, no evidence outside the persona's view. Count rows on the four bases (must be 0 — gate 11). Gate minimum: one evidenced counter-reading per section A row.
6. **Shortcut and diversity.** Read the §F probe output: for every HIT, the strongest case that it collapses the task (could a run answer from that record alone?) and the disposition's evidence. Recompute the largest unit-of-discovery share (gate 12).
5. **Draft grounding** (draft mode). Every literal in a drafted criterion matches a re-read record; every criterion maps to a plan row.
7. **Surface dispositions** (gate 17). For every §G disposition, the strongest case that the slot needs a row after all: is it core (asked for by its own prompt span, gate 15)? Is its fact graded in fewer rows than the disposition claims? Resolve each with evidence.

Check mode:
1. **Re-read as `/rubric`** in phase order; apply the pre-verdict sweep (5.0): one missing requirement, one phrasing mismatch with the prompt, one non-atomic row, one category mislabel, one over-specific or hard-coded title, one duplicate or cascade group, one vague exemplar, one prohibition-only title. Calibrate each ruling against the 7-row table in `Evals/references/rules/rubric_qc_examples.md` (2026-10-17: do-nothing, valid case and count format, LITERAL key, PT/UTC day, reachability, anonymized token, OE conflict) — calibration, not policy.
2. **Counter-reading per finding** (false positive?): a documented atomicity exception, a descriptive negation, a valid possessive, permitted sampling, an immutable source name, a value the title does name. **Counter-reading per cleared row** (false negative?): try a valid alternative and a plausible near miss against the title alone. Resolve each with a rule § or record pointer.
3. **Re-verify** through `hg.py` every value a finding or a clearance depends on.
4. **Recount** predicted all-fail from recorded defects only, then the tally from the findings table (highest severity once, overlap groups once after removing Major members, missing outcomes in the numerator only).
5. **Fixes.** Any rewrite, split or merge the report proposes is grounded in a re-read record and the plan row it fixes.
6. **Stage gate.** `python3 Task_Authoring/tools/stage_gate.py rubric-check Task_Authoring/task_inputs --paste` (recomputes the criteria count from `09_Rubrics.json`, verifies every quoted span against it, checks issue types and the dimension table, applies the binary validity gate — `validity.rubric` blocks any incorrect / unauthorized / unobservable / contradiction / missing-coverage finding, any Coverage gap, any unauthorized criterion and any predicted all-fail row — and needs a counter-reading row naming every criterion C1…Cn).

Record: `| Check | Verdict | Strongest counter-reading | Resolution (evidence: pointer / rule § / case id) | Unresolved |`

## Check report template

```text
# 09 Rubric Check — <task id>
Checked <date> · Criteria N (builder minimum 5: ok / short) · Plan <date>
JSON field map: criterion=`<key>` · weight=`<key>` · category=`<key>` · justification=`<key>` · evidence=`<key>` · schema gate: pass / fail (<defect>)
Readiness for /rubric: FAIL-RISK (<dimensions>) | NON-FAIL-RISK | CLEAN — a prediction only; /rubric gives the verdict

## Coverage
| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |
Unauthorized criteria: <C-n list>

## Coverage — gradable surface
| Surface slot | Stable fact ID | Criteria | Covered / dispositioned / gap | Disposition reason (evidence) |
(one row per slot of 01_Gradable_Surface.json; `no gradable surface` when the task has none)
Mechanism share: N% of the criteria weight (reported, not gated)

## Findings
| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |

## Overlap groups · Spot-check groups · Predicted all-fail
| Group / row | Members / basis | Shared condition / reason |

## Dimensions
| Dimension | Count / % | Threshold | Status |
(Overall Rubric Quality · Criteria Weights · Category Balance · Process Rubrics · Agent-Centric Phrasing · Negative Criteria · Predicted all-fail · schema and other repair gates) · threshold margin

## Self-review
| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |

## Reminders
- An all-Outcome set is normal; Process is not added to look thorough.
- Fix the criteria (Claude, Codex or the human) in the builder, re-export, re-run check, then run /rubric.
```

## Deliver

Both modes: handoff is blocked until `stage_gate.py rubric-writing` / `rubric-check` prints PASS; its output sits in the Self-review.

Prep: report the path, row counts, Process-candidate results, the surface coverage (slots covered / dispositioned)
with the mechanism share (reported, not gated), and blocking items (UGT
defects, infeasible writes, unverified visibility). Next: `/create-rubric-writing draft` (or the human writes the
criteria from the plan), enter them in the builder, export the JSON to
`task_inputs/09_Rubrics.json`, then run `/create-rubric-writing check`.

Check: report the path, readiness, the dimension table, the tallies, the surface coverage with the mechanism share
(reported, not gated) and the self-review. Next: fix
and re-run check; then `/rubric` with the criteria JSON, the exact prompt,
assignment + persona, the SQL or "no injection", and reference files (the OEs may be
supplied as a comparison reference). PASS or a scored NON-FAIL proceeds only when
`stage_gate.py rubric-check` passed (no validity defect); NON-FAIL with PARTIAL/BLOCKED does
not clear the gate. After the verifier runs: `/create-allfail`. Before submit,
`stage_gate.py release` must pass: no PROVISIONAL plan, no UNRESOLVED or UNVERIFIED item, and
every certificate bound to one bundle digest (GEN_EXECUTION §6b).
