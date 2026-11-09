# /injection: Injection data-integrity review

## 1. Scope

| Item | Value |
|---|---|
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`, `ruthless-grading-v1`) |
| Mode | Chat review, attempt workspace (no task-folder preflight) |
| Actual review time | 2026-11-07 (session) |
| Clock | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal/`, manifest `Evals/references/universes/normal/universe_manifest.json` SHA-256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Reviewed input | `Evals/task_inputs/01_Universe_Inject.sql` (revision 7, 83,518 bytes, 330 lines) SHA-256 `a610e7a5fefebc8df11f327857d8578d39e2c86b05436a486797164eeb604dfc`, user attachment `01_Universe_Inject (4).sql` |
| Previous version | Revision 6, SHA-256 `85efa372…0d29`, reviewed FAIL / COMPLETE (finding C1) in report SHA-256 `6e01f45b480a69c6764cfe350279babcb38ac65b68c68a6ccf11ea82d0c482b6` ("R6 report"). That report carried R4 (`efe75aaf…54e5a0`) and R3 (`a3d4b779…69bf`) evidence |
| References | Eval 0 SHA `e034019b…6eff`; WORKFLOW SHA `ee4cd8e1…fd5d`; schema snapshot `injection.json` SHA `31dcb2b4…5151` (unverified); `id_contracts.json` SHA `fc4711ef…4682`. All recomputed this run and unchanged since R6 |
| Lint | `hg_injection_lint.py` `injection-lint-v1`: 180 statements (1 BEGIN, 139 INSERT, 39 UPDATE, 1 COMMIT); FAIL 0 / CHECK 0 / INFO 0 |
| Reused evidence | Yes, only for statements that are byte-identical to revision 6 (see §5 and §9) |

## 2. Input / authority issues

None. The SQL is substantive and runs as one transaction (`BEGIN` … `COMMIT`).

**Changes from revision 6.** Full-file comparison: revision 7 equals revision 6 with lines 79–82 deleted (`diff <(sed '79,82d' rev6) rev7` gives no output). That removes exactly two statements:

| Removed (rev 6 lines) | Record |
|---|---|
| 78–79 | `slack.slack_messages` `b8b079a1305da1183e10f2214c040662`, Owen `channel_join` in `CE156FDFB428`, 2026-02-12T22:41:27Z |
| 80–81 | `slack.slack_messages` `300958649de97d10a627b1b1b540f733`, Owen `channel_join` in `C09Q4S613CN`, 2026-02-12T22:41:49Z |

This is the smallest fix the R6 report gave for C1. Neither id appears anywhere else in revision 7 (grep count 0). Both rows were `reply_count 0` top-level join events, so no thread recount or UPDATE depends on them. Every line from rev 6 line 83 on moves up by 4 (new = old − 4).

## 3. Checklist

- [x] Save/reload SQL; hash, base manifest and review version recorded (NEW)
- [x] Lint run; every flag resolved, none raised (NEW)
- [x] Inventory of every statement and record (NEW for the diff; unchanged rows REUSED from the R6 §5 ledger with renumbered lines)
- [x] Check A: references and new-key collisions (REUSED for all remaining records; removal creates no new keys)
- [x] Check B: SQL structure and supported schema rules (NEW lint parse of the whole file; REUSED provisional snapshot comparison)
- [x] Check C: dates, relationships and facts in the combined state (NEW re-check of Owen's membership history in all four affected channels; REUSED for the rest)
- [x] Coverage, findings, limits and one final verdict (NEW)

## 4. Lint flags and resolutions

| Flag | Result | Resolution |
|---|---|---|
| future_date, id_contract, drive_unreadable, identities/duplicate_account, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape | 0 flags | The clean lint is consistent with R6's independent confirmations, which still apply because no remaining statement changed: every event time ≤ clock (latest is the Linear comment at 2026-02-13T00:40:00Z; only the Gcal 2026-02-15 start/end plan fields are later); all 31 remaining Slack inserts have `ts` equal to `created_at`; Gmail `history_id` NULL; no `content_path`; Docs have non-empty `body_text`; no generated/FTS columns set; Linear dates in `YYYY-MM-DDTHH:MM:SSZ`; JSON columns in base shape. The line-1 comment is a template answer with no tool-call, pass-rate, gate or padding content. The lint doesn't cover membership history, so it was re-checked by hand (§6 C). |

## 5. Operation ledger

Base paths: Slack = `Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/slack/`; Linear = `…/Other_Services/Services_Data/linear/data.json`; GH = `Universe_Normal/Normal_HarmonyGames_GitHub/Services_Data/github/data.json`. "REUSED (R6)" = same row in the R6 report §5 (and through it R4/R3), statement byte-identical, all dependencies unchanged (§9). Lines are revision-7 line numbers.

| SQL lines | Table | Op | Records | References resolved (path/pointer) | Result | Verification |
|---|---|---|---|---|---|---|
| 4–13 | gdrive.drive_files | INSERT ×5 | folder `d_9b41e7c2…` (Owen), Doc `f_3ca9e15d…` (Arthur), Doc `f_72e0b4c3…`, Slides `f_d15a8c70…`, Sheet `f_a9ba8abc…` (Brian) | parents = Owen root `/drive_files/7047`, Arthur root `/18538`, Brian root `/22881`; ids absent from 53,866 drive_files | PASS | REUSED (R6) |
| 15–16 | gdocs.docs_documents | INSERT | `f_3ca9e15d…` carry-over notes | id = drive id; absent from 633 docs; `body_text` 2,482 chars = style-run `end` | PASS | REUSED (R6) |
| 17–18 | gdocs.docs_documents | INSERT | `f_72e0b4c3…` ZM notes | as above | PASS | REUSED (R6) |
| 20–27 | gsheets.* | INSERT | 1 spreadsheet, 3 tabs (Core 15, Live-Ops 9, Mini-Games 4) | 398 spreadsheets, no collision | PASS | REUSED (R6) |
| 29–54 | gslides.* | INSERT | 1 presentation, 4 pages, 8 elements | 164 presentations, no collision; Season Pass on slide vs later dated sheet/ENG-2428 = supported stale context | PASS | REUSED (R6) |
| 56–57 | slack.slack_messages | INSERT | `488d87e2…` Arthur→Owen DM 2026-02-12T23:10:05Z | `D05S1S2AB5M` (`channels.json /533`) members Arthur + Owen (Owen re-confirmed this run) | PASS: "put you back on one of the paid seats" fits the base 2026-02-11 20:41:09–11Z bulk `channel_leave` | REUSED (R6) |
| 58–59 | slack.slack_messages | INSERT | `91be79cc…` Marcus Bennett (`EMPLOYEE_0002`) 2025-12-11T11:20:12Z | `D05USBTQY1F` (`channels.json /599`) | PASS: id absent from 687,230 messages | REUSED (R6) |
| 60–63 | slack.slack_messages | INSERT | `9bf944b8…` Brian DM; `e48eb03d…` Brian reply under `37dc1365…` | as R6 | PASS | REUSED (R6) |
| 64–65 | slack.slack_messages | INSERT reply | `d49c2458…` Brian, god-bugs, 2025-12-29 | parent `d25dd8d1…` (`messages/C05V5FNLB9V/2025-12.json /22`) | PASS | REUSED (R6) |
| 66–67 | slack.slack_messages | INSERT reply | `70692cd0…` Robert (`EMPLOYEE_0016`) 2025-12-19T17:10:22Z | parent `15e314b2…` (`messages/C09Q4S613CN/2025-11.json /236`) | PASS | REUSED (R6) |
| 68–75 | slack.slack_messages | INSERT reply ×4 | Vincent replies 2025-11-21/22 | as R6 | PASS | REUSED (R6) |
| 76–77 | slack.slack_messages | INSERT `channel_join` | `c399a0bd…` Owen joins `C05V5FNLB9V` god-bugs 2026-02-12T22:41:03Z (ts 1770936063.680719) | base Owen events in channel (full scan of all month files, this run): join 2023-10-07 (`2023-10.json /10`), leave ts 1770842470.006689 = 2026-02-11T20:41:10Z (`2026-02.json /2`); no Owen record after the leave | PASS: leave → rejoin 26 h later, before clock | NEW (re-check) |
| 78–79 | slack.slack_messages | INSERT `channel_join` | `8b1af0fc…` Owen joins `C050WGU41HR` engineering-bots 2026-02-12T22:42:58Z (ts 1770936178.946639) | join 2023-09-15 (`2023-09.json /506`), leave ts 1770842469.401659 = 2026-02-11T20:41:09Z (`2026-02.json /4`); no Owen record after the leave | PASS | NEW (re-check) |
| — | (removed) | — | former Owen joins in `CE156FDFB428` and `C09Q4S613CN` | base: no Owen join/leave in `CE156FDFB428`; only the 2025-11-02 join in `C09Q4S613CN` (`2025-11.json /10`); Owen still listed member of both (`channels.json /359`, `/145`) | C1 resolved: the combined history no longer has a join without a leave | NEW |
| 80–91 | slack.slack_messages | INSERT reply ×6 | Vincent replies 2025-11-21 | as R6 | PASS | REUSED (R6, old 84–95) |
| 92–93 | slack.slack_messages | INSERT reply | `87dc850c…` Marcus, god-bugs | parent `a9665999…` | PASS | REUSED (R6, old 96–97) |
| 94–113 | slack.slack_messages | INSERT reply ×10 | GitHub-bot mirrors of PR comments | parents in `C050WGU41HR`; ts = `created_at` = matching `github_pr_comments.created_at` (lines 143–181) | PASS | REUSED (R6, old 98–117) |
| 114–117 | slack.slack_messages | INSERT reply ×2 | `ea8f1a2d…` (13:05:35Z) under `50de5b6f…`, `52eafc2b…` (01:51:55Z) under `d109a867…` | ts = review-comment `created_at` (lines 183–186); earlier than each parent's base `latest_reply` | PASS | REUSED (R6, old 118–121) |
| 118–141 | slack.slack_messages | UPDATE ×24 | thread metadata (incl. line 120 on `15e314b2…`: reply_count 1) | R6 recount; no removed row was a reply | PASS | REUSED (R6, old 122–145) |
| 143–182 | github pr_comments / timeline_events | INSERT ×10 each | as R6 | PRs and ids as R6 | PASS | REUSED (R6, old 147–186) |
| 183–186 | github.github_review_comments | INSERT ×2 | `#1905#rc_1` 2025-11-19T13:05:35Z, `#1908#rc_1` 2025-11-20T01:51:55Z | reviews `/reviews/1046`, `/1048` | PASS (Advisory 3) | REUSED (R6, old 187–190) |
| 188–251 | trello.* | INSERT | card `690b2728…d512`, 2 actions, checklist, 28 items | as R6 | PASS | REUSED (R6, old 192–255) |
| 252–257 | trello.* | INSERT | ZM card + 2 actions | as R6 | PASS | REUSED (R6, old 256–261) |
| 259–278 | gmail.* | INSERT ×5 each | as R6 | as R6 | PASS | REUSED (R6, old 263–282) |
| 280–287 | gcal.gcal_events | INSERT ×4 | as R6 | as R6 | PASS | REUSED (R6, old 284–291) |
| 289–314 | linear.linear_comments | INSERT ×13 | as R6 | base `/comments` empty | PASS | REUSED (R6, old 293–318) |
| 315–327 | linear.linear_issues | UPDATE ×13 | `updated_at` = each new comment's time | as R6 | PASS | REUSED (R6, old 319–331) |
| 328–329 | linear.linear_issues | UPDATE ×2 | ENG-2403/2404 `description` → NULL, `updated_at` → 2026-02-12T22:30:00Z | `/issues/2340`, `/2341` | PASS | REUSED (R6, old 332–333) |


### Slack thread recount

Unchanged from R6: all 24 UPDATEs match base replies + SQL replies. The two removed rows were top-level `channel_join` events, not replies, so no count changes.

## 6. Check results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | Removing rows creates no new key and leaves no dangling reference (grep count 0 for both removed ids). All remaining new ids, actors, parents and targets REUSED from R6 §6 A: full Slack collision coverage (687,230 messages / 5,353 files, scan_complete), one account per person, ID contracts, Drive readability. Owen remains a listed member of `C05V5FNLB9V` (`/53`), `C050WGU41HR` (`/21`), `CE156FDFB428` (`/359`), `C09Q4S613CN` (`/145`) and DM `D05S1S2AB5M` (`/533`), re-confirmed this run from `channels.json` (SHA prefix `476eaa6d…`, equal to the route map's source hash). |
| B — SQL structure and supported schema rules | PASS | NEW lint parse of all 180 statements: balanced transaction, column/value counts match, quoting/escaping well formed, JSON valid and base-shaped, no generated columns, NOT NULL columns supplied. Provisional snapshot comparison REUSED: Advisory 1. |
| C — Dates, relationships and consistency | PASS | C1 resolved. NEW full scan of Owen's `channel_join`/`channel_leave` events in all four channels: god-bugs and engineering-bots each have join → base leave 2026-02-11 → injected rejoin 2026-02-12, with no Owen record in between; `CE156FDFB428` and `C09Q4S613CN` now have no injected join, and their base histories are untouched. The rest of the combined state (doc/branch facts, reply chronology, review-comment/bot-mirror match, Trello activity, Linear `updated_at`) is REUSED from R6 §6 C. |

## 7. Findings

No failing findings.

**C1 (from R6), resolved.** Revision 7 deletes the two Owen `channel_join` rows in channels he never left (`CE156FDFB428`, `C09Q4S613CN`), as R6 recommended. Verified by full diff and a fresh membership-history scan.

### Advisories (not failing)

1. **Columns not in the schema snapshot or the base export (B, provisional NOT COVERED), carried from R3/R4/R6.** `gslides.slides_pages.notes`, `gslides.slides_page_elements.ordinal`, `.table_json`, `github.github_review_comments.pull_request_review_id`, `.side`, `.subject_type`, `.seq` (lines 31–54, 183–186). The snapshot is unverified, so this is a compatibility limit, not a defect. The script is one transaction, so a missing column on the live database would roll back every record. To be safe, drop those 7 columns and their values.
2. **Cached Trello board activity, carried.** DD Product Roadmap's `dateLastActivity` (2025-10-10) predates the injected card's activity (2025-11-05). Cached field with unknown semantics.
3. **Review-comment timing (minor), carried.** Both review comments are 3–4 s after their review's `submitted_at` (13:05:35Z vs 13:05:32Z; 01:51:55Z vs 01:51:51Z) and are linked to it by `pull_request_review_id`. On GitHub, comments in a review are normally created at or before submission. No base rule to test against; not a defect. Setting both to the review time or one second before, and moving the bot mirrors on lines 115/117 to match, would remove the oddity.
4. **Partial rejoin (informational, new).** The base bulk leave covers 6 channels; the SQL rejoins Owen to 2 of them (god-bugs, engineering-bots). The DM's "one of the paid seats so you can read the DD channels" doesn't promise the other four, so this is consistent. (R6 Advisory 4 on "joined the conversation" wording is moot now that the canvas-channel row is gone.)

## 8. Evidence limits (outside certification scope)

- Live execution, current database compatibility and undocumented constraints are not certified (schema snapshot unverified; Advisory 1).
- Trello board membership isn't in the export. GitHub PR file lists aren't exported, so review-comment `path` values can't be matched to changed files.
- Agent visibility, discoverability and difficulty belong to `/prompt` and `/hardness`. Notes carried for `/prompt`: the only base record of build 0.3.310 is Leonard's DM to Arthur (`D04UGG61DUM/2026-02.json /103`), which Owen can't see, and the doc ties it to "the economy line"; blanking ENG-2403/2404 removes the checklist hints from the two masters.

## 9. Stage provenance (for reuse)

Static checks A–C depend on: SQL SHA `a610e7a5…4dfc`; universe manifest SHA `5e01ac44…e450`; schema snapshot SHA `31dcb2b4…5151`; id_contracts SHA `fc4711ef…4682`; lint `injection-lint-v1`; clock 2026-02-14 00:00 UTC. Reused items come from the R6 report (SHA `6e01f45b…82b6`) §5 ledger rows, §5 thread recount and §6 A/B/C evidence for unchanged records, which in turn carry R4 (`efe75aaf…54e5a0`) and R3 (`a3d4b779…69bf`) evidence. Each reused item covers a statement byte-identical to revision 6 (verified by full diff: the only change is deletion of rev-6 lines 79–82), with the base manifest, reference hashes and clock recomputed and unchanged. R6's FAIL came only from C1, which affected the two deleted rows, so the reused rows are unaffected by that report's defect. Re-checked NEW: Owen's join/leave history in the four affected channels, membership in `channels.json` (source hash matches the route map), and Slack source files `messages/C05V5FNLB9V/2026-02.json` (`67d010aa…`), `messages/C050WGU41HR/2026-02.json` (`9deee79f…`), `messages/CE156FDFB428/2025-11.json` (`9ad33c35…`), `messages/C09Q4S613CN/2025-11.json` (`2d0817b9…`). This PASS / COMPLETE report can be reused by `/prompt` for the static checks while the SQL hash and dependencies above match.

## 10. Next action

Run `/prompt`, then `/hardness`. Both read the injection SQL, so any earlier pass on them is outdated. Later stages (`/oe`, `/rubric`) also read the SQL and need rerunning after those.

### FINAL VERDICT: PASS

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (runtime does not report the effort level)

Next action: Run /prompt, then /hardness (both read the changed injection SQL)

Evidence limits: Static scope only; live deployment and current schema compatibility not certified (snapshot unverified, Advisory 1); Agent visibility and difficulty belong to /prompt and /hardness
