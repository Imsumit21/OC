# /injection: Injection data-integrity review

## 1. Scope

| Item | Value |
|---|---|
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`, `ruthless-grading-v1`) |
| Mode | Chat review, attempt workspace (no task-folder preflight) |
| Actual review time | 2026-11-07T18:14:00Z |
| Clock | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal/`, manifest `Evals/references/universes/normal/universe_manifest.json` SHA-256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Reviewed input | `Evals/task_inputs/01_Universe_Inject.sql` (revision 6, 84,569 bytes) SHA-256 `85efa372e6373fb3b035bd2250e8f644e48220cff63714c84fbc44b2727d0a29`, user attachment `01_Universe_Inject (3).sql` |
| Previous version | Revision 4, SHA-256 `be13a93a…50d9`, reviewed PASS / COMPLETE in report SHA-256 `efe75aaff1bf759d6e0ae801e42353895b9446117893d9f500e8e125dd54e5a0` ("R4 report"), which itself reused the R3 report (SHA `a3d4b779…69bf`) |
| References | Eval 0 SHA `e034019b…6eff`; WORKFLOW SHA `ee4cd8e1…fd5d`; schema snapshot `injection.json` SHA `31dcb2b4…5151` (unverified); `id_contracts.json` SHA `fc4711ef…4682`. All recomputed this run and unchanged since R4 |
| Lint | `hg_injection_lint.py` `injection-lint-v1`: 182 statements (1 BEGIN, 141 INSERT, 39 UPDATE, 1 COMMIT); FAIL 0 / CHECK 0 / INFO 0 |
| Reused evidence | Yes, only for statements that are byte-identical to revision 4 (see §5 and §9) |

## 2. Input / authority issues

None. SQL is substantive and runs as one transaction (`BEGIN` … `COMMIT`).

**Changes from revision 4** (difflib comparison of the full files):

| New line(s) | Record | Change |
|---|---|---|
| 16 | `gdocs.docs_documents` `f_3ca9e15d…` | `body_text` rewritten (2,234 → 2,482 chars); style-run `end` 2234 → 2482 |
| 36, 42, 48, 54 | `gslides.slides_page_elements` BODY texts | Rewording to "main screens are on the optimized sprites"; Live-Ops slide no longer lists Daily Gift |
| 57 | `slack.slack_messages` `488d87e2…` | `text`: "gave you read access" → "put you back on one of the paid seats so you can read the DD channels" |
| 59 | `slack.slack_messages` | Row `456afffc…` (2025-12-03) replaced by `91be79cc…` (2025-12-11, "on last night's Android build") |
| 65 | `slack.slack_messages` `d49c2458…` | `text` reworded |
| 66–67 | `slack.slack_messages` | NEW reply `70692cd0…` by Robert (`EMPLOYEE_0016`) under `15e314b2…` in `C09Q4S613CN` |
| 76–83 | `slack.slack_messages` | NEW ×4 `channel_join` rows for Owen (`EMPLOYEE_0021`) 2026-02-12 22:41–22:42Z in `C05V5FNLB9V`, `CE156FDFB428`, `C09Q4S613CN`, `C050WGU41HR` |
| 97 | `slack.slack_messages` `87dc850c…` | `text` reworded |
| 99–117 | 10 GitHub-bot mirror rows | Only the `issuecomment-…` numbers inside attachment URLs changed; ids, ts, parents unchanged |
| 119, 121 | GitHub-bot review mirrors | Rows `3134bfa3…`/`dc86553c…` replaced by `ea8f1a2d…` (13:05:35Z) and `52eafc2b…` (01:51:55Z) |
| 124 | `slack.slack_messages` UPDATE | NEW thread metadata on `15e314b2…` |
| 188, 190 | `github.github_review_comments` | `created_at` 13:04:10Z → 13:05:35Z and 01:50:40Z → 01:51:55Z |
| 193 | `trello.trello_cards` `690b2728…d512` | `dateLastActivity` → 2025-11-05T10:41:00Z |
| 199 | `trello.trello_checklists` | name "Screens checked" → "Main screens checked" |
| 296 | `linear.linear_comments` ENG-2363 | "Android still hits this" (was "…too") |
| 332–333 | `linear.linear_issues` UPDATE | NEW: ENG-2403 and ENG-2404 `description = NULL`, `updated_at = 2026-02-12T22:30:00Z` |

No other injected row references the three removed ids (`456afffc`, `3134bfa3`, `dc86553c`): grep count 0.

## 3. Checklist

- [x] Save/reload SQL; hash, base manifest and review version recorded (NEW)
- [x] Lint run; every flag resolved, none raised (NEW)
- [x] Inventory of every statement and record (NEW for the diff; unchanged rows REUSED from the R4 §5 ledger)
- [x] Check A: references and new-key collisions (NEW for changed/new records; REUSED for unchanged)
- [x] Check B: SQL structure and supported schema rules (NEW lint parse of the whole file; REUSED provisional snapshot comparison)
- [x] Check C: dates, relationships and facts in the combined state (NEW for changed records and their interactions; REUSED for unchanged)
- [x] Coverage, findings, limits and one final verdict (NEW)

## 4. Lint flags and resolutions

| Flag | Result | Resolution |
|---|---|---|
| future_date, id_contract, drive_unreadable, identities/duplicate_account, actor_name, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape | 0 flags | Confirmed independently: every event time ≤ clock (latest is the Linear comment at 2026-02-13T00:40:00Z; only the Gcal 2026-02-15 start/end plan fields are later). All 33 Slack inserts have `ts` equal to `created_at` (recomputed this run). Gmail `history_id` NULL; no `content_path`; Docs have non-empty `body_text`; `text_fts`/`body_text_fts` not set; Linear dates in `YYYY-MM-DDTHH:MM:SSZ`; JSON columns are in base shape. The line-1 comment is a template answer with no tool-call, pass-rate, gate or padding content. **The clean lint doesn't cover membership history.** That is where the Check C defect below was found. |

## 5. Operation ledger

Base paths: Slack = `Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/slack/`; Linear = `…/Other_Services/Services_Data/linear/data.json`; GH = `Universe_Normal/Normal_HarmonyGames_GitHub/Services_Data/github/data.json`. "REUSED (R4)" = same row in the R4 report §5, statement byte-identical, all dependencies unchanged (§9). Old R4 line numbers shift by +10 after new line 67 and by +11 after new line 124.

| SQL lines | Table | Op | Records | References resolved (path/pointer) | Result | Verification |
|---|---|---|---|---|---|---|
| 4–13 | gdrive.drive_files | INSERT ×5 | folder `d_9b41e7c2…` (Owen), Doc `f_3ca9e15d…` (Arthur), Doc `f_72e0b4c3…`, Slides `f_d15a8c70…`, Sheet `f_a9ba8abc…` (Brian) | parents = Owen root `/drive_files/7047`, Arthur root `/18538`, Brian root `/22881`; ids absent from 53,866 drive_files | PASS | REUSED (R4) |
| 15–16 | gdocs.docs_documents | INSERT | `f_3ca9e15d…` carry-over notes | id = drive id; absent from 633 docs (R4) | PASS: rewritten `body_text` is 2,482 chars once `''` and `\n` are decoded, and style run `end` 2482 equals it (recomputed this run) | NEW (body) / REUSED (id) |
| 17–18 | gdocs.docs_documents | INSERT | `f_72e0b4c3…` ZM notes | as above | PASS | REUSED (R4) |
| 20–27 | gsheets.* | INSERT | 1 spreadsheet, 3 tabs (Core 15, Live-Ops 9, Mini-Games 4) | 398 spreadsheets, no collision | PASS | REUSED (R4) |
| 29–54 | gslides.* | INSERT | 1 presentation, 4 pages, 8 elements | 164 presentations, no collision | PASS: BODY text edits only; Live-Ops slide drops Daily Gift, which now agrees with the sheet ("last pass") and Trello (`incomplete`). Season Pass still on the slide while the sheet says "next" and Oliver's 2025-12-05 ENG-2428 comment says unfinished: stale claim corrected by a later dated record, the same supported context as R4 | NEW (texts) / REUSED (ids) |
| 56–57 | slack.slack_messages | INSERT | `488d87e2…` Arthur→Owen DM 2026-02-12T23:10:05Z | `D05S1S2AB5M` members Arthur + Owen (R4) | PASS: text only. "put you back on one of the paid seats" fits the base bulk `channel_leave` of Owen at 2026-02-11 20:41:09–11Z (6 channels incl. `C050WGU41HR/2026-02.json /4`, `C05V5FNLB9V/2026-02.json /2`) | NEW (text) / REUSED (membership) |
| 58–59 | slack.slack_messages | INSERT | `91be79cc…` Marcus Bennett (`EMPLOYEE_0002`, `users.json /0`) 2025-12-11T11:20:12Z | `D05USBTQY1F` (`channels.json /599`) members incl. Marcus and Owen | PASS: id absent from 687,230 messages / 5,353 files (`lookup`, scan_complete) | NEW |
| 60–63 | slack.slack_messages | INSERT | `9bf944b8…` Brian DM; `e48eb03d…` Brian reply under `37dc1365…` | as R4 | PASS | REUSED (R4) |
| 64–65 | slack.slack_messages | INSERT reply | `d49c2458…` Brian, god-bugs, 2025-12-29 | parent `d25dd8d1…` (`messages/C05V5FNLB9V/2025-12.json /22`) | PASS: text only | NEW (text) / REUSED (refs) |
| 66–67 | slack.slack_messages | INSERT reply | `70692cd0…` Robert (`EMPLOYEE_0016`, `users.json /9`) 2025-12-19T17:10:22Z | parent `15e314b2…` by Robert (`messages/C09Q4S613CN/2025-11.json /236`, ts 1764013100.931229, reply_count 0); Robert in `C09Q4S613CN` members (`channels.json /145`) | PASS: same channel, `thread_ts_legacy` = parent ts, later than parent; id absent (lookup); no base reply carries that `thread_ts` (full message scan) | NEW |
| 68–75 | slack.slack_messages | INSERT reply ×4 | Vincent replies 2025-11-21/22 | as R4 | PASS | REUSED (R4) |
| 76–77 | slack.slack_messages | INSERT `channel_join` | `c399a0bd…` Owen joins `C05V5FNLB9V` god-bugs 2026-02-12T22:41:03Z | base: Owen joined 2023-10-07 (`2023-10.json /10`), left 2026-02-11T20:41:10Z (`2026-02.json /2`) | PASS: leave → rejoin is a coherent sequence | NEW |
| 78–79 | slack.slack_messages | INSERT `channel_join` | `b8b079a1…` Owen joins `CE156FDFB428` (Android canvas comments) 2026-02-12T22:41:27Z | base: Owen already posted 4 replies there on 2025-11-19 (`messages/CE156FDFB428/2025-11.json /203–/206`); no `channel_join`/`channel_leave` by Owen in this channel | **FAIL (C1)**: join without an earlier leave | NEW |
| 80–81 | slack.slack_messages | INSERT `channel_join` | `30095864…` Owen joins `C09Q4S613CN` dd-road-to-sub-250mb 2026-02-12T22:41:49Z | base: Owen joined 2025-11-02 (`messages/C09Q4S613CN/2025-11.json /10`) and posted 2025-11-19; no `channel_leave` by Owen in this channel; not in the base 2026-02-11 bulk leave | **FAIL (C1)**: second join without a leave | NEW |
| 82–83 | slack.slack_messages | INSERT `channel_join` | `8b1af0fc…` Owen joins `C050WGU41HR` engineering-bots 2026-02-12T22:42:58Z | base: joined 2023-09-15 (`2023-09.json /506`), left 2026-02-11T20:41:09Z (`2026-02.json /4`) | PASS | NEW |
| 84–95 | slack.slack_messages | INSERT reply ×6 | Vincent replies 2025-11-21 | as R4 | PASS | REUSED (R4) |
| 96–97 | slack.slack_messages | INSERT reply | `87dc850c…` Marcus, god-bugs | parent `a9665999…` | PASS: text only | NEW (text) / REUSED (refs) |
| 98–117 | slack.slack_messages | INSERT reply ×10 | GitHub-bot mirrors of PR comments | parents in `C050WGU41HR` (R4 pointers); ids/ts unchanged | PASS: only URL comment numbers changed; ts = `created_at` = the matching `github_pr_comments.created_at` (lines 148–184) | NEW (attachments) / REUSED (refs) |
| 118–121 | slack.slack_messages | INSERT reply ×2 | `ea8f1a2d…` (13:05:35Z) under `50de5b6f…`, `52eafc2b…` (01:51:55Z) under `d109a867…` | parents as R4 | PASS: ids absent (lookup); ts = review-comment `created_at` (lines 188, 190); both earlier than each parent's `latest_reply` (1763557543.301089, 1763603522.124499), so the UPDATEs on lines 141/143 still hold | NEW |
| 122–145 | slack.slack_messages | UPDATE ×24 | thread metadata | see recount below | PASS | NEW (line 124) / REUSED (others, re-checked for the changed replies) |
| 147–186 | github pr_comments / timeline_events | INSERT ×10 each | as R4 | PRs and ids as R4 | PASS | REUSED (R4) |
| 187–190 | github.github_review_comments | INSERT ×2 | `#1905#rc_1` 2025-11-19T13:05:35Z, `#1908#rc_1` 2025-11-20T01:51:55Z | reviews `#1905#rev_1` submitted 13:05:32Z (`/reviews/1046`), `#1908#rev_1` 01:51:51Z (`/reviews/1048`), both APPROVED by `EMPLOYEE_0025_GITHUB_USERNAME`; no base review comments on either PR (1,614 scanned) | PASS (see Advisory 3) | NEW (times) / REUSED (ids, commits) |
| 192–255 | trello.* | INSERT | card `690b2728…d512`, 2 actions, checklist, 28 items | as R4 | PASS: `dateLastActivity` 2025-11-05T10:41:00Z = latest action (`commentCard` at 10:41:00Z); checklist rename only | NEW (2 fields) / REUSED (rest) |
| 256–261 | trello.* | INSERT | ZM card + 2 actions | as R4 | PASS | REUSED (R4) |
| 263–282 | gmail.* | INSERT ×5 each | as R4 | as R4 | PASS | REUSED (R4) |
| 284–291 | gcal.gcal_events | INSERT ×4 | as R4 | as R4 | PASS | REUSED (R4) |
| 293–318 | linear.linear_comments | INSERT ×13 | as R4 | base `/comments` empty | PASS: ENG-2363 text edit only | NEW (text) / REUSED (rest) |
| 319–331 | linear.linear_issues | UPDATE ×13 | `updated_at` = each new comment's time | as R4 | PASS | REUSED (R4) |
| 332–333 | linear.linear_issues | UPDATE ×2 | ENG-2403 "Core Game UI Optimization", ENG-2404 "Live-Ops UI Optimization": `description` → NULL, `updated_at` → 2026-02-12T22:30:00Z | `/issues/2340` (base `updated_at` 2025-11-06T15:29:43Z, checklist description), `/issues/2341` (base 2025-11-19T14:29:13Z, checklist with `[X]` marks) | PASS: column nullable in snapshot; NULL is a base representation (ENG-2401 `/issues/2338` has `description: null`); new time is later than base and before the clock. Searches of Snowflake and other JSON exports for the checklist wording found no current copy that would now disagree (Snowflake `rg -F` exit 1; the Slack hits are 2025-11 planning messages, which are historical) | NEW |

### Slack thread recount (base replies + SQL replies vs SQL UPDATE)

NEW: `15e314b2…` has 0 base replies (full scan of `thread_ts` = 1764013100.931229) + 1 SQL reply = `reply_count` 1, 1 user (Robert), `latest_reply` 1766164222.418229, `thread_ts_legacy` = parent ts. All match line 124.
Re-checked for changed replies: `50de5b6f` (4 base + 2 SQL = 6) and `d109a867` (6), with latest still the base reply, because the replacement mirrors are earlier. The other 22 are REUSED from R4 (reply sets and ts unchanged). All 24 match.

## 6. Check results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | NEW: 8 new Slack ids absent from 687,230 messages in 5,353 files (`lookup`, scan_complete, no errors). Actors resolve: Owen `EMPLOYEE_0021` (`users.json /11`), Robert `EMPLOYEE_0016` (`/9`), Marcus `EMPLOYEE_0002` (`/0`); all are listed members of the target channels (`channels.json /21, /53, /145, /359, /599`; Robert isn't in `CE156FDFB428` and posts nothing there). Parent `15e314b2…` exists in the same channel. GitHub reviews `/reviews/1046`, `/1048` exist. Linear ENG-2403/2404 exist (`/issues/2340`, `/2341`). Unchanged records REUSED from R4 §6 A (full collision coverage, one account per person, ID contracts, Drive readability). |
| B — SQL structure and supported schema rules | PASS | NEW lint parse of all 182 statements: balanced transaction, column/value counts match, quoting/escaping well formed, JSON columns valid and in base shape, no generated columns set, Linear dates in base format, NOT NULL columns supplied (`linear_issues.updated_at` set; `description` nullable). Provisional snapshot comparison REUSED: Advisory 1. |
| C — Dates, relationships and consistency | **FAIL** | C1 (below): two injected `channel_join` events for Owen are in channels he never left in the base. Everything else NEW passes: the rewritten doc's added rules are instructions, not facts; its claim that 0.3.310 "came off the economy line" agrees with the injected #1915/#1916 comments ("into EconomyChanges … next BoomBit drop") and the base `EconomyChanges` branch (GH `/branches/253`), and no base record states another branch (Slack/GitHub/Linear/Gmail searches for "0.3.310" found only Leonard's DM `D04UGG61DUM/2026-02.json /103`). Other new and changed records keep their chronology (replies after parents, review comments matching the bot mirrors, Trello activity = last action, Linear `updated_at` later than base). The god-bugs and engineering-bots rejoins reconcile the base 2026-02-11 leaves. Unchanged records REUSED from R4 §6 C. |

## 7. Findings

### C1 — Owen "joins" two channels he is already in (FAIL, Check C: impossible membership chronology introduced by SQL)

- **Records:** line 78–79, `b8b079a1305da1183e10f2214c040662`, `CE156FDFB428`, `subtype 'channel_join'`, 2026-02-12T22:41:27Z; line 80–81, `300958649de97d10a627b1b1b540f733`, `C09Q4S613CN`, `subtype 'channel_join'`, 2026-02-12T22:41:49Z. Text `<@EMPLOYEE_0021_SLACK_ID> has joined the channel`.
- **Evidence:**
  - `C09Q4S613CN`: Owen already joined on 2025-11-02 (`messages/C09Q4S613CN/2025-11.json /10`, `channel_join`, ts 1762045303.105739) and posted on 2025-11-19 (ts 1763524896.854659). The channel has no `channel_leave` by Owen at any date.
  - `CE156FDFB428`: Owen posted 4 thread replies on 2025-11-19 (`messages/CE156FDFB428/2025-11.json /203–/206`) and has no join or leave there.
  - The base records Owen's seat removal as one bulk `channel_leave` at 2026-02-11 20:41:09–11Z across 6 channels (`C04V7N09LE7`, `C050WGU41HR`, `C05KNDCHAAG`, `C05V5FNLB9V`, `C0880U9751A`, `C08R27X0EAH`). Neither of these two channels is in it.
  - A join event requires the user not to be a member, so the combined history has a join with no matching leave.
  - Slack's export is complete for both channels' months (scan of all 5,353 message files, no errors).
- **Alternatives considered:**
  - An unexported leave: the base's own seat-removal leaves are exported, and none covers these channels.
  - That the join only means "rejoined after a seat change": the DM on line 57 says so, but the base's own record of that change lists the channels he left, and these two aren't among them.
- **Effect:** these two rows contradict Owen's base membership history and his own Nov 19 activity in the same channels. The other two joins (god-bugs, engineering-bots) are correct.
- **Smallest fix:** delete the two statements at lines 78–79 and 80–81. Owen stays a listed member of both channels (`channels.json /145`, `/359`), so his read access doesn't depend on them. Nothing else needs to change: no UPDATE or other row references these ids. If you want the "back on a paid seat" story to cover these channels too, you'd also have to add matching Owen `channel_leave` rows at 2026-02-11 ~20:41:1xZ. That's a larger change and not required.

### Advisories (not failing)

1. **Columns not in the schema snapshot or the base export (B, provisional NOT COVERED), carried from R3/R4.** `gslides.slides_pages.notes`, `gslides.slides_page_elements.ordinal`, `.table_json`, `github.github_review_comments.pull_request_review_id`, `.side`, `.subject_type`, `.seq` (lines 31–54, 187–190). The snapshot is unverified, so this is a compatibility limit, not a defect. The script is one transaction, so a missing column on the live database would roll back every record. To be safe, drop those 7 columns and their values.
2. **Cached Trello board activity, carried from R4.** DD Product Roadmap's `dateLastActivity` (2025-10-10) predates the injected card's activity (2025-11-05). Cached field with unknown semantics.
3. **Review-comment timing (new, minor).** Both review comments are now 3–4 s after their review's `submitted_at` (13:05:35Z vs 13:05:32Z; 01:51:55Z vs 01:51:51Z) and are tied to it by `pull_request_review_id`. On GitHub, comments inside a review are normally created at or before submission. The base links no review comment to a review, so there's no base rule to test against. Not a defect. Setting both to the review time or one second before it, and moving the matching bot mirrors on lines 119/121 to the same time, would remove the oddity.
4. **Join wording in canvas comment channels (new, cosmetic).** Base canvas-comment (`FC:`) channels use "has joined the conversation" (7 base rows, e.g. `CE22D7884D8F/2026-01.json`). Moot if C1's fix deletes the `CE156FDFB428` row.

## 8. Evidence limits (outside certification scope)

- Live execution, current database compatibility and undocumented constraints are not certified (schema snapshot unverified; Advisory 1).
- Trello board membership isn't in the export. GitHub PR file lists aren't exported, so review-comment `path` values can't be matched to changed files.
- Agent visibility, discoverability and difficulty belong to `/prompt` and `/hardness`. For `/prompt`, these are notes, not findings here:
  - The only base record of build 0.3.310 is Leonard's DM to Arthur (`D04UGG61DUM/2026-02.json /103`, "0.3.310 on is what I'm testing"), which Owen can't see. The doc now ties it to "the economy line".
  - Blanking ENG-2403/2404 removes the checklist hints from the two masters.

## 9. Stage provenance (for reuse)

Static checks A–C depend on: SQL SHA `85efa372…0d29`; universe manifest SHA `5e01ac44…e450`; schema snapshot SHA `31dcb2b4…5151`; id_contracts SHA `fc4711ef…4682`; lint `injection-lint-v1`; clock 2026-02-14 00:00 UTC. Reused items come from the R4 report SHA `efe75aaf…54e5a0` §5 ledger rows, the §5 thread recount and the §6 A/B/C evidence for unchanged records. That report in turn carries R3 (SHA `a3d4b779…69bf`) evidence. Each reused item covers a statement that is byte-identical in revision 6 (verified by full diff), with every reference fingerprint, the base manifest and the clock recomputed and unchanged. Changed and new lines were verified NEW (§2, §5). This FAIL report can't be reused as a whole-check PASS by `/prompt`. A changed SQL version invalidates it.

## 10. Next action

Delete the two `channel_join` inserts for `CE156FDFB428` (lines 78–79) and `C09Q4S613CN` (lines 80–81), then send `/injection` again. After that passes, rerun `/prompt` and `/hardness`, because both read the injection SQL.

### FINAL VERDICT: FAIL

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (runtime does not report the effort level)

Next action: Remove the two Owen `channel_join` rows for `CE156FDFB428` and `C09Q4S613CN` (SQL lines 78–81), then rerun /injection

Evidence limits: Static scope only; live deployment and current schema compatibility not certified (snapshot unverified, Advisory 1); Agent visibility and difficulty belong to /prompt and /hardness
