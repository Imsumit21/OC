# P3 findings, delta on rev11: Truthfulness and Today's date

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Pass P3, blind. R11 = /private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review_rev11. Prompt: R11/inputs/04_Prompt.txt, byte-identical to rev10. New SQL: R11/inputs/01_Universe_Inject.sql, sha256 1348d287ac4a105c41b9f0bf511c6664e306adcc3cf42406688a228fd4b684e7 (hash checked, read, never run). Previous: R11/prev/01_Universe_Inject.rev10.sql, sha256 ffbac4586fb91842ca16263c2b76987c26623c7ed689e00d33886c63f9331bdc. "L" is a line in the new SQL. Paths without a prefix sit under Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/.

## Result

**Findings: none. Sentences checked: 6 of 6. Premises re-confirmed: 16 of 16. Changed or new statements dated: 17 of 17.**

- Truthfulness: no finding.
- Today's date (clock, "yesterday", "Monday the 6th", nothing after the clock): no finding.
- Departed-person premises: no finding.
- Injection SQL hygiene (ids, columns, message authors, apostrophes): no finding. Two advisories, A1 and A2.
- PLATFORM tags: none.

## What changed

107 statements became 110 (80 INSERT, 30 UPDATE). 14 statements were edited and 3 added. No statement deleted. Line numbers after old L34 moved by 4, and after old L206 by 5.

## T1 to T16 on the new SQL

| # | Prompt quote | Touched? | Re-confirmed on (locator and quoted value) | Status |
|---|---|---|---|---|
| T1 | "Frederick" | No | Base only. `slack/users.json` EMPLOYEE_0008_SLACK_ID "Frederick Stone", deleted false. `contacts/contacts.json` holds one Frederick. | Confirmed |
| T2 | "Frederick" is still at the company | No | Base only. #executives 2025-09-30T21:26Z: "can you clarify? Fine at current pace, or fine to juice bids yet again?" | Confirmed |
| T3 | "messaged me" | No | L11 is byte-identical to rev10 (line sha256 7fc9d772 on both). Id bca784379e7dbca9e64e79a64dfefbba, channel D05SD5QLG94, Julia and Frederick both in `slack/channels.json` members. | Confirmed |
| T4 | "yesterday" | Yes, L13 text only | L11 ts 1759263617.418209, "2025-09-30T20:20:17.418209Z" = Tue Sep 30 13:20 PT. L13 edit left ts 1759263878.305129 and "2025-09-30T20:24:38.305129Z" as they were. ts and created_at agree on all 12 injected Slack rows. | Confirmed |
| T5 | "asking for the live-ops and push calendar" | No | L11: "Julia, I need the live-ops and push calendar for the beta buy we start Mon Oct 6 through Sun Nov 2." | Confirmed |
| T6 | "the Zombie Match 3D beta" | Yes, L109 and L258, not the evidence | L109 title unchanged: "ZM3D beta live-ops calendar - working rules". Base evidence unchanged: team_ZOM "Zombie Match 3D"; #company-internal 2025-09-12T19:11Z "We finalized the dev pipeline for the beta." The edited Trello action (L258) no longer carries the list name "BETA: Sep 30". The prompt gives no beta date, so SC-13 still does not touch it. | Confirmed |
| T7 | "the four buy weeks" | Yes, L113 and L136-141 | The quoted sentence survives at L113: "The calendar covers Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC, the four buy weeks in my UA plan." Deck slide 2 keeps "The four buy weeks" and W1 to W4 at L136-140. Only its last line changed, L141: "Small scale at first, any scale-up comes after the pivot call." | Confirmed |
| T8 | "that start Monday the 6th" | Yes, L134 | L11 "we start Mon Oct 6" unchanged; Oct 6, 2025 is a Monday. L134 now reads "Beta-cohort buy, starting once the stores approve the Sep 30 builds." The clause I relied on is intact. Added evidence for those builds: match3d commit 3f5352a5b5 carries tags TestFlight_iOS_50 and Submission_Android_135. | Confirmed |
| T9 | "What he wants in it is in his message" | Yes, L13 opener | L11 list unchanged. My rev10 quote of L13 is gone: "Two things the brief does not spell out." now reads "Two things on top of the brief." It remains a reply in the same thread (thread_parent_id bca784379e7dbca9e64e79a64dfefbba), so "his message" is still not false. | Confirmed |
| T10 | "his working rules for building it are in the brief" | Yes, L109-127 | Four paragraphs and the style runs were edited. L110-111 unchanged: "Frederick, Sep 24 / How I want the beta calendar built for the four buy weeks." L11 unchanged: "The working rules for the calendar are in my brief, shared with you." | Confirmed |
| T11 | "he shared with me" | No | Drive row identical, now L108: owner Frederick, shared_with_emails_json ["julia.lawson@harmonygames.co"], role reader, created 2025-09-24 17:15:22+00. | Confirmed |
| T12 | "my live-ops calendar sheet" | No | Rows identical, now L146-147 (sheet, owner Julia) and L106 (folder "ZM Live Ops"). L11: "Put it in the calendar sheet in your ZM Live Ops folder". | Confirmed |
| T13 | "its ticket" | Yes, brief only, not the evidence | ZOM-429 is in no changed statement and cmt_zom429_1 is identical. L19 unchanged: "Re-tested the weekly leaderboard on the current prod build: it still does not start a new week." The brief's new last sentence in "Held or not" concerns the sheet row: "A held beat keeps its usual windows on its row, marked held." Which beats are held stays P1's question. | Confirmed |
| T14 | "so the owner picks it up" | No | No statement sets assignee_id. ZOM-429 assignee stays douglas@harmonygames.co, last Slack post 2025-09-30T23:56Z. ZOM-542 moves Regression to Todo, so it stays open with Samuel and the open-ticket assignee set is unchanged. Quote on ZOM-526 identical, now L190: "it does not have to land before the beta". | Confirmed |
| T15 | "the calendar ticket" | No | cmt_zom78_1 and the ZOM-78 update identical, now L205: "Let us use this ticket for the ZM3D beta live-ops calendar instead of opening a new one. Link the sheet here when it is ready." | Confirmed |
| T16 | "the recommendation he asked for" | No | L11: "Then send me your recommendation back here, with the trade-offs, on what we run and what we hold in those weeks." | Confirmed |

## Date and clock of every changed or new record

All 17 sit before 2025-10-01 07:00 UTC. PT = UTC minus 7.

| L | Record | Kind | Date | Check |
|---|---|---|---|---|
| 13 | Slack 890dc27f, Frederick reply | Edited | 2025-09-30T20:24:38Z | ts and created_at agree, after parent L11. |
| 15 | Slack 933cee9f, Robert, Halloween ok | Edited | 2025-09-18T16:40:23Z | After Martin's parent, 2025-09-17T15:10:09Z. |
| 17 | Slack 669d15f6, Robert DM | Edited | 2025-09-30T22:10:41Z | Sep 30 15:10 PT. Still the latest dated row in the SQL. |
| 27 | Slack a08ff7cb, Vincent, lightSweep | Edited | 2025-09-30T21:46:15Z | Holds in git. Oliver's commit 25c6c66b6b at 21:20:26Z changes `lightSweep Box Variant.mat`, before this message and after the tagged commit 3f5352a5b5 for iOS 50 and Android 135, so "the next store build" is right. |
| 35 | Slack 7d70c775, Douglas, "Both tables are updated." | New | 2025-09-26T16:22:44Z | Fri Sep 26 09:22 PT. After Brian's ask at 15:10:00Z. Douglas posted at 16:06Z that day. No later post in the channel disputes it. |
| 37 | UPDATE parent 0069f614 | New | latest_reply 1758903764.713429 | Base reply_count 2, reply_users_count 1, latest_reply 1758899428.567489. New 3, 2 and the L35 ts are right. |
| 109 | gdocs brief | Edited | created 2025-09-24 17:15:22, modified 17:40:52 | Dates unchanged and match Drive row L108. All 9 style runs recomputed; each lands exactly on its heading. No date added to the text. |
| 132 | Deck slide 1 element | Edited | Deck 2025-09-23 | No date changed. "Sep 30 builds" stays a forward reference from Sep 23. |
| 136 | Deck slide 2 element | Edited | Deck 2025-09-23 | Week dates unchanged. "pivot call" is not new to this deck: slide 3 already had it, and pivot talk is in Slack by 2025-09-21. |
| 164 | GitHub #472#rc_1 | Edited | 2025-09-30T15:52:58Z | Equals review rev_1, before merge at 15:53:04Z. |
| 166 | Slack 65564543, #zombie-prs mirror | Edited | 2025-09-30T15:53:00Z | Text matches L164 exactly. Attachment ts 1759247578 = 15:52:58Z. Before base latest_reply 1759247586.958099. |
| 210 | Linear cmt_zom465_3, Brian | New | 2025-09-30T18:13:41Z | After cmt_zom465_2 at 18:05:02Z. Sequence 3. Author usr_fc22d5941b2aeb5c = Brian. See note below. |
| 211 | UPDATE ZOM-465 | Edited | updated_at 2025-09-30T18:13:41Z | Equals the latest comment. Base value was 2025-09-23. |
| 222 | Linear cmt_zom504_1, Vincent | Edited | 2025-09-22T15:30:39Z | After issue created 2025-08-25. Vincent is the reporter, so "Re-tested" fits. |
| 240 | UPDATE ZOM-542 state to Todo | Edited | updated_at 2025-09-22T18:40:21Z | Equals cmt_zom542_1. Todo is a live ZOM state (45 tickets). |
| 255 | Linear cmt_zom563_1, Vincent | Edited | 2025-09-30T22:04:33Z | After base started_at 18:14:25Z. Equals completed_at. |
| 258 | Trello action 68dac820 | Edited | 2025-09-29T17:55:44Z | Id prefix decodes to the same instant. Equals the card's dateLastActivity. "Mon Oct 13" is a Monday. The data shape without list and textData has one base example. |

Note on L210: it says "the master VFX list was written before that event came in". ZOM-465 was created 2025-08-11T14:48:37Z and PR #468 merged Collect & Win 2025-09-29T16:13:50Z, so the claim holds on the meaning Marcus uses at L209 ("came in after my note above"). Brian's design doc `f_7989a718d6be1e4428b143` was created 2025-08-01, before the ticket. So on a "spec existed" reading the phrase is loose. It is in a comment, not a prompt premise, and no prompt date rests on it. Not a finding.

## Clock and departed-person sweeps, rerun

- Latest dated row that is not a future event: 2025-09-30T22:10:41Z (L17). The only dates after the clock are the Oct 8 GCal release (L98-104), a future deadline, which is allowed.
- All 31 injected Linear comments sit after their issue's created_at and before the clock, in sequence order per issue.
- Both new records have authors with Sep 2025 Slack activity: Douglas and Brian. The rev10 list of named people is otherwise unchanged.
- "victor" as a name appears 0 times in the SQL. Felix, Lauren and Thomas also 0.
- Shutdown rule: not applicable on an Oct 1 task.

## Injection SQL hygiene, rerun

- Parse: 110 statements tokenized with no unterminated quote, and every INSERT has equal column and value counts. Wrapper lint on the new hash: FAIL 0, CHECK 0, INFO 0.
- Apostrophes: all doubled ("Nathan''s", "Martin''s", "teams''").
- Ids: 72 primary ids, none duplicated in the SQL. New Slack id and ts are absent from a full scan of `slack/messages/`. The base Linear comments array is empty, so cmt_zom465_3 cannot collide. Other ids are unchanged from rev10.
- Message authors: all 12 are in their channel's members list. New row: C09EVVCFHKR EMPLOYEE_0031 (Douglas), channel_join 2025-09-15T18:01:27Z, no leave event.
- New thread reply sits in the same channel as its parent and after it. The UPDATE target exists in base.
- Live schema: 0 missing columns, 0 NOT NULL problems on every injected table.

**A1 (advisory, carried from rev10).** The same 13 columns across 7 tables are absent from `Evals/references/schema/injection.json` and present in `Task_Authoring/references/universe_schema_live.json`. `Evals/references/schema/README.md` treats that as provisional, not a defect.

**A2 (advisory, new, outside P3).** L35 adds a row to #zm-collect-win, which is SC-57's channel: `slack/channels.json` has is_archived true, is_private false, and Julia is not in members. The row's date is consistent, since people posted there through Sep 30. No prompt premise rests on it. Whether Julia can read it, and whether an answer depends on it, is P2's call.

## Limits

- Scope is P3 only. Which beats are held, and whether each rule resolves to one answer, was not judged here.
- No live tool was run. Persona visibility rests on `Evals/references/persona/acl.md`.
