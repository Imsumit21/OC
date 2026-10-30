# Injection data-integrity review (`/injection`, run as the `/prompt` injection gate)

## 1. Scope

| Field | Value |
|---|---|
| Review | Eval 0 run inside `/prompt` (STEP 0.5, gate state STALE), chat review for attempt 6adfee3e0350cc55431db61d, audit mode |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`; reused_evidence: [] (every check rerun on this SQL: NEW) |
| Actual review time | 2026-10-29T12:52Z |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf71025…` |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, input revision 7, 50,529 bytes, sha256 `bc3abbdfb1d89e4c46693bd9648c267d5e8e3d6ebba3dd256d80b466e8b5e83e` |
| Eval / rules | `0_Injection_Quality_Eval.md` `e034019b8ec45043…`; WORKFLOW `ee4cd8e1cc291c3b…`; scoring.json `c14873e614cdcda5…`; known_base_issues.md `79b202893d5e3a9e…` |
| Schema refs | `references/schema/injection.json` `31dcb2b43feca8e5…` (unverified snapshot; confluence tables not covered); `id_contracts.json` `fc4711ef07667333…` |

## 2. Input / authority issues

- The only input for this stage is the SQL (revision 7). `hg_injection_gate.py` returned STALE: `input_manifest.json` still recorded the revision 6 hash `1cffcf3c…`. A `0_injection.md` covering revision 7 was on disk, but the manifest was never updated for it, so its result could not be reused under the gate. This review reran every check and replaces it.
- Two record requests returned "Source manifest changed during read" on the first try. Each was rerun on its own. Every check cited below finished with `scan_complete: true` and no errors.
- SQL comments (header and section labels, including "decoy(s)") were read only as evidence of intent.

## 3. Checklist

- [x] Save and reload SQL; record hash, base manifest and review version (NEW)
- [x] `hg_injection_lint.py`: 0 FAIL / 2 CHECK / 0 INFO; both resolved in §4 (NEW)
- [x] Inventory every statement: 75 (69 INSERT, 6 UPDATE; no DELETE, upsert or BEGIN/COMMIT) (NEW)
- [x] Check A: references, targets, collisions, ID contracts, Drive readability, one account per person (NEW)
- [x] Check B: statement structure, identifier quoting, column/value counts, JSON literals, generated columns, Linear text dates, NOT NULL (NEW)
- [x] Check C: chronology against the clock and within records, internal consistency, consistency with base Slack, Confluence, Snowflake, GitHub, Linear and Trello (NEW)
- [x] Coverage, findings, limits and one verdict

## 4. Lint flags

`hg_injection_lint.py` injection-lint-v1, universe synthcut, clock 2025-10-01T07:00:00Z, sha256 `bc3abbdf…`. 75 statements. Checks run: future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape.

| Flag | Line | Value | Resolution |
|---|---|---|---|
| padding_comment (CHECK) | 171 | `-- trello: wording authority, same-service decoy, April bundle card` | Not padding. Card `68d6735c…0d12` "Engineering release wording" says "Use for internal release notes", so it competes with the product wording card `68d67230…0d11` as a source-authority choice. The April card `680222a0…0d13` carries the stale "five coin bundles" claim that the ENG-2371 comment and the IAP_TRANSACTIONS SKU list contradict. No tool-call or pass-rate intent. |
| padding_comment (CHECK) | 180 | `-- confluence: H1/H2/H3 decoys, conflict format and the page the task corrects` | Not padding. The engineering "shipped" definition, the messaging guide and the narrative's "April 14" date are competing authorities that the wording card and the scope note override, so each serves the task. Advisory: neutral comment wording. |

## 5. Operation ledger

Line numbers refer to the saved SQL. Every collision check was a complete scan.

| Line | Table / op | Record / key values | References resolved (base path / pointer) | Coll. | Result |
|---|---|---|---|---|---|
| 11–15 | slack_messages INSERT ×5 | `a4ff3b73…` 15:30Z, `b5387eae…` 16:10Z (thread parent; thread_ts_legacy = own ts; reply_count 1; latest_reply `1759255200.000200`), `f7630544…` 16:33Z, `dce0ca4c…` 17:00Z, `947998e5…` 18:00Z (reply), all 2025-09-30; ts equals created_at for each | channel `C1CB3D58E38B` = `mpdm-leonard.hayes--julia.lawson--brian.foster-1`, members EMPLOYEE_0005/0026/0038 (slack/channels.json); 0005 Julia Lawson, 0026 Brian Foster, 0038 Leonard Hayes (slack/users.json) | `lookup` over `messages/*.json`: 4,840 files, 610,468 records, 0 hits for all 7 IDs; the mpim has no base message files | OK; authors are members |
| 16–17 | slack_messages INSERT ×2 | `a189120e…` 2025-09-28 19:00Z, `5e6ac223…` 19:10Z; SLACK_BOT_0004 in `C050WGU41HR`; attachment ts 1759086000 / 1759086600 | #engineering-bots; SLACK_BOT_0004 is a member and `is_bot`, and posts the GitHub mirrors in that channel (e.g. `C050WGU41HR/2025-03.json` /404); text equals the PR comments at lines 161–162 | 0 hits; no ts clash in `C050WGU41HR/2025-09.json` | OK |
| 21–25 | gmail_threads INSERT ×5 | `…/1860000000000000001`–`…0005`, history_id NULL | gmail/users.json has julia.lawson, leonard.hayes, brian.foster | fixed-string grep of all 81,404 thread files for `186000000000000000`, `CAFQ4claims9x2m1` and `calendar-5c1a7e93b2d04f61a8e7b8`: 0 hits | OK (history_id contract met) |
| 27, 61 | gmail_messages INSERT ×2 | scope note, Julia INBOX + Leonard SENT copies; internal_date 1759241100000 = Tue 2025-09-30 14:05Z = Date header | threads at lines 21 and 25 | 0 hits | OK |
| 34, 43, 52 | gmail_messages INSERT ×3 | invites, 1758880800000 = Fri 2025-09-26 10:00Z; one per mailbox | threads at lines 22–24 | 0 hits | OK |
| 71, 73, 75 | gcal_events INSERT ×3 | `evt_5c1a7e93…`, `evt_7d2b8f04…`, `evt_8e3c9a15…`; 2025-09-29 15:00–15:30Z (= 8:00–8:30 PDT); created 09-25 18:00Z, updated 09-26 10:00Z; shared ical_uid; `self` on the owning calendar | calendars julia.lawson, leonard.hayes, brian.foster exist (`/calendars`, field calendar_id) | 10,395 events: event_id 0 hits, ical_uid 0 hits | OK |
| 80–81 | drive_files INSERT ×2 (Docs) | `f_5a1b2c3d4e5f60718293a4` "Q4 Product Claims.docx" (09-29 09:00Z → 09-30 15:40Z); `…a5` "September list" (09-12 09:00–10:00Z) | parent `d_8140f09bf9f1b94cb8ee2d` = Julia's root folder | 53,631 drive_files: 0 hits | OK (readable through gdocs rows) |
| 83, 102 | docs_documents INSERT ×2 | same IDs; non-empty body_text (13 items / 9 items) | drive rows above | 595 docs: 0 hits | OK |
| 118–119 | drive_files INSERT ×2 (Sheets) | `f_6b2c3d4e5f60718293a4b5` register, `f_7c3d4e5f60718293a4b5c6` level manifest | same folder | 0 hits | OK |
| 121–122 | sheets_spreadsheets INSERT ×2 | same IDs | drive rows | 356 spreadsheets: 0 hits | OK |
| 124–126 | sheets_sheets INSERT ×3 | Register (12-column header; row_count 14), Old register (C01–C09, matching the September list), Levels (1200 + 1200 + 2355 = 4755 live; 245 planned) | spreadsheets above | new spreadsheets; keys unique in SQL | OK; Levels matches LEVEL_PERFORMANCE (`/tables/9/comment`: "domino_delights 1-4755") and the GDD "~4,800 levels across 160 chapters" |
| 130–136 | linear_issues INSERT ×7 | ENG-2369 … ENG-2375, created 09-26 09:00 → 09-29 12:00Z in number order | team_ENG, project `1061a4f4…` "GoD - Beta"; users Brian `usr_fc22…`, Julia `usr_8140…`, Leonard `usr_63ff…`, Calvin Price `usr_49b9…`, all team_ENG members | 3,687 issues: id and identifier 0 hits (base max ENG-2366) | OK; state_history_json `'[]'` |
| 137 | linear_issues INSERT | DES-313, created/assigned Samuel Turner `usr_caaf…`, label "Levels" | team_DES; project `1061a4f4…` (180 base DES issues use this ENG project) | 0 hits (base max DES-312) | OK; advisory V1 |
| 139–149 | linear_comments INSERT ×11 | `cmt_eng2369_1`, `cmt_eng1874_1`, `cmt_eng1385_1`, `cmt_eng2373_1`, `cmt_eng2374_1`, `cmt_eng2136_1`, `cmt_eng2323_1`, `cmt_eng2372_1`, `cmt_eng2371_1`, `cmt_eng2370_1`, `cmt_des313_1` | new issues above; base ENG-1874, ENG-1385, ENG-2136, ENG-2323 exist once each | base comments array is empty (0 records); IDs unique in SQL | OK; each comment sits between its issue's created and completed/updated times |
| 151–157 | linear_issues UPDATE ×4 | updated_at → matching comment time on ENG-1874, ENG-1385, ENG-2136, ENG-2323 | each target exists exactly once; base updated_at earlier (2024-10-03 … 2025-05-13) | n/a | OK |
| 161–162 | github_pr_comments INSERT ×2 | `#1755#c_9`, `#1838#c_4`, PERSON_0180, 2025-09-28 19:00 / 19:10Z | PERSON_0180 = Brian Foster; PR #1755 "Season Pass" merged to develop 2025-03-29, head `a05073dca537…` (/pull_requests/830); PR #1838 merged 2025-05-08 (/pull_requests/922) | 687 PR comments: 0 hits | OK; advisory V4 |
| 164–165 | github_timeline_events INSERT ×2 | `#1755#ev_41`, `#1838#ev_22`, commented | same PRs | 11,406 events: 0 hits | OK |
| 167–169 | github_pull_requests UPDATE ×2 | updated_at → 2025-09-28 19:00 / 19:10Z | targets exist | n/a | OK |
| 173–176 | trello_cards INSERT ×4 | `68daad00…0d10` "Q4 live-claim standard" (ObjectId time 2025-09-29 16:00Z = dateLastActivity), `68d67230…0d11` "External wording - product claims" (09-26 11:00Z), `68d6735c…0d12` "Engineering release wording" (11:05Z), `680222a0…0d13` "Shop bundles…" (2025-04-18 10:00Z) | boards DD Product Roadmap `65eb4ec5…638f` and Harmony Games `640643a3…`; lists October `6835c1b7…` and Backlog `65eb4ec5…6390` on 638f, Backlog `64135913…` on `640643a3…` | 803 cards: 0 hits | OK |
| 178 | trello_actions INSERT | `680222a0…0e13` commentCard 2025-04-18 10:00Z; idMemberCreator `793af7ca…` = Julia Lawson | card at line 176 | 5,252 actions: 0 hits | OK |
| 182–186 | confluence_pages INSERT ×5 | release_status_definitions (Arthur Blake, 09-05), external_messaging_guide (Robert, 09-08), q4_product_narrative (Leonard, 09-22), q4_claims_conflict_format (Julia, 09-29 16:00Z), q4_product_claims (Julia, 09-29 10:00Z) | space_ENG / space_PROD; parents page_eng_home, page_prod_home; users 0025/0016/0038/0005 | 30 pages: 0 hits on new IDs | OK |
| 188–192 | confluence_page_versions INSERT ×5 | number 1; bodies and dates match their pages | pages above | 58 versions: 0 hits; no base versions on these page_ids | OK |

## 6. Check A — Records, references and IDs: PASS

- Every actor resolves to the person the record names, with one account per service (Slack 0005/0026/0038 and bot 0004; Linear Brian, Julia, Leonard, Calvin, Samuel; GitHub PERSON_0180 = Brian; Trello member Julia; Confluence 0005/0016/0025/0038; Gmail, Drive and gcal mailboxes/calendars for Julia, Leonard and Brian). No second accounts.
- Every parent and target resolves (complete scans, pointers in §5). Every Slack author is a member of the channel it posts in. All 6 UPDATE targets exist exactly once.
- No new key collides with the base or with another statement.
- ID contracts: Gmail history_id is NULL (allowed); no Drive content_path is set. Drive readability: both Docs have non-empty gdocs body_text; both spreadsheets have gsheets grids.

## 7. Check B — SQL structure and supported schema rules: PASS

- 75 complete, `;`-terminated statements; no transactions, upserts or deletes. A static parse found column/value counts equal in all 69 INSERTs and no repeated column.
- `"references"` (gmail) and the camelCase/reserved Trello columns (`"idBoard"`, `"idList"`, `"desc"`, `"dueComplete"`, `"idMembers_json"`, `"idLabels_json"`, `"idShort"`, `"shortLink"`, `"shortUrl"`, `"dateLastActivity"`, `"idAttachmentCover"`, `"idMemberCreator"`, `"idCard"`) are quoted.
- Every `*_json` literal parses (static parse, 0 failures) and the lint's json_shape check passed (Slack metadata_json `'{}'`).
- The generated columns `text_fts` / `body_text_fts` are not set.
- Every Linear `*_at` value matches `YYYY-MM-DDTHH:MM:SSZ`; due_date is NULL. The lint's missing_required check passed, including `state_history_json = '[]'` on all 8 new issues.
- Provisional snapshot comparison (advisory): confluence tables are not covered by the snapshot.

## 8. Check C — Dates, relationships and consistency: PASS

- **Clock.** No event timestamp is after 2025-10-01 07:00Z; the latest is ENG-2375 updated 2025-09-30T18:05Z. No plan fields are set. Lint future_date: clean.
- **Grader-facing text.** None (lint grader_language clean; manual read of every body).
- **Chronology.** Slack reply follows its parent and the parent's latest_reply equals it. Leonard's "scope note I sent this morning" (16:10Z) follows the 14:05Z email. The live-claim standard card (09-29 16:00Z) follows the 15:00–15:30Z review; the gcal description calls it "Proposed". The Confluence claims page (09-29 10:00Z) follows the 13-item draft (09-29 09:00Z). On every new Linear issue created ≤ started ≤ comment ≤ completed ≤ updated. Trello ObjectId times equal dateLastActivity. Gmail weekdays are correct.
- **Checked against the base and consistent:**
  - Snowflake LIVE_EVENT_PERFORMANCE (`/tables/18/rows`, 529 rows read in full): EVT-0513 Weekly Quests 09-22→09-28 and EVT-0515 Weekly Leaderboards 09-22→09-28 completed; EVT-0525 Axe Arena and EVT-0526 Streak Fever 09-27→09-28 completed; EVT-0531 River Rush 09-29 completed and the last River Rush row; Win & Collect windows start Mon/Wed/Fri; the only Season Pass run is EVT-0527 on zombie_match_3d.
  - IAP_TRANSACTIONS (`/tables/4/comment`): DD SKUs are dd_coins_small/medium/large/mega, dd_remove_ads, dd_starter_pack; no Season Pass SKU ("absence here means no sales").
  - GDD (page_domino_gdd): US soft launch 11 April 2025, worldwide 6 May 2025; "~4,800 levels across 160 chapters". INSTALL_EVENTS comment (`/tables/1/comment`): "the US soft launch 2025-04-11".
  - Live-Ops calendar (page_liveops_calendar v3): Win & Collect "three staggered windows (Mon-Tue, Wed-Thu, Fri-Sun)"; River Rush "Recurring weekly".
  - Base Trello card "Collectibles (1 month)" sits in the October list, matching Brian's "old placeholder" message.
  - Stale/decoy sources are later corrections with record support: Leonard's 15:30Z Season Pass message is corrected by his 18:00Z reply; his 09-22 narrative page ("April 14") is corrected by the 09-30 scope note; Robert's 09-08 messaging guide is superseded by the 09-26 wording card.
- No injected record builds on known base issues SC-1–SC-3.

## 9. Advisories (not failing)

- **V2 — Season Pass: a Slack vs Snowflake base conflict that injected records build on (for `/prompt`).** Pre-existing and not caused by the SQL; Snowflake can't be edited.
  - Base Slack says the DD Season Pass was in production and sold: #god-bugs 2025-04-02 (`C05V5FNLB9V/2025-04.json` /3) "testing them out in both dev and prod servers. Season pass and daily gift was okay"; 2025-04-03 (/76) "the current season pass event was created on April 1st"; Brian Foster, #zombie-design 2025-07-23 (`C090N54TG79/2025-07.json` /734) "If users purchase the Season Pass on the level fail screen in DD and MF, they can also continue the level. In DD, this is represented with a +5 tile" and "in DD, since the Season Pass gives an extra move, users often choose to purchase the pass from this screen".
  - Snowflake has no DD Season Pass sale or run: IAP_TRANSACTIONS comment lists no Season Pass SKU and says "absence here means no sales"; the only LIVE_EVENT_PERFORMANCE Season Pass run is ZM3D EVT-0527.
  - The injected PR #1755 comment and its Slack mirror (Brian, 09-28: "the dd_season_pass default remains false in the production config and no SKU was configured in the store catalog") and the ENG-2136 comment (Brian, 09-28: "no store SKU; no completed run. The out-of-moves screen shows the $0.99 starter pack instead") side with Snowflake and contradict Brian's own July message about the DD fail screen.
  - Read as September state these can follow a later switch-off, so this is not failed here. `/prompt` decides whether the task depends on it (Eval 1 Phase 3.2, base-data-v1).
- **V1 — DES-313's creator and assignee (Samuel Turner `usr_caaf…`) are not team_DES members** (he is in team_ART, team_ENG, team_ZOM). In the base, 0 of 7,089 creator/assignee entries are non-members of the issue's team. No documented constraint, so not failed. Safer: use a team_DES member (Brian, Julia or Leonard), or file it as an ENG issue.
- V3: the Slack reply's `thread_parent_id` holds the parent's ts rather than its message id; the base export exposes only `thread_ts` and the parent's `thread_ts_legacy` matches, so not failed.
- V4: comment/event IDs skip numbers (`#1755#c_9`, `#1838#c_4`, `ev_41`, `ev_22`); not listed ID contracts.
- V5: the April 2025 "Shop bundles" card says "Keep the wording for the Q4 pack" six months early; it is a stale claim the ENG-2371 comment corrects, so allowed.

## 10. Evidence limits

- Static review only. No SQL was executed; live deployment and current database compatibility aren't certified. The schema snapshot is unverified and doesn't cover confluence.
- Collision scope is the local synth-cut base plus this SQL.
- Task discoverability, persona feasibility, difficulty and whether the task depends on V2 belong to `/prompt` and `/hardness`.

## 11. Provenance and dependencies

- SQL sha256 `bc3abbdf…`; lint injection-lint-v1 (0 FAIL, 2 CHECK).
- `hg_records.py`, one request per service, all `scan_complete: true`, no errors: linear (issues 3,687, users 41, teams 5, projects 2, comments 0), github (PR comments 687, timeline 11,406, PRs 2,475, users 46), trello (cards 803, actions 5,252, boards 5, lists 47, members 42), confluence (pages 30, versions 58, users 37, spaces 4), gcal (events 10,395, calendars 38), gdrive (drive_files 53,631), gdocs (595), gsheets (356), slack (channels 948, users 218).
- Direct reads: linear/data.json team memberships and project/team pattern; slack/channels.json; slack users; gmail users.json and thread grep; Snowflake `/tables/18/rows` (all 529), `/tables/{1,4,9,18,36}/comment`; Confluence page_domino_gdd, page_liveops_calendar, page_live_ops_engine; Slack `C05V5FNLB9V/2025-04.json`, `C090N54TG79/2025-07.json`, `C050WGU41HR/2025-0{3,9}.json`.
- Static SQL parse script (column counts, JSON literals, Linear date format): 0 issues.
- Reused evidence: none.

### FINAL VERDICT: PASS

Execution status: COMPLETE

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt (running now as part of this review). V2 is assessed there under base-data-v1.

Evidence limits: Static scope only; no live execution or database-compatibility certification; schema snapshot unverified (confluence not covered); collisions checked against the local synth-cut base plus this SQL.
