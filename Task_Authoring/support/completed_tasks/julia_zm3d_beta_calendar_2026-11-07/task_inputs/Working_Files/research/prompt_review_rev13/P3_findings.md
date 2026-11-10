# P3 findings, delta on rev13: Truthfulness and Today's date

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Pass P3, blind. R13 = /private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review_rev13. Prompt: R13/inputs/04_Prompt.txt, byte-identical to rev12. New SQL: R13/inputs/01_Universe_Inject.sql, sha256 1f2175a297fd390960f22c3767f790fc980a881023affa6ece970745fb40289b (hash checked, read, never run). Previous: R13/prev/01_Universe_Inject.rev12.sql, sha256 b5ccbfa577fc9f2c8f6eb3098f8d62a16623d799f41d11285de8227f1bed60d3, identical to the file I reviewed as rev12. "L" is a line in the new SQL. Paths without a prefix sit under Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/.

## Result

**Findings: none. Sentences checked: 6 of 6. Premises re-confirmed: 16 of 16. Changed statements dated: 5 of 5.**

- Truthfulness: no finding.
- Today's date (clock, "yesterday", "Monday the 6th", nothing after the clock): no finding.
- Departed-person premises: no finding.
- Injection SQL hygiene (ids, columns, message authors, apostrophes): no finding. Advisories A1 and A2 carry over unchanged.
- PLATFORM tags: none.

## What changed

Still 111 statements (81 INSERT, 30 UPDATE). 5 statements edited, none added or deleted. No line numbers moved. No timestamp changed in any of the 5.

## T1 to T16 on the new SQL

Two premises are touched, T6 and T10. Neither loses its evidence.

| # | Prompt quote | Touched? | Re-confirmed on | Status |
|---|---|---|---|---|
| T1 | "Frederick" | No | Base only, unchanged. | Confirmed |
| T2 | "Frederick" is still at the company | No | Base only, unchanged. | Confirmed |
| T3 | "messaged me" | No | L11 identical to rev12. | Confirmed |
| T4 | "yesterday" | No | L11 and L13 identical. ts and created_at agree on all 12 injected Slack rows. | Confirmed |
| T5 | "asking for the live-ops and push calendar" | No | L11 identical. | Confirmed |
| T6 | "the Zombie Match 3D beta" | Yes, L109 and L259, not the evidence | L109 title unchanged: "ZM3D beta live-ops calendar - working rules". My rev12 line "still has no list name" no longer applies: L259 again carries `"list":{"id":"6851a674975da1fe76e70d93","name":"BETA: Sep 30"}`. That matches base: the last rename, 2025-09-12T16:42:21Z, is to "BETA: Sep 30", and 71 base actions since then use it. The prompt gives no beta date, so SC-13 still does not touch it. | Confirmed |
| T7 | "the four buy weeks" | No | L113 sentence and deck L136-140 unchanged in this diff. | Confirmed |
| T8 | "that start Monday the 6th" | No | L11 and deck L134 unchanged. | Confirmed |
| T9 | "What he wants in it is in his message" | No | L11 and L13 identical. | Confirmed |
| T10 | "his working rules for building it are in the brief" | Yes, L115, L125 and style runs | L110-111 unchanged: "Frederick, Sep 24 / How I want the beta calendar built for the four buy weeks." L11 unchanged: "The working rules for the calendar are in my brief, shared with you." | Confirmed |
| T11 | "he shared with me" | No | Drive row L108 unchanged. | Confirmed |
| T12 | "my live-ops calendar sheet" | No | Rows L106 and L146-147 unchanged. | Confirmed |
| T13 | "its ticket" | No | L19 identical. ZOM-429 in no changed statement. L119 unchanged. | Confirmed |
| T14 | "so the owner picks it up" | No | No statement sets assignee_id. ZOM-429 assignee stays Douglas. L190 unchanged. | Confirmed |
| T15 | "the calendar ticket" | No | L205 unchanged. | Confirmed |
| T16 | "the recommendation he asked for" | No | L11 identical. | Confirmed |

## Date and clock of every changed record

All 5 sit before 2025-10-01 07:00 UTC.

| L | Record | Date | Check |
|---|---|---|---|
| 109 | gdocs brief | created 2025-09-24 17:15:22, modified 17:40:52 | Dates unchanged and match Drive row L108. All 9 style runs recomputed; each lands exactly on its heading, including the moved "Config locks" at 2873-2885. No date added. "the rotating shop" cites nothing newer than the brief: ZOM-348 "Rotating Shop Discount Issues" was created 2025-07-04. |
| 157 | GitHub #468#rc_38, Arthur | 2025-09-29T15:36:41Z | Unchanged. Before PR #468 merged at 16:13:50Z. New text: "still need their final models before the event runs. Not a blocker for this PR". "before the event runs" is a future reference, and "not a blocker" fits a PR that merged 37 minutes later. |
| 170 | Slack 78aa8ed7, #zombie-prs mirror | 2025-09-29T15:36:43Z | Unchanged. Text matches L157 exactly. Attachment ts 1759160201 = 15:36:41Z. |
| 210 | Linear cmt_zom465_3, Brian | 2025-09-30T18:13:41Z | Unchanged. "before the event runs" is a future reference. "ticked before that event merged" still holds: ZOM-465 base updated_at 2025-09-23T14:16:25Z, #468 merged 2025-09-29T16:13:50Z. |
| 259 | Trello action 68dac820 | 2025-09-29T17:55:44Z | Unchanged and equals the id prefix and the card's dateLastActivity. Field set now matches 14 base comment actions, which closes my rev12 note on the missing twin. List name matches the base actions around its date. |

## Sweeps, rerun

- Latest dated row that is not a future event: 2025-09-30T22:10:41Z (L17). The only dates after the clock are the Oct 8 GCal release (L98-104), a future deadline, which is allowed.
- All 32 injected Linear comments sit after their issue's created_at and before the clock, in sequence order per issue.
- "victor" as a name appears 0 times in the SQL. Felix, Lauren and Thomas also 0.
- Parse: 111 statements with no unterminated quote and equal column and value counts. Wrapper lint on the new hash: FAIL 0, CHECK 0, INFO 0.
- Apostrophes: all doubled ("Nathan''s", "Martin''s", "teams''").
- Ids: 73 primary ids, none duplicated in the SQL, none new in this revision.
- Message authors: all 12 still in their channel's members list.
- Live schema: 0 missing columns, 0 NOT NULL problems on every injected table.

**A1 (advisory, carried).** The same 13 columns across 7 tables are absent from `Evals/references/schema/injection.json` and present in `Task_Authoring/references/universe_schema_live.json`. `Evals/references/schema/README.md` treats that as provisional, not a defect.

**A2 (advisory, carried, outside P3).** L35 sits in #zm-collect-win (SC-57): is_archived true, is_private false, Julia not in members. Whether she can read it is P2's call.

## Limits

- Scope is P3 only. Which beats are held, and whether each rule resolves to one answer, was not judged here.
- No live tool was run.
