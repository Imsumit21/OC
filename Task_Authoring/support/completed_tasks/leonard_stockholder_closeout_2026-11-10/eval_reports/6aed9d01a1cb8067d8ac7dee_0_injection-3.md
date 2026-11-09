# Injection Data-Integrity Review (Eval 0)

- Review version: `injection-static-v2`
- Evidence contract: `stage-evidence-v1` (reused_evidence: none; every check below is NEW for this SQL version)
- Mode: chat/attachment review, attempt 6aed9d01a1cb8067d8ac7dee
- Actual review time: 2026-11-08T15:07Z
- Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
- Universe: `Universe_Normal` (source hg4-2026-08-31 v37); manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450`
- Input: `Evals/task_inputs/01_Universe_Inject.sql`, 111,997 bytes, sha256 `9b02cc8f34a91f69c6faf607f5578d25b52e10c6115a0cddf99a180f4d8b5bfb` (input-store revision 6, from attachment `01_Universe_Inject (2).sql`; replaces revision 3, sha256 `bc72db9c31e9982751e47762f94939c7c5367ee7979830e28acb55627b957f2d`)
- References: schema snapshot `Evals/references/schema/injection.json` sha256 `31dcb2b43feca8e5c7cb67f37973f819c9b9774f12f8b15cb7da89ecd74c5151` (unverified/provisional); ID contracts `Evals/references/schema/id_contracts.json` sha256 `fc4711ef07667333c1cf2a417279826f0432539195f7acdfacfa86e9d9ed4682`; lint `injection-lint-v1`
- Evaluator: Opus 5.5 (claude-opus-5-5), session effort

## Input / authority issues

- New SQL version supplied with this command and saved as the current injection input. The previous `/injection` PASS covered the older 74,125-byte version only and is not reused.
- SQL comments are section headers only (`-- ===== GDRIVE =====` etc.); no padding/test comments.
- No Snowflake or Confluence records are touched.

## Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, manifest, review version | DONE (NEW) |
| Run `hg_injection_lint.py`; resolve every flag | DONE (NEW): 0 FAIL / 0 CHECK / 0 INFO |
| Inventory every statement and record | DONE (NEW): 149 statements (BEGIN, 132 INSERT, 15 UPDATE, COMMIT) |
| Check A: references, collisions, ID contracts, Drive readability, one account per person | PASS (NEW) |
| Check B: SQL structure and supported schema rules | PASS with provisional snapshot advisory (NEW) |
| Check C: dates, relationships, consistency | PASS (NEW) |
| Report coverage, findings, limits, one verdict | DONE |

## Lint flags and resolutions

`hg_injection_lint.py` (sha of SQL matches): statements 149; rows by table as in the ledger; base files loaded: contacts, slack/users, trello, gmail/users, linear, confluence_working. Flags: **none** (FAIL 0, CHECK 0, INFO 0). Clean lint did not replace checks A–C below.

## Operation ledger (execution order)

Coverage tools: `hg_records.py` (two requests; all checks `scan_complete: true` except the Gmail thread-id check, which was redone with `search-many --key id` over all 88,726 thread files, complete); `lookup`/`search-many`/`get-many`; streaming scripts over all Gmail thread files for header-address dates.

| SQL lines | Table | Op | Record(s) | Key checks / result |
|---|---|---|---|---|
| 1 | — | BEGIN | single transaction | ends with COMMIT (291) |
| 3–4 | gdrive.drive_files | INSERT | `d_601064334a0b493022fe83` folder "Stockholder close-out" | id unused (53,866 files checked); parent `d_63fffeb4fab5233ed5bb73` = Leonard's root folder (exists); created 2026-02-12T23:20:37Z ≤ modified 02-13T01:05:41Z ≤ clock |
| 5–6 | gdrive.drive_files | INSERT | `f_a37b403d5200d4f0a31d31` Doc "Stockholder close-out notes" | unused id; readable via gdocs row (line 15) |
| 7–8 | gdrive.drive_files | INSERT | `f_762c60832854d3e7a7f7df` Doc "Holder outreach notes" (root) | unused; gdocs row (line 17) |
| 9–10 | gdrive.drive_files | INSERT | `f_5ecaa967db3adcfa440b09` Sheet "Holder list (draft)" | unused; gsheets rows (19–22) |
| 11–12 | gdrive.drive_files | INSERT | `f_75dddccabb26eeea4842c8` Slides "Harmony Games February 26 Update" | unused; gslides rows (24–45) |
| 14–17 | gdocs.docs_documents | INSERT ×2 | `f_a37b…`, `f_762c…` | ids unused (633 docs); body non-empty; style runs end at body length (2146; 290) and title runs end at len(title)+1 (28; 22) |
| 19–22 | gsheets.sheets_spreadsheets / sheets_sheets | INSERT ×2 | `f_5eca…`, sheet 0 | id unused (398); grid_json valid array; 7 holder rows match the Nov 2024 owner list values |
| 24–45 | gslides presentations / pages ×5 / elements ×5 | INSERT ×11 | `f_75dd…`, slide_*/el_* ids | presentation id unused (164); page/element ids new within this presentation |
| 47–48 | slack.slack_messages | INSERT | `846a70ba…1734` ts 1768418331.402719, #executives `C07C2866011`, reply to `b658ec71…` | id/ts unused (687,230 msgs); parent exists (Leonard, ts 1768417784.194359, 0 base replies); author Leonard `EMPLOYEE_0038_SLACK_ID` is a channel member; ts = created_at |
| 49 | slack.slack_messages | UPDATE | parent `b658ec71107dd059e03ea425728ba3b3` | thread_ts_legacy = own ts, reply_count 1, users 1, latest_reply = reply ts — matches SQL replies |
| 50–55 | slack.slack_messages | INSERT ×3 | `d281112d…`, `44975451…`, `a8540bc3…` in #winddown `C0ADGSZKR3R` (Feb 12 23:15Z) | unused; Leonard member; ts = created_at |
| 56–63 | slack.slack_messages | INSERT ×4 | replies `4f54dff9…`, `0e3d2253…`, `846c625f…` (Leonard), `7440b1ba…` (Arthur `EMPLOYEE_0025_SLACK_ID`) to `e3e198cc…` | unused; both authors are #winddown members; replies after parent ts 1770934638.035469 |
| 64 | slack.slack_messages | UPDATE | parent `e3e198cc6e3f866a032d34c5f69e39f9` | reply_count 4, reply_users 2, latest_reply 1770949437.902269 — correct (base had 0 replies) |
| 66–67 | trello.trello_cards | INSERT | `698e5a10c3f24b7e9d16a0e4` "Stockholder close-out", idShort 456 | id unused (803 cards); board `640643a3…318e` and list "To Do" `…93195` exist; idShort 454/455 exist so 456 is next and free; shortLink in url (`XVXa9OOQ`) unused; hex id time = 2026-02-12T22:54:08Z = createCard date; badges comments 1 |
| 68–69 | trello.trello_actions | INSERT | `698e5a108882c0b9e98cdb3e` createCard | id unused (5,294 actions); creator `PERSON_6094_TRELLO_USER_ID` = Leonard (top actor on this board) |
| 70 | trello.trello_boards | UPDATE | board `640643a3fd8f3ca308d9318e` dateLastActivity → 2026-02-13T18:14:27Z | equals latest SQL action; base was 2025-11-12 |
| 71–72 | trello.trello_actions | INSERT | `698f6a03a222ee9dc57bc90f` commentCard | unused; hex time = action date; card dateLastActivity matches |
| 74–83 | gmail threads/messages | INSERT thread + 3 msgs, 2 snippet UPDATEs | Leonard thread `…/1857029474983245439` (KPMG 2025 audit request 16:48Z, Leonard reply 17:12Z, KPMG clarification 17:37Z) | thread and 3 message ids unused (104,480 msgs / 88,726 threads); sender `PERSON_3088_EMAIL` and cc list match the base KPMG 2024 audit thread (`leonard_1817557789846606177`); internal_date = date = Date header; In-Reply-To/References chain valid; snippet ends on latest message |
| 84–90 | gmail | INSERT thread + 2 msgs, 1 UPDATE | `…/1857034369525983506` Sunset intake request (18:06Z) + Leonard reply (18:19Z) | unused ids; `PERSON_2888_EMAIL` = Sunset Head of Partnerships in base (`00016827.json`, same signature) |
| 91–99 | gmail | INSERT ×3 msgs, 3 thread UPDATEs | Robert's "Re: Board position" (22:38:16Z) in Leonard `…/1856958794180374704`, Robert `…/1856959418563541618`, Arthur `…/1856959418725253571` | 3 base threads exist; In-Reply-To = Leonard's 22:14:52Z message `<CAPBs_a5B01Fz…>` (present in all three); same Message-ID across copies (base pattern); labels SENT/INBOX per mailbox |
| 100–105 | gmail | INSERT ×2 msgs, 2 thread UPDATEs | Robert's Feb 12 23:41Z reply on 2023 "Funds Transfer" threads (Leonard `…/1773963101399472184`, Robert `…/1773963101279916523`) to `PERSON_3941_EMAIL` | threads exist; In-Reply-To `<CAGkro_Ox2wP8…>` is Robert's Aug 11 2023 13:00:43 PT message (quoted header matches) |
| 106–108 | gmail | INSERT msg, thread UPDATE | DSN `<698ce305…GMR@mx.google.com>` (12:13:57 PT) in Leonard `…/1856860994291529096` | thread exists; replies to Leonard's 12:13:48 PT termination mail to `PERSON_3140_EMAIL`; sender `PERSON_3555_EMAIL` is the base mailer-daemon; no later mail from that address in base |
| 109–112 | gmail | INSERT thread + msg | `…/1856121753612004097` Calvin Price fwd of Carta PTEP extension (Feb 3) | unused; ES-3 values (granted 8,138, vested 4,408, grant Nov 10 2023, terminated Oct 24 2025, old last day Jan 24 2026) match base Carta mail `leonard_1847333347700620793`; new last day Feb 20 2026 is a plan date |
| 113–116 | gmail | INSERT thread + msg | `…/1783169549554193375` Carta activity Nov 20 2023 (ES-8, ES-10 accepted) | unused; Message-ID/thread-id/timestamp pattern matches base Carta mails; ES-n option URLs follow base numbering (ES-n = 18258519+n); no conflicting base ES-8/ES-10 record |
| 117–120 | gmail | INSERT thread + msg | `…/1856961760270377901` Leonard → "Husnu Akin <PERSON_8862_EMAIL>" (Feb 12 22:52Z) | unused; see Check C identity note |
| 121–122 | gmail.gmail_messages | UPDATE ×2 | body of base `<CAPBs_a6zM=…>` (Nov 26 2024 L&I owner list) in Arthur and Leonard copies | both targets exist; only change vs base: removes the line "(Total ownership percentage adds to 100%)."; the 27 listed percentages sum to 94.129%, so the edit removes a self-contradiction; both copies updated consistently |
| 124–125 | gcal.gcal_events | INSERT | `evt_6f1a2c9e4b7d3a58c0e1d2` "Holder notes due" Feb 17 17:00Z | event_id/ical_uid unused (11,130 events); formats match base; created Feb 13 ≤ clock; start is a plan time |
| 127–131 | contacts.contacts | INSERT ×2, UPDATE ×1 | new `d3c6e5b57e0ee6656a1bdd2c` (PERSON_0693), `13f3b76067d577bc30c45242` (PERSON_2275); update `db57e559500151d6b3991b62` (Matthew Collins) | new ids/emails unused (170 contacts); naming pattern matches base; update target exists; "left the board May 2025" matches base resignation mail of May 1 2025 (`leonard_1830959847543474636`) |
| 133–134 | linear.linear_projects | INSERT | `ec2ea957-fc8e-4958-b809-0fb735b1e916` "Holder records" | id/name unused (2 projects); team_ENG and lead `usr_63fffeb4fab5233e` (Leonard, ENG member) exist; created 02-12T23:24:12Z, updated 02-13T18:21:46Z (after the KPMG and Sunset mails it mentions) |
| 135–290 | linear.linear_issues ×26, linear_comments ×52 | INSERT | ENG-2438 … ENG-2463 (numbers 2438–2463); 2 comments each | base ENG max is 2437, so ids/identifiers/numbers are free; base comments collection is empty, so no comment-id collision; creator Leonard; state Backlog; state_history_json `[]`; every issue created after the project and before its comments; updated_at = last comment time |
| 291 | — | COMMIT | | |

## Check A — Records, references and IDs: PASS

- All referenced existing records resolve: Drive parent, Slack channels/users/parents, Trello board/list/member, 6 base Gmail threads, the 2 updated Gmail messages, Gmail mailboxes, labels (`Label_b19fb8d1b3` "Opened"), contact `db57e559…`, Linear team/user. Coverage numbers are in the ledger.
- All new keys are unused in the full local collections and unique within the SQL (Drive 5, Docs 2, Sheets 1, Slides 1, Slack 8 ids + 8 ts, Trello card/2 actions/idShort/shortLink, Gmail 5 threads + 14 messages, gcal event + iCalUID, contacts 2, Linear project 1 + 26 issues + 52 comments).
- ID contracts: Gmail `history_id` NULL on all 5 new threads; no Drive `content_path` used. No violation.
- Readable Drive files: both Docs have non-empty `docs_documents.body_text`; the Sheet and Slides have gsheets/gslides content rows; the folder needs none. Lint `drive_unreadable`: 0.
- One account per person: no new service accounts; all authors/creators map to existing accounts for the people named (Leonard, Robert, Arthur). Lint `duplicate_account`: 0.
- Holder ↔ address pairs on the Linear issues match base records where names are recoverable: Oct 2024 option-issuance mail (Brian Foster/PERSON_4243, Cameron/cameron@, [PERSON_NAME_0038]/PERSON_2314, Oliver Brooks/PERSON_1174), Nov 2023 list (Directors and internal team incl. PERSON_3641, [EMAIL_0801], PERSON_2360, PERSON_2361, PERSON_4194), seed-round mails (PERSON_3063 greeted "Arthur", PERSON_0693 = [PERSON_NAME_4468], PERSON_2260 + brothers), May 2024 (Martin/PERSON_4363, [PERSON_NAME_0068]/PERSON_3140).

## Check B — SQL structure and supported schema rules: PASS (provisional advisory)

- Static parse of all 132 INSERTs: column and value counts match; no duplicate columns; single-row statements terminated by `;`; escaping valid; all JSON columns parse with the snapshot shape (arrays; `metadata_json` `{}` object). No generated column (`text_fts`, `body_text_fts`) is set. Linear date fields use `YYYY-MM-DDTHH:MM:SSZ` / `YYYY-MM-DD`; every NOT NULL column without a default is supplied (incl. `state_history_json = '[]'`). 15 UPDATEs target existing columns.
- **Provisional snapshot MISMATCH (advisory, not a defect):** 4 columns are not in the unverified snapshot or the base export shapes: `gslides.slides_pages.notes` (5 rows, NULL), `gslides.slides_page_elements.table_json` (NULL) and `.ordinal` (0) (5 rows), `linear.linear_projects.links_json` (`'[]'`). Mitigating evidence: the earlier SQL version used the same four columns, and the saved Opus run shows its slide text ("What it means for you", "Distributions, tax papers") and the "Holder records" project, so that script loaded. Optional hardening: drop these four columns (all carry empty values), so a schema change can't roll back the whole transaction.
- Live database compatibility is outside this static scope.

## Check C — Dates, relationships and consistency: PASS

- Clock: every event timestamp is ≤ 2026-02-14T00:00Z (latest: Feb 13 18:21:46Z project update). Only plan fields are later (gcal start Feb 17; Carta "last day" Feb 20 in body text; KPMG due 2/27 in body text). Historical inserts (Carta Nov 2023; contact updated_at 2025-05-02) are allowed.
- Chronology: replies follow parents (Slack, Gmail, DSN 9 s after the send); Gmail `internal_date` = `date` = Date header for all 14 inserts; quoted "On … wrote" headers match the quoted messages; Trello ids encode their action times; Linear project → issues → comments in order.
- Facts vs base, all checked:
  - All 26 Linear "Last mail with that address before Feb" comments match Leonard's mailbox (from/to/cc/bcc/reply-to, before Feb 1 PT), incl. the 3 "No mail…" cases (body-only mentions exist but no mail to/from those addresses). Claire Morgan's May 1, 2023 comes from a Reply-To header.
  - All 25 "Nov 2024 owner list" comments match the L&I owner list values; ENG-2451 correctly "Not on the list".
  - Calvin ES-3 extension consistent with the base Carta termination mail; Robert's "Leonard and me on the board" is consistent with base directors (PERSON_4337 resigned Feb 12, 2026; Matthew Collins resigned May 1, 2025; Nov 2023 director list = PERSON_4337, Matthew Collins, Robert, plus Leonard).
  - KPMG and Sunset senders/cc keep their base roles; the DSN's "disabled account" has no contradicting later mail.
  - Body edit at lines 121–122 removes an inconsistent "adds to 100%" claim (listed percentages sum to 94.13%); the sheet note "only add to about 94%" agrees.
- Grader-facing text: none found (lint `grader_language` 0; manual read of every injected text). The notes are written as Leonard's own instructions, not addressed to a solver or grader.
- Context notes (not defects):
  - The injected email to "Husnu Akin <PERSON_8862_EMAIL>" ("on the board and since") builds on base evidence that Matthew Collins is Akin: he signs "akin" (Apr 15 and May 1, 2025 mails); Carta calls him "Husnu Matthew Collins"; the term sheet names "Akin …" as the outside director. `PERSON_8862_EMAIL` appears nowhere else in the base, so linking it to the ENG-2447 holder depends on that inference. Recipient addresses are not service accounts. /prompt should confirm the link is solvable.
  - The Sheet and Slides (created Feb 10) sit in the close-out folder created Feb 12. That reads as a later move (Drive keeps the original created time); not impossible chronology.
  - The Slack reply "chatgpt has the other seed investors a couple of shares off … go by the ledger" is a soft claim. No ledger figure in Gmail confirms or refutes it ("3,051,881" / "305,188" not found). Don't grade an exact discrepancy from it unless /prompt locates the ledger.
  - Pre-existing base quirks not caused by the SQL: the Feb 11 contractor termination letter says "effective January 31, 2025"; the PERSON_3140 holder appears as [PERSON_NAME_0067] and [PERSON_NAME_0068] in different base records.
- Known base issues: no Snowflake/Confluence record is used; no Feb 14 known data issue overlaps this SQL.

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | Full-collection collision checks complete; all references resolve; no ID-contract, Drive-readability or duplicate-account issue. |
| B — SQL structure and supported schema rules | PASS | Structure, JSON shapes, NOT NULL, Linear formats and generated columns clean. Provisional MISMATCH: 4 columns absent from the unverified snapshot (advisory). |
| C — Dates, relationships and consistency | PASS | All event times ≤ clock; chronology valid; 26 date comments and 25 share comments match base; no grader-facing text. |

## Findings

No demonstrated defects.

Advisories (not grading failures):
1. Check B, lines 26–45 and 133–134: four columns not in the provisional snapshot (`slides_pages.notes`, `slides_page_elements.table_json`, `slides_page_elements.ordinal`, `linear_projects.links_json`). Smallest optional fix: remove those columns and values from the INSERTs (all are NULL/0/`[]`).
2. Check C, line 120: the "Husnu Akin" ↔ Matthew Collins (ENG-2447) link is inferential (base signatures/Carta/term sheet); /prompt to confirm solvability.
3. Check C, line 48: the "couple of shares off" Slack claim can't be checked against a ledger from Gmail; avoid grading an exact figure from it unless the ledger is found.

## Dependencies for later stages (stage-evidence-v1)

- Static checks valid for SQL sha256 `9b02cc8f34a91f69c6faf607f5578d25b52e10c6115a0cddf99a180f4d8b5bfb`, universe manifest sha256 `5e01ac44…de450`, schema snapshot sha256 `31dcb2b4…5c151`, id_contracts sha256 `fc4711ef…d4682`, clock 2026-02-14 00:00 UTC.
- Reusable facts (ledger rows above): ID collision results per collection; Slack thread counters; Gmail chain/timestamp checks; Linear comment date and share values vs base; Carta ES-3 values; director roster facts.
- Not covered here (owned by /prompt, /hardness): discoverability, persona visibility, the Akin identity inference, task difficulty.
- Note: the shared `input_manifest.json` injection entry was not rewritten by the report writer; this report carries the current fingerprints.

### FINAL VERDICT: PASS

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Next action: Proceed to /prompt (optional hardening: drop the 4 snapshot-mismatch columns, then rerun /injection)

Evidence limits: Static review only; no live execution or live schema check. The 4 snapshot-mismatch columns are a provisional advisory (an earlier run loaded the same columns). Pseudonymized display names stop full name↔address verification for a few holders; their addresses do match base investor/seed-round mail.
