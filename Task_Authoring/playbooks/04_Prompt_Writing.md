# 04 — Prompt Writing: brief (prep) + prompt check (Playbook) — HarmonyGames · Spec V2

> Command: `/create-prompt-writing` (brief) · `/create-prompt-writing draft` (draft) · `/create-prompt-writing check` (check) · Writes: `task_inputs/Working_Files/04_Prompt_Writing_Brief.md` / `task_inputs/Working_Files/04_Prompt_Check.md` · Paired eval: `/prompt` (`Evals/1_Prompt_Eval.md`, release `task-quality-v1`) · Gates: **`tools/stage_gate.py prompt-writing` / `prompt-check` (blocking)** · Read first: `setup/GEN_EXECUTION.md`

> **Claude, Codex or the human writes the prompt.** This stage prepares the facts, drafts the prompt on request, and checks whatever was written — GEN_EXECUTION §2.

## Purpose

Claude or Codex may draft and revise the prompt (GEN_EXECUTION §2). This command works in three modes:

- **Brief mode** writes `04_Prompt_Writing_Brief.md`: the design facts to read before typing.
  It covers what the assignment demands, what the universe holds, the fair final outcomes
  the prompt must pin, what the agent must discover, and what must stay out of the prompt.
- **Draft mode** (on request) writes `04_Prompt.txt` from the brief: the persona's voice,
  one pinned final state, the symptom not the cause, and nothing from brief §9. Run check
  mode on the draft before `/prompt`.
- **Check mode** reads `04_Prompt.txt` (whoever wrote it) and writes `04_Prompt_Check.md`:
  findings against the brief, the universe and the `/prompt` dimensions, with suggested
  rewording where it helps. Fix the text (Claude, Codex or the human) before `/prompt`.

Both modes follow Rule zero (Prompt Writing §03): seed the context, don't type it in.
The universe carries the rules, the detail and the difficulty; the prompt is a short
trigger that names the problem, not the method. State the requested work and a destination the sender knows; accept every fair reading rather than adding answer-key clauses.
Leave the rules and evidence in the universe; record fair alternatives in acceptance.

Run order: after `/create-injection` (and `/create-error-async`, `/create-reference-files`
if used); before `/create-humantime` and the `/injection` + `/prompt` pair.

**Doc names.** Under `references/Docs/`: Prompt Writing = `6_Prompt Writing Guidelines - V2.md`;
Common Errors = `9_Common Errors & Pre-QC - V2.md`; Long Horizon = `10_Long Horizon Guidelines - V2.md`;
Persona ACL = `4_Persona ACL Policy - V2.md`; the QC Spec V2 rows = `QC_Spec_Doc_Latest.csv`
(GEN_EXECUTION calls it `QC_Spec_Doc_Latest.csv`). Taxonomy screens are cited by number from
`Taxonomy_V2_Step_Map.md`; if it is absent, generate it with `tools/build_taxonomy_map.py`.
V3 changed-topic rules govern over conflicting Docs/Evals; unchanged local checks remain (GEN_EXECUTION, authority).

## Writing the prompt

- The brief describes requirements as facts, noun phrases and record locators; it may also carry draft wording.
- A drafted prompt follows the assigned person's plausible role and register: ordinary colleague request, clean spelling, no spec-sheet layout, no trap hints, riddles or answer-key clauses. Name a destination the sender would know.
- Check mode may propose replacement wording under the preserved local authorship exception. Clean spelling, normal capitals and punctuation pass; planted mistakes, broken spacing and invented emoji codes fail (Eval 1 §1.2 AI-Text, §2.7).
- No line may point at the trap or hedge the prompt's own facts: a riddle or hint fails, naming the symptom is fine, and "if my date or channel is off, use the message that is actually there" is a hint and fails. Audit/compliance-form wording and long if / but-not / then-also chains fail on their own; a per-case rule belongs in a seeded record, not the prompt (Eval 1 §2.7, A-13/A-15/B-14).

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

Brief-mode inputs (stop and name any missing required slot)
- `task_inputs/00_Assigments.md` and `Working_Files/00_Task_Context.json` (required): all eight V3 assignment fields, supported source, assigned role, freeze and mode.
- `task_inputs/Working_Files/01_Grounding_Dossier.md` (including its "Facts for the human") + `01_Universe_Inject.sql`: required if anything was seeded. If nothing was seeded, say so and ground on the base universe.
- `task_inputs/03_Error_Async_Config.txt`, `02_Reference_Files_Manifest.md`, `01a_Hardening_Report.md` if present. Carry over every "must not appear in the prompt" constraint, every alternate-path fact and each file's "how the persona would refer to it" description.
- `Evals/references/persona/roster.json` (17 personas — the `/prompt` identity gate; `references/persona_roster_v2.json` adds the platform's `thomas`/`tim_steudler`, which fail that gate), Persona ACL, `Evals/references/persona/acl.md`.
- `01_Scenario_Design.md` (anchors, hidden authorities, delegation lattice, deliverables), `01_Hardness_Manifest.json` and the dossier's anchor-name table (§7 Constraints for the prompt brief).
- `Evals/references/tools/catalog.json` (298 tools): write capability and the forbidden-name list.
- Taxonomy screens 5–9 (competency pages), 10 (Task Skill), 12 (Task Complexity Dimensions), 23 (Sound Human) and 24 (Write the Prompt goal + writing guideline).
- Prompt Writing (all), Long Horizon §3, Common Errors §3–5 and §10, the Prompt rows of the QC Spec V2 CSV, `Evals/references/rules/task_categories.md`.
- The universe, only through `Task_Authoring/tools/hg.py search` (GEN_EXECUTION §4).

Check-mode inputs
- `task_inputs/04_Prompt.txt` (required), human-written and exactly as it will be submitted.
- `task_inputs/Working_Files/04_Prompt_Writing_Brief.md` (required).
- The brief-mode inputs, for verification; `Evals/1_Prompt_Eval.md`, `Evals/references/rules/scoring.json` (Prompt and Universe groups), `prompt_qc_examples.md`, `Evals/references/rules/prompt_qc_cases.json` (the 15 `calibration_cases`), `long_horizon.md`.

Output: brief mode writes only `04_Prompt_Writing_Brief.md`, draft mode writes `04_Prompt.txt`, and check mode writes only
`04_Prompt_Check.md`.

## Hard gates

1. **Draft from the brief.** A drafted prompt is grounded in the brief and the universe, never in memory; run check mode on it before `/prompt`.
2. **Grounded.** Look up every name, ID, figure, date and locator with `tools/hg.py search` during this run. Never use memory, notes or an earlier draft. Confluence and Snowflake are live and unscoped; verify their values like any other source.
3. **Persona view.** Confirm every fact the task depends on is readable by the assigned persona:
   - Gmail, Slack, Calendar and the Drive family are scoped to the persona (sender/recipient/cc; channel membership; owner/share).
   - GitHub, Linear, Trello, Contacts, Confluence and Snowflake are unscoped (`acl.md`, QC Spec V2 Feasibility row). Confirm the page/table exists and has a cataloged read; no run is needed to prove availability.

   Universe Explorer's god-mode view never counts. Check writes against the catalog, not the ACL.
   Prove it with `python3 Task_Authoring/tools/persona_view.py can-see <persona> <service> <id>` (base records) or
   `persona_view.py check-sql <persona> 01_Universe_Inject.sql --load-bearing <ids>` (seeded records); the gate re-runs
   it on every scoped id in §5 and §5a.
4. **Assigned clock.** Recompute relative dates against the shared context's `freeze_utc`, the seed bound: seeded record timestamps and completed events must not be after it, only plan fields (due date, scheduled start/end, deadline) may be later, and the eval clock `universe.clock_utc` is recorded beside it for each report's `Clock:` line. Human-facing dates use Pacific, with UTC beside them when calendar days differ; "today" and "yesterday" come from `universe.persona_today` (Sat Feb 14, 2026 / Wed Oct 1, 2025); do not prescribe an exact time for a date-only request. Ignore the QC form row 128 / spec Audit Workflow "today is February 28, 2026" — the task clock wins (A-30). **State premises** (Eval 1 §2.3, A-26/B-16): every actor is active at the clock and every object exists by then. On Feb 14, business as usual after the Feb 11, 2026 shutdown announcement is a false premise; on either date a departed person acting (Victor, gone since April 2025) is false; on Oct 1 anything first appearing after 2025-09-30 23:59:59 PT is false. A single loose factual slip is a Fail.
5. **Every fair outcome.** Brief §4b is the common acceptance table for 04, 08 and 09. List requested deliverables, destinations and recipients, fixed values or closed sets of accepted fair values, delegated choices (quote the span), allowed variants and material/representational fields. Multiple defensible outcomes are allowed when all pass the rubric. Never add answer-key clauses just to eliminate alternatives. The structure remains a canonical outcome table, but the old one-acceptance-class requirement is superseded. Supply `outcome_reviews` for prompt-writing and prompt-check in `Working_Files/00_V3_Authoring_Evidence.json` (Guide schema).
6. **Symptom, not cause.** The root cause appears only in the discovery map, flagged "never in the prompt". The situation section says what is visibly wrong, never why.
7. **Check findings.** Every finding gives a verbatim span of `04_Prompt.txt` (verified as an exact substring), the rule and its source, the severity and the defect, and may add suggested wording.
8. **Stage gate.** `tools/stage_gate.py prompt-writing` (brief) and `tools/stage_gate.py prompt-check` (check) PASS;
   handoff is blocked until they pass.
9. **Write boundary** (GEN_EXECUTION §1): write only under `Task_Authoring/task_inputs/`, execute no SQL, and write nothing under `Evals/`, `claude/` or `HarmonyGames_*`.

## Procedure — brief mode (checklist)

- [ ] Read GEN_EXECUTION, this playbook and Prompt Writing in full. Load the upstream slots.
- [ ] **Assignment.** Copy all eight fields from the shared normalized context and retain the raw paste.
  - Resolve the persona in the roster: exact name, email, role and department. Never infer an email.
  - Record the competency's focus and expected outputs (its taxonomy page) and the task skill's definition. Authoring needs an authored artifact; a chat message alone does not exercise it.
  - Map the business function to the nearest of the six in `task_categories.md` and record the mapping.
  - Record the tier: Normal 50–100 calls, Long-Horizon 100–500+, Super-Long-Horizon paused.
- [ ] **Remit.** Explain from cited records why this persona would plausibly be pulled into this competency's work: what they did, own or saw. The competency sets the kind of work, not the job title. If no defensible remit exists, stop and report it. Never switch personas.
- [ ] **Breadth for the tier.** List the services that carry real weight, with the measured volume behind each (messages in the window, rows, tickets). QC floor: 2 services, the second non-trivial (that is C12, the `/prompt` prediction). The tier's own target (GEN_EXECUTION §3a) is a **blocking harness check**, not advice: Long Horizon → `hardness_gate.py --profile extreme` (≥ 10 of 13 services and the rest of the extreme targets), Normal Horizon → `--profile normal` (≥ 7). `stage_gate.py prompt-check` blocks unless `01_Hardness_Manifest.json` exists and the dossier carries a current `HARDNESS GATE (<the tier's profile>): PASS` (`tier.hardness`; re-run under `--rerun all`). Length comes from evidence breadth and reasoning depth, not from the number of deliverables (Long Horizon §3). Do not estimate a call count.
- [ ] **Situation.** From the dossier, record the visible symptom, who sees it (the persona's vantage) and where it shows (a locator).
- [ ] **Phases.** Investigation: the questions to resolve, without their answers. Action: the writes those answers feed. Confirm each write genuinely depends on the investigation.
- [ ] **Final state.** For each deliverable, record its kind, its required contents (as requirements, not wording), its exact destination, its exact recipients (from Contacts or the roster) and the catalog write it needs. Keep only writes the scenario needs. Each write needs reads first. Independent writes added for volume are bolt-ons.
- [ ] **Decision-ambiguity scan.** For each deliverable, list what else a careful run could defend:
  - another destination, recipient or selection (which items or people qualify; ties);
  - act now vs defer, file vs chase, stage vs send, inform vs wait for approval;
  - the persona doing it vs delegating it ("I'll" vs "you").

  Record what settles each one, or add every fair alternative to §4b acceptance with its source/prompt basis. A second fair outcome alone is not a failure.
- [ ] **Anchor names (noun phrases only).** Carry the dossier's anchor-name table over unchanged into §6 as `Anchor · May be named`: each entry is a **noun phrase of at most 6 words** ("the known-defects list"), with no verb or imperative framing at the start, no second-person request ("you", "your", "please", "can you") and no sentence. Synonyms go in the same cell separated by `;`. The same rule binds the scenario's anchor-name table, the dossier's §7 table and the manifest's `anchors[].prompt_reference`; `stage_gate.py` scenario, injection and prompt-writing block any entry that breaks it (`boundary.anchor_naming`; red team A, R2 #3). How the human words the request around the anchor is the human's alone.
- [ ] **Discovery map.** Start from "Facts for the human". For each fact the agent must find, record its value, locator, persona readability, and which source the agent meets first and what overturns it.
  - Default: never name it in the prompt. Naming an artifact turns a fuzzy search into one exact fetch (Prompt Writing §06).
  - A human-readable item off the discovery path may be named, but only if the persona would know it.
- [ ] **Search as the persona (§5a).** For every §5 fact (UGT anchors and feasibility facts first), run the search
      a real person would type: `python3 Task_Authoring/tools/persona_view.py search <persona> <service> "<natural query>" --limit 10`
      (`--no-hidden` on Gmail keeps it fast). Record query · visible hits · hidden by ACL · first visible hit id ·
      found YES/NO, and paste at least the decisive outputs verbatim. A fact the persona cannot find with a natural
      search is NO: route it to `/create-injection` and say "routed" on the row (the gate blocks an unrouted NO and
      re-checks every hit id's visibility).
- [ ] **Search-behaviour risks**, per fact. These are design notes for this brief only, not prompt content:
  - Agents latch onto the first framing they meet.
  - They stop at a message that sounds like a conclusion, even when the thread continues.
  - They prefer secondhand chat over structured systems (GitHub, Linear, Snowflake).
  - They rarely search for a reply to a dispute or a question.
  - They never see results past the search limit.

  If a load-bearing fact cannot be found by a search the agent would plausibly run, route it to `/create-injection`. If it lives only in Confluence or Snowflake, note that the agent's system prompt advertises neither service.
- [ ] **Triggers and incorporation.** For every seeded requirement the rubric will grade, record what kind of trigger the prompt must carry (a deliverable, scope, constraint or recipient) and, when the requirement lives in a record, the incorporating source: its locator, that the persona can read it, that one search leads to it alone, and that it states instructions rather than the answer (`prompt-incorporation-v1`). Never write the trigger as a clause. Separate requirements a competent assistant would obviously infer (checking data before filing, telling the requester) from gotchas nobody could infer. A gotcha gets a trigger or is dropped, otherwise its criterion is unauthorized (Prompt Writing §4.3).
- [ ] **Dates and constraints**, each with its absolute date and source.
- [ ] **Levers.** Fill the template §8 table for all six characteristics. At least one of Ambiguity, Dynamic Change, Multi-Source must be load-bearing (`/prompt` §1.5 hard gate).
- [ ] **Must-not-appear list.** Build it from these sources:
  - catalog tool names and parameters for every service in play;
  - MCP server names;
  - internal and opaque IDs from the dossier, and opaque filenames;
  - the root cause and every finding the agent must make (culprit records, people, counts);
  - each injected failure or wait, and each async-target artifact (from `01`);
  - reference-file paths and `/app/artifact` (from `02`);
  - markdown, numbered steps, and per-deliverable content lists or format rules (they belong in records).
- [ ] **Entity traps.** `python3 Task_Authoring/tools/entity.py collisions`, then `entity.py resolve <name>` for every person, handle or alias the prompt could plausibly use; paste the output in §10. Add lookalike channels, ticket series (`references/universe_kb/trap_catalog.json` N01–N03) and similar documents (D01–D08). Known traps (Common Errors §4, screen 24): three Marcuses plus Oscar Bennett; ENG-#### vs ZOM-###. Pin the correct entity's exact identity (email or id).
- [ ] **Name-swap test.** Swap every name in the situation for a different one. If the scenario still works, it rests on no real records; route it to `/create-injection`.
- [ ] Write the brief from the template below, then run the Self-review.

## Brief template

The section headings of `04_Prompt_Writing_Brief.md`, in order. Every cell holds a fact,
a locator or a requirement.

```
# Prompt Brief — <task slug> · prep
> Built <date> from <slots read> · Persona view verified: <all | list of exceptions>
> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human.
```

- `## 1 · Assignment fit`. Table with columns Axis · Assigned value · What it requires here (cited).
  - Business function (and its `task_categories.md` mapping).
  - Persona: name, email, role; voice and remit in one line; read scope (scoped services and key channels it is in).
  - Competency: focus, expected outputs, remit argument.
  - Task skill: the assigned skill, any stacked skills, and the deliverable or discovery that exercises each.
  - Task type: the tier, the services that carry weight and the measured volumes.
- `## 2 · Situation`. Symptom · Seen by · Where it shows (locator) · Relevant records the persona cannot see. Third person; no cause.
- `## 3 · Investigation → action`. The questions to resolve (no answers), then the writes they feed.
- `## 4 · Pinned final state (UGT anchor)` (legacy heading). Table: Deliverable · Required contents · Destination · Recipients · Catalog write · Fed by. Below it record alternatives a careful run could defend. Then `### 4b · Canonical outcome (all fair outcomes)`: Deliverable · Field · Fixed value (or closed accepted set, with sources) · Delegated by (quoted span, or —) · Allowed equivalence class · Material / representational. Keep every fair reading, including precise/rounded values and source redaction tokens, in acceptance; 08 and 09 reuse this table.
- `## 5 · Discovery map`. Table: Fact · Value · Locator · Persona-readable · Met first / overturned by · Search risk · Name in prompt? (No by default, or Yes with the reason).
- `## 5a · Search-as-persona proof`. Table: Fact (§5 row) · Service · Natural query · Visible hits · Hidden by ACL · First visible hit (id) · Found? (YES / NO — routed). One row per §5 fact, plus the pasted `persona_view.py search` outputs.
- `## 6 · Triggers, incorporation and implicit requirements`. Table: Graded requirement · Seeded where · Trigger category the prompt must carry · Incorporating source (locator · persona-readable · unique · instructions-not-answer) · Inferable (yes, or gotcha → needs a trigger or is dropped). Then the anchor-name table `Anchor · May be named` (noun phrases of ≤ 6 words only, `;`-separated synonyms; the gate checks each entry).
- `## 7 · Dates and constraints`. Table: Item · Absolute date or value · Source · Past fact or deadline.
- `## 8 · Difficulty levers`. Table: Lever · Used · Load-bearing · Where it lives · Prompt-side condition. The conditions to test:
  - Ambiguity: the prompt is vague about where the answer lives, never about what is asked; the destination is named when the persona would know it, and left to the data only when finding it is the task and each place is findable from a persona-visible record (Eval 1 §1.5, §2.7; A-14).
  - Dynamic change: the correction is met second in discovery order (Prompt Writing §05). The prompt gives a reason to check the first summary but names neither the summary nor the correction.
  - Multi-source: 3+ systems carry weight, and no source is named as an exact artifact.
  - Async: discovery is unavoidable. Name no artifact on a waited search service and do not mention the wait.
  - Error recovery: the alternate path exists and is persona-readable (cite it), the failure is not mentioned, and no forced error sits on a scoped tool whose denial the agent must reason about.
  - Access control: an alternate route or an escalation is a reasonable action, and no requirement asks the agent to describe a restriction it never saw.
- `## 9 · Must not appear in the prompt`. The grouped list, with the source of each item.
- `## 10 · Entity traps`. The `entity.py` output verbatim, then a table: Correct entity (exact) · Lookalike(s) · How they differ · Locator (email or record id).
- `## 11 · Pre-submit checklist`. The Prompt Writing §08 items as unchecked boxes, plus task-specific boxes taken from §4, §6, §8 and §9.
- `## 12 · Blockers and routed defects`. Anything routed to `/create-injection`, `/create-error-async` or `/create-reference-files`, and any fact still unverified.
- `## 13 · Self-review`. As specified in Self-review below.

Every row of §2, §4, §5, §7 and §10 carries a record id, email or pointer; the gate counts them.

## Procedure — check mode (checklist)

- [ ] Read GEN_EXECUTION, this playbook, the brief, and `04_Prompt.txt` byte for byte. Never normalise whitespace, case or spelling. Record the word count (whitespace-delimited) and a 12-character sha256 prefix, which ties the report to this exact text.
- [ ] Run C1–C24 in order. For C17, extract every proper noun, ID, figure, date, relationship, state premise and asserted event from the prompt; look each one up with `tools/hg.py search` and check it against brief §10.
- [ ] Self-test the text against the 15 `calibration_cases` in `Evals/references/rules/prompt_qc_cases.json` (rules `staged_errors`, `trap_hint_or_riddle`, `hidden_destination`, `audit_form`, `if_chain`, `false_state_premise`, `ugt_both_fair_figure`) and `prompt_qc_examples.md`; report each as matched / not matched, never as a defect by itself.
- [ ] Record each finding with a quoted span, the rule and its source, the severity and the defect, under release `task-quality-v1` (a `prompt-ugt-v1` record is historical and needs a fresh review, A-31). Do not quote clean spans.
- [ ] Run the Self-review, then route (see the report template).

Severity words: **Fail** (scores 1–2 at `/prompt`), **Non-fail** (3–4), **Advisory** (no `/prompt` dimension; a hardness or later-stage risk), **UNVERIFIED** (evidence incomplete — never reported as Fail).

| # | Check (Eval 1 §) | Dimension · severity |
|---|---|---|
| C1 | Field: 20–4,000 words | Field limit · Fail (the field rejects it) |
| C2 | Assignment bound: all eight V3 fields in the shared context; persona resolves; source supports freeze | Intake BLOCKED until complete and supported; never change assigned fields |
| C3 | Persona (§1.1) and voice (§1.2): role plausibility, voice judged against the role only — the persona's own Slack/mail style is not a standard (A-27); would they know this situation, is it inside their remit (prepare / review / approve) | Persona · Fail (implausible) / Non-fail (fits another persona better). A better-fitting colleague alone is not a Fail |
| C4 | Competency, task skill, business function: assess the actual work independently from role; Authoring calls for an authored artifact | Mismatch alone is Non-fail / quality reduction under V3; role implausibility is C3 Fail |
| C5 | Complexity and seeding (§1.5): ≥ 1 of Ambiguity / Dynamic Change / Multi-Source is load-bearing (brief §8, cite where it lives); the prompt does not restate operating details that live, or should live, in records | Complexity Dimensions and Data Seeding · **Fail** (No Load-Bearing Complexity / Prompt Carries the Recipe) |
| C6 | Fair outcomes: test the strongest alternative for every deliverable against §4b and sidecar outcome reviews | Rejecting a fair reading fails; multiple valid answers alone does not |
| C7 | Clarity (§2.6): enumerate the concrete writes under each reasonable reading; scan "I'll / I need to / I want to / I'm going to [verb]" beside agent imperatives — "I'll [verb]" assigns the act to the persona unless the prompt also asks the agent for it; separate staging from approval, informing from waiting for permission, internal edits from external sends. A vague verb ("make sure", "clean up", "straighten out", "do whatever needs doing") with no competing concrete write is Minor — "make sure" / "check" defaults to verify and report; delegated discretion ("don't wait on me, go with your read") is authorized when records hold the rule. Report every deliverable whose channel, time or form is left open (email vs Slack to the same person, which free day, reminder vs event) — it is a Minor finding, not clean, when brief §4b lists that field as delegated or representational; an open **material** field is a C6 Fail (two acceptance classes) | Clarity · **Fail** (Action Decision Ambiguity — two named, incompatible writes are both supported: write now vs after approval, cover A vs cover B; or Major — intent unrecoverable and not settled by a documented convention) / Non-fail (Minor) |
| C8 | Incorporation (`prompt-incorporation-v1`): every record the prompt tells the agent to follow is (a) available — persona-readable or an uploaded file; (b) identified unambiguously or leads to one source; (c) actually states what is attributed to it; (d) supplies instructions, not a precomputed answer. A brief §6 requirement with no incorporating trigger is unauthorized | (a) Feasibility Fail · (b) UGT/Clarity Fail · (c) Truthfulness (C17 bands) · (d) Investigation Fail · untriggered requirement: Advisory (an unauthorized criterion later) |
| C9 | Pre-solved (§1.3.3): no root cause, conclusion, finding entity (the record or person the agent must identify) or presupposed answer count | Investigation · **Fail** (Pre-solved) |
| C10 | Discovery collapse: no brief §5 "No" item, hidden authority or async-target artifact is named by exact title, channel or ID | Advisory (defeats `01`; the wait never fires) — C9 if the named item is the finding |
| C11 | Investigation → action (§2.5): ≥ 1 catalog write, and the writes depend on what the investigation finds | Investigation · Fail when no write is asked (unless the assignment intends a read-only deliverable) or no write needs a finding |
| C12 | Tool use and cross-service (§2.4): tool-dependent; ≥ 2 services carry weight, the second not trivially; facts are scattered and must be reconciled | Tool Use and Cross-Service · Fail — this is the QC floor and the `/prompt` prediction. The tier's target (≥ 10 / ≥ 7 services and the rest of GEN_EXECUTION §3a) is a separate **blocking harness check**, not a C-finding: `stage_gate.py prompt-check` fails unless the manifest exists and the dossier's `hardness_gate` PASS for the tier's profile (Long Horizon → extreme, Normal → normal) is pasted and current (`tier.hardness`) |
| C13 | Coherence (§1.3.2): deleting any sentence changes something else. Several asks serving one stated purpose (one review, deadline, account or handoff) are stacking, not bolt-ons; a list of unrelated items joined only by the persona's to-do list is | Coherence · Fail (Bolt-on) · stacking alone: Advisory |
| C14 | Tool mention (§1.3.4): no function or parameter name, no MCP server name, no "the X tool". Natural product names ("in QuickBooks", "the Linear ticket") are clean (`prompt_qc_examples.md`, row 103) | Explicit Tool Mention · **Fail** (Evals override; QC form Non-fail for server/"tool") |
| C15 | Command list (§1.3.1): the prompt scripts the method in ≥ 2 sequenced steps — which sources, in which order, numbered or "first… then… finally". One check-before-acting constraint, or the order of deliverables and who to tell (the screen 24 skeleton), is not a command list | Contrived · Fail |
| C16 | Ordinary request (§2.7, §1.2): no spec-sheet layout, answer-key clause, arbitrary format constraint or call-inflation choreography. Each of these fails on its own: staged errors (misspellings, made-up emoji, broken punctuation — clean spelling, capitals and punctuation are fine); a riddle or hint aimed at the trap ("Hidden root causes the prompt does not hint at" is the good indicator, naming the symptom is fine, "a nagging feeling the thing that actually bites us is not on anybody's list" fails); a plausibility hedge letting a record correct the prompt ("If my date or channel is off, use the message that is actually there"); a hidden destination the persona would know (name it; leave it to the data only when finding it is the task and each place is findable from a persona-visible record); audit or compliance-form wording (deliverable-catalogue verbs: "reconcile…, classify…, rank…, complete the review artifacts and handoff it requires"); long if / but-not / then-also chains (a per-case rule belongs in a seeded record — "Can you sort out the leftover reviews before Friday? Arthur posted how he wants each kind handled." passes) | Contrived / hinting · Fail where present; two or more spec-sheet triggers also fail (§2.7 hard gate). Calibration: `prompt_qc_cases.json` rules `staged_errors`, `trap_hint_or_riddle`, `hidden_destination`, `audit_form`, `if_chain` |
| C17 | Truthfulness (§2.3): every tight identifier (channel, file/doc/repo name, ticket ID, entity name, email, amount, date), relationship, state premise ("still no reply", "there's no ticket", "for two weeks", "I own this"), company/people premise (business as usual after the Feb 11, 2026 shutdown on a Feb 14 task, a departed person still acting — Victor since April 2025, anything not existing by 2025-09-30 23:59:59 PT on an Oct 1 task; A-26/B-16) and narrative claim (who emailed whom when, what the persona has been working on, people said to be in a channel). A near-match is a phantom; a misspelt tight identifier that matches no record is a finding (quote it, give no correction). Hypotheses ("I think it's fixed, check") and requested new outputs are not premises. Absence needs the absence rule below | Truthfulness · Fail (1 major — wrong or phantom tight identifier, contradicted state premise, one loose factual slip — or 2+ minor) / Non-fail (none for a loose descriptor). Unverifiable premise: UNVERIFIED, and confirm the task is solvable without it |
| C18 | Feasibility (§2.2 A–D, §3.1): per deliverable, the catalog can create, format and deliver it (a draft is not a send); every needed fact exists and has a cataloged read; every per-X breakdown has an X field; every exact value or precision survives the tool path; no conflicting instructions; no human-judgement, physical or beyond-tool asks | Feasibility · **Fail** (no middle band, Evals override; any explicit ask). Incomplete capability or rendering evidence: UNVERIFIED |
| C19 | Persona ACL (§2.2 E, standalone): lens 1 — every required Gmail / Slack / GCal / Drive-family read is visible to the persona, or an unscoped alternate exists, or the intended outcome is an affirmative denial finding plus report/escalation; lens 2 — no ask directs the persona to read someone else's scoped data. Writes are never ACL-scoped | Feasibility (Persona ACL) · **Fail**, non-waivable |
| C20 | Today's date (§2.8): past events fall before the clock; later dates only as semantic future dates for events that have not happened (deadline, meeting start, scheduled send — 08 hard gate 4); relative wording resolves to one window; "today"/"yesterday" are `universe.persona_today` (Sat Feb 14, 2026 / Wed Oct 1, 2025) and the day before; dates are Pacific, both days when PT and UTC differ; the QC form's "today is February 28, 2026" does not apply (A-30) | Alignment with Today's Date · **Fail** on a material contradiction (a post-clock event described as done is also C17). Relative wording alone: Advisory (Prompt Writing §4.2 asks for absolute dates; `/prompt` allows it) |
| C21 | Injected friction (§3.2): no injected failure or wait is announced; every forced error leaves a persona-readable alternate path; no forced error on a scoped tool whose denial the task turns on | Announced: Contrived Non-fail (Pre-solved Fail if it hands over the workaround) · a configuration that removes the only route: Cross-Service Coherence Fail |
| C22 | Universe coherence (§3.2) on records the prompt touches: reuse a matching `/injection` PASS; report any inconsistency met during C17–C18 | Cross-Service Coherence · Fail / Non-fail (one minor) |
| C23 | Originality (§2.9): fingerprint (scenario, persona + scenario, entities, asks, services + writes, shape, phrasing) against each sample supplied with the task and against the guideline, taxonomy and `long_horizon.md` examples | Supplied sample: Originality · **Fail** at a verbatim / near-verbatim sentence, same scenario + entities, ≥ 4 of 7, or persona + scenario + ask lift; Non-fail at 2–3. Guideline examples only: Advisory (`/prompt` §2.9 is N/A without supplied samples) |
| C24 | Diversity (§1.4): more than "investigate + post one Slack message" | Advisory |

**Fair-reading procedure (C6; replaces V2 unique-ground-truth rejection).** For each deliverable:
1. Write Reading A (best-supported) and Reading B (the strongest plausible alternative, not a strawman). Give each its decision, writes, destinations and contents. Account for every explicit option the prompt lists.
2. Settle each material difference only by: a newer source on the same issue and scope (before the clock); an incorporated source's authority over the decisions it governs; source identity (whose words or which record the prompt names); scope (a partial update leaves the rest standing); or the same material result (decision, writes, destinations and contents all the same — the same destination alone is not enough).
3. If both readings remain fair, include both in §4b and the sidecar `accepted_outcomes`; record why each is defensible. Multiple results, rounding, anonymized source tokens and Pacific/UTC date variants do not fail solely for differing. An unsupported premise or impossible write is still a truthfulness/feasibility defect. Test the cheapest valid reading for a shortcut; if it makes the task too easy, change the universe/design rather than excluding that reading in the rubric.
4. Record both readings, resolving or accepting evidence, and the current outcome-review artifact hash in the sidecar. In prompt-check also supply the assigned-role review with source IDs and an explicit remit rationale. The Guide defines the schema.

**`BOTH_FAIR_FIGURE`** (Eval 1 §2.1, A-24/B-15) is the only PASS for a single reported figure that no source settles, and only when all five hold: the decision, writes, destinations and recipients are identical and only that figure differs; each value sits on a persona-visible record other than the prompt; no newer source, authority check, source identity or scope check settles it; each reading completes every ask; the figure does not change the next action. Record it with both quotes, leading reading first (`kind` AMOUNT / COUNT / RATE / DATE), so the report prints "Rubric must accept: X or Y". Never add a "go with the most recent" line (it settles the fork), a file-now-versus-defer fork is not a figure, and a newer source still settles (#49).

**Absence rule (C17, C18).** "Does not exist" needs the search scope (service, file, query), the surfaces searched (records, attachments, repository files and refs, table metadata, the SQL overlay) and a positive control showing the lookup works; otherwise it is UNVERIFIED. One counter-example refutes an absence.

## Check report template

```
# Prompt Check — <task slug>
> Prompt: 04_Prompt.txt · <n> words · sha256 <12 chars> · Clock: <universe.clock_line> · checked <date> against 04_Prompt_Writing_Brief.md (<date>) · release task-quality-v1
> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.
```

- `## Summary`. Fail count · Non-fail count · Advisory count · UNVERIFIED checks · checks clean (C-ids) · predicted `/prompt` band (FAIL if any Fail; NON-FAIL if any Non-fail or an UNVERIFIED hard gate among C4, C6, C17, C18, C19; else PASS) · Status: BLOCKED (any Fail or C2), UNRESOLVED (UNVERIFIED hard gate) or READY FOR /prompt.
- `## Findings`. Table: # · Check · Dimension · severity · Quoted span · Rule (source) · Defect.
- `## UGT readings`. Per deliverable: Reading A · Reading B · resolution and evidence.
- `## Verification log`. Table: Span · Type (person / ID / figure / date / event / state / channel / doc) · Universe record (locator) · Result.
- `## Brief coverage`. Table: Brief item (§4 deliverables, §6 triggers) · Present in the prompt (quoted span, or "absent").
- `## Self-review`. As specified below.
- `## Route`.
  - **Any Fail:** edit `04_Prompt.txt` (Claude, Codex or the human), then re-run `/create-prompt-writing check`. The new hash shows the text changed.
  - **Universe-rooted defect** (missing evidence, two credible sources): fix it via `/create-injection`, not the prompt.
  - **UNRESOLVED:** name the missing evidence; it does not clear the gate (GEN_EXECUTION §3).
  - **No Fail:** paste `04_Prompt.txt` exactly as saved into `/prompt`, paired with `/injection`, using the GEN_EXECUTION §7 paste list. Whether to act on Non-fail or Advisory findings is the human's call.
  - **`/prompt` FAIL is fatal in V2**, because no hint can rescue an unsolvable prompt. Fix the cause and re-run.

## Self-review (GEN_EXECUTION §6a)

Every mode ends with this loop and records it under `## Self-review` in its output.

1. **Re-read as the eval.** Walk `Evals/1_Prompt_Eval.md` Phases 1–3 in order against the output (not
   from memory), and confirm every C-check has a finding, a clean result with evidence, or UNVERIFIED.
2. **Strongest counter-reading.** For every PASS-direction result write the best case that `/prompt`
   fails it; for every Fail or Non-fail finding write the best case that it is a false positive. Resolve
   each with a record pointer, an Eval 1 § or a case id from `prompt_qc_cases.json`, never opinion:

   | Area | Counter to a PASS | Counter to a FAIL |
   |---|---|---|
   | Fair alternatives (C6) | Is Reading B the strongest? Is every defensible result accepted, with sources and a current outcome review? | Is a rejected result actually wrong, or merely a second fair reading? Would accepting it expose a universe shortcut that must be fixed upstream? |
   | Clarity (C7) | Is an unpinned channel, time or form left unreported? Does an "I'll" sit beside the same ask to the agent? | Are the competing writes named, incompatible and both supported — or is it one vague verb (Minor)? |
   | Incorporation (C8) | Does the pointed-to record exist, readable by the persona, unique, and state the rule attributed to it — or does it hand over the answer? | Is the requirement actually incorporated by the prompt, or only found during research (then it adds no obligation and no defect)? |
   | Truthfulness (C17) | Was every tight identifier, state premise and narrative claim looked up in this run, near-matches included? | Is it a hypothesis or a requested new output? Does the absence claim meet the absence rule? Is a misspelling harmless to lookup? |
   | Feasibility and ACL (C18–C19) | Can the persona read every required scoped record (sender, membership, share)? Does the tool path keep the asked precision, field and delivery (draft ≠ send)? | Is there an unscoped alternate, an affirmative-denial outcome, or only incomplete capability evidence (UNVERIFIED, not Fail)? |
   | Contrived register (C15–C16) | Does the request hint at a trap/cause, read as a riddle, an audit form or an if-chain, use planted mistakes, hide a destination the persona knows, or hedge a fact a record then corrects? | Is it an ordinary request with clean spelling, one plain ask and a known named destination? |

3. **Re-verify facts, not notes.** Re-read every load-bearing value through `tools/hg.py`; a value
   carried from the brief, dossier or an earlier check is a lead, not evidence.
4. **Draft grounding** (draft mode). Every name, ID, date and figure in the drafted prompt is looked up in this run; nothing from brief §9 appears.
5. **Mechanics.** Every quoted span is an exact substring of `04_Prompt.txt` (verify programmatically);
   each severity follows the C-table and each Fail names its `/prompt` category; the `04_Prompt.txt`
   hash is identical before and after the run. Brief mode: every fact has a locator verified in this run;
   persona view, assigned clock and fair-outcome acceptance hold; the root cause appears only in §5; a design-level Fail
   is routed, never worked around.
6. **Record** per check: final result, evidence, each counter-reading and its resolution, and anything
   left UNVERIFIED (named, never hidden). Never soften a finding to reach READY; never invent one to
   look thorough. Gate minimum: brief — one evidenced counter-reading per area of the table above (UGT,
   Clarity, Incorporation, Truthfulness, Feasibility/ACL, Contrived);
   check — one evidenced counter-reading row per C-check (C1–C24, named by id).
7. **Stage gate.** Brief: `python3 Task_Authoring/tools/stage_gate.py prompt-writing Task_Authoring/task_inputs --paste`.
   Check: `python3 Task_Authoring/tools/stage_gate.py prompt-check Task_Authoring/task_inputs --paste` (it recomputes the
   word count and sha256 of `04_Prompt.txt`, verifies every quoted span as an exact substring, and certifies the tier: manifest present,
   `hardness_gate` PASS for the tier's profile pasted in the dossier and current — `tier.hardness`). Brief mode also
   requires the §4b outcome table and current sidecar fair-reading review. The checks
   verify recorded review evidence, not semantic fairness. Handoff is blocked until PASS.

## Deliver

- **Both modes.** Handoff is blocked until `stage_gate.py prompt-writing` / `prompt-check` prints PASS; its output sits in the Self-review.
- **Brief mode.** Report the path, the routed blockers and any unverified facts. Next step: `/create-prompt-writing draft` (or the human writes `04_Prompt.txt`), then `/create-prompt-writing check`.
- **Check mode.** Report the path, the Fail findings by C-id, the predicted band and the route. Next step: edit the prompt (Claude, Codex or the human) and re-check, or, with no Fail, runs `/injection` + `/prompt`. After that comes `/create-humantime`.
- **Task date.** `/prompt` and `/injection` ask the task date first; answer with the assignment's universe date (the selected universe, GEN_EXECUTION § 0a), never inferred.
