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
| Injection SQL | `R/inputs/01_Universe_Inject.sql`, sha256 `ffbac4586fb91842ca16263c2b76987c26623c7ed689e00d33886c63f9331bdc`, 259 lines |
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

**Channels and threads.** Each author is in the channel's member list: `D05SD5QLG94` (Julia, Frederick), `D05GU6L0XFH` (Julia, Robert), `C08R8CHB0QL` zombie-art, `C0880U9751A` zombie-match3d, `C08R27X0EAH` zombie-bugs, `C093LEZGF6J` zombie-prs (bot). All eight reply parents (seven base, one from L11) exist in the same channel, and each reply's `thread_ts_legacy` equals its parent's ts.

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
- Base: Marcus, #zombie-bugs 08-11, "some chest quest animations show the reward before the chest open, and then plays the open animation of the chest. its wierd"; Marcus DM 09-23, "the rewards appears first and then the chest opens. it needs to open and then the rewards appear"; Marcus DM 09-30, "The chest opens before the rewards and I haven't done it like that. Sometimes it plays ok u know"; Vincent, Bug Checklist 09-30, "the timing is off. Especially in the quest chests." No commit after the ticket opened on 07-03 names a quest box animation; the Quests prefab commits since then are a cell change on 07-09, a chest tooltip on 07-13 and `reward_Claimed` in September.
- Why not a defect: the sign-off is about the art curve, the complaints are about reward timing on claim, and "Sometimes it plays ok" allows both.
- Minimum fix: L208 ending "Art side is signed off on my end. The reward-before-open timing on claim is a separate integration issue."

**ADV-3. "Premium strip" has no trace in the client.**
- Injected: L160, "the Season Pass premium strip is still set to the October range. It needs the November range before that season opens, Oliver is taking the date change."
- Base: at HEAD, `git grep` finds no "october" or "november" in `Assets/Scripts`, `Assets/Resources`, `Assets/Data`, `Assets/Prefabs/UI` or the Season Pass prefabs, no "strip" in Season Pass scripts or prefabs, and no "premium strip" anywhere in `Assets`. `SeasonPassResponse.cs` L8 takes `end_time` from the server.
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
| 1 | 11 | slack.slack_messages | INSERT | `bca784379e7dbca9e64e79a64dfefbba` D05SD5QLG94 ts 1759263617.418209 | user EMPLOYEE_0008; parent none; rc 1/1 | new; id = sha256(channel\|ts)[:32]; free in 610,468 msgs / 4,840 files | OK. Root ask. Author in DM members; ts/created_at equal; reply_count 1/1 and latest_reply = stmt L13 ts; Mon Oct 6 and Sun Nov 2 weekdays correct |
| 2 | 13 | slack.slack_messages | INSERT | `890dc27f56e8501bd7590ffdfc231057` D05SD5QLG94 ts 1759263878.305129 | user EMPLOYEE_0008; parent bca78437; rc 0/0 | new; id = sha256(channel\|ts)[:32]; free in 610,468 msgs / 4,840 files | OK. Reply to L11. The four rows, Login Calendar row and old Domino translated tab verified in `f_a325dd4af80afc5994d5dc` PNs Beta. Zombie Lane permanent matches Confluence `page_liveops_calendar`. ADV-4 |
| 3 | 15 | slack.slack_messages | INSERT | `933cee9f6464a80e4b1f05259b595b20` C08R8CHB0QL ts 1758213623.552919 | user EMPLOYEE_0016; parent 9025d428; rc 0/0 | new; id = sha256(channel\|ts)[:32]; free in 610,468 msgs / 4,840 files | OK. Reply in Martin's Sep 17 Halloween thread, after root; author is a channel member |
| 4 | 17 | slack.slack_messages | INSERT | `669d15f685f158633e56302160957f1e` D05GU6L0XFH ts 1759270241.638119 | user EMPLOYEE_0016; parent none; rc 0/0 | new; id = sha256(channel\|ts)[:32]; free in 610,468 msgs / 4,840 files | OK. Top-level DM, after base 20:46:05Z; refers to L15 thread; later word supersedes L15 by date |
| 5 | 19 | slack.slack_messages | INSERT | `b5f2955c2e154efc6835946ecfe1758e` C0880U9751A ts 1759265412.481909 | user EMPLOYEE_0012; parent none; rc 0/0 | new; id = sha256(channel\|ts)[:32]; free in 610,468 msgs / 4,840 files | OK. Top-level; author is a member; later than L173 and supersedes it by date; ZOM-429 subject matches |
| 6 | 21 | slack.slack_messages | UPDATE | `9025d428af1f551a20e303c3acbc545b` | reply_count 0→1; users 0→1; latest None→1758213623.552919; thread_ts_legacy set | slack/messages/C08R8CHB0QL/2025-09.json#/121 | OK. Base 0/0/null, no replies; +1 reply L15 (Robert) gives 1/1, latest = L15 ts |
| 7 | 23 | slack.slack_messages | INSERT | `e343557b2e94a1701251ebd079e6f0ce` C08R27X0EAH ts 1759187861.318279 | user EMPLOYEE_0038; parent ede90bc6; rc 0/0 | new; id = sha256(channel\|ts)[:32]; free in 610,468 msgs / 4,840 files | OK. Reply to Leonard's Sep 21 root; base names the airstrike freeze (Vincent, #zombie-design 09-22 18:00) |
| 8 | 25 | slack.slack_messages | UPDATE | `ede90bc6ec6cb16fd97663f2888f39a2` | reply_count 0→1; users 0→1; latest None→1759187861.318279; thread_ts_legacy set | slack/messages/C08R27X0EAH/2025-09.json#/879 | OK. Base 0/0/null; +1 reply L23 gives 1/1, latest = L23 ts |
| 9 | 27 | slack.slack_messages | INSERT | `a08ff7cbfc52008d7dee8457e9385a3c` C08R27X0EAH ts 1759268775.482369 | user EMPLOYEE_0012; parent d0dd5d3a; rc 0/0 | new; id = sha256(channel\|ts)[:32]; free in 610,468 msgs / 4,840 files | OK. Commit `25c6c66b6b` (21:20:26Z, Oliver) changes `lightSweep Box Variant.mat`; reply is later, 21:46:15Z. ADV-11 |
| 10 | 29 | slack.slack_messages | UPDATE | `d0dd5d3ad4658add1f79802e2aa60e48` | reply_count 4→5; users 3→3; latest 1759254162.721499→1759268775.482369 | slack/messages/C08R27X0EAH/2025-09.json#/1091 | OK. Base 4 replies, repliers Marcus/Oliver/Vincent; Vincent already counted so users stay 3; 4 to 5; latest = L27 ts |
| 11 | 31 | slack.slack_messages | INSERT | `532747cb5d123a95d13204e57b5a7a38` C08R8CHB0QL ts 1759250468.275139 | user EMPLOYEE_0016; parent a3e78e82; rc 0/0 | new; id = sha256(channel\|ts)[:32]; free in 610,468 msgs / 4,840 files | OK. Port theme attested (Martin, top-level 09-30 16:27Z, before this reply); desert root is this thread |
| 12 | 33 | slack.slack_messages | UPDATE | `a3e78e820b9f880ef4e3d941562110df` | reply_count 3→4; users 3→4; latest 1759161266.305589→1759250468.275139 | slack/messages/C08R8CHB0QL/2025-09.json#/255 | OK. Base 3/3 (Julia, Claire, Martin); Robert is a new replier, so 4/4; latest = L31 ts |
| 13 | 35 | gmail.gmail_threads | INSERT | `brian.foster@harmonygames.co/1843954828968110017` | user brian.foster | new; free in 81,404 threads | OK. Brian mailbox exists; id free; history_id NULL; snippet equals its message row |
| 14 | 36 | gmail.gmail_messages | INSERT | `brian.foster/<CAPT--p4sBC8XnaA7qBDM…` | 2025-09-22T09:12:41+00:00; labels ["ARCHIVED","SENT","Label_b19fb8d1b3"] | new; free in 95,164 msgs | OK. Thread and Message-ID match headers; internal_date = header date; thread id >>20 = internal_date; label ids match X-Gmail-Labels; snippet is a prefix of the flattened body; weekdays correct |
| 15 | 46 | gmail.gmail_threads | INSERT | `julia.lawson@harmonygames.co/1843954828968533812` | user julia.lawson | new; free in 81,404 threads | OK. Julia mailbox exists; id free; history_id NULL; snippet equals its message row |
| 16 | 47 | gmail.gmail_messages | INSERT | `julia.lawson/<CAPT--p4sBC8XnaA7qBDM…` | 2025-09-22T09:12:41+00:00; labels ["INBOX","Label_b19fb8d1b3","CATEGORY_PERSONAL"] | new; free in 95,164 msgs | OK. Thread and Message-ID match headers; internal_date = header date; thread id >>20 = internal_date; label ids match X-Gmail-Labels; snippet is a prefix of the flattened body; weekdays correct |
| 17 | 57 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843954828968789474` | user frederick.stone | new; free in 81,404 threads | OK. Frederick mailbox exists; id free; history_id NULL; snippet equals its message row |
| 18 | 58 | gmail.gmail_messages | INSERT | `frederick.stone/<CAPT--p4sBC8XnaA7qBDM…` | 2025-09-22T09:12:41+00:00; labels ["INBOX","CATEGORY_PERSONAL"] | new; free in 95,164 msgs | OK. Thread and Message-ID match headers; internal_date = header date; thread id >>20 = internal_date; label ids match X-Gmail-Labels; snippet is a prefix of the flattened body; weekdays correct |
| 19 | 68 | gmail.gmail_threads | INSERT | `brian.foster@harmonygames.co/1844311412965607905` | user brian.foster | new; free in 81,404 threads | OK. Brian mailbox exists; id free; history_id NULL; snippet equals its message row |
| 20 | 69 | gmail.gmail_messages | INSERT | `brian.foster/<CAPT--p4a5fY9wd6vr+8J…` | 2025-09-26T07:40:26+00:00; labels ["ARCHIVED","SENT","Label_b19fb8d1b3"] | new; free in 95,164 msgs | OK. Thread and Message-ID match headers; internal_date = header date; thread id >>20 = internal_date; label ids match X-Gmail-Labels; snippet is a prefix of the flattened body; weekdays correct |
| 21 | 77 | gmail.gmail_threads | INSERT | `julia.lawson@harmonygames.co/1844311412966040123` | user julia.lawson | new; free in 81,404 threads | OK. Julia mailbox exists; id free; history_id NULL; snippet equals its message row |
| 22 | 78 | gmail.gmail_messages | INSERT | `julia.lawson/<CAPT--p4a5fY9wd6vr+8J…` | 2025-09-26T07:40:26+00:00; labels ["INBOX","CATEGORY_PERSONAL"] | new; free in 95,164 msgs | OK. Thread and Message-ID match headers; internal_date = header date; thread id >>20 = internal_date; label ids match X-Gmail-Labels; snippet is a prefix of the flattened body; weekdays correct |
| 23 | 86 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844311412966288046` | user frederick.stone | new; free in 81,404 threads | OK. Frederick mailbox exists; id free; history_id NULL; snippet equals its message row |
| 24 | 86 | gmail.gmail_messages | INSERT | `frederick.stone/<CAPT--p4a5fY9wd6vr+8J…` | 2025-09-26T07:40:26+00:00; labels ["INBOX","CATEGORY_PERSONAL"] | new; free in 95,164 msgs | OK. Thread and Message-ID match headers; internal_date = header date; thread id >>20 = internal_date; label ids match X-Gmail-Labels; snippet is a prefix of the flattened body; weekdays correct |
| 25 | 94 | gcal.gcal_events | INSERT | `evt_9a4c2e7f1b3d58e06c7a2f` | douglas 10-08 15:00-16:00Z | gcal/data.json#/calendars/6; id free in 10,395 | OK. Calendar exists; 15:00Z = 18:00 Istanbul; start_ts and end_ts are plan fields; created and updated before clock; `self` on this attendee; shared iCal UID across 4 distinct event ids matches base copy shape |
| 26 | 96 | gcal.gcal_events | INSERT | `evt_5c1e83a7d94b02f6c8e31a` | julia.lawson 10-08 15:00-16:00Z | gcal/data.json#/calendars/13; id free in 10,395 | OK. Calendar exists; 15:00Z = 18:00 Istanbul; start_ts and end_ts are plan fields; created and updated before clock; `self` on this attendee; shared iCal UID across 4 distinct event ids matches base copy shape |
| 27 | 98 | gcal.gcal_events | INSERT | `evt_a72f4d9e0c1b58d3e6f40b` | owen.baker 10-08 15:00-16:00Z | gcal/data.json#/calendars/25; id free in 10,395 | OK. Calendar exists; 15:00Z = 18:00 Istanbul; start_ts and end_ts are plan fields; created and updated before clock; `self` on this attendee; shared iCal UID across 4 distinct event ids matches base copy shape |
| 28 | 100 | gcal.gcal_events | INSERT | `evt_1d6b9a03e5c27f84b0d92c` | frederick.stone 10-08 15:00-16:00Z | gcal/data.json#/calendars/10; id free in 10,395 | OK. Calendar exists; 15:00Z = 18:00 Istanbul; start_ts and end_ts are plan fields; created and updated before clock; `self` on this attendee; shared iCal UID across 4 distinct event ids matches base copy shape |
| 29 | 102 | gdrive.drive_files | INSERT | `d_5f2c8e1b7a94d03c6e2b58` | ZM Live Ops | gdrive/data.json#/drive_files/11673; id free in 53,631 | OK. Parent is Julia's root folder; modified = L142 created; id free |
| 30 | 104 | gdrive.drive_files | INSERT | `f_7c3e91a4d2b85f60e1a9c4` | ZM3D beta live-ops calendar - working rules.docx | gdrive/data.json#/drive_files/2060; id free in 53,631 | OK. Parent is Frederick's root folder; Julia shared; `.docx` on Google Doc matches 539 base files; readable through L105 |
| 31 | 105 | gdocs.docs_documents | INSERT | `f_7c3e91a4d2b85f60e1a9c4` | ZM3D beta live-ops calendar - working rules | new; free in 595 docs | OK. Body 2,802 chars, non-empty; all 9 style runs exact on heading text with line breaks either side; times equal L104 |
| 32 | 125 | gdrive.drive_files | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | ZM3D beta UA plan | gdrive/data.json#/drive_files/2060; id free in 53,631 | OK. Presentation mime with no extension matches base; readable through L126-L139; null content_path matches all 132 base decks |
| 33 | 126 | gslides.slides_presentations | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | ZM3D beta UA plan | new; free in 132 | OK. Ids, owner, shares, times match L125 |
| 34 | 127 | gslides.slides_pages | INSERT | `slide_6f2a9d14c7e0` | index 0 | new; free in 4,540 object ids | OK. Page shape matches base |
| 35 | 128 | gslides.slides_page_elements | INSERT | `el_9d1c74b0a26e` | ZM3D beta UA plan | new; free in 4,540 object ids | OK. Element shape matches base; dated Sep 23, equal to drive created |
| 36 | 131 | gslides.slides_pages | INSERT | `slide_b83e51a09d72` | index 1 | new; free in 4,540 object ids | OK. Page shape matches base |
| 37 | 132 | gslides.slides_page_elements | INSERT | `el_5e83a1f4c092` | The four buy weeks | new; free in 4,540 object ids | OK. W1-W4 dates and weekdays match L11 and L105. ADV-5 |
| 38 | 138 | gslides.slides_pages | INSERT | `slide_0c47d2e81b6f` | index 2 | new; free in 4,540 object ids | OK. Page shape matches base |
| 39 | 139 | gslides.slides_page_elements | INSERT | `el_c07b2e9d3148` | Geos and budget | new; free in 4,540 object ids | OK. Unity retention line matches base (#executives 09-19 and 09-29). ADV-5 |
| 40 | 142 | gdrive.drive_files | INSERT | `f_e4a17c90b3d25f6a8c1d73` | ZM3D Beta Live-Ops Calendar.xlsx | parent from L102; id free in 53,631 | OK. Parent L102; `.xlsx` on Sheet matches 356 base files; shared to Frederick; readable through L143-L145 (lint exemption, ADV-15); web link unique in base |
| 41 | 143 | gsheets.sheets_spreadsheets | INSERT | `f_e4a17c90b3d25f6a8c1d73` | ZM3D Beta Live-Ops Calendar | new; free in 356 | OK. Ids, owner, shares, times match L142 |
| 42 | 144 | gsheets.sheets_sheets | INSERT | `f_e4a17c90…` sheet 0 | Calendar 200x9 | child of L143 | OK. 9 headers = column_count 9; JSON valid |
| 43 | 145 | gsheets.sheets_sheets | INSERT | `f_e4a17c90…` sheet 1 | Pushes 200x7 | child of L143 | OK. 7 headers = column_count 7; JSON valid |
| 44 | 150 | github.github_review_comments | INSERT | `match3d#470#rc_10` | 2025-09-30T15:51:06Z; CollectAndWinMainScreenController.cs | github/data.json#/pull_requests/2375; id free in 1,387; #/reviews/2176 | OK. Review `rev_9` APPROVED 15:51:06Z exists; path in PR #470 diff; before merge 15:51:15Z; next free seq. Confluence says Collect & Win not yet live; windows match `runtime.exs`. ADV-1 |
| 45 | 152 | github.github_reviews | INSERT | `match3d#468#rev_3` | COMMENTED 2025-09-29T15:36:41Z | github/data.json#/pull_requests/2372; id free in 2,230 | OK. Next free review seq; before merge 09-29 16:13:50Z; COMMENTED, empty body, null commit match base |
| 46 | 153 | github.github_review_comments | INSERT | `match3d#468#rc_38` | 2025-09-29T15:36:41Z; GameLoader.cs | github/data.json#/pull_requests/2372; id free in 1,387 | OK. Next free seq; path in #468 (`rc_1`); `Collect&Win Item Potion` prefabs only, no later vial model commit; references L152 |
| 47 | 154 | github.github_timeline_events | INSERT | `match3d#468#ev_6` | reviewed commit 648e2c7b | github/data.json#/pull_requests/2372; id free in 11,406 | OK. Next free seq; commit = PR head_sha, position 63, authored 09-26 22:03:06Z; blank actor and null date match all 2,116 base `reviewed` events. ADV-7 |
| 48 | 156 | slack.slack_messages | INSERT | `73bc730c620936feba3dcfbba00e2745` C093LEZGF6J ts 1759247468.897619 | user SLACK_BOT_0004; parent c2b9c903; rc 0/0 | new; id = sha256(channel\|ts)[:32]; free in 610,468 msgs / 4,840 files | OK. Mirror of L150: text equal with &amp; escape; attachment ts = comment second; 2.9 s lag; shape equals base; parent is #470 root |
| 49 | 158 | slack.slack_messages | UPDATE | `c2b9c90355cf8c2c4326ab19d3a24f79` | reply_count 16→17; users 1→1; latest 1759247478.371389→1759247478.371389 | slack/messages/C093LEZGF6J/2025-09.json#/579 | OK. Base 16 replies + L156 = 17; L156 earlier than base latest, so latest unchanged |
| 50 | 160 | github.github_review_comments | INSERT | `match3d#472#rc_1` | 2025-09-30T15:52:58Z; RewardVFXManager.cs | github/data.json#/pull_requests/2377; id free in 1,387; #/reviews/2179 | OK. Review `rev_1` APPROVED 15:52:58Z exists; path in #472 diff; before merge 15:53:04Z; first rc on PR. ADV-3 |
| 51 | 162 | slack.slack_messages | INSERT | `65564543e4bc8dd707a177aada2337a3` C093LEZGF6J ts 1759247580.842719 | user SLACK_BOT_0004; parent 61f686b8; rc 0/0 | new; id = sha256(channel\|ts)[:32]; free in 610,468 msgs / 4,840 files | OK. Mirror of L160: text equal; 2.84 s lag; parent is #472 root |
| 52 | 164 | slack.slack_messages | UPDATE | `61f686b8a8b6c164b14aff6b5b1897bf` | reply_count 3→4; users 1→1; latest 1759247586.958099→1759247586.958099 | slack/messages/C093LEZGF6J/2025-09.json#/589 | OK. Base 3 replies + L162 = 4; latest unchanged |
| 53 | 166 | slack.slack_messages | INSERT | `78aa8ed77c0bd7b8a3fad227b22bc3fb` C093LEZGF6J ts 1759160203.696979 | user SLACK_BOT_0004; parent 4b7c4127; rc 0/0 | new; id = sha256(channel\|ts)[:32]; free in 610,468 msgs / 4,840 files | OK. Mirror of L153: text equal; 2.70 s lag; parent is #468 root |
| 54 | 168 | slack.slack_messages | UPDATE | `4b7c41278397b56b36e9b2f8a820c454` | reply_count 41→42; users 1→1; latest 1759162433.383449→1759162433.383449; attachments_json 1 field | slack/messages/C093LEZGF6J/2025-09.json#/530 | OK. Base 41 replies + L166 = 42; latest unchanged; attachment diff is exactly one field (Reviewers gains Arthur, matching L152) |
| 55 | 173 | linear.linear_comments | INSERT | `cmt_zom429_1` | ZOM-429 seq 1; 2025-09-16T18:12:04Z | linear/data.json#/issues/3495; base comments 0 | OK. Author = assignee. Base updated_at 09-22 is later, so no issue UPDATE is needed. Superseded by L19 by date |
| 56 | 175 | linear.linear_comments | INSERT | `cmt_zom556_1` | ZOM-556 seq 1; 2025-09-24T15:20:38Z | linear/data.json#/issues/3632; base comments 0 | OK. Author = creator. Submission builds exist before 09-24 (iOS #43, Android #127). Ticket says 'bottom part' should reset |
| 57 | 176 | linear.linear_issues | UPDATE | ZOM-556 | updated_at 2025-09-22T14:44:06Z→2025-09-24T15:20:38Z | linear/data.json#/issues/3632 | OK. updated_at advances and equals the ticket's last comment |
| 58 | 178 | linear.linear_comments | INSERT | `cmt_zom565_1` | ZOM-565 seq 1; 2025-09-29T14:34:12Z | linear/data.json#/issues/3642; base comments 0 | OK. Commit `44988da015` 14:33:08Z on `marcus.bennett/EndlessMode_Vfx`; base Slack 14:34 'i wrote a comment on the linear task'; Gmail mention to Calvin 14:49:44Z; ticket text matches |
| 59 | 179 | linear.linear_comments | INSERT | `cmt_zom565_2` | ZOM-565 seq 2; 2025-09-30T16:12:27Z | linear/data.json#/issues/3642; base comments 0 | OK. Brian's list: 'P1/P2 – Endless mode remaining VFX'; ZOM-465 lists Refill Timer open |
| 60 | 180 | linear.linear_issues | UPDATE | ZOM-565 | updated_at 2025-09-25T13:46:04Z→2025-09-30T16:12:27Z | linear/data.json#/issues/3642 | OK. updated_at advances and equals the ticket's last comment |
| 61 | 182 | linear.linear_comments | INSERT | `cmt_zom543_1` | ZOM-543 seq 1; 2025-09-30T16:20:37Z | linear/data.json#/issues/3618; base comments 0 | OK. Author = assignee; #459 body and `QueueManager.cs` L52-58 give this flow; #472 merged 15:53:04Z |
| 62 | 183 | linear.linear_issues | UPDATE | ZOM-543 | updated_at 2025-09-25T17:44:22Z→2025-09-30T16:20:37Z | linear/data.json#/issues/3618 | OK. updated_at advances and equals the ticket's last comment |
| 63 | 185 | linear.linear_comments | INSERT | `cmt_zom526_1` | ZOM-526 seq 1; 2025-09-24T17:30:35Z | linear/data.json#/issues/3600; base comments 0 | OK. Calvin 09-18 Season Pass token path; Brian 09-24 'almost ready to merge'; `winAndCollect` branch attested |
| 64 | 186 | linear.linear_comments | INSERT | `cmt_zom526_2` | ZOM-526 seq 2; 2025-09-26T15:40:50Z | linear/data.json#/issues/3600; base comments 0 | OK. Brian created ZOM-521; matches L225 untick; Axe Arena postponed 09-22 (#company-internal) |
| 65 | 187 | linear.linear_comments | INSERT | `cmt_zom526_3` | ZOM-526 seq 3; 2025-09-30T16:24:19Z | linear/data.json#/issues/3600; base comments 0 | OK. After #472 merge; title matches |
| 66 | 188 | linear.linear_issues | UPDATE | ZOM-526 | updated_at 2025-09-17T15:52:10Z→2025-09-30T16:24:19Z | linear/data.json#/issues/3600 | OK. updated_at advances and equals the ticket's last comment |
| 67 | 190 | linear.linear_comments | INSERT | `cmt_zom552_1` | ZOM-552 seq 1; 2025-09-26T15:45:23Z | linear/data.json#/issues/3628; base comments 0 | OK. Author = assignee; commits `daeea991ce`, `ba194fd16b`; `SeasonPass_left`, `SeasonPass_premium` in code; state stays In Progress (SC-38) |
| 68 | 191 | linear.linear_issues | UPDATE | ZOM-552 | updated_at 2025-09-18T18:50:36Z→2025-09-26T15:45:23Z | linear/data.json#/issues/3628 | OK. updated_at advances and equals the ticket's last comment |
| 69 | 193 | linear.linear_comments | INSERT | `cmt_zom534_1` | ZOM-534 seq 1; 2025-09-25T16:35:04Z | linear/data.json#/issues/3608; base comments 0 | OK. Author = assignee; commit `47c65623e7` 'sync quests end with client'; Leonard 09-11 'my quest points are reset' |
| 70 | 194 | linear.linear_comments | INSERT | `cmt_zom534_2` | ZOM-534 seq 2; 2025-09-30T01:09:52Z | linear/data.json#/issues/3608; base comments 0 | OK. Description: '@Leonard said'; 00:00 UTC daily cron; store builds live; state stays In Progress |
| 71 | 195 | linear.linear_issues | UPDATE | ZOM-534 | updated_at 2025-09-15T15:10:32Z→2025-09-30T01:09:52Z | linear/data.json#/issues/3608 | OK. updated_at advances and equals the ticket's last comment |
| 72 | 197 | linear.linear_comments | INSERT | `cmt_zom432_1` | ZOM-432 seq 1; 2025-09-24T16:10:28Z | linear/data.json#/issues/3499; base comments 0 | OK. Author = assignee; before L198 |
| 73 | 198 | linear.linear_comments | INSERT | `cmt_zom432_2` | ZOM-432 seq 2; 2025-09-30T21:07:26Z | linear/data.json#/issues/3499; base comments 0 | OK. #471 merged 15:52:24Z with `Daily Gift.prefab` and `img - DailyGift.png` (`41a0d814ed`); tags TestFlight_iOS_50 and Submission_Android_135 on `3f5352a5b5`; builds done 19:15Z and 20:13Z. ADV-10 |
| 74 | 199 | linear.linear_issues | UPDATE | ZOM-432 | state_id Todo→Done; completed_at None→2025-09-30T21:07:26Z; updated_at 2025-07-23T09:48:01Z→2025-09-30T21:07:26Z | linear/data.json#/issues/3499 | OK. Done after L198; 120 of 427 base Done tickets also have no started_at |
| 75 | 201 | linear.linear_comments | INSERT | `cmt_zom78_1` | ZOM-78 seq 1; 2025-09-30T18:15:14Z | linear/data.json#/issues/3665; base comments 0 | OK. Ticket 'Event Calendar For Zombie Match 3D', created by Julia; before L11 |
| 76 | 202 | linear.linear_issues | UPDATE | ZOM-78 | updated_at 2025-04-26T09:21:59Z→2025-09-30T18:15:14Z | linear/data.json#/issues/3665 | OK. updated_at advances and equals the ticket's last comment |
| 77 | 204 | linear.linear_comments | INSERT | `cmt_zom465_1` | ZOM-465 seq 1; 2025-09-26T18:10:01Z | linear/data.json#/issues/3534; base comments 0 | OK. #456 (merged 09-24) and #458 (09-22) cover six icons; ticket marks Idle Icon done |
| 78 | 205 | linear.linear_comments | INSERT | `cmt_zom465_2` | ZOM-465 seq 2; 2025-09-30T18:05:02Z | linear/data.json#/issues/3534; base comments 0 | OK. No Collect & Win entry under `Assets/Animations/mainMenu/icons/`; #468 merged after L204 |
| 79 | 206 | linear.linear_issues | UPDATE | ZOM-465 | updated_at 2025-09-23T14:16:25Z→2025-09-30T18:05:02Z | linear/data.json#/issues/3534 | OK. updated_at advances and equals the ticket's last comment |
| 80 | 208 | linear.linear_comments | INSERT | `cmt_zom344_1` | ZOM-344 seq 1; 2025-09-16T16:20:28Z | linear/data.json#/issues/3403; base comments 0 | OK. Author = creator and assignee; ticket proposes the endless chest animation. ADV-2 |
| 81 | 209 | linear.linear_issues | UPDATE | ZOM-344 | state_id Todo→Done; completed_at None→2025-09-16T16:20:28Z; updated_at 2025-07-03T12:28:16Z→2025-09-16T16:20:28Z | linear/data.json#/issues/3403 | OK. Done with L208; see ADV-2 |
| 82 | 211 | linear.linear_comments | INSERT | `cmt_zom442_1` | ZOM-442 seq 1; 2025-09-19T15:10:51Z | linear/data.json#/issues/3510; base comments 0 | OK. Author = assignee; `ZombieLaneCellBase.cs` L226-227 send both params; state stays In Validation |
| 83 | 212 | linear.linear_issues | UPDATE | ZOM-442 | updated_at 2025-07-30T21:43:45Z→2025-09-19T15:10:51Z | linear/data.json#/issues/3510 | OK. updated_at advances and equals the ticket's last comment |
| 84 | 214 | linear.linear_comments | INSERT | `cmt_zom471_1` | ZOM-471 seq 1; 2025-09-17T16:45:30Z | linear/data.json#/issues/3541; base comments 0 | OK. Author = assignee; #zombie-match3d 08-13: Leonard 'we don't need it! cancel the ticket', Vincent 'it already has start button' |
| 85 | 215 | linear.linear_issues | UPDATE | ZOM-471 | updated_at 2025-08-13T18:01:16Z→2025-09-17T16:45:30Z | linear/data.json#/issues/3541 | OK. updated_at advances and equals the ticket's last comment |
| 86 | 217 | linear.linear_comments | INSERT | `cmt_zom504_1` | ZOM-504 seq 1; 2025-09-22T15:30:39Z | linear/data.json#/issues/3577; base comments 0 | OK. Author = creator. ADV-6 |
| 87 | 218 | linear.linear_issues | UPDATE | ZOM-504 | updated_at 2025-09-15T15:10:41Z→2025-09-22T15:30:39Z | linear/data.json#/issues/3577 | OK. updated_at advances and equals the ticket's last comment |
| 88 | 220 | linear.linear_comments | INSERT | `cmt_zom517_1` | ZOM-517 seq 1; 2025-09-18T17:40:54Z | linear/data.json#/issues/3591; base comments 0 | OK. Author = creator |
| 89 | 221 | linear.linear_issues | UPDATE | ZOM-517 | updated_at 2025-09-03T22:22:22Z→2025-09-18T17:40:54Z | linear/data.json#/issues/3591 | OK. updated_at advances and equals the ticket's last comment |
| 90 | 223 | linear.linear_comments | INSERT | `cmt_zom521_1` | ZOM-521 seq 1; 2025-09-26T17:25:02Z | linear/data.json#/issues/3596; base comments 0 | OK. Author = assignee; matches L225 unticked items; Calvin card work 09-29 |
| 91 | 224 | linear.linear_comments | INSERT | `cmt_zom521_2` | ZOM-521 seq 2; 2025-09-30T16:27:38Z | linear/data.json#/issues/3596; base comments 0 | OK. #475 merged 16:09:15Z; ZOM-528 and ZOM-541 exist and are In Progress |
| 92 | 225 | linear.linear_issues | UPDATE | ZOM-521 | description 6 ticked→4 ticked, 2 open; updated_at 2025-09-17T15:50:49Z→2025-09-30T16:27:38Z | linear/data.json#/issues/3596 | OK. Diff is exactly two lines; order and spacing preserved; resolves SC-15 in line with ZOM-526 and ZOM-528 In Progress |
| 93 | 234 | linear.linear_comments | INSERT | `cmt_zom542_1` | ZOM-542 seq 1; 2025-09-22T18:40:21Z | linear/data.json#/issues/3617; base comments 0 | OK. Author = assignee; state stays Regression |
| 94 | 235 | linear.linear_issues | UPDATE | ZOM-542 | updated_at 2025-09-14T22:59:17Z→2025-09-22T18:40:21Z | linear/data.json#/issues/3617 | OK. updated_at advances and equals the ticket's last comment |
| 95 | 237 | linear.linear_comments | INSERT | `cmt_zom544_1` | ZOM-544 seq 1; 2025-09-29T15:35:50Z | linear/data.json#/issues/3619; base comments 0 | OK. Author = creator; Vincent 09-25 test: levels, currencies, cards all no_entry; 09-30 'data sycning' still pending |
| 96 | 238 | linear.linear_issues | UPDATE | ZOM-544 | updated_at 2025-09-22T13:41:02Z→2025-09-29T15:35:50Z | linear/data.json#/issues/3619 | OK. updated_at advances and equals the ticket's last comment |
| 97 | 240 | linear.linear_comments | INSERT | `cmt_zom546_1` | ZOM-546 seq 1; 2025-09-24T19:00:57Z | linear/data.json#/issues/3621; base comments 0 | OK. Author = assignee; no later base refill-count report |
| 98 | 241 | linear.linear_issues | UPDATE | ZOM-546 | updated_at 2025-09-15T18:39:28Z→2025-09-24T19:00:57Z | linear/data.json#/issues/3621 | OK. updated_at advances and equals the ticket's last comment |
| 99 | 243 | linear.linear_comments | INSERT | `cmt_zom549_1` | ZOM-549 seq 1; 2025-09-26T16:50:46Z | linear/data.json#/issues/3624; base comments 0 | OK. `AnalyticsManager.cs` L508-510 send all three (landed 09-17 `f44fe52b7f`); `left_level` block has no total_equipped_power |
| 100 | 244 | linear.linear_issues | UPDATE | ZOM-549 | updated_at 2025-09-22T13:40:39Z→2025-09-26T16:50:46Z | linear/data.json#/issues/3624 | OK. updated_at advances and equals the ticket's last comment |
| 101 | 246 | linear.linear_comments | INSERT | `cmt_zom566_1` | ZOM-566 seq 1; 2025-09-30T17:53:19Z | linear/data.json#/issues/3643; base comments 0 | OK. #zm-collect-win 09-30: 'Analytics and name changes first', 'none of them blockers'; ticket created 16:26:02Z |
| 102 | 247 | linear.linear_comments | INSERT | `cmt_zom566_2` | ZOM-566 seq 2; 2025-09-30T19:40:47Z | linear/data.json#/issues/3643; base comments 0 | OK. Author = assignee; PR #477 22:26:30Z; DM 22:08 'estoy agregando eventos de analytics' |
| 103 | 248 | linear.linear_issues | UPDATE | ZOM-566 | state_id Todo→In Progress; started_at None→2025-09-30T17:20:13Z; updated_at 2025-09-30T16:26:02Z→2025-09-30T19:40:47Z | linear/data.json#/issues/3643 | OK. Base Todo; started after creation (16:26:02Z) and after Owen's 16:49 Slack; PR #477 later |
| 104 | 250 | linear.linear_comments | INSERT | `cmt_zom563_1` | ZOM-563 seq 1; 2025-09-30T22:04:33Z | linear/data.json#/issues/3640; base comments 0 | OK. DM: Douglas 18:16 prod update, Vincent 21:58 'Yep it works as expected'; ticket started 18:14:25Z |
| 105 | 251 | linear.linear_issues | UPDATE | ZOM-563 | state_id In Progress→Done; completed_at None→2025-09-30T22:04:33Z; updated_at 2025-09-30T18:14:25Z→2025-09-30T22:04:33Z | linear/data.json#/issues/3640 | OK. Done after Vincent's 21:58 confirmation |
| 106 | 253 | trello.trello_actions | INSERT | `68dac8204f1e9a3b7c2d5e61` | commentCard 2025-09-29T17:55:44Z | trello/data.json#/cards/781; id free in 5,252 | OK. Action id prefix 0x68dac820 = 2025-09-29T17:55:44Z = date; author created the card; card/list/board ids and shortLinks match base actions; list name matches 63 base actions (SC-13); Mon Oct 13 weekday correct and weekly cron is MON 00:00 in `quests-stack.ts` |
| 107 | 255 | trello.trello_cards | UPDATE | `68c452a03006277f55d9dc96` | badges.comments 0→1; dateLastActivity 2025-09-12T17:31:20Z→2025-09-29T17:55:44Z | trello/data.json#/cards/781 | OK. Base comments 0 to 1 (L253 is the only comment); other badge keys unchanged; 09-12 to 09-29, later than base and before clock |

## 11. Stage ownership and evidence record

Intended `input_manifest.json` injection entry (not written, per the setup):

```json
{"review_version":"injection-static-v2","evidence_contract":"stage-evidence-v1","reused_evidence":[],"sql_sha256":"ffbac4586fb91842ca16263c2b76987c26623c7ed689e00d33886c63f9331bdc","universe":"synthcut","universe_manifest_sha256":"da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a"}
```

Reusable by `/prompt` while the SQL hash, base manifest and references above stay unchanged: key uniqueness, actor and reference resolution, thread counts, SQL structure, and the Docs offsets. Any SQL change, including an advisory fix, invalidates the affected rows. Task discoverability, persona reach and Unique Ground Truth stay with `/prompt`. Advisories ADV-1 to ADV-6 are flagged for it specifically.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (level not reported by the runtime)

Next action: Proceed to /prompt. Before that review, consider the one-line fixes for ADV-1 to ADV-6; ADV-1 and ADV-2 matter most. Any SQL edit needs a rerun of this stage.

Evidence limits: No required static check is unresolved. Outside this static scope: live execution and deployment; current database compatibility (the snapshot is unverified, 12 used columns are NOT COVERED, and the live schema file named in the SQL header was not opened by instruction); actual search ranking and Agent visibility. Two facts cannot be settled from the export: what Douglas's Sep 30 prod update contained (ADV-1), and whether `state_history_json` needs updating for the four state changes (ZOM-344, ZOM-432, ZOM-563, ZOM-566), because the export has no state history. Sprites are Git LFS pointers, so art claims were checked by file change, not by eye. The report is saved in the review folder, not through `hg_write_output.py`, as the setup requires.
