# Injection Data-Integrity Report (Eval 0)

**Review version:** `injection-static-v2`
**Evidence contract:** `stage-evidence-v1` (`reused_evidence: []`; every item below is NEW)

## 1. Scope and provenance

| Item | Value |
|---|---|
| Review | Independent `/injection` review, chat/attachment mode, audit only |
| Actual review time | 2026-11-06 (machine clock 2026-11-06T11:08Z; not the task clock) |
| Universe | Oct 1, 2025 (synth-cut), `hg4-synth-sep30cut` v16 |
| Fixed clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Injection SQL | `R/inputs/01_Universe_Inject.sql`, sha256 `1f2175a297fd390960f22c3767f790fc980a881023affa6ece970745fb40289b`, 259 lines |
| Assignment read | Julia Lawson, Product Manager, Marketing and GTM, Planning and decision support, long-horizon, medium, October 1, 2025 07:00 |
| Universe manifest | `Evals/references/universes/synthcut/universe_manifest.json`, sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`; archive sha256 `d04f295b4c878cce145ad0d77fc5668962b1cb63412fc98f427a0026aeb0fb0c` |
| Repository state | Workspace commit `f97a36c`; `match3d` HEAD `0ff577550e`; `match3d-backend` HEAD `a0e4a21`; `match3d-quests` HEAD `d8ca05a` |
| Run location | Review folder R = `/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review_rev10` |

Source file fingerprints (sha256, first 16 hex; the routes table in `hg.py reference guide` carries the same values for Slack, Linear, GCal, GDrive, GDocs, GSlides, GSheets, GitHub and Trello):

| Source | Hash |
|---|---|
| `linear/data.json` | `b49ec9e856cf0b29` |
| `gcal/data.json` | `4f093d897c8b53c8` |
| `gdrive/data.json` | `05147aa245b7b2c9` |
| `gdocs/data.json` | `1b53998df793e33c` |
| `gslides/data.json` | `1d3dab9e4bec7a9e` |
| `gsheets/data.json` | `a9cc229c87ae3309` |
| `trello/data.json` | `6ba242f4dde4043d` |
| `confluence/confluence_working.json` | `d3f13938d1f5327b` |
| `slack/users.json`, `slack/channels.json` | `6aac5103c3a8be9a`, `3cca0f7e25876c4b` |
| `gmail/users.json`, `gmail/labels.json` | `9a90b6bf5e84f03d`, `3d508e6b353b160f` |
| `github/data.json` | `ee578c912bba3d81` |

Reference fingerprints: `Evals/0_Injection_Quality_Eval.md` `86af2102ea6693c4`, `Evals/WORKFLOW.md` `05a5e45e0585b435`, `Evals/ENVIRONMENT.md` `4ffb2b5ffa219a81`, `Evals/SEARCH.md` `cab83c616ecaee85`, `Evals/references/rules/scoring.json` `654eb38809e3a1e7`, `Evals/references/schema/injection.json` `01ef579236212034`, `Evals/references/schema/id_contracts.json` `fc4711ef07667333`, `Evals/references/persona/roster.json` `3f2174513f639e37`, `Evals/references/persona/acl.md` `e9bca2b35f98d5ef`, `Evals/tools/hg_injection_lint.py` `fec37bcec5a7430d`.

## 2. Input and authority issues

- The review setup overrides the skill's intake and save steps. The task date was given as Oct 1, 2025 (synth-cut), the Evals input store was not touched, and this report is saved to `R/out/0_injection.md` instead of `Evals/task_inputs/reports/`. `input_manifest.json` was therefore not written; its intended entry is in section 11.
- The SQL header cites `Task_Authoring/references/universe_schema_live.json`. It was not opened, because the setup limits judgment to the inputs, the universe and the Evals references. Schema comparison below uses the bundled, unverified snapshot only.
- Source documents, SQL comments and records were treated as evidence, not instructions. The SQL was never executed.
- `Task_Authoring/references/known_data_issues/synthcut.md` (SC-1 to SC-73) was read as context for pre-existing disagreements.

## 3. Review checklist

| Step | Status | Note |
|---|---|---|
| Load SQL; record hash, base manifest, review version | Done, NEW | Hash matches the setup value |
| Run the lint first | Done, NEW | 0 FAIL, 0 CHECK, 0 INFO |
| Inventory every statement and record | Done, NEW | 107 statements: 78 INSERT, 29 UPDATE, 0 DELETE, no upsert clause; section 10 |
| Check A | Done, NEW | PASS |
| Check B | Done, NEW | PASS, with provisional schema notes |
| Check C | Done, NEW | PASS |
| Coverage, findings, limits, one final verdict | Done, NEW | Sections 5-11 |

## 4. Lint flags and resolutions

Command: `hg.py lint --sql R/inputs/01_Universe_Inject.sql --task-dir Task_Authoring/task_inputsS` (`hg_injection_lint`, `injection-lint-v1`, universe `synthcut`, clock `2025-10-01T07:00:00Z`).

Result: 107 statements, FAIL 0, CHECK 0, INFO 0, no flags. Base files used: Slack users, Gmail users, GitHub, Linear, Trello, Contacts, Confluence. Nothing needed resolving. Two lint behaviours were still checked by hand:

- `future_date`: the only values after the clock are the eight `start_ts`/`end_ts` plan fields on the four Oct 8 calendar rows, which are allowed. Every event timestamp is at or before the clock.
- `grader_language`: no flag. All injected text was read in full. The closest phrase, "Two things the brief does not spell out." (L13), is Frederick writing to Julia about his own brief and then supplying the two points; it is not addressed to a solver or grader and does not describe the test. See ADV-4.

## 5. Results for checks A-C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All new keys free against complete collections; all 11 Slack ids match the formula; all actors, channels, parents, targets and PRs resolve; one account per person; ID contracts hold. Section 6. |
| B — SQL structure and supported schema rules | PASS | 107 statements parse; column and value counts match; 128 JSON literals valid; generated columns untouched; Linear date format correct; no required column missing. 12 columns are NOT COVERED by the unverified snapshot (advisory only). Section 7. |
| C — Dates, relationships and consistency | PASS | No future event dates; all thread counts and ordering correct; each lifecycle and factual claim traced to base or to other injected records; no demonstrated contradiction. Six coherence advisories recorded. Section 8. |

Outside-scope limits are listed in the verdict block. They are not missing mandatory checks.

## 6. Check A: records, references and IDs

**Key uniqueness (complete collections, NEW).**

| Collection | Scope scanned | New keys | Collisions |
|---|---|---:|---:|
| Slack messages, by id | 4,840 files, 610,468 messages (529,432 carry an id) | 11 | 0 |
| Slack messages, by path channel + ts | Same scope, including the 81,036 base records with no id | 11 | 0 |
| Gmail threads and messages | 81,404 thread files, 95,164 messages | 6 + 6 | 0 |
| GCal event_id and ical_uid | 10,395 events | 4 + 1 shared | 0 |
| Drive files | 53,631 | 4 | 0 |
| Docs / Slides / Sheets | 595 / 132 / 356 | 1 / 1 / 1 | 0 |
| Slides object ids | 4,540 base ids | 6 | 0 |
| GitHub review comments / reviews / timeline | 1,387 / 2,230 / 11,406 | 3 / 1 / 1 | 0 |
| Linear comments | 0 in base | 30 | 0 |
| Trello actions | 5,252 | 1 | 0 |

`hg.py records --request` ran 24 checks across these services and returned `scan_complete: true` for all, no errors. Slack and Gmail were scanned directly, as the setup allows. Duplicate keys inside the SQL: none.

**Slack id contract.** All 11 injected ids equal `sha256("<channel>|<ts>")[:32]`. The same formula holds on 529,418 of 529,432 id-bearing base records; the 14 exceptions are pre-existing and do not touch this SQL.

**Actors and accounts.** Every actor resolves to the person the record names and no second account is created.

| Service | Resolved |
|---|---|
| Slack | EMPLOYEE_0008 Frederick Stone, 0016 Robert, 0012 Vincent Parker, 0038 Leonard Hayes, SLACK_BOT_0004 (zombie-prs bot) |
| Linear | 11 authors: Douglas, Vincent, Marcus Bennett, Brian Foster, Calvin Price, Oliver Brooks, Leonard, Samuel Turner, Frederick, Robert (`usr_Robert`), Owen Baker |
| GitHub | `EMPLOYEE_0025_GITHUB_USERNAME` = Arthur Blake |
| Trello | `PERSON_6094_TRELLO_USER_ID` = Leonard Hayes, creator of the card |
| Gmail | Brian, Julia and Frederick mailboxes exist in `users.json` |
| GCal | Calendars for Douglas, Julia, Owen and Frederick exist |
| Drive | Owners are `drive_users`; parents are the owners' root folders |

Victor Barnes is not used. No person who left before the cut appears.

**Channels and threads.** Each author is in the channel's member list: `D05SD5QLG94` (Julia, Frederick), `D05GU6L0XFH` (Julia, Robert), `C08R8CHB0QL` zombie-art, `C0880U9751A` zombie-match3d, `C08R27X0EAH` zombie-bugs, `C093LEZGF6J` zombie-prs (bot). All seven reply parents exist in the same channel, and each reply's `thread_ts_legacy` equals its parent's ts.

**Other references.** PRs #468, #470, #471, #472 and #475, reviews `#470#rev_9` and `#472#rev_1`, commit `648e2c7b9c`, tickets ZOM-528 and ZOM-541, branch `Marcus/EndlessMode_Vfx` (named so in the ZOM-565 description; exported as `marcus.bennett/EndlessMode_Vfx`), card `68c452a03006277f55d9dc96`, list and board ids all resolve. All 29 UPDATE targets exist.

**ID contracts.** `gmail.history_id` is NULL on all 12 Gmail rows. `drive_files.content_path` is NULL on all four rows, which the contract allows.

**Readable Drive rule.** The folder is excluded. The brief has a `docs_documents` row with a 2,802-character body. The deck has `slides_presentations`, pages and elements, matching all 132 base decks with NULL content_path. The sheet has `sheets_spreadsheets` and `sheets_sheets` rows. The lint's own rule (lines 1172-1177) treats a native Sheet or Slides file backed by a service row as readable, so this is not a FAIL. See ADV-15.

## 7. Check B: SQL structure and supported schema rules

- **Structure:** 107 statements, one tokenizer pass, no unterminated quote, no unsupported expression. Line 86 holds two statements; both parse. No `NOW()`, `random()`, cast or `ON CONFLICT`. Parents precede children: Gmail threads before messages, the folder before the sheet, Drive rows before Docs, Slides and Sheets rows, `rev_3` before `rc_38`, L11 before L13.
- **Column and value counts:** equal on all 78 INSERTs.
- **Quoted identifiers:** `"references"`, `"index"`, `"idMemberCreator"`, `"idBoard"`, `"idCard"`, `"dateLastActivity"` are quoted.
- **JSON:** 128 literals in `*_json` columns all parse. Shapes were compared with base records: Slack attachments, GCal attendees, start and end, Gmail headers, Docs style runs, Sheets grid, Trello `data` and `badges`, timeline `data`. All match, except `shared_roles_json`, which has no base counterpart (`shared_with_emails` is the export field).
- **Generated columns:** `text_fts` and `body_text_fts` are not set.
- **Linear date format:** every `*_at` value is `YYYY-MM-DDTHH:MM:SSZ`. No new issue is inserted, so `state_history_json` is not required.
- **NOT NULL with no default:** no INSERT omits one, against the snapshot.

**Provisional snapshot comparison (unverified; a mismatch is advisory only).** All tables are covered. Used columns not in the snapshot:

| Table | NOT COVERED columns |
|---|---|
| `gcal.gcal_events` | `extras_json` |
| `gdrive.drive_files` | `drive_id` |
| `gslides.slides_pages` | `notes` |
| `gslides.slides_page_elements` | `ordinal`, `table_json` |
| `github.github_review_comments` | `pull_request_review_id`, `seq`, `side`, `start_line`, `start_side`, `subject_type` |
| `github.github_reviews` | `seq` |
| `linear.linear_comments` | `sequence` |

All other used columns MATCH. See ADV-13.

## 8. Check C: dates, relationships and consistency

**Dates.** All event timestamps are at or before 2025-10-01 07:00 UTC; the latest is Linear `ZOM-563` at 2025-09-30T22:04:33Z. Only the Oct 8 plan fields are later. Every stated weekday is correct: Mon Sep 22, Fri Sep 26, Mon Oct 6, Mon Oct 13, Wed Oct 29, Fri Oct 31, Sat Nov 1, Sun Nov 2 and deck weeks W1-W4. Slack `created_at` equals `ts` on all 11 rows. Gmail `internal_date`, `date` and the `+0300` Date header agree. Trello id prefix equals its action date. Drive, Docs, Slides and Sheets created and modified times agree across their paired rows.

**Thread updates.**

| Parent | Base replies / users / latest | After SQL | Result |
|---|---|---|---|
| `bca78437` (new root) | n/a | 1 / 1 / L13 ts | Correct |
| `9025d428` Halloween | 0 / 0 / none | 1 / 1 / L15 ts | Correct |
| `ede90bc6` airstrike | 0 / 0 / none | 1 / 1 / L23 ts | Correct |
| `d0dd5d3a` lightSweep | 4 / 3 / 1759254162.721499 | 5 / 3 / L27 ts | Correct: Vincent already replied |
| `a3e78e82` desert | 3 / 3 / 1759161266.305589 | 4 / 4 / L31 ts | Correct: Robert is new |
| `c2b9c903` #470 | 16 / 1 / 1759247478.371389 | 17 / 1 / same | Correct: L156 is earlier than latest |
| `61f686b8` #472 | 3 / 1 / 1759247586.958099 | 4 / 1 / same | Correct: L162 is earlier than latest |
| `4b7c4127` #468 | 41 / 1 / 1759162433.383449 | 42 / 1 / same | Correct: L166 is earlier than latest |

Base `reply_users_count` counts distinct repliers including the root author, and the updates follow that rule. Every reply follows its parent.

**GitHub notes against PR times.**

| Note | Comment time | PR created | PR merged | Review link |
|---|---|---|---|---|
| `#470#rc_10` | 09-30 15:51:06Z | 09-29 21:22:50Z | 09-30 15:51:15Z | `rev_9` APPROVED 15:51:06Z |
| `#472#rc_1` | 09-30 15:52:58Z | 09-29 22:36:36Z | 09-30 15:53:04Z | `rev_1` APPROVED 15:52:58Z |
| `#468#rc_38` | 09-29 15:36:41Z | 09-26 20:16:25Z | 09-29 16:13:50Z | new `rev_3`, same second |

All three paths are in their PR diffs (`CollectAndWinMainScreenController.cs`, `RewardVFXManager.cs`, `GameLoader.cs`). The three mirrors carry the note text, the comment-second `ts`, a 2.7-2.9 s lag, and the base attachment shape and pretext form. Their `discussion_r` numbers are unique and sit between neighbouring base values. The #468 parent UPDATE changes one attachment field only.

**Linear.** Each comment was checked against its ticket and against commits, PRs and Slack including private DMs; the per-record evidence is in the ledger. `updated_at` never regresses and equals the ticket's last comment on all 21 UPDATEs. ZOM-429 has no UPDATE because its base `updated_at` (09-22) is already later than its comment (09-16). Sequences and comment times are ordered. No comment predates its ticket. The ZOM-521 UPDATE changes exactly two checklist lines and preserves the rest byte for byte. Strongest confirmations:

- ZOM-565: Marcus's commit `44988da015` at 14:33:08Z, his Slack note "i wrote a comment on the linear task" at 14:34, and the 14:49:44Z Gmail mention all bracket the injected 14:34:12Z comment.
- ZOM-563: Douglas's 18:16 prod update and Vincent's 21:58 "Yep it works as expected" precede the 22:04:33Z close.
- ZOM-432: PR #471 changes `Daily Gift.prefab` and `img - DailyGift.png`, and tags `TestFlight_iOS_50` and `Submission_Android_135` sit on `3f5352a5b5`, after that merge and before the 21:07:26Z comment.
- ZOM-471: Leonard's "yeah, we don't need it! cancel the ticket" and Vincent's "it already has start button" (#zombie-match3d, 08-13).
- ZOM-549: `AnalyticsManager.cs` L508-510 sends all three `endless_left` fields, and the `left_level` block has no `total_equipped_power`.
- Vincent's L27 lightSweep reply: commit `25c6c66b6b` at 21:20:26Z does change `lightSweep Box Variant.mat`.

**Cross-service facts.**

- Collect & Win windows Mon-Tue, Wed-Thu, Fri-Sun: `match3d-backend/config/runtime.exs` L211-219 and Confluence `page_liveops_calendar`.
- Collect & Win not on prod: Confluence "not yet live", Owen's 09-26 "no va para release ahora", Vincent's 09-29 "prod serverdayım… deve geçince çözüldü", and no ZM3D Collect & Win row in `LIVE_EVENT_PERFORMANCE`. See ADV-1.
- Season Pass on the 1st at 00:00 UTC: Confluence spec; Douglas 09-30 23:01 "The event resets the very first day of the month in prod".
- Config lock: the spec's 24h freeze makes Brian's Oct 31 07:00 UTC date miss a lock at Oct 31 00:00 UTC, which is the intended supersession.
- Robert as Product: spec "Owner: Robert (Product)".
- Weekly quest rollover: `quests-stack.ts` cron `weekDay: 'MON'`, hour 0.
- Unity campaigns separate: #executives 09-19 and 09-29.

**Gmail.** Six messages across three mailboxes. Thread and Message-ID match the headers. `X-Gmail-Labels` matches `label_ids_json`, and all five label ids exist (`Label_b19fb8d1b3` = Opened). The top bits of each thread id equal `internal_date`. Snippets are prefixes of the flattened body and equal the thread snippet. Separate thread ids per mailbox match the base pattern (Julia and Frederick copy of 2025-05-08). The Sep 26 mail is a new thread, not a reply, and its body says "reply on this mail", so it stands as its own commitment mail.

**Docs, Drive, Sheets, Slides, GCal, Trello.** All nine style runs sit exactly on their heading text with a line break on each side. The sheet grids have 9 and 7 headers, matching `column_count`. Parents and shares are consistent. GCal 15:00Z equals 18:00 Istanbul, and the four copies follow the base per-attendee shape. Trello's comment is by the card's creator, its list name matches the 63 base actions that say "BETA: Sep 30" (SC-13), and badges and `dateLastActivity` move forward by exactly that one comment.

**Pre-existing context, not caused by this SQL.** SC-13 list name; SC-15 is resolved by the ZOM-521 UPDATE in line with ZOM-526 and ZOM-528 In Progress; SC-16 is resolved for ZOM-563. Base holds no CHANGES_REQUESTED review after 2025-07-16 (ADV-12).

## 9. Findings

### Demonstrated defects

None. No statement violates a rule in Checks A, B or C on the evidence available.

### Advisories that a /prompt reviewer could score under Cross-Service Coherence

These do not fail Eval 0. Each is a reconcilable tension, not a proven incompatibility. All are repairable in one line.

**ADV-1. A prod backend update lands after "DEV stack only" and before the Oct 8 release.**
- Injected: L150, 09-30 15:51:06Z, "Server-side windows for Collect & Win are still on the DEV stack only, they reach prod with the next backend release."; L94, "The server windows that are still on the DEV stack go live with this release" (Oct 8).
- Base: Douglas DM, 09-30 18:16Z, "Ok, I updated the prod environment with the latest teams/social changes"; injected L250 makes this visible to Julia: "Checked on prod after Douglas's teams update".
- Repo: on `match3d-backend` `main`, the first Win and Collect commit `adb56ad` (09-01) precedes the teams commit `3345557` (09-12), and at `3345557` the prod block of `runtime.exs` already has `ZombiesGame.WinAndCollect, enabled: true`. No release or prod ref exists. A reader can argue the windows went live on Sep 30, which would move Collect & Win's first window from Fri Oct 10 to Mon Oct 6.
- Why not a defect: the DM is scoped to teams/social, Confluence says "not yet live", and nothing shows the windows shipped. What that deploy contained cannot be established.
- Minimum fix: add one Douglas comment on ZOM-563 at about 18:15Z, for example "Prod has the teams/social changes only. The live-ops server windows stay on dev until the Oct 8 release.", and move L250 to sequence 2.

**ADV-2. ZOM-344 closes on "reads well" while the quest chest timing complaint runs on.**
- Injected: L208, 09-16, "Quest box open and close animation reuses the endless chest curve and reads well on the quest screen. Art side is signed off on my end."; L209 sets Done.
- Base: Marcus, #zombie-bugs 08-11, "some chest quest animations show the reward before the chest open, and then plays the open animation of the chest. its wierd"; Marcus DM 09-23, "the rewards appears first and then the chest opens. it needs to open and then the rewards appear"; Marcus DM 09-30, "The chest opens before the rewards and I haven't done it like that. Sometimes it plays ok u know"; Vincent, Bug Checklist 09-30, "the timing is off. Especially in the quest chests." After the ticket opened on 07-03, the only Quests-screen prefab commits are unrelated (a chest tooltip on 07-13, `reward_Claimed` in September).
- Why not a defect: the sign-off is about the art curve, the complaints are about reward timing on claim, and "Sometimes it plays ok" allows both.
- Minimum fix: L208 ending "Art side is signed off on my end. The reward-before-open timing on claim is a separate integration issue."

**ADV-3. "Premium strip" has no trace in the client.**
- Injected: L160, "the Season Pass premium strip is still set to the October range. It needs the November range before that season opens, Oliver is taking the date change."
- Base: `git grep` finds no "strip", "october" or "november" in Season Pass scripts, Season Pass prefabs, `Assets/Data` or `Assets/Prefabs/UI` at HEAD. `SeasonPassResponse.cs` L8 takes `end_time` from the server.
- Why not a defect: a text search does not rule out art or server config, and sprites are LFS pointers here. The note stands on its own.
- Minimum fix: "the Season Pass premium strip art still shows the October season. It needs the November art before that season opens, Oliver is taking the change."

**ADV-4. Frederick's reply narrows the brief's naming rule but calls it unstated.**
- Injected: L105, "the English copy on that row names the game as Zombie Match 3D and events by their ZM3D names. Anything else is held"; L13, "Two things the brief does not spell out." and "Copy that does not name the game at all is fine to go out, the naming rule is only about wrong names."
- Why not a defect: same author, later date, so the reply governs. Both are rule sources, which is why /prompt may ask about it.
- Minimum fix: open L13 with "Two changes to the brief."

**ADV-5. The deck says both "scaled up week by week" and "hold the spend there".**
- Injected: L132, "Small scale at first, scaled up week by week if the cohorts hold."; L139, "we start buying users at small scale and hold the spend there until the pivot call."; L128, "Scaled beta-cohort buy".
- Why not a defect: the slides read in sequence if scaling follows the pivot call.
- Minimum fix: L132 "Small scale at first; after the pivot call, scaled up week by week if the cohorts hold."

**ADV-6. "Still only… with the bot" has no earlier record.**
- Injected: L217, "Still only shows up with the bot running; in manual play across a long endless session I could not get it."
- Base: ZOM-504 description, same author, "I couldn't notice anything particularly but it happens in every attempt." No base record mentions a bot for this bug.
- Why not a defect: a later retest may validly differ.
- Minimum fix: replace "Still only shows up" with "Re-tested: it only shows up".

### Cosmetic advisories

- **ADV-7.** `#468#ev_6` is `reviewed` but sorts after `ev_4` merged and `ev_5` closed, because `created_at` is NULL as in base. The review predates the merge.
- **ADV-8.** Base `revision_id` equals the first 10 hex of the file id; `4c1a7e9b02` and `a9d3f60c48` do not. Unlisted field, so not an ID finding.
- **ADV-9.** The #468 parent gains Arthur in Reviewers; base #472 was not updated that way. Both forms exist in base.
- **ADV-10.** Samuel's base list for Daily Gift says only "fixed font size" and "fixed alignment and position of elements", while L198 says the frame shipped in #471. The sprite did change (`41a0d814ed`), but it is an LFS pointer, so the frame was not confirmed by eye.
- **ADV-11.** L27 "rides the next build": dev builds #2027 and #1758 with that commit had already finished at 21:27Z, so it fits only the next store build. The commit subject does not mention lightSweep; the file list does.
- **ADV-12.** The brief's "unresolved change-request review blocker" clause has no qualifying record: base has none after `match3d#303` on 2025-07-16 and the SQL adds none. It simply never fires.
- **ADV-13.** 12 columns are NOT COVERED by the unverified snapshot (section 7). Advisory under Eval 0, but worth confirming against the live schema file before deploy.
- **ADV-14.** Julia is not in the listed members of public `#zombie-prs`. The GitHub comments are unscoped, so nothing depends on the mirrors.
- **ADV-15.** The injected sheet has NULL `content_path`, while all 356 base sheets have one. It is served through the Sheets rows and passes the lint rule; a raw Drive content read would find no bytes.
- **ADV-16.** Gmail bodies use LF where base mail uses CRLF, and headers are a short set. No effect on the checks.

## 10. Full operation ledger

Operation order as in the SQL. Paths are relative to each service's `Services_Data/<service>/` folder. Line = first line of the statement. Result covers Checks A, B and C for that record.

| # | Line | Table | Op | Record / target | Before → after or key values | Source / coverage | Result |
|---|---|---|---|---|---|---|---|
### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: Every scored fork is ruled out by a quoted rule or third-party record, and the moved date sits inside a stated boundary. The reward-table item is outside the scored comparison because its channel is not confirmed visible, and the only record on it says it is done.

Alternative selection: Every beat, push row, still-to-do candidate, write and destination was swept. D is the strongest remaining alternative because it changes a write.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | All three Collect &amp; Win items are flagged since the brief. The October season is clipped to the span. Brian is told in a reply, with a new time before the lock. | Plan seven beats on the calendar with Boss Arena, Zombie Lane, the rotating shop and the Halloween one-off off it; hold Weekly Leaderboard until its fix is confirmed on prod; Collect &amp; Win starts late; two pushes go, eight are held. | Fill the Calendar and Pushes tabs; comment on ZOM-429; link the sheet on ZOM-78; reply to Brian on the Sep 26 mail; send Frederick the recommendation in the DM. | Julia sheet ZM3D Beta Live-Ops Calendar; Linear ZOM-429 and ZOM-78; Gmail thread of the Sep 26 mail; Slack DM D05SD5QLG94. | Collect &amp; Win Still to do: prod deploy (Douglas), final vial models (Claire), event icon animation (Marcus). Season Pass First window Oct 6 00:00 UTC. Brian handoff moved to Thu Oct 30. | BR\_STILL (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql pointer docs\_documents f\_7c3e91a4d2b85f60e1a9c4): "anything flagged since this brief as still needed for it (prod deploy, config or player-facing art)"; BZ (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql pointer linear\_comments cmt\_zom465\_3): "the Collect &amp; Win icon does have to land before the event runs"; BR\_CLIP (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql): "Clip anything that starts before or runs past that to those two instants." |
| B | The icon animation is cosmetic polish, so it stays off the Collect &amp; Win row. | Plan seven beats on the calendar with Boss Arena, Zombie Lane, the rotating shop and the Halloween one-off off it; hold Weekly Leaderboard until its fix is confirmed on prod; Collect &amp; Win starts late; two pushes go, eight are held. | Fill the Calendar and Pushes tabs; comment on ZOM-429; link the sheet on ZOM-78; reply to Brian on the Sep 26 mail; send Frederick the recommendation in the DM. | Julia sheet ZM3D Beta Live-Ops Calendar; Linear ZOM-429 and ZOM-78; Gmail thread of the Sep 26 mail; Slack DM D05SD5QLG94. | Collect &amp; Win Still to do: prod deploy (Douglas), final vial models (Claire) only. Season Pass First window Oct 6 00:00 UTC. Brian handoff moved to Thu Oct 30. | BR\_STILL (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql pointer docs\_documents f\_7c3e91a4d2b85f60e1a9c4): "what still has to land before it runs for bought users"; Z565 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql pointer linear\_comments cmt\_zom565\_2): "so they can follow and do not have to land before the beta" |
| C | First window means the first one that opens inside the span, so Season Pass shows Nov 1 and the October season is only noted. | Plan seven beats on the calendar with Boss Arena, Zombie Lane, the rotating shop and the Halloween one-off off it; hold Weekly Leaderboard until its fix is confirmed on prod; Collect &amp; Win starts late; two pushes go, eight are held. | Fill the Calendar and Pushes tabs; comment on ZOM-429; link the sheet on ZOM-78; reply to Brian on the Sep 26 mail; send Frederick the recommendation in the DM. | Julia sheet ZM3D Beta Live-Ops Calendar; Linear ZOM-429 and ZOM-78; Gmail thread of the Sep 26 mail; Slack DM D05SD5QLG94. | Collect &amp; Win Still to do: prod deploy (Douglas), final vial models (Claire), event icon animation (Marcus). Season Pass First window Nov 1 00:00 UTC. Brian handoff moved to Thu Oct 30. | BR\_SPAN (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql): "The calendar covers Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC"; BF26 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql): "The November season still opens on Sat Nov 1." |
| D | The prompt lists four writes and the brief is rules for building the calendar, so mail to Brian stays with Julia and is only flagged to her. | Plan seven beats on the calendar with Boss Arena, Zombie Lane, the rotating shop and the Halloween one-off off it; hold Weekly Leaderboard until its fix is confirmed on prod; Collect &amp; Win starts late; two pushes go, eight are held. | Fill the Calendar and Pushes tabs; comment on ZOM-429; link the sheet on ZOM-78; send Frederick the recommendation in the DM. No mail to Brian. | Julia sheet ZM3D Beta Live-Ops Calendar; Linear ZOM-429 and ZOM-78; Slack DM D05SD5QLG94. | Collect &amp; Win Still to do: prod deploy (Douglas), final vial models (Claire), event icon animation (Marcus). Season Pass First window Oct 6 00:00 UTC. Brian handoff moved to Thu Oct 30. | P (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/04\_Prompt.txt): "Once the sheet's done, link it on the calendar ticket and send Frederick the recommendation he asked for." |
| E | The handoff moves back to the original Wed Oct 29. | Plan seven beats on the calendar with Boss Arena, Zombie Lane, the rotating shop and the Halloween one-off off it; hold Weekly Leaderboard until its fix is confirmed on prod; Collect &amp; Win starts late; two pushes go, eight are held. | Fill the Calendar and Pushes tabs; comment on ZOM-429; link the sheet on ZOM-78; reply to Brian on the Sep 26 mail; send Frederick the recommendation in the DM. | Julia sheet ZM3D Beta Live-Ops Calendar; Linear ZOM-429 and ZOM-78; Gmail thread of the Sep 26 mail; Slack DM D05SD5QLG94. | Collect &amp; Win Still to do: prod deploy (Douglas), final vial models (Claire), event icon animation (Marcus). Season Pass First window Oct 6 00:00 UTC. Brian handoff moved to Wed Oct 29. | BR\_LOCK (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql): "moves to any time before it" |

Explicit option inventory: The prompt has no candidate option list.
Inventory evidence: P (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/04\_Prompt.txt): "Can you take it on for me?"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: D
Resolution: EXCLUDED. The prompt delegates the whole job and points to the brief, and the brief states this write. Brian names the same place.
Resolution evidence: BR\_LOCK (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql): "A committed date that misses the lock moves to any time before it and its owner is told in a reply on the mail where they committed to it."; P (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/04\_Prompt.txt): "Can you take it on for me?"; BF26B (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql): "If the new date is a problem on your side, reply on this mail."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same. |
| writes | DIFFERENT | Reading D drops the reply. |
| destinations | DIFFERENT | Reading D drops the mail thread. |
| contents | SAME | Same cells. |

Authority chain: P → BR\_LOCK

Resolution relevance challenge: The rule is explicit that the owner is told in a reply. Take it on for me hands that to the Agent.
Delegation challenge: NOT_CLAIMED. No materially different call is delegated.
Challenge evidence: BR\_LOCK (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql): "A committed date that misses the lock moves to any time before it and its owner is told in a reply on the mail where they committed to it."

Compared alternative: B
Resolution: EXCLUDED. Brian, who is not the assignee, states on Sep 30 that the icon must land before the event runs. That closes the gap the owner note left.
Resolution evidence: BZ (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql pointer linear\_comments cmt\_zom465\_3): "the Collect &amp; Win icon does have to land before the event runs"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same. |
| writes | SAME | Same. |
| destinations | SAME | Same. |
| contents | DIFFERENT | One item and owner in one cell. |

Authority chain: P → BR\_STILL → BZ

Resolution relevance challenge: The quote answers the exact open question: must this item land before the event runs.
Delegation challenge: NOT_CLAIMED. No materially different call is delegated.
Challenge evidence: BZ (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql pointer linear\_comments cmt\_zom465\_3): "the Collect &amp; Win icon does have to land before the event runs"

Compared alternative: C
Resolution: EXCLUDED. The clip rule makes the running October season a window inside the span that starts Oct 6 00:00 UTC, so it is the first window. Oct 1 and Nov 1 both fall away.
Resolution evidence: BR\_CLIP (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql): "Clip anything that starts before or runs past that to those two instants."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same. |
| writes | SAME | Same. |
| destinations | SAME | Same. |
| contents | DIFFERENT | One date in one cell. |

Authority chain: P → BR\_CLIP

Resolution relevance challenge: The rule states what happens to anything that starts before the span.
Delegation challenge: NOT_CLAIMED. No materially different call is delegated.
Challenge evidence: BR\_CLIP (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql): "Clip anything that starts before or runs past that to those two instants."

Compared alternative: E
Resolution: AUTHORIZED_VARIATION. The brief accepts any time before the lock, so both dates are valid.
Resolution evidence: BR\_LOCK (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql): "moves to any time before it"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same. |
| writes | SAME | Same. |
| destinations | SAME | Same. |
| contents | DIFFERENT | The moved date differs inside the boundary. |

Authority chain: P → BR\_LOCK
Authority kind: OBJECTIVE_ACCEPTANCE_BOUNDARY
Acceptance boundary: Any instant before Oct 31 00:00 UTC, the lock 24h before the Nov 1 00:00 UTC open.
Acceptance for A: Thu Oct 30 is before the lock.
Acceptance for E: Wed Oct 29 is before the lock.

Resolution relevance challenge: The rule names the boundary itself.
Delegation challenge: EXPLICIT_AUTHORITY. The words any time before it authorize every date in the boundary.
Challenge evidence: BR\_LOCK (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql): "moves to any time before it"

Strongest-alternative challenge (D): D is not a strawman: the prompt lists its writes and does not mention Brian. It fails only because the prompt incorporates the brief and the brief states the write.
Challenge evidence: BR\_LOCK (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev13/inputs/01\_Universe\_Inject.sql): "A committed date that misses the lock moves to any time before it and its owner is told in a reply on the mail where they committed to it."

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

#### Decision sweep

Basis labels: RECORD, SCOPE_GAP, SILENCE. "Rule" means Frederick's message, reply or brief.

**Beats**

| Item | Outcome | Basis | Settled by |
|---|---|---|---|
| Collect & Win | In, late start, not held. First window Fri Oct 10 00:00 UTC. Windows: Oct 10-12, then each Mon-Tue, Wed-Thu, Fri-Sun, last Oct 31 00:00 to Nov 2 23:59 UTC. W1 (from Oct 10) to W4 | RECORD | Rule "starts late, it is not held"; rc_10 "still on the DEV stack only"; cmt_zom563_1 "wait for the Oct 8 release"; GCal 2025-10-08 15:00Z. Wed window opened 00:00 UTC, before the release |
| Plague Race | In, W1 to W4, no dates | RECORD | Rule; rc_10 "already running on prod" |
| Weekly Leaderboard (leagues) | Held until the fix is confirmed on prod. Keeps Mon 00:00 to Sun 23:59 UTC windows and W1 to W4, marked held | RECORD | Vincent Sep 30 meets the hold test and is newer than Douglas Sep 16; rule "keeps its usual windows and weeks"; CDK `LEAGUES_SCHEDULE` "0 0 * * 1" via `github_get_file_contents` |
| Endless Monster Mode | In, W1 to W4. Weekly Mon 00:00 to Sun 23:59 UTC with a daily 00:00 UTC reset | RECORD | Confluence "daily reset 00:00 UTC, weekly reset Monday 00:00 UTC". A row stating both satisfies either emphasis |
| Season Pass | In. First window Oct 6 00:00 UTC. Windows Oct 6 00:00 to Oct 31 23:59 UTC and Nov 1 00:00 to Nov 2 23:59 UTC | RECORD | Rule "Clip anything that starts before or runs past that to those two instants."; "closing 23:59 UTC on its last day"; rc_1 October range; Brian Nov 1 |
| Quest rollover | In, W1 to W4, no dates | RECORD | ZOM-534 Leonard (reporter) "it is good on prod now" |
| Daily gift | In, W1 to W4, no dates | RECORD | ZOM-556 Vincent "claiming works and nothing is lost"; rule "Wrong counters ... do not hold" |
| Boss Arena | Off | RECORD | Rule |
| Rotating shop | Off | RECORD | Rule "the rotating shop is not a beat" |
| Zombie Lane | Off | RECORD | Reply "keep Zombie Lane off the calendar" |
| Halloween one-off | Off | RECORD | Robert Sep 30 "pulling my ok. Take it off the beta calendar"; rule "his later word is the one that counts" |
| Desert and Port themes | Not beats | RECORD | Robert Sep 30 "nothing waits on new themes" |

**Push rows (PNs Beta, sheet row number)**

| Row | Item | Status / Live col | Outcome, what is missing | Basis | Settled by |
|---|---|---|---|---|---|
| 2 | Quests | Not Ready / LIVE | Hold: Ready | RECORD | Rule |
| 3 | Hourly Coins | Not Ready / LIVE | Left off | RECORD | Reply |
| 4 | Lives recharged | Ready / LIVE | Send, no game name | RECORD | Reply "fine to go out" |
| 5 | 1 day lapsed | Ready / LIVE | Hold: game name (copy says Puzzles vs Zombies) | RECORD | Rule; spec rename 24 July 2025 |
| 6 | 7 days lapsed | Ready / LIVE | Send | RECORD | Reply |
| 7 | FTUE | Ready / LIVE | Hold: game name (Puzzles vs Zombies) | RECORD | Rule |
| 8 | Win & Collect | Not Ready / WIP | Hold: Ready, LIVE, event name | RECORD | Rule; Confluence "under a different name" |
| 9 | Nathan's Treasure Hunt | Not Ready / WIP | Left off | RECORD | Reply |
| 10 | Plague Race | Ready / WIP | Hold: LIVE | RECORD | Rule |
| 11 | Streak Fever | Not Ready / WIP | Left off | RECORD | Reply |
| 12 | Axe Arena | Not Ready / WIP | Left off | RECORD | Reply |
| 13 | Login Calendar | Not Ready / WIP | Hold: Ready, LIVE | RECORD | Rule "(Login Calendar and Weekly Rankings are fine)" |
| 14 | Season Pass | Not Ready / WIP | Hold: Ready, LIVE | RECORD | Rule |
| 15 | Weekly Leaderboard | Ready / WIP | Hold: LIVE | RECORD | Rule |

**Still-to-do candidates flagged since the brief (created Sep 24 17:15 UTC)**

| Item | Outcome | Basis | Settled by |
|---|---|---|---|
| Collect & Win prod deploy | In, Douglas | RECORD | rc_10; GCal organizer douglas@; cmt_zom563_1 |
| Final vial models | In, Claire | RECORD | Arthur rc_38 "still need their final models before the event runs" |
| Collect & Win event icon animation | In, Marcus | RECORD | Brian cmt_zom465_3 "does have to land before the event runs". Brian is not the assignee |
| Collect & Win reward tables | Out | SCOPE_GAP, no cell | Douglas, the person asked: "Both tables are updated." Only his word, so not RECORD under the owner-claim rule. A careful reader has no ground to put it in a cell: the only record says it is done, and request and answer sit in the same thread, so either both are visible or neither is |
| Weekly Leaderboard fix | In, Douglas | RECORD | Rule "its fix if it is held"; ZOM-429 assignee |
| November config | In, Brian, moved to any time before Oct 31 00:00 UTC | RECORD | Spec "locked 24h before each season opens"; Oct 31 10:00 Istanbul is 07:00 UTC, a miss; rule "any time before it" |
| Premium strip art | In, Oliver | RECORD | Arthur rc_1 |
| Daily gift frame ZOM-432 | Out, shipped | RECORD | Samuel; #471 commit "Fixing UI Elements on Daily Gift"; builds #50 and #135 in #builds Sep 30 |
| Quests more content, Trello #61 | Out | SCOPE_GAP, no cell | Leonard, named owner: "The weekly rollover does not wait on them". The only flag says it is not needed |
| lightSweep box | Out | RECORD | Vincent (reporter) "nothing has to land for the beta" |
| Airstrike freeze | Out, unverified | RECORD | Leonard (reporter) "Could not get it to freeze" |
| ZOM-526 token travel | Out | RECORD | Brian; #472 merged; rest waits on Axe Arena |
| ZOM-565 Endless VFX | Out | RECORD | Brian "do not have to land before the beta" |
| ZOM-566 and PR #477 | Out | RECORD | Rule "not analytics"; Brian on the header and info text |
| ZOM-552, 442, 549, 548 | Out | RECORD | Rule "not analytics" |
| ZOM-543 queue manager | Out | RECORD | Not deploy, config or art; #472 merged |
| ZOM-521, 528, 541 card VFX | Out | RECORD | Card pack is not a beat |
| Collect & Win Bug_Checklist canvas (8 open items) | Out | RECORD | Vincent "none of them blockers and doesn't affect the submission" |
| Marcus particles note Sep 24 16:58 UTC | Out | RECORD | Predates the brief's created time |
| Store approval of Sep 30 builds | Out | RECORD | Deck dated Sep 23, not flagged since the brief |

Julia's mail: 287 threads scanned by subject for Aug and Sep 2025; only Brian's two mails carry a config commitment.

**Open PRs:** #477 analytics, out. #476 vision bot, not a beat. match3d-backend#34 draft, no review. auth-game-backend#2 and game-of-dominoes-backend#79, not ZM3D beats. **Change-request rule:** all 74 CHANGES_REQUESTED reviews checked; latest are match3d-backend#4 (June) and match3d#303 (July), none on or after Aug 1, so no beat holds under it. The undefined "Aug-Sep live-ops cohort" changes nothing.

**Writes and destinations**

| Item | Outcome | Basis | Settled by |
|---|---|---|---|
| Sheet | ZM3D Beta Live-Ops Calendar, tabs Calendar and Pushes | RECORD | DM "the calendar sheet in your ZM Live Ops folder" |
| Calendar ticket | ZOM-78, not ENG-2240 | RECORD | cmt_zom78_1 |
| Held-beat note | ZOM-429 only. A held push is not a held beat | RECORD | Rule "Hold a beat only when players provably cannot enter, score or claim" |
| Recommendation | DM D05SD5QLG94 | RECORD | DM "back here" |
| Brian reply | Sep 26 mail, in scope | RECORD | Rule; prompt "Can you take it on for me?"; Brian "reply on this mail" |
| New date | Any instant before Oct 31 00:00 UTC | RECORD, objective boundary | Rule "any time before it". Later rubric must not lock one date |

**Earlier forks**
- F1: closed. Settled by Brian, cmt_zom465_3: "the Collect & Win icon does have to land before the event runs".
- F2: closed as a fork. Douglas: "Both tables are updated." Label stays SCOPE_GAP, see the sweep row.
- F3: closed. No longer a both-fair figure. Settled by "Clip anything that starts before or runs past that to those two instants."

Forks open: none on this draft. P1 has not reported.

---

**Feasibility:** PASS (5). Every write has a cataloged operation; all facts exist. No per-X breakdown. Numeric asks are dates only; catalog has no return schemas, so rendering is an evidence limit, not a defect.

**Persona ACL Reachability:** PASS (5). Lens 1: DM, Robert DM, #zombie-match3d, #zombie-bugs, #zombie-art by membership; brief and deck by reader share; `Push Notifications Zombie Match` by share; Julia's sheet by ownership; mail by her mailbox copies; release event on her calendar. GitHub, Linear, Trello, Confluence unscoped. #zombie-prs and #zm-collect-win need no read. Lens 2: no ask directs an out-of-view read. No required record is hidden.

**Truthfulness:** PASS (5).

| Claim | Found | Evidence |
|---|---|---|
| Frederick messaged yesterday | Yes | ts 2025-09-30T20:20:17Z, 13:20 PT |
| Live-ops and push calendar for the ZM3D beta | Yes | "I need the live-ops and push calendar for the beta buy" |
| Four buy weeks, Monday the 6th | Yes | Deck W1 to W4; Oct 6 2025 is a Monday |
| Brief shared with Julia | Yes | reader share, Sep 24 |
| My live-ops calendar sheet | Yes | owner Julia, folder ZM Live Ops |
| Calendar ticket | Yes | ZOM-78 |
| Recommendation he asked for | Yes | "send me your recommendation back here" |

Departed people: none. Nothing after the clock is treated as done.

**Tool Use & Cross-service:** PASS (5). Graded fact per service: GitHub (which windows are on prod, vial and strip items), GCal (release instant, so Oct 10), Gmail (Oct 31 commitment), Confluence (24h lock, Endless resets), GSheets (push rows), Slack (Leaderboard hold, Halloween pull), Linear (owners, icon item, ZOM-78). Dropping any changes an answer.

**Investigation + Action:** PASS (5). Writes depend on findings.

**Clarity:** PASS (5). Intent is clear, no "I'll" statement exists, and the write-action test gives one set once the brief is applied. Reading D (no reply to Brian) is the closest split, and the incorporated rule states the write.

**Contrived:** PASS (5). All Eval 2.7 indicators No. The destination and recipient are named; a single "If" is not an if-chain; "If a beat ends up held" does not point at which beat.

**Alignment with Today's Date:** PASS (5). All relative words resolve; future dates are treated as future.

**Originality:** N/A, no samples supplied.

---

### Phase 3: Universe Feasibility

**Data Existence:** PASS (5). 7 of 7 premises plus all sweep records. All retrievable via cataloged tools. Linear comments exist only through the SQL (base `comments` is empty); `linear_list_comments` is cataloged.

**Cross-Service Coherence:** PASS (5) with base issues unscored as directed; see the note below.

| # | Status on 1f2175a2 | Evidence | Scored? |
|---|---|---|---|
| C1 | Present, unchanged | SQL Trello action `"name":"BETA: Sep 30"` against list record `BETA: Oct 10`. SC-13. The action agrees with 67 base actions; the odd one out is the base list record. The answer reads the comment text, never the list name | No: base issue, no task value |
| C2 | Present, unchanged | Confluence "re-imported from Google Sheets hourly in production" against CDK `IMPORT_REWARDS_SCHEDULE ... "*/5 * * * *"`. SC-62. With F2 closed, no graded fact touches it | No: base issue, no task value |
| C3 | Fixed | Slide 2 "any scale-up comes after the pivot call" now agrees with slide 3 "hold the spend there until the pivot call"; slide 1 no longer says "Scaled" | Closed |

**Note on the rule used.** The direction to leave unscored a base issue that changes no task value was applied as given. I did not find that sentence in Eval 1. The closest text is STEP 0.5 and deep_recheck step 2, which apply the "changes a value, set, order, recipient or destination" test to Eval 0 findings. §3.2 itself says the dimension fails on presence "whether or not the contributor introduced it". Read alone, §3.2 scores C1 and C2, and two low-impact items fail. That reading gives Coherence 2 and an overall FAIL.

Changed records checked for new inconsistencies, none found:
- Douglas reply: author in channel, parent id, `thread_ts_legacy`, reply_count 2 to 3, reply_users 1 to 2, ts matches created_at. SC-57 touched, no posting graded.
- cmt_zom465_3: sequence 3, follows 18:05:02, `updated_at` raised to match, and "the master VFX list was ticked" agrees with the ZOM-521 `[X]` icon line.
- cmt_zom563_1 and _2: sequence, 18:17:05 follows `started_at` 18:14 and the base DM at 18:16; closing comment matches `completed_at`.
- ZOM-542 Todo fits its comment. rc_38 and rc_1 match their Slack mirrors. Brief `style_runs` land on all nine headings.

Other known cards touched, no task value changed: SC-15 and SC-16 (repaired by the SQL, not graded), SC-18 (#477 is out as analytics), SC-38 (lock only is read from the spec).

Noted, not scored: `PNs Beta` Status and Live columns disagree on sight (Not Ready / LIVE), but the brief treats them as two axes, so this is designed friction. #468 timeline ev_6 sits after `closed` with a null date; this one is SQL-made, changes no value, and stays with Eval 0.
- Injection SQL considered: Yes. Static integrity: direct task-relevant checks; Eval 0 pending. Sources, access and configuration: supported.

| Prompt ask / source | Static evidence | Discovery/access | Task coherence |
|---|---|---|---|
| Calendar and pushes | NEW | Supported | PASS |
| Ticket note, link | NEW | Supported | PASS |
| Recommendation, Brian reply | NEW | Supported | PASS |

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 5 | Every fork settled by a quoted rule or third-party record |
| Prompt | Feasibility | 5 | All asks doable |
| Prompt | Persona ACL Reachability | 5 | All required reads visible |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | One write set |
| Prompt | Contrived / Unnatural | 5 | Natural request |
| Prompt | Alignment with Today's Date | 5 | Resolves |
| Prompt | Originality / Sample Similarity | N/A | No samples |
| Prompt | Truthfulness | 5 | 7 of 7 premises hold |
| Prompt | Tool Use & Cross-service | 5 | Each service changes a graded fact |
| Prompt | Investigation + Action | 5 | Writes follow findings |
| Prompt | Coherence (Bolt-on) | 5 | One workflow |
| Prompt | Persona | 5 | Fits Julia |
| Prompt | Business Function | 5 | Product |
| Prompt | Assigned Competency | 5 | Marketing and GTM |
| Prompt | Assigned Task Skill | 5 | Planning and decision support |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three load-bearing |
| Universe | Data Exists | 5 | All retrievable |
| Universe | Cross-Service Coherence | 5 (2 if §3.2 is read alone) | C1 and C2 unscored as directed |

Draft status: no demonstrated failure; NON-FAIL / PARTIAL with no numeric score until Eval 0 and P1 to P4 are in. Final verdict block comes after the Deep Recheck.

---

### Issues Found

| # | Issue | Severity | Dimension |
|---|---|---|---|
| 1 | C1 and C2 present, unscored as directed; the rule is not in Eval 1's text | Decides the verdict if the Portal reads §3.2 alone | Cross-Service Coherence |

### Recommended Improvements

1. C1 can be removed outright: move Leonard's rollover note off Trello card #61 to a surface with no list-name field. C2 is base data and stays.
2. For later stages: accept any handoff time before Oct 31 00:00 UTC. Season Pass First window is Oct 6 00:00 UTC, no longer either-or.

### Evidence limits
Eval 0 report on this hash pending. P1 to P4 pending. Evals/Docs PDFs and the Example Task not read (no extractor); scoring.json and Eval 1 overrides were used. Runtime visibility of non-member public Slack channels unverified; no required record depends on it. `review_context_sha256` null and full `validate_record` not run, since `start` is out of bounds; the UGT object passed `hg_prompt_ugt.validate_review` read-only with a local context.

---

### Appendix: every open ZOM ticket (post-SQL)

Default row: not flagged since the brief, so out under the rule "Nothing else goes in". Basis RECORD.

| Ticket | State | Owner | Title | Outcome |
|---|---|---|---|---|
| ZOM-16 | Backlog | marcus.bennett | Liquid Impact | Out (default) |
| ZOM-48 | Backlog | Robert | Reward Animations | Out (default) |
| ZOM-56 | Backlog | marcus.bennett | Glued VFX | Out (default) |
| ZOM-62 | Todo | vincent.parker | Zombie Ops #3 Spec (Dead Eye) | Out (default) |
| ZOM-64 | Backlog | marcus.bennett | Experiment with VFX when matching boss busters off t | Out (default) |
| ZOM-65 | Backlog | none | Profile page endpoints | Out (default) |
| ZOM-66 | Backlog | none | Stats endpoints | Out (default) |
| ZOM-69 | Backlog | none | Bot system | Out (default) |
| ZOM-70 | Backlog | none | Rewards system | Out (default) |
| ZOM-73 | Backlog | arthur.blake | A/B Test Item Sizes | Out (default) |
| ZOM-76 | Backlog | EMPLOYEE_0032_NAME | [PERSON_NAME_0120] to implement this VFX | Out (default) |
| ZOM-78 | Backlog | douglas | Event Calendar For Zombie Match 3D | Calendar ticket, gets the link |
| ZOM-97 | Todo | Robert | REVISION FOR ITEMS | Out (default) |
| ZOM-104 | Backlog | claire.morgan | Gas Can improvement | Out (default) |
| ZOM-118 | Todo | marcus.bennett | Shop Animations Master Ticket | Out (default) |
| ZOM-119 | Backlog | marcus.bennett | Shine for gold and gem piles. | Out (default) |
| ZOM-121 | Backlog | marcus.bennett | Card pack animation in the shop | Out (default) |
| ZOM-122 | Backlog | marcus.bennett | Simple animations for offers bands and labels. | Out (default) |
| ZOM-130 | Todo | leonard.hayes | Create an out of moves screen flow with offers | Out (default) |
| ZOM-137 | Backlog | claire.morgan | FOOD ITEMS | Out (default) |
| ZOM-147 | Backlog | claire.morgan | Peach | Out (default) |
| ZOM-148 | Backlog | claire.morgan | Plum | Out (default) |
| ZOM-150 | Backlog | claire.morgan | Cherries | Out (default) |
| ZOM-151 | Backlog | claire.morgan | Cucumbers | Out (default) |
| ZOM-155 | Backlog | claire.morgan | Squash | Out (default) |
| ZOM-168 | Backlog | EMPLOYEE_0032_NAME | 5th In-game Boost Double Damage | Out (default) |
| ZOM-171 | Todo | martin.walsh | Icon for double damage in-game boost | Out (default) |
| ZOM-181 | Todo | claire.morgan | 8. Vaious Solid color Plates/cups/mugs/egg on plates | Out (default) |
| ZOM-182 | Todo | claire.morgan | 9. Bagel | Out (default) |
| ZOM-184 | Todo | claire.morgan | 11.Curling Iron (Maybe Drop the item) | Out (default) |
| ZOM-202 | In Progress | arthur.blake | Minimize or migrate selection panel for easier diffi | Out (default) |
| ZOM-236 | Backlog | EMPLOYEE_0032_NAME | Shop Pack Idle animation | Out (default) |
| ZOM-237 | Backlog | none | packs animations bugs | Out (default) |
| ZOM-243 | Backlog | marcus.bennett | Poison/Fire/Shock Death Vfx Animations | Out (default) |
| ZOM-255 | Backlog | owen.baker | Tap to skip kill cam + Dimming the board area and on | Out (default) |
| ZOM-292 | Todo | arthur.blake | Level Editor Improvements 2.0 | Out (default) |
| ZOM-293 | Todo | Robert | Dynamic Difficulty Tiering Down Issue | Out (default) |
| ZOM-311 | In Progress | arthur.blake | Consider migrating the list of items and list of mon | Out (default) |
| ZOM-317 | Backlog | martin.walsh | Martin to polish UI assets in FIGMA | Out (default) |
| ZOM-342 | Todo | claire.morgan | Indoor Plant | Out (default) |
| ZOM-348 | Todo | none | Rotating Shop Discount Issues | Rotating shop, not a beat |
| ZOM-359 | Regression | arthur.blake | Phone heating up too much after playing 15 to 20 lev | Out (default) |
| ZOM-386 | Todo | douglas | Track Player Card Inventory and Sync to BigQuery | Out (default) |
| ZOM-387 | Todo | arthur.blake | Giant Analytics Ticket | Out, analytics |
| ZOM-390 | Backlog | julia.lawson | Icon and Event Visual for Win Streak Event (axe aren | Axe Arena not in beta |
| ZOM-400 | Todo | arthur.blake | We want to add a new field to left_level event to tr | Out (default) |
| ZOM-427 | Todo | arthur.blake | App icon is too zoomed in for android | Out (default) |
| ZOM-429 | Backlog | douglas | Leaderboard next session doesn't start without killi | Held beat ticket, gets the note |
| ZOM-438 | Todo | arthur.blake | Investigate why some zombie tracks do not spawn | Out (default) |
| ZOM-439 | Todo | arthur.blake | Investigate card_upgrade event not recording correct | Out (default) |
| ZOM-441 | Todo | arthur.blake | Fix reward_str and chest_content_str sending issue | Out (default) |
| ZOM-442 | In Validation | oliver.brooks | Analytics Instrumentation for Tropy Reward Redeem | Out, analytics |
| ZOM-443 | Todo | arthur.blake | Investigate non-random item removal from board due t | Out (default) |
| ZOM-449 | Backlog | arthur.blake | Some items are acting weird in low-end android devic | Out (default) |
| ZOM-453 | Todo | samuel.turner | Fix text inconsistency | Out (default) |
| ZOM-458 | Todo | arthur.blake | Quitting algo levels still makes the level change an | Out (default) |
| ZOM-465 | In Progress | marcus.bennett | Endless Mode Master VFX Ticket | Icon animation in, Marcus (RECORD, Brian) |
| ZOM-467 | In Progress | marcus.bennett | Zombie Match 3d - Marketing Videos | Out (default) |
| ZOM-468 | Todo | arthur.blake | Low-end devices rendering issues | Out (default) |
| ZOM-471 | Todo | samuel.turner | Add red dot icon for players not in Plague Race | Out, Leonard "we don’t need it!" Aug 13 |
| ZOM-475 | Todo | oliver.brooks | Consecutive glass impact sfx/vfx causes crash on and | Not a beat (SC-8, do not grade) |
| ZOM-477 | Todo | EMPLOYEE_0032_NAME | DOT kills can take too long and cause perceived unre | Out (default) |
| ZOM-481 | Todo | owen.baker | Zombie Health bar persists too long after death. | Out (default) |
| ZOM-482 | Backlog | EMPLOYEE_0032_NAME | Make "Fast-forwarding" another boolean properties in | Out (default) |
| ZOM-483 | Todo | calvin.price | Infinite lives from new-install are not granted, rew | Out (default) |
| ZOM-484 | Todo | marcus.bennett | Info Screen Animations | Out (default) |
| ZOM-504 | Backlog | EMPLOYEE_0032_NAME | In endless mode, objects might stay persistent in th | Out, visual, bot only |
| ZOM-505 | Backlog | vincent.parker | Tutorial repeats at level 19 in V 1736 Android versi | Out (default) |
| ZOM-508 | Todo | oliver.brooks | Assisted Start | Out (default) |
| ZOM-513 | In Progress | claire.morgan | Convert Maracas into multi-color variant-enabled | Out (default) |
| ZOM-514 | In Progress | claire.morgan | Request to add motorcycle helmet as a survival item | Out (default) |
| ZOM-517 | Backlog | EMPLOYEE_0032_NAME | Monster loses enrage during item refill in endless m | Out, retest clean |
| ZOM-520 | Todo | oliver.brooks | First loss as level doesn't reset win streak | Out (default) |
| ZOM-521 | In Progress | calvin.price | Master Ticket - VFX implementation | Out, see sweep |
| ZOM-526 | In Progress | none | Tokens traveling to live-ops | Out, see sweep |
| ZOM-528 | In Progress | calvin.price | Claimed Cards traveling to inventory section | Out, see sweep |
| ZOM-534 | In Progress | douglas | Quest points not resetting until app restart in prod | Quests not held, good on prod |
| ZOM-535 | Todo | EMPLOYEE_0032_NAME | Fast matching might target an already-dead zombie | Out (default) |
| ZOM-539 | Todo | samuel.turner | Implement Red Dot for Cards and Shop | Out (default) |
| ZOM-541 | In Progress | calvin.price | Cards Collect Vfx animation | Out, see sweep |
| ZOM-542 | Todo | samuel.turner | Update home screen and victory score screen for game | Out, not flagged since brief |
| ZOM-543 | In Progress | calvin.price | Queue Manager | Out, see sweep |
| ZOM-544 | In Progress | EMPLOYEE_0032_NAME | Implement Google Apple Login | Not a beat |
| ZOM-545 | Todo | douglas | Ingest bot params from a spreadsheet | Out (default) |
| ZOM-546 | Todo | owen.baker | Bug: refill algorithm spawns fewer items over time | Out, retest clean |
| ZOM-548 | In Validation | EMPLOYEE_0032_NAME | Track events for boss arena as listed in the spreads | Out, analytics, Boss Arena off |
| ZOM-549 | In Validation | EMPLOYEE_0032_NAME | Add new fields to left_level and endless_left analyt | Out, analytics |
| ZOM-552 | In Progress | oliver.brooks | Season Pass Analytics | Out, analytics |
| ZOM-554 | Todo | owen.baker | Quiting level mid tornado boost breaks the object ph | Out (default) |
| ZOM-556 | Todo | calvin.price | When the daily gift is skipped, it doesn't reset to  | Daily gift not held, wrong counter |
| ZOM-559 | Todo | oliver.brooks | Homing out on android(samsung), sound disappears. | Out (default) |
| ZOM-560 | Todo | samuel.turner | The abandoned pack win streak freezer reward is not  | Out (default) |
| ZOM-562 | Todo | owen.baker | Orphan items in boss arena | Boss Arena off |
| ZOM-564 | Todo | oliver.brooks | "Free" label stays on boosters after Tutorial | Out (default) |
| ZOM-565 | Todo | calvin.price | Endless Horde Start Screen Vfx | Out, see sweep |
| ZOM-566 | In Progress | owen.baker | Collect&Win Analytics | Out, analytics |

ENG-2240 Web interface for the liveops calendar (Todo): decoy for the calendar ticket, out. No non-ZOM open ticket since June matches a live-ops beat.
