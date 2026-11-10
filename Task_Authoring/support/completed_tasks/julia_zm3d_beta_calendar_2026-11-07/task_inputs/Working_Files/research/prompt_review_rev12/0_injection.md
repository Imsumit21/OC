# Injection Data-Integrity Report (Eval 0), delta review of rev12

**Review version:** `injection-static-v2`
**Evidence contract:** `stage-evidence-v1`
**Reused evidence:** the rev11 report (section 12). Everything on changed or new statements is NEW.

## 1. Scope and provenance

| Item | Value |
|---|---|
| Review | Independent `/injection` delta review, chat/attachment mode, audit only |
| Actual review time | 2026-11-06 (machine clock 2026-11-06T11:52Z; not the task clock) |
| Universe | Oct 1, 2025 (synth-cut), `hg4-synth-sep30cut` v16 |
| Fixed clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| SQL under review | `R12/inputs/01_Universe_Inject.sql`, sha256 `b5ccbfa577fc9f2c8f6eb3098f8d62a16623d799f41d11285de8227f1bed60d3`, 265 lines, 111 statements |
| Previous SQL | `R12/prev/01_Universe_Inject.rev11.sql`, sha256 `1348d287ac4a105c41b9f0bf511c6664e306adcc3cf42406688a228fd4b684e7`, 110 statements |
| Previous reports | rev11 `review_rev11/out/0_injection.md`, sha256 `a069bf09d0684c98342b0416a2d99c59754852dbf8de08ee7f415a9adb4dcc12` (hash rechecked); it reuses rev10 `review_rev10/out/0_injection.md`, sha256 `67e1ab6fe77bf78e8f7010487272ed2a2ddf056f4a54d5ade27b6c486ecc7e0a` |
| Universe manifest | sha256 prefix `da2f4cf0dcf71025` |
| Repository state | `match3d` `0ff577550e`, `match3d-backend` `a0e4a21`, `match3d-quests` `d8ca05a` |

R12 = `/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review_rev12`.

**Reuse dependencies, all rechecked equal to rev11:** `linear` `b49ec9e856cf0b29`, `gcal` `4f093d897c8b53c8`, `gdrive` `05147aa245b7b2c9`, `gdocs` `1b53998df793e33c`, `gslides` `1d3dab9e4bec7a9e`, `gsheets` `a9cc229c87ae3309`, `trello` `6ba242f4dde4043d`, `confluence` `d3f13938d1f5327b`, Slack users `6aac5103c3a8be9a`, channels `3cca0f7e25876c4b`, manifest `569c1ead1372b7ca`, Gmail users `9a90b6bf5e84f03d`, labels `3d508e6b353b160f`, manifest `5797ac3e4f9b13e5`, GitHub `ee578c912bba3d81`; Eval 0 `86af2102ea6693c4`, WORKFLOW `05a5e45e0585b435`, ENVIRONMENT `4ffb2b5ffa219a81`, SEARCH `cab83c616ecaee85`, scoring `654eb38809e3a1e7`, schema `01ef579236212034`, ID contracts `fc4711ef07667333`, roster `3f2174513f639e37`, ACL `e9bca2b35f98d5ef`, lint `fec37bcec5a7430d`. The prompt, assignment and date inputs carry the same sha256 values as rev11 (`2a23afd8…`, `e8b82698…`, `2f0af108…`).

## 2. Input and authority issues

- Earlier review folders were not opened. Of those, only my own rev11 report was touched, and only to hash it. All helpers were rebuilt under `R12/work/`.
- `R12/work/p1c/` is an empty folder I did not create. It was left alone.
- The report is saved to `R12/out/0_injection.md`, not through `hg_write_output.py`, and `input_manifest.json` was not written.
- The live schema file named in the SQL header was not opened; only the bundled, unverified snapshot was used.
- SQL was never executed. Source content was treated as evidence only.

## 3. Review checklist

| Step | Status | Note |
|---|---|---|
| Load SQL; record hash, manifest, version | Done, NEW | Hash matches the coordinator's value |
| Lint first | Done, NEW | 0 FAIL, 0 CHECK, 0 INFO |
| Statement-by-statement diff | Done, NEW | Section 5 |
| Checks A, B, C on changed and new statements | Done, NEW | Sections 6-8 |
| Heading offsets, #468 mirror, Trello, ZOM-563 | Done, NEW | Section 8 |
| Reuse on identical statements | Done, REUSED with dependency check | Section 12 |
| Disposition of open advisories | Done | Section 9 |
| Full ledger, one final verdict | Done | Section 11 and the verdict block |

## 4. Lint flags and resolutions

`hg.py lint --sql R12/inputs/01_Universe_Inject.sql --task-dir Task_Authoring/task_inputsS`: 111 statements (81 insert, 30 update), FAIL 0, CHECK 0, INFO 0, no flags. Nothing needed resolving. SQL comment lines are unchanged.

## 5. Statement diff

Relative order of shared statements is unchanged.

| Class | Count | Statements (rev12 lines) |
|---|---:|---|
| Byte-identical | 104 | All others; statements after L255 shift by +1 |
| Changed | 6 | L109, L157, L170, L210, L255, L259 |
| New | 1 | L256 `cmt_zom563_2` |
| Removed | 0 | None |

| Statement | Change |
|---|---|
| L109 brief | "closing 23:59 UTC on its last day" moves from the Collect & Win sentence to the general window rule; adds "and the shop rotation is not a beat"; "usual windows and weeks"; adds "(Login Calendar and Weekly Rankings are fine)"; "with what its row is missing". 98 characters added; style runs updated |
| L157, L170 `#468#rc_38` and mirror | Adds "and need to be in before the beta" |
| L210 `cmt_zom465_3` | "was ticked before that event merged" replaces "was written before that event came in" |
| L255 `cmt_zom563_1` | Now Douglas at 18:17:05Z: "Prod has the teams and social changes now. That update carried only these, the Collect & Win server windows wait for the Oct 8 release." |
| L256 `cmt_zom563_2` (new) | Vincent's rev11 closing comment moved here, sequence 2, 22:04:33Z |
| L259 Trello | Restores `idCard` and `textData`; `list` stays out |

## 6. Results for checks A-C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | One new key, free; authors, ticket and review links resolve; no Slack or Gmail key changed. Section 7. |
| B — SQL structure and supported schema rules | PASS | 111 statements parse; counts match; 132 JSON literals valid; no new columns. Section 7. |
| C — Dates, relationships and consistency | PASS | No future event dates; 9 heading runs exact; mirror equals body; ZOM-563 order and stamps correct; new claims attested. No demonstrated contradiction. Section 8. |

## 7. Checks A and B

**Check A.**
- `cmt_zom563_2` is free: base Linear has 0 comments, and the 32 SQL ids are unique.
- `hg.py records`, 5 checks on the touched collections: all `scan_complete: true`, no errors. 41 users, 3,687 issues, 1,387 review comments, 5,252 Trello actions.
- `usr_cd7849ec043ab3da` is Douglas, the ZOM-563 assignee. `usr_65c76e0b87aa7e9b` is Vincent, its creator.
- Slack and Gmail collision results are REUSED: no key changed, and the rev11 manifest fingerprints match (81,404 thread files still present).
- All other keys are byte-identical to rev11.

**Check B.**
- 111 statements parse; column and value counts equal on all 81 inserts; no upsert, expression or cast.
- L255 and L256 precede the L257 UPDATE.
- 132 JSON literals parse. Linear `*_at` values are all `YYYY-MM-DDTHH:MM:SSZ`. Generated columns untouched. No required column omitted.
- Snapshot: no new columns. The same 12 remain NOT COVERED (ADV-13).

## 8. Check C: dates, relationships and consistency

**Dates.** The only values after the clock are the eight Oct 8 `start_ts` and `end_ts` plan fields. The latest event is L17 at 2025-09-30T22:10:41Z. Linear order and `updated_at` were recomputed for all 32 comments and 21 UPDATEs: no fault. Slack was rescanned (610,468 messages) for searches, and all 8 base thread rollups recompute correctly.

### 8.1 Heading offsets (L109)

Body is 3,090 characters, LF only. Each run was recomputed; each sits on the exact heading text, with a line break on both sides, and each heading occurs once.

| Style | Text | rev11 | rev12 |
|---|---|---|---|
| TITLE | ZM3D beta live-ops calendar - working rules | 0-43 | 0-43 |
| HEADING_2 | Span and time base | 163-181 | 163-181 |
| HEADING_2 | Scope | 609-614 | 606-611 |
| HEADING_2 | When a beat starts | 760-778 | 794-812 |
| HEADING_2 | Held or not | 1284-1295 | 1318-1329 |
| HEADING_2 | One-offs | 1912-1920 | 1956-1964 |
| HEADING_2 | Still to do | 2120-2131 | 2164-2175 |
| HEADING_2 | Push copy | 2437-2446 | 2481-2490 |
| HEADING_2 | Config locks | 2765-2777 | 2863-2875 |

New brief facts:
- "Shop rotation": Confluence *Economy Design* has "The daily rotating shop", and Slack uses "rotating shop" from July.
- "Login Calendar and Weekly Rankings": the PNs Beta rows are "Login Calendar update" and the headline "Weekly Rankings Reset!" (sheet hash unchanged from rev10).

### 8.2 #468 mirror against its GitHub body

- Body (L157): "The Collect & Win vials that spawn in the levels are still the first-pass models. The final vial models are missing and need to be in before the beta, Claire has those on her list."
- Mirror (L170): identical after unescaping `&amp;`.
- Attachment `ts` 1759160201 equals the comment's second (09-29 15:36:41Z); lag 2.70 s.
- `text` is the only attachment key that changed and `attachments_json` the only row column. `body` is the only L157 column that changed.
- The #470 and #472 mirrors still equal their bodies too.
- The note still precedes the #468 merge at 16:13:50Z. See ADV-22 for "before the beta".

### 8.3 Trello payload (L259)

| Population | `data` keys | Count |
|---|---|---:|
| **rev12 row** | **board, card, idCard, text, textData** | **0 of 56 exact** |
| rev11 row | board, card, text | 1 of 56 exact |
| rev10 row | board, card, idCard, list, text, textData | 14 of 56 exact |
| ZM ROADMAP comments carrying `list` | | 12 of 12 |
| Base rows with `idCard` or `textData` but no `list` | | 0 |

Not a defect. Eval 0 bars inferring constraints from stored examples, no documented rule requires `list`, and base already holds two commentCard rows without it. JSON is valid; `data.idCard` equals the column and `card.id`; `textData` matches base; kept values equal rev11; L261 stays correct.

The row is one key from this board's shape, but the exact key set is one base doesn't contain. That follows from my rev11 fallback suggestion to restore only the other two keys. Restoring `list` makes it match 14 rows exactly (ADV-18).

### 8.4 ZOM-563 comment order and stamps

| Time (UTC) | Record | Source |
|---|---|---|
| 09-23 07:36:43 | Ticket created | Base |
| 09-30 18:14:25 | `started_at` | Base |
| 18:16:33 | Douglas "Ok, I updated the prod environment with the latest teams/social changes" | Base DM |
| **18:17:05** | **L255, Douglas, sequence 1** | Injected |
| 21:58:44 | Vincent "Yep it works as expected" | Base DM |
| **22:04:33** | **L256, Vincent, sequence 2** | Injected |
| 22:04:33 | L257 `completed_at` and `updated_at`, state Done | Injected, unchanged |

Order and sequence agree. `created_at` equals `updated_at` on both comments. `updated_at` on the ticket equals the last comment. "the Oct 8 release" matches L98. "only these" fits the DM's "teams/social" and cannot be tested from git, so it stands as Douglas's own statement.

### 8.5 L210

Calvin's base DM on 09-17 ("I've updated the Master ticket VFX implementation and the remaining tickets") and the ZOM-521 base `updated_at` of 09-17 put the ticks before #468 merged on 09-29, so the new wording is supported.

## 9. What happened to each open advisory

Open after rev11: ADV-1, 2, 3, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21. ADV-4, 5, 6 and 11 closed earlier and stay closed.

| ADV | Subject | rev12 status | Current marking |
|---|---|---|---|
| 1 | Sep 30 prod update vs "DEV stack only" | **Closed.** L255 scopes the update on a record Julia can read, and it is the suggested fix. Note for `/prompt`: Douglas is the deployer, so this is his own statement; L154 and Confluence support the state before the update | None |
| 2 | ZOM-344 close vs chest timing | **Open, unchanged.** L213 and L214 byte-identical | CSC |
| 3 | Premium strip wording | Open, unchanged | Cosmetic |
| 7 | `#468#ev_6` order | Open, unchanged | Cosmetic |
| 8 | `revision_id` pattern | Open, unchanged | Cosmetic |
| 9 | #468 Reviewers edit | Open, unchanged | Cosmetic |
| 10 | Daily Gift frame not confirmed by eye | Open, unchanged | Cosmetic |
| 12 | Change-request clause has no record | Open, unchanged; clause still in L109 | Cosmetic |
| 13 | 12 columns NOT COVERED | Open, unchanged; no new columns | Cosmetic |
| 14 | Julia not listed in #zombie-prs | Open, unchanged | Cosmetic |
| 15 | Sheet has NULL `content_path` | Open, unchanged | Cosmetic |
| 16 | Gmail LF and short headers | Open, unchanged | Cosmetic |
| 17 | "Written before that event came in" | **Closed.** L210 uses the suggested wording, and base supports it | None |
| 18 | Trello payload shape | **Reduced.** Two of three keys restored; `list` still absent | Cosmetic |
| 19 | #zm-collect-win archived flag, Julia not listed | Open, unchanged | Cosmetic |
| 20 | "Event icon" is a widget | Open, unchanged | Cosmetic |
| 21 | 23:59 close vs 00:00 cron | **Moved.** Now a general window rule in L109; the gap is the same | Cosmetic |

CSC = a /prompt reviewer could score this under Cross-Service Coherence.

## 10. Findings

### Demonstrated defects

None. No statement violates a rule in Checks A, B or C on the evidence available.

### Advisories: a /prompt reviewer could score this under Cross-Service Coherence

**ADV-2. ZOM-344 closes on "reads well" while the quest chest timing complaint runs on (open since rev10).**
- Injected: L213 (09-16) "Quest box open and close animation reuses the endless chest curve and reads well on the quest screen. Art side is signed off on my end."; L214 sets Done.
- Base: Marcus 08-11 "some chest quest animations show the reward before the chest open"; Marcus DM 09-23 "the rewards appears first and then the chest opens"; Marcus DM 09-30 "The chest opens before the rewards and I haven't done it like that. Sometimes it plays ok u know"; Vincent, Bug Checklist 09-30 "the timing is off. Especially in the quest chests."
- Not a defect: art sign-off and reward timing on claim are different scopes.
- Fix: end L213 with "Art side is signed off on my end. The reward-before-open timing on claim is a separate integration issue."

**ADV-22 (new, lower likelihood). "Before the beta" sits awkwardly with builds already submitted.**
- Injected: L157 (09-29) "need to be in before the beta"; L210 (09-30 18:13:41Z) "does have to land before the beta"; L132 "Beta-cohort buy, starting once the stores approve the Sep 30 builds."
- Base: submission builds iOS #50 and Android #135 started at 18:43-18:45Z on `3f5352a5b5` (tags `TestFlight_iOS_50`, `Submission_Android_135`), which include #468. No vial or Collect & Win icon art reaches `main` by the clock. So the builds the buy starts on carry first-pass vials and no icon animation.
- Not a defect: L27 points to a "next store build", and Collect & Win can't start before the Oct 8 release, so a later build can carry both. The brief asks for exactly this kind of item.
- Fix: in L157, L170 and L210 use the brief's own phrase, "before Collect & Win runs for bought users". L157 and L170 must stay equal.

### Advisories: cosmetic

- **ADV-3.** L164 still uses "October range" and "date change" for an art item.
- **ADV-7.** `#468#ev_6` sorts after merged and closed because `created_at` is NULL, as in base.
- **ADV-8.** `revision_id` values don't follow the base first-10-hex pattern; unlisted field.
- **ADV-9.** The #468 parent gains Arthur in Reviewers; base #472 wasn't updated that way.
- **ADV-10.** Samuel's Daily Gift list mentions only font and alignment. The sprite changed in #471, but it is an LFS pointer.
- **ADV-12.** The brief's change-request clause has no qualifying record; the latest CHANGES_REQUESTED is `match3d#303`, 2025-07-16.
- **ADV-13.** 12 columns are NOT COVERED by the unverified snapshot: `extras_json`, `drive_id`, `notes`, `ordinal`, `table_json`, `pull_request_review_id`, `seq` (review comments and reviews), `side`, `start_line`, `start_side`, `subject_type`, `sequence`. Confirm against the live schema before deploy.
- **ADV-14.** Julia isn't in the listed members of public `#zombie-prs`; GitHub is unscoped, so nothing depends on the mirrors.
- **ADV-15.** The injected sheet has NULL `content_path`, unlike all 356 base sheets; it is served through its Sheets rows and passes the lint rule.
- **ADV-16.** Gmail bodies use LF where base uses CRLF, and the header set is short.
- **ADV-18.** L259 Trello `data` has no `list`, which leaves a key set no base row has (section 8.3). Fix: add `"list":{"id":"6851a674975da1fe76e70d93","name":"BETA: Sep 30"}` after `idCard`. That name matches 63 base actions, despite the SC-13 list-name quirk.
- **ADV-19.** L35 sits in `#zm-collect-win`: `is_archived: true` (SC-57) and Julia is not a listed member. Brian's ask is in the same public channel, so whoever can read the ask can read the reply.
- **ADV-20.** "Event icon" at L209 and L210 is really a progress-bar widget with a bottle icon. The claim holds in substance.
- **ADV-21.** L109 says windows close 23:59 UTC; the cron resets at 00:00 the next day (`0 0 * * 3`). This follows the brief's own "Sun Nov 2 23:59 UTC" convention.

## 11. Full operation ledger

Operation order as in rev12. "rev11 line" is blank for the new statement. IDENTICAL rows point at the rev11 report's ledger, which carries rev10's source pointers forward.

| # | Line | rev11 line | Table | Op | Record / target | Status | Result |
|---|---|---|---|---|---|---|---|
| 1 | 11 | 11 | slack.slack_messages | INSERT | `bca784379e7dbca9e64e79a64dfefbba` | IDENTICAL | REUSED rev11 ledger #1 |
| 2 | 13 | 13 | slack.slack_messages | INSERT | `890dc27f56e8501bd7590ffdfc231057` | IDENTICAL | REUSED rev11 ledger #2 |
| 3 | 15 | 15 | slack.slack_messages | INSERT | `933cee9f6464a80e4b1f05259b595b20` | IDENTICAL | REUSED rev11 ledger #3 |
| 4 | 17 | 17 | slack.slack_messages | INSERT | `669d15f685f158633e56302160957f1e` | IDENTICAL | REUSED rev11 ledger #4 |
| 5 | 19 | 19 | slack.slack_messages | INSERT | `b5f2955c2e154efc6835946ecfe1758e` | IDENTICAL | REUSED rev11 ledger #5 |
| 6 | 21 | 21 | slack.slack_messages | UPDATE | `9025d428af1f551a20e303c3acbc545b` | IDENTICAL | REUSED rev11 ledger #6 |
| 7 | 23 | 23 | slack.slack_messages | INSERT | `e343557b2e94a1701251ebd079e6f0ce` | IDENTICAL | REUSED rev11 ledger #7 |
| 8 | 25 | 25 | slack.slack_messages | UPDATE | `ede90bc6ec6cb16fd97663f2888f39a2` | IDENTICAL | REUSED rev11 ledger #8 |
| 9 | 27 | 27 | slack.slack_messages | INSERT | `a08ff7cbfc52008d7dee8457e9385a3c` | IDENTICAL | REUSED rev11 ledger #9 |
| 10 | 29 | 29 | slack.slack_messages | UPDATE | `d0dd5d3ad4658add1f79802e2aa60e48` | IDENTICAL | REUSED rev11 ledger #10 |
| 11 | 31 | 31 | slack.slack_messages | INSERT | `532747cb5d123a95d13204e57b5a7a38` | IDENTICAL | REUSED rev11 ledger #11 |
| 12 | 33 | 33 | slack.slack_messages | UPDATE | `a3e78e820b9f880ef4e3d941562110df` | IDENTICAL | REUSED rev11 ledger #12 |
| 13 | 35 | 35 | slack.slack_messages | INSERT | `7d70c7753179c98b6c8b2b5457a1e5e7` | IDENTICAL | REUSED rev11 ledger #13 |
| 14 | 37 | 37 | slack.slack_messages | UPDATE | `0069f6143e89802993b39e442d3baeb2` | IDENTICAL | REUSED rev11 ledger #14 |
| 15 | 39 | 39 | gmail.gmail_threads | INSERT | `brian.foster@harmonygames.co/1843954828968110017` | IDENTICAL | REUSED rev11 ledger #15 |
| 16 | 40 | 40 | gmail.gmail_messages | INSERT | `brian.foster/<CAPT--p4sBC8XnaA7qB…` | IDENTICAL | REUSED rev11 ledger #16 |
| 17 | 50 | 50 | gmail.gmail_threads | INSERT | `julia.lawson@harmonygames.co/1843954828968533812` | IDENTICAL | REUSED rev11 ledger #17 |
| 18 | 51 | 51 | gmail.gmail_messages | INSERT | `julia.lawson/<CAPT--p4sBC8XnaA7qB…` | IDENTICAL | REUSED rev11 ledger #18 |
| 19 | 61 | 61 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843954828968789474` | IDENTICAL | REUSED rev11 ledger #19 |
| 20 | 62 | 62 | gmail.gmail_messages | INSERT | `frederick.stone/<CAPT--p4sBC8XnaA7qB…` | IDENTICAL | REUSED rev11 ledger #20 |
| 21 | 72 | 72 | gmail.gmail_threads | INSERT | `brian.foster@harmonygames.co/1844311412965607905` | IDENTICAL | REUSED rev11 ledger #21 |
| 22 | 73 | 73 | gmail.gmail_messages | INSERT | `brian.foster/<CAPT--p4a5fY9wd6vr+…` | IDENTICAL | REUSED rev11 ledger #22 |
| 23 | 81 | 81 | gmail.gmail_threads | INSERT | `julia.lawson@harmonygames.co/1844311412966040123` | IDENTICAL | REUSED rev11 ledger #23 |
| 24 | 82 | 82 | gmail.gmail_messages | INSERT | `julia.lawson/<CAPT--p4a5fY9wd6vr+…` | IDENTICAL | REUSED rev11 ledger #24 |
| 25 | 90 | 90 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844311412966288046` | IDENTICAL | REUSED rev11 ledger #25 |
| 26 | 90 | 90 | gmail.gmail_messages | INSERT | `frederick.stone/<CAPT--p4a5fY9wd6vr+…` | IDENTICAL | REUSED rev11 ledger #26 |
| 27 | 98 | 98 | gcal.gcal_events | INSERT | `evt_9a4c2e7f1b3d58e06c7a2f` | IDENTICAL | REUSED rev11 ledger #27 |
| 28 | 100 | 100 | gcal.gcal_events | INSERT | `evt_5c1e83a7d94b02f6c8e31a` | IDENTICAL | REUSED rev11 ledger #28 |
| 29 | 102 | 102 | gcal.gcal_events | INSERT | `evt_a72f4d9e0c1b58d3e6f40b` | IDENTICAL | REUSED rev11 ledger #29 |
| 30 | 104 | 104 | gcal.gcal_events | INSERT | `evt_1d6b9a03e5c27f84b0d92c` | IDENTICAL | REUSED rev11 ledger #30 |
| 31 | 106 | 106 | gdrive.drive_files | INSERT | `d_5f2c8e1b7a94d03c6e2b58` | IDENTICAL | REUSED rev11 ledger #31 |
| 32 | 108 | 108 | gdrive.drive_files | INSERT | `f_7c3e91a4d2b85f60e1a9c4` | IDENTICAL | REUSED rev11 ledger #32 |
| 33 | 109 | 109 | gdocs.docs_documents | INSERT | `f_7c3e91a4d2b85f60e1a9c4` | CHANGED | CHANGED body and style runs: 4 lines edited, 98 chars added. All 9 runs recomputed exact; times, owner, shares unchanged. 'Shop rotation' attested (Confluence 'daily rotating shop'); Login Calendar and Weekly Rankings match PNs Beta row text. ADV-21 |
| 34 | 129 | 129 | gdrive.drive_files | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | IDENTICAL | REUSED rev11 ledger #34 |
| 35 | 130 | 130 | gslides.slides_presentations | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | IDENTICAL | REUSED rev11 ledger #35 |
| 36 | 131 | 131 | gslides.slides_pages | INSERT | `slide_6f2a9d14c7e0` | IDENTICAL | REUSED rev11 ledger #36 |
| 37 | 132 | 132 | gslides.slides_page_elements | INSERT | `el_9d1c74b0a26e` | IDENTICAL | REUSED rev11 ledger #37 |
| 38 | 135 | 135 | gslides.slides_pages | INSERT | `slide_b83e51a09d72` | IDENTICAL | REUSED rev11 ledger #38 |
| 39 | 136 | 136 | gslides.slides_page_elements | INSERT | `el_5e83a1f4c092` | IDENTICAL | REUSED rev11 ledger #39 |
| 40 | 142 | 142 | gslides.slides_pages | INSERT | `slide_0c47d2e81b6f` | IDENTICAL | REUSED rev11 ledger #40 |
| 41 | 143 | 143 | gslides.slides_page_elements | INSERT | `el_c07b2e9d3148` | IDENTICAL | REUSED rev11 ledger #41 |
| 42 | 146 | 146 | gdrive.drive_files | INSERT | `f_e4a17c90b3d25f6a8c1d73` | IDENTICAL | REUSED rev11 ledger #42 |
| 43 | 147 | 147 | gsheets.sheets_spreadsheets | INSERT | `f_e4a17c90b3d25f6a8c1d73` | IDENTICAL | REUSED rev11 ledger #43 |
| 44 | 148 | 148 | gsheets.sheets_sheets | INSERT | `sheet 0 Calendar` | IDENTICAL | REUSED rev11 ledger #44 |
| 45 | 149 | 149 | gsheets.sheets_sheets | INSERT | `sheet 1 Pushes` | IDENTICAL | REUSED rev11 ledger #45 |
| 46 | 154 | 154 | github.github_review_comments | INSERT | `match3d#470#rc_10` | IDENTICAL | REUSED rev11 ledger #46 |
| 47 | 156 | 156 | github.github_reviews | INSERT | `match3d#468#rev_3` | IDENTICAL | REUSED rev11 ledger #47 |
| 48 | 157 | 157 | github.github_review_comments | INSERT | `match3d#468#rc_38` | CHANGED | CHANGED body only: adds 'and need to be in before the beta'. Path, review link, time, seq unchanged. Before #468 merge 16:13:50Z. ADV-22 |
| 49 | 158 | 158 | github.github_timeline_events | INSERT | `match3d#468#ev_6` | IDENTICAL | REUSED rev11 ledger #49 |
| 50 | 160 | 160 | slack.slack_messages | INSERT | `73bc730c620936feba3dcfbba00e2745` | IDENTICAL | REUSED rev11 ledger #50 |
| 51 | 162 | 162 | slack.slack_messages | UPDATE | `c2b9c90355cf8c2c4326ab19d3a24f79` | IDENTICAL | REUSED rev11 ledger #51 |
| 52 | 164 | 164 | github.github_review_comments | INSERT | `match3d#472#rc_1` | IDENTICAL | REUSED rev11 ledger #52 |
| 53 | 166 | 166 | slack.slack_messages | INSERT | `65564543e4bc8dd707a177aada2337a3` | IDENTICAL | REUSED rev11 ledger #53 |
| 54 | 168 | 168 | slack.slack_messages | UPDATE | `61f686b8a8b6c164b14aff6b5b1897bf` | IDENTICAL | REUSED rev11 ledger #54 |
| 55 | 170 | 170 | slack.slack_messages | INSERT | `78aa8ed77c0bd7b8a3fad227b22bc3fb` | CHANGED | CHANGED attachment text only: equals L157 body after unescape; attachment ts = comment second; lag 2.70 s; no other key or column changed |
| 56 | 172 | 172 | slack.slack_messages | UPDATE | `4b7c41278397b56b36e9b2f8a820c454` | IDENTICAL | REUSED rev11 ledger #56 |
| 57 | 177 | 177 | linear.linear_comments | INSERT | `cmt_zom429_1` | IDENTICAL | REUSED rev11 ledger #57 |
| 58 | 179 | 179 | linear.linear_comments | INSERT | `cmt_zom556_1` | IDENTICAL | REUSED rev11 ledger #58 |
| 59 | 180 | 180 | linear.linear_issues | UPDATE | `ZOM-556` | IDENTICAL | REUSED rev11 ledger #59 |
| 60 | 182 | 182 | linear.linear_comments | INSERT | `cmt_zom565_1` | IDENTICAL | REUSED rev11 ledger #60 |
| 61 | 183 | 183 | linear.linear_comments | INSERT | `cmt_zom565_2` | IDENTICAL | REUSED rev11 ledger #61 |
| 62 | 184 | 184 | linear.linear_issues | UPDATE | `ZOM-565` | IDENTICAL | REUSED rev11 ledger #62 |
| 63 | 186 | 186 | linear.linear_comments | INSERT | `cmt_zom543_1` | IDENTICAL | REUSED rev11 ledger #63 |
| 64 | 187 | 187 | linear.linear_issues | UPDATE | `ZOM-543` | IDENTICAL | REUSED rev11 ledger #64 |
| 65 | 189 | 189 | linear.linear_comments | INSERT | `cmt_zom526_1` | IDENTICAL | REUSED rev11 ledger #65 |
| 66 | 190 | 190 | linear.linear_comments | INSERT | `cmt_zom526_2` | IDENTICAL | REUSED rev11 ledger #66 |
| 67 | 191 | 191 | linear.linear_comments | INSERT | `cmt_zom526_3` | IDENTICAL | REUSED rev11 ledger #67 |
| 68 | 192 | 192 | linear.linear_issues | UPDATE | `ZOM-526` | IDENTICAL | REUSED rev11 ledger #68 |
| 69 | 194 | 194 | linear.linear_comments | INSERT | `cmt_zom552_1` | IDENTICAL | REUSED rev11 ledger #69 |
| 70 | 195 | 195 | linear.linear_issues | UPDATE | `ZOM-552` | IDENTICAL | REUSED rev11 ledger #70 |
| 71 | 197 | 197 | linear.linear_comments | INSERT | `cmt_zom534_1` | IDENTICAL | REUSED rev11 ledger #71 |
| 72 | 198 | 198 | linear.linear_comments | INSERT | `cmt_zom534_2` | IDENTICAL | REUSED rev11 ledger #72 |
| 73 | 199 | 199 | linear.linear_issues | UPDATE | `ZOM-534` | IDENTICAL | REUSED rev11 ledger #73 |
| 74 | 201 | 201 | linear.linear_comments | INSERT | `cmt_zom432_1` | IDENTICAL | REUSED rev11 ledger #74 |
| 75 | 202 | 202 | linear.linear_comments | INSERT | `cmt_zom432_2` | IDENTICAL | REUSED rev11 ledger #75 |
| 76 | 203 | 203 | linear.linear_issues | UPDATE | `ZOM-432` | IDENTICAL | REUSED rev11 ledger #76 |
| 77 | 205 | 205 | linear.linear_comments | INSERT | `cmt_zom78_1` | IDENTICAL | REUSED rev11 ledger #77 |
| 78 | 206 | 206 | linear.linear_issues | UPDATE | `ZOM-78` | IDENTICAL | REUSED rev11 ledger #78 |
| 79 | 208 | 208 | linear.linear_comments | INSERT | `cmt_zom465_1` | IDENTICAL | REUSED rev11 ledger #79 |
| 80 | 209 | 209 | linear.linear_comments | INSERT | `cmt_zom465_2` | IDENTICAL | REUSED rev11 ledger #80 |
| 81 | 210 | 210 | linear.linear_comments | INSERT | `cmt_zom465_3` | CHANGED | CHANGED body only: 'was ticked before that event merged'. Calvin updated the master ticket 09-17, #468 merged 09-29. Closes ADV-17. ADV-20, ADV-22 |
| 82 | 211 | 211 | linear.linear_issues | UPDATE | `ZOM-465` | IDENTICAL | REUSED rev11 ledger #82 |
| 83 | 213 | 213 | linear.linear_comments | INSERT | `cmt_zom344_1` | IDENTICAL | REUSED rev11 ledger #83 |
| 84 | 214 | 214 | linear.linear_issues | UPDATE | `ZOM-344` | IDENTICAL | REUSED rev11 ledger #84 |
| 85 | 216 | 216 | linear.linear_comments | INSERT | `cmt_zom442_1` | IDENTICAL | REUSED rev11 ledger #85 |
| 86 | 217 | 217 | linear.linear_issues | UPDATE | `ZOM-442` | IDENTICAL | REUSED rev11 ledger #86 |
| 87 | 219 | 219 | linear.linear_comments | INSERT | `cmt_zom471_1` | IDENTICAL | REUSED rev11 ledger #87 |
| 88 | 220 | 220 | linear.linear_issues | UPDATE | `ZOM-471` | IDENTICAL | REUSED rev11 ledger #88 |
| 89 | 222 | 222 | linear.linear_comments | INSERT | `cmt_zom504_1` | IDENTICAL | REUSED rev11 ledger #89 |
| 90 | 223 | 223 | linear.linear_issues | UPDATE | `ZOM-504` | IDENTICAL | REUSED rev11 ledger #90 |
| 91 | 225 | 225 | linear.linear_comments | INSERT | `cmt_zom517_1` | IDENTICAL | REUSED rev11 ledger #91 |
| 92 | 226 | 226 | linear.linear_issues | UPDATE | `ZOM-517` | IDENTICAL | REUSED rev11 ledger #92 |
| 93 | 228 | 228 | linear.linear_comments | INSERT | `cmt_zom521_1` | IDENTICAL | REUSED rev11 ledger #93 |
| 94 | 229 | 229 | linear.linear_comments | INSERT | `cmt_zom521_2` | IDENTICAL | REUSED rev11 ledger #94 |
| 95 | 230 | 230 | linear.linear_issues | UPDATE | `ZOM-521` | IDENTICAL | REUSED rev11 ledger #95 |
| 96 | 239 | 239 | linear.linear_comments | INSERT | `cmt_zom542_1` | IDENTICAL | REUSED rev11 ledger #96 |
| 97 | 240 | 240 | linear.linear_issues | UPDATE | `ZOM-542` | IDENTICAL | REUSED rev11 ledger #97 |
| 98 | 242 | 242 | linear.linear_comments | INSERT | `cmt_zom544_1` | IDENTICAL | REUSED rev11 ledger #98 |
| 99 | 243 | 243 | linear.linear_issues | UPDATE | `ZOM-544` | IDENTICAL | REUSED rev11 ledger #99 |
| 100 | 245 | 245 | linear.linear_comments | INSERT | `cmt_zom546_1` | IDENTICAL | REUSED rev11 ledger #100 |
| 101 | 246 | 246 | linear.linear_issues | UPDATE | `ZOM-546` | IDENTICAL | REUSED rev11 ledger #101 |
| 102 | 248 | 248 | linear.linear_comments | INSERT | `cmt_zom549_1` | IDENTICAL | REUSED rev11 ledger #102 |
| 103 | 249 | 249 | linear.linear_issues | UPDATE | `ZOM-549` | IDENTICAL | REUSED rev11 ledger #103 |
| 104 | 251 | 251 | linear.linear_comments | INSERT | `cmt_zom566_1` | IDENTICAL | REUSED rev11 ledger #104 |
| 105 | 252 | 252 | linear.linear_comments | INSERT | `cmt_zom566_2` | IDENTICAL | REUSED rev11 ledger #105 |
| 106 | 253 | 253 | linear.linear_issues | UPDATE | `ZOM-566` | IDENTICAL | REUSED rev11 ledger #106 |
| 107 | 255 | 255 | linear.linear_comments | INSERT | `cmt_zom563_1` | CHANGED | CHANGED author, body, stamps; same id, sequence 1. Douglas = assignee; 18:17:05Z is 32 s after his 18:16:33Z DM and after started_at 18:14:25Z; Oct 8 matches L98. Closes ADV-1 |
| 108 | 256 | — | linear.linear_comments | INSERT | `cmt_zom563_2` | NEW | NEW. Id free; Vincent = creator; sequence 2; 22:04:33Z after his 21:58:44Z DM; body byte-equal to rev11 L255; equals L257 updated_at and completed_at |
| 109 | 257 | 256 | linear.linear_issues | UPDATE | `ZOM-563` | IDENTICAL | REUSED rev11 ledger #108 |
| 110 | 259 | 258 | trello.trello_actions | INSERT | `68dac8204f1e9a3b7c2d5e61` | CHANGED | CHANGED data_json: restores idCard and textData, list still absent. Valid JSON; kept values equal rev11; idCard equals column and card.id. ADV-18 |
| 111 | 261 | 260 | trello.trello_cards | UPDATE | `68c452a03006277f55d9dc96` | IDENTICAL | REUSED rev11 ledger #110 |

## 12. Stage evidence record

**Reused:** per-record source facts for the 104 byte-identical statements from `review_rev11/out/0_injection.md` (sha256 `a069bf09d0684c98342b0416a2d99c59754852dbf8de08ee7f415a9adb4dcc12`) and, through it, `review_rev10/out/0_injection.md` (sha256 `67e1ab6fe77bf78e8f7010487272ed2a2ddf056f4a54d5ade27b6c486ecc7e0a`). Slack and Gmail collision coverage is also reused, because no key changed and the manifest fingerprints match. Verified unchanged: statement bytes, source and reference fingerprints, the clock, git heads.

**Not reused, rerun on the full rev12 SQL:** lint, JSON validity, date checks, Linear order and `updated_at`, Slack thread rollups, mirror equality, heading offsets, and record checks on Linear, GitHub review comments and Trello actions.

Intended `input_manifest.json` injection entry (not written, per the setup):

```json
{"review_version":"injection-static-v2","evidence_contract":"stage-evidence-v1","reused_evidence":[{"source_report":"review_rev11/out/0_injection.md","sha256":"a069bf09d0684c98342b0416a2d99c59754852dbf8de08ee7f415a9adb4dcc12","scope":"per-record source facts for 104 byte-identical statements; Slack and Gmail collision coverage","verified_unchanged":"statement bytes; source and reference fingerprints; Slack and Gmail manifests; clock; git heads"}],"sql_sha256":"b5ccbfa577fc9f2c8f6eb3098f8d62a16623d799f41d11285de8227f1bed60d3","universe":"synthcut"}
```

Any SQL change, including an advisory fix, invalidates the affected rows. Task discoverability, persona reach and Unique Ground Truth stay with `/prompt`.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (level not reported by the runtime)

Next action: Proceed to /prompt. Before that, consider ADV-2 (one sentence on L213), ADV-22 (one phrase on L157, L170 and L210) and ADV-18 (add `list` on L259). Any SQL edit needs a rerun of the affected rows.

Evidence limits: No required static check is unresolved. Outside this static scope: live execution and deployment; current database compatibility (the snapshot is unverified, 12 used columns are NOT COVERED, and the live schema file in the SQL header was not opened by instruction); search ranking and Agent visibility. Two facts cannot be confirmed from the export: L255's statement that the Sep 30 update carried only the teams and social changes (git shows no deploy content), and whether `state_history_json` needs updating for the five state changes (ZOM-344, ZOM-432, ZOM-542, ZOM-563, ZOM-566). Sprites are Git LFS pointers, so art claims were checked by file change, not by eye. The report is saved in the review folder, not through `hg_write_output.py`, as the setup requires.
