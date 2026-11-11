# /injection — Injection data-integrity review

## Scope

| Field | Value |
|---|---|
| Review | `/injection`, chat attachment review, attempt 6aeed82596dcfe103f9f74d9 |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1` (no evidence reused; all checks NEW) |
| Review time | 2026-11-08T05:02:44Z |
| Universe | `Universe_Normal` (Feb 14, 2026 normal); manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Fixed clock | 2026-02-14 00:00 UTC |
| Input | `Evals/task_inputs/01_Universe_Inject.sql` (uploaded as `01_Universe_Inject (3).sql`, identical to the two earlier uploads), 74,429 bytes, sha256 `872bbb30771099c1d72d7121c9a9d195f056839043854ef63dd74223eb0279fd`, input-store revision 3 |
| References | Eval 0 sha256 `e034019b8ec450437509a73dd3bae2d303b57561b0f67fcc1e5d19266f663eff`; WORKFLOW sha256 `ee4cd8e1cc291c3b733bfd53907f073f3c8dcbfbbec4723b978a1e4a504fcd5d`; schema snapshot `injection.json` sha256 `31dcb2b43feca8e5c7cb67f37973f819c9b9774f12f8b15cb7da89ecd74c5151`; `id_contracts.json` sha256 `fc4711ef07667333c1cf2a417279826f0432539195f7acdfacfa86e9d9ed4682`; scoring.json sha256 `c14873e614cdcda5190db761e6fd0922111991308dace2e1ccd3de8ad789e5bc` |
| Lint | `hg_injection_lint.py` `injection-lint-v1` on the same SQL hash |

## Input / authority issues

None. The SQL is one `BEGIN … COMMIT` transaction with 126 statements (122 INSERT, 2 UPDATE). Nothing is executed. SQL comments are only section banners (`-- ===== GDRIVE =====` and so on), with no padding or tool-call/pass-rate wording.

## Checklist

- [x] Saved/reloaded SQL; hash, base manifest and review version recorded (NEW)
- [x] Lint run; every flag resolved (NEW): 0 FAIL / 0 CHECK / 0 INFO
- [x] Every statement and affected record inventoried (NEW)
- [x] Check A: references, targets, collisions, ID contracts, Drive readability, one account per person (NEW)
- [x] Check B: structure, generated columns, Linear text dates, NOT NULL `state_history_json`, JSON shapes, snapshot comparison (NEW)
- [x] Check C: chronology vs clock, cross-record facts against the base SVB notices, Slack/Gmail/Trello/Linear consistency (NEW)

## Lint flags and resolutions

| Flag | Count | Resolution |
|---|---|---|
| FAIL (future_date, id_contract, drive_unreadable, duplicate_account, actor_name, generated_column, text_time_format, missing_required, json_shape) | 0 | none raised |
| CHECK (unknown_actor, grader_language, padding_comment) | 0 | none raised. A manual read of all injected text found no grader-facing or test-describing language either |
| INFO | 0 | none |

The base lists the lint loaded: contacts, slack/users, trello, gmail/users, linear, confluence_working.

## Operation ledger

Base paths are relative to `Universe_Normal/`. "OK" means the reference resolves and no collision was found in the full collection listed.

| # (SQL line) | Table | Op | Record(s) | Key references / values | Check result |
|---|---|---|---|---|---|
| 1 (3–8) | gdrive.drive_files | INSERT ×3 | `f_6feda53b2382c63bf47b25` (Doc "Angel note: how to count the money"), `f_3304033843904a426f3c00` (Sheet "Angel note working"), `f_a4b3c4287a4314d8e532e1` (Slides "Note to angels (draft)") | parent `d_63fffeb4fab5233ed5bb73` = Leonard's root folder (`gdrive/data.json` `/drive_files/9034`); owner leonard.hayes, shared writer robert + arthur.blake (all in `/drive_users` 7, 13, 20); created 2026-02-12T22:44–23:52Z, modified ≤ 2026-02-13T00:41:06Z | OK. No ID collision across 53,866 drive_files |
| 2 (10–11) | gdocs.docs_documents | INSERT | `f_6feda53b2382c63bf47b25` | body_text 2,180 chars, non-empty; style_runs end at 2180 = body length; drive_file_id matches | OK, readable. No collision across 633 docs |
| 3 (13–16) | gsheets.sheets_spreadsheets / sheets_sheets | INSERT ×2 | `f_3304033843904a426f3c00`, sheet 0 | grid 2×8 = row_count 2, column_count 8; row 2 "All USD notices, by date" 984,888.21 / 608,820.50 / 73,685.61 | OK. No collision across 398 spreadsheets. Figures verified (C3) |
| 4 (18–39) | gslides.slides_presentations / slides_pages ×5 / slides_page_elements ×5 | INSERT ×11 | `f_a4b3c4287a4314d8e532e1`, slides `slide_876d…`…`slide_8f7e…` | "$985K / $609K / $74K" = sheet figures rounded | OK. No collision across 164 presentations |
| 5 (41–44) | slack.slack_messages | INSERT ×2 | `fa707da5…`, `f5b759f3…` in C0ADGSZKR3R (#winddown) | user EMPLOYEE_0038 = Leonard Hayes; mentions EMPLOYEE_0016 = Robert; both are channel members (`slack/channels.json` `/154`); ts 1770945821 / 1770945859 = created_at 01:23:41Z / 01:24:19Z | OK. IDs absent from all 5,353 message files (687,230 records); ts absent from both channels' files |
| 6 (45–46) | slack.slack_messages | INSERT | `6312d121…` in C05URGU759U (#leapblock) | user EMPLOYEE_0024, a channel member (`/51`) and the Leapblock-side contact in base #leapblock (e.g. Jan 27 "here is the new invoice", Feb 12 call with Leonard); ts 1770971846 = 08:37:26Z | OK |
| 7 (48–49) | trello.trello_cards | INSERT | `698e55f9af74d68d679de7b3`, idShort 456 | board `640643a3fd8f3ca308d9318e` (`/boards/1`), list "To Do" `…93195` (`/lists/3`); idShort 456 unused (base max 455); shortLink/shortUrl NULL like base cards; badges.comments 1 = one commentCard | OK. No collision across 803 cards |
| 8 (50–53) | trello.trello_actions | INSERT ×2 | `698e55f9…de737` createCard, `698e685b…0fde` commentCard | idMemberCreator PERSON_6094 = Leonard Hayes (`/members/2`); id timestamp prefixes 0x698e55f9 = 22:36:41Z and 0x698e685b = 23:55:07Z match `date` | OK. No collision across 5,294 actions |
| 9 (54) | trello.trello_boards | UPDATE | `640643a3fd8f3ca308d9318e` | dateLastActivity 2025-11-12T17:25:43Z → 2026-02-12T23:55:07Z (= latest injected action) | OK |
| 10 (56–73) | gmail.gmail_threads ×3 / gmail_messages ×6 | INSERT | "Chase records" thread: copies in arthur.blake (SENT), robert, leonard.hayes; reply from leonard (SENT in his copy) | Message-IDs `<CAOOpSqA…>`, `<CAPBs_a5…>`; internal_date 1771000004000 / 1771002517000 = date 16:26:44Z / 17:08:37Z; header offsets -0500 (Arthur, ET) and -0800 (Leonard, PT); reply quotes "8:26 AM" = 16:26Z in PT; In-Reply-To/References chain correct; Label_b19fb8d1b3 = "Opened" (exists in `gmail/labels.json`); history_id NULL | OK. Thread numbers and Message-IDs absent from all 88,726 thread files |
| 11 (74–81) | gmail.gmail_threads ×2 / gmail_messages ×2 | INSERT | "Invitation: Angel calls" to robert and arthur.blake | internal_date 1770946280000 = 01:31:20Z; Tue Feb 17 9:00 PST = 12:00 EST = 17:00Z | OK, no collision |
| 12 (83–88) | gcal.gcal_events | INSERT ×3 | `evt_cdc76b69…`, `evt_f21476dc…`, `evt_351ff9bb…` on the leonard/robert/arthur calendars | the three calendars exist (`/calendars/15, 29, 0`); one shared ical_uid with distinct event_ids and a per-copy `self` flag, matching the base convention; start 2026-02-17T17:00Z (plan field), created 01:31:17Z | OK. No collision across 11,130 events (event_id and ical_uid) |
| 13 (90–91) | contacts.contacts | INSERT | `564155d70112411151e512a6` Lauren Brooks, lauren@harmonygames.co, "Telegram Contractor" | lauren@harmonygames.co is "Lauren Brooks" in base Gmail (e.g. "Canceled event: All Hands … (Lauren Brooks)", Dec 24 2025) and was invited to "Telegram Kickoff", Oct 13 2025. No existing contact with this email or name (only Oliver Brooks) | OK. No collision across 170 contacts; no second account |
| 14 (93–94) | linear.linear_projects | INSERT | `0742c172-…-316e5c8cb187` "Payee history" | team_ENG (`/teams/2`); lead `usr_63fffeb4fab5233e` = leonard.hayes (`/users/13`); start_date `2026-02-12`; created 2026-02-12T23:12:43Z | OK. No collision (2 projects; name unused) |
| 15 (95–…) | linear.linear_issues | INSERT ×22 | ENG-2438 … ENG-2459 (numbers 2438–2459) | team_ENG; creator Leonard; state_id `Backlog` (a literal base state, 34 ENG uses); `state_history_json '[]'`; every `*_at` in `YYYY-MM-DDTHH:MM:SSZ`; time_in_status 1476–1486 min = minutes from each created_at to the clock; updated_at = that issue's last comment | OK. No id/identifier collision across 3,852 issues; base ENG max is 2437 |
| 16 (95–…) | linear.linear_comments | INSERT ×59 | 59 distinct `comment_<32 hex>` ids | authors Leonard (`usr_63ff…`) and Arthur Blake (`usr_cc3e…`), both team_ENG members (`tmem_team_ENG_*`); created 2026-02-12T23:36:28Z … 2026-02-13T00:57:16Z, each after its issue's created_at | OK. Base has 0 Linear comments, so no collision |
| 17 (last) | linear.linear_teams | UPDATE | team_ENG `issue_counter = 2459` | equals the highest injected number; base ENG max 2437 | OK (column not in snapshot, see B) |

## Check A — Records, references and IDs: PASS

- **Actors and targets:** every actor, parent and target in the ledger resolves in the base: Drive folder and users, Slack channels/users/memberships, Trello board/list/member, Gmail mailboxes and label, calendars, Linear users/team/memberships. Each author id matches the person the record names (EMPLOYEE_0038 = Leonard Hayes, EMPLOYEE_0016 = Robert, PERSON_6094 = Leonard Hayes, usr_cc3e = arthur.blake).
- **Collisions:** all new keys were checked against the complete collections (counts in the ledger), and none collide. The Linear numbering continues from the base ENG maximum (2437) without overlap. Trello idShort 456 is unused.
- **ID contracts:** Gmail `history_id` is NULL on all threads. No Drive `content_path` is used: the Google-native files are served by their gdocs/gsheets/gslides rows, and the Doc body is non-empty.
- **One account per person:** the new contact is the base Lauren Brooks (lauren@harmonygames.co) and has no existing contact row, so this adds no second account.
- **Payee references:** each Linear issue names an SVB payee and account ending. All 22 resolve to real "SVB Payment Notification: Payment Processed" notices in robert@harmonygames.co's mailbox (132 unique notices). Two of them also cover the base's alternate spellings: Deel's "[ORG_NAME_0057], Inc." (same account 8380, as the Deel comment says) and Singular's "[SOURCE_ORG_0351] Labs Inc" (same account 4015). Together the 22 issues cover every payee/account on those notices.

## Check B — SQL structure and supported schema rules: PASS

- Statements are well formed and column/value counts match (the lint parsed all 126). `E''` strings escape correctly, and doubled quotes are balanced.
- Generated columns `text_fts` and `body_text_fts` are not set.
- Linear text dates all use the base format, and `start_date` is `YYYY-MM-DD`. Every Linear issue sets `state_history_json` to `'[]'`.
- JSON shapes: `metadata_json` = `'{}'`; Trello `data_json` and `badges_json` are objects; all `*_json` list columns are arrays; gcal `start_json`/`end_json` are objects. The lint found no shape errors.
- **Provisional snapshot comparison (advisory only, not a defect):** MATCH for every table except these columns, which the bundled snapshot does NOT COVER: `linear.linear_projects.links_json`, `linear.linear_teams.issue_counter`, `gslides.slides_pages.notes`, `gslides.slides_page_elements.table_json` and `ordinal`. The snapshot is unverified (schema README), so this is a disclosed compatibility limit only. Note that everything runs in one transaction: if any of these columns is missing in the live database, the whole script would roll back.

## Check C — Dates, relationships and consistency: PASS

**C1. Clock.** Every event timestamp falls between 2026-02-12T22:36:41Z and 2026-02-13T17:08:37Z, before the 2026-02-14 00:00 UTC clock. Only the calendar start/end (Tue 2026-02-17, a plan field) is later, and it is presented as upcoming ("angel calls on tuesday").

**C2. Chronology.** The order is coherent:
1. Sheet (22:44), deck (22:52), Trello card (22:36).
2. Linear project and issues (23:12–23:23), then comments (23:36–00:57).
3. Doc created at 23:52, which comes before the Trello comment "doing this properly now, it's in a doc" (23:55). Doc last modified at 00:41.
4. Slack request "the doc I just wrote" / "I put everyone … into the Payee history project" (01:23–01:24).
5. Calendar event (01:31:17), then the invite emails (01:31:20).

Gmail replies follow their parents. The base #winddown channel ends at 23:04Z on Feb 12, so the injected posts come after it.

**C3. Facts against the base SVB notices** (Robert's mailbox; Leonard's copies give identical totals):
- Sheet and deck "All USD notices, by date": the USD notices summed by Transaction Date over the doc's windows (≤ 2025-01-08, 2025-01-09 to 2025-11-23, ≥ 2025-11-24) give **984,888.21 / 608,820.50 / 73,685.61**, exactly what the sheet shows. $985K / $609K / $74K on the deck are those figures rounded.
- Doc "first SVB wires in Sep 2023 … last run on Feb 2": the first notice is Deel on 2023-09-05 and the last run is 2026-02-02. ✓
- Leapblock Slack close-out (2023 104,868; 2024 232,726; 2025 62,950; 2026 7,400; total 407,944 over 30 wires; first 13 Sep 33,290). The notices show 29 Leapblock wires totalling 374,654 (2023 71,578; 2024 232,726; 2025 62,950; 2026 7,400). The difference is exactly one wire of 33,290, and the base has an SVB "Payment Awaiting Approval" for Leapblock ***1359, 33,290.00 USD, Transaction Date Sep 13 2023 (gmail thread `00001577.json`), with no Processed notice. The yearly figures add up to the total. The message is consistent with the base, and the doc rule says it overrides the notices for that payee.
- Arthur's "Chase records" email: "$4,000 to JPMorgan ***3203 on the SVB notices in Aug 2024 was me". This matches a notice of 4,000.00 USD on Aug 19 2024 initiated by Arthur and approved by Leonard (`00006272.json`), and agrees with ENG-2450 ("I approved this one in Aug 2024"). A Carta renewal payment-verification email in Aug 2024 exists in Leonard's mail, which supports the "Carta's renewal" context. "Sunset's file" refers to the existing Sunset vendor.
- Linear memory comments against the notice dates. Each is consistent:
  - Eveline wires from 2023-10-27 ("since Oct 2023")
  - BANCO from Apr 2024 ("early 2024")
  - Singular from 2024-09-25 ("from Sep 2024")
  - PERSON_4419 LLC one payment on 2025-01-02 ("Jan 2025")
  - TYZ 2024-02-06 ("wired them in Feb")
  - [PERSON_NAME_36400] Sep–Nov 2024 ("from Sep 2024 … until Dec 2024")
  - AppLovin from 2025-08-29 ("Aug 2025")
  - Graham 2025-05-29 ("end of May")
  - CREATIVE X 2025-05-16 ("May 2025")
  - M 2023-10-27 ("Oct 2023 … next payday")
  - Nathan 2024-08-02 ("ended late Jul 2024")
  - Martin Walsh 1,999 BGN on 2025-10-30 ("Oct 2025")
  - Brooks 3 × 500 from 2025-10-30 ("contract … in Oct, $500 a month")
  - PERSON_6074 2025-03-21 ("paid Mar 2025")
  - [PERSON_NAME_0054] 500 on 2025-05-29 ("$500 … end of May 2025")
  - Private Entrepreneur 125 on 2024-05-07 ("spring 2024")
  - Leapblock last wire 2026-02-02 ("Martin paid through Jan 2026"), which matches base #leapblock "We paid him until end of January".
- Durations: Linear `time_in_status_minutes` equals the floor of the minutes from created_at to the fixed clock (for example ENG-2438: 23:13:29 → 00:00 = 1,486.5 → 1486).

**C4. Grader-facing text.** None found. The doc and the Slack messages are written in the persona's voice and address colleagues. Whether the doc spells out too much is a task-design question for `/prompt` and `/hardness`, not an injection defect.

**Advisories (not defects, no change required by this stage):**
- The doc names "the warehouse's daily revenue table" (Snowflake) for each game's lifetime revenue. No known base issue for lifetime revenue was found in `guidelines/known_data_issues.md`, but no injected record touches Snowflake. `/prompt` should confirm the revenue figures from the warehouse.
- Known issue NB-23 (Singular invoice INVSINC22671 has two totals) is near this scenario. The SQL builds Singular only on the SVB wires (25,000 on 2024-09-25 and 6,250 on 2025-09-26), not on the invoice. Keep any Singular "as billed" total out of grading.
- NB-24 (base Linear has no comments) does not affect this SQL. It adds its own comments, and nothing grades a base comment.

## Findings

No demonstrated defects.

## Final summary

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All references resolve; no collisions over complete collections; ID contracts, Drive readability and one-account rules met; all 22 payee issues map to real notices |
| B — SQL structure and supported schema rules | PASS | Structure, generated columns, Linear formats, NOT NULL and JSON shapes clean. Snapshot NOT COVERED for 5 columns (advisory, see B) |
| C — Dates, relationships and consistency | PASS | All events before the clock; chronology coherent; sheet, deck, Leapblock, JPMorgan and Linear facts reconcile with the base notices |

Stage dependencies for reuse by `/prompt`: SQL sha256 `872bbb30…279fd`; universe manifest sha256 `5e01ac44…de450`; schema snapshot sha256 `31dcb2b4…5151`; notice cohort = 132 unique Payment Processed notices in robert@harmonygames.co (329 notice messages across leonard.hayes, robert and arthur.blake).

### FINAL VERDICT: PASS

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt

Evidence limits: Static review only. No live execution or deployment check. The schema snapshot is unverified and does not cover linear_projects.links_json, linear_teams.issue_counter, slides_pages.notes, or slides_page_elements.table_json/ordinal (advisory; the script is a single transaction). Agent visibility and task difficulty are out of scope.
