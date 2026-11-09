# /injection: Injection data-integrity review

## 1. Scope

| Item | Value |
|---|---|
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`, `ruthless-grading-v1`) |
| Mode | Chat review, attempt workspace (no task-folder preflight) |
| Actual review time | 2026-11-07T19:57Z |
| Clock | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal/`, manifest `Evals/references/universes/normal/universe_manifest.json` SHA-256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Reviewed input | `Evals/task_inputs/01_Universe_Inject.sql` (revision 8, 87,726 bytes, 346 lines) SHA-256 `2ebfcae230b0666433d8c1c0924bd0d9a742807ac964280c5b89e9ef0ae1d0b6`, user attachment `01_Universe_Inject (5).sql` |
| Previous version | Revision 7, SHA-256 `a610e7a5…4dfc`, reviewed PASS / COMPLETE in report SHA-256 `81c50e16dfb4170377c20867d4e78b1e0797f81d5fccf3ff33edcac123141342` ("R7 report"), which carried R6 (`6e01f45b…82b6`), R4 (`efe75aaf…54e5a0`) and R3 (`a3d4b779…69bf`) evidence |
| References | Eval 0 SHA `e034019b…6eff`; WORKFLOW SHA `ee4cd8e1…fd5d`; schema snapshot `injection.json` SHA `31dcb2b4…5151` (unverified); `id_contracts.json` SHA `fc4711ef…4682`; Slack `channels.json` `476eaa6d…`; Trello `data.json` `aefef82b…`. All recomputed this run; Eval/WORKFLOW/schema/id-contract/manifest hashes equal R7's |
| Lint | `hg_injection_lint.py` `injection-lint-v1`: 188 statements (1 BEGIN, 147 INSERT, 39 UPDATE, 1 COMMIT); FAIL 0 / CHECK 0 / INFO 0 |
| Reused evidence | Yes, only for statements byte-identical to revision 7 (see §2, §5, §9) |

## 2. Input / authority issues

None. The SQL is substantive and runs as one transaction (`BEGIN` line 2 … `COMMIT` line 346). The line-1 comment ("Are you planning to inject? Yes") is a template answer, not grader-facing or padding text.

**Changes from revision 7** (full `diff`, three hunks only):

| Hunk | Rev-8 lines | Change |
|---|---|---|
| `76a77,84` | 76–83 | 4 new `slack.slack_messages` `channel_leave` rows for Owen (`EMPLOYEE_0021_SLACK_ID`) in `CE156FDFB428`, `C09Q4S613CN`, `C05433XK267`, `C09SWTHEMEW`, 2026-02-11T20:41:12–15Z |
| `78a87,94` | 86–93 | 4 new `channel_join` rows for Owen in the same four channels, 2026-02-12T22:41:27Z–22:42:36Z (two of these ids, `b8b079a1…`, `300958649…`, are the rows removed in rev 7, now paired with a leave) |
| `189c205` | 204–205 | `trello.trello_cards` `690b27282f4c1b7a6e93d512` `dateLastActivity` `2025-11-05T10:41:00Z` → `2025-11-21T15:30:00Z`; every other value identical |

Line mapping for unchanged statements: rev-7 lines 1–75 are the same; rev-7 76–77 → 84–85; rev-7 78–79 → 94–95; rev-7 line n ≥ 80 → n + 16.

## 3. Checklist

- [x] Save/reload SQL; hash, base manifest and review version recorded (NEW)
- [x] Lint run; every flag resolved, none raised (NEW)
- [x] Inventory of every statement and record (NEW for the 9 changed statements; unchanged rows REUSED from the R7 §5 ledger with renumbered lines)
- [x] Check A: references and new-key collisions (NEW full Slack lookup for all 8 changed-row ids; REUSED for the rest)
- [x] Check B: SQL structure and supported schema rules (NEW lint parse of the whole file; REUSED provisional snapshot comparison)
- [x] Check C: dates, relationships and facts in the combined state (NEW: Owen's full join/leave history across all base channels, ts/created_at for all 39 Slack inserts, base ts collisions, Trello `dateLastActivity` convention; REUSED for the rest)
- [x] Coverage, findings, limits and one final verdict (NEW)

## 4. Lint flags and resolutions

| Flag | Result | Resolution |
|---|---|---|
| future_date, id_contract, drive_unreadable, identities/duplicate_account, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape | 0 flags | Consistent with independent checks: the 8 new Slack rows are dated 2026-02-11/12 (≤ clock); the new Trello date 2025-11-21T15:30:00Z ≤ clock; the new rows set no generated/FTS column, use `metadata_json '{}'` and `'[]'` list fields (base shape), and `EMPLOYEE_0021_SLACK_ID` is Owen's single existing Slack account. Unchanged rows as R7 §4. The lint does not test membership history or Trello activity semantics, so those were checked by hand (§6 C). |

## 5. Operation ledger

Base paths: Slack = `Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/slack/`; Trello = `…/Other_Services/Services_Data/trello/data.json`; Linear = `…/Other_Services/Services_Data/linear/data.json`; GH = `Universe_Normal/Normal_HarmonyGames_GitHub/Services_Data/github/data.json`. "REUSED (R7)" = same row in the R7 report §5 (and through it R6/R4/R3), statement byte-identical, all dependencies unchanged (§9). Lines are revision-8 line numbers.

| SQL lines | Table | Op | Records | References resolved (path/pointer) | Result | Verification |
|---|---|---|---|---|---|---|
| 4–13 | gdrive.drive_files | INSERT ×5 | folder `d_9b41e7c2…` (Owen), Doc `f_3ca9e15d…` (Arthur), Doc `f_72e0b4c3…`, Slides `f_d15a8c70…`, Sheet `f_a9ba8abc…` (Brian) | parents = Owen root `/drive_files/7047`, Arthur root `/18538`, Brian root `/22881`; ids absent from 53,866 drive_files | PASS | REUSED (R7) |
| 15–18 | gdocs.docs_documents | INSERT ×2 | carry-over notes, ZM notes | id = drive id; absent from 633 docs; non-empty `body_text` | PASS | REUSED (R7) |
| 20–27 | gsheets.* | INSERT | 1 spreadsheet, 3 tabs | 398 spreadsheets, no collision | PASS | REUSED (R7) |
| 29–54 | gslides.* | INSERT | 1 presentation, 4 pages, 8 elements | 164 presentations, no collision | PASS (Advisory 1) | REUSED (R7) |
| 56–75 | slack.slack_messages | INSERT ×10 | Arthur→Owen DM `488d87e2…`; Marcus DM; Brian DM + reply; god-bugs reply; Robert reply; 4 Vincent replies | as R7 rows 56–75 | PASS | REUSED (R7) |
| 76–77 | slack.slack_messages | INSERT `channel_leave` | `e3e5bf78…` Owen leaves `CE156FDFB428`, ts 1770842472.100349 = 2026-02-11T20:41:12Z, text "has left the conversation" | channel `channels.json /359` (Owen listed member); base has no Owen join/leave there; no base ts collision | PASS (Advisory 5) | NEW |
| 78–79 | slack.slack_messages | INSERT `channel_leave` | `d38307a8…` Owen leaves `C09Q4S613CN` 2026-02-11T20:41:13Z | `/145` member; base join 2025-11-02T01:01:43Z (`messages/C09Q4S613CN/2025-11.json /10`), no base leave | PASS | NEW |
| 80–81 | slack.slack_messages | INSERT `channel_leave` | `0cc44f9d…` Owen leaves `C05433XK267` builds 2026-02-11T20:41:14Z | `/25` member; base join 2023-09-15T06:27:46Z (`messages/C05433XK267/2023-09.json /228`), no base leave | PASS | NEW |
| 82–83 | slack.slack_messages | INSERT `channel_leave` | `186107ee…` Owen leaves `C09SWTHEMEW` 2026-02-11T20:41:15Z | `/149` member; base join 2025-12-17T20:59:01Z (`messages/C09SWTHEMEW/2025-12.json /44`), no base leave | PASS | NEW |
| 84–85 | slack.slack_messages | INSERT `channel_join` | `c399a0bd…` Owen rejoins god-bugs `C05V5FNLB9V` 2026-02-12T22:41:03Z | base join 2023-10-07, base leave 2026-02-11T20:41:10Z (`2026-02.json /2`) | PASS | REUSED (R7 76–77), history re-scanned NEW |
| 86–87 | slack.slack_messages | INSERT `channel_join` | `b8b079a1…` Owen rejoins `CE156FDFB428` 2026-02-12T22:41:27Z, "has joined the conversation" | preceded by injected leave line 77 | PASS (Advisory 5) | NEW |
| 88–89 | slack.slack_messages | INSERT `channel_join` | `300958649…` Owen rejoins `C09Q4S613CN` 2026-02-12T22:41:49Z | preceded by injected leave line 79 | PASS | NEW |
| 90–91 | slack.slack_messages | INSERT `channel_join` | `a93fda6f…` Owen rejoins `C05433XK267` 2026-02-12T22:42:12Z | preceded by injected leave line 81 | PASS | NEW |
| 92–93 | slack.slack_messages | INSERT `channel_join` | `ef892f6e…` Owen rejoins `C09SWTHEMEW` 2026-02-12T22:42:36Z | preceded by injected leave line 83 | PASS | NEW |
| 94–95 | slack.slack_messages | INSERT `channel_join` | `8b1af0fc…` Owen rejoins engineering-bots `C050WGU41HR` 2026-02-12T22:42:58Z | base join 2023-09-15, base leave 2026-02-11T20:41:09Z (`2026-02.json /4`) | PASS | REUSED (R7 78–79), history re-scanned NEW |
| 96–107 | slack.slack_messages | INSERT reply ×6 | Vincent replies 2025-11-21 | as R7 | PASS | REUSED (R7 80–91) |
| 108–109 | slack.slack_messages | INSERT reply | `87dc850c…` Marcus, god-bugs | parent `a9665999…` | PASS | REUSED (R7 92–93) |
| 110–129 | slack.slack_messages | INSERT reply ×10 | GitHub-bot mirrors of PR comments | ts = `created_at` = matching `github_pr_comments.created_at` (lines 159–198) | PASS | REUSED (R7 94–113) |
| 130–133 | slack.slack_messages | INSERT reply ×2 | `ea8f1a2d…`, `52eafc2b…` | ts = review-comment `created_at` (lines 199–202) | PASS (Advisory 3) | REUSED (R7 114–117) |
| 134–157 | slack.slack_messages | UPDATE ×24 | thread metadata | R7/R6 recount; none of the 8 new rows is a reply | PASS | REUSED (R7 118–141) |
| 159–198 | github pr_comments / timeline_events | INSERT ×10 each | as R7 | PRs and ids as R7 | PASS | REUSED (R7 143–182) |
| 199–202 | github.github_review_comments | INSERT ×2 | `#1905#rc_1`, `#1908#rc_1` | reviews `/reviews/1046`, `/1048` | PASS (Advisories 1, 3) | REUSED (R7 183–186) |
| 204–205 | trello.trello_cards | INSERT | `690b27282f4c1b7a6e93d512` "UI optimization pass", `dateLastActivity` **2025-11-21T15:30:00Z** (changed) | id absent from 803 base cards (re-confirmed); actions on the card: createCard 2025-11-05T10:30:00Z (line 207), commentCard 2025-11-05T10:41:00Z (line 209); check items carry no dates | PASS: later than the last exported action, ≥ creation, ≤ clock; base convention allows this (§6 C) | NEW (date); other values REUSED (R7 188–189) |
| 206–267 | trello.* | INSERT | 2 actions, checklist, 28 items | as R7 | PASS | REUSED (R7 190–251) |
| 268–273 | trello.* | INSERT | ZM card + 2 actions | as R7 | PASS | REUSED (R7 252–257) |
| 275–294 | gmail.* | INSERT ×5 each | as R7 | `history_id` NULL | PASS | REUSED (R7 259–278) |
| 296–303 | gcal.gcal_events | INSERT ×4 | as R7 (2026-02-15 start/end are plan fields) | as R7 | PASS | REUSED (R7 280–287) |
| 305–330 | linear.linear_comments | INSERT ×13 | as R7 | base `/comments` empty | PASS | REUSED (R7 289–314) |
| 331–343 | linear.linear_issues | UPDATE ×13 | `updated_at` = each new comment's time | as R7 | PASS | REUSED (R7 315–327) |
| 344–345 | linear.linear_issues | UPDATE ×2 | ENG-2403/2404 `description` → NULL, `updated_at` → 2026-02-12T22:30:00Z | `/issues/2340`, `/2341` | PASS | REUSED (R7 328–329) |

### Slack thread recount

Unchanged from R7/R6: all 24 UPDATEs match base replies + SQL replies. The 8 new rows are top-level membership events (`thread_parent_id` NULL, `reply_count 0`), so no count changes.

## 6. Check results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | NEW `lookup` of all 8 changed-row ids over `slack messages/*/*.json`: 0 matches, 687,230 records / 5,353 files, `scan_complete: true`, no errors. No duplicate ids among the 39 SQL Slack inserts. Owen (`EMPLOYEE_0021_SLACK_ID`, existing single account) is a listed member of all six affected channels: `C050WGU41HR` `/21`, `C05433XK267` `/25`, `C05V5FNLB9V` `/53`, `C09Q4S613CN` `/145`, `C09SWTHEMEW` `/149`, `CE156FDFB428` `/359` (`channels.json` SHA `476eaa6d…`, equal to the route map's source hash). Trello card id re-confirmed absent from 803 base cards. All other ids, actors, parents, ID contracts and Drive readability REUSED from R7 §6 A. |
| B — SQL structure and supported schema rules | PASS | NEW lint parse of all 188 statements: balanced transaction, column/value counts match, quoting well formed, JSON valid and base-shaped, no generated columns, NOT NULL columns supplied. New rows use the same 18-column list as the existing Slack inserts. Provisional snapshot comparison REUSED: Advisory 1. |
| C — Dates, relationships and consistency | PASS | NEW full scan of Owen's `channel_join`/`channel_leave` events across every Slack channel file: the base bulk leave at 2026-02-11T20:41:09–11Z covers `C04V7N09LE7`, `C050WGU41HR`, `C05KNDCHAAG`, `C05V5FNLB9V`, `C0880U9751A`, `C08R27X0EAH`; the four injected leaves continue that sequence at 20:41:12–15Z in channels where Owen was a member and had no prior leave. Each of the six rejoins (lines 84–95) now follows a leave. No Owen-authored message exists in the four channels after 2026-02-11T20:41 in the base or the SQL, so nothing contradicts his absence before the rejoin. All 39 Slack inserts have `ts` = `created_at` (NEW parse); none of the 8 new ts values collides with a base ts in its channel. Trello: `dateLastActivity` 2025-11-21T15:30:00Z is later than the card's last exported action (2025-11-05T10:41:00Z); in the base, 162 of 796 cards with actions also have `dateLastActivity` later than their newest exported action (624 equal, 10 earlier), so this is a supported representation (e.g. unexported checklist ticks: 27 of 28 items complete), not a defect. Rest REUSED from R7 §6 C. |

## 7. Findings

No failing findings.

**C1 (from R6), still resolved.** R6 failed the Owen joins in `CE156FDFB428` and `C09Q4S613CN` because he had never left those channels. Revision 7 removed them; revision 8 restores them together with matching earlier leaves, so every injected join now follows a leave. Verified by full history scan (§6 C).

### Advisories (not failing)

1. **Columns not in the schema snapshot or the base export (B, provisional NOT COVERED), carried.** `gslides.slides_pages.notes`, `gslides.slides_page_elements.ordinal`, `.table_json`, `github.github_review_comments.pull_request_review_id`, `.side`, `.subject_type`, `.seq` (lines 31–54, 199–202). Snapshot unverified, so this is a compatibility limit, not a defect. The script is one transaction, so a missing column on the live database would roll back every record. To be safe, drop those 7 columns and their values.
2. **Cached Trello board activity, carried.** DD Product Roadmap's `dateLastActivity` (2025-10-10) predates the injected card's activity (now 2025-11-21). Cached field with unknown semantics.
3. **Review-comment timing (minor), carried.** Both review comments are 3–4 s after their review's `submitted_at`. Not a defect; aligning them to the review time (and the bot mirrors on lines 131/133) would remove the oddity.
4. **Partial rejoin (informational, updated).** The base bulk leave plus the injected leaves cover 10 channels; the SQL rejoins Owen to 6 (god-bugs, engineering-bots, builds, dd-road-to-sub-250mb, the publishing channel, the Android-bugs canvas channel). `C04V7N09LE7`, `C05KNDCHAAG`, `C0880U9751A`, `C08R27X0EAH` stay left. Consistent with the DM's "one of the paid seats so you can read the DD channels".
5. **Membership events in a canvas comment channel (minor, new).** `CE156FDFB428` ("FC:F09GAFM2DRR:Bugs on Android…", `created 0`) is a canvas comment channel. None of the base's 28 `FC:` channels has any `channel_join`/`channel_leave` event, and lines 77/87 use "left/joined the conversation" where base uses "the channel". This is not an incompatible fact (Owen is a listed member and the leave precedes the join), so it does not fail. If you don't need Owen's access to that canvas channel to change, dropping both rows (lines 76–77 and 86–87) is the cleanest option.

## 8. Evidence limits (outside certification scope)

- Live execution, current database compatibility and undocumented constraints are not certified (schema snapshot unverified; Advisory 1).
- Trello board membership and checklist-state history aren't exported. GitHub PR file lists aren't exported, so review-comment `path` values can't be matched to changed files.
- Agent visibility, discoverability and difficulty belong to `/prompt` and `/hardness`. Notes carried for `/prompt`: the only base record of build 0.3.310 is Leonard's DM to Arthur (`D04UGG61DUM/2026-02.json /103`), which Owen can't see; blanking ENG-2403/2404 removes the checklist hints from the two masters. New for `/prompt`: Owen's injected leave/rejoin means he was out of builds, the publishing channel, dd-road-to-sub-250mb and the canvas channel from 2026-02-11T20:41Z to 2026-02-12T22:41Z; how membership affects history reads is a visibility question for `/prompt`.

## 9. Stage provenance (for reuse)

Static checks A–C depend on: SQL SHA `2ebfcae2…d0b6`; universe manifest SHA `5e01ac44…e450`; schema snapshot SHA `31dcb2b4…5151`; id_contracts SHA `fc4711ef…4682`; lint `injection-lint-v1`; clock 2026-02-14 00:00 UTC. Reused items come from the R7 report (SHA `81c50e16…1342`) §5 ledger rows, §5 thread recount and §6 A/B/C evidence for unchanged statements, carrying R6 (`6e01f45b…82b6`), R4 (`efe75aaf…54e5a0`) and R3 (`a3d4b779…69bf`). Each reused item covers a statement byte-identical to revision 7 (verified by full diff: only hunks `76a77,84`, `78a87,94`, `189c205`), with the base manifest, reference hashes and clock recomputed and unchanged. Re-checked NEW: Slack id lookup (5,353 files, complete), Owen's join/leave history across all channel files, `channels.json` (`476eaa6d…`), Slack files `messages/CE156FDFB428/2025-11.json` (`9ad33c35…`), `messages/C09Q4S613CN/2025-11.json` (`2d0817b9…`), `messages/C05433XK267/2023-09.json` (`88991471…`), `messages/C05433XK267/2026-02.json` (`288b7c1e…`), `messages/C09SWTHEMEW/2025-12.json` (`3d3f4bfc…`), `messages/C09SWTHEMEW/2026-02.json` (`78dba474…`), and Trello `data.json` (`aefef82b…`, cards/actions). This PASS / COMPLETE report can be reused by `/prompt` for the static checks while the SQL hash and dependencies above match.

## 10. Next action

Run `/prompt`, then `/hardness`. Both read the injection SQL, so any earlier pass on them is outdated. `/oe` and `/rubric` also read the SQL and need rerunning after those.

### FINAL VERDICT: PASS

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (runtime does not report the effort level)

Next action: Run /prompt, then /hardness (both read the changed injection SQL); then /oe and /rubric

Evidence limits: Static scope only; live deployment and current schema compatibility not certified (snapshot unverified, Advisory 1); Agent visibility and difficulty belong to /prompt and /hardness
