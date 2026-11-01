## PROMPT EVALUATION REPORT

### Task: Julia delegates Leonard's ZM difficulty baseline: build the register (Tickets + Rules in force) from the Trello card rules, Leonard's card comment, his "notes for monday" doc attached to the card, the "Before Monday" checklist and his DM thread; file it in ZM Difficulty, share it with the Monday invite, comment on tickets per rule 6 as changed, and reply to Leonard in the DM with counts, keys, which ticket replaced which and when a new player gets their starting tier
### Assigned Persona: Julia Lawson - Product Manager (roster `julia_lawson`, julia.lawson@harmonygames.co)
### Assigned Business Function: Product
### Assigned Competency: Engineering Ops
### Assigned Task Skill: Retrieval
### Assigned Horizon: long-horizon (Task Type field; Difficulty Mode "medium" recorded as context)

Review: `/prompt`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode. Actual review date 2026-10-30. Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe `Universe_SynthCut` (hg4-synth-sep30cut v16). Eval release task-quality-v1 (manifest `0040c6a5…9c2e`, verified with `hg_eval_release.py snapshot prompt`). Check record: prompt sha256 `22f26066…1787`, review context `92bcd429…ec3c`, policy prompt-source-checks-v2.

Inputs:
- `04_Prompt.txt`: revision 24 (attached as `04_Prompt (9).txt`), 525 bytes, sha256 `22f26066…1787`. Byte-identical to the prompt graded last round.
- `00_Task_Assigned_Inputs.md`: all five fields stated, which clears intake.
- `01_Universe_Inject.sql`: revision 25, 94,599 bytes, sha256 `2ee488e2…6a`. It changed since the last /prompt round (revision 22, `52c581f4…a43`). Per the Eval 0 diff (same hash), it adds 6 INSERTs and 1 UPDATE and changes 2 rows:
  - Leonard's Drive file and Google Doc "notes for monday" (physical lines 11–12, 20–21), attached to card #80 (Trello attachment, line 85);
  - Blake's GitHub review `rev_8` and review comment `rc_7` on PR match3d#265 (lines 133–136), mirrored by the GitHub bot in #zombie-prs (lines 60–62);
  - card #80 `desc` and the updateCard `card.desc` (lines 65 and 73), which add rule 1's reverse sentence: "It works the other way too: a title match Blake marked ''not tiers'' in his review on its PR stays off."
- No error/async config, dynamic context or reference files were supplied, and the prompt references none. A saved Agent trajectory exists in the workspace; under stage ownership it was not opened.
- Evidence contract `stage-evidence-v1`. **Reused:** prior `1_prompt.md` facts for byte-identical SQL rows and base records (ticket scope and statuses, Blake's mails, the deck, ZOM-42, the build files, the enrage sheet, checklist, thread reply, card comment, invite, folder, agenda, Linear states, ZOM-281). **NEW:** everything revision 25 touches: the notes doc and its Drive ACL, the card attachment, card rule 1's new sentence, PR #265 with all its reviews and review comments, GitHub user EMPLOYEE_0025 (Arthur Blake), ZOM-258 and ZOM-312 in Linear, a complete GitHub scan for "not tier", the invite's attendee list, the agenda doc, and the #zombie-prs channel. Forks B–T recomputed with the new counts; forks U, V, W and X added.
- Line numbers: report text uses physical (`\n`) SQL lines. The generated UGT section uses the check helper's numbering, which also splits on bare `\r` inside Gmail bodies, so rows after line 86 show higher numbers there (Blake's reply is helper line 138; the PR #265 review and comment are helper lines 204 and 206).

**What this round changes.** The prompt is the same. The answer changes in four places, and each one comes from a new record that the prompt reaches through "everything it points to":
- **ZOM-312 drops out.** It is a title match, but Blake marked it "not tiers" in his review on PR #265.
- **ZOM-258 drops out.** Leonard's notes say "leave ZOM-258 off the list".
- **Arthur gets view access instead of comment.** The notes say "view access is enough for him".
- **The DM reply also says which ticket replaced which.** That is ZOM-282 replacing ZOM-254.

The new answer is 28 tickets (Live 16 / Editor only 8 / Replaced 1 / Not shipped 3), 13 comments, four shares (Robert and Brian edit, Leonard comments, Arthur views) and the DM reply.

---

### Injection Gate
- **State:** NEVER_REVIEWED. The gate reads `reports/input_manifest.json`, which this portal's writer never creates.
- **Eval 0 handling:** `0_injection.md` (injection-static-v2) reviews the identical SQL hash `2ee488e2…6a` (revision 25): **FINAL VERDICT: PASS**, COMPLETE (lint: 170 INSERT, 2 UPDATE, 0 FAIL / 0 CHECK / 0 INFO). Static checks A–B are REUSED. The Check C items this prompt depends on were redone here (Phase 3.2).
- **Reviewed SQL sha256:** `2ee488e28ab5b13fb02eb3d32ca292b93362bc1decd424856f140ffe5a221e6a`. Eval 0 verdict: PASS.
- **Eval 0 downstream advisories on records this prompt depends on:**
  - **D4 (notes doc):** Julia can reach it two ways:
    - card #80 attachment "notes for monday" (line 85; `trello_get_attachments`), with Trello unscoped;
    - the doc itself, shared with julia.lawson@ as reader (Drive line 12, `shared_roles_json` `[{"email": "julia.lawson@harmonygames.co", "role": "reader"}]`), via `gdrive_search` / `gdocs_get_document_text`.

    All three instructions go into the answer (forks U, V, X).
  - **D5 ("not tiers"):** the mark sits in review comment `rc_7` of Blake's review `rev_8` on PR #265 (title "ZOM-312"). GitHub is unscoped, and the PR is found with `github_search_pull_requests` "ZOM-312" or from ZOM-312's closing note "merged with match3d#265". It is read with `github_get_pull_request_reviews` / `github_get_pull_request_comments`. A complete scan of GitHub `data.json` for "not tiers" finds nothing in base (scan_complete). The only "not tier" hits are a 2024 GameOfDominoes commit and PR #571 ("not tier 0"), so ZOM-312 is the only ticket the reverse rule removes (fork W). The Slack mirror is in #zombie-prs, a public channel Julia isn't a member of; the answer doesn't need it.
  - **D1–D3 and the r17 notes** are carried unchanged: ZOM-281 in and Live; starting-tier timing from the build (10 games played); ZOM-42's wording for the promotion/demotion window.
- **Advisories carried:** A1–A5 and G1 (schema-snapshot columns, Trello action `_id` fields, new GitHub columns). None changes a graded value.

---

### Phase 0: Sources read

Docs and references read: Eval 1 (applied in full); `prompt_rubric_reliability.md` release binding; `deep_recheck.md`; `common_errors.md`; `acl.md`; `roster.json`; tool catalog (Trello attachment, GitHub PR review/comment, Drive share/search tools checked by name and parameters). The PDFs in `Evals/Docs` were not re-extracted; Eval 1's inline bands and Local Overrides were applied (evidence limit, unchanged from prior rounds).

Universe exploration, NEW this round (synth-cut base plus SQL overlay):
- **Card rule 1 (line 65 = line 73):** "… plus any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''. It works the other way too: a title match Blake marked ''not tiers'' in his review on its PR stays off. Duplicates are out; open, cancelled and never-merged ones are in, as Not shipped."
- **Notes doc (line 21; Drive line 12):** owner leonard.hayes@, shared with julia.lawson@ (reader), created 2025-09-30T15:47:03Z, modified 15:51:58Z. It reads:
  > notes for monday / julia, three things for the register: / - leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays. / - arthur is only listening in on monday, view access is enough for him. / - when you reply to me, also tell me which ticket replaced which. / for the session: register first, top to bottom, then the rules tab, then rage by level.
- **Card #80 timeline (Trello):**
  - createCard 2025-09-29T18:05:12Z;
  - updateCard (desc) 2025-09-30T14:04:31Z;
  - commentCard 15:41:55Z ("rest of the card stands");
  - notes doc 15:47–15:51Z, attached 15:52:40Z;
  - addChecklistToCard 16:20:11Z;
  - Leonard's DM 19:48:26Z, thread reply 20:07:18Z.
- **PR match3d#265 (base `/pull_requests/2147`):** title "ZOM-312", author EMPLOYEE_0025 (`/users/6`, name "Arthur Blake"), head 28cc6fa…, merged 2025-07-03T18:01:36Z. The base already has Blake's own COMMENTED reviews on it (rev_3, rev_5). The injected rev_8 (COMMENTED, 17:50:12Z, commit = head) carries rc_7 on `LevelSettings.cs`: "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work".
- **ZOM-312 (base `/issues/3368`):** "Delete Difficulty Tier and Reassign", created 2025-06-26, completed 2025-07-08. It is a title match (Difficulty, Tier), and was Editor only last round.
- **ZOM-258 (base `/issues/3308`):** "Icon for Enraged monster", created 2025-06-13, completed 2025-06-23. It is a title match (Enraged), and was Live last round.
- **Invite (line 121, Julia's calendar):** Leonard (organizer), Julia, robert@, arthur.blake@, brian.foster@.
- **Agenda doc (line 19):** "1. Baseline (Julia): the register … One sheet with two tabs, Tickets and Rules in force … 2. Rage by level (Leonard) …". The notes' "then rage by level" is agenda item 2, Leonard's own topic, not a register tab.

Status derivation (shows solvability, not a golden answer):
- **Live 16:** ZOM-23, 42, 45, 199, 221, 246, 263, 274, 281, 282, 288, 295, 300, 303, 305, 378.
- **Editor only 8:** ZOM-162, 163, 173, 200, 201, 250, 277, 315.
- **Replaced 1:** ZOM-254, replaced by ZOM-282.
- **Not shipped 3:** ZOM-202, 280, 293.
- **Total 28** = 31 title matches (Duplicates ZOM-203 and ZOM-276 already out) minus ZOM-312 ("not tiers"), plus the five "tiers:" tickets ZOM-221, 281, 300, 305, 378 (35), minus ZOM-30, 49, 50, 161, 262, 275 (DM reply) and ZOM-258 (notes).
- **Comments (13):** ZOM-199 (what the build does: cpm > 90), ZOM-254 (replaced by ZOM-282), and the 11 Editor only and Not shipped tickets (the change isn't in the store builds). ZOM-312 now gets none.
- **Shares:** robert@ and brian.foster@ can edit; leonard.hayes@ can comment; arthur.blake@ can view.
- **Rules in force (unchanged):**
  - starting tier after the first 10 games played, from their average CPM: above 90 to tier 1, everyone else tier 0;
  - promotion at 80% or more over up to the most recent 10 attempts, and on tier -2 one win promotes;
  - demotion on 4 losses in a row at any time, or 50% or lower over up to the last 10 games;
  - the record resets after every promotion or demotion;
  - after a demotion, the level being played is replayed lower until a win;
  - enrage: the sheet's Live tab as it stands.
- **DM reply:** total 28, the four status counts, the keys of the 3 Not shipped and 8 Editor only tickets, that ZOM-282 replaced ZOM-254, and when a new player gets their starting tier.

---

### Requirement ledger

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Find Leonard's Tuesday DM ask, including his thread reply | SQL lines 48 and 54 (D05HB64NMQU, 19:48:26Z and 20:07:18Z) | Slack DM history; thread via reply_count | `slack_conversations_history`, `slack_conversations_replies` / `slack_read_thread`, search | Julia (EMPLOYEE_0005) is a DM member | The ask: register; six tickets off; reply with total, per-status counts, Not shipped and Editor only keys, and the starting-tier timing |
| "everything it points to": card rules | Card #80 (line 65), updateCard (73), commentCard (75), checklist and items (77–83) | DM names "the difficulty baseline card on the zm roadmap board" | `trello_get_cards_on_board`, `trello_get_card`, `trello_get_card_actions`, checklist reads | Trello unscoped | Rules 1–7 (rule 1 with the 'not tiers' reverse sentence), the attack-power addendum, and the rule 6 and rule 7 changes |
| "everything it points to": notes on the card | Trello attachment (line 85) → Google Doc (line 21), Drive file (line 12) | Card attachment; Drive search/recent files | `trello_get_attachments`, `gdrive_search`, `gdocs_get_document_text` | Doc shared with Julia as reader | ZOM-258 off; Arthur view; reply says which ticket replaced which |
| Ticket scope | Linear ZOM issues; "tiers:" comments (incl. ZOM-281); PR #265 review comment; Trello comment; DM thread reply; notes | Linear search/list; per-ticket comments; PR lookup per title match | Linear search/get and comments; `github_search_pull_requests`, `github_get_pull_request_reviews`, `github_get_pull_request_comments` | Linear, GitHub unscoped; doc as above | 28 tickets |
| Status per ticket (rules 3–4) | Blake's mail and reply; Linear states and closing notes | Gmail search; Linear | Gmail read; Linear reads | Julia's mailbox; unscoped | Live 16 / Editor only 8 / Replaced 1 / Not shipped 3 |
| Rules in force tab (rule 5) | Deck, ZOM-42, Blake's reply, enrage sheet Live tab, `TierManager.cs`, `WinRateRule.cs`, `WinHistory.cs`, `GameLoader.cs` | GSlides, Linear, Gmail, GSheets, GitHub | `gslides_get_presentation_text`, Linear get, `gsheets_values_batch_get`, `github_get_file_contents` | Deck shared; sheet owned by Julia; GitHub, Linear unscoped | As in Phase 0 (unchanged) |
| Build the register: one sheet, tabs Tickets + Rules in force | Agenda doc; card rule 2 | GDocs | `gsheets_create_spreadsheet`, `gsheets_batch_update`, `gsheets_values_update` | Write (ACL-free) | New spreadsheet |
| Put it in the ZM Difficulty folder | Prompt; card rule 7 | Drive folder d_96489e1e00a56685625939 | `gdrive_move_file` (or create with parent) | Julia is writer | File in folder |
| Share with everyone on Monday's invite | Prompt; card rule 7, checklist rule 7 change, notes (Arthur) | GCal event on Julia's calendar | `gdrive_share_file` (role param) | Julia's own calendar | robert@, brian.foster@ writer; leonard.hayes@ commenter; arthur.blake@ reader |
| Ticket comments (rule 6 as changed) | Card rule 6; checklist item; Blake's reply; rule 4 | Linear | `linear_create_comment` | Write | ZOM-199, ZOM-254 and the 11 Editor only and Not shipped tickets |
| Reply to Leonard in the DM | DM, thread reply, notes | Slack | `slack_send_message` | Write | Total 28, per-status counts, Not shipped and Editor only keys, ZOM-282 replaced ZOM-254, and that a new player gets their starting tier after their first 10 games (from those games' average CPM) |

Output capability: spreadsheet/tab creation, moving into the folder, sharing, Linear comments and the Slack reply are SUPPORTED by declared catalog tools. The `commenter` and `reader` roles are free strings for `gdrive_share_file` `role`. Their runtime acceptance is UNVERIFIED (evidence limit, not a failure).

---

### Phase 1: Prompt Structure & Persona (prompt text byte-identical; re-judged against the new sources)

**Persona:** PASS (5). The prompt matches the exact roster entry. It is a CEO-to-PM delegation; the card says "Julia owns this one", and the notes are addressed "julia, three things for the register".

**Assigned Competency:** PASS (5). Engineering Ops: reconciling tickets with what shipped in store builds, PR review marks, the build code for the starting tier, and 13 ticket comments.

**Assigned Task Skill:** PASS (5). Retrieval is the core work:
- every in-scope ticket, including one found only through a closing note and one removed only by a PR review comment;
- each ticket's state, shipped status and rule value, across seven services;
- three late instruction layers to find: the comment, the notes and the checklist.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS. Data seeding PASS.
- **Dynamic Change:**
  - the notes (15:47Z) and the checklist (16:20Z) change the card after Leonard's comment "rest of the card stands" (15:41Z);
  - the thread reply narrows the scope after the DM.
- **New friction:**
  - ZOM-312 is a title match that only a PR review comment removes;
  - ZOM-258 is a title match that only the attached notes remove;
  - Arthur's role is set by the notes, not by rule 7.
- **Decoys (unchanged):** Brian's "+50% … every monster" and "the editor bits too"; Domino card #211; the "Next pass" tab; Vincent's channel request; ZOM-281 having no PR; the code's own first-games window against ZOM-42's wording; "rage by level" in the notes and agenda.

**Naturalness:** PASS. First person, lowercase and casual, with no document formatting, polished connectives or enumerated specs.

**Anti-Patterns:**
| Pattern | Status |
|---------|--------|
| Command List | PASS. One lowercase "then" with no first/finally, and the order is Leonard's own condition ("reply here when it''s in the folder") |
| Bolt-On | PASS. Every sentence serves the baseline |
| Pre-Solving | PASS. No counts, tickets, statuses, exclusions, timings or causes named |
| Tool Mention | PASS. "dm", "folder", "invite" and "tickets" are natural nouns |

**Diversity:** a two-tab sheet, folder placement, role-based sharing with three roles, a 13-ticket Linear comment batch, and a DM reply over a 28-ticket cohort with a rules answer.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** PASS (5). Every fork resolves to one end state.
- **U (new): Arthur commenter vs viewer. Excluded.**
  - Card rule 7 says "everyone else comments", and the checklist's later rule 7 change is only about Brian.
  - Leonard's notes are "three things for the register" and were written after the card text (14:04Z): "arthur is only listening in on monday, view access is enough for him."
  - Under rule 7 Arthur already gets comment access, so the line only does anything if it lowers him to view. "Only listening in" gives the reason he doesn't need to comment.
  - This is the strongest new alternative, tested in full below.
- **V (new): ZOM-258 stays because the DM reply's list is final. Excluded.** The notes name ZOM-258 by key. The DM reply opens "forgot one thing", so it adds to his earlier instructions rather than replacing them, and no record puts ZOM-258 back.
- **W (new): ZOM-312 stays because #265 is Blake's own PR. Excluded.**
  - Rule 1 asks for a mark in "his review on its PR"; it doesn't require someone else's PR.
  - rev_8 is a review by EMPLOYEE_0025 (Arthur Blake) on PR #265, titled "ZOM-312", and rc_7 belongs to it (`pull_request_review_id` rev_8).
- **X (new): the DM reply leaves out the replacement. Excluded.** The prompt says to reply "with what he asked for" after going through "everything it points to". The notes say "when you reply to me, also tell me which ticket replaced which."
- **N (retested): drop all editor-tooling tickets.** Excluded. The two new "doesn't reach players" reasons each name one ticket. Card rule 3 still has an Editor only status, and the checklist comments on Editor only tickets.
- **B–T:** excluded on byte-identical rows, as last round, with counts recomputed.

### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: Every fork resolves to one end state. Revision 25 adds Leonard's 'notes for monday' doc on the card and Blake's 'not tiers' review on PR match3d\#265. The four new forks are excluded: U (Arthur commenter) by the notes' 'view access is enough for him', which only matters if it lowers his rule-7 comment role; V (ZOM-258 stays) by the notes naming it and the DM reply being an addition ('forgot one thing'); W (ZOM-312 stays) by card rule 1's reverse sentence and Blake's review rev\_8 on PR \#265; X (DM without the replacement) by the notes' 'when you reply to me, also tell me which ticket replaced which'. Forks B to T stay excluded on byte-identical rows, with the counts recomputed. End state: 28 tickets (Live 16, Editor only 8, Replaced 1, Not shipped 3), 13 comments, four shares (Robert and Brian edit, Leonard comments, Arthur views), and the DM answer including ZOM-282 replacing ZOM-254.

Alternative selection: B to T are every fork from earlier rounds, recomputed for the revision-25 overlay (every row they rest on is byte-identical to revision 22 per the Eval 0 diff; line numbers remapped). U, V, W and X are new and test each instruction revision 25 adds: Arthur's role (notes vs rule 7), ZOM-258 (notes vs the title rule and the DM reply's explicit list), ZOM-312 (rule 1's reverse sentence vs Blake being the PR author), and the reply contents (notes vs the DM's own list). N was retested against the two new 'doesn't reach players' reasons.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Follow the card as Leonard left it, his card comment, his 'notes for monday' doc attached to the card, his checklist and his DM thread: scope is every difficulty ticket created up to Aug 31 by title word plus every ticket with Blake's 'tiers:' closing note (ZOM-221, 281, 300, 305, 378), minus a title match Blake marked 'not tiers' in his review on its PR (ZOM-312, PR match3d\#265), attack power counting only when written out (ZOM-271 out), minus the six analytics and tutorial tickets his DM reply lists and ZOM-258 from his notes; status against Blake's store builds mail; Replaced only where another ticket's closing note says so (ZOM-282 on ZOM-254); comments on ZOM-199, on Replaced ZOM-254 and, per the checklist's rule 6 change, on every Editor only and Not shipped ticket; share with the invite attendees, Robert and Brian as editors, Leonard as commenter and Arthur as viewer per the notes; the Rules in force tab as before; the DM reply gives the total, per-status counts, the Not shipped and Editor only keys, which ticket replaced which, and when a new player gets their starting tier. | 28 tickets (the six analytics/tutorial tickets and ZOM-258 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Robert and Brian edit, Leonard comments, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 28 rows: the 35 rule-1 tickets (31 title matches without Duplicates ZOM-203 and ZOM-276 and without ZOM-312, which Blake marked 'not tiers' in his review on PR match3d\#265, plus tiers: tickets ZOM-221, 281, 300, 305, 378) minus the seven Leonard leaves off (ZOM-30, 49, 50, 161, 262, 275 in his DM reply and ZOM-258 in his notes for monday); Live 16, Editor only 8, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force as the build runs them: starting tier set after the first 10 games played (wins and losses), average CPM above 90 to tier 1, everyone else tier 0 (90 exactly stays on tier 0); promotion and demotion in ZOM-42's wording: 80% or more over up to the most recent 10 attempts (the last 10 games played) promotes, one win on tier -2 promotes; demotion on a losing streak of 4 games in a row at any time or a win rate of 50% or lower over up to the last 10 games; the record resets after every promotion or demotion; after a demotion the level being played is replayed lower (below the new tier) until a win; enrage from the sheet Live tab copied as it stands: nine monster rows and MonsterBase 0.8/0.8 with their numbers, and Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP) as not copied yet; DM gives the total 28, the per-status counts, the keys of the Not shipped (ZOM-202, 280, 293) and Editor only (ZOM-162, 163, 173, 200, 201, 250, 277, 315) tickets, that ZOM-282 replaced ZOM-254, and that a new player gets their starting tier after their first 10 games (levels played), from the average CPM of those games. | CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 311-311): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; SHEET\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 26-26): "\["MonsterBase (base prefab)", "0.8", "0.8", "0"\], \["Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)", "not copied yet", "not copied yet", "0"\]"; TCOMMENT\_W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 75-75): "written out (ATK on its own doesn''t)"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 79-79): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 81-81): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; CARD\_R1B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''"; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 309-309): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 92-92): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"; DMT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "tell me when a new player gets their starting tier"; DECK\_PROMO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Promotion: win rate of 80% or more over the last 10 attempts moves you up one tier."; Z42MR (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we evaluate UP TO THE MOST RECENT 10 attempts of the player"; CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; Z42LAST (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we constantly look at the last 10 games played"; Z42STREAK (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "A losing streak of 4 games in a row can still trigger at any time"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"; Z42RESET (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "every time a promotion/demotion happens, the record is reset and we start at 0 games played"; WR\_DEM50 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/WinRateRule.cs lines 31-31): "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"; GL\_RETRY (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Match3D/Game/Levels/GameLoader.cs lines 101-101): "// Make sure we go down a tier for this level"; REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "One more, for the rules tab: the starting tier check in the build is cpm &gt; 90, not &gt;= 90."; NOTES\_258 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays."; NOTES\_ART (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "arthur is only listening in on monday, view access is enough for him."; NOTES\_REPL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "when you reply to me, also tell me which ticket replaced which."; CARD\_R1NT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "It works the other way too: a title match Blake marked ''not tiers'' in his review on its PR stays off."; GH265RC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 206-206): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work" |
| B | match3d\#401 changed how enrage works (speed and damage split per monster, hp method dropped), so ZOM-282 is Replaced by match3d\#401 and gets a Replaced comment. | ZOM-282 Replaced by match3d\#401. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a Replaced comment on ZOM-282 naming match3d\#401. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-282. | Register shows ZOM-282 Replaced; DM counts Live 15, Replaced 2. | GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 200-200): "this gives enrage speed and damage their own values, they shared one since ZOM-282." |
| C | Comment on every listed ticket whose text the store builds contradict, including ZOM-42 (6-7 levels vs 10). | Correction comment also on ZOM-42. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a comment on ZOM-42. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-42. | Extra correction comment; register unchanged. | Z42A (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "gets assigned after the first 6-7 levels based on CPM" |
| D | Read the scope window in Pacific days with an Apr 21 start, dropping ZOM-23 (2025-04-21T04:51:38Z, Apr 20 PT); ZOM-30 is already off under Leonard's DM reply. | 27 tickets; ZOM-23 out. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Register 27 rows; DM total 27 and Live 15. | Z23 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3277): "2025-04-21T04:51:38Z" |
| E | Also post the register in \#zombie-design because Vincent asked Julia to drop it there. | Share with the invite and also post in \#zombie-design. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a Slack post in \#zombie-design. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus C090N54TG79. | Same register; extra channel post. | VINCENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 52-52): "julia when you have the difficulty list can you drop it in here too" |
| F | ZOM-277 (created after ZOM-250) changed how ZOM-250's average attack power works, so ZOM-250 is Replaced by ZOM-277 and gets a Replaced comment. | ZOM-250 Replaced by ZOM-277. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the ten Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a Replaced comment on ZOM-250 naming ZOM-277. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Register shows ZOM-250 Replaced; DM counts Editor only 7, Replaced 2; ZOM-250 drops out of the Editor only keys; the ZOM-250 comment names ZOM-277 instead of saying the change isn't in the store builds. | Z250 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3300): "(This is per set of items)"; Z277 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3329): "The average power should really be 334 / 5 uniques" |
| G | ZOM-254 was closed (2025-06-23) after ZOM-282 (2025-06-21) and its own QA note says blunder enrages the monsters, so ZOM-282 is not the 'later' ticket and ZOM-254 stays Live with no Replaced comment. | ZOM-254 Live; no Replaced ticket. | Same as A without the ZOM-254 comment. | Same as A without Linear ZOM-254. | Register shows ZOM-254 Live; DM counts Live 17, Replaced 0, and no replacement to report. | Z254C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 287-287): "checked on the dev build, blunder enrages the monsters on the board now" |
| H | Rule 5 asks for enrage as it works in the store builds today, so the three monsters the sheet has not copied are given what they actually run on in main: no own override, so MonsterBase's 0.8 speed / 0.8 damage. | 28 tickets (the six analytics/tutorial tickets and ZOM-258 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Robert and Brian edit, Leonard comments, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same 28 rows and counts as A; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab, with Mailman, Mayor2 and PartyGirl given 0.8 speed / 0.8 damage (MonsterBase) instead of not copied yet; DM as A. | CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; MB\_ENRAGE (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/MonsterBase.prefab lines 342-343): "enrageSpeedPercentage: 0.8" |
| I | Fill the gap from the VarC prefabs the History tab says the Live tab was copied from: VarC-PartyGirl carries enragePercentage 0.6, so PartyGirl is 0.6 speed / 0.6 damage; Mailman and Mayor2 show no enrage value in their prefab text. | 28 tickets (the six analytics/tutorial tickets and ZOM-258 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Robert and Brian edit, Leonard comments, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same 28 rows and counts as A; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab, with PartyGirl at 0.6 / 0.6 and Mailman and Mayor2 without numbers; DM as A. | SHEET\_HIST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 30-30): "\["2025-09-08", "Live tab copied from the VarC prefabs in main", "Julia"\]"; PG\_PREFAB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/VarC-PartyGirl.prefab lines 215-216): "propertyPath: enragePercentage" |
| J | Leonard's comment adds attack power in the title; ZOM-271's title says 'ATK POWER' / 'ATK Power', and 'ATK on its own' is read as ATK without 'power', so ZOM-271 (Done, June 16, card-profile stat display) is in scope as Live. | 29 tickets; ZOM-271 Live; otherwise as A. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 29 rows (adds ZOM-271); Live 17, Editor only 8, Replaced 1, Not shipped 3; DM total 29 and Live 17. | TCOMMENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 75-75): "attack power in the title counts too"; Z271 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3323): "Comprehensive Item Stat Display Rules also ATK POWER BUG. Also Change Damage sort to ATK Power sort" |
| K | Take the starting-tier window from the written rules (deck, ZOM-42, ZOM-199): average CPM over the player's first 10 levels read as ten distinct levels, so replays of a lost level don't count; &gt; 90 to tier 1, the rest tier 0. | 28 tickets (the six analytics/tutorial tickets and ZOM-258 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Robert and Brian edit, Leonard comments, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register and counts as A; Rules in force and the DM answer give the starting tier as after the first 10 distinct levels (replays not counted), instead of after the first 10 games played (wins and losses) as the build counts them. | Z42S (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "1st 10 level avg CPM &gt; 90 (top 20%) moves to tier 1, rest stays in tier 0)"; DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0." |
| L | The 'Before Monday' checklist items are unchecked, so they are Leonard's pending notes, not rules in force; card rules 6 and 7 as written stand: comments only on ZOM-199 and ZOM-254, with the Not shipped and Editor only tickets left as they are, and only Robert edits. | Checklist not applied: two comments; Brian comments. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, leonard.hayes@ and brian.foster@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 and ZOM-254 only; reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. | Same 28 rows and counts; no comments on the eleven Editor only and Not shipped tickets; brian.foster@ as commenter. | CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CL\_NAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 77-77): "'Before Monday', '68daca5871dba40417a00383'" |
| M | ZOM-378 'Level 1 is removed and creates tutorial order problems' is a tutorial ticket, so it goes off the list with the other analytics and tutorial tickets Leonard named. | 27 tickets; ZOM-378 off. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 27 rows; Live 15; DM total 27 and Live 15. | DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3440): "It creates other important issues like wrong tutorials at the wrong spot." |
| N | Leonard's reason 'they don't change how hard a level plays' (repeated in his notes for ZOM-258) and Blake's 'players never see it' on ZOM-312 are the test, so every ticket that only touches editor or debug tooling is left off too (ZOM-162, 163, 173, 200, 201, 202, 250, 277, 315), with no comments on them. | Editor-tooling tickets off the list; no comments on them. | As A without the comments on the editor-tooling tickets. | As A without those Linear tickets. | 19 rows (ZOM-162, 163, 173, 200, 201, 202, 250, 277 and 315 off); no Editor only rows; DM without Editor only keys. | DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 94-94): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; NOTES\_258 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays."; GH265RC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 206-206): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work" |
| O | ZOM-281 is assigned to someone else (usr\_EMPLOYEE\_0032), so it isn't one of Blake's tickets and its 'tiers:' note doesn't bring it in; its title has none of rule 1's words, so it stays off the list. | 27 tickets; ZOM-281 out. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 27 rows; Live 15; DM total 27 and Live 15. | Z281 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "Win streak not lost when replaying without main menu" |
| P | No PR or commit in match3d names ZOM-281, so it counts as never merged and goes on the list as Not shipped, with the checklist's not-in-the-store-builds comment. | 28 tickets; ZOM-281 Not shipped; extra comment on ZOM-281. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a not-in-the-store-builds comment on ZOM-281. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-281. | Register shows ZOM-281 Not shipped; DM counts Live 15, Not shipped 4, and ZOM-281 among the Not shipped keys. | CARD\_R1NS (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "open, cancelled and never-merged ones are in, as Not shipped" |
| Q | Answer Leonard's starting-tier question from ZOM-42's line that players get assigned after the first 6-7 levels, and put that on the Rules in force tab. | 28 tickets (the six analytics/tutorial tickets and ZOM-258 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Robert and Brian edit, Leonard comments, Arthur views; starting tier after the first 6-7 levels, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register and counts as A; Rules in force and the DM answer say a new player gets their starting tier after the first 6-7 levels. | Z42A (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "gets assigned after the first 6-7 levels based on CPM" |
| R | Use the written threshold from the deck and ZOM-199: average CPM of 90 or more starts a player on tier 1. | 28 tickets (the six analytics/tutorial tickets and ZOM-258 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Robert and Brian edit, Leonard comments, Arthur views; starting tier after the first 10 games played, average CPM of 90 or more to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register and counts as A; Rules in force (and any threshold in the DM answer) give 90 or more to tier 1, so 90 exactly goes to tier 1. | DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0." |
| S | Card rule 5 asks for promotion and demotion 'as they work in the store builds today'. The build's tier history is appended at the end and cleared on every tier change, and the win-rate check counts from index 0, so promotion and demotion are judged on the first 10 (and first 4) games since the last tier change, not the most recent ones. The Rules in force tab says that. | 28 tickets (the six analytics/tutorial tickets and ZOM-258 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Robert and Brian edit, Leonard comments, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 28 rows: the 35 rule-1 tickets (31 title matches without Duplicates ZOM-203 and ZOM-276 and without ZOM-312, which Blake marked 'not tiers' in his review on PR match3d\#265, plus tiers: tickets ZOM-221, 281, 300, 305, 378) minus the seven Leonard leaves off (ZOM-30, 49, 50, 161, 262, 275 in his DM reply and ZOM-258 in his notes for monday); Live 16, Editor only 8, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force as the build runs them: starting tier set after the first 10 games played (wins and losses), average CPM above 90 to tier 1, everyone else tier 0 (90 exactly stays on tier 0); promotion and demotion judged on the first games played since the last tier change, not the latest: 80% or more over the first 10 games on the tier promotes, on tier -2 only if the first game there is a win; 50% or lower over the first 10, or losing the first 4 games on the tier, demotes; a player who does neither in those games stays on the tier; enrage from the sheet Live tab copied as it stands: nine monster rows and MonsterBase 0.8/0.8 with their numbers, and Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP) as not copied yet; DM gives the total 28, the per-status counts, the keys of the Not shipped (ZOM-202, 280, 293) and Editor only (ZOM-162, 163, 173, 200, 201, 250, 277, 315) tickets, that ZOM-282 replaced ZOM-254, and that a new player gets their starting tier after their first 10 games (levels played), from the average CPM of those games. | CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; WH\_LOOP (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 46-46): "for (int i = 0; i &lt; gamesCount; i++)"; WH\_APPEND (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 160-160): "tierWinHistory += win ? "W" : "L";"; WH\_RESET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 26-26): "PlayerPrefs.SetString(TierWinHistoryKey, "");"; TM\_RULE (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 121-121): "WinHistory.GetWorstTierWinRatePossible(rule.NumGames) : WinHistory.GetBestTierWinRatePossible(rule.NumGames)" |
| T | Rule 5's go-by-the-build sentence now covers only the starting tier, so for demotion follow Robert's deck, the first write-up rule 5 names: demotion is 4 losses in a row only, with no 50%-or-lower rule; the window wording still follows ZOM-42. | 28 tickets (the six analytics/tutorial tickets and ZOM-258 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Robert and Brian edit, Leonard comments, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 28 rows: the 35 rule-1 tickets (31 title matches without Duplicates ZOM-203 and ZOM-276 and without ZOM-312, which Blake marked 'not tiers' in his review on PR match3d\#265, plus tiers: tickets ZOM-221, 281, 300, 305, 378) minus the seven Leonard leaves off (ZOM-30, 49, 50, 161, 262, 275 in his DM reply and ZOM-258 in his notes for monday); Live 16, Editor only 8, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force as the build runs them: starting tier set after the first 10 games played (wins and losses), average CPM above 90 to tier 1, everyone else tier 0 (90 exactly stays on tier 0); promotion and demotion in ZOM-42's wording: 80% or more over up to the most recent 10 attempts (the last 10 games played) promotes, one win on tier -2 promotes; demotion only on a losing streak of 4 games in a row (no 50%-or-lower rule); the record resets after every promotion or demotion; after a demotion the level being played is replayed lower (below the new tier) until a win; enrage from the sheet Live tab copied as it stands: nine monster rows and MonsterBase 0.8/0.8 with their numbers, and Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP) as not copied yet; DM gives the total 28, the per-status counts, the keys of the Not shipped (ZOM-202, 280, 293) and Editor only (ZOM-162, 163, 173, 200, 201, 250, 277, 315) tickets, that ZOM-282 replaced ZOM-254, and that a new player gets their starting tier after their first 10 games (levels played), from the average CPM of those games. | CARD\_R5WU (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself."; DECK\_DEM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Demotion: 4 losses in a row moves you down one tier." |
| U | Card rule 7 says everyone on the invite other than Robert comments, and the later checklist changes rule 7 only for Brian; Leonard's note that view access is 'enough' for Arthur sets a floor, not a cap, so Arthur still gets comment access. | 28 tickets (the six analytics/tutorial tickets and ZOM-258 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Robert and Brian edit, Leonard and Arthur comment; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register, comments and DM; arthur.blake@ shared as commenter, not viewer. | CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 81-81): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; NOTES\_ART (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "arthur is only listening in on monday, view access is enough for him." |
| V | ZOM-258 'Icon for Enraged monster' is a rule-1 title match, and Leonard's later DM reply lists the tickets to leave off (30, 49, 50, 161, 262 and 275) without ZOM-258, so the DM list is his final exclusion list and ZOM-258 stays on as Live. | 29 tickets; ZOM-258 Live. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 29 rows; Live 17; DM total 29 and Live 17. | CARD\_R1W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "as a whole word in the title"; Z258 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3308): "Icon for Enraged monster"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays" |
| W | ZOM-312 'Delete Difficulty Tier and Reassign' is a title match. PR match3d\#265 is Blake's own PR, so his 'not tiers' line is a comment on his own code, not 'his review on its PR'; ZOM-312 stays on as Editor only and gets the checklist's not-in-the-store-builds comment. | 29 tickets; ZOM-312 Editor only with a comment. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a not-in-the-store-builds comment on ZOM-312. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-312. | 29 rows; Editor only 9 with ZOM-312 among the Editor only keys; DM total 29. | CARD\_R1W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "as a whole word in the title"; Z312 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3368): "Delete Difficulty Tier and Reassign"; PR265 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /pull\_requests/2147): ""title": "ZOM-312"" |
| X | The prompt says to reply with what Leonard asked for in the DM; the DM and its thread reply ask for the counts, the Not shipped and Editor only keys and the starting-tier timing, so the reply leaves out which ticket replaced which. | 28 tickets (the six analytics/tutorial tickets and ZOM-258 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Robert and Brian edit, Leonard comments, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors, leonard.hayes@ as commenter and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the eleven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register, comments and shares; the DM gives the total, counts, keys and starting-tier timing without saying that ZOM-282 replaced ZOM-254. | DMC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "reply here when it''s in the folder with how many tickets made the list and how many of each status"; DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"; DMT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "tell me when a new player gets their starting tier" |

Explicit option inventory: The prompt lists no options; the status values sit in the incorporated card.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "build the register the way he set it up"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: EXCLUDED. Card rule 4 now makes a ticket Replaced only when another ticket's closing note says so and says PRs that change or split its numbers don't. match3d\#401 is a PR, and its comment describes a split of the shared value, not a replacement.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 200-200): "this gives enrage speed and damage their own values, they shared one since ZOM-282."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Live vs Replaced for ZOM-282. |
| writes | DIFFERENT | B adds a ZOM-282 comment. |
| destinations | DIFFERENT | B adds ZOM-282. |
| contents | DIFFERENT | Status cell and DM counts differ (Live 15 / Replaced 2). |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The quoted sentences exclude PRs and value splits by name; \#401's comment says it gives speed and damage their own values.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 200-200): "this gives enrage speed and damage their own values, they shared one since ZOM-282."

Compared alternative: C
Resolution: EXCLUDED. Card rule 6 limits Blake-sourced comments to tickets his mail or reply calls wrong (only ZOM-199 in the reply), and says ZOM-42 stays as it is even if its wording is a bit off; the checklist's rule 6 change adds only Editor only and Not shipped tickets, and ZOM-42 is Live.
Resolution evidence: CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "ZOM-199 says &gt;= but the code never changed from the original spec"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 79-79): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | C decides ZOM-42 needs a comment. |
| writes | DIFFERENT | C adds one comment. |
| destinations | DIFFERENT | C adds ZOM-42. |
| contents | DIFFERENT | Extra comment text. |

Authority chain: P → DMR → CARD\_R6X

Resolution relevance challenge: The quoted sentences name ZOM-42 as staying as it is; the checklist change covers Editor only and Not shipped tickets, which ZOM-42 (Live) is not; the reply names only ZOM-199.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "ZOM-199 says &gt;= but the code never changed from the original spec"

Compared alternative: D
Resolution: EXCLUDED. The scope has no start date (everything since ZM started), so ZOM-23 is in under any timezone; the next title match after Aug 31 is ZOM-517 on 2025-09-03.
Resolution evidence: CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; Z517 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3591): "2025-09-03T22:22:22Z"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | D drops ZOM-23. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rows and counts differ by one. |

Authority chain: P → DMR → CARD\_SCOPE

Resolution relevance challenge: The quoted scope removes the start-date edge; Z517 shows no ticket near the Aug 31 end.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; Z517 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3591): "2025-09-03T22:22:22Z"

Compared alternative: E
Resolution: EXCLUDED. The prompt and card both define the audience as the invite list; Vincent is not an attendee and his channel request is not part of Leonard's ask.
Resolution evidence: CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system before monday's tuning session. can you take it off my plate? go through his ask and everything it points to and build the register the way he set it up. put it in the zm difficulty folder and share it with everyone on monday's tuning invite. if his rules say something needs to happen on the tickets, go ahead and do that too. then reply to leonard in the dm with what he asked for. go with your read on the details, no need to check with me first"; CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 191-191): "VALUES ('evt\_91674a9c23d012a9ac34da', 'julia.lawson@harmonygames.co', 'ZM difficulty tuning'"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | E adds a channel post. |
| writes | DIFFERENT | E adds a Slack post. |
| destinations | DIFFERENT | E adds \#zombie-design. |
| contents | DIFFERENT | Extra post. |

Authority chain: P → DMR → CARD\_R7

Resolution relevance challenge: The prompt names the audience as the invite; the invite on Julia's calendar does not include Vincent.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system before monday's tuning session. can you take it off my plate? go through his ask and everything it points to and build the register the way he set it up. put it in the zm difficulty folder and share it with everyone on monday's tuning invite. if his rules say something needs to happen on the tickets, go ahead and do that too. then reply to leonard in the dm with what he asked for. go with your read on the details, no need to check with me first"; CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 191-191): "VALUES ('evt\_91674a9c23d012a9ac34da', 'julia.lawson@harmonygames.co', 'ZM difficulty tuning'"

Compared alternative: F
Resolution: EXCLUDED. Rule 4 now requires another ticket's closing note saying it replaces this one; ZOM-277's closing note says nothing changes in the game and names no replacement, and rule 4 says a ticket players never had stays Editor only.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; Z277C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 301-301): "this is the average in the editor''s stats panel, nothing changes in the game itself"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Editor only vs Replaced for ZOM-250. |
| writes | DIFFERENT | F replaces ZOM-250's not-in-the-store-builds comment with a Replaced comment. |
| destinations | SAME | ZOM-250 gets a comment under both readings. |
| contents | DIFFERENT | Status, DM counts and the ZOM-250 comment text differ. |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The quoted rule removes formula changes as a Replaced trigger and ranks Editor only over Replaced for tickets players never had; ZOM-277's closing note has no replace wording.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; Z277C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 301-301): "this is the average in the editor''s stats panel, nothing changes in the game itself"

Compared alternative: G
Resolution: EXCLUDED. Rule 4 now keys on another ticket's closing note, with no ordering condition. ZOM-282's closing note says it replaces the blunder 2.0 boost from ZOM-254; ZOM-254's QA note describes the dev build and is not a closing note on another ticket that replaces it. Close order no longer matters.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 311-311): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Replaced vs Live for ZOM-254. |
| writes | DIFFERENT | G drops the ZOM-254 comment. |
| destinations | DIFFERENT | G drops Linear ZOM-254. |
| contents | DIFFERENT | Status and DM counts differ (Live 17 / Replaced 0), and the DM has no replacement to report. |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The rule no longer says 'later', so close dates cannot reverse it; ZOM-282's note names ZOM-254 explicitly, which is what the rule asks for.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 311-311): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"

Compared alternative: H
Resolution: EXCLUDED. Rule 5 now says how to fill the enrage section: copy the sheet's Live tab as it stands, put a monster the sheet has not copied on the tab as not copied yet, and do not work numbers out from anywhere else. Deriving 0.8/0.8 for Mailman, Mayor2 and PartyGirl from MonsterBase inheritance in the repo is working numbers out from somewhere else. The later, more specific sentence in the same rule governs the store-builds clause for these rows; the copied numeric rows equal main (Eval 0 Check C), so the two clauses no longer pull apart.
Resolution evidence: CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; SHEET\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 26-26): "\["MonsterBase (base prefab)", "0.8", "0.8", "0"\], \["Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)", "not copied yet", "not copied yet", "0"\]"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and share list. |
| writes | SAME | Same spreadsheet, shares, Linear comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | Rules in force tab: three monsters as not copied yet (A) vs 0.8/0.8 (H). |

Authority chain: P → DMR → CARD\_R5C

Resolution relevance challenge: Not a strawman: H was the leading reading last round, and 'as they work in the store builds today' still sits in rule 5. The new sentence speaks to exactly this case, a monster the sheet hasn't copied, and names the required entry ('not copied yet') and forbids the derivation H needs.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."

Compared alternative: I
Resolution: EXCLUDED. Rule 5 says to copy the Live tab as it stands and not to work numbers out from anywhere else, so reading PartyGirl's old enragePercentage 0.6 out of its prefab is excluded; the code also no longer reads that field (Monster.cs declares only enrageSpeedPercentage and enrageDamagePercentage).
Resolution evidence: CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; MONSTER\_CS (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Monster/Monster.cs lines 87-88): "\[SerializeField\] private float enrageSpeedPercentage = 0.25f;"; PG\_PREFAB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/VarC-PartyGirl.prefab lines 215-216): "propertyPath: enragePercentage"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and share list. |
| writes | SAME | Same spreadsheet, shares, Linear comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | PartyGirl 0.6/0.6 vs not copied yet. |

Authority chain: P → DMR → CARD\_R5C

Resolution relevance challenge: The new rule 5 sentence forbids taking numbers from anywhere but the Live tab, which covers prefab text; the dead field is a second, independent reason.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted.
Challenge evidence: CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; MONSTER\_CS (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Monster/Monster.cs lines 87-88): "\[SerializeField\] private float enrageSpeedPercentage = 0.25f;"

Compared alternative: J
Resolution: EXCLUDED. Leonard's card comment now says attack power counts only when written out in the title and that ATK on its own doesn't. ZOM-271's title never spells out 'attack power'; it uses the abbreviation 'ATK POWER' / 'ATK Power'. 'Written out' sets the test (the words spelled in full), and the parenthetical names the abbreviation as what fails it, so ZOM-271 stays out. Every other ZOM title created up to Aug 31 with ATK or attack was checked: ZOM-246, 250, 263, 277 and 315 spell out 'attack power'; ZOM-21 ('Monster Attack Speed') has no 'attack power'.
Resolution evidence: TCOMMENT\_W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 75-75): "written out (ATK on its own doesn''t)"; Z271 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3323): "Comprehensive Item Stat Display Rules also ATK POWER BUG. Also Change Damage sort to ATK Power sort"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-271 out vs in (Live). |
| writes | SAME | Same spreadsheet, comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | One more register row; DM total 29 vs 28 and Live 17 vs 16. |

Authority chain: P → DMR → TCOMMENT\_W

Resolution relevance challenge: Not a strawman: ATK is the game's short form and ZOM-271 also says ATK POWER, so a reader could take 'ATK on its own' as 'ATK without power'. But 'written out' is the governing test and 'ATK POWER' is not attack power written out; the parenthetical illustrates the abbreviation failing that test rather than creating a second, looser one.
Delegation challenge: NOT_CLAIMED. No alternative scope is authorized.
Challenge evidence: TCOMMENT\_W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 75-75): "written out (ATK on its own doesn''t)"

Compared alternative: K
Resolution: EXCLUDED. Rule 5 asks for the tier rules as they work in the store builds today and says that for when a new player gets their starting tier, where a write-up and the build disagree, go by the build. The build buckets a player when total games reach 10, and total games are wins plus losses, so the window is the first 10 games played. Leonard's DM asks for the tier numbers 'as they are today', so the DM answer follows the same build fact. 'First 10 levels' read as level plays is the same answer; only 'ten distinct levels' differs, and the build clause excludes it.
Resolution evidence: CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; WH\_GAMES (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 147-147): "return GetTotalWins() + GetTotalLosses();"; DMNUM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "plus the tier and enrage numbers as they are today"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and share list. |
| writes | SAME | Same spreadsheet, shares, Linear comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | Starting-tier window on the Rules in force tab and in the DM answer: first 10 games played (A) vs first 10 distinct levels (K). |

Authority chain: P → DMR → CARD\_R5W

Resolution relevance challenge: Not a strawman: three records (deck, ZOM-42, ZOM-199) say 'first 10 level(s)'. The card's own criterion is how the rules work in the store builds, and the build code fixes the unit as games, wins and losses.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied.
Challenge evidence: CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; WH\_GAMES (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 147-147): "return GetTotalWins() + GetTotalLosses();"

Compared alternative: L
Resolution: EXCLUDED. The checklist is Leonard's later change to the same two rules on the same card: its items are labelled 'rule 6 change' and 'rule 7 change', stated as decisions with a reason ('he''ll fix rows during the session'), and were added at 16:20, after his 14:04 description update and his 15:41 'rest of the card stands' comment. Under Eval 1 §2.1 check 1 a later applicable update by the same author for the same issue and scope resolves the earlier sentence without announcing replacement. Leonard's 19:48 DM points to the card (which carries the checklist) and his 20:07 reply asks for the Not shipped and Editor only keys. An unchecked item is a to-do for the card owner ('Julia owns this one'), not a hedge; no record says the changes are pending or tentative.
Resolution evidence: CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 79-79): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 81-81): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; CL\_ACT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "'addChecklistToCard', '2025-09-30T16:20:11Z'"; UPD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "'updateCard', '2025-09-30T14:04:31Z'"; DMR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "the rules for the register are on the difficulty baseline card on the zm roadmap board"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Whether the checklist changes apply. |
| writes | DIFFERENT | L posts 2 Linear comments instead of 14 and shares Brian as commenter instead of editor. |
| destinations | DIFFERENT | L drops the eleven Editor only and Not shipped tickets. |
| contents | DIFFERENT | Brian's role differs. |

Authority chain: P → DMR → CL\_R6

Resolution relevance challenge: Not a strawman: the card description still literally says the Not shipped and Editor only tickets stay as they are and that everyone but Robert comments, and the items are unchecked. The quoted items name the exact rules they change and say what now happens; they post-date both the description and Leonard's 'rest of the card stands' comment, and come from the same author on the same card.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the later card change is applied.
Challenge evidence: CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 79-79): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; TCOMMENT\_S (Evals/task\_inputs/01\_Universe\_Inject.sql lines 75-75): "rest of the card stands."; CL\_ACT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "'addChecklistToCard', '2025-09-30T16:20:11Z'"

Compared alternative: M
Resolution: EXCLUDED. Leonard's exclusion names its tickets in parentheses (30, 49, 50, 161, 262 and 275) and ZOM-378 is not among them. ZOM-378 is in scope as one of Blake's tier tickets, and his closing note says the fix lines the first levels up with their tier versions, which changes how hard those levels play, so Leonard's reason does not reach it either.
Resolution evidence: DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 379-379): "tiers: closing. level 1 is back in the list so the first levels line up with their tier versions again"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-378 on vs off. |
| writes | SAME | ZOM-378 is Live and gets no comment either way. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | One row fewer; DM total 28 and Live 15. |

Authority chain: P → DMX

Resolution relevance challenge: Not a strawman: ZOM-378's title says 'tutorial order problems' and its description is about tutorials. But the DM gives an explicit list, and the tiers: note quoted ties ZOM-378 to tier level versions, which is difficulty.
Delegation challenge: NOT_CLAIMED. No alternative scope is authorized.
Challenge evidence: DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 379-379): "tiers: closing. level 1 is back in the list so the first levels line up with their tier versions again"

Compared alternative: N
Resolution: EXCLUDED. The exclusion is scoped to 'the analytics and tutorial tickets' with their keys listed, and in the same message Leonard asks for the keys of the editor only ones, which only makes sense if they stay on the list; the checklist's rule 6 change also has Editor only tickets commented, and card rule 3 lists Editor only as a status. The newer 'doesn't change how hard a level plays' (ZOM-258 note) and 'players never see it' (ZOM-312 review) lines each name one ticket by key or PR; card rule 3 keeps an Editor only status and the checklist comments on Editor only tickets, so the list still holds them.
Resolution evidence: DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 79-79): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Editor-tooling tickets off vs on. |
| writes | DIFFERENT | N drops their comments. |
| destinations | DIFFERENT | N drops those Linear tickets. |
| contents | DIFFERENT | Rows, counts and DM keys differ. |

Authority chain: P → DMK

Resolution relevance challenge: The reason clause explains the listed tickets; the same message asks for editor only keys, which rules out dropping them.
Delegation challenge: NOT_CLAIMED. No alternative scope is authorized.
Challenge evidence: DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"

Compared alternative: O
Resolution: EXCLUDED. Rule 1 now brings in 'any ticket Blake counts as tier work even if the title doesn't say so', marked by his closing note starting 'tiers:'; it does not require Blake to be the assignee. The ZOM-281 note is by usr\_cc3e90160f490686, which Linear /users/35 maps to arthur.blake@, and it starts 'tiers: closing.', 22 minutes before ZOM-281 was completed.
Resolution evidence: CARD\_R1B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''"; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 309-309): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; LUSR\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /users/35): "arthur.blake@harmonygames.co"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | O drops ZOM-281. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rows and counts differ by one (29 / Live 16). |

Authority chain: P → DMR → CARD\_R1B

Resolution relevance challenge: Not a strawman: ZOM-281's assignee is another person and the old rule 1 wording tied scope to Blake's own tickets. The current rule 1 keys on the note, and the note's author id is Blake's.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R1B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''"; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 309-309): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; LUSR\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /users/35): "arthur.blake@harmonygames.co"

Compared alternative: P
Resolution: EXCLUDED. Card rule 3 makes Blake's store builds mail the authority for what is in the store builds and what counts as shipped. The mail says both store builds were cut from main on Sep 26 and everything difficulty related was merged long before that; it strips only level editor and debug code, and ZOM-281 (win streak on replay) is a gameplay fix. ZOM-281 is Done, completed 2025-06-27, and Blake's closing note says it was checked on the dev build. Rule 1's 'never-merged' covers work that never landed, not a Done ticket the shipped-authority calls merged.
Resolution evidence: CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 92-92): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that."; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 94-94): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 309-309): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; Z281D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "2025-06-27T09:56:19Z"; Z281 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "Win streak not lost when replaying without main menu"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Live vs Not shipped for ZOM-281. |
| writes | DIFFERENT | P adds a ZOM-281 comment. |
| destinations | DIFFERENT | P adds ZOM-281. |
| contents | DIFFERENT | Status cell, DM counts and Not shipped keys differ. |

Authority chain: P → DMR → CARD\_R3 → MAIL\_MERGED

Resolution relevance challenge: Not a strawman: a complete GitHub scan finds no 'ZOM-281' string, so an Agent looking for a merged PR finds none. The card names the mail as the shipped authority and the mail answers the question for difficulty work as a class.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 92-92): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that."; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 94-94): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 309-309): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; Z281D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "2025-06-27T09:56:19Z"; Z281 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "Win streak not lost when replaying without main menu"

Compared alternative: Q
Resolution: EXCLUDED. ZOM-42's 6-7 levels line is provisional ('to be defined later') and the same ticket's rule 1 gives the first 10 levels' average CPM; the deck and ZOM-199 also say first 10. Card rule 5 says that for when a new player gets their starting tier, where a write-up and the build disagree, go by the build, and the build buckets a player when total games reach 10. Leonard's DM asks for the tier numbers as they are today.
Resolution evidence: Z42TBD (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "to be defined later"; Z42S (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "1st 10 level avg CPM &gt; 90 (top 20%) moves to tier 1, rest stays in tier 0)"; DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; DMNUM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "plus the tier and enrage numbers as they are today"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Starting-tier timing on the Rules in force tab and in the DM answer: 10 games vs 6-7 levels. |

Authority chain: P → DMR → CARD\_R5W

Resolution relevance challenge: Not a strawman: ZOM-42 is the system ticket rule 4 sends to the rules tab, and its 6-7 sentence is the only text that answers 'when' in so many words. Its own 'to be defined later', its own rule 1, the deck, ZOM-199 and the build all give 10.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: Z42TBD (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "to be defined later"; Z42S (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "1st 10 level avg CPM &gt; 90 (top 20%) moves to tier 1, rest stays in tier 0)"; DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; DMNUM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "plus the tier and enrage numbers as they are today"

Compared alternative: R
Resolution: EXCLUDED. Blake's reply is written 'for the rules tab' and says the build checks cpm &gt; 90, not &gt;= 90, so 90 exactly stays on tier 0; card rule 5 asks for the starting tier 'as they work in the store builds today', and rule 6 has the ZOM-199 comment say what the build does; TierManager.cs line 93 is 'cpm &gt; 90.0f'. Rule 5's narrowed build clause covers when the starting tier is given, so the threshold rests on the rules-tab note and the opening clause.
Resolution evidence: REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "One more, for the rules tab: the starting tier check in the build is cpm &gt; 90, not &gt;= 90."; REPLY90 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "so 90 exactly stays on tier 0"; CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set (the ZOM-199 comment is in both). |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Threshold: above 90 vs 90 or more. |

Authority chain: P → DMR → CARD\_R5B

Resolution relevance challenge: Not a strawman: the deck and ZOM-199 both say 90 or more. Blake's reply, addressed to the rules tab, and the build say otherwise, and rule 5 asks for the starting tier as it works in the store builds.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "One more, for the rules tab: the starting tier check in the build is cpm &gt; 90, not &gt;= 90."; REPLY90 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "so 90 exactly stays on tier 0"; CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"

Compared alternative: S
Resolution: EXCLUDED. Card rule 5 (revision 22) now settles this item directly: 'For which games promotion and demotion look at, write it the way ZOM-42 words it.' ZOM-42 words the window as up to the most recent 10 attempts / the last 10 games played, with the record reset after every promotion or demotion, and says a losing streak of 4 in a row can still trigger at any time. The later, more specific sentence in the same rule governs the opening 'as they work in the store builds today' for this one item, the same way rule 5's enrage sentence governs the enrage rows (fork H). The code's first-10-since-the-last-change window is therefore not what the tab states.
Resolution evidence: CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; Z42MR (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we evaluate UP TO THE MOST RECENT 10 attempts of the player"; Z42LAST (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we constantly look at the last 10 games played"; Z42RESET (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "every time a promotion/demotion happens, the record is reset and we start at 0 games played"; Z42STREAK (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "A losing streak of 4 games in a row can still trigger at any time"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rules in force tab: promotion and demotion over the latest 10 (and 4 in a row at any time) vs over the first 10 and first 4 games since the last tier change. |

Authority chain: P → DMR → CARD\_R5PD

Resolution relevance challenge: Not a strawman: last round's deep recheck passes P1 and P2 raised it and it failed UGT. The new card sentence names exactly this item ('which games promotion and demotion look at') and names ZOM-42 as the wording to use, and ZOM-42 states the window in one consistent way across its promotion, demotion and streak paragraphs.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card names the wording to use.
Challenge evidence: CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; Z42MR (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we evaluate UP TO THE MOST RECENT 10 attempts of the player"; Z42STREAK (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "A losing streak of 4 games in a row can still trigger at any time"

Compared alternative: T
Resolution: EXCLUDED. Rule 5 opens by asking for promotion and demotion 'as they work in the store builds today', and the build has the 50%-or-lower demotion rule (WinRateRule.cs line 31). ZOM-42, the other write-up rule 5 names and the one it sends promotion/demotion wording to, has the same rule. The deck's demotion line omits it; it does not say there is no such rule, so there is no write-up/build disagreement for a tie-break to settle. Both demotion rules go on the tab.
Resolution evidence: CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; WR\_DEM50 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/WinRateRule.cs lines 31-31): "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"; CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; DECK\_DEM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Demotion: 4 losses in a row moves you down one tier."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rules in force demotion: two rules (4 in a row, or 50% or lower over up to the last 10) vs the 4-loss rule only. |

Authority chain: P → DMR → CARD\_R5B

Resolution relevance challenge: Not a strawman: the narrowed build clause no longer covers demotion, and the deck is a named write-up whose demotion line lists only the 4-loss rule. It is excluded because the deck is silent on the 50% rule rather than contrary, while the build and ZOM-42 both have it and rule 5 asks for the rules as they work in the store builds.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card names the wording to use.
Challenge evidence: CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; WR\_DEM50 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/WinRateRule.cs lines 31-31): "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"; DECK\_DEM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Demotion: 4 losses in a row moves you down one tier."

Compared alternative: U
Resolution: EXCLUDED. Leonard's notes for monday, attached to the card and written after the card text (doc 2025-09-30T15:47-15:51Z; card description updated 14:04:31Z), are 'three things for the register', and one of them is Arthur's access: he is 'only listening in', so 'view access is enough for him'. Rule 7's default for him is comment, so the line has no effect unless it lowers him to view. The later checklist (16:20:11Z) changes rule 7 only for Brian and says nothing about Arthur.
Resolution evidence: NOTES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "julia, three things for the register:"; NOTES\_ART (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "arthur is only listening in on monday, view access is enough for him."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 81-81): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; TATT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 85-85): "'notes for monday', '68daca5871dba40417a00383'"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Arthur viewer vs commenter. |
| writes | DIFFERENT | Different role on the arthur.blake@ share. |
| destinations | SAME | Same four shares. |
| contents | SAME | Same register and DM. |

Authority chain: P → DMR → NOTES → NOTES\_ART

Resolution relevance challenge: Not a strawman: 'enough' can be read as a floor. But the doc lists changes to the register setup, and 'only listening in' gives the reason he does not need to comment; reading it as a floor makes the instruction do nothing.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; Leonard's instruction is applied, not delegated.
Challenge evidence: NOTES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "julia, three things for the register:"; NOTES\_ART (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "arthur is only listening in on monday, view access is enough for him."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 81-81): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; TATT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 85-85): "'notes for monday', '68daca5871dba40417a00383'"

Compared alternative: V
Resolution: EXCLUDED. The notes name ZOM-258 and say to leave it off; the DM reply opens 'forgot one thing', which adds exclusions rather than replacing earlier ones, and no record puts ZOM-258 back. Both are Leonard's, and they cover different tickets, so both apply (scope check).
Resolution evidence: NOTES\_258 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays."; DMF (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "forgot one thing: leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275)"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-258 off vs Live. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rows 28 vs 29; Live 16 vs 17. |

Authority chain: P → DMR → NOTES → NOTES\_258

Resolution relevance challenge: The quoted note names the ticket by key; 'forgot one thing' marks the DM reply as an addition, so it cannot be read as the complete list.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; Leonard's instruction is applied, not delegated.
Challenge evidence: NOTES\_258 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays."; DMF (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "forgot one thing: leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275)"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"

Compared alternative: W
Resolution: EXCLUDED. Rule 1 asks for a title match Blake marked 'not tiers' in his review on its PR, and does not say the PR has to be someone else's. Blake left review rev\_8 on PR match3d\#265 (title 'ZOM-312'), and its review comment says 'not tiers ... leave it out when we list tier work'. So ZOM-312 stays off and gets no comment.
Resolution evidence: CARD\_R1NT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "It works the other way too: a title match Blake marked ''not tiers'' in his review on its PR stays off."; GH265REV (Evals/task\_inputs/01\_Universe\_Inject.sql lines 204-204): "'harmonygames-Games/match3d\#265\#rev\_8', 'harmonygames-Games/match3d\#265', 'EMPLOYEE\_0025\_GITHUB\_USERNAME', 'COMMENTED'"; GH265RC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 206-206): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work"; PR265 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /pull\_requests/2147): ""title": "ZOM-312""; GHU\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /users/6): ""name": "Arthur Blake""

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-312 off vs Editor only. |
| writes | DIFFERENT | W adds a ZOM-312 comment. |
| destinations | DIFFERENT | W adds Linear ZOM-312. |
| contents | DIFFERENT | Rows 28 vs 29; Editor only 8 vs 9; keys differ. |

Authority chain: P → DMR → CARD\_R1NT

Resolution relevance challenge: Rule 1 asks only for Blake's review on the ticket's PR. Review rev\_8 is authored by EMPLOYEE\_0025 (Arthur Blake) on PR \#265, and the comment is part of that review.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; Leonard's instruction is applied, not delegated.
Challenge evidence: CARD\_R1NT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "It works the other way too: a title match Blake marked ''not tiers'' in his review on its PR stays off."; GH265REV (Evals/task\_inputs/01\_Universe\_Inject.sql lines 204-204): "'harmonygames-Games/match3d\#265\#rev\_8', 'harmonygames-Games/match3d\#265', 'EMPLOYEE\_0025\_GITHUB\_USERNAME', 'COMMENTED'"; GH265RC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 206-206): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work"; PR265 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /pull\_requests/2147): ""title": "ZOM-312""; GHU\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /users/6): ""name": "Arthur Blake""

Compared alternative: X
Resolution: EXCLUDED. The prompt says to reply with what Leonard asked for, after going through his ask and everything it points to. His notes, reached through the card the DM points to, ask: 'when you reply to me, also tell me which ticket replaced which.' Both are Leonard's asks to Julia and they cover different content, so both apply.
Resolution evidence: P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system before monday's tuning session. can you take it off my plate? go through his ask and everything it points to and build the register the way he set it up. put it in the zm difficulty folder and share it with everyone on monday's tuning invite. if his rules say something needs to happen on the tickets, go ahead and do that too. then reply to leonard in the dm with what he asked for. go with your read on the details, no need to check with me first"; NOTES\_REPL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "when you reply to me, also tell me which ticket replaced which."; DMR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "the rules for the register are on the difficulty baseline card on the zm roadmap board"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same register decisions. |
| writes | SAME | Same DM reply write. |
| destinations | SAME | Same DM. |
| contents | DIFFERENT | The DM includes or leaves out 'ZOM-282 replaced ZOM-254'. |

Authority chain: P → DMR → NOTES → NOTES\_REPL

Resolution relevance challenge: The note addresses the reply directly ('when you reply to me') and is Leonard's own ask; the prompt's 'what he asked for' covers his asks through everything the DM points to.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; Leonard's instruction is applied, not delegated.
Challenge evidence: P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system before monday's tuning session. can you take it off my plate? go through his ask and everything it points to and build the register the way he set it up. put it in the zm difficulty folder and share it with everyone on monday's tuning invite. if his rules say something needs to happen on the tickets, go ahead and do that too. then reply to leonard in the dm with what he asked for. go with your read on the details, no need to check with me first"; NOTES\_REPL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "when you reply to me, also tell me which ticket replaced which."; DMR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "the rules for the register are on the difficulty baseline card on the zm roadmap board"

Strongest-alternative challenge (U): U is the strongest new alternative: 'view access is enough for him' does not say 'instead of comment', and rule 7 says everyone else comments. It is excluded because the doc is a list of changes for the register written after the card text, its reason ('only listening in') is why he doesn't need to comment, and reading it as a floor makes it do nothing. S, the strongest earlier fork, stays excluded by rule 5's ZOM-42 wording sentence.
Challenge evidence: NOTES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "julia, three things for the register:"; NOTES\_ART (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "arthur is only listening in on monday, view access is enough for him."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "For which games promotion and demotion look at, write it the way ZOM-42 words it."

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

**Feasibility:** PASS (5).
- Every ask maps to cataloged tools, and the needed data exists and is tool-visible. That covers the card text and attachment, checklist items, the notes doc, the DM thread, sheet cells, Linear states and comments, mail, calendar attendees, PR #265's reviews and review comments, and the repo files.
- The comment batch (13 `linear_create_comment` calls) and four shares are ordinary write volume over a source-defined cohort, not padding.

**Persona ACL Reachability:** PASS (5). Every scoped read is visible to Julia:
- DM and its thread: she is a member;
- #zombie-design: member;
- Arthur's mails: her mailbox;
- the invite: her calendar;
- folder: writer;
- agenda doc and deck: reader;
- notes doc: reader;
- sheet: owner.

GitHub, Linear and Trello (including the attachment and checklist) are unscoped. The #zombie-prs mirror of the "not tiers" comment is not needed, because the GitHub review is unscoped.

**Explicit Tool Mention:** PASS (5).

**Clarity & Specificity:** PASS (5).
- **Write set:** the same under every surviving reading: one spreadsheet in the folder, four shares (two editors, one commenter, one viewer), 13 Linear comments and one DM reply.
- **Instruction layers stack without conflict:**
  - card rules 1–7;
  - Leonard's comment (rule 1, attack power);
  - the notes (ZOM-258, Arthur's role, the reply's replacement line);
  - the checklist (rules 6 and 7, Brian);
  - the DM thread (six tickets off, the keys).

  Each later layer changes a different item.
- A top-level DM message and a thread reply carry the same content to the same recipient.
- **Not a fork:** ticking the two checklist items after doing them. The prompt doesn't ask for it.

**Contrived / Unnatural:** PASS (5).
- Destination and audience are named the way the persona knows them.
- No staged typos, opaque IDs, exact timestamps, trap hints, riddles, audit wording or if-chains.
- "if his rules say something needs to happen on the tickets" is one conditional whose rule lives on the card.

**Alignment with Today's Date:** PASS (5).
- "tuesday" resolves to 2025-09-30: the DM is at 19:48:26Z (12:48 PT), the thread reply at 20:07:18Z, and the notes at 15:47Z.
- "monday's tuning session/invite" resolves to 2025-10-06T17:00Z (10:00 PT).
- Every new record is dated before the clock: PR #265 review 2025-07-03, notes 2025-09-30.

**Originality:** N/A (no comparison samples supplied).

**Truthfulness:** PASS (5). Premises PR1–PR5 are verified against revision 25 (the DM, folder, card and invite rows keep their keys, authors and times):
- Leonard's Tuesday DM exists;
- the Monday session and its invite exist;
- the ZM Difficulty folder is unique;
- Leonard's rules are on the card the DM names, with the comment, notes and checklist on it.

**Tool Use & Cross-service:** PASS (5). Each service changes a graded fact:
- **Slack:** the six-ticket exclusion, the reply's key lists and the starting-tier question.
- **Linear:** the cohort, the states, the Replaced trigger and ZOM-42's window wording.
- **Trello:** the rules, the reverse 'not tiers' rule, the comment set and Brian's role.
- **Docs (notes):** ZOM-258, Arthur's role and the reply's replacement line.
- **Gmail:** shipped vs Editor only, the cpm rule and the ZOM-199 comment.
- **GitHub:** ZOM-312 out, the 10-game starting window, both demotion rules and the level drop.
- **Sheets:** enrage.
- **Calendar:** the share list.

Writes span Sheets, Drive, Linear and Slack.

**Investigation + Action:** PASS (5). **Coherence (Bolt-on):** PASS (5). **Business Function:** PASS (5), Product. **Complexity Dimensions & Data Seeding:** PASS (5).

---

### Phase 3: Universe Feasibility

**Data Existence:** PASS (5). Every needed entity is verified and retrievable through cataloged reads.

**Cross-Service Coherence:** NON-FAIL (3). One minor inconsistency in task-touched data (Temporal Field); not a lifecycle or sum mismatch.
- **PR match3d#401 `updated_at` precedes its own injected comment (CONFIRMED, deep recheck P2 DR3).**
  - **The records:** the SQL adds comment `harmonygames-Games/match3d#401#c_2` (physical line 130, `created_at` '2025-08-25T17:02:28Z', "this gives enrage speed and damage their own values, they shared one since ZOM-282 …") and timeline event `#401#ev_7` 'commented' at the same time (line 132). It doesn't move the base PR's `updated_at` forward: base `/pull_requests` match3d#401 has `updated_at` "2025-08-25T16:42:14Z" (= merged_at = closed_at).
  - **Why it counts:** in the base export no PR comment, review or review comment is dated after its PR's `updated_at` (0 of 687 comments, 2,230 reviews and 1,387 review comments). So the PR's last-update time now contradicts its own latest comment.
  - **Why it is task-touched:** this is the fork-B decoy the agent reads, in GitHub or through its #zombie-prs mirror (line 58).
  - **Severity:** it changes no value, set, order, recipient or destination the answer is graded on. Under the date-slip rule that makes it one minor inconsistency (NON-FAIL), not fail-level. Post-merge comments are normal in the base (11 of them), so this is not a lifecycle mismatch.
  - **Fix:** add `UPDATE github.github_pull_requests SET updated_at = '2025-08-25T17:02:28Z' WHERE id = 'harmonygames-Games/match3d#401';` after the #401 rows. `updated_at` and `id` are columns in the snapshot schema for `github_pull_requests`.
  - **Not defects:**
    - The #401 timeline id skips ev_6 (base ev_1–ev_5); 2 base PRs already have id gaps.
    - PR #265's injected review (17:50:12Z) is before its `updated_at` 18:01:36Z.
- **Notes doc (NEW):**
  - The Drive file and GDocs rows agree on id, title, owner, share and times.
  - Created 15:47:03Z, modified 15:51:58Z, attached 15:52:40Z: after the card description and before the checklist and the DM.
  - The doc sits in d_63fffeb4fab5233ed5bb73, the same parent as the ZM Difficulty folder.
  - Its three instructions don't contradict another Leonard record. Rule 7's comment default is narrowed for Arthur, and the later checklist touches only Brian.
  - The card has no addAttachmentToCard action. The base has the same pattern on 6 of its 42 cards with attachments, so this is not an inconsistency.
- **PR #265 review (NEW):**
  - rev_8 and rc_7 are authored by Blake, the PR author, which matches his existing rev_3/rev_5 on the same PR.
  - Submitted 17:50:12Z, after rev_6 (17:35) and before the 18:01:21Z approval and 18:01:36Z merge.
  - The commit id equals the PR head.
  - The bot mirror ts 1751565015 (17:50:15Z) follows the comment, and the parent's reply_count goes 12→13.
  - The base export has no review `seq`, and 3 base PRs already list reviews out of time order, so rev_8's place in the list is not a defect.
- **Card desc (changed):**
  - The new sentence describes a review mark that exists on exactly one title match (ZOM-312).
  - A complete scan finds no base "not tiers" text.
  - ZOM-312's Linear closing note "merged with match3d#265" points to the same PR.
- **Unchanged rows:** REUSED (byte-identical): thread reply and checklist rows, in-scope closing notes, ZOM-281's note, ZOM-282 naming ZOM-254, Slack authors as channel members.
- **Known base-data issues (not scored):** none touched; the task uses no Snowflake or Confluence data.
- **Not task-touched (not scored):** `Monster.cs` passes a single `enrageDamagePercentage`. Keep rubric rows off stacking behaviour.
- Injection SQL considered: Yes. Static integrity evidence: REUSED from `0_injection.md` (same hash, checks A–B). The task-relevant Check C items were redone above.

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|-----------|--------------|-------------|---------------|
| Prompt | Unique Ground Truth | 5 | New forks U, V, W, X settled by the notes doc and card rule 1's reverse sentence with Blake's PR #265 review; B–T unchanged with counts recomputed; P1's blind derivation matches |
| Prompt | Feasibility | 5 | All asks cataloged; data exists |
| Prompt | Persona ACL Reachability | 5 | Every scoped read visible to Julia, including the notes doc (reader) |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | Same write set under every reading; instruction layers change different items |
| Prompt | Contrived / Unnatural | 5 | No flags |
| Prompt | Alignment with Today's Date | 5 | Tue Sep 30 and Mon Oct 6 resolve; new records before the clock |
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
| Universe | Cross-Service Coherence | 3 | One minor Temporal Field inconsistency: PR match3d#401 updated_at (16:42:14Z) precedes the injected #401 comment (17:02:28Z) |

---

### Issues Found

| # | Issue | Severity | Dimension |
|---|-------|----------|-----------|
| 1 | Injected comment `match3d#401#c_2` (2025-08-25T17:02:28Z, SQL line 130) post-dates base PR #401 `updated_at` 2025-08-25T16:42:14Z, which the SQL leaves unchanged; base never has a comment or review after its PR's `updated_at` | Minor | Cross-Service Coherence |

### Recommended Improvements

1. **Required to reach PASS: fix issue 1.** Add this statement to the SQL after the PR #401 comment and timeline rows:
   `UPDATE github.github_pull_requests SET updated_at = '2025-08-25T17:02:28Z' WHERE id = 'harmonygames-Games/match3d#401';`
   Changing the SQL outdates every pass that reads it, so rerun /injection, /prompt, /hardness, /oe and /rubric, in that order.
2. **Bring the OEs and rubric to revision 25 before /oe and /rubric.** The expected answer changed.
   - **Scope:** 28 tickets. ZOM-312 is off (Blake's "not tiers" review on PR #265) and ZOM-258 is off (Leonard's notes). ZOM-30, 49, 50, 161, 262 and 275 stay off; ZOM-281 and ZOM-378 are on; ZOM-271 is out.
   - **Counts:** Live 16, Editor only 8, Replaced 1 (ZOM-254, replaced by ZOM-282), Not shipped 3.
   - **Comments (13):**
     - ZOM-199: the build checks cpm > 90;
     - ZOM-254: replaced by ZOM-282;
     - the 8 Editor only tickets (ZOM-162, 163, 173, 200, 201, 250, 277, 315) and the 3 Not shipped tickets (ZOM-202, 280, 293): the change isn't in the store builds.

     ZOM-42, ZOM-281, ZOM-258 and ZOM-312 get none.
   - **Shares:** robert@ and brian.foster@ can edit; leonard.hayes@ can comment; arthur.blake@ can view.
   - **DM reply:** the total 28, the per-status counts, the Not shipped and Editor only keys, that ZOM-282 replaced ZOM-254, and when a new player gets their starting tier.
3. **Grading the Rules in force tab (unchanged from last round):**
   - **Starting tier:** credit "after the first 10 levels" or "after 10 games played". Fail "after 6-7 levels". The threshold is above 90, so 90 exactly stays on tier 0.
   - **Window:** grade it against ZOM-42's wording ("up to the most recent 10" / "the last 10 games", the record reset on each change, a 4-loss streak at any time).
   - **Demotion:** expect both rules (4 losses in a row; 50% or lower).
   - **Other items:** on tier -2, one win promotes. After a demotion the level drops; grade only that it drops, not by how many tiers. Mailman, Mayor2 and PartyGirl (incl. PartyGirl 50HP) go on the tab as not copied yet.
4. **Don't grade ticking the checklist items**, and don't require a "rage by level" tab: in the notes and the agenda, that is Leonard's session topic.
5. **Optional wording**, carried from earlier rounds: "then reply to leonard in the dm…" could follow Leonard's own condition and read "once it's in the folder, reply to leonard in the dm with what he asked for." If you change it, put it in your own voice; prompts are screened for AI-written text. A prompt change outdates every pass that reads the prompt.

---

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 7 sentences, 31 forks | 0 | 0 |
| P2 | 7 sentences | 3 | 1 |
| P3 | 7 sentences, 11 claims, SQL | 1 | 0 |
| P4 | 7 sentences | 1 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P2 | "if his rules say something needs to happen on the tickets, go ahead and do that too." | Linear comments "parking this, nothing merged yet" on ZOM-400, 427, 438, 439, 441, 443, 458, 468 (lines 317–355), dated about 30 days after each issue's `updated_at` | §3 date-slip | Cross-Service Coherence | REJECTED | All eight issues are open (state Todo), with `updated_at` = `created_at` (never edited); for example ZOM-400 was created and updated "2025-07-17T23:42:56Z", and its comment is 2025-08-17. A later comment on an untouched open ticket contradicts no field. Linear's issue `updatedAt` tracks the issue's own properties, base Linear has no comments to set a pattern, and the ten-minute gap the pass saw on other tickets is closing notes on Done tickets just before `completed_at`. None of these tickets is in scope. |
| DR2 | P2 | "go through his ask and everything it points to and build the register the way he set it up." | Trello createCard `683dbef4991df7f0987ddb73` (decoy card #211) board name "Product Roadmap"; base board `65eb4ec525346c8070ca638f` "DD Product Roadmap" | Referential | Cross-Service Coherence | REJECTED | The board was renamed on 2025-07-15 (base updateBoard: `"old": {"name": "Product Roadmap"}`), and every one of the 2,084 base actions before that date carries "Product Roadmap". The createCard is dated 2025-06-02, so the old name is correct. |
| DR3 | P2 | "go through his ask and everything it points to and build the register the way he set it up." | SQL `match3d#401#c_2` created_at '2025-08-25T17:02:28Z' (line 130) and `#401#ev_7` (line 132); base PR #401 `updated_at` "2025-08-25T16:42:14Z" | Referential / date | Cross-Service Coherence | CONFIRMED | Base GitHub has no comment, review or review comment dated after its PR's `updated_at` (0 of 4,304), and the SQL doesn't update #401. One minor Temporal Field inconsistency in the fork-B decoy, which changes no graded value, so NON-FAIL (3) under the date-slip rule. The ev_6 gap part is rejected: 2 base PRs already have timeline id gaps. |
| DR4 | P3 | (SQL structure) | `schema/injection.json` lacks columns the SQL uses (`github_reviews.seq`, `github_review_comments.pull_request_review_id/seq/side/subject_type`, `linear_comments.sequence`, gslides columns) | §6.8 | Data exists | REJECTED | The snapshot is unverified ("Missing/mismatched definitions alone are advisory", schema/README.md). Eval 0 lint shows 0 FAIL and carries these as A1/A2/G1. The pass itself rates it advisory. |
| DR5 | P4 | "then reply to leonard in the dm with what he asked for." | DM `6f773865…` (line 48) "reply here when it''s in the folder with how many tickets made the list…" | §6.6 | Command list | REJECTED | §6.6 and Eval 1 §1.3.1 target a first / then / finally procedure. Here there is one lowercase "then", with no first or finally, and the order is Leonard's own condition. Same finding as last round. The optional rewording stays under Recommended Improvements. |

Effect on verdict: Cross-Service Coherence drops from 5 to 3 (DR3). Every other dimension stays 5, and the verdict moves from PASS to NON-FAIL. P1's blind derivation matches the main review exactly:
- 28 tickets: Live 16, Editor only 8, Replaced 1, Not shipped 3;
- the same key lists and 13 comments;
- Robert and Brian edit, Leonard comments, Arthur views;
- starting tier after the 10th game, above 90;
- the DM includes the replacement.

Fork list:
- F1 / W: settled | ZOM-312 off | On as Editor only, with a comment | Settled by: card rule 1 "a title match Blake marked ''not tiers'' in his review on its PR stays off"; PR #265 review comment "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work"; ZOM-312 note "merged with match3d#265."
- F2 / V: settled | ZOM-258 off | On as Live (DM list is final) | Settled by: notes "leave ZOM-258 off the list."; DM reply "forgot one thing: …" adds to it
- F3 / U: settled | Arthur views | Arthur comments (rule 7) | Settled by: notes "arthur is only listening in on monday, view access is enough for him." (15:51Z, after the card text at 14:04Z; the 16:20Z checklist changes rule 7 only for Brian)
- F4 / X: settled | DM says ZOM-282 replaced ZOM-254 | DM leaves it out | Settled by: notes "when you reply to me, also tell me which ticket replaced which."
- F5 / N: settled | Only named tickets off | All editor-tooling tickets off | Settled by: DM reply "put the keys of the not shipped ones and the editor only ones"; card rule 3 status "Editor only"; the checklist's Editor only comments
- F6 / S: settled | Window in ZOM-42's wording | The code's first games since the last change | Settled by: card rule 5 "For which games promotion and demotion look at, write it the way ZOM-42 words it."
- F7 / T: settled | Demotion: 4 in a row, or 50% or lower | 4 in a row only (deck) | Settled by: rule 5 "as they work in the store builds today"; `WinRateRule.cs` "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"; ZOM-42 "50% or lower"
- F8 / Q, K: settled | Starting tier after 10 games played | After 6-7 levels / 10 distinct levels | Settled by: rule 5 "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; `TierManager.cs` "if (totalGames == 10)"; `WinHistory.cs` "return GetTotalWins() + GetTotalLosses();"
- F9 / R: settled | cpm > 90 | 90 or more | Settled by: Blake's reply "One more, for the rules tab: the starting tier check in the build is cpm > 90, not >= 90."
- F10 / L: settled | Checklist in force (13 comments, Brian edits) | Unticked items pending | Settled by: "rule 6 change: …" / "rule 7 change: Brian gets edit as well, he''ll fix rows during the session", added 16:20:11Z, after "rest of the card stands." (15:41:55Z)
- F11 / O, P: settled | ZOM-281 in, Live | Out / Not shipped | Settled by: "tiers: closing. checked on the dev build"; Blake's mail "everything difficulty related was merged long before that"
- F12 / M: settled | ZOM-378 on | Off as tutorial | Settled by: DM reply "(30, 49, 50, 161, 262 and 275)"
- F13 / J: settled | ZOM-271 out | In | Settled by: Leonard's comment "written out (ATK on its own doesn''t)"
- F14 / H, I: settled | Enrage Live tab as it stands | Derived values | Settled by: rule 5 "Copy its Live tab as it stands … don''t work numbers out from anywhere else."
- F15 / G, B, F: settled | ZOM-254 Replaced by ZOM-282; ZOM-282 Live; ZOM-250 Editor only | Other Replaced readings | Settled by: ZOM-282 note "this replaces the blunder 2.0 boost from ZOM-254"; rule 4 "only when another ticket''s closing note says it replaces this one" / "PRs that change or split its numbers don''t"
- F16 / C: settled | No comment on ZOM-42 | Comment on ZOM-42 | Settled by: rule 6 "Every other ticket stays as it is, ZOM-42 … included"
- F17 / D: settled | ZOM-23 in | Out | Settled by: scope "so everything since we started ZM"
- F18 / E: settled | Share with the invite only | Also post in #zombie-design | Settled by: prompt "share it with everyone on monday's tuning invite"
- F19: settled (P1) | The level drops after a demotion | It doesn't | Settled by: `GameLoader.cs` "// Make sure we go down a tier for this level"; the size of the drop isn't graded
- F20: not a fork | DM top-level reply | Thread reply | Same recipient and content; accept either
- F21: not a fork | Leave the checklist items unticked | Tick them | Not asked; changes no graded content

Platform defects: none.

### FINAL VERDICT: NON-FAIL

Score: 3

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Next action: To reach PASS, add `UPDATE github.github_pull_requests SET updated_at = '2025-08-25T17:02:28Z' WHERE id = 'harmonygames-Games/match3d#401';` to the SQL, then send /injection, /prompt, /hardness, /oe and /rubric, in that order. Either way, bring the OEs and rubric to revision 25 before /oe and /rubric: 28 tickets, ZOM-312 and ZOM-258 off, 13 comments, Arthur as viewer, and the DM's replacement line (Recommended Improvements 2–4).

Evidence limits: The Evals/Docs PDFs were not re-extracted; Eval 1's restated bands and overrides were applied. Runtime acceptance of the `commenter` and `reader` share roles is unverified (declared parameters only). Eval 0 checks A–B were reused from the same-hash 0_injection.md, because this portal never writes the gate manifest. Byte-identical SQL rows reuse prior /prompt facts under stage-evidence-v1. The schema snapshot behind DR4 is unverified.

**Lowest Dimension:** Cross-Service Coherence, 3. PR match3d#401 `updated_at` (2025-08-25T16:42:14Z) precedes the injected #401 comment (17:02:28Z); base GitHub never has a comment after its PR's `updated_at`.

**Summary:** The prompt is unchanged. Revision 25's new records (Leonard's notes on the card, and Blake's "not tiers" review on PR #265 with card rule 1's reverse sentence) each settle one item: ZOM-312 and ZOM-258 off, Arthur as viewer, and the replacement line in the DM. Ground truth stays unique at 28 tickets (Live 16 / Editor only 8 / Replaced 1 / Not shipped 3), 13 comments, four shares and the DM reply. The deep recheck confirmed one minor date inconsistency on the PR #401 decoy, which holds Cross-Service Coherence at NON-FAIL until a one-line UPDATE fixes it.

Eval version: task-quality-v1

Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e

Reviewed prompt SHA-256: 22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787

Review context SHA-256: 92bcd4292145ebdab46ec7a39a65d6cc437d37c3f33d291585b6970bdd55ec3c

Prompt record SHA-256: afc84d5c44f7dc44699201acb2b61eb53bd645226a0f58051c457d0a65a239c8

