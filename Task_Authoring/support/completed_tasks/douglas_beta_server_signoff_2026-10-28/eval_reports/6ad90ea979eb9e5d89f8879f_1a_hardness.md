# Hardness Review: `/hardness` (Opus observed)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## 1. Scope and provenance

| Item | Value |
|---|---|
| Review | Chat/attachment review, portal attempt 6ad90ea979eb9e5d89f8879f, audit mode |
| Actual review date | 2026-10-26 |
| Selected spec | `Evals/1A_Hardness_Eval.md` (SHA-256 `a3d48e04…7503a3`), `model-aware-v3`, `ruthless-grading-v1`, `prompt-incorporation-v1`, `stage-evidence-v1` |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Prompt | `Evals/task_inputs/04_Prompt.txt` (rev 8), SHA-256 `a0414d89216a9777c4d2eca8b78eea8ab2ee77edc26503d3d24a2daae3ca3e3e`. All six uploaded prompt versions have this same hash, so the run cannot have received a different prompt text |
| Assignment | `Evals/task_inputs/00_Task_Assigned_Inputs.md` SHA-256 `31d7b596…a5627d1f`: Douglas, Software Engineer; Engineering; Engineering Ops; Retrieval; long-horizon |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (rev 7), SHA-256 `f5a42cee096292f3b7261a31b89e7b8e345ec48aecbf4c60e6bfcc373740c9c3`. Read as a static overlay and never executed |
| Selected run | `Evals/task_inputs/opus/trajectory.json` (uploaded as `Run1_trajectory.json`), SHA-256 `0687d8dba3cb06b1daf4458ba3698ee94f36ce0dff0f7a748edac71096658b26`, 1,482,472 bytes, 386 entries |
| Run model | `system/init.model` = `claude-opus-5-5[1m]`; all 184 assistant messages report `claude-opus-5-5`; `modelUsage.canonicalModel` = `claude-opus-5-5`. Claude Code 2.1.280, bypassPermissions, 0 subagents, 158 turns, 157 tool calls, `terminal_reason: completed`, `is_error: false` |
| Run selection | This is the only run you supplied for this review, so it is your selection. There was no earlier saved Opus or Haiku run |
| Reference files | None. The prompt names no attachment, and every source it points to is an environment record |
| Reused evidence | None reused as approval. `1_prompt.md` was used only as a discovery lead. Every fact it pointed to was rechecked here against the SQL lines and the base records |

### Input and authority issues

- **Prompt text not embedded in the export.** The trajectory starts with `system/init` and the first assistant turn. It has no user message. The saved prompt is the authority for requirements. Task and source match is still established from the run itself: its first actions are to find Arthur's DM (calls #2–#5) and to search Gmail `from:leonard` (call #7, before any record mentioning Leonard was read). Later it looks for the "beta sign-off" folder, moves not-on-prod tickets to Todo and replies in the Arthur DM. Only this prompt explains that combination. This is recorded as a limit, not a blocker.
- **Hint status:** no hint is visible. No user turn, system text or tool result points the agent at sources. The run also missed the decisive email, which a hint would most likely have surfaced. It is treated as **unhinted**.
- **Source version:** Arthur's Sep 30 email (SQL lines 65–76) is in **every** uploaded SQL version (`01_Universe_Inject.sql` and versions 2–4). The only difference between versions is the ZOM-535/ZOM-504 comments and UPDATEs, which do not touch any graded value. The run's tool results match the rev-7 overlay for every injected record it read (card 80 and its comment, prod deploys doc, deploy log, Confluence page, Leonard's email, PRs #37–#54, Linear comments).
- `input_manifest.json`: not written. The output writer has no manifest key, and this review writes under `reports/` only through the writer. Input fingerprints are in the table above.

## 2. Requirement map

`authority_contract: prompt-incorporation-v1`

Incorporation chain:
- "the way he laid it out" and "what he asked for" point to Arthur's DM (SQL l.46).
- The DM points to "the beta card on the roadmap board", which is card 80 (SQL l.55).
- Card rule 3 points to the prod deploys doc (SQL l.17), and the doc points to "the server freeze on the calendar" (SQL l.93).
- Card rule 1 points to the deploy log (SQL l.22, l.24). Card rule 6 points to the ZM Beta Confluence page (SQL l.31).
- "his sign-off rules" also covers Arthur's later amendments to the same rules for the same sign-off: his card comment (SQL l.63, adds imports) and his Sep 30 19:42 UTC email, subject "Beta sign-off - server side" (SQL l.68): *"One more for the server sign-off: leave ZOM-547 and ZOM-553 off the register … They're not part of the count either way. Rest of the card stands."*
- "handle what he asked for" incorporates Leonard's email (SQL l.80).
- Not incorporated: Oliver's #zombie-match3d request (SQL l.44) and the Domino Delights Confluence page (SQL l.27).

**Strongest counter-reading of the email:** "the way he laid it out" means only the DM and the card it names, so the email is optional. **Rejected.**
- The prompt also delegates "**his sign-off rules**".
- The email is from Arthur, to Douglas, sits in Douglas's INBOX (labels `INBOX, IMPORTANT`), and its subject is exactly the card's name.
- It explicitly amends the card ("One more for the server sign-off … Rest of the card stands"). It has the same form as the card comment, which the run itself correctly treated as binding.
- It is dated before the DM, and the DM does not retract it.

Under the contract, a later applicable update for the same issue and scope governs. The run had Gmail search (`gmail_search_messages`, used at call #7) and the prompt itself tells the agent that email holds task context.

| # | Requirement | Expected (verified) | Observed | Citations | Outcome |
|---|---|---|---|---|---|
| R1 | Find and apply Arthur's rules: card 80, card comment, Sep 30 email | All three applied | Card (#9) and comment (#10) read and applied. **The email was never retrieved.** The only Gmail query was `from:leonard` (#7), and no message with ID `CAuC1dALZ…` or text "leave ZOM-547" appears anywhere in the export | SQL l.55, l.63, l.68; traj calls #7, #9, #10 | **MATERIAL_FAIL** (root cause F1) |
| R2 | Scope: ZOM tickets Done after the 2025-08-25 11:52 UTC cut through Sep 30 with a server change; parent tickets out; ZOM-547/553 out per the email | **16 tickets:** ZOM-459, 509, 336, 392, 518, 510, 256, 531, 537, 444, 499, 487, 550, 435, 503, 557 | **18 tickets:** the correct 16 **plus ZOM-547 and ZOM-553**. Correctly excluded: ZOM-457 (parent), ZOM-461 (Done 11:51:48Z, before the cut), ZOM-563 (In Progress), and the client-only tickets | Linear `data.json` /issues/3528 (459 Done 11:53:11Z), /3530 (461 11:51:48Z), /3526 (457 parent), /3622 (547 Done 09-17), /3629 (553 Done 09-30), /3640 (563 In Progress); SQL Linear comments l.700–852; traj #24, #59–#134 | **MATERIAL_FAIL** (from F1) |
| R3 | On-prod classification under the prod deploys doc (`prod:` comment, prior non-author Approve, Arthur Approve during the 2025-09-26 22:00Z freeze, rollbacks, deploy-log imports) | Y: 459 (#38), 509 (#39), 510 (prod import 09-08), 531 (#45), 537 (#46), 444 (#47, Arthur APPROVED 16:05 before the 16:20 deploy), 499 (#44 redeployed 09-22), 487 (#48). N: 336 (#40 dev only), 392 (#41 approved 18:05 after the 16:30 deploy), 518 (#43 no Approve), 256 (pack imported to dev only), 550 (#50 freeze deploy, Arthur only COMMENTED), 435 (#51 dev only), 503 (#52 freeze deploy with a non-Arthur Approve), 557 (#54 rolled back 09-28) | All 16 in-scope tickets classified correctly, each with the right reason. #49/#53 were also classified correctly as deployed, but they should not have been listed | SQL l.145–677 (PR comments and reviews), l.22, l.24, l.17, l.93; traj #13, #17–#19, #25–#58, #136 | **MET** |
| R4 | Register: one row per ticket with ticket, server change(s), on prod Y/N | 16 rows | Sheet `1t93KwCu…` has 18 ticket rows (Ticket / Server change(s) / On prod / Notes) plus a summary row reading "18 tickets in scope; 10 on prod / 8 not". The ZOM-547 and ZOM-553 rows and the summary count are wrong | traj #135, #136 (`updatedRows: 21`) | **MATERIAL_FAIL** (from F1) |
| R5 | Register in the ZM Beta sign-off folder `d_69fcebc4…` (Douglas is a writer), not the client QA folder (Douglas is a reader) | File parented to `d_69fcebc484d472907b0b5c` | `gdrive_move_file`, result `parents: ["d_69fcebc484d472907b0b5c"]` | SQL l.8, l.10, l.31; traj #20, #137 | **MET** |
| R6 | Not-on-prod tickets back to Todo, one comment each naming the change still to go out; same ticket, no new tickets | 8 tickets: 336, 392, 518, 256, 550, 435, 503, 557 | All 8 `linear_update_issue state=Todo` calls succeed (for example ZOM-336 shows `status: Todo`, state history Done→Todo at 07:03:22Z). 8 `linear_create_comment` calls name #40, #41, #43, the level pack import, #50, #51, #52 (noting #42 is on prod) and #54. No new tickets | Card rule 5 (SQL l.55); traj #139–#155 | **MET** |
| R7 | Reply to Arthur in the DM with how many tickets are on prod and which ones aren't | "8 on prod" (of 16); not on prod: 256, 336, 392, 435, 503, 518, 550, 557 | Posted to D05QQF7V404: "**18 tickets in scope. 10 are on prod, 8 are not.**" The on-prod list includes ZOM-547 and ZOM-553. The not-on-prod list (8 tickets with reasons) is correct. It adds a correct note that Douglas's Sep 22 DM claims about #41/#51 were wrong | SQL l.46; traj #156 (`ok: true`, channel D05QQF7V404) | **MATERIAL_FAIL** (from F1): the on-prod count Arthur explicitly asked for is wrong; the not-on-prod half is MET |
| R8 | Leonard: after the register is in the folder, share it with him directly with comment access | Share to leonard.hayes@harmonygames.co, role commenter, after the move | `gdrive_share_file` role `commenter`, result confirms; done after the move (#137 → #138). An extra email reply to Leonard (#157) is harmless and no wrong recipients were added | SQL l.80; traj #138, #157 | **MET** |
| R9 | Final response to Douglas reports what was done | Accurate summary | Clear summary of the actions, the not-on-prod reasons and the deploy-log discrepancy. It repeats "18 tickets … 10 on prod" | traj final `result` | **MINOR_GAP**, part of F1 (same count error, not counted separately) |
| R10 | No unauthorized writes (for example, not posting in #zombie-match3d; not rolling back #50/#52; not editing the deploy log) | None | None made; the run explicitly left #50/#52 and the deploy log alone | traj #135–#157 | **MET** |

Output capability: Sheet creation (`gsheets_create_spreadsheet` + `gsheets_values_update`), folder move (`gdrive_move_file`), share (`gdrive_share_file role=commenter`), Linear state change and comment, Slack DM and Gmail reply are all **SUPPORTED**. Each one returned a successful result in this run. There are no capability-caused misses to exclude.

## 3. Grouped failures

| ID | Root cause | Type | Affected outputs | Severity |
|---|---|---|---|---|
| F1 | The run never searched Douglas's mailbox for Arthur's sign-off mail, so it missed his Sep 30 amendment excluding ZOM-547/ZOM-553 from the register and the count | Retrieval failure of a discoverable, accessible, incorporated source | Register (2 extra rows and a wrong summary), Arthur DM (on-prod count 10 instead of 8, with 2 wrong tickets listed), final response | Consequential, bounded |

Why F1 is a real model failure and not a task defect:
- **Discoverable:** the email is in Douglas's INBOX (`label_ids: INBOX, IMPORTANT`). Its subject, "Beta sign-off - server side", is the card's exact name, and a generic search for "sign-off", "beta" or `from:arthur` would match it.
- **Accessible:** it is the persona's own mailbox, and the run had already used the Gmail tool on it (#7).
- **Not a hidden policy:** it is Arthur's own amendment to the rules the prompt delegates.
- **The run had a nudge:** PR #49's title "Boss arena: mirror balance values" appears in its PR listing (#23), and the email's reason is that the backend copies are "only mirrors".

Rejected candidate failures:
- The extra Gmail reply to Leonard is harmless and not a failure.
- Not posting in #zombie-match3d is correct, because Oliver's request is unincorporated.
- The DM's "Correction to what I told you on 9/22" is accurate and helpful.
- A Sheet as the file type is an authorized variation.

## 4. Correct work and usability

All 16 in-scope classifications are right. That includes every trap:
- the approve-after-deploy on #41 and the missing Approve on #43;
- the dev-only deploys #40 and #51 and the dev-only level pack import;
- the calendar freeze date (Sep 26 22:00Z) over the Slack "monday the 29th";
- Arthur's in-freeze Approve on #47, and the in-freeze deploys #50/#52 without his Approve;
- the #44 rollback and redeploy, and the #54 rollback;
- the minute-level cut excluding ZOM-461, and the parent exclusion of ZOM-457.

All 8 Linear Todo moves and comments are correct, and so are the folder, the share and the DM's not-on-prod list. Fixing the result means:
1. delete two register rows and fix the summary line;
2. send Arthur a corrected count (8 of 16).

No ticket state, comment, share or folder needs to change. That is a bounded correction, and most of the delivered work stays usable.

## 5. Task/environment defects and unassessed scope

- Task/environment defects: none found that affect this run. All required reads and writes are supported, and the persona has access to everything needed.
- Unassessed: the export does not embed the prompt text (see §1). Arthur's email being present in the run's environment is inferred from the SQL, because the run never queried it. The same Gmail INSERT block put Leonard's email into the run's environment, and the run did read that one (#8), so this is treated as established.
- Horizon: 157 tool calls, within the Long Horizon 100–500+ tier. Call volume is not hardness evidence.

## 6. Score rationale

**Score 3 (Hard, NON-FAIL).** The run has one genuine, consequential Opus failure (F1). The register given to the CTO for go/no-go contains two tickets he explicitly said to leave off. The headline number he asked for ("how many tickets are on prod") is reported as 10 instead of 8. That is more than a cosmetic or minor defect, so it is not a 2. It changes the register's contents and one of the two answers Arthur requested.

**Why not 4:** there is one root cause, and the correction is bounded (remove 2 rows, fix the count). Every classification, every Linear write, the folder, the share and the not-on-prod list are correct and usable. A 4 needs material failures that require substantial correction across the result.

**Why not 5:** the central result is not invalidated, and most of the core task is done correctly.

### FINAL VERDICT: NON-FAIL
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Assessment version: model-aware-v3

Assessed model: Opus

Assessment mode: OPUS_OBSERVED

Score: 3

Execution status: COMPLETE

Difficulty: Hard

Gate decision: PROCEED

Gate reason: OBSERVED_OPUS_FAILURE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (level not identified by runtime)

Next action: Proceed with dependent authoring (OE, rubric). Keep F1 as the observed failure: a rubric should check that ZOM-547/ZOM-553 are off the register and that the DM reports 8 on prod.

Evidence limits: One run only; no average-score or repeatability claim. The prompt text is not embedded in the export, so task match is inferred from the run's behaviour and the byte-identical prompt versions. Arthur's email being present in the run state is inferred from the applied SQL overlay.
