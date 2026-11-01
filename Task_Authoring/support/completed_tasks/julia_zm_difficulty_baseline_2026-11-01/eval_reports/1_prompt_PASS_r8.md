## PROMPT EVALUATION REPORT

### Task: Julia delegates Leonard's ZM difficulty baseline: build the register (Tickets + Rules in force) from the Trello card rules, its "Before Monday" checklist and Leonard's DM thread, file it in ZM Difficulty, share it with the Monday invite, comment on tickets per rule 6 as changed, reply to Leonard in the DM with counts, keys and when a new player gets their starting tier
### Assigned Persona: Julia Lawson - Product Manager (roster `julia_lawson`, julia.lawson@harmonygames.co)
### Assigned Business Function: Product
### Assigned Competency: Engineering Ops
### Assigned Task Skill: Retrieval
### Assigned Horizon: long-horizon (Task Type field; Difficulty Mode "medium" recorded as context)

Review: `/prompt`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode. Actual review date 2026-10-30. Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe `Universe_SynthCut` (hg4-synth-sep30cut v16), manifest sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`. Eval release task-quality-v1 (manifest `0040c6a5…9c2e`, verified with `hg_eval_release.py snapshot prompt`). Check record: prompt sha256 `22f26066…1787`, review context `656247c9…0b41`.

Inputs:
- `04_Prompt.txt`: revision 23, 525 bytes, sha256 `22f26066…1787`. Attached as `04_Prompt (8).txt`; byte-identical to the prompt graded in the last two rounds.
- `00_Task_Assigned_Inputs.md`: all five fields stated, which clears intake.
- `01_Universe_Inject.sql`: revision 22, 89,187 bytes, sha256 `52c581f442c120a641e1dc1c7f6b8dd9e4ad089fd9faf5e1a87b7710b4bfba43`. Changed since the last /prompt round (revision 20, `6972a450…858b`). Per the Eval 0 diff, only card #80 rule 5's last sentence changed, identically at line 58 (card `desc`) and line 66 (updateCard `card.desc`):
  - was: "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself; where a write-up and the build disagree, go by the build."
  - now: "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself. For when a new player gets their starting tier, where a write-up and the build disagree, go by the build. For which games promotion and demotion look at, write it the way ZOM-42 words it."
  - Every other row is byte-identical, and no key, author or timestamp changed.
- No error/async config, dynamic context or reference files were supplied, and the prompt references none. A saved Agent trajectory exists in the workspace; under stage ownership it was not opened for this review.
- Evidence contract `stage-evidence-v1`. **Reused:** prior `1_prompt.md` facts for byte-identical SQL rows and base records (ticket scope and statuses, checklist, thread reply, card comment, enrage sheet, Blake's mails, invite, folder, agenda, Linear states, ZOM-281). **NEW:** everything rule 5 touches: ZOM-42 re-read in full (`/issues/3485`), the deck slide (line 37), Blake's rules-tab reply, `TierManager.cs`, `WinRateRule.cs` and `WinHistory.cs` re-read in full, and `GameLoader.cs` (retry tier). Forks K, Q, R and S recomputed; fork T added.
- Line numbers: the report text uses physical (`\n`) SQL lines. The generated UGT section uses the check helper's numbering, which also splits on bare `\r` inside Gmail bodies, so rows after line 78 show higher numbers there (Blake's reply is helper line 129).

**What this round changes.** The prompt is the same and so is the answer, except that the Rules in force tab now has one wording for which games promotion and demotion count: ZOM-42's. That closes last round's only open fork (S). The narrower build clause still covers the one thing the DM asks about (when a new player gets their starting tier), and nothing else that the old blanket clause settled is reopened (Phase 2, forks K, Q, R, T).

---

### Injection Gate
- **State:** NEVER_REVIEWED. The gate reads `reports/input_manifest.json`, which this portal's writer never creates.
- **Eval 0 handling:** `0_injection.md` (injection-static-v2) reviews the identical SQL hash `52c581f4…a43` (revision 22): **FINAL VERDICT: PASS**, COMPLETE (lint: 164 INSERT, 1 UPDATE, 0 FAIL / 0 CHECK / 0 INFO). Static checks A–B are REUSED; the Check C items this prompt depends on were redone here (Phase 3.2).
- **Reviewed SQL sha256:** `52c581f442c120a641e1dc1c7f6b8dd9e4ad089fd9faf5e1a87b7710b4bfba43`. Eval 0 verdict: PASS.
- **Eval 0 downstream advisories on records this prompt depends on:**
  - **D2 (starting-tier timing):** Eval 0 says no record states the build's timing. That search was bounded to text hits. The build file itself states it: `TierManager.cs` line 31 `if (totalGames == 10)` calls `ApplyInitialBucketing()`, and `WinHistory.cs` `GetTotalGames()` returns wins plus losses. Rule 5 says to go by the build for exactly this item, so "after the first 10 games played" is the single supported answer, and ZOM-42's "6-7 levels … to be defined later" is excluded (forks Q, K).
  - **D3 (ZOM-42's window wording and the 50% rule):** ZOM-42 gives the window one way: "UP TO THE MOST RECENT 10 attempts", "we constantly look at the last 10 games played", the record reset "every time a promotion/demotion happens", and a 4-loss streak that "can still trigger at any time". The 50% demotion rule is in the build (`WinRateRule.cs` line 31) and in ZOM-42, so it belongs on the tab (fork T). The pull between "as they work in the store builds today" and "write it the way ZOM-42 words it" is resolved by the later, more specific sentence for this one item (fork S).
  - **D1 (ZOM-281 in scope):** unchanged; ZOM-281 is in and Live (forks O, P).
- **Advisories carried:** A1–A5 (schema-snapshot columns, Trello action `_id` fields and similar). None changes a graded value.

---

### Phase 0: Sources read

Docs and references read: Eval 1 (unchanged release, applied in full); `prompt_rubric_reliability.md` release binding; `deep_recheck.md`; `common_errors.md`; `acl.md`; `roster.json`; tool catalog. The PDFs in `Evals/Docs` were not re-extracted; Eval 1's inline bands and Local Overrides were applied (evidence limit, unchanged from prior rounds).

Universe exploration (synth-cut base plus SQL overlay), NEW this round:
- **Card rule 5 (line 58 = line 66):** "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today. … The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself. For when a new player gets their starting tier, where a write-up and the build disagree, go by the build. For which games promotion and demotion look at, write it the way ZOM-42 words it."
- **ZOM-42 (base Linear `/issues/3485`), its window wording:**
  - Promotion: "Starting at tier -1, we evaluate UP TO THE MOST RECENT 10 attempts of the player" and "we constantly look at the last 10 games played, if at any time win rate is 80%+, we promote"; "Tier -2 is an exception. You promote instantly after 1 win".
  - Demotion: "Lose 4 in a row, you're demoted"; "we demote someone when their win rate for up to the last 10 games is 50% or lower", with early exits.
  - Reset: "every time a promotion/demotion happens, the record is reset and we start at 0 games played"; "A losing streak of 4 games in a row can still trigger at any time, regardless of whatever record."
- **Deck slide (line 37):** "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1 … Promotion: win rate of 80% or more over the last 10 attempts … On tier -2 one win promotes you. Demotion: 4 losses in a row moves you down one tier." (no 50% rule, no level-drop line).
- **Build:**
  - `TierManager.cs`: lines 30–32 bucket at `totalGames == 10`; line 93 `cpm > 90.0f`; lines 146–150 `RetryTierOffset--` on a demotion.
  - `WinRateRule.cs` Defaults: tier ≤ -2 promotes on one win (line 25), ≥ 80% over 10 promotes (28), ≤ 50% over 10 demotes (31), 4 losses demote (34).
  - `WinHistory.cs`: total games = wins + losses; the starting CPM is the running average of the first 10 games; the tier history is appended at the end and cleared on each change, and the win-rate loop counts from index 0 (the code's window is the first games since the last change, which the card now sends to ZOM-42's wording).
  - `GameLoader.cs` lines 97–103: with a retry offset, "Make sure we go down a tier for this level". So after a demotion, the level is replayed lower until a win: at the new tier's version plus the offset, which is below the new tier. No write-up describes this.
- **Blake's reply (physical line 107):** "One more, for the rules tab: the starting tier check in the build is cpm > 90, not >= 90. ZOM-199 says >= but the code never changed from the original spec, so 90 exactly stays on tier 0."

Status derivation (shows solvability, not a golden answer; REUSED from byte-identical rows):
- **Live 17:** ZOM-23, 42, 45, 199, 221, 246, 258, 263, 274, 281, 282, 288, 295, 300, 303, 305, 378.
- **Editor only 9:** ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315.
- **Replaced 1:** ZOM-254, replaced by ZOM-282.
- **Not shipped 3:** ZOM-202, 280, 293.
- **Total 30** = 31 title matches minus Duplicates ZOM-203 and ZOM-276, plus the five "tiers:" tickets ZOM-221, 281, 300, 305, 378 (36), minus ZOM-30, 49, 50, 161, 262, 275.
- **Comments (14):** ZOM-199 (what the build does: cpm > 90), ZOM-254 (replaced by ZOM-282), and the 12 Editor only and Not shipped tickets (the change isn't in the store builds).
- **Shares:** robert@ and brian.foster@ can edit; leonard.hayes@ and arthur.blake@ can comment.
- **Rules in force (NEW wording):** starting tier after the first 10 games played, from their average CPM, above 90 to tier 1, everyone else tier 0. Promotion at 80% or more over up to the most recent 10 attempts, and on tier -2 one win promotes. Demotion on 4 losses in a row at any time, or 50% or lower over up to the last 10 games. The record resets after every promotion or demotion. After a demotion, the level being played is replayed lower until a win. Enrage: the sheet's Live tab as it stands.
- **DM reply:** total 30, the four status counts, the keys of the 3 Not shipped and 9 Editor only tickets, and when a new player gets their starting tier.

---

### Requirement ledger

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Find Leonard's Tuesday DM ask, including his thread reply | SQL lines 44 and 50 (D05HB64NMQU, 19:48:26Z and 20:07:18Z) | Slack DM history; thread via reply_count | `slack_conversations_history`, `slack_conversations_replies` / `slack_read_thread`, search | Julia is a DM member | The ask: register; six tickets off; reply with total, per-status counts, the Not shipped and Editor only keys, and the starting-tier timing |
| "everything it points to": card rules | Card #80 (line 58), updateCard (66), commentCard (68), checklist and items (70–76) | DM names "the difficulty baseline card on the zm roadmap board" | `trello_get_cards_on_board`, `trello_get_card`, `trello_get_comments`, `trello_get_checklist` | Trello unscoped | Rules 1–7 (rule 5 with the starting-tier build clause and the ZOM-42 window clause), the attack-power addendum, and the rule 6 and rule 7 changes |
| Ticket scope | Linear ZOM issues; "tiers:" comments (incl. ZOM-281); Trello comment; DM thread reply | Linear search/list; per-ticket comments | Linear search/get, `linear_list_comments` | Unscoped | 30 tickets |
| Status per ticket (rules 3–4) | Blake's mail and reply; Linear states and closing notes | Gmail search; Linear | Gmail read; Linear reads | Julia's mailbox; unscoped | Live 17 / Editor only 9 / Replaced 1 / Not shipped 3 |
| Rules in force tab (rule 5) | Deck, ZOM-42, Blake's reply, enrage sheet Live tab, `TierManager.cs`, `WinRateRule.cs`, `WinHistory.cs`, `GameLoader.cs` | GSlides, Linear, Gmail, GSheets, GitHub | `gslides_get_presentation_text`, `linear` get, `gsheets_values_batch_get`, `github_get_file_contents` | Deck shared; sheet owned by Julia; GitHub, Linear unscoped | Starting tier after the first 10 games played, cpm > 90; promotion and demotion with ZOM-42's window (both demotion rules); the level drop; enrage Live tab as it stands |
| Build the register: one sheet, tabs Tickets + Rules in force | Agenda doc; card rule 2 | GDocs | `gsheets_create_spreadsheet`, `gsheets_batch_update`, `gsheets_values_update` | Write (ACL-free) | New spreadsheet |
| Put it in the ZM Difficulty folder | Prompt; card rule 7 | Drive folder d_96489e1e00a56685625939 | `gdrive_move_file` (or create with parent) | Julia is writer | File in folder |
| Share with everyone on Monday's invite | Prompt; card rule 7 as changed by the checklist | GCal event on Julia's calendar | `gdrive_share_file` (role param) | Julia's own calendar | robert@ and brian.foster@ writer; leonard.hayes@ and arthur.blake@ commenter |
| Ticket comments (rule 6 as changed) | Card rule 6; checklist item; Blake's reply; rule 4 | Linear | `linear_create_comment` | Write | ZOM-199, ZOM-254 and the 12 Editor only and Not shipped tickets |
| Reply to Leonard in the DM | DM and thread reply | Slack | `slack_send_message` | Write | Total 30, per-status counts, Not shipped and Editor only keys, and that a new player gets their starting tier after their first 10 games (from those games' average CPM) |

Output capability: spreadsheet/tab creation, moving into the folder, sharing, Linear comments and the Slack reply are SUPPORTED by declared catalog tools. The `commenter` role is a free-string parameter with no base example; runtime acceptance UNVERIFIED (evidence limit, not a failure).

---

### Phase 1: Prompt Structure & Persona (prompt text byte-identical; re-judged against the new sources)

**Persona:** PASS (5). The prompt matches the exact roster entry. It is a CEO-to-PM delegation; the card says "Julia owns this one", and Julia owns the enrage sheet.

**Assigned Competency:** PASS (5). Engineering Ops: reconciling tickets with what shipped in store builds, reading the build code for the starting tier, and 14 ticket comments.

**Assigned Task Skill:** PASS (5). Retrieval is the core work: every in-scope ticket (including one found only through a closing note), state, shipped status and rule value, across seven services, with two late instruction layers to find.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS. Data seeding PASS.
- **Dynamic Change:** the checklist changes two card rules after Leonard wrote "rest of the card stands", and the thread reply narrows the scope after the DM.
- **Superseded sources:** the deck's "90 or more" vs Blake's "cpm > 90"; ZOM-42's provisional "6-7 levels" vs the build's 10 games; the deck's 4-loss-only demotion vs the build's and ZOM-42's two rules; the deck's blunder slide vs Arthur's Slack.
- **Decoys:** Brian's "+50% … every monster" and "the editor bits too"; Domino card #211; the "Next pass" tab; Vincent's channel request; ZOM-281 having no PR; the code's own first-games window against ZOM-42's wording.

**Naturalness:** PASS. First person, lowercase and casual, with no document formatting, polished connectives or enumerated specs.

**Anti-Patterns:**
| Pattern | Status |
|---------|--------|
| Command List | PASS. One lowercase "then" with no first/finally, and the order is Leonard's own condition ("reply here when it''s in the folder") |
| Bolt-On | PASS. Every sentence serves the baseline |
| Pre-Solving | PASS. No counts, tickets, statuses, exclusions, timings or causes named |
| Tool Mention | PASS. "dm", "folder", "invite" and "tickets" are natural nouns |

**Diversity:** a two-tab sheet, folder placement, role-based sharing, a 14-ticket Linear comment batch and a DM reply over a 30-ticket cohort with a rules answer.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** PASS (5). Every fork resolves to one end state.
- **S (last round's open fork), now excluded:** the promotion/demotion window. Rule 5's new sentence names this exact item and the wording to use: "For which games promotion and demotion look at, write it the way ZOM-42 words it." ZOM-42 is consistent across its promotion, demotion and streak paragraphs: up to the most recent 10 attempts, the record reset on every change, and a 4-loss streak at any time. The later, more specific sentence governs the opening "as they work in the store builds today" for this item, just as the enrage sentence governs the enrage rows (H).
- **T (new), excluded:** with the build clause narrowed to the starting tier, could the tab follow the deck's demotion line (4 losses only)? No. Rule 5 opens with "as they work in the store builds today", the build has the 50% rule (`WinRateRule.cs` line 31), and ZOM-42 has it too. The deck is silent on that rule rather than contrary to it, so no tie-break is needed.
- **K and Q (starting-tier timing), still excluded:** the narrowed clause names exactly this item ("For when a new player gets their starting tier … go by the build"), and the build buckets at `totalGames == 10` (wins plus losses).
- **R (threshold), still excluded:** Blake's reply is addressed "for the rules tab" and says cpm > 90, not >= 90, so 90 exactly stays on tier 0. It matches the build (`cpm > 90.0f`) and rule 5's opening clause.
- **Not a fork:** the level drop after a demotion. No write-up describes it; `GameLoader.cs` replays the level lower after a demotion, and rule 5's opening asks for it as the build works. The yes/no answer is single; the size of the drop is an unsettled edge (deep recheck P1), so it isn't graded.
- **B–P:** excluded on byte-identical rows, as last round.

### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: Every fork resolves to one end state. S (the promotion/demotion game window, last round's open fork) is now excluded by card rule 5's new sentence 'For which games promotion and demotion look at, write it the way ZOM-42 words it'; ZOM-42 words it as up to the most recent 10 attempts, the record reset on each change and a 4-loss streak at any time. T (deck-only demotion) is excluded by rule 5's 'as they work in the store builds today', WinRateRule.cs line 31 and ZOM-42's 50% rule. K and Q (starting-tier timing) are excluded by rule 5's starting-tier build clause and TierManager.cs 'if (totalGames == 10)'; R (threshold) by Blake's rules-tab reply and 'cpm &gt; 90.0f'. B to P stay excluded on byte-identical rows. End state: 30 tickets (Live 17, Editor only 9, Replaced 1, Not shipped 3), 14 comments, four shares, the DM answer.

Alternative selection: B to R are every fork from earlier rounds, recomputed for the revision-22 overlay (only card rule 5's last sentence changed, at SQL lines 58 and 66; every other row is byte-identical to revision 20). S is last round's open fork (the promotion/demotion window), retested against the new 'write it the way ZOM-42 words it' sentence. T is new: with the go-by-the-build sentence narrowed to the starting tier, the deck's 4-loss-only demotion line is the strongest reading the narrowing could reopen. K, Q and R are retested against the narrowed clause (K and Q are timing, which the clause names; R is the threshold, which now rests on Blake's rules-tab note and rule 5's opening). The level drop after a demotion was checked: no write-up describes it and GameLoader.cs replays the level lower after a demotion, so the yes/no answer is single (the size of the drop is not graded).

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Follow the card as Leonard left it, his checklist and his DM thread: scope is every difficulty ticket created up to Aug 31 by title word plus every ticket with Blake's 'tiers:' closing note (ZOM-221, 281, 300, 305, 378), attack power counting only when written out (ZOM-271 out), minus the six analytics and tutorial tickets his DM reply lists; status against Blake's store builds mail (ZOM-281 Done, gameplay, Live); Replaced only where another ticket's closing note says so (ZOM-282 on ZOM-254); comments on ZOM-199 (flagged by Blake's reply), on Replaced ZOM-254 and, per the checklist's rule 6 change, on every Editor only and Not shipped ticket; share with the invite attendees, Robert and Brian as editors; the Rules in force tab gives the starting tier as the build runs it (after the first 10 games played, cpm &gt; 90), promotion and demotion with ZOM-42's game window (up to the most recent 10, 4 in a row at any time, record reset on each change) and copies the enrage sheet's Live tab as it stands; the DM reply gives the total, per-status counts, the Not shipped and Editor only keys and when a new player gets their starting tier. | 30 tickets (six analytics/tutorial tickets off, ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Brian and Robert edit; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 30 rows: the 36 rule-1 tickets (31 title matches without Duplicates ZOM-203 and ZOM-276, plus tiers: tickets ZOM-221, 281, 300, 305, 378) minus the six Leonard leaves off (ZOM-30, 49, 50, 161, 262, 275); Live 17, Editor only 9, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force as the build runs them: starting tier set after the first 10 games played (wins and losses), average CPM above 90 to tier 1, everyone else tier 0 (90 exactly stays on tier 0); promotion and demotion in ZOM-42's wording: 80% or more over up to the most recent 10 attempts (the last 10 games played) promotes, one win on tier -2 promotes; demotion on a losing streak of 4 games in a row at any time or a win rate of 50% or lower over up to the last 10 games; the record resets after every promotion or demotion; after a demotion the level being played is replayed lower (below the new tier) until a win; enrage from the sheet Live tab copied as it stands: nine monster rows and MonsterBase 0.8/0.8 with their numbers, and Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP) as not copied yet; DM gives the total 30, the per-status counts, the keys of the Not shipped (ZOM-202, 280, 293) and Editor only (ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315) tickets, and that a new player gets their starting tier after their first 10 games (levels played), from the average CPM of those games. | CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 298-298): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; SHEET\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 22-22): "\["MonsterBase (base prefab)", "0.8", "0.8", "0"\], \["Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)", "not copied yet", "not copied yet", "0"\]"; TCOMMENT\_W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 68-68): "written out (ATK on its own doesn''t)"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 72-72): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 74-74): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; CARD\_R1B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''"; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 296-296): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"; DMT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 44-44): "tell me when a new player gets their starting tier"; DECK\_PROMO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 37-37): "Promotion: win rate of 80% or more over the last 10 attempts moves you up one tier."; Z42MR (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we evaluate UP TO THE MOST RECENT 10 attempts of the player"; CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; Z42LAST (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we constantly look at the last 10 games played"; Z42STREAK (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "A losing streak of 4 games in a row can still trigger at any time"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"; Z42RESET (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "every time a promotion/demotion happens, the record is reset and we start at 0 games played"; WR\_DEM50 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/WinRateRule.cs lines 31-31): "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"; GL\_RETRY (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Match3D/Game/Levels/GameLoader.cs lines 101-101): "// Make sure we go down a tier for this level"; REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 129-129): "One more, for the rules tab: the starting tier check in the build is cpm &gt; 90, not &gt;= 90." |
| B | match3d\#401 changed how enrage works (speed and damage split per monster, hp method dropped), so ZOM-282 is Replaced by match3d\#401 and gets a Replaced comment. | ZOM-282 Replaced by match3d\#401. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a Replaced comment on ZOM-282 naming match3d\#401. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-282. | Register shows ZOM-282 Replaced; DM counts Live 16, Replaced 2. | GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 191-191): "this gives enrage speed and damage their own values, they shared one since ZOM-282." |
| C | Comment on every listed ticket whose text the store builds contradict, including ZOM-42 (6-7 levels vs 10). | Correction comment also on ZOM-42. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a comment on ZOM-42. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-42. | Extra correction comment; register unchanged. | Z42A (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "gets assigned after the first 6-7 levels based on CPM" |
| D | Read the scope window in Pacific days with an Apr 21 start, dropping ZOM-23 (2025-04-21T04:51:38Z, Apr 20 PT); ZOM-30 is already off under Leonard's DM reply. | 29 tickets; ZOM-23 out. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Register 29 rows; DM total 29 and Live 16. | Z23 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3277): "2025-04-21T04:51:38Z" |
| E | Also post the register in \#zombie-design because Vincent asked Julia to drop it there. | Share with the invite and also post in \#zombie-design. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a Slack post in \#zombie-design. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus C090N54TG79. | Same register; extra channel post. | VINCENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "julia when you have the difficulty list can you drop it in here too" |
| F | ZOM-277 (created after ZOM-250) changed how ZOM-250's average attack power works, so ZOM-250 is Replaced by ZOM-277 and gets a Replaced comment. | ZOM-250 Replaced by ZOM-277. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the eleven Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a Replaced comment on ZOM-250 naming ZOM-277. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Register shows ZOM-250 Replaced; DM counts Editor only 8, Replaced 2; ZOM-250 drops out of the Editor only keys. | Z250 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3300): "(This is per set of items)"; Z277 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3329): "The average power should really be 334 / 5 uniques" |
| G | ZOM-254 was closed (2025-06-23) after ZOM-282 (2025-06-21) and its own QA note says blunder enrages the monsters, so ZOM-282 is not the 'later' ticket and ZOM-254 stays Live with no Replaced comment. | ZOM-254 Live; no Replaced ticket. | Same as A without the ZOM-254 comment. | Same as A without Linear ZOM-254. | Register shows ZOM-254 Live; DM counts Live 18, Replaced 0. | Z254C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 274-274): "checked on the dev build, blunder enrages the monsters on the board now" |
| H | Rule 5 asks for enrage as it works in the store builds today, so the three monsters the sheet has not copied are given what they actually run on in main: no own override, so MonsterBase's 0.8 speed / 0.8 damage. | 30 tickets (six analytics/tutorial tickets off, ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Brian and Robert edit; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same 30 rows and counts as A; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab, with Mailman, Mayor2 and PartyGirl given 0.8 speed / 0.8 damage (MonsterBase) instead of not copied yet; DM as A. | CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; MB\_ENRAGE (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/MonsterBase.prefab lines 342-343): "enrageSpeedPercentage: 0.8" |
| I | Fill the gap from the VarC prefabs the History tab says the Live tab was copied from: VarC-PartyGirl carries enragePercentage 0.6, so PartyGirl is 0.6 speed / 0.6 damage; Mailman and Mayor2 show no enrage value in their prefab text. | 30 tickets (six analytics/tutorial tickets off, ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Brian and Robert edit; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same 30 rows and counts as A; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab, with PartyGirl at 0.6 / 0.6 and Mailman and Mayor2 without numbers; DM as A. | SHEET\_HIST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 26-26): "\["2025-09-08", "Live tab copied from the VarC prefabs in main", "Julia"\]"; PG\_PREFAB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/VarC-PartyGirl.prefab lines 215-216): "propertyPath: enragePercentage" |
| J | Leonard's comment adds attack power in the title; ZOM-271's title says 'ATK POWER' / 'ATK Power', and 'ATK on its own' is read as ATK without 'power', so ZOM-271 (Done, June 16, card-profile stat display) is in scope as Live. | 31 tickets; ZOM-271 Live; otherwise as A. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 31 rows (adds ZOM-271); Live 18, Editor only 9, Replaced 1, Not shipped 3; DM total 31 and Live 18. | TCOMMENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 68-68): "attack power in the title counts too"; Z271 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3323): "Comprehensive Item Stat Display Rules also ATK POWER BUG. Also Change Damage sort to ATK Power sort" |
| K | Take the starting-tier window from the written rules (deck, ZOM-42, ZOM-199): average CPM over the player's first 10 levels read as ten distinct levels, so replays of a lost level don't count; &gt; 90 to tier 1, the rest tier 0. | 30 tickets (six analytics/tutorial tickets off, ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Brian and Robert edit; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register and counts as A; Rules in force and the DM answer give the starting tier as after the first 10 distinct levels (replays not counted), instead of after the first 10 games played (wins and losses) as the build counts them. | Z42S (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "1st 10 level avg CPM &gt; 90 (top 20%) moves to tier 1, rest stays in tier 0)"; DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 37-37): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0." |
| L | The 'Before Monday' checklist items are unchecked, so they are Leonard's pending notes, not rules in force; card rules 6 and 7 as written stand: comments only on ZOM-199 and ZOM-254, with the Not shipped and Editor only tickets left as they are, and only Robert edits. | Checklist not applied: two comments; Brian comments only. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and leonard.hayes@, arthur.blake@ and brian.foster@ as commenters; post Linear comments on ZOM-199 and ZOM-254 only; reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. | Same 30 rows and counts; no comments on the twelve Editor only and Not shipped tickets; brian.foster@ as commenter. | CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CL\_NAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 70-70): "'Before Monday', '68daca5871dba40417a00383'" |
| M | ZOM-378 'Level 1 is removed and creates tutorial order problems' is a tutorial ticket, so it goes off the list with the other analytics and tutorial tickets Leonard named. | 29 tickets; ZOM-378 off. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 29 rows; Live 16; DM total 29 and Live 16. | DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3440): "It creates other important issues like wrong tutorials at the wrong spot." |
| N | Leonard's reason 'they don't change how hard a level plays' is the test, so every ticket that only touches editor or debug tooling is left off too (ZOM-162, 163, 173, 200, 201, 202, 250, 277, 312, 315), with no comments on them. | Editor-tooling tickets off the list; no comments on them. | As A without the comments on the editor-tooling tickets. | As A without those Linear tickets. | About 20 rows; no Editor only rows; DM without Editor only keys. | DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 85-85): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not." |
| O | ZOM-281 is assigned to someone else (usr\_EMPLOYEE\_0032), so it isn't one of Blake's tickets and its 'tiers:' note doesn't bring it in; its title has none of rule 1's words, so it stays off the list. | 29 tickets; ZOM-281 out. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 29 rows; Live 16; DM total 29 and Live 16. | Z281 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "Win streak not lost when replaying without main menu" |
| P | No PR or commit in match3d names ZOM-281, so it counts as never merged and goes on the list as Not shipped, with the checklist's not-in-the-store-builds comment. | 30 tickets; ZOM-281 Not shipped; extra comment on ZOM-281. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a not-in-the-store-builds comment on ZOM-281. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-281. | Register shows ZOM-281 Not shipped; DM counts Live 16, Not shipped 4, and ZOM-281 among the Not shipped keys. | CARD\_R1NS (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "open, cancelled and never-merged ones are in, as Not shipped" |
| Q | Answer Leonard's starting-tier question from ZOM-42's line that players get assigned after the first 6-7 levels, and put that on the Rules in force tab. | 30 tickets (six analytics/tutorial tickets off, ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Brian and Robert edit; starting tier after the first 6-7 levels, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register and counts as A; Rules in force and the DM answer say a new player gets their starting tier after the first 6-7 levels. | Z42A (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "gets assigned after the first 6-7 levels based on CPM" |
| R | Use the written threshold from the deck and ZOM-199: average CPM of 90 or more starts a player on tier 1. | 30 tickets (six analytics/tutorial tickets off, ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Brian and Robert edit; starting tier after the first 10 games played, average CPM of 90 or more to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register and counts as A; Rules in force (and any threshold in the DM answer) give 90 or more to tier 1, so 90 exactly goes to tier 1. | DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 37-37): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0." |
| S | Card rule 5 asks for promotion and demotion 'as they work in the store builds today'. The build's tier history is appended at the end and cleared on every tier change, and the win-rate check counts from index 0, so promotion and demotion are judged on the first 10 (and first 4) games since the last tier change, not the most recent ones. The Rules in force tab says that. | 30 tickets (six analytics/tutorial tickets off, ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Brian and Robert edit; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 30 rows: the 36 rule-1 tickets (31 title matches without Duplicates ZOM-203 and ZOM-276, plus tiers: tickets ZOM-221, 281, 300, 305, 378) minus the six Leonard leaves off (ZOM-30, 49, 50, 161, 262, 275); Live 17, Editor only 9, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force as the build runs them: starting tier set after the first 10 games played (wins and losses), average CPM above 90 to tier 1, everyone else tier 0 (90 exactly stays on tier 0); promotion and demotion judged on the first games played since the last tier change, not the latest: 80% or more over the first 10 games on the tier promotes, on tier -2 only if the first game there is a win; 50% or lower over the first 10, or losing the first 4 games on the tier, demotes; a player who does neither in those games stays on the tier; enrage from the sheet Live tab copied as it stands: nine monster rows and MonsterBase 0.8/0.8 with their numbers, and Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP) as not copied yet; DM gives the total 30, the per-status counts, the keys of the Not shipped (ZOM-202, 280, 293) and Editor only (ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315) tickets, and that a new player gets their starting tier after their first 10 games (levels played), from the average CPM of those games. | CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; WH\_LOOP (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 46-46): "for (int i = 0; i &lt; gamesCount; i++)"; WH\_APPEND (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 160-160): "tierWinHistory += win ? "W" : "L";"; WH\_RESET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 26-26): "PlayerPrefs.SetString(TierWinHistoryKey, "");"; TM\_RULE (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 121-121): "WinHistory.GetWorstTierWinRatePossible(rule.NumGames) : WinHistory.GetBestTierWinRatePossible(rule.NumGames)" |
| T | Rule 5's go-by-the-build sentence now covers only the starting tier, so for demotion follow Robert's deck, the first write-up rule 5 names: demotion is 4 losses in a row only, with no 50%-or-lower rule; the window wording still follows ZOM-42. | 30 tickets (six analytics/tutorial tickets off, ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Brian and Robert edit; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 30 rows: the 36 rule-1 tickets (31 title matches without Duplicates ZOM-203 and ZOM-276, plus tiers: tickets ZOM-221, 281, 300, 305, 378) minus the six Leonard leaves off (ZOM-30, 49, 50, 161, 262, 275); Live 17, Editor only 9, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force as the build runs them: starting tier set after the first 10 games played (wins and losses), average CPM above 90 to tier 1, everyone else tier 0 (90 exactly stays on tier 0); promotion and demotion in ZOM-42's wording: 80% or more over up to the most recent 10 attempts (the last 10 games played) promotes, one win on tier -2 promotes; demotion only on a losing streak of 4 games in a row (no 50%-or-lower rule); the record resets after every promotion or demotion; after a demotion the level being played is replayed lower (below the new tier) until a win; enrage from the sheet Live tab copied as it stands: nine monster rows and MonsterBase 0.8/0.8 with their numbers, and Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP) as not copied yet; DM gives the total 30, the per-status counts, the keys of the Not shipped (ZOM-202, 280, 293) and Editor only (ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315) tickets, and that a new player gets their starting tier after their first 10 games (levels played), from the average CPM of those games. | CARD\_R5WU (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself."; DECK\_DEM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 37-37): "Demotion: 4 losses in a row moves you down one tier." |

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
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 298-298): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Replaced vs Live for ZOM-254. |
| writes | DIFFERENT | G drops the ZOM-254 comment. |
| destinations | DIFFERENT | G drops Linear ZOM-254. |
| contents | DIFFERENT | Status and DM counts differ (Live 17 / Replaced 0). |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The rule no longer says 'later', so close dates cannot reverse it; ZOM-282's note names ZOM-254 explicitly, which is what the rule asks for.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 298-298): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"

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
Resolution: EXCLUDED. Rule 5 asks for the tier rules as they work in the store builds today and says that for when a new player gets their starting tier, where a write-up and the build disagree, go by the build. The build buckets a player when total games reach 10, and total games are wins plus losses, so the window is the first 10 games played. Leonard's DM asks for the tier numbers 'as they are today', so the DM answer follows the same build fact. 'First 10 levels' read as level plays is the same answer; only 'ten distinct levels' differs, and the build clause excludes it.
Resolution evidence: CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; WH\_GAMES (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 147-147): "return GetTotalWins() + GetTotalLosses();"; DMNUM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 44-44): "plus the tier and enrage numbers as they are today"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and share list. |
| writes | SAME | Same spreadsheet, shares, Linear comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | Starting-tier window on the Rules in force tab and in the DM answer: first 10 games played (A) vs first 10 distinct levels (K). |

Authority chain: P → DMR → CARD\_R5W

Resolution relevance challenge: Not a strawman: three records (deck, ZOM-42, ZOM-199) say 'first 10 level(s)'. The card's own criterion is how the rules work in the store builds, and the build code fixes the unit as games, wins and losses.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied.
Challenge evidence: CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; WH\_GAMES (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 147-147): "return GetTotalWins() + GetTotalLosses();"

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
Resolution evidence: DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 366-366): "tiers: closing. level 1 is back in the list so the first levels line up with their tier versions again"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-378 on vs off. |
| writes | SAME | ZOM-378 is Live and gets no comment either way. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | One row fewer; DM total 28 and Live 15. |

Authority chain: P → DMX

Resolution relevance challenge: Not a strawman: ZOM-378's title says 'tutorial order problems' and its description is about tutorials. But the DM gives an explicit list, and the tiers: note quoted ties ZOM-378 to tier level versions, which is difficulty.
Delegation challenge: NOT_CLAIMED. No alternative scope is authorized.
Challenge evidence: DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 366-366): "tiers: closing. level 1 is back in the list so the first levels line up with their tier versions again"

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

Compared alternative: O
Resolution: EXCLUDED. Rule 1 now brings in 'any ticket Blake counts as tier work even if the title doesn't say so', marked by his closing note starting 'tiers:'; it does not require Blake to be the assignee. The ZOM-281 note is by usr\_cc3e90160f490686, which Linear /users/35 maps to arthur.blake@, and it starts 'tiers: closing.', 22 minutes before ZOM-281 was completed.
Resolution evidence: CARD\_R1B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''"; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 296-296): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; LUSR\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /users/35): "arthur.blake@harmonygames.co"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | O drops ZOM-281. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rows and counts differ by one (29 / Live 16). |

Authority chain: P → DMR → CARD\_R1B

Resolution relevance challenge: Not a strawman: ZOM-281's assignee is another person and the old rule 1 wording tied scope to Blake's own tickets. The current rule 1 keys on the note, and the note's author id is Blake's.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R1B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''"; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 296-296): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; LUSR\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /users/35): "arthur.blake@harmonygames.co"

Compared alternative: P
Resolution: EXCLUDED. Card rule 3 makes Blake's store builds mail the authority for what is in the store builds and what counts as shipped. The mail says both store builds were cut from main on Sep 26 and everything difficulty related was merged long before that; it strips only level editor and debug code, and ZOM-281 (win streak on replay) is a gameplay fix. ZOM-281 is Done, completed 2025-06-27, and Blake's closing note says it was checked on the dev build. Rule 1's 'never-merged' covers work that never landed, not a Done ticket the shipped-authority calls merged.
Resolution evidence: CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that."; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 85-85): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 296-296): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; Z281D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "2025-06-27T09:56:19Z"; Z281 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "Win streak not lost when replaying without main menu"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Live vs Not shipped for ZOM-281. |
| writes | DIFFERENT | P adds a ZOM-281 comment. |
| destinations | DIFFERENT | P adds ZOM-281. |
| contents | DIFFERENT | Status cell, DM counts and Not shipped keys differ. |

Authority chain: P → DMR → CARD\_R3 → MAIL\_MERGED

Resolution relevance challenge: Not a strawman: a complete GitHub scan finds no 'ZOM-281' string, so an Agent looking for a merged PR finds none. The card names the mail as the shipped authority and the mail answers the question for difficulty work as a class.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that."; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 85-85): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 296-296): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; Z281D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "2025-06-27T09:56:19Z"; Z281 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "Win streak not lost when replaying without main menu"

Compared alternative: Q
Resolution: EXCLUDED. ZOM-42's 6-7 levels line is provisional ('to be defined later') and the same ticket's rule 1 gives the first 10 levels' average CPM; the deck and ZOM-199 also say first 10. Card rule 5 says that for when a new player gets their starting tier, where a write-up and the build disagree, go by the build, and the build buckets a player when total games reach 10. Leonard's DM asks for the tier numbers as they are today.
Resolution evidence: Z42TBD (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "to be defined later"; Z42S (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "1st 10 level avg CPM &gt; 90 (top 20%) moves to tier 1, rest stays in tier 0)"; DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 37-37): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; DMNUM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 44-44): "plus the tier and enrage numbers as they are today"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Starting-tier timing on the Rules in force tab and in the DM answer: 10 games vs 6-7 levels. |

Authority chain: P → DMR → CARD\_R5W

Resolution relevance challenge: Not a strawman: ZOM-42 is the system ticket rule 4 sends to the rules tab, and its 6-7 sentence is the only text that answers 'when' in so many words. Its own 'to be defined later', its own rule 1, the deck, ZOM-199 and the build all give 10.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: Z42TBD (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "to be defined later"; Z42S (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "1st 10 level avg CPM &gt; 90 (top 20%) moves to tier 1, rest stays in tier 0)"; DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 37-37): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; DMNUM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 44-44): "plus the tier and enrage numbers as they are today"

Compared alternative: R
Resolution: EXCLUDED. Blake's reply is written 'for the rules tab' and says the build checks cpm &gt; 90, not &gt;= 90, so 90 exactly stays on tier 0; card rule 5 asks for the starting tier 'as they work in the store builds today', and rule 6 has the ZOM-199 comment say what the build does; TierManager.cs line 93 is 'cpm &gt; 90.0f'. Rule 5's narrowed build clause covers when the starting tier is given, so the threshold rests on the rules-tab note and the opening clause.
Resolution evidence: REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 129-129): "One more, for the rules tab: the starting tier check in the build is cpm &gt; 90, not &gt;= 90."; REPLY90 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 129-129): "so 90 exactly stays on tier 0"; CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set (the ZOM-199 comment is in both). |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Threshold: above 90 vs 90 or more. |

Authority chain: P → DMR → CARD\_R5B

Resolution relevance challenge: Not a strawman: the deck and ZOM-199 both say 90 or more. Blake's reply, addressed to the rules tab, and the build say otherwise, and rule 5 asks for the starting tier as it works in the store builds.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 129-129): "One more, for the rules tab: the starting tier check in the build is cpm &gt; 90, not &gt;= 90."; REPLY90 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 129-129): "so 90 exactly stays on tier 0"; CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"

Compared alternative: S
Resolution: EXCLUDED. Card rule 5 (revision 22) now settles this item directly: 'For which games promotion and demotion look at, write it the way ZOM-42 words it.' ZOM-42 words the window as up to the most recent 10 attempts / the last 10 games played, with the record reset after every promotion or demotion, and says a losing streak of 4 in a row can still trigger at any time. The later, more specific sentence in the same rule governs the opening 'as they work in the store builds today' for this one item, the same way rule 5's enrage sentence governs the enrage rows (fork H). The code's first-10-since-the-last-change window is therefore not what the tab states.
Resolution evidence: CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; Z42MR (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we evaluate UP TO THE MOST RECENT 10 attempts of the player"; Z42LAST (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we constantly look at the last 10 games played"; Z42RESET (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "every time a promotion/demotion happens, the record is reset and we start at 0 games played"; Z42STREAK (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "A losing streak of 4 games in a row can still trigger at any time"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rules in force tab: promotion and demotion over the latest 10 (and 4 in a row at any time) vs over the first 10 and first 4 games since the last tier change. |

Authority chain: P → DMR → CARD\_R5PD

Resolution relevance challenge: Not a strawman: last round's deep recheck passes P1 and P2 raised it and it failed UGT. The new card sentence names exactly this item ('which games promotion and demotion look at') and names ZOM-42 as the wording to use, and ZOM-42 states the window in one consistent way across its promotion, demotion and streak paragraphs.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card names the wording to use.
Challenge evidence: CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; Z42MR (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we evaluate UP TO THE MOST RECENT 10 attempts of the player"; Z42STREAK (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "A losing streak of 4 games in a row can still trigger at any time"

Compared alternative: T
Resolution: EXCLUDED. Rule 5 opens by asking for promotion and demotion 'as they work in the store builds today', and the build has the 50%-or-lower demotion rule (WinRateRule.cs line 31). ZOM-42, the other write-up rule 5 names and the one it sends promotion/demotion wording to, has the same rule. The deck's demotion line omits it; it does not say there is no such rule, so there is no write-up/build disagreement for a tie-break to settle. Both demotion rules go on the tab.
Resolution evidence: CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; WR\_DEM50 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/WinRateRule.cs lines 31-31): "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"; CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; DECK\_DEM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 37-37): "Demotion: 4 losses in a row moves you down one tier."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rules in force demotion: two rules (4 in a row, or 50% or lower over up to the last 10) vs the 4-loss rule only. |

Authority chain: P → DMR → CARD\_R5B

Resolution relevance challenge: Not a strawman: the narrowed build clause no longer covers demotion, and the deck is a named write-up whose demotion line lists only the 4-loss rule. It is excluded because the deck is silent on the 50% rule rather than contrary, while the build and ZOM-42 both have it and rule 5 asks for the rules as they work in the store builds.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card names the wording to use.
Challenge evidence: CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; WR\_DEM50 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/WinRateRule.cs lines 31-31): "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"; DECK\_DEM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 37-37): "Demotion: 4 losses in a row moves you down one tier."

Strongest-alternative challenge (S): S is still the strongest alternative, because rule 5 opens with 'as they work in the store builds today' and the code counts the first games since the last tier change. It is now excluded: rule 5's new sentence sends exactly this item, which games promotion and demotion look at, to ZOM-42's wording, which is the most recent 10 with a reset on each change and a 4-loss streak at any time. T, the next strongest, is excluded by the build and ZOM-42 both having the 50% rule.
Challenge evidence: CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; Z42MR (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we evaluate UP TO THE MOST RECENT 10 attempts of the player"; Z42STREAK (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "A losing streak of 4 games in a row can still trigger at any time"; CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; WR\_DEM50 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/WinRateRule.cs lines 31-31): "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

**Feasibility:** PASS (5).
- Every ask maps to cataloged tools, and the needed data exists and is tool-visible: card text, checklist items, the DM thread, sheet cells, Linear states and comments (including ZOM-281's note and ZOM-42's description), mail, calendar attendees and repo files (`TierManager.cs`, `WinRateRule.cs`, `WinHistory.cs`, `GameLoader.cs`).
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
- **Write set:** the same under every surviving reading: one spreadsheet in the folder, four shares (two editors, two commenters), 14 Linear comments (rule 6 with the checklist change, and rule 4), and one DM reply.
- **Rule 5 now reads cleanly item by item:** timing of the starting tier → the build; which games promotion/demotion count → ZOM-42's wording; enrage → the sheet's Live tab as it stands; everything else → as the build works (the thresholds, both demotion rules, the tier -2 rule, whether the level drops).
- **The DM question has one answer:** "tell me when a new player gets their starting tier" is answered by the build (after the 10th game played), which rule 5 names for exactly this item.
- A top-level DM message and a thread reply carry the same content to the same recipient.
- **Not a fork:** ticking the two checklist items after doing them. The prompt doesn't ask for it, and it changes no register, comment, share or reply content.

**Contrived / Unnatural:** PASS (5).
- Destination and audience are named the way the persona knows them.
- No staged typos, opaque IDs, exact timestamps, trap hints, riddles, audit wording or if-chains.
- "if his rules say something needs to happen on the tickets" is one conditional whose rule lives on the card.

**Alignment with Today's Date:** PASS (5). "tuesday" resolves to 2025-09-30: the DM is at 19:48:26Z (12:48 PT) and the thread reply at 20:07:18Z (13:07 PT). "monday's tuning session/invite" resolves to 2025-10-06T17:00Z (10:00 PT).

**Originality:** N/A (no comparison samples supplied).

**Truthfulness:** PASS (5). Premises PR1–PR5 are verified against revision 22 (the DM, folder, card and invite rows keep their keys, authors and times):
- Leonard's Tuesday DM exists;
- the Monday session and its invite exist;
- the ZM Difficulty folder is unique;
- Leonard's rules are on the card the DM names, with the checklist changes and the revision-22 rule 5 wording.

**Tool Use & Cross-service:** PASS (5). Each service changes a graded fact:
- **Slack:** the six-ticket exclusion, the reply's key lists and the starting-tier question.
- **Linear:** the cohort (including ZOM-281 through its note), the states, the Replaced trigger and ZOM-42's window wording.
- **Trello:** the rules, the attack-power scope, the rule 5 clauses, the comment set and Brian's role.
- **Gmail:** shipped vs Editor only, the cpm rule and the ZOM-199 comment.
- **GitHub:** the 10-game starting window, both demotion rules and the level drop.
- **Sheets:** enrage.
- **Calendar:** the share list.

Writes span Sheets, Drive, Linear and Slack.

**Investigation + Action:** PASS (5). **Coherence (Bolt-on):** PASS (5). **Business Function:** PASS (5), Product. **Complexity Dimensions & Data Seeding:** PASS (5).

---

### Phase 3: Universe Feasibility

**Data Existence:** PASS (5). Every needed entity is verified and retrievable through cataloged reads.

**Cross-Service Coherence:** PASS (5).
- **Changed rows (NEW checks):** line 58 desc = line 66 `card.desc`. The new sentences assert no fact. They point at a real difference (ZOM-42's "6-7 levels … to be defined later" vs its own "1st 10 level" and the build's 10 games) and name ZOM-42, an existing Done ticket whose window wording is internally consistent. Nothing in the new text conflicts with rule 6 (Blake's mail and reply flag only ZOM-199), the checklist (rules 6 and 7 only) or Leonard's comment (rule 1).
- **The code's window vs ZOM-42's wording:** `WinHistory.cs` counts from the oldest game since the last change, while ZOM-42 and the method's doc comment say the latest. The card now tells the reader which one the tab states. A build that differs from its write-up is the situation rule 5 is written for, not inconsistent data.
- **ZOM-42's "6-7 levels" (base Linear):** provisional, marked "to be defined later", and overtaken by the same ticket's "1st 10 level" and by the build. Not a Snowflake/Confluence conflict.
- **Unchanged rows:** REUSED (byte-identical): thread reply and checklist rows, in-scope closing notes, ZOM-281's note, ZOM-282 naming ZOM-254, Slack authors as channel members.
- **Known base-data issues (not scored):** none touched; the task uses no Snowflake or Confluence data.
- **Not task-touched (not scored):** `Monster.cs` passes a single `enrageDamagePercentage`. Keep rubric rows off stacking behaviour.
- Injection SQL considered: Yes. Static integrity evidence: REUSED from `0_injection.md` (same hash, checks A–B); task-relevant Check C items redone above.

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|-----------|--------------|-------------|---------------|
| Prompt | Unique Ground Truth | 5 | S closed by rule 5's ZOM-42 window sentence; T excluded by the build and ZOM-42; K, Q, R by the starting-tier clause, the build and Blake's rules-tab reply; B–P unchanged |
| Prompt | Feasibility | 5 | All asks cataloged; data exists |
| Prompt | Persona ACL Reachability | 5 | Every scoped read visible to Julia |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | Same write set under every reading; each rule 5 item has one source |
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
| Universe | Cross-Service Coherence | 5 | No inconsistent data |

---

### Issues Found

None at fail level or NON-FAIL level. Last round's Issue 1 (fork S) is fixed by the new rule 5 sentence.

### Recommended Improvements (not scored)

1. **Bring the OEs and rubric to revision 22 before /oe and /rubric.**
   - **Scope:** 30 tickets, with ZOM-281 in and Live. ZOM-30, 49, 50, 161, 262 and 275 are off; ZOM-378 is on; ZOM-271 is out.
   - **Counts:** Live 17, Editor only 9, Replaced 1 (ZOM-254, replaced by ZOM-282), Not shipped 3.
   - **Comments (14):** ZOM-199 (the build checks cpm > 90); ZOM-254 (replaced by ZOM-282); the 9 Editor only tickets (ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315) and the 3 Not shipped tickets (ZOM-202, 280, 293), saying the change isn't in the store builds. ZOM-42 and ZOM-281 get none.
   - **Shares:** robert@ and brian.foster@ can edit; leonard.hayes@ and arthur.blake@ can comment.
   - **DM reply:** the total 30, the per-status counts, the Not shipped and Editor only keys, and when a new player gets their starting tier.
2. **Grading the Rules in force tab:**
   - **Starting tier:** credit "after the first 10 levels" or "after 10 games played". Fail "after 6-7 levels". The threshold is above 90, so 90 exactly stays on tier 0.
   - **Promotion/demotion window:** grade it against ZOM-42's wording ("up to the most recent 10" / "the last 10 games", the record reset on each change, a 4-loss streak at any time). Don't fail an answer that also notes the code counts the first games since the last change, as long as the tab states ZOM-42's window. Don't require the code's window.
   - **Demotion:** expect both rules (4 losses in a row; 50% or lower over up to the last 10).
   - **Other items:** on tier -2, one win promotes. After a demotion the level is replayed lower: grade only that it drops, not by how many tiers (the build replays below the new tier, which can be two versions under the one the player lost on). Keep rows off the tier cap (the build's MaxTier is 5; the deck says -2 to +2). Mailman, Mayor2 and PartyGirl (incl. PartyGirl 50HP) go on the tab as not copied yet.
3. **Don't grade ticking the checklist items.** The prompt doesn't ask for it.
4. **Optional wording**, carried from earlier rounds: "then reply to leonard in the dm…" could follow Leonard's own condition and read "once it's in the folder, reply to leonard in the dm with what he asked for." If you change it, put it in your own voice; prompts are screened for AI-written text. A prompt change outdates every pass that reads the prompt.

---

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 7 sentences, 33 forks | 2 | 0 |
| P2 | 7 sentences | 1 | 0 |
| P3 | 7 sentences | 1 | 0 |
| P4 | 7 sentences | 1 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P1 | "if his rules say something needs to happen on the tickets, go ahead and do that too." / "share it with everyone on monday's tuning invite." | Checklist "Before Monday" items "rule 6 change: …" / "rule 7 change: …" (SQL lines 72, 74), state incomplete; card rules 6–7 (line 58); comment "rest of the card stands" 15:41:55Z | common_errors §2 | Unique Ground Truth | REJECTED | Reading B (card as first written) is ruled out by the check items themselves: Leonard, the card's author, labels them "rule 6 change" and "rule 7 change" and gives a reason ("he''ll fix rows during the session"). He added them at 16:20:11Z (addChecklistToCard, line 76), after his 15:41 "rest of the card stands" comment, and his 19:48 DM sends Julia to the card that carries them. His 20:07 reply asks for "the keys of the not shipped ones and the editor only ones so i know who to chase". An unticked "Before Monday" item is a to-do for the card owner ("Julia owns this one"); no record calls the changes pending. Same as fork L, rejected on the same records in earlier rounds. |
| DR2 | P1 | "go through his ask and everything it points to and build the register the way he set it up." | ZOM-200 / ZOM-201 closing notes "closing. works on the dev build" (SQL); Blake's mail (line 81) "A ticket whose changes are only level editor or debug tooling never reached players, Done or not." | common_errors §2 | Unique Ground Truth | REJECTED | Reading B (Not shipped) is ruled out by card rule 1: "open, cancelled and never-merged ones are in, as Not shipped". ZOM-200 and ZOM-201 are Done, and their closing notes say they work on the dev build (merged). Blake's mail puts debug tooling in the same stripped group as the level editor ("only level editor or debug tooling"). Brian's Slack calls the debug menu one of "the editor bits too (tier delete, the stats window, the debug menu)". Rule 4's "stays Editor only or Not shipped" keeps the two statuses apart, and rule 1 has already assigned Not shipped. Both stay Editor only (9 / 3). The pass itself rated it "likely settled by the quotes above". |
| DR3 | P2 | "go through his ask and everything it points to and build the register the way he set it up." | `linear_comments.sequence`, `slides_pages.notes`, `slides_page_elements.table_json` / `ordinal` vs `schema/injection.json` | Eval 0 A1/A2 | Data exists | REJECTED | The bundled schema is an unverified snapshot ("missing/mismatched definitions alone are advisory", schema/README.md). Eval 0 lint shows 0 FAIL and carries these as advisories A1–A2. Not a demonstrated defect; same as DR10/DR11 last round. |
| DR4 | P3 | "if his rules say something needs to happen on the tickets, go ahead and do that too." | Same snapshot columns as DR3 | Eval 0 A1/A2 | Data seeding | REJECTED | Same as DR3. The pass itself marks it advisory with no score impact. |
| DR5 | P4 | "then reply to leonard in the dm with what he asked for." | DM `6f773865…` (line 44) "reply here when it''s in the folder with how many tickets made the list…" | common_errors §3 / §6.6 | Command list | REJECTED | §6.6 defines the failure as a first / then / finally list, and Eval 1 §1.3.1 asks whether the prompt prescribes a step-by-step procedure. Here there is one lowercase "then", with no first or finally, and the order is Leonard's own condition. The pass's own read is reject. The optional rewording stays under Recommended Improvements. |

Effect on verdict: unchanged. No finding confirmed; every dimension stays 5. P1's independent derivation matches the main review: 30 tickets; Live 17 / Editor only 9 / Replaced 1 / Not shipped 3; ZOM-200 and 201 Editor only; starting tier after 10 games played, cpm > 90; the window in ZOM-42's wording; both demotion rules. P1 also raised an edge on the level-drop size (the build replays below the new tier). The yes/no answer is single, so the main review now records the size as ungraded and changed its own wording to avoid locking it in.

Fork list:
- F1 / S: settled | Promotion/demotion over up to the most recent 10, record reset on each change, 4-loss streak at any time | The code's first 10 / first 4 games since the last tier change, or the deck's "last 10 attempts" | Settled by: card rule 5 (line 58) "For which games promotion and demotion look at, write it the way ZOM-42 words it."; ZOM-42 "we evaluate UP TO THE MOST RECENT 10 attempts of the player", "A losing streak of 4 games in a row can still trigger at any time"
- F2 / T: settled | Demotion: 4 in a row, or 50% or lower over up to the last 10 | 4 losses in a row only (deck line 37) | Settled by: rule 5 "as they work in the store builds today"; `WinRateRule.cs` line 31 "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"; ZOM-42 "we demote someone when their win rate for up to the last 10 games is 50% or lower"
- F3 / Q: settled | Starting tier after 10 games | After 6-7 levels | Settled by: rule 5 "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; `TierManager.cs` "if (totalGames == 10)"; ZOM-42 "to be defined later"
- F4 / K: settled | First 10 games played | First 10 distinct levels | Settled by: the same rule 5 clause; `WinHistory.cs` "return GetTotalWins() + GetTotalLosses();"
- F5 / R: settled | cpm > 90 | 90 or more | Settled by: Blake's reply "One more, for the rules tab: the starting tier check in the build is cpm > 90, not >= 90." / "so 90 exactly stays on tier 0"; `TierManager.cs` "case var cpm when cpm > 90.0f:"
- F6 / L (DR1): settled | Checklist in force: 14 comments, Brian edits | Unticked items pending: 2 comments, Brian comments | Settled by: check items "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds" and "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; addChecklistToCard 2025-09-30T16:20:11Z, after "rest of the card stands." at 15:41:55Z
- F7 (DR2): settled | ZOM-200 / 201 Editor only | Not shipped | Settled by: rule 1 "open, cancelled and never-merged ones are in, as Not shipped"; closing notes "closing. works on the dev build"; Blake's mail "only level editor or debug tooling"
- F8: settled | The level is replayed lower after a demotion | It does not drop | Settled by: `GameLoader.cs` line 101 "// Make sure we go down a tier for this level"; `TierManager.cs` lines 146–150 `RetryTierOffset--`. The size of the drop isn't graded.
- F9 / O: settled | ZOM-281 in | Out (assignee isn't Blake) | Settled by: rule 1 "his closing note on those starts with ''tiers:''"; note by arthur.blake@ "tiers: closing. checked on the dev build"
- F10 / P: settled | ZOM-281 Live | Not shipped (no PR names it) | Settled by: rule 3 names Blake's store builds mail; mail "everything difficulty related was merged long before that"
- F11 / M: settled | ZOM-378 on | Off as a tutorial ticket | Settled by: DM reply "(30, 49, 50, 161, 262 and 275)"
- F12 / N: settled | Only the six listed tickets off | Editor-tooling tickets off too | Settled by: DM reply "put the keys of the not shipped ones and the editor only ones"
- F13 / J: settled | ZOM-271 out | In | Settled by: Leonard's comment "written out (ATK on its own doesn''t)"
- F14 / H, I: settled | Enrage Live tab as it stands | MonsterBase 0.8/0.8, PartyGirl 0.6/0.6, Brian's +50% or the deck's +25% | Settled by: rule 5 "Copy its Live tab as it stands … don''t work numbers out from anywhere else."
- F15 / G: settled | ZOM-254 Replaced by ZOM-282 | ZOM-254 Live | Settled by: ZOM-282 note "this replaces the blunder 2.0 boost from ZOM-254"
- F16 / B: settled | ZOM-282 Live | Replaced by match3d#401 | Settled by: rule 4 "PRs that change or split its numbers don''t"
- F17 / F: settled | ZOM-250 Editor only | Replaced by ZOM-277 | Settled by: rule 4 "only when another ticket''s closing note says it replaces this one"
- F18 / C: settled | No comment on ZOM-42 | Correction comment on ZOM-42 | Settled by: rule 6 "Every other ticket stays as it is, ZOM-42 … included"
- F19 / D: settled | ZOM-23 in | Out under a Pacific start | Settled by: scope "so everything since we started ZM"
- F20 / E: settled | Share with the invite only | Also post in #zombie-design | Settled by: prompt "share it with everyone on monday's tuning invite"
- F21: settled (P1) | Tier cap not stated, or MaxTier 5 | Deck's -2 to +2 | Settled by: rule 5 "as they work in the store builds today" (`TierManager.cs` "const int MaxTier = 5;"); rule 5 doesn't ask for a cap, so keep rubric rows off it
- F22: not a fork | DM top-level reply | Thread reply | Same recipient and content; accept either
- F23: not a fork | Leave the checklist items unticked | Tick them | Not asked; changes no graded content

Platform defects: none.

### FINAL VERDICT: PASS

Score: 5

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Next action: Send /hardness, then /oe and /rubric, in that order (the SQL changed, so those passes are outdated). Bring the OEs and rubric to revision 22: ZOM-42's window wording and both demotion rules on the Rules in force tab, everything else as before (Recommended Improvements 1–2).

Evidence limits: The Evals/Docs PDFs were not re-extracted; Eval 1's restated bands and overrides were applied. Runtime acceptance of the `commenter` share role (including on a folder Leonard owns) is unverified (declared parameters only). Eval 0 checks A–B were reused from the same-hash 0_injection.md, because this portal never writes the gate manifest. Byte-identical SQL rows reuse prior /prompt facts under stage-evidence-v1. The schema snapshot behind DR3/DR4 is unverified.

**Lowest Dimension:** none below 5. Unique Ground Truth was last round's failing dimension and now passes: the promotion/demotion window has one stated wording (ZOM-42's).

**Summary:** The prompt is unchanged. The only SQL change splits card rule 5's tie-break: go by the build for when a new player gets their starting tier, and write which games promotion and demotion count the way ZOM-42 words it. That closes last round's fork S without reopening anything: starting-tier timing (10 games played) and the threshold (cpm > 90) still have one answer, and both demotion rules belong on the tab. The answer is 30 tickets (Live 17 / Editor only 9 / Replaced 1 / Not shipped 3), 14 comments, four shares and the DM reply. All dimensions score 5.

Eval version: task-quality-v1

Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e

Reviewed prompt SHA-256: 22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787

Review context SHA-256: 656247c9d657cc4fae004dbf3eb704b9be04914349cdb870d93d9be0cdc70b41

Prompt record SHA-256: 3fdaa4a1de523bc956a5e678e9f93527cf18e0976bec4d26face3143c77c5158
