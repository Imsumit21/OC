# Injection Data-Integrity Review (Eval 0)

Review version: `injection-static-v2`
Evidence contract: `stage-evidence-v1`
Review time: 2026-11-02T12:51Z (actual)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Mode: chat review, attempt 6ae4e299a13034b7eb8305f8 (static, SQL not executed)

## 1. Scope and inputs

| Input | Value |
|---|---|
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (input revision 14, from chat attachment `01_Universe_Inject (11).sql`), 148,881 bytes, SHA-256 `4895577edea84edb71253b2c53e41f0eb638fbbc2d60f04927fc0c84c5c6eef9`. Replaces `01_Universe_Inject (10).sql` (SHA `efe3cab1…c881`, last reviewed PASS/COMPLETE), so that report no longer applies. |
| Diff from the previous version | Exactly two hunks (`diff` v10 → v11): **line 3** header comment "11 UPDATE" → "12 UPDATE" (matches the parsed SQL: 130 INSERT, 12 UPDATE); **line 31 added**: `UPDATE gsheets.sheets_sheets SET grid_json = E'…' WHERE spreadsheet_id = 'f_48247af79428823c3cac92' AND sheet_id = 0;`. Every other statement is byte-identical to v10; statements after line 30 shift down by one line. |
| Assignment (context only) | Frederick Stone, Co-founder; not graded here |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Eval | `Evals/0_Injection_Quality_Eval.md` `e034019b8ec450437509a73dd3bae2d303b57561b0f67fcc1e5d19266f663eff` |
| Shared workflow | WORKFLOW contracts as routed by EXECUTION.md (unchanged since the previous review); gsheets route; schema entry `gsheets.sheets_sheets` |
| Schema snapshot | `references/schema/injection.json` `31dcb2b43feca8e5…` (unverified, provisional) |
| ID contracts | `references/schema/id_contracts.json` `fc4711ef07667333…` |
| Lint | `hg_injection_lint.py` `a8226e2a69425355…`, version `injection-lint-v1` |
| Roster / ACL | roster.json `3f2174513f639e37…`, acl.md `e9bca2b35f98d5ef…` (identity checks only) |
| Known data issues | `guidelines/known_data_issues.md` `29b89d856c454124…` (SC-10 is relevant, see §8) |

Input/authority issues: none for this stage. SQL comment lines are evidence of intent only; none addresses a grader or mentions tool calls, pass rate or gates. The new line 31 carries no comment.

## 2. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW, done (saved as input revision 14 before review) |
| Run lint; resolve every flag | NEW, done (0 FAIL, 0 CHECK, 0 INFO) |
| Inventory every statement and affected record | NEW, done: 144 statements (BEGIN, 130 INSERT, 12 UPDATE, COMMIT), ledger §5, line numbers verified against the SQL |
| Check A | NEW for line 31; REUSED for byte-identical rows (§11): PASS |
| Check B | NEW for line 31 and whole-script lint parse; REUSED for byte-identical rows: PASS (provisional snapshot advisory) |
| Check C | NEW for line 31 and every injected record that depends on the investor list's Latest Status column; REUSED for byte-identical rows: PASS |
| Report coverage, findings, limits, one verdict | NEW, done |

## 3. Lint result

`hg_injection_lint.py` on SHA `4895577e…eef9`, universe synthcut, clock 2025-10-01T07:00Z. Base files loaded: contacts, slack users, trello, gmail users, linear, confluence. Rows parsed: 130 INSERT, 12 UPDATE across 17 tables (gsheets.sheets_sheets: 1 insert, 1 update).

Flags: **none** (FAIL 0, CHECK 0, INFO 0). Nothing to resolve. Checks A–C were still run in full.

## 4. Source coverage (new checks in this run)

| Check | Source / pointer | Coverage | Result |
|---|---|---|---|
| UPDATE target `f_48247af79428823c3cac92` | `hg_records.py` gsheets `data.json` `/sheets_spreadsheets`, field `spreadsheet_id` | 356 records, scan complete, 0 errors | 1 match at `/sheets_spreadsheets/96`: "Game Investor List - Harmony Games 2025", created 2025-08-28T01:28:36Z, modified 2025-09-15T19:27:01Z, shared with Leonard, Arthur, Robert, Frederick and others; one sheet, `sheet_id` 0, "Game Investors List 25", 89 grid rows × 28 cols |
| Grid comparison, injected vs base | strict PostgreSQL E-string decode of line 31 → JSON parse → cell-by-cell compare with base `/sheets_spreadsheets/96/sheets/0/grid` | all 89 × 28 cells | 2,491 identical; **1 differs**: row 8 "London Venture Partners", col 13 "Latest Status": base "Pitch/Catch up on 09/07 - waiting to hear back from them if they want to pursue further" → "Pitch/Catch up on 09/09 - waiting to hear back from them if they want to pursue further" |
| E-string escaping | line 31 | whole literal | only `\\` escapes (29), no lone quotes, no `\x`/`\u`/octal escapes; decoded text parses as a JSON list of lists (base shape) |
| LVP meeting date, calendar | gcal `data.json` search "LVP" (case-sensitive) and "London Venture" | scan complete, 0 errors | 4 events (`/events/597`, `/2738`, `/7567`, `/9289`), the same `ical_uid` `2b94e2ad…@hg4` on Robert's, Leonard's, Arthur's and Frederick's calendars: "LVP <> [SOURCE_ORG_0001] Catch Up", 2025-09-09T16:30–17:15Z (Tue Sep 9, 09:30 PT), created 09-06, updated 09-09T15:08:53Z |
| LVP, Slack Sep 2025 | slack `messages/*/2025-09.json` search "LVP" / "London Venture" | scan complete, 0 errors | 8 hits. Relevant: `C096HFA5Z8W/169` (09-13, Leonard: "sent a kick-ass follow-up email to … LVP"); `D04UC0UEN2V/48` (09-25, Leonard: "we got rejection from LVP"); `D04UP3U4MUY/6` (Tue Sep 9 daily agenda). None says Sep 7. |
| LVP, Gmail / Docs | gmail search "London Venture" (complete, 8 newsletter hits); gdocs "London Venture"/"LVP" (complete, 2 + 1 hits) | as stated | gmail "LVP" (case-sensitive) stopped at its 30-hit limit (mostly base64 header noise plus the "re-intros: Are (LVP) <> Leonard" thread `00000999`). No hit contradicts Sep 9. The partial Gmail scan doesn't block this check: the change aligns the sheet with the calendar and doesn't claim that no other source exists |
| Known issue | `guidelines/known_data_issues.md` SC-10 | full entry | "The investor sheet says 'Catch up on 09/07' (a Sunday), but calendar, invite and Slack say Tue Sep 9." Sep 7 2025 = Sunday, Sep 9 2025 = Tuesday (computed) |
| Other SQL dependencies on this sheet | grep of saved SQL for `f_48247af…`, "Game Investor", "09/07", "Latest Status" | whole SQL | Only line 31 targets the sheet. The Q4 doc (line 23) relies on the column: "go only by the Latest Status notes (as of 09/11), which are all from this round". No injected row mentions 09/07 or LVP |
| Reused coverage | previous report §4/§11 (all byte-identical rows) | see §11 | unchanged |

## 5. Operation ledger

Every statement in execution order (line numbers in the current SQL). Line 31 is new and was verified fresh. Every other row is byte-identical to v10 and reuses the v10 ledger (§11). The whole script was re-parsed by the lint in this run.

| SQL line | Table | Op | Record / target | Change vs v10 | Verification | Result |
|---|---|---|---|---|---|---|
| 5 | — | BEGIN | — | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 7 | gdrive.drive_files | INSERT | `f_8d2c47a91e05b3f6d7c418` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 9 | gdrive.drive_files | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 11 | gdrive.drive_files | INSERT | `d_5e8a1c3f9b07d2e64a1b93` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 13 | gdrive.drive_files | INSERT | `f_c61a0e93b7d24f58a2e917` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 15 | gdrive.drive_files | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 17 | gdrive.drive_files | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 20 | gdocs.docs_documents | INSERT | `f_8d2c47a91e05b3f6d7c418` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 22 | gdocs.docs_documents | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 24 | gdocs.docs_documents | INSERT | `f_c61a0e93b7d24f58a2e917` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 27 | gsheets.sheets_spreadsheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 29 | gsheets.sheets_sheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 31 | gsheets.sheets_sheets | UPDATE | `spreadsheet_id = 'f_48247af79428823c3cac92' AND sheet_id = 0` (base "Game Investor List - Harmony Games 2025" / tab "Game Investors List 25", `/sheets_spreadsheets/96`) | ADDED: full grid replace (89×28); exactly one cell differs from base: row 8 London Venture Partners, col 13 Latest Status "Pitch/Catch up on 09/07 …" → "Pitch/Catch up on 09/09 …" | NEW | PASS |
| 33 | gslides.slides_presentations | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 35 | gslides.slides_pages | INSERT | `slide_b4c21ca913ab` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 37 | gslides.slides_page_elements | INSERT | `el_6825f973029b (Harmony Games)` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 39 | gslides.slides_page_elements | INSERT | `el_cffa02683868 (Q4 2025 update (draft))` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 41 | gslides.slides_pages | INSERT | `slide_256dc0474f7c` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 43 | gslides.slides_page_elements | INSERT | `el_72151261faca (Highlights)` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 45 | gslides.slides_page_elements | INSERT | `el_ca7b40076cd7 (Zombie Match 3D alpha numbers )` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 47 | gslides.slides_pages | INSERT | `slide_fd6dbd079420` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 49 | gslides.slides_page_elements | INSERT | `el_90fbf6fd9c1b (Product)` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 51 | gslides.slides_page_elements | INSERT | `el_ef5243814e8f (Boss Arena, Season Pass, 300+ )` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 53 | gslides.slides_pages | INSERT | `slide_bb11abfc5fad` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 55 | gslides.slides_page_elements | INSERT | `el_69587907b898 (Engine)` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 57 | gslides.slides_page_elements | INSERT | `el_6ca8bffe4445 (What shipped in Q3 (Arthur to )` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 59 | gslides.slides_pages | INSERT | `slide_cb3f0884f833` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 61 | gslides.slides_page_elements | INSERT | `el_0c72e8ba6af7 (Team)` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 63 | gslides.slides_page_elements | INSERT | `el_1e212bf4628e (Headcount and contractors (Leo)` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 65 | gslides.slides_pages | INSERT | `slide_a56932e4c738` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 67 | gslides.slides_page_elements | INSERT | `el_5da52b8348b0 (Bridge round)` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 69 | gslides.slides_page_elements | INSERT | `el_4f7f04b6e984 (New investors: welcome, with y)` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 71 | gslides.slides_pages | INSERT | `slide_c9c7eed73bb9` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 73 | gslides.slides_page_elements | INSERT | `el_b45885b83bf9 (Try the game)` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 75 | gslides.slides_page_elements | INSERT | `el_ed13f88ca45b (Firms in talks get the interna)` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 77 | gslides.slides_pages | INSERT | `slide_329b5dfcb888` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 79 | gslides.slides_page_elements | INSERT | `el_09521ac10bd5 (Thank you)` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 82 | slack.slack_messages | INSERT | `4921f321db5d08f936aac24a6a1d2af8` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 84 | slack.slack_messages | INSERT | `7fef94264090696760180223fc8265e7` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 86 | slack.slack_messages | INSERT | `20924cc7f5176991d8a97a8eafb291d0` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 88 | slack.slack_messages | INSERT | `19e1e65d5952f075e8492867c6bcd472` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 90 | slack.slack_messages | INSERT | `800870c56bda852a57dfa06cb4fd63e6` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 92 | slack.slack_messages | INSERT | `1a68c2da0f36fc25489d3d9bbe9ccc32` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 94 | slack.slack_messages | INSERT | `c183280a284440a6ca6cdbb5270c9139` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 96 | slack.slack_messages | INSERT | `398502c0596e5347cc297f61eaefbd50` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 98 | slack.slack_messages | INSERT | `229090ba6b316b667d1a6451b0297a47` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 100 | slack.slack_messages | UPDATE | `id = '99aa913348bb05e6eda8daa06d37fc2a'` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 101 | slack.slack_messages | INSERT | `99b22482ddd77dd01b451afb39014839` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 103 | slack.slack_messages | INSERT | `f7261dd1b05eb2da3b81fe7d8cde2854` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 105 | slack.slack_messages | INSERT | `3cddf83c394676d8b72c0c20ed58f520` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 107 | slack.slack_messages | INSERT | `301ad67f082965686f35a9484aa25b0a` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 110 | trello.trello_actions | INSERT | `68c64270d660c977c4696986` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 112 | trello.trello_cards | UPDATE | `id = '68c5a49e8491a9d7faf869d0'` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 113 | trello.trello_boards | UPDATE | `id = '640643a3fd8f3ca308d9318e'` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 115 | gmail.gmail_threads | INSERT | `frederick.stone/1844623441920000059` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 117 | gmail.gmail_messages | INSERT | `frederick.stone/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@ma` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 119 | gmail.gmail_threads | INSERT | `robert/1844623441920000061` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 121 | gmail.gmail_messages | INSERT | `robert/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 123 | gmail.gmail_threads | INSERT | `leonard.hayes/1844623441920000062` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 125 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 127 | gmail.gmail_threads | INSERT | `frederick.stone/1844724419788800011` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 129 | gmail.gmail_messages | INSERT | `frederick.stone/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@ma` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 131 | gmail.gmail_threads | INSERT | `leonard.hayes/1844724419788800013` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 133 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 135 | gmail.gmail_threads | INSERT | `robert/1844724419788800014` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 137 | gmail.gmail_messages | INSERT | `robert/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 139 | gmail.gmail_threads | INSERT | `arthur.blake/1844724419788800015` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 141 | gmail.gmail_messages | INSERT | `arthur.blake/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 143 | gmail.gmail_threads | INSERT | `leonard.hayes/1844162278195200024` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 145 | gmail.gmail_messages | INSERT | `leonard.hayes/<CACJhvEE55qdWXuKC3BWlscoxBKrLUWavLQ3cpTJ@mail` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 147 | gmail.gmail_threads | INSERT | `frederick.stone/1844354293432320031` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 149 | gmail.gmail_messages | INSERT | `frederick.stone/<CAiKDPIoVSAFUBccUSRRBTi6dsmJdhof2EzteoIx@ma` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 151 | gmail.gmail_threads | INSERT | `frederick.stone/1844610859008000037` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 153 | gmail.gmail_messages | INSERT | `frederick.stone/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@ma` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 155 | gmail.gmail_threads | INSERT | `leonard.hayes/1844610859008000039` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 157 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 159 | gmail.gmail_threads | INSERT | `frederick.stone/1844318935449600041` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 161 | gmail.gmail_messages | INSERT | `frederick.stone/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@ma` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 163 | gmail.gmail_threads | INSERT | `leonard.hayes/1844318935449600043` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 165 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 167 | gmail.gmail_threads | INSERT | `frederick.stone/1844294398771200045` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 169 | gmail.gmail_messages | INSERT | `frederick.stone/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@ma` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 171 | gmail.gmail_threads | INSERT | `leonard.hayes/1844294398771200047` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 173 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 175 | gmail.gmail_threads | INSERT | `robert/1844294398771200048` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 177 | gmail.gmail_messages | INSERT | `robert/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 179 | gmail.gmail_threads | INSERT | `arthur.blake/1844294398771200049` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 181 | gmail.gmail_messages | INSERT | `arthur.blake/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 183 | gmail.gmail_threads | UPDATE | `id = 'frederick.stone@harmonygames.co/1844294398771200045'` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 184 | gmail.gmail_messages | INSERT | `frederick.stone/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@ma` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 186 | gmail.gmail_threads | UPDATE | `id = 'leonard.hayes@harmonygames.co/1844294398771200047'` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 187 | gmail.gmail_messages | INSERT | `leonard.hayes/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 189 | gmail.gmail_threads | UPDATE | `id = 'robert@harmonygames.co/1844294398771200048'` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 190 | gmail.gmail_messages | INSERT | `robert/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 192 | gmail.gmail_threads | UPDATE | `id = 'arthur.blake@harmonygames.co/1844294398771200049'` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 193 | gmail.gmail_messages | INSERT | `arthur.blake/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 195 | gmail.gmail_threads | INSERT | `frederick.stone/1844276782694400053` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 197 | gmail.gmail_messages | INSERT | `frederick.stone/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@ma` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 199 | gmail.gmail_threads | INSERT | `leonard.hayes/1844276782694400055` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 201 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 203 | gmail.gmail_threads | INSERT | `robert/1844276782694400056` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 205 | gmail.gmail_messages | INSERT | `robert/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 207 | gmail.gmail_threads | INSERT | `arthur.blake/1844276782694400057` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 209 | gmail.gmail_messages | INSERT | `arthur.blake/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 211 | gmail.gmail_threads | UPDATE | `id = 'frederick.stone@harmonygames.co/1844276782694400053'` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 212 | gmail.gmail_messages | INSERT | `frederick.stone/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@ma` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 214 | gmail.gmail_threads | UPDATE | `id = 'leonard.hayes@harmonygames.co/1844276782694400055'` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 215 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 217 | gmail.gmail_threads | UPDATE | `id = 'robert@harmonygames.co/1844276782694400056'` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 218 | gmail.gmail_messages | INSERT | `robert/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 220 | gmail.gmail_threads | UPDATE | `id = 'arthur.blake@harmonygames.co/1844276782694400057'` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 221 | gmail.gmail_messages | INSERT | `arthur.blake/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 223 | gmail.gmail_threads | INSERT | `frederick.stone/1843992534712320061` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 225 | gmail.gmail_messages | INSERT | `frederick.stone/<calendar-2b67d1aa-cbdd-d816-22c3-d5ace6cf90` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 227 | gmail.gmail_threads | INSERT | `robert/1843992534712320063` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 229 | gmail.gmail_messages | INSERT | `robert/<calendar-c82c189b-c33c-a6e0-5e43-def7d943af26@google` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 231 | gmail.gmail_threads | INSERT | `arthur.blake/1843992534712320064` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 233 | gmail.gmail_messages | INSERT | `arthur.blake/<calendar-44faeeb8-a4b0-dae2-c4eb-4d2fda67b29b@` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 235 | gmail.gmail_threads | INSERT | `frederick.stone/1843718101401600063` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 237 | gmail.gmail_messages | INSERT | `frederick.stone/<calendar-2d8383e3-21d5-e958-783a-c960b5e984` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 239 | gmail.gmail_threads | INSERT | `robert/1843718101401600065` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 241 | gmail.gmail_messages | INSERT | `robert/<calendar-010d9a7c-8101-ee76-3333-bfb1ce826d3a@google` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 243 | gmail.gmail_threads | INSERT | `arthur.blake/1843718101401600066` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 245 | gmail.gmail_messages | INSERT | `arthur.blake/<calendar-9d6c5aee-50ea-1d96-5cd0-dcef1de61254@` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 247 | gmail.gmail_threads | INSERT | `frederick.stone/1844724105216000067` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 249 | gmail.gmail_messages | INSERT | `frederick.stone/<calendar-297f69c9-ad63-fafd-14c3-70dbf78756` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 252 | gcal.gcal_events | INSERT | `evt_2f86b0d4c9e17a35b64e0d` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 254 | gcal.gcal_events | INSERT | `evt_b511d4619c6f46ee63959b` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 256 | gcal.gcal_events | INSERT | `evt_8bd5e929463b854ec0ad13` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 258 | gcal.gcal_events | INSERT | `evt_ca908a712455521f1f8b43` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 260 | gcal.gcal_events | INSERT | `evt_7d3e19b04a6c25f8e1b9a0` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 262 | gcal.gcal_events | INSERT | `evt_99df25b554cac93e2926fd` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 264 | gcal.gcal_events | INSERT | `evt_671dce00bcb85abb3e355e` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 266 | gcal.gcal_events | INSERT | `evt_d65aa89778c3ebfa5d97b2` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 268 | gcal.gcal_events | INSERT | `evt_9c41e7a2d05b38f6e1a7c4` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 270 | gcal.gcal_events | INSERT | `evt_75d8a0687ea57b663a40b0` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 273 | linear.linear_issues | INSERT | `ZOM-567` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 275 | linear.linear_comments | INSERT | `lc_94eb35d962cfbdd31e1bd496` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 277 | linear.linear_comments | INSERT | `lc_b549f3057640a5eb08f7581e` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 280 | contacts.contacts | INSERT | `e3a91c07d5b48f26a0c7e314` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 282 | contacts.contacts | INSERT | `b72f0d6e19c3a84e5d21f9a0` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 284 | contacts.contacts | INSERT | `5d0e8b31f7a29c64e1b0d3a8` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 286 | contacts.contacts | INSERT | `a4c2e9f07b31d85e6c0f1b29` | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |
| 288 | — | COMMIT | — | unchanged (byte-identical to v10) | REUSED (v10 ledger) + lint whole-script parse NEW | PASS |

## 6. Check A: records, references and IDs

- **UPDATE target resolves.** `gsheets.sheets_sheets` (`spreadsheet_id = 'f_48247af79428823c3cac92'`, `sheet_id = 0`) is base sheet "Game Investors List 25" of spreadsheet "Game Investor List - Harmony Games 2025" (`/sheets_spreadsheets/96`, complete scan of 356 spreadsheets, single match). The predicate covers the full composite key, so it updates exactly one row. That spreadsheet has exactly one sheet, id 0.
- **No new keys.** Line 31 inserts nothing; no collision check applies. No other statement in the SQL touches this spreadsheet.
- **IDs and identity.** No ID-contract fields involved; no accounts, authors or Drive content paths added or changed. The spreadsheet stays readable (grid content present).
- **Byte-identical rows.** References, collisions, Drive readability and one-account-per-person reused from the v10 review (§11): PASS.

## 7. Check B: SQL structure and supported schema rules

- Single BEGIN/COMMIT block; 144 statements; the new UPDATE has one `SET` assignment and a primary-key predicate, and is terminated correctly (lint parse and independent regex/decode).
- `grid_json` is `text` (nullable) in the snapshot; the value is a valid E-string that decodes to a JSON list of lists with 89 rows × 28 columns, the same shape and dimensions as the base grid and the existing `sheets_sheets` INSERT at line 29. Lint `json_shape`: clean. `row_count`/`column_count` aren't touched; base values (1003 / 28) still fit the grid.
- No generated column, Linear text-date or NOT NULL concern applies to this statement.
- **Provisional snapshot comparison:** `gsheets.sheets_sheets` columns `spreadsheet_id`, `sheet_id`, `grid_json`: MATCH. The four uncovered columns from earlier rows are unchanged (Advisory 1).

## 8. Check C: dates, relationships and consistency

- **The edit removes a pre-existing base disagreement and adds none.** Base sheet row 8 says "Pitch/Catch up on 09/07" (a Sunday). The base calendar has the "LVP <> … Catch Up" on Tue 2025-09-09 16:30–17:15Z on all four founders' calendars, with the same `ical_uid`. The Sep 9 agenda DM and Leonard's Sep 13 "follow-up email to … LVP" fit that date. The new value, 09/09, agrees with those records. This is known data issue **SC-10**. The sheet is a gsheets record, which injection can change (unlike Snowflake and Confluence), so aligning it is a legitimate fix rather than an attempt to "correct" an uneditable base source.
- **Timing.** The UPDATE changes current content only; it asserts no new event timestamp. The spreadsheet's base `modified_time` (2025-09-15T19:27:01Z) falls after 09/09 and before the clock, so a sheet that read "09/09" as of its last edit is consistent. No timestamp needs to move.
- **Injected records that depend on the column.** The Q4 send-list doc (line 23) says the Latest Status notes are "as of 09/11" and "all from this round" (since the Sep 3 kickoff). The LVP note at 09/09 still falls in that window, so the previous review's finding still holds. After the edit, the 23 non-empty notes carry dates 09/09 (LVP), 09/11 (11 "as of 09/11" / T-accelerate), "before 09/12" (Transcend, Acterra) and NCsoft's scheduled "follow-up … on 09/15" (a plan date, unchanged by this edit), or describe Sep 2025 answers. Nothing else in the SQL cites LVP or 09/07.
- **Stale context unchanged.** The note still says "waiting to hear back". Base Slack (`D04UC0UEN2V/48`, 2025-09-25) later reports "we got rejection from LVP". That staleness is in the base, predates this edit (the sheet was last modified 09-15) and is supported historical context. The injection neither creates nor worsens it. Whether the task's rules turn on LVP's status is for `/prompt`.
- **Grader-facing text.** None; the only changed text is the date inside an existing note.
- **Byte-identical rows.** Clock, chronology and base agreement reused from the v10 review (§11): all event timestamps at or before 2025-10-01T07:00Z (latest 2025-09-30T23:48Z); only Oct 6 gcal start/end are later, as plan fields.

## 9. Findings

No demonstrated defects. Remaining advisory (doesn't block this stage):

1. **Columns not in the schema snapshot (Check B, provisional, unchanged from v10).** `slides_pages.notes` (all NULL), `slides_page_elements.table_json` (all NULL) and `.ordinal`, and `linear_comments.sequence` appear in neither the snapshot nor the base exports. If a platform table lacks any of them, that INSERT fails and BEGIN/COMMIT rolls back the whole script. No task content depends on them. Smallest fix: drop those four columns and their values, or confirm the script loads on the platform.

Note for later stages (not an injection finding): with this UPDATE the LVP date is no longer a base conflict *in the agent's view*, but SC-10 remains on the known-issues list, and the late-September rejection still conflicts with the sheet's "waiting to hear back". `/prompt` and `/rubric` decide whether any graded item depends on LVP.

## 10. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | The new UPDATE's composite-key target resolves to one base sheet (complete scan). No new keys. Byte-identical rows reuse v10's PASS (references, collisions, ID contracts, readable Drive files, one account per person). |
| B — SQL structure and supported schema rules | PASS | Valid E-string; decoded `grid_json` is a JSON list of lists matching the base shape and size; full-key predicate. Four columns the snapshot doesn't cover are advisory. Not live-certified. |
| C — Dates, relationships and consistency | PASS | One cell changed, 09/07 → 09/09. That matches the base calendar (Tue Sep 9, four copies) and the Slack records, and resolves SC-10 in the sheet. It stays consistent with the Q4 doc's "as of 09/11 … all from this round" and the sheet's 09-15 modified time. No new timestamps; no grader-facing text. |

Outside certification scope (disclosed, not gates): live execution and current database compatibility (including the four columns), search ranking, Agent visibility and persona access, task difficulty.

## 11. Stage ownership and reuse

Reused evidence (stage-evidence-v1), from `Evals/task_inputs/reports/0_injection.md` as it stood before this rerun, SHA-256 `c2750b9fd4060e2c03b755832f63c4608a7bd4344aee6db5cfeb117e82070e4b` (injection-static-v2, PASS/COMPLETE, SQL `efe3cab1…c881`), which itself reused the v9 review for rows unchanged then:

| Item | Source ledger / check | Dependencies verified unchanged |
|---|---|---|
| Checks A–C results for all 143 statements other than line 31 (ids/collisions, membership/identity, structure, JSON shapes, chronology, base agreement, Trello/Gmail/Calendar/Slides/Docs relationships) | previous §4–§8, §11 | `diff` v10 → v11 shows only the line 3 comment and added line 31; universe manifest `da2f4cf0…aac1a`; Eval 0 `e034019b…`; schema snapshot `31dcb2b4…`; id_contracts `fc4711ef…`; lint `a8226e2a…`; roster `3f217451…`; acl `e9bca2b3…`; clock 2025-10-01T07:00Z (all equal to the previous report) |
| Q4 doc's Latest Status range claim | previous §8 | re-examined fresh here against the changed cell (§8) |

`/prompt` may reuse these static checks only while all of these hold: SQL SHA-256 `4895577edea84edb71253b2c53e41f0eb638fbbc2d60f04927fc0c84c5c6eef9`, universe manifest `da2f4cf0…aac1a`, schema snapshot `31dcb2b4…`, id_contracts `fc4711ef…`, Eval 0 `e034019b…`, clock 2025-10-01T07:00Z. `/prompt` still owns discoverability and persona access. This SQL changed, so earlier /prompt, /hardness, /oe and /rubric results are outdated; run /prompt, /hardness, /oe and /rubric again in that order.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness (with a fresh run on this SQL), /oe and /rubric. Optionally drop the four snapshot-uncovered columns (Advisory 1) first; that makes a new SQL version that needs /injection again.

Evidence limits: Static review only. Live load, current database compatibility (including the four snapshot-uncovered columns), Agent visibility and difficulty are outside scope. The Gmail "LVP" text search stopped at its hit limit (header noise). That isn't a required check here, since the edit aligns the sheet with the calendar.
