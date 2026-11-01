## HARDNESS EVALUATION REPORT (Opus observed)

### Task: Julia takes over Leonard's ZM difficulty baseline. She builds the register (Tickets and Rules in force tabs) from the Trello card rules, Leonard's card comment, the "notes for monday" doc, the "Before Monday" checklist, Blake's store builds mail and his separate reply, Leonard's two DM thread replies and Robert's group-DM column request. She files it in ZM Difficulty, shares it with the Monday invite, comments on tickets under rule 6 as changed, and replies to Leonard in the DM.

## 1. Scope and provenance

| Item | Value |
|---|---|
| Review | `/hardness`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode, actual review date 2026-10-31 |
| Clock | 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Assessment | `model-aware-v3`, mode `OPUS_OBSERVED`, eval `1A_Hardness_Eval.md`; `authority_contract: prompt-incorporation-v1`; `evidence_contract: stage-evidence-v1` |
| Prompt | `Evals/task_inputs/04_Prompt.txt`, revision 46, 525 bytes, sha256 `22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787` (byte-identical to the last hardness round) |
| Assignment | `00_Task_Assigned_Inputs.md` sha256 `d39753c9…1e5a51`: Julia Lawson (Product Manager), Product, Engineering Ops, Retrieval, long-horizon, medium |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql`, revision 45, 98,831 bytes, sha256 `f6afeda7b08647d790a5d96b5bd7ccb2cb6291d83fadf4bd9f2ae2a79f5362f8`. Proposed overlay, not executed. `0_injection.md` PASS and `1_prompt.md` PASS (5) are on this hash. Changed since the last hardness round (revision 42): Robert's group-DM column request (lines 47–50) and card rule 2's new sentence (lines 73, 81) |
| Reference files | None. The prompt references none |
| Run | `Evals/task_inputs/opus/trajectory.json` (uploaded as `Run1_trajectory (7).json`, input revision 47), 4,985,335 bytes, sha256 `35adc2283efcafead8a4728255fa16a592b762aa22907fbd4becfce7c1d4fd24`; session `795ab2c3-…523702`; 2,779 events; 908 tool calls (237 top-level, 671 in 12 background subagents); run timestamps 2026-10-31T22:23:02Z to 22:31:21Z |

### Run identity, hint status and task/source match

- **Model:** CONFIRMED Opus. The init event (index 0) shows `model: claude-opus-5-5[1m]`. 977 assistant messages are `claude-opus-5-5` (plus 10 `<synthetic>`), and `modelUsage` lists canonicalModel `claude-opus-5-5` only. Claude Code 2.1.280, bypassPermissions.
- **Completion:** the final `result` event has `subtype: success`, `terminal_reason: completed`, `is_error: false`, `num_turns` 238, and a final reply is present.
- **Subagents:** 12 background agents scanned Linear comments. The first four (ranges 10–134, 135–259, 260–384, 385–520) and batches A, B, C, D and F all ended `failed` ("Autocompact is thrashing", task_updated at 1394, 1405, 1412, 1463, 2522, 2556, 2572, 2618, 2649). The parent then **stopped** batches E, G and H while they were still running (TaskStop at 2666, 2680, 2689) and never collected their results. The subagent failures themselves are runtime events and are not counted. What the parent did next is counted (see F1).
- **Unhinted:** no hint evidence. The export omits the initial user turn, which is normal for this SDK export. Discovery starts cold:
  - own Slack profile (2), user search, the Leonard DM, then both thread replies via `slack_read_thread` (19, 21);
  - Trello search "difficulty baseline" (24), the card with checklists and actions (28, after an invalid-argument retry at 26), attachments (30);
  - Blake's reply thread `julia.lawson@harmonygames.co/1844695547248825769` (61), then group DMs (`slack_channels_list` mpim at 71) and Robert's thread (78).
- **Prompt match:** the run searches for the tuning invite, files into "ZM Difficulty", shares with the invite, comments on tickets and answers the starting-tier question. This matches the saved prompt.
- **SQL version match (revision 45):** at 79 the run reads Robert's revision-45-only reply in `CAFC495E4006` ("yeah three things after status please. who it's assigned to in linear, the day it got marked done …", SQL line 50). It also builds the three columns from it (text at 83). Revision 42 records also appear: Blake's separate reply thread (61) and both DM thread replies (20, 22).

## 2. Input and authority issues

- The export lacks the user prompt turn. This is an evidence limit. The run's behavior and the revision-45-specific record above resolve it, and it does not affect the band.
- This review replaces the earlier `1a_hardness.md`, which graded run sha `dc029b70…3163` (upload (6)) against SQL revision 42 (score 4). That score is not inherited.
  - **Reused facts (REUSED, `1_prompt.md` on the same prompt and SQL hashes):** the in-scope set and status derivation (24 tickets: Live 16, Editor only 4, Replaced 1, Not shipped 3), the 9 comments, shares (Robert writer; Brian and Leonard commenter; Arthur reader), the Rules in force expectations, and the per-ticket Linear assignee/priority/completed_at table (its §"Linear fields for the 24 tickets").
  - **Rechecked here (NEW):** SQL lines 26 (enrage Live tab), 19 (agenda), 50, 52, 58, 73 (card rules 1–7), 244, 278, 298, 302, 348 (the five "tiers:" notes). Linear `data.json` `/issues/3334` (ZOM-281), `/issues/3245` (ZOM-200) and `/issues/3295` (ZOM-246) via `hg_records.py`. The helper matched these records but flagged "Source changed during the read" (`scan_complete: false`). They are positive matches with full records, not absence claims, so the flag doesn't affect them.
- Tool errors: an invalid `attachments` argument (26), two `channel_not_found` from using a user ID as the channel (13, 15), and an unprefixed tool name (2695). All were self-inflicted and recovered at once.
- No task or environment defect affected the result. `linear_list_comments` worked for the parent throughout (about 100 direct calls), so the comment that was missed was reachable.

## 3. Requirement map (prompt + incorporated instructions)

**Authority chain.** These prompt phrases carry the requirements:
- "go through his ask and everything it points to and build the register the way he set it up";
- "if his rules say something needs to happen on the tickets";
- "reply to leonard in the dm with what he asked for".

Together they bring in:
- Leonard's DM request (SQL line 52) and both of his thread replies (lines 58 and 62);
- card #80's rules (line 73), its comment, the "Before Monday" checklist and the notes doc;
- Blake's store builds mail and his reply;
- through card rule 2, Robert's group-DM reply (line 50).

No unincorporated policy was used.

| # | Requirement | Expected | Observed (trajectory index) | Outcome |
|---|---|---|---|---|
| R1 | Find Leonard's full ask: the DM, **both thread replies**, card rules, comment, checklist, notes doc, Blake's mail and reply, **Robert's group-DM columns** | All of these | DM (6–10); both thread replies read (19–22); card with checklists/actions (28); attachments (30); notes doc; Blake's reply thread (61); group DM and Robert's thread (76, 78) | MET |
| R2 | One sheet, two tabs: Tickets and Rules in force (agenda, SQL line 19) | New spreadsheet with both tabs | `gsheets_create_spreadsheet` "Tickets" (2724), `batch_update` adding "Rules in force" (2726) | MET |
| R3 | Scope: 24 tickets = 31 title matches minus Duplicates and ZOM-312, plus the 5 "tiers:" tickets (ZOM-221, **281**, 300, 305, 378), minus the 11 Leonard leaves off | 24 rows | **23 rows** (payload 2728; result `updatedRange Tickets!A1:H24`). All 11 exclusions were applied, along with ZOM-312 off and both Duplicates out. **ZOM-281 is missing.** It is a Done ticket created 2025-06-19 (`/issues/3334`) whose title has no scope word ("Win streak not lost when replaying without main menu"). Its only route in is Blake's closing note "tiers: closing. checked on the dev build" (SQL line 278, author `usr_cc3e90160f490686` = arthur.blake@) | **MATERIAL_FAIL** (F1) |
| R4 | Columns per rule 2 + Robert: ticket, title, Linear state, status, then assignee, done day, priority; replaced-by | As listed | Ticket / Title / Linear state / Status / Assignee / Done date / Priority / Replaced by (2728) | MET |
| R5 | Status per rules 3–4 on in-scope tickets | Live 16, Editor only 4 (173, 200, 277, 315), Replaced 1 (254 by 282), Not shipped 3 (202, 280, 293) | All 23 listed rows have the expected status and replaced-by value. Live is 15 only because ZOM-281 is absent | MET for listed rows (the count error is F1) |
| R6 | Robert's three columns, per ticket (Linear `assignee_id`, `completed_at`, `priority`) | Values per `1_prompt.md` table; done day blank for ZOM-202, 280, 293 | All 23 rows × 3 cells match. Assignee tokens are as shown (EMPLOYEE_0032_NAME on 246, 254, 263, 274, 280). Priority uses Linear labels (Urgent/High/Medium/Low). ZOM-200/274/282 use the UTC day (accepted). Done day is blank on exactly 202, 280 and 293. The ZOM-281 row (EMPLOYEE_0032_NAME, Urgent, 2025-06-27) is absent with its ticket | MET for listed rows |
| R7 | Decoy resistance: ZOM-282 not Replaced by a PR, ZOM-250 handling, ZOM-378 kept despite "tutorial", ZOM-312 off per PR #265, ZOM-258 off per the notes, ZOM-173/277/315 kept as Editor only | As expected | All handled correctly (2728; PR #265 review read at 2702) | MET |
| R8 | Titles as in Linear | Linear `title` | Two cells rewritten to the truncated titles Linear actually stores (2738, 2740). `/issues/3245` and `/issues/3295` titles end in "Th..." and "a ..." in the base | MET |
| R9 | Rules in force tab (rule 5) | Starting tier from the build (10th game, `cpm > 90`, exactly 90 stays on 0). Promotion/demotion in ZOM-42's words. Level drop after demotion. Enrage = exact copy of the Live tab incl. "not copied yet" | All present (2742). The enrage table matches SQL line 26 cell by cell. Promotion and demotion quote ZOM-42 ("UP TO THE MOST RECENT 10 attempts", "win rate for up to the last 10 games is 50% or lower", 4-loss streak, reset). Level drop is yes. An extra "System" row is not required and not scored | MET |
| R10 | File in the ZM Difficulty folder | `d_96489e1e00a56685625939` | `gdrive_move_file` to that parent; result `parents` confirms (2745–2746) | MET |
| R11 | Share with the invite per rule 7 as changed (checklist, notes, Leonard's second reply) | robert@ writer; brian.foster@ commenter; leonard.hayes@ commenter; arthur.blake@ reader | Exactly these four roles, all successful (2747–2754) | MET |
| R12 | Rule 6 as changed: 9 comments; the 7 Editor only / Not shipped ones name iOS 0.3.49 and Android 0.3.133; none on ZOM-162, 163, 201, 250 | ZOM-199 (build checks > 90 at the 10th game), ZOM-254 (replaced by ZOM-282), 173, 200, 277, 315, 202, 280, 293 | Exactly 9 `linear_create_comment` calls, all successful (2756–2773), with correct content. All 7 Editor only / Not shipped comments name both builds. No forbidden comments. ZOM-281 needs no comment (Live, no wrong-text note) | MET |
| R13 | DM reply to Leonard after filing | In DM D05HB64NMQU: folder/link, total **24**, per-status counts **16/4/1/3**, keys of the 3 Not shipped and 4 Editor only tickets, which ticket replaced which, starting-tier timing | Delivered (2775, result `ok: true`) as a thread reply under his request ("reply here"), after filing and sharing. Correct: link/folder; access line; Editor only and Not shipped keys; "ZOM-254 … was replaced by ZOM-282"; starting tier (10th game, > 90, exactly 90 stays on 0); all 11 exclusions listed. **Wrong: "23 tickets made the list" and "Live: 15". It also tells Leonard the "tiers:" notes added only "221, 300, 305 and 378"** | **MATERIAL_FAIL** (F1): the two figures Leonard explicitly asked for ("how many tickets made the list and how many of each status") are wrong |
| R14 | No out-of-scope writes | None beyond the required set | Full top-level write inventory: 1 spreadsheet create, 1 batch update, 4 value writes, 1 move, 4 shares, 9 Linear comments, 1 Slack send. Subagents made no writes | MET |
| R15 | Final response to Julia | Faithful summary | Accurate about what was done, but it repeats 23 tickets / Live 15 | MINOR_GAP (follows from F1; not counted separately) |

### Output capability ledger

| Action | Path | Status |
|---|---|---|
| Create sheet + tabs + values | `gsheets_create_spreadsheet`, `gsheets_batch_update`, `gsheets_values_update` (successful results 2725–2743) | SUPPORTED |
| File in folder | `gdrive_move_file` (2746) | SUPPORTED |
| Share with roles | `gdrive_share_file` with `writer`/`commenter`/`reader` (all accepted, 2748–2754) | SUPPORTED |
| Ticket comments | `linear_create_comment` (2757–2773) | SUPPORTED |
| DM reply | `slack_send_message` (2776) | SUPPORTED |
| Read ticket comments | `linear_list_comments` (worked in about 100 direct parent calls; ZOM-281's result at 560 and 2400 inside subagents shows the "tiers:" note) | SUPPORTED, not used by the parent for ZOM-281 |

## 4. Grouped failures and independent causes

| ID | Root cause | Affected outputs | Outcome | Evidence | Consequence |
|---|---|---|---|---|---|
| F1 | **Premature completion of the "tiers:" scan: ZOM-281 was never checked by the parent, and it stopped the subagent that had found it.** The parent read comments directly only on a chosen set of mostly arthur.blake-assigned tickets (its own note at 1474: "scanning Blake's tickets directly"). It handed the rest to batches A–H. ZOM-281 is assigned to `usr_EMPLOYEE_0032`, so it fell in batch E. Batch E had already returned the match: at 2398–2400 it read ZOM-281's comments, and its own summary at 2643 lists "ZOM-281 … 'tiers: closing. checked on the dev build'". The parent killed batch E at 2666 while it was running and built the register without its results or a direct check. The earlier 260–384 agent had also found the same match (558–560, summary 864) before it failed. Card rule 1 counts "any ticket Blake counts as tier work … his closing note on those starts with 'tiers:'", whoever the assignee is | (a) Tickets tab: one Live row missing (23 vs 24). (b) DM reply: wrong total and Live count (23 / 15 vs 24 / 16), and an incomplete list of "tiers:" additions. (c) Final summary to Julia repeats it | MATERIAL_FAIL | SQL lines 73 (rule 1), 278 (ZOM-281 note); Linear `/issues/3334` (Done, created 2025-06-19, non-matching title); trajectory 1474, 1742 (batch E list incl. 281), 2400, 2643, 2666 (TaskStop), 2728 (register payload), 2775–2776 (DM payload and delivered result) | The baseline omits a shipped tier ticket the card explicitly brings in, and Leonard received wrong headline figures. Shares, comments, the rules tab and every other register row are unaffected |

This is one independent cause. Its affected outputs are counted once. The subagent context failures are runtime events. They are not the cause: the parent's direct `linear_list_comments` calls kept working, and the result that would have prevented the miss was in the agent it chose to stop.

## 5. Correct work and usability

Almost all of the result is correct and usable as delivered. **Every failure from the previous round is fixed in this run:**
- **Discovery:** both of Leonard's DM thread replies were read (19–22). Blake's separate reply was found under its new subject. Robert's revision-45 group-DM request was found by listing group DMs.
- **Scope:** all 11 exclusions applied (30, 49, 50, 161, 162, 163, 201, 250, 258, 262, 275). ZOM-312 was taken off per Blake's "not tiers" PR review. Four of the five "tiers:" tickets were found, ZOM-378 was kept despite "tutorial", and the Duplicates were left out.
- **Statuses and columns:** every listed ticket has the expected status and replaced-by. All 69 assignee / done day / priority cells match Linear, with done day blank on exactly the three never-done tickets.
- **Rules in force:** fully correct, including an exact enrage copy with "not copied yet".
- **Delivery:** right folder; all four shares at the right roles (Brian as commenter, Arthur as viewer); exactly the 9 required comments, with both builds on the seven that need them, and none on the four removed tickets.
- **DM reply:** the Not shipped and Editor only keys, the replaced-by line, the starting-tier answer and the correct access line.

The run used 908 calls. Call volume is not difficulty evidence on its own and is not counted.

## 6. Task/environment defects and unassessed scope

- **Task/environment defects:** none affecting the result. Twelve subagents hit a runtime context-thrash error (9 failed). The parent's own tool access was unaffected, and the needed record was reachable and had in fact been retrieved.
- **Unassessed:** nothing material. The register rests on the exact `values_update` payloads plus their successful results. The shares, comments and DM rest on their payloads plus successful results.
- **Evidence limits:**
  - One run only; no average-score or repeatability claim.
  - The export omits the initial user turn (resolved in section 1).
  - `hg_records.py` reported a transient "Source changed during the read" on Linear `data.json`. The three records used are positive matches with full content, so no absence claim depends on it.

## 7. Score rationale

The band is **3 (Hard)**. One genuine model failure (F1) left a required result wrong:
- the register omits a Live ticket that card rule 1 explicitly brings in, which is the trap the "tiers:" rule sets for a non-Blake assignee;
- the DM gives Leonard the wrong total (23) and Live count (15), and those two figures are what he asked for in his request.

Fixing it is bounded: add one row (ZOM-281 | Win streak not lost when replaying without main menu | Done | Live | EMPLOYEE_0032_NAME | 2025-06-27 | Urgent) and send Leonard a corrected count (24; Live 16). No write needs undoing, and every other output is correct.

- **Why not 2:** a score of 2 means only minor defects, with the core result correct. Here the scope of the central deliverable is wrong, and the headline numbers delivered to the requester are wrong. That is an omitted required result that changes correctness and delivery, so it is MATERIAL_FAIL, not a cosmetic gap.
- **Why not 4:** a score of 4 needs substantial correction across the result. Here the correction touches one register row and one DM message. The sharing, the 9 ticket comments, the rules tab and 23 of 24 rows with all their columns are right, and nothing has to be deleted or reverted.

## 8. Next action

Gate: PROCEED (`OBSERVED_OPUS_FAILURE`). This clears only the hardness gate. Keep the F1 evidence for dependent authoring. In the rubric and OEs, these are the items this run actually failed. Check each one explicitly:
- ZOM-281 included as Live (the non-Blake-assigned "tiers:" ticket);
- the 24 total and Live 16 in the DM.

Keep them separate from the items the run got right this time: both thread replies (the 11 exclusions), Brian as commenter, no comments on ZOM-162/163/201/250, the keys in the DM, Robert's three columns, Blake's separate reply, ZOM-312, the enrage copy and the builds in the comments.

`2_oe.md` and `3_rubric.md` predate SQL revision 45, which both of them read. Send `/oe` and then `/rubric` again on the current inputs. Any later change to the prompt or injection SQL needs a fresh matching unhinted Opus run, then `/injection` (if SQL changed), `/prompt` and `/hardness` again, before `/oe` and `/rubric`.

### FINAL VERDICT: NON-FAIL

Assessment version: model-aware-v3

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Assessed model: Opus

Assessment mode: OPUS_OBSERVED

Score: 3

Execution status: COMPLETE

Difficulty: Hard

Gate decision: PROCEED

Gate reason: OBSERVED_OPUS_FAILURE

Evaluator model: Opus 5.5 (claude-opus-5-5), effort unconfirmed

Next action: Proceed with dependent authoring (/oe, then /rubric, on the revision-45 SQL); retain the F1 evidence (ZOM-281 "tiers:" ticket missed after the parent stopped the subagent that found it: 23 rows instead of 24, and a wrong 23 / Live 15 count in Leonard's DM).

Evidence limits: One run only; no average-score or repeatability claim. The export omits the initial user turn; prompt and SQL match were established from the run's behavior and the revision-45-only group-DM record in its tool results.
