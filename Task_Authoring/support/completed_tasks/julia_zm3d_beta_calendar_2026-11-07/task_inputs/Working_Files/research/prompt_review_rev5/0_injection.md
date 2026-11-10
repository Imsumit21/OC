# Injection data-integrity review: Eval 0

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. The previous PASS / COMPLETE report (`R/prev/0_injection.previous_report_on_c955d6ca.md`, SHA-256 `02aeea5105a6…`) was read, and its reuse dependencies still match (hashes below). Even so, **nothing was reused**: every statement, including the 11 byte-identical ones, was re-checked NEW against the base. `reused_evidence: []`. |
| Mode | Independent chat review, audit only. Workspace adaptations: the report goes to `R/out/0_injection.md`. `hg_store_input.py`, `hg_write_output.py` and `input_manifest.json` were not used. Search and lint went through `Task_Authoring/tools/hg.py` (`--task-dir Task_Authoring/task_inputsS`). Base exports and git history were read directly with read-only commands. |
| Review time | 2026-11-06 |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`. `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` (re-hashed; same as the previous report). |
| Input under review | `R/inputs/01_Universe_Inject.sql`: 60,635 bytes, 243 lines, SHA-256 `3c035f2af02934538a1e07d04fe82a2ea2f0a7b8031cff8ca1bd53eb4217bc6f` (re-hashed; matches the brief). Not executed. |
| Previous version | `R/prev/01_Universe_Inject.previous_c955d6ca.sql`, SHA-256 `c955d6ca2bca5d1aa0c457e3107a28e8210903a833b3192a54d1e5337adc1cf2` (re-hashed). |
| Schema snapshot | `Evals/references/schema/injection.json` SHA-256 `01ef579236212034a43a53914754f86ed9248be48c961009cef5b4bd6106f6eb` (unverified, provisional; unchanged). |
| ID contracts | `Evals/references/schema/id_contracts.json` SHA-256 `fc4711ef07667333c1cf2a417279826f0432539195f7acdfacfa86e9d9ed4682` (unchanged). |
| Key source files | github `data.json` `ee578c912bba…`; linear `b49ec9e856cf…`; trello `6ba242f4dde4…`; gdrive `05147aa245b7…`; gcal `4f093d897c8b…`. Also the Slack `messages/*/*.json` (4,840 files, 610,468 records), the Gmail `threads/*.json` (81,404 files) and the git repos under `github/root/harmonygames-Games/` (match3d, match3d-backend, match3d-quests). |
| Known base issues | `Task_Authoring/references/known_data_issues/synthcut.md` SHA-256 `8895c4dc73da…`. Cards touched: SC-6, SC-13, SC-15, SC-16 pattern, SC-38, SC-48. |
| Context-only inputs | `00_Task_Assigned_Inputs.md` (`e8b8269803d5…`), `02_Universe_Date.txt` ("Oct 1, 2025 (synth-cut)", `2f0af1081ce8…`), `04_Prompt.txt` (`2a23afd87c4c…`). All three are unchanged from the previous review. |

## 2. Input / authority issues

- The SQL header points to `Working_Files/01_Grounding_Dossier.md` and `universe_schema_live.json`. Neither was supplied. They are treated as statements of intent, not evidence.
- No SQL comment is about tool calls, pass rates, gates or padding. The section header words "cohort" and "INT-01" are authoring labels, not grader-facing text.
- **Grader-facing text:** none. The lint found none, and every injected text field was also read by hand. "Two things the brief does not spell out" (stmt 2) is Frederick talking about his own brief to Julia; that is in-world, not addressed to a solver.
- **Advisories from the previous report now resolved:**
  - N1: the ZOM-387 statements were removed.
  - N3: mirror lag is now 2.7–2.9 s, and `&` is escaped as `&amp;`.
  - N4 (ZOM-565 pointer): the comment is now timed between the two DMs (see Check C).
  - A12a: the "Everything the live-ops side asked for is in" wording is gone.
- **Base shape now matched:** the `9025d428` parent now gets `thread_ts_legacy` = its own ts, which is the base convention (15,204 of 15,204 base parents with replies).

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, manifest, review version | Done. Hashes are recorded above; nothing was written to the store (workspace adaptation). |
| Diff against the previous SQL | Done statement by statement with a quote-aware, comment-stripped splitter and a per-column diff. <br>• prev 106 statements → current 96 <br>• 11 byte-identical <br>• 83 changed versions of a previous record (same key, or the same record under a new Slack/Gmail key) <br>• 2 new records (`cmt_zom432_2`; the Trello card `68c452a0…` UPDATE) <br>• 12 previous records dropped (§5) |
| Run lint; resolve every flag | Done: 0 flags (§4). |
| Inventory every statement | Done: 96 statements (70 INSERT, 26 UPDATE). No DELETE, upsert or conflict clause. |
| Check A | **PASS** (NEW, complete collection scans). |
| Check B | **PASS** (provisional snapshot comparison). |
| Check C | **PASS** (NEW for every statement and record group). |
| Report coverage, findings, limits, verdict | Done. |

## 4. Lint

`hg_injection_lint.py` (injection-lint-v1) was run through `hg.py lint` on SHA `3c035f2a…`, universe synthcut, clock `2025-10-01T07:00:00Z`.

- **Base loaded:** slack/users, gmail/users, github/data, linear/data, trello/data, contacts, confluence_working.
- **Checks run:** future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required.
- **Statements:** 96 (70 insert, 26 update). The per-table row counts match the ledger.
- **Flags:** FAIL 0, CHECK 0, INFO 0. Nothing to resolve.

The lint has no JSON-shape check, so all 118 `*_json` literals were parsed by hand: 0 errors. A clean lint is not a PASS, so checks A–C were run in full.

## 5. Operation ledger

"Prev" is the previous-version status: IDENT means byte-identical; chg means a changed statement, or the same record under a new key. **Every row's basis is NEW.**

### Complete collision and target scans

All of these ran over the full collections:

- **Slack** (610,468 records in 4,840 files, including 81,036 legacy records without an `id`):
  - all 8 injected IDs are absent, and no injected (channel, ts) pair exists;
  - all 8 IDs equal `sha256("<channel>|<ts>")[:32]`;
  - base ts precision is 6 decimals (529,432 of 529,432), and the injected ts match it.
- **Gmail:** a fixed-string grep of all 81,404 thread files plus users and labels finds 0 hits for the 6 thread numbers and 2 Message-ID tokens. The positive control (Brian's base `CAPT--p4fNJdXvZXqxW6yWBwp0p60u`) finds 3.
- **GitHub:** all new keys are absent:
  - `/reviews` (2,230): `#468#rev_3`;
  - `/review_comments` (1,387): `#470#rc_10`, `#468#rc_38`;
  - `/timeline_events` (11,406): `#468#ev_6`, `#473#ev_5`;
  - `/pull_request_comments` (687): `#473#c_2`.

  The base maxima are #468 rev_2/rc_37/ev_5/c_1, #470 rev_9/rc_9/ev_8 and #473 c_1/ev_4, so the new numbering follows on. The referenced `#470#rev_9` exists.
- **Linear:** the base has 0 comments, and all 24 injected comment IDs are unique. All 21 issue targets and all 10 authors exist. No issue gets more than one UPDATE.
- **Drive** (53,631 files): the 4 IDs and 4 names are absent. Docs (595), Slides (132) and Sheets (356) contain none of the new IDs. The parent folders `d_8140f09b…` (Julia's root) and `d_175c0d7b…` (Frederick's root) exist.
- **GCal** (10,395 events): the 4 `event_id`s and the `ical_uid` are absent. All 4 calendars exist.
- **Trello** (5,252 actions): the action ID is absent. The card `/cards/781`, the board, the list and the member (`PERSON_6094` = Leonard Hayes) all exist.

### Statement ledger

| # | Line | Table | Op | Record / target | Prev | Key after-values and check result |
|---|---|---|---|---|---|---|
| 1 | L11 | slack_messages | I | `bca78437…` DM D05SD5QLG94 | chg | Frederick (DM member), 2025-09-30T20:20:17.418209Z. Parent of stmt 2: thread_ts = own ts; rc 1 / ruc 1 / latest = stmt 2 ts. Text unchanged. Pointers resolve to stmts 23, 24–25, 34 and 68. |
| 2 | L13 | slack_messages | I | `890dc27f…` reply to 1 | chg | Frederick, 20:24:38Z, after its parent. PNs Beta rows confirmed (§6, Slack). |
| 3 | L15 | slack_messages | I | `933cee9f…` reply in C08R8CHB0QL | chg | Robert (member), 2025-09-18T16:40:23Z. Parent `9025d428` (`C08R8CHB0QL/2025-09.json /121`, Martin, Sep 17 15:10:09). |
| 4 | L17 | slack_messages | I | `669d15f6…` DM D05GU6L0XFH | chg | Robert (member), 2025-09-30T22:10:41Z, top-level. Sits between base 20:46:05Z and Oct 1 03:32:57Z. |
| 5 | L19 | slack_messages | I | `b5f2955c…` C0880U9751A | chg | Vincent (member), 2025-09-30T20:50:12Z. Last message in the channel's 2025-09 file. |
| 6 | L21 | slack_messages | U | `9025d428…` | chg | thread_ts NULL→own ts; rc 0→1, ruc 0→1, latest = stmt 3 ts. Base 0/0/NULL. |
| 7–18 | L23–80 | gmail_threads / messages ×6 users | I | Sep 22 handoff (7–12); Sep 26 correction (13–18) | chg | New thread IDs and Message-IDs. Bodies and subjects are byte-identical to the previous version. Checked in §6, Gmail. |
| 19–22 | L82–88 | gcal_events | I | `evt_9a4c…`, `evt_5c1e…`, `evt_a72f…`, `evt_1d6b…` | chg | Changes: summary dash, and created/updated now carry seconds. Start/end 2025-10-08 15:00–16:00Z are plan fields. Checked in §6, GCal. |
| 23 | L90 | drive_files | I | `d_5f2c8e1b…` folder "ZM Live Ops" | chg | Julia, parent = her root. Created 2025-08-11T07:20:38Z; modified 2025-09-30T06:35:14Z (= creation of the sheet inside it). |
| 24 | L92 | drive_files | I | `f_7c3e91a4…` brief (.docx, native Doc) | chg | Frederick, reader Julia. Size 13872; content_path `frederick.stone@…/ZM3D beta live-ops calendar - working rules.docx`. Contract shape OK; advisory D1. |
| 25 | L93 | docs_documents | I | `f_7c3e91a4…` | chg | Only the created/modified times changed. Body (2,704 chars) and style runs are byte-identical to the previous version and were re-derived NEW (§6, Docs). |
| 26–27 | L113–114 | drive_files + slides_presentations | I | `f_2b9d4e7a…` UA plan | chg | Frederick, reader Julia. No size and no content_path (base convention for Slides, 132 of 132). Times are equal across the two rows. |
| 28–32 | L115–126 | slides_pages / elements | I | `slide_6f2a…`, `el_9d1c…`, `slide_b83e…`, `el_5e83…`, `slide_0c47…` | IDENT | Each page is inserted before its element. All 8 week labels are correct weekdays (W1 Mon Oct 6 – W4 Sun Nov 2). Re-checked NEW. |
| 33 | L127 | slides_page_elements | I | `el_c07b2e9d3148` | chg | Text changed: "small retention campaigns already running" became "Unity retention campaigns". Grounded (§6, Drive). |
| 34–35 | L130–131 | drive_files + sheets_spreadsheets | I | `f_e4a17c90…` calendar sheet (.xlsx, native Sheet) | chg | Julia, reader Frederick, parent = stmt 23. Size 9216; content_path `julia.lawson@…/ZM Live Ops/ZM3D Beta Live-Ops Calendar.xlsx`. Advisory D1. |
| 36–37 | L132–133 | sheets_sheets | I | Calendar (0), Pushes (1) | IDENT | Header rows only. The header widths (9 and 7) equal `column_count`. |
| 38 | L138 | github_review_comments | I | `#470#rc_10` | chg | Arthur, 2025-09-30T15:51:06Z. Now attached to base `#470#rev_9` (Arthur, APPROVED, submitted 15:51:06Z), 9 s before the merge at 15:51:15Z. Path is in the #470 net diff. Seq 10. |
| 39 | L140 | github_reviews | I | `#468#rev_3` | IDENT | Arthur, COMMENTED, empty body, 2025-09-29T15:36:41Z. After rev_2 (09-26 21:54) and before the merge (16:13:50). |
| 40 | L141 | github_review_comments | I | `#468#rc_38` | chg | Body and path changed. Path `Assets/Match3D/Game/Levels/GameLoader.cs` is in the #468 squash diff (28 lines). Review link points to stmt 39, inserted earlier. |
| 41 | L142 | github_timeline_events | I | `#468#ev_6` | IDENT | `reviewed`, actor `''`, NULL, commit `648e2c7b…`, which is #468's head (authored 2025-09-26T22:03:06Z). Advisory N2. |
| 42 | L144 | github_pr_comments | I | `#473#c_2` | chg | Body reworded; updated_at now NULL (base convention). Arthur, 2025-09-30T16:16:33Z, 35 min after the merge (precedent in §6). |
| 43 | L146 | github_timeline_events | I | `#473#ev_5` | IDENT | `commented` / Arthur / 16:16:33Z / `{}`. Follows ev_4 `head_ref_deleted`. |
| 44 | L148 | github_pull_requests | U | #473 `/pull_requests/2378` | IDENT | updated_at 15:43:58Z → 16:16:33Z (forward). |
| 45 | L150 | slack_messages | I | `73bc730c…` #470 comment mirror | chg | ts 1759247468.897619, 2.9 s after rc_10. Parent `c2b9c903` (`/579`). |
| 46 | L152 | slack_messages | U | `c2b9c903…` | chg | rc 16→17. latest stays at the base merge broadcast `1759247478.371389` (15:51:18), which is later than the mirror. |
| 47 | L154 | slack_messages | I | `78aa8ed7…` #468 comment mirror | chg | ts 1759160203.696979, 2.7 s after rc_38. Parent `4b7c4127` (`/530`). |
| 48 | L156 | slack_messages | U | `4b7c4127…` "opened" card | chg | rc 41→42; latest unchanged (base merge broadcast 16:13:53). attachments: the only change is Reviewers, which gains `<@EMPLOYEE_0025_SLACK_ID>` (§6, mirrors). |
| 49 | L158 | slack_messages | I | `bd1a7d0a…` #473 comment mirror | chg | ts 1759248995.720659, 2.7 s after c_2. Parent `d05a2f8a` (`/605`). |
| 50 | L160 | slack_messages | U | `d05a2f8a…` "opened" card | chg | rc 2→3; latest = stmt 49 ts. attachments: the only change is Comments "1"→"2". |
| 51–94 | L165–235 | linear_comments (24) + linear_issues UPDATEs (20) | I / U | 21 issues | chg | Per-issue results are in the §6 Linear table. Every `*_at` value is `YYYY-MM-DDTHH:MM:SSZ`. |
| 95 | L237 | trello_actions | I | `68dac820…` commentCard | chg | Card changed to `68c452a0…` (#61 quests card) and creator to Leonard. Date 2025-09-29T17:55:44Z = the ID's timestamp prefix `0x68dac820`. |
| 96 | L239 | trello_cards | U | `68c452a0…` | chg (new target) | badges.comments 0→1 (the only badge change); dateLastActivity 2025-09-12T17:31:20Z → 2025-09-29T17:55:44Z. |

### Removed prev-only statements and their dependencies

The 12 dropped records are:

- `#470#rev_10`, `#470#ev_9`, and the PR #470 updated_at bump;
- `#471#c_18`, `#471#ev_8`, and the PR #471 bump;
- the #471 mirror and its `da3fe08c` parent bump;
- the ZOM-429 updated_at UPDATE;
- `cmt_zom387_1` and the ZOM-387 UPDATE;
- the Trello card `6851a724…` UPDATE.

The old-key Slack and Gmail rows are not dropped records: they are the same records re-keyed, and each is counted among the 83 changed versions.

A grep of the current SQL for `rev_10`, `#c_18`, `#471#ev`, `#470#ev_9`, `da3fe08c`, `a0c26779`, `c778c9b9`, `dacaa8f6`, `c85ccb18`, `ZOM-387`, `cmt_zom387`, `match3d#471`, `6851a724` and the old latest_reply values returns 0 hits.

- `rc_10` now points to the base `rev_9`.
- "PR #471" in `cmt_zom432_2` is plain text about the base PR, which exists (`/pull_requests/2376`).
- Dropping the ZOM-429 UPDATE is consistent: its comment moved to 09-16, before the base updated_at of 09-22T14:51:23Z.
- The base cards `6851a724…` and #471, and the `da3fe08c` thread, keep their base values.

## 6. Checks

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | Every new key is absent from its complete base collection and unique within the SQL (§5). Every target and actor resolves:<br>• 4 Slack thread parents, and a new DM parent that the SQL creates before its reply;<br>• Slack membership of all 4 authors in their channels;<br>• 3 GitHub PRs and the base review `rev_9`;<br>• 2 Drive root folders and the SQL-created folder;<br>• 4 calendars;<br>• the Trello card, board, list and member;<br>• 21 Linear issues and 10 users.<br>Identities: `EMPLOYEE_0025` = Arthur Blake (one login); `SLACK_BOT_0004` = the base GitHub app; `PERSON_6094` = Leonard Hayes (the only Leonard member). Lint identities: 0.<br>ID contracts hold: Gmail `history_id` is NULL; both Drive `content_path`s start with the owner's email and have no `root/` prefix.<br>Readability: the Doc has a docs row with non-empty body; the Slides have text elements; the Sheet has sheet rows. |
| B — SQL structure and supported schema rules | PASS (provisional) | The 96 statements parse with balanced quotes. On all 70 INSERTs the column and value counts match, with no duplicate columns. Every UPDATE is `WHERE id = '<literal>'` with no repeated assignment.<br>Against the snapshot:<br>• no NOT NULL column without a default is omitted, and no NULL goes into a NOT NULL column;<br>• no generated column (`text_fts`, `body_text_fts`) is written;<br>• no cast, `now()` or random function is used;<br>• the 118 JSON literals parse.<br>Reserved or mixed-case identifiers are quoted (`"references"`, `"index"`, `"idMemberCreator"`, `"dateLastActivity"`, …). `state_id` literals `Done` and `In Progress` match team_ZOM usage (427 and 15 issues).<br>The snapshot comparison is a MISMATCH on the same columns as before (A1). |
| C — Dates, relationships and consistency | PASS | **Clock:** 154 timestamp values were swept, including JSON-embedded ones. Only the GCal start/end (2025-10-08) are after the clock, and they are plan fields. The latest event time is stmt 4 at 2025-09-30T22:10:41Z.<br>**Threads and lifecycles:** all Slack thread counts and latest_reply values, the Linear chronology for 21 issues, Gmail threading, the GitHub review/merge order and the Trello badges are correct.<br>**Facts:** every factual claim was checked against code on main or branches, commits, PRs, Slack (including DMs), notification mails and the other injected records (detail below). No incompatible fact was introduced, and there is no grader-facing text. |

### Check C detail by record group

**Slack asks, approvals and re-test (1–6).**

- The DM pair 1→2 is chronological, from the same author. The parent fields equal its single reply, and `thread_ts` = own ts follows the base convention.
- Stmt 2's named rows exist on the PNs Beta tab (`gsheets/data.json /sheets_spreadsheets/220/sheets/1`): Hourly Coins, Nathan's Treasure Hunt, Streak Fever and Axe Arena. The tab also has a Plague Race row ("Ready") and a Login Calendar update row.
- "Zombie Lane" is the trophy path (`C090N54TG79/2025-09 /492`).
- The Halloween approval (3) replies to Martin's Sep 17 thread, which tags Robert, Leonard and Julia. The retraction (4) is a later, top-level DM from the same approver.
- Stmt 5 (Vincent, Sep 30: the restart does not help) supersedes `cmt_zom429_1` (Douglas, Sep 16: force-close works). The base supports leaderboard trouble on new builds: `C08R27X0EAH/2025-09 /902`, Sep 22, "Killing the app doesn't help". This is a supported later correction, not a contradiction.

**Gmail (7–18).**

- **Thread and message IDs:** each mailbox copy has its own thread ID, and `id >> 20` = internal_date ms. This matches the base cross-mailbox pattern (one message in Julia's and Frederick's mailboxes: `…1831593703253535697` / `…1831593703341644616`). `X-GM-THRID` equals the thread ID in every copy.
- **Message-IDs:** `<CAPT--p4…@mail.gmail.com>` matches Brian's own base sent mail (`<CAPT--p4fNJd…>`, `<CAPT--p4izyQ…>`).
- **Date header:** `+0300` matches Brian's base Date offsets, and the mails' "Istanbul time" fits it. The Date header, `date` and internal_date agree in all 6 rows.
- **Labels** (`Label_b19fb8d1b3` = the user label "Opened"):
  - Brian: SENT + Opened, X-Gmail-Labels "Sent,Opened". The same combination is common in Julia's and Frederick's base sent mail; Brian's two base sent mails add ARCHIVED.
  - Julia, Sep 22: INBOX + Opened + CATEGORY_PERSONAL (29 base cases).
  - Julia, Sep 26 and both Frederick copies: INBOX + CATEGORY_PERSONAL (41 and 387 base cases).
  - Each `X-Gmail-Labels` value matches its labels in base wording and order.
- **Delivered-To:** present only on received copies, as in the base (internal mail: received 96/96, 86/86 and 378/385 have it; sent 0).
- **Snippet:** 175 characters, an exact prefix of the whitespace-collapsed body. The thread snippet equals the message snippet.
- **Content:** bodies and subjects are unchanged from the previous version. The correction is a new subject without reply headers, so it starts its own thread. Weekdays are correct (Mon Sep 22, Fri Sep 26, Wed Oct 29, Fri Oct 31, Sat Nov 1).
- **Base support:** "Season opens on Sat Nov 1" matches backend `match3d-backend:lib/zombies_game/season_pass/monthly_server.ex` ("resets on the first day of each month at 00:00 UTC"). No base mail mentions "config handoff" or "November season" (complete grep: 0 files).
- Shape gaps are in advisory D2.

**GCal (19–22).**

- One row per calendar, each with a distinct `evt_` + 22-hex ID, all sharing one `…@hg4` ical_uid. This is the base pattern (802 multi-row ical_uids, never sharing an event_id).
- `self` is set on each calendar's own attendee; transparency is `opaque`, as in all 10,395 base events.
- Created 2025-09-24T16:05:37Z, updated 2025-09-26T17:20:09Z, sequence 1: valid.
- 15:00–16:00Z = 18:00–19:00 Istanbul (UTC+3), as the description says.
- No base event or message gives another backend-release date. The description ("server windows still on the DEV stack go live with this release") matches `rc_10`.

**Drive, Docs, Slides and Sheets (23–37).**

- **Docs style runs:** all 9 runs (TITLE 0–43 plus 8 HEADING_2 runs) start at a line start and end exactly before the `\n`. The body is 2,704 chars, BMP only, with 0 CR. The byline is unstyled.
- **Brief content (NEW):**
  - the Collect & Win windows (Mon–Tue, Wed–Thu, Fri–Sun from 00:00 UTC) match backend `win_and_collect/group_{1,2,3}_server.ex` and `config/runtime.exs`, which reset Wed, Fri and Mon at `0 0 *`;
  - Season Pass opens on the 1st at 00:00 UTC (backend monthly server);
  - the translated push tab is Domino-era: "PN BETA Translated" has 44 Domino and 0 Zombie hits.
- **Slide 3's "Unity retention campaigns":** grounded by "Unity iOS UK-Retention campaigns" (`C07C2866011/2025-08 /319`) and Leonard's 09-29 ask to turn on "iOS Unity retention campaigns" (`/1160`).
- **Drive shape:** now matches base conventions:
  - native Docs: `.docx`/`.html` name, size and content_path on 595 of 595;
  - native Sheets: `.xlsx`, size and content_path on 356 of 356;
  - Slides and folders: no size and no content_path;
  - root children use `owner/<name>`;
  - 'private' visibility with shares occurs in the base.
- **Timestamps:** each Drive row's times equal its content-table row's. The folder's modified time equals the sheet's creation.

**GitHub (38–44).**

- **rc_10 / #470:**
  - It now sits in the base APPROVED review `rev_9`, at its submission second. The base has 17 APPROVED reviews with same-instant inline comments, so this has precedent.
  - It is 9 s before the merge, so no updated_at bump is needed (base updated_at 15:51:15).
  - Content: the C&W server is still dev-only in the base (Douglas's 1-hour dev events and debug reset endpoint, `D05SG9H1CFM/2025-09 /78`; client/server bug-fixing through Sep 25–30). Plague Race, leagues and Endless run on prod (`D05QHF52KB3/2025-08 /5`, prod scheduler jobs; `C080X4GTZ0E/2025-08 /87`, "endless and plague race is working now").
- **rc_38 / #468:**
  - `GameLoader.cs` came in with "Updated GameLoader to show CollectAndWin objects", and the comment ("vials that spawn in the levels") fits it.
  - Claire is the Art Lead (roster). No base record shows final C&W bottle/vial models delivered; Martin was still proposing changes on 09-17 (`D076V3NEA7P /69`).
- **c_2 / #473:**
  - Oliver authored #473 (Season Pass addressables).
  - It is a human comment 35 min after the merge. The base has 2 human post-merge PR comments in 643 (9 and 41 min), so this has precedent.
  - No base record states the premium-strip date range either way.

**#zombie-prs mirrors and "opened" cards (45–50).**

- **Shape:** every mirror has the base comment-mirror shape: color `24292f`, fallback "Comment on #N", the commenter handle in the pretext, `#discussion_r…` for review comments and `#issuecomment-…` for PR comments, the title, footer and `mrkdwn_in`, and subtype NULL.
- **Text:** the attachment text equals the GitHub body with `&`→`&amp;`. The attachment `ts` equals the GitHub second.
- **Lag:** the base never mirrors at 0 s (1,876 comment mirrors; 2–3 s is the mode). The injected 2.7–2.9 s fits.
- **ID order:** monotonic among all base IDs from 09-26 on, at the base rate:
  - discussion: base 2389766458 (09-30 03:44) < injected 2391980467 (15:51) < base 2392548744 (18:57), about 183k/h on both sides;
  - issuecomment: base 3352864685 (15:59) < injected 3352918642 (16:16) < base 3353411814 (18:54), about 187k/h;
  - #468: 2388843617 sits between base 2383566804 (09-26 21:54) and 2389315092 (09-29 21:28).
- **Threads:** base reply counts were recounted from the message files (16, 41 and 2). The new counts and latest_reply values are correct, and reply_users_count stays 1 (same bot).
- **Card fields after the SQL:**
  - Base "Comments" = the PR's comment count on 561 of 561 cards. After the SQL, #473 has 2 PR comments (card "2") and #468 still has 1 (card "1").
  - Base "Reviewers" lists actual reviewers in review order, with Arthur shown as `<@EMPLOYEE_0025_SLACK_ID>` (#470 and #471 cards). After the SQL, #468 has reviews by coderabbit and then Arthur, so the new value is correct.
  - All other card bytes are unchanged after JSON parse, including the `&amp;amp;quot;` escaping.
- #470 now shows both an approval mirror and a comment mirror for one review (advisory D3).

**Linear (51–94).**

Team_ZOM conventions in the base:

- Done: completed_at set on 427 of 427; started_at null on 120 of 427; updated_at = completed_at on 401 of 427.
- In Progress: started_at set on 15 of 15.

Per-issue chronology passes for all 21 issues:

- comments come after creation, with created = updated and is_edited false;
- sequences run 1..n in time order;
- updated_at moves forward from base and is ≥ the latest comment, or the base value is already later (ZOM-429);
- started ≥ created and completed ≥ started/created.

| Issue | Post-SQL lifecycle | Comment author and claim | Base evidence (result) |
|---|---|---|---|
| ZOM-429 | Backlog (unchanged) | Douglas (assignee), 09-16: force-close lands in the new week | Description: "only proceeds… if the app is killed". Superseded later by stmt 5 (consistent). |
| ZOM-556 | Todo; updated 09-24 | Vincent (creator): claim works, row doesn't reset | Matches the description; submission builds existed (Android #127 09-22, iOS #43 09-23) (consistent). |
| ZOM-565 | Todo (Done removed); updated 09-29T14:34:12Z | Marcus (creator): pushed a prefab change on `Marcus/EndlessMode_Vfx`; bar hidden; glow on every box; P1/P2 polish | Commit `44988da015` on that branch at 14:33:08Z ("a little change to the prefab… still hidden in there for you to use"). DM `D05U73FNDDL /130` 14:34:06 ("pushed…"), then the comment at 14:34:12, then DM `/131` 14:34:25 ("i wrote a comment on the linear task"). Linear reminder mail to Calvin at 14:49:44, "Marcus Bennett mentioned you in a comment on [ZOM-565]". The description mentions the hidden bar and glow; Brian's list has "P1/P2 - Endless mode Remaining VFX" (`C09ATAJ220H /96`) (consistent). |
| ZOM-543 | In Progress; updated 09-30 16:20 | Calvin (assignee): level_end, daily_gift, season_pass, tutorial plus C&W | `main:Assets/Scripts/UI/MainMenu/QueueManager.cs` enqueues Level_end_animations, daily_gift, season_pass_event and unblock_tutorials. "Implement Win&Collect into Queue Manager" (#472) merged 15:53, before the comment (consistent). |
| ZOM-526 | In Progress; updated 09-26 | Brian (creator), 09-24 and 09-26: SP tokens fly; C&W trigger on its branch; unticked on master | "Adding season Pass token animation" landed 09-11; the C&W token commits were on the `winAndCollect` branch until #468 merged 09-29 (consistent; stale after 09-29, D6). |
| ZOM-552 | In Progress | Oliver (assignee): redeem sent; left and premium in | `SeasonPass_redeem`, `SeasonPass_left` and `SeasonPass_premium` were added 09-18/19 by Oliver (consistent; SC-38 area). |
| ZOM-534 | In Progress | Douglas (assignee): rollover syncs quests-end | Oliver "pushed a fix for the quests reset bug" 09-10; the ticket has been In Progress since 09-15 (consistent). |
| ZOM-432 | Todo→Done; completed = updated 09-30T21:07:26Z; started NULL | Calvin 09-24: the frame is the last piece. Samuel 21:07: the frame went out with #471; in iOS 50 and Android 135 | #471 commit `f0bb8b4822` "Fixing UI Elements on Daily Gift … update header image" (Samuel). #471 merged 15:52:24. iOS Submission #50 (`C05433XK267 /1123`, 19:15:49) and Android #135 (`/1124`, 20:13:09) both built from main afterwards; #135 lists the Daily Gift change. The Done shape matches the base (consistent; D7). |
| ZOM-78 | Backlog; updated 09-30 | Frederick: use this ticket for the calendar | The title fits ("Event Calendar For Zombie Match 3D"). Frederick is an active Linear user (team_ART and team_ENG) but not a team_ZOM member (D4). |
| ZOM-465 | In Progress | Marcus (assignee), 09-26: icons done; 09-30: C&W icon not yet | Animated-icons PRs #454, #456 and #458 merged 09-19 to 09-24. At the clock, main has animated icons for Endless, InfiniteBoss, PlagueRace, Quests, SeasonPass and ZombieLane, and none for C&W. #468 opened after the 09-26 note. #475 (09-30) is the card-pack animation, not the C&W icon (consistent; N6). |
| ZOM-344 | Todo→Done; completed = updated 09-16 | Marcus (creator and assignee): art signed off | Not contradicted, but no commit or message corroborates it (D5). |
| ZOM-442 | In Validation | Oliver (assignee): `trophy_level` and `chest_content` | `ZombieLaneCellBase.cs` sends `trophy_reward_redeem` with exactly these parameters (added 07-30) (consistent). |
| ZOM-471 | Todo (Done removed) | Samuel (assignee): not started; Leonard said not needed; start button | Thread `C0880U9751A/2025-08 /287` (Vincent: "it already has start button") and `/288` (Leonard: "yeah, we don't need it! cancel the ticket") (consistent; SC-71 untouched). |
| ZOM-504 | Backlog | Vincent (creator): still only with the bot | DM `D07GJJBFHA5/2025-09 /14–16`, 09-03: "did u run a level w bot?" / "I couldn't repro without bots" (consistent). |
| ZOM-517 | Backlog | Robert (creator): enrage holds through refills | No later base report of the bug (consistent). |
| ZOM-521 | In Progress; description: two items unticked | Calvin (assignee): the last two items are tokens and cards | Byte diff against the base: exactly 2 characters (`X`→space at 190 and 290). This matches the In Progress children ZOM-526 and ZOM-528, and repairs SC-15 (A11). |
| ZOM-542 | Regression (Done removed) | Samuel (assignee): mockup stage | Robert's 09-14 ask with a sketch (`C08R8CHB0QL /87–90`); no implementation before 09-22 (consistent). |
| ZOM-544 | In Progress | Vincent (creator): Apple works, no restore; Google waits on backend | Douglas 09-24: Apple infra on dev, "still waiting for the `googlePlayClientId`" (`CD843DBC4C3E /12`). Vincent 09-25: levels and currencies not stored (`/36`). The `…/auth` branch has submission builds (consistent). |
| ZOM-546 | Todo | Owen (assignee): refills hold | "Manual refill logic (#453)" merged 09-22, before the 09-24 note (consistent). |
| ZOM-549 | In Validation | Vincent (creator): endless_left has 3 fields; left_level lacks total_equipped_power | `AnalyticsManager.cs` on main: endless_left sends exactly `endless_level`, `nuke_damage_total` and `total_equipped_power` (no `player_cpm`), added 09-17 in #451; left_level has no `total_equipped_power` (consistent). |
| ZOM-566 | Todo→In Progress; started 17:20:13; updated 19:40:47 | Owen (assignee): start and redeem mapped | Base unfurl at 16:26:31 (`D07E9PSQB6W /3`, Brian to Owen), before started_at. The In Progress shape matches the base (consistent). |

No base Linear notification mail or Slack unfurl contradicts any post-SQL state. The mails found for these issues are assignment notices (ZOM-543, 78, 465, 565, 429, 432), mention notices (ZOM-534 and ZOM-565) and the ZOM-566 unfurl.

**Trello (95–96).**

- The card's base history is create, then two renames by Leonard on 09-12, with 0 comments.
- The action payload matches the base `commentCard` shape on this board: keys board, card (id, idShort, name, shortLink), idCard, list, text and textData. The list name "BETA: Sep 30" follows the convention of every action since the Sep 12 rename (SC-13). The board shortLink `HSqnngwQ` and card shortLink `viBYIjSG` equal the base action values.
- Badges: base `comments` equals the commentCard count on 79 of 79 board cards, so 0→1 is correct. No other badge changed.
- The board's dateLastActivity (09-30T17:09:07Z) is already later, so it needs no change.
- "Mon Oct 13 rollover" is a Monday and fits the quests service's Monday weekly timer (`match3d-quests:lambda/getQuestRemainingTime.ts`).

## 7. Findings and advisories

**No demonstrated defects.**

Advisories do not affect the verdict. Each is tagged **[CSC]** (a /prompt reviewer could score it under Cross-Service Coherence) or **[cosmetic]**.

**Carried forward and still applicable:**

- **A1 [cosmetic: deploy-compatibility limit].** The SQL writes columns that the local snapshot lacks, the same set as before:
  - `gcal_events.extras_json`;
  - `drive_files.drive_id`;
  - `slides_pages.notes`;
  - `slides_page_elements.ordinal` and `table_json`;
  - `github_review_comments.pull_request_review_id`, `seq`, `side`, `start_line`, `start_side` and `subject_type`;
  - `github_reviews.seq`;
  - `linear_comments.sequence`.

  If the live database lacks any of them, the script will not load.
- **A6 [CSC].** The brief says "latest dated approval from Product, and if he takes that back". The only approver in the data is Robert (Co-Founder & Creative Director, Executive), while Julia is the Product Manager. Either reading takes Halloween off the calendar.
- **A9 [cosmetic].** Stmt 5 says "the current prod build" without naming it. The base context is iOS 0.3.49 (`C0880U9751A/2025-09 /463`).
- **A10 [cosmetic].** Some scope rules are in Frederick's DM reply rather than in the brief.
- **A11 [CSC].** The ZOM-521 untick repairs SC-15. Record it in the dossier's `hazard_acknowledgements` (`resolution: repaired`).
- **N2 [cosmetic].** `#468#ev_6` (`reviewed`) is numbered after ev_4 `merged` and ev_5 `closed`, although the review is pre-merge. This follows from appending; the review row has the right time.
- **N4 residual [cosmetic].** The base export has 0 Linear comments, although comment-surface attachments exist (ZOM-471 `/attachments/868`; ZOM-542). The injected comments therefore take `sequence` 1. ZOM-565 is now fully aligned.
- **N5 [cosmetic].** The 3 state-changing UPDATEs (ZOM-432, ZOM-344, ZOM-566) do not touch `state_history_json`. The export has no history field, so whether a history view shows these transitions is outside static scope.
- **N6 [CSC].** ZOM-521 keeps "Live-ops icons … animations" ticked, while `cmt_zom465_2` says the C&W icon animation is still to do. "Came in after my note above" and the #468 timing reconcile the two.

**New in this revision:**

- **D1 [cosmetic: runtime-readability limit].** The native Doc (24) and Sheet (34) now follow the base convention (`.docx`/`.xlsx` name, size and content_path). Their `content_path` values cannot resolve to bytes, because injection cannot add files. Eval 0 and the lint serve native Docs and Sheets from their gdocs/gsheets rows, so this is not a listed failure. If a Drive download path reads `content_path` for native files, it would 404; that is not determinable statically. NULL `content_path`, as in the previous version, avoids asserting bytes.
- **D2 [cosmetic].** Gmail shape details:
  - `mbox_from` lacks the trailing `\r` that all 6,085 base messages in these mailboxes carry, and its time equals the Date header (base delivery is usually a few seconds later);
  - the header order differs from the base, with no Received or Content-Type headers;
  - `in_reply_to` is NULL where the base uses `''`;
  - Brian's SENT copies omit the ARCHIVED label that his 2 base sent mails carry.
- **D3 [cosmetic].** After the SQL, #470's APPROVED `rev_9` has an inline comment and both a "Review approved" mirror (base) and a "Comment" mirror (injected). The base pairs inline-comment approvals with a comment mirror only in 14 of 17, and with both in 1 of 17.
- **D4 [cosmetic].** Frederick comments on ZOM-78 but is not a team_ZOM member. No team_ZOM issue in the base has a non-member creator. Linear allows comments on public teams, and team privacy is not exported.
- **D5 [CSC].** ZOM-344 is closed Done on 09-16 on Marcus's word alone. No commit, PR or message corroborates the quest-box animation, though none contradicts it.
- **D6 [CSC].** Items described as open on 09-26 had landed before the clock:
  - the C&W token trigger, in #468 (09-29);
  - the card-pack animation, in #475 (09-30).

  Yet ZOM-526 and ZOM-528 stay In Progress and ZOM-521 stays unticked. The chronology is coherent; this is the SC-16 pattern. `/prompt` should decide whether the "still to do" reading depends on it.
- **D7 [CSC].** ZOM-432's closing evidence is indirect:
  - Samuel's #471 commit says "update header image", not "frame";
  - the iOS Submission #50 change list shows only "Bump max level for debug menu" (a base Jenkins quirk), so "in both submission builds" rests on both builds coming from main after #471, which is true.
- **D8 [cosmetic].** `#473#c_2` is a human comment 35 minutes after the merge. It has precedent (2 of 643 base PR comments).

**Known base issues touched** (/prompt, /oe and /rubric decide dependence):

- **SC-6 [CSC]:** the brian.foster@ address is also used by the Node CEO "Brian Cooper" in Frederick's base mail. The injected mails are clearly HG Brian Foster's (his mailbox, `+0300`, the CAPT Message-ID pattern).
- **SC-13 [CSC]:** the list is named "BETA: Oct 10", but the action payload says "BETA: Sep 30", following the actions convention.
- **SC-15 [CSC]:** repaired (A11).
- **SC-16 pattern [CSC]:** D6.
- **SC-38 [CSC]:** `#473#c_2` and `cmt_zom552_1` touch Season Pass.
- **SC-48 [cosmetic]:** Istanbul times.

## 8. Limits

- **Outside the static scope:**
  - live execution and deploy-time schema compatibility (A1);
  - runtime handling of `content_path` for native Drive files (D1);
  - the `linear_comments.sequence` semantics and any state-history view (N5);
  - search ranking, Agent visibility and task difficulty.
- **Not comparable with the base export:** Gmail `snippet` and `size_estimate`; Linear comments and state history; Linear team privacy.
- **Bounded content searches:** Slack text searches covered every channel for the months named, mostly 2025-08 to 2025-10, with complete file coverage for those months. They support "no contradicting record" findings only within those months. All collision checks were complete collection scans.
- **Workspace adaptation:** no input-store save, no `hg_write_output.py` and no `input_manifest.json` write. §9 gives the manifest entry.
- No required static check is unresolved.

## 9. Stage dependencies (for reuse)

| Dependency | Value |
|---|---|
| SQL | `3c035f2af02934538a1e07d04fe82a2ea2f0a7b8031cff8ca1bd53eb4217bc6f` |
| Universe manifest | `da2f4cf0dcf7…4aac1a` |
| Schema snapshot | `01ef57923621…06f6eb` (A1 set unchanged) |
| id_contracts | `fc4711ef0766…ed4682` |
| Known issues | `8895c4dc73da…961a52` |
| Clock | 2025-10-01T07:00:00Z |
| Lint | injection-lint-v1, 0 flags |

**New base facts recorded in this run (NEW):**

- **Slack IDs and threads:**
  - IDs = `sha256(channel|ts)[:32]` (529,418 of 529,432 id-bearing records);
  - parents with replies carry `thread_ts` = own ts (15,204 of 15,204);
  - comment-mirror lag ≥ 1 s (1,876 of 1,876; mode 2–3 s).
- **Slack PR cards:** "Comments" = PR comment count (561 of 561 cards); "Reviewers" lists actual reviewers.
- **GitHub:** `#470#rev_9` is APPROVED at 15:51:06Z. APPROVED reviews with inline comments: 17.
- **Gmail:** thread ID `>> 20` = delivery ms; Brian's sent mail uses CAPT Message-IDs and `+0300`.
- **Drive:** native Doc and Sheet conventions (§6).
- **GCal:** the multi-row ical_uid pattern.
- **Trello:** `badges.comments` = commentCard count (79 of 79).
- **Backend:** W&C groups Mon–Tue, Wed–Thu, Fri–Sun with resets at Wed/Fri/Mon 00:00 UTC; Season Pass resets monthly on the 1st at 00:00 UTC.
- **Linear:** ZOM-565 timing chain; ZOM-471 source thread; ZOM-504 bot-only DM.

Manifest entry that would be written:

```json
{"review_version": "injection-static-v2", "evidence_contract": "stage-evidence-v1", "input_sha256": "3c035f2af02934538a1e07d04fe82a2ea2f0a7b8031cff8ca1bd53eb4217bc6f", "reused_evidence": [], "dependencies": {"universe_manifest": "da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a", "schema_snapshot": "01ef579236212034a43a53914754f86ed9248be48c961009cef5b4bd6106f6eb", "id_contracts": "fc4711ef07667333c1cf2a417279826f0432539195f7acdfacfa86e9d9ed4682", "clock": "2025-10-01T07:00:00Z"}, "result": "PASS", "execution_status": "COMPLETE"}
```

`/prompt` may rely on this stage for SQL `3c035f2a…bc6f`.

## 10. Next action

Proceed to `/prompt`. The SQL changed, so any earlier `/prompt`, `/hardness`, `/oe` or `/rubric` result for `c955d6ca…` is out of date; rerun them in that order. Carry A6, A11, N6, D5, D6, D7 and the SC-6, SC-13, SC-38 touches into `/prompt`. Optional cleanups before then:

- D1: return `content_path` and `size` to NULL on the native Doc and Sheet, or confirm the runtime ignores them;
- D2: add the trailing `\r` to `mbox_from`.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt

Evidence limits: Static scope only. Live deploy compatibility is unverified, because the bundled snapshot (`01ef5792…`) lacks several columns the SQL writes (A1). Runtime handling of `content_path` on native Drive files is not determinable statically (D1). The base export has no Gmail snippet or size fields, no Linear comments or state history, and no team privacy, so those parts were checked only for internal consistency. Content searches for contradictions covered the 2025-08 to 2025-10 months.
