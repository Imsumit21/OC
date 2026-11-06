# /injection — Injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`: the 16 new or changed lines (12 data statements plus the header comment) checked NEW; the byte-identical statements' results REUSED from the prior report (see §11) |
| Mode | Chat/attachment review, static (no SQL executed, no base export modified) |
| Attempt | 6adfee3b47f7621feba5b96c |
| Actual review time | 2026-11-05T20:31:45Z |
| Clock | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal`, archive hg4-2026-08-31 v37; manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Input | `Evals/task_inputs/01_Universe_Inject.sql` (revision 9, saved from attachment `_uploads/01_Universe_Inject (4).sql`), 92,711 bytes, sha256 `f1a290ced1765a5b5ed0fe039b0f65428ea3924ab4269267bfea352a04211f10` |
| Previous SQL version | revision 6, 85,772 bytes, sha256 `4236a0301de9f4d287fb4a5be26e1dd6538cabe70f0c69b2031b167be11e1b76` (PASS / COMPLETE in prior report sha256 `6052e12e5eeaabc0750c2731081f50b91721b1e3fd5b2c4c231709e29e2cfd7b`); the diff was taken against the byte-identical saved upload `_uploads/01_Universe_Inject (3).sql` |
| References | Eval 0 `e034019b…6eff`; WORKFLOW.md `ee4cd8e1…fcd5d`; schema snapshot `injection.json` `31dcb2b4…5151` (unverified, provisional); `id_contracts.json` `fc4711ef…4682`; lint `hg_injection_lint.py` `a8226e2a…448b` (injection-lint-v1). All re-hashed this run and identical to the prior review. |
| Assignment (context only) | Robert, Co-founder & Creative Director; long-horizon (per SQL header and saved assignment) |

## 2. Input / authority issues

None. The new attachment was saved as the injection input (revision 9) and read before base searches. SQL comments (lines 1–4) are evidence of intent only. Line 3's statement count was updated to "136 INSERT (one row each), 3 UPDATE", which matches the lint parse. No comment mentions tool calls, pass rate or graders.

**Change set vs the previously reviewed SQL (line diff, NEW):** 276 → 291 lines; 133 → 141 statements (129 → 136 INSERT, 2 → 3 UPDATE). Every previously existing record key is unchanged.

| New line(s) | Record | Change |
|---|---|---|
| 3 | header comment | statement counts updated |
| 46 | Slack `6908b2f1…` (#prototype, Leonard, VO campaign reply) | text reworded: "$100/day capped at $3,000 a month… runs at from March (it's still in learning this week)… moves to our new company's card from March if we keep CF going, so count it as its own line in what we pay each month". Keys, thread and timestamp unchanged |
| 48–49 | **NEW** Slack `103ed629eef6bb64a30ab49eb5c8fe40` | #prototype `C09UHHN6PFZ`, Leonard (EMPLOYEE_0038), reply in thread `bdb4f7af…` (ts 1770837702.167889), ts 1770923700.470906 = 2026-02-12T19:15:00Z: "@Robert the CF character concept art is only in layer.ai, can you pull it out yourself before then? the art goes with CF, there's nothing on the layer account for our new company to take, it just lapses" |
| 50 | **NEW** UPDATE Slack `bdb4f7af824ec3819acdf5fc3cc480ea` | thread_ts_legacy = own ts, reply_count 1, reply_users_count 1, latest_reply 1770923700.470906 |
| 86–97 | **NEW** Gmail threads ×3 + messages ×3 | Blake → Robert, cc Leonard, subject "jenkins", 2026-02-13T04:20:00Z, Message-ID `<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com>`: jobs moved to Blake's own machine; build boxes are HG's and go with the laptops in the sale; shut down "the extra copy of CF's backend that was still running from the January redeploy, so CF's own account bills $62 a month now… still on HG's AWS bill till March like Domino's" |
| 142 | Linear project `0fa95761-…` description | state rules reworded: Done if one of us pays it himself through May (even if HG still owns it) or the LLC takes it with nothing left to do; Todo if the LLC takes it and something is still to do (assign the mover); Canceled if it stays with HG |
| 174 | Linear comment `comment_d7d8b2de…` (ENG-2445, Blake, 00:58Z) | CF AWS figure "$62" → "$95" |
| 210 | Linear comment `comment_3f50781a…` (ENG-2454, Leonard) | shortened to "cancelled it on the 11th" (art sentence moved to the new Slack reply) |
| 280, 282 | Linear issue ENG-2472 updated_at and comment `comment_ffcbb4c7…` created/updated_at | 2026-02-13T01:10:00Z → 2026-02-12T23:41:00Z |

## 3. Checklist

- [x] Save/reload SQL; hash, base manifest and review version recorded (NEW)
- [x] `hg_injection_lint.py` run on the new hash: 0 FAIL / 0 CHECK / 0 INFO across 141 statements (NEW)
- [x] Full operation ledger, 139 data statements (136 INSERT, 3 UPDATE) + BEGIN/COMMIT (new/changed rows NEW; others REUSED)
- [x] Check A: references and collisions (new keys checked NEW over complete Slack and Gmail collections; unchanged keys REUSED)
- [x] Check B: structure and schema rules (NEW via lint; new size_estimate recomputed NEW)
- [x] Check C: dates, relationships, consistency (new/changed facts NEW against base Slack/Gmail and the other SQL rows; unchanged cross-checks REUSED)
- [x] Coverage, findings, limits and one final verdict

## 4. Lint flags and resolutions

`hg_injection_lint.py` (injection-lint-v1, clock 2026-02-14T00:00:00Z, SQL sha256 `f1a290ce…1f10`) loaded base slack/users, trello, gmail/users, github, linear, contacts, confluence and parsed 141 statements (begin 1, insert 136, update 3, commit 1; slack_messages 6 insert + 3 update, gmail_threads 14, gmail_messages 14, linear_issues 37, linear_comments 37, etc.). **Flags: none (FAIL 0, CHECK 0, INFO 0).** Nothing to resolve. A clean lint is not a pass, so checks A–C were done below.

## 5. Operation ledger

All statements run in SQL order inside one `BEGIN … COMMIT`. Line numbers are for the new file. Rows marked NEW/CHANGED were checked this run. The rest are byte-identical to revision 6, and their results are REUSED from the prior report (sha256 `6052e12e…7b`, §5) under stage-evidence-v1, with the base manifest, references and record keys verified unchanged. There are no deletes or upserts. "Coll." = collision check against the complete base collection plus the other SQL rows.

| SQL lines | Service.table | Op | Record id(s) | Key values / relationships | Base check (path / pointer) | Result |
|---|---|---|---|---|---|---|
| 7–14 | gdrive.drive_files ×4 | INSERT | `f_1e468a9d69ea0f0a2001f5` (ground-rules Doc), `f_a7af6f358dd5648c11a608` ("LLC notes (Monday)"), `f_d996e4c434ce160dc52596` (Sheet "LLC 90 days (draft)"), `f_7d2c9e7822e87b92a11759` (Slides, owner robert) | parents = owners' root folders; dates 2026-02-08 to 02-12 | gdrive/data.json `/drive_files` (53,866 rows): coll. none (REUSED) | OK |
| 16–19 | gdocs.docs_documents ×2 | INSERT | same Doc ids | body_text non-empty (1,214 / 154 chars); style runs cover exact body length | coll. none (REUSED) | OK |
| 21–24 | gsheets spreadsheet + sheet | INSERT | `f_d996…` / sheet 0 | grid 5×8 | 398 base spreadsheets, 0 matches (REUSED) | OK |
| 26–39 | gslides presentation, 3 pages, 3 elements | INSERT | `f_7d2c…`, `slide_886d…`, `slide_0540…`, `slide_3482…`, `el_7e28…`, `el_4f79…`, `el_c309…` | BLANK layout text boxes | ids absent from gslides export (REUSED) | OK |
| 41–44 | slack.slack_messages ×2 | INSERT | `9ed17488…`, `85bc96b0…` | #builds Jenkins DD iOS Submission #218 start 21:40Z / success 21:49:30Z | bot member; base builds end at #217; coll. none (REUSED) | OK |
| 45–46 | slack.slack_messages | INSERT (text CHANGED, NEW) | `6908b2f17c379e809aafa6b2b169f4bf` | #prototype, Leonard, reply to `73ec270a…`, 2026-02-12T23:20Z; new text keeps $100/day, $3,000/month cap, Leonard's card to end of Feb, new company's card from March | parent = `messages/C09UHHN6PFZ/2026-02.json` "VO campaign is created…" by Leonard (REUSED); keys unchanged | OK |
| 47 | slack.slack_messages | UPDATE | `73ec270a3d07eb8d8488384898be079e` | reply_count 1, latest_reply 1770938400.370665 | unchanged (REUSED) | OK |
| 48–49 | slack.slack_messages | **INSERT (NEW)** | `103ed629eef6bb64a30ab49eb5c8fe40`, ts `1770923700.470906` | #prototype `C09UHHN6PFZ`, user EMPLOYEE_0038 (Leonard), mentions EMPLOYEE_0016 (Robert); thread_parent_id `bdb4f7af…`, thread_ts_legacy 1770837702.167889; created_at 2026-02-12T19:15:00Z = ts; metadata_json `'{}'`; reactions/files/attachments `'[]'` | channels.json: C09UHHN6PFZ (#prototype, not archived) members include EMPLOYEE_0016 and EMPLOYEE_0038. Parent = `messages/C09UHHN6PFZ/2026-02.json` `/575`: Leonard, ts 1770837702.167889 (2026-02-11T19:21:42Z), "canceled layer.ai account @EMPLOYEE_0033 - we have access until March 3rd", reply_count 0, thread_ts null. Thread scan of `messages/*/2026-*.json` for "1770837702.167889" (complete, 134 files): only `/575/ts`, so no existing replies. `lookup` id and ts over `messages/*.json` (complete, 687,230 records, 5,353 files): 0 matches each | OK |
| 50 | slack.slack_messages | **UPDATE (NEW)** | `bdb4f7af824ec3819acdf5fc3cc480ea` | thread_ts_legacy = own ts, reply_count 1, reply_users_count 1, latest_reply 1770923700.470906 | before: reply_count 0, latest_reply null, no replies; after matches exactly the one injected reply; same shape as the accepted line-47 update | OK |
| 51–53 | slack insert + UPDATE | INSERT / UPDATE | `ad623a2f…` / `bc4bc3d0…` | Robert–Blake DM, Blake "$140 a month" reply 03:10Z; parent reply_count 0 → 1 | unchanged (REUSED) | OK (advisory A-3) |
| 54–55 | slack.slack_messages | INSERT | `6257a3c4…` | Robert–Leonard DM, Leonard, 2026-02-13T05:40Z | unchanged (REUSED) | OK |
| 57–60 | trello card + createCard action | INSERT | `698e6548aa9516b76c4ab475` / `698e65489a4031a95d3ce53e` | board "Harmony Games", list To Do, idShort 456, 23:42Z, by Leonard | unchanged (REUSED) | OK |
| 62–73 | gmail threads ×3 / messages ×3 | INSERT | `…/1856975772057961391`, `…/1856975772058401508`, `…/1856975772058497766`; `<CA-Uw65DzW6…@mail.gmail.com>` | Blake "billing moved to my card", 02:35Z; size 1490 = body 590 + 900 | unchanged (REUSED) | OK |
| 74–85 | gmail threads ×3 / messages ×3 | INSERT | `…/1856989298688254292`, `…/1856989298688559716`, `…/1856989298688898804`; `<CAxkiKZL4o…@mail.gmail.com>` | Leonard "LLC money", 06:10Z; size 1254 = body 354 + 900 | unchanged (REUSED) | OK |
| 86–97 | gmail threads ×3 / messages ×3 | **INSERT (NEW)** | threads `arthur.blake@harmonygames.co/1856982378087055316`, `robert@harmonygames.co/1856982378087295205`, `leonard.hayes@harmonygames.co/1856982378087236711`; message `<mailbox>/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com>` per mailbox | From arthur.blake, To robert, Cc leonard.hayes, subject "jenkins". internal_date 1770956400000 = 2026-02-13T04:20:00Z = `date` = header "Fri, 13 Feb 2026 04:20:00 +0000" (13 Feb 2026 is a Friday). Labels: sender `["SENT"]`, recipients `["INBOX","IMPORTANT","CATEGORY_PERSONAL"]`, the same as both earlier injected internal emails. size_estimate 1265 = decoded body 365 + 900, the same offset as every other injected message. Thread snippet = message snippet = first 140 chars of body; history_id NULL | Complete `search-many` over `threads/*.json` (88,726 files, scan complete, no errors): Message-ID string 0 hits, each thread number 0 hits. `files gmail` for each thread number: 0 paths. All three mailboxes are existing roster users (lint identities clean) | OK |
| 98–117 | gmail App Review ×3, calendar invites ×2 (threads + messages) | INSERT | `…/1856994331853686118`, `…/1856994331852829558`, `…/1856994331852922225`; `…/1856987728970293624`, `…/1856987728969768237` | App Review rejection 07:30Z; "LLC: decide" invites 05:45:03Z | unchanged (REUSED; mailbox label patterns match base) | OK (advisory A-4) |
| 119–124 | gcal.gcal_events ×3 | INSERT | `evt_c82c…`, `evt_f5f2…`, `evt_949a…` | Mon Feb 16 18:00–18:45Z (plan fields); created 05:45Z | unchanged (REUSED) | OK |
| 126–139 | github PR #1917, branch, 2 commits, PR-commit, 2 timeline events | INSERT | `harmonygames-Games/GameOfDominoes#1917` etc. | commit 17:40Z → PR 18:05Z → merge 21:10Z | unchanged (REUSED) | OK (A-2, A-7) |
| 141–142 | linear.linear_projects | INSERT (description CHANGED, NEW) | `0fa95761-d59b-4ff4-a8a3-15df3210ca6e` "LLC take-over" | text only; team, lead, state, start_date, created_at unchanged | coll. none, lead/team resolve (REUSED) | OK |
| 143–290 | linear.linear_issues ×37 / linear_comments ×37 | INSERT | `ENG-2438` … `ENG-2474`; one comment each | Changed (NEW): line 174 ENG-2445 comment "$95"; line 210 ENG-2454 comment shortened; line 280 ENG-2472 updated_at 2026-02-12T23:41:00Z; line 282 ENG-2472 comment created/updated 2026-02-12T23:41:00Z. Ids, issue_ids and authors unchanged | ENG-2472 created 23:36:20Z < comment 23:41:00Z = updated_at (the same convention as the other 36 issues); `YYYY-MM-DDTHH:MM:SSZ` (lint). Keys: 2,331 base ENG issues, max number 2437; base comments empty (REUSED) | OK |

## 6. Check A — Records, references and IDs: PASS

- **New Slack reply (NEW):** author EMPLOYEE_0038 = Leonard Hayes, who also wrote the parent. The mention EMPLOYEE_0016 = Robert. Both are members of #prototype `C09UHHN6PFZ` (channels.json). The parent `bdb4f7af…` exists at `messages/C09UHHN6PFZ/2026-02.json` `/575` with no replies. The new id and ts are unused across all 687,230 Slack messages (complete lookup). The line-50 UPDATE targets an existing row, and its after-state matches exactly one injected reply.
- **New Gmail thread (NEW):** the three thread ids and the Message-ID are unused across all 88,726 base thread files (complete search-many plus file-name check). The sender and recipients are existing roster mailboxes, so no second accounts (lint identities check clean). `history_id` is NULL on all 14 thread rows, which meets the listed ID contract.
- **Changed Linear rows (NEW):** only text and timestamps changed. No id, issue_id or author changed.
- **Unchanged rows (REUSED):** actors resolve with one account per person (Slack EMPLOYEE_0038/0025/SLACK_BOT_0005, Linear `usr_63fffeb4fab5233e`/`usr_cc3e90160f490686`, Trello `PERSON_6094_TRELLO_USER_ID`, GitHub EMPLOYEE_0025). Parents and targets exist. All other key collisions were checked against complete collections in the prior reviews, and those keys and the base are unchanged. No duplicate keys inside the SQL (the new keys are distinct from every other SQL key).
- **Readable Drive files (REUSED):** both Docs have non-empty body_text; the Sheet and Slides have their content rows.

## 7. Check B — SQL structure and supported schema rules: PASS

- 141 statements; every INSERT is single-row with matching column/value counts (lint parse, NEW; no missing_required). The 3 UPDATEs use primary-key predicates.
- No generated columns set (`text_fts` / `body_text_fts` absent).
- Linear text dates are all `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DD`, including the changed ENG-2472 values. There are no casts or `now()`, and `state_history_json = '[]'` is set on all 37 issues (lint, NEW).
- JSON (NEW): the new Slack row has `metadata_json '{}'` and list-shaped reactions/files/attachments. The new Gmail rows' label, recipient, header and attachment arrays are valid JSON lists. Lint json_shape is clean.
- Escaping (NEW): `there''s`, `HG''s`, `CF''s`, `Domino''s`, `that''s`, `it''s`, `company''s` are doubled correctly. The Gmail bodies use `E'…\r\n…'` like the other injected messages.
- `size_estimate` (NEW): 1265 = decoded body 365 + 900.
- Provisional snapshot comparison: MATCH for all 21 affected tables per lint. The snapshot is unverified, so this is not proof of live compatibility.

## 8. Check C — Dates, relationships and consistency: PASS

**Clock (NEW).** The new events are 2026-02-12T19:15Z (Slack reply) and 2026-02-13T04:20Z (Gmail). ENG-2472 moved to 2026-02-12T23:41Z. The latest event overall is still the App Review mail at 2026-02-13T07:30Z, before 2026-02-14 00:00 UTC. Only Calendar start/end and the project start_date are later, and they are plan fields.

**New and changed facts checked against base and the rest of the SQL (NEW):**

| Record | Check | Result |
|---|---|---|
| Lines 48–50 Slack reply: concept art only in layer.ai, "pull it out yourself before then", nothing for the new company to take, "it just lapses" | "before then" resolves to the parent's "we have access until March 3rd" (base `/575`, Feb 11). The reply (Feb 12 19:15Z) follows its parent (Feb 11 19:21:42Z). Consistent with ENG-2454 "cancelled it on the 11th" (line 210) and the doc's "the games with their art… come to it only through Sunset's sale" (line 17): the art travels with the game, and the subscription has nothing to transfer. Slack 2026 scan for "layer" (complete, 134 files) shows no record that keeps or moves the layer.ai account | consistent |
| Lines 86–97 Gmail "jenkins": jobs moved "tonight" | 04:20Z = 20:20 PT on Feb 12, so "tonight" holds. It fulfils Blake's ENG-2446 comment at 01:07Z (line 178), "I'll move our jenkins jobs to my own machine before then". "Build boxes are HG's… go with the laptops whenever the sale needs them" matches line 178 and the base #executives sale list (REUSED). Base #builds `C05433XK267/2026-02.json` has no posts after 2026-02-13 00:00Z, so no later base build contradicts the move | consistent |
| Same email: extra CF backend copy from "the January redeploy" shut down; CF's account now $62/month; on HG's AWS bill till March "like Domino's" | Base Blake DM `D04UY3DQJE5/2026-01.json` /18–/26 (2026-01-29 to 01-31): the CF backend first ran behind a us-west-1 load balancer (`ComboF-Combo-iCqjMyeKWboh…us-west-1`), then was deployed again with CDK into the `hg-cf-prod-admin` account in us-east-1 (`ComboF-Combo-DH80wG0lCkb1…us-east-1`). So two copies after a January redeploy is supported. ENG-2445's "about $95" (00:58Z) is the earlier figure from the same owner, and the email (04:20Z) gives the reason it fell, so this is a dated supersession, not a contradiction. "Like Domino's" matches Blake's DM (line 52, 03:10Z): "still on HG's AWS bill till then". Gmail "redeploy" (complete, 88,726 files): only unrelated newsletters and a Unity notice; "combo fighter aws": 0 hits. No base record gives another CF-account cost | consistent |
| Line 46 VO reply rewording | Same figures as before ($100/day, $3,000/month cap, Leonard's card to end of Feb). "Our new company's card from March" matches the doc's "new one Blake and I are setting up" and Leonard's split email (line 85: "whatever one of us already pays personally counts toward his third") | consistent |
| Line 142 project rules | Text-only rule change. It doesn't conflict with any record: every issue is still Backlog, and the rules govern future moves. "Pays it himself through May" matches the split email (line 85) and the plan window in the doc (March 1 to May 31) | consistent |
| Line 174 ENG-2445 "$95" | See the email row above (superseded at 04:20Z by $62) | consistent |
| Lines 280/282 ENG-2472 at 23:41Z | After issue creation (23:36:20Z). Now precedes the ground-rules doc (23:46Z), which names the LLC as "the new one Blake and I are setting up", so the doc is the later word (see A-5) | consistent |

**Unchanged cross-checks (REUSED from prior report §8, rows byte-identical, base unchanged):** chronology commit 17:40Z → PR 18:05Z → merge 21:10Z → Jenkins #218 21:40–21:49:30Z → App Review rejection 07:30Z; notes Feb 9 → draft sheet Feb 10 → project 23:24Z → Trello card 23:42Z → doc 23:46Z → comments 00:24–01:37Z Feb 13 → billing email 02:35Z → DM $140 03:10Z → **jenkins email 04:20Z (NEW)** → request DM 05:40Z → invite 05:45Z → split email 06:10Z. Every reply follows its parent, and Gmail internal_date matches each Date header. The base fact matches recorded previously stand (Helpshift DD/ZM only, AppsFlyer free tier, layer.ai/Soundly cancelled on the 11th, Firebase Blaze plan, Kub-card billing, IP via Sunset's sale, build machines at Blake's, App Review mailbox patterns, and others).

**Superseding values are dated later records from named owners (REUSED + NEW):** DD prod AWS ~$1k / "maybe $300" → $140 (03:10Z); Metabase + dbt ~$300 → $248 email (02:35Z); Figma "LLC 0" → ENG-2453 "stays HG's"; ENG-2462 "done" → App Review rejection; **CF AWS ~$95 (00:58Z) → $62 (04:20Z, NEW)**.

**Grader-facing text (NEW for new/changed rows):** none. The new Slack reply and email are colleagues writing to each other, and the project description is an instruction to the team on its own issues. None addresses a solver or grader or describes the test. Lint grader_language: 0 flags.

**Base-data conflicts:** no injected record builds on a listed Snowflake/Confluence conflict. Advisory A-9 below covers the nearby NB-2 (Snowflake AWS totals).

## 9. Findings

**Demonstrated defects: none.**

Advisories (non-blocking, no rule broken):

- **A-2 (REUSED), lines 126–133:** after #1917 merges, the base branch head isn't moved. Base doesn't move branch heads after merges either.
- **A-3 (REUSED, realism), line 52:** Blake's "$140 a month" DM is threaded under an unrelated Feb 2 message. The reference is valid. Optional: post it top-level and drop the line-53 UPDATE.
- **A-4 (REUSED, for /prompt), lines 98–109:** the App Review rejection reads as a later correction to #1917. /prompt should confirm DD's player-support item has one defensible call.
- **A-5 (UPDATED, for /prompt), line 282 vs lines 17, 46, 49:** "Calm Play could just be our LLC" is now at 23:41Z. The later doc (23:46Z) and both Leonard Slack replies say "our new company" / "the new one Blake and I are setting up". The ordering now favours the new company. /prompt's ground-truth check should still confirm nothing hinges on the Calm Play idea.
- **A-6 (REUSED, for /prompt):** no injected record gives a ZM hosting figure. /prompt must confirm Robert can see a source for it, or that the call doesn't depend on the exact figure.
- **A-7 (REUSED, known issue NB-13):** don't grade an exact branch name.
- **A-8 (REUSED, for /prompt):** CF's $0 items (Firebase/BigQuery, store-listing support, GA). Base Firebase Blaze plan and the Jan 9 support-tool DM don't contradict the SQL.
- **A-9 (NEW, for /prompt), lines 86–97 and 174:** the CF AWS figure now has two dated values from Blake: $95 in ENG-2445 (00:58Z) and $62 in an email to Robert (04:20Z) that gives the reason. Both records are visible to Robert, so the expected answer should use $62. Snowflake's HG-wide monthly AWS totals ($1,485–$2,745, known issue NB-2) are a company total, not CF's account, so keep the rubric off the Snowflake AWS figures.

## 10. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | New Slack id/ts unused (complete, 687,230 records). New Gmail thread ids and Message-ID unused (complete, 88,726 files). Parent `bdb4f7af…` exists with no replies; author and mention are #prototype members. Existing keys unchanged (REUSED). history_id contract met; Drive files readable; no second accounts. |
| B — SQL structure and supported schema rules | PASS | Lint clean on the new hash (141 statements). No generated columns. Linear formats and `state_history_json` present. New size_estimate = body + 900. JSON shapes and escaping valid. Snapshot comparison provisional (MATCH). |
| C — Dates, relationships and consistency | PASS | All events at or before the clock. The new reply follows its parent, and "before then" = March 3rd from the base parent. The jenkins email fulfils ENG-2446, and base Jan 29–31 DMs show the us-west-1 → us-east-1 CF redeploy. $95 → $62 is a dated supersession. ENG-2472 comment follows issue creation. No grader-facing text. |

## 11. Stage provenance / reuse record

- `review_version: injection-static-v2`; `evidence_contract: stage-evidence-v1`.
- `reused_evidence`: prior report `Evals/task_inputs/reports/0_injection.md` sha256 `6052e12e5eeaabc0750c2731081f50b91721b1e3fd5b2c4c231709e29e2cfd7b` (which itself reused the review sha256 `3d38911e…e287`). Reused: §5 ledger rows for the byte-identical statements, §6 collision/reference results for unchanged keys, §7 JSON checks for unchanged literals, and §8 chronology and base fact cross-checks. Dependencies verified unchanged this run: universe manifest `5e01ac44…de450`, the Eval 0, WORKFLOW, schema, id_contracts and lint hashes, the clock, and every pre-existing record key (line diff vs revision 6: changed lines 3, 46, 142, 174, 210, 280, 282 keep their key literals; added lines 48–50 and 86–97).
- NEW this run: lint on SQL `f1a290ce…1f10`; Slack `lookup` id and ts over `messages/*.json` (complete, 687,230 records, 5,353 files); direct read of `messages/C09UHHN6PFZ/2026-02.json` (727 records; parent `/575` and neighbours) and `channels.json` (#prototype members); Slack `search-many` over `messages/*/2026-*.json` (complete, 134 files) for the parent ts, "redeploy", "backend", "aws", "jenkins", "layer" and "concept art"; direct reads of `messages/C05433XK267/2026-02.json` (no posts after Feb 13 00:00Z) and `messages/D04UY3DQJE5/2026-01.json` /16–/27; Gmail `search-many` over `threads/*.json` (complete, 88,726 files) for the Message-ID, the 3 thread numbers, "redeploy" and "combo fighter aws"; Gmail `files` check for each thread number; size_estimate and label comparison against the other injected Gmail rows.
- /prompt may reuse checks A–C for SQL sha256 `f1a290ce…1f10`. Prompt incorporation, discoverability, Robert's visibility and solvability (including A-4 to A-6, A-8 and A-9) belong to /prompt.

## 12. Limits

Outside the certified static scope: live execution and deployment, current database compatibility (schema snapshot unverified), search ranking, assigned-persona visibility and task difficulty. The Gmail "jenkins" query hit its 60-match limit and the Slack "aws"/"backend" queries are discovery only. None is used as proof of absence; the collision checks above are complete-scope. No unresolved required static checks.

### FINAL VERDICT: PASS

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (not otherwise reported by the runtime)

Next action: Proceed to /prompt

Evidence limits: None for the required static checks. Static scope only: no live deployment, database-compatibility, visibility or difficulty certification; the schema snapshot comparison is provisional.
