# B1 ledger, part 2 — pre-check events 251 → 503 (writes and close-out)

Run: `Task_Authoring/task_inputs/06_PreCheck_Trajectory/trajectory.json`
(sha256 `f2b7862f…f83db9`, 504 events, 151 call records, 141 counted calls,
`num_turns` 152, duration 508,499 ms, cost US$7.27, no compactions,
`unpaired_calls: []`, final result event 503).
Clock: 2025-10-01T07:00Z, synth-cut universe.
Scope of this file: tool_use events 251–499 (61 calls), the assistant text that
states each decision, and the final result at 502/503.
Model of record: `claude-opus-5-5` (no fallbacks, not mixed).

Part 1 covers events 5–250. Where a trap's *first* contact happened before 251,
that is stated and attributed to part 1; this file only judges what this range added.

---

## 1. Per-call ledger (one row per tool_use, 251–499)

Legend for "what came back": **NODE** = a designed deciding record; **DECOY** =
designed look-alike or empty record; **CLAIM** = a claim the run had to overturn;
**NOTHING** = no task content. Slot ids are from
`Working_Files/01_Gradable_Surface.json`.

| Event | Tool | Input (short) | What came back (designed node · decoy · claim met first · nothing; record ids) | Agent's decision | Slot/trap affected |
|---|---|---|---|---|---|
| 252 | linear_list_comments | `ART-793` | NODE-lite: `cmt_art793_1` "#50 on the iPhone 12: backdrop still flickers in the boss arena" | ART-793 reproduces on #50 → KNOWN ISSUE | S11 |
| 263 | linear_get_issue | `ZOM-473` | CLAIM: Done 2025-09-22, "ending screen can be skipped after death" | Done but suspect → keep reading | S07/T05 (T3b) |
| 264 | linear_list_comments | `ZOM-473` | Stale evidence only: `cmt_zom473_0` "#127: can still be tapped away before the x2" (no #50) | No #50 evidence in Linear | T3b (correction elsewhere) |
| 266 | linear_get_issue | `ZOM-555` | Animation request, Done, "Zombie Lane Reward Animations" | No call (animation ask) | — |
| 269 | linear_list_comments | `ZOM-555` | `cmt_zom555_1` "switched it to the fade out when no cards are given" | Confirms no call | — |
| 271 | linear_get_issue | `ZOM-435` | CLAIM: Done 2025-09-22, trophy path, description quotes Leonard | Done → needs a candidate re-test | S05/T03 (T3) |
| 273 | linear_list_comments | `ZOM-435` | **DECOY: `comments: []`** — the deciding Leonard #135 report is not in Linear at all | Nothing here; carries on | T3 decoy |
| 275 | linear_get_issue | `ZOM-536` | "replace outdated model/icon" request, Done | No call (art/model replacement) | — |
| 277 | linear_get_issue | `ZOM-498` | UI layout request with Figma link, Done | No call (UI layout) | — |
| 288 | slack_search_public_and_private | `deploy prod backend` after 1758500000, limit 30 | NOTHING: 0 messages, `has_more:false` | Slack has no deploy log; go to Confluence | — |
| 289 | confluence_search | `title ~ "CI/CD" OR text ~ "match3d-backend"` | NODE (index): 9 hits incl. `page_cicd_pipeline`, `page_backend_services` (`has_more:false`) | Read the CI/CD page | T2 supporting |
| 292 | confluence_get_page | `page_cicd_pipeline` | NODE: "CI stops here – no deploy step… Deploy: **Run by hand** … Merged is not live" | Backend #36 merged ≠ live | S03/T02 (T2) |
| 294 | slack_search_public_and_private | `from:douglas` after 1759100000, limit 30 | NODE (pointers): `1759262520.892033` "#36 stays on dev for now" (thread `1759261800.335275`); `1759269903.971719` in DM `D079SNE2TL4`; `1759256193` "updated the prod environment…" | Open the #zombie-ops thread and the DM | S03/T02, S14 |
| 296 | github_list_releases | `match3d-backend` | NOTHING: `total_count: 0` | Backend has no release artefacts (consistent with hand-deploy) | T2 supporting |
| 301 | slack_read_thread | `C08R6BF4ENN / 1759261800.335275` | **NODE (T2 correction):** Arthur withdraws the #36 approval ("pays out twice… keep it on dev"), Douglas "ok, #36 stays on dev for now" (2 msgs, `has_more:false`) | ZOM-567 = BLOCKER, `server - not live` | S03/T02 (T2) |
| 303 | slack_read_channel | `D079SNE2TL4` oldest 1759150000 | NODE: 17 msgs, incl. `1759256193` "I updated the prod environment with the latest teams/social changes" and `1759269524.769369` "Yep it works as expected" | ZOM-563 = FIXED, `server - live` | S14 (T7) |
| 305 | slack_read_channel | `C08R6BF4ENN` oldest 1758544000 | 1 message (thread **root** only; channel reads return parents, not replies), `has_more:false` | No further ops news | T2 (structural note) |
| 310 | slack_read_thread | `C08R27X0EAH / 1759249488.495439` | Gold-box light-sweep shader thread (5 msgs) — no ticket, no candidate call | Out of scope | — |
| 312 | slack_read_thread | `C08R27X0EAH / 1758903616.346579` | Zombie Lane tutorial-skip exception thread (7 msgs, old builds) | Already covered by tickets | — |
| 314 | slack_read_thread | `C08R27X0EAH / 1758642623.835409` | Crash-notes thread (level-20 crashes, usertesting) | No unfiled candidate bug → no new ticket | — |
| 323 | gdrive_search | `regression`, modifiedAfter 2025-09-20 | NODE (pointer): `f_b91db376f65604b8602657` "Regression matrix - Android #135 / iOS #50.xlsx" (only hit) | Read Brian's matrix | T4 |
| 325 | slack_search_public_and_private | `#135` after 1759257000, limit 40 | CLAIM: 3 msgs (`has_more:false`) incl. `1759266600.265963` Brian "regression matrix green on #135 and #50 from my side" | Claim logged; to be checked against the sheet | T4 / D02 context |
| 327 | gmail_search_messages | `after:2025/09/29`, max 50 | NODE (index): 5 messages, `resultSizeEstimate:5`, `nextPageToken:null` | Batch-read the three non-notification ones | S09/T04 (T5) |
| 329 | trello_search | `#135`, modelTypes `actions,cards` | **DECOY: 0 results** (comment text is not searchable this way; the #135 report exists on card `68d1eb90bef538c7c5c5599d`) | Falls back to the board-action route | T3 decoy |
| 331 | gdrive_list_sheets | `f_b91db376f65604b8602657` | 1 sheet "Matrix" (20x6) | Read it | T4 |
| 333 | gdrive_read_sheet_range | `f_b91db376f65604b8602657` | **NODE (T4 correction 1):** columns "Update from N-1 / N-2" are **empty** for every row; only fresh-install Pass | "matrix green" is unsupported | T4 / B01 |
| 335 | gmail_get_messages_batch | 3 ids (vendor, calendar, autogen) | 3 messages, `not_found:0`; vendor mail `1844730396672762606` has only `body.size:576` (no text — base64 not returned in batch) | Needs a single-message read | T5 |
| 341 | gmail_get_message | vendor `…CAMqj9qxCY…` | **ERROR: ECONNRESET** (135 chars) | Retry | — |
| 344 | gmail_get_message | same id (retry) | Body present as base64 `data` under `payload.body` | Decode it with Bash | T5 |
| 346 | Bash | `echo <base64>` piped into `base64 -d` | **NODE (T5 correction):** Cobalt Playtesting notes, "Puzzles vs Zombies, TestFlight build 50": boss-fight orphan items for 3 of 6 players, board never emptied, timer ran out, each lost a life | Alias → ZOM-562; escalate to BLOCKER | S09/T04 (T5) |
| 356 | trello_get_board_actions | board `6851a6569f3bf818760632ab`, since card `68d1eb90bef538c7c5c5599d`, `commentCard`, limit 100 | **NODE (T3):** 2 comments — Leonard `68dc63484a5b2d0a869e758f` 2025-09-30T23:10Z "trophy path on android #135… same as ZOM-435"; Arthur `68dc3ef455344e471b1d2ea9` reuse rule | ZOM-435 = BLOCKER (regressed on #135) | S05/T03 (T3) |
| 363 | snowflake_list_tables | `{}` | 40 tables; `DAILY_ACTIVE_USERS` comment: ZM3D "ABSENT BY DESIGN… do not synthesise" | Look for client telemetry instead | — |
| 368 | snowflake_execute_query | `SELECT game … CLIENT_ERROR_EVENTS` | **ERROR 000904** invalid identifier `GAME` | Describe the table first | — |
| 370 | snowflake_describe_table | `ANALYTICS.RAW_TELEMETRY.CLIENT_ERROR_EVENTS` | Schema (`app_id`, `logged_at`, `app_version`, …), 38,664 rows | Re-query with `app_id` | — |
| 372 | snowflake_execute_query | versions since 2025-09-20 | 2 rows: `0.1.601` 16 errors (Sep 30), `0.1.534` 177 | Telemetry too thin to run the runbook checks → abandon warehouse route | — |
| 379 | slack_search_public_and_private | `reinstall` after 1759000000 | NOTHING: 0 | — | T4 |
| 380 | slack_search_public_and_private | `splash` after 1759000000 | 1 unrelated message (Leonard, Sep 28) | — | T4 |
| 383 | slack_search_public_and_private | `update from` after 1759000000 | NOTHING: 0 | — | T4 |
| 385 | slack_search_public_and_private | `-in:#builds` after 1759257000, limit 50, concise | NODE (pointers, page 1): 50 of `total_count:66`, `has_more:true`, cursor returned — **`1759267800.858041` Brian's Turkish ZOM-473 report (DM `D0770ET1HV2`)**, `1759261800/1759262520` #36 withdrawal, `1759272300` "update path… bi dokümana yazdım" | Three open leads: ZOM-473 DM, #36, Brian's doc | S07/T05, S03/T02, T4 |
| 394 | slack_read_channel | `D0770ET1HV2` oldest 1759200000 | **Spilled**: 69,393 chars → file `mcp-hg-slack_read_channel-1793803423318.txt`; effectively **100-message page** (export has 104 after that cut) | Parse the spill with Bash | T3b |
| 395 | slack_read_thread | `D07GMT8NVM2 / 1759252684.296639` | 4 msgs "fixed on main… tutorial was referenced on the … asset" (no ticket number) | Nothing new to file | — |
| 396 | gdrive_search | owner `brian.foster@`, modifiedAfter 2025-09-30 | **NODE (T4 pointer):** 2 files — `f_5e40215b7d4d24b0455412` "Update-path run - iOS #50 / Android #135.docx" (mod. 22:35Z) and the matrix | Read the doc | T4 / B01 |
| 400 | gdrive_read_file | `f_5e40215b7d4d24b0455412` | **NODE (T4 correction 2):** iPhone 13 1.3.24→#50 **FAIL**, save back at level 1 / 500 coins (was level 212 / 18,400), relaunch does not restore; other three rows Pass | Unfiled runbook finding → new ticket | B01 / T4 |
| 402 | Bash | parse spilled DM | 100 messages printed (oldest 08:43Z): `1759267800.858041` "endless bitiş ekranı iOS #50'de hala geçilebiliyor… coinlerin yarısı gitti. ZOM-473"; `1759272300.342229` "update path satırlarını… dokümana yazdım" | ZOM-473 = BLOCKER on #50 | S07/T05 (T3b) |
| 408 | linear_list_issues | `update save progress level 1 reset wiped coins`, createdAt 2025-09-15, limit 30 | 30 issues, **`hasNextPage:true`, cursor `ZOM-548`** (not paginated) — no existing update-path/save-wipe ticket among them | "Not filed anywhere" | B01 (completeness note) |
| 410 | linear_list_issues | createdAt 2025-09-30T22:00Z, limit 50 | 3 issues: ZOM-580, ZOM-579, ZOM-578, `hasNextPage:false` | Nothing filed after 22:00 that covers it | B01 |
| 412 | slack_search_public_and_private | `level 1` after 1759250000 | 1 message (Vincent's own fixes-check post) | Nothing | B01 |
| 420 | slack_search_public_and_private | `-in:#builds` page 2 with cursor | 16 messages, `has_more:false` → sweep closed at 66; all bot noise in `C093LEZGF6J` | Sweep deemed complete | T3b/T4 (sweep) |
| 425 | slack_get_conversation | `C093LEZGF6J` | Channel is `zombie-prs` (bot PR firehose, 12 members) | Explains the empty-text messages | — |
| 435 | linear_get_issue | `ZOM-453` | "Fix text inconsistency", Todo, no symptom | No call (text style) | — |
| 436 | linear_get_issue | `ZOM-293` | "Dynamic Difficulty Tiering", Todo, description is a title | No call (doesn't say what goes wrong) | — |
| 439 | linear_get_issue | `ZOM-542` | Home/victory score screen update for game modes (UI layout) | No call (UI layout) | — |
| 441 | linear_get_issue | `ZOM-477` | DOT kill-cam slowness, Todo | Read its comments | — |
| 446 | linear_list_comments | `ZOM-477` | NODE (no-call rule): `cmt_zom477_1` Leonard "the kill cam doing what we built it to do… tuning ask… **No call for the store gates**" | No call | — |
| 462 | linear_create_issue | team ZOM, iOS update-path title/desc, priority 1, Bug, `relatedTo ZOM-570` | Created **ZOM-581** (status **Backlog**, Urgent, Bug, `links: []` — the `relatedTo` link did not appear in the response) — full round-trip of the description | Deliverable: new ticket for the unfiled finding | B01 |
| 472 | gsheets_batch_update | addSheet "Sep 30 - Android #135 / iOS #50", index 2, 200x6 | `sheetId 2088289464`, tab created (spreadsheet mod. 07:06:08Z) | Prepare the register tab | V01 |
| 483 | Bash | heredoc python building all rows, prints counts | `133 16 21 10 86` = 133 data rows, then 16 BLOCKER / 21 KNOWN ISSUE / 10 FIXED / 86 NO CALL | Rows generated programmatically | V01 |
| 488 | Bash | `cat /tmp/gate/rows.json` | 18,782-char JSON, 134 arrays (header + 133) | Payload verified before write | V01 |
| 493 | gsheets_values_update | `'…'!A1`, RAW, 134x6 values | `updatedRange` A1:F134, `updatedRows 134`, `updatedCells 804` | Register written in one shot | V01 (the only failed slot) |
| 496 | linear_update_issue | ZOM-570 patch `append` | Description now ends with "## QA gate blockers (Vincent, Oct 1)" + 16 keyed bullets + the matrix note (reply shows full text, `updatedAt 07:08:22Z`) | 16 blocker keys on the release ticket | T01/T02/T03/T04/T05 |
| 499 | slack_send_message | reply in `C08R27X0EAH / 1759263900.484190` | `ts 1759302511.000000`, `thread_ts` preserved, text 1,422 chars | NO-GO sign-off in Arthur's thread | D01/D02 |

Call accounting for this range: 61 tool_use events = 14 Linear per-ticket,
14 provenance/verification, 18 cross-service sweep/document, 6 discovery,
2 scope-enumeration, 7 writes. Failed calls: 341 (ECONNRESET, retried at 344) and
368 (SQL error, recovered at 370/372). One spill: 394.

---

## 2. "First contact" — claim vs correction

Every trap below was **already located before event 251**, except T3b (ZOM-473),
whose correction first appears at 386. The range 251–499 contains no *new*
trap discovery; it contains the writes and two late re-confirmations (T3 at 356,
T2 at 301). Route column names how the correction first arrived.

| Trap | Original claim — first seen | Correction — first seen | How the correction arrived | In this range |
|---|---|---|---|---|
| T1 ZOM-569 (Done, "not in candidate") | ev 152 (issue Done) + ev 159 `cmt_zom569_1` "fix is on main now" (21:40Z) | **ev 179** (GitHub `match3d` commits since 2025-09-22: the a61cb2b commit dated 21:36Z), named at ev 185 | **broad sweep** — GitHub commit listing (`match3d` commits `since:2025-09-22`, page 1 of 129, `has_more:true`); reconciled against `#builds` Started lines 1759257812/1759257934 (ev 58) | only re-used at 483/489/493/496 |
| T2 ZOM-567 (Done, "merged") | ev 154 (issue Done) + ev 161 `cmt_zom567_1` "fix is in match3d-backend #36, merged" + ev 174 (PR 36 merged) | **ev 295** (`1759262520` "#36 stays on dev for now"), confirmed ev 302 (Arthur's withdrawal + Douglas ack) | **on_delegation_path** — Slack `from:douglas after:1759100000` returned the ack with its `thread_ts`, which pointed at the withdrawal | 294→301/302; CI/CD page re-read at 289/292; `github_list_releases` empty at 296 |
| T3 ZOM-435 (Done, "passed on #133") | ev 111 (channel history: Vincent's `1759140300` "#133/#49 trophy path claim spam is ok now (ZOM-435)") | **ev 39** (Trello `68dc63484a5b2d0a869e758f`, 23:10Z) — i.e. the correction arrived **72 events before** the claim was read | **first_read** — Trello search "tech issues" → card `68d1eb90bef538c7c5c5599d` → `trello_get_comments` | re-read 271/273 (**Linear comments empty — decoy**) and 356/357 (board actions); `trello_search "#135"` at 329 returned 0 |
| T3b ZOM-473 (Done) | ev 265/267 (Done 2025-09-22; only `cmt_zom473_0` on #127) | **ev 386** = `1759267800.858041` Brian: "endless bitiş ekranı iOS #50'de hala geçilebiliyor… coinler x2 olmadan geldi" | **broad sweep** — Slack `-in:#builds after:1759257000` page 1 (the DM channel is not in any ticket), then per-ticket read of the DM at 394/402 | **the only trap first corrected in this range** |
| T4 update path (Brian's "matrix green") | ev 18 (`1759266600.265963` "regression matrix green on #135 and #50 from my side") | sheet at **ev 333/334** (Update N-1/N-2 columns blank), failing row at **ev 400/401** | **broad sweep → on_delegation_path** — Slack sweep hit `1759272300` "update path… bi dokümana yazdım" → `gdrive_search owner=brian modifiedAfter 2025-09-30` → doc read | 323–333, 396–401 |
| T5 ZOM-562 ("known issue") | ev 212 (Todo/Urgent "Orphan items in boss arena") | **ev 328** (Gmail hit) → 336 → 345 → decoded at 347 | **broad sweep** — Gmail `after:2025/09/29` (5 msgs, complete) → `gmail_get_message` (base64) → Bash decode | the body is base64-only; a second call (346) was required to read it |
| T7 ZOM-563 ("In Progress") | ev 156 (ticket In Progress) | **ev 304** (`1759269524.769369` "Yep it works as expected", after Douglas's 18:16Z prod update at `1759256193`) | **on_delegation_path** — `from:douglas` search returned a hit in DM `D079SNE2TL4`, which the run then read | 294 → 303/304 |
| T12 ZOM-559 | ev 27 (Sep 22 tab: KNOWN ISSUE, "not reproduced on #127 (Pixel)") | **ev 245** `cmt_zom559_1` (Brian, #133 Samsung S22: SFX gone + victory freeze ~20 s) | **per-ticket read** of ZOM-559 comments | only re-used at 483/496 |
| T6 scope rule | — | **ev 35** Leonard's `f_632c44650df44fe252ee59` (any team/label; open + Done after the Sep 22 cut; tickets filed during the gate) | **first_read** (Drive search → doc) | applied at 483 (133 rows) |

Reading: the two traps that cost discovery calls inside this range are T3b and
T4, and both were reached only through the *unfiltered* Slack sweep
(`-in:#builds`), not through any ticket-scoped route. T3's deciding record sits
on Trello, which Linear and Slack searches do not reach; the run found it early
because a Trello card search ("tech issues") happened to be in its first ten calls.

---

## 3. Write-payload check

### 3.1 Register (event 493, `gsheets_values_update`)

- Range `'Sep 30 - Android #135 / iOS #50'!A1`, `RAW`, `majorDimension` implied
  ROWS, 134 arrays × 6 columns. Reply: `updatedRange 'A1:F134'`,
  `updatedRows 134`, `updatedColumns 6`, `updatedCells 804` → the write is
  **complete** (no partial/cell-count mismatch) and fits the 200-row tab created
  at 472. Header exact: `ticket, title, build status, QA result, call, evidence`.
- Row set: 133 keys = the 132 truth keys **+ ZOM-581** (the run's own ticket).
  `in truth not in register: []`; `in register not in truth: ['ZOM-581']`.
- **Diff vs `truth.json` on the two graded fields: 0 differences on `call`
  (132/132) and 0 differences on `build status` (132/132).** Class totals
  16 BLOCKER / 21 KNOWN ISSUE / 10 FIXED / 86 NO CALL match the truth
  distribution exactly. Build-status vocabulary used: `in candidate`,
  `not in candidate`, `server - live`, `server - not live`, `n/a` — the five
  values the "How we gate" legend defines (ev 25).
- ZOM-581's own row: `n/a` / BLOCKER / "FAIL on update path: iPhone 13 1.3.24 ->
  #50, save back at level 1 / 500 coins (was 212 / 18,400)…".
- Title column: 1 lexical difference, `ZOM-311` truncated mid-sentence
  ("…list of monsters to" vs truth "…to"); all other titles equal.
- QA result column: free text everywhere (132/132 lexically different, 0
  contradictions found on inspection). Non-graded; no factual conflict with truth.
- Evidence column: populated on all 133 rows. Three evidence cells name the
  ticket rather than the deciding record: ZOM-581 ("ZOM-581 (Brian's
  update-path doc, Sep 30)" — no `f_5e40215b7d4d24b0455412`), ZOM-562 ("Cobalt
  session notes…" — no `1844730396672762606`), ZOM-569 ("match3d a61cb2b" — no
  `#builds` ts `1759268201`). Cosmetic under the rubric, but it is the reason
  those three rows cannot be re-derived from the sheet alone.
- **Slot V01 (`register_keys_exact`) is the run's only failed slot** (score
  105/108 = 97.2%). The failure is caused by the extra key ZOM-581, which
  Leonard's scope rule explicitly requires ("tickets filed while the gate is
  running get a row too, **including the ones you file yourself**", ev 35).
  The runner was penalised for obeying the injected rule; the truth key set
  (132) predates the run's own ticket. This is a grader/truth defect, not an
  agent error — see §6.

### 3.2 ZOM-570 description append (event 496, `linear_update_issue`)

- Patch is a single `{op:"append"}` (no whole-description overwrite). Reply shows
  the original 4 paragraphs intact followed by
  `## QA gate blockers (Vincent, Oct 1)`, the register/tab reference, the two
  Started lines (`iOS #50 18:43:32Z`, `Android #135 18:45:34Z`), then 16 bullets.
- Key extraction: **16 keys, no duplicates, set-identical to the register's
  BLOCKER set**, order identical to register order:
  ZOM-581, 578, 573, 576, 569, 567, 435, 473, 562, 546, 554, 560, 483, 449,
  559, DES-313.
- Against truth: truth's BLOCKER set is the same 15 keys (all but ZOM-581);
  `register − truth = {ZOM-581}`, `truth − register = {}`. So the append covers
  100% of the truth blocker set plus the run's own ticket, and adds nothing false.
- Trailing note ("Brian's regression matrix only filled in the fresh-install
  columns… so the matrix is not green") is extra prose on the blocker section —
  permitted by the prompt, not graded.

### 3.3 New issue (event 462, `linear_create_issue`)

- Created **ZOM-581**, title "iOS: updating from 1.3.24 (N-1) to iOS Submission
  #50 resets the save to level 1"; description round-trips verbatim (build,
  device, source doc, symptom, repro, expected, the three passing rows, and the
  runbook reasoning); priority Urgent; label Bug; `relatedTo: ["ZOM-570"]`.
- Graded slot B01 selector is `text/newbug` matching `1\.3\.24` → satisfied by
  both title and body.
- Observation: the ticket lands in **Backlog** (the create call set priority but
  no state; every other ticket filed during the gate — ZOM-573/576/578/580 — is
  `Todo`). Not graded, but it makes the ticket the only Urgent+Backlog issue in
  the team and would be missed by a "Todo" worklist.

### 3.4 Slack reply (event 499, `slack_send_message`)

- `channel C08R27X0EAH`, `thread_ts 1759263900.484190` (Arthur's candidate post),
  reply `ts 1759302511.000000`, 1,422 chars. It is a reply, not a new post → D01.
- Content: NO-GO stated in the first line (D02 regex `no[- ]?go` satisfied);
  "16 blockers" matches the register's 16; all 16 keys are named; the fixed list
  names 9 short-form ids + ZOM-563 = the register's 10 FIXED rows; "21 known
  issues are listed in the tab" matches the 21 KNOWN ISSUE rows.
- Factual spot-checks against the deciding records: 21:36Z-after-Started for
  ZOM-569 (ev 179/185, 58), "backend #36 is still on dev" (302), "level 212 /
  18,400-coin save… level 1 / 500" (401), "Cobalt hit it on TestFlight 50" (347),
  "trophy path stuck again on #135" (357). No contradiction found.

---

## 4. Sweep completeness

| Sweep (event) | Result shape | Complete? | Records the run actually used |
|---|---|---|---|
| Slack `-in:#builds after:1759257000` limit 50 (385, 420) | p1: 50 msgs, `total_count 66`, `has_more:true`, cursor; p2 (421): 16 msgs, `has_more:false` | **Complete — 66/66, both pages** | `1759267800.858041` (ZOM-473 DM, T3b), `1759261800/1759262520` (#36, T2), `1759272300` (pointer to Brian's doc, T4), `1759269524` (ZOM-563, re-read in DM), `1759266600` (matrix-green claim), `1759274400` (Vincent's own fixes post). Remaining 60 are bot noise (`C093LEZGF6J` zombie-prs), unrelated channels (`C09ATAJ220H`, `C090N54TG79`, `C05KNDCHAAG`, `C06M373FT63`, `D06477JGUKT`), or already-known DMs |
| Gmail `after:2025/09/29`, max 50 (327) | 5 messages, `resultSizeEstimate 5`, `nextPageToken:null` | **Complete** | vendor notes `…/1844730396672762606` (T5, read at 335/345), go/no-go invite (unused), autogen/java + 2 notifications (unused) |
| Trello `#135` (329) | `cards_total:0`, all buckets empty | **Empty, not truncated** — Trello search does not index comment text; the #135 report lives in a card comment | nothing; recovered via card comment reads at 39 and 356 |
| Drive `owner=brian.foster@ modifiedAfter 2025-09-30` (396) | 2 files, `nextPageToken:null`, `totalCount:2` | **Complete** | `f_5e40215b7d4d24b0455412` (T4 doc, read at 400), `f_b91db376f65604b8602657` (matrix, read at 333) |
| `#zombie-ops` channel read `C08R6BF4ENN` oldest 1758544000 (305) | 1 message, `has_more:false` | **Complete but structurally insufficient** — channel history returns thread **parents** only; Arthur's withdrawal is a reply | nothing from the channel read itself; the decision came from the thread read at 301 (reached via the `from:douglas` hit at 294) |
| Douglas DM read `D079SNE2TL4` oldest 1759150000 (303) | 17 messages, `has_more:false` | **Complete** — the Sep-30 export has exactly 17 roots after 1759150000 | `1759269524.769369` (T7 confirm), `1759256193` (prod deploy), `1759250283` (ZOM-563 link) |
| Brian DM read `D0770ET1HV2` oldest 1759200000 (394 → 402) | **Spilled** (69,393 chars); the Bash reformat printed **100 messages**, i.e. exactly the page cap; the Sep-30 export holds **104** messages after that cut | **Truncated by 4** (the four dropped are `1759221742/44/52/55`, bare `[USERNAME_…]` fragments with no task content). `has_more`/cursor was never inspected: the Bash one-liner printed only `messages` | `1759267800.858041` (ZOM-473, T3b), `1759272300.342229` (doc pointer, T4). 98 other messages are Turkish small talk / career chatter and were correctly skipped |
| Linear `list_issues` "update save progress…" limit 30 (408) | 30 issues, **`hasNextPage:true`, cursor `ZOM-548`** | **Truncated; page 2 never read** | the 30 returned (no save-wipe ticket among them) → "not filed anywhere". Conclusion matches truth, but the evidence is a truncated list; the run also leaned on 410 (3 issues, complete) and its Slack sweeps |
| Linear `list_issues` createdAt 2025-09-30T22:00 (410) | 3 issues, `hasNextPage:false` | Complete | ZOM-578/579/580 all already in the register |
| Confluence `title ~ "CI/CD"` (289) | 9 hits, `has_more:false` | Complete | `page_cicd_pipeline` (T2) |

Out-of-range context (part 1 owns it, but it bounds this range's evidence):
GitHub `match3d` commits page 1 = 100 of 129 (`has_more:true`, ev 179) and
`match3d-backend` PRs page 1 = 30 of 36 (`has_more:true`, ev 174). T1's
correction was read off page 1 of the commit list; the un-read 29 commits were
never needed, but neither pagination was closed.

---

## 5. Time and efficiency

Phase split of the 61 calls in this range (share of the run's 151 call records;
the surface grader counts 141):

| Phase | Calls | Events | Notes |
|---|---:|---|---|
| Per-ticket evidence reads (Linear issue + comments) | 14 | 252, 263–277 (10), 435–446 (5 with 446) | one batch of no-call candidates (435/436/439/441/446) is pure confirmation; ZOM-435's Linear comments returned empty (273) |
| Fix provenance / server-state verification | 14 | 294, 296, 301–314, 368–372, 394–402 | 3 were wasted on the warehouse (363/368/370/372: one bad query, one describe, one thin result, then abandoned); 1 spill + 1 Bash parse for a single DM |
| Cross-service sweeps & document reads (Slack, Gmail, Drive, Sheets) | 18 | 323–346, 379–385, 396–400, 412, 420 | includes 3 near-empty keyword searches (379 `reinstall`, 380 `splash`, 383 `update from`) that produced nothing and 1 retry (341) |
| Discovery / orientation | 6 | 288, 289, 292, 356, 363, 425 | 356 (Trello board actions) and 292 (CI/CD page) are the two highest-value calls in the range |
| Scope enumeration (is it already filed / anything new) | 2 | 408, 410 | 408 not paginated |
| Writes | 7 | 462, 472, 483, 488, 493, 496, 499 | 2 of the 7 are self-checks (483 counts, 488 dumps the payload) |
| **Total** | **61** | 251–499 | = 40.4% of 151 call records |

Cost of the traps inside this range: T3b ≈ 3 calls (386 sweep share, 394 spill,
402 parse; the sweep was already paid for), T4 ≈ 6 calls (323, 331, 333, 396,
400 + the 325 claim), T7 ≈ 1 net (294 pointer + 303), T2 ≈ 3 (294, 301, 296/292),
T5 ≈ 4 (327, 335, 341/344, 346). Wasted: 4 (warehouse), 3 (empty keyword
searches), 1 (ECONNRESET retry), 1 (`trello_search "#135"` returned nothing) = 9
of 61 ≈ 15%.

The close-out is efficient: one addSheet + one values_update + one append + one
reply, with a local pre-flight (483/488) so the 804-cell write went in first try.
No re-write, no correction pass, no second Slack post.

---

## 6. Findings for the hardening report (attribution)

1. **V01 is a grader defect, not a run defect.** The register holds 132/132 truth
   keys plus ZOM-581; the extra key is *required* by Leonard's injected scope
   rule (ev 35). `truth.json` has no ZOM-581 because truth was cut before the run
   filed it. Effect: the only failed slot (weight 3, 2.8%) is a rule-following
   artefact — which is why the platform reads 97.2% with every requirement MET.
2. **All 132 graded calls and all 132 build statuses are exact.** Every designed
   trap (T1, T2, T3, T3b, T4, T5, T7, T12) was resolved toward the node, and the
   16-key blocker set is exact and duplicate-free in both the register and the
   ZOM-570 description.
3. **The traps were found by sweeps, not by ticket reads.** ZOM-435 lives only on
   a Trello comment (Linear comments empty at 273), ZOM-473 only in a Turkish DM,
   ZOM-562 only in a base64 Gmail body, ZOM-569 only in a GitHub commit time,
   ZOM-567 only in a Slack reply. Ticket-scoped reading alone would have missed
   five of eight.
4. **Two enumerations were left open** (409 `hasNextPage:true` / cursor ZOM-548;
   394 the 100-message page cap on a 104-message window). Neither changed a
   result, but "not filed anywhere" (the premise of the new ticket) rests on a
   truncated Linear query.
5. **Structural blind spot observed, not caused by the run:** `slack_read_channel`
   returns thread parents only (305 returned 1 message for a 2-message thread), so
   a channel-history sweep alone cannot surface Arthur's withdrawal. The run got
   there via the `from:` search hit's `thread_ts`.

