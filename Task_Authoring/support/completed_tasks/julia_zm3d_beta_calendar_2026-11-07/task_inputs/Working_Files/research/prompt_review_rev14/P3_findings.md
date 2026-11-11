# P3 findings: Truthfulness and Today's date

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Pass P3, blind. This report stands alone for SQL sha256 edae63f3e83852f212c19892a9c9cf7304404b80db3178f92a470f301a598e13 (hash checked, read, never run). R14 = /private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review_rev14. Prompt: R14/inputs/04_Prompt.txt. SQL: R14/inputs/01_Universe_Inject.sql. "L" is a line in that SQL. Paths without a prefix sit under Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/. Base records were reopened for this run.

## Result

**Findings: none. Sentences checked: 6 of 6. Premises confirmed: 16 of 16.**

- Truthfulness: no finding.
- Today's date (clock, "yesterday", "Monday the 6th", nothing after the clock): no finding.
- Departed-person premises: no finding.
- Injection SQL hygiene (ids, columns, message authors, apostrophes): no finding. Advisories A1 and A2 below.
- PLATFORM tags: none.

The prompt names no channel, vendor, amount, ticket id or fiscal period. Its tight claims are one person (Frederick), two dates ("yesterday", "Monday the 6th") and one count ("four buy weeks").

## Change from rev13

Confirmed by my own diff against R14/prev/01_Universe_Inject.rev13.sql (sha256 1f2175a297fd390960f22c3767f790fc980a881023affa6ece970745fb40289b): exactly 1 of 111 statements differs, the gdocs brief row. The prompt is byte-identical. Dates on the row are unchanged. All 9 style runs recomputed, and each lands exactly on its heading.

- L113 adds: "Endless goes down as its weekly windows, with the daily reset noted." This cites nothing newer than the brief's Sep 24 date. `match3d-backend` zombies-game-cdk-stack.ts has `ENDLESS_MONSTER_DAILY_SCHEDULE` ("PROD: every day at 00:00 AM UTC") and `ENDLESS_MONSTER_WEEKLY_SCHEDULE` ("PROD: every monday at 00:00 AM UTC"), the weekly one first committed in c04e168 on 2025-07-11. #zombie-bugs 2025-08-07T10:11Z Vincent also says "the daily reset".
- L127 now reads: "moves to any time before it and you tell its owner in a reply on the mail where they committed to it." No date in it, and no prompt premise rests on it.

These edits touch T7 and T10 by sitting in the same row. Neither quoted sentence changed.

## Premise table

| # | Prompt quote | Records (locator and quoted value) | Section | Dimension | Status |
|---|---|---|---|---|---|
| T1 | "Frederick" | `slack/users.json` EMPLOYEE_0008_SLACK_ID name "Frederick Stone", deleted false. `contacts/contacts.json` holds one Frederick: frederick.stone@harmonygames.co, "Commercial Lead, Marketing & Business Development". Roster: frederick_stone, Co-founder. | 3 tight claims | Truthfulness | Confirmed |
| T2 | "Frederick" is still at the company | #executives 2025-09-30T21:26Z: "can you clarify? Fine at current pace, or fine to juice bids yet again?". 173 Slack messages in Sep 2025. Aug-Sep Slack search for "last day", "resign", "laid off", "let go", "offboard", "on leave" returned no line naming him. | 6.8 | Truthfulness (departed person) | Confirmed |
| T3 | "messaged me" | L11 slack.slack_messages id bca784379e7dbca9e64e79a64dfefbba, channel D05SD5QLG94, user EMPLOYEE_0008_SLACK_ID. `slack/channels.json` D05SD5QLG94: is_im true, members include EMPLOYEE_0005_SLACK_ID (Julia Lawson) and EMPLOYEE_0008_SLACK_ID. `slack/messages/D05SD5QLG94/` holds 126 Julia and 111 Frederick messages. | 3 tight claims | Truthfulness | Confirmed |
| T4 | "yesterday" | L11 ts 1759263617.418209, created_at "2025-09-30T20:20:17.418209Z" = Tue Sep 30 13:20 PT. Reply L13 id 890dc27f56e8501bd7590ffdfc231057, "2025-09-30T20:24:38.305129Z". ts and created_at agree on all 12 injected Slack rows. | 6.8 clock | Today's date | Confirmed |
| T5 | "asking for the live-ops and push calendar" | L11: "Julia, I need the live-ops and push calendar for the beta buy we start Mon Oct 6 through Sun Nov 2." | 3 tight claims | Truthfulness | Confirmed |
| T6 | "the Zombie Match 3D beta" | `linear/data.json` team_ZOM name "Zombie Match 3D". #company-internal 2025-09-12T19:11Z Leonard: "We finalized the dev pipeline for the beta." #company-internal 2025-09-22T16:22Z Brian: "We’ve decided to postpone Axe Arena for the beta release". L109 brief title: "ZM3D beta live-ops calendar - working rules". Frederick's message says only "the beta buy"; the brief supplies the game. The prompt gives no beta date, so SC-13 does not touch it. L259 carries list name "BETA: Sep 30", matching the last rename on 2025-09-12T16:42:21Z. | 3 tight claims | Truthfulness | Confirmed |
| T7 | "the four buy weeks" | L113: "The calendar covers Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC, the four buy weeks in my UA plan." L136-140 deck `f_2b9d4e7a1c63f08d5e7b21` slide 2: "The four buy weeks / W1 Mon Oct 6 - Sun Oct 12 / W2 Mon Oct 13 - Sun Oct 19 / W3 Mon Oct 20 - Sun Oct 26 / W4 Mon Oct 27 - Sun Nov 2". Span is 28 days. | 3 tight claims | Truthfulness | Confirmed |
| T8 | "that start Monday the 6th" | Oct 6, 2025 is a Monday (computed). L11 "we start Mon Oct 6". A future date stated as a plan, so it may stand on an Oct 1 clock. Checked against it, none contradicts: #zombie-match3d 2025-09-30T16:04Z Frederick: "We are only running the retention campaigns." L134 deck: "Beta-cohort buy, starting once the stores approve the Sep 30 builds." Those builds exist: #builds 2025-09-30T19:15Z "Match 3D iOS Submission - #50 - main Success", 20:13Z "Match3D Android Submission - #135 - main  Success", and match3d commit 3f5352a5b5 has tags TestFlight_iOS_50 and Submission_Android_135. D04UP2L3E3S 2025-09-25T05:15Z Leonard: "We can barely get the beta out by mid october": an earlier opinion in a DM Julia is not in, and it sets no buy date. | 6.8 clock | Today's date | Confirmed |
| T9 | "What he wants in it is in his message" | L11: "Every beat players can see in those weeks: which windows it runs in, if anything is held and until when, the push that goes with it, what still has to land before it runs and who owns that." L13 adds "Two things on top of the brief." in the same thread (thread_parent_id bca784379e7dbca9e64e79a64dfefbba), so "his message" is not false. | 3 tight claims | Truthfulness | Confirmed |
| T10 | "his working rules for building it are in the brief" | L109-127 gdocs.docs_documents `f_7c3e91a4d2b85f60e1a9c4`, title "ZM3D beta live-ops calendar - working rules", L110-111: "Frederick, Sep 24 / How I want the beta calendar built for the four buy weeks." L11: "The working rules for the calendar are in my brief, shared with you." | 3 tight claims | Truthfulness | Confirmed |
| T11 | "he shared with me" | L108 gdrive.drive_files `f_7c3e91a4d2b85f60e1a9c4`: owner frederick.stone@harmonygames.co, shared_with_emails_json ["julia.lawson@harmonygames.co"], role reader, created 2025-09-24 17:15:22+00. Parent `d_175c0d7bc72ed244b944cb` is Frederick's root in `gdrive/data.json`. | 3 tight claims | Truthfulness | Confirmed |
| T12 | "my live-ops calendar sheet" | L146-147 `f_e4a17c90b3d25f6a8c1d73`: "ZM3D Beta Live-Ops Calendar.xlsx", owner julia.lawson@harmonygames.co. L106 folder `d_5f2c8e1b7a94d03c6e2b58` "ZM Live Ops", owner Julia, under `d_8140f09bf9f1b94cb8ee2d` (Julia's root). L11: "Put it in the calendar sheet in your ZM Live Ops folder". Julia owns no other calendar or live-ops spreadsheet in base. | 3 tight claims | Truthfulness | Confirmed |
| T13 | "its ticket" (a held beat has a ticket) | `linear/data.json` ZOM-429: "Leaderboard next session doesn't start without killing the app", state Backlog. L19 Vincent, #zombie-match3d 2025-09-30T20:50:12Z: "Re-tested the weekly leaderboard on the current prod build: it still does not start a new week." Which beats are held is P1's question; this entry only shows the premise can be true. | 3 tight claims | Truthfulness | Confirmed |
| T14 | "so the owner picks it up" | ZOM-429 assignee douglas@harmonygames.co, is_active true, last Slack post 2025-09-30T23:56Z, 509 messages in Sep 2025. No SQL statement sets assignee_id. All open ZOM assignees are active in Sep 2025; none is Victor Barnes. The 7 unassigned open tickets (ZOM-65, 66, 69, 70, 237, 348, 526) are not the ticket of a held beat: ZOM-526 is polish per L190 ("it does not have to land before the beta"), and ZOM-348 is the rotating shop, "not a beat" per L115. | 6.8, P3 departed person | Truthfulness (departed person) | Confirmed |
| T15 | "the calendar ticket" | `linear/data.json` ZOM-78: "Event Calendar For Zombie Match 3D", state Backlog, creator Julia, assignee Douglas, created 2025-04-26. The only ZOM ticket with "calendar" in title or description. L205 cmt_zom78_1, author Frederick, 2025-09-30T18:15:14Z: "Let us use this ticket for the ZM3D beta live-ops calendar instead of opening a new one. Link the sheet here when it is ready." | 3 tight claims | Truthfulness | Confirmed |
| T16 | "the recommendation he asked for" | L11: "Then send me your recommendation back here, with the trade-offs, on what we run and what we hold in those weeks." | 3 tight claims | Truthfulness | Confirmed |

"Can you take it on for me?" and "Once the sheet's done" state no fact.

## Clock sweep

- Everything the prompt treats as done is before the clock: the brief share (Sep 24), the ticket comment (Sep 30 18:15Z), the message (Sep 30 20:20Z), the thread reply (Sep 30 20:24Z).
- Latest dated row that is not a future event: 2025-09-30T22:10:41Z (L17). The only dates after the clock are the Oct 8 GCal release (L98-104), a future deadline, which is allowed.
- All 32 injected Linear comments sit after their issue's created_at and before the clock, in sequence order per issue.
- Latest Slack record in the base is 2025-10-01T05:51Z (Sep 30 22:51 PT).
- Shutdown rule: not applicable on an Oct 1 task.

## Departed-person sweep

- Every person the SQL names or uses as an author has a Sep 2025 Slack post: Frederick, Robert, Leonard, Vincent, Brian, Oliver, Calvin, Owen, Marcus, Samuel, Claire, Martin, Arthur, Douglas.
- "victor" as a name appears 0 times in the SQL. Felix, Lauren and Thomas also 0. Victor Barnes has no Slack post since Jun 2025 and no open ZOM ticket.

## Injection SQL hygiene

- Parse: 111 statements (81 INSERT, 30 UPDATE), no unterminated quote, equal column and value counts on every INSERT. Wrapper lint on this hash: FAIL 0, CHECK 0, INFO 0.
- Apostrophes: all doubled ("Nathan''s", "Martin''s", "teams''").
- Ids: 73 primary ids, no duplicate in the SQL, no collision with base. Slack ids and ts, Gmail tokens (0 hits under `gmail/threads`), GCal events and ical uid, Drive files, GitHub review comments, review and timeline event, and the Trello action were all rechecked. The base Linear comments array is empty.
- Update targets: all 8 Slack parents and the Trello card exist in base; ZOM issues exist. Review parents `#470#rev_9` and `#472#rev_1` exist in base; `#468#rev_3` is inserted by the SQL.
- Message authors: all 12 are in their channel's members list, with no leave event for those authors in the channels checked. Every thread reply sits in its parent's channel and after it.
- Live schema: 0 missing columns, 0 NOT NULL problems on every injected table.

**A1 (advisory).** 13 columns across 7 tables are absent from `Evals/references/schema/injection.json` and present in `Task_Authoring/references/universe_schema_live.json`: gcal_events.extras_json; drive_files.drive_id; slides_pages.notes; slides_page_elements.table_json and ordinal; github_review_comments.pull_request_review_id, side, start_line, start_side, subject_type and seq; github_reviews.seq; linear_comments.sequence. `Evals/references/schema/README.md` treats that as provisional, not a defect.

**A2 (advisory, outside P3).** L35 sits in #zm-collect-win (SC-57): is_archived true, is_private false, Julia not in members. Its date is consistent, since people posted there through Sep 30. Whether she can read it is P2's call.

## Limits

- Scope is P3 only. Which beats are held, and whether each rule resolves to one answer, was not judged here.
- No live tool was run. Persona visibility rests on `Evals/references/persona/acl.md`.
- R14/out and R14/work hold other reviewers' files. I did not open them; my helpers are in R14/work/p3_rev14.
