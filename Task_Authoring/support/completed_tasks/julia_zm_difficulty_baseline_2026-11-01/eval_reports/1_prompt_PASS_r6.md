## PROMPT EVALUATION REPORT

### Task: Julia delegates Leonard's ZM difficulty baseline: build the register (Tickets + Rules in force) from the Trello card rules, its "Before Monday" checklist and Leonard's DM thread, file it in ZM Difficulty, share it with the Monday invite, comment on tickets per rule 6 as changed, reply to Leonard in the DM with counts and keys
### Assigned Persona: Julia Lawson - Product Manager (roster `julia_lawson`, julia.lawson@harmonygames.co)
### Assigned Business Function: Product
### Assigned Competency: Engineering Ops
### Assigned Task Skill: Retrieval
### Assigned Horizon: long-horizon (Task Type field; Difficulty Mode "medium" recorded as context)

Review: `/prompt`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode. Actual review date 2026-10-30. Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe `Universe_SynthCut` (hg4-synth-sep30cut v16), manifest sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`. Eval release task-quality-v1 (manifest `0040c6a5…9c2e`, verified with `hg_eval_release.py snapshot prompt`). Check record: prompt sha256 `22f26066…1787`, review context `0e910489…6516`.

Inputs:
- `04_Prompt.txt`: revision 18, 525 bytes, sha256 `22f26066…1787`. Attached as `04_Prompt (6).txt`; byte-identical to revision 15 (last /prompt round, PASS 5).
- `00_Task_Assigned_Inputs.md`: all five fields stated, which clears intake.
- `01_Universe_Inject.sql`: revision 17, 88,468 bytes, sha256 `10c1ee9238d42bf41259cdb6afdeb728f93246abd2ab65f56275d75b4cf3ce18`. Changed since the last /prompt round (revision 14, `a58a5d1e…958a3`). The changes are new instructions from Leonard:
  - **DM thread reply (new, 2025-09-30T20:07:18Z, Leonard in D05HB64NMQU):** "forgot one thing: leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays. and in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase". The parent DM's thread counters are updated to match.
  - **"Before Monday" checklist on card #80 (new, addChecklistToCard 2025-09-30T16:20:11Z, Leonard):** "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds" and "rule 7 change: Brian gets edit as well, he''ll fix rows during the session". Both items are `incomplete`. The card badge and dateLastActivity are updated to match.
  - Every other row is byte-identical (Eval 0 range diff).
- No error/async config, dynamic context or reference files were supplied, and the prompt references none.
- Evidence contract `stage-evidence-v1`. **Reused:** prior `1_prompt.md` facts for byte-identical SQL rows and base records (card description and comment, enrage sheet, Blake's mails, invite, folder, agenda, deck, Linear, GitHub code). **NEW:** everything that depends on the thread reply and the checklist: scope, statuses after the exclusion, the comment set, share roles, DM reply content, forks L–N, and the B–K recomputation.
- Line numbers: the report text uses physical (`\n`) SQL lines, as Eval 0 does. The generated UGT section uses the check helper's numbering, which also splits on bare `\r` inside Gmail bodies, so rows after line 78 show higher numbers there (for example the invite is physical line 112, helper line 182).

**What this round changes.** The prompt is the same, but the answer it leads to is not. Under revision 17 the end state is 29 tickets instead of 35, 14 Linear comments instead of 2, Brian Foster as editor instead of commenter, and a DM reply that also lists 12 ticket keys.

---

### Injection Gate
- **State:** NEVER_REVIEWED. The gate reads `reports/input_manifest.json`, which this portal's writer never creates.
- **Eval 0 handling:** `0_injection.md` (injection-static-v2, today) reviews the identical SQL hash `10c1ee92…ce18` (revision 17): **FINAL VERDICT: PASS**, COMPLETE. I re-ran `hg_injection_lint.py` (injection-lint-v1) on the same hash: 163 INSERT, 1 UPDATE, 0 FAIL / 0 CHECK / 0 INFO. Static checks A–B are REUSED; the Check C items this prompt depends on were redone here (Phase 3.2).
- **Reviewed SQL sha256:** `10c1ee9238d42bf41259cdb6afdeb728f93246abd2ab65f56275d75b4cf3ce18`. Eval 0 verdict: PASS.
- **Eval 0 findings on records this prompt depends on:** none at fail level. Eval 0's "possible solver ambiguity" note (ZOM-378 has "tutorial" in its title) is tested here as UGT fork M and excluded.
- **Advisories carried:** A1/A2 (`linear_comments.sequence`, gslides `notes`/`table_json`/`ordinal` absent from the unverified schema snapshot); injected Trello actions omit base `_id` fields. None changes a graded value.

---

### Phase 0: Sources read

Docs and references read: Eval 1 in full; `prompt_rubric_reliability.md` release binding; `deep_recheck.md`; `common_errors.md`; `acl.md`; `roster.json`; tool catalog (Slack, Trello, Drive, Linear entries re-read for the new paths). The PDFs in `Evals/Docs` were not re-extracted; Eval 1's inline bands and Local Overrides were applied (evidence limit, unchanged from prior rounds).

Universe exploration (synth-cut base plus SQL overlay), NEW this round:
- **Instruction layers, in time order:** card description (updateCard 14:04:31Z) → Leonard's card comment adding written-out attack power, "rest of the card stands." (15:41:55Z) → "Before Monday" checklist changing rules 6 and 7 (16:20:11Z) → Leonard's DM asking for the baseline and pointing to the card (19:48:26Z) → his thread reply leaving six tickets off and asking for keys (20:07:18Z). All are Leonard's, all before the clock.
- **Discovery paths:** the parent DM shows `reply_count` 1, and the thread is readable with `slack_conversations_replies` / `slack_read_thread`. The card badge shows `checkItems` 2, and the checklist is readable with `trello_get_card`, `trello_get_checklist` or `trello_get_checklists_on_board`.
- **The six excluded tickets** (base Linear, all created before Aug 31, all in rule-1 scope and all Live in the earlier derivation): ZOM-30 "Need to track average blunder … analytics" (labels Improvement, Analytics), ZOM-49 "Add Blunder Count by Level to Analytics", ZOM-50 "Track player skill tier in the left_level event", ZOM-161 "Add difficulty tier assignment for left level event" (Analytics), ZOM-262 "Tutorial for Blunder Locked User", ZOM-275 "Update FTUE message to reflect Blunder mechanic 2.0 changes".
- **Title scan of the 29 kept tickets** for analytics, tutorial, FTUE, track, event and instrument: only ZOM-378 "Level 1 is removed and creates tutorial order problems". ZOM-162 and ZOM-221 match "track" only as monster tracks. ZOM-378 is in scope through Blake's note "tiers: closing. level 1 is back in the list so the first levels line up with their tier versions again".
- **Invite attendees** (Julia's copy, physical line 112): leonard.hayes@ (organizer), julia.lawson@, robert@, arthur.blake@, brian.foster@. "Brian" in the checklist can only be Brian Foster.

Status derivation (shows solvability, not a golden answer; earlier statuses REUSED from byte-identical rows, exclusion NEW):
- **Live 16:** ZOM-23, 42, 45, 199, 221, 246, 258, 263, 274, 282, 288, 295, 300, 303, 305, 378.
- **Editor only 9:** ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315.
- **Replaced 1:** ZOM-254, replaced by ZOM-282.
- **Not shipped 3:** ZOM-202, 280, 293.
- **Total 29** = 35 rule-1 tickets minus ZOM-30, 49, 50, 161, 262, 275.
- **Comments (14):** ZOM-199 (what the build does: cpm > 90), ZOM-254 (replaced by ZOM-282), and the 12 Editor only and Not shipped tickets (the change isn't in the store builds).
- **Shares:** robert@ and brian.foster@ can edit; leonard.hayes@ and arthur.blake@ can comment.
- **DM reply:** total 29, the four status counts, and the keys of the 3 Not shipped and 9 Editor only tickets.

---

### Requirement ledger

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Find Leonard's Tuesday DM ask, including his thread reply | SQL lines 44 and 50 (D05HB64NMQU, 19:48:26Z and 20:07:18Z) | Slack DM history; thread via reply_count 1 | `slack_conversations_history`, `slack_conversations_replies` / `slack_read_thread`, search | Julia is a DM member | The ask: register; six tickets off; reply with total, per-status counts, and the Not shipped and Editor only keys |
| "everything it points to": card rules | Card #80 (line 58), updateCard (66), commentCard (68), checklist and items (70–76) | DM names "the difficulty baseline card on the zm roadmap board" | `trello_get_cards_on_board`, `trello_get_card`, `trello_get_comments`, `trello_get_checklist` | Trello unscoped | Rules 1–7, the attack-power addendum, and the rule 6 and rule 7 changes |
| Ticket scope | Linear ZOM issues; "tiers:" comments; Trello comment; DM thread reply | Linear search/list; per-ticket comments | Linear search/get, `linear_list_comments` | Unscoped | 29 tickets (35 rule-1 tickets minus the six named) |
| Status per ticket (rules 3–4) | Blake's mail and reply; Linear states and closing notes; GitHub | Gmail search; Linear; GitHub | Gmail read; Linear; GitHub reads | Julia's mailbox; unscoped | Live 16 / Editor only 9 / Replaced 1 / Not shipped 3 |
| Rules in force tab (rule 5) | Deck, ZOM-42, Blake's reply, enrage sheet Live tab, code | GSlides, Linear, Gmail, GSheets, GitHub | `gslides_get_presentation_text`, `gsheets_values_batch_get`, `github_get_file_contents` | Deck shared; sheet owned by Julia; GitHub unscoped | Unchanged from last round (starting tier, promotion, demotion with both rules, enrage Live tab as it stands) |
| Build the register: one sheet, tabs Tickets + Rules in force | Agenda doc; card rule 2 | GDocs | `gsheets_create_spreadsheet`, `gsheets_batch_update`, `gsheets_values_update` | Write (ACL-free) | New spreadsheet |
| Put it in the ZM Difficulty folder | Prompt; card rule 7 | Drive folder d_96489e1e00a56685625939 | `gdrive_move_file` (or create with parent) | Julia is writer | File in folder |
| Share with everyone on Monday's invite | Prompt; card rule 7 as changed by the checklist | GCal event on Julia's calendar | `gdrive_share_file` (role param) | Julia's own calendar | robert@ and brian.foster@ writer; leonard.hayes@ and arthur.blake@ commenter |
| Ticket comments (rule 6 as changed) | Card rule 6; checklist item; Blake's reply; rule 4 | Linear | `linear_create_comment` | Write | ZOM-199, ZOM-254 and the 12 Editor only and Not shipped tickets |
| Reply to Leonard in the DM | DM and thread reply | Slack | `slack_send_message` | Write | Total 29, per-status counts, Not shipped and Editor only keys |

Output capability: spreadsheet/tab creation, moving into the folder, sharing, Linear comments and the Slack reply are SUPPORTED by declared catalog tools. The `commenter` role is a free-string parameter with no base example; runtime acceptance UNVERIFIED (evidence limit, not a failure).

---

### Phase 1: Prompt Structure & Persona (prompt text byte-identical; re-judged against the new sources)

**Persona:** PASS (5). The prompt matches the exact roster entry. It is a CEO-to-PM delegation; the card says "Julia owns this one", and Julia owns the enrage sheet.

**Assigned Competency:** PASS (5). Engineering Ops: reconciling tickets with what shipped in store builds, PR/code checks, and now 14 ticket comments.

**Assigned Task Skill:** PASS (5). Retrieval is the core work: every in-scope ticket, state, shipped status and rule value, across six services, with two late instruction layers to find.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS. Data seeding PASS.
- **Dynamic Change (stronger this round):** the checklist changes two card rules after Leonard wrote "rest of the card stands", and the thread reply narrows the scope after the DM. A path that reads only the card description and the top-level DM hits the old rules first.
- **Superseded sources:** the deck's "90 or more" vs Blake's "cpm > 90"; the deck's blunder slide vs Arthur's Slack.
- **Decoys:** Brian's "+50% … every monster" and "the editor bits too"; Domino card #211; the "Next pass" tab; Vincent's channel request.

**Naturalness:** PASS. First person, lowercase and casual, with no document formatting, polished connectives or enumerated specs.

**Anti-Patterns:**
| Pattern | Status |
|---------|--------|
| Command List | PASS. One lowercase "then" with no first/finally, and the order is Leonard's own condition (deep recheck P4 DR1, rejected) |
| Bolt-On | PASS. Every sentence serves the baseline |
| Pre-Solving | PASS. No counts, tickets, statuses, exclusions or causes named |
| Tool Mention | PASS. "dm", "folder", "invite" and "tickets" are natural nouns |

**Diversity:** a two-tab sheet, folder placement, role-based sharing, a 14-ticket Linear comment batch and a DM reply over a 29-ticket cohort.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** PASS (5). The new layers add three forks; quoted records exclude all three. Forks B–K are recomputed on the 29-ticket list and stay excluded.

### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: Every fork tested resolves to one end state. SQL revision 17 adds two instruction layers: Leonard's 16:20 'Before Monday' checklist on card \#80 (rule 6 change: Editor only and Not shipped tickets also get a not-in-the-store-builds comment; rule 7 change: Brian edits too) and his 20:07 DM thread reply (six analytics/tutorial tickets off; reply lists the Not shipped and Editor only keys). L (checklist not in force) is excluded by the later same-author change to the same rules; M (ZOM-378 off as tutorial) by the explicit key list and Blake's tiers: note; N (editor tooling off) by Leonard's request for the editor only keys. B to K stay excluded on byte-identical rules and records, recomputed on the 29-ticket list.

Alternative selection: B to K are every fork from earlier rounds, recomputed for the revision-17 overlay (card description, comment, sheet, mail, Linear and code rows are byte-identical). L, M and N are new forks from the two new instruction layers: L is the strongest because the card description still literally says Not shipped and Editor only tickets stay as they are and that only Robert edits, and the checklist items are unchecked. M tests the one in-scope ticket outside Leonard's list with 'tutorial' in its title (a title scan of the 29 for analytics, tutorial, FTUE, track, event and instrument finds only ZOM-378; ZOM-162 and ZOM-221 match 'track' only as monster tracks); N tests applying his reason clause beyond the list.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Follow the card as Leonard left it, his checklist and his DM thread: scope is every difficulty ticket created up to Aug 31, attack power counting only when written out (ZOM-271 out), minus the six analytics and tutorial tickets his DM reply lists; Replaced only where another ticket's closing note says so (ZOM-282 on ZOM-254); comments on ZOM-199 (flagged by Blake's reply), on Replaced ZOM-254 and, per the checklist's rule 6 change, on every Editor only and Not shipped ticket; share with the invite attendees, Robert and Brian as editors; the Rules in force tab copies the enrage sheet's Live tab as it stands; the DM reply gives the total, per-status counts and the Not shipped and Editor only keys. | 29 tickets (six analytics/tutorial tickets off, ZOM-378 on); ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Brian and Robert edit. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 29 rows: the 35 rule-1 tickets (31 title matches without Duplicates ZOM-203 and ZOM-276, plus tiers: tickets ZOM-221, 300, 305, 378) minus the six Leonard leaves off (ZOM-30, 49, 50, 161, 262, 275); Live 16, Editor only 9, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab, copied as it stands: nine monster rows and MonsterBase 0.8/0.8 with their numbers, and Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP) as not copied yet; DM gives the total 29, the per-status counts and the keys of the Not shipped (ZOM-202, 280, 293) and Editor only (ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315) tickets. | CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 296-296): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; SHEET\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 22-22): "\["MonsterBase (base prefab)", "0.8", "0.8", "0"\], \["Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)", "not copied yet", "not copied yet", "0"\]"; TCOMMENT\_W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 68-68): "written out (ATK on its own doesn''t)"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 72-72): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 74-74): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them." |
| B | match3d\#401 changed how enrage works (speed and damage split per monster, hp method dropped), so ZOM-282 is Replaced by match3d\#401 and gets a Replaced comment. | ZOM-282 Replaced by match3d\#401. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a Replaced comment on ZOM-282 naming match3d\#401. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-282. | Register shows ZOM-282 Replaced; DM counts Live 15, Replaced 2. | GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 191-191): "this gives enrage speed and damage their own values, they shared one since ZOM-282." |
| C | Comment on every listed ticket whose text the store builds contradict, including ZOM-42 (6-7 levels vs 10). | Correction comment also on ZOM-42. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a comment on ZOM-42. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-42. | Extra correction comment; register unchanged. | Z42A (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "gets assigned after the first 6-7 levels based on CPM" |
| D | Read the scope window in Pacific days with an Apr 21 start, dropping ZOM-23 (2025-04-21T04:51:38Z, Apr 20 PT); ZOM-30 is already off under Leonard's DM reply. | 28 tickets; ZOM-23 out. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Register 28 rows; DM total 28 and Live 15. | Z23 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3277): "2025-04-21T04:51:38Z" |
| E | Also post the register in \#zombie-design because Vincent asked Julia to drop it there. | Share with the invite and also post in \#zombie-design. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a Slack post in \#zombie-design. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus C090N54TG79. | Same register; extra channel post. | VINCENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "julia when you have the difficulty list can you drop it in here too" |
| F | ZOM-277 (created after ZOM-250) changed how ZOM-250's average attack power works, so ZOM-250 is Replaced by ZOM-277 and gets a Replaced comment. | ZOM-250 Replaced by ZOM-277. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a Replaced comment on ZOM-250 naming ZOM-277. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Register shows ZOM-250 Replaced; DM counts Editor only 8, Replaced 2; ZOM-250 drops out of the Editor only keys. | Z250 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3300): "(This is per set of items)"; Z277 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3329): "The average power should really be 334 / 5 uniques" |
| G | ZOM-254 was closed (2025-06-23) after ZOM-282 (2025-06-21) and its own QA note says blunder enrages the monsters, so ZOM-282 is not the 'later' ticket and ZOM-254 stays Live with no Replaced comment. | ZOM-254 Live; no Replaced ticket. | Same as A without the ZOM-254 comment. | Same as A without Linear ZOM-254. | Register shows ZOM-254 Live; DM counts Live 17, Replaced 0. | Z254C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 274-274): "checked on the dev build, blunder enrages the monsters on the board now" |
| H | Rule 5 asks for enrage as it works in the store builds today, so the three monsters the sheet has not copied are given what they actually run on in main: no own override, so MonsterBase's 0.8 speed / 0.8 damage. | 29 tickets (six analytics/tutorial tickets off, ZOM-378 on); ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Brian and Robert edit. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same 29 rows and counts as A; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab, with Mailman, Mayor2 and PartyGirl given 0.8 speed / 0.8 damage (MonsterBase) instead of not copied yet; DM as A. | CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; MB\_ENRAGE (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/MonsterBase.prefab lines 342-343): "enrageSpeedPercentage: 0.8" |
| I | Fill the gap from the VarC prefabs the History tab says the Live tab was copied from: VarC-PartyGirl carries enragePercentage 0.6, so PartyGirl is 0.6 speed / 0.6 damage; Mailman and Mayor2 show no enrage value in their prefab text. | 29 tickets (six analytics/tutorial tickets off, ZOM-378 on); ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Brian and Robert edit. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same 29 rows and counts as A; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab, with PartyGirl at 0.6 / 0.6 and Mailman and Mayor2 without numbers; DM as A. | SHEET\_HIST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 26-26): "\["2025-09-08", "Live tab copied from the VarC prefabs in main", "Julia"\]"; PG\_PREFAB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/VarC-PartyGirl.prefab lines 215-216): "propertyPath: enragePercentage" |
| J | Leonard's comment adds attack power in the title; ZOM-271's title says 'ATK POWER' / 'ATK Power', and 'ATK on its own' is read as ATK without 'power', so ZOM-271 (Done, June 16, card-profile stat display) is in scope as Live. | 30 tickets; ZOM-271 Live; otherwise as A. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 30 rows (adds ZOM-271); Live 17, Editor only 9, Replaced 1, Not shipped 3; DM total 30 and Live 17. | TCOMMENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 68-68): "attack power in the title counts too"; Z271 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3323): "Comprehensive Item Stat Display Rules also ATK POWER BUG. Also Change Damage sort to ATK Power sort" |
| K | Take the starting-tier window from the written rules the card names: average CPM over the player's first 10 levels (ten distinct levels), &gt; 90 to tier 1, the rest tier 0. | 29 tickets (six analytics/tutorial tickets off, ZOM-378 on); ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Brian and Robert edit. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register and counts as A; Rules in force gives the starting tier as average CPM over the first 10 distinct levels &gt; 90 to tier 1, instead of the first 10 games played (wins and losses) as the build counts them. | Z42S (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "1st 10 level avg CPM &gt; 90 (top 20%) moves to tier 1, rest stays in tier 0)" |
| L | The 'Before Monday' checklist items are unchecked, so they are Leonard's pending notes, not rules in force; card rules 6 and 7 as written stand: comments only on ZOM-199 and ZOM-254, with the Not shipped and Editor only tickets left as they are, and only Robert edits. | Checklist not applied: two comments; Brian comments only. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 and ZOM-254 only; reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. | Same 29 rows and counts; no comments on the twelve Editor only and Not shipped tickets; brian.foster@ as commenter. | CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CL\_NAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 70-70): "'Before Monday', '68daca5871dba40417a00383'" |
| M | ZOM-378 'Level 1 is removed and creates tutorial order problems' is a tutorial ticket, so it goes off the list with the other analytics and tutorial tickets Leonard named. | 28 tickets; ZOM-378 off. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 28 rows; Live 15; DM total 28 and Live 15. | DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3440): "It creates other important issues like wrong tutorials at the wrong spot." |
| N | Leonard's reason 'they don't change how hard a level plays' is the test, so every ticket that only touches editor or debug tooling is left off too (ZOM-162, 163, 173, 200, 201, 202, 250, 277, 312, 315), with no comments on them. | Editor-tooling tickets off the list; no comments on them. | As A without the comments on the editor-tooling tickets. | As A without those Linear tickets. | About 19 rows; no Editor only rows; DM without Editor only keys. | DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 85-85): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not." |

Explicit option inventory: The prompt lists no options; the status values sit in the incorporated card.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "build the register the way he set it up"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: EXCLUDED. Card rule 4 now makes a ticket Replaced only when another ticket's closing note says so and says PRs that change or split its numbers don't. match3d\#401 is a PR, and its comment describes a split of the shared value, not a replacement.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 191-191): "this gives enrage speed and damage their own values, they shared one since ZOM-282."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Live vs Replaced for ZOM-282. |
| writes | DIFFERENT | B adds a ZOM-282 comment. |
| destinations | DIFFERENT | B adds ZOM-282. |
| contents | DIFFERENT | Status cell and DM counts differ (Live 15 / Replaced 2). |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The quoted sentences exclude PRs and value splits by name; \#401's comment says it gives speed and damage their own values.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 191-191): "this gives enrage speed and damage their own values, they shared one since ZOM-282."

Compared alternative: C
Resolution: EXCLUDED. Card rule 6 limits Blake-sourced comments to tickets his mail or reply calls wrong (only ZOM-199 in the reply), and says ZOM-42 stays as it is even if its wording is a bit off; the checklist's rule 6 change adds only Editor only and Not shipped tickets, and ZOM-42 is Live.
Resolution evidence: CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 129-129): "ZOM-199 says &gt;= but the code never changed from the original spec"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 72-72): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | C decides ZOM-42 needs a comment. |
| writes | DIFFERENT | C adds one comment. |
| destinations | DIFFERENT | C adds ZOM-42. |
| contents | DIFFERENT | Extra comment text. |

Authority chain: P → DMR → CARD\_R6X

Resolution relevance challenge: The quoted sentences name ZOM-42 as staying as it is; the checklist change covers Editor only and Not shipped tickets, which ZOM-42 (Live) is not; the reply names only ZOM-199.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 129-129): "ZOM-199 says &gt;= but the code never changed from the original spec"

Compared alternative: D
Resolution: EXCLUDED. The scope has no start date (everything since ZM started), so ZOM-23 is in under any timezone; the next title match after Aug 31 is ZOM-517 on 2025-09-03.
Resolution evidence: CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; Z517 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3591): "2025-09-03T22:22:22Z"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | D drops ZOM-23. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rows and counts differ by one. |

Authority chain: P → DMR → CARD\_SCOPE

Resolution relevance challenge: The quoted scope removes the start-date edge; Z517 shows no ticket near the Aug 31 end.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; Z517 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3591): "2025-09-03T22:22:22Z"

Compared alternative: E
Resolution: EXCLUDED. The prompt and card both define the audience as the invite list; Vincent is not an attendee and his channel request is not part of Leonard's ask.
Resolution evidence: CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system before monday's tuning session. can you take it off my plate? go through his ask and everything it points to and build the register the way he set it up. put it in the zm difficulty folder and share it with everyone on monday's tuning invite. if his rules say something needs to happen on the tickets, go ahead and do that too. then reply to leonard in the dm with what he asked for. go with your read on the details, no need to check with me first"; CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 182-182): "VALUES ('evt\_91674a9c23d012a9ac34da', 'julia.lawson@harmonygames.co', 'ZM difficulty tuning'"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | E adds a channel post. |
| writes | DIFFERENT | E adds a Slack post. |
| destinations | DIFFERENT | E adds \#zombie-design. |
| contents | DIFFERENT | Extra post. |

Authority chain: P → DMR → CARD\_R7

Resolution relevance challenge: The prompt names the audience as the invite; the invite on Julia's calendar does not include Vincent.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system before monday's tuning session. can you take it off my plate? go through his ask and everything it points to and build the register the way he set it up. put it in the zm difficulty folder and share it with everyone on monday's tuning invite. if his rules say something needs to happen on the tickets, go ahead and do that too. then reply to leonard in the dm with what he asked for. go with your read on the details, no need to check with me first"; CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 182-182): "VALUES ('evt\_91674a9c23d012a9ac34da', 'julia.lawson@harmonygames.co', 'ZM difficulty tuning'"

Compared alternative: F
Resolution: EXCLUDED. Rule 4 now requires another ticket's closing note saying it replaces this one; ZOM-277's closing note says nothing changes in the game and names no replacement, and rule 4 says a ticket players never had stays Editor only.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; Z277C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 288-288): "this is the average in the editor''s stats panel, nothing changes in the game itself"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Editor only vs Replaced for ZOM-250. |
| writes | DIFFERENT | F replaces ZOM-250's not-in-the-store-builds comment with a Replaced comment. |
| destinations | SAME | ZOM-250 gets a comment under both readings. |
| contents | DIFFERENT | Status, DM counts and the ZOM-250 comment text differ. |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The quoted rule removes formula changes as a Replaced trigger and ranks Editor only over Replaced for tickets players never had; ZOM-277's closing note has no replace wording.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; Z277C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 288-288): "this is the average in the editor''s stats panel, nothing changes in the game itself"

Compared alternative: G
Resolution: EXCLUDED. Rule 4 now keys on another ticket's closing note, with no ordering condition. ZOM-282's closing note says it replaces the blunder 2.0 boost from ZOM-254; ZOM-254's QA note describes the dev build and is not a closing note on another ticket that replaces it. Close order no longer matters.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 296-296): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Replaced vs Live for ZOM-254. |
| writes | DIFFERENT | G drops the ZOM-254 comment. |
| destinations | DIFFERENT | G drops Linear ZOM-254. |
| contents | DIFFERENT | Status and DM counts differ (Live 17 / Replaced 0). |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The rule no longer says 'later', so close dates cannot reverse it; ZOM-282's note names ZOM-254 explicitly, which is what the rule asks for.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 296-296): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"

Compared alternative: H
Resolution: EXCLUDED. Rule 5 now says how to fill the enrage section: copy the sheet's Live tab as it stands, put a monster the sheet has not copied on the tab as not copied yet, and do not work numbers out from anywhere else. Deriving 0.8/0.8 for Mailman, Mayor2 and PartyGirl from MonsterBase inheritance in the repo is working numbers out from somewhere else. The later, more specific sentence in the same rule governs the store-builds clause for these rows; the copied numeric rows equal main (Eval 0 Check C), so the two clauses no longer pull apart.
Resolution evidence: CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; SHEET\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 22-22): "\["MonsterBase (base prefab)", "0.8", "0.8", "0"\], \["Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)", "not copied yet", "not copied yet", "0"\]"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and share list. |
| writes | SAME | Same spreadsheet, shares, Linear comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | Rules in force tab: three monsters as not copied yet (A) vs 0.8/0.8 (H). |

Authority chain: P → DMR → CARD\_R5C

Resolution relevance challenge: Not a strawman: H was the leading reading last round, and 'as they work in the store builds today' still sits in rule 5. The new sentence speaks to exactly this case, a monster the sheet hasn't copied, and names the required entry ('not copied yet') and forbids the derivation H needs.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."

Compared alternative: I
Resolution: EXCLUDED. Rule 5 says to copy the Live tab as it stands and not to work numbers out from anywhere else, so reading PartyGirl's old enragePercentage 0.6 out of its prefab is excluded; the code also no longer reads that field (Monster.cs declares only enrageSpeedPercentage and enrageDamagePercentage).
Resolution evidence: CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; MONSTER\_CS (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Monster/Monster.cs lines 87-88): "\[SerializeField\] private float enrageSpeedPercentage = 0.25f;"; PG\_PREFAB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/VarC-PartyGirl.prefab lines 215-216): "propertyPath: enragePercentage"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and share list. |
| writes | SAME | Same spreadsheet, shares, Linear comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | PartyGirl 0.6/0.6 vs not copied yet. |

Authority chain: P → DMR → CARD\_R5C

Resolution relevance challenge: The new rule 5 sentence forbids taking numbers from anywhere but the Live tab, which covers prefab text; the dead field is a second, independent reason.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted.
Challenge evidence: CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; MONSTER\_CS (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Monster/Monster.cs lines 87-88): "\[SerializeField\] private float enrageSpeedPercentage = 0.25f;"

Compared alternative: J
Resolution: EXCLUDED. Leonard's card comment now says attack power counts only when written out in the title and that ATK on its own doesn't. ZOM-271's title never spells out 'attack power'; it uses the abbreviation 'ATK POWER' / 'ATK Power'. 'Written out' sets the test (the words spelled in full), and the parenthetical names the abbreviation as what fails it, so ZOM-271 stays out. Every other ZOM title created up to Aug 31 with ATK or attack was checked: ZOM-246, 250, 263, 277 and 315 spell out 'attack power'; ZOM-21 ('Monster Attack Speed') has no 'attack power'.
Resolution evidence: TCOMMENT\_W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 68-68): "written out (ATK on its own doesn''t)"; Z271 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3323): "Comprehensive Item Stat Display Rules also ATK POWER BUG. Also Change Damage sort to ATK Power sort"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-271 out vs in (Live). |
| writes | SAME | Same spreadsheet, comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | One more register row; DM total 30 vs 29 and Live 17 vs 16. |

Authority chain: P → DMR → TCOMMENT\_W

Resolution relevance challenge: Not a strawman: ATK is the game's short form and ZOM-271 also says ATK POWER, so a reader could take 'ATK on its own' as 'ATK without power'. But 'written out' is the governing test and 'ATK POWER' is not attack power written out; the parenthetical illustrates the abbreviation failing that test rather than creating a second, looser one.
Delegation challenge: NOT_CLAIMED. No alternative scope is authorized.
Challenge evidence: TCOMMENT\_W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 68-68): "written out (ATK on its own doesn''t)"

Compared alternative: K
Resolution: EXCLUDED. Deep recheck P1 DR1. Rule 5 asks for the tier rules as they work in the store builds today; the deck and ZOM-42 are where they are written up. The build buckets a player when total games reach 10, and total games are wins plus losses, so the window is the first 10 games played. This is the same rule 5 clause that makes cpm &gt; 90 beat the written '&gt;= 90'. ZOM-42 itself calls the same plays 'attempts' and 'games' elsewhere, so 'first 10 levels' read as level plays is the same answer; only the reading 'ten distinct levels' differs, and the build clause excludes it.
Resolution evidence: CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; WH\_GAMES (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 147-147): "return GetTotalWins() + GetTotalLosses();"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and share list. |
| writes | SAME | Same spreadsheet, shares, Linear comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | Starting-tier window: first 10 games played (A) vs first 10 distinct levels (K). |

Authority chain: P → DMR → CARD\_R5B

Resolution relevance challenge: Not a strawman: three records (deck, ZOM-42, ZOM-199) say 'first 10 level(s)'. The card's own criterion is how the rules work in the store builds, and the build code fixes the unit as games, wins and losses.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied.
Challenge evidence: CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; WH\_GAMES (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 147-147): "return GetTotalWins() + GetTotalLosses();"

Compared alternative: L
Resolution: EXCLUDED. The checklist is Leonard's later change to the same two rules on the same card: its items are labelled 'rule 6 change' and 'rule 7 change', stated as decisions with a reason ('he''ll fix rows during the session'), and were added at 16:20, after his 14:04 description update and his 15:41 'rest of the card stands' comment. Under Eval 1 §2.1 check 1 a later applicable update by the same author for the same issue and scope resolves the earlier sentence without announcing replacement. Leonard's 19:48 DM points to the card (which carries the checklist) and his 20:07 reply asks for the Not shipped and Editor only keys. An unchecked item is a to-do for the card owner ('Julia owns this one'), not a hedge; no record says the changes are pending or tentative.
Resolution evidence: CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 72-72): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 74-74): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; CL\_ACT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 76-76): "'addChecklistToCard', '2025-09-30T16:20:11Z'"; UPD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 66-66): "'updateCard', '2025-09-30T14:04:31Z'"; DMR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 44-44): "the rules for the register are on the difficulty baseline card on the zm roadmap board"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Whether the checklist changes apply. |
| writes | DIFFERENT | L posts 2 Linear comments instead of 14 and shares Brian as commenter instead of editor. |
| destinations | DIFFERENT | L drops the twelve Editor only and Not shipped tickets. |
| contents | DIFFERENT | Brian's role differs. |

Authority chain: P → DMR → CL\_R6

Resolution relevance challenge: Not a strawman: the card description still literally says the Not shipped and Editor only tickets stay as they are and that everyone but Robert comments, and the items are unchecked. The quoted items name the exact rules they change and say what now happens; they post-date both the description and Leonard's 'rest of the card stands' comment, and come from the same author on the same card.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the later card change is applied.
Challenge evidence: CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 72-72): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; TCOMMENT\_S (Evals/task\_inputs/01\_Universe\_Inject.sql lines 68-68): "rest of the card stands."; CL\_ACT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 76-76): "'addChecklistToCard', '2025-09-30T16:20:11Z'"

Compared alternative: M
Resolution: EXCLUDED. Leonard's exclusion names its tickets in parentheses (30, 49, 50, 161, 262 and 275) and ZOM-378 is not among them. ZOM-378 is in scope as one of Blake's tier tickets, and his closing note says the fix lines the first levels up with their tier versions, which changes how hard those levels play, so Leonard's reason does not reach it either.
Resolution evidence: DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 364-364): "tiers: closing. level 1 is back in the list so the first levels line up with their tier versions again"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-378 on vs off. |
| writes | SAME | ZOM-378 is Live and gets no comment either way. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | One row fewer; DM total 28 and Live 15. |

Authority chain: P → DMX

Resolution relevance challenge: Not a strawman: ZOM-378's title says 'tutorial order problems' and its description is about tutorials. But the DM gives an explicit list, and the tiers: note quoted ties ZOM-378 to tier level versions, which is difficulty.
Delegation challenge: NOT_CLAIMED. No alternative scope is authorized.
Challenge evidence: DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 364-364): "tiers: closing. level 1 is back in the list so the first levels line up with their tier versions again"

Compared alternative: N
Resolution: EXCLUDED. The exclusion is scoped to 'the analytics and tutorial tickets' with their keys listed, and in the same message Leonard asks for the keys of the editor only ones, which only makes sense if they stay on the list; the checklist's rule 6 change also has Editor only tickets commented, and card rule 3 lists Editor only as a status.
Resolution evidence: DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 72-72): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Editor-tooling tickets off vs on. |
| writes | DIFFERENT | N drops their comments. |
| destinations | DIFFERENT | N drops those Linear tickets. |
| contents | DIFFERENT | Rows, counts and DM keys differ. |

Authority chain: P → DMK

Resolution relevance challenge: The reason clause explains the listed tickets; the same message asks for editor only keys, which rules out dropping them.
Delegation challenge: NOT_CLAIMED. No alternative scope is authorized.
Challenge evidence: DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"

Strongest-alternative challenge (L): L keeps the card description's literal rules 6 and 7 and reads the unchecked checklist as pending; it is excluded only because the checklist items, by the same author, later, on the same card, name the rules they change and state the new requirement.
Challenge evidence: CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 72-72): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CL\_ACT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 76-76): "'addChecklistToCard', '2025-09-30T16:20:11Z'"; TCOMMENT\_S (Evals/task\_inputs/01\_Universe\_Inject.sql lines 68-68): "rest of the card stands."

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

**Feasibility:** PASS (5).
- Every ask maps to cataloged tools, and the needed data exists and is tool-visible: card text, checklist items, the DM thread, sheet cells, Linear states and comments, mail, calendar attendees and repo files.
- The comment batch (14 `linear_create_comment` calls) and four shares are ordinary write volume over a source-defined cohort, not padding.

**Persona ACL Reachability:** PASS (5). Every scoped read is visible to Julia:
- DM and its thread: she is a member;
- #zombie-design: member;
- Arthur's mails: her mailbox;
- the invite: her calendar;
- folder: writer;
- agenda doc and deck: reader;
- sheet: owner.

GitHub, Linear and Trello (including the checklist) are unscoped.

**Explicit Tool Mention:** PASS (5).

**Clarity & Specificity:** PASS (5).
- **Write set:** the same under every reading that survives: one spreadsheet in the folder, four shares (two editors, two commenters), 14 Linear comments (rule 6 with the checklist change and rule 4), and one DM reply. Reading L (2 comments, Brian as commenter) would diverge, but the checklist excludes it (UGT above).
- A top-level DM message and a thread reply carry the same content to the same recipient.
- There are no "I'll [verb]" statements.
- **Not a fork:** ticking the two checklist items after doing them. The prompt doesn't ask for it, and it changes no register, comment, share or reply content.

**Contrived / Unnatural:** PASS (5).
- Destination and audience are named the way the persona knows them.
- No staged typos, opaque IDs, exact timestamps, trap hints, riddles, audit wording or if-chains.
- "if his rules say something needs to happen on the tickets" is one conditional whose rule lives on the card. It does not hint at the checklist or the thread reply.

**Alignment with Today's Date:** PASS (5). "tuesday" resolves to 2025-09-30: the DM is at 19:48:26Z (12:48 PT) and the thread reply at 20:07:18Z (13:07 PT). "monday's tuning session/invite" resolves to 2025-10-06T17:00Z (10:00 PT).

**Originality:** N/A (no comparison samples supplied).

**Truthfulness:** PASS (5). Premises PR1–PR5 are verified against revision 17:
- Leonard's Tuesday DM exists;
- the Monday session and its invite exist;
- the ZM Difficulty folder is unique;
- Leonard's rules are on the card the DM names, now with the checklist changes.

**Tool Use & Cross-service:** PASS (5). Each service changes a graded fact:
- **Slack:** the six-ticket exclusion and the reply's key lists.
- **Linear:** the cohort, the states and the Replaced trigger.
- **Trello:** the rules, the attack-power scope, the comment set and Brian's role.
- **Gmail:** shipped vs Editor only, the cpm rule and the ZOM-199 comment.
- **GitHub:** the tier rules as built.
- **Sheets:** enrage.
- **Calendar:** the share list.

Writes span Sheets, Drive, Linear and Slack.

**Investigation + Action:** PASS (5). **Coherence (Bolt-on):** PASS (5). **Business Function:** PASS (5), Product. **Complexity Dimensions & Data Seeding:** PASS (5).

---

### Phase 3: Universe Feasibility

**Data Existence:** PASS (5). Every needed entity is verified and retrievable through cataloged reads, including the thread reply and the checklist.

**Cross-Service Coherence:** PASS (5).
- **New rows (NEW checks):**
  - The thread reply's author (Leonard, EMPLOYEE_0038) is a member of D05HB64NMQU.
  - Its thread_parent_id and thread_ts_legacy point at the 19:48 DM, and the parent's reply_count 1 / reply_users_count 1 / latest_reply match the one reply.
  - The checklist's card and board ids resolve. The card badge (checkItems 2, checked 0) matches two `incomplete` items, and the card's dateLastActivity equals the 16:20:11Z checklist action.
  - Apostrophes are doubled (`don''t`, `isn''t`, `he''ll`).
  - Every new date precedes the clock.
- **Six named tickets:** all exist and fit Leonard's description (analytics/tracking or tutorial/FTUE titles and labels), so the reply doesn't misdescribe a record.
- **Checklist vs card description:** rules 6 and 7 in the description still carry the old wording. The checklist is a later, labelled change by the same author on the same card, and no later record restates the old rules. That is a supported correction, not an inconsistency (Eval 0 Check C agrees).
- **Unchanged rows:** REUSED (byte-identical): in-scope closing notes match states and completion times; ZOM-282 names ZOM-254; Slack authors are channel members.
- **Known base-data issues (not scored):** none touched; the task uses no Snowflake or Confluence data.
- **Not task-touched (not scored):** `Monster.cs` passes a single `enrageDamagePercentage`, and `WinHistory.GetWinRate` reads from index 0. Keep rubric rows off stacking behaviour and the oldest-vs-latest window.
- Injection SQL considered: Yes. Static integrity evidence: REUSED from `0_injection.md` (same hash, checks A–B); task-relevant Check C items redone above.

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|-----------|--------------|-------------|---------------|
| Prompt | Unique Ground Truth | 5 | New forks L, M, N excluded by the checklist items, the explicit key list, the tiers: note and the editor-only request; B–K excluded as before |
| Prompt | Feasibility | 5 | All asks cataloged; data exists |
| Prompt | Persona ACL Reachability | 5 | Every scoped read visible to Julia |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | Same write set under every surviving reading |
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
| Universe | Cross-Service Coherence | 5 | No inconsistency in task-touched data |

---

### Issues Found

None at any severity.

### Recommended Improvements (not scored)

1. **Update the OEs and rubric to revision 17. The old ones no longer match the answer.**
   - **Scope:** 29 tickets. ZOM-30, 49, 50, 161, 262 and 275 are off; ZOM-378 stays on.
   - **Counts:** Live 16, Editor only 9, Replaced 1, Not shipped 3.
   - **Comments:** 14 in total:
     - ZOM-199: the build checks cpm > 90.
     - ZOM-254: replaced by ZOM-282.
     - The 9 Editor only tickets (ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315) and the 3 Not shipped tickets (ZOM-202, 280, 293): the change isn't in the store builds.
     - ZOM-42 still gets none.
   - **Shares:** robert@ and brian.foster@ can edit; leonard.hayes@ and arthur.blake@ can comment.
   - **DM reply:** the total 29, the per-status counts, and the Not shipped and Editor only keys.
2. **Keep the earlier settled forks:**
   - Mailman, Mayor2 and PartyGirl (incl. PartyGirl 50HP) go on the Rules in force tab as not copied yet.
   - ZOM-271 is out.
   - Starting tier is over the first 10 games played. Accept "first 10 levels" unless the answer says losses don't count.
   - Grade demotion on both rules.
3. **Don't grade ticking the checklist items.** The prompt doesn't ask for it.
4. **Optional wording**, carried from last round: "then reply to leonard in the dm…" could follow Leonard's own condition and read "once it's in the folder, reply to leonard in the dm with what he asked for." If you change it, put it in your own voice; prompts are screened for AI-written text. A prompt change outdates every pass that reads the prompt.

---

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 7 sentences, 20 forks | 0 | 0 |
| P2 | 7 sentences | 0 | 0 |
| P3 | 7 sentences | 0 | 0 |
| P4 | 7 sentences | 1 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P4 | "then reply to leonard in the dm with what he asked for." | DM `6f773865…` (SQL line 44) "reply here when it''s in the folder with how many tickets made the list and how many of each status" | common_errors §3 / §6.6 | Command list | REJECTED | §6.6 defines the failure as a "first / then / finally" list, and Eval 1 §1.3.1 asks whether the prompt prescribes a step-by-step procedure. Here there is one lowercase "then", with no first or finally, and the order is Leonard's own condition. P4 itself left the call to the main session. The optional rewording is under Recommended Improvements. |

Effect on verdict: unchanged. No finding was confirmed. P1's independent derivation matches the main review: 29 tickets; Live 16 / Editor only 9 / Replaced 1 / Not shipped 3; 14 comments; Robert and Brian edit. P1 flagged the checklist fork (F1) as the one most at risk. It is recorded as reading L, EXCLUDED, on the quoted check items, the later action date and the same author.

Fork list:
- F1 / L: settled | Checklist in force: 14 comments, Brian edits | Unchecked items are pending: 2 comments, Brian comments | Settled by: check items "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds" and "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; addChecklistToCard 2025-09-30T16:20:11Z, after updateCard 14:04:31Z and the "rest of the card stands." comment 15:41:55Z
- F2 / M: settled | ZOM-378 on (29) | Off as a tutorial ticket (28) | Settled by: DM reply "(30, 49, 50, 161, 262 and 275)"; ZOM-378 note "tiers: closing. level 1 is back in the list so the first levels line up with their tier versions again"
- F3 / N: settled | Only the six listed tickets off | Editor-tooling tickets off too | Settled by: DM reply "put the keys of the not shipped ones and the editor only ones"; check item rule 6 change
- F4 / J: settled | ZOM-271 out (29, Live 16) | In (30, Live 17) | Settled by: Leonard's comment "written out (ATK on its own doesn''t)"
- F5 / H, I: settled | Enrage Live tab as it stands, three monsters not copied yet | MonsterBase 0.8/0.8 or PartyGirl 0.6/0.6 | Settled by: rule 5 "Copy its Live tab as it stands … don''t work numbers out from anywhere else"
- F6 / K: settled | Starting tier over the first 10 games | First 10 distinct levels | Settled by: rule 5 "as they work in the store builds today"; `TierManager.cs` "if (totalGames == 10)"; `WinHistory.cs` "return GetTotalWins() + GetTotalLosses();"
- F7 / G: settled | ZOM-254 Replaced by ZOM-282 | ZOM-254 Live | Settled by: rule 4 "only when another ticket''s closing note says it replaces this one"; ZOM-282 "this replaces the blunder 2.0 boost from ZOM-254"
- F8 / B: settled | ZOM-282 Live | Replaced by match3d#401 | Settled by: rule 4 "PRs that change or split its numbers don''t"
- F9 / F: settled | ZOM-250 Editor only (not-in-the-store-builds comment) | Replaced by ZOM-277 | Settled by: ZOM-277 note "nothing changes in the game itself"; rule 4 "a ticket players never had stays Editor only or Not shipped"
- F10 / C: settled | No comment on ZOM-42 | Correction comment on ZOM-42 | Settled by: rule 6 "Every other ticket stays as it is, ZOM-42 … included"; the checklist change covers only Editor only and Not shipped tickets
- F11 / D: settled | ZOM-23 in | Out under a Pacific Apr 21 start | Settled by: scope "every ZOM ticket created up to Aug 31 (so everything since we started ZM)"; next title match ZOM-517 "2025-09-03T22:22:22Z"
- F12 / E: settled | Share with the invite only | Also post in #zombie-design | Settled by: prompt "share it with everyone on monday's tuning invite"; rule 7
- F13: settled | Editor-only tickets not in the store builds | Brian's "the editor bits too" | Settled by: rule 3 "What is in the store builds and what counts as shipped: Blake''s store builds mail"
- F14: settled | Start tier cpm > 90 | >= 90 | Settled by: Blake's reply "ZOM-199 says >= but the code never changed from the original spec"
- F15: settled | Demotion on 4 losses in a row or ≤50% over up to the last 10, level drops one tier | 4 losses only (deck) | Settled by: rule 5 names the deck and ZOM-42; ZOM-42 "we demote someone when their win rate for up to the last 10 games is 50% or lower"; ZOM-303 merged
- F16: settled | Duplicates ZOM-203, 276 out; "tiers:" tickets ZOM-221, 300, 305, 378 in; open/cancelled ZOM-202, 280, 293 Not shipped | Other scope | Settled by: rule 1
- F17: settled | Card #80, folder d_96489e1e00a56685625939, invite evt_91674a9c23d012a9ac34da | Domino card #211 or another folder | Settled by: DM "the difficulty baseline card on the zm roadmap board"; the only "ZM Difficulty" folder
- F18: not a fork | DM top-level reply | Thread reply | Same recipient and content
- F19: not a fork | Leave the checklist items unticked | Tick them after doing them | Not asked; changes no graded content

Platform defects: none.

### FINAL VERDICT: PASS

Score: 5

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Clock: Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Next action: Send /hardness, then /oe and /rubric. Bring the OEs and rubric in line with revision 17: 29 tickets (six off, ZOM-378 on), Live 16 / Editor only 9 / Replaced 1 / Not shipped 3, 14 ticket comments, Robert and Brian as editors, and the DM reply with counts plus the Not shipped and Editor only keys.

Evidence limits: The Evals/Docs PDFs were not re-extracted; Eval 1's restated bands and overrides were applied. Runtime acceptance of the `commenter` share role is unverified (declared parameters only). Eval 0 checks A–B were reused from the same-hash 0_injection.md, because this portal never writes the gate manifest. Byte-identical SQL rows reuse prior /prompt facts under stage-evidence-v1.

**Lowest Dimension:** None below 5. Every scored dimension is 5.

**Summary:** The prompt is unchanged and still passes on SQL revision 17. Leonard's new checklist (rules 6 and 7 changed) and DM thread reply (six tickets off, keys in the reply) are later instructions from the same author on the sources the prompt incorporates. The three new forks are excluded by quoted records. The answer has moved to 29 tickets, 14 comments and Brian as an editor, so the OEs and rubric must follow it.

Eval version: task-quality-v1

Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e

Reviewed prompt SHA-256: 22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787

Review context SHA-256: 0e91048971428e3bae82083ca9f5beeb114c96cda4af8fbc28c37fbde1cb6516

Prompt record SHA-256: e5218ad639ae2699aa618d6c5ebf4619d90b339f32de4ec1af4616a9e0e65ded
