# /injection — Injection data-integrity review

## 1. Scope

| Item | Value |
|---|---|
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`) |
| Mode | Chat review, attempt workspace (no task-folder preflight) |
| Actual review time | 2026-11-07T12:56:21Z |
| Clock | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal/` — `hg4-2026-08-31-v37.zip` (archive SHA-256 `2913eb8b…e21a`); manifest `Evals/references/universes/normal/universe_manifest.json` SHA-256 `5e01ac44…e450` |
| Reviewed input | `Evals/task_inputs/01_Universe_Inject.sql` (revision 3, 80,854 bytes) SHA-256 `975909fb25e515722df0331b79770f69e97919a13766a31e21ab742426f5a1d1` — user attachment `01_Universe_Inject.sql` |
| Assignment (context only) | Owen Baker, Game Engineer (Unity); Engineering / Engineering Ops / Actions; long-horizon; medium |
| References | Eval 0 SHA `e034019b…eff`; WORKFLOW SHA `ee4cd8e1…d5fd`; schema snapshot `injection.json` SHA `31dcb2b4…5151` (unverified); `id_contracts.json` SHA `fc4711ef…82` |
| Lint | `hg_injection_lint.py` v`injection-lint-v1`: 174 statements (1 BEGIN, 136 INSERT, 36 UPDATE, 1 COMMIT); FAIL 0 / CHECK 0 / INFO 0 |
| Reused evidence | None (all checks NEW) |

## 2. Input / authority issues

None. SQL is substantive, single transaction (`BEGIN` … `COMMIT`). SQL comments are section headers only (no padding, tool-call, pass-rate or gate comments).

## 3. Checklist

- [x] Save/reload SQL; hash, base manifest and review version recorded (NEW)
- [x] Lint run; every flag resolved — none raised (NEW)
- [x] Inventory of every statement and record (NEW)
- [x] Check A — references and new-key collisions (NEW)
- [x] Check B — SQL structure and supported schema rules; provisional snapshot comparison separated (NEW)
- [x] Check C — dates, relationships and facts in the combined state (NEW)
- [x] Coverage, findings, limits and one final verdict (NEW)

## 4. Lint flags and resolutions

| Flag | Result | Resolution |
|---|---|---|
| future_date, id_contract, drive_unreadable, identities/duplicate_account, actor_name, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape | 0 flags | Confirmed independently below (event times ≤ clock; Gmail `history_id` NULL; no `content_path` used; Sheets/Slides have native rows; generated `text_fts`/`body_text_fts` not set; Linear `created_at`/`updated_at` in `YYYY-MM-DDTHH:MM:SSZ`; all JSON columns in base shape). |

## 5. Operation ledger

Base paths: Other = `Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/`; GH = `Universe_Normal/Normal_HarmonyGames_GitHub/Services_Data/github/data.json`; Gmail = `Universe_Normal/Normal_HarmonyGames_Gmail/Services_Data/gmail/`.

| SQL lines | Table | Op | Records | References resolved (path/pointer) | Result |
|---|---|---|---|---|---|
| 4–5 | gdrive.drive_files | INSERT | `d_9b41e7c2a05d36f8e1c7a4` folder "DD bug carry-over" (owner Owen) | parent `d_4e13bd40cc73d0fc76f87c` = Owen root (`gdrive/data.json /drive_files/7047`) | PASS (id unused, 53,866 records scanned) |
| 6–7 | gdrive.drive_files | INSERT | `f_3ca9e15d7b20f4e681ad52` Doc "DD bug carry-over notes" (owner Arthur, reader Owen) | parent `d_cc3e90160f490686039986` = Arthur root (`/drive_files/18538`) | PASS |
| 8–13 | gdrive.drive_files | INSERT | `f_72e0b4c3d91a5f68c2b7e4` Doc, `f_d15a8c70e3f2b94a61c8d3` Slides, `f_a9ba8abc7d5189babcb378` Sheet (owner Brian; readers Owen, Arthur, Oliver) | parent `d_fc22d5941b2aeb5c03ad32` = Brian root (`/drive_files/22881`) | PASS |
| 15–18 | gdocs.docs_documents | INSERT | 2 docs, ids = drive ids, non-empty `body_text` | gdocs 633 records scanned, no collision | PASS (readable) |
| 20–27 | gsheets.sheets_spreadsheets / sheets_sheets | INSERT | 1 spreadsheet, 3 tabs (Core 15, Live-Ops 9, Mini-Games 4 rows) | gsheets 398 scanned, no collision | PASS (native Sheets row; readable) |
| 29–54 | gslides.* | INSERT | 1 presentation, 4 pages, 8 elements | gslides 164 scanned, no collision | PASS (native Slides row) |
| 56–57 | slack.slack_messages | INSERT | `488d87e2…` Arthur→Owen DM, ts 1770937805 (2026-02-12T23:10:05Z) | `D05S1S2AB5M` members incl. Arthur `EMPLOYEE_0025` and Owen `EMPLOYEE_0021` (`slack/channels.json /533`) | PASS |
| 58–59 | slack.slack_messages | INSERT | `456afffc…` Marcus Bennett (`EMPLOYEE_0002`), 2025-12-03 | `D05USBTQY1F` members incl. Marcus and Owen (`/599`) | PASS |
| 60–61 | slack.slack_messages | INSERT | `9bf944b8…` Brian (`EMPLOYEE_0026`), 2025-12-08 | `D07E9PSQB6W` members incl. Brian and Owen (`/806`) | PASS |
| 62–63 | slack.slack_messages | INSERT reply | `e48eb03d…` Brian, 2025-12-01 | parent `37dc1365…` in `C09Q4S613CN` dd-road-to-sub-250mb (`messages/C09Q4S613CN/2025-11.json /242`); Brian member | PASS |
| 64–65 | slack.slack_messages | INSERT reply | `d49c2458…` Brian, 2025-12-29 | parent `d25dd8d1…` in `C05V5FNLB9V` god-bugs (`messages/C05V5FNLB9V/2025-12.json /22`) | PASS |
| 66–85 | slack.slack_messages | INSERT reply ×10 | Vincent (`EMPLOYEE_0012`) replies 2025-11-21/22 on canvas comment roots | parents in `CE156FDFB428` "Bugs on Android 2231" (`messages/CE156FDFB428/2025-11.json` /139, /188, /165, /212, /126, /147, /229, /227, /175, /224); Vincent member | PASS |
| 86–87 | slack.slack_messages | INSERT reply | `87dc850c…` Marcus, 2025-11-28 | parent `a9665999…` god-bugs (`messages/C05V5FNLB9V/2025-11.json /30`) | PASS |
| 88–111 | slack.slack_messages | INSERT reply ×12 | GitHub-bot (`SLACK_BOT_0004`) mirrors of the GitHub comments below | parents in `C050WGU41HR` engineering-bots (`2025-11.json` /147, /166, /195, /198, /202, /210, /234, /242; `2025-12.json` /18, /22); bot is a member | PASS |
| 112–134 | slack.slack_messages | UPDATE ×23 | thread metadata on the 23 parents above | see thread recount table | PASS |
| 136–175 | github.github_pr_comments / timeline_events | INSERT ×10 each | `#1895#c_3`, `#1898#c_3`, `#1901#c_3`, `#1902#c_3`, `#1903#c_3`, `#1905#c_3`, `#1907#c_2`, `#1908#c_3`, `#1915#c_2`, `#1916#c_2` and matching `ev_N` | PRs exist (GH `/pull_requests/1022…1046`); base comments are `c_1`/`c_2` (or `c_1` only for #1907/#1915/#1916); 884 comments and 12,435 events scanned, no collision | PASS |
| 176–179 | github.github_review_comments | INSERT ×2 | `#1905#rc_1`, `#1908#rc_1` by Arthur | reviews `#1905#rev_1` (APPROVED 13:05:32Z) and `#1908#rev_1` (APPROVED 01:51:51Z) by `EMPLOYEE_0025_GITHUB_USERNAME`; `commit_id` = each PR's `head_sha`; 1,614 review comments scanned, no collision | PASS |
| 181–244 | trello.* | INSERT | card `690b2728…d512` "UI optimization pass" (idShort 211), 2 actions, checklist `690b2728…e1d5`, 28 check items | board `65eb4ec5…638f` DD Product Roadmap, list `66c38013…50e3` (name matches), member `d1cd0fef…f068` = Brian Foster; max base idShort on board 210 | PASS |
| 245–250 | trello.* | INSERT | card `68d27e28…502d` "ZM bug list close-outs" (idShort 80), 2 actions | board `6851a656…32ab` ZM ROADMAP, list `68c45122…d16b` Backlog; max base idShort 79 | PASS |
| 252–271 | gmail.gmail_threads / gmail_messages | INSERT ×5 each | Vincent→Owen mail (Owen INBOX + Vincent SENT copies), 3 calendar invitation mails (Owen, Oliver, Robert) | all mailboxes exist in `gmail/users.json`; thread ids use base `<mailbox>/<decimal>` form; all 8 thread/message identifiers absent from all 88,726 thread files (`rg` exit 1) | PASS |
| 273–280 | gcal.gcal_events | INSERT ×4 | "DD bug review" on Arthur/Robert/Oliver/Owen calendars, 2026-02-15 17:00–17:30Z | calendars exist (`gcal/data.json /calendars`); event ids and `ical_uid` unused (11,130 events) | PASS |
| 282–307 | linear.linear_comments | INSERT ×13 | comments on ENG-2401, 2363, 2428, 2437, 2429, 2410, 2430, 2280, 2281, 2398, 2181, 2351, 2406 | issues exist by `id` (`linear/data.json /issues`); authors Arthur `usr_cc3e…`, Vincent `usr_65c7…`, Oliver `usr_bdf0…`, Brian `usr_fc22…`; base `/comments` is empty, so no collision possible | PASS |
| 308–320 | linear.linear_issues | UPDATE ×13 | `updated_at` set to each new comment's time | every new value is later than the base `updated_at` (e.g. ENG-2401 2025-11-04T18:10:01Z → 2026-02-13T00:40:00Z; ENG-2429 2025-11-18T17:51:59Z → 2025-11-19T14:27:00Z) | PASS |

### Slack thread recount (base replies + SQL replies vs SQL UPDATE)

All 23 match exactly on `thread_ts_legacy` = parent ts, `reply_count`, `reply_users_count` and `latest_reply`. Examples: `d25dd8d1` 60 base + 1 new = 61, 3 users, latest 1767021345.207719; `50de5b6f` 4 + 2 = 6, 1 user, latest stays base 1763557543.301089; `dfb3bc5e` 4 + 1 = 5, latest stays base 1763077285.311909. Every new reply has the parent's channel and `thread_ts_legacy`, a later ts than its parent, and a `ts` equal to its `created_at` (all 28 checked).

## 6. Check results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | Every actor, channel, parent, board, list, PR, review, issue, mailbox, calendar and Drive parent resolves (ledger). New-key collision scans complete with no hits: Slack 687,230 messages in 5,353 files; Drive 53,866; GitHub comments 884 / events 12,435 / review comments 1,614; Trello cards 803, actions 5,294, checklists 54, check items 161; Gcal 11,130; Gmail 88,726 thread files; Docs/Sheets/Slides full collections. One account per person: every author ID maps to the named person (Slack users.json, Linear users, GitHub users, Trello members). Listed ID contracts: Gmail `history_id` NULL; no Drive `content_path` used. Drive readability: the 2 Docs have docs rows with non-empty `body_text`; the Sheet and Slides deck have native gsheets/gslides rows; the folder needs no content. |
| B — SQL structure and supported schema rules | PASS | Balanced single transaction; every INSERT's column/value counts match (lint parse); quoting/escaping (`''`, `E'…\n'`) well formed; JSON columns parse and match the base shape (`metadata_json '{}'`, arrays `'[]'`, objects `'{}'`); generated `text_fts`/`body_text_fts` not set; Linear text dates in `YYYY-MM-DDTHH:MM:SSZ`; NOT NULL columns supplied for all inserted tables (no new Linear issues, so `state_history_json` not applicable). Provisional snapshot comparison: see Advisory 1 (7 columns NOT COVERED). |
| C — Dates, relationships and consistency | PASS | All event timestamps ≤ 2026-02-14 00:00 UTC (latest: Linear comment 2026-02-13T00:40:00Z); only the Gcal start/end (2026-02-15) is later, a scheduled plan field. GitHub comments fall between PR creation and merge; review comments precede their review's `submitted_at`; Slack bot mirrors carry the same timestamps as the GitHub comments. Vincent's injected records (Nov 20–22, 2025) predate his last base Slack message (2025-11-23T09:36:50Z), consistent with the doc's "before he left". Arthur's "28 UI children" equals the base tree (ENG-2403/2404/2405 hold 15 + 9 + 4 = 28); the Sheet's screen→ticket map matches the Linear titles; ENG-2073 exists ("Sign-In Account Synchronization Issues"); Trello badges (28 items / 27 checked / 1 comment) match the inserted rows. Injected Slack replies don't contradict their base threads (e.g., the train-background canvas thread ends with Arthur "ok let me see…" before Vincent's "still off… leaving this one open"). The Slides deck's "All UI tickets shipped" and the Trello ticks are contradicted by later dated records (Brian on ENG-2437 2025-11-24, Oliver on ENG-2428 2025-12-05); that is supported stale context, not an integrity defect. No grader-facing text found. |

## 7. Findings

No demonstrated defects.

### Advisories (not failing)

1. **Columns not in the schema snapshot or the base export (B, provisional NOT COVERED).** `gslides.slides_pages.notes` (lines 32–50), `gslides.slides_page_elements.ordinal`, `.table_json` (lines 34–54), `github.github_review_comments.pull_request_review_id`, `.side`, `.subject_type`, `.seq` (lines 177, 179). The bundled snapshot is unverified, so this is a compatibility limit, not a defect. Because the whole script is one transaction, a missing column on the live database would roll back every record. Smallest safe change: drop those 7 columns from the column lists and values. All carry NULL, constants or data the base export doesn't show anyway, so nothing visible is lost.
2. **Folder created after it is referenced (C, minor).** Arthur's DM (line 57, 2026-02-12T23:10:05Z) says "Put a sheet in your DD bug carry-over folder", but the folder `d_9b41e7c2a05d36f8e1c7a4` (line 5) has `created_time`/`modified_time` 2026-02-12T23:30:00Z. One valid reading is that Owen made the folder after the request, so this isn't impossible chronology. Setting both times before 23:10 (for example `2026-02-12T23:00:00Z`) removes the ambiguity.
3. **Cached Trello board activity.** DD Product Roadmap's `dateLastActivity` (2025-10-10) predates the injected UI card's activity (2025-11-05 to 2025-11-21). ZM ROADMAP (2025-10-13) is already later than its injected card (2025-09-23). This is a cached field with unknown semantics, so it isn't a defect.

## 8. Evidence limits (outside certification scope)

- Live execution, current database compatibility and undocumented constraints are not certified (schema snapshot unverified; Advisory 1).
- Trello board membership isn't present in the export; Brian is a workspace member (`/members/9`).
- GitHub PR file lists aren't exported, so the review-comment `path` values can't be matched to changed files.
- Agent visibility, discoverability and task difficulty belong to `/prompt` and `/hardness`. For example, the only base record of build 0.3.310 is Leonard's 2026-02-11 DM to Arthur (`messages/D04UGG61DUM/2026-02.json /103`), which Owen can't see. Nothing contradicts the doc's claim.

## 9. Stage provenance (for reuse)

Static checks A–C above depend on: SQL SHA `975909fb…a1d1`; universe manifest SHA `5e01ac44…e450`; schema snapshot SHA `31dcb2b4…5151`; id_contracts SHA `fc4711ef…82`; lint `injection-lint-v1`; clock 2026-02-14 00:00 UTC. A changed SQL version invalidates this report.

## 10. Next action

Proceed to `/prompt`. If you take up Advisory 1 or 2, the edited SQL needs `/injection` again first.

### FINAL VERDICT: PASS

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (runtime does not report the effort level)

Next action: Proceed to /prompt

Evidence limits: Static scope only; schema snapshot unverified (7 columns NOT COVERED, Advisory 1); live load, Agent visibility and difficulty not certified.
