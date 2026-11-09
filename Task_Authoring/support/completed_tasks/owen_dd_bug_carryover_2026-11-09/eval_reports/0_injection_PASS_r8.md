# /injection: Injection data-integrity review

## 1. Scope

| Item | Value |
|---|---|
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`, `ruthless-grading-v1`) |
| Mode | Chat review, attempt workspace (no task-folder preflight) |
| Actual review time | 2026-11-08 (session date), after the revision-13 save |
| Clock | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal/`, manifest `Evals/references/universes/normal/universe_manifest.json` SHA-256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Reviewed input | `Evals/task_inputs/01_Universe_Inject.sql` (revision 13, 89,786 bytes, 353 lines) SHA-256 `1ab32145ce306e86a5fa7be5a206dc23f3ca69e1ae673e2d6899f4385330ef76`, user attachment `01_Universe_Inject (8).sql` |
| Previous version | Revision 11, SHA-256 `f9555a3c…dcadd` (attachment `(7)`), reviewed PASS / COMPLETE in report SHA-256 `c282f2321932987575c004e263f8b166aa9a9ec287a5b6541d0802a24467f185` ("R11 report"), which carried R10 (`c46e263e…4bef`), R8, R7, R6, R4 and R3 evidence |
| References | Eval 0 SHA `e034019b…6eff`; WORKFLOW SHA `d5702ee2…3e33`; scoring.json `c14873e6…e5bc`; schema snapshot `injection.json` `31dcb2b4…5151` (unverified); `id_contracts.json` `fc4711ef…4682`; Slack `channels.json` `476eaa6d…0c76`, `users.json` `6aac5103…75dc`. All recomputed this run and **unchanged** from R11. Injection guide (`hg_reference.py guide injection`) re-loaded. |
| Lint | `hg_injection_lint.py` `injection-lint-v1` on SHA `1ab32145…ef76`: 192 statements (1 BEGIN, 150 INSERT, 40 UPDATE, 1 COMMIT); FAIL 0 / CHECK 0 / INFO 0 |
| Reused evidence | Yes, only for statements byte-identical to revision 11 (see §2, §5, §9) |

## 2. Input / authority issues

None. The SQL is substantive and runs as one transaction (`BEGIN` line 2 … `COMMIT` line 353).

**Changes from revision 11** (full `diff` of attachment `(7)` vs `(8)`, one hunk):

| Hunk | Rev-11 lines | Change |
|---|---|---|
| `65,66d64` | 65–66 | **Removed** 1 `slack.slack_messages` INSERT: `458a0bea1985feacad315da88ef9d030`, Brian (`EMPLOYEE_0026_SLACK_ID`) in DM `D07E9PSQB6W`, ts `1765471447.518229` = 2025-12-11T16:44:07Z: "Also, Vincent told me before he left that the Apple sync line on his Android list is the same sync problem as ENG-2073, nothing new needed for it." |

No row was added or edited. Line mapping: rev-11 lines 1–64 are the same; rev-11 lines 67–355 → −2 (65–353).

## 3. Checklist

- [x] Save/reload SQL; hash, base manifest and review version recorded (NEW)
- [x] Lint run on the whole file; no flags (NEW)
- [x] Inventory of every statement and record (NEW for the removal; unchanged rows REUSED from the R11 §5 ledger with renumbered lines)
- [x] Check A: no remaining statement references the removed id or ts (NEW SQL-wide search); remaining ids unchanged, so R11 collision results stay valid (REUSED)
- [x] Check B: whole-file lint parse (NEW); provisional snapshot comparison (REUSED)
- [x] Check C: remaining DM sequence and the Apple-sync fact re-checked after the removal (NEW); rest REUSED
- [x] Coverage, findings, limits and one final verdict (NEW)

## 4. Lint flags and resolutions

| Flag | Result | Resolution |
|---|---|---|
| future_date, id_contract, drive_unreadable, identities/duplicate_account, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape | 0 flags | Consistent with the independent checks. The change only removes a row, so it can't add a flag; the per-table counts drop by exactly one Slack insert (43 → 42). |

## 5. Operation ledger

Base paths as in R11 §5. "REUSED (R11)" = same row in the R11 report §5 (and through it R10/R8/R7/R6/R4/R3), statement byte-identical, all dependencies unchanged (§9). Lines are revision-13 line numbers.

| SQL lines | Table | Op | Records | References resolved | Result | Verification |
|---|---|---|---|---|---|---|
| 4–13 | gdrive.drive_files | INSERT ×5 | folder (Owen), 2 Docs, Slides, Sheet | parents = owners' roots; ids absent from 53,866 drive_files | PASS | REUSED (R11 4–13) |
| 15–18 | gdocs.docs_documents | INSERT ×2 | carry-over notes, ZM notes | id = drive id; no collision | PASS | REUSED (R11 15–18) |
| 20–27 | gsheets.* | INSERT | 1 spreadsheet, 3 tabs | no collision | PASS | REUSED (R11 20–27) |
| 29–54 | gslides.* | INSERT | 1 presentation, 4 pages, 8 elements | no collision | PASS (Advisory 1) | REUSED (R11 29–54) |
| 56–62 | slack.slack_messages | INSERT ×3 | Arthur→Owen DM; Marcus→Owen DM; Brian→Owen DM (2025-12-08T15:10:44Z) | as R11 | PASS | REUSED (R11 56–62) |
| 63–66 | slack.slack_messages | INSERT ×2 | Brian, `D07E9PSQB6W`, 2025-12-11T16:42:31Z (Tavern regression) and 16:46:03Z (two popups) | `channels.json /806`; ids absent; no ts collision | PASS | REUSED (R11 63–64, 67–68) |
| — | slack.slack_messages | (removed) | `458a0bea…` 2025-12-11T16:44:07Z | no statement references it (below) | PASS | NEW |
| 67–79 | slack.slack_messages | INSERT ×7 | god-bugs replies; 4 Vincent replies in `CE156FDFB428` | as R11 | PASS | REUSED (R11 69–81) |
| 81–82 | slack.slack_messages | INSERT reply | `948d64b2…` Vincent, tooltips thread | parent `ef80c659…` | PASS | REUSED (R11 83–84) |
| 82–89 | slack.slack_messages | INSERT `channel_leave` ×4 | Owen leaves 4 channels, 2026-02-11 | as R11 | PASS (Advisory 5) | REUSED (R11 84–91) |
| 90–101 | slack.slack_messages | INSERT `channel_join` ×6 | Owen rejoins 6 channels, 2026-02-12 | as R11 | PASS (Advisories 4, 5) | REUSED (R11 92–103) |
| 102–113 | slack.slack_messages | INSERT reply ×6 | Vincent replies 2025-11-21 | as R11 | PASS | REUSED (R11 104–115) |
| 114–115 | slack.slack_messages | INSERT reply | `87dc850c…` Marcus | parent `a9665999…` | PASS | REUSED (R11 116–117) |
| 116–135 | slack.slack_messages | INSERT reply ×10 | GitHub-bot mirrors | ts = PR comment `created_at` | PASS | REUSED (R11 118–137) |
| 136–139 | slack.slack_messages | INSERT reply ×2 | `ea8f1a2d…`, `52eafc2b…` | ts = review comment `created_at` | PASS (Advisory 3) | REUSED (R11 138–141) |
| 140–164 | slack.slack_messages | UPDATE ×25 | thread metadata (incl. `ef80c659…` 7 replies / 3 users) | R11 recount; none involves `D07E9PSQB6W` | PASS | REUSED (R11 142–166) |
| 166–205 | github pr_comments / timeline_events | INSERT ×10 each | as R11 | as R11 | PASS | REUSED (R11 168–207) |
| 206–209 | github.github_review_comments | INSERT ×2 | `#1905#rc_1`, `#1908#rc_1` | reviews exist | PASS (Advisories 1, 3) | REUSED (R11 208–211) |
| 211–274 | trello.* | INSERT | card, 2 actions, checklist, 28 items | as R11 | PASS (Advisory 2) | REUSED (R11 213–276) |
| 275–280 | trello.* | INSERT | ZM card + 2 actions | as R11 | PASS | REUSED (R11 277–282) |
| 282–301 | gmail.* | INSERT ×5 each | incl. Vincent→Owen 2025-11-20T18:12:00Z (Apple sync = ENG-2073) | `history_id` NULL | PASS | REUSED (R11 284–303) |
| 303–310 | gcal.gcal_events | INSERT ×4 | 2026-02-15 start/end are plan fields | as R11 | PASS | REUSED (R11 305–312) |
| 312–337 | linear.linear_comments | INSERT ×13 | as R11 | base `/comments` empty | PASS | REUSED (R11 314–339) |
| 338–350 | linear.linear_issues | UPDATE ×13 | `updated_at` = new comment time | as R11 | PASS | REUSED (R11 340–352) |
| 351–352 | linear.linear_issues | UPDATE ×2 | ENG-2403/2404 `description` → NULL | `/issues/2340`, `/2341` | PASS | REUSED (R11 353–354) |

(Line 80 is the unchanged `INSERT` header paired with line 81, as in R11. Every unchanged statement was confirmed byte-identical by the full diff.)

### Removal impact (NEW)

- SQL-wide search for `458a0bea`, `1765471447` and `16:44:07`: 0 hits. No UPDATE, reply or reaction targets the removed row.
- `D07E9PSQB6W` is a DM with no thread parents among the injected rows, so no `reply_count`/`latest_reply` needs to change.
- Remaining Slack inserts: 42; ids and (channel, ts) pairs are a subset of R11's collision-checked set, so no new collision can arise.

## 6. Check results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | NEW: no dangling reference to the removed row (§5). No new keys. All other ids, actors, parents, ID contracts and Drive readability REUSED from R11 §6 A. |
| B — SQL structure and supported schema rules | PASS | NEW lint parse of all 192 statements: balanced transaction, column/value counts match, quoting and JSON well formed, no generated columns, NOT NULL columns supplied. The removal took out a whole INSERT header + VALUES pair, leaving no orphan header. Provisional snapshot comparison REUSED: Advisory 1. |
| C — Dates, relationships and consistency | PASS | NEW: the remaining Brian DM lines (16:42:31Z "My fix didn't hold"; 16:46:03Z "And I never got back to the two popups…") still read as a coherent pair; the "And" continues the first line without needing the removed one. The Apple-sync = ENG-2073 fact is still recorded by Vincent's own email to Owen (2025-11-20T18:12:00Z, lines 282–289), so nothing in the SQL now points to a missing statement; the removed line only restated it (old Advisory 6). The only other "sync" hit (line 57, Arthur's "next BoomBit sync") is unrelated. Rest REUSED from R11 §6 C. |

## 7. Findings

No failing findings.

### Advisories (not failing)

1. **Columns not in the schema snapshot or the base export (B, provisional NOT COVERED), carried.** `gslides.slides_pages.notes`, `gslides.slides_page_elements.ordinal`, `.table_json`, `github.github_review_comments.pull_request_review_id`, `.side`, `.subject_type`, `.seq` (lines 31–54, 206–209). Snapshot unverified, so this is a compatibility limit, not a defect. The script is one transaction, so a missing column on the live database would roll back every record. To be safe, drop those 7 columns and their values.
2. **Cached Trello board activity, carried.** DD Product Roadmap's `dateLastActivity` (2025-10-10) predates the injected card's activity (2025-11-21). Cached field with unknown semantics.
3. **Review-comment timing (minor), carried.** Both review comments are 3–4 s after their review's `submitted_at`.
4. **Partial rejoin (informational), carried.** Owen is rejoined to 6 of the 10 channels he left.
5. **Membership events in a canvas comment channel (minor), carried.** `CE156FDFB428` is an `FC:` channel; no base `FC:` channel has join/leave events.
6. **Apple-sync fact now has one source (informational, updated).** With Brian's DM line removed, Vincent's 2025-11-20 email is the only record linking the Apple sync line to ENG-2073. That is consistent data; whether the Agent finds it is for `/prompt` and `/hardness`.

## 8. Evidence limits (outside certification scope)

- Live execution, current database compatibility and undocumented constraints are not certified (schema snapshot unverified; Advisory 1).
- Trello board membership and checklist-state history aren't exported; GitHub PR file lists aren't exported; which build carried Brian's second tooltip fix isn't recorded (no contradiction).
- "Marcus pinged me" (line 63) refers to an unrecorded Marcus→Brian contact, carried.
- Agent visibility, discoverability and difficulty belong to `/prompt` and `/hardness`.

## 9. Stage provenance (for reuse)

Static checks A–C depend on: SQL SHA `1ab32145ce306e86a5fa7be5a206dc23f3ca69e1ae673e2d6899f4385330ef76`; universe manifest SHA `5e01ac44…e450`; schema snapshot SHA `31dcb2b4…5151`; id_contracts SHA `fc4711ef…4682`; Eval 0 SHA `e034019b…6eff`; WORKFLOW SHA `d5702ee2…3e33`; scoring.json SHA `c14873e6…e5bc`; Slack channels `476eaa6d…0c76` / users `6aac5103…75dc`; lint `injection-lint-v1`; clock 2026-02-14 00:00 UTC. Reused items come from the R11 report (SHA `c282f232…f185`) §5 ledger rows, Slack thread recount and §6 A/B/C evidence for unchanged statements, carrying R10 (`c46e263e…4bef`), R8, R7, R6, R4 and R3. Each reused item covers a statement byte-identical to revision 11 (full diff: only hunk `65,66d64`, a deletion), with all dependency hashes recomputed and unchanged. Re-checked NEW: whole-file lint; SQL-wide search for the removed id/ts; DM sequence and Apple-sync source after removal. This PASS / COMPLETE report can be reused by `/prompt` for the static checks while the SQL hash and dependencies above match.

## 10. Next action

Run `/prompt`, then `/hardness`. Both read the injection SQL, so earlier passes on them are outdated. `/oe` and `/rubric` also read the SQL and need rerunning after those.

### FINAL VERDICT: PASS

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (runtime does not report the effort level)

Next action: Run /prompt, then /hardness (both read the changed injection SQL); then /oe and /rubric

Evidence limits: Static scope only; live deployment and current schema compatibility not certified (snapshot unverified, Advisory 1); Agent visibility and difficulty belong to /prompt and /hardness
