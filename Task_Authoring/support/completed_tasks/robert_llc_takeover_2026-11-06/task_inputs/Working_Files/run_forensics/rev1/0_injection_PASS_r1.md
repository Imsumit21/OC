# /injection — Injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1` (nothing reused; all checks NEW) |
| Mode | Chat/attachment review, static (no SQL executed, no base export modified) |
| Attempt | 6adfee3b47f7621feba5b96c |
| Actual review time | 2026-11-05T09:27:08Z |
| Clock | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal`, archive hg4-2026-08-31-v37; manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Input | `Evals/task_inputs/01_Universe_Inject.sql` (saved from attachment `_uploads/01_Universe_Inject.sql`), 85,151 bytes, sha256 `7573eb1a6bca35e3fa5827e43eac1021821179d586b92c529852525b998a99d0` |
| References | Eval 0 sha256 `e034019b…6eff`; WORKFLOW.md `ee4cd8e1…fcd5d`; schema snapshot `injection.json` `31dcb2b4…5151` (unverified, provisional); `id_contracts.json` `fc4711ef…4682`; lint `hg_injection_lint.py` `a8226e2a…448b` (injection-lint-v1) |
| Assignment (context only) | Robert, Co-founder & Creative Director; Executive / Finance / Planning and decision support; long-horizon; easy |

## 2. Input / authority issues

None. SQL saved and read in full before base searches. SQL comments (lines 1–4) treated as evidence of intent only: they describe services/statement counts and re-application, with no tool-call, pass-rate or grader content.

## 3. Checklist

- [x] Save/reload SQL; hash, base manifest and review version recorded (NEW)
- [x] `hg_injection_lint.py` run: 0 FAIL / 0 CHECK / 0 INFO across 133 statements (NEW)
- [x] Full operation ledger, 131 data statements (129 INSERT, 2 UPDATE) + BEGIN/COMMIT (NEW)
- [x] Check A: references and collisions (NEW)
- [x] Check B: structure and schema rules (NEW)
- [x] Check C: dates, relationships, consistency (NEW)
- [x] Coverage, findings, limits and one final verdict

## 4. Lint flags and resolutions

`hg_injection_lint.py` (injection-lint-v1, clock 2026-02-14T00:00:00Z) ran checks future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape. It loaded base slack/users, trello, gmail/users, github, linear, contacts, confluence. **Flags: none (FAIL 0, CHECK 0, INFO 0).** Nothing to resolve. A clean lint is not a pass, so checks A–C were done in full below.

## 5. Operation ledger

All statements run in SQL order inside one `BEGIN … COMMIT`. There are no deletes or upserts. "Coll." = collision check result against the complete base collection plus the other SQL rows.

| SQL lines | Service.table | Op | Record id(s) | Key values / relationships | Base check (path / pointer) | Result |
|---|---|---|---|---|---|---|
| 7–8 | gdrive.drive_files | INSERT | `f_1e468a9d69ea0f0a2001f5` | Google Doc "LLC ground rules…", owner leonard.hayes, parent `d_63fffeb4fab5233ed5bb73`, shared writer robert + arthur.blake, created/modified 2026-02-12T23:46Z | gdrive/data.json `/drive_files` (53,866 rows): parent = Leonard's root folder (owner leonard.hayes); id coll. none | OK |
| 9–10 | gdrive.drive_files | INSERT | `f_a7af6f358dd5648c11a608` | Google Doc "LLC notes (Monday)…", Leonard root, 2026-02-09T23:55Z | same | OK |
| 11–12 | gdrive.drive_files | INSERT | `f_d996e4c434ce160dc52596` | Spreadsheet "LLC 90 days (draft)", Leonard root, 2026-02-10T18:30Z | same | OK |
| 13–14 | gdrive.drive_files | INSERT | `f_7d2c9e7822e87b92a11759` | Presentation "Combo Fighter: next 90 days", owner robert, parent `d_9f7ba94f7526d54d8482ba`, 2026-02-08T03:00Z | parent = Robert's root folder; coll. none | OK |
| 16–17 | gdocs.docs_documents | INSERT | `f_1e468a9d69ea0f0a2001f5` | body_text non-empty (1,214 chars); style runs TITLE 0–59, NORMAL 59–1214 = exact body length | gdocs/data.json `/docs_documents`: coll. none (document_id and drive_file_id) | OK |
| 18–19 | gdocs.docs_documents | INSERT | `f_a7af6f358dd5648c11a608` | body_text = title + "\n" (155 chars); runs TITLE 0–155, NORMAL 155–155 (zero-length) | coll. none | OK (advisory A-1) |
| 21–22 | gsheets.sheets_spreadsheets | INSERT | `f_d996e4c434ce160dc52596` | drive_file_id = same id, owner Leonard | gsheets/data.json `/sheets_spreadsheets` complete lookup (398 records) on spreadsheet_id and drive_file_id: 0 matches | OK |
| 23–24 | gsheets.sheets_sheets | INSERT | (`f_d996…`, sheet 0) | grid 5 rows × 8 cols; header Item/Game/Decision/Monthly cost/Paid by/Next step/Owner/By | parent spreadsheet created at line 22 | OK |
| 26–27 | gslides.slides_presentations | INSERT | `f_7d2c9e7822e87b92a11759` | owner robert, revision `5493af5cba` | gslides/data.json `/slides_presentations`: coll. none | OK |
| 28–39 | gslides.slides_pages ×3 / slides_page_elements ×3 | INSERT | pages `slide_886d78971206`, `slide_05405983565d`, `slide_34827ed9cf24`; elements `el_7e281c2d6d42`, `el_4f79d571a8ab`, `el_c30917bbd73c` | BLANK layout, TEXT_BOX 9144000×5143500 at ordinal 0, indexes 0–2 | object ids absent from the whole gslides export; layout/kind/size match base pages | OK |
| 41–42 | slack.slack_messages | INSERT | `9ed17488702e4bf387cc012f7bb0a509` | #builds `C05433XK267`, SLACK_BOT_0005 Jenkins attachment "DD iOS Submission - #218 Started by user Arthur Blake", ts 1770932400.314774 = created_at 2026-02-12T21:40:00Z | channels.json: bot 0005 is a member; base DD iOS Submission builds end at #217 (ts 1769620132); ts coll. none | OK |
| 43–44 | slack.slack_messages | INSERT | `85bc96b0aa43bb455a58da9d8b63c060` | #builds, "#218 - Blake/boombitWithEcon Success after 9 min 12 sec … Replace Helpshift with support email. [Arthur Blake]", 21:49:30Z (= 21:40:00 start + 9m12s + post lag) | branch label matches base #216 build branch `Blake/boombitWithEcon` | OK |
| 45–46 | slack.slack_messages | INSERT | `6908b2f17c379e809aafa6b2b169f4bf` | #prototype `C09UHHN6PFZ`, Leonard (EMPLOYEE_0038), reply in thread `73ec270a…` (ts 1770404397.819789), 2026-02-12T23:20Z | Leonard is a member; parent = messages/C09UHHN6PFZ/2026-02.json `/389` "VO campaign is created…", by Leonard, reply_count 0 and no existing replies | OK |
| 47 | slack.slack_messages | UPDATE | `73ec270a3d07eb8d8488384898be079e` | thread_ts_legacy = own ts, reply_count 1, reply_users_count 1, latest_reply = 1770938400.370665 | before: reply_count 0, latest_reply null, no replies in any month file; after matches the one injected reply; parent-with-replies shape (thread_ts = own ts) matches base | OK |
| 48–49 | slack.slack_messages | INSERT | `ad623a2f0d4387109d108e767b174609` | DM `D04V95AAAHW` (Robert–Blake), Blake (EMPLOYEE_0025), reply in thread `bc4bc3d0…` (ts 1770056235.480619), 2026-02-13T03:10Z, "Domino's prod account is down to $140 a month…" | DM members include EMPLOYEE_0016 (Robert) and EMPLOYEE_0025 (Blake); parent at messages/D04V95AAAHW/2026-02.json `/4`, by Blake, reply_count 0, no replies | OK (advisory A-3) |
| 50 | slack.slack_messages | UPDATE | `bc4bc3d0e2a0ea6ae92cb2a9712e8f76` | reply_count 1, latest_reply 1770952200.665739 | before 0 / null; after consistent | OK |
| 51–52 | slack.slack_messages | INSERT | `6257a3c4456db0bd2aeb872619d7a364` | DM `D04UP2L3E3S` (Robert–Leonard), Leonard, top-level, 2026-02-13T05:40Z (request message) | DM members include EMPLOYEE_0016 and EMPLOYEE_0038; ts coll. none | OK |
| 54–55 | trello.trello_cards | INSERT | `698e6548aa9516b76c4ab475` | board `640643a3fd8f3ca308d9318e` "Harmony Games", list `640643a3fd8f3ca308d93195` "To Do", idShort 456, shortLink NULL, url `…/c/N6TBAK8A/456-llc-what-we-take-from-hg`, dateLastActivity 2026-02-12T23:42Z | trello/data.json: board/list exist and are open; 449 board cards, max idShort 455, so 456 is next and unused; all 449 base cards have shortLink NULL and the same url pattern; card id hex prefix 698e6548 = 2026-02-12T23:42:00Z | OK |
| 56–57 | trello.trello_actions | INSERT | `698e65489a4031a95d3ce53e` | createCard by `PERSON_6094_TRELLO_USER_ID` (Leonard Hayes), same date | member resolves to Leonard; data_json shape matches base createCard actions; coll. none | OK |
| 59–70 | gmail.gmail_threads ×3 / gmail_messages ×3 | INSERT | threads `arthur.blake@…/1856975772057961391`, `robert@…/1856975772058401508`, `leonard.hayes@…/1856975772058497766`; message `<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>` per mailbox | Blake → Robert + Leonard "billing moved to my card", 2026-02-13T02:35Z (internal_date 1770950100000 matches); SENT for the sender, INBOX for the recipients | all 88,726 thread files streamed for every new thread number and Message-ID: 0 hits; history_id NULL (contract OK) | OK |
| 71–82 | gmail threads ×3 / messages ×3 | INSERT | threads `…/1856989298688254292` (leonard), `…/1856989298688559716` (robert), `…/1856989298688898804` (arthur); msg `<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com>` | Leonard → Robert, cc Blake "LLC money", 2026-02-13T06:10Z (1770963000000 matches) | 0 hits | OK |
| 83–94 | gmail threads ×3 / messages ×3 | INSERT | `robert@…/1856994331853686118` + `<136285951.151027292.1770967800000@email.apple.com>`; `arthur.blake@…/1856994331852829558` + `<375944835…457@email.apple.com>`; `leonard.hayes@…/1856994331852922225` + `<883960163…220@email.apple.com>` | App Review (SVC_4131) "We noticed an issue with your submission." for Domino Delights, Guideline 1.5 support option, 2026-02-13T07:30Z | sender SVC_4131_NAME/EMAIL matches base App Review mail (e.g. leonard@…_1837254479382458041.json); labels `Label_ad4e31dc09` (Testflight Notifications) and `Label_aeb79a643f` (App Center) exist in labels.json; 0 id hits | OK (advisory A-4) |
| 95–102 | gmail threads ×2 / messages ×2 | INSERT | `robert@…/1856987728970293624` + `<calendar-0b12e6f6-…@google.com>`; `arthur.blake@…/1856987728969768237` + `<calendar-cbc32ea4-…@google.com>` | Invitations "LLC: decide" Mon Feb 16 10:00–10:45 PT / 1:00–1:45 ET (= 18:00–18:45Z), sent 2026-02-13T05:45:03Z | Robert's subject token `([PERSON_NAME_0055])` matches 99 base invite subjects in Robert's mailbox; 0 id hits | OK |
| 104–109 | gcal.gcal_events ×3 | INSERT | `evt_c82c0965b68d959ee4241b` (leonard cal), `evt_f5f279f282d20ec86bb8e5` (robert cal), `evt_949ab837443564b6be0edf` (arthur cal) | one shared ical_uid `ede6e91c6f01552379e2f3a694ee537c@hg4`; start/end 2026-02-16T18:00–18:45Z (plan fields); created/updated 2026-02-13T05:45:00Z; `self` flag on each owner's copy | gcal/data.json: all three calendars exist; event ids and ical_uid unused; per-calendar copies sharing an `@hg4` uid is the base pattern; no clashing Feb 16 events on those calendars | OK |
| 111–112 | github.github_pull_requests | INSERT | `harmonygames-Games/GameOfDominoes#1917` | merged by EMPLOYEE_0025 (Arthur Blake); base_ref `Blake/boombitWithEcon`, head_ref `Blake/supportEmail`; base_sha `71a5f99d…`, head_sha `d67e7d02…`, merge `e1f05eab…`; created 2026-02-12T18:05Z, merged/closed 21:10Z | github/data.json: repo exists; 1,906 repo PRs, max #1916 (2025-12-26), so #1917 is unused and next; base_sha = head of base branch `arthur.blake/boombitWithEcon` | OK |
| 113–114 | github.github_branches | INSERT | `harmonygames-Games/GameOfDominoes:arthur.blake/supportEmail` | head_sha `d67e7d02…` | name unused; base maps every PR head_ref `Blake/X` to branch `arthur.blake/X` (checked 8/8), so this mirrors base | OK (see NB-13 note) |
| 115–118 | github.github_commits ×2 | INSERT | `d67e7d0277db893512d589e28ded199e5177b1c6`, `e1f05eabfc9ed3f2579d0f16e9fa281858268bda` | authored 17:40Z (before PR open) / merge 21:10Z; merge committer '' + SVC_0181, committed_date NULL, parent_shas '[]' | shas absent from commits; merge-commit fields match all base merge commits (e.g. #1915/#1916: committer '' / SVC_0181, committed_date NULL); all 12,687 base commits have NULL committed_date and empty parents | OK |
| 119–120 | github.github_pull_request_commits | INSERT | `…#1917#c_0` | commit d67e7d02, position 0 | id pattern matches base (`#999#c_0`); coll. none | OK |
| 121–124 | github.github_timeline_events ×2 | INSERT | `…#1917#ev_1` merged, `…#1917#ev_2` closed | 21:10Z, data commit_id = merge sha | pattern matches base merged/closed pairs; coll. none | OK |
| 126–127 | linear.linear_projects | INSERT | `0fa95761-d59b-4ff4-a8a3-15df3210ca6e` "LLC take-over" | team_ENG, lead `usr_63fffeb4fab5233e` (leonard.hayes), state started, start_date 2026-02-13, created 2026-02-12T23:24Z | linear/data.json: 2 base projects, no id/name collision; lead resolves; team exists | OK |
| 128–275 | linear.linear_issues ×37 | INSERT | `ENG-2438` … `ENG-2474` (numbers 2438–2474, identifier = id) | project above, team_ENG, creator Leonard, state_id 'Backlog', priority 0, labels/links/relations/state_history '[]', created 23:25:00–23:37:00Z at 20 s steps, updated_at = own comment time | 2,331 base ENG issues, max number 2437, so 2438–2474 continue with no gap and no collision (id and identifier); 'Backlog' is a base state literal (92 rows) | OK |
| 130–275 | linear.linear_comments ×37 | INSERT | one per issue: `comment_2bd90ac9…` (ENG-2438) … `comment_39bd0d5e…` (ENG-2474), full ids in SQL | authors `usr_63fffeb4fab5233e` (Leonard) or `usr_cc3e90160f490686` (arthur.blake); times 2026-02-13T00:24–01:37Z, all after their issue's created_at | base comments array is empty, so no collision; both authors are team_ENG members (tmem_team_ENG_*) | OK |

Linear comment-to-author map (SQL order): Leonard authors ENG-2438, 2439, 2440, 2441, 2447, 2448, 2449, 2450, 2451, 2452, 2453, 2454, 2455, 2460, 2461, 2463, 2464, 2465, 2466, 2467, 2468, 2469, 2470, 2471, 2472, 2473, 2474. Blake authors ENG-2442, 2443, 2444, 2445, 2446, 2456, 2457, 2458, 2459, 2462.

## 6. Check A — Records, references and IDs: PASS

- **Actors resolve, one account per person:** Slack EMPLOYEE_0038 = Leonard Hayes, EMPLOYEE_0025 = Arthur Blake, SLACK_BOT_0005 = Jenkins bot. Linear `usr_63fffeb4fab5233e` = leonard.hayes, `usr_cc3e90160f490686` = arthur.blake. Trello `PERSON_6094_TRELLO_USER_ID` = Leonard Hayes. GitHub EMPLOYEE_0025_GITHUB_USERNAME = Arthur Blake. Gmail/GCal/Drive use the existing roster emails. No new person accounts are created.
- **Parents and targets exist:** Drive parent folders are the owners' root folders. Slack channels/DMs exist and each author is a listed member. Both UPDATE targets exist, had no replies before, and are updated to match exactly one injected reply. The Trello board/list are open. The GitHub repo and base branch/sha exist. Linear team, lead and memberships exist. Children follow parents in the same transaction (Docs/Sheets/Slides after Drive, issues after the project, comments after issues).
- **Collisions (complete scope):** none found in gdrive `/drive_files`, gdocs, gsheets (398 spreadsheets, complete lookup), gslides (ids and object ids), Slack (687,230 messages in 5,353 files, complete lookup on 5 new ids; ts checked per channel), Trello cards/actions/idShort, Gmail (all 88,726 thread files streamed for 11 thread numbers + 7 Message-IDs), GCal event ids/ical_uid, GitHub PR/branch/commit/PR-commit/timeline ids, Linear project/issue/identifier/comment ids. Duplicate SQL keys: none. Gmail message ids and the shared Calendar ical_uid repeat across mailboxes/calendars by design, scoped per user as in base.
- **ID contracts:** Gmail history_id NULL on all 11 threads (OK). No Drive content_path is used; the native Doc/Sheet/Slides each have their content rows.
- **Readable Drive files:** both Docs have docs_documents rows with non-empty body_text; the Sheet has spreadsheet + sheet rows with a grid; the Slides deck has presentation/page/element rows. No media files.

## 7. Check B — SQL structure and supported schema rules: PASS

- 133 statements; every INSERT is single-row with matching column/value counts (lint parse; no missing_required). The 2 UPDATEs target primary-key predicates.
- No generated columns set (`text_fts` / `body_text_fts` absent).
- Linear text dates are all `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DD`, with no casts or `now()`. `state_history_json = '[]'` is supplied on all 37 issues.
- JSON: all 293 JSON literals parse (independent parse after unescaping `''` and `E''` strings), and shapes match the snapshot (slack `metadata_json '{}'`, arrays for `*_json` list columns).
- Provisional snapshot comparison: MATCH for all 21 affected tables per lint (no NOT COVERED entries). The snapshot is unverified, so this is not proof of live compatibility.

## 8. Check C — Dates, relationships and consistency: PASS

**Clock.** The latest event timestamp is the Apple mail at 2026-02-13T07:30Z, before 2026-02-14 00:00 UTC. The only later values are the Calendar plan fields (start/end 2026-02-16), which is allowed. All injected Slack posts (latest 2026-02-13T05:40Z) fall before the Slack export end noted in NB-6 (Feb 13 10:03 UTC).

**Chronology:**
- Commit 17:40Z → PR opened 18:05Z → merged 21:10Z → Jenkins #218 started 21:40Z → success 21:49:30Z → Blake's ENG-2462 comment "merged in #1917" at 01:30Z Feb 13.
- Drive notes on Mon Feb 9 (15:55 PT) → draft sheet on Tue Feb 10 (Leonard's DM: "my draft from Tuesday" ✓) → Linear project 23:24Z Feb 12 → Trello card 23:42Z → ground-rules doc 23:46Z (cites the card ✓) → comments 00:24–01:37Z Feb 13 → Leonard's request DM 05:40Z ("I'll email you how we split the money") → invite 05:45Z → split email 06:10Z.
- Every reply follows its parent, every comment follows its issue, and Gmail internal_date matches each Date header.

**Facts cross-checked against base** (base Slack #winddown `C0ADGSZKR3R` and #executives `C07C2866011`, 2026 files):

| Injected claim | Base evidence | Result |
|---|---|---|
| Figma prepaid to Sep 11 (ENG-2453) | #winddown 2026-02-12 01:21 Robert: "Our Figma is good until September 11th" | consistent |
| Helpshift: DD and ZM off before Feb 28 (ENG-2461) | #winddown 2026-02-11 05:58 Leonard: same | consistent |
| Singular termination letter in #winddown, deferred quarterly payment (ENG-2450) | #winddown 02-09 21:57 / 02-12 21:41 | consistent |
| AppsFlyer free tier up to 15K installs (ENG-2451) | #winddown 02-12 21:45 | consistent |
| layer.ai cancelled on the 11th (ENG-2454) | #winddown 02-11 19:23 Leonard: "I just canceled layer" | consistent |
| Soundly: Robert cancelled on the 11th (ENG-2455) | #winddown 02-11 19:48 Robert: "Soundly canceled" | consistent |
| Cursor and CodeRabbit cancelled on the 12th (ENG-2457/2458) | #winddown 02-12 22:50 / 22:59 Blake | consistent |
| Unity note: Blake sends Leonard's draft (ENG-2459) | #winddown 02-12 21:35 | consistent |
| Carta tied to the closed Chase account, no rush (ENG-2469) | #winddown 02-12 21:47–21:48 | consistent |
| Keep Deel/Gusto/Intuit, keep Linear during the transition, archive Google accounts after Feb 15, keep Slack/Google/GA/GitHub under HG until the data is extracted | #winddown 02-12 22:00 / 22:05 | consistent |
| Blake moves GitHub/dbt/Metabase billing to his Kub card (email, line 62) | #winddown 02-12 23:00 Blake | consistent |
| Lifestyle route in #executives (doc) | #executives 02-04 20:42 Leonard | consistent |
| "the way I wrote after the call on Wednesday": HG assets reach the LLC via Sunset's sale (doc) | #executives Wed 02-11 23:00 Leonard: "put our IP to auction and if no one buys it we can buy via our LLC" | consistent |
| Build machines go in Sunset's sale (ENG-2446) | #executives 02-11 19:45: Sunset liquidates "laptops build machines etc as well as IP" | consistent |
| ZM store listings moved to HG's accounts in July (ENG-2440) | Gmail 2025-07-15 Play Console: "Puzzles vs Zombies" transfer accepted by Harmony Games, completed 07-16 | consistent |
| Calm Play has its own Singular org (ENG-2472) | #prototype 02-11 17:41 Leonard posts `calmplayllc.sng.link` tracking links | consistent |
| VO campaign $100/day, $3k/month cap (Slack line 46, slide 2) | base parent "VO campaign is created…" (02-06), and the slide and reply agree with each other | consistent |
| Jenkins #218 on `Blake/boombitWithEcon` | base #216 on the same branch; #217 started 01-28 | consistent |

**Superseding values are supported as later records, not contradictions:**
- DD prod AWS: ENG-2441 ~$1k/"maybe $300" (00:48Z) is superseded by Blake's DM $140 (03:10Z) from the person who runs it.
- Metabase + dbt: ENG-2447/2448 ~$300 is superseded by Blake's email $100 + $100 + GitHub $48 = $248.
- Figma "LLC 0" in the draft sheet vs ENG-2453 "stays HG's".
- DD player support: ENG-2462 "done" is followed by Apple's later rejection (A-4).

These are stale-vs-later pairs with dates and named owners. No injected record contradicts another one with no ordering or authority to resolve it.

**Base-data conflicts:** none of the injected records builds on a listed Snowflake/Confluence conflict. The doc points to the warehouse daily revenue table for DD/ZM January revenue. That is not a listed conflict (NB-17 covers installs, not revenue), so no Check C advisory applies; /prompt must still confirm the values exist and are visible.

## 9. Findings

**Demonstrated defects: none.**

Advisories (non-blocking, no rule broken; listed for the author and later stages):

- **A-1 (cosmetic) — line 19, `f_a7af6f358dd5648c11a608` style_runs:** NORMAL_TEXT run 155–155 is zero-length. No base doc has a zero-length run, but no schema rule forbids it. Optional fix: drop the second run object.
- **A-2 (relationship, base-consistent) — lines 111–118:** after merging #1917, base branch `arthur.blake/boombitWithEcon` keeps head `71a5f99d…`, not the merge commit. The base doesn't move branch heads after merges either (1 of 46 checked), so this is not a defect.
- **A-3 (realism) — line 49:** Blake's "$140 a month" note is threaded under an unrelated Feb 2 git-config message in the Robert–Blake DM. The reference is valid, but the topic doesn't match. Optional: post it top-level (thread_parent_id NULL, drop the line-50 UPDATE).
- **A-4 (for /prompt) — lines 83–94 vs 111–124/227:** Apple's Feb 13 07:30Z rejection says DD's support option "still opens a support screen that doesn't load", after #1917/#218 replaced Helpshift and Blake marked ENG-2462 done. This reads as a later correction (it doesn't name the build), so it is not an integrity failure. /prompt should confirm the intended reading is the only defensible one.
- **A-5 (for /prompt) — line 267 vs line 17:** Leonard's ENG-2472 comment "Calm Play could just be our LLC" (01:10Z Feb 13) comes after his ground-rules doc ("The LLC is the new one Blake and I are setting up", 23:46Z Feb 12). "Could" is speculative, so the facts don't conflict, but /prompt's unique-ground-truth check should test it.
- **A-6 (for /prompt) — line 151:** ZM's hosting is only "well over $1k a month". The doc's revenue test for ZM depends on January revenue sitting clearly on one side of that.
- **A-7 (known issue NB-13):** the branch/head_ref naming mirrors base, so later stages shouldn't grade an exact branch name.

## 10. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All actors/parents/targets resolve; complete-scope collision checks found no duplicates across 10 services; Gmail history_id contract met; all Drive files readable; no second accounts. |
| B — SQL structure and supported schema rules | PASS | 133 statements parse; no generated columns; Linear text formats and required `state_history_json` present; 293/293 JSON literals valid with snapshot shapes. Snapshot comparison provisional (MATCH). |
| C — Dates, relationships and consistency | PASS | No event after the clock; chronology coherent; thread/reply counts correct; injected facts match base #winddown/#executives/Gmail; superseding values are dated later records from named owners; no grader-facing text. |

## 11. Stage provenance / reuse record

- `review_version: injection-static-v2`; `evidence_contract: stage-evidence-v1`; `reused_evidence: []`.
- SQL sha256 `7573eb1a6bca35e3fa5827e43eac1021821179d586b92c529852525b998a99d0`. Universe manifest sha256 `5e01ac44…de450`. Schema `31dcb2b4…5151`. ID contracts `fc4711ef…4682`.
- Source scopes used: linear/data.json (users, teams, projects, issues, comments, team_memberships); trello/data.json (boards, lists, cards, members, actions); gcal/data.json (calendars, events); gdrive/data.json `/drive_files`; gdocs/data.json `/docs_documents`; gslides/data.json `/slides_presentations`; gsheets/data.json `/sheets_spreadsheets` (complete lookup); slack channels.json, users.json, messages/*.json (complete id lookup) and the full C09UHHN6PFZ, D04V95AAAHW, D04UP2L3E3S and C05433XK267 histories; gmail labels.json and all threads/*.json (stream scan); github/data.json (repositories, branches, commits, commit_map, pull_requests, pull_request_commits, timeline_events, users).
- /prompt may reuse checks A–C for this exact SQL hash. Prompt incorporation, discoverability, Robert's visibility and solvability (including A-4 to A-6 and the Snowflake revenue lookup) are /prompt's job.

## 12. Limits

Outside the certified static scope: live execution and deployment, current database compatibility (the schema snapshot is unverified), search ranking, assigned-persona visibility and task difficulty. There are no unresolved required static checks.

### FINAL VERDICT: PASS

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (not otherwise reported by the runtime)

Next action: Proceed to /prompt

Evidence limits: None for the required static checks. Static scope only: no live deployment, database-compatibility, visibility or difficulty certification; the schema snapshot comparison is provisional.
