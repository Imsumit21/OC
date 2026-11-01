# 01 — Scenario Design (Playbook) — HarmonyGames · Spec V2 · effective profile (extreme by default)

> Command: `/create-scenario` (`--revise` after a `/create-hardening` MODE B report) · Writes: `task_inputs/Working_Files/01_Scenario_Design.md` + the draft manifest `task_inputs/Working_Files/01_Hardness_Manifest.draft.json` + the gradable surface `task_inputs/Working_Files/01_Gradable_Surface.json` · Checks: `tools/hardness_gate.py --design`, `tools/gradable_surface.py validate`, `tools/redteam_review.py --mode redteam --dual`, **`tools/stage_gate.py scenario` (blocking)**; advisory (UNCALIBRATED): `tools/trap_liveness.py --design`, `tools/hardness_forecast.py forecast --design --preregister` · Next: `/create-injection` · Read first: `setup/GEN_EXECUTION.md`, `references/Hardness_Mastery.md`, `plans/Fold_Hardening_Into_Scenario_And_Injection.md` §4.4

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
assignment fields and the context's registered universe/KB source (`universe.key`, the
`freeze_utc` seed bound, `source.kb_status`). The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is missing — there is no default. Check each relied-on fact at that universe's seed bound; the KB is authoritative data only when `kb_status` is `bound`, otherwise its summaries are leads.
V3 changed-topic rules take
precedence over the older V2 reference documents in `references/Docs/`; local authorship and hardness-profile
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
  It carries `mechanism_portfolio[]` (S5a): one entry per solver rule.
- `task_inputs/Working_Files/01_Gradable_Surface.json` — the fact slots the deliverables make gradable (S6b). This
  stage owns the file; `/create-injection` never rewrites it (it records expected values and `flipped_by` in its
  preflight report instead, so this stage's certificate stays current).

## Hard gates

1. **Persona can carry it.** The persona is one of the 17 in `Evals/references/persona/roster.json`
   (the platform's `thomas` and `tim_steudler` fail `/prompt`'s identity gate — escalate instead).
   Reach census done: Slack channel count, Gmail mailbox exists,
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
11. **Gradable surface valid** (`tools/gradable_surface.py validate`, gate check `surface.valid`): work-kind
    weights, ≤ 5 samples per group plus a volume slot, exception slots only for members an incorporated authority
    singles out, no fact in ≥ 3 slots.
    - Every V3 rubric rule blocks, with its basis printed: structure, weights, duplicates, sampling, exceptions,
      mechanisms. `surface_grader` and the forecast score this surface, so a broken rule would count losses the real
      rubric can't have.
    - The geometry (mechanism share, always-pass share) is reported and never gated.
12. **Red team ran, or an explicit fallback is recorded** (`tool.redteam_dual`, blocking): a tool-error stub such as
    `set REDTEAM_MODEL` is not a review.
13. **Revision intake dispositioned** (`--revise` only; `revise.*`, blocking): every proposed node verdict kept, purged
    or rebuilt, every export bound on evidence to the revision it ran on, or marked `historical`.

Advisory and UNCALIBRATED (each liveness flag still needs a written disposition): liveness flags (S5b) and the prior
forecast (S9b). They inform the design; they never block it.

## Procedure

### S0r — Revision intake (`--revise`; only when a `/create-hardening` MODE B report exists for this task)
`/create-hardening` MODE B owns the forensics (decision 3): it binds each export to the revision it ran on, runs
`tools/trajectory_ledger.py` and `tools/node_verdicts.py` against **that revision's** solver, reviews every call that
touches a node's deciding records, briefs or writes, and appends the results to `support/hardness_ledger/ledger.jsonl`.
This step consumes that output and owns the decisions:
- [ ] Name the verdicts file the intake consumes (`run_forensics/<revision>/node_verdicts.json`) in section 14.
- [ ] **Disposition every proposed verdict** in a table (node · runs · proposed verdict · disposition · evidence):
      `keep`, `purge` (a FALSE or BYPASSED node leaves the design, recorded in `design_delta`) or `rebuild`. Confirm or
      assign CONFOUNDED (tool, fairness, verifier, run) for every flagged candidate — the tools only flag it.
- [ ] Every evidence cell cites a run and an event (`run-3 event 987`); every export stays bound to the revision it
      ran on. Historical evidence never certifies a new revision, and an old export never blocks a repair: mark such
      a run `historical`.
      - Bound means BOUND on evidence in `node_verdicts.json`: a basis (discriminating content, or the sole revision
        with its reason) and seen needles (`revise.revision_binding`). INSUFFICIENT, AMBIGUOUS, UNBOUND and a legacy
        `SINGLE` never certify; such a run was not evaluated, and only a `historical` line lets the intake pass.
      - INSUFFICIENT usually means a revision was not passed: MODE B binds against every stored revision
        (`Working_Files/run_forensics/*/01_Universe_Inject.sql`).
- [ ] Route each finding: verifier defects → `/create-allfail` and `/create-rubric-writing check`; OE defects →
      `/create-oe-writing check`; prompt-side defects → `/create-prompt-writing check`; universe-side changes → S5a
      onward.
- [ ] The Self-review then needs at least (LANDED + LEAKED rows in the intake) + 1 evidenced counter-readings.

### S0 — Assignment and persona reach
- [ ] **Universe first.** Record `universe.key`, `universe.label`, `universe.clock_line`, `freeze_utc` (seed bound) and
      `universe.shutdown_rules_apply` in section 0 before any storyline research. Every candidate, census and count is
      derived in that universe only (`Evals/ENVIRONMENT.md`); no count or id carries across universes.
- [ ] Copy all eight V3 assignment fields from the shared context. Map `business_function` to the Evals category
      (`Evals/references/rules/task_categories.md`).
- [ ] **Loss budget from the mode.** Record the cap and the design target E[average] ≤ cap − 8 points: Easy ≤ 82 %,
      Medium ≤ 77 %, Hard ≤ 62 % (`plans/V3_Opus55_Difficulty_Plan.md` §3). S5a sizes the portfolio to it.
- [ ] **Theme screen.** No bio-adjacent theme (zombies, infection, outbreaks, contamination) in the storyline or the
      seeded text. A safety false positive switched the model in 8 of 12 Season Pass runs, and under V3 any non-Opus-5.5
      run is invalid (`Hardness_Mastery.md` §12).
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
      Sheets/Snowflake → partner thread in Gmail → meeting in Calendar). The Atlas census is 76
      storylines for Feb 14 and 70 for Oct 1 (`Evals/Docs/README.md`); never cite 80.
- [ ] **State at the cut.** Synth-cut excludes the six post-cut storylines (Combo Fighter, Zombie Match Lite, the
      Telegram Domino Delights port, the UI sprite optimization sprint, the Mattel Barbie idle life sim pitch, the web
      distribution partnership) and anything after 2025-09-30 23:59:59 PT; never build a shutdown or wind-down premise
      there. Normal: business as usual after the Feb 11, 2026 shutdown announcement is a false premise unless the
      wind-down is acknowledged. In either universe Victor Barnes cannot review, approve or reply, and no departed or
      terminated person acts after leaving (`Evals/1_Prompt_Eval.md` §2.3; `Evals/ENVIRONMENT.md`).
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
      lookalikes (shared first names, token conflicts, lookalike handles). No second account for an existing
      person (cite a real namesake to keep one), no duplicate-mailbox device, and no trap that depends on a
      malformed ID (`Evals/0_Injection_Quality_Eval.md` Check A; `Evals/references/schema/id_contracts.json`).
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

- [ ] **Coupling seams** (moved from `/create-hardening` MODE A A2): list the under-used couplings between the
      storyline's services — a rule homed in one service that changes a value read in another, a record whose meaning
      depends on another cohort member (A22 hypothesis), an exception the main instructions do not carry (A23
      hypothesis). They are the raw material for S5a.

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
- [ ] **Delegate by role, not by location.**
      - The hub names *what* governs ("the refund policy", "the vendor's latest reply").
      - It never lists every document, link or location.
      - S3's authorities are found by search, not by a hub link.
      - When Season Pass's hub named every source, Opus 4.8 read them all and every rule leaked as a checklist
        (`Hardness_Mastery.md` §12).
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
- [ ] **Seed bound.** Every seeded event timestamp (created, sent, posted, commented, modified,
      `dateLastActivity`, action date) is at or before `freeze_utc`; only plan fields (due, scheduled start/end,
      deadline) may be later, and calling a record "scheduled" does not exempt its event timestamps
      (`Evals/0_Injection_Quality_Eval.md` Check C).
- [ ] Trap list (family · records · requirement · expected wrong reading · resolver ·
      discovery order). ≥ 12 traps, ≥ 7 families, ≥ 6 requirements, ≥ 3 in rarely-opened
      services, ≥ 4 supersessions (≥ 2 cross-service, ≥ 1 with ≥ 3 versions), ≥ 6 distractors.
- [ ] **Failure-diversity plan**: for each chain, which runs plausibly miss it and which
      requirements that touches. No single discovery may gate most requirements.
- [ ] **Trap independence** (§2.6 item 6): a trap counts only if an agent that has defeated all
      the others can still fail it; merge traps that fall to the same rule. No record states a
      chain's conclusion (item 5).
- [ ] **Hardness v2 trap selection** (`Hardness_Mastery.md` §13; Opus 5.5): name at least two of the nine v2 traps
      the design uses, as two separate decisions that each need checking across sources (Part 5 rule 1), ranked by
      cost: a done source with the missing piece in another service (A24, `done_gap`) and a correction somewhere else
      come first. For each, name the convincing wrong source and the record that beats it — who wrote each, when and
      with what authority — and the weight-5 row the miss flips (status, number, inclusion or write).
- [ ] **Corrections off the first-read path.** No correction may sit in the superseded record's container, an
      anchor's container (including replies in the anchor's thread) or the container of a record that delegates to
      the superseded one: Opus 5.5 reads those on the way and settles the trap (v2 Part 2; dd-2024 rev1 T1, T3).
      Put it in a later reply on another item, a page comment, a review or another service, tied to the same item and
      person. Volume and plain arithmetic are not difficulty (v2 Part 4): never count them toward a trap.

### S5a — Mechanism portfolio (the design driver; the S5 counts stay as floors)
- [ ] Generate **10–15 grounded candidates** (moved from `/create-hardening` MODE A A3), each cited to real records:

| # | Anchor storyline (cited) | Coupling (finding → what it changes next) | Characteristic | Discovery-order proof | Reach | Findability term | Gradable fact (a fact, not criterion text) | Services carrying weight | Walk Δ vs tier | Risks |
|---|---|---|---|---|---|---|---|---|---|---|

      Each also carries: its ledger prior with record ids
      (`python3 Task_Authoring/tools/hardness_ledger.py priors --model <assigned baseline model> --family <family>`; priors
      are per model and never pooled; another model's evidence needs a transfer record), the step that stays hard
      **after complete retrieval**, the natural call that returns the deciding record, its incorporation chain, and the
      gradable slots it affects.
- [ ] Select by expected loss and independence (moved from MODE A A4, depth over breadth). Prefer A1/A15/A16/A17/A19:
      a wrong reading at one node that corrupts the next; one authoritative-but-wrong claim met before the evidence that
      overturns it; reading past an apparent conclusion; a deciding fact held only in a structured system; day-level
      data that must be aggregated. Reject, with a reason: independent lookups, bolt-on writes, unreachable or unfindable
      evidence, an unfairly rejected alternative outcome, an unauthorized requirement, a walk pushed outside the tier.
      Also reject what leaked on Season Pass (`Hardness_Mastery.md` §9, §12):
      - rules listed in a hub-named document;
      - a plain-words pointer to the deciding record, in a record every run reads;
      - a list whose membership rule is stated explicitly;
      - a claim contradicted by per-item records the agent reads anyway.
- [ ] **Size the portfolio to the S0 budget: the target, not the cap.**
      - Use at least 3 independent loss channels on separate outputs; Hard needs at least 4. A channel is a designed
        mechanism or a declared complexity channel (a cohort's exact derived values, a dependency chain, delegated
        synthesis). No unit of discovery may decide more than half the weight (`playbooks/09_Rubric_Writing.md`
        gate 12), so Hard's at-risk weight needs at least two independent cohorts or chains.
      - **Budget arithmetic.** With weight W at risk, failing at a weighted mean rate p̄, and the rest passing at r
        (0.95 unless measured), E[average] = r(1 − W) + (1 − p̄)W. Hard's 62 % target needs W ≥ 73 % at p̄ = 0.5
        (76 % at r = 1). Two-thirds of the weight at p̄ = 0.5 gives 66.7 % (65.0 % at r = 95 %): it clears the 70 %
        cap but misses the 62 % target by 4.7 points with a perfect remainder, or 3.0 with a 95 % remainder: that
        is the whole margin.
      - **Spread.** Near-certain rows lower the mean but add no spread. The gate reads the population SD of the six
        runs. For six independent normal runs, a design σ of 0.10 lands in 0.10–0.30 only about 30 % of the time
        (normal approximation), and σ alone does not determine the six-run SD: mixtures and correlated channels can
        pass or fail at the same σ. Compute the six-run SD distribution from the forecast's joint outcome model on
        the actual rubric rows, with covariance — channels can be dependent, or each flip several rows at once.
        An interior σ around 0.15–0.20 is a model-motivated candidate, not a validated requirement; equal independent
        channels at p̄ = 0.5 illustrate it (W_v ≈ 0.32√k), but never transfer a channel count. Read the forecast's
        P(SD in band) and P(patterns) (at least 2 patterns, the largest at most 50 %). Run an attainable-variance
        check on the legal rubric before fixing a target: if the work can only earn weight-1 rows, the variance may be
        out of reach, and then change the work or the scenario, never the weights.
      - **Scale rows.** Only aggregate rows (a volume row, a derived total) compound over a cohort; a sampled member
        fails at about the per-member rate e. Independent members give 1 − (1 − e)^N; shared causes (one rule, source
        or format) give less, and opposing count errors can cancel. Use the forecast's per-slot P(fail) (F1).
        Evidence: the A2 PR residue register, 133 PRs, averaged 70.2 % with 0/6 runs right on its two derived totals
        (`Hardness_Mastery.md` §0, A2; model unstated).
      - **All-fail rows.** A row that fails all six runs is legal when VALID, with a step-14 justification
        (`playbooks/11_AllFail_Analysis.md`); the forecast reports each slot's P(fails all six) as that workload.
        A predicted all-fail is different: a value the persona can't reach, which blocks at any count (09 gate 11).
      - **Populations are workload, not rows:** at most 5 samples per group, a volume row, and direct rows for
        singled-out exceptions.
      - Expected loss is Σ weight × failure rate over the mechanisms and complexity channels, plus slips. It must
        reach the budget (`plans/V3_Opus55_Difficulty_Plan.md` §3).
      - **Landing rates.** Use Opus 5.5 ledger priors (calibration battery, `source: probe`) where they exist. Otherwise
        use Opus 4.8 priors, transferred at quarter weight and halved, labelled TRANSFERRED · UNCALIBRATED.
      - A design that misses the budget is redesigned before any SQL, never built.
- [ ] Per selected node, one line on the four A5b checks: **incorporated** (the chain from a named anchor); **survives
      complete retrieval** (a node that is hard only because nobody searches is a call multiplier, not the engine);
      **tool-surface proof** (the decisive record is returned by the natural call — a node that lands only because a
      search misses, a result spills or an endpoint errors is CONFOUNDED by design); **graded weight** (the S6b slots
      it can flip). Retrieval traps, decoys and authorities every run reaches leak (`Hardness_Mastery.md:98`); put the
      difficulty in the judgment that remains after the correct target is found.
- [ ] **Never resolve a liveness flag by removing an incorporation or UGT link.**
- [ ] **Solver rules.** One rule per mechanism node, each with an explicit natural-reading fallback, written as the
      draft manifest's `mechanism_portfolio` (`references/Hardness_Manifest_Spec.md`): `id` = the future rule id in
      `Working_Files/solver/solver.py`, `mechanism`, `prior_family` with its `prior_family_reason` (the ledger family
      whose prior the forecast uses, and why it applies), `nodes`, `requirement`, `natural_reading`, `decides`,
      `source`, `signature`. `/create-injection` S4b writes the solver itself (`tools/oracle_kit.py` contract).

### S5b — Design liveness flags (advisory, UNCALIBRATED)
- [ ] `python3 Task_Authoring/tools/trap_liveness.py --design --task-dir Task_Authoring/task_inputs` (plan §7.3):
      breadcrumb collision, self-advertising decoy, order (the correction sits in the hub thread), rule placement. No
      SQL exists yet, so only the manifest-structure flags can fire; injection S5c re-runs it on the SQL.
- [ ] Write a disposition for every flag in section 5. Lexical warnings, not proof: redesign the difficulty, never
      remove a fairness link.
- [ ] `python3 -B Task_Authoring/tools/hardness_v2_check.py --design --task-dir Task_Authoring/task_inputs` (Hardness
      v2 Part 7 self-checks: SAME_PLACE, DONE_CHECK, TWO_DECISIONS, DECISION_FLIP, INPUT_CHECK, FILTER_CHECK,
      RULE_IN_PROMPT). Without SQL, records that only the overlay can place report UNRESOLVED; injection re-runs it on
      the SQL. Write a disposition for every FLAG and UNRESOLVED in section 5; a FLAG is answered by moving evidence or
      changing the work, never by raising a weight (`09_Rubric_Writing.md` gate 8).

### S6 — Deliverables and writes
- [ ] One register/record (exact totals, checked-absence states) + 3–6 dependent writes over
      ≥ 3 services. Destination and recipients pinned by an authority or the hub.
- [ ] A reuse-vs-create write (A8) where the storyline has an existing record.
- [ ] Every write's content depends on findings (`depends_on`). No bolt-ons.

### S6b — Gradable surface (`Working_Files/01_Gradable_Surface.json`)
- [ ] Write the fact slots the deliverables make gradable, before any rubric exists (`tools/gradable_surface.py`
      docstring for the shape): each slot's selector, weight by kind of work (lookup 1; interpretation, calculation,
      comparison, limited reconciliation 3; multi-source reconciliation, deeper reasoning, cross-modal, tracing 5) with
      a `work_reason`, class (direct · aggregate · write_content · delivery), role (sample · exception · volume ·
      core) and the mechanisms that can flip it.
- [ ] Validate it against the V3 rubric rules:
      `python3 Task_Authoring/tools/gradable_surface.py validate --task-dir Task_Authoring/task_inputs` → PASS
      (work-kind weights; ≤ 5 samples per group plus a volume slot; exception slots only for members an incorporated
      authority singles out — `singled_out_by`; no fact in ≥ 3 slots). The mechanism share is reported, never gated.
- [ ] Geometry needs room: the slots the designed mechanisms can flip must carry more than 1 − cap of the weight
      (`/create-injection` S5b′ proves it with the solver). Delivery slots fail only at a base rate and never count.
- [ ] OE coverage: plan an OE step that reaches every slot. A row no step reaches is `oe_unmapped` and returns as
      ROW_DEFECT, OE_GAP or UNRESOLVED (`Evals/3_Rubrics_Eval.md` OE cross-reference).

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
      One reading unless a single reported figure forks and meets all five BOTH_FAIR_FIGURE checks (same
      decision, writes and destinations; both values on persona-visible primary records; no newer source,
      authority, identity or scope settles it; every ask completed; next action unchanged) — then record
      `Rubric must accept: X or Y`. Prefer values whose PT and UTC days agree; avoid anonymized tokens as
      deciding values without a persona-visible mapping (`Evals/1_Prompt_Eval.md` §2.1).
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
      Every deciding fact also sits on a record reachable from a prompt noun, readable as content, outside Gmail
      Trash/Spam. Never only inside a Gmail or Slack attachment (metadata only; Trello serves bytes for 42 of 106);
      an unreferenced deciding comment needs a seeded link from a record the prompt gives a reason to open
      (`Evals/3_Rubrics_Eval.md` reachability).
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
      and what it must not (locations, IDs, root cause, contents lists). The sketch names a destination the
      persona would know; a hidden destination is an explicit discovery ask backed by a persona-visible record that
      names each place. No trap hint or riddle, no audit-form wording, and per-case rules are seeded authority
      records, not prompt if-chains (`Evals/1_Prompt_Eval.md` §2.7).
- [ ] **Grading devices** (for the human's rubric later): exact cohort multisets, aggregate
      invariants, ≤ 5 spot checks per group + a volume criterion, one criterion per required
      write/recipient.
      No decoy or exclusion that only a `leaves X as found / open / unchanged` row could grade: each exclusion is an
      exact count or scope on a required write, or a requirement inside a required artifact. This is how a v2 trap 9
      (A25, work someone already did) and v2's "guard row" are graded here: "creates charge records for exactly 17 of
      the 20 receipts", never "leaves the first two alone" (`Hardness_Mastery.md` §10). No graded count, format
      or line limit the prompt will not state (`Evals/3_Rubrics_Eval.md` Negative Criteria, Overly Specific).

- [ ] **Coherence rail** (Cross-Service Coherence is a hard fail on presence): every S1 audit row
      dispositioned; every designed disagreement is a dated human claim with a named, later
      overturning record (never two silent fields); every record the plan seeds is planned with its
      companion fields (thread counters, issue/PR `updated_at`, Linear lifecycle stamps, Trello
      badges, Confluence version rows, one GCal copy per attendee calendar, Drive-family sharing
      mirrored) so `base_check.py` will pass; every claim the plan makes about a base artifact (a git
      branch a ticket was picked onto, a build, a release, a PR) agrees with the base: pick notes name a branch
      that `git branch --contains` shows holding the ticket's commits, dated inside the branch's window from
      `#builds` and git (`tools/base_claims.py`, blocking at injection); traps that need a branch git does not
      show (backed-out picks, re-picks) go on tickets with no commit naming them; every id in the record plan follows the base scheme
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
      (fix, or rebut with a record pointer) in section 13. `REDTEAM_*` is a precondition: a reviews file that only holds
      the tool's error (`set REDTEAM_MODEL or pass --model`, an HTTP error) is not a review. If the proxy cannot run,
      record `RED TEAM UNAVAILABLE: <error line>` **and** an explicit fallback,
      `RED TEAM FALLBACK: <who reviewed the design instead, how, and why>`, in section 13. Without one of the two the
      gate blocks (`tool.redteam_dual`): no silent skip.
- [ ] **S9b Prior forecast (advisory, UNCALIBRATED, pre-registered):**
      `python3 Task_Authoring/tools/hardness_forecast.py forecast --design --task-dir Task_Authoring/task_inputs --model <baseline model> --mechanisms <portfolio ids> --preregister`
      (the surface's declared `mechanisms` stand in for the solver). Paste the ledger id (`hev_…`) and the reported
      P(all gates) range in section 12. It informs S5a; it never blocks.
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
## 12 Self-test results   (gate output verbatim, lazy-solver leaks fixed; gradable_surface validate; S9b forecast id) + ### Self-review
## 13 Red team (dual)   (finding · source file · disposition with evidence; or RED TEAM FALLBACK)
## 14 Revision intake (S0r)   (--revise only: verdicts file · node · runs · proposed verdict · disposition · run-N event M)
```
Section 5 also carries `### Mechanism portfolio (S5a)` and `### Liveness flags (S5b)` with a disposition per flag.
Section 0 also records the universe key, label, clock line, seed bound and `shutdown_rules_apply`.

**Self-review** (gate minimum): one evidenced counter-reading per QC coherence category (temporal, semantic,
cross-service referential, quantitative, state/lifecycle, identifier/format, other) plus one per decision point
in the two-reading table, in a table with a "counter-reading" column; the `hardness_gate.py --design` output
verbatim; an `Unresolved:` line. Under `--revise` the minimum rises to (LANDED + LEAKED rows in section 14) + 1.

## Deliver

Run `python3 Task_Authoring/tools/stage_gate.py scenario Task_Authoring/task_inputs --paste`; handoff is blocked
until it prints PASS, and its output sits in the Self-review. Report the storyline, services (natural vs
injected), cohort × surfaces, authorities, chains, the mechanism portfolio with each prior's record ids, the
gradable surface's mechanism share (reported, not gated), budget total, the `hardness_gate` and `stage_gate` verdicts
verbatim, the dual red-team dispositions (or the recorded fallback) and the pre-registered forecast id, labelled
UNCALIBRATED. Next: `/create-injection`.
