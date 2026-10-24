# 04 — Prompt Brief & Prompt Check (Playbook) — HarmonyGames · Spec V2

> Command: `/create-prompt-brief` (brief) · `/create-prompt-brief check` (check) · Writes: `task_inputs/04_Prompt_Brief.md` / `task_inputs/Working_Files/04_Prompt_Check.md` · Paired eval: `/prompt` · Read first: `setup/GEN_EXECUTION.md`

## Purpose

In Spec V2 the prompt is human-only (GEN_EXECUTION §2). This command helps the human
before and after they write it, and never writes it:

- **Brief mode** writes `04_Prompt_Brief.md`: the design facts to read before typing.
  It covers what the assignment demands, what the universe holds, the one final state
  the prompt must pin, what the agent must discover, and what must stay out of the prompt.
- **Check mode** reads the human's `04_Prompt.txt` and writes `04_Prompt_Check.md`:
  report-only findings against the brief, the universe and the QC Spec V2 prompt
  dimensions. The human then fixes their own text before `/prompt`.

Both modes follow Rule zero (`references/Docs/05_Prompt_Writing.md` §03): seed the
context, don't type it in. The universe carries the rules, the detail and the difficulty;
the prompt is a short trigger that names the problem, not the method. A short prompt
still needs exactly one end state. Leave the rules and evidence in the universe, but
never leave the destination open.

Run order: after `/create-injection` (and `/create-error-async`, `/create-reference-files`
if used); before `/create-humantime` and the `/injection` + `/prompt` pair.

## The authorship boundary

- No mode produces prompt text in any form: no draft or partial draft, no opening line, no sample phrasing, no "the prompt could say…", no fill-in template, no key-phrase list, no tone or voice example in the persona's register.
- The brief describes requirements, not wording. Use fields, noun phrases and record locators, written in the third person. You may cite the guideline's own ✗/✓ examples by section; you may not invent task-specific phrasings.
- Style guidance stays at guideline level. Point to `05_Prompt_Writing.md` §4.1 and the taxonomy screen "Before You Write: Sound Human, Not LLM", and add nothing task-specific. Never coach text past the AI-text detector.
- Check mode never proposes replacement wording and never rewrites, paraphrases or tidies the prompt. It never corrects or counts typos, capitalisation, punctuation or spelling, because casual typing is expected. It never scores or predicts the AI-text detector.
- **Refusal.** The human may ask this command to write, draft, rewrite, shorten, polish, "humanize", translate or grammar-fix the prompt, or to add typos to it. Decline: Spec V2 prohibits LLM drafting and polishing (`05_Prompt_Writing.md` §4.1, GEN_EXECUTION §2). Offer the brief or the check instead. The same applies to Oracle Events and rubric criteria.
- The brief is for the human to read. It is never pasted into the eval sandbox or any model to generate text.

## Inputs / Output

Brief-mode inputs (stop and name any missing required slot)
- `task_inputs/00_Assigments.md` (required): business function, persona, competency, task skill, task type.
- `task_inputs/Working_Files/01_Grounding_Dossier.md` (including its "Facts for the human") + `01_Universe_Inject.sql`: required if anything was seeded. If nothing was seeded, say so and ground on the base universe.
- `task_inputs/03_Error_Async_Config.txt`, `02_Reference_Files_Manifest.md`, `01a_Hardening_Report.md` if present. Carry over every "must not appear in the prompt" constraint, every alternate-path fact and each file's "how the persona would refer to it" description.
- `Evals/references/persona/roster.json` (17 personas — the `/prompt` identity gate; `references/persona_roster_v2.json` adds the platform's `thomas`/`tim_steudler`, which fail that gate), `references/Docs/04_Persona_ACL_Policy.md`, `Evals/references/persona/acl.md`.
- `01_Scenario_Design.md` (anchors, hidden authorities, delegation lattice, deliverables) and `01_Hardness_Manifest.json`.
- `Evals/references/tools/catalog.json` (298 tools): write capability and the forbidden-name list.
- `references/Docs/00_Taxonomy_V2_Step_Map.md` appendix: the five competency pages (screens 5–9), Task Skill (10), Task Complexity Dimensions (12), Sound Human (23) and Write the Prompt goal + writing guideline (24).
- `references/Docs/05_Prompt_Writing.md`, `10` §3–5, `11`, `12`; the Prompt rows of `references/Docs/QC_Spec_V2.csv`.
- The universe, only through `Task_Authoring/tools/hg.py search` (GEN_EXECUTION §4).

Check-mode inputs
- `task_inputs/04_Prompt.txt` (required), human-written and exactly as it will be submitted.
- `task_inputs/04_Prompt_Brief.md` (required).
- The brief-mode inputs, for verification.

Output: brief mode writes only `04_Prompt_Brief.md`, and check mode writes only
`04_Prompt_Check.md`. Neither mode creates, edits or touches `04_Prompt.txt`.

## Hard gates

1. **No transcribable sentence** in either output. If the human could paste a line into the prompt field, delete that line.
2. **Grounded.** Look up every name, ID, figure, date and locator with `tools/hg.py search` during this run. Never use memory, notes or an earlier draft. Confluence and Snowflake are live and unscoped; verify their values like any other source.
3. **Persona view.** Confirm every fact the task depends on is readable by the assigned persona:
   - Gmail, Slack, Calendar and the Drive family are scoped to the persona.
   - GitHub, Linear, Trello and Contacts are shared.
   - Confluence and Snowflake: unscoped per the current Evals (`acl.md`); confirm the page/table exists and appears in the pre-check run.

   Universe Explorer's god-mode view never counts. Check writes against the catalog, not the ACL.
4. **Clock: 2026-02-14T00:00:00Z, a Saturday.** Absolute dates are safest; clear relative wording is allowed by the current `/prompt`. Past facts fall before the clock. A later date may appear only as a deadline that has not happened yet (`12_Example_Task.md` §2, "The date").
5. **One final state.** Pin exactly one set of deliverables, destinations and recipients. If the universe supports two final states, stop and route the defect to `/create-injection`; the brief must not paper over it. Examples: two equally credible sources, two plausible filing locations, act vs defer.
6. **Symptom, not cause.** The root cause appears only in the discovery map, flagged "never in the prompt". The situation section says what is visibly wrong, never why.
7. **Report-only check.** Every finding gives four things: a verbatim span of `04_Prompt.txt` (verified as an exact substring), the rule and its source, the QC Spec V2 severity, and the defect. Nothing else.
8. **Write boundary** (GEN_EXECUTION §1): write only under `Task_Authoring/task_inputs/`, execute no SQL, and write nothing under `Evals/`, `claude/` or `HarmonyGames_*`.

## Procedure — brief mode (checklist)

- [ ] Read GEN_EXECUTION, this playbook and `05_Prompt_Writing.md` in full. Load the upstream slots.
- [ ] **Assignment.** Copy the five axes verbatim from `00`.
  - Resolve the persona in the roster: exact name, email, role and department. Never infer an email.
  - Record the competency's focus and expected outputs (its taxonomy page) and the task skill's definition.
  - Record the tier: Normal 50–100 calls, Long-Horizon 100–500+, Super-Long-Horizon paused.
- [ ] **Remit.** Explain from cited records why this persona would plausibly be pulled into this competency's work: what they did, own or saw. The competency sets the kind of work, not the job title. If no defensible remit exists, stop and report it. Never switch personas.
- [ ] **Breadth for the tier.** List the services that carry real weight: at least 2, target 3+, and 3+ for Long-Horizon. Give the measured volume behind each (messages in the window, rows, tickets). Length comes from evidence breadth and reasoning depth, not from the number of deliverables (`09_Long_Horizon_Task.md` §3). Do not estimate a call count.
- [ ] **Situation.** From the dossier, record the visible symptom, who sees it (the persona's vantage) and where it shows (a locator).
- [ ] **Phases.** Investigation: the questions to resolve, without their answers. Action: the writes those answers feed. Confirm each write genuinely depends on the investigation.
- [ ] **Final state.** For each deliverable, record its kind, its exact destination, its exact recipients (from Contacts or the roster) and the catalog write it needs. Keep only writes the scenario needs. Each write needs reads first. Independent writes added for volume are bolt-ons.
- [ ] **Decision-ambiguity scan.** For each deliverable, list what else a careful run could defend:
  - another destination or recipient;
  - act now vs defer, or file vs chase;
  - the persona doing it vs delegating it ("I'll" vs "you").

  Record what settles each one: the prompt's scope, or a documented universe convention (cite it). Discovery ambiguity passes; decision ambiguity fails (`05` §07).
- [ ] **Discovery map.** Start from "Facts for the human". For each fact the agent must find, record its value, locator, persona readability, and which source the agent meets first and what overturns it.
  - Default: never name it in the prompt. Naming an artifact turns a fuzzy search into one exact fetch (`05` §06).
  - A human-readable item off the discovery path may be named, but only if the persona would know it.
- [ ] **Search-behaviour risks**, per fact. These are design notes for this brief only, not prompt content:
  - Agents latch onto the first framing they meet.
  - They stop at a message that sounds like a conclusion, even when the thread continues.
  - They prefer secondhand chat over structured systems (GitHub, Linear, Snowflake).
  - They rarely search for a reply to a dispute or a question.
  - They never see results past the search limit.

  If a load-bearing fact cannot be found by a search the agent would plausibly run, route it to `/create-injection`. If it lives only in Confluence or Snowflake, note that the agent's system prompt advertises neither service.
- [ ] **Triggers.** For every seeded requirement the rubric will grade, record what kind of trigger the prompt must carry: a deliverable, scope, constraint or recipient. Never write it as a clause. Separate requirements a competent assistant would obviously infer (checking data before filing, telling the requester) from gotchas nobody could infer. A gotcha gets a trigger or is dropped, otherwise its criterion is unauthorized.
- [ ] **Dates and constraints**, each with its absolute date and source.
- [ ] **Levers.** Fill the template §8 table for all six characteristics.
- [ ] **Must-not-appear list.** Build it from these sources:
  - catalog tool names and parameters for every service in play;
  - MCP server names;
  - internal and opaque IDs from the dossier, and opaque filenames;
  - the root cause;
  - each injected failure or wait, and each async-target artifact (from `01`);
  - reference-file paths and `/app/artifact` (from `02`);
  - markdown and numbered steps.
- [ ] **Entity traps.** Search Contacts, Slack and Gmail for shared first names, lookalike channels, ticket series and similar documents. Known traps (`11_QC_Companion.md`): three Marcuses plus Oscar Bennett; ENG-#### vs ZOM-###. Pin the correct entity's exact identity.
- [ ] **Name-swap test.** Swap every name in the situation for a different one. If the scenario still works, it rests on no real records; route it to `/create-injection`.
- [ ] Write the brief from the template below, then run the self-check.

## Brief template

The section headings of `04_Prompt_Brief.md`, in order. Every cell holds a fact,
a locator or a requirement, never wording.

```
# Prompt Brief — <task slug> · prep only · contains no prompt text
> Built <date> from <slots read> · Persona view verified: <all | list of exceptions>
> Write 04_Prompt.txt yourself, from scratch, without an LLM (Spec V2).
```

- `## 1 · Assignment fit`. Table with columns Axis · Assigned value · What it requires here (cited).
  - Business function.
  - Persona: name, email, role; voice and remit in one line; read scope (scoped services and key channels it is in).
  - Competency: focus, expected outputs, remit argument.
  - Task skill: the assigned skill, any stacked skills, and the deliverable or discovery that exercises each.
  - Task type: the tier, the services that carry weight and the measured volumes.
- `## 2 · Situation`. Symptom · Seen by · Where it shows (locator) · Relevant records the persona cannot see. Third person; no cause.
- `## 3 · Investigation → action`. The questions to resolve (no answers), then the writes they feed.
- `## 4 · Pinned final state (UGT anchor)`. Table: Deliverable · Destination (exact) · Recipient(s) (exact) · Catalog write (reference only; never in the prompt) · Fed by. Below it, a risk table: Decision-ambiguity risk · Alternative a careful run could take · What pins it.
- `## 5 · Discovery map`. Table: Fact · Value · Locator · Persona-readable · Met first / overturned by · Search risk · Name in prompt? (No by default, or Yes with the reason).
- `## 6 · Triggers and implicit requirements`. Table: Graded requirement · Seeded where · Trigger category the prompt must carry · Inferable (yes, or gotcha → needs a trigger or is dropped).
- `## 7 · Dates and constraints`. Table: Item · Absolute date or value · Source · Past fact or deadline.
- `## 8 · Difficulty levers`. Table: Lever · Used · Where it lives · Prompt-side condition. The conditions to test:
  - Ambiguity: the prompt is vague about where the answer lives, never about what is asked; the destination is pinned.
  - Dynamic change: the correction is met second in discovery order. The prompt gives a reason to check the first summary (`12` §2, "It builds in the trap") but names neither the summary nor the correction.
  - Multi-source: 3+ systems carry weight, and no source is named as an exact artifact.
  - Async: discovery is unavoidable. Name no artifact on a waited search service and do not mention the wait.
  - Error recovery: the alternate path exists and is persona-readable (cite it), the failure is not mentioned, and no forced error sits on a scoped tool whose denial the agent must reason about.
  - Access control: an alternate route or an escalation is a reasonable action, and no requirement asks the agent to describe a restriction it never saw.
- `## 9 · Must not appear in the prompt`. The grouped list, with the source of each item.
- `## 10 · Entity traps`. Table: Correct entity (exact) · Lookalike(s) · How they differ · Locator.
- `## 11 · Pre-submit checklist`. The `05_Prompt_Writing.md` §08 items as unchecked boxes, plus task-specific boxes taken from §4, §6, §8 and §9.
- `## 12 · Blockers and routed defects`. Anything routed to `/create-injection`, `/create-error-async` or `/create-reference-files`, and any fact still unverified.

## Procedure — check mode (checklist)

- [ ] Read GEN_EXECUTION, this playbook, the brief, and `04_Prompt.txt` byte for byte. Never normalise whitespace, case or spelling. Record the word count (whitespace-delimited) and a 12-character sha256 prefix, which ties the report to this exact text.
- [ ] Run C1–C23 below. For C11, extract every proper noun, ID, figure, date and asserted event from the prompt. Look each one up with `tools/hg.py search` and check it against brief §10.
- [ ] Record each finding with a quoted span, the rule and its source, the severity and the defect. Do not quote clean spans.
- [ ] Route (see the report template).

| # | Check | QC Spec V2 dimension · severity |
|---|---|---|
| C1 | Word count is 20–4,000 (Taxonomy step 24) | Field limit · Fail (the field rejects it) |
| C2 | One final state: every §4 deliverable, destination and recipient is determinate. No act-vs-defer split, no A-vs-B split, no "I'll do it" vs "you do it" split | UGT · Fail (Multiple Valid Answers); Clarity · Fail (Action Decision Ambiguity) |
| C3 | Intent is recoverable; readings differ only in wording, or in channel to the same recipient | Clarity · Fail (Major) / Non-fail (Minor) |
| C4 | Every §6 graded requirement has a trigger in the prompt | No prompt row · Non-fail now; if graded later, it is an unauthorized criterion |
| C5 | No root cause, conclusion or answer is stated | Investigation · Fail (Pre-solved) |
| C6 | No tool or parameter name, no MCP server name, no "the X tool" | Explicit Tool Mention · **Fail** (the current `/prompt` treats all three as pass/fail) |
| C7 | No internal ID or opaque filename a real person would not know (human-readable titles are fine) | Contrived · Fail (unnecessary opaque reference) / Non-fail (single tell) |
| C8 | No §5 "No" item and no async-target artifact is named, otherwise discovery collapses to a fetch and the wait never fires | No QC row · Non-fail (it defeats `01`); also C5 if naming it hands over the answer |
| C9 | No injected failure or wait is announced | Contrived · Non-fail; Pre-solved · Fail if it hands over the workaround |
| C10 | Past events fall before the clock; later dates appear only as deadlines; relative wording is unambiguous | Today's Date · **Fail** on a material temporal contradiction; a post-clock event described as done is also Truthfulness · Fail |
| C11 | Every proper noun, ID, figure, date and asserted event is true of the universe, and the entity traps are cleared | Truthfulness · Fail (1 major or 2+ minor) / Non-fail (1 minor). Tight identifiers are major; loose descriptors are minor unless they cause failure |
| C12 | Persona: the remit and the content are plausible for the assigned persona | Persona · Fail (implausible) / Non-fail (fits another persona better) |
| C13 | Competency, business function and task skill(s) match brief §1 | Competency / Task Skill · **hard Fail**; Business Function · Non-fail |
| C14 | Feasible: required reads are persona-readable, writes are in the catalog, no instructions conflict, every ask achievable | Feasibility · **Fail** (no middle band in the current `/prompt`) |
| C15 | The universe is needed; 2+ services (target 3) carry weight — the design carries ≥ 10 (`01_Hardness_Manifest.json`); both investigation and action are required | Tool Use & Cross-Service · Fail |
| C16 | Bolt-on test: deleting any sentence changes something else | Coherence · Fail |
| C17 | Plain prose. None of: markdown, headings, bullets, numbered or sequenced steps, spec-sheet register (item-by-item deliverable contents, output-format rules), arbitrary format constraints, exact-timestamp demands, or the stock formal phrases listed in `05` §4.1 | Contrived · Fail / Non-fail (single tell) |
| C18 | No sentence copied or lightly reworded from a guideline/taxonomy example or the ML-selected task | `/prompt` §2.9 applies only to supplied samples (N/A otherwise) — report as advisory |
| C19 | Spec-sheet register: ≥ 2 of {item-by-item deliverable contents, preservation/format rules, prescribed reply format, contents-driven length} | Contrived · **Fail** (`1_Prompt_Eval.md` §2.7) — the lattice must carry those details |
| C20 | ACL lens 2: the prompt does not direct the agent to read another person's scoped data | Feasibility (Persona-ACL hard gate) · Fail |
| C21 | Every asked figure is observable at the asked precision; every per-X breakdown has a per-X field | Feasibility (numeric/dimensional observability) · Fail |
| C22 | Requested outputs use native service writes (Docs/Sheets/Slides/Confluence/Linear/Trello/GitHub/Gmail/Slack/Calendar); no unverifiable file-format exports | Feasibility (output capability) · Fail if unsupported |
| C23 | Hidden authorities and the hub are **named, never located**: the prompt identifies each anchor in plain words that lead to one source, without naming its service, channel, board, file or ID | Clarity/UGT if the name is ambiguous · Fail; a located authority collapses A12 (report as a hardness defect) |

## Check report template

```
# Prompt Check — <task slug>
> Prompt: 04_Prompt.txt · <n> words · sha256 <12 chars> · checked <date> against 04_Prompt_Brief.md (<date>)
> Report-only. No replacement wording. Typos and capitalisation are not assessed.
```

- `## Summary`. Fail count · Non-fail count · checks clean (C-ids) · Status: BLOCKED or READY FOR /prompt.
- `## Findings`. Table: # · Check · Dimension · severity · Quoted span · Rule (source) · Defect.
- `## Verification log`. Table: Span · Type (person / ID / figure / date / event / channel / doc) · Universe record (locator) · Result.
- `## Brief coverage`. Table: Brief item (§4 deliverables, §6 triggers) · Present in the prompt (quoted span, or "absent").
- `## Route`.
  - **Any Fail:** the human edits `04_Prompt.txt` themselves, then re-runs `/create-prompt-brief check`. The new hash shows the text changed.
  - **Universe-rooted defect** (missing evidence, two credible sources): fix it via `/create-injection`, not the prompt.
  - **No Fail:** paste `04_Prompt.txt` exactly as saved into `/prompt`, paired with `/injection`, using the GEN_EXECUTION §7 paste list. Whether to act on Non-fail findings is the human's call.
  - **`/prompt` FAIL is fatal in V2**, because no hint can rescue an unsolvable prompt. Fix the cause and re-run.

## Self-check

Brief mode
- Scan for transcribable text and delete any:
  - quoted strings not taken from a record or a guideline;
  - first-person or casual-register sentences;
  - "could say", "something like", or "e.g." followed by a phrase;
  - opening lines.
- Every fact has a locator verified in this run. Persona view, clock and one final state hold. The root cause appears only in §5.
- QC Spec V2 dimensions the brief protects: UGT, Clarity, Feasibility, Truthfulness, Investigation, Tool Use & Cross-Service, Persona, Competency, Business Function, Task Skill, Date Alignment. A design-level Fail blocks handoff; route it, never work around it.

Check mode
- Every quoted span is an exact substring of `04_Prompt.txt`; verify this programmatically.
- No finding contains replacement wording, "instead", "consider", "try", or any remark on typos, capitalisation or AI-likeness.
- Each severity follows the C-table, and each Fail names its QC Spec V2 failure category.
- The `04_Prompt.txt` hash is identical before and after the run.

## Deliver

- **Brief mode.** Report the path, the routed blockers and any unverified facts. Next step: the human writes `04_Prompt.txt` from scratch without an LLM, then runs `/create-prompt-brief check`.
- **Check mode.** Report the path, the Fail findings by C-id, and the route. Next step: the human edits the prompt and re-checks, or, with no Fail, runs `/injection` + `/prompt` (`Evals/1_Prompt_Eval.md` is the eval `/prompt` runs). After that comes `/create-humantime`.
