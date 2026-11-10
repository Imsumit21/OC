# Injection data-integrity review: Eval 0

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. Base facts for the 84 byte-identical statements are **REUSED** from my previous PASS / COMPLETE report on `3c035f2a…` (`R6/prev/0_injection.previous_report_on_3c035f2a.md`, SHA-256 `01dbb84d8c7e19c6fb863e682acc36945373eb005e08c99c73793d31bd7ca385`; the copy is byte-identical to the report I wrote). The 13 changed or new statements were checked **NEW** in full. The whole-file checks were also re-run NEW: lint, Check B, the clock sweep, Linear chronology, and collisions for every changed or new key. |
| Reuse conditions | All four hold:<br>1. The prior ledger records each reused claim with its source pointer.<br>2. Dependencies are unchanged: the universe manifest, schema snapshot, id_contracts and known-issues file were re-hashed (below), and the clock is the same.<br>3. Each reused statement is byte-identical (quote-aware statement diff), and its base collections are unchanged. Uniqueness for unchanged keys rests on the same complete scans over the same files.<br>4. No changed statement affects a reused claim; the cross-statement effects are re-checked in §6. |
| Mode | Independent chat review, audit only. Same workspace adaptations as before: the report goes to `R6/out/0_injection.md`; no input store, no `hg_write_output.py`, no `input_manifest.json`; the lint runs through `Task_Authoring/tools/hg.py` (`--task-dir Task_Authoring/task_inputsS`). |
| Review time | 2026-11-06 |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`. Manifest `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` (re-hashed; unchanged). |
| Input under review | `R6/inputs/01_Universe_Inject.sql`: 60,835 bytes, 244 lines, 97 statements, SHA-256 `f8d905bdd0c29585b17090b54aeb7837135f9d2462440ba71d81192d0871249c` (re-hashed; matches the brief). Not executed. |
| Previous version | `R6/prev/01_Universe_Inject.previous_3c035f2a.sql`, SHA-256 `3c035f2af02934538a1e07d04fe82a2ea2f0a7b8031cff8ca1bd53eb4217bc6f`. Byte-identical to the file I reviewed before. |
| Schema snapshot / ID contracts | `01ef579236212034a43a53914754f86ed9248be48c961009cef5b4bd6106f6eb` / `fc4711ef07667333c1cf2a417279826f0432539195f7acdfacfa86e9d9ed4682` (both unchanged). |
| Known base issues | `Task_Authoring/references/known_data_issues/synthcut.md` `8895c4dc73da…` (unchanged). |
| Context-only inputs | `00_Task_Assigned_Inputs.md` `e8b82698…`, `02_Universe_Date.txt` `2f0af108…`, `04_Prompt.txt` `2a23afd8…`. All three are unchanged. |

## 2. Input / authority issues

- No SQL comment changed. None is about padding, tool calls, pass rates or gates.
- **Grader-facing text:** none. The lint found none, and every changed text field was also read by hand.
- **Resolved by this revision:**
  - D1: `content_path` and `size` are now NULL on the native Doc and Sheet.
  - Most of D2: Brian's SENT copies now carry ARCHIVED, and `in_reply_to`/`references` are `''`.
  - The token-travel half of D6.
- The Sep 22 mail drops its unsupported "from the September handoff" reference.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, manifest, review version | Done (workspace adaptation: recorded here). |
| Diff against the previous SQL | Done statement by statement, with a per-column diff. <br>• 96 → 97 statements <br>• 84 byte-identical <br>• 12 changed records <br>• 1 new record (`cmt_zom526_3`) <br>• 0 dropped |
| Run lint; resolve every flag | NEW: 0 flags (§4). |
| Inventory every statement | NEW: 97 statements (71 INSERT, 26 UPDATE). No DELETE or upsert. |
| Check A | **PASS**: NEW for changed and new keys and references; REUSED for byte-identical ones. |
| Check B | **PASS** (provisional): NEW over the whole file. |
| Check C | **PASS**: NEW, claim by claim, for every changed or new record; whole-file clock and Linear chronology re-run NEW. |
| Report coverage, findings, limits, verdict | Done. |

## 4. Lint

`hg_injection_lint.py` (injection-lint-v1) was run through `hg.py lint` on SHA `f8d905bd…`, universe synthcut, clock `2025-10-01T07:00:00Z`.

- **Checks run:** future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required.
- **Statements:** 97 (71 insert, 26 update). Linear comments 25, linear_issues updates 20; the other row counts are as before.
- **Flags:** FAIL 0, CHECK 0, INFO 0.

All 118 JSON literals were parsed by hand: 0 errors.

## 5. Operation ledger

Numbering: current #1–59 are prev #1–59; #60 is new; current #61–97 are prev #60–96.

### Changed and new statements (all NEW)

| # | Line | Table | Op | Record | Change against prev | Result |
|---|---|---|---|---|---|---|
| 8 | L24 | gmail_messages | I | Brian's copy of the Sep 22 mail, `<CAPT--p4sBC8…>` | Body: "Nothing else changes from the September handoff." → "Nothing else changes." Labels `SENT, Opened` → `ARCHIVED, SENT, Opened`; X-Gmail-Labels "Archived,Sent,Opened". `in_reply_to`/`references` NULL → `''`. | PASS |
| 10, 12 | L35, L46 | gmail_messages | I | Julia's and Frederick's copies of the Sep 22 mail | The same body edit; `in_reply_to`/`references` NULL → `''`. | PASS |
| 14 | L57 | gmail_messages | I | Brian's copy of the Sep 26 mail, `<CAPT--p4a5fY…>` | Labels → `ARCHIVED, SENT, Opened`; X-Gmail-Labels updated; NULL → `''`. | PASS |
| 16, 18 | L66, L74 | gmail_messages | I | Julia's and Frederick's copies of the Sep 26 mail | NULL → `''` only. | PASS |
| 24 | L92 | drive_files | I | `f_7c3e91a4…` brief (native Doc) | `size` 13872 → NULL; `content_path` → NULL. | PASS |
| 34 | L130 | drive_files | I | `f_e4a17c90…` calendar sheet (native Sheet) | `size` 9216 → NULL; `content_path` → NULL. | PASS |
| 59 | L177 | linear_comments | I | `cmt_zom526_2` (Brian, 09-26T15:40:50Z, seq 2) | Adds "and, once that event is back, Axe Arena"; "the event runs" → "the events run". | PASS |
| 60 | L178 | linear_comments | I | **new** `cmt_zom526_3` (Calvin `usr_49b9dfa5…`, 09-30T16:24:19Z, seq 3) | "Collect and Win tokens go through the queue manager now (#472). Only the Axe Arena travel is left here, and that waits on the event coming back." | PASS |
| 61 | L179 | linear_issues | U | ZOM-526 | `updated_at` 09-26T15:40:50Z → 09-30T16:24:19Z, equal to the new latest comment. Base was 09-17T15:52:10Z. | PASS |
| 88 | L226 | linear_comments | I | `cmt_zom544_1` (Vincent, 09-29T15:35:50Z) | Removes "on the auth branch" and "Google Play login is still waiting on the backend setup." | PASS |
| 96 | L238 | trello_actions | I | `68dac820…` commentCard (Leonard, 09-29T17:55:44Z) | Text → "New quest set goes in with the Mon Oct 13 rollover if it is ready. Nothing in the beta waits on it, the current set runs the whole time either way." | PASS (advisory E1) |

### Byte-identical statements (84; REUSED)

These are REUSED from the prior ledger (`01dbb84d…` §5), each with its recorded pointers:

| Current # | Statements | Prior result reused |
|---|---|---|
| 1–7, 9, 11, 13, 15, 17 | Slack DM and Halloween rows; Gmail threads | Slack ID formula, membership, threads and pointers; Gmail thread IDs. |
| 19–23, 25–33, 35–37 | GCal; the folder; docs and style runs; Slides; Sheets rows | GCal base shape; style runs; slide text; sheet headers. |
| 38–44 | GitHub `#470#rc_10` on `rev_9`; `#468` `rev_3`, `rc_38`, `ev_6`; `#473` `c_2`, `ev_5`; the PR bump | Review and merge timing; paths in the PR net diffs; numbering. |
| 45–50 | Mirrors and cards | Mirror text, lag and ID order; card Comments and Reviewers fields. |
| 51–58, 62–87, 89–95 | Linear comments and UPDATEs other than ZOM-526 and ZOM-544 | The per-issue claim table. |
| 97 | Trello card UPDATE | Badges 0→1; dateLastActivity. |

### NEW collision rescans for changed and new keys

- **Gmail:** the 6 thread numbers and 2 Message-ID tokens appear in 0 of 81,404 thread files plus users.json.
- **Drive:** `f_7c3e91a4…` and `f_e4a17c90…` are absent from 53,631 files.
- **Trello:** `68dac820…` is absent from 5,252 actions.
- **Linear:** `cmt_zom526_3` is new; the base has 0 comments, and all 25 SQL comment IDs are unique.

## 6. Checks

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | The changed and new keys are absent from their complete collections (§5). New and changed references resolve:<br>• `cmt_zom526_3` → ZOM-526 (`/issues/3600`), author Calvin Price (one Linear account);<br>• the author of #472 is `PERSON_0003_GITHUB_USERNAME` = "Calvin Price";<br>• the Trello action still targets card `/cards/781`, board and list, with member `PERSON_6094` = Leonard Hayes.<br>Drive readability: the Doc has its docs row with a non-empty body, and the Sheet has its sheet rows. This is the readable route both Eval 0 and the lint use for native files, and the lint's `drive_unreadable` check passes. Byte-identical statements: REUSED (§5). |
| B — SQL structure and supported schema rules | PASS (provisional) | NEW over all 97 statements:<br>• column and value counts match on all 71 INSERTs, with no duplicate columns;<br>• every UPDATE uses `WHERE id = '<literal>'`;<br>• no NOT NULL column is omitted and no NULL goes into a NOT NULL column (`drive_files.size` and `content_path` are nullable);<br>• no generated column is written;<br>• the 118 JSON literals parse;<br>• `cmt_zom526_3.created_at`/`updated_at` and ZOM-526 `updated_at` use `YYYY-MM-DDTHH:MM:SSZ`.<br>The snapshot MISMATCH set is identical (A1). |
| C — Dates, relationships and consistency | PASS | **Clock** (NEW, 156 values): only the 16 GCal start/end values are later than the clock, and they are plan fields. The new latest Linear time is 09-30T16:24:19Z.<br>**Linear chronology** (NEW, 21 issues): all OK. ZOM-526 now has comments 09-24 → 09-26 → 09-30 with seq 1, 2, 3; updated_at = the latest comment; still In Progress with `started_at` 09-17.<br>**Claims:** every changed claim matches the base (detail below). |

### Check C detail for each changed record

**Gmail Sep 22 mail (8, 10, 12).**

- The removed phrase "from the September handoff" pointed at a handoff the base never records ("config handoff" appears in 0 Gmail files), so removing it takes out an unsupported reference.
- The snippet is unchanged and is still the 175-character prefix of the body: the edit sits after character 175, and the thread snippet still equals it.
- The Sep 26 correction ("Correction to my Sep 22 mail … Same contents, same owner") still reads correctly against the edited body.
- Advisory E3: `size_estimate` stays 4312 although the body is 27 characters shorter.

**Gmail labels and reply fields (8, 14, and all 6).**

- `["ARCHIVED","SENT","Label_b19fb8d1b3"]` with "Archived,Sent,Opened" is exactly the shape of one of Brian's two base sent mails (`brian.foster@…/1822693237981026750`), in the same order.
- `''` for `in_reply_to` and `references` is the base convention for non-replies in these three mailboxes (5,316 messages have `''`/`''`).
- Message-ID, X-GM-THRID, Subject, Date / `internal_date` and Delivered-To are unchanged and still consistent (NEW re-check).

**Drive (24, 34).**

- Both native files now carry `size` NULL and `content_path` NULL. No content is lost: the Doc is served from its `docs_documents` row and the Sheet from its `sheets_sheets` rows.
- This departs from the base convention (595 of 595 native Docs and 356 of 356 native Sheets carry both fields) but removes D1's dangling path (advisory D1′).
- The parents, owners, shares and timestamps are unchanged.

**ZOM-526 (59, 60, 61).**

- **"Once that event is back, Axe Arena" (Brian, 09-26):**
  - Brian's queue spec to Calvin lists "4. Axe arena tokens travelling the icon" (`D0770ET6WBW/2025-09 /212`, 09-18; repeated in `D0770ET1HV2 /2307`, 09-24). Brian's 08-14 note planned to "reuse the animations from the next Season Pass and Axe Arena" for token travel (`C09ATAJ220H/2025-08 /11`).
  - Axe Arena was postponed for the beta on 09-22: "*<!here>* We've decided to postpone Axe Arena for the beta release" (`C05KNDCHAAG/2025-09 /31`); also `D07GK9QQG7M /249`.
  - So the note is grounded, and its 09-26 date falls after the postponement.
- **"C&W tokens go through the queue manager now (#472)" (Calvin, 09-30 16:24:19Z):**
  - #472 is "Implement Win&Collect into Queue Manager", authored by Calvin Price and merged 2025-09-30T15:53:04Z by Arthur. That is 31 minutes before the comment.
  - Its diff makes `RewardVFXManager` wait on `CollectAndWinProgressController.GetCollectAndWinStatusRoutine()` before `PlaySeasonPassToken()`. Main's `QueueManager` runs that inside `Level_end_animations`, which is Brian's order (C&W tokens, then SP tokens).
  - "Only the Axe Arena travel is left" fits Brian's queue spec and the postponement.
- **Author:** Calvin is not the assignee (ZOM-526 has none) but implemented #472 and is the assignee of the parent, ZOM-521. That is plausible.
- **Consistency with the other injected records:**
  - ZOM-521's description still leaves "Tokens traveling to live-ops" unticked (byte-identical UPDATE), which now matches the Axe Arena remainder;
  - `cmt_zom521_1` (09-26) says the last two items are tokens and cards;
  - Frederick's DM lists Axe Arena among the items "not in the beta".
- **No contradiction:** there is no base unfurl, notification or mention of ZOM-526 after 09-17.

**ZOM-544 (88).**

- "Apple sign-in works from the settings menu, but progress does not restore yet: levels, currencies and cards are not synced." This matches Vincent's 09-25 Apple sign-in test (`CD843DBC4C3E/2025-09 /36`): levels, currencies and cards all failed.
- Apple auth code is on main (`Assets/Scripts/Backend/Requests/Authentication/AppleAuthentication.cs`, `ServerAuthentication.cs`).
- Removing the Google Play sentence removes a claim that went stale 73 minutes later. Douglas posted at 09-29T16:48Z: "I completed the Google Play setup in the backend … ready for testing on dev" (`/39`).
- Advisory E2: the comment no longer names the build tested.

**Trello (96).**

- Base context: the card is "Add more quests and balance quest rewards - (Leonard/Douglas)" in the "BETA: Sep 30" list, created and renamed by Leonard on 09-12.
- Mon Oct 13 is a Monday and fits the quests service's Monday weekly timer.
- No base record makes the beta depend on the new quests, and none mentions an Oct 13 quest set.
- The payload shape, list name (SC-13 convention), card and board fields, ID timestamp, badges and dateLastActivity are unchanged and still correct.
- Advisory E1: internal wording tension.

**Cross-statement effects:** none of the changes alters a fact any reused statement relies on. Every Gmail key, thread ID and snippet is the same; the Drive IDs and parents are the same; ZOM-526's earlier comment `cmt_zom526_1` and the ZOM-521 UPDATE are untouched.

## 7. Findings and advisories

**No demonstrated defects.**

Each advisory is tagged **[CSC]** (a /prompt reviewer could score it under Cross-Service Coherence) or **[cosmetic]**, with its status since the previous report.

**Advisories from the previous report:**

| ID | Tag | Status | Note |
|---|---|---|---|
| A1 | cosmetic (deploy-compatibility limit) | Unchanged | Same snapshot-missing column set. |
| A6 | CSC | Unchanged | "Approval from Product … he" against Robert as the approver; the brief is unchanged. |
| A9 | cosmetic | Unchanged | Stmt 5's "current prod build" names no build. |
| A10 | cosmetic | Unchanged | Rules sit in Frederick's DM. |
| A11 | CSC | Unchanged | SC-15 repaired by the ZOM-521 untick. Now better supported: ZOM-526 explains the remaining token item. |
| N2 | cosmetic | Unchanged | `#468#ev_6` numbering. |
| N4 residual | cosmetic | Unchanged | The base export has no Linear comments, so injected comments take `sequence` 1. |
| N5 | cosmetic | Unchanged | No `state_history_json` on ZOM-432, ZOM-344 or ZOM-566. |
| N6 | CSC | Unchanged | ZOM-521 "icons" item ticked against `cmt_zom465_2`. |
| D1 | cosmetic | **Resolved** | NULL `content_path`/`size` remove the dangling path. It reappears as D1′ below, because the files no longer match the base shape for native files. |
| D2 | cosmetic | **Mostly resolved** | ARCHIVED and `''` are fixed. Still unchanged: no trailing `\r` on `mbox_from`, `mbox_from` time equal to the Date header, and the header order. |
| D3 | cosmetic | Unchanged | #470 has both an approval mirror and a comment mirror. |
| D4 | cosmetic | Unchanged | Frederick, not a team_ZOM member, comments on ZOM-78. |
| D5 | CSC | Unchanged | ZOM-344 Done with no corroborating artefact. |
| D6 | CSC | **Partly resolved** | Token half: `cmt_zom526_3` records that the C&W trigger landed (#472) and that only the postponed Axe Arena travel remains, so ZOM-526 In Progress and the unticked ZOM-521 item are now justified. Still open: #475 (card-pack animation) merged 09-30T16:09Z while ZOM-528 is In Progress and ZOM-521's "Claimed Cards" item is unticked (SC-16 pattern). |
| D7 | CSC | Unchanged | ZOM-432 closure evidence is indirect ("update header image"; the iOS #50 change list). |
| D8 | cosmetic | Unchanged | The #473 comment is post-merge, with base precedent. |
| SC-6 | CSC | Unchanged | Brian's address is shared with the Node CEO in base. |
| SC-13 | CSC | Unchanged | The list name differs from the action payload. |
| SC-38 | CSC | Unchanged | Season Pass. |
| SC-48 | cosmetic | Unchanged | Istanbul times. |
| SC-16 pattern | CSC | Reduced | See D6. |

**New in this revision:**

- **D1′ [cosmetic].** The native Doc and Sheet now have NULL `size` and `content_path`, whereas every base native Doc and Sheet carries both. This is readable under the Eval and lint rule, and it was accepted in the earlier `c955d6ca` version.
- **E1 [CSC].** The Trello comment says the new quest set "goes in with the Mon Oct 13 rollover if it is ready", then "the current set runs the whole time either way". These can be reconciled if the new quests are additive, as the card name "Add more quests" suggests. Read the other way, they conflict.
- **E2 [cosmetic].** `cmt_zom544_1` no longer says which build was tested. The base tests were on dev and the auth-branch builds. The claim itself matches the base.
- **E3 [cosmetic].** The `size_estimate` of the Sep 22 copies stays 4312 after a 27-character body cut. The base export has no size field to compare against.

## 8. Limits

- **Outside the static scope:** live deploy compatibility (A1); search ranking, visibility and difficulty.
- **Not comparable with the base export:** Gmail `snippet` and `size_estimate`; Linear comments, state history and team privacy.
- **Bounded content searches:** the NEW content searches for this revision covered Slack 2025-07 to 2025-10 in every channel and DM, plus Gmail, GitHub data and the git repos.
- **Workspace adaptation:** no input store, no output writer and no manifest write.
- No required static check is unresolved.

## 9. Stage dependencies (for reuse)

| Dependency | Value |
|---|---|
| SQL | `f8d905bdd0c29585b17090b54aeb7837135f9d2462440ba71d81192d0871249c` |
| Universe manifest | `da2f4cf0…4aac1a` |
| Schema snapshot | `01ef5792…06f6eb` |
| id_contracts | `fc4711ef…ed4682` |
| Known issues | `8895c4dc…961a52` |
| Clock | 2025-10-01T07:00:00Z |
| Lint | injection-lint-v1, 0 flags |

**New base facts recorded this run:**

- PR #472: author Calvin Price; merged 2025-09-30T15:53:04Z; changes the `RewardVFXManager` C&W → SP token order.
- Axe Arena postponed for the beta on 2025-09-22 (`C05KNDCHAAG/2025-09 /31`).
- Brian's queue spec includes Axe Arena token travel (`D0770ET6WBW/2025-09 /212`, `D0770ET1HV2/2025-09 /2307`).
- Douglas completed the Google Play backend setup on 09-29T16:48Z (`CD843DBC4C3E /39`).
- Base non-reply Gmail convention: `''`/`''` (5,316 messages).

Manifest entry that would be written:

```json
{"review_version": "injection-static-v2", "evidence_contract": "stage-evidence-v1", "input_sha256": "f8d905bdd0c29585b17090b54aeb7837135f9d2462440ba71d81192d0871249c", "reused_evidence": [{"source_report": "R6/prev/0_injection.previous_report_on_3c035f2a.md", "sha256": "01dbb84d8c7e19c6fb863e682acc36945373eb005e08c99c73793d31bd7ca385", "ledger_items": ["§5 rows for statements now numbered 1-7, 9, 11, 13, 15, 17, 19-23, 25-33, 35-58, 62-87, 89-95, 97 (byte-identical)", "§5 complete collision scans for unchanged keys", "§6 Check C detail for unchanged groups"], "dependencies": {"universe_manifest": "da2f4cf0…4aac1a (unchanged)", "schema_snapshot": "01ef5792…06f6eb (unchanged)", "id_contracts": "fc4711ef…ed4682 (unchanged)", "clock": "2025-10-01T07:00Z (unchanged)", "statements": "byte-identical (statement diff)"}}], "result": "PASS", "execution_status": "COMPLETE"}
```

## 10. Next action

Proceed to `/prompt`. Earlier stage results for `3c035f2a…` are out of date; rerun `/prompt`, `/hardness`, `/oe` and `/rubric` in that order. Carry A6, A11, N6, D5, D6 (cards half), D7, E1 and the SC-6, SC-13, SC-38 touches into `/prompt`. Optional cleanups: E1 (clarify that the quest set is additive) and D2's remaining `mbox_from` `\r`.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt

Evidence limits: Static scope only. Live deploy compatibility is unverified: the bundled snapshot (`01ef5792…`) lacks several columns the SQL writes (A1). Gmail snippet and size, Linear comments and state history, and team privacy cannot be compared with the base export. Claims for the 84 byte-identical statements rest on the prior report `01dbb84d…`, whose reuse dependencies all still match.
