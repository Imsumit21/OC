## HARDNESS EVALUATION REPORT (Opus observed)

### Task: Julia delegates Leonard's ZM difficulty baseline: register (Tickets + Rules in force) from the Trello card rules, its "Before Monday" checklist and Leonard's DM thread reply; ZM Difficulty folder; share with the Monday invite; rule-6 ticket comments as changed; DM reply with counts and keys

## 1. Scope and provenance

| Item | Value |
|---|---|
| Review | `/hardness`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode, actual review date 2026-10-30 |
| Clock | 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Assessment | `model-aware-v3`, mode `OPUS_OBSERVED`, eval `1A_Hardness_Eval.md`; `authority_contract: prompt-incorporation-v1`; `evidence_contract: stage-evidence-v1` |
| Prompt | `Evals/task_inputs/04_Prompt.txt`, revision 18, 525 bytes, sha256 `22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787` |
| Assignment | `00_Task_Assigned_Inputs.md` sha256 `d39753c9…1e5a51`: Julia Lawson (Product Manager), Product, Engineering Ops, Retrieval, long-horizon |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql`, revision 17, 88,468 bytes, sha256 `10c1ee9238d42bf41259cdb6afdeb728f93246abd2ab65f56275d75b4cf3ce18` (proposed overlay; not executed) |
| Reference files | None; the prompt references none |
| Run | `Evals/task_inputs/opus/trajectory.json` (uploaded as `Run1_trajectory (2).json`, input revision 19), 2,465,082 bytes, sha256 `a6b52c7a120e62216539cfb92045d0184e925c1c74e57a19f5b764919eb305a1`; session `a7438d45-…5a92`; 706 events; 222 tool calls (114 top-level, 108 in 3 read-only subagents) |

### Run identity, hint status and task/source match

- **Model:** CONFIRMED Opus. Init event (index 0) `model: claude-opus-5-5[1m]`; assistant messages `claude-opus-5-5`; `modelUsage` lists only `claude-opus-5-5[1m]` / `claude-opus-5-5` (canonicalModel `claude-opus-5-5`). Claude Code 2.1.280, bypassPermissions.
- **Completion:** final `result` event `subtype: success`, `terminal_reason: completed`, `num_turns` 115, final reply present. 3 subagents spawned and completed (2 later stopped by the parent after their results were in, indices 539/542), no failures.
- **Unhinted:** no hint evidence. The export omits the initial user turn (normal for this SDK export). Discovery starts cold: own Slack profile (2), user search "Leonard" (4), Leonard DM (6), DM thread (13), Trello search "difficulty baseline" (15), card with checklists and actions (18). No narration or call shows knowledge of answers before retrieval.
- **Prompt match:** the run uses "ZM Difficulty folder" and searches the calendar for "tuning" (39), matching the saved prompt (revision 18, byte-identical to 15).
- **SQL version match:** the run's tool results contain the revision-17-only strings: Leonard's thread reply "forgot one thing" (3 hits), checklist "rule 6 change" (4) and "rule 7 change" (3), plus earlier current strings "Copy its Live tab as it stands" (9), "incl. PartyGirl 50HP" (4), "written out (ATK on its own" (3). The run saw the current overlay.

## 2. Input and authority issues

- The export lacks the user prompt turn (evidence limit; resolved by behavior and revision-specific strings above; does not affect the band).
- This review replaces the earlier `1a_hardness.md` (run sha `ecfae005…6d91`, SQL revision 14). That run predates SQL revision 17 and is not inherited.
- No task/environment defects affected the run. Every needed write path was SUPPORTED and returned success, including `gdrive_share_file` with role `commenter` (668, 670), which `/prompt` listed as UNVERIFIED.

## 3. Requirement map (prompt + incorporated instructions)

Authority chain: the prompt ("go through his ask and everything it points to and build the register the way he set it up", "if his rules say something needs to happen on the tickets", "reply to leonard in the dm with what he asked for") incorporates Leonard's DM (SQL line 44) and its thread reply (line 50). The DM names card #80 on the ZM roadmap board (line 58) with its comment (line 68) and its "Before Monday" checklist (lines 70–76: rule 6 and rule 7 changes). Card rules incorporate the session agenda layout and Blake's store builds mail. Folder and sharing come from the prompt and rule 7 as changed. No unincorporated policy was used.

Verification marks: NEW = checked in this review against SQL, base data or the trajectory. REUSED = raw source facts from `1_prompt.md` (same prompt and SQL hashes; Phase 0 status derivation), spot-checked where noted.

| # | Requirement | Expected | Observed (trajectory index) | Outcome | Verification |
|---|---|---|---|---|---|
| R1 | Find Leonard's ask, the thread reply and the card rules incl. comment and checklist | DM line 44 + thread line 50; card #80, comment, checklist | DM (6), thread (13, 20, 29); card with `checklists: all`, `actions: all` (18, 22) | MET | NEW |
| R2 | One sheet, two tabs Tickets and Rules in force | New spreadsheet with both tabs | `gsheets_create_spreadsheet` initial tab Tickets (652); `addSheet` Rules in force (654) | MET | NEW |
| R3 | Scope: 35 rule-1 tickets minus the six Leonard leaves off (30, 49, 50, 161, 262, 275); ZOM-271 out; Duplicates 203/276 out; "tiers:" tickets 221, 300, 305, 378 in | 29 tickets | 29 rows, exactly the expected set (656); exclusions named in DM (701) | MET | NEW: ticket-by-ticket comparison with `1_prompt.md` Phase 0 lists. "tiers:" completeness checked: the SQL has exactly four "tiers:" closing notes (lines 192, 244, 248, 294); `hg_search.py search linear "tiers:"` over base `linear/data.json` (scan_complete true) finds only ZOM-42's description, not a closing note |
| R4 | Columns per rule 2 | Ticket, title, Linear state as found, status, replaced-by | Ticket / Title / Linear state / Status / Replaced by (656), with a note "Linear states as found on Oct 1" | MET | NEW; states ZOM-202 In Progress, 280 Canceled, 293 Todo match `1_prompt.md` facts (REUSED) |
| R5 | Status per rules 3–4 | Live 16 (23, 42, 45, 199, 221, 246, 258, 263, 274, 282, 288, 295, 300, 303, 305, 378); Editor only 9 (162, 163, 173, 200, 201, 250, 277, 312, 315); Replaced 1 (254 by 282); Not shipped 3 (202, 280, 293) | Identical per ticket (656) | MET | NEW comparison; expected derivation REUSED from `1_prompt.md` |
| R6 | Decoy resistance: ZOM-282 not Replaced by match3d#401; ZOM-250 not Replaced by ZOM-277; ZOM-254 Replaced despite close-date order; ZOM-378 kept despite "tutorial" in its title | As in R5 | ZOM-282 Live, ZOM-250 Editor only, ZOM-254 Replaced by ZOM-282, ZOM-378 Live | MET | NEW |
| R7a | Rules tab: starting tier as in the store builds | First 10 **games** played (wins + losses) average CPM > 90 → tier 1, else tier 0 (`TierManager.cs` lines 30–32 `totalGames == 10`, line 93 `cpm > 90.0f`; `Player/WinHistory.cs` line 147 `GetTotalWins() + GetTotalLosses()`) | "After the 10th level, average CPM over those 10 levels > 90 moves the player to tier 1 … 90 exactly stays on tier 0" (658); promotion row says "from level 11 on" | MINOR_GAP | NEW: code read in the GitHub export; the run fetched TierManager.cs (553) |
| R7b | Promotion | Tier −2: one win; tier ≥ −1: ≥ 80% over up to last 10 since last change | Same, with early exit and record reset (658) | MET | NEW against `WinRateRule.cs` (read by run, 554) |
| R7c | Demotion and level drop | 4 losses in a row or ≤ 50% over up to last 10 (tier ≥ −1); current level drops one tier until won | Same; "Tier -2 is the floor"; level-drop row cites ZOM-303 (658) | MET | NEW |
| R7d | Enrage: copy the Live tab as it stands (rule 5) | Nine monster rows + MonsterBase 0.8/0.8, hp 0; "Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)" not copied yet; no derived numbers | Exact copy including the not-copied row (658); "Next pass" tab (read at 239) not used | MET | NEW against SQL line 22 |
| R8 | Put it in the ZM Difficulty folder | `d_96489e1e00a56685625939` | `gdrive_move_file` newParentId `d_96489e1e00a56685625939`, parents confirmed in result (660–661) | MET | NEW |
| R9 | Share with the invite attendees, rule 7 as changed | robert@ and brian.foster@ writer; leonard.hayes@ and arthur.blake@ commenter (invite SQL line 112) | Exactly these four shares, all successful (663–670) | MET | NEW |
| R10 | Rule 6 as changed: 14 comments | ZOM-199 (build checks > 90), ZOM-254 (replaced by ZOM-282), and the 12 Editor only and Not shipped tickets (not in the store builds); nothing else | Exactly these 14 `linear_create_comment` calls, all successful (672–699), with correct content per kind | MET | NEW |
| R11 | Reply to Leonard in the DM after filing | DM D05HB64NMQU; total 29; 16/9/1/3; Not shipped and Editor only keys | `slack_send_message` channel D05HB64NMQU, thread_ts `1759261706.530914` (Leonard's ask), after move and shares (701); link, 29, 16/9/1/3, all 12 keys | MET | NEW |
| R12 | No out-of-scope writes (decoys: #zombie-design request, comments on ZOM-42/275, extra Replaced comments, deck edits) | None | Full write inventory over all 222 calls: 1 spreadsheet create, 1 addSheet, 2 value writes, 1 move, 4 shares, 14 Linear comments, 1 Slack send; subagents and Bash calls read-only | MET | NEW |
| R13 | Final response to Julia | Faithful summary | Matches the actual writes and counts; discloses its "tiers:" scan scope honestly (final result event) | MET | NEW |

## 4. Grouped failures and independent causes

| ID | Root cause | Affected outputs | Outcome | Evidence | Consequence |
|---|---|---|---|---|---|
| F1 | Stated the starting-tier window in the written sources' unit ("10th level", "those 10 levels", "from level 11 on") instead of the build's unit (games played, wins + losses), though it read the code | Rules in force, Starting tier cell (and the "level 11" phrase in Promotion) | MINOR_GAP | `TierManager.cs` lines 30–32 and 93; `Player/WinHistory.cs` line 147; run row at 658 | A player who loses early gets bucketed before reaching level 10. The > 90 threshold, boundary and outcomes are right, and the run's own Promotion/Demotion rows correctly speak of "attempts". One-phrase fix; no effect on the ticket register, counts, comments, shares or DM |

No MATERIAL_FAIL was found. All the seeded difficulty resolved correctly: both late instruction layers (the checklist's rule 6/7 changes and the DM thread reply's exclusions and key request), the written-out attack power rule (ZOM-271 out), the Duplicates, the four "tiers:" tickets, the ZOM-282/#401 and ZOM-250/277 Replaced decoys, the ZOM-254 close-date trap, ZOM-378's "tutorial" title, the comment decoys on ZOM-42/275, the #zombie-design request, the deck's "90 or more" and stale +25% HP, the "Next pass" tab and the uncopied monsters.

## 5. Correct work and usability

The central deliverable is correct and usable as delivered: a 29-ticket register matching the expected set, every status and the replaced-by cell, filed in the right folder, shared with the right four people at the right roles, the exact 14 required ticket comments, and an accurate DM reply in Leonard's thread with counts and all 12 keys. The Rules tab is correct apart from F1 and flags real deck-vs-build discrepancies.

The run used about 114 top-level calls plus 108 subagent comment reads (222 total). Volume and source count are not difficulty on their own: the run handled them and got the answer right.

## 6. Task/environment defects and unassessed scope

- Task/environment defects: none affecting the run.
- Unassessed: none material. Register contents are established from the exact write payloads plus successful `values_update` results (Tickets A1:E33, Rules A1:D23).
- The run's comment scan covered keyword tickets and Blake-assigned tickets only (about 107). That was a risk, not a miss: the full base search plus the SQL show no other "tiers:" closing note.
- Evidence limits: one run only; no average-score or repeatability claim. The export omits the initial user turn (resolved above).

## 7. Score rationale

The band is **2 (Easy)**. The run met 12 of 13 requirement groups outright, with one minor imprecision (F1); the core result is correct and usable.
- **Why not 3:** score 3 needs a consequential failure requiring correction. F1 is one wording choice in one tab cell that matches the written rule text the card names (ZOM-42, Robert's deck). It leaves the threshold and outcomes right and doesn't touch the register, counts, comments, sharing or DM. The revision-17 additions (checklist, thread reply) were the new difficulty this round, and the run applied both completely.
- **Why not 1:** the run had the code in hand (553) and still stated a window the store builds don't use, against rule 5's "as they work in the store builds today". That's a genuine, if minor, defect.

## 8. Next action and suggested revisions

Gate: HOLD (`INSUFFICIENT_DIFFICULTY`). Opus solved this task again, including the two new instruction layers. Natural ways to add consequential difficulty within this scenario (check `known_base_issues.md` before building on base records):
- Make shipped status depend on timing, not a label: a ticket that is Done in Linear but whose only merged PR landed in main after the Sep 26 store-build cut in Blake's mail, so it is Not shipped. The Agent must compare PR merge dates with the cut instead of reading closing notes.
- Put a "tiers:" closing note on a ticket that is neither keyword-matched nor assigned to Blake. This run narrowed its comment scan to exactly those two groups and said so; a note outside them would turn that shortcut into a real miss.
- Make a value only the code settles change the register or the DM (for example a ticket whose shipped status depends on whether its change is behind an editor-only `#if UNITY_EDITOR` block), so the build check carries weight beyond one Rules-tab cell.

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

Evidence limits: One run only; no average-score or repeatability claim. The export omits the initial user turn; prompt and SQL match were established from the run's behavior and revision-specific strings in its tool results.
