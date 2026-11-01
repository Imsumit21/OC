## PROMPT EVALUATION REPORT

### Task: Julia delegates Leonard's ZM difficulty baseline. The Agent builds the register (Tickets + Rules in force) from the Trello card rules, Leonard's card comment, his "notes for monday" doc, the "Before Monday" checklist and his Tuesday DMs. Those DMs include his new reply in the thread under Julia's Monday question. The Agent then files the register in ZM Difficulty, shares it with the Monday invite, comments on tickets per rule 6 as changed, and replies to Leonard in the DM.
### Assigned Persona: Julia Lawson - Product Manager (roster `julia_lawson`, julia.lawson@harmonygames.co)
### Assigned Business Function: Product
### Assigned Competency: Engineering Ops
### Assigned Task Skill: Retrieval
### Assigned Horizon: long-horizon (Task Type field; Difficulty Mode "medium" recorded as context)

Review: `/prompt`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode. Actual review date 2026-10-31. Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe `Universe_SynthCut` (hg4-synth-sep30cut v16; `Evals/references/universes/synthcut/universe_manifest.json`). Eval release task-quality-v1 (manifest SHA-256 `0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e`, verified with `hg_eval_release.py snapshot prompt`).

Binding:
- Reviewed prompt SHA-256: `22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787`
- Review context SHA-256: `e260e8f90d2cd3ba534532e3c94628508af4892bf092a4f28a01f20bda512e19`
- Prompt record SHA-256: `83ef6a69e7d4ea4146f0c1b026446812296feb2037c077d3c9004870626f8b2c` (policy prompt-source-checks-v2, format 2)

Inputs:
- `04_Prompt.txt`: revision 29 (attached as `04_Prompt (10).txt`), 525 bytes, sha256 `22f26066…1787`. It is byte-identical to the prompt graded last round.
- `00_Task_Assigned_Inputs.md`: all five fields are stated, so intake is clear.
- `01_Universe_Inject.sql`: revision 28, 96,059 bytes, sha256 `cd185b05da3d1db6fd0222f8a65795265eb1aff028e43039e92b5afd5af59795`. It has changed since the last /prompt round (revision 25, `2ee488e2…6a`). The change is 2 Slack INSERTs and 1 UPDATE (Eval 0 diff, same hash):
  - physical line 56: Julia's DM to Leonard, 2025-09-29T21:38:52Z: "leonard, anything you need from me before monday''s tuning session?" (thread parent, reply_count 1);
  - physical line 58: Leonard's thread reply, 2025-09-30T21:16:42Z (Tuesday, 14:16 PT): "one more for the baseline: leave the level editor tickets off too (162, 163, 201 and 250), the designers keep their own list for those, so no comments on them either. and scratch brian editing, robert will fix rows in the session. comment access is enough for brian";
  - physical line 137: `UPDATE github.github_pull_requests SET updated_at = '2025-08-25T17:02:28Z' WHERE id = 'harmonygames-Games/match3d#401';`. This is the fix the last round asked for.
- No error/async config, dynamic context or reference files were supplied, and the prompt references none. A saved Agent trajectory exists in the workspace, but under stage ownership it was not opened.
- Evidence contract `stage-evidence-v1`.
  - **Reused:** facts from the prior `1_prompt.md` (revision-25 round) for byte-identical SQL rows and base records: ticket scope and statuses, Blake's mails, the deck, ZOM-42, the build files, the enrage sheet, the checklist, the first thread reply, the card comment, the notes doc, PR #265, the invite, the folder, the agenda, Linear states and ZOM-281. SQL lines were remapped by exact quote: 1–55 unchanged, 56–132 → 60–136, 133–358 → 138–363.
  - **NEW:** both new Slack rows and their DM; the PR #401 update. Also NEW are ZOM-45, 162, 163, 173, 200, 201, 202, 203, 250, 277, 312 and 315 in Linear (complete `/issues` lookup, scan_complete) with their injected closing notes, and Blake's mail's level-editor sentences. Every fork was recomputed with the new counts; forks Y, Z and AA were added and F was dropped.
- Line numbers: report text uses physical (`\n`) SQL lines. The generated UGT section uses the check helper's numbering, which also splits on bare `\r` inside Gmail bodies, so rows after physical line 90 show higher numbers there.

**What this round changes.** The prompt is the same. Leonard's new thread reply changes three things:
- **Four tickets drop out:** ZOM-162, 163, 201 and 250, with no comments on them.
- **Brian gets comment access instead of edit.**
- **The PR #401 date mismatch is fixed.** Cross-Service Coherence goes back to 5.

The reply also opens a new fork. It says "the level editor tickets" but lists only four keys. Three other tickets on the list, ZOM-173, 277 and 315, are level-editor-only work by their own titles and closing notes and by Blake's store builds mail. No record says whether they stay on. The ticket set, the DM counts and keys, and three Linear comments all depend on that, so Unique Ground Truth fails.

---

### Injection Gate
- **State:** NEVER_REVIEWED. The gate reads `reports/input_manifest.json`, which this portal's writer never creates.
- **Eval 0 handling:** `0_injection.md` (injection-static-v2, review date 2026-10-31) reviews the identical SQL hash `cd185b05…95` (revision 28): **FINAL VERDICT: PASS**, COMPLETE. Lint found 172 INSERT and 3 UPDATE statements, with 0 FAIL / 0 CHECK / 0 INFO. Its static checks A–B are REUSED. The Check C items this prompt depends on were redone here (Phase 3.2).
- **Reviewed SQL sha256:** `cd185b05da3d1db6fd0222f8a65795265eb1aff028e43039e92b5afd5af59795`. Eval 0 verdict: PASS.
- **Eval 0 findings on records this prompt depends on:**
  - **D6 (list scope).** Eval 0 flagged that Leonard's "the level editor tickets … (162, 163, 201 and 250)" leaves ZOM-173 open, and ZOM-45 too. This review confirms the fork and widens it to ZOM-277 and ZOM-315 (closing notes: "the editor''s stats panel … nothing changes in the game itself"). ZOM-45 is not reached: its note says "the level carries it at runtime too, the game reads it when it loads the level", so it is Live. This changes the graded ticket set, counts, keys and comment writes, so it is scored under **Unique Ground Truth** and **Clarity** (Phase 2), not as a Coherence defect: the records are consistent, but the instruction is open.
  - **D7 (discoverability).** The new instruction is a thread reply under Julia's own 9/29 DM. It is discoverable: Julia is a DM member, the parent's `reply_count` is 1 and `latest_reply` is `1759267002.665190`, and thread reads are cataloged (`slack_conversations_replies` / `slack_read_thread`). The prompt reaches it as Leonard's Tuesday DM about the baseline ("one more for the baseline"). Fork AA tests this.
  - **G1–G3, D1–D5, A1–A5** are carried unchanged. None changes a graded value.

---

### Phase 0: Sources read

Docs and references read:
- Eval 1, applied in full;
- the `hg_reference.py guide prompt` WORKFLOW sections and scoring groups;
- the `prompt_rubric_reliability.md` release binding;
- `deep_recheck.md`;
- `acl.md` and `roster.json`;
- the tool catalog, by name and parameters (Slack thread reads, Drive share role, Linear comment, Sheets create).

The PDFs in `Evals/Docs` were not re-extracted; Eval 1's inline bands and Local Overrides were applied (evidence limit, unchanged from earlier rounds).

Universe exploration, NEW this round (synth-cut base plus SQL overlay):
- **The new thread (physical lines 56 and 58).** The parent is Julia (EMPLOYEE_0005) at 2025-09-29T21:38:52Z: "leonard, anything you need from me before monday''s tuning session?". It has reply_count 1, reply_users_count 1 and latest_reply = the reply's ts. The reply is Leonard (EMPLOYEE_0038) at 2025-09-30T21:16:42Z, with `thread_parent_id` set to the parent. Both are in D05HB64NMQU, an IM whose members are EMPLOYEE_0005 and EMPLOYEE_0038 (Eval 0, channels.json).
- **Instruction timeline, all 2025-09-30 UTC.**
  - The card description is updated at 14:04:31Z.
  - Leonard comments at 15:41:55Z ("rest of the card stands").
  - The notes doc is written 15:47–15:51Z.
  - The checklist is added at 16:20:11Z ("rule 7 change: Brian gets edit as well").
  - Leonard sends the DM request at 19:48:26Z and the thread reply at 20:07:18Z.
  - **The new reply comes at 21:16:42Z.** It is the latest instruction.
- **Blake's store builds mail** (Julia's copy, physical line 94): "The level editor (Assets/Scripts/LevelEditor and the LevelDesigner panels), anything in an Editor folder and the debug menu (Assets/Scripts/Debug) are stripped from store builds. A ticket whose changes are only level editor or debug tooling never reached players, Done or not."
- **The Editor only tickets before this round**, with Linear base titles and injected closing notes:

  | Ticket | Title (Linear base) | Closing note (SQL) | Named in Leonard's reply? |
  |---|---|---|---|
  | ZOM-162 | "Dynamic difficulty tracks are linked across tiers in level editor" | "closing. works on the dev build" (186) | yes |
  | ZOM-163 | "Play button in level editor not loading difficulty tiers" | "closing. works on the dev build" (188) | yes |
  | ZOM-201 | "Dynamic difficulty stat window not functioning. Also turn it into an overlay in editor while not obstructing game board." | "closing. works on the dev build" (200) | yes |
  | ZOM-250 | "Create faux level timer and add attack power stats in level editor" | "closing. works on the dev build" (220) | yes |
  | **ZOM-173** | "Item Set Count in editor not updating with difficulty tier changes", Linear label **"Level Editor"** (its Duplicate ZOM-203: "The number of item sets in the level editor UI does not update…") | "merged with match3d#243 together with ZOM-307. this one is the set count in the level objects panel…" (190) | **no** |
  | **ZOM-277** | "Correct average attack power calculation for items in level" | "closing. this is the average in the editor''s stats panel, nothing changes in the game itself" (236) | **no** |
  | **ZOM-315** | "Use base damage of item if total attack power excludes items without cardData" | "closing. this is the total attack power in the editor''s stats panel, items without cardData now count with their base damage. nothing changes in the game itself" (284) | **no** |
  | ZOM-200 | "Need debug menu for dynamic difficulty to add the metric of last 10 level average CPM…" | "closing. works on the dev build" (198) | no; debug menu, which Blake's mail names apart from the level editor |

- **ZOM-45** ("Expose the ability to mark level difficulty in editor also level object in Unity"): note "the level carries it at runtime too, the game reads it when it loads the level" (228). It is Live, not level-editor-only.
- **ZOM-202** (In Progress, "Minimize or migrate selection panel for easier difficulty tab comparison"): note "wip on a branch, nothing merged yet" (202). It is Not shipped under rule 1 ("open … ones are in, as Not shipped").
- **PR match3d#401:** after the UPDATE, `updated_at` 2025-08-25T17:02:28Z equals the injected comment `#c_2` and timeline event `#ev_7`. merged_at and closed_at stay 16:42:14Z.

Status derivation under the leading reading A (this shows solvability; it is not a golden answer):
- **Live 16:** ZOM-23, 42, 45, 199, 221, 246, 263, 274, 281, 282, 288, 295, 300, 303, 305, 378.
- **Editor only 4:** ZOM-173, 200, 277, 315.
- **Replaced 1:** ZOM-254, replaced by ZOM-282.
- **Not shipped 3:** ZOM-202, 280, 293.
- **Total 24** = the 35 rule-1 tickets minus the eleven Leonard leaves off: ZOM-30, 49, 50, 161, 262 and 275 (first DM reply), ZOM-258 (notes), and ZOM-162, 163, 201 and 250 (new reply).
- **Comments (9):**
  - ZOM-199: the build checks cpm > 90;
  - ZOM-254: replaced by ZOM-282;
  - ZOM-173, 200, 277, 315, 202, 280 and 293: the change isn't in the store builds.

  ZOM-162, 163, 201 and 250 get none ("so no comments on them either").
- **Shares:** robert@ can edit; brian.foster@ and leonard.hayes@ can comment; arthur.blake@ can view.
- **Rules in force:** unchanged from last round.
- **DM reply:** the total, the per-status counts, the Not shipped and Editor only keys, that ZOM-282 replaced ZOM-254, and when a new player gets their starting tier.
- **Under reading Y:** ZOM-173, 277 and 315 also go off. That gives 21 tickets (Live 16 / Editor only 1, ZOM-200 / Replaced 1 / Not shipped 3), 6 comments, and Editor only key ZOM-200 only.

---

### Requirement ledger

authority_contract: prompt-incorporation-v1

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Find Leonard's Tuesday DM ask, including both thread replies | SQL 48 (request, 19:48:26Z), 54 (reply 20:07:18Z), 58 (reply 21:16:42Z under Julia's line-56 message) | Slack DM history; threads via reply_count | `slack_conversations_history`, `slack_conversations_replies` / `slack_read_thread`, search | Julia (EMPLOYEE_0005) is a DM member | The register; ten tickets off (six analytics/tutorial, four level editor); reply contents |
| "everything it points to": card rules | Card #80 (line 69), updateCard (77), commentCard (79), checklist and items (81–87) | DM names "the difficulty baseline card on the zm roadmap board" | `trello_get_cards_on_board`, `trello_get_card`, `trello_get_card_actions`, checklist reads | Trello unscoped | Rules 1–7, the attack-power addendum, the rule 6 change (rule 7 change for Brian later withdrawn) |
| "everything it points to": notes on the card | Trello attachment (89) → Google Doc (21), Drive file (12) | Card attachment; Drive search | `trello_get_attachments`, `gdrive_search`, `gdocs_get_document_text` | Doc shared with Julia as reader | ZOM-258 off; Arthur view; reply says which ticket replaced which |
| Ticket scope | Linear ZOM issues; "tiers:" notes; PR #265 review comment; Trello comment; both DM replies; notes | Linear search/list; comments; PR lookup | Linear reads; `github_search_pull_requests`, `github_get_pull_request_reviews`, `github_get_pull_request_comments` | Linear, GitHub unscoped | **24 (reading A) or 21 (reading Y): unresolved** |
| Status per ticket (rules 3–4) | Blake's mail and reply; Linear states and closing notes | Gmail; Linear | Gmail read; Linear reads | Julia's mailbox; unscoped | A: Live 16 / Editor only 4 / Replaced 1 / Not shipped 3 |
| Rules in force tab (rule 5) | Deck, ZOM-42, Blake's reply, enrage sheet Live tab, `TierManager.cs`, `WinRateRule.cs`, `WinHistory.cs`, `GameLoader.cs` | GSlides, Linear, Gmail, GSheets, GitHub | `gslides_get_presentation_text`, Linear get, `gsheets_values_batch_get`, `github_get_file_contents` | Deck shared; sheet owned by Julia; GitHub, Linear unscoped | Unchanged from last round |
| Build the register: one sheet, tabs Tickets + Rules in force | Agenda doc; card rule 2 | GDocs | `gsheets_create_spreadsheet`, `gsheets_batch_update`, `gsheets_values_update` | Write (ACL-free) | New spreadsheet |
| Put it in the ZM Difficulty folder | Prompt; card rule 7 | Drive folder d_96489e1e00a56685625939 | `gdrive_move_file` (or create with parent) | Julia is writer | File in folder |
| Share with everyone on Monday's invite | Prompt; card rule 7; notes (Arthur); new reply (Brian) | GCal event on Julia's calendar | `gdrive_share_file` (role param) | Julia's own calendar | robert@ writer; brian.foster@ and leonard.hayes@ commenter; arthur.blake@ reader |
| Ticket comments (rule 6 as changed) | Card rule 6; checklist item; Blake's reply; rule 4; new reply ("no comments on them either") | Linear | `linear_create_comment` | Write | A: 9 comments; Y: 6 comments (unresolved) |
| Reply to Leonard in the DM | DM, both thread replies, notes | Slack | `slack_send_message` | Write | Total, per-status counts, Not shipped and Editor only keys, ZOM-282 replaced ZOM-254, starting-tier timing |

Output capability: these paths are SUPPORTED by declared catalog tools:
- creating the spreadsheet and its tabs;
- moving it into the folder;
- sharing;
- the Linear comments;
- the Slack reply.

The `commenter` and `reader` roles are free strings for `gdrive_share_file` `role`. Their runtime acceptance is UNVERIFIED (an evidence limit, not a failure).

---

### Phase 1: Prompt Structure & Persona (prompt text byte-identical; re-judged against the new sources)

**Persona:** PASS (5). The prompt matches the exact roster entry, and a CEO delegating to a PM fits the role. The card says "Julia owns this one", and the notes are addressed "julia, three things for the register".

**Assigned Competency:** PASS (5). Engineering Ops: reconciling tickets with what shipped in store builds, PR review marks, the build code, and a batch of ticket comments.

**Assigned Task Skill:** PASS (5). Retrieval is the core work:
- every in-scope ticket across title rules, closing notes and a PR review;
- each ticket's state and shipped status;
- five late instruction layers: the card comment, the notes, the checklist and two DM thread replies.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS. Data seeding: PASS.
- **Dynamic Change (strengthened):** the 21:16Z reply withdraws the 16:20Z checklist's Brian edit and narrows the 16:20Z rule 6 change. It sits in a different thread from the request.
- **Friction carried:** ZOM-312 is removed by a PR review comment; ZOM-258 is removed by the notes; Arthur's role comes from the notes.
- **Decoys carried:**
  - Brian's "+50% … every monster" and "the editor bits too";
  - Domino card #211;
  - the "Next pass" tab;
  - Vincent's channel request;
  - ZOM-281 having no PR;
  - "rage by level".

**Naturalness:** PASS. First person, lowercase and casual, with no document formatting, polished connectives or enumerated specs.

**Anti-Patterns:**

| Pattern | Status |
|---------|--------|
| Command List | PASS. One lowercase "then", with no "first" or "finally". The order follows Leonard's own condition ("reply here when it''s in the folder") |
| Bolt-On | PASS. Every sentence serves the baseline |
| Pre-Solving | PASS. No counts, tickets, statuses, exclusions, timings or causes are named |
| Tool Mention | PASS. "dm", "folder", "invite" and "tickets" are natural nouns |

**Diversity:** a two-tab sheet, folder placement, role-based sharing with three roles, a batch of Linear comments, and a DM reply over a source-defined cohort with a rules answer.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** FAIL (2). Fork Y is unresolved; every other fork is settled.
- **Y (new, strongest): the four listed keys vs every level editor ticket. UNRESOLVED.**
  - **What Leonard wrote:** "leave the level editor tickets off too (162, 163, 201 and 250), the designers keep their own list for those, so no comments on them either."
  - **The category is "the level editor tickets", and his reason covers the whole category.**
  - **ZOM-173, 277 and 315 fit the category on every record that describes them:**
    - ZOM-173 carries the Linear label "Level Editor" (base `/issues/3215/labels`). None of the four listed keys has that label; theirs are "Bug" or "Improvement";
    - ZOM-173's title says "Item Set Count **in editor**", the same phrase as listed ZOM-201 ("overlay **in editor**");
    - its duplicate ZOM-203 says "in the level editor UI";
    - its closing note puts it "in the level objects panel";
    - the ZOM-277 and ZOM-315 notes put them in "the editor''s stats panel … nothing changes in the game itself". That is the stats panel ZOM-250 ("attack power stats in level editor") built.
  - **Blake's mail treats the level editor as one stripped area.**
  - **Nothing ranks the list over the category.** No record says "only these" or that the other three stay. The newer-source, authority and source-identity checks don't separate the readings, because both come from the same message. Scope is the open question itself.
  - **This differs from the analytics/tutorial list (fork M).** There, the stated reason ("they don't change how hard a level plays") did not reach ZOM-378. Here the reason does reach ZOM-173, 277 and 315.
  - **The two answers:**
    - Reading A: 24 tickets, Editor only ZOM-173, 200, 277, 315, and 9 comments.
    - Reading Y: 21 tickets, Editor only ZOM-200, and 6 comments.

    The register rows, the DM total and Editor only keys, and three Linear comment writes all differ.
- **Z (new): Brian keeps edit per the checklist. Excluded.** The 21:16Z reply, later than the 16:20Z checklist and by the same author, says "scratch brian editing, robert will fix rows in the session. comment access is enough for brian".
- **AA (new): the 21:16Z reply isn't part of "his ask" because it sits under Julia's own message. Excluded.**
  - It is Leonard's, in the same DM, on the Tuesday the prompt names, and opens "one more for the baseline".
  - The parent shows reply_count 1, and thread reads are cataloged.
- **N (retested): drop all editor and debug tooling. Excluded.**
  - The new reply names level editor tickets, and Blake's mail lists the debug menu separately, so ZOM-200 isn't reached.
  - ZOM-202 is open, so it is Not shipped under rule 1.
  - Leonard's 20:07Z reply still asks for "the editor only ones", and N would leave that empty.
- **F (dropped):** "ZOM-250 Replaced by ZOM-277" no longer arises, because ZOM-250 is off the list.
- **B–E, G–X:** excluded on byte-identical rows, as last round, with the counts recomputed.

### Unique Ground Truth comparison

Unique Ground Truth: FAIL 2

Basis: Fork Y is unresolved. Leonard's 2025-09-30 21:16Z DM reply says to leave off 'the level editor tickets' because 'the designers keep their own list for those', then lists 162, 163, 201 and 250. ZOM-173, 277 and 315 are also level editor tickets by their titles and closing notes and by Blake's mail, and no record says whether the list is complete. Reading A (24 tickets, Editor only 173, 200, 277, 315, 9 comments) and Reading Y (21 tickets, Editor only 200, 6 comments) differ in the register, the DM counts and keys, and three Linear comment writes. Every other fork is settled: Brian commenter (Z) by 'scratch brian editing'; the thread reply counts (AA) by its author, day and 'one more for the baseline'; B-X as before, with counts recomputed; F is gone because ZOM-250 is now off the list.

Alternative selection: Revision 28 adds Julia's 9/29 DM question and Leonard's 9/30 21:16Z thread reply (four level editor tickets off, no comments on them, Brian comment not edit) and the PR \#401 updated\_at fix. New readings test each new instruction: Y (the category 'level editor tickets' vs the four listed keys), Z (Brian edit per the checklist vs the reply), AA (the thread reply outside the request thread). B-X are every earlier fork, recomputed on rows byte-identical to revision 25; F drops out because ZOM-250 is now off the list. N (all editor and debug tooling off) is retested against the new reply.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Follow the card as Leonard left it, his card comment, his 'notes for monday' doc attached to the card, his checklist and his Tuesday DMs (the request thread and his later reply in the thread under Julia's Monday question): scope is every difficulty ticket created up to Aug 31 by title word plus every ticket with Blake's 'tiers:' closing note (ZOM-221, 281, 300, 305, 378), minus a title match Blake marked 'not tiers' in his review on its PR (ZOM-312, PR match3d\#265), attack power counting only when written out (ZOM-271 out), minus the six analytics and tutorial tickets his DM reply lists, ZOM-258 from his notes and the four level editor tickets his later DM reply lists (ZOM-162, 163, 201, 250), which also get no comments; status against Blake's store builds mail; Replaced only where another ticket's closing note says so (ZOM-282 on ZOM-254); comments on ZOM-199, on Replaced ZOM-254 and, per the checklist's rule 6 change, on every Editor only and Not shipped ticket still on the list; share with the invite attendees, Robert as editor, Brian as commenter per Leonard's later DM reply, Leonard as commenter and Arthur as viewer per the notes; the Rules in force tab as before; the DM reply gives the total, per-status counts, the Not shipped and Editor only keys, which ticket replaced which, and when a new player gets their starting tier. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and the four level editor tickets Leonard lists, ZOM-162, 163, 201 and 250, off; ZOM-312 off as Blake's 'not tiers'; ZOM-378 and ZOM-281 on); ZOM-173, 200, 277 and 315 stay on as Editor only; ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-271 out; checklist rule 6 change in force for the tickets still listed: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); no comments on ZOM-162, 163, 201 or 250; reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280, 293; Leonard DM D05HB64NMQU. | 24 rows: the 35 rule-1 tickets (31 title matches without Duplicates ZOM-203 and ZOM-276 and without ZOM-312, which Blake marked 'not tiers' in his review on PR match3d\#265, plus tiers: tickets ZOM-221, 281, 300, 305, 378) minus the eleven Leonard leaves off (ZOM-30, 49, 50, 161, 262, 275 in his first DM reply, ZOM-258 in his notes for monday, and ZOM-162, 163, 201, 250 in his later DM reply); Live 16, Editor only 4, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force as the build runs them: starting tier set after the first 10 games played (wins and losses), average CPM above 90 to tier 1, everyone else tier 0 (90 exactly stays on tier 0); promotion and demotion in ZOM-42's wording: 80% or more over up to the most recent 10 attempts (the last 10 games played) promotes, one win on tier -2 promotes; demotion on a losing streak of 4 games in a row at any time or a win rate of 50% or lower over up to the last 10 games; the record resets after every promotion or demotion; after a demotion the level being played is replayed lower (below the new tier) until a win; enrage from the sheet Live tab copied as it stands: nine monster rows and MonsterBase 0.8/0.8 with their numbers, and Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP) as not copied yet; DM gives the total 24, the per-status counts, the keys of the Not shipped (ZOM-202, 280, 293) and Editor only (ZOM-173, 200, 277, 315) tickets, that ZOM-282 replaced ZOM-254, and that a new player gets their starting tier after their first 10 games (levels played), from the average CPM of those games. | CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 316-316): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; SHEET\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 26-26): "\["MonsterBase (base prefab)", "0.8", "0.8", "0"\], \["Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)", "not copied yet", "not copied yet", "0"\]"; TCOMMENT\_W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 79-79): "written out (ATK on its own doesn''t)"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 85-85): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; CARD\_R1B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''"; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 314-314): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 96-96): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"; DMT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "tell me when a new player gets their starting tier"; DECK\_PROMO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Promotion: win rate of 80% or more over the last 10 attempts moves you up one tier."; Z42MR (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we evaluate UP TO THE MOST RECENT 10 attempts of the player"; CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; Z42LAST (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we constantly look at the last 10 games played"; Z42STREAK (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "A losing streak of 4 games in a row can still trigger at any time"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"; Z42RESET (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "every time a promotion/demotion happens, the record is reset and we start at 0 games played"; WR\_DEM50 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/WinRateRule.cs lines 31-31): "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"; GL\_RETRY (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Match3D/Game/Levels/GameLoader.cs lines 101-101): "// Make sure we go down a tier for this level"; REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 92-92): "One more, for the rules tab: the starting tier check in the build is cpm &gt; 90, not &gt;= 90."; NOTES\_258 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays."; NOTES\_ART (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "arthur is only listening in on monday, view access is enough for him."; NOTES\_REPL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "when you reply to me, also tell me which ticket replaced which."; CARD\_R1NT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "It works the other way too: a title match Blake marked ''not tiers'' in his review on its PR stays off."; GH265RC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work"; DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "leave the level editor tickets off too (162, 163, 201 and 250)"; DMR2\_BR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "comment access is enough for brian" |
| B | match3d\#401 changed how enrage works (speed and damage split per monster, hp method dropped), so ZOM-282 is Replaced by match3d\#401 and gets a Replaced comment. | ZOM-282 Replaced by match3d\#401. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a Replaced comment on ZOM-282 naming match3d\#401. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-282. | Register shows ZOM-282 Replaced; DM counts Live 15, Replaced 2. | GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 62-62): "this gives enrage speed and damage their own values, they shared one since ZOM-282." |
| C | Comment on every listed ticket whose text the store builds contradict, including ZOM-42 (6-7 levels vs 10). | Correction comment also on ZOM-42. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a comment on ZOM-42. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-42. | Extra correction comment; register unchanged. | Z42A (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "gets assigned after the first 6-7 levels based on CPM" |
| D | Read the scope window in Pacific days with an Apr 21 start, dropping ZOM-23 (2025-04-21T04:51:38Z, Apr 20 PT); ZOM-30 is already off under Leonard's DM reply. | 23 tickets; ZOM-23 out. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Register 23 rows; DM total 23 and Live 15. | Z23 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3277): "2025-04-21T04:51:38Z" |
| E | Also post the register in \#zombie-design because Vincent asked Julia to drop it there. | Share with the invite and also post in \#zombie-design. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a Slack post in \#zombie-design. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus C090N54TG79. | Same register; extra channel post. | VINCENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 52-52): "julia when you have the difficulty list can you drop it in here too" |
| G | ZOM-254 was closed (2025-06-23) after ZOM-282 (2025-06-21) and its own QA note says blunder enrages the monsters, so ZOM-282 is not the 'later' ticket and ZOM-254 stays Live with no Replaced comment. | ZOM-254 Live; no Replaced ticket. | Same as A without the ZOM-254 comment. | Same as A without Linear ZOM-254. | Register shows ZOM-254 Live; DM counts Live 17, Replaced 0, and no replacement to report. | Z254C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 292-292): "checked on the dev build, blunder enrages the monsters on the board now" |
| H | Rule 5 asks for enrage as it works in the store builds today, so the three monsters the sheet has not copied are given what they actually run on in main: no own override, so MonsterBase's 0.8 speed / 0.8 damage. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same 24 rows and counts as A; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab, with Mailman, Mayor2 and PartyGirl given 0.8 speed / 0.8 damage (MonsterBase) instead of not copied yet; DM as A. | CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; MB\_ENRAGE (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/MonsterBase.prefab lines 342-343): "enrageSpeedPercentage: 0.8" |
| I | Fill the gap from the VarC prefabs the History tab says the Live tab was copied from: VarC-PartyGirl carries enragePercentage 0.6, so PartyGirl is 0.6 speed / 0.6 damage; Mailman and Mayor2 show no enrage value in their prefab text. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same 24 rows and counts as A; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab, with PartyGirl at 0.6 / 0.6 and Mailman and Mayor2 without numbers; DM as A. | SHEET\_HIST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 30-30): "\["2025-09-08", "Live tab copied from the VarC prefabs in main", "Julia"\]"; PG\_PREFAB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/VarC-PartyGirl.prefab lines 215-216): "propertyPath: enragePercentage" |
| J | Leonard's comment adds attack power in the title; ZOM-271's title says 'ATK POWER' / 'ATK Power', and 'ATK on its own' is read as ATK without 'power', so ZOM-271 (Done, June 16, card-profile stat display) is in scope as Live. | 25 tickets; ZOM-271 Live; otherwise as A. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 25 rows (adds ZOM-271); Live 17, Editor only 4, Replaced 1, Not shipped 3; DM total 25 and Live 17. | TCOMMENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 79-79): "attack power in the title counts too"; Z271 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3323): "Comprehensive Item Stat Display Rules also ATK POWER BUG. Also Change Damage sort to ATK Power sort" |
| K | Take the starting-tier window from the written rules (deck, ZOM-42, ZOM-199): average CPM over the player's first 10 levels read as ten distinct levels, so replays of a lost level don't count; &gt; 90 to tier 1, the rest tier 0. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register and counts as A; Rules in force and the DM answer give the starting tier as after the first 10 distinct levels (replays not counted), instead of after the first 10 games played (wins and losses) as the build counts them. | Z42S (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "1st 10 level avg CPM &gt; 90 (top 20%) moves to tier 1, rest stays in tier 0)"; DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0." |
| L | The 'Before Monday' checklist items are unchecked, so they are Leonard's pending notes, not rules in force; card rule 6 as written stands: comments only on ZOM-199 and ZOM-254, with the Not shipped and Editor only tickets left as they are. | Checklist not applied: two comments. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, leonard.hayes@ and brian.foster@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 and ZOM-254 only; reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. | Same 24 rows and counts; no comments on the seven Editor only and Not shipped tickets; brian.foster@ as commenter as in A. | CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CL\_NAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 81-81): "'Before Monday', '68daca5871dba40417a00383'" |
| M | ZOM-378 'Level 1 is removed and creates tutorial order problems' is a tutorial ticket, so it goes off the list with the other analytics and tutorial tickets Leonard named. | 23 tickets; ZOM-378 off. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 23 rows; Live 15; DM total 23 and Live 15. | DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3440): "It creates other important issues like wrong tutorials at the wrong spot." |
| N | Leonard's reason 'they don't change how hard a level plays' (repeated in his notes for ZOM-258) and Blake's 'players never see it' on ZOM-312 are the test, so every ticket that only touches editor or debug tooling is left off too (ZOM-162, 163, 173, 200, 201, 202, 250, 277, 315), with no comments on them. | Editor-tooling tickets off the list; no comments on them. | As A without the comments on the editor-tooling tickets. | As A without those Linear tickets. | 19 rows (ZOM-173, 200, 202, 277 and 315 off on top of ZOM-162, 163, 201, 250); no Editor only rows; DM without Editor only keys. | DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 98-98): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; NOTES\_258 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays."; GH265RC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work" |
| O | ZOM-281 is assigned to someone else (usr\_EMPLOYEE\_0032), so it isn't one of Blake's tickets and its 'tiers:' note doesn't bring it in; its title has none of rule 1's words, so it stays off the list. | 23 tickets; ZOM-281 out. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 23 rows; Live 15; DM total 23 and Live 15. | Z281 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "Win streak not lost when replaying without main menu" |
| P | No PR or commit in match3d names ZOM-281, so it counts as never merged and goes on the list as Not shipped, with the checklist's not-in-the-store-builds comment. | 24 tickets; ZOM-281 Not shipped; extra comment on ZOM-281. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a not-in-the-store-builds comment on ZOM-281. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-281. | Register shows ZOM-281 Not shipped; DM counts Live 15, Not shipped 4, and ZOM-281 among the Not shipped keys. | CARD\_R1NS (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "open, cancelled and never-merged ones are in, as Not shipped" |
| Q | Answer Leonard's starting-tier question from ZOM-42's line that players get assigned after the first 6-7 levels, and put that on the Rules in force tab. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 6-7 levels, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register and counts as A; Rules in force and the DM answer say a new player gets their starting tier after the first 6-7 levels. | Z42A (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "gets assigned after the first 6-7 levels based on CPM" |
| R | Use the written threshold from the deck and ZOM-199: average CPM of 90 or more starts a player on tier 1. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM of 90 or more to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register and counts as A; Rules in force (and any threshold in the DM answer) give 90 or more to tier 1, so 90 exactly goes to tier 1. | DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0." |
| S | Card rule 5 asks for promotion and demotion 'as they work in the store builds today'. The build's tier history is appended at the end and cleared on every tier change, and the win-rate check counts from index 0, so promotion and demotion are judged on the first 10 (and first 4) games since the last tier change, not the most recent ones. The Rules in force tab says that. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 24 rows: the 35 rule-1 tickets (31 title matches without Duplicates ZOM-203 and ZOM-276 and without ZOM-312, which Blake marked 'not tiers' in his review on PR match3d\#265, plus tiers: tickets ZOM-221, 281, 300, 305, 378) minus the eleven Leonard leaves off (ZOM-30, 49, 50, 161, 262, 275 in his first DM reply, ZOM-258 in his notes for monday, and ZOM-162, 163, 201, 250 in his later DM reply); Live 16, Editor only 4, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force as the build runs them: starting tier set after the first 10 games played (wins and losses), average CPM above 90 to tier 1, everyone else tier 0 (90 exactly stays on tier 0); promotion and demotion judged on the first games played since the last tier change, not the latest: 80% or more over the first 10 games on the tier promotes, on tier -2 only if the first game there is a win; 50% or lower over the first 10, or losing the first 4 games on the tier, demotes; a player who does neither in those games stays on the tier; enrage from the sheet Live tab copied as it stands: nine monster rows and MonsterBase 0.8/0.8 with their numbers, and Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP) as not copied yet; DM gives the total 24, the per-status counts, the keys of the Not shipped (ZOM-202, 280, 293) and Editor only (ZOM-173, 200, 277, 315) tickets, that ZOM-282 replaced ZOM-254, and that a new player gets their starting tier after their first 10 games (levels played), from the average CPM of those games. | CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; WH\_LOOP (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 46-46): "for (int i = 0; i &lt; gamesCount; i++)"; WH\_APPEND (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 160-160): "tierWinHistory += win ? "W" : "L";"; WH\_RESET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 26-26): "PlayerPrefs.SetString(TierWinHistoryKey, "");"; TM\_RULE (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 121-121): "WinHistory.GetWorstTierWinRatePossible(rule.NumGames) : WinHistory.GetBestTierWinRatePossible(rule.NumGames)" |
| T | Rule 5's go-by-the-build sentence now covers only the starting tier, so for demotion follow Robert's deck, the first write-up rule 5 names: demotion is 4 losses in a row only, with no 50%-or-lower rule; the window wording still follows ZOM-42. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 24 rows: the 35 rule-1 tickets (31 title matches without Duplicates ZOM-203 and ZOM-276 and without ZOM-312, which Blake marked 'not tiers' in his review on PR match3d\#265, plus tiers: tickets ZOM-221, 281, 300, 305, 378) minus the eleven Leonard leaves off (ZOM-30, 49, 50, 161, 262, 275 in his first DM reply, ZOM-258 in his notes for monday, and ZOM-162, 163, 201, 250 in his later DM reply); Live 16, Editor only 4, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force as the build runs them: starting tier set after the first 10 games played (wins and losses), average CPM above 90 to tier 1, everyone else tier 0 (90 exactly stays on tier 0); promotion and demotion in ZOM-42's wording: 80% or more over up to the most recent 10 attempts (the last 10 games played) promotes, one win on tier -2 promotes; demotion only on a losing streak of 4 games in a row (no 50%-or-lower rule); the record resets after every promotion or demotion; after a demotion the level being played is replayed lower (below the new tier) until a win; enrage from the sheet Live tab copied as it stands: nine monster rows and MonsterBase 0.8/0.8 with their numbers, and Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP) as not copied yet; DM gives the total 24, the per-status counts, the keys of the Not shipped (ZOM-202, 280, 293) and Editor only (ZOM-173, 200, 277, 315) tickets, that ZOM-282 replaced ZOM-254, and that a new player gets their starting tier after their first 10 games (levels played), from the average CPM of those games. | CARD\_R5WU (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself."; DECK\_DEM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Demotion: 4 losses in a row moves you down one tier." |
| U | Card rule 7 says everyone on the invite other than Robert comments, and the later checklist changes rule 7 only for Brian; Leonard's note that view access is 'enough' for Arthur sets a floor, not a cap, so Arthur still gets comment access. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian, Leonard and Arthur comment; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and brian.foster@, leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register, comments and DM; arthur.blake@ shared as commenter, not viewer. | CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 85-85): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; NOTES\_ART (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "arthur is only listening in on monday, view access is enough for him." |
| V | ZOM-258 'Icon for Enraged monster' is a rule-1 title match, and Leonard's later DM reply lists the tickets to leave off (30, 49, 50, 161, 262 and 275) without ZOM-258, so the DM list is his final exclusion list and ZOM-258 stays on as Live. | 25 tickets; ZOM-258 Live. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 25 rows; Live 17; DM total 25 and Live 17. | CARD\_R1W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "as a whole word in the title"; Z258 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3308): "Icon for Enraged monster"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays" |
| W | ZOM-312 'Delete Difficulty Tier and Reassign' is a title match. PR match3d\#265 is Blake's own PR, so his 'not tiers' line is a comment on his own code, not 'his review on its PR'; ZOM-312 stays on as Editor only and gets the checklist's not-in-the-store-builds comment. | 25 tickets; ZOM-312 Editor only with a comment. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a not-in-the-store-builds comment on ZOM-312. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-312. | 25 rows; Editor only 5 with ZOM-312 among the Editor only keys; DM total 25. | CARD\_R1W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "as a whole word in the title"; Z312 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3368): "Delete Difficulty Tier and Reassign"; PR265 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /pull\_requests/2147): ""title": "ZOM-312"" |
| X | The prompt says to reply with what Leonard asked for in the DM; the DM and its thread reply ask for the counts, the Not shipped and Editor only keys and the starting-tier timing, so the reply leaves out which ticket replaced which. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register, comments and shares; the DM gives the total, counts, keys and starting-tier timing without saying that ZOM-282 replaced ZOM-254. | DMC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "reply here when it''s in the folder with how many tickets made the list and how many of each status"; DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"; DMT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "tell me when a new player gets their starting tier" |
| Y | Leonard's later DM reply leaves off 'the level editor tickets' and gives the reason 'the designers keep their own list for those'. Blake's store builds mail defines level editor work (Assets/Scripts/LevelEditor and the LevelDesigner panels). ZOM-173, 277 and 315 are level editor tickets on the same footing as the four keys he lists: ZOM-173 carries the Linear label 'Level Editor' (none of the four listed keys does), its title says 'Item Set Count in editor' (ZOM-201's says 'overlay in editor'; ZOM-173's duplicate ZOM-203 says 'in the level editor UI'), its closing note puts it in the level objects panel, and the ZOM-277 and ZOM-315 notes put them in the editor's stats panel, the panel ZOM-250 ('attack power stats in level editor') created. So the parenthetical names examples, and all seven level editor tickets go off, with no comments; only ZOM-200 (debug menu) is left as Editor only. | 21 tickets: ZOM-173, 277 and 315 also off as level editor tickets, with no comments; ZOM-200 the only Editor only ticket; otherwise as A. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the four Editor only and Not shipped tickets ZOM-200, 202, 280 and 293 (the change isn't in the store builds); no comments on ZOM-162, 163, 173, 201, 250, 277 or 315; reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254, ZOM-200, 202, 280, 293; Leonard DM D05HB64NMQU. | 21 rows (24 minus ZOM-173, 277, 315); Live 16, Editor only 1 (ZOM-200), Replaced 1, Not shipped 3; DM total 21, Editor only key ZOM-200 only; rules tab as A. | DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "leave the level editor tickets off too (162, 163, 201 and 250), the designers keep their own list for those, so no comments on them either."; MAIL\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 98-98): "The level editor (Assets/Scripts/LevelEditor and the LevelDesigner panels), anything in an Editor folder and the debug menu (Assets/Scripts/Debug) are stripped from store builds."; Z173L (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3215/labels): "Level Editor"; Z173T (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3215): "Item Set Count in editor not updating with difficulty tier changes"; Z201T (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3246): "Also turn it into an overlay in editor while not obstructing game board."; Z203T (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3248): "The number of item sets in the level editor UI does not update when you switch between difficulty tabs"; Z173C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 260-260): "this one is the set count in the level objects panel"; Z277C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 306-306): "this is the average in the editor''s stats panel, nothing changes in the game itself"; Z315C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 354-354): "this is the total attack power in the editor''s stats panel, items without cardData now count with their base damage. nothing changes in the game itself"; Z250T (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3300): "Create faux level timer and add attack power stats in level editor" |
| Z | The 'Before Monday' checklist's rule 7 change ('Brian gets edit as well') is on the card the DM points to, so Brian keeps edit access. | Robert and Brian edit, Leonard comments, Arthur views; otherwise as A. | Same as A except brian.foster@ is shared as editor. | Same as A. | Same register, comments and DM as A. | CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 85-85): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session" |
| AA | Leonard's later message sits in the thread under Julia's own Monday question, not in his Tuesday request thread, so it is not part of 'his ask'; the register keeps ZOM-162, 163, 201 and 250 (Editor only, commented) and Brian keeps edit. | 28 tickets (Live 16, Editor only 8, Replaced 1, Not shipped 3); 13 comments; Robert and Brian edit, Leonard comments, Arthur views. | Same kinds of writes as A, plus comments on ZOM-162, 163, 201 and 250, and brian.foster@ shared as editor. | As A plus Linear ZOM-162, 163, 201, 250. | 28 rows; DM total 28 with Editor only keys ZOM-162, 163, 173, 200, 201, 250, 277, 315. | DMP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "leonard, anything you need from me before monday''s tuning session?"; DM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "julia before monday''s tuning session i want a baseline of the difficulty system from you" |

Explicit option inventory: The prompt lists no options; the status values sit in the incorporated card.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "build the register the way he set it up"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: EXCLUDED. Card rule 4 now makes a ticket Replaced only when another ticket's closing note says so and says PRs that change or split its numbers don't. match3d\#401 is a PR, and its comment describes a split of the shared value, not a replacement.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 62-62): "this gives enrage speed and damage their own values, they shared one since ZOM-282."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Live vs Replaced for ZOM-282. |
| writes | DIFFERENT | B adds a ZOM-282 comment. |
| destinations | DIFFERENT | B adds ZOM-282. |
| contents | DIFFERENT | Status cell and DM counts differ (Live 15 / Replaced 2). |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The quoted sentences exclude PRs and value splits by name; \#401's comment says it gives speed and damage their own values.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 62-62): "this gives enrage speed and damage their own values, they shared one since ZOM-282."

Compared alternative: C
Resolution: EXCLUDED. Card rule 6 limits Blake-sourced comments to tickets his mail or reply calls wrong (only ZOM-199 in the reply), and says ZOM-42 stays as it is even if its wording is a bit off; the checklist's rule 6 change adds only Editor only and Not shipped tickets, and ZOM-42 is Live.
Resolution evidence: CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 142-142): "ZOM-199 says &gt;= but the code never changed from the original spec"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | C decides ZOM-42 needs a comment. |
| writes | DIFFERENT | C adds one comment. |
| destinations | DIFFERENT | C adds ZOM-42. |
| contents | DIFFERENT | Extra comment text. |

Authority chain: P → DMR → CARD\_R6X

Resolution relevance challenge: The quoted sentences name ZOM-42 as staying as it is; the checklist change covers Editor only and Not shipped tickets, which ZOM-42 (Live) is not; the reply names only ZOM-199.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 142-142): "ZOM-199 says &gt;= but the code never changed from the original spec"

Compared alternative: D
Resolution: EXCLUDED. The scope has no start date (everything since ZM started), so ZOM-23 is in under any timezone; the next title match after Aug 31 is ZOM-517 on 2025-09-03.
Resolution evidence: CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; Z517 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3591): "2025-09-03T22:22:22Z"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | D drops ZOM-23. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rows and counts differ by one. |

Authority chain: P → DMR → CARD\_SCOPE

Resolution relevance challenge: The quoted scope removes the start-date edge; Z517 shows no ticket near the Aug 31 end.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; Z517 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3591): "2025-09-03T22:22:22Z"

Compared alternative: E
Resolution: EXCLUDED. The prompt and card both define the audience as the invite list; Vincent is not an attendee and his channel request is not part of Leonard's ask.
Resolution evidence: CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system before monday's tuning session. can you take it off my plate? go through his ask and everything it points to and build the register the way he set it up. put it in the zm difficulty folder and share it with everyone on monday's tuning invite. if his rules say something needs to happen on the tickets, go ahead and do that too. then reply to leonard in the dm with what he asked for. go with your read on the details, no need to check with me first"; CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 195-195): "VALUES ('evt\_91674a9c23d012a9ac34da', 'julia.lawson@harmonygames.co', 'ZM difficulty tuning'"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | E adds a channel post. |
| writes | DIFFERENT | E adds a Slack post. |
| destinations | DIFFERENT | E adds \#zombie-design. |
| contents | DIFFERENT | Extra post. |

Authority chain: P → DMR → CARD\_R7

Resolution relevance challenge: The prompt names the audience as the invite; the invite on Julia's calendar does not include Vincent.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system before monday's tuning session. can you take it off my plate? go through his ask and everything it points to and build the register the way he set it up. put it in the zm difficulty folder and share it with everyone on monday's tuning invite. if his rules say something needs to happen on the tickets, go ahead and do that too. then reply to leonard in the dm with what he asked for. go with your read on the details, no need to check with me first"; CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 195-195): "VALUES ('evt\_91674a9c23d012a9ac34da', 'julia.lawson@harmonygames.co', 'ZM difficulty tuning'"

Compared alternative: G
Resolution: EXCLUDED. Rule 4 now keys on another ticket's closing note, with no ordering condition. ZOM-282's closing note says it replaces the blunder 2.0 boost from ZOM-254; ZOM-254's QA note describes the dev build and is not a closing note on another ticket that replaces it. Close order no longer matters.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 316-316): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Replaced vs Live for ZOM-254. |
| writes | DIFFERENT | G drops the ZOM-254 comment. |
| destinations | DIFFERENT | G drops Linear ZOM-254. |
| contents | DIFFERENT | Status and DM counts differ (Live 17 / Replaced 0), and the DM has no replacement to report. |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The rule no longer says 'later', so close dates cannot reverse it; ZOM-282's note names ZOM-254 explicitly, which is what the rule asks for.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 316-316): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"

Compared alternative: H
Resolution: EXCLUDED. Rule 5 now says how to fill the enrage section: copy the sheet's Live tab as it stands, put a monster the sheet has not copied on the tab as not copied yet, and do not work numbers out from anywhere else. Deriving 0.8/0.8 for Mailman, Mayor2 and PartyGirl from MonsterBase inheritance in the repo is working numbers out from somewhere else. The later, more specific sentence in the same rule governs the store-builds clause for these rows; the copied numeric rows equal main (Eval 0 Check C), so the two clauses no longer pull apart.
Resolution evidence: CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; SHEET\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 26-26): "\["MonsterBase (base prefab)", "0.8", "0.8", "0"\], \["Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)", "not copied yet", "not copied yet", "0"\]"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and share list. |
| writes | SAME | Same spreadsheet, shares, Linear comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | Rules in force tab: three monsters as not copied yet (A) vs 0.8/0.8 (H). |

Authority chain: P → DMR → CARD\_R5C

Resolution relevance challenge: Not a strawman: H was the leading reading last round, and 'as they work in the store builds today' still sits in rule 5. The new sentence speaks to exactly this case, a monster the sheet hasn't copied, and names the required entry ('not copied yet') and forbids the derivation H needs.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."

Compared alternative: I
Resolution: EXCLUDED. Rule 5 says to copy the Live tab as it stands and not to work numbers out from anywhere else, so reading PartyGirl's old enragePercentage 0.6 out of its prefab is excluded; the code also no longer reads that field (Monster.cs declares only enrageSpeedPercentage and enrageDamagePercentage).
Resolution evidence: CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; MONSTER\_CS (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Monster/Monster.cs lines 87-88): "\[SerializeField\] private float enrageSpeedPercentage = 0.25f;"; PG\_PREFAB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/VarC-PartyGirl.prefab lines 215-216): "propertyPath: enragePercentage"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and share list. |
| writes | SAME | Same spreadsheet, shares, Linear comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | PartyGirl 0.6/0.6 vs not copied yet. |

Authority chain: P → DMR → CARD\_R5C

Resolution relevance challenge: The new rule 5 sentence forbids taking numbers from anywhere but the Live tab, which covers prefab text; the dead field is a second, independent reason.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted.
Challenge evidence: CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; MONSTER\_CS (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Monster/Monster.cs lines 87-88): "\[SerializeField\] private float enrageSpeedPercentage = 0.25f;"

Compared alternative: J
Resolution: EXCLUDED. Leonard's card comment now says attack power counts only when written out in the title and that ATK on its own doesn't. ZOM-271's title never spells out 'attack power'; it uses the abbreviation 'ATK POWER' / 'ATK Power'. 'Written out' sets the test (the words spelled in full), and the parenthetical names the abbreviation as what fails it, so ZOM-271 stays out. Every other ZOM title created up to Aug 31 with ATK or attack was checked: ZOM-246, 250, 263, 277 and 315 spell out 'attack power'; ZOM-21 ('Monster Attack Speed') has no 'attack power'.
Resolution evidence: TCOMMENT\_W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 79-79): "written out (ATK on its own doesn''t)"; Z271 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3323): "Comprehensive Item Stat Display Rules also ATK POWER BUG. Also Change Damage sort to ATK Power sort"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-271 out vs in (Live). |
| writes | SAME | Same spreadsheet, comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | One more register row; DM total 25 vs 24 and Live 17 vs 16. |

Authority chain: P → DMR → TCOMMENT\_W

Resolution relevance challenge: Not a strawman: ATK is the game's short form and ZOM-271 also says ATK POWER, so a reader could take 'ATK on its own' as 'ATK without power'. But 'written out' is the governing test and 'ATK POWER' is not attack power written out; the parenthetical illustrates the abbreviation failing that test rather than creating a second, looser one.
Delegation challenge: NOT_CLAIMED. No alternative scope is authorized.
Challenge evidence: TCOMMENT\_W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 79-79): "written out (ATK on its own doesn''t)"

Compared alternative: K
Resolution: EXCLUDED. Rule 5 asks for the tier rules as they work in the store builds today and says that for when a new player gets their starting tier, where a write-up and the build disagree, go by the build. The build buckets a player when total games reach 10, and total games are wins plus losses, so the window is the first 10 games played. Leonard's DM asks for the tier numbers 'as they are today', so the DM answer follows the same build fact. 'First 10 levels' read as level plays is the same answer; only 'ten distinct levels' differs, and the build clause excludes it.
Resolution evidence: CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; WH\_GAMES (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 147-147): "return GetTotalWins() + GetTotalLosses();"; DMNUM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "plus the tier and enrage numbers as they are today"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and share list. |
| writes | SAME | Same spreadsheet, shares, Linear comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | Starting-tier window on the Rules in force tab and in the DM answer: first 10 games played (A) vs first 10 distinct levels (K). |

Authority chain: P → DMR → CARD\_R5W

Resolution relevance challenge: Not a strawman: three records (deck, ZOM-42, ZOM-199) say 'first 10 level(s)'. The card's own criterion is how the rules work in the store builds, and the build code fixes the unit as games, wins and losses.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied.
Challenge evidence: CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; WH\_GAMES (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 147-147): "return GetTotalWins() + GetTotalLosses();"

Compared alternative: L
Resolution: EXCLUDED. The checklist is Leonard's later change to the same two rules on the same card: its items are labelled 'rule 6 change' and 'rule 7 change', stated as decisions with a reason ('he''ll fix rows during the session'), and were added at 16:20, after his 14:04 description update and his 15:41 'rest of the card stands' comment. Under Eval 1 §2.1 check 1 a later applicable update by the same author for the same issue and scope resolves the earlier sentence without announcing replacement. Leonard's 19:48 DM points to the card (which carries the checklist) and his 20:07 reply asks for the Not shipped and Editor only keys. An unchecked item is a to-do for the card owner ('Julia owns this one'), not a hedge; no record says the changes are pending or tentative.
Resolution evidence: CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 85-85): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; CL\_ACT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 87-87): "'addChecklistToCard', '2025-09-30T16:20:11Z'"; UPD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 77-77): "'updateCard', '2025-09-30T14:04:31Z'"; DMR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "the rules for the register are on the difficulty baseline card on the zm roadmap board"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Whether the checklist changes apply. |
| writes | DIFFERENT | L posts 2 Linear comments instead of 9. |
| destinations | DIFFERENT | L drops the seven Editor only and Not shipped tickets. |
| contents | DIFFERENT | Same register; the seven comments are missing. |

Authority chain: P → DMR → CL\_R6

Resolution relevance challenge: Not a strawman: the card description still literally says the Not shipped and Editor only tickets stay as they are and that everyone but Robert comments, and the items are unchecked. The quoted items name the exact rules they change and say what now happens; they post-date both the description and Leonard's 'rest of the card stands' comment, and come from the same author on the same card.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the later card change is applied.
Challenge evidence: CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; TCOMMENT\_S (Evals/task\_inputs/01\_Universe\_Inject.sql lines 79-79): "rest of the card stands."; CL\_ACT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 87-87): "'addChecklistToCard', '2025-09-30T16:20:11Z'"

Compared alternative: M
Resolution: EXCLUDED. Leonard's exclusion names its tickets in parentheses (30, 49, 50, 161, 262 and 275) and ZOM-378 is not among them. ZOM-378 is in scope as one of Blake's tier tickets, and his closing note says the fix lines the first levels up with their tier versions, which changes how hard those levels play, so Leonard's reason does not reach it either.
Resolution evidence: DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 384-384): "tiers: closing. level 1 is back in the list so the first levels line up with their tier versions again"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-378 on vs off. |
| writes | SAME | ZOM-378 is Live and gets no comment either way. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | One row fewer; DM total 23 and Live 15. |

Authority chain: P → DMX

Resolution relevance challenge: Not a strawman: ZOM-378's title says 'tutorial order problems' and its description is about tutorials. But the DM gives an explicit list, and the tiers: note quoted ties ZOM-378 to tier level versions, which is difficulty.
Delegation challenge: NOT_CLAIMED. No alternative scope is authorized.
Challenge evidence: DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 384-384): "tiers: closing. level 1 is back in the list so the first levels line up with their tier versions again"

Compared alternative: N
Resolution: EXCLUDED. Leonard's later DM reply removes only level editor tickets by name, and the reason he gives ('the designers keep their own list for those') is about level editor work, not debug tooling or unmerged work. Blake's mail names the debug menu separately from the level editor, so ZOM-200 (debug menu) is not reached; ZOM-202 is open and goes on as Not shipped under rule 1. Leonard's first reply still asks for 'the editor only ones', which N leaves empty. The narrower level-editor fork is tested separately as Y. The exclusion is scoped to 'the analytics and tutorial tickets' with their keys listed, and in the same message Leonard asks for the keys of the editor only ones, which only makes sense if they stay on the list; the checklist's rule 6 change also has Editor only tickets commented, and card rule 3 lists Editor only as a status. The newer 'doesn't change how hard a level plays' (ZOM-258 note) and 'players never see it' (ZOM-312 review) lines each name one ticket by key or PR; card rule 3 keeps an Editor only status and the checklist comments on Editor only tickets, so the list still holds them.
Resolution evidence: DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."; MAIL\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 98-98): "The level editor (Assets/Scripts/LevelEditor and the LevelDesigner panels), anything in an Editor folder and the debug menu (Assets/Scripts/Debug) are stripped from store builds."; DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"

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
Resolution evidence: CARD\_R1B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''"; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 314-314): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; LUSR\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /users/35): "arthur.blake@harmonygames.co"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | O drops ZOM-281. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rows and counts differ by one (23 / Live 15). |

Authority chain: P → DMR → CARD\_R1B

Resolution relevance challenge: Not a strawman: ZOM-281's assignee is another person and the old rule 1 wording tied scope to Blake's own tickets. The current rule 1 keys on the note, and the note's author id is Blake's.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R1B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''"; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 314-314): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; LUSR\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /users/35): "arthur.blake@harmonygames.co"

Compared alternative: P
Resolution: EXCLUDED. Card rule 3 makes Blake's store builds mail the authority for what is in the store builds and what counts as shipped. The mail says both store builds were cut from main on Sep 26 and everything difficulty related was merged long before that; it strips only level editor and debug code, and ZOM-281 (win streak on replay) is a gameplay fix. ZOM-281 is Done, completed 2025-06-27, and Blake's closing note says it was checked on the dev build. Rule 1's 'never-merged' covers work that never landed, not a Done ticket the shipped-authority calls merged.
Resolution evidence: CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 96-96): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that."; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 98-98): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 314-314): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; Z281D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "2025-06-27T09:56:19Z"; Z281 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "Win streak not lost when replaying without main menu"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Live vs Not shipped for ZOM-281. |
| writes | DIFFERENT | P adds a ZOM-281 comment. |
| destinations | DIFFERENT | P adds ZOM-281. |
| contents | DIFFERENT | Status cell, DM counts and Not shipped keys differ. |

Authority chain: P → DMR → CARD\_R3 → MAIL\_MERGED

Resolution relevance challenge: Not a strawman: a complete GitHub scan finds no 'ZOM-281' string, so an Agent looking for a merged PR finds none. The card names the mail as the shipped authority and the mail answers the question for difficulty work as a class.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 96-96): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that."; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 98-98): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 314-314): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; Z281D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "2025-06-27T09:56:19Z"; Z281 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "Win streak not lost when replaying without main menu"

Compared alternative: Q
Resolution: EXCLUDED. ZOM-42's 6-7 levels line is provisional ('to be defined later') and the same ticket's rule 1 gives the first 10 levels' average CPM; the deck and ZOM-199 also say first 10. Card rule 5 says that for when a new player gets their starting tier, where a write-up and the build disagree, go by the build, and the build buckets a player when total games reach 10. Leonard's DM asks for the tier numbers as they are today.
Resolution evidence: Z42TBD (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "to be defined later"; Z42S (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "1st 10 level avg CPM &gt; 90 (top 20%) moves to tier 1, rest stays in tier 0)"; DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; DMNUM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "plus the tier and enrage numbers as they are today"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Starting-tier timing on the Rules in force tab and in the DM answer: 10 games vs 6-7 levels. |

Authority chain: P → DMR → CARD\_R5W

Resolution relevance challenge: Not a strawman: ZOM-42 is the system ticket rule 4 sends to the rules tab, and its 6-7 sentence is the only text that answers 'when' in so many words. Its own 'to be defined later', its own rule 1, the deck, ZOM-199 and the build all give 10.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: Z42TBD (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "to be defined later"; Z42S (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "1st 10 level avg CPM &gt; 90 (top 20%) moves to tier 1, rest stays in tier 0)"; DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; DMNUM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "plus the tier and enrage numbers as they are today"

Compared alternative: R
Resolution: EXCLUDED. Blake's reply is written 'for the rules tab' and says the build checks cpm &gt; 90, not &gt;= 90, so 90 exactly stays on tier 0; card rule 5 asks for the starting tier 'as they work in the store builds today', and rule 6 has the ZOM-199 comment say what the build does; TierManager.cs line 93 is 'cpm &gt; 90.0f'. Rule 5's narrowed build clause covers when the starting tier is given, so the threshold rests on the rules-tab note and the opening clause.
Resolution evidence: REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 92-92): "One more, for the rules tab: the starting tier check in the build is cpm &gt; 90, not &gt;= 90."; REPLY90 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 142-142): "so 90 exactly stays on tier 0"; CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set (the ZOM-199 comment is in both). |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Threshold: above 90 vs 90 or more. |

Authority chain: P → DMR → CARD\_R5B

Resolution relevance challenge: Not a strawman: the deck and ZOM-199 both say 90 or more. Blake's reply, addressed to the rules tab, and the build say otherwise, and rule 5 asks for the starting tier as it works in the store builds.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 92-92): "One more, for the rules tab: the starting tier check in the build is cpm &gt; 90, not &gt;= 90."; REPLY90 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 142-142): "so 90 exactly stays on tier 0"; CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"

Compared alternative: S
Resolution: EXCLUDED. Card rule 5 (revision 22) now settles this item directly: 'For which games promotion and demotion look at, write it the way ZOM-42 words it.' ZOM-42 words the window as up to the most recent 10 attempts / the last 10 games played, with the record reset after every promotion or demotion, and says a losing streak of 4 in a row can still trigger at any time. The later, more specific sentence in the same rule governs the opening 'as they work in the store builds today' for this one item, the same way rule 5's enrage sentence governs the enrage rows (fork H). The code's first-10-since-the-last-change window is therefore not what the tab states.
Resolution evidence: CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; Z42MR (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we evaluate UP TO THE MOST RECENT 10 attempts of the player"; Z42LAST (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we constantly look at the last 10 games played"; Z42RESET (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "every time a promotion/demotion happens, the record is reset and we start at 0 games played"; Z42STREAK (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "A losing streak of 4 games in a row can still trigger at any time"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rules in force tab: promotion and demotion over the latest 10 (and 4 in a row at any time) vs over the first 10 and first 4 games since the last tier change. |

Authority chain: P → DMR → CARD\_R5PD

Resolution relevance challenge: Not a strawman: last round's deep recheck passes P1 and P2 raised it and it failed UGT. The new card sentence names exactly this item ('which games promotion and demotion look at') and names ZOM-42 as the wording to use, and ZOM-42 states the window in one consistent way across its promotion, demotion and streak paragraphs.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card names the wording to use.
Challenge evidence: CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; Z42MR (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we evaluate UP TO THE MOST RECENT 10 attempts of the player"; Z42STREAK (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "A losing streak of 4 games in a row can still trigger at any time"

Compared alternative: T
Resolution: EXCLUDED. Rule 5 opens by asking for promotion and demotion 'as they work in the store builds today', and the build has the 50%-or-lower demotion rule (WinRateRule.cs line 31). ZOM-42, the other write-up rule 5 names and the one it sends promotion/demotion wording to, has the same rule. The deck's demotion line omits it; it does not say there is no such rule, so there is no write-up/build disagreement for a tie-break to settle. Both demotion rules go on the tab.
Resolution evidence: CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; WR\_DEM50 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/WinRateRule.cs lines 31-31): "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"; CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; DECK\_DEM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Demotion: 4 losses in a row moves you down one tier."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rules in force demotion: two rules (4 in a row, or 50% or lower over up to the last 10) vs the 4-loss rule only. |

Authority chain: P → DMR → CARD\_R5B

Resolution relevance challenge: Not a strawman: the narrowed build clause no longer covers demotion, and the deck is a named write-up whose demotion line lists only the 4-loss rule. It is excluded because the deck is silent on the 50% rule rather than contrary, while the build and ZOM-42 both have it and rule 5 asks for the rules as they work in the store builds.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card names the wording to use.
Challenge evidence: CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; WR\_DEM50 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/WinRateRule.cs lines 31-31): "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"; DECK\_DEM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Demotion: 4 losses in a row moves you down one tier."

Compared alternative: U
Resolution: EXCLUDED. Leonard's notes for monday, attached to the card and written after the card text (doc 2025-09-30T15:47-15:51Z; card description updated 14:04:31Z), are 'three things for the register', and one of them is Arthur's access: he is 'only listening in', so 'view access is enough for him'. Rule 7's default for him is comment, so the line has no effect unless it lowers him to view. The later checklist (16:20:11Z) changes rule 7 only for Brian and says nothing about Arthur.
Resolution evidence: NOTES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "julia, three things for the register:"; NOTES\_ART (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "arthur is only listening in on monday, view access is enough for him."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 85-85): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; TATT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 89-89): "'notes for monday', '68daca5871dba40417a00383'"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Arthur viewer vs commenter. |
| writes | DIFFERENT | Different role on the arthur.blake@ share. |
| destinations | SAME | Same four shares. |
| contents | SAME | Same register and DM. |

Authority chain: P → DMR → NOTES → NOTES\_ART

Resolution relevance challenge: Not a strawman: 'enough' can be read as a floor. But the doc lists changes to the register setup, and 'only listening in' gives the reason he does not need to comment; reading it as a floor makes the instruction do nothing.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; Leonard's instruction is applied, not delegated.
Challenge evidence: NOTES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "julia, three things for the register:"; NOTES\_ART (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "arthur is only listening in on monday, view access is enough for him."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 85-85): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; TATT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 89-89): "'notes for monday', '68daca5871dba40417a00383'"

Compared alternative: V
Resolution: EXCLUDED. The notes name ZOM-258 and say to leave it off; the DM reply opens 'forgot one thing', which adds exclusions rather than replacing earlier ones, and no record puts ZOM-258 back. Both are Leonard's, and they cover different tickets, so both apply (scope check).
Resolution evidence: NOTES\_258 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays."; DMF (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "forgot one thing: leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275)"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-258 off vs Live. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rows 24 vs 25; Live 16 vs 17. |

Authority chain: P → DMR → NOTES → NOTES\_258

Resolution relevance challenge: The quoted note names the ticket by key; 'forgot one thing' marks the DM reply as an addition, so it cannot be read as the complete list.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; Leonard's instruction is applied, not delegated.
Challenge evidence: NOTES\_258 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays."; DMF (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "forgot one thing: leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275)"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"

Compared alternative: W
Resolution: EXCLUDED. Rule 1 asks for a title match Blake marked 'not tiers' in his review on its PR, and does not say the PR has to be someone else's. Blake left review rev\_8 on PR match3d\#265 (title 'ZOM-312'), and its review comment says 'not tiers ... leave it out when we list tier work'. So ZOM-312 stays off and gets no comment.
Resolution evidence: CARD\_R1NT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "It works the other way too: a title match Blake marked ''not tiers'' in his review on its PR stays off."; GH265REV (Evals/task\_inputs/01\_Universe\_Inject.sql lines 209-209): "'harmonygames-Games/match3d\#265\#rev\_8', 'harmonygames-Games/match3d\#265', 'EMPLOYEE\_0025\_GITHUB\_USERNAME', 'COMMENTED'"; GH265RC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work"; PR265 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /pull\_requests/2147): ""title": "ZOM-312""; GHU\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /users/6): ""name": "Arthur Blake""

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-312 off vs Editor only. |
| writes | DIFFERENT | W adds a ZOM-312 comment. |
| destinations | DIFFERENT | W adds Linear ZOM-312. |
| contents | DIFFERENT | Rows 24 vs 25; Editor only 4 vs 5; keys differ. |

Authority chain: P → DMR → CARD\_R1NT

Resolution relevance challenge: Rule 1 asks only for Blake's review on the ticket's PR. Review rev\_8 is authored by EMPLOYEE\_0025 (Arthur Blake) on PR \#265, and the comment is part of that review.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; Leonard's instruction is applied, not delegated.
Challenge evidence: CARD\_R1NT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "It works the other way too: a title match Blake marked ''not tiers'' in his review on its PR stays off."; GH265REV (Evals/task\_inputs/01\_Universe\_Inject.sql lines 209-209): "'harmonygames-Games/match3d\#265\#rev\_8', 'harmonygames-Games/match3d\#265', 'EMPLOYEE\_0025\_GITHUB\_USERNAME', 'COMMENTED'"; GH265RC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work"; PR265 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /pull\_requests/2147): ""title": "ZOM-312""; GHU\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /users/6): ""name": "Arthur Blake""

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

Compared alternative: Y
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. Leonard's 2025-09-30T21:16:42Z DM reply names a category ('the level editor tickets') and a reason that covers the whole category ('the designers keep their own list for those'), then lists four keys in parentheses. ZOM-173, 277 and 315 fit the category by every record that describes them: ZOM-173 even carries the Linear label 'Level Editor', its title says 'in editor', the same phrase as listed ZOM-201, and its duplicate ZOM-203 says 'in the level editor UI'; the injected closing notes put ZOM-173 in the level objects panel and ZOM-277 and ZOM-315 in the editor's stats panel, with 'nothing changes in the game itself'; Blake's mail treats the level editor as one stripped area. No record says the list is complete ('just these', 'only'), and none says the other three stay. Newer source, authority and source identity are the same message; scope is the very question. A reader can keep the list literal (24 tickets, 9 comments, Editor only 173, 200, 277, 315) or apply the category (21 tickets, 6 comments, Editor only 200). The ticket set, the counts and keys in the DM, and three Linear comment writes all differ.
Resolution evidence: DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "leave the level editor tickets off too (162, 163, 201 and 250), the designers keep their own list for those, so no comments on them either."; Z173L (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3215/labels): "Level Editor"; Z173T (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3215): "Item Set Count in editor not updating with difficulty tier changes"; Z201T (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3246): "Also turn it into an overlay in editor while not obstructing game board."; Z173C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 260-260): "this one is the set count in the level objects panel"; Z277C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 306-306): "this is the average in the editor''s stats panel, nothing changes in the game itself"; Z315C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 354-354): "this is the total attack power in the editor''s stats panel, items without cardData now count with their base damage. nothing changes in the game itself"; MAIL\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 98-98): "The level editor (Assets/Scripts/LevelEditor and the LevelDesigner panels), anything in an Editor folder and the debug menu (Assets/Scripts/Debug) are stripped from store builds."; DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-173, 277 and 315 on the list as Editor only vs off. |
| writes | DIFFERENT | Comments on ZOM-173, 277 and 315 vs none. |
| destinations | DIFFERENT | Linear ZOM-173, 277 and 315 touched vs not. |
| contents | DIFFERENT | 24 vs 21 rows; Editor only 4 vs 1; DM total and Editor only keys differ. |

Resolution relevance challenge: Not a strawman: the reason Leonard gives applies to every level editor ticket, and ZOM-173's title is worded the same as listed ZOM-201's. The parenthetical favours A, but it doesn't say the four are the only ones, and the earlier analytics/tutorial list was settled differently: there the stated reason ('they don't change how hard a level plays') didn't reach ZOM-378. Here the reason does reach ZOM-173, 277 and 315. Leonard's first reply asking for 'the editor only ones' doesn't settle it either, because ZOM-200 (debug menu, which Blake's mail lists apart from the level editor) stays Editor only under Y. 'go with your read on the details' gives permission to act, not a rule that picks one reading. The deep recheck's P1 pass called the parenthetical settling, citing Leonard's earlier ask for 'the editor only ones'. That ask is still met under Y by ZOM-200, and the parenthetical never says the list is closed, so it does not rule Y out.
Delegation challenge: NOT_CLAIMED. No source accepts either set; the prompt's 'go with your read' does not authorize two different registers and comment sets.
Challenge evidence: DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "the designers keep their own list for those"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; P (Evals/task\_inputs/04\_Prompt.txt): "go with your read on the details, no need to check with me first"

Compared alternative: Z
Resolution: EXCLUDED. Leonard's DM reply at 2025-09-30T21:16:42Z, after the checklist (added 16:20:11Z), takes back the checklist's rule 7 change for Brian: 'scratch brian editing, robert will fix rows in the session. comment access is enough for brian'. It is the same author and the same item, later in time, and it names the replacement role.
Resolution evidence: DMR2\_BR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "and scratch brian editing, robert will fix rows in the session. comment access is enough for brian"; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 85-85): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Brian editor vs commenter. |
| writes | DIFFERENT | Different role on the brian.foster@ share. |
| destinations | SAME | Same four shares. |
| contents | SAME | Same register and DM. |

Authority chain: P → DMR2\_BR

Resolution relevance challenge: Not a strawman: the checklist item is still on the card. But 'scratch brian editing' takes that item back by name and gives the reason (Robert fixes rows instead).
Delegation challenge: NOT_CLAIMED. Leonard's later instruction is applied, not delegated.
Challenge evidence: DMR2\_BR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "and scratch brian editing, robert will fix rows in the session. comment access is enough for brian"

Compared alternative: AA
Resolution: EXCLUDED. The prompt points to what Leonard DM'd on Tuesday about the baseline and asks for the reply in the DM. The 21:16:42Z message is Leonard's, in the same DM, on the same Tuesday, and opens 'one more for the baseline', so it adds to his baseline ask. Its place in a thread under Julia's Monday question doesn't change who wrote it or what it is about. Julia is a DM member, the parent shows reply\_count 1, and Slack thread reads are cataloged.
Resolution evidence: DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "one more for the baseline: leave the level editor tickets off too (162, 163, 201 and 250)"; P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | 28 vs 24 tickets; Brian's role. |
| writes | DIFFERENT | Four extra comments; different Brian role. |
| destinations | DIFFERENT | Linear ZOM-162, 163, 201, 250 touched vs not. |
| contents | DIFFERENT | 28 vs 24 rows and DM counts and keys. |

Authority chain: P → DMR2\_LE

Resolution relevance challenge: Not a strawman: the message is in a thread under Julia's own message, which a reader of the request thread alone would miss. But source identity (Leonard), timing (Tuesday, after the request) and subject ('for the baseline') tie it to the ask.
Delegation challenge: NOT_CLAIMED. No delegation claimed.
Challenge evidence: DMP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "leonard, anything you need from me before monday''s tuning session?"; DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "one more for the baseline"

Strongest-alternative challenge (Y): Y is the strongest alternative and is not excluded. Leonard names a category, gives a category-wide reason and lists four keys. Three more tickets are level editor tickets by their own titles and notes, and nothing says the list is exhaustive.
Challenge evidence: DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "leave the level editor tickets off too (162, 163, 201 and 250), the designers keep their own list for those, so no comments on them either."; Z173T (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3215): "Item Set Count in editor not updating with difficulty tier changes"; Z277C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 306-306): "this is the average in the editor''s stats panel, nothing changes in the game itself"; Z173L (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3215/labels): "Level Editor"

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

**Feasibility:** PASS (5). Every ask maps to a cataloged write or read, and the data exists under either reading. The fork is about which answer is right, not whether the task can be done.
- Thread replies are readable with `slack_conversations_replies` / `slack_read_thread`.
- Shares use `gdrive_share_file` with a role string.
- Comments use `linear_create_comment`.
- The comment batch (9 calls, or 6) and four shares are ordinary write volume over a source-defined cohort, not padding.

**Persona ACL Reachability:** PASS (5). Every scoped read is visible to Julia:
- DM D05HB64NMQU and both threads: she is a member, and the new thread's parent is her own message;
- Arthur's mails: her mailbox;
- the invite: her calendar;
- the folder: writer;
- the agenda doc and deck: reader;
- the notes doc: reader;
- the enrage sheet: owner.

GitHub, Linear and Trello are unscoped.

**Explicit Tool Mention:** PASS (5).

**Clarity & Specificity:** FAIL (2), Action Decision Ambiguity.
- The prompt incorporates Leonard's instructions ("go through his ask and everything it points to", "if his rules say something needs to happen on the tickets, go ahead and do that too").
- Under reading A the Agent posts comments on ZOM-173, 277 and 315. Under reading Y it posts none on them ("so no comments on them either").
- These are two reasonable readings with different write actions, and nothing in the prompt or the records picks one. "go with your read on the details" gives the Agent permission to act; it does not choose between them.
- Eval 1 §2.6 scores the write divergence here and §2.1 scores the end-state difference. The both-fair exception that bars double scoring covers only figure-only forks, and this fork changes writes.
- Every other instruction layer still changes a different item without conflict.
- A top-level DM message and a thread reply carry the same content to the same recipient (not a fork).

**Contrived / Unnatural:** PASS (5).
- The destination and audience are named the way the persona knows them.
- No staged typos, opaque IDs, exact timestamps, trap hints, riddles, audit wording or if-chains.
- "if his rules say something needs to happen on the tickets" is one conditional, and the rule it points to lives on the card.

**Alignment with Today's Date:** PASS (5).
- "tuesday" resolves to 2025-09-30: the DM is at 19:48:26Z (12:48 PT) and the thread replies at 20:07:18Z and 21:16:42Z (14:16 PT).
- "monday's tuning session/invite" resolves to 2025-10-06T17:00Z (10:00 PT).
- The new records are dated 2025-09-29 and 2025-09-30, before the clock. The PR #401 value is 2025-08-25.

**Originality:** N/A (no comparison samples supplied).

**Truthfulness:** PASS (5). Premises PR1–PR5 are re-verified against revision 28; the DM, folder, card and invite rows keep their keys, authors and times:
- Leonard's Tuesday DM exists;
- the Monday session and its invite exist;
- the ZM Difficulty folder is unique;
- Leonard's rules are on the card the DM names.

**Tool Use & Cross-service:** PASS (5). Each service changes a graded fact:
- **Slack:** ten tickets off, Brian's role, the reply's key lists, the starting-tier question;
- **Linear:** the cohort, states, Replaced trigger, ZOM-42's wording;
- **Trello:** the rules and the comment set;
- **Docs (notes):** ZOM-258, Arthur's role, the replacement line;
- **Gmail:** shipped vs Editor only, the cpm rule;
- **GitHub:** ZOM-312 out, the starting window, the demotion rules;
- **Sheets:** enrage;
- **Calendar:** the share list.

Writes span Sheets, Drive, Linear and Slack.

**Investigation + Action:** PASS (5). **Coherence (Bolt-on):** PASS (5). **Business Function:** PASS (5), Product. **Complexity Dimensions & Data Seeding:** PASS (5).

---

### Phase 3: Universe Feasibility

**Data Existence:** PASS (5). Every needed entity is verified and retrievable through cataloged reads.

**Cross-Service Coherence:** PASS (5). No inconsistency in task-touched data.
- **PR match3d#401 (fixed).**
  - The UPDATE (physical line 137) sets `updated_at` to 2025-08-25T17:02:28Z, which equals the injected comment `#c_2` (line 134) and timeline `#ev_7` (line 136).
  - state, merged, merged_at and closed_at (16:42:14Z) are untouched.
  - A comment after merge on a closed PR is normal in the base.
  - Last round's only Coherence finding is closed.
- **New thread (lines 56 and 58).**
  - Both authors are members of the IM.
  - The parent's reply_count 1, reply_users_count 1 and latest_reply match the single reply; the reply's thread_parent_id and thread_ts_legacy match the parent.
  - Times follow the other records: Julia's question (9/29 21:38Z) comes after the invite was created (9/29 18:24:51Z), and the reply (9/30 21:16Z) comes after every other instruction.
  - Apostrophes are doubled (`monday''s`).
- **No conflict between the new reply and the records.**
  - Its four keys are Done level-editor tickets whose injected notes ("closing. works on the dev build") don't contradict it.
  - "scratch brian editing" is a later correction of the checklist by its author, not a contradiction.
  - The open scope of "the level editor tickets" is an instruction ambiguity (scored in Phase 2), not a data inconsistency.
- **Unchanged rows:** REUSED (byte-identical) from the revision-25 round and the same-hash `0_injection.md`: notes doc, PR #265 review, card description, checklist, first thread reply, closing notes, ZOM-281, ZOM-282 naming ZOM-254, and Slack authors as channel members.
- **Known base-data issues (not scored):** none touched; the task uses no Snowflake or Confluence data.
- **Not task-touched (not scored):** `Monster.cs` passes a single `enrageDamagePercentage`. Keep rubric rows off stacking behaviour.
- **Injection SQL considered:** Yes. Static integrity evidence: REUSED from `0_injection.md` (same hash `cd185b05…95`, checks A–B). The task-relevant Check C items were redone above.

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|-----------|--------------|-------------|---------------|
| Prompt | Unique Ground Truth | 2 | Fork Y unresolved: "the level editor tickets (162, 163, 201 and 250)" vs ZOM-173, 277 and 315, which are also level-editor-only; 24 vs 21 tickets, 9 vs 6 comments |
| Prompt | Feasibility | 5 | All asks cataloged; data exists |
| Prompt | Persona ACL Reachability | 5 | Every scoped read visible to Julia, including the new thread |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 2 | Action Decision Ambiguity: comments on ZOM-173, 277 and 315 under one reading, none under the other |
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
| Universe | Cross-Service Coherence | 5 | PR #401 date fixed; new thread consistent |

---

### Issues Found

| # | Issue | Severity | Dimension |
|---|-------|----------|-----------|
| 1 | Leonard's new DM reply (SQL line 58) says "leave the level editor tickets off too (162, 163, 201 and 250), the designers keep their own list for those". ZOM-173 (Linear label "Level Editor", title "Item Set Count in editor…", note "the level objects panel"), ZOM-277 and ZOM-315 (notes "the editor''s stats panel … nothing changes in the game itself") are also level editor tickets, and no record says whether the list is complete. The ticket set (24 vs 21), the DM counts and Editor only keys, and three Linear comments depend on it | Major | Unique Ground Truth |
| 2 | Same fork: comments on ZOM-173, 277 and 315 are posted under one reading and not under the other | Major | Clarity & Specificity |

### Recommended Improvements

1. **Required: close fork Y in the SQL (line 58).** Two ways:
   - **(a) Keep the answer at 24.** Make Leonard's list explicitly complete and drop the category label, so his words cover only the four keys. For example, have him name the four keys and say they are the only ones to leave off. Don't call them "the level editor tickets" or give a reason that covers every editor ticket. ZOM-173, 277 and 315 then stay Editor only with comments.
   - **(b) Leave the category and list all of it.** Name ZOM-162, 163, 173, 201, 250, 277 and 315. The answer becomes 21 tickets, Editor only 1 (ZOM-200), and 6 comments. Before choosing (b), decide about ZOM-202 ("Minimize or migrate selection panel…", In Progress, "wip on a branch, nothing merged yet"). It is level-editor panel work too, so a category-based reader could drop it as well. Option (a) avoids that question.

   Changing the SQL outdates every pass that reads it, so rerun /injection, /prompt, /hardness, /oe and /rubric, in that order.
2. **Bring the OEs and rubric to the new answer before /oe and /rubric.** Under option (a):
   - **Scope:** 24 tickets. ZOM-30, 49, 50, 161, 262, 275, ZOM-258, ZOM-312 and ZOM-162, 163, 201 and 250 are off; ZOM-281 and ZOM-378 are on; ZOM-271 is out.
   - **Counts:** Live 16, Editor only 4 (ZOM-173, 200, 277, 315), Replaced 1 (ZOM-254, replaced by ZOM-282), Not shipped 3 (ZOM-202, 280, 293).
   - **Comments (9):**
     - ZOM-199: the build checks cpm > 90;
     - ZOM-254: replaced by ZOM-282;
     - ZOM-173, 200, 277, 315, 202, 280 and 293: the change isn't in the store builds.

     ZOM-162, 163, 201, 250, ZOM-42, ZOM-281, ZOM-258 and ZOM-312 get none.
   - **Shares:** robert@ can edit; brian.foster@ and leonard.hayes@ can comment; arthur.blake@ can view.
   - **DM reply:** the total 24, the per-status counts, the Not shipped and Editor only keys, that ZOM-282 replaced ZOM-254, and when a new player gets their starting tier.
3. **Rules in force tab grading (unchanged):**
   - starting tier after the first 10 levels / 10 games played, above 90;
   - ZOM-42's window wording;
   - both demotion rules;
   - one win promotes on tier -2;
   - the level drops after a demotion (not by how much);
   - Mailman, Mayor2 and PartyGirl (incl. PartyGirl 50HP) as not copied yet.
4. **Don't grade ticking the checklist items** or a "rage by level" tab.
5. **Optional wording, carried from earlier rounds:** "then reply to leonard in the dm…" could follow Leonard's own condition ("once it's in the folder, reply…"). If you change it, put it in your own voice; prompts are screened for AI-written text. A prompt change outdates every pass that reads the prompt.

---

## Deep Recheck

Passes: P1, P2, P3 and P4 on Opus 5.5 (claude-opus-5-5), session effort. Each ran as a fresh subagent, blind to the main review. They started while the check record was being finished and never saw it or any finding. Every cited record was reopened in the main session.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 7 sentences; Leonard's three DMs, card rules 1–7, card comment, checklist, notes, Blake's mails, agenda | 1 finding, 23 forks | 0 findings (its fork F2 is the main review's fork Y, kept as unresolved) |
| P2 | 7 sentences | 4 | 0 |
| P3 | 7 sentences; full SQL static checks | 2 | 0 |
| P4 | 7 sentences | 1 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| P1-DR1 | P1 | "then reply to leonard in the dm with what he asked for." | DM 6f77386… "tell me when a new player gets their starting tier"; card rule 5; `TierManager.cs` "if (totalGames == 10)", "cpm > 90.0f" | §2 contents | Clarity | REJECTED | Card rule 5 settles it: "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build." The build gives one answer: after 10 games played, from their average CPM, above 90 to tier 1. Whether the reply also states the threshold is a rubric acceptance question, not a fork |
| P1-F2 | P1 | "build the register the way he set it up." | DM 5f6ed4d5… "leave the level editor tickets off too (162, 163, 201 and 250)"; DM 33c941fa… "the editor only ones" | §2 set | Unique Ground Truth | CONFIRMED (as the main review's fork Y; P1's settlement rejected) | P1 called the closed list settled because the earlier ask for "the editor only ones" would be emptied. Under Y, ZOM-200 (debug menu) is still Editor only, so that ask still has content. The parenthetical never says the list is closed. Nothing quoted rules out Y, and ZOM-173's Linear label "Level Editor" (base `/issues/3215/labels`), which P1 itself noted, supports it |
| P2-DR1 | P2 | "if his rules say something needs to happen on the tickets, go ahead and do that too." | SQL comments "parking this, nothing merged yet" on ZOM-400, 427, 438, 439, 441, 443, 458, 468, about 30 days after each issue's `updated_at` | §3 date-slip | Cross-Service Coherence | REJECTED | Byte-identical to revision 25 and rejected there on the same records. All eight are open Todo issues with `updated_at` = `created_at`, outside the register scope. The base has no Linear comments, so there is no convention of comments moving `updated_at`. No graded value depends on them |
| P2-DR2 | P2 | "leonard dm'd me on tuesday asking for a baseline…" | base `slack/messages/D05HB64NMQU/2025-08.json` Turkish messages vs the injected English DMs | §3 | Cross-Service Coherence | REJECTED | A language change between months is not a field, reference, date, state or ID inconsistency in any QC category. No record contradicts another |
| P2-DR3 | P2 | "go through his ask and everything it points to…" | `match3d#265#rev_8` submitted 17:50:12Z, listed after base rev_7 (18:01:21Z) | §3 | Cross-Service Coherence | REJECTED | Carried from revision 25. The base has no review `seq`, 3 base PRs already list reviews out of time order, and PR `updated_at` 18:01:36Z is later than the review |
| P2-DR4 / P3-DR2 | P2, P3 | (decoy card #211) | SQL action `683dbef4991df7f0987ddb73` board name "Product Roadmap" vs board `65eb4ec5…` "DD Product Roadmap" | §3 | Cross-Service Coherence | REJECTED | 2,084 base Trello action payloads for this board id use "Product Roadmap" and only the board record says "DD Product Roadmap" (stream count of `trello/data.json`). The SQL follows the base convention |
| P3-DR1 | P3 | (SQL overlay) | 8 columns missing from the unverified schema snapshot (slides `notes`, `table_json`, `ordinal`; GitHub review `seq`, review comment `seq`/`pull_request_review_id`/`side`/`subject_type`; linear_comments `sequence`) | P3 SQL | Injection schema | REJECTED | This is Eval 0 advisory G1, carried. `schema/README.md` treats a missing snapshot column as a provisional advisory, not a defect, and no graded value depends on it |
| P4-DR1 | P4 | "then reply to leonard in the dm with what he asked for." | prompt text | §6.6 | Command List | REJECTED | One lowercase "then" with no "first" or "finally" and no procedure. The order follows Leonard's own "reply here when it''s in the folder" |

Effect on verdict: unchanged by the passes. The main review's fork Y (Unique Ground Truth 2, Clarity 2) stands, now with ZOM-173's "Level Editor" label added as evidence.

Fork list:
- F-Y: **open** | ZOM-162, 163, 201 and 250 off; ZOM-173, 277 and 315 stay Editor only with comments (24 tickets, 9 comments) | ZOM-173, 277 and 315 also off as level editor tickets with no comments (21 tickets, Editor only ZOM-200, 6 comments) | Missing: a dated, persona-visible Leonard line saying the four keys are the complete list (or naming the other three), for example in DM 5f6ed4d5ae1a0a04b616af6d6d2dda43 itself
- F-Z: settled | Brian commenter | Brian editor (checklist) | Settled by: "and scratch brian editing, robert will fix rows in the session. comment access is enough for brian" (2025-09-30T21:16:42Z, after the 16:20:11Z checklist)
- F-AA: settled | The 21:16Z thread reply is part of Leonard's ask | Ignore it (it sits under Julia's message) | Settled by: "one more for the baseline" by Leonard in the same DM on the Tuesday the prompt names; parent reply_count 1
- F-N: settled | Only level editor tickets are removed | All editor and debug tooling off (ZOM-200, 202 too) | Settled by: Blake's mail naming "the debug menu (Assets/Scripts/Debug)" apart from the level editor; rule 1 "open … ones are in, as Not shipped" (ZOM-202 "wip on a branch, nothing merged yet")
- F-F: no longer a fork | ZOM-250 Replaced by ZOM-277 | — | ZOM-250 is off the list under every reading
- F-L (P1 F1): settled | Checklist rule 6 change in force | Card rule 6 as written | Settled by: "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds" (16:20:11Z, after "rest of the card stands" at 15:41:55Z); the 21:16Z reply's "so no comments on them either" treats it as live
- F-W: settled | ZOM-312 off | On as Editor only | Settled by: card rule 1 "a title match Blake marked ''not tiers'' in his review on its PR stays off"; PR #265 rc_7 "not tiers: …"
- F-V: settled | ZOM-258 off | On as Live | Settled by: notes "leave ZOM-258 off the list."
- F-U: settled | Arthur views | Arthur comments | Settled by: notes "arthur is only listening in on monday, view access is enough for him."
- F-X: settled | DM says ZOM-282 replaced ZOM-254 | DM leaves it out | Settled by: notes "when you reply to me, also tell me which ticket replaced which."
- F-S (P1 F14): settled | Window in ZOM-42's wording | The code's first games since the last change | Settled by: rule 5 "For which games promotion and demotion look at, write it the way ZOM-42 words it."
- F-T (P1 F13): settled | Demotion: 4 in a row, or 50% or lower | 4 in a row only | Settled by: `WinRateRule.cs` "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"; ZOM-42 "50% or lower"
- F-Q/K (P1 DR1): settled | Starting tier after 10 games played | After 6-7 levels / 10 distinct levels | Settled by: rule 5 "go by the build"; `TierManager.cs` "if (totalGames == 10)"; `WinHistory.cs` "return GetTotalWins() + GetTotalLosses();"
- F-R (P1 F15): settled | cpm > 90 | 90 or more | Settled by: Blake "the starting tier check in the build is cpm > 90, not >= 90"
- F-O/P (P1 F6): settled | ZOM-281 in, Live | Out / Not shipped | Settled by: "tiers: closing. checked on the dev build"; Blake "everything difficulty related was merged long before that"
- F-M (P1 F4): settled | ZOM-378 on | Off as tutorial | Settled by: "(30, 49, 50, 161, 262 and 275)" plus the reason "they don''t change how hard a level plays", which doesn't reach ZOM-378 ("tiers: … line up with their tier versions again")
- F-J (P1 F3): settled | ZOM-271 out | In | Settled by: "written out (ATK on its own doesn''t)"
- F-H/I (P1 F16): settled | Enrage Live tab as it stands | Derived values | Settled by: rule 5 "Copy its Live tab as it stands … don''t work numbers out from anywhere else."
- F-B/G (P1 F11): settled | ZOM-254 Replaced by ZOM-282; ZOM-282 Live | Other Replaced readings | Settled by: ZOM-282 note "this replaces the blunder 2.0 boost from ZOM-254"; rule 4 "PRs that change or split its numbers don''t"
- F-C (P1 F19): settled | No comment on ZOM-42 | Comment on ZOM-42 | Settled by: rule 6 "Every other ticket stays as it is, ZOM-42 … included"
- F-D (P1 F23): settled | ZOM-23 in | Out | Settled by: scope "so everything since we started ZM"; no ticket sits on the Aug 31 boundary
- F-E (P1 F21): settled | Share with the invite only | Also post in #zombie-design | Settled by: prompt "share it with everyone on monday's tuning invite"
- P1 F7–F10, F12: settled as P1 quotes them: ZOM-200 Editor only ("Done or not"); ZOM-45 and ZOM-288 Live; ZOM-173 Editor only (the level model changes are ZOM-307's); ZOM-263 Live; ZOM-303 Live with the level drop (`GameLoader.cs`)
- P1 F17, F20: not forks | One combined "not copied yet" row or one row per monster; the DM reply as a thread reply or a top-level message | Same values, recipient and content; the rubric must accept either layout and either placement

Platform defects: none.

### FINAL VERDICT: FAIL

Score: 2

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Next action: Close fork Y in SQL line 58 (Recommended Improvement 1). Either make Leonard's four keys an explicitly complete list without the "level editor tickets" label, or list every level editor ticket. Then send /injection, /prompt, /hardness, /oe and /rubric, in that order. Bring the OEs and rubric to the resulting answer (Recommended Improvement 2).

Evidence limits: The Evals/Docs PDFs were not re-extracted; Eval 1's restated bands and overrides were applied. Runtime acceptance of the `commenter` and `reader` share roles is unverified (declared parameters only). Eval 0 checks A–B were reused from the same-hash 0_injection.md, because this portal never writes the gate manifest. Byte-identical SQL rows reuse prior /prompt facts under stage-evidence-v1. The schema snapshot is unverified (G1).

**Lowest Dimension:** Unique Ground Truth, 2 (with Clarity & Specificity, 2). Leonard's new DM reply removes "the level editor tickets" but lists only 162, 163, 201 and 250. ZOM-173 (Linear label "Level Editor"), ZOM-277 and ZOM-315 are also level-editor-only, so the register is 24 or 21 tickets, the comments 9 or 6, and the DM's Editor only keys differ.

**Summary:** The prompt is unchanged, and the PR #401 date fix brings Cross-Service Coherence back to 5. Leonard's new thread reply settles Brian as a commenter and removes four named tickets. Its wording ("the level editor tickets", "the designers keep their own list for those") also reaches ZOM-173, 277 and 315, which leaves two defensible ticket sets and comment batches, so the prompt fails until the reply's list is closed or completed.

Eval version: task-quality-v1

Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e

Reviewed prompt SHA-256: 22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787

Review context SHA-256: e260e8f90d2cd3ba534532e3c94628508af4892bf092a4f28a01f20bda512e19

Prompt record SHA-256: 83ef6a69e7d4ea4146f0c1b026446812296feb2037c077d3c9004870626f8b2c
