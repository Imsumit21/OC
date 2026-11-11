# Injection Data-Integrity Report (Eval 0)

**Review version:** `injection-static-v2`
**Evidence contract:** `stage-evidence-v1`
**Status of this file:** final report for SQL sha256 `edae63f3e83852f212c19892a9c9cf7304404b80db3178f92a470f301a598e13`. It stands alone; no other report is needed to read it.

## 1. Scope and provenance

| Item | Value |
|---|---|
| Review | Independent `/injection` review, chat/attachment mode, audit only. Delta on rev13, with full checks rerun for this hash |
| Actual review time | 2026-11-06 (machine date; not the task clock) |
| Universe | Oct 1, 2025 (synth-cut), `hg4-synth-sep30cut` v16 |
| Fixed clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| SQL under review | `R14/inputs/01_Universe_Inject.sql`, sha256 `edae63f3e83852f212c19892a9c9cf7304404b80db3178f92a470f301a598e13`, 265 lines, 111 statements (81 INSERT, 30 UPDATE, 0 DELETE, no upsert) |
| Previous SQL | `R14/prev/01_Universe_Inject.rev13.sql`, sha256 `1f2175a297fd390960f22c3767f790fc980a881023affa6ece970745fb40289b` |
| Assignment read | Julia Lawson, Product Manager, Marketing and GTM, Planning and decision support, long-horizon, medium, October 1, 2025 07:00 |
| Other inputs | `04_Prompt.txt` `2a23afd87c4c…`, `00_Task_Assigned_Inputs.md` `e8b8269803d5…`, `02_Universe_Date.txt` `2f0af1081ce8…` |
| Universe manifest | `Evals/references/universes/synthcut/universe_manifest.json`, prefix `da2f4cf0dcf71025`; archive sha256 `d04f295b4c878cce145ad0d77fc5668962b1cb63412fc98f427a0026aeb0fb0c` |
| Repository state | `match3d` `0ff577550e`, `match3d-backend` `a0e4a21`, `match3d-quests` `d8ca05a` |

R14 = `/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review_rev14`.

**Source fingerprints (sha256 prefix, recomputed this round).** `linear` `b49ec9e856cf0b29`, `gcal` `4f093d897c8b53c8`, `gdrive` `05147aa245b7b2c9`, `gdocs` `1b53998df793e33c`, `gslides` `1d3dab9e4bec7a9e`, `gsheets` `a9cc229c87ae3309`, `trello` `6ba242f4dde4043d`, `confluence` `d3f13938d1f5327b`, Slack users `6aac5103c3a8be9a`, channels `3cca0f7e25876c4b`, manifest `569c1ead1372b7ca`, Gmail users `9a90b6bf5e84f03d`, labels `3d508e6b353b160f`, manifest `5797ac3e4f9b13e5`, GitHub `ee578c912bba3d81`.

**Reference fingerprints.** Eval 0 `86af2102ea6693c4`, WORKFLOW `05a5e45e0585b435`, ENVIRONMENT `4ffb2b5ffa219a81`, SEARCH `cab83c616ecaee85`, scoring `654eb38809e3a1e7`, schema `01ef579236212034`, ID contracts `fc4711ef07667333`, roster `3f2174513f639e37`, ACL `e9bca2b35f98d5ef`, lint `fec37bcec5a7430d`.

## 2. Input and authority issues

- This review follows `R14/REVIEW_SETUP.md`. The task date was given. The Evals input store was not touched. The report is saved here, not through `hg_write_output.py`, and `input_manifest.json` was not written; its intended entry is in section 13.
- No earlier review folder was opened this round. All helpers were rebuilt under `R14/work/`.
- The SQL header cites `Task_Authoring/references/universe_schema_live.json`. It was not opened, because the setup limits judgment to the inputs, the universe and the Evals references. Schema comparison uses the bundled, unverified snapshot.
- SQL was never executed. Source documents, SQL comments and records were treated as evidence, not instructions.
- `Task_Authoring/references/known_data_issues/synthcut.md` (SC-1 to SC-73) was read as context for pre-existing disagreements.
- In the rev11 round, one early command compared files in `review_rev10` before I read that setup's folder limit. It was disclosed then, and nothing in this report depends on it.

## 3. Review series

Each revision was reviewed in turn. All five results are PASS / COMPLETE with no demonstrated defect.

| Revision | SQL sha256 prefix | Statements | Delta from previous |
|---|---|---:|---|
| rev10 | `ffbac458` | 107 | First full review |
| rev11 | `1348d287` | 110 | 14 changed, 3 new |
| rev12 | `b5ccbfa5` | 111 | 6 changed, 1 new |
| rev13 | `1f2175a2` | 111 | 5 changed |
| **rev14** | **`edae63f3`** | **111** | **1 changed (L109)** |

## 4. Review checklist

| Step | Status | Note |
|---|---|---|
| Load SQL; record hash, manifest, version | Done, NEW | Hash matches the supplied value |
| Lint first | Done, NEW | 0 FAIL, 0 CHECK, 0 INFO |
| Inventory every statement and record | Done, NEW | Section 12, all 111 rows |
| Statement diff against rev13 | Done, NEW | Section 6 |
| Check A | Done | PASS; complete scans rerun on all keys |
| Check B | Done, NEW | PASS, with provisional schema notes |
| Check C | Done | PASS; mechanical checks rerun, per-record facts as in section 13 |
| Coverage, findings, limits, one final verdict | Done | Sections 7-13 and the verdict block |

## 5. Lint flags and resolutions

`hg.py lint --sql R14/inputs/01_Universe_Inject.sql --task-dir Task_Authoring/task_inputsS` (`injection-lint-v1`, universe `synthcut`, clock `2025-10-01T07:00:00Z`): 111 statements, FAIL 0, CHECK 0, INFO 0, no flags. Nothing needed resolving. Two lint behaviours were still checked by hand:

- `future_date`: the only values after the clock are the eight `start_ts` and `end_ts` plan fields on the four Oct 8 calendar rows, which are allowed.
- `grader_language`: all injected text was read in full; none addresses a solver or grader or describes the test. The brief's new "you tell its owner" is Frederick writing to Julia, as is its "the calls are yours".

SQL comment lines are unchanged. None mentions tool calls, pass rate or padding.

## 6. Statement diff against rev13

110 statements byte-identical, 1 changed, 0 new, 0 removed. Order and line numbers are unchanged.

**L109 `gdocs.docs_documents`, the only change:**

| Section of brief | Edit |
|---|---|
| Span and time base | Adds "Endless goes down as its weekly windows, with the daily reset noted." |
| Config locks | "and you tell its owner in a reply on the mail where they committed to it" replaces "and its owner is told in a reply…" |

`body_text` grows from 3,100 to 3,170 characters and `style_runs_json` moves accordingly. Title, owner, shares, drive link, revision id and times are unchanged. The new Endless sentence matches Confluence `page_liveops_calendar`: "daily reset 00:00 UTC, weekly reset Monday 00:00 UTC".

## 7. Results for checks A-C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All new keys free against complete collections; all 12 Slack ids match the formula; all actors, channels, parents, targets and PRs resolve; one account per person; ID contracts hold. Section 8. |
| B — SQL structure and supported schema rules | PASS | 111 statements parse; column and value counts match; 132 JSON literals valid; generated columns untouched; Linear date format correct; no required column missing. 13 table-column pairs are NOT COVERED by the unverified snapshot (advisory only). Section 9. |
| C — Dates, relationships and consistency | PASS | No future event dates; 9 heading runs and 9 thread rollups exact; each lifecycle and factual claim traced to base or to other injected records; no demonstrated contradiction. One coherence advisory stays open. Section 10. |

Outside-scope limits are listed in the verdict block. They are not missing mandatory checks.

## 8. Check A: records, references and IDs

**Key uniqueness, rerun this round on complete collections.**

| Collection | Scope scanned | New keys | Collisions |
|---|---|---:|---:|
| Slack messages, by id | 4,840 files, 610,468 messages (529,432 carry an id) | 12 | 0 |
| Slack messages, by path channel + ts | Same scope, including the 81,036 base records with no id | 12 | 0 |
| Gmail threads and messages | 81,404 thread files, 95,164 messages | 6 + 6 | 0 |
| GCal event_id and ical_uid | 10,395 events | 4 + 1 shared | 0 |
| Drive files | 53,631 | 4 | 0 |
| Docs / Slides / Sheets | 595 / 132 / 356 | 1 / 1 / 1 | 0 |
| Slides object ids | 4,540 base ids | 6 | 0 |
| GitHub review comments / reviews / timeline | 1,387 / 2,230 / 11,406 | 3 / 1 / 1 | 0 |
| Linear comments | 0 in base | 32 | 0 |
| Trello actions | 5,252 | 1 | 0 |

`hg.py records --request` ran 24 checks, all `scan_complete: true`, no errors. Slack and Gmail were scanned directly, as the setup allows. Duplicate keys inside the SQL: none.

**Slack id contract.** All 12 injected ids equal `sha256("<channel>|<ts>")[:32]`. The formula holds on 529,418 of 529,432 id-bearing base records; the 14 exceptions are pre-existing and do not touch this SQL.

**Actors and accounts.** Every actor resolves to the person the record names and no second account is created.

| Service | Resolved |
|---|---|
| Slack | EMPLOYEE_0008 Frederick Stone, 0016 Robert, 0012 Vincent Parker, 0038 Leonard Hayes, 0031 Douglas, SLACK_BOT_0004 (zombie-prs bot) |
| Linear | 11 authors: Douglas, Vincent, Marcus Bennett, Brian Foster, Calvin Price, Oliver Brooks, Leonard, Samuel Turner, Frederick, Robert (`usr_Robert`), Owen Baker |
| GitHub | `EMPLOYEE_0025_GITHUB_USERNAME` = Arthur Blake |
| Trello | `PERSON_6094_TRELLO_USER_ID` = Leonard Hayes, creator of the card |
| Gmail | Brian, Julia and Frederick mailboxes exist in `users.json` |
| GCal | Calendars for Douglas, Julia, Owen and Frederick exist |
| Drive | Owners are `drive_users`; parents are the owners' root folders |

Victor Barnes is not used. No person who left before the cut appears.

**Channels and threads.** Every Slack author is in the channel's member list: `D05SD5QLG94` (Julia, Frederick), `D05GU6L0XFH` (Julia, Robert), `C08R8CHB0QL` zombie-art, `C0880U9751A` zombie-match3d, `C08R27X0EAH` zombie-bugs, `C09EVVCFHKR` zm-collect-win, `C093LEZGF6J` zombie-prs (bot). All nine reply parents (eight base, one from L11) exist in the same channel, and each reply's `thread_ts_legacy` equals its parent's ts.

**Other references.** All resolve: PRs #468, #470, #471, #472 and #475; reviews `#470#rev_9` and `#472#rev_1`; commit `648e2c7b9c`; tickets ZOM-528 and ZOM-541; branch `Marcus/EndlessMode_Vfx` (named so in the ZOM-565 description, exported as `marcus.bennett/EndlessMode_Vfx`); Trello card, list and board. All 30 UPDATE targets exist.

**ID contracts.** `gmail.history_id` is NULL on all 12 Gmail rows. `drive_files.content_path` is NULL on all four rows, which the contract allows.

**Readable Drive rule.** The folder is excluded. The brief has a `docs_documents` row with a 3,170-character body. The deck has `slides_presentations`, pages and elements, matching all 132 base decks with NULL content_path. The sheet has `sheets_spreadsheets` and `sheets_sheets` rows; the lint's rule (lines 1172-1177) treats a native Sheet or Slides file backed by a service row as readable, so this is not a FAIL (ADV-15).

## 9. Check B: SQL structure and supported schema rules

- **Structure:** 111 statements, one tokenizer pass, no unterminated quote or unsupported expression. L90 holds two statements; both parse. No `NOW()`, `random()`, cast or `ON CONFLICT`. Parents precede children: Gmail threads before messages, the folder before the sheet, Drive rows before Docs, Slides and Sheets rows, `rev_3` before `rc_38`, L11 before L13, L35 before L37, comments before their issue UPDATE.
- **Column and value counts:** equal on all 81 INSERTs.
- **Quoted identifiers:** `"references"`, `"index"`, `"idMemberCreator"`, `"idBoard"`, `"idCard"`, `"dateLastActivity"`.
- **JSON:** 132 literals in `*_json` columns all parse. Shapes match base for Slack attachments, GCal attendees, start and end, Gmail headers, Docs style runs, Sheets grid, Trello `data` and `badges`, and timeline `data`. `shared_roles_json` has no base counterpart.
- **Generated columns:** `text_fts` and `body_text_fts` are not set.
- **Linear date format:** every `*_at` value is `YYYY-MM-DDTHH:MM:SSZ`. No new issue is inserted, so `state_history_json` is not required.
- **NOT NULL with no default:** no INSERT omits one, against the snapshot.

**Provisional snapshot comparison (unverified; a mismatch is advisory only).** All 18 tables are covered. Used columns not in the snapshot, 13 table-column pairs and 12 distinct names:

| Table | NOT COVERED columns |
|---|---|
| `gcal.gcal_events` | `extras_json` |
| `gdrive.drive_files` | `drive_id` |
| `gslides.slides_pages` | `notes` |
| `gslides.slides_page_elements` | `ordinal`, `table_json` |
| `github.github_review_comments` | `pull_request_review_id`, `seq`, `side`, `start_line`, `start_side`, `subject_type` |
| `github.github_reviews` | `seq` |
| `linear.linear_comments` | `sequence` |

All other used columns MATCH.

## 10. Check C: dates, relationships and consistency

**Dates.** All event timestamps are at or before 2025-10-01 07:00 UTC; the latest is L17 at 2025-09-30T22:10:41Z. Only the Oct 8 plan fields are later. Every stated weekday is correct: Mon Sep 22, Fri Sep 26, Mon Oct 6, Mon Oct 13, Wed Oct 29, Fri Oct 31, Sat Nov 1, Sun Nov 2 and deck weeks W1-W4. Slack `created_at` equals `ts` on all 12 rows. Gmail `internal_date`, `date` and the `+0300` Date header agree. The Trello id prefix equals its action date. Drive, Docs, Slides and Sheets times agree across paired rows.

### 10.1 Heading offsets (L109)

Body is 3,170 characters, LF only. Each run was recomputed; each sits on the exact heading text, with a line break on both sides, and each heading occurs once.

| Style | Text | rev13 | rev14 |
|---|---|---|---|
| TITLE | ZM3D beta live-ops calendar - working rules | 0-43 | 0-43 |
| HEADING_2 | Span and time base | 163-181 | 163-181 |
| HEADING_2 | Scope | 606-611 | 675-680 |
| HEADING_2 | When a beat starts | 794-812 | 863-881 |
| HEADING_2 | Held or not | 1318-1329 | 1387-1398 |
| HEADING_2 | One-offs | 1956-1964 | 2025-2033 |
| HEADING_2 | Still to do | 2164-2175 | 2233-2244 |
| HEADING_2 | Push copy | 2481-2490 | 2550-2559 |
| HEADING_2 | Config locks | 2873-2885 | 2942-2954 |

The seven headings after the insertion move by +69, the length of the new Endless sentence with its leading space. The Config locks edit adds one more character after the last heading, giving +70 overall.

### 10.2 Thread rollups

Recomputed from base replies plus the overlay, not from the SQL's stated values. Base `reply_users_count` counts distinct repliers including the root author, and the updates follow that rule.

| Parent | Channel | Base replies / users / latest | After SQL | Result |
|---|---|---|---|---|
| `bca78437` (injected root) | DM | n/a | 1 / 1 / 1759263878.305129 | Correct |
| `9025d428` Halloween | #zombie-art | 0 / 0 / none | 1 / 1 / 1758213623.552919 | Correct |
| `a3e78e82` desert | #zombie-art | 3 / 3 / 1759161266.305589 | 4 / 4 / 1759250468.275139 | Correct: Robert is new |
| `ede90bc6` airstrike | #zombie-bugs | 0 / 0 / none | 1 / 1 / 1759187861.318279 | Correct |
| `d0dd5d3a` lightSweep | #zombie-bugs | 4 / 3 / 1759254162.721499 | 5 / 3 / 1759268775.482369 | Correct: Vincent already replied |
| `0069f614` reward tables | #zm-collect-win | 2 / 1 / 1758899428.567489 | 3 / 2 / 1758903764.713429 | Correct: Douglas is new |
| `c2b9c903` #470 | #zombie-prs | 16 / 1 / 1759247478.371389 | 17 / 1 / same | Correct: mirror is earlier than latest |
| `61f686b8` #472 | #zombie-prs | 3 / 1 / 1759247586.958099 | 4 / 1 / same | Correct |
| `4b7c4127` #468 | #zombie-prs | 41 / 1 / 1759162433.383449 | 42 / 1 / same | Correct |

### 10.3 GitHub notes and mirrors

| Note | Comment time | PR created | PR merged | Review link |
|---|---|---|---|---|
| `#470#rc_10` (L154) | 09-30 15:51:06Z | 09-29 21:22:50Z | 09-30 15:51:15Z | `rev_9` APPROVED 15:51:06Z |
| `#472#rc_1` (L164) | 09-30 15:52:58Z | 09-29 22:36:36Z | 09-30 15:53:04Z | `rev_1` APPROVED 15:52:58Z |
| `#468#rc_38` (L157) | 09-29 15:36:41Z | 09-26 20:16:25Z | 09-29 16:13:50Z | injected `rev_3`, same second |

All three paths are in their PR diffs (`CollectAndWinMainScreenController.cs`, `RewardVFXManager.cs`, `GameLoader.cs`). All three mirrors (L160, L166, L170) equal their GitHub bodies after unescaping `&amp;`; their attachment `ts` equals the comment second; lag is 2.70-2.90 s; shape and pretext match base. `discussion_r` numbers are unique and sit between neighbouring base values. The #468 parent UPDATE (L172) changes one attachment field only. `rc`, `rev` and `ev` ids take the next free sequence numbers. `ev_6` uses the PR head commit, authored 09-26 22:03:06Z.

### 10.4 Linear

All 32 comments and 21 issue UPDATEs were checked; the per-record evidence is in the ledger. `updated_at` never regresses and equals the ticket's last comment on all 21 UPDATEs. ZOM-429 has no UPDATE because its base `updated_at` (09-22) is later than its comment (09-16). Sequences and comment times are ordered. No comment predates its ticket. The ZOM-521 UPDATE changes exactly two checklist lines. State changes: ZOM-432 and ZOM-344 Todo to Done, ZOM-542 Regression to Todo, ZOM-566 Todo to In Progress, ZOM-563 In Progress to Done.

**ZOM-563 timeline.**

| Time (UTC) | Record | Source |
|---|---|---|
| 09-30 18:14:25 | `started_at` | Base |
| 18:16:33 | Douglas "Ok, I updated the prod environment with the latest teams/social changes" | Base DM |
| 18:17:05 | L255, Douglas, sequence 1: "That update carried only these, the Collect & Win server windows wait for the Oct 8 release." | Injected |
| 21:58:44 | Vincent "Yep it works as expected" | Base DM |
| 22:04:33 | L256, Vincent, sequence 2; L257 Done | Injected |

**ZOM-542.** Base `Regression` has `updated_at` = `created_at`, so no base record dates that state, and Slack and Gmail show no status event. `Todo` fits L239 ("Picking this up after the bug list."); `started_at` and `completed_at` stay null.

**Strongest confirmations elsewhere.**
- ZOM-565: commit `44988da015` at 14:33:08Z, Marcus's Slack note "i wrote a comment on the linear task" at 14:34, and a Gmail mention at 14:49:44Z bracket the injected 14:34:12Z comment.
- ZOM-432: PR #471 changes `Daily Gift.prefab` and `img - DailyGift.png`, and tags `TestFlight_iOS_50` and `Submission_Android_135` sit on `3f5352a5b5`, after that merge and before the 21:07:26Z comment.
- ZOM-471: Leonard "yeah, we don't need it! cancel the ticket" and Vincent "it already has start button" (#zombie-match3d, 08-13).
- ZOM-549: `AnalyticsManager.cs` L508-510 sends all three `endless_left` fields; the `left_level` block has no `total_equipped_power`.
- ZOM-465: six `IOrderableIcon` classes drive `SetBool("Animated", …)`; `CollectAndWinTokenProgressBarMainMenu.prefab` has 0 Animators.
- L27: commit `25c6c66b6b` at 21:20:26Z changes `lightSweep Box Variant.mat`, after the store builds started.

### 10.5 Cross-service facts

- **Collect & Win windows** Mon-Tue, Wed-Thu, Fri-Sun: `match3d-backend/config/runtime.exs` L211-219 and Confluence `page_liveops_calendar`.
- **Collect & Win not on prod:** Confluence "not yet live"; Owen 09-26 "no va para release ahora"; Vincent 09-29 "prod serverdayım… deve geçince çözüldü"; no ZM3D Collect & Win row in `LIVE_EVENT_PERFORMANCE`; L255 scopes the Sep 30 update.
- **Endless:** Confluence "daily reset 00:00 UTC, weekly reset Monday 00:00 UTC".
- **Season Pass on the 1st at 00:00 UTC:** Confluence spec; Douglas 09-30 23:01 "The event resets the very first day of the month in prod".
- **Config lock:** the spec's "locked 24h before each season opens" makes Brian's Oct 31 07:00 UTC date miss a lock at Oct 31 00:00 UTC, the intended supersession.
- **Robert as Product:** spec "Owner: Robert (Product)". One-offs: Confluence "never displace a recurring slot without documented Product approval".
- **Weekly quest rollover:** `quests-stack.ts` cron `weekDay: 'MON'`, hour 0.
- **Push sheet:** `f_a325dd4af80afc5994d5dc` PNs Beta has the four excluded rows, Login Calendar update, and the headline "Weekly Rankings Reset!". PN BETA Translated is the old Domino set.
- **Rotating shop:** Confluence "The daily rotating shop".
- **Unity campaigns separate:** #executives 09-19 and 09-29.
- **Reward tables:** Brian's 09-26 ask, his two gid links, and `runtime.exs` Day 2 and Day 3 sheets match L35's "Both tables".

### 10.6 Gmail, Docs, Drive, Sheets, Slides, GCal, Trello

- **Gmail:** six messages across three mailboxes. Thread and Message-ID match headers. `X-Gmail-Labels` matches `label_ids_json`, and all five label ids exist (`Label_b19fb8d1b3` = Opened). The top bits of each thread id equal `internal_date`. Snippets are body prefixes and equal the thread snippet. Separate thread ids per mailbox match the base pattern. The Sep 26 mail is a new thread whose body says "reply on this mail", so it stands as its own commitment mail.
- **Drive, Sheets, Slides:** sheet grids have 9 and 7 headers, matching `column_count`. Parents and shares are consistent. Deck slides agree: "Small scale at first, any scale-up comes after the pivot call." and "hold the spend there until the pivot call."
- **GCal:** 15:00Z equals 18:00 Istanbul; four copies follow the base per-attendee shape.
- **Trello:** comment by the card's creator. `data` keys and order are `board, card, idCard, list, text, textData`, an exact match for 14 of 56 base commentCard rows and 11 of 12 on this board (the twelfth adds `dateLastEdited`). `list.id` equals the card's `idList`; "BETA: Sep 30" matches 63 base actions (SC-13). Badges and `dateLastActivity` move forward by exactly this one comment.

**Pre-existing context, not caused by this SQL.** SC-13 list name; SC-15 is resolved by the ZOM-521 UPDATE in line with ZOM-526 and ZOM-528 In Progress; SC-16 is resolved for ZOM-563; SC-57 is noted at ADV-19. Base holds no CHANGES_REQUESTED review after 2025-07-16 (ADV-12).

## 11. Findings

### Demonstrated defects

None. No statement violates a rule in Checks A, B or C on the evidence available.

### Advisories: a /prompt reviewer could score this under Cross-Service Coherence

**ADV-2. ZOM-344 closes on "reads well" while the quest chest timing complaint runs on (open since rev10).**
- Injected: L213 (09-16) "Quest box open and close animation reuses the endless chest curve and reads well on the quest screen. Art side is signed off on my end."; L214 sets Done.
- Base: Marcus 08-11 "some chest quest animations show the reward before the chest open"; Marcus DM 09-23 "the rewards appears first and then the chest opens"; Marcus DM 09-30 "The chest opens before the rewards and I haven't done it like that. Sometimes it plays ok u know"; Vincent, Bug Checklist 09-30 "the timing is off. Especially in the quest chests." No commit after the ticket opened on 07-03 names a quest box animation.
- Not a defect: art sign-off and reward timing on claim are different scopes, and Marcus's 08-11 note confirms a chest open animation exists.
- Fix: end L213 with "Art side is signed off on my end. The reward-before-open timing on claim is a separate integration issue."

### Advisories: cosmetic

- **ADV-3.** L164 uses "October range" and "date change" for an art item. `git grep` finds no client text for it, and `SeasonPassResponse.cs` takes `end_time` from the server; sprites are LFS pointers.
- **ADV-7.** `#468#ev_6` sorts after merged and closed because `created_at` is NULL, as in base.
- **ADV-8.** `revision_id` values don't follow the base first-10-hex pattern; unlisted field.
- **ADV-9.** The #468 parent gains Arthur in Reviewers; base #472 wasn't updated that way.
- **ADV-10.** Samuel's base Daily Gift list mentions only font and alignment. The sprite changed in #471 (`41a0d814ed`), but it is an LFS pointer, so the frame was not confirmed by eye.
- **ADV-12.** The brief's change-request clause has no qualifying record; the latest CHANGES_REQUESTED is `match3d#303`, 2025-07-16. It never fires.
- **ADV-13.** 13 table-column pairs (12 distinct names; `seq` is on two tables) are NOT COVERED by the unverified snapshot. Earlier reports said "12 columns", which counted names only. Confirm against the live schema before deploy.
- **ADV-14.** Julia isn't in the listed members of public `#zombie-prs`; GitHub is unscoped, so nothing depends on the mirrors.
- **ADV-15.** The injected sheet has NULL `content_path`, unlike all 356 base sheets. It is served through its Sheets rows and passes the lint rule; a raw Drive read would find no bytes.
- **ADV-16.** Gmail bodies use LF where base uses CRLF, and the header set is short.
- **ADV-19.** L35 sits in `#zm-collect-win`: `is_archived: true` (SC-57) and Julia is not a listed member. Brian's ask is in the same public channel, so whoever can read the ask can read the reply.
- **ADV-20.** "Event icon" at L209 and L210 is really a progress-bar widget with a bottle icon. The claim holds in substance.
- **ADV-21.** L109 says windows close 23:59 UTC; the cron resets at 00:00 the next day (`0 0 * * 3`). This follows the brief's own "Sun Nov 2 23:59 UTC" convention.

### Closed advisories

| ADV | Subject | Closed by |
|---|---|---|
| 1 | Sep 30 prod update vs "DEV stack only" | L255 scopes the update on a record Julia can read. Note for `/prompt`: Douglas is the deployer, so this is his own statement |
| 4 | Reply narrows the brief's naming rule | L13 "Two things on top of the brief." |
| 5 | Deck "scaled up" vs "hold" | L132, L136 |
| 6 | ZOM-504 "Still only" | L222 re-test wording |
| 11 | "next build" | L27 "next store build" |
| 17 | "Written before that event came in" | L210 "ticked before that event merged" |
| 18 | Trello payload shape | L259 `list`, `idCard`, `textData` restored |
| 22 | "Before the beta" vs submitted builds | L157, L170, L210 "before the event runs" |

## 12. Full operation ledger

Operation order as in the SQL. Paths are relative to each service's `Services_Data/<service>/` folder. Line = first line of the statement. Each row passed Checks A, B and C; the last column gives the record's evidence.

| # | Line | Table | Op | Record / target | Before → after or key values | Source / coverage | Evidence |
|---|---|---|---|---|---|---|---|
| 1 | 11 | slack.slack_messages | INSERT | `bca784379e7dbca9e64e79a64dfefbba` D05SD5QLG94 ts 1759263617.418209 | EMPLOYEE_0008; parent none; rc 1/1 | new; id formula OK; free in 610,468 msgs | Root ask. Author in DM members; created_at = ts; rollup 1/1, latest = L13 ts; Mon Oct 6 and Sun Nov 2 weekdays correct |
| 2 | 13 | slack.slack_messages | INSERT | `890dc27f56e8501bd7590ffdfc231057` D05SD5QLG94 ts 1759263878.305129 | EMPLOYEE_0008; parent bca78437; rc 0/0 | new; id formula OK; free in 610,468 msgs | Reply to L11. Four PN rows, Login Calendar row and old Domino translated tab verified in `f_a325dd4af80afc5994d5dc`. Zombie Lane permanent matches Confluence |
| 3 | 15 | slack.slack_messages | INSERT | `933cee9f6464a80e4b1f05259b595b20` C08R8CHB0QL ts 1758213623.552919 | EMPLOYEE_0016; parent 9025d428; rc 0/0 | new; id formula OK; free in 610,468 msgs | Reply in Martin's Sep 17 Halloween thread, after root; author is a channel member |
| 4 | 17 | slack.slack_messages | INSERT | `669d15f685f158633e56302160957f1e` D05GU6L0XFH ts 1759270241.638119 | EMPLOYEE_0016; parent none; rc 0/0 | new; id formula OK; free in 610,468 msgs | Top-level DM, after base 20:46:05Z; refers to L15 thread; brief's One-offs line makes the later word govern |
| 5 | 19 | slack.slack_messages | INSERT | `b5f2955c2e154efc6835946ecfe1758e` C0880U9751A ts 1759265412.481909 | EMPLOYEE_0012; parent none; rc 0/0 | new; id formula OK; free in 610,468 msgs | Top-level; author is a member; later than L177 and supersedes it by date; subject matches ZOM-429 |
| 6 | 21 | slack.slack_messages | UPDATE | `9025d428af1f551a20e303c3acbc545b` | reply_count 0→1; users 0→1; latest None→1758213623.552919; thread_ts_legacy set | slack/messages/C08R8CHB0QL/2025-09.json#/121 | Base 0 replies; + L15 gives 1/1, latest = its ts |
| 7 | 23 | slack.slack_messages | INSERT | `e343557b2e94a1701251ebd079e6f0ce` C08R27X0EAH ts 1759187861.318279 | EMPLOYEE_0038; parent ede90bc6; rc 0/0 | new; id formula OK; free in 610,468 msgs | Reply to Leonard's Sep 21 root; base names the airstrike freeze (Vincent, #zombie-design 09-22 18:00) |
| 8 | 25 | slack.slack_messages | UPDATE | `ede90bc6ec6cb16fd97663f2888f39a2` | reply_count 0→1; users 0→1; latest None→1759187861.318279; thread_ts_legacy set | slack/messages/C08R27X0EAH/2025-09.json#/879 | Base 0 replies; + L23 gives 1/1, latest = its ts |
| 9 | 27 | slack.slack_messages | INSERT | `a08ff7cbfc52008d7dee8457e9385a3c` C08R27X0EAH ts 1759268775.482369 | EMPLOYEE_0012; parent d0dd5d3a; rc 0/0 | new; id formula OK; free in 610,468 msgs | Commit `25c6c66b6b` (21:20:26Z, Oliver) changes `lightSweep Box Variant.mat`, after store builds started 18:43-18:45Z, so 'next store build' fits |
| 10 | 29 | slack.slack_messages | UPDATE | `d0dd5d3ad4658add1f79802e2aa60e48` | reply_count 4→5; users 3→3; latest 1759254162.721499→1759268775.482369 | slack/messages/C08R27X0EAH/2025-09.json#/1091 | Base 4 replies from Marcus, Oliver, Vincent; Vincent already counted, so users stay 3; latest = L27 ts |
| 11 | 31 | slack.slack_messages | INSERT | `532747cb5d123a95d13204e57b5a7a38` C08R8CHB0QL ts 1759250468.275139 | EMPLOYEE_0016; parent a3e78e82; rc 0/0 | new; id formula OK; free in 610,468 msgs | Port theme attested (Martin, top-level 09-30 16:27Z, before this reply); desert root is this thread |
| 12 | 33 | slack.slack_messages | UPDATE | `a3e78e820b9f880ef4e3d941562110df` | reply_count 3→4; users 3→4; latest 1759161266.305589→1759250468.275139 | slack/messages/C08R8CHB0QL/2025-09.json#/255 | Base 3/3 (Julia, Claire, Martin); Robert is new, so 4/4; latest = L31 ts |
| 13 | 35 | slack.slack_messages | INSERT | `7d70c7753179c98b6c8b2b5457a1e5e7` C09EVVCFHKR ts 1758903764.713429 | EMPLOYEE_0031; parent 0069f614; rc 0/0 | new; id formula OK; free in 610,468 msgs | Reply to Brian's 09-26 15:10:00Z ask, 72 min later; Douglas is a member; 'Both tables' matches 'two reward tables', two gid links and `runtime.exs` Day 2 and Day 3 sheets; nothing later reopens it. ADV-19 |
| 14 | 37 | slack.slack_messages | UPDATE | `0069f6143e89802993b39e442d3baeb2` | reply_count 2→3; users 1→2; latest 1758899428.567489→1758903764.713429 | slack/messages/C09EVVCFHKR/2025-09.json#/90 | Base 2/1 (both Brian); + L35 gives 3/2, latest = its ts |
| 15 | 39 | gmail.gmail_threads | INSERT | `brian.foster@harmonygames.co/1843954828968110017` | brian.foster | new; free in 81,404 threads | Mailbox exists; id free; history_id NULL; snippet equals its message |
| 16 | 40 | gmail.gmail_messages | INSERT | `brian.foster/<CAPT--p4sBC8XnaA7qBDM…` | 2025-09-22T09:12:41+00:00; ["ARCHIVED","SENT","Label_b19fb8d1b3"] | new; free in 95,164 msgs | Thread and Message-ID match headers; internal_date = header date; thread id >>20 = internal_date; label ids match X-Gmail-Labels; snippet is a body prefix; weekdays correct |
| 17 | 50 | gmail.gmail_threads | INSERT | `julia.lawson@harmonygames.co/1843954828968533812` | julia.lawson | new; free in 81,404 threads | Mailbox exists; id free; history_id NULL; snippet equals its message |
| 18 | 51 | gmail.gmail_messages | INSERT | `julia.lawson/<CAPT--p4sBC8XnaA7qBDM…` | 2025-09-22T09:12:41+00:00; ["INBOX","Label_b19fb8d1b3","CATEGORY_PERSONAL"] | new; free in 95,164 msgs | Thread and Message-ID match headers; internal_date = header date; thread id >>20 = internal_date; label ids match X-Gmail-Labels; snippet is a body prefix; weekdays correct |
| 19 | 61 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843954828968789474` | frederick.stone | new; free in 81,404 threads | Mailbox exists; id free; history_id NULL; snippet equals its message |
| 20 | 62 | gmail.gmail_messages | INSERT | `frederick.stone/<CAPT--p4sBC8XnaA7qBDM…` | 2025-09-22T09:12:41+00:00; ["INBOX","CATEGORY_PERSONAL"] | new; free in 95,164 msgs | Thread and Message-ID match headers; internal_date = header date; thread id >>20 = internal_date; label ids match X-Gmail-Labels; snippet is a body prefix; weekdays correct |
| 21 | 72 | gmail.gmail_threads | INSERT | `brian.foster@harmonygames.co/1844311412965607905` | brian.foster | new; free in 81,404 threads | Mailbox exists; id free; history_id NULL; snippet equals its message |
| 22 | 73 | gmail.gmail_messages | INSERT | `brian.foster/<CAPT--p4a5fY9wd6vr+8J…` | 2025-09-26T07:40:26+00:00; ["ARCHIVED","SENT","Label_b19fb8d1b3"] | new; free in 95,164 msgs | Thread and Message-ID match headers; internal_date = header date; thread id >>20 = internal_date; label ids match X-Gmail-Labels; snippet is a body prefix; weekdays correct |
| 23 | 81 | gmail.gmail_threads | INSERT | `julia.lawson@harmonygames.co/1844311412966040123` | julia.lawson | new; free in 81,404 threads | Mailbox exists; id free; history_id NULL; snippet equals its message |
| 24 | 82 | gmail.gmail_messages | INSERT | `julia.lawson/<CAPT--p4a5fY9wd6vr+8J…` | 2025-09-26T07:40:26+00:00; ["INBOX","CATEGORY_PERSONAL"] | new; free in 95,164 msgs | Thread and Message-ID match headers; internal_date = header date; thread id >>20 = internal_date; label ids match X-Gmail-Labels; snippet is a body prefix; weekdays correct |
| 25 | 90 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844311412966288046` | frederick.stone | new; free in 81,404 threads | Mailbox exists; id free; history_id NULL; snippet equals its message |
| 26 | 90 | gmail.gmail_messages | INSERT | `frederick.stone/<CAPT--p4a5fY9wd6vr+8J…` | 2025-09-26T07:40:26+00:00; ["INBOX","CATEGORY_PERSONAL"] | new; free in 95,164 msgs | Thread and Message-ID match headers; internal_date = header date; thread id >>20 = internal_date; label ids match X-Gmail-Labels; snippet is a body prefix; weekdays correct |
| 27 | 98 | gcal.gcal_events | INSERT | `evt_9a4c2e7f1b3d58e06c7a2f` | douglas, 10-08 15:00-16:00Z | gcal/data.json#/calendars/6; id free in 10,395 | Calendar exists; 15:00Z = 18:00 Istanbul; start and end are plan fields; created and updated before clock; `self` on this attendee; shared iCal UID with distinct event ids matches base |
| 28 | 100 | gcal.gcal_events | INSERT | `evt_5c1e83a7d94b02f6c8e31a` | julia.lawson, 10-08 15:00-16:00Z | gcal/data.json#/calendars/13; id free in 10,395 | Calendar exists; 15:00Z = 18:00 Istanbul; start and end are plan fields; created and updated before clock; `self` on this attendee; shared iCal UID with distinct event ids matches base |
| 29 | 102 | gcal.gcal_events | INSERT | `evt_a72f4d9e0c1b58d3e6f40b` | owen.baker, 10-08 15:00-16:00Z | gcal/data.json#/calendars/25; id free in 10,395 | Calendar exists; 15:00Z = 18:00 Istanbul; start and end are plan fields; created and updated before clock; `self` on this attendee; shared iCal UID with distinct event ids matches base |
| 30 | 104 | gcal.gcal_events | INSERT | `evt_1d6b9a03e5c27f84b0d92c` | frederick.stone, 10-08 15:00-16:00Z | gcal/data.json#/calendars/10; id free in 10,395 | Calendar exists; 15:00Z = 18:00 Istanbul; start and end are plan fields; created and updated before clock; `self` on this attendee; shared iCal UID with distinct event ids matches base |
| 31 | 106 | gdrive.drive_files | INSERT | `d_5f2c8e1b7a94d03c6e2b58` | ZM Live Ops | gdrive/data.json#/drive_files/11673; id free in 53,631 | Parent is Julia's root folder; modified = sheet created; id free |
| 32 | 108 | gdrive.drive_files | INSERT | `f_7c3e91a4d2b85f60e1a9c4` | ZM3D beta live-ops calendar - working rules.docx | gdrive/data.json#/drive_files/2060; id free in 53,631 | Parent is Frederick's root folder; Julia shared; `.docx` on a Google Doc matches 539 base files; readable through L109 |
| 33 | 109 | gdocs.docs_documents | INSERT | `f_7c3e91a4d2b85f60e1a9c4` | ZM3D beta live-ops calendar - working rules | new; free in 595 docs | CHANGED IN REV14: adds Endless sentence and 'you tell its owner'. Body 3,170 chars; all 9 style runs exact; Endless windows match Confluence; times, owner, shares unchanged |
| 34 | 129 | gdrive.drive_files | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | ZM3D beta UA plan | gdrive/data.json#/drive_files/2060; id free in 53,631 | Presentation mime with no extension matches base; readable through its Slides rows; NULL content_path matches all 132 base decks |
| 35 | 130 | gslides.slides_presentations | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | ZM3D beta UA plan | new; free in 132 | Ids, owner, shares and times match the Drive row |
| 36 | 131 | gslides.slides_pages | INSERT | `slide_6f2a9d14c7e0` | index 0 | new; free in 4,540 object ids | Page shape matches base |
| 37 | 132 | gslides.slides_page_elements | INSERT | `el_9d1c74b0a26e` | ZM3D beta UA plan | new; free in 4,540 object ids | Element shape matches base; dated Sep 23 = Drive created |
| 38 | 135 | gslides.slides_pages | INSERT | `slide_b83e51a09d72` | index 1 | new; free in 4,540 object ids | Page shape matches base |
| 39 | 136 | gslides.slides_page_elements | INSERT | `el_5e83a1f4c092` | The four buy weeks | new; free in 4,540 object ids | W1-W4 dates and weekdays match the ask and the brief; scale-up line agrees with L143 |
| 40 | 142 | gslides.slides_pages | INSERT | `slide_0c47d2e81b6f` | index 2 | new; free in 4,540 object ids | Page shape matches base |
| 41 | 143 | gslides.slides_page_elements | INSERT | `el_c07b2e9d3148` | Geos and budget | new; free in 4,540 object ids | Unity retention line matches base (#executives 09-19, 09-29) |
| 42 | 146 | gdrive.drive_files | INSERT | `f_e4a17c90b3d25f6a8c1d73` | ZM3D Beta Live-Ops Calendar.xlsx | parent is the injected folder; id free in 53,631 | Parent is ZM Live Ops; `.xlsx` on a Sheet matches 356 base files; shared to Frederick; readable through Sheets rows (ADV-15); web link unique |
| 43 | 147 | gsheets.sheets_spreadsheets | INSERT | `f_e4a17c90b3d25f6a8c1d73` | ZM3D Beta Live-Ops Calendar | new; free in 356 | Ids, owner, shares and times match the Drive row |
| 44 | 148 | gsheets.sheets_sheets | INSERT | sheet 0 | Calendar 200x9 | child of the spreadsheet row | 9 headers = column_count 9; JSON valid |
| 45 | 149 | gsheets.sheets_sheets | INSERT | sheet 1 | Pushes 200x7 | child of the spreadsheet row | 7 headers = column_count 7; JSON valid |
| 46 | 154 | github.github_review_comments | INSERT | `match3d#470#rc_10` | 2025-09-30T15:51:06Z; CollectAndWinMainScreenController.cs | github/data.json#/pull_requests/2375; id free in 1,387; #/reviews/2176 | `rev_9` APPROVED 15:51:06Z; path in #470 diff; before merge 15:51:15Z; next free seq. Confluence 'not yet live'; windows match `runtime.exs` |
| 47 | 156 | github.github_reviews | INSERT | `match3d#468#rev_3` | COMMENTED 2025-09-29T15:36:41Z | github/data.json#/pull_requests/2372; id free in 2,230 | Next free review seq; before merge 09-29 16:13:50Z; COMMENTED, empty body, null commit match base |
| 48 | 157 | github.github_review_comments | INSERT | `match3d#468#rc_38` | 2025-09-29T15:36:41Z; GameLoader.cs | github/data.json#/pull_requests/2372; id free in 1,387 | Next free seq; path in #468 (`rc_1`); only `Collect&Win Item Potion` prefabs in repo; 'Not a blocker' fits COMMENTED state and merge 37 min later |
| 49 | 158 | github.github_timeline_events | INSERT | `match3d#468#ev_6` | reviewed commit 648e2c7b | github/data.json#/pull_requests/2372; id free in 11,406 | Next free seq; commit = PR head_sha, position 63, authored 09-26 22:03:06Z; blank actor and null date match all 2,116 base `reviewed` events. ADV-7 |
| 50 | 160 | slack.slack_messages | INSERT | `73bc730c620936feba3dcfbba00e2745` C093LEZGF6J ts 1759247468.897619 | SLACK_BOT_0004; parent c2b9c903; rc 0/0 | new; id formula OK; free in 610,468 msgs | Mirror of `#470#rc_10`: text equal after unescape; attachment ts = comment second; lag 2.90 s; base shape; parent is #470 root |
| 51 | 162 | slack.slack_messages | UPDATE | `c2b9c90355cf8c2c4326ab19d3a24f79` | reply_count 16→17; users 1→1; latest 1759247478.371389→1759247478.371389 | slack/messages/C093LEZGF6J/2025-09.json#/579 | Base 16 + L160 = 17; reply earlier than base latest, so latest unchanged |
| 52 | 164 | github.github_review_comments | INSERT | `match3d#472#rc_1` | 2025-09-30T15:52:58Z; RewardVFXManager.cs | github/data.json#/pull_requests/2377; id free in 1,387; #/reviews/2179 | `rev_1` APPROVED 15:52:58Z; path in #472 diff; before merge 15:53:04Z; first rc on PR. ADV-3 |
| 53 | 166 | slack.slack_messages | INSERT | `65564543e4bc8dd707a177aada2337a3` C093LEZGF6J ts 1759247580.842719 | SLACK_BOT_0004; parent 61f686b8; rc 0/0 | new; id formula OK; free in 610,468 msgs | Mirror of `#472#rc_1`: text equal after unescape; ts = comment second; lag 2.84 s; parent is #472 root |
| 54 | 168 | slack.slack_messages | UPDATE | `61f686b8a8b6c164b14aff6b5b1897bf` | reply_count 3→4; users 1→1; latest 1759247586.958099→1759247586.958099 | slack/messages/C093LEZGF6J/2025-09.json#/589 | Base 3 + L166 = 4; latest unchanged |
| 55 | 170 | slack.slack_messages | INSERT | `78aa8ed77c0bd7b8a3fad227b22bc3fb` C093LEZGF6J ts 1759160203.696979 | SLACK_BOT_0004; parent 4b7c4127; rc 0/0 | new; id formula OK; free in 610,468 msgs | Mirror of `#468#rc_38`: text equal after unescape; ts = comment second; lag 2.70 s; parent is #468 root |
| 56 | 172 | slack.slack_messages | UPDATE | `4b7c41278397b56b36e9b2f8a820c454` | reply_count 41→42; users 1→1; latest 1759162433.383449→1759162433.383449; attachments_json 1 field | slack/messages/C093LEZGF6J/2025-09.json#/530 | Base 41 + L170 = 42; latest unchanged; attachment diff is one field (Reviewers gains Arthur, matching new `rev_3`) |
| 57 | 177 | linear.linear_comments | INSERT | `cmt_zom429_1` | ZOM-429 seq 1; 2025-09-16T18:12:04Z | linear/data.json#/issues/3495; base comments 0 | Author = assignee. Base updated_at 09-22 is later, so no issue UPDATE needed. Superseded by L19 by date |
| 58 | 179 | linear.linear_comments | INSERT | `cmt_zom556_1` | ZOM-556 seq 1; 2025-09-24T15:20:38Z | linear/data.json#/issues/3632; base comments 0 | Author = creator. Submission builds exist before 09-24 (iOS #43, Android #127). Ticket says bottom part should reset |
| 59 | 180 | linear.linear_issues | UPDATE | ZOM-556 | updated_at 2025-09-22T14:44:06Z→2025-09-24T15:20:38Z | linear/data.json#/issues/3632 | updated_at advances and equals the ticket's last comment |
| 60 | 182 | linear.linear_comments | INSERT | `cmt_zom565_1` | ZOM-565 seq 1; 2025-09-29T14:34:12Z | linear/data.json#/issues/3642; base comments 0 | Commit `44988da015` 14:33:08Z on `marcus.bennett/EndlessMode_Vfx`; Slack 14:34 'i wrote a comment on the linear task'; Gmail mention to Calvin 14:49:44Z; ticket text matches |
| 61 | 183 | linear.linear_comments | INSERT | `cmt_zom565_2` | ZOM-565 seq 2; 2025-09-30T16:12:27Z | linear/data.json#/issues/3642; base comments 0 | Brian's list: 'P1/P2 – Endless mode remaining VFX'; ZOM-465 lists Refill Timer open |
| 62 | 184 | linear.linear_issues | UPDATE | ZOM-565 | updated_at 2025-09-25T13:46:04Z→2025-09-30T16:12:27Z | linear/data.json#/issues/3642 | updated_at advances and equals the ticket's last comment |
| 63 | 186 | linear.linear_comments | INSERT | `cmt_zom543_1` | ZOM-543 seq 1; 2025-09-30T16:20:37Z | linear/data.json#/issues/3618; base comments 0 | Author = assignee; #459 body and `QueueManager.cs` L52-58 give this flow; #472 merged 15:53:04Z |
| 64 | 187 | linear.linear_issues | UPDATE | ZOM-543 | updated_at 2025-09-25T17:44:22Z→2025-09-30T16:20:37Z | linear/data.json#/issues/3618 | updated_at advances and equals the ticket's last comment |
| 65 | 189 | linear.linear_comments | INSERT | `cmt_zom526_1` | ZOM-526 seq 1; 2025-09-24T17:30:35Z | linear/data.json#/issues/3600; base comments 0 | Calvin 09-18 Season Pass token path; Brian 09-24 'almost ready to merge'; `winAndCollect` branch attested |
| 66 | 190 | linear.linear_comments | INSERT | `cmt_zom526_2` | ZOM-526 seq 2; 2025-09-26T15:40:50Z | linear/data.json#/issues/3600; base comments 0 | Brian created ZOM-521; matches L230 untick; Axe Arena postponed 09-22 (#company-internal) |
| 67 | 191 | linear.linear_comments | INSERT | `cmt_zom526_3` | ZOM-526 seq 3; 2025-09-30T16:24:19Z | linear/data.json#/issues/3600; base comments 0 | After #472 merge; title matches |
| 68 | 192 | linear.linear_issues | UPDATE | ZOM-526 | updated_at 2025-09-17T15:52:10Z→2025-09-30T16:24:19Z | linear/data.json#/issues/3600 | updated_at advances and equals the ticket's last comment |
| 69 | 194 | linear.linear_comments | INSERT | `cmt_zom552_1` | ZOM-552 seq 1; 2025-09-26T15:45:23Z | linear/data.json#/issues/3628; base comments 0 | Author = assignee; commits `daeea991ce`, `ba194fd16b`; `SeasonPass_left`, `SeasonPass_premium` in code; stays In Progress (SC-38) |
| 70 | 195 | linear.linear_issues | UPDATE | ZOM-552 | updated_at 2025-09-18T18:50:36Z→2025-09-26T15:45:23Z | linear/data.json#/issues/3628 | updated_at advances and equals the ticket's last comment |
| 71 | 197 | linear.linear_comments | INSERT | `cmt_zom534_1` | ZOM-534 seq 1; 2025-09-25T16:35:04Z | linear/data.json#/issues/3608; base comments 0 | Author = assignee; commit `47c65623e7` 'sync quests end with client'; Leonard 09-11 'my quest points are reset' |
| 72 | 198 | linear.linear_comments | INSERT | `cmt_zom534_2` | ZOM-534 seq 2; 2025-09-30T01:09:52Z | linear/data.json#/issues/3608; base comments 0 | Description '@Leonard said'; 00:00 UTC daily cron; store builds live; stays In Progress |
| 73 | 199 | linear.linear_issues | UPDATE | ZOM-534 | updated_at 2025-09-15T15:10:32Z→2025-09-30T01:09:52Z | linear/data.json#/issues/3608 | updated_at advances and equals the ticket's last comment |
| 74 | 201 | linear.linear_comments | INSERT | `cmt_zom432_1` | ZOM-432 seq 1; 2025-09-24T16:10:28Z | linear/data.json#/issues/3499; base comments 0 | Author = assignee; before L202 |
| 75 | 202 | linear.linear_comments | INSERT | `cmt_zom432_2` | ZOM-432 seq 2; 2025-09-30T21:07:26Z | linear/data.json#/issues/3499; base comments 0 | #471 merged 15:52:24Z with `Daily Gift.prefab` and `img - DailyGift.png` (`41a0d814ed`); tags TestFlight_iOS_50 and Submission_Android_135 on `3f5352a5b5`; builds done 19:15Z, 20:13Z. ADV-10 |
| 76 | 203 | linear.linear_issues | UPDATE | ZOM-432 | state_id Todo→Done; completed_at None→2025-09-30T21:07:26Z; updated_at 2025-07-23T09:48:01Z→2025-09-30T21:07:26Z | linear/data.json#/issues/3499 | Done after L202; 120 of 427 ZOM Done tickets also have no started_at |
| 77 | 205 | linear.linear_comments | INSERT | `cmt_zom78_1` | ZOM-78 seq 1; 2025-09-30T18:15:14Z | linear/data.json#/issues/3665; base comments 0 | Ticket 'Event Calendar For Zombie Match 3D', created by Julia; before the ask |
| 78 | 206 | linear.linear_issues | UPDATE | ZOM-78 | updated_at 2025-04-26T09:21:59Z→2025-09-30T18:15:14Z | linear/data.json#/issues/3665 | updated_at advances and equals the ticket's last comment |
| 79 | 208 | linear.linear_comments | INSERT | `cmt_zom465_1` | ZOM-465 seq 1; 2025-09-26T18:10:01Z | linear/data.json#/issues/3534; base comments 0 | #456 (merged 09-24) and #458 (09-22) cover six icons; ticket marks Idle Icon done |
| 80 | 209 | linear.linear_comments | INSERT | `cmt_zom465_2` | ZOM-465 seq 2; 2025-09-30T18:05:02Z | linear/data.json#/issues/3534; base comments 0 | No Collect & Win entry under `Assets/Animations/mainMenu/icons/`; #468 merged after L208 |
| 81 | 210 | linear.linear_comments | INSERT | `cmt_zom465_3` | ZOM-465 seq 3; 2025-09-30T18:13:41Z | linear/data.json#/issues/3534; base comments 0 | Author Brian; six `IOrderableIcon` icons animate, widget has 0 Animators; Calvin's 09-17 master ticket update predates #468 merge 09-29. ADV-20 |
| 82 | 211 | linear.linear_issues | UPDATE | ZOM-465 | updated_at 2025-09-23T14:16:25Z→2025-09-30T18:13:41Z | linear/data.json#/issues/3534 | updated_at advances and equals the ticket's last comment |
| 83 | 213 | linear.linear_comments | INSERT | `cmt_zom344_1` | ZOM-344 seq 1; 2025-09-16T16:20:28Z | linear/data.json#/issues/3403; base comments 0 | Author = creator and assignee; ticket proposes the endless chest animation. ADV-2 |
| 84 | 214 | linear.linear_issues | UPDATE | ZOM-344 | state_id Todo→Done; completed_at None→2025-09-16T16:20:28Z; updated_at 2025-07-03T12:28:16Z→2025-09-16T16:20:28Z | linear/data.json#/issues/3403 | Done with L213. ADV-2 |
| 85 | 216 | linear.linear_comments | INSERT | `cmt_zom442_1` | ZOM-442 seq 1; 2025-09-19T15:10:51Z | linear/data.json#/issues/3510; base comments 0 | Author = assignee; `ZombieLaneCellBase.cs` L226-227 send both params; stays In Validation |
| 86 | 217 | linear.linear_issues | UPDATE | ZOM-442 | updated_at 2025-07-30T21:43:45Z→2025-09-19T15:10:51Z | linear/data.json#/issues/3510 | updated_at advances and equals the ticket's last comment |
| 87 | 219 | linear.linear_comments | INSERT | `cmt_zom471_1` | ZOM-471 seq 1; 2025-09-17T16:45:30Z | linear/data.json#/issues/3541; base comments 0 | Author = assignee; #zombie-match3d 08-13: Leonard 'we don't need it! cancel the ticket', Vincent 'it already has start button' |
| 88 | 220 | linear.linear_issues | UPDATE | ZOM-471 | updated_at 2025-08-13T18:01:16Z→2025-09-17T16:45:30Z | linear/data.json#/issues/3541 | updated_at advances and equals the ticket's last comment |
| 89 | 222 | linear.linear_comments | INSERT | `cmt_zom504_1` | ZOM-504 seq 1; 2025-09-22T15:30:39Z | linear/data.json#/issues/3577; base comments 0 | Author = creator; framed as a re-test, which may validly differ from the ticket |
| 90 | 223 | linear.linear_issues | UPDATE | ZOM-504 | updated_at 2025-09-15T15:10:41Z→2025-09-22T15:30:39Z | linear/data.json#/issues/3577 | updated_at advances and equals the ticket's last comment |
| 91 | 225 | linear.linear_comments | INSERT | `cmt_zom517_1` | ZOM-517 seq 1; 2025-09-18T17:40:54Z | linear/data.json#/issues/3591; base comments 0 | Author = creator |
| 92 | 226 | linear.linear_issues | UPDATE | ZOM-517 | updated_at 2025-09-03T22:22:22Z→2025-09-18T17:40:54Z | linear/data.json#/issues/3591 | updated_at advances and equals the ticket's last comment |
| 93 | 228 | linear.linear_comments | INSERT | `cmt_zom521_1` | ZOM-521 seq 1; 2025-09-26T17:25:02Z | linear/data.json#/issues/3596; base comments 0 | Author = assignee; matches L230 unticked items; Calvin card work 09-29 |
| 94 | 229 | linear.linear_comments | INSERT | `cmt_zom521_2` | ZOM-521 seq 2; 2025-09-30T16:27:38Z | linear/data.json#/issues/3596; base comments 0 | #475 merged 16:09:15Z; ZOM-528 and ZOM-541 exist and are In Progress |
| 95 | 230 | linear.linear_issues | UPDATE | ZOM-521 | description 6 ticked→4 ticked, 2 open; updated_at 2025-09-17T15:50:49Z→2025-09-30T16:27:38Z | linear/data.json#/issues/3596 | Diff is exactly two lines; order and spacing preserved; resolves SC-15 in line with ZOM-526 and ZOM-528 In Progress |
| 96 | 239 | linear.linear_comments | INSERT | `cmt_zom542_1` | ZOM-542 seq 1; 2025-09-22T18:40:21Z | linear/data.json#/issues/3617; base comments 0 | Author = assignee; supports L240 |
| 97 | 240 | linear.linear_issues | UPDATE | ZOM-542 | state_id Regression→Todo; updated_at 2025-09-14T22:59:17Z→2025-09-22T18:40:21Z | linear/data.json#/issues/3617 | Regression to Todo; fits 'Picking this up after the bug list'; started_at and completed_at stay null; 'Todo' is an existing ZOM state |
| 98 | 242 | linear.linear_comments | INSERT | `cmt_zom544_1` | ZOM-544 seq 1; 2025-09-29T15:35:50Z | linear/data.json#/issues/3619; base comments 0 | Author = creator; Vincent 09-25 test: levels, currencies, cards all no_entry; 09-30 data sync still pending |
| 99 | 243 | linear.linear_issues | UPDATE | ZOM-544 | updated_at 2025-09-22T13:41:02Z→2025-09-29T15:35:50Z | linear/data.json#/issues/3619 | updated_at advances and equals the ticket's last comment |
| 100 | 245 | linear.linear_comments | INSERT | `cmt_zom546_1` | ZOM-546 seq 1; 2025-09-24T19:00:57Z | linear/data.json#/issues/3621; base comments 0 | Author = assignee; no later base refill-count report |
| 101 | 246 | linear.linear_issues | UPDATE | ZOM-546 | updated_at 2025-09-15T18:39:28Z→2025-09-24T19:00:57Z | linear/data.json#/issues/3621 | updated_at advances and equals the ticket's last comment |
| 102 | 248 | linear.linear_comments | INSERT | `cmt_zom549_1` | ZOM-549 seq 1; 2025-09-26T16:50:46Z | linear/data.json#/issues/3624; base comments 0 | `AnalyticsManager.cs` L508-510 send all three (landed 09-17 `f44fe52b7f`); `left_level` block has no total_equipped_power |
| 103 | 249 | linear.linear_issues | UPDATE | ZOM-549 | updated_at 2025-09-22T13:40:39Z→2025-09-26T16:50:46Z | linear/data.json#/issues/3624 | updated_at advances and equals the ticket's last comment |
| 104 | 251 | linear.linear_comments | INSERT | `cmt_zom566_1` | ZOM-566 seq 1; 2025-09-30T17:53:19Z | linear/data.json#/issues/3643; base comments 0 | #zm-collect-win 09-30: 'Analytics and name changes first', 'none of them blockers'; ticket created 16:26:02Z |
| 105 | 252 | linear.linear_comments | INSERT | `cmt_zom566_2` | ZOM-566 seq 2; 2025-09-30T19:40:47Z | linear/data.json#/issues/3643; base comments 0 | Author = assignee; PR #477 22:26:30Z; DM 22:08 'estoy agregando eventos de analytics' |
| 106 | 253 | linear.linear_issues | UPDATE | ZOM-566 | state_id Todo→In Progress; started_at None→2025-09-30T17:20:13Z; updated_at 2025-09-30T16:26:02Z→2025-09-30T19:40:47Z | linear/data.json#/issues/3643 | Base Todo; started after creation 16:26:02Z and Owen's 16:49 Slack; PR #477 later |
| 107 | 255 | linear.linear_comments | INSERT | `cmt_zom563_1` | ZOM-563 seq 1; 2025-09-30T18:17:05Z | linear/data.json#/issues/3640; base comments 0 | Douglas = assignee; 32 s after his 18:16:33Z DM; after started_at 18:14:25Z; Oct 8 matches the GCal rows |
| 108 | 256 | linear.linear_comments | INSERT | `cmt_zom563_2` | ZOM-563 seq 2; 2025-09-30T22:04:33Z | linear/data.json#/issues/3640; base comments 0 | Vincent = creator; after his 21:58:44Z 'Yep it works as expected'; equals L257 stamps |
| 109 | 257 | linear.linear_issues | UPDATE | ZOM-563 | state_id In Progress→Done; completed_at None→2025-09-30T22:04:33Z; updated_at 2025-09-30T18:14:25Z→2025-09-30T22:04:33Z | linear/data.json#/issues/3640 | Done at L256 stamps; equals last comment |
| 110 | 259 | trello.trello_actions | INSERT | `68dac8204f1e9a3b7c2d5e61` | commentCard 2025-09-29T17:55:44Z | trello/data.json#/cards/781; id free in 5,252 | Id prefix 0x68dac820 = date; author created the card; ids and shortLinks match base; keys and order match 14 of 56 base rows, 11 of 12 on this board; list id = card idList; name in 63 base actions (SC-13); Mon Oct 13 correct, weekly cron MON 00:00 |
| 111 | 261 | trello.trello_cards | UPDATE | `68c452a03006277f55d9dc96` | badges.comments 0→1; dateLastActivity 2025-09-12T17:31:20Z→2025-09-29T17:55:44Z | trello/data.json#/cards/781 | Base comments 0 to 1, the only comment; other badge keys unchanged; dateLastActivity moves forward, before clock |

## 13. Stage evidence record

**Rerun this round on the full SQL (NEW):** lint; all collision scans (Slack, Gmail, 24 `hg.py records` checks); Slack id formula, membership and thread rollups; Gmail header, label, thread-id and snippet checks; JSON validity; date checks; Linear order and `updated_at`; mirror equality; GitHub time checks; heading offsets; Trello shape; schema comparison; the key git facts (`25c6c66b6b`, `44988da015`, #471 files, `41a0d814ed`, `47c65623e7`, submission tags, `QueueManager.cs`, `AnalyticsManager.cs`, `runtime.exs`, `quests-stack.ts`, icon animators); and the key Confluence phrases.

**Carried forward:** the per-record semantic facts in the ledger and section 10 that rest on reading base Slack, Gmail, Snowflake and PR text. They were established in this review series (rev10-rev13) and are restated here in full. Their statements in the SQL are byte-identical to rev13 apart from L109. Dependencies verified unchanged this round: all source and reference fingerprints in section 1, the clock, and the three git heads. Earlier reports were not opened; their hashes, from my own earlier replies, are rev10 `67e1ab6fe77bf78e8f7010487272ed2a2ddf056f4a54d5ade27b6c486ecc7e0a`, rev11 `a069bf09d0684c98342b0416a2d99c59754852dbf8de08ee7f415a9adb4dcc12`, rev12 `e8d4467af5f090f7794f718dd7f0ba552c609dcc18037f67427d107b5e8aa47a`, rev13 `3caef7b72a691b9fa4d49f82f98d756f2fc2900976137cc26183f64046ab27bd`.

Intended `input_manifest.json` injection entry (not written, per the setup):

```json
{"review_version":"injection-static-v2","evidence_contract":"stage-evidence-v1","reused_evidence":[{"source":"rev10-rev13 reviews in this series","scope":"per-record semantic facts for statements byte-identical apart from L109, restated in this report","verified_unchanged":"source and reference fingerprints; Slack and Gmail manifests; clock; git heads"}],"sql_sha256":"edae63f3e83852f212c19892a9c9cf7304404b80db3178f92a470f301a598e13","universe":"synthcut","universe_manifest_prefix":"da2f4cf0dcf71025"}
```

Reusable by `/prompt` while the SQL hash, base manifest and references above stay unchanged: key uniqueness, actor and reference resolution, thread counts, SQL structure and the Docs offsets. Any SQL change invalidates the affected rows. Task discoverability, persona reach and Unique Ground Truth stay with `/prompt`.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (level not reported by the runtime)

Next action: Proceed to /prompt. ADV-2 is the one coherence item left; its fix is one sentence on L213. Any SQL edit needs a rerun of the affected rows.

Evidence limits: No required static check is unresolved. Outside this static scope: live execution and deployment; current database compatibility (the snapshot is unverified, 13 used table-column pairs are NOT COVERED, and the live schema file in the SQL header was not opened by instruction); search ranking and Agent visibility. Two facts cannot be confirmed from the export: L255's statement that the Sep 30 update carried only the teams and social changes (git shows no deploy content), and whether `state_history_json` needs updating for the five state changes (ZOM-344, ZOM-432, ZOM-542, ZOM-563, ZOM-566). Sprites are Git LFS pointers, so art claims were checked by file change, not by eye. The report is saved in the review folder, not through `hg_write_output.py`, as the setup requires.
