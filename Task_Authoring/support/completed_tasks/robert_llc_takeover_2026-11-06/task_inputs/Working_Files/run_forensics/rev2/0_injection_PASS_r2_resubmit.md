# /injection — Injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`: changed records checked NEW; unchanged records' results REUSED from the prior report (see §11) |
| Mode | Chat/attachment review, static (no SQL executed, no base export modified) |
| Attempt | 6adfee3b47f7621feba5b96c |
| Actual review time | 2026-11-05T11:07:28Z |
| Clock | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal`, archive hg4-2026-08-31 v37; manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Input | `Evals/task_inputs/01_Universe_Inject.sql` (revision 4, saved from attachment `_uploads/01_Universe_Inject (2).sql`), 85,444 bytes, sha256 `edf1fd9036113b77674d7e2f2c51b31920471b110f6c10c0c51ac3fa16d6cee3` |
| Previous SQL version | 85,151 bytes, sha256 `7573eb1a…aed23` (PASS in prior report sha256 `c741b3eee50828395190c3b6dcdb78b82634a7c2b3bad1ec5a699e1853baf72a`) |
| References | Eval 0 `e034019b…6eff`; WORKFLOW.md `ee4cd8e1…fcd5d`; schema snapshot `injection.json` `31dcb2b4…5151` (unverified, provisional); `id_contracts.json` `fc4711ef…4682`; lint `hg_injection_lint.py` `a8226e2a…448b` (injection-lint-v1). All match the prior review. |
| Assignment (context only) | Robert, Co-founder & Creative Director; Executive / Finance / Planning and decision support; long-horizon; easy |

## 2. Input / authority issues

None. The new attachment was saved as the injection input (revision 4) and read in full before base searches. SQL comments (lines 1–4) are evidence of intent only, with no tool-call, pass-rate or grader content.

**Change set vs the previously reviewed SQL:** same 276 lines and 133 statements, and every record key is unchanged (an id-token comparison of the two files shows no additions or removals). 17 statements differ, all in content fields only:

| Lines | Record | Change |
|---|---|---|
| 10, 19 | Drive/Docs `f_a7af6f358dd5648c11a608` | Name/title shortened to "LLC notes (Monday)"; body split into a title line + note paragraph; style runs 0–19 / 19–154 |
| 46 | Slack `6908b2f1…` (Leonard, #prototype) | Appends "so count it in what the LLC costs" |
| 62, 66, 70 | Gmail "billing moved to my card" ×3 copies | Body adds "so count it as mine like the other two" and "then CF's are on the free tier, its volume is tiny"; size 1356 → 1448 |
| 86–94 | Gmail App Review ×3 copies + 2 thread snippets | New rejection reason (email-only support does nothing without a mail account); Arthur's/Leonard's copies get per-mailbox greeting and labels; sizes updated |
| 127 | Linear project | start_date 2026-02-13 → 2026-02-12 |
| 151, 159, 163, 167, 195 | Linear comments ENG-2443/2445/2446/2447/2454 | Wording changes (see ledger) |

## 3. Checklist

- [x] Save/reload SQL; hash, base manifest and review version recorded (NEW)
- [x] `hg_injection_lint.py` run on the new hash: 0 FAIL / 0 CHECK / 0 INFO across 133 statements (NEW)
- [x] Full operation ledger, 131 data statements (129 INSERT, 2 UPDATE) + BEGIN/COMMIT (17 changed rows NEW; others REUSED)
- [x] Check A: references and collisions (changed rows NEW; key collisions REUSED because keys and base are unchanged)
- [x] Check B: structure and schema rules (NEW via lint; changed JSON/style runs re-verified NEW)
- [x] Check C: dates, relationships, consistency (changed facts NEW against base and the other SQL rows; unchanged cross-checks REUSED)
- [x] Coverage, findings, limits and one final verdict

## 4. Lint flags and resolutions

`hg_injection_lint.py` (injection-lint-v1, clock 2026-02-14T00:00:00Z, sha256 of SQL `edf1fd90…6cee3`) ran checks future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape. It loaded base slack/users, trello, gmail/users, github, linear, contacts, confluence. **Flags: none (FAIL 0, CHECK 0, INFO 0).** Nothing to resolve. A clean lint is not a pass, so checks A–C were done below.

## 5. Operation ledger

All statements run in SQL order inside one `BEGIN … COMMIT`. Rows marked CHANGED differ from the previously reviewed SQL (17 statements: lines 10, 19, 46, 62, 66, 70, 86, 88, 90, 92, 94, 127, 151, 159, 163, 167, 195) and were re-checked NEW. All other rows are byte-identical to the previous version; their results are REUSED from the prior report (sha256 `c741b3ee…f72a`, §5) under stage-evidence-v1, with the base manifest, references and record keys verified unchanged. There are no deletes or upserts. "Coll." = collision check result against the complete base collection plus the other SQL rows.

| SQL lines | Service.table | Op | Record id(s) | Key values / relationships | Base check (path / pointer) | Result |
|---|---|---|---|---|---|---|
| 7–8 | gdrive.drive_files | INSERT | `f_1e468a9d69ea0f0a2001f5` | Google Doc "LLC ground rules…", owner leonard.hayes, parent `d_63fffeb4fab5233ed5bb73`, shared writer robert + arthur.blake, created/modified 2026-02-12T23:46Z | gdrive/data.json `/drive_files` (53,866 rows): parent = Leonard's root folder (owner leonard.hayes); id coll. none | OK |
| 9–10 | gdrive.drive_files | INSERT | `f_a7af6f358dd5648c11a608` | **CHANGED (NEW):** name now "LLC notes (Monday)" (= docs title at line 19), Leonard root, 2026-02-09T23:55Z | same; id unchanged, so REUSED collision result | OK |
| 11–12 | gdrive.drive_files | INSERT | `f_d996e4c434ce160dc52596` | Spreadsheet "LLC 90 days (draft)", Leonard root, 2026-02-10T18:30Z | same | OK |
| 13–14 | gdrive.drive_files | INSERT | `f_7d2c9e7822e87b92a11759` | Presentation "Combo Fighter: next 90 days", owner robert, parent `d_9f7ba94f7526d54d8482ba`, 2026-02-08T03:00Z | parent = Robert's root folder; coll. none | OK |
| 16–17 | gdocs.docs_documents | INSERT | `f_1e468a9d69ea0f0a2001f5` | body_text non-empty (1,214 chars); style runs TITLE 0–59, NORMAL 59–1214 = exact body length | gdocs/data.json `/docs_documents`: coll. none (document_id and drive_file_id) | OK |
| 18–19 | gdocs.docs_documents | INSERT | `f_a7af6f358dd5648c11a608` | **CHANGED (NEW):** title "LLC notes (Monday)"; body_text = title line (19 chars incl. \n) + one note paragraph, 154 chars total; runs TITLE 0–19, NORMAL_TEXT 19–154 = exact body length, no zero-length run | coll. none (REUSED, id unchanged) | OK (old A-1 resolved) |
| 21–22 | gsheets.sheets_spreadsheets | INSERT | `f_d996e4c434ce160dc52596` | drive_file_id = same id, owner Leonard | gsheets/data.json `/sheets_spreadsheets` complete lookup (398 records) on spreadsheet_id and drive_file_id: 0 matches | OK |
| 23–24 | gsheets.sheets_sheets | INSERT | (`f_d996…`, sheet 0) | grid 5 rows × 8 cols; header Item/Game/Decision/Monthly cost/Paid by/Next step/Owner/By | parent spreadsheet created at line 22 | OK |
| 26–27 | gslides.slides_presentations | INSERT | `f_7d2c9e7822e87b92a11759` | owner robert, revision `5493af5cba` | gslides/data.json `/slides_presentations`: coll. none | OK |
| 28–39 | gslides.slides_pages ×3 / slides_page_elements ×3 | INSERT | pages `slide_886d78971206`, `slide_05405983565d`, `slide_34827ed9cf24`; elements `el_7e281c2d6d42`, `el_4f79d571a8ab`, `el_c30917bbd73c` | BLANK layout, TEXT_BOX 9144000×5143500 at ordinal 0, indexes 0–2 | object ids absent from the whole gslides export; layout/kind/size match base pages | OK |
| 41–42 | slack.slack_messages | INSERT | `9ed17488702e4bf387cc012f7bb0a509` | #builds `C05433XK267`, SLACK_BOT_0005 Jenkins attachment "DD iOS Submission - #218 Started by user Arthur Blake", ts 1770932400.314774 = created_at 2026-02-12T21:40:00Z | channels.json: bot 0005 is a member; base DD iOS Submission builds end at #217 (ts 1769620132); ts coll. none | OK |
| 43–44 | slack.slack_messages | INSERT | `85bc96b0aa43bb455a58da9d8b63c060` | #builds, "#218 - Blake/boombitWithEcon Success after 9 min 12 sec … Replace Helpshift with support email. [Arthur Blake]", 21:49:30Z (= 21:40:00 start + 9m12s + post lag) | branch label matches base #216 build branch `Blake/boombitWithEcon` | OK |
| 45–46 | slack.slack_messages | INSERT | `6908b2f17c379e809aafa6b2b169f4bf` | **CHANGED text (NEW):** appends "so count it in what the LLC costs"; #prototype `C09UHHN6PFZ`, Leonard (EMPLOYEE_0038), reply in thread `73ec270a…` (ts 1770404397.819789), 2026-02-12T23:20Z | Leonard is a member; parent = messages/C09UHHN6PFZ/2026-02.json `/389` "VO campaign is created…", by Leonard, reply_count 0 and no existing replies | OK |
| 47 | slack.slack_messages | UPDATE | `73ec270a3d07eb8d8488384898be079e` | thread_ts_legacy = own ts, reply_count 1, reply_users_count 1, latest_reply = 1770938400.370665 | before: reply_count 0, latest_reply null, no replies in any month file; after matches the one injected reply; parent-with-replies shape (thread_ts = own ts) matches base | OK |
| 48–49 | slack.slack_messages | INSERT | `ad623a2f0d4387109d108e767b174609` | DM `D04V95AAAHW` (Robert–Blake), Blake (EMPLOYEE_0025), reply in thread `bc4bc3d0…` (ts 1770056235.480619), 2026-02-13T03:10Z, "Domino's prod account is down to $140 a month…" | DM members include EMPLOYEE_0016 (Robert) and EMPLOYEE_0025 (Blake); parent at messages/D04V95AAAHW/2026-02.json `/4`, by Blake, reply_count 0, no replies | OK (advisory A-3) |
| 50 | slack.slack_messages | UPDATE | `bc4bc3d0e2a0ea6ae92cb2a9712e8f76` | reply_count 1, latest_reply 1770952200.665739 | before 0 / null; after consistent | OK |
| 51–52 | slack.slack_messages | INSERT | `6257a3c4456db0bd2aeb872619d7a364` | DM `D04UP2L3E3S` (Robert–Leonard), Leonard, top-level, 2026-02-13T05:40Z (request message) | DM members include EMPLOYEE_0016 and EMPLOYEE_0038; ts coll. none | OK |
| 54–55 | trello.trello_cards | INSERT | `698e6548aa9516b76c4ab475` | board `640643a3fd8f3ca308d9318e` "Harmony Games", list `640643a3fd8f3ca308d93195` "To Do", idShort 456, shortLink NULL, url `…/c/N6TBAK8A/456-llc-what-we-take-from-hg`, dateLastActivity 2026-02-12T23:42Z | trello/data.json: board/list exist and are open; 449 board cards, max idShort 455, so 456 is next and unused; all 449 base cards have shortLink NULL and the same url pattern; card id hex prefix 698e6548 = 2026-02-12T23:42:00Z | OK |
| 56–57 | trello.trello_actions | INSERT | `698e65489a4031a95d3ce53e` | createCard by `PERSON_6094_TRELLO_USER_ID` (Leonard Hayes), same date | member resolves to Leonard; data_json shape matches base createCard actions; coll. none | OK |
| 59–70 | gmail.gmail_threads ×3 / gmail_messages ×3 | INSERT (messages CHANGED, NEW) | threads `arthur.blake@…/1856975772057961391`, `robert@…/1856975772058401508`, `leonard.hayes@…/1856975772058497766`; message `<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>` per mailbox | Blake → Robert + Leonard "billing moved to my card", 2026-02-13T02:35Z (internal_date 1770950100000 matches); SENT for the sender, INBOX for the recipients. Body adds "so count it as mine like the other two" and "then CF's are on the free tier, its volume is tiny"; size_estimate 1448 = body 548 + 900 (same offset as every other injected message); snippet = first 140 chars, unchanged | all 88,726 thread files streamed for every new thread number and Message-ID: 0 hits; history_id NULL (contract OK) | OK |
| 71–82 | gmail threads ×3 / messages ×3 | INSERT | threads `…/1856989298688254292` (leonard), `…/1856989298688559716` (robert), `…/1856989298688898804` (arthur); msg `<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com>` | Leonard → Robert, cc Blake "LLC money", 2026-02-13T06:10Z (1770963000000 matches) | 0 hits | OK |
| 83–94 | gmail threads ×3 / messages ×3 | INSERT (CHANGED, NEW) | `robert@…/1856994331853686118` + `<136285951.151027292.1770967800000@email.apple.com>`; `arthur.blake@…/1856994331852829558` + `<375944835…457@email.apple.com>`; `leonard.hayes@…/1856994331852922225` + `<883960163…220@email.apple.com>` | App Review (SVC_4131) "We noticed an issue with your submission." for Domino Delights, Guideline 1.5: support option "only opens an email draft… does nothing" without a mail account; asks for a support URL. 2026-02-13T07:30Z. Per mailbox: Robert "Hello [PERSON_NAME_0054]", INBOX/CATEGORY_UPDATES/Label_ad4e31dc09/Label_aeb79a643f, size 1924; Arthur "Hello Arthur", INBOX/CATEGORY_UPDATES/UNREAD, size 1912; Leonard "Hello Leonard", ARCHIVED/CATEGORY_UPDATES/Label_6e8d84b057, size 1913 (each = body + 900); thread snippets (lines 88, 92) = message snippets | all 49 base App Review mails (complete subject scan, 88,728 files): Robert's use [PERSON_NAME_0054] + Label_ad4e31dc09/Label_aeb79a643f; Arthur's 8 use "Hello Arthur" + INBOX/CATEGORY_UPDATES/UNREAD; Leonard's use "Hello Leonard" + ARCHIVED/CATEGORY_UPDATES/Label_6e8d84b057. Injected copies match each mailbox's base pattern. All labels exist in labels.json (`ARCHIVED`, `UNREAD` system; `Label_6e8d84b057` "App Center / Test Flight"). 0 id hits (REUSED, ids unchanged) | OK (advisory A-4) |
| 95–102 | gmail threads ×2 / messages ×2 | INSERT | `robert@…/1856987728970293624` + `<calendar-0b12e6f6-…@google.com>`; `arthur.blake@…/1856987728969768237` + `<calendar-cbc32ea4-…@google.com>` | Invitations "LLC: decide" Mon Feb 16 10:00–10:45 PT / 1:00–1:45 ET (= 18:00–18:45Z), sent 2026-02-13T05:45:03Z | Robert's subject token `([PERSON_NAME_0055])` matches 99 base invite subjects in Robert's mailbox; 0 id hits | OK |
| 104–109 | gcal.gcal_events ×3 | INSERT | `evt_c82c0965b68d959ee4241b` (leonard cal), `evt_f5f279f282d20ec86bb8e5` (robert cal), `evt_949ab837443564b6be0edf` (arthur cal) | one shared ical_uid `ede6e91c6f01552379e2f3a694ee537c@hg4`; start/end 2026-02-16T18:00–18:45Z (plan fields); created/updated 2026-02-13T05:45:00Z; `self` flag on each owner's copy | gcal/data.json: all three calendars exist; event ids and ical_uid unused; per-calendar copies sharing an `@hg4` uid is the base pattern; no clashing Feb 16 events on those calendars | OK |
| 111–112 | github.github_pull_requests | INSERT | `harmonygames-Games/GameOfDominoes#1917` | merged by EMPLOYEE_0025 (Arthur Blake); base_ref `Blake/boombitWithEcon`, head_ref `Blake/supportEmail`; base_sha `71a5f99d…`, head_sha `d67e7d02…`, merge `e1f05eab…`; created 2026-02-12T18:05Z, merged/closed 21:10Z | github/data.json: repo exists; 1,906 repo PRs, max #1916 (2025-12-26), so #1917 is unused and next; base_sha = head of base branch `arthur.blake/boombitWithEcon` | OK |
| 113–114 | github.github_branches | INSERT | `harmonygames-Games/GameOfDominoes:arthur.blake/supportEmail` | head_sha `d67e7d02…` | name unused; base maps every PR head_ref `Blake/X` to branch `arthur.blake/X` (checked 8/8), so this mirrors base | OK (see NB-13 note) |
| 115–118 | github.github_commits ×2 | INSERT | `d67e7d0277db893512d589e28ded199e5177b1c6`, `e1f05eabfc9ed3f2579d0f16e9fa281858268bda` | authored 17:40Z (before PR open) / merge 21:10Z; merge committer '' + SVC_0181, committed_date NULL, parent_shas '[]' | shas absent from commits; merge-commit fields match all base merge commits (e.g. #1915/#1916: committer '' / SVC_0181, committed_date NULL); all 12,687 base commits have NULL committed_date and empty parents | OK |
| 119–120 | github.github_pull_request_commits | INSERT | `…#1917#c_0` | commit d67e7d02, position 0 | id pattern matches base (`#999#c_0`); coll. none | OK |
| 121–124 | github.github_timeline_events ×2 | INSERT | `…#1917#ev_1` merged, `…#1917#ev_2` closed | 21:10Z, data commit_id = merge sha | pattern matches base merged/closed pairs; coll. none | OK |
| 126–127 | linear.linear_projects | INSERT | `0fa95761-d59b-4ff4-a8a3-15df3210ca6e` "LLC take-over" | team_ENG, lead `usr_63fffeb4fab5233e` (leonard.hayes), state started, **start_date 2026-02-12 (CHANGED, NEW)**, created 2026-02-12T23:24Z; start_date is a plan field in `YYYY-MM-DD` form | linear/data.json: 2 base projects, no id/name collision; lead resolves; team exists | OK |
| 128–275 | linear.linear_issues ×37 | INSERT | `ENG-2438` … `ENG-2474` (numbers 2438–2474, identifier = id) | project above, team_ENG, creator Leonard, state_id 'Backlog', priority 0, labels/links/relations/state_history '[]', created 23:25:00–23:37:00Z at 20 s steps, updated_at = own comment time | 2,331 base ENG issues, max number 2437, so 2438–2474 continue with no gap and no collision (id and identifier); 'Backlog' is a base state literal (92 rows) | OK |
| 130–275 | linear.linear_comments ×37 | INSERT | one per issue: `comment_2bd90ac9…` (ENG-2438) … `comment_39bd0d5e…` (ENG-2474), full ids in SQL | authors `usr_63fffeb4fab5233e` (Leonard) or `usr_cc3e90160f490686` (arthur.blake); times 2026-02-13T00:24–01:37Z, all after their issue's created_at. Text CHANGED (NEW) on ENG-2443 (no cost figure now; "bills every month on HG's AWS bill"), ENG-2445 (drops "nakama"), ENG-2446 ("build boxes at my place", "our jenkins jobs"), ENG-2447 ("more or less"), ENG-2454 ("character source art"); ids, authors and times unchanged | base comments array is empty, so no collision; both authors are team_ENG members (tmem_team_ENG_*) | OK |

Linear comment-to-author map (SQL order): Leonard authors ENG-2438, 2439, 2440, 2441, 2447, 2448, 2449, 2450, 2451, 2452, 2453, 2454, 2455, 2460, 2461, 2463, 2464, 2465, 2466, 2467, 2468, 2469, 2470, 2471, 2472, 2473, 2474. Blake authors ENG-2442, 2443, 2444, 2445, 2446, 2456, 2457, 2458, 2459, 2462.

## 6. Check A — Records, references and IDs: PASS

- **Changed rows (NEW):** no actor, parent, channel, thread, issue or mailbox reference changed. The new Gmail labels resolve in `gmail/labels.json`: `ARCHIVED` and `UNREAD` (system), `Label_6e8d84b057` "App Center / Test Flight" (user). Robert's copy keeps `Label_ad4e31dc09` / `Label_aeb79a643f`, which exist. The Drive name and Docs title of `f_a7af6f358dd5648c11a608` agree. The thread rows at lines 88/92 keep their ids and user_email; only the snippet changed, and it equals the message snippet.
- **Actors resolve, one account per person (REUSED, rows unchanged):** Slack EMPLOYEE_0038 = Leonard Hayes, EMPLOYEE_0025 = Arthur Blake, SLACK_BOT_0005 = Jenkins bot. Linear `usr_63fffeb4fab5233e` = leonard.hayes, `usr_cc3e90160f490686` = arthur.blake. Trello `PERSON_6094_TRELLO_USER_ID` = Leonard Hayes. GitHub EMPLOYEE_0025_GITHUB_USERNAME = Arthur Blake. Gmail/GCal/Drive use existing roster emails. No new person accounts.
- **Parents and targets exist (REUSED):** Drive parents are the owners' root folders; Slack authors are members of their channels/DMs; both UPDATE targets exist, had no replies before, and are updated to match exactly one injected reply; Trello board/list open; GitHub repo and base branch/sha exist; Linear team, lead and memberships exist; children follow parents in the same transaction.
- **Collisions (REUSED, complete scope):** the set of record keys is identical to the previously reviewed SQL and the base manifest is unchanged, so the prior complete-scope results stand: none in gdrive `/drive_files`, gdocs, gsheets (398 spreadsheets), gslides (ids and object ids), Slack (687,230 messages in 5,353 files), Trello cards/actions/idShort, Gmail (all 88,726 thread files, 11 thread numbers + 7 Message-IDs), GCal event ids/ical_uid, GitHub PR/branch/commit/PR-commit/timeline ids, Linear project/issue/identifier/comment ids. No duplicate keys in the SQL.
- **ID contracts:** Gmail history_id NULL on all 11 threads (lint, NEW). No Drive content_path used.
- **Readable Drive files (NEW for the changed doc):** `f_a7af…` has a docs_documents row with non-empty body_text (154 chars); `f_1e468a…` (1,214 chars), the Sheet (spreadsheet + sheet grid) and the Slides deck (presentation/pages/elements) are unchanged.

## 7. Check B — SQL structure and supported schema rules: PASS

- 133 statements; every INSERT single-row with matching column/value counts (lint parse, NEW; no missing_required). The 2 UPDATEs use primary-key predicates.
- No generated columns set (`text_fts` / `body_text_fts` absent).
- Linear text dates all `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DD` (including the changed `start_date '2026-02-12'`); no casts or `now()`; `state_history_json = '[]'` on all 37 issues.
- JSON: lint json_shape clean on all `*_json` columns; changed literals re-parsed NEW: the line-19 style_runs array (2 runs, contiguous 0–19–154), the label arrays on lines 90/94, and the unchanged header arrays.
- Provisional snapshot comparison: MATCH for all 21 affected tables per lint. The snapshot is unverified; not proof of live compatibility.

## 8. Check C — Dates, relationships and consistency: PASS

**Clock (NEW).** No event timestamp changed. Latest event is still the App Review mail at 2026-02-13T07:30Z, before 2026-02-14 00:00 UTC. Only the Calendar start/end (2026-02-16) are later, and they are plan fields. The changed Linear `start_date` (2026-02-12) is a plan field on the project's creation day (created 2026-02-12T23:24Z = 15:24 PT Feb 12).

**Changed facts checked against base and the rest of the SQL (NEW):**

| Changed record | Check | Result |
|---|---|---|
| Line 46: VO campaign "count it in what the LLC costs" | Agrees with the ground-rules doc (line 17: "Services we keep running just move their billing to the LLC") and Leonard's split email (line 74: "including what one of us already pays for it"); slide 2 still says $100/day (~$3k a month) | consistent |
| Lines 62–70: GitHub "count it as mine like the other two"; BigQuery/Firebase "then CF's are on the free tier" | $100 + $100 + $48 = $248 unchanged; ENG-2444 says CF events go through Firebase; ENG-2449/2452 keep GitHub and GA under HG until the data is out. size_estimate = body + 900 on all three copies, as on every injected message | consistent |
| Lines 86–94: rejection now says the email-only support option does nothing without a mail account | Directly follows from #1917 / Jenkins #218 "Replace Helpshift with support email" (Feb 12 21:10–21:49Z) and ENG-2462 "support goes to the email address now" (01:30Z Feb 13); rejection is later (07:30Z Feb 13). Per-mailbox greetings and labels match all 49 base App Review mails (complete subject scan) | consistent, a dated later correction |
| Lines 10/19: notes doc text unchanged in substance; title split out | Body still says "Servers about $1k a month, Blake is looking at it"; matches the draft sheet's "DD servers ~1000 (Blake: maybe 300)" and ENG-2441 | consistent |
| Line 151 ENG-2443: ZM account "bills every month on HG's AWS bill" (cost figure removed) | No other injected record states a ZM hosting figure, so nothing contradicts it | consistent (see A-6) |
| Line 159 ENG-2445: CF's account "its auth and backend stacks" (nakama dropped) | ENG-2443 places a nakama on ZM's account; base Nakama references are DD backend (game-of-dominoes-backend PRs #51/#55/#57/#78) and a 2025-07 DM about backend + Nakama on one Aurora DB; nothing in base or SQL says CF runs its own Nakama | consistent |
| Line 163 ENG-2446: "the build boxes at my place are HG's… move our jenkins jobs" (Blake) | Base: Blake on the build machine's location, "8 feet behind me" (slack C05433XK267/2023-09.json /271); Jenkins served from `blake.tplinkdns.com:9009` (C05433XK267/2025-11.json /930); #executives 02-11 puts "laptops build machines" in Sunset's sale | consistent |
| Line 167 ENG-2447: "about $300 a month with dbt, more or less" | Stale estimate later superseded by Blake's $248 email (02:35Z vs 00:52Z), as before | consistent (stale-vs-later) |
| Line 195 ENG-2454: "CF's character source art" | layer.ai cancelled on the 11th matches base #winddown 02-11 19:23 Leonard | consistent |

**Unchanged cross-checks (REUSED from prior report §8, rows byte-identical, base unchanged):** chronology commit 17:40Z → PR 18:05Z → merge 21:10Z → Jenkins #218 21:40–21:49:30Z → ENG-2462 01:30Z; notes Mon Feb 9 → draft sheet Tue Feb 10 → project 23:24Z Feb 12 → Trello card 23:42Z → ground-rules doc 23:46Z → comments 00:24–01:37Z Feb 13 → request DM 05:40Z → invite 05:45Z → split email 06:10Z; every reply follows its parent and Gmail internal_date matches each Date header. Base fact matches: Figma to Sep 11, Helpshift off before Feb 28, Singular termination/deferred payment, AppsFlyer 15K free tier, layer.ai/Soundly cancelled on the 11th, Cursor/CodeRabbit on the 12th, Unity note, Carta/Chase, keep Deel/Gusto/Intuit/Linear, archive Google accounts after Feb 15, Slack/Google/GA/GitHub kept until data extraction, Blake's Kub-card billing (#winddown 02-12 23:00), lifestyle route (#executives 02-04), IP via Sunset's sale (#executives 02-11), ZM listings moved in July 2025 (Play Console mail), Calm Play Singular links (#prototype 02-11), Jenkins #218 branch.

**Superseding values are dated later records from named owners, not contradictions:** DD prod AWS ~$1k / "maybe $300" (ENG-2441, 00:48Z) → Blake's DM $140 (03:10Z); Metabase + dbt ~$300 (ENG-2447/2448) → Blake's $248 email (02:35Z); Figma "LLC 0" in the draft sheet → ENG-2453 "stays HG's"; ENG-2462 "done" → Apple's later rejection of the email-only support.

**Grader-facing text:** none. The new phrases ("count it in what the LLC costs", "count it as mine like the other two") are colleagues addressing each other in-thread about the plan, not text addressed to a solver or grader.

**Base-data conflicts:** no injected record builds on a listed Snowflake/Confluence conflict. The doc's warehouse daily revenue reference is not a listed conflict.

## 9. Findings

**Demonstrated defects: none.**

Advisories (non-blocking, no rule broken):

- **A-1 resolved:** the zero-length style run in the notes doc is gone (runs now 0–19 TITLE, 19–154 NORMAL_TEXT).
- **A-2 (REUSED) — lines 111–118:** after merging #1917, base branch `arthur.blake/boombitWithEcon` keeps head `71a5f99d…`; the base doesn't move branch heads after merges either. Not a defect.
- **A-3 (REUSED, realism) — line 49:** Blake's "$140 a month" DM is threaded under an unrelated Feb 2 message in the Robert–Blake DM. Valid reference; optional to post top-level (thread_parent_id NULL and drop the line-50 UPDATE).
- **A-4 (updated, for /prompt) — lines 86–94:** the rejection now names exactly what #1917 shipped (email-only support), so the later-correction reading is clearer than before. /prompt should still confirm that DD's player-support item has one defensible call.
- **A-5 (REUSED, for /prompt) — line 267 vs line 17:** "Calm Play could just be our LLC" (01:10Z) after the doc's "the new one Blake and I are setting up" (23:46Z). Speculative wording; /prompt's unique-ground-truth check should test it.
- **A-6 (updated, for /prompt) — line 151:** ENG-2443 no longer gives a ZM hosting figure, and no other injected record does; the notes doc's "Servers about $1k a month" is unattributed and the draft sheet ties ~1000 to DD. The doc's revenue test for ZM needs ZM's current hosting cost, so /prompt must confirm a source for it that Robert can see (or that the call doesn't depend on the exact figure).
- **A-7 (REUSED, known issue NB-13):** branch/head_ref naming mirrors base, so later stages shouldn't grade an exact branch name.

## 10. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | Record keys identical to the prior version, so complete-scope collision checks (REUSED) stand; new Gmail labels exist; all actors/parents/targets resolve; history_id contract met; all Drive files readable; no second accounts. |
| B — SQL structure and supported schema rules | PASS | Lint clean on the new hash (133 statements); no generated columns; Linear formats and `state_history_json` present; changed JSON/style runs valid. Snapshot comparison provisional (MATCH). |
| C — Dates, relationships and consistency | PASS | No event after the clock; changed facts agree with base (build machines at Blake's, App Review mailbox patterns, layer.ai) and the other SQL rows; superseding values are dated later records; no grader-facing text. |

## 11. Stage provenance / reuse record

- `review_version: injection-static-v2`; `evidence_contract: stage-evidence-v1`.
- `reused_evidence`: prior report `Evals/task_inputs/reports/0_injection.md` sha256 `c741b3eee50828395190c3b6dcdb78b82634a7c2b3bad1ec5a699e1853baf72a` — §5 ledger rows for the 116 byte-identical statements, §6 collision/reference results, §7 JSON checks for unchanged literals, §8 chronology and base fact cross-checks. Dependencies verified unchanged: universe manifest `5e01ac44…de450`, Eval 0, WORKFLOW, schema, id_contracts and lint hashes, clock, and the full record-key set of the SQL.
- NEW this run: lint on SQL `edf1fd90…6cee3`; all 17 changed statements; gmail labels.json; complete gmail subject scan for App Review mail (88,728 files, scan_complete, 49 matches); slack search-many over `messages/*/202*.json` (build box / mac mini / aurora complete; "build machine" and "nakama" capped at their limits, used only as positive evidence) and direct reads of C05433XK267/2023-09.json /268–275 and C04UTBZL6AX/2023-11.json /959–962.
- /prompt may reuse checks A–C for SQL sha256 `edf1fd90…6cee3`. Prompt incorporation, discoverability, Robert's visibility and solvability (including A-4 to A-6 and the Snowflake revenue lookup) are /prompt's job.

## 12. Limits

Outside the certified static scope: live execution and deployment, current database compatibility (schema snapshot unverified), search ranking, assigned-persona visibility and task difficulty. No unresolved required static checks.

### FINAL VERDICT: PASS

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (not otherwise reported by the runtime)

Next action: Proceed to /prompt

Evidence limits: None for the required static checks. Static scope only: no live deployment, database-compatibility, visibility or difficulty certification; the schema snapshot comparison is provisional.
