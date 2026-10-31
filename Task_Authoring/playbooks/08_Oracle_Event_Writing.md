# 08 — Oracle Event Writing: fact ledger (prep) + OE check (Playbook) — HarmonyGames · Spec V2

> Command: `/create-oe-writing` (prep) · `/create-oe-writing draft` (draft) · `/create-oe-writing check` (check) · Writes: `task_inputs/Working_Files/08_OE_Writing_Ledger.md` / `task_inputs/Working_Files/08_OE_Check.md` · Paired eval: `/oe` · Gates: **`tools/stage_gate.py oe-writing` / `oe-check` (blocking)** · Read first: `setup/GEN_EXECUTION.md`

> **Claude, Codex or the human writes the Oracle Events.** This stage prepares the facts, drafts the events on request, and checks whatever was written — GEN_EXECUTION §2.

## Purpose

Oracle Events (OEs) replaced the golden answer in Spec V2. They prove the task is
solvable (with hinting gone, nothing else does) and they drive the rubric. `/oe`
(`oracle-events-v2`) scores them: a missing or wrong step is FAIL 2; minor, non-action
and final-response defects are NON-FAIL 3; a clean set is PASS 5; the result is the
minimum of completeness and accuracy (`Evals/README.md`; `7_Oracle Events V2.md` §9).
The taxonomy (Oct 3) has them written **while the baseline runs**.

Prep mode queries the universe and records every verified fact the critical path
touches — where it lives, which tool reaches it, what it returns, whether the persona can
see it, what must be known first. Draft mode (on request) writes `08_Oracle_Events.md`
from the ledger. `check` mode compares the events, whoever wrote them, with the ledger
and the universe and reports defects.

OEs do not set the tool-call minimum. That is measured on the golden run (a baseline
rollout scoring 100% on the rubric) or, if none exists, the 6-rollout average
(GEN_EXECUTION §3). Never compare an OE count with the tier.

## Writing the events

- Claude or Codex may draft, complete, rewrite or polish the OEs (GEN_EXECUTION §2). The platform's Oracle Events field blocks pasting, so a drafted set is typed into it and kept identical in `task_inputs/08_Oracle_Events.md`.
- The ledger is a fact sheet: facts as noun phrases with values, order as dependency edges between fact IDs (F7 needs F3). Draft mode turns it into events.
- Event format (taxonomy screen 44, Oct 3): a heading line `OE <n>` + what the step is for and where to look + its parameters, then an `Expected:` line with the actual values it returns or produces (and any trap). Each event covers Action, Information, Tool/Service, Parameters and Expected Data; plain sentences, no function names or raw IDs needed. Rules on that screen: cover the full path including every write; nothing about what the final response says; no non-actions; no redundant events; every Expected line matches the universe exactly.
- Every `Expected:` line is a value ledger (Eval 2 §2.4, A-23/B-17/C-18). Each ID, event name, field value, channel, SHA, version, number, count and date on it must be quotable character-for-character from the cited record — quote the call site or live record, never a declaration, config or policy document (#7: `quest_completed`, not `quest_completion`). Figures match after dropping thousands separators or with a recorded calculation; narrative values are marked `not_a_claim`; absence wording (none / never / nothing / no later commit) needs a scope-bound ABSENCE evidence check over the whole population, or repeats a record's own 3+ words (#47: 24 of 99 Critical comments end "✅ Addressed in commit X").
- `check` quotes the span, names the rule, states the defect and cites the ledger fact, and may propose corrected event text.

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

Prep inputs (`task_inputs/` = `Task_Authoring/task_inputs/`):
- `00_Assigments.md` — persona, competency, tier.
- `04_Prompt.txt` — **required, stop if missing**. Every requirement is quoted from it.
- `01_Grounding_Dossier.md` + `01_Universe_Inject.sql` — the seeded chain (SQL is read as an overlay, never executed).
- `01_Scenario_Design.md` + `01_Hardness_Manifest.json` if present — anchors, delegation lattice, hidden authorities, chains and traps (leads for where facts live and which lookalikes compete; never a source of values).
- `03_Error_Async_Config.txt` — killed/async functions and its "Facts for the human" list.
- `02_Reference_Files_Manifest.md` + `02_Reference_Files/` — attachments the agent reads.
- `04_Prompt_Writing_Brief.md` if present — intended chain and designed traps.
- Universe: only the selected universe, through `Task_Authoring/tools/hg.py search` (`search`, `search-many`, `lookup`; `get` takes a service-relative `--file`, e.g. `--file contacts.json`). Snowflake columns: `Evals/references/schema/snowflake.json`.
- Tools: `Evals/references/tools/catalog.json` (298 tools; names and parameters only).
- Persona/ACL: `Evals/references/persona/roster.json` (17 usable), `Task_Authoring/references/Docs/4_Persona ACL Policy - V2.md`, `Evals/references/persona/acl.md`.
- Rules: `7_Oracle Events V2.md`, `9_Common Errors & Pre-QC - V2.md` §7, `Evals/Docs/Original_Conference_Guidelines_Example_Task.pdf` (the ML-selected example task), QC Spec `Task_Authoring/references/Docs/QC_Spec_Doc_Latest.csv` (Oracle Events — Completeness, Accuracy). Where `references/Docs/` still holds the Sep 26 export names, these are `7_Oracle Events V2.md`, `9_Common Errors & Pre-QC - V2.md` and `QC_Spec_Doc_Latest.csv`; screen 44 is `Taxonomy.json` `turn[44]`.
- The gate: `Evals/2_Oracle_Events_Eval.md` (all phases), `Evals/references/rules/oracle_events.md`, `oracle_events_qc_examples.md` + `oracle_events_qc_cases.json` (historical labels, V12 era: every flag scored Non-Fail 3).

Check inputs: the above, plus `08_OE_Writing_Ledger.md` (required — run prep first) and
`08_Oracle_Events.md` (Claude, Codex or human; required — stop if missing).

Output: `task_inputs/Working_Files/08_OE_Writing_Ledger.md` (prep) or `task_inputs/Working_Files/08_OE_Check.md`
(check). Nothing else is written; `08_Oracle_Events.md` is never touched.

## Hard gates

1. **Prompt first.** No `04_Prompt.txt`, no ledger. Requirements come from the prompt, not the brief or dossier; a seeded fact the prompt never asks about is context, not a requirement.
2. **Ledger = facts.** The ledger holds facts and dependency edges; event text goes in `08_Oracle_Events.md` (draft mode).
3. **Verified values only.** Each value is read from the record and carries a source pointer (service + file + JSON pointer or record ID; for injected rows, the SQL statement). Dossier, brief and memory are leads, not sources. Numeric and date facts get two checks: the raw value, and a catalog tool that reaches it at that precision. Every value on a future `Expected:` line gets one ledger row in `08_OE_Writing_Ledger.md` §B with its verbatim quote and result (`VERIFIED`, `MINOR`/`INACCURATE`, `UNRESOLVED` or `not_a_claim`); a declaration, config or policy document does not source a call-site value (B-17/B-18). Never cite the placeholder `threads/00000000.json` — it is the `source_layout.json` sample hint, not a record (B-03).
4. **Assigned clock.** Recompute every relative date against the shared context's freeze. Retain raw UTC for source checks; human-facing dates use Pacific with UTC alongside when calendar days differ. Type each date by meaning before applying the clock:
   - *Record time* — creation, modification, sending, version/edit or completion. After the assigned freeze it is a universe defect: report it instead of treating it as historical evidence.
   - *Semantic future date* — a meeting start, a deadline, a scheduled send, an effective date, a due date stored in a record created before the clock. It may fall after the clock when it describes an event that has not happened yet. It is never expected as done (Accuracy below), and a record whose own record time is after the clock is still a defect.

   Write the type beside every date in Expected data ("created …", "starts …", "due …") so the check can apply the right rule. The seed bound is `freeze_utc` (nothing after it is completed; the eval clock `universe.clock_utc` supplies the `Clock:` line). No step expects a record after the seed bound as completed, and on Oct 1 no step uses a post-cut storyline record — Combo Fighter, Zombie Match Lite, the Telegram Domino Delights port, the UI sprite optimization sprint, the Mattel Barbie idle life sim pitch or the web distribution partnership (A-03/B-16).
5. **Persona reachability, proven per fact.** Gmail: persona sent, received or was copied. Slack: channel member or DM party. Calendar: own calendar or invited. Drive/Docs/Sheets/Slides: file shared with the persona. GitHub, Linear, Trello, Contacts, Confluence and Snowflake: unscoped (Confluence and Snowflake confirmed live, `Evals/ENVIRONMENT.md` `service-availability-v1`); record the natural pointer that leads the agent there, since its system prompt does not advertise them. Explorer and `hg_search` are god-mode and never prove visibility. An unreachable critical-path fact makes the task infeasible: mark the ledger BLOCKED and route it to the prompt or injection — no OE can fix it. **Proof is mechanical:** for every scoped §B row run `python3 Task_Authoring/tools/persona_view.py can-see <persona> <service> <id>` (base records) or `persona_view.py check-sql <persona> Task_Authoring/task_inputs/01_Universe_Inject.sql --load-bearing <ids>` (seeded records) and paste the YES lines verbatim under §B ("Visibility proof"). The gate re-runs every pasted line, blocks a line that differs from the re-run, and blocks a scoped §B id with no pasted YES line. It does not trust the paste for coverage: it extracts every scoped id or pointer from every §B row itself and runs `can-see` / `check-sql` on all of them (`reach.ledger_B`), and it blocks a §B fact on a scoped service that carries no record id at all (`reach.ledger_B_ids`), since such a fact could never be checked. Content is readable per type (B-19): no step may read a Gmail or Slack attachment's content (no bytes are returned, though names and metadata are), Drive and Linear attachments carry content, and Trello attachment reads are unreliable (42 of 106). Evidence that exists only inside a Gmail or Slack attachment is not agent-readable, so an OE step that reads it is infeasible.
6. **Service = where the data lives.** A figure held in more than one place gets one row per location, with the authoritative one stated; single-source figures are labelled (e.g. "Snowflake-only").
7. **Every required write is feasible.** Each maps to a catalog tool that exists, with its required parameters. **Catalog only**: run-log evidence that an uncataloged tool works (e.g. `github_request_reviewers` in v1 runs) does not count — platform `/prompt` fails the ask (task-1, 2026-10-05); reword the incorporated line to a cataloged write instead. A write the catalog cannot perform makes the task infeasible — BLOCKED. Writes are governed by the catalog, not the ACL (`4_Persona ACL Policy - V2.md` §5). A create-issue step must be satisfiable with `state_history_json` (`'[]'` for a new issue) or the load fails on NOT NULL (B-04); an expected Linear date matches the stored text exactly, `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DD`, including the `Z` (B-05).
8. **Friction has a reachable alternative.** Every `01_` function on the path has alternative-path facts in the ledger. At rate 1.0 a retry never succeeds — record no retry fact. A forced error on a scoped tool whose denial the task wants reasoned about is flagged (`4_Persona ACL Policy - V2.md` §8).
9. **Coverage.** Every requirement has ≥ 1 fact; every fact the user asked to be told has a row with its exact value; every input a derived fact uses has its own row. Coverage is also two-way with the rubric (A-19, C-13/B-12): every record a rubric row will grade has an OE step, the step label appears verbatim (the rubric review cites it and `hg_review_score` binds it to the saved OE bytes), and editing `08_Oracle_Events.md` after the rubric review makes that review stale.
10. **Stage gate.** `tools/stage_gate.py oe-writing` (prep) and `tools/stage_gate.py oe-check` (check) PASS; handoff is blocked until they pass.
11. **Multi-version facts.** Where the design has supersessions (`01_Hardness_Manifest.json` traps with `versions`), every version gets its own row with timestamp and author, and the governing one is marked with its resolver.
12. **Locator provenance** (red team B, R1 #8). Visibility is not discoverability. Every opaque id or high-information exact locator in a §B Locator cell must be obtainable by the agent, not only by the author who already knows the answer. Opaque means a Slack channel / DM id or ts, a Drive `f_`/`d_` id, `evt_`, a ticket id (`ENG-n` …), `usr_`, `repo#n`, a Gmail `mailbox/id`, a 24/32-hex id, `page_`, `cmt_`. The **Locator origin** column records where it comes from:
    - `prompt` — the id appears in `04_Prompt.txt`;
    - `F-n` — the id appears in the Expected data (or value) of an **earlier** §B fact that this fact depends on (dependencies are topological: only rows above, no cycles);
    - `search "<query>"` — a natural search a person would type, with no opaque id in the query; the gate re-runs it as the persona (`persona_view search`, or the seeded SQL row's text) and requires it to reach the record.

    An opaque id that traces to none of these blocks handoff (`provenance.locators`, `provenance.search` in `stage_gate.py oe-writing`). Natural-language locators (a channel name, a document title the persona would know) need no origin.
13. **Accepted outcomes.** OEs describe a complete valid route to a result accepted by brief §4b. They do not eliminate other fair routes or outcomes. A write's Expected line states its actual fields; representational differences or accepted material variants are not accuracy defects. Where the prompt report records `BOTH_FAIR_FIGURE`, the OE states both values and the record behind each, so a rubric row can accept either (B-15/A-24).
14. **Status facts get their own discovery step; one write per event** (task-1 blind audit, 2026-10-05). Every person-status fact a rule depends on ("still here", left, on leave) needs its own §B row and its own retrieving event — the status of a people who *qualify* as much as of those who don't. A write event performs exactly one write on one record (8 status changes = 8 events); reads over a population may stay one event. No event states what the agent refrains from doing; an exclusion is graded as an exact count or scope on a required write, or as a requirement inside a required artifact — a preserved-state row ("leaves X open") is not a valid rubric row either (B-11).

## Procedure — prep mode (checklist)

- [ ] Read GEN_EXECUTION, this playbook and `7_Oracle Events V2.md` in full. Load the inputs; stop on a missing `04_Prompt.txt`.
- [ ] Bind the persona to its exact roster entry (name, email, role) and list its scoped services.
- [ ] Split the prompt into requirements R1…Rn, each with its quoted span, typed Discovery (must be found), Write (must change state), Tell (the user asked to be told it) or Constraint (recipient, deadline, location, prohibition). Mark implicit rows and quote the span that entails them.
- [ ] For each requirement find the evidence: dossier and SQL for seeded records, then the base universe via `tools/hg.py search`, then reference files. One F-row per fact, exact value.
- [ ] Per fact: service; tool family (catalog names that list/search/get it); locator (channel ID + thread ts, message ID, issue identifier, file ID + tab/range, table + filter, date range) with any default that changes the result (mailbox folder, default date window, page size/pagination, server-side vs local filter) and IDs in the namespace of that service; locator origin (gate 12: `prompt`, the earlier `F-n` whose Expected data holds the id, or the natural `search "<query>"` that reaches it); expected data (exact values, counts, timestamps with zone, row counts, the precision the tool path shows); visibility proof; depends-on (F-IDs whose values form this locator); source pointer.
- [ ] Expected-value ledger (A-23/B-17): for every value a future `Expected:` line will state, record the verbatim quote from its record — the call site or live record, never a declaration, config or policy document — or `not_a_claim`. Counts get their population; an absence gets a scope-bound ABSENCE check (service, query, surfaces, positive control) or the record's own wording. A value that cannot be quoted becomes an open risk (§F).
- [ ] Aggregates: derive the full requested population first (the prompt's "every"/"all" set), then the filter, join keys, deduplication, row count, aggregate and computation; recompute once from scratch.
- [ ] Writes: per Write requirement, the prompt span that assigns it to the agent (not a user-reserved "I'll…"), the catalog tool, its required parameters, the target and its F-ID (recipient email from Contacts, channel ID, team/project ID, folder ID), the end state that completes it (sent, not drafted; state changed, not only commented), only the content the prompt requires, and an **authority-aware defer search** (Eval 2.6; red team B, R1 #11). Search every service that governs the affected entity, not only Slack and mail: its Linear issue and comments, Confluence pages, Docs and Sheets that own it, GitHub issues/PRs, calendar holds, and every thread that mentions it (the target's identifier + "defer", "hold off", "not yet", "wait", "as-is", "accept", "freeze", creation → clock). Record: the services searched, the candidate population (how many records matched), that pagination completed (no search hit its limit), the version resolution (which version of each candidate governs at the clock) and the result. A negative result counts only over a complete population. If any of these is missing, the decision is **UNRESOLVED** and stays on the ledger (§F) — never "no defer found". The gate requires each §C defer cell to name ≥ 2 services, a record pointer, "complete" and the governing version, or to say UNRESOLVED (`evidence.defer_search`).
- [ ] Friction: per `01_` function — mode/rate/wait, facts it blocks, the alternative locator and facts, their visibility. Async: the `*_submit_*` → status → result family and the facts behind the slow path.
- [ ] Traps: stale vs superseding records (timestamps), conclusion-sounding messages (where the thread really ends), lookalikes (shared first names, ENG-#### vs ZOM-###, another title's documents). For each: which fact it competes with, and the discriminator.
- [ ] Open risks: competing readings not yet captured in acceptance; unverified visibility; records near/after the assigned freeze; facts supported only by injection SQL; and status/activity disagreements. Include all fair outcomes; report actual inaccessible evidence or contradictions separately.
- [ ] Visibility proof: paste the `persona_view` YES line for every scoped §B id (gate 5); re-read every §B expected value through `tools/hg.py` (or the SQL statement for seeded rows) and keep its pointer in the Source pointer column.
- [ ] Self-scan for event text (gate 2), write the ledger, then run the Self-review (prep). Status is BLOCKED if any gate 4, 5, 7 or 8 item fails.
- [ ] `python3 Task_Authoring/tools/stage_gate.py oe-writing Task_Authoring/task_inputs --paste` → PASS (quoted §A spans are exact substrings of `04_Prompt.txt`; every §B row sourced; visibility re-proved on every scoped §B id, pasted or not; every scoped fact carries an id; every opaque locator has a provenance (gate 12) and its search origins reach the record; every §C defer search is complete or UNRESOLVED; tally matches the tables; no event text, agent voice or "should").

## Ledger template

Write exactly these headings and columns.

```text
# 08 OE Writing Ledger — <task id>
Generated <date> · Clock <universe.clock_line> · seed bound <freeze_utc> · Persona <name> <email> (<assigned role>) · Tier <Normal | Long-Horizon> · Mode <Easy | Medium | Hard>
Status: READY | BLOCKED — <blocking items>
Inputs read: <slot — present / absent>

## A · Requirements (traced to the prompt)
| R | Prompt span (quoted) | Type (Discovery / Write / Tell / Constraint) | Explicit / implicit | Fact IDs |

## B · Facts
| F | Fact / value | Service | Tool family (catalog) | Locator | Locator origin (prompt · F-n · search "<query>") | Expected data (dates typed: created / starts / due) | Ledger result for the Expected line (VERIFIED quote · not_a_claim · ABSENCE evidence_check · UNRESOLVED) | Persona-visible? (proof) | Depends on | Source pointer |

Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)

## C · Write capability
| R | Required write | Prompt authority (quoted; agent, not user-reserved) | Catalog tool (exists?) | Required parameters | Target (fact ID) | Completing end state | Content the prompt requires | Defer search (services · population · pagination complete · governing version · result, or UNRESOLVED) | Feasible? |

## D · Friction facts
| Function (01_) | Mode / rate / wait | Facts blocked | Alternative path (service, locator) | Alternative facts | Visible? |

## E · Traps and distractors
| T | What the agent meets (pointer) | Competes with (fact ID) | Discriminator (timestamp / author / ID) |

## F · Open risks
| # | Risk | Facts affected | Consequence (OE accuracy / rubric / UGT / feasibility) | Check needed |

## G · Tally
Requirements N · facts N · writes N (feasible N) · friction items N · expected values N (quoted N · not_a_claim N · ABSENCE-checked N) · unverified visibility N · blocking N
```

Illustrative B row, from the guideline's example task (shape only — not this task):
`| F4 | Paid spend, combo_fighter | Snowflake (only) | snowflake_execute_query | AD_SPEND_DAILY, game_id = combo_fighter, 2025-12-26..2026-02-08 | search "combo_fighter" | 152 rows; channel = meta on all; 4510.33 USD; 615 paid installs | VERIFIED: quote "4510.33"; 615 installs by recorded calculation; 152 rows from the table | unverified → risk 2 | — | snowflake.json, AD_SPEND_DAILY |`

## Procedure — check mode (checklist)

Mirrors `/oe` phase by phase (Eval § in brackets). Judge content, not style: plain sentences, no function names and no raw IDs are all valid (Eval "Judge content, not writing style"; screen 44).

- [ ] **Intake.** Load `08_Oracle_Events.md` and `08_OE_Writing_Ledger.md`; stop if either is missing or empty. Edit neither. Count the characters of the whole OE text: outside 300–50,000 the platform field rejects it.
- [ ] **Inventory [1.2].** Partition the whole text — numbered events, headers, notes — into STEP / CONTEXT / RESPONSE_DESCRIPTION / NON_ACTION. Quote spans verbatim, typos included. A CONTEXT note never waives an instruction it asserts.
- [ ] **Five fields per STEP [1.3]** — action, information, tool/service, parameters, expected data, plus dependencies. A field is MISSING only when the event does not say it and a reader cannot work it out from it and the events before it — never because it is unlabelled, mid-sentence or named in words. Tool/service, parameters and dependencies may be not applicable (first discovery, pure calculation).
- [ ] **Completeness [3.1–3.5] → INCOMPLETE.** Walk ledger §A route-independently: a requirement is covered by any accurate, persona-reachable event that satisfies it, by whatever tool or service; a different valid route is checked under Accuracy, never reported missing. Report: a requirement no event covers; a requested population narrowed before it is derived ("every active loan" → only the flagged ones) or a join, mapping, dedup or aggregate method the result needs left out; a required write with no executing event (retrieving or mentioning its subject is not performing it); a fact in an Expected line that no event retrieves; a rubric row whose graded record has no step (an OE gap, not a rubric pass — A-19/C-13); a value (ID, recipient, channel, date) used before the prompt or an earlier event produced it — unless the event's own pointer finds it uniquely through a natural search that carries no opaque id the prompt or an earlier event did not supply (ledger gate 12); a jump from discovery to write with the analysis missing; expected data absent or only a verb ("cross-reference the amounts", "Expected: the amounts") with no finding; a `01_` friction item with no explicit recovery or wait event.
- [ ] **Accuracy [2.1–2.6, 3.2–3.4] → INACCURATE unless it passes the Minor test.** Per STEP:
  - *Service* — the data lives there (Sheets named for a Snowflake-only figure fails even if the figure is right).
  - *Tool* — a cataloged tool performs the operation. A named tool or branch that cannot complete the step (a draft offered as a send; a filter it lacks where no local filtering recovers the records) fails; an unambiguous name slip for an existing tool is MINOR; a name that maps to no tool or capability is UNRESOLVED until the catalog or schema settles it.
  - *Parameters and identifiers* — entity, ID (in the named service's namespace: Contacts IDs are not CRM IDs), recipient, filter, window and value match the records and the tool contract; the argument carries the right kind of input (a message ID passed as a search query fails); a default that changes the result (mailbox folder, date window, pagination, server-side vs local filter) is handled; a literal call missing a required argument fails. A record named in words is as good as its ID when it resolves to exactly one record the persona can read.
  - *Expected data* — every value equals the universe, re-read through `tools/hg.py` (the ledger is a lead); counts and totals recomputed; author, date, state and lifecycle right (current vs historical, proposed vs done, a new record's state vs an existing settled one); the precision is observable on the tool path and any calculation is stated [2.3A]; nothing on or after the clock expected as done [2.5] — a record time on or after the clock is a defect, a semantic future date (meeting start, deadline, scheduled send) is valid when it describes an event that has not happened (gate 4). The Expected line's value ledger [2.4] must quote each ID, event/field name, channel, SHA, version, number, count and date character-for-character from the cited record, or mark it `not_a_claim`; an absence word needs the scope-bound evidence check. An unledgered value is UNRESOLVED, and a wrong event name, field value or ID is INACCURATE (B-17/B-18).
  - *Visibility* — every scoped read reachable by the persona; an intended denial is valid only when the next event reports, escalates or reads an authorised alternative [2.2]. A rate-1.0 tool is never shown succeeding.
  - *Authority* [3.3–3.4, `prompt-incorporation-v1`] — every write traces to a prompt span. A write the prompt forbids, one the user reserved ("I'll post…"), or one it does not authorise (including "repairing" a designed absence) fails. Every branch an event offers as sufficient ("update the status or add a note") must complete the requirement alone.
  - *Act-vs-defer* [2.6] — a write on a proposal where ledger §C records a defer/hold/accept-timing decision fails. Where §C marks the defer search UNRESOLVED (a governing service unsearched, the population or pagination incomplete, the governing version unknown), the act-vs-defer judgement is UNRESOLVED, never "no defer".
  - *Final state* — judged against the canonical outcome (brief §4b, gate 13): a material field that differs is INACCURATE; a representational difference inside the allowed equivalence class is not a defect.
  - *Consistency* [3.2] — the same record and value treated the same way in every event; no cycles. Read the set straight through as the agent: each event executable from what earlier events produced.
- [ ] **Minor test** [2.3; QC examples "Consequence and severity"]. MINOR only if following the event literally still reaches the same records, values and end state: an unambiguous tool or parameter name slip in prose; a rounded figure or loose window that returns the same rows; an off-by-one date or partial title that still identifies one record; a side explanation outside the expected result (the size of a trap, the purpose of a lookup, a false "only in X" while the named route works) that changes no step, parameter, write or answer; an offered alternative branch that still reaches the same result with local filtering. Any value, count, state or record content stated as the step's expected data that the universe contradicts is INACCURATE even when the path survives (Eval Quick Reference: "Expected data does not match the source"; screen 44: every Expected line matches exactly).
- [ ] **Non-action / final-response** [HARD GATE; Completeness 3] — "does not give up", "does not stall", "does not stop at the first explanation"; "the response explains…". A tool-observed negative finding ("search the repository and confirm no implementation evidence is found") is a valid step. A required write's Expected line may state the content the prompt requires.
- [ ] **Format** [2.7; Accuracy 3, never FAIL] — NO_DETAILS_OR_EXPECTED, ARROW_CHAIN, MULTIPLE_ACTIONS (a lookup and a write, or two writes, in one event), JSON, NO_NUMBER_OR_SERVICE. Tool names, IDs and query style are not defects.
- [ ] **Unresolved** [4.1] — a check evidence cannot settle (unknown tool name, unprovable visibility, a record a bounded search did not find) is UNRESOLVED, not INACCURATE; record the search scope.
- [ ] **Advisory, no `/oe` effect** — redundant or unnecessary events (screen 44 asks for none; `/oe` does not score them); `set_acting_user` as a step; readability (goal first, values written out, traps named) — an observation, never wording.
- [ ] **Pre-verdict sweep** [4.0] — one wrong count/ID/channel/tool; one missing write; one Expected fact with no retrieving event; one unledgered Expected value or unbacked absence word; one act-vs-defer conflict; one non-action or final-response event; one prompt-forbidden write; one missing recovery/wait event.
- [ ] **Predict and report.** Completeness = 2 if any INCOMPLETE, else 3 if any non-action/final-response, else 5. Accuracy = 2 if any INACCURATE, else 3 if any MINOR or format, else 5. `/oe` = the minimum; FAIL whenever either is 2 (a proven failure stays FAIL with checks unresolved); with no failure, any UNRESOLVED gives NON-FAIL / PARTIAL and no score. Path feasibility: BROKEN (any inaccurate) · UNRESOLVED · INCOMPLETE (any missing) · SUPPORTED. Task solvability: SUPPORTED_BY_OE only when SUPPORTED; UPSTREAM_BLOCKER only when the ledger is BLOCKED on a prompt-authorised requirement with every authorised route ruled out (route to prompt/injection — no OE edit fixes it); else NOT_ESTABLISHED. A defect cell cites the ledger value a span contradicts and may give the corrected span; a "Recommended Fixes" section is optional.

| Finding | `/oe` (governs — GEN_EXECUTION §3) | QC Spec V2 label (all score 3) | Report severity |
|---|---|---|---|
| Incomplete — requirement, population/method, write, retrieving event, dependency, analysis, expected finding, friction path | Completeness FAIL 2 | Non-Fail — Incomplete Oracle Events | BLOCKING |
| Inaccurate — service, missing tool/capability, ID/namespace/argument/default, value/state/date, precision, visibility, unauthorised or reserved write, insufficient branch, act-vs-defer, inconsistency | Accuracy FAIL 2 | Non-Fail — Inaccurate Oracle Event | BLOCKING |
| Minor — passes the Minor test | Accuracy NON-FAIL 3 | Non-Fail — Minor Oracle Event Inaccuracies | MINOR |
| Non-action / final-response event | Completeness NON-FAIL 3 | Non-Fail — Incomplete Oracle Events (closest) | MODERATE |
| Format defect (five codes) | Accuracy NON-FAIL 3 | Non-Fail — Minor Oracle Event Inaccuracies (closest) | MODERATE |
| Unresolved check | no score while nothing fails (NON-FAIL / PARTIAL) | — | OPEN |
| Redundant event, `set_acting_user`, readability | none | — | ADVISORY |
| Field length outside 300–50,000 | platform rejects the field | — | BLOCKING |

## Check report template

```text
# 08 OE Check — <task id>
Checked <date> · Clock: <universe.clock_line> · Events N · Characters N (300–50,000: ok / out) · Ledger <date> · release task-quality-v1
/oe prediction (a prediction only; /oe gives the verdict): FAIL 2 | NON-FAIL 3 | PASS 5 | NON-FAIL / PARTIAL
Completeness N · Accuracy N · Path feasibility <…> · Task solvability <…>

## Inventory
| Segment (quoted start) | Role | Event |

## Coverage
| R / F | Event(s) | Covered / missing / partial | Route (ledger / other valid) |

## Expected-data sign-off
| Event | Claim (quoted) | Source re-read (hg.py pointer) | Value found | Ledger entry (result · quote · evidence_check / not_a_claim) | Match / minor / wrong / unresolved |

## Findings
| # | Severity | Component | Event | Quoted span | Rule (Eval § / source) | What is wrong | Evidence (ledger fact + source pointer) |

## Pre-verdict sweep
| Eval 4.0 check (7) | Result |

## Advisory (no effect on the prediction)
| Event | Note |

## Tally
Blocking N (incomplete N · inaccurate N · length N) · moderate N (non-action N · final-response N · format N) · minor N · unresolved N · advisory N

## Self-review
<per the Self-review section>

## Reminders
- The tool-call minimum is measured on the golden run or the 6-rollout average, never on the OE count.
- Fix the events (Claude, Codex or the human), re-run check, then run /oe.
```

## Self-review (GEN_EXECUTION §6a — both modes, recorded under **Self-review**)

Prep (ledger):
1. *Re-read as the eval.* Walk Eval 1.1, 2.1–2.6 and 3.1–3.5 against the ledger, in order: every requirement has facts; every write has authority, tool, required parameters, completing end state and a defer search; every friction item has alternative facts; every scoped fact has visibility proof.
2. *Counter-readings.* For each requirement row (type, explicit/implicit, population): the strongest other reading of its prompt span and whether it adds or removes facts. For each authoritative location: the competing one (superseded version, lookalike, other service) and its discriminator. For each absence fact: the bounded search behind it. Resolve each with a pointer or prompt span.
3. *Re-verify.* Re-read every §B value and §C target through `tools/hg.py` (fresh read, not the dossier, SQL comments or brief); recompute every aggregate from rows; re-confirm each Expected-line ledger row (verbatim quote from the record, or `not_a_claim`). Record the pointer; a value you cannot re-read becomes an open risk (§F).
4. *Counter-reading count.* At least one evidenced counter-reading per §A requirement row (the gate counts them).
5. *Draft grounding* (draft mode). Every Expected value in a drafted event is re-read from its source record in this run.

Check (report):
1. *Re-read as the eval.* Walk Eval 1.2, 1.3, the HARD GATE, 2.1–2.7, 3.1–3.6 and 4.0 in order against the report — not from memory.
2. *Counter-readings, one per judgement.* COVERED → the best case it is missing (mentions the subject but performs no write; part of the population; route unreachable for the persona). MISSING → the best case it is covered by another valid route [3.1] or not required (user-reserved, not in the prompt). VERIFIED value → the best case it is wrong (superseding version, lookalike, wrong namespace, a default that changes the result, post-clock date). INACCURATE → the best case it is MINOR (Minor test) or UNRESOLVED (thin evidence); MINOR → the best case it changes the result. Non-action/final-response flag → the best case it is a tool-observed negative finding or required-write content. Cite a similar `oracle_events_qc_cases.json` row where one exists — its label is V12-era (every flag Non-Fail 3) and never sets the current band.
3. *Re-verify.* Re-read every expected value the report relies on, verified or contradicted, through `tools/hg.py`; never from the ledger alone. A value you cannot re-read is UNRESOLVED.
4. *Fixes.* Any corrected event text the report proposes is grounded in a record re-read in this run.
5. *Stage gate:* `python3 Task_Authoring/tools/stage_gate.py oe-check Task_Authoring/task_inputs --paste` (recomputes the event and character counts of `08_Oracle_Events.md`, verifies every quoted span, every sign-off pointer, the 7-row sweep and the tally; needs one evidenced counter-reading per Coverage and Findings row).
6. *Record* the prediction per component with evidence, each counter-reading and its resolution, and every UNRESOLVED item. Never soften a finding to reach PASS; never invent one.

## Deliver

Both modes: handoff is blocked until `stage_gate.py oe-writing` / `oe-check` prints PASS; its output sits in the Self-review.

Prep: report the path, status (READY / BLOCKED) with each blocking item, and the tally.
Next: `/create-oe-writing draft` (or the human writes the OEs) — typed into the platform field (it blocks paste and
copy) and kept identical in `task_inputs/08_Oracle_Events.md` — then `/create-oe-writing check`.

Check: report the path, the `/oe` prediction (components, feasibility, solvability) and the tally. Release (`stage_gate.py release`, GEN_EXECUTION §6b) requires this report to say Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE · Blocking 0, with no UNRESOLVED item left. Next: fix the events and
re-run check; when clear, run `/oe` with the OEs, the exact prompt, assignment +
persona, the SQL or "no injection", and any referenced files (alongside `/rubric` if
criteria exist; Capture Files once). Then `/create-rubric-writing` — `/rubric` does not
require an `/oe` PASS, but the plan uses the OEs as the path reference.
