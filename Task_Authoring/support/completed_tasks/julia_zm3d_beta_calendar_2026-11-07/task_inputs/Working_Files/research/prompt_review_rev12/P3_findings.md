# P3 findings, delta on rev12: Truthfulness and Today's date

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Pass P3, blind. R12 = /private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review_rev12. Prompt: R12/inputs/04_Prompt.txt, byte-identical to rev11. New SQL: R12/inputs/01_Universe_Inject.sql, sha256 b5ccbfa577fc9f2c8f6eb3098f8d62a16623d799f41d11285de8227f1bed60d3 (hash checked, read, never run). Previous: R12/prev/01_Universe_Inject.rev11.sql, sha256 1348d287ac4a105c41b9f0bf511c6664e306adcc3cf42406688a228fd4b684e7, identical to the file I reviewed as rev11. "L" is a line in the new SQL. Paths without a prefix sit under Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/.

## Result

**Findings: none. Sentences checked: 6 of 6. Premises re-confirmed: 16 of 16. Changed or new statements dated: 7 of 7.**

- Truthfulness: no finding.
- Today's date (clock, "yesterday", "Monday the 6th", nothing after the clock): no finding.
- Departed-person premises: no finding.
- Injection SQL hygiene (ids, columns, message authors, apostrophes): no finding. Advisories A1 and A2 carry over unchanged.
- PLATFORM tags: none.

## What changed

110 statements became 111 (81 INSERT, 30 UPDATE). 6 statements were edited and 1 added. None deleted. The only line added is L256, so lines up to L255 keep their rev11 numbers and the Trello action moves from L258 to L259.

Note on ZOM-563: the id cmt_zom563_1 now holds a different comment (new author, time and body). Vincent's closing text moved, unchanged, to the new id cmt_zom563_2.

## T1 to T16 on the new SQL

| # | Prompt quote | Touched? | Re-confirmed on | Status |
|---|---|---|---|---|
| T1 | "Frederick" | No | Base only, unchanged. | Confirmed |
| T2 | "Frederick" is still at the company | No | Base only, unchanged. | Confirmed |
| T3 | "messaged me" | No | L11 identical to rev11. | Confirmed |
| T4 | "yesterday" | No | L11 and L13 identical to rev11. "2025-09-30T20:20:17.418209Z" = Tue Sep 30 13:20 PT. ts and created_at agree on all 12 injected Slack rows. | Confirmed |
| T5 | "asking for the live-ops and push calendar" | No | L11 identical: "Julia, I need the live-ops and push calendar for the beta buy we start Mon Oct 6 through Sun Nov 2." | Confirmed |
| T6 | "the Zombie Match 3D beta" | Yes, L109 and L259, not the evidence | L109 title unchanged: "ZM3D beta live-ops calendar - working rules". The edited Trello action still has no list name, so SC-13 still does not touch the prompt. Base quotes unchanged. | Confirmed |
| T7 | "the four buy weeks" | Yes, L113, not the quoted sentence | The sentence survives at L113: "The calendar covers Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC, the four buy weeks in my UA plan." Deck L136-140 unchanged. | Confirmed |
| T8 | "that start Monday the 6th" | No | L11 and deck L134 unchanged. | Confirmed |
| T9 | "What he wants in it is in his message" | No | L11 and L13 identical. | Confirmed |
| T10 | "his working rules for building it are in the brief" | Yes, L113, L115, L119, L125 and style runs | L110-111 unchanged: "Frederick, Sep 24 / How I want the beta calendar built for the four buy weeks." L11 unchanged: "The working rules for the calendar are in my brief, shared with you." | Confirmed |
| T11 | "he shared with me" | No | Drive row L108 identical. | Confirmed |
| T12 | "my live-ops calendar sheet" | No | Rows L106 and L146-147 identical. | Confirmed |
| T13 | "its ticket" | Yes, brief only, not the evidence | ZOM-429 is in no changed statement. L19 identical: "Re-tested the weekly leaderboard on the current prod build: it still does not start a new week." The rev11 quote at L119 now reads: "A held beat keeps its usual windows and weeks on its row, marked held." It concerns the sheet row, not the ticket. Which beats are held stays P1's question. | Confirmed |
| T14 | "so the owner picks it up" | No | No statement sets assignee_id. ZOM-429 assignee stays Douglas. The new L255 comment adds a Douglas action dated 2025-09-30T18:17:05Z. ZOM-526 quote at L190 identical. | Confirmed |
| T15 | "the calendar ticket" | No | cmt_zom78_1 at L205 identical. | Confirmed |
| T16 | "the recommendation he asked for" | No | L11 identical. | Confirmed |

## Date and clock of every changed or new record

All 7 sit before 2025-10-01 07:00 UTC.

| L | Record | Kind | Date | Check |
|---|---|---|---|---|
| 109 | gdocs brief | Edited | created 2025-09-24 17:15:22, modified 17:40:52 | Dates unchanged and match Drive row L108. All 9 style runs recomputed; each lands exactly on its heading. No date added. New text cites nothing newer than the brief: "Login Calendar" and "Weekly Rankings" are in the PNs Beta tab (sheet modified 2025-06-23), and the shop rotation is in ZOM-348 "Rotating Shop Discount Issues" (created 2025-07-04). |
| 157 | GitHub #468#rc_38, Arthur | Edited | 2025-09-29T15:36:41Z | Date unchanged. Before PR #468 merged at 16:13:50Z. "before the beta" is a future reference. |
| 170 | Slack 78aa8ed7, #zombie-prs mirror | Edited | 2025-09-29T15:36:43Z | Text matches L157 exactly. Attachment ts 1759160201 = 15:36:41Z. |
| 210 | Linear cmt_zom465_3, Brian | Edited | 2025-09-30T18:13:41Z | Date unchanged. New wording holds: ZOM-465 shows "~~Idle Icon Animation~~" struck and base updated_at 2025-09-23T14:16:25Z, before #468 merged on 2025-09-29T16:13:50Z. This closes my rev11 note on "came in". |
| 255 | Linear cmt_zom563_1, Douglas | Edited (new author, time, body) | 2025-09-30T18:17:05Z | Base backs it. D079SNE2TL4 2025-09-30T18:16:33Z Douglas: "Ok, I updated the prod environment with the latest teams/social changes, let me know if you are still getting those issues". Comment lands 32 seconds later, after base started_at 18:14:25Z. "the Oct 8 release" is a future event and the GCal row was created 2025-09-24 (L98-104). A Sep 2025 Slack search outside #zombie-prs, plus Douglas's Sep 30 DMs, found nothing showing Collect & Win windows on prod. |
| 256 | Linear cmt_zom563_2, Vincent | New | 2025-09-30T22:04:33Z | Equals the ZOM-563 UPDATE's completed_at and updated_at. Base: D079SNE2TL4 2025-09-30T21:58:44Z Vincent: "Yep it works as expected". Sequence 2, after L255. |
| 259 | Trello action 68dac820 | Edited | 2025-09-29T17:55:44Z | Date unchanged and equals the id prefix and the card's dateLastActivity. idCard matches the column. The field set (board, card, idCard, text, textData) has no exact base twin, since base rows with textData also carry list; every field is one base uses. |

## Clock and departed-person sweeps, rerun

- Latest dated row that is not a future event: 2025-09-30T22:10:41Z (L17). The only dates after the clock are the Oct 8 GCal release (L98-104), a future deadline, which is allowed.
- All 32 injected Linear comments sit after their issue's created_at and before the clock, in sequence order per issue.
- Authors of changed rows are Frederick, Arthur, Brian, Douglas, Vincent and Leonard, all active in Sep 2025.
- "victor" as a name appears 0 times in the SQL. Felix, Lauren and Thomas also 0.
- Shutdown rule: not applicable on an Oct 1 task.

## Injection SQL hygiene, rerun

- Parse: 111 statements tokenized with no unterminated quote, and every INSERT has equal column and value counts. Wrapper lint on the new hash: FAIL 0, CHECK 0, INFO 0.
- Apostrophes: all doubled ("Nathan''s", "Martin''s", "teams''").
- Ids: 73 primary ids, none duplicated in the SQL. New id cmt_zom563_2 cannot collide, since the base Linear comments array is empty.
- Message authors: all 12 still in their channel's members list. No Slack row was added.
- Live schema: 0 missing columns, 0 NOT NULL problems on every injected table.

**A1 (advisory, carried).** The same 13 columns across 7 tables are absent from `Evals/references/schema/injection.json` and present in `Task_Authoring/references/universe_schema_live.json`. `Evals/references/schema/README.md` treats that as provisional, not a defect.

**A2 (advisory, carried, outside P3).** L35 sits in #zm-collect-win (SC-57): is_archived true, is_private false, Julia not in members. Whether she can read it is P2's call.

## Limits

- Scope is P3 only. Which beats are held, and whether each rule resolves to one answer, was not judged here.
- The base DM cited for L255 and L256 (D079SNE2TL4) is not one Julia is in. It is used only to confirm the dates; the Linear comments themselves are unscoped.
- No live tool was run.
