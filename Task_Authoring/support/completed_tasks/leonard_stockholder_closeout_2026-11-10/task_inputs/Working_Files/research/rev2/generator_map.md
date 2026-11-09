# Generator map (rev2)

Read-only map of the generators under `Working_Files/plan/` and `Working_Files/solver/`, written 2026-11-08 for whoever edits
records next. Paths are relative to `Task_Authoring/task_inputs/Working_Files/` unless they start with `Task_Authoring/` or
`task_inputs/`. Line numbers are for the files as they stood when this was written (build_sql.py 506 lines, build_scenario.py 503,
solver.py 276, assemble_design.py 493, dossier_text.py 279, assemble_dossier.py 176, build_final_manifest.py 115,
build_dispositions.py 76, finish.sh 37, run_checks.sh 32). `*.pre_sweep.py` are stale copies: do not edit them.

## 0. File inventory and data flow

```
holder_facts.json ─┐            last_mail.py ──> last_mail.json ─┐   (last_mail.py is NOT run by finish.sh)
00_Task_Context.json ─> build_scenario.py ──> 01_Hardness_Manifest.draft.json + 01_Gradable_Surface.json
                         │  (imported by build_sql.py and assemble_design.py; every import rewrites both files)
                         ├─> assemble_design.py ──> 01_Scenario_Design.md   (--scenario only)
                         └─> build_sql.py ──> task_inputs/01_Universe_Inject.sql + plan/sql_ids.json
                                   owner_list_bodies.json ─┘
sql_ids.json + draft + design_delta.json ─> build_final_manifest.py ─> 01_Hardness_Manifest.json (solver digest)
SQL ─> solver/solver.py (via tools/oracle_kit.py truth) ─> solver/truth.json
tools --json ─> build_dispositions.py ─> 01c_Dispositions.json
SQL + sql_ids + final manifest + truth + plan/*.txt + research/g1_grounding.md + dossier_text.py ─> assemble_dossier.py ─> 01_Grounding_Dossier.md
```

`owner_list_slack.json` and `LAST_PT` (build_sql.py 447-448) and `channel()` (build_sql.py 436-442) are dead: nothing reads them.

## 1. finish.sh: steps, outputs, gates, flags

Flag: only `--scenario` (`$1`, line 9). No `set -e` (line 3 is `set -u`), so a failing step does not stop the run; output is
cut/grepped, so read the files, not the console. Runs from the workspace root (line 4), exports `TASK_AUTHORING_TASK_DIR`.

| Line | Step | Writes |
|---|---|---|
| 8 | `build_scenario.py` | `01_Hardness_Manifest.draft.json`, `01_Gradable_Surface.json` |
| 10 | (--scenario) `policy_scores.py` | `plan/policy_scores_output.txt` |
| 11 | (--scenario) `run_forecast.sh --preregister` = `hardness_forecast.py forecast --design ... --mechanisms ADV,LETTER,TOLD,ASOF,FAM,BOARD,ASK` (run_forecast.sh line 3: mechanism list is hard-coded) | `plan/forecast_output.txt` |
| 12 | (--scenario) grep last `hev_...` id | `plan/forecast_id.txt` |
| 13 | (--scenario) `assemble_design.py` (runs hardness_gate --design, gradable_surface validate + gradeable-report, trap_liveness --design, hardness_v2_check --design and pastes them; lines 14-18) | `01_Scenario_Design.md` |
| 14 | (--scenario) `write_evidence.py` | `00_V3_Authoring_Evidence.json` |
| 15 | (--scenario) GATE `stage_gate.py scenario --paste` (on PASS pastes the gate block into the design's Self-review) | `01_Scenario_Design.md` |
| 17 | `build_sql.py` (imports build_scenario again) | `task_inputs/01_Universe_Inject.sql`, `plan/sql_ids.json` |
| 18 | `touch solver/solver.py` (keeps the solver newer than the SQL for staleness checks) | - |
| 19 | `seed_snapshot.py` | `research/sweeps/seed_snapshot.md` |
| 20 | `build_final_manifest.py` | `01_Hardness_Manifest.json` |
| 21 | `run_checks.sh` (no flag): sql_lint, hg.py lint, base_check, base_claims, fact_check --no-leak, hardness_gate (final manifest + SQL), persona_view check-sql (with `plan/load_bearing_ids.txt`), oracle_kit check, oracle_kit truth, difficulty_mutation mutate + geometry, trap_liveness (reads the previous `01c_Dispositions.json`) | `plan/{sql_lint,base_check,base_claims,fact_check,hardness_gate,checksql,oracle_kit,oracle_truth,mutation,geometry,trap_liveness_sql}.txt`, `plan/hg_lint.json`, `solver/truth.json` |
| 22 | `build_dispositions.py` (runs difficulty_mutation mutate --json and trap_liveness --json) | `01c_Dispositions.json` |
| 23 | `run_checks.sh --preflight`: all of line 21 again, plus `hardness_forecast.py forecast --preregister` (channel-rate label `...policy_scores-rev1`, run_checks.sh 26) and `preflight_report.py` | adds `01c_Forecast.json`, `01c_Preflight_Report.json/.md`, `plan/forecast.txt`, `plan/preflight.txt` |
| 24-25 | copies the SQL to `run_forensics/rev1/01_Universe_Inject.sql` | **hard-coded rev1: for rev2 change both lines to rev2 first, or the archived rev1 SQL is overwritten** |
| 26 | `assemble_dossier.py` | `01_Grounding_Dossier.md` |
| 27 | GATE `stage_gate.py injection --paste` | dossier Self-review |
| 29-33 | inline Python strips the trailing pasted `STAGE GATE error-async` block | edits `task_inputs/03_Error_Async_Config.txt` in place |
| 34 | GATE `stage_gate.py error-async --paste` | `03_Error_Async_Config.txt` |
| 35 | `assemble_brief.py` | `04_Prompt_Writing_Brief.md` |
| 36 | `write_brief_evidence.py` | `00_V3_Authoring_Evidence.json` |
| 37 | GATE `stage_gate.py prompt-writing --paste` | brief |

Other hard-coded "rev1" labels to bump for rev2: assemble_dossier.py 98 (heading), build_final_manifest.py 17 (`_note`),
build_dispositions.py 73 (`_note`), solver.py 143 (`revision or "rev1"`) and its docstring line 1, run_checks.sh 26 (rate label).

## 2. Record emitters (file, function/variable, lines, text source)

All in `plan/build_sql.py` unless stated. Emit helpers: `ins()` 75-77 (one INSERT, records the key in ROWS), `upd()` 80-83
(UPDATE ... WHERE key), `q()` 55-65 (SQL literal; `E'..'` with `\n` escapes when text has a newline). SQL section order is fixed
at line 490 (gdrive, gdocs, gsheets, gslides, slack, trello, gmail, gcal, contacts, linear). SQL line numbers are for the current
`task_inputs/01_Universe_Inject.sql` (279 lines).

| Record | Text variable (lines) | Emitted by (lines) | How the text is built | SQL lines |
|---|---|---|---|---|
| Close-out notes doc `f_a37b403d5200d4f0a31d31` | `NOTES_DOC` 91-115 | `gdoc(B.DOC_NOTES, NOTES_DOC, B.FOLDER, T["notes"], "3c986c6ce3")` line 258; `gdoc()` 243-253 writes a `gdrive.drive_files` row via `drive()` 239-240 and a `gdocs.docs_documents` row | Literal. Title = first line ("Stockholder close-out notes"); body = text + "\n"; `style_runs_json` computed (TITLE run over the first line, NORMAL_TEXT after). Id from build_scenario.py 15; parent = folder `B.FOLDER` (build_scenario 15); time `T["notes"]` 2026-02-13T01:05:41Z (line 33); revision id literal | drive 9-10, docs 18-19 |
| Older "Holder outreach notes" `f_762c60832854d3e7a7f7df` | `OLD_DOC` 116-124 | `gdoc(B.DOC_OLD, OLD_DOC, ROOT, T["old"], "84bdd1a5ac")` line 259 | Literal; parent = Leonard's Drive root `ROOT` (line 19), `T["old"]` 2026-02-10T17:41:09Z | drive 11-12, docs 20-21 |
| Folder `d_601064334a0b493022fe83` | `FOLDER_NAME` 256 | `drive(...)` 257 | Literal name; created `T["folder"]`, modified `T["notes"]` | 7-8 |
| Linear project `ec2ea957-...` | `PROJECT_DESC` 125-128 | `ins("linear.linear_projects", ...)` 416-418 | Literal; name "Holder records" literal at 418; created `T["project"]`, updated `T["project_upd"]` (after Sunset's mail) | 121-122 |
| 26 Linear issues ENG-2438..2463 | loop over `B.HOLDERS` (build_scenario.py 50-77) at 461-487 | `ins("linear.linear_issues", ...)` 480-481 | **Title**: `holder_facts.json[k]["title_form"]`, overridden by `TITLE` 451 (ENG-2447 "Husnu Matthew Collins", ENG-2460 "Brian Foster"). **Description**: `f"Email: {EMAIL[k]}" + NOTICE.get(k, "")`; `EMAIL` is a literal dict 454-459 (sources in the comment 452-453); `NOTICE` 460 is an empty legacy hook (notice route removed in rev7). State literal "Backlog", creator `LIN[LEO]`, number from the key. `created_at` = `T["issue0"]` then `+ step("issue|k", 6, 34)` s cumulative (465-466); `updated_at` = that issue's `fig_at` | issue n (0-based) INSERT at 123+6n, VALUES 124+6n (ENG-2457 238, ENG-2461 262, ENG-2463 274) |
| 52 Linear comments (2 per issue) | built in the same loop 469-478 | `ins("linear.linear_comments", ...)` 483-486 | Comment 0 (last-mail): `last_text` 476-477 = `"Last mail with that address before Feb: {when(date_pt)}"` or `"No mail with that address before Feb"`, from `LASTMAIL[k]["date_pt"]` (`last_mail.json`, loaded 449, produced by `last_mail.py`: newest message in Leonard's mailbox before 2026-02-01 PT carrying `EMAIL[k]` in from/to/cc/bcc; `when()` 431-433 formats "Jan 24, 2026"). Comment 1 (figure): `fig_text` 469-475 from `holder_facts.json[k]["owner_list_figure"]` ("Nov 2024 owner list: X", Griffin pair "..., both funds on one line", empty figure -> "Not on the Nov 2024 owner list"). Ids `"comment_" + hx(f"note|{k}|{i}", 32)` 484; times `last_at` (T["last0"] + step 8-20 s) and `fig_at` (T["fig0"] + step 26-70 s), assertion `last_at < T["robert"]` 479 | 125-128 for ENG-2438, then +6 per issue; last 276, 278 |
| KPMG request | `KPMG_ID` 23, `KPMG_SUBJECT` 136, `KPMG_BODY` 137-159 | `message("kpmg", LEO, B.TH_KPMG, ...)` 352 (cc `KPMG_CC` 351) | Literal; new thread row (thread id `B.TH_KPMG`, build_scenario 17); `T["kpmg"]` 2026-02-13T16:48:33Z; labels `LABEL_IN` | thread 77-78, message 79-80 |
| Leonard's ack | `ACK_ID` 24, `ACK_BODY` 160-166 | `message("kpmg_ack", ...)` 353-354 | Literal head + computed quote of `KPMG_BODY` ("> " per line); parent `KPMG_ID`; thread snippet UPDATE | 81-83 |
| KPMG follow-up | `FOLLOW_ID` 167, `FOLLOW_BODY` 168-177 | `message("kpmg_follow", ...)` 355-356 | Literal; subject "RE: " + subject; parent `ACK_ID`, refs `KPMG_ID ACK_ID`; `T["follow"]` 17:37:15Z | 84-86 |
| Sunset request + ack | `SUNSET_ID` 25, `SUNSET_SUBJECT/BODY` 179-198, `SUNSET_ACK_ID` 178, `SUNSET_ACK` 358-359 | `message("sunset", ...)` 357, `message("sunset_ack", ...)` 360-361 | Literal; ack quotes the body (computed); new thread `B.TH_SUNSET` | 87-93 |
| Leonard's Jan 14 #executives note | `EXEC_FIX` 285 (ts `1768418331.402719`, channel literal `C07C2866011`) | `ins("slack.slack_messages", ...)` 286-289 | Literal top-level message, no thread; id `slack_id("C07C2866011", ts)` | 51-52 |
| #winddown origin posts (3) | `ORIGIN` 129-131 | loop 291-295 | Literal, top-level in `B.WD` | 53-58 |
| #winddown family thread reply (4 messages: family line, Covered label, Arthur sharing, Arthur's "sounds good") | `AMEND` 132-135 | loop 296-300, then parent UPDATE 301 | Literal; `thread_parent_id = LIST_ID`, `thread_ts_legacy = LIST_TS` (base parent, line 290); UPDATE on the parent sets `reply_count = len(AMEND)`, `reply_users_count 2`, `latest_reply = AMEND[-1][0]` (2 is literal: change it if the speaker set changes) | 59-67 |
| Robert's board reply-all | `BOARD_PARENT` 362, `BOARD_REFS` 363, `BOARD_ID` 364, `BOARD_BODY` 365-377, `BOARD_TO` 378, `BOARD_CC` 379 | loop 380-383: three `message()` calls (Leonard `.../1856958794180374704` INBOX; Robert `.../1856959418563541618` SENT; Arthur `.../1856959418725253571`) | Literal body with a quoted fragment of Leonard's base reply; same Message-ID in all three mailboxes; base threads, so `new_thread=False` (snippet UPDATEs); `T["board"]` 2026-02-12T22:38:16Z | 94-102 |
| Robert's reply to Nebojsa (T7) | `ROBERT_ID` 26, `ROBERT_PARENT` 27, `ROBERT_SUBJECT/BODY` 199-210, `NEB_TO` 384, `ROBERT_REFS` 385 | `message("robert_leo", ...)` 386-387 (thread `B.M_NEB_THREAD`, build_scenario 18), `message("robert_rob", ...)` 388-389 | Literal; base threads; `T["robert"]` 23:41:12Z | 103-108 |
| Owner-list UPDATEs (both copies of the Nov 26, 2024 list) | `owner_list_bodies.json` (one line, entries `{file, id, body}`) | loop 391-395 | Computed: base body with the one sentence "(Total ownership percentage adds to 100%)." removed; asserts the old text is present | 109-110 |
| Contacts | literals in 407-411 | 2 INSERTs (Bergmann `hx("contact_bergmann", 24)`, Eren `hx("contact_eren", 24)`) + 1 UPDATE on base `db57e559500151d6b3991b62` (job "Investor and advisor (left the board May 2025)", updated_at 2025-05-02T16:20:11Z) | Literal token names/emails; times `T["folder"]` and +41 s | 115-119 |
| Draft holder sheet `f_5ecaa967db3adcfa440b09` | `DRAFT_TITLE` 214, `DRAFT_GRID` 215-223 | `drive()` 261, `sheets_spreadsheets` 262-264, `sheets_sheets` 265-266 (`grid_json` = `js(DRAFT_GRID)`) | Literal grid (figures copied from the owner list, "copied from the Nov 2024 list"); `T["sheet"]` 2026-02-10T18:12:26Z | drive 13-14, 23-26 |
| Deck `f_75dddccabb26eeea4842c8` | `DECK_TITLE` 224, `DECK` 225-229 (one string per slide) | `drive()` 268, presentation 269-271, per-slide page + element loop 274-278 | Literal slide text; page ids `PAGES` 272 (two literal, rest `"slide_" + hx(f"deck-page-{n}", 12)`), element ids `ELS` 273 likewise; one TEXT_BOX per slide | drive 15-16, 28-49 |
| Trello card + actions | `CARD_NAME/DESC/COMMENT` 211-213 | 304-321 | Literal; see id rules below; board `dateLastActivity` UPDATE 320 | 69-75 |
| GCal hold | `HOLD_SUMMARY` 230 | 397-404 | Literal; 30 min from `T["hold_start"]` | 112-113 |

**UPDATE statements (complete list, 13):** Slack parent counters (301; SQL 67); Trello board activity (320; SQL 73); Gmail
thread snippets from `message()` 342-343 whenever `new_thread=False` (kpmg_ack, kpmg_follow, sunset_ack, 3 board copies, 2
Robert copies; SQL 81, 84, 91, 94, 97, 100, 103, 106); owner-list bodies (395; SQL 109-110); Contacts job (409; SQL 117).

### 2a. Id, thread, Message-ID and timestamp conventions

- **Times.** All seeded times sit in the dict `T` (build_sql.py 31-36). Helpers: `ep()` 43-44 ISO->epoch, `iso_of()` 47-48,
  `plus(iso, sec)` 51-52. Deterministic jitter: `step(label, lo, hi)` 427-428 = `lo + int(hx(label, 6), 16) % (hi-lo+1)`.
- **Hash ids.** `hx(label, n)` 39-40 = `sha256("hg-leonard-closeout|" + label)[:n]`. Used for contact ids, comment ids, deck ids,
  Trello action suffixes, the GCal `ical_uid` (`hx("hold_ical", 32) + "@hg4"`).
- **Fixed ids** (Drive/Docs/Sheets/Slides, folder, project, Trello card, event, Gmail thread ids of new threads, base thread
  ids): constants in build_scenario.py 11-23 and build_sql.py 15-29, chosen from `research/s4_carrier_formats.md`
  (collision-checked). Trello ids start with the 8-hex epoch of their time (card `698e5a10...` = 2026-02-12T22:54:08Z).
- **Gmail** (`message()` 330-347). Message row id = `f"{box}/{raw_id}"` (344), where `raw_id` is the literal RFC Message-ID with
  angle brackets, hand-written in the sender's real client format: Leonard Gmail `<CAPBs_...@mail.gmail.com>`, Robert
  `<CAGkro_...@mail.gmail.com>`, KPMG Outlook `<LV3PR19MB8524<hex>@LV3PR19MB8524.namprd19.prod.outlook.com>`, Sunset Superhuman
  `<mlkq74xd.<uuid>@we.are.superhuman.com>`. Base formats worth copying: Carta notices
  `<{epoch*100}.10.{19 digits}@notifications-email-sending-worker-{pod}>` (e.g. ES-14's, date 2026-02-12T22:31:54Z) and Gmail DSN
  bounces `<{8-hex epoch}.{8hex}.{5hex}.{4hex}.GMR@mx.google.com>` (base example `robert@harmonygames.co/<64934165.170a0220.5e42c.6a02.GMR@mx.google.com>`,
  subject "Delivery Status Notification (Failure)", body "** Address not found ** ... wasn't delivered to X ...", file
  `Normal_HarmonyGames_Gmail/.../threads/00001116.json /messages/1`). Thread row id = `f"{box}/{19 digits}"`; for new threads the number is
  about `(epoch_ms << 20) + random low bits` (TH_KPMG decodes to 16:48:35Z for a 16:48:33Z message; TH_SUNSET 18:06:22.9Z for
  18:06:21Z). `new_thread=True` inserts the `gmail_threads` row (341); otherwise the snippet is UPDATEd (343). Row fields:
  `internal_date` = ms, `date` = ISO, Date header via `email.utils.format_datetime` (+0000), body CRLF, snippet = first 140
  chars collapsed, `size_estimate` = len + 900, In-Reply-To/References from `parent`/`refs`, labels `LABEL_IN`/`LABEL_SENT`
  (28-29). `GLOG[key] = {message, thread}` (347) goes to `sql_ids.json["gmail"]` and is read by build_final_manifest.py
  (THREAD_TO_MSG 28, facts home_ids 82-92) and assemble_dossier.py (`GM`, `TH` 24-25). Base files are named
  `threads/leonard@harmonygames.co_<thread>.json` (mailbox key `leonard.hayes@...`).
- **Slack.** `ts` strings are literals in `EXEC_FIX`/`ORIGIN`/`AMEND`; row id `slack_id(channel, ts)` = `sha256(f"{channel}|{ts}")[:32]`
  (86-87); `created_at = iso_of(float(ts))`; users `SLACK_U` 17. `SLACK["C/ts"] = id` goes to `sql_ids.json["slack"]`;
  build_final_manifest.py `map_id()` 31-34 rewrites every `"C/ts"` pointer in the draft to the row id. The solver recomputes the
  same hash for the family reply (solver.py 26-30).
- **Linear.** Issue id = identifier = `ENG-24xx`; comment ids and times as in the table above.
- **Trello.** Action id = `"%08x" % epoch + hx(label, 16)` (317, 319); `shortLink` = base64(sha256(SALT+card))[:8] with
  `+`->`x`, `/`->`Q` (308).

## 3. Solver: how each truth field is computed (solver/solver.py)

Contract: `load_state()` 133-143 parses the SQL with `tools/base_check.parse_sql` and indexes **INSERT rows only** by `id`,
`identifier`, `document_id`, `spreadsheet_id`, `presentation_id`, `event_id`. Almost every figure is a **constant** from base
research (`STOCK` 34-47, `OPTION` 49-64, `COMMON` 65, sets 66-69); the SQL only switches rules on through five deciding records:

| Constant | Id (line) | Test in `solve()` |
|---|---|---|
| `R_NOTES` close-out notes | 22 | present (157) |
| `R_KPMG` FY25 request | 23 | present and body contains "December 31, 2025" (158) |
| `R_ROBERT` reply to Nebojsa | 24 | present and body contains "closing" (159) |
| `R_FAMILY` family reply | 30 (`_slack_id("C0ADGSZKR3R", "1770949310.220519")`) | present and text contains "for a family" (160) |
| `R_BOARD` Robert's board reply | 31 | present (234) |

Rule switches: `_off(rule, key, disable, degrade)` 150-151 is true when the rule is disabled or the key is a member hit by
`ch_<rule>`; over-application operators are hard-coded per control key (184, 189, 191, 208, 214, 217, 236). Keys: 12 STOCK +
14 OPTION + SUMMARY (`KEYS` 70). Truth lands in `solver/truth.json` via `oracle_kit.py truth` (run_checks.sh 21).

| Field | Stock lines (176-198) | Option lines (199-224) |
|---|---|---|
| Holder | SQL issue `title` if the issue row exists, else the STOCK name (`title()` 162-163) | same |
| Instrument | "Series Seed and advisor options" if the advisor grant counts, else "Series Seed" | "Option" |
| Shares held now | `listed - adv` when ADV is on (STOCK col 3 owner-list figure, col 4 advisor grant from the Due Diligence table), else `listed`; `adv_over` takes 6,104 off ENG-2441/2442 (191-192) | 0 |
| Options now | the advisor grant (ADV on) else 0 | `vested` (OPTION col 4) if live, `granted` if `live_miss` misreads a lapsed line, else 0 (219) |
| Options at Dec 31 | the advisor grant (advisor grants count at every date) | `as_of()` 168-173 when the KPMG test passes and ASOF is on: `last <= 2025-12-31` -> 0; `effective > 2025-12-31` -> full `granted`; else `vested`. Off: today's value. `asof_over` on ENG-2455 -> vested (217-218) |
| Last day | None | OPTION col 6 if live, else None. Live = `last >= CLOCK` ("2026-02-14", line 19) or a `live_miss` misread (203-204) |
| Told | STOCK col 5 constant (Griffin pair True from base mail; others False). `TOLD_ELSEWHERE` {2440, 2446} (68): told only if notes present and TOLD on, and for ENG-2446 also the Robert test (182-183). `told_over` makes ENG-2448 told (184-185). DMs and letters are **not read from SQL**: Segerstråle's Feb 9 DM is base and only gated through `R_NOTES` | OPTION col 7 = had a Feb 11 letter (True for ES-1, 4, 7, 12, 13, 15). `NO_LETTER` {2459, 2463} (67) count as told when the notes are absent or LETTER is off (206-207). `letter_over` flips ENG-2450/2460 to untold (208-209). None for lapsed lines (222) |
| Owed | "Already told" if told else "First note"; "Covered" for `FAMILY_COVERED` {2444, 2445} (66) when the family test passes and FAM on; `fam_over` makes ENG-2442 Covered | "Nothing" if lapsed; live: "Date note" if told else "Full note" (210-212); `ask_over` gives ENG-2461 "Date note" |
| State | "Todo" if First note else "Done" (197) | "Canceled" if Nothing else "Todo" (223) |
| Open question | None | "equity" for ENG-2453 if notes present and ASK on (213); `ask_over` -> "exercise" on ENG-2461 |

SUMMARY (225-241): Common 6,000,000; Series Seed total = sum(listed - adv) = 3,051,879; options now = sum(vested of lines with
`last >= CLOCK`) + 103,764 grants = 55,942 + 103,764 = 159,706 (231); at Dec 31 = sum(`as_of`) + grants = 139,993 + 103,764 = 243,757
(232); issued plus options = 6,000,000 + 3,051,879 + 243,757 = 9,295,636; Directors "Leonard Hayes, Robert" unless BOARD is off or
`R_BOARD` is missing (four directors) or `board_over` (Leonard only); Griffin share = (2,662,255 + 84,438) / seed = 90.0 %. Note
SUMMARY loops `OPTION` with the raw col 6, so any per-line last-day override must be applied there too (231-232).
`aggregates()` 245-258: class and state counts, notes = First+Date+Full, reason comments = 26 - notes, `first_to_go` = earliest
`Last day` among `Told == "No"`. `deciding()` 269-272 lists each rule's seeded deciding records (used by intervention checks).

### 3a. Recipes

**(i) A delivery-failure notice that makes one letter-told holder untold.** Pick a holder whose *only* told record is the Feb 11
letter: ES-12 Owen Baker (ENG-2457, letter `leonard.hayes@harmonygames.co/<CAPBs_a5HKTOGV3nwn6iyxz8GhwLGRaF_Gs-uii3x7tVQ9eTfQQ@mail.gmail.com>`,
thread `.../1856860994291529096`, sent 2026-02-11T20:13:48Z to PERSON_3140_EMAIL) or ES-7 Marcus (ENG-2456, work address). ES-1, 4, 15
were also told in group DM C51ECE5102ED and ES-13 in DM D05Q3QAH2QZ (`research/s2_option_notice_state.md` lines 152-166), so a bounce
does not untell them. ES-1 and ES-15 are the LETTER controls; do not use them.
1. build_sql.py: add `T["bounce"]` (a minute after the letter) and a `message("bounce", LEO, f"{LEO}/1856860994291529096", "<{hex epoch}.….GMR@mx.google.com>", "PERSON_3555_EMAIL"-style daemon sender, ..., "Delivery Status Notification (Failure)", body, T["bounce"], LABEL_IN, parent=<letter id>, new_thread=False)` in the Gmail block (after 389).
2. Close the rule first: H1's told sentence (NOTES_DOC 108) says "sent to them directly"; a bounced letter was sent, so the rule must say it reached them (or that a message that came back does not count). Then follow (iii) for that sentence (facts 84-85 in build_final_manifest.py, assemble_design.py 258, assemble_brief.py 80, dossier_text.py CR row 246).
3. Route: `EMAIL["ENG-2457"]` (build_sql.py 458) equals the bounced address, and NOTES_DOC 112 says messages go to the issue's email. Either the bounce names a different address than the issue's, or the issue's Email line moves to a grounded alternative; if you change it, re-run `ONLY=ENG-2457 last_mail.py` (it re-reads `EMAIL` from build_sql.py by regex, line 12).
4. solver.py: add `R_BOUNCE = f"{MB}/<…>"`; in the option loop after line 205: `if k == "ENG-2457" and have(R_BOUNCE) and not _off("LETTER", k, disable, degrade): told = False`; add ENG-2457 to `MEMBERS["LETTER"]` (118) and `R_BOUNCE` to `deciding()` LETTER (270). Fits the existing `ch_letter` text ("a member's missing letter is not noticed: the member counts as told"). Outcome: Told No, Owed Full note, State Todo (unchanged); Date note 6->5, Full note 2->3; notes 14, reason comments 12, first_to_go ES-14 and every figure unchanged.
5. build_scenario.py: HOLDERS line 70 class -> "Full note"; `MEMBERS["LETTER"]` 241; a new trap (family `done_gap` or `superseding`) with `seeded=[bounce message id]`, `base=[letter id]`, `versions=[vr("gmail", letter, "2026-02-11T20:13:48Z", "gmail:1856860994291529096"), vr("gmail", bounce, T, "gmail:1856860994291529096", True)]`; add the node to PORTFOLIO LETTER `nodes` (222) and a hop to chain C2 (254-256); slots: new `TC_ES12` (["field","ENG-2457","Told"]) and `C_ES12` (Owed) with `["LETTER"]`, `C_DATE` regex `(6|six)` -> `(5|five)` (413), re-point `ND_ES-12` (446-448, it is a date-note sample); add the new slot ids to LETTER `decides` (223).
6. Downstream literals: assemble_design.py 270 (counts), 96 (CAND LETTER), TWO table 110-132 (add the bounce decision point); assemble_brief.py 109, 115; write_brief_evidence.py 17, 19; write_check_findings.py 27; dossier_text.py findability 26-44, DIS 103-113, facts-for-the-human 138-167, CR 241-265; build_dispositions.py `TEXT["LETTER"]` 33; build_final_manifest.py optional fact (82-92) and `FILE_POINTERS` 48-53 if the gate's base lookup of the letter thread hits an attachment; `plan/load_bearing_ids.txt` (add the bounce id); `plan/design_delta.json` (new entry).

**(ii) A Carta notice extending one lapsed line's window.** Lapsed lines: ES-2 (ENG-2451), ES-3 (2452), ES-5 (2454), ES-6 (2455),
ES-16 (2461), ES-17 (2462). Avoid ES-6 (ASOF control), ES-17 (T15/T16, P_FRED), ES-5 (NB-32: never grade his end date) and ES-16
(ASK control `ask_over` is hard-coded on ENG-2461 at solver 214 and build_scenario 239; its issue Email is a work address,
cameron@harmonygames.co). ES-3 Calvin Price (base notice `leonard.hayes@harmonygames.co/<176175436721.10.9685252272573766647@notifications-email-sending-worker-6b65bf6cf7-dg8x2>`,
thread 1847333347700620793, 2025-10-29) is the cleanest.
1. build_sql.py: add `T["ext"]` and a `message()` from `SVC_0077_EMAIL` / `SVC_0077_NAME` (Carta's base sender), subject in Carta's form ("Termination details for Calvin Price"), body copying the base notice layout with a new "Last day to exercise", Message-ID in Carta's format, labels `LABEL_IN`; a new thread (pick a 19-digit id ≈ `ms << 20`) or the base thread.
2. Rule check: NOTES_DOC 106 "Carta is the record ... If a line's last day has passed, it holds nothing" does not say the later Carta notice wins; consider "Carta's latest notice is the record" (then (iii)).
3. solver.py: add `R_EXT` and `EXT = {"ENG-2452": "2026-04-24"}`; a helper `last_of(o)` returning the extended date when `have(R_EXT)` and the governing rule is on; use it at 203-204, 222 and in SUMMARY 231-232 (`as_of` is unchanged, since the old last day is already after Dec 31). Effects for ES-3: live, Told No, Owed Full note, State Todo, Options now 4,408, Last day the new date; options now 159,706 -> 164,114; notes 14 -> 15, reason comments 12 -> 11, Canceled 6 -> 5, Todo 14 -> 15; first_to_go stays ES-14 if the new date is after Feb 21. Remove ENG-2452 from `CHANNELS["CH-LIVE"]` (126) since `live_miss` only acts on lapsed lines.
4. build_scenario.py: HOLDERS 65 class; CH-LIVE members 246; ASOF members 242 (still valid: as-of unchanged); slots `P1` regex `159,?706` (403), `P_lapsed_ES3` (404-405), `LC_ES-3` (468-469), `LS_ES-3` (471-472) must be re-pointed; T3 resolver text "leaving 159,706 live" (126); a trap (family `superseding`, versions = base notice then the new one); chain hop; if it is a new rule, see section 4a.
5. Downstream literals: assemble_design.py 270, 359 ("14 personal notes"), 401, 461 (159,706 literal-value sweep), H2 "14 hits" (281); assemble_brief.py 65, 109, 115, 118; write_brief_evidence.py 17-20, 31; write_check_findings.py 27-31; build_scenario.py `BUDGET_COND` 297 (14 notes) and WRITES 303 (count 14), 306 (12 comments); dossier_text.py lists; load_bearing_ids.txt; design_delta.json.

**(iii) Removing or rewording a sentence.** Change the generator text, then every place that quotes or paraphrases it:
1. The record: build_sql.py (`NOTES_DOC` 91-115, `PROJECT_DESC` 125-128, `AMEND` 132-135, `EXEC_FIX` 285, mail bodies).
2. Manifest facts (build_final_manifest.py 82-92): values must stay verbatim substrings of their `home_ids` records (fact_check). Today: told rule = NOTES_DOC 108, line rule = 106, owed rule = 109, family rule = AMEND[0], state rule = PROJECT_DESC, "we're closing the company" = ROBERT_BODY, "That leaves Leonard and me on the board" = BOARD_BODY.
3. build_scenario.py: FRAGS `delegation_quote` and `names_authorities` quotes (192-210) must be verbatim in `delegated_by_record` (notes doc quotes: "the reach-out I promised", "where I left things today", "the investor email on the Task List", "the holder sheet comes first", "notes ready for me by Tuesday", "the update outline", "everything goes in the close-out folder", "reply under my list in #winddown", "Carta is the record"; project quotes: "one issue per holder on Carta, live or lapsed", "my close-out notes have how each holder gets handled", "what Sunset asked for", "as I said in #winddown"); trap `resolver` / `expected_wrong_reading` (115-190); PORTFOLIO `natural_reading` (218-240); surface label synonyms `yes_no` 489-491 (they follow "Labels for the sheet", NOTES_DOC 114, and AMEND[1] "Covered").
4. solver.py substring tests 158-160 ("December 31, 2025", "closing", "for a family") and the rule logic itself if the meaning changes.
5. Prose copies: assemble_design.py classification predicate 255-264 (a paraphrase of NOTES_DOC, not a copy), TWO 110-132, QC 135-152, counts 270; assemble_brief.py 80-81, 109-118; write_brief_evidence.py 12-31; write_check_findings.py 27-31, 61-64; dossier_text.py findability 26-44, DIS 103-113, constraints 116-127, CR 241-265.
6. Record the change in `plan/design_delta.json` (`{id, change, reason}`; build_final_manifest.py 79 appends it to the manifest's `design_delta`), then re-run finish.sh (with `--scenario` if the draft manifest or surface changed) and re-check the prompt (`task_inputs/04_Prompt.txt`).

## 4. Manifest generation (build_scenario.py data structures)

| Structure | Lines | Becomes |
|---|---|---|
| ids and base pointers | 11-47 | constants used everywhere (design, SQL, dossier) |
| `HOLDERS` (issue, name, Carta id, class) | 50-77 | `surface.truth_keys` (484); class column is used only for the design's holder table (assemble_design.py 88); `I` map 78-79 |
| `REQS` | 81-94 | `requirements` |
| `trap()` helper / `TRAPS` | 107-113 / 115-190 | `traps`; `vr()` 102-105 builds `version_records` (`seeded` -> `id`, else `base_pointer`); build_final_manifest maps ids and sorts versions by `at` (65-73) |
| `frag()` / `FRAGS` | 211-216 / 192-210 | `ask_fragments` |
| `PORTFOLIO` | 218-240 | `mechanism_portfolio` |
| `MEMBERS` | 241-243 | channel members (must equal solver.py `MEMBERS` 116-124) |
| `CHANNELS` | 244-249 | `channels`: CH-LIVE literal + one `CH-<ID>` per PORTFOLIO entry (degrade `ch_<id>`) |
| `CHAINS` | 251-269 | `chains` (root_cause must be a mechanism enum id) |
| `BUDGET`, `BUDGET_COND` | 271-297 | `call_budget` |
| `WRITES`, `SERVICES` | 299-322 | `writes`, `services` |
| `manifest` dict (anchors 340-344, authorities 346-351, cohort + `surf()` evidence surfaces 352-364, hazard acknowledgements 369-374) | 325-377 | `01_Hardness_Manifest.draft.json` (497) |
| `slot()` and the slot calls | 381-387 / 391-480 | `surface.slots`; selectors: `["field", key, solverField]` (direct, must read a solver field), `["text", deliverable, regex]` (write_content), `["delivery", ...]`, `["link", deliverable]`; `mechanisms` must be PORTFOLIO ids |
| `surface` dict (classes, truth_fields, truth_keys, schedule columns, yes_no synonyms, deliverables) | 482-496 | `01_Gradable_Surface.json` (498) |

Solver keys are declared twice: build_scenario `HOLDERS` (truth_keys) and solver `STOCK`/`OPTION` (+SUMMARY). The solver's
`RULES` 72-98, `DEGRADES` 99-115, `MEMBERS` 116-124 and `CHANNELS` 125-130 mirror PORTFOLIO by hand. oracle_kit checks rules <->
portfolio one-to-one, every node a trap or chain, every direct slot reads a solver value, every control is a solver key and every
operator moves a value.

### 4a. New mechanism entry

Template (TOLD, build_scenario.py 225-227):

```python
{"id": "TOLD", "mechanism": "A25", "prior_family": "A25",
 "prior_family_reason": "a completion record sits away from the list that says the work is open",
 "nodes": ["T6", "T7", "T8", "C3"], "requirement": "R4",
 "natural_reading": "the Feb 12 list means no angel has been told",
 "decides": ["C_SEG", "C_NEB", "C_FIRST", "TC_SEG", "TC_NEB", "LC_Seg", "LC_Neb"],
 "controls": ["ENG-2448"], "over_application": "told_over: treats Tor's November runway warning as being told",
 "source": "dm-and-mail", "signature": "Feb 9 DM; Robert's Feb 12 reply"},
```

Fields: `id` (unique, also the solver rule id); `mechanism` (A1-A25 or 2.6.1-2.6.14; A22/A23 are hypotheses); `prior_family` and
`prior_family_reason` (gate-required); `nodes` (existing trap/chain ids); `requirement` (an R id); `natural_reading`; `decides`
(surface slot ids); `controls` (solver keys the rule must leave alone); `over_application` (`"<op>: description"`, op accepted by
`solve()`); `source`; `signature`. Everything that must change with it:
1. build_scenario.py: PORTFOLIO entry, `MEMBERS[id]` (241-243), traps/chains for its nodes, slots tagged with the id.
2. solver.py: `RULES[id]` (its `decides` lists **solver field names**, unlike the manifest's slot ids), `DEGRADES` entries for `<op>` and `ch_<id>`, `MEMBERS[id]`, code in `solve()` honouring `_off(id, …)` and the operator on its controls, `deciding()` 270-271. The engine limit is k <= 8 rules (7 today).
3. build_dispositions.py: `ONLY[id]` 26-32, `TEXT[id]` 33-34, `OVER[op]` 35-36 (a missing key raises KeyError).
4. assemble_design.py: `ANCH[id]` 91 (KeyError otherwise) and a `CAND` row 94-108.
5. run_forecast.sh line 3 `--mechanisms` list.
6. Re-run `finish.sh --scenario` (draft, surface and design change), then the injection half.
