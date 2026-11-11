# /injection — Injection data-integrity review (rev7)

## Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2`, evidence contract `stage-evidence-v1` |
| Review time | 2026-11-08T19:21:13Z |
| Universe | `Universe_Normal` (Feb 14, 2026 normal); manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Fixed clock | 2026-02-14 00:00 UTC |
| Input | `inputs/01_Universe_Inject.sql`, 75,892 bytes, sha256 `40f90385e31e099d28a10e483f0a94490a34096c87f08c4ca35c97c3f311d37c` |
| Previous revision | `prev/01_Universe_Inject.rev6.sql`, sha256 `ad50f039b5c28053bb1b1905c09ecb4b634918b2ab45ca3afc2163d035854a06` |
| References | Eval 0 sha256 `86af2102ea6693c41047ed84dd60d59069d7c8810a652aeb7367ce4b563dfcd3`; schema snapshot `injection.json` sha256 `01ef579236212034a43a53914754f86ed9248be48c961009cef5b4bd6106f6eb`; `id_contracts.json` sha256 `fc4711ef07667333c1cf2a417279826f0432539195f7acdfacfa86e9d9ed4682`; WORKFLOW sha256 `05a5e45e…8c69` (from `hg_reference guide injection`) |
| Lint | `hg_injection_lint.py` `injection-lint-v1` on the same SQL hash |

Provenance caution: `prev/rev6_eval0_report.md` is bound to a different file (sha256 `a52191c3…7253`, 74,853 bytes, no `BEGIN;`), not to `prev/01_Universe_Inject.rev6.sql`, and to older Eval 0, schema and WORKFLOW hashes. No verdict or check from it is reused. Only raw base facts on rows that are textually the same are marked REUSED below; almost everything was rerun NEW.

## Diff, rev6 to rev7 (line-level, complete)

| SQL line | Change |
|---|---|
| 3 | Header comment: `123 INSERT` → `124 INSERT` (accurate; lint counts 124 INSERT, 2 UPDATE, 1 BEGIN, 1 COMMIT) |
| 51–52 | NEW `slack.slack_messages` row `a14881891ac2003c9a5861d2c5060287`, C04UEQVDVB7, Leonard, ts `1770947533.284619`: "fyi that Apr 2024 wire to the account ending 8605 came back to us. Blake had the wrong number, he re-sent it to 3341" |
| 176 | ENG-2447 `comment_b13f790b…` body: removes ". the bank has him from Sep 2024", now "that’s Lucas, mini games dev" |
| 200 | ENG-2450 `comment_10121682…` body: "…but I can’t remember what it was for" → "I approved this one in Aug 2024, think it was an advance to one of the contractors but I can’t place which" |

## Checklist

- [x] SQL hash, base manifest and review version recorded (NEW). The input store was deliberately not written to, per the brief. The inputs were read from the review folder
- [x] Lint run (NEW): 0 FAIL / 0 CHECK / 0 INFO
- [x] Every statement inventoried (NEW, independent parser): 128 statements, 124 rows, value counts match columns on all rows
- [x] Check A (NEW): collisions over complete collections, references, ID contracts, Drive readability, one account per person
- [x] Check B (NEW): structure, transaction, generated columns, Linear text dates, NOT NULL, 196 JSON fields, doc style runs, snapshot comparison
- [x] Check C (NEW for all changed rows, clock, chronology, SVB totals and returned wires; REUSED only where marked)

## Lint flags and resolutions

| Flag | Count | Resolution |
|---|---|---|
| FAIL (`future_date`, `id_contract`, `drive_unreadable`, `duplicate_account`, `actor_name`, `generated_column`, `text_time_format`, `missing_required`) | 0 | none raised |
| CHECK (`unknown_actor`, `grader_language`, `padding_comment`) | 0 | none raised. Manual read of the three changed text values and all 14 SQL comments finds no grader-facing, padding or call-count language. Line 4 ("re-apply this exact SQL before every agent run") is an operator note in a SQL comment, not injected data |
| INFO | 0 | none |

Base lists loaded by the lint: contacts, slack/users, trello, gmail/users, linear, confluence_working.

## Operation ledger

Base paths are relative to `Universe_Normal/`. Slack paths are under `Normal_HarmonyGames_Other_Services/Services_Data/slack/messages/`. All collision results are NEW, `scan_complete: true`, 0 matches.

| # (SQL line) | Table | Op | Record(s) | Key references / values | Result |
|---|---|---|---|---|---|
| 1 | — | BEGIN | line 5 | matches trailing COMMIT | OK |
| 2 | gdrive.drive_files | INSERT ×3 | `f_6feda53b…`, `f_33040338…`, `f_a4b3c428…` | parent `d_63fffeb4fab5233ed5bb73` = Leonard's root (`gdrive/data.json` `/drive_files`) | OK, 53,866 checked |
| 3 | gdocs.docs_documents | INSERT | `f_6feda53b…` | body 2,307 chars, last style run ends 2307, `drive_file_id` resolves | OK, 633 checked; readable |
| 4 | gsheets ×2 | INSERT | `f_33040338…`, sheet 0 | grid row 2: 984,888.21 / 608,820.50 / 73,685.61 | OK, 398 checked; values recomputed (C3) |
| 5 | gslides ×11 | INSERT | `f_a4b3c428…`, 5 pages, 5 elements | pages/elements resolve to the presentation; "$985K / $609K / $74K" | OK, 164 checked |
| 6 | slack.slack_messages | INSERT ×2 | `fa707da5…`, `f5b759f3…` C0ADGSZKR3R (#winddown) | EMPLOYEE_0038 = Leonard, in members; not archived | OK |
| 7 | slack.slack_messages | INSERT | `6312d121…` C05URGU759U (#leapblock) | EMPLOYEE_0024 in members, Robert in members | OK |
| 8 | slack.slack_messages | INSERT **(new)** | `a14881891ac2003c9a5861d2c5060287` C04UEQVDVB7 | see C2 | OK; slack ids 687,230 records, 5,353 files |
| 9 | trello cards / actions | INSERT ×3 | `698e55f9…de7b3`; `…de737`, `…0fde` | board `640643a3…`, list `…3195` "To Do" (open), PERSON_6094 = Leonard; `idCard` resolves | OK, 803 / 5,294 checked |
| 10 | trello.trello_boards | UPDATE | `640643a3fd8f3ca308d9318e` | `dateLastActivity` = latest injected action | OK, target exists |
| 11 | gmail threads ×5 / messages ×8 | INSERT | Chase thread ×3 mailboxes, invites ×2 | every `thread_id` resolves in SQL; `in_reply_to` of the reply = first Message-ID | OK, 88,726 thread files / 104,480 messages; no thread or message id collisions |
| 12 | gcal.gcal_events | INSERT ×3 | `evt_cdc76b69…`, `evt_f21476dc…`, `evt_351ff9bb…` | calendars exist for Leonard, Robert, Arthur; start 2026-02-17T17:00Z (plan field) | OK, 11,130 checked |
| 13 | contacts.contacts | INSERT | `564155d7…` Lauren Brooks | lauren@harmonygames.co; Slack user EMPLOYEE_0035 (one account) | OK, 170 checked |
| 14 | linear.linear_projects | INSERT | `0742c172-…-316e5c8cb187` | team_ENG exists; lead usr_63ff = Leonard | OK, 2 checked |
| 15 | linear.linear_issues | INSERT ×22 | ENG-2438 … ENG-2459 | numbers 2438–2459 unique; base ENG max 2437; state `Backlog`; `state_history_json '[]'` | OK, 3,852 checked (id and identifier) |
| 16 | linear.linear_comments | INSERT ×60 | 60 distinct ids including **changed** `comment_b13f790b…`, `comment_10121682…` | authors usr_63ff (49) = Leonard, usr_cc3e (11) = Arthur, both `tmem_team_ENG_*` members | OK; base `/comments` is empty |
| 17 | linear.linear_teams | UPDATE | `team_ENG` `issue_counter = 2459` | target exists; = highest injected number | OK (column not in snapshot, B) |
| 18 | — | COMMIT | last | paired with BEGIN | OK |

## Check A — Records, references and IDs: PASS

- All new unique keys are absent from their complete base collections (counts in the ledger) and unique within the SQL. Slides pages and elements repeat only the parent presentation id, as designed.
- All referenced actors, parents, channels, boards, lists, calendars, mailboxes and teams resolve. The new Slack row's author EMPLOYEE_0038_SLACK_ID is Leonard Hayes (`slack/users.json`); the two changed comments' author `usr_63fffeb4fab5233e` is leonard.hayes@harmonygames.co and an ENG team member.
- ID contracts: Gmail `history_id` NULL on all five threads; no Drive `content_path` is used; the Doc is readable through its docs_documents body.
- One account per person: no new actor is introduced. Lauren Brooks's contact matches the single Slack user with that email.

## Check B — SQL structure and supported schema rules: PASS

- 128 statements: 1 BEGIN, 124 single-row INSERTs, 2 UPDATEs, 1 COMMIT, in a correct order; parents precede children. The rev6 report's `COMMIT`-without-`BEGIN` advisory no longer applies.
- `text_fts` and `body_text_fts` are not set. All Linear `*_at` values are `YYYY-MM-DDTHH:MM:SSZ`; `state_history_json` is `'[]'` on all 22 issues; all 196 JSON-typed literals parse; doc style runs end at the body length.
- Provisional snapshot comparison (`injection.json` sha256 `01ef5792…`): MATCH on every column of every affected table except NOT COVERED: `linear.linear_projects.links_json`, `gslides.slides_pages.notes`, `gslides.slides_page_elements.table_json`, `ordinal`. `linear.linear_teams.issue_counter` (UPDATE target) is likewise not covered, and the base `teams` export has no such field. Snapshot is unverified, so this is a disclosed compatibility limit only.

## Check C — Dates, relationships and consistency: PASS

**C1. Clock (NEW).** Every event timestamp in the SQL is before 2026-02-14T00:00:00Z. The only values at or after the clock are the three calendar events' `start_ts`/`end_ts` on 2026-02-17 (plan fields).

**C2. New Slack row `a14881891ac2003c9a5861d2c5060287` (NEW).**
- Timestamp: ts `1770947533.284619` decodes to 2026-02-13T01:52:13.284619Z and equals `created_at` 2026-02-13T01:52:13Z. It follows Leonard's #winddown request (01:23:41Z / 01:24:19Z) and precedes the clock. NB-6 is not engaged: it is before the Slack export's end (Feb 13 10:03:26Z, latest base ts 1770977006.104929).
- Channel: C04UEQVDVB7 is `admin_foundersonly` (private, not archived, 7 members). `persona_view.py can-see robert slack C04UEQVDVB7` returns YES.
- Author and membership after Feb 11 (NB-1): Leonard (EMPLOYEE_0038) and Robert (EMPLOYEE_0016) and Arthur (EMPLOYEE_0025) are in `channels.json` members, each with a `channel_join` (2023-03-17, 2023-03-25) and no `channel_leave` anywhere in the channel history or in any 2026-02 file. None of NB-1's seven (Julia, Marcus, Owen, Oliver, Martin, Claire, Brian) is a member of this channel, so no post is by someone in a channel they left. Leonard's Feb 11 20:40 decision keeps the founders: `C0ADGSZKR3R/2026-02.json` /94, "so we’ll keep maybe the three of us"; the guest conversion names only those moved to `#prototype` (/92, `C09UHHN6PFZ/2026-02.json` /604). Base has 418 founder posts after Feb 11 20:40 UTC.
- Feb 11 shutdown rules: the post is about a 2024 wire in a wind-down context and assumes no continuing operations. The base continues to carry founder posts through Feb 13.
- Content: every claim is supported by base records.
  - One wire to account ending 8605, and only one: `gmail/threads/00004079.json` (Awaiting Approval), `00004080.json` (Scheduled), `00004088.json` (Processed) on Apr 2 2024, 4,032.00 USD, "BANCO DE AMERICA ***8605", Created/Submitted by Arthur, Approved by Leonard. Complete Gmail scan of "BANCO DE AMERICA": no other ***8605 payment.
  - "came back to us": `leonard@harmonygames.co_1795505181532693167.json`, Apr 5 2024 14:26Z, SVB Wire Investigations: "the wire transfer … has been returned … Wire Date: 4/2/2024 … Returned Amount: 4,032 USD … Return Reason: BENEFICIARY ACCOUNT INVALID".
  - "Blake had the wrong number": `C04UEQVDVB7/2024-04.json` /19–/21, Leonard "This wire didn’t go through", Arthur "thats the motmot one?", "I think I messed up the bank account number. Fixed up and resubmitted the payment."; and /71, Leonard "this is money returned to us because Blake put the wrong account number … and bank returned our money". Robert is in this channel and took part at /73–/89 on Apr 12.
  - "re-sent it to 3341": `00004120.json` (Recipient Modified, ***3341, Apr 5 15:40Z), `00004121.json` (Awaiting Approval, submitted by Arthur), `00004124.json` (Processed), 4,032.00 USD, Transaction Date Apr 05 2024. Then ***3341 is the only account used through Feb 27 2025 (`00011701.json`, complete scan).
  - The base contains exactly two returned wires (complete Gmail scan of "wire return / return reason"): this one and the 125.00 USD Private Entrepreneur wire of May 7 2024, which ENG-2459's existing comment already covers. No base record contradicts the new row or the ENG-2442 issue's "accounts ending 3341, 8605".
- NB-12: the row names the payee only by account digits and "Blake" (Arthur, as in base /71), so it does not depend on a tokenized name.
- Schema/shape: matches the other three Slack rows; `thread_parent_id` NULL (top-level post). `ts` absent from base.

**C3. Changed ENG-2447 comment (NEW).** "that’s Lucas, mini games dev": consistent. `slack/users.json` has `U7CADAB457A` Lucas, lucas@harmonygames.co. `C04UTBZL6AX/2024-06.json` /1092, Robert: "Lucas actually sent me this and said we should build it as a mini game"; `D07GJJBLGFK/2024-08.json` /26, Arthur: "We had an intern, Lucas, implement the game" (ENG-1221 coin dozer); `C07C2866011/2024-10.json` /238 "tile dozer just got a few update by Lucas". The token ***6577 / [PERSON_NAME_36400] is his: the Western Union notices (`gmail/threads/00005184.json` … `00006329.json`) name [PERSON_NAME_36400], Ukraine, and `00005350.json` message 1 forwards "Invoice paid" to lucas@harmonygames.co; SVB ***6577 begins Sep 2024 with three Processed notices (`00007151`, `00008235`, `00009058`, 2,150.00 USD). Removing the Sep 2024 clause cannot introduce a contradiction. The issue's other two comments are unchanged and read consistently.

**C4. Changed ENG-2450 comment (NEW).**
- "I approved this one in Aug 2024": `gmail/threads/00006272.json` / `leonard@harmonygames.co_1807851044272471527.json`, 4,000.00 USD to JPMorgan ***3203, Transaction Date Aug 19 2024, Submitted by Arthur, Approved by Leonard. `C04UEQVDVB7/2024-08.json` /37 Arthur 2024-08-19 20:49Z "payment started in SVB. Please approve", /38 Leonard 20:56Z "done - thank you". Supported.
- "think it was an advance to one of the contractors but I can’t place which": a hedged memory at 2026-02-13T00:26:36Z. It is corrected later in the same SQL by Arthur's email (`CAOOpSqA2MTK…`, 2026-02-13T16:26:44Z: "the $4,000 to JPMorgan ***3203 … was me. That was our own Chase account, I sent it over to put the money back after Carta's renewal came out of Chase. So it never left the company.") and Leonard's reply (`CAPBs_a5xhlL…`, 17:08:37Z: "ah that’s the one I couldn’t place, thanks"). The eval treats a stale statement with a later correction as valid when records support it, and they do: the base independently corroborates Arthur's email. `leonard@harmonygames.co_1806180183982475868.json` (Aug 1 2024): "Renewal date August 15, 2024 Payment method Bank account ending in 3203 Plan Grow". So ***3203 is an account the company's Carta renewal was set against, with a renewal date four days before the wire. The new wording does not conflict with the email: the guess is hedged, the reply echoes "couldn’t place", and the correction is explicit and later.
- Complete searches for this wire's purpose found no other record that assigns it (Slack Aug 2024, all channels; Gmail Aug–Sep 2024 for 3203 / 4,000 / advance; Snowflake `FINANCE_LEDGER` is monthly-aggregated with no such counterparty). No base record contradicts "an advance" as a mistaken recollection.

**C5. Linear chronology (NEW, all 60 comments and 22 issues).** Comments are sorted within each issue, none precede their issue, `created_at = updated_at` on each, each issue's `updated_at` equals its last comment, and issues do not overlap: 23:36:28Z → 00:58:46Z. The last comment precedes Leonard's #winddown request. `time_in_status_minutes` equals floor(minutes from `created_at` to the clock) on all 22 issues.

**C6. SVB totals (NEW).** Complete scan: 132 unique "Payment Processed" notices in robert@harmonygames.co, 2023-09-05 to 2026-02-02 (131 USD, 1 BGN). USD by Transaction Date over the doc's windows gives **984,888.21 / 608,820.50 / 73,685.61**, exactly the sheet row; the deck rounds them. The sheet and deck are labelled quick figures ("quick pass", Trello "fine for a first pass"), and the doc says a notice is "where you start, not the last word"; the rev7 row and the May 2024 comment are the concrete "came back" statements the doc anticipates, so they do not conflict with the quick totals.

**C7. Unchanged rows (REUSED).** Raw base facts for text-identical rows, cited from `prev/rev6_eval0_report.md`: ENG-2454 laptop comment (`C04UEQVDVB7/2025-10.json` /500–/529), ENG-2455 Lauren contract (`C05KNDCHAAG/2025-10.json` /26, `C07C2866011/2025-10.json` /526, /535, /630, /639; PDF has no readable content, a limit recorded in that report), Leapblock close-out (`gmail/threads/00001577.json`), the remaining memory comments ENG-2438–2441, 2443–2446, 2448–2449, 2451–2453, 2456–2458, and the "Chase records" thread. Base manifest hash is unchanged. The report binds to a different SQL hash, so these are raw facts only and no earlier check result is carried over.

**C8. Grader-facing text.** None in the changed text or the SQL comments.

Pre-existing base context, not caused by this SQL: NB-23, NB-24, NB-26 apply as before, and this SQL's new Linear comments are additions to an empty base collection.

## Findings

None. No defect was demonstrated in A, B or C.

## Final summary

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | 0 collisions across complete collections (Drive 53,866; Docs 633; Sheets 398; Slides 164; Slack 687,230; Gmail 88,726 files / 104,480 messages; Trello 803 / 5,294; Calendar 11,130; Contacts 170; Linear 3,852 issues, 0 comments, 2 projects). Authors, parents and targets resolve; ID contracts and readability met |
| B — SQL structure and supported schema rules | PASS | 128 statements with paired BEGIN/COMMIT; no generated columns; Linear formats and NOT NULL met; 196 JSON literals valid; style runs correct. Snapshot NOT COVERED columns disclosed |
| C — Dates, relationships and consistency | PASS | All events before the clock; new Slack row and both changed comments verified against quoted base records, NB-1, NB-6, NB-12 and the Feb 11 shutdown facts; SVB totals recomputed; Linear chronology and durations correct |

Scores (1–5). `injection-static-v2` is an unscored stage; these are given because the review brief asked for them.

| Dimension | Score | Basis |
|---|---|---|
| A — Records, references and IDs | 5 | Complete-collection collisions and all references clean |
| B — SQL structure and supported schema rules | 5 | Clean parse, paired transaction, JSON and format rules met; snapshot limits are advisory only |
| C — Dates, relationships and consistency | 5 | All changed rows supported; no introduced contradiction; later correction of ENG-2450 is record-backed |
| Overall | 5 | PASS / COMPLETE |

Stage dependencies for reuse by `/prompt`: SQL sha256 `40f90385e31e099d28a10e483f0a94490a34096c87f08c4ca35c97c3f311d37c`; universe manifest `5e01ac44…de450`; `injection.json` `01ef5792…06f6eb`; `id_contracts.json` `fc4711ef…4682`; notice cohort = 132 unique Processed notices in Robert's mailbox; wire-return evidence as quoted in C2 and C4.

### FINAL VERDICT: PASS

Score: 5/5 (A 5, B 5, C 5; requested by the review brief, the stage itself is unscored)

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt (rev7 is a new SQL version, so earlier /prompt results need rerunning).

Evidence limits: Static review only, no execution or deployment check. The schema snapshot is unverified and does not cover `linear_projects.links_json`, `linear_teams.issue_counter`, `slides_pages.notes`, `slides_page_elements.table_json`/`ordinal`. `prev/rev6_eval0_report.md` binds to a different SQL hash than `prev/01_Universe_Inject.rev6.sql` and to older reference hashes, so only raw base facts on text-identical rows are reused (C7). Lauren Brooks's contract PDF has no readable content in the export. Base Linear has no comments (NB-24). Agent visibility beyond the channel check and task difficulty are out of scope.
