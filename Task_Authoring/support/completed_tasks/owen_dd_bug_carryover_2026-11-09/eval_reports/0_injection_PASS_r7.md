# /injection: Injection data-integrity review

## 1. Scope

| Item | Value |
|---|---|
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`, `ruthless-grading-v1`) |
| Mode | Chat review, attempt workspace (no task-folder preflight) |
| Actual review time | 2026-11-07 (session date), after the revision-11 save |
| Clock | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal/`, manifest `Evals/references/universes/normal/universe_manifest.json` SHA-256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Reviewed input | `Evals/task_inputs/01_Universe_Inject.sql` (revision 11, 90,399 bytes, 355 lines) SHA-256 `f9555a3cf6fcbbc649e18ee842a75ad00ea7da4cfe3071210a65b3e3ca26cadd`, user attachment `01_Universe_Inject (7).sql` |
| Previous version | Revision 10, SHA-256 `7e1d0b11…0c2c` (attachment `(6)`), reviewed PASS / COMPLETE in report SHA-256 `c46e263ecd7250a4ee8ffcf3551e6ef47670d1f459f79879998f5eb7cc674bef` ("R10 report"), which carried R8 (`7388c979…3eed`), R7, R6, R4 and R3 evidence |
| References | Eval 0 SHA `e034019b…6eff` (unchanged, re-read in full); WORKFLOW SHA `d5702ee2…3e33` (**changed** from R10's `ee4cd8e1…fd5d`; injection guide sections re-read this run); scoring.json `c14873e6…e5bc`; schema snapshot `injection.json` `31dcb2b4…5151` (unverified, unchanged); `id_contracts.json` `fc4711ef…4682` (unchanged); Slack `channels.json` `476eaa6d…` and `users.json` `6aac5103…` (unchanged) |
| Lint | `hg_injection_lint.py` `injection-lint-v1` on SHA `f9555a3c…dcadd`: 193 statements (1 BEGIN, 151 INSERT, 40 UPDATE, 1 COMMIT); FAIL 0 / CHECK 0 / INFO 0 |
| Reused evidence | Yes, only for statements byte-identical to revision 10 (see §2, §5, §9) |

## 2. Input / authority issues

None. The SQL is substantive and runs as one transaction (`BEGIN` line 2 … `COMMIT` line 355). The line-1 comment is a template answer, not grader-facing or padding text.

**Changes from revision 10** (full `diff` of attachment `(6)` vs `(7)`, two hunks):

| Hunk | Rev-11 lines | Change |
|---|---|---|
| `82a83,84` | 83–84 | 1 new `slack.slack_messages` reply `948d64b2f42b443b0e509a0c66a03e3c` by Vincent Parker (`EMPLOYEE_0012_SLACK_ID`) in `CE156FDFB428`, thread `ef80c659…` (canvas line "☑ navigation bar tooltips"), ts `1763845512.559339` = 2025-11-22T21:05:12Z: "checked Brian's second fix, the 1 pixel gap is gone and the tooltips look right on my android now" |
| `146a149` | 149 | 1 new `UPDATE slack.slack_messages` on parent `ef80c659…`: `thread_ts_legacy '1763394941.178509'`, `reply_count 7`, `reply_users_count 3`, `latest_reply '1763845512.559339'` |

Line mapping for unchanged statements: rev-10 lines 1–82 are the same; rev-10 lines 83–146 → +2 (85–148); rev-10 lines 147–352 → +3 (150–355).

**WORKFLOW change:** WORKFLOW.md's hash differs from the R10 dependency. The injection-applicable sections (input contract, save/reuse, stage evidence reuse, ruthless standard, report contents, verdict block, invalidation) and the injection scoring group were re-read via `hg_reference.py guide injection`; Eval 0, the schema snapshot and id_contracts are unchanged. No re-read rule adds an injection check that the reused rows did not already cover, so reuse of unchanged-statement evidence stays valid (§9).

## 3. Checklist

- [x] Save/reload SQL; hash, base manifest and review version recorded (NEW)
- [x] Lint run; every flag resolved, none raised (NEW, whole file)
- [x] Inventory of every statement and record (NEW for the 2 added statements; unchanged rows REUSED from the R10 §5 ledger with renumbered lines)
- [x] Check A: references and new-key collisions (NEW full Slack id lookup for the new id; NEW SQL-wide id and (channel, ts) uniqueness over all 43 Slack inserts; NEW parent/thread resolution; REUSED for the rest)
- [x] Check B: SQL structure and supported schema rules (NEW lint parse of the whole file; REUSED provisional snapshot comparison)
- [x] Check C: dates, relationships and facts in the combined state (NEW: full base thread read, recount, chronology against Brian's promise and Android builds, scan of Slack 2025-11 onward for later contrary statements, Vincent's departure date; REUSED for the rest)
- [x] Coverage, findings, limits and one final verdict (NEW)

## 4. Lint flags and resolutions

| Flag | Result | Resolution |
|---|---|---|
| future_date, id_contract, drive_unreadable, identities/duplicate_account, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape | 0 flags | Consistent with independent checks: the new reply is dated 2025-11-22 (≤ clock); it sets no generated/FTS column; `metadata_json '{}'` and `'[]'` list fields match base shape; `EMPLOYEE_0012_SLACK_ID` is Vincent Parker's single Slack account and already authors 2 base replies in this same thread; text is in-world. The new UPDATE sets only thread metadata. Unchanged rows as R10 §4. |

## 5. Operation ledger

Base paths: Slack = `Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/slack/`; Trello = `…/Other_Services/Services_Data/trello/data.json`; Linear = `…/Other_Services/Services_Data/linear/data.json`; GH = `Universe_Normal/Normal_HarmonyGames_GitHub/Services_Data/github/data.json`. "REUSED (R10)" = same row in the R10 report §5 (and through it R8/R7/R6/R4/R3), statement byte-identical, all dependencies unchanged (§9). Lines are revision-11 line numbers.

| SQL lines | Table | Op | Records | References resolved (path/pointer) | Result | Verification |
|---|---|---|---|---|---|---|
| 4–13 | gdrive.drive_files | INSERT ×5 | folder `d_9b41e7c2…` (Owen), Doc `f_3ca9e15d…` (Arthur), Doc `f_72e0b4c3…`, Slides `f_d15a8c70…`, Sheet `f_a9ba8abc…` (Brian) | parents = Owen root `/drive_files/7047`, Arthur root `/18538`, Brian root `/22881`; ids absent from 53,866 drive_files | PASS | REUSED (R10 4–13) |
| 15–18 | gdocs.docs_documents | INSERT ×2 | carry-over notes, ZM notes | id = drive id; absent from 633 docs; non-empty `body_text` | PASS | REUSED (R10 15–18) |
| 20–27 | gsheets.* | INSERT | 1 spreadsheet ("UI pass tracker"), 3 tabs | 398 spreadsheets, no collision | PASS | REUSED (R10 20–27) |
| 29–54 | gslides.* | INSERT | 1 presentation, 4 pages, 8 elements | 164 presentations, no collision | PASS (Advisory 1) | REUSED (R10 29–54) |
| 56–62 | slack.slack_messages | INSERT ×3 | Arthur→Owen DM; Marcus→Owen DM (2025-12-11T11:20:12Z); Brian→Owen DM (2025-12-08T15:10:44Z) | as R10 | PASS | REUSED (R10 56–62) |
| 63–68 | slack.slack_messages | INSERT ×3 | Brian, `D07E9PSQB6W`, 2025-12-11T16:42:31Z / 16:44:07Z / 16:46:03Z (Tavern regression, Apple sync = ENG-2073, two popups) | `channels.json /806`; ids absent; no ts collision | PASS | REUSED (R10 63–68) |
| 69–81 | slack.slack_messages | INSERT ×7 | god-bugs replies `e48eb03d…`, `d49c2458…`, `70692cd0…`; 4 Vincent replies in `CE156FDFB428` (2025-11-21T16:20:12Z, 2025-11-22T21:00:12Z, 21:10:12Z, 21:11:12Z) | as R10 | PASS | REUSED (R10 69–81) |
| **83–84** | slack.slack_messages | INSERT reply | `948d64b2f42b443b0e509a0c66a03e3c`, Vincent (`EMPLOYEE_0012_SLACK_ID`), `CE156FDFB428`, ts `1763845512.559339` = `created_at` 2025-11-22T21:05:12Z, `thread_parent_id ef80c659e26c08225ceeb4f7a9f97d42`, `thread_ts_legacy 1763394941.178509` | parent `CE156FDFB428/2025-11.json /152` (`document_comment_root` "☑ navigation bar tooltips", `thread_ts 1763394941.178509`); id absent from 687,230 base Slack records; ts absent from the channel's 272 base records; no SQL duplicate | PASS | NEW |
| 84–91 | slack.slack_messages | INSERT `channel_leave` ×4 | Owen leaves `CE156FDFB428`, `C09Q4S613CN`, `C05433XK267`, `C09SWTHEMEW`, 2026-02-11T20:41:12–15Z | as R10 | PASS (Advisory 5) | REUSED (R10 82–89) |
| 92–103 | slack.slack_messages | INSERT `channel_join` ×6 | Owen rejoins `C05V5FNLB9V`, `CE156FDFB428`, `C09Q4S613CN`, `C05433XK267`, `C09SWTHEMEW`, `C050WGU41HR`, 2026-02-12T22:41:03–22:42:58Z | as R10 | PASS (Advisories 4, 5) | REUSED (R10 90–101) |
| 104–115 | slack.slack_messages | INSERT reply ×6 | Vincent replies 2025-11-21 (`1ccf4d66…`, `8240272f…`, `ea0a6b8a…`, `063efe55…`, `d9ee1b37…`, `2c76e592…`) | as R10 | PASS | REUSED (R10 102–113) |
| 116–117 | slack.slack_messages | INSERT reply | `87dc850c…` Marcus, god-bugs | parent `a9665999…` | PASS | REUSED (R10 114–115) |
| 118–137 | slack.slack_messages | INSERT reply ×10 | GitHub-bot mirrors of PR comments | ts = matching `github_pr_comments.created_at` | PASS | REUSED (R10 116–135) |
| 138–141 | slack.slack_messages | INSERT reply ×2 | `ea8f1a2d…`, `52eafc2b…` | ts = review-comment `created_at` | PASS (Advisory 3) | REUSED (R10 136–139) |
| 142–148 | slack.slack_messages | UPDATE ×7 | thread metadata (`37dc1365…` … `55a5f61f…`) | R10 recount | PASS | REUSED (R10 140–146) |
| **149** | slack.slack_messages | UPDATE | parent `ef80c659…`: `reply_count` 6→7, `reply_users_count` 3→3, `latest_reply` `1763748462.772499`→`1763845512.559339`, `thread_ts_legacy` = base `thread_ts` | `CE156FDFB428/2025-11.json /152`; recount below | PASS | NEW |
| 150–166 | slack.slack_messages | UPDATE ×17 | thread metadata (`3f6d03da…` … `f36b5099…`) | R10 recount; none involves `ef80c659…` | PASS | REUSED (R10 147–163) |
| 168–207 | github pr_comments / timeline_events | INSERT ×10 each | as R10 | PRs and ids as R10 | PASS | REUSED (R10 165–204) |
| 208–211 | github.github_review_comments | INSERT ×2 | `#1905#rc_1`, `#1908#rc_1` | reviews `/reviews/1046`, `/1048` | PASS (Advisories 1, 3) | REUSED (R10 205–208) |
| 213–214 | trello.trello_cards | INSERT | `690b27282f4c1b7a6e93d512` "UI optimization pass" | as R10 | PASS (Advisory 2) | REUSED (R10 210–211) |
| 215–276 | trello.* | INSERT | 2 actions, checklist, 28 items | as R10 | PASS | REUSED (R10 212–273) |
| 277–282 | trello.* | INSERT | ZM card + 2 actions | as R10 | PASS | REUSED (R10 274–279) |
| 284–303 | gmail.* | INSERT ×5 each | incl. Vincent→Owen 2025-11-20T18:12:00Z | `history_id` NULL | PASS | REUSED (R10 281–300) |
| 305–312 | gcal.gcal_events | INSERT ×4 | 2026-02-15 start/end are plan fields | as R10 | PASS | REUSED (R10 302–309) |
| 314–339 | linear.linear_comments | INSERT ×13 | as R10 | base `/comments` empty | PASS | REUSED (R10 311–336) |
| 340–352 | linear.linear_issues | UPDATE ×13 | `updated_at` = each new comment's time | as R10 | PASS | REUSED (R10 337–349) |
| 353–354 | linear.linear_issues | UPDATE ×2 | ENG-2403/2404 `description` → NULL, `updated_at` → 2026-02-12T22:30:00Z | `/issues/2340`, `/2341` | PASS | REUSED (R10 350–351) |

(Line 82 is an unchanged `INSERT` header that now pairs with the new VALUES on line 83; the leave row's identical header moved to line 84. Every unchanged statement was confirmed byte-identical by the full diff.)

### Slack thread recount for `ef80c659…` (NEW)

Base replies (`CE156FDFB428/2025-11.json`, all with `thread_ts 1763394941.178509`): `/154` Vincent (2025-11-17, screenshot), `/206` Owen "This should be fixed now" (2025-11-19), `/240` Brian "I send the fix" (2025-11-20), `/269` Brian (2025-11-21, image), `/270` Vincent "I still have 1 pixel gap on my android but that's okay" (2025-11-21T18:03:01Z), `/271` Brian "I'll send another fix" (2025-11-21T18:07:42Z) = 6 replies, users {Vincent, Owen, Brian} = 3, matching the base parent (`reply_count 6`, `reply_users_count 3`, `latest_reply 1763748462.772499`). Plus SQL line 83 (Vincent) = **7 replies, 3 users, latest `1763845512.559339`** = the UPDATE on line 149. No other SQL row targets this thread; the other 24 UPDATEs are unaffected (R10 recount reused).

## 6. Check results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | NEW `lookup` of `948d64b2f42b443b0e509a0c66a03e3c` over `slack messages/*/*.json`: 0 matches, 687,230 records / 5,353 files, `scan_complete: true`, no errors. NEW parse of all 43 SQL Slack inserts: 0 duplicate ids, 0 duplicate (channel, ts). Parent `ef80c659…` exists (`CE156FDFB428/2025-11.json /152`), and the new row's `thread_ts_legacy` equals the parent's `thread_ts`. Author `EMPLOYEE_0012_SLACK_ID` (Vincent Parker, one Slack account) already posts in this thread (`/154`, `/270`). The UPDATE target exists. All other ids, actors, parents, ID contracts and Drive readability REUSED from R10 §6 A. |
| B — SQL structure and supported schema rules | PASS | NEW lint parse of all 193 statements: balanced transaction, column/value counts match, quoting well formed (`Brian''s`), JSON valid and base-shaped (`metadata_json '{}'`), no generated columns, NOT NULL columns supplied. The new row uses the same 18-column list as the other Slack inserts; the new UPDATE uses the same four columns as the other 24 thread UPDATEs. Provisional snapshot comparison REUSED: Advisory 1. |
| C — Dates, relationships and consistency | PASS | NEW: ts = `created_at` (1763845512 = 2025-11-22T21:05:12Z), before the clock; reply follows its parent (2025-11-17) and the last base reply (2025-11-21T18:07:42Z); it sits between Vincent's injected 21:00:12Z and 21:10:12Z replies on other lines, a coherent testing pass. **"Brian's second fix":** follows Brian's "I'll send another fix" (`/271`); the builds channel shows DD Android develop builds #2218–#2231 between 2025-11-21T18:37Z and 2025-11-22, with #2231 posted for Android testing at 2025-11-22T20:54:39Z (`C05433XK267/2025-11.json /825`), 11 minutes before this reply, so "on my android now" fits. That no commit is labeled as the tooltip fix is an unrecorded detail, not an incompatible fact. **Vincent's tenure:** his last Slack activity is 2025-11-23T09:36Z (R10 evidence, unchanged source), so a 2025-11-22 reply fits. **No later contradiction:** NEW scan of all 325 Slack message files for 2025-11, 2025-12 and 2026-* for "pixel", "tooltip", "navigation bar", "nav bar", "navbar" after 2025-11-21: no record says the navigation bar tooltip gap is still present or came back (hits are about other screens/games). No SQL record mentions tooltips other than line 83; the canvas line is already ticked (☑). Rest REUSED from R10 §6 C. |

## 7. Findings

No failing findings.

### Advisories (not failing)

1. **Columns not in the schema snapshot or the base export (B, provisional NOT COVERED), carried.** `gslides.slides_pages.notes`, `gslides.slides_page_elements.ordinal`, `.table_json`, `github.github_review_comments.pull_request_review_id`, `.side`, `.subject_type`, `.seq` (lines 31–54, 208–211). Snapshot unverified, so this is a compatibility limit, not a defect. The script is one transaction, so a missing column on the live database would roll back every record. To be safe, drop those 7 columns and their values.
2. **Cached Trello board activity, carried.** DD Product Roadmap's `dateLastActivity` (2025-10-10) predates the injected card's activity (2025-11-21). Cached field with unknown semantics.
3. **Review-comment timing (minor), carried.** Both review comments are 3–4 s after their review's `submitted_at`. Not a defect.
4. **Partial rejoin (informational), carried.** Owen is rejoined to 6 of the 10 channels he left.
5. **Membership events in a canvas comment channel (minor), carried.** `CE156FDFB428` is an `FC:` canvas comment channel; no base `FC:` channel has join/leave events. Not an incompatible fact.
6. **Second source for the same facts (informational), carried.** Brian's 3 DM lines (63–68) restate facts carried by other injected records; they agree.
7. **For `/prompt` (informational, new).** Line 83 is now the latest record on the "☑ navigation bar tooltips" thread and says the 1-pixel gap is gone after Brian's second fix. It doesn't name a build or version. Whether that settles the fork the last `/prompt` report raised on this line (including any build-version question) is for `/prompt`, not this stage.

## 8. Evidence limits (outside certification scope)

- Live execution, current database compatibility and undocumented constraints are not certified (schema snapshot unverified; Advisory 1).
- Trello board membership and checklist-state history aren't exported. GitHub PR file lists aren't exported. Build changelogs don't name a tooltip fix, so which build carried Brian's second fix isn't recorded (no contradiction).
- "Marcus pinged me" (line 63–68 set) refers to an unrecorded Marcus→Brian contact, carried.
- Agent visibility, discoverability and difficulty belong to `/prompt` and `/hardness`. Owen is a member of `CE156FDFB428` per R10 evidence (left 2026-02-11T20:41:12Z, rejoined 2026-02-12T22:41:27Z, lines 85 and 95).

## 9. Stage provenance (for reuse)

Static checks A–C depend on: SQL SHA `f9555a3cf6fcbbc649e18ee842a75ad00ea7da4cfe3071210a65b3e3ca26cadd`; universe manifest SHA `5e01ac44…e450`; schema snapshot SHA `31dcb2b4…5151`; id_contracts SHA `fc4711ef…4682`; Eval 0 SHA `e034019b…6eff`; WORKFLOW SHA `d5702ee2…3e33`; scoring.json SHA `c14873e6…e5bc`; lint `injection-lint-v1`; clock 2026-02-14 00:00 UTC. Reused items come from the R10 report (SHA `c46e263e…4bef`) §5 ledger rows, §5 thread recount and §6 A/B/C evidence for unchanged statements, carrying R8 (`7388c979…3eed`), R7, R6, R4 and R3. Each reused item covers a statement byte-identical to revision 10 (verified by full diff: only hunks `82a83,84` and `146a149`), with base manifest, Eval 0, schema snapshot, id_contracts and Slack channels/users hashes recomputed and unchanged; the WORKFLOW change was reviewed (§2) and adds no check affecting the reused rows. Re-checked NEW: Slack id lookup (5,353 files, complete); `messages/CE156FDFB428/2025-11.json` (272 records; `/152`, `/154`, `/206`, `/240`, `/269`, `/270`, `/271`); `messages/C05433XK267/2025-11.json` `/735–/825`; 325 Slack files for 2025-11, 2025-12, 2026-* scanned for the tooltip/gap terms; SQL-wide Slack id/(channel, ts) uniqueness. This PASS / COMPLETE report can be reused by `/prompt` for the static checks while the SQL hash and dependencies above match.

## 10. Next action

Run `/prompt`, then `/hardness`. Both read the injection SQL, so any earlier pass on them is outdated. `/oe` and `/rubric` also read the SQL and need rerunning after those.

### FINAL VERDICT: PASS

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (runtime does not report the effort level)

Next action: Run /prompt, then /hardness (both read the changed injection SQL); then /oe and /rubric

Evidence limits: Static scope only; live deployment and current schema compatibility not certified (snapshot unverified, Advisory 1); Agent visibility and difficulty belong to /prompt and /hardness
