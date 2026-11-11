# Injection data-integrity review: Eval 0 (delta on rev7)

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. Delta review: every changed, new and removed statement checked NEW; whole-file lint, structure, clock and chronology re-run NEW; base facts for byte-identical statements REUSED from my rev7 report. |
| Mode | Independent chat review, audit only. No input store, no `hg_write_output.py`, no `input_manifest.json`. Lint and search ran through `Task_Authoring/tools/hg.py` (`--task-dir Task_Authoring/task_inputsS`); export JSON and git history were read directly and read-only. |
| Review time | 2026-11-06 |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`. Manifest `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` (re-hashed). |
| Input under review | `R8/inputs/01_Universe_Inject.sql`: 59,622 bytes, 241 lines, 96 statements, SHA-256 `0e8c8ad83f3be435db1f9268f114c916f52293993eb687a55b34005015f9f815` (re-hashed at start and before writing). Not executed. |
| Previous version | `R8/prev/01_Universe_Inject.rev7.sql`, SHA-256 `091722f6a28117d59d40742adf1c0bbf379dd756c540a9dc79187b87275cb876`. |
| Previous report | `R8/prev/0_injection.rev7.md`, SHA-256 `1acef9559b3bbdceb6c7ea484bf54558e1588e6c7557b69195ce619e11bcb927`. Byte-identical to the report I wrote. PASS / COMPLETE. |
| Schema snapshot / ID contracts | `01ef579236212034a43a53914754f86ed9248be48c961009cef5b4bd6106f6eb` / `fc4711ef07667333c1cf2a417279826f0432539195f7acdfacfa86e9d9ed4682` (re-hashed; unchanged). |
| Known base issues | `8895c4dc73da249168b712c1da8da0ba0fb10dbc34dc7e90369dd43464961a52` (re-hashed; unchanged). |
| Context-only inputs | `00_Task_Assigned_Inputs.md` `e8b82698…`, `02_Universe_Date.txt` `2f0af108…`, `04_Prompt.txt` `2a23afd8…`. All unchanged. |

### Reuse decision

All four conditions hold for the 87 byte-identical statements.

1. The rev7 ledger carries claims with source pointers for each group. Unlike rev6, it does not depend on an unavailable report.
2. Universe manifest, schema, id_contracts, known issues and clock are unchanged.
3. Each reused statement is byte-identical by hash (statement diff), and base collections are unchanged.
4. No changed statement affects a reused claim. Cross-effects are tested in §6.

## 2. Input / authority issues

- No SQL comment changed (15 lines, identical). None concerns padding, tool calls, pass rates or gates. One section comment is now stale (G4).
- Grader-facing text: none. Lint found none, and every changed text field was read by hand. The new brief sentence is addressed to Julia in Frederick's voice, like the rest of the brief.
- **Correction to my rev7 report:** it gave 598,459 as the Slack message count. That is the count of distinct IDs; the row count is 610,468 across 4,840 files. No result changes.
- Two files I did not create appeared in `R8/out/` during this run (`P1_findings.md`, `P2_findings.md`). I did not open or change them, and nothing here relies on them.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, manifest, review version | Done (workspace adaptation: recorded here). |
| Diff against previous SQL | Done with a quote-aware statement diff, statement hashing and field-level diffs. 98 → 96 statements: **87 byte-identical (2 of them moved), 6 changed, 3 new, 5 removed.** |
| Run lint; resolve every flag | NEW: 0 flags (§4). |
| Inventory every statement | NEW: 96 statements (71 INSERT, 25 UPDATE). No DELETE or upsert. |
| Check A | **PASS**: NEW for all changed, new and removed items. |
| Check B | **PASS** (provisional): NEW over the whole file. |
| Check C | **PASS**: NEW for all changed, new and removed items; whole-file clock and Linear chronology re-run NEW. |
| Report coverage, findings, limits, verdict | Done. |

## 4. Lint

`hg_injection_lint.py` (injection-lint-v1) via `hg.py lint` on SHA `0e8c8ad8…`, universe synthcut, clock `2025-10-01T07:00:00Z`.

- Statements: 96 (71 insert, 25 update). Review comments 3, reviews 1, timeline events 1. `github_pr_comments` and `github_pull_requests` are no longer touched.
- **Flags: FAIL 0, CHECK 0, INFO 0.** Nothing to resolve.

## 5. Operation ledger

**Mapping.** Cur 1–24 = prev 1–24. Cur 26–33 = prev 26–33. Cur 35–41 = prev 35–41. Cur 42–43 = prev 45–46 (moved). Cur 47–48 = prev 47–48. Cur 49–61 = prev 51–63. Cur 63–82 = prev 65–84. Cur 84 = prev 86. Cur 86–94 = prev 88–96. Cur 96 = prev 98.

### Changed statements (all NEW; field diff shows only the listed field moved)

| Cur # | Prev # | Line | Table | Record | Change | Result |
|---|---|---|---|---|---|---|
| 25 | 25 | L93 | docs_documents | `f_7c3e91a4…` brief | `body_text` adds, in "Held or not": "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date." `style_runs_json`: last four headings +103. | PASS (G5) |
| 34 | 34 | L130 | drive_files | `f_e4a17c90…` calendar sheet | `web_view_link` NULL → `https://drive.google.com/file/d/1oIsTl3jQeyuTuqudrlGaxEze57_FtuiMHX72lDwtDSE/view` | PASS |
| 62 | 64 | L180 | linear_comments | `cmt_zom534_1` (Douglas) | Body adds "That is on main, so nothing else has to land for the beta." The watch sentence becomes "I am keeping this open to watch…". | PASS (G2) |
| 83 | 85 | L210 | linear_comments | `cmt_zom521_2` (Calvin) | "this item and ZOM-528" → "this item, ZOM-528 and ZOM-541". | PASS |
| 85 | 87 | L220 | linear_comments | `cmt_zom542_1` (Samuel) | Rewritten to "Picking this up after the bug list. The home screen and victory score changes for endless and boss arena are a layout refresh on screens that already work, so they are not needed for the beta." | PASS (G3) |
| 95 | 97 | L235 | trello_actions | `68dac820…` (Leonard) | `text` second sentence → "The rollover does not wait on them, the current quests keep running either way." | PASS |

### New statements (all NEW)

| Cur # | Line | Table | Record | Result |
|---|---|---|---|---|
| 44 | L148 | github_review_comments | `harmonygames-Games/match3d#472#rc_1` (Arthur, 15:52:58Z, on `rev_1`, `Assets/RewardVFXManager.cs`, seq 1): "Fine for this PR. Separately, the Season Pass premium strip is still set to the October range. It needs the November range before that season opens, Oliver is taking the date change." | PASS (G1, G6) |
| 45 | L150 | slack_messages | Mirror `65564543e4bc8dd707a177aada2337a3`, ts `1759247580.842719`, thread parent `61f686b8…` | PASS |
| 46 | L152 | slack_messages U | Parent `61f686b8…`: `reply_count` 3→4, `latest_reply` stays `1759247586.958099` | PASS |

### Removed statements (dependency check NEW)

| Prev # | Record | Dependency result |
|---|---|---|
| 42 | `#473#c_2` PR comment | Text moved into #44. 0 references left. |
| 43 | `#473#ev_5` timeline event | 0 references. |
| 44 | PR #473 `updated_at` bump | Reverts to base 15:43:58Z, the correct value with no later comment. |
| 49 | Mirror `bd1a7d0a…` | 0 references. |
| 50 | Parent `d05a2f8a…` UPDATE | Reverts to base: `reply_count` 2, `latest_reply` `1759246882.921709`, Comments "1", all matching its unchanged thread. |

Searches of the rev8 SQL: `#473`, `pull/473`, `bd1a7d0a…`, `d05a2f8a…`, `github_pr_comments`, `github_pull_requests` and `Addressables` each appear **0** times. "Nothing in the beta" appears 0 times. "premium strip" appears exactly twice (#44 and its mirror #45).

### Byte-identical statements (87; REUSED)

REUSED from `R8/prev/0_injection.rev7.md` (`1acef955…`) §5–§6, with sources and values as recorded there, by group: Slack asks; Halloween; leaderboard retest; Gmail; GCal; folder and deck; Sheets; GitHub `#470#rc_10`, `#468` `rev_3`, `rc_38`, `ev_6`; mirrors and parents for #470 and #468; Linear comments and UPDATEs; Trello card UPDATE. Whole-file lint, Check B, clock and Linear chronology were re-run NEW over them.

## 6. Checks

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | New keys collide with nothing: `#472#rc_1` (base has **0** review comments on #472); mirror ID and (channel, ts) absent from 610,468 messages in 4,840 files; Drive link token absent from 53,631 Drive rows and from 2025 Slack. References resolve: `#472#rev_1` exists (`/reviews/2179`); parent `61f686b8…` exists (`C093LEZGF6J/2025-09 /589`); ZOM-541 exists (`/issues/3616`). No statement left depends on a removed one. All 26 comment IDs unique; no duplicate keys inside the SQL. |
| B — SQL structure and supported schema rules | PASS (provisional) | Whole file, NEW. Column and value counts match on all 71 INSERTs with no duplicate columns. All 25 UPDATEs use `WHERE id = '<literal>'`. All 116 JSON literals parse. No generated column is written. All Linear timestamps are in the required format. #44's column list is identical to the other two review-comment rows. Snapshot mismatch set is the same (A1), with no new column. |
| C — Dates, relationships and consistency | PASS | **Clock:** 133 timestamp values; the only 16 after the clock are GCal start/end plan fields (#19–22); latest event 09-30T22:10:41Z. **Linear chronology:** 21 issues, sequences contiguous, times ascending, `updated_at` = latest comment on all 20 updated issues; ZOM-429's base `updated_at` is already later. **Claims:** below. |

### New GitHub and Slack rows against their base neighbours

| Check | Finding | Result |
|---|---|---|
| Review | `rev_1` is Arthur's APPROVED, `submitted_at` 15:52:58Z, `body` empty. `rc_1` has the same second and same author. Precedent: 17 base APPROVED reviews have a same-second same-author comment, including Arthur's `match3d#336#rev_2`. "Fine for this PR." fits an approval. | PASS |
| PR times | Opened 09-29T22:36:36Z, merged 15:53:04Z. The comment is 6 seconds before merge. PR `updated_at` 15:53:04Z is already later, so no bump is needed. | PASS |
| Path | `Assets/RewardVFXManager.cs` is in #472's merge diff, exists on main, and is used by 13 base review comments. | PASS |
| Timeline | No inline-comment event type exists in base. `ev_4` `reviewed` already covers `rev_1`, so no new row is due. | PASS |
| ID derivation (GitHub) | `<pr>#rc_<n>` with `seq` 1, first on the PR. | PASS |
| ID derivation (Slack) | Base formula established on 50 of 50 sampled rows: `sha256("<channel>\|<ts>")[:32]`. New row recomputes to `65564543e4bc8dd707a177aada2337a3`. | PASS |
| Thread | Base thread has 3 replies (`/590`, `/619`, `/621`). New reply makes 4. `thread_ts_legacy` = parent ts. `reply_users_count` stays 1 (same bot). | PASS |
| Reply count and latest | 3→4 is correct. `latest_reply` stays base `/621`, later than the mirror. | PASS |
| Ordering | ts sits between `/619` (approval mirror, 15:53:00.373) and `/620` (15:53:06.481). Approval-then-comment is the reverse of the #470 pair, but both occur in base: 180 approval-first, 150 comment-first of 330 pairs. | PASS |
| Mirror lag | Attachment `ts` 1759247578 = 15:52:58Z. Message 15:53:00.842: 2.84 s. Base range 1.91–335.61 s, median 5.85 s. | PASS |
| `discussion_r` | `2391985983` is above rc_10's `2391980467` and between base neighbours `2389766453` and `2392548750`. Linear interpolation from those neighbours gives ~2391985557. | PASS |
| Text | Mirror text equals the GitHub body exactly. | PASS |
| Field shapes | Attachment keys are identical to a base Arthur inline-comment mirror (`#395`): same pretext and fallback forms, `user` bot, `text` empty, `subtype` null. Title equals base `/590`'s `#472 Implement Win&amp;Collect into Queue Manager`. Review comment: `line`, `position`, `commit_id`, `in_reply_to_id` NULL as in all 1,387 base rows; `diff_hunk` empty as in 53 base rows (G6). | PASS |
| Parent card fields | `Comments` stays "1": it counts PR-level comments only (#468 shows "1" with 37 inline). Reviewers stays as base, which already omits Arthur despite his approval. | PASS |

### Docs row: heading offsets (all recomputed against `body_text`, length 2,807)

| Heading | Start–end | Text at offsets | Whole line |
|---|---|---|---|
| TITLE | 0–43 | ZM3D beta live-ops calendar - working rules | Yes |
| Span and time base | 163–181 | exact | Yes |
| Scope | 424–429 | exact | Yes |
| When a beat starts | 611–629 | exact | Yes |
| Held or not | 1230–1241 | exact | Yes |
| One-offs | 1831–1839 | exact | Yes |
| Still to do | 2039–2050 | exact | Yes |
| Push copy | 2268–2277 | exact | Yes |
| Config locks | 2594–2606 | exact | Yes |

The added sentence is 103 characters, inserted after 1241, so only the last four runs move, each by +103. The body is pure ASCII, so characters and bytes agree. The new rule fits Frederick's "if anything is held and until when" and defines what to write when no date exists.

### Drive row: link form

| Check | Finding |
|---|---|
| Form | `https://drive.google.com/file/d/<T>/view` is the base form for native Sheets: 200 of 356 use it; the other 156 are NULL. No `docs.google.com` form is used. |
| Token | 44 characters, leading `1`, base alphabet. 493 base links use 44-character tokens, which is the native-file length. |
| Relation to `id` | The token differs from the `f_…` id, as on every base row. |
| Collision | 0 Drive rows, 0 Slack hits. |
| Other injected Drive rows | Stay NULL, all with precedent: folders 23,257 NULL; presentations 132 of 132 NULL; Docs 334 of 595 NULL. |

### Check C detail: changed text

**`cmt_zom534_1` (#62): PASS.**

- "syncs quests-end with the client": commit `47c65623e7` (Oliver, 09-10), "Using remaining-time endpoint to sync quests end with client", changes `QuestManager.cs`, `QuestAPI.cs`, `QuestTimerAPI.cs`.
- "That is on main": confirmed as an ancestor of main, and Oliver said "yeah its on main" (`C08R27X0EAH /592`). Leonard next day: "my quest points are reset" (`executives /389`).
- "nothing else has to land": the owner's judgement, with no base record saying otherwise. All Sep 30 builds are later than the commit. See G2.
- "keeping this open": ZOM-534 is In Progress, assigned to Douglas. He was active 3.4 minutes earlier in Slack (`D05SG9H1CFM`).
- Douglas's 09-30 "reset endpoint" thread (`D07GY332589 /275–315`) is Season Pass on dev, not quests. It also supports the brief: "The event resets the very first day of the month in prod".

**`cmt_zom521_2` (#83): PASS.** ZOM-541 is In Progress, assigned to Calvin, created by Marcus, and is the ticket Brian and Calvin refer to (`D0770ET6WBW /197, /199`). "leaving … open" matches its state, and Calvin owns it. All rev7 evidence still applies: #475, builds, Brian's "I'll test it tomorrow". A mention on another ticket needs no `updated_at` change on ZOM-541.

**`cmt_zom542_1` (#85): PASS.**

- The rewrite removes "Not in the build yet" and "mockup stage" and asserts less.
- No ZOM-542 branch or PR exists, and no PR mentions the victory screen.
- Samuel's "Fixing UI Elements on Home screen" (`7c8dde3c05`) is ZOM-498, a different ticket, and came after the comment.
- "after the bug list": Samuel holds open tickets ZOM-453, 539 and 560.
- Brian and Vincent on 09-23 treat an endless UI change as undecided: "belli değil" (`D0770ET1HV2 /2118–2119`, my translation).
- ZOM-542's base state is untouched (G3).

**Trello (#95): PASS.** "The rollover does not wait on them" is true of the base mechanism: `cronWeeklyRule` runs at 00:00 `MON` regardless of content. Oct 13 is a Monday. The text holds together, and the claim is now narrow enough not to reach the quest push row. #96's badge and `dateLastActivity` still follow.

**`#472#rc_1` content (#44): PASS.** Monthly seasons are confirmed by Douglas (`D07GY332589 /311`). Oliver owns Season Pass (#473 author, active on it 09-30). The strip's date range itself is an uncontradicted author statement, as in rev7. The note is now pre-merge rather than post-merge, which closes D8.

**Brief (#25): PASS.** See offsets above. No conflict with the other rules.

**Cross-statement effects:** none. The note moved with identical wording after its prefix. No other record cited #473. Moved statements #42–43 keep their dependency on #38.

## 7. Findings and advisories

**No demonstrated defects.**

Each advisory is tagged **[CSC]** (a /prompt reviewer could score it under Cross-Service Coherence) or **[cosmetic]**.

**New in this revision:**

| ID | Tag | Record | Note | Optional fix |
|---|---|---|---|---|
| G1 | CSC | #44, #45 | A Season Pass note sits on a PR about Collect & Win queueing. "Separately" covers it, and `RewardVFXManager` does play Season Pass tokens, but #473 was the natural home. Arthur reaches it after Oliver self-merged #473 at 15:41:20Z, so he uses his next open review. Oliver, the named owner, is not on #472 and leaves no trace of taking it. No contradiction. | None needed. |
| G2 | CSC | #62 | "nothing else has to land for the beta" against Vincent's unanswered 09-12 timer parse error on `"0:10:60"` (`D07GMT8NVM2 /216`); main still uses `TimeSpan.Parse` (`QuestManager.cs:311–312`). The comment's "backend timing edge case" reads naturally as this, so the two reconcile. Oliver's later `d376fab4c8` (09-25T18:10Z, "fixing quests' chest") is a different item. | None needed. |
| G3 | CSC | #85 | ZOM-542 stays in **Regression** with label "Hot Fix - Global Launch", while the comment reads as ordinary queued work. Only ZOM-359 and ZOM-542 are in that state. Base state, same as rev7. | None needed. |
| G4 | cosmetic | L136 comment | "conversation notes" and "PR bumps" no longer describe anything in the section. | Trim the comment. |
| G5 | cosmetic | #25, #37 | A no-date hold puts text in a column headed "Hold until (UTC)". | None needed. |
| G6 | cosmetic | #44 | Empty `diff_hunk`; 53 of 1,387 base rows are empty, as are rc_10 and rc_38. | None needed. |

**Carried from rev7:**

| ID | Tag | Status | Note |
|---|---|---|---|
| F1 | CSC | **Resolved** | ZOM-541 now named. |
| F2 | CSC | **Resolved** | "Nothing in the beta" replaced by the narrower rollover claim. |
| D6 | CSC | **Resolved** | Residual closed with F1. |
| SC-16 pattern | CSC | **Resolved for the card line** | ZOM-526, 528 and 541 all explained. |
| D8 | cosmetic | **Resolved** | The note is pre-merge now. |
| F3 | CSC | Unchanged | Touches SC-47 (Weekly Quests status). |
| A11 | CSC | Unchanged | SC-15 repair. |
| A6 | CSC | Unchanged | "Approval from Product … he" against Robert as the approver. |
| N6 | CSC | Unchanged | ZOM-521 "icons" item ticked against `cmt_zom465_2`. |
| D5 | CSC | Unchanged | ZOM-344 Done with no corroborating artefact. |
| D7 | CSC | Unchanged | ZOM-432 closure evidence is indirect. |
| SC-6 | CSC | Unchanged | Brian's address is shared with the Node CEO in base. |
| SC-13 | CSC | Unchanged | List name differs from the action payload. |
| SC-38 | CSC | Unchanged | Season Pass; the premium-strip note now sits on #472. |
| F4 | cosmetic | Unchanged | "this item" does not name the checklist line. |
| F5 | cosmetic | Unchanged | #475's title says "animated icons". |
| F6 | cosmetic | Unchanged | Silent on "balance quest rewards". |
| A1 | cosmetic (deploy-compatibility limit) | Unchanged | Same snapshot-missing column set. |
| A9 | cosmetic | Unchanged | Stmt 5's "current prod build" names no build. |
| A10 | cosmetic | Unchanged | Rules sit in Frederick's DM. |
| N2 | cosmetic | Unchanged | `#468#ev_6` numbering. |
| N4 residual | cosmetic | Unchanged | Injected comments start at `sequence` 1. |
| N5 | cosmetic | Unchanged | No `state_history_json` on ZOM-432, ZOM-344 or ZOM-566. |
| D1′ | cosmetic | Unchanged | Native Doc and Sheet have NULL `size`/`content_path`. The Sheet now has a link but still no path. |
| D2 | cosmetic | Unchanged | `mbox_from` details. |
| D3 | cosmetic | Reduced | Comment plus approval mirrors now on #470 and #472; base has 330 such pairs. |
| D4 | cosmetic | Unchanged | Frederick is not a team_ZOM member and comments on ZOM-78. |
| E2 | cosmetic | Unchanged | `cmt_zom544_1` does not name the build tested. |
| E3 | cosmetic | Unchanged | `size_estimate` stays 4312. |
| SC-70 | cosmetic | Unchanged | Istanbul times. |

## 8. Limits

- **Outside the static scope:** live deploy compatibility (A1), search ranking, visibility and difficulty.
- **Not comparable with the base export:** Gmail `snippet` and `size_estimate`; Linear comments, state history and team privacy.
- **Owner judgements:** "nothing else has to land" (#62), "not needed for the beta" (#85) and the premium strip's date range (#44) are checked for contradiction, not positive proof.
- **Slack ID formula** established on 50 sampled base rows, then confirmed on two SQL rows; it is not a listed ID contract.
- **`discussion_r`** interpolation is a plausibility check only.
- **Translations** of Turkish DMs are mine.
- **Workspace adaptation:** no input store, no output writer and no manifest write.
- No required static check is unresolved.

## 9. Stage dependencies (for reuse)

| Dependency | Value |
|---|---|
| SQL | `0e8c8ad83f3be435db1f9268f114c916f52293993eb687a55b34005015f9f815` |
| Universe manifest | `da2f4cf0…4aac1a` |
| Schema snapshot | `01ef5792…06f6eb` |
| id_contracts | `fc4711ef…ed4682` |
| Known issues | `8895c4dc…961a52` |
| Clock | 2025-10-01T07:00:00Z |
| Lint | injection-lint-v1, 0 flags |

**New base facts recorded this run:**

- PR #472: `rev_1` APPROVED 15:52:58Z (`/reviews/2179`); merged 15:53:04Z; 0 base review comments.
- Slack thread `61f686b8…`: replies `/590`, `/619`, `/621`.
- Slack message ID: `sha256("<channel>|<ts>")[:32]`.
- Mirror stats on `zombie-prs`: inline lag 1.91–335.61 s, median 5.85; 330 comment and approval pairs, either order.
- Quest fix: `47c65623e7` on main; `C08R27X0EAH /587–594`; `executives /389`.
- Native Sheet link form: `drive.google.com/file/d/<44-char>/view` on 200 of 356.
- Season Pass monthly reset in prod: `D07GY332589 /311`.

Manifest entry that would be written:

```json
{"review_version": "injection-static-v2", "evidence_contract": "stage-evidence-v1", "input_sha256": "0e8c8ad83f3be435db1f9268f114c916f52293993eb687a55b34005015f9f815", "reused_evidence": [{"source_report": "R8/prev/0_injection.rev7.md", "sha256": "1acef9559b3bbdceb6c7ea484bf54558e1588e6c7557b69195ce619e11bcb927", "ledger_items": ["§5 and §6 rows for the 87 byte-identical statements (current 1-24, 26-33, 35-43, 47-61, 63-82, 84, 86-94, 96)"], "dependencies": {"universe_manifest": "da2f4cf0…4aac1a (unchanged)", "schema_snapshot": "01ef5792…06f6eb (unchanged)", "id_contracts": "fc4711ef…ed4682 (unchanged)", "clock": "2025-10-01T07:00Z (unchanged)", "statements": "byte-identical (statement hash)"}}], "result": "PASS", "execution_status": "COMPLETE"}
```

## 10. Next action

Proceed to `/prompt`. Earlier stage results for `091722f6…` are out of date; rerun `/prompt`, `/hardness`, `/oe` and `/rubric` in that order.

Carry G1, G2, G3, F3, A6, A11, N6, D5, D7, SC-6, SC-13 and SC-38 into `/prompt`. No SQL edit is needed for this PASS.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt

Evidence limits: Static scope only. Live deploy compatibility is unverified: the bundled snapshot (`01ef5792…`) lacks several columns the SQL writes (A1). Gmail snippet and size, Linear comments and state history, and team privacy cannot be compared with the base export. Owner judgements in #44, #62 and #85 are checked for contradiction, not positive proof. Base facts for the 87 byte-identical statements rest on rev7 report `1acef955…`, whose reuse dependencies all still match.
