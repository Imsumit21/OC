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
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (revision 15) SHA-256 `ea5b542897c846d955d1361bd50ed2531214044b53e229fc032b2c55bbbd2504` (same version as the current /injection PASS and /prompt PASS) |
| Run | `Evals/task_inputs/opus/trajectory.json` (uploaded as `Run1_trajectory (4).json`, saved under `opus`, revision 16) SHA-256 `d8b88c21f1cf5837a6042502fb94a5db08320e8726f1b0efb3acc24f9d213a14`, 5,909,408 bytes |
| Previous /hardness | FAIL 2 (narrow miss) on the previous Opus run (SHA `f5dc1d4e…a9fa`) against SQL revision 13. Replaced by this review; its score is not inherited |
| Reference files | None used by the prompt |

## Run provenance

- **Model:** the init event says `model: claude-opus-5-5[1m]`, all 406 assistant messages say `claude-opus-5-5`, and `modelUsage` has the single key `claude-opus-5-5[1m]` (`canonicalModel: claude-opus-5-5`). Confirmed **Opus 5.5**.
- **Session:** `f97d74d2-4dac-4fe6-9391-a3a988b19006`, Claude Code 2.1.280, `subtype: success`, `terminal_reason: completed`, `is_error: false`, 289 turns, no sub-agents (`subagent_stats.spawned: 0`).
- **Unhinted:** the export has no hint text (0 matches for "hint"). The run found Arthur's DM, the notes doc, the ENG-2401 `[2231]` comment and the Trello closing rule on its own.
- **Task and source match:** the export doesn't include the user prompt turn; the stream opens on the first tool call. The match comes from behaviour: the run opens Arthur's DM thread `D05S1S2AB5M / 1770937805.214409` (call 4), reads the SQL-only notes doc `f_3ca9e15d7b20f4e681ad52` (7) and the ENG-2401 `[2231]` comment (10), uses the folder `d_9b41e7c2a05d36f8e1c7a4` and replies in that DM thread (288). **Revision-15 overlay present:** Brian's new Daily Gift line ("Daily Gift isn't finished either…", SQL line 65) appears in the DM read at call 96 (6 matches), the popup line without its leading "And" appears (SQL line 63), and Brian's removed Tavern line ("My fix didn't hold", revision 13 only) appears 0 times. Vincent's tooltip reply (SQL line 81, "1 pixel gap is gone") is present.

## Input / authority issues

Nothing blocks this review. Evidence limit: the export doesn't contain the literal prompt turn (see above). `input_manifest.json` was not updated by this review; the writer saves only the report, and the report records its own fingerprints.

## Checklist

- [x] Inputs listed; new upload saved under `opus` (revision 16) (NEW)
- [x] Model, unhinted status, task and SQL-revision match (NEW)
- [x] `guide hardness` shared sections read; Eval 1A read in full (NEW)
- [x] Requirement map from the prompt, the DM, the notes doc and the ENG-2401 comment (`prompt-incorporation-v1`). Expected values REUSED from the current /prompt PASS on the same prompt and SQL hashes (revision-15 ledger: 70 items, Fixed 58 / Broken 7 / Gone 3 / Covered 2; reply 9 / 68 / 23 of 28; Tavern stays Broken on Marcus's DM; ENG-2437 held on Brian's new DM line). The two deciding records the run missed were re-read in the SQL: Marcus's DM (line 59) and Vincent's email (lines 283–289). Owen's membership of DM `D05USBTQY1F` re-checked in base `slack/channels.json` (members include `EMPLOYEE_0021_SLACK_ID` = Owen, per call 1) (NEW)
- [x] All 288 tool calls inventoried. Every write payload and result inspected: 69 creates, 14 updates, 29 comments, sheet creation in the folder, the values write (71 rows), 3 shares and the DM reply (NEW)
- [x] Sheet rows compared row-by-row with the previous run's sheet (whose rows the previous review checked against the /prompt ledger): the same 70 bug texts, and only the Tavern row's outcome differs (NEW)
- [x] Narrow-miss, failure-pattern and tool-call lines (NEW)

## Requirement map (`authority_contract: prompt-incorporation-v1`)

Authority chain: prompt ("everything he asked for, the way he lays it out") → Arthur's DM → carry-over notes doc → later change on ENG-2401 ("put [2231] at the front of every title you file"). Brian's closing rule (Trello card "UI optimization pass", 2025-11-05: "every one gets a note naming the current public build") is pulled in by the notes.

| # | Requirement | Expected | Observed (call #) | Outcome |
|---|---|---|---|---|
| R1 | Scope: 63 canvas lines plus the bugs posted in #god-bugs after the last line; skip deleted-line comments, follow-ups, the QA-doc pointer and Leonard's design question | 70 items | 70 sheet rows (284), the same 70 texts as the previous verified run | MET |
| R2 | Ticket format: ENG team, Bug label, parent ENG-2401, `[2231] ` + the line as written, no assignee, no description | All new tickets | All 69 creates have exactly `{team: Engineering, labels:[Bug], parentId: ENG-2401, state, title}`; every title starts with `[2231] ` and keeps the text verbatim (e.g. "In profile,", "Tavern buttons lost its frame. @Owen Baker") (166–234) | MET |
| R3 | Lives removed on the economy line → 3 lives bugs Gone | 3 Canceled | ENG-2492, 2493, 2494 Canceled (220–222) | MET |
| R4a | Covered: Android manual sign-in → ENG-2363 (Vincent's Linear comment) | Note, no ticket | Canvas wording on ENG-2363 (235); no ticket | MET |
| **R4b** | **Covered: Apple sync line → ENG-2073 (Vincent→Owen email, Owen's INBOX, 2025-11-20T18:12Z, subject "sign in lines on my list", SQL lines 283–289: "The Apple sync line on my Android list comes down to the same sync problem as ENG-2073, no need for anything new.")** | **Note on ENG-2073, no new ticket; sheet row Covered / ENG-2073** | **New ticket ENG-2499 "[2231] In general, I cannot sync and sign in with my Apple account…" in Bugs (227). ENG-2073 was opened (139, 140) but got no comment. Sheet row Broken / ENG-2499 (284)** | **MATERIAL_FAIL** |
| **R5a** | **Tavern tick overturned: Marcus→Owen DM `D05USBTQY1F`, 2025-12-11T11:20:12Z (SQL line 59): "the Tavern buttons lost their frame again on last night's Android build, I looked at the prefab and Brian's fix didn't hold". The Dec 10 Android builds are EconomyChanges; nothing later names a Tavern fix** | **Broken → Bugs; sheet row Broken** | **ENG-2444 filed Done (172). Sheet row "Fixed, ENG-2444, Tick stands on the canvas; no later record says otherwise. Brian sent the fix (Nov 20)" (284). The run never searched "Tavern" and never opened DM `D05USBTQY1F`** | **MATERIAL_FAIL** |
| R5b | River/Memory Tile shop icons tick overturned (Brian, Dec 1 "don't trust that tick") | Broken | ENG-2496 Bugs (224) | MET |
| R6 | Unmerged PR #1913 → Tile Dozer background Broken | Bugs | ENG-2501 Bugs (229) | MET |
| R7 | Other Broken: backend errors on loss, train backgrounds, nav bar after team quit, megatile face | Bugs ×4 | ENG-2498, 2497, 2495, 2500 Bugs | MET |
| R8 | Everything else Fixed (52 canvas + 5 bug-channel, excluding Tavern), incl. tooltips (second-fix reply), saga map, flicker, music/acid | Done | Done for each, e.g. flicker ENG-2502, music ENG-2503, acid ENG-2504 | MET |
| R9 | UI tree: hold ENG-2424 (W&C off), 2426 (Axe Arena popup), 2428 (reward track), 2434 (Tile Dozer how-to-play), 2437 (Daily Gift last pass, Brian's new DM line) | 5 stay | All 5 left as they were, with reasoned lines (264–268); ENG-2437 cites "per Brian (Dec 11) the Daily Gift panel never got its last pass" | MET |
| R10 | The other 14 open children → Done; 9 already Done stay | 14 moves | ENG-2410, 2414, 2415, 2417, 2418, 2419, 2425, 2427, 2429, 2430, 2431, 2432, 2433, 2435 → Done (236–249) | MET |
| R11 | A line on every child naming the current public build (Brian's rule) | 28 lines | 28 comments, one per child (250–277), each naming Android 0.3.310 | MET |
| R12 | Sheet in the DD bug carry-over folder, columns Bug/Outcome/Ticket/Why | 70 rows: Fixed 58 / Broken 7 / Gone 3 / Covered 2 | Created directly in `d_9b41e7c2…` (280), filled `Sheet1!A1:D71` (284). Counts Fixed **59** / Broken 7 / Gone 3 / Covered **1**: the Apple and Tavern rows are wrong (R4b, R5a) | MINOR_GAP (knock-on of R4b, R5a) |
| R13 | Share with everyone on Sunday's review | Arthur, Robert, Oliver | Reader shares to arthur.blake@, robert@, oliver.brooks@ (285–287) | MET |
| R14a | Reply in Arthur's DM thread | Thread reply | `D05S1S2AB5M`, `thread_ts 1770937805.214409`, `ok: true` (288) | MET |
| **R14b** | **Still broken (Covered counts as broken)** | **9 (7 Broken + 2 Covered)** | **"Still broken: 8" (7 Bugs + 1 Covered) (288)** | **MATERIAL_FAIL (knock-on of R5a; R4b only moved the Apple line between Covered and Broken)** |
| **R14c** | **New tickets filed** | **68** | **"New tickets filed: 69 (ENG-2438 to ENG-2506)" (288)** | **MATERIAL_FAIL (knock-on of R4b)** |
| R14d | UI children Done | 23 of 28 | "23 of 28", with the 5 open ones named correctly | MET |

## Grouped failures and independent causes

**Cause A: Vincent's email tying the Apple sync line to ENG-2073 was never found (Gmail).** The notes say "Vincent tied a few lines to tickets before he left", and the email is in Owen's own INBOX. The run made three Gmail searches, none of which could match it: `from:brian.foster@` (60), "UI tickets" (100) and a "brian closing OR rule OR UI" query (118). "sign in lines on my list" appears 0 times in the export. The run opened ENG-2073 (139, 140) but had no record tying the line to it, so it filed a new ticket. Affected outputs:
1. The Apple line's decision (Covered → Broken)
2. The missing note on ENG-2073, plus an extra ticket ENG-2499
3. The sheet row (Broken / ENG-2499 instead of Covered / ENG-2073)
4. The "new tickets" reply number (69 instead of 68)

**Cause B: Marcus's Dec 11 DM overturning the Tavern tick was never found (Slack DM).** The notes say "A tick on the canvas stands unless a later record about that bug says otherwise." Marcus's message is in DM `D05USBTQY1F`, which Owen is a member of, and says Brian's fix didn't hold on the Dec 10 Android (EconomyChanges) build. The run never searched for "Tavern" (no tool input contains it outside the writes) and never opened that DM. It stopped at the canvas thread ("Brian sent the fix (Nov 20)"), which the Dec 11 record overrides. Affected outputs:
1. The Tavern decision (Broken → Fixed) and ticket ENG-2444 filed Done instead of Bugs
2. The sheet row (Fixed instead of Broken)
3. The "still broken" reply number (8 instead of 9)

**Independent causes: 2.** They rest on different deciding records in different services (a Gmail message vs a Slack DM with another person), about different items, and a run could make either miss without the other. No other MATERIAL_FAIL or MINOR_GAP exists outside their knock-ons.

## Narrow miss / failure pattern / tool calls

**Narrow miss: NO.** Independent causes: 2.

**Failed share: about 26%** (estimated range 22–29%). It rests on the same 31 core items as the previous review, weighted rubric-style for a total of about 113: weight 5 for traps and the three reply numbers, 3 for standard decisions and deliverables, 1 for incidental ones. Cause A: Apple decision (5) + ENG-2073 note (3) + sheet row (3) + 68-ticket number (5) = 16. Cause B: Tavern decision and ticket state (5) + sheet row (3) + still-broken number (5) = 13. Total 29 / 113 ≈ 26%. Folding the ENG-2073 note into the Apple decision and weighting the sheet rows at 1 gives about 22%; weighting every failed item at 5 gives about 29%.

**Difficulty mode:** medium, so the loss is 15% and the baseline limit is 85%. The central estimate and the low end are both above the loss, and there are two causes, so the narrow-miss rule does not apply; the score comes from the bands.

**Failure-pattern risk: NO.** Traps (✓ = right in this run, ✗ = wrong), with the approximate share of the weighted answer each decides, knock-ons included:
- economy-line build basis (lives Gone, W&C off, unmerged #1913): ~20% ✓
- Brian's Owen DM `D07E9PSQB6W` (SQL lines 61–65: popup holds ENG-2426/2434, Daily Gift hold ENG-2437, music/acid confirmations), including the knock-on on "23 of 28": ~18% ✓. The popups are also settled by the PR #1908 / #1905 reviews, so a run that misses the DM can still get them right
- Apple → ENG-2073 (Vincent's email): ~14% ✗
- Tavern → Marcus's DM `D05USBTQY1F` (SQL line 59): ~12% ✗
- ENG-2428 Linear hold (Oliver's note): ~5% ✓
- `[2231]` title change on ENG-2401: ~6% ✓
- ENG-2363 Covered (Vincent's Linear comment): ~6% ✓
- shop-icon tick (Brian's Dec 1 sub-250 reply): ~6% ✓
- Trello closing rule on every child: ~5% ✓
- scope exclusions (deleted lines, follow-ups, QA doc, Leonard): ~4% ✓
- tooltips second-fix reply: ~3% ✓
- calendar invitees for sharing: ~3% ✓

**Largest trap share ≈ 20%**, below the 30% line, so there is no warning.

**Tool calls: 288** (288 by the main agent, 0 by sub-agents). Task type long-horizon, minimum 100 (90% = 90). Not under 90% of the minimum. By tool: 69 `linear_create_issue`, 40 `linear_list_comments`, 29 `linear_create_comment`, 15 `slack_search_public_and_private`, 14 `linear_list_issues`, 14 `linear_update_issue`, 13 `slack_read_channel`, 13 `Bash` (parsing oversized tool outputs), 11 `slack_conversations_search_messages`, then GitHub, Drive, Gmail, Calendar, Trello and Confluence reads.

## Correct work and usability

Everything outside Causes A and B is right and usable as-is:
- 67 of the 69 tickets are correct in format and state (ENG-2499 shouldn't exist; ENG-2444 has the wrong state). Format is correct on all 69.
- The ENG-2363 Covered note is posted.
- All 19 open-child decisions are right (14 moved, 5 held with correct reasons, including the new Daily Gift hold), and all 28 children have a line naming 0.3.310.
- The sheet is in the right folder with the right columns, and 68 of its 70 rows are right.
- The shares and the thread reply destination are correct; one of the three reply numbers ("23 of 28") is right.

Fixing the run takes a bounded set of corrections: cancel ENG-2499 and add the note on ENG-2073; move ENG-2444 to Bugs; fix two sheet rows; correct two of the three reply numbers.

## Task / environment defects

None found. Every write the task needs succeeded (Linear create/update/comment, Drive create in folder, Sheets values update, Drive share, Slack thread reply): **SUPPORTED**. Both missed records are persona-visible and reachable with cataloged tools: Vincent's email in Owen's INBOX (`gmail_search_messages`), and Marcus's message in DM `D05USBTQY1F`, of which Owen is a member (`slack_search_public_and_private` / `slack_read_channel`).

## Unassessed scope

Nothing material. Every write was read from its exact payload and successful result. The only gap is the missing prompt turn noted above.

## Score rationale

**Score 3 (Hard, NON-FAIL).** Two independent genuine retrieval misses (Vincent's Apple email in Gmail, Marcus's Tavern DM in Slack) produce consequential failures: two of the 70 bug decisions are wrong, one extra ticket exists, a required Covered note is missing, and two of the three numbers Arthur asked for are wrong. The correction is bounded (about six small edits), and the substantial core work (the other 68 decisions, all ticket formatting, the whole UI tree, the sheet location and sharing, the thread reply) is correct and usable.
- **Why not 2:** there are two independent causes and the failed share (≈26%) is above the medium loss (15%), so the narrow-miss rule does not apply, and these are consequential errors, not minor ones.
- **Why not 4:** the needed correction is a handful of targeted edits, not substantial rework across the result; 68 of 70 items, all 19 UI decisions and all 28 child lines stand.

## Next action (advice, from "Making a Task Hard for Opus 5.5")

- The revision-15 change worked: taking Brian's Tavern line out of his DM made the Tavern tick depend again on Marcus's DM alone, and this run missed it ("Part 3. What beats Opus 5.5, 2. A correction somewhere else"). Together with the Apple trap that is two independent traps in different services.
- Proceed to the dependent stages. Keep the rubric and OEs aligned with the current expected answers: 9 still broken (7 Broken + 2 Covered), 68 new tickets, 23 of 28.
- If you change the SQL again, earlier passes become outdated: send `/injection`, `/prompt` and `/hardness` again with a new unhinted Opus run.

### FINAL VERDICT: NON-FAIL

Assessment version: model-aware-v3

Assessed model: Opus

Assessment mode: OPUS_OBSERVED

Score: 3

Execution status: COMPLETE

Difficulty: Hard

Gate decision: PROCEED

Gate reason: OBSERVED_OPUS_FAILURE

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Evaluator model: Opus 5.5 (claude-opus-5-5), session default effort

Next action: Proceed with dependent authoring (OEs, rubric); retain the observed failure evidence (Apple → ENG-2073 email missed; Tavern → Marcus's Dec 11 DM missed).

Evidence limits: One run only; no average-score, pass@1 or repeatability claim. The export omits the literal prompt turn; the task match comes from behaviour and SQL-only records, including the revision-15 overlay check. The failed share is an estimate (22–29%).
