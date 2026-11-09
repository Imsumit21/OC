# /injection — Injection data-integrity review

## 1. Scope

| Item | Value |
|---|---|
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`) |
| Mode | Chat review, attempt workspace (no task-folder preflight) |
| Actual review time | 2026-11-07T15:12:14Z |
| Clock | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal/`, `hg4-2026-08-31-v37.zip` (archive SHA-256 `2913eb8b…e21a`); manifest `Evals/references/universes/normal/universe_manifest.json` SHA-256 `5e01ac44…e450` |
| Reviewed input | `Evals/task_inputs/01_Universe_Inject.sql` (revision 4, 81,098 bytes) SHA-256 `be13a93a5920e0a68549489834fe9bcf0ef29f65a1390897389b4db7aa3850d9`, user attachment `01_Universe_Inject (2).sql` |
| Previous version | Revision 3, SHA-256 `975909fb…a1d1`, reviewed PASS / COMPLETE in report SHA-256 `a3d4b779dec3e35e0fd28075752729aa728da79244fda71b15e85008b03769bf` ("R3 report") |
| Assignment (context only) | Owen Baker, Game Engineer (Unity); Engineering / Engineering Ops / Actions; long-horizon; medium |
| References | Eval 0 SHA `e034019b…6eff`; WORKFLOW SHA `ee4cd8e1…fd5d`; schema snapshot `injection.json` SHA `31dcb2b4…5151` (unverified); `id_contracts.json` SHA `fc4711ef…4682` (all unchanged since R3) |
| Lint | `hg_injection_lint.py` `injection-lint-v1`: 174 statements (1 BEGIN, 136 INSERT, 36 UPDATE, 1 COMMIT); FAIL 0 / CHECK 0 / INFO 0 |
| Reused evidence | Yes: unchanged statements (see §3 and §9) |

## 2. Input / authority issues

None. SQL is substantive, one transaction (`BEGIN` … `COMMIT`).

**Changes from revision 3** (full `diff`, line numbers unchanged because line 1 was blank before):

| Line | Record | Change |
|---|---|---|
| 1 | SQL comment | Blank line → `-- Are you planning to inject? Yes` (template answer, not a stored record) |
| 5 | `gdrive.drive_files` `d_9b41e7c2…` folder | `created_time`/`modified_time` 2026-02-12T23:30:00Z → 23:00:00Z |
| 16 | `gdocs.docs_documents` `f_3ca9e15d…` | `body_text` rewritten (2,011 → 2,234 chars); style-run `end` 2011 → 2234 |
| 57 | `slack.slack_messages` `488d87e2…` | `text`: "those fix notes are the only record" → "that's the only record" |
| 186 | `trello.trello_actions` `690b29bc…` | comment `text` → "When we close these UI tickets out every one gets a note naming the current public build, otherwise nobody can tell later what players actually had." |

All other 169 lines are byte-identical to revision 3.

## 3. Checklist

- [x] Save/reload SQL; hash, base manifest and review version recorded (NEW)
- [x] Lint run; every flag resolved, none raised (NEW)
- [x] Inventory of every statement and record (NEW diff; unchanged rows REUSED from R3 §5)
- [x] Check A: references and new-key collisions (NEW for changed records; REUSED for unchanged)
- [x] Check B: SQL structure and supported schema rules (NEW lint parse of whole file; REUSED provisional snapshot comparison)
- [x] Check C: dates, relationships and facts in the combined state (NEW for changed records and their interactions; REUSED for unchanged)
- [x] Coverage, findings, limits and one final verdict (NEW)

## 4. Lint flags and resolutions

| Flag | Result | Resolution |
|---|---|---|
| future_date, id_contract, drive_unreadable, identities/duplicate_account, actor_name, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape | 0 flags | Confirmed independently: event times ≤ clock (latest still Linear comment 2026-02-13T00:40:00Z); Gmail `history_id` NULL; no `content_path`; Docs have non-empty `body_text`, Sheets/Slides native rows; `text_fts`/`body_text_fts` not set; Linear dates `YYYY-MM-DDTHH:MM:SSZ`; JSON columns in base shape. Line 1 comment is a template answer (no tool-call, pass-rate, gate or padding content) and isn't loaded into any service. |

## 5. Operation ledger

Base paths: Other = `Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/`; GH = `Universe_Normal/Normal_HarmonyGames_GitHub/Services_Data/github/data.json`; Gmail = `Universe_Normal/Normal_HarmonyGames_Gmail/Services_Data/gmail/`. "REUSED (R3 ledger)" = same row in R3 report §5, statement byte-identical, all dependencies unchanged (§9).

| SQL lines | Table | Op | Records | References resolved (path/pointer) | Result | Verification |
|---|---|---|---|---|---|---|
| 4–5 | gdrive.drive_files | INSERT | `d_9b41e7c2a05d36f8e1c7a4` folder "DD bug carry-over" (owner Owen) | parent `d_4e13bd40cc73d0fc76f87c` = Owen root (`gdrive/data.json /drive_files/7047`) | PASS: id unused (53,866 drive_files, re-looked-up this run); `created_time`/`modified_time` now 2026-02-12T23:00:00Z, before Arthur's DM at 23:10:05Z | NEW |
| 6–7 | gdrive.drive_files | INSERT | `f_3ca9e15d7b20f4e681ad52` Doc "DD bug carry-over notes" (owner Arthur, reader Owen) | parent `d_cc3e90160f490686039986` = Arthur root (`/drive_files/18538`) | PASS: drive row unchanged from R3; id unused (re-looked-up this run) | NEW (id) / REUSED (refs) |
| 8–13 | gdrive.drive_files | INSERT | `f_72e0b4c3d91a5f68c2b7e4` Doc, `f_d15a8c70e3f2b94a61c8d3` Slides, `f_a9ba8abc7d5189babcb378` Sheet (owner Brian; readers Owen, Arthur, Oliver) | parent `d_fc22d5941b2aeb5c03ad32` = Brian root (`/drive_files/22881`) | PASS | REUSED (R3 ledger) |
| 15–18 | gdocs.docs_documents | INSERT | 2 docs, ids = drive ids, non-empty `body_text` | gdocs 633 records scanned, no collision | PASS: carry-over notes `body_text` rewritten (2,234 chars, ASCII); style run `end` 2234 = body length; `f_3ca9e15d…` absent from all 633 docs (this run); ZM notes doc unchanged (144) | NEW (carry-over doc) / REUSED (ZM doc) |
| 20–27 | gsheets.sheets_spreadsheets / sheets_sheets | INSERT | 1 spreadsheet, 3 tabs (Core 15, Live-Ops 9, Mini-Games 4 rows) | gsheets 398 scanned, no collision | PASS (native Sheets row; readable) | REUSED (R3 ledger) |
| 29–54 | gslides.* | INSERT | 1 presentation, 4 pages, 8 elements | gslides 164 scanned, no collision | PASS (native Slides row) | REUSED (R3 ledger) |
| 56–57 | slack.slack_messages | INSERT | `488d87e2…` Arthur→Owen DM, ts 1770937805 (2026-02-12T23:10:05Z) | `D05S1S2AB5M` members incl. Arthur `EMPLOYEE_0025` and Owen `EMPLOYEE_0021` (`slack/channels.json /533`) | PASS: only `text` changed; id absent from 687,230 messages in 5,353 files (this run) | NEW (id, text) / REUSED (channel membership) |
| 58–59 | slack.slack_messages | INSERT | `456afffc…` Marcus Bennett (`EMPLOYEE_0002`), 2025-12-03 | `D05USBTQY1F` members incl. Marcus and Owen (`/599`) | PASS | REUSED (R3 ledger) |
| 60–61 | slack.slack_messages | INSERT | `9bf944b8…` Brian (`EMPLOYEE_0026`), 2025-12-08 | `D07E9PSQB6W` members incl. Brian and Owen (`/806`) | PASS | REUSED (R3 ledger) |
| 62–63 | slack.slack_messages | INSERT reply | `e48eb03d…` Brian, 2025-12-01 | parent `37dc1365…` in `C09Q4S613CN` dd-road-to-sub-250mb (`messages/C09Q4S613CN/2025-11.json /242`); Brian member | PASS | REUSED (R3 ledger) |
| 64–65 | slack.slack_messages | INSERT reply | `d49c2458…` Brian, 2025-12-29 | parent `d25dd8d1…` in `C05V5FNLB9V` god-bugs (`messages/C05V5FNLB9V/2025-12.json /22`) | PASS | REUSED (R3 ledger) |
| 66–85 | slack.slack_messages | INSERT reply ×10 | Vincent (`EMPLOYEE_0012`) replies 2025-11-21/22 on canvas comment roots | parents in `CE156FDFB428` "Bugs on Android 2231" (`messages/CE156FDFB428/2025-11.json` /139, /188, /165, /212, /126, /147, /229, /227, /175, /224); Vincent member | PASS | REUSED (R3 ledger) |
| 86–87 | slack.slack_messages | INSERT reply | `87dc850c…` Marcus, 2025-11-28 | parent `a9665999…` god-bugs (`messages/C05V5FNLB9V/2025-11.json /30`) | PASS | REUSED (R3 ledger) |
| 88–111 | slack.slack_messages | INSERT reply ×12 | GitHub-bot (`SLACK_BOT_0004`) mirrors of the GitHub comments below | parents in `C050WGU41HR` engineering-bots (`2025-11.json` /147, /166, /195, /198, /202, /210, /234, /242; `2025-12.json` /18, /22); bot is a member | PASS | REUSED (R3 ledger) |
| 112–134 | slack.slack_messages | UPDATE ×23 | thread metadata on the 23 parents above | see thread recount table | PASS | REUSED (R3 ledger) |
| 136–175 | github.github_pr_comments / timeline_events | INSERT ×10 each | `#1895#c_3`, `#1898#c_3`, `#1901#c_3`, `#1902#c_3`, `#1903#c_3`, `#1905#c_3`, `#1907#c_2`, `#1908#c_3`, `#1915#c_2`, `#1916#c_2` and matching `ev_N` | PRs exist (GH `/pull_requests/1022…1046`); base comments are `c_1`/`c_2` (or `c_1` only for #1907/#1915/#1916); 884 comments and 12,435 events scanned, no collision | PASS | REUSED (R3 ledger) |
| 176–179 | github.github_review_comments | INSERT ×2 | `#1905#rc_1`, `#1908#rc_1` by Arthur | reviews `#1905#rev_1` (APPROVED 13:05:32Z) and `#1908#rev_1` (APPROVED 01:51:51Z) by `EMPLOYEE_0025_GITHUB_USERNAME`; `commit_id` = each PR's `head_sha`; 1,614 review comments scanned, no collision | PASS | REUSED (R3 ledger) |
| 181–244 | trello.* | INSERT | card `690b2728…d512` "UI optimization pass" (idShort 211), 2 actions, checklist `690b2728…e1d5`, 28 check items | board `65eb4ec5…638f` DD Product Roadmap, list `66c38013…50e3` (name matches), member `d1cd0fef…f068` = Brian Foster; max base idShort on board 210 | PASS: comment action `690b29bc…` text changed to "every one gets a note naming the current public build…"; JSON valid (lint json_shape clean); card/action ids absent from 803 cards / 5,294 actions (this run); badge `comments: 1` still matches | NEW (ids, comment) / REUSED (board, list, member, checklist) |
| 245–250 | trello.* | INSERT | card `68d27e28…502d` "ZM bug list close-outs" (idShort 80), 2 actions | board `6851a656…32ab` ZM ROADMAP, list `68c45122…d16b` Backlog; max base idShort 79 | PASS | REUSED (R3 ledger) |
| 252–271 | gmail.gmail_threads / gmail_messages | INSERT ×5 each | Vincent→Owen mail (Owen INBOX + Vincent SENT copies), 3 calendar invitation mails (Owen, Oliver, Robert) | all mailboxes exist in `gmail/users.json`; thread ids use base `<mailbox>/<decimal>` form; all 8 thread/message identifiers absent from all 88,726 thread files (`rg` exit 1) | PASS | REUSED (R3 ledger) |
| 273–280 | gcal.gcal_events | INSERT ×4 | "DD bug review" on Arthur/Robert/Oliver/Owen calendars, 2026-02-15 17:00–17:30Z | calendars exist (`gcal/data.json /calendars`); event ids and `ical_uid` unused (11,130 events) | PASS | REUSED (R3 ledger) |
| 282–307 | linear.linear_comments | INSERT ×13 | comments on ENG-2401, 2363, 2428, 2437, 2429, 2410, 2430, 2280, 2281, 2398, 2181, 2351, 2406 | issues exist by `id` (`linear/data.json /issues`); authors Arthur `usr_cc3e…`, Vincent `usr_65c7…`, Oliver `usr_bdf0…`, Brian `usr_fc22…`; base `/comments` is empty, so no collision possible | PASS | REUSED (R3 ledger) |
| 308–320 | linear.linear_issues | UPDATE ×13 | `updated_at` set to each new comment's time | every new value is later than the base `updated_at` (e.g. ENG-2401 2025-11-04T18:10:01Z → 2026-02-13T00:40:00Z; ENG-2429 2025-11-18T17:51:59Z → 2025-11-19T14:27:00Z) | PASS | REUSED (R3 ledger) |

### Slack thread recount (base replies + SQL replies vs SQL UPDATE), REUSED from R3 (lines 58–134 unchanged)

All 23 match exactly on `thread_ts_legacy` = parent ts, `reply_count`, `reply_users_count` and `latest_reply`. Examples: `d25dd8d1` 60 base + 1 new = 61, 3 users, latest 1767021345.207719; `50de5b6f` 4 + 2 = 6, 1 user, latest stays base 1763557543.301089; `dfb3bc5e` 4 + 1 = 5, latest stays base 1763077285.311909. Every new reply has the parent's channel and `thread_ts_legacy`, a later ts than its parent, and a `ts` equal to its `created_at` (all 28 checked).

## 6. Check results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | Changed records (NEW): `d_9b41e7c2…` and `f_3ca9e15d…` absent from all 53,866 `gdrive/data.json /drive_files`; `f_3ca9e15d…` absent from all 633 `gdocs/data.json /docs_documents` (`document_id`); `690b2728…d512` and `690b29bc…` absent from all 803 `/cards` and 5,294 `/actions` in `trello/data.json`; `488d87e2…` absent from 687,230 Slack messages in 5,353 files. All scans complete, no errors. Actors and parents of changed rows are unchanged (Owen root `/drive_files/7047`, Arthur root `/drive_files/18538`, DM `D05S1S2AB5M` members Arthur + Owen, Trello member `d1cd0fef…` = Brian Foster). Unchanged records: REUSED from R3 §6 A (full collision coverage over Slack, Drive, GitHub, Trello, Gcal, Gmail, Docs/Sheets/Slides; one account per person; ID contracts; Drive readability). |
| B — SQL structure and supported schema rules | PASS | Lint parse of the whole revision-4 file (NEW): 174 statements, balanced transaction, column/value counts match, quoting/escaping well formed (`''` and `E'…\n'` in the rewritten doc), JSON columns valid and in base shape (incl. rewritten Trello `data_json`), no generated columns set, Linear dates in base format, NOT NULL columns supplied. The line-1 `--` comment sits before `BEGIN` and is valid SQL. Provisional snapshot comparison REUSED: Advisory 1. |
| C — Dates, relationships and consistency | PASS | NEW: folder now created 2026-02-12T23:00:00Z, before Arthur's DM (23:10:05Z) that says "Put a sheet in your DD bug carry-over folder", so R3 Advisory 2 is resolved; doc (22:48Z) still precedes the DM's "carry-over notes doc I shared with you". Rewritten doc style run covers exactly 2,234 chars = body length. Doc's "Brian's closing rule from the UI work applies to the line on every child, Done or not" matches Brian's 2025-11-05 Trello comment ("every one gets a note naming the current public build") and the DM's "leave a line on every child saying where it landed"; no other injected record quotes the old wording ("build it was checked on"), so no stale copy is left behind (grep of whole SQL). The doc's new rules ("A design question for Leonard isn't a bug post", "or the screen is switched off there", "one per canvas line and one per bug posted after it, even where two read alike", "nothing in the description") are instructions, not factual claims; nothing in the SQL contradicts them. No grader-facing text in the changed records. Unchanged records: REUSED from R3 §6 C (all event times ≤ clock, only Gcal 2026-02-15 plan fields later; GitHub/Slack chronology; 28 UI children = 15 + 9 + 4; Trello badges; stale Slides/Trello ticks contradicted by later dated records = supported context). |

## 7. Findings

No demonstrated defects.

### Advisories (not failing)

1. **Columns not in the schema snapshot or the base export (B, provisional NOT COVERED), carried from R3.** `gslides.slides_pages.notes` (lines 32–50), `gslides.slides_page_elements.ordinal`, `.table_json` (lines 34–54), `github.github_review_comments.pull_request_review_id`, `.side`, `.subject_type`, `.seq` (lines 177, 179). The snapshot is unverified, so this is a compatibility limit, not a defect. Because the script is one transaction, a missing column on the live database would roll back every record. Smallest safe change: drop those 7 columns from the column lists and values (all NULL, constants, or data the base export doesn't show).
2. **Cached Trello board activity, carried from R3.** DD Product Roadmap's `dateLastActivity` (2025-10-10) predates the injected UI card's activity (2025-11-05 to 2025-11-21). Cached field with unknown semantics; not a defect.
3. **R3 Advisory 2 (folder created after it was referenced) is resolved** by the new 23:00Z timestamps.

## 8. Evidence limits (outside certification scope)

- Live execution, current database compatibility and undocumented constraints are not certified (schema snapshot unverified; Advisory 1).
- Trello board membership isn't in the export; Brian is a workspace member (`/members/9`).
- GitHub PR file lists aren't exported, so review-comment `path` values can't be matched to changed files.
- Agent visibility, discoverability and difficulty belong to `/prompt` and `/hardness`. The doc's new rules point at records `/prompt` should confirm exist and that Owen can see: which bug-channel post is "a design question for Leonard", and which record shows a screen "switched off" in 0.3.310. As in R3, the only base record of build 0.3.310 is Leonard's 2026-02-11 DM to Arthur (`messages/D04UGG61DUM/2026-02.json /103`), which Owen can't see; the doc states it directly.

## 9. Stage provenance (for reuse)

Static checks A–C depend on: SQL SHA `be13a93a…50d9`; universe manifest SHA `5e01ac44…e450`; schema snapshot SHA `31dcb2b4…5151`; id_contracts SHA `fc4711ef…4682`; lint `injection-lint-v1`; clock 2026-02-14 00:00 UTC. Reused items come from R3 report SHA `a3d4b779…69bf` §5 ledger rows (lines 8–13, 20–54, 58–179, 188–320 and the unchanged references of lines 4–7, 56–57, 181–244), the §5 Slack thread recount and §6 A/B/C unchanged-record evidence. Each covers statements that are byte-identical in revision 4 (verified by full diff), with every reference fingerprint, the base manifest and the clock unchanged. Changed lines 1, 5, 16, 57 and 186 were re-verified NEW. A changed SQL version invalidates this report.

## 10. Next action

Proceed to `/prompt`. If you take up Advisory 1, the edited SQL needs `/injection` again first.

### FINAL VERDICT: PASS

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (runtime does not report the effort level)

Next action: Proceed to /prompt

Evidence limits: Static scope only; schema snapshot unverified (7 columns NOT COVERED, Advisory 1); live load, Agent visibility and difficulty not certified.
