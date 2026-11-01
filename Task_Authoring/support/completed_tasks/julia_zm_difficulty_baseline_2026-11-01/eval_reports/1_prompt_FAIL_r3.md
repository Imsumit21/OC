## PROMPT EVALUATION REPORT

### Task: Julia delegates Leonard's ZM difficulty baseline: build the register (Tickets + Rules in force) from the Trello card rules, file it in ZM Difficulty, share it with the Monday invite, comment on tickets per card rule 6, reply to Leonard in the DM with counts
### Assigned Persona: Julia Lawson - Product Manager (roster `julia_lawson`, julia.lawson@harmonygames.co)
### Assigned Business Function: Product
### Assigned Competency: Engineering Ops
### Assigned Task Skill: Retrieval
### Assigned Horizon: long-horizon (Task Type field; Difficulty Mode "medium" recorded as context)

Review: `/prompt`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode. Actual review date 2026-10-30. Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe `Universe_SynthCut` (hg4-synth-sep30cut v16), manifest `Evals/references/universes/synthcut/universe_manifest.json` (sha256 `da2f4cf0…a1a`).

Inputs:
- `04_Prompt.txt`: revision 10, 525 bytes, sha256 `22f26066…1787`. Attached as `04_Prompt (3).txt`; byte-identical to revision 8 (the last /prompt round).
- `00_Task_Assigned_Inputs.md`: all five fields stated, which clears intake.
- `01_Universe_Inject.sql`: revision 9, 86,060 bytes, sha256 `99b35b05…b168`. Changed since the last /prompt round (revision 7, `3242b0a3…e080`) on seven lines, no IDs changed: 22 (sheet Live tab), 26 (sheet History tab), 52 (Slack GitHub-bot copy), 56 and 64 (card rule 4), 111/181 (PR #401 comment), 216/286 (ZOM-282 closing comment). Line numbers below use the line-splitting convention of `hg_prompt_checks.py` (embedded CRs in Gmail rows count as breaks), so lines after 69 run higher than `grep -n`.
- No error/async config, dynamic context or reference files were supplied, and the prompt references none.
- Evidence contract `stage-evidence-v1`. reused_evidence: base facts from the prior `1_prompt.md` (sha256 `62245593…414c4e`, Phase 0 and Phase 3 ledgers) whose records and SQL rows are byte-identical (Gmail lines 69–159, Calendar, Drive, Docs, Slides, Slack rows other than 52, Linear rows other than 286, GitHub code files). Everything depending on the seven changed lines was checked NEW.

**What changed since the last round (SQL only).**
- Card rule 4 now reads: "Replaced: only when a later ticket's closing note says it replaces this one. Name that ticket. Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don't, and a ticket players never had stays Editor only or Not shipped."
- The ZOM-282 closing note now says "this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."
- The #401 comment (and bot copy) now says "this gives enrage speed and damage their own values, they shared one since ZOM-282. also drops the old EnrageHealth method, nothing has called it since june".
- The sheet's Live tab now lists 13 rows (adds Mailman, Mayor1/Mayor2 split, PartyGirl); History adds "2025-06-19 enrage hp boost switched off, Blake".

---

### Injection Gate
- State: NEVER_REVIEWED. The gate reads `reports/input_manifest.json`, which this portal's writer never creates.
- Eval 0 handling: `0_injection.md` (injection-static-v2, today, sha256 `152735a6…52b8d2`) covers the identical SQL hash `99b35b05…b168` (revision 9) with **FINAL VERDICT: PASS**, COMPLETE. Its WORKFLOW, scoring, schema, base-manifest and known-issues hashes match the current files. I re-ran `hg_injection_lint.py` (injection-lint-v1: 161 statements, 0 FAIL / 0 CHECK / 0 INFO). Static checks A–B are REUSED; the Check C items this prompt depends on were re-done here (Phase 3.2).
- Reviewed SQL sha256: `99b35b05c5224ea5c7342964e5807613f0a6891550d8d42b6920e9e0a8cfb168`. Eval 0 verdict: PASS.
- Eval 0 advisories: A1 (`linear_comments.sequence`) and A2 (gslides `notes`/`table_json`/`ordinal`) are columns absent from the unverified schema snapshot (also raised by deep recheck P3 DR1). Load risk only; they stay advisories. A7 (four VarC prefabs truncated at 10,240 bytes) is now resolved by git history and becomes the Cross-Service Coherence finding below.

---

### Phase 0: Sources read

Docs and references: Eval 1 in full; `hg_reference.py guide prompt`; `prompt_rubric_reliability.md` (release task-quality-v1 verified with `hg_eval_release.py snapshot prompt`); `deep_recheck.md`; `common_errors.md`; `acl.md`; `roster.json`; tool catalog; `known_base_issues.md`. The PDFs in `Evals/Docs` were not re-extracted; Eval 1's inline bands and Local Overrides were applied (evidence limit, unchanged from prior rounds).

Universe exploration (synth-cut base plus SQL overlay):
- **Linear** (NEW). 553 ZOM issues. Whole-word title scan for the card words over issues created up to Aug 31: 28 tickets; plus "attack power" titles per Leonard's card comment (ZOM-246, 250, 263, 277, 315) = 33; minus Duplicates ZOM-203 and ZOM-276 = 31; plus the four "tiers:" closing notes (ZOM-221, 300, 305, 378, all by usr_cc3e90160f490686 = arthur.blake@) = **35**. The base export has **no Linear comments at all**; all 109 comments are SQL rows. Of these, only ZOM-282's closing note uses "replace". No ZOM description says one ticket replaces another (descriptions with "replac" are about item replacement or ZOM-42's monster upgrade table).
- **Trello, Gmail, Drive, Calendar, Docs, Slides, Slack** (REUSED, prior report Phase 0; rows byte-identical): card #80 with Leonard's updateCard (2025-09-30T14:04:31Z) and comment (15:41:55Z); Blake's store builds mail and reply (only ZOM-199 flagged); folder `ZM Difficulty` (Julia writer, unique); invite "ZM difficulty tuning" 2025-10-06T17:00Z (Leonard, Julia, Robert, Arthur Blake, Brian Foster); agenda "One sheet with two tabs, Tickets and Rules in force"; Robert's deck; DM D05HB64NMQU; #zombie-design decoys (Brian, Vincent, Arthur's "the blunder part of robert's tiers deck is old").
- **GitHub** (NEW for enrage). `Monster.cs` at HEAD `0ff577550e` has separate `enrageSpeedPercentage`/`enrageDamagePercentage` and no `EnrageHealth`, matching the rewritten ZOM-282 and #401 comments. Base PR #401 CodeRabbit summary: "Enrage health boosts have been removed". match3d git history (read-only `git log`/`show`): `6a4d8ba57e` "Split enrage parameter into separate ones" (2025-08-25, 12 files) and `476a02949b` "Monster speeds and damages final adjustment" (2025-08-27, 11 files) are the only commits that set split per-monster values; neither touches VarC-Mailman, VarC-Mayor2 or the two VarC-PartyGirl prefabs (see Phase 3.2).

Status derivation under the rewritten card (NEW; shows solvability, not a golden answer):
- **Not shipped 3:** ZOM-202 (In Progress), 280 (Canceled), 293 (Todo).
- **Editor only 9:** ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315.
- **Replaced 1:** ZOM-254 → ZOM-282 (the only closing note with replace wording).
- **Live 22:** ZOM-23, 30, 42, 45, 49, 50, 161, 199, 221, 246, 258, 262, 263, 274, 275, 282, 288, 295, 300, 303, 305, 378.
- Comments under rule 6: ZOM-199 (the build checks cpm > 90) and ZOM-254 (replaced by ZOM-282).

---

### Requirement ledger

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Find Leonard's Tuesday DM ask | SQL line 44 (D05HB64NMQU, 2025-09-30T19:48:26Z) | Slack DM history / search | Slack read/search tools | Julia is a DM member | The ask: register, then reply with total and per-status counts |
| "everything it points to": card rules | Trello card #80 (line 56), updateCard (64), commentCard (66) | DM names "the difficulty baseline card on the zm roadmap board" | `trello_get_cards_on_board`, `trello_get_card`, `trello_get_comments` | Trello unscoped | Rules 1–7 plus the attack-power addendum |
| Ticket scope (rule 1) | Linear ZOM issues; SQL "tiers:" comments | Linear search/list; per-ticket comments | Linear search/get, `linear_list_comments` | Linear unscoped | 35 tickets; same under every edge |
| Status per ticket (rules 3–4) | Blake's mail and reply; Linear states and closing notes; GitHub | Gmail search; Linear; GitHub | Gmail read; Linear; GitHub reads | Julia's mailbox; unscoped | Live 22 / Editor only 9 / Replaced 1 / Not shipped 3 |
| Rules in force tab (rule 5) | Deck, ZOM-42, Blake's reply, enrage sheet Live tab, code | GSlides, Linear, Gmail, GSheets, GitHub | `gslides_get_presentation_text`, `gsheets_values_batch_get` | Deck shared; sheet owned by Julia | Start tier > 90 → tier 1; promotion 80%/10 and tier -2 one win; demotion on 4 losses or ≤50%/10 with the level dropping one tier (ZOM-303); enrage per monster from the Live tab, hp 0 (**three Live rows disagree with the code; see issue 1**) |
| Build the register: one sheet, tabs Tickets + Rules in force | Agenda doc; card rule 2 | GDocs | `gsheets_create_spreadsheet`, `gsheets_batch_update`, `gsheets_values_update` | Write (ACL-free) | New spreadsheet |
| Put it in the ZM Difficulty folder | Prompt; card rule 7 | Drive folder d_96489e1e00a56685625939 | `gdrive_move_file` (or create with parent) | Julia is writer | File in folder |
| Share with everyone on Monday's invite | Prompt; card rule 7 | GCal event on Julia's calendar | `gdrive_share_file` (role param) | Julia's own calendar | robert@ writer; leonard.hayes@, arthur.blake@, brian.foster@ commenters |
| Ticket comments (rule 6) | Card rule 6; Blake's reply; rule 4 | Linear | `linear_create_comment` | Write | ZOM-199 and ZOM-254 only |
| Reply to Leonard in the DM | DM | Slack | `slack_send_message` | Write | Total 35 and per-status counts |

Output capability: spreadsheet/tab creation, moving into the folder, sharing, Linear comments and the Slack reply are SUPPORTED by declared catalog tools. The `commenter` role is a free-string parameter with no base example; runtime acceptance UNVERIFIED (evidence limit, not a failure).

---

### Phase 1: Prompt Structure & Persona (REUSED; prompt text byte-identical, assignment unchanged)

**Persona:** PASS (5). Exact roster entry; CEO-to-PM delegation; card says "Julia owns this one"; Julia owns the enrage sheet.

**Assigned Competency:** PASS (5). Engineering Ops: reconciling tickets with what shipped in store builds, PR/code checks and ticket comments.

**Assigned Task Skill:** PASS (5). Retrieval is the core: every in-scope ticket, state, shipped status and rule value across six services.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS. Superseded sources (deck "90 or more" vs Blake's "cpm > 90"; deck blunder slide vs Arthur's Slack); decoys (Brian's "+50% … every monster", "the editor bits too", Domino card #211, "Next pass" tab, Vincent's channel request). Data seeding PASS.

**Naturalness:** PASS. First person, lowercase, casual; no document formatting, polished connectives or enumerated specs. Clean typing raises no flag.

**Anti-Patterns:**
| Pattern | Status |
|---------|--------|
| Command List | PASS. One natural "then reply" (P4 DR1, rejected as a defect) |
| Bolt-On | PASS. Every sentence serves the baseline |
| Pre-Solving | PASS. No counts, tickets, statuses or causes named |
| Tool Mention | PASS. "dm", "folder", "invite", "tickets" are natural nouns |

**Diversity:** Two-tab sheet, folder placement, role-based sharing, Linear comments and a DM reply over a 35-ticket cohort.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** PASS (5). The rewritten rule 4 closes the previous round's ZOM-250 fork. Deep recheck P1 tested 30 forks and found none open.

### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: The rewritten card rule 4 makes Replaced depend on one observable fact, a later ticket's closing note saying it replaces this one. Only ZOM-282's note does (on ZOM-254), which closes last round's ZOM-250 fork and the \#401 fork. The comment set, scope edges and audience stay closed by rules 6, 1 and 7.

Alternative selection: B to F are every fork from the last two rounds re-tested against the rewritten rule 4. G is the strongest new fork the rewrite opens (what counts as a 'later' ticket when ZOM-254 closed after ZOM-282). A scan of every Linear comment (all are SQL rows; the base export has none) and every ZOM description finds no other closing note with replace wording.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Follow the card as updated: scope is every difficulty ticket created up to Aug 31; Replaced only where a later ticket's closing note says so (ZOM-282 on ZOM-254); comments only on ZOM-199 (flagged by Blake's reply) and on Replaced ZOM-254; share with the invite attendees. | 35 tickets; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; comments on ZOM-199 and ZOM-254 only. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. | 35 rows (31 title matches without Duplicates ZOM-203 and ZOM-276, plus tiers: tickets ZOM-221, 300, 305, 378); Live 22, Editor only 9, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab; DM gives the total and per-status counts. | CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: only when a later ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 286-286): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments." |
| B | match3d\#401 changed how enrage works (speed and damage split per monster, hp method dropped), so ZOM-282 is Replaced by match3d\#401 and gets a Replaced comment. | ZOM-282 Replaced by match3d\#401. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. Plus a Replaced comment on ZOM-282 naming match3d\#401. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. Plus ZOM-282. | Register shows ZOM-282 Replaced; DM counts Live 21, Replaced 2. | GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 181-181): "this gives enrage speed and damage their own values, they shared one since ZOM-282." |
| C | Comment on every ticket whose text the store builds contradict, including ZOM-42 (6-7 levels vs 10) and ZOM-275 (FTUE text). | Correction comments also on ZOM-42 and ZOM-275. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. Plus comments on ZOM-42 and ZOM-275. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. Plus ZOM-42 and ZOM-275. | Extra correction comments; register unchanged. | Z42A (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "gets assigned after the first 6-7 levels based on CPM"; Z275 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3327): "Making Them Stronger and Faster!" |
| D | Read the scope window in Pacific days with an Apr 21 start, dropping ZOM-23 (2025-04-21T04:51:38Z, Apr 20 PT) and ZOM-30. | 33 tickets; ZOM-23 and ZOM-30 out. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. | Register 33 rows; DM total and Live count two lower. | Z23 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3277): "2025-04-21T04:51:38Z" |
| E | Also post the register in \#zombie-design because Vincent asked Julia to drop it there. | Share with the invite and also post in \#zombie-design. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. Plus a Slack post in \#zombie-design. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. Plus C090N54TG79. | Same register; extra channel post. | VINCENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "julia when you have the difficulty list can you drop it in here too" |
| F | ZOM-277 (created after ZOM-250) changed how ZOM-250's average attack power works, so ZOM-250 is Replaced by ZOM-277 and gets a Replaced comment. | ZOM-250 Replaced by ZOM-277. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. Plus a Replaced comment on ZOM-250 naming ZOM-277. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. Plus ZOM-250. | Register shows ZOM-250 Replaced; DM counts Editor only 8, Replaced 2. | Z250 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3300): "(This is per set of items)"; Z277 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3329): "The average power should really be 334 / 5 uniques" |
| G | ZOM-254 was closed (2025-06-23) after ZOM-282 (2025-06-21) and its own QA note says blunder enrages the monsters, so ZOM-282 is not the 'later' ticket and ZOM-254 stays Live with no Replaced comment. | ZOM-254 Live; no Replaced ticket. | Same as A without the ZOM-254 comment. | Same as A without Linear ZOM-254. | Register shows ZOM-254 Live; DM counts Live 23, Replaced 0. | Z254C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 264-264): "checked on the dev build, blunder enrages the monsters on the board now" |

Explicit option inventory: The prompt lists no options; the status values sit in the incorporated card.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "build the register the way he set it up"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: EXCLUDED. Card rule 4 now makes a ticket Replaced only when a later ticket's closing note says so and says PRs that change or split its numbers don't. match3d\#401 is a PR, and its comment describes a split of the shared value, not a replacement.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: only when a later ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 181-181): "this gives enrage speed and damage their own values, they shared one since ZOM-282."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Live vs Replaced for ZOM-282. |
| writes | DIFFERENT | B adds a ZOM-282 comment. |
| destinations | DIFFERENT | B adds ZOM-282. |
| contents | DIFFERENT | Status cell and DM counts differ. |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The quoted sentences exclude PRs and value splits by name; \#401's comment says it gives speed and damage their own values.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: only when a later ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 181-181): "this gives enrage speed and damage their own values, they shared one since ZOM-282."

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

Resolution relevance challenge: The quoted sentences close the comment set by source and name ZOM-42; the reply names only ZOM-199; neither mail mentions ZOM-275.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 119-119): "ZOM-199 says &gt;= but the code never changed from the original spec"

Compared alternative: D
Resolution: EXCLUDED. The scope has no start date (everything since ZM started) so ZOM-23 and ZOM-30 are in under any timezone; the next title match after Aug 31 is ZOM-517 on 2025-09-03.
Resolution evidence: CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; Z517 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3591): "2025-09-03T22:22:22Z"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | D drops two tickets. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rows and counts differ by two. |

Authority chain: P → DMR → CARD\_SCOPE

Resolution relevance challenge: The quoted scope removes the start-date edge; Z517 shows no ticket near the Aug 31 end.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; Z517 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3591): "2025-09-03T22:22:22Z"

Compared alternative: E
Resolution: EXCLUDED. The prompt and card both define the audience as the invite list; Vincent is not an attendee and his channel request is not part of Leonard's ask.
Resolution evidence: CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system before monday's tuning session. can you take it off my plate? go through his ask and everything it points to and build the register the way he set it up. put it in the zm difficulty folder and share it with everyone on monday's tuning invite. if his rules say something needs to happen on the tickets, go ahead and do that too. then reply to leonard in the dm with what he asked for. go with your read on the details, no need to check with me first"; CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 172-172): "VALUES ('evt\_91674a9c23d012a9ac34da', 'julia.lawson@harmonygames.co', 'ZM difficulty tuning'"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | E adds a channel post. |
| writes | DIFFERENT | E adds a Slack post. |
| destinations | DIFFERENT | E adds \#zombie-design. |
| contents | DIFFERENT | Extra post. |

Authority chain: P → DMR → CARD\_R7

Resolution relevance challenge: The prompt names the audience as the invite; the invite on Julia's calendar does not include Vincent.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system before monday's tuning session. can you take it off my plate? go through his ask and everything it points to and build the register the way he set it up. put it in the zm difficulty folder and share it with everyone on monday's tuning invite. if his rules say something needs to happen on the tickets, go ahead and do that too. then reply to leonard in the dm with what he asked for. go with your read on the details, no need to check with me first"; CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 172-172): "VALUES ('evt\_91674a9c23d012a9ac34da', 'julia.lawson@harmonygames.co', 'ZM difficulty tuning'"

Compared alternative: F
Resolution: EXCLUDED. Rule 4 now requires a later ticket's closing note saying it replaces this one; ZOM-277's closing note says nothing changes in the game and names no replacement, and rule 4 says a ticket players never had stays Editor only.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: only when a later ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; Z277C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 278-278): "this is the average in the editor''s stats panel, nothing changes in the game itself"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Editor only vs Replaced for ZOM-250. |
| writes | DIFFERENT | F adds a ZOM-250 comment. |
| destinations | DIFFERENT | F adds ZOM-250. |
| contents | DIFFERENT | Status and DM counts differ. |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The quoted rule removes formula changes as a Replaced trigger and ranks Editor only over Replaced for tickets players never had; ZOM-277's closing note has no replace wording.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: only when a later ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; Z277C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 278-278): "this is the average in the editor''s stats panel, nothing changes in the game itself"

Compared alternative: G
Resolution: EXCLUDED. Rule 4 keys on a later ticket's closing note, not on close order. ZOM-282 was created a week after ZOM-254 and its closing note says it replaces the blunder 2.0 boost from ZOM-254. ZOM-254's QA note describes the dev build before the change and is not a closing note on a later ticket.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: only when a later ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 286-286): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Replaced vs Live for ZOM-254. |
| writes | DIFFERENT | G drops the ZOM-254 comment. |
| destinations | DIFFERENT | G drops Linear ZOM-254. |
| contents | DIFFERENT | Status and DM counts differ. |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: ZOM-282 is later by creation date and number, and its closing note names ZOM-254 explicitly, which is what the rule asks for.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: only when a later ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 286-286): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"

Strongest-alternative challenge (G): ZOM-254 was completed two days after ZOM-282, so a reader keying 'later' on close dates could keep ZOM-254 Live; only the creation order and the explicit naming in ZOM-282's note settle it.
Challenge evidence: Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 286-286): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

Forks settled by records (full list in the Deep Recheck fork list): starting tier (Blake's reply "cpm > 90, not >= 90", `TierManager.cs` `cpm > 90.0f`); demotion (both ZOM-42 rules ship in `WinRateRule.cs`); ZOM-315/277 Editor only ("nothing changes in the game itself"); enrage numbers from the sheet's Live tab (card rule 5).

**Feasibility:** PASS (5). Every ask maps to cataloged tools and the needed data exists; numeric values are tool-visible in the sheet, mail, ticket and code; no per-X breakdown lacks a field.

**Persona ACL Reachability:** PASS (5). DM (member), #zombie-design (member), Arthur's mails (her mailbox), the invite (her calendar), folder (writer), agenda doc and deck (reader), sheet (owner). Deep recheck P2 DR4 independently confirmed no hidden record.

**Explicit Tool Mention:** PASS (5).

**Clarity & Specificity:** PASS (5). The write set is the same under every reading tested: rule 6 plus the rewritten rule 4 give exactly two comments (ZOM-199, ZOM-254); folder and audience are named. A top-level DM message vs a thread reply under Leonard's message carries the same content and recipient (P1 F29), not a write divergence. No "I'll [verb]" statements.

**Contrived / Unnatural:** PASS (5). Destination and audience named the way the persona knows them; no staged typos, opaque IDs, exact timestamps, trap hints, riddles, audit wording or if-chains.

**Alignment with Today's Date:** PASS (5). "tuesday" → 2025-09-30 (DM 19:48:26Z, 12:48 PT); "monday's tuning session/invite" → 2025-10-06T17:00Z. Nothing treated as done falls after the clock.

**Originality:** N/A (no comparison samples supplied).

**Truthfulness:** PASS (5). Premises PR1–PR5 verified (Leonard's Tuesday DM; the Monday session and invite; the unique ZM Difficulty folder; Leonard's rules on the card the DM names). Deep recheck P3 re-verified 15 claims with no finding.

**Tool Use & Cross-service:** PASS (5). Linear sets the cohort, states and the Replaced trigger; Gmail sets shipped/Editor only, the cpm rule and the ZOM-199 comment; GitHub sets the tier rules; Sheets sets enrage; Calendar sets the share list; Trello carries the rules. Writes span Sheets, Drive, Linear and Slack.

**Investigation + Action:** PASS (5). **Coherence (Bolt-on):** PASS (5). **Business Function:** PASS (5), Product.

---

### Phase 3: Universe Feasibility

**Data Existence:** PASS (5). Every needed entity verified and retrievable through cataloged reads.

**Cross-Service Coherence:** FAIL (2).
- **Fail-level (confirmed from deep recheck P2 DR1).** The card makes the enrage sheet the source for per-monster enrage ("Enrage is per monster: your monster enrage sheet has the numbers") and asks for the rules "as they work in the store builds today". The injected Live tab (line 22) gives **Mailman 0.4/0.4, Mayor2 0.4/0.6 and PartyGirl (both VarC versions) 0.4/0.3**. The store-build code never got those values:
  - `enrageSpeedPercentage`/`enrageDamagePercentage` first appear in `Monster.cs` in `6a4d8ba57e` (2025-08-25). Before it, the code had one `enragePercentage`.
  - The only commits that set split per-monster values are `6a4d8ba57e` (12 files: MonsterBase, VarC Bikekid, Boxer, Cheerleader, Karen, Magician ×3, three Boss prefabs, Monster.cs) and `476a02949b` (2025-08-27, 11 files: VarC Boxer, Cheerleader, Chef, FootballPlayer, Karen, Magician ×3, Mayor1, Plumber ×2). Neither touches VarC-Mailman, VarC-Mayor2 or VarC-PartyGirl(-50HP).
  - Those prefabs' full history (`git log --all --full-history`) shows enrage data only from `920acdefa7` / `eae9586e62` (2025-08-07); later non-merge commits (`fd11448097`, revert `4e4e04aaab`) only move transform/health/isBoss lines. VarC-PartyGirl still carries the obsolete `enragePercentage: 0.6`.
  - So in builds cut from main those three monsters inherit MonsterBase `enrageSpeedPercentage: 0.8` / `enrageDamagePercentage: 0.8` (MonsterBase.prefab lines 342–343). The working-tree and git blobs of those prefabs are cut at 10,240 bytes, so the file text alone can't show it, but the commit file lists don't depend on blob content.
  - The base CodeRabbit comment on #401 lists those prefabs among the changed files, which the commit contradicts. That base self-disagreement is not scored on its own, but it is the record the injected sheet now agrees with.
  - Effect: three of the thirteen per-monster enrage values a run is graded on disagree between the named source and the shipped code. This changes graded values, so it is not a single minor slip.
- **Rejected (P2 DR2).** History row "2025-09-02 VarC values set (this tab: Live), Julia" vs commit `476a02949b` on 2025-08-27. Julia is the sheet owner, not the committer, so the row reads as when she logged the values on the tab. No record contradicts that, and no graded order, window or count uses the date. Optional clarity edit only.
- **Fixed since the last round:** the respawn-hp claims are gone. ZOM-282's note ("the hp part was switched off on the 19th"), the #401 comment ("drops the old EnrageHealth method, nothing has called it since june"), the bot copy (identical text, ts matches) and the History row "2025-06-19 enrage hp boost switched off" now agree with the June 19 hp switch-off and the current `Monster.cs`.
- Checked and consistent (NEW for changed rows, REUSED otherwise): every in-scope closing note matches its issue state and completion time; the ten other Live rows equal their prefab values; ZOM-282 (created 2025-06-19) is later than ZOM-254 (2025-06-12); every SQL date precedes the clock; Slack authors are channel members.
- Known base-data issues (not scored): none touched; no Snowflake or Confluence data.
- Not task-touched (not scored): ZOM-359 "parking this" comment on a Regression ticket outside scope; `Monster.cs` passes the single `enrageDamagePercentage` (damage doesn't stack across blunders), so keep rubric rows off stacking behaviour.

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|-----------|--------------|-------------|---------------|
| Prompt | Unique Ground Truth | 5 | Rewritten rule 4 closes the ZOM-250 fork; forks B–G excluded by quoted records |
| Prompt | Feasibility | 5 | All asks cataloged; data exists |
| Prompt | Persona ACL Reachability | 5 | Every scoped read visible to Julia |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | Same write set under every reading |
| Prompt | Contrived / Unnatural | 5 | No flags |
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
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three; seeded |
| Universe | Data Exists | 5 | Verified |
| Universe | Cross-Service Coherence | 2 | Sheet Live tab gives Mailman, Mayor2 and PartyGirl split enrage values the store-build code never received |

---

### Issues Found

| # | Issue | Severity | Dimension |
|---|-------|----------|-----------|
| 1 | Sheet `f_0ba93ae0238d9ed4178212` Live tab (SQL line 22) rows "Mailman 0.4/0.4", "Mayor2 0.4/0.6", "PartyGirl (both VarC versions) 0.4/0.3" disagree with match3d: no commit ever set split enrage values on VarC-Mailman, VarC-Mayor2 or VarC-PartyGirl(-50HP), so they run on MonsterBase 0.8/0.8 in the store builds. Graded rules-tab values. | Major | Cross-Service Coherence |

### Recommended Improvements

1. **Make the Live tab match the code (fixes issue 1).** In SQL line 22, delete the three rows `["Mailman", "0.4", "0.4", "0"]`, `["Mayor2", "0.4", "0.6", "0"]` and `["PartyGirl (both VarC versions)", "0.4", "0.3", "0"]`. The tab's existing row "MonsterBase (default for any monster without its own value)" 0.8/0.8 then covers them, which is what MonsterBase.prefab lines 342–343 ship. The other way is to keep the rows and set each to "0.8", "0.8". Either way the remaining ten rows (Bikekid, Boxer, Cheerleader, Chef, FootballPlayer, Karen, Magician, Mayor1, Plumber, MonsterBase) already match the prefabs. Keep the grid JSON valid, and keep any rubric row or OE off per-monster values for those three monsters.
2. **Optional:** the History row "2025-09-02 VarC values set (this tab: Live), Julia" could read "2025-08-27" (the prefab commit date) if you want it to log the code change rather than the sheet entry. Not scored.

The fix changes only the injection SQL. After saving it, send these again in order: `/injection`, `/prompt`, `/hardness`, `/oe`, `/rubric`. The prompt text needs no change.

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 7 sentences, 30 forks | 0 | 0 |
| P2 | 7 sentences | 2 defects (+2 informational) | 1 |
| P3 | 7 sentences, 15 claims | 1 | 0 |
| P4 | 7 sentences | 1 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P2 | "go through his ask and everything it points to and build the register the way he set it up." | SQL line 22 sheet Live tab "Mailman 0.4/0.4", "Mayor2 0.4/0.6", "PartyGirl 0.4/0.3"; match3d commits 6a4d8ba57e, 476a02949b; MonsterBase.prefab "enrageSpeedPercentage: 0.8" | §3 coherence | Cross-Service Coherence | CONFIRMED | Opened both commit file lists and the three prefabs' full history: no commit sets split enrage values on them; they inherit MonsterBase 0.8/0.8. P2's reading of the truncated files alone would not prove absence; the commit lists do. |
| DR2 | P2 | same sentence | SQL line 26 History "2025-09-02 VarC values set (this tab: Live), Julia"; commit 476a02949b 2025-08-27 | §3 date slip | Cross-Service Coherence | REJECTED | The row names Julia (sheet owner, not the committer) and reads as when the tab was set; no record contradicts it and nothing graded uses the date. |
| DR3 | P2 | "if his rules say something needs to happen on the tickets, go ahead and do that too." | Linear, Gmail, Trello, Slides, GCal, Slack | §3 two services | Tool Use & Cross-service | REJECTED | Informational pass result, no defect; agrees with the Phase 2 rating. |
| DR4 | P2 | "put it in the zm difficulty folder and share it with everyone on monday's tuning invite." | Folder d_96489e1e00a56685625939 Julia writer; DM D05HB64NMQU members | §3 hidden record | Persona ACL Reachability | REJECTED | Informational, no defect; confirms no hidden record. |
| DR5 | P3 | "if his rules say something needs to happen on the tickets, go ahead and do that too." | SQL linear_comments `sequence`, slides `notes`/`table_json`/`ordinal` vs schema snapshot | SQL columns | Cross-Service Coherence | REJECTED | Same as Eval 0 advisories A1/A2; the snapshot is marked unverified, so absence is not proven. Kept in the Injection Gate section. |
| DR6 | P4 | "then reply to leonard in the dm with what he asked for." | DM line 44 "reply here when it''s in the folder with how many tickets made the list and how many of each status" | §6.6 step list | Explicit procedure | REJECTED | One lowercase "then" with no first/finally list; it follows Leonard's own order. Not a step list. |

Effect on verdict: Cross-Service Coherence drops to 2 (DR1), so the verdict is FAIL. All other dimensions unchanged.

Fork list:
- F1: settled | Title keywords as whole words (rule 1) | Only tickets that "changed difficulty" (drop ZOM-30, 49, 50, 161) | Settled by: card rule 1 "That is any ticket with difficulty, difficult, tier, tiers, tiering, enrage, enraged, blunder or CPM as a whole word in the title"
- F2: settled | Attack-power titles in | Card description only | Settled by: commentCard 2025-09-30T15:41:55Z "adding to rule 1: attack power in the title counts too"
- F3: settled | "tiers:" tickets in (ZOM-221, 300, 305, 378) | Keyword titles only | Settled by: rule 1 "his closing note on those starts with 'tiers:'" and the four arthur.blake@ notes
- F4: settled | Duplicates ZOM-203, 276 out | In as Not shipped | Settled by: rule 1 "Duplicates are out"
- F5: settled | Aug 31 edge in any timezone | A boundary ticket flips | Settled by: no title match between ZOM-315 (2025-06-26) and ZOM-517 ("2025-09-03T22:22:22Z"); scope has no start date
- F6: settled | Shipped per Blake's mail | Brian's "the editor bits too" | Settled by: rule 3 "What is in the store builds and what counts as shipped: Blake''s store builds mail"
- F7–F12: settled | ZOM-45 Live; ZOM-173, 312, 277, 315, 250, 162, 163, 200, 201 Editor only; ZOM-202 Not shipped | Opposite statuses | Settled by: the closing notes ("the game reads it when it loads the level"; "this one is the set count in the level objects panel"; "the new events are the ones the editor listens to"; "nothing changes in the game itself"; "wip on a branch, nothing merged yet") and rule 1 "open, cancelled and never-merged ones are in, as Not shipped"
- F13 / G: settled | ZOM-254 Replaced by ZOM-282 | ZOM-254 Live because it closed after ZOM-282 | Settled by: ZOM-282 note "this replaces the blunder 2.0 boost from ZOM-254"; ZOM-282 created 2025-06-19T05:23:06Z, ZOM-254 2025-06-12T21:59:58Z
- F14 / B: settled | ZOM-282 Live | Replaced by match3d#401 | Settled by: rule 4 "PRs that change or split its numbers don''t"
- F / ZOM-250: settled | ZOM-250 Editor only | Replaced by ZOM-277 | Settled by: rule 4 "only when a later ticket''s closing note says it replaces this one" and "a ticket players never had stays Editor only or Not shipped"; ZOM-277 note "nothing changes in the game itself"
- F15: settled | ZOM-42 Live | Editor only | Settled by: rule 4 "ZOM-42 is the system itself: it stays Live"
- F16: settled | Analytics/level-data/FTUE tickets Live | Not shipped (no PR) | Settled by: Blake's mail "everything difficulty related was merged long before that"
- F17: settled | 35 = Live 22, Editor only 9, Replaced 1, Not shipped 3 | Edge totals 30/31/37 | Settled by: F1–F16
- F18: settled | Start tier cpm > 90 | >= 90 | Settled by: Blake's reply "the starting tier check in the build is cpm > 90, not >= 90"
- F19: settled | First 10 levels | ZOM-42 "after the first 6-7 levels" | Settled by: deck "first 10 levels", ZOM-199, `TierManager.cs` `totalGames == 10`
- F20: settled | Demotion on 4 losses or ≤50% of last 10 | 4 losses only (deck) | Settled by: rule 5 names the deck and ZOM-42; ZOM-42 "win rate for up to the last 10 games is 50% or lower"; `WinRateRule.cs`
- F21: settled | Level drops one tier after demotion | Not, since ZOM-293 is open | Settled by: ZOM-303 merged as match3d#244; ZOM-293's comment predates it
- F22: settled | Promotion 80%/10, tier -2 one win | none | Settled by: deck, ZOM-42, `WinRateRule.cs`
- F23: settled for UGT | Enrage from the sheet's Live tab | +50% (Brian/ZOM-282), deck +25% hp, Next pass tab | Settled by: rule 5 "your monster enrage sheet has the numbers"; Arthur "the blunder part of robert''s tiers deck is old". The three Live rows that disagree with the code are scored under Cross-Service Coherence (DR1), not as a fork.
- F24 / C: settled | Comments on ZOM-199 and ZOM-254 only | Also ZOM-42, ZOM-275, ZOM-282 | Settled by: rule 6 "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included"
- F25: settled | Folder d_96489e1e00a56685625939, one sheet two tabs | Another folder | Settled by: unique folder; agenda "One sheet with two tabs, Tickets and Rules in force"
- F26 / E: settled | Share with invite: Robert writer, others commenters | Also Vincent / #zombie-design | Settled by: prompt "share it with everyone on monday's tuning invite"; invite attendees; rule 7 "Robert can edit, everyone else comments"
- F27: settled | ZM ROADMAP card #80 | Domino "Difficulty baseline" card | Settled by: DM "the difficulty baseline card on the zm roadmap board"
- F28: settled | Tue = Sep 30, Mon = Oct 6 | none | Settled by: DM 2025-09-30T19:48:26Z; event 2025-10-06T17:00:00Z
- F29: not a fork | DM reply top-level | Thread reply | Same recipient and content; no material difference
- F30: not graded | Tier range -2..+2 (deck) | Player tiers to 5 (`MaxTier = 5`) | Missing: no record ranks them; rule 5 doesn't ask for a range, so keep rubric rows off a tier cap

Platform defects: none.

### FINAL VERDICT: FAIL

Score: 2

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session default effort

Clock: Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Next action: In SQL line 22, remove (or set to 0.8/0.8) the Live-tab rows for Mailman, Mayor2 and PartyGirl so the enrage sheet matches the store-build code. Then send /injection, /prompt, /hardness, /oe and /rubric again.

Evidence limits: The Evals/Docs PDFs were not re-extracted; Eval 1's restated bands and overrides were applied. Runtime acceptance of the `commenter` share role is unverified (declared free-string parameter). Eval 0 checks A–B were reused from the same-hash 0_injection.md, because this portal never writes the gate manifest. The VarC-Mailman, VarC-Mayor2 and VarC-PartyGirl prefab blobs are cut at 10,240 bytes in both the working tree and git objects; the DR1 finding rests on commit file lists and history, not on the truncated file text. Byte-identical SQL rows reuse prior /prompt facts.

Eval version: task-quality-v1

Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e

Reviewed prompt SHA-256: 22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787

Review context SHA-256: 144633e6766c52ffd89f1aeb0e466172aed7b616a143ebde1f3906400d6506c1

Prompt record SHA-256: fbfbe61ef3a10911342a1c72fd9ac01f1581856f29eb21aa772135fb17e2d700

**Lowest Dimension:** Cross-Service Coherence, 2. The enrage sheet's Live tab gives Mailman, Mayor2 and PartyGirl split values that no match3d commit ever applied.

**Summary:** The rewritten card rule 4 closes last round's ZOM-250 fork, and the hp-boost comments now agree with the code, so UGT and Clarity are back to 5. The deep recheck found that three rows of the newly expanded enrage Live tab disagree with the store-build code, which changes graded rules-tab values. That is a one-line SQL fix.
