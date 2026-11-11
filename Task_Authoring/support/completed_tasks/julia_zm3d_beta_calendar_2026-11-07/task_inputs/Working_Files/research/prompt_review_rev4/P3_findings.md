# Deep recheck P3: Truthfulness and Today's date (review_rev4)

Pass: **P3**. Blind to the main review and to the other passes.
Task date: Oct 1, 2025 (synth-cut). Clock: 2025-10-01 00:00 PT (07:00 UTC). In the persona's voice "today" is Wed Oct 1, 2025 and "yesterday" is Tue Sep 30. Each premise is checked against records that exist by 2025-09-30 23:59:59 PT.

Inputs read in full:
- `R/inputs/04_Prompt.txt` (6 sentences)
- the Platform assignment block in `R/inputs/00_Task_Assigned_Inputs.md` (Julia Lawson, Product Manager)
- `R/inputs/02_Universe_Date.txt` ("Oct 1, 2025 (synth-cut)")
- `R/inputs/01_Universe_Inject.sql`: 261 lines, 106 statements. I read all of it as a proposed overlay and never executed it.

Path abbreviations:
- `OS/` = `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/`
- `GH/` = `Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/`
- `SQL:Ln` = line n of `R/inputs/01_Universe_Inject.sql`

## Result

**Findings: none.** I checked 6 of 6 prompt sentences and 10 factual premises, plus a clock sweep and the four injection SQL checks.
- **Truthfulness: no finding.** Every person, channel/DM, ticket, document, sheet, date and span the prompt states matches a record the persona can open.
- **Today's date / clock: no finding.** Nothing the prompt treats as already done falls after 2025-09-30 23:59:59 PT.
- **Departed-person premise: no finding.** Frederick, the ticket owner and every person the injected records name were active up to the clock. Victor Barnes and Felix Young are not involved.

Platform defects: none.

## Sentences checked

- S1 "Frederick messaged me yesterday asking for the live-ops and push calendar for the Zombie Match 3D beta, the four buy weeks that start Monday the 6th."
- S2 "Can you take it on for me?" (no factual premise)
- S3 "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me."
- S4 "It goes in my live-ops calendar sheet."
- S5 "If a beat ends up held, leave a note on its ticket so the owner picks it up."
- S6 "Once the sheet's done, link it on the calendar ticket and send Frederick the recommendation he asked for."

## Premise checks (one entry per premise; none is a finding)

`PC# | pass | checklist section | quoted prompt text | record path, id and quoted value | Eval dimension | result`

- **PC1 | P3 | common_errors §3 Tight claims, §6.4; deep_recheck P3 departed-person | S1 "Frederick"** | Records:
  - `OS/slack/users.json` /6: id `EMPLOYEE_0008_SLACK_ID`, real_name "Frederick Stone", deleted false.
  - `OS/linear/data.json` /users/1: `usr_175c0d7bc72ed244`, "frederick.stone@harmonygames.co", is_active true.
  - `Evals/references/persona/roster.json`: frederick_stone, role "Co-founder".
  - Still active at the clock. `OS/slack/messages/C07C2866011/2025-09.json` /1194 (id a4119e077309f2749941920811bfaa04, ts 1759267585.969279 = 2025-09-30 21:26 UTC) by EMPLOYEE_0008: "can you clarify? Fine at current pace, or fine to juice bids yet again?"
  - He has 950 Slack posts from Jun to Oct 2025. A search of 2025 Slack for a departure mention ("last day", "leaving", "stepping down", "left the company") found none.
  - | Truthfulness (departed person) | **consistent: no finding**

- **PC2 | P3 | §6.8 Clock; §3 Tight claims | S1 "messaged me yesterday"** | Records:
  - SQL:L11: slack_messages `8b090dec472117f4598b9ad84318272e`, channel `D05SD5QLG94`, user EMPLOYEE_0008_SLACK_ID, ts 1759263600.418207, created_at "2025-09-30T20:20:00.418207Z", which is Tue Sep 30 13:20 PDT.
  - SQL:L13: thread reply `097c95c6e043ada8294b60f13e1656ba` by the same user at 2025-09-30T20:24:38Z (13:24 PDT).
  - `OS/slack/channels.json` /529: D05SD5QLG94 is_im true, members include "EMPLOYEE_0005_SLACK_ID" (Julia Lawson, users.json /3) and "EMPLOYEE_0008_SLACK_ID".
  - Both messages fall on Sep 30 in PT and in UTC, so "yesterday" holds.
  - | Today's date / Truthfulness | **consistent: no finding**

- **PC3 | P3 | §3 Tight claims | S1 "the live-ops and push calendar for the Zombie Match 3D beta"** | Records:
  - SQL:L11: "Julia, I need the live-ops and push calendar for the beta buy we start Mon Oct 6 through Sun Nov 2."
  - SQL:L93 brief title: "ZM3D beta live-ops calendar - working rules".
  - `OS/linear/data.json` /issues/3665 ZOM-78, title "Event Calendar For Zombie Match 3D" (the game's name).
  - | Truthfulness | **consistent: no finding**

- **PC4 | P3 | §3 Tight claims (date); §6.8 Clock | S1 "the four buy weeks that start Monday the 6th"** | Records:
  - SQL:L11: "start Mon Oct 6 through Sun Nov 2".
  - SQL:L120, gslides element `el_5e83a1f4c092` on slide `slide_b83e51a09d72` of "ZM3D beta UA plan": "The four buy weeks / W1 Mon Oct 6 - Sun Oct 12 / W2 Mon Oct 13 - Sun Oct 19 / W3 Mon Oct 20 - Sun Oct 26 / W4 Mon Oct 27 - Sun Nov 2".
  - SQL:L97, the brief: "Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC, the four buy weeks in my UA plan".
  - Date arithmetic: 2025-10-06 is a Monday. It is the first Monday after Wed Oct 1. Oct 6 to Nov 2 is 28 days, which is four Mon–Sun weeks. The weeks are in the future, and the prompt does not treat them as done.
  - Base context: Unity retention campaigns were already live on Sep 29–30. In `OS/slack/messages/C07C2866011/2025-09.json` (2025-09-29 22:28Z) EMPLOYEE_0038 writes "do you mind turning on iOS Unity retention campaigns?". This matches the UA plan slide (SQL:L128): "The small retention campaigns already running are a separate budget and are not part of these buys." No contradiction.
  - | Truthfulness / Today's date | **consistent: no finding**

- **PC5 | P3 | §3 Tight claims | S3 "What he wants in it is in his message"** | Records:
  - SQL:L11 is the parent DM. It covers windows, held/until, push, still-to-do and owner, the sheet, the ticket link and the recommendation.
  - SQL:L13 is Frederick's own thread reply on the same parent (thread_parent_id 8b090dec…). It covers push rows and the Zombie Lane exclusion.
  - Both are from the same author, in the same DM thread, on Sep 30.
  - | Truthfulness | **consistent: no finding**

- **PC6 | P3 | §3 Tight claims | S3 "his working rules for building it are in the brief he shared with me"** | Records:
  - SQL:L92: drive_files `f_7c3e91a4d2b85f60e1a9c4`, "ZM3D beta live-ops calendar - working rules.docx".
    - owner_email "frederick.stone@harmonygames.co"
    - shared_roles_json `[{"email":"julia.lawson@harmonygames.co","role":"reader"}]`
    - created 2025-09-24 10:15Z
  - Its parent `d_175c0d7bc72ed244b944cb` is `OS/gdrive/data.json` /drive_files/2060, Frederick's folder (owner frederick.stone@).
  - SQL:L93, gdocs body: "Frederick, Sep 24 / How I want the beta calendar built for the four buy weeks. The rules stay here; the calls are yours."
  - DM SQL:L11: "The working rules for the calendar are in my brief, shared with you."
  - | Truthfulness | **consistent: no finding**

- **PC7 | P3 | §3 Tight claims | S4 "It goes in my live-ops calendar sheet."** | Records:
  - SQL:L130–133: `f_e4a17c90b3d25f6a8c1d73`, "ZM3D Beta Live-Ops Calendar.xlsx".
    - owner_email "julia.lawson@harmonygames.co"
    - created 2025-09-30 06:35Z, which is before the clock
    - tabs "Calendar" and "Pushes" with header rows
  - Its parent `d_5f2c8e1b7a94d03c6e2b58` is "ZM Live Ops" (SQL:L90, owner julia.lawson@). That folder's parent `d_8140f09bf9f1b94cb8ee2d` is `OS/gdrive/data.json` /drive_files/11673, Julia's folder.
  - DM SQL:L11: "Put it in the calendar sheet in your ZM Live Ops folder".
  - | Truthfulness | **consistent: no finding**

- **PC8 | P3 | §3 Tight claims (ticket); deep_recheck P3 departed-person | S5 "leave a note on its ticket so the owner picks it up"** | Records:
  - The beat that can be held is the weekly leaderboard. SQL:L19 (Vincent Parker, `C0880U9751A` #zombie-match3d, 2025-09-30T20:50Z): "Re-tested the weekly leaderboard on the current prod build: it still does not start a new week. I killed the app and reopened it twice".
  - Its ticket exists: `OS/linear/data.json` /issues/3495 ZOM-429, "Leaderboard next session doesn't start without killing the app". Its assignee `usr_cd7849ec043ab3da` is /users/36 "douglas@harmonygames.co", is_active true. Douglas's last Slack post is 2025-09-30T23:56Z.
  - None of the open live-ops ZOM tickets is assigned to a departed person. /users/27 "usr_Victor Barnes" and /users/11 felix.young@ hold no open ZOM live-ops ticket.
  - `GH/data.json` reviews has no CHANGES_REQUESTED review dated 2025-08 or later, and the SQL adds only COMMENTED reviews. So no beat is held by a PR blocker that might lack a ticket.
  - | Truthfulness (ticket and owner exist; owner active) | **consistent: no finding**

- **PC9 | P3 | §3 Tight claims (ticket) | S6 "link it on the calendar ticket"** | Records:
  - `OS/linear/data.json` /issues/3665 ZOM-78, "Event Calendar For Zombie Match 3D". Creator `usr_8140f09bf9f1b94c` is /users/18 julia.lawson@; created 2025-04-26.
  - SQL:L205: comment `cmt_zom78_1` by `usr_175c0d7bc72ed244` (Frederick) at 2025-09-30T18:15Z: "Let us use this ticket for the ZM3D beta live-ops calendar instead of opening a new one. Link the sheet here when it is ready."
  - DM SQL:L11: "link it on the calendar ticket".
  - | Truthfulness | **consistent: no finding**

- **PC10 | P3 | §3 Tight claims | S6 "send Frederick the recommendation he asked for"** | Records:
  - SQL:L11: "Then send me your recommendation back here, with the trade-offs, on what we run and what we hold in those weeks. … I need your call, not a list of what we have."
  - | Truthfulness | **consistent: no finding**

- **PC11 | P3 | §6.8 Clock sweep | the whole prompt and every injected record** | Records:
  - The latest injected record time is SQL:L17, the Robert DM `58d06bd55ea4129eaadb726291967d5a` at 2025-09-30T22:10:00Z (15:10 PDT). Next latest are the ZOM-432 completed_at 2025-09-30T21:20Z (SQL:L203) and the PR #471 comment at 21:07:26Z (SQL:L155).
  - The only item after the clock is the scheduled GCal release at 2025-10-08 15:00–16:00Z (SQL:L82–88, created 2025-09-24, updated 2025-09-26). It is a future event, which is allowed.
  - The prompt's own future items ("start Monday the 6th", "If a beat ends up held") are framed as future.
  - The Sep 30 builds the UA plan depends on exist by the clock:
    - `OS/slack/messages/C05433XK267/2025-09.json` /1123 (#builds, 2025-09-30 19:15Z): "Match 3D iOS Submission - #50 - main Success"
    - same file /1124 (20:13Z): "Match3D Android Submission - #135 - main Success"
    - Both match SQL:L155: "both submission builds from today, iOS 50 and Android 135".
  - Every weekday named in the injected text is correct: Mon Oct 6, Sun Nov 2, Sat Nov 1, Wed Oct 29, Fri Oct 31, Wed Oct 8, Mon Oct 13, the W1–W4 ranges, "Mon, 22 Sep 2025" and "Fri, 26 Sep 2025".
  - | Today's date | **consistent: no finding**

## Injection SQL (common_errors §3 SQL line, §6.8 Injection)

- **SQL-A | ids do not collide | no finding.** No injected key exists in the base, and there are no duplicate keys inside the SQL (75 INSERT rows).
  - Slack: I scanned all 610,468 message records under `OS/slack/messages/*/*.json`. None of the 9 injected ids or 9 injected ts values appears.
  - Gmail: none of thread numbers 1844470925517303296 / 1844835127305531392 or Message-IDs `CAH4q9Zb2fK7…` / `CAH4q9Zc8uV1…` appears in the 81,404 thread files.
  - GCal: event ids `evt_9a4c…`, `evt_5c1e…`, `evt_a72f…`, `evt_1d6b…` are new.
  - Drive, Docs, Sheets and Slides: ids `d_5f2c8e…`, `f_7c3e91…`, `f_2b9d4e…`, `f_e4a17c…`, the slide ids and the element ids are new.
  - GitHub: none of these ids is in `GH/data.json` reviews, review_comments, pull_request_comments or timeline_events: #470#rev_10/#rc_10/#ev_9, #468#rev_3/#rc_38/#ev_6, #473#c_2/#ev_5, #471#c_18/#ev_8.
  - Linear: no `cmt_zom*` in `OS/linear/`. The base comments array is empty, so a full base comment-id check is not possible; this is an evidence limit.
  - Trello: action `68dac8204f1e9a3b7c2d5e61` is new.
- **SQL-B | columns exist | no finding.** All 106 statements parse, and every INSERT has as many values as columns.
  - Every column used exists in `Task_Authoring/references/universe_schema_live.json`.
  - Some columns are missing from the older `Evals/references/schema/injection.json` snapshot: `gcal_events.extras_json`, `drive_files.drive_id`, `slides_pages.notes`, `slides_page_elements.table_json`/`ordinal`, `github_reviews.seq`, `github_review_comments.pull_request_review_id`/`side`/`start_line`/`start_side`/`subject_type`/`seq`, `linear_comments.sequence`. This is advisory only under `Evals/references/schema/README.md`: "A missing table/column or mismatch alone is a provisional advisory, not a demonstrated defect."
- **SQL-C | author of an added message is in its channel | no finding.** No author has a `channel_leave` event in these channels.
  - L11/L13 EMPLOYEE_0008 in D05SD5QLG94 (channels.json /529)
  - L15 EMPLOYEE_0016 (Robert) in C08R8CHB0QL #zombie-art (/129)
  - L17 EMPLOYEE_0016 in D05GU6L0XFH (/450, members include EMPLOYEE_0005 and EMPLOYEE_0016)
  - L19 EMPLOYEE_0012 (Vincent Parker) in C0880U9751A #zombie-match3d (/108)
  - L161/165/169/173 SLACK_BOT_0004 in C093LEZGF6J #zombie-prs (/134)
- **SQL-D | apostrophes inside quoted strings are doubled | no finding.** A string-aware parse ends with no unterminated literal and no trailing text. The only in-string apostrophe is "Nathan''s" (L13), and it is doubled.
- **Related integrity (thread dates and links) | no finding.**
  - Every injected reply is later than its parent:
    - 9025d428… Sep 17 15:10Z → reply Sep 18 16:40Z
    - c2b9c903… Sep 29 21:22Z → Sep 30 16:04Z
    - 4b7c4127… Sep 26 20:16Z → Sep 29 15:36Z
    - d05a2f8a… Sep 30 15:41Z → 16:16Z
    - da3fe08c… Sep 29 22:00Z → Sep 30 21:07Z
  - The reply_count and latest_reply updates match the base:
    - 41→42, with latest_reply kept at 1759162433.383449 because that base reply is later
    - 16→17
    - 2→3
    - 7→8
    - 0→1
  - Every link resolves to a base record:
    - Commit "f7e971b0" (L186) = `GH/data.json` commit f7e971b02d24… "Endless Mode start screen VFX", 2025-09-25.
    - The timeline commit ids 4935e948… and 648e2c7b… exist.
    - PRs match3d#468, #470, #471 and #473 exist.
    - Trello card 6851a724601a61857a1b202f exists, with list "Jun 30th" and member d1cd0fef645a6c978ae1f068 "Brian Foster". The comment badge goes 1→2.
    - Every Linear comment author is an active Linear user. Every updated ZOM issue exists, and each injected comment falls after its issue's created_at.

## DR findings table

`DR# | pass | checklist section | quote | record | dimension/issue | proposed score/severity`

none. Truthfulness: 6 sentences checked, 0 findings. Today's date: 6 sentences checked, 0 findings.
