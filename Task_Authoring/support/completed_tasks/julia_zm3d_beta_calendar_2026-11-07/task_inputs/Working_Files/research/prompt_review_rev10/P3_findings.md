# P3 findings: Truthfulness and Today's date

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Pass P3, blind. Prompt: R/inputs/04_Prompt.txt. SQL: R/inputs/01_Universe_Inject.sql (sha256 ffbac4586fb91842ca16263c2b76987c26623c7ed689e00d33886c63f9331bdc, read, never run). "SQL Ln" is a line in that file. Paths without a prefix sit under Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/.

## Result

**Findings: none. Sentences checked: 6 of 6. Premises checked: 16.**

- Truthfulness: no finding.
- Today's date (clock, "yesterday", "Monday the 6th", nothing after the clock): no finding.
- Departed-person premises: no finding.
- Injection SQL hygiene (ids, columns, message authors, apostrophes): no finding. One advisory, A1 below.
- PLATFORM tags: none.

The prompt names no channel, vendor, amount, ticket id or fiscal period. Its tight claims are one person (Frederick), two dates ("yesterday", "Monday the 6th") and one count ("four buy weeks").

## Premise table

Each entry: prompt quote | records and quoted text | section | dimension | status.

| # | Prompt quote | Records (locator and quoted value) | Section | Dimension | Status |
|---|---|---|---|---|---|
| T1 | "Frederick" | `slack/users.json` EMPLOYEE_0008_SLACK_ID name "Frederick Stone", deleted false. `contacts/contacts.json` is the only Frederick: frederick.stone@harmonygames.co, "Commercial Lead, Marketing & Business Development". Roster: frederick_stone, Co-founder. | 3 tight claims | Truthfulness | Confirmed |
| T2 | "Frederick" is still at the company | Latest base post 2025-09-30T21:26Z, #executives: "can you clarify? Fine at current pace, or fine to juice bids yet again?". 173 Slack messages in Sep 2025. Search of Aug-Sep Slack for "last day", "resign", "laid off", "let go", "offboard", "on leave" returned no departure for him. | 6.8 | Truthfulness (departed person) | Confirmed |
| T3 | "messaged me" | SQL L11, slack.slack_messages id bca784379e7dbca9e64e79a64dfefbba, channel D05SD5QLG94, user EMPLOYEE_0008_SLACK_ID. `slack/channels.json` D05SD5QLG94: is_im true, members include EMPLOYEE_0005_SLACK_ID (Julia Lawson) and EMPLOYEE_0008_SLACK_ID. `slack/messages/D05SD5QLG94/` holds 126 Julia and 111 Frederick messages, so it is their DM. | 3 tight claims | Truthfulness | Confirmed |
| T4 | "yesterday" | SQL L11 ts 1759263617.418209, created_at "2025-09-30T20:20:17.418209Z" = Tue Sep 30 13:20 PT. Reply SQL L13 id 890dc27f56e8501bd7590ffdfc231057, created_at "2025-09-30T20:24:38.305129Z". ts and created_at agree on all 11 injected Slack rows. | 6.8 clock | Today's date | Confirmed |
| T5 | "asking for the live-ops and push calendar" | SQL L11: "Julia, I need the live-ops and push calendar for the beta buy we start Mon Oct 6 through Sun Nov 2." | 3 tight claims | Truthfulness | Confirmed |
| T6 | "the Zombie Match 3D beta" | `linear/data.json` /teams team_ZOM name "Zombie Match 3D". Slack #company-internal 2025-09-12T19:11Z Leonard: "We finalized the dev pipeline for the beta." Slack #company-internal 2025-09-22T16:22Z Brian: "We’ve decided to postpone Axe Arena for the beta release" SQL L105 brief title: "ZM3D beta live-ops calendar - working rules". Frederick's message says only "the beta buy"; the brief supplies the game. The prompt gives no beta launch date, so SC-13 (Trello list "BETA: Oct 10" vs "BETA: Sep 30") does not touch it. | 3 tight claims | Truthfulness | Confirmed |
| T7 | "the four buy weeks" | SQL L109 brief: "The calendar covers Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC, the four buy weeks in my UA plan." SQL L132-137 deck `f_2b9d4e7a1c63f08d5e7b21` slide 2: "The four buy weeks / W1 Mon Oct 6 - Sun Oct 12 / W2 Mon Oct 13 - Sun Oct 19 / W3 Mon Oct 20 - Sun Oct 26 / W4 Mon Oct 27 - Sun Nov 2". Span is 28 days. | 3 tight claims | Truthfulness | Confirmed |
| T8 | "that start Monday the 6th" | Oct 6, 2025 is a Monday (computed). SQL L11 "we start Mon Oct 6". It is a future date stated as a plan, so it may stand on a clock of Oct 1. Records checked against it, none contradicts: #zombie-match3d 2025-09-30T16:04Z Frederick: "We are only running the retention campaigns." (no buy running yet). Deck slide 1 (SQL L130): "starting once the stores approve the Sep 30 builds", and those builds exist: #builds 2025-09-30T19:15Z "Match 3D iOS Submission - #50 - main Success", 20:13Z "Match3D Android Submission - #135 - main  Success". DM D04UP2L3E3S 2025-09-25T05:15Z Leonard: "We can barely get the beta out by mid october": an earlier opinion in a DM Julia is not in, and it sets no buy date. | 6.8 clock | Today's date | Confirmed |
| T9 | "What he wants in it is in his message" | SQL L11: "Every beat players can see in those weeks: which windows it runs in, if anything is held and until when, the push that goes with it, what still has to land before it runs and who owns that." Thread reply SQL L13 adds "Two things the brief does not spell out." The reply sits in the same thread of the same DM (thread_parent_id bca784379e7dbca9e64e79a64dfefbba), so "his message" is not false. | 3 tight claims | Truthfulness | Confirmed |
| T10 | "his working rules for building it are in the brief" | SQL L105-123, gdocs.docs_documents `f_7c3e91a4d2b85f60e1a9c4`, title "ZM3D beta live-ops calendar - working rules", body "Frederick, Sep 24 / How I want the beta calendar built for the four buy weeks." SQL L11: "The working rules for the calendar are in my brief, shared with you." | 3 tight claims | Truthfulness | Confirmed |
| T11 | "he shared with me" | SQL L104 gdrive.drive_files `f_7c3e91a4d2b85f60e1a9c4`: owner frederick.stone@harmonygames.co, shared_with_emails_json ["julia.lawson@harmonygames.co"], role reader, created 2025-09-24 17:15:22+00, before the clock. Parent `d_175c0d7bc72ed244b944cb` is in `gdrive/data.json` as Frederick's root. | 3 tight claims | Truthfulness | Confirmed |
| T12 | "my live-ops calendar sheet" | SQL L142-143 `f_e4a17c90b3d25f6a8c1d73`: name "ZM3D Beta Live-Ops Calendar.xlsx", owner julia.lawson@harmonygames.co. Parent folder SQL L102 `d_5f2c8e1b7a94d03c6e2b58` "ZM Live Ops", owner Julia, under `d_8140f09bf9f1b94cb8ee2d` (Julia's root in `gdrive/data.json`). SQL L11: "Put it in the calendar sheet in your ZM Live Ops folder". Julia owns no other calendar or live-ops spreadsheet in base. | 3 tight claims | Truthfulness | Confirmed |
| T13 | "its ticket" (a held beat has a ticket) | `linear/data.json` ZOM-429: "Leaderboard next session doesn't start without killing the app", state Backlog. SQL L19 Vincent, #zombie-match3d 2025-09-30T20:50:12Z: "Re-tested the weekly leaderboard on the current prod build: it still does not start a new week." Which beats are held is P1's question; this entry only shows the premise can be true. | 3 tight claims | Truthfulness | Confirmed |
| T14 | "so the owner picks it up" | ZOM-429 assignee usr_cd7849ec043ab3da = douglas@harmonygames.co, is_active true. Douglas's last Slack post 2025-09-30T23:56Z; 509 messages in Sep 2025. Across all open ZOM tickets, assignees are all people active in Sep 2025, none is Victor Barnes or another leaver. The 7 unassigned open tickets (ZOM-65, 66, 69, 70, 237, 348, 526) are not the ticket of a held beat. ZOM-526 is polish per SQL L186: "it does not have to land before the beta". | 6.8, P3 departed person | Truthfulness (departed person) | Confirmed |
| T15 | "the calendar ticket" | `linear/data.json` ZOM-78: "Event Calendar For Zombie Match 3D", state Backlog, creator Julia, assignee Douglas, created 2025-04-26. It is the only ZOM ticket with "calendar" in title or description. SQL L201 cmt_zom78_1, author usr_175c0d7bc72ed244 (Frederick), 2025-09-30T18:15:14Z: "Let us use this ticket for the ZM3D beta live-ops calendar instead of opening a new one. Link the sheet here when it is ready." | 3 tight claims | Truthfulness | Confirmed |
| T16 | "the recommendation he asked for" | SQL L11: "Then send me your recommendation back here, with the trade-offs, on what we run and what we hold in those weeks." | 3 tight claims | Truthfulness | Confirmed |

"Can you take it on for me?" and "Once the sheet's done" state no fact.

## Clock sweep

- Everything the prompt treats as done is before the clock: the brief share (Sep 24), the ticket comment (Sep 30 18:15Z), the message (Sep 30 20:20Z), the thread reply (Sep 30 20:24Z).
- Latest dated row in the SQL that is not a future event: 2025-09-30T22:10:41Z (SQL L17). The only dates after the clock are the Oct 8 GCal release (SQL L94-100), a future deadline, which is allowed.
- All 30 injected Linear comments sit after their issue's created_at and before the clock.
- Weekdays in injected text all match: Mon Sep 22, Fri Sep 26, Mon Oct 6, Mon Oct 13, Wed Oct 29, Fri Oct 31, Sat Nov 1, Sun Nov 2, and all deck week bounds.
- Latest Slack record in the base is 2025-10-01T05:51Z (Sep 30 22:51 PT), so nothing Slack-based sits after the clock.
- Shutdown rule: not applicable on an Oct 1 task (`shutdown_rules_apply: false`).

## Departed-person sweep

- Every person the SQL names or uses as an author has a Sep 2025 Slack post: Frederick, Robert, Leonard, Vincent, Brian, Oliver, Calvin, Owen, Marcus, Samuel, Claire, Martin, Arthur, Douglas. Latest posts run from 2025-09-29 to 2025-10-01 UTC.
- Victor Barnes appears nowhere in the SQL. The single "victor" text match is "victory score" in cmt_zom542_1. He has no Slack post since Jun 2025 and no open ZOM ticket.

## Injection SQL hygiene

- Parse: 107 statements (78 INSERT, 29 UPDATE) tokenized with no unterminated quote. Every INSERT has equal column and value counts. The wrapper lint (`hg.py lint --sql`) returned FAIL 0, CHECK 0, INFO 0.
- Apostrophes: all doubled ("Nathan''s", "Martin''s", "Douglas''s", "teams''").
- Ids: no collision with base and no duplicate inside the SQL, across 70 primary ids. Covered: 11 Slack ids and ts, 12 Gmail thread and message ids (0 grep hits under `gmail/threads`), 4 GCal events and their ical uid, 4 Drive files with their Docs, Sheets and Slides ids, 3 GitHub review comments, 1 review, 1 timeline event, 1 Trello action. The base Linear comments array is empty, so the 30 Linear ids cannot collide.
- Update targets: all 7 Slack parents, the Trello card and the ZOM issues exist in base. Review parents `match3d#470#rev_9` and `#472#rev_1` exist in base; `#468#rev_3` is inserted by SQL L152.
- Message authors: all 11 are in their channel's members list. D05SD5QLG94 EMPLOYEE_0008; D05GU6L0XFH EMPLOYEE_0016; C08R8CHB0QL EMPLOYEE_0016; C0880U9751A EMPLOYEE_0012; C08R27X0EAH EMPLOYEE_0038 and EMPLOYEE_0012; C093LEZGF6J SLACK_BOT_0004. No channel_leave event for Vincent, Leonard or Robert in C0880U9751A, C08R27X0EAH or C08R8CHB0QL.
- Injected thread replies sit in the same channel as their parent and after it.

**A1 (advisory, not a finding).** 13 columns across 7 tables are absent from `Evals/references/schema/injection.json`: gcal_events.extras_json; drive_files.drive_id; slides_pages.notes; slides_page_elements.table_json and ordinal; github_review_comments.pull_request_review_id, side, start_line, start_side, subject_type and seq; github_reviews.seq; linear_comments.sequence. All of them exist in `Task_Authoring/references/universe_schema_live.json`, which reports 0 missing columns and 0 missing NOT NULL columns for every injected table. `Evals/references/schema/README.md` treats a snapshot-only mismatch as a provisional advisory, not a defect.

## Limits

- Scope is P3 only. Which beats are held, and whether each rule resolves to one answer, was not judged here.
- Persona-visible checks for premises rest on `Evals/references/persona/acl.md`; no live tool was run.
