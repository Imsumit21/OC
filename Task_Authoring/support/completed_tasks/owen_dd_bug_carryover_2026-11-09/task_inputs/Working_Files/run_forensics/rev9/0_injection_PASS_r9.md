# /injection: Injection data-integrity review

## 1. Scope

| Item | Value |
|---|---|
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`, `ruthless-grading-v1`) |
| Mode | Chat review, attempt workspace (no task-folder preflight) |
| Actual review time | 2026-11-08 (session date), after the revision-15 save |
| Clock | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal/`, manifest `Evals/references/universes/normal/universe_manifest.json` SHA-256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Reviewed input | `Evals/task_inputs/01_Universe_Inject.sql` (revision 15, 89,264 bytes, 350 lines) SHA-256 `ea5b542897c846d955d1361bd50ed2531214044b53e229fc032b2c55bbbd2504`, user attachment `01_Universe_Inject (9).sql` |
| Previous version | Revision 13, SHA-256 `1ab32145…ef76` (attachment `(8)`), reviewed PASS / COMPLETE in report SHA-256 `2e6de14ac3dfdca343ff555673dc95a7e7669f0bc95768219a7b32e712b43570` ("R13 report"), which carried R11 (`c282f232…f185`), R10, R8, R7, R6, R4 and R3 evidence |
| References | Eval 0 SHA `e034019b…6eff`; WORKFLOW SHA `d5702ee2…3e33`; scoring.json `c14873e6…e5bc`; schema snapshot `injection.json` `31dcb2b4…5151` (unverified); `id_contracts.json` `fc4711ef…4682`; Slack `channels.json` `476eaa6d…0c76`, `users.json` `6aac5103…75dc`. All recomputed this run and **unchanged** from R13. |
| Lint | `hg_injection_lint.py` `injection-lint-v1` on SHA `ea5b5428…2504`: 190 statements (1 BEGIN, 149 INSERT, 39 UPDATE, 1 COMMIT); FAIL 0 / CHECK 0 / INFO 0 |
| Reused evidence | Yes, only for statements byte-identical to revision 13 (see §2, §5, §9) |

## 2. Input / authority issues

None. The SQL is substantive and runs as one transaction (`BEGIN` line 2 … `COMMIT` line 350).

**Changes from revision 13** (full `diff -u` of attachment `(8)` vs `(9)`, three hunks):

| Hunk | Change |
|---|---|
| `@@ -60,9 +60,9` | **Removed** Slack `c4a762005895751153ce787815ca49bf` (Brian, DM `D07E9PSQB6W`, ts `1765471351.236119` = 2025-12-11T16:42:31Z, "Marcus pinged me, the Tavern buttons lost their frame again… My fix didn't hold"). **Edited** `2ea7c02c…` (16:46:03Z): text now starts "I never got back to the two popups…" (leading "And " dropped); id, ts and every other column unchanged. **Added** Slack `2f3add0dcfc251b7e92cd216af7352e2` (Brian, `D07E9PSQB6W`, ts `1765471651.208713`, created_at 2025-12-11T16:47:31Z): "Daily Gift isn't finished either, the panel never got its last pass." |
| `@@ -316,8 +316,6` | **Removed** Linear comment `comment_3e81bf306c58746580a9cfa0ca12bd60` on ENG-2437 (Brian, 2025-11-24T16:00:00Z). |
| `@@ -347,7 +345,6` | **Removed** `UPDATE linear.linear_issues SET updated_at = '2025-11-24T16:00:00Z' WHERE id = 'ENG-2437'`. |

Line mapping: rev-13 lines 1–62 and 64 unchanged; 66–318 → same; 321–349 → −2; 351–353 → −3.

## 3. Checklist

- [x] Save/reload SQL; hash, base manifest and review version recorded (NEW)
- [x] Lint run on the whole file; no flags (NEW)
- [x] Inventory of every statement and record (NEW for the three hunks; unchanged rows REUSED from the R13 §5 ledger with renumbered lines)
- [x] Check A: new Slack id and (channel, ts) collision-checked against the complete base and the SQL; removed ids/ts not referenced anywhere (NEW)
- [x] Check B: whole-file lint parse (NEW); provisional snapshot comparison (REUSED)
- [x] Check C: new Daily Gift line vs base ENG-2437 and the injected Sheet/Trello rows; Tavern regression still sourced after removal; ENG-2437 `updated_at` after removing the comment (NEW); rest REUSED
- [x] Coverage, findings, limits and one final verdict (NEW)

## 4. Lint flags and resolutions

| Flag | Result | Resolution |
|---|---|---|
| future_date, id_contract, drive_unreadable, identities/duplicate_account, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape | 0 flags | Consistent with the independent checks. Per-table counts: Slack inserts unchanged at 42 (one removed, one added); `linear_comments` 13 → 12; `linear_issues` updates 15 → 14. |

## 5. Operation ledger

"REUSED (R13)" = same row in the R13 report §5 (and through it R11 and earlier), statement byte-identical, all dependencies unchanged (§9). Lines are revision-15 line numbers.

| SQL lines | Table | Op | Records | References resolved | Result | Verification |
|---|---|---|---|---|---|---|
| 4–13 | gdrive.drive_files | INSERT ×5 | folder (Owen), 2 Docs, Slides, Sheet | parents = owners' roots; ids absent from 53,866 drive_files | PASS | REUSED (R13 4–13) |
| 15–18 | gdocs.docs_documents | INSERT ×2 | carry-over notes, ZM notes | id = drive id | PASS | REUSED (R13 15–18) |
| 20–27 | gsheets.* | INSERT | 1 spreadsheet, 3 tabs (Live-Ops tab lists Daily Gift / ENG-2437 / "last pass") | no collision | PASS | REUSED (R13 20–27) |
| 29–54 | gslides.* | INSERT | 1 presentation, 4 pages, 8 elements | no collision | PASS (Advisory 1) | REUSED (R13 29–54) |
| 56–62 | slack.slack_messages | INSERT ×3 | Arthur→Owen DM; Marcus→Owen DM (Tavern regression, line 59); Brian→Owen DM 2025-12-08T15:10:44Z | as R13 | PASS | REUSED (R13 56–62) |
| — | slack.slack_messages | (removed) | `c4a76200…` 2025-12-11T16:42:31Z | no statement references it | PASS | NEW |
| 63–64 | slack.slack_messages | INSERT (text edited) | `2ea7c02c…` Brian, `D07E9PSQB6W`, 16:46:03Z, two popups | id/ts unchanged from R13 collision check; DM membership as R13 (`channels.json /806`) | PASS | NEW (text) / REUSED (keys) |
| 65–66 | slack.slack_messages | INSERT | `2f3add0d…` Brian, `D07E9PSQB6W`, ts `1765471651.208713` = created_at 2025-12-11T16:47:31Z, Daily Gift | id absent from all 5,353 message files (687,230 records, scan complete); ts absent from all 12 `D07E9PSQB6W` files (441 records); each appears once in the SQL | PASS | NEW |
| 67–79 | slack.slack_messages | INSERT ×7 | god-bugs replies; 4 Vincent replies in `CE156FDFB428` | as R13 | PASS | REUSED (R13 67–79) |
| 80–81 | slack.slack_messages | INSERT reply | `948d64b2…` Vincent, tooltips thread | parent `ef80c659…` | PASS | REUSED (R13 81–82) |
| 82–89 | slack.slack_messages | INSERT `channel_leave` ×4 | Owen leaves 4 channels, 2026-02-11 | as R13 | PASS (Advisory 5) | REUSED (R13 82–89) |
| 90–101 | slack.slack_messages | INSERT `channel_join` ×6 | Owen rejoins 6 channels, 2026-02-12 | as R13 | PASS (Advisories 4, 5) | REUSED (R13 90–101) |
| 102–113 | slack.slack_messages | INSERT reply ×6 | Vincent replies 2025-11-21 | as R13 | PASS | REUSED (R13 102–113) |
| 114–115 | slack.slack_messages | INSERT reply | `87dc850c…` Marcus | parent `a9665999…` | PASS | REUSED (R13 114–115) |
| 116–135 | slack.slack_messages | INSERT reply ×10 | GitHub-bot mirrors | ts = PR comment `created_at` | PASS | REUSED (R13 116–135) |
| 136–139 | slack.slack_messages | INSERT reply ×2 | `ea8f1a2d…`, `52eafc2b…` | ts = review comment `created_at` | PASS (Advisory 3) | REUSED (R13 136–139) |
| 140–164 | slack.slack_messages | UPDATE ×25 | thread metadata | none involves `D07E9PSQB6W` | PASS | REUSED (R13 140–164) |
| 166–205 | github pr_comments / timeline_events | INSERT ×10 each | as R13 | as R13 | PASS | REUSED (R13 166–205) |
| 206–209 | github.github_review_comments | INSERT ×2 | `#1905#rc_1`, `#1908#rc_1` | reviews exist | PASS (Advisories 1, 3) | REUSED (R13 206–209) |
| 211–274 | trello.* | INSERT | card, 2 actions, checklist, 28 items (incl. Tavern `complete` line 244, Daily Gift `incomplete` line 266) | as R13 | PASS (Advisory 2) | REUSED (R13 211–274) |
| 275–280 | trello.* | INSERT | ZM card + 2 actions | as R13 | PASS | REUSED (R13 275–280) |
| 282–301 | gmail.* | INSERT ×5 each | incl. Vincent→Owen 2025-11-20T18:12:00Z | `history_id` NULL | PASS | REUSED (R13 282–301) |
| 303–310 | gcal.gcal_events | INSERT ×4 | 2026-02-15 start/end are plan fields | as R13 | PASS | REUSED (R13 303–310) |
| 312–335 | linear.linear_comments | INSERT ×12 | as R13 minus ENG-2437 comment | base `/comments` empty (0 records, re-read) | PASS | REUSED (R13 312–318, 321–337) |
| — | linear.linear_comments | (removed) | `comment_3e81bf30…` ENG-2437 | not referenced anywhere | PASS | NEW |
| 336–347 | linear.linear_issues | UPDATE ×12 | `updated_at` = new comment time | one per remaining comment issue | PASS | REUSED (R13 338–349 minus 349) |
| — | linear.linear_issues | (removed) | ENG-2437 `updated_at` UPDATE | base value 2025-11-12T19:26:04Z now stands; no injected activity on ENG-2437 remains | PASS | NEW |
| 348–349 | linear.linear_issues | UPDATE ×2 | ENG-2403/2404 `description` → NULL | `/issues/2340`, `/2341` | PASS | REUSED (R13 351–352) |

## 6. Check results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | NEW: `2f3add0d…` and (`D07E9PSQB6W`, `1765471651.208713`) collision-free across the complete base and the SQL (§5). Author `EMPLOYEE_0026_SLACK_ID` = Brian Foster, a member of DM `D07E9PSQB6W` (R13). SQL-wide search for removed `c4a76200`, `1765471351`, `comment_3e81bf30` / `3e81bf30`: 0 hits. Base Linear `/comments` is empty, so the removed comment can't orphan anything. All other ids, actors, parents, ID contracts and Drive readability REUSED. |
| B — SQL structure and supported schema rules | PASS | NEW lint parse of all 190 statements: balanced transaction, column/value counts match, quoting (`isn''t`, `Arthur''s`) well formed, no orphan INSERT header after the removals. Provisional snapshot comparison REUSED: Advisory 1. |
| C — Dates, relationships and consistency | PASS | NEW: ts `1765471651.208713` matches created_at 2025-12-11T16:47:31Z, before the clock, and follows the 16:46:03Z line; "either" reads naturally after the two-popups message. **Daily Gift:** base ENG-2437 "Daily Gift UI Optimization" is assigned to and created by Brian (`usr_fc22d5941b2aeb5c`), `completed_at` null; the injected Sheet row says "last pass" and the Trello item is `incomplete`. No base Slack/GitHub record mentions ENG-2437 or says the Daily Gift UI pass was done (complete scans). Brian's line matches all of these. **Tavern:** removing Brian's DM leaves Marcus's own DM (line 59, 2025-12-11T11:20:12Z, "Brian's fix didn't hold") as the source for the regression, so nothing in the SQL now points to a missing statement. The old "Marcus pinged me" evidence limit is gone with it. **ENG-2437 `updated_at`:** with the comment and its UPDATE both removed, the base 2025-11-12 value is consistent. Rest REUSED from R13 §6 C. |

## 7. Findings

No failing findings.

### Advisories (not failing)

1. **Columns not in the schema snapshot or the base export (B, provisional NOT COVERED), carried.** `gslides.slides_pages.notes`, `gslides.slides_page_elements.ordinal`, `.table_json`, `github.github_review_comments.pull_request_review_id`, `.side`, `.subject_type`, `.seq` (lines 31–54, 206–209). Snapshot unverified, so this is a compatibility limit, not a defect. Because the script is one transaction, a missing column on the live database would roll back every record. To be safe, drop those 7 columns and their values.
2. **Cached Trello board activity, carried.** DD Product Roadmap's `dateLastActivity` (2025-10-10) predates the injected card's activity (2025-11-21).
3. **Review-comment timing (minor), carried.** Both review comments are 3–4 s after their review's `submitted_at`.
4. **Partial rejoin (informational), carried.** Owen is rejoined to 6 of the 10 channels he left.
5. **Membership events in a canvas comment channel (minor), carried.** `CE156FDFB428` is an `FC:` channel; no base `FC:` channel has join/leave events.
6. **Single-source facts (informational, updated).** The Apple-sync = ENG-2073 link (Vincent's 2025-11-20 email), the Tavern regression (Marcus's DM, line 59) and now "Daily Gift unfinished" in words (Brian's DM, line 65; Sheet "last pass" and Trello `incomplete` agree) each rest on one record. The data is consistent; whether the Agent finds them is for `/prompt` and `/hardness`.

## 8. Evidence limits (outside certification scope)

- Live execution, current database compatibility and undocumented constraints are not certified (schema snapshot unverified; Advisory 1).
- Trello board membership and checklist-state history aren't exported; GitHub PR file lists aren't exported; which build carried Brian's second tooltip fix isn't recorded (no contradiction).
- Agent visibility, discoverability and difficulty belong to `/prompt` and `/hardness`.

## 9. Stage provenance (for reuse)

Static checks A–C depend on: SQL SHA `ea5b542897c846d955d1361bd50ed2531214044b53e229fc032b2c55bbbd2504`; universe manifest SHA `5e01ac44…e450`; schema snapshot SHA `31dcb2b4…5151`; id_contracts SHA `fc4711ef…4682`; Eval 0 SHA `e034019b…6eff`; WORKFLOW SHA `d5702ee2…3e33`; scoring.json SHA `c14873e6…e5bc`; Slack channels `476eaa6d…0c76` / users `6aac5103…75dc`; Linear `data.json` (base issue `ENG-2437`, `/comments` empty); lint `injection-lint-v1`; clock 2026-02-14 00:00 UTC. Reused items come from the R13 report (SHA `2e6de14a…3570`) §5 ledger rows and §6 A/B/C evidence for unchanged statements, carrying R11 and earlier. Each reused item covers a statement byte-identical to revision 13 (full diff: three hunks listed in §2), with all dependency hashes recomputed and unchanged. Re-checked NEW: whole-file lint; new Slack id/ts collision scans; SQL-wide search for removed ids/ts; Daily Gift consistency vs base ENG-2437, Sheet and Trello; Tavern source after removal; ENG-2437 `updated_at`. This PASS / COMPLETE report can be reused by `/prompt` for the static checks while the SQL hash and dependencies above match.

## 10. Next action

Run `/prompt`, then `/hardness`. Both read the injection SQL, so earlier passes on them are outdated. `/oe` and `/rubric` also read the SQL and need rerunning after those.

### FINAL VERDICT: PASS

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (runtime does not report the effort level)

Next action: Run /prompt, then /hardness (both read the changed injection SQL); then /oe and /rubric

Evidence limits: Static scope only; live deployment and current schema compatibility not certified (snapshot unverified, Advisory 1); Agent visibility and difficulty belong to /prompt and /hardness
