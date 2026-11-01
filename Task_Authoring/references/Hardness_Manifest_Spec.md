# Hardness Manifest — `task_inputs/Working_Files/01_Hardness_Manifest.draft.json` → `01_Hardness_Manifest.json`

Before designing or implementing a manifest, run
`python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`
and use `Working_Files/00_Task_Context.json`. The exact eight-field assignment,
assigned role, canonical freeze, difficulty mode/cap and shared data source are
bound across stages. The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is missing — there is no default.
Compiled from the older Feb 14 export; reference-only for both universes until re-verified against the selected universe. Lines tagged [normal-only] do not exist on Oct 1 (synth-cut).
The freeze (`freeze_utc`) is the seed bound: it scopes relied-on facts and seeded
event timestamps; only plan fields (due, scheduled start/end, deadline) may be
later. Later-edited bodies need dated versions or
independent before-freeze evidence to establish earlier state. V3 rules govern fair
outcomes, prompt style, source evidence and empirical difficulty.

**Preserved local policy:** Long Horizon still maps to `extreme` (≥500 necessary
calls and all existing targets); Normal retains its current limits/exceptions.
Easy/Medium/Hard does not choose or relax the design profile. The corrected empirical
average must still be strictly below its assigned 90%/85%/70% cap.

The machine-checkable declaration of a task's difficulty design. `/create-scenario` writes the
**draft** `01_Hardness_Manifest.draft.json`; `/create-injection` writes the **final**
`01_Hardness_Manifest.json` once the SQL exists, keeping every draft id or recording the change in
`design_delta` (`stage_gate.py injection` → `structure.design_delta`). `tools/hardness_gate.py` checks
the final manifest **against the SQL itself** (every seeded id cited here must literally appear in
`01_Universe_Inject.sql`; every injected schema must be used by the design; delegation quotes and
supersession timestamps are read from the records).

```sh
python3 Task_Authoring/tools/hardness_gate.py Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.draft.json --design
python3 Task_Authoring/tools/hardness_gate.py \
    Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.json \
    Task_Authoring/task_inputs/01_Universe_Inject.sql
```

**The profile is a task property, not a flag.** The gate reads `effective_profile` from the
manifest; `--profile` is only a cross-check and FAILs (`effective_profile`) when it disagrees.
The gate's `PROFILES` table (`tools/hardness_gate.py`) is the single source of the numbers;
this page and `GEN_EXECUTION.md` §3a restate them. A manifest that passes the gate is necessary, not sufficient: the gate checks structure and
quantities; the dossier, `/injection`, `/prompt`, the red team and — finally — the
Opus pre-check decide whether the difficulty is real.

## Fields

| Field | Shape | Meaning |
|---|---|---|
| `assignment_context` | `{context_hash, assignment_hash, policy_hash, freeze_utc, difficulty_mode}` | required V3 binding copied from `Working_Files/00_Task_Context.json`; draft and final must match the same current assignment/context. Never choose a mode/cap or clock separately in the manifest |
| `persona` | string | roster `persona_key` (must be one of the 17 in `Evals/references/persona/roster.json`). Gate check `persona_reach` runs `persona_view.py check-sql` for this persona: every seeded id cited by `ask_fragments`, `authorities` (incl. decoys), `traps` (any `*seeded_ids`, seeded `version_records`), `chains` (hop records that are SQL row keys) and `cohort.evidence_surfaces[].seeded_ids` must be YES — NO or UNVERIFIED fails, except a declared `denied_probes` record |
| `denied_probes` | `[{record, reason, alternate_evidence_ids[]}]` | designed access denials (an `acl_alternate` trap). A denied probe is **never load-bearing**: `persona_reach` accepts its NO only if the record is cited solely by `traps` or as a decoy (never by a fragment, authority record, chain or cohort surface), `reason` is set, and every `alternate_evidence_ids` record is YES for the persona (the alternates carry the dependency). UNVERIFIED never satisfies a dependency — there is no UNVERIFIED exception |
| `horizon` | `"Normal Horizon"` \| `"Long Horizon"` | the assigned tier, verbatim |
| `effective_profile` | `"extreme"` \| `"normal"` | **required**, resolved once at scenario time; every gate reads it. Long Horizon → `extreme`; Normal Horizon → `normal`, or `extreme` only with `profile_exception` |
| `profile_exception` | `{reason, requester_confirmation}` | required when a Normal Horizon task uses `extreme` (Borderline Horizon, score capped at 3): why, and the requester's confirmation (who, when, where recorded) |
| `volume_exception` | `{reason, requester_confirmation, call_budget_floor, per_record_floor}` | optional, `extreme` only: a requester-confirmed lower volume floor for one task. `reason` and `requester_confirmation` are nonblank strings; it replaces exactly two numeric minima — `call_budget` (`call_budget_floor`, integer 100–500; 100 is the platform's Long Horizon minimum) and `per_record_calls` (`per_record_floor`, integer 0–300); every other extreme target and the necessity reason on every budget row still apply. Present but null, partial, mistyped (bool, float, string number) or out of range FAILs `effective_profile` and leaves both minima at 500/300 |
| `design_delta` | `[{id, change, reason}]` | final manifest only: every draft id the final manifest drops or renames, with the reason (the injection gate fails a missing draft id without one) |
| `services` | `{svc: {role, weight_reason}}` | every service that carries weight; `weight_reason` = the fact/rule/write the answer cannot do without. Keys: `slack gmail gcal gdrive gdocs gsheets gslides contacts github linear trello confluence snowflake` |
| `requirements` | `{R-id: one-line summary}` (or `[{id, summary}]`) | every graded requirement; every `trap.requirement`, `authority.governs`, `chain.ends_in` and surface `requirement` must be declared here. The summary states the output columns/decisions a cohort surface may serve (`decides`) |
| `anchors` | `[{id, prompt_reference, service, locator, requirement_ids?[]}]` | 1–3 sources the prompt names in plain words. `prompt_reference` is a **noun phrase of ≤ 6 words** — no verb or imperative framing, no second-person request (the stage gates block it). `requirement_ids` = requirements the anchor itself carries |
| `ask_fragments` | `[{id, service, container, locator, kind, incorporated_via[], seeded_ids[], base_pointers[], delegated_by_record, delegation_quote, requirement_ids[], names_authorities?[{id, quote}], supersedes?, resolver?}]` | every requirement-bearing record. `kind`: `delegation` · `requirement` · `amendment` · `destination` · `recipient` · `format` · `exclusion`. `incorporated_via` is the explicit chain from an anchor to this fragment (e.g. `["A1","K3"]` = A1 delegates to K3, which delegates to this one); the gate follows each fragment's last link back to an anchor and rejects cycles. `delegated_by_record` (required) = the id/pointer of the record **in which the delegator's words point to this fragment** — one of the immediate delegator's own records (`seeded_ids`, `base_pointers` or the anchor's `locator`). `delegation_quote` (required) = those words, an **exact substring of that record's text**, read from the seeded SQL row or from the base record through `tools/hg.py` (Slack `C…/ts`, Linear key, `mailbox/<id>`, or `<service>:<file> <json pointer>`); a quote the record does not contain fails `incorporation_chains`. `requirement_ids` = the requirements this fragment carries: every declared requirement must be named by ≥ 1 incorporated fragment or anchor (`requirement_coverage`; an orphan requirement fails). `names_authorities` = the authorities this fragment's own record names, each with the exact naming `quote` (`authority_incorporation`: every authority must be named by a fragment's record, or be the very record an incorporated fragment delegates to — an orphan authority fails) |
| `authorities` | `[{id, name, home_service, decoy_service, governs[], findable_query, seeded_ids[], base_pointers[], decoy_seeded_ids[], decoy_base_pointers[], decoy_scope?}]` | hidden governing sources (A12): named by a fragment (`names_authorities`), homed in a rarely-searched service, with a near-matching decoy where Opus looks first and (for ≥ 1 authority) a same-service decoy; `governs` lists the requirement ids it controls — **no overlap between authorities**. Every decoy declares `decoy_scope: {dimension: lot\|team\|game\|issuer, decoy, task}` (the decoy's differing clause is true for another scope) **or** each decoy record is an older entry of a trap's `version_records` (time-ordered supersession). A same-scope contradiction is two live answers: it fails Cross-Service Coherence (`1_Prompt_Eval.md` §3.2) and Unique Ground Truth (§2.1) — gate check `decoy_scope` |
| `cohort` | `{definition_source, key, size, evidence_surfaces[{service, tool, per_record_calls, records?, seeded?, seeded_ids?[], why_no_bulk, short_circuit, requirement, decides}]}` | the spine (A2). `records` = how many cohort records the surface applies to (default `size`); `per_record_calls` may be fractional. `why_no_bulk` must name the bulk call that does *not* return the field. Seeded surfaces follow the necessity rule (`Hardness_Mastery.md` §2.5). `short_circuit` (required for extreme) = why a correct run cannot skip this surface once the others decide the record, and why one filtered search cannot sweep it (§2.6). `requirement` = the declared R-id the surface serves, carried by an incorporated fragment; `decides` = the output column or decision that requirement's summary states (verbatim words of the summary). An output column added only to make a read "necessary" is manufactured work (red team A, R1 #7) — gate check `surface_requirements` |
| `chains` | `[{id, root_cause, hops[{service, record, finding}], ends_in}]` | ≥ 3 independent forensic chains, each ending in a graded fact. `root_cause` is a **mechanism id** from the enum in `Hardness_Mastery.md` (§2.6, "Mechanism id enum": `A1`–`A21`, `2.6.1`–`2.6.14`, plus the library hypotheses `A22` cross-shard dependency and `A23` brief-transmission loss); distinct root causes = distinct ids (two chains with the same id count once) |
| `traps` | `[{id, family, distractor_type?, services[], seeded_ids[], base_pointers[], requirement, expected_wrong_reading, resolver, discovery_order?, version_records?}]` | every designed difficulty; `family` from the list below; `requirement` = the requirement it can make a run fail (spread them); `discovery_order` = why the wrong item is met first. `superseding` / `effective_date` traps need `version_records: [{service, id \| base_pointer, seeded: bool, at}]` (≥ 2, oldest first) — "cross-service" and "≥ 3 versions" are counted from these records, not from `services`. Gate check `supersession_chronology` reads each record's **own** timestamp (SQL: Slack `ts`, Gmail `date`, Linear/GitHub/Confluence `created_at`, review `submitted_at`, Trello id time / action `date`, GCal `updated`, Drive-family `modified_time`; base records through `tools/hg.py`) and requires them strictly increasing in the listed order; `at` is a declaration only. The last entry is the governing (newest) version |
| `call_budget` | `[{phase, service, calls, reason, conditional_on?}]` | necessary calls by phase × service; every row needs a `reason` (why each call answers a distinct necessary question — the Evals anti-inflation check). A row with `conditional_on` (an unverified tool behaviour it depends on) **counts 0** toward the profile minimum until verified: the blocking `call_budget` check uses the unconditional floor and reports both totals. Floor ≥ 500 for the extreme profile, plan ~600 |
| `writes` | `[{service, tool, count, depends_on[], requirements[]?}]` | dependent writes; `depends_on` = chain/trap/fragment ids whose findings decide the content; `requirements` = the R-ids the write satisfies |
| `facts` | `[{key, value, kind, aliases?[], must_appear_in?[], forbidden_variants?[], home_ids?[], version_records?[]}]` | the fact sheet `tools/fact_check.py --no-leak` holds the SQL text to (gate check `fact_consistency`, no-leak always on). `kind`: `amount` · `date` · `count` · `name` · `status` · `id` · `version`. Wherever `key` or an alias is mentioned, a value of that kind in the same sentence/line must equal `value` (`$11.7K` = `11,700`; a date with a timezone is compared in UTC); a `name` may not appear in a near-spelling; `forbidden_variants` may appear nowhere; each `must_appear_in` record id (SQL row id, Slack `C/ts`, Gmail thread, sheet, deck) must state `value`. Records listed in `traps[].version_records` (all but the newest) are exempt — they are the superseded versions. **No-leak:** `home_ids` = the per-record carrier rows of a per-record fact; its value in any other seeded text row (outside `home_ids`, `must_appear_in` and the fact's own `version_records`) is a `fact_leak` error — above all in bulk-readable rows (Slack messages, Linear issue descriptions, Sheets cells, Confluence bodies), where one call returns the per-record answer |
| `integration_exceptions` | `[{record_id, reason}]` | seeded records that deliberately lack an integration companion (`base_check`): a meeting with no invitation mails (`reason: "no_notify: …"`), a PR without its linear[bot] comment, a GitHub event without its Slack mirror. `record_id` = the event id / `ical_uid`, the PR id, or the comment/review id |
| `hazard_acknowledgements` | `[{hazard_id, resolution, why_safe, requirement?}]` | pre-existing inconsistencies (`references/universe_kb/coherence_hazards.json`) the task touches. Every state/lifecycle (`L…`) or cross-service referential (`R…`) hazard among task-touched records — SQL-updated, referenced by seeded rows or text, or cited by the manifest — needs an entry with a **verified** `resolution`, or gate check `hazard_scope` fails. An acknowledgement alone never changes a verdict (red team A, R1 #4). `resolution`: `excluded` = the hazard's records are neither modified by the SQL nor cited by the design (only neighbouring seeded rows touch them); `repaired` = the SQL fixes the inconsistent fields and `base_check` re-evaluates the hazard predicate on the post-SQL state (supported: Linear L01–L07; any other hazard type FAILs as unverifiable, and a predicate that still holds FAILs); `dated_claim` = the disagreement is an attributed, dated **text** claim a later record overturns — never a system field the SQL modifies. A hazard record the SQL modifies is a `base_check` FAIL unless `repaired` is verified. `why_safe` = how the task incorporates it; `requirement` (optional) must be a declared R-id |
| `mechanism_portfolio` | `[{id, mechanism, prior_family, prior_family_reason, nodes[], requirement, natural_reading, decides?[], source?, signature?, prior?{alpha, beta, record_ids[]}}]` | the designed mechanisms (`/create-scenario` S5a), **one entry per solver rule**: `id` = the rule id in `Working_Files/solver/solver.py` (`tools/oracle_kit.py` checks rules ↔ entries one-to-one); `mechanism` from the enum (`A22`/`A23` are hypotheses); `nodes` = the trap / chain ids the rule implements; `natural_reading` = the fallback the rule's ablation computes; `prior_family` = the ledger family its prior comes from (`tools/hardness_ledger.py priors`; `family` is the legacy spelling) and `prior_family_reason` = why that family's evidence applies to this rule (same mechanism id, or the closest library family and what differs); `source` = rules sharing a source share a per-run latent in the forecast; `signature` = the words a subagent brief must carry for the rule to reach a worker. Gate check `mechanism_portfolio`: unique ids, enum mechanisms, existing nodes, requirement, natural reading, prior family and its reason present. Optional for legacy manifests |
| `gradable_surface` | `path` or `{path, digest?}` | `Working_Files/01_Gradable_Surface.json` (scenario S6b; `tools/gradable_surface.py`), relative to this manifest's folder |
| `solver` | `{path, digest}` | the solver (`solver/solver.py`) and its sha256; `oracle_kit.py check` compares the digest with the file (`contract.digest`) |
| `preflight` | `{report, digest}` | `01c_Preflight_Report.json` (`tools/preflight_report.py`, injection S4b–S5e) and its sha256. Gate check `artifact_fields` (all three fields): relative paths and 64-hex digests; `stage_gate.py injection` verifies the files themselves |

**Trap families:** `superseding` · `distractor` · `tool_surface` · `scope_alias` ·
`stale_summary` · `reuse_exclusion` · `effective_date` · `authority` · `pagination` ·
`exact_predicate` · `acl_alternate` · `friction` · `synthesis_omission` ·
`eliminating_evidence` · `conclusion_stop` · `entity_collision` · `unit_or_timezone` ·
`cross_reference_gap` · `near_miss_mention` (a record names the rule/value but is not the governing one) · `mutable_pointer` (a pointer to an artifact that changed after the pointer was written) · `done_gap` (Hardness v2 trap 1, mechanism A24: one source says an item is done, another service shows a required piece missing) · `completion_elsewhere` (Hardness v2 trap 9, mechanism A25: the item looks open but a record in another place shows it already done; grade it as an exact count or scope on the required write, never a "leaves X alone" row).

**Version-record containers (optional, Hardness v2).** `traps[].version_records[].container` overrides the container
`tools/hardness_v2_check.py` derives for a record (`slack:<channel>/<thread root ts>`, `gmail:<thread id>`,
`file:<drive file id>`, `gcal:<ical uid or event id>`, `trello:<card id>`, `linear:<issue>`, `github:<repo>#<pr>`,
`confluence:<page id>`, `snowflake:<table>`). Declare it when a base record holds a version and the SQL overlay cannot
place it; otherwise the check reports UNRESOLVED. No gate reads the field; `chains[].root_cause` and
`mechanism_portfolio[].mechanism` also accept `A24` and `A25` (`Hardness_Mastery.md` §13).

**Distractor types:** `lookalike_entity` · `near_duplicate_record` ·
`non_authoritative_instruction` · `stale_summary` · `partial_listing` · `keyword_collision` ·
`scope_adjacent` · `already_done` · `withdrawn_ask` · `other_title`.

## Extreme-profile thresholds (`hardness_gate.py`)

| Check | Threshold |
|---|---|
| SQL lint | clean (`tools/sql_lint.py`) |
| Services injected / carrying weight | ≥ 10 / ≥ 10 |
| SQL rows | ≥ 120 INSERTed rows (UPDATE companions do not count) |
| Effective profile | `effective_profile` set; Long Horizon = extreme; Normal Horizon at extreme only with `profile_exception`; `--profile` agrees; a complete `volume_exception` lowers only the call-budget and per-record minima |
| Requirements | all referenced R-ids declared; ≥ 6 declared; every declared requirement named by an incorporated fragment or anchor (`requirement_coverage`) |
| Orphan injection | none (every injected schema appears in `services`) |
| Anchors | 1–3, each with a plain-language `prompt_reference` |
| Ask fragments | ≥ 12, over ≥ 7 services and ≥ 10 containers, every chain ends at an anchor; each `delegation_quote` is in its `delegated_by_record`'s text |
| Hidden authorities | ≥ 2, homed in gmail/gsheets/trello/snowflake/gslides/gcal/gdocs, a decoy **record** (`decoy_seeded_ids` / `decoy_base_pointers`), non-overlapping `governs`; ≥ 1 authority's decoy in the **same** service (adjacent scope); every authority named by a fragment (`authority_incorporation`); every decoy scoped or superseded (`decoy_scope`) |
| Cohort | ≥ 40 records × ≥ 3 surfaces over ≥ 2 services; Σ per_record_calls × records ≥ 300; every surface's `requirement` declared + incorporated and its `decides` stated by it (`surface_requirements`) |
| Call budget | unconditional floor ≥ 500 (plan ~600; `conditional_on` rows count 0), every row with a reason, ≥ 10 services, no service > 50% **outside the per-record phase** (at scale only Linear comments are honestly per-record, so the spine concentrates there) |
| Traps | ≥ 12 in ≥ 7 families, hitting ≥ 6 distinct requirements, each with records + resolver + expected wrong reading |
| Rarely-opened evidence | ≥ 3 traps in gmail/gsheets/trello/snowflake/gslides/gcal |
| Supersession | ≥ 4, each with `version_records`; ≥ 2 whose versions span ≥ 2 services; ≥ 1 with ≥ 3 versions; the records' own timestamps strictly increasing (`supersession_chronology`) |
| Seeded ids | every id in `seeded_ids`, `decoy_seeded_ids` and seeded `version_records` appears in the SQL as an exact token outside comments |
| Distractors | ≥ 6 of ≥ 4 types |
| Discovery-order proofs | ≥ 4 |
| Independent chains | ≥ 3 with distinct mechanism ids (`Hardness_Mastery.md` enum), ≥ 3 hops over ≥ 2 services |
| Writes | ≥ 4 over ≥ 3 services, each depending on findings |

The `normal` profile is for a **Normal Horizon** assignment, where the golden run must stay
inside 50–100 calls: budget 60–100 necessary calls, ≥ 7 services carrying weight, ≥ 6 injected,
≥ 50 rows, cohort ≥ 10 × 2 surfaces, ≥ 7 fragments over ≥ 5 services, ≥ 1 hidden authority,
≥ 2 chains, ≥ 8 traps in ≥ 5 families. Difficulty there comes from authorities, chains and
traps, not volume. The profile is the manifest's `effective_profile`: a Long Horizon task at
`normal` fails `effective_profile` (Wrong Horizon); a Normal Horizon task at `extreme` (Borderline
Horizon, score capped at 3) passes only with `profile_exception {reason, requester_confirmation}`.
Every gate — `hardness_gate`, `stage_gate` scenario / injection / prompt-check — reads the same value.

## Minimal example (shape only — not a task)

```json
{
  "persona": "julia_lawson",
  "assignment_context": {"context_hash": "<current context_hash>", "assignment_hash": "<current assignment_hash>", "policy_hash": "<current policy_hash>", "freeze_utc": "2026-02-14T00:00:00Z", "difficulty_mode": "medium"},
  "horizon": "Long Horizon",
  "effective_profile": "extreme",
  "requirements": {"R2": "release-readiness class per record", "R3": "register destination", "R5": "build carried by the release"},
  "services": {"trello": {"role": "hidden cohort rule", "weight_reason": "membership rule for the cohort"}},
  "anchors": [{"id": "A1", "prompt_reference": "robert's wind-down list", "service": "gdocs", "locator": "gdocs:f_<id>",
               "requirement_ids": ["R3"]}],
  "ask_fragments": [{"id": "K1", "service": "gdocs", "container": "f_<doc>", "locator": "section 2", "kind": "delegation",
                     "incorporated_via": ["A1"], "seeded_ids": ["f_<doc>"], "delegated_by_record": "gdocs:f_<id>",
                     "delegation_quote": "<the delegating words, verbatim from the anchor record>",
                     "requirement_ids": ["R2", "R5"],
                     "names_authorities": [{"id": "H1", "quote": "<the words naming the release-readiness control>"}]}],
  "authorities": [{"id": "H1", "name": "the release-readiness control", "home_service": "trello", "decoy_service": "confluence",
                   "governs": ["R2", "R3"], "findable_query": "release readiness control", "seeded_ids": ["<card id>"],
                   "decoy_base_pointers": ["confluence:page_<slug>"],
                   "decoy_scope": {"dimension": "game", "decoy": "Match3D", "task": "Game of Dominoes"}}],
  "cohort": {"definition_source": "H1", "key": "PR id", "size": 64,
             "evidence_surfaces": [{"service": "linear", "tool": "linear_list_comments", "per_record_calls": 1, "records": 64, "seeded": true,
                                    "why_no_bulk": "no bulk comment listing; list_issues returns no comments",
                                    "short_circuit": "the comment's finding is its own column in the register for every issue; no other surface decides it",
                                    "requirement": "R2", "decides": "release-readiness class"}]},
  "chains": [{"id": "C1", "root_cause": "A1", "ends_in": "R5",
              "hops": [{"service": "slack", "record": "<ts>", "finding": "claim"}, {"service": "snowflake", "record": "<table>", "finding": "rows contradict"}]}],
  "traps": [{"id": "T1", "family": "superseding", "services": ["gmail", "slack"], "seeded_ids": ["<msg id>"], "requirement": "R5",
             "expected_wrong_reading": "carries the 1.0.56 build", "resolver": "later Gmail from the publisher", "discovery_order": "Slack summary is found by the first search",
             "version_records": [{"service": "slack", "base_pointer": "<channel>/<ts>", "seeded": false},
                                 {"service": "gmail", "id": "<msg id>", "seeded": true},
                                 {"service": "gmail", "id": "<msg id 2>", "seeded": true}]}],
  "call_budget": [{"phase": "per-record", "service": "linear", "calls": 64, "reason": "each issue's triage comments decide its tier for ~30% of issues; no bulk comment call"}],
  "writes": [{"service": "linear", "tool": "linear_update_issue", "count": 3, "depends_on": ["C1", "T1"]}]
}
```
