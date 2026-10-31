# 01 — Universe Injection (Playbook) — HarmonyGames · Spec V2 · effective profile (extreme by default)

> Command: `/create-injection` · Writes: `task_inputs/01_Universe_Inject.sql` + `task_inputs/Working_Files/01_Grounding_Dossier.md` + final `task_inputs/Working_Files/01_Hardness_Manifest.json` + `Working_Files/solver/solver.py` + `Working_Files/01c_Dispositions.json` + `Working_Files/01c_Preflight_Report.json` (+ `.md`) · Checks: `tools/sql_lint.py`, `tools/base_check.py`, `tools/fact_check.py`, `tools/persona_view.py check-sql`, `tools/hardness_gate.py`, `tools/oracle_kit.py check`, `tools/difficulty_mutation.py`, `tools/preflight_report.py`, **`tools/stage_gate.py injection` (blocking)**; advisory (UNCALIBRATED): `tools/trap_liveness.py`, `tools/hardness_forecast.py --preregister` · Paired eval: `/injection` · Read first: `setup/GEN_EXECUTION.md`, `references/Hardness_Mastery.md`, `references/Ask_Carriers.md`, `plans/Fold_Hardening_Into_Scenario_And_Injection.md` §4.5

## Purpose

Implement the approved `01_Scenario_Design.md` as a long, deep, coherent injection: the
cohort spine's evidence, the hidden authorities and their decoys, the delegation lattice
spread across 10–13 services and dozens of containers, every chain and trap — as literal SQL
a reviewer can re-apply to a fresh environment. Then prove, mechanically, that the SQL is
what the design claims (`sql_lint.py` + `hardness_gate.py`).

If `01_Scenario_Design.md` does not exist, run `/create-scenario` first. If implementation
shows the design is wrong (an anchor is unreachable, a shortcut exists, a record would break
coherence), update the design and its draft manifest, re-run the design gate, then continue —
never silently weaken the design inside the SQL. A change made only in the final manifest is
recorded in its `design_delta` (`{id, change, reason}`); the gate fails a draft id that vanishes
without one.

**Revisions.** `/create-hardening` is revision N+1, not an input of this stage: it edits the SQL,
final manifest and dossier, re-runs `stage_gate.py injection --paste`, then `stage_gate.py hardening`,
whose gate re-runs the injection checks on the revised files and certifies their digests. Optional
outputs of later stages (reference files, error/async configuration, the hardening report) are never
inputs of this stage — their gates need an injection PASS, so consuming them would make a freshness
cycle (red team A, R1 #18).

**Loop.** An SQL-level fix stays here: re-run S4b–S5e and the gate. A design-level fix returns to `/create-scenario`
with a `design_delta`. Revision N+1 is this stage run again, against the previous revision's SQL and truth
(`oracle_kit.py check --previous-sql --previous-truth`).

This stage never drafts prompt, Oracle Event or criterion text (GEN_EXECUTION §2). What the
human needs goes into the dossier as structured facts.

## Inputs / Output

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`
and read `Working_Files/00_Task_Context.json` (GEN_EXECUTION § 0). Use all eight
assignment fields and the context's registered universe/KB source (`universe.key`, the `freeze_utc`
seed bound, `source.kb_status`). The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is missing — there is no default. Check each relied-on fact at that universe's seed bound; the KB is authoritative data only when `kb_status` is `bound`, otherwise its summaries are leads.
V3 changed-topic rules take
precedence over the older V2 reference documents in `references/Docs/`; local authorship and hardness-profile
exceptions remain as recorded in GEN_EXECUTION § 2 and § 3a.

Inputs
- `task_inputs/00_Assigments.md`, `01_Scenario_Design.md`, the draft `01_Hardness_Manifest.draft.json`, the gradable
  surface `01_Gradable_Surface.json` (read only: this stage never rewrites it).
  Nothing else from `task_inputs/`: reference files, error/async configuration and hardening outputs come later.
- `references/Ask_Carriers.md` — carriers, companion-field integrity, ID derivation, quoting, SQL skeletons.
- `references/Native_Artifact_Anatomy.md` — voice, length, naming per service.
- `references/universe_schema_live.json` — **private** column authority (144 tables, exported from the platform DB on 2026-10-04 with `setup/extract_schema.sql`). Do not paste it into `/injection`: supplied definitions become binding there; the eval compares against its own 58-table snapshot (advisory).
- The universe through `Task_Authoring/tools/hg.py search` / `tools/hg.py records`; persona identity from `Evals/references/persona/roster.json` (17).

Output
- `task_inputs/01_Universe_Inject.sql` — line 1 exactly `-- Are you planning to inject? Yes` (or `No`); a short header (persona + roster email, horizon, services, statement counts); statements grouped by service in dependency order. No scenario spoilers or self-validation in the SQL.
- `task_inputs/Working_Files/01_Grounding_Dossier.md` — grounding blocks 1.A–1.F · record ledger · findability and discovery-order proofs · self-validation table · integrations and companions · touched-data census and coherence hazards · intended disagreements · constraints for the prompt brief · **Facts for the human** · fact sheet · platform follow-ups · Self-review (tool outputs verbatim). The gate looks these headings up by name.
- `task_inputs/Working_Files/01_Hardness_Manifest.json` — the final manifest: the draft's ids (any change listed in
  `design_delta`), the same `effective_profile`, plus everything only the SQL can settle (delegation quotes,
  version timestamps, `facts` with `home_ids`), the `mechanism_portfolio`, and `solver {path, digest}`,
  `gradable_surface` and `preflight {report, digest}`.
- `task_inputs/Working_Files/solver/solver.py` (S4b) — the task's solver (`tools/oracle_kit.py` contract); it owns
  truth: `solver/truth.json`, every total in the dossier and in Facts for the human, and later the OE / rubric
  expected values come from it (`Hardness_Mastery.md` §2.6 item 14).
- `task_inputs/Working_Files/01c_Dispositions.json` (S5b, S5c) — your written disposition for every mutation result
  and every liveness flag.
- `task_inputs/Working_Files/01c_Preflight_Report.json` (+ `.md`, S5e) — written by `tools/preflight_report.py`, bound
  by sha256 to the SQL, solver, surface, manifest and dispositions it checked.
- `task_inputs/Working_Files/run_forensics/<rev>/01_Universe_Inject.sql` (S5e) — this revision's SQL, stored byte for
  byte and never edited: revision binding compares every run against every stored revision.

## Hard gates

1. **Design implemented, not re-invented.** Every manifest element maps to concrete records; every injected record maps back to a manifest element (no orphan rows — padding).
2. **Breadth and length at the effective profile.** The manifest's `effective_profile` (set by `/create-scenario`, never re-chosen here) sets the thresholds: extreme ≥ 10 of 13 schemas injected, ≥ 120 rows; normal ≥ 6 schemas, ≥ 50 rows, budget 60–100; the gate's other thresholds hold (`references/Hardness_Manifest_Spec.md`). `hardness_gate.py` reads the profile from the manifest and fails a disagreeing `--profile`.
3. **No dossier, no SQL.** Every claim in the dossier cites a service file + JSON pointer or ID. A fabricated citation fails the dossier.
4. **Assigned freeze.** Every seeded created/sent/updated/ts value and any claimed completed event must be at or before the shared context's `freeze_utc`; nothing after it is treated as completed. Calling a record "scheduled" does not exempt its event timestamps; later dates are allowed only for plan fields (due, scheduled start/end, deadline). A current mutable body edited later needs dated history or before-bound evidence for its earlier state (`Evals/0_Injection_Quality_Eval.md` Check C).
5. **Reproducible.** Literal values only (no `NOW()`, `random()`, generated UUIDs); explicit IDs; parents before children; UPDATE/DELETE keyed on primary keys; no procedural `DO` blocks.
6. **Schema-aligned** to the live schema, line by line; NOT NULL columns supplied (374 NOT NULL columns, only 4 defaults in all 144 tables); generated `*_fts` columns never written; reserved words and camelCase quoted (`"references"`, `"primary"`, `"desc"`, every Trello camelCase column, every Snowflake `wh_` column in UPPERCASE).
7. **Precedence (carrier eligibility — the same statement in every playbook).** Load-bearing facts only in ● carriers of `Ask_Carriers.md` §5 **as amended by §6b** (verified tool behaviour, which supersedes §5 and `Hardness_Mastery.md` §2.2). §6b verifies that injected **Linear comments render** through `linear_list_comments` with no bulk alternative, so Linear comments are a **● load-bearing per-record carrier** (the strongest one). The remaining ○ carriers (GCal description, Slides notes, Contacts description, Drive `content_text`, Slack file `content_inline`) hold supporting detail only until §6b verifies them; their rendering is a platform follow-up confirmed in the Opus pre-check before any criterion depends on them.
8. **Reachable from the persona's view.** Gmail: a copy in the persona's mailbox (`user_email` = persona, persona-prefixed message and thread ids). Slack: persona in `members_json`. GCal: one event row per attendee calendar with `self:true` on the owner's copy. Drive family: owner or `shared_with_emails_json`. Universe Explorer and `hg_search` never prove reach.
9. **Coherent.** No new inconsistency in any touched record; designed disagreements are dated human claims or stale versions overturned by later records, listed under intended disagreements. Companion fields updated (§S4).
10. **Findable in the designed order.** Every first link findable by a broad search; every dynamic-change seed has a discovery-order proof; every hidden authority findable by searching its own name; every decoy reached first by the path Opus takes (Confluence/Slack first-hit searches).
11. **Not pre-solving.** Seed rules, evidence and claims — never totals, classifications, the register, or the answer.
12. **Facts declared, consistent and not leaked.** Declare every load-bearing fact (amounts, dates, counts, names, statuses, ids, versions) in the manifest's `facts` field (`references/Hardness_Manifest_Spec.md`); give every per-record fact its `home_ids` (the per-record carrier rows). `tools/fact_check.py --no-leak` verifies them against every text the SQL writes and fails a per-record value that also appears outside its home rows — above all in bulk-readable rows (Slack messages, Linear issue descriptions, Sheets cells, Confluence bodies). Its PASS output goes in the dossier's fact sheet.
13. **Stage gate.** `tools/stage_gate.py injection` PASS; handoff is blocked until it passes.
14. **Friction-compatible.** The task stays solvable without any tool `03_Error_Async_Config.txt` kills. (Evidence: forced errors and async waits do not make Opus fail — every run routed around them. Use them only to add realism.)
15. **Solver contract** (S4b, blocking, `solver.contract`): deterministic; reproduces the previous revision's truth on
    the previous SQL; rules ↔ `mechanism_portfolio` one-to-one; every direct and aggregate surface slot produced; golden
    values spot-checked against their records.
16. **Every mutation result dispositioned** (S5b, blocking, `mutation.dispositions`): each KILLED / WEAK / SURVIVED /
    EQUIVALENT rule or degrade mutant and each intervention carries a written disposition — EQUIVALENT is never
    auto-labelled FALSE.
17. **Geometry can reach the cap** (S5b′, blocking, `geometry.upper_bound`): the flippable-weight upper bound U must
    exceed 1 − cap. If it does not, no supported failure state of the designed mechanisms can clear the cap: redesign the
    deliverables. When the solver is not composable (not key-local), U is no guaranteed bound: it reads UNVERIFIED and
    passes only with a written `geometry.U` disposition in `01c_Dispositions.json` (`"geometry": {"geometry.U":
    {disposition: accepted-unverified | redesign | solver-gap, reason}}`), never a BLOCK.

Advisory (UNCALIBRATED; never blocking): the geometry margin L_max, liveness flags (each with a written disposition),
optional blind probes, and the pre-registered forecast.

## Procedure

### S1 — Grounding dossier (before any SQL)

Open 2–3 real sibling records before mirroring any shape (`Native_Artifact_Anatomy.md` is the index).

- **1.A Structural** — per affected table: live-schema columns (NOT NULL marked), data location + pointer, base count, 3 verbatim sample IDs, enums seen, timestamp format, export-field → column mapping (export `links` = `links_json`, `user` = `user_id`, …).
- **1.B Entity** — per person/channel/game/ticket/PR/doc/figure referenced: canonical spelling, every service it appears in (cited), value in each, `AGREE` / `DISAGREE (pre-existing: avoid or document)` / `DISAGREE (designed)`. Traps: three Marcuses + Oscar Bennett; Thomas vs Thomas Baker; `ENG-####` vs `ZOM-###`; Frederick Stone's GitHub login shows "Ryan".
- **1.C Voice and realism** — per author: 3 quoted real messages, length band, capitalisation, emoji, sign-off, and posting hours (retain raw UTC; human-facing dates Pacific plus UTC when days differ). For **every seeded speaker** (Slack `user_id`, Gmail sender, Linear/Confluence author, PR comment author, Trello member) one line naming the person or email with its `status_at_clock` from the registered source's `activity.json`, verified at the assigned freeze — the gate lists the speakers from the SQL and checks each line. Take lengths, posting hours, subject/title prefixes and branch/PR title patterns from `references/universe_kb/conventions.json` (`slack.length_chars_by_channel_type`, `slack.per_person_hours_and_style`, `gmail.internal_subject_len_chars`, `linear.title_prefixes_by_team`, `github.pr_title_patterns` / `branch_patterns`, `gcal.duration_min`) and cite the key used.
- **1.D Keyword** — per search term: hit count + pointer, or `NEW TERM — introduced in <records>, reached via <anchor>`. A bounded miss (`scan_complete:false`) proves nothing.
- **1.E Persona reach** — per scoped record: service class + visibility path with a citation. Write every load-bearing record id (seeded and base) one per line to a scratch file and run `python3 Task_Authoring/tools/persona_view.py check-sql <persona> Task_Authoring/task_inputs/01_Universe_Inject.sql --load-bearing <file>`; paste the output (verdict PASS) under 1.E. The gate re-runs the check on every scoped id in 1.E, in Facts for the human and on rows marked `LB`. Required evidence must be YES. A designed denial (`DENIAL-INTENDED: <reason>`, NO) or an unverifiable record (`UNVERIFIED-OK: <reason>`) is a probe, never load-bearing: the row carries no `LB` and lists `alternate_evidence_ids: <ids>` that are YES; the manifest lists it in `denied_probes` and cites it only from traps or decoys. UNVERIFIED never satisfies a required dependency.
- **1.F Collision** — **identity tokens first**: header tokens (`PERSON_n_EMAIL`, `EMPLOYEE_00NN_SLACK_ID`) and body-text tokens (`[PERSON_NAME_n]`) are separate identity spaces; a new external person needs an unused header token (grep all three data folders for it: 0 hits) and must not reuse a token that already belongs to someone else. Then per minted ID: `python3 Task_Authoring/tools/hg.py search lookup <svc> --ids-file F --file <glob over the full collection>`, require `scan_complete:true` and 0 hits; format matches 1.A samples.

### S2 — Record ledger (from the design's record plan)

One row per record to insert or update: `# · service · table · id · container · manifest element (fragment/authority/trap/chain/cohort) · carrier ●/○ (hard gate 7's eligibility: §5 as amended by §6b — a Linear comment is ●) · reach path · discovery role (first link / connecting / overturning / decoy / write target)`. This ledger is what the gate's "no orphan injection" and "seeded ids exist" checks enforce.

### S3 — Findability, discovery order, hidden-authority proofs

Per seeded record:
```
Record:              <schema.table · id>
Agent's likely query: "<terms>" via <service> search/list
Term present:        hg_search search <svc> "<term>" -> <pointer>
Competing base hits: <count>; reachable via <recent date | live thread | distinctive co-term>
Chain position:      first link | connecting | terminal
```
Per dynamic-change seed: claim met first · overturned by · why met first · why decisive.
Per hidden authority: name → `hg_search` result for that name in its home service; decoy →
the first-hit path that reaches it (e.g. Confluence search on the topic word) and the
decisive clause on which it differs.

### S4 — Write the SQL (service recipes; skeletons in `Ask_Carriers.md` §6)

- **Slack.** `id` = `sha256('<channel_id>|<ts>').hexdigest()[:32]`; `ts` has 6 decimals and is unique per channel (collision-check `(channel, ts)`). A thread reply needs the parent's `reply_count`, `reply_users_count`, `latest_reply` updated (and `thread_parent_id` per the encoding confirmed in `Ask_Carriers.md` §7 SELECT 1). Membership changes update `members_json` and `num_members` together. Put decisive facts in **thread replies** (A14) and keep the parent sounding conclusive where the design calls for A1.
- **Gmail.** One `gmail_threads` row + one message row **per mailbox copy you seed** (sender copy labelled SENT, recipient copies INBOX). The base does *not* hold a copy in every participant's mailbox (≈ 20 % coverage), so a missing non-persona copy is not a defect; a copy whose owner is neither the sender nor in To/Cc/Bcc is. Ids are `<mailbox>/<RFC Message-ID>` (`<…@…>`) and `<mailbox>/<numeric thread id>`; replies carry `in_reply_to` = the parent's bare Message-ID (`<…@…>`, a message in the same mailbox), `"references"`, a later `date`, "Re: ". `internal_date` (ms) equals `date`. Persona must hold a copy of every message it needs. **Load-bearing mail is INBOX or SENT** in the persona's copy — never SPAM/TRASH (search defaults may skip them; base mail from the same sender may sit in SPAM — check and say so in the dossier).
- **GCal.** One event row per attendee calendar, shared `ical_uid`, `self:true` on each owner's copy; start < end; cancellations via `status`; deadlines may be after the clock only as future events. Load-bearing facts in time/attendees/status, not `description` (○). **Notification choice:** base data carries "Invitation" / "Updated invitation" emails for many events. Decide per seeded event whether the organizer notified attendees: if yes, seed the matching Gmail copies (and accept that the time/date now appears in a mail subject); if no, seed none and state it — a calendar-only fact must not leak into a subject line.
- **Drive / Docs / Sheets / Slides.** The Google file id (`f_` + 22 hex) is the same in `drive_files` and the Docs/Sheets/Slides row, with identical sharing; folders are `d_`. Spread Sheets facts across **separate spreadsheets** (one `values_batch_get` would collapse tabs). Slides: decisive figure in element text (●), not notes (○). Bump `modified_time` on both rows when editing.
- **GitHub.** Continue per-PR suffixes (`#c_N`, `#rev_N`, `#rc_N`, `#ev_N`); every PR comment needs a matching `commented` timeline event; bump PR `updated_at`; `seq` NOT NULL. Ids are `<pr_id>#c_<n>` / `#rev_<n>` / `#rc_<n>` / `#ev_<n>`. File contents are git packs — not SQL-injectable; carry code facts in review comments (`diff_hunk`) instead. No GitHub issues in base (○). **Mirror rule:** every seeded PR comment or review in GameOfDominoes, game-of-dominoes-backend or match3d also needs its Slack copy (bot message with the base attachment shape) in `#engineering-bots` `C050WGU41HR` / `#zombie-prs` `C093LEZGF6J` at the same time — copy the shape of an existing mirror message.
- **Linear.** `id` = `identifier` = `<KEY>-<next number>` (highest: ART 792, DES 312, ENG 2437, EPI 28, ZOM 672); `team_<KEY>`; users exist in `linear_users`; varchar ISO-Z timestamps; keep `links_json` = `[]` (no lone Linear↔GitHub bridge — the missing link is real friction). Comments have no base rows, but injected comments **render** through `linear_list_comments` (verified in V1 trajectories, `Ask_Carriers.md` §6b) and no list call returns them — the strongest per-record surface, and a ● load-bearing carrier under hard gate 7 (no platform follow-up needed). Keep the per-record finding out of the issue's `description` and title: `linear_list_issues` returns those in bulk (a `fact_leak` under `--no-leak`). Each comment row: `id`, `issue_id`, `author_id` (a real `linear_users` id), `parent_id` NULL or a comment id, `body`, timestamps after the issue's `created_at`; bump the issue's `updated_at` to at least the newest comment. Lifecycle stamps follow the state (Done ⇔ `completed_at`; Canceled/Duplicate ⇔ `canceled_at`; Todo/Backlog none; created ≤ started ≤ completed ≤ updated), including after an UPDATE of `state_id`. A comment dated after the issue closed reads as "Closed with later activity" (QC appendix) unless it is a neutral note or a dated claim the task resolves — disposition each.
- **Trello.** Mint ids whose first 8 hex digits are the record's Unix seconds; comments are `commentCard` actions with the full `data_json` shape; update `badges_json` (comments, checkItems, checkItemsChecked — full base shape, never `'{}'`) and `"dateLastActivity"`; checklists name the card's own board; `idShort` unused on the board; board activity thins by late 2025, so posts near the selected clock stand out, which suits a hidden authority (A12).
- **Confluence.** An edit = UPDATE the page (body, version, `updated_at`) + INSERT version N+1 with the same body/title and an edit message; versions contiguous 1..N; every `ri:content-title` link names an existing page; mark `-- re-verify after regeneration`.
- **Snowflake.** Tables `snowflake.wh_<db>__<schema>__<table>`, UPPERCASE quoted columns; keep mirrored tables in step (AD_SPEND/AD_SPEND_DAILY/UA_SPEND_UNIFIED_V2; REVENUE_DAILY/_V2); update table comments that quote counts. Prefer not to make a Snowflake **insert** load-bearing (data is being regenerated); its value is that figures must be *derived* (A19).
- **Contacts.** `last_name` NOT NULL (`''` allowed); keep records sparse like the base (`job`, `email`).
- **Companions.** For every seeded record whose service has an automated mirror, look it up in `references/universe_kb/integrations.json` and seed the companion with the exact `shape` inside the integration's active `window`, at its base rate (e.g. `INT-01` GitHub app → `#engineering-bots` only for GameOfDominoes, backend and match3d in their windows; `INT-11` invitation mails; `INT-03` linear[bot] PR comment). Record each decision in the dossier's **Integrations and companions** table (service · INT id · companion seeded or none · reason).
- **Text.** Match 1.C voice: varied length, fragments, half-answers, typos where the author has them. No AI tells, no tidy completeness, no em-dash-heavy prose in casual channels. Seed claims and evidence, never conclusions.

### Eval checks A–C (`task-quality-v1`; `Evals/0_Injection_Quality_Eval.md`)

These are the eval's rules, not `sql_lint.py`'s; both sets must pass.
- **No grader-facing or padding text** (Check C): nothing addressed to a solver or grader or describing the test ("This description does not state them."); no comment about tool calls, pass rate, traps, rubric, hardness, baselines or ground truth; every record needs a task purpose.
- **Drive readable** (Check A): a Google Doc needs a `docs_documents` row with non-empty `body_text`; a file's `content_path` points at real bytes as `<owner_email>/<path>`, with no leading `/` or `root/`; `content_text` alone is not served.
- **One account per person per service** (Check A); Gmail `history_id` is digits or NULL and `content_path` follows the form above (`Evals/references/schema/id_contracts.json`).
- **Generated columns** (Check B): `gmail.gmail_messages.body_text_fts` and `slack.slack_messages.text_fts` never appear in INSERT or UPDATE.
- **Linear text dates** (Check B): exactly `YYYY-MM-DDTHH:MM:SSZ`, dates `YYYY-MM-DD` — no space, offset, milliseconds, `::timestamptz`, CAST or `now()`; a new issue sets `state_history_json` = `'[]'`.
- **Actor ids** resolve to the person the record names (Gmail `from_email`/`from_name`, Trello `idmembercreator`/`memberCreator`, GitHub `author_login`/`author_name`).
- **Reachable evidence**: every seeded deciding fact is prompt-linked, readable as content and outside Gmail Trash/Spam — never only inside a Gmail or Slack attachment (metadata only).
- **Per-case rules** are seeded authority records; the prompt never carries an if-chain.

### S4b — Solver completion (blocking)
- [ ] Complete `Working_Files/solver/solver.py` from the design's `mechanism_portfolio`: one rule per mechanism node,
      each with its natural-reading fallback, `load_state` (base records through `tools/hg.py`, SQL rows through
      `base_check.parse_sql` — never executed), `solve(state, disable, degrade, keys_)` with per-record ablations
      (`(rule, key set)`), `aggregates`, `evidence`, and where possible `touched`, `deciding` and the `DEGRADES`
      operators (`tools/oracle_kit.py` docstring). Declare what the design has, so the tools can see it:
      - **Controls.** A rule's control members, and the operator that over-applies the rule to them (`controls`,
        `over_application`). `node_verdicts` reports each written control as a control trial (OVER-APPLIED or
        HELD), never a landing.
      - **Complexity channels** (`CHANNELS`: `kind`, `degrade`, `members`, optional `latent` and `family`; or surface
        `slots` when the solver can't express the failure). Geometry U counts them, `node_verdicts` reports each per
        run, and the forecast models them.
      - **Base routes.** `base_route(record_id)`, so the golden check reads base records through `tools/hg.py records`.

      `contract.controls` checks that every declared control and channel is live.
- [ ] `python3 Task_Authoring/tools/oracle_kit.py check --task-dir Task_Authoring/task_inputs [--previous-sql <revision N-1
      SQL> --previous-truth <its truth.json>]` → PASS. Then
      `python3 Task_Authoring/tools/oracle_kit.py truth --task-dir Task_Authoring/task_inputs --out Task_Authoring/task_inputs/Working_Files/solver/truth.json`.
- [ ] Every total in the dossier and in Facts for the human comes from `truth.json`. Spot-check the golden values the
      contract lists as unverified (base records) through `tools/hg.py`.
- [ ] Record `solver {path, digest}` in the final manifest.

### S5 — Validate

- [ ] `python3 Task_Authoring/tools/sql_lint.py Task_Authoring/task_inputs/01_Universe_Inject.sql` → 0 errors; every warning dispositioned in the dossier.
- [ ] `python3 Task_Authoring/tools/base_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql` → PASS (the `/injection` Checks A + C against the base data; resolve every warning or justify it in the dossier).
- [ ] `python3 Task_Authoring/tools/hg.py lint --no-base` (drop `--no-base` once the universe data is installed) → the eval's `hg_injection_lint.py` on this SQL: fix every FAIL, disposition every CHECK in the Self-review, note every INFO. It exits 0 even with FAIL flags — read `counts.FAIL` and `flags[]`, never the exit status. Write one Self-review line per CHECK flag as `LINT <check> L<line>: <disposition and evidence>` (a grouped flag names its first line); the injection stage gate re-runs the lint with base data and blocks on any FAIL or undispositioned CHECK. `--no-base` cannot certify the base-dependent checks (identities, Drive bytes). A clean lint is not a PASS, and these are not `sql_lint.py`'s rules — keep all three tools.
- [ ] `python3 Task_Authoring/tools/fact_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql --manifest Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.json --no-leak` → PASS (declare every load-bearing fact in `facts`, per-record facts with `home_ids`; `tools/fact_check.py` verifies them). Paste the output in the fact sheet.
- [ ] `persona_view.py check-sql … --load-bearing <file>` → PASS for every load-bearing seeded record (1.E).
- [ ] Write the final manifest (every draft id kept, or listed in `design_delta`; each fragment's
      `delegation_quote` copied verbatim from its delegating record; each trap's `version_records` in the
      records' real time order; hazard acknowledgements with a verified `resolution`), then
      `python3 Task_Authoring/tools/hardness_gate.py Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.json Task_Authoring/task_inputs/01_Universe_Inject.sql` → PASS
      (profile from the manifest; no `--profile` needed).
- [ ] Self-validation table — every row holds. "Tool" rows are enforced by `sql_lint.py` / `base_check.py`
      (each rule measured at ~100 % in the base; proven by `support/examples/calibration/injection/mutation_matrix.py`);
      "Manual" rows are not mechanically checkable and need cited evidence in the dossier.

| QC category (`QC_Spec_Doc_Latest.csv`, `1_Prompt_Eval.md` §3.2) | Tool-enforced | Manual (cite evidence) |
|---|---|---|
| Missing Universe Data | — | every needed fact exists, persona-readable, reachable by a cataloged tool; killed tools have alternates |
| Temporal Field | on/after clock; created ≤ updated; replies after parents; Slack post not older than its channel; start < end; start/end_json = start/end_ts; Gmail internal_date = date; Linear stamps ordered; issue/PR updated_at ≥ seeded activity | **dates written in text** agree with the fields and with each other (a record must not cite a record created after it; "last month", "Q4" resolve to the right period) |
| Cross-service Referential | channels, users, issues, PRs, threads, calendars, cards, pages, parents resolve; `<@user>`/`<#channel>` mentions; Linear ids cited in text; `ri:content-title` links; Gmail in_reply_to; GCal copy on every attendee/organizer calendar; Docs/Sheets/Slides sharing = Drive row; shares name real people | the same person/figure/date spelled and valued the same in every service (names, amounts, file names); PR/ticket numbers cited in prose point at the record meant |
| Quantitative / Reconciliation | Slack reply counters; Trello badge counts | figures quoted in text match the source rows (sheet cells, Snowflake, invoices); totals sum; "same as last month" really is |
| State / Lifecycle | Linear state ⇔ stamps (incl. after UPDATE); badges/activity follow comments; Confluence versions contiguous, page.version = newest; warn: archived-channel posts, comments after an issue closed | a status contradicted by activity in another service (a ticket marked closed that later records show still in progress, or open when they show it finished; a person who "left" yet acts later); a commitment in text that the data never fulfils |
| Identifier / Format | Slack sha id; Gmail Message-ID/thread ids; Drive/Docs f_/d_ + 22 hex; GCal evt_ + ical_uid 32hex@hg4; GitHub `#c_/rev_/rc_/ev_<n>`; Trello timestamped ids; Linear id = identifier = team + number; collisions; duplicate keys; valid JSON in every `*_json` column | emails/ids copied verbatim from the base; no second naming scheme inside a service |
| Semantic / Category | — | labels, list names, channel purpose, doc titles match the content; one name per entity; deliberate dual naming listed for the human |
| Other | — | voice matches; nothing reads as planted; no record states the conclusion |

- [ ] **Self-review** (S7) written into the dossier.
- [ ] Lazy-solver pass on the implemented records (first hits, no threads, bulk shortcuts, stop at the first conclusion) — fix every point it scores.
- [ ] Local red team (recommended): `python3 Task_Authoring/tools/redteam_review.py --mode redteam --dual --in Task_Authoring/task_inputs/Working_Files/01_Grounding_Dossier.md --in Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.json --out Task_Authoring/task_inputs/Working_Files/01b_Redteam_Review.md`.
- [ ] **Stage gate (blocking):** `python3 Task_Authoring/tools/stage_gate.py injection Task_Authoring/task_inputs --paste` → `STAGE GATE injection: PASS`. It re-runs `sql_lint`, `base_check`, `fact_check --no-leak`, `hardness_gate` (at the manifest's `effective_profile`) and `persona_view` and compares them with the pastes, requires the upstream scenario PASS to be current, the final manifest to keep every draft id or list it in `design_delta`, every anchor name to be a noun phrase of ≤ 6 words, a disposition line per `sql_lint` warning class, the KB citations and the self-review. `--paste` writes the PASS into the Self-review.

### S5b — Mutation and interventions (blocking: a written disposition for every result)
- [ ] `python3 Task_Authoring/tools/difficulty_mutation.py mutate --task-dir Task_Authoring/task_inputs` (plan §7.2):
      every rule ablation, rule × shard ablation, degrade, and the exact whole-mechanism combination table (k ≤ 8, else
      UNSUPPORTED; `--max-k N` above 8 runs only with `--allow-max-k N`, an explicit override disclosed in the output,
      the same in `hardness_forecast.py` and `preflight_report.py`), each diagnosed KILLED / WEAK / SURVIVED / EQUIVALENT on the gradable surface; plus one intervention per
      node (its injected deciding records removed from an in-memory copy of the SQL): load-bearing, inert, or escaped
      (a record outside the node's closure changed — undeclared coupling).
- [ ] Write a disposition for every rule mutant, degrade mutant and intervention in `Working_Files/01c_Dispositions.json`
      (`{"mutation": {id: {disposition, reason}}}`; dispositions `live`, `weak-accepted`, `redesign`, `retire`,
      `redundant`, `masked`, `solver-gap`). EQUIVALENT may be a FALSE trap, a redundant rule, a masking interaction or an
      incomplete solver: the author decides which.

### S5b′ — Geometry (U blocking, L_max advisory)
- [ ] `python3 Task_Authoring/tools/difficulty_mutation.py geometry --task-dir Task_Authoring/task_inputs` (plan §5):
      U = the weight share the designed mechanisms can flip (every per-record ablation subset, aggregates fed by a
      changeable record, degrades, the degrades of declared complexity channels; delivery slots never). U ≤ 1 − cap
      blocks; on a solver that is not composable U is UNVERIFIED and needs its `geometry.U` disposition (gate 17).
      L_max (the largest loss over whole-mechanism combinations) below (1 − cap) + 0.10 warns.

### S5c — Liveness flags (advisory; each flag dispositioned)
- [ ] `python3 Task_Authoring/tools/trap_liveness.py --task-dir Task_Authoring/task_inputs` on the SQL; write a
      disposition per flag under `"liveness"` in `01c_Dispositions.json`. Redesign the difficulty; never remove a fairness
      link.

### S5d — Blind probes (optional, advisory)
- [ ] `tools/judgment_probe.py` when it exists (plan §7.4); results enter the ledger with `source: probe` and stay apart
      from platform evidence.

### S5e — Forecast (advisory, UNCALIBRATED, pre-registered) and the preflight report
- [ ] `python3 Task_Authoring/tools/hardness_forecast.py forecast --task-dir Task_Authoring/task_inputs --model <baseline
      model> --preregister --out Task_Authoring/task_inputs/Working_Files/01c_Forecast.json` — priors per model from the
      ledger (another model only through a transfer record: TRANSFERRED · UNCALIBRATED), exact solver outcomes, 10,000
      simulated six-run baselines through `difficulty_stats.compute()` per scenario. Its ledger id is written before the
      platform run; nothing changes after. Declared channels take their rates from the model's ledger records of their
      family; a channel with none needs a disclosed `--channel-rate <channel>=<e>`, otherwise it prints UNPARAMETERIZED
      and is not simulated. The forecast also reports each slot's P(fail) and P(fails all six); the latter is all-fail
      justification workload, never a block.
- [ ] `python3 Task_Authoring/tools/preflight_report.py --task-dir Task_Authoring/task_inputs --forecast Task_Authoring/task_inputs/Working_Files/01c_Forecast.json`
      → writes `01c_Preflight_Report.json` + `.md` (solver contract, surface validation with expected values and
      `flipped_by`, mutation with dispositions, geometry, liveness, forecast). Record `preflight {report, digest}` in the
      final manifest. Any later edit to the SQL, solver, surface, manifest or dispositions makes it stale.
- [ ] **Store the revision.** Copy the final `01_Universe_Inject.sql` byte for byte to
      `Working_Files/run_forensics/<rev>/01_Universe_Inject.sql` (`<rev>` = this revision's label, e.g. `rev3`) and
      never edit that copy. A run is bound to a revision only on content the other stored revisions don't hold, so
      every later intake passes every stored revision (`--sql <rev>=<its copy>` for each
      `Working_Files/run_forensics/*/01_Universe_Inject.sql`); with one SQL alone the binding is INSUFFICIENT.

### S5f — Early target-model runs (advisory; after S5e, before `/injection`)
- [ ] Run 1–2 Opus 5.5 trajectories of the full build in the independent harness, configured like the platform (Claude
      Code version, effort, subagent policy).
      - Store them under `Working_Files/run_forensics/<rev>/early/`, never in `06_*` or `07_*`.
      - They are ledger evidence (`source: independent-harness`), never the platform pre-check.
- [ ] Take each one in with `01a_Hardening.md` MODE B (pre-check) steps 1–4, passing every stored revision with
      `--sql` (the task's first revision has no other: then `--sole-revision "<why this is the only revision>"`, which
      the tools refuse while another revision is stored). A run that is not BOUND on evidence (INSUFFICIENT,
      AMBIGUOUS, UNBOUND) is not evidence for this revision. Confirm every failed slot against the run's write payload.
      Record one verdict per mechanism in the dossier.
- [ ] **Keep or replace.** Keep channels that fail in Opus 5.5's own decisions (designed mechanisms that land, or
      declared complexity channels that fail), and replace those that leak through `/create-scenario --revise`, then
      rebuild. Control errors and unattributed slips count for neither.
      - At most two cycles; after that, change the scenario rather than iterate.
      - Season Pass spent 14 revisions without target-model evidence (`Hardness_Mastery.md` §12).

### S6 — Hand-off sections of the dossier
- **Intended disagreements** — each designed contradiction, why it is realistic, what resolves it.
- **Constraints for the prompt brief** — an anchor-name table `Anchor · May be named (noun phrases only) · Record`: each entry a noun phrase of ≤ 6 words with no verb or imperative framing and no second-person request, synonyms separated by `;` (the gate blocks any other shape, `boundary.anchor_naming`; never a sentence the human could transcribe); what must never be named (locations of hidden authorities, async targets, IDs, root cause); deadlines; deliverable kinds.
- **Fact sheet** — the manifest's `facts` as a table (key · value · kind · must appear in) and the `fact_check.py` output verbatim.
- **Facts for the human** — one row per seeded or relied-on record (full record ids, never abbreviated with `…`): locator · base/seeded · fact (values, actors, UTC timestamps) · reach path · role (evidence · claim met first · overturning evidence · decoy · authority · alternate path · write target) · re-verify?
- **Platform follow-ups** — ○ carriers (hard gate 7; not Linear comments, which §6b verified) whose rendering must be confirmed in the Opus pre-check; Confluence/Snowflake figures to re-verify after regeneration. A `call_budget` row that depends on an unverified behaviour carries `conditional_on` and counts 0 until verified.

### S7 — Self-review (GEN_EXECUTION §6a, validity side) — recorded in the dossier under **Self-review**

1. **Tool outputs, verbatim.** Paste the final `sql_lint.py`, `base_check.py` and `hardness_gate.py` output blocks
   unedited (verdict, every finding, every warning); `check-sql` sits under 1.E and `fact_check` in the fact sheet. Each warning gets a one-line disposition with evidence; a
   FAIL blocks hand-off. Re-run both after every SQL change (§6a.4) and paste the final run only.
2. **Re-read as `/injection`.** Walk `Evals/0_Injection_Quality_Eval.md` Checks A–C in order against the
   SQL: inventory (every statement, insert/update/delete, upserts), A (references incl. archived/history
   records, uniqueness scoped to the full collection, ownership/membership/share identities, ID
   contracts), B (structure, literal JSON in JSON columns, generated/NOT NULL columns), C (dates,
   parent/reply, statuses, counts, amounts, claimed updates and superseding records). Mark each PASS /
   FAIL / PENDING with the record pointer; PENDING is never silently upgraded.
3. **Touched-data census.** List every base record the task touches — seeded records' neighbours, the
   records the asks route through, and every record a correct run must open (cohort members, the
   threads around seeded replies, tickets in the queues the prompt names, the PRs/channels that settle a
   status). `/prompt` §3.2 fails Cross-Service Coherence on an inconsistency in this data **even if it is
   pre-existing**. Match the census against `references/universe_kb/coherence_hazards.json` under a
   **Touched-data census and coherence hazards** heading: cite each hazard id that intersects it with a
   disposition, and write `<category>: none in scope` for a hazard category with none (all six required).
   A State/Lifecycle or Referential hazard the task touches needs a `hazard_acknowledgements` entry with a
   **verified** `resolution`: `excluded` (records neither modified nor cited), `repaired` (the SQL fixes the
   fields and `base_check` re-evaluates the hazard on the post-SQL state — Linear L01–L07; other types FAIL
   as unverifiable) or `dated_claim` (text claims only — never a record the SQL modifies). An
   acknowledgement alone never turns the `base_check` FAIL into a warning.
4. **Counter-readings per coherence category** on that census, one row each (category · strongest
   argument it FAILS · evidence that resolves it · verdict):

   | Category | Counter-reading to test |
   |---|---|
   | Temporal | a date in prose (subject, body, sheet note) contradicts a field; a record cites something created after it; an event "already happened" after the clock |
   | Semantic / Category | a label, list, channel or title misdescribes the record; two records share a name in a way the task does not intend |
   | Cross-service Referential | the same person, amount or date differs between services; a cited ticket/PR/file/page is the wrong one or absent |
   | Quantitative | a quoted figure does not match its source rows; parts do not sum; "same as before" is not |
   | State / Lifecycle | a status contradicts before-freeze activity elsewhere, including sibling defects in scope. A second fair answer alone is not a failure: incorporate every fair result in acceptance; separately repair or exclude actual coherence defects |
   | Identifier / Format | an id copied from a sample with a changed scheme; an email typed by hand |
   | People status (platform /prompt F2, task-1 2026-10-05) | anyone whose presence a rule depends on ("still here", last day, left) must agree across Slack/Linear/Gmail activity, Snowflake `FINANCE.EXPENSES.PAYROLL_ROSTER` / `HEADCOUNT` (and their table comments / `snowflake_tables.row_count`) and Confluence headcount lines. HarmonyGames convention for staying on unpaid: a `$0` roster + headcount line to 2026-02-13 (payee counts unchanged; normal universe only — on synth-cut the line runs to the last payroll before 2025-10-01). A last day before payroll ends needs a stated notice period. Synthetic Snowflake/Confluence inconsistencies fail Cross-Service Coherence whoever introduced them. |
   | Other | the designed disagreement reads as two silent system fields rather than a dated human claim overturned later |

   For every designed disagreement also write the best argument that it is an *unintended*
   inconsistency, and why the records (dates, authors, later correction) support the designed reading
   (`0_Injection_Quality_Eval.md` Check C: "an author merely calling something a decoy does not resolve
   an actual contradiction").
5. **Re-verify facts, not notes.** Re-read each load-bearing value from its source with `tools/hg.py`
   (§6a.3); a value carried from the scenario design is a lead.
6. **Record** the final verdict per check, each counter-reading and its resolution, and anything left
   unresolved, named.

## Self-check (QC Spec V2 / Evals)
- Universe — Feasibility and Cross-service Coherence (fails on the inconsistency itself).
- `/injection` (`injection-static-v2`): complete inventory, full-collection collision coverage, no broken references, valid literal JSON in `*_json` columns, chronology — S7 records it.
- Contributes to `/prompt` feasibility, cross-service and pre-solved; and to the trajectory horizon via the call budget.

## Deliver
Run `python3 Task_Authoring/tools/stage_gate.py injection Task_Authoring/task_inputs --paste`; handoff is blocked
until it prints PASS. Report: the SQL path and row/schema counts (from `sql_lint.py`), the gate verdict, services
carrying weight, hidden authorities and decoys, chains, any red-team findings and their
disposition, the preflight (solver contract, mutation dispositions, U and L_max per gate view, liveness flags and
their dispositions, the pre-registered forecast id with its P(all gates) range — labelled UNCALIBRATED), and open
platform follow-ups. Next: paste the SQL into `/injection`; then
`/create-error-async` / `/create-reference-files` if designed; then `/create-prompt-writing`.
