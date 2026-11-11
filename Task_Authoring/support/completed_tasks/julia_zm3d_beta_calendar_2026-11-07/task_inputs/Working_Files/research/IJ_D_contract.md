# Injection-Stage Machine Contract (IJ_D)

Read-only research for `/create-injection` on `Task_Authoring/task_inputsS` (synth-cut, Julia Lawson, ZM3D beta
live-ops calendar). Every claim below is read from the tool source; line numbers refer to the current tree.
Universe clock for synth-cut: **CLOCK = 2025-10-01T00:00:00Z** (seed bound); DATA_CLOCK = +7 h (visibility only).
Statements are seeded values, never executed.

## 1. sql_lint.py (Check B — schema + clock)

Command: `python3 Task_Authoring/tools/sql_lint.py <sql> [--json]`; exit 1 if any error.

**Line 1 (hard error, `sql_lint.py:612-615`).** The first non-blank line must fullmatch
`--\s*Are you planning to inject\?\s*(Yes|No)` (case-insensitive). Anything else → error line 1. Use
`-- Are you planning to inject? Yes` exactly.

**Statement grammar (`:623-647`).** Split on `;` outside quotes/comments/`$tag$`. Each statement must be a
schema-qualified `INSERT INTO s.t (cols) VALUES (...), (...);`, `UPDATE s.t SET ... WHERE ...;`, or
`DELETE FROM s.t WHERE ...;`. `BEGIN`/`COMMIT`/`SET ` are tolerated silently. A `DO $` block is a warning and is
not linted. Anything else → error "unsupported statement shape". **Ordering is not checked** (parents-before-children
is a deploy convention and a dossier statement, not a lint rule; `base_check` resolves forward references because it
collects every INSERT before resolving).

**Writable tables.** Exactly the 64 in `WRITABLE_TABLES` (`:64-129`). `snowflake.*` → error "do not write
Snowflake"; a table not in the live schema → error "unknown table"; a live table outside the 64 (`public._changelog`,
workflow-state tables, `*_meta` …) → error "not one of the 64 writable tables". Every `confluence.*` statement is a
warning ("unscoped and rarely opened") and must be dispositioned in the dossier.

**Columns.**
- unknown column in INSERT list or UPDATE SET → error.
- INSERT omitting a column that is NOT NULL, has no default and is not generated → error
  `INSERT omits NOT NULL column(s) [...]` (`:686-689`). This is the most common first-draft failure.
- INSERT or UPDATE writing a **generated** column → error `... the database computes it` (`:669-692`). Generated =
  schema `generated == "ALWAYS"`, every `*_fts` column (`slack_messages.text_fts`, any `body_text_fts`), plus anything
  flagged `generated` in `references/schema/injection.json`. Never list them.
- value count ≠ column count → error (`:696-698`). `NULL` in a NOT NULL column → error.

**Values.**
- `FORBIDDEN` (`:139`, applied with string literals blanked at `:625`): `now(`, `current_timestamp`, `current_date`,
  `localtimestamp`, `random(`, `gen_random_uuid`, `uuid_generate_v*`, `clock_timestamp` → error. Literals only.
- `*_json` columns: must parse; the `LIST_JSON` set (`members_json`, `label_ids_json`, `to_json`, `cc_json`,
  `bcc_json`, `parents_json`, `shared_with_emails_json`, `owners_json`, `attendees_json`, `idMembers_json`,
  `idLabels_json`, `reactions_json`, `files_json`, `attachments_json`, `labels_json`, `links_json`, `relations_json`,
  `assignee_logins_json`, `requested_reviewer_logins_json`, `member_logins_json`) must be JSON **arrays**; `{}` is a
  warning ("use '[]'"); any other object/string → error (`:510-524`). Other `*_json` (`metadata_json`,
  `state_history_json`, `badges_json`, `data_json`, `extras_json` …) are free-form but must still parse.

**Time (`:727-776`).** `parse_time` accepts epoch s / epoch ms / ISO-8601 (space or T, `Z` or `±hh[:mm]`, fractional) /
RFC-2822. For every column the eval linter's `EVENT_FIELDS` lists (read by `ast` from
`Evals/tools/hg_injection_lint.py`) **or** whose name matches its `EVENT_NAME`:
- value strictly `> CLOCK` (with a V3 `TASK_CONTEXT`) → error "is after the assigned clock … (an event field of the
  eval linter's inventory: seeded events are bound to the freeze)". Seeding exactly `2025-10-01T00:00:00Z` passes;
  one microsecond later fails.
- an unparseable literal in such a column → error ("write an ISO-8601 UTC literal").
- non-event columns matching `FUTURE_OK` (`due|start|end|deadline|scheduled|post_at|expires|original_start|effective`)
  after the clock → **warning** only ("allowed only as a deadline or a not-yet-happened event"). This is why
  `gcal.start_ts`/`end_ts` of a forward-dated event are allowed; its `created`/`updated` are not.
- other `PAST_ONLY` columns (`created|updated|sent|date|ts|time|timestamp|internal_date|completed|canceled|…`) after
  the clock → error.
- `created_at > updated_at` in one row → error.
- weekend (UTC) `ts|created_at|date` in a MESSAGE_TABLE → warning.
- **Text date columns** (flagged `format` in injection.json; Linear `*_at` = `iso_utc`, `due_date` = `date`): literal
  must be exactly `YYYY-MM-DDTHH:MM:SSZ` / `YYYY-MM-DD`. No space, no `+00`, no milliseconds, no cast, no expression
  (`:757-776`).

**Duplicates.** A repeated primary key within one table's SQL → error (`:707-716`). PKs come from
`universe_constraints_live.json`, else the built-in composite map (`sheets`, `slides`, `gmail_label_user_counters`,
`github_commits`, `commit_map`).

**Service ID contracts — errors (`row_rules`, `:457-603`).**
- Drive/Docs/Sheets/Slides: `[fd]_[0-9a-f]{22}`; Drive prefix must match mime (`d_` ⇔ folder).
- GCal `event_id` `evt_[0-9a-f]{22}`; `ical_uid` `[0-9a-f]{32}@hg4`; owner (`calendar_id`) is the **only** attendee
  with `self:true`; `start_ts`/`end_ts` must equal the dateTime inside `start_json`/`end_json`.
- GitHub comment/review ids `<pr_id>#c_<n>` / `#rev_<n>` / `#rc_<n>` / `#ev_<n>`.
- Trello ids `[0-9a-f]{24}` whose first 8 hex = the record's own Unix seconds (within 24 h of its `date`); year ≥ 2011
  and not after CLOCK.
- Gmail `id` `<mailbox>/<RFC Message-ID>`, `thread_id` `<mailbox>/<15-20 digits>`, `in_reply_to` `<…@…>`,
  `internal_date` (ms) must agree with `date` within 1 s; an own-mailbox copy whose From is the mailbox must carry
  `SENT`; otherwise the mailbox owner must be in To/Cc/Bcc.
- Linear `id == identifier`, `number` matches, `team_id == team_<KEY>`, and the lifecycle: Done ⇔ `completed_at`,
  Canceled/Duplicate ⇔ `canceled_at`, unstarted states carry no stamps, started ≤ completed, created ≤ stamps ≤
  updated.
- Slack `num_members == len(members_json)`.

**Stats / warnings reporting.** Output prints `schemas touched`, `rows by schema`, `errors: N  warnings: M`, then one
line per finding. The dossier must paste that summary line and the row total verbatim; the stage gate re-runs and
compares exactly.

## 2. base_check.py (/injection Checks A + C vs the base exports)

Command: `python3 Task_Authoring/tools/base_check.py <sql> [--manifest 01_Hardness_Manifest.json] [--json]`;
exit 0 = PASS, 1 = FAIL. Text header: `BASE CHECK (/injection A + C, static): PASS  — N inserts, M updates`; then
`Check A — records, references, IDs: PASS|FAIL (n)` and `Check C — dates and relationships: …`, then
`Warnings (n):`. JSON: `{verdict, check_A, check_C, warnings, notes, hazards_touched, kb, stats}`.

**Check A (references/ids; each row a FAIL):** new PK free in base and unique in SQL; every reference resolves to a
base record or a row the SQL inserts (channel, user, thread parent, issue/project/assignee, PR/repo/login, mailbox
thread, calendar, board/list/card/member, space/page, Drive parent, `drive_file_id`); every UPDATE/DELETE target
exists; **Slack id = `sha256("<channel>|<ts>")[:32]`** and `(channel,ts)` not already in base; Gmail ids carry their own
mailbox and thread prefix; `<@U…>` / `<#C…>` mentions resolve; Trello checklist→card→board, item→checklist, card/item
members, `idShort` unique per board; Linear state names exist; Drive/Docs/Sheets/Slides owner and every share entry are
real `@harmonygames.co` identities.

**Check C (coherence; FAIL):** replies after parents (Slack ts, Linear/GitHub/Confluence comments, Gmail reply after the
message it answers, Trello action after the card); Slack post not older than its channel and `created_at` == `ts`; GCal
`end_ts > start_ts`; **adding a reply to an existing Slack thread requires an UPDATE of the parent's
`reply_count`/`latest_reply`**, and every parent's counters equal its replies; GCal every attendee/organizer with a
calendar holds a copy (same `ical_uid`, agreeing time/status/title); Docs/Sheets/Slides owner+sharing mirror the
`drive_files` row; Linear lifecycle after UPDATEs and `updated_at` not older than its comments; a comment dated after
its issue closed FAILs ("a closed ticket that still has later activity"); every PR comment has its `commented` timeline
event (same `pr_id` and `created_at`); PR `updated_at` covers seeded activity; Trello badges/`dateLastActivity` follow
added comments/check items; Confluence versions continue `1..N` contiguously with `page.version = newest` and
`ri:content-title` links resolving.

**Warnings (non-blocking):** posts into archived channels; a Linear state that team never uses; KB advisory rows when
`kb_status == reference-only` (prefixed `ADVISORY (KB reference-only — record evidence required)`).

**Manifest inputs.** `integration_exceptions: [{record_id, reason}]` waives one companion (e.g. `no_notify`).
`hazard_acknowledgements: [{hazard_id, resolution, why_safe, requirement?}]`: touching a hazard record is a warning;
the SQL *modifying* a `state_lifecycle`/`cross_service_referential` hazard record is a FAIL and only
`resolution: repaired` clears it, and only if the predicate re-evaluates clean on the post-SQL state (supported for
Linear L01–L07; anything else is "unverifiable" → FAIL). `excluded`/`dated_claim` never apply to a modified record.

**Integrity layer.** INT-01 (mirrored-repo PR open/merge/comment/review needs its Slack app copy threaded under the PR's
"opened" message; FAIL at ≥95% base rate, warning ≥50%); INT-03 (a seeded PR naming a Linear key in the bot's active
repo window needs the `linear[bot]` comment); INT-11 (a meeting with attendees needs invitation mails; warning, waivable
by `integration_exceptions`); voice realism (a seeded author with no authored activity ±60 days = warning; dated after
a departure signal = FAIL).

## 3. base_claims.py (B1–B4: release-branch claims)

Command: `python3 Task_Authoring/tools/base_claims.py <sql> [--json]`; header
`BASE CLAIMS (injected text vs base git + #builds): PASS|FAIL`. It scans every text-bearing seeded value (Slack text +
attachments, Gmail subject/body, Linear title/description/comment, GitHub bodies, Trello desc/comment/old.desc,
Confluence bodies) for branch mentions:

- `BRANCH_RX` (`:59`): `release/<suffix>` — **any** `release/...` string in seeded text is a claim.
- plus, for every known base branch whose suffix contains `_` or `-`, a bare-suffix match (`:375-385`), e.g.
  `lava_fix_3` — so never paste a base branch suffix into seeded prose.

**B1 FAIL** branch does not exist. **B2 FAIL** record dated before the branch existed (window start = first `#builds`
build or first non-develop commit, −12 h tolerance). **B3 FAIL** a positive pick claim ("picked onto / cherry-picked
onto / going out on / landed on / moved the pick to …") dated after the window closed + 3 days. **B4 FAIL** the ticket
the clause is about has commits and `git branch --contains` shows none on the claimed branch. **B4′ WARN** same for a
backed-out mention. **INFO** ticket with no commit naming it → date-checked only.

**Our design seeds no branch claims** (the deploy is a GCal event). An all-event design with no `release/` string and no
base branch suffix in any seeded text produces zero claims → `PASS` with no rows. The one way to trip it accidentally is
wording such as "release/1.4 branch" or a copied branch name inside a GCal description, a Confluence body or a Slack
message.

## 4. hg.py lint (the eval's `Evals/tools/hg_injection_lint.py`)

Command: `python3 Task_Authoring/tools/hg.py lint [--task-dir DIR] [--sql PATH] [--checks …] [--no-base] [--summary]`.
The upstream linter always exits 0; the stage gate reads the JSON. Keys: `tool`, `version`, `sql`, `sha256`,
`universe`, `clock`, `checks`, `statements{total,by_kind}`, `rows{table:{op:count}}`, `base{used,loaded}`,
`counts{FAIL,CHECK,INFO,by_check}`, `flags[]`, `info[]`, `note`.

**Check ids and severities** (`CHECKS`, `:43`; docstring `:5-18`):

| id | severity | trigger |
|---|---|---|
| `future_date` | FAIL | event timestamp after the task clock |
| `id_contract` | FAIL | value breaks `references/schema/id_contracts.json` |
| `drive_unreadable` | FAIL | injected Drive doc/sheet/slide the agent cannot open: no `docs_documents` row with non-empty `body_text`, or a `content_path` that is not real base bytes in the base path format (`content_text` alone does not serve reads) |
| `duplicate_account` | FAIL | a second account for an existing person in one service (`slack_users`, `trello_members`, gmail mailbox columns) |
| `actor_name` | FAIL | sender/creator id belongs to a different person than the record names |
| `unknown_actor` | CHECK | author/creator id with no account in base or SQL |
| `grader_language` | CHECK | text addressed to a solver/grader or describing the test (`GRADER_PATTERNS`) |
| `padding_comment` | CHECK | SQL comment mentioning tool calls / pass rate / gates / hardness (`PADDING`) |
| `generated_column` | FAIL | INSERT/UPDATE writes a generated column |
| `text_time_format` | FAIL | text date column not `YYYY-MM-DDTHH:MM:SSZ` / `YYYY-MM-DD` |
| `missing_required` | FAIL | INSERT omits a NOT NULL column with no default |
| `unparsed` | INFO | statement/value the linter could not evaluate |

**Gate rule (`stage_gate.py:1215-1283`).** Non-zero exit, an `error` payload, **any FAIL**, a `sha256` that is not the
current SQL file's sha256, or a CHECK flag with no disposition line blocks `tool.injection_lint`. INFO never gates.
Disposition format — one line per CHECK flag, keyed by that flag's own line, inside the **Self-review** section:

```
LINT grader_language L137: in-world Slack phrasing (Julia quoting a league name); not addressed to a solver
LINT padding_comment L12: header comment for the reviewer, mentions no gate or pass rate
```

`LINT_DISPOSITION` regex (`:1188`): optional bullet/number, `LINT <check> L<line>: <text>`. Two flags of the same check
on different lines need two lines; a flag's `also.records` are covered by the parent line. Duplicate identical flags
collapse to one.

## 5. fact_check.py (`--no-leak`)

Command: `python3 Task_Authoring/tools/fact_check.py <sql> --manifest 01_Hardness_Manifest.json --no-leak [--json]`
(exit 0 PASS / 1 FAIL). Header `FACT CHECK: PASS|FAIL — N text-bearing rows, M declared facts, K declared superseded
records`.

**`facts` entry** (manifest spec line 65):

```json
{"key": "beta cutover", "value": "2025-10-09", "kind": "date",
 "aliases": ["cutover"], "must_appear_in": ["C08…/1759272000.167533"],
 "home_ids": ["evt_…"], "forbidden_variants": [], "version_records": []}
```

`kind` ∈ `amount|date|count|name|status|id|version`. Rules: wherever `key`/an alias is mentioned, any value of that kind
in the same sentence/line must equal `value` (amount normalisation `$11.7K` = `11,700`; dates compared in UTC when both
carry a zone); a `name` may not appear in a near-spelling (difflib ≥ 0.8); `forbidden_variants` may appear nowhere;
each `must_appear_in` record must state the value (unknown/unmatched ids are warnings); records named in
`traps[].version_records` (all but the newest) are exempt as superseded.

**`--no-leak`** (`leaks()`, `:479-515`): if a fact declares `home_ids`, its value may appear **only** in its home rows,
its `must_appear_in` records and its own `version_records`. Any other seeded text row that states the value is a
`fact_leak` **error**, annotated `— bulk-readable: <what>` when it lands in a Slack message, Linear description, Sheets
cell, Confluence body, Docs body, GCal description, etc. Practical rule: give every per-record answer one home row and
never restate it in a channel/description/cell. Facts about global rules/dates may omit `home_ids` (they are allowed to
repeat).

It also errors on unresolved ids cited in text (Linear keys, `github.com/…/pull/N`, `<repo>#N`, Slack permalinks,
`f_/d_`, `evt_`, `page_`) and warns on entity-spelling drift, conflicting amounts/dates per subject, inactive people,
ambiguous bare first names.

## 6. hardness_gate.py (full mode — checks that start to run with SQL)

Command: `python3 Task_Authoring/tools/hardness_gate.py <manifest> <sql> [--profile extreme] [--json]`; header
`HARDNESS GATE (extreme): PASS|FAIL`. In `--design` these ten are reported as skipped; with SQL they run:

| check | requirement of the SQL |
|---|---|
| `sql_lint_clean` | `sql_lint.errors == []` (exact same linter, so pass sql_lint first) |
| `base_consistency` | `base_check(sql, manifest).verdict == PASS` (manifest's `integration_exceptions`/`hazard_acknowledgements` supplied) |
| `services_injected` | distinct schemas touched ≥ 10 (extreme). Synth-cut/Julia profile must list the same services in `manifest.services` |
| `rows` | `ops.insert ≥ 120` (extreme) — UPDATE companions do not count. This task's `volume_exception` (`call_budget_floor` 128, `per_record_floor` 75) replaces only the call-budget/per-record minima; `rows` stays 120 and `services_injected` stays 10 |
| `no_orphan_injection` | every injected schema is a key of `manifest.services`; an injected schema absent from the design fails |
| `seeded_ids_exist_in_sql` | every `ask_fragments[].seeded_ids`, `traps[].seeded_ids`, `authorities[].seeded_ids`, `*_decoy_seeded_ids` and `version_records[].id` where `seeded` is truthy must appear **literally** in the SQL outside comments (`_has_token`/`_code_only`) |
| `supersession_chronology` | for each trap with ≥2 `version_records`, the rows' own timestamps (`created_at`/`ts`/`date`/`updated_at`, or the base record) must be strictly increasing in listed order (oldest first) |
| `persona_reach` | every seeded id cited by fragments/authorities/traps/chains/cohort surfaces is YES for the persona via `persona_view check-sql`; UNVERIFIED never satisfies a dependency; only `denied_probes` (traps/decoys only, with all-YES `alternate_evidence_ids`) may be NO |
| `fact_consistency` | `fact_check --no-leak` errors == 0 |
| `hazard_scope` | touched records in a hazard need a `hazard_acknowledgements` entry with a valid `resolution` |

Non-SQL checks that also run (unchanged): effective_profile, assignment_context, anchors, ask_fragments counts,
cohort size (with `cohort_exception.cohort_floor` 10–40), evidence_surfaces, call_budget (floor/cap), traps,
supersession, independent_chains, mechanism_portfolio, artifact_fields. `artifact_fields` requires
`gradable_surface {path,digest}`, optional `solver {path,digest}`, optional `preflight {report,digest}` — relative
paths and 64-hex sha256. `volume_exception` must be complete: `{reason, requester_confirmation, call_budget_floor
(100-500), per_record_floor (0-300)}`.

## 7. oracle_kit.py (solver contract)

`python3 -B Task_Authoring/tools/oracle_kit.py check --task-dir DIR [--solver S] [--sql SQL] [--revision R]
[--previous-sql P --previous-truth T] [--manifest M] [--surface S] [--json]` → prints `SOLVER CONTRACT: PASS|FAIL`
plus `[PASS|FAIL|WARN] contract.<id>: detail`; exit 1 on FAIL.
`truth --solver S --sql SQL [--revision R] --out truth.json` writes `{key: {field: value, "groups": [...],
"evidence": [...]}}` (the solver's `solve(load_state(sql))`, `json.dumps(indent=2)`), prints
`wrote <path> (N keys, sha256 …)`.

**Module contract.** Required: `RULES`, `load_state`, `solve`, `aggregates`, `evidence`.
- `RULES {rule_id: {mechanism, requirement, natural_reading, nodes[], decides[], signature?, authority[]?,
  source?, family?, controls[]?, over_application?}}` — rule ids are the manifest `mechanism_portfolio` ids, 1:1.
- `load_state(sql_text, revision=None)` → state (parse via `base_check.parse_sql`, never execute). The exemplar
  returns `{"ids": set(...), "revision": ..., "rows": n}`.
- `solve(state, disable=frozenset(), degrade=frozenset(), keys_=None)` → `{key: {field: value, groups?, evidence}}`;
  `disable` takes rule ids or `(rule, key_set)` pairs; `degrade` takes operator names or `(operator, key_set)` pairs.
- `aggregates(rows)` → `{"classes": {…}, "groups": {group: [keys]}}`; `evidence(rows, key, field)` → `[record ids]`.
- optional `touched`, `deciding`, `DEGRADES {operator: description}`, `REVISIONS`, `KEY_REGEX`, `FIELDS`,
  `CLASS_FIELD`, `GROUPS_FIELD`, `base_route(record_id) -> {service, file, pointer, field}|None`.

**Checks emitted** (`_check` ids): `contract.interface`, `contract.deterministic` (two solves forward/reverse +
fresh processes `PYTHONHASHSEED=1,2` identical canonical JSON), `contract.regression` (WARN when no previous
revision), `contract.rules_nodes` (one-to-one with `mechanism_portfolio`; every node a manifest trap/chain id; same
node lists), `contract.slots` (every `class: direct|aggregate` surface slot must read a solver value by selector, and
the referenced keys must exist), `contract.controls`, `contract.golden`, `contract.digest` (WARN if no `solver`
declared, FAIL if `path`/`digest` mismatch or point at another file).

**`contract.controls`** (`:169-241`): every `controls[]` member must be a solver key; every `over_application`
operator must be accepted by `solve(degrade={op})`, must move at least one control member's `decides` field (or class),
and must **not** equal that rule's ablation (`solve(disable={rule})`) for those members — otherwise
"the control cannot be separated from a rule error". Every `CHANNELS` entry needs a known `kind`
(`scale|chain|delegation|synthesis|tool_surface`), `latent ∈ {member,batch,run}`, and either `members` + a working
`degrade`, or `slots` that are real surface slot ids.

**`contract.golden`** samples ≤12 keys × every `FIELDS` entry; each field needs `evidence()` ids that (a) exist as an
`id` in the SQL index, or (b) are routed by `base_route` and read through `hg.py records`. A value that is absent from
its deciding records → FAIL; unrouted base ids → "unverified" (reported, not blocking).

## 8. difficulty_mutation.py (mutants, interventions, geometry)

`python3 -B Task_Authoring/tools/difficulty_mutation.py mutate --task-dir DIR [--dispositions D.json]
[--require-dispositions] [--out OUT] [--json]` and `… geometry --task-dir DIR [--views auto|v3] [--out OUT] [--json]`.

**mutate** emits `{key_locality, mutants[{id, diagnostic, flipped_slots, flipped_weight, …}], shards{count, source,
diagnostics{KILLED,WEAK,SURVIVED,EQUIVALENT}}, interventions[], dispositions{required,recorded,missing}}`.
Mutant ids: `rule:<id>`, `degrade:<op>`; interventions `intervention:<kind>:<id>`.
Diagnostics: **KILLED** = flips a direct slot of weight ≥3; **WEAK** = only aggregate/weight-1 slots, or an aggregate
change that cancels; **SURVIVED** = changes outputs no slot reads; **EQUIVALENT** = changes no output.
Interventions (deciding records removed from an in-memory copy): **load-bearing** (own closure only), **inert**
(nothing changed — for a degrade this is the required fairness property: truth does not read the decoy), **escaped**
(something outside the closure changed = undeclared coupling).

**Dispositions** (`DISPOSITIONS = ("live","weak-accepted","redesign","retire","redundant","masked","solver-gap")`,
`:93`): `01c_Dispositions.json` → `{"mutation": {"rule:<id>|degrade:<op>|intervention:<kind>:<id>":
{"disposition": <one of the seven>, "reason": "non-empty"}}}`. Every `required` id needs one; `--require-dispositions`
exits 1 otherwise. Malformed or unknown disposition = FAIL at the gate.

**geometry** emits `{U, U_exact, flippable_weight, total_weight, flippable_slots, not_flippable,
flippable_by_class, elements, inert_elements, assumptions, L_max{value,status}, views{V3:{cap, mode,
needs_loss_above, U{verdict, bound_verdict}, L_max{verdict}}}}`. Rule: **U must exceed 1 − cap** for every view, else
BLOCK. If the solver is not composable (not key-local, or locality checked on too few configurations) the verdict is
**UNVERIFIED**, never BLOCK, and needs `{"geometry": {"geometry.U": {"disposition":
"accepted-unverified|redesign|solver-gap", "reason": "…"}}}`. `L_max` warns below `(1 − cap) + 0.10`; advisory.
Exit 1 on BLOCK or a missing required disposition.

## 9. preflight_report.py

`python3 -B Task_Authoring/tools/preflight_report.py --task-dir DIR [--forecast F.json] [--views auto]
[--max-k 8]` → writes `Working_Files/01c_Preflight_Report.json` + `.md`, prints
`PREFLIGHT: PASS|FAIL · blocking {...} · advisory {...}`; exit 1 on a blocking part.

`bound_to` = sha256 of **sql, solver, surface (`01_Gradable_Surface.json`), manifest (`01_Hardness_Manifest.json`),
dispositions (`01c_Dispositions.json`)**, each `{path (relative to the task folder), sha256}`. Any edit after the run
makes it stale → re-run last. Top-level keys: `kind: "PREFLIGHT_REPORT"`, `version`, `tool`, `label`, `revision`,
`verdict`, `blocking{solver_contract, surface_validation, mutation_dispositions, geometry_upper_bound}`,
`advisory{geometry_margin, geometry_bound_verdict, liveness_dispositions_missing, forecast}`,
`bound_to`, `solver_contract`, `surface{validation, expected{slot:value}, flipped_by{slot:[mutant ids]}}`,
`mutation{key_locality, mutants, shards, interventions, dispositions}`, `geometry{…, dispositions}`, `liveness`,
`forecast`, `max_k`, `max_k_override`.

## 10. stage_gate.py — `injection`

`python3 Task_Authoring/tools/stage_gate.py injection Task_Authoring/task_inputsS [--rerun all] [--paste]
[--json]`. Primary artifact: `Working_Files/01_Grounding_Dossier.md`. Every check id it can emit:

**Structure.** `structure.sections` — all of: `1.A structural`, `1.B entity`, `1.C voice`, `1.D keyword`,
`1.E persona reach`, `1.F collision`, `record ledger`, `findability`, `self-validation`,
`integrations / companions`, `coherence census` (`coherence|touched-data`), `intended disagreements`,
`constraints for the brief`, `facts for the human`, `platform follow-ups`, **`fact sheet`** (required because the
manifest spec declares `facts`), `self-review` — each present and non-empty. `structure.placeholders` — no `<template
slot>`, TODO/TBD, unchecked boxes or all-empty table rows.
`structure.design_delta` — every id in the draft manifest (`requirements` keys, `anchors`, `ask_fragments`,
`authorities`, `chains`, `traps`, `denied_probes`) still present in the final manifest, or listed in
`design_delta: [{id, change, reason}]` with a non-empty reason.
`structure.preflight` — `01c_Preflight_Report.json` exists, `kind == PREFLIGHT_REPORT`, and its `bound_to` sha256s match
the current SQL/solver/surface/manifest/dispositions.
`structure.facts_declared` — manifest `facts` non-empty.

**Evidence.** `evidence.entity` (≥90% of 1.B rows carry a record id), `evidence.keyword` (100%, ids or `NEW TERM`),
`evidence.persona_reach` (100%), `evidence.record_ledger` (100% every row/item has an id), `evidence.facts_for_human`
(100%), `evidence.kb_locators` (only when the KB is not bound: each of coherence census / voice / integrations /
record ledger cites a record locator or email).

**Tool pastes + re-runs.** `tool.sql_lint` — the dossier pastes `errors: N  warnings: M` and `total rows: N`; the
gate re-runs sql_lint and requires 0 errors and exactly those numbers (stale paste = FAIL).
`review.warning_dispositions` — every sql_lint **warning class** (weekend, clock/deadline, confluence/snowflake,
delete, or the normalised message) has a line in the dossier pairing it with "warn/disposition".
`tool.injection_lint` — pasted/fresh `hg.py lint`: exit 0, 0 FAIL, sha256 == current SQL, CHECK flags ≤ dispositions
(see §4). `tool.base_check` — dossier pastes `BASE CHECK (/injection A + C, static): PASS` and the gate re-runs it.
`tool.base_claims` — pastes `BASE CLAIMS (…): PASS`; re-run PASS.
`tool.hardness_gate` — pastes `HARDNESS GATE (extreme): PASS`; if any pasted profile differs from the manifest's
`effective_profile` → FAIL; re-run with `--profile <manifest profile>`. `tool.hardness_gate_profile` only fires on that
mismatch.
`tool.check_sql_pasted` — dossier contains a line `CHECK-SQL as <persona_key> <email>` and, on its own line,
`verdict: PASS`, produced by `persona_view.py check-sql <persona> <sql> --load-bearing <ids>`; the email must equal the
assignment persona's email.
`tool.fact_check` — pastes `FACT CHECK: PASS` from `fact_check … --no-leak --json` (re-run when `--rerun all`).
`reach.injection` — every scoped load-bearing id on the `1.E persona reach` and `facts for the human` lines must be
YES for the persona (`persona_view` visibility, SQL overlay included). A NO row needs `DENIAL-INTENDED:` + YES
`alternate_evidence_ids`; UNVERIFIED needs `UNVERIFIED-OK:` + YES alternates; neither may be marked `LB`.
`tool.base_check`/`base_claims`/`hardness_gate`/`fact_check` re-runs are skipped under `--rerun lint` (PARTIAL only).

**Preflight-derived.** `solver.contract` — the preflight's `solver_contract.verdict == PASS`, and the gate re-runs
`oracle_kit.contract` on the current solver/SQL/manifest/surface. `mutation.dispositions` — every id in the
preflight's `mutation.dispositions.required` has an entry in `01c_Dispositions.json` with a valid disposition and a
non-empty reason. `geometry.upper_bound` — the preflight carries the task's gate view (`V3`) with `U.verdict` PASS, or
UNVERIFIED **with** a `geometry.U` disposition; the gate re-runs the geometry from the solver and SQL.
`geometry.margin` (advisory) — `L_max.verdict == OK`. `liveness.dispositions` (advisory) — every required liveness
flag dispositioned. `forecast.preregistered` (advisory) — the preflight's forecast hash is in the ledger.

**KB gates.** `kb.coherence_hazards` — the census section names `coherence_hazards.json`, cites only real hazard ids on
lines that say "hazard", and covers all six categories (`temporal, semantic, referential, data-quality/quantitative,
state/lifecycle, identifier/format`) or says "none in scope"; `kb.activity` — speakers/dates valid; `kb.integrations`
— per-service companion decisions. Under `reference-only`/`unavailable` KB these degrade to warnings, but
`evidence.kb_locators` then blocks.

**Boundary.** `boundary.anchor_naming` — every anchor named by a noun phrase ≤6 words, no imperative verb, no
second-person request. Sources: a table column `anchor name` / `may be named` / `noun phrase`, `Anchor A<n> name[s]:`
lines, and the manifest's `anchors[].prompt_reference`.

**Self-review.** `review.counter_readings` — ≥ `7 + n_intended_disagreements` counter-readings, each carrying an
evidence pointer (record id, §, `L<n>`, mechanism id). `review.coverage` — the last Self-review section addresses all
six QC categories (`temporal`, `semantic|category`, `referential|cross-service`, `data quality|quantitative`,
`state|lifecycle`, `identifier|format`) plus `check A` (Checks A–C walk) and `touched|census`.
`review.unresolved` — mentions `unresolved`/`left open`/`open items`/`unverified` (write "Unresolved: none").

The dossier's Self-review must also carry the `LINT <check> L<n>:` lines (§4) and any sql_lint/fact_check warning
dispositions.

## Exemplar shapes (task_inputsH, completed extreme task)

**SQL header** (`01_Universe_Inject.sql`, 409 lines, 121 INSERT + 11 UPDATE, 132 statements, 10 schemas):

```
-- Are you planning to inject? Yes

-- HarmonyGames injection - Claire Morgan (…), Art Lead - Long Horizon - synth-cut, freeze 2025-10-01T00:00:00Z
-- Services: gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, trello - 121 INSERT, 11 UPDATE
-- Literal values only; parents before children; re-apply before every agent run.

-- slack: #zombie-art asks and replies, …
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy,
  reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json,
  attachments_json, created_at, metadata_json) VALUES (…);
```

Grouping: one comment banner per service, statements ordered parent→child, companion UPDATEs after their sibling inserts.
Representative column lists (copy these):

```
linear.linear_issues: id, uuid, project_id, team_id, parent_id, assignee_id, creator_id, state_id, cycle_id,
  identifier, number, title, description, priority, estimate, due_date, started_at, completed_at, canceled_at,
  archived_at, time_in_status_minutes, labels_json, links_json, relations_json, state_history_json,
  is_archived, created_at, updated_at
gmail.gmail_messages: id, thread_id, user_email, label_ids_json, snippet, history_id, internal_date, date,
  size_estimate, subject, from_email, from_name, to_json, cc_json, bcc_json, reply_to_json, body_text, body_html,
  headers_json, payload_json, in_reply_to, "references", mbox_from, date_parsed_source, attachments_meta_json
gcal.gcal_events: event_id, calendar_id, summary, description, location, start_ts, end_ts, start_json, end_json,
  organizer_email, creator_email, attendees_json, status, visibility, transparency, rrule_json,
  recurring_event_id, original_start_json, sequence, created, updated, hangout_link, ical_uid, extras_json
gdrive.drive_files: id, name, mime_type, parents_json, owner_email, shared_with_emails_json, shared_roles_json,
  visibility_role, visibility, owners_json, modified_time, created_time, size, trashed, starred, content_path,
  web_view_link, icon_link, description, drive_id, content_text
gdocs.docs_documents: document_id, title, owner_email, shared_with_emails_json, visibility, body_text,
  style_runs_json, revision_id, drive_file_id, created_time, modified_time
gsheets.sheets_spreadsheets: spreadsheet_id, title, owner_email, shared_with_emails_json, visibility,
  drive_file_id, created_time, modified_time
gslides.slides_presentations: presentation_id, title, owner_email, shared_with_emails_json, visibility,
  drive_file_id, revision_id, created_time, modified_time
trello.trello_cards: id, name, "idBoard", "idList", "desc", pos, closed, due, "dueComplete", "idMembers_json",
  "idLabels_json", "idShort", "shortLink", "shortUrl", url, "dateLastActivity", cover_json, badges_json, start,
  "idAttachmentCover"
```

Quoting: camelCase Trello columns (`"idBoard"`, `"idList"`, `"idShort"`, `"dateLastActivity"`) and Gmail
`"references"` are double-quoted; everything else bare.

**Final manifest keys the draft lacks** (draft: assignment_context … gradable_surface): `facts`,
`hazard_acknowledgements`, `integration_exceptions`, `design_delta`, `solver {path, digest}`. The exemplar carries **no**
`preflight` key; `artifact_fields` only validates it when present, and the stage gate reads
`Working_Files/01c_Preflight_Report.json` directly, so declaring `preflight {report, digest}` is optional (keep the digest
current if you do declare it).

`facts` array shape (5 entries in the exemplar; all per-record answers, kinds `id`):

```json
"facts": [
  {"key": "Shuttlecock ticket", "value": "ART-793", "kind": "id", "home_ids": ["ART-793"]},
  {"key": "rework parent", "value": "ZOM-567", "kind": "id", "home_ids": ["ZOM-567", "cmt_zom567_1"]},
  {"key": "October object cut", "value": "2025-09-17T02:00:00Z", "kind": "date"},
  {"key": "objects check-in", "value": "2025-09-25", "kind": "date",
   "must_appear_in": ["claire.morgan@harmonygames.co/1844255455526780928"]}
]
```

A global rule/date may omit `home_ids` (it may be restated); a per-record answer must declare `home_ids` and is then
confined to those rows.

`hazard_acknowledgements` (one entry):

```json
{"hazard_id": "L03", "resolution": "repaired", "requirement": "R11",
 "why_safe": "SC-16: ZOM-513 and ZOM-514 were In Progress although #412 shipped; the SQL closes both
  (Done, completed_at 2025-09-26T18:00Z / 18:02Z) after Robert's dated closing comments, and base_check
  re-evaluates the post-SQL state (PASS)."}
```

`version_records` live inside each trap: `version_records: [{id, seeded: true, when|base_pointer, note}]`, oldest first,
timestamps strictly increasing; `delegation_quote` is an **exact substring** of `delegated_by_record`'s text (seeded row
or base record read by `hg.py`). `solver`: `{"path": "Working_Files/solver/solver.py", "digest": "<64 hex>"}`;
`gradable_surface`: `{"path": "01_Gradable_Surface.json", "digest": "<64 hex>"}`.

**Solver skeleton** (`Working_Files/solver/solver.py`, 668 lines, stdlib only):

```python
"""<task> solver … Parses the injection SQL as data through tools/base_check.parse_sql; never executes SQL."""
import collections, hashlib, json

KEY_REGEX = r"[A-Za-z][A-Za-z &'-]{1,40}"
FIELDS = ["object", "PR", "call", "rework ticket", "notes"]
CLASS_FIELD = "call"
GROUPS_FIELD = "groups"
REVISIONS = ("rev1",)
KEYS = json.loads(r"""["Bed", "Wardrobe", …]""")

RULES = {
  "R_DONE_MISSING": {"mechanism": "A24", "family": "A24", "requirement": "R3", "nodes": ["T1", "CH1"],
                     "decides": ["call", "rework ticket"], "controls": ["Chocolate Bar", "Sandwich"],
                     "over_application": "over:every-object-missing-a-colour", "source": "corn-dog",
                     "signature": "promised-colour-missing", "authority": [H1],
                     "natural_reading": "merged + done note = ready"},
  … one entry per mechanism_portfolio id …
}
DEGRADES = {"over:every-object-missing-a-colour": "treat every … as Rework", …}
CHANNELS = {}      # e.g. {"scale:status": {"kind": "scale", "degrade": "slip:status", "members": [...]}}
RULES_ORDER = ("R_BATCH_CUT", "R_CUT_AMEND", …)
FALLBACK = {"R_DONE_MISSING": {"Corn Dog": ("OCTOBER", None)}, …}

def load_state(sql_text, revision=None):
    from base_check import parse_sql          # parse as data, never execute
    rows = [x for x in parse_sql(sql_text) if x["op"] == "insert"]
    ids = {…}
    return {"ids": ids, "revision": revision or "rev1", "rows": len(rows)}

def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None): …   # deterministic dict output
def aggregates(rows): …  # {"classes": {...}, "groups": {g: [keys]}}
def evidence(rows, key, field): …   # ids present in the SQL or routed by base_route
def touched(state, rule): …; def deciding(state, rule, key): …
def base_route(record_id):
    return {"service": "github", "file": "data.json", "pointer": "/pull_requests", "field": "id"} or None
```

**`01c_Dispositions.json`**: `{"mutation": {"rule:<id>": {"disposition": "live", "reason": "KILLED: …"},
"intervention:rule:<id>": {"disposition": "live", "reason": "load-bearing: …"}, "degrade:<op>": {…}},
"liveness": {"<node>:<flag>": {"disposition": "keep the link", "reason": "…"}}}` (add `"geometry"` only for an
UNVERIFIED U).

**`01c_Preflight_Report.json`**: keys `kind, version, tool, label, revision, verdict, blocking, advisory, bound_to,
solver_contract, surface, mutation, geometry, liveness, forecast, max_k, max_k_override`; `bound_to` maps
`sql|solver|surface|manifest|dispositions` to `{path, sha256}`.

**`01_Grounding_Dossier.md` heading list the gate looks up** (H2 exact names):

```
## 1.A Structural
## 1.B Entity table
## 1.C Voice and realism
## 1.D Keyword
## 1.E Persona reach
## 1.F Collision
## 2 Record ledger
## 3 Findability and discovery order
## 4 Self-validation
## 5 Intended disagreements
## 6 Constraints for the prompt brief
## 7 Facts for the human
## 8 Fact sheet
## 9 Integrations and companions
## 10 Touched-data census and coherence hazards   (### Touched-data census, ### Hazard audit)
## 11 Platform follow-ups
## 12 Self-review
```

- **Facts for the human** = one table row per seeded or relied-on record:
  `| locator | base/seeded | fact / element | actor / UTC | reach path | role | re-verify? |` — locator must be a full
  record id (100%).
- **Fact sheet** = `| Key | Value | Kind | Must appear in / home |` + the pasted FACT CHECK block and a disposition for
  each warning.
- **1.E** = a sentence + `CHECK-SQL as <persona> <email>` … `verdict: PASS` fenced paste + a `| Record | Service class |
  Visibility path |` table.
- **Anchor names** come from the manifest (`anchors[].prompt_reference`, e.g. "Frederick's beta calendar ask", "my
  beta live-ops calendar sheet") — ≤6-word noun phrases.
- **Self-review** = `**Checks A–C walk**` table, touched-data census line, `**Counter-readings**` table
  (`| Category | Strongest counter-reading | Resolution (evidence) | Verdict |`, ≥7+n rows, each with an id/§/L<n>),
  `Unresolved: …`, the check-sql paste and the `LINT …` lines.

## Pitfalls (first-draft failures, in order of likelihood)

1. **Missing/extra NOT NULL columns** — copy each table's column list from the exemplar and add every non-nullable,
   default-less column. Do not include `*_fts`/generated columns.
2. **Timestamps past the freeze** — synth-cut bound is `2025-10-01T00:00:00Z`; every `created_at`/`updated_at`/`ts`/
   `date`/`internal_date`/`completed_at` must be ≤ it. GCal `start_ts`/`end_ts` and deadlines may be later (warning
   only); their `created`/`updated` may not.
3. **Linear text dates** written with a space, `+00`, milliseconds or a cast → `text_time_format` FAIL and sql_lint
   error.
4. **Slack ids** must be `sha256("<channel>|<ts>")[:32]`, `(channel,ts)` free in base and unique in SQL; replying into an
   existing thread without bumping `reply_count`/`latest_reply` is a Check C FAIL.
5. **Gmail copies** — own-mailbox copy from self needs `SENT`; otherwise the owner must be a recipient; `internal_date`
   must equal `date` in ms; `id`/`thread_id` need the mailbox prefix.
6. **GCal** — `ical_uid` `[0-9a-f]{32}@hg4`; `self:true` only on the calendar owner; `start_ts == start_json.dateTime`;
   `end > start`; every attendee with a calendar needs its own copy row (base_check) and attendees need invitation mails
   unless declared `no_notify`.
7. **Trello ids** must encode their own timestamp (`int(id[:8],16)` ≈ date ±1 day); badges/`dateLastActivity` must
   follow added comments/check items.
8. **GitHub PR comments** need the paired `github_timeline_events` 'commented' row (same `pr_id`, same `created_at`) and
   the review/comment id scheme; a mirrored-repo PR activity needs the Slack app copy (INT-01).
9. **Confluence** page versions must continue `1..N` and `confluence_pages.version` must be updated to the newest.
10. **Hazard touches** — modifying a state/lifecycle or referential hazard record FAILs base_check unless the ack says
    `repaired` **and** the post-SQL predicate passes; `excluded`/`dated_claim` never apply to a modified record.
11. **Branch words in prose** — any `release/…` or bare base-branch suffix in seeded text triggers base_claims; keep the
    deploy as calendar/chat evidence only.
12. **Fact leaks** — a per-record value with `home_ids` restated in a channel message, Linear description or sheet cell
    is a blocking `fact_leak`; keep one home row per per-record answer.
13. **Manifest ids must be literal in the SQL** — every `seeded_ids`, `decoy_seeded_ids` and `version_records[].id`
    (`seeded: true`) must appear verbatim (not in a comment); and every injected schema must be a `services` key
    (`no_orphan_injection`).
14. **Draft ids must survive** — dropping an anchor/trap/fragment/requirement without a `design_delta {id, change,
    reason}` fails `structure.design_delta`.
15. **Supersession order** — version records must be listed oldest-first with strictly increasing readable timestamps.
16. **Solver determinism** — sort keys, no set iteration in the output, no float formatting drift; `PYTHONHASHSEED 1/2`
    must agree. Return plain dicts/lists and JSON-safe scalars.
17. **Control operability** — every `over_application`/channel `degrade` must be accepted by `solve()` and must move a
    member value, and must not equal the rule ablation, else `contract.controls` FAILs.
18. **Surface-slot coverage** — each `direct`/`aggregate` slot's selector must resolve to a solver key/value; a key that
    the solver does not emit fails `contract.slots`.
19. **Golden evidence** — every sampled field needs `evidence()` ids that exist in the SQL `id` column, or a
    `base_route` (an unrouted base id is only "unverified").
20. **Manifest digests** — `solver.digest` must match the file (first 12 hex compared) and the path must resolve to the
    solver actually checked; regenerate after any solver edit.
21. **Stale preflight** — the preflight binds five files by sha256; run it **after** the last edit, then run stage_gate
    (which re-checks freshness). Any later edit re-opens it.
22. **Pasted numbers** — `errors: 0  warnings: N`, `total rows: N`, `HARDNESS GATE (extreme): PASS`, `FACT CHECK: PASS`,
    `BASE CHECK …: PASS`, `BASE CLAIMS …: PASS` must match the re-run exactly; the hg.py lint sha256 must equal the
    current SQL.
23. **CHECK dispositions** — one `LINT <check> L<line>: …` line per CHECK flag, in the Self-review, keyed by the flag's
    own line.
24. **Anchor naming** — imperative verbs ("find", "list") or >6 words fail `boundary.anchor_naming`; the gate reads the
    manifest's `prompt_reference` too.
25. **Self-review depth** — fewer than `7 + intended-disagreements` evidenced counter-readings, or a missing "Unresolved"
    line, fails.

## Exact command sequence

```bash
cd /Users/sumitkumar/Source/Outlier/OC
T=Task_Authoring/task_inputsS
python3 Task_Authoring/tools/sql_lint.py            $T/01_Universe_Inject.sql
python3 Task_Authoring/tools/base_check.py          $T/01_Universe_Inject.sql --manifest $T/Working_Files/01_Hardness_Manifest.json
python3 Task_Authoring/tools/base_claims.py         $T/01_Universe_Inject.sql
python3 Task_Authoring/tools/hg.py lint             --task-dir $T
python3 Task_Authoring/tools/fact_check.py          $T/01_Universe_Inject.sql --manifest $T/Working_Files/01_Hardness_Manifest.json --no-leak
python3 Task_Authoring/tools/hardness_gate.py       $T/Working_Files/01_Hardness_Manifest.json $T/01_Universe_Inject.sql --profile extreme
python3 -B Task_Authoring/tools/oracle_kit.py check --task-dir $T
python3 -B Task_Authoring/tools/oracle_kit.py truth --task-dir $T --out $T/Working_Files/truth.json
python3 -B Task_Authoring/tools/difficulty_mutation.py mutate   --task-dir $T --dispositions $T/Working_Files/01c_Dispositions.json
python3 -B Task_Authoring/tools/difficulty_mutation.py geometry --task-dir $T
python3 -B Task_Authoring/tools/trap_liveness.py    --task-dir $T
python3 -B Task_Authoring/tools/hardness_forecast.py forecast --task-dir $T --model <M> --preregister --freeze $T/04_Prompt.txt --freeze $T/Working_Files/01_Hardness_Manifest.json --freeze $T/Working_Files/truth.json
python3 -B Task_Authoring/tools/preflight_report.py --task-dir $T --forecast <forecast.json>
python3 Task_Authoring/tools/stage_gate.py injection $T --paste
```

(Order matters: preflight last before the gate, because it binds the five files by sha256; `stage_gate --rerun all`
re-runs sql_lint, base_check, base_claims, hardness_gate, fact_check, oracle_kit and geometry, so a stale paste or stale
digest is caught there.)
