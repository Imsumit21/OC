# /injection — Injection Data-Integrity Review

## Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`) |
| Mode | Chat review, attempt 6aea332703436a747f8302ec |
| Review time | 2026-11-04T22:18Z |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16, archive sha256 `d04f295b…fb0c`); manifest `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` (unchanged since R1) |
| Reviewed input | `Evals/task_inputs/01_Universe_Inject.sql` (saved rev 5, from attachment `01_Universe_Inject (3).sql`), 89,009 bytes, sha256 `c40a78a9db79b113d51c059b0e097d4b87a94361c24d9723321f64d002da1d16` |
| Prior review reused (R1) | `Evals/task_inputs/reports/0_injection.md` sha256 `fed1dffb1fdc5b8a075767f68fdd4c5c055b819229c62c59b085fab92623b0ab` (PASS/COMPLETE, 2026-11-04T18:36Z, SQL rev 3 sha256 `403883…8948`) |
| References | Eval 0 sha256 `e034019b…3eff`; WORKFLOW sha256 `ee4cd8e1…d5d`; schema snapshot `injection.json` sha256 `31dcb2b4…5151`; `id_contracts.json` sha256 `fc4711ef…82f`; lint `injection-lint-v1`. All identical to R1 |
| Assignment (context only) | Samuel Turner, Game Designer, Long-Horizon, Oct 1, 2025 |

## Input / authority issues

None. The SQL is substantive: 148 statements (BEGIN, 138 single-row INSERTs, 8 UPDATEs, COMMIT), the same counts as rev 3. A line diff against rev 3 shows exactly **two changed lines** and nothing else:

1. Line 44, Slack DM `6fd96f3c…` (Leonard → Samuel): the text of the request changed ("iOS and Android separately", "the lapsed reminders the client schedules day by day, and anything the client already schedules that's still a Hold and why").
2. Line 292, Linear comment `cmt_275f13c4…` on DES-346 (Leonard): body changed to "No bonus ad is live today and I moved rewarded ads to Oct 21 on the roadmap, so this one isn't in the beta."

No ID, actor, timestamp, column list or other statement changed. SQL comments are unchanged operational notes.

## Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, manifest, review version | NEW, done |
| Run `hg_injection_lint.py`; resolve flags | NEW, done (0 FAIL / 0 CHECK / 0 INFO on rev 5) |
| Inventory every statement | NEW diff + full ledger (unchanged rows REUSED from R1 with provenance) |
| Check A | PASS (REUSED for 146 byte-identical statements; NEW for the 2 changed rows) |
| Check B | PASS (NEW parse of changed rows; REUSED otherwise) |
| Check C | PASS (NEW base check of the new DES-346 claim and the new DM text) |
| Report coverage, limits, verdict | done |

### Reuse basis (stage-evidence-v1)

R1's ledger records each statement's record IDs, base pointers, collision coverage and results. These dependencies are verified unchanged: every reused statement is byte-identical (line diff), the universe manifest, Eval 0, WORKFLOW, schema snapshot and ID contracts have the same sha256, and the clock is the same. The two changed statements only change free text, so their ID/collision/actor/chronology results still hold. Their structure and content were checked again (NEW).

## Lint flags and resolutions

`hg_injection_lint.py` on rev 5 (sha256 `c40a78…1d16`) ran the future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required and json_shape checks. **Flags: none.**

## Operation ledger (execution order)

| SQL line(s) | Table | Op | Record(s) | Base resolution / result | Verification |
|---|---|---|---|---|---|
| 7–12 | gdrive.drive_files | INSERT ×3 | `f_dc45e0e5…` (Doc "Beta message rule", Leonard), `f_de7a1ae2…` (Slides "Beta readiness", Leonard), `f_8eb8c047…` (Sheet "Phone message checks", Vincent) | Parents `d_63fffeb4fab5233ed5bb73` (Leonard's root) and `d_65c76e0b87aa7e9b84d1df` (Vincent's root) exist in gdrive/data.json with matching owners. IDs absent from gdrive, gdocs, gsheets, gslides data and the Drive source manifest (full-file scans). PASS | REUSED (R1 ledger, statement byte-identical) |
| 14–15 | gdocs.docs_documents | INSERT | `f_dc45e0e5…` | Non-empty body_text (1,462 chars); style runs 0–18 TITLE / 18–1462 NORMAL match its length exactly. Readable. PASS | REUSED (R1 ledger, statement byte-identical) |
| 17–20 | gsheets spreadsheets/sheets | INSERT ×2 | `f_8eb8c047…`, sheet 0 "Beta" | Native sheet with grid rows. created 09-15 12:51Z comes before Vincent's 13:05Z email that names it. PASS | REUSED (R1 ledger, statement byte-identical) |
| 22–29 | gslides presentations/pages/elements | INSERT ×4 | `f_de7a1ae2…`, `slide_7cbfbffe1b54`, `el_b78f5cefad1f`, `el_9ecdf1278098` | Native deck. All 132 base presentations likewise have no content_path. PASS | REUSED (R1 ledger, statement byte-identical) |
| 31–32 | slack.slack_messages | INSERT | `394f73aa…` Brian (EMPLOYEE_0026) in C0880U9751A #zombie-match3d, 09-26 | Author is a channel member (joined 2025-01), no leave event. PASS | REUSED (R1 ledger, statement byte-identical) |
| 33–36 | slack.slack_messages | INSERT ×2 | `37c5701a…` Robert parent (reply_count 1, latest_reply = reply ts), `09aae609…` Arthur reply | Both members. Reply ts comes after the parent. PASS | REUSED (R1 ledger, statement byte-identical) |
| 37–39 | slack.slack_messages | INSERT + UPDATE | `d2b16907…` Leonard reply in C08R8CHB0QL #zombie-art; parent `a3e78e82…` | Base parent has 3 replies (users 0005, 0009, 0033), latest `1759161266.305589`. The UPDATE to 4 / 4 / `1759169129.445834` is exact (Leonard is a new distinct replier and a channel member). PASS | REUSED (R1 ledger, statement byte-identical) |
| 40–42 | slack.slack_messages | INSERT + UPDATE | `4a5ee025…` Vincent reply in DM D06UFE81RF0; parent `c42902df…` (Samuel, 0 replies) | DM members are Samuel and Vincent. UPDATE to 1/1/latest plus `thread_ts_legacy` = parent ts follows the base parent convention. PASS | REUSED (R1 ledger, statement byte-identical) |
| 43–44 | slack.slack_messages | INSERT | `6fd96f3c…` Leonard to Samuel DM D06L58XCVKK, 09-30 20:40Z | DM members include both. PASS | **NEW** for this row: text changed in rev 5 (only change). Re-parsed: 18 columns / 18 values, quoting closed, `metadata_json` `{}`, JSON lists valid. id/ts/channel/user/created_at byte-identical to rev 3, so the collision, membership and chronology results carry over. New wording is a persona request to Samuel; no grader-facing text, no factual figure asserted |
| 46–48 | trello actions/cards | INSERT + UPDATE | action `68d41578…` updateCard dueComplete true→false on card 7 `6851a769…` | Base card dueComplete=true, matching `old`. The UPDATE sets dueComplete=false. Member PERSON_6094 = Leonard Hayes. PASS | REUSED (R1 ledger, statement byte-identical) |
| 49–51 | trello actions/cards | INSERT + UPDATE | commentCard `68d415a7…` on card 7; badges comments 1→2, dateLastActivity 09-24 16:00:39Z | Base badges.comments=1, so +1 is correct. badges.dueComplete false matches the card field. PASS | REUSED (R1 ledger, statement byte-identical) |
| 52–54 | trello actions/cards | INSERT + UPDATE | commentCard `68dae8c7…` on card 79 "Fix TECH ISSUES"; badges comments 0→1 | Embedded list name "BETA: Sep 30" matches the list's name at that date (renamed 2025-09-12; every later action uses it). PASS (see advisory SC-13) | REUSED (R1 ledger, statement byte-identical) |
| 56–63 | gmail threads/messages | INSERT ×4 | Vincent's "Phone messages for beta" in Samuel's INBOX thread `…/1843335316636662321` and Vincent's SENT thread `…/1843335316636098078` | Both mailboxes exist in gmail/users.json. Thread IDs' embedded time (id>>20) = 2025-09-15 13:05:48 matches the message date. history_id NULL (contract OK). PASS | REUSED (R1 ledger, statement byte-identical) |
| 64–65 | gmail.gmail_messages | INSERT | GitHub notification `…/pull/248/review/2963610417@github.com` into existing thread `samuel.turner@harmonygames.co/1836006988541924555` | Base thread exists (8 PR #248 notifications). 20:58:14Z falls between the base reviews 2963243580 (19:04Z) and 2963696884 (21:21Z), and the review number is in order. To/Cc/Reply-To placeholders match base messages. PASS | REUSED (R1 ledger, statement byte-identical) |
| 66–73 | gmail threads/messages | INSERT ×4 | Leonard's invite (09-23) and cancellation (09-25) | Thread IDs' embedded times match. "10am CST – El Salvador" = 16:00Z, and Samuel's calendar zone is America/El_Salvador. PASS | REUSED (R1 ledger, statement byte-identical) |
| 75–78 | gcal.gcal_events | INSERT ×2 | `evt_b56d5b19…` (Samuel), `evt_8cad40bb…` (Leonard), shared ical_uid `924cf356…@hg4`, cancelled | Event IDs and ical_uid are absent from base (10,395 events). One ical_uid across two calendars is a base convention (798 cases). created/updated equal the invite/cancel email times. PASS | REUSED (R1 ledger, statement byte-identical) |
| 80–83 | github review_comments/reviews | INSERT ×2 | `…#248#rc_18`, `…#248#rev_7`, author EMPLOYEE_0025 (Arthur Blake) | PR #248 exists (merged 21:23:32Z). rc_1–17 and rev_1–6 exist; rc_18 and rev_7 are new. Comment at 20:58:14Z comes before Arthur's base APPROVED review (21:23:25Z). The diff_hunk is an exact prefix of base rc_16's hunk. PASS | REUSED (R1 ledger, statement byte-identical) |
| 85–92 | linear.linear_team_memberships | INSERT ×4 | team_DES + Calvin, Samuel, Martin, Oliver | Users exist. The 4 IDs are absent (76 base memberships). Each is created before that user's first DES issue/comment. PASS | REUSED (R1 ledger, statement byte-identical) |
| 93–150 | linear.linear_issues | INSERT ×34 | DES-313 … DES-346 | Base DES stops at DES-312 (247 DES issues, 3,687 total), so no id/identifier collision. Number order matches created_at order. Children are created after parent DES-314. All creators/assignees/authors are DES members. state_history_json `'[]'` given. PASS | REUSED (R1 ledger, statement byte-identical) |
| 151–296 | linear.linear_comments | INSERT ×68 | 66 on DES-313…346, `cmt_f1b8a109…` on ZOM-542, `cmt_2b519285…` on ZOM-556 | Base has 0 Linear comments, so no collision. Each comment comes after its issue's created_at and on/before its updated_at. Sequences run 1..n with no gaps and follow time order. PASS | REUSED for 67 comments. **NEW** for `cmt_275f13c4…` (line 292, body changed): 9 columns / 9 values, id/issue/author/time/sequence unchanged; new claim "No bonus ad is live today" checked against base (Check C) |
| 297–298 | linear.linear_issues | UPDATE ×2 | ZOM-542 relations → DES-330, ZOM-556 relations → DES-338 | Base relations of both are `[]`, so nothing is overwritten. They mirror DES-330 and DES-338's relations. updated_at equals the injected comment time. PASS | REUSED (R1 ledger, statement byte-identical) |
| 299 | linear.linear_teams | UPDATE | team_DES issue_counter = 346 | Equals the highest injected number (DES-346). Column not in snapshot (advisory below). PASS | REUSED (R1 ledger, statement byte-identical) |

## Check A — Records, references and IDs: PASS

- REUSED from R1 (A bullets; statements unchanged): every actor resolves to the named person (Linear `usr_49b9…` Calvin, `usr_4e13…` Owen, `usr_51f5…` Martin, `usr_63ff…` Leonard, `usr_65c7…` Vincent, `usr_8140…` Julia, `usr_bdf0…` Oliver, `usr_caaf…` Samuel, `usr_cc3e…` Arthur, `usr_fc22…` Brian, `usr_Robert` Robert; Slack 0012/0016/0025/0026/0038; Trello PERSON_6094; GitHub EMPLOYEE_0025). There are no second accounts and all parents/targets exist. Collision coverage was complete: a Slack `lookup` of 610,468 records with 0 hits, a Gmail scan of all 81,404 threads with 0 hits, Linear `hg_records` scan_complete, and full reads of Trello, GCal, GitHub and Drive/Docs/Sheets/Slides. The ID contracts and the readable-file rule are met.
- NEW: the two changed rows keep the same IDs (`6fd96f3c3977cee8345e685d31cbc177`, `cmt_275f13c47da0f6fd4687`), authors (EMPLOYEE_0038 / `usr_63fffeb4fab5233e` = Leonard) and parents (DM D06L58XCVKK, issue DES-346), so R1's collision and identity results apply unchanged.

## Check B — SQL structure and supported schema rules: PASS

- NEW: line 44 has 18 columns and 18 values. The quotes close and `''` escapes are balanced, `reactions_json`/`files_json`/`attachments_json` = `'[]'` and `metadata_json` = `'{}'` (correct shapes), and there's no `text_fts`. Line 292 has 9 columns and 9 values, with `created_at`/`updated_at` in `YYYY-MM-DDTHH:MM:SSZ`.
- REUSED from R1: every other INSERT's column/value counts, JSON shapes, Linear date format, `state_history_json '[]'` and NOT NULL coverage.
- Provisional snapshot advisories (unchanged, not failures): `linear.linear_comments.sequence`, `linear.linear_teams.issue_counter`, `github.github_review_comments.seq`, `github.github_reviews.seq`, `gslides.slides_pages.notes`, `gslides.slides_page_elements.table_json` and `.ordinal` are absent from the unverified snapshot.

## Check C — Dates, relationships and consistency: PASS

- REUSED from R1: all 288 ISO timestamps are ≤ 2025-10-01T07:00Z (latest 2025-09-30T20:40:51Z, unchanged). Reply/parent ordering, Linear state/timestamp coherence and the earlier fact cross-checks hold: 6 "Ready" on the PNs Beta tab, the DES-315…327 copies, PR #248 code, and the supported stale/correction records.
- NEW, DES-346 comment (line 292), claim "No bonus ad is live today" (2025-09-29T16:02Z). Base data agrees:
  - Slack DM `D077ALC9VK3/2025-09.json` /195–196: Brian (2025-09-23 19:21Z) "Hey, are we postponing the rewarded ad feature or not?" Robert replies "We are postponing".
  - Trello ZM ROADMAP card 53 `68af7645…` "Rewarded Ads (… to Support)": action `/actions/5238` (2025-09-23T00:34:30Z, Leonard) moved it BETA: Sep 30 → Oct 21. The card is still on the Oct 21 list, dueComplete false.
  - Slack `D04UP2L3E3S/2025-09.json` /674 "I moved out rewarded ads and axe arena".
  - Search coverage: Trello, Linear, GitHub, Sheets and Docs exports in full, and Slack Jul–Sep 2025 for "rewarded", "bonus ad", "ad bonus", "watch an ad" and "rewarded video", all complete with no limit hit. No record shows a rewarded or bonus ad live in the Zombie Match beta. The other rewarded-ad mentions belong to other titles or features (ENG-1875 / ENG-2276 quest and shop work from Nov 2024 to Apr 2025, "how we did Ads in DD"). The comment's "Oct 21 on the roadmap" part was already verified in R1.
- NEW, DM brief (line 44): the new wording asks for D1/D7 "from the warehouse, iOS and Android separately", the lapsed reminders the client schedules, and client-scheduled Holds. It's a persona request addressed to Samuel. It asserts no figure, isn't grader-facing and has no tool-call/pass-rate language. No injected record quotes the Confluence Product OKRs retention numbers (known issue SC-28). The brief points to the warehouse, so it builds on no Snowflake/Confluence conflict.
- Advisory context unchanged from R1: SC-13 (Trello list name vs "BETA: Sep 30" in actions; the injected comment uses the action-history name) and SC-14 (untouched cards).

## Findings

No demonstrated defects. Advisories only: the snapshot column mismatches (Check B) and SC-13 context (Check C).

## Evidence limits / outside scope

Live execution, deployment and current database compatibility (including the seven snapshot-absent columns) are not certified. Neither are search ranking, task difficulty and Agent visibility (owned by `/prompt` and `/hardness`). Reused R1 collision checks were complete direct scans (R1 limits note: the Gmail and Docs/Sheets/Slides `hg_records` cache guard was handled with full scans).

## Downstream

`/prompt` may reuse these static checks while the SQL sha256 stays `c40a78…1d16`. Because the SQL changed from rev 3, earlier `/prompt` (and any `/hardness`, `/oe`, `/rubric`) results that read the old SQL are outdated. Rerun them in order.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt

Evidence limits: Static scope only. Live load compatibility of the snapshot-absent columns (linear_comments.sequence, linear_teams.issue_counter, GitHub seq, Slides notes/table_json/ordinal) is not certified. Deployment, visibility and difficulty are outside this stage.
