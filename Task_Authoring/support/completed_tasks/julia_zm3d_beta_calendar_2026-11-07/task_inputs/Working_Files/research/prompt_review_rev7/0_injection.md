# Injection data-integrity review: Eval 0

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. Reuse was tested, not assumed. See "Reuse decision" below. |
| Mode | Independent chat review, audit only. No input store, no `hg_write_output.py`, no `input_manifest.json`. Lint and search ran through `Task_Authoring/tools/hg.py` (`--task-dir Task_Authoring/task_inputsS`); export JSON and git history were read directly and read-only. |
| Review time | 2026-11-06 |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`. Manifest `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` (re-hashed). |
| Input under review | `R/inputs/01_Universe_Inject.sql`: 61,201 bytes, 245 lines, 98 statements, SHA-256 `091722f6a28117d59d40742adf1c0bbf379dd756c540a9dc79187b87275cb876` (re-hashed at start and again before writing). Not executed. |
| Previous version | `R/prev/01_Universe_Inject.rev6.sql`, SHA-256 `f8d905bdd0c29585b17090b54aeb7837135f9d2462440ba71d81192d0871249c`. |
| Previous report | `R/prev/0_injection.rev6.md`, SHA-256 `6baf29368cca1fc25de7c3acda19bfa66126bf28dcbafd089d0b563d2e102513`, PASS / COMPLETE. |
| Schema snapshot / ID contracts | `01ef579236212034a43a53914754f86ed9248be48c961009cef5b4bd6106f6eb` / `fc4711ef07667333c1cf2a417279826f0432539195f7acdfacfa86e9d9ed4682` (both re-hashed; match rev6). |
| Known base issues | `Task_Authoring/references/known_data_issues/synthcut.md` `8895c4dc73da249168b712c1da8da0ba0fb10dbc34dc7e90369dd43464961a52` (matches rev6). |
| Rules read | `Evals/WORKFLOW.md` `05a5e45e…8c69`, `Evals/0_Injection_Quality_Eval.md` `86af2102…fcd3`. |
| Context-only inputs | `00_Task_Assigned_Inputs.md` `e8b82698…`, `02_Universe_Date.txt` `2f0af108…`, `04_Prompt.txt` `2a23afd8…`. All match rev6. |

### Reuse decision

| Condition | Result |
|---|---|
| 2. Dependencies unchanged | **Holds.** Universe manifest, schema snapshot, id_contracts, known issues and clock all match rev6. |
| 3. Scope supports the use | **Holds** for byte-identical statements. |
| 4. No changed statement affects a reused claim | **Holds**, tested in §6. |
| 1. Original ledger records the exact claim, source pointer and coverage | **Holds only for rev6's own 13 NEW rows** (its §5–§6). It **does not hold for rev6's 84 "REUSED" rows.** Those rows only summarise an older report (`01dbb84d…`), for example "Slack ID formula, membership, threads and pointers". That report is not in `R/prev/`, and its folder is off-limits to this review. |

The contract says reports lacking enough provenance "fall back to source verification, not guessed reuse". So the byte-identical statements were **re-verified from source** here rather than inherited. Only the specific rev6 facts listed in §5 are REUSED. This is a provenance limit in the evidence chain, not a defect in the SQL.

## 2. Input / authority issues

- No SQL comment changed (15 comment lines, identical). None concerns padding, tool calls, pass rates or gates.
- Grader-facing text: none. The lint found none, and both changed text fields were read by hand.
- No statement was removed, so the removed-statement dependency check has nothing to act on. Old Trello wording ("New quest set", "current set") appears 0 times in the SQL and nothing else depended on it.
- Rev6 labels its Istanbul-times advisory "SC-48". In the current known-issues file SC-48 is the "Pitch Sep 25" deck date; the timezone item is **SC-70**. Corrected below.
- Two files I did not create appeared in `R/out/` during this run (`P3_findings.md`, `P4_findings.md`), along with `R/work/`. I did not open or change them, and nothing here relies on them. `R/inputs/` and `R/prev/` were unchanged by hash.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, manifest, review version | Done (workspace adaptation: recorded here). |
| Diff against the previous SQL | Done with a quote-aware statement diff plus a field-level diff. 97 → 98 statements: **95 byte-identical, 1 new (#85), 2 changed (#86, #97), 0 removed.** |
| Run lint; resolve every flag | NEW: 0 flags (§4). |
| Inventory every statement | NEW: 98 statements (72 INSERT, 26 UPDATE). No DELETE or upsert. |
| Check A | **PASS**, NEW across the whole file. |
| Check B | **PASS** (provisional), NEW across the whole file. |
| Check C | **PASS**, NEW for every record group (§6). |
| Report coverage, findings, limits, verdict | Done. |

## 4. Lint

`hg_injection_lint.py` (injection-lint-v1) run through `hg.py lint` on SHA `091722f6…`, universe synthcut, clock `2025-10-01T07:00:00Z`.

- Checks run: future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required.
- Statements: 98 (72 insert, 26 update). Linear comments 26, linear_issues updates 20.
- **Flags: FAIL 0, CHECK 0, INFO 0.** Nothing to resolve.

## 5. Operation ledger

Numbering is the current file. Current #1–84 are prev #1–84; #85 is new; current #86–98 are prev #85–97.

### Changed and new statements (all NEW)

| # | Line | Table | Op | Record | Change against rev6 | Result |
|---|---|---|---|---|---|---|
| 85 | L214 | linear_comments | I | **new** `cmt_zom521_2`, ZOM-521, Calvin `usr_49b9dfa5208d400d`, 2025-09-30T16:27:38Z, seq 2 | "Card pack animation went in with #475. I am leaving this item and ZOM-528 open until Brian has seen it in a build." | PASS (advisories F1, F4, F5) |
| 86 | L215–222 | linear_issues | U | ZOM-521 | `updated_at` 09-26T17:25:02Z → 09-30T16:27:38Z. Base was 09-17T15:50:49Z. Description unchanged from rev6 (verified by normalised comparison). Against base, it unticks "Tokens traveling to live-ops" and "Claimed Cards traveling to inventory Section". | PASS |
| 97 | L239 | trello_actions | I | `68dac8204f1e9a3b7c2d5e61`, commentCard, Leonard, 09-29T17:55:44Z | `data.text` only (everything else verified identical): "More quests get added with the Mon Oct 13 rollover if they are ready. Nothing in the beta waits on them, the current quests keep running either way." | PASS (advisories F2, F3, F6) |

### Byte-identical statements (95): basis for each group

| # | Records | Verification | Result and source |
|---|---|---|---|
| 1–2 | Frederick's DM ask and threaded reply, `D05SD5QLG94` | NEW | IDs and (channel, ts) absent from 598,459 messages in 4,840 files. Frederick and Julia are DM members. `ts` = `created_at`. #1 `reply_count` 1 and `latest_reply` = #2's ts. |
| 3, 6 | Robert's Halloween reply; parent UPDATE | NEW | Parent `C08R8CHB0QL/2025-09 /121` (Martin, 09-17T15:10:09Z, tags Robert, Leonard, Julia). `reply_count` 0→1, `latest_reply` = #3's ts. |
| 4 | Robert's DM pulling the ok, `D05GU6L0XFH` | NEW | Robert and Julia are members. Later than #3. |
| 5 | Vincent's leaderboard retest, `C0880U9751A` | NEW | Key clean; Vincent is a member. Later correction to `cmt_zom429_1`, which is a supported supersession. |
| 7, 9, 11, 13, 15, 17 | Gmail threads | NEW | 6 thread numbers absent from 81,406 Gmail JSON files. Snippet equals the message snippet. |
| 8, 10, 12, 14, 16, 18 | Gmail messages | NEW + REUSED | NEW: `internal_date` = Date header; `date` matches; snippet is a body prefix; X-GM-THRID, user and Message-ID agree; Message-ID tokens absent (same scan). REUSED from rev6 §6: base label shape (`brian.foster@…/1822693237981026750`); 5,316 base non-replies with `''`/`''`. |
| 19–22 | GCal Oct 8 release (4 calendars) | NEW | 0 of 10,395 event IDs or ical UIDs collide. All 4 calendars exist in base. 15:00Z = 18:00 Istanbul. `created`/`updated` are before the clock; start/end are plan fields. |
| 23–25 | Folder, brief, Docs row | NEW | Not among 53,631 Drive files or 595 Docs. Parents resolve to Julia's and Frederick's roots. All 9 style runs land exactly on their headings. |
| 26–33 | Deck, Slides rows | NEW | Not among 132 presentations. 3 pages, each with its element. Week dates verified (Oct 6 Mon, Nov 2 Sun). |
| 34–37 | Calendar sheet, Sheets rows | NEW | Not among 356 spreadsheets. Parent is #23 (earlier in the SQL). Headers are 9 and 7 wide, equal to `column_count`. |
| 38 | `#470#rc_10` on `rev_9` | NEW | Key clean (9 siblings). `rev_9` is Arthur's APPROVED at 15:51:06Z, the same second. Path exists on main. |
| 39–41 | `#468` `rev_3`, `rc_38`, `ev_6` | NEW | Keys clean. Before merge (09-29T16:13:50Z). `GameLoader.cs` is in the #468 merge diff. |
| 42–44 | `#473` `c_2`, `ev_5`, PR bump | NEW | Keys clean. Post-merge comment (D8). `updated_at` 15:43:58Z → 16:16:33Z. |
| 45, 47, 49 | Slack mirrors | NEW | Mirror text equals the GitHub body after HTML unescape (3 of 3). Attachment `ts` equals the comment time; message lands 2 seconds later. Keys clean. |
| 46, 48, 50 | Thread parent UPDATEs | NEW | Targets exist (`/579`, `/530`, `/605`). Reply counts 16→17, 41→42, 2→3. Field-level `attachments_json` diff: #48 adds Arthur to Reviewers; #50 Comments 1→2; nothing else moved. |
| 51–84, 87–96 | Linear comments and UPDATEs | NEW + REUSED | Whole-file chronology and per-issue claims in §6. REUSED from rev6 §6: #472 diff reading; Axe Arena postponement `C05KNDCHAAG/2025-09 /31`; Douglas's Google Play note `CD843DBC4C3E /39`. |
| 98 | Trello card UPDATE | NEW | Field diff against base: only `comments` 0→1. `dateLastActivity` equals #97's date and is later than base 09-12T17:31:20Z. |

### NEW collision and coverage results

| Service | Result | Coverage |
|---|---|---|
| Slack | 8 message IDs and (channel, ts) pairs absent | 598,459 messages, 4,840 files |
| Gmail | 6 thread numbers, 2 Message-ID tokens absent | 81,406 files, `scan_complete: true` |
| Drive / Docs / Slides / Sheets | All new IDs absent | 53,631 / 595 / 132 / 356 |
| GCal | 4 event IDs and shared ical UID absent | 10,395 events |
| GitHub | `#470#rc_10`, `#468#rev_3`, `#468#rc_38`, `#468#ev_6`, `#473#c_2`, `#473#ev_5` absent | Complete arrays |
| Linear | `cmt_zom521_2` new; all 26 SQL comment IDs unique | Base `/comments` has 0 rows |
| Trello | `68dac820…` absent | 5,252 actions |

## 6. Checks

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All new keys are absent from complete collections (§5). All references resolve: every Linear author (26 of 26), Slack user, Drive parent, thread parent and PR target. Calvin `usr_49b9dfa5…` is one Linear account, a team_ZOM member since 2025-06-23. `PERSON_0003_GITHUB_USERNAME` = "Calvin Price"; `PERSON_6094` = Leonard Hayes. No removed statements. Drive readability: native Doc, Sheet and Slides all have their content rows; lint `drive_unreadable` passes. |
| B — SQL structure and supported schema rules | PASS (provisional) | Whole file, NEW. Column and value counts match on all 72 INSERTs with no duplicate columns. Every UPDATE uses `WHERE id = '<literal>'` with no duplicate assignments. All 118 JSON literals parse. No generated column is written. All 26 comment timestamps use `YYYY-MM-DDTHH:MM:SSZ`. The snapshot lacks `linear_comments.sequence`, the same advisory mismatch as rev6 (A1). |
| C — Dates, relationships and consistency | PASS | **Clock:** 135 timestamp values; the only 16 after the clock are GCal start/end plan fields (#19–22); latest event is 09-30T22:10:41Z. **Linear chronology:** 21 issues, sequences contiguous, comment times ascending, `updated_at` = latest comment on all 20 updated issues. ZOM-429 has no UPDATE; its base `updated_at` is already later. **Claims:** below. |

### Check C detail: changed records

**`cmt_zom521_2` and ZOM-521 (#85, #86): PASS.** Each claim traced to base.

| Claim | Base evidence |
|---|---|
| "#475" is Calvin's, merged before the comment | #475 by `PERSON_0003_GITHUB_USERNAME`, opened 15:59:05Z, Arthur approved 16:09:09Z, merged 16:09:15Z (`/pull_requests/2380`). Comment is 18 minutes later. |
| It is the card pack animation | PR body "Adding card pack animation". Commits `90e10bc821` and `277746231e`. Merge `0ef583a659` adds `CloseAfterAnimations()`, which calls `TokenTweenPath.StartPath()` on each card: the cards-travel behaviour in ZOM-528's description. Still on main. |
| A build exists to look at | iOS Internal #1756 at 16:14:48Z (`C05433XK267 /1115`) and Android #2025 at 16:16:41Z (`/1116`), both before the comment. |
| Brian had not yet seen it in a build | Calvin 09-29T19:20:08Z asks Brian to test iOS #1746 (`D0770ET6WBW /262`). Brian 19:24:17Z: "I don't have any time to test today. But I'll test it tomorrow" (`/263`), then "it looks great on the video" (`/267`). That DM ends there. |
| Open state is right | ZOM-528 is In Progress, assigned to Calvin, parent ZOM-521, created by Brian. Calvin is also ZOM-521's assignee, so "leaving open" is his call. |
| Calvin was active | Merge commit `2874d2a27c` 15:58:03Z, PR opened 15:59:05Z; 10:27 local on his -06:00 commits. He posted no Slack on 09-30, which is not a conflict. Same window as his `cmt_zom543_1` and `cmt_zom526_3`. |
| Team state convention | Team ZOM states: Done, Todo, Backlog, Canceled, In Progress, Duplicate, In Validation, Regression. All 3 In Validation tickets are analytics (ZOM-442, 548, 549); no VFX ticket under ZOM-521 is in that state. The export has no state history, so a validation step on the Done children cannot be ruled out, but nothing shows one. Staying In Progress pending review fits this line. |

**After the comment, the base agrees with it.** Turkish DM `D0770ET1HV2 /3126–3138` (09-30T16:53–16:57Z). Translations are mine:

- Vincent: "the card animations got merged too in the meantime"; he asks where he can see how they should look.
- Brian answers by forwarding Calvin's video, not a build.
- They then discuss scenarios where the inventory section is not shown: "it looks odd in Zombie Lane", "something similar in quest".

So the item stays open for a real reason, and nothing up to the clock shows Brian testing a build.

**Other injected records:** `cmt_zom521_1` (09-26: "last two items", "Cards VFX is what I am on now") leads into this comment. The unticked "Claimed Cards" line now has a dated explanation, and `cmt_zom526_3` covers the tokens line. SC-15's safer route (child states) agrees: ZOM-526 and ZOM-528 are both In Progress. Rev6's D6 card half is resolved. ZOM-541 is the one gap (F1).

**Trello action (#97): PASS.**

- **Card state and history.** `/cards/781`, open, `dueComplete` false, 0 comments in base. Actions `/actions/5134`, `/5135`, `/5162` are all Leonard's on 09-12, adding "Add more quests", then "and balance quest rewards", then the owners. Leonard's 09-30 sweep set `dueComplete` on other BETA cards but not this one, which fits "if they are ready".
- **Payload.** Keys `board, card, idCard, list, text, textData` match the base commentCard shape. Sub-keys match. Card name equals the card record. List name "BETA: Sep 30" follows every base action on this list (SC-13). ID prefix `68dac820` decodes to 2025-09-29T17:55:44Z, equal to the action date.
- **Author.** Leonard created the card and is named on it. His 09-12 pipeline lists "Add quests and rebalance quest rewards (Leonard, Douglas)" (`C05KNDCHAAG/2025-09 /21`). Slack activity at 17:45:04Z and 18:37:02Z brackets the action.
- **"Mon Oct 13 rollover".** Oct 13 is a Monday, the start of W2. `match3d-quests/lib/quests-stack.ts` has `cronWeeklyRule` at 00:00 on `MON`. The PNs Beta Quests row reads "Rollover / Revisit once new quests roll out".
- **"Nothing in the beta waits on them".** Leonard's 09-12 post names four gating items (Win & Collect, Reward Animations, Season Pass, Infinite HP Boss Mode); quests are not among them. See F2 for the one wrinkle.
- **Does the text hold together?** Yes. "More quests get added" states the additive reading the card name implies, so "the current quests keep running either way" now follows. Rev6's E1 tension is **resolved**.

### Check C detail: byte-identical groups (NEW from source)

| Group | Result | Evidence |
|---|---|---|
| Slack asks (#1–2) | PASS | PNs Beta tab of "Push Notifications Zombie Match" contains all four rows Frederick excludes (rows 2, 8, 10, 11). "Pivot call" fits 09-29 talk in `zombie-design` and the leadership mpdm. |
| Halloween (#3–4, #6) | PASS | Parent thread real. Robert's reversal is later and the brief says the later word counts. |
| Leaderboard retest (#5) vs `cmt_zom429_1` | PASS | Dated supersession of Douglas's 09-16 note, in line with ZOM-429's base bug. Advisory A9. |
| Gmail handoff (#7–18) | PASS | Dates and weekdays correct (Oct 29 Wed, Oct 31 Fri, Nov 1 Sat). The correction reads correctly against the first mail. |
| GCal release (#19–22) | PASS | Consistent with rc_10 and the brief. |
| Brief and deck (#23–33) | PASS | C&W windows match `match3d-backend/lib/zombies_game/win_and_collect.ex` (Mon-Tue, Wed-Thu, Fri-Sun, week start Monday 00:00 UTC). Advisory A6. |
| GitHub notes and mirrors (#38–50) | PASS | rc_10's "DEV stack only" is supported: Owen on 09-26, "no va para release ahora", so Douglas does not deploy (`D05SG9H1CFM /405–409`). No base record says C&W reached prod. The premium-strip and vial notes are uncontradicted author statements. |
| Linear status comments (#51–96) | PASS | ZOM-471: Vincent "it already has start button", Leonard "we don't need it!" (`C0880U9751A/2025-08 /287–288`). ZOM-565: matches its description and `D05U73FNDDL /130–131`, with the comment's 14:34:12Z between those two messages. ZOM-543: `QueueManager.cs` has `Level_end_animations`, `daily_gift`, `season_pass_event`, `unblock_tutorials`. ZOM-549: `nuke_damage_total`, `endless_level`, `total_equipped_power` on endless at `AnalyticsManager.cs:508–510`; no left_level use. ZOM-552: `SeasonPass_premium`, commit `ba194fd16b`. ZOM-442: `trophy_level`, `chest_content` in `ZombieLaneCellBase.cs`. ZOM-534: fix by Oliver and Douglas on 09-10 (`C08R27X0EAH /587–594`). ZOM-566: `D07E9PSQB6W /3`, #477. ZOM-432: PR #471 and submission builds iOS #50 and Android #135 finished before 21:07Z (`/1123`, `/1124`). |
| Tester self-reports (ZOM-504, 517, 546, 556, 542, 344) | PASS, no contradiction | These report an individual's own test or sign-off, so the base cannot positively prove them. Every ticket-ID mention across 2025 Slack was read; none contradicts them. D5 stays open. |

**Cross-statement effects of this revision:** none. #85 and #86 add a later comment and a later `updated_at`. #97 changes only `text`, and #98's values depend only on the action's date and existence.

## 7. Findings and advisories

**No demonstrated defects.**

Each advisory is tagged **[CSC]** (a /prompt reviewer could score it under Cross-Service Coherence) or **[cosmetic]**.

**New in this revision:**

| ID | Tag | Record | Note | Optional fix |
|---|---|---|---|---|
| F1 | CSC | #85 | The comment names ZOM-528 but not **ZOM-541 "Cards Collect Vfx animation"**. That is Marcus's integration ticket for this same work (Brian: "He created a ticket and assigned it to you", `D0770ET6WBW /197`; Calvin: "I still have Marcus's card animation ticket", `/199`). It is In Progress, assigned to Calvin, and #475 is what it asks for. Nothing contradicts the comment, but ZOM-541 now shows the merged-PR, open-ticket pattern with no note, which is what D6 was repaired for. | "I am leaving this item, ZOM-528 and ZOM-541 open until Brian has seen it in a build." One body edit; no other record changes. |
| F2 | CSC | #97 | "Nothing in the beta waits on them" against PNs Beta row 1: Status "Not Ready", Details "Revisit once new quests roll out". The quest **push** can be read as waiting on the new quests. Both are true if the comment means the beat, and the row text is carried over from the Domino sheet. Not a contradiction. Unchanged in meaning from rev6. | "No beat in the beta waits on them, …" |
| F3 | CSC | #97 | "the current quests keep running" touches SC-47 (do not grade Weekly Quests status). The task's own data now settles it, which is the safer direction, but the rubric should lean on this record rather than the base live-ops calendar. | None needed in the SQL. |
| F4 | cosmetic | #85 | "this item" does not name the checklist line, and "card pack animation" differs from "Claimed Cards traveling to inventory Section". `cmt_zom521_1` gives the bridge. | None needed. |
| F5 | cosmetic | #85 | #475's title and branch say "animated icons"; only its body and commits say card pack. The comment uses the accurate wording. | None needed. |
| F6 | cosmetic | #97 | The card also covers "balance quest rewards"; the comment is silent on that half. | None needed. |

**Carried from rev6:**

| ID | Tag | Status | Note |
|---|---|---|---|
| E1 | CSC | **Resolved** | The new Trello text states the additive reading. |
| D6 | CSC | **Resolved, residual in F1** | The cards half is now explained by `cmt_zom521_2`. |
| SC-16 pattern | CSC | Reduced | ZOM-526 and ZOM-528 explained; ZOM-541 remains (F1). |
| A11 | CSC | Improved | SC-15 repair: both unticked items now have dated explanations. |
| A6 | CSC | Unchanged | "Approval from Product … he" against Robert as the approver. |
| N6 | CSC | Unchanged | ZOM-521 "icons" item ticked against `cmt_zom465_2`. |
| D5 | CSC | Unchanged | ZOM-344 Done with no corroborating artefact. |
| D7 | CSC | Unchanged | ZOM-432 closure evidence is indirect. |
| SC-6 | CSC | Unchanged | Brian's address is shared with the Node CEO in base. |
| SC-13 | CSC | Unchanged | List name differs from the action payload. |
| SC-38 | CSC | Unchanged | Season Pass. |
| A1 | cosmetic (deploy-compatibility limit) | Unchanged | Same snapshot-missing column set. |
| A9 | cosmetic | Unchanged | Stmt 5's "current prod build" names no build. |
| A10 | cosmetic | Unchanged | Rules sit in Frederick's DM. |
| N2 | cosmetic | Unchanged | `#468#ev_6` numbering. |
| N4 residual | cosmetic | Unchanged | Base export has no Linear comments, so injected comments start at `sequence` 1. |
| N5 | cosmetic | Unchanged | No `state_history_json` on ZOM-432, ZOM-344 or ZOM-566. |
| D1′ | cosmetic | Unchanged | Native Doc and Sheet have NULL `size`/`content_path`; base native files carry both. |
| D2 | cosmetic | Unchanged | `mbox_from` trailing `\r`, time, header order. |
| D3 | cosmetic | Unchanged | #470 has both an approval and a comment mirror. |
| D4 | cosmetic | Unchanged | Frederick is not a team_ZOM member (ART and ENG only) and comments on ZOM-78. |
| D8 | cosmetic | Unchanged | #473 comment is post-merge, with base precedent. |
| E2 | cosmetic | Unchanged | `cmt_zom544_1` does not name the build tested. |
| E3 | cosmetic | Unchanged | `size_estimate` stays 4312 after the body cut. |
| SC-70 (rev6 "SC-48") | cosmetic | Unchanged, relabelled | Istanbul times. |

## 8. Limits

- **Outside the static scope:** live deploy compatibility (A1), search ranking, visibility and difficulty.
- **Not comparable with the base export:** Gmail `snippet` and `size_estimate`; Linear comments, state history and team privacy. Base attachments marked `surface: comment` show the source once had Linear comments that the export omits; uniqueness is scoped to the reviewed export.
- **Self-report comments:** for the ZOM-504, 517, 546, 556, 542 and 344 rows the check establishes no contradiction, not positive proof.
- **Not re-derived:** the Slack ID formula that rev6's chain mentions. It is not a listed ID contract; collisions were checked directly.
- **Content searches:** Slack was scanned in full for 2025-09 and 2025-10, plus 2025-08 for quest terms and 2025 for ticket IDs. Gmail was scanned in full for ZOM-521, ZOM-528 and the Trello card name (0 hits). Git was read on `main` and across branches where stated.
- **Translations** of the Turkish and Spanish DMs are mine; redacted tokens hide a few words.
- **Evidence chain:** rev6's older report `01dbb84d…` was not available, so its findings were not relied on.
- **Workspace adaptation:** no input store, no output writer and no manifest write.
- No required static check is unresolved.

## 9. Stage dependencies (for reuse)

| Dependency | Value |
|---|---|
| SQL | `091722f6a28117d59d40742adf1c0bbf379dd756c540a9dc79187b87275cb876` |
| Universe manifest | `da2f4cf0…4aac1a` |
| Schema snapshot | `01ef5792…06f6eb` |
| id_contracts | `fc4711ef…ed4682` |
| Known issues | `8895c4dc…961a52` |
| Clock | 2025-10-01T07:00:00Z |
| Lint | injection-lint-v1, 0 flags |

**New base facts recorded this run (with pointers, so later reviews need not rely on a chain):**

- PR #475: Calvin; opened 15:59:05Z; Arthur approved 16:09:09Z, merged 16:09:15Z; merge `0ef583a659`; `CloseAfterAnimations` → `TokenTweenPath.StartPath()`.
- Builds with #475: iOS Internal #1756 (`C05433XK267 /1115`), Android #2025 (`/1116`).
- Brian on testing: `D0770ET6WBW /262–267`. Post-merge QA talk: `D0770ET1HV2 /3126–3138`.
- ZOM-541 (`/issues/3616`) is Marcus's card integration ticket, In Progress, started 09-25T17:44:34Z.
- Quests weekly reset: `match3d-quests/lib/quests-stack.ts` `cronWeeklyRule` 00:00 `MON`.
- C&W windows: `match3d-backend/lib/zombies_game/win_and_collect.ex`. C&W not released as of 09-26: `D05SG9H1CFM /405–409`.
- PNs Beta tab: spreadsheet index 220 "Push Notifications Zombie Match", Quests row "Not Ready / Revisit once new quests roll out".
- Leonard's beta pipeline: `C05KNDCHAAG/2025-09 /21`.

Manifest entry that would be written:

```json
{"review_version": "injection-static-v2", "evidence_contract": "stage-evidence-v1", "input_sha256": "091722f6a28117d59d40742adf1c0bbf379dd756c540a9dc79187b87275cb876", "reused_evidence": [{"source_report": "R/prev/0_injection.rev6.md", "sha256": "6baf29368cca1fc25de7c3acda19bfa66126bf28dcbafd089d0b563d2e102513", "ledger_items": ["§6 Gmail label shape and 5,316 non-reply convention", "§6 PR #472 diff reading", "§6 Axe Arena postponement pointer", "§6 Douglas Google Play note pointer"], "dependencies": {"universe_manifest": "da2f4cf0…4aac1a (unchanged)", "schema_snapshot": "01ef5792…06f6eb (unchanged)", "id_contracts": "fc4711ef…ed4682 (unchanged)", "clock": "2025-10-01T07:00Z (unchanged)", "statements": "byte-identical (statement diff)"}}], "result": "PASS", "execution_status": "COMPLETE"}
```

## 10. Next action

Proceed to `/prompt`. Earlier stage results for `f8d905bd…` are out of date; rerun `/prompt`, `/hardness`, `/oe` and `/rubric` in that order.

Carry F1, F2, F3, A6, A11, N6, D5, D7, SC-6, SC-13 and SC-38 into `/prompt`.

F1 and F2 are optional one-phrase edits to #85 and #97. Neither is needed for this PASS. If either is applied, only the edited statement needs a fresh Check C.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt

Evidence limits: Static scope only. Live deploy compatibility is unverified: the bundled snapshot (`01ef5792…`) lacks several columns the SQL writes (A1). Gmail snippet and size, Linear comments and state history, and team privacy cannot be compared with the base export. Tester self-report comments are checked for contradiction, not positive proof. Rev6's older report `01dbb84d…` was unavailable, so byte-identical statements were re-verified from source; only the four rev6 facts in the manifest entry are reused.
