# /injection — Injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review | `/injection`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. reused_evidence: unchanged rows only, taken from the prior `0_injection.md` (sha256 `078eccf5e73def575115694d2d07c2550049b75e4eb18342987c7669e877be0f`, §4 ledger and §6). See §3. |
| Actual review date | 2026-10-30 |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`, hg4-synth-sep30cut v16. `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`, the same as in the prior review |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, 82,412 bytes, sha256 `37a8c7ab3444732ff708fe4590c47f186c99f44d6de88e67699dc9590c4e5080` (input revision 4, attached to this /injection message as `01_Universe_Inject (2).sql`) |
| Prior SQL compared | revision 3, sha256 `b2576603…f5e51`. diff hunks: line 3 (header), +13–14 (Slides Drive file), 25–31 → 27–41 (Confluence replaced by GSlides), +50–51 (Arthur Slack message), 56 (Trello card rule 5), 60 and 62 (DD card and its action re-dated). Every other row is byte-identical. |
| Assignment (context only) | Julia Lawson, Product Manager; Product; Engineering Ops; Retrieval; long-horizon |
| References | WORKFLOW.md sha256 `ee4cd8e1…cd5d`; scoring.json `c14873e6…e5bc`; schema injection.json `31dcb2b4…5151` (unverified snapshot); `Evals/references/known_base_issues.md`. All unchanged from the prior review. |
| Lint | `hg_injection_lint.py` injection-lint-v1: 160 statements (BEGIN, 157 INSERT, 1 UPDATE, COMMIT), 158 rows, 0 unparsed. 0 FAIL / 0 CHECK / 0 INFO |

Manifest note: the review version, evidence contract, input hash and source provenance above take the place of the injection entry of `input_manifest.json`. This portal allows writes under `reports/` only through the report writer.

## 2. Input and authority issues

- The attached file differed from the saved revision 3, so it was saved as revision 4 before review.
- The SQL is substantive. All 160 statements parse, and an independent parse found 158 rows with no unparsed statements.
- No Confluence or Snowflake writes remain, so the authority conflict from the prior review no longer applies.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, base manifest, review version | NEW, done |
| Run lint; resolve every flag | NEW: 0 flags. Checks A–C done in full. |
| Inventory every statement and target | NEW for the changed and added rows. REUSED (prior report §4) for byte-identical rows. Full ledger in §4. |
| Check A: references, IDs, collisions | NEW for 13 changed/new rows, plus a fresh intra-SQL uniqueness check over all 158 rows. REUSED for unchanged rows. PASS |
| Check B: SQL structure, supported schema rules | NEW for the whole file (parse, JSON validity, generated columns, Linear formats, NOT NULL). PASS. Provisional advisories recorded. |
| Check C: dates, relationships, consistency | NEW for the changed rows and their links to the base. REUSED for unchanged rows. PASS |
| Coverage, findings, limits, one verdict | NEW, below |

Reuse basis (stage-evidence-v1): the reused rows are byte-identical in SQL. The base manifest, WORKFLOW, scoring and schema hashes and the fixed clock are unchanged. The new rows add only keys that do not collide with each other or with unchanged rows (fresh check: 0 duplicate keys across all 158 rows). The prior per-row results are carried below with their values and coverage. One prior statement is corrected here rather than reused: the claim that base Trello idShort "never runs against createCard order". A fresh ID-timestamp check finds 12 adjacent out-of-order pairs across the base boards. The conclusion no longer depends on it, because the re-dated card is now in order (see C).

## 4. Operation ledger

Lines refer to `01_Universe_Inject.sql` (revision 4). Base paths are relative to `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/`.

| Line(s) | Table / op | Record(s) | Key values checked | Base evidence | Verif. | Result |
|---|---|---|---|---|---|---|
| 5 / 331 | BEGIN / COMMIT | one transaction | all statements commit or roll back together | — | NEW | Structure OK |
| 8 | gdrive.drive_files INSERT | folder `d_96489e1e00a56685625939` "ZM Difficulty" | parent `d_63fffeb4fab5233ed5bb73` (Leonard's root); owner Leonard; Julia writer; created 2025-06-13 | parent exists (gdrive/data.json `/drive_files`, 53,631 rows, full load); id absent | NEW | PASS |
| 10 | gdrive.drive_files INSERT | doc `f_9ec79682ff351aa466364a` | in new folder; created 09-29 18:31Z, modified 09-30 11:04Z | id absent (full load) | NEW | PASS |
| 12 | gdrive.drive_files INSERT | sheet `f_0ba93ae0238d9ed4178212` | owner Julia; created 08-26, modified 09-02 | id absent (full load) | NEW | PASS |
| 14 | gdrive.drive_files INSERT | slides `f_048bf5e69f8e7f1a659a5c` "ZM dynamic difficulty - how tiers work" | mime presentation; parent `d_9f7ba94f7526d54d8482ba`; owner robert@; readers Julia, Leonard, Arthur, Brian; created = modified 2025-06-16T14:10:33Z | parent = folder "robert@harmonygames.co", owner robert@, root (no parents); id absent (full load). Base presentations (132) all have null content_path, with content served from gslides, which matches this row. | NEW | PASS |
| 17 | gdocs.docs_documents INSERT | `f_9ec79682ff351aa466364a` | body_text non-empty (readable doc); style runs 0–29 / 29–431 | no collision (prior §4 line 14) | REUSED | PASS |
| 20 | gsheets.sheets_spreadsheets INSERT | `f_0ba93ae0238d9ed4178212` | drive_file_id matches; dates match drive row | no collision (prior §4 line 17) | REUSED | PASS |
| 22, 24, 26 | gsheets.sheets_sheets INSERT ×3 | tabs 0 Live / 1 Next pass / 2 History | grid_json valid JSON list of rows | prior §4 lines 19–23 | REUSED | PASS |
| 29 | gslides.slides_presentations INSERT | `f_048bf5e69f8e7f1a659a5c` | drive_file_id = presentation_id, as in base; owner, sharing and dates match the line-14 Drive row; revision_id `048bf5e69f` | presentation_id absent from all 132 base presentations (gslides/data.json, full load) | NEW | PASS (revision_id has no ID contract) |
| 31, 35, 39 | gslides.slides_pages INSERT ×3 | `slide_cb43e6c53c57`, `slide_7329e157cabf`, `slide_fc10746fe8c2`, index 0/1/2, BLANK | format `slide_` + 12 hex, as in the base | absent from all 2,309 base pages | NEW | PASS (advisory A2: `notes` column) |
| 33, 37, 41 | gslides.slides_page_elements INSERT ×3 | `el_bf0658751368`, `el_d0979892e11a`, `el_0573925c4c2c`, TEXT_BOX, full-slide geometry 9144000×5143500 | page_object_id each matches its page; format `el_` + 12 hex | absent from all 2,231 base elements; kind and geometry match the base | NEW | PASS (advisory A2: `table_json`, `ordinal`) |
| 44 | slack.slack_messages INSERT | `6f77386571537f0bd88c959bdc216f94` DM `D05HB64NMQU` | Leonard → Julia; ts 1759261706 = 2025-09-30T19:48:26Z | id absent (full lookup, below) | NEW id / REUSED membership (prior §4 line 33) | PASS |
| 46 | slack.slack_messages INSERT | `84ff828e…` #zombie-design | Brian, 2025-09-29T22:31:17Z | id absent; channel member (prior) | NEW id / REUSED | PASS (stale claim, see C) |
| 48 | slack.slack_messages INSERT | `0282d920…` #zombie-design | Vincent, 2025-09-30T16:12:40Z | id absent; member | NEW id / REUSED | PASS |
| 50 | slack.slack_messages INSERT | `6995ba10acf2888f04f033b8bbeb5629` #zombie-design `C090N54TG79` | Arthur (`EMPLOYEE_0025_SLACK_ID`); ts 1756912929.304417 = created_at 2025-09-03T15:22:09.304417Z; top-level; metadata `{}` | id absent (lookup over 4,840 files / 610,468 messages, scan_complete). ts not in any of the channel's 4 month files. Arthur is in the channel's 10 members (slack/channels.json) and posted 29 base messages there, including 1756916734 (Sep 3, 16:25Z). Channel created 1749707858 (2025-06-12). | NEW | PASS |
| 52 | slack.slack_messages INSERT | `5313e8da…` #zombie-prs bot reply to `1c181040…` | reply ts 1756141351 (2025-08-25T17:02:31Z) | parent found at messages/C093LEZGF6J/2025-08.json `/439`; id absent | NEW id / REUSED | PASS |
| 53 | slack.slack_messages UPDATE | parent `1c181040768a5650a30ad1e68cf1b9b4` | reply_count 2→3, latest_reply → the new reply | parent exists (lookup); prior §4 line 41 | NEW existence / REUSED | PASS |
| 56 | trello.trello_cards INSERT | `68daca5871dba40417a00383` "Difficulty baseline (Julia)", ZM ROADMAP, list "Oct 21", idShort 80 | rule 5 now reads "written up in Robert's dynamic difficulty deck and in ZOM-42 itself" | id and shortLink IDdFKb6g absent (trello/data.json, full load). Rule 5 points at the line-14/29 deck: owner Robert, shared with Julia, created 06-16, which is before the card's 09-29 createCard. | NEW | PASS |
| 58 | trello.trello_actions INSERT | `68daca5845e48874fb98e25a` createCard 2025-09-29T18:05:12Z | creator `PERSON_6094_TRELLO_USER_ID` = Leonard Hayes | id absent | NEW | PASS |
| 60 | trello.trello_cards INSERT | `683dbef4e319167a802bd888` "Difficulty baseline", DD board `65eb4ec525346c8070ca638f`, list `65eb4f4e26cfce07d665a38e` "Rebirth (June)", idShort 211 | ID timestamp 0x683dbef4 = 2025-06-02T15:10:44Z = dateLastActivity = createCard date | Card id and shortLink YsDcEVy2 absent. List exists on this board and is open. Board max idShort is 210; #211 is free. #210 was created 2025-05-27T14:57:29Z (last base createCard on the board), and no base card on the board was created after 2025-06-02, so 211 is the next number in creation order. | NEW | PASS (advisory A3: list choice) |
| 62 | trello.trello_actions INSERT | `683dbef4991df7f0987ddb73` createCard 2025-06-02T15:10:44Z | board name "Product Roadmap" and shortLink Yg3yTuCR; card idShort 211 and shortLink match line 60; list id and name match | id absent; creator Leonard Hayes | NEW | PASS |
| 64 | trello.trello_actions INSERT | `68dbfa4362a051efb5e0ae45` commentCard 2025-09-30T15:41:55Z | = card dateLastActivity; badges comments 1 | id absent | NEW | PASS |
| 67–85 | gmail.gmail_threads ×5 + gmail_messages ×5 | "store builds for monday", Arthur → Julia, Leonard, Robert, Brian; 2025-09-30T09:12:44Z | internal_date 1759223564000 matches | all 5 mailboxes exist. IDs absent from all 81,404 thread files (prior §4 lines 54–72). | REUSED | PASS |
| 86–95 | gmail.gmail_messages ×5 | "Re: store builds for monday", 13:26:05Z; In-Reply-To/References → first Message-ID | reply after parent; quoted "2:12 AM" = 09:12Z in PDT | prior §4 lines 74–82 | REUSED | PASS |
| 97–106 | gcal.gcal_events ×5 | "ZM difficulty tuning", 2025-10-06 17:00–18:00Z (plan field); created 09-29T18:24:51Z; shared ical_uid | calendars exist; IDs not in base | prior §4 lines 85–93 | REUSED | PASS |
| 109 | github.github_pr_comments INSERT | `harmonygames-Games/match3d#401#c_2` | EMPLOYEE_0025; 2025-08-25T17:02:28Z, after merge 16:42:14Z | prior §4 line 96 | REUSED | PASS |
| 111 | github.github_timeline_events INSERT | `…#401#ev_7` commented | same actor and time | prior §4 line 98 | REUSED | PASS |
| 113–330 | linear.linear_comments INSERT ×109 | `cmt_*` on ZOM-23 … ZOM-495 | formats `YYYY-MM-DDTHH:MM:SSZ`; NOT NULL columns present | Base Linear has 0 comments, so no collision is possible. 109 IDs unique. All issues and the 7 authors exist. Per-issue chronology and cited PRs checked (prior §4 lines 101–317 and the paragraph after it). | REUSED | PASS (advisory A1) |

## 5. Lint flags and resolutions

| Flag | Resolution |
|---|---|
| (none) | 0 FAIL / 0 CHECK / 0 INFO. The lint's drive_unreadable check recognises the Slides file through its gslides rows. Checks A–C were still run in full. |

## 6. Checks A–C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A: Records, references and IDs | **PASS** | All new references resolve: the Slides parent is Robert's root folder, the slides pages and elements link to their presentation, Arthur's Slack user exists and is a #zombie-design member, the DD card's list is on its board, and the Trello creator is Leonard Hayes. No new key collides. Coverage: Slack lookup over 610,468 messages; GDrive 53,631 files; GSlides 132 presentations / 2,309 pages / 2,231 elements; Trello cards, shortLinks and actions, all full loads. Intra-SQL: 0 duplicate keys over 158 rows. Trello rule 5 now points at an injectable record that exists in the overlay (the deck), which resolves the prior broken Confluence reference. The new Slides file is readable through gslides content, like the 132 base presentations. Unchanged rows reuse prior results. |
| B: SQL structure and supported schema rules | **PASS** | All 160 statements parse. Every `*_json` literal is valid JSON with the base shape (slack metadata `{}`, list fields `[]`). No generated column is written (`text_fts` and `body_text_fts` are absent). Linear dates use the base format. NOT NULL columns are present. The UPDATE targets one existing row. No Confluence or Snowflake writes. Provisional snapshot comparison: MATCH for gdrive, gdocs, gsheets, slack, trello, gmail, gcal, github and gslides presentations. MISMATCH (advisory): `gslides.slides_pages.notes`, `gslides.slides_page_elements.table_json` and `ordinal` (A2), and `linear.linear_comments.sequence` (A1). None appear in the snapshot or the base export shape. |
| C: Dates, relationships and consistency | **PASS** | Every event timestamp is ≤ 2025-10-01T07:00Z. The only later value is the Oct 6 meeting, which is a plan field. DD card #211 is now created 2025-06-02, after #210 (2025-05-27) and with no later base card, so the prior chronology defect is fixed. The deck (06-16) matches the base at its date: ZOM-42 says promotion at 80%+ of the last 10 attempts, one win promotes from tier -2, and 4 losses in a row demote. ZOM-199 (06-01) says ">= 90" for tier 1. ZOM-254 (06-12) gives +25% speed, damage and max HP. The deck's blunder slide is superseded by ZOM-282 (06-19) and PR #401 (merged 2025-08-25T16:42Z). Arthur's Sep 3 Slack correction ("split since match3d#401, hp doesn't change, values per monster. julia keeps the numbers") comes after #401, and the "julia keeps the numbers" part fits Julia's sheet (created 08-26, Live set 09-02). Arthur's Sep 30 email corrects the starting-tier boundary to "> 90", which matches ZOM-42. These are allowed stale and corrected records. No grader-facing text appears in the new rows (slides text, Slack text, card rule 5). Unchanged rows reuse prior consistency results. |

## 7. Findings

No FAIL findings.

Prior findings resolved:
- F1 (Confluence rows) is resolved. The three `confluence.*` INSERTs were removed. The tier write-up is now a Slides deck owned by Robert (lines 14, 29–41), Arthur's correction is a #zombie-design Slack message (line 50), and Trello rule 5 points at the deck (line 56).
- F2 (Trello idShort order) is resolved. The card is now `683dbef4e319167a802bd888`, created 2025-06-02T15:10:44Z with consistent ID timestamps, action date and dateLastActivity, after #210.

**Advisories (not failures):**
- A1. `linear.linear_comments.sequence` (109 rows) is not in the unverified snapshot. Base Linear has no comments to show the live shape. If the live table lacks this column, the single transaction rolls back. Dropping it is the safe choice unless you have seen it load.
- A2. The same risk applies to `gslides.slides_pages.notes` (all NULL) and `gslides.slides_page_elements.table_json` (all NULL) and `ordinal` (all 0). They are absent from both the snapshot and the base gslides export, whose pages have only object_id/index/layout/elements and whose elements have only the 8 snapshot fields. Dropping these three columns costs nothing, since every value is NULL or 0.
- A3. The DD decoy card sits in "Rebirth (June)". That is the June 2024 release list: its other 18 cards were created 2024-03-08 → 2024-06-03, and 2025 work is in lists like "July (Cheesecake)", "(Pupusa)" and "(Grogu)". Filing a June 2025 card there is odd but not a contradiction. A 2025 list or "Backlog" would read more naturally.
- A4. Carried from the prior review, unchanged: comments on Todo issues dated after the issue's `updated_at` (ZOM-400, 427, 438, 439, 441, 443, 458, 468); "wip on a branch" on ZOM-202/311 with no GitHub branch; the gdocs `revision_id` style; the sheet History "0.6 -> 0.8" entry extending the base record. None is a defect.
- Base-data check: none of the listed synth-cut conflicts (SC-1 to SC-3) touch this SQL.

## 8. Next action and downstream

Proceed to `/prompt`. Optionally drop the unverified columns (A1, A2) before running the task. If you change the SQL, rerun `/injection`. Any earlier `/prompt`, `/hardness`, `/oe` or `/rubric` result that read the previous SQL is outdated and must be rerun.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt. Optionally drop `linear_comments.sequence`, `slides_pages.notes` and `slides_page_elements.table_json`/`ordinal` first, then rerun /injection.

Evidence limits: Static review only. No SQL was executed, and live database compatibility is not certified. The injection schema snapshot is unverified, and four inserted columns (A1, A2) are not covered by it. Rows byte-identical to revision 3 reuse the prior review's per-row checks under stage-evidence-v1, including its Gmail collision coverage by fixed-string grep over all 81,404 thread files.
