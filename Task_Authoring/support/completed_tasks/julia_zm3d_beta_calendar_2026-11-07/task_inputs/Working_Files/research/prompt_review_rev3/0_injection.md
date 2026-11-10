# Injection data-integrity review: Eval 0

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. Base facts reused from the previous `injection-static-v2` report (`R/prev/0_injection.previous_report_on_3afbf7cb.md`, SHA-256 `51ac84336418da1b4a0e78d83bc93304bd2bfcb10e56dfc14bdd7e3c457757dd`) only for byte-identical statements. Every changed or new statement was checked NEW. Every ID-collision, reference, Slack-thread, Linear-chronology, clock and Check B check was also rerun NEW for the whole file. |
| Mode | Independent chat review, audit. Workspace adaptation: report written to `R/out/0_injection.md`; the input store, the output writer and `input_manifest.json` were not used (section 9 gives the manifest entry). |
| Review time | 2026-11-06 |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`; `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` (re-hashed; same as the previous report) |
| Input | `R/inputs/01_Universe_Inject.sql`, 62,399 bytes, 276 lines, SHA-256 `837d4f5dedbdedb0febe279f64b5df61f0debdf29e93ef779a4ddd5ff754d76b` (re-hashed). Not executed. |
| Previous version | `R/prev/01_Universe_Inject.previous_3afbf7cb.sql`, 61,537 bytes, SHA-256 `3afbf7cbbdb7611dad909cfc7244829642e03e136b66c5c555fe77d28570dd63` (PASS / COMPLETE in the previous report) |
| Schema snapshot | `Evals/references/schema/injection.json` SHA-256 `01ef579236212034a43a53914754f86ed9248be48c961009cef5b4bd6106f6eb`. This is **not** the snapshot the previous report names (`31dcb2b4…5151`, the Portal copy), so no schema-dependent result was reused. Check B was redone in full against the local snapshot (unverified, provisional). |
| ID contracts | `Evals/references/schema/id_contracts.json` SHA-256 `fc4711ef07667333c1cf2a417279826f0432539195f7acdfacfa86e9d9ed4682` (re-hashed; same as the previous report) |
| Linear source | `linear/data.json` manifest SHA-256 `b49ec9e856cf0b295bd3d6edb1d21673f7fd33b516dcb159e602ca9128953b4d`, freshness `297033cb…893b` |
| Lint | `hg_injection_lint.py` injection-lint-v1 via `Task_Authoring/tools/hg.py lint` |
| Known base issues | `Task_Authoring/references/known_data_issues/synthcut.md` (Portal copy of the card list; SC-15, SC-16, SC-38 touched) |
| Other inputs | `00_Task_Assigned_Inputs.md` (sha `e8b82698…49eb`), `02_Universe_Date.txt` ("Oct 1, 2025 (synth-cut)", sha `2f0af108…c519`), `04_Prompt.txt` (sha `2a23afd8…2beb`): context only |

## 2. Input / authority issues

- The SQL header comments point to a grounding dossier and to `Task_Authoring/references/universe_schema_live.json`. Neither was supplied. They are treated as statements of intent, not evidence. No SQL comment changed in this revision, and no comment is about padding, tool calls, pass rates or gates.
- **Schema snapshot provenance:** the previous report's Check B used the Portal snapshot `31dcb2b4…`, while the local bundle carries `01ef5792…`. Reuse condition 2 fails for schema-dependent results, so Check B is NEW. The local snapshot gives the same mismatch set as the previous report's advisory A1 (see A1).
- **Previous-report provenance:** many previous ledger rows say only "Unchanged | REUSED" and point to an earlier report (`dad52a1a…f3db`) that was not supplied. For those rows the claim-level evidence was not carried forward (reuse condition 1). So this review re-verified NEW, for the whole file:
  - every ID collision;
  - every reference target;
  - every Slack thread, member and timestamp fact;
  - Linear chronology;
  - the clock sweep;
  - the base ticket each unchanged Linear comment sits on.

  Content facts were REUSED only where the previous ledger recorded the claim and its source pointer.
- **Previous-report numbering slip:** the ledger rows for ZOM-543 cite statements "74–75". In SQL `3afbf7cb` they were statements 73–74. This is provenance only, and the facts were re-verified here.
- **Latent issue fixed in this revision:** in SQL `3afbf7cb`, `cmt_zom521_1` ("Master VFX checklist is down to the last two items") sat beside the unchanged base ZOM-521 checklist, which ticks all six items (SC-15). That contradiction was not flagged by the previous PASS. The new ZOM-521 description UPDATE (statement 100) resolves it.
- No grader-facing or solver-facing text in any changed record (lint plus a manual read).

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, manifest, review version | NEW, done (workspace adaptation: hashes recorded here; no store write) |
| Diff against the previously reviewed SQL | NEW, done, statement by statement (comment-stripped, quote-aware parser): <br>• new 1–75 = prev 1–75, byte-identical <br>• prev 76 (`UPDATE ZOM-526 updated_at '2025-09-24T17:30:00Z'`) → new 76 (INSERT `cmt_zom526_2`) + new 77 (`UPDATE ZOM-526 updated_at '2025-09-26T15:40:00Z'`) <br>• new 78–99 = prev 77–98, byte-identical <br>• prev 99 (`UPDATE ZOM-521 updated_at`) → new 100 (`UPDATE ZOM-521 SET description = …, updated_at = '2025-09-26T17:25:00Z'`) <br>• new 101–112 = prev 100–111, byte-identical <br>No SQL comment changed. |
| Run lint; resolve every flag | NEW, done (0 flags) |
| Inventory every statement | NEW, done. 112 statements: 78 INSERT, 34 UPDATE. No DELETE, upsert or conflict clause. Matches the lint count. |
| Check A | NEW for the whole file (complete collision scans and target checks, section 5). REUSED only for previously recorded identity facts that were not re-scanned (Gmail one-account-per-person). Result: PASS |
| Check B | NEW for the whole file against the local snapshot: PASS (snapshot mismatches advisory) |
| Check C | NEW in full for statements 76, 77 and 100. Reopened NEW for 75 (`cmt_zom526_1`), 99 (`cmt_zom521_1`) and 73 (`cmt_zom543_1`) because the change touches their tickets. NEW chronology for all Linear, Slack and Trello statements and a clock sweep of the whole file. REUSED content facts for the other byte-identical statements where the previous ledger recorded them. Result: PASS |
| Report coverage, findings, limits, verdict | done |

## 4. Lint

`hg_injection_lint.py` (injection-lint-v1) ran on SHA `837d4f5d…76b`, universe synthcut, clock `2025-10-01T07:00:00Z`.

- **Base loaded:** slack/users, gmail/users, github/data, linear/data, trello/data, contacts, confluence_working.
- **Checks run:** future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required.
- **Statements:** 112 (78 insert, 34 update).
- **Flags:** FAIL 0, CHECK 0, INFO 0. Nothing to resolve.

The local lint run does not list `json_shape`, which the Portal run listed. Every `*_json` literal was therefore parsed by hand: all parse, and the shapes match their columns (section 6, B). A clean lint is not a PASS, so checks A–C were completed in full.

## 5. Operation ledger

Statement numbers are positions in the new SQL. "NEW" means verified in this review against the base cited. "REUSED" means taken from the previous report (SHA `51ac8433…57dd`, section 5, where rows from statement 77 on were numbered one lower). Reuse needs a byte-identical statement, an unchanged universe manifest (`da2f4cf0…`), unchanged id_contracts (`fc4711ef…`), the same clock and a recorded claim with its source.

**Complete NEW collision and target scans used below**, all `scan_complete: true`, 0 errors:

- **Slack:** `lookup` over `messages/*/*.json`, 4,840 files and 610,468 records. All 10 injected message IDs are absent. All 7 UPDATE or thread-parent targets exist.
- **Linear:** `/comments` has 0 base records, so all 23 injected comment IDs are unique against the base. All 22 issue targets exist in `/issues` (3,687 records). All 10 authors exist in `/users` (41 records).
- **GitHub:** all new keys are absent:
  - `/reviews`: 2,230 records;
  - `/review_comments`: 1,387;
  - `/timeline_events`: 11,406;
  - `/pull_request_comments`: 687.

  All 5 PR targets exist in `/pull_requests` (2,475 records).
- **Drive:** in `/drive_files` (53,631 records), all 4 new IDs and all 4 new names are absent, and both parent folders exist.
- **Docs, Slides, Sheets:** the new IDs are absent from `/docs_documents` (595 records), `/slides_presentations` (132) and `/sheets_spreadsheets` (356).
- **GCal:** in `/events` (10,395 records), all 4 `event_id`s and the shared `ical_uid` are absent.
- **Trello:** the action ID is absent from `/actions` (5,252 records). The card, member and board all exist.
- **Gmail:** a literal search over all 81,404 `threads/*.json` files plus `users.json` found 0 files containing `1844470925517303296`, `1844835127305531392`, `CAH4q9Zb2fK7xQe1M8sPnL3vT6wR0yDc` or `CAH4q9Zc8uV1nE5kJ2mRtP7aW3xQ9bLs`. A substring search covers every exact match. The positive control found a known thread ID.

| # (line) | Table | Op | Record / target | Key values | Check result | Basis |
|---|---|---|---|---|---|---|
| 1 (L11) | slack.slack_messages | INSERT | `8b090dec…` DM D05SD5QLG94 | EMPLOYEE_0008 (Frederick Stone), 2025-09-30T20:20:00.418207Z; reply_count 1, latest_reply `1759263878.305127` | ID absent from base; author is a DM member; ts unique in the channel; created_at = ts; reply fields match the single reply (2). Content facts as in the previous report row 1 | NEW (A, thread) / REUSED (content) |
| 2 (L13) | slack.slack_messages | INSERT | `097c95c6…` reply to 1 | EMPLOYEE_0008, ts `1759263878.305127` | Absent from base; member; after its parent; thread_ts_legacy = parent ts. Content facts as in the previous report row 2: PNs Beta rows at `gsheets/data.json /sheets_spreadsheets/220/sheets/1`; Zombie Lane at #zombie-design 2025-09 /492 | NEW (A) / REUSED (content) |
| 3 (L15) | slack.slack_messages | INSERT | `2e75e232…` reply in C08R8CHB0QL | Robert (EMPLOYEE_0016), 2025-09-18T16:40Z | Parent `9025d428…` exists (`C08R8CHB0QL/2025-09.json /121`); reply after parent; author a member of zombie-art; ts unique | NEW |
| 4 (L17) | slack.slack_messages | INSERT | `58d06bd5…` reply in DM D05GU6L0XFH | Robert, 2025-09-30T22:10Z | Parent `c5431028…` exists (`D05GU6L0XFH/2025-09.json /675`); after parent; member; ts unique. Advisory A5 | NEW |
| 5 (L19) | slack.slack_messages | INSERT | `fa3eee2c…` C0880U9751A | Vincent Parker, 2025-09-30T20:50:12Z | Absent; member of zombie-match3d; ts unique. Content as in the previous report row 5 (C0880U9751A 2025-09 /463). Advisory A9 | NEW (A) / REUSED (content) |
| 6–7 (L21–22) | slack.slack_messages | UPDATE | `9025d428…`, `c5431028…` | reply_count 0→1, reply_users_count 0→1, latest_reply = the injected reply's ts | Base reply_count 0 and reply_users_count 0 (re-read), so +1 is correct | NEW |
| 8–13 (L24–55) | gmail threads + messages | INSERT ×6 | thread `…/1844470925517303296` for Brian, Julia and Frederick | Brian Foster, 2025-09-22T09:12Z | Thread and message IDs absent from all Gmail threads; history_id NULL (contract). Sat Nov 1 2025 and Wed Oct 29 2025 fall on those weekdays. Content as in the previous report row 8–13 | NEW (A) / REUSED (content) |
| 14–19 (L57–81) | gmail threads + messages | INSERT ×6 | thread `…/1844835127305531392` | Brian, 2025-09-26T07:40Z; Oct 29 → Fri Oct 31, 10:00 Istanbul | Absent from base; history_id NULL; Fri Oct 31 2025 is a Friday; consistent with 8–13. Advisories A2, A3 | NEW (A, dates) / REUSED (content) |
| 20–23 (L83–89) | gcal.gcal_events | INSERT ×4 | `evt_9a4c…`, `evt_5c1e…`, `evt_a72f…`, `evt_1d6b…` | 2025-10-08 15:00–16:00Z; created 2025-09-24, updated 2025-09-26 | IDs and ical_uid absent from base; start/end are plan fields; created/updated before the clock. Content as in the previous report row 20–23. Advisory A7 | NEW (A, clock) / REUSED (content) |
| 24 (L91) | gdrive.drive_files | INSERT | `d_5f2c8e1b…` folder "ZM Live Ops" | parent `d_8140f09b…` | ID and name absent; parent is Julia's root folder (`/drive_files/11673`, owner julia.lawson) | NEW |
| 25–26 (L93–112) | drive_files + docs_documents | INSERT | `f_7c3e91a4…` working-rules doc | Frederick owner, Julia reader; parent `d_175c0d7b…` | IDs absent; parent is Frederick's root folder (`/drive_files/2060`); doc row has non-empty body_text (readable). Heading runs and rule text as in the previous report row 26 | NEW (A) / REUSED (content, style runs) |
| 27–34 (L114–129) | drive_files + slides presentation, pages, elements | INSERT | `f_2b9d4e7a…` "ZM3D beta UA plan", 3 slides | Frederick, 2025-09-23 | IDs absent; text elements make it readable. W1 Mon Oct 6 – W4 Sun Nov 2 2025 all fall on the weekdays stated | NEW |
| 35–38 (L131–134) | drive_files + sheets_spreadsheets + sheets_sheets ×2 | INSERT | `f_e4a17c90…` | Julia owner, Frederick reader; parent = statement 24 | IDs absent; parent created earlier in the script; header rows only | NEW |
| 39–42 (L139–144) | github reviews / review_comments / timeline / PR #470 | INSERT ×3 + UPDATE | `#470#rev_10`, `#470#rc_10`, `#470#ev_9` | 2025-09-30T16:04:12Z | Keys absent; base maxima rev_9, rc_9, ev_8; PR `/pull_requests/2375` updated_at 2025-09-30T15:51:15Z → 16:04:12Z (forward, after merge). The file path exists in `root/…/match3d`. Content as in the previous report row 40 | NEW (A) / REUSED (content) |
| 43–46 (L146–152) | same for #370 | INSERT ×3 + UPDATE | `#370#rev_1`, `#370#rc_1`, `#370#ev_5` | 2025-09-30T19:48:33Z | Keys absent; base has no reviews or review comments, ev max 4; PR `/pull_requests/2264` updated_at moves forward. Prefab path exists in the repo | NEW |
| 47–50 (L154–160) | same for #438 | INSERT ×3 + UPDATE | `#438#rev_4`, `#438#rc_74`, `#438#ev_9` | 2025-09-30T20:41:17Z | Keys absent; base maxima rev_3, rc_73, ev_8; PR `/pull_requests/2339` moves forward. `SeasonPassMainScreen.cs` exists in the repo | NEW |
| 51–53 (L162–166) | pr_comments / timeline / PR #454 | INSERT ×2 + UPDATE | `#454#c_4`, `#454#ev_6` | Marcus (PERSON_0396), 2025-09-30T18:05:52Z | Keys absent (base max c_1: a gap in an unlisted field, not a finding); PR `/pull_requests/2357` moves forward. Advisory A12 | NEW |
| 54–56 (L168–172) | pr_comments / timeline / PR #471 | INSERT ×2 + UPDATE | `#471#c_18`, `#471#ev_8` | Samuel Turner, 2025-09-30T21:07:26Z | Keys absent (base max c_2: gap, not a finding); PR `/pull_requests/2376` moves forward. Build-number content as in the previous report row 54 | NEW (A) / REUSED (content) |
| 57–66 (L174–192) | slack.slack_messages INSERT ×5 + UPDATE ×5 | bot mirrors in C093LEZGF6J (zombie-prs) | parents `c2b9c903` 16→17, `d648cbe9` 2→3, `2f138acf` 78→79, `ef414467` 3→4, `da3fe08c` 7→8 | ts = GitHub created_at | IDs absent; parents exist; each base reply_count + 1 equals the SQL value. The new latest_reply is later than each base latest_reply; thread_ts_legacy = parent ts; ts unique. Mirror texts match their GitHub comments. Advisory A4 | NEW |
| 67–74 (L197–207) | linear comments + issue UPDATEs | ZOM-429, -556, -565, -543 | see section 6 C | | IDs unique (base /comments empty); targets and authors exist; each comment comes after issue creation; each UPDATE moves updated_at forward from base and equals the comment time; `YYYY-MM-DDTHH:MM:SSZ` | NEW (A, C chronology); content reviewed NEW against each base ticket (section 6) |
| 75 (L209) | linear.linear_comments | INSERT (unchanged, **reopened**) | `cmt_zom526_1` on ZOM-526 | Brian Foster (`usr_fc22d5941b2aeb5c`, `/users/40`), 2025-09-24T17:30:00Z, sequence 1 | See section 6 C. Agrees with the base and with 76 | NEW |
| **76 (L210)** | linear.linear_comments | **INSERT (new)** | `cmt_zom526_2` on ZOM-526 (`/issues/3600`) | Brian Foster, parent NULL, is_edited false, created = updated = 2025-09-26T15:40:00Z (08:40 PDT), sequence 2 | **Check A:** ID absent from base `/comments` (0 records, complete) and appears once in the SQL; issue exists; author resolves to brian.foster, whose email matches one Linear account (complete `/users` scan); Brian is the issue's creator. **Check B:** 9 columns and 9 values; text format; boolean literal. **Check C:** section 6 | NEW |
| **77 (L211)** | linear.linear_issues | **UPDATE (changed value)** | ZOM-526 | updated_at 2025-09-17T15:52:10Z (base) → 2025-09-26T15:40:00Z | Moves forward; equals the latest comment (76); the only UPDATE on ZOM-526; before the clock; correct format | NEW |
| 78–98 (L213–243) | linear comments + issue UPDATEs | ZOM-552, -534, -432, -78, -465, -344, -387, -442, -471, -504, -517 | | | As 67–74; ZOM-387 has no UPDATE because its comment (2025-07-25) predates base updated_at 2025-07-27 | NEW (A, C chronology); content reviewed NEW against each base ticket |
| 99 (L245) | linear.linear_comments | INSERT (unchanged, **reopened**) | `cmt_zom521_1` on ZOM-521 | Calvin Price (assignee, `/users/6`), 2025-09-26T17:25:00Z | See section 6 C: now agrees with statement 100. Advisory A12a | NEW |
| **100 (L246–253)** | linear.linear_issues | **UPDATE (changed)** | ZOM-521 (`/issues/3596`) | description: base `- [X] Tokens traveling to live-ops` → `- [ ]`, and base `- [X]   Claimed Cards traveling to inventory Section` → `- [ ]   …`; updated_at 2025-09-17T15:50:49Z → 2025-09-26T17:25:00Z | **Check A:** target exists (id = identifier `ZOM-521`). **Check B:** two distinct assignments; balanced quotes; multi-line literal with LF only (0 CR bytes); `→` preserved. Byte comparison with the base: 339 = 339 characters, 8 = 8 lines, exactly two one-character replacements (offsets 190 and 290). All other text, including the three spaces before "Claimed", is identical. Base Linear uses both `- [ ]` and `- [X]` (11 descriptions each, 4 mixed), so the representation is preserved. **Check C:** section 6 | NEW |
| 101–110 (L255–268) | linear comments + issue UPDATEs | ZOM-542, -544, -546, -549, -566 | | | As 67–74 | NEW (A, C chronology); content reviewed NEW against each base ticket |
| 111 (L270) | trello.trello_actions | INSERT | `68dac820…` commentCard | Brian Foster (member `d1cd0fef…` = `/members/9` "Brian Foster"), 2025-09-29T17:55:44Z | ID absent; card `/cards/702`, board `/boards/4` and member exist; "Mon Oct 13" 2025 is a Monday | NEW |
| 112 (L272–275) | trello.trello_cards | UPDATE | `6851a724…` | badges.comments 1→2; dateLastActivity 2025-06-30T16:56:34Z → 2025-09-29T17:55:44Z | Base comments 1, so +1 is correct; moves forward; equals the action date | NEW |

Internal duplicates: the only repeated leading values are the three Drive file IDs, each used once in `drive_files` and once in its content-table rows (Docs; Slides presentation, pages and elements; Sheets spreadsheet and sheets). That is the expected cross-table link, not a key collision. ZOM-526 has two comments with distinct IDs and sequences 1 and 2, in time order. Each Linear issue has at most one UPDATE.

## 6. Checks

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | Every new key is absent from its complete base collection and unique in the SQL (section 5 scans). Every target and actor resolves:<br>• the 7 Slack parents;<br>• 5 GitHub PRs;<br>• 2 Drive parent folders, plus the SQL-created folder used by statements 35–38;<br>• the Trello card, board and member;<br>• 22 Linear issues and 10 Linear users.<br>The new `cmt_zom526_2` author is Brian Foster's single Linear account and the ticket's creator. Listed ID contracts hold (Gmail history_id NULL; no Drive content_path). Drive files are readable (doc body_text, slide text elements, sheet grid). No second account for an existing person (lint identities: 0). |
| B — SQL structure and supported schema rules | PASS (provisional) | 112 statements parse with balanced quotes and nothing left unparsed. Column and value counts match on all 78 INSERTs. There are no duplicate columns or assignments, no NOT NULL column without a default is omitted, no NULL goes into a NOT NULL column, and no generated column (`text_fts`, `body_text_fts`) is written. Every `*_json` literal parses. Linear dates in 67–110 are `YYYY-MM-DDTHH:MM:SSZ`. There are no casts and no `now()`. Snapshot comparison against the local `01ef5792…` is a MISMATCH on the same columns as before (advisory A1). |
| C — Dates, relationships and consistency | PASS | All event timestamps fall at or before 2025-10-01T07:00Z; the latest is statement 4, 2025-09-30T22:10Z. Only gcal start/end (2025-10-08) are later, and they are plan fields. Thread counts, parents and chronology hold. Statements 76, 77 and 100 agree with the base tickets, their parent and children, the base Slack unfurls and the other injected records (below). No grader-facing text. |

### Check C detail for the changed and reopened statements

**Base records read** (`linear/data.json`, complete):

- **ZOM-521** "Master Ticket - VFX implementation" (`/issues/3596`):
  - In Progress; assignee Calvin Price; creator Brian Foster; no parent.
  - Base description ticks all six items.
  - updated_at 2025-09-17T15:50:49Z.
- **Children of ZOM-521** (complete `parent_id` scan):

  | Child | Pointer | Title | State |
  |---|---|---|---|
  | ZOM-523 | `/issues/3597` | End-game Level Animations | Done |
  | ZOM-524 | `/issues/3598` | End-game → Main Menu animations | Done |
  | ZOM-525 | `/issues/3599` | Live-ops icons appearing… | Done |
  | ZOM-526 | `/issues/3600` | Tokens traveling to live-ops | In Progress (since 2025-09-17, never completed, unassigned, creator Brian) |
  | ZOM-527 | `/issues/3601` | Rewards in the claim scene… | Done |
  | ZOM-528 | `/issues/3602` | Claimed Cards traveling to inventory section | In Progress (assignee Calvin) |

- **ZOM-526** has no children and no relations. Its description says: "Part of the queue manager. … We will implement this together with season passes and collect&win events".
- No Linear attachment, relation, GitHub, Gmail, Trello, Confluence or Docs record mentions ZOM-521, ZOM-526 or ZOM-528. All searches were complete with 0 matches. In Gmail, all 81,406 files were scanned.

**Base Slack messages that quote or unfurl the same ticket.** Complete scans of `messages/*/*.json` for "ZOM-521", "ZOM-526", "ZOM-528", "Master Ticket - VFX", "master ticket", "Claimed Cards traveling", "Tokens traveling", "tokens travel(l)ing" and "token travel":

- `D0770ET6WBW/2025-09.json /198`, Calvin Price, 2025-09-17T15:51:55Z: "I've updated the Master ticket VFX implementation and the remaining tickets", with the Linear unfurl of ZOM-521, State In Progress. The unfurl shows ✔︎ on End-game Level, End-game → Main Menu, Live-ops icons, **Tokens traveling to live-ops** and Rewards in the claim scene. **Claimed Cards traveling to inventory Section is unticked.**
- `D0770ET6WBW/2025-09.json /16` (2025-09-02) and `CC43664F351E/2025-09.json /11` (2025-09-03): earlier unfurls of the same Linear issue under its old key ENG-2368. All six items are unticked; State Todo. ENG-2368 does not exist as a separate base issue.
- Context in the same DM:
  - `/196`: Brian, Sep 17, "could you update the linear?"
  - `/197`: "Marcus completed the card animation that travels to the inventory section … assigned it to you".
  - `/219`: Brian, Sep 23, testing the queue-manager build #1949: "I didn't see any token animation or level-end animation".
  - `/262`: Calvin, Sep 29: "test … card animation VFX implementation".
- Elsewhere:
  - `D0770ET6WBW/2025-09.json /212` and `D0770ET1HV2/2025-09.json /2307`: Brian's queue order, with Season Pass token travel as item 3.
  - `D0770ET6WBW/2025-08.json /7`: "Tokens traveling to live-ops - … I think [PERSON_NAME_0022]'ll import it when he implement Season Pass".
  - `C09ATAJ220H/2025-08.json /7`: Brian lists these as "the polish VFX tasks".
  - `D07GCPNJPSA/2025-09.json /181`: Calvin, Sep 12, says the season pass token animation exists but does not trigger on the first token.

**Statement 100 (ZOM-521 description):**

- **Agrees with the child states.** The unticked items are exactly the two In Progress children (ZOM-526, ZOM-528). The ticked items are exactly the four Done children (ZOM-523, 524, 525, 527). This follows SC-15's "Safer: use the child ticket states".
- **Agrees with the Sep 17 base unfurl for Claimed Cards.** The unfurl shows it unticked, and Calvin's Sep 29 test request (`/262`) shows ZOM-528 still in progress.
- **The Tokens untick is the only change from the Sep 17 unfurl.** It is explained by statement 76 (Brian, Sep 26: "Unticked this one … marked done too early"). That reading fits:
  - the base: the ✔︎ was set by Calvin on Sep 17 while ZOM-526 was In Progress and never completed;
  - Brian's Sep 23 test of build #1949, where he saw no token animation.
- **updated_at is consistent.** It moves forward from the base, is at or after the 15:40Z untick, and equals the 17:25Z comment.
- **The disagreement in the base was already there.** The base description ticks all six items, while the base unfurl shows Claimed Cards unticked one minute after the base updated_at (SC-15). The injection removes that disagreement and does not introduce one (advisory A11).

**Statement 76 (`cmt_zom526_2`):**

- "Unticked this one on the master ticket, it was marked done too early." ZOM-526's parent is the master ticket ZOM-521, and "this one" is the ZOM-526 item, which statement 100 unticks. The early ✔︎ is visible in the base Sep 17 unfurl, and ZOM-526 was never completed.
- "The Season Pass part I mentioned above" refers back to `cmt_zom526_1` (sequence 1, Sep 24: "finishing it alongside Season Pass"). The internal reference resolves, and the time order is correct.
- "Polish on an effect that already ships":
  - Brian's own base word calls token travel a "polish VFX task" (C09ATAJ220H Aug 14).
  - The effect ships elsewhere per `cmt_zom526_1` (Quests, Endless, Daily Gift).
  - The base shows a working Season Pass token animation by Sep 12 (D07GCPNJPSA /181).
- "Season Pass runs without it" agrees with:
  - injected `#470#rc_10`: "Season Pass schedules are already running on prod";
  - the base #zombie-ops 2025-09 /21 prod premium-buy test (previous report row 40);
  - PR #438 "Feature/season pass" merged 2025-09-15.

  No base record makes Season Pass depend on token travel. The ZOM-526 line "implement this together with season passes" is an implementation plan, not a dependency.
- "Before the beta buy or the November season" uses dates set elsewhere:
  - the beta buy starts Mon Oct 6, per the Sep 23 UA deck (27–34) and statement 1;
  - the November season opens Sat Nov 1, per Brian's own Gmail (8–19).

  Both are future plan references, which the clock allows.
- **Author and date:** Brian Foster is the creator of ZOM-521 and ZOM-526, and the person who listed the polish tasks. The comment is dated 2025-09-26T15:40Z, before the clock.
- **Other injected records:** none says token travel is done or blocking. Statement 26 (brief) says "cosmetic, VFX … gaps do not hold a beat", which is consistent. Statement 73 (`cmt_zom543_1`, Queue Manager In Progress, flow including season_pass) is consistent.

**Statement 77:** chronology only. It moves forward and equals the latest comment.

**Reopened 75 (`cmt_zom526_1`):** "in progress" matches ZOM-526 In Progress, and "finishing it alongside Season Pass" matches the base Aug 20 and Aug 22 plan. It is consistent with 76.

**Reopened 99 (`cmt_zom521_1`):** "Master VFX checklist is down to the last two items, both polish on existing effects" now matches statement 100, which leaves exactly two items unticked, and Brian's "polish" wording. In SQL `3afbf7cb` it contradicted the all-ticked base checklist; that contradiction is now gone. "Everything the live-ops side asked for is in" next to an unticked "Tokens traveling to live-ops" item is reconciled by statement 76, which says that item is not required (advisory A12a).

**Unchanged Linear comments 67–110 (other than 75 and 99):** each was read against its base ticket, covering title, description, state, assignee, creator and parent. No incompatible fact was found.

- `cmt_zom429_1` (Sep 23, "force-closes and reopens, they land in the new week fine") is contradicted later by statement 5 (Vincent, Sep 30, prod, "killed the app and reopened it twice … still last week"). That is a later correction the records support, not an introduced contradiction.
- `cmt_zom565_1` ("can close" while Todo) touches SC-16 (A8).

## 7. Findings

**No demonstrated defects.**

### Advisories (do not affect the verdict)

- **A1 · schema snapshot (local `01ef5792…`):** these columns are not in the bundled snapshot:
  - `gcal_events.extras_json`;
  - `drive_files.drive_id`;
  - `slides_pages.notes`;
  - `slides_page_elements.table_json` and `ordinal`;
  - `github_review_comments.pull_request_review_id`, `side`, `start_line`, `start_side`, `subject_type` and `seq`;
  - `github_reviews.seq`;
  - `linear_comments.sequence`, used by all 23 comments including the new one.

  If the live database lacks any of these, the script will not load. The base has no Linear comments, so the semantics of `sequence` (per issue or global) cannot be checked. The SQL treats it as per issue: 22 issues at 1, and ZOM-526 at 1 and 2.
- **A2 · Gmail threading (14–19):** the correction has "Re:" and In-Reply-To/References but its own thread ID.
- **A3 · Gmail snippet (14–19):** the snippet ("Correction to my Sep 22 mail: the November…") differs from how the body starts ("…, Frederick in copy: …").
- **A4 · Slack mirrors (57–65):** subtype `bot_message` and a pretext author `EMPLOYEE_0025_GITHUB_USERNAME`, whereas base #zombie-prs mirrors use subtype null and real handles.
- **A5 · Halloween retraction placement (4):** threaded under an unrelated DM message. Findability is a `/prompt` question.
- **A6 · authority wording (26):** "Product latest dated approval … if he takes that back". The approver in the data is Robert (Co-Founder), not Julia (Product Manager). Hand off to `/prompt`.
- **A7 · minor shape:** gcal `transparency='transparent'` (base events are `opaque`). New reviews are logged as `commented` timeline events (the base uses `reviewed`).
- **A8 · known base-data areas:**
  - SC-15 (ZOM-521/526, now repaired; see A11);
  - SC-16 (`cmt_zom565_1` "can close" while Todo);
  - SC-38 (Season Pass ship date or analytics: `cmt_zom552_1`, and statement 76's "Season Pass runs without it", which is the same claim as `#470#rc_10`).

  No Snowflake or Confluence record is built on. `/prompt`, `/oe` and `/rubric` decide dependence.
- **A9 · build named loosely (5):** "the current prod build" names neither a version nor a platform.
- **A10 · rules in a DM (2):** scope rules sit in a DM reply rather than the brief (a `/prompt` question).
- **A11 · SC-15 repaired, not avoided (new, 76 and 100):** the injection replaces the base "all six ticked" checklist with one that matches the child states. Only the Tokens untick has an injected actor and reason (76). The Claimed Cards untick has no injected record, although the base Sep 17 unfurl already shows it unticked. The Portal card SC-15 still reads "Don't grade: what is left on ZOM-521" and describes the old state. The authoring README asks for such repairs to be recorded (`hazard_acknowledgements`, `resolution: repaired`). If anything graded depends on ZOM-521's checklist, record the repair there and expect `/prompt` or `/rubric` reviewers to check SC-15. Not a data-integrity defect.
- **A12a · wording beside the unticked item (99, unchanged):** Calvin's "Everything the live-ops side asked for is in" sits beside the unticked "Tokens traveling to live-ops". It is reconciled by Brian's statement 76, but a literal reader could take the item name as a live-ops ask. `/prompt` should confirm the intended reading.
- **A12 · later narrowing (86 vs 51, unchanged):** `cmt_zom465_1` (Sep 26, Marcus: "every event icon animates at idle now") is narrowed by `#454#c_4` (Sep 30, Marcus: "The Collect & Win event icon animation is still to do"). This is a supported later-word reading, because Collect & Win was only "almost ready to merge" on Sep 24 (D0770ET6WBW 2025-09 /252). Whether it works as a clean trap is a `/prompt` question.

## 8. Limits

- Outside the static scope: live execution, deploy-time schema compatibility (A1, including `linear_comments.sequence` semantics), search ranking, Agent visibility and task difficulty.
- Workspace adaptation: no input-store save, no `hg_write_output.py`, no `input_manifest.json` write. Section 9 gives the entry.
- No required static check is unresolved.

## 9. Stage dependencies (for reuse)

| Dependency | Value |
|---|---|
| SQL | SHA `837d4f5d…76b` |
| Universe manifest | `da2f4cf0…a1a` |
| Local schema snapshot | `01ef5792…6eb` (differs from the Portal's `31dcb2b4…`; A1 set identical) |
| id_contracts | `fc4711ef…82` |
| Clock | 2025-10-01T07:00Z |
| Lint | injection-lint-v1 |

New facts this run:

- **Linear:**
  - Base `/comments` is empty (0 records).
  - ZOM-521 `/issues/3596` base description is all six items `[X]`, updated_at 2025-09-17T15:50:49Z.
  - Children: ZOM-523, 524, 525 and 527 Done; ZOM-526 (`/issues/3600`, updated_at 2025-09-17T15:52:10Z) and ZOM-528 (`/issues/3602`) In Progress.
  - Base updated_at for the other 20 targeted issues is as printed in section 5.
- **Slack:**
  - D0770ET6WBW 2025-09 /198 is the Sep 17 ZOM-521 unfurl (Tokens ✔︎, Claimed Cards unticked).
  - /219: Brian on Sep 23 saw no token animation.
  - C09ATAJ220H 2025-08 /7: token travel listed as "polish VFX".
  - D07GCPNJPSA 2025-09 /181: Season Pass token animation exists on Sep 12.
  - All 10 injected Slack IDs are absent from 610,468 base messages.
- **Other services:**
  - All GitHub, Drive, Docs, Slides, Sheets, GCal and Trello new keys are absent in complete scans.
  - The Gmail IDs are absent from 81,404 thread files.

Manifest entry that would be written:

```json
{"review_version": "injection-static-v2", "evidence_contract": "stage-evidence-v1", "input_sha256": "837d4f5dedbdedb0febe279f64b5df61f0debdf29e93ef779a4ddd5ff754d76b", "reused_evidence": [{"source_report": "R/prev/0_injection.previous_report_on_3afbf7cb.md", "sha256": "51ac84336418da1b4a0e78d83bc93304bd2bfcb10e56dfc14bdd7e3c457757dd", "ledger_items": ["1-2 content", "5 content", "8-19 content", "20-23 content", "26 content and style runs", "40 content", "54 content"], "dependencies": {"universe_manifest": "da2f4cf0…a1a (unchanged)", "id_contracts": "fc4711ef…82 (unchanged)", "clock": "2025-10-01T07:00Z (unchanged)", "statements": "byte-identical (statement diff)"}, "not_reused": "all schema-dependent results (snapshot differs); all collision, reference and chronology checks (re-run NEW)"}]}
```

`/prompt` may rely on this stage for SQL `837d4f5d…76b`.

## 10. Next action

Proceed to `/prompt`. Because the SQL changed, any earlier `/prompt`, `/hardness`, `/oe` and `/rubric` result for `3afbf7cb` is outdated: run them again in that order. Check A11 (SC-15 repair) and A12a there.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt

Evidence limits: Static scope only. Live deploy compatibility is unverified: the bundled local schema snapshot (`01ef5792…`, not the Portal's `31dcb2b4…`) lacks several columns the SQL uses, including `linear_comments.sequence` (advisory A1).
