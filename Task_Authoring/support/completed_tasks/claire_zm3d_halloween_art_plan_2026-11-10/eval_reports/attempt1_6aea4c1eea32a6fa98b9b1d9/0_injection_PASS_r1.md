# /injection — Injection data-integrity review

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1` (no reused evidence; all checks NEW) |
| Mode | Chat review, attempt 6aea4c1eea32a6fa98b9b1d9 |
| Actual review time | 2026-11-05T11:15Z |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, 152,979 bytes, sha256 `df47d9068f630e82a164742576e71c0b652390231db193816e8783897239bd24` (input revision 3; from upload `_uploads/01_Universe_Inject.sql`) |
| References | Eval 0 sha256 `e034019b…3eff`; WORKFLOW sha256 `ee4cd8e1…fcd5d`; schema snapshot `injection.json` sha256 `31dcb2b4…5c7cb` (unverified); `id_contracts.json` sha256 `fc4711ef…d4682`; scoring.json sha256 `c14873e6…e5bc` |
| Lint | `hg_injection_lint.py` injection-lint-v1: 220 statements (217 INSERT, 3 UPDATE); FAIL 0, CHECK 0, INFO 1 |

## 2. Input / authority issues

None. SQL saved and read in full before base searches. Assignment (Claire Morgan, Art Lead) is context only; no prompt, persona or run is needed for this stage. Source text and SQL comments were treated as evidence only.

## 3. Lint flags and resolutions

| Flag | Severity | Resolution |
|---|---|---|
| `unparsed` line 163: 13 injected media/binary Drive files (11 PNG store screens, 2 MP4 cuts) have no bytes | INFO | Accepted. Media carries metadata only, as in the base. Names, folders, owners and timestamps are the task-usable facts. Becomes a FAIL only if a rubric row or OE depends on image/video *content*. |

No FAIL or CHECK flags (future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape all clean). A clean lint was not treated as a pass; checks A–C below were run by hand.

## 4. Operation ledger (execution order)

| SQL lines | Service.table | Op | Records / target | Result |
|---|---|---|---|---|
| 1–5 | slack.slack_messages | INSERT ×5 | `7bc65781…` (Robert, C08R8CHB0QL #zombie-art, 2025-09-25T16:30:22Z); `c737e6b9…` (Claire, DM D05V2N6PZNU, 09-26T07:40:09Z, thread parent, reply_count 1); `ca1f5be7…` (Marcus reply, 09-29T17:20:37Z); `55737ddb…` (Martin, #zombie-art, 09-30T15:20:41Z); `df862615…` (Leonard, C06DJBJL798 #zombie_marketing, 09-30T22:05:13Z) | PASS |
| 14 | slack.slack_messages | INSERT | `8ce7e9ee…` Robert reply under base `9025d428…` (Martin's "Halloween theme" icon post, ts 1758121809.236839), 09-17T16:52:31Z | PASS |
| 15 | slack.slack_messages | UPDATE | `id = 9025d428af1f551a20e303c3acbc545b`: thread_ts_legacy → own ts, reply_count 0→1, reply_users_count 0→1, latest_reply → 1758127951.679146 | PASS (target exists; matches base parent convention, e.g. thread 1755114007.441789) |
| 17–156 | linear.linear_issues | INSERT ×62 | ART-793 … ART-854 (team_ART, creator usr_175c0d7bc72ed244 Frederick Stone; 58 Todo, ART-836/837/838/839 Canceled) | PASS (advisory 6.2) |
| 18–156 | linear.linear_comments | INSERT ×78 | `cmt_art793_1` … `cmt_art854_2`; authors Frederick (69) and usr_c77c50cc15c5342d Marcus Bennett (9) | PASS |
| 158 | linear.linear_issues | UPDATE | `id = ART-792`: time_in_status_minutes 246277 → NULL | PASS (base value runs to ~2026-02-13, past the clock, known issue SC-22; NULL matches base ART-774/ART-790) |
| 160–175 | gdrive.drive_files | INSERT ×16 | Folders `d_272d849c…` "ZM3D Halloween 2025" (parent Leonard root `d_63fffeb4…`), `d_74a7c95c…` "Store", `d_6c2e4339…` "UA masters"; 11 PNGs (Martin) in Store; 2 MP4s (Marcus) in UA masters | PASS (media INFO) |
| 177–182 | gdrive.drive_files + gsheets ×5 | INSERT | `f_02b1968f5e882366fbb883` "ZM3D live creatives" (Frederick, parent `d_175c0d7b…`), sheets Read me / Store / Unity (56 rows) / Archive | PASS (advisory 6.4) |
| 184–185 | gdrive.drive_files + gdocs | INSERT | `f_fdd6d2d2f4a4d2f5b908fb` "ZM3D release calendar — Q4" (Arthur, parent `d_cc3e9016…`), non-empty body_text | PASS |
| 192–206 | gdrive.drive_files + gslides (1 presentation, 4 pages, 8 elements) | INSERT | `f_5ebf55ad29e815d46243c8` "Seasonal art direction — Q4 2025" (Robert, parent `d_9f7ba94f…`) | PASS |
| 211–265 | gmail.gmail_threads ×10 + gmail_messages ×10 | INSERT | Frederick's "October UA plan (draft)" (2025-09-12T17:40Z) and "October UA plan - changes" (2025-09-30T23:10Z), one copy each in Claire, Frederick (SENT), Leonard, Marcus, Martin mailboxes | PASS |
| 271–272 | gmail.gmail_threads + gmail_messages | INSERT | Vendor PERSON_6311 "Halloween props for Zombie Match 3D" to Claire, 2025-09-24T14:00Z | PASS (context 6.5) |
| 276–282 | gcal.gcal_events ×7 | INSERT | "ZM3D Halloween review", Thu 2025-10-02 16:00–16:30Z, one copy per attendee calendar, shared ical_uid `83766dff…@hg4` | PASS |
| 284 | trello.trello_cards | INSERT | `68dc52e015f87c50c441d1a9` "Halloween push - store + ads", board ZM ROADMAP, list "Oct 21", idShort 80 | PASS |
| 285–286 | trello.trello_actions ×2 | INSERT | createCard `68dc52e0…` (Leonard, 09-30T22:00Z); commentCard `68dc65a0…` (Frederick, 09-30T23:20Z) | PASS (advisory 6.3) |
| 287 | trello.trello_boards | UPDATE | `id = 6851a6569f3bf818760632ab` dateLastActivity 2025-09-30T17:09:07Z → 23:20:00Z | PASS |
| 289 | contacts.contacts | INSERT | `6b350edd259a8b4499a9e625` PERSON_6311, "Founder, KayKit" | PASS |

## 5. Checks A–C

| Check | Result | Evidence |
|---|---|---|
| A — Records, references and IDs | PASS | See A below. |
| B — SQL structure and supported schema rules | PASS | Structure clean; provisional snapshot MISMATCH advisories only (6.1). |
| C — Dates, relationships and consistency | PASS | All event timestamps ≤ clock; cross-record facts reconcile with base and each other; advisories 6.2–6.5. |

### A — Records, references and IDs (NEW)

- **Actors resolve to the named people.** Slack `EMPLOYEE_0016/0009/0002/0033/0038_SLACK_ID` = Robert, Claire Morgan, Marcus Bennett, Martin Walsh, Leonard Hayes (slack/users.json); every author is a member of the channel used (C08R8CHB0QL 23 members, C06DJBJL798 17, DM D05V2N6PZNU incl. Claire + Marcus). Linear `usr_175c0d7bc72ed244` = frederick.stone, `usr_c77c50cc15c5342d` = marcus.bennett, both team_ART members. Trello `PERSON_6094_TRELLO_USER_ID` = Leonard Hayes, `4b4a68fc0fec0b254e4f9d8e` = Frederick Stone (matching the SQL comment). Drive owners/sharees all in drive_users; Gmail mailboxes all in gmail/users.json; gcal calendars all exist. No second accounts.
- **Parents/targets exist.** Drive parents are the owners' root folders; Trello board `6851a6569f3bf818760632ab` (ZM ROADMAP) and list `6851a677e090018224fb8c7f` ("Oct 21") exist; Slack thread parent `9025d428…` exists in C08R8CHB0QL/2025-09.json; UPDATE targets ART-792 and the Trello board exist.
- **No collisions (complete scans).** Slack: 6 ids vs 4,840 message files / 610,468 records, 0 matches; ts values unique within each channel. Linear: base ART max ART-792, 0 of ART-793…854 used as id or identifier, no base references to those identifiers in Slack/Linear/Trello/Docs/Confluence/gcal/GitHub; base has 0 comments; 78 comment ids unique. Drive: 19 ids vs 53,631 files, 0. Sheets: `f_02b1968f…` vs 356 spreadsheets, 0. Docs vs 595, 0. Slides presentation/page/element ids vs 132 presentations, 0. Gmail: 11 thread numbers and 3 Message-IDs grep'd across all 81,404 thread files, 0. gcal: 7 event ids and ical_uid vs 10,395 events, 0. Trello card/actions ids, 0; idShort 80 is next after board max 79. Contacts id vs 170, 0; PERSON_6311 appears nowhere in base (new person, not a second account).
- **ID contracts.** Gmail history_id NULL (allowed). No content_path values to check. Gmail ids follow base `<mailbox>/<Message-ID>` and `<mailbox>/<thread>` format; X-GM-THRID headers equal the thread ids; Trello ids' embedded timestamps (0x68dc52e0 = 22:00Z, 0x68dc65a0 = 23:20Z) match their dates.
- **Readable Drive files.** Doc has docs_documents with non-empty body_text; Sheet has a sheets_spreadsheets row + 4 grids; Slides has presentation/pages/elements. Media are metadata-only (INFO above).

### B — SQL structure and supported schema rules (NEW)

- 220 statements parsed; column/value counts match; quoting/escaping valid; all `*_json` literals parse and have the snapshot's shape (objects for metadata_json/start_json/end_json/data_json/badges_json, arrays elsewhere; slack metadata_json `'{}'`).
- Generated columns (`text_fts`, `body_text_fts`) not set. Linear dates all `YYYY-MM-DDTHH:MM:SSZ`; `state_history_json = '[]'` and every NOT NULL column supplied. Trello camelCase columns are double-quoted.
- Provisional snapshot comparison: MATCH for all covered columns; MISMATCH (NOT COVERED) for 10 columns, see 6.1. Advisory only under the README; no verified definitions were supplied.

### C — Dates, relationships and consistency (NEW)

- **Clock.** Latest event timestamp is 2025-09-30T23:20Z (Trello comment); all created/sent/modified/action dates ≤ 2025-10-01T07:00Z. The only later dates are the Oct 2 calendar event (scheduled) and plan dates in text (Oct 12–Nov 6). Slack created_at equals ts for all 6 messages; Gmail internal_date equals date and the `Date:` header (-0700 PDT) for all 11 messages.
- **Weekdays.** Thu Oct 16, Fri Oct 17, Wed Oct 22, Thu Nov 6, Sun Oct 12, Sat Oct 18, Fri Oct 31, Wed Oct 15, Thu Oct 2 are all correct for 2025.
- **Build facts match the base Jenkins feed** (#builds channel C05433XK267): Match3D Android #440 Apr 5, #456/#457 Apr 7, #475 Apr 8, #633 Apr 29, #771 May 28, #852 Jun 5, #1427 Jul 28, #1450 Jul 29, #1452 Jul 29 (branch …/ZombieSwap), #1529 Aug 4 UTC, #1630 Aug 13, #1896 Sep 16, #1935 Sep 22, #1966 Sep 24; Match 3D iOS Internal #1232 Jul 29 (…/ZombieSwap). So the deck's "older than Android #1452 / iOS 1232 (the zombie swap with the new background, Jul 29)" is supported. "Captured Dec 5, 2024 … before the first Match3D build" is consistent (first Match3D Android build Jan 12, 2025). Re-capture comments follow each build's success time (e.g. #1966 success 18:10Z, comment 18:40Z).
- **Linear ↔ sheet ↔ Trello.** Every Unity-sheet row's ART ticket exists with matching title/format; "Live since" dates are on/after capture dates; Archive "Paused on" dates (Sep 15 ×3, Sep 19) equal the Canceled tickets' updated_at. ART-831 ("Not on the live creatives sheet yet") and ART-826 (julia 4:5, absent from the sheet) agree with Frederick's Trello comment that Julia's 4:5 static "never made it onto the live creatives sheet". Every non-canceled issue's updated_at equals its latest comment time; no comment predates its issue.
- **Thread/timing chains.** Robert's reply 1h42m after Martin's base post; Marcus's reply after Claire's parent; Drive files created before the Slack messages that announce them (Store PNGs 15:12Z → Martin 15:20Z; MP4s 17:05Z → Marcus 17:20Z); folder modified times equal their latest child; deck created 16:10Z before Robert's 16:30Z post; Trello card 22:00Z → Leonard's Slack 22:05Z → calendar invite 22:10Z → Frederick's changes mail 23:10Z → Trello comment 23:20Z; board dateLastActivity updated to the new latest action.
- **Base context supports the scenario.** Frederick's Aug 13 #zombie_marketing thread (cited by ART-809) exists: music baked into the first cut, then Marcus's no-music exports, so both master types are supported. Base Slack (executives mpdm) shows Unity phone and tablet campaigns, iOS UK retention campaigns, budgets cut to $1 on Sep 19 and iOS turned back on Sep 29; compatible with "still running (checked Sep 29)" and Sep 17–25 uploads.
- No grader-facing text in injected records; SQL comments describe content only (no tool-call, pass-rate or gate language).

## 6. Advisories (non-blocking)

1. **Columns not in the schema snapshot** (all set to NULL or `'[]'`): linear_issues.`uuid` (62 rows), linear_comments.`sequence` (78), drive_files.`drive_id` (19), docs_documents.`text_style_runs_json` (1), slides_pages.`notes` (4), slides_page_elements.`table_json`/`ordinal` (8), gcal_events.`extras_json` (7), trello_cards.`start`/`"idAttachmentCover"` (1). The snapshot is unverified, so this is not a defect. If the platform rejects any of them on load, dropping them from the column and value lists loses nothing.
2. **Canceled tickets without `canceled_at`:** ART-836, ART-837, ART-838 (Sep 15) and ART-839 (Sep 19) have state Canceled but canceled_at NULL. All 372 base Canceled issues set canceled_at. Nothing contradicts this, but setting canceled_at to each ticket's updated_at (`2025-09-15T17:00:00Z` / `2025-09-19T17:00:00Z`) would match the base and the Archive tab.
3. **SC-11 (Snowflake base conflict touched):** Frederick's Trello comment calls Julia's 4:5 "still our best CPI there" (iOS UK). Snowflake books every unity_ads row at spend 0 / CPI 0, while Slack shows paid Unity bids. /prompt decides whether the task depends on this. Keep rubric rows and OEs off Unity CPI values from Snowflake. The comment's own fact (keep ART-826 in scope) doesn't depend on Snowflake.
4. **Sheet Drive row:** base spreadsheets all carry a content_path. The injected sheet has none but is served through its gsheets rows, which the lint accepts. Make sure the task reads it through Sheets, not as a Drive file download.
5. **Vendor offer vs. an existing purchase (context):** the KayKit "Halloween Bits" bundle offered to Claire (Sep 24) was already bought on Jan 20, 2025 (Unity Asset Store confirmation in Robert's mailbox; asset-seat emails in Arthur's). This is consistent supported context, not a contradiction. /prompt should check whether Claire can see that evidence if the task relies on it.

## 7. Findings

No demonstrated defects. No repair is required for this static scope.

## 8. Stage dependencies for reuse

Verified facts above depend on SQL sha256 `df47d906…bd24`, synth-cut manifest `da2f4cf0…aac1a`, the fixed clock 2025-10-01T07:00Z, schema snapshot `31dcb2b4…` and id_contracts `fc4711ef…`. Collision/absence claims rely on the complete scans listed in Check A. Any SQL edit invalidates this report: rerun /injection, then /prompt, /hardness, /oe and /rubric.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt. Optionally apply advisories 6.1–6.2 first (any SQL change needs /injection rerun).

Evidence limits: Static review only. No live execution or deployment check; the schema snapshot is unverified (10 columns not covered, advisory). Media files are metadata-only. Agent visibility, task discoverability and difficulty belong to /prompt and /hardness.
