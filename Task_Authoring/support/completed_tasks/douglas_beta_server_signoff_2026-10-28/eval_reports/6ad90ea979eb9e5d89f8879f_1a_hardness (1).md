# Hardness Review: `/hardness` (Opus observed)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## 1. Scope and provenance

| Item | Value |
|---|---|
| Review | Chat/attachment review, portal attempt 6ad90ea979eb9e5d89f8879f, audit mode |
| Actual review date | 2026-10-26 |
| Selected spec | `Evals/1A_Hardness_Eval.md` (SHA-256 `a3d48e04…7503a3`), `model-aware-v3`, `ruthless-grading-v1`, `prompt-incorporation-v1`, `stage-evidence-v1`; WORKFLOW SHA-256 `ee4cd8e1…fcd5d` |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Prompt | `Evals/task_inputs/04_Prompt.txt` (input rev 11), SHA-256 `a0414d89216a9777c4d2eca8b78eea8ab2ee77edc26503d3d24a2daae3ca3e3e` |
| Assignment | `Evals/task_inputs/00_Task_Assigned_Inputs.md` SHA-256 `31d7b596…a5627d1f`: Douglas, Software Engineer; Engineering; Engineering Ops; Retrieval; long-horizon |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (input rev 10), SHA-256 `c1edeb4431f439c7db8ea531244eaa6f34f1312f4b420d3c606e0684cdcf075c`. Read as a static overlay, never executed |
| Selected run | `Evals/task_inputs/opus/trajectory.json` (uploaded as `Run1_trajectory (2).json`, input rev 12), SHA-256 `1c4308e2bb1407c94f048e4b09823acc1a3ca033abcfa8d2cfb48ca9f0e90007`, 1,457,750 bytes, 389 entries, session `08ef3cb6-…` |
| Run model | `system/init.model` = `claude-opus-5-5[1m]`; all 184 assistant messages report `claude-opus-5-5`; `modelUsage.canonicalModel` = `claude-opus-5-5`. Claude Code 2.1.280, bypassPermissions, 0 subagents, 156 turns, 155 tool calls, `terminal_reason: completed`, `is_error: false` |
| Run selection | The run attached to this `/hardness` message is the user's selection. It replaces the earlier saved Opus run (session `1c9ba43e-…`, SHA-256 `0687d8db…`), which was graded in the previous report; that score is not inherited |
| Reference files | None. The prompt names no attachment; every source it points to is an environment record |
| Reused evidence | No verdict reused. `1_prompt.md` (requirement ledger, SQL rev 10) was used as a discovery lead only. Every graded fact below was rechecked here against the SQL lines, base Linear (`hg_records`, 3,687 issues, scan complete) and the run's own tool results |

### Input and authority issues

- **Prompt text not embedded in the export.** The trajectory has no user prompt turn (starts with `system/init`). Task match is established from the run itself: it opens by finding Arthur's DM (#2–#5), then the beta card (#7), Gmail `from:leonard` (#10, before any record mentioning Leonard was read), the "beta sign-off" folder (#14), and ends by moving tickets to Todo, sharing with Leonard and replying in the Arthur DM. Only this prompt explains that combination. Recorded as a limit, not a blocker.
- **Hint status:** no hint is visible in any system text or tool result; the run missed three decisive records, which a hint would likely have surfaced. Treated as **unhinted**.
- **Source version:** the run's tool results match the rev-10 overlay for every injected record it read: card 80 and its comment (#7–#8), Arthur's DM with `reply_count 1` (#5, SQL l.50), Leonard's email `<CAreN_…>` in thread `…/1844721277206562572` (#10–#11, SQL l.72–74), the Confluence page body (#13, SQL l.31), the prod deploys doc and both deploy-log tabs (#18, #20–#21), the freeze event (#22), PRs #38–#54 and the Linear comments.
- `input_manifest.json`: not written (no writer key; fingerprints are in the table above).

## 2. Requirement map

`authority_contract: prompt-incorporation-v1`

Incorporation chain:
- "the way he laid it out" / "what he asked for" → Arthur's DM (SQL l.50) → "the beta card on the roadmap board" = card 80 (SQL l.61).
- Card rule 3 → prod deploys doc (SQL l.17) → "the server freeze on the calendar" (SQL l.93, 2025-09-26 22:00Z). Rule 1 → deploy log (l.22, l.24). Rule 6 → ZM Beta Confluence page (l.31).
- "his sign-off rules" also covers Arthur's later additions to the same sign-off: card comment adding spreadsheet imports as server changes (l.69); DM thread reply on ZOM-537 (l.52: *"537 isn't only #46. the new economy values also need the economy table import on the backend"*); email reply in Leonard's thread (l.84: *"leave ZOM-547 and ZOM-553 off… the backend copies (#49 and #53) are only mirrors. They're not part of the count either way. Rest of the card stands."*).
- Arthur's Confluence reply (l.37) is a fact under rules 1/4: ZOM-487's server change includes the boss arena HP table import.
- "handle what he asked for" → Leonard's email (l.84 quoted body / l.74).
- Not incorporated: Oliver's #zombie-match3d request (l.48). Not counted either way.

Robustness check on the 547/553 exclusion: even read strictly as a fact rather than an instruction, Arthur states the fix values come from the client sheet and the backend PRs are mirrors, so the fix did not "need a server change" (rule 1). Both readings exclude them.

| # | Requirement | Expected | Observed (run) | Citations | Outcome |
|---|---|---|---|---|---|
| R1 | Scope: ZOM Done after 2025-08-25 11:52Z through Sep 30, server change, no parents | 16 tickets: ZOM-459, 509, 336, 392, 518, 510, 256, 531, 537, 444, 499, 487, 550, 435, 503, 557. Out: 457 (parent), 461 (Done 11:51:48Z), 547/553 (Arthur) | 18 tickets: the 16 plus ZOM-547 and ZOM-553. 457 and 461 correctly excluded | Run #136, #154; Linear `/issues/3622` 547 Done 2025-09-17, `/issues/3629` 553 Done 2025-09-30, `/issues/3530` 461 Done 11:51:48Z; SQL l.84 | **MATERIAL_FAIL** (F1) |
| R2 | On prod per the doc, all server changes per ticket (rule 4, imports count) | Y (6): 459, 509, 510, 531, 444, 499. N (10): 336, 392, 518, 256, 537, 487, 550, 435, 503, 557 | Y (10): the 6 plus **537, 487** (and 547, 553). N (8): 336, 392, 518, 256, 550, 503, 435, 557 | Run #136; SQL l.24 (economy table and boss arena HP table imports target **dev**), l.52, l.37; #46 `prod:` 09-09 + Arthur Approve (PR-only part is on prod), #48 `prod:` 09-16 + non-author Approve | **MATERIAL_FAIL** (F2) for 537/487; the other 14 statuses MET |
| R3 | Register: one row per ticket (ticket, server change(s), Y/N) in the ZM Beta sign-off folder | Sheet/file in `d_69fcebc4…` with 16 correct rows | Sheet created and moved into `d_69fcebc4…` (#134–#135, `parents` confirmed); 18 rows, 4 wrong (2 extra, 2 wrong Y) plus a "10 / 8" summary | Run #134–#136; SQL l.8 (Douglas writer), l.31 | Placement **MET**; content **MATERIAL_FAIL** (same causes F1/F2) |
| R4 | Rule 5: every not-on-prod ticket back to Todo with a comment naming the change still to go out | 10 tickets moved + 10 comments, incl. ZOM-537 (economy table import to prod) and ZOM-487 (boss arena HP table import to prod) | 8 moved + 8 accurate comments (#137–#152). **ZOM-537 and ZOM-487 left in Done, no comment** | Run #137–#152; card 80 rule 5 (l.61) | 8/10 **MET**; 2 **MATERIAL_FAIL** (F2) |
| R5 | DM reply to Arthur: how many on prod, which aren't | "6 on prod; not on prod: 336, 392, 518, 256, 537, 487, 550, 435, 503, 557" | Sent to D05QQF7V404 (#154): "18 in scope. 10 on prod, 8 aren't", lists 10 on prod incl. 537/487/547/553; not-on-prod list omits 537 and 487 | Run #154 result `channel: D05QQF7V404`; SQL l.50 | Delivery **MET**; content **MATERIAL_FAIL** (F1/F2) |
| R6 | Leonard: share the register directly, comment access, after it is in the folder | `gdrive_share_file` leonard.hayes@, role commenter, after the move | Shared as `commenter` (#153) after the move (#135) | Run #153; SQL l.84 quoted body | **MET** |
| R7 | Final response | Accurate summary of what was done | Clear and well organized, but repeats the wrong 18/10/8 figures and the wrong on-prod list | Run final `result` | **MINOR_GAP** (inherits F1/F2; not separately counted) |

Unrequested action: the run also replied to Leonard by email (#155) with "18 tickets in scope: 10 are on prod and 8 aren't". Not required and not scored as a separate failure; it spreads the F1/F2 error to a second recipient.

## 3. Grouped failures and independent causes

All three misses share one pattern: the run read Arthur's base instructions (card, card comment, doc) but never read his later additions, which sat in three different places it had already reached.

**F1 — Arthur's email reply not read; ZOM-547/553 wrongly in the register (MATERIAL).**
- Evidence: the run searched `from:leonard` (#10), read only Leonard's original message `<CAreN_…>` (#11), and never called `gmail_get_thread` or searched the thread. Arthur's reply `<CAuC1…>` is in Douglas's INBOX, same thread `…/1844721277206562572`, subject "Re: beta go/no-go thursday" (SQL l.84). The run later replied into that same thread (#155, `threadId …/1844721277206562572`) without reading it.
- Effect: 2 extra register rows marked Y; on-prod count inflated by 2 in the register, the DM and the final answer.
- Agent failure: the thread was in the persona's mailbox, the read tool was available, and the run already had the thread ID.

**F2 — Import server changes for ZOM-537 and ZOM-487 missed; both marked on prod and left in Done (MATERIAL).** Two independent retrieval misses with the same consequence type:
- *ZOM-537 (DM thread):* the run saw Arthur's DM had `reply_count 1` and wrote "Check the thread reply on the latest message" (msg 12). It called `slack_read_thread` with Arthur's **user ID** instead of the DM channel and got `channel_not_found` (#6). It never retried, although `D05QQF7V404` appears 310 times in the saved channel output it had just parsed (msg 7). The reply (SQL l.52) names the economy table import, which the Console & imports tab shows on **dev** only (l.24, 2025-09-16).
- *ZOM-487 (Confluence comment):* the run read the ZM beta page (#13) but never listed its comments. Arthur's reply (l.37) says the boss arena HP table import is part of ZOM-487's server change; the deploy log shows it on **dev** only (l.24, 2025-09-17).
- Effect: under rule 4 both tickets are N. The run marked both Y in the register and DM, and skipped the rule-5 Todo move and comment for each (2 of 10 required Linear transitions and 2 of 10 comments missing).
- Agent failure: both sources were reachable with available tools. The 537 miss came from the Agent's own wrong argument and its decision not to retry after a clear error.

Net effect on the central answer: the run reported **10 on prod / 8 not** where the correct answer is **6 on prod / 10 not**. 4 of 10 claimed "on prod" tickets are wrong, and 2 of 10 not-on-prod tickets are missing from the list Arthur asked for.

## 4. Correct work and usability

- Correct method on the hard rules: prod only via `prod:` comment, non-author Approve before deploy (#41 approved after deploy, #43 never approved), Arthur's Approve during the freeze (#50 COMMENTED only, #52 no Arthur Approve), rollback handling (#44 rolled back and redeployed before freeze = Y; #54 rolled back = N), imports from the Console & imports tab (510 Y, 256 N), and the stale "Prod deploys" quick list correctly ignored.
- Correct scope edges: ZOM-461 (Done one minute before the cut) and parent ZOM-457 excluded; all 16 true in-scope tickets found from 73 Done tickets.
- 14 of 16 true in-scope statuses correct; 8 of 10 Todo moves with accurate, specific comments.
- Register in the right folder (not the client QA folder); Leonard shared as commenter after placement; DM sent in the right conversation; Douglas's Sep 22 wrong claim flagged to Arthur.

## 5. Task / environment defects

- None found that cause any counted failure. Every missed record was in the persona's reach: Douglas's INBOX (Gmail), a DM he is a member of (Slack), and unscoped Confluence.
- Observation: in this runtime `slack_read_channel` accepted a user ID and resolved it to the DM, but `slack_read_thread` did not. The correct channel ID was in the Agent's own output and a retry was trivial, so this stays an Agent error. Even if the 537 miss were excluded entirely, F1 and the 487 miss alone still give a wrong count (8 on prod instead of 6), extra rows and a missing Todo move. The band does not change.
- Output capability: register creation and placement, share with `role=commenter`, Linear state and comments, DM send were all **SUPPORTED**, shown by successful results in this run (#134–#136, #137–#153, #154).

## 6. Unassessed scope

- The prompt text is not embedded in the export (see §1).
- Presence of Arthur's email reply and Confluence comment in the run state is inferred from the applied rev-10 overlay, because the run never queried them. Sibling rows from the same INSERT blocks were read and match (Leonard's email l.74; the page l.31), so this is treated as established.

## 7. Score rationale

**Score 4 (Hard, NON-FAIL).** The run makes material, model-caused errors across all three main outputs: the register (4 wrong rows), the DM answer Arthur asked for (10/8 instead of 6/10, two not-on-prod tickets missing) and the rule-5 Linear actions (2 of 10 tickets not moved or commented). These come from three independent retrieval misses. Fixing it means removing two rows, flipping two statuses, two Linear transitions and comments, and a corrected DM (and email). That is substantial correction across the result.

- **Why not 3:** this is not one bounded fix to an otherwise correct result. Three separate sources were missed, and each error spreads into the register, the DM, the final answer and (for F2) the Linear writes. The headline number Arthur asked for is wrong by 4.
- **Why not 5:** substantial core work remains correct and usable. All 16 true in-scope tickets are present, 14 of 16 statuses are right, all 8 not-on-prod tickets it found are correct with accurate Todo moves and comments, and the hardest rule logic (approval timing, freeze, rollbacks) is applied correctly. Folder placement and Leonard's share are correct. The central result is materially wrong but not defeated.

### FINAL VERDICT: NON-FAIL
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Assessment version: model-aware-v3

Assessed model: Opus

Assessment mode: OPUS_OBSERVED

Score: 4

Execution status: COMPLETE

Difficulty: Hard

Gate decision: PROCEED

Gate reason: OBSERVED_OPUS_FAILURE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (level not identified by runtime)

Next action: Proceed with dependent authoring (OE, rubric). Keep F1 and F2 as the observed failures: check that ZOM-547/553 are off the register, that ZOM-537 and ZOM-487 are N and moved to Todo with comments naming the dev-only imports, and that the DM reports 6 on prod with all 10 not-on-prod tickets.

Evidence limits: One run only; no average-score or repeatability claim. The prompt text is not embedded in the export, so task match is inferred from the run's behaviour. Arthur's email reply and Confluence comment being present in the run state are inferred from the applied rev-10 overlay.
