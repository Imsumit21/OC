# 01 — Scenario Design (Playbook) — HarmonyGames · Spec V2 · effective profile (extreme by default)

> Command: `/create-scenario` · Writes: `task_inputs/Working_Files/01_Scenario_Design.md` + the draft manifest `task_inputs/Working_Files/01_Hardness_Manifest.draft.json` · Checks: `tools/hardness_gate.py --design`, `tools/redteam_review.py --mode redteam --dual`, **`tools/stage_gate.py scenario` (blocking)** · Next: `/create-injection` · Read first: `setup/GEN_EXECUTION.md`, `references/Hardness_Mastery.md`

**Profile.** S0 resolves the task's `effective_profile` once and writes it into the draft manifest
(Long Horizon → `extreme`; Normal Horizon → `normal`, or `extreme` only with a recorded
`profile_exception`). Every number below is the **extreme** value; on `normal` use the `normal`
column of `GEN_EXECUTION.md` §3a (the gate's `PROFILES` table is the source). No command takes a
`--profile` of its own choosing: `hardness_gate.py` reads the manifest and fails a disagreeing flag.

## Purpose

Design the task's difficulty **before any SQL is written**, so the injection implements a
design that is already proven to be broad (10–13 services), voluminous (≥ 500 necessary
agent calls), genuinely hard for Opus (built from the measured mechanisms A1–A21 in
`Hardness_Mastery.md` §0) and fair (every defensible outcome accepted, every requirement incorporated,
every record reachable).

The two failure modes this stage exists to prevent:
1. **"It says it's hard."** Easy asks stacked into a long list, injected into 2–3 services.
   Countered by the manifest + gate: breadth, depth and traps are declared as checkable
   records, then verified against the SQL.
2. **"It's hard because it's unfair."** Ambiguous asks, unreachable evidence, unincorporated
   rules, one choke point. Countered by the QC rails in §S8.

This stage may design scenarios, traps and record plans. It never drafts prompt text,
Oracle Event text or criterion text (GEN_EXECUTION §2).

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
- `task_inputs/00_Assigments.md` — persona, business function, competency, task skill, horizon.
- `references/Hardness_Mastery.md` (techniques + evidence), `references/Scenario_Atlas.md`
  (verified storylines with per-service anchors), `references/Ask_Carriers.md` (where asks and
  facts can live; per-item call costs; bulk shortcuts), `references/Universe_Brief.md`,
  `references/Persona_Briefs.md`.
- The universe through `Task_Authoring/tools/hg.py search` / `tools/hg.py records` (GEN_EXECUTION §4).

Output
- `task_inputs/Working_Files/01_Scenario_Design.md` — the design dossier (template at the end).
- `task_inputs/Working_Files/01_Hardness_Manifest.draft.json` — the draft manifest (`references/Hardness_Manifest_Spec.md`),
  with ids minted in S2 (no placeholders: the stage gate rejects template slots). `/create-injection` writes
  the final `01_Hardness_Manifest.json`, keeping every draft id or recording the change in `design_delta`.

## Hard gates

1. **Persona can carry it.** The persona is one of the 17 in `Evals/references/persona/roster.json`
   (the platform's `thomas` and `tim_steudler` fail `/prompt`'s identity gate — escalate instead).
   Reach census done: Slack channel count, Gmail mailbox exists (Marcus Bennett has none),
   Drive root exists (Simon Walker has none), calendar.
2. **Storyline natively spans ≥ 8 services** before injection; injection lifts it to ≥ 10 (extreme; normal: ≥ 6 injected, ≥ 7 carrying weight).
3. **Cohort spine** of 40–150 source-defined records × ≥ 3 per-record surfaces over ≥ 2 services
   (normal: ≥ 10 × ≥ 2), with a written **shortcut audit** naming the bulk call that does not cover
   each surface; every surface serves a declared, incorporated requirement and the output column or
   decision that requirement states (`requirement` + `decides`).
4. **2–4 hidden authorities** in rarely-searched services with decoys elsewhere and
   non-overlapping governance (`Hardness_Mastery.md` §3); every decoy scoped to a different
   lot/team/game/issuer or time-superseded; every authority named by a fragment.
5. **≥ 3 independent chains** with distinct mechanism ids (`Hardness_Mastery.md` enum); traps spread over ≥ 6 requirements.
6. **Every requirement incorporated**: anchors → hub → explicit delegations → amendments; each
   delegation's words quoted verbatim from the delegating record (`delegation_quote`); every
   declared requirement named by an incorporated fragment or anchor — no orphan requirement or
   authority.
7. **Fair outcomes**: each decision point gets the strongest two-reading test (§S8); all fair results remain accepted.
8. **Call budget ≥ 500** necessary calls counting only unconditional rows (plan ~600 for headroom; normal: 60–100), ≥ 10 services, no service > 50% outside the per-record phase; every row carries a necessity reason.
9. **`hardness_gate.py --design` PASS** on the draft manifest, at its `effective_profile`.
10. **`stage_gate.py scenario` PASS** (structure, evidence, persona reach, universe-KB use, self-review, boundary); handoff is blocked until it passes.

## Procedure

### S0 — Assignment and persona reach
- [ ] Copy all eight V3 assignment fields from the shared context. Map `business_function` to the Evals category
      (`Evals/references/rules/task_categories.md`).
- [ ] Persona reach census: `python3 Task_Authoring/tools/persona_view.py reach <persona> --top 10`. Paste the
      output verbatim in section 0; the gate re-runs it and compares the channel and thread counts. Add the
      Linear/GitHub/Trello identities from `python3 Task_Authoring/tools/entity.py resolve <persona name>`
      (`references/Ask_Carriers.md` §1 persona ID map).
- [ ] Competency drives the *kind* of work; pick a remit the persona would plausibly be pulled
      into. Record the remit argument with before-freeze sources and the assigned role. Write `role_reviews.scenario` in `Working_Files/00_V3_Authoring_Evidence.json` (Guide schema), binding the design hash and source IDs.
- [ ] **Effective profile.** Write `horizon` (verbatim) and `effective_profile` into the draft
      manifest. Long Horizon → `extreme`. Normal Horizon → `normal`, unless the requester confirms
      the extreme design: then record that a ≥ 500-call design scores Borderline Horizon (non-fail,
      task score capped at 3) and write `profile_exception: {reason, requester_confirmation}` (who
      confirmed, when, where). Every later gate reads this one value.

### S1 — Storyline
- [ ] Start from `references/Scenario_Atlas.md` (ranked, verified anchors per service, natural
      contradictions, persona reach). Or mine a new one: follow one storyline across services
      (decision in Slack → ticket in Linear → PR in GitHub → spec in Docs → numbers in
      Sheets/Snowflake → partner thread in Gmail → meeting in Calendar).
- [ ] **Universe KB.** Place the storyline on `references/universe_kb/timeline.md` (spine events and beats in
      the window; cite the event dates). Take the cohort from `universe_kb/cohorts.json` and cite its id (e.g.
      `LIN-OPEN-ENG`), its selection rule and count, and drop its `hazards_inside` ids; if none fits, write
      `cohorts.json: no fit — <reason>`. Build traps on `universe_kb/trap_catalog.json` entries and cite their ids
      (e.g. `D01`, `N01`), so each trap has base precedent.
- [ ] **Originality.** Do not reuse the ML-selected example (Combo Fighters launch record), the
      calibration tasks in `Evals/references/rules/hardness_calibration.md` (133-PR residue
      register, RC-flag gate, art-canon handoff control) or their cohorts, numbers, flag
      vocabularies or surface combinations.
- [ ] **Active at the clock.** For every person the design gives a seeded voice or relies on, copy
      `status_at_clock` from the registered source's activity data into section 1b (person · email ·
      status_at_clock · seeding role). Verify status at the assigned freeze; February labels do not establish October activity
      or justify seeding someone after their actual departure. The gate uses the selected source's KB.
- [ ] **Identity traps.** `python3 Task_Authoring/tools/entity.py collisions`, plus `entity.py resolve <name>` for
      every person the task names. Paste the output in section 1c and pin each correct entity against its
      lookalikes (shared first names, token conflicts, lookalike handles).
- [ ] **Coherence audit.** List pre-existing inconsistencies in the data the task will touch.
      The Evals fail Cross-Service Coherence on *any* inconsistency in task-touched data, even
      pre-existing (`1_Prompt_Eval.md` §3.2; QC "fails based on the presence of the inconsistency
      itself"). Avoid defective areas, or make the disagreement a dated human claim that a
      later record overturns — never two system fields that silently disagree.
      - **Scope = everything a correct run opens**, not only what you will seed: the anchors, the
        cohort members, every record on each chain, the queues/channels/folders the asks route
        through, and the records that settle each status (PRs, threads, calendar entries).
      - **Walk the seven QC categories** (`references/Docs/QC_Spec_Doc_Latest.csv`, Universe
        Inconsistency examples) over that scope with `tools/hg.py search` / `records`, one row each:
        temporal (dates in prose vs fields vs clock), semantic (labels/titles vs content, ambiguous
        name overlaps), cross-service referential (same person/figure/date per service; cited
        records exist), quantitative (quoted figures vs source rows), state/lifecycle (status vs
        activity in every service), identifier/format (one scheme per service), other.
      - **Sibling-defect sweep.** For every designed defect (a stale status, a wrong owner, a
        superseded figure), search the base for *other* records with the same kind of defect in the
        same scope. Investigate whether each is an actual coherence defect or another fair result.
        Preserve every fair result in acceptance; repair or exclude actual coherence defects, include them in
        the cohort, or move the design.
      - **Known hazards first.** Walk `references/universe_kb/coherence_hazards.json` (68 measured hazards in 6
        categories, each with example ids) over the scope. Cite each hazard id the scope touches; for a category
        with none, write `<category>: none in scope`. The gate validates every cited id and requires all six
        categories.
      - Record each finding as `record · category · fields · evidence pointer · hazard id · disposition
        (avoid / fold into design / designed claim + overturning record)`.
      - **Hazard resolutions are verified, never declared** (`hazard_acknowledgements[].resolution`):
        `excluded` — the hazard's records are neither modified by the SQL nor cited by the design;
        `repaired` — the SQL fixes the inconsistent fields and `base_check` re-evaluates the hazard on
        the post-SQL state (Linear L01–L07 only; any other hazard type cannot be repaired verifiably,
        so keep it out); `dated_claim` — an attributed, dated text claim a later record overturns,
        never a system field the SQL modifies. An acknowledgement without a verified resolution fails.

### S2 — The cohort spine (A2/A3; ≥ 500 calls)
- [ ] Define the cohort **by a rule** the agent must reconstruct (window × state × label ×
      owner × service), not by a list. Size 40–150.
- [ ] Choose 3–6 per-record surfaces (● carriers under the S8 carrier-eligibility statement — `Ask_Carriers.md` §5 as
      amended by §6b, so Linear comments are ● although `Hardness_Mastery.md` §2.2 still marks them ○). For each, run
      the **shortcut audit**: which bulk call would return this field for all records? If one
      exists (`Ask_Carriers.md` §3), move the evidence or drop the surface.
- [ ] Write the classification predicate: closed vocabulary, whole-word rules, exclusions,
      "NONE stands alone", per-line cutoff; plus a **house rule that overrides the natural
      reading** (A15) and an **effective-date dual regime** (S11) if the storyline supports it.
- [ ] Add **boundary records** (A17): a later-added member, an unticketed lookalike, a stale
      shorter list somewhere authoritative-looking.
- [ ] Estimate per-record calls from `Ask_Carriers.md` §4. If base surfaces give < 4 honest
      calls per record, **seed per-record evidence into the verified no-bulk surfaces** (Linear
      comments per issue, PR conversation comments per PR — `Hardness_Mastery.md` §2.5; Slack
      replies are search-sweepable and never count as per-record volume) under the necessity rule
      (`Hardness_Mastery.md` §2.5): decisive for an unpredictable 15–40 % subset, neutral notes on
      the rest. Record `records` per surface; Σ calls × records ≥ 300.
- [ ] **Short-circuit and sweep audit** (`Hardness_Mastery.md` §2.6 items 1–2): for each surface,
      can a correct run skip it once another surface decides the record? Can one filtered
      search (channel/date/author/label) page through the whole trail? Fix by homing evidence in
      each record's natural container, not a dedicated one, and by tying the surface to a
      **requirement that already needs its value**: the surface's `requirement` is a declared R-id
      carried by an incorporated fragment, and `decides` names the output column or decision that
      requirement's own summary states. Never add an output column only to make a read necessary
      — a column no incorporated requirement asks for is manufactured work (red team A, R1 #7;
      gate check `surface_requirements`). If no requirement needs the surface, drop the surface.
      Write the answer in the surface's `short_circuit` field.
      Per-record facts are **raw events to join** (build id, deploy/flag event, commit ref), never
      the classification in prose (§2.6 item 12).

- [ ] **Mint ids now** (collision-checked with `tools/hg.py search lookup`), not placeholders, so
      the final manifest keeps every draft id; an id that must change later goes into the final
      manifest's `design_delta` with its reason.

### S3 — Hidden authorities (A12)
- [ ] 2–4 authorities: cohort rule · classification rule · destination/format rule ·
      recipient/communication rule. Each named in plain words by the hub or the prompt.
- [ ] Home each in a rarely-searched service (Trello card, Docs handbook, Gmail thread, Calendar
      event, Slides deck, separate Sheet). Place a near-matching **decoy** that differs on a
      decisive clause where Opus looks first (Confluence page, Slack thread), and for at least
      one authority a second, **same-service** decoy with an adjacent scope.
- [ ] Name each authority by **what it governs or who issued it**, and give the decoy the same
      search terms; no self-advertising cues on decoys or superseded versions ("draft", "old",
      a stale month in the title) — `Hardness_Mastery.md` §2.6 items 3–4.
- [ ] **Decoy scope.** A decoy may differ on a decisive clause only where that clause is true for
      **another scope** — a different lot, team, game or issuer (`decoy_scope: {dimension, decoy,
      task}`) — or where the decoy is an **older version** the authority supersedes (an earlier entry
      of a trap's `version_records`). Two live, identically scoped records with contradictory rules
      can fail Cross-Service Coherence (`1_Prompt_Eval.md` §3.2); multiple fair readings alone are allowed. The
      check `decoy_scope` fails a decoy with neither.
- [ ] Prove findability: a natural search for the authority's own name returns it
      (`python3 Task_Authoring/tools/hg.py search search <svc> "<name>"`).
- [ ] `governs` lists must not overlap.

### S4 — Delegation lattice (asks spread across services)
- [ ] 1–3 **anchors** the prompt will name in plain words. Give each anchor's names as **noun
      phrases only** (≤ 6 words, no verb or imperative framing, no second-person request) in an
      `Anchor · Anchor name (noun phrase, ≤ 6 words) · Record` table, and the same phrase as the
      manifest's `prompt_reference`; `stage_gate.py` blocks any other shape (`boundary.anchor_naming`).
- [ ] A **hub** in the owner's voice that explicitly delegates to spokes.
- [ ] **≥ 12 ask fragments** across **≥ 7 services** and **≥ 10 containers** (channels,
      threads, tickets, cards, docs, pages, events, decks, sheets, mail threads). Each carries
      exactly one requirement (rule clause · destination · recipient subset · format · deadline
      · exclusion · reuse instruction).
- [ ] **Amendments** in a different service, later in time, changing one clause (retain the rest).
- [ ] **Non-authoritative instruction distractors** outside the chain (another persona's list,
      a suggestion without authority, the same rule for another title).
- [ ] Fill the incorporation table: fragment → chain back to an anchor → **the record that carries
      the delegating words** (`delegated_by_record`) → **the words themselves, verbatim**
      (`delegation_quote`, an exact substring of that record's text; the gate reads the seeded row or
      the base record through `tools/hg.py`) → the requirements it carries (`requirement_ids`) → the
      authorities its own record names (`names_authorities [{id, quote}]`). A requirement no record
      points to is unauthorized, whatever the manifest says: every declared requirement must be named
      by an incorporated fragment or anchor, and every authority by a fragment (gate checks
      `incorporation_chains`, `requirement_coverage`, `authority_incorporation`).

### S5 — Chains and traps
- [ ] ≥ 3 independent chains (`Hardness_Mastery.md` §4) — one wrong-summary chain (A1), at
      least one rarely-opened-service chain (A13), one reply chain (A14); others from A4–A11,
      A15–A20. Each chain's `root_cause` is the bare mechanism id from the enum in
      `Hardness_Mastery.md` §2.6 ("Mechanism id enum"); chains sharing an id count as one.
- [ ] **Supersession chronology.** List each trap's `version_records` oldest first; the gate reads
      every record's own timestamp from the SQL row or base record and fails any order that is not
      strictly increasing — write the `at` values from the records, not from the plan.
- [ ] Trap list (family · records · requirement · expected wrong reading · resolver ·
      discovery order). ≥ 12 traps, ≥ 7 families, ≥ 6 requirements, ≥ 3 in rarely-opened
      services, ≥ 4 supersessions (≥ 2 cross-service, ≥ 1 with ≥ 3 versions), ≥ 6 distractors.
- [ ] **Failure-diversity plan**: for each chain, which runs plausibly miss it and which
      requirements that touches. No single discovery may gate most requirements.
- [ ] **Trap independence** (§2.6 item 6): a trap counts only if an agent that has defeated all
      the others can still fail it; merge traps that fall to the same rule. No record states a
      chain's conclusion (item 5).

### S6 — Deliverables and writes
- [ ] One register/record (exact totals, checked-absence states) + 3–6 dependent writes over
      ≥ 3 services. Destination and recipients pinned by an authority or the hub.
- [ ] A reuse-vs-create write (A8) where the storyline has an existing record.
- [ ] Every write's content depends on findings (`depends_on`). No bolt-ons.

### S7 — Call budget
- [ ] Table by phase × service (discovery · rules · enumeration · per-record · reconciliation ·
      reads-before-writes · writes/read-back). Total ≥ 500 (plan ~600); ≥ 10 services; max share ≤ 50% outside the per-record phase.
      A row that depends on unverified tool behaviour carries `conditional_on` and **counts 0**:
      the floor that must clear the profile minimum is the unconditional total.
- [ ] Note the golden-run rule: a correct run must also need the volume.

### S8 — QC rails (each item must be answered in the dossier)
- [ ] **Two-reading test** at every decision point (destination, recipient, act-vs-defer,
      inclusion edge): best reading vs strongest alternative, resolved by newer source /
      authority / identity / scope, or explicitly accepted as another fair outcome under V3.
- [ ] **Incorporation**: every graded requirement has a chain to the prompt.
- [ ] **Reach**: every scoped record readable by the persona (Gmail: copy in the persona's
      mailbox; Slack: member; GCal: owner/invitee; Drive family: owner/shared). List every load-bearing
      base record in the **Reach table (load-bearing records)** and prove each with
      `python3 Task_Authoring/tools/persona_view.py can-see <persona> <service> <id>`; the gate re-runs it on every
      scoped id in that table and on any row marked `LB`. Required evidence must be YES. A designed access denial
      or an unverifiable record is a **probe, never load-bearing**: its row says `DENIAL-INTENDED: <reason>` (NO)
      or `UNVERIFIED-OK: <reason>` (UNVERIFIED), carries no `LB`, and lists `alternate_evidence_ids: <ids>` —
      reachable records that are YES and carry the dependency instead; the gate blocks a probe without YES
      alternates. UNVERIFIED never satisfies a required dependency. In the manifest the same probe is a
      `denied_probes` entry, cited only by traps or decoys. Planned seeds are checked at the injection gate.
- [ ] **Feasibility**: required writes exist in `Evals/references/tools/catalog.json` **and can
      produce the required shape** (e.g. tabs on creation); the persona can **edit** every write
      target (owner or shared as writer); external recipients have an authorized access path;
      numeric values observable at the needed precision; output formats native.
- [ ] **Explicit rules** (§2.6 items 7–9): temporal comparison for multi-version evidence, how
      parent/folded records aggregate every status, the build/snapshot a check refers to, what
      "now" means against a future deadline, each write's end state — all in incorporated records;
      every cross-reference postdates the record it refers to.
- [ ] **Precedence (carrier eligibility — one statement for every playbook):** load-bearing facts
      only in ● carriers of `Ask_Carriers.md` §5 **as amended by §6b** (verified tool behaviour, which
      supersedes §5 and `Hardness_Mastery.md` §2.2). §6b verifies that injected **Linear comments render**
      through `linear_list_comments` with no bulk alternative, so Linear comments are a **● load-bearing
      per-record carrier**. Every other ○ entry (GCal description, Slides notes, Contacts description,
      Drive `content_text`, Slack file `content_inline`) holds supporting detail only until §6b verifies it.
- [ ] **Prompt naturalness**: everything the prompt would otherwise enumerate lives in the
      lattice — list what the human's trigger must say (anchors, deadline, deliverable kinds)
      and what it must not (locations, IDs, root cause, contents lists).
- [ ] **Grading devices** (for the human's rubric later): exact cohort multisets, aggregate
      invariants, ≤ 5 spot checks per group + a volume criterion, one criterion per required
      write/recipient.

- [ ] **Coherence rail** (Cross-Service Coherence is a hard fail on presence): every S1 audit row
      dispositioned; every designed disagreement is a dated human claim with a named, later
      overturning record (never two silent fields); every record the plan seeds is planned with its
      companion fields (thread counters, issue/PR `updated_at`, Linear lifecycle stamps, Trello
      badges, Confluence version rows, one GCal copy per attendee calendar, Drive-family sharing
      mirrored) so `base_check.py` will pass; every id in the record plan follows the base scheme
      (`playbooks/01_Universe_Injection.md` S5 table). Companions come from
      `references/universe_kb/integrations.json`: for every service the manifest seeds, cite the `INT-nn`
      integrations that would mirror the record (GitHub app → Slack, linear[bot] → PR, invitation mails …) and
      say what is seeded, or `<service>: none` with the reason.

### S9 — Self-test and red team
- [ ] `python3 Task_Authoring/tools/hardness_gate.py Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.draft.json --design`
      → PASS (the profile comes from the manifest's `effective_profile`).
- [ ] **Lazy-solver pass**: walk the design as an agent that issues one broad search per
      service, reads first hits, never opens threads/replies, stops at the first conclusion,
      and uses every bulk shortcut. Every point it still scores is a leak — fix it.
- [ ] **Literal-value sweep**: search each authority's decisive value (date, count, name, tier
      word) as a literal across every service, including mail subjects, snippets and file
      names. A hit outside the authority is a leak (sample-task: an "Updated invitation" subject
      leaked a calendar-only cut-off).
- [ ] **Wording sweep**: no word of a rule's decisive phrase appears in the evidence that
      decides it (search the rule's key terms across the seeded records).
- [ ] **"The rest stands" check**: for every partial amendment, confirm no later record in the
      chain re-asserts the amended clause.
- [ ] **Self-review (GEN_EXECUTION §6a, validity side)** — written into section 12 under **Self-review**:
      1. Re-read `Evals/1_Prompt_Eval.md` §2.1 (Unique Ground Truth), §2.2 (Feasibility) and §3.2
         (Cross-Service Coherence) and `Evals/0_Injection_Quality_Eval.md` Check C, and walk them in
         order against the design — not from memory.
      2. For each QC coherence category, the strongest counter-reading that the design's touched data
         FAILS (including pre-existing defects and sibling defects from the S1 sweep), with the record
         pointer that resolves it; for each designed disagreement, the best argument that it is an
         unintended inconsistency, and why the dated records support the designed reading.
      3. For each decision point, the two-reading result from S8 restated with its evidence.
      4. Re-read every load-bearing base value through `tools/hg.py` (a value copied from the Atlas or
         a brief is a lead, not evidence).
      5. Paste `hardness_gate.py --design` output verbatim; record anything unresolved by name.
- [ ] **Dual red team (required):**
      `python3 Task_Authoring/tools/redteam_review.py --mode redteam --dual --in Task_Authoring/task_inputs/Working_Files/01_Scenario_Design.md --in Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.draft.json --out Task_Authoring/task_inputs/Working_Files/01b_Redteam_Review.md`
      (two independent reviewers → `01b_Redteam_Review.md` and `01b_Redteam_Review.second.md`). Address every finding of both
      (fix, or rebut with a record pointer) in section 13. If the proxy fails, record
      `RED TEAM UNAVAILABLE: <error line>` in section 13; the gate then warns instead of blocking.
- [ ] **Stage gate (blocking):** `python3 Task_Authoring/tools/stage_gate.py scenario Task_Authoring/task_inputs --paste`.
      Handoff is blocked until it prints `STAGE GATE scenario: PASS`; `--paste` writes that output into the
      Self-review, where `/create-injection`'s gate looks for it (its digests go stale on any later edit).

## `01_Scenario_Design.md` template

Use these headings (the gate looks them up by name; each must be non-empty, and every factual row carries a
record id or pointer):

```
# Scenario Design — <slug> · design only · contains no prompt, OE or criterion text
## 0 Assignment, persona census and horizon note   (persona_view reach output verbatim; effective_profile + any profile_exception)
## 1 Storyline   (anchors per service with ids; timeline, cohorts and trap_catalog ids)
## 1a Coherence audit   (record · category · fields · pointer · hazard id · disposition; sibling-defect sweep)
## 1b Active speakers   (person · email · status_at_clock from activity.json · seeding role)
## 1c Identity traps   (entity.py output verbatim + correct entity vs lookalikes)
## 2 Cohort spine   (rule, size, surfaces, shortcut audit, predicate, house rule, dual regime, boundary records)
## 3 Hidden authorities   (name, home, decoy, governs, findability proof)
## 4 Delegation lattice   (anchors + anchor-name table, hub, fragments, amendments, distractors, incorporation table with verbatim delegation quotes)
## 5 Chains and trap register   (family, records, requirement, wrong reading, resolver, discovery order)
## 6 Failure-diversity plan
## 7 Deliverables and dependent writes
## 8 Service role map   (13 rows: role, load-bearing fact/write, carrier ●/○)
## 9 Call budget   (phase × service)
## 10 QC rails   (### Two-reading table · ### Reach table (load-bearing records) · feasibility, precedence,
                  naturalness constraints, grading devices)
## 11 Record plan for /create-injection   (+ ### Integrations and companions: service · INT id · companion · decision)
## 12 Self-test results   (gate output verbatim, lazy-solver leaks fixed) + ### Self-review
## 13 Red team (dual)   (finding · source file · disposition with evidence)
```

**Self-review** (gate minimum): one evidenced counter-reading per QC coherence category (temporal, semantic,
cross-service referential, quantitative, state/lifecycle, identifier/format, other) plus one per decision point
in the two-reading table, in a table with a "counter-reading" column; the `hardness_gate.py --design` output
verbatim; an `Unresolved:` line.

## Deliver

Run `python3 Task_Authoring/tools/stage_gate.py scenario Task_Authoring/task_inputs --paste`; handoff is blocked
until it prints PASS, and its output sits in the Self-review. Report the storyline, services (natural vs
injected), cohort × surfaces, authorities, chains, budget total, the `hardness_gate` and `stage_gate` verdicts
verbatim and the dual red-team dispositions. Next: `/create-injection`.
