# /injection — Injection data-integrity review

## Scope

| Field | Value |
|---|---|
| Review | `/injection`, chat attachment review, attempt 6aeed82596dcfe103f9f74d9 |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. Records changed since the last review, and every collision check, were checked NEW. Facts about unchanged records are marked REUSED where noted, and the main numeric fact (the SVB totals) was recomputed NEW |
| Review time | 2026-11-08T11:47:03Z |
| Universe | `Universe_Normal` (Feb 14, 2026 normal); manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` (unchanged since the last review) |
| Fixed clock | 2026-02-14 00:00 UTC |
| Input | `Evals/task_inputs/01_Universe_Inject.sql` (uploaded as `01_Universe_Inject (7).sql`), 74,853 bytes, sha256 `a52191c3efc1bd4a03d13024218305650928fa6f3e2535ce10cbc2d5338f7253`, input-store revision 5. It replaces revision 3 (sha256 `872bbb30…279fd`, reviewed PASS 2026-11-08T05:02:44Z) |
| References | Eval 0 sha256 `e034019b…6eff` (unchanged); WORKFLOW sha256 `d5702ee2…3e33` (changed since the last review, so reuse is limited to raw base facts); schema snapshot `injection.json` `31dcb2b4…5151` (unchanged); `id_contracts.json` `fc4711ef…4682` (unchanged); ENVIRONMENT `b0b45005…d721`; SEARCH `cab83c61…a45c` |
| Lint | `hg_injection_lint.py` `injection-lint-v1` on the same SQL hash |

## Input / authority issues

None. 126 statements: 123 INSERT, 2 UPDATE, 1 trailing `COMMIT`. **Unlike revision 3, the file no longer opens with `BEGIN;`** (see Check B). The only SQL comments are section banners (`-- ===== GDOCS =====` and so on; the GDRIVE banner was removed). None of them mention padding, tool calls or pass rates. Nothing is executed.

### Changes from the previously reviewed revision (line-level diff)

| Change | Revision 3 | Revision 5 (this review) |
|---|---|---|
| Lines 1–2 | `BEGIN;` + GDRIVE banner | removed; the file starts at the first `INSERT INTO gdrive.drive_files` |
| gdocs body (`f_6feda53b…`) | 2,180 chars | 2,307 chars: adds "Leave Combo Fighter’s revenue off for now, on the page, on the deck and when you tell me, until we’ve checked its first sales." Style runs re-split: 1920–2151 and 2152–2307 |
| ENG-2454 comment `comment_e89f05a3…` (Arthur) | "paid him direct for this one, not through Leapblock" | "paid him direct for **his laptop**, not through Leapblock" |
| ENG-2455 | 2 comments, updated_at 00:43:26Z | new 3rd comment `comment_990674712ad0127e26f780eadb5418ea` (Leonard, 00:45:13Z): "her contract had her running our paid UA on telegram, so she’s marketing, not build"; updated_at 00:45:13Z |
| ENG-2456 … ENG-2459 | comments 00:44:39Z … 00:57:16Z | the same comments re-timed 00:45:40Z … 00:58:46Z; each issue's updated_at moved to match |

## Checklist

- [x] Saved/reloaded SQL; hash, base manifest and review version recorded (NEW)
- [x] Lint run; every flag resolved (NEW): 0 FAIL / 0 CHECK / 0 INFO
- [x] Every statement and affected record inventoried (NEW, from a full diff and a parse of all 126 statements)
- [x] Check A: references, targets, collisions (all rerun NEW over complete collections), ID contracts, Drive readability, one account per person
- [x] Check B: structure, transaction boundary, generated columns, Linear text dates, NOT NULL `state_history_json`, JSON shapes, doc style runs (NEW); snapshot comparison (REUSED, same snapshot hash and same column lists)
- [x] Check C: clock and chronology for all records (NEW); Linear durations and order for all 22 issues (NEW); SVB totals recomputed (NEW); changed comments checked against base Slack (NEW); facts about unchanged records (REUSED, see C3)

## Lint flags and resolutions

| Flag | Count | Resolution |
|---|---|---|
| FAIL (future_date, id_contract, drive_unreadable, duplicate_account, actor_name, generated_column, text_time_format, missing_required, json_shape) | 0 | none raised |
| CHECK (unknown_actor, grader_language, padding_comment) | 0 | none raised. A manual read of the changed text (doc sentence, ENG-2454 and ENG-2455 comments) found no grader-facing or test-describing language |
| INFO | 0 | none |

The lint loaded these base lists: contacts, slack/users, trello, gmail/users, linear, confluence_working. It counted rows per table: drive_files 3, docs 1, spreadsheets 1, sheets 1, presentations 1, pages 5, page_elements 5, slack_messages 3, trello cards 1 / actions 2 / boards UPDATE 1, gmail threads 5 / messages 8, gcal events 3, contacts 1, linear projects 1 / issues 22 / comments 60 / teams UPDATE 1.

## Operation ledger

Base paths are relative to `Universe_Normal/`. "OK" means the reference resolves and no collision was found in the full collection listed. The collision counts are this run's lookups (NEW).

| # (SQL line) | Table | Op | Record(s) | Key references / values | Check result |
|---|---|---|---|---|---|
| 1 (1–6) | gdrive.drive_files | INSERT ×3 | `f_6feda53b2382c63bf47b25` (Doc), `f_3304033843904a426f3c00` (Sheet), `f_a4b3c4287a4314d8e532e1` (Slides) | parent `d_63fffeb4fab5233ed5bb73` (Leonard's root folder); owner leonard.hayes; shared with robert and arthur.blake; created 2026-02-12T22:44–23:52Z, modified ≤ 2026-02-13T00:41:06Z (rows unchanged from rev 3; references REUSED) | OK. lookup `/drive_files` id: 0 of 3 found, 53,866 records, scan complete |
| 2 (8–9) | gdocs.docs_documents | INSERT | `f_6feda53b2382c63bf47b25` | **changed body**: decoded length 2,307; last style run ends at 2307; all 10 runs line up with the paragraph breaks (NEW parse) | OK, readable. lookup document_id: 0 found / 633 |
| 3 (11–14) | gsheets.sheets_spreadsheets / sheets_sheets | INSERT ×2 | `f_3304033843904a426f3c00`, sheet 0 | row 2 "All USD notices, by date" 984,888.21 / 608,820.50 / 73,685.61 | OK. lookup: 0 found / 398. Figures recomputed NEW (C3) |
| 4 (16–37) | gslides presentations / pages ×5 / page_elements ×5 | INSERT ×11 | `f_a4b3c4287a4314d8e532e1`, slides `slide_876d…` … `slide_8f7e…` | "$985K / $609K / $74K"; "What each brought in: to fill in" | OK. lookup presentation_id: 0 found / 164. Page/element keys are distinct per (presentation, slide) |
| 5 (39–42) | slack.slack_messages | INSERT ×2 | `fa707da5…`, `f5b759f3…` in C0ADGSZKR3R (#winddown) | EMPLOYEE_0038 = Leonard; mentions EMPLOYEE_0016 = Robert; 01:23:41Z / 01:24:19Z (unchanged; membership REUSED) | OK |
| 6 (43–44) | slack.slack_messages | INSERT | `6312d121…` in C05URGU759U (#leapblock) | EMPLOYEE_0024, 08:37:26Z (unchanged) | OK. Slack lookup id over `messages/*.json`: 0 of 3 found, 687,230 records, 5,353 files, complete |
| 7 (46–47) | trello.trello_cards | INSERT | `698e55f9af74d68d679de7b3`, idShort 456 | board `640643a3…`, list "To Do" (unchanged) | OK. lookup: 0 found / 803 |
| 8 (48–51) | trello.trello_actions | INSERT ×2 | createCard `…de737`, commentCard `…0fde` | PERSON_6094 = Leonard; 22:36:41Z / 23:55:07Z | OK. lookup: 0 found / 5,294 |
| 9 (52) | trello.trello_boards | UPDATE | `640643a3fd8f3ca308d9318e` | dateLastActivity → 2026-02-12T23:55:07Z (= latest injected action) | OK |
| 10 (54–71) | gmail threads ×3 / messages ×6 | INSERT | "Chase records" (Arthur → Leonard, Robert; Leonard reply) | rows unchanged; Message-IDs, In-Reply-To chain, offsets REUSED | OK. All 5 thread numbers and all 4 Message-ID tokens: 0 matches over 88,726 thread files, complete (NEW) |
| 11 (72–79) | gmail threads ×2 / messages ×2 | INSERT | "Invitation: Angel calls" | unchanged | OK (included in the scan above) |
| 12 (81–86) | gcal.gcal_events | INSERT ×3 | `evt_cdc76b69…`, `evt_f21476dc…`, `evt_351ff9bb…` | start 2026-02-17T17:00Z (plan field), created 01:31:17Z | OK. lookup event_id: 0 found / 11,130 |
| 13 (88–89) | contacts.contacts | INSERT | `564155d70112411151e512a6` Lauren Brooks, lauren@harmonygames.co | Slack user EMPLOYEE_0035 "Lauren Brooks" lauren@harmonygames.co (`slack/users.json`) | OK. lookup: 0 found / 170; no second account |
| 14 (91–92) | linear.linear_projects | INSERT | `0742c172-…-316e5c8cb187` "Payee history" | team_ENG; lead usr_63ff = leonard.hayes | OK. lookup: 0 found / 2 |
| 15 (93–…) | linear.linear_issues | INSERT ×22 | ENG-2438 … ENG-2459 | creator usr_63ff; `Backlog`; `state_history_json '[]'`; all 27 columns given; updated_at = the issue's last comment for all 22 (NEW check) | OK. lookup id and identifier: 0 found / 3,852; base ENG max number 2437 |
| 16 (…) | linear.linear_comments | INSERT ×60 | 60 distinct `comment_<32 hex>` ids, including new `comment_990674712ad0127e26f780eadb5418ea` | authors usr_63ff (49) and usr_cc3e = arthur.blake (11), both with `tmem_team_ENG_*` memberships (NEW read of `linear/data.json` `/users`, `/team_memberships`) | OK. 60/60 unique in SQL; base `/comments` holds 0 records |
| 17 (last–1) | linear.linear_teams | UPDATE | team_ENG `issue_counter = 2459` | = highest injected number | OK (column not covered by the snapshot, see B) |
| 18 (last) | — | COMMIT | — | no matching `BEGIN` (see B) | Advisory |

## Check A — Records, references and IDs: PASS

- **Collisions (NEW):** every newly inserted key was checked against its complete base collection with the counts in the ledger, and none is found. Inside the SQL, ids are distinct per table; slide pages/elements repeat only the parent presentation id, as intended.
- **Actors and targets:** the new comment's author `usr_63fffeb4fab5233e` is leonard.hayes and a team_ENG member. Arthur's changed ENG-2454 comment is by `usr_cc3e90160f490686` = arthur.blake. The other references are on unchanged rows and resolve as recorded in the previous review (REUSED: same SQL text, same base manifest, and the base source hashes were checked again by this run's verified-index lookups).
- **ID contracts:** Gmail `history_id` is NULL on all threads. No Drive `content_path` is used. The Doc is readable through its gdocs row (non-empty body, 2,307 chars).
- **One account per person:** the Lauren Brooks contact matches the single Slack user EMPLOYEE_0035 (lauren@harmonygames.co). No existing contact has that email.

## Check B — SQL structure and supported schema rules: PASS

- All 126 statements parse (lint plus an independent parse of the Linear rows); column and value counts match. `E''` escapes decode correctly; the doc's ’ characters are literal UTF-8.
- Generated columns `text_fts` and `body_text_fts` are not set. Linear dates use `YYYY-MM-DDTHH:MM:SSZ` (checked on all 60 comments and 22 issues). `state_history_json` = `'[]'` on every issue. JSON shapes are clean (lint).
- **Transaction boundary (advisory, not a defect):** revision 5 removed the opening `BEGIN;` but kept the closing `COMMIT;`. On PostgreSQL a `COMMIT` with no open transaction only gives a warning ("there is no transaction in progress"), so this statically shows no load error. But if the runner executes statements one at a time, they are no longer all-or-nothing: a failure in any one statement (for example a column the snapshot doesn't cover, below) would leave a partial overlay instead of rolling back. Smallest fix: put `BEGIN;` back as the first line, or remove the final `COMMIT;`.
- **Provisional snapshot comparison (advisory, REUSED, same snapshot hash and same column lists):** MATCH for every table except these columns, which the snapshot does NOT COVER: `linear.linear_projects.links_json`, `linear.linear_teams.issue_counter`, `gslides.slides_pages.notes`, `gslides.slides_page_elements.table_json` and `ordinal`. The snapshot is unverified, so this is a disclosed compatibility limit only.

## Check C — Dates, relationships and consistency: PASS

**C1. Clock (NEW).** Every event timestamp falls between 2026-02-12T22:36:41Z and 2026-02-13T17:08:37Z, before 2026-02-14 00:00 UTC. The only later dates are the calendar start/end on Tue 2026-02-17, which are plan fields.

**C2. Chronology (NEW for the changed records).**
- On all 22 issues, every comment comes after its issue's created_at, comments are in order, each comment has created_at = updated_at, and issue updated_at equals the last comment. Comments run one issue at a time without overlap, from 23:36:28Z to 00:58:46Z. For example ENG-2455 ends at 00:45:13Z and ENG-2456 starts at 00:45:40Z.
- `time_in_status_minutes` equals floor(minutes from created_at to the clock) for all 22 issues (for example ENG-2455: 23:21:11 → 1478). The re-timing changed only comment times and updated_at, not created_at, so the durations are unchanged and still correct.
- The last Linear comment (00:58:46Z) comes before Leonard's #winddown request at 01:23:41Z, which says the payees are already in the project. The doc's modified_time (00:41:06Z) comes before that Slack post, which calls it "the doc I just wrote". The calendar event and invites (01:31Z) follow.

**C3. Facts.**
- *SVB totals (NEW recomputation):* across 987 matching notice messages (complete scan), robert@harmonygames.co has 132 unique "Payment Processed" notices, first dated 2023-09-05 and last 2026-02-02. Summing the USD notices by Transaction Date over the doc's windows (≤ 2025-01-08 / 2025-01-09 – 2025-11-23 / ≥ 2025-11-24) gives **984,888.21 / 608,820.50 / 73,685.61**, exactly the sheet row. The deck's $985K / $609K / $74K are those figures rounded.
- *ENG-2454, changed to "paid him direct for his laptop, not through Leapblock" (Arthur) (NEW):* the base supports it. In `slack/messages/C04UEQVDVB7/2025-10.json`: /500 Leonard (2025-10-29) "reminder for laptop follow-up for Martin"; /522 Leonard (2025-10-30 17:14Z) "did you handle Martin’s laptop?"; /523–/525 Arthur (EMPLOYEE_0025 = Arthur Blake) "not yet, but thats on my list … we are doing that as direct wire, right?", Leonard "yeah"; /529 Arthur "Martin's is ready for approval". The matching notice is Martin [PERSON_NAME_7250] Walsh ***3801, 1,999.00 BGN, Transaction Date Oct 30 2025. This also agrees with Leonard's next comment on the same issue, "Blake ran it, I approved".
- *ENG-2455, new comment "her contract had her running our paid UA on telegram, so she’s marketing, not build" (Leonard) (NEW):* consistent with the base.
  - `C05KNDCHAAG/2025-10.json` /26: Leonard's welcome says Lauren "will lead our Telegram distribution strategy, starting with a focused experiment on Domino Delights". The technical work goes to Arthur "and a few folks", not to her.
  - `C07C2866011/2025-10.json` /526 and /535: the offer Leonard drafted is a Telegram-only profit share whose "Direct costs" include "UA on Telegram", on "assets [she] manages". /630: "sent this contract out" (Consulting Agreement Lauren Brooks.pdf). /639: "signed the contract".
  - `C09KU8U4DPF/2025-10.json` /15, /21: she is sent marketing material and asked about running playables and videos.
  - The notices show 500.00 USD to [PERSON_NAME_7249] Brooks ***5384 on Oct 30 2025, Dec 01 2025 and Jan 06 2026, matching "the contract I sent out in Oct, $500 a month" and "direct wire from me, not through Deel" (Slack /520–/521, 2025-10-30: "Let me do [her] as a direct payment … $500 I’ll do a wire").
  - The contract PDF itself has no readable bytes in the export (Slack file `F09KR391A91`). Its wording can't be quoted, but no base record says she did build work.
- *Doc sentence "Leave Combo Fighter’s revenue off … until we’ve checked its first sales" (NEW):* consistent with the deck, whose revenue slide already reads "What each brought in: to fill in". No injected record states a Combo Fighter revenue or sales figure.
- *ENG-2456 … 2459 re-timed comments:* the text is unchanged, so the date checks against the notices still hold (REUSED from the previous ledger: PERSON_6074 2025-03-21 "paid Mar 2025"; [PERSON_NAME_9100] after the raise; [PERSON_NAME_0054] 500 on 2025-05-29; Private Entrepreneur 125 on 2024-05-07 "spring 2024", returned and re-sent through Payoneer).
- *Unchanged records (REUSED, raw base facts with the record/pointer recorded in the previous review):* the Leapblock close-out (30 wires / 407,944, one of 33,290 only "Awaiting Approval", gmail `threads/00001577.json`); this run's recount finds 29 Leapblock-like Processed notices, as before. Also reused: Arthur's JPMorgan ***3203 4,000.00 USD on Aug 19 2024 (`threads/00006272.json`, re-read NEW in this run) and the memory comments on ENG-2438 … ENG-2453.

**C4. Grader-facing text.** None found in the changed text. The new doc sentence and the two comments are in the personas' voices and address colleagues.

**Advisories (not defects, no change required by this stage):**
- **NB-26 (Combo Fighter sales: none or two).** The new doc sentence "until we’ve checked its first sales" sits next to this conflict: the Confluence QA runbook says no purchase was ever recorded, while Robert says in Slack "2 people bought rotation pack". The sentence keeps Combo Fighter revenue out of the deliverable, which avoids the conflict. Its phrase "its first sales" assumes some sales happened, but no injected record says how many. `/prompt` decides whether the task depends on it; keep the rubric and OEs off whether Combo Fighter sold anything.
- NB-23 (Singular invoice totals) and NB-24 (no base Linear comments) apply as in the previous review. This SQL builds Singular only from the SVB wires and adds its own comments.
- The doc still points to "the warehouse’s daily revenue table" (Snowflake) for Domino Delights and ZM lifetime revenue. No injected record touches Snowflake. `/prompt` should confirm those figures.

## Findings

No demonstrated defects. One structural advisory: the `COMMIT;` has no matching `BEGIN;` (Check B). Restore `BEGIN;` at the top to keep the overlay all-or-nothing.

## Final summary

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All new keys checked NEW against complete collections (Drive 53,866; Docs 633; Sheets 398; Slides 164; Slack 687,230 msgs; Gmail 88,726 thread files; Trello 803 cards / 5,294 actions; Calendar 11,130; Contacts 170; Linear 3,852 issues / 0 comments / 2 projects): 0 collisions. Authors resolve; ID contracts, Drive readability and one-account rules met |
| B — SQL structure and supported schema rules | PASS | Structure, Linear formats, NOT NULL and JSON shapes clean; doc style runs match the 2,307-char body. Advisory: `COMMIT` without `BEGIN`; snapshot does NOT COVER 5 columns |
| C — Dates, relationships and consistency | PASS | All events before the clock; all 22 issues' comment order, updated_at and durations correct; SVB totals recomputed exactly; the "laptop" and "paid UA on Telegram" comments are supported by base Slack and the SVB notices |

Stage dependencies for reuse by `/prompt`: SQL sha256 `a52191c3…7253`; universe manifest sha256 `5e01ac44…de450`; schema snapshot sha256 `31dcb2b4…5151`; id_contracts sha256 `fc4711ef…4682`; notice cohort = 132 unique "Payment Processed" notices in robert@harmonygames.co (987 matching messages across mailboxes, complete scan); Slack evidence `C04UEQVDVB7/2025-10.json` /500–/529, `C05KNDCHAAG/2025-10.json` /26, `C07C2866011/2025-10.json` /526, /535, /630, /639.

### FINAL VERDICT: PASS

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt (the earlier /prompt pass read the previous SQL and needs rerunning). Optionally restore `BEGIN;` as the first line. That would be a new SQL version, so /injection would need to run again.

Evidence limits: Static review only. No live execution or deployment check. The schema snapshot is unverified and does not cover linear_projects.links_json, linear_teams.issue_counter, slides_pages.notes or slides_page_elements.table_json/ordinal. Without `BEGIN;`, a runtime failure in any one statement would not roll back the rest. Lauren Brooks's contract PDF has no readable content in the export, so the ENG-2455 comment was checked against the Slack offer and welcome text instead. Agent visibility and task difficulty are out of scope.
