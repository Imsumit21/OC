## Self-review

**1. Re-read as the eval** (2_Oracle_Events_Eval.md, in order, against this report):
- **Phase 1.2 inventory.** All @@NEV@@ segments are STEP. There are no headers, notes, response descriptions or non-actions.
- **Phase 1.3 five fields.** Every read names its service, what it reads and its search, thread or pointer. The two decision steps cite the events they use; their tool is not applicable. Every write names its target, its fields and its service; the sign-off lists the catalog tool and its required parameters.
- **HARD GATE.** No event says what the agent refrains from doing or what the final answer says. The round-1 wordings that read as non-actions ("The 9 already Done stay.", "No new ticket for this line.") are gone.
- **Phase 2.1–2.6.**
  - Service: every value is read where it lives. Build membership is read from #builds (Android EconomyChanges lines), #engineering-bots (the develop push), GitHub (the develop merge and PR #1916).
  - Tools: all are cataloged (Evals/references/tools/catalog.json), including github_search_commits and github_get_pull_request.
  - Parameters: thread_ts 1770937805.214409; folder d_9b41e7c2a05d36f8e1c7a4; the three attendee addresses from evt_6e2c91d4b07f3a58c1d2e4.
  - Expected data: re-read below.
  - Clock: every record time is at or before 2026-02-14T00:00:00Z. Sunday's review (Feb 15 17:00Z) is a semantic future date and is not expected as done.
  - Act-vs-defer: ledger §C, no hold.
- **Phase 2.7 format.** One action per event, numbered, with a service; no arrows and no JSON.
- **Phase 3.1–3.6.** R1–R10 are covered by route. Platform round 1's two missing steps (R20 near-miss tickets, R21 build evidence for the treasure and bottom bar fixes) now have their own reads, and the decision step cites them. Every search term comes from the prompt or an earlier event.
- **Phase 4.0** is the 8-row sweep above.

**2. Counter-readings** (one per Coverage row, one per Finding, plus the value judgements the prediction rests on):

| Judgement | Counter-reading (strongest case against) | Resolution (evidence) |
|---|---|---|
| R1 covered (OE 1) | The best case it is missing: the agent reads an older Arthur DM. | D05S1S2AB5M holds Owen and Arthur; the Thursday message is ts 1770937805.214409 (SQL L55), the one about moving DD's bug list into Linear. Holds. |
| R2 covered (OEs 1–6) | The best case it is partial: the notes point at Brian's rule without naming the card. | OE 4 finds the card by the master's name, its description says "Tickets are under the UI Changes master." (SQL L210). Holds. |
| R3 covered | The best case it is partial: an item's outcome rests on a fix that never reached 0.3.310, or a Broken item is really Covered. | Round 1 found both gaps. Build reads now back every "later record says fixed" item (OE 17 #2297, OEs 19–21) and OE 26 rules out the six near-miss tickets (SQL L325–L335). Holds. |
| R4 covered | The best case it is missing: titles drop the prefix or the two tied lines get tickets. | OE 3 gives the [2231] prefix (SQL L311); OE 30 gives the fields; OEs 100 and 101 note ENG-2073 and ENG-2363 instead of filing. 68 creates counted. Holds. |
| R5 covered | The best case it is wrong: ENG-2432 and ENG-2433 should stay because of the shop icons regression. | OE 2 now quotes "A bug on a screen doesn't hold its child, that's what the bug ticket is for." (SQL L14), cited in OE 31. Holds. |
| R6 covered | The best case it is partial: lines only on moved children, or no build named. | 28 line events, each naming 0.3.310, per Brian's rule (SQL L215) and the notes (SQL L14). Holds. |
| R7 covered | The best case it is wrong: the sheet lands outside the folder. | The move event sets the parent to d_9b41e7c2a05d36f8e1c7a4 (SQL L3); creating it in the folder directly is an equal route. Holds. |
| R8 covered | The best case it is wrong: Owen is also shared, or someone else is on the review. | The event's attendees are Arthur, Robert, Oliver and Owen (SQL L309); three shares. Holds. |
| R9 covered | The best case it is wrong: "still broken" is 7. | The notes: "When you report back, Covered ones count as still broken." (SQL L14): 9. Holds. |
| R10 covered (constraint) | The best case it needs a step. | The review starts 2026-02-15T17:00:00Z (SQL L309), after the clock; every write runs now. Holds. |
| X1 OE 26 | The best case it was never needed: the near-miss tickets are obviously different. | Platform round 1 scored it FAIL 2 because Covered comes before Broken in the notes and the six tickets were planted near the seven items; the read is now explicit, with Arthur's comments verbatim (SQL L325–L335). Fixed. |
| X2 OE 20 | The best case it was fine: Brian's "I send the fix" is a later record. | The notes add "A fix only counts once it is in that build"; the Dec 17 merge of develop into EconomyChanges (hg.py github /commits/252) carries the Dec 2 develop commit. Fixed. |
| X3 OE 21 | The best case it was fine: Brian closed the thread. | Same rule; PR #1916 merged into EconomyChanges on Dec 26 (hg.py github /pull_requests/1046), before Brian's Dec 29 close. Fixed. |
| X4 OE 17 | The best case the iOS line was enough. | The rule goes by the Android build; #2297 Android EconomyChanges lists the flicker, acid and music fixes (hg.py #builds 2025-12 /116). Fixed. |
| X5 OE 13 | The best case it was MINOR only. | It was MINOR on round 1, but a wrong author is a value the record contradicts; parent user EMPLOYEE_0016 = Robert (hg.py C09Q4S613CN 2025-11 /242). Fixed. |
| X6 OE 8 | The best case a reader finds the lines anyway. | The cited range now matches the canvas creates and the two note events; line 3 is CE156FDFB428/1763041538.186339 and line 29 CE156FDFB428/1763132009.017599. Fixed. |
| X7 OE 13 | The best case the tick date is close enough. | No tool returns when a box was ticked; the line's post time is observable (root ts 1763549455.195819). Fixed. |
| X8 OE 2 | The best case OE 31 is self-evident. | Without this sentence a reviewer reads the shop regression as UI work missing from the build; now quoted (SQL L14). Fixed. |
| X9 OE 2 | The best case a truncated quote is harmless. | The cut clause is the commit rule a reviewer checks the train line against (SQL L14); now quoted whole. Fixed. |
| X10 OE 16 | The best case Leonard's Dec 1 post was enough. | Round 1's deep recheck accepted it, but the shipped removal (#2299, Leonard's Dec 16 notes) closes the gap for Gone (C05433XK267/1765397569.397939, C9CA62B5180A/1765933143.608699). Fixed. |
| X11 OE 31 | The best case "stay" is an end state. | The blind reviewer flagged it as a possible non-action; rephrased as the end count (ledger F-row for the tree, ENG-2409 to ENG-2437). Fixed. |
| X12 OE 22 | The best case "music" is a natural search. | It put the target 111th of 618 Owen-visible hits (plan/oe_locator_ranks.json); a direct read of Brian's DM, motivated by OEs 4 and 11, is sounder. Fixed. |
| X13 OE 23 | The best case "from Vincent" is enough. | 174 base messages match Vincent's address, mostly invites (plan/oe_locator_ranks.json); narrowed to his mail about signing in, owen.baker@harmonygames.co/1849333980856689601. Fixed. |
| X14 OE 12 | The best case a search hit shows base and head. | The PR read returns them (hg.py github data.json /pull_requests/1043); the event now names it. Fixed. |
| X15 OE 18 | The best case the hit shows its parent. | Search hits do not carry the parent text; the events now open the thread to reach C09Q4S613CN/1764013100.931229 and C09Q4S613CN/1764042435.541279. Fixed. |
| X16 OE 19 | The best case "the day before" is a harmless slip. | The two times are 8:56 AM and 4:29 PM PT the same day (C050WGU41HR/1764694580.083459, C9CA62B5180A/1764721779.638599); a wrong date is INACCURATE under the Minor test. Fixed. |
| X17 OE 26 | The best case "Bugs and Todo" was a fair shorthand for open. | Round 2 flagged it as narrower than "open"; the event now names all seven open states, which exist in hg.py linear data.json state_id values, and the six narrowed tickets (ENG-2406, ENG-2181, ENG-2351, ENG-2280, ENG-2281, ENG-2398) stay the only near-misses. Fixed. |
| X18 OE 17 | The best case the failed status is irrelevant because the changes list shows the branch. | True for the branch, but leaving out "Still Failing" while quoting #2299's "Success" misstated #2297 (C05433XK267/1765310444.095399); OE 30 no longer says the fixes are in that build. Fixed. |
| X19 OE 30 | The best case "never merged" is safe because the PR is open at the clock. | It is, but the record's own state is "open" with merged False (hg.py github data.json /pull_requests/1043); the event now uses that. Fixed. |
| OE 30 the 53 tick-stands lines | The best case some need a build check. | The notes' Fixed test is "the tick stands, or a later record says it was fixed"; the build rule binds fixes found by later records (SQL L14). Round 1 found no defect here. Holds. |
| OE 30 Tavern Broken | The best case the fix held: Brian sent it Nov 20. | Marcus's Dec 11 DM (SQL L58) says it lost its frame again and Brian's fix didn't hold. Holds. |
| OE 31 ENG-2437 held | The best case it is Done: Brian promised it Nov 19. | His Dec 11 line (SQL L64) says the panel never got its last pass, later than the Nov 19 plan (hg.py D07E9PSQB6W 2025-11 /20). Holds. |
| Visibility | The best case a read is hidden from Owen. | persona_view check-sql shows every load-bearing seeded row YES; can-see YES for every base record cited (08_OE_Writing_Ledger.md §B proof). Holds. |

**3. Re-verify.**
- **Base records.** Re-read in this run through tools/hg.py: plan/oe_reads.py (the canvas channel's and the bug channel's month files read whole, single messages by lookup and get-many, 40 Linear issues field by field, 4 PRs, the merge commit, 3 contacts, the economy doc).
- **Seeded records.** Parsed from 01_Universe_Inject.sql as text.
- **Rebuild.** plan/assemble_oe_events.py rebuilt the file and asserted 162 quoted substrings against their own records before writing.
- **New reads in this check:** #builds 2025-12 /116 and /146; #engineering-bots commit fbe7bdea; the group DM 2025-12 /37 and /911; github /commits/252 and /pull_requests/1046; ENG-2406, ENG-2181, ENG-2351, ENG-2280, ENG-2281, ENG-2398; plan/oe_locator_ranks.json.
- **Recomputed.** 69 roots, 63 lines, 55 ticked, 8 unticked; 58 / 7 / 3 / 2; 68 tickets; 19 open − 5 held = 14; 9 + 14 = 23.

**4. Fixes.** Every corrected span in the Findings table was grounded in a record re-read this run (its Evidence column). The events file was rewritten only through the builder, so the quote asserts held after every edit.

**5. Blind reviewer and platform round 1.** An independent agent read only the prompt, the events, the SQL and the eval rules, verifying values through hg.py and persona_view with Working_Files closed to it. It found one wrong author (X5), four MINOR items (X6–X10) and a non-action risk (X11), and confirmed every title, count, quote, time and author otherwise. Platform /oe round 1 (FAIL 2: Completeness 2, Accuracy 3) raised X1–X6 on the 146-event draft; round 2 (NON-FAIL 3: Completeness 5, Accuracy 3, sha 250fa6b2c682) raised X17 and X18. All are fixed.

**6. Record.**
- **Prediction:** Completeness 5 (no INCOMPLETE item remains, and no non-action or final-response event); Accuracy 5 (no INACCURATE, MINOR or format item remains); /oe PASS 5; Path feasibility SUPPORTED; Task solvability SUPPORTED_BY_OE.
- **Residual risk (not a finding):** a fresh reviewer may ask for build evidence on other items; every item whose outcome rests on a later fix now has it, and the tick-stands lines need none under the notes.
- **File:** 08_Oracle_Events.md sha256 @@OESHA@@, @@NEV@@ events, @@OECHARS@@ characters. Type it into the platform exactly as written.
- **Unresolved: none.**
