## PROMPT EVALUATION REPORT

### Task: Julia delegates Leonard's ZM difficulty baseline: build the register (Tickets + Rules in force) from the Trello card rules, file it in ZM Difficulty, share it with the Monday invite, comment on tickets per card rule 6, reply to Leonard in the DM with counts
### Assigned Persona: Julia Lawson - Product Manager (roster `julia_lawson`, julia.lawson@harmonygames.co)
### Assigned Business Function: Product
### Assigned Competency: Engineering Ops
### Assigned Task Skill: Retrieval
### Assigned Horizon: long-horizon (Task Type field; Difficulty Mode "medium" recorded as context)

Review: `/prompt`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode. Actual review date 2026-10-30. Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe `Universe_SynthCut` (hg4-synth-sep30cut v16), manifest `Evals/references/universes/synthcut/universe_manifest.json` (sha256 `da2f4cf0…a1a`). Eval release task-quality-v1 (manifest `0040c6a5…9c2e`, verified with `hg_eval_release.py snapshot prompt`). Check record: prompt sha256 `22f26066…1787`, review context `62810c85…34ab`.

Inputs:
- `04_Prompt.txt`: revision 13, 525 bytes, sha256 `22f26066…1787`. Attached as `04_Prompt (4).txt`; byte-identical to revision 10 (the last /prompt round).
- `00_Task_Assigned_Inputs.md`: all five fields stated, which clears intake.
- `01_Universe_Inject.sql`: revision 12, 86,015 bytes, sha256 `e0df1fbb…a5fa`. Changed since the last /prompt round (revision 9, `99b35b05…b168`) on six lines, no IDs changed: 12 and 20 (sheet `modified_time` 2025-09-02T19:12:40Z → 2025-09-08T18:21:40Z), 22 (Live tab), 26 (History tab), 56 and 64 (card rule 4). Line numbers use the `hg_prompt_checks.py` convention; the changed lines are all before line 69, so they equal `grep -n`.
- No error/async config, dynamic context or reference files were supplied, and the prompt references none.
- Evidence contract `stage-evidence-v1`. reused_evidence: facts from the prior `1_prompt.md` (history copy `1_prompt-eb597b4d….md`) whose SQL rows and base records are byte-identical (every SQL line except 12, 20, 22, 26, 56, 64; Linear, Gmail, Calendar, Drive, Docs, Slides, Slack, GitHub code). Everything depending on the six changed lines was checked NEW.

**What changed since the last round (SQL only).**
- Card rule 4 (lines 56 and 64): "Replaced: only when a later ticket's closing note says it replaces this one" → "Replaced: only when **another** ticket's closing note says it replaces this one". The rest of the card is byte-identical.
- Enrage sheet Live tab (line 22): the Mailman 0.4/0.4, Mayor2 0.4/0.6 and PartyGirl 0.4/0.3 rows are gone. The MonsterBase row label changed from "MonsterBase (default for any monster without its own value)" to "MonsterBase (base prefab)", and a new last row reads `["Mailman, Mayor2, PartyGirl (both VarC versions)", "not copied yet", "not copied yet", "0"]`.
- History tab (line 26): "2025-09-02 VarC values set (this tab: Live), Julia" → "2025-09-08 Live tab copied from the VarC prefabs in main, Julia"; the sheet's modified time moved to 2025-09-08T18:21:40Z to match.

---

### Injection Gate
- State: NEVER_REVIEWED. The gate reads `reports/input_manifest.json`, which this portal's writer never creates.
- Eval 0 handling: `0_injection.md` (injection-static-v2, today) covers the identical SQL hash `e0df1fbb…a5fa` (revision 12) with **FINAL VERDICT: PASS**, COMPLETE. I re-ran `hg_injection_lint.py` (injection-lint-v1: 161 statements, 0 FAIL / 0 CHECK / 0 INFO). Static checks A–B are REUSED; the Check C items this prompt depends on were re-done here (Phase 3.2).
- Reviewed SQL sha256: `e0df1fbbc62ba4220a3dc4468909a417aee0e23b5e478b9739c76f424379fa5a`. Eval 0 verdict: PASS.
- Eval 0 findings on records this prompt depends on: none fail-level. Eval 0's C2 (PENDING last time, about the MonsterBase "default" label and four prefabs whose blobs are cut at 10,240 bytes) is closed there by the "not copied yet" row. That same row is what opens the UGT fork below; Eval 0 checks data integrity, not whether the task has one answer. Advisories A1/A2 (`linear_comments.sequence`, gslides `notes`/`table_json`/`ordinal` absent from the unverified schema snapshot) stay advisories.

---

### Phase 0: Sources read

Docs and references: Eval 1 (Local Overrides, STEP 0, 0.5, Phase 2, report template, Phase 5); `hg_reference.py guide prompt`; `prompt_rubric_reliability.md`; `deep_recheck.md`; `common_errors.md`; `acl.md`; `roster.json`; tool catalog. The PDFs in `Evals/Docs` were not re-extracted; Eval 1's inline bands and Local Overrides were applied (evidence limit, unchanged from prior rounds).

Universe exploration (synth-cut base plus SQL overlay):
- **Trello card rule 4** (NEW). With "another", the only closing note with replace wording is still ZOM-282's (line 286: "closing. this replaces the blunder 2.0 boost from ZOM-254"). A full scan of the SQL for "replac", "supersed" and "instead of" finds no other closing note; a scan of base Linear comments for "replac" returns nothing (the base export has no Linear comments; all 109 are SQL rows). Removing "later" removes the close-order fork (G) and adds no new Replaced candidate.
- **Enrage sheet** (NEW). Live tab rows: Bikekid 0.25/0.25, Boxer 0.5/0.4, Cheerleader 0.6/0.4, Chef 0.5/0.5, FootballPlayer 0.6/0.4, Karen 0.4/0.4, Magician (all three VarC versions) 0.2/0.2, Mayor1 0.5/0.5, Plumber (both VarC versions) 0.3/0.3, "MonsterBase (base prefab)" 0.8/0.8, "Mailman, Mayor2, PartyGirl (both VarC versions)" "not copied yet"/"not copied yet"; hp 0 throughout. History: "2025-09-08, Live tab copied from the VarC prefabs in main, Julia".
- **GitHub, the three uncopied monsters** (NEW). `git log --all` on `VarC-Mailman.prefab` and `VarC-Mayor2.prefab`: 920acdefa7 (2025-08-07), fd11448097 (2025-08-21), 4e4e04aaab (2025-08-25 revert); on `VarC-PartyGirl.prefab`: eae9586e62 (2025-08-07), fd11448097, 4e4e04aaab. The only commits that add `enrageSpeedPercentage` under `Assets/Prefabs/Monsters` are 6a4d8ba57e (2025-08-25) and 476a02949b (2025-08-27), and neither touches these prefabs. So in main they carry no split enrage override and run on MonsterBase's `enrageSpeedPercentage: 0.8` / `enrageDamagePercentage: 0.8` (MonsterBase.prefab lines 342–343). The working-tree text can't show this: `VarC-Mailman`, `VarC-Mayor2`, `VarC-PartyGirl` and `VarC-PartyGirl-50HP` are cut at 10,240 bytes, and `VarC-PartyGirl` shows only the obsolete `propertyPath: enragePercentage` / `value: 0.6` (lines 215–216), a field `Monster.cs` no longer declares (lines 87–88 have only `enrageSpeedPercentage` and `enrageDamagePercentage`).
- **Everything else** (REUSED, prior report Phase 0; rows byte-identical): 35-ticket scope (31 title matches without Duplicates ZOM-203 and ZOM-276, plus "tiers:" tickets ZOM-221, 300, 305, 378); card #80 with Leonard's updateCard (2025-09-30T14:04:31Z) and comment (15:41:55Z); Blake's store builds mail and reply (only ZOM-199 flagged); folder `ZM Difficulty` (Julia writer, unique); invite "ZM difficulty tuning" 2025-10-06T17:00Z (Leonard, Julia, Robert, Arthur Blake, Brian Foster); agenda "One sheet with two tabs, Tickets and Rules in force"; Robert's deck; DM D05HB64NMQU; #zombie-design decoys.

Status derivation (unchanged; shows solvability, not a golden answer): Live 22, Editor only 9, Replaced 1 (ZOM-254 → ZOM-282), Not shipped 3 (ZOM-202, 280, 293). Comments under rule 6: ZOM-199 and ZOM-254.

---

### Requirement ledger

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Find Leonard's Tuesday DM ask | SQL line 44 (D05HB64NMQU, 2025-09-30T19:48:26Z) | Slack DM history / search | Slack read/search tools | Julia is a DM member | The ask: register, then reply with total and per-status counts |
| "everything it points to": card rules | Trello card #80 (line 56), updateCard (64), commentCard (66) | DM names "the difficulty baseline card on the zm roadmap board" | `trello_get_cards_on_board`, `trello_get_card`, `trello_get_comments` | Trello unscoped | Rules 1–7 plus the attack-power addendum |
| Ticket scope (rule 1) | Linear ZOM issues; SQL "tiers:" comments | Linear search/list; per-ticket comments | Linear search/get, `linear_list_comments` | Linear unscoped | 35 tickets |
| Status per ticket (rules 3–4) | Blake's mail and reply; Linear states and closing notes; GitHub | Gmail search; Linear; GitHub | Gmail read; Linear; GitHub reads | Julia's mailbox; unscoped | Live 22 / Editor only 9 / Replaced 1 / Not shipped 3 |
| Rules in force tab (rule 5) | Deck, ZOM-42, Blake's reply, enrage sheet Live tab, code | GSlides, Linear, Gmail, GSheets, GitHub | `gslides_get_presentation_text`, `gsheets_values_batch_get`, `github_get_file_contents`, `github_get_file_history` | Deck shared; sheet owned by Julia; GitHub unscoped | Start tier > 90 → tier 1; promotion 80%/10 and tier -2 one win; demotion on 4 losses or ≤50%/10 with the level dropping one tier (ZOM-303); enrage per monster from the Live tab, hp 0. **Mailman, Mayor2 and PartyGirl: 0.8/0.8 (store builds) or "not copied yet" (sheet), unsettled; see issue 1** |
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

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS. Data seeding PASS. Superseded sources (deck "90 or more" vs Blake's "cpm > 90"; deck blunder slide vs Arthur's Slack); decoys (Brian's "+50% … every monster", "the editor bits too", Domino card #211, "Next pass" tab, Vincent's channel request).

**Naturalness:** PASS. First person, lowercase, casual; no document formatting, polished connectives or enumerated specs.

**Anti-Patterns:**
| Pattern | Status |
|---------|--------|
| Command List | PASS. One lowercase "then" with no first/finally (P4 DR1, rejected as last round; optional rewording below) |
| Bolt-On | PASS. Every sentence serves the baseline |
| Pre-Solving | PASS. No counts, tickets, statuses or causes named |
| Tool Mention | PASS. "dm", "folder", "invite", "tickets" are natural nouns |

**Diversity:** Two-tab sheet, folder placement, role-based sharing, Linear comments and a DM reply over a 35-ticket cohort.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** FAIL (2). Two forks are open.
- **Fork H, new this round.** Rule 4's "another" closes last round's close-order fork, and forks B–G stay excluded. But the new "not copied yet" row opens a fork. Rule 5 says "your monster enrage sheet has the numbers" and asks for enrage "as they work in the store builds today". The sheet gives Mailman, Mayor2 and PartyGirl no numbers, and since the label change no record says what a monster without its own value runs on. One run writes 0.8/0.8, the store-build value, which is derivable only from git history and prefab inheritance (and for Mayor2 the exported prefab text has no Monster component at all). Another run lists them as not copied yet. The Rules in force tabs differ, and no prompt sentence or record ranks the two readings. It is not a both-fair figure: three monsters are affected, and "not copied yet" is not a value on a record.
- **Fork J, found by deep recheck P1; it was already in the data last round.** Leonard's card comment says "attack power in the title counts too". ZOM-271 (Done, created 2025-06-16) is titled "Comprehensive Item Stat Display Rules also ATK POWER BUG. Also Change Damage sort to ATK Power sort". It never says the words "attack power", yet display-only attack power tickets such as ZOM-246 are in. So the register has 35 or 36 rows, and the DM's total and Live counts change with it. No record says whether the abbreviation counts.

### Unique Ground Truth comparison

Unique Ground Truth: FAIL 2

Basis: Rule 4 now reads 'another ticket's closing note', which removes last round's close-order fork G; B to G stay excluded. The revision-12 enrage sheet opens a new fork: rule 5 says the sheet has the per-monster numbers and asks for enrage as it works in the store builds today, but the sheet gives Mailman, Mayor2 and PartyGirl 'not copied yet' and no record states what they run on. Readings A (0.8/0.8 from MonsterBase) and H (not copied, no numbers) give different Rules in force contents and nothing settles it. Deep recheck P1 confirmed a second open fork: Leonard's comment adds 'attack power in the title', and ZOM-271's title says 'ATK POWER', so the scope is 35 or 36 tickets (DM counts differ).

Alternative selection: B to G are every fork from earlier rounds re-tested against revision 12 (rule 4 'another'). H and I are the forks the new 'not copied yet' row opens; H is the strongest, since it follows the card's named source literally. A scan of every Linear comment and ZOM description finds no other closing note with replace wording. J (ZOM-271's 'ATK POWER' title) was added from deep recheck P1 DR1.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Follow the card as updated: scope is every difficulty ticket created up to Aug 31; Replaced only where another ticket's closing note says so (ZOM-282 on ZOM-254); comments only on ZOM-199 (flagged by Blake's reply) and on Replaced ZOM-254; share with the invite attendees; the Rules in force tab gives enrage as it works in the store builds today, so Mailman, Mayor2 and PartyGirl, which the sheet has not copied, are given the MonsterBase 0.8 speed / 0.8 damage they run on. | 35 tickets; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; comments on ZOM-199 and ZOM-254 only. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. | 35 rows (31 title matches without Duplicates ZOM-203 and ZOM-276, plus tiers: tickets ZOM-221, 300, 305, 378); Live 22, Editor only 9, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab, with Mailman, Mayor2 and PartyGirl at 0.8 speed / 0.8 damage (MonsterBase); DM gives the total and per-status counts. | CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 286-286): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; SHEET\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 22-22): "\["MonsterBase (base prefab)", "0.8", "0.8", "0"\]" |
| B | match3d\#401 changed how enrage works (speed and damage split per monster, hp method dropped), so ZOM-282 is Replaced by match3d\#401 and gets a Replaced comment. | ZOM-282 Replaced by match3d\#401. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. Plus a Replaced comment on ZOM-282 naming match3d\#401. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. Plus ZOM-282. | Register shows ZOM-282 Replaced; DM counts Live 21, Replaced 2. | GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 181-181): "this gives enrage speed and damage their own values, they shared one since ZOM-282." |
| C | Comment on every ticket whose text the store builds contradict, including ZOM-42 (6-7 levels vs 10) and ZOM-275 (FTUE text). | Correction comments also on ZOM-42 and ZOM-275. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. Plus comments on ZOM-42 and ZOM-275. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. Plus ZOM-42 and ZOM-275. | Extra correction comments; register unchanged. | Z42A (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "gets assigned after the first 6-7 levels based on CPM"; Z275 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3327): "Making Them Stronger and Faster!" |
| D | Read the scope window in Pacific days with an Apr 21 start, dropping ZOM-23 (2025-04-21T04:51:38Z, Apr 20 PT) and ZOM-30. | 33 tickets; ZOM-23 and ZOM-30 out. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. | Register 33 rows; DM total and Live count two lower. | Z23 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3277): "2025-04-21T04:51:38Z" |
| E | Also post the register in \#zombie-design because Vincent asked Julia to drop it there. | Share with the invite and also post in \#zombie-design. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. Plus a Slack post in \#zombie-design. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. Plus C090N54TG79. | Same register; extra channel post. | VINCENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "julia when you have the difficulty list can you drop it in here too" |
| F | ZOM-277 (created after ZOM-250) changed how ZOM-250's average attack power works, so ZOM-250 is Replaced by ZOM-277 and gets a Replaced comment. | ZOM-250 Replaced by ZOM-277. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. Plus a Replaced comment on ZOM-250 naming ZOM-277. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. Plus ZOM-250. | Register shows ZOM-250 Replaced; DM counts Editor only 8, Replaced 2. | Z250 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3300): "(This is per set of items)"; Z277 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3329): "The average power should really be 334 / 5 uniques" |
| G | ZOM-254 was closed (2025-06-23) after ZOM-282 (2025-06-21) and its own QA note says blunder enrages the monsters, so ZOM-282 is not the 'later' ticket and ZOM-254 stays Live with no Replaced comment. | ZOM-254 Live; no Replaced ticket. | Same as A without the ZOM-254 comment. | Same as A without Linear ZOM-254. | Register shows ZOM-254 Live; DM counts Live 23, Replaced 0. | Z254C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 264-264): "checked on the dev build, blunder enrages the monsters on the board now" |
| H | Same register, but the enrage section copies the sheet the card names: the nine monster rows and MonsterBase with their numbers, and Mailman, Mayor2 and PartyGirl listed as not copied yet (no numbers), because the card says the sheet has the numbers and the sheet gives none for them. | 35 tickets; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; comments on ZOM-199 and ZOM-254 only. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. | 35 rows (31 title matches without Duplicates ZOM-203 and ZOM-276, plus tiers: tickets ZOM-221, 300, 305, 378); Live 22, Editor only 9, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab, with Mailman, Mayor2 and PartyGirl shown as not copied yet (no enrage numbers); DM gives the total and per-status counts. | CARD\_R5 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Enrage is per monster: your monster enrage sheet has the numbers."; SHEET\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 22-22): "\["Mailman, Mayor2, PartyGirl (both VarC versions)", "not copied yet", "not copied yet", "0"\]" |
| I | Fill the gap from the VarC prefabs the History tab says the Live tab was copied from: VarC-PartyGirl carries enragePercentage 0.6, so PartyGirl is 0.6 speed / 0.6 damage; Mailman and Mayor2 show no enrage value in their prefab text. | 35 tickets; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; comments on ZOM-199 and ZOM-254 only. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. | 35 rows (31 title matches without Duplicates ZOM-203 and ZOM-276, plus tiers: tickets ZOM-221, 300, 305, 378); Live 22, Editor only 9, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab, with PartyGirl at 0.6 / 0.6 and Mailman and Mayor2 without numbers; DM gives the total and per-status counts. | SHEET\_HIST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 26-26): "\["2025-09-08", "Live tab copied from the VarC prefabs in main", "Julia"\]"; PG\_PREFAB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/VarC-PartyGirl.prefab lines 215-216): "propertyPath: enragePercentage" |
| J | Leonard's comment adds attack power in the title; ZOM-271's title says 'ATK POWER' / 'ATK Power' (and its description 'the attack power upgrade'), so ZOM-271 (Done, June 16, card-profile stat display) is in scope as Live. | 36 tickets; ZOM-271 Live; otherwise as A. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90) and ZOM-254 (replaced by ZOM-282); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. | 36 rows (adds ZOM-271); Live 23, Editor only 9, Replaced 1, Not shipped 3; DM total 36 and Live 23. | TCOMMENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 66-66): "attack power in the title counts too"; Z271 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3323): "Comprehensive Item Stat Display Rules also ATK POWER BUG. Also Change Damage sort to ATK Power sort" |

Explicit option inventory: The prompt lists no options; the status values sit in the incorporated card.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "build the register the way he set it up"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: EXCLUDED. Card rule 4 now makes a ticket Replaced only when another ticket's closing note says so and says PRs that change or split its numbers don't. match3d\#401 is a PR, and its comment describes a split of the shared value, not a replacement.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 181-181): "this gives enrage speed and damage their own values, they shared one since ZOM-282."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Live vs Replaced for ZOM-282. |
| writes | DIFFERENT | B adds a ZOM-282 comment. |
| destinations | DIFFERENT | B adds ZOM-282. |
| contents | DIFFERENT | Status cell and DM counts differ. |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The quoted sentences exclude PRs and value splits by name; \#401's comment says it gives speed and damage their own values.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 181-181): "this gives enrage speed and damage their own values, they shared one since ZOM-282."

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
Resolution: EXCLUDED. Rule 4 now requires another ticket's closing note saying it replaces this one; ZOM-277's closing note says nothing changes in the game and names no replacement, and rule 4 says a ticket players never had stays Editor only.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; Z277C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 278-278): "this is the average in the editor''s stats panel, nothing changes in the game itself"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Editor only vs Replaced for ZOM-250. |
| writes | DIFFERENT | F adds a ZOM-250 comment. |
| destinations | DIFFERENT | F adds ZOM-250. |
| contents | DIFFERENT | Status and DM counts differ. |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The quoted rule removes formula changes as a Replaced trigger and ranks Editor only over Replaced for tickets players never had; ZOM-277's closing note has no replace wording.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; Z277C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 278-278): "this is the average in the editor''s stats panel, nothing changes in the game itself"

Compared alternative: G
Resolution: EXCLUDED. Rule 4 now keys on another ticket's closing note, with no ordering condition. ZOM-282's closing note says it replaces the blunder 2.0 boost from ZOM-254; ZOM-254's QA note describes the dev build and is not a closing note on another ticket that replaces it. Close order no longer matters.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 286-286): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Replaced vs Live for ZOM-254. |
| writes | DIFFERENT | G drops the ZOM-254 comment. |
| destinations | DIFFERENT | G drops Linear ZOM-254. |
| contents | DIFFERENT | Status and DM counts differ. |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The rule no longer says 'later', so close dates cannot reverse it; ZOM-282's note names ZOM-254 explicitly, which is what the rule asks for.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 286-286): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"

Compared alternative: H
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. Rule 5 names the sheet as where the enrage numbers are and also asks for enrage as it works in the store builds today. The sheet gives Mailman, Mayor2 and PartyGirl no numbers ('not copied yet'), and since revision 10 the MonsterBase row is labelled only 'base prefab', no longer 'default for any monster without its own value'. No visible record states what those three run on: the 0.8/0.8 of Reading A rests on Unity variant inheritance plus the absence of an override in prefab files whose text is cut at 10,240 bytes (VarC-Mailman, VarC-Mayor2, both VarC-PartyGirl). Nothing in the prompt, DM, card or sheet ranks the store-build value over the named sheet's gap, so the per-monster enrage content of the Rules in force tab differs. Deep recheck P2 DR1 (confirmed): the exported VarC-Mayor2.prefab text holds only VFX objects with no Monster component or m\_SourcePrefab before the 10,240-byte cut, so Mayor2's value under Reading A is visible only through commit history (no commit ever added enrageSpeedPercentage to it).
Resolution evidence: CARD\_R5 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Enrage is per monster: your monster enrage sheet has the numbers."; CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; SHEET\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 22-22): "\["Mailman, Mayor2, PartyGirl (both VarC versions)", "not copied yet", "not copied yet", "0"\]"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and share list. |
| writes | SAME | Same spreadsheet, Linear comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | Rules in force tab: three monsters at 0.8/0.8 (A) vs listed as not copied yet with no numbers (H). |

Resolution relevance challenge: Not a strawman: H is a literal application of the card's own pointer ('your monster enrage sheet has the numbers') to the sheet's own words. The only passage favouring A ('as they work in the store builds today') does not say where the missing numbers come from, and no record states 0.8 for these monsters. This is not a both-fair figure: three monsters are affected, and H's 'not copied yet' is not a figure stated on a record.
Delegation challenge: NOT_CLAIMED. The prompt says "go with your read on the details" but authorizes no alternative contents; no materially different result is accepted as interchangeable.
Challenge evidence: CARD\_R5 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Enrage is per monster: your monster enrage sheet has the numbers."; SHEET\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 22-22): "\["MonsterBase (base prefab)", "0.8", "0.8", "0"\], \["Mailman, Mayor2, PartyGirl (both VarC versions)", "not copied yet", "not copied yet", "0"\]"

Compared alternative: I
Resolution: EXCLUDED. The card asks for enrage as it works in the store builds today, and the build's Monster component has only enrageSpeedPercentage and enrageDamagePercentage; the enragePercentage 0.6 left on VarC-PartyGirl is a field the code no longer reads, so 0.6 is not what PartyGirl runs on.
Resolution evidence: CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; MONSTER\_CS (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Monster/Monster.cs lines 87-88): "\[SerializeField\] private float enrageSpeedPercentage = 0.25f;"; PG\_PREFAB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/VarC-PartyGirl.prefab lines 215-216): "propertyPath: enragePercentage"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and share list. |
| writes | SAME | Same spreadsheet, Linear comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | PartyGirl 0.6/0.6 vs 0.8/0.8; Mailman and Mayor2 without numbers. |

Authority chain: P → DMR → CARD\_R5B

Resolution relevance challenge: The store-build criterion is tied to the code, and Monster.cs declares no enragePercentage field, so the prefab value is dead data.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted.
Challenge evidence: MONSTER\_CS (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Monster/Monster.cs lines 87-88): "\[SerializeField\] private float enrageSpeedPercentage = 0.25f;"

Compared alternative: J
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. Confirmed from deep recheck P1 DR1. Rule 1's whole-word test covers the listed keywords; Leonard's comment adds 'attack power in the title' without saying whether an abbreviation counts. ZOM-271's title has 'ATK POWER' / 'ATK Power', never the words 'attack power'. Display-only attack power tickets such as ZOM-246 are already in, so a reader who treats ATK as attack power includes ZOM-271; a literal reader leaves it out. No record settles abbreviations, and the register rows and DM counts differ.
Resolution evidence: TCOMMENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 66-66): "attack power in the title counts too"; CARD\_R1W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "as a whole word in the title"; Z271 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3323): "Comprehensive Item Stat Display Rules also ATK POWER BUG. Also Change Damage sort to ATK Power sort"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-271 in (Live) vs out. |
| writes | SAME | Same spreadsheet, comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | One more register row; DM total 36 vs 35 and Live 23 vs 22. |

Resolution relevance challenge: Not a strawman: 'ATK' is the game's own short form for attack (the description says 'the atk power upgrade preview'), and the comment's reason ('enrage tuning leans on those numbers') does not exclude it. 'as a whole word in the title' governs the keyword list, not the comment's phrase. Not a both-fair figure: a register row and two DM counts change.
Delegation challenge: NOT_CLAIMED. No alternative scope is authorized.
Challenge evidence: TCOMMENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 66-66): "adding to rule 1: attack power in the title counts too, enrage tuning leans on those numbers. rest of the card stands."

Strongest-alternative challenge (H): H applies rule 5's own pointer to the sheet's own words; A needs a value no record states, derived from prefab inheritance in truncated files.
Challenge evidence: CARD\_R5 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "Enrage is per monster: your monster enrage sheet has the numbers."; SHEET\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 22-22): "\["Mailman, Mayor2, PartyGirl (both VarC versions)", "not copied yet", "not copied yet", "0"\]"

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

**Feasibility:** PASS (5). Every ask maps to cataloged tools and the needed data exists. The tier and sheet values are tool-visible. For the three uncopied monsters, the store-build value (0.8/0.8) is reachable only through `github_get_file_history`/commit files plus Unity prefab inheritance, because their prefab text is cut at 10,240 bytes. The runtime behaviour of those history tools is UNVERIFIED (evidence limit). This is not scored separately, because the fork is already the UGT failure, and the recommended fix removes the need for it.

**Persona ACL Reachability:** PASS (5). DM (member), #zombie-design (member), Arthur's mails (her mailbox), the invite (her calendar), folder (writer), agenda doc and deck (reader), sheet (owner); GitHub and Linear unscoped.

**Explicit Tool Mention:** PASS (5).

**Clarity & Specificity:** PASS (5). The write set is the same under every reading tested: rule 6 with rule 4 gives exactly two comments (ZOM-199, ZOM-254), and the folder and audience are named. Fork H differs only in the contents of the Rules in force tab, which is scored once under UGT. A top-level DM message vs a thread reply carries the same content and recipient. No "I'll [verb]" statements.

**Contrived / Unnatural:** PASS (5). Destination and audience are named the way the persona knows them. No staged typos, opaque IDs, exact timestamps, trap hints, riddles, audit wording or if-chains (P4 DR2 checked the "if his rules say…" sentence: it is one conditional whose rule lives in the card).

**Alignment with Today's Date:** PASS (5). "tuesday" → 2025-09-30 (DM 19:48:26Z, 12:48 PT); "monday's tuning session/invite" → 2025-10-06T17:00Z. The new sheet dates (History 2025-09-08, modified 2025-09-08T18:21:40Z) fall before the clock.

**Originality:** N/A (no comparison samples supplied).

**Truthfulness:** PASS (5). Premises PR1–PR5 verified (Leonard's Tuesday DM; the Monday session and invite; the unique ZM Difficulty folder; Leonard's rules on the card the DM names). The prompt text is unchanged, and none of these records changed.

**Tool Use & Cross-service:** PASS (5). Linear sets the cohort, states and the Replaced trigger. Gmail sets shipped/Editor only, the cpm rule and the ZOM-199 comment. GitHub sets the tier rules. Sheets sets enrage. Calendar sets the share list. Trello carries the rules. Writes span Sheets, Drive, Linear and Slack.

**Investigation + Action:** PASS (5). **Coherence (Bolt-on):** PASS (5). **Business Function:** PASS (5), Product. **Complexity Dimensions & Data Seeding:** PASS (5).

---

### Phase 3: Universe Feasibility

**Data Existence:** PASS (5). Every needed entity is verified and retrievable through cataloged reads.

**Cross-Service Coherence:** PASS (5).
- **Fixed since the last round:** the Live tab no longer gives Mailman, Mayor2 and PartyGirl values that the code never received. The 11 numeric rows equal the VarC prefab overrides and MonsterBase 0.8/0.8 in main at 2025-09-08T18:21:40Z, and they stay unchanged through the clock (Eval 0 Check C, same SQL hash; spot-checked here against the prefab texts for Bikekid, Boxer, Cheerleader, Chef, FootballPlayer, Karen, Magician ×3, Mayor1 and Plumber ×2).
- The History row "2025-09-08 Live tab copied from the VarC prefabs in main" and the modified time 2025-09-08T18:21:40Z agree with each other. Last round's optional date note is resolved.
- "not copied yet" is a sheet state, not a factual claim about the code, so it contradicts no record. Its effect on the answer is the UGT fork, not a coherence defect.
- Rule 4's "another" agrees with ZOM-282's note; no other note uses replace wording.
- Checked and consistent (REUSED, byte-identical rows): every in-scope closing note matches its issue state and completion time; ZOM-282 (created 2025-06-19) names ZOM-254; every SQL date precedes the clock; Slack authors are channel members.
- Known base-data issues (not scored): none touched; no Snowflake or Confluence data.
- Not task-touched (not scored): `Monster.cs` passes the single `enrageDamagePercentage` (damage doesn't stack across blunders), so keep rubric rows off stacking behaviour.

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|-----------|--------------|-------------|---------------|
| Prompt | Unique Ground Truth | 2 | Two open forks: Mailman/Mayor2/PartyGirl enrage 0.8/0.8 vs "not copied yet"; ZOM-271 "ATK POWER" in or out (35 vs 36 tickets) |
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
| Universe | Cross-Service Coherence | 5 | Last round's Live-tab mismatch fixed; no new inconsistency |

---

### Issues Found

| # | Issue | Severity | Dimension |
|---|-------|----------|-----------|
| 1 | Card rule 5 (SQL line 56) says "Enrage is per monster: your monster enrage sheet has the numbers" and asks for enrage "as they work in the store builds today". The sheet's Live tab (line 22) now gives `["Mailman, Mayor2, PartyGirl (both VarC versions)", "not copied yet", "not copied yet", "0"]`, and the MonsterBase row is labelled only "(base prefab)". So the Rules in force tab can list those three at 0.8/0.8 (what they run on in main, provable only from git history because their prefabs are cut at 10,240 bytes) or as not copied yet, and no record picks one. | Major | Unique Ground Truth |
| 2 | Leonard's card comment (SQL line 66) says "adding to rule 1: attack power in the title counts too". ZOM-271's title says "ATK POWER" / "ATK Power", not "attack power". Including it gives 36 tickets and Live 23; leaving it out gives 35 and Live 22. No record settles whether the short form counts. | Major | Unique Ground Truth |

### Recommended Improvements

1. **Settle the three uncopied monsters in the card (fixes issue 1).** In card rule 5, on SQL line 56 and identically inside the updateCard `card.desc` on line 64 (the sentence appears exactly once on each line), replace `Enrage is per monster: your monster enrage sheet has the numbers.` with `Enrage is per monster: your monster enrage sheet has the numbers, and any monster it hasn''t copied yet goes on the tab as not copied.` Keep the doubled apostrophe and leave the sheet unchanged. Then rule 5 itself says what to write for Mailman, Mayor2 and PartyGirl, and no code or prefab inheritance is needed. Putting numbers on the sheet for them instead is not recommended: the exported `VarC-Mayor2.prefab` text holds no Monster component, so its value can't be checked from the file.
2. **Settle the abbreviation in Leonard's comment (fixes issue 2).** On SQL line 66 (the only place the text appears), replace `adding to rule 1: attack power in the title counts too,` with `adding to rule 1: attack power spelled out in the title counts too,`. That keeps ZOM-271 out and the count at 35. If you would rather include it, say so instead (for example `attack power in the title counts too, ATK as well,`), and update the counts you expect to 36 tickets and Live 23.
3. **Optional, wording (not scored):** to avoid any reviewer reading the lowercase "then" as a step list, "then reply to leonard in the dm with what he asked for" could read "once it's in the folder, reply to leonard in the dm with what he asked for." This follows Leonard's own "reply here when it's in the folder" (SQL line 44).

The card and comment text, and any prompt wording, are screened for AI-written text, so put each change in your own words. Fixes 1 and 2 change only the injection SQL. After saving it, send these again in order: `/injection`, `/prompt`, `/hardness`, `/oe`, `/rubric`. If you also take the optional prompt rewording, the same list applies. Keep the rubric and OEs consistent with the fixes: the three monsters as not copied, and ZOM-271 in or out to match the comment.


## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 7 sentences, 15 forks | 3 | 2 |
| P2 | 7 sentences | 3 | 1 |
| P3 | 7 sentences, 11 claims | 0 | 0 |
| P4 | 7 sentences | 2 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P1 | "go through his ask and everything it points to and build the register the way he set it up." | Trello comment (SQL line 66) "attack power in the title counts too"; Linear ZOM-271 (/issues/3323) title "…ATK POWER BUG. Also Change Damage sort to ATK Power sort" | §2 which items are in the set | Unique Ground Truth | CONFIRMED | Opened both. The title never has the words "attack power", and rule 1's "as a whole word in the title" governs the keyword list, not the comment. Display-only attack power tickets (ZOM-246) are in, so no record rules out including ZOM-271. Fork J. |
| DR2 | P1 | "build the register the way he set it up." | Blake's mail (line 75) "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; ZOM-200 (Done, debug menu) | §2 which status | Unique Ground Truth | REJECTED | Card rule 1 limits Not shipped to "open, cancelled and never-merged ones", and ZOM-200 is Done and merged. Brian's Slack (line 46) counts the debug menu among "the editor bits too (tier delete, the stats window, the debug menu)". So Editor only is the label, as settled in earlier rounds. |
| DR3 | P1 | "build the register the way he set it up." | Sheet Live tab (line 22) "Mailman, Mayor2, PartyGirl (both VarC versions)", "not copied yet"; VarC prefabs cut at 10,240 bytes | §2 which number | Unique Ground Truth | CONFIRMED | Same as the main review's fork H. Opened the sheet, the prefabs and the git history. |
| DR4 | P2 | "go through his ask and everything it points to and build the register the way he set it up." | `VarC-Mayor2.prefab` (VFX objects only, no Monster component, cut at 10,240 bytes); `VarC-PartyGirl.prefab` lines 215–216 `enragePercentage` 0.6 | §3 hidden record / data exists | Unique Ground Truth | CONFIRMED | Verified Mayor2's text has no `m_SourcePrefab` or Monster target. It strengthens fork H (Reading A's Mayor2 value is visible only through history) and rules out fix "put numbers on the sheet". It is merged into H, not scored twice. The 10,240-byte cap is not on the known platform list, so it is not tagged PLATFORM. |
| DR5 | P2 | same sentence | `WinHistory.cs` `GetWinRate` counts `winHistory[i]` from index 0 over a newest-last string; ZOM-42 "last 10 games" | §3 coherence | Cross-Service Coherence | REJECTED | The code does read the oldest results since the last tier change. But card rule 5 names the sources for the tier rules: "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself." The method's own docstring says "Get win rate over last n games", so this is an unflagged base code bug, not a record the task relies on. Advisory: keep rubric rows off the oldest-vs-latest window. |
| DR6 | P2 | same sentence | `Monster.cs` line 628 `EnrageDamage(enrageDamagePercentage);` | §3 coherence | Cross-Service Coherence | REJECTED | Already noted as not task-touched. Rule 5 asks for per-monster numbers, not stacking behaviour; keep rubric rows off stacking. |
| DR7 | P4 | "then reply to leonard in the dm with what he asked for." | DM (line 44) "reply here when it''s in the folder with how many tickets made the list and how many of each status" | §3 search hits / §6.6 | Command list | REJECTED | One lowercase "then" with no first/finally. §6.6 defines the failure as a "first / then / finally" list. The order is Leonard's own. Optional rewording given. |
| DR8 | P4 | "if his rules say something needs to happen on the tickets, go ahead and do that too." | Card rule 6 (line 56) | §2.7 if-chains | Contrived | REJECTED | P4 itself marked it advisory: one conditional, the rule lives in the card, no hidden destination. |

Effect on verdict: UGT stays 2 with a second confirmed fork (J); no other dimension changed. The verdict stays FAIL.

Fork list:
- F1 / H: open | Mailman, Mayor2, PartyGirl at MonsterBase 0.8/0.8 (store builds) | Listed as not copied yet (the named sheet) | Missing: a card line or sheet value saying what to write for monsters the sheet hasn't copied (fix 1)
- F2 / J: open | ZOM-271 out (35 tickets, Live 22) | ZOM-271 in as Live (36, Live 23) | Missing: a comment line saying whether "ATK" counts as attack power (fix 2)
- F3 / I: settled | Enrage from the sheet and code | PartyGirl 0.6/0.6 from the old prefab field | Settled by: `Monster.cs` lines 87–88 declare only "enrageSpeedPercentage" and "enrageDamagePercentage", and rule 5 "as they work in the store builds today"
- F4 / G: settled | ZOM-254 Replaced by ZOM-282 | ZOM-254 Live because it closed after ZOM-282 | Settled by: rule 4 "only when another ticket''s closing note says it replaces this one" and ZOM-282 "this replaces the blunder 2.0 boost from ZOM-254"
- F5 / B: settled | ZOM-282 Live | Replaced by match3d#401 | Settled by: rule 4 "PRs that change or split its numbers don''t"
- F6 / F: settled | ZOM-250 Editor only | Replaced by ZOM-277 | Settled by: ZOM-277 note "nothing changes in the game itself" and rule 4 "a ticket players never had stays Editor only or Not shipped"
- F7 / C: settled | Comments on ZOM-199 and ZOM-254 only | Also ZOM-42, ZOM-275 | Settled by: rule 6 "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included"
- F8 / D: settled | ZOM-23 and ZOM-30 in | Out under a Pacific Apr 21 start | Settled by: scope "every ZOM ticket created up to Aug 31 (so everything since we started ZM)"; next title match ZOM-517 "2025-09-03T22:22:22Z"
- F9 / E: settled | Share with the invite only | Also post in #zombie-design | Settled by: prompt "share it with everyone on monday's tuning invite"; rule 7 "Share it with everyone on the tuning session invite"
- F10: settled | ZOM-200/201 Editor only | Not shipped | Settled by: rule 1 "open, cancelled and never-merged ones are in, as Not shipped"; Brian "the editor bits too (tier delete, the stats window, the debug menu)"
- F11: settled | Duplicates ZOM-203, 276 out | In | Settled by: rule 1 "Duplicates are out"
- F12: settled | "tiers:" tickets ZOM-221, 300, 305, 378 in | Keyword titles only | Settled by: rule 1 "his closing note on those starts with ''tiers:''"
- F13: settled | Start tier cpm > 90 | >= 90 | Settled by: Blake's reply "ZOM-199 says >= but the code never changed from the original spec"
- F14: settled | Demotion on 4 losses or ≤50%, level drops one tier | 4 losses only (deck) | Settled by: rule 5 "written up in Robert''s dynamic difficulty deck and in ZOM-42 itself"; ZOM-303 merged
- F15: settled | Enrage hp 0, per monster | Deck +25% hp, Brian's +50% | Settled by: rule 5 "your monster enrage sheet has the numbers"; Arthur "the blunder part of robert''s tiers deck is old"
- F16: settled | Folder d_96489e1e00a56685625939, one sheet, two tabs | Another folder | Settled by: agenda "One sheet with two tabs, Tickets and Rules in force"; the only "ZM Difficulty" folder
- F17: not a fork | DM top-level reply | Thread reply | Same recipient and content

Platform defects: none.

### FINAL VERDICT: FAIL

Score: 2

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session default effort

Clock: Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Next action: In the injection SQL, add to card rule 5 (lines 56 and 64) what to write for monsters the sheet hasn't copied, and make Leonard's comment (line 66) say whether "ATK" counts as attack power. Then send /injection, /prompt, /hardness, /oe and /rubric again.

Evidence limits: The Evals/Docs PDFs were not re-extracted; Eval 1's restated bands and overrides were applied. Runtime acceptance of the `commenter` share role and the behaviour of the GitHub file-history tools are unverified (declared parameters only). Eval 0 checks A–B were reused from the same-hash 0_injection.md, because this portal never writes the gate manifest. The VarC-Mailman, VarC-Mayor2 and VarC-PartyGirl prefab blobs are cut at 10,240 bytes; findings about them rest on git commit history. Byte-identical SQL rows reuse prior /prompt facts.

Eval version: task-quality-v1

Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e

Reviewed prompt SHA-256: 22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787

Review context SHA-256: 62810c858ba6595aa408366fd3b7ad1ac6134eb60d4244605a83b6538d9834ab

Prompt record SHA-256: 55d5991643857b73e1ad24764033c012ca09ec2fb47224f800a52dd116f5caa2

**Lowest Dimension:** Unique Ground Truth - 2 - The enrage values for Mailman, Mayor2 and PartyGirl (0.8/0.8 vs not copied) and ZOM-271's scope (35 vs 36 tickets) are both left open by the records.

**Summary:** The prompt text is unchanged and still strong. Last round's enrage-value mismatch is fixed, and rule 4's "another" closes the close-order fork. The new "not copied yet" row leaves the Rules in force contents for three monsters unsettled, and the deep recheck found that "ATK POWER" on ZOM-271 leaves the ticket count open. Two small SQL text edits fix both.
