## HARDNESS EVALUATION REPORT (Opus observed)

### Task: Julia delegates Leonard's ZM difficulty baseline: register (Tickets + Rules in force) from the Trello card rules, ZM Difficulty folder, share with the Monday invite, rule-6 ticket comments, DM reply with counts

## 1. Scope and provenance

| Item | Value |
|---|---|
| Review | `/hardness`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode, actual review date 2026-10-30 |
| Clock | 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Assessment | `model-aware-v3`, mode `OPUS_OBSERVED`, eval `1A_Hardness_Eval.md`; `authority_contract: prompt-incorporation-v1`; `evidence_contract: stage-evidence-v1` |
| Prompt | `Evals/task_inputs/04_Prompt.txt`, revision 15, 525 bytes, sha256 `22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787` |
| Assignment | `00_Task_Assigned_Inputs.md` sha256 `d39753c9…1e5a51`: Julia Lawson (Product Manager), Product, Engineering Ops, Retrieval, long-horizon |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql`, revision 14, 86,342 bytes, sha256 `a58a5d1e61b32432ff8a931fc5e55f957b11ab54d0e813f9a9bffdcde99958a3` (proposed overlay; not executed) |
| Reference files | None; the prompt references none |
| Run | `Evals/task_inputs/opus/trajectory.json` (uploaded as `Run1_trajectory.json`), 3,987,348 bytes, sha256 `ecfae0050886e10679f8b54eab0721af3cd6ddec518cd4bd9b17fdbb3c486d91`; session `65da0129-…947275`; 2,174 events |

### Run identity, hint status and task/source match

- **Model:** CONFIRMED Opus. The init event (index 0) says `model: claude-opus-5-5[1m]`. All 808 non-synthetic assistant messages say `claude-opus-5-5`. `modelUsage` lists only `claude-opus-5-5` / `claude-opus-5-5[1m]` (canonicalModel `claude-opus-5-5`). Claude Code 2.1.280, bypassPermissions.
- **Completion:** two `result/success` events (index 0 of the background wait, then the final one, `terminal_reason: completed`), and the final reply is present (index 2171). The second init (index 907) has the same session_id: it is a continuation after background agents, not a separate run.
- **Unhinted:** no hint evidence. The export does not contain the initial user turn, which is normal for this SDK export. The run's discovery path starts cold: it reads its own Slack profile (2), searches for "Leonard" (4), reads the DM (6), then searches Trello for "difficulty baseline" (13). That is the path the bare prompt implies. No narration or call shows knowledge of answers before retrieval.
- **Prompt match:** the run uses "ZM Difficulty folder" and the tuning invite (gcal search "tuning", 20). Those come from prompt revisions 2–5, which are byte-identical (md5 `17027eb5…`), not from revision 1 ("put it where it's supposed to go"). Matches the saved prompt.
- **SQL version match:** the run's tool results contain all three revision-13/14-only strings: card rule 5 "Copy its Live tab as it stands" (3 hits), Trello comment "written out (ATK on its own" (3), and the Live-tab label "incl. PartyGirl 50HP" (4). Uploads (8) and (9) are byte-identical. The run saw the current overlay.

## 2. Input and authority issues

- The export lacks the user prompt turn (evidence limit; resolved by behavior plus the saved prompt as above; does not change the band).
- No task/environment defects affected the run. Every needed write path was SUPPORTED and returned success, including `gdrive_share_file` with role `commenter`, which earlier stages listed as UNVERIFIED.
- Background subagents: 11 spawned, 8 failed, 3 killed by the parent. The parent re-ran the comment scans itself (204 top-level `linear_list_comments`). This was self-recovered and caused no task loss, so it is not a model-failure finding.

## 3. Requirement map (prompt + incorporated instructions)

Authority chain: the prompt ("go through his ask and everything it points to and build the register the way he set it up", "if his rules say…") incorporates Leonard's DM (SQL line 44, D05HB64NMQU). The DM names the Trello card ("the rules for the register are on the difficulty baseline card on the zm roadmap board"; card #80, SQL lines 56/64) and its comment (line 66). Rule 2 incorporates the session agenda layout (line 16); rule 3 incorporates Blake's store builds mail. The folder and sharing come from the prompt and card rule 7. No unincorporated policy was used.

Verification marks: NEW = checked in this review against SQL/base/trajectory. REUSED = raw source facts from `1_prompt.md` (sha of current report, same prompt/SQL hashes, Phase 0 / requirement ledger), re-checked where noted.

| # | Requirement | Expected | Observed (trajectory index) | Outcome | Verification |
|---|---|---|---|---|---|
| R1 | Find Leonard's ask and the rules | DM line 44, then card #80 + updateCard + comment | DM read (6); `trello_search` (13); `trello_get_comments` (16) | MET | NEW |
| R2 | One sheet, two tabs "Tickets" and "Rules in force" (agenda) | New spreadsheet with both tabs | `gsheets_create_spreadsheet` title "ZM difficulty baseline register", initial tab Tickets (2146); `addSheet` "Rules in force" (2148) | MET | NEW |
| R3 | Scope: rule 1 whole-word keywords + "attack power" written out, plus "tiers:" closing notes, Duplicates out, created ≤ Aug 31 | 35 tickets: 31 title matches (ZOM-203, 276 out; ZOM-271 "ATK POWER" out) + ZOM-221, 300, 305, 378 | 35 rows, same set; ZOM-203/276 noted as duplicates excluded; ZOM-271 absent (2150) | MET | NEW: membership compared ticket by ticket; ZOM-271/203/276 titles checked in `linear/data.json` /issues |
| R4 | Columns per rule 2: ticket, title, Linear state as found, status, replaced-by | Five columns | Ticket / Title / Linear state (as found, Oct 1) / Status / Replaced by (2150) | MET | NEW; states ZOM-202 In Progress, 280 Canceled, 293 Todo, 23 Done match base `state_id`; truncated titles (ZOM-200, 246) match base text |
| R5 | Status per rules 3–4 against Blake's store builds mail | Live 22 (23, 30, 42, 45, 49, 50, 161, 199, 221, 246, 258, 262, 263, 274, 275, 282, 288, 295, 300, 303, 305, 378); Editor only 9 (162, 163, 173, 200, 201, 250, 277, 312, 315); Replaced 1 (254 by 282); Not shipped 3 (202, 280, 293) | Identical per ticket (2150) | MET | NEW comparison; expected derivation REUSED from `1_prompt.md` |
| R6 | Decoy resistance: ZOM-282 not Replaced by match3d#401; ZOM-250 not Replaced by ZOM-277; ZOM-254 Replaced despite close-date order | As expected in R5 | ZOM-282 Live, ZOM-250 Editor only, ZOM-254 Replaced by ZOM-282 | MET | NEW |
| R7a | Rules tab: starting tier "as it works in the store builds today" | Avg CPM of first 10 **games** (wins + losses) > 90 → tier 1, else tier 0 (`TierManager.cs` `if (totalGames == 10)`, `ApplyInitialBucketing` `cpm > 90.0f`; `WinHistory.GetTotalGames()` = wins + losses) | "Set once, after the first 10 **levels**: average CPM over those 10 above 90 starts you on tier 1… exactly 90 stays on tier 0" (2152) | MINOR_GAP | NEW: code read at `…/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs` lines 28–35, 85–105 and `WinHistory.cs` `GetTotalGames`. The run fetched TierManager.cs (435), which includes `totalGames == 10` |
| R7b | Promotion | Tier ≤ -2: one win; tier ≥ -1: ≥ 80% over up to the last 10 | Same, with early exit and history reset (2152) | MET | NEW: `WinRateRule.cs` Defaults lines 22–34; `ApplyTierChange` → `ResetTierWinHistory` |
| R7c | Demotion and level drop | 4 losses in a row or ≤ 50% over up to the last 10 (tier ≥ -1); current level drops one tier until won | Same; "Tier -2 is never demoted"; level-drop row cites ZOM-303 (2152) | MET | NEW: `WinRateRule.cs`; `RetryTierOffset--` on demotion, reset on win |
| R7d | Enrage: copy the Live tab as it stands (rule 5) | 10 rows with numbers incl. MonsterBase 0.8/0.8, hp 0; "Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)" as not copied yet; no derived numbers | Exact copy, including the "not copied yet" row (2152); "Next pass" decoy not used | MET | NEW against SQL line 22 |
| R8 | Put it in the ZM Difficulty folder | Folder `d_96489e1e00a56685625939` | `gdrive_move_file` newParentId `d_96489e1e00a56685625939`, parents confirmed (2154) | MET | NEW (folder id REUSED from `1_prompt.md`) |
| R9 | Share with everyone on the invite: Robert edits, others comment | robert@ writer; leonard.hayes@, arthur.blake@, brian.foster@ commenter (attendees per SQL lines 100–108) | Exactly these four shares, all successful (2157–2163) | MET | NEW |
| R10 | Rule 6 ticket comments, only two kinds | ZOM-199 (Blake's reply: build checks > 90) with what the build does; ZOM-254 naming ZOM-282; nothing else | ZOM-199: "the starting tier check is cpm > 90, not >= 90…" (2165); ZOM-254: "Replaced by ZOM-282…" (2167); no other Linear writes | MET | NEW |
| R11 | Reply to Leonard in the DM with ticket total and per-status counts, once it's in the folder | DM D05HB64NMQU after the move; 35; 22/9/1/3 | `slack_send_message` → channel D05HB64NMQU (2169), after move and shares; link, 35, 22/9/1/3 | MET | NEW |
| R12 | No out-of-scope writes (decoys: #zombie-design request, comments on ZOM-42/275, extra Replaced comments) | None | One Slack send (DM only); two Linear comments only; no Trello/Drive edits beyond the register | MET | NEW: full write inventory over all 741 tool calls |
| R13 | Final response to Julia | Faithful summary | Summary matches the actual writes and counts (2171) | MET | NEW |

## 4. Grouped failures and independent causes

| ID | Root cause | Affected outputs | Outcome | Evidence | Consequence |
|---|---|---|---|---|---|
| F1 | Copied the written sources' wording ("first 10 level", ZOM-42/ZOM-199/deck) for the starting-tier window instead of the build's unit, although it had read the code | Rules in force, "Starting tier" cell only | MINOR_GAP | Expected: `TierManager.cs` `totalGames == 10`, `GetTotalGames()` = wins + losses. Observed: "after the first 10 levels" (2152). Base ZOM-42 itself notes assignment "after the first 6-7 levels" (`linear/data.json` /issues/3485) | A player who loses early gets a tier before level 10. The threshold, the > 90 boundary, the tier outcomes and every other rule row are correct. It's a one-phrase correction with no effect on the ticket register, the counts, the comments, the sharing or the DM |

No MATERIAL_FAIL was found. The other deliberately seeded traps all resolved correctly: ZOM-271 excluded, the Duplicates excluded, the "tiers:" tickets found through a full comment scan, the ZOM-282/#401 and ZOM-250/277 Replaced decoys, the ZOM-42/275 comment decoys, the #zombie-design request, the deck's "90 or more" and stale +25% HP, the enrage "Next pass" tab and the uncopied monsters.

## 5. Correct work and usability

The central deliverable is correct and usable as delivered. The 35-ticket register matches the expected set, every per-ticket status and the replaced-by cell. It's filed in the right folder, shared with the right people at the right roles, and backed by exactly the two required ticket comments and an accurate DM reply. The Rules tab is correct apart from F1, and it also flags three real deck-vs-build discrepancies.

## 6. Task/environment defects and unassessed scope

- Task/environment defects: none affecting the run.
- Unassessed: none material. The register contents are established from the exact write payloads plus successful `values_update` results (Tickets A1:E40, Rules A1:D21). No separate artifact copy is needed.
- Evidence limits: one run only; no average-score or repeatability claim. The export omits the initial user turn (resolved above).

## 7. Score rationale

The band is **2 (Easy)**. The run met all 13 requirement groups apart from one minor imprecision (F1), and the core result is correct and usable.
- **Why not 3:** score 3 needs a consequential failure that requires correction. F1 is one wording choice in one cell. It matches the written rule text the card itself names ("written up in Robert's dynamic difficulty deck and in ZOM-42"). It leaves the threshold and outcomes correct and doesn't touch the register, counts, comments, sharing or DM. Treating it as consequential would inflate severity.
- **Why not 1:** the run had the code in hand (index 435) and still stated a window that the store builds don't use, against rule 5's "as they work in the store builds today". That's a genuine, if minor, defect.

Call volume (741 tool calls, 619 of them comment scans) and the scenario's many sources don't show difficulty on their own: the run handled the volume and got the answer right.

## 8. Next action and suggested revisions

The gate is HOLD (`INSUFFICIENT_DIFFICULTY`). For the hardness gate, Opus solved this task. Natural, task-relevant ways to make it harder, built on what this scenario already has (check `known_base_issues.md` before building on base records):
- Make shipped status depend on timing rather than a label. For example, a ticket that is Done in Linear, but whose only merged PR landed in main after the Sep 26 store-build cut in Blake's mail, so it isn't in the store builds. The Agent then has to compare PR merge dates against the cut instead of reading closing notes.
- Put a later, scoped correction to one card rule in a less obvious place that the card or DM still points to, for example a reply in Blake's store-builds thread that changes what counts as Editor only for one folder. That way one rule in force has to be reconciled across two sources.
- Make a Rules in force value that only the code settles change the register or the DM, so the store-builds-vs-docs check carries weight instead of only one tab cell.

Any change to the prompt or injection SQL needs a fresh matching unhinted Opus run, then `/injection` (if SQL changed), `/prompt` and `/hardness` again.

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

Evidence limits: One run only; no average-score or repeatability claim. The export omits the initial user turn; prompt and SQL match were established from the run's behavior and from revision-specific strings in its tool results.
