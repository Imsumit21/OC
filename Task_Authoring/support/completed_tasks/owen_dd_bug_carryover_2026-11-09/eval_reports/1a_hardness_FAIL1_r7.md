# /hardness — Observed Opus difficulty

## Scope

| Item | Value |
|---|---|
| Mode | Chat review, attempt workspace (no task-folder preflight) |
| Eval | `Evals/1A_Hardness_Eval.md`, assessment version `model-aware-v3`, mode `OPUS_OBSERVED` |
| Actual review time | 2026-11-08 |
| Clock | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal/` (`hg4-2026-08-31` v37); manifest `Evals/references/universes/normal/universe_manifest.json` SHA-256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Prompt | `Evals/task_inputs/04_Prompt.txt` (revision 5) SHA-256 `03e95ad1e900b7713667498d1f45ac7ff2a6a2fceee128889db9f83ed580b303` |
| Assignment | `Evals/task_inputs/00_Task_Assigned_Inputs.md` SHA-256 `ea53bf24d79d3e1aeed064901b237b763371c58f814fe68348af177326c24124`: Owen Baker, Game Engineer (Unity); Engineering / Engineering Ops / Actions; **long-horizon**, difficulty mode **medium** |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (revision 11) SHA-256 `f9555a3cf6fcbbc649e18ee842a75ad00ea7da4cfe3071210a65b3e3ca26cadd` (same version as the current /injection PASS and /prompt PASS 5) |
| Run | `Evals/task_inputs/opus/trajectory.json` (uploaded as `Run1_trajectory (2).json`, saved under `opus`, revision 12) SHA-256 `b0a1d4db639b2da221cde7b97b0323164ebeece5dd9dd02358dcf45986742eb0`, 5,635,350 bytes |
| Previous /hardness | NON-FAIL 4 on an earlier Opus run (SHA `27fb0c6d…5a3`) against SQL revision 8. Replaced by this review; its score is not inherited |
| Reference files | None used by the prompt |

## Run provenance

- **Model:** the init event says `model: claude-opus-5-5[1m]`, all 439 assistant messages say `claude-opus-5-5`, and `modelUsage` has the single key `claude-opus-5-5[1m]`. Confirmed **Opus 5.5**.
- **Session:** `1ee3960c-6f27-4a48-aa24-42f36079ec90`, Claude Code 2.1.280, `subtype: success`, `terminal_reason: completed`, `is_error: false`, 360 turns, no sub-agents.
- **Unhinted:** the export has no hint text (0 matches for "hint"). The run found the DM, the notes doc, the ENG-2401 `[2231]` comment and the Trello closing rule on its own.
- **Task and source match:** the export doesn't include the user prompt turn: the stream opens on the first assistant tool call. The match comes from behaviour: the run opens Arthur's DM, uses the SQL-only folder `d_9b41e7c2a05d36f8e1c7a4`, reads the SQL-only "DD bug review" invite `evt_6e2c91d4…` and replies in DM thread `1770937805.214409`. **Revision-11 overlay present:** Vincent's tooltips reply (SQL line 83, revision 11 only: "the 1 pixel gap is gone") appears in the run's tool results. Brian's revision-10 DM lines (SQL lines 61–67) appear too. So the run used the current SQL, or a later one with the same rows.

## Input / authority issues

Nothing blocks this review. Evidence limit: the export doesn't contain the literal prompt turn (see above). `input_manifest.json` was not updated by this review. The writer only saves the report, and the report records its own fingerprints.

## Checklist

- [x] Inputs listed; new upload saved under `opus` (NEW)
- [x] Model, unhinted status, task and SQL-revision match (NEW)
- [x] EXECUTION, ENVIRONMENT, UNIVERSE_MAP and `guide hardness` read; Eval 1A read in full (NEW)
- [x] Requirement map from the prompt, the DM, the notes doc and the ENG-2401 comment (`prompt-incorporation-v1`). Expected values REUSED from the current /prompt PASS 5 ledger on the same prompt and SQL hashes (`1_prompt.md` requirement ledger and decision row A), with the trap-deciding records re-checked against SQL lines 61–67 and 83 (NEW)
- [x] All 359 tool calls inventoried. Every write payload and its result were inspected: 68 creates, 15 updates, 30 comments, sheet creation, the values write, 3 shares and the DM reply (NEW)
- [x] Narrow-miss, failure-pattern and tool-call lines (NEW)

## Requirement map (`authority_contract: prompt-incorporation-v1`)

Authority chain: prompt ("everything he asked for, the way he lays it out") → Arthur's DM (SQL line 57) → carry-over notes doc (SQL line 16) → later change on ENG-2401 ("put [2231] at the front of every title you file"). Brian's closing rule (Trello card 211) is pulled in by the notes ("applies to the line on every child").

| # | Requirement | Expected | Observed (call #) | Outcome |
|---|---|---|---|---|
| R1 | Scope: 63 canvas lines plus bugs posted in #god-bugs after the last line. Skip deleted-line comments, follow-ups, the QA-doc pointer and the Leonard design question | 70 items | 70 sheet rows, 70 distinct tickets (355). Follow-ups were merged, and the QA-doc post and Leonard's question were excluded | MET |
| R2 | Ticket format: ENG team, Bug label, parent ENG-2401, `[2231] ` + title as written, no assignee, no description | All new tickets | All 68 creates are `{team: Engineering, labels:[Bug], parentId: ENG-2401}`, every title starts with `[2231] `, none has an assignee or description (calls 243–306) | MET |
| R3 | Lives removed on the economy line → 3 lives bugs Gone | 3 Canceled | ENG-2477/2489/2490 Canceled (278, 290, 291) | MET |
| R4 | Covered: Apple sync → ENG-2073; Android manual sign-in → ENG-2363 | 2 notes, no new ticket | Canvas wording commented on ENG-2073 (307) and ENG-2363 (308); no ticket filed for either | MET |
| R5 | Ticks overturned by later records: Tavern (Marcus/Brian, Dec 11) and River/Memory Tile shop icons (Brian, Dec 1 "don't trust that tick") | Broken ×2 | ENG-2492 and ENG-2483 in Bugs (293, 284) | MET |
| R6 | Unmerged PR #1913 → Tile Dozer background Broken | Bugs | ENG-2500 Bugs (301) | MET |
| R7 | Other Broken: backend errors on loss, train backgrounds, nav bar after team quit, megatile face | Bugs ×4 | ENG-2445, 2469, 2486, 2499 Bugs | MET |
| R8 | Everything else Fixed (53 canvas + 5 bug-channel), including the tooltips line settled by revision 11 and the saga-map line | Done ×58 | 58 Done. Tooltips ENG-2475 Done ("Vincent confirmed Brian's second fix"), saga map ENG-2471 Done | MET |
| R9 | UI tree: hold ENG-2424 (W&C off), 2426 (Axe Arena popup), 2428 (reward track), 2434 (Tile Dozer how-to-play), 2437 (no last pass) | 5 stay | All 5 left as they were, with reasoned lines (339–343) | MET |
| R10 | The other 14 open children → Done; 9 already Done stay | 14 moves | 14 moves (310–324; one ECONNRESET at 309 retried successfully at 324) | MET |
| R11 | Line on every child naming the current public build (Trello rule) | 28 lines | 28 comments naming Android 0.3.310 (325–352) | MET |
| R12 | Sheet in the DD bug carry-over folder, columns Bug/Outcome/Ticket/Why | 70 rows | Created with `parentId d_9b41e7c2…` (353–354), header `Bug, Outcome, Ticket, Why`, 70 rows (355): Fixed 58 / Broken 7 / Gone 3 / Covered 2 | MET |
| R13 | Share with everyone on Sunday's review (invite attendees) | Arthur, Robert, Oliver | Reader shares to arthur.blake@, robert@, oliver.brooks@ (356–358), matching the `evt_6e2c91d4…` attendees | MET |
| R14 | Reply in Arthur's DM thread with the three numbers | 9 still broken / 68 new / 23 of 28 Done | Thread reply in D05S1S2AB5M `thread_ts 1770937805.214409` (359): **9 / 68 / 23 of 28** | MET |

## Grouped failures and independent causes

No MATERIAL_FAIL or MINOR_GAP outcomes. **Independent causes: 0.** Minor notes with no effect on the result: (a) the run created the sheet with `gdrive_create_file` and then `gsheets_create_spreadsheet` on the same file id, so there is still one file; (b) one ECONNRESET on a state change, retried successfully; (c) titles keep Slack mention codes and placeholders verbatim, which is what the notes ask for ("the line as it was written").

## Why the traps no longer bit

The previous run (SQL revision 8) failed on four independent records: Vincent's email (Apple → ENG-2073), Marcus's DM (Tavern), Brian's sub-250 reply (shop icons) and Arthur's PR reviews (Axe Arena / Tile Dozer popups). Revision 10 added Brian's DM lines in Owen–Brian DM `D07E9PSQB6W` (SQL lines 61–67, Dec 8–11, 2025). Those lines restate three of those four deciding facts in one place:
- line 63: "the Tavern buttons lost their frame again on the Dec 10 Android version. My fix didn't hold"
- line 65: "Vincent told me before he left that the Apple sync line … is the same sync problem as ENG-2073"
- line 67: "the Axe Arena info popup still has the old frame and the Tile Dozer how-to-play popup still points at the old sprites"

This run read that DM through `slack_read_thread`/search results and cites "Brian, Dec 11" for all three (sheet rows; comments 341–342; summary "Brian said Vincent tied it there"). Three traps that used to need Gmail, a different DM and GitHub reviews now come from one easy-to-find DM with the persona's teammate. The only trap left in its original place (Brian's Dec 1 shop-icon reply in the sub-250 thread) was caught as well.

## Narrow miss / failure pattern / tool calls

**Narrow miss: NO.** 0 independent causes. Failed share ≈ 0% of about 30 core items (70 bug decisions with about 12 trap items weighted separately, 19 open-child decisions, 28 child lines, 2 Covered notes, ticket format, sheet/folder/share, 3 reply numbers). Difficulty mode medium, loss 15%. The narrow-miss rule doesn't apply: the run has no miss at all, so it scores 1 under the band table.

**Failure-pattern risk: YES.** Traps (✓ = right in this run), with the approximate share of the weighted answer each decides, knock-ons included:
- economy-line build basis (lives Gone, W&C off, unmerged #1913): ~20% ✓
- `[2231]` title change on ENG-2401: ~6% ✓
- ENG-2363 Covered (Vincent's Linear comment): ~8% ✓
- shop-icon tick (Brian's Dec 1 sub-250 reply): ~8% ✓
- **Brian's Owen DM `D07E9PSQB6W` (Tavern + Apple → ENG-2073 + Axe Arena/Tile Dozer holds + music/acid confirmations): ~30% ✓.** The original records (Vincent's email, Marcus's DM, the PR reviews) are still there, but this one DM now settles all of these items
- ENG-2428 / ENG-2437 Linear holds: ~11% ✓
- tooltips second-fix reply (revision 11): ~3% ✓
- Trello closing rule on every child: ~5% ✓
- scope exclusions (deleted lines, follow-ups, QA doc, Leonard): ~5% ✓
- calendar invitees for sharing: ~3% ✓

**Largest trap share ≈ 30%** (Brian's DM), up from ≈20% in the previous review because revision 10 put three independent traps behind one record.

**Tool calls: 359** (359 by the main agent, 0 by sub-agents). Task type long-horizon, minimum 100 (90% = 90). Not under 90% of the minimum. By tool: 78 `slack_read_thread`, 68 `linear_create_issue`, 40 `linear_list_comments`, 30 `linear_create_comment`, 21 Slack searches, 15 `linear_update_issue`, then Slack, Linear, GitHub, Drive, Calendar and Trello reads.

## Correct work and usability

The whole result can be used as-is: all 68 tickets are correctly formatted with the right state, both Covered notes are posted, 23 of 28 children are Done with the right 5 held, there are 28 build lines, the sheet is correct, folder and shares are right, and the DM reply has the expected numbers. The final message also flags two judgement calls honestly (verbatim titles; Robert's music post counted as a bug), and both match the expected answer.

## Task / environment defects

None found. Every write the task needs succeeded (Linear create/update/comment, Drive create in folder, Sheets values update, Drive share, Slack thread reply): **SUPPORTED**.

## Unassessed scope

Nothing material. Every write was read from its exact payload and successful result. The only gap is the missing prompt turn noted above.

## Score rationale

**Score 1 (Too easy, FAIL).** The run meets every core requirement with no meaningful defect: every per-item decision, every UI-tree call, every deliverable and all three reply numbers match the expected answer from the current /prompt ledger.
- **Why not 2:** score 2 needs at least a minor defect, a narrow miss or a low call count. This run has none of those. The notes above don't change any item's outcome.

## Next action (advice, from "Making a Task Hard for Opus 5.5")

- **Part 7, self-check 2 (same-place check) and Part 8 ("Move a correction out of the obvious place"):** Brian's DM lines 63, 65 and 67 hand over the Tavern, Apple/ENG-2073 and popup decisions in Owen's own DM with a teammate. That is the easiest place to look. Remove those three lines, or reduce them to something that doesn't settle the item (line 61's music/acid confirmations can stay if the other records don't already settle those). The original deciding records stay in place: Vincent's email, Marcus's DM and Arthur's PR reviews / #engineering-bots notices. The previous run missed all three of them.
- Check that removing them doesn't open a fork: the /prompt sweep settled each item from the original record as well (rows for Tavern, Apple and the popups).
- Changing the SQL makes earlier passes outdated. Send `/injection`, `/prompt` and then `/hardness` again with a new unhinted Opus run on the redeployed environment.

### FINAL VERDICT: FAIL

Assessment version: model-aware-v3

Assessed model: Opus

Assessment mode: OPUS_OBSERVED

Score: 1

Execution status: COMPLETE

Difficulty: Too easy

Gate decision: HOLD

Gate reason: INSUFFICIENT_DIFFICULTY

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Evaluator model: Opus 5.5 (claude-opus-5-5), session default effort

Next action: Take the three restated facts out of Brian's DM `D07E9PSQB6W` (SQL lines 63, 65, 67) so the Tavern, Apple/ENG-2073 and Axe Arena/Tile Dozer decisions again depend on their original records. Then rerun /injection and /prompt, get a new unhinted Opus run and send /hardness again.

Evidence limits: One run only; no average-score, pass@1 or repeatability claim. The export omits the literal prompt turn; the task match comes from behaviour and SQL-only records, including the revision-11 tooltips reply.
