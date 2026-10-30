# Injection data-integrity review (`/injection`)

## 1. Scope

| Field | Value |
|---|---|
| Review | Chat review, attempt 6adfee3e0350cc55431db61d, audit mode (fresh rerun on the same saved SQL) |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`; reused_evidence: [] (every check rerun: NEW). The previous report on this same SQL hash was read only to make sure none of its findings were missed; each one was re-verified from source below. |
| Actual review time | 2026-10-29T10:40Z |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf71025…` |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, input revision 6 (attached as `01_Universe_Inject (2).sql`), 47,520 bytes, sha256 `1cffcf3ce8dab295389a04e14b56c14deecac38883f81b6462ce47855f1b841a` |
| Eval / rules | `0_Injection_Quality_Eval.md` sha256 `e034019b8ec45043…`; WORKFLOW `ee4cd8e1cc291c3b…`; scoring.json `c14873e614cdcda5…`; known_base_issues.md `79b202893d5e3a9e…` |
| Schema refs | `references/schema/injection.json` sha256 `31dcb2b43feca8e5…` (unverified snapshot; confluence not covered); `id_contracts.json` `fc4711ef07667333…` |

## 2. Input / authority issues

- The only input for this stage is the SQL. It is unchanged since the last review (same hash).
- The universe files were still loading onto this machine (lazy filesystem) when the review started, so the first record/Snowflake scans returned "Source manifest changed during read". Each was rerun after loading finished. Every check below has `scan_complete: true` and no errors.
- SQL comments (header and section labels, including "decoy(s)") were read as evidence of intent only.
- Outside this stage's scope (context for `/prompt`): the saved prompt is about a Zombie Match 3D "What's New" line (Vincent, Len, Owen's refill bug). This SQL builds a Domino Delights Q4 product-claims register for Julia Lawson. The injected records don't support that prompt. `/prompt` owns that judgement; it isn't scored here.

## 3. Checklist

- [x] Save and reload SQL; record hash, base manifest and review version (NEW)
- [x] `hg_injection_lint.py`: 0 FAIL / 2 CHECK / 0 INFO; both resolved in §4 (NEW)
- [x] Inventory every statement: 73 (65 INSERT, 8 UPDATE; no BEGIN/COMMIT, upsert or delete) (NEW)
- [x] Check A: references, targets, collisions, ID contracts, Drive readability, one account per person (NEW)
- [x] Check B: statement structure, identifier quoting, column/value counts, JSON, generated columns, Linear text dates, NOT NULL, snapshot comparison (NEW)
- [x] Check C: chronology against the clock and within records, internal consistency, consistency with base Slack/Confluence/Snowflake/GitHub/Linear/Trello/gcal (NEW)
- [x] Coverage, findings, limits and one verdict

## 4. Lint flags

`hg_injection_lint.py` injection-lint-v1, universe synthcut, clock 2025-10-01T07:00:00Z, sha256 `1cffcf3c…841a`. 73 statements. Checks run: future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape.

| Flag | Line | Value | Resolution |
|---|---|---|---|
| padding_comment (CHECK) | 165 | `-- trello: wording authority, same-service decoy, April bundle card` | Not padding. Card `68d6735c…0d12` (Engineering release wording) is scoped to internal release notes and competes with the product wording card. That's a source-authority choice with a task purpose. The April card `680222a0…0d13` carries the stale "five coin bundles" claim that the ENG-2369 comment corrects. No tool-call or pass-rate language. Advisory: use neutral comment wording. |
| padding_comment (CHECK) | 174 | `-- confluence: H1/H2/H3 decoys, conflict format and the page the task corrects` | Not padding. The engineering "shipped" definition, the messaging guide and the narrative's 14 April date are competing authorities that the scope note and wording card override, so they have a task purpose. Same advisory. |

The lint did not catch F1 (identifier quoting) or F2–F6 (chronology/consistency). Those come from the manual checks.

## 5. Operation ledger

Line numbers refer to the saved SQL. Coll. = collision check for the new key; all were complete scans.

| Line | Table / op | Record / key values | References resolved (base path / pointer) | Coll. | Result |
|---|---|---|---|---|---|
| 11 | slack_messages INSERT | `a4ff3b73…` ts 1759246200.000050 = 2025-09-30T15:30Z (created_at matches), EMPLOYEE_0038 | channel `C1CB3D58E38B` = `mpdm-leonard.hayes--julia.lawson--brian.foster-1`, members 0005/0026/0038 (slack/channels.json); EMPLOYEE_0038 = Leonard Hayes (users.json) | `lookup` over all 4,840 message files / 610,468 records: 0 hits for all 7 IDs | OK |
| 12 | slack_messages INSERT (thread parent) | `b5387eae…` ts 1759248600.000100 = 16:10Z; reply_count 1, latest_reply 1759255200.000200 | as above | OK | OK; advisory V1 |
| 13 | slack_messages INSERT | `f7630544…` 16:33Z, EMPLOYEE_0026 = Brian Foster | member | OK | OK |
| 14 | slack_messages INSERT | `dce0ca4c…` 17:00Z, Brian: Collectibles card "in the October list is just the old placeholder" | base Trello card `67ec1f60…` "Collectibles (1 month)" in list `6835c1b7…` October | OK | OK, consistent |
| 15 | slack_messages INSERT (reply) | `947998e5…` 18:00Z, Leonard; thread_parent_id `1759248600.000100` | parent line 12; latest_reply on the parent equals this ts | OK | OK; advisory V1 |
| 16–17 | slack_messages INSERT ×2 | `a189120e…` 2025-09-28T19:00Z, `5e6ac223…` 19:10Z; SLACK_BOT_0004 in `C050WGU41HR` | #engineering-bots exists; SLACK_BOT_0004 is a member and a bot; mirror text = PR comments lines 155–156 | OK | OK; advisory V7 |
| 21–24 | gmail_threads INSERT ×4 | `…/1860000000000000001`–`…0004`, history_id NULL | gmail/users.json has julia.lawson, leonard.hayes, brian.foster; base thread ids use `<mailbox>/<number>` | grep of all 81,404 thread files for the 4 numbers and 4 Message-IDs: 0 hits | OK (history_id contract met) |
| 26 | gmail_messages INSERT | `julia…/<CAFQ4claims9x2m1@mail.gmail.com>`, internal_date 1759215900000 = 2025-09-30T07:05Z = Date header (Tue 30 Sep is correct), Leonard → Julia, scope note | thread line 21 | 0 hits | **F1** (unquoted `references`) |
| 33, 42, 51 | gmail_messages INSERT ×3 | calendar invites, 1758880800000 = 2025-09-26T10:00Z (Fri, correct), one per mailbox, attachments_meta `seed/att_0001.ics` | threads lines 22–24 | 0 hits | **F1**; advisory V2 |
| 63, 65, 67 | gcal_events INSERT ×3 | `evt_5c1a7e93…`, `evt_7d2b8f04…`, `evt_8e3c9a15…`; 2025-09-29 15:00–15:30Z (= 8:00–8:30 PDT, as invited); created 09-25 18:00Z, updated 09-26 10:00Z; shared ical_uid | calendars for all 3 people exist (gcal /calendars) | 10,395 events: event_id 0 hits, ical_uid 0 hits | **F3** (points to a card that doesn't exist yet) |
| 72–73 | drive_files INSERT ×2 (Docs) | `f_5a1b2c3d4e5f60718293a4` "Q4 Product Claims.docx" (created 09-29 09:00Z, modified 09-30 15:40Z); `…a5` "September list" (created 09-12 09:00Z, modified 09-12 10:00Z) | parent `d_8140f09bf9f1b94cb8ee2d` = Julia's folder (gdrive /drive_files/11673) | 53,631 drive_files: 0 hits | OK (readable through gdocs rows); `…a5` content shares **F5** |
| 75, 94 | docs_documents INSERT ×2 | same IDs; non-empty body_text (13 items / 9 items) | drive rows above | 595 docs: 0 hits | `…a4` OK; `…a5` **F5** |
| 110–111 | drive_files INSERT ×2 (Sheets) | `f_6b2c3d4e5f60718293a4b5` register (created 09-28 13:00Z), `f_7c3d4e5f60718293a4b5c6` level manifest (09-29 17:00Z) | same folder | 0 hits | OK |
| 113–114 | sheets_spreadsheets INSERT ×2 | same IDs | drive rows | 356 spreadsheets: 0 hits | OK |
| 116–118 | sheets_sheets INSERT ×3 | Register (header + 13 empty rows, 12 cols), Old register (header + 9), Levels (1200+1200+2355 = 4755 live, 245 planned) | spreadsheets above | new spreadsheets | OK; Levels total fits the GDD "~4,800 levels across 160 chapters" (page_domino_gdd); advisory V8 |
| 122–127 | linear_issues INSERT ×6 | ENG-2373, ENG-2374, ENG-2369, ENG-2371, ENG-2372, DES-313 | team_ENG (/teams/2), team_DES (/teams/1), project `1061a4f4…` (/projects/0); users Brian `usr_fc22…` (/users/40), Julia `usr_8140…` (/users/18), Leonard `usr_63ff…` (/users/13), Calvin Price `usr_49b9…` (/users/6), Samuel Turner `usr_caaf…` (/users/34) | 3,687 issues: id and identifier 0 hits (base max ENG-2366, DES-312) | OK; state_history_json `'[]'` present; advisories V4, V6 |
| 129 | linear_comments INSERT | `cmt_eng645_1` on ENG-645, 2025-09-29T10:00Z, EVT-0513 (2025-09-28) | ENG-645 /issues/2745 (archived) | base comments array: 0 records; IDs unique in SQL | OK (EVT-0513 Weekly Quests 09-22→09-28 completed, Snowflake /tables/18/rows/512); advisory V5 |
| 130 | linear_comments INSERT | `cmt_eng1874_1` on ENG-1874, 09-29T10:10Z, EVT-0515 (2025-09-28) | /issues/1769 | OK | OK (rows/514 Weekly Leaderboards 09-22→09-28 completed) |
| 131 | linear_comments INSERT | `cmt_eng1385_1` on ENG-1385, Win & Collect Mon/Wed/Fri | /issues/1240 | OK | OK (Live-Ops calendar: three windows Mon-Tue, Wed-Thu, Fri-Sun) |
| 132 | linear_comments INSERT | `cmt_eng2065_1` on ENG-2065, **2025-09-29T10:30Z**, "last completed run EVT-0531 (2025-09-29)" | /issues/1980 (archived) | OK | **F6**; advisory V9 |
| 133 | linear_comments INSERT | `cmt_eng2136_1` on ENG-2136, 09-28T16:00Z, Season Pass default=false, no SKU, no run | /issues/2057 | OK | OK (no DD Season Pass run in LIVE_EVENT_PERFORMANCE) |
| 134 | linear_comments INSERT | `cmt_eng2323_1` on ENG-2323, 10% cohort | /issues/2262 | OK | OK |
| 135 | linear_comments INSERT | `cmt_eng2367_1` on new ENG-2373, 09-28T17:00Z | line 122 (created 09-26) | OK | OK (ID label differs from the issue number, cosmetic) |
| 136 | linear_comments INSERT | `cmt_eng2368_1` on new ENG-2374, **2025-09-28T17:10Z**, "both completed 2025-09-30 (EVT-0532, EVT-0533)" | line 123 | OK | **F2** |
| 137 | linear_comments INSERT | `cmt_eng2369_1` on ENG-2369, 09-26T13:20Z (issue 12:00–14:00) | line 124 | OK | OK |
| 138 | linear_comments INSERT | `cmt_eng2372_1` on ENG-2372, 09-28T16:35Z, Calvin | line 126 | OK | OK |
| 139 | linear_comments INSERT | `cmt_des313_1` on DES-313, 09-29T09:20Z, Samuel | line 127 | OK | OK; advisory V8 |
| 141–151 | linear_issues UPDATE ×6 | updated_at set to the matching comment time on ENG-645, 1874, 1385, 2065, 2136, 2323 | each target exists exactly once; base updated_at earlier (2024-05-06 … 2025-05-13) | n/a | OK; ENG-2065's value shares **F6** |
| 155–156 | github_pr_comments INSERT ×2 | `#1755#c_9`, `#1838#c_4`, PERSON_0180, 2025-09-28 19:00/19:10Z | PERSON_0180 = Brian Foster (/users/17); PR #1755 "Season Pass", merged to develop 2025-03-29, head `a05073dca537` (/pull_requests/830); PR #1838 "ENG-2323: Add Hero Offers to Shop", merged 2025-05-08 (/pull_requests/922) | 687 PR comments: 0 hits | OK |
| 158–159 | github_timeline_events INSERT ×2 | `#1755#ev_41`, `#1838#ev_22` commented | same PRs | 11,406 events: 0 hits | OK |
| 161–163 | github_pull_requests UPDATE ×2 | updated_at → 2025-09-28 19:00 / 19:10Z | targets exist; base updated_at = merge times | n/a | OK |
| 167 | trello_cards INSERT | `68d672304f5e6d7a8b9c0d10` "Q4 live-claim standard"; ID time 2025-09-26 11:00Z; dateLastActivity 2025-09-26 10:30Z | board `65eb4ec5…638f` DD Product Roadmap (/boards/2); list `6835c1b7…` October on that board (/lists/38) | 803 cards: 0 hits | **F1**, **F3** |
| 168 | trello_cards INSERT | `68d67230…0d11` "External wording - product claims", ID 11:00Z, activity 11:00Z | same | 0 hits | **F1** |
| 169 | trello_cards INSERT | `68d6735c…0d12` "Engineering release wording", ID 11:05Z, activity 11:05Z | board `640643a3…` Harmony Games (/boards/1), list `64135913…` Backlog on that board (/lists/7) | 0 hits | **F1** |
| 170 | trello_cards INSERT | `680222a0…0d13` "Shop bundles - five coin bundles + starter", ID/activity 2025-04-18 10:00Z | board 638f, list `65eb4ec5…6390` Backlog on that board (/lists/8) | 0 hits | **F1** |
| 172 | trello_actions INSERT | `680222a0…0e13` commentCard 2025-04-18 10:05Z, idMemberCreator NULL | card line 170 | 5,252 actions: 0 hits | **F1**; advisory V3 |
| 176–180 | confluence_pages INSERT ×5 | release_status_definitions (Arthur Blake, 09-05), external_messaging_guide (Robert, 09-08), q4_product_narrative (Leonard, 09-22), q4_claims_conflict_format (Julia, 09-29 16:00Z), q4_product_claims (Julia, **09-25**) | space_ENG/space_PROD (/spaces/0,1); parents page_eng_home (/pages/0), page_prod_home (/pages/14); users 0025/0016/0038/0005 = Arthur Blake / Robert / Leonard Hayes / Julia Lawson | 30 pages: 0 hits on new IDs | **F4** on page_q4_product_claims |
| 182–186 | confluence_page_versions INSERT ×5 | `ver_6be4…`, `ver_5c89…`, `ver_6dfb…`, `ver_4a4c…`, `ver_4d11…`, number 1, same bodies/dates as pages | pages above | 58 versions: 0 hits | `ver_4d11…` shares **F4**; advisory V10 |

## 6. Check A — Records, references and IDs: PASS

- Every actor resolves to the person the record names, with one account per service (§5): Slack 0005/0026/0038, Linear users, GitHub PERSON_0180, Confluence users, and the Gmail, Drive and gcal accounts. No second accounts.
- Every parent and target resolves: channels and membership, Drive folder, Trello boards and lists (each list belongs to the card's board), Linear team/project/issues, GitHub PRs, Confluence spaces/parents, gcal calendars. All 8 UPDATE targets exist exactly once.
- No new key collides with the base or within the SQL. Complete-scan coverage is in §5.
- ID contracts: Gmail history_id NULL (allowed); no Drive content_path is set. Drive readability: both Docs have gdocs rows with non-empty body_text; both spreadsheets have gsheets grids.
- Advisories only: V2–V6.

## 7. Check B — SQL structure and supported schema rules: FAIL

**F1 — Reserved words and camelCase columns are unquoted (9 statements).**
- The backing database is PostgreSQL: the snapshot types are `character varying`, `timestamp with time zone` and `tsvector`, and Eval 0 cites the PostgreSQL "can only be updated to DEFAULT" error.
- Gmail, lines 26, 33, 42, 51: the column list has `… in_reply_to, references, mbox_from …`. The snapshot column is `references` (position 23). `REFERENCES` is a reserved key word in PostgreSQL, so each of the 4 INSERTs is a syntax error.
- Trello cards, lines 167–170: the column list has unquoted `desc` (snapshot position 5). `DESC` is reserved, so each of the 4 INSERTs is a syntax error.
- Even with `desc` quoted, the snapshot columns are mixed-case: `idBoard`, `idList`, `dueComplete`, `idMembers_json`, `idLabels_json`, `idShort`, `shortLink`, `shortUrl`, `dateLastActivity`. Unquoted, PostgreSQL folds them to lowercase (`idboard` …), which is not the column, so they fail with "column does not exist".
- Trello action, line 172: unquoted `idMemberCreator, idBoard, idCard` fold the same way (snapshot positions 4–6).
- Effect: the scope email, the 3 invites, all 4 Trello cards (including the live-claim standard and the wording rules) and the Trello comment cannot load. There is no BEGIN/COMMIT, so depending on the loader the script either stops at line 26 (losing everything after it) or skips those 9 records.
- Fix: quote exactly these identifiers.
  - Gmail: `… in_reply_to, "references", mbox_from …`
  - Trello cards: `id, name, "idBoard", "idList", "desc", pos, closed, due, "dueComplete", "idMembers_json", "idLabels_json", "idShort", "shortLink", "shortUrl", url, "dateLastActivity", cover_json, badges_json, start, "idAttachmentCover"`
  - Trello action: `id, type, date, "idMemberCreator", "idBoard", "idCard", data_json`
  - `index` in sheets_sheets is non-reserved and works unquoted; quoting it as `"index"` is harmless.

Other Check B results (pass):
- Column/value counts match in all 65 INSERTs.
- Every `*_json` literal parses, with the snapshot's shape (Slack metadata_json `'{}'`; array columns `'[]'`; trello badges and data_json are objects).
- No generated `text_fts` / `body_text_fts` columns are set.
- Linear `*_at` values all use `YYYY-MM-DDTHH:MM:SSZ`. NOT NULL columns, including `state_history_json = '[]'`, are present.
- Provisional snapshot comparison (advisory): `gcal_events.extras_json`, `trello_cards.start`/`idAttachmentCover`, `linear_issues.uuid`, `linear_comments.sequence` and `confluence_page_versions.synthesized` are NOT COVERED; the confluence tables are NOT COVERED. Every other column used MATCHES.

## 8. Check C — Dates, relationships and consistency: FAIL

No event timestamp is after the clock (latest: ENG-2371 updated 2025-09-30T18:05Z; the lint agrees). No grader-facing text was found in any injected record. The Slack reply follows its parent, and the parent's latest_reply equals the reply ts. On the new Linear issues, created ≤ comment ≤ completed ≤ updated. PR comments follow the merges. The gcal times match the invite text.

**F2 — The ENG-2374 comment reports a future run and cites a warehouse run that doesn't exist.**
- `cmt_eng2368_1` (line 136; created/updated 2025-09-28T17:10Z; ENG-2374 updated_at the same) says: "Axe Arena and Streak Fever alternate on the daily slot; both completed 2025-09-30 (EVT-0532, EVT-0533)."
- (a) A comment written on 28 Sep reports runs completed on 30 Sep. That's impossible chronology.
- (b) Snowflake `LIVE_EVENT_PERFORMANCE` (full `search-many` scan, complete):
  - EVT-0532 is Streak Fever only, 2025-09-30 (`/tables/18/rows/528`, the last row).
  - **EVT-0533 doesn't exist** (0 hits).
  - There is no Axe Arena run on 30 Sep. The last Axe Arena run is EVT-0525, 2025-09-27→28, completed (row 523). Streak Fever before that was EVT-0526, 09-27→28 (row 524).
- The SQL can't change Snowflake, and the live-claim standard in the SQL counts warehouse runs, so this injected fact contradicts the base.
- Fix, either one:
  - Date the comment (and ENG-2374 updated_at) on or after `2025-09-29T00:00:00Z` (e.g. `2025-09-29T17:10:00Z`) and cite real runs: "Axe Arena last completed EVT-0525 (2025-09-28); Streak Fever last completed EVT-0526 (2025-09-28)."
  - Or, to cite EVT-0532, date the comment after 30 Sep ends and before the clock (2025-10-01T00:00Z–07:00Z), and drop EVT-0533 and the Axe Arena claim.

**F3 — The live-claim standard card exists before the meeting that "agreed" it, and its last activity is before its own creation.**
- Card `68d672304f5e6d7a8b9c0d10` (line 167) says "Live-claim standard (agreed at the Q4 review)".
- Its Trello ID time is 2025-09-26 11:00Z, and its dateLastActivity is 2025-09-26 **10:30Z**, 30 minutes before it was created. In the base, 0 of 803 cards have dateLastActivity before their ID time.
- The only Q4 review is the injected gcal event on **2025-09-29 15:00Z**. Base gcal has no "Q4 review"/"claims"/"live-claim" event in 10,395 events, and base Slack 2025 has no "Q4 review" or "live-claim" in 1,638 files (complete scans). So a card last touched on 26 Sep describes as agreed something that happens on 29 Sep.
- The gcal events (lines 63–67, last updated 2025-09-26 10:00Z) also point to "the Q4 live-claim standard card", which doesn't exist until 11:00Z.
- Fix:
  - Create the card after the meeting, e.g. id `68daad004f5e6d7a8b9c0d10` (ID time 2025-09-29 16:00Z) with `"dateLastActivity" = '2025-09-29 16:00:00+00'`.
  - Reword the gcal description's first sentence so it doesn't point at a card that doesn't exist yet (e.g. "Proposed live-claim standard for sign-off:"). The standard's text can stay in the event.

**F4 — The Confluence claims page summarises a 13-claim register before either exists.**
- `page_q4_product_claims` and `ver_4d11…` (lines 180, 186), created/updated 2025-09-25T09:00Z, say "All 13 product claims are live. See the claims register for the full list."
- On 25 Sep the only claims list is the 9-item September list (2025-09-12). The register workbook is created 2025-09-28 13:00Z and the 13-item draft 2025-09-29 09:00Z.
- Fix: date the page and its version on or after `2025-09-29T09:00:00Z` (e.g. `2025-09-29T10:00:00Z`).

**F5 — The September list doc states a verification date after its last edit.** (New in this review; the previous report missed it.)
- `f_5a1b2c3d4e5f60718293a5` "Q4 Product Claims - September list" has docs_documents created 2025-09-12 09:00Z and modified 2025-09-12 10:00Z (drive_files the same; lines 73, 94).
- Its body says "Status: all 9 items verified live with the owning teams **as of 29 September**."
- A document last edited on 12 Sep can't report a verification as of 29 Sep 2025. The 2024 reading doesn't work either: item 6 cites "#1755", which was merged 2025-03-29 (GitHub /pull_requests/830).
- Fix: change the status line to a date on or before 12 Sep (e.g. "as of 12 September"), or move the doc's modified times to on/after 29 Sep while keeping it older than the 13-item draft.

**F6 — The ENG-2065 comment calls the River Rush run "completed" while that run's day is still in progress.** (New in this review.)
- `cmt_eng2065_1` (line 132, created/updated 2025-09-29T10:30Z; ENG-2065 updated_at the same, line 147) says "last completed run EVT-0531 (2025-09-29)".
- EVT-0531 is a single-day River Rush run, start = end = 2025-09-29, completed (Snowflake `/tables/18/rows/527`).
- Event days here are UTC days: the SQL's own comment says "Mondays 00:00 UTC", and Confluence `page_live_ops_engine` says the "weekly generator runs Sunday 00:00 UTC". So the run ends at 2025-09-30T00:00Z, 13.5 hours after the comment. Under PT the day ends even later.
- Fix: date the comment and ENG-2065 updated_at on or after `2025-09-30T00:00:00Z` (e.g. `2025-09-30T10:30:00Z`).

Checked and consistent (no finding):
- PR #1755 merge facts (develop, head `a05073dca537`).
- EVT-0513 / EVT-0515 Weekly Quests / Leaderboards 09-22→09-28, completed.
- Win & Collect windows against the Live-Ops calendar page.
- GDD soft launch 11 Apr / worldwide 6 May 2025 match the scope note's "not the 14 April date".
- Level manifest totals match the GDD's ~4,800 levels.
- The Collectibles placeholder card is in the October list.
- Leonard's "the scope note I sent this morning" (Slack 16:10Z) follows the 07:05Z email.
- Weekday names in the Gmail headers are correct.
- No injected record builds on known base issues SC-1–SC-3 (no September installs, burn or runway facts).

## 9. Advisories (not failing)

- V1: The Slack reply's `thread_parent_id` holds the parent's ts, and the parent's `thread_ts_legacy` is NULL. The base export only exposes `thread_ts`, and the DB semantics aren't documented, so this isn't failed. The safer form: parent `thread_ts_legacy = '1759248600.000100'`.
- V2: The invite `attachments_meta_json` rel_path `seed/att_0001.ics` has no bytes. Base paths use the takeout layout (e.g. `gmail/dwt-takeout-export-…/att_0001.ics`). The task doesn't need the .ics; `'[]'` is cleaner.
- V3: The Trello comment action has `idMemberCreator` NULL (0 of 5,252 base actions) and an ID time 5 minutes before its `date`. Consider adding a real member ID.
- V4: Linear numbers are out of creation order (ENG-2369 was created after ENG-2372/2373; ENG-2371 after ENG-2372–2374). This isn't a listed ID contract.
- V5: Comments and updates land on archived issues ENG-645 (a quest-points endpoint) and ENG-2065.
- V6: The label "Level Design" doesn't exist among base issue labels (base has "Levels", "Level Editor").
- V7: The #1838 Slack mirror's attachment `ts` is 1759086000 (the #1755 time) rather than 1759086600.
- V8: DES-313's comment (09-29 09:20Z) quotes manifest numbers 8 hours before the manifest sheet is created (17:00Z). The "Old register" tab (sheet modified 09-28 14:00Z) already uses the 13-item numbering (C11), while the 13-item draft is created the next day. Neither is provably impossible, but the dates read oddly.
- V9: "River Rush runs on the daily slot". The Live-Ops calendar says "Recurring weekly".
- V10: There's no sender copy of the scope note in Leonard's mailbox. The script has no BEGIN/COMMIT. `synthesized = true` is set on page versions, but the base page_versions records have no such field (not covered by the snapshot).

## 10. Evidence limits

- Static review only. No SQL was executed, and live deployment and current database compatibility aren't certified. The schema snapshot is unverified and doesn't cover confluence.
- Collision scope is the local synth-cut base plus this SQL.
- Task discoverability, the prompt/SQL mismatch noted in §2, persona feasibility and difficulty belong to `/prompt` and `/hardness`.
- `input_manifest.json` was not rewritten by this run. Its injection entry already records `injection-static-v2` for this same SQL hash. This report carries its own fingerprints.

## 11. Provenance and dependencies

- SQL sha256 `1cffcf3c…841a`; lint injection-lint-v1.
- `hg_records.py`, one request per service (confluence, gcal, gdocs, gdrive, github, gsheets, linear, trello). All `scan_complete: true`, no errors. Records checked: linear issues 3,687, users 41, comments 0; github PR comments 687, timeline 11,406, PRs 2,475; trello cards 803, actions 5,252; confluence pages 30, versions 58; gcal events 10,395; drive_files 53,631; docs 595; spreadsheets 356.
- Slack: `lookup` over `messages/*.json` (4,840 files, 610,468 records, complete); channels.json; users.json; `search-many` over `messages/*/2025-*.json` (1,638 files, complete).
- Gmail: users.json; grep of all 81,404 thread files.
- Snowflake: `search-many` full scan of snowflake.json for EVT-0513/0515/0525/0526/0531/0532/0533 (complete), then `get-many` of `/tables/18/rows/512, 514, 523, 524, 527, 528`.
- Confluence base pages read: page_domino_gdd, page_liveops_calendar, page_live_ops_engine. Trello ObjectId times were decoded from the IDs.
- Reused evidence: none.

### FINAL VERDICT: FAIL

Execution status: COMPLETE

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Fix F1 (quote "references", "desc" and the Trello camelCase columns in 9 statements), F2 (ENG-2374 comment: real run IDs and a date after those runs), F3 (re-date the live-claim standard card after the 29 Sep review and reword the gcal pointer), F4 (date the Confluence claims page on or after 29 Sep 09:00Z), F5 (September list status date) and F6 (date the ENG-2065 comment on or after 30 Sep 00:00Z). Then send /injection again, followed by /prompt, /hardness, /oe and /rubric.

Evidence limits: Static scope only; no live execution or database-compatibility certification; schema snapshot unverified (confluence not covered); collisions checked against the local synth-cut base plus this SQL.
