# R_A: `/create-scenario` Artifact Contract (machine-verified)

Scope: exact shapes demanded by `hardness_gate.py --design`, `gradable_surface.py validate|gradeable-report`,
and `stage_gate.py scenario --paste`, plus `trap_liveness.py --design` and `hardness_forecast.py forecast --design --preregister`.
Evidence: source read with line numbers + one completed exemplar (`task_inputsH`).

## 1. hardness_gate --design check table

Command (docstring l.14; Spec l.29): `python3 Task_Authoring/tools/hardness_gate.py <draft.json> --design [--json]`.
`evaluate()` at `tools/hardness_gate.py:288`. Profile resolution: `resolve_profile` l.178–198; thresholds:
`PROFILES["extreme"]` l.83–90 (`services_weight 10, services_injected 10, rows 120, anchors_max 3, fragments 12,
fragment_services 7, fragment_containers 10, cohort 40, surfaces 3, surface_services 2, per_record_calls 300,
budget 500, budget_services 10, budget_max_share 0.50, traps 12, trap_families 7, trap_requirements 6,
supersessions 4, supersession_cross_service 2, supersession_3_versions 1, distractors 6, distractor_types 4,
writes 4, write_services 3, shifts 4, chains 3, chain_hops 3, authorities 2, rare_traps 3`).

`--design` skipping (`evaluate` l.296–303): `sql_only = {sql_lint_clean, services_injected, rows,
no_orphan_injection, seeded_ids_exist_in_sql, base_consistency, persona_reach, fact_consistency, hazard_scope,
supersession_chronology}` — each appended as `ok=True, detail="skipped (--design: no SQL yet)"`. Everything else runs
for real. Two further design behaviours: `in_sql()` returns True for every token when `design` (l.324–325), so the
"id not in SQL" branches of `hidden_authorities` and `seeded_ids_exist_in_sql` can never fire; and
`RecordText.contains()` returns `(None, "design mode: seeded records are checked once the SQL exists")` for any ref
with no seeded row (l.855–863) — and with empty SQL there are **no** seeded rows.

| # | check id (code order) | extreme requirement | runs in `--design`? | manifest keys read |
|---|---|---|---|---|
| 1 | `assignment_context` (l.305–312) | only runs when `runtime_context.TASK_CONTEXT` is loaded; then `assignment_context` must equal current `context_hash, assignment_hash, policy_hash, freeze_utc, difficulty_mode` | YES (gated when context loaded) | `assignment_context{5 keys}` |
| 2 | `effective_profile` (l.313; `resolve_profile` l.178) | `effective_profile ∈ {extreme,normal}`; `horizon ∈ {"Normal Horizon","Long Horizon"}` verbatim; Long→extreme; Normal+extreme needs `profile_exception{reason, requester_confirmation}`; `--profile` must agree; a malformed `volume_exception` fails here | YES | `effective_profile`, `horizon`, `profile_exception`, `volume_exception` |
| 3 | `sql_lint_clean` (l.327) | 0 lint errors | **skipped** | — (SQL) |
| 4 | `base_consistency` (l.333/340) | base_check PASS | **skipped** | `integration_exceptions`, `hazard_acknowledgements` |
| 5 | `services_injected` (l.341) | ≥ 10 injected schemas | **skipped** | `services` keys vs SQL |
| 6 | `rows` (l.344) | ≥ 120 INSERTed rows | **skipped** | — |
| 7 | `services_carrying_weight` (l.349) | ≥ 10 services whose value has a nonblank `weight_reason` | YES | `services{svc:{role,weight_reason}}` |
| 8 | `no_orphan_injection` (l.352) | every injected schema present in `services` | **skipped** | `services` |
| 9 | `seeded_ids_exist_in_sql` (l.363) | every id in `ask_fragments[].seeded_ids/decoy_seeded_ids`, `traps[].seeded_ids/decoy_seeded_ids`, `authorities[].seeded_ids/decoy_seeded_ids` and seeded `version_records[].id` appears as an exact token outside `--` comments; also **fails if zero ids are cited** (`cited and not missing`) | **skipped** | `ask_fragments/authorities/traps` `*seeded_ids`, `version_records` |
| 10 | `anchors` (l.367) | 1 ≤ count ≤ 3, each with nonblank `prompt_reference` (≤6 words enforced later by stage_gate `boundary.anchor_naming`) | YES | `anchors[{id,prompt_reference}]` |
| 11 | `ask_fragments` (l.374) | ≥ 12 fragments | YES | `ask_fragments` |
| 12 | `ask_fragment_services` (l.375) | ≥ 7 distinct `service` | YES | `ask_fragments[].service` |
| 13 | `ask_fragment_containers` (l.377) | ≥ 10 distinct nonblank `container` | YES | `ask_fragments[].container` |
| 14 | `incorporation_chains` (l.447) | per fragment: no self-link, every `incorporated_via` link is an anchor id or fragment id, last link chain reaches an anchor (cycle/unknown ⇒ broken), has `seeded_ids` or `base_pointers`, `delegated_by_record` present **and ∈ parent's `seeded_ids ∪ base_pointers ∪ {locator}`**, `delegation_quote` nonblank and an exact substring of that record's text (deferred in design for planned seeds, real for base records); every `requirement_ids` entry declared; every `names_authorities[].id` known + has a `quote` found in the fragment's own record (deferred in design) | YES | `anchors[].seeded_ids/base_pointers/locator`, `ask_fragments[*]`, `requirements` |
| 15 | `requirement_coverage` (l.456) | every declared requirement id appears in some **incorporated** fragment's or anchor's `requirement_ids`; zero orphans | YES | `requirements`, `ask_fragments`, `anchors` |
| 16 | `authority_incorporation` (l.466) | each authority id is named by a fragment's `names_authorities` (quote verified) **or** the authority's own record set intersects an incorporated fragment's record set; no unknown authority ids | YES | `authorities[].seeded_ids/base_pointers`, `ask_fragments[].names_authorities` |
| 17 | `cohort_size` (l.477) | `cohort.size` ≥ 40 | YES | `cohort.size` |
| 18 | `evidence_surfaces` (l.479) | ≥ 3 surfaces over ≥ 2 services; every surface has `why_no_bulk`; at extreme (`cohort ≥ 40`) every surface also has `short_circuit` | YES | `cohort.evidence_surfaces[]` |
| 19 | `surface_requirements` (l.498) | every surface's `requirement` is declared **and** carried by an incorporated fragment, and `decides` (normalised, lowercased) is a substring of that requirement's summary; ≥ 1 surface | YES | `cohort.evidence_surfaces[].requirement/decides`, `requirements` |
| 20 | `per_record_calls` (l.501) | Σ `per_record_calls × records` (records defaults to `size`) ≥ 300 | YES | `cohort.evidence_surfaces[].per_record_calls/records`, `cohort.size` |
| 21 | `call_budget` (l.521) | Σ `calls` rows **without** `conditional_on` ≥ 500 (or `volume_exception.call_budget_floor`); no `budget_cap` at extreme; every row has a nonblank `reason` | YES | `call_budget[{phase,service,calls,reason,conditional_on?}]`, `volume_exception` |
| 22 | `call_budget_spread` (l.525) | ≥ 10 services with >0 calls **and** the largest per-service share of calls **outside `phase == "per-record"`** ≤ 50% | YES | `call_budget[].phase/service/calls` |
| 23 | `traps` (l.536) | ≥ 12 traps, ≥ 7 distinct `family`, every family ∈ `TRAP_FAMILIES` (l.103–107, 21 members) | YES | `traps[].family` |
| 24 | `trap_independence` (l.538) | ≥ 6 distinct nonblank `traps[].requirement` | YES | `traps[].requirement` |
| 25 | `trap_completeness` (l.540) | each trap has `seeded_ids` or `base_pointers`, a `resolver`, an `expected_wrong_reading` | YES | `traps[]` |
| 26 | `supersession` (l.559) | ≥ 4 traps of family `superseding`\|`effective_date`; ≥ 2 of them with `version_records` spanning ≥ 2 services; ≥ 1 with ≥ 3 versions; every such trap needs ≥ 2 records each with `service` + (`id`\|`base_pointer`) and parseable `at` (ISO), non-decreasing oldest-first | YES | `traps[].version_records[{service,id,base_pointer,seeded,at,container?}]` |
| 27 | `supersession_chronology` (l.585) | the records' **own** timestamps read from SQL/base (per `TABLE_TIME`, l.694–702) strictly increasing in listed order | **skipped** | `traps[].version_records` |
| 28 | `distractors` (l.591) | ≥ 6 traps with `family: "distractor"`, ≥ 4 distinct `distractor_type` from `DISTRACTOR_TYPES` | YES | `traps[].distractor_type` |
| 29 | `discovery_order_proofs` (l.595) — this is what **"shifts"** means | `PROFILES["extreme"]["shifts"] = 4`: ≥ 4 traps carry a nonblank `discovery_order` (the proof of *why the wrong item is met first* — the reading-order shift, not a service list) | YES | `traps[].discovery_order` |
| 30 | `independent_chains` (l.604) | ≥ 3 chains; ≥ 3 **distinct** `root_cause` values, each in `MECHANISM_IDS` (`A1`–`A25` + `2.6.1`–`2.6.14`, l.120); each ≥ 3 hops over ≥ 2 services; each has `ends_in` | YES | `chains[{id,root_cause,hops[],ends_in}]` |
| 31 | `mechanism_portfolio` (l.251, fn l.218) | if present: non-empty list, unique `id`, `mechanism ∈ MECHANISM_IDS`, nonempty `nodes` all being trap/chain ids, `requirement`, `natural_reading`, `prior_family` (or legacy `family`), `prior_family_reason` | YES (**optional**: absent ⇒ PASS "legacy manifest") | `mechanism_portfolio[]` |
| 32 | `artifact_fields` (l.283, fn l.258) | optional: `gradable_surface` (path string or `{path,digest?}`), `solver{path,digest}`, `preflight{report,digest}`; paths relative (no leading `/`, no `..`), digests 64-hex sha256 | YES (optional) | `gradable_surface`, `solver`, `preflight` |
| 33 | `hidden_authorities` (l.623) | ≥ 2 authorities; each `home_service ∈ AUTHORITY_HOMES = rarely-opened ∪ {gdocs}` (gmail,gsheets,trello,snowflake,gslides,gcal,gdocs); has `decoy_service`, `governs`, `findable_query`, records (`seeded_ids`\|`base_pointers`) and a decoy **record** (`decoy_seeded_ids`\|`decoy_base_pointers`); `governs` lists must not overlap across authorities; ≥ 1 authority with `decoy_service == home_service` (a same-service decoy) | YES | `authorities[]` |
| 34 | `decoy_scope` (l.640) | each authority's decoy either declares `decoy_scope{dimension ∈ {lot,team,game,issuer}, decoy, task}` with `decoy != task` (normalised) **or** all its `decoy_seeded_ids/decoy_base_pointers` appear as non-last entries of some trap's `version_records` | YES | `authorities[].decoy_scope`, `traps[].version_records` |
| 35 | `rarely_opened_evidence` (l.645) | ≥ 3 traps whose `services` intersect `RARELY_OPENED = {gmail,gsheets,trello,snowflake,gslides,gcal}` (l.109) | YES | `traps[].services` |
| 36 | `requirements` (l.655) | ≥ 6 declared requirements; nothing referenced (trap.requirement, authority.governs, chain.ends_in, writes[].requirements) may be undeclared. The `uncovered` list is **reported in the detail only and does not gate** — but `requirement_coverage` (#15) does gate orphans | YES | `requirements`, `traps`, `authorities`, `chains`, `writes` |
| 37 | `writes` (l.660) | ≥ 4 writes over ≥ 3 distinct services, each with nonempty `depends_on` | YES | `writes[{service,tool,count,depends_on,requirements?}]` |

Verdict is `PASS` only when no check has `ok == false` (l.679–682). Notes are informational (l.664–677).

**How planned (not-yet-seeded) ids are written.** Nothing needs a `planned` flag: `--design` short-circuits every
membership test (`in_sql` ⇒ True, l.325) and defers quote/timestamp reads. Consequences you must respect now:
(i) the ids you write must be the ids you will later seed, verbatim, because the final gate is exact-token;
(ii) do **not** use a base pointer (`base_pointers`) for a record you intend to create in SQL — that path is
**really read from base data even in `--design`** and a missing base record makes `contains()` return `False`, failing
`incorporation_chains` / `authority_incorporation`; (iii) `version_records` still need a parseable `at` in design
(`_ordered`, l.544 — `datetime.fromisoformat`, `Z` allowed) since `supersession` runs; only the *real* timestamp
comparison (`supersession_chronology`) is deferred.
**How `delegation_quote` is verified in `--design`:** `RecordText.contains` (l.855–869) first looks for a seeded row —
there are none with empty SQL — then `if self.design: return None, "design mode: seeded records are checked once the
SQL exists"`; the caller only records a break on `found is False` (l.427–429). So for a **planned seed** the quote is
accepted unseen (an IOU repaid at the injection gate, when the real row text must contain it verbatim, whitespace-
normalised). If `delegated_by_record` is instead a **base pointer** the quote is fully verified now.

## 2. Manifest skeleton

Adapted from `Task_Authoring/task_inputsH/Working_Files/01_Hardness_Manifest.draft.json` (top-level keys, in order:
`assignment_context, persona, horizon, effective_profile, volume_exception, requirements, services, anchors,
ask_fragments, authorities, cohort, chains, traps, call_budget, writes, mechanism_portfolio, gradable_surface`). The
final `…Manifest.json` in that folder adds `design_delta, facts, hazard_acknowledgements, integration_exceptions,
solver`. Field meanings: `references/Hardness_Manifest_Spec.md` l.44–70.

```json
{
  "assignment_context": {"context_hash": "<from 00_Task_Context.json>", "assignment_hash": "<…>",
                         "policy_hash": "<…>", "freeze_utc": "2025-10-01T00:00:00Z", "difficulty_mode": "hard"},
  "persona": "claire_morgan",
  "horizon": "Long Horizon",
  "effective_profile": "extreme",
  "volume_exception": {"reason": "<why the real necessary volume is below 500 / 300>",
                       "requester_confirmation": "<who, when, where>",
                       "call_budget_floor": 100, "per_record_floor": 43},
  "profile_exception": {"reason": "…", "requester_confirmation": "…"},

  "requirements": {"R1": "<one line, states the output column/decision a surface may serve>", "R2": "…", "R3": "…",
                   "R4": "…", "R5": "…", "R6": "…"},
  "services": {"slack": {"role": "…", "weight_reason": "the fact/rule/write the answer cannot do without"},
               "gmail": {"role": "…", "weight_reason": "…"}},

  "anchors": [{"id": "A1", "prompt_reference": "Julia's object hand-off request", "service": "slack",
               "locator": "C08R8CHB0QL/1759272000.167533",
               "seeded_ids": ["C08R8CHB0QL/1759272000.167533"], "container": "slack:C08R8CHB0QL/1759272000.167533",
               "requirement_ids": ["R10"]}],

  "ask_fragments": [{"id": "K1", "service": "gdocs", "container": "file:f_da218fea555af2d7ea40f3",
                     "locator": "f_da218fea555af2d7ea40f3", "kind": "requirement",
                     "incorporated_via": ["A1"], "seeded_ids": ["f_da218fea555af2d7ea40f3"], "base_pointers": [],
                     "delegated_by_record": "C08R8CHB0QL/1759272000.167533",
                     "delegation_quote": "my October levels plan",
                     "requirement_ids": ["R1"],
                     "names_authorities": [{"id": "H1", "quote": "every object on your roster"}]}],

  "authorities": [{"id": "H1", "name": "Julia's October levels object plan", "home_service": "gdocs",
                   "decoy_service": "gdocs", "governs": ["R1", "R2", "R3"],
                   "findable_query": "October levels",
                   "seeded_ids": ["f_da218fea555af2d7ea40f3"],
                   "base_pointers": [], "decoy_seeded_ids": ["f_1265318f45054aaef57a4a"], "decoy_base_pointers": [],
                   "decoy_scope": {"dimension": "lot", "decoy": "September level batch (levels 165-275)",
                                   "task": "October level batch (levels 276 onward)"}}],

  "cohort": {"definition_source": "K1", "key": "object", "size": 56, "members": ["Bed", "Wardrobe"],
             "evidence_surfaces": [{"service": "github", "tool": "github_get_pull_request_reviews",
                                    "per_record_calls": 1.0, "records": 12, "seeded": true,
                                    "seeded_ids": ["harmonygames-Games/match3d#431#rev_1"],
                                    "why_no_bulk": "reviews come per PR only; no list call returns them",
                                    "short_circuit": "why a correct run cannot skip this surface once others decide",
                                    "requirement": "R4", "decides": "Call column"}]},

  "chains": [{"id": "CH1", "root_cause": "A24", "ends_in": "R3",
              "hops": [{"service": "slack", "record": "C08R8CHB0QL/1757614800.772141", "finding": "…"},
                       {"service": "github", "record": "harmonygames-Games/match3d#431", "finding": "…"},
                       {"service": "gdocs", "record": "f_da218fea555af2d7ea40f3", "finding": "…"}]}],

  "traps": [{"id": "T1", "family": "done_gap", "distractor_type": "lookalike_entity",
             "services": ["slack", "github", "gdocs"],
             "seeded_ids": ["C08R8CHB0QL/1757614800.772141"], "base_pointers": ["harmonygames-Games/match3d#431"],
             "requirement": "R3", "expected_wrong_reading": "…", "resolver": "…",
             "discovery_order": "why the wrong item is met first",
             "version_records": [{"service": "github", "id": "harmonygames-Games/match3d#431#rev_1", "seeded": true,
                                  "at": "2025-09-16T23:30:00Z", "container": "github:harmonygames-Games/match3d#431"},
                                 {"service": "slack", "id": "D0506EUNTPB/1758907200.825728", "seeded": true,
                                  "at": "2025-09-26T17:20:00Z", "container": "slack:D0506EUNTPB"}]}],

  "call_budget": [{"phase": "discovery", "service": "slack", "calls": 2, "reason": "…"},
                  {"phase": "per-record", "service": "github", "calls": 12, "reason": "…"},
                  {"phase": "rules", "service": "gmail", "calls": 2, "reason": "…", "conditional_on": "…"}],
  "writes": [{"service": "gsheets", "tool": "gsheets_values_update", "count": 1,
              "depends_on": ["R_DONE_MISSING", "K1"], "requirements": ["R1", "R9"]}],

  "mechanism_portfolio": [{"id": "R_DONE_MISSING", "mechanism": "A24", "prior_family": "A24",
                           "prior_family_reason": "same mechanism id; ledger record …",
                           "nodes": ["T1", "CH1"], "requirement": "R3",
                           "natural_reading": "merged + done note = ready",
                           "decides": ["call column"], "source": "corn-dog",
                           "signature": "promised-colour-missing", "controls": ["Chocolate Bar"],
                           "over_application": "over:every-object-missing-a-colour"}],

  "denied_probes": [{"record": "<id the persona cannot see>", "reason": "…",
                     "alternate_evidence_ids": ["<id that IS visible and carries the dependency>"]}],
  "facts": [{"key": "store release ticket", "value": "ZOM-570", "kind": "id", "must_appear_in": ["…"],
             "aliases": [], "forbidden_variants": [], "home_ids": [], "version_records": []}],
  "integration_exceptions": [{"record_id": "9d72b77776d730fafe2e5df5bf96d358@hg4", "reason": "no_notify: …"}],
  "hazard_acknowledgements": [{"hazard_id": "L05", "resolution": "dated_claim", "requirement": "R1",
                               "why_safe": "…"}],
  "gradable_surface": {"path": "01_Gradable_Surface.json"},
  "solver": {"path": "solver/solver.py", "digest": "<64 hex>"},
  "preflight": {"report": "01c_Preflight_Report.json", "digest": "<64 hex>"},
  "design_delta": [{"id": "T1", "change": "renamed to T1a", "reason": "…"}]
}
```

Notes that the code enforces beyond the Spec's prose:
- `requirements` may be a dict (id → summary) or a list of `{id, summary}` (`_declared`, l.201–211). A summary that
  omits the surface's `decides` text fails `surface_requirements` (substring test, lowercased, l.496).
- `anchors[].seeded_ids` / `base_pointers` are optional for the gate but are what makes a child fragment's
  `delegated_by_record` legal (parent's `seeded_ids ∪ base_pointers ∪ {locator}`, l.417). `locator` alone suffices.
- Extra keys are tolerated everywhere (`cohort.members`, `anchors[].container`, `traps[].discovery_order`,
  `mechanism_portfolio[].controls/over_application/signature/source`) — nothing validates them, but
  `hardness_forecast`/`trap_liveness` do read some (see §5).
- `writes[].depends_on` values in the exemplar mix mechanism rule ids (`R_DONE_MISSING`) with fragment ids (`K1`) —
  `writes` only requires the list to be non-empty; nothing checks the referents.
- **Planned ids**: write the literal id you will INSERT (a Slack `channel/ts`, a Gmail `<mailbox>/<thread-id>`, a
  `f_…`/`evt_…` Drive id, a `linear:KEY`, a `github:repo#N#rev_1|c_2|rc_1`). Do not wrap them in a `planned` object;
  `--design` passes them through (`in_sql` True) and the injection gate later demands exact tokens. Put the *record
  that will contain* a quote in `seeded_ids`, never in `base_pointers` unless it really exists in the base universe.

## 3. Gradable surface skeleton

Owner docstring `tools/gradable_surface.py:2–41`. Commands: `validate [SURFACE] [--task-dir DIR] [--manifest M]
[--solver S] [--json]` and `gradeable-report [SURFACE] [--task-dir DIR] [--out F] [--json]` (l.1405–1416, 1434–1454).
Top-level keys used by `validate`/`gradeable`: `kind` (must be `"GRADABLE_SURFACE"`), `version` (**int `1`**),
`task`, `revision`, `sql_sha256` (optional), `classes`, `truth_fields {class, groups}`, `truth_keys` (optional but see
`register_keys_exact` below), `deliverables`, `slots`.

```json
{
  "kind": "GRADABLE_SURFACE", "version": 1, "task": "claire-zm3d-october-object-handoff", "revision": "r1",
  "classes": ["OCTOBER", "NOVEMBER", "REWORK", "CUT"],
  "truth_fields": {"class": "call", "groups": "groups"},
  "truth_keys": ["<optional>", "<explicit expected key set>"],
  "deliverables": {
    "register": {"kind": "table", "name_regex": "(?:october)", "key_column": "object",
                 "key_regex": "[A-Za-z][A-Za-z &'-]{1,40}", "columns": ["object", "PR", "call", "rework ticket", "notes"],
                 "class_column": "call", "reason_column": "notes",
                 "comparators": {"call": "norm", "PR": "pr_number", "rework ticket": "issue_key"},
                 "missing_values": ["", "-", "n/a"]},
    "tickets": {"kind": "json_text", "tool": "linear_create_issue"},
    "reuse":   {"kind": "json_text", "tool": "linear_update_issue"},
    "slack":   {"kind": "json_text", "tool": "slack_send_message"}
  },
  "slots": [
    {"id": "S01", "title": "Corn Dog call", "weight": 5, "work_kind": "multi_source_reconciliation",
     "work_reason": "…why this kind of work…", "class": "direct", "role": "exception",
     "selector": ["field", "Corn Dog", "call"], "fact_id": "corndog.call", "group": "exception",
     "mechanisms": ["R_DONE_MISSING"], "singled_out_by": "H1"},
    {"id": "T02", "title": "A new rework ticket for the lollipops", "weight": 5,
     "work_kind": "multi_source_reconciliation", "work_reason": "…", "class": "write_content", "role": "exception",
     "selector": ["text", "tickets", "lol+i?pops?"], "fact_id": "lollipops.ticket", "group": "tickets",
     "mechanisms": ["R_WITHDRAWN"], "singled_out_by": "H2"},
    {"id": "V01", "title": "Register covers exactly the roster plus #460's ten new objects", "weight": 3,
     "work_kind": "limited_reconciliation", "work_reason": "…", "class": "delivery", "role": "volume",
     "selector": ["delivery", "register_keys_exact"], "fact_id": "register.keys",
     "mechanisms": ["R_SCOPE_ROSTER"], "volume_for": ["open", "batch", "exception"]},
    {"id": "D02", "title": "Reply in Julia's #zombie-art thread", "weight": 1, "work_kind": "lookup",
     "work_reason": "delivery into the named thread is a direct check", "class": "delivery", "role": "core",
     "selector": ["delivery", "slack_thread", "1759272000.167533"], "fact_id": "reply.thread"}
  ]
}
```

**Slot fields** (`l.101–136` docstring): `id` (unique, non-empty), `title`, `weight` ∈ {1,3,5} **exactly** the band of
`work_kind` (`WORK_BANDS`, l.104: lookup 1; interpretation/calculation/comparison/limited_reconciliation 3;
multi_source_reconciliation/deeper_reasoning/cross_modal/tracing 5), `work_reason` non-blank, `class` ∈
`("direct","aggregate","write_content","delivery")` (l.105), `role` ∈ `("sample","exception","volume","core")`
(l.106), `selector` (list), `fact_id?`, `group?`, `volume_for?`, `singled_out_by?`, `mechanisms?[]`, `flipped_by?`,
`incorporating_span?`, `accepted_outcomes?`, `gradable?` (false ⇒ UNGRADED, still needs rubric coverage),
`expected_keys?`, `decides?`. `role(slot)` defaults to `sample` for a 3-arg `field` selector, else `core` (l.216);
`slot_group` defaults to `f"{table}:{column}"` for a `field` selector (l.205).

**Selector vocabulary** (`SELECTORS`, l.107–110 — value = number of required arguments):
`field key column` (2) · `total class` (1) · `printed_total class` (1) · `group_count group` (1) · `group_size group` (1)
· `group_key key group` (2) · `groups_of key` (1) · `sole_reason key group` (2) · `reason_matches key regex` (2) ·
`tracker_lists heading_regex key` (2) · `tracker_count heading_regex n` (2) · `tracker_entry regex value_patterns[]` (3)
· `text deliverable regex` (2) · `link deliverable` (1) · `delivery check ...` (1, with per-check extra args in
`DELIVERY_CHECKS`, l.112–116: `share_reader 0, slide_updated 0, slack_after_email 0, register_is_csv 0,
register_keys_exact 0, tracker_state 1, tracker_preserves 1, email_reply 1, slack_thread 1, register_parent 1,
slack_channel_post 2, trello_card 2`).
Class ↔ selector coupling is not enforced but is the convention (`SELECTOR_CLASS`, l.1136–1140):
field/group_key/groups_of/sole_reason/reason_matches → direct; total/printed_total/group_count/group_size/
tracker_lists/tracker_count → aggregate; tracker_entry/text → write_content; link/delivery → delivery.

**Validate rules** (`validate`, l.979–1121; every FAIL blocks `surface.valid`):
| family | rule (line) |
|---|---|
| `structure.kind` | `kind == "GRADABLE_SURFACE"` and `version == 1` (981) |
| `structure.deliverable` | each deliverable a dict with `kind ∈ {table,text,json_text,calls}`; a `table` needs `key_column`, `key_regex`, `columns` (984–990) |
| `structure.comparator` | every `comparators` value ∈ `("issue_key","pr_number","sha_prefix","yes_no","norm")` (991–994) |
| `structure.slots` | at least one slot (997) |
| `structure.slot_ids` | ids present and unique (999–1002) |
| `structure.selector` | known kind; enough args; `delivery` check known + enough args; `text`/`link` target is a declared deliverable or one of `slide, tracker, email, slack`; `field` key must match **some** table's `key_regex` and the column must be in that table's `columns`; `total`/`printed_total` class must be in `classes`; `reason_matches`/`text` regex must compile; `tracker_entry` needs a non-empty list of compiling patterns (1004–1045) |
| `weights.band` | `weight ∈ {1,3,5}` and `== WORK_BANDS[work_kind]` (1046–1052) |
| `weights.work_kind` | `work_kind ∈ WORK_BANDS` (1049) |
| `weights.reason` | `work_reason` non-blank (1053) |
| `structure.class` / `structure.role` | in `CLASSES` / `ROLES` (1055–1058) |
| `gradeable.slot` | each slot must survive a **dry run through the real grader decoder** (`gradeable`, l.914; structurally: `slack_thread` arg must be a `\d{10}\.\d{6}` ts; `tracker_state` arg must not look like a Trello id; `register_keys_exact` needs `truth_keys`/`expected_keys` unless `role == "volume"`; group/tracker slots need `truth_fields.groups` to name a **field** that is not a table column) (858–938) |
| `duplicates.fact` | the same `fact_id` (else JSON of the selector) in **≥ 3** slots fails (1064–1070) |
| `sampling.limit` | ≤ 5 `role: "sample"` rows per group (`SAMPLE_LIMIT`, 1093–1096) |
| `sampling.volume` | every sampled group has a `role: "volume"` slot whose `volume_for` contains it (or `prefix:*`) (1097–1099) |
| `exceptions.singled_out_by` | every `role: "exception"` slot names a `singled_out_by` that, when a manifest is supplied, is an authority / ask_fragment / anchor **id of that manifest** (1081–1092) |
| `mechanisms.known` | with `--solver` or a manifest `mechanism_portfolio`, every `mechanisms[]` entry must be a real rule/portfolio id (1100–1106) |
| `gradeable.truth` | only with `--truth`; a truth row's group field must be a list (962–976) |

Report (never gated, l.1107–1119): `slots, total_weight, weight_by_class, mechanism_weight, mechanism_share,
always_pass_share_if_no_mechanism_lands, ungraded_slots, groups`. `gradeable-report` prints
`SURFACE.GRADEABLE PASS · N slot(s) · {'GRADABLE': N}` (l.1445–1448) — the exact pair
`GRADABLE SURFACE (…): PASS · 21 slots · weight 85 · mechanism share 91.8% …` and `SURFACE.GRADEABLE PASS · 21
slot(s) · {'GRADABLE': 21}` is what the exemplar pastes into its self-review (task_inputsH `01_Scenario_Design.md`
l.670–671).

**Examples from task_inputsH** (21 slots: 16 direct, 3 write_content, 2 delivery; roles: 15 exception, 4 sample,
1 volume, 1 core — it has **no `aggregate` slot**; the shape above for `aggregate` is the vocabulary's own, e.g.
`{"id":"A01","weight":3,"work_kind":"interpretation","class":"aggregate","role":"volume",
"selector":["total","REWORK"],"volume_for":["batch:*"],"fact_id":"total.rework"}`):
- direct / exception: `S01` `["field","Corn Dog","call"]` w5, `mechanisms:["R_DONE_MISSING"]`, `singled_out_by:"H1"`.
- direct / sample: `S10` `["field","Rocking Chair","call"]` w3 `interpretation`, `group:"open"` (`S13` is the
  `group:"batch"` sample; `V01`'s `volume_for:["open","batch","exception"]` covers both).
- write_content / exception: `T01` `["text","tickets","corn ?dog"]` w3, `singled_out_by:"H2"`.
- delivery / volume: `V01` `["delivery","register_keys_exact"]` w3, `volume_for:["open","batch","exception"]`.
- delivery / core: `D02` `["delivery","slack_thread","1759272000.167533"]`.

## 4. stage_gate scenario

Command: `python3 Task_Authoring/tools/stage_gate.py scenario <task_dir> --paste` (`st_scenario` l.2393; stage spec
l.3200–3202: outputs `01_Scenario_Design.md`, `01_Hardness_Manifest.draft.json`, `01_Gradable_Surface.json`; input
`00_Assigments.md`; primary = `01_Scenario_Design.md`). `--paste` only writes on `PASS` (l.3610–3618) and inserts the
rendered block **inside the last Self-review section** of the primary artifact (`paste_block`, l.3323–3356), replacing
any earlier `STAGE GATE scenario:` block; with no Self-review heading it appends `## Self-review` + the block. The
pasted block is digest-neutral (`digest_text` drops every `STAGE GATE …` / `[PASS] …` line and the now-empty fences,
l.383–393), so pasting does not stale itself.

**Required sections** (`sections_present`, l.2395–2404 — a heading matching the regex, non-empty per
`content_lines()`; heading text as in the exemplar):
`assignment / persona census` (`assignment|census`) · `storyline` · `coherence` · `active|speaker` ·
`identity|entity` · `cohort` · `hidden authorit` · `delegation` · `chains|trap register` · `failure.diversity` ·
`deliverable` · `service role` · `call budget` · `qc rails` · `reach table` · `record plan` ·
`integration|companion` · `red.team` · `self[- ]review`. Check id `structure.sections`.

| check id | what it looks for (line) |
|---|---|
| `assignment.v3_context` | `00_Assigments.md` carries a V3 marker; `task_context.load_context(require_source=True)` succeeds (l.486–510) |
| `assignment.source_mode` | context `source.mode ∈ {universe, snapshot}` with a universe key (l.511–521) |
| `structure.outputs` / `structure.inputs` | the 3 outputs + `00_Assigments.md` exist (l.567) |
| `structure.fresh` | every output mtime newer than every input mtime (l.575) |
| `structure.sections` | the 19 sections above, each non-empty (l.2395, 590) |
| `structure.placeholders` | no `<template slot>`, no `TODO/TBD/FIXME/XXX` outside code spans, no unchecked `- [ ]`/☐, no `[ a | b ]` choices, no all-empty table row (l.608–636). Tool fences are exempt — but note a *plain* line like `<name>` fails |
| `evidence.storyline` | ≥ 80% of the storyline section's items (table data rows + bullet/numbered lines, `Section.items` l.352) carry an `RX_ID` pointer (l.125–140: Slack channel/ts, `f_…`/`evt_…`, Linear key, `repo#N`, `mailbox/<id>`, 24/32-hex, `page_…`, `cmt_…`, pointer, `INT-nn`, `SQL line N`) |
| `evidence.coherence_audit` | ≥ 100% of items in the coherence section carry such a pointer |
| `evidence.hidden_authorities` | ≥ 100% of items in the `hidden authorit` section, pointer required |
| `evidence.delegation` | ≥ 90% |
| `evidence.trap_register` | ≥ 90% |
| `evidence.record_plan` | ≥ 80% |
| `evidence.active_speakers` | ≥ 100%, pattern is `RX_EMAIL` (an email **or** `PERSON_/EMPLOYEE_/SVC_####_EMAIL`) |
| `tool.hardness_gate_design` | `01_Hardness_Manifest.draft.json --design --json` is **re-run**; the doc must contain the verbatim head `HARDNESS GATE (extreme (design)): PASS` (or FAIL) — `rx_design` l.2414 — and the re-run must agree (l.2416, `rerun_json_tool` l.1139) |
| `tool.persona_reach` (census) | in an `assignment|census` section the doc must contain `REACH  <name> <email>` (`REACH\s+(.+?) <([^>]+)>`, l.2442) with the assignment persona's email, **plus** `visible channels=(\d+)` equal to a re-run `persona_view reach` slack channel count, and, if the mailbox is set, `mailbox=\S+ threads=(\d+)` equal to the re-run Gmail thread count (l.2452–2463) |
| `tool.entity` | the `identity|entity` section contains the pasted `SHARED_FIRST_NAMES` or a line starting `ENTITY ` (l.1072–1078) |
| `kb.coherence_hazards` | the coherence section text must contain the literal `coherence_hazards`; every `[TSRQLI]\d{2}` on a line containing "hazard" must be a real id; all six categories `temporal, semantic, referential, quantitative, state/lifecycle, identifier/format` must each be represented by a cited valid hazard id or by `<category words> … none in scope` (l.906–929, `HAZ_CATS` l.185) |
| `kb.activity` | the `active|speaker` section must contain `activity`; every listed table row that resolves to a person in `activity.json` (by email or `First Last`) must include that person's `status_at_clock` string; ≥ 1 resolving row (l.943–965) |
| `kb.integrations` | the `integration|companion` section: every `INT-\d{2}` must exist in `integrations.json`, and for **each service key in the draft manifest's `services`** that has an integration source, either its INT id is cited or a line matching `\b<svc>\b[^|\n]{0,80}(?:no companion|none|n/a)` (l.1027–1050) |
| `kb.storyline` | the whole non-tool doc text must contain `timeline`, a valid `cohorts.json` id (`LIN\|SL\|GH\|GC\|GM\|SF\|TR\|DOC-…`) or `<cohorts.json … no fit / none fits / not used>`, and `trap_catalog` **with** a valid `[PNDCBXK]\d{2}` id (l.1053–1069) |
| `evidence.kb_locators` | only when `source.kb_status != "bound"`: every KB-dependent section (coherence, active
speakers, integrations, storyline) must cite a real record locator or an email, or say "no records in scope"
(l.878–903) |
| `boundary.anchor_naming` | **this is the anchor-name table check** (l.1360–1400): any table anywhere with a column matching `anchor name\|may be named\|noun phrase`, plus `Anchor A<n> name[sd]? : <phrase>` lines, plus the manifest's `anchors[].prompt_reference`. Each phrase (split on `;`, ` / `, `|`) must be ≤ 6 words, must not start with an imperative verb (`ANCHOR_VERB` l.1344–1349: pull/put/find/draft/send/…/report), and must contain no second-person word (`SECOND_PERSON` l.1350: you/your/yours/please/pls). `required=True`, so **zero entries fails**. Exemplar table: `| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |` with rows `| A1 | Julia's object hand-off request | C08R8CHB0QL/1759272000.167533 |` |
| `tool.redteam_dual` | `01b_Redteam_Review.md` **and** `01b_Redteam_Review.second.md` both exist and their first 4000 chars contain no tool-error stub (`set REDTEAM_MODEL`, `pass --model`, `budget_exceeded`, `HTTP \d{3}`, `redteam_review: error|failed`), **or** the design carries a line `RED TEAM FALLBACK: <who reviewed instead, and why>` ≥ 25 chars (l.2101–2131) |
| `surface.valid` | `Working_Files/01_Gradable_Surface.json` loads via `gradable_surface.load` and `validate(surface, draft_manifest)` has no FAIL findings (l.2134–2153) |
| `forecast.preregistered` | **non-blocking**: the doc must cite a ledger id matching `\bhev_[0-9a-f]{16}\b` whose ledger `kind == "forecast"` (l.2231–2236) |
| `revise.intake` / `revise.verdict_dispositions` / `revise.revision_binding` | SKIP unless a `01a_Hardening_Report.md` says `MODE B` or a `revision intake` section exists; then the section must name the `node_verdicts*.json` it consumes, every proposed rule needs a table row containing `keep|purge|rebuild`, CONFOUNDED candidates need a `confounded` word, and unbound exports must be marked historical (l.2239–2298). Returns `n_rev = count of LANDED/LEAKED` |
| `reach.scenario` | **persona reach paste comparison** (l.2433 + `reach_check` l.744–797) over the union of lines in the `reach table|load-bearing` section(s) **and** every line containing `LB`/`load-bearing`. Each scoped id (`SCOPED` l.146: gmail `mailbox/<id>`, `evt_…`, `[fd]_[0-9a-f]{22}`, Slack `C…/ts`) is re-verified with the SQL (none here) → `persona_view.can_see`. A `NO` verdict is accepted only on a line containing `DENIAL-INTENDED:` and an `UNVERIFIED` only with `UNVERIFIED-OK:`, in both cases with **no** `LB` token on that line and `alternate_evidence_ids <ids>` all YES; `planned_ok=True` also accepts an `UNVERIFIED` whose reason contains `(U4` (planned seeds not yet in base). Exemplar Reach table: `\| Record \| Service \| Visibility path \|` with cells like `planned seed in public #zombie-art (member)` |
| `review.counter_readings` | min = `max(7 + n_dp, n_rev + 1)` where `n_dp` = rows of the table(s) under a `two-reading\|decision point` section (l.2434). The **last** `self[- ]review` section's items (table rows + bullets) that mention counter/strongest/false-positive/false-negative/best case/argument/would fail/argue — or sit in a table with a `counter` column — must number ≥ min **and** contain an `RX_EVID` pointer (l.661–676) |
| `review.coverage` | that self-review's non-gate text must mention all of `temporal`, `semantic|category`, `referential|cross-service`, `quantitative|reconciliation`, `state|lifecycle`, `identifier|format`, `other`, and `HARDNESS GATE` (`QC_CATS` l.182–184 + l.2436) |
| `review.unresolved` | the self-review must contain `unresolved|left open|open items|unverified` (write `Unresolved: none`) |
| `v3.manifest_context` | the draft manifest's `assignment_context` five keys equal the current context (l.1988–2004) |
| `v3.role_review` | `00_V3_Authoring_Evidence.json` (see below) |
| `v3.evidence` / `v3.evidence_context` | the evidence file parses and `spec_version == "V3"` with `context_hash` equal to the current one (l.279–280) |
| `handoff.pasted` | a `STAGE GATE scenario: PASS` block exists in the primary artifact (or `--paste` writes it) and none of its recorded `file#digest` pairs is stale (l.1327–1338, 551–562) |
| `chain.*` | upstream chain: none for scenario (`upstream=[]`) |

**`00_V3_Authoring_Evidence.json` → `role_reviews.scenario`** (`v3_artifact_checks._review` l.134–152, called with
`role=True` for the scenario stage, l.267/282–286). Required top level: `spec_version: "V3"`, `context_hash` (current).
Required object `role_reviews.scenario` (exemplar shape, task_inputsH):
```json
{"reviewer": "Claude (build lane), scenario stage",
 "rationale": "<why this persona may do this work at the clock: role, that she authored the evidence, XFN decision not engineering status, every citation before freeze_utc, visibility, write rights>",
 "artifact": "01_Scenario_Design.md",
 "artifact_hash": "d4248908fa9c",
 "persona_role": "Art Lead",
 "source_ids": ["github:harmonygames-Games/match3d#431", "slack:C08R8CHB0QL/1758160800.325959"]}
```
Rules: `reviewer` and `rationale` non-blank; `artifact` must be exactly `"01_Scenario_Design.md"`;
`artifact_hash` must equal the **current** normalized digest of that file — get it with
`python3 Task_Authoring/tools/stage_gate.py --artifact-hash Task_Authoring/<task>/Working_Files/01_Scenario_Design.md`
(lenient: 12 hex); `persona_role` must equal `context["persona_role"]` (the assignment's role string, not the roster
label); `source_ids` a non-empty list of non-blank strings. `outcome_reviews` is **not** read at the scenario stage
(it belongs to prompt-writing/prompt-check). The digest deliberately ignores gate lines, so record the hash **before**
editing anything else in the file; any later wording change stales `v3.role_review` until you re-record it.

## 5. trap_liveness / hardness_forecast / hardness_v2_check

All three are **advisory** at the scenario stage (they never block a gate), but `stage_gate`'s
`forecast.preregistered` check (non-blocking) wants the ledger id they produce, and the design's Liveness and
self-review tables are expected to quote them.

### trap_liveness.py `--design` (S5b)
```sh
python3 -B Task_Authoring/tools/trap_liveness.py --design --task-dir Task_Authoring/<task> \
    [--manifest Working_Files/01_Hardness_Manifest.draft.json] [--prompt 04_Prompt.txt] [--out F.json] [--json]
```
(usage l.31–34; `main` l.469–524.) In `--design` it prefers `01_Hardness_Manifest.draft.json` over the final one, takes
**no SQL** (`sql_text=""`), and optionally reads `04_Prompt.txt` if it exists. Inputs read from the manifest
(`entry_set` l.157, `decisive` l.188, `decoys` l.211, `flags_for` l.241, `a15_nodes` l.294):
`anchors[].locator` (hub = the anchor locator most fragments delegate from), `ask_fragments[].delegated_by_record /
container / locator / seeded_ids / base_pointers / delegation_quote`, `traps[]` (`id, family, distractor_type,
requirement, services, seeded_ids, version_records[].id/.at, mechanism`), `authorities[]` (`id, governs,
home_service, seeded_ids, decoy_seeded_ids, decoy_scope.decoy`) and `mechanism_portfolio[].mechanism/nodes`.
Flags: `breadcrumb` (a decisive record is the target of a direct delegation from the hub, or named in the hub/prompt),
`self-advertising` (a decoy's title/first 200 chars carry another `decoy_scope` token or a stale word — needs record
text, so it cannot fire in design), `order` (a decisive record is the hub or a reply in its thread, or the delegation
quote labels a decoy superseded), `rule placement` (A15 nodes only). Output `{"kind":"TRAP_LIVENESS", "nodes":[{id,
flag...}], "dispositions":{"required":["T1:breadcrumb", …], "missing":[…]}}`; **every flag needs a written
disposition** — put the `{node:flag: {disposition, reason}}` map in `--dispositions` or (as the exemplar does) a
`| Flag | Disposition |` table under a "Liveness flags (S5b)" heading naming the trap and flag.

### hardness_forecast.py `forecast --design --preregister` (S9b)
```sh
python3 -B Task_Authoring/tools/hardness_forecast.py forecast --task-dir Task_Authoring/<task> \
    --model claude-opus-5-5 --design \
    --mechanisms R_DONE_MISSING,R_WITHDRAWN,...  \
    [--surface Working_Files/01_Gradable_Surface.json] [--manifest Working_Files/01_Hardness_Manifest.draft.json] \
    [--max-k 13 --allow-max-k 13] [--views auto] [--calls 550] [--draws 10000] [--seed 0] \
    [--freeze Working_Files/01_Hardness_Manifest.draft.json --freeze Working_Files/01_Gradable_Surface.json] \
    --preregister [--out F.json] [--json]
```
(`main` l.1814–1872, design branch l.1952–1966, 2069–2073.) Hard requirements in `--design`: `--mechanisms`
(the **`mechanism_portfolio` rule ids**, else `ValueError("--design needs --mechanisms …")`), `--model` (required at
the parser), and a slot layout (default `--surface 01_Gradable_Surface.json`, or `--slots`/`--layout`). It reads each
slot's `mechanisms` / `flipped_by` to compute `flipped(F)` (the slots a landing rule can flip), and the manifest's
`mechanism_portfolio` for each rule's `prior_family` (or legacy `family`) and `source` (rules sharing a `source` share
a latent in the `source` dependence scenario). `len(mechanisms) > --max-k` (default 8) refuses unless
`--allow-max-k N`; the exemplar's 13 rules need `--max-k 13 --allow-max-k 13`. It exits 2 with `UNSUPPORTED` above
`max_k`. `--preregister` appends a `kind: "forecast"` record to `Task_Authoring/support/hardness_ledger/ledger.jsonl`
and prints its `hev_<16 hex>` id — **cite that id in `01_Scenario_Design.md`** (anywhere; `prior_forecast` scans the
whole text) or `forecast.preregistered` is a non-blocking WARN. `--freeze <file>` records a sha256 per file (use the
draft manifest + surface): retrospection safety, not a gate.

### hardness_v2_check.py `--design` (advisory)
```sh
python3 -B Task_Authoring/tools/hardness_v2_check.py --design --task-dir Task_Authoring/<task> \
    [--manifest Working_Files/01_Hardness_Manifest.draft.json] [--surface Working_Files/01_Gradable_Surface.json] \
    [--prompt 04_Prompt.txt] [--json] [--strict]
```
(usage l.43–50; args l.675–687.) Reads the manifest (`traps[].version_records[].container`, `family`,
`mechanism_portfolio[].nodes/mechanism`, `chains[].root_cause`) and the surface (`slots[].weight == 5`,
`slots[].mechanisms/flipped_by`). Emits `SAME_PLACE, DONE_CHECK, TWO_DECISIONS, DECISION_FLIP, INPUT_CHECK,
FILTER_CHECK, RULE_IN_PROMPT` with `FLAG|CLEAN|SKIP|UNRESOLVED`; exit 1 only with `--strict`. Paste its block into the
self-review (the exemplar does, task_inputsH l.674–684) and give every FLAG a disposition.

## 6. Pitfalls

**Hardness gate (blocking in `--design`)**
1. `anchors` count must be 1–3 at the extreme profile (`anchors_max 3`) — a 4th anchor fails even though the Spec's
   prose says "1–3 sources"; the same phrase is re-checked by `boundary.anchor_naming`.
2. `prompt_reference` (and any anchor-name table cell) must be a **noun phrase ≤ 6 words**, no leading imperative verb,
   no second-person word (`ANCHOR_VERB`/`SECOND_PERSON`, stage_gate l.1344–1350). `Julia's object hand-off request` = 5
   words. Every table row and every manifest anchor is checked, so a duplicate verbose table row fails twice.
3. `delegated_by_record` must literally be one of the immediate parent's `seeded_ids`, `base_pointers` or `locator`
   (l.417–423). A fragment whose parent is an anchor needs that anchor to carry `seeded_ids` or the same `locator`.
4. `incorporated_via` must be a real path ending at an anchor; a fragment that lists only itself/another fragment
   fails ("never reaches an anchor"), and `delegated_by_record` must be the *last* link's record, not any ancestor's.
5. **Orphan requirement**: every declared requirement must appear in an *incorporated* fragment's or anchor's
   `requirement_ids` — but a fragment does not count as incorporated while it is broken, so one bad delegation quote
   silently orphans its requirements. Declare ≥ 6 requirements and give each one a trap (≥ 6 distinct
   `traps[].requirement`) or the `requirements` check reports it (the *undeclared* half is blocking; `uncovered` in the
   detail is not).
6. `surface_requirements`: the surface's `decides` must be a **substring of the declared requirement summary**, so the
   summary text must contain the exact output-column words ("Call column", "Rework tickets").
7. `call_budget`: rows with `conditional_on` count **0**, and the largest per-service share of calls **outside
   `phase == "per-record"`** must be ≤ 50% — a discovery-heavy budget fails. Need ≥ 10 distinct services with calls.
8. `supersession`: the trap `family` must be exactly `superseding` or `effective_date` (a `distractor` with
   `version_records` does not count); ≥ 4 such traps, ≥ 2 spanning 2 services, ≥ 1 with 3 versions, each `at` an
   ISO string and non-decreasing in list order (oldest first). `distractor_type` values must come from the 10-item
   enum and only `family: "distractor"` traps count toward the 6/4 requirement.
9. `hidden_authorities`: `home_service` must be one of gmail/gsheets/trello/snowflake/gslides/gcal/**gdocs**; `governs`
   lists must be pairwise disjoint; at least one authority needs `decoy_service == home_service`; each needs
   `findable_query` and both a real record set and a decoy record set.
10. `decoy_scope` is mandatory unless the decoy *is* an older `version_records` entry: `{dimension: lot|team|game|issuer,
    decoy, task}` with `decoy != task` after whitespace normalisation.
11. `rarely_opened_evidence` counts traps whose `services` intersect `{gmail,gsheets,trello,snowflake,gslides,gcal}` —
    put ≥ 3 traps' decisive evidence there (gdocs does **not** count).
12. `mechanism_portfolio` is optional but all-or-nothing per entry: `prior_family` **and** `prior_family_reason` are both
    required, `nodes` must be existing trap/chain ids, and `mechanism` must be in `A1–A25 ∪ 2.6.1–2.6.14`.
13. `chains.root_cause` must be a mechanism id and ≥ 3 chains must use **distinct** ids; each chain needs ≥ 3 hops over
    ≥ 2 services and a declared `ends_in`.
14. `artifact_fields` paths must be relative to the manifest's own folder (no leading `/`, no `..`) and digests 64-hex —
    a sensible first draft simply omits `solver`/`preflight` (written at injection); `gradable_surface: {"path":
    "01_Gradable_Surface.json"}` is enough.
15. `volume_exception` is `extreme`-only, and `call_budget_floor` must be an **int 100–500**, `per_record_floor` an int
    0–300; present-but-null or a string fails `effective_profile`. Long Horizon + `normal` and Normal Horizon +
    `extreme` without `profile_exception` both fail.

**Gradable surface (blocking via `surface.valid`)**
16. `version` must be the integer `1` (a string `"1"` fails `structure.kind`).
17. `weight` must equal the band of `work_kind` exactly (1 lookup; 3 interpretation/calculation/comparison/
    limited_reconciliation; 5 multi_source_reconciliation/deeper_reasoning/cross_modal/tracing). "Important so weight 5"
    is not allowed; change the work kind instead.
18. ≤ 5 `role: "sample"` slots per `group`, and each sampled group needs a `role: "volume"` slot whose `volume_for`
    names it (or `<prefix>:*`). An all-sample surface fails even though every slot is individually valid.
19. `role: "exception"` requires `singled_out_by` ∈ the manifest's authority/fragment/anchor ids **when validated with
    `--task-dir`** (stage_gate always passes the draft manifest). The exemplar's exceptions name `H1`/`H2`.
20. The same `fact_id` (or the same selector when `fact_id` is absent) in **3+** slots fails `duplicates.fact`; give the
    direct call and its ticket different `fact_id`s (as `corndog.call` / `corndog.ticket` do).
21. `field` selectors: the key must `re.fullmatch` some table deliverable's `key_regex` (`_table_for_key`, l.453) and
    the column must be in that table's `columns`. `text`/`link` targets must be a declared deliverable or one of
    `slide, tracker, email, slack`.
22. `delivery register_keys_exact` needs `truth_keys` (or slot `expected_keys`) unless the slot is the volume row; a
    `slack_thread` arg must look like `\d{10}\.\d{6}`, and a `tracker_state` arg must not look like a Trello id.
23. `truth_fields.groups` must name a field, never a value, and must not be the name of a table column.

**stage_gate scenario (blocking)**
24. `structure.fresh`: every output must be **newer** than `00_Assigments.md` — regenerate/touch after any assignment
    edit, or the gate fails on mtime.
25. `structure.placeholders` fails on any bare `<word>` in prose (e.g. writing `<persona>` or `<task>`), on `TODO/TBD`,
    and on an empty table row `| | | |`. Tool-output fences are exempt, prose is not.
26. 19 sections are required by heading regex: in particular `QC rails` (not "quality"), `Reach table (load-bearing
    records)`, `Record plan for /create-injection`, `Integrations and companions`, `Hidden authorities`, `Cohort spine`,
    `Delegation lattice`, `Chains and trap register`, `Failure-diversity plan`, `Service role map`, `Call budget`,
    `Active speakers`, `Identity traps`, `Coherence audit`, `Storyline`, `Assignment, persona census…`, `Red team`,
    `Self-review`, `Deliverables`.
27. `review.counter_readings` minimum is `max(7 + decision-points, revisions + 1)`: every data row of the Two-reading
    table raises the bar by one. A counter-reading is an item whose text says counter/strongest/false-positive/
    false-negative/best case/best argument/could fail/would fail/argue — **or** any row of a table whose header has a
    column matching `counter` (so name the column `Strongest counter-reading`, as the exemplar does, and every row
    counts). Each counted item must carry a pointer (`RX_EVID`: record id, `§N`, `R1`/`F1`/`P1`/`K1`, `L3`, `run-1`, a
    `.json/.md/.sql` filename, an `Eval N`) in the same row/item.
28. `review.coverage` requires the words `temporal`, `semantic`, `referential`, `quantitative`, `state`/`lifecycle`,
    `identifier`/`format`, `other` **and** the literal `HARDNESS GATE` in the last self-review section; `review.unresolved`
    requires `Unresolved:` (write `Unresolved: none`).
29. The self-review must contain the verbatim head `HARDNESS GATE (extreme (design)): PASS` and the re-run must agree —
    copy the tool's first line exactly (`HARDNESS GATE ({profile}): {verdict}`, hardness_gate l.1135, profile rendered
    `extreme (design)`).
30. `tool.persona_reach` wants `REACH  <name> <email>` **plus** `visible channels=<n>` **and** `mailbox=<box>
    threads=<n>` matching a fresh re-run — paste the whole `persona_view reach` block, don't retype the numbers.
31. Planned seeds in the Reach table pass only as `UNVERIFIED` with reason containing `(U4` (persona_view's
    "not in base (U4)" wording): cite the record id in the **Record** column of a `Reach table (load-bearing records)`
    line, and never mark that line `LB` if the record is a denial. Put `DENIAL-INTENDED:`/`UNVERIFIED-OK:` +
    `alternate_evidence_ids <ids>` on the same line for a genuine probe.
32. `evidence.*` ratios: table data rows **and** every bullet line count as items, so a bullet list without record ids
    drags the ratio down (100% is required for coherence, hidden authorities and active speakers).
33. `kb.*`: the coherence section must say `coherence_hazards` and cover all six categories (use valid `T…/S…/R…/Q…/L…/
    I…` ids or "<category> none in scope"); the active-speaker section must say `activity`; integrations must cover
    **every** service key in the draft manifest's `services` that has an integration source, or state `no companion`;
    the doc must cite `timeline`, a valid `cohorts.json` id and a `trap_catalog` id with a valid `[PNDCBXK]\d{2}`.
34. `v3.role_review`: `role_reviews.scenario.artifact_hash` must equal the doc's **current** digest
    (`--artifact-hash`); `persona_role` must be the assignment's role string; `rationale` and `reviewer` non-blank;
    `source_ids` non-empty. Because the digest ignores gate lines, record it after the last prose edit and re-record it
    after any edit; `handoff.pasted` also goes stale on any later output edit (it compares recorded `file#digest`
    pairs).
35. `tool.redteam_dual`: two review files, `01b_Redteam_Review.md` **and** `01b_Redteam_Review.second.md` (task_inputsH
    has neither — it used the fallback), or the exact line `RED TEAM FALLBACK: <≥25 chars>`.

**Cross-tool**
36. `00_V3_Authoring_Evidence.json` must live in `Working_Files/`, and its `context_hash` must equal
    `00_Task_Context.json`'s; a stale context after re-running `task_context.py --write` fails `v3.evidence_context`.
37. `--design` never reads SQL, so any `base_pointers` entry is really fetched from the base universe: a typo there is a
    hard FAIL now, unlike a planned seed id which is deferred.

**Exemplar inventory — `ls Task_Authoring/task_inputsH/Working_Files/`** (the shapes to copy; note what is absent):
`00_Pre_Scenario_Analysis.md, 00_Session_Goal.md, 00_Task_Context.json, 00_V3_Authoring_Evidence.json,
01_Gradable_Surface.json, 01_Grounding_Dossier.md, 01_Hardness_Manifest.draft.json, 01_Hardness_Manifest.json,
01_Scenario_Design.md, 01c_Dispositions.json, 01c_Forecast.json, 01c_Preflight_Report.json, 01c_Preflight_Report.md,
04_Prompt_Check.md, 04_Prompt_Writing_Brief.md, README.md` plus the directories `Eval_Sandbox, research, run_forensics,
scenario_gen, solver`. There is **no** `01b_Redteam_Review*.md` (the recorded `RED TEAM FALLBACK:` line stands in), no
`01a_Hardening_Report.md`, and no `03_Error_Async_Config.txt`.
