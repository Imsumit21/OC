# P4 deep recheck findings (rev13 delta)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Inputs: 04_Prompt.txt (unchanged), 01_Universe_Inject.sql (sha256 1f2175a2…289b, verified), prev/01_Universe_Inject.rev12.sql (sha256 b5ccbfa5…60d3, verified).

## Result

**Prompt: `none`, confirmed.** The prompt matches the text I reviewed in earlier rounds exactly, and every record its destinations rest on is unchanged.

**Does anything reach a scored fail? No.**
- **Prompt dimensions:** no P4 topic is hit, so Contrived, Naturalness and Explicit Tool Mention have nothing to fail on.
- **Eval 0 grader-facing clause:** this is the only rule that reaches record text, and on my reading nothing meets it. Every candidate is an in-world statement to Julia or on a ticket; none speaks to a solver or grader or describes the test. The closest quotes are still DR5, DR10, DR18 and DR22.
- **§1.2 argument:** a reviewer could still try to extend §2.7 to the brief as an incorporated record. §1.2 governs requirements, and §2.7 sends per-case rules to seeded records, so that extension is exposure, not a score.

**This revision is a small net improvement.** Arthur's #468 comment now reads as a real review note, and "rotating shop" fixes the wording tell in DR24. No finding closes and none is added.

Open items stay at 23: 4 HIGH, 12 MED, 7 LOW. All four HIGH items stand: DR2 (B19), DR3 (the "has to land" template), DR4 (B15-B16) and DR19 (Brian's ZOM-465 note). Severities keep the same meaning: exposure if a reviewer extends the test, not scores.

## Count

| Item | Checked |
|---|---|
| Prompt | 6 sentences, 100 words, identical |
| SQL diff | 7 hunks, 5 changed sentences (table below) |
| Non-sentence changes | Slack mirror of #468; Trello `data_json` list field restored, comment text identical; brief heading offsets (all 9 style runs match the new body) |
| Unchanged, carried from rev12 | Frederick's DM and thread reply, cmt_zom78_1, cmt_zom429_1, Brian's mails, the calendar sheet and folder |

## P4 prompt findings

`none`, 6 sentences checked. Every earlier "no finding" line stands: catalog tool names, MCP or "tool" wording, section 3 search hits, step lists, bolt-on, opaque id or timestamp, stated cause, trap hint, hidden destination, audit form, if-chains, staged errors, spec-like or polished voice.

The hidden destination result depends on records, so I rechecked them. The DM, the reply, cmt_zom78_1, ZOM-429 and the sheet rows are identical in both SQL files.

## Changed sentences

"Planted" means settling a question nobody in the record asked.

| Id | Sentence | Voice | Points at a trap | Planted | Effect |
|---|---|---|---|---|---|
| B8 | "Boss Arena is off this calendar until the pivot call, and the rotating shop is not a beat." | Mixed | No | Rules doc; closes a scope fork | Better. "rotating shop" is the company term (160 Slack hits). Still tacked onto an unrelated sentence, so DR24 stays LOW on form alone. |
| B23 | "Anything else is held, with which of those its row is missing." | Mixed, stiffer | No | Rules doc; limits the cell to the listed conditions | Slightly worse. A closed-set output rule that works with B22's carve-out. Folded into DR22. |
| #468 rc_38, s1 (and Slack mirror) | "The Collect & Win vials that spawn in the levels still need their final models before the event runs." | Person | States the need outright | No (was Partly) | Better. Now about what the PR adds, on the file that spawns them. |
| #468 rc_38, s2 (and Slack mirror) | "Not a blocker for this PR, Claire has those on her list." | Person | No | No (was Partly) | Better. "not a blocker" is real company language (112 Slack hits). The best change this round. |
| cmt_zom465_3, s1 | "Marcus, the Collect & Win icon does have to land before the event runs, it is the one event icon with no animation." | Authoring | States the answer outright | Yes, unchanged | Slightly better. It no longer mirrors the "before the beta" tail on Brian's three other comments, but "does have to land" is still the DR3 template, emphatic and unasked. DR19 stays HIGH. |

One small new tell: "before the event runs" has 0 base Slack hits, and two injected authors now share it (Arthur on #468, Brian on ZOM-465). It also echoes "before it runs" in F2 and B20. This adds to DR3 without changing its severity.

## Status of earlier findings

| DR# | Rev12 | Rev13 | Why |
|---|---|---|---|
| DR3 | HIGH | HIGH | Still 7 comments by 4 authors, plus the shared tail above. |
| DR19 | HIGH | HIGH | See the table above. |
| DR22 | MED | MED | B22 unchanged. B23's "which of those" adds to the same per-row precision. |
| DR24 | LOW | LOW | Wording tell removed; bolt-on form remains. |

Unchanged: DR1, DR2, DR4 to DR13, DR15 to DR18, DR20, DR21 and DR23, at their rev12 severities. DR14 stays closed. DR12's count is still 0 contractions and 46 uncontracted forms across 52 texts. DR17's is still 32 comments on 22 tickets.

## Tallies

- **Brief:** 5 Person, 10 Mixed, 13 Authoring of 28 sentences, unchanged.
- **Records that settle something:** 14 Yes, 9 Partly, 14 No of 37 rows (rev12: 14, 10, 13). #468 rc_38 moved from Partly to No.

## Handoffs to other passes (not P4 findings)

- **P1, new:** #468 rc_38 and cmt_zom465_3 now tie their deadline to "before the event runs", not the beta start, so the Collect & Win items are due by that beat's first window.
- **P1, still open:** B22's carve-out only affects the "what is missing" cell, because both rows are held on status anyway.
- **P1, still open:** B26 allows any time before the lock, so the moved date has no single value.
- **P1, still open:** the DR3 comments are mostly owners' own claims (SCOPE_GAP). cmt_zom465_3 and #468 rc_38 are third-party flags, so they are stronger.
- **P1/P2, still open:** B16 has no CHANGES_REQUESTED review in Aug-Sep.
- **P2, still open:** Douglas's "Both tables are updated." sits in #zm-collect-win, which is not private but does not list Julia as a member.
- **P2, still open:** the amended push rules sit in a thread reply, and S3 says only "his message".

## Platform defects

None.

## Blindness note

I read R13/REVIEW_SETUP.md first and opened no sibling review folder this round. Helpers are under R13/work/p4. I did not open other passes' R13/out files. Earlier statuses come from my own findings, as this delta requires.
