# Injection data-integrity review: Eval 0

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1` (base facts reused from the previous `injection-static-v2` report, SHA-256 `dad52a1a44f6b43ddd514024c380f974947cf718d4b033a6f77610712518f3db`, only for statements that are byte-identical; every changed or new statement checked new) |
| Mode | Chat review, audit (attempt 6aea4c1e9b621f28dc3a5332) |
| Review time | 2026-11-05 |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` (re-hashed, unchanged) |
| Input | `Evals/task_inputs/01_Universe_Inject.sql` (injection revision 7, uploaded as `01_Universe_Inject (4).sql`), 61,537 bytes, SHA-256 `3afbf7cbbdb7611dad909cfc7244829642e03e136b66c5c555fe77d28570dd63` (attachment to the /injection message) |
| Previous version | SHA-256 `4c6328ab2e86835892054641d61871f9c304db667e4e27446eabfd71489b5e47` (PASS / COMPLETE) |
| Schema snapshot | `Evals/references/schema/injection.json` SHA-256 `31dcb2b43feca8e5c7cb67f37973f819c9b9774f12f8b15cb7da89ecd74c5151` (unverified snapshot, provisional; unchanged) |
| ID contracts | `Evals/references/schema/id_contracts.json` SHA-256 `fc4711ef07667333c1cf2a417279826f0432539195f7acdfacfa86e9d9ed4682` |
| Lint | `hg_injection_lint.py` injection-lint-v1 |

## 2. Input / authority issues

- SQL comments mention a dossier and a `universe_schema_live.json`; neither was supplied. Treated as statements of intent, not evidence.
- No grader-facing text and no comments about padding, tool calls or pass rate (lint and manual read of all changed text).

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, manifest and version | NEW, done |
| Diff against the previously reviewed SQL | NEW, done. Changes: (a) new Slack reply `097c95c6…` (statement 2) and the parent's reply fields on statement 1; (b) Gmail statements 8–13 text: "Season 2 opens" → "The November season opens" (snippets re-cut); (c) gcal 20–23 description: "The live-ops server windows go live" → "The server windows that are still on the DEV stack go live"; (d) Docs statement 26: one rules paragraph rewritten (+119 chars) and `style_runs_json` re-offset; (e) GitHub `#470#rc_10` (40) and its Slack mirror (57): added "The Plague Race, leagues, Endless and Season Pass schedules are already running on prod."; (f) GitHub `#471#c_18` (54) and its Slack mirror (61): "it is in submission 135" → "it is in both submission builds from today, iOS 50 and Android 135, so nothing is left on it"; (g) Linear `cmt_zom565_1` (71): "went in with build #2023" removed; (h) Linear `cmt_zom543_1` + ZOM-543 UPDATE (74–75): time 2025-09-29T18:20Z → 2025-09-30T16:20Z. All other lines byte-identical |
| Run lint; resolve every flag | NEW on the new SHA, done (0 flags) |
| Inventory every statement | NEW, done (111 statements: 77 INSERT, 34 UPDATE; no DELETE, upsert or conflict clause). Statement numbers from 2 on are one higher than in the previous report because of the new statement 2 |
| Check A | NEW for statements 1–2, 8–13, 20–23, 26, 40, 54, 57, 61, 71, 74–75; REUSED for identical ones: PASS |
| Check B | NEW (whole file parsed, column/value counts, JSON literals, lint) + REUSED: PASS (snapshot mismatches advisory) |
| Check C | NEW for every changed claim (checked against base Sheets, Slack, Linear and the other injected records); REUSED for identical ones: PASS |
| Report coverage, findings, limits, verdict | done |

## 4. Lint

`hg_injection_lint.py` ran on SHA `3afbf7cb…dd63` against universe synthcut, clock 2025-10-01T07:00:00Z, loading slack/users, gmail/users, github, linear, trello, contacts and confluence. Counts: FAIL 0, CHECK 0, INFO 0. Checks run: future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape. Nothing to resolve. A clean lint is not a PASS, so checks A–C were completed.

## 5. Operation ledger

"REUSED" rows are byte-identical to the previous version (report SHA `dad52a1a…f3db`, section 5, where their number was one lower from row 2 on); their base facts came from complete scans against the same universe manifest (`da2f4cf0…a1a`, re-hashed now), schema snapshot (`31dcb2b4…151`, re-hashed now) and clock, so reuse conditions 1–4 of `stage-evidence-v1` hold.

| # | Table | Op | Record / target | Key values | Check result | Basis |
|---|---|---|---|---|---|---|
| 1 | slack.slack_messages | INSERT | `8b090dec…` DM D05SD5QLG94 | Frederick Stone (EMPLOYEE_0008) to Julia, 2025-09-30T20:20:00Z; now reply_count 1, reply_users_count 1, latest_reply `1759263878.305127`, thread_ts_legacy = own ts | Members of D05SD5QLG94 (`slack/channels.json`, re-read): EMPLOYEE_0005, EMPLOYEE_0008, …; ID unique (reused); reply fields match exactly one reply (statement 2) by one user | NEW (reply fields) / REUSED (ID) |
| 2 | slack.slack_messages | INSERT | `097c95c6e043ada8294b60f13e1656ba` reply in D05SD5QLG94, parent `8b090dec…` | EMPLOYEE_0008, ts 1759263878.305127 = created_at 2025-09-30T20:24:38.305127Z (13:24 PT), thread_ts_legacy = parent ts, metadata `{}` | **New.** ID absent from all 610,468 base Slack messages (`lookup` `messages/*/*.json`, 4,840 files, scan complete, 0 errors) and appears once in the SQL; ts unique in the DM (base DM 2025-09 ts all ≤ 1758221424) and in the SQL; author is a DM member; reply 4 min 38 s after its parent. **Claims checked:** the "PNs Beta tab" exists in base spreadsheet "Push Notifications Zombie Match" (`gsheets/data.json /sheets_spreadsheets/220/sheets/1`, 15 rows incl. header); the four rows it leaves off all exist there: Hourly Coins (row 2), Nathan's Treasure Hunt (row 8), Streak Fever (row 10), Axe Arena (row 11); "local notifications" rows exist (rows 2–6). "Zombie Lane … permanent track with no window or reset" fits base #zombie-design 2025-09 /492 ("trophy path (AKA Zombie Lane)") and the level-based reward messages (#zombie-design 2025-09 /0, /496); no base message gives Zombie Lane a window or reset. The naming-rule clarification is a later word (Sep 30) by the doc's own author (doc dated Sep 24), not a contradiction | NEW |
| 3 | slack.slack_messages | INSERT | `2e75e232…` reply in C08R8CHB0QL | Robert (EMPLOYEE_0016), 2025-09-18T16:40Z; parent `9025d428…` | Parent in same channel; reply after parent; member | REUSED |
| 4 | slack.slack_messages | INSERT | `58d06bd5…` reply in DM D05GU6L0XFH | Robert, 2025-09-30T22:10Z; parent `c5431028…` | Parent exists; reply after parent; members. Advisory A5 | REUSED |
| 5 | slack.slack_messages | INSERT | `fa3eee2c…` C0880U9751A | Vincent Parker (EMPLOYEE_0012), 2025-09-30T20:50:12Z, "Re-tested the weekly leaderboard on the current prod build…" | Member; ID unique; consistent with base 0.3.49 iOS release (C0880U9751A 2025-09 /463). Advisory A9 | REUSED |
| 6–7 | slack.slack_messages | UPDATE | `9025d428…`, `c5431028…` | reply_count 0→1 each | Base counts 0, so +1 correct | REUSED |
| 8–13 | gmail threads/messages | INSERT ×6 | thread `…/1844470925517303296` (Brian, Julia, Frederick) | Brian Foster, 2025-09-22T09:12Z; text now "The November season opens on Sat Nov 1" | IDs unchanged and unique (reused). Text change only renames the season; Sat Nov 1, 2025 is a Saturday; "Wed Oct 29" unchanged and correct. Thread and message snippets both re-cut and match the body's opening ("Julia, Handing over … The config handoff we agreed wit") | NEW (text) / REUSED (IDs) |
| 14–19 | gmail threads/messages | INSERT ×6 | thread `…/1844835127305531392` | Brian, 2025-09-26T07:40Z; Wed Oct 29 → Fri Oct 31 | Unchanged. Advisories A2, A3 | REUSED |
| 20–23 | gcal.gcal_events | INSERT ×4 | `evt_9a4c…`, `evt_5c1e…`, `evt_a72f…`, `evt_1d6b…` | Release 2025-10-08 15:00–16:00Z; description now "The server windows that are still on the DEV stack go live with this release" | IDs unique (reused); start/end are plan fields; the narrower wording agrees with statements 40/57 (only Collect & Win windows still on DEV; the rest already on prod). Advisory A7 | NEW (text) / REUSED (IDs) |
| 24 | gdrive.drive_files | INSERT | `d_5f2c8e1b…` folder "ZM Live Ops" | parent `d_8140f09b…` (Julia root) | ID/name unique; parent exists | REUSED |
| 25 | gdrive.drive_files | INSERT | `f_7c3e91a4…` "working rules" doc | Frederick owner, Julia reader | ID unique | REUSED |
| 26 | gdocs.docs_documents | INSERT | `f_7c3e91a4…` | body now 2,634 chars; "When a beat starts" paragraph adds "A beat that is only waiting on that release starts late, it is not held." and "For the quest rollover and the daily gift (the Login Calendar row on the push sheet) …" | Style runs recomputed against the new body: TITLE 0–43 and HEADING_2 163–181 "Span and time base", 424–429 "Scope", 611–629 "When a beat starts", 1217–1228 "Held or not", 1715–1723 "One-offs", 1916–1927 "Still to do", 2145–2154 "Push copy", 2471–2483 "Config locks": each starts and ends at a line boundary and covers exactly its heading line. The "Login Calendar" row exists on the PNs Beta tab (`/sheets_spreadsheets/220/sheets/1` row 12, "Login Calendar update") | NEW |
| 27–34 | drive_files + slides presentation/pages/elements | INSERT | `f_2b9d4e7a…` "ZM3D beta UA plan", 3 slides | Frederick, 2025-09-23 | IDs unique; readable | REUSED |
| 35–38 | drive_files + sheets_spreadsheets + sheets_sheets ×2 | INSERT | `f_e4a17c90…` | Julia owner, Frederick reader | IDs unique; parent from #24 | REUSED |
| 39 | github.github_reviews | INSERT | `#470#rev_10` | EMPLOYEE_0025, COMMENTED, 2025-09-30T16:04:12Z | Unique (2,230 base reviews); next after base `rev_9` | REUSED |
| 40 | github.github_review_comments | INSERT | `#470#rc_10` → `#470#rev_10` | 2025-09-30T16:04:12Z; body adds "The Plague Race, leagues, Endless and Season Pass schedules are already running on prod." | ID unique (reused). **Claim checked:** base shows these on prod before Sep 30: #zombie-bugs 2025-08 /805 (EMPLOYEE_0012, Aug 29, "ios 1504 prod env • Endless mode didnt refresh daily … plague race didn't refresh daily"), #zombie-bugs 2025-09 /879 (Sep 21, endless bug on "production build"), #zombie-ops 2025-09 /21 (Sep 12, "test the premium buy on a prod build" for Season Pass); no base message in the ZM channels (Sep 2025 scan of #zombie-match3d, -bugs, -ops, -design, -art, zm-collect-win and the Season Pass channel) says any of these is still on DEV. "Leagues running" does not contradict statement 5 (rollover still broken on prod): a running schedule with a reset bug | NEW |
| 41–42 | github timeline + PR UPDATE | INSERT/UPDATE | `#470#ev_9`; PR updated_at → 16:04:12Z | | Unchanged | REUSED |
| 43–46 | github reviews / review_comments / timeline / PR #370 | INSERT/UPDATE | `#370#rev_1`, `#370#rc_1`, `#370#ev_5` | | Unchanged | REUSED |
| 47–50 | same for #438 | INSERT/UPDATE | `#438#rev_4`, `#438#rc_74`, `#438#ev_9` | | Unchanged | REUSED |
| 51–53 | pr_comments / timeline / PR #454 | INSERT/UPDATE | `#454#c_4`, `#454#ev_6` | Marcus Bennett | Unchanged | REUSED |
| 54 | github.github_pr_comments | INSERT | `#471#c_18` | Samuel Turner (EMPLOYEE_0004), 2025-09-30T21:07:26Z (14:07 PT); body now "it is in both submission builds from today, iOS 50 and Android 135, so nothing is left on it and that one can be closed" | ID unique (reused). **Claim checked against the base numbering:** ZM3D store builds use the 0.3.N patch number as the build number (e.g. #zombie-bugs 2025-08 /416 "0.3.16 (16)", 2025-09 /878 "testflight 39 is the submission candidate" = 0.3.39); iOS 0.3.49 was released on Sep 29 (#zombie-match3d 2025-09 /463), so iOS 50 the next day is the next number; Android required version was 0.3.127 on Sep 23 (#zombie-match3d 2025-09 /407), so Android 135 a week later fits. The Jenkins CI counters in #builds (Android #20xx, iOS Internal #17xx) are a different series and don't conflict. No base message names a different Sep 30 submission build | NEW |
| 55–56 | timeline / PR #471 | INSERT/UPDATE | `#471#ev_8` | | Unchanged | REUSED |
| 57–66 | slack.slack_messages INSERT ×5 + UPDATE ×5 | bot mirrors in C093LEZGF6J | parents `c2b9c903`(16→17), `d648cbe9`(2→3), `2f138acf`(78→79), `ef414467`(3→4), `da3fe08c`(7→8) | ts = GitHub created_at | IDs, ts, parents and counts unchanged and correct; the mirror texts of 57 and 61 now match their GitHub comments (40, 54) character for character. Advisory A4 | NEW (text) / REUSED |
| 67–70, 72–73, 76–109 | linear.linear_comments INSERT + linear_issues UPDATE | ZOM issues except ZOM-565 and ZOM-543 | | Unchanged | REUSED |
| 71 | linear.linear_comments | INSERT | `cmt_zom565_1` | usr_c77c50cc15c5342d, 2025-09-29T16:05:00Z; "went in with build #2023" removed | Text change removes a claim only; ID, author, time unchanged. Base ZOM-565 (`linear/data.json /issues/3642`) created/updated 2025-09-25T13:46:04Z, so the UPDATE (72) still moves forward. Advisory A8 (SC-16) unchanged | NEW (text) / REUSED |
| 74–75 | linear.linear_comments INSERT + linear_issues UPDATE | `cmt_zom543_1`, ZOM-543 | usr_49b9dfa5208d400d (the issue's assignee), now 2025-09-30T16:20:00Z | Base ZOM-543 (`/issues/3618`, "Queue Manager") updated_at 2025-09-25T17:44:22Z → 2025-09-30T16:20:00Z moves forward; comment created = updated = issue updated_at; `YYYY-MM-DDTHH:MM:SSZ` format; 09:20 PT Sep 30, before the clock; no other statement touches ZOM-543 | NEW |
| 110 | trello.trello_actions | INSERT | `68dac820…` commentCard | Brian Foster, 2025-09-29T17:55:44Z | Unchanged | REUSED |
| 111 | trello.trello_cards | UPDATE | `6851a724…` | badges.comments 1→2 | Unchanged | REUSED |

Internal duplicates: the only repeated leading values are the three Drive file IDs, each used once in `drive_files` and once per content table row (Docs, Slides presentation/pages/elements, Sheets spreadsheet/sheets), which is the expected cross-table link, not a key collision. The new Slack ID and ts appear once.

## 6. Checks

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | New key `097c95c6e043ada8294b60f13e1656ba` is absent from the complete Slack message collection (610,468 records, 4,840 files, scan complete) and unique in the SQL; its author EMPLOYEE_0008 is a member of D05SD5QLG94 and its parent `8b090dec…` is created earlier in the script. Linear targets ZOM-543 (`/issues/3618`) and ZOM-565 (`/issues/3642`) exist (complete `/issues` scan, 3,687 records). All other keys, actors and references are unchanged from the previous review, where every one resolved and every new key was unique across complete scans. One account per person; listed ID contracts met; Drive files readable. |
| B — SQL structure and supported schema rules | PASS (provisional) | 111 statements parse (lint parser, 0 unparsed); column and value counts match on every INSERT; no NOT NULL column omitted; `*_json` literals parse with the expected shape (new message `metadata_json` `{}`, list fields `[]`; doc `style_runs_json` a list); no generated column written; Linear dates in `YYYY-MM-DDTHH:MM:SSZ`. Snapshot comparison: MISMATCH (advisory A1). |
| C — Dates, relationships and consistency | PASS | All event timestamps are at or before 2025-10-01T07:00Z (latest 2025-09-30T22:10Z); only gcal start/end (2025-10-08) are later, as plan fields. Thread: parent reply_count/reply_users_count/latest_reply match the single new reply, which follows its parent. Every new or changed factual claim matches the base: the PNs Beta tab and its Hourly Coins, Nathan's Treasure Hunt, Streak Fever, Axe Arena and Login Calendar rows exist; Zombie Lane is a level-based trophy path; Plague Race, Endless and Season Pass were on prod before Sep 30; iOS 50 / Android 135 follow the base build numbering. The changed injected records agree with each other (gcal "still on the DEV stack" = rc_10's Collect & Win only). Doc heading runs match their heading lines. No grader-facing text. |

## 7. Findings

No demonstrated defects.

### Advisories (do not affect the verdict)

- **A1 · schema snapshot:** columns not in the bundled snapshot: `gcal_events.extras_json`, `drive_files.drive_id`, `slides_pages.notes`, `slides_page_elements.table_json/ordinal`, `github_review_comments.pull_request_review_id/side/start_line/start_side/subject_type/seq`, `github_reviews.seq`, `linear_comments.sequence`. If the live database lacks any of these, the script won't load.
- **A2 · Gmail threading:** the correction mail (14–19) has "Re:" and In-Reply-To/References but its own thread ID; Gmail would normally keep it in thread `1844470925517303296`.
- **A3 · Gmail snippet:** the correction's snippet ("Correction to my Sep 22 mail: the November…") differs from how its body starts ("Correction to my Sep 22 mail, Frederick in copy: …").
- **A4 · Slack mirrors (57–65):** subtype `bot_message` and pretext author `EMPLOYEE_0025_GITHUB_USERNAME`, whereas base #zombie-prs mirrors use subtype null and handles like `arthur.blake`.
- **A5 · Halloween retraction placement (4):** threaded under Robert's unrelated "hardcore players" DM message; findability is a `/prompt` question.
- **A6 · authority wording (doc #26):** "Product latest dated approval … if he takes that back": the approver in the data is Robert (Co-Founder & Creative Director), while Julia is the Product Manager. Hand-off to `/prompt`.
- **A7 · minor shape:** gcal `transparency='transparent'` (base all `opaque`); new reviews logged as `commented` timeline events (base uses `reviewed`). The earlier note about `thread_ts_legacy` on message 1 no longer applies: it now has a reply, so thread_ts = own ts is the normal shape.
- **A8 · known base-data areas (not Snowflake/Confluence; `/prompt` decides dependence):** Linear comments touch SC-15 (ZOM-521/526), SC-38 (ZOM-552) and SC-16 (e.g. ZOM-565 "can close" while Todo). No Snowflake or Confluence record is built on.
- **A9 · build named loosely (5):** "the current prod build" names neither a version nor a platform; consistent data, strength of the evidence is a `/prompt` question.
- **A10 · new rules in a DM (2, new):** statement 2 adds scope rules (which push rows to drop, that copy without a game name may go out, that Zombie Lane is off the calendar) in a DM reply rather than the brief. This is consistent data; whether the Agent finds it and whether it settles the push-copy rule cleanly is a `/prompt` question.

## 8. Limits

- Outside the static scope: live execution, deploy-time schema compatibility (A1), search ranking, Agent visibility and task difficulty.
- No required static check is unresolved.

## 9. Stage dependencies (for reuse)

SQL SHA `3afbf7cb…dd63`; universe manifest `da2f4cf0…a1a`; schema `31dcb2b4…151`; id_contracts `fc4711ef…82`; clock 2025-10-01T07:00Z; lint injection-lint-v1. New facts this run: `097c95c6…` absent from all base Slack messages (complete scan); D05SD5QLG94 members include EMPLOYEE_0005 and EMPLOYEE_0008; base sheet "Push Notifications Zombie Match" `/sheets_spreadsheets/220/sheets/1` "PNs Beta" rows 1–14 (Hourly Coins 2, Nathan's Treasure Hunt 8, Plague Race 9, Streak Fever 10, Axe Arena 11, Login Calendar 12, Season Pass 13, Weekly Leaderboard 14), with a near-copy for Domino Adventure at `/sheets_spreadsheets/73/sheets/1`; Plague Race/Endless on prod per #zombie-bugs 2025-08 /805 and 2025-09 /879, Season Pass prod test per #zombie-ops 2025-09 /21; iOS 0.3.49 released Sep 29 (#zombie-match3d 2025-09 /463), Android 0.3.127 required Sep 23 (/407); ZOM-543 base updated_at 2025-09-25T17:44:22Z, ZOM-565 2025-09-25T13:46:04Z; doc heading offsets as in statement 26. Reused facts (previous report SHA `dad52a1a…f3db`) for byte-identical statements. `/prompt` may rely on this stage for this SQL hash.

## 10. Next action

Proceed to `/prompt`. Because the SQL changed, any earlier `/prompt`, `/hardness`, `/oe` and `/rubric` result is outdated: run them again in that order.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt

Evidence limits: Static scope only; live deploy compatibility unverified (bundled schema snapshot lacks several columns used, advisory A1).
