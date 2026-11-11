# Injection data-integrity review: Eval 0

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. Base facts are reused from the previous `injection-static-v2` report (`R/prev/0_injection.previous_report_on_837d4f5d.md`, SHA-256 `e19b226bc538c49b02f6249aa127c22098a5f95c2898649af9428407fb6b7a32`), but only for byte-identical statements, and only where that report records the claim together with a source pointer. Every changed, new or removed statement was checked NEW. Collision, reference, Slack-thread, Linear-chronology, clock and Check B checks were also rerun NEW over the whole file. |
| Mode | Independent chat review, audit. Workspace adaptation: the report goes to `R/out/0_injection.md`. The input store, `hg_write_output.py` and `input_manifest.json` were not used; section 9 gives the manifest entry. |
| Review time | 2026-11-06 |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`; `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` (re-hashed; same as the previous report) |
| Input | `R/inputs/01_Universe_Inject.sql`, 59,751 bytes, 261 lines, SHA-256 `c955d6ca2bca5d1aa0c457e3107a28e8210903a833b3192a54d1e5337adc1cf2` (re-hashed). Not executed. |
| Previous version | `R/prev/01_Universe_Inject.previous_837d4f5d.sql`, 62,399 bytes, SHA-256 `837d4f5dedbdedb0febe279f64b5df61f0debdf29e93ef779a4ddd5ff754d76b` (PASS / COMPLETE in the previous report) |
| Schema snapshot | `Evals/references/schema/injection.json` SHA-256 `01ef579236212034a43a53914754f86ed9248be48c961009cef5b4bd6106f6eb` (re-hashed; same as the previous report; unverified, provisional) |
| ID contracts | `Evals/references/schema/id_contracts.json` SHA-256 `fc4711ef07667333c1cf2a417279826f0432539195f7acdfacfa86e9d9ed4682` (re-hashed; same) |
| Key sources | `linear/data.json` SHA-256 `b49ec9e8…3b4d` (same as the previous report); `github/data.json` SHA-256 `ee578c91…7538` |
| Lint | `hg_injection_lint.py` injection-lint-v1, run through `Task_Authoring/tools/hg.py lint` |
| Known base issues | `Task_Authoring/references/known_data_issues/synthcut.md` (SHA-256 `8895c4dc…1a52`). Cards touched: SC-15, SC-16, SC-22, SC-38 and SC-71. |
| Other inputs | Context only: `00_Task_Assigned_Inputs.md` (sha `e8b82698…49eb`), `02_Universe_Date.txt` ("Oct 1, 2025 (synth-cut)", sha `2f0af108…c519`) and `04_Prompt.txt` (sha `2a23afd8…2beb`). All three are unchanged from the previous review. |

## 2. Input / authority issues

- The SQL header comments point to a grounding dossier and to `universe_schema_live.json`. Neither was supplied. They are statements of intent, not evidence. No SQL comment changed in this revision, and none is about padding, tool calls, pass rates or gates.
- **Reuse provenance.** Several rows in the previous report say only "content as in the previous report row N". Those rows point to an earlier report (`51ac8433…`) that was not supplied. Under reuse condition 1, those content claims were not carried forward. This review re-verified them NEW where they bear on Check C (section 5 marks the basis per row). REUSED is used only where the supplied report records the claim and its pointer.
- **Seven earlier advisories are resolved by this revision:**
  - A2: the Gmail correction now starts its own thread under a new subject, with no reply headers.
  - A3: the correction's snippet is now the start of its body.
  - A4: the mirror subtype is now null and the handles are real.
  - A5: the Halloween retraction is now a top-level DM message.
  - A7 (both halves): GCal transparency is now `opaque`, and review timeline events now use the base `reviewed` shape.
  - The SC-16-style "can close while still Todo" condition on ZOM-565 (old A8 item).
- No grader-facing or solver-facing text in any changed or new record (lint plus a manual read).

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, manifest, review version | NEW, done. Workspace adaptation: hashes are recorded here and nothing is written to the store. |
| Diff against the previously reviewed SQL | NEW, done statement by statement with a comment-stripped, quote-aware splitter and a per-column field diff. <br>• prev 112 statements → new 106 <br>• 71 byte-identical <br>• 23 changed <br>• 12 new <br>• 18 removed <br>• No SQL comment changed. <br>The mapping is in section 5. |
| Run lint; resolve every flag | NEW, done (0 flags) |
| Inventory every statement | NEW, done: 106 statements (75 INSERT, 31 UPDATE). No DELETE, upsert or conflict clause. The count matches the lint. |
| Check A | NEW over the whole file (complete collision scans and target and actor checks): **PASS** |
| Check B | NEW over the whole file against the local snapshot: **PASS** (provisional; snapshot mismatches are advisory) |
| Check C | NEW in full for every changed, new and removed statement group. Also NEW for the whole file: the clock sweep, the Linear per-issue chronology, the Slack thread counts and the weekday claims. The unchanged Linear comments got a NEW topic and actor read. Content is REUSED only for pointer-recorded claims. **PASS** |
| Report coverage, findings, limits, verdict | done |

## 4. Lint

`hg_injection_lint.py` (injection-lint-v1) ran on SHA `c955d6ca…1cf2` with universe synthcut and clock `2025-10-01T07:00:00Z`.

- **Base loaded:** slack/users, gmail/users, github/data, linear/data, trello/data, contacts, confluence_working.
- **Checks run:** future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required.
- **Statements:** 106 (75 insert, 31 update).
- **Flags:** FAIL 0, CHECK 0, INFO 0. Nothing to resolve.

The lint ran no `json_shape` check, so every `*_json` literal was parsed by hand: 122 literals, 0 errors. A clean lint is not a PASS, so checks A–C were run in full.

## 5. Operation ledger

Statement numbers are positions in the new SQL; "prev" numbers are positions in `837d4f5d`. "NEW" means verified in this review against the cited base record. "REUSED" means taken from the previous report (`e19b226b…`) for a byte-identical statement where that report recorded the claim and its pointer. The dependencies for reuse are unchanged: universe manifest `da2f4cf0…`, id_contracts `fc4711ef…`, snapshot `01ef5792…` and the clock.

**Complete NEW collision and target scans**, all `scan_complete: true` with 0 errors:

- **Slack:** `lookup` over `messages/*/*.json` (4,840 files, 610,468 records). All 9 injected message IDs are absent, and no injected `ts` collides in any 2025-09 channel file. The 5 thread parents exist; their base reply counts were re-read: `9025d428` 0, `c2b9c903` 16, `4b7c4127` 41, `d05a2f8a` 2 and `da3fe08c` 7.
- **GitHub (`hg_records`):** all new keys are absent:
  - `/reviews` (2,230): `#470#rev_10`, `#468#rev_3`;
  - `/review_comments` (1,387): `#470#rc_10`, `#468#rc_38`;
  - `/timeline_events` (11,406): `#470#ev_9`, `#468#ev_6`, `#473#ev_5`, `#471#ev_8`;
  - `/pull_request_comments` (687): `#473#c_2`, `#471#c_18`.

  All 4 PR targets exist in `/pull_requests` (2,475): #468 `/2372`, #470 `/2375`, #471 `/2376` and #473 `/2378`.
- **Linear:** `/comments` has 0 records, so all 24 comment IDs are unique against the base. All 22 issue targets exist in `/issues` (3,687), with `id` = `identifier`. All 10 authors exist in `/users` (41).
- **Drive, Docs, Slides, Sheets:**
  - In Drive (53,631 records), the 4 new IDs and 4 new names are absent, and both parent folders `d_8140f09b…` and `d_175c0d7b…` exist.
  - Docs (595), Slides (132) and Sheets (356): the new IDs are absent.
- **GCal:** in 10,395 events, the 4 `event_id`s and the shared `ical_uid` are absent.
- **Trello:** the action ID is absent from 5,252 actions; the card, member and board exist.
- **Gmail:** a fixed-string grep of all 81,404 `threads/*.json` plus `users.json` found 0 files containing `1844470925517303296`, `1844835127305531392`, `CAH4q9Zb2fK7xQe1M8sPnL3vT6wR0yDc` or `CAH4q9Zc8uV1nE5kJ2mRtP7aW3xQ9bLs`. The positive control found 1 file.
- **Internal duplicates:** none. The only repeated leading values are the Drive file IDs reused as their content-table keys, which is the expected cross-table link. Each Linear issue has at most one UPDATE.

### Statement mapping and ledger

| New # (line) | Prev # | Table | Op | Record / target | Key values (after) | Check result | Basis |
|---|---|---|---|---|---|---|---|
| **1** (L11) | 1 | slack_messages | INSERT, **text changed** | `8b090dec…`, DM `D05SD5QLG94` (Julia–Frederick) | Frederick (`EMPLOYEE_0008`), 2025-09-30T20:20:00.418207Z; reply_count 1 / users 1 / latest `1759263878.305127` | Only `text` changed. The ask is reworded and the recommendation is a separate sentence. Its claims match stmts 23, 24–25, 34 and 70 (ZM Live Ops folder, shared brief, calendar sheet, calendar ticket ZOM-78), and the four buy weeks match the UA deck. The reply fields equal its single reply (2), from the same user. The author is a DM member. | NEW |
| 2 (L13) | 2 | slack_messages | INSERT | `097c95c6…`, reply to 1 | Frederick, ts `1759263878.305127` | After its parent; thread_ts_legacy = parent ts. The PNs Beta tab (`gsheets/data.json /sheets_spreadsheets/220/sheets/1`) has the Hourly Coins, Nathan's Treasure Hunt, Streak Fever and Axe Arena rows (re-read NEW). Zombie Lane is at #zombie-design 2025-09 /492. | NEW (A, rows) / REUSED (Zombie Lane pointer) |
| 3 (L15) | 3 | slack_messages | INSERT | `2e75e232…`, reply in C08R8CHB0QL | Robert (`EMPLOYEE_0016`), 2025-09-18T16:40Z | Parent `9025d428` (`C08R8CHB0QL/2025-09.json /121`, Sep 17, "*Halloween theme* for an app icon or an event", tagging Robert and Julia). After the parent; Robert is a zombie-art member. | NEW |
| **4** (L17) | 4 | slack_messages | INSERT, **thread fields changed** | `58d06bd5…`, DM `D05GU6L0XFH` | Robert, 2025-09-30T22:10:00.638114Z; thread_parent_id and thread_ts_legacy now NULL; reply_count 0 | The message is now top-level. DM members (`channels.json /450`) include Julia (`EMPLOYEE_0005`) and Robert. ts is unique. It sits between base `/…` 2025-09-30T20:46:05Z and the 2025-10.json message at 2025-10-01T03:32:57Z. created_at = ts. | NEW |
| 5 (L19) | 5 | slack_messages | INSERT | `fa3eee2c…`, C0880U9751A | Vincent, 2025-09-30T20:50:12Z | ID absent; author is a member. The "current prod build" context is `C0880U9751A/2025-09 /463` ("I just released 0.3.49 on IOS", Sep 29 21:55, re-read NEW). Advisory A9. | NEW |
| 6 (L21) | 6 | slack_messages | UPDATE | `9025d428…` | reply_count 0→1, reply_users_count 0→1, latest = stmt 3 ts | Base 0 / 0 / null (re-read), so +1 is correct. | NEW |
| — | **7 removed** | slack_messages | UPDATE | `c5431028…` (old DM parent of stmt 4) | — | Removed together with stmt 4's thread link. Nothing in the SQL still references `c5431028` or `1759248350.473459` (grep 0). The base parent is left untouched. | NEW |
| 7–12 (L23–54) | 8–13 | gmail threads + messages ×3 users | INSERT ×6 | thread `…/1844470925517303296`, Message-ID `<CAH4q9Zb…>` | Brian, 2025-09-22T09:12Z | IDs absent (grep above); history_id NULL (contract). internal_date 1758532320000 = 2025-09-22T09:12:00Z. Sat Nov 1 and Wed Oct 29 2025 fall on those weekdays. A complete Gmail search finds no base mail on "November season", "Season Pass config" or "config handoff", so nothing contradicts it. | NEW |
| **13–18** (L56–80) | 14–19 | gmail threads + messages ×3 users | INSERT ×6, **changed** | thread `…/1844835127305531392`, Message-ID `<CAH4q9Zc…>` | Brian, 2025-09-26T07:40Z. Subject `ZM3D Season Pass November config handoff: new date`; In-Reply-To, References and their headers removed; snippet re-cut; body adds "If the new date is a problem on your side, reply on this mail."; size_estimate 4085→3966 | Section 6, Gmail. | NEW |
| **19–22** (L82–88) | 20–23 | gcal_events | INSERT ×4, **transparency changed** | `evt_9a4c…`, `evt_5c1e…`, `evt_a72f…`, `evt_1d6b…` | `transparent`→`opaque`; 2025-10-08 15:00–16:00Z; created 2025-09-24, updated 2025-09-26 | All 10,395 base events are `opaque`, so this matches. IDs and ical_uid are absent. All 4 calendars exist. Start and end are plan fields. 15:00–16:00Z = 18:00–19:00 Istanbul (UTC+3), as the description states. | NEW |
| 23–24 (L90–92) | 24–25 | drive_files | INSERT ×2 | `d_5f2c8e1b…` folder; `f_7c3e91a4…` doc file | parents `d_8140f09b…` (Julia's root) and `d_175c0d7b…` (Frederick's root) | IDs and names absent; parents exist. | NEW |
| **25** (L93–111) | 26 | docs_documents | INSERT, **body and style runs changed** | `f_7c3e91a4…` brief | Body 2,704 chars (BMP only, so UTF-16 = chars; 0 CR); 9 style runs | Section 6, Docs. | NEW |
| 26–33 (L113–127) | 27–34 | drive_files + slides ×7 | INSERT | `f_2b9d4e7a…` UA deck, 3 slides | Frederick, 2025-09-23 | IDs absent; readable through its text elements. W1 Mon Oct 6 – W4 Sun Nov 2: all 8 weekday labels re-checked NEW. | NEW |
| 34–37 (L130–133) | 35–38 | drive_files + sheets ×3 | INSERT | `f_e4a17c90…` calendar sheet | Julia owner, Frederick reader; parent = stmt 23 | IDs absent; the parent is created earlier in the script; header rows only. | NEW |
| 38–39 (L138–139) | 39–40 | github_reviews / review_comments | INSERT ×2 | `#470#rev_10`, `#470#rc_10` | Arthur (`EMPLOYEE_0025`, `/users` "Arthur Blake"), 2025-09-30T16:04:12Z | Keys absent; base maxima are rev_9 and rc_9. The path `…/CollectAndWinMainScreenController.cs` exists in `root/harmonygames-Games/match3d`. `pull_request_review_id` is created in stmt 38 before 39. The content claim (Season Pass schedules already running on prod) is as recorded in the previous report's section 6 (#zombie-ops 2025-09 /21). | NEW (A, path) / REUSED (content pointer) |
| **40** (L141) | 41 | github_timeline_events | INSERT, **changed** | `#470#ev_9` | `reviewed`, actor `''`, created_at NULL, data `{"commit_id":"4935e948…"}` | Section 6, GitHub. | NEW |
| 41 (L143) | 42 | github_pull_requests | UPDATE | #470 `/pull_requests/2375` | updated_at 2025-09-30T15:51:15Z → 16:04:12Z | Moves forward and equals the review time. | NEW |
| **42–44** (L145–147) | — **new** | reviews / review_comments / timeline | INSERT ×3 | `#468#rev_3`, `#468#rc_38`, `#468#ev_6` | Arthur, 2025-09-29T15:36:41Z; path `Assets/Sprites/CollectAndWin/icn - poison - red.png.meta`; ev `reviewed` / `''` / NULL / commit `648e2c7b…` | Section 6, GitHub. There is no #468 updated_at UPDATE: base updated_at 2025-09-29T16:13:50Z (the merge) is already later than the review. | NEW |
| **45–47** (L149–153) | — **new** | pr_comments / timeline / PR #473 | INSERT ×2 + UPDATE | `#473#c_2`, `#473#ev_5` | Arthur, 2025-09-30T16:16:33Z; ev `commented` / Arthur / 16:16:33Z / `{}`; PR updated_at 15:43:58Z → 16:16:33Z | Section 6, GitHub. | NEW |
| 48–50 (L155–159) | 54–56 | pr_comments / timeline / PR #471 | INSERT ×2 + UPDATE | `#471#c_18`, `#471#ev_8` | Samuel (`EMPLOYEE_0004`), 2025-09-30T21:07:26Z | Keys absent. The base has c_1 and c_2, so c_18 is a gap in an unlisted field, not a finding. ev_8 follows ev_7 `closed`, in base `commented` shape. updated_at 15:52:24Z → 21:07:26Z moves forward. "iOS 50 and Android 135" is NEW-verified: `C05433XK267/2025-09.json /1123` (Match 3D iOS Submission #50, success 19:15:49Z) and `/1124` (Android Submission #135, success 20:13:09Z). Both come before the comment and after the #471 merge. | NEW |
| **51** (L161) | 57 | slack_messages | INSERT, **changed** | `c778c9b9…`, #470 mirror in `c2b9c903` | subtype `bot_message`→NULL; pretext handle → `arthur.blake` | Section 6, mirrors. | NEW |
| 52 (L163) | 58 | slack_messages | UPDATE | `c2b9c903…` (`C093LEZGF6J/2025-09 /579`) | reply_count 16→17, latest `1759248252.248252` | Base 16 replies counted (= reply_count). Base latest `1759247478.371389` (15:51:18) is earlier than the new one. reply_users_count stays 1 because the new reply is the same bot. | NEW |
| **53–54** (L165–167) | — **new** | slack_messages | INSERT + UPDATE | `dacaa8f6…`, #468 mirror in `4b7c4127` (`/530`) | ts `1759160201.160201` (09-29 15:36:41); parent reply_count 41→42; latest kept at `1759162433.383449` | Section 6, mirrors. | NEW |
| **55–56** (L169–171) | — **new** | slack_messages | INSERT + UPDATE | `c85ccb18…`, #473 mirror in `d05a2f8a` (`/605`) | ts `1759248993.248993`; parent 2→3; latest `1759248993.248993` | Section 6, mirrors. | NEW |
| **57** (L173) | 65 | slack_messages | INSERT, **changed** | `a0c26779…`, #471 mirror in `da3fe08c` | subtype→NULL; handle → `samuel.turner`; issuecomment id `3349327810`→`3353762954` | Section 6, mirrors. | NEW |
| 58 (L175) | 66 | slack_messages | UPDATE | `da3fe08c…` (`/583`) | 7→8, latest `1759266446.266446` | Base 7 replies; base latest `1759247547.085249` is earlier than the new one. | NEW |
| — | **43–53 removed** | github ×11 | INSERT / UPDATE | #370 `rev_1`/`rc_1`/`ev_5` + PR bump; #438 `rev_4`/`rc_74`/`ev_9` + PR bump; #454 `c_4`/`ev_6` + PR bump | — | No remaining statement references #370, #438 or #454, or these keys (grep 0). The two `rev_1` hits are substrings of `#470#rev_10`. The `rc_38` review link points to the new `#468#rev_3`. The removed text moved to #468 (stmt 43), #473 (stmt 45) and Linear `cmt_zom465_2` (stmt 79). The base PRs are left untouched. | NEW |
| — | **59–64 removed** | slack ×6 | INSERT / UPDATE | #370, #438 and #454 mirrors and their parent bumps (`d648cbe9`, `2f138acf`, `ef414467`) | — | No remaining reference (grep 0). The base parents keep their base counts. | NEW |
| 59–63, 65–74, 76–78, 81, 83, 85–87, 89–95, 97–103 | 67–71, 73–82, 84–86, 88, 90–93, 95–101, 103–109 | linear_comments + issue UPDATEs (updated_at-only) | INSERT / UPDATE | 22 issues (section 6 table) | ISO `…Z` text | Byte-identical. NEW checks: comment after issue creation; updated_at moves forward from base and is at or after the latest comment; sequences are 1..n in time order; authors resolve; each comment's topic and author fit the ticket's title, state, assignee or creator (NEW read of all 22 base tickets). ZOM-521/526 detail is REUSED from the previous report's section 6 (pointers recorded). | NEW / REUSED (ZOM-521/526 base unfurl facts) |
| **64** (L187) | 72 | linear_issues | UPDATE, **changed** | ZOM-565 (`/issues/3642`) | `Todo`→`Done`; completed_at = updated_at = 2025-09-29T17:10:00Z; started_at stays NULL | Section 6, Linear. | NEW |
| **75** (L203) | 83 | linear_issues | UPDATE, **changed** | ZOM-432 (`/issues/3499`) | `Todo`→`Done`; completed = updated = 2025-09-30T21:20:00Z | Section 6, Linear. | NEW |
| **79** (L209) | — **new** | linear_comments | INSERT | `cmt_zom465_2` on ZOM-465 (`/issues/3534`) | Marcus (`usr_c77c50cc…` = marcus.bennett, the assignee), 2025-09-30T18:05:00Z, sequence 2 | ID unique. Created after `cmt_zom465_1` (Sep 26 18:10, sequence 1). Section 6. | NEW |
| **80** (L210) | 87 | linear_issues | UPDATE, **changed value** | ZOM-465 | updated_at base 2025-09-23T14:16:25Z → 2025-09-30T18:05:00Z (was 09-26T18:10) | Moves forward and equals the latest comment (79). | NEW |
| **82** (L213) | 89 | linear_issues | UPDATE, **changed** | ZOM-344 (`/issues/3403`) | `Todo`→`Done`; completed = updated = 2025-09-16T16:20:00Z | Section 6, Linear. | NEW |
| **84** (L216) | — **new** | linear_issues | UPDATE | ZOM-387 (`/issues/3450`) | `Todo`→`In Progress`; started_at 2025-07-25T13:20:00Z; time_in_status_minutes 307507→NULL; updated_at unchanged (2025-07-27T20:46:47Z) | Section 6, Linear. Advisory N1. | NEW |
| **88** (L222) | 94 | linear_issues | UPDATE, **changed** | ZOM-471 (`/issues/3541`) | `Todo`→`Done`; completed = updated = 2025-09-17T16:45:00Z | Section 6, Linear. | NEW |
| 94 (L231–238) | 100 | linear_issues | UPDATE | ZOM-521 description + updated_at | unchanged from the previous version | Byte-identical. The previous report's NEW byte comparison (two one-character unticks) and SC-15 analysis are REUSED. | REUSED |
| **96** (L241) | 102 | linear_issues | UPDATE, **changed** | ZOM-542 (`/issues/3617`) | `Regression`→`Done`; completed = updated = 2025-09-22T18:40:00Z | Section 6, Linear. | NEW |
| **104** (L253) | 110 | linear_issues | UPDATE, **changed** | ZOM-566 (`/issues/3643`) | `Todo`→`In Progress`; started_at 2025-09-30T17:20:00Z; updated 2025-09-30T19:40:00Z | Section 6, Linear. | NEW |
| 105 (L255) | 111 | trello_actions | INSERT | `68dac820…` commentCard | Brian (`/members` `d1cd0fef…`), 2025-09-29T17:55:44Z | ID absent; the card, board and member exist. "Mon Oct 13" 2025 is a Monday. | NEW |
| 106 (L257–260) | 112 | trello_cards | UPDATE | `6851a724…` | badges.comments 1→2; dateLastActivity 2025-06-30T16:56:34Z → 2025-09-29T17:55:44Z | Base comments 1 (re-read), so +1 is correct. Moves forward and equals the action date. | NEW |

## 6. Checks

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | Every new key is absent from its complete base collection and unique in the SQL (section 5 scans). Every target and actor resolves:<br>• 5 Slack thread parents;<br>• 4 GitHub PRs;<br>• 2 Drive parent folders, plus the folder created in stmt 23;<br>• the Trello card, board and member;<br>• 22 Linear issues and 10 Linear users.<br>The new GitHub rows use `EMPLOYEE_0025` (Arthur Blake), a single base login. The new Linear comment uses Marcus's single account, and he is the ticket's assignee. The new Slack rows use the base GitHub app user `SLACK_BOT_0004_SLACK_ID`. The listed ID contracts hold: Gmail history_id is NULL, and no Drive content_path is set. All injected Drive files are readable (doc body_text, slide text elements, sheet grid). No second account for an existing person (lint identities: 0). For the removed statements, nothing left in the SQL depends on them. |
| B — SQL structure and supported schema rules | PASS (provisional) | 106 statements parse with balanced quotes and nothing left unparsed. Column and value counts match on all 75 INSERTs, with no duplicate columns. No UPDATE assigns a column twice, and every WHERE is `id = '<literal>'`. No NOT NULL column without a default is omitted, and no NULL goes into a NOT NULL column (snapshot). No generated column (`text_fts`, `body_text_fts`) is written. All 122 `*_json` literals parse. All Linear `*_at` values are `YYYY-MM-DDTHH:MM:SSZ`. There are no casts, `now()` or random functions. `time_in_status_minutes = NULL` goes into a nullable column. The `state_id` values `Done` and `In Progress` are literal names already used by team_ZOM (427 and 15 issues). The snapshot comparison is a MISMATCH on the same columns as before (A1). |
| C — Dates, relationships and consistency | PASS | **Clock:** every event timestamp is at or before 2025-10-01T07:00Z (the latest is stmt 4, 2025-09-30T22:10Z). Only the gcal start and end (2025-10-08) are later, and they are plan fields.<br>**Threads:** Slack thread counts and latest_reply values are correct for all 5 parents. Linear chronology holds for all 22 issues. Gmail threading is coherent.<br>**Consistency:** the changed and new statements agree with the base and with the other injected records (detail below). No grader-facing text. |

### Check C detail: changed, new and removed groups

**Slack DM rows (1, 4; removed UPDATE prev 7).**

- Stmt 1 changes only its text. Its reply fields still equal the single reply (stmt 2), from the same author. Every pointer in the new wording resolves to an injected record:
  - the ZM Live Ops folder (23);
  - the brief shared with Julia (24–25);
  - the calendar sheet in that folder (34);
  - the calendar ticket ZOM-78 (`cmt_zom78_1`, stmt 70).
- Stmt 4 is now top-level in the Julia–Robert DM (`channels.json /450`, where both are members). Both thread fields are NULL, reply_count is 0, and created_at = ts. It is ordered after the DM's last Sep 30 message (20:46:05Z) and before its Oct 1 03:32:57Z message.
- Removing the old parent bump (prev 7) leaves no dangling reference.

**Gmail (13–18).** The correction is now a standalone message under the new subject `…: new date`:

- **Threading:** in_reply_to and references are NULL, and the In-Reply-To and References headers are gone. Each user copy has its own thread `…/1844835127305531392`, and `X-GM-THRID` equals it in every copy. A new subject without reply headers starting a new thread is coherent Gmail behaviour.
- **Headers:** Subject = column, Message-ID = id suffix, Date header `Fri, 26 Sep 2025 07:40:00 +0000` = `date` = internal_date 1758872400000. mbox_from carries the same instant.
- **Labels:** Brian SENT; Julia INBOX, CATEGORY_PERSONAL, UNREAD; Frederick INBOX, CATEGORY_PERSONAL. Each `X-Gmail-Labels` header matches its label_ids.
- **Snippet:** 175 characters, an exact prefix of the whitespace-collapsed body, the same length rule as the Sep 22 mail. The thread snippet equals the message snippet.
- **Body:** "Correction to my Sep 22 mail" resolves to stmts 7–12. "Treat Fri Oct 31 as the date I am committing to and drop the Oct 29 one" supersedes it explicitly. The new sentence "reply on this mail" matches the brief's new lock rule (stmt 25).
- **Not checkable against the base:** the base export carries no `snippet` or `size_estimate` fields (limit). Non-reply base messages store `in_reply_to` as `''`, while the SQL uses NULL. The column is nullable and the unchanged Sep 22 mail does the same.

**GCal (19–22).** Only `transparency` changed, to `opaque`, which all 10,395 base events use. Everything else is as before; the clock and plan-field rules hold.

**Docs (25).** Three sentences change:

1. Plague Race is added to the beats whose window dates are not put down.
2. One-offs: "may overlap recurring beat slots … only with the latest dated approval from Product".
3. Config locks: "…its owner is told in a reply on the mail where they committed to it".

The other checks:

- **Style runs:** all 9 runs, re-derived from the new body, cover exactly their heading lines:

  | Style | Start–end | Heading |
  |---|---|---|
  | TITLE | 0–43 | ZM3D beta live-ops calendar - working rules |
  | HEADING_2 | 163–181 | Span and time base |
  | HEADING_2 | 424–429 | Scope |
  | HEADING_2 | 611–629 | When a beat starts |
  | HEADING_2 | 1230–1241 | Held or not |
  | HEADING_2 | 1728–1736 | One-offs |
  | HEADING_2 | 1936–1947 | Still to do |
  | HEADING_2 | 2165–2174 | Push copy |
  | HEADING_2 | 2491–2503 | Config locks |

  Each `end` is exclusive and stops before the `\n`, which is the base convention (base docs, for example `f_00117462…` TITLE 0–8 "Shortcut", next char `\n`). The edits add 13 chars in "When a beat starts" and 7 in "One-offs". The previous offsets therefore shift by exactly +13 (Held or not, One-offs) and +20 (Still to do, Push copy, Config locks). The byline "Frederick, Sep 24" is unstyled, as before. No run lands mid-line.
- **Content, NEW:**
  - the push sheet has a `Plague Race` row with Status `Ready` and a `Login Calendar update` row (`/sheets_spreadsheets/220/sheets/1`);
  - the translated tab is Domino-era copy (`/sheets/2`, "Domino Adventures", "Tiledozer & Luckydrop");
  - injected `#470#rc_10` says the Plague Race schedules are already on prod, which fits rule 1;
  - rule 3 matches the correction mail's "reply on this mail".

  No base record contradicts the Collect & Win window pattern. The base shows Day 2 and Day 3 reward tables, in `C09EVVCFHKR/2025-09`, Sep 19. "Product … he" persists (A6).

**GitHub (40; new 42–47; removed prev 43–53).**

- **#470 (stmt 40):** `#470#ev_9` now has the exact base shape of a review event: `reviewed`, actor `''`, created_at NULL, `data.commit_id`. Compare base #470 ev_2–ev_6 (`/timeline_events/10959–10963`). The commit `4935e948…` is #470's head (authored 2025-09-30T03:38:02Z), as in base ev_5/ev_6. ev_9 follows ev_8 `closed`, and the review is post-merge (16:04:12 vs merge 15:51:15). That ordering is chronological.

  Post-merge reviews are rare but have base precedent: 4 of 2,206 reviews. One is Arthur's own `GameOfDominoes#1578#rev_2`, 6h18m after merge, whose reviewed event is also numbered after `merged`.
- **#468 (42–44):**
  - **Times:** the PR was created 2025-09-26T20:16:25Z and merged 2025-09-29T16:13:50Z (`/pull_requests/2372`). The review at 15:36:41Z comes after the last base review (rev_2, 09-26T21:54:00Z) and 37 minutes before the merge. No updated_at bump is needed.
  - **Numbering:** rev_3 and rc_38 follow base rev_2 and rc_37, and their `seq` values match.
  - **Path:** the path exists in the PR (base `rc_32` path) and in `root/harmonygames-Games/match3d`.
  - **Reviewed commit:** the event's commit is the head `648e2c7b…`, authored 2025-09-26T22:03:06Z, before the review.
  - **Ordering:** ev_6 is numbered after base ev_4 `merged` and ev_5 `closed`, although the review is pre-merge (advisory N2).
  - **Content:** Claire Morgan is the Art Lead (roster) and commits art to ZM3D (`C05433XK267/2025-09` builds "changes from claire.morgan"). The C&W bottle and vial visuals were still being changed on Sep 19 (`C3DD99314033/2025-09 /5`, `/27`). No base record says the final vial sprites were delivered.
- **#473 (45–47):**
  - **Times:** the PR was created 15:41:05Z and self-merged 15:41:20Z by Oliver (`EMPLOYEE_0003` = Oliver Brooks). The comment at 16:16:33Z is 35 minutes after the merge.
  - **Precedent:** 11 of 643 base PR comments are post-merge, including human ones such as `GameOfDominoes#926#c_1`, 41 minutes after merge.
  - **Numbering and shape:** c_2 follows base c_1. ev_5 follows ev_4 `head_ref_deleted` in base `commented` shape (actor, created_at, `{}`). updated_at moves forward from 15:43:58Z.
  - **Content:** #473 "Addressables/sp" is Oliver's Season Pass addressables PR (commit `72b0ab93` "setting addressables for season pass objects"), and Oliver is also ZOM-552's assignee. So "Oliver is taking the date change" fits.
- **Removed #370, #438 and #454 records:** nothing left in the SQL depends on them (grep 0).

**#zombie-prs mirrors (51, 53–57; removed prev 59–64).**

- **Text and author:** each mirror's attachment `text` equals its GitHub body byte for byte. Its pretext author handle equals the GitHub author (`EMPLOYEE_0025` → `arthur.blake`, `EMPLOYEE_0004` → `samuel.turner`, both base handles). Review comments use `#discussion_r…` and PR comments use `#issuecomment-…`, as in the base. Title, footer, color, `mrkdwn_in` and `subtype` null all match the base comment-mirror shape. A COMMENTED review with an empty body gets no separate "Review comment by" message, as in the base: Owen's #470 rev_3 and rev_5 have only their `Comment` mirrors (`/596`, `/598`).
- **ID numbering:** monotonic and at base rates.
  - Discussion IDs: base #468 `2383566804` (09-26 21:54) < injected #468 `2388843617` (09-29 15:36) < base #471 `2389372779` (09-29 22:04) < base #470 `2389766458` (09-30 03:44) < injected #470 `2389987213` (09-30 16:04). The injected #468 interval runs at about 80k/h, against about 82k/h in the base neighbour.
  - Issuecomment IDs: base #473 `3352799089` (15:41) < injected #473 `3352918642` (16:16) < injected #471 `3353762954` (21:07), at about 180–200k/h, as in the base.
- **#468 thread (`4b7c4127`, `/530`):** base reply_count 41 (= 41 replies counted), latest `1759162433.383449` (the merge broadcast, 09-29T16:13:53). The injected reply at 09-29T15:36:41 falls between base `/570` (09-26 21:54:03) and `/575`. The UPDATE to 42 is correct, and latest_reply correctly stays at the later base reply. reply_users_count stays 1 because the same bot posts.
- **#473 thread (`d05a2f8a`, `/605`):** base reply_count 2, latest `1759246882.921709` (15:41:22). The injected reply at 16:16:33 is later, so 3 and the new latest are correct.
- **#470 thread (`/579`):** base 16, latest 15:51:18 → 17, new latest 16:04:12. Correct.
- **#471 thread (`/583`):** base 7, latest 15:52:27 → 8, new latest 21:07:26. Correct.
- **Parent identities:** every parent is that PR's "opened" message; its thread ts is 3 seconds after the PR's created_at.
- **Removed mirrors and bumps (prev 59–64):** nothing left in the SQL references them.
- **Minor shape gaps** (advisory N3):
  - the injected message ts equals the GitHub second, whereas all 956 base comment mirrors post 1 s or more later (most 2–9 s);
  - the attachment text keeps a raw `&` (in "Collect & Win"), whereas the base escapes it as `&amp;` (1,866 against 1).

**Linear issue UPDATEs (64, 75, 80, 82, 84, 88, 96, 104).**

Base conventions for team_ZOM (553 issues):

| State | Issues | completed_at set | started_at null | updated_at = completed_at | tis null |
|---|---|---|---|---|---|
| Done | 427 | 427 | 120 | 401 | 57 |
| In Progress | 15 | 0 | 0 | — (started_at always set) | 12 |

In all 15 In Progress issues, updated_at equals started_at.

`time_in_status_minutes` is a cache measured at 2026-02-13T19:33Z from the last state change (SC-22). For example, ZOM-387: created 2025-07-15T06:26:50Z + 307,507 min = 2026-02-13T19:33Z.

| Issue | Post-SQL lifecycle | Same-ticket comments / related notes | Result |
|---|---|---|---|
| ZOM-565 (64) | Todo→Done; created 09-25T13:46:04Z; started NULL; completed = updated 09-29T17:10Z; tis NULL as in base | `cmt_zom565_1` (Marcus, creator, 09-29T16:05Z): "…(commit f7e971b0)… can close". Commit `f7e971b0` "Endless Mode start screen VFX" by Marcus was authored 2025-09-25T13:25:12Z. Base unfurls show Todo at 09-25 13:46 and 09-29 14:34 (`D05U73FNDDL/2025-09 /116`, `/131`), both before the completion. | Consistent; Done shape matches the base. Advisory N4 (the 14:34 "I wrote a comment" pointer). |
| ZOM-432 (75) | Todo→Done; completed = updated 09-30T21:20Z | `cmt_zom432_1` (Calvin, assignee, 09-24): "frame is the last piece". `#471#c_18` (Samuel, 09-30T21:07:26Z): "daily-gift frame went out with this PR… can be closed". #471 merged at 15:52:24Z and contains commit `f0bb8b48` "Fixing UI Elements on Daily Gift… update header image" (09-27) and the `Daily Gift/img - DailyGift.png.meta` path (base `rc_2`). | Consistent: closed 13 minutes after the closing note. |
| ZOM-465 (79, 80) | In Progress (base started 09-23T14:16:25Z); updated → 09-30T18:05Z | `cmt_zom465_1` (09-26T18:10Z) "every event icon animates" → `cmt_zom465_2` (09-30T18:05Z) "Collect & Win came in after my note above … still to do". #468 "Collect And Win" was opened 09-26T20:16:25Z, after the 18:10 note, and merged 09-29. The base unfurl `D076V3NB6P7/2025-09 /67` shows In Progress on 09-23. | Consistent; a supported later narrowing (N6). |
| ZOM-344 (82) | Todo→Done; completed = updated 09-16T16:20Z | `cmt_zom344_1` (Marcus, creator and assignee, same instant): "Art side is signed off". The only base Slack mention is 07-04, and no GitHub record names it. | Consistent. |
| ZOM-387 (84) | Todo→In Progress; started 07-25T13:20Z; tis 307507→NULL; updated stays 07-27T20:46:47Z (≥ started) | `cmt_zom387_1` (Owen, 07-25T14:00Z) comes after started_at. "The three events we already had" matches the description (begin_level, left_level, notification_permission, quoted in base `#319#c_1`). Children: ZOM-442 In Validation (started 07-30) and ZOM-444 Done (started 07-28). Linked PR #319 "ZOM-387" (branch `Blake/ZOM-387`) was merged 07-19, six days before started_at. | Ordering valid (started ≥ created, updated ≥ started). Nulling tis removes a cache that would otherwise say "in Todo since creation". Advisory N1. |
| ZOM-471 (88) | Todo→Done; completed = updated 09-17T16:45Z | `cmt_zom471_1` (Samuel, assignee, same instant). The base unfurl at creation (08-13) shows Todo. No later record shows it open. The base commit `fcf7692f` "Hide red Dot from quest icon" (08-25) is a different feature. | Consistent. Priority untouched (SC-71). |
| ZOM-542 (96) | Regression→Done; started NULL; completed = updated 09-22T18:40Z | `cmt_zom542_1` (Samuel, assignee, same instant) fits Robert's ask (`C08R8CHB0QL/2025-09 /87`, 09-14). The later Samuel commit `0e5a3c9d` "Fixing UI Elements on Home screen" (09-23T00:12Z) belongs to ZOM-498 (Done 09-30, in PR #471), a different ticket, so there is no conflict. | Consistent. |
| ZOM-566 (104) | Todo→In Progress; created 09-30T16:26:02Z; started 17:20Z; updated 19:40Z | The base unfurl at 16:26:31Z shows Todo, before started_at. `cmt_zom566_1` (Owen, assignee, 19:40Z). Brian sent the ticket to Owen ("I prepare the collect&Win logs", `D07E9PSQB6W/2025-09 /3`), and Owen is the #468 author (`PERSON_5877` = Owen Baker). | Consistent; In Progress shape (started_at set) matches the base. |

All 22 targeted issues, whether their state changed or not, satisfy the following:

- comments come after creation;
- started ≥ created;
- completed ≥ started (or ≥ created when started is null);
- updated ≥ completed and ≥ started;
- updated moves forward from base and is at or after the latest comment;
- sequences are 1..n in time order.

**Unchanged statements.**

- Topic and actor fit for all 22 Linear comments was re-read NEW against the base tickets: author = assignee, creator or a named tester, and the topic matches the title or description. No incompatible fact was found.
- The supported later correction `cmt_zom429_1` → stmt 5 (Vincent, Sep 30) remains.
- ZOM-521 / ZOM-526 (stmts 67–69, 93–94) are REUSED from the previous report's section 6: the base Sep 17 unfurl `D0770ET6WBW/2025-09 /198`, the child states, and the SC-15 repair.

## 7. Findings

**No demonstrated defects.**

### Advisories (do not affect the verdict)

Carried from the previous report and still applicable:

- **A1 · schema snapshot mismatch (local `01ef5792…`):** the SQL writes these columns, which the snapshot lacks:
  - `gcal_events.extras_json`;
  - `drive_files.drive_id`;
  - `slides_pages.notes`;
  - `slides_page_elements.table_json` and `ordinal`;
  - `github_review_comments.pull_request_review_id`, `side`, `start_line`, `start_side`, `subject_type` and `seq`;
  - `github_reviews.seq`;
  - `linear_comments.sequence`.

  This is the same set as before. If the live database lacks any of them, the script will not load. The semantics of `sequence` are unknowable from the base, which has no Linear comments.
- **A6 · authority wording (25):** the brief says "the latest dated approval from Product, and if he takes that back". The only approver and retractor in the data is Robert (Co-Founder & Creative Director, Executive). Julia is the Product Manager. Both readings lead to the same outcome: Halloween comes off the calendar either because the approval was retracted or because no Product approval exists. `/prompt` should confirm the intended mapping.
- **A9 · loose build reference (5):** "the current prod build" names no version. The base context is the iOS 0.3.49 release (`C0880U9751A/2025-09 /463`).
- **A10 · rules in a DM (2):** some scope rules sit in a DM reply rather than in the brief.
- **A11 · SC-15 repaired, not avoided (93–94, unchanged):** record the repair in `hazard_acknowledgements`.
- **A12a · wording beside the unticked item (93, unchanged):** "Everything the live-ops side asked for is in" sits beside the unticked "Tokens traveling to live-ops" item.

New in this revision:

- **N1 · ZOM-387 started_at after its linked PR merged (84):** the SQL starts the issue on 2025-07-25T13:20Z. Base PR #319, titled "ZOM-387" on branch `Blake/ZOM-387`, merged on 2025-07-19T16:55Z with most of the analytics events. In the base, started_at sometimes follows the linked PR's merge, but only by hours (ZOM-366: 3h20m; ZOM-352: 1 minute). This is not impossible, because started_at is a manual state-change time. It is still the least natural date in the set. Two fixes would make it natural:
  - set started_at at or before 2025-07-19T00:40:58Z (PR #319 opened), keeping the Jul 25 comment as progress; or
  - leave the issue in Todo.

  Separately, nulling `time_in_status_minutes` touches SC-22. Record it in `hazard_acknowledgements` as `resolution: repaired`.
- **N2 · #468 timeline ordering (44):** `#468#ev_6` (`reviewed`, created_at NULL) is numbered after base ev_4 `merged` and ev_5 `closed`, although its review (`rev_3`, 15:36:41Z) is pre-merge. Base numbering is chronological; only post-merge reviews are numbered after `merged` (3 of the 4 base cases). This follows from the append-only constraint and creates no timestamp contradiction, because the review row carries the correct time. A reader of the timeline alone would see a review after closing.
- **N3 · mirror realism (51, 53, 55, 57):**
  - The injected Slack ts is in the same second as the GitHub event. Base mirrors post 1 s or more later: 0 of 956 have a 0 s delay, and most take 2–9 s. Adding 2–5 s to each mirror `ts` and `created_at` would fix it; the parents' `latest_reply` values must change to match.
  - Raw `&` appears in attachment `text` where the base uses `&amp;` (1,866 against 1). This affects exact-string searches for "Collect &amp; Win" against "Collect & Win".
- **N4 · comments missing from the base export:** the base export has 0 Linear comments, yet the base shows comments existed:
  - ZOM-565 has a comment-surface image (`/attachments/959`), and Marcus's DM at 09-29T14:34Z says "i wrote a comment on the linear task" (`D05U73FNDDL /131`);
  - ZOM-471 (`/attachments/868`);
  - ZOM-542 (12 comment-surface attachments).

  The injected comments therefore take sequence 1. On ZOM-565 the only visible comment (16:05Z) comes after Marcus's 14:34Z pointer. The pointer most plausibly refers to the unexported base comment, so this is a pre-existing gap rather than introduced chronology. `/prompt` should not rely on comment counts or on that pointer.
- **N5 · state history:** the 7 state-changing UPDATEs change `state_id` but not `state_history_json`. The snapshot lists that column as NOT NULL, and the export has no history field to compare with. If the live Linear tool shows state history, it will not include these transitions. This is outside static certification.
- **N6 · C&W icon animation versus ZOM-521 (79 vs 94):** `cmt_zom465_2` (Sep 30) says the C&W event icon animation is still to do. ZOM-521's Sep 26 checklist ticks "Live-ops icons appearing on the screen and animations on these icons". The phrase "came in after my note above" and the #468 timing (opened Sep 26 20:16Z) reconcile them as a later addition. This is the SC-15 area, a `/prompt` hand-off.
- **N7 · known base-data areas touched:**
  - SC-15 (ZOM-521, unchanged);
  - SC-16 pattern: five tickets are now closed with dated reasons, and none of the SC-16-named tickets is touched;
  - SC-22 (ZOM-387 tis);
  - SC-38: Season Pass is touched by `#473#c_2` ("premium strip … November range") and `cmt_zom552_1`;
  - SC-71: ZOM-471's priority is not touched; only its state changed.

  `/prompt`, `/oe` and `/rubric` decide dependence.

## 8. Limits

- **Outside the static scope:**
  - live execution and deploy-time schema compatibility (A1, including the `linear_comments.sequence` semantics and the `state_history_json` behaviour in N5);
  - search ranking and Agent visibility;
  - task difficulty.
- **Not checkable against the base:** the export has no Gmail `snippet` or `size_estimate` fields and no Linear comments or state history. Results stated against these use the SQL's internal consistency only.
- **Bounded searches:** the contradiction searches for Season Pass dates (Slack 2025-09, limit reached) are bounded. No required check depends on them; the Gmail checks were complete.
- **Workspace adaptation:** no input-store save, no `hg_write_output.py`, no `input_manifest.json` write. Section 9 gives the entry.
- No required static check is unresolved.

## 9. Stage dependencies (for reuse)

| Dependency | Value |
|---|---|
| SQL | SHA `c955d6ca…1cf2` |
| Universe manifest | `da2f4cf0…a1a` |
| Local schema snapshot | `01ef5792…6eb` (A1 set identical) |
| id_contracts | `fc4711ef…82` |
| Clock | 2025-10-01T07:00Z |
| Lint | injection-lint-v1 (0 flags) |

**New facts recorded this run:**

- **GitHub:**
  - PR times:

    | PR | Pointer | Created | Merged | Base updated_at |
    |---|---|---|---|---|
    | #468 | `/pull_requests/2372` | 09-26T20:16:25Z | 09-29T16:13:50Z | 09-29T16:13:50Z |
    | #470 | `/2375` | — | 09-30T15:51:15Z | — |
    | #471 | `/2376` | — | 09-30T15:52:24Z | — |
    | #473 | `/2378` | 15:41:05Z | 15:41:20Z | 15:43:58Z |

  - Base maxima: #468 rev_2 / rc_37 / ev_5; #470 rev_9 / rc_9 / ev_8; #473 c_1 / ev_4.
  - Base reviewed-event shape: `''` / NULL / commit_id.
  - Post-merge reviews: 4 of 2,206.
- **Slack:**
  - #zombie-prs parent counts: `4b7c4127` 41 / latest `1759162433.383449`; `d05a2f8a` 2 / `1759246882.921709`; `c2b9c903` 16; `da3fe08c` 7.
  - Mirror delay: at least 1 s in 956 of 956.
  - DM `D05GU6L0XFH` = Julia + Robert.
- **Linear:**
  - team_ZOM conventions (Done: started_at null 120 of 427, updated = completed 401 of 427; In Progress: updated = started 15 of 15);
  - `time_in_status_minutes` is measured at 2026-02-13T19:33Z;
  - ZOM-387 is linked to PR #319 (merged 07-19).
- **Builds:** iOS Submission #50 and Android Submission #135 succeeded on 2025-09-30 (`C05433XK267 /1123`, `/1124`).
- **Collisions:** all collision scans listed in section 5.

Manifest entry that would be written:

```json
{"review_version": "injection-static-v2", "evidence_contract": "stage-evidence-v1", "input_sha256": "c955d6ca2bca5d1aa0c457e3107a28e8210903a833b3192a54d1e5337adc1cf2", "reused_evidence": [{"source_report": "R/prev/0_injection.previous_report_on_837d4f5d.md", "sha256": "e19b226bc538c49b02f6249aa127c22098a5f95c2898649af9428407fb6b7a32", "ledger_items": ["stmt 2 Zombie Lane pointer (#zombie-design 2025-09 /492)", "stmts 38-39 Season Pass prod pointer (#zombie-ops 2025-09 /21)", "stmts 67-69 and 93-94 ZOM-521/526 section-6 analysis and byte comparison"], "dependencies": {"universe_manifest": "da2f4cf0…a1a (unchanged)", "schema_snapshot": "01ef5792…6eb (unchanged)", "id_contracts": "fc4711ef…82 (unchanged)", "clock": "2025-10-01T07:00Z (unchanged)", "statements": "byte-identical (statement diff)"}, "not_reused": "all collision, reference, thread-count, chronology, clock and Check B results (re-run NEW); content rows whose prior provenance pointed to the unsupplied report 51ac8433 (re-verified NEW)"}]}
```

`/prompt` may rely on this stage for SQL `c955d6ca…1cf2`.

## 10. Next action

Proceed to `/prompt`. Because the SQL changed, any earlier `/prompt`, `/hardness`, `/oe` and `/rubric` result for `837d4f5d` is outdated: rerun them in that order. Carry A6, N1, N4 and N6 into `/prompt`. Optionally fix N1 (ZOM-387 started_at) and N3 (mirror delay) before then.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt

Evidence limits: Static scope only. Live deploy compatibility is unverified: the bundled snapshot (`01ef5792…`) lacks several columns the SQL writes, including `linear_comments.sequence` (A1). Gmail snippet and size and Linear comments and state history cannot be compared with the base export.
