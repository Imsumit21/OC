# /injection — Injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`: the 8 changed statements checked NEW; the 125 byte-identical statements' results REUSED from the prior report (see §11) |
| Mode | Chat/attachment review, static (no SQL executed, no base export modified) |
| Attempt | 6adfee3b47f7621feba5b96c |
| Actual review time | 2026-11-05T14:14:08Z |
| Clock | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal`, archive hg4-2026-08-31 v37; manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Input | `Evals/task_inputs/01_Universe_Inject.sql` (revision 6, saved from attachment `_uploads/01_Universe_Inject (3).sql`), 85,772 bytes, sha256 `4236a0301de9f4d287fb4a5be26e1dd6538cabe70f0c69b2031b167be11e1b76` |
| Previous SQL version | revision 4, 85,444 bytes, sha256 `edf1fd9036113b77674d7e2f2c51b31920471b110f6c10c0c51ac3fa16d6cee3` (PASS / COMPLETE in prior report sha256 `3d38911e1850f7eecdd438b0eaab41724d4a154746e5fe96e3467c815c61e287`) |
| References | Eval 0 `e034019b…6eff`; WORKFLOW.md `ee4cd8e1…fcd5d`; schema snapshot `injection.json` `31dcb2b4…5151` (unverified, provisional); `id_contracts.json` `fc4711ef…4682`; lint `hg_injection_lint.py` `a8226e2a…448b` (injection-lint-v1). All re-hashed this run and identical to the prior review. |
| Assignment (context only) | Robert, Co-founder & Creative Director; Executive / Finance / Planning and decision support; long-horizon; easy |

## 2. Input / authority issues

None. The new attachment was saved as the injection input (revision 6) and read before base searches. SQL comments (lines 1–4) are evidence of intent only, with no tool-call, pass-rate or grader content.

**Change set vs the previously reviewed SQL (line diff, NEW):** same 276 lines and 133 statements; every record key, actor, parent and timestamp is unchanged. 8 statements differ, all in text content (plus one derived size field):

| Line | Record | Change |
|---|---|---|
| 62, 66, 70 | Gmail "billing moved to my card" ×3 mailbox copies (`<CA-Uw65DzW6…@mail.gmail.com>`) | Last sentence "then CF's are on the free tier, its volume is tiny." → "and with CF's tiny volume they cost nothing after that, so there's nothing there for the LLC."; size_estimate 1448 → 1490 |
| 127 | Linear project `0fa95761-…` "LLC take-over" | description adds "or pay for" |
| 163 | Linear comment `comment_7a0dea62…` (ENG-2446, Blake) | appends "so the LLC doesn't need them" |
| 183 | Linear comment `comment_8f925764…` (ENG-2451, Leonard) | appends "I'll set CF up on it" |
| 187 | Linear comment `comment_17c00e14…` (ENG-2452, Leonard) | appends "nothing for the LLC to take or pay" |
| 223 | Linear comment `comment_fa730ebd…` (ENG-2461, Leonard) | appends "CF was never on it, its support is the contact on its store listing and that moves with the game" |

## 3. Checklist

- [x] Save/reload SQL; hash, base manifest and review version recorded (NEW)
- [x] `hg_injection_lint.py` run on the new hash: 0 FAIL / 0 CHECK / 0 INFO across 133 statements (NEW)
- [x] Full operation ledger, 131 data statements (129 INSERT, 2 UPDATE) + BEGIN/COMMIT (8 changed rows NEW; others REUSED)
- [x] Check A: references and collisions (changed rows NEW; key collisions REUSED because the key set and base are unchanged)
- [x] Check B: structure and schema rules (NEW via lint; changed size field recomputed NEW)
- [x] Check C: dates, relationships, consistency (changed facts NEW against base Slack/Gmail and the other SQL rows; unchanged cross-checks REUSED)
- [x] Coverage, findings, limits and one final verdict

## 4. Lint flags and resolutions

`hg_injection_lint.py` (injection-lint-v1, clock 2026-02-14T00:00:00Z, SQL sha256 `4236a030…1b76`) loaded base slack/users, trello, gmail/users, github, linear, contacts, confluence and parsed 133 statements (linear_issues 37, linear_comments 37 inserts, etc.). **Flags: none (FAIL 0, CHECK 0, INFO 0).** Nothing to resolve. A clean lint is not a pass, so checks A–C were done below.

## 5. Operation ledger

All statements run in SQL order inside one `BEGIN … COMMIT`. Rows marked CHANGED/NEW differ from the previously reviewed SQL (lines 62, 66, 70, 127, 163, 183, 187, 223). All other rows are byte-identical to revision 4; their results are REUSED from the prior report (sha256 `3d38911e…e287`, §5) under stage-evidence-v1, with the base manifest, references and record keys verified unchanged. There are no deletes or upserts. "Coll." = collision check against the complete base collection plus the other SQL rows.

| SQL lines | Service.table | Op | Record id(s) | Key values / relationships | Base check (path / pointer) | Result |
|---|---|---|---|---|---|---|
| 7–8 | gdrive.drive_files | INSERT | `f_1e468a9d69ea0f0a2001f5` | Google Doc "LLC ground rules…", owner leonard.hayes, parent `d_63fffeb4fab5233ed5bb73`, shared writer robert + arthur.blake, created/modified 2026-02-12T23:46Z | gdrive/data.json `/drive_files` (53,866 rows): parent = Leonard's root folder (owner leonard.hayes); id coll. none | OK |
| 9–10 | gdrive.drive_files | INSERT | `f_a7af6f358dd5648c11a608` | (prev. version change, REUSED) name now "LLC notes (Monday)" (= docs title at line 19), Leonard root, 2026-02-09T23:55Z | same; id unchanged, so REUSED collision result | OK |
| 11–12 | gdrive.drive_files | INSERT | `f_d996e4c434ce160dc52596` | Spreadsheet "LLC 90 days (draft)", Leonard root, 2026-02-10T18:30Z | same | OK |
| 13–14 | gdrive.drive_files | INSERT | `f_7d2c9e7822e87b92a11759` | Presentation "Combo Fighter: next 90 days", owner robert, parent `d_9f7ba94f7526d54d8482ba`, 2026-02-08T03:00Z | parent = Robert's root folder; coll. none | OK |
| 16–17 | gdocs.docs_documents | INSERT | `f_1e468a9d69ea0f0a2001f5` | body_text non-empty (1,214 chars); style runs TITLE 0–59, NORMAL 59–1214 = exact body length | gdocs/data.json `/docs_documents`: coll. none (document_id and drive_file_id) | OK |
| 18–19 | gdocs.docs_documents | INSERT | `f_a7af6f358dd5648c11a608` | (prev. version change, REUSED) title "LLC notes (Monday)"; body_text = title line (19 chars incl. \n) + one note paragraph, 154 chars total; runs TITLE 0–19, NORMAL_TEXT 19–154 = exact body length, no zero-length run | coll. none (REUSED, id unchanged) | OK  |
| 21–22 | gsheets.sheets_spreadsheets | INSERT | `f_d996e4c434ce160dc52596` | drive_file_id = same id, owner Leonard | gsheets/data.json `/sheets_spreadsheets` complete lookup (398 records) on spreadsheet_id and drive_file_id: 0 matches | OK |
| 23–24 | gsheets.sheets_sheets | INSERT | (`f_d996…`, sheet 0) | grid 5 rows × 8 cols; header Item/Game/Decision/Monthly cost/Paid by/Next step/Owner/By | parent spreadsheet created at line 22 | OK |
| 26–27 | gslides.slides_presentations | INSERT | `f_7d2c9e7822e87b92a11759` | owner robert, revision `5493af5cba` | gslides/data.json `/slides_presentations`: coll. none | OK |
| 28–39 | gslides.slides_pages ×3 / slides_page_elements ×3 | INSERT | pages `slide_886d78971206`, `slide_05405983565d`, `slide_34827ed9cf24`; elements `el_7e281c2d6d42`, `el_4f79d571a8ab`, `el_c30917bbd73c` | BLANK layout, TEXT_BOX 9144000×5143500 at ordinal 0, indexes 0–2 | object ids absent from the whole gslides export; layout/kind/size match base pages | OK |
| 41–42 | slack.slack_messages | INSERT | `9ed17488702e4bf387cc012f7bb0a509` | #builds `C05433XK267`, SLACK_BOT_0005 Jenkins attachment "DD iOS Submission - #218 Started by user Arthur Blake", ts 1770932400.314774 = created_at 2026-02-12T21:40:00Z | channels.json: bot 0005 is a member; base DD iOS Submission builds end at #217 (ts 1769620132); ts coll. none | OK |
| 43–44 | slack.slack_messages | INSERT | `85bc96b0aa43bb455a58da9d8b63c060` | #builds, "#218 - Blake/boombitWithEcon Success after 9 min 12 sec … Replace Helpshift with support email. [Arthur Blake]", 21:49:30Z (= 21:40:00 start + 9m12s + post lag) | branch label matches base #216 build branch `Blake/boombitWithEcon` | OK |
| 45–46 | slack.slack_messages | INSERT | `6908b2f17c379e809aafa6b2b169f4bf` | (REUSED) appends "so count it in what the LLC costs"; #prototype `C09UHHN6PFZ`, Leonard (EMPLOYEE_0038), reply in thread `73ec270a…` (ts 1770404397.819789), 2026-02-12T23:20Z | Leonard is a member; parent = messages/C09UHHN6PFZ/2026-02.json `/389` "VO campaign is created…", by Leonard, reply_count 0 and no existing replies | OK |
| 47 | slack.slack_messages | UPDATE | `73ec270a3d07eb8d8488384898be079e` | thread_ts_legacy = own ts, reply_count 1, reply_users_count 1, latest_reply = 1770938400.370665 | before: reply_count 0, latest_reply null, no replies in any month file; after matches the one injected reply; parent-with-replies shape (thread_ts = own ts) matches base | OK |
| 48–49 | slack.slack_messages | INSERT | `ad623a2f0d4387109d108e767b174609` | DM `D04V95AAAHW` (Robert–Blake), Blake (EMPLOYEE_0025), reply in thread `bc4bc3d0…` (ts 1770056235.480619), 2026-02-13T03:10Z, "Domino's prod account is down to $140 a month…" | DM members include EMPLOYEE_0016 (Robert) and EMPLOYEE_0025 (Blake); parent at messages/D04V95AAAHW/2026-02.json `/4`, by Blake, reply_count 0, no replies | OK (advisory A-3) |
| 50 | slack.slack_messages | UPDATE | `bc4bc3d0e2a0ea6ae92cb2a9712e8f76` | reply_count 1, latest_reply 1770952200.665739 | before 0 / null; after consistent | OK |
| 51–52 | slack.slack_messages | INSERT | `6257a3c4456db0bd2aeb872619d7a364` | DM `D04UP2L3E3S` (Robert–Leonard), Leonard, top-level, 2026-02-13T05:40Z (request message) | DM members include EMPLOYEE_0016 and EMPLOYEE_0038; ts coll. none | OK |
| 54–55 | trello.trello_cards | INSERT | `698e6548aa9516b76c4ab475` | board `640643a3fd8f3ca308d9318e` "Harmony Games", list `640643a3fd8f3ca308d93195` "To Do", idShort 456, shortLink NULL, url `…/c/N6TBAK8A/456-llc-what-we-take-from-hg`, dateLastActivity 2026-02-12T23:42Z | trello/data.json: board/list exist and are open; 449 board cards, max idShort 455, so 456 is next and unused; all 449 base cards have shortLink NULL and the same url pattern; card id hex prefix 698e6548 = 2026-02-12T23:42:00Z | OK |
| 56–57 | trello.trello_actions | INSERT | `698e65489a4031a95d3ce53e` | createCard by `PERSON_6094_TRELLO_USER_ID` (Leonard Hayes), same date | member resolves to Leonard; data_json shape matches base createCard actions; coll. none | OK |
| 59–70 | gmail.gmail_threads ×3 / gmail_messages ×3 | INSERT (messages CHANGED, NEW) | threads `arthur.blake@…/1856975772057961391`, `robert@…/1856975772058401508`, `leonard.hayes@…/1856975772058497766`; message `<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>` per mailbox | Blake → Robert + Leonard "billing moved to my card", 2026-02-13T02:35Z (internal_date 1770950100000 matches). **Body last sentence changed** from "then CF's are on the free tier, its volume is tiny." to "and with CF's tiny volume they cost nothing after that, so there's nothing there for the LLC."; size_estimate 1448 → **1490 = body 590 chars + 900** (same offset as every other injected message, NEW); snippet (first 140 chars) unchanged; thread rows (lines 60/64/68) unchanged | keys unchanged → collision result REUSED (all 88,726 thread files, 0 hits); history_id NULL (lint, NEW) | OK |
| 71–82 | gmail threads ×3 / messages ×3 | INSERT | threads `…/1856989298688254292` (leonard), `…/1856989298688559716` (robert), `…/1856989298688898804` (arthur); msg `<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com>` | Leonard → Robert, cc Blake "LLC money", 2026-02-13T06:10Z (1770963000000 matches) | 0 hits | OK |
| 83–94 | gmail threads ×3 / messages ×3 | INSERT | `robert@…/1856994331853686118` + `<136285951.151027292.1770967800000@email.apple.com>`; `arthur.blake@…/1856994331852829558` + `<375944835…457@email.apple.com>`; `leonard.hayes@…/1856994331852922225` + `<883960163…220@email.apple.com>` | App Review (SVC_4131) "We noticed an issue with your submission." for Domino Delights, Guideline 1.5: support option "only opens an email draft… does nothing" without a mail account; asks for a support URL. 2026-02-13T07:30Z. Per mailbox: Robert "Hello [PERSON_NAME_0054]", INBOX/CATEGORY_UPDATES/Label_ad4e31dc09/Label_aeb79a643f, size 1924; Arthur "Hello Arthur", INBOX/CATEGORY_UPDATES/UNREAD, size 1912; Leonard "Hello Leonard", ARCHIVED/CATEGORY_UPDATES/Label_6e8d84b057, size 1913 (each = body + 900); thread snippets (lines 88, 92) = message snippets | all 49 base App Review mails (complete subject scan, 88,728 files): Robert's use [PERSON_NAME_0054] + Label_ad4e31dc09/Label_aeb79a643f; Arthur's 8 use "Hello Arthur" + INBOX/CATEGORY_UPDATES/UNREAD; Leonard's use "Hello Leonard" + ARCHIVED/CATEGORY_UPDATES/Label_6e8d84b057. Injected copies match each mailbox's base pattern. All labels exist in labels.json (`ARCHIVED`, `UNREAD` system; `Label_6e8d84b057` "App Center / Test Flight"). 0 id hits (REUSED, ids unchanged) | OK (advisory A-4) |
| 95–102 | gmail threads ×2 / messages ×2 | INSERT | `robert@…/1856987728970293624` + `<calendar-0b12e6f6-…@google.com>`; `arthur.blake@…/1856987728969768237` + `<calendar-cbc32ea4-…@google.com>` | Invitations "LLC: decide" Mon Feb 16 10:00–10:45 PT / 1:00–1:45 ET (= 18:00–18:45Z), sent 2026-02-13T05:45:03Z | Robert's subject token `([PERSON_NAME_0055])` matches 99 base invite subjects in Robert's mailbox; 0 id hits | OK |
| 104–109 | gcal.gcal_events ×3 | INSERT | `evt_c82c0965b68d959ee4241b` (leonard cal), `evt_f5f279f282d20ec86bb8e5` (robert cal), `evt_949ab837443564b6be0edf` (arthur cal) | one shared ical_uid `ede6e91c6f01552379e2f3a694ee537c@hg4`; start/end 2026-02-16T18:00–18:45Z (plan fields); created/updated 2026-02-13T05:45:00Z; `self` flag on each owner's copy | gcal/data.json: all three calendars exist; event ids and ical_uid unused; per-calendar copies sharing an `@hg4` uid is the base pattern; no clashing Feb 16 events on those calendars | OK |
| 111–112 | github.github_pull_requests | INSERT | `harmonygames-Games/GameOfDominoes#1917` | merged by EMPLOYEE_0025 (Arthur Blake); base_ref `Blake/boombitWithEcon`, head_ref `Blake/supportEmail`; base_sha `71a5f99d…`, head_sha `d67e7d02…`, merge `e1f05eab…`; created 2026-02-12T18:05Z, merged/closed 21:10Z | github/data.json: repo exists; 1,906 repo PRs, max #1916 (2025-12-26), so #1917 is unused and next; base_sha = head of base branch `arthur.blake/boombitWithEcon` | OK |
| 113–114 | github.github_branches | INSERT | `harmonygames-Games/GameOfDominoes:arthur.blake/supportEmail` | head_sha `d67e7d02…` | name unused; base maps every PR head_ref `Blake/X` to branch `arthur.blake/X` (checked 8/8), so this mirrors base | OK (see NB-13 note) |
| 115–118 | github.github_commits ×2 | INSERT | `d67e7d0277db893512d589e28ded199e5177b1c6`, `e1f05eabfc9ed3f2579d0f16e9fa281858268bda` | authored 17:40Z (before PR open) / merge 21:10Z; merge committer '' + SVC_0181, committed_date NULL, parent_shas '[]' | shas absent from commits; merge-commit fields match all base merge commits (e.g. #1915/#1916: committer '' / SVC_0181, committed_date NULL); all 12,687 base commits have NULL committed_date and empty parents | OK |
| 119–120 | github.github_pull_request_commits | INSERT | `…#1917#c_0` | commit d67e7d02, position 0 | id pattern matches base (`#999#c_0`); coll. none | OK |
| 121–124 | github.github_timeline_events ×2 | INSERT | `…#1917#ev_1` merged, `…#1917#ev_2` closed | 21:10Z, data commit_id = merge sha | pattern matches base merged/closed pairs; coll. none | OK |
| 126–127 | linear.linear_projects | INSERT (CHANGED, NEW) | `0fa95761-d59b-4ff4-a8a3-15df3210ca6e` "LLC take-over" | description now "One issue per thing the LLC might take from HG **or pay for**. …" (text only); team_ENG, lead `usr_63fffeb4fab5233e` (leonard.hayes), state started, start_date 2026-02-12 (plan field), created 2026-02-12T23:24Z — all unchanged | linear/data.json: 2 base projects, no id/name collision (REUSED); lead and team resolve (REUSED) | OK |
| 128–275 | linear.linear_issues ×37 | INSERT | `ENG-2438` … `ENG-2474` (numbers 2438–2474, identifier = id) | project above, team_ENG, creator Leonard, state_id 'Backlog', priority 0, labels/links/relations/state_history '[]', created 23:25:00–23:37:00Z at 20 s steps, updated_at = own comment time | 2,331 base ENG issues, max number 2437, so 2438–2474 continue with no gap and no collision (id and identifier); 'Backlog' is a base state literal (92 rows) | OK |
| 130–275 | linear.linear_comments ×37 | INSERT (4 CHANGED, NEW) | one per issue: `comment_2bd90ac9…` (ENG-2438) … `comment_39bd0d5e…` (ENG-2474), full ids in SQL | Text CHANGED (NEW) on: line 163 `comment_7a0dea62…` ENG-2446 (Blake) appends "so the LLC doesn't need them"; line 183 `comment_8f925764…` ENG-2451 (Leonard) appends "I'll set CF up on it"; line 187 `comment_17c00e14…` ENG-2452 (Leonard) appends "nothing for the LLC to take or pay"; line 223 `comment_fa730ebd…` ENG-2461 (Leonard) appends "CF was never on it, its support is the contact on its store listing and that moves with the game". Ids, issue_ids, authors and timestamps unchanged; all other 33 comments byte-identical (REUSED) | base comments array is empty, so no collision (REUSED); both authors are team_ENG members (REUSED) | OK |

Linear comment-to-author map (SQL order, unchanged): Leonard authors ENG-2438, 2439, 2440, 2441, 2447, 2448, 2449, 2450, 2451, 2452, 2453, 2454, 2455, 2460, 2461, 2463, 2464, 2465, 2466, 2467, 2468, 2469, 2470, 2471, 2472, 2473, 2474. Blake authors ENG-2442, 2443, 2444, 2445, 2446, 2456, 2457, 2458, 2459, 2462.

## 6. Check A — Records, references and IDs: PASS

- **Changed rows (NEW):** only text columns and one Gmail `size_estimate` changed. No id, actor, issue_id, thread, mailbox, label or parent reference changed (line diff shows identical key/foreign-key literals on all 8 lines).
- **Actors resolve, one account per person (REUSED, unchanged):** Slack EMPLOYEE_0038 = Leonard Hayes, EMPLOYEE_0025 = Arthur Blake, SLACK_BOT_0005 = Jenkins bot. Linear `usr_63fffeb4fab5233e` = leonard.hayes, `usr_cc3e90160f490686` = arthur.blake. Trello `PERSON_6094_TRELLO_USER_ID` = Leonard Hayes. GitHub EMPLOYEE_0025_GITHUB_USERNAME = Arthur Blake. Gmail/GCal/Drive use existing roster emails. No new person accounts (lint identities check clean, NEW).
- **Parents and targets exist (REUSED):** Drive parents are the owners' root folders; Slack authors are channel/DM members; both UPDATE targets exist, had no replies, and are updated to match exactly one injected reply; Trello board/list open; GitHub repo and base branch/sha exist; Linear team, lead and memberships exist; children follow parents in the same transaction.
- **Collisions (REUSED, complete scope):** the record-key set is identical to revision 4 and the base manifest is unchanged, so the complete-scope results stand: none in gdrive `/drive_files`, gdocs, gsheets (398 spreadsheets), gslides (ids and object ids), Slack (687,230 messages in 5,353 files), Trello cards/actions/idShort, Gmail (all 88,726 thread files, 11 thread numbers + 7 Message-IDs), GCal event ids/ical_uid, GitHub PR/branch/commit/PR-commit/timeline ids, Linear project/issue/identifier/comment ids. No duplicate keys in the SQL.
- **ID contracts:** Gmail history_id NULL on all 11 threads (lint, NEW). No Drive content_path used.
- **Readable Drive files (REUSED, rows unchanged):** both Docs have docs_documents rows with non-empty body_text (1,214 and 154 chars); the Sheet has spreadsheet + sheet grid; the Slides deck has presentation/pages/elements.

## 7. Check B — SQL structure and supported schema rules: PASS

- 133 statements; every INSERT single-row with matching column/value counts (lint parse, NEW; no missing_required). The 2 UPDATEs use primary-key predicates.
- No generated columns set (`text_fts` / `body_text_fts` absent).
- Linear text dates all `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DD`; no casts or `now()`; `state_history_json = '[]'` on all 37 issues (lint, NEW; the changed Linear rows keep their date literals).
- JSON: lint json_shape clean on all `*_json` columns. The changed Gmail rows keep their label/recipient/header arrays unchanged.
- Escaping (NEW): the changed literals use doubled quotes correctly (`there''s`, `doesn''t`, `I''ll`, `CF''s`); lint parsed each statement to its expected column count.
- `size_estimate` (NEW): 1490 = decoded body length 590 + 900, the same offset used on every other injected Gmail message.
- Provisional snapshot comparison: MATCH for all 21 affected tables per lint. The snapshot is unverified; not proof of live compatibility.

## 8. Check C — Dates, relationships and consistency: PASS

**Clock (NEW).** No timestamp changed. Latest event is still the App Review mail at 2026-02-13T07:30Z, before 2026-02-14 00:00 UTC. Only the Calendar start/end (2026-02-16) and the project start_date are later or plan-only, and they are plan fields.

**Changed facts checked against base and the rest of the SQL (NEW):**

| Changed record | Check | Result |
|---|---|---|
| Lines 62/66/70 Gmail: BigQuery/Firebase "with CF's tiny volume they cost nothing after that, so there's nothing there for the LLC" | SQL: ENG-2444 (line 155) "CF's go through firebase"; ENG-2449/2452 keep GitHub and GA under HG until the data is out; doc line 17 "Services we keep running just move their billing to the LLC" (a $0 service adds nothing). $100 + $100 + $48 = $248 unchanged. Base Gmail (search "combo fighter", 400-hit limit, positive evidence only): Firebase project "Combo Fighter" was linked to Cloud Billing and moved to the pay-as-you-go Blaze plan on Sat, 27 Dec 2025 (`gmail/threads/blake@harmonygames.co_1852687304846883695.json` /messages/0). Blaze is usage-billed, so a low-volume project costing nothing is compatible; no base record gives a CF Firebase/BigQuery charge ("firebase billing" complete scan of 88,726 thread files: 0 hits; 2026 Slack "firebase"/"bigquery" complete over 134 files: no CF cost) | consistent |
| Line 127 project description "…take from HG or pay for" | Matches the 37 issues, several of which are pay-only items (VO campaign, Kub-card bills) | consistent |
| Line 163 ENG-2446: build boxes are HG's, go in Sunset's sale, jobs move to Blake's machine "so the LLC doesn't need them" | Doc line 17: equipment comes to the LLC only through Sunset's sale; base #executives 02-11 puts "laptops build machines" in the sale (REUSED) | consistent |
| Line 183 ENG-2451 (Leonard): "I'll set CF up on it" (AppsFlyer free tier) | Base Slack "appsflyer" complete (5,353 files, 83 hits): #winddown `C0ADGSZKR3R/2026-02.json` /180 "I think appsflyer will be the way to go"; no record assigns the setup to someone else or says CF is already on AppsFlyer. Free tier 15K installs unchanged (REUSED base match) | consistent |
| Line 187 ENG-2452 (GA): "nothing for the LLC to take or pay" | Consistent with the same comment's "stays under HG until the data is extracted", ENG-2449, and Blake's email (BigQuery/Firebase stay on HG's Google account with GA until the data is out) | consistent |
| Line 223 ENG-2461 (Helpshift): "CF was never on it, its support is the contact on its store listing and that moves with the game" | Issue row (line 221) "Player support desk for DD and ZM". Base #winddown `C0ADGSZKR3R/2026-02.json` /57 (Leonard, 2026-02-11): "We gotta move domino delights and zombie match off Helpshift before Feb 28th". Base DM `D04UGG61DUM/2026-01.json` /76–/84 (2026-01-09): Blake "should i add Helpshift to CF?… maybe too early in design for that. maybe link to support email"; Leonard "I think we can hook up [USERNAME_25728] to CF… just contact us". No later record shows Helpshift added to CF: Slack "helpshift" complete over all 2025 (2,017 files, 358 hits) and 2026 (134 files, 25 hits) month files, filtered for "combo"/"CF"/"fighter": only /76. Doc line 17 says a game brings its listings (via Sunset's sale) and its player support, so "moves with the game" agrees | consistent (see A-8) |

**Unchanged cross-checks (REUSED from prior report §8, rows byte-identical, base unchanged):** chronology commit 17:40Z → PR 18:05Z → merge 21:10Z → Jenkins #218 21:40–21:49:30Z → ENG-2462 01:30Z → App Review rejection 07:30Z; notes Mon Feb 9 → draft sheet Tue Feb 10 → project 23:24Z Feb 12 → Trello card 23:42Z → ground-rules doc 23:46Z → comments 00:24–01:37Z Feb 13 → Blake's billing email 02:35Z → request DM 05:40Z → invite 05:45Z → split email 06:10Z; every reply follows its parent and Gmail internal_date matches each Date header. Base fact matches as recorded previously (Figma to Sep 11, Helpshift off before Feb 28, Singular termination, AppsFlyer 15K free tier, layer.ai/Soundly cancelled on the 11th, Cursor/CodeRabbit on the 12th, Unity, Carta/Chase, keep Deel/Gusto/Intuit/Linear, archive Google accounts after Feb 15, Slack/Google/GA/GitHub kept until data extraction, Blake's Kub-card billing, lifestyle route, IP via Sunset's sale, ZM listings moved July 2025, Calm Play Singular links, build machine at Blake's, App Review mailbox patterns).

**Superseding values are dated later records from named owners, not contradictions (REUSED):** DD prod AWS ~$1k / "maybe $300" (ENG-2441, 00:48Z) → Blake's DM $140 (03:10Z); Metabase + dbt ~$300 (ENG-2447/2448) → Blake's $248 email (02:35Z); Figma "LLC 0" in the draft sheet → ENG-2453 "stays HG's"; ENG-2462 "done" → Apple's later rejection of the email-only support.

**Grader-facing text (NEW for changed rows):** none. The new phrases ("nothing there for the LLC", "so the LLC doesn't need them", "nothing for the LLC to take or pay", "I'll set CF up on it", "CF was never on it") are colleagues writing to each other on the plan's own issues and email. None addresses a solver/grader or describes the test. Lint grader_language: 0 flags.

**Base-data conflicts:** no injected record builds on a listed Snowflake/Confluence conflict. The doc's warehouse daily-revenue reference (unchanged) is not a listed conflict.

## 9. Findings

**Demonstrated defects: none.**

Advisories (non-blocking, no rule broken):

- **A-2 (REUSED), lines 111–118:** after #1917 merges, base branch `arthur.blake/boombitWithEcon` keeps head `71a5f99d…`. Base doesn't move branch heads after merges either. Not a defect.
- **A-3 (REUSED, realism), line 49:** Blake's "$140 a month" DM is threaded under an unrelated Feb 2 message in the Robert–Blake DM. The reference is valid. Optional fix: post it top-level (thread_parent_id NULL) and drop the line-50 UPDATE.
- **A-4 (REUSED, for /prompt), lines 86–94:** the rejection names exactly what #1917 shipped (email-only support), so it reads as a later correction. /prompt should confirm DD's player-support item has one defensible call.
- **A-5 (REUSED, for /prompt), line 267 vs line 17:** "Calm Play could just be our LLC" (01:10Z) comes after the doc's "the new one Blake and I are setting up" (23:46Z). The wording is speculative; /prompt's unique-ground-truth check should test it.
- **A-6 (REUSED, for /prompt), line 151:** no injected record gives a ZM hosting figure. The notes doc's "Servers about $1k a month" is unattributed, and the draft sheet ties ~1000 to DD. /prompt must confirm that Robert can see a source for ZM's current hosting cost, or that the call doesn't depend on the exact figure.
- **A-7 (REUSED, known issue NB-13):** branch/head_ref naming mirrors base, so later stages shouldn't grade an exact branch name.
- **A-8 (NEW, for /prompt), lines 62–70 and 223:** the new wording now states CF's $0 items outright (Firebase/BigQuery after extraction, store-listing support, GA). Base shows two things Robert may or may not see: CF's Firebase project is on the pay-as-you-go Blaze plan (Blake's mailbox), and a Jan 9 DM in which Leonard floated hooking CF up to a support tool. Neither contradicts the SQL. /prompt should confirm the expected answer treats these items as $0 / not taken, and that no base record Robert can see suggests otherwise.

## 10. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | Record keys identical to revision 4, so the complete-scope collision checks (REUSED) stand. The changed rows alter text only. All actors/parents/targets resolve; the history_id contract is met; all Drive files are readable; no second accounts. |
| B — SQL structure and supported schema rules | PASS | Lint is clean on the new hash (133 statements). No generated columns. Linear formats and `state_history_json` are present. The changed size_estimate = body + 900 and the quote escaping is valid. The snapshot comparison is provisional (MATCH). |
| C — Dates, relationships and consistency | PASS | No timestamps changed and no event falls after the clock. The new statements agree with base: #winddown has only DD/ZM moving off Helpshift, the Jan 9 DM leaves CF's support open with no Helpshift setup, the CF Firebase Blaze plan allows a $0 cost, and AppsFlyer was chosen. They also agree with the other SQL rows (ENG-2444/2449/2461 issue text, ground-rules doc). No grader-facing text. |

## 11. Stage provenance / reuse record

- `review_version: injection-static-v2`; `evidence_contract: stage-evidence-v1`.
- `reused_evidence`: prior report `Evals/task_inputs/reports/0_injection.md` sha256 `3d38911e1850f7eecdd438b0eaab41724d4a154746e5fe96e3467c815c61e287`. Reused: §5 ledger rows for the 125 byte-identical statements, §6 collision/reference results, §7 JSON checks for unchanged literals, and §8 chronology and base fact cross-checks. Dependencies verified unchanged this run: universe manifest `5e01ac44…de450`, the Eval 0, WORKFLOW, schema, id_contracts and lint hashes, the clock, and the full record-key set (line diff vs revision 4 shows key literals identical on all 8 changed lines).
- NEW this run: lint on SQL `4236a030…1b76`; all 8 changed statements; size_estimate recomputation; Slack search-many `messages/*/*.json` "appsflyer" (complete, 5,353 files, 83 hits); Slack `messages/*/2025-*.json` "helpshift"/"firebase" (complete, 2,017 files) and `messages/*/2026-*.json` "helpshift"/"firebase"/"bigquery" (complete, 134 files); direct reads of `D04UGG61DUM/2026-01.json` /66–/99, `D04UGG61DUM/2026-02.json` /0–/13 and `C0ADGSZKR3R/2026-02.json` /57–/59; Gmail `threads/*.json` "firebase billing" (complete, 88,726 files, 0 hits), "combo fighter" and "bigquery" (capped at their limits, used only as positive evidence); Gmail read of `blake@harmonygames.co_1852687304846883695.json` /messages/0.
- /prompt may reuse checks A–C for SQL sha256 `4236a030…1b76`. Prompt incorporation, discoverability, Robert's visibility and solvability (including A-4 to A-6 and A-8, and the Snowflake revenue lookup) are /prompt's job.

## 12. Limits

Outside the certified static scope: live execution and deployment, current database compatibility (schema snapshot unverified), search ranking, assigned-persona visibility and task difficulty. Slack "helpshift" scans before 2025 were not filtered (capped broad scan only). This doesn't affect a required check: CF's own Jenkins jobs and Firebase project first appear in Dec 2025, and base #winddown limits the Helpshift move to DD/ZM. No unresolved required static checks.

### FINAL VERDICT: PASS

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (not otherwise reported by the runtime)

Next action: Proceed to /prompt

Evidence limits: None for the required static checks. Static scope only: no live deployment, database-compatibility, visibility or difficulty certification; the schema snapshot comparison is provisional.
