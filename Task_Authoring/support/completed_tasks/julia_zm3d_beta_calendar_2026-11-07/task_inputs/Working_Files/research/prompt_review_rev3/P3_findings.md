# Deep Recheck P3 · Truthfulness and today's date

Pass: P3 (`Evals/references/rules/deep_recheck.md` § P3; `common_errors.md` § 3 tight claims, § 3 SQL line, § 6.4, § 6.8). Run blind: no other reviewer's findings, scores or verdict were seen.
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). "Today" is Wed Oct 1, 2025 and "yesterday" is Tue Sep 30, 2025. Premises are checked against what exists by 2025-09-30 23:59:59 PT.
Inputs read in full: `00_Task_Assigned_Inputs.md` (platform block), `02_Universe_Date.txt`, `04_Prompt.txt` (6 sentences), `01_Universe_Inject.sql` (276 lines, 112 statements: 78 INSERT, 34 UPDATE; never executed).

## Findings

`none`. Sentences checked: 6 of 6. Tight claims checked: 14. SQL statements checked: 112.

- Truthfulness: no finding.
- Today's date / clock (including departed-person and post-clock premises): no finding.
- Injection SQL checks for P3 (ids, columns, channel authors, apostrophes, thread dates): no finding.

## Premise checks (all CONFIRMED)

Format: `PC# | P3 | checklist section | prompt quote | record, locator, quoted value | dimension | result`

**S1 · "Frederick messaged me yesterday asking for the live-ops and push calendar for the Zombie Match 3D beta, the four buy weeks that start Monday the 6th."**

- PC1 | P3 | §3 tight claims (person) / departed-person | "Frederick" | `Evals/references/persona/roster.json`: `frederick_stone`, "Frederick Stone", role "Co-founder", department "Executive". `slack/users.json`: `EMPLOYEE_0008_SLACK_ID`, name "Frederick Stone", `deleted: false`. `linear/data.json` `/users/1`: `usr_175c0d7bc72ed244`, "frederick.stone@harmonygames.co", `is_active: true`. His latest base Slack message (non-injected) is at 2025-09-30T21:26:25Z, so he has not left (he is not Victor Barnes, who left in April 2025). | Truthfulness | CONFIRMED
- PC2 | P3 | §3 tight claims (channel) | "messaged me" | `slack/channels.json` `D05SD5QLG94`: `is_im: true`, members include `EMPLOYEE_0005_SLACK_ID` (Julia Lawson) and `EMPLOYEE_0008_SLACK_ID` (Frederick Stone). The base history of this channel has 126 messages by Julia and 111 by Frederick. The SQL (line 11) inserts message `8b090dec472117f4598b9ad84318272e` in `D05SD5QLG94`, by `user_id` `EMPLOYEE_0008_SLACK_ID`. | Truthfulness | CONFIRMED
- PC3 | P3 | §6.8 clock ("yesterday") | "yesterday" | SQL line 11: ts `1759263600.418207` / `created_at` "2025-09-30T20:20:00.418207Z" = Tue 2025-09-30 13:20 PDT. The follow-up reply on line 13 (`097c95c6e043ada8294b60f13e1656ba`, ts `1759263878.305127`) is Tue 2025-09-30 13:24 PDT. Both fall on the day before the Wed Oct 1 clock, and both are before 2025-09-30 23:59:59 PT. | Today's date | CONFIRMED
- PC4 | P3 | §3 tight claims (what was asked) | "asking for the live-ops and push calendar" | SQL line 11 text: "Julia, I need the live-ops and push calendar for the beta buy we start Mon Oct 6 through Sun Nov 2." | Truthfulness | CONFIRMED
- PC5 | P3 | §3 tight claims (product) | "the Zombie Match 3D beta" | `linear/data.json` ZOM-78, title "Event Calendar For Zombie Match 3D". The brief (SQL line 94) is titled "ZM3D beta live-ops calendar - working rules". UA plan slide 0 (SQL line 117): "Scaled beta-cohort buy, starting once the stores approve the Sep 30 builds." | Truthfulness | CONFIRMED
- PC6 | P3 | §3 tight claims (date/period) / §6.8 | "the four buy weeks that start Monday the 6th" | SQL line 11: "the beta buy we start Mon Oct 6 through Sun Nov 2". Brief (SQL line 98): "The calendar covers Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC, the four buy weeks in my UA plan." UA plan slide 1 (SQL line 121, `el_5e83a1f4c092`): "The four buy weeks / W1 Mon Oct 6 - Sun Oct 12 / W2 Mon Oct 13 - Sun Oct 19 / W3 Mon Oct 20 - Sun Oct 26 / W4 Mon Oct 27 - Sun Nov 2". Computed: 2025-10-06 is a Monday, it is the next Monday after Wed Oct 1, and there are 4 weeks through Sun 2025-11-02. This is a future start, so it is not treated as done. | Truthfulness / Today's date | CONFIRMED

**S2 · "Can you take it on for me?"** No factual premise. Checked; nothing to verify.

**S3 · "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me."**

- PC7 | P3 | §3 tight claims | "What he wants in it is in his message" | SQL line 11 lists the contents: "Every beat players can see in those weeks: which windows it runs in, if anything is held and until when, the push that goes with it, what still has to land before it runs and who owns that, and your recommendation with the trade-offs." | Truthfulness | CONFIRMED
- PC8 | P3 | §3 tight claims (document, sharing, date) | "his working rules for building it are in the brief he shared with me" | SQL lines 93–94: `gdrive.drive_files` / `gdocs.docs_documents` `f_7c3e91a4d2b85f60e1a9c4`, "ZM3D beta live-ops calendar - working rules". Owner `frederick.stone@harmonygames.co`; `shared_with_emails_json` `["julia.lawson@harmonygames.co"]`, role "reader"; created "2025-09-24 10:15:00+00". Body: "How I want the beta calendar built for the four buy weeks. The rules stay here; the calls are yours." SQL line 11 (Frederick): "The working rules for it are in my brief, shared with you." The reply on line 13 adds push rules ("Two things the brief does not spell out"). That does not make the prompt's claim false, because the prompt mirrors Frederick's own wording and the reply is part of "his message" thread. | Truthfulness | CONFIRMED

**S4 · "It goes in my live-ops calendar sheet."**

- PC9 | P3 | §3 tight claims (file, owner) | "my live-ops calendar sheet" | SQL lines 131–134: `f_e4a17c90b3d25f6a8c1d73`, "ZM3D Beta Live-Ops Calendar.xlsx" (spreadsheet title "ZM3D Beta Live-Ops Calendar"). Owner `julia.lawson@harmonygames.co`; parent `d_5f2c8e1b7a94d03c6e2b58`, "ZM Live Ops" (SQL line 91, owner Julia), whose parent `d_8140f09bf9f1b94cb8ee2d` is Julia's root folder (`gdrive/data.json` `/drive_files/11673`, name "julia.lawson@harmonygames.co"). Created "2025-09-30 06:35:00+00" = Sep 29 23:35 PDT, before the clock. Tabs "Calendar" and "Pushes" have header rows only. SQL line 11: "Put it in the calendar sheet in your ZM Live Ops folder". Base check: Julia owns no other calendar or live-ops sheet; her only matching file is "[LiveOps] Event Icon Management System.docx", a document. | Truthfulness | CONFIRMED

**S5 · "If a beat ends up held, leave a note on its ticket so the owner picks it up."**

- PC10 | P3 | §3 tight claims (ticket) / departed-person ("the owner picks it up") | "its ticket … the owner" | The hold candidate in the records is the weekly leaderboard. SQL line 19 (`fa3eee2c614b0741aeb240275f86abf7`, `C0880U9751A` #zombie-match3d, `EMPLOYEE_0012_SLACK_ID` Vincent Parker, 2025-09-30T20:50:12Z): "Re-tested the weekly leaderboard on the current prod build: it still does not start a new week. I killed the app and reopened it twice". Its ticket exists: `linear/data.json` ZOM-429, "Leaderboard next session doesn't start without killing the app", state "Backlog", `assignee_id` `usr_cd7849ec043ab3da` = "douglas@harmonygames.co" (`is_active: true`; roster `douglas`, "Software Engineer"; latest base Slack message from `EMPLOYEE_0031_SLACK_ID` Douglas at 2025-09-30T23:56:14Z). The owner is a current employee, not a departed one. The brief's other hold route ("An unresolved change-request review blocker on an in-scope live-ops PR from that cohort") gives no further held beat that might lack a ticket. `github/data.json` `/reviews` has exactly one `CHANGES_REQUESTED` review on match3d: `harmonygames-Games/match3d#303#rev_6`, submitted 2025-07-16, on a PR created 2025-07-15, which is outside the Aug–Sep cohort. The premise holds. Which beats are held is a Unique Ground Truth (P1) question, not a Truthfulness one. | Truthfulness | CONFIRMED

**S6 · "Once the sheet's done, link it on the calendar ticket and send Frederick the recommendation he asked for."**

- PC11 | P3 | §3 tight claims (ticket) | "the calendar ticket" | `linear/data.json` ZOM-78: "Event Calendar For Zombie Match 3D", state "Backlog", not archived, not canceled, assignee douglas, creator Julia (`usr_8140f09bf9f1b94c`). SQL line 222, `cmt_zom78_1`, by `usr_175c0d7bc72ed244` (Frederick), 2025-09-30T18:15:00Z: "Let us use this ticket for the ZM3D beta live-ops calendar instead of opening a new one. Link the sheet here when it is ready." SQL line 11: "link it on the calendar ticket". | Truthfulness | CONFIRMED
- PC12 | P3 | §3 tight claims | "send Frederick the recommendation he asked for" | SQL line 11: "your recommendation with the trade-offs … and send me the recommendation back here … I need your call, not a list of what we have." | Truthfulness | CONFIRMED
- PC13 | P3 | departed-person | "send Frederick" | Same records as PC1: Frederick is current and active on Sep 30, 2025. | Today's date (departed person) | CONFIRMED

**Whole prompt · clock (§6.8, deep_recheck P3 "nothing first appearing after 2025-09-30 23:59:59 PT")**

- PC14 | P3 | §6.8 clock | Everything the prompt treats as done: the message (S1), the shared brief (S3), the existing sheet (S4) and the calendar ticket (S6) | Every injected timestamp is on or before 2025-09-30T22:10:00Z (Sep 30 15:10 PDT). That latest one is SQL line 17, `58d06bd55ea4129eaadb726291967d5a`. The highest Slack ts is `1759270200.638114`, and the Gmail `internal_date` values are 2025-09-22T09:12Z and 2025-09-26T07:40Z. The only timestamps after the clock are the start and end of the scheduled release event (SQL lines 83–89, "2025-10-08 15:00:00+00" to "16:00:00+00"; created 2025-09-24T13:05Z, updated 2025-09-26T11:20Z). That is a future event, which is allowed, and the prompt does not treat it as done. The base records the premises rely on (ZOM-78 created 2025-04-26; ZOM-429 created 2025-07-22; Frederick's DM channel) all predate the clock. The synth-cut task has no shutdown premise. | Today's date | CONFIRMED

## Injection SQL checks (deep_recheck P3; common_errors § 3 SQL line, § 6.8 Injection)

- **IDs do not collide (no finding).**
  - Slack: the 10 injected message ids, and their (channel, ts) pairs, were checked against 610,468 base messages in 4,840 `messages/*/*.json` files. 0 collisions.
  - Gmail: thread ids `…/1844470925517303296` and `…/1844835127305531392`, and Message-IDs `<CAH4q9Zb2fK7xQe1M8sPnL3vT6wR0yDc@mail.gmail.com>` and `<CAH4q9Zc8uV1nE5kJ2mRtP7aW3xQ9bLs@mail.gmail.com>`, were checked against 81,404 threads and 95,164 messages. 0 collisions.
  - GCal: the 4 `event_id` values and the `ical_uid` were checked against 10,395 events. 0 collisions.
  - Drive, Docs, Slides and Sheets: the 4 Drive ids were checked against 53,631 `drive_files`, plus the `docs_documents`, `slides_presentations` and `sheets_spreadsheets` ids and the slide and element object ids. 0 collisions. The two referenced parents both exist: `d_8140f09bf9f1b94cb8ee2d` (Julia's root folder) and `d_175c0d7bc72ed244b944cb` (Frederick's root folder).
  - GitHub: reviews (3 checked against 2,230), review comments (3 against 1,387), PR comments (2 against 687) and timeline events (5 against 11,406). 0 collisions. All 5 PRs that are updated (#370, #438, #454, #470, #471) exist.
  - Linear: the base `/comments` array is empty and issues have no nested comments, so the 23 `cmt_zom*` ids cannot collide. All 22 updated issues exist, and all 10 comment authors exist in `/users`.
  - Trello: action `68dac8204f1e9a3b7c2d5e61` was checked against 595 actions. 0 collisions. The card `6851a724601a61857a1b202f` exists.
  - Every check that used `hg.py records` reported `scan_complete: true`.
- **Columns exist (no finding).**
  - All 112 statements parse, and every INSERT has as many values as columns.
  - Every column, and every UPDATE SET and WHERE column, exists in `Task_Authoring/references/universe_schema_live.json` (`runtime_verified: true`, exported 2026-10-31, universe hg4-synth-sep30cut v16).
  - Advisory only: 13 of those columns are missing from the older Evals snapshot `Evals/references/schema/injection.json`, which its README calls "unverified against the backing database". They are `gcal_events.extras_json`, `drive_files.drive_id`, `github_review_comments.pull_request_review_id/side/start_line/start_side/subject_type/seq`, `github_reviews.seq`, `slides_page_elements.table_json/ordinal`, `slides_pages.notes` and `linear_comments.sequence`.
- **Each added message's author is in its channel (no finding).** Each injected author is listed in the `slack/channels.json` members of the channel it posts to, and none has a `channel_leave` event there:
  - `EMPLOYEE_0008_SLACK_ID` → `D05SD5QLG94`
  - `EMPLOYEE_0016_SLACK_ID` → `C08R8CHB0QL` #zombie-art (`channel_join` 1746550152)
  - `EMPLOYEE_0016_SLACK_ID` → `D05GU6L0XFH`
  - `EMPLOYEE_0012_SLACK_ID` → `C0880U9751A` #zombie-match3d (`channel_join` 1736646994)
  - `SLACK_BOT_0004_SLACK_ID` → `C093LEZGF6J` #zombie-prs
- **Apostrophes doubled (no finding).** The only apostrophe inside a quoted string is "Nathan''s" on line 13, and it is doubled. The quotes balance across the whole file, and there are no curly or unescaped apostrophes.
- **Thread dates (no finding).**
  - Every injected Slack reply is later than its parent and later than the parent's latest base reply. The `reply_count` updates add exactly 1: c2b9c903 16→17, d648cbe9 2→3, 2f138acf 78→79, ef414467 3→4, da3fe08c 7→8, and 9025d428 and c5431028 0→1. The `latest_reply` values move forward.
  - No injected `updated_at` or `dateLastActivity` moves a base value backwards.
  - Every Linear comment is later than its issue's `created_at` (ZOM-566 was created 16:26:02Z and its comment is at 19:40Z).
  - The Gmail correction (Sep 26) comes after the original (Sep 22).
  - Every weekday label in the injected text matches its date: Mon Oct 6, Sun Oct 12, Mon Oct 13, Sun Oct 19, Mon Oct 20, Sun Oct 26, Mon Oct 27, Wed Oct 29, Fri Oct 31, Sat Nov 1, Sun Nov 2, Mon Sep 22, Fri Sep 26.

## Summary

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P3 | 6 prompt sentences (14 tight claims and clock premises); 112 SQL statements | 0 | 0 |

Truthfulness: no finding. Today's date / clock (including departed-person premises): no finding. Platform defects: none.
