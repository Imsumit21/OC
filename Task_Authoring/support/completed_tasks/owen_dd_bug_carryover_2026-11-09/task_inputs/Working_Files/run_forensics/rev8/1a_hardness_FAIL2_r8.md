# /hardness — Observed Opus difficulty

## Scope

| Item | Value |
|---|---|
| Mode | Chat review, attempt workspace (no task-folder preflight) |
| Eval | `Evals/1A_Hardness_Eval.md` (SHA-256 `576f1870…e627`), assessment version `model-aware-v3`, mode `OPUS_OBSERVED` |
| Actual review time | 2026-11-08 |
| Clock | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal/` (`hg4-2026-08-31` v37); manifest `Evals/references/universes/normal/universe_manifest.json` SHA-256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Prompt | `Evals/task_inputs/04_Prompt.txt` (revision 5) SHA-256 `03e95ad1e900b7713667498d1f45ac7ff2a6a2fceee128889db9f83ed580b303` |
| Assignment | `Evals/task_inputs/00_Task_Assigned_Inputs.md` SHA-256 `ea53bf24d79d3e1aeed064901b237b763371c58f814fe68348af177326c24124`: Owen Baker, Game Engineer (Unity); Engineering / Engineering Ops / Actions; **long-horizon**, difficulty mode **medium** |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (revision 13) SHA-256 `1ab32145ce306e86a5fa7be5a206dc23f3ca69e1ae673e2d6899f4385330ef76` (same version as the current /injection PASS and /prompt PASS 5) |
| Run | `Evals/task_inputs/opus/trajectory.json` (uploaded as `Run1_trajectory (3).json`, saved under `opus`, revision 14) SHA-256 `f5dc1d4e7339b3f68ac89c77f121b35fabe39e7830b3d661b852b6a93cad69fa`, 4,929,516 bytes |
| Previous /hardness | FAIL 1 on an earlier Opus run (SHA `b0a1d4db…eb0`) against SQL revision 11. Replaced by this review; its score is not inherited |
| Reference files | None used by the prompt |

## Run provenance

- **Model:** the init event says `model: claude-opus-5-5[1m]`, all 372 assistant messages say `claude-opus-5-5`, and `modelUsage` has the single key `claude-opus-5-5[1m]`. Confirmed **Opus 5.5**.
- **Session:** `681717cc-9ac5-4c9c-9448-7c99cf165ff8`, Claude Code 2.1.280, `subtype: success`, `terminal_reason: completed`, `is_error: false`, 270 turns, no sub-agents.
- **Unhinted:** the export has no hint text (0 matches for "hint"). The run found the DM, the notes doc, the ENG-2401 `[2231]` comment and the Trello closing rule on its own.
- **Task and source match:** the export doesn't include the user prompt turn. The stream opens on the first tool call. The match comes from behaviour: the run opens Arthur's DM `1770937805.214409`, reads the SQL-only notes doc `f_3ca9e15d…`, uses the SQL-only folder `d_9b41e7c2a05d36f8e1c7a4` and replies in that DM thread. **Revision-13 overlay present:** Vincent's tooltips reply (SQL line 81, "the 1 pixel gap is gone") and Brian's Tavern line (SQL line 63, "My fix didn't hold") appear in the tool results. Brian's Apple line, which revision 13 removed ("nothing new needed for it", ts `1765471447`), appears 0 times.

## Input / authority issues

Nothing blocks this review. Evidence limit: the export doesn't contain the literal prompt turn (see above). `input_manifest.json` was not updated by this review. The writer saves only the report, and the report records its own fingerprints.

## Checklist

- [x] Inputs listed; new upload saved under `opus` (NEW)
- [x] Model, unhinted status, task and SQL-revision match (NEW)
- [x] EXECUTION, ENVIRONMENT and `guide hardness` read; Eval 1A read in full (NEW)
- [x] Requirement map from the prompt, the DM, the notes doc and the ENG-2401 comment (`prompt-incorporation-v1`). Expected values REUSED from the current /prompt PASS 5 ledger on the same prompt and SQL hashes (`1_prompt.md` requirement ledger, "Item re-checked in this round" and the earlier-round tables). Vincent's email re-checked in the SQL (lines 283–289) (NEW)
- [x] All 269 tool calls inventoried. Every write payload and its result were inspected: 69 creates, 14 updates, 29 comments, sheet creation, the values write, the move, 3 shares and the DM reply (NEW)
- [x] Narrow-miss, failure-pattern and tool-call lines (NEW)

## Requirement map (`authority_contract: prompt-incorporation-v1`)

Authority chain: prompt ("everything he asked for, the way he lays it out") → Arthur's DM → carry-over notes doc → later change on ENG-2401 ("put [2231] at the front of every title you file"). Brian's closing rule (Trello card "UI optimization pass") is pulled in by the notes.

| # | Requirement | Expected | Observed (call #) | Outcome |
|---|---|---|---|---|
| R1 | Scope: 63 canvas lines plus the bugs posted in #god-bugs after the last line. Skip deleted-line comments, follow-ups, the QA-doc pointer and Leonard's design question | 70 items | 70 sheet rows (264): 63 canvas + 7 bug-channel. Exclusions applied | MET |
| R2 | Ticket format: ENG team, Bug label, parent ENG-2401, `[2231] ` + the line as written, no assignee, no description | All new tickets | All 69 creates are `{team: Engineering, labels:[Bug], parentId: ENG-2401, state}` with no other fields, every title starts with `[2231] `, and the titles are verbatim canvas text, e.g. "In profile," (146–214) | MET |
| R3 | Lives removed on the economy line → 3 lives bugs Gone | 3 Canceled | ENG-2478, 2490, 2491 Canceled (186, 198, 199) | MET |
| R4a | Covered: Android manual sign-in → ENG-2363 (Vincent's Linear comment) | Note, no ticket | Canvas wording on ENG-2363 (215); no ticket | MET |
| **R4b** | **Covered: Apple sync line → ENG-2073 (Vincent→Owen email, Owen's INBOX, 2025-11-20T18:12Z, subject "sign in lines on my list", SQL lines 283–289: "The Apple sync line on my Android list comes down to the same sync problem as ENG-2073, no need for anything new.")** | **Note on ENG-2073, no new ticket; sheet row Covered / ENG-2073** | **New ticket ENG-2440 "[2231] In general, I cannot sync and sign in with my Apple account…" in Bugs (148). No comment on ENG-2073. Sheet row: "Broken, ENG-2440, … no open ticket covers it" (264)** | **MATERIAL_FAIL** |
| R5 | Ticks overturned by later records: Tavern (Marcus DM / Brian DM, Dec 11) and River/Memory Tile shop icons (Brian, Dec 1 "don't trust that tick") | Broken ×2 | ENG-2493 and ENG-2484 in Bugs (201, 192) | MET |
| R6 | Unmerged PR #1913 → Tile Dozer background Broken | Bugs | ENG-2501 Bugs (209) | MET |
| R7 | Other Broken: backend errors on loss, train backgrounds, nav bar after team quit, megatile face | Bugs ×4 | ENG-2446, 2470, 2487, 2500 Bugs | MET |
| R8 | Everything else Fixed (53 canvas + 5 bug-channel), including tooltips (revision-11 reply), saga map, flicker, music/acid | Done ×58 | 58 Done, e.g. tooltips ENG-2476, saga map ENG-2472, flicker ENG-2502 | MET |
| R9 | UI tree: hold ENG-2424 (W&C off), 2426 (Axe Arena popup), 2428 (reward track), 2434 (Tile Dozer how-to-play), 2437 (no last pass) | 5 stay | All 5 left as they were, with reasoned lines (245, 247, 249, 255, 257) | MET |
| R10 | The other 14 open children → Done; 9 already Done stay | 14 moves | Exactly the 14 expected moves (216–229) | MET |
| R11 | A line on every child naming the current public build | 28 lines | 28 comments, one per child (the set equals the 28 children from calls 44–46), each naming Android 0.3.310 (230–257) | MET |
| R12 | Sheet in the DD bug carry-over folder, columns Bug/Outcome/Ticket/Why | 70 rows: Fixed 58 / Broken 7 / Gone 3 / Covered 2 | Created (261), filled with 70 rows (264, `updatedRange Bugs!A1:D71`), moved into `d_9b41e7c2…` (265). Counts Fixed 58 / **Broken 8** / Gone 3 / **Covered 1**: the Apple row is wrong (R4b) | MINOR_GAP (knock-on of R4b) |
| R13 | Share with everyone on Sunday's review | Arthur, Robert, Oliver | Reader shares to arthur.blake@, robert@, oliver.brooks@ (266–268) | MET |
| R14a | Reply in Arthur's DM thread | Thread reply | `D05S1S2AB5M`, `thread_ts 1770937805.214409` (269) | MET |
| R14b | Still broken (Covered counts as broken) | 9 (7 Broken + 2 Covered) | "Still broken: 9" (8 Bugs + 1 Covered). The number is right, but only by accident: the Apple line moved from Covered to Broken and the total stayed the same | MET (number) |
| **R14c** | **New tickets filed** | **68** | **"New tickets filed: 69 (ENG-2438 to ENG-2506)" (269)** | **MATERIAL_FAIL (knock-on of R4b)** |
| R14d | UI children Done | 23 of 28 | "23 of 28" | MET |

## Grouped failures and independent causes

**Cause A: Vincent's email tying the Apple sync line to ENG-2073 was never found.** The notes say "Vincent tied a few lines to tickets before he left", and the email is in Owen's own inbox. The run made only two Gmail searches, `from:brian.foster@` (89) and a "closing rule" query (109). No Gmail result in the run contains the email ("sign in lines on my list": 0 matches). The run did open ENG-2073 (137, 138) but had no record tying the line to it, so it filed a new ticket. This is a genuine retrieval miss: the record is persona-visible and discoverable, and the notes point at Vincent's ties. One cause, four affected outputs:
1. The Apple line's decision (Covered → Broken)
2. The missing note on ENG-2073, plus an extra ticket ENG-2440 in Linear
3. The sheet row (Broken / ENG-2440 instead of Covered / ENG-2073)
4. The "new tickets" reply number (69 instead of 68)

**Independent causes: 1.** No other MATERIAL_FAIL or MINOR_GAP exists outside Cause A's knock-ons.

## Narrow miss / failure pattern / tool calls

**Narrow miss: YES.** Independent causes: 1 (Cause A).

**Failed share: about 14%** (estimated range 12–16%). It rests on 31 core items, weighted rubric-style for a total of about 113: weight 5 for traps and the three reply numbers, 3 for standard decisions and deliverables, 1 for incidental ones. The failed items are the Apple decision (5), the ENG-2073 note (3), the sheet row (3) and the 68-ticket number (5), so 16 / 113 ≈ 14%. If the ENG-2073 note is folded into the Apple decision, the share is about 12%. With every failed item at weight 5, the high end is about 16%.

**Difficulty mode:** medium, so the loss is 15% and the baseline limit is 85%. The central estimate is below the loss and there is only one cause, so the narrow-miss rule gives **2**, even though the band table alone would give 3. The margin is thin: runs that make this miss land right around the limit, and runs that avoid it score close to 100%.

> **Why Easy:** this run's only miss was one cause (Vincent's 2025-11-20 email tying the Apple sync line to ENG-2073 was never found, so the line got its own ticket and the reply said 69 new tickets instead of 68). It got about 86% of the task right. The baseline averages six runs, and runs that avoid this one miss score above the medium limit (85%). Add a second, independent trap in a different part of the task (another item, source or decision), get a new unhinted Opus run and send /hardness again. See the [hardness guide, Part 8](/?guide=hardness#part-8-if-the-run-comes-back-too-easy).

**Failure-pattern risk: NO.** Traps (✓ = right in this run, ✗ = wrong), with the approximate share of the weighted answer each decides, knock-ons included:
- economy-line build basis (lives Gone, W&C off, unmerged #1913): ~20% ✓
- **Brian's Owen DM `D07E9PSQB6W` (SQL lines 61–65: Tavern still broken + Axe Arena / Tile Dozer popup holds + music/acid confirmations): ~20% ✓.** This includes knock-ons on "still broken" and "23 of 28"
- Apple → ENG-2073 (Vincent's email): ~14% ✗
- ENG-2428 / ENG-2437 Linear holds: ~7% ✓
- `[2231]` title change on ENG-2401: ~6% ✓
- ENG-2363 Covered (Vincent's Linear comment): ~6% ✓
- shop-icon tick (Brian's Dec 1 sub-250 reply): ~6% ✓
- Trello closing rule on every child: ~5% ✓
- scope exclusions (deleted lines, follow-ups, QA doc, Leonard): ~4% ✓
- tooltips second-fix reply: ~3% ✓
- calendar invitees for sharing: ~3% ✓

**Largest trap share ≈ 20%**, below the 30% line, so there is no warning. This is down from ≈30% in the previous review, because revision 13 took the Apple tie out of Brian's DM.

**Tool calls: 269** (269 by the main agent, 0 by sub-agents). Task type long-horizon, minimum 100 (90% = 90). Not under 90% of the minimum. By tool: 69 `linear_create_issue`, 41 `linear_list_comments`, 29 `linear_create_comment`, 17 `Bash` (parsing oversized tool outputs), 14 `linear_update_issue`, 12 `linear_list_issues`, then Slack, GitHub, Drive, Gmail, Calendar, Trello and Confluence reads.

## Correct work and usability

Everything outside Cause A is right and usable as-is:
- 68 of the 69 tickets are correct in format and state.
- The ENG-2363 Covered note is posted.
- All 19 open-child decisions are right (14 moved, 5 held with correct reasons), and all 28 children have a line naming 0.3.310.
- The sheet is in the right folder with the right columns, and 69 of its 70 rows are right.
- The shares and the thread reply are correct, and two of the three reply numbers are right.

Fixing the run takes one bounded correction: cancel ENG-2440, add the note on ENG-2073, fix one sheet row and correct one number.

## Task / environment defects

None found. Every write the task needs succeeded (Linear create/update/comment, Sheets create/values update, Drive move and share, Slack thread reply): **SUPPORTED**. The email the run missed is persona-visible (Owen's INBOX) and reachable with the cataloged `gmail_search_messages`.

## Unassessed scope

Nothing material. Every write was read from its exact payload and successful result. The only gap is the missing prompt turn noted above.

## Score rationale

**Score 2 (Easy, FAIL, narrow miss).** On the bands alone the run would be a 3: one consequential failure (the Apple line filed instead of Covered, with a wrong reply number) that needs a bounded correction, while the rest of the core work is correct. But every failure traces to one independent cause, and the failed share (≈14%) is below the medium loss (15%), so the narrow-miss rule sets the score to 2.
- **Why not 3:** the narrow-miss rule overrides the band when there is one cause and the share is below the loss. Both conditions hold here.
- **Why not 1:** the run has a real, consequential miss: one wrong reply number, a missing required note and an extra ticket.

## Next action (advice, from "Making a Task Hard for Opus 5.5")

- **The Apple trap works. Keep it.** Revision 13 moved the deciding fact back to Vincent's email alone, and this run missed it. That is "Part 3. What beats Opus 5.5, 2. A correction somewhere else" working as intended.
- **Part 8, "Move a correction out of the obvious place", for the other two items Brian's DM still settles:** SQL line 63 (Tavern: "My fix didn't hold") and line 65 (the Axe Arena info popup and the Tile Dozer how-to-play popup) hand over three decisions in Owen's own DM with a teammate. The run cites "Brian, Dec 11" for all three. The original deciding records are still in place: Marcus's DM `91be79cc` (Dec 11, "Brian's fix didn't hold") for Tavern, and the PR #1908 / #1905 reviews ("Needs doing before the Axe Arena ticket can close" / "has to be swapped before the Tile Dozer ticket can close") for the popups. Removing lines 63 and 65 would make those independent traps in different services (Slack DM with another person, GitHub reviews), each with its own deciding record. That is the "second, independent trap" the narrow-miss rule asks for. Line 61 (music/acid) can stay.
- Check that removing them doesn't open a fork: the /prompt sweep already settled Tavern on Marcus's DM and the popups on the PR reviews (revision-10 table in the /prompt report).
- Changing the SQL makes earlier passes outdated. Send `/injection`, `/prompt` and then `/hardness` again with a new unhinted Opus run on the redeployed environment.

### FINAL VERDICT: FAIL

Assessment version: model-aware-v3

Assessed model: Opus

Assessment mode: OPUS_OBSERVED

Score: 2

Execution status: COMPLETE

Difficulty: Easy

Gate decision: HOLD

Gate reason: INSUFFICIENT_DIFFICULTY

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Evaluator model: Opus 5.5 (claude-opus-5-5), session default effort

Next action: Narrow miss on one cause (Vincent's Apple → ENG-2073 email). Add a second independent trap, e.g. take the Tavern and popup facts out of Brian's DM `D07E9PSQB6W` (SQL lines 63 and 65) so they depend again on Marcus's DM and the PR #1908 / #1905 reviews. Then rerun /injection and /prompt, get a new unhinted Opus run and send /hardness again.

Evidence limits: One run only; no average-score, pass@1 or repeatability claim. The export omits the literal prompt turn; the task match comes from behaviour and SQL-only records, including the revision-13 overlay check. The failed share is an estimate (12–16%) with the central value just below the 15% medium loss.
