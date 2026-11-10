# P4 deep recheck findings (rev11 delta)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Inputs: 04_Prompt.txt (unchanged), 01_Universe_Inject.sql (sha256 1348d287…84e7, verified), prev/01_Universe_Inject.rev10.sql (sha256 ffbac458…1bdc, verified).

## Result

**Prompt: `none`, confirmed.** The prompt matches the text I reviewed in rev10 exactly, and every record its destinations rest on is unchanged.

**The revision helps overall, but two new sentences add exposure.**
- **Closed:** the Robert echo (DR1 drops from HIGH to LOW) and the Eval 0 shape match in Frederick's opener (DR14).
- **Added:** Brian's new ZOM-465 note is now the most planted record in the set (DR19, HIGH), and "moves to any time before it" reads as an answer tolerance (DR18, MED).
- **Still HIGH:** DR2 (B19), DR3 (the "has to land" template, which grew from 6 comments to 7) and DR4 (B15-B16).

Open items are now 20: 4 HIGH, 10 MED, 6 LOW. DR14 is closed.

**Score effect under the current text: still none.** The same three limits apply as in rev10: §2.7 tests prompt wording, the persona's style is not a standard, and Eval 0 leaves voice out of scope. Nothing reaches the Eval 0 grader-facing FAIL bar on my reading. The closest quotes are now DR5, DR10 and DR18. Severities keep the same meaning: exposure if a reviewer extends the test, not scores.

## Count

| Item | Checked |
|---|---|
| Prompt | 6 sentences, 100 words, identical |
| SQL diff | 18 hunks, 18 changed or new sentences (table below) |
| Non-sentence changes | ZOM-542 state to Todo; Trello `data_json` trimmed; reply counts; brief heading offsets (all 9 style runs match the new body) |
| Unchanged, carried from rev10 | Frederick's DM, cmt_zom78_1, cmt_zom429_1, cmt_zom534_2, Brian's mails, the calendar sheet and folder |

## P4 prompt findings

`none`, 6 sentences checked. Every rev10 "no finding" line stands: catalog tool names, MCP or "tool" wording, section 3 search hits, step lists, bolt-on, opaque id or timestamp, stated cause, trap hint, hidden destination, audit form, if-chains, staged errors, spec-like or polished voice.

The hidden destination result depends on records, so I rechecked them. The DM, cmt_zom78_1, ZOM-429 and the sheet rows are identical in both SQL files.

## Changed sentences

Ids carry over from rev10. B3a and B17a are new brief sentences. "Planted" means settling a question nobody in the record asked.

| Id | Sentence | Voice | Points at a trap | Planted | Effect |
|---|---|---|---|---|---|
| R1 | "Two things on top of the brief." | Person (was Mixed) | No | n/a | Better. Frederick says "On top of that" in base. Closes DR14. |
| Robert Sep 18, s1 | "Halloween one-off: approved from my side for one week of the beta." | Mixed | Sets up the reversal | Partly, unchanged | Better. "one of the beta weeks" assumed a plan that came later. |
| Robert Sep 18, s2 | "…and I sign the object off if it lands in time." | Mixed | No | Partly, unchanged | Better. "the cut" is gone. |
| Robert Sep 30, s3 | "Sorry for the flip." | Person (message was Authoring) | No longer echoes B19 | Partly (was Yes) | Much better. See DR1. |
| lightSweep, s2 | "…so it rides the next store build and nothing has to land for the beta." | Mixed | DR3 phrase | Partly, unchanged | Neutral. "store build" is real company wording. |
| Douglas reply | "Both tables are updated." | Person | No | No | Clean. Brian asked "Could you update them?" in that thread. Douglas's real replies look the same ("Updated!", "updated, all stages are accepted now"). The best-grounded injected record in the set. |
| B3a (new) | "Clip anything that starts before or runs past that to those two instants." | Authoring | No | Rules doc; closes an edge-value fork | Worse. DR20. |
| B6 | "Collect & Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC and closing 23:59 UTC on its last day." | Person | No | No | Neutral. Plain fact. |
| B12 | "…the daily gift (Login Calendar on the push sheet, same beat)…" | Authoring (whole sentence) | States rule | Rules doc | Slightly better. The parenthetical now sounds like a note, but "not its window dates" stands, so DR6 stays. |
| B17a (new) | "A held beat keeps its usual windows on its row, marked held." | Mixed | No | Rules doc; closes a layout fork | Slightly worse. DR21. |
| B26 | "A committed date that misses the lock moves to any time before it and its owner is told in a reply on the mail where they committed to it." | Authoring | Riddle form | Rules doc | Worse. DR18, on top of DR7. |
| Deck, slide 1 | "Beta-cohort buy, starting once the stores approve the Sep 30 builds." | Person | No | No | Better. "Scaled" is gone. |
| Deck, slide 2 | "Small scale at first, any scale-up comes after the pivot call." | Person | No | No | Better. Now agrees with slide 3, so my rev10 P2 handoff closes. |
| #472 rc_1, s2 (and Slack mirror) | "Separately, the Season Pass premium strip art still shows the October range." | Mixed | Now fits B20's "player-facing art" | Yes, unchanged | Neutral. DR9 stays. Slight mismatch: it is now art, but the comment still says Oliver "is taking the date change". |
| cmt_zom465_3, s1 (new) | "Marcus, the Collect & Win icon does have to land before the beta, it is the one event icon with no animation." | Authoring | States the answer outright | Yes | Worse. DR19. |
| cmt_zom465_3, s2 (new) | "Keep it on this ticket, the master VFX list was written before that event came in." | Authoring | Explains away ZOM-521's ticked item | Yes | Worse. DR19. |
| cmt_zom504_1, s1 | "Re-tested: it only shows up with the bot running; in manual play across a long endless session I could not get it." | Person | No | No | Neutral. |
| cmt_zom563_1, s1 | "Checked on prod: teams' lives, golden frames and names all work as expected." | Person | No | No | Neutral. |

## New findings

Format: DR# | pass | checklist section | quote | record | dimension | severity.

| DR# | Pass | Section | Quote | Record | Dimension / issue | Severity |
|---|---|---|---|---|---|---|
| DR18 | P4-ext | §1.2 voice; Eval 0 closest quote | B26: "moves to any time before it" | Brief f_7c3e91a4… (SQL l.127). Replaces "moves earlier". It reads as an acceptance range: a founder moving a dependency names a date or says "before the lock", not "any time". No in-world reason is given. Same family as DR5 ("is fine, a different instant is not"). | Contrived (extended): grader register | MED |
| DR19 | P4-ext | Planted-record test | "Marcus, the Collect & Win icon does have to land before the beta…"; "Keep it on this ticket, the master VFX list was written before that event came in." | cmt_zom465_3 (SQL l.210), 8 minutes after Marcus's note, which asked nothing. Sentence 1 inverts the DR3 template with emphatic "does", in Brian's own phrase from ZOM-526, ZOM-565 and ZOM-566. Sentence 2 explains a record discrepancy nobody raised on this ticket (ZOM-521's ticked "animations on these icons"). "master VFX list": 0 Slack hits, and ZOM-465 is itself titled "Endless Mode Master VFX Ticket". | Contrived (extended): planted to settle | HIGH |
| DR20 | P4-ext | §1.2 voice | B3a: "Clip anything that starts before or runs past that to those two instants." | Brief SQL l.113. Closes a P1 edge-value fork. "clip" in Frederick's Slack is only an audio clip. "instant(s)" now appears 5 times in the brief. A rules doc is a fair home for this; the register is the issue. | Contrived (extended): spec register | MED |
| DR21 | P4-ext | §1.2 voice | B17a: "A held beat keeps its usual windows on its row, marked held." | Brief SQL l.119. A layout rule for the sheet, in plain words. | Contrived (extended) | LOW |

## Status of rev10 findings

| DR# | Rev10 | Rev11 | Why |
|---|---|---|---|
| DR1 | HIGH | **LOW** | The echo of "his later word…" is gone, so nothing now needs Robert to have read a brief shared only with Julia. The message gives a real reason, and pivot talk is live that day (Robert, Sep 30: "when we're talking about the pivot"). Residual: he still volunteers it in a DM about other things. |
| DR2 | HIGH | HIGH | B19 unchanged. It still foretells the reversal, and "Product … he" still withholds the name. It now carries the trap alone. |
| DR3 | HIGH | HIGH | Worse: 7 comments by 4 authors, Brian with 4 of them. Base still has 0 uses of "has to land". |
| DR4 | HIGH | HIGH | B15-B16 unchanged. |
| DR5 | MED | MED | B5 unchanged. B3a adds to the "instant" register. |
| DR6 | MED | MED | Parenthetical improved, "not its window dates" unchanged. |
| DR7 | MED | MED | Form unchanged. New wording is scored in DR18. |
| DR8 | MED | MED | Unchanged. |
| DR9 | MED | MED | "art" edit changes nothing about the placement. |
| DR10 | MED | MED | Unchanged. |
| DR11 | MED | MED | Text unchanged; only metadata was trimmed. |
| DR12 | MED | MED | 0 contractions, 45 uncontracted forms across 51 texts. |
| DR13 | LOW | LOW | R2-R5 unchanged. |
| DR14 | LOW | **Closed** | New opener no longer matches the Eval 0 example. |
| DR15 | LOW | LOW | Unchanged. |
| DR16 | LOW | LOW | Unchanged. |
| DR17 | LOW | LOW | Now 31 comments on 22 tickets. |

## Tallies

- **Brief:** 7 Person, 8 Mixed, 13 Authoring of 28 sentences (rev10: 7, 7, 12 of 26).
- **Records that settle something:** 13 Yes, 10 Partly, 13 No of 36 rows. This includes the correction below, Robert's move to Partly, and the two new records.

## Correction to my rev10 table

I marked cmt_zom566_1 as planted Yes, and that was too strong. Its first sentence restates a real exchange in #zm-collect-win on Sep 30, an hour earlier:
- Owen asked "is the list sorted by priority order?"
- Vincent said "none of them blockers".
- Brian said "Analytics and name changes first".

It should be Partly. The tail ("do not have to land before the beta") is still the DR3 template, so DR3 stands. The rev10 line that only the lightSweep reply answers a question in its own thread also stands.

## Handoffs to other passes (not P4 findings)

- **P1, new:** B26 now allows any time before the lock, so the moved date has no single value. The rubric must accept any time before it.
- **P1, new:** cmt_zom465_3 is a third-party flag, not an owner's claim, so it is stronger evidence than the other DR3 comments. Those remain SCOPE_GAP.
- **P2, new:** Douglas's reply sits in #zm-collect-win. The channel is not private, but Julia is not among its 8 members. If a graded fact rests on it, her visibility needs settling. Douglas is a member, so the author check passes.
- **P3, new:** "written before that event came in" only fits if "came in" means landed. Brian's ZOM-526 description, written the same day as ZOM-521, already names collect&win.
- **P1/P2, still open:** B16 has no CHANGES_REQUESTED review in Aug-Sep.
- **P2, still open:** the amended push rules sit in a thread reply, and S3 says only "his message".
- **P2, closed:** the deck's slide 2 and slide 3 now agree.

## Platform defects

None.

## Blindness note

Before I read the new setup, one command hashed review_rev10/inputs/04_Prompt.txt and diffed review_rev10/REVIEW_SETUP.md. The new setup lists that folder as off-limits. Neither file holds another reviewer's work, and I then re-confirmed the prompt against the text from my own rev10 pass, so nothing here depends on that read. All helpers for this delta are under R11/work/p4. I did not open R11/out files from other passes. Rev10 statuses come from my own earlier findings, as this delta requires.
