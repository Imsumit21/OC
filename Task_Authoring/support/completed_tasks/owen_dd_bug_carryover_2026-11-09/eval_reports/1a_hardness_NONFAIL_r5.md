# /hardness — Observed Opus difficulty

## Scope

| Item | Value |
|---|---|
| Mode | Chat review, attempt workspace (no task-folder preflight) |
| Eval | `Evals/1A_Hardness_Eval.md`, assessment version `model-aware-v3`, mode `OPUS_OBSERVED` |
| Actual review time | 2026-11-07 |
| Clock | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal/` (`hg4-2026-08-31` v37); manifest `Evals/references/universes/normal/universe_manifest.json` SHA-256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Prompt | `Evals/task_inputs/04_Prompt.txt` (revision 5) SHA-256 `03e95ad1e900b7713667498d1f45ac7ff2a6a2fceee128889db9f83ed580b303` |
| Assignment | `Evals/task_inputs/00_Task_Assigned_Inputs.md` SHA-256 `ea53bf24…4124`: Owen Baker, Game Engineer (Unity); Engineering / Engineering Ops / Actions; **long-horizon**, difficulty mode **medium** |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (revision 8) SHA-256 `2ebfcae230b0666433d8c1c0924bd0d9a742807ac964280c5b89e9ef0ae1d0b6` (same version as the current /injection PASS and /prompt PASS 5) |
| Run | `Evals/task_inputs/opus/trajectory.json` (uploaded as `Run1_trajectory.json`, saved under `opus`) SHA-256 `27fb0c6dd41a4ab5667da2423b4be8e076989a6f7ffd4730c5f89292fe2175a3`, 4,819,574 bytes |
| Reference files | None used by the prompt |

## Run provenance

- **Model:** init `model: claude-opus-5-5[1m]`; all 329 assistant messages `claude-opus-5-5`; result `modelUsage.claude-opus-5-5[1m].canonicalModel: claude-opus-5-5`. Confirmed **Opus 5.5**.
- **Session:** `8fdee854-ae0f-44fc-8a4a-0c69a196343d`, Claude Code 2.1.280, `terminal_reason: completed`, `is_error: false`, 262 turns, no sub-agents (`subagent_stats.spawned: 0`).
- **Unhinted:** no hint text anywhere in the export (no added instructions, no "hint" string); the run worked from the prompt and discovered Arthur's DM, the notes doc, the ENG-2401 comment and the Trello rule itself (calls 3, 6, 9, 133).
- **Task match:** the export does not embed the user prompt turn (stream starts at the first assistant turn). Match established from behaviour: the run opens Owen's DM with Arthur, uses the "DD bug carry-over" folder `d_9b41e7c2a05d36f8e1c7a4` (SQL-only record), the Sunday "DD bug review" invite and replies in DM thread `1770937805.214409`. Injected records were present in the run (notes doc, ENG-2401 `[2231]` comment, ENG-2428/2437 comments, ENG-2363 comment, Trello card 211 all returned), and the SQL is one transaction, so the whole overlay was live.

## Input / authority issues

None blocking. Evidence limit: the export does not include the literal prompt turn (see above).

## Checklist

- [x] Inputs listed; run saved under `opus` (NEW)
- [x] Model, unhinted status, task match (NEW)
- [x] EXECUTION / ENVIRONMENT / UNIVERSE_MAP / SEARCH and `guide hardness` read (NEW)
- [x] SQL read before base searches; requirement map from prompt → DM → notes doc → ENG-2401 comment (NEW; deciding-record facts cross-checked against the current /prompt ledger on the same SQL/prompt hashes, REUSED only where re-verified below)
- [x] All 261 tool calls inventoried; every write payload and result inspected (NEW)
- [x] Each divergence's deciding record located, persona visibility checked, and "nothing later settles it" re-searched in Dec 2025–Feb 2026 Slack (NEW)
- [x] Narrow-miss, failure-pattern and tool-call lines (NEW)

## Requirement map (`authority_contract: prompt-incorporation-v1`)

Authority chain: prompt ("everything he asked for, the way he lays it out") → Arthur's DM (SQL line 57, D05S1S2AB5M, 2026-02-12 23:10:05Z) → "the carry-over notes doc I shared with you" (SQL line 16, gdocs `f_3ca9e15d7b20f4e681ad52`) → "If anything changes after this I'll put it on the master ticket" → ENG-2401 comment (SQL line 306, "put [2231] at the front of every title"). Brian's closing rule (Trello card 211) is incorporated by the notes ("Brian's closing rule from the UI work applies to the line on every child").

| # | Requirement | Expected | Observed (run call #) | Outcome |
|---|---|---|---|---|
| R1 | Scope: 63 canvas lines + bugs posted in #god-bugs after the last line; skip deleted-line comments, follow-ups, QA-doc pointer, Leonard design question | 70 items | 63 canvas lines + 7 #god-bugs posts; same exclusions (15–32, 136) | MET |
| R2 | Ticket format: ENG team, Bug label, parent ENG-2401, title as written with `[2231] ` prefix, no assignee, no description | All new tickets | All 69 creates `{team: Engineering, labels:[Bug], parentId: ENG-2401}`, `[2231]` prefix, no description (137–205) | MET |
| R3 | Build basis: 0.3.310 off the economy line; lives removed → 3 lives bugs Gone | 3 Canceled | 3 Canceled (177, 189, 190) | MET |
| R4 | Unmerged PR doesn't count: Tile Dozer background (PR #1913 never merged) | Broken | Bugs (200) | MET |
| R5 | Other Broken: backend errors on loss, train backgrounds, nav bar after team quit, megatile face | Broken ×4 | Bugs ×4 (145, 169, 186, 199) | MET |
| R6 | Covered: Android manual sign-in → ENG-2363 (Vincent's Linear comment) | Note on ENG-2363, no new ticket | Note on ENG-2363 (206) | MET |
| R7 | **Covered: Apple sync line → ENG-2073** (Vincent's email, SQL lines 276–282, Owen's INBOX, 2025-11-20: "The Apple sync line on my Android list comes down to the same sync problem as ENG-2073, no need for anything new"; ENG-2073 status Bugs, open, call 66) | Note on ENG-2073, no new ticket | New Bugs ticket ENG-2440 (139); sheet "No fix since and no open ticket covers it" (257) | **MATERIAL_FAIL** |
| R8 | **Shop-icon tick overturned** (Brian, SQL line 63, C09Q4S613CN reply 2025-12-01: "the round icons on the River Tile and Memory Tile shops are there again on the current build, so don't trust that tick") | Broken (Bugs) | Done ENG-2484 (183); sheet "no later record says otherwise" | **MATERIAL_FAIL** |
| R9 | **Tavern tick overturned** (Marcus, SQL line 59, Owen–Marcus DM D05USBTQY1F 2025-12-11: "the Tavern buttons lost their frame again on last night's Android build … Brian's fix didn't hold"; the Dec 10 Android builds were EconomyChanges #2298–#2301, `C05433XK267/2025-12.json` /139–/154) | Broken (Bugs) | Done ENG-2493 (192) | **MATERIAL_FAIL** |
| R10 | Remaining ticked/fixed items incl. flicker, music, acid, bottom bar, nav-bar tooltips, saga map | Fixed (Done) ×58 | Done ×58 of those (rest of 137–205) | MET |
| R11 | UI tree: hold ENG-2428 (Oliver: reward track old frames), ENG-2437 (Brian: no last pass), ENG-2424 (Collect & Win switched off) | Stay | Stayed, with reasoned lines (238, 242, 250) | MET |
| R12 | **UI tree: hold ENG-2426 Axe Arena and ENG-2434 Tile Dozer** (Arthur's PR reviews, SQL lines 200/202 and #engineering-bots notifications lines 131/133, C050WGU41HR where Owen is a member: "the Tile Dozer how-to-play popup still points at the old sprites … has to be swapped before the Tile Dozer ticket can close"; "the Axe Arena info popup keeps the old frame here. Needs doing before the Axe Arena ticket can close") | Stay | Moved to Done (214, 220); lines say "Landed: Done … is in the current public build" (240, 248) | **MATERIAL_FAIL** |
| R13 | Other 14 open children → Done; 9 already Done stay; masters unchanged | 14 moves | 14 correct moves (207–222 minus 214, 220); masters untouched | MET |
| R14 | Line on every child naming the current public build (Trello card 211 rule) | 28 lines | 28 lines naming 0.3.310 (223–250); 2 carry R12's wrong "Done" content | MET (content on 2 lines follows R12) |
| R15 | Sheet in DD bug carry-over folder, columns Bug/Outcome/Ticket/Why | 70 rows | Created, moved into `d_9b41e7c2…` (253–254), 70 rows, right columns (257); 3 rows carry R7–R9 | MET (3 rows follow R7–R9) |
| R16 | Share with everyone on Sunday's review (calendar invitees) | Arthur, Robert, Oliver | Shared reader with all three (251–252, 258–260) | MET |
| R17 | Reply in Arthur's DM thread with the three numbers | 9 still broken / 68 new tickets / 23 of 28 Done | Thread reply (261): **7 / 69 / 25** | **MATERIAL_FAIL** (knock-on of R7–R9, R12) |

### Why the expected values hold (challenge of each failure)

- **R7:** Opus itself judged the Apple line not fixed (Bugs). The notes' "Covered" outcome comes before "Broken" ("Take the first outcome that fits") and warns "Vincent tied a few lines to tickets before he left". The email is in Owen's own inbox. ENG-2073's description alone does not mention Apple, so the email decides it. Opus found ENG-2073 (calls 52, 66–67) but never searched Gmail for Vincent or sign-in (its only Gmail queries: "310", "from:brian.foster", "UI ticket"; calls 40, 109, 130). The deciding record never reached the run (string not present in any tool result). Genuine retrieval miss.
- **R8:** "A tick on the canvas stands unless a later record about that bug says otherwise." Brian's message names both shops and says not to trust the tick. "Robert's reports in the sub-250 channel aren't part of this" excludes Robert's reports as items. It doesn't exclude later evidence about a canvas line. No later record says it was fixed again: Dec 2025–Feb 2026 Slack searches for "river tile", "memory tile" and "shop icon" return only an unrelated lives-banner change and a Combo Fighter icon remark. Opus read C09Q4S613CN only up to `latest 1764100000` (Nov 25, call 119), never opened the thread and never searched the shop names. Residual note: Dec 1's "current build" was a develop build. The economy line's first builds are Dec 9, and nothing records a re-fix, so the expected Broken stands.
- **R9:** The Dec 10 Android builds were all EconomyChanges, the line 0.3.310 comes off (0.3.310 posted `C05433XK267/2026-02.json` /232). No later Tavern record exists in Dec 2025–Feb 2026 Slack ("tavern": 0 hits). Opus read only Owen's DMs with Arthur and Brian (calls 3, 105), never the Marcus DM.
- **R12:** The notes say "every open child goes Done unless a record shows a piece of its UI work never made it into that build … Then it stays where it is". Each review names one unfinished piece of UI and the ticket it blocks. Later "Axe Arena" hits ("Fix issue opening Axe Arena panel from Nate") are a different defect. No Tile Dozer how-to-play record follows. Opus listed PRs with summary fields only (call 51), never called `github_get_pull_request_reviews`/`_comments` (both in the catalog), and never read #engineering-bots. It applied the same hold rule correctly to the three children whose notes sat in Linear.

## Grouped failures and independent causes

| Cause | Deciding record (service) | Items made wrong |
|---|---|---|
| C1 | Vincent's Nov 20 email tying the Apple line to ENG-2073 (Gmail) never read | Apple line filed as new Bugs ticket ENG-2440 instead of a note on ENG-2073; sheet row; new-ticket count 69 vs 68 |
| C2 | Brian's Dec 1 "don't trust that tick" reply (Slack, sub-250 thread) never read | Shop-icon ticket Done instead of Bugs; sheet row; still-broken count |
| C3 | Marcus's Dec 11 "Brian's fix didn't hold" DM (Slack DM) never read | Tavern ticket Done instead of Bugs; sheet row; still-broken count |
| C4 | Arthur's PR #1905 / #1908 review comments (GitHub reviews + #engineering-bots) never read | ENG-2426 and ENG-2434 wrongly moved to Done with "Landed: Done" lines; Done count 25 vs 23 |

All four rest on different records in different places, and a run could miss any one without the others. **Independent causes: 4.** The DM reply's three wrong numbers are knock-ons (still broken 7 vs 9 from C2+C3; tickets 69 vs 68 from C1; Done 25 vs 23 from C4). They are counted once per required item, not as extra causes.

## Narrow miss / failure pattern / tool calls

**Narrow miss: NO.** 4 independent causes. Failed share ≈ 30% of the weighted core answer, on about 30 core items: 70 bug decisions (routine ones grouped, about 12 trap items weighted separately), 19 open-child decisions, 28 child lines, 2 Covered notes, ticket format, sheet/folder/share, and the 3 reply numbers (weight 5 each, all wrong). Difficulty mode medium, loss 15%. Not a single cause, and the failed share is above the loss.

**Failure-pattern risk: NO.** Traps (✓ = this run right, ✗ = wrong), with the approximate share of the weighted answer each would decide including knock-ons:
- economy-line build basis (lives Gone, Collect & Win off, unmerged #1913): ~20% ✓
- `[2231]` title change on ENG-2401: ~6% ✓
- lives Gone: ~12% ✓ (part of the build-basis share)
- PR #1913 unmerged: ~7% ✓
- ENG-2363 Covered: ~8% ✓
- **Apple → ENG-2073 (email): ~10% ✗**
- **Tavern (Marcus DM): ~8% ✗**
- **shop icons (Brian reply): ~8% ✗**
- **Axe Arena + Tile Dozer PR reviews: ~11% ✗**
- ENG-2428/2437 Linear holds: ~11% ✓
- ENG-2424 switched off: ~8% ✓
- Trello closing rule on every child: ~5% ✓
- scope exclusions (deleted lines, follow-ups, QA doc, Leonard): ~5% ✓
- calendar invitees for sharing: ~3% ✓

**Largest trap share ≈ 20%** (economy-line build basis), below 30%. The difficulty is spread over at least 4 independent misses in Gmail, Slack (two places) and GitHub.

**Tool calls: 261** (261 main agent, 0 sub-agents). Task type long-horizon, minimum 100 (90% = 90). Not under 90% of the minimum. By tool: 69 `linear_create_issue`, 40 `linear_list_comments`, 29 `linear_create_comment`, 16 `linear_update_issue`, 16 `linear_list_issues`, then Slack, GitHub, Drive, Calendar and Trello reads.

## Correct work and usability

The run is substantial and largely usable:
- It found every instruction source, including the late ENG-2401 title change and Brian's Trello rule.
- It applied the build-basis rule correctly (lives Canceled, unmerged PR #1913 not counted, Collect & Win switched off).
- It handled ENG-2363 as Covered and held the three children whose notes sat in Linear.
- It filed 69 correctly formatted tickets, 65 of them with the right outcome.
- It wrote a build line on all 28 children.
- It built the sheet in the right folder with the right columns and shared it with exactly the invitees.
- It replied in the right thread.
- Its final message was honest about its judgement calls, though it didn't flag any of the four misses.

## Correction needed

- Cancel or remove ENG-2440 and add the canvas wording as a note on ENG-2073.
- Move ENG-2484 and ENG-2493 to Bugs.
- Revert ENG-2426 and ENG-2434 from Done and fix their two child lines.
- Fix three sheet rows.
- Send corrected numbers to Arthur (9 / 68 / 23).

This touches every deliverable (Linear bug tickets, UI tree, child lines, sheet, DM reply), so it is substantial correction across the result, not one bounded fix.

## Task / environment defects

None found. Every deciding record was visible to Owen: Gmail INBOX; C09Q4S613CN and D05USBTQY1F membership in `channels.json`; C050WGU41HR membership; GitHub reviews reachable via cataloged `github_get_pull_request_reviews`/`_comments`. Each was reachable through cataloged tools, and none of the four misses comes from an unincorporated rule. No capability-caused miss: every write the task needs succeeded in the run (Linear create/update/comment, `gsheets_create_spreadsheet` + `gdrive_move_file`, `gsheets_values_update`, `gdrive_share_file`, `slack_send_message` with `thread_ts`): **SUPPORTED**.

## Unassessed scope

None material. The sheet's 70 rows, all 69 creates, all 16 state changes, all 29 comments and the DM reply were read from exact payloads plus successful results.

## Score rationale

**Score 4 (Hard, NON-FAIL).**
- **Why not 3:** four independent retrieval misses, in three services, each overturning a decision the notes make deciding. Together they make all three requested reply numbers wrong and need fixes in every deliverable. That is more than one bounded correction.
- **Why not 5:** the central migration is mostly right: 65 of 69 tickets carry the right outcome, the formatting and build-basis traps are handled, 26 of 28 children end in the right state, and the sheet and sharing are correct. Substantial correct work remains usable, so the failures don't invalidate the central result or defeat much of the core task.

### FINAL VERDICT: NON-FAIL

Assessment version: model-aware-v3

Assessed model: Opus

Assessment mode: OPUS_OBSERVED

Score: 4

Execution status: COMPLETE

Difficulty: Hard

Gate decision: PROCEED

Gate reason: OBSERVED_OPUS_FAILURE

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Evaluator model: Opus 5.5 (claude-opus-5-5), session default effort

Next action: Proceed with dependent authoring (/oe, then /rubric); keep the four observed failure causes (ENG-2073 email, Brian's shop reply, Marcus's Tavern DM, Arthur's PR #1905/#1908 reviews) as distinct graded items so baseline runs can split on them.

Evidence limits: One run only; no average-score, pass@1 or repeatability claim. The export omits the literal prompt turn (task match established from behaviour and SQL-only records).
