
> **Two builds.** Per-universe KB outputs live in `by_universe/{normal,synthcut}/`, selected
> by the task context (`source.kb_output_path`; `source.kb_status` = `bound`) and rebuilt per
> `setup/GEN_EXECUTION.md` § 0a:
> `python3 Task_Authoring/tools/entity.py --task-dir <task_dir> build`, then
> `python3 Task_Authoring/references/universe_kb/_build/run_all.py --task-dir <task_dir>`.
> The `*.json` / `*.md` files in this directory are the legacy Feb-14 KB: reference-only,
> never written by the per-universe build. Counts, clock and dates below describe that
> legacy build unless they say otherwise.

## Persona view and entity resolution (`tools/persona_view.py`, `tools/entity.py`, `entities.json`)

Two deterministic, read-only, stdlib-only tools. Run them from the workspace root with `python3`.
The exact visibility rules and every UNVERIFIED case are in the docstring at the top of
`tools/persona_view.py`. The join rules are at the top of `tools/entity.py`.

**Persona view.** These commands read the base as one persona sees it, under the ACL in
`Evals/references/persona/acl.md`. The persona can be given as a `persona_key`, its exact
roster email or its exact name. The 19 personas come from `persona_roster_v2.json`. `thomas`
and `tim_steudler` are flagged as not usable in tasks.

```sh
python3 Task_Authoring/tools/persona_view.py personas
python3 Task_Authoring/tools/persona_view.py reach arthur_blake [--top 10] [--json]
python3 Task_Authoring/tools/persona_view.py can-see julia_lawson slack C080X4GTZ0E/1741568716.506519
python3 Task_Authoring/tools/persona_view.py can-see robert gcal evt_00009bfb80dabb15aa5bb5 --calendar martin.walsh@harmonygames.co
python3 Task_Authoring/tools/persona_view.py who-can-see gdrive f_00da0af9039fdf198986af
python3 Task_Authoring/tools/persona_view.py search simon_walker gsheets "retention" --limit 10 [--no-hidden]
python3 Task_Authoring/tools/persona_view.py check-sql arthur_blake task/01_Universe_Inject.sql --load-bearing ids.txt
python3 Task_Authoring/tools/persona_view.py --self-test
```

- **Verdicts:** every answer is YES, NO or UNVERIFIED, with a reason and evidence fields.
  Never cite UNVERIFIED as visible.
- **`search`:** reports how many hits the ACL hides and in how many containers. It does not
  show hidden content. A Gmail search with the hidden count scans every mailbox, which takes
  about 25 s or more. Use `--no-hidden` to search only the persona's own mailbox.
- **`check-sql`:**
  - Judges every row in a scoped service against the final state after the whole SQL has
    run, including UPDATEs to `members_json`, sharing and calendars.
  - The `--load-bearing` file takes one id per line. A listed id can name an SQL row or a
    base record.
  - Exits with 1 if a load-bearing row is NO. It also exits with 1 if a load-bearing row is
    UNVERIFIED, unless you pass `--allow-unverified`.
- **Caches:** derived caches are written to `Task_Authoring/support/local_search/cache/pv_*.json`.
  They are rebuilt automatically when a source file changes.

**Entity resolution.** `entities.json` holds one record for each person, bot, service
account or Drive `Resource:` owner. It joins:
- the two rosters
- Slack users
- Gmail mailboxes
- GCal calendars
- Drive users and share recipients
- Linear, GitHub, Trello and Confluence users
- Contacts

Every identity records how it was joined:
- `exact_email`
- `exact_name`
- `exact_name+username_localpart`
- `own_record`, when the record was not merged into another entity

Records that match more than one entity, or that only share a token number, are listed under
`unresolved`. They are never merged.

```sh
python3 Task_Authoring/tools/entity.py build                 # root entities.json (~3 s); with a task context, by_universe/<key>/entities.json
python3 Task_Authoring/tools/entity.py resolve "usr_Victor Barnes"
python3 Task_Authoring/tools/entity.py resolve marcus        # every Marcus, with join evidence
python3 Task_Authoring/tools/entity.py collisions            # traps: shared names, lookalikes, token conflicts
python3 Task_Authoring/tools/entity.py --self-test           # includes a check against Ask_Carriers §1
```

## Universe knowledge base: timeline, activity, hazards, traps, cohorts, integrations, conventions

Built by `_build/run_all.py` (stdlib only, read-only on every export, about 10 minutes, peak memory under 2 GB). Caches are written to `Task_Authoring/support/local_search/cache/kb_cache/`. Each `.md` file is rendered from its `.json` twin, so all numbers come from the generator. Clock (legacy root build): 2026-02-14T00:00:00Z. These files extend `Scenario_Atlas.md`, `Ask_Carriers.md` (§6a/§6b) and `Hardness_Mastery.md` §2.5–2.6. They do not repeat those documents.

| File | What it is | Use it when |
|---|---|---|
| `timeline.json` / `.md` | 48 dated spine events (2024 → 2026-02-13). Each event has verified evidence in 2+ services, and every id is re-read with its own timestamp. Also 175 storyline-YAML beats from 2024 on whose artifact ids verify in 2+ services. | Placing seeded records in the right era, and checking "X happened on D" before a prompt states it. |
| `activity.json` | One entry per `@harmonygames.co` person (41), keyed by email, with the Slack id. Gives first and last activity per service, monthly authored volume, Slack style, hour histograms, departure signals (channel leaves, last commit, last Linear action) and `status_at_clock`. `seed_voice_candidates_feb_2026` ranks the 10 people active in Feb 2026. | Choosing who may plausibly write a seeded 2026 message, comment or mail, and who must stay silent. |
| `coherence_hazards.json` / `.md` | 68 pre-existing inconsistencies in 6 QC categories (temporal, semantic/category, cross-service referential, quantitative, state/lifecycle, identifier/format). Each has a count, a denominator, up to 10 example ids, and keep-out guidance. It also lists what was checked and found clean. | Defining task scope: keep these ids out, or make the reconciliation the explicit job. |
| `trap_catalog.json` / `.md` | 31 natural traps: lookalike people, ENG/ZOM number twins, near-duplicate documents, stale vs current versions, superseded claims, struck-through retractions, bot noise, redaction, lookalike containers and renamed apps. Each has ids, the risk, and a legitimate use. | Designing A1/A12/A14 traps that already have base precedent. |
| `cohorts.json` / `.md` | 191 natural record sets of 40–500 records, each with its exact selection rule and count, full id lists, the per-record surfaces, whether a bulk call already returns them, and the hazard ids inside the set. | Picking the cohort spine (Hardness_Mastery §2) and budgeting honest per-record calls. |
| `integrations.json` / `.md` | 23 automated mirrors and integrations, each with its exact record shape (example Slack JSON and Gmail headers), active windows, and base rates for how often the companion record exists. | Seeding any PR comment or review, Linear key, build, Helpshift issue, invite or bot post, so its companions exist only where the base has them. |
| `conventions.json` / `.md` | Writing and id conventions: message length and tone by channel type, per-person working hours and style, Gmail subject and body norms, Linear states, labels and title prefixes by team, PR, branch and commit style, Trello lists and labels, GCal durations, document title families, Confluence version messages. | Writing seeded text, titles and timestamps that look native. |

**Six findings that change how tasks are designed**

1. **GitHub app mirror windows.** The mirror covers only GameOfDominoes (2023-04-14 → 2025-12-26), game-of-dominoes-backend (to 2025-12-03) and match3d (2025-06-30 → 2025-10-24).
   - Combo-Fighters, liveops, match3d-backend and every other repo are never mirrored.
   - Inside the windows, the copy rate is about 99% for opened, merged and approved events, about 89–94% for comments, and only 17% for COMMENTED reviews on GameOfDominoes.
   - The mirror uses real logins (`arthur.blake`). GitHub itself uses tokens.
2. **linear[bot] links Linear and GitHub.** It commented on 370 PRs (78% of the 475 PRs that name a Linear key). It is the only Linear↔GitHub link besides titles and branches, because `links_json` is empty.
   - It uses a split token: `author_login` is PERSON_6028 on the comment, but `actor_login` is SVC_0323 on the timeline.
3. **No Trello integration exists.** There is no Trello bot anywhere in Slack.
4. **Helpshift issue numbers live only in Gmail.** Issues reach Gmail through svc_0143, fanned out to SVC_0293, Leonard and Arthur. The Zapier posts in #issuefeed carry no issue number.
5. **Calendar invites only partly match GCal.** 87.9% of dated invitation mails match a GCal instance within ±1 day.
6. **Ten people were active in February 2026** (authored activity on or after 2026-02-01): Leonard, Robert, Oliver, Arthur, Marcus Bennett, Martin, Owen, Brian, Claire and Julia. Claire and Julia have one Slack message each.
   - Simon and Lauren were last active in January.
   - Vincent's last authored activity is on 2025-12-02, Douglas's on 2025-12-31 (a Confluence edit only; Slack ends 2025-10-24), and Samuel's, Calvin's and Frederick's on 2025-10-23/24.

**Using these files in injection**

- **Scope a task.** Pick a cohort in `cohorts.json` and drop the ids listed under `hazards_inside`. Then check every load-bearing id against `coherence_hazards.json`.
- **Seed a record.** Look up its service in `integrations.json` and add the required companions in the same window. Take the author from `activity.json`: an active person, posting within their own `slack_core_80pct_window_local`. Write the text to the `conventions.json` length and tone percentiles for that channel type.
- **Build a trap.** Start from a `trap_catalog.json` entry, so the trap has base precedent. Make the correct resolution decidable from an incorporated record, not from a label (Hardness_Mastery §2.6).

**Limits**

- **Identity joins** use exact email or Slack id only.
  - GitHub logins are attached only where `entities.json` joined them by `exact_email`. Trello is name-joined there, so it is shown as informational and never used for status.
  - Snowflake roster tokens are not joined.
- **The heuristic lists need a human read before use:**
  - C01 correction-marker replies
  - C02 parent-claim-overturned threads
  - R06 Slack mirrors with no matching GitHub comment text
  - the Gmail-copy similarity classes
  - near-duplicate titles found by normalised name
- **Snowflake** was read by byte range for the 35 tables under 70 MB. The five large telemetry tables (RESOURCE_FLOW_EVENTS, VIRTUAL_CURRENCY_LEDGER, RAW_GAME_EVENTS, STG_EVENTS_ENRICHED, RAW_EVENTS) have metadata only. **Sheets** grids were streamed for tab and row counts only, not cell semantics.
- **Rendering.** Nothing here verifies live-DB rendering or tool behaviour beyond `Ask_Carriers` §6b. Base counts can differ slightly from older documents that ignored the 101,657 raw-shaped Slack records. Example: Slack `reply_count` agrees on all but 2 thread parents once raw replies are counted.
- **Storyline YAML.** The beats are verified only as id existence. Their prose and figures are not ground truth. Six YAML artifact ids are missing from the base, including 3 #prototype messages dated 2026-02-13.

## Integrity layer: facts, hazards, companions, voice, reach

Large injections must agree with themselves, with the base and with what the persona can
see. Four rule sets use the files above; all are read-only and stdlib-only.

```sh
python3 Task_Authoring/tools/fact_check.py task/01_Universe_Inject.sql --manifest task/01_Hardness_Manifest.json
python3 Task_Authoring/tools/base_check.py task/01_Universe_Inject.sql --manifest task/01_Hardness_Manifest.json
python3 Task_Authoring/tools/hardness_gate.py task/01_Hardness_Manifest.json task/01_Universe_Inject.sql
python3 Task_Authoring/tools/fact_check.py --integrity-matrix [--out DIR]   # planted-defect catch matrix + sample-task run
```

- **Facts (`tools/fact_check.py`).** Scans every text-bearing value the SQL writes (Slack text and
  GitHub-app attachments, Gmail subject/body, Linear, PR/review bodies, Trello, Confluence, Docs,
  Sheets cells, Slides text, GCal summary/description). Errors: contradictions of the manifest's
  `facts` sheet, and ids cited in text that resolve neither in the base nor in the SQL (Linear keys,
  PR links and `<repo>#N`, Slack permalinks, `f_`/`d_`, `evt_`, `page_`). Warnings: one entity spelled
  two ways, one subject (or one meeting) carrying different amounts/dates across rows, people named
  while inactive (`activity.json`), bare first names that several entities share (`entities.json`
  collisions). Declared superseded versions (`traps[].version_records`) are exempt.
- **Hazard touch (`base_check`, `coherence_hazards.json`).** Example ids of each hazard are matched
  against the ids the SQL updates, references (foreign keys, joined base threads) or cites in text.
  Any touch is a warning; an UPDATE/DELETE of a `state_lifecycle` or `cross_service_referential`
  hazard record is a FAIL unless the manifest acknowledges it. Login tokenisation (I08) is not counted.
- **Integration companions (`base_check`, `integrations.json`).** INT-01: a seeded PR open, merge,
  comment or review inside GameOfDominoes / game-of-dominoes-backend / match3d's mirror window needs
  its Slack copy in the repo's channel, threaded under the PR's 'Pull request opened' message
  (base index of those parents: `support/local_search/cache/base_gh_mirror_v1.json`). INT-03: a seeded PR
  whose title/branch names a Linear key, inside the repo's linear[bot] window, needs the bot comment
  (`base_gh_integrations_v1.json`: GameOfDominoes 321/321 → FAIL, match3d 47/50 → warning). INT-11: a
  seeded meeting with attendees needs an 'Invitation:' mail in an attendee mailbox (base 836/941 →
  warning). Severity follows the base copy rate: FAIL at ≥ 95% (n ≥ 20), warning at ≥ 50%, nothing
  below. `integration_exceptions` waives a record.
- **Voice realism (`base_check`, `activity.json`).** A seeded Slack message, mail, Linear
  comment/issue, PR comment/review or Confluence edit by a person with no authored activity within
  ±60 days is a warning; one dated after a `quiet_since_*` person's last authored activity is a FAIL.
  Joins are exact-email only (`entities.json`); unjoined tokens and bots are skipped.
- **Gate (`hardness_gate.py`, full mode).** `persona_reach` (load-bearing seeded ids must be YES in
  `persona_view.py check-sql`), `fact_consistency` (fact_check errors) and `hazard_scope`
  (state/lifecycle or referential hazards among SQL-touched or manifest-cited records need
  `hazard_acknowledgements`). Field shapes: `references/Hardness_Manifest_Spec.md`.

