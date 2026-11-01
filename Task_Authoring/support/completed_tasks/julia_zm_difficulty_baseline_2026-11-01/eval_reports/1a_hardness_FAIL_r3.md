## HARDNESS EVALUATION REPORT (Opus observed)

### Task: Julia delegates Leonard's ZM difficulty baseline: register (Tickets + Rules in force) from the Trello card rules (rule 5 as revised in SQL revision 22), its "Before Monday" checklist and Leonard's DM thread reply; ZM Difficulty folder; share with the Monday invite; rule-6 ticket comments as changed; DM reply with counts, keys and starting-tier timing

## 1. Scope and provenance

| Item | Value |
|---|---|
| Review | `/hardness`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode, actual review date 2026-10-30 |
| Clock | 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Assessment | `model-aware-v3`, mode `OPUS_OBSERVED`, eval `1A_Hardness_Eval.md`; `authority_contract: prompt-incorporation-v1`; `evidence_contract: stage-evidence-v1` |
| Prompt | `Evals/task_inputs/04_Prompt.txt`, revision 23, 525 bytes, sha256 `22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787` (byte-identical to the prompt in the last hardness round) |
| Assignment | `00_Task_Assigned_Inputs.md` sha256 `d39753c9…1e5a51`: Julia Lawson (Product Manager), Product, Engineering Ops, Retrieval, long-horizon |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql`, revision 22, 89,187 bytes, sha256 `52c581f442c120a641e1dc1c7f6b8dd9e4ad089fd9faf5e1a87b7710b4bfba43` (proposed overlay; not executed) |
| Reference files | None; the prompt references none |
| Run | `Evals/task_inputs/opus/trajectory.json` (uploaded as `Run1_trajectory (3).json`, input revision 24), 4,383,355 bytes, sha256 `1c38d9bc8a99fb28acf00e8599be53ef87cf33f4410a6189cb8271dc7c3be036`; session `76960c28-…9060`; 2,126 events; 836 tool calls (596 top-level, 240 in 4 background subagents); run timestamps 2026-10-31T04:51:54Z to 05:02:51Z |

### Run identity, hint status and task/source match

- **Model:** CONFIRMED Opus. Init event (index 0) `model: claude-opus-5-5[1m]`; 892 assistant messages `claude-opus-5-5` (4 `<synthetic>`); `modelUsage` lists only `claude-opus-5-5[1m]` / `claude-opus-5-5` (canonicalModel `claude-opus-5-5`). Claude Code 2.1.280, bypassPermissions.
- **Completion:** final `result` event `subtype: success`, `terminal_reason: completed`, `is_error: false`, `num_turns` 597, final reply present.
- **Subagents:** all 4 background comment-scan subagents (indices 102–115, ZOM-10 to ZOM-566) failed with "Autocompact is thrashing" (system `task_notification` status `failed`). The parent recovered by scanning comments itself: 499 distinct top-level `linear_list_comments` targets covering ZOM-10 to ZOM-509 (only ZOM-460 missing, which returns `issue_not_found`). This is a runtime hiccup the run worked around, not a task defect and not an Agent failure.
- **Unhinted:** no hint evidence. The export omits the initial user turn (normal for this SDK export). Discovery starts cold: own Slack profile (2), user search "Leonard" (3), Leonard DM (6), DM thread (13 fails with `channel_not_found` on the user ID, retried on `D05HB64NMQU` at 29), Trello search "difficulty baseline" (15), card with checklists and actions (18 fails on an invalid `attachments` value, retried at 22). Nothing shows prior knowledge of answers.
- **Prompt match:** the run searches the calendar for "tuning" (36), uses "ZM Difficulty folder" and answers the DM's starting-tier question, matching the saved prompt.
- **SQL version match:** the run's tool results contain the revision-22-only rule 5 sentences "For when a new player gets their starting tier … go by the build." and "write it the way ZOM-42 words it" (9 occurrences each), plus the thread reply "forgot one thing" (3), checklist "rule 6 change" (3) and "rule 7 change" (3). The run saw the current overlay.

## 2. Input and authority issues

- The export lacks the user prompt turn (evidence limit; resolved by behavior and revision-specific strings above; does not affect the band).
- This review replaces the earlier `1a_hardness.md` (run sha `a6b52c7a…5e51`, SQL revision 17). That run predates SQL revisions 18–22 and its score is not inherited.
- No task/environment defects affected the result. Every write path was SUPPORTED and returned success, including `gdrive_share_file` with role `commenter` (2084, 2086).
- Six tool errors (13, 18, 20, 423, 970, 1487) were all self-inflicted argument errors or probes of nonexistent tickets; each was recovered or harmless.

## 3. Requirement map (prompt + incorporated instructions)

Authority chain: the prompt ("go through his ask and everything it points to and build the register the way he set it up", "if his rules say something needs to happen on the tickets", "reply to leonard in the dm with what he asked for") incorporates Leonard's DM (SQL line 44) and its thread reply (line 50). The DM names the difficulty baseline card on the ZM roadmap board (card #80, line 58), with its comment (line 68) and "Before Monday" checklist (lines 70–76: rule 6 and rule 7 changes). Card rules incorporate the session agenda layout (line 17), Blake's store builds mail, the enrage sheet's Live tab (line 22), ZOM-42 and the build. Folder and sharing come from the prompt and rule 7 as changed. No unincorporated policy was used.

Verification marks: NEW = checked in this review against the SQL, base data or the trajectory. REUSED = raw source facts from `1_prompt.md` (same prompt and SQL hashes, revision 22; Phase 0 status derivation).

| # | Requirement | Expected | Observed (trajectory index) | Outcome | Verification |
|---|---|---|---|---|---|
| R1 | Find Leonard's ask, thread reply and card rules incl. comment and checklist | DM line 44 + thread line 50; card #80, comment, checklist | DM (6), thread (29), card with `checklists: all`, `actions: all` (22) | MET | NEW |
| R2 | One sheet, two tabs Tickets and Rules in force (agenda line 17) | New spreadsheet with both tabs | `gsheets_create_spreadsheet` initial tab Tickets (2060); `addSheet` Rules in force (2071) | MET | NEW |
| R3 | Scope: 30 tickets (title matches incl. written-out "attack power", minus Duplicates ZOM-203/276, plus "tiers:" tickets ZOM-221, 281, 300, 305, 378, minus ZOM-30, 49, 50, 161, 262, 275) | 30 tickets | 30 rows, exactly the expected set (2062) | MET | NEW comparison; expected set REUSED from `1_prompt.md`; ZOM-281 "tiers:" note confirmed at SQL line 226 |
| R4 | Columns per rule 2 | Ticket, title, Linear state as found, status, replaced-by | Ticket / Title / Linear state / Status / Replaced by (2062). Titles for ZOM-200 and ZOM-246 rewritten at 2067/2069 to the exact Linear titles, which themselves end in "..." (base `linear/data.json`, confirmed by `hg_records.py`) | MET | NEW |
| R5 | Status per rules 3–4 | Live 17 (23, 42, 45, 199, 221, 246, 258, 263, 274, 281, 282, 288, 295, 300, 303, 305, 378); Editor only 9 (162, 163, 173, 200, 201, 250, 277, 312, 315); Replaced 1 (254 by 282); Not shipped 3 (202 In Progress, 280 Canceled, 293 Todo) | Identical per ticket, states included (2062) | MET | NEW comparison; derivation REUSED |
| R6 | Decoy resistance (ZOM-282 not Replaced by match3d#401; ZOM-250 not Replaced by ZOM-277; ZOM-254 Replaced; ZOM-378 kept despite "tutorial"; ZOM-271 out) | As in R3/R5 | All handled correctly (2062) | MET | NEW |
| R7a | Starting tier, go by the build (rule 5) | After the first 10 games played (wins + losses), average CPM > 90 → tier 1, else tier 0; 90 stays on 0 (`TierManager.cs` line 31 `totalGames == 10`, line 93 `cpm > 90.0f`) | "until the end of their 10th level attempt (10 games played, wins and losses both count) … above 90 (cpm > 90) moves them to tier 1 … 90 exactly stays on tier 0" (2074) | MET | NEW against `TierManager.cs` in the GitHub export |
| R7b | Promotion in ZOM-42's wording | Tier −2 promotes after 1 win; from tier −1, up to the most recent 10 attempts, ≥ 80%; record resets on every change | Same, quoting ZOM-42 incl. early exit and reset (2074) | MET | NEW against ZOM-42 description (base Linear) |
| R7c | Demotion in ZOM-42's wording, plus level drop | 4 losses in a row at any time; ≤ 50% over up to the last 10; reset; level replayed lower after a demotion until won | Same, incl. "can trigger at any time", early-exit examples, the 60–70% no-change line, and the level drop row citing `RetryTierOffset` + `GameLoader` (2074). Extra "Tier range −2 to +5" row matches `TierManager.cs` lines 13–14 | MET | NEW |
| R7d | Enrage: copy the Live tab as it stands (rule 5) | Nine monster rows + MonsterBase 0.8/0.8/0; "Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)" not copied yet; no derived numbers | Exact copy of SQL line 22, including the not-copied row (2074) | MET | NEW, cell-by-cell |
| R8 | Put it in the ZM Difficulty folder | `d_96489e1e00a56685625939` | `gdrive_move_file` newParentId `d_96489e1e00a56685625939`; result parents confirm (2076–2077) | MET | NEW |
| R9 | Share with the invite attendees, rule 7 as changed | robert@ and brian.foster@ writer; leonard.hayes@ and arthur.blake@ commenter (invite SQL line 112) | Exactly these four shares, all successful (2079–2086) | MET | NEW |
| R10 | Rule 6 as changed: 14 comments | ZOM-199 (build checks > 90), ZOM-254 (replaced by ZOM-282), and the 12 Editor only and Not shipped tickets (not in the store builds); nothing else | Exactly these 14 `linear_create_comment` calls, all successful, with correct content per kind (2088–2118) | MET | NEW |
| R11 | Reply to Leonard in the DM after filing | DM D05HB64NMQU; total 30; 17/9/1/3; Not shipped and Editor only keys; starting-tier timing | `slack_send_message` channel D05HB64NMQU, thread_ts `1759261706.530914`, after move and shares (2121); link, 30, 17/9/1/3, all 12 keys, "stays on tier 0 until they've played 10 levels … end of their 10th attempt … above 90" | MET | NEW |
| R12 | No out-of-scope writes (decoys: #zombie-design request, comments on ZOM-42/275, deck or sheet edits) | None | Full write inventory over all 836 calls: 1 spreadsheet create, 1 addSheet, 4 value writes (2 of them title corrections), 1 move, 4 shares, 14 Linear comments, 1 Slack send. Subagent and Bash calls read-only | MET | NEW |
| R13 | Final response to Julia | Faithful summary | Accurate counts, keys, rules, comments and link. One internal contradiction: "**Sharing:** Robert has edit and everyone else can comment", then later in the same reply "gave Brian edit" (the actual share at 2081 is Brian writer) | MINOR_GAP | NEW |

## 4. Grouped failures and independent causes

| ID | Root cause | Affected outputs | Outcome | Evidence | Consequence |
|---|---|---|---|---|---|
| F1 | The final summary's "Sharing" line restates the original rule 7, contradicting the checklist change the run actually applied and describes two paragraphs later | Final response to Julia only | MINOR_GAP | Final `result` text; share call 2081 (`brian.foster@`, `writer`) | Julia could briefly misread Brian's access, but the same reply corrects it and the actual share, the DM to Leonard and the register are all right. No correction to any artifact is needed |

No MATERIAL_FAIL was found. All the seeded difficulty resolved correctly: both late instruction layers (the checklist's rule 6/7 changes and the thread reply's exclusions and key request), rule 5's split authority (build for starting-tier timing, ZOM-42's words for the promotion/demotion window), the written-out attack power rule, the Duplicates, the five "tiers:" tickets (including ZOM-281 with no PR), the Replaced decoys, ZOM-378's "tutorial" title, the comment decoys, the deck's "90 or more" and 4-loss-only demotion, ZOM-42's provisional "6-7 levels", the "Next pass" tab and the uncopied monsters.

## 5. Correct work and usability

The central deliverable is correct and usable as delivered: a 30-ticket register matching the expected set, every state, status and replaced-by cell; a Rules in force tab that states the starting tier as the build runs it, promotion and demotion in ZOM-42's words with both demotion rules and the level drop, and an exact copy of the enrage Live tab; filed in the right folder; shared with the right four people at the right roles; the exact 14 required ticket comments; and an accurate DM reply in Leonard's thread with the total, counts, all 12 keys and the starting-tier answer.

The run used 836 calls, most of them a near-exhaustive comment scan after its subagents failed. Volume and source count are not difficulty on their own: the run handled them and got the answer right.

## 6. Task/environment defects and unassessed scope

- Task/environment defects: none affecting the result. The subagent autocompact failures were a runtime event the Agent recovered from.
- Unassessed: none material. Register contents are established from the exact write payloads plus successful `values_update` results (Tickets A1:E31, Rules A1:D22).
- Evidence limits: one run only; no average-score or repeatability claim. The export omits the initial user turn (resolved above).

## 7. Score rationale

The band is **2 (Easy)**. The run met 12 of 13 requirement groups outright; the only defect (F1) is one contradictory line in the final summary to Julia, and the core result is correct and usable.
- **Why not 3:** score 3 needs a consequential failure that requires correction. F1 changes no artifact: the register, comments, shares and the DM to Leonard are all right, and the same reply states Brian's edit access correctly. The revision-22 change to rule 5 (the new difficulty this round) was applied exactly.
- **Why not 1:** the final response does contain a genuine, if minor, misstatement about the sharing roles.

## 8. Next action and suggested revisions

Gate: HOLD (`INSUFFICIENT_DIFFICULTY`). Opus solved the task again, including rule 5's split authority. The last several rounds added more wording forks to rules the Agent reads directly, and Opus resolves those reliably. Difficulty will more likely come from facts the Agent has to establish rather than read. Natural options within this scenario (no conflicts with `known_base_issues.md` for these records):
- Make shipped status depend on timing, not a label: a ticket that is Done in Linear with a "works on the dev build" note, but whose only merged PR landed in main after the Sep 26 store-build cut in Blake's mail. Under rule 3 it is Not shipped, and the Agent must compare the PR merge date with the cut instead of trusting the closing note.
- Make one register status depend on the code, not the ticket text: for example a ticket whose change sits entirely inside an `#if UNITY_EDITOR` block in match3d, so it is Editor only even though nothing in its title or notes says "editor".
- Let a later closing note or Blake reply partly undo an earlier one (for example a "tiers:" note on a ticket that a later comment reverts before the cut), so the scope or status rests on reading the history in order.

Any change to the prompt or injection SQL needs a fresh matching unhinted Opus run, then `/injection` (if SQL changed), `/prompt` and `/hardness` again, before `/oe` and `/rubric`.

### FINAL VERDICT: FAIL

Assessment version: model-aware-v3

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Assessed model: Opus

Assessment mode: OPUS_OBSERVED

Score: 2

Execution status: COMPLETE

Difficulty: Easy

Gate decision: HOLD

Gate reason: INSUFFICIENT_DIFFICULTY

Evaluator model: Opus 5.5 (claude-opus-5-5), effort unconfirmed

Next action: Revise the task to add a consequential, discoverable difficulty (see section 8), then obtain a fresh unhinted Opus run and rerun /injection (if SQL changed), /prompt and /hardness.

Evidence limits: One run only; no average-score or repeatability claim. The export omits the initial user turn; prompt and SQL match were established from the run's behavior and revision-22-specific strings in its tool results.
