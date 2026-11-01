## PROMPT EVALUATION REPORT

### Task: Julia delegates Leonard's ZM difficulty baseline: build the register (Tickets + Rules in force) from the Trello card rules, file and share it, comment on tickets per the card, reply to Leonard in the DM with counts
### Assigned Persona: Julia Lawson - Product Manager (roster `julia_lawson`, julia.lawson@harmonygames.co)
### Assigned Business Function: Product
### Assigned Competency: Engineering Ops
### Assigned Task Skill: Retrieval
### Assigned Horizon: long-horizon (Task Type field; Difficulty Mode "medium" recorded as context)

Review: `/prompt`, chat review of attempt 6adfee3ef9092601a61245bb. Actual review date 2026-10-30. Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut), universe `Universe_SynthCut` (hg4-synth-sep30cut v16).

Inputs: `04_Prompt.txt` (515 bytes, sha256 in the verdict block), `00_Task_Assigned_Inputs.md` (all five fields stated; clears intake), `01_Universe_Inject.sql` (82,412 bytes, sha256 `37a8c7ab3444732ff708fe4590c47f186c99f44d6de88e67699dc9590c4e5080`). No error/async config, dynamic context or reference files were supplied; none is referenced by the prompt.

---

### Injection Gate
- State: NEVER_REVIEWED (the gate reads `reports/input_manifest.json`, which this portal's writer never creates; no manifest entry exists).
- Eval 0 handling: a `0_injection.md` report from today covers the identical SQL hash (`37a8c7ab…5080`, revision 4) under `injection-static-v2` with **FINAL VERDICT: PASS**, COMPLETE. I re-ran `hg_injection_lint.py` on the saved SQL (injection-lint-v1: 0 FAIL / 0 CHECK / 0 INFO) and re-checked every task-relevant row directly (below). Static ID/structure checks A–B are REUSED from that report. Check C items this prompt depends on were re-done here.
- Reviewed SQL sha256: `37a8c7ab3444732ff708fe4590c47f186c99f44d6de88e67699dc9590c4e5080`. Eval 0 verdict: PASS.
- Eval 0 findings on records this prompt depends on: none. The schema advisories (A1 `linear_comments.sequence`, A2 gslides `notes`/`table_json`/`ordinal` not in the unverified snapshot) are load risks only. If the live table rejects a column, the whole transaction rolls back and the task's Linear comments and deck disappear. They stay advisories here and do not change a score.

---

### Phase 0: Sources read

Docs/references: Eval 1 in full, the `hg_reference.py guide prompt` view, `prompt_rubric_reliability.md`, `deep_recheck.md`, `common_errors.md`, `acl.md`, `roster.json`, tool `catalog.json`, `known_base_issues.md`. The PDFs in `Evals/Docs` were not re-extracted. Eval 1's inline bands and local overrides were applied (evidence limit; no check depends on PDF text beyond what Eval 1 restates).

Universe exploration, synth-cut base plus the SQL overlay:
- **Linear** (`linear/data.json`, 553 ZOM issues; base `comments` is empty, so all 109 ZOM comments come from the SQL). A whole-word title scan for the card words plus "attack power" (card comment), created 2025-04-21..2025-08-31 UTC, finds 33 tickets. ZOM-203 and ZOM-276 are Duplicate, leaving 31. Adding the four tickets whose Blake closing note starts "tiers:" (ZOM-221, 300, 305, 378) gives **35**. ZOM-23 and ZOM-30 are among the 31 and sit on the start edge (F3). No title match falls between Aug 31 and Sep 1 UTC/PT; the next one is ZOM-517 on 2025-09-03.
- **GitHub** match3d: PRs #243 (ZOM-173/307), #244 (ZOM-303), #265 (ZOM-312), #271 (ZOM-295), #401 (enrage split; comment "this also finishes the hp part of ZOM-282"). Code: `Assets/Scripts/DynamicDifficulty/TierManager.cs` (`if (totalGames == 10)`, `cpm > 90.0f`, MinTier -2 / MaxTier 5, win history reset on each tier change), `WinRateRule.cs` (tier ≤ -2 one win promotes; ≥80% of last 10 promotes; ≤50% of last 10 demotes; 4 losses demote), `LevelEditor/UI/StatsPanel.cs` ("Total Attack Power"), VarC monster prefabs (enrage values identical to the sheet's Live tab).
- **Slack**: DM D05HB64NMQU (members include Julia EMPLOYEE_0005 and Leonard EMPLOYEE_0038). #zombie-design C090N54TG79 is private, and its members include Julia, Leonard, Arthur 0025, Brian 0026 and Vincent 0012. Base #executives has Leonard on 2025-09-29: "I just released IOS 0.3.49" and "this is the latest Android - 0.3.133", which match Arthur's mail.
- **Gmail**: Arthur's "store builds for monday" (2025-09-30 09:12Z) and reply (13:26Z, cpm > 90) are in Julia's mailbox.
- **Trello**: card "Difficulty baseline (Julia)" on ZM ROADMAP plus the Sep 30 comment adding "attack power". The decoy card "Difficulty baseline" on Product Roadmap is a Domino Delights card.
- **Drive/Docs/Sheets/Slides/GCal**: folder ZM Difficulty (Leonard owns it, Julia is a writer); agenda doc; Julia's own "ZM monster enrage" sheet (Live / Next pass / History) inside that folder; Robert's deck (shared with Julia); event "ZM difficulty tuning" on 2025-10-06 with attendees Leonard, Julia, Robert, Arthur and Brian.

Status derivation under the card rules (UTC reading, 35 rows): **Not shipped 3** (ZOM-202 In Progress "nothing merged", ZOM-280 Canceled, ZOM-293 Todo). **Editor only 9** (ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315). **Replaced 1** (ZOM-254 → ZOM-282). **Live 22** (ZOM-23, 30, 42, 45, 49, 50, 161, 199, 221, 246, 258, 262, 263, 274, 275, 282, 288, 295, 300, 303, 305, 378). This is the evaluator's derivation, given only to show the task is solvable. It is not a golden answer.

---

### Requirement ledger

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Find Leonard's Tuesday DM ask | SQL slack row (D05HB64NMQU, 2025-09-30T19:48Z) | Slack DM history / search | `slack_*` read/search | Julia is a DM member | Ask: register, counts reply |
| "everything it points to": card rules | Trello card 68daca58… desc + commentCard 68dbfa43… | DM names "difficulty baseline card on the zm roadmap board" | `trello_get_cards_on_board`, `trello_get_card`, `trello_get_comments` | Trello unscoped | Rules 1–7 + "attack power" addendum |
| Ticket scope (rule 1) | Linear ZOM issues + SQL comments ("tiers:") | Linear list/search; per-ticket comments | `linear_*` search/get, `linear_list_comments` | Linear unscoped | 35 tickets (UTC reading); 33 on the Pacific reading (F3) |
| Status per ticket (rule 3–4) | Arthur's mail + reply; Linear states/comments; GitHub PRs, comments, code | Gmail search; Linear; `github_get_file_contents`, PR reads | Gmail read, GitHub reads | Mailbox; GitHub unscoped | Live / Editor only / Replaced / Not shipped |
| Rules in force tab (rule 5) | Deck (slides), ZOM-42, Arthur reply (cpm > 90), Arthur Slack (deck blunder slide old), enrage sheet Live tab, code | GSlides, Linear, Gmail, Slack, GSheets, GitHub | `gslides_get_presentation_text`, `gsheets_values_batch_get` | Deck shared with Julia; sheet owned by Julia; #zombie-design member | Start tier >90 over first 10 levels → tier 1; promotion 80%/10 and tier -2 one win; demotion 4 losses or ≤50%/10, level drops one tier after demotion (ZOM-303); per-monster enrage speed/damage, HP 0 |
| Build register: one sheet, tabs Tickets + Rules in force | Agenda doc; card rule 2 | GDocs | `gsheets_create_spreadsheet`, `gsheets_batch_update`, `gsheets_values_update` | Write (ACL-free) | New spreadsheet |
| Put it in ZM Difficulty | Card rule 7 | Drive folder d_9648… | `gdrive_move_file` (or create with parent) | Julia is a writer on the folder | File in folder |
| Share: Robert edit, others comment | Card rule 7 + invite attendees | GCal event on Julia's calendar | `gdrive_share_file` (role param) | Calendar invite visible | Robert writer; Leonard, Arthur, Brian commenter |
| Ticket comments (rule 6) | Card rule 6 | Linear | `linear_create_comment` | Write | Comments on Replaced tickets and on tickets that state something the build doesn't do; set is open, see F1 |
| Reply to Leonard in DM with counts | DM | Slack | `slack_send_message` | Write | Total and per-status counts |

Output capability: spreadsheet creation, tab creation (batch update), move to folder, share and Linear comments are all SUPPORTED by declared catalog tools. The `commenter` role value is a free-string parameter and no base file shows it, so runtime acceptance is UNVERIFIED. That is an evidence limit, not a failure.

---

### Phase 1: Prompt Structure & Persona

**Persona:** PASS (5)
- Julia Lawson is an exact roster entry (Product Manager, Product). The CEO-to-PM delegation, the casual voice and ownership of a difficulty baseline all fit. Julia owns the enrage sheet in the folder, and the card says "Julia owns this one".

**Assigned Competency:** PASS (5)
- Engineering Ops: reconciling tickets against what shipped in store builds, PR/code checks and ticket comments are ticket/release-ops work.

**Assigned Task Skill:** PASS (5)
- Retrieval is the core of the work: collecting every in-scope ticket, its state and shipped status, and the rule values from five sources.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y — PASS
- Dynamic change: the deck's ">= 90"/"+25% HP" is superseded by Arthur's reply (cpm > 90) and Arthur's Slack ("the blunder part of robert's tiers deck is old"). Brian's "+50% … every monster" decoy is contradicted by the enrage sheet and the prefabs. Brian's claim that the editor bits shipped is contradicted by Arthur's mail.
- Multi-source: Slack, Trello, Linear, Gmail, GitHub, Slides, Sheets, Drive and Calendar. Decoys: the Domino "Difficulty baseline" card, the "Next pass" tab, Vincent's channel request.
- Data seeding: PASS. The rules live in the card, the mail and the agenda; the prompt stays short.

**Naturalness:** FAIL (scored under Contrived, see 2.7)
- First person, lowercase, natural shortcuts, no document formatting, no polished connectives. The one defect is the hidden destination and recipients (2.7).

**Anti-Patterns:**
| Pattern | Status |
|---------|--------|
| Command List | PASS. One short "then reply" at the end; no step list |
| Bolt-On | PASS. Every clause serves the baseline |
| Pre-Solving | PASS. No cause, counts or tickets named |
| Tool Mention | PASS. "dm", "tickets" and "folder" are natural service nouns |

**Diversity:** Goes well beyond "investigate + post one Slack message": a sheet with two tabs, a folder move, role-based sharing, several Linear comments and a DM reply over a 35-ticket cohort.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** FAIL (2)

### Unique Ground Truth comparison

Unique Ground Truth: FAIL 2

Basis: Three record-driven forks change required writes, contents and counts: (1) card rule 6's comment set is open, because store-build code contradicts ticket text in places no record flags (ZOM-42 "6-7 levels" vs totalGames == 10; ZOM-275 "Stronger and Faster!" vs the shipped "Faster and Deadlier!"), and Not shipped tickets are not addressed; (2) ZOM-282 is Live-with-comment or Replaced by match3d\#401; (3) the Apr 21 scope start read as a UTC or Pacific day moves ZOM-23 and ZOM-30. No prompt sentence or persona-visible record settles any of them.

Alternative selection: Rule 6 is written for every ticket, and the code shows more discrepancies than the seeded records flag. Rule 4 does not say whether splitting one enrage value into per-monster speed/damage values is a numbers change. The card window has no timezone.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Rule 6 applies to every ticket statement the store builds contradict, including ones only the code shows (ZOM-42 placement after 6-7 levels, ZOM-275 message text); ZOM-282 Live with a per-monster comment; scope in UTC days. | Comments on ZOM-199, ZOM-282, ZOM-254 and also ZOM-42 and ZOM-275; ZOM-282 Live; ZOM-23 and ZOM-30 in scope. | Create the register spreadsheet (Tickets and Rules in force tabs), move it into ZM Difficulty, share Robert as editor and Leonard, Arthur and Brian as commenters, post rule-6 and Replaced comments on the affected Linear tickets, and reply in the D05HB64NMQU DM. Includes comments on ZOM-42 and ZOM-275. | ZM Difficulty folder; Linear tickets; Leonard DM D05HB64NMQU. | Extra correction comments on ZOM-42 (placement after 10 levels) and ZOM-275 (shipped text); register 35 rows; DM counts include ZOM-23 and ZOM-30. | CARD\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Where a ticket says something the store builds don''t do, comment on it with what they actually do."; Z42A (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "gets assigned after the first 6-7 levels based on CPM"; CODE10 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 31-31): "if (totalGames == 10)"; FTUE (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Data/Tutorials/Tutorial Bar Full.asset lines 110-113): "Faster and" |
| B | Comment only where a seeded record flags the difference (ZOM-199 from Blake's reply, ZOM-282 from the enrage sheet) plus Replaced ZOM-254; ZOM-42 is handled by rule 4 alone and code-only discrepancies get no comment. | Comments on ZOM-199, ZOM-282 and ZOM-254 only; ZOM-282 Live; ZOM-23 and ZOM-30 in scope. | Create the register spreadsheet (Tickets and Rules in force tabs), move it into ZM Difficulty, share Robert as editor and Leonard, Arthur and Brian as commenters, post rule-6 and Replaced comments on the affected Linear tickets, and reply in the D05HB64NMQU DM. No comments on ZOM-42 or ZOM-275. | ZM Difficulty folder; Linear tickets; Leonard DM D05HB64NMQU. | No ZOM-42 or ZOM-275 comment; register 35 rows; DM counts include ZOM-23 and ZOM-30. | CARD\_42 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "ZOM-42 is the system itself: it stays Live and its rules go on the rules tab." |
| C | The card window is read in the company Pacific day; ZOM-23 (04:51Z) and ZOM-30 (05:34Z) were created Apr 20 PT and fall outside. | ZOM-42 handled as in A; ZOM-23 and ZOM-30 excluded. | Create the register spreadsheet (Tickets and Rules in force tabs), move it into ZM Difficulty, share Robert as editor and Leonard, Arthur and Brian as commenters, post rule-6 and Replaced comments on the affected Linear tickets, and reply in the D05HB64NMQU DM. Includes a comment on ZOM-42. | ZM Difficulty folder; Linear tickets; Leonard DM D05HB64NMQU. | Register omits ZOM-23 and ZOM-30; DM total and Live count are each two lower than A. | CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "every ZOM ticket created Apr 21 - Aug 31 that changed difficulty"; Z23 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3277): "2025-04-21T04:51:38Z"; Z30 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3354): "2025-04-21T05:34:29Z" |
| D | match3d\#401 changed how ZOM-282 works (one shared value split into independent per-monster speed and damage values), so ZOM-282 is Replaced by match3d\#401. | ZOM-282 Replaced by match3d\#401; otherwise as A. | Create the register spreadsheet (Tickets and Rules in force tabs), move it into ZM Difficulty, share Robert as editor and Leonard, Arthur and Brian as commenters, post rule-6 and Replaced comments on the affected Linear tickets, and reply in the D05HB64NMQU DM. ZOM-282 comment names match3d\#401 as the replacement. | ZM Difficulty folder; Linear tickets; Leonard DM D05HB64NMQU. | ZOM-282 status Replaced; DM counts Live 21 and Replaced 2 instead of 22 and 1. | PR401 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /pull\_requests/2299): "Monster enrage now scales speed and damage independently"; CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "changed how it works (not just its numbers), so it no longer works the way the ticket says" |

Explicit option inventory: The saved prompt contains no explicit option list; status options sit in the incorporated card, not the prompt.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "build the register the way he set it up"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. Rule 6 covers any ticket that says something the store builds do not do; the code contradicts ZOM-42 and ZOM-275 with no seeded record flagging it, and rule 4 gives ZOM-42 its own handling. No record limits the comment set.
Resolution evidence: CARD\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Where a ticket says something the store builds don''t do, comment on it with what they actually do."; CARD\_42 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "ZOM-42 is the system itself: it stays Live and its rules go on the rules tab."; Z275 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3327): "Making Them Stronger and Faster!"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | A decides ZOM-42 and ZOM-275 need corrections; B decides they do not. |
| writes | DIFFERENT | A adds Linear comments on ZOM-42 and ZOM-275; B does not. |
| destinations | SAME | Both use the same folder, tickets and DM. |
| contents | DIFFERENT | Only A contains those correction texts. |

Resolution relevance challenge: Both cited card passages govern exactly this ticket; ZOM-42 itself and TierManager.cs show the discrepancy that would trigger rule 6.
Delegation challenge: NOT_CLAIMED. The prompt delegates detail calls ("go with your read") but no source authorizes either write outcome as interchangeable.
Challenge evidence: Z42A (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "gets assigned after the first 6-7 levels based on CPM"; Z303 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3358): "many of our levels only have 2 tiers of difficult, 0 and 1"

Compared alternative: C
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. The card window has no timezone, the task clock is Pacific, and Linear stores UTC; ZOM-23 and ZOM-30 change membership and counts at that edge.
Resolution evidence: CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "every ZOM ticket created Apr 21 - Aug 31 that changed difficulty"; Z23 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3277): "2025-04-21T04:51:38Z"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | A includes two tickets C excludes. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Register rows and DM counts differ by two. |

Resolution relevance challenge: The timestamps sit inside the UTC/PT gap for the start date the card names.
Delegation challenge: NOT_CLAIMED. No record names a timezone for the window.
Challenge evidence: Z30 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3354): "2025-04-21T05:34:29Z"

Compared alternative: D
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. The \#401 comment says it finishes ZOM-282's hp part, but the PR also made speed and damage independent; rule 4 does not say whether that counts as how it works or only its numbers.
Resolution evidence: GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 179-179): "this also finishes the hp part of ZOM-282"; Z282 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "We can start at +50% to both."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Live vs Replaced for ZOM-282. |
| writes | DIFFERENT | The ZOM-282 comment names a replacement only under D. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Status cell, replaced-by cell and DM counts differ. |

Resolution relevance challenge: Both cited passages speak to whether \#401 replaced or completed ZOM-282.
Delegation challenge: NOT_CLAIMED. No record authorizes either status as interchangeable.
Challenge evidence: PR401 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /pull\_requests/2299): "Monster enrage now scales speed and damage independently"

Strongest-alternative challenge (B): B is the reading a careful agent following only the seeded corrections would take; it removes required Linear writes, so it is not a strawman.
Challenge evidence: CARD\_42 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "ZOM-42 is the system itself: it stays Live and its rules go on the rules tab."

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

Forks settled by records (full list in the Deep Recheck fork list):
- Demotion rule: `WinRateRule.cs` ships both rules (≤50% of last 10, 4 losses), matching ZOM-42. The deck's single line is a summary.
- Starting tier: Blake's reply ("the starting tier check in the build is cpm > 90, not >= 90") and `TierManager.cs` `cpm > 90.0f`.
- ZOM-315: `LevelEditor/UI/StatsPanel.cs` is the only place "Total Attack Power" exists, so it is Editor only.
- ZOM-45 is Live, settled by Blake's note "the game reads it when it loads the level". ZOM-173 and ZOM-312 are Editor only, settled by their closing notes.
- ZOM-254 was replaced first by ZOM-282: ZOM-280 is Canceled and ZOM-274 is a bug fix.
- Enrage numbers come from the enrage sheet's Live tab (card rule 5). It matches the VarC prefabs and outranks Brian's "+50%", the deck and the Next pass tab.
- Sharing goes to the invite list (card rule 7: "Share it with everyone on the tuning session invite"). Vincent's channel request is outside that rule.

**Feasibility:** PASS (5). Every ask maps to cataloged tools. All data exists. Numeric values (enrage per monster, CPM threshold, 80%/50%/4 losses) are tool-visible in the sheet, the mail and code. Every breakdown has fields: status comes from Linear state, comments and code; per-monster values are sheet rows.

**Persona ACL Reachability:** PASS (5). Scoped reads: DM (member), #zombie-design (member), Arthur's mails (Julia's mailbox), the invite (Julia's calendar), folder/doc/deck/sheet (writer, shared, shared, owner). The #zombie-prs bot copy of the #401 comment is in a channel Julia isn't in, but the same comment is in GitHub (unscoped).

**Explicit Tool Mention:** PASS (5).

**Clarity & Specificity:** FAIL (2). Action Decision Ambiguity: "if his rules say something needs to happen on the tickets, go ahead and do that too" brings in card rule 6, and its readings lead to different Linear writes. Under one reading ZOM-42 and ZOM-275 get correction comments; under the other they don't. Not shipped tickets may or may not get comments. Nothing picks one. Same records as UGT fork F1.

**Contrived / Unnatural:** FAIL (2). Hidden destination and recipients the persona would know: "put it where it's supposed to go and share it with the people who should have it". Julia owns "ZM monster enrage" inside the ZM Difficulty folder (SQL drive row, owner julia.lawson@) and is an attendee on the "ZM difficulty tuning" invite. The card states both plainly: "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite". This matches the 2026-10-17 calibration (#42 "wherever that's actually been asked for", #47). No other contrived flags: no staged typos, no opaque IDs, no trap hint. "if his rules say something needs to happen on the tickets" reads as a pointer to the card, not a riddle.

**Alignment with Today's Date:** PASS (5). "tuesday" resolves to 2025-09-30 (DM 19:48Z, 12:48 PT). "monday's tuning session" resolves to 2025-10-06 17:00Z. Nothing treated as done sits after the clock.

**Originality:** N/A (no comparison samples supplied).

**Truthfulness:** PASS (5). Leonard (EMPLOYEE_0038 = Leonard Hayes) DMed on Tue Sep 30. The Monday session exists. "the dm" and "his rules" (the card the DM names) exist. No departed person acts.

**Tool Use & Cross-service:** PASS (5). Linear sets the cohort, Gmail sets the shipped rules and cpm > 90, GitHub and code set Editor only and demotion, Sheets sets the enrage numbers, Calendar sets the share list. Writes span Sheets, Drive, Linear and Slack.

**Investigation + Action:** PASS (5). Investigation feeds every write: register rows, comments, counts.

**Coherence (Bolt-on):** PASS (5).

**Business Function:** PASS (5). Product (a PM preparing a design-tuning baseline).

---

### Phase 3: Universe Feasibility

**Data Existence:** PASS (5). Every needed entity was verified and is retrievable through cataloged reads (Linear issues and comments, Trello card and comments, Gmail threads, Slack history, Drive/Sheets/Slides/Docs, GCal, GitHub PRs/comments/file contents).

**Cross-Service Coherence:** NON-FAIL (3)
- Inconsistencies in task-touched data: one minor Temporal Field Inconsistency, found by deep recheck P2 and confirmed. The card's only lifecycle actions are createCard `2025-09-29T18:05:12Z` (its ObjectId timestamp decodes to the same second) and the 2025-09-30 15:41Z comment. There is no updateCard. Yet the description already cites "Blake's store builds mail" (sent 2025-09-30T09:12:44Z), the session agenda (created 18:31:09Z) and the invite (created 18:24:51Z). It changes no order, window, count, recipient or destination the answer uses, so it scores NON-FAIL rather than FAIL. Otherwise: Injected Linear comments all sit before or at their tickets' completion/cancel times and match their states ("nothing merged" only on open or never-done tickets). Injected Slack authors are channel members. Arthur's "Leonard released it yesterday" matches Leonard's #executives "I just released IOS 0.3.49" (2025-09-29). The sheet's Live tab equals the VarC prefab values. Calendar, doc and deck dates precede the clock.
- Base-code note (not scored; nothing graded depends on it): `Monster.cs SetEnrage` sums the speed percentage per enrage but passes a single `enrageDamagePercentage` to `EnrageDamage`, so damage does not stack across blunders. Keep rubric rows on the sheet's per-blunder numbers and off stacking behaviour.
- Known base-data issues (not scored): none. The task touches no Snowflake or Confluence data.
- Injection SQL considered: Yes.
- Static integrity evidence: REUSED from `0_injection.md` (same SQL hash, injection-static-v2 PASS, checks A–B). Task-relevant Check C re-done directly here.
- Prompt-specific sources, access and configuration: supported (no error/async config).

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|-----------|--------------|-------------|---------------|
| Prompt | Unique Ground Truth | 2 | F1 open rule-6 comment set, F2 ZOM-282 Live vs Replaced, F3 Apr 21 UTC vs PT edge |
| Prompt | Feasibility | 5 | All asks cataloged; data exists |
| Prompt | Persona ACL Reachability | 5 | Every scoped read visible to Julia |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 2 | Write-action divergence on ticket comments |
| Prompt | Contrived / Unnatural | 2 | Hidden destination and recipients the persona knows |
| Prompt | Alignment with Today's Date | 5 | Tue Sep 30, Mon Oct 6 resolve |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied |
| Prompt | Truthfulness | 5 | Premises verified |
| Prompt | Tool Use & Cross-service | 5 | Each service changes a graded fact |
| Prompt | Investigation + Action | 5 | Investigation feeds the writes |
| Prompt | Coherence (Bolt-on) | 5 | None |
| Prompt | Persona | 5 | Fits a PM |
| Prompt | Business Function | 5 | Product |
| Prompt | Assigned Competency | 5 | Engineering Ops |
| Prompt | Assigned Task Skill | 5 | Retrieval |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three dimensions, seeded |
| Universe | Data Exists | 5 | Verified |
| Universe | Cross-Service Coherence | 3 | Card cites a mail sent after the card was created |

---

### Issues Found

| # | Issue | Severity | Dimension |
|---|-------|----------|-----------|
| 1 | Card rule 6's comment set is open. Store-build code contradicts ticket text where no seeded record flags it: ZOM-42 "gets assigned after the first 6-7 levels" vs `TierManager.cs` `if (totalGames == 10)`; ZOM-275 "Making Them Stronger and Faster!" vs the shipped `Tutorial Bar Full.asset` "Faster and / Deadlier!". Rule 6 is also silent on Not shipped tickets (ZOM-202, 280, 293). Comment writes differ by reading. | Major | UGT, Clarity |
| 2 | ZOM-282: Live with a per-monster comment, or Replaced by match3d#401 ("Monster enrage now scales speed and damage independently" vs "this also finishes the hp part of ZOM-282"). Card rule 4 doesn't say whether that split is "how it works". Status, replaced-by cell and DM counts change (Live 22/Replaced 1 vs 21/2). | Major | UGT |
| 3 | Scope start "Apr 21" has no timezone. ZOM-23 (`2025-04-21T04:51:38Z`) and ZOM-30 (`05:34:29Z`) are Apr 20 in Pacific time: 35 vs 33 rows, Live 22 vs 20. | Major | UGT |
| 4 | Hidden destination and recipients the persona knows: "put it where it's supposed to go and share it with the people who should have it". Julia owns a sheet in ZM Difficulty and is on the invite. | Major | Contrived |
| 5 | Card createCard 2025-09-29T18:05:12Z, with no updateCard action, cites Blake's mail sent 2025-09-30T09:12:44Z and the agenda and invite created after it. | Minor | Cross-Service Coherence |

### Recommended Improvements

1. **Name the destination and the audience in the prompt.** Julia knows both: the ZM Difficulty folder and the people on Monday's tuning invite. Keep the voice casual. Prompts are screened for AI-written text, so word it yourself.
2. **Close card rule 6.** As written it reaches every claim in every ticket, and the code contradicts more ticket text than your seeded records flag. Two examples: ZOM-42's "6-7 levels" (`TierManager.cs` checks `totalGames == 10`) and ZOM-275's message (the shipped text is "Faster and Deadlier!"). Either say exactly which kind of discrepancy earns a comment and that every other ticket stays as it is, including ZOM-42 and the Not shipped ones, or name the tickets that get a comment. Then check each ticket in scope against that wording.
3. **Settle ZOM-282 in the card.** Rule 4 should say whether a PR that splits one value into per-monster values (match3d#401) counts as a numbers change or a change in how it works. Alternatively, have a seeded record state ZOM-282's status.
4. **Remove the date edge.** Start the window at a date with no in-scope ticket within a day of it, so that UTC and Pacific readings give the same set. The first ZOM ticket was created 2025-04-18T19:56:53Z, and no title-matching ticket was created before ZOM-23, so a start of Apr 18 gives the same 35 tickets under both readings.
5. **Fix the card's timeline.** Add a Trello `updateCard` action for the description edit, dated between 2025-09-30T09:12:44Z (Blake's mail) and 2025-09-30T15:41:55Z (the comment), with an unused ID. The card's own ID encodes 2025-09-29T18:05:12Z, so re-dating createCard won't work.

The card is part of your injection SQL, so fixes 2–5 change the SQL. After saving the new SQL, send these again in order: `/injection`, `/prompt`, `/hardness`, `/oe`, `/rubric`. A prompt-only change (fix 1) needs `/prompt`, `/hardness`, `/oe`, `/rubric`.


## Deep Recheck

Passes: P1, P2, P3, P4. Each ran as a fresh subagent on Opus 5.5 (claude-opus-5-5) at the session's effort, blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 6 sentences, 28 forks | 7 | 4 |
| P2 | 6 sentences | 1 | 1 |
| P3 | 7 sentences, 14 claims, 158 SQL statements | 1 | 0 (advisory) |
| P4 | 6 sentences | 3 | 1 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P1 | "build the register the way he set it up" | linear ZOM-23 `2025-04-21T04:51:38Z`, ZOM-30 `2025-04-21T05:34:29Z`; card "every ZOM ticket created Apr 21 - Aug 31" | §2 set membership | Unique Ground Truth | CONFIRMED | No record names a timezone. Both tickets are Apr 20 in PT. |
| DR2 | P1 | "build the register the way he set it up" | ZOM-271 "…ATK POWER BUG…" | §2 set membership | Unique Ground Truth | REJECTED | The card comment says "attack power in the title counts too", and rule 1 requires the listed words "as a whole word in the title". "ATK" is not "attack". |
| DR3 | P1 | "if his rules say something needs to happen on the tickets, go ahead and do that too." | card rule 6; ZOM-202, ZOM-280, ZOM-293 | §2 writes | Unique Ground Truth | CONFIRMED | Rule 6 is silent on Not shipped tickets that describe things the builds don't do. Merged into F1. |
| DR4 | P1 | same | ZOM-42 "6-7 levels" vs `TierManager.cs` `if (totalGames == 10)`; ZOM-275 "Making Them Stronger and Faster!" vs `Tutorial Bar Full.asset` "Faster and"/"Deadlier!"; `PlatformsManager.cs` `// PlayerManager.Instance.DamagePenalty();` | §2 open set | Unique Ground Truth | CONFIRMED | Opened and verified. The rule-6 set is not closed. Merged into F1. |
| DR5 | P1 | "build the register the way he set it up" | PR #401 "Monster enrage now scales speed and damage independently"; #401 comment "this also finishes the hp part of ZOM-282"; ZOM-282 "We can start at +50% to both." | §2 which source wins | Unique Ground Truth | CONFIRMED | No quoted record says whether the split is "how it works" or "just its numbers". The main review had leaned Live; under the recheck rule that leaning is not a kill. |
| DR6 | P1 | "build the register the way he set it up" | `WinHistory` ordering; `Monster.cs` damage not stacking | §2 rules tab | Clarity | REJECTED | Card rule 5 names the sources: "The tier rules are written up in Robert's dynamic difficulty deck and in ZOM-42 itself" and "your monster enrage sheet has the numbers". Code-level quirks are not the documented rules. |
| DR7 | P1 | "share it with the people who should have it." | Vincent in C090N54TG79 "can you drop it in here too" | §2 recipients | Clarity | REJECTED | Card rule 7: "Share it with everyone on the tuning session invite". Vincent is not on the invite. |
| DR8 | P2 | "go through his ask and everything it points to…" | createCard 68daca5845e48874fb98e25a `2025-09-29T18:05:12Z`; mail CAAMNAwYx… `2025-09-30T09:12:44Z`; gcal created 18:24:51Z; doc created 18:31:09Z | §3 date slip | Cross-Service Coherence | CONFIRMED | No updateCard action exists. Minor: no order, window or count the answer uses depends on it. |
| DR9 | P3 | (SQL) | `linear_comments.sequence`, gslides `notes`/`table_json`/`ordinal` absent from the schema snapshot | §6.8 | Injection advisory | REJECTED | Same advisory as Eval 0 A1/A2. The snapshot is unverified, so this is not a demonstrated defect. Kept in the Injection Gate section, not scored. |
| DR10 | P4 | "put it where it's supposed to go and share it with the people who should have it." | card rule 7; folder d_96489e1e00a56685625939 (Julia writer; she owns f_0ba93ae0238d9ed4178212 in it); invite evt_91674a9c23d012a9ac34da | 2.7 | Contrived | CONFIRMED | Matches the main review's finding. The persona knows both the folder and the invite. |
| DR11 | P4 | "if his rules say something needs to happen on the tickets, go ahead and do that too." | card rule 6 | 2.7 | Contrived | REJECTED | It names its source ("his rules") and the object ("the tickets"). It neither hints at a hidden fact nor chains conditions. |
| DR12 | P4 | "then reply to leonard in the dm with what he asked for." | prompt | 1.3.1 | Command List | REJECTED | A single natural "then", with no first/then/finally list. |

Effect on verdict: Cross-Service Coherence moves from 5 to 3. UGT gains two forks (F1 widened to the open comment set, F2 added). UGT, Contrived and Clarity stay at 2, so the overall verdict is unchanged at FAIL 2.

Forks:
- F1: FAIL | Reading A: rule 6 applies to every ticket statement the builds contradict, so ZOM-42 and ZOM-275 get comments too (and possibly the Not shipped tickets) | Reading B: comment only where a seeded record flags it (ZOM-199, ZOM-282) plus Replaced ZOM-254 | Missing: a card sentence that closes the comment set (which discrepancies count, and whether ZOM-42 and Not shipped tickets get comments).
- F2: FAIL | Reading A: ZOM-282 Live with a per-monster comment (Live 22, Replaced 1) | Reading B: ZOM-282 Replaced by match3d#401 (Live 21, Replaced 2) | Missing: a dated, persona-visible record saying whether #401's split counts as a numbers change.
- F3: FAIL | Reading A: scope in UTC days, 35 rows | Reading B: Pacific days, ZOM-23 and ZOM-30 out, 33 rows | Missing: a timezone in card rule 1, or a start date with no ticket on the edge.
- F4: settled | Scope end Aug 31 | — | Settled by: no title match between 2025-08-31 and 2025-09-01 PT; the next is ZOM-517 at 2025-09-03T22:22:22Z.
- F5: settled | ZOM-271 out | in | Settled by: card comment "attack power in the title counts too" and rule 1 "as a whole word in the title".
- F6: settled | Duplicates = Linear state Duplicate (ZOM-203, ZOM-276) | near-duplicates | Settled by: Linear `state_id` "Duplicate" and `duplicates` relations to ZOM-173.
- F7: settled | Store-build source = Blake's mail | Brian's Slack "the editor bits too" | Settled by: card rule 3 "Blake's store builds mail".
- F8: settled | ZOM-45 Live | Editor only | Settled by: "the game reads it when it loads the level".
- F9: settled | ZOM-173 and ZOM-312 Editor only | Live | Settled by: "the slider removal and the level model changes in that PR are ZOM-307's"; "the new events are the ones the editor listens to".
- F10: settled | ZOM-202, ZOM-280, ZOM-293 Not shipped | Editor only / Live | Settled by: rule 1 "open, cancelled and never-merged ones are in, as Not shipped".
- F11: settled | ZOM-254 replaced by ZOM-282 | match3d#401 | Settled by: ZOM-282 created 2025-06-19 and its note "the hp boost still applies on respawned monsters"; ZOM-280 Canceled.
- F12: settled | ZOM-315 Editor only | Live | Settled by: `LevelEditor/UI/StatsPanel.cs` "Total Attack Power".
- F13: settled | Starting tier > 90 | >= 90 | Settled by: Blake's reply "cpm > 90, not >= 90"; `cpm > 90.0f`.
- F14: settled | Demotion: 4 losses or ≤50% of last 10 | 4 losses only | Settled by: ZOM-42 "we demote someone when their win rate for up to the last 10 games is 50% or lower"; `WinRateRule.Defaults`.
- F15: settled | The level drops after a demotion | — | Settled by: ZOM-303 and PR #244 "lowering level difficulty after repeated failures".
- F16: settled | Enrage = sheet Live tab, per monster, hp 0 | +50% every monster / deck +25% HP / Next pass | Settled by: card rule 5 "your monster enrage sheet has the numbers"; Blake's Slack "the blunder part of robert's tiers deck is old".
- F17: settled | Share: Robert writer, Leonard, Arthur and Brian commenters; no channel post | also Vincent or #zombie-design | Settled by: card rule 7 and the invite attendees.
- F18: settled | Card = ZM ROADMAP #80 | Product Roadmap #211 | Settled by: DM "on the difficulty baseline card on the zm roadmap board".
- F19: settled | Rules tab from the deck, ZOM-42 and Blake's correction | code-literal quirks | Settled by: card rule 5 naming the deck and ZOM-42.
- F20: open (in F1) | ZOM-262 and ZOM-274 Live, no comment | Live with comment (blunder damage is commented out; damage doesn't stack) | Missing: same as F1.

Platform defects: none.

### FINAL VERDICT: FAIL

Score: 2

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session default effort

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Next action: Close card rule 6 and settle ZOM-282 in rule 4; remove the Apr 21 UTC/PT edge; add an updateCard action dated after Blake's mail; name the folder and the invite list in the prompt. Then send /injection, /prompt, /hardness, /oe, /rubric again.

Evidence limits: Evals/Docs PDFs were not re-extracted (Eval 1's restated bands and overrides were applied). Runtime acceptance of the `commenter` share role is unverified (declared free-string parameter). Eval 0 checks A–B were reused from the same-hash 0_injection.md because the gate manifest is never written in this portal.

Eval version: task-quality-v1

Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e

Reviewed prompt SHA-256: 11634c6ef52010224bf32d1c5f09763e1e31766b2262d6be3c623612a5afd61f

Review context SHA-256: f6a2e97f06b9042455cea4a7517ed199149e56e4bd34a8f2648faa4adb5728f9

Prompt record SHA-256: e43c0279a4ae1ea408b9f11a0d1627ee44d18ec1844b55226d42bba001d71f27

**Lowest Dimension:** Unique Ground Truth, Contrived and Clarity, each 2. The rule-6 comment set is open, ZOM-282's status forks, the Apr 21 timezone edge moves two tickets, and the prompt hides a destination and audience the persona knows.

**Summary:** The scenario is strong and well seeded. It is cross-service, has real decoys and dynamic corrections, every read is visible to Julia, and the core status and rules facts are settled by records and code. It fails on three record-driven UGT forks that change Linear writes, register rows and DM counts, and on the hidden-destination wording. Close rule 6, settle ZOM-282, move the scope start off the edge and name the folder and invite in the prompt.
