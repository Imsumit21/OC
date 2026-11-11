# Injection Data-Integrity Report (Eval 0), delta review of rev13

**Review version:** `injection-static-v2`
**Evidence contract:** `stage-evidence-v1`
**Reused evidence:** the rev12 report (section 12). Everything on changed statements is NEW.

## 1. Scope and provenance

| Item | Value |
|---|---|
| Review | Independent `/injection` delta review, chat/attachment mode, audit only |
| Actual review time | 2026-11-06 (machine date; not the task clock) |
| Universe | Oct 1, 2025 (synth-cut), `hg4-synth-sep30cut` v16 |
| Fixed clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| SQL under review | `R13/inputs/01_Universe_Inject.sql`, sha256 `1f2175a297fd390960f22c3767f790fc980a881023affa6ece970745fb40289b`, 265 lines, 111 statements |
| Previous SQL | `R13/prev/01_Universe_Inject.rev12.sql`, sha256 `b5ccbfa577fc9f2c8f6eb3098f8d62a16623d799f41d11285de8227f1bed60d3`, 111 statements |
| Previous report | rev12 `review_rev12/out/0_injection.md`, sha256 `e8d4467af5f090f7794f718dd7f0ba552c609dcc18037f67427d107b5e8aa47a` (hash rechecked). It reuses rev11 `a069bf09d0684c98342b0416a2d99c59754852dbf8de08ee7f415a9adb4dcc12` and rev10 `67e1ab6fe77bf78e8f7010487272ed2a2ddf056f4a54d5ade27b6c486ecc7e0a` |
| Universe manifest | sha256 prefix `da2f4cf0dcf71025` |
| Repository state | `match3d` `0ff577550e`, `match3d-backend` `a0e4a21`, `match3d-quests` `d8ca05a` |

R13 = `/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review_rev13`.

**Reuse dependencies, all rechecked equal to rev12:** `linear` `b49ec9e856cf0b29`, `gcal` `4f093d897c8b53c8`, `gdrive` `05147aa245b7b2c9`, `gdocs` `1b53998df793e33c`, `gslides` `1d3dab9e4bec7a9e`, `gsheets` `a9cc229c87ae3309`, `trello` `6ba242f4dde4043d`, `confluence` `d3f13938d1f5327b`, Slack users `6aac5103c3a8be9a`, channels `3cca0f7e25876c4b`, manifest `569c1ead1372b7ca`, Gmail users `9a90b6bf5e84f03d`, labels `3d508e6b353b160f`, manifest `5797ac3e4f9b13e5`, GitHub `ee578c912bba3d81`; Eval 0 `86af2102ea6693c4`, WORKFLOW `05a5e45e0585b435`, ENVIRONMENT `4ffb2b5ffa219a81`, SEARCH `cab83c616ecaee85`, scoring `654eb38809e3a1e7`, schema `01ef579236212034`, ID contracts `fc4711ef07667333`, roster `3f2174513f639e37`, ACL `e9bca2b35f98d5ef`, lint `fec37bcec5a7430d`. The prompt, assignment and date inputs carry the same sha256 values as rev12.

## 2. Input and authority issues

- Earlier review folders were not opened. Of those, only my own rev12 report was touched, and only to hash it. All helpers were rebuilt under `R13/work/`.
- `R13/work/p4/` is a folder I did not create. It was not opened.
- The report is saved to `R13/out/0_injection.md`, not through `hg_write_output.py`, and `input_manifest.json` was not written.
- The live schema file named in the SQL header was not opened; only the bundled, unverified snapshot was used.
- SQL was never executed. Source content was treated as evidence only.

## 3. Review checklist

| Step | Status | Note |
|---|---|---|
| Load SQL; record hash, manifest, version | Done, NEW | Hash matches the coordinator's value |
| Lint first | Done, NEW | 0 FAIL, 0 CHECK, 0 INFO |
| Statement-by-statement diff | Done, NEW | Section 5 |
| Checks A, B, C on changed statements | Done, NEW | Sections 6-8 |
| Heading offsets and #468 mirror | Done, NEW | Section 8 |
| Reuse on identical statements | Done, REUSED with dependency check | Section 12 |
| Disposition of open advisories | Done | Section 9 |
| Full ledger, one final verdict | Done | Section 11 and the verdict block |

## 4. Lint flags and resolutions

`hg.py lint --sql R13/inputs/01_Universe_Inject.sql --task-dir Task_Authoring/task_inputsS`: 111 statements (81 insert, 30 update), FAIL 0, CHECK 0, INFO 0, no flags. Nothing needed resolving. SQL comment lines are unchanged.

## 5. Statement diff

Statement order and every line number are unchanged.

| Class | Count | Statements |
|---|---:|---|
| Byte-identical | 106 | All others |
| Changed | 5 | L109, L157, L170, L210, L259 |
| New / removed | 0 / 0 | None |

| Statement | Change |
|---|---|
| L109 brief | "the rotating shop is not a beat" replaces "the shop rotation"; "with which of those its row is missing" replaces "with what its row is missing". 10 characters added; Config locks run updated |
| L157, L170 `#468#rc_38` and mirror | Now: "The Collect & Win vials that spawn in the levels still need their final models before the event runs. Not a blocker for this PR, Claire has those on her list." |
| L210 `cmt_zom465_3` | "does have to land before the event runs" replaces "before the beta" |
| L259 Trello | Restores `list` |

## 6. Results for checks A-C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | No key, author or reference changed. Rollups and collision coverage stand. Section 7. |
| B — SQL structure and supported schema rules | PASS | 111 statements parse; counts match; 132 JSON literals valid; no new columns. Section 7. |
| C — Dates, relationships and consistency | PASS | No future event dates; 9 heading runs exact; all three mirrors equal their bodies; each changed claim is consistent with base. No demonstrated contradiction. Section 8. |

## 7. Checks A and B

**Check A.** The five changed statements keep their ids, authors, parents, review links and timestamps; only text, style runs or `data_json` differ. L259's new `list.id` is `6851a674975da1fe76e70d93`, the card's own `idList`. Collision coverage, actor resolution and thread rollups are REUSED: no key changed, no `ts` changed, the parent UPDATEs are byte-identical, and all fingerprints match rev12.

**Check B.** 111 statements parse; column and value counts equal on all 81 inserts; no upsert, expression or cast. 132 JSON literals parse. Linear order and `updated_at` were recomputed for all 32 comments and 21 UPDATEs: no fault. Generated columns untouched. No required column omitted. Snapshot: no new columns; the same 12 remain NOT COVERED (ADV-13).

## 8. Check C: dates, relationships and consistency

**Dates.** The only values after the clock are the eight Oct 8 `start_ts` and `end_ts` plan fields. The latest event is L17 at 2025-09-30T22:10:41Z.

### 8.1 Heading offsets (L109)

Body is 3,100 characters, LF only. Each run was recomputed; each sits on the exact heading text, with a line break on both sides, and each heading occurs once.

| Style | Text | rev12 | rev13 |
|---|---|---|---|
| TITLE | ZM3D beta live-ops calendar - working rules | 0-43 | 0-43 |
| HEADING_2 | Span and time base | 163-181 | 163-181 |
| HEADING_2 | Scope | 606-611 | 606-611 |
| HEADING_2 | When a beat starts | 794-812 | 794-812 |
| HEADING_2 | Held or not | 1318-1329 | 1318-1329 |
| HEADING_2 | One-offs | 1956-1964 | 1956-1964 |
| HEADING_2 | Still to do | 2164-2175 | 2164-2175 |
| HEADING_2 | Push copy | 2481-2490 | 2481-2490 |
| HEADING_2 | Config locks | 2863-2875 | 2873-2885 |

Only Config locks moves, because the one length change (+10) falls in Push copy; the "rotating shop" swap keeps the same length. "Rotating shop" is the base term (Confluence "The daily rotating shop", Slack from July). "Which of those" refers to the listed conditions in the same paragraph.

### 8.2 #468 mirror against its GitHub body

- Body (L157): "The Collect & Win vials that spawn in the levels still need their final models before the event runs. Not a blocker for this PR, Claire has those on her list."
- Mirror (L170): identical after unescaping `&amp;`.
- Attachment `ts` equals the comment's second (09-29 15:36:41Z); lag 2.70 s.
- `text` is the only attachment key that changed and `attachments_json` the only row column. `body` is the only L157 column that changed.
- The #470 and #472 mirrors still equal their bodies.

Facts in the new wording hold. The repo has only `Collect&Win Item Potion` prefabs and no later vial commit by the clock. "Not a blocker for this PR" fits the `COMMENTED` review state and the merge 37 minutes later, and it keeps this note clear of the brief's change-request clause.

### 8.3 Other changed statements

- **L210.** "the event" is Collect & Win, named earlier in the sentence. The rest is unchanged from rev12.
- **L259.** Keys and order are now `board, card, idCard, list, text, textData`, an exact match for 14 of 56 base commentCard rows and 11 of 12 on this board; the twelfth only adds `dateLastEdited`. `idCard` equals the column and `card.id`. "BETA: Sep 30" matches 63 base actions on this list (SC-13). Kept values are equal to rev12, and L261 stays correct.
- **Remaining "before the beta" text.** Three Linear comments (L183 `cmt_zom565_2`, L190 `cmt_zom526_2`, L251 `cmt_zom566_1`) use it, all in the negative: "do not have to land before the beta". None sets a requirement, so the build-timing question doesn't arise.

## 9. What happened to each open advisory

Open after rev12: ADV-2, 3, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22. ADV-1, 4, 5, 6, 11 and 17 closed earlier and stay closed.

| ADV | Subject | rev13 status | Current marking |
|---|---|---|---|
| 2 | ZOM-344 close vs chest timing | **Open, unchanged.** L213 and L214 byte-identical | CSC |
| 3 | Premium strip wording | Open, unchanged | Cosmetic |
| 7 | `#468#ev_6` order | Open, unchanged | Cosmetic |
| 8 | `revision_id` pattern | Open, unchanged | Cosmetic |
| 9 | #468 Reviewers edit | Open, unchanged | Cosmetic |
| 10 | Daily Gift frame not confirmed by eye | Open, unchanged | Cosmetic |
| 12 | Change-request clause has no record | Open, unchanged; L157's "Not a blocker" keeps it clear of that note | Cosmetic |
| 13 | 12 columns NOT COVERED | Open, unchanged | Cosmetic |
| 14 | Julia not listed in #zombie-prs | Open, unchanged | Cosmetic |
| 15 | Sheet has NULL `content_path` | Open, unchanged | Cosmetic |
| 16 | Gmail LF and short headers | Open, unchanged | Cosmetic |
| 18 | Trello payload shape | **Closed.** `list` restored; shape matches base | None |
| 19 | #zm-collect-win archived flag, Julia not listed | Open, unchanged | Cosmetic |
| 20 | "Event icon" is a widget | Open, unchanged | Cosmetic |
| 21 | 23:59 close vs 00:00 cron | Open, unchanged | Cosmetic |
| 22 | "Before the beta" vs submitted builds | **Closed.** L157, L170 and L210 now say "before the event runs" | None |

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
- **ADV-19.** L35 sits in `#zm-collect-win`: `is_archived: true` (SC-57) and Julia is not a listed member. Brian's ask is in the same public channel, so whoever can read the ask can read the reply.
- **ADV-20.** "Event icon" at L209 and L210 is really a progress-bar widget with a bottle icon. The claim holds in substance.
- **ADV-21.** L109 says windows close 23:59 UTC; the cron resets at 00:00 the next day (`0 0 * * 3`). This follows the brief's own "Sun Nov 2 23:59 UTC" convention.

## 11. Full operation ledger

Operation order as in rev13; line numbers equal rev12. IDENTICAL rows point at the rev12 report's ledger, which carries earlier source pointers forward.

| # | Line | Table | Op | Record / target | Status | Result |
|---|---|---|---|---|---|---|
| 1 | 11 | slack.slack_messages | INSERT | `bca784379e7dbca9e64e79a64dfefbba` | IDENTICAL | REUSED rev12 ledger #1 |
| 2 | 13 | slack.slack_messages | INSERT | `890dc27f56e8501bd7590ffdfc231057` | IDENTICAL | REUSED rev12 ledger #2 |
| 3 | 15 | slack.slack_messages | INSERT | `933cee9f6464a80e4b1f05259b595b20` | IDENTICAL | REUSED rev12 ledger #3 |
| 4 | 17 | slack.slack_messages | INSERT | `669d15f685f158633e56302160957f1e` | IDENTICAL | REUSED rev12 ledger #4 |
| 5 | 19 | slack.slack_messages | INSERT | `b5f2955c2e154efc6835946ecfe1758e` | IDENTICAL | REUSED rev12 ledger #5 |
| 6 | 21 | slack.slack_messages | UPDATE | `9025d428af1f551a20e303c3acbc545b` | IDENTICAL | REUSED rev12 ledger #6 |
| 7 | 23 | slack.slack_messages | INSERT | `e343557b2e94a1701251ebd079e6f0ce` | IDENTICAL | REUSED rev12 ledger #7 |
| 8 | 25 | slack.slack_messages | UPDATE | `ede90bc6ec6cb16fd97663f2888f39a2` | IDENTICAL | REUSED rev12 ledger #8 |
| 9 | 27 | slack.slack_messages | INSERT | `a08ff7cbfc52008d7dee8457e9385a3c` | IDENTICAL | REUSED rev12 ledger #9 |
| 10 | 29 | slack.slack_messages | UPDATE | `d0dd5d3ad4658add1f79802e2aa60e48` | IDENTICAL | REUSED rev12 ledger #10 |
| 11 | 31 | slack.slack_messages | INSERT | `532747cb5d123a95d13204e57b5a7a38` | IDENTICAL | REUSED rev12 ledger #11 |
| 12 | 33 | slack.slack_messages | UPDATE | `a3e78e820b9f880ef4e3d941562110df` | IDENTICAL | REUSED rev12 ledger #12 |
| 13 | 35 | slack.slack_messages | INSERT | `7d70c7753179c98b6c8b2b5457a1e5e7` | IDENTICAL | REUSED rev12 ledger #13 |
| 14 | 37 | slack.slack_messages | UPDATE | `0069f6143e89802993b39e442d3baeb2` | IDENTICAL | REUSED rev12 ledger #14 |
| 15 | 39 | gmail.gmail_threads | INSERT | `brian.foster@harmonygames.co/1843954828968110017` | IDENTICAL | REUSED rev12 ledger #15 |
| 16 | 40 | gmail.gmail_messages | INSERT | `brian.foster/<CAPT--p4sBC8XnaA7qB…` | IDENTICAL | REUSED rev12 ledger #16 |
| 17 | 50 | gmail.gmail_threads | INSERT | `julia.lawson@harmonygames.co/1843954828968533812` | IDENTICAL | REUSED rev12 ledger #17 |
| 18 | 51 | gmail.gmail_messages | INSERT | `julia.lawson/<CAPT--p4sBC8XnaA7qB…` | IDENTICAL | REUSED rev12 ledger #18 |
| 19 | 61 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843954828968789474` | IDENTICAL | REUSED rev12 ledger #19 |
| 20 | 62 | gmail.gmail_messages | INSERT | `frederick.stone/<CAPT--p4sBC8XnaA7qB…` | IDENTICAL | REUSED rev12 ledger #20 |
| 21 | 72 | gmail.gmail_threads | INSERT | `brian.foster@harmonygames.co/1844311412965607905` | IDENTICAL | REUSED rev12 ledger #21 |
| 22 | 73 | gmail.gmail_messages | INSERT | `brian.foster/<CAPT--p4a5fY9wd6vr+…` | IDENTICAL | REUSED rev12 ledger #22 |
| 23 | 81 | gmail.gmail_threads | INSERT | `julia.lawson@harmonygames.co/1844311412966040123` | IDENTICAL | REUSED rev12 ledger #23 |
| 24 | 82 | gmail.gmail_messages | INSERT | `julia.lawson/<CAPT--p4a5fY9wd6vr+…` | IDENTICAL | REUSED rev12 ledger #24 |
| 25 | 90 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844311412966288046` | IDENTICAL | REUSED rev12 ledger #25 |
| 26 | 90 | gmail.gmail_messages | INSERT | `frederick.stone/<CAPT--p4a5fY9wd6vr+…` | IDENTICAL | REUSED rev12 ledger #26 |
| 27 | 98 | gcal.gcal_events | INSERT | `evt_9a4c2e7f1b3d58e06c7a2f` | IDENTICAL | REUSED rev12 ledger #27 |
| 28 | 100 | gcal.gcal_events | INSERT | `evt_5c1e83a7d94b02f6c8e31a` | IDENTICAL | REUSED rev12 ledger #28 |
| 29 | 102 | gcal.gcal_events | INSERT | `evt_a72f4d9e0c1b58d3e6f40b` | IDENTICAL | REUSED rev12 ledger #29 |
| 30 | 104 | gcal.gcal_events | INSERT | `evt_1d6b9a03e5c27f84b0d92c` | IDENTICAL | REUSED rev12 ledger #30 |
| 31 | 106 | gdrive.drive_files | INSERT | `d_5f2c8e1b7a94d03c6e2b58` | IDENTICAL | REUSED rev12 ledger #31 |
| 32 | 108 | gdrive.drive_files | INSERT | `f_7c3e91a4d2b85f60e1a9c4` | IDENTICAL | REUSED rev12 ledger #32 |
| 33 | 109 | gdocs.docs_documents | INSERT | `f_7c3e91a4d2b85f60e1a9c4` | CHANGED | CHANGED body and style runs: 2 wordings, 10 chars added; only the Config locks run moves. All 9 runs recomputed exact. 'Rotating shop' is the base term. ADV-21 |
| 34 | 129 | gdrive.drive_files | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | IDENTICAL | REUSED rev12 ledger #34 |
| 35 | 130 | gslides.slides_presentations | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | IDENTICAL | REUSED rev12 ledger #35 |
| 36 | 131 | gslides.slides_pages | INSERT | `slide_6f2a9d14c7e0` | IDENTICAL | REUSED rev12 ledger #36 |
| 37 | 132 | gslides.slides_page_elements | INSERT | `el_9d1c74b0a26e` | IDENTICAL | REUSED rev12 ledger #37 |
| 38 | 135 | gslides.slides_pages | INSERT | `slide_b83e51a09d72` | IDENTICAL | REUSED rev12 ledger #38 |
| 39 | 136 | gslides.slides_page_elements | INSERT | `el_5e83a1f4c092` | IDENTICAL | REUSED rev12 ledger #39 |
| 40 | 142 | gslides.slides_pages | INSERT | `slide_0c47d2e81b6f` | IDENTICAL | REUSED rev12 ledger #40 |
| 41 | 143 | gslides.slides_page_elements | INSERT | `el_c07b2e9d3148` | IDENTICAL | REUSED rev12 ledger #41 |
| 42 | 146 | gdrive.drive_files | INSERT | `f_e4a17c90b3d25f6a8c1d73` | IDENTICAL | REUSED rev12 ledger #42 |
| 43 | 147 | gsheets.sheets_spreadsheets | INSERT | `f_e4a17c90b3d25f6a8c1d73` | IDENTICAL | REUSED rev12 ledger #43 |
| 44 | 148 | gsheets.sheets_sheets | INSERT | `sheet 0 Calendar` | IDENTICAL | REUSED rev12 ledger #44 |
| 45 | 149 | gsheets.sheets_sheets | INSERT | `sheet 1 Pushes` | IDENTICAL | REUSED rev12 ledger #45 |
| 46 | 154 | github.github_review_comments | INSERT | `match3d#470#rc_10` | IDENTICAL | REUSED rev12 ledger #46 |
| 47 | 156 | github.github_reviews | INSERT | `match3d#468#rev_3` | IDENTICAL | REUSED rev12 ledger #47 |
| 48 | 157 | github.github_review_comments | INSERT | `match3d#468#rc_38` | CHANGED | CHANGED body only. Path, review link, time, seq unchanged; `Collect&Win Item Potion` prefabs are the only vial models in repo; before #468 merge 16:13:50Z; state COMMENTED fits 'Not a blocker'. Closes ADV-22 |
| 49 | 158 | github.github_timeline_events | INSERT | `match3d#468#ev_6` | IDENTICAL | REUSED rev12 ledger #49 |
| 50 | 160 | slack.slack_messages | INSERT | `73bc730c620936feba3dcfbba00e2745` | IDENTICAL | REUSED rev12 ledger #50 |
| 51 | 162 | slack.slack_messages | UPDATE | `c2b9c90355cf8c2c4326ab19d3a24f79` | IDENTICAL | REUSED rev12 ledger #51 |
| 52 | 164 | github.github_review_comments | INSERT | `match3d#472#rc_1` | IDENTICAL | REUSED rev12 ledger #52 |
| 53 | 166 | slack.slack_messages | INSERT | `65564543e4bc8dd707a177aada2337a3` | IDENTICAL | REUSED rev12 ledger #53 |
| 54 | 168 | slack.slack_messages | UPDATE | `61f686b8a8b6c164b14aff6b5b1897bf` | IDENTICAL | REUSED rev12 ledger #54 |
| 55 | 170 | slack.slack_messages | INSERT | `78aa8ed77c0bd7b8a3fad227b22bc3fb` | CHANGED | CHANGED attachment text only: equals L157 body after unescape; attachment ts = comment second; lag 2.70 s; no other key or column changed |
| 56 | 172 | slack.slack_messages | UPDATE | `4b7c41278397b56b36e9b2f8a820c454` | IDENTICAL | REUSED rev12 ledger #56 |
| 57 | 177 | linear.linear_comments | INSERT | `cmt_zom429_1` | IDENTICAL | REUSED rev12 ledger #57 |
| 58 | 179 | linear.linear_comments | INSERT | `cmt_zom556_1` | IDENTICAL | REUSED rev12 ledger #58 |
| 59 | 180 | linear.linear_issues | UPDATE | `ZOM-556` | IDENTICAL | REUSED rev12 ledger #59 |
| 60 | 182 | linear.linear_comments | INSERT | `cmt_zom565_1` | IDENTICAL | REUSED rev12 ledger #60 |
| 61 | 183 | linear.linear_comments | INSERT | `cmt_zom565_2` | IDENTICAL | REUSED rev12 ledger #61 |
| 62 | 184 | linear.linear_issues | UPDATE | `ZOM-565` | IDENTICAL | REUSED rev12 ledger #62 |
| 63 | 186 | linear.linear_comments | INSERT | `cmt_zom543_1` | IDENTICAL | REUSED rev12 ledger #63 |
| 64 | 187 | linear.linear_issues | UPDATE | `ZOM-543` | IDENTICAL | REUSED rev12 ledger #64 |
| 65 | 189 | linear.linear_comments | INSERT | `cmt_zom526_1` | IDENTICAL | REUSED rev12 ledger #65 |
| 66 | 190 | linear.linear_comments | INSERT | `cmt_zom526_2` | IDENTICAL | REUSED rev12 ledger #66 |
| 67 | 191 | linear.linear_comments | INSERT | `cmt_zom526_3` | IDENTICAL | REUSED rev12 ledger #67 |
| 68 | 192 | linear.linear_issues | UPDATE | `ZOM-526` | IDENTICAL | REUSED rev12 ledger #68 |
| 69 | 194 | linear.linear_comments | INSERT | `cmt_zom552_1` | IDENTICAL | REUSED rev12 ledger #69 |
| 70 | 195 | linear.linear_issues | UPDATE | `ZOM-552` | IDENTICAL | REUSED rev12 ledger #70 |
| 71 | 197 | linear.linear_comments | INSERT | `cmt_zom534_1` | IDENTICAL | REUSED rev12 ledger #71 |
| 72 | 198 | linear.linear_comments | INSERT | `cmt_zom534_2` | IDENTICAL | REUSED rev12 ledger #72 |
| 73 | 199 | linear.linear_issues | UPDATE | `ZOM-534` | IDENTICAL | REUSED rev12 ledger #73 |
| 74 | 201 | linear.linear_comments | INSERT | `cmt_zom432_1` | IDENTICAL | REUSED rev12 ledger #74 |
| 75 | 202 | linear.linear_comments | INSERT | `cmt_zom432_2` | IDENTICAL | REUSED rev12 ledger #75 |
| 76 | 203 | linear.linear_issues | UPDATE | `ZOM-432` | IDENTICAL | REUSED rev12 ledger #76 |
| 77 | 205 | linear.linear_comments | INSERT | `cmt_zom78_1` | IDENTICAL | REUSED rev12 ledger #77 |
| 78 | 206 | linear.linear_issues | UPDATE | `ZOM-78` | IDENTICAL | REUSED rev12 ledger #78 |
| 79 | 208 | linear.linear_comments | INSERT | `cmt_zom465_1` | IDENTICAL | REUSED rev12 ledger #79 |
| 80 | 209 | linear.linear_comments | INSERT | `cmt_zom465_2` | IDENTICAL | REUSED rev12 ledger #80 |
| 81 | 210 | linear.linear_comments | INSERT | `cmt_zom465_3` | CHANGED | CHANGED body only: 'before the event runs'. Time, author, sequence unchanged. Closes ADV-22. ADV-20 |
| 82 | 211 | linear.linear_issues | UPDATE | `ZOM-465` | IDENTICAL | REUSED rev12 ledger #82 |
| 83 | 213 | linear.linear_comments | INSERT | `cmt_zom344_1` | IDENTICAL | REUSED rev12 ledger #83 |
| 84 | 214 | linear.linear_issues | UPDATE | `ZOM-344` | IDENTICAL | REUSED rev12 ledger #84 |
| 85 | 216 | linear.linear_comments | INSERT | `cmt_zom442_1` | IDENTICAL | REUSED rev12 ledger #85 |
| 86 | 217 | linear.linear_issues | UPDATE | `ZOM-442` | IDENTICAL | REUSED rev12 ledger #86 |
| 87 | 219 | linear.linear_comments | INSERT | `cmt_zom471_1` | IDENTICAL | REUSED rev12 ledger #87 |
| 88 | 220 | linear.linear_issues | UPDATE | `ZOM-471` | IDENTICAL | REUSED rev12 ledger #88 |
| 89 | 222 | linear.linear_comments | INSERT | `cmt_zom504_1` | IDENTICAL | REUSED rev12 ledger #89 |
| 90 | 223 | linear.linear_issues | UPDATE | `ZOM-504` | IDENTICAL | REUSED rev12 ledger #90 |
| 91 | 225 | linear.linear_comments | INSERT | `cmt_zom517_1` | IDENTICAL | REUSED rev12 ledger #91 |
| 92 | 226 | linear.linear_issues | UPDATE | `ZOM-517` | IDENTICAL | REUSED rev12 ledger #92 |
| 93 | 228 | linear.linear_comments | INSERT | `cmt_zom521_1` | IDENTICAL | REUSED rev12 ledger #93 |
| 94 | 229 | linear.linear_comments | INSERT | `cmt_zom521_2` | IDENTICAL | REUSED rev12 ledger #94 |
| 95 | 230 | linear.linear_issues | UPDATE | `ZOM-521` | IDENTICAL | REUSED rev12 ledger #95 |
| 96 | 239 | linear.linear_comments | INSERT | `cmt_zom542_1` | IDENTICAL | REUSED rev12 ledger #96 |
| 97 | 240 | linear.linear_issues | UPDATE | `ZOM-542` | IDENTICAL | REUSED rev12 ledger #97 |
| 98 | 242 | linear.linear_comments | INSERT | `cmt_zom544_1` | IDENTICAL | REUSED rev12 ledger #98 |
| 99 | 243 | linear.linear_issues | UPDATE | `ZOM-544` | IDENTICAL | REUSED rev12 ledger #99 |
| 100 | 245 | linear.linear_comments | INSERT | `cmt_zom546_1` | IDENTICAL | REUSED rev12 ledger #100 |
| 101 | 246 | linear.linear_issues | UPDATE | `ZOM-546` | IDENTICAL | REUSED rev12 ledger #101 |
| 102 | 248 | linear.linear_comments | INSERT | `cmt_zom549_1` | IDENTICAL | REUSED rev12 ledger #102 |
| 103 | 249 | linear.linear_issues | UPDATE | `ZOM-549` | IDENTICAL | REUSED rev12 ledger #103 |
| 104 | 251 | linear.linear_comments | INSERT | `cmt_zom566_1` | IDENTICAL | REUSED rev12 ledger #104 |
| 105 | 252 | linear.linear_comments | INSERT | `cmt_zom566_2` | IDENTICAL | REUSED rev12 ledger #105 |
| 106 | 253 | linear.linear_issues | UPDATE | `ZOM-566` | IDENTICAL | REUSED rev12 ledger #106 |
| 107 | 255 | linear.linear_comments | INSERT | `cmt_zom563_1` | IDENTICAL | REUSED rev12 ledger #107 |
| 108 | 256 | linear.linear_comments | INSERT | `cmt_zom563_2` | IDENTICAL | REUSED rev12 ledger #108 |
| 109 | 257 | linear.linear_issues | UPDATE | `ZOM-563` | IDENTICAL | REUSED rev12 ledger #109 |
| 110 | 259 | trello.trello_actions | INSERT | `68dac8204f1e9a3b7c2d5e61` | CHANGED | CHANGED data_json: restores list. Key set and order equal 14 of 56 base rows, 11 of 12 on this board; list id = card idList; name in 63 base actions. Closes ADV-18 |
| 111 | 261 | trello.trello_cards | UPDATE | `68c452a03006277f55d9dc96` | IDENTICAL | REUSED rev12 ledger #111 |

## 12. Stage evidence record

**Reused:** per-record source facts for the 106 byte-identical statements from `review_rev12/out/0_injection.md` (sha256 `e8d4467af5f090f7794f718dd7f0ba552c609dcc18037f67427d107b5e8aa47a`) and, through it, the rev11 and rev10 reports. Also reused because no key or `ts` changed and fingerprints match: collision coverage, actor resolution and Slack thread rollups. Verified unchanged: statement bytes, source and reference fingerprints, the clock, git heads.

**Not reused, rerun on the full rev13 SQL:** lint, JSON validity, date checks, Linear order and `updated_at`, mirror equality, heading offsets, Trello shape.

Intended `input_manifest.json` injection entry (not written, per the setup):

```json
{"review_version":"injection-static-v2","evidence_contract":"stage-evidence-v1","reused_evidence":[{"source_report":"review_rev12/out/0_injection.md","sha256":"e8d4467af5f090f7794f718dd7f0ba552c609dcc18037f67427d107b5e8aa47a","scope":"per-record source facts for 106 byte-identical statements; collision coverage; actor resolution; Slack thread rollups","verified_unchanged":"statement bytes; source and reference fingerprints; Slack and Gmail manifests; clock; git heads"}],"sql_sha256":"1f2175a297fd390960f22c3767f790fc980a881023affa6ece970745fb40289b","universe":"synthcut"}
```

Any SQL change, including an advisory fix, invalidates the affected rows. Task discoverability, persona reach and Unique Ground Truth stay with `/prompt`.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (level not reported by the runtime)

Next action: Proceed to /prompt. ADV-2 is the one coherence item left; its fix is one sentence on L213. Any SQL edit needs a rerun of the affected rows.

Evidence limits: No required static check is unresolved. Outside this static scope: live execution and deployment; current database compatibility (the snapshot is unverified, 12 used columns are NOT COVERED, and the live schema file in the SQL header was not opened by instruction); search ranking and Agent visibility. Two facts cannot be confirmed from the export: L255's statement that the Sep 30 update carried only the teams and social changes (git shows no deploy content), and whether `state_history_json` needs updating for the five state changes (ZOM-344, ZOM-432, ZOM-542, ZOM-563, ZOM-566). Sprites are Git LFS pointers, so art claims were checked by file change, not by eye. The report is saved in the review folder, not through `hg_write_output.py`, as the setup requires.
