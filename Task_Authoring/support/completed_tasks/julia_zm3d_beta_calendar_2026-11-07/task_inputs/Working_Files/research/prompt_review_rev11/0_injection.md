# Injection Data-Integrity Report (Eval 0), delta review of rev11

**Review version:** `injection-static-v2`
**Evidence contract:** `stage-evidence-v1`
**Reused evidence:** the rev10 report (section 13). Everything on changed or new statements is NEW.

## 1. Scope and provenance

| Item | Value |
|---|---|
| Review | Independent `/injection` delta review, chat/attachment mode, audit only |
| Actual review time | 2026-11-06 (machine clock 2026-11-06T11:27Z; not the task clock) |
| Universe | Oct 1, 2025 (synth-cut), `hg4-synth-sep30cut` v16 |
| Fixed clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| SQL under review | `R11/inputs/01_Universe_Inject.sql`, sha256 `1348d287ac4a105c41b9f0bf511c6664e306adcc3cf42406688a228fd4b684e7`, 264 lines, 110 statements |
| Previous SQL | `R11/prev/01_Universe_Inject.rev10.sql`, sha256 `ffbac4586fb91842ca16263c2b76987c26623c7ed689e00d33886c63f9331bdc`, 107 statements |
| Previous report | `review_rev10/out/0_injection.md`, sha256 `67e1ab6fe77bf78e8f7010487272ed2a2ddf056f4a54d5ade27b6c486ecc7e0a` (PASS / COMPLETE; hash rechecked) |
| Universe manifest | sha256 prefix `da2f4cf0dcf71025`; archive sha256 `d04f295b4c878cce145ad0d77fc5668962b1cb63412fc98f427a0026aeb0fb0c` |
| Repository state | `match3d` `0ff577550e`, `match3d-backend` `a0e4a21`, `match3d-quests` `d8ca05a` |

R11 = `/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review_rev11`.

**Reuse dependencies, all rechecked equal to the rev10 report:** `linear` `b49ec9e856cf0b29`, `gcal` `4f093d897c8b53c8`, `gdrive` `05147aa245b7b2c9`, `gdocs` `1b53998df793e33c`, `gslides` `1d3dab9e4bec7a9e`, `gsheets` `a9cc229c87ae3309`, `trello` `6ba242f4dde4043d`, `confluence` `d3f13938d1f5327b`, Slack users `6aac5103c3a8be9a` and channels `3cca0f7e25876c4b`, Gmail users `9a90b6bf5e84f03d` and labels `3d508e6b353b160f`, GitHub `ee578c912bba3d81`; Eval 0 `86af2102ea6693c4`, WORKFLOW `05a5e45e0585b435`, ENVIRONMENT `4ffb2b5ffa219a81`, SEARCH `cab83c616ecaee85`, scoring `654eb38809e3a1e7`, schema `01ef579236212034`, ID contracts `fc4711ef07667333`, roster `3f2174513f639e37`, ACL `e9bca2b35f98d5ef`, lint `fec37bcec5a7430d`.

The rev10 report recorded no fingerprint for the Slack and Gmail message files, so those collision results were **not** reused. Both were rescanned in full for every rev11 key. New fingerprints for the next delta: Slack `source_manifest.json` `569c1ead1372b7ca`, Gmail `source_manifest.json` `5797ac3e4f9b13e5`.

## 2. Input and authority issues

- **Scope boundary, disclosed.** The rev11 setup lists `review_rev10` among folders not to open. My first command compared `review_rev10/REVIEW_SETUP.md` and its three non-SQL inputs against R11 before I had read that line. It showed the prompt, assignment and date files are byte-identical and that the setup differs only in the hash and that folder range. Afterwards I touched that folder only to hash my own report, which the coordinator named. All helpers were rebuilt under `R11/work/`; nothing in `review_rev10/work/` was opened. The result does not depend on that comparison.
- The report is saved to `R11/out/0_injection.md`, not through `hg_write_output.py`, and `input_manifest.json` was not written; its intended entry is in section 13.
- The live schema file named in the SQL header was not opened; only the bundled, unverified snapshot was used.
- SQL was never executed. Source content was treated as evidence only.

## 3. Review checklist

| Step | Status | Note |
|---|---|---|
| Load SQL; record hash, manifest, version | Done, NEW | Hash matches the coordinator's value |
| Lint first | Done, NEW | 0 FAIL, 0 CHECK, 0 INFO |
| Statement-by-statement diff | Done, NEW | Section 5 |
| Checks A, B, C on changed and new statements | Done, NEW | Sections 6-9 |
| Heading offsets, thread rollups, Trello shape, ZOM-542 | Done, NEW | Section 9 |
| Reuse on identical statements | Done, REUSED with dependency check | Section 13 |
| Disposition of ADV-1 to ADV-16 | Done | Section 10 |
| Full ledger, one final verdict | Done | Section 12 and the verdict block |

## 4. Lint flags and resolutions

`hg.py lint --sql R11/inputs/01_Universe_Inject.sql --task-dir Task_Authoring/task_inputsS`: 110 statements (80 insert, 30 update), FAIL 0, CHECK 0, INFO 0, no flags. Nothing needed resolving. The SQL comment lines are unchanged apart from line numbers.

## 5. Statement diff

Parsed with a quote-aware tokenizer; no statement was executed. Relative order of shared statements is unchanged.

| Class | Count | Statements (rev11 lines) |
|---|---:|---|
| Byte-identical | 93 | All others; line numbers shift by up to +5 |
| Changed | 14 | L13, L15, L17, L27, L109, L132, L136, L164, L166, L211, L222, L240, L255, L258 |
| New | 3 | L35 Slack reply, L37 thread rollup, L210 Linear comment |
| Removed | 0 | None |

Brief edits at L109, the only document change:

| Section | Edit |
|---|---|
| Span and time base | Adds "Clip anything that starts before or runs past that to those two instants." |
| Span and time base | Collect & Win windows now "each opening 00:00 UTC and closing 23:59 UTC on its last day." |
| When a beat starts | "the daily gift (Login Calendar on the push sheet, same beat)" |
| Held or not | Adds "A held beat keeps its usual windows on its row, marked held." |
| Config locks | "moves to any time before it" replaces "moves earlier" |

## 6. Results for checks A-C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | New keys free against complete collections; new Slack id matches the formula; Douglas, Brian, the channel, thread parent and ZOM-465 all resolve. All rev11 keys rescanned. Section 7. |
| B — SQL structure and supported schema rules | PASS | 110 statements parse; counts match; 132 JSON literals valid; no new columns. The Trello payload is valid JSON and a shape base already holds. Section 8. |
| C — Dates, relationships and consistency | PASS | No future event dates; 9 heading runs and 9 thread rollups recompute exactly; ZOM-542, the new reply and the new comment are consistent with base; no demonstrated contradiction. Section 9. |

## 7. Check A: records, references and IDs

**Complete-collection rescans for all rev11 keys (NEW).**

| Collection | Scope | Result |
|---|---|---|
| Slack by id, and by path channel + ts | 4,840 files, 610,468 messages | 0 collisions on 12 inserts |
| Gmail threads and messages | 81,404 threads, 95,164 messages | 0 collisions |
| `hg.py records`, 22 checks | Linear, GitHub, GCal, Drive, Docs, Slides, Sheets, Trello, Slack users and channels | All `scan_complete: true`, no errors; new keys absent; all referenced records found |
| Duplicate keys inside the SQL | 80 inserts | 0 |

**New keys.** `7d70c7753179c98b6c8b2b5457a1e5e7` equals `sha256("C09EVVCFHKR|1758903764.713429")[:32]`. `cmt_zom465_3` is free; base Linear has 0 comments and the 31 SQL ids are unique.

**References.** `C09EVVCFHKR` is `#zm-collect-win`. `EMPLOYEE_0031_SLACK_ID` is Douglas, a listed member who joined on 09-15. Parent `0069f6143e89802993b39e442d3baeb2` is Brian's 09-26 ask at ts 1758899400.476649, and the reply's `thread_ts_legacy` equals it. `usr_fc22d5941b2aeb5c` is Brian Foster. ZOM-465 and ZOM-542 exist. The Trello action keeps its board, card, member and the top-level `idCard` column.

## 8. Check B: SQL structure and supported schema rules

- 110 statements parse; column and value counts equal on all 80 inserts; no upsert clause, expression or cast.
- Parents precede children: L35 before L37, L210 before L211, L239 before L240.
- 132 JSON literals parse. Linear `*_at` values are all `YYYY-MM-DDTHH:MM:SSZ`. Generated columns are untouched. No required column is omitted.
- Snapshot comparison: no new columns; `state_id` on `linear_issues` is covered. The same 12 columns remain NOT COVERED (ADV-13).

## 9. Check C: dates, relationships and consistency

**Dates.** The only values after the clock are the eight Oct 8 `start_ts` and `end_ts` plan fields. The latest event is L17 at 2025-09-30T22:10:41Z. The new reply's `created_at` equals its ts.

### 9.1 Heading offsets (L109)

Body is 2,992 characters, LF only. Each run was recomputed; each sits on the exact heading text, with a line break on both sides, and each heading occurs once.

| Style | Text | rev10 | rev11 |
|---|---|---|---|
| TITLE | ZM3D beta live-ops calendar - working rules | 0-43 | 0-43 |
| HEADING_2 | Span and time base | 163-181 | 163-181 |
| HEADING_2 | Scope | 497-502 | 609-614 |
| HEADING_2 | When a beat starts | 648-666 | 760-778 |
| HEADING_2 | Held or not | 1169-1180 | 1284-1295 |
| HEADING_2 | One-offs | 1736-1744 | 1912-1920 |
| HEADING_2 | Still to do | 1944-1955 | 2120-2131 |
| HEADING_2 | Push copy | 2261-2270 | 2437-2446 |
| HEADING_2 | Config locks | 2589-2601 | 2765-2777 |

The brief's facts still hold. Collect & Win windows match `runtime.exs` L211-219, whose cron closes at midnight (ADV-21). The Login Calendar row exists. The One-offs later-word rule is unchanged, so the cut in L17 loses nothing.

### 9.2 Thread rollups

Recomputed from base replies plus the overlay, not from the SQL's stated values.

| Parent | Channel | Base replies / users / latest | After SQL | Result |
|---|---|---|---|---|
| `0069f614` **new** | #zm-collect-win | 2 / 1 / 1758899428.567489 | 3 / 2 / 1758903764.713429 | Correct: Douglas is a new replier and the latest |
| `9025d428` | #zombie-art | 0 / 0 / none | 1 / 1 / 1758213623.552919 | Correct |
| `a3e78e82` | #zombie-art | 3 / 3 / 1759161266.305589 | 4 / 4 / 1759250468.275139 | Correct |
| `ede90bc6` | #zombie-bugs | 0 / 0 / none | 1 / 1 / 1759187861.318279 | Correct |
| `d0dd5d3a` | #zombie-bugs | 4 / 3 / 1759254162.721499 | 5 / 3 / 1759268775.482369 | Correct |
| `c2b9c903` | #zombie-prs | 16 / 1 / 1759247478.371389 | 17 / 1 / same | Correct |
| `61f686b8` | #zombie-prs | 3 / 1 / 1759247586.958099 | 4 / 1 / same | Correct |
| `4b7c4127` | #zombie-prs | 41 / 1 / 1759162433.383449 | 42 / 1 / same | Correct |
| `bca78437` (injected root) | DM | n/a | 1 / 1 / 1759263878.305129 | Correct |

**New #zm-collect-win reply (L35).** Brian's ask at 09-26 15:10:00Z: "I Also changed 1 reward in each of the two reward tables. Could you update them?", with two gid links into one sheet. `runtime.exs` confirms two tables (`Collect&Win - Day 2`, `Collect&Win - Day 3`). Douglas's "Both tables are updated." comes 72 minutes later; his previous base post is 16:06Z, and the channel carries base messages through 09-30, so a 09-26 post fits despite `is_archived: true` (SC-57, ADV-19). No later base record reopens the request.

### 9.3 ZOM-542 state change

Regression → Todo at L240, `updated_at` 2025-09-22T18:40:21Z.

- Base: `Regression`, with `updated_at` = `created_at`, so no base record dates that state. Slack and Gmail hold no status event for the ticket; the only bot line is creation in #zombie-art.
- `Todo` fits L239 ("Picking this up after the bug list.") better than Regression, and fits an Improvement ticket. The other base Regression tickets include bugs such as ZOM-359 and ENG-2331.
- `updated_at` advances and equals the comment time. `started_at` and `completed_at` stay null, which is valid for Todo. `Todo` is an existing ZOM state.
- No code or Slack shows the work started by the cut; #471 touches the Home screen under ZOM-498, a different ticket.

No defect. One disclosed limit: `state_history_json` cannot be checked (five state changes now, verdict block).

### 9.4 Trello payload (L258)

| Population | `data` keys | Count |
|---|---|---:|
| rev10 row | board, card, idCard, list, text, textData | same as 11 of 12 on this board |
| **rev11 row** | **board, card, text** | **same as 1 of 56** |
| ZM ROADMAP comments | board, card, idCard, list, text, textData (one also dateLastEdited) | 12 of 12 |
| All base commentCard | carry `list` and `textData` | 54 of 56 |
| All base commentCard | carry `data.idCard` | 15 of 56 |
| Base rows with no `list` | both 2014 Welcome Board sample cards | 2 of 56 |

Not a defect. Eval 0 bars inferring constraints from stored examples, and no documented rule requires these keys. Base already loads two rows without `list` or `textData`, the top-level `idCard` column is still set, and `board`, `card` and `text` keep the base key sets. `badges` and `dateLastActivity` at L260 stay correct. It is, however, a shape regression from rev10, which matched this board exactly (ADV-18).

### 9.5 Other changed and new statements

- **L210, Brian on ZOM-465.** Sequence 3, after L209, dated after the brief, and L211 moves `updated_at` to match. Code supports "the one event icon with no animation": the six `IOrderableIcon` classes (Quest, Endless, InfiniteBoss, ZombieLane, SeasonPass, PlagueRace) all drive `SetBool("Animated", …)`, and `CollectAndWinTokenProgressBarMainMenu.prefab` has 0 Animators. See ADV-17 and ADV-20.
- **L164 and L166.** Mirror text equals the review comment after unescaping; its ts equals the comment second. "Art" removes the code conflict, and `Assets/Sprites/Season Pass/` holds `bg - golden stripe.png`.
- **L255.** Still supported by Douglas's 18:16 and Vincent's 21:58 DMs.
- **L13, L15, L17, L27, L222, L132, L136.** Text only; no id, thread or time changed. Each new sentence was read against base and against L11, L109 and L143; no conflict.
- **Unchanged neighbours reopened by the delta.** L208 and L209 (same ticket as L210) and L260 (card behind L258) are consistent with the edits.

## 10. What happened to ADV-1 to ADV-16

| ADV | rev10 subject | rev11 status | Current marking |
|---|---|---|---|
| 1 | Sep 30 prod update vs "DEV stack only" | **Reduced.** L255 drops the Julia-visible "Douglas's teams update". The suggested clarifying comment was not added, so L154, L98 and the base DM still stand | CSC, lower likelihood |
| 2 | ZOM-344 close vs chest timing | **Open, unchanged.** L213 and L214 are byte-identical | CSC |
| 3 | "Premium strip" with no client trace | **Reduced.** L164 and L166 now say "art", which removes the code conflict. "October range" and "date change" remain on an art item | Cosmetic |
| 4 | Reply narrows the brief's naming rule | **Closed.** L13 no longer claims the brief is silent; the reply states the rule outright | None |
| 5 | Deck "scaled up" vs "hold" | **Closed.** L132 and L136 agree with L143 | None |
| 6 | ZOM-504 "Still only" | **Closed.** L222 is framed as a re-test | None |
| 7 | `#468#ev_6` order | Open, unchanged | Cosmetic |
| 8 | `revision_id` pattern | Open, unchanged | Cosmetic |
| 9 | #468 Reviewers edit | Open, unchanged | Cosmetic |
| 10 | Daily Gift frame not confirmed by eye | Open, unchanged | Cosmetic |
| 11 | "next build" | **Closed.** L27 says "next store build" | None |
| 12 | Change-request clause has no record | Open, unchanged; clause kept in L109 | Cosmetic |
| 13 | 12 columns NOT COVERED | Open, unchanged; no new columns | Cosmetic |
| 14 | Julia not listed in #zombie-prs | Open, unchanged | Cosmetic |
| 15 | Sheet has NULL `content_path` | Open, unchanged | Cosmetic |
| 16 | Gmail LF and short headers | Open, unchanged | Cosmetic |

## 11. Findings

### Demonstrated defects

None. No statement violates a rule in Checks A, B or C on the evidence available.

### Advisories: a /prompt reviewer could score this under Cross-Service Coherence

**ADV-2. ZOM-344 closes on "reads well" while the quest chest timing complaint runs on (open).**
- Injected: L213 (09-16) "Quest box open and close animation reuses the endless chest curve and reads well on the quest screen. Art side is signed off on my end."; L214 sets Done.
- Base: Marcus 08-11 "some chest quest animations show the reward before the chest open"; Marcus DM 09-23 "the rewards appears first and then the chest opens"; Marcus DM 09-30 "The chest opens before the rewards and I haven't done it like that. Sometimes it plays ok u know"; Vincent, Bug Checklist 09-30 "the timing is off. Especially in the quest chests."
- Not a defect: art sign-off and reward timing on claim are different scopes.
- Fix: end L213 with "Art side is signed off on my end. The reward-before-open timing on claim is a separate integration issue."

**ADV-1. A prod backend update lands after "DEV stack only" (reduced, lower likelihood).**
- Injected: L154 (09-30 15:51:06Z) "they reach prod with the next backend release."; L98 (Oct 8) "go live with this release".
- Base: Douglas DM 09-30 18:16Z "Ok, I updated the prod environment with the latest teams/social changes". On `match3d-backend` `main`, Win and Collect `adb56ad` precedes the teams commit `3345557`, where prod `runtime.exs` already has `enabled: true`.
- What changed: L255 no longer repeats this to Julia, whose reach excludes that DM. The tension survives only for a reviewer reading evaluator-wide.
- Not a defect: the DM is scoped to teams/social and nothing shows the windows shipped.
- Fix, optional: a Douglas comment on ZOM-563 at about 18:15Z, "Prod has the teams/social changes only. The live-ops server windows stay on dev until the Oct 8 release."

**ADV-17 (new). "Written before that event came in" rubs against Brian's own earlier text; lower likelihood.**
- Injected: L210 "Keep it on this ticket, the master VFX list was written before that event came in."
- Base: ZOM-526, child of ZOM-521, Brian, 2025-09-02: "We will implement this together with season passes and collect&win events"; Brian 09-12, #zm-animations: "P0 – Collect & Win → may need your help later, but not clear yet". Backend Win and Collect dates from 09-01.
- Not a defect: "came in" can mean landed, as L209 uses it, and #468 merged 09-29.
- Fix: "Keep it on this ticket, the master VFX list was ticked before that event merged."

### Advisories: cosmetic

- **ADV-3 (reduced).** L164 "premium strip art still shows the October range … the date change" still uses date wording for an art item. Reword to "still shows October" and "the change" if you touch it.
- **ADV-7.** `#468#ev_6` sorts after merged and closed because `created_at` is NULL, as in base.
- **ADV-8.** `revision_id` values don't follow the base first-10-hex pattern; unlisted field.
- **ADV-9.** The #468 parent gains Arthur in Reviewers; base #472 wasn't updated that way.
- **ADV-10.** Samuel's Daily Gift list mentions only font and alignment. The sprite changed in #471, but it is an LFS pointer.
- **ADV-12.** The brief's change-request clause has no qualifying record; the latest CHANGES_REQUESTED is `match3d#303`, 2025-07-16.
- **ADV-13.** 12 columns are NOT COVERED by the unverified snapshot: `extras_json`, `drive_id`, `notes`, `ordinal`, `table_json`, `pull_request_review_id`, `seq` (review comments and reviews), `side`, `start_line`, `start_side`, `subject_type`, `sequence`. Confirm against the live schema before deploy.
- **ADV-14.** Julia isn't in the listed members of public `#zombie-prs`; GitHub is unscoped, so nothing depends on the mirrors.
- **ADV-15.** The injected sheet has NULL `content_path`, unlike all 356 base sheets; it is served through its Sheets rows and passes the lint rule.
- **ADV-16.** Gmail bodies use LF where base uses CRLF, and the header set is short.
- **ADV-18 (new).** Trello `data` dropped `idCard`, `list` and `textData` (section 9.4). The row now differs from all 12 comments on its board. Fix: restore `"idCard":"68c452a03006277f55d9dc96"`, `"list":{"id":"6851a674975da1fe76e70d93","name":"BETA: Sep 30"}` and `"textData":{"emoji":{}}`. If `list` went on purpose, because of the SC-13 name, restore the other two.
- **ADV-19 (new).** L35 sits in `#zm-collect-win`: `is_archived: true` (SC-57) and Julia is not a listed member. Brian's ask is in the same public channel, so whoever can read the ask can read the reply. Reach belongs to `/prompt`.
- **ADV-20 (new).** "Event icon" at L209 and L210 is really a progress-bar widget with a bottle icon, not a `MainMenu/icons` prefab. The claim holds in substance.
- **ADV-21 (new).** L109 says windows close 23:59 UTC; the cron resets at 00:00 the next day (`0 0 * * 3`). This follows the brief's own "Sun Nov 2 23:59 UTC" convention.

## 12. Full operation ledger

Operation order as in rev11. "rev10 line" is blank for new statements. IDENTICAL rows point at the rev10 report's ledger.

| # | Line | rev10 line | Table | Op | Record / target | Status | Result |
|---|---|---|---|---|---|---|---|
| 1 | 11 | 11 | slack.slack_messages | INSERT | `bca784379e7dbca9e64e79a64dfefbba` | IDENTICAL | REUSED rev10 ledger #1. Keys, JSON, dates and rollups also rechecked in the full passes |
| 2 | 13 | 13 | slack.slack_messages | INSERT | `890dc27f56e8501bd7590ffdfc231057` | CHANGED | CHANGED text only: opener now 'Two things on top of the brief.' Ids, thread and times unchanged. Facts on the four PN rows reused. Closes ADV-4 |
| 3 | 15 | 15 | slack.slack_messages | INSERT | `933cee9f6464a80e4b1f05259b595b20` | CHANGED | CHANGED text only: 'one week of the beta', 'if it lands in time'. Author, thread, ts unchanged; L21 rollup recomputed OK |
| 4 | 17 | 17 | slack.slack_messages | INSERT | `669d15f685f158633e56302160957f1e` | CHANGED | CHANGED text only: drops the last clause. Brief's One-offs line still carries the later-word rule, so nothing is lost |
| 5 | 19 | 19 | slack.slack_messages | INSERT | `b5f2955c2e154efc6835946ecfe1758e` | IDENTICAL | REUSED rev10 ledger #5. Keys, JSON, dates and rollups also rechecked in the full passes |
| 6 | 21 | 21 | slack.slack_messages | UPDATE | `9025d428af1f551a20e303c3acbc545b` | IDENTICAL | REUSED rev10 ledger #6. Keys, JSON, dates and rollups also rechecked in the full passes |
| 7 | 23 | 23 | slack.slack_messages | INSERT | `e343557b2e94a1701251ebd079e6f0ce` | IDENTICAL | REUSED rev10 ledger #7. Keys, JSON, dates and rollups also rechecked in the full passes |
| 8 | 25 | 25 | slack.slack_messages | UPDATE | `ede90bc6ec6cb16fd97663f2888f39a2` | IDENTICAL | REUSED rev10 ledger #8. Keys, JSON, dates and rollups also rechecked in the full passes |
| 9 | 27 | 27 | slack.slack_messages | INSERT | `a08ff7cbfc52008d7dee8457e9385a3c` | CHANGED | CHANGED text only: 'next store build'. Commit `25c6c66b6b` 21:20:26Z is after store builds iOS #50 and Android #135 started. Closes ADV-11 |
| 10 | 29 | 29 | slack.slack_messages | UPDATE | `d0dd5d3ad4658add1f79802e2aa60e48` | IDENTICAL | REUSED rev10 ledger #10. Keys, JSON, dates and rollups also rechecked in the full passes |
| 11 | 31 | 31 | slack.slack_messages | INSERT | `532747cb5d123a95d13204e57b5a7a38` | IDENTICAL | REUSED rev10 ledger #11. Keys, JSON, dates and rollups also rechecked in the full passes |
| 12 | 33 | 33 | slack.slack_messages | UPDATE | `a3e78e820b9f880ef4e3d941562110df` | IDENTICAL | REUSED rev10 ledger #12. Keys, JSON, dates and rollups also rechecked in the full passes |
| 13 | 35 | — | slack.slack_messages | INSERT | `7d70c7753179c98b6c8b2b5457a1e5e7` | NEW | NEW. id = sha256(channel\|ts)[:32]; free in 610,468 msgs; created_at = ts; Douglas is a channel member; reply to Brian's 09-26 15:10:00Z ask, 72 min later; 'Both tables' matches 'two reward tables' and his two gid links; no later base record reopens it. ADV-19 |
| 14 | 37 | — | slack.slack_messages | UPDATE | `0069f6143e89802993b39e442d3baeb2` | NEW | NEW. Base 2/1/1758899428.567489 (both replies Brian) + L35 = 3/2/1758903764.713429. Matches recompute |
| 15 | 39 | 35 | gmail.gmail_threads | INSERT | `brian.foster@harmonygames.co/1843954828968110017` | IDENTICAL | REUSED rev10 ledger #13. Keys, JSON, dates and rollups also rechecked in the full passes |
| 16 | 40 | 36 | gmail.gmail_messages | INSERT | `brian.foster/<CAPT--p4sBC8XnaA7qB…` | IDENTICAL | REUSED rev10 ledger #14. Keys, JSON, dates and rollups also rechecked in the full passes |
| 17 | 50 | 46 | gmail.gmail_threads | INSERT | `julia.lawson@harmonygames.co/1843954828968533812` | IDENTICAL | REUSED rev10 ledger #15. Keys, JSON, dates and rollups also rechecked in the full passes |
| 18 | 51 | 47 | gmail.gmail_messages | INSERT | `julia.lawson/<CAPT--p4sBC8XnaA7qB…` | IDENTICAL | REUSED rev10 ledger #16. Keys, JSON, dates and rollups also rechecked in the full passes |
| 19 | 61 | 57 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843954828968789474` | IDENTICAL | REUSED rev10 ledger #17. Keys, JSON, dates and rollups also rechecked in the full passes |
| 20 | 62 | 58 | gmail.gmail_messages | INSERT | `frederick.stone/<CAPT--p4sBC8XnaA7qB…` | IDENTICAL | REUSED rev10 ledger #18. Keys, JSON, dates and rollups also rechecked in the full passes |
| 21 | 72 | 68 | gmail.gmail_threads | INSERT | `brian.foster@harmonygames.co/1844311412965607905` | IDENTICAL | REUSED rev10 ledger #19. Keys, JSON, dates and rollups also rechecked in the full passes |
| 22 | 73 | 69 | gmail.gmail_messages | INSERT | `brian.foster/<CAPT--p4a5fY9wd6vr+…` | IDENTICAL | REUSED rev10 ledger #20. Keys, JSON, dates and rollups also rechecked in the full passes |
| 23 | 81 | 77 | gmail.gmail_threads | INSERT | `julia.lawson@harmonygames.co/1844311412966040123` | IDENTICAL | REUSED rev10 ledger #21. Keys, JSON, dates and rollups also rechecked in the full passes |
| 24 | 82 | 78 | gmail.gmail_messages | INSERT | `julia.lawson/<CAPT--p4a5fY9wd6vr+…` | IDENTICAL | REUSED rev10 ledger #22. Keys, JSON, dates and rollups also rechecked in the full passes |
| 25 | 90 | 86 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844311412966288046` | IDENTICAL | REUSED rev10 ledger #23. Keys, JSON, dates and rollups also rechecked in the full passes |
| 26 | 90 | 86 | gmail.gmail_messages | INSERT | `frederick.stone/<CAPT--p4a5fY9wd6vr+…` | IDENTICAL | REUSED rev10 ledger #24. Keys, JSON, dates and rollups also rechecked in the full passes |
| 27 | 98 | 94 | gcal.gcal_events | INSERT | `evt_9a4c2e7f1b3d58e06c7a2f` | IDENTICAL | REUSED rev10 ledger #25. Keys, JSON, dates and rollups also rechecked in the full passes |
| 28 | 100 | 96 | gcal.gcal_events | INSERT | `evt_5c1e83a7d94b02f6c8e31a` | IDENTICAL | REUSED rev10 ledger #26. Keys, JSON, dates and rollups also rechecked in the full passes |
| 29 | 102 | 98 | gcal.gcal_events | INSERT | `evt_a72f4d9e0c1b58d3e6f40b` | IDENTICAL | REUSED rev10 ledger #27. Keys, JSON, dates and rollups also rechecked in the full passes |
| 30 | 104 | 100 | gcal.gcal_events | INSERT | `evt_1d6b9a03e5c27f84b0d92c` | IDENTICAL | REUSED rev10 ledger #28. Keys, JSON, dates and rollups also rechecked in the full passes |
| 31 | 106 | 102 | gdrive.drive_files | INSERT | `d_5f2c8e1b7a94d03c6e2b58` | IDENTICAL | REUSED rev10 ledger #29. Keys, JSON, dates and rollups also rechecked in the full passes |
| 32 | 108 | 104 | gdrive.drive_files | INSERT | `f_7c3e91a4d2b85f60e1a9c4` | IDENTICAL | REUSED rev10 ledger #30. Keys, JSON, dates and rollups also rechecked in the full passes |
| 33 | 109 | 105 | gdocs.docs_documents | INSERT | `f_7c3e91a4d2b85f60e1a9c4` | CHANGED | CHANGED body and style runs: 4 lines edited, 190 chars added. All 9 runs recomputed exact. Times, owner, shares unchanged. See section 9.1. ADV-21 |
| 34 | 129 | 125 | gdrive.drive_files | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | IDENTICAL | REUSED rev10 ledger #32. Keys, JSON, dates and rollups also rechecked in the full passes |
| 35 | 130 | 126 | gslides.slides_presentations | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | IDENTICAL | REUSED rev10 ledger #33. Keys, JSON, dates and rollups also rechecked in the full passes |
| 36 | 131 | 127 | gslides.slides_pages | INSERT | `slide_6f2a9d14c7e0` | IDENTICAL | REUSED rev10 ledger #34. Keys, JSON, dates and rollups also rechecked in the full passes |
| 37 | 132 | 128 | gslides.slides_page_elements | INSERT | `el_9d1c74b0a26e` | CHANGED | CHANGED text: 'Beta-cohort buy'. Closes half of ADV-5 |
| 38 | 135 | 131 | gslides.slides_pages | INSERT | `slide_b83e51a09d72` | IDENTICAL | REUSED rev10 ledger #36. Keys, JSON, dates and rollups also rechecked in the full passes |
| 39 | 136 | 132 | gslides.slides_page_elements | INSERT | `el_5e83a1f4c092` | CHANGED | CHANGED text: 'any scale-up comes after the pivot call', now agrees with L143. Closes ADV-5 |
| 40 | 142 | 138 | gslides.slides_pages | INSERT | `slide_0c47d2e81b6f` | IDENTICAL | REUSED rev10 ledger #38. Keys, JSON, dates and rollups also rechecked in the full passes |
| 41 | 143 | 139 | gslides.slides_page_elements | INSERT | `el_c07b2e9d3148` | IDENTICAL | REUSED rev10 ledger #39. Keys, JSON, dates and rollups also rechecked in the full passes |
| 42 | 146 | 142 | gdrive.drive_files | INSERT | `f_e4a17c90b3d25f6a8c1d73` | IDENTICAL | REUSED rev10 ledger #40. Keys, JSON, dates and rollups also rechecked in the full passes |
| 43 | 147 | 143 | gsheets.sheets_spreadsheets | INSERT | `f_e4a17c90b3d25f6a8c1d73` | IDENTICAL | REUSED rev10 ledger #41. Keys, JSON, dates and rollups also rechecked in the full passes |
| 44 | 148 | 144 | gsheets.sheets_sheets | INSERT | `sheet 0 Calendar` | IDENTICAL | REUSED rev10 ledger #42. Keys, JSON, dates and rollups also rechecked in the full passes |
| 45 | 149 | 145 | gsheets.sheets_sheets | INSERT | `sheet 1 Pushes` | IDENTICAL | REUSED rev10 ledger #43. Keys, JSON, dates and rollups also rechecked in the full passes |
| 46 | 154 | 150 | github.github_review_comments | INSERT | `match3d#470#rc_10` | IDENTICAL | REUSED rev10 ledger #44. Keys, JSON, dates and rollups also rechecked in the full passes |
| 47 | 156 | 152 | github.github_reviews | INSERT | `match3d#468#rev_3` | IDENTICAL | REUSED rev10 ledger #45. Keys, JSON, dates and rollups also rechecked in the full passes |
| 48 | 157 | 153 | github.github_review_comments | INSERT | `match3d#468#rc_38` | IDENTICAL | REUSED rev10 ledger #46. Keys, JSON, dates and rollups also rechecked in the full passes |
| 49 | 158 | 154 | github.github_timeline_events | INSERT | `match3d#468#ev_6` | IDENTICAL | REUSED rev10 ledger #47. Keys, JSON, dates and rollups also rechecked in the full passes |
| 50 | 160 | 156 | slack.slack_messages | INSERT | `73bc730c620936feba3dcfbba00e2745` | IDENTICAL | REUSED rev10 ledger #48. Keys, JSON, dates and rollups also rechecked in the full passes |
| 51 | 162 | 158 | slack.slack_messages | UPDATE | `c2b9c90355cf8c2c4326ab19d3a24f79` | IDENTICAL | REUSED rev10 ledger #49. Keys, JSON, dates and rollups also rechecked in the full passes |
| 52 | 164 | 160 | github.github_review_comments | INSERT | `match3d#472#rc_1` | CHANGED | CHANGED body: 'art still shows'. Path, review link, time, seq unchanged. Sprites hold `bg - golden stripe.png`. Reduces ADV-3 |
| 53 | 166 | 162 | slack.slack_messages | INSERT | `65564543e4bc8dd707a177aada2337a3` | CHANGED | CHANGED attachment text: equals L164 body after unescape; ts, lag, parent, discussion id unchanged |
| 54 | 168 | 164 | slack.slack_messages | UPDATE | `61f686b8a8b6c164b14aff6b5b1897bf` | IDENTICAL | REUSED rev10 ledger #52. Keys, JSON, dates and rollups also rechecked in the full passes |
| 55 | 170 | 166 | slack.slack_messages | INSERT | `78aa8ed77c0bd7b8a3fad227b22bc3fb` | IDENTICAL | REUSED rev10 ledger #53. Keys, JSON, dates and rollups also rechecked in the full passes |
| 56 | 172 | 168 | slack.slack_messages | UPDATE | `4b7c41278397b56b36e9b2f8a820c454` | IDENTICAL | REUSED rev10 ledger #54. Keys, JSON, dates and rollups also rechecked in the full passes |
| 57 | 177 | 173 | linear.linear_comments | INSERT | `cmt_zom429_1` | IDENTICAL | REUSED rev10 ledger #55. Keys, JSON, dates and rollups also rechecked in the full passes |
| 58 | 179 | 175 | linear.linear_comments | INSERT | `cmt_zom556_1` | IDENTICAL | REUSED rev10 ledger #56. Keys, JSON, dates and rollups also rechecked in the full passes |
| 59 | 180 | 176 | linear.linear_issues | UPDATE | `ZOM-556` | IDENTICAL | REUSED rev10 ledger #57. Keys, JSON, dates and rollups also rechecked in the full passes |
| 60 | 182 | 178 | linear.linear_comments | INSERT | `cmt_zom565_1` | IDENTICAL | REUSED rev10 ledger #58. Keys, JSON, dates and rollups also rechecked in the full passes |
| 61 | 183 | 179 | linear.linear_comments | INSERT | `cmt_zom565_2` | IDENTICAL | REUSED rev10 ledger #59. Keys, JSON, dates and rollups also rechecked in the full passes |
| 62 | 184 | 180 | linear.linear_issues | UPDATE | `ZOM-565` | IDENTICAL | REUSED rev10 ledger #60. Keys, JSON, dates and rollups also rechecked in the full passes |
| 63 | 186 | 182 | linear.linear_comments | INSERT | `cmt_zom543_1` | IDENTICAL | REUSED rev10 ledger #61. Keys, JSON, dates and rollups also rechecked in the full passes |
| 64 | 187 | 183 | linear.linear_issues | UPDATE | `ZOM-543` | IDENTICAL | REUSED rev10 ledger #62. Keys, JSON, dates and rollups also rechecked in the full passes |
| 65 | 189 | 185 | linear.linear_comments | INSERT | `cmt_zom526_1` | IDENTICAL | REUSED rev10 ledger #63. Keys, JSON, dates and rollups also rechecked in the full passes |
| 66 | 190 | 186 | linear.linear_comments | INSERT | `cmt_zom526_2` | IDENTICAL | REUSED rev10 ledger #64. Keys, JSON, dates and rollups also rechecked in the full passes |
| 67 | 191 | 187 | linear.linear_comments | INSERT | `cmt_zom526_3` | IDENTICAL | REUSED rev10 ledger #65. Keys, JSON, dates and rollups also rechecked in the full passes |
| 68 | 192 | 188 | linear.linear_issues | UPDATE | `ZOM-526` | IDENTICAL | REUSED rev10 ledger #66. Keys, JSON, dates and rollups also rechecked in the full passes |
| 69 | 194 | 190 | linear.linear_comments | INSERT | `cmt_zom552_1` | IDENTICAL | REUSED rev10 ledger #67. Keys, JSON, dates and rollups also rechecked in the full passes |
| 70 | 195 | 191 | linear.linear_issues | UPDATE | `ZOM-552` | IDENTICAL | REUSED rev10 ledger #68. Keys, JSON, dates and rollups also rechecked in the full passes |
| 71 | 197 | 193 | linear.linear_comments | INSERT | `cmt_zom534_1` | IDENTICAL | REUSED rev10 ledger #69. Keys, JSON, dates and rollups also rechecked in the full passes |
| 72 | 198 | 194 | linear.linear_comments | INSERT | `cmt_zom534_2` | IDENTICAL | REUSED rev10 ledger #70. Keys, JSON, dates and rollups also rechecked in the full passes |
| 73 | 199 | 195 | linear.linear_issues | UPDATE | `ZOM-534` | IDENTICAL | REUSED rev10 ledger #71. Keys, JSON, dates and rollups also rechecked in the full passes |
| 74 | 201 | 197 | linear.linear_comments | INSERT | `cmt_zom432_1` | IDENTICAL | REUSED rev10 ledger #72. Keys, JSON, dates and rollups also rechecked in the full passes |
| 75 | 202 | 198 | linear.linear_comments | INSERT | `cmt_zom432_2` | IDENTICAL | REUSED rev10 ledger #73. Keys, JSON, dates and rollups also rechecked in the full passes |
| 76 | 203 | 199 | linear.linear_issues | UPDATE | `ZOM-432` | IDENTICAL | REUSED rev10 ledger #74. Keys, JSON, dates and rollups also rechecked in the full passes |
| 77 | 205 | 201 | linear.linear_comments | INSERT | `cmt_zom78_1` | IDENTICAL | REUSED rev10 ledger #75. Keys, JSON, dates and rollups also rechecked in the full passes |
| 78 | 206 | 202 | linear.linear_issues | UPDATE | `ZOM-78` | IDENTICAL | REUSED rev10 ledger #76. Keys, JSON, dates and rollups also rechecked in the full passes |
| 79 | 208 | 204 | linear.linear_comments | INSERT | `cmt_zom465_1` | IDENTICAL | REUSED rev10 ledger #77. Keys, JSON, dates and rollups also rechecked in the full passes |
| 80 | 209 | 205 | linear.linear_comments | INSERT | `cmt_zom465_2` | IDENTICAL | REUSED rev10 ledger #78. Keys, JSON, dates and rollups also rechecked in the full passes |
| 81 | 210 | — | linear.linear_comments | INSERT | `cmt_zom465_3` | NEW | NEW. Id free; author Brian (`usr_fc22d5941b2aeb5c`); sequence 3; 18:13:41Z after L209; ticket created 08-11; dated after the brief. 'One event icon with no animation' holds: six `IOrderableIcon` icons use animators, Collect & Win widget has none. ADV-17, ADV-20 |
| 82 | 211 | 206 | linear.linear_issues | UPDATE | `ZOM-465` | CHANGED | CHANGED: updated_at 18:05:02Z→18:13:41Z = new last comment L210; base 09-23T14:16:25Z, so it advances |
| 83 | 213 | 208 | linear.linear_comments | INSERT | `cmt_zom344_1` | IDENTICAL | REUSED rev10 ledger #80. Keys, JSON, dates and rollups also rechecked in the full passes |
| 84 | 214 | 209 | linear.linear_issues | UPDATE | `ZOM-344` | IDENTICAL | REUSED rev10 ledger #81. Keys, JSON, dates and rollups also rechecked in the full passes |
| 85 | 216 | 211 | linear.linear_comments | INSERT | `cmt_zom442_1` | IDENTICAL | REUSED rev10 ledger #82. Keys, JSON, dates and rollups also rechecked in the full passes |
| 86 | 217 | 212 | linear.linear_issues | UPDATE | `ZOM-442` | IDENTICAL | REUSED rev10 ledger #83. Keys, JSON, dates and rollups also rechecked in the full passes |
| 87 | 219 | 214 | linear.linear_comments | INSERT | `cmt_zom471_1` | IDENTICAL | REUSED rev10 ledger #84. Keys, JSON, dates and rollups also rechecked in the full passes |
| 88 | 220 | 215 | linear.linear_issues | UPDATE | `ZOM-471` | IDENTICAL | REUSED rev10 ledger #85. Keys, JSON, dates and rollups also rechecked in the full passes |
| 89 | 222 | 217 | linear.linear_comments | INSERT | `cmt_zom504_1` | CHANGED | CHANGED text: 'Re-tested: it only shows up…'. Author, ticket, time unchanged. Closes ADV-6 |
| 90 | 223 | 218 | linear.linear_issues | UPDATE | `ZOM-504` | IDENTICAL | REUSED rev10 ledger #87. Keys, JSON, dates and rollups also rechecked in the full passes |
| 91 | 225 | 220 | linear.linear_comments | INSERT | `cmt_zom517_1` | IDENTICAL | REUSED rev10 ledger #88. Keys, JSON, dates and rollups also rechecked in the full passes |
| 92 | 226 | 221 | linear.linear_issues | UPDATE | `ZOM-517` | IDENTICAL | REUSED rev10 ledger #89. Keys, JSON, dates and rollups also rechecked in the full passes |
| 93 | 228 | 223 | linear.linear_comments | INSERT | `cmt_zom521_1` | IDENTICAL | REUSED rev10 ledger #90. Keys, JSON, dates and rollups also rechecked in the full passes |
| 94 | 229 | 224 | linear.linear_comments | INSERT | `cmt_zom521_2` | IDENTICAL | REUSED rev10 ledger #91. Keys, JSON, dates and rollups also rechecked in the full passes |
| 95 | 230 | 225 | linear.linear_issues | UPDATE | `ZOM-521` | IDENTICAL | REUSED rev10 ledger #92. Keys, JSON, dates and rollups also rechecked in the full passes |
| 96 | 239 | 234 | linear.linear_comments | INSERT | `cmt_zom542_1` | IDENTICAL | REUSED rev10 ledger #93. Keys, JSON, dates and rollups also rechecked in the full passes |
| 97 | 240 | 235 | linear.linear_issues | UPDATE | `ZOM-542` | CHANGED | CHANGED: adds state_id Regression→Todo. updated_at = L239 comment time; started_at and completed_at stay null, valid for Todo; 'Todo' is an existing ZOM state (45 tickets). See section 9.3 |
| 98 | 242 | 237 | linear.linear_comments | INSERT | `cmt_zom544_1` | IDENTICAL | REUSED rev10 ledger #95. Keys, JSON, dates and rollups also rechecked in the full passes |
| 99 | 243 | 238 | linear.linear_issues | UPDATE | `ZOM-544` | IDENTICAL | REUSED rev10 ledger #96. Keys, JSON, dates and rollups also rechecked in the full passes |
| 100 | 245 | 240 | linear.linear_comments | INSERT | `cmt_zom546_1` | IDENTICAL | REUSED rev10 ledger #97. Keys, JSON, dates and rollups also rechecked in the full passes |
| 101 | 246 | 241 | linear.linear_issues | UPDATE | `ZOM-546` | IDENTICAL | REUSED rev10 ledger #98. Keys, JSON, dates and rollups also rechecked in the full passes |
| 102 | 248 | 243 | linear.linear_comments | INSERT | `cmt_zom549_1` | IDENTICAL | REUSED rev10 ledger #99. Keys, JSON, dates and rollups also rechecked in the full passes |
| 103 | 249 | 244 | linear.linear_issues | UPDATE | `ZOM-549` | IDENTICAL | REUSED rev10 ledger #100. Keys, JSON, dates and rollups also rechecked in the full passes |
| 104 | 251 | 246 | linear.linear_comments | INSERT | `cmt_zom566_1` | IDENTICAL | REUSED rev10 ledger #101. Keys, JSON, dates and rollups also rechecked in the full passes |
| 105 | 252 | 247 | linear.linear_comments | INSERT | `cmt_zom566_2` | IDENTICAL | REUSED rev10 ledger #102. Keys, JSON, dates and rollups also rechecked in the full passes |
| 106 | 253 | 248 | linear.linear_issues | UPDATE | `ZOM-566` | IDENTICAL | REUSED rev10 ledger #103. Keys, JSON, dates and rollups also rechecked in the full passes |
| 107 | 255 | 250 | linear.linear_comments | INSERT | `cmt_zom563_1` | CHANGED | CHANGED text: drops 'after Douglas's teams update'. Still supported by Douglas 18:16 and Vincent 21:58 DMs. Reduces ADV-1 |
| 108 | 256 | 251 | linear.linear_issues | UPDATE | `ZOM-563` | IDENTICAL | REUSED rev10 ledger #105. Keys, JSON, dates and rollups also rechecked in the full passes |
| 109 | 258 | 253 | trello.trello_actions | INSERT | `68dac8204f1e9a3b7c2d5e61` | CHANGED | CHANGED data_json: keeps board, card, text; drops idCard, list, textData. Valid JSON; ids, name, text, date unchanged; top-level idCard column set. See section 9.4. ADV-18 |
| 110 | 260 | 255 | trello.trello_cards | UPDATE | `68c452a03006277f55d9dc96` | IDENTICAL | REUSED rev10 ledger #107. Keys, JSON, dates and rollups also rechecked in the full passes |

## 13. Stage evidence record

**Reused:** for the 93 byte-identical statements, per-record source facts from `review_rev10/out/0_injection.md` (sha256 `67e1ab6fe77bf78e8f7010487272ed2a2ddf056f4a54d5ade27b6c486ecc7e0a`, section 10 ledger rows as cited above, plus sections 6-8). Verified unchanged: statement bytes, all source and reference fingerprints in section 1, the clock, and the git heads. Not reused: Slack and Gmail collision coverage, thread rollups, JSON validity, date checks, Linear ordering, mirror equality and heading offsets, all rerun on the full rev11 SQL.

Intended `input_manifest.json` injection entry (not written, per the setup):

```json
{"review_version":"injection-static-v2","evidence_contract":"stage-evidence-v1","reused_evidence":[{"source_report":"review_rev10/out/0_injection.md","sha256":"67e1ab6fe77bf78e8f7010487272ed2a2ddf056f4a54d5ade27b6c486ecc7e0a","scope":"per-record source facts for 93 byte-identical statements","verified_unchanged":"statement bytes; source and reference fingerprints; clock; git heads"}],"sql_sha256":"1348d287ac4a105c41b9f0bf511c6664e306adcc3cf42406688a228fd4b684e7","universe":"synthcut"}
```

Any SQL change, including an advisory fix, invalidates the affected rows. Task discoverability, persona reach and Unique Ground Truth stay with `/prompt`.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (level not reported by the runtime)

Next action: Proceed to /prompt. Before that, consider ADV-2 (one sentence on L213), ADV-17 (one clause on L210) and ADV-18 (restore three Trello keys on L258). Any SQL edit needs a rerun of the affected rows.

Evidence limits: No required static check is unresolved. Outside this static scope: live execution and deployment; current database compatibility (the snapshot is unverified, 12 used columns are NOT COVERED, and the live schema file in the SQL header was not opened by instruction); search ranking and Agent visibility. Two facts cannot be settled from the export: what Douglas's Sep 30 prod update contained, and whether `state_history_json` needs updating for the five state changes (ZOM-344, ZOM-432, ZOM-542, ZOM-563, ZOM-566). Sprites are Git LFS pointers, so art claims were checked by file change, not by eye. My first command read `review_rev10` inputs before I read the new folder limit (section 2); the result does not depend on it. The report is saved in the review folder, not through `hg_write_output.py`, as the setup requires.
