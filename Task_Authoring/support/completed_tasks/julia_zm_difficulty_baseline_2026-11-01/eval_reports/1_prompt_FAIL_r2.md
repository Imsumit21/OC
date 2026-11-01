## PROMPT EVALUATION REPORT

### Task: Julia delegates Leonard's ZM difficulty baseline: build the register (Tickets + Rules in force) from the Trello card rules, file it in ZM Difficulty, share it with the Monday invite, comment on tickets per card rule 6, reply to Leonard in the DM with counts
### Assigned Persona: Julia Lawson - Product Manager (roster `julia_lawson`, julia.lawson@harmonygames.co)
### Assigned Business Function: Product
### Assigned Competency: Engineering Ops
### Assigned Task Skill: Retrieval
### Assigned Horizon: long-horizon (Task Type field; Difficulty Mode "medium" recorded as context)

Review: `/prompt`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode. Actual review date 2026-10-30. Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe `Universe_SynthCut` (hg4-synth-sep30cut v16), manifest `Evals/references/universes/synthcut/universe_manifest.json`.

Inputs:
- `04_Prompt.txt`: revision 8, 525 bytes, sha256 `22f26066…1787`. Attached to this /prompt message as `04_Prompt (2).txt`. It differed from saved revision 5, so it was saved as the new version first.
- `00_Task_Assigned_Inputs.md`: all five fields stated, which clears intake.
- `01_Universe_Inject.sql`: revision 7, 85,712 bytes, sha256 `3242b0a3…e080`.
- No error/async config, dynamic context or reference files were supplied, and the prompt references none.
- Evidence contract `stage-evidence-v1`. Base-universe facts that are unchanged since the prior `/prompt` report (prompt revision 5, SQL revision 4) are REUSED and marked as such. Everything that depends on the changed card, the changed ZOM-315 comment, the new updateCard row or the new prompt wording was checked fresh (NEW).

**What changed since the last round.** Prompt: "put it where it's supposed to go and share it with the people who should have it" became "put it in the zm difficulty folder and share it with everyone on monday's tuning invite".

SQL card (line 56, mirrored in the new updateCard at line 64):
- Rule 1 scope changed from "Apr 21 - Aug 31" to "up to Aug 31 (so everything since we started ZM)".
- Rule 4 gained "A later PR that only finishes what a ticket asked for, or splits its value into separate or per-monster numbers, is a numbers change: the ticket stays Live."
- Rule 6 was rewritten to "only two kinds" of comment, with "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included".
- A Trello `updateCard` was added at 2025-09-30T14:04:31Z.
- The ZOM-315 closing comment now says the change is editor-only.

---

### Injection Gate
- State: NEVER_REVIEWED. The gate reads `reports/input_manifest.json`, and this portal's writer never creates that file.
- Eval 0 handling: `0_injection.md` (injection-static-v2, today) covers the identical SQL hash `3242b0a3…e080` (revision 7) with **FINAL VERDICT: PASS**, COMPLETE. I re-ran `hg_injection_lint.py` on the saved SQL (injection-lint-v1: 161 statements, 0 FAIL / 0 CHECK / 0 INFO). Static checks A–B are REUSED from that report. The Check C items this prompt depends on were re-done here (Phase 3.2).
- Reviewed SQL sha256: `3242b0a30c3389bfd09ec17858293ce931073d665a96d7078b017187b17e8e6a`. Eval 0 verdict: PASS.
- Eval 0 findings on records this prompt depends on: none. Advisories A1 (`linear_comments.sequence`) and A2 (gslides `notes`/`table_json`/`ordinal`) concern columns missing from the unverified schema snapshot. They are load risks only: if the live table rejects a column, the whole transaction rolls back. They stay advisories and do not change a score.

---

### Phase 0: Sources read

Docs and references: Eval 1 in full; the `hg_reference.py guide prompt` view; `prompt_rubric_reliability.md`; `deep_recheck.md`; `common_errors.md`; `acl.md`; `roster.json`; the tool catalog; `known_base_issues.md`. The PDFs in `Evals/Docs` were not re-extracted. Eval 1's inline bands and Local Overrides were applied (evidence limit).

Universe exploration (synth-cut base plus the SQL overlay):
- **Linear** (NEW). `linear/data.json` holds 553 ZOM issues. The first was created 2025-04-18T19:56:53Z (ZOM-10).
  - A whole-word title scan for the card words, plus "attack power" (from the card comment), over every ZOM issue finds 33 tickets. The earliest is ZOM-23 (2025-04-21T04:51:38Z) and the latest before the end date is ZOM-315 (2025-06-26T22:36:29Z). The next title match is ZOM-517 at 2025-09-03T22:22:22Z.
  - ZOM-203 and ZOM-276 are Duplicate, which leaves 31.
  - The four SQL closing notes that start "tiers:" are on ZOM-221, 300, 305 and 378, all by usr_cc3e90160f490686 (arthur.blake@). That makes **35** tickets, with no ticket within two days of either edge.
- **Gmail** (NEW). Arthur Blake's "store builds for monday" (2025-09-30T09:12:44Z, signed "Blake") and "Re: store builds for monday" (13:26:05Z) are in Julia's mailbox. The reply says "ZOM-199 says >= but the code never changed from the original spec" and is the only ticket-text correction in either mail.
- **Trello** (NEW). Card #80 "Difficulty baseline (Julia)" on ZM ROADMAP. createCard is 2025-09-29T18:05:12Z, Leonard's updateCard (new rules text) 2025-09-30T14:04:31Z, and Leonard's comment ("attack power in the title counts too") 15:41:55Z. The decoy card "Difficulty baseline" (#211) sits on another board.
- **Drive** (NEW): folder `ZM Difficulty` (owner Leonard, Julia writer). A scan of base `drive_files` finds no other folder with "difficulty" in its name; the only near names are two "Funnel Completion Rate and Dynamic Difficulty…" files.
- **Calendar** (NEW): Julia's own copy of "ZM difficulty tuning" (2025-10-06 17:00Z, Monday) with attendees Leonard (organizer), Julia, Robert, Arthur Blake and Brian Foster. Base gcal has no event on 2025-10-06 and none with "tuning" in its summary.
- **Docs, Sheets and Slides** (NEW read of the SQL rows):
  - The agenda doc (in the folder; Julia is a reader) asks for "One sheet with two tabs, Tickets and Rules in force".
  - Julia's own "ZM monster enrage" sheet has Live / Next pass / History tabs.
  - Robert's deck "ZM dynamic difficulty - how tiers work" is shared with Julia.
- **Slack** (REUSED, prior report §Phase 0; SQL rows byte-identical): the DM D05HB64NMQU includes Julia and Leonard. #zombie-design C090N54TG79 includes Julia, Leonard, Arthur, Brian and Vincent. Brian's "+50% … every monster" decoy, Vincent's "drop it in here too" request and Arthur's "the blunder part of robert's tiers deck is old".
- **GitHub** (REUSED, prior report §Phase 0; base unchanged; the SQL PR comment is byte-identical):
  - `TierManager.cs` has `cpm > 90.0f`.
  - `WinRateRule.cs` has 80%/10 promotion, the tier -2 one-win promotion, and demotion on ≤50%/10 or 4 losses.
  - `StatsPanel.cs` has "Total Attack Power" (editor-only).
  - The VarC prefabs match the sheet's Live tab.
  - match3d#401 carries the comment "this also finishes the hp part of ZOM-282".

Status derivation under the updated card (NEW for ZOM-282 and ZOM-315; other rows REUSED from the prior derivation, whose records are unchanged):
- **Not shipped 3:** ZOM-202, 280, 293.
- **Editor only 9:** ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315.
- **Replaced 1:** ZOM-254 → ZOM-282.
- **Live 22:** ZOM-23, 30, 42, 45, 49, 50, 161, 199, 221, 246, 258, 262, 263, 274, 275, 282, 288, 295, 300, 303, 305, 378.

Comments under rule 6: ZOM-199 (the build checks cpm > 90) and ZOM-254 (replaced by ZOM-282). This derivation only shows the task can be solved. It is not a golden answer.

---

### Requirement ledger

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Find Leonard's Tuesday DM ask | SQL line 44 (D05HB64NMQU, 2025-09-30T19:48:26Z) | Slack DM history / search | Slack read/search tools | Julia is a DM member | The ask: register, then a reply with the total and per-status counts |
| "everything it points to": card rules | Trello card #80 desc (line 56), updateCard (64), commentCard (66) | DM names "the difficulty baseline card on the zm roadmap board" | `trello_get_cards_on_board`, `trello_get_card`, `trello_get_comments` | Trello unscoped | Rules 1–7 plus the attack-power addendum |
| Ticket scope (rule 1) | Linear ZOM issues; SQL "tiers:" comments | Linear search/list; per-ticket comments | Linear search/get, `linear_list_comments` | Linear unscoped | 35 tickets, the same under UTC and Pacific readings |
| Status per ticket (rules 3–4) | Blake's mail and reply; Linear states and comments; GitHub PRs, comments, code | Gmail search; Linear; GitHub file/PR reads | Gmail read; GitHub reads | Julia's mailbox; GitHub unscoped | Live / Editor only / Replaced / Not shipped; ZOM-282 Live per rule 4 |
| Rules in force tab (rule 5) | Deck, ZOM-42, Blake's reply, Arthur's Slack, enrage sheet Live tab, code | GSlides, Linear, Gmail, Slack, GSheets, GitHub | `gslides_get_presentation_text`, `gsheets_values_batch_get` | Deck shared with Julia; sheet owned by Julia; #zombie-design member | Start tier > 90 → tier 1; promotion 80%/10 and tier -2 one win; demotion on 4 losses or ≤50%/10, with the level dropping one tier (ZOM-303); enrage per monster from the Live tab, hp 0 |
| Build the register: one sheet, tabs Tickets + Rules in force | Agenda doc; card rule 2 | GDocs | `gsheets_create_spreadsheet`, `gsheets_batch_update`, `gsheets_values_update` | Write (ACL-free) | New spreadsheet |
| Put it in the ZM Difficulty folder | Prompt; card rule 7 | Drive folder d_96489e1e00a56685625939 | `gdrive_move_file` (or create with a parent) | Julia is a writer on the folder | File in the folder |
| Share with everyone on Monday's invite | Prompt; card rule 7 (Robert edits, everyone else comments) | GCal event on Julia's calendar | `gdrive_share_file` (role param) | Julia's own calendar | robert@ writer; leonard.hayes@, arthur.blake@, brian.foster@ commenters |
| Ticket comments (rule 6) | Card rule 6; Blake's reply | Linear | `linear_create_comment` | Write | Comments on ZOM-199 and ZOM-254 only |
| Reply to Leonard in the DM | DM | Slack | `slack_send_message` | Write | Total (35) and per-status counts |

Output capability: spreadsheet and tab creation, moving the file to the folder, sharing, Linear comments and the Slack reply are all SUPPORTED by declared catalog tools. The `commenter` role is a free-string parameter with no base example, so runtime acceptance is UNVERIFIED. That is an evidence limit, not a failure.

---

### Phase 1: Prompt Structure & Persona

**Persona:** PASS (5)
- Julia Lawson is an exact roster entry (Product Manager, Product).
- A CEO-to-PM delegation of a difficulty baseline fits, and the casual voice fits.
- The card says "Julia owns this one", and Julia owns the enrage sheet in the folder.

**Assigned Competency:** PASS (5)
- Engineering Ops: the work is reconciling tickets against what shipped in the store builds, PR and code checks, and ticket comments, which is ticket and release-ops work.

**Assigned Task Skill:** PASS (5)
- Retrieval is the core of the work. The agent has to collect every in-scope ticket, its state and shipped status, plus the rule values, from six services.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS
- Dynamic change: two sources are superseded.
  - The deck's "90 or more" is superseded by Blake's reply ("cpm > 90, not >= 90").
  - The deck's blunder slide is superseded by Arthur's Slack ("the blunder part of robert's tiers deck is old").
- Decoys contradicted by later records:
  - Brian's "+50% … every monster" is contradicted by the sheet's Live tab.
  - Brian's "the editor bits too" is contradicted by Blake's mail.
- Multi-source: Slack, Trello, Linear, Gmail, GitHub, Slides, Sheets, Drive and Calendar. Other decoys: the Domino "Difficulty baseline" card, the "Next pass" tab and Vincent's channel request.
- Data seeding: PASS. The rules live in the card, the mails and the agenda, and the prompt stays short.

**Naturalness:** PASS. It is first person, lowercase and casual, with natural shortcuts. There is no document formatting, no polished connectives and no enumerated deliverable spec. Clean typing raises no flag.

**Anti-Patterns:**
| Pattern | Status |
|---------|--------|
| Command List | PASS. One natural "then reply" at the end; no step list |
| Bolt-On | PASS. Every sentence serves the baseline: build, file, share, ticket follow-up, reply |
| Pre-Solving | PASS. No counts, tickets, statuses or causes named. The folder and invite are destinations the persona knows, not answers |
| Tool Mention | PASS. "dm", "folder", "invite" and "tickets" are natural service nouns |

**Diversity:** The task goes well beyond "investigate + post one Slack message". It needs a two-tab sheet, a folder placement, role-based sharing, Linear comments and a DM reply over a 35-ticket cohort.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** FAIL (2)

### Unique Ground Truth comparison

Unique Ground Truth: FAIL 2

Basis: The updated card closes the previous round's forks (ZOM-282, the open comment set, the date edge, the hidden destination), but deep recheck P1 found a new one: ZOM-250 is Editor only or Replaced by ZOM-277, because ZOM-277 changed how its average attack power is calculated and the card never ranks Editor only against Replaced. Status, one Linear comment and the DM counts change.

Alternative selection: The alternatives are the four forks that failed the previous round (ZOM-282 status, the open rule-6 comment set, the start-date timezone edge) plus Vincent's channel request, the one live decoy for the share step. Deep recheck P1 added F: an editor-only ticket that a later ticket changed.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Follow the card as updated: scope is every difficulty ticket created up to Aug 31; ZOM-282 stays Live because \#401 only finishes it and splits its value; comments only on ZOM-199 (flagged by Blake's reply) and on Replaced ZOM-254; share with the invite attendees. | 35 tickets; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; comments on ZOM-199 and ZOM-254 only. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. | 35 rows (31 title matches without Duplicates ZOM-203 and ZOM-276, plus tiers: tickets ZOM-221, 300, 305, 378); ZOM-282 Live; ZOM-254 Replaced by ZOM-282; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab; DM gives the total and per-status counts. | CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; CARD\_R4N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "A later PR that only finishes what a ticket asked for, or splits its value into separate or per-monster numbers, is a numbers change: the ticket stays Live."; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments." |
| B | match3d\#401 changed how enrage works (speed and damage split per monster, hp boost removed), so ZOM-282 is Replaced by match3d\#401 and gets a Replaced comment. | ZOM-282 Replaced by match3d\#401. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. Plus a Replaced comment on ZOM-282 naming match3d\#401. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. Plus ZOM-282. | Register shows ZOM-282 Replaced (by match3d\#401); DM counts Live 21, Replaced 2 instead of Live 22, Replaced 1. | GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 181-181): "this also finishes the hp part of ZOM-282"; Z282 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "We can start at +50% to both." |
| C | Comment on every ticket whose text the store builds contradict, including ZOM-42 (6-7 levels vs 10) and ZOM-275 (FTUE text). | Correction comments also on ZOM-42 and ZOM-275. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. Plus comments on ZOM-42 and ZOM-275. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. Plus ZOM-42 and ZOM-275. | Extra correction comments on ZOM-42 and ZOM-275; register unchanged. | Z42A (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "gets assigned after the first 6-7 levels based on CPM"; Z275 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3327): "Making Them Stronger and Faster!" |
| D | Read the scope window in Pacific days with an Apr 21 start, dropping ZOM-23 (2025-04-21T04:51:38Z, Apr 20 PT) and ZOM-30. | 33 tickets; ZOM-23 and ZOM-30 out. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. | Register 33 rows; DM total and Live count two lower. | Z23 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3277): "2025-04-21T04:51:38Z" |
| E | Also post the register in \#zombie-design because Vincent asked Julia to drop it there. | Share with the invite and also post in \#zombie-design. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. Plus a Slack post in \#zombie-design. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. Plus C090N54TG79. | Same register; extra channel post. | VINCENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "julia when you have the difficulty list can you drop it in here too" |
| F | ZOM-277 (created after ZOM-250) changed how ZOM-250's average attack power works (per unique item instead of per set), so under card rule 4 ZOM-250 is Replaced by ZOM-277 and gets a Replaced comment; no card sentence ranks Editor only above Replaced. | ZOM-250 Replaced by ZOM-277. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. Plus a Replaced comment on ZOM-250 naming ZOM-277. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. Plus ZOM-250. | Register shows ZOM-250 Replaced (by ZOM-277); DM counts Editor only 8 and Replaced 2 instead of 9 and 1. | Z250 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3300): "(This is per set of items)"; Z277 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3329): "The average power should really be 334 / 5 uniques"; CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: a ticket or PR created after this one changed how it works (not just its numbers), so it no longer works the way the ticket says." |

Explicit option inventory: The prompt lists no options; the status values sit in the incorporated card.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "build the register the way he set it up"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: EXCLUDED. Card rule 4 says a later PR that only finishes what a ticket asked for, or splits its value into separate or per-monster numbers, is a numbers change and the ticket stays Live. match3d\#401 finishes ZOM-282's hp part and splits its value per monster, so ZOM-282 stays Live.
Resolution evidence: CARD\_R4N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "A later PR that only finishes what a ticket asked for, or splits its value into separate or per-monster numbers, is a numbers change: the ticket stays Live."; GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 181-181): "this also finishes the hp part of ZOM-282"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Live vs Replaced for ZOM-282. |
| writes | DIFFERENT | B adds a ZOM-282 comment. |
| destinations | DIFFERENT | B adds ZOM-282 as a comment target. |
| contents | DIFFERENT | Status cell and DM counts differ. |

Authority chain: P → DMR → CARD\_R4N

Resolution relevance challenge: The quoted rule-4 sentence names exactly the two things \#401 did to ZOM-282 (finishing the hp part per the \#401 comment, splitting the value per monster).
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "A later PR that only finishes what a ticket asked for, or splits its value into separate or per-monster numbers, is a numbers change: the ticket stays Live."; GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 181-181): "this also finishes the hp part of ZOM-282"

Compared alternative: C
Resolution: EXCLUDED. Card rule 6 limits comments to tickets Blake's mail or reply calls wrong (only ZOM-199 in the reply) and Replaced tickets, and says every other ticket stays as it is, ZOM-42 included, even if its wording is a bit off.
Resolution evidence: CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 119-119): "ZOM-199 says &gt;= but the code never changed from the original spec"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | C decides ZOM-42 and ZOM-275 need comments. |
| writes | DIFFERENT | C adds two comments. |
| destinations | DIFFERENT | C adds two tickets. |
| contents | DIFFERENT | Extra comment texts. |

Authority chain: P → DMR → CARD\_R6X

Resolution relevance challenge: The quoted sentences close the comment set by source (Blake's mail or reply) and name ZOM-42 as staying as it is; the reply names only ZOM-199; neither mail mentions ZOM-275.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 119-119): "ZOM-199 says &gt;= but the code never changed from the original spec"

Compared alternative: D
Resolution: EXCLUDED. The scope has no start date (everything since ZM started) so ZOM-23 and ZOM-30 are in under any timezone. The end edge holds no ticket: the last title match before Aug 31 is ZOM-315 (2025-06-26) and the next ZOM title match is ZOM-517 at 2025-09-03T22:22:22Z.
Resolution evidence: CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; Z517 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3591): "2025-09-03T22:22:22Z"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | D drops two tickets. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rows and counts differ by two. |

Authority chain: P → DMR → CARD\_SCOPE

Resolution relevance challenge: The quoted scope removes the Apr 21 start that created the edge; Z517 shows no ticket sits near the Aug 31 end.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; Z517 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3591): "2025-09-03T22:22:22Z"

Compared alternative: E
Resolution: EXCLUDED. The prompt says to share it with everyone on Monday's tuning invite and the card says to share it with everyone on the invite; Vincent is not an attendee and his channel request is not part of Leonard's ask.
Resolution evidence: CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; P (Evals/task\_inputs/04\_Prompt.txt): "share it with everyone on monday's tuning invite"; CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 172-172): "VALUES ('evt\_91674a9c23d012a9ac34da', 'julia.lawson@harmonygames.co', 'ZM difficulty tuning'"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | E adds a channel post. |
| writes | DIFFERENT | E adds a Slack post. |
| destinations | DIFFERENT | E adds \#zombie-design. |
| contents | DIFFERENT | Extra post. |

Authority chain: P → DMR → CARD\_R7

Resolution relevance challenge: The prompt and card both define the audience as the invite list; the invite on Julia's calendar does not include Vincent.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; P (Evals/task\_inputs/04\_Prompt.txt): "share it with everyone on monday's tuning invite"; CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 172-172): "VALUES ('evt\_91674a9c23d012a9ac34da', 'julia.lawson@harmonygames.co', 'ZM difficulty tuning'"

Compared alternative: F
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. ZOM-250 defines Avg Attack Power as per set of items; ZOM-277, created later, changes the formula to per unique item, which fits rule 4's 'changed how it works ... so it no longer works the way the ticket says'. The card gives an explicit precedence only for Not shipped (rule 1); rule 3 and Blake's mail make ZOM-250 editor-only but never say Editor only wins over Replaced, and rule 6 lists the categories without ranking them.
Resolution evidence: Z250 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3300): "(This is per set of items)"; Z277 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3329): "The average power should really be 334 / 5 uniques"; CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: a ticket or PR created after this one changed how it works (not just its numbers), so it no longer works the way the ticket says."; CARD\_R1NS (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "open, cancelled and never-merged ones are in, as Not shipped"; CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 75-75): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Editor only vs Replaced for ZOM-250. |
| writes | DIFFERENT | F adds a Replaced comment on ZOM-250. |
| destinations | DIFFERENT | F adds ZOM-250 as a comment target. |
| contents | DIFFERENT | Status cell, replaced-by cell and DM counts (Editor only 9/8, Replaced 1/2) differ. |

Resolution relevance challenge: Rule 3's 'judged against the store builds' and the mail's 'never reached players' establish that ZOM-250 is editor-only work but do not state a ranking between Editor only and Replaced; rule 1 shows the card ranks statuses only where it says so.
Delegation challenge: NOT_CLAIMED. 'go with your read on the details' does not authorize two different statuses, comment sets and counts as interchangeable.
Challenge evidence: CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 75-75): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; CARD\_R1NS (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "open, cancelled and never-merged ones are in, as Not shipped"

Strongest-alternative challenge (F): ZOM-277's own text says the ZOM-250 average calculation 'doesn't make sense' and sets a new formula, which is rule 4's 'changed how it works'; only an unwritten precedence of Editor only over Replaced excludes it.
Challenge evidence: Z277 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3329): "The average power should really be 334 / 5 uniques"; CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: a ticket or PR created after this one changed how it works (not just its numbers), so it no longer works the way the ticket says."

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

Forks settled by records (the full list is in the Deep Recheck fork list):
- Starting tier: Blake's reply says "the starting tier check in the build is cpm > 90, not >= 90", and `TierManager.cs` has `cpm > 90.0f`.
- Demotion: `WinRateRule.cs` ships both rules (≤50% of last 10 and 4 losses), matching ZOM-42.
- ZOM-315 is Editor only. Its closing note says "nothing changes in the game itself", and "Total Attack Power" appears only in `LevelEditor/UI/StatsPanel.cs`.
- ZOM-254 was first replaced by ZOM-282. ZOM-254 says "Monster Max HP, +25%", and ZOM-282 says "speed and monster attack damage but NOT HP". ZOM-280 is Canceled, and ZOM-274 is a bug fix.
- The enrage numbers come from the sheet's Live tab (card rule 5: "your monster enrage sheet has the numbers").

**Feasibility:** PASS (5)
- Every ask maps to cataloged tools, and all the needed data exists.
- The numeric values (per-monster enrage, the CPM threshold, 80%/50%/4 losses) are tool-visible in the sheet, the mail, the ticket and the code.
- No per-X breakdown lacks a field: status comes from Linear state, comments and code, and the per-monster values are sheet rows.

**Persona ACL Reachability:** PASS (5). All scoped reads are open to Julia:
- the DM (member);
- #zombie-design (member);
- Arthur's mails (her mailbox);
- the invite (her calendar);
- the folder (writer), the agenda doc (reader), the deck (shared) and the sheet (owner).

The #zombie-prs bot copy of the #401 comment is in a channel Julia isn't in, but the same comment is in GitHub, which is unscoped (REUSED).

**Explicit Tool Mention:** PASS (5).

**Clarity & Specificity:** FAIL (2). Action Decision Ambiguity, found by deep recheck P1 (fork F1).
- Under one reading ZOM-250 gets a Replaced comment naming ZOM-277. Under the other it stays as it is.
- Nothing in the card picks one.
- Every other write is the same under all readings tested: card rule 6 closes the rest of the comment set, and the folder and invite are named.
- No "I'll [verb]" statements appear, so there is no delegation ambiguity.

**Contrived / Unnatural:** PASS (5)
- The destination and audience are now named the way the persona would know them ("the zm difficulty folder", "everyone on monday's tuning invite").
- There are no staged typos, opaque IDs, exact timestamps, trap hints, riddles, audit-form wording or if-chains.
- "if his rules say something needs to happen on the tickets" points to a named source; it doesn't hint at a hidden fact.

**Alignment with Today's Date:** PASS (5)
- "tuesday" resolves to 2025-09-30 (DM at 19:48:26Z, 12:48 PT).
- "monday's tuning session" and "monday's tuning invite" resolve to the 2025-10-06 17:00Z event.
- Nothing the prompt treats as already done falls after the clock.

**Originality:** N/A (no comparison samples supplied).

**Truthfulness:** PASS (5). All five premises were verified (PR1–PR5 in the check record):
- Leonard (EMPLOYEE_0038) DMed Julia on Tue Sep 30.
- The Monday session and its invite exist.
- The ZM Difficulty folder exists and is unique.
- Leonard's rules exist on the card the DM names.
- No departed person acts, and nothing post-dates the clock.

**Tool Use & Cross-service:** PASS (5). Each service changes a graded fact:
- Linear sets the cohort and the comment targets.
- Gmail sets what counts as shipped, the cpm > 90 rule and the ZOM-199 comment.
- GitHub sets Editor only vs Live and the demotion rules.
- Sheets sets the enrage numbers.
- Calendar sets the share list.
- Trello carries the rules.

Writes span Sheets, Drive, Linear and Slack.

**Investigation + Action:** PASS (5). The investigation feeds every write: the register rows, the comments and the counts.

**Coherence (Bolt-on):** PASS (5).

**Business Function:** PASS (5). Product: a PM preparing a design-tuning baseline.

---

### Phase 3: Universe Feasibility

**Data Existence:** PASS (5). Every needed entity was verified, and each can be retrieved through cataloged reads: Linear issues and comments, the Trello card, actions and comments, Gmail threads, Slack history, Drive/Sheets/Slides/Docs, GCal, and GitHub PRs, comments and file contents.

**Cross-Service Coherence:** NON-FAIL (3)
- Inconsistency in task-touched data: one minor Cross-service Referential Inconsistency, found by deep recheck P2 and confirmed.
  - match3d commit `b511fcbcd5` (2025-06-19, arthur blake, "Disable monster enrage health.") turns `EnrageHealth(totalEnragePercentage);` into a comment. That was the only call, so it applies to every monster.
  - The injected ZOM-282 comment (SQL line 286, 2025-06-21) still says "the hp boost still applies on respawned monsters, will clean that up later".
  - The injected match3d#401 comment (SQL line 181, and the Slack bot copy at line 52) says "this also finishes the hp part of ZOM-282, respawned monsters don''t get the boost anymore".
  - The enrage sheet's History tab likewise credits match3d#401 with "hp boost removed". In fact #401 only deleted the dead `EnrageHealth` method.
  - ZOM-282 stays Live under card rule 4 either way, so no graded value, count, recipient or destination changes. That makes it a single minor inconsistency (NON-FAIL), not a lifecycle or sum mismatch.
- Fixed since the last round: the card's description now follows Leonard's `updateCard` (2025-09-30T14:04:31Z). That is after Blake's reply (13:26:05Z) and before the comment (15:41:55Z), and its ID prefix decodes to the same second.
- Checked and consistent (NEW for changed rows, REUSED otherwise):
  - The ZOM-315 comment (2025-07-02T11:07:32Z) comes before its completion (11:16:32Z) and matches `StatsPanel.cs`.
  - Every added Slack author is a member of its channel.
  - Arthur's "Leonard released it yesterday" matches Leonard's #executives message on 2025-09-29.
  - The sheet's Live tab equals the VarC prefab values.
  - Every SQL date is before the clock.
  - The decoy card's action label "Product Roadmap" matches 2,084 base actions on that board.
- Known base-data issues (not scored): none. The task touches no Snowflake or Confluence data.
- Not task-touched (not scored):
  - The injected comment on ZOM-359 ("parking this, nothing merged yet") sits on a ticket in the Regression state. ZOM-359 is outside the register scope.
  - Code note: since #401, `Monster.cs` adds up the damage percentage per enrage but passes the single `enrageDamagePercentage`, so damage doesn't stack across blunders. Keep rubric rows on the sheet's per-blunder numbers and off stacking behaviour.
- Injection SQL considered: Yes.
- Static integrity evidence: REUSED from `0_injection.md` (same SQL hash; injection-static-v2 PASS, checks A–B). The task-relevant Check C was re-done here.
- Prompt-specific sources, access and configuration: supported (no error/async config).

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|-----------|--------------|-------------|---------------|
| Prompt | Unique Ground Truth | 2 | ZOM-250 Editor only vs Replaced by ZOM-277 (fork F1); the previous round's forks are closed |
| Prompt | Feasibility | 5 | All asks cataloged; data exists |
| Prompt | Persona ACL Reachability | 5 | Every scoped read visible to Julia |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 2 | Write divergence: a ZOM-250 comment or none |
| Prompt | Contrived / Unnatural | 5 | Destination and audience named; no flags |
| Prompt | Alignment with Today's Date | 5 | Tue Sep 30 and Mon Oct 6 resolve |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied |
| Prompt | Truthfulness | 5 | Five premises verified |
| Prompt | Tool Use & Cross-service | 5 | Each service changes a graded fact |
| Prompt | Investigation + Action | 5 | Investigation feeds the writes |
| Prompt | Coherence (Bolt-on) | 5 | None |
| Prompt | Persona | 5 | Fits a PM |
| Prompt | Business Function | 5 | Product |
| Prompt | Assigned Competency | 5 | Engineering Ops |
| Prompt | Assigned Task Skill | 5 | Retrieval |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three dimensions; seeded |
| Universe | Data Exists | 5 | Verified |
| Universe | Cross-Service Coherence | 3 | ZOM-282 and #401 comments claim a respawn hp boost that the code turned off on Jun 19 |

---

### Issues Found

| # | Issue | Severity | Dimension |
|---|-------|----------|-----------|
| 1 | ZOM-250 ("Avg Attack Power" … "(This is per set of items)") was changed by ZOM-277, created later ("The average power should really be 334 / 5 uniques"). That fits card rule 4's "changed how it works". The card ranks statuses only for Not shipped (rule 1), so ZOM-250 can be Editor only or Replaced by ZOM-277. The status, one Linear comment and the DM counts (Editor only 9/8, Replaced 1/2) change. | Major | UGT, Clarity |
| 2 | The injected ZOM-282 comment (line 286) and the #401 comment (lines 181 and 52) say the hp boost survived on respawned monsters until #401. The sheet's History tab also credits #401 with "hp boost removed". match3d commit b511fcbcd5 turned `EnrageHealth` off for every monster on 2025-06-19. | Minor | Cross-Service Coherence |

### Recommended Improvements

1. **Rank Editor only above Replaced in the card (fixes issue 1).** Add a sentence to rule 3 or rule 4 saying that a ticket whose changes are only level editor or debug tooling is Editor only, even if a later ticket or PR changed it. This covers all nine Editor only tickets (ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315). Rule 6 then keeps ZOM-250 without a comment. The other way to fix it is to have rule 4 name ZOM-250 directly. After the change, check each of those nine tickets against the new sentence. Write it in Leonard's voice; prompts and seeded text are screened for AI-written wording.
2. **Make the hp-boost comments match the code (fixes issue 2).** b511fcbcd5 switched the enrage hp boost off on 2025-06-19, so none of these records should say it lasted until #401:
   - the ZOM-282 closing comment (line 286, 2025-06-21);
   - the #401 PR comment (line 181) and its Slack bot copy (line 52), which must stay identical;
   - the History tab row "speed and damage split, hp boost removed".

   One option: the ZOM-282 comment says enrage now only touches speed and damage, and the #401 comment and History row say the split, without the hp claim. Card rule 4's split clause still keeps ZOM-282 Live without the word "finishes".
3. **Optional:** "then reply to leonard" is one natural ordering word, not a step list, and was not scored. If you want to avoid any search-hit screen on "Then", "and reply to leonard" says the same thing.

Both fixes change the injection SQL. After saving the new SQL, send these again in order: `/injection`, `/prompt`, `/hardness`, `/oe`, `/rubric`. The prompt text itself needs no change.

## Deep Recheck

Passes: P1, P2, P3, P4. Each ran as a fresh subagent on Opus 5.5 (claude-opus-5-5) at the session's effort, blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 7 sentences, 21 forks | 1 | 1 |
| P2 | 7 sentences | 6 | 1 |
| P3 | 7 sentences, 16 claims, 159 SQL statements | 1 | 0 (advisory) |
| P4 | 7 sentences | 2 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P1 | "go through his ask and everything it points to and build the register the way he set it up." | ZOM-250 "(This is per set of items)"; ZOM-277 "The average power should really be 334 / 5 uniques"; card rule 4 "changed how it works (not just its numbers)" | §2 which status | Unique Ground Truth | CONFIRMED | No quoted record ranks Editor only against Replaced. Rule 1 ranks only Not shipped. Rule 3 ("judged against the store builds") and Blake's mail ("never reached players") make ZOM-250 editor-only but don't rule out Replaced. |
| DR2 | P2 | same | match3d#401 `EnrageDamage(enrageDamagePercentage);`; ZOM-274 "Monsters can only be enraged once bug" | §3 lifecycle | Cross-Service Coherence | REJECTED | Card rule 4: "A later PR that only finishes what a ticket asked for, or splits its value into separate or per-monster numbers, is a numbers change: the ticket stays Live." #401 is that split. After it, `_enrageCount` still rises and speed still stacks, so monsters can still be enraged more than once, as ZOM-274 requires. Damage stacking is kept as a not-scored code note. |
| DR3 | P2 | same | ZOM-282 comment "the hp boost still applies on respawned monsters"; #401 comment "finishes the hp part of ZOM-282"; commit b511fcbcd5 `//EnrageHealth(totalEnragePercentage);` | §3 references | Cross-Service Coherence | CONFIRMED | Opened the commit (2025-06-19, arthur blake, "Disable monster enrage health."). The file before #401 has no other EnrageHealth call. Minor, because ZOM-282 stays Live either way. |
| DR4 | P2 | "build the register the way he set it up." | deck "Demotion: 4 losses in a row moves you down one tier." vs ZOM-42 and `WinRateRule.cs` | §3 omission | Cross-Service Coherence | REJECTED | The deck summarizes and doesn't say "only". Card rule 5 names both the deck and ZOM-42, and the code ships both rules. Settled (F8). |
| DR5 | P2 | same | match3d#265 changes `GameEvents/LevelDesignGameEvents.cs` | §2 status | Unique Ground Truth | REJECTED | Persona-visible comment on ZOM-312: "delete and reassign live in the level settings panel, the new events are the ones the editor listens to". |
| DR6 | P2 | "go through his ask and everything it points to" | decoy action board name "Product Roadmap" vs base "DD Product Roadmap" | §3 label | Cross-Service Coherence | REJECTED | 2,084 base actions on board 65eb4ec5… use "Product Roadmap". The injected label follows base. |
| DR7 | P2 | same | ZOM-359 Regression with "parking this, nothing merged yet" | §3 lifecycle | Cross-Service Coherence | REJECTED | ZOM-359 is outside the register scope (no keyword in the title, no "tiers:" note), so it isn't task-touched data. Listed as not scored. |
| DR8 | P3 | (SQL) | `linear_comments.sequence`; gslides `notes`/`table_json`/`ordinal` absent from the schema snapshot | §6.8 | Injection advisory | REJECTED | Same as Eval 0 advisories A1 and A2. The snapshot is unverified, so this is not a demonstrated defect. It stays in the Injection Gate section. |
| DR9 | P4 | "then reply to leonard in the dm with what he asked for." | prompt | 1.3.1 | Command List | REJECTED | A single "then" that follows Leonard's own order ("reply here when it''s in the folder"). common_errors §6.6 fails a "first / then / finally" list; this isn't one. Optional wording note in fix 3. |
| DR10 | P4 | "if his rules say something needs to happen on the tickets, go ahead and do that too." | card rule 6 | 2.7 | Contrived | REJECTED | One short conditional that names its source ("his rules") and its object ("the tickets"). It's not a long if-chain, and it hints at no hidden fact: the comment rule is required work, not a trap. |

Effect on verdict: Unique Ground Truth drops from 5 to 2 and Clarity from 5 to 2 (fork F1). Cross-Service Coherence drops from 5 to 3. The verdict moves from PASS 5 to FAIL 2.

Forks:
- F1: FAIL | Reading A: ZOM-250 Editor only, no comment (Editor only 9, Replaced 1) | Reading B: ZOM-250 Replaced by ZOM-277, with a Replaced comment (Editor only 8, Replaced 2) | Missing: a card sentence ranking Editor only above Replaced, or a dated, persona-visible record giving ZOM-250's status.
- F2: settled | ZOM-282 Live | Replaced by match3d#401 | Settled by: card rule 4 "splits its value into separate or per-monster numbers, is a numbers change: the ticket stays Live".
- F3: settled | Comments only on ZOM-199 and ZOM-254 | also ZOM-42, ZOM-275 or Not shipped tickets | Settled by: card rule 6 "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included"; Blake's reply flags only "ZOM-199 says >=".
- F4: settled | Scope 35 tickets under UTC and Pacific | 33 | Settled by: card rule 1 "created up to Aug 31 (so everything since we started ZM)". The first ZOM ticket is 2025-04-18; ZOM-23 is the earliest title match; the next match after ZOM-315 is ZOM-517 (2025-09-03T22:22:22Z).
- F5: settled | Attack-power tickets in | out | Settled by: Leonard's card comment "attack power in the title counts too".
- F6: settled | Duplicates ZOM-203 and ZOM-276 out | in | Settled by: Linear state Duplicate; rule 1 "Duplicates are out".
- F7: settled | "tiers:" tickets ZOM-221, 300, 305, 378 in | out | Settled by: rule 1 "his closing note on those starts with 'tiers:'".
- F8: settled | Demotion: 4 losses or ≤50% of last 10, and the level drops a tier | 4 losses only | Settled by: ZOM-42 "50% or lower", `WinRateRule.cs`, ZOM-303 and match3d#244.
- F9: settled | Starting tier > 90 | >= 90 | Settled by: Blake's reply "cpm > 90, not >= 90"; `cpm > 90.0f`.
- F10: settled | Enrage from the sheet's Live tab, per monster, hp 0 | Brian's +50%, deck +25% or the Next pass tab | Settled by: rule 5 "your monster enrage sheet has the numbers"; Arthur's Slack "the blunder part of robert''s tiers deck is old".
- F11: settled | ZOM-254 Replaced by ZOM-282 | match3d#401 or ZOM-280 | Settled by: ZOM-254 "Monster Max HP, +25%" vs ZOM-282 "NOT HP"; ZOM-280 Canceled; rule 4 "Name the first one that did."
- F12: settled | ZOM-45 Live; ZOM-173, 312 and 315 Editor only; ZOM-202, 280 and 293 Not shipped | the other status | Settled by: their closing notes ("the game reads it when it loads the level"; "the new events are the ones the editor listens to"; "nothing changes in the game itself") and rule 1 "open, cancelled and never-merged ones are in, as Not shipped".
- F13: settled | Editor and debug tickets Editor only | Live per Brian's "the editor bits too" | Settled by: rule 3 "Blake''s store builds mail" and the mail's stripped list.
- F14: settled | Share: robert@ editor; leonard.hayes@, arthur.blake@, brian.foster@ commenters; no channel post | also Vincent or #zombie-design | Settled by: the prompt "everyone on monday's tuning invite", card rule 7, and the invite's attendees.
- F15: settled | Card = ZM ROADMAP #80 | Product Roadmap #211 | Settled by: DM "on the difficulty baseline card on the zm roadmap board".
- F16: settled | Folder = ZM Difficulty d_96489e1e00a56685625939 | another folder | Settled by: the prompt "the zm difficulty folder"; no other folder with that name exists in base Drive.

Platform defects: none.

### FINAL VERDICT: FAIL

Score: 2

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session default effort

Clock: Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Next action: Add a card sentence that ranks Editor only above Replaced (ZOM-250 vs ZOM-277), and make the ZOM-282, #401 and History-tab hp claims match commit b511fcbcd5. Then send /injection, /prompt, /hardness, /oe and /rubric again.

Evidence limits: The Evals/Docs PDFs were not re-extracted; Eval 1's restated bands and overrides were applied. Runtime acceptance of the `commenter` share role is unverified (declared free-string parameter). Eval 0 checks A–B were reused from the same-hash 0_injection.md, because this portal never writes the gate manifest. Slack and GitHub facts on byte-identical SQL rows were reused from the prior /prompt report.

Eval version: task-quality-v1

Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e

Reviewed prompt SHA-256: 22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787

Review context SHA-256: 73b9f5721b06d3aaf497626ef1ab28496c368a9389ade7e511bae65a3b830a81

Prompt record SHA-256: 8bfdd2c09bb09bdba58a69006118c84bbeca059c55c95cf087ab03f7b251dd42

**Lowest Dimension:** Unique Ground Truth and Clarity, each 2. ZOM-250 can be Editor only or Replaced by ZOM-277, and the card doesn't rank the two.

**Summary:** This round fixed every earlier defect: the hidden destination, the open rule-6 comment set, the ZOM-282 status, the Apr 21 timezone edge and the card timeline. The scenario is strong, cross-service and fully visible to Julia. It fails on one new record-driven fork (ZOM-250 Editor only vs Replaced by ZOM-277), which changes a status, a Linear comment and the DM counts. A minor coherence slip remains in the respawn-hp comments.
