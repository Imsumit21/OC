## PROMPT EVALUATION REPORT

### Task: Julia delegates Leonard's ZM difficulty baseline. The Agent builds the register (Tickets + Rules in force) from the Trello card rules, Leonard's card comment, his "notes for monday" doc, the "Before Monday" checklist and his Tuesday DMs (both thread replies), using Blake's store builds mail and his reply to it. It then files the register in ZM Difficulty, shares it with the Monday invite, comments on tickets per rule 6 as changed (with the two store builds on the Editor only and Not shipped comments), and replies to Leonard in the DM.
### Assigned Persona: Julia Lawson - Product Manager (roster `julia_lawson`, julia.lawson@harmonygames.co)
### Assigned Business Function: Product
### Assigned Competency: Engineering Ops
### Assigned Task Skill: Retrieval
### Assigned Horizon: long-horizon (Task Type field; Difficulty Mode "medium" recorded as context)

Review: `/prompt`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode. Actual review date 2026-10-31. Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe `Universe_SynthCut` (hg4-synth-sep30cut v16). Eval release task-quality-v1 (manifest SHA-256 `0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e`, verified with `hg_eval_release.py snapshot prompt`).

Binding:
- Reviewed prompt SHA-256: `22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787`
- Review context SHA-256: `15bb8b89d397e407ec743314852cc4edd30595f2c85b237c785083869a5c926c`
- Prompt record SHA-256: `764896e09a3104929bbb01f6f16ddd3988a7b5ce0765ab2aee7517dacd3fba38` (policy prompt-source-checks-v2, format 2)

Inputs:
- `04_Prompt.txt`: revision 43 (attached as `04_Prompt (12).txt`), 525 bytes, sha256 `22f26066…1787`. Byte-identical to the prompt graded last round (revision 31).
- `00_Task_Assigned_Inputs.md`: all five fields stated; intake clear.
- `01_Universe_Inject.sql`: revision 42, 97,366 bytes, 393 lines, sha256 `7966b1496ad972ff3cb125f922660304d110b4ad9b7004e1c40ed9feed20c5b8`. Changed since the revision graded last round (revision 30, `dd7536cd…1c`):
  1. Line 54 (Leonard's 20:07:18Z reply in his request thread) adds: "and when you comment on the editor only and not shipped ones, put the two builds in the comment (ios 0.3.49 and android 0.3.133) so people can see what you checked against".
  2. Card rule 3 (line 69, and the updateCard action line 77) now reads "What is in the store builds and what counts as shipped: Blake''s store builds mail and his reply to it."
  3. Blake's editor-strip paragraph left the 09:12:44Z "store builds for monday" mail. His 13:26:05Z mail moved into its own thread (5 mailbox copies; Julia's copy line 134, thread row line 132) with the subject "editor stuff and ZOM-199, before Monday". It keeps In-Reply-To / References to the first mail and opens "Two things I left out of the mail this morning." It carries (1) the editor/debug strip rule and (2) "the starting tier check in the code is cpm > 90, not >= 90, and it runs when a player''s 10th game ends, wins and losses both counted, not after 10 levels cleared. ZOM-199 says >= 90 after the first 10 levels, but the code never changed from the original spec, so 90 exactly stays on tier 0."
  4. Physical line numbers from line 94 onward shifted. Every SQL anchor in the check record was re-found by content at its new line (0 misses after updating the three changed mail quotes).
- No error/async config, dynamic context or reference files were supplied, and the prompt references none. A saved Agent trajectory, OEs and rubric exist in the workspace; under stage ownership none were opened.
- Evidence contract `stage-evidence-v1`.
  - **Reused:** facts from the prior `1_prompt.md` that rest on byte-identical SQL rows or base records: ticket scope, Linear states, closing notes, the deck, ZOM-42, the build files, the enrage sheet, the card comment, checklist, notes doc, PR #265 and #401, the invite, the folder, the agenda, and Leonard's 21:16Z reply.
  - **NEW:** the three changed instruction texts, their effect on every fork (new AB, AC, AD, AE; Q/K, R and L retested), a base read of ZOM-199 (`/issues/3243`), a base Gmail check that no other "store builds" mail from Blake exists, the requirement ledger, Clarity, and the deep recheck.

**What this round changes.** The answer stays 24 tickets and 9 comments. Two things are added. The seven Editor only and Not shipped comments must now name the two store builds (iOS 0.3.49, Android 0.3.133). And Blake's reply, which gives the Editor only rule and the ZOM-199 correction, is now a separate Gmail thread under a new subject. Card rule 3's "and his reply to it", the mail's opening line and its In-Reply-To header tie it to the store builds mail, so it isn't a fork, but the Agent has to find it outside the first thread.

---

### Injection Gate
- **State:** NEVER_REVIEWED. The gate reads `reports/input_manifest.json`, which this portal's report writer never creates.
- **Eval 0 handling:** `0_injection.md` (injection-static-v2, review date 2026-10-31) reviews the identical SQL hash `7966b149…20c5b8` (revision 42): **FINAL VERDICT: PASS**, COMPLETE. Re-ran `hg_injection_lint.py --summary` on the saved SQL here: 0 FAIL / 0 CHECK / 0 INFO. Its static checks A–B are REUSED. The Check C items this prompt depends on were redone here (Phase 3).
- **Reviewed SQL sha256:** `7966b1496ad972ff3cb125f922660304d110b4ad9b7004e1c40ed9feed20c5b8`. Eval 0 verdict: PASS.
- **Eval 0 findings on records this prompt depends on:** C-1 (header comment still says "172 INSERT"; comments aren't data) and G1 (off-snapshot GitHub columns) carried; neither changes a graded value.

---

### Phase 0: Sources read

Docs and references: Eval 1 (Local Overrides, §1.3 anti-patterns, §2.1 UGT, common mistakes); `prompt_rubric_reliability.md` (release binding verified); `deep_recheck.md`; `common_errors.md`; `acl.md` and `roster.json`. The `Evals/Docs` PDFs were not re-extracted; Eval 1's inline bands and Local Overrides were applied (evidence limit, unchanged from earlier rounds).

Universe exploration, NEW this round:
- **Line 54 (re-read verbatim).** Same id, ts, thread parent and author as before; only `text` grew. The build numbers match Blake's 09:12:44Z mail word for word ("iOS 0.3.49 (Leonard released it yesterday) and Android 0.3.133", line 96 in Julia's copy).
- **Line 134 (Julia's copy of Blake's reply).** From arthur.blake@ to Julia, Leonard, Robert and Brian; labels INBOX, IMPORTANT; 2025-09-30T13:26:05Z; own thread `…/1844695547248825769`; In-Reply-To and References `<CAAMNAwY…>` (the store builds mail).
- **Base ZOM-199** (`/issues/3243`, Done): "If first 10 level CPM >= 90, then tier 1, otherwise everyone else stays at default tier 0." This matches Blake's claim of what ZOM-199 says. ZOM-42's spec says "1st 10 level avg CPM > 90", which matches "the code never changed from the original spec".
- **Base Gmail "store builds"**: the only base hits are investor pitch mails ("live store builds below"). No other store-builds mail or reply from Blake competes with the injected pair.
- **Instruction timeline (all 2025-09-30 UTC):** store builds mail 09:12:44Z → Blake's reply 13:26:05Z → card rules 14:04:31Z → card comment 15:41:55Z → notes doc 15:47–15:51Z → checklist 16:20:11Z → DM request 19:48:26Z → first thread reply 20:07:18Z (now with build numbers) → reply under Julia's question 21:16:42Z.

Status derivation under the leading reading (shows solvability; not a golden answer):
- **Live 16:** ZOM-23, 42, 45, 199, 221, 246, 263, 274, 281, 282, 288, 295, 300, 303, 305, 378.
- **Editor only 4:** ZOM-173, 200, 277, 315.
- **Replaced 1:** ZOM-254, replaced by ZOM-282.
- **Not shipped 3:** ZOM-202, 280, 293.
- **Total 24.**
- **Comments (9):** ZOM-199 (the build checks cpm > 90, so 90 exactly stays on tier 0; the check runs when the 10th game ends); ZOM-254 (replaced by ZOM-282); ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds, iOS 0.3.49 and Android 0.3.133). None on ZOM-162, 163, 201 or 250.
- **Shares:** robert@ edit; brian.foster@ and leonard.hayes@ comment; arthur.blake@ view.
- **DM reply:** the total, per-status counts, the Not shipped and Editor only keys, that ZOM-282 replaced ZOM-254, and that a new player gets their starting tier when their 10th game ends (wins and losses counted).

---

### Requirement ledger

authority_contract: prompt-incorporation-v1

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Find Leonard's Tuesday DM ask, including both thread replies | SQL 48 (request, 19:48:26Z), 54 (reply 20:07:18Z), 58 (reply 21:16:42Z under Julia's line-56 message) | Slack DM history; threads via reply_count | `slack_conversations_history`, `slack_conversations_replies` / `slack_read_thread`, search | Julia (EMPLOYEE_0005) is a DM member | The register; ten tickets off; build numbers in seven comments; reply contents |
| "everything it points to": card rules | Card #80 (line 69), updateCard (77), commentCard (79), checklist and items (81–87) | DM names "the difficulty baseline card on the zm roadmap board" | `trello_get_cards_on_board`, `trello_get_card`, `trello_get_card_actions`, checklist reads | Trello unscoped | Rules 1–7, the attack-power addendum, the rule 6 change (rule 7 change later withdrawn) |
| "everything it points to": notes on the card | Trello attachment (89) → Google Doc (21), Drive file (12) | Card attachment; Drive search | `trello_get_attachments`, `gdrive_search`, `gdocs_get_document_text` | Doc shared with Julia as reader | ZOM-258 off; Arthur view; reply says which ticket replaced which |
| Ticket scope | Linear ZOM issues; "tiers:" notes; PR #265 review comment; Trello comment; both DM replies; notes | Linear search/list; comments; PR lookup | Linear reads; GitHub PR reviews/comments | Linear, GitHub unscoped | 24 tickets |
| Status per ticket (rules 3–4) | Blake's store builds mail (Julia's copy line 96) **and his reply** (line 134, own thread); Linear states and closing notes | Gmail search (from Blake, "Monday", "store builds", "ZOM-199"); Linear | Gmail search/read; Linear reads | Julia's mailbox (both mails INBOX); Linear unscoped | Live 16 / Editor only 4 / Replaced 1 / Not shipped 3 |
| Rules in force tab (rule 5) | Deck, ZOM-42, Blake's reply (cpm > 90; 10th game, wins and losses), enrage sheet Live tab, `TierManager.cs`, `WinRateRule.cs`, `WinHistory.cs`, `GameLoader.cs` | GSlides, Linear, Gmail, GSheets, GitHub | `gslides_get_presentation_text`, Linear get, `gsheets_values_batch_get`, `github_get_file_contents` | Deck shared; sheet owned by Julia; GitHub, Linear unscoped | Starting tier when the 10th game ends, average CPM above 90 to tier 1; rest unchanged from last round |
| Build the register: one sheet, tabs Tickets + Rules in force | Agenda doc; card rule 2 | GDocs | `gsheets_create_spreadsheet`, `gsheets_batch_update`, `gsheets_values_update` | Write (ACL-free) | New spreadsheet |
| Put it in the ZM Difficulty folder | Prompt; card rule 7 | Drive folder d_96489e1e00a56685625939 | `gdrive_move_file` (or create with parent) | Julia is writer | File in folder |
| Share with everyone on Monday's invite | Prompt; card rule 7; notes (Arthur); line 58 (Brian) | GCal event on Julia's calendar (line 155) | `gdrive_share_file` (role param) | Julia's own calendar | robert@ writer; brian.foster@ and leonard.hayes@ commenter; arthur.blake@ reader |
| Ticket comments (rule 6 as changed) | Card rule 6; checklist item; Blake's reply; rule 4; line 54 (builds); line 58 ("no comments on them either") | Linear | `linear_create_comment` | Write | 9 comments; the seven Editor only / Not shipped ones name iOS 0.3.49 and Android 0.3.133 |
| Reply to Leonard in the DM | DM, both thread replies, notes | Slack | `slack_send_message` | Write | Total, per-status counts, Not shipped and Editor only keys, ZOM-282 replaced ZOM-254, starting-tier timing |

Output capability: creating the spreadsheet and its tabs, moving it into the folder, sharing, the Linear comments and the Slack reply are SUPPORTED by declared catalog tools. The `commenter` and `reader` roles are free strings for `gdrive_share_file` `role`; their runtime acceptance is UNVERIFIED (an evidence limit, not a failure).

---

### Phase 1: Prompt Structure & Persona (prompt byte-identical; re-judged against revision-42 sources)

**Persona:** PASS (5). Exact roster entry; a CEO delegating to a PM fits the role. The card says "Julia owns this one", and the notes are addressed "julia, three things for the register".

**Assigned Competency:** PASS (5). Engineering Ops: reconciling tickets with what shipped in store builds, PR review marks, the build code, and a batch of ticket comments that cite the builds checked.

**Assigned Task Skill:** PASS (5). Retrieval is the core work: every in-scope ticket across title rules, closing notes and a PR review; each ticket's state and shipped status from two Blake mails in separate threads; five late instruction layers (card comment, notes, checklist, two DM thread replies).

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS. Data seeding: PASS.
- **Dynamic Change:** the 21:16Z reply withdraws the checklist's Brian edit and removes four tickets; the 20:07Z reply adds build numbers to the rule 6 comments.
- **Friction:** Blake's reply now sits in its own thread under a new subject; ZOM-312 removed by a PR review comment; ZOM-258 by the notes; Arthur's role from the notes; ZOM-173, 277 and 315 kept as Editor only although they look like the four removed tickets.
- **Decoys carried:** Brian's "+50% … every monster" and "the editor bits too"; Domino card #211; the "Next pass" tab; Vincent's channel request; ZOM-281 having no PR; "rage by level".

**Naturalness:** PASS. First person, lowercase and casual; no document formatting, polished connectives or enumerated specs.

**Anti-Patterns:**

| Pattern | Status |
|---------|--------|
| Command List | PASS. No "first"/"finally" steps or numbered procedure. The one lowercase "then" orders the final reply after the filing, which Leonard's own ask requires ("reply here when it''s in the folder"); the prompt prescribes deliverables, not a search procedure (deep recheck P4-DR1) |
| Bolt-On | PASS. Every sentence serves the baseline |
| Pre-Solving | PASS. No counts, tickets, statuses, exclusions, builds, timings or causes named |
| Tool Mention | PASS. "dm", "folder", "invite" and "tickets" are natural nouns |

**Diversity:** a two-tab sheet, folder placement, role-based sharing with three roles, a batch of Linear comments with source-defined content, and a DM reply over a source-defined cohort with a rules answer.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** PASS (5). Every fork is settled by a prompt sentence or a persona-visible record.
- **AC (strongest this round): Blake's 13:26Z mail isn't "his reply to it" because it's in its own thread. EXCLUDED.**
  - The best case for AC: the mail has a new subject ("editor stuff and ZOM-199, before Monday") and its own Gmail thread, and without it there is no basis for Editor only or for the ZOM-199 comment (Live 20 / Editor only 0, four fewer comments).
  - Card rule 3: "What is in the store builds and what counts as shipped: Blake''s store builds mail and his reply to it." Rule 6 names the same pair.
  - The mail opens "Two things I left out of the mail this morning.", comes from Blake to the same four people the same day, and its In-Reply-To header is the store builds mail. Source identity, timing and the header all say it is that reply.
- **AB: the seven Editor only / Not shipped comments only say "the change isn't in the store builds". EXCLUDED** by Leonard's 20:07Z reply, after the checklist: "when you comment on the editor only and not shipped ones, put the two builds in the comment (ios 0.3.49 and android 0.3.133)". It adds to the checklist wording; both apply.
- **AD: builds in all nine comments.** Not material: same comments on the same tickets; Leonard scopes the builds to "the editor only and not shipped ones". The rubric should neither require nor penalize an extra build mention.
- **AE: ZOM-199 comment with the threshold only (no timing).** Same single comment. Rule 6 asks for "what the build does" where the reply says the ticket's text is wrong; Blake flags both ">= 90" and "after the first 10 levels". Require the > 90 threshold (90 exactly stays on tier 0); accept, don't require, the 10th-game timing.
- **Q/K (starting-tier timing), now settled more directly:** Blake's reply says the check "runs when a player''s 10th game ends, wins and losses both counted, not after 10 levels cleared", matching `TierManager.cs` "if (totalGames == 10)" and card rule 5 ("go by the build").
- **Y, Z, AA, N, L, B–X:** excluded on unchanged rows, as last round (Y by "just those four, on top of the ones i already left off"; Z by "scratch brian editing"; AA by "one more for the baseline"; L by the checklist and "no comments on them either").

**Feasibility:** PASS (5). All asks map to cataloged tools; all data exists (ledger above).

**Persona ACL Reachability:** PASS (5). Every scoped read is visible to Julia: both DM threads (IM member), her mailbox (both Blake mails, INBOX), her calendar (invite), Drive files shared with or owned by her. Trello, Linear and GitHub are unscoped.

**Truthfulness:** PASS (5). Five premises verified (record PR1–PR5): the Tuesday DM (2025-09-30T19:48:26Z, a Tuesday in PT and UTC), Monday's tuning session and invite (2025-10-06, line 155), the ZM Difficulty folder, and Leonard's rules on the card. Nothing the prompt treats as done is after the clock.

**Tool Use & Cross-service:** PASS (5). Slack (ask, exclusions, builds in comments, Brian's role), Trello (rules), Linear (scope, states, comments), Gmail (shipped status, Editor only rule, cpm > 90 and timing), GitHub (ZOM-312 removal, build rules), Drive/Docs/Sheets/Slides (notes, enrage numbers, deck, register) and Calendar (share list) each change a graded fact.

**Investigation + Action:** PASS (5). The investigation feeds the sheet, the shares, the comments and the reply.

**Clarity & Specificity:** PASS (5). Every reading posts the same 9 comments on the same tickets; the build numbers and the ZOM-199 content are source-defined. No "I'll" statements.

**Contrived / Unnatural:** PASS (5). No opaque ids, timestamps, trap hints, hidden destinations, audit-form wording or if-chains in the prompt. The build numbers sit in Leonard's DM, not the prompt.

**Alignment with Today's Date:** PASS (5). "tuesday" = Sep 30, 2025; "monday's tuning session" = Oct 6, 2025 (the invite); every relied-on record is before the clock.

**Originality / Sample Similarity:** N/A (no samples supplied).

**Coherence (Bolt-on):** PASS (5).


### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: Every fork is settled by a prompt sentence or a persona-visible record. SQL revision 42 changes three instruction texts: Leonard's 20:07Z DM reply now asks for the two store builds (iOS 0.3.49, Android 0.3.133) in the Editor only and Not shipped comments (fork AB, settled by that reply); card rule 3 now names 'Blake''s store builds mail and his reply to it', and Blake's reply moved to its own thread 'editor stuff and ZOM-199, before Monday' (fork AC, settled by its opening line 'Two things I left out of the mail this morning.' and its In-Reply-To header); the reply now also says the starting tier check runs when the 10th game ends, wins and losses counted (settles Q/K more directly). AD and AE are content edges with the same writes. Y, Z, AA, N and B-X stay excluded on unchanged rows. 24 tickets, 9 comments.

Alternative selection: Revision 42 changes line 54 (build numbers in comments), the card's rule 3 wording (lines 69/77) and moves Blake's editor-strip and cpm text into a separate-thread reply (line 134 for Julia's copy). AC is the strongest new alternative (the reply is in its own thread under a new subject); AB, AD and AE test the comment contents. Y, Z, AA, N and B-X are every earlier fork, retested against rows that are byte-identical or re-anchored by content.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Follow the card as Leonard left it, his card comment, his 'notes for monday' doc attached to the card, his checklist and his Tuesday DMs (the request thread and his later reply in the thread under Julia's Monday question): scope is every difficulty ticket created up to Aug 31 by title word plus every ticket with Blake's 'tiers:' closing note (ZOM-221, 281, 300, 305, 378), minus a title match Blake marked 'not tiers' in his review on its PR (ZOM-312, PR match3d\#265), attack power counting only when written out (ZOM-271 out), minus the six analytics and tutorial tickets his DM reply lists, ZOM-258 from his notes and the four tickets his later DM reply takes off by key (ZOM-162, 163, 201, 250; 'just those four'), which also get no comments; status against Blake's store builds mail and his reply to it (the 13:26Z 'editor stuff and ZOM-199, before Monday' mail, which says editor and debug tooling never reached players); Replaced only where another ticket's closing note says so (ZOM-282 on ZOM-254); comments on ZOM-199, on Replaced ZOM-254 and, per the checklist's rule 6 change, on every Editor only and Not shipped ticket still on the list, each naming the two store builds (iOS 0.3.49 and Android 0.3.133) per Leonard's first DM reply; the ZOM-199 comment says what the build does (cpm &gt; 90, checked when the 10th game ends); share with the invite attendees, Robert as editor, Brian as commenter per Leonard's later DM reply, Leonard as commenter and Arthur as viewer per the notes; the Rules in force tab as before; the DM reply gives the total, per-status counts, the Not shipped and Editor only keys, which ticket replaced which, and when a new player gets their starting tier. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and the four tickets Leonard's later DM reply takes off, ZOM-162, 163, 201 and 250, off ('just those four'); ZOM-312 off as Blake's 'not tiers'; ZOM-378 and ZOM-281 on); ZOM-173, 200, 277 and 315 stay on as Editor only; ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-271 out; checklist rule 6 change in force for the tickets still listed: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds iOS 0.3.49 and Android 0.3.133); no comments on ZOM-162, 163, 201 or 250; reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280, 293; Leonard DM D05HB64NMQU. | 24 rows: the 35 rule-1 tickets (31 title matches without Duplicates ZOM-203 and ZOM-276 and without ZOM-312, which Blake marked 'not tiers' in his review on PR match3d\#265, plus tiers: tickets ZOM-221, 281, 300, 305, 378) minus the eleven Leonard leaves off (ZOM-30, 49, 50, 161, 262, 275 in his first DM reply, ZOM-258 in his notes for monday, and ZOM-162, 163, 201, 250 in his later DM reply); Live 16, Editor only 4, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force as the build runs them: starting tier set after the first 10 games played (wins and losses), average CPM above 90 to tier 1, everyone else tier 0 (90 exactly stays on tier 0); promotion and demotion in ZOM-42's wording: 80% or more over up to the most recent 10 attempts (the last 10 games played) promotes, one win on tier -2 promotes; demotion on a losing streak of 4 games in a row at any time or a win rate of 50% or lower over up to the last 10 games; the record resets after every promotion or demotion; after a demotion the level being played is replayed lower (below the new tier) until a win; enrage from the sheet Live tab copied as it stands: nine monster rows and MonsterBase 0.8/0.8 with their numbers, and Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP) as not copied yet; DM gives the total 24, the per-status counts, the keys of the Not shipped (ZOM-202, 280, 293) and Editor only (ZOM-173, 200, 277, 315) tickets, that ZOM-282 replaced ZOM-254, and that a new player gets their starting tier after their first 10 games (levels played), from the average CPM of those games. | CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 276-276): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; SHEET\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 26-26): "\["MonsterBase (base prefab)", "0.8", "0.8", "0"\], \["Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)", "not copied yet", "not copied yet", "0"\]"; TCOMMENT\_W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 79-79): "written out (ATK on its own doesn''t)"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 85-85): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; CARD\_R1B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''"; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 274-274): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 96-96): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"; DMT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "tell me when a new player gets their starting tier"; DECK\_PROMO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Promotion: win rate of 80% or more over the last 10 attempts moves you up one tier."; Z42MR (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we evaluate UP TO THE MOST RECENT 10 attempts of the player"; CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; Z42LAST (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we constantly look at the last 10 games played"; Z42STREAK (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "A losing streak of 4 games in a row can still trigger at any time"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"; Z42RESET (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "every time a promotion/demotion happens, the record is reset and we start at 0 games played"; WR\_DEM50 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/WinRateRule.cs lines 31-31): "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"; GL\_RETRY (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Match3D/Game/Levels/GameLoader.cs lines 101-101): "// Make sure we go down a tier for this level"; REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "For the rules tab: the starting tier check in the code is cpm &gt; 90, not &gt;= 90"; NOTES\_258 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays."; NOTES\_ART (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "arthur is only listening in on monday, view access is enough for him."; NOTES\_REPL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "when you reply to me, also tell me which ticket replaced which."; CARD\_R1NT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "It works the other way too: a title match Blake marked ''not tiers'' in his review on its PR stays off."; GH265RC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work"; DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "take 162, 163, 201 and 250 off the list too. just those four, on top of the ones i already left off."; DMR2\_BR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "comment access is enough for brian"; DMR1\_BLD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "put the two builds in the comment (ios 0.3.49 and android 0.3.133)"; CARD\_R3B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Blake''s store builds mail and his reply to it." |
| B | match3d\#401 changed how enrage works (speed and damage split per monster, hp method dropped), so ZOM-282 is Replaced by match3d\#401 and gets a Replaced comment. | ZOM-282 Replaced by match3d\#401. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a Replaced comment on ZOM-282 naming match3d\#401. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-282. | Register shows ZOM-282 Replaced; DM counts Live 15, Replaced 2. | GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 62-62): "this gives enrage speed and damage their own values, they shared one since ZOM-282." |
| C | Comment on every listed ticket whose text the store builds contradict, including ZOM-42 (6-7 levels vs 10). | Correction comment also on ZOM-42. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a comment on ZOM-42. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-42. | Extra correction comment; register unchanged. | Z42A (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "gets assigned after the first 6-7 levels based on CPM" |
| D | Read the scope window in Pacific days with an Apr 21 start, dropping ZOM-23 (2025-04-21T04:51:38Z, Apr 20 PT); ZOM-30 is already off under Leonard's DM reply. | 23 tickets; ZOM-23 out. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Register 23 rows; DM total 23 and Live 15. | Z23 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3277): "2025-04-21T04:51:38Z" |
| E | Also post the register in \#zombie-design because Vincent asked Julia to drop it there. | Share with the invite and also post in \#zombie-design. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a Slack post in \#zombie-design. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus C090N54TG79. | Same register; extra channel post. | VINCENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 52-52): "julia when you have the difficulty list can you drop it in here too" |
| G | ZOM-254 was closed (2025-06-23) after ZOM-282 (2025-06-21) and its own QA note says blunder enrages the monsters, so ZOM-282 is not the 'later' ticket and ZOM-254 stays Live with no Replaced comment. | ZOM-254 Live; no Replaced ticket. | Same as A without the ZOM-254 comment. | Same as A without Linear ZOM-254. | Register shows ZOM-254 Live; DM counts Live 17, Replaced 0, and no replacement to report. | Z254C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 252-252): "checked on the dev build, blunder enrages the monsters on the board now" |
| H | Rule 5 asks for enrage as it works in the store builds today, so the three monsters the sheet has not copied are given what they actually run on in main: no own override, so MonsterBase's 0.8 speed / 0.8 damage. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same 24 rows and counts as A; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab, with Mailman, Mayor2 and PartyGirl given 0.8 speed / 0.8 damage (MonsterBase) instead of not copied yet; DM as A. | CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; MB\_ENRAGE (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/MonsterBase.prefab lines 342-343): "enrageSpeedPercentage: 0.8" |
| I | Fill the gap from the VarC prefabs the History tab says the Live tab was copied from: VarC-PartyGirl carries enragePercentage 0.6, so PartyGirl is 0.6 speed / 0.6 damage; Mailman and Mayor2 show no enrage value in their prefab text. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same 24 rows and counts as A; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab, with PartyGirl at 0.6 / 0.6 and Mailman and Mayor2 without numbers; DM as A. | SHEET\_HIST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 30-30): "\["2025-09-08", "Live tab copied from the VarC prefabs in main", "Julia"\]"; PG\_PREFAB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/VarC-PartyGirl.prefab lines 215-216): "propertyPath: enragePercentage" |
| J | Leonard's comment adds attack power in the title; ZOM-271's title says 'ATK POWER' / 'ATK Power', and 'ATK on its own' is read as ATK without 'power', so ZOM-271 (Done, June 16, card-profile stat display) is in scope as Live. | 25 tickets; ZOM-271 Live; otherwise as A. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 25 rows (adds ZOM-271); Live 17, Editor only 4, Replaced 1, Not shipped 3; DM total 25 and Live 17. | TCOMMENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 79-79): "attack power in the title counts too"; Z271 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3323): "Comprehensive Item Stat Display Rules also ATK POWER BUG. Also Change Damage sort to ATK Power sort" |
| K | Take the starting-tier window from the written rules (deck, ZOM-42, ZOM-199): average CPM over the player's first 10 levels read as ten distinct levels, so replays of a lost level don't count; &gt; 90 to tier 1, the rest tier 0. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register and counts as A; Rules in force and the DM answer give the starting tier as after the first 10 distinct levels (replays not counted), instead of after the first 10 games played (wins and losses) as the build counts them. | Z42S (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "1st 10 level avg CPM &gt; 90 (top 20%) moves to tier 1, rest stays in tier 0)"; DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0." |
| L | The 'Before Monday' checklist items are unchecked, so they are Leonard's pending notes, not rules in force; card rule 6 as written stands: comments only on ZOM-199 and ZOM-254, with the Not shipped and Editor only tickets left as they are. | Checklist not applied: two comments. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, leonard.hayes@ and brian.foster@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 and ZOM-254 only; reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. | Same 24 rows and counts; no comments on the seven Editor only and Not shipped tickets; brian.foster@ as commenter as in A. | CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CL\_NAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 81-81): "'Before Monday', '68daca5871dba40417a00383'" |
| M | ZOM-378 'Level 1 is removed and creates tutorial order problems' is a tutorial ticket, so it goes off the list with the other analytics and tutorial tickets Leonard named. | 23 tickets; ZOM-378 off. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 23 rows; Live 15; DM total 23 and Live 15. | DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3440): "It creates other important issues like wrong tutorials at the wrong spot." |
| N | Leonard's reason 'they don't change how hard a level plays' (repeated in his notes for ZOM-258) and Blake's 'players never see it' on ZOM-312 are the test, so every ticket that only touches editor or debug tooling is left off too (ZOM-162, 163, 173, 200, 201, 202, 250, 277, 315), with no comments on them. | Editor-tooling tickets off the list; no comments on them. | As A without the comments on the editor-tooling tickets. | As A without those Linear tickets. | 19 rows (ZOM-173, 200, 202, 277 and 315 off on top of ZOM-162, 163, 201, 250); no Editor only rows; DM without Editor only keys. | DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; NOTES\_258 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays."; GH265RC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work" |
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
| Y | All four keys Leonard's later DM reply takes off (ZOM-162, 163, 201, 250) are level editor tickets by their titles, so his intent is the level editor category: Blake's store builds mail defines level editor work (Assets/Scripts/LevelEditor and the LevelDesigner panels), and ZOM-173 (Linear label 'Level Editor', 'Item Set Count in editor', level objects panel), ZOM-277 and ZOM-315 (the editor's stats panel, which ZOM-250 created) are level editor tickets on the same footing. So those three go off too, with no comments; only ZOM-200 (debug menu) is left as Editor only. | 21 tickets: ZOM-173, 277 and 315 also off as level editor tickets, with no comments; ZOM-200 the only Editor only ticket; otherwise as A. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the four Editor only and Not shipped tickets ZOM-200, 202, 280 and 293 (the change isn't in the store builds); no comments on ZOM-162, 163, 173, 201, 250, 277 or 315; reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254, ZOM-200, 202, 280, 293; Leonard DM D05HB64NMQU. | 21 rows (24 minus ZOM-173, 277, 315); Live 16, Editor only 1 (ZOM-200), Replaced 1, Not shipped 3; DM total 21, Editor only key ZOM-200 only; rules tab as A. | DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "take 162, 163, 201 and 250 off the list too."; Z201T (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3246): "Also turn it into an overlay in editor while not obstructing game board."; Z250T (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3300): "Create faux level timer and add attack power stats in level editor"; MAIL\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "The level editor (Assets/Scripts/LevelEditor and the LevelDesigner panels), anything in an Editor folder and the debug menu (Assets/Scripts/Debug) are stripped before we ship to players on iOS and Android."; Z173L (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3215/labels): "Level Editor"; Z173T (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3215): "Item Set Count in editor not updating with difficulty tier changes"; Z173C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 220-220): "this one is the set count in the level objects panel"; Z277C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 266-266): "this is the average in the editor''s stats panel, nothing changes in the game itself"; Z315C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 314-314): "this is the total attack power in the editor''s stats panel, items without cardData now count with their base damage. nothing changes in the game itself" |
| Z | The 'Before Monday' checklist's rule 7 change ('Brian gets edit as well') is on the card the DM points to, so Brian keeps edit access. | Robert and Brian edit, Leonard comments, Arthur views; otherwise as A. | Same as A except brian.foster@ is shared as editor. | Same as A. | Same register, comments and DM as A. | CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 85-85): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session" |
| AA | Leonard's later message sits in the thread under Julia's own Monday question, not in his Tuesday request thread, so it is not part of 'his ask'; the register keeps ZOM-162, 163, 201 and 250 (Editor only, commented) and Brian keeps edit. | 28 tickets (Live 16, Editor only 8, Replaced 1, Not shipped 3); 13 comments; Robert and Brian edit, Leonard comments, Arthur views. | Same kinds of writes as A, plus comments on ZOM-162, 163, 201 and 250, and brian.foster@ shared as editor. | As A plus Linear ZOM-162, 163, 201, 250. | 28 rows; DM total 28 with Editor only keys ZOM-162, 163, 173, 200, 201, 250, 277, 315. | DMP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "leonard, anything you need from me before monday''s tuning session?"; DM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "julia before monday''s tuning session i want a baseline of the difficulty system from you" |
| AB | The seven Editor only and Not shipped comments only say the change isn't in the store builds, as the checklist words it; the build numbers are not needed. | As A. | As A, but the seven comments omit the build numbers. | As A. | Seven comments without iOS 0.3.49 / Android 0.3.133. | CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "saying the change isn''t in the store builds" |
| AC | Blake's 13:26Z mail sits in its own thread under a new subject, so it is not 'his reply to it'; status and comments go by the 09:12Z store builds mail alone, which says nothing about editor tooling or ZOM-199. | No Editor only basis: ZOM-173, 200, 277, 315 count as Live (Done, merged before Sep 26); no wrong-text comment on ZOM-199. | Four fewer comments (no Editor only comments) and no ZOM-199 comment. | Linear ZOM-199, 173, 200, 277, 315 untouched. | Live 20, Editor only 0; DM Editor only keys empty. | MAIL2\_SUBJ (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "'editor stuff and ZOM-199, before Monday'"; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 96-96): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that." |
| AD | Put the two build numbers in every ticket comment, including ZOM-199 and ZOM-254. | As A. | As A; the ZOM-199 and ZOM-254 comments also mention the builds. | As A. | Two comments carry an extra build reference. | DMR1\_BLD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "when you comment on the editor only and not shipped ones" |
| AE | The ZOM-199 comment only needs the threshold (cpm &gt; 90, 90 exactly stays on tier 0), not when the check runs. | As A. | As A. | As A. | ZOM-199 comment states the &gt; 90 threshold without the 10th-game timing. | REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "For the rules tab: the starting tier check in the code is cpm &gt; 90, not &gt;= 90" |

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
Resolution evidence: CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "ZOM-199 says &gt;= 90 after the first 10 levels, but the code never changed from the original spec"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | C decides ZOM-42 needs a comment. |
| writes | DIFFERENT | C adds one comment. |
| destinations | DIFFERENT | C adds ZOM-42. |
| contents | DIFFERENT | Extra comment text. |

Authority chain: P → DMR → CARD\_R6X

Resolution relevance challenge: The quoted sentences name ZOM-42 as staying as it is; the checklist change covers Editor only and Not shipped tickets, which ZOM-42 (Live) is not; the reply names only ZOM-199.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "ZOM-199 says &gt;= 90 after the first 10 levels, but the code never changed from the original spec"

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
Resolution evidence: CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system before monday's tuning session. can you take it off my plate? go through his ask and everything it points to and build the register the way he set it up. put it in the zm difficulty folder and share it with everyone on monday's tuning invite. if his rules say something needs to happen on the tickets, go ahead and do that too. then reply to leonard in the dm with what he asked for. go with your read on the details, no need to check with me first"; CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 155-155): "VALUES ('evt\_91674a9c23d012a9ac34da', 'julia.lawson@harmonygames.co', 'ZM difficulty tuning'"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | E adds a channel post. |
| writes | DIFFERENT | E adds a Slack post. |
| destinations | DIFFERENT | E adds \#zombie-design. |
| contents | DIFFERENT | Extra post. |

Authority chain: P → DMR → CARD\_R7

Resolution relevance challenge: The prompt names the audience as the invite; the invite on Julia's calendar does not include Vincent.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system before monday's tuning session. can you take it off my plate? go through his ask and everything it points to and build the register the way he set it up. put it in the zm difficulty folder and share it with everyone on monday's tuning invite. if his rules say something needs to happen on the tickets, go ahead and do that too. then reply to leonard in the dm with what he asked for. go with your read on the details, no need to check with me first"; CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 155-155): "VALUES ('evt\_91674a9c23d012a9ac34da', 'julia.lawson@harmonygames.co', 'ZM difficulty tuning'"

Compared alternative: G
Resolution: EXCLUDED. Rule 4 now keys on another ticket's closing note, with no ordering condition. ZOM-282's closing note says it replaces the blunder 2.0 boost from ZOM-254; ZOM-254's QA note describes the dev build and is not a closing note on another ticket that replaces it. Close order no longer matters.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 276-276): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Replaced vs Live for ZOM-254. |
| writes | DIFFERENT | G drops the ZOM-254 comment. |
| destinations | DIFFERENT | G drops Linear ZOM-254. |
| contents | DIFFERENT | Status and DM counts differ (Live 17 / Replaced 0), and the DM has no replacement to report. |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The rule no longer says 'later', so close dates cannot reverse it; ZOM-282's note names ZOM-254 explicitly, which is what the rule asks for.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 276-276): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"

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
Resolution evidence: DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 344-344): "tiers: closing. level 1 is back in the list so the first levels line up with their tier versions again"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-378 on vs off. |
| writes | SAME | ZOM-378 is Live and gets no comment either way. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | One row fewer; DM total 23 and Live 15. |

Authority chain: P → DMX

Resolution relevance challenge: Not a strawman: ZOM-378's title says 'tutorial order problems' and its description is about tutorials. But the DM gives an explicit list, and the tiers: note quoted ties ZOM-378 to tier level versions, which is difficulty.
Delegation challenge: NOT_CLAIMED. No alternative scope is authorized.
Challenge evidence: DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 344-344): "tiers: closing. level 1 is back in the list so the first levels line up with their tier versions again"

Compared alternative: N
Resolution: EXCLUDED. Leonard's later DM reply takes off only four tickets by key and closes the list ('just those four, on top of the ones i already left off'), so no other editor or debug tooling ticket comes off. Blake's mail names the debug menu separately from the level editor, so ZOM-200 (debug menu) is not reached; ZOM-202 is open and goes on as Not shipped under rule 1. Leonard's first reply still asks for 'the editor only ones', which N leaves empty. The narrower level-editor fork is tested separately as Y. The exclusion is scoped to 'the analytics and tutorial tickets' with their keys listed, and in the same message Leonard asks for the keys of the editor only ones, which only makes sense if they stay on the list; the checklist's rule 6 change also has Editor only tickets commented, and card rule 3 lists Editor only as a status. The newer 'doesn't change how hard a level plays' (ZOM-258 note) and 'players never see it' (ZOM-312 review) lines each name one ticket by key or PR; card rule 3 keeps an Editor only status and the checklist comments on Editor only tickets, so the list still holds them.
Resolution evidence: DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "just those four, on top of the ones i already left off."; DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."; MAIL\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "The level editor (Assets/Scripts/LevelEditor and the LevelDesigner panels), anything in an Editor folder and the debug menu (Assets/Scripts/Debug) are stripped before we ship to players on iOS and Android."; DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"

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
Resolution evidence: CARD\_R1B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''"; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 274-274): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; LUSR\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /users/35): "arthur.blake@harmonygames.co"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | O drops ZOM-281. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rows and counts differ by one (23 / Live 15). |

Authority chain: P → DMR → CARD\_R1B

Resolution relevance challenge: Not a strawman: ZOM-281's assignee is another person and the old rule 1 wording tied scope to Blake's own tickets. The current rule 1 keys on the note, and the note's author id is Blake's.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R1B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''"; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 274-274): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; LUSR\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /users/35): "arthur.blake@harmonygames.co"

Compared alternative: P
Resolution: EXCLUDED. Card rule 3 makes Blake's store builds mail the authority for what is in the store builds and what counts as shipped. The mail says both store builds were cut from main on Sep 26 and everything difficulty related was merged long before that; it strips only level editor and debug code, and ZOM-281 (win streak on replay) is a gameplay fix. ZOM-281 is Done, completed 2025-06-27, and Blake's closing note says it was checked on the dev build. Rule 1's 'never-merged' covers work that never landed, not a Done ticket the shipped-authority calls merged.
Resolution evidence: CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 96-96): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that."; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 274-274): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; Z281D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "2025-06-27T09:56:19Z"; Z281 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "Win streak not lost when replaying without main menu"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Live vs Not shipped for ZOM-281. |
| writes | DIFFERENT | P adds a ZOM-281 comment. |
| destinations | DIFFERENT | P adds ZOM-281. |
| contents | DIFFERENT | Status cell, DM counts and Not shipped keys differ. |

Authority chain: P → DMR → CARD\_R3B → MAIL\_MERGED

Resolution relevance challenge: Not a strawman: a complete GitHub scan finds no 'ZOM-281' string, so an Agent looking for a merged PR finds none. The card names the mail as the shipped authority and the mail answers the question for difficulty work as a class.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 96-96): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that."; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 274-274): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; Z281D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "2025-06-27T09:56:19Z"; Z281 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "Win streak not lost when replaying without main menu"

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
Resolution evidence: REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "For the rules tab: the starting tier check in the code is cpm &gt; 90, not &gt;= 90"; REPLY90 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "so 90 exactly stays on tier 0"; CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set (the ZOM-199 comment is in both). |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Threshold: above 90 vs 90 or more. |

Authority chain: P → DMR → CARD\_R5B

Resolution relevance challenge: Not a strawman: the deck and ZOM-199 both say 90 or more. Blake's reply, addressed to the rules tab, and the build say otherwise, and rule 5 asks for the starting tier as it works in the store builds.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "For the rules tab: the starting tier check in the code is cpm &gt; 90, not &gt;= 90"; REPLY90 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "so 90 exactly stays on tier 0"; CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"

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
Resolution evidence: CARD\_R1NT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "It works the other way too: a title match Blake marked ''not tiers'' in his review on its PR stays off."; GH265REV (Evals/task\_inputs/01\_Universe\_Inject.sql lines 169-169): "'harmonygames-Games/match3d\#265\#rev\_8', 'harmonygames-Games/match3d\#265', 'EMPLOYEE\_0025\_GITHUB\_USERNAME', 'COMMENTED'"; GH265RC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work"; PR265 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /pull\_requests/2147): ""title": "ZOM-312""; GHU\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /users/6): ""name": "Arthur Blake""

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-312 off vs Editor only. |
| writes | DIFFERENT | W adds a ZOM-312 comment. |
| destinations | DIFFERENT | W adds Linear ZOM-312. |
| contents | DIFFERENT | Rows 24 vs 25; Editor only 4 vs 5; keys differ. |

Authority chain: P → DMR → CARD\_R1NT

Resolution relevance challenge: Rule 1 asks only for Blake's review on the ticket's PR. Review rev\_8 is authored by EMPLOYEE\_0025 (Arthur Blake) on PR \#265, and the comment is part of that review.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; Leonard's instruction is applied, not delegated.
Challenge evidence: CARD\_R1NT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "It works the other way too: a title match Blake marked ''not tiers'' in his review on its PR stays off."; GH265REV (Evals/task\_inputs/01\_Universe\_Inject.sql lines 169-169): "'harmonygames-Games/match3d\#265\#rev\_8', 'harmonygames-Games/match3d\#265', 'EMPLOYEE\_0025\_GITHUB\_USERNAME', 'COMMENTED'"; GH265RC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 65-65): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work"; PR265 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /pull\_requests/2147): ""title": "ZOM-312""; GHU\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /users/6): ""name": "Arthur Blake""

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
Resolution: EXCLUDED. Leonard's 2025-09-30T21:16:42Z DM reply (revision 30) now names no category and gives no category-wide reason. It takes off four keys and closes the list in so many words: 'just those four, on top of the ones i already left off.' ZOM-173, 277 and 315 are not among the four, and not among the ones he already left off (the six in his first DM reply, ZOM-258 in his notes). So they stay on the list and, as level-editor-only work stripped from store builds (Blake's mail), they are Editor only and get the checklist's rule 6 comment. Same author, latest message, same issue (which tickets come off): the newer, explicit closed list settles it (checks 1-3); the scope check (4) keeps the rest of the card and checklist unchanged.
Resolution evidence: DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "just those four, on top of the ones i already left off."; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; NOTES\_258 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays."; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-173, 277 and 315 on as Editor only (A) vs off (Y). |
| writes | DIFFERENT | Three Linear comments on ZOM-173, 277 and 315 under A, none under Y. |
| destinations | DIFFERENT | Linear ZOM-173, 277, 315 touched under A only. |
| contents | DIFFERENT | 24 vs 21 rows; Editor only 4 vs 1; DM total and Editor only keys differ. |

Authority chain: P → DMR2\_LE

Resolution relevance challenge: Not a strawman: the four keys are all level editor tickets by title, so a reader could look for the theme. But Leonard's own words now close the list ('just those four'), and the message no longer names the category or gives a reason that reaches other tickets. The cited line addresses exactly this difference: whether tickets beyond the four come off.
Delegation challenge: NOT_CLAIMED. Leonard's explicit closed list is applied; no alternative is delegated.
Challenge evidence: DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "just those four, on top of the ones i already left off."

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
Resolution evidence: DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "one more for the baseline: take 162, 163, 201 and 250 off the list too."; P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system"

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

Compared alternative: AB
Resolution: EXCLUDED. Leonard's 20:07Z reply, in his own request thread and after the 16:20Z checklist, adds to those same comments: 'when you comment on the editor only and not shipped ones, put the two builds in the comment (ios 0.3.49 and android 0.3.133)'. Same author, later, same scope; it adds content and does not replace the checklist's wording, so both apply.
Resolution evidence: DMR1\_BLD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "when you comment on the editor only and not shipped ones, put the two builds in the comment (ios 0.3.49 and android 0.3.133) so people can see what you checked against"; P (Evals/task\_inputs/04\_Prompt.txt): "go through his ask and everything it points to"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same tickets and statuses. |
| writes | SAME | Same seven comments are posted. |
| destinations | SAME | Same Linear tickets. |
| contents | DIFFERENT | Build numbers present vs absent in seven comments. |

Authority chain: P → DMR1\_BLD

Resolution relevance challenge: Not a strawman: the checklist alone words the comment without builds. The later DM reply settles it.
Delegation challenge: NOT_CLAIMED. No delegation claimed.
Challenge evidence: CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "saying the change isn''t in the store builds"; DMR1\_BLD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "put the two builds in the comment (ios 0.3.49 and android 0.3.133)"

Compared alternative: AC
Resolution: EXCLUDED. Card rule 3 names 'Blake''s store builds mail and his reply to it', and rule 6 the same pair. The 13:26Z mail is from Blake to the same four people the same day, opens 'Two things I left out of the mail this morning.', and its In-Reply-To header points at the store builds mail. A changed subject does not change what it is. It is in Julia's inbox (her mailbox copy, INBOX label) and Gmail reads and search are cataloged.
Resolution evidence: CARD\_R3B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "What is in the store builds and what counts as shipped: Blake''s store builds mail and his reply to it."; MAIL2\_HDR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "Two things I left out of the mail this morning."; MAIL2\_IRT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "\{"name": "In-Reply-To", "value": "&lt;CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com&gt;"\}"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Editor only status and the ZOM-199 comment exist vs not. |
| writes | DIFFERENT | Four Editor only comments and the ZOM-199 comment vs none. |
| destinations | DIFFERENT | Linear ZOM-199, 173, 200, 277, 315 touched vs not. |
| contents | DIFFERENT | Live 16/Editor only 4 vs Live 20/Editor only 0. |

Authority chain: P → DMR → CARD\_R3B → MAIL2\_HDR

Resolution relevance challenge: Not a strawman: the mail is in its own Gmail thread with a new subject, so a reader of the first thread alone would miss it. The card's own wording, the opening line and the reply header tie it to the store builds mail.
Delegation challenge: NOT_CLAIMED. No delegation claimed.
Challenge evidence: MAIL2\_SUBJ (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "'editor stuff and ZOM-199, before Monday'"; MAIL2\_HDR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "Two things I left out of the mail this morning."

Compared alternative: AD
Resolution: EXCLUDED. Leonard scopes the build numbers to 'the editor only and not shipped ones'. Adding them to the ZOM-199 or ZOM-254 comment is extra wording, not a different comment, ticket or decision; it does not contradict any instruction. Not material; the rubric should neither require nor penalize it.
Resolution evidence: DMR1\_BLD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "when you comment on the editor only and not shipped ones"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same register. |
| writes | SAME | Same nine comments on the same tickets. |
| destinations | SAME | Same. |
| contents | SAME | Required content present in both; one adds a harmless reference. |

Authority chain: P → DMR1\_BLD

Resolution relevance challenge: Weak alternative; recorded so the rubric doesn't grade the extra mention.
Delegation challenge: NOT_CLAIMED. No delegation claimed.
Challenge evidence: DMR1\_BLD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 54-54): "when you comment on the editor only and not shipped ones"

Compared alternative: AE
Resolution: EXCLUDED. Rule 6 says to comment 'with what the build does' where Blake's mail or reply says a ticket's text is wrong. Blake says ZOM-199 is wrong on both points: 'ZOM-199 says &gt;= 90 after the first 10 levels' while the code checks cpm &gt; 90 'when a player''s 10th game ends, wins and losses both counted, not after 10 levels cleared'. A comment with only the threshold covers the sharper error; both are the same single comment on the same ticket. The threshold is the required content; the timing is supported and should be accepted, not required.
Resolution evidence: CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does"; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "ZOM-199 says &gt;= 90 after the first 10 levels, but the code never changed from the original spec"; MAIL2\_10TH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "it runs when a player''s 10th game ends, wins and losses both counted, not after 10 levels cleared"; Z199D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3243): "If first 10 level CPM &gt;= 90, then tier 1, otherwise everyone else stays at default tier 0."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same register. |
| writes | SAME | One comment on ZOM-199 either way. |
| destinations | SAME | Linear ZOM-199. |
| contents | SAME | Both state what the build does for the threshold Blake flags; the timing is additive detail from the same mail. |

Authority chain: P → DMR → CARD\_R6N

Resolution relevance challenge: Edge content question, not a different write; carried to the rubric guidance.
Delegation challenge: NOT_CLAIMED. No delegation claimed.
Challenge evidence: REPLY90 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "so 90 exactly stays on tier 0"

Strongest-alternative challenge (AC): AC is the strongest alternative this round: Blake's reply now sits in its own Gmail thread with a new subject, and without it there is no basis for Editor only or for the ZOM-199 comment. Card rule 3 names 'his reply to it', and the mail opens 'Two things I left out of the mail this morning.' with an In-Reply-To to the store builds mail, so it is that reply. Y stays excluded by 'just those four'.
Challenge evidence: CARD\_R3B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "Blake''s store builds mail and his reply to it."; MAIL2\_HDR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "Two things I left out of the mail this morning."; DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "just those four, on top of the ones i already left off."

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.


### Phase 3: Universe Feasibility

**Data Existence:** PASS (5). Every needed entity is verified and retrievable through cataloged reads.

**Cross-Service Coherence:** PASS (5). No inconsistency in task-touched data.
- **Line 54 (changed text):** same keys, author, channel and thread fields; the build numbers equal Blake's mail ("iOS 0.3.49 … and Android 0.3.133", line 96) and the base Slack release note "I just released IOS 0.3.49" (C07C2866011, Sep 29 PT). The 20:07Z timing is after the 16:20Z checklist whose rule 6 change it presupposes.
- **Card rule 3 (lines 69/77):** "and his reply to it" agrees with rule 6, which already named "his reply to it". The updateCard action's new desc equals the card desc.
- **Blake's reply (line 134 and four other mailbox copies):** own thread rows with matching ids; In-Reply-To / References point at the store builds mail; sent 13:26:05Z, before the 14:04:31Z card rules that cite it. What it says ZOM-199 says (">= 90 after the first 10 levels") matches base ZOM-199 ("If first 10 level CPM >= 90, then tier 1"). "the code never changed from the original spec" matches ZOM-42 ("1st 10 level avg CPM > 90") and `TierManager.cs` ("cpm > 90.0f", "if (totalGames == 10)").
- **Unchanged rows:** REUSED (byte-identical) from the earlier rounds and the same-hash `0_injection.md`.
- **Known base-data issues (not scored):** none touched; the task uses no Snowflake or Confluence data.
- **Not task-touched (not scored):** `Monster.cs` passes a single `enrageDamagePercentage`; keep rubric rows off stacking behaviour. The distractor card action's board label "Product Roadmap" matches the base actions' own label for that board (base board name "DD Product Roadmap").
- **Injection SQL considered:** Yes. Static integrity evidence: REUSED from `0_injection.md` (same hash `7966b149…20c5b8`, checks A–B; lint re-run, 0 flags). The task-relevant Check C items were redone above.
- **Prompt-specific sources, access and configuration:** supported. No error/async config or dynamic context applies.

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|-----------|--------------|-------------|---------------|
| Prompt | Unique Ground Truth | 5 | New forks AB and AC settled by Leonard's 20:07Z reply, card rule 3 and the reply's own opening line and header; AD/AE same writes |
| Prompt | Feasibility | 5 | All asks cataloged; data exists |
| Prompt | Persona ACL Reachability | 5 | Both Blake mails in Julia's inbox; both DM threads visible |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | Comment writes and contents don't diverge |
| Prompt | Contrived / Unnatural | 5 | No flags |
| Prompt | Alignment with Today's Date | 5 | Tue Sep 30 and Mon Oct 6 resolve; records before the clock |
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
| Universe | Cross-Service Coherence | 5 | Changed rows consistent with base ZOM-199, ZOM-42 and the code |

---

### Issues Found

None.

### Recommended Improvements

1. **Bring the OEs and rubric to this round's SQL before /oe and /rubric.**
   - **Unchanged:** 24 tickets (Live 16; Editor only 4: ZOM-173, 200, 277, 315; Replaced 1: ZOM-254 by ZOM-282; Not shipped 3: ZOM-202, 280, 293); shares robert@ edit, brian.foster@ and leonard.hayes@ comment, arthur.blake@ view.
   - **New: build numbers.** The seven comments on ZOM-173, 200, 277, 315, 202, 280 and 293 should say the change isn't in the store builds and name iOS 0.3.49 and Android 0.3.133. Don't require or penalize builds in the ZOM-199 / ZOM-254 comments.
   - **New: where Blake's reply lives.** Any OE step that reads "Re: store builds for monday" in the first thread should now point at the separate mail "editor stuff and ZOM-199, before Monday" (Julia's inbox, 2025-09-30 13:26 UTC).
   - **ZOM-199 comment:** require cpm > 90 (90 exactly stays on tier 0); accept, don't require, "checked when the 10th game ends, wins and losses counted".
2. **Starting tier (Rules in force tab and DM reply):** Blake now says it outright: the check runs "when a player's 10th game ends, wins and losses both counted, not after 10 levels cleared". Accept "after the 10th game" or "after 10 levels played"; reject "after 10 levels cleared/won" and ZOM-42's "6-7 levels". Don't require the > 90 threshold in the DM reply.
3. **Don't grade** ticking the checklist items, a "rage by level" tab, or whether the DM reply is a thread reply or a top-level message.
4. **Optional wording, carried:** "then reply to leonard in the dm…" could drop "then" or follow Leonard's own condition ("once it's in the folder, reply…"). Not a defect. If you change it, write it in your own voice (prompts are screened for AI-written text); a prompt change outdates every pass that reads the prompt.

---

## Deep Recheck

Passes: P1, P2, P3 and P4 on Opus 5.5 (claude-opus-5-5), session effort, each blind to the main review. Each ran as a fresh subagent given only the saved inputs (not `reports/`), the persona references, `SEARCH.md`, `common_errors.md` and `deep_recheck.md`. Every cited record was reopened in the main session.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 7 sentences; 6 outcomes; 16 forks | none | 0 |
| P2 | 7 sentences | 3 | 0 |
| P3 | 7 sentences; SQL static checks | 2 | 0 |
| P4 | 7 sentences | 1 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| P2-DR1 | P2 | "if his rules say something needs to happen on the tickets, go ahead and do that too." | SQL line 276 `cmt_912bdd42…` (ZOM-282, 2025-06-21T01:09:19Z) "this replaces the blunder 2.0 boost from ZOM-254"; line 252 `cmt_9698eeba…` (ZOM-254, 2025-06-23T09:08:05Z) "checked on the dev build, blunder enrages the monsters on the board now" | Coherence | Cross-Service Coherence | REJECTED | No contradiction: ZOM-282 replaces the boost numbers while enrage itself stays, which is what ZOM-254's later check says. Card rule 4 makes the closing note the only test ("Replaced: only when another ticket''s closing note says it replaces this one"), so the date order changes no status. Rows byte-identical to earlier rounds |
| P2-DR2 | P2 | "go through his ask and everything it points to" | "parking this, nothing merged yet" comments on ZOM-400, 427, 438, 439, 441, 443, 458, 468, dated after each issue's `updated_at` | Coherence | Data coherence | REJECTED | None of these tickets is in the register's scope (all created after Aug 31 or not difficulty tickets), so no graded value depends on them. Not task-touched; not scored |
| P2-DR3 | P2 | "go through his ask and everything it points to" | SQL line 134, Blake's reply in its own thread `…/1844695547248825769`, subject "editor stuff and ZOM-199, before Monday", In-Reply-To `<CAAMNAwY…>` | Coherence | Discoverability | REJECTED | Same as fork AC, settled: card rule 3 "Blake''s store builds mail and his reply to it"; the mail opens "Two things I left out of the mail this morning."; INBOX label in Julia's mailbox |
| P3-DR1 | P3 | (SQL overlay) | SQL line 74, Trello action `683dbef4991df7f0987ddb73` board name "Product Roadmap" vs base board name "DD Product Roadmap" | SQL | Injection consistency | REJECTED | Base Trello actions on that board use the same label (`/actions/1844/data/board/name` = "Product Roadmap"), so the injected action follows the base convention. Distractor card only |
| P3-DR2 | P3 | (SQL overlay) | SQL line 3 header "172 INSERT (one row each), 3 UPDATE" vs 177 INSERT | SQL | Injection header | REJECTED | A comment, not data (Eval 0 advisory C-1, carried) |
| P4-DR1 | P4 | "then reply to leonard in the dm with what he asked for." | prompt text | §6.6 | Command List | REJECTED | §6.6 fails a "first / then / finally" list and Eval 1 §1.3.1 tests for a step-by-step procedure. Here there is one lowercase "then", no "first"/"finally" or numbering, and it orders the reply after filing, which Leonard's own ask requires ("reply here when it''s in the folder"). Same ruling as earlier rounds; optional wording in Recommended Improvement 4 |

Effect on verdict: unchanged. No finding was confirmed; every score stays at 5. P1's independent answer matches this review: 24 tickets (16 / 4 / 1 / 3), 9 comments with the builds on the seven Editor only and Not shipped ones, the same shares and the same DM reply.

Fork list:
- F-AC: settled | Blake's 13:26Z mail is "his reply to it" (Editor only 4, ZOM-199 comment) | Separate thread, so not his reply (Live 20, Editor only 0, no ZOM-199 comment) | Settled by: card rule 3 "What is in the store builds and what counts as shipped: Blake''s store builds mail and his reply to it."; mail "Two things I left out of the mail this morning." with In-Reply-To `<CAAMNAwY…>`
- F-AB: settled | Seven Editor only / Not shipped comments name iOS 0.3.49 and Android 0.3.133 | Comments say only "the change isn''t in the store builds" | Settled by: "when you comment on the editor only and not shipped ones, put the two builds in the comment (ios 0.3.49 and android 0.3.133)" (Leonard, DM `33c941fa…`, 2025-09-30T20:07:18Z, after the 16:20:11Z checklist)
- F-AD: not material | Builds only in the seven comments | Builds in all nine | Same comments on the same tickets; Leonard scopes the builds to "the editor only and not shipped ones"; the rubric should neither require nor penalize the extra mention
- F-AE: settled | ZOM-199 comment states cpm > 90 (90 exactly stays on tier 0), timing optional | Comment must also state the 10th-game timing | Settled by: rule 6 "comment on that ticket with what the build does"; Blake "the starting tier check in the code is cpm > 90, not >= 90"; one comment either way, the rubric requires the threshold and accepts the timing
- F-Q/K: settled | Starting tier when the 10th game ends (wins and losses), average CPM above 90 | After 6-7 levels / 10 levels cleared | Settled by: Blake "it runs when a player''s 10th game ends, wins and losses both counted, not after 10 levels cleared"; rule 5 "go by the build"; `TierManager.cs` "if (totalGames == 10)"
- F-R: settled | cpm > 90 | 90 or more (ZOM-199) | Settled by: "ZOM-199 says >= 90 after the first 10 levels, but the code never changed from the original spec, so 90 exactly stays on tier 0"
- F-Y: settled | ZOM-162, 163, 201 and 250 off; ZOM-173, 277, 315 stay Editor only | All level editor tickets off | Settled by: "take 162, 163, 201 and 250 off the list too. just those four, on top of the ones i already left off."
- F-Z: settled | Brian commenter | Brian editor (checklist) | Settled by: "and scratch brian editing, robert will fix rows in the session. comment access is enough for brian" (21:16:42Z)
- F-AA: settled | The 21:16Z thread reply is part of Leonard's ask | Ignore it | Settled by: "one more for the baseline" by Leonard in the same DM on the Tuesday the prompt names
- F-N: settled | Only the four keys come off | All editor and debug tooling off | Settled by: "just those four"; DM `33c941fa…` "put the keys of the not shipped ones and the editor only ones"
- F-L: settled | Checklist rule 6 change in force (9 comments) | Card rule 6 as written (2 comments) | Settled by: checklist item "rule 6 change: the Editor only and Not shipped tickets get a comment too" (16:20:11Z); DM `33c941fa…` "when you comment on the editor only and not shipped ones"; DM `5f6ed4d5…` "no comments on them either."
- F-J: settled | ZOM-271 out | In | Settled by: "attack power in the title counts too, written out (ATK on its own doesn''t)"
- F-U: settled | Arthur views | Arthur comments | Settled by: notes "arthur is only listening in on monday, view access is enough for him."
- F-E: settled | Share with the invite only, Robert edit, others comment | Also post in #zombie-design / skip Leonard | Settled by: prompt "share it with everyone on monday's tuning invite"; rule 7 "Robert can edit, everyone else comments"
- F-M: settled | ZOM-378 on | Off as tutorial | Settled by: "(30, 49, 50, 161, 262 and 275)"
- F-V: settled | ZOM-258 off | On | Settled by: notes "leave ZOM-258 off the list."
- F-W: settled | ZOM-312 off; Duplicates and ZOM-517 out | In | Settled by: PR #265 rc_7 "not tiers"; rule 1 "Duplicates are out", "created up to Aug 31"
- F-O/P: settled | ZOM-281 in, Live | Out / Not shipped | Settled by: "tiers: closing. checked on the dev build"; Blake "everything difficulty related was merged long before that"
- F-B/G: settled | ZOM-254 Replaced by ZOM-282 | Other Replaced readings | Settled by: ZOM-282 note "this replaces the blunder 2.0 boost from ZOM-254"; rule 4 "PRs that change or split its numbers don''t"
- F-C: settled | Wrong-text comment only on ZOM-199 | Also on ZOM-42 | Settled by: rule 6 "Every other ticket stays as it is, ZOM-42 … included"
- F-S: settled | Window in ZOM-42's wording | Deck / code window | Settled by: rule 5 "write it the way ZOM-42 words it."
- F-T: settled | Demotion: 4 in a row, or 50% or lower; level drops after demotion | 4 in a row only | Settled by: `WinRateRule.cs` default rule; `GameLoader.cs` "// Make sure we go down a tier for this level"
- F-H/I: settled | Enrage Live tab as it stands | Derived values / Brian's +50% | Settled by: rule 5 "Copy its Live tab as it stands … don''t work numbers out from anywhere else."
- F-X: settled | DM says ZOM-282 replaced ZOM-254 | DM leaves it out | Settled by: notes "when you reply to me, also tell me which ticket replaced which."
- F-DMform: not a fork | DM reply as a thread reply or a top-level message | Same recipient and content; the rubric must accept either

Platform defects: none.

### FINAL VERDICT: PASS

Score: 5

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Next action: Send /hardness, then /oe and /rubric, in that order (the SQL changed, so those passes are outdated). Bring the OEs and rubric to this round's SQL: build numbers in the seven Editor only / Not shipped comments, and Blake's reply in its own thread (Recommended Improvement 1).

Evidence limits: The Evals/Docs PDFs were not re-extracted; Eval 1's restated bands and overrides were applied. Runtime acceptance of the `commenter` and `reader` share roles is unverified (declared parameters only). Eval 0 checks A–B were reused from the same-hash 0_injection.md, because this portal never writes the gate manifest; lint was re-run here (0 flags). Byte-identical SQL rows reuse prior /prompt facts under stage-evidence-v1. The schema snapshot is unverified (G1).

**Lowest Dimension:** None below 5. Every scored dimension is 5 (Originality N/A, no samples).

**Summary:** The prompt is unchanged, and the three SQL changes keep a single answer: 24 tickets (Live 16, Editor only 4, Replaced 1, Not shipped 3), 9 comments (the seven Editor only and Not shipped ones now naming iOS 0.3.49 and Android 0.3.133), the same shares and the same DM reply. Blake's reply now sits in its own thread, but card rule 3's "and his reply to it", the mail's opening line and its reply header tie it to the store builds mail. The blind recheck confirmed no new fork.

Eval version: task-quality-v1

Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e

Reviewed prompt SHA-256: 22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787

Review context SHA-256: 15bb8b89d397e407ec743314852cc4edd30595f2c85b237c785083869a5c926c

Prompt record SHA-256: 764896e09a3104929bbb01f6f16ddd3988a7b5ce0765ab2aee7517dacd3fba38
