# /injection: injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review | `/injection`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. reused_evidence: rows byte-identical to revision 22 keep the prior `0_injection.md` results (§4 ledger and §6 of the r22 report, which carry per-row provenance back through revisions 20, 17, 14, 12, 11, 9 and earlier). Line numbers are remapped below. See §3. |
| Actual review date | 2026-10-31T05:48Z (UTC) |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`, hg4-synth-sep30cut v16. `universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`, unchanged |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, 94,599 bytes, 358 physical lines, sha256 `2ee488e28ab5b13fb02eb3d32ca292b93362bc1decd424856f140ffe5a221e6a` (input revision 25, attached as `01_Universe_Inject (13).sql`) |
| Prior SQL compared | revision 22, sha256 `52c581f4…a43` (upload `(12)`, PASS). `diff`: header line 3 (counts), **6 new INSERTs** (Drive file + Google Doc "notes for monday", Slack GitHub-bot thread reply, Trello attachment, GitHub review + review comment on PR #265), **1 new UPDATE** (Slack parent reply_count 12→13), and **2 changed rows** (card `desc` + `badges_json`, updateCard `data.card.desc`). Every other row is byte-identical. |
| Line remap (old → new) | 1–11 → 1–11; 12–17 → 14–19; 18–55 → 22–59; 58 → 65; 56–76 (other) → 63–83; 77–123 → 86–132; 124–345 → 137–358. New rows: 11–12, 20–21, 60–62, 84–85, 133–136. |
| Assignment (context only) | Julia Lawson, Product Manager; Product; Engineering Ops; Retrieval; long-horizon |
| References | WORKFLOW.md `ee4cd8e1…cd5d`; Eval 0 `e034019b…3eff`; known_base_issues.md `79b20289…3a7b`; schema/injection.json `31dcb2b4…5151` (unverified snapshot); id_contracts.json `fc4711ef…4682`; ENVIRONMENT.md `4ffb2b5f…e165`; SEARCH.md `cab83c61…a45c`; lint `a8226e2a…448b`. All re-hashed and unchanged from the prior review. |
| Lint | `hg_injection_lint.py` (injection-lint-v1) on sha256 `2ee488e2…6a`: 174 statements (BEGIN, 170 INSERT, 2 UPDATE, COMMIT); 0 FAIL / 0 CHECK / 0 INFO |

Manifest note: the review version, evidence contract, input hash and source provenance above stand in for the injection entry of `input_manifest.json` (`review_version: injection-static-v2`). This portal allows writes under `reports/` only through the report writer.

## 2. Input and authority issues

- The attached file differed from saved revision 22, so it was saved as revision 25 of the injection input before review.
- The SQL is substantive and parses in full. It makes no Confluence or Snowflake writes.
- Line numbers are physical (`\n`) lines. The 10 lines that contain bare CR bytes (Gmail bodies, lines 88–116) are unchanged from r22.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, base manifest, review version | NEW, done |
| Run lint; resolve every flag | NEW: 0 flags. Checks A–C still run below. |
| Inventory every statement and target | NEW for the 9 new or changed rows and the header. REUSED (r22 report §4) for byte-identical rows, with lines remapped (§1). Spot-checked the remap at lines 41, 58, 59, 73, 75, 83, 88, 116, 119, 127, 130, 132, 139, 239, 357 and 358. |
| Check A: references, IDs, collisions | NEW complete scans for every new key, plus parent/actor resolution. REUSED complete collision results for unchanged keys. PASS |
| Check B: SQL structure, supported schema rules | NEW whole-file parse (lint), plus a NEW column/value count and JSON parse for every new or changed row. PASS (advisory G1) |
| Check C: dates, relationships, consistency | NEW for the new records and the changed card text. PASS |
| Coverage, findings, limits, one verdict | NEW, below |

Reuse basis (stage-evidence-v1): reused rows are byte-identical in the SQL. The base manifest, WORKFLOW, Eval 0, known_base_issues, schema snapshot, id contracts and fixed clock are unchanged. The new rows add keys (checked fresh below) but change no existing key, timestamp or reference, so the earlier collision and chronology results still hold.

## 4. Operation ledger

Lines refer to `01_Universe_Inject.sql` (revision 25).

| Line(s) | Table / op | Record(s) | Key values checked | Base evidence | Verif. | Result |
|---|---|---|---|---|---|---|
| 3 | comment | header | "170 INSERT (one row each), 2 UPDATE" | lint: 170 INSERT, 2 UPDATE | NEW | PASS (accurate; comments are not data) |
| 5 / 358 | BEGIN / COMMIT | one transaction | all statements commit or roll back together | — | NEW (lint) | Structure OK |
| 8, 10, 14, 16 | gdrive.drive_files ×4 | folder "ZM Difficulty", agenda doc, enrage sheet, tiers deck | unchanged | r22 §4 (old 8–14) | REUSED | PASS |
| **12** | gdrive.drive_files INSERT (**new**) | `f_f494073fc667097c3c2c6b` "notes for monday", Google Doc | 13/13 cols/values. Parent `d_63fffeb4fab5233ed5bb73`, owner Leonard Hayes, shared with Julia (reader), private. Created 2025-09-30T15:47:03Z, modified 15:51:58Z | gdrive `data.json` `/drive_files`: id absent (53,631 records, complete). Parent exists: Leonard's root folder (`name` = leonard.hayes@harmonygames.co, owner Leonard, folder mime) | NEW | PASS |
| 19 | gdocs.docs_documents | agenda `f_9ec79682…` | unchanged | r22 §4 (old 17) | REUSED | PASS |
| **21** | gdocs.docs_documents INSERT (**new**) | `f_f494073fc667097c3c2c6b` | 11/11. body_text non-empty (399 chars); style runs 0–17 (title "notes for monday" + `\n`) and 17–399 match the body length, the same convention as the agenda doc (0–29 / 29–431, 431 chars). Owner/sharing/times equal the Drive row; `drive_file_id` = Drive id | gdocs `/docs_documents`: document_id absent (595 records, complete). Readable-Drive-file rule met (Doc with non-empty body_text) | NEW | PASS |
| 24–30 | gsheets spreadsheet + 3 sheets | `f_0ba93ae0…` | unchanged | r22 §4 (old 20–26) | REUSED | PASS |
| 33–45 | gslides presentation, pages, elements | `f_048bf5e6…` (line 41 tier text) | unchanged | r22 §4 (old 29–41) | REUSED | PASS (A2) |
| 48–56 | slack.slack_messages ×5 | Leonard DM, Brian, Vincent, Leonard reply, Arthur | unchanged | r22 §4 (old 44–52) | REUSED | PASS |
| 58 / 59 | slack bot reply + parent UPDATE | `5313e8da…`, `1c181040…` | unchanged | r22 §4 (old 54/55) | REUSED | PASS |
| **61** | slack.slack_messages INSERT (**new**) | `1491582caca6e2769404e7b09eac3d55`, ts `1751565015.214669` (2025-07-03T17:50:15Z), `C093LEZGF6J`, SLACK_BOT_0004, thread reply to `6a42cb69…` | 18/18. `attachments_json` list, `metadata_json` `{}`, `reactions_json`/`files_json` `[]`; `text_fts` not set. Attachment: fallback "Comment on #265", pretext `…pull/265#discussion_r2183514406\|Comment> on pull request by …arthur.blake`, text = GitHub rc_7 body, title `#265 ZOM-312`, attachment ts 1751565012 (17:50:12Z = rc_7 created_at) | Slack `messages/*.json`: id absent (4,840 files, 610,468 records, complete); no other message in `C093LEZGF6J/2025-07.json` has this ts. The format matches the base reply `36adbf73…` field for field (Arthur's "Yes." comment). discussion id `r2183514406` > the last base id in the thread, `r2183357987` (17:35:02Z), and appears once in the SQL | NEW | PASS |
| **62** | slack UPDATE (**new**) | parent `6a42cb69b452e0c89f36407f56a3d84b` reply_count 12→13 | Base parent: reply_count 12, reply_users_count 1 (bot), latest_reply `1751565699.130039` (18:01:39Z merge notice) | Base thread has exactly 12 replies (listed). The new reply (17:50:15Z) is before latest_reply, so latest_reply and reply_users_count correctly stay unchanged | NEW | PASS |
| **65** | trello.trello_cards (**changed**) | `68daca5871dba40417a00383` | Two edits: rule 1 adds "It works the other way too: a title match Blake marked 'not tiers' in his review on its PR stays off."; `badges_json.attachments` 0→1. 18/18; badges parses as an object; id, list, `dateLastActivity` 16:20:11Z unchanged | Decoded desc 2,481 chars, equal to line 73 `card.desc`. One attachment row (line 85) is on this card; base `/attachments` has none for this card (76 records, complete) | NEW | PASS |
| 67, 69, 71 | trello createCard, DD card #211, createCard | unchanged | r22 §4 (old 60–64) | REUSED | PASS (A3) |
| **73** | trello updateCard 14:04:31Z (**changed**) | `68dbe36f4b2b4fffb7525fde` | 7/7. `data_json` parses as an object; `card.desc` = line 65 desc; `old.desc` unchanged | — | NEW | PASS |
| 75 | trello commentCard 15:41:55Z | `68dbfa43…` | unchanged | r22 §4 (old 68) | REUSED | PASS |
| 77 / 79 / 81 / 83 | checklist, 2 check items, addChecklistToCard 16:20:11Z | `68dc033b…` | unchanged | r22 §4 (old 70–76) | REUSED | PASS |
| **85** | trello.trello_attachments INSERT (**new**) | `68dbfcc8aa008dbd8cccea3e` "notes for monday" on card `68daca58…` | 10/10. url `https://docs.google.com/document/d/f_f494073fc667097c3c2c6b/edit` (= line 12 id), isUpload false, bytes/rel_path NULL, idMember PERSON_6094, date 2025-09-30T15:52:40Z | Trello `/attachments`: id absent (76 records, complete). PERSON_6094 = Leonard Hayes (`/members`). Same shape as base link attachment `/attachments/75` (Leonard, Google Docs URL, isUpload false, bytes/rel_path null; base `mimeType` is `""`, here NULL) | NEW | PASS (G3) |
| 88–116 | gmail threads ×5 + messages ×10 | unchanged | r22 §4 (old 79–107) | REUSED | PASS |
| 119–127 | gcal.gcal_events ×5 | unchanged | r22 §4 (old 110–118) | REUSED | PASS |
| 130 / 132 | github PR #401 comment + timeline event | unchanged | r22 §4 (old 121/123) | REUSED | PASS (A5) |
| **134** | github.github_reviews INSERT (**new**) | `harmonygames-Games/match3d#265#rev_8`, Arthur (EMPLOYEE_0025), COMMENTED, empty body, submitted 2025-07-03T17:50:12Z, commit `28cc6fa1…`, seq 8 | 8/8 cols/values | GitHub `/reviews`: id absent (2,230 records, complete). PR #265 has base rev_1–rev_7, so rev_8 is next. EMPLOYEE_0025 = Arthur Blake (`/users`). The PR exists (`/pull_requests`: "ZOM-312", merged by owen.baker 18:01:36Z). Commit `28cc6fa1…` is the PR head and its `pull_request_commits` position 2. Arthur's base reviews rev_3/rev_5 are also COMMENTED with an empty body | NEW | PASS (G1) |
| **136** | github.github_review_comments INSERT (**new**) | `…#265#rc_7`, Arthur, body "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work", path `Assets/Scripts/LevelEditor/UI/LevelSettings.cs`, line 116, RIGHT/line, review `#rev_8`, created 17:50:12Z, seq 7 | 15/15 | `/review_comments`: id absent (1,387 records, complete); base rc_1–rc_6, so rc_7 is next. The diff_hunk is byte-identical (1,021 chars) to base rc_3's hunk on the same path. Line 116 is `DeleteDifficultyClicked()` in that hunk, matching the base "LevelSettings.cs:116-136" | NEW | PASS (G1, G2) |
| 139–357 | linear.linear_comments ×110 | `cmt_*` on ZOM-23 … ZOM-495 (ZOM-281 `tiers:` note at line 239; ZOM-312 closing note at line 275; ZOM-258 at old 291 → 304) | unchanged | r22 §4 (old 126–344) | REUSED | PASS (A1, A4) |

## 5. Lint flags and resolutions

| Flag | Resolution |
|---|---|
| (none) | 0 FAIL / 0 CHECK / 0 INFO. Checks A–C still run below. |

## 6. Checks A–C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A: Records, references and IDs | **PASS** | **New keys**, all absent from complete base scans and each defined once in the SQL: Drive/Docs `f_f494073fc667097c3c2c6b` (its 4 occurrences are the id, document_id, drive_file_id and the attachment URL); Slack `1491582c…` (all 4,840 message files); Trello attachment `68dbfcc8…`; GitHub `#265#rev_8` and `#265#rc_7` (`rev_8` also appears as rc_7's `pull_request_review_id`, a valid foreign reference). Docs `revision_id` `ec74a426a2` is unique in the SQL. **References:** Drive parent (Leonard's root folder), owner and sharer emails; Slack parent `6a42cb69…` and channel `C093LEZGF6J`; Trello card `68daca58…` (in SQL) and member PERSON_6094 = Leonard; GitHub PR #265, commit `28cc6fa1…` (PR head) and author EMPLOYEE_0025 = Arthur Blake (arthur.blake@harmonygames.co). **One account per person:** "Blake" in the card and review is Arthur Blake, the same person as Linear `usr_cc3e90160f490686` (arthur.blake@, assignee/creator of ZOM-312) and the Gmail sender. No second account. **ID contracts:** no Gmail history_id or Drive content_path in the new rows (the new file is a native Google Doc served from docs_documents). Unchanged keys keep their earlier complete collision results. |
| B: SQL structure and supported schema rules | **PASS** | All 174 statements parse (lint). Hand counts for every new or changed row: drive_files 13/13, docs_documents 11/11, slack_messages 18/18, trello_cards 18/18, trello_actions 7/7, trello_attachments 10/10, github_reviews 8/8, github_review_comments 15/15. Every `*_json` text in these rows parses with the snapshot's shape (lists, Slack `metadata_json` `{}`, card `badges_json` object, action `data_json` object). No generated column (`text_fts`) is set, and no Linear date field is new. **Provisional snapshot comparison (advisory G1):** `github_reviews.seq` and `github_review_comments.seq`, `pull_request_review_id`, `side` and `subject_type` are NOT COVERED by the snapshot (and absent from the base export). Under Eval 0 a snapshot mismatch alone is advisory. The snapshot is already known to be incomplete: `linear_comments.sequence` is also off-snapshot, yet the r22-era Opus run shows injected records loaded ("Difficulty baseline (Julia)" and 57 `tiers:` hits in the saved trajectory). |
| C: Dates, relationships and consistency | **PASS** | **Clock:** every new event time is before 2025-10-01 07:00Z (latest 2025-09-30T15:52:40Z). **Chronology:** PR #265 opened 12:41:57Z; Arthur's base reviews 16:05:36 and 17:34:34; CodeRabbit 17:35:00; **rev_8/rc_7 17:50:12Z**; approval 18:01:21; merge 18:01:36Z. The review falls inside the open window. Slack mirror 17:50:15Z (3 s after, the same lag as base replies), before the 18:01:22/18:01:39 notices. Doc created 15:47:03, modified 15:51:58, attached 15:52:40, all after the card update (14:04:31) and comment (15:41:55) and before the checklist (16:20:11) and the card's `dateLastActivity` (16:20:11). **Facts:** ZOM-312 "Delete Difficulty Tier and Reassign" (Done, created 2025-06-26, before Aug 31) is a title match (Difficulty, Tier). The review's "level settings tooling for the designers, players never see it" agrees with the PR (LevelEditor UI, "Delete difficulties") and with the existing closing note at line 275 ("delete and reassign live in the level settings panel"), which does not start with `tiers:`. So the new rule 1 sentence and the review agree, and no record marks ZOM-312 as tier work. The doc's "ZOM-258 … only the icon players see over a monster" matches ZOM-258 "Icon for Enraged monster" (VFX label, hover icon). Its only SQL comment (Marcus Bennett, "checked on the dev build") is not a `tiers:` note. "arthur is only listening in on monday, view access is enough" is a later instruction from the session owner that narrows rule 7's "everyone else comments" for one attendee. It is dated after the card text and contradicts no factual record. "register first … then the rules tab, then rage by level" matches the agenda doc order (line 19). **Grader-facing text:** none. The new texts are a persona's notes, a GitHub review and a bot mirror. **Base-data conflicts:** SC-1 to SC-3 untouched, and there are no Snowflake or Confluence writes. |

## 7. Findings

No demonstrated defects and no unresolved required checks.

**Advisories (not failures):**
- **G1 (new), compatibility limit:** the two GitHub inserts use `seq`, `pull_request_review_id`, `side` and `subject_type`, which are not in the schema snapshot or the base export. If the live tables lacked any of them, that INSERT would error and the whole BEGIN/COMMIT block would roll back. That would be visible in the next run as none of the injected records appearing. Nothing here proves a mismatch, and the snapshot is demonstrably incomplete (see Check B). After the next run, confirm that injected records (for example the "notes for monday" doc) are present.
- **G2 (new), cosmetic:** rc_7 sets `line` 116 and `commit_id`, while the base comments on PR #265 have both null. This is valid data, not a defect.
- **G3 (new), cosmetic:** no `addAttachmentToCard` action accompanies the attachment. Base has 48 such actions for 76 attachments, so not every attachment has one. `mimeType` is NULL here and `""` in the comparable base link attachment.
- **D4 (new), downstream for /prompt, /oe and /rubric:** Leonard's "notes for monday" doc (attached to the card, shared only with Julia, in Leonard's root Drive folder) adds three instructions. (1) Exclude ZOM-258, a title match on "Enraged" that no PR review marks "not tiers". Its only exclusion source is this doc. (2) Give Arthur view access instead of comment, overriding rule 7's "everyone else comments" (Robert edit and Brian edit via the checklist still stand). (3) The reply to Leonard must say which ticket replaced which. These stages should reflect all three, and /prompt should confirm the doc is discoverable from Julia's view (card attachment and Drive share).
- **D5 (new), downstream:** the reverse rule ("a title match Blake marked 'not tiers' in his review on its PR stays off") now depends on a GitHub review comment on PR #265, mirrored in Slack `C093LEZGF6J`. The only such mark in the SQL is on ZOM-312, so ZOM-312 is out of the register. /prompt should confirm Julia can reach either the PR review or the Slack mirror. /oe and /rubric should expect ZOM-312 to be excluded.
- **D2, D3, D1 and the r17 notes carried** (build timing for the starting tier has no build-side statement; "write it the way ZOM-42 words it" for promotion/demotion windows; ZOM-281 enters only via the `tiers:` note; instruction layers card → checklist → DM reply, now plus the notes doc).
- A1–A5 carried unchanged.

## 8. Next action and downstream

Proceed to `/prompt`. Because the SQL changed, every earlier pass that read it is outdated. Rerun `/prompt`, `/hardness`, `/oe` and `/rubric` in that order.

Stage dependencies for reuse: this result depends on SQL sha256 `2ee488e2…6a`, synth-cut manifest `da2f4cf0…ac1a`, GitHub `data.json` (`/reviews`, `/review_comments`, `/pull_requests`, `/pull_request_comments`, `/timeline_events`, `/pull_request_commits`, `/users`), GDrive `data.json` `/drive_files`, GDocs `data.json` `/docs_documents`, Trello `data.json` (`/attachments`, `/members`, `/actions`), Slack `messages/*.json` (id scan) and `messages/C093LEZGF6J/2025-07.json` (thread), Linear `data.json` (`/issues`, `/users`, `/comments`), and the reference hashes in §1.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness, /oe and /rubric, since the SQL changed.

Evidence limits: Static review only. No SQL was executed, and live database compatibility and Agent visibility are not certified. The schema snapshot is unverified. The new GitHub columns are not covered by it (G1), and A1/A2 are carried. Rows byte-identical to revision 22 reuse the prior review's per-row checks under stage-evidence-v1, and every new key had a fresh complete collision scan.
