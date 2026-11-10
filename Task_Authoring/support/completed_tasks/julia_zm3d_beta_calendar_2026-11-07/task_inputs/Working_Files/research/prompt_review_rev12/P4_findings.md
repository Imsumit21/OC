# P4 deep recheck findings (rev12 delta)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Inputs: 04_Prompt.txt (unchanged), 01_Universe_Inject.sql (sha256 b5ccbfa5…60d3, verified), prev/01_Universe_Inject.rev11.sql (sha256 1348d287…84e7, verified).

## Result

**Prompt: `none`, confirmed.** The prompt matches the text I reviewed in rev10 and rev11 exactly, and every record its destinations rest on is unchanged.

**Does anything reach a scored fail? No.**
- **Prompt dimensions:** no P4 topic is hit, so Contrived, Naturalness and Explicit Tool Mention have nothing to fail on.
- **Eval 0 grader-facing clause:** this is the only rule that reaches record text. On my reading nothing meets it. Every candidate is an in-world statement to Julia or on a ticket; none speaks to a solver or grader or describes the test. The closest quotes are DR5, DR10, DR18 and DR22.
- **The one argument a reviewer could still make:** §1.2 treats an incorporated record as part of the request, so §2.7 might be extended to the brief. That clause governs requirements, though, and §2.7 itself says "A per-case rule belongs in a seeded record, not in the prompt." The exposure below is about that extension, not a score.

**This revision adds exposure rather than removing it.** No finding closes. Three new items are added, all from sentences that close a fork nobody in the record raised. The four HIGH items are untouched: DR2 (B19), DR3 (the "has to land" template), DR4 (B15-B16) and DR19 (Brian's ZOM-465 note). DR19's second sentence did improve.

Open items are now 23: 4 HIGH, 12 MED, 7 LOW. Severities keep the same meaning: exposure if a reviewer extends the test, not scores.

## Count

| Item | Checked |
|---|---|
| Prompt | 6 sentences, 100 words, identical |
| SQL diff | 10 hunks, 10 changed or new sentences (table below) |
| Non-sentence changes | Trello `data_json` fields restored; old cmt_zom563_1 renumbered to cmt_zom563_2 with its text unchanged; Slack mirror of #468; brief heading offsets (all 9 style runs match the new body) |
| Unchanged, carried from rev11 | Frederick's DM and thread reply, cmt_zom78_1, cmt_zom429_1, Brian's mails, the calendar sheet and folder |

## P4 prompt findings

`none`, 6 sentences checked. Every earlier "no finding" line stands: catalog tool names, MCP or "tool" wording, section 3 search hits, step lists, bolt-on, opaque id or timestamp, stated cause, trap hint, hidden destination, audit form, if-chains, staged errors, spec-like or polished voice.

The hidden destination result depends on records, so I rechecked them. The DM, the reply, cmt_zom78_1, ZOM-429 and the sheet rows are identical in both SQL files.

## Changed sentences

Ids carry over from earlier passes. "Planted" means settling a question nobody in the record asked.

| Id | Sentence | Voice | Points at a trap | Planted | Effect |
|---|---|---|---|---|---|
| B4 | "Every window is stated in server time (UTC) as a start-end instant, closing 23:59 UTC on its last day." | Authoring, unchanged | No | Rules doc; closes an end-time fork | Slightly worse. A plain fact on B6 became a general spec rule. Stays in DR5. |
| B6 | "Collect & Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC." | Person | No | No | Back to the rev10 wording. |
| B8 | "Boss Arena is off this calendar until the pivot call, and the shop rotation is not a beat." | Mixed (was Person) | No | Rules doc; closes a scope fork | Worse. DR24. |
| B17a | "A held beat keeps its usual windows and weeks on its row, marked held." | Mixed | No | Rules doc | Neutral. DR21 stays. |
| B22 | "…names the game as Zombie Match 3D and events by their ZM3D names (Login Calendar and Weekly Rankings are fine)." | Mixed (was Person) | Mildly, by elimination | Rules doc; closes a per-row fork | Worse. DR22. |
| B23 | "Anything else is held, with what its row is missing." | Mixed | No | Rules doc | Neutral. |
| #468 rc_38, s2 (and Slack mirror) | "The final vial models are missing and need to be in before the beta, Claire has those on her list." | Person | States the need outright | Partly, unchanged | Neutral for voice. "need to be in" is natural and avoids the DR3 template, but the comment now carries the whole flag. |
| cmt_zom465_3, s2 | "Keep it on this ticket, the master VFX list was ticked before that event merged." | Authoring | Explains away ZOM-521's ticked item | Yes, unchanged | Better. Concrete and true: ZOM-521's base list is dated Sep 17, #468 merged Sep 29. Closes my rev11 P3 handoff. Nobody asked, so DR19 stays. |
| cmt_zom563_1, s1 (new) | "Prod has the teams and social changes now." | Person | No | No | Clean. Restates Douglas's real base DM from a minute earlier ("I updated the prod environment with the latest teams/social changes"). |
| cmt_zom563_1, s2 (new) | "That update carried only these, the Collect & Win server windows wait for the Oct 8 release." | Mixed | States the fact; closes the reading that this update shipped the windows | Yes | Worse. DR23. |

## New findings

Format: DR# | pass | checklist section | quote | record | dimension | severity.

| DR# | Pass | Section | Quote | Record | Dimension / issue | Severity |
|---|---|---|---|---|---|---|
| DR22 | P4-ext | §2.7 trap hint; Eval 0 closest quote | B22: "(Login Calendar and Weekly Rankings are fine)" | Brief SQL l.125. These are exact strings from two row copies on PNs Beta ("Check the login calendar"; "Weekly Rankings Reset!"), inside a general rule dated Sep 24. Both rows already fail "Ready and LIVE" (Not Ready/WIP and Ready/WIP), so the carve-out only changes what goes in "what is missing". That is rubric-level precision. By elimination it also points at the names that are not fine. Same "is fine" form as B5 and R4. | Contrived (extended): per-case carve-out | MED |
| DR23 | P4-ext | Planted-record test | "That update carried only these, the Collect & Win server windows wait for the Oct 8 release." | cmt_zom563_1 (SQL l.255), on a teams bug ticket with no mention of Collect & Win and no question. The base DM it builds on (D079SNE2TL4) is Vincent and Douglas only, so Julia can't see what the sentence corrects. Third injected statement of the same fact, after GCal and #470 rc_10. "server windows": 0 base hits. | Contrived (extended): planted to settle | MED |
| DR24 | P4-ext | §1.2 voice, bolt-on form | B8: "and the shop rotation is not a beat." | Brief SQL l.115. Tacked onto an unrelated Boss Arena sentence. The company term is "rotating shop": 160 Slack hits, plus Confluence and Linear. "shop rotation": 0 hits, and Frederick uses neither. The exclusion is fair (a daily rotation fits B7's "a reset"), so only the form is exposed. | Contrived (extended) | LOW |

## Status of earlier findings

| DR# | Rev11 | Rev12 | Why |
|---|---|---|---|
| DR1 | LOW | LOW | Unchanged. |
| DR2 | HIGH | HIGH | B19 unchanged. |
| DR3 | HIGH | HIGH | Still 7 comments by 4 authors. Base still has 0 uses of "has to land". |
| DR4 | HIGH | HIGH | B15-B16 unchanged. |
| DR5 | MED | MED | B5 unchanged. B4's new clause adds to the same register. |
| DR6 | MED | MED | B12 unchanged. |
| DR7 | MED | MED | Unchanged. |
| DR8 | MED | MED | Unchanged. |
| DR9 | MED | MED | Unchanged. |
| DR10 | MED | MED | Unchanged. |
| DR11 | MED | MED | Text unchanged; only metadata moved. |
| DR12 | MED | MED | 0 contractions, 46 uncontracted forms across 52 texts. |
| DR13 | LOW | LOW | Unchanged. |
| DR14 | Closed | Closed | |
| DR15 | LOW | LOW | Unchanged. |
| DR16 | LOW | LOW | Unchanged. |
| DR17 | LOW | LOW | Now 32 comments on 22 tickets. |
| DR18 | MED | MED | B26 unchanged ("moves to any time before it"). |
| DR19 | HIGH | HIGH | Sentence 1 unchanged. Sentence 2 improved but is still unasked. |
| DR20 | MED | MED | B3a unchanged. |
| DR21 | LOW | LOW | "and weeks" changes nothing. |

## Tallies

- **Brief:** 5 Person, 10 Mixed, 13 Authoring of 28 sentences (rev11: 7, 8, 13). B8 and B22 moved from Person to Mixed.
- **Records that settle something:** 14 Yes, 10 Partly, 13 No of 37 rows (rev11: 13, 10, 13 of 36). The new row is cmt_zom563_1.

## Handoffs to other passes (not P4 findings)

- **P1, new:** B22's carve-out only affects the "what is missing" cell for the Login Calendar and Weekly Leaderboard rows, because both are held on status anyway.
- **P3, closed:** "ticked before that event merged" now fits the dates.
- **P1, still open:** B26 allows any time before the lock, so the moved date has no single value.
- **P1, still open:** the DR3 comments are mostly owners' own claims (SCOPE_GAP). cmt_zom465_3 and #468 rc_38 are third-party flags, so they are stronger.
- **P1/P2, still open:** B16 has no CHANGES_REQUESTED review in Aug-Sep.
- **P2, still open:** Douglas's "Both tables are updated." sits in #zm-collect-win, which is not private but does not list Julia as a member.
- **P2, still open:** the amended push rules sit in a thread reply, and S3 says only "his message".

## Platform defects

None.

## Blindness note

I read R12/REVIEW_SETUP.md first and opened no sibling review folder this round. Helpers are under R12/work/p4. I left the other files in R12/work unopened and did not open other passes' R12/out files. Earlier statuses come from my own findings, as this delta requires.
